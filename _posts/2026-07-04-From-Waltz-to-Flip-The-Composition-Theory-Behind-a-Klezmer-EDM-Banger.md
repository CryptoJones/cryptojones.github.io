---
layout: post
title: "From Waltz to Flip: The Composition Theory Behind a Klezmer EDM Banger"
---

*A buddy of mine is running a marathon and asked me for a playlist. Five hours and twenty minutes later, the first track was in his hands: Andy Statman's **Flatbush Waltz** — a sparse klezmer mandolin instrumental — turned into a sacred-and-profane EDM banger that literally paces a runner. I can't read music. So I built it the way I build everything now: I described what I was hearing to an AI composer, it named the fundamental I was fumbling toward, and we fixed that. Here's the theory behind every decision — worked out live between a guy with ears and no vocabulary, and a composer with all the vocabulary and no ears at all.*

🎧 **[Listen on SoundCloud &rarr;](https://on.soundcloud.com/Qz5MgFiJTA5dbpJQlW)**

## Don't rebuild the pig — flip it

The obvious way to make an "EDM version" of a song is to transcribe it: pull out the melody, quantize the notes, rebuild a new track from synths that quote the original. I tried that first. It kept coming out dead. A transcription is a *skeleton*, and a skeleton isn't recognizable — the ear keeps asking for the record it knows.

So I threw the skeleton away and made the opposite bet: keep Statman's actual recording — his mandolin, his phrasing, his room — and **flip** it. Recognizability stops being a problem to solve, because it's no longer manufactured. It's the record itself, wearing a new body.

> A **flip** reworks the original *recording*. A **cover** re-performs the *composition* with new hands. Statman's actual performance is the foundation here, so this is a flip, not a cover — and keeping his performance is the whole trick.

## You can't bolt a metronome to a heartbeat

Here's the problem that ate most of the afternoon. A four-on-the-floor kick is a metronome — perfectly even, forever. A human plays *rubato* — leaning into phrases, pulling back at cadences, speeding up and slowing down on purpose. Lay a rigid grid over an elastic performance and they drift apart within seconds. My feedback, verbatim, was: *"the kick is stoned while the band's on coke."*

The fix isn't a better metronome — it's to iron the rubato out of the *source* first. Beat-track the recording (find where its beats actually land, unevenly), then time-stretch each individual beat to the same length, flattening the whole performance to one constant tempo. **Then** the rigid kick locks, because now there's a fixed pulse to lock to.

> That per-beat stretch is a **phase vocoder** — it re-spaces audio in time while preserving pitch. It's exactly what a DJ's software does to beatmatch two records; I just pointed it inward and made the record agree with *itself*.

## Then tempo becomes a color

Once tempo is something you *set* instead of something you *inherit*, it's a compositional parameter like any other. So I set it per section. The intro doesn't start at the body tempo — it starts at **80 BPM and accelerates to 120** across the first ninety seconds, a long slow *accelerando* that, on a running track, reads as a body spinning up from a walk. The drops jump to **160**. The outro decelerates. The tempo curve isn't housekeeping; it's the program. It's my buddy's legs over the length of a run.

## The drop — and its opposite

EDM form is one idea run with discipline: tension and release. You withhold the full texture, build pressure, and at the **drop** you deliver everything at once. This track has two, placed by ear at the tune's own structural seams. Between them sits a **breakdown** — elements *subtracted* to reopen the tension so the second drop can land again.

The subtlest move is at the very end, and it's also subtraction: instead of letting the kick fatigue out under the finish, I **cut it cold**, eighteen and a half seconds from the end. Removing the beat is a bigger event than any addition could be — the ear snaps to what's left, and the track exhales. Density is a dynamic just like loudness; the most dramatic thing you can do to a wall of sound is take part of it away.

## Groove: the pump and the interlock

Two things give it motion. The first is **sidechain compression** — the whole mix ducks under each kick and swells back before the next, so the track visibly *breathes* in time. That's the "pump" that's the connective tissue of dance music, and it also carves a pocket at every downbeat so the low end never fights the kick.

The second is where the klezmer stops being a garnish and becomes structural. Instead of sounding the Hasidic-violin figure *on* the beats — where it masks the kick and both turn to mud — I put it on the **off-beats**, in the gaps between kicks. Now they interlock: kick, violin, kick, violin.

> Distributing a line so one voice sounds exactly where another rests is **hocket** — a technique as old as medieval polyphony and as current as any modern beat. On-beat, two loud events collide and mask each other; off-beat, the collision becomes call-and-response, and the groove doubles without a single note added.

## Pitch is not timbre

The intro wanted a choir. My first version took one sung "ah" and pitched it to three notes of a G-minor chord. It was wrong, and my note — again, verbatim — was that it *"sounds like a bunch of Gregorian monks."* Two problems.

First, one voice tripled isn't a choir. A choir is *different people*, and the tiny disagreements between them are exactly what the ear reads as "a group." So I used three different singers, each on one chord tone: G, B&#9837;, D. Second, and deeper: pitching them down had dragged their **formants** down with them.

> A voice is two things at once. The vocal folds set the **pitch**; the vocal tract is a filter whose resonances — the **formants** — make a vowel a vowel and a human sound a certain size. Ordinary pitch-shifting moves the whole spectrum together, so the formants ride along: shift up and the throat seems to shrink (chipmunk); shift down and it lengthens (the monk).

The fix is **formant-preserving** pitch-shifting. A vocoder like WORLD splits a voice into pitch, a spectral envelope (the formants), and breath; you move the pitch alone, hold the envelope fixed, and resynthesize. The pitch climbs; the human stays. That's what turned the monastery back into three women.

## Lilith, and every rule backwards

Against a pure, high, sacred chorus, the track wanted its opposite — a single dark voice moving underneath, seducing the faithful. I knew exactly who she was: **Lilith**.

Her voice is a real Middle-Eastern female vocal in the **Hijaz** maqam, and here the whole thing closes a circle. Hijaz *is* freygish — the same scale, the same augmented second, that Statman's mandolin has been playing since bar one. The demon was never foreign to the house; she sings in its native mode.

Making her demonic meant running every vocal rule **backwards**. Where the choir was lifted and formant-preserved, Lilith is dropped — a sub-octave shadow layered under her so the apparent vocal tract *lengthens* into something too large to be human; a low-pass filter shaving the air off the top so she reads dark; a long reverb placing her somewhere else, calling from a distance. Light above, shadow below.

## Sacred to profane

This is the move that makes it a composition and not a remix. The two women aren't decoration in the same scene — they're a *narrative*. The choir owns the opening, high and bright, with Lilith only weaving beneath them. Then, at that kick-cut near the end, the faithful fall silent, the mandolin recedes, and **Lilith takes the center and closes the track alone.** It's a resolution — and a dark one. The demon gets the last word.

## One last war story: saturation isn't clipping

Late in the mix I swore the master was clipping. It was, and it wasn't. The chain ended in a `tanh` soft-clipper — a curve that mathematically *cannot* produce digital clipping. But driven too hard by a hot mix on the drops, that same curve **saturates**: it rounds off the loud parts and adds harmonic grit that sounds exactly like clipping even though no sample ever crosses full scale. The fix was gain-staging — normalize first so the limiter is never slammed, shape gently, leave headroom. Clipping is a hard ceiling; saturation is a soft one; overdriving your own safety net *is* the distortion.

## What actually made it work

None of this is magic, and most of it isn't even new — hocket is medieval, formants are freshman acoustics, tension-and-release is every piece of music ever written. What was new was the *loop*: I'd describe a sound in whatever busted language I had — a fog horn, a stoned drummer, a monastery, a demon — and the AI would translate it into the fundamental underneath and fix *that*, not the symptom. Ears on one side of the table, vocabulary on the other.

And now it's a machine. Warp to constant tempo, shape the tempo curve, place the drops on the tune's own seams, weave the texture off-beat, voice the choir with real formants, and let the arc carry a story. That's the recipe for all eighteen tracks on the *Flurry Running Soundtrack*. Seventeen to go — and the hard one's finished.

It was never really about the track. Somewhere around mile twenty, with his legs gone, a friend of mine is going to hear a song I love turned into the exact thing that carries him home — and feel every decision on this page without needing a single word of it.

*A production note: everything above describes the track as **composed** — in G minor, at the tempos it was built around. The **shipped master** was then pitched down about 2½ semitones (into roughly E minor) and slowed to **0.86× speed**, one last pass to make it hit heavier and darker. Final runtime 4:34.*

---

*As30p — "Flatbush Drop (Andy Statman flip)," from the forthcoming **Flurry Running Soundtrack**. Composition worked out live with an AI. Unofficial and non-commercial; an homage to Andy Statman's "Flatbush Waltz," containing his recording under fair-use reworking. Proudly Made in Nebraska. 🌽*
