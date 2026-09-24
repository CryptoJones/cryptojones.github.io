---
layout: post
title: "The Smallest Neural Network"
audio: /audio/posts/the-smallest-neural-network.mp3
description: "My first machine learning model was just y = mx + b. Here is how that one line grows into a neural network, explained with nine knobs and no hard math."
keywords: "machine learning, neural network, linear regression, gradient descent, XOR, hidden layer, activation function, beginner"
---

I just started a master's degree in machine learning. Three videos in, my class
had me build my first model in a Jupyter notebook. It predicted a test score from
how many hours a student studied.

When it finished, I wanted to see the model. I wanted to open the file and look
at the numbers inside, the way you can open a model file for a big AI chatbot.

It turns out there was no file. The whole model was two numbers. That surprised
me, so I kept pulling on the thread. This post is where the thread led: from one
straight line to the smallest neural network worth looking at.

## My first model was just a line

The model learned this formula:

```
Score = (4.46 × Hours) + 53.10
```

That is the same `y = mx + b` from algebra class. The slope, `m`, is 4.46. The
starting point, `b`, is 53.10. Every extra hour of studying adds about four and a
half points.

> **Model:** a formula that makes a guess. **Training** is how the computer picks
> the numbers in that formula so its guesses fit the data.

Those two numbers are the whole model. In the notebook they lived in the
computer's memory. When the notebook closed, they were gone, because nothing
saved them to a file. A big AI model is the same idea. It just has billions of
numbers instead of two.

## That line is one neuron

Here is the part that clicked for me. A single straight line is also the
simplest possible piece of a neural network.

> **Neuron:** a tiny math step. It takes an input, multiplies it by a number,
> and adds another number. That is `mx + b` again.

```
  Hours ──(× 4.46)──► ( + 53.10 ) ──► Score
```

So my first model already had the shape of a one-neuron network. But two things
were missing before anyone would call it a real neural network. The first is
how it learns. The second is how it bends.

## Missing piece one: learning by nudging

My class used a tool called scikit-learn. For a straight line, it does not really
"learn" step by step. It solves for the best line in one shot with a formula.

Neural networks cannot do that. They are too tangled for a one-shot formula. So
they learn by nudging instead.

> **Knob:** my word for one of the model's numbers. The official name is a
> **weight** or a **parameter**.

Nudging works like this:

1. Start with the knobs set to anything, even zero.
2. Make a guess.
3. Check how wrong the guess was.
4. Turn every knob a tiny bit in the direction that makes it less wrong.
5. Repeat thousands of times.

> **Gradient descent:** the official name for step 4. It is a rule that tells
> each knob which way to turn, and how far.

I ran this on the same study-hours data from class. Both knobs started at zero.
Here is how they moved:

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5, 7, 8, 10], float)          # hours studied
y = np.array([55, 62, 68, 70, 78, 85, 90, 95], float)   # test scores

m, b = 0.0, 0.0
for step in range(20001):
    guess = m * x + b
    error = guess - y
    m -= 0.01 * (2 * error * x).mean()
    b -= 0.01 * (2 * error).mean()
    if step in (0, 100, 1000, 5000, 20000):
        print(f"step {step:>5}: m={m:6.2f}  b={b:6.2f}")
```

```
step     0: m=  8.29  b=  1.51
step   100: m=  9.12  b= 22.08
step  1000: m=  4.51  b= 52.74
step  5000: m=  4.46  b= 53.10
```

At first the knobs wander. The slope even overshoots up past 9. But the nudges
keep pulling them back, and they settle on 4.46 and 53.10. That is the exact
answer the one-shot formula gave. Two different roads, same place.

This nudging is how every big AI model learns. It is the same loop. It just runs
on billions of knobs instead of two.

## Missing piece two: the squiggle

Some problems cannot be solved with a straight line, no matter how you set the
knobs. The classic example is called XOR.

> **XOR:** short for "exclusive or." The answer is yes when exactly one of two
> switches is on. Both off is no. Both on is also no.

| Switch A | Switch B | Answer |
|:--------:|:--------:|:------:|
| off | off | no |
| off | on | yes |
| on | off | yes |
| on | on | no |

If you draw those four answers on a graph, the two "yes" points sit on opposite
corners. You cannot draw one straight line that puts both yes points on one
side and both no points on the other. A single neuron is stuck.

The fix has two parts. First, add a middle layer of neurons between the input
and the output.

> **Hidden layer:** a row of neurons in the middle. You never see its numbers
> directly. It turns the input into something the last neuron can use.

Second, add a bend after each neuron.

> **Activation function:** a squiggle that bends a straight line into a curve.
> The one used here, called a sigmoid, squishes any number into the range
> between 0 and 1.

The bend matters more than it sounds. Without it, stacking layers of straight
lines just gives you one bigger straight line. The squiggle is what lets layers
add up to something new.

## Nine knobs

Here is the smallest network that can learn XOR. Two inputs go into two hidden
neurons, and those feed one output neuron.

```
   A ──┬──► (hidden 1) ──┐
       ╳                 ├──► (output)
   B ──┴──► (hidden 2) ──┘
```

Count the knobs. Each hidden neuron has two weights and one starting number.
That makes 6. The output neuron has two weights and one starting number. That
makes 3 more. Nine knobs in all.

```python
import numpy as np
np.random.seed(1)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], float)
Y = np.array([[0], [1], [1], [0]], float)

squiggle = lambda z: 1 / (1 + np.exp(-z))

W1 = np.random.randn(2, 2); b1 = np.zeros(2)   # 6 knobs
W2 = np.random.randn(2, 1); b2 = np.zeros(1)   # 3 knobs

for step in range(10000):
    h   = squiggle(X @ W1 + b1)
    out = squiggle(h @ W2 + b2)
    d2 = (out - Y) * out * (1 - out)
    d1 = (d2 @ W2.T) * h * (1 - h)
    W2 -= h.T @ d2;  b2 -= d2.sum(0)
    W1 -= X.T @ d1;  b1 -= d1.sum(0)

print(np.round(out, 2).ravel())
```

```
[0.01 0.99 0.99 0.01]
```

That is no, yes, yes, no. It learned XOR. The nudging loop is the same idea as
before. The only new part is that the nudges have to pass backward through the
squiggles to reach the hidden knobs.

> **Backpropagation:** the method for sending those nudges backward through
> each layer, so every knob knows which way to turn.

## Sometimes it gets stuck

Change the first line to `np.random.seed(0)` and run it again. This time the
answer comes out as `0.01, 0.5, 0.99, 0.5`. Two of the four answers are stuck
on "I don't know."

The seed only changes where the knobs start. From a bad starting spot, the
nudges lead into a dead end, and small nudges cannot climb out. Big models run
into the same kind of trouble. It is just buried under billions of knobs where
you cannot see it.

## Why nobody can read a big model

With nine knobs, you can print every one and, with some patience, work out what
each hidden neuron is doing. One might learn "at least one switch is on." The
other might learn "both switches are on." The output neuron subtracts one from
the other.

Now picture a billion knobs. The recipe is still simple. Guess, check, nudge,
repeat. But nobody set any single knob by hand. Each one landed where it did
after trillions of tiny nudges, and its meaning is tangled up with millions of
others.

That is how people can build something and still not understand its insides.
They built the learning. The learning built the knowledge. Reading that
knowledge back out is a whole research field of its own, called
interpretability, and it is still young.

My first model had two knobs. This one has nine. The distance from here to a
chatbot is mostly scale, and I think that is the most useful thing a beginner
like me can know.
