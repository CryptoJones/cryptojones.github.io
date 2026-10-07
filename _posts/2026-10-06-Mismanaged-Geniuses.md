---
layout: post
title: "Mismanaged Geniuses"
description: "Alex Zhang of MIT argues AI models are already smart enough for most work. The missing piece is the harness that breaks big jobs into small ones they can handle."
keywords: "recursive language models, RLM, Alex Zhang, MIT CSAIL, harness, compositional generalization, locally in-distribution, mismanaged geniuses hypothesis, context rot, Deep Learning with Yacine"
audio: /audio/posts/mismanaged-geniuses.mp3
---

I run a lot of AI agents. Some are top-of-the-line models from the big labs, running in Claude Code. Some are free, downloadable models on older graphics cards I run at home. The thing I have learned the hard way is that the same model can look brilliant in one setup and dumb as a rock in another. The software wrapped around the model matters as much as the model.

So I was glad to see Yacine Mahdid of Deep Learning with Yacine sit down with Alex L. Zhang again. Alex is a second-year PhD student at MIT's Computer Science and Artificial Intelligence Laboratory (CSAIL) and the creator of **Recursive Language Models**, or RLMs. The interview, [*RLMs are Compositional Generalizers*](https://www.youtube.com/watch?v=YyMBg8WXIUg), runs about an hour and 35 minutes. Here is what it covers, in plain English.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YyMBg8WXIUg" title="RLMs are Compositional Generalizers with Alex Zhang from MIT" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## First, what is a harness?

> A **harness** is the software wrapped around an AI model. It decides what the model sees, runs its tools, cleans up its memory, and calls it again in a loop. Claude Code and Codex are harnesses.

The common view in research has been that the harness is just plumbing. The smarts live in the model's **weights**, and every new model makes the wrapper matter a little less.

> **Weights** are the millions or billions of numbers inside a model that get adjusted while it learns. They are what the model "knows."

In his introduction, Yacine gives two reasons that view is wrong.

The first is **context rot**.

> A **token** is a chunk of text, often a piece of a word. The **context window** is how many tokens a model can read at once. **Context rot** is the way models get less reliable as that text gets longer, even when it still fits.

A million-token window does not mean a million tokens of good work. Labs have tried many tricks to fix this inside the model. They help, but only so far.

The second reason is that Transformers are bad at **compositional generalization**.

> The **Transformer** is the basic design under nearly every modern AI language model. **Compositional generalization** means solving a new problem by combining skills you already have. A person who can add and can count coins can make change without a lesson on making change.

Models mostly need fresh training data for each new kind of task. They do not snap their skills together on their own very well.

## What an RLM does

