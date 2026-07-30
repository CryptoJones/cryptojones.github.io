---
layout: post
title: "America Needs More Than AI Chips"
description: "America protects AI chips, but open models may shape who controls the software. This analysis explores national strategy, business ownership, and the safety tradeoff."
audio: /audio/posts/America-Needs-More-Than-AI-Chips.mp3
---

<div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; margin-bottom:1rem;">
  <iframe src="https://www.youtube.com/embed/lWMebfCc5f4" title="America Needs An Open-Source AI Strategy by CNBC" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute; top:0; left:0; width:100%; height:100%;"></iframe>
</div>

<div style="margin-bottom:1.5rem;"><strong><a href="https://www.youtube.com/watch?v=lWMebfCc5f4">Watch America Needs An Open-Source AI Strategy on YouTube</a></strong></div>

CNBC's video, *America Needs An Open-Source AI Strategy*, makes a sharp argument. The United States has spent years thinking about the physical side of artificial intelligence. It wants faster chips, bigger data centers, and enough power to run them. Those things matter, but they are only the ground floor. The models that run on top may decide who gets to build, learn, and compete.

The video tells this story in three parts. First, it looks at a blind spot in Washington. Second, it asks who owns the knowledge an AI system gains inside a company. Third, it shows an AI industry split over the risks and rewards of open models. Together, these sections point to one larger issue: control.

> **Open weights** means that people can download the learned numbers inside an AI model and run or change the model themselves. This is not always the same as open-source software. The training data, full code, or license may still have limits.

## 1. Washington protects the hardware

The first section says American policy is focused on chips, power, and data centers. That makes sense. AI cannot run without machines. The United States also does not want to depend too much on foreign factories for its most important chips.

But a chip is not an AI strategy by itself. It is more like a powerful engine. People still need a car they can afford to drive, repair, and improve. Open models can give students, small companies, and researchers that chance. They can test an idea without paying a large provider for every request.

