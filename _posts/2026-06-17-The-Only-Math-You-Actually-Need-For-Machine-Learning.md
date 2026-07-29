---
layout: post
title: "The Only Math You Actually Need for Machine Learning"
audio: /audio/posts/The-Only-Math-You-Actually-Need-For-Machine-Learning.mp3
---

*The lie that keeps people out of machine learning is that you need a math degree
first — four semesters of analysis and proofs before you're allowed to touch a
neural network. You don't. I made a video about the small, mostly-conceptual slice
that actually matters, ranked by what it pays back.*

Watch it here:
[youtube.com/watch?v=3aC5zWFHZH4](https://www.youtube.com/watch?v=3aC5zWFHZH4)

## The shortlist

There are really two different skills people lump together as "ML math," and
confusing them is why folks over-study and quit. **Operating** models — running them
locally, RAG, hosting, quantization — needs almost no advanced math. **Understanding**
why training works and reading papers without bouncing off the notation needs a small,
specific slice. The video is about that second skill, and even there it comes down to
three topics in priority order:

1. **Linear algebra (the conceptual version).** The keystone, and the one most people
   skip. Vectors, dot products, matrices as *actions* on space, and above all **tensor
   shapes** — because ninety percent of the errors you hit early are shape mismatches.
   Get this and embeddings, attention, and "why is everything a matmul" all click.
2. **Probability & statistics.** It pays off on both ends — the data going in, and the
   model's behavior coming out: what a loss is, what **softmax** does, why
   **temperature 0.7** behaves the way it does. The settings stop being magic sliders
   you nudge and pray over.
3. **Calculus — exactly one idea.** The **gradient**: which way is downhill. Training is
   walking downhill on the loss; the learning rate is your step size; and autograd does
   every actual derivative for you. A weekend of intuition, not a course.

There's also a segment I'm partial to: if you ever took **discrete math**, you already
own pieces of the machine. Functions (`f(g(x))` is literally a stack of layers), graphs
(attention is a graph; RAG is nearest-neighbor search), counting and conditional
probability, and Big-O (why attention is O(n²)) all map straight onto ML. You're not
starting from zero.

And a generous "what to skip": real analysis, measure theory, proof-heavy multivariable
calculus. That's researcher tooling — not a prerequisite for building things.

## Who it's for

Anyone who can already get a model *running* but wants to understand **why** it works —
to go from "it works and I don't know why" to "I know exactly why," and read a paper or
a model card without bouncing off it. No degree required, and you can start today.

## A note on how it was made

The whole thing was produced on my own hardware with open tools — narrated in my own
voice, with the slide deck and final assembly done locally (the usual `ffmpeg`
gymnastics, a neon "cyberdeck" theme, and a slow Ken Burns drift so nothing sits dead on
screen). No cloud render farm, no subscriptions. More on that pipeline in a future post.

## Credit where it's due

The video teaches these concepts in my own words and visuals — for the real deep dives,
go to the people who do them best:

- **3Blue1Brown** — *Essence of Linear Algebra* and *Essence of Calculus*. The visual,
  intuition-first foundation. Watch these first.
- **StatQuest** (Josh Starmer) — probability, softmax, sampling, all in friendly pieces.
- **Andrej Karpathy** — *Neural Networks: Zero to Hero*. Build a tiny net from scratch
  and watch the gradient happen in code.
- **Susanna S. Epp** — *[Discrete Mathematics with Applications](https://www.amazon.com/Discrete-Mathematics-Applications-Susanna-Epp/dp/1337694193/)*.
  The book behind the "secret weapon" segment.

*Proudly Made in Nebraska. Go Big Red! 🌽 <https://xkcd.com/2347/>*
