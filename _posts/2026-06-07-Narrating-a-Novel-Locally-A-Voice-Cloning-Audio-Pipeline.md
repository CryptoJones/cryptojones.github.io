---
layout: post
title: "Narrating a Novel Locally: A Voice-Cloning Audio Pipeline"
audio: /audio/posts/Narrating-a-Novel-Locally-A-Voice-Cloning-Audio-Pipeline.mp3
---

*I wanted a multi-voice audiobook — a full narrator plus distinct character voices —
produced entirely on my own hardware, for free, without cloning a single living
person. This is the audio pipeline that got me there: zero-shot voice cloning on an
8GB consumer GPU, a casting system, and the one trick that matters more than any of
it — keeping the read from jumping around.*

The commercial route priced itself out immediately. A cloud TTS read of an entire
novel would have run tens of thousands of credits and months of wall-clock on a
metered plan. So the whole thing runs locally on [F5-TTS](https://github.com/SWivid/F5-TTS),
a zero-shot voice-cloning model: give it ~10 seconds of reference audio plus the
transcript of that snippet, and it speaks new text in that voice. No fine-tuning, no
training run — it clones from the reference at inference time on an 8GB card.

```python
from f5_tts.api import F5TTS
f5 = F5TTS()
f5.infer(
    ref_file=ref_wav, ref_text=ref_transcript,   # ~10s seed + its exact transcript
    gen_text=line,                                # the sentence to speak
    file_wave=out_path,
    remove_silence=True,
    speed=1.0, seed=42,                           # see "consistency" below
)
```

## The rule that shaped everything: consent

Before any tech: **no cloning living, identifiable people.** Not actors, not
celebrities, nobody who didn't agree to it. Every voice in the production comes from
one of two places:

1. **Public-domain audio seeds** — LibriVox / archive.org recordings old enough or
   licensed to be free to use.
2. **My own voice**, which I own.

That constraint isn't a footnote, it drove the whole casting process. The dead-sounding
"ROM construct" character, for instance, started life as a public-domain LibriVox
chapter read by a volunteer, then got machined into something inhuman with DSP (more on
that below) — *not* lifted from any film performance. If you take one thing from this
post, let it be that you can do expressive, characterful voice work without scraping a
real person's identity.

## Consistency beats per-voice perfection

Here's the counterintuitive lesson. The thing that makes AI narration sound *amateur*
isn't a slightly-off character voice — it's the audio **lurching** between clips:
timbre and pace drifting from one sentence to the next. Zero-shot TTS re-estimates
duration and prosody on every independent generation, so back-to-back clips wander in
speed and tone even from the same reference.

Fixing that took a four-part "de-jitter" recipe, and it's worth more than any amount of
per-character polish:

- **Pin the seed.** A fixed RNG seed (`seed=42`) gives every clip the same latent
  initialization, which holds timbre steady across thousands of generations.
- **Pin the speed.** `speed=1.0` everywhere. No per-line pace, ever. (I tried slowing a
  drugged-out character down to 0.85 — it read as a *jump*, so it got reverted.)
- **One loudness target on every clip.** Every single cue ends its filter chain with
  the *identical* `loudnorm`:

  ```
  loudnorm=I=-16:TP=-1.5:LRA=11
  ```

  No per-voice loudness shaping. The whole production sits at one level.
- **Short crossfades at every seam.** Clips are joined with a tiny triangular
  crossfade so the boundaries don't click or lurch:

  ```
  acrossfade=d=0.12:c1=tri:c2=tri
  ```

A useful gotcha: a "casting sheet" that slams five voices together back-to-back will
sound *jumpier* than the real thing, because it's nothing but seams. A real chapter is
~80% one narrator, so it flows. Judge consistency on real material, not the stress test.

A second gotcha worth saving you the rabbit hole: **moving the same model to the cloud
does not fix drift.** It's the same model — hosted F5 only offloads your GPU, it doesn't
change the prosody behavior. Don't chase consistency by changing where it runs.

## Casting: one source of truth

Every speaker — the narrator, each principal, and each one-line walk-on — maps to a
voice in a single table that both the renderer and the stitcher read. A row is just:
*tag → (seed, speed, DSP chain)*.

- **Principals** get a fixed public-domain seed, chosen once and reused everywhere so a
  character sounds the same in chapter 2 and chapter 20.
- **Distinctness comes from DSP, not from hunting down 30 seeds.** Two characters can
  share a base seed and still sound clearly different if each gets its own *internally
  uniform* processing. Which leads to the timbre chains…
- **Walk-on "drop" characters** (a guard, a clerk — one or two lines) get a
  **deterministically random** voice: hash the character's name, pick a (seed, pitch)
  pair from a gender-appropriate pool, and guarantee no two walk-ons collide *and* that
  none lands too close in pitch to a principal on the same seed. Everybody's different,
  nobody had to be hand-cast.

## Timbre is an ffmpeg chain

Once a voice's *identity* lives in its seed, its *character* is just a deterministic
audio-filter chain — independently dialable, and applied identically to every line that
character speaks (consistency again). Pitch shifts use the resample trick (`asetrate`
to move pitch+formants, `atempo` to restore the original duration), so they sound like
a differently-sized person rather than a chipmunk artifact:

```bash
# deepen a voice ~1.25 semitones, add body
asetrate=24000*0.93,aresample=24000,atempo=1.0753,bass=g=2:f=120, ... ,loudnorm=...

# an AI/comms character: telephone band + a touch of bitcrush
highpass=f=300,lowpass=f=3400,acompressor=...:ratio=4,acrusher=bits=8:mode=log:mix=0.15,loudnorm=...

# the "dead ROM construct": pitch-down, flat affect, digital grit, hollow comb echo
asetrate=24000*0.95,aresample=24000,atempo=1.0526,acompressor=...:ratio=4,acrusher=bits=7:mode=log:mix=0.35,aecho=0.85:0.6:18:0.35,highpass=f=80,loudnorm=...
```

Compressor flattens emotional affect, `acrusher` adds digital grit, an 18ms `aecho`
gives a hollow comb. Every chain ends in the same `loudnorm` — that's the
non-negotiable.

## The script: verbatim text, then heuristic attribution

The audio is only as good as the script feeding it, and there were two rules:

1. **Text is verbatim from the source file — never reconstructed from memory.** An LLM
   will happily "remember" a famous novel and paraphrase it. For a faithful reading
   that's poison. Every line is sliced out of the actual source text; the model never
   gets to improvise the words.
2. **Attribution is heuristic.** To turn flat prose into tagged cues
   (`[NARRATION]`, `[CASE]`, `[MOLLY]`, …) the tagger matches balanced quote pairs and
   then guesses the speaker from the surrounding text: self-introductions ("my name
   is…"), speech-verb patterns (*name + said*, *said + name*, *pronoun + verb* resolved
   by gender), action-beat subjects, and a running 2–3 party "who's in this scene"
   tracker that resets after long stretches of narration. It lands around 80% right on
   the first pass — good enough to review and nudge, and narration (over half the lines)
   is 100% correct because it's just the un-quoted remainder.

Prose gets grouped a few sentences per cue; dialogue is one cue per quote. Quotes are
stripped (they're *spoken*, not read aloud as "quote… unquote").

## Stitching it together

Per chapter the pipeline is:

1. **Render** every cue to its own wav (`output/<chapter>/NNN_TAG.wav`). The whole loop
   is **resumable** — it skips any clip that already exists, so a multi-hour run on a
   small GPU can be killed and restarted without losing work. The model loads once and
   stays resident across thousands of cues.
2. **Process** each cue with its character's filter chain (ending in the shared
   `loudnorm`).
3. **Crossfade** the processed cues into one continuous chapter track with the 0.12s
   triangular fade at every seam.
4. **Mux** the chapter audio under its video and move on.

```bash
# resumable render: existing clips are skipped, model stays loaded
python3 render_all.py            # all chapters
python3 render_all.py ch05 ch06  # or just a few

# per-chapter stitch: per-voice DSP + uniform loudnorm + crossfades
bash stitch_chapter.sh ch05
```

Everything is plain Python and `ffmpeg`. No proprietary stack, no per-minute meter, no
nonconsensual voice in the building. The visual side — the animated ASCII-art
backgrounds and the lo-fi score each chapter plays over — is its own pure-Python engine
I've open-sourced separately as
**[The Flatline Sessions](https://github.com/CryptoJones/TheFlatlineSessions)**.

---

*The takeaways, if you're building something similar: clone only what you have the
right to clone; pin your seed, speed, and loudness so the read doesn't lurch; let DSP
do the work of making voices distinct; and keep your script verbatim from a real source
instead of trusting a model's memory.*
