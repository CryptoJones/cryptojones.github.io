---
layout: post
title: "Software Fundamentals Matter More Than Ever"
description: "Matt Pocock argues that specs to code makes worse code every pass, that bad code is more expensive than ever, and that five old books fix the ways AI coding fails."
audio: /audio/posts/Software-Fundamentals-Matter-More-Than-Ever.mp3
---

*Matt Pocock gave a talk at the AI Engineer conference called "Software Fundamentals Matter More Than Ever." It is about eighteen minutes long and it is worth every one of them. His message is simple. If you have been worried that AI made your skills worthless, the opposite is true. The old books matter more now than they did before. Here is what he said, and why I think he is right.*

🎥 **[Watch the talk on YouTube &rarr;](https://www.youtube.com/watch?v=v4F1gFy-hqg)**

## The idea he is arguing against

There is a movement right now called specs to code. The pitch goes like this. You write a spec that explains how your app should work. You feed the spec to an AI. The AI writes the code. When something breaks, you do not read the code. You just fix the spec and run it again.

Pocock tried it. He kept peeking at the code anyway. What he found was that each run made the code worse. Then worse again. Run it enough times and you end up with garbage.

He calls this vibe coding wearing a costume. I think that is fair.

## Why it falls apart

He went looking for an explanation in two old books.

The first is *A Philosophy of Software Design* by John Ousterhout. Ousterhout defines bad code as complex code. Complexity is anything about the structure of a system that makes it hard to understand and change. So a bad codebase is one you cannot change without breaking things. A good codebase is easy to change.

The second is *The Pragmatic Programmer*, which has a chapter on software entropy. Entropy is the idea that systems drift toward a mess on their own. Every time you change code while thinking only about that one change, and never about the design of the whole thing, the codebase gets a little worse. Do that a few hundred times and it collapses.

That is exactly what the compiler loop was doing. Every pass was a change made with no thought about the whole.

![The specs-to-code entropy loop: spec to AI to code, re-run, and the code degrades a little more each pass until it collapses](/images/software-fundamentals-entropy-loop.svg)

## Code is not cheap

The slogan behind specs to code is that code is cheap now. Pocock disagrees, and this is the part that stuck with me.

Bad code is the most expensive it has ever been. If your codebase is hard to change, you cannot collect any of the winnings AI is handing out. AI does great work in a good codebase. It flails in a bad one. So good codebases matter more than they used to, which means the fundamentals matter more than they used to.

That is the whole thesis. The rest of the talk is about specific ways things go wrong and which old idea fixes each one.

## The AI built the wrong thing

You have an idea in your head. The AI builds something else.

*The Pragmatic Programmer* says nobody knows exactly what they want. There is a gap between you and the AI, and closing it is really just requirements gathering.

Pocock reached for a third book here, *The Design of Design* by Fred Brooks. Brooks describes something called the design concept. When two people build something together, there is an idea floating between them. It is invisible. You cannot save it to a markdown file. It is the shared theory of what you are making. When you and the AI do not share one, you get the wrong app.

His fix is a skill he wrote called Grill Me. It is two lines. It tells the AI to interview him relentlessly about every part of the plan until they reach a shared understanding, walking down each branch of the design tree and settling decisions one at a time.

The AI then asks him forty questions. Sometimes sixty. He says he has watched it ask a hundred before it was satisfied. That conversation becomes the requirements document. He says he likes this better than the built in plan mode in Claude Code, because plan mode is in a hurry to produce a document and start working.

## The AI talks too much

Second failure. The AI buries you in words and you feel like you are talking past each other.

Pocock says this feels like working with a domain expert in a field you know nothing about. If they build microchips and you do not know what a microchip is, you will translate their words into code that neither of you understands.

The fix comes from domain driven design, which has a concept called a ubiquitous language. Developers, the code, and the domain experts all pull their words from the same model. In practice it is a markdown file listing the terms you and the AI agree on, with real definitions, used everywhere.

So he wrote a skill that scans a codebase, collects the terminology, and writes that file as a set of markdown tables. He keeps it open while planning. He says reading the AI's thinking traces showed it planning better, thinking in fewer words, and shipping code that matched the plan more closely.

## It got built and it does not work

Third failure. Right thing, broken.

The obvious answer is feedback loops. Static types. Give a front end agent access to the browser so it can look at what it made. Automated tests. None of this is new.

The catch is that the AI does not use its feedback loops the way a veteran would. It writes a mountain of code and only then thinks about type checking it. *The Pragmatic Programmer* calls this outrunning your headlights. Driving faster than you can see.

The line I keep repeating since watching this: the rate of feedback is your speed limit.

Test driven development fixes it by force. Write the test. Make it pass. Clean up the code. The AI cannot take giant leaps because the process will not let it.

## Testing is hard because your code is bad

Pocock is honest that testing has always been hard. You have to decide how big a unit to test, what to mock, and which behaviors are even worth testing. Those decisions all depend on each other.

His observation is that good codebases are easy to test. So the way to get better tests is to fix the code.

Back to Ousterhout, who says to build deep modules. A deep module hides a lot of functionality behind a simple interface. You can look inside if you want, and most days you will not need to. A shallow module does very little and still makes you deal with a complicated interface.

A codebase made of shallow modules is a field of tiny blobs. AI is very good at producing exactly that. It is also bad at navigating it. The agent wanders, misses the module that mattered, and never really learns what your code does.

Deep modules are the same code with boundaries drawn around it. Design those interfaces yourself and guard them. The implementation inside can be the AI's problem. He has a skill for this too, one that hunts for related code and wraps it in a deep module.

That kind of codebase rewards TDD, because the boundary you test at is simple.

![Deep modules versus shallow modules: shallow is a field of tiny modules with fat interfaces the AI gets lost in; deep is a few large modules behind simple interfaces you can test at the boundary](/images/software-fundamentals-deep-vs-shallow.svg)

## Your brain is the last bottleneck

Here is the failure I felt in my chest. Everything is working, you are shipping more than ever, and you are exhausted.

Pocock says a sprawling codebase makes this worse because you have to hold all of it in your head alongside the AI. Deep modules let you treat things as gray boxes. Design the interface, then stop reading every line of the implementation. Skip that discipline for anything touching money or safety. For most modules in most apps, a testable boundary and a clear purpose are enough.

He credits this with saving his brain. I believe him.

His fifth tip is the shortest one. Design the interface, delegate the implementation.

## Invest every day

He closes with Kent Beck: invest in the design of the system every day. Specs to code does the reverse. It divests.

His last picture is the one I will keep. AI is a great tactical programmer. It is the sergeant on the ground making the changes. Someone has to be thinking above that, at the strategic level, about where the system is going. That is you. And it takes the same fundamentals people have been practicing for twenty years and longer.

![Who does what: you work at the strategic level — the design of the whole system — while the AI works tactically, writing code, passing tests, and filling in the modules](/images/software-fundamentals-tactical-strategic.svg)

That is a comforting message, and I do not think it is only comforting. I think it is correct. The books are on Amazon. The talk is free. Go watch it.

🎥 **[Software Fundamentals Matter More Than Ever, Matt Pocock, AI Engineer &rarr;](https://www.youtube.com/watch?v=v4F1gFy-hqg)**
