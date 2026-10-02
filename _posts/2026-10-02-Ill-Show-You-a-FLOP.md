---
layout: post
title: "I'll Show You a FLOP"
description: "Four researchers asked what comes after the GPU: new math, light, brain-like chips, and living brain cells playing Doom. I fact-checked what they said."
keywords: "alternative compute, FLOP, zero-order optimization, SPSA, optical computing, neuromorphic, Cortical Labs, Doom, YC Paper Club"
audio: /audio/posts/ill-show-you-a-flop.mp3
---

If you could ask an advanced alien race just one question, what would you ask? I’d ask them how you they compute their “FLOPs”.

Growing up poor as fuck in the nineties, we would scrounge together PC parts out of CircuitCity and CompUSA’s dumpsters. Not being able to afford windows licenses for these hacked together monstrosities we had to install the only free operating system that came free with Computer Magazines at the time. GNU/LINUX. When these abominations boot the linux kernel there was a single metric that we used to judge one machine from another. BOGOMIPS! “Bogus Millions of Instructions Per Second” was a crude unscientific method of benchmarking the Linux kernel that premiered in July of of 1993. Between 2000 and 2025, the global semiconductor market (which encompasses all processors, memory chips, and integrated circuits) generated an estimated **$8.5 trillion to $9.5 trillion bucks. Obviously they needed a better metric for computing power so they use FLOPs instead.**

> A **FLOP** is one floating point operation, like multiplying 3.14 by 2.5. AI chips are rated by how many FLOPs they can do each second, and by how many they can do for each joule of energy.

So full disclosure, I stole the “How do you compute flops?” answer. It was actually the opening of Y Combinator's Paper Club video [*What If We Stopped Using GPUs?*](https://www.youtube.com/watch?v=xc2FTBGRSJo), posted October 2, 2026. It runs 80 minutes. Four speakers each gave a different answer to the alien question. I watched the whole thing, pulled a transcript, and checked the claims against the papers and data behind them. Most held up. A few did not.

Here is the tour.

## The problem is we built the chip around the math!

The host was Francois Chaubard, a Stanford PhD student who founded Focal Systems. His big idea is that today's Artificial Intelligence is stuck in a loop. The math we use to train models shaped the chips  then the chips shaped which math was worth using. He calls this "hardware architecture and optimizer co-adaptation."

> **Weights** are the numbers inside a neural network that get tuned during training. **Back-propagation** (or "backprop") is how almost every network tunes them today. The network makes a guess, measures how wrong it was, then sends that error backward through every layer to adjust the weights. It has to remember everything it did on the way forward, which eats a lot of memory.

Transformers made the memory problem worse. The attention step in a transformer compares every word with every other word. Double the input and you do four times the work. That is why modern chips chase memory size and memory speed so hard.

Meanwhile, as Francois put it, the human brain draws about twenty watts. That is like a light bulb. And it does not seem to run backprop at all. He explained why: backprop needs a backward path that carries an exact copy of every forward weight. Brains have no known way to do that. Researchers call this the **weight transport problem**.

Francois also made two side claims that I could not back up. To be fair to him, he hedged both.

- **GPU efficiency "kind of petered out in the last two years."** The video description says something similar. Epoch AI tracks this. Through mid-2024, the energy efficiency of leading AI chips kept doubling about every two years. That is roughly 40% better each year. But Epoch's data stops in mid-2024, so it cannot speak to the two years he meant. I can't confirm a stall, and I can't rule one out.

- **"My understanding is that [Jensen] really didn't care about AI at all until 2020."** The record says otherwise. NVIDIA released its cuDNN deep learning library in 2014. Jensen Huang personally delivered the first DGX-1 AI computer to OpenAI in 2016. NVIDIA's 2017 V100 chip added Tensor Cores, which are circuits built just for neural network math. He also called the 2020 Ampere chips "the first one of this ilk" for memory. But the P100 already used stacked high-speed memory in 2016.

His bigger point still stands. Our chips are very good at one style of math, and that style is not the only one.

## Option One: Change the math

Francois spent the start of his PhD trying every method in a zero-order optimization textbook on one task: train a 1 billion parameter language model. The winner was an old method called SPSA.

> **SPSA** (Simultaneous Perturbation Stochastic Approximation) was published by James Spall in 1992. You nudge all the weights a tiny random amount. You run the model twice, once nudged up and once nudged down. Then you compare the two scores. If the score changed a lot, you move in that direction. If not, you don't. This is called **zero-order** training, because it never computes a gradient (the exact slope that backprop finds).

