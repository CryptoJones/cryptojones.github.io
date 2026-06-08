---
layout: post
title: "From a Memory Aid to Multi-Tenant: The .NET Decision That Exploded the Scope"
---

*ApplyTrack started life as a glorified memory aid — a folder of Markdown files
so I'd stop forgetting where I'd applied and when to follow up. It is now an
open-source, multi-tenant, self-hostable application with magic-link auth, a
two-runtime backend, and a CI pipeline that ships container images. This post is
about the single design decision that turned the first thing into the second one
— moving the core API off pure Python and onto .NET — and the avalanche of scope
that came with it.*

*It's also, secretly, a post about systems design. I've been told the thing that
separates a senior or staff engineer from a strong mid-level one isn't knowing
more frameworks — it's reasoning about **trade-offs, invariants, coupling, and
failure modes** before you write a line of code. So as I walk through this
rewrite I'm going to narrate the systems-design thinking out loud: the concepts I
reached for at each fork, and why. The project was, honestly, an excuse to
practice exactly that muscle.*

## What it actually was at the start

The honest origin story: I kept losing track of job applications. Did I already
apply to that company? When was I supposed to follow up on the screen? What
salary did the post say before they took it down?

So I built the dumbest possible thing that solved it. Every application was a
Markdown file with some YAML frontmatter:

```markdown
---
company: Acme Corp
role: Senior Platform Engineer
lane: applied
status: screen
link: https://example.com/jobs/123
salary: "$180k–$210k"
applied: 2026-05-01
followup: 2026-05-08
score: 87
---

Recruiter was responsive. Take-home is a Postgres schema design.
```

The whole "database" was a directory of those files. State lived in three JSON
files next to it — `.criteria.json` for my search keywords, `.blacklist.json`
for companies I never wanted to see again, `.seen.json` so the discovery poller
wouldn't show me the same listing twice. A thin FastAPI app put a vanilla-JS
single-page app in front of it, and a Python poller scraped a handful of public
job boards and dropped fresh matches in as new files.

That's it. **Single user. Files on disk. No auth worth the name.** It was a
memory enhancement utility, and for one person it was *perfect*. The "schema"
was a slug naming convention. The "migration story" was `git add`.

## The deceptively small product decision

Then I decided to open-source it and make it something other people could
self-host for their own job search. On the surface that sounds like a packaging
problem — write a README, add a Dockerfile, push to GitHub. Ship it.

It is not a packaging problem. The moment "one person" becomes "many people on
one deployment," every cozy assumption the file-based design rested on falls
over at once:

- A folder of Markdown files has no concept of *whose* files they are.
- Three shared JSON config files can't hold one search profile **per user**.
- "No auth" stops being charmingly minimal and starts being a data breach.
- A `.seen.json` that dedupes for *me* will happily hide your leads behind mine.

This is the first place systems-design thinking earns its keep. Multi-tenancy
isn't a feature you bolt on the side — it's a **system invariant**: a property
that has to hold on *every single read and write in the system*, in both
runtimes, forever. Invariants are the things you design the system *around*, not
checks you remember to sprinkle in. And the test of a design is whether it can
even *express* the invariant you need. The file-on-disk model couldn't express
"this row belongs to that user" at all — there was no place for the constraint to
live. That's the tell that you've outgrown a data model: not that it's slow, but
that the property you now need is *inexpressible* in it.

## The fork in the road: stay Python, or move the core to .NET

Here's where the real decision was. The path of least resistance was obvious:
keep it all Python. FastAPI was already there. Reach for SQLAlchemy, bolt on an
auth library, add a `tenant_id` foreign key, and grind it out in the language
the whole thing was already written in. One runtime, one mental model, no
context-switching.

I didn't do that. I moved the core API to **.NET 10** — ASP.NET Core Minimal
APIs on Kestrel, Dapper + Npgsql over Postgres, DbUp for migrations — and kept
Python *only* for the discovery poller.

The reasons that won the argument were all systems-design arguments, not language
preferences:

- **The auth + session + concurrency surface is exactly what this stack is built
  for.** Multi-tenant CRUD with optimistic locking, server-side sessions, and a
  hard request-scoped security boundary is bread-and-butter ASP.NET Core. The
  design principle here is *don't hand-roll your load-bearing primitives* —
  identity, sessions, and concurrency control are exactly the parts where a
  framework's well-trodden spine beats a bespoke assembly of libraries, because
  the failure mode of getting them subtly wrong is "data breach," not "bug."
