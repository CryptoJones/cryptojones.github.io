---
layout: post
title: "Seven Days Until My Own App Stops Working"
description: "Apple makes you pay to keep your own app running on your own phone. Here is what broke, what it cost, and why the seven day limit is the worst part."
audio: /audio/posts/Seven-Days-Until-My-Own-App-Stops-Working.mp3
---

I wrote the app, I own the phone, and I own the computer that built it. On Sunday afternoon my phone still told me no.

The exact words were "Untrusted Developer," and below that, in smaller print, it named the developer it did not trust. The name was mine.

That is the part people outside this world have trouble believing. You can write every line of the code and hold both devices in your hands, and Apple still decides whether the app is allowed to run. Then Apple charges you for the privilege.

## First it would not sign at all

Before I ever got to the seven day nonsense, I hit a wall that took a couple of hours to understand.

> **Signing** is the step where your computer stamps an app with a certificate so the phone can check who made it. No stamp, no install.

I had a certificate that was created that same afternoon, so it had not expired, and the private key was sitting right there in my keychain. Despite all of that, the tool that lists usable certificates kept telling me this:

```
0 valid identities found
```

Zero, with the certificate plainly visible in the same keychain.

Here is what was actually wrong, and I am writing it down because almost nothing online says it clearly. Apple does not simply hand you a certificate and wish you luck. Your certificate is signed by one of Apple's own middle certificates, and my Mac only carried the old version of it. That older middle certificate expired on February 7, 2023, while my brand new certificate was signed by its replacement. The two were never introduced.

So my Mac held a good certificate and a good key with no way to connect either one back to Apple. Every tool in the chain reported that situation as though I had no certificate whatsoever, which is a genuinely terrible error message. The actual repair was a single download and a single import:

```
curl -fsSL -o /tmp/AppleWWDRCAG3.cer \
  https://www.apple.com/certificateauthority/AppleWWDRCAG3.cer
security import /tmp/AppleWWDRCAG3.cer -k ~/Library/Keychains/login.keychain-db
```

One valid identity, immediately. A three year old expired file had been quietly breaking everything, and nothing in the error output pointed anywhere near it.

## Then it built, and that felt great for about a minute

The build ran for 498 seconds, which is a hair over eight minutes for a debug build of a Flutter app heading to a physical phone. It compiled, it signed itself, it copied across the cable, and the icon appeared on my home screen exactly where it should have.

I tapped it, and that is when I got the Untrusted Developer box.

The fix for that one is not difficult, but you would never guess it on your own. You open Settings, then General, then a menu buried down the list called VPN and Device Management. Your own name is waiting in there like a stranger who needs to be let inside. You tap your name, tap Trust, and confirm.

The app opens after that. A timer also starts that nobody bothers to mention.

## Seven days

This is the part that genuinely made me angry.

A free Apple developer account will let you put your own app on your own phone, and it works exactly as advertised. It also stops working after seven days.

The certificate is not what expires. The certificate Apple issued me is valid until August 2027. The **app** is what stops launching. Same phone, same code, same certificate, and on the eighth day it simply refuses to open. You plug the phone back into the Mac and run the entire build again.

You are also limited to three of these at a time, so if you want a fourth thing you made, something else has to be sacrificed.

I understand the security reasoning behind it. Apple does not want a free tier that quietly becomes a permanent channel for handing out apps outside the App Store, and I agree that a limit belongs somewhere in that system.

Seven days is not that limit. Seven days is short enough that it stops functioning as a safety rail and starts functioning as an advertisement. It is calibrated to be exactly miserable enough, and the misery has a price tag attached to it, which is rather the point.

Thirty days would be a security limit. Ninety days would be a security limit. Seven days is a sales pitch.

## So I paid

Ninety nine dollars a year, which is what the Apple Developer Program costs.

> The **Apple Developer Program** is Apple's paid membership. It runs $99 a year, and it turns a hobby build into something that can live on a phone for a year, go out through TestFlight, or reach the App Store.

For that money the seven days becomes a full year and the three app cap disappears entirely. I can register a hundred devices instead of negotiating with one stubborn phone. Push notifications begin working, which for a chat client is not a pleasant bonus so much as the entire point.

I want to be honest about the value here. For anybody shipping real software, ninety nine dollars is nothing at all, and it is a rounding error measured against a single afternoon of my time. I am not writing this because the price is outrageous.

I am writing it because of what the free tier quietly teaches you. It teaches you that the phone in your pocket is not truly yours. You are renting the right to run your own work on your own hardware, and that rent comes due every seven days until you pay the yearly fee.

## The last annoyance

I paid on Sunday, and the account was not approved on Sunday.

So at the moment I am sitting on a working build, signed by a free account, with a countdown attached to it. Apple has my money and my app still expires on Saturday. Approval takes anywhere from a few minutes to two full days, and there is no way to check the status from the command line unless you have already configured API keys that you cannot configure yet, because you have not been approved yet.

If you are about to do this for the first time, do it in this order. Pay first, wait for the approval email, and then build. I did it backwards, so I get to build the same app twice.

There is a Raspberry Pi on my desk that will run anything I compile for it, forever, at no charge. Same code, same person writing it. The only real difference is who owns the lock.
