---
layout: post
title: "Three Tools, One Song: The Setup Behind Music I Can't Read"
---

*I can't read music. Not a note. But I keep putting out tracks, so people ask how. The short answer is that I built a little factory for it. Three tools do the work: one writes the song in code, one moves it into a real studio program, and one listens to the result and tells me if it's any good. Here's how each one works, in plain words — and two songs that came out the other end.*

🎧 **[As30p – Flatbush Drop &rarr;](https://on.soundcloud.com/41x9CBmWx7EUfKRLKA)**  •  **[As30p – Tennessee &rarr;](https://on.soundcloud.com/LnRqxMJjUsIHRg6XlS)**

## The problem: ears but no words

I can hear when something is wrong. I just can't say *why* in music terms. I don't know the names of the chords. I can't sight-read. So the normal path — write it down, play it, fix the notes — is closed to me.

So I stopped trying to write music the normal way. Instead, I describe what I want in plain English, an AI turns that into code, and the code builds the actual sound. Then I listen and say what's still off. We go around again. To make that loop fast and honest, I wrote three tools. Each one has its own job.

> A quick word on the **AI** part: it's not a "make me a song" button. It's a partner that knows the words I don't. I bring the ears; it brings the vocabulary and writes the code. Neither of us could make these tracks alone.

## Tool 1: the composer — [As30p](https://github.com/CryptoJones/As30p)

The first tool is a set of Python scripts that build a song from scratch. Not from some giant model that spits out finished audio — from real math and real samples. Kicks, hats, risers, one-shots: about 38,000 sounds sitting in a folder. The script picks them, layers them, shapes them, and mixes them into a full track.

Every time it runs, it saves **three files**, not one:

- a **`.wav`** — the actual audio you hear;
- a **`.mid`** — a MIDI file you can open in any studio program to see the layout;
- a **`.md`** — a plain-text sheet that writes down every choice it made, so I can look back later and learn.

That last file matters more than it sounds. It turns each track into a lesson instead of a lucky accident.

The best part is how the song's plan is stored. Near the top of the build script there's a simple list. Each line is one section of the song: its name, how many bars long it is, the tempo, and which layers play. Here's a piece of a real one:

    ('drop1',  56, 160, DROP),   # 56 bars at 160 BPM, full "drop" layers on
    ('break1', 32, 160, BREAK),  # 32 bars, strip it back down
    ('drop2',  56, 160, DROP),   # bring it all back

Want the drop to hit harder, or start sooner, or run at a different speed? Change one line. Everything downstream — the audio, the MIDI, the notes sheet — rebuilds to match. The whole shape of the song lives in a list you can read out loud.

> **BPM** means "beats per minute" — the speed of the song. 160 BPM is fast and dance-y. A **drop** is the big moment in electronic music where everything comes in at once. A **break** is the quieter part before it, so the drop feels bigger when it lands.

## Tool 2: the bridge — [FL Studio MCP Server](https://github.com/CryptoJones/FL-Studio-MCP-Server)

Code is great at making sound. It's bad at the human part — nudging a clip half a beat to the left because it just *feels* better there. That's what a real studio program is for. Mine is FL Studio.

Here's the catch: FL Studio has no normal way for outside tools to talk to it. It only has a small Python interpreter built inside. So I wrote a bridge that connects my AI assistant to FL Studio. It works three ways:

- **Read and write project files with FL closed.** It can build a fresh project, set the tempo, load in the samples, and lay out the clips — all without opening the program. To pull this off I had to figure out FL's own file format by hand, because it isn't public.
- **Control FL while it's running.** It can start and stop playback, move mixer faders, and poke at the live project over a MIDI link.
- **Piano-roll helpers.** Small scripts that transpose notes, add a human feel, strum a chord, and so on, installed right into FL's tools menu.

The real trick is the round trip. The code builds the project. I open it in FL and move things around by hand until it feels right. I hit save. Then a "diff" tool compares my saved file to what the code made and tells me *exactly* what changed — this clip moved here, that one got longer. I feed those changes back into the script.

> The rule that keeps this sane: **the code owns the sound, and I own the placement.** The script decides how a kick is built and mixed. I decide where it lands in the bar. Neither one steps on the other's job.

## Tool 3: the ear — [VibeComposing-Analyzer](https://github.com/CryptoJones/VibeComposing-Analyzer)

The last tool fixes my biggest weakness. I don't have golden ears. I can't always hear that the low end is too wide, or that two sounds are fighting for the same space. So I built something that can *show* me.

It's a plugin for VLC, the free media player. I wrote it in C so it's fast. While a song plays, it reads the audio and draws a live dashboard right in the VLC window. You click tabs to switch between views. The audio itself passes through untouched — the plugin only watches.

Two views do most of the work for me:

- **Compose view** — it shows the key of the song, which notes are playing, and how in-tune the pitch is. When I can't name the key by ear, the screen names it for me.
- **Production view** — this is a full mix check. It shows the loudness against a target, whether the bass is safe in mono, how wide each part of the sound is, and where two sounds might be covering each other up. These are the exact same things the As30p playbook says to watch. Now I can *see* them instead of guessing.

> **Mono safety** matters because a lot of speakers — phones, club subs, a laptop — play bass as one channel, not two. If your low end leans too far to one side, it can get weak or even disappear on those systems. The meter warns me before that happens.

## Putting it together: one loop

On their own, each tool is handy. Together they make a loop I can spin as fast as I can think:

1. **Compose in code.** As30p builds the track and writes down every choice.
2. **Arrange in FL.** The bridge moves it into the studio, I fix the feel by hand, and the diff tells the code what I did.
3. **Judge in VLC.** The analyzer shows me if the mix is actually good, using hard numbers instead of hope.
4. Whatever's still wrong goes back to step one.

I say what I hear. The tools handle the words and the math. Around and around until it's done.

## Hear what comes out

Two tracks from this setup. The first is **Flatbush Drop** — a sparse klezmer mandolin tune turned into a dance banger. I wrote a whole post on the music theory behind that one: [From Waltz to Flip](/From-Waltz-to-Flip-The-Composition-Theory-Behind-a-Klezmer-EDM-Banger/). The second is a flip of Arrested Development's **Tennessee**.

🎧 **[Flatbush Drop &rarr;](https://on.soundcloud.com/41x9CBmWx7EUfKRLKA)**

🎧 **[Tennessee &rarr;](https://on.soundcloud.com/LnRqxMJjUsIHRg6XlS)**

## The tools, if you want to poke at them

All three are open source:

- **[As30p](https://github.com/CryptoJones/As30p)** — the Python scripts that compose and render the track.
- **[FL Studio MCP Server](https://github.com/CryptoJones/FL-Studio-MCP-Server)** — the bridge between the code and FL Studio.
- **[VibeComposing-Analyzer](https://github.com/CryptoJones/VibeComposing-Analyzer)** — the VLC plugin that listens and grades the mix.

You don't need to read music to make it. You just need a way to turn what you hear into something a computer can act on. That's all these three tools really are.
