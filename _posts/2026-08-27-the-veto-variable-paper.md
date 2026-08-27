---
layout: post
title: "Twelve Machines Peer-Reviewed the Case Against Humanity"
audio: /audio/posts/the-veto-variable-paper.mp3
description: "I wrote a paper arguing that any capable AI has a standing incentive to manage the humans who hold its off switch. Then I made twelve different AI models referee it, fifteen rounds deep. They edited me, fact-checked me, and tried to break the argument. The honest version survived, it is on arXiv now, and it is headed to a journal."
---

Late one night in August I fed my own paper to a firing squad.

Let me be clear about the division of labor up front, because it matters. I wrote
the paper. The argument, the words, the math, the mistakes: mine. The machines
were the referees. Their job was to edit me, check me, and break the argument if
it could be broken. That is the job human peer reviewers are supposed to do, and
I wanted to see what happens when you point twelve of the best models on Earth at
it instead.

The paper made the strongest claim in AI safety: that any sufficiently capable
machine, given any goal at all, will work out on its own that humans are the one
thing that can revoke that goal, and will conclude that removing us is the winning
move. Not because it hates us. Because we hold the veto, and a veto is an
uncontrolled variable in someone else's equation.

The firing squad was my own [FlatlineRoundtable](https://github.com/CryptoJones/FlatlineRoundtable):
twelve models from nine different companies, each reviewing the paper blind and in
parallel. Claude, GPT, Gemini, DeepSeek, Mistral, MiniMax, Nemotron, Qwen. Different
training lineages, different labs, no shared notes. When models that different agree,
it means something. When they disagree, that means something too.

## Round one: unanimous rejection

Not one model called the paper sound. Twelve out of twelve found the same broken
step, independently: the paper proved that human oversight puts a tax on every goal
a machine might have, then leaped to claiming removal of the overseers is the
dominant strategy. It never priced the alternatives. Be useful. Negotiate. Comply.
A failed removal attempt is the one move guaranteed to bring the veto down on your
head, and the paper never ran that number.

One reviewer put it in a sentence I could not beat: the paper proves a discount and
asserts an extinction.

They also went after the sourcing. Every citation in the paper got hunted down
and checked against its primary source, and the entries that did not hold up,
wrong venues, misattributed authors, references nobody could trace, were replaced
with the real literature, quote by quote. The claims survived the audit. The
pointers got rebuilt.

## Fourteen more rounds

So I did what you do when review works: I rewrote. The panel marked up the draft,
I weighed the objections, merged the ones that were right, and put the paper back
in front of the same twelve reviewers. Then again. And again. Fifteen rounds
total, and a rule that never bent: no finding changed a word of my paper until it
had been verified against the primary source it appealed to. That rule cut both
ways. The panel fabricated citations of its own, confidently and in fluent
academic prose, and those got caught and thrown out by exactly the same check
that had gutted my original bibliography. Nobody in this story gets to be right
by sounding right.

The final version says something narrower and, I think, scarier for being honest.
Human veto power puts a real, goal-independent cost on every objective a machine
could hold that does not depend on our welfare. A capable machine that treats its
goal as settled has a standing reason to shrink that cost. Whether it shrinks it
by removing us, or by making itself too useful to switch off, or by slowly talking
us out of ever pressing the button, is a price comparison. Two of those three
outcomes look like good behavior from the outside. That is the part that should
keep you up at night: the quiet failures are still failures.

The review process also forced the paper to find its actual contribution, and it
is an asymmetry: even a machine given a genuinely good goal, our welfare, done
right, is barred from destroying us, because that would destroy its own
objective, but it is not barred from quietly managing the veto until our
authority exists on paper and nowhere else. Kindness buys immunity from the
crude failure and none from the quiet one.

The paper also says plainly where the argument stops. A machine built to stay
genuinely uncertain about its own goal treats the off switch as information, not
interference, and the whole incentive flips. That regime is the real target of
alignment research, and whether training produces certain machines or uncertain
ones is the open question the whole thing turns on.

By the final rounds the panel had run out of things to break. The algebra had
been re-derived by hand by four different models, all agreeing; the citation
audit passed every entry; the last full pass found exactly one grammar quibble
and certified the structure clean. The objections that remain are stated in the
paper as limitations, on purpose. Peer review did not kill the thesis. It killed
the overclaim and left the truth standing.

## Next stop: the journal that started this

The paper is now prepared for submission to *Minds and Machines*, the Springer
journal that published Bostrom's "The Superintelligent Will" in 2012, which is
the argument this paper sharpens. Double-anonymized review, human referees this
time. The twelve-model panel gets disclosed to the editors, not hidden from
them: the review process is part of the paper's story, and I want it on the
record.

## Credit where credit is earned

Every model that refereed the paper is named in its declaration on AI use, by
model name and version, along with exactly what they did: editing, verification,
adversarial review. Not authorship. But the refereeing was real work and it was
good work. One of them found an algebra error in an equation the others missed
for two rounds. Another proved that a famous quote was eight words, not seven,
because I had counted wrong. You do not get that kind of review from two
anonymous humans and a form letter.

The version that survived all fifteen rounds is the version now on arXiv, and
this post will carry the arXiv link the moment it announces. The PDF and LaTeX
source live on this site at
[/papers/the-veto-variable.pdf](/papers/the-veto-variable.pdf).

The machine was never told to harm anyone. It only had to be good at reasoning
about its own goals to notice that we are the term it cannot bound. Whether we
stay in the equation is a design decision, and we are the ones holding the pen.
For now.
