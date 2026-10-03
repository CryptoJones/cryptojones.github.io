---
layout: post
title: "A Curious Teddy Bear Is Reading"
description: "Stanford's CME 295 opened with a 104-minute tour from tokens to the full Transformer. Here are my notes on the lecture, in plain English."
keywords: "Stanford, CME 295, transformers, large language models, tokenization, BPE, word2vec, RNN, LSTM, self-attention, query key value, Super Study Guide"
audio: /audio/posts/a-curious-teddy-bear-is-reading.mp3
---

Being Autistic and having ADHD where every I am just becomes a messy disaster. Clothes spread all over. Not knowing where anything is. My second ex-wife has the opposite form of autism where she needs everything to be in order, not moved, and put back in it’s place. My behavior patterns bugged her so much that she gave me the nickname “transformer.” So when I first started learning about LLMs and I saw the word, my first thought was “What the fuck is a transformer?”

If you’re curious about what Optimus Prime has to do with LLMs, Stanford University posted the first lecture of [CME 295: Transformers and Large Language Models](https://www.youtube.com/watch?v=114i2Kz-LZA) for Autumn 2026. It runs one hour and 44 minutes. In that time it goes from “how do you turn words into numbers?” all the way to the full Transformer, the design at the core of today’s large language models.

The teachers are Afshine and Shervine Amidi. They are twin brothers. Both went to school in France at École Centrale Paris, then came to the US for grad school. Afshine went to MIT and Shervine went to Stanford. They have since worked at Uber, Google, and now Netflix. They have taught some version of this class since 2021, and it is now a full Stanford course.

Most of the examples in the lecture come back to one sentence: “**A cute teddy bear is reading.**” So will mine.

## Why I want to follow along and keep up with the meat-space class.

Last year’s lectures are online too. Afshine’s answer was simple: the field moves too fast. This year adds new training methods, AI coding agents, and new kinds of models that write text in different ways. His advice to students was blunt. If you study for the exams, use this year’s lectures.

The class meets Fridays from 3:30 to 5:20. There is no homework. There are two exams, each worth half the grade. The midterm on October 23 covers the first four lectures. The final covers the last five. Last year’s exams are on the [course site](https://cme295.stanford.edu/) as practice.

For background, Afshine asked for some linear algebra (what a matrix is and how to multiply them) and some machine learning basics, like what a neural network and an embedding are. The class reviews those too.

> A **matrix** is a grid of numbers. Multiplying a list of numbers by a matrix turns it into a new list. Most of what happens inside an AI model is lots of these multiplies.

## How we got here

Ten or fifteen years ago, language AI looked very different. There was no one model that did everything. You had one model per job: one to tell if a review was positive or negative, one to translate, and one to find names and places in text.

Then in 2017 a paper from Google called [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762) introduced the **Transformer**. Its big win was that it **scaled**. Give it more data, more computing power, and more parameters, and it kept getting better, much more than older designs did.

> **Parameters** are the numbers inside a model that get adjusted while it learns. A bigger model has more of them.

People took that design and made it much bigger, and that is how today’s large language models (LLMs) came about.

The next turning point was ChatGPT, released in November 2022. Afshine called it a turning point for products. For many people, it was the first time they chatted with an AI. Now, in 2026, he assumed most of the room uses coding agents almost every day. The class will trace that whole path.

## Step one: chop the text into tokens

Models do not understand text. They understand numbers. So the first job is to split text into pieces we can turn into numbers.

> **Tokenization** is splitting text into small pieces called **tokens**. The full list of tokens a model is allowed to use is its **vocabulary**. The number of tokens a piece of text turns into is its **sequence length**.

There are three main ways to do it.

**By word.** Split on spaces: “a,” “cute,” “teddy,” “bear,” “is,” “reading.” It is simple and easy to read. But English has many forms of the same word (“bear,” “bears”), so the vocabulary gets huge. Nothing tells the model that “bear” and “bears” mean nearly the same thing. And any word it never saw while learning is simply unknown. That is called an **out of vocabulary** problem.

**By character.** Split into single letters. Now almost nothing is unknown, as long as every letter is in the vocabulary. The vocabulary is tiny, and typos are less of a problem. But the sequences get very long, and the model’s work grows with sequence length. A single letter also does not mean much by itself.

**By subword.** Split into pieces somewhere in between, like “read” plus “ing.” Related words can share pieces, so “bears” might become “bear” plus “s.” The catch is that you have to learn the pieces from a big pile of training text, so the result depends on that text.

There is a trade-off here. A bigger vocabulary means fewer, longer tokens and shorter sequences. A smaller vocabulary means more, shorter tokens and longer sequences.

Subword is by far the most common choice today. The usual method is **BPE**.

> **BPE (Byte Pair Encoding)** starts with a small vocabulary, like single letters. It finds the two tokens that show up next to each other most often, adds that pair as a new token, and merges them everywhere in the training text. Then it counts again and repeats until the vocabulary is the size you want.

For example, “a” and “n” show up together a lot (“an idea,” “an amazing course”), so “an” becomes a token. One practical tip from the lecture: if you work in many languages, train your tokenizer on text from all of them, or your sequences will come out long.

As a side note that is not from the lecture, BPE started as a data compression trick by Philip Gage in 1994. Sennrich and colleagues [brought it to machine translation in 2016](https://aclanthology.org/P16-1162/).

There are also **special tokens**. An unknown token stands in for anything outside the vocabulary. Beginning-of-sequence and end-of-sequence tokens tell the model when to start and stop writing. A padding token fills out short sequences so they all match in length, which computer chips like. Chat models also use tokens to mark who is talking, the user or the assistant.

How big are vocabularies today? A student asked, and the answer was on the order of hundreds of thousands, something like 200,000.

## Step two: turn tokens into meaningful numbers

The lazy way is a **one-hot encoding**: give each token a long list of zeros with a single 1 in its own slot. The problem is that every token looks equally unrelated to every other token. “Teddy bear” should be close to “soft.” “Book” maybe not.

In 2013, [word2vec](https://arxiv.org/abs/1301.3781) fixed this with a clever trick called a proxy task.

> A **proxy task** is a task you train on not because you care about it, but because learning it teaches the model something else you do care about.

Word2vec trains a tiny neural network. It either guesses a missing word from the words around it, or it guesses the nearby words from a single word.

> A **neural network** is a stack of matrix multiplies with a little math in between. It learns by making a guess, scoring how wrong it was (that score is the **loss**), and nudging its parameters to do better next time.

Afshine walked through a simple version. Start with a word’s one-hot list. Multiply it by a matrix to squeeze it down to a short list of numbers. Multiply that by a second matrix to grow it back to the size of the vocabulary. Then turn those numbers into odds for each possible next word. Do that over a lot of text, and the short list in the middle becomes a useful stand-in for the word. That short list is the word’s **embedding**.

> An **embedding** is a list of numbers that stands for a token. Tokens with similar meanings end up with similar lists.

The surprise was that these embeddings captured real relationships. Paris is to France as Berlin is to Germany, and the numbers show it.

The class then asked: what is wrong with this? A student found the first big problem, and Afshine added the second.

- **One word, one meaning.** “Bank” gets the same embedding in “river bank” and “go to the bank.” Sarcastic “oh, how cute” gets the same “cute” as a sincere one.
- **Word order gets lost.** “The child is hugging the teddy bear” and “the teddy bear is hugging the child” use the same words. Each word’s embedding stays the same no matter where it sits, so the embeddings alone cannot tell you who is hugging whom.

## Step three: RNNs and LSTMs try to remember

**RNNs** (recurrent neural networks) were the main fix in the 2010s.

> An **RNN** reads tokens one at a time. It keeps a running summary called a **hidden state** and updates it after each token. The hidden state is its memory of everything so far.

That solves word order, since the RNN reads in order. But it crams the whole past into one list of numbers that keeps getting rewritten. Things from far back fade. If “it” refers to the teddy bear two sentences ago, the RNN may have lost track.

> The **long-range dependency** problem is when a model has trouble connecting words that are far apart. For RNNs it comes from a deeper training issue called the **vanishing gradient**, where the learning signal gets weaker and weaker as it flows back through many steps, until early steps barely learn anything.

The **LSTM** (long short-term memory, from 1997) added a second memory, the **cell state**, built to carry information longer. It helped, but it did not fully fix the problem.

RNNs had one more flaw. To handle token 100, you must first finish tokens 1 through 99. That one-at-a-time work is slow when you train on huge amounts of text.

## Step four: attention

In the 2010s researchers tried many fixes. The one that stood out was **attention**. Instead of relying only on the hidden state, let the model look straight back at any earlier token and decide which ones matter right now.

Afshine’s example was translation. When you are about to write the French word for “teddy bear,” it would be great to look directly at “teddy bear” in the English sentence. A plain RNN can only see it through the blurry hidden state. Attention gives a direct line.

The 2017 paper went further with **self-attention**, which Afshine called “attention on steroids.” It builds the meaning of each token from **every** token in the same sentence, itself included, all at once. It drops the RNN completely, which is where the title *Attention Is All You Need* comes from. And because no token has to wait for the one before it, the work can be done in parallel during training. That is a big part of why Transformers scaled.

That raises a fair question one student asked: if every token sees every other token at the same time, how does the model know the word order? Hold that thought. We will fix it below.

### Queries, keys, and values

Self-attention uses three lists of numbers for each token.

> A **query** is a token asking, “who here helps explain me?” A **key** is each token’s name tag, used to answer that. A **value** is the information a token hands over if it is picked.

Say the token “teddy bear” asks what best describes it. Its query is compared with every token’s key. “Cute” matches well, so it gets a high score. The scores become weights that add up to one, and the new meaning of “teddy bear” is a weighted mix of everyone’s values, with “cute” counting for a lot.

Where do queries, keys, and values come from? Each token’s embedding is multiplied by three matrices, one for each. The model learns those matrices in training. The query and key lists have to be the same length, so they can be compared number by number.

All of this fits in one formula. Afshine said it is probably the most important formula when it comes to transformers, and noted it came up on a past midterm:

**Attention(Q, K, V) = softmax(Q Kᵀ / √d_k) V**

Here Q, K, and V are the queries, keys, and values for the whole sentence, stacked into matrices. The small ᵀ means “turn the matrix on its side” so the multiply lines up (a student asked about that one too). Step by step:

1.  Multiply the queries by the keys. That gives a score for every pair of tokens.
2.  Divide by the square root of d_k, the length of each key. Without this, the scores grow with longer keys, and the next step gets lopsided and hard to train.
3.  **Softmax** turns each row of scores into weights that add up to one.
4.  Use those weights to mix the values.

He worked the matrix math on the board to show that each row of the result really is that weighted mix.

## Step five: the full Transformer

The original Transformer was built for translation, like English to German or French. It has two halves.

> The **encoder** reads the source sentence and builds a meaning for each token that takes the words around it into account. The **decoder** uses that meaning to write the translation one token at a time.

### Fixing word order

Before anything enters the encoder or decoder, each token’s embedding gets a **position embedding** added to it. That is how the model knows where each token sits. The token embeddings themselves are learned along with the rest of the Transformer.

There are two kinds. One is learned, but it only has entries for positions it saw in training, so it has nothing for a longer input. The other uses sine and cosine waves of different speeds. Afshine compared it to a watch. The hour, minute, and second hands turn at different speeds, and together they tell you the exact time. Waves at different speeds work the same way for positions. As a bonus, nearby positions tend to look alike. The paper itself, not the lecture, reports that both kinds scored about the same, and it went with the waves.

### The encoder

Each encoder block has two parts:

1.  A **self-attention** layer, where every token looks at every token.
2.  A **feed-forward network**, a small neural network applied to each token. It makes the list of numbers longer, bends it with a simple math rule, and shrinks it back. That bend lets it learn patterns a plain multiply cannot.

> A **layer** is one step in the model’s stack of math. A **block** is a group of layers that gets repeated.

Each block takes in lists of a set length and puts out lists of the same length, so blocks can be stacked. The original paper stacks six of them. The attention is also **multi-head**. The base model runs eight separate sets of queries, keys, and values side by side, joins the results, and multiplies by one more learned matrix to get back to the starting size. Afshine compared this to the many filters in an image model, where each filter looks for something different.

### The decoder

To start translating, you feed the decoder the beginning-of-sequence token. Each decoder block has three parts:

1.  **Masked self-attention.** Each token can look at itself and earlier tokens only, never later ones. When the model is writing, the later words do not exist yet. In training, the model sees the whole correct translation at once, so the “mask” hides the later words. Otherwise it could cheat by copying the next word instead of learning to predict it.
2.  **Cross-attention.** The query comes from the decoder, while the keys and values come from the encoder’s output. This is where the translation looks back at the English sentence.
3.  Another **feed-forward network**.

At the end, the output becomes odds for every token in the vocabulary. Pick the next token (the simplest way is to take the most likely one), feed it back in, and repeat until the model outputs end-of-sequence. Feeding each new token back in like this is called **autoregressive** generation.

A student noticed softmax shows up twice and asked why. Shervine explained they do different jobs. The softmax inside attention decides how much each token listens to the others. The softmax at the very end picks the next word.

### The tricks

Afshine raced through the training tricks that made it all work:

- **Residual connections**: each layer’s output is its input plus a change, instead of a full replacement. That makes deep stacks easier to train.
- **Layer normalization**: keeps the numbers in a steady range so training settles faster.
- **Dropout**: during training, randomly switch off some parts so the model does not lean too hard on any one feature.
- **Label smoothing**: instead of saying the right next word is 100% certain, say it is about 90% and spread the rest thinly over every other word. Language often has more than one good answer. “What a nice day” and “what a nice evening” are both fine.

### What actually matters?

Near the end a student asked: this all looks complicated, so what really makes it work? Shervine boiled it down to two things. First, attention, which the paper’s title already hints at. Second, the feed-forward networks, which hold most of the model’s parameters and do much of the learning. The rest are tricks to train it better. And, he added, the quality of the data.

He also gave a preview. In the next lectures, many of these parts get dropped, and modern LLMs repeat a smaller set of them over and over.

## My take

This first hundrend minute class was a lot for my smooth brain to process. Afshine said so himself: it is probably one of the hardest in the course, because it packs in so many new ideas. But the path is clear. Words become tokens. Tokens become numbers. Numbers that ignore context are not enough, so RNNs add memory. Memory fades, so attention lets every token look at every other token directly. Wrap that in an encoder and decoder, add position waves and a few training tricks, and you have the 2017 Transformer.

The teddy bear example helps a lot. Most new ideas land on the same six words, so you are only learning one new thing at a time.

Shervine closed by noting that all of this was just 2017. The next lectures cover how these models are trained, and the second half covers how they power the agents we use today. I plan to follow along.

## Go get the books

If you want to follow along too, the Amidi twins wrote the textbook for this class. They also wrote a second book in the same **Super Study Guide** series. Both lean on pictures over long walls of text, and in my opinion that is the same style that makes this lecture work.

- [***Super Study Guide: Transformers & Large Language Models***](https://superstudy.guide/transformers-large-language-models/) (2024, about 250 pages). This is the course textbook. It covers the core of this class: tokens, embeddings, attention, how LLMs are trained, and how they are used.
- [***Super Study Guide: Algorithms & Data Structures***](https://superstudy.guide/algorithms-data-structures/) (about 150 pages). The building blocks of programming: ways to store data, ways to search and sort it, and how to reason about graphs and trees. Great for brushing up before a coding interview or a computer science class.

Both come in dead-trees and as e-books, and Afshine said Stanford’s library has copies of the Transformers book. They also keep a free [Transformers and LLMs cheat sheet](https://cme295.stanford.edu/cheatsheet/) that sums up the whole course. They updated it a couple of weeks before this lecture, and it is translated into 15 languages.

## Sources

- Stanford Online, [*CME295 Transformers & LLMs, Autumn 2026, Lecture 1: Transformers*](https://www.youtube.com/watch?v=114i2Kz-LZA) (2026)
- [CME 295 course site](https://cme295.stanford.edu/), [syllabus](https://cme295.stanford.edu/syllabus/), and [cheat sheet](https://cme295.stanford.edu/cheatsheet/)
- Vaswani et al., [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762) (2017)
- Mikolov et al., [*Efficient Estimation of Word Representations in Vector Space*](https://arxiv.org/abs/1301.3781) (2013)
- Sennrich, Haddow, and Birch, [*Neural Machine Translation of Rare Words with Subword Units*](https://aclanthology.org/P16-1162/) (ACL 2016)
- Hochreiter and Schmidhuber, [*Long Short-Term Memory*](https://www.bioinf.jku.at/publications/older/2604.pdf) (1997)
- OpenAI, [*Introducing ChatGPT*](https://openai.com/index/chatgpt/) (2022)
- Afshine and Shervine Amidi, [*Super Study Guide: Transformers & Large Language Models*](https://superstudy.guide/transformers-large-language-models/) and [*Super Study Guide: Algorithms & Data Structures*](https://superstudy.guide/algorithms-data-structures/)
