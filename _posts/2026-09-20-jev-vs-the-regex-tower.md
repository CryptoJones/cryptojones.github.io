---
layout: post
title: "Jev vs. the Regex Tower"
audio: /audio/posts/jev-vs-the-regex-tower.mp3
description: "I swapped the fuzzy part of a book-matching script for two yes or no questions to an AI model. Then I tested both on 500 real searches."
keywords: "Jev, TypeSafe, System One, regex, heuristics, fuzzy matching, book search, Open Library, LLM as a judge"
---

I have a tool that searches a book catalog. It types in a title and an author,
gets back a list of hits, and has to decide which hit is the book I asked for.

For a long time a script made that choice. The script lowercases the titles. It
splits them into words. It counts how many words overlap. It checks that the
author's last name shows up somewhere. It runs a regex to throw out solutions
manuals. Then it blends all of that into one score.

> **Regex**: short for regular expression. It is a pattern for matching text,
> like "the word solutions followed by the word manual."

It works. Mostly. And every time it does not work, the fix is one more regex.
After a while you are not fixing a script. You are stacking a tower.

All of the code for this post is at
[github.com/CryptoJones/jev-testbed](https://github.com/CryptoJones/jev-testbed).

## The problem with the script

The script is not wrong so much as stiff. It is trying to answer a question
about meaning: is this the same book? But all it can look at is letters.

So a title that ends in "Solutions" slips past a pattern that only knows
"Solutions Manual." A correct book with a blank author field gets thrown away,
because the last name check fails. I could patch both. I have patched things
like them before. Each patch is a new special case, and it will misfire on some
other book next month.

## What I did instead

I put **Jev** in the loop. Jev is a model from TypeSafe. You hand it some data
and a list of typed questions. For a yes or no question, it does not write you
a paragraph. It hands back one number between 0 and 1. That number is how sure
it is that the answer is yes.

> **Noul**: TypeSafe's name for a yes or no question that comes back as a
> probability. A 0.98 means "almost surely yes." A 0.03 means "almost surely no."

For each search hit, I ask Jev two questions in a single request:

```js
questions[`match_${i}`] = noul(
  `Is candidates[${i}] the same work as the wanted book? ` +
  `A different edition, year, or format is STILL the same work.`,
  { true: 'The same work', false: 'A different book' }
);
questions[`companion_${i}`] = noul(
  `Is candidates[${i}] a companion volume, like a study guide ` +
  `or a solutions manual, rather than the book itself?`,
  { true: 'A companion volume', false: 'The book itself' }
);
```

Here is the part I care about most. Everything that was already an exact rule
**stays in code**. The language filter stays in code. The file size cap stays in
code. So do the cutoffs: a hit needs a match score of at least 0.6 and a
companion score under 0.5. The model does not get a vote on policy. It only
makes the one judgment call the regexes were faking.

## The test: 500 real searches

I started with seven test cases I wrote by hand. The script got 5 of 7. Jev got
7 of 7. That proves nothing except that I can write test cases. So I built a
real test.

**The list.** 500 famous young adult novels, from *Harry Potter* to *Iron
Widow*. Young adult books are a good stress test. The shelf is full of series,
box sets, movie tie-ins, graphic novel versions, study guides, and books that
have one title in the US and another in the UK.

**The hits.** For each book I pulled the top 10 results from
[Open Library's](https://openlibrary.org/developers/api) public search. I used
the exact search text my real tool builds. This is catalog data only. Nothing
gets downloaded. The question is "which hit would you pick," and you do not
need the file to answer that.

**The pairing.** I saved every result list, so both methods judged the exact
same hits. Then every case where they disagreed was checked by hand.

## Results

| | Script | Jev |
|---|---|---|
| Right answer | 480 of 500 | 497 of 500 |
| Percent | 96.0% | 99.4% |
| Mistakes | 20 | 3 |

On 433 books both methods picked the very same record. On 34 more they picked
two different catalog records for the same book, so both were right. That
leaves 23 books where exactly one of them was right. Jev won 20 of those. The
script won 3.

Is that luck? I ran the usual test for paired results like these. The odds of
a 20 to 3 split by pure chance are about 1 in 2,000.

The 20 script misses sort into three neat piles.

**The script loves a box set (7 books).** Ask for *The Last Olympian* and it
picks a record titled *The Lightning Thief / The Sea of Monsters / The Titan's
Curse / The Battle of the Labyrinth / The Last Olympian*. The title I wanted is
right there in the text, after all. It did the same for *The Hammer of Thor*
and *The Summer I Turned Pretty*. For *The Golden Compass* it chose *The Golden
Compass Graphic Novel, Volume 2*. Jev picked the real novel every time. In that
last case it picked a record called *Northern Lights*. That title shares zero
words with what I asked for, and it is exactly the right book. It is the UK
name.

**The script cannot see through a title change (8 books).** *Harry Potter and
the Sorcerer's Stone* is filed as *Philosopher's Stone*. *Point Blank* is
*Point Blanc*. *Days of Blood & Starlight* is spelled out with the word "and."
Someone typed *Blue Lily, Lily Blue* as "Blue Lilly, Lilly Blue." Cornelia
Funke's *Inkheart* is filed under its German name, *Tintenherz*. The script
found nothing for all eight. Jev matched every one.

**The script does not know when to walk away (5 books).** I did not expect this
pile. Sometimes the book is simply not in the results. The script picks
*something* anyway.

| I wanted | The script picked | Jev's score for that pick |
|---|---|---|
| The 5th Wave | A three book "Collection #1-3" | 0.26 |
| A Wind in the Door | *The Time Trilogy* omnibus | 0.37 |
| Octavian Nothing, volume one | Volume two | 0.24 |
| The Absolutely True Diary of a Part-Time Indian | A college thesis *about* the novel | 0.04 |

Jev picked nothing for all of them. That is the right answer. A calm "no" turns
out to be worth as much as a sure "yes."

This pile matters more than the numbers show. When the script misses a book, I
see "not found" and I go look. When the script grabs a thesis and saves it
under the novel's name, I do not find out until I open the file.

## Where Jev lost

It was not a clean sweep, and the three losses taught me things.

***Four* by Veronica Roth.** The right record was *Four: A Divergent
Collection*. Jev scored it 0.38, under my 0.6 cutoff. A one word title plus the
word "Collection" made it hedge. The script matched it fine.

***A Monster Calls* and *The Knife of Never Letting Go*.** Jev scored the
English records around 0.93. It scored a Spanish edition around 0.96. My code
took the top score. That is not Jev being wrong. The Spanish edition *is* the
same work, and that is the question I asked. It is a hole in **my** tie-break
rule, which only knew how to prefer file types. I wanted the English one.

The fix was a few lines of code, not a new prompt. When scores are that close,
an English record now beats a record that looks foreign. Since I had saved every
score, I could replay all 500 choices without calling the model again. Exactly
those two picks changed. That would put Jev at 499 of 500. But I wrote that
rule after I saw the misses, so it is not a fair score. The honest number stays
at 497.

One more bug showed up that belongs to neither method. Six searches came back
empty because my search text builder turns `Tyrant's` into `Tyrant s`. Running
500 real searches finds things seven test cases never will.

## What it cost

The whole run used 1.18 million tokens. That is about 2,400 per book, for up to
ten hits with two questions each.

> **Token**: the unit a model reads and bills by. It is roughly three quarters
> of a word.

So here is the honest trade. The script is free and it is 96% right. Jev costs
a little and it is 99.4% right. The smart build is a mix. Let the script handle
the easy exact matches. Call Jev only when the script is unsure, or when it is
about to grab something with "Collection" in the title.

## The takeaway

I did not replace the script with a model. I replaced the one part of the
script that was *pretending to understand language*, and I kept the rest. On
500 real searches that took the mistakes from 20 down to 3. And each of those
three points at a real thing I can fix.

Some cautions, because there are always cautions. This is one kind of book, and
famous novels have very clean catalog data. Open Library records carry no file
types, so my "prefer EPUB over PDF" rule never got used. And the hand check was
a single pass that nobody has double-checked. Every hit and every score is in
the [repo](https://github.com/CryptoJones/jev-testbed), in
`results/ya-500.jsonl`, if you want to check my work.

## Thanks

A big thank you to the team at [TypeSafe](https://typesafe.io) for giving me
early access to Jev. This experiment would not exist without it.
