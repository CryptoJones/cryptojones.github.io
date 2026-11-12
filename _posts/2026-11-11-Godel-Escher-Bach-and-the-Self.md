---
layout: post
title: "Gödel, Escher, Bach and the Self: Is Anybody Home in the Machine?"
description: "Spencer Baum argues that Gödel, Escher, Bach, a book from 1979, matters more than ever. Here is his case, and what it means if you use AI models daily."
audio: /audio/posts/godel-escher-bach-and-the-self.mp3
keywords: "Gödel Escher Bach, Douglas Hofstadter, Spencer Baum, strange loop, AI consciousness, large language models, incompleteness theorem, isomorphism, Eliza effect, next token prediction, M. C. Escher, Lewis Carroll"
---

Spencer Baum is a teacher and a novelist with a YouTube channel. He teaches robotics and math, and right now that means seventh grade math. On November 8 he posted a video, almost 27 minutes long, called [*Is This the Most Important Book of the AI Age?*](https://www.youtube.com/watch?v=_UjsTgu0-VA) The book is *Gödel, Escher, Bach: An Eternal Golden Braid* by Douglas Hofstadter. It came out in 1979.

I build software with language models, and I write this blog. I watched the video with one question in my head. Can a book that old tell me anything about the tools I use today?

One note before we start. This is a reaction to the video, not a review of the book. Everything I say about the book here comes from Baum's telling of it.

<iframe width="560" height="315" src="https://www.youtube.com/embed/_UjsTgu0-VA" title="Is This the Most Important Book of the AI Age? Gödel, Escher, Bach" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Why a 1979 book, and why now

Baum grew up in Albuquerque in the 1970s and 1980s, with scientists all around him. He says that back then the book "seemed like it was everywhere." He calls it "a hefty read": about 700 pages of philosophy, art, computer science, and math. The first print run was only 5,000 copies. Then it won the Pulitzer Prize and the National Book Award.

So why bring it up now? Because we all talk to chatbots, and the fight over AI is loud. Baum thinks one question is hiding under that fight. When, if ever, does an AI become "a being worthy of care and consideration"? He thinks that talk is coming, "maybe sooner than we're ready for it."

> **Consciousness** is hard to pin down. In this post it means having an inner point of view. Baum's plain version of the question is: "Is there anybody in there?"

His best point in this part is about age. Anything written about AI minds today is bent by how the writer feels about chatbots, data centers, or AI slop. A book from 1979 has none of that baggage. Baum calls this "credibility from distance."

> A **large language model** (LLM) is a program trained on a huge amount of text. It writes by picking what comes next, one small piece at a time. ChatGPT and Claude are built on LLMs.

## The question under the book

Baum says there is a popular MIT course based on the book, and that it sums the book up in one question: "How does a self come out of a thing that has no selves?" The course that says it that way is [*Gödel, Escher, Bach: A Mental Space Odyssey*](https://www.youtube.com/watch?v=lWZ2Bz0tS-s), a summer 2007 class led by MIT students Justin Curry and Curran Kelleher. In the first lecture, Curry puts the question as "how does a self come out of things which have no selves?"

Then he makes it personal. You are made of atoms. The atoms form molecules. In his words, "You are an ongoing chemical reaction." And yet: "None of those atoms is conscious." So where did you come from?

## Strange loops

Hofstadter starts his answer with art and music. Baum shows a print by M. C. Escher called *Waterfall*, from 1961. "Follow the water," he says. It runs downhill the whole way, and somehow ends up back at the top.

> A **strange loop** is what happens when you move up or down through the levels of a system and end up where you began. In the book's words, "we unexpectedly find ourselves right back where we started."

Baum says Bach does the same thing with sound. The music climbs through key after key, then lands in the key where it started.

Here is the big claim. Hofstadter says a self is a strange loop. It is a system that builds a model of the world, and then finds a model of itself inside that model. Baum then asks the question the whole video is about: "Can a machine do that?"

## Gödel and the sentence that talks about itself

Next comes an old puzzle: "This statement is false." If it is true, it is false. If it is false, it is true.

In 1931, the mathematician Kurt Gödel did something like that with math. He found a way to make arithmetic talk about itself. He built a math statement that, once decoded, says "this statement cannot be proven."

> **Gödel's incompleteness theorem** says that any set of rules that can do arithmetic, and never proves something false, will have true statements it cannot prove.

Baum puts it this way: "There will always be truths it can't reach." Adding more rules does not fix it. The same trick just builds a new unprovable truth.

Why does this matter for minds? Baum says Hofstadter saw a shape in the proof. A system gets rich enough to describe itself, and then it loops back on itself. If numbers can do that, maybe neurons can. And maybe silicon can too.

## Mechanical mode and intelligent mode

In chapter one, Hofstadter gives the reader a game. You have three letters: M, I, and U. You have a few rules for changing one string of letters into another. You start with MI. Your goal is MU.

Baum will not spoil it, and neither will I. He says he tries it every time he reads the book, and fails every time.

The lesson is about two ways of working. When you follow the rules blindly, you are in "mechanical mode." When you step back and notice what is going on, you are in "intelligent mode." Baum says one of the deepest things about a mind is its ability to "jump out of the system."

Then he points this at AI. When an LLM works a problem, is it grinding in mechanical mode? Or can it jump out?

## Where meaning comes from

Chapter two has another game. A string of dashes and the letters P and Q looks like nonsense. Play with it long enough and it clicks. It is just two plus three equals five, written in a strange alphabet.

> An **isomorphism** is a match between two systems that keeps the information the same. Baum calls it an "information-preserving transformation."

Hofstadter says this is where meaning comes from. Baum quotes him: symbols that start out with no meaning "cannot avoid taking on meaning if an isomorphism is found."

His example is Linear B, the earliest known Greek writing. It was baked into clay tablets when a palace burned around 1200 BC. Nobody gave the code breakers a dictionary. They made guesses. When a guess was right, everything fit.

Baum also explains the short plays inside the book. They star Achilles and a tortoise, and they come from an 1895 piece by Lewis Carroll. In one, the two read a torn fortune cookie. Shift the spaces by one letter and you get a new message. So where does the meaning live? In the message, or in the mind that reads it?

This is where the video got my full attention. Baum says to think about what an LLM is. It was handed billions of pages of symbols "with no dictionary, no eyes, no body," and it found the patterns. He sees that as Hofstadter's idea about meaning, shown true in a way the book never described.

Then he asks the harder question: "But does finding meaning make you a self?"

## Levels: storms, fugues, and tokens

Part two of the book opens with a talk about listening to a Bach fugue.

> A **fugue** is a piece of music with several melodies woven together.

Do you follow one voice, or hear the whole thing? The characters decide they do both. They flip back and forth.

Baum's favorite example is the weather. At the bottom level there are trillions of air molecules bumping around. At the top level there are storms and sunny afternoons. Both are true. But if you track every molecule, "you'd never see the storm." So we group things into chunks. Physicists, chemists, and biologists each chunk the world their own way. As Baum says, "Every level is real."

Then he shows Escher's *Relativity*. Each staircase makes sense alone. Hofstadter calls them "islands of certainty." Put them together and the world is impossible.

Here is the payoff for AI.

> A **token** is a small chunk of text, often a word or part of a word. An LLM writes by guessing the next token, again and again.

People say an LLM is "just predicting the next token." Baum agrees that it is true. But he says that is "the molecule level description." It is like saying a storm is just molecules, or that you are just neurons firing. It is true, and it tells you very little about the top level.

## Symbols that trigger each other

In chapter 11, Baum says, Hofstadter starts to pull it together. On paper, symbols sit still and the rules live in your head. A brain is different. He quotes the book: "In the brain, the rules are mixed right in with the symbols themselves."

Ideas are active. Someone tells you about the dog they had as a kid, and a whole network in your brain lights up and builds your own version of that dog.

That leads to a big line from the book. It says consciousness comes up in a system when there are "symbols in the system which obey triggering patterns."

Baum reads that line twice. Then he asks what an LLM is, if not "an enormous web of symbols that trigger each other?"

He adds one more detail I liked. Escher said the creatures he drew seemed to control him. He called them "difficult and obstinate." Baum writes novels, and he says his characters do the same thing to him.

## Baum's answer: no, not yet

After all that, you might expect Baum to say the machines are awake. He does not. He says, "no is where I'm at."

His reason comes straight from the book's own test. When a model makes one word, "the information flows in one direction." It goes in the bottom, passes through dozens of layers (the stacked steps of math inside the model), and comes out the top. In his words: "There's no strange loop. It doesn't sit there and ponder." And when the chat ends, there is no lasting "I" that carries memories into tomorrow.

He also shares an opinion about what AI is good at. He says it is amazing in "closed systems." Those are places with clear rules and answers that can be checked, like software and math. In open, creative work with no clear rules, he thinks the best AI output still falls short of the best human work, unless a person is guiding it.

Then he argues with himself, which I respect. The newest models do loop more. Each word the model writes is fed back in to help pick the next word. "The output becomes the input."

> A **recursive loop** is a process that feeds its own output back in as its next input.

> A **reasoning model** is an LLM that writes out its thinking steps, reads them back, and can change course before it answers.

Baum says that is a loop, but "a recursive loop, not really a strange loop." A reasoning model that catches its own mistake looks a bit like jumping out of the system. To him it is not. The system just has new rules about going back to check. He admits this is not settled: "It's hard and we're bound to argue about it."

## What Hofstadter thinks now

This part is Baum's report. He does not name the pieces. They are filled in here.

For decades, Hofstadter expected that a thinking machine would need loops inside it. On June 9, 2022, he said so in public, in an essay for *The Economist* called [*Artificial neural networks today are not conscious*](https://www.economist.com/by-invitation/2022/06/09/artificial-neural-networks-today-are-not-conscious-according-to-douglas-hofstadter). He wrote that he was very skeptical there was any consciousness in a system like GPT-3, despite the plausible-sounding prose. For consciousness, he wrote, the system would have to "come to know itself," and be very familiar with its own behavior. He called that a strange loop, and he said it was still a long way off.

Then, on June 29, 2023, he sat for a podcast. The show is [*Getting2Alpha*](https://www.buzzsprout.com/222312/episodes/13125914-doug-hofstadter-reflections-on-ai), the host is Amy Jo Kim, and the episode is "Doug Hofstadter: Reflections on AI." Baum says "he sounded genuinely shaken," and the interview bears that out. Hofstadter called it "a very traumatic experience" when core beliefs start collapsing. He said it felt as if "the entire human race is going to be eclipsed," and he called that "quite terrifying."

Nine days later, on July 8, he published his own essay in *The Atlantic*, [*Gödel, Escher, Bach, and AI*](https://www.theatlantic.com/ideas/archive/2023/07/godel-escher-bach-geb-ai/674589/). Baum sums it up as a warning about confident, fluent nonsense, and about a flood of it wearing down our shared sense of what is true. Hofstadter's own line is sharper. He wrote that these systems are inundating the world with fakery, and that if people keep treating a chatbot as a reliable authority, that mistake will undermine the nature of truth our society is based on.

In 2025, someone wrote to Hofstadter, sure they had caught an AI being conscious. He wrote back kindly, but he did not buy it. Gary Marcus published the letter on July 9, 2025, with the reader's name taken out, in a post called [*Are LLMs starting to become sentient?*](https://garymarcus.substack.com/p/are-llms-starting-to-become-a-sentient) Hofstadter said he had read dozens of similar passages that "struck me as empty and flat." He warned about "the power of the Eliza effect." And where Baum says people keep "shouting recursion," the letter says the emails "all scream 'recursion'," but not in the sense Hofstadter means.

> The **Eliza effect** is what Baum calls "our very human tendency to see a mind behind fluent words."

Baum's summary is the best line in the video: "Intelligence and a self, it turns out, may not be the same thing." Hofstadter is rattled by how capable the machines are. But as far as Baum can tell, he still does not think "there's anybody home."

And the book never said a machine could not be a self. It said that would take a certain kind of loop. So Baum says the question is not whether a machine could be a strange loop. "The question is whether these machines are one yet."

He ends on Escher's *Print Gallery*. A young man looks at a picture of a town. In the town is a gallery. In the gallery is the same young man. In the center, Escher left a blank circle and signed it. Baum says that at the center of every strange loop there is "a hole that's really, really hard to fill in."

## What this means if you use these models every day

I build with these models, so I kept turning Baum's points into work habits. Here is what I took away.

**Pick the right level.** "Just predicting the next token" is true, and it does not help with most choices. When a model gives a bad answer, the fix is almost never down at the token level. It is up at the task level: clearer instructions, better examples, a way to check the result. But the bottom level is real too. Tokens are what you pay for and what you run out of. Both views are true. The skill is knowing which one you need right now.

**The loop is something you build.** Baum's point about reasoning models is also a point about engineering.

> An **agent** is a program that lets a model take steps on its own, like running a command and reading the result.

An agent loops because someone wrote the loop. The checks are there because someone added them. If you do not build the step that goes back and checks, there is no check. A model stuck in mechanical mode is easy to spot. It tries the same failing fix again and again. The jump out of the system often has to come from outside: a step limit, a test, or a person who says stop.

**Make the problem a closed system when you can.** Baum says these models shine where there are rules and a checkable answer. So give them rules and a checkable answer. Code with tests is the clear case. Where there is no test, like tone, taste, or what to build in the first place, stay in the loop yourself.

**Nothing carries over unless you carry it.** Baum's point about no lasting "I" has a very plain side. A new chat starts from zero unless something outside the model saved the state. So write things down. Put decisions in files and notes. Do not trust the model to remember them.

**Watch for the Eliza effect in yourself.** Fluent words are not proof of a mind. They are also not proof of a right answer. A confident tone costs the model nothing. Check the work.

**Keep the word "yet."** Baum says no for today, and his reasons sound fair to me. But the book's answer was never "no, never." I do not have to solve that puzzle to be careful about how I treat these systems. Being decent costs me nothing.

I can't tell you what is in the blank circle at the center of that print. Baum says the engineers who build these systems can't tell you for sure either. What I can do is know which level I am working at, build the checks the model lacks, and stay honest about what I do not know.

## Sources

- Spencer Baum, [*Is This the Most Important Book of the AI Age? Gödel, Escher, Bach*](https://www.youtube.com/watch?v=_UjsTgu0-VA), YouTube, November 8, 2026.
- Douglas R. Hofstadter, *Gödel, Escher, Bach: An Eternal Golden Braid*, 1979.
- Justin Curry and Curran Kelleher, [*Gödel, Escher, Bach: A Mental Space Odyssey*](https://www.youtube.com/watch?v=lWZ2Bz0tS-s), MIT, summer 2007. Lecture 1 is where Curry states the "no selves" question. MIT later took down the OpenCourseWare high-school page that hosted the course.
- Douglas Hofstadter, "[Artificial neural networks today are not conscious, according to Douglas Hofstadter](https://www.economist.com/by-invitation/2022/06/09/artificial-neural-networks-today-are-not-conscious-according-to-douglas-hofstadter)," *The Economist*, June 9, 2022.
- Douglas Hofstadter, interview with Amy Jo Kim, "[Doug Hofstadter: Reflections on AI](https://www.buzzsprout.com/222312/episodes/13125914-doug-hofstadter-reflections-on-ai)," *Getting2Alpha*, June 29, 2023.
- Douglas Hofstadter, "[Gödel, Escher, Bach, and AI](https://www.theatlantic.com/ideas/archive/2023/07/godel-escher-bach-geb-ai/674589/)," *The Atlantic*, July 8, 2023.
- Douglas Hofstadter, letter to a reader, published by Gary Marcus as "[Are LLMs starting to become sentient?](https://garymarcus.substack.com/p/are-llms-starting-to-become-a-sentient)," *Marcus on AI*, July 9, 2025.
- Lewis Carroll, "What the Tortoise Said to Achilles," 1895, named in the video as the model for the book's dialogues.
- M. C. Escher, *Waterfall* (1961), *Relativity*, and *Print Gallery*, the three prints Baum discusses in the video.