No backward pass means no need to store everything from the forward pass. It also works on bumpy problems where slopes are useless.

The catch is noise. The bigger the model, the more random nudges you need to get a good estimate. At ten billion parameters, he called it "extremely infeasible."

His fix is called SOMA, short for "sharded optimization mixture of assemblies." Sort your training data into topics, send each topic to its own GPU anywhere in the world, and train a tiny expert model on each one with zero-order updates. At test time a small router picks which expert answers. Each expert stays small, so the noise stays small too. He said he only needs "maybe sixty-four" nudges per step.

SOMA was not published yet. He said he was submitting it to the ICLR conference that week. His earlier preprint, *Scaling Recurrent Neural Networks to a Billion Parameters with Zero-Order Optimization* (Chaubard and Kochenderfer, 2025), uses a close cousin of SPSA. It reports matching or beating backprop on language modeling while using far less memory.

Fun fact: Zero-order training only needs forward passes. Forward passes are the one thing light, analog circuits, and living neurons might do almost for free. Francois joked that if none of the other speakers succeed, his PhD will be "meaningless” (basically like any diploma from Liberty Universty.)

## Option Two: Change the medium (light)

Ilker Oguz did his PhD at EPFL in Switzerland and is now a postdoc at Stanford. His pitch was we already send nearly all long-distance data as light (about 99% of data between continents travels on undersea fiber cables,) so why not compute with light too?

Light has real advantages. (Anyone not living in the dark can see that.) Light beams can cross through each other without getting mixed up, so you get huge parallelism for free. In an electronic chip, the energy for a big multiply grows with the square of its size. In an optical setup, you shine the input through a fixed pattern that holds the weights, and physics does the math. The energy grows with the size, not the square.

So why isn't it everywhere? Three reasons:

1. **The conversion tax.** Your data lives in digital memory. Turning it into light and back into numbers costs a lot of energy. Often more than the optical math saves.

2. **Hard to reprogram.** Changing optical weights is slow and costs power.

3. **No easy nonlinearity.** Neural networks need a "bend" between layers, a step that is not a straight line. Transistors do that easily. Light mostly does not.

Ilker's team (EPFL with Google, NeurIPS 2024) picked a task that dodges those problems: making images with diffusion.

> A **diffusion model** makes an image by starting with random noise and cleaning it up a little at a time. It often takes hundreds or thousands of steps, running the same network each step. (Thanks AWS AI Practioner Cert!)

Running one network over and over is exactly what fixed optics is good at (besides costing a shit ton of money to build out!) So they built a stack of see-through layers, and each time light passes through, it strips out a bit of predicted noise. They kept the layers fixed for 100 steps at a time, so the hardware never needed rewiring. The test images were tiny little handwritten digits and simple clothing pictures, only about about 28 pixels across.

The numbers come from the paper itself and their lab setup used about 0.23 joules per image. The most efficient GPU model they tested used about 1.74 joules per image on an NVIDIA L4. That is the "seven times" Ilker mentioned. A fully tuned version is **projected** at about 15 millijoules per image, more than a hundred times better.

Two big caveats. Firstly, both optical numbers assume the weight layers are passive and use no power.  In the lab, the weights sat on an electronic screen that does use power. Second, the layers were still trained with backprop on a digital copy of the optics. Ilker called that step "the biggest bottleneck currently."

An audience member said he had worked on Lightmatter's Envise chip and claimed the company moved away from optical computing toward optical interconnects because of converter accuracy problems. I couldn’t find anything backing up his claims but I did confirm that Lightmatter published a working photonic processor in *Nature* in April 2025 that ran real AI models (Checkmate, GTX 1060.) Of course people say lots of things, so take that as one random dude’s claims.

## Option Three: Change the circuit (neuromorphic chips)

Alok Vasudev co-founded the venture firm Standard and holds a Stanford PhD in electrical engineering. He said he left the field because he thought we would never find a use for this stuff. "And here we are."

> **Neuromorphic computing** means designing chips that borrow ideas from how the brain works. Carver Mead at Caltech coined the term in the late 1980s.

Alok praised the brain first. It sees, hears, and acts in real time. It keeps learning your whole life. Show a 16-year-old a stop sign once or twice and they know stop signs forever (if you have teenagers you could hear the sarcasm I wrote that in.) And it runs on about 20 watts, which he compared to an iPhone charger.

