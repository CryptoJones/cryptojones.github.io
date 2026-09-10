---
layout: post
title: "The One Bit That Knew My Laptop Was Dying"
audio: /audio/posts/the-one-bit-that-knew-my-laptop-was-dying.mp3
description: "My gaming laptop shut itself off at 1 AM with two chargers plugged in. Finding out why meant reading the firmware's own code, one bit at a time."
---

At 1:03 in the morning my laptop turned itself off. I was upstairs in bed. The
machine had two power cables attached, a big barrel charger and a USB-C cable,
and it still ran its battery down to two percent and shut down.

The next morning it would not boot at all. That turned out to be a separate
problem, which is a story for another day. This post is about the first
question: how does a laptop know it has power, and why did mine get it so
wrong?

The answer took me from a file you can read with `cat` all the way down to the
laptop's own firmware code. Along the way I found out that the operating system
was never told the thing I most needed to know.

## Layer one: the file that tells you almost nothing

Linux keeps hardware information in a fake filesystem called sysfs. It looks
like ordinary files and folders, but nothing is really on disk. Reading a file
runs a bit of kernel code that goes and asks the hardware.

> **sysfs**: a folder tree, usually at `/sys`, that lets you read hardware
> state by reading files. The files are made up on the spot by the kernel.

Power lives under `/sys/class/power_supply/`. My laptop has two entries there.
One is the battery. The other is the charger.

The important file is `online`. It holds `1` when the laptop has outside power
and `0` when it does not.

That sounds like exactly what I needed. It is not, and here is why.

**My laptop has two ways to take in power.** There is the barrel plug, the fat
round one that carries 330 watts. There is also USB-C, which on this model tops
out at 65 watts. Both of them feed the same charging chip inside.

The `online` file reads `1` if **either** one is working. It cannot tell them
apart. So on the night everything went wrong, that file could not have told me
whether the barrel plug had quit, because USB-C was still there to hold the
value at `1`.

There is a second trap. The battery reports how much current is flowing in a
file called `current_now`. When the battery is full, charging stops, and that
file reads zero. So the number goes silent at exactly the moment you want to
check on things.

Two files, and both of them are useless for the question I had.

## Layer two: ACPI, where firmware ships you code

Under sysfs sits ACPI. That is the standard that lets firmware describe
hardware to any operating system.

> **ACPI**: a set of tables the manufacturer builds into the machine. They tell
> the OS what devices exist, and they include small programs the OS can run to
> ask about them.

Those small programs are the interesting part. Firmware ships actual code, in a
language called AML, and Linux runs it.

My laptop declares two power devices this way. The charger is device type
`ACPI0003`, and the battery is `PNP0C0A`. The charger has a method named
`_PSR`, which stands for Power Source. The battery has `_BST` for its current
state. When you read that `online` file, Linux runs `_PSR` and hands you
whatever it returns.

So `_PSR` decides what the file says. What does `_PSR` look at?

You can find out, because the tables are readable. Three tools that ship with
Ubuntu will pull the firmware out of your own running machine and turn it back
into something close to source code:

```bash
sudo acpidump > acpi.dat
acpixtract -a acpi.dat
iasl -d dsdt.dat
```

That gave me a 57,000 line file. Somewhere in there is the code that decides
whether my laptop thinks it is plugged in.

## Layer three: the embedded controller

Before the code makes sense, one more piece.

Every laptop has a small chip called the embedded controller, or EC. It is a
tiny computer that runs whenever the machine has any power at all, even when
the lid is shut and the system is off. It watches the charger, runs the fans,
handles the keyboard backlight, and talks to the battery.

> **Embedded controller**: a small always-on chip that manages power, fans, and
> keys. The main processor asks it questions. It is the part that actually
> knows.

The EC keeps its state in 256 bytes of memory. Not files, not a protocol, just
256 bytes. Every fact about power on my laptop lives somewhere in there.

Linux can show them to you through a debug interface:

```bash
sudo modprobe ec_sys
sudo xxd /sys/kernel/debug/ec/ec0/io
```

Two notes. That module loads read only by default, and you should keep it that
way, because writing random bytes to the chip that controls your battery is a
bad idea. And this only works because someone decided to expose it. Nothing
here is a documented, promised interface.

## Reading the firmware's own map

The decompiled firmware includes a map of those 256 bytes. Field names, in
order, with their sizes in bits. Here is the piece that mattered, at byte 0x48:

```
Offset (0x48),
    KBBL,   1,
        ,   1,
        ,   1,
        ,   2,
    BTST,   1,
```

`KBBL` is bit 0, and it is the keyboard backlight. Then three unnamed bits.
Then `BTST` at bit 5.

`BTST` is the one. It is `1` only when the barrel plug is delivering power.
USB-C never sets it. That is the single bit that could have answered my
question, and it was sitting there the whole time.

Notice what shares that byte. The keyboard backlight and the power source are
neighbors, one bit apart, in the same eight bits of memory. There is no reason
for that beyond whoever laid out the firmware needing somewhere to put them.

There is a second useful bit in the same byte, at position 6. It reads `1`
whenever **any** source is feeding the laptop, barrel or USB-C. That one is not
in the firmware map at all. The map stops naming fields after bit 5. I found it
the same way I found the first one, by dumping the 256 bytes with the charger
in, dumping them again with it out, and comparing.

Put the two bits together and the byte answers the whole question:

| Byte 0x48 | bit 6 | bit 5 | What it means |
|---|---|---|---|
| `0x01` | 0 | 0 | Nothing is feeding it. Running on battery. |
| `0x41` | 1 | 0 | Powered, but not by the barrel. So it is on USB-C. |
| `0x71` | 1 | 1 | The barrel plug is delivering. |

