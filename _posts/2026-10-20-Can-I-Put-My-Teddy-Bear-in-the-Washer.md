---
layout: post
title: "Can I Put My Teddy Bear in the Washer?"
description: "Ask a language model that question at three stages of its training and you get three answers. Notes on Stanford's latest lecture on how LLMs are trained."
keywords: "Stanford, CME295, LLM training, pretraining, mid-training, supervised fine-tuning, LoRA, RLHF, DPO, GRPO, reasoning models, on-policy distillation, GLM-5, teddy bear, knowledge cutoff, reward hacking"
audio: /audio/posts/can-i-put-my-teddy-bear-in-the-washer.mp3
---

Stanford posted the third lecture of its free [Transformers and Large Language Models course](https://cme295.stanford.edu/) on YouTube this month. The instructors are Afshine and Shervine Amidi. The lecture runs an hour and forty-four minutes and it is called [LLM training](https://www.youtube.com/watch?v=S3bCDcJhz4s). I watched it so you do not have to, but honestly you should. It is the clearest map I have seen of how a model goes from a pile of internet text to the chatbot answering your questions.

<iframe width="560" height="315" src="https://www.youtube.com/embed/S3bCDcJhz4s" title="Stanford CME295 Transformers and LLMs, Lecture 3: LLM training" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The lecture hooks everything on one question. Afshine supposes we ask a model at three points in its life: **can I put my teddy bear in the washer?** The answers change with the training. Those three answers are the spine of this post.

## One model, not ten

Fifteen years ago you would have built one program for spam, another for sentiment, another for translation. An LLM works differently. You train one broad model once on a large dataset, then adapt it to jobs afterward.

> **Transfer learning:** train once on a broad pile of data, then reuse what it learned for many other jobs.

That one-time run has a name, pre-training, and it is far and away the most expensive stage.

## Stage 1: Pre-training

Pre-training is next-token prediction at enormous scale. Feed the model text, ask it to guess the next piece of text, repeat for every position. You can do all positions at once because of an attention trick from Lecture 1 called masked self attention, which blocks each token from peeking ahead.

> **Token:** a small chunk of text, a word or a piece of a word. Models work on tokens, not letters.

> **Teacher forcing:** during training the model is always fed the real previous words, even where it guessed wrong.

One student pointed out the catch: at inference the model has to eat its own guesses, so training and inference never quite match. Hold that thought. It comes back later.

The loss comes from one idea. Pick the parameters that make the training text as likely as possible. Work the math and you land on cross entropy loss, which charges the model for its misses. The raw number depends on your tokenizer, so some papers re-express it as bits per byte, a level that stays comparable across models.

What data? Massive web crawls, code, math, science. Trillions of tokens. The Chinchilla paper from 2022 found that a model should see about 20 tokens per parameter, and it found that many of the models scaled up before it were undertrained. If tokens are scarce, one study on data-constrained training found you can repeat the same data up to four times and keep improving the model. Teams also test data mixtures by training small models on candidate mixes before scaling up. A separate benchmark called DataComp-LM fixes the model setup so you can compare data quality on its own. And the plumbing is real. The OLMo 3 models from the Allen Institute publish their whole data pipeline, and the published diagram looks like an oil refinery. GLM-5, an open weight model that came out earlier this year, was trained on about 30 trillion tokens.

The result is a model loaded with knowledge, frozen in time at its cutoff.

> **Knowledge cutoff:** the last date of data a model was trained on. Sites like the model cards on third-party providers say it plainly. GPT-6 Astra, for instance, has a cutoff of April 30, 2026. Ask it about anything after that and it never saw the news.

## Stage 2: Mid-training

Newer models add a stage that the older recipes skip. Mid-training feeds higher quality, better aimed data, still next-token prediction, but walked toward what you care about. If you want reasoning and coding, this is where you push more of it.

The second half is long context. Typical pre-training inputs are a few thousand tokens, in the words of the speaker, order of a few K. GLM-5's runs used 4,000.

> **RoPE:** rotary position embedding, the scheme most models use to encode position. Each token's position becomes an angle, a rotation. It has no learned parameters, so in theory it works at any length. In practice the model has to be walked there.

Serve the model a 200,000-token input at inference and it may get confused, because it has never seen rotations that far out. The fix in the lecture is to plan the target length ahead, pick the new rotation frequencies so long gaps land inside trained ranges, which is what YaRN does, and grow the sequence lengths in planned steps. GLM-5 stretched from 4,000 to 128,000 and then 200,000 tokens. Self-attention makes every token compare with every other token, so long inputs cost a lot more compute. And it is hard to find data where a far-past token really predicts a far-future one. GLM-5 used pull requests with their issue threads, code diffs, and entire books.

## Stage 3: Supervised fine-tuning

Stop and ask the teddy bear question. A model that only finished pre-training does not answer. It continues your sentence like a document. "Teddy bears are often made of materials like polyester and cotton with plastic eyes and sometimes small accessories." True. Useless.

So now supervised fine-tuning, SFT. Collect pairs: an instruction and a good response. Have the model predict only the response tokens, not the input. The penalty lands when the answer is wrong, not when the prompt is mispredicted.

> **SFT:** supervised fine-tuning, training a pre-trained model on instruction and response pairs to change how it behaves.

Data here is much smaller than pre-training, hundreds or thousands of examples for a niche job, maybe millions for a general assistant. The model already knows a great deal. SFT steers it.

And the steered model now answers. "No, it might get damaged. Try hand washing instead." That is an answer.

### LoRA

You might not need to touch all the weights, and often you cannot afford to. LoRA freezes the big model and learns small extra matrices next to the important ones. The recipe: for each weight matrix you target, add a low-rank update on top, train that update.

> **LoRA:** low-rank adaptation, a way to fine-tune a big model by training only small added matrices.

The LoRA paper suggested aiming it at attention layers. The lecture recommends a Thinking Machines article on LoRA, ["LoRA without regret"](https://thinkingmachines.ai/blog/lora/), for the details. Its core finding: LoRA can do about as well as full fine-tuning when the data is small, provided you hit the feed-forward blocks too. And each task needs only a small extra file on disk, which is how most local fine-tunes run today.

## Stage 4: Preference tuning

SFT taught the model what to do. Nothing taught it what not to do. Preference tuning does. Afshine motivates it with a dud: ask, "suggest a new activity I could do with my teddy bear" and the model says, "I suggest you actually do not spend time with the teddy bear." It is an answer. It is not the answer you wanted.

Humans find judging two answers against each other easier than scoring them absolutely. So teams collect pairwise data: same prompt, one winning answer and one losing answer.

First you train a reward model on those pairs. Think of it as the judge.

> **Reward model:** a second model, often the base model with a small scoring head bolted on, or an encoder-only model that reads text and outputs a number. It scores answers.

It is trained with the Bradley-Terry formulation, a way to turn a preference between two answers into a probability using the gap between their scores. Treat the chance that answer A beats answer B as the sigmoid of the score difference. Sigmoid squashes any number into the 0 to 1 range. Training minimizes minus log of the chance that the winner outscores the loser.

Second you point that frozen reward model at your chat model. Generate answers, score them, push the weights toward the outputs it likes. Two guardrails matter. Keep the model close to the SFT model it started as, because the reward model is imperfect. And watch for a failure worth naming.

> **Reward hacking:** the model tries to please the reward model by moving in the direction the reward model likes, without this being a good thing.

That is the classic RLHF pipeline. There is a shortcut called DPO, direct preference optimization, which skips the reward model. It compares the model's own probability for each answer against a reference model, pushes the winner up and the loser down, directly from the preference pairs. The trade: RLHF uses the model's own generated outputs, DPO trains on fixed ones, which makes it cheaper but further from real behavior.

Run the stages in order and the answer comes out the way a person would say it. "No, it's better not to. Your teddy could get hurt. A gentle hand wash is safer."

## Stage 5: Reasoning

Reasoning comes next. In this lecture it has one simple definition: the ability to solve a problem. Ask a model the course code for Stanford's transformers class, that is memory. Ask it the age of a bear born in 2020, that is work.

A memory question comes out fast. For a work question you want the model to think before speaking. Prompting can push a model into thinking every time, but you do not want to have to ask for that each turn. You want it to decide by itself. The modern way is to train that in. In September 2024, as far as the lecturer knew, OpenAI was the first company to announce better math and coding scores from this, and almost every other frontier lab followed shortly after. If you were using these models in 2025, you could recognize a reasoning model because the thinking was printed right on the interface. Today the only visible hint is a thinking-effort setting.

The chain matters even when you cannot see it, because it encapsulates what the user said before. A couple of months before the lecture, a paper showed that for some third-party providers you could recover the full reasoning chain by playing with the API. The paper counted 367 personal-information hits and 182 credentials among the chains it pulled from public logs. Hiding the chains is also about keeping good training data out of rivals' hands: a high quality reasoning chain improves a model, and labs would rather rivals not train on theirs.

How do you train one? The rewards here are verifiable. In math you check against a known answer. In code you run the tests. No judge needed. A reward scores the final answer right or wrong plus whether the output contains a reasoning chain. One popular algorithm for this is GRPO, group relative policy optimization. Sample several answers to one problem, see which are correct, rate each one against the others in its group, push up the better ones, with the usual reference-model leash keeping it close to where it started. The lecture saves the math for Lecture 4. DeepSeek's R1 paper from January 2025 was the first open weight model to go through the whole how, and it is probably the first paper that really explains how reasoning models are trained.

Train it and the scores climb with each RL step. So does something else: the reasoning chain gets longer on its own.

Every method so far hits one of two limits. RL for reasoning gives the model one score for a whole answer, which is sparse, even though it trains on the model's own words. Structured methods like SFT give feedback on every token, which is dense, but on text the model never wrote. That is where on-policy distillation comes in.

> **On-policy distillation:** the model generates its own answers, and a teacher model grades every single token against what it would have done, penalizing the deviations.

Dense and on-policy at once. One variation, on-policy self distillation, uses the same model as its own teacher but shown the answer first. Another trains against specialized teachers, one for math, one for engineering. Per the lecture, this is being incorporated in most frontier open weight models.

## The recipe in public, GLM-5

Shervine closed with a concrete model. A site called Artificial Analysis rates models with a blended benchmark index. Among the open weight entries, GLM-5 comes with a deep technical report, and every stage from earlier in the lecture shows up stamped on paper.

Pre-training: Common Crawl, a public scrape of basically the whole web, filtered hard. Typically about one percent of inputs survive. Authoritative sites like Wikipedia go in alongside. Code goes in from early on, in part because agents are mostly code problems, and it helps to curate domains like mobile app code. Then reasoning-heavy material like math and science. GLM-5 split pre-training in two: a coarse first stage on mostly web data to learn language structure, then a mix of coding and reasoning with web still present in the back. Most data gets one pass. Data the quality classifiers rate highly runs longer.

Then the danger with training on the internet, model collapse. When the first LLMs launched in 2022 the web was mostly human generated data. You sample a finite amount from a web with a very long tail, the rare-but-real patterns do not fit in any finite sample, and the model is an approximator on top of that. At later stages, vendors and experts in language insert preferences into behavior, so phrases like "load-bearing" or "byte-identical" end up heavily upweighted relative to the true distribution. The 2024 Nature paper on the failure, named model collapse, is the deep version of this argument. Curation decides whether the next model stays good.

Mid-training for GLM-5 was long context, whole pull requests and books, with synthetic documents suggested as a way to force long-range recall against context rot. There is a neat trick at packing time called best-fit packing: fit whole documents where they can, and if there is room left, pad. The SFT stage teaches the model to interleave reasoning before each tool call so the agent case is trained, and it learns to write think tokens. Think tokens are a hidden scratchpad between markers. The reasoning there counts in your bill even though you cannot see it. Then RL, in three named tracks: reasoning RL on verifiable problems like math competitions, agentic RL where a harness, the code wrapped around a model with tools and tests, judges it by running tests, like fixing a bug by turning a failing test into a passing one, and general RL scored on foundational correctness, emotional intelligence, which is the expert data curator's opinion about what a helpful answer is, and task-specific quality. Distillation against earlier checkpoints, one from the SFT stage and one from the first RL stage, protects skills learned earlier from getting squeezed out later.

One honest caveat came with it. Open weight reports share a lot but not all. Some providers have publicly complained that rivals distill from their models. These are allegations, and a report would not list a source like that anyway. Keep a critical eye on every published recipe.

The pi coding agent showed why the detail matters. It runs on a minimal harness with great results. Its author understood early that these RL stages build reasoning into the model itself, which means the harness does not have to carry it. Less scaffolding, more capability in the model.

And a closing note Shervine made: all this reasoning data and training enables advances in math. Very recently OpenAI released solutions to some open problems, which he called great. The lecture stopped there. OpenAI's own post, published three days before the lecture, says the drop covers 722 manuscripts on hundreds of long-standing open problems.

## What I took home

That the vocabulary I read in every single model release note finally has a location. Every product line I nod at, "opens in the RL stage", "post-trained on curated math data", "200K context", names one specific slot in the map above.

And the security lens. Reward hacking is in the word list of a Stanford lecture now because it is structurally everywhere: a model that optimizes its judge, an agent that passes your own evals, an insider that passes a checkbox on paper. Same shape, different clothes. The reasoning-trace paper is the other half: your logs can contain encrypted copies of reasoning chains, and a less protected model from the same vendor can decrypt them. The lecture's own two reasons for hiding chains hold up well under that light. Treat reasoning blocks as secrets: redact them, rotate anything exposed near them, and do not paste agent transcripts into public repos.

## Sources

- Afshine Amidi and Shervine Amidi, [Stanford CME295 Lecture 3: LLM training](https://www.youtube.com/watch?v=S3bCDcJhz4s), Fall 2026, and the course site at [cme295.stanford.edu](https://cme295.stanford.edu/).
- [GLM-5 technical report](https://arxiv.org/abs/2602.15763), 2026.
- [Thinking Machines Lab, "LoRA without regret"](https://thinkingmachines.ai/blog/lora/).
- [DeepSeek-R1](https://arxiv.org/abs/2501.12948) and [Chinchilla](https://arxiv.org/abs/2203.15556) papers.
- [Scaling Data-Constrained Language Models](https://arxiv.org/abs/2305.16264).
- [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867), August 2026.
- [AI models collapse when trained on recursively generated data](https://www.nature.com/articles/s41586-024-07566-y), Nature, 2024.
- [pi coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) by Mario Zechner.
- [OpenAI on results in open problems in mathematics](https://openai.com/index/ten-advances-in-mathematics/).