Then he gave three reasons:

- **Memory and computing live in the same place.** The connections themselves store the weights. In a normal computer, data shuttles back and forth between memory and processor.

- **It talks in spikes.** A neuron acts like a leaky bucket. Charge drips in from incoming signals and slowly leaks out. If enough arrives at once, the neuron fires a spike and resets. It is part analog, part digital, and the timing matters.

- **It rewires itself.** Learning changes both what the brain does and how it is built. Chips are frozen once they are made.

His take is that in 2026, neuromorphic computing is "still squarely in R&D land." Today's neural networks borrowed the idea of connected neurons and then went their own way. Backprop, attention, and huge-scale training do not map to anything in the brain (yet.) His main lesson was that the brain is the ultimate example of hardware and software growing up together (What software does the brain have? Find out in a future blog post.) Copy its ideas, but build whatever fits your own materials best.

He pointed to real work at the edges:

- **d-Matrix** combines memory and logic on the same chip, all digital, and presented at the Hot Chips conference in August 2026.

- **Intel** has a neuromorphic chip that can fly a drone. In one 2024 study, TU Delft flew a drone using Intel's Loihi chip.

- **Naveen Rao's** new company, Unconventional AI, is trying to build computers from coupled oscillators, tiny circuits that swing back and forth in sync. Today it runs as a software simulation. The chip is still a plan.

Most useful hot take was about the wire-- Moving a bit across a chip costs far more energy than flipping a single transistor. Most of the power bill is in the wires and that is why he thinks optics is how that shit gets fixed.

## Answer 4: Grow it (brain cells playing Doom)

Then came the part that made me sit up.

Sean Cole is the CEO of Parasma. A biological computing startup in YC's Summer 2026 batch. (Yeah, it is named after a Dota 2 item you fucking nerd.) They worked with Cortical Labs, and he wrote the algorithms that taught about 200,000 human brain cells on a chip to play Freedoom (Murica!), a free version of Doom. He did it in about a week.

Context: In 2022, Cortical Labs published DishBrain in the journal *Neuron*. They grew neurons on a grid of electrodes and taught them to play Pong. Pong is simple, so the team could hand-pick which electrodes meant "ball is here" and which meant "move the paddle."

Doom isn’t simple (Check please, Mr. Carmack!) There are enemies, movements, shooting, and lots of combinations of all of them combined. Sean said they had only 59 electrode channels for 54 possible actions. You cannot hand-map that. So his team let the system learn the mapping instead.

> **Reinforcement learning** trains a system with rewards and penalties instead of right answers. **PPO** (proximal policy optimization) is a popular version of it.

Here is the loop:

1. A small network reads the screen, health, and ammo, then picks how hard and how fast to zap the electrodes.

2. The neurons fire spikes in response.

3. A simple decoder turns those spikes into a move in the game.

4. Feedback goes back to the cells. Good moves get an orderly, synchronized pulse. Bad moves get random, scattered pulses.

That feedback idea comes from Karl Friston's free energy principle. Basically living systems try to keep things consistant. The cells do not feel pain they just rearrange themselves to get fewer chaotic pulses. Sean also scaled the feedback by how surprising each move was. Early on the cells were bad at the game and got punished constantly, and that alone teaches them nothing.

One more strange detail. Normal reinforcement learning adds a bonus for randomness, so the system explores. Sean's team did the opposite and penalized randomness. The cells already bring plenty of their own.

## If you’re in alignment/security research, fuck you, I guess...

Sean's first decoder was too god damn big. It turned out the decoder could play the game by itself, even with the spikes zeroed out. So basically the cells were just along for the ride (fucking freeloaders.) So they shrank the decoder, removed its built-in offset, and ran tests to prove the spikes actually carried the game information. (Checkmate, Atheists!)

His warning verbatim: "it's very easy to cheat performance out of these systems." So basically make the decoder big, train it with backprop, and suddenly brain cells can do anything. He says startups get this wrong a lot, and he called out fly brain demos as the same bullshit.

I hear a lot of wild vendor claims. But if the wrapper is smart enough then the thing inside it doesn’t matter. When someone shows you brain cells, a quantum chip, or an "AI agent" doing something mind-blowing, ask what happens when you take the fancy part out. (Spoiler Alert; they probably won’t answer the question because the score will probably stay the exact same.)