- **Hand-written SQL over a typed data layer.** Dapper maps SQL straight to
  records with no ORM mystery. This is a *legibility* trade-off: for a schema that
  two different runtimes have to agree on byte-for-byte, I wanted the SQL to be
  the explicit, reviewable contract, not an abstraction generating queries I'd
  have to reverse-engineer. An ORM optimizes for developer convenience; I was
  optimizing for *the boundary being inspectable*.
- **I wanted the invariant to be structurally enforced, not remembered.** A
  compiled, statically-typed API layer lets me make "every query filters
  `tenant_id`" a property of the *type system and the DI graph* rather than a rule
  in a code-review checklist. The best way to enforce an invariant is to make
  violating it *unrepresentable* — and a typed boundary gets you closer to that
  than a dynamically-typed one.

I knew, choosing it, that I was trading a weekend of Python grinding for
something much bigger. I underestimated by how much — but that's the other
half of staff-level thinking: the cheap option and the *right* option are often
different options, and the skill is knowing when the goal has changed enough that
the cheap one is now the expensive one.

## The avalanche

Picking .NET didn't just change the language. It detonated the scope, because
once you commit to a *real* API you have to actually build all the things the
file-based toy got to skip:

**A real schema, and migrations to evolve it.** The folder-of-files became nine
DbUp migrations — `applications`, `search_profiles`, `blacklist`, `users`,
`magic_tokens`, `sessions`, `seen`, `poll_requests`, and the cascade wiring.
Idempotent `.sql` scripts that run on startup. The slug naming convention became
a `UNIQUE (tenant_id, name)` constraint and a validation choke-point.

**Real authentication.** I built passwordless magic-link sign-in: request a
link, get a single-use token (only its SHA-256 is stored, 15-minute TTL), verify
it, and mint an **opaque server-side session** — deliberately not a JWT, so
logout is instant revocation, not "wait for the token to expire." The endpoint
that requests a link always returns `200` whether or not the account exists, so
it can't be used to enumerate who has signed up.

**A tenancy choke-point.** This is the heart of the whole rewrite, and it's the
single design pattern I'm proudest of. The systems-design idea is *funnel the
dangerous decision through exactly one place*. One middleware resolves the
session cookie to a tenant, and it is the **only** place a `tenant_id` enters the
system. Endpoints are handed a repository from DI that's already scoped to the
caller — endpoint code physically cannot query another tenant's rows, because it
never sees a tenant id to get wrong. That's the difference between a security
*control* and a security *invariant*: instead of N endpoints each remembering to
filter correctly (N chances to leak), there's one choke-point and N endpoints
that *structurally can't*. You shrink the attack surface to a single auditable
function:

```csharp
// every read and write carries the tenant, unconditionally
UPDATE applications
   SET ..., version = version + 1
 WHERE id = @id AND tenant_id = @tenantId AND version = @expectedVersion;
// 0 rows affected -> 409 Conflict
```

**Optimistic concurrency.** The old design's "version" was a file's mtime and
size. On a multi-user database that's meaningless, so every application row got a
real `version` column. Writes pass `?expected_version=`, a mismatch answers
**409 Conflict**, and the SPA's overwrite-confirm flow drives off that — two
open tabs can't silently clobber each other. The design decision underneath is
*optimistic vs. pessimistic locking*: I bet that write-write conflicts are rare
(two people rarely edit the same application row at the same instant), so I don't
pay the cost of locking rows on every read — I just detect the rare collision and
make the client resolve it. Choosing the concurrency-control strategy that
matches your *actual* contention profile, rather than reflexively reaching for
locks, is a very systems-design call.

**Security designed in, not bolted on — graded against 20 years of OWASP.** Once
strangers trust the thing with their data, "I'll secure it later" is a design
smell, so I audited the app against the **OWASP Top 10** — and not just the
current list. I ran it against two decades of the Top 10, every edition back to
the original 2007 list, because the categories that *rotate off* the list don't
stop being exploitable; they just stop being fashionable. (CSRF dropped off years
ago, but a multi-tab session app still has to answer for it.) The threat model is
the union of all of them, not the latest snapshot. What came out of that audit: a
strict CSP and a security-header middleware, per-IP rate limits, an SSRF-hardened
link probe (because a server that fetches user-supplied URLs is a confused-deputy
waiting to happen), DOMPurify on rendered notes to kill stored XSS, generic 500s
that don't leak internals, the no-account-enumeration auth surface, and a
dependency-audit CI job so a vulnerable transitive package fails the build instead
of shipping.

