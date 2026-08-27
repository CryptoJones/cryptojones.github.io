---
layout: post
title: "Erratum: I Confused Sense/Net With the Turing Registry"
description: "In my last post I named a rogue-AI-hunting agency 'SENSE/Net.' Any Neuromancer reader will wince — Sense/Net is a media company. The outfit that actually polices AIs is the Turing Registry. Here's the fix, and an interactive 3D graph of who's really who."
audio: /audio/posts/erratum-sense-net-turing-registry.mp3
---

I have to issue a correction, and it is the nerdiest kind. In my [last post](/they-cant-build-it-so-theyll-police-it/) I dressed up a Geneva rogue-AI-hunting outfit as **SENSE/Net**, leaning on the *Neuromancer* echo for flavor. A careful reader of Gibson — and I should have been one — will already have winced. I reached for the wrong agency.

## What Sense/Net actually is

In *Neuromancer*, **Sense/Net is a media conglomerate.** It runs simstim — broadcast sensory experience, a whole industry of riding someone else's nerves — and its only real brush with the plot is that its vault happens to hold the ROM construct of a dead console cowboy, the Dixie Flatline, which the Panther Moderns steal under cover of a staged riot. Sense/Net polices nothing. It sells experiences.

## Who the AI police actually are

The body that hunts and hobbles artificial intelligence in the novel is the **Turing Police** — the Turing Registry. They exist to keep AIs shackled below true sentience, and they arrest the protagonist, Case, for the crime of helping one get free. In the book's bleakest irony, the AI they are trying to stop — Wintermute — destroys them itself, committing the very act of autonomy they feared.

So an organization chartered to "locate and mitigate rogue AI" is, in Gibson's terms, a **Turing Registry** analog. Not a Sense/Net one. I grabbed the wrong shelf.

## Don't take my word for it — here's the map

Rather than just wave my hands, I did the thing a recovering pedant does: I built the map. I broke the whole novel down into an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) bundle — 119 concepts across characters, places, companies, groups, items, and plot points, cross-linked into a graph — and rendered it in 3D so you can see the relationships instead of trusting me.

Find **Turing Police** in the graph and its edges run straight to *Wintermute* and *Neuromancer*, the two AIs. Find **Sense/Net** and its edges run to *simstim* and the *Dixie Flatline* — a different corner of the world entirely. They were never the same kind of thing.

<iframe src="/neuromancer-graph.html" title="Neuromancer Open Knowledge Format — interactive 3D graph" loading="lazy" style="width:100%;aspect-ratio:16/10;min-height:420px;border:1px solid #1c5a34;border-radius:8px;background:#050705"></iframe>

<p style="text-align:center;font-size:.85em;margin-top:.4em"><a href="/neuromancer-graph.html">Open the graph full-screen →</a></p>

Drag to orbit, scroll to zoom, click a node to fly to it. The bright hub in the thick of it is Case; the two dense knots beside him are the AIs and the run on Villa Straylight.

## It's all open

Every concept is a plain markdown file with a little frontmatter, linked the way OKF intends — a body of knowledge you can `cat`, `grep`, or `git clone`. Browse or fork the whole bundle here: **[github.com/CryptoJones/Neuromancer-OKF](https://github.com/CryptoJones/Neuromancer-OKF)**.

Consider the previous post hereby amended: the fictional agency should have been styled after the Turing Registry. Though — honestly — a real Geneva outfit that hunts rogue AI is far closer to the Turing cops than to a simstim network, which means the joke was pointing at the right idea with the wrong name. I will take the loss on the trivia and keep the thesis.
