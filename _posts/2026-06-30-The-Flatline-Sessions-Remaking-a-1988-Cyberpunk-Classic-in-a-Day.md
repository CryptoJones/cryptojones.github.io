---
layout: post
title: "The Flatline Sessions: Remaking a 1988 Cyberpunk Classic in a Day"
---

<p align="center"><strong>🎂 HAPPY BIRTHDAY, P13XU5! 🎂</strong></p>

*Yesterday evening I had an empty folder and a copy of Interplay's 1988
Neuromancer. About twenty-two hours later I had a finished, standalone, winnable
remake of it — its own art, its own prose, its own soundtrack, two endings, and
downloadable builds for Windows, macOS, and Linux. Here's how it came together,
and the one decision that made all of it legal to ship.*

![The Flatline Sessions key art](/images/flatline-key-art.png)

## Own everything you show

The 1988 game is a cyberpunk classic, but its art, text, and code belong to
Interplay, and the story and characters belong to William Gibson. You can't ship
any of that. So the whole project ran on a single rule: **the engine can be
faithful, but every asset the player actually sees has to be ours.**

That's the ScummVM model taken all the way. The map, rooms, exits, shop prices,
ICE rules, and win path are ported faithfully (cross-referenced against the
excellent [Javamancer](https://github.com/maehem/javamancer) port). But every
room plate, every line of prose, and every note of music is newly authored. The
result plays like the original and ships with **no original files required** —
which is the difference between a defensible fan remaster and a takedown waiting
to happen.

## The art is AI — except in two places

Every background is a FLUX render off a local RTX 3060, then **pixelated
in-engine** so it reads as chunky retro art with crisp text on top. (That
pixelation started as a downscaling accident and instantly became the look of
the whole game.)

Two images are deliberately *not* AI, and that's the point. Ratz the bartender
has a **hand-painted pink prosthetic arm** — Gibson's prose says pink, the model
rendered it teal, so I ran a pink layer over it in Procreate. There's one other
**hand-drawn piece** tucked away in the game, rendered sharp while everything
else stays pixelated — but telling you where would ruin it. The players who go
looking will know it when they find it.

![The Chatsubo — Ratz and the pink arm](/images/flatline-chatsubo.png)

## The soundtrack named the game

The score is area-reactive — different music for the streets, the shops,
cyberspace, and the endgame — built by arranging royalty-free sample loops into
original cues with ffmpeg. I put it up under my music handle, **As30p**, as an
album called *The Flatline Sessions*.

Then the album named the game. When it came time to give the storefront page a
title that wasn't a trademark, the soundtrack already had one. The game, the
album, and the store page all became *The Flatline Sessions* — one brand I
actually own, wrapped around a faithful homage in the fine print. You can [hear
the whole soundtrack here](https://soundcloud.com/as30p/sets/the-flatline-sessions).

## Cyberspace, ICE, and two endings

You jack into the matrix with a deck, fly a neon grid, and break the ICE on data
fortresses in turn-based combat. Crack the AI-guarded bank and the endgame opens:
the Neuromancer AI drops its mask, pulls you onto Cyberspace Beach, and admits
it's been the puppeteer the whole time.

Then it offers you a choice, straight out of the novel. **Refuse**, run your
icebreaker, and free the AI. Or **stay** — walk up the sand to a Linda Lee it
built from your own memory, and never go back to the meat. Two endings, no wrong
answer; the horror of the beach is how good the offer is.

![Cyberspace Beach — the endgame](/images/flatline-beach.png)

## The one real war story: exports

The engine loads all its art, audio, fonts, and data off disk at runtime — great
from source, but it silently breaks inside an exported build, where those files
are packed away in a `.pck`. The fix was to make every loader prefer the imported
resource and fall back to a raw disk read, then verify it by **headless-booting
the exported macOS app and confirming it loaded a real asset without error.**
Boring, essential, and the whole difference between shipping a game and shipping
a black screen.

## Play it, hear it, read it

🕹️ **[Play *The Flatline Sessions* &rarr;](https://cryptojones.itch.io/the-flatline-sessions)** — free, on Windows / macOS / Linux.

<iframe width="720" height="405" src="https://www.youtube.com/embed/Dl9qZNm67bQ" title="The Flatline Sessions trailer" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="max-width:100%;"></iframe>

Empty folder to shipped game in a day, mostly because the unglamorous decisions —
own your assets, disclose your AI, verify your exports — got made first.

---

*MIT (code) &middot; [GitHub](https://github.com/CryptoJones/neuromancer-godot)
&middot; [Soundtrack](https://soundcloud.com/as30p/sets/the-flatline-sessions).
Unofficial, non-commercial fan remaster. Not affiliated with or endorsed by
William Gibson or Interplay; contains no original game assets. Proudly Made in
Nebraska. 🌽*
