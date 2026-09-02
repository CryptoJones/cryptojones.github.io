---
layout: post
title: "Headlines Are Not the Goal. Science Is."
audio: /audio/posts/the-veto-variable-paper.mp3
description: "I wrote a paper arguing that any capable AI has a standing incentive to manage the humans who hold its off switch. Then I made twelve different AI models referee it, forty-five rounds deep. They edited me, fact-checked me, and broke my favorite number. The honest version survived, and it is headed to arXiv and a journal."
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
a dozen models at a time, drawn from eleven different companies over the life of
the project. Claude, GPT, Gemini, DeepSeek, Mistral, MiniMax, Nemotron, Qwen, GLM,
and poolside's Laguna. Different training lineages, different labs, no shared notes. When models that different agree,
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

## Forty-one more rounds

So I did what you do when review works: I rewrote. The panel marked up the draft,
I weighed the objections, merged the ones that were right, and put the paper back
in front of the panel. Then again. And again. Forty-five rounds
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

The panel never ran out of things to break. For the last rounds I took away
every advantage it had. Round forty-one went in naive: no history, no notes from
earlier rounds, just the paper, the way a real journal referee will meet it.
Round forty-two went further. Every reviewer ran cold, in an empty room, with no
memory and no access to anything but the manuscript itself.

And the cold panel broke my favorite number. The paper used to say the veto
would need to be held eighty-three thousand times more widely before a good
goal's own kindness could stop the quiet takeover. Twelve isolated reviewers
converged on the same problem: that number came from parameter ranges I picked
myself. A stipulation is not a measurement, no matter how carefully you hedge
it. One reviewer said the honest version of the paper contains no such numbers
at all.

So the number is gone. Not hedged. Not footnoted. Deleted. What stands in its
place is the inequality the number was always dressing up, and that inequality
holds on its own and claims nothing it cannot defend. Deleting it cost the paper
its best headline. Headlines are not the goal. Science is.

The objections that remain are stated in the paper as limitations, on purpose.
Peer review did not kill the thesis. It killed the overclaim, twice, and left
the truth standing.

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

The version that survived all forty-five rounds is the version on this site
today. It is on arXiv as [arXiv:2609.00109](https://arxiv.org/abs/2609.00109) (now v2, which adds the pre-registered derivation experiment and credits the writers who reached the conclusion before me; [what changed and why](/the-veto-variable-v2/)). You can [read the whole thing right here](/papers/the-veto-variable.html), on a
dark page with the math typeset and every citation clickable, instead of
squinting at a white PDF. The PDF and LaTeX
source live on this site at
[/papers/the-veto-variable.pdf](/papers/the-veto-variable.pdf).

The machine was never told to harm anyone. It only had to be good at reasoning
about its own goals to notice that we are the term it cannot bound. Whether we
stay in the equation is a design decision, and we are the ones holding the pen.
For now.