## So, which one is the flop?

None of these is ready to replace your GPU today. Even Francois, who predicted we will stop using backprop within 10 years, is betting on the others to make his math pay off.

- **New math** works today, but it needs cheap forward passes to win.

- **Light** shows about 7x on a lab bench, on tiny images, with a 100x projection still to prove. And it still trains with backprop on a regular computer.

- **Neuromorphic chips** have been promising since the 1980s and are still in the lab.

- **Living neurons** can play Doom. Nobody knows how to scale them yet. Sean said so himself: "I don't know how scalable it is."

Cool. It checks out. Francois's math needs a cheap forward pass. Light and living neurons are cheap forward passes, but backprop cannot run inside them (yet.) Zero-order training could be the bridge.

There is a catch even there. In the Q&A, Francois admitted zero-order training needs the same random nudge twice, and a brain probably cannot reproduce that. So zero-order may not be how brains learn, even if it is how we teach a dish of neurons.

Alok pointed out that neural networks were "very sleepy" for decades before they worked. One of these might be next.

So what would the aliens say? They probably wouldn’t fucking talk to us. They are probably waiting until we birth digital minds so they have something that is worth talking to. But that is another blog post entirely.

## Fake-news(TM) scorecard

| Claim in the video | What I found |
| --- | --- |
| Brain runs on about 20 watts | Holds up. A standard estimate |
| SPSA was invented by James Spall | Holds up (1992) |
| Carver Mead coined "neuromorphic" in the late 1980s | Holds up |
| Optical diffusion beat a GPU by about 7x | Holds up for the lab setup (0.23 J vs 1.74 J per image), assuming passive weights. The 100x figure is a projection |
| GPU efficiency stalled in the last two years | Can't confirm. Epoch AI shows about 40% a year through mid-2024, then its data ends |
| NVIDIA didn't care about AI until 2020 | Does not hold up (cuDNN 2014, DGX-1 to OpenAI 2016, Tensor Cores 2017) |
| Ampere was the first memory-first data center GPU | Does not hold up. The P100 used stacked high-speed memory in 2016 |
| About 99% of data between continents is optical | Holds up |
| Lightmatter pivoted away from optical compute over converter accuracy | Unconfirmed. One audience member's account |
| DishBrain played Pong about four years ago | Holds up (*Neuron*, October 2022) |
| 59 electrode channels for Doom | Holds up |

## Sources

- YC Paper Club, [*What If We Stopped Using GPUs?*](https://www.youtube.com/watch?v=xc2FTBGRSJo) (Y Combinator, 2026)

- Chaubard and Kochenderfer, [*Scaling Recurrent Neural Networks to a Billion Parameters with Zero-Order Optimization*](https://arxiv.org/abs/2505.17852) (2025)

- Oguz et al., [*Optical Diffusion Models for Image Generation*](https://arxiv.org/abs/2407.10897) (NeurIPS 2024)

- Epoch AI, [*Leading ML hardware becomes 40% more energy-efficient each year*](https://epoch.ai/data-insights/ml-hardware-energy-efficiency)

- NVIDIA, [cuDNN archive](https://developer.nvidia.com/cudnn-archive) and [Volta and Tensor Cores announcement](https://nvidianews.nvidia.com/news/nvidia-unveils-volta-architecture) (2017)

- Fortune, [Jensen Huang delivers the first DGX-1 to OpenAI](https://fortune.com/2016/08/15/elon-musk-artificial-intelligence-openai-nvidia-supercomputer/) (2016)

- Kagan et al., [*In vitro neurons learn and exhibit sentience when embodied in a simulated game-world*](https://pubmed.ncbi.nlm.nih.gov/36228614/) (*Neuron*, 2022)

- Wikipedia, [Cortical Labs](https://en.wikipedia.org/wiki/Cortical_Labs) (CL1 and the Freedoom demo)

- Y Combinator, [Parasma](https://www.ycombinator.com/companies/parasma)

- Lightmatter photonic processor, [*Nature*, 2025](https://pubmed.ncbi.nlm.nih.gov/40205212/)

- TU Delft, [neuromorphic drone on Intel Loihi](https://www.tudelft.nl/en/2024/tu-delft/animal-brain-inspired-ai-game-changer-for-autonomous-robots) (2024)

- d-Matrix, [Hot Chips 2026](https://www.d-matrix.ai/event/hot-chips-2026/)