**And then everything else that comes after "it works on my machine":** a
three-service `docker compose up`, account export (a zip of your Markdown — your
data stays yours) and one-call account deletion via `ON DELETE CASCADE`, and a
tag-driven release pipeline that publishes both runtimes as container images. None
of that existed in the memory-aid version. None of it is optional once strangers
trust the thing with their data.

## The compromise that kept it sane: polyglot, with the schema as the contract

The one thing I refused to do was rewrite the poller. It already had eight source
fetchers, the HTML scraping, and the scoring/dedup logic — all in working,
tested Python. Re-implementing that in C# would have been throwing away the part
that already worked to satisfy a purity I didn't care about.

So ApplyTrack is deliberately **polyglot**: a .NET API and a Python poller that
**never call each other**. They share exactly one thing — the Postgres schema —
and that schema *is* the contract between them.

```
            ┌─────────────────────────────────┐
Browser ──► │ ASP.NET Core (.NET 10, Kestrel)  │
 (the SPA)  │  • serves the SPA + JSON API     │──┐
            │  • magic-link auth + sessions    │  │
            │  • CRUD + criteria + blacklist   │  │
            └─────────────────────────────────┘  ├──► Postgres  (shared schema
            ┌─────────────────────────────────┐  │              = the contract)
 Cron  ───► │ Python poller                    │──┘
            │  • fetch + score + dedupe leads  │
            │  • drain the on-demand poll queue│
            └─────────────────────────────────┘
```

The systems-design backbone here is **clear data ownership**. Every table has
exactly one writer-of-record: .NET owns auth, sessions, and CRUD, and it owns the
migrations; Python writes new leads and reads profiles, the seen-ledger, and the
active-user list. Ambiguous ownership ("either service might write this") is how
you get races and corruption that no amount of locking saves you from, so I made
ownership explicit and one-directional. **Both runtimes unconditionally filter
`WHERE tenant_id`** — the cron worker doesn't get to bypass the choke-point just
because it's a background job; it builds a tenant-scoped reader *inside* its
per-tenant loop. (The invariant doesn't get a day off because the request didn't
come from a browser.)

Two more design choices in that diagram are doing quiet work:

- **Decoupling via a queue.** The "Poll now" button doesn't shell out to Python
  from C# — synchronous cross-runtime calls would couple their uptime and latency
  together. Instead it drops a row in a `poll_requests` queue that the worker
  drains on its own schedule. That's the classic move: turn a *temporal* coupling
  into an *asynchronous* one. The API can answer "queued" in milliseconds even if
  the poller is mid-run or restarting; neither runtime blocks on the other.
- **Failure isolation / blast radius.** The worker processes tenants in a loop
  where one tenant's failure is caught and *can't* abort the others. When you have
  a shared background job, the design question is always "what's the blast radius
  of one bad input?" — and the answer here is "one tenant's poll, not everyone's."

This contract is the part I'd defend hardest in an interview. The temptation when
you go polyglot is to have the two halves talk over an internal HTTP API — and
then you've signed up for versioning, retries, authentication *between your own
services*, and a second contract to keep in sync. That's **accidental coupling**
dressed up as architecture. Making the *database the single source of truth* and
the *schema the contract* meant there was exactly one thing to keep honest, with
no network partition to reason about between the halves and a schema-shape test on
each side to guard against drift. Fewer moving parts that can disagree is, almost
always, the better system.

## Was the .NET decision worth it?

Yes — but I want to be honest about what "yes" cost.

If the goal had stayed "help *me* remember my applications," choosing .NET would
have been malpractice. The Markdown-files version was better at that job:
zero infrastructure, grep-able, git-versioned, done in an afternoon. The whole
multi-tenant edifice would have been a monument to a problem I didn't have.

