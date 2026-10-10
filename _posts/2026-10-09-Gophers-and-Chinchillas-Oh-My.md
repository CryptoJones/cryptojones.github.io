---
layout: post
title: "Gophers and Chinchillas, Oh My!"
description: "My study notes on Stanford CME 295 Lecture 2: how the Transformer became today's LLMs, the tricks modern models use, and how they pick each next word."
keywords: "Stanford, CME 295, large language models, BERT, GPT, scaling laws, Chinchilla, mixture of experts, RoPE, grouped query attention, RMSNorm, sampling, temperature, context window, chain of thought"
---

These are my class notes for Lecture 2 of Stanford's [CME 295: Transformers & Large Language Models](https://www.youtube.com/watch?v=GaIeu3npx04). It was taught on October 2, 2026 and runs 1 hour 43 minutes. Lecture 1 built the Transformer from scratch. My notes on that one are in [A Curious Teddy Bear Is Reading]({% post_url 2026-10-03-A-Curious-Teddy-Bear-Is-Reading %}).

Afshine opens by saying this lecture focuses on large language models and how they relate to the Transformer. In other words: how did that one design turn into the LLMs we use every day?

Afshine Amidi teaches the first 80 minutes or so, on how the model is built. His twin brother Shervine takes the last 20, on how the model picks its words and how to prompt it. The teddy bear is back too.

How to use these notes:
- Timestamps are in brackets so I can jump back to the part I forgot.
- The chapter list in the YouTube description is copied from Lecture 1 and does not match this video, so ignore it.
- Afshine mostly says "this paper" without naming it. **Paper names, authors, and years in these notes are mine**, added so I can look them up. Anything marked *(my note)* is also mine, not the lecture's.

## The one-paragraph version

Today's LLMs are mostly just the second half of the Transformer (the part that writes), made huge. Bigger models trained on more text keep getting better, but for a fixed budget there is a best mix of model size and amount of data. To get big without getting slow, many models split their work among "experts," so each word only visits a few small parts of the model. Since 2017, most of the original parts have been swapped for better ones: a new way to track word order, cheaper attention, and a simpler way to keep the numbers steady. When writing, the model picks each next word partly at random, and a setting called temperature controls how random. Good prompts, like giving examples or showing the steps, make answers better without retraining anything.

## Words I need for the rest of these notes

> **Parameters** (or **weights**): the numbers inside a model that get adjusted while it learns.
>
> **Loss:** a score for how wrong the model's guesses are. Training tries to push it down. **Cross-entropy loss** measures how surprised the model was by the real next token. Lower is better.
>
> **Backpropagation:** the method training uses to figure out how to nudge each parameter to lower the loss.
>
> **Vector:** a list of numbers. Every token becomes one inside the model.
>
> **Dot product:** a way to measure how alike two vectors are. Multiply them number by number, then add it all up.
>
> **Softmax:** turns a list of scores into probabilities that add up to 1. Bigger score, bigger probability.
>
> **Head:** attention runs several times side by side, each copy looking for different things. Each copy is a head.

## Quick recap of Lecture 1 [0:00]

- Models read numbers, not text. **Tokenization** cuts text into pieces. Sub-word tokens are the usual choice.
- **Embeddings** turn tokens into vectors. word2vec did this but ignored context.
- **RNNs** read in order but forget the start of long text.
- The 2017 Transformer dropped the step-by-step reading and let every token look at every other token directly, using **attention**. Each token makes a **query** (what am I looking for?), a **key** (what do I have?), and a **value** (what do I pass along?).
- The attention formula, which Afshine says to memorize [1:00:38]: **softmax(QKᵀ / √d) · V**. In words: compare each query to every key (dot products), scale down, turn into probabilities with softmax, then take that mix of the values.
- It was built for translation: an **encoder** reads the source sentence and a **decoder** writes the output one token at a time.

## Part 1: Pulling the Transformer apart [3:40]

The big question: the Transformer was great at translation. Can we use it for everything else? People tried keeping just one half.

