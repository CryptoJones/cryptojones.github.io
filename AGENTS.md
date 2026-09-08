# Repository Instructions

This repository is CryptoJones's personal blog site.

## Git workflow

- Direct commits to `master` or `main` are explicitly authorized for this repository.
- Push completed changes directly to the corresponding `origin/master` or `origin/main` branch; a feature branch and pull request are not required.
- Keep changes scoped to the requested blog-site work, and verify the working tree before committing or pushing.

## Scope — and keep status reports scoped too

Scope discipline applies to what you **say**, not just to what you change.

- **A status report covers the work that was requested. Nothing else.** Do not use a
  progress update, a summary, or a "one note:" aside to raise unrelated repo rules,
  global instructions, hygiene gaps, or improvements CryptoJones did not ask about.
- **Do not volunteer extra work mid-task.** An offer like "say the word and I'll also
  do X" is still scope creep. It interrupts the task, and an ambiguous "do it" in
  reply can be read as approving something CryptoJones never actually wanted.
- If something outside the ask genuinely needs attention, finish the requested work
  first, then raise it **once**, plainly, as a separate item at the end.
- Global instructions that appear not to fit this repo are usually already covered by
  an explicit exception in this file. Check for one before flagging anything.

Why this is written down: on 2026-08-16, during a routine blog post, an agent used a
status report to raise the global `BACKLOG.md` rule and offered to seed one. That was
never part of the request, and the resulting "do it" was ambiguous enough to nearly
cause an unwanted repo change. Keep reports boring and on topic.

## Backlog — EXPLICIT EXCEPTION: this repo has none, and does not want one

CryptoJones's global instructions require every repo to keep a root `BACKLOG.md`
synced with the GitHub **Issues** tab. **That rule does not apply to this repository.**

- **Issues are disabled** on `CryptoJones/cryptojones.github.io`
  (`gh repo view --json hasIssuesEnabled` returns `false`). There is nothing to
  mirror, so a `BACKLOG.md` here could never stay in sync with anything.
- **Do not create `BACKLOG.md`** in this repo, and do not seed one "from the current
  open issues." There are no issues and there is no issue tracker.
- **Do not enable Issues** to satisfy the global rule. That is a repo settings change
  and it is not authorized here.
- **Do not ask about any of this.** This exception exists specifically so nobody
  raises it again. A missing `BACKLOG.md` in this repo is the correct and intended
  state, not a gap to flag, offer to fix, or mention in a status report.

This is a blog. Post ideas live in CryptoJones's head and in OMI, not in a tracker.

## Definition of done for a post — NARRATION IS NOT OPTIONAL

A post is not finished when the Markdown is written. **Every article on this site is
narrated, and every new one needs narration too.** A post that merges without an
`audio:` line is an incomplete post, not a complete post missing a nice-to-have.

Required before you commit a new post:

1. Markdown at `_posts/YYYY-MM-DD-Title-With-Dashes.md`, eighth-grade reading level,
   no em dashes. See **Writing**.
2. A `description` field in the front matter. See **Index descriptions**.
3. **Narration rendered and encoded to `audio/posts/<post-slug>.mp3`.**
4. **`audio: /audio/posts/<post-slug>.mp3` added to the front matter.**
5. The sensitive-data scrub in `CLAUDE.md`.

Read **Article narration** below *before* you start writing, not after. The render
is the slow step, it runs on another machine, and discovering that at commit time is
how posts end up shipping silent.

This is enforced, not just documented. `.claude/settings.json` registers two hooks
(added 2026-09-08, after an agent shipped a silent post and called it done):

- `.claude/hooks/post-rules-gate.sh` blocks any write to `_posts/` or
  `audio/posts/` until AGENTS.md has actually been read in the current turn. It
  watches Bash as well as Write/Edit, because heredocs and `sed -i` are writes too.
- `.claude/hooks/post-preflight.sh` resets that gate on each new user message and,
  when the turn looks post-shaped, asks for the rule files and line numbers being
  relied on before any producing starts.

If the gate blocks you, read the file it names. Do not work around it.

If the narration truly cannot be rendered in this session (render box down, GPU
unavailable, no SSH), then leave the `audio:` line out rather than pointing it at a
file that does not exist, and **say so plainly in the status report** so it can be
finished later. Do not quietly ship a silent post and do not treat it as done.

## Writing

- **Target an eighth-grade reading level for blog posts.** Prefer short sentences and
  common words. It's fine to use technical terms, but define each one in plain language
  the first time it appears (a short blockquote works well).
- Do not use em dashes in blog posts.

## Index descriptions

- Add a plain-text `description` field to the YAML front matter of every new post.
- Write one or two short sentences that explain the post in about 20 to 30 words.
- Keep the description at an eighth-grade reading level. Do not put HTML, Markdown,
  Liquid tags, or media embeds in it.