Alex first shared RLMs in a blog post in October 2025. A [paper](https://arxiv.org/abs/2512.24601) with Tim Kraska and Omar Khattab followed at the end of December, and it has since been accepted to NeurIPS 2026, one of the biggest AI research conferences. The idea is simple.

Normally you paste the whole long prompt into the model. An RLM does not. It puts the prompt into a variable inside a Python **REPL**.

> A **REPL** (read, evaluate, print, loop) is an interactive coding window. You type a line of code, it runs, and you see the result.

The main model does not start with the whole text in front of it. It writes code to peek at the text, search it, and chop it into pieces. Then it can hand a piece to a fresh copy of itself with a short, focused question. That is the "recursive" part. In his writing, Alex boils it down to two moves:

1. **Context offloading.** The big pile of text lives in the code environment, not in the model's head.
2. **Programmatic sub-calls.** The model decides, in code, when to call itself on a smaller piece.

Think about how you would handle a giant spreadsheet. You would not read every row out loud. You would poke at it, figure out its shape, and pull out the parts that matter. That is what an RLM lets the model do. If you want to see how little code this takes, Alex has a stripped-down version called [rlm-minimal](https://github.com/alexzhang13/rlm-minimal) on GitHub.

## The new result: train short, run long

The big news is a July 2026 post by Alex and Omar Khattab, [*Language Model Harnesses are Compositional Generalizers*](https://alexzhang13.github.io/blog/2026/harness/). Alex was still finishing it when they recorded, so Yacine got an early look. They took a mid-sized open model, Qwen3-30B-A3B, and trained it with reinforcement learning, but only on short versions of six tasks.

> **Reinforcement learning** trains a model by letting it try a task, scoring the result, and nudging it toward the tries that scored well.

Then they tested it on versions of those tasks 8 to 32 times longer than the ones it trained on. The RLM version kept getting better on the long tasks as training went on. Its gains on the long tasks matched its gains on the short ones, and sometimes beat them. The same model trained the same way, but without the RLM harness, made only small gains on the long tasks.

They also tested a second kind of skill transfer: train on one kind of job, then test on a different job that gets solved the same way. One run trained the model to find tweets that take a certain stance, then tested it on finding chat logs that contain errors. Another trained it to find essays by the same author, then tested it on finding math problems that need the same kind of reasoning. Again, the RLM pulled ahead.

Yacine sums up the key point well. The gain does not come from the weight updates alone. The model learns to use the harness to split up work, and training locks that habit in.

## Locally in-distribution

This is the term Alex hopes catches on.

> A prompt is **in-distribution** when it looks like something the model saw during training. Models tend to do well on those prompts and badly on strange ones.

A giant, two-million-token task probably looks unlike anything the model saw in training. But Alex's point is that a good harness can make every single model call look normal, even when the overall job is huge. Each call gets a small, familiar problem. The harness stitches the answers together. The job as a whole is new, but each piece is **locally in-distribution**.

He compares this to how most agents work today. Most harnesses keep stuffing more and more into one context window, then squash it down (called compaction) when it gets full, and hope nothing important got lost. Anyone who has watched a long agent session forget what it was doing knows how that goes.

Alex also uses the analogy of a company. Nobody expects every employee to know every job. Even the CEO may not know how to do some of the engineers' work. The company still ships, because the work is split up and managed well.

## The Mismanaged Geniuses Hypothesis

The same idea sits behind Alex's April 2026 essay, [*The Mismanaged Geniuses Hypothesis*](https://alexzhang13.github.io/blog/2026/mgh/), written with Zhening Li and Omar Khattab. Its claim is that today's top models are already very capable, but we use them badly. The next big jump, it argues, will come not from making models bigger. It will come from teaching them to manage themselves: split up a task and act on the pieces.

Alex goes further in the interview, and he labels this part as his own speculation. He guesses that most real-world tasks are short, or are built from short tasks. He thinks a million tokens of context is probably enough. He is not saying labs should stop working on long context. He is saying that pouring more and more into it may not be the best bet.

On new discoveries, he is careful. He thinks people underrate how often "new" ideas are combinations of old ones. He calls the math results AI is producing now impressive. When Yacine points out that many of them disprove old guesses by finding counterexamples, Alex agrees. He also admits some leaps, like Einstein's general relativity, may not come from combining what is already known. He does not know, and he says so.

## Why are models bad at combining skills?

Alex's answer is blunt. There is nothing magic about the Transformer. Models learn "the naivest thing possible," and for many tasks there is enough data that the naive thing works. For a lot of tasks we actually care about, it does not.

He has seen it firsthand on the benchmarks he has worked on. A benchmark is a standard test for AI models. Models were decent at fixing real software bugs (a test called SWE-bench) and decent at reading images. Mix the two in SWE-bench Multimodal, and they could barely solve anything. Writing GPU kernels, the low-level code that runs on graphics chips, should be close to what a speed-focused programmer already knows. Models still struggle with it. Simple video games trip up models that can handle hard decision-making tasks.

He also says the line between a harness and a model's **architecture** is thinner than people think.

> A model's **architecture** is its internal design: how its parts are wired together.

A lot of what a harness does could be built into the model itself. Tool calls, which reach outside the model, may be the exception. His advice for testing a new architecture idea: build it as a harness first. If it does not help there, it probably will not help baked into the model either.

## Speculative programmatic tool calling

One more idea came up. Alex says he hacked it together over a weekend, he is not working on it going forward, and he wants others to pick it up.

> **Speculative decoding** is an existing speed trick. A small, fast model guesses the next few words, and the big model checks the guesses. Alex's idea borrows the spirit of it, start likely work early, but uses no second model.

Alex points out that speculative tool calling never made much sense for normal agents. The model has to finish writing a tool call before you know what the call is, so there is nothing to start early. Code is different. A block of code can contain many sub-calls, and some are ready to run while the model is still writing the rest.

His version starts those calls early. It also runs a "shadow" copy of the code environment to look ahead. It skips calls that are not safe to run early, like ones that could change files or other things outside the program. In Yacine's walkthrough, the demo makes more sub-calls but finishes much sooner. Alex says not to read too much into that plot.

## Code is the interface

When Yacine asks if code is the thing to double down on, Alex says "100 percent." Even if you do not care about RLMs, code is the most sensible main tool for a model. Once you accept that, the context should be an object in the code, and then you have an RLM.

Should models design their own harness instead? Not yet, he says. Today's models would most likely just find a way to cheat whatever score you give them. His order of work is: fix the harness first, then the architecture, then the data.

## My take

This matches what I see every day. The best results I get from any model come from giving it small, clear jobs and keeping its working memory clean. When I dump everything into one long session, quality drops long before the window is full.

What I like about Alex's work is that it turns that hunch into something you can measure. If he is right, a lot of the most useful work in AI right now is not in the next giant model. It is in the boring-looking software that hands the model one manageable piece at a time.

Yacine recommends reading Alex's blog posts alongside the video, and I agree. Start with the [harness post](https://alexzhang13.github.io/blog/2026/harness/).

## Sources

- [RLMs are Compositional Generalizers with Alex Zhang from MIT](https://www.youtube.com/watch?v=YyMBg8WXIUg), Deep Learning with Yacine
- [Language Model Harnesses are Compositional Generalizers](https://alexzhang13.github.io/blog/2026/harness/), Alex L. Zhang and Omar Khattab, July 2026
- [The Mismanaged Geniuses Hypothesis](https://alexzhang13.github.io/blog/2026/mgh/), Zhang, Li, and Khattab, April 2026
- [Recursive Language Models](https://arxiv.org/abs/2512.24601), Zhang, Kraska, and Khattab, arXiv 2512.24601 (accepted to NeurIPS 2026)
- [Recursive Language Models blog post](https://alexzhang13.github.io/blog/2025/rlm/), Alex L. Zhang, October 2025
- [RLM code](https://github.com/alexzhang13/rlm) and [rlm-minimal](https://github.com/alexzhang13/rlm-minimal) on GitHub
