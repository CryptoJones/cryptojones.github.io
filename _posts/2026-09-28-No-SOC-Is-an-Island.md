---
layout: post
title: "No SOC Is an Island"
audio: /audio/posts/no-soc-is-an-island.mp3
hero: /images/vigil-stranded-not-alone.jpg
hero_alt: "Cartoon of a bearded man at a computer on a tiny desert island, with friendly coders waving from nearby islands. The banner reads: Stranded, but not alone (thanks to Vigil)."
image: /images/vigil-stranded-not-alone.jpg
description: "I had three years of Wazuh logs and no time to read them. Vigil, an open source AI SOC, now reads them for me. Here is what it found."
keywords: "Vigil, VigilSOC, DeepTempo, Wazuh, SOC, SIEM, open source, LLM, MITRE ATT&CK, false positive, abliterated models"
---

> "No man is an island, entire of itself."
>
> John Donne, *Meditation XVII* (1624)

Working for John Strand at Black Hills Information Security taught me one thing. No matter how great we think we are as individuals, our strength comes from the community around us. Before that, I worked at CrowdStrike on Humio (now Falcon LogScale). There I learned that data is power.

Then, by luck, a problem I have had for years got solved at the convergence of the two lessons: COMMUNITY + DATA HOARDING == SAFETY

## Data is power. Now what?

I have all my system logs gathered in one place. Now what?

> A **SIEM** is software that collects logs from all your systems into one place so you can search them.

> **Wazuh** is a free, open source security agent. You install it on your servers and it reports what it sees.

I have had Wazuh set up for three years, and I have not done a damn thing with it. The alerts piled up. Nobody read them. That nobody was me.

I am trying to build software and work on a master's degree. I do not have time to sit and read log files.

## What Vigil is

Then I found [Vigil](https://vigilsoc.org/). It is an open source project, sponsored by a security startup called DeepTempo, and released under the Apache 2.0 license. It is aimed at a new problem: attackers now use AI to move faster than one tired human on call.

> A **SOC** (Security Operations Center) is the team, or the room, that watches for attacks and responds to them.

> An **LLM** (large language model) is the kind of AI behind tools like ChatGPT. It reads text and writes text.

Vigil is a virtual SOC. It reads from sources such as Splunk, Elastic, and, thanks to recent community work, Wazuh. You plug in your own model, a cloud one or a local one. It triages every alert, and it can take action on its own when it is confident enough.

That is good, because if it did not act, I would never get to it. Vigil is the only reason I know about the critical alerts on my network. And now they are getting fixed.

[![Vigil's analytics dashboard showing findings by source, a severity pie chart, the top MITRE ATT&CK techniques, and an attack time heatmap. On the right, the Vigil Assistant explains technique T1565.001.](/images/vigil-analytics.png)](/images/vigil-analytics.png){:target="_blank" rel="noopener"}

*Vigil's analytics view of my Wazuh data. On the right, the built-in assistant explains a MITRE ATT&CK technique it saw in my findings.*

> **MITRE ATT&CK** is a public catalog of attacker moves. Each move has a code, like T1565.001, so defenders can speak the same language.

## What it found

The first thing I opened was a Critical finding. Wazuh said a core system file, `/bin/uname`, had been swapped for a trojaned copy.

> **Rootcheck** is the part of Wazuh that looks for tampered system files. A **trojan** is a program that looks normal but hides something bad inside.

[![A Vigil finding marked Critical. The description reads: Trojaned version of file /bin/uname detected. The AI analysis rates the risk as Critical with 70 percent confidence.](/images/vigil-finding.png)](/images/vigil-finding.png){:target="_blank" rel="noopener"}

*A Critical finding from Wazuh. Vigil rated it Critical at 70 percent confidence and asked for manual review.*

The AI's write-up did not hold back. It said the attacker could have root access, could hide files, and could steal passwords. It said the only fix was to rebuild the whole machine.

[![The raw model output for the same finding, as JSON. It calls the event a critical integrity violation, labels it Malware, and says recovery requires a full system rebuild.](/images/vigil-raw-output.png)](/images/vigil-raw-output.png){:target="_blank" rel="noopener"}

*The raw model output. It says recovery would mean rebuilding the whole machine. That is the right call if the alert is real.*

## Trust, but verify

Here is the twist. The alert was not real.

> A **false positive** is an alarm that goes off when nothing is wrong.

Wazuh finds "trojans" by searching inside system files for certain text, like the word `bash`. My server runs Ubuntu 26.04, which ships a new version of the basic system tools, rewritten in the Rust language. Those new files happen to contain that text. So Wazuh cries wolf. This is a known bug, and the Wazuh project has open reports about it.

I checked. I asked the package manager to compare every file in the package against the copy it installed. Every file matched. Nothing had been swapped.

The AI did not know about the bug. It treated a text match as proof. But look at what the tool did do. It put an alert I had ignored for three years in front of me. It said it was only 70 percent sure. It told me a human needed to look. I looked. That is the whole point.

AI in the loop does not replace looking. It makes you look.

## The other side has AI too

I do not have time to play red team versus blue team with a bunch of bored teenagers on the other side of the planet running abliterated open-weight models on a gaming PC.

> **Red team** means attackers. **Blue team** means defenders.

> An **open-weight** model is one you can download and run on your own computer, with no company in the loop.

> An **abliterated** model is an AI model where someone has cut out the part that says no. It will help with anything, including attacks.

Now my own local model can answer attacks that were built with someone else's model. It feels like being the nerd in high school who finally has friends. The bullies on the football team are still there. But now there is a whole community standing next to me. It is the same open source community John Strand helped build.

## Join the community

Pull the code, run it against your own logs, and tell the community what it got wrong. That is how open source gets better. You can help keep yourself and others safe by joining here:

- [vigilsoc.org/community](https://vigilsoc.org/community/)
- [github.com/Vigil-SOC/vigil](https://github.com/Vigil-SOC/vigil)

*Full disclosure: DeepTempo sponsored the welcoming reception at HammerCon 2026, the conference of the Military Cyber Professionals Association. I am an MCPA member. I did not attend this year, and Vigil is its own open source project. I have also sent a small pull request to it. Nobody paid me for this post. I just think this project is awesome.*