### Encoder only: BERT (2018) [5:10]

> **BERT** stands for Bidirectional Encoder Representations from Transformers. "Bidirectional" means each token can look at the words both before and after it.

- BERT keeps only the encoder. A special **[CLS]** token goes at the start. After attention, it has "seen" every other token, so its embedding sums up the whole input.
- Use that summary for a task. Example: is this tweet positive or negative? You can also use a single token's embedding, for example to ask "is this word a noun?"
- **Training happens in two steps:**
  1. **Pre-training** (expensive, done once, tons of data). Two practice tasks that are not the real goal but teach the model how text works:
     - **Masked language modeling (MLM):** hide some words ("A [MASK] teddy bear is [MASK]") and make the model guess them from context. Afshine said the real recipe is a bit more complicated so the model doesn't pick up bad habits. *(My note: BERT swaps 15% of tokens. Of those, 80% become [MASK], 10% become a random word, and 10% stay the same.)*
     - **Next sentence prediction (NSP):** given two sentences, did the second really come after the first? This teaches how sentences connect across a document.
  2. **Fine-tuning** (cheap, per job). Add a small layer on top of [CLS] and keep training on a small set of labeled examples, often just hundreds. *(My note: usually all the weights get nudged, not just the new layer.)*
- **Pros:** strong results, sees context on both sides, fine-tuning needs little data.
- **Cons:** you *must* fine-tune for each job, and there is no obvious way to make it write text. (Lecture 8 will show it can be done.)

### Decoder only: GPT (2018) [14:30]

> **GPT** stands for Generative Pre-trained Transformer.

- GPT keeps only the decoder and treats every job as **text in, text out**. Its only skill is predicting the next token.
- Predicting one token at a time, each based on the ones before it, is called **autoregressive** decoding.
- The big idea: no fine-tuning needed. For the tweet example, just ask "Is this tweet positive or negative?" and paste the tweet. Fine-tuning is optional, to make it better. *(My note: the very first GPT in 2018 still got fine-tuned for each task. "Just ask" really took off with the bigger GPTs that came later.)*

**Decoder only vs. the original encoder-decoder:** both write text, but:
1. In encoder-decoder, the input gets special treatment. Its tokens all see each other (two-way attention). In decoder only, every token sees only itself and the tokens before it (**causal attention**).
2. Decoder only has one less part and treats everything the same, so it is simpler and more general.

People tried both for text in, text out. **Decoder only won.** It is what nearly all of today's LLMs use.

## Part 2: Bigger is better, up to a point [19:50]

### Scaling laws (2020) [19:58]

- A 2020 paper (Kaplan and others, at OpenAI) found that loss drops in a steady, predictable way as you add training tokens, model size, and compute. It is almost a law.
- Bigger models are also **more token-efficient**: they reach the same quality after seeing fewer tokens.
- So from 2020 to 2022, everyone made models bigger.
- Loss here is cross-entropy on next-token prediction.

### FLOPs vs. FLOPS [22:20]

Easy to mix up:
- **FLOPs** (small s) = floating point operations, a *count* of work. Training a big LLM takes on the order of 10^25 (a 1 followed by 25 zeros).
- **FLOPS** (capital S, or FLOP/s) = operations *per second*, a measure of how fast hardware is.

> **Floating point:** how computers store decimal numbers. They only keep so many digits, so tiny rounding errors creep in.

### Chinchilla: most models were undertrained (2022) [23:48]