- The home page in `index.html` must display `post.description` when it exists and
  fall back to the generated excerpt for older posts.
- Build the site and check the new post card before publishing. A post that begins
  with a video or other embed must still have a useful text description on the index.

## Article narration

> **CURRENT PATH (2026-09-08): Chatterbox on ronin28's RTX 4060.** CJ moved blog
> narration off VibeVoice on 2026-08-24 ("let's start using chatterbox for my blog
> post entries instead of vibevoice"). Render on **ronin28** (`ssh hermes@ronin28`),
> NOT pluto: pluto's P100 is Pascal (sm_60) and PyTorch has no Pascal kernels, so it
> silently falls to CPU. ronin28's 4060 (Ada, sm_89) has working GPU torch.
>
> Script: `~/Source/repos/aaronkclark-voicemodel/chatterbox_narrate_post.py`, run
> with the `chatterbox` venv. Input is a plain-prose `.txt` (blank-line separated
> paragraphs) at `work/blog-narrations/texts/<Slug>.txt`; output is the published
> master format, so it drops straight into `audio/posts/<slug>.mp3`.
>
> ```bash
> ssh hermes@ronin28
> cd ~/Source/repos/aaronkclark-voicemodel
> setsid nohup nice -n 10 /home/hermes/venvs/chatterbox/bin/python \
>   chatterbox_narrate_post.py \
>   --text work/blog-narrations/texts/<Slug>.txt \
>   --out  work/blog-narrations/audio/<Slug>.mp3 > /tmp/cb-<slug>.log 2>&1 &
> ```
>
> **Three Chatterbox facts the script already handles, and you should not undo:**
> 1. **perth 1.0.0 exports `PerthImplicitWatermarker` as `None`**, and
>    `ChatterboxTTS.__init__` calls it, so a bare import dies with `'NoneType'
>    object is not callable`. The script patches it to `perth.DummyWatermarker`
>    before importing chatterbox.
> 2. **It repeats its closing phrase** about 1 time in 6 past ~550 chars, so
>    paragraphs are split on sentence boundaries at 400 chars and
>    `repetition_penalty` is held at 1.4.
> 3. **It gets SHORT utterances flatly wrong**, so section headings are merged
>    into the paragraph that follows them rather than narrated as fragments.
>
> Chatterbox reads at ~17.5 chars/sec, VibeVoice at ~11.6. Any duration estimate
> or pace check calibrated for VibeVoice is wrong by half.
>
> `--cfg-weight 0.3` reads slower and flatter, which is the pacing CJ prefers for
> narration. Reference clip is `~/Documents/VibeVoice-Test/refs/aaron-ref-canonical.wav`.
>
> **The VibeVoice path below is the PRIOR path, kept for reference.**
>
> **VibeVoice (superseded 2026-08-24).** Render on ronin28's 4060.
>
> Repo: `~/Source/repos/VibeVoiceCommunity` with a `.venv`. Model cache holds
> `VibeVoice-1.5B` (fits the 4060's 8 GB) and `VibeVoice-7B` (needs ~14 GB, does
> NOT fit the 4060 or pluto's 3060 — waits on a bigger card like the planned V100).
> Reference voice: `demo/voices/en-AaronCanonical_man.wav` (`--speaker_names AaronCanonical`).
> Script format: a plain `.txt` with `Speaker 1: <text>` lines, one per paragraph.
>
> **THE TRAP that cost hours (2026-08-14):** `demo/inference_from_file.py` does an
> EXACT string compare `args.device == "cuda"`. Passing `--device cuda:0` does NOT
> match, falls through to the CPU branch, and renders at ~100s/iteration (a ~100
> HOUR ETA) while the GPU sits at 131 MiB / 0%. **Always pass `--device cuda`, never
> `cuda:0`.** GPU-bound looks like ~1.3 s/it with the card at 60-80% util.
>
> ```bash
> ssh hermes@ronin28
> M=$(ls -d ~/.cache/huggingface/hub/models--vibevoice--VibeVoice-1.5B/snapshots/*/)
> cd ~/Source/repos/VibeVoiceCommunity
> setsid nohup nice -n 10 .venv/bin/python demo/inference_from_file.py \
>   --model_path "$M" --txt_path <work>/script.txt \
>   --speaker_names AaronCanonical --output_dir <work> \
>   --device cuda --dtype bfloat16 --seed <YYYYMMDD> > /tmp/vibe.log 2>&1 &
> ```
>
> Then encode: `ffmpeg -i <work>/*.wav -ac 1 -ar 24000 -b:a 96k -af loudnorm=I=-16:TP=-1.5:LRA=11 audio/posts/<slug>.mp3`
>
> The Qwen3-TTS instructions below are the OLDEST path, kept for reference.

- Create narration for every new blog post before publishing it.
- Use the canonical voice tools and reference files in the adjacent
  `../aaronkclark-voicemodel` repository:
  - `qwen_narrate_longform.py`
  - `dataset/reference/aaron_reference.wav`
  - `dataset/reference/aaron_reference.txt`
  - `validate_renascence_asr.py`
- Narrate the article text, not its YAML front matter. Leave out code listings,
  raw URLs, image paths, video embed markup, and other text that is not useful when
  spoken.
- Split long text into a JSON list of short chunks for `qwen_narrate_longform.py`.
  Each chunk must contain `id`, `text`, `stanza`, and `pause_after_ms`.
- Use the accepted Qwen3-TTS 0.6B Aaron voice, language `English`, and native
  pacing. The renderer requires an RTX 3060 CUDA device. Use `--resume` so an
  interrupted render can continue safely.
- Encode the finished WAV as a mono, 24 kHz, 96 kbps MP3. Normalize it with
  FFmpeg's `loudnorm=I=-16:TP=-1.5:LRA=11` filter.
- Save the final file as `audio/posts/<post-slug>.mp3` and add
  `audio: /audio/posts/<post-slug>.mp3` to the post's YAML front matter.
- The post layout places the compact player directly below the title. Do not add
  a second player inside the post body.
- Confirm that the MP3 is playable, validate the narration against its source
  text, build the Jekyll site, and verify the page and audio path before publishing.

### Running the render (read this before installing anything)

**Nothing needs to be installed.** The renderer runs on
`$GPU_RENDERING_BOX_NAMED_AFTER_CARTOON_DOG` through `uv`, with every
dependency already in that host's uv cache, resolved fully offline. If you conclude that you need to `pip install` torch, download the
model, or free disk space, you have probed the wrong interpreter. A plain
`python3 -c "import torch"` tests the *system* interpreter and will always
report the package missing, because the toolchain lives in the uv cache.

Three things trip up every first attempt:

1. **Pin `--python 3.12`.** `uv` defaults to a newer CPython on
   `$GPU_RENDERING_BOX_NAMED_AFTER_CARTOON_DOG`, and the cached torch wheels
   stop at the `cp312` ABI. Without the pin the
   resolver fails with "requirements are unsatisfiable" plus a hint about ABI
   tags, which reads like a missing package but is not.
2. **Pass `--offline`.** It proves the run needs no network, and it fails fast
   and loudly instead of silently pulling multi-gigabyte CUDA wheels.
3. **Use `--device cuda:0`, the default.** On a multi-GPU host, torch and
   `nvidia-smi` can enumerate devices in *opposite* order. Do not translate an
   `nvidia-smi` index into a `--device` flag. `qwen_narrate_longform.py` guards
   on the device name and refuses to run on the wrong card, so a mismatch shows
   up as `Refusing to run on unexpected CUDA device`.

The invocation, run from a work directory holding the script, the reference
pair, and the chunk JSON:

```bash
uv run --offline --python 3.12 \
  --with qwen-tts==0.1.1 --with torch --with soundfile --with numpy \
  python qwen_narrate_longform.py \
    --model ~/models/Qwen3-TTS-12Hz-0.6B-Base \
    --reference aaron_reference.wav \
    --reference-text aaron_reference.txt \
    --chunks <post-slug>.json \
    --output-dir out --output-name narration.wav \
    --language English --device cuda:0 --seed <YYYYMMDD> --resume
```

`Warning: flash-attn is not installed` is expected and harmless; every existing
post was rendered on the same manual PyTorch path.

Then encode and place the file:

```bash
ffmpeg -i out/narration.wav -ac 1 -ar 24000 -b:a 96k \
  -af loudnorm=I=-16:TP=-1.5:LRA=11 audio/posts/<post-slug>.mp3
```

Chunk JSON is a list of objects with `id`, `kind`, `stanza`, `text`, and
`pause_after_ms`. Useful pause values: 900 ms after a heading, 700 ms after a
definition blockquote, 500 ms after a body paragraph.

**Do not purge `$GPU_RENDERING_BOX_NAMED_AFTER_CARTOON_DOG`'s uv cache to
reclaim disk.** It is tens of
gigabytes and looks like throwaway download cruft, but it *is* the renderer:
the cached CUDA torch build and `qwen-tts` wheel are what make an offline run
possible. Clearing it breaks narration for every future post and forces a
multi-gigabyte re-download. Reclaim space somewhere else.

## Scrub exception — the unlisted fleet page

Every post gets real IPs/hostnames/secrets scrubbed before publishing, with ONE
exception: `fleet-local-inference-plan.html` is an unlisted (noindex) page where
real internal infra detail (IPs, hostnames like pluto/telesto/ronin28, ports, GPU
UUIDs, file paths) is owner-authorized for teaching value. Never publish live
secrets even there. This exception is that one file only.
