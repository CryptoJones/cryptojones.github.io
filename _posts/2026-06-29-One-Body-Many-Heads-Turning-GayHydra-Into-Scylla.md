---
layout: post
title: "One Body, Many Heads: Turning GayHydra into Scylla"
audio: /audio/posts/One-Body-Many-Heads-Turning-GayHydra-Into-Scylla.mp3
---

*I built a Software Architecture course around a single stubborn idea — protect a
stable core, push all the volatility out to disposable edges — and then I put my
money where my mouth is. The capstone isn't a toy. It's a real, finished refactor:
how I wrapped **GayHydra**, my hardened Ghidra fork, in a hexagonal architecture and
turned it into **Scylla**, a reverse-engineering platform that grew nine different
"heads" without anyone ever touching the engine. This post is the short version of
that story.*

Watch the course playlist here:
[youtube.com/watch?v=wsWIRSx4qOQ](https://www.youtube.com/watch?v=wsWIRSx4qOQ&list=PLHJ9XgP4lCzY)

## The one big idea

Most of what people call "software architecture" is one principle wearing four
different hats. Hexagonal (ports & adapters), Clean/Onion, Domain-Driven strategic
design, and Juval Löwy's volatility-based decomposition all converge on the same
move:

> Find the part of the system that should almost never change, protect it ruthlessly,
> and shove everything that *does* change — UIs, transports, frameworks, the API
> fashion of the decade — out to the edges where you can throw it away and rebuild it.

Couple it badly and your software rots: a change in one corner drags six others with
it. Decompose by *volatility* instead of by function, and the things that change
together live together, while the durable center sits still. That's the whole thesis.
Scylla is what it looks like when you actually do it.

## GayHydra is the body. Don't rewrite the body.

The first rule is the **proven-engine maxim**: when you have a chunk of code that is
*correct* — battle-tested, congealed, full of decades of edge cases someone already
suffered through — you do not rewrite it to feel clever. You wrap it.

GayHydra is my hardened fork of Ghidra (Apache-2.0). It is the engine: the
disassembler, the decompiler, the analyzers. It is decidedly **not** something I was
ever going to reimplement in a weekend. So in the Scylla architecture, GayHydra is
the immovable body. Everything else is built *around* it, never *into* it.

## The durable core is a model, not a transport

The actual center of the architecture isn't even the engine binary — it's the
**reverse-engineering domain model**: functions, basic blocks, decompiled output,
cross-references, types. That model is completely transport-agnostic. It doesn't know
what a network is. It doesn't know what JSON is. A small Ghidra script (`dump_model`)
runs the engine headless and dumps that model into a stable, serialized artifact — a
`.scylla` file.

Once the truth lives in a portable artifact, everything downstream becomes a
*projection* of it. This is the part juniors usually miss: the stable thing to protect
is your **model of the domain**, not the database, not the framework, not the wire
format.

## Ports & adapters: the engine becomes a service

Here's the seam. The engine-as-service is the **port** — the abstract contract that
says "give me a binary, I'll give you the model." How that contract is *fulfilled* is
an **adapter**, and adapters are disposable on purpose:

- `analyzeHeadless` runs **inside a hardened container**, streams its results out over
  a thin gRPC surface, and a Rust client picks them up on the other side.
- The container, the gRPC skin, the client — all of it is the *edge*. When gRPC goes
  out of style (it will), I swap the thin skin and the core never notices.

This is the rule I hammer in the course: **don't let the era's universal adapter go
structural.** Every decade has a transport everyone swears is permanent — CORBA, SOAP,
REST, gRPC, and now MCP. Use them at the edge, never as the spine. The moment your
domain model imports your transport library, you've welded the disposable part to the
permanent part.

## Hardening the shell without touching the engine

Because the engine is sealed, I could harden the *adapter* aggressively without any
risk to correctness: read-only root filesystem, every Linux capability dropped,
`no-new-privileges`, a non-root user, memory/CPU/PID caps, and gRPC bound to loopback
only. The blast radius of "we run someone's untrusted binary" stays inside a box that
can't do anything.

That hardening pass also produced my favorite junior-teachable war stories — all of
them in the *shell*, none of them in the engine:

- **The JVM derives `user.home` from the passwd entry, not `$HOME`.** On a read-only
  root filesystem the launcher kept dying until I pointed home at a writable `/tmp`
  tmpfs. The fix was a one-liner; finding it was an afternoon.
- **A JRE is not a JDK.** The model-dump script compiles at *runtime*, so a
  runtime-only base image fails the moment it's needed. The base image has to ship a
  full JDK.
- **`/tmp` has to be mounted executable** for the same reason. "Secure defaults" and
  "actually runs" occasionally disagree, and you want that disagreement to surface
  loudly — so the service tails the analyzer's stderr on failure instead of swallowing
  it.

None of these touched GayHydra. That's the payoff of protecting the core: when the
edges fight you, the fight stays at the edges.

## Nine heads, one port

Scylla is a fitting name. The mythological Scylla had many heads on one body — and so
does this. Every "head" is just a different adapter projecting the **same client
port** (the same verbs: navigate, view, annotate, diff, merge, export). The body is
written once; the heads are thin:

- **Terminal (`scylla-cli`)** — a full RE tool in your shell. `diff` even uses
  `git diff --exit-code` semantics so it drops straight into CI.
- **AI agents (`scylla-mcp`)** — an MCP server so an LLM can drive reverse engineering.
  All binary-derived text is wrapped as untrusted data so the model treats it as
  *data*, never instructions.
- **Browser (`scylla-wasm`)** — the port compiled to WebAssembly; navigate an artifact
  entirely client-side, no server.
- **Remote (`scylla-rpc`)** — a Cap'n Proto RPC surface for networked consumers.
- **GraphQL, TUI, and an LSP** — yes, a *Language Server*. Since a binary has no source
  files, the head projects the whole program as one virtual document, functions in
  address order, one per line. Then "find references" on a function becomes "who calls
  it" — the call graph read backwards. Your editor navigates a stripped binary like
  it's source code.

Add them up — CLI, MCP, WASM, native server, RPC, GraphQL, TUI, LSP — and that's the
nine-headed monster. Every head was new code at the edge. The engine and the domain
model never moved. That's not luck; that's the architecture doing its job.

## The lesson, in one sentence

You can bolt a Language Server, a browser app, an AI agent, and a CI diff tool onto a
decades-old binary-analysis engine *without rewriting a line of it* — if, and only if,
you decided up front which part was the body and which parts were allowed to be heads.

The full capstone walks through every principle against the real commit history.

- **Course:** [the Software Architecture playlist](https://www.youtube.com/watch?v=wsWIRSx4qOQ&list=PLHJ9XgP4lCzY)
- **GayHydra (the engine):** [codeberg.org/CryptoJones/GayHydra](https://codeberg.org/CryptoJones/GayHydra)
- **Scylla (the hexagon around it):** [codeberg.org/CryptoJones/Scylla](https://codeberg.org/CryptoJones/Scylla)

*Proudly Made in Nebraska. Go Big Red! 🌽 <https://xkcd.com/2347/>*
