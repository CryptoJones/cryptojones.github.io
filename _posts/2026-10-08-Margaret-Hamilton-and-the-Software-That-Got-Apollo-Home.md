---
layout: post
title: "Margaret Hamilton and the Software That Got Apollo Home"
description: "Margaret Hamilton led the team that built NASA's Apollo flight software. Here is how her design handled the Apollo 11 alarms, and why she matters to software engineering."
---

Margaret Hamilton led the team that wrote the software for NASA's Apollo spacecraft. That code helped people land on the Moon. She is also often credited with popularizing the term "software engineering."

> **Software engineering** means building programs in a planned, tested, and careful way. It treats code as a real product that must work when things go wrong.

## Who she was

Margaret Hamilton was born in 1936. She studied mathematics. Early in her career, she worked on software for weather prediction. From 1961 to 1963, she worked on SAGE, a United States air defense system. In 1964, she began writing software for NASA's Apollo Guidance Computer. She did this work at MIT's Instrumentation Laboratory, a research lab at the Massachusetts Institute of Technology. She later became Director of the Software Engineering Division.

## The Apollo flight software

NASA's Apollo spacecraft carried an onboard computer. It helped guide the ship to the Moon, land it, and bring it home. Hamilton led the team that built the onboard flight software for two Apollo spacecraft: the command module and the lunar module.

> **Flight software** is the code that runs on a spacecraft during a mission. It handles navigation, control, and the many tasks a ship needs to fly safely.

## The 1201 and 1202 alarms

In July 1969, Apollo 11 began its descent to the Moon's surface. During the descent, the lunar module computer showed warning alarms numbered 1201 and 1202. The alarms meant the computer was overloaded. It had more work than it could finish in time. A rendezvous radar was flooding the computer with data. Accounts of the event disagree on the exact timing.

> A **rendezvous radar** is a radar used to find and meet up with another spacecraft. On Apollo, it helped the lunar module find the command module again in orbit.

Hamilton's software had a design that helped here. It used **priority scheduling**, which means the computer runs the most important tasks first. When the computer got overloaded, it dropped the less important work. Then it restarted the more important jobs from a saved point, called a checkpoint.

> **Priority scheduling** is a way to decide which jobs a computer does first when it cannot do everything at once.

> A **checkpoint** is a saved record of where a job was. The computer can restart from that point instead of starting over.

The computer kept doing its most important work, and the landing went on.

## Designing for mistakes

Hamilton's team built the software to expect trouble. When the computer had too much to do, it did not simply stop. It kept the most important work going.

This idea is simple, but it is hard to do well. It is easy to write a program that works only when everything goes right. Hamilton's work asked a better question: what happens when something goes wrong?

## The name "software engineering"

Hamilton is often credited with popularizing the term "software engineering." The term puts software next to other kinds of engineering, like building bridges or rockets. Those fields depend on careful planning and testing.

## Later work

In 1986, Hamilton founded Hamilton Technologies, Inc. in Cambridge, Massachusetts. Its work built on a method called Development Before the Fact. The method aims to prevent common errors instead of handling them after the fact. Her work there also includes the Universal Systems Language.

On November 22, 2016, President Barack Obama awarded her the Presidential Medal of Freedom. It is the highest civilian honor in the United States.

## What we can learn

Her career offers a few lessons for anyone who writes code:

- **Plan for mistakes.** Ask what happens when something fails, not only when everything works.
- **Protect the most important work.** When a system is overloaded, decide what matters most and keep that running.
- **Treat software as engineering.** Careful planning and testing are part of the job, not extras.

Margaret Hamilton showed that good software is not an accident. It takes careful thought, and her work is still a good model for that thought.