The decision was right *because the goal changed*. The instant the target became
"many people, one deployment, self-hostable, don't leak anyone's data," I needed
a real security boundary, real sessions, real concurrency control, and a schema
that could evolve under live data. Those are precisely the problems .NET's spine
is shaped to hold, and leaning on it — instead of hand-assembling the same guards
out of Python libraries — is why the tenancy story is *one middleware and a
scoped repo* instead of a discipline I have to re-prove in every endpoint.

The lesson I'm taking with me is a systems-design one: **the scope explosion
wasn't caused by the technology choice — it was *revealed* by it.** The
multi-tenant complexity was an inherent property of the problem the moment I went
from one user to many; pure Python wouldn't have made it smaller, just quieter and
easier to get subtly wrong. Picking the stack that makes the invariant loud forced
me to actually build the invariant. Going from a memory aid to a real application
was never going to be a packaging task. It was a different application wearing the
old one's name.

And that, I think, is the actual content of "be good at systems design" — the
thing I keep hearing is the gate to senior and staff roles. It isn't memorizing
patterns. It's the habit of, at every fork, asking the questions this rewrite kept
forcing on me: *What invariant must hold, everywhere, forever? Where does the
dangerous decision get funneled so it's auditable in one place? Who owns this
data, and is that ownership unambiguous? What's coupled to what, and can I trade a
synchronous dependency for an asynchronous one? What's the blast radius when this
fails — because it will fail?* The stack I picked didn't make me ask those
questions. It just made it impossible to skip them. Honestly, that's why I built
the thing the hard way: a side project is the cheapest place there is to practice
the expensive kind of thinking.

## The part I deliberately left out: a local frontier model

There's a feature I cut from v1 on purpose — an AI engine for drafting tailored
cover letters and application materials. It was the heaviest thing to build and
the scariest data to handle, so the disciplined call was to ship the tracker
without it and leave a clean seam for later. (Knowing what *not* to build yet is
its own systems-design skill; scope is a design decision.) But I keep turning over
what that seam could become, and the answer that excites me isn't "call an API."
It's: **run a powerful frontier model locally, right next to the data.**

Think about the shape of this app. It's self-hosted, no telemetry, your data
stays on your box — that's the whole pitch. The instant you bolt on a hosted LLM,
you've quietly broken that promise: now your entire job search, your résumé, every
note you wrote about a recruiter, is flowing to a third party's servers to be
logged and maybe trained on. A *local* model is the only addition that doesn't
violate the thing that makes ApplyTrack worth self-hosting in the first place.
**Data locality isn't just a performance idea — here it's the privacy
architecture.** The model comes to the data; the data never leaves.

And once a capable model is sitting in the same trust boundary as the database, a
lot of the app's rough edges turn into soft ones:

- **Discovery gets a brain.** Today the poller scores leads with keyword matching
  — blunt, full of false positives. A local model does *semantic* relevance: it
  actually reads the posting against your history and your real preferences, not
  just your keyword list. It can extract clean structured fields out of the messy
  free-text every board formats differently, and explain *why* a lead scored the
  way it did.
- **The materials engine, finally.** Draft a cover letter grounded in the specific
  posting *and* your own past applications — retrieval over your history, not a
  generic template. Tailor a résumé summary per role. All of it on hardware you
  control, with your writing never leaving the building.
- **A research assistant over your own funnel.** "What stage is everything in, and
  what's gone cold?" "Summarize every interview note for this company before my
  onsite." "Which of these three offers fits what I said I wanted?" That's RAG over
  data the app already owns.

