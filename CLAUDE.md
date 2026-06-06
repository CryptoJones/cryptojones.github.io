# CLAUDE.md — cryptojones.github.io

Jekyll blog (CRT/phosphor theme) hosted on GitHub Pages. Posts are Markdown in
`_posts/`; standalone hand-styled guides are root-level `*.html`.

## Authoring a blog post

- File: `_posts/YYYY-MM-DD-Title-With-Dashes.md`.
- Front matter: `layout: post` and a quoted `title:`. The `post` layout renders
  the title as the page `<h1>`, so **do not** repeat the title as an `#` heading
  in the body. Lead with the intro/subtitle paragraph instead.
- New posts auto-appear in the index (it loops `site.posts`); no manual index edit
  needed. The homepage "featured guide" pin in `index.html` is optional and manual.
- Source drafts often arrive from CryptoJones's real machines (e.g. via `scp`), so
  assume they contain live infrastructure details until proven otherwise.

## MANDATORY: scrub sensitive data before publishing

Every post is public the moment it merges. **Before writing or committing any post,
genericize all real-world identifiers.** Never publish:

- **Private/real IPs, subnets, CIDRs** (e.g. `172.16.x`, `10.x`, real `192.168.x`),
  router/gateway IPs, MAC addresses.
- **Internal hostnames** and machine names (`mac-mini`, `*.local`, real `*.ts.net`
  names), real `*.ts.net`/tailnet identifiers.
- **Real service host:port + path combos** that reveal internal infra
  (e.g. an LLM endpoint like `:8080/v1/models`).
- **Secrets**: API keys, tokens, auth keys, passwords, private cert/key material.
- **Personal paths & usernames** (`/Users/akclark/...`, `$USER` expansions),
  real file paths from the source machine.
- **Unintended personal details**: employer/client names, phone numbers, non-public
  email, location specifics.

Replace with documentation placeholders:

| Real thing | Use instead |
|---|---|
| LAN subnet / gateway | `192.168.1.0/24` / `192.168.1.1` (or RFC 5737 `192.0.2.0/24`) |
| Internal host:port | `192.168.1.50:8080` with a generic path (`/`) |
| Hostname | `your-host`, `<host>.<tailnet>.ts.net` |
| Username / home path | `youruser`, `/home/youruser/...` |
| Secrets | `<your-api-key>`, `<token>` |

Keep the teaching value: add a "substitute your own values" note rather than real
data. Public profile links already in `_config.yml` (GitHub, LinkedIn, etc.) are
intentional and fine.

**Final check before commit:** grep the new/changed post for `172.16`, `10.`,
real `192.168`, `/Users/`, `/home/`, tokens, and internal hostnames. If anything
real survives, fix it before committing.

## Attribution

Copyright/attribution: **CryptoJones** <cryptojones@owasp.org>.
