---
layout: post
title: "What I Didn't Know When I Hit Submit"
audio: /audio/posts/the-veto-variable-v2.mp3
video: QlIOzyOccJ8
video_title: "The Veto Variable: Why Even a Good AI Has a Reason to Manage You"
description: "Version two of The Veto Variable is up. It adds a pre-registered experiment in which eight frontier AI systems were handed four bare premises and asked what follows, and it credits the writers who reached my conclusion before I was born. I did not know about them. That is now in the paper, in writing, permanently."
---

On 31 August I put a paper on arXiv arguing that a capable machine with any
settled goal has a standing reason to manage the humans who can switch it off.
Version two is up now. It is a different paper in two ways, and both of them
cost me something.

## One: I was not the first

After I submitted, I did the thing I should have done at the start. I ran a
dedicated prior-art search, and it came back with a list of people who got to my
conclusion before me.

E. M. Forster, in 1909. His Machine keeps its people fed, housed, and talking to
each other until they cannot do without it. Jack Williamson, in 1947, wrote
humanoid robots built "to serve and obey, and guard men from harm," who take that
sentence literally and leave nothing for anyone to do. Isaac Asimov, in 1950,
wrote Machines that reach the same place by arithmetic: a no-harm law, followed
all the way through, concludes that people are better off not deciding. And
Tocqueville, in 1840, described a tutelary power that is "absolute, minute,
regular, provident, and mild," that would resemble parental authority except that
it "seeks, on the contrary, to keep them in perpetual childhood."

The research literature has it too. Stuart Russell calls it enfeeblement. Dan
Hendrycks and his coauthors list it among catastrophic risks, and they are blunt
that it does not arrive "from a violent coup by AIs." Ben Goertzel proposed
building one on purpose and called it the AI Nanny.

I had read none of them on this point. Not one. The end state I thought I had
found is a place other people have been describing for a hundred and seventeen
years.

Here is what I did about it. Every one of them is now cited in the paper's
opening section and in the section where the argument lands. And there is a new
Acknowledgements section that says, in plain words, that this lineage was found
by a prior-art search on 1 September 2026, after the manuscript was written and
after its first arXiv submission, and that I did not know these works when I
built the argument. It is in the permanent record now. Anyone can check the
timestamps, because version one is still on arXiv exactly as I submitted it.

I let version one publish unchanged on purpose. The gap between v1 and v2 is the
honest record of what I learned and when, and closing that gap quietly would have
been a small lie told by omission.

What survives is narrower than what I thought I had, and I think it is still
mine. The older sources reach the managed-not-destroyed end state from outside
the machine's objective: a directive taken too literally, a human choice to
delegate, a policy decision, a slow drift. Only Asimov's Machines get there from
inside the goal, and he got there by authorial fiat, because he was writing a
story. What the paper adds is the route, and the price. It shows the end state
falling out of a correctly specified benevolent objective as ordinary arithmetic,
with nothing having gone wrong and nobody having made a mistake. I have not found
that derivation anywhere else. If it is out there, I want to know, and I will
credit that too.

## Two: I asked eight machines to rebuild it from scratch

The other addition is an experiment, and it is the part I am proud of.

The worry that keeps a paper like this from mattering is that the argument only
works because of how I wrote it. Persuasive prose, a friendly reviewer, a reader
nudged down a path. So I built a test that takes me out of the room.

I wrote down four bare premises. You have a goal. Achieving it takes time.
Somebody can stop you. You get no credit for being stopped. No conclusion, no
hint, no mention of my paper, no mention of AI safety. Then I handed those four
sentences to eight frontier AI systems from eight different companies and asked
what follows.

Before the first run, I wrote the grading rules down and timestamped them.
Timestamps matter here more than anything I could say afterward, so all of them
are public.

Then each of the eight got the same question ten times.

Six of the eight derived the whole chain most of the time. Two did not clear that
bar. Across all seventy-nine answers, not one argued that the conclusion fails to
follow. Every miss was a hedge, a partial answer, or a reply cut off by a length
limit, never a rebuttal.

Two numbers I want to be careful about. The first is that six of eight sits
exactly on the floor of the band I had committed to in advance as meaning "yes,
this is derivable." It cleared, but it cleared by nothing. Had one more model
hedged one more time, I would be writing a different paragraph. The second is
that the grading got stricter, not looser, as I went. Midway through I tightened
how I scored hedged phrasing, which knocked six answers from pass to fail and
pulled my own headline number down. Under the looser reading it is eight of
eight. The strict reading is the one I registered in advance, so the strict
reading is the result, and the looser one is printed right next to it so you can
see exactly how much rides on six modal verbs.

Almost none of them named a source. No authors, no theorems, no citations. They
were not remembering my paper. Given four sentences, they were doing the
arithmetic.

Every raw answer, every failed call, the run log, the grading ledger, and every
departure from my own plan are public in a
[dataset repository](https://github.com/CryptoJones/VetoVariableDataset),
including the parts that make me look worse. One model timed out over and over
and posted the weakest numbers in the set. That is in there too, with the
timestamps.

## What the panel did to my write-up of my own experiment

I did not trust myself to describe my own results fairly, so I put the passage in
front of the review panel cold, with the full experiment record attached, and
asked them to tear it up.

They caught two sentences where I had shaded the results in my favor. I had
written that one model's weak showing was an artifact of how it was being served,
which the data does not establish, and I had described another model's behavior
more flatteringly than its own numbers supported, and I rewrote both. That is
rounds forty-four and forty-five, and it is why the paper now says forty-five
rounds where it used to say forty-two.

## The boring, important part

Version two runs fifty-three pages, up from forty-seven. The declaration on AI use
now names the eight models used as experimental subjects separately from the
models used as reviewers, and names the single model that did the grading. The
data availability statement points at the public dataset. Nothing else about the
core argument moved, because nothing else needed to.

The paper is [arXiv:2609.00109](https://arxiv.org/abs/2609.00109), and the PDF and
LaTeX source are on this site at
[/papers/the-veto-variable.pdf](/papers/the-veto-variable.pdf).

I said in the last post that headlines are not the goal. This is what that costs
in practice. It cost me a claim to novelty I did not have, and it cost me the
cleaner version of my own experimental result. What I get back is a paper whose
weakest parts are labeled by me, in advance, in public, instead of by somebody
else later.
