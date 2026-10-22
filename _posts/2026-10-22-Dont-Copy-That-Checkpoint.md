---
layout: post
title: "Don't Copy That F̶l̶o̶p̶p̶y̶!̶ Checkpoint!"
description: "Big Brother China wants to dictate its Frontier Labs' Releases, and the USA is pushing DeepSeek out of federal agencies. As a 90s cynic I explain why this will go as well as putting screen doors on their submarines."
audio: /audio/posts/Dont-Copy-That-Checkpoint.mp3
keywords: "open weights, model weights, AI export controls, China MOFCOM, DeepSeek, warez scene, Business Software Alliance, Don't Copy That Floppy, LLaMA leak, DeCSS, PGP, data hoarding"
---

In 1992, the software industry made a rap video. It was called "Don't Copy That Floppy." It was mailed to schools to warn kids that copying a game disk for a friend was stealing. Plenty of us laughed at it while simultaneously smoking weed and downloading pirated video games broken up into 1.44 MB .arj or .rar files.

I thought about that dumass video this week when Devsplainers posted a video called [*Open Source AI Is Quietly Closing*](https://www.youtube.com/watch?v=gD40lPTj1SQ). It walks through a new draft rule from China, new license terms from the big AI labs, and a US order pushing the Chinese AI company DeepSeek out of federal agencies. Its advice is simple: decide what to save, and save it tonight.

From the #NoShit Department: The video is careful to say that nobody can take back the model files, called weights, that you already have. It worries about the next Chinese release, and about new licenses that already squeeze the companies that host models cheaply. I lived through the 90s, so let me back that up with some history. Governments and companies spent decades trying to put software back in the box. They never got the copies back. They only slowed down what came next.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gD40lPTj1SQ" title="Open Source AI Is Quietly Closing" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

> **Model weights** are the learned numbers inside an AI model, saved in one or more files. If you have the weights and a program to run them, you have the model. An **open-weight model** is one whose weights are published so anyone can download them and run them on their own computer. A **checkpoint** is a saved copy of the weights. The file you download is a checkpoint.

## What the video says

On October 16, China's Ministry of Commerce and Ministry of Science and Technology put out a draft rule for public comment. It adds top AI models to China's list of technology that needs a license to leave the country. A model gets caught if it hits any one of three lines:

- It was trained with at least 10^26 math operations. That is a 1 followed by 26 zeros.
- It has at least 2 trillion parameters.
- It ranks in the world's top 10 on a public ranking when it is exported. That can be overall skill, one narrow skill like coding, safety, how efficiently it was trained, or just how many people use it.

> A **parameter** is one of the learned numbers inside a model. A model with 2 trillion parameters has 2 trillion of them, and the weights file holds every one.

That third line has no size floor. The video's biggest worry is that it could reach models far smaller than 2 trillion parameters.

The video says the rule covers the core technology of a large model, including the weights. According to ChinaTalk, the draft itself also covers source code, model design, and the methods used to train and run the model. Using a model through an app or an API is outside the rule. Shipping the weights out of China is the part that would need a license.

> An **API** is a way for one program to send requests to a model running on someone else's computer. You get answers back, but you never get the weights.

There are two escape hatches. Models that are already public are left out. And new open-source releases get what the draft calls automatic licensing. A ministry spokesperson called it basically "file and ship." A Chinese lab files a report and, on paper, may ship.

One part is not just on paper. Since October 16, Chinese companies already have to register with the ministry before they export anything on the list. Comments on the rest close on November 15.

The video then covers the labs. It says most of this year's big open models now ship with custom licenses that put limits on hosting companies, the businesses that run open models and sell access cheaply. Kimi K3 and Meta's Muse Spark Open, for example, need a separate deal for a hosting business with more than $20 million a year in revenue. DeepSeek is the exception. At home, the video says, none of these licenses block personal use.

And it covers the US side. The Department of Homeland Security barred federal civilian agencies from buying DeepSeek products and ordered them removed from agency systems. That includes outside products built using DeepSeek. The order was issued July 24 and published in the Federal Register on October 20. As the video points out, it only covers those agencies. It says nothing about running open weights yourself.

The video's last chapter is called "Verdict: what to save tonight." That is where the video and I land in the same place.

## I have seen this fucking movie

If you were online in the 90s, you know the warez scene.

> **Warez** (say "wares") was the old name for pirated software. The **scene** was the organized underground that cracked it and passed it around.

It was not a few kids on a modem. It was a full blown supply chain. **Release groups** got new software, cracked the copy protection, and packaged it. Each release came with an **NFO file**, a text file with the group's name, install notes, and a lot of pictures drawn with keyboard characters. (God I miss ascii-art!) **Couriers** raced to move each release from one server to the next. The fastest servers were called **topsites**. They were private, high-speed FTP servers that only members (usually paid) could reach. IRC bots announced each new release the moment it landed. Before the internet took over, the same thing ran on dial-up bulletin boards.

> **FTP** is an old way to move files between computers. **IRC** is an old chat system. A **BBS** was a computer you dialed into with a modem to swap files and messages.

The software companies fought back hard. Microsoft and other publishers formed the Business Software Alliance (BSA) in 1988. The BSA went after businesses using unlicensed software. It would get a tip, look into the company, and make it pay a settlement and buy real licenses. In 1994 it set up a phone line in Britain and offered informants up to 2,500 pounds to report their own employers. By 1998 it was running ads in airports and ballparks telling workers to "nail your boss." In 2007 it briefly raised its top US reward to a million dollars.

The Software Publishers Association, a separate trade group, took the other side of the street. That is where "Don't Copy That Floppy" came from.

Then the government stepped in. On December 11, 2001, US Customs and the Justice Department ran Operation Buccaneer. Agents carried out more than 65 searches in the US and five other countries. The best-known target was a group called DrinkOrDie, founded in Moscow in 1993. DrinkOrDie fell apart. People went to prison. By October 2002, thirteen people had federal prison sentences, some close to four years.

And despite those fuckers best efforts, warez didn't go away. The groups changed names. The servers moved. New releases kept coming. The raids took out people. They could not take back files.

## Files want out

That pattern shows up again and again when someone tries to fence in bits.

> **Encryption** means scrambling a message so only the right person can read it.

**The crypto wars.** In 1993, US Customs opened a criminal investigation into Phil Zimmermann because his encryption program, PGP, had spread overseas. US export rules treated strong encryption like a weapon. In 1995, MIT Press printed the PGP source code as a book. A book could leave the country legally. The investigation was dropped in 1996 with no charges. Around the same time, a federal judge ruled in *Bernstein v. Department of Justice* that source code is protected speech. An appeals panel agreed in 1999, then pulled its own ruling so the full court could hear the case again. Before that happened, the government loosened its export rules, and the case was dismissed in 2003.

**DeCSS.** In 1999, a program called DeCSS broke the copy protection on DVDs. The movie studios sued. In 2001, a federal appeals court upheld an order that stopped the hacker magazine *2600* from posting the code or knowingly linking to it. It did not matter. People printed the code on T-shirts. A math fan turned it into a prime number. The Norwegian teen who helped write it, "DVD Jon," was found not guilty in January 2003, and again on appeal that December.

**09 F9.** In May 2007, a leaked key used to unlock HD DVD and Blu-ray discs was spreading online. It starts with the digits 09 F9. Digg, a popular news-voting site, started deleting posts that had the key. Users posted it in hundreds of stories and thousands of comments. The same day, Digg co-founder Kevin Rose gave up and posted the key himself, right in the title of his blog post.

> A **torrent** is a way to share a big file where the people downloading it also upload pieces to each other. There is no single server to shut down.

**LLaMA.** On February 24, 2023, Meta announced its LLaMA model and gave the weights to approved researchers, case by case. On March 3, someone shared a link to a torrent of the weights on 4chan, an anonymous message board. Meta sent takedown notices, which are legal demands to remove a file. The copies kept spreading. To be clear, that was a leak that broke Meta's terms. It is history, not a how-to. Meta later released its Llama models openly, and that is how most people got them.

And proving that the universe is an asshole, that September, the French lab Mistral released its first model by posting a torrent link. The labs now ship models over the same kind of pipes the file-sharers built, with a license attached.

## These people are still smoking crack thirty years later

A model is a file. A big file, but a file. Once it is out, it is out. You cannot recall a file the way you recall a car.

China's draft leaves technology that is already public out of its rules. To me, that fits the lesson every BSA lawyer learned the hard way. Stopping a release is easier than erasing its copies.

So what can a government actually control? It can slow down the next release from the big labs. It can make a lab file paperwork, wait, and maybe hold back its best model. It can tell its own agencies what they may run, and it can go after people who share files it has banned. That is real power, and it matters. It still does not erase every copy.

The labs work the same way. A new license can tell a big cloud company it needs a separate deal. It can limit what I may do with a file. It cannot reach into the hard drive in my closet and delete it.

The cynic in me says the rules will get tighter. Encryption export rules lasted most of the 90s. The BSA is still around. Nobody shut down warez by passing a law. They made it more expensive and pushed it out of sight.

## Why I'm saving weights anyway

Here is why I sound like a hypocrite-- If the copies can't be controlled, why am I hoarding them?

Because control is not the same as access. The 90s proved that copies survive. They did not prove that copies stay easy to find. A file that is one click away on a big website today might be hard to find next year. That could happen because of a new law, a new license, a take-down, or a company that just decides to pull it. Hugging Face, the main site where labs post their weights, is a company. It follows the law where it operates. If that law changes, the download button changes with it.

The models on official pages today are legal to download, under their licenses. Save them now, while that is simple and lawful.

So here is my advice.

1. **Grab what you would actually run.** The models people run at home are far below China's 2-trillion-parameter line. The video warns that the top-10 line could still catch smaller models, so size alone does not make a model safe from the rule. But that rule is about what leaves China next, not what is already on your drive. Pick a few good models in sizes your hardware can handle. A big flagship you can never load is a souvenir, not a tool.
2. **Get them from the official source.** Download from the lab's own download page. If the lab makes you accept a license before the download, do it there. Don't use a mirror to skip that step, and don't trust a random re-upload.
3. **Save the license with the weights.** Put the license file, the model card (the lab's write-up of what the model is), and the date you downloaded it in the same folder. That file is the deal you got. Read it, too. Personal use is usually fine. If you plan to host a model for other people or build a product on it, check the terms first. Some now need a separate deal above a revenue limit.
4. **Checksum everything.** Record the SHA-256 checksum (a short fingerprint of the file) of each file when you download it. Check it again later. A copy you can't trust is worth nothing.
5. **Keep more than one copy.** The old rule is 3-2-1: three copies, on two kinds of storage, with one private copy somewhere else that you still control, like a drive you store at a relative's house. Hard drives fail. I have lost more data to dead drives than to any government.
6. **Keep one copy offline.** A disconnected drive in a drawer can't be wiped by a bad update, ransomware (a program that locks your files until you pay), or a cloud account that got shut off.
7. **Save the tools, too.** A weights file is useless without the program that runs it. Keep a copy of the version of the software that works with your models today.

> A **checksum** is a short code made from a file's contents. If even one bit of the file changes, the code changes. **SHA-256** is a common way to make one.

Build that library with files you got legally, and follow the license when you store, run, or share them. That is not piracy. That is a library.

## The lesson from the floppy era

The kids who laughed at "Don't Copy That Floppy" were not wrong about the tech. You really could copy that floppy. But a lot of the software from that era is hard to find now. Copying a disk was easy. Keeping a working copy for thirty years took effort, and most people didn't bother.

That is my real fear with open models. Not that some government will ban them and win. It is that we will assume they will always be one click away, and then one day they won't be. The copies that survive will be the ones somebody bothered to save.

Be somebody.

## Sources

- Devsplainers, [*Open Source AI Is Quietly Closing*](https://www.youtube.com/watch?v=gD40lPTj1SQ), October 21, 2026
- China Ministry of Commerce, [spokesperson Q&A on the draft revision of the export technology catalogue](https://www.mofcom.gov.cn/syxwfb/art/2026/art_a4acff07e134447fbe7bbeb486df3ea6.html), October 16, 2026
- ChinaTalk, [MOFCOM's New Rules and the Future of Chinese AI](https://www.chinatalk.media/p/mofcoms-new-ai-rules), October 21, 2026
- Federal Register, [DHS notice of exclusion and removal order for DeepSeek products](https://www.federalregister.gov/documents/full_text/html/2026/10/20/2026-21447.html), October 20, 2026
- CNBC, [U.S. bans DeepSeek from government agency systems](https://www.cnbc.com/2026/10/20/us-deepseek-federal-agency-ban.html), October 20, 2026
- Wikipedia, [Warez scene](https://en.wikipedia.org/wiki/Warez_scene) and [Topsite (warez)](https://en.wikipedia.org/wiki/Topsite_(warez))
- US Department of Justice (archived), [Operation Buccaneer](https://ipmall.law.unh.edu/content/us-department-justice-cybercrimegov-archived-major-criminal-ip-operations-operation)
- Wikipedia, [DrinkOrDie](https://en.wikipedia.org/wiki/DrinkOrDie)
- The Independent, [Copy that floppy at your peril](https://www.the-independent.com/life-style/network-copy-that-floppy-at-your-peril-from-november-employers-whose-staff-engage-in-software-piracy-could-find-themselves-having-to-pay-up-or-face-legal-action-says-tim-jackson-1443471.html), October 1994
- Los Angeles Times, [A Pitch to Snitch](https://www.latimes.com/archives/la-xpm-1998-aug-14-fi-12979-story.html), August 14, 1998
- Computerworld, [BSA raises reward to $1 million for reports of piracy](https://www.computerworld.com/article/1609486/bsa-raises-reward-to-1-million-for-reports-of-piracy.html), July 3, 2007
- Wikipedia, [Software and Information Industry Association](https://en.wikipedia.org/wiki/Software_Publishers_Association) ("Don't Copy That Floppy," 1992)
- Hacker Culture, [PGP](https://www.hackerculture.org/en/artifact/pgp)
- Wikipedia, [Bernstein v. United States](https://en.wikipedia.org/wiki/Bernstein_v._United_States)
- Digital Media Law Project, [Universal v. Reimerdes](https://www.dmlp.org/threats/universal-v-reimerdes)
- Carnegie Mellon, [Gallery of CSS Descramblers](https://www.cs.cmu.edu/~dst/DeCSS/Gallery/)
- Wikipedia, [Illegal number](https://en.wikipedia.org/wiki/Illegal_number)
- EFF, [Norwegian Teenager Jon Johansen Acquitted in DVD Case](https://w2.eff.org/IP/Video/Johansen_DeCSS_case/20030107_eff_pr.html), January 7, 2003
- MPR News, [Hacker hero "DVD Jon" acquitted again](https://archive.mpr.org/stories/2003/12/23/hacker-hero-dvd-jon-acquitted-again), December 23, 2003
- Wikipedia, [Digg: AACS encryption key controversy](https://en.wikipedia.org/wiki/Digg)
- Wikipedia, [Llama (language model)](https://en.wikipedia.org/wiki/Llama_(language_model))
- Simon Willison, [Many options for running Mistral models in your terminal](https://simonwillison.net/2023/Dec/18/mistral/), December 18, 2023