Here's the systems-design payoff, and the reason I'm dwelling on it: **the
architecture I already built is exactly the shape that makes this a clean add.**
The polyglot, schema-as-contract design means a model runtime is just *another
worker against the same database*, behind the same tenant choke-point, owning its
own writes — no different in kind from the Python poller. I wouldn't be retrofitting
AI into a monolith; I'd be adding a third lane to a system that was already
designed as decoupled lanes sharing one contract. The decoupling I did for boring
reasons (keep the Python fetchers, don't couple the runtimes) turns out to be the
thing that makes the *interesting* future cheap. Good boundaries pay you back in
directions you didn't predict when you drew them — which is, maybe, the whole
argument for caring about them.

## Where this falls over at enterprise scale

I want to close on the most senior-engineer move there is: being honest about the
limits of your own design. ApplyTrack is built for *self-hosting and small
multi-tenant deployments* — dozens, maybe low hundreds of users on one box. The
architecture is deliberately right-sized for that. If someone asked me to take it
to "enterprise" — thousands of orgs, millions of applications, an SLA — here's
where I already know it would break, roughly in the order the cracks would show:

- **The single Postgres is the first ceiling.** Every layer leans on one database:
  CRUD, the session lookup on *every authenticated request*, the poll queue, and
  the poller's writes all land on the same instance. That's a single point of
  failure and a single point of contention. The first work is the boring,
  load-bearing stuff: a primary with read replicas, a connection pooler
  (PgBouncer) so thousands of clients don't exhaust backends, and moving the
  hot-path session check off Postgres into a cache like Redis. Server-side sessions
  bought me instant revocation; at scale that convenience becomes a per-request
  database read I'd have to buy back with a cache + invalidation.

- **Pooled (shared-schema) tenancy hits a wall — both technically and on
  compliance.** Row-level `tenant_id` filtering is the right call for hundreds of
  tenants, but it has a *noisy-neighbor* problem (one tenant's heavy queries
  degrade everyone on the shared tables) and a *trust* problem (enterprise buyers,
  SOC 2, data-residency rules often demand physical isolation, not "we promise the
  `WHERE` clause is always there"). The escape path is a tenancy spectrum:
  Postgres row-level security as belt-and-suspenders, then schema-per-tenant, then
  database-per-tenant or sharding by tenant for the big customers. None of that is
  free — it turns one migration into N, and the choke-point has to learn to route.

- **The poller doesn't scale horizontally — it's one cron worker in a `for`
  loop.** Fetch-once-per-run is a clever rate-limit dodge at small scale, but the
  scoring pass is O(tenants × listings) on a *single* process, and a slow source
  stalls the whole sweep. Enterprise needs the work fanned across many workers
  (tenant sharding with leader election or partition assignment, so two workers
  never double-process a tenant), a real broker (SQS/Redis/Kafka) instead of a
  database-polling `poll_requests` table, per-source rate-limit *budgets*, and
  backpressure so a board outage doesn't cascade. Scraping public boards at all is
  itself brittle at volume — IP bans, CAPTCHAs, ToS exposure — so at scale you'd
  push toward official APIs and a shared caching layer in front of every source.

- **The schema-as-contract that saved me small becomes a coupling tax large.**
  Two runtimes sharing one database is the perfect amount of architecture for two
  components; the *shared-database integration* pattern is a known anti-pattern
  the moment you have several teams and services, because it couples their deploys
  and their schema evolution. Past a certain size you have to break the shared DB
  into service-owned stores that talk over events or APIs — which reintroduces
  exactly the versioning-and-contracts cost I was so happy to avoid. That's not a
  mistake in the current design; it's the trade-off having an expiry date.

- **The identity model assumes one human per tenant.** Today `tenant_id == user.id`
  — fine for individuals self-hosting. Enterprise means *organizations*: many users
  per tenant, teams, roles and RBAC, SSO/SAML/OIDC and SCIM provisioning instead of
  magic links, and an audit log of who-did-what for compliance. The schema was
  named to future-proof orgs, but actually building them is a real project on its
  own.

- **And everything operational I got to ignore at one box.** Single-node Docker
  Compose has no HA, no rolling deploys, no autoscaling — that's Kubernetes or a
  managed platform, multiple stateless API replicas behind a load balancer (easy,
  since sessions live in the data tier) and a poller that's safe to run more than
  one of (hard). Plus the things multi-tenant SaaS lives or dies on: per-tenant
  metering and quotas so one tenant can't starve the poller, distributed tracing
  and structured logs, alerting, and an unbounded-growth story (partitioning and
  archival for `applications` and the `seen` ledger) before the tables get slow.

The through-line: almost none of these are *bugs*. They're trade-offs I made
**on purpose** for the scale I'm actually at, each with a known escape hatch for
the day the scale changes. That's the real deliverable of systems-design thinking
— not a system that's ready for a million users, but one where you can name,
precisely, what would have to change to get there, and why you correctly chose not
to build it yet.

---

*ApplyTrack is open-source (Apache-2.0) and self-hostable —
[github.com/CryptoJones/OSApplyTrack](https://github.com/CryptoJones/OSApplyTrack).
One `docker compose up` brings up the database, the API, and the poller. Your
data is yours: one-click Markdown export, one-call account deletion, no
telemetry, no SaaS.*
