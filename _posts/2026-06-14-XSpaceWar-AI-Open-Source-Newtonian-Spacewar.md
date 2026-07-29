---
layout: post
title: "XSpaceWar-AI: We Rebuilt Spacewar! With Real Gravity — and It's Free"
audio: /audio/posts/XSpaceWar-AI-Open-Source-Newtonian-Spacewar.mp3
---

*Sixty-four years ago a couple of MIT hackers wired two spaceships and a star
into a PDP-1 and invented the multiplayer video game. We took that idea, gave it
honest Newtonian physics, generated every pixel and every sound from math, taught
the bots to be genuinely mean, and put 16 ships in the same arena. It's done, it
runs on Windows, macOS, and Linux, it's Apache-2.0 open source, and it costs
nothing.*

**👉 Play it now on [itch.io](https://cryptojones.itch.io/xspacewar-ai) — or grab
a build straight from
[GitHub Releases](https://github.com/CryptoJones/XSpaceWar-AI/releases/latest).**

- 🎮 **itch.io:** [cryptojones.itch.io/xspacewar-ai](https://cryptojones.itch.io/xspacewar-ai)
- 🌐 **Landing page:** [cryptojones.github.io/XSpaceWar-AI](https://cryptojones.github.io/XSpaceWar-AI/)
- ⬇️ **Direct downloads (Win · macOS · Linux):** [GitHub Releases](https://github.com/CryptoJones/XSpaceWar-AI/releases/latest)
- 🛠️ **Source (Apache-2.0):** [github.com/CryptoJones/XSpaceWar-AI](https://github.com/CryptoJones/XSpaceWar-AI)

## The first networked match said everything

Dedicated server on one machine, two pilots joining from two more. The human —
barely moving, just letting the star do the work — beat the AI **3 to −19**,
while the bot fell into the gravity well **fifty-nine times**. Newtonian gravity
is undefeated.

![The first networked deathmatch — human beats the AI 3 to −19]({{ site.baseurl }}/images/xspacewar-ai-victory.png)

That score isn't a difficulty setting. It's physics. The star pulls with pure
`G·M / r²` — no caps, no clamps, no softening. Fly too close and the pull
genuinely diverges; you cannot thrust your way out of a star you've already
fallen into. That's not a bug, it's a star.

![The gravity well claims another ship]({{ site.baseurl }}/images/xspacewar-ai-star.png)

## What it actually is

A modern, top-down **space-fighter** with a heavy AI focus — a 2026 reimagining
of the classic networked *Spacewar!* / `xspacewar`. Bird's-eye view like the 1962
original, but built in **Godot 4** with:

- **Honest Newtonian flight.** Conserved momentum, inverse-square gravity on ships
  *and* torpedoes, gravity-assist slingshots, hyperspace. No drag — to slow down
  you flip 180° and burn against your own velocity, the same maneuver Spacewar!
  pilots have flown since '62.
- **100% procedural everything.** Stars, planets, moons, asteroid fields, nebulae,
  ships, VFX — and *audio*. There's not a single hand-drawn art asset or recorded
  sound file in the game; every sound is synthesized from math at load. Every
  match is a fresh seeded arena.
- **Up to 16 ships**, four game modes: Free-for-all, Team battle, AI bots
  (**Rookie → Insane**), and **Movie Mode** — an all-AI attract reel that
  regenerates a brand-new arena, roster, and teams every 30 minutes. Leave it
  running on a second monitor; it never plays the same match twice.
- **Multiplayer that works today.** Host-authoritative netcode with client-side
  prediction and reconciliation, automatic **LAN discovery**, **direct IP**, and
  platform-agnostic **internet play** through the project's own relay/master
  server — room codes, an online server browser, no port forwarding and no
  platform account required.
- **Seven UI languages**, including right-to-left Arabic.

## Standing on 64 years of shoulders

XSpaceWar-AI is a clean-room implementation, but it knows exactly where it comes
from: **Spacewar!** (MIT, 1962, on the DEC PDP-1), the 1974 PDP-11 networked
port, and **Ron Frederick's** 1992 X11 `xspacewar 1.2` — an early *serverless*
networked game where peers shared state directly. Huge thanks to Ron
([github.com/ronf](https://github.com/ronf)), whose 1992 networked Spacewar is
this game's direct ancestor.

## Get in a ship

The whole thing is free and open source under Apache-2.0. No launcher, no account,
no telemetry, ~100 MB on disk.

- **Easiest:** play in the browser or download from
  **[itch.io](https://cryptojones.itch.io/xspacewar-ai)**.
- **Prebuilt binaries:** the zip for your platform on
  **[GitHub Releases](https://github.com/CryptoJones/XSpaceWar-AI/releases/latest)**
  (Windows, macOS universal, Linux x86_64).
- **From source:** clone
  [the repo](https://github.com/CryptoJones/XSpaceWar-AI), run `./install.sh`
  (it fetches and SHA-512-verifies Godot 4.6.3 for you), then `godot --path .`.
- **Steam:** coming soon.

> **macOS note:** the build is ad-hoc signed but not notarized, so Gatekeeper may
> claim it's "damaged." It isn't — right-click → **Open**, or
> `xattr -dr com.apple.quarantine /path/to/XSpaceWar-AI.app`. Full instructions are
> on the [releases page](https://github.com/CryptoJones/XSpaceWar-AI/releases/latest).

Bring friends. Pick *HOST — LAN skirmish*, share a 4-letter room code over the
internet, or just turn on Movie Mode and watch the bots feed themselves to the
star. The gravity is real, the maps are infinite, and the source is yours.

🚀 **[Play XSpaceWar-AI →](https://cryptojones.itch.io/xspacewar-ai)**

---

*Apache-2.0 · [GitHub](https://github.com/CryptoJones/XSpaceWar-AI) ·
[Codeberg mirror](https://codeberg.org/CryptoJones/XSpaceWar-AI). Dedicated to
JVL. Proudly Made in Nebraska. 🌽*
