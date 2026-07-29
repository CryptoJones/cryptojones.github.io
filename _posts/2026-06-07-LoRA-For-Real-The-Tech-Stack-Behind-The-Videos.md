---
layout: post
title: "LoRA, For Real: The Tech Stack Behind the Videos"
audio: /audio/posts/LoRA-For-Real-The-Tech-Stack-Behind-The-Videos.mp3
---

**Huge thanks to Ronin 48 and Thomas Wenzke for the initial push to do this.**

*I made two videos about LoRA. One is 90 seconds for people who have never
written a line of code; the other is a 13-minute walk through building adapters
for frontier models. This post is neither of those. The videos use analogies —
"a tiny notepad clipped onto a frozen brain." This post is the actual stack: the
config files, the quantization scheme, the data pipeline, and the GPU bill.*

## The two videos

- **The 90-second version — "LoRA: WTF Is It?"** — zero CS background required:
  [youtube.com/watch?v=XniGimn0Eng](https://www.youtube.com/watch?v=XniGimn0Eng)
- **The full explainer — "Building LoRA Adapters for Frontier Models"** — the
  deep dive:
  [youtube.com/watch?v=2UOfcOxyAfA](https://www.youtube.com/watch?v=2UOfcOxyAfA)

Watch those for the *why*. Read this for the *how*. The code that backs all of
it is the **SELMA** project — an Apache-2.0 legal-reasoning model fine-tuned with
QLoRA — and it's public: [github.com/CryptoJones/SELMA](https://github.com/CryptoJones/SELMA).

## What we're actually building

Full fine-tuning of a 70B-parameter model means updating all 70 billion weights.
That needs the model, its gradients, and optimizer state resident in VRAM at
once — comfortably 1TB+ across a node of A100s. LoRA sidesteps that: freeze every
original weight, and inject a pair of small low-rank matrices (`A` and `B`)
alongside the layers you want to adapt. Only `A` and `B` train. The update to a
weight matrix `W` is approximated as `W + (B·A) · (alpha/r)`, where `r` is the
rank and `alpha` is a scaling term.

QLoRA goes one step further: it loads the frozen base model in **4-bit** so it
fits in a fraction of the memory, then trains the LoRA matrices in higher
precision on top. That's how a 70B model fine-tunes on a single 80GB card
instead of a cluster.

## The base model

```
Base:        meta-llama/Llama-3.3-70B-Instruct
Method:      QLoRA (4-bit NF4 + Low-Rank Adaptation)
Context:     128K tokens (native)
Quantization: NF4 double-quant via bitsandbytes, bf16 compute
```

Llama 3.3 70B is gated, so the pipeline assumes you've accepted the license on
HuggingFace and authenticated (`huggingface-cli login`, or `export HF_TOKEN=...`
before the run). The full rationale for picking this base — license, context
window, provenance — is in the repo's `docs/MODEL_SELECTION.md`.

## The QLoRA config

This is the heart of it. From `configs/training_config.yaml`:

```yaml
quantization:
  load_in_4bit: true
  bnb_4bit_compute_dtype: "bfloat16"
  bnb_4bit_quant_type: "nf4"
  bnb_4bit_use_double_quant: true

lora:
  r: 64
  lora_alpha: 128
  lora_dropout: 0.05
  target_modules: [q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj]

training:
  num_train_epochs: 3
  per_device_train_batch_size: 2
  gradient_accumulation_steps: 8      # effective batch = 16
  learning_rate: 2.0e-4
  lr_scheduler_type: "cosine"
  warmup_ratio: 0.05
  max_seq_length: 4096
  gradient_checkpointing: true
```

A few decisions worth calling out:

- **`r: 64`, `alpha: 128`.** A 2:1 alpha-to-rank ratio is a common, stable
  starting point. Higher rank buys more capacity (and more trainable params) at
  the cost of memory and overfitting risk.
- **Target the whole transformer block, not just attention.** Adapting the MLP
  projections (`gate/up/down_proj`) in addition to the attention projections
  (`q/k/v/o_proj`) consistently helps on knowledge-heavy fine-tunes. Attention-only
  LoRA is cheaper but leaves capability on the table.
- **`gradient_checkpointing: true`** trades compute for memory — it recomputes
  activations on the backward pass instead of storing them. On a 70B QLoRA run
  it's the difference between fitting and OOM.
- **`group_by_length`** batches similar-length sequences together to cut padding
  waste.

## The version you can actually run at home

The 70B run needs an A100/H100. Most people don't have one, so there's a second
config — `configs/training_config_8b.yaml` — that targets **Llama 3.1 8B** and
fits on a single 24GB consumer card:

```yaml
model:
  name: "meta-llama/Llama-3.1-8B-Instruct"
  attn_implementation: "flash_attention_2"
lora:
  r: 32
  lora_alpha: 64
training:
  max_seq_length: 2048      # reduced from 4096 to fit in VRAM
```

Rough wall-clock for the 8B run: ~2–3 hours on an RTX 4090, ~6–8 hours on a free
Colab T4 with `batch_size=1`. This is the one to start with — iterate on 8B,
then scale the recipe to 70B once it works.

## Multi-state architecture: many small adapters, one frozen giant

This is where LoRA stops being a memory trick and starts being an architecture.
Instead of one model that tries to know all 50 states' criminal codes (and
constantly confuses Georgia's assault statute with California's), SELMA trains
**one adapter per jurisdiction** — 50 states plus a federal baseline — all
sharing the same frozen Llama base.

```
models/
├── federal/      # 18 U.S.C. — baseline for every model
├── georgia/      # federal + O.C.G.A. Title 16
├── california/   # federal + Cal. Penal Code
└── ...           # one directory per state
```

The payoff is exactly the "swap the notepad" idea from the video, made concrete:

- **Update independence** — amend Georgia's code, retrain only the Georgia
  adapter. The other 49 are untouched.
- **Deployment flexibility** — an agency ships only the adapter for its
  jurisdiction; the multi-gigabyte base is shared.
- **Less cross-contamination** — a narrow adapter hallucinates less across
  jurisdictions than one overloaded generalist.

Each adapter is a few hundred MB against a ~140GB base. Fifty specialists for
the storage cost of one model plus change.

## The data pipeline

Adapters are only as good as what you feed them. SELMA's training mix:

| Source | What it is | Size |
|---|---|---|
| U.S. Code Title 18 | Federal criminal statutes (USLM XML) | ~2,700 sections |
| State criminal codes | e.g. O.C.G.A. Title 16 | ~500 sections each |
| ALEA US Courts | Federal filings with NOS codes | 491K examples |
| LegalBench | Legal-reasoning benchmark tasks | 91.8K examples |
| CaseHOLD | Holding classification | 585K examples |
| Synthetic | Generated incident→statute mappings | ~50K examples |

The flow is three scripts:

```bash
# 1. fetch raw sources (statutes auto-discovered from the current release)
python scripts/data_collection/fetch_federal_statutes.py
python scripts/data_collection/generate_synthetic.py   # ~50K incident→charge pairs

# 2. combine + split into instruction-tuning JSONL
python scripts/training/prepare_dataset.py
#    -> data/processed/train.jsonl + eval.jsonl

# 3. train
python scripts/training/train_qlora.py --config configs/training_config.yaml
```

The synthetic step is the quiet hero: hand-written statute text teaches the model
*what the law says*, but the ~50K generated incident-to-statute examples teach it
*how to apply the law to a fact pattern* — which is the actual task.

## The training run, and the merge gotcha

On an A100-80GB, the 70B QLoRA run lands around **~72GB VRAM** and **6–10 hours**.
The one that bites people isn't training — it's the merge:

```bash
python scripts/training/merge_adapter.py --config configs/model_config.yaml
```

Merging the LoRA weights back into the base produces a standalone model you can
serve without PEFT — but it loads the full 70B in fp16 **on CPU**, which wants
**~140GB of system RAM**. GPU pods don't have that. The fix is to skip the merge
on the training box (`train.sh --skip-merge`), upload the adapter to HuggingFace,
and merge later on a high-memory CPU instance — or just **serve the adapter
unmerged**, which is the whole point of LoRA anyway.

Deployment ends up trivial: the adapter ships to HuggingFace
([Ronin48LLC/selma-lora-adapter](https://huggingface.co/Ronin48LLC/selma-lora-adapter)),
a GGUF export feeds llama.cpp / LM Studio / Ollama, and `ollama run` serves it
with no Python at all.

## Bonus: how the videos themselves were built

Same spirit — small, scriptable, no proprietary stack. The whole pipeline is
plain Python and CLI tools:

1. **Deck** — generated with `python-pptx`. A house-style palette (WCAG-AAA
   contrast), Calibri, and a PIL/Noto text-fitter that measures each line so
   titles never overflow after the font substitution that happens during render.
2. **Render** — `soffice --headless --convert-to pdf`, then
   `pdftoppm -scale-to-x 1920 -scale-to-y 1080 -png` to get one 1080p frame per
   slide.
3. **Narration** — a cloned voice via ElevenLabs TTS, one MP3 per slide, driven
   by a script split on `[SLIDE N]` markers. (Rule I learned the hard way: render
   one or two sample slides and approve the voice *before* paying for the full run.)
4. **Assembly** — `ffmpeg` stitches each still to its narration with a short
   lead/tail of silence, then concatenates to a single 1920×1080 H.264/AAC file.
5. **Captions** — `faster-whisper` with word timestamps does forced-ish
   alignment: the caption *wording* stays exactly the script's, but the *timing*
   is pulled from the real audio, so subtitles track the voice instead of drifting.

That's it. Two YouTube videos and a 70B legal model, and not one piece of the
stack is closed-source or unavailable to you. The adapters are small, the recipe
is in a YAML file, and the giant stays frozen.

---

*The code: [github.com/CryptoJones/SELMA](https://github.com/CryptoJones/SELMA)
(Apache-2.0). Questions or corrections — find me where I usually am.*
