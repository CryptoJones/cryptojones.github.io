---
layout: post
title: "Letting Windows Users Have the Life They Chose"
description: "Windows support drains time from small software projects. This post argues for macOS and Linux builds, honest limits, and letting Windows users handle the bridge."
audio: /audio/posts/Letting-Windows-Users-Have-the-Life-They-Chose.mp3
---

I am done treating Windows as a required build target.

That does not mean Windows users are banned. It means I am no longer spending my time making a native Windows package for every tool I build. If the software runs on macOS and Linux, that is the product. Windows users can decide how they want to run it.

> A **build target** is an operating system or type of computer that a project promises to support with tested releases.

For years, a Windows build looked like a sign that a project had grown up. It meant more people could click a download button and get started. That made sense when most software had to live directly on the user's desktop.

It makes less sense for developer tools, servers, command-line programs, and self-hosted apps. These tools already live in a Unix-shaped world. Their production servers run Linux. Their containers run Linux. Their setup guides assume a Unix shell. Macs are now the main work machines for most developers I know. macOS also gives them the same basic tools and shell habits they use on Linux servers.

Linux and macOS belong in the same build plan. Forcing a native Windows build into that plan often creates a third product that only looks like the first two.

## Support is not a checkbox

A Windows build is easy right up until it is not.

Paths use different marks. File names follow different rules. Shell commands change. Permissions work in another way. Symbolic links may fail. A file that can be replaced on Linux may still be locked on Windows. An antivirus tool may hold a build, scan it, or warn about it. Installers need their own care. Signing needs more tools and more money.

None of these problems is impossible. That is not the point. The point is that they take time every week.

Then there is testing. A green compiler run is not support. Someone has to use the program on Windows, catch strange behavior, test upgrades, and answer bug reports. If nobody on the core team does that, the Windows badge is mostly theater. The project has made a promise it cannot keep.

I would rather make two honest promises than three weak ones.

## The worst bugs are the boring ones

Windows support rarely fails in a grand and interesting way. It fails through a pile of small cuts.

A script quotes an argument wrong. A path grows too long. A test passes on Linux and leaves a file open on Windows. A package uses a tool that comes with every Linux system but not with Windows. A release job breaks because one runner changed its image.

Each bug seems small. Each fix also needs a test so it does not return. Soon the project carries branches, wrappers, and special cases that have nothing to do with what the software is meant to do.

That cost lands hardest on small projects. A large company can pay a Windows team. A small group may have one maintainer working after dinner. Asking that person to support every major system is not being fair to users. It is asking for free labor with no end date.

## Windows already has a bridge

Windows users are not stuck. Windows Subsystem for Linux, usually called WSL, can run a Linux environment inside Windows. Containers and Linux virtual machines offer other paths.

> A **virtual machine** is a computer made in software. It can run Linux in a window on a Windows computer.

Those choices are good enough for many developer tools and self-hosted apps. They also put the border where it belongs. The Windows system handles Windows. The Linux program gets the setting it was built and tested for.

Yes, that adds a setup step. So does native Windows support. The difference is who owns the cost. I do not think every small software project should rebuild the same bridge. Microsoft made Windows. Microsoft also made WSL. Let that bridge do its job.

## No more fake support

Dropping Windows should be clear, not sneaky.

The project page should say that macOS and Linux are the supported targets. The install guide should show WSL or a virtual machine as a path for Windows users. The issue form should not pretend that native Windows bugs will be fixed. Release notes should not offer an old Windows package that nobody has tested in a year.

Community patches are welcome if they are clean and do not make the macOS or Linux builds worse. A person or company can fund a Windows maintainer if native support matters to them. What they cannot do is turn a download count into a claim on somebody else's weekends.

There are obvious cases where Windows must be a target. A Windows driver needs Windows. A desktop program sold to Windows users needs Windows. This argument is for the large class of developer tools that fit macOS and Linux and only ship a Windows build because people expect to see one.

Expectation is not a good reason to carry dead weight.

## Let them choose the whole thing

People choose Windows for many sound reasons. Their job may require it. Their games may run there. They may know it well and like it. Fine. Keep it.

But a choice has edges. Choosing an operating system does not mean every volunteer developer owes that system a native port. Sometimes the answer is WSL. Sometimes it is a container. Sometimes it is a Linux machine on the network. Sometimes the software is simply not for that setup.

That is not punishment. It is a boundary.

My build system should spend its time proving that the real product works. My release process should be short enough to trust. My bug list should be about the program, not the habits of an operating system I do not use.

So I am keeping macOS and Linux as build targets and dropping Windows. Windows users can still come along. They just have to bring their own bridge.

They chose the life. Let them have the whole thing.