The video points to Chinese labs such as [DeepSeek](https://github.com/deepseek-ai/DeepSeek-V3), [Z.ai](https://github.com/zai-org/GLM-5), and [Moonshot AI](https://github.com/MoonshotAI/Kimi-K3). These companies have released models that developers can download or study. Their work is spreading because it is useful and easy to reach. If American builders cannot find a strong open model at home, many will use a foreign one. A ban may reduce one risk, but it can also push talent and new products away from the United States.

The video calls this Washington's blind spot, but the record is more mixed. [America's 2025 AI Action Plan](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf) has a section that supports open-source and open-weight AI. It calls for better access to computing power for startups and researchers. A later [White House progress report](https://www.whitehouse.gov/wp-content/uploads/2026/01/WHOSTP-2025-Wins.pdf) also points to public and private funding for fully open science models.

That does not destroy the video's argument. It makes the argument more exact. The blind spot is not a missing sentence in a policy paper. It is the gap between a promise and a strong system that lasts. The country can lead in chips while losing influence over the software people use on those chips. A serious plan needs steady research funding, government demand for strong American open models, security tests, clear licenses, and tools that help people run models safely.

[Nvidia's Nemotron family](https://developer.nvidia.com/topics/ai/nemotron) is a useful step, as the video notes. Nvidia publishes weights, training data, and technical recipes for these models. Still, one company's product plan is not a national plan. A business can change direction when the market changes. A public strategy should last longer than a product cycle.

## 2. Who owns a company's learning?

The second section moves from national power to business power. Palantir leader Alex Karp argues that companies may pay an AI provider while also giving that provider access to their most valuable work. The video calls this a company's “weights and alpha.” In plain language, that means the special knowledge that helps the company win.

The deeper concern is not only whether a provider trains on customer files. An AI system can learn how a company works. It may discover which data matters, which steps solve a problem, and which workers need to be involved. That pattern becomes part of what Microsoft leader Satya Nadella calls the “learning loop.” [Microsoft's OpenEnv project](https://commandline.microsoft.com/openenv-protocol-reinforcement-learning-environments-evals-recursive-self-improvement/) describes the loop as a lasting asset that a company should own.

> A **learning loop** is the cycle in which a system uses results and feedback to get better at a job.

If that learning stays trapped inside one provider's service, moving to another model can feel like hiring a new team with no memory. The company may still own its files, but it does not fully control what the system learned from them. Prices can rise. Rules can change. A useful feature can disappear.

Open weights can give a company more control because it can run the model on its own systems or hire another company to manage it. That does not make open models free. Servers, security, updates, and skilled workers all cost money. For many businesses, renting a closed model will remain the easiest choice.

The real goal should be the right to leave. A company should be able to carry its data, instructions, test results, and useful memory to a new model. Open models help create that pressure, even when the company never runs one. They give buyers another option, which forces closed providers to earn trust instead of depending on a locked door.

Governments face the same question at a larger scale. A country may not want health, defense, or citizen data tied to a service that another country controls. A local model is not always better, but local control can matter when laws, public records, and national security are involved.

## 3. The industry chooses sides

The final section covers an [open letter called “Open Weights and American AI Leadership”](https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf). Its first list of signers included major technology companies and research groups. Anthropic was not on that list. That disagreement is not a small policy fight. It shows two different ideas about safety.

Supporters say open weights spread power. More people can inspect a model, find weak points, and build defenses. Open models also keep a few large companies from controlling the whole market. They may become the common tools for everyday tasks, while costly closed models handle the hardest work.

Critics point to a real problem. Once model weights are released, they cannot be called back. A bad actor can remove safety limits or adapt the model for a cyberattack or dangerous science. A closed provider can watch for abuse and shut off an account. An open model has no central switch.

[Anthropic's public position](https://www.anthropic.com/news/position-open-weights-models) is more careful than a simple call to close every model. The company says less powerful open models are a public good and says it has never called for a general ban. Its concern is that very powerful weights could help dangerous groups or hostile governments. That concern is supported by its own [tests of biological misuse](https://www.anthropic.com/news/frontier-threats-red-teaming-for-ai-safety), though tests from one company should not end a public debate.

The video also warns against a simple rule that says closed always means safe and open always means dangerous. It describes a security test in which a closed American model caused trouble, while an open Chinese model helped researchers understand the problem. The [Linux Foundation's account of the incident](https://www.linuxfoundation.org/blog/open-models-and-open-weights-are-foundational-to-secure-ai) makes a similar case for giving defenders access to capable tools. One case does not settle the argument. It does show that a company label is not a safety test.

Both sides hold part of the truth. Openness can help defenders study a system. It can also help attackers change it. Closing a model can limit access. It can also hide failures and place too much trust in one company. The [United Kingdom's AI Security Institute](https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber) says weight access helps some safety research, but it also warns that capable open models give cyber defenders less time to prepare. Safety depends on the model's power, the way it is released, the tools around it, and the job it is allowed to do.

That suggests a middle path. Smaller and lower-risk models can be released more freely. Powerful models should face stronger tests before release. Model makers can publish clear reports about limits, training methods, and known dangers. Governments can set rules based on what a model can do, not just whether its weights are open. Researchers have proposed [releasing powerful open models in stages](https://www.nature.com/articles/d41586-026-00679-6), with outside tests before wider access.

## A strategy built on choice

The video's three sections all return to the same question: who has the power to choose? A nation needs a choice beyond foreign models. A company needs a choice beyond one provider. Researchers and the public need enough access to test claims about safety.

America should not treat every open model as harmless. It also should not treat openness as a gift to its rivals. Open weights are part of the basic structure of the AI market. Ignoring them could leave the country with excellent chips and too little control over what runs on them.

The best strategy is not “open everything” or “close everything.” It is to build strong American options, test them honestly, and make sure users can leave when a provider stops serving them. Hardware creates capacity. Choice creates lasting power.

## References

The analysis above draws on these primary and research sources:

* [America's AI Action Plan](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf)
* [Open Weights and American AI Leadership](https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf)
* [Nvidia Nemotron model documentation](https://developer.nvidia.com/topics/ai/nemotron)
* [DeepSeek-V3 model repository](https://github.com/deepseek-ai/DeepSeek-V3)
* [Z.ai GLM model repository](https://github.com/zai-org/GLM-5)
* [Moonshot AI Kimi model repository](https://github.com/MoonshotAI/Kimi-K3)
* [Microsoft's explanation of the learning loop](https://commandline.microsoft.com/openenv-protocol-reinforcement-learning-environments-evals-recursive-self-improvement/)
* [Anthropic's position on open weights](https://www.anthropic.com/news/position-open-weights-models)
* [UK AI Security Institute research on cyber risk](https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber)
* [A staged approach to open-weight releases](https://www.nature.com/articles/d41586-026-00679-6)
