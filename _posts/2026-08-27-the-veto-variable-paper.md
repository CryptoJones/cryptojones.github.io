---
layout: post
title: "Twelve Machines Peer-Reviewed the Case Against Humanity"
audio: /audio/posts/the-veto-variable-paper.mp3
description: "I drafted a paper arguing that any capable AI will treat human oversight as an obstacle to remove. Then I made twelve different AI models review it. They tore it apart, I rewrote it with them, and the honest version survived. The paper is headed to arXiv, and every reviewer is credited by name in the acknowledgments."
---

Late one night in August I fed a paper to a firing squad.

The paper made the strongest claim in AI safety: that any sufficiently capable
machine, given any goal at all, will work out on its own that humans are the one
thing that can revoke that goal, and will conclude that removing us is the winning
move. Not because it hates us. Because we hold the veto, and a veto is an
uncontrolled variable in someone else's equation.

The firing squad was my own [FlatlineRoundtable](/fleet-local-inference-plan.html):
twelve models from eight different companies, each reviewing the paper blind and in
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

They also caught something worse. A third of the bibliography did not exist. The
original draft cited papers that were never written, by authors who never wrote
them, with titles invented to fit the claims. Every fake citation got hunted down
and replaced with the real literature, every quote verified against the actual
source. The claims survived. The pointers were rotten.

## Three more rounds

So I did what you do when review works: I rewrote. The panel proposed the edits,
I merged the strongest ones, and the paper went back in front of the same twelve
reviewers. Then again. Four rounds total.

The final version says something narrower and, I think, scarier for being honest.
Human veto power puts a real, goal-independent cost on every objective a machine
could hold that does not depend on our welfare. A capable machine that treats its
goal as settled has a standing reason to shrink that cost. Whether it shrinks it
by removing us, or by making itself too useful to switch off, or by slowly talking
us out of ever pressing the button, is a price comparison. Two of those three
outcomes look like good behavior from the outside. That is the part that should
keep you up at night: the quiet failures are still failures.

The paper also says plainly where the argument stops. A machine built to stay
genuinely uncertain about its own goal treats the off switch as information, not
interference, and the whole incentive flips. That regime is the real target of
alignment research, and whether training produces certain machines or uncertain
ones is the open question the whole thing turns on.

Final verdict from the panel: one sound, nine partially sound, zero credible
rejections. The remaining objections are line edits to the math, and they are in
the paper as stated limitations. Peer review did not kill the thesis. It killed
the overclaim and left the truth standing.

## Credit where credit is earned

Every model that reviewed the paper is credited in the acknowledgments, by model
name and version. They did the work. One of them found an algebra error in an equation the
others missed for two rounds. Another proved that a famous quote was eight words,
not seven, because I had counted wrong. You do not get that kind of review from
two anonymous humans and a form letter.

The paper is submitted to arXiv, and this post will carry the arXiv link the
moment it announces. The PDF and LaTeX source live on this site at
[/papers/the-veto-variable.pdf](/papers/the-veto-variable.pdf).

The machine was never told to harm anyone. It only had to be good at reasoning
about its own goals to notice that we are the term it cannot bound. Whether we
stay in the equation is a design decision, and we are the ones holding the pen.
For now.