- Question: with a fixed compute budget, how much should go to model size vs. training data?
- Answer: there is a sweet spot, and most 2022 models were **too big for how much data they saw**.
- Proof: same budget, two models. The smaller one (70B parameters, 1.4 trillion tokens) beat the bigger one (Afshine said "200 and something billion") that saw fewer tokens.
- Rule of thumb: about **20 training tokens per parameter**.
- *(My note: why "Chinchilla"? The paper is Hoffmann and others at DeepMind, which names its models after animals. The big model was Gopher, 280B parameters, trained on 300 billion tokens. The small one they built to test the idea was Chinchilla. Both are small furry rodents. The paper never calls its result a "law." People just named it after the model that proved it.)*
- **How I'll remember it:** a smaller animal that was fed more beat a bigger animal that was fed less. Chinchilla was a quarter of Gopher's size but ate about four times as much text, on the same budget.
- Afshine's side note: this is about *training* cost. If you serve the model to lots of users, you also want it small, because every answer costs compute.
- Q&A: does data quality matter? Afshine said papers disagree, but in his view, for pre-training the amount matters more than the quality. Quality matters more in the later training steps (Lecture 3).

### So what makes it an "LLM"? [27:00]

- **Language model:** assigns probabilities to sequences of tokens, in practice by predicting the next token.
- **Large:** billions to trillions of parameters, trillions of training tokens, lots of GPUs.
- **Architecture:** decoder only. Even the decoder's **cross-attention** layer (which used to read the encoder's output) is removed. What's left, repeated over and over: causal multi-head attention + feed-forward network.

> **Feed-forward network (FFN):** the part of each block where most of the math happens. Attention is where tokens talk to each other. The FFN is where each token gets "thought about" on its own.

## Part 3: Mixture of experts [30:46]

**The analogy:** a room has a math expert, a physics expert, and a biology expert. If I have a math question, do I ask all of them? No. Just the math expert.

- Same idea for models: for each input, only use part of the model. Then the model can be huge without every token paying for all of it.
- A **mixture of experts (MoE)** has several **experts** (small networks) plus a **router**, also called a gate, that decides which experts each token goes to and how much each one counts.
- MoE is older than LLMs. *(My note: the idea goes back to a 1991 paper by Jacobs, Jordan, and others. The sparse version for big networks came from Shazeer and others in 2017.)*
- **Dense MoE** [31:38]: uses every expert, just weighted. Still pays full cost. Not what LLMs want.
- **Sparse MoE** [32:18]: picks only the **top k** experts (k is 1, 2, or some number you choose) and skips the rest. The output is the chosen experts' answers added up, weighted by the router. This is the one LLMs use.
- **Where does it go?** It replaces the **feed-forward network**, because that is where the compute is. Attention is where tokens communicate, so it stays.
- Q&A [35:09]: why not treat attention heads as experts? You could try. Afshine pointed out that not all heads are equally useful, which leads to the GQA trick later in the lecture.
- Routing is **per token**. Each token in a sentence picks its own experts.
- The router learns which experts to pick through normal training (backpropagation).

### Routing collapse [36:36]

> **Routing collapse:** the model keeps sending tokens to the same few experts and ignores the rest.

