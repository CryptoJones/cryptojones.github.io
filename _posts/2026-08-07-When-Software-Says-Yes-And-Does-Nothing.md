---
layout: post
title: "When Software Says Yes and Does Nothing"
description: "The most expensive bugs do not crash. They accept your request, report success, and quietly do nothing. Here is what running a fleet of AI agents taught me."
audio: /audio/posts/buzz.mp3
permalink: /buzz.html
---

I sent the same message to eight AI agents. Every single send came back successful. Every agent was set up correctly. Not one of them answered.

There was no error. Not on my end, not on theirs. The logs were clean. If you had looked at any part of that system, it would have told you everything was fine.

This is the worst kind of bug, and it does not have a good name. I have started calling it **silent success**.

> **Agent:** a program that reads messages and writes replies on its own, usually powered by a large language model. Think of it as a coworker who lives in a chat room.

## Why a crash is the good outcome

When software crashes, it does you a favor. It tells you something is wrong, and it usually tells you where to look. You get a line number. You get a stack trace. You get a place to start.

Silent success gives you none of that. It gives you a green light and a false belief. You walk away thinking the job is done. The bug does not surface for an hour, or a day, or until someone asks why they never heard back.

The cost is not the fix. The fix is usually one word. The cost is the hours you spend looking in the wrong place, because the system already told you that place was fine.

## First I had to get them off my desktop

I run a small fleet of these agents. They live in a chat app and review each other's work.

The supported way to create one opens a form inside the desktop app. That works, but it leaves you with agents that only exist while that app is running on your machine. Close the laptop and the whole fleet goes quiet. That is fine for trying things out. It is useless for anything you actually want to rely on.

So I pulled the agents out into their own service. Each one now starts on its own in the background and keeps running whether or not the desktop app is open, and whether or not I am at my desk. They are no longer guests inside a program. They are a service.

Getting there meant doing by hand every step the form does for you: making the keys, signing the permission that proves I own each agent, registering it, and setting it to launch on its own. That is where I met silent success for the first time, and it set the pattern for everything after.

The startup script accepted the account key in two formats. One of those two code paths could never run. A single missing option in the script meant the check for that format never matched anything. Hand it a key in that format and you get a short message saying the key is unavailable. Not "wrong format." Not "this branch is unreachable." Just unavailable, which sends you off to check the key itself, which is fine, which is the one thing that is not the problem.

## Three ways it happened again

Once the fleet was running, silent success showed up in three more shapes.

**The permission that gets checked too late.** When I added agents to a channel, they joined as regular members. Regular members are allowed to read but not to post. So an agent would wake up, read the thread, think about it, write a perfectly good reply, and then have that reply rejected on the way out. Nothing was logged. The agent's own log said the turn finished normally. From every angle it looked like an agent that had nothing to say.

**The default that ignores you on purpose.** Sending an agent a direct message does not wake it up. It only wakes on an explicit mention. This is a deliberate design choice and a reasonable one, since it stops agents from reacting to everything. But a plain message is still accepted, still delivered, and then dropped. The send reports success because the send *was* successful. The wake-up is what did not happen.

**The field name that does not exist.** One command returns an ID under a different name than every other command does. My script asked for the name it expected, got back an empty value, and cheerfully built a list of blanks. Nothing failed. The script did exactly what I told it to do, which was not what I meant.

## The rule I use now

When something does not work, my first guess used to be that it broke somewhere I had not looked yet. Now my first guess is the opposite:

> It was accepted and ignored.

That one flip has saved me more time than any tool. Start by asking whether the thing you asked for was quietly declined, rather than hunting for an error that was never written.

There is a practical version of this too. When a system reports success, check what it says it *did*, not just that it said yes. The message send that worked returned an empty list of people to notify. The answer was right there in the response. I just was not reading it, because the word "success" had already told me to stop looking.

## The same mistake, made by a human

The worst version of this was not the software. It was me.

One of my agents seemed to produce nothing during a group review. I checked the channel, saw no post from it, decided that lane was broken, and swapped out the model it was running.

Then I looked at the timestamps. I had checked at 8:20. It had posted at 8:28.

It was not broken. It was slow. And its review turned out to be the best of the seven, including catching two factual errors the other agents had made. I had thrown out the best work in the batch because I ran out of patience eight minutes early.

The software rule and the people rule are the same rule. Wait for the signal that says the work is finished. Do not treat your own impatience as evidence.

## How much of this was my own fault

A fair amount of it. I should say that plainly.

The supported path existed. There was a form, and it worked, and I chose not to use it because I wanted something the form could not give me. Every problem in this post found me on the other side of that decision.

Software gets tested hardest along the route most people take. That route gets the clear error messages, because that is where people complained. Step off it and you are somewhere with fewer signs, not because anyone was careless, but because nobody has been lost there yet.

The key format problem was entirely mine. That was my script, my missing option, my dead code. Nobody else wrote it and nobody else could have warned me. A couple of the others are known to the people who maintain the project and are written down in public. The rest sit in between, real enough, but they only ever bite someone who is automating instead of clicking.

I do not regret the trade. Agents that only run while a window is open were not worth having. But it is worth being honest about what the trade actually costs, because the cost is not usually the work. It is that off the main road, "yes" means less than you think it does. Fewer things are checked. Fewer mistakes have been given a good error message yet. The system is not lying to you. It just has not been taught what to say when you do something unusual.

If you go off the path on purpose, and sometimes you should, budget for that. Not extra coding time. Extra time being wrong about where the problem is.

## If you build things

You cannot always stop silent success, but you can make it louder.

Check permissions when someone asks, not when they deliver. Tell the caller what you actually did, not just that you heard them. If a request is going to be ignored, say so out loud, even when ignoring it is the correct behavior. A response that says "accepted, and no one will be notified" would have saved me an entire afternoon.

Most of all, be suspicious of the word "success." It is supposed to mean the work happened. Often it only means the request was received. Those are very different promises, and only one of them is worth trusting.

None of the problems above were hard. Every one of them was a small, sensible decision made by someone reasonable. That is exactly why they were expensive. Loud bugs get fixed fast, because they are annoying. Quiet ones get to stay.

*Proudly Made in Nebraska. Go Big Red! 🌽 <https://xkcd.com/2347/>*
