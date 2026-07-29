---
layout: post
title: "OSAPHLA: An Open-Source Pan-Hispanic Language Academy"
audio: /audio/posts/OSAPHLA-Open-Source-Language-Academy.mp3
---

I've been building a full language-learning academy as a single-user PWA — no
accounts, no telemetry, no server dependency once it's loaded. It's called
**OSAPHLA** (Open Source Accessible Pan-Hispanic Language Academy), and it
ships two complete, mirrored paths: Spanish for English speakers, and English
for Spanish speakers.

## Try it now

There's a working demo running live at **[osaphla.cryptojones.dev](https://osaphla.cryptojones.dev)**.
No install, no login — just open it in a browser and pick a language to start.

## What's actually in it

Each path is 36 weeks deep: 180 assessed sections, 4,320 question-bank items,
and 88 reading activities per path (360 sections total across both). The
target is an ILR 2 core with ILR 2+/2+/2 stretch preparation — it doesn't
claim to hand out an official ILR rating, but the assessment design is built
around that framework.

Every section follows the same shape:

- themeable semantic slides with optional local narration
- a descriptive transcript and an optional rendered MP4
- objectives, instruction, vocabulary, model sentences, and a productive task
- an on-device microphone lab with optional local Whisper transcription
- a 24-item question bank (8 multiple choice, 8 cloze, 8 ordering)
- a randomized 12-item attempt per section, targeting 85%

Ordering items use ordinary buttons plus dedicated left/right controls, so
there's no drag-precision requirement. Cloze work starts lenient about
missing accents and gets stricter as the course progresses, and regional
accepted answer forms are spelled out explicitly rather than fuzzy-matched.

## Local-first by design

Settings, attempts, recordings, and progress all live in the browser. There's
no account system, no remote database, and no required runtime API — the app
shell and authored course content work offline after the first load. A
one-button offline installer grabs all 180 videos and narration tracks for a
selected course when you want the whole thing available without a connection.

Media is generated locally too: a renderer built on the Kokoro neural TTS
model, Chrome, and FFmpeg produces narration, captions, and transcripts from
the same slide data that drives the adaptive HTML lessons. Narration rotates
across a fixed set of voices per lesson (so the same lesson always has the
same voice on rerender), and both paths handle phoneme-level code-switching
between `en-us` and `es-419` — Spanish terms embedded in English instruction
keep Latin American pronunciation instead of being run through the English
phonemizer.

## Accessibility as a first-class feature

New learners choose a language, then get native-language guidance to
configure a visual-comfort lab before anything else: system, high-contrast
dark, high-contrast light, low-glare charcoal, warm paper, and monochrome
themes, plus independent controls for typography, spacing, reading width,
focus, cursor, density, and motion. Automated quality gates check WCAG
compliance and 320-pixel reflow as part of the standard test suite, alongside
curriculum-contract and balanced-assessment validation.

## Try it, run it, or read the source

The demo is the fastest way to see it: **[osaphla.cryptojones.dev](https://osaphla.cryptojones.dev)**.

**[View the OSAPHLA source on GitHub](https://github.com/CryptoJones/OSAPHLA)**.

To run it locally, it's a standard Node/Vite project — `npm install` and
`npm run start:local` will prompt for a port, start the dev server, and open
it in a browser.

---

*Proudly Made in Nebraska. Go Big Red! 🌽 <https://xkcd.com/2347/>*