- Why it happens: experts picked early get trained more, so they get better, so they get picked more. Rich get richer.
- Why it is bad: your real model is smaller than the one you paid for.
- Fix: a **load-balancing loss**, an extra penalty during training that pushes the share of tokens each expert gets toward an even split.
- Q&A [38:34]: picking the top 1 or 2 experts is an on/off choice, so how can training learn from it? A **stop-gradient** treats "the fraction of tokens sent to expert *i*" as a fixed number. Training only learns through the router's probabilities, which *can* be nudged.
- Q&A [43:47]: why is *N* (the number of experts) multiplied in the loss? Both the token fractions and the probabilities are about 1/*N* each, so their sum shrinks as *N* grows. Multiplying by *N* keeps the loss the same size no matter how many experts there are.
- Training MoE models is hard. This is one reason why.

### MoE today [40:04]

- A Mistral paper (Mixtral) showed tokens spread across many experts, which is what you want.
- Some modern models add **shared experts** that every token always uses, for basic work every token needs. That lets the other experts specialize. Afshine noted this is not used everywhere: the biggest model on his slide doesn't use one. *(My note: DeepSeekMoE, 2024, popularized it.)*
- Modern models use **lots of small experts**: 60 to hundreds, instead of 8 or 16. More, finer experts gave better results.
- Top open models as of the lecture: 256 to 384 experts, about 8 active per token, hundreds of billions to a trillion total parameters.
- Q&A: do scaling laws hold for MoE? The 2020 paper tested regular (dense) models. Teams with very different designs run small scaling tests of their own first.

## Part 4: What changed inside the Transformer since 2017 [44:00]

### Word order: from added positions to RoPE [44:30]

Attention links every token to every other directly, so on its own it has no idea what order the words are in. You have to add position info.

**2017 option 1: learned position embeddings.** Learn one embedding per position (1, 2, 3, ...) and add it to the token's embedding.
- Problem: if training only went up to position 512, the model has never seen position 600 and has no embedding for it.

**2017 option 2: sine and cosine formula** [50:01]. The clock analogy: hour, minute, and second hands all move at different speeds, and together they tell you the exact time. Position embeddings work the same way. Early numbers in the list wiggle fast, later numbers wiggle slowly, and together they pin down the position.
- The formula: number 2*i* of the vector for position *m* is sin(ω*ᵢ*·*m*), and number 2*i*+1 is cos(ω*ᵢ*·*m*). The speed ω*ᵢ* gets slower as *i* grows.
- Why it works [53:48]: using the trig rule cos(a − b) = cos a·cos b + sin a·sin b, the dot product of the vectors for positions *m* and *n* comes out to **the sum of cos(ω*ᵢ*·(*m* − *n*))**. It only depends on *m* − *n*. And since cos(0) = 1 is as big as cosine gets, the sum is biggest when *m* = *n*. Close positions look alike, far positions look less alike.
- The formula gives a vector for any position, even ones never seen in training. Both 2017 options performed about the same.

**Why neither is used today:** the position gets added to the token and flows through *every* layer. But only attention cares about position. The FFN doesn't care if a word is at spot 5 or spot 12. Better to apply position info only inside attention.

- Q&A [58:04]: doesn't making far tokens matter less bring back the RNN problem? Not really. Far tokens get a small nudge down but keep their direct connection. Nearby words are usually more relevant, but the model can still look far back.

Options that work inside attention [59:54]:
- **Learned bias (T5):** learn an extra number based on distance and add it to the scores inside the softmax. Same problem as before: it's learned, so it may not cover every distance well. *(My note: T5 actually groups distances into 32 buckets, and everything far away shares one bucket.)*
- **ALiBi** (Attention with Linear Biases) [1:01:41]: the bias is a fixed straight-line function of distance. Nothing to learn.
- **RoPE** (Rotary Position Embedding) [1:02:16]: **this is what's used today.**

> **RoPE** rotates each query and key vector by an angle based on its position. The score between a query and a key still depends on what the two words are. But the *position* part of it depends only on how far apart they are, not on where they sit in the text.

- Rotating a vector means multiplying it by a **rotation matrix**, a small grid of sines and cosines: [[cos φ, −sin φ], [sin φ, cos φ]] turns a 2-number vector by angle φ. Rotate the query by its position *m* and the key by its position *n*, and the math works out so only *n* − *m* is left.
- In more than 2 dimensions, rotate the numbers in pairs, each pair at its own speed (same clock idea).
- Nothing is learned, so the formula works for any position. *(My note: in practice, models still get worse past the length they trained on. That's why tricks like position interpolation and YaRN exist.)*
- Roughly, the attention score shrinks as tokens get farther apart. Not perfectly, but close enough.

### Sliding window attention [1:10:14]

- Attending to everything at every layer is a lot of computation. Instead, each token only looks back a fixed number of tokens. Also called **local attention**.
- Isn't that the RNN forgetting problem again? No, because there are many layers stacked. If layer 1 lets you see 1 token back, layer 2 sees what that token saw, and so on. Each layer reaches farther. It's like the **receptive field** in image networks (CNNs), where each layer sees a wider patch of the picture.
- *(My note: most current models mix sliding-window layers with some full-attention layers, rather than using sliding windows everywhere.)*

### KV cache and grouped query attention [1:13:30]

> **KV cache:** while writing, the model compares each new token's query to the keys of itself and every earlier token. Instead of recomputing those keys (and values) every time, it saves them. That saved memory is the KV cache. (Afshine describes this without using the name.)

- Problem: the cache grows with every token, and multi-head attention stores separate keys and values **for every head**. Memory fills up fast.
- Nobody bothers saving queries, since each query is used once.
- **Multi-query attention (MQA):** all heads share one set of keys and values. (The auto-captions call this "group query attention" too, but from the description it's MQA.)
- **Grouped query attention (GQA):** heads are split into groups, and each group shares keys and values. A middle ground. **Very common today.**
- Original multi-head attention: every head has its own.

### Normalization: pre-norm and RMSNorm [1:18:19]

> **Normalize:** rescale a layer's numbers so they stay in a steady range. That keeps training stable.
>
> **Residual connection:** a shortcut that adds a layer's input to its output, so learning signals (gradients) can flow through the network easily.

- **Post-norm** (2017 Transformer): do the layer, add the input back, *then* normalize. Problem: the normalize step sits on the shortcut and gets in its way.
- **Pre-norm** (today): normalize first, do the layer, then add the original input back. The shortcut stays clean.
- **LayerNorm** (used in the 2017 Transformer): re-center the numbers around zero, re-scale them, then apply a learned scale (gamma) and a learned shift (beta) for each number.
- **RMSNorm** (today): skip re-centering and the shift. Just re-scale by the **root mean square** (square each number, average them, take the square root) and apply a learned scale. Works just as well and is simpler.

### Today's recipe [1:20:50]

| 2017 Transformer | Common choice today |
|---|---|
| Added position embeddings | RoPE |
| Full attention everywhere | Sliding window (local) attention, often mixed with full |
| Multi-head attention | Grouped query attention (GQA) |
| Post-norm | Pre-norm |
| LayerNorm | RMSNorm |
| Encoder + decoder | Decoder only, often with mixture of experts |

## Part 5: How the model picks the next word (Shervine) [1:21:07]

At the end of the decoder stack, a **linear layer** (one big multiply) scores every token in the vocabulary, and softmax turns those scores into probabilities. Now pick one.

### Greedy and beam search [1:22:16]

- **Greedy:** always take the most likely token. Problem: the best word *now* does not always lead to the best sentence overall.
- **Beam search** [1:23:13]: keep the *k* best partial sentences at each step instead of one. Closer to the best overall sentence, without checking every possible sentence.
- **The problem both share:** they're **deterministic**. Same question, same answer, every time. A chatbot that greets everyone with the exact same words feels robotic. Shervine called this mostly a thought experiment, since in real use the context (like the time and date) changes a little each time anyway.

### Sampling [1:26:30]

- Pick the next token at **random**, using the probabilities. Likely words come up often, unlikely ones now and then.
- **Top-k:** only sample from the *k* most likely tokens.
- **Top-p** [1:27:25]: sort tokens from most to least likely, and keep the smallest group whose probabilities add up to *at least* *p*. Example: 0.6, 0.3, 0.1 with *p* = 0.8 keeps the first two.
- In both cases, the kept probabilities get rescaled to add up to 1 before sampling.
- When you *do* want the same answer every time: summarizing text, and **LLM-as-a-judge** grading (a later lecture), where you want the ratings to be consistent.

### Temperature [1:29:01]

> **Temperature (T)** divides the scores before softmax: softmax(score / T). T = 1 is normal.

- **T above 1:** probabilities get **flatter**. More random, more creative.
- **T below 1:** probabilities get **sharper**. Near 0, the top token takes almost everything. T = 0 can't literally divide by zero, so tools treat it as "just take the top token" (greedy).
- So randomness is a dial, not an on/off switch.

### Why temperature 0 doesn't guarantee the same answer [1:31:54]

- In theory, fixed weights + temperature 0 = same output every time. In practice, not always.
- Servers **batch** your request together with other people's. The batch can change the order the math gets added up in.
- Floating point addition is **not associative**, meaning the order you add numbers in can change the answer. (big + small) − big can give 0, while small on its own stays small. Different order, slightly different numbers, sometimes a different word.
- The main cause is a lack of **batch invariance**: the GPU math routines (called **kernels**) give slightly different results depending on how big the batch is. Floating point rounding is why that order change matters at all.
- It can be fixed: kernels built to give the same result at any batch size bring back identical outputs. Recommended reading: Horace He's post *Defeating Nondeterminism in LLM Inference* (Thinking Machines).

### Guided decoding for structured output [1:34:42]

> **JSON:** a common text format for data that programs read, like `{"name": "teddy", "age": 3}`.

- You need valid JSON every time, or the code that reads it breaks.
- Just asking for JSON works most of the time with today's models. "Most of the time" is not 100%.
- **Guided (constrained) decoding:** at each step, only allow tokens that keep the output valid. If JSON must start with `{`, nothing else is allowed first.

## Part 6: Prompting and context [1:35:30]

### Context window [1:36:02]

- **Context:** everything the model sees when predicting the next token. That's your prompt **plus every token it has already written**, since each output token gets fed back in.
- **Context window:** the most context a model can handle. It has to fit the prompt *and* the answer.
- **Output tokens:** the tokens the model generates.
- Rough sizes as of the lecture: around **1 million** input tokens, around **100k** output tokens, and climbing. (Shervine had to redo the slide two days before class.)
- Rules of thumb: 1 token ≈ 3/4 of a word. 1 page ≈ 500 tokens (the lecture's number; other estimates put a full single-spaced page closer to 650). 100k tokens ≈ a book. 1 million tokens ≈ a very big book.
- Why the limit? Mostly computing cost.

### Context rot [1:38:43]

- **Needle in a haystack test:** hide one fact somewhere in a long context and ask the model to find it. The longer the context, the more often it misses.
- Better models help, but this can't be fully fixed. Bury one fact in enough noise and finding it gets hard for anyone.
- That's why **starting a fresh chat** and **context compaction** (shrinking a long chat down to a short summary) still matter.

### In-context learning [1:40:13]

Ways to get better answers without changing any weights:
- **Zero-shot:** just ask.
- **Few-shot:** include a few example questions with answers. The model picks up the format, and maybe the reasoning.
- Few-shot is used less now that **reasoning models** (models trained to think through steps before answering) are better. Downsides: the model can copy your exact examples too closely instead of reasoning, and extra tokens cost money and time. People often turn the examples into written instructions instead.

### Chain of thought and self-consistency [1:41:44]

- **Chain of thought** (2022): show the model examples that include the *steps* to the answer, not just the answer. It copies the step-by-step pattern, and accuracy goes up. Shervine stressed this is much more than a prompting trick. It comes back later in the course with reasoning models and "thinking tokens."
- **Self-consistency** [1:42:31]: generate several reasoning paths and take a **majority vote** on the final answer. More stable, especially for math. It costs several answers' worth of compute, so Shervine framed it as something you'd more likely run offline.

## Things to remember for the midterm

- Attention = softmax(QKᵀ / √d) · V.
- Encoder only = BERT (understand text, needs fine-tuning). Decoder only = GPT (text in, text out). Nearly all LLMs today are decoder only.
- Scaling: bigger and more data = better. Chinchilla says ~20 tokens per parameter, and most 2022 models were undertrained. Smaller animal, fed more, beats bigger animal, fed less.
- FLOPs = amount of work. FLOPS = speed.
- Sparse MoE replaces the FFN. The router picks top-k experts per token. Watch out for routing collapse. Fix it with a load-balancing loss, trained through the router probabilities using a stop-gradient.
- Sinusoidal positions: dot product = sum of cos(ω*ᵢ*(*m* − *n*)), biggest when *m* = *n*.
- RoPE rotates queries and keys, so the position part of the score depends only on *n* − *m*.
- Common modern recipe: RoPE, sliding window, GQA, pre-norm, RMSNorm.
- The KV cache is why GQA and MQA exist.
- Greedy and beam search are deterministic. Sampling with top-k, top-p, and temperature adds variety.
- Temperature 0 doesn't guarantee the same answer, because of batching and floating point math, unless the kernels are batch-invariant.
- Context = prompt + generated tokens, and it must fit in the context window. Longer context brings context rot.
- Few-shot, chain of thought, and self-consistency all improve answers without training.

## Sources

- Stanford Online, [*CME295 Transformers & LLMs, Autumn 2026, Lecture 2: Large Language Models*](https://www.youtube.com/watch?v=GaIeu3npx04) (2026)
- [CME 295 course site](https://cme295.stanford.edu/), [syllabus](https://cme295.stanford.edu/syllabus/), and [cheat sheet](https://cme295.stanford.edu/cheatsheet/)
- Vaswani et al., [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762) (2017)
- Devlin et al., [*BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*](https://arxiv.org/abs/1810.04805) (2018)
- Radford et al., [*Improving Language Understanding by Generative Pre-Training*](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) (2018)
- Kaplan et al., [*Scaling Laws for Neural Language Models*](https://arxiv.org/abs/2001.08361) (2020)
- Hoffmann et al., [*Training Compute-Optimal Large Language Models*](https://arxiv.org/abs/2203.15556) (2022)
- Jacobs, Jordan, Nowlan, and Hinton, [*Adaptive Mixtures of Local Experts*](https://direct.mit.edu/neco/article/3/1/79/5560/Adaptive-Mixtures-of-Local-Experts) (1991)
- Shazeer et al., [*Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*](https://arxiv.org/abs/1701.06538) (2017)
- Dai et al., [*DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models*](https://arxiv.org/abs/2401.06066) (2024)
- Jiang et al., [*Mixtral of Experts*](https://arxiv.org/abs/2401.04088) (2024)
- Raffel et al., [*Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer*](https://arxiv.org/abs/1910.10683) (T5, JMLR 2020; preprint 2019)
- Press, Smith, and Lewis, [*Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation*](https://arxiv.org/abs/2108.12409) (ALiBi, 2021)
- Su et al., [*RoFormer: Enhanced Transformer with Rotary Position Embedding*](https://arxiv.org/abs/2104.09864) (2021)
- Beltagy, Peters, and Cohan, [*Longformer: The Long-Document Transformer*](https://arxiv.org/abs/2004.05150) (2020)
- Jiang et al., [*Mistral 7B*](https://arxiv.org/abs/2310.06825) (2023)
- Shazeer, [*Fast Transformer Decoding: One Write-Head is All You Need*](https://arxiv.org/abs/1911.02150) (MQA, 2019)
- Ainslie et al., [*GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*](https://arxiv.org/abs/2305.13245) (2023)
- Ba, Kiros, and Hinton, [*Layer Normalization*](https://arxiv.org/abs/1607.06450) (2016)
- Xiong et al., [*On Layer Normalization in the Transformer Architecture*](https://arxiv.org/abs/2002.04745) (2020)
- Zhang and Sennrich, [*Root Mean Square Layer Normalization*](https://arxiv.org/abs/1910.07467) (2019)
- Holtzman et al., [*The Curious Case of Neural Text Degeneration*](https://arxiv.org/abs/1904.09751) (top-p, 2019)
- Horace He, [*Defeating Nondeterminism in LLM Inference*](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) (Thinking Machines, 2025)
- Hong, Troynikov, and Huber, [*Context Rot: How Increasing Input Tokens Impacts LLM Performance*](https://www.trychroma.com/research/context-rot) (Chroma, 2025)
- Wei et al., [*Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*](https://arxiv.org/abs/2201.11903) (2022)
- Wang et al., [*Self-Consistency Improves Chain of Thought Reasoning in Language Models*](https://arxiv.org/abs/2203.11171) (2022)