I also found what `_PSR` really reads. It is a different field, called `ACDF`,
at byte 0x40, bit 0. That is the ambiguous one. It goes to `1` for the barrel
plug or for USB-C, without distinction, and that is the value that becomes the
`online` file.

So the chain looks like this:

```
charger  ->  EC  ->  EC memory
                       |
                       +-- 0x40 bit 0 (ACDF) -> _PSR -> online -> the OS
                       |
                       +-- 0x48 bit 5 (BTST) -> nothing reads it
                       +-- 0x48 bit 6        -> not even named
```

**The firmware knows which cable is feeding the laptop. It just never tells the
operating system.** No ACPI method reads `BTST`. The only way to see it is to
go around ACPI entirely and read the chip.

## A blind spot I did not expect

Modern USB-C charging has its own kernel subsystem. It is supposed to expose
the power deal that got negotiated: how many volts, how many amps, what the
charger offered.

On my laptop three of those drivers are loaded, and the folder they publish to
is **empty**. Zero ports registered. So Linux can tell me nothing at all about
the USB-C side. Not the voltage, not the current, not whether a deal was ever
struck.

That is why bit 6 matters so much. It is a yes or no, and a yes or no is
everything I have. If you want real numbers for USB-C on a machine like this,
sysfs will not give them to you and you need a meter that sits in the cable.

## The driver, and a message that looks like an error

Acer laptops load a driver called `acer_wmi`. It handles hotkeys and a few
vendor extras. It also prints this, and it shows up in the system log every
time you plug or unplug a charger:

```
acer_wmi: Unknown function number - 9 - 1
```

That looks like something broke. It did not. Firmware can send the OS a
notification when hardware changes, and this firmware sends event number 9
whenever the power source changes. The driver simply has no case written for
number 9, so it logs the number it does not recognize and moves on.

Which means it is a free, timestamped log of every power change, sitting in
your system log, disguised as an error. On my machine it matched the exact
second the power switched over.

## The cable cannot introduce itself

Here is the part I did not expect at all.

Some laptops can identify their charger. Dell put an extra pin in the middle of
their connector, and a small chip inside the charger reports its wattage over
that pin. Plug in the wrong charger and the laptop tells you so.

My barrel plug is 5.5 mm across and 1.7 mm on the pin. It has two conductors.
Positive on the inside, ground on the outside. That is all.

**There is no third pin, so there is nothing to say anything with.** I searched
the whole 57,000 line firmware dump for any field holding an adapter wattage or
an adapter type. There is none. The laptop cannot tell a 330 watt charger from
a 90 watt one. It sees voltage on a pin and starts drawing current.

That is fine when everything works. It also means the machine has no way to
warn you that the power coming in is not enough for what you are asking it to
do.

And the numbers here are unkind. 330 watts at 19.5 volts is about 17 amps,
through a barrel connector smaller than a pencil eraser. Any bad contact in
that path turns into heat. Heat makes the contact worse. Worse contact makes
more heat.

## Layer four: the part that actually turned it off

One more piece sits above all of this, and it is the piece that pulled the
trigger.

A service called UPower watches the battery and acts on policy. Mine was set,
by default, to take action at two percent. Hibernating was turned off as too
risky. With hibernation ruled out, the fallback action is to power off.

So at two percent, UPower did precisely what it was configured to do. The clean
shutdown I found in the logs was not a crash and not a failure. It was the
operating system saving my filesystems on the way down, correctly, while every
layer beneath it still believed the machine was plugged in.

That is the whole shape of the problem in one sentence. The policy engine at
the top was making a good decision using a value from the bottom that could not
tell two very different situations apart.

## What I actually built

Knowing about those two bits turned an unanswerable question into a one line
answer.

A small service copies the EC bytes to a readable file once a second, so
ordinary programs can look at them without special permission. A second script
decodes bit 5 and bit 6 and writes one line to a log, but only when something
changes. A polybar module reads the same two bits and colors an icon.

That log is why I can tell you what happened at 1 AM. Not a reconstruction, not
a guess. A timestamped record showing that for the whole slide from 45 percent
down to 2 percent, the laptop had no power coming in at all, from either cable,
while both sat plugged into it.

Everything above the chip agreed the machine was fine. Only the bits nobody
reads knew otherwise.

The scripts are on GitHub, along with two diagnostic tools that helped me
separate a failing laptop jack from a failing charger:
[Polybar-PowerGuard-Acer-PH18-71](https://github.com/CryptoJones/Polybar-PowerGuard-Acer-PH18-71).

## If you want to try this

The tools are already on your machine. Nothing here needs installing.

```bash
# what the OS thinks
cat /sys/class/power_supply/*/online
cat /sys/class/power_supply/BAT*/status

# every power change since boot, hiding in the log
sudo dmesg -T | grep -i "unknown function number"

# the firmware's own map of the chip
sudo acpidump > acpi.dat && acpixtract -a acpi.dat && iasl -d dsdt.dat
grep -n "EmbeddedControl" dsdt.dsl

# the raw bytes
sudo modprobe ec_sys && sudo xxd /sys/kernel/debug/ec/ec0/io
```

Your bytes will be at different offsets. Field names differ by vendor and by
model, and mine were found by dumping the memory twice, once with the charger
in and once with it out, then comparing. It took about ten minutes.

The lesson I keep relearning is that the cheap direct measurement usually
exists, and I usually reach for it last. I spent hours on clever theories about
what killed that laptop. The answer was two bits, one second at a time, in a
log I had already written.
