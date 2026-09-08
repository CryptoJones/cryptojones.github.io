#!/usr/bin/env bash
# Gate: do not write a blog post until AGENTS.md has been read THIS TURN.
#
# Why this exists (2026-09-08): an agent wrote and shipped a post with no
# narration, then offered narration as an optional extra. AGENTS.md in this repo
# carries a header reading "Definition of done for a post -- NARRATION IS NOT
# OPTIONAL". The file was never opened. The failure was not a missing search; it
# was building a working model of the repo from two sample posts and never going
# back for the file that defines "done".
#
# So the gate sits at the transition from understanding to producing, which is
# where that class of error happens -- not at the start of a task, where an
# agent is already careful.
#
# Two roles, chosen by $1:
#   record   PostToolUse on Read|Bash          -- note AGENTS.md was really read
#   enforce  PreToolUse  on Write|Edit|Bash    -- block post writes until it was
#
# Bash is matched on both sides on purpose. Under bypass-permissions the model
# is told to prefer cat/heredocs over Read/Write, so a gate that only watched
# the dedicated file tools would be watching an empty road.
set -uo pipefail

MODE="${1:-enforce}"
STATE="${XDG_STATE_HOME:-$HOME/.local/state}/cryptojones-blog"
mkdir -p "$STATE" 2>/dev/null || true

input="$(cat)"

# field <dotted.path> -- jq on the fast path, python3 when jq is absent. Never
# install anything: a hook that tries to bootstrap its own dependency can wedge
# the host it is supposed to be protecting.
field() {
  if command -v jq >/dev/null 2>&1; then
    printf '%s' "$input" | jq -r "$1 // empty" 2>/dev/null
  else
    printf '%s' "$input" | python3 -c '
import json, sys
path = sys.argv[1].lstrip(".").split(".")
try:
    d = json.load(sys.stdin)
    for p in path:
        d = d.get(p, "") if isinstance(d, dict) else ""
    print(d if isinstance(d, str) else "")
except Exception:
    print("")
' "$1"
  fi
}

sid="$(field '.session_id' | tr -cd 'A-Za-z0-9._-')"
[ -n "$sid" ] || sid="nosession"
FLAG="$STATE/agents-read-$sid"

tool="$(field '.tool_name')"
target="$(field '.tool_input.file_path')"
[ -n "$target" ] || target="$(field '.tool_input.command')"
[ -n "$target" ] || exit 0

if [ "$MODE" = "record" ]; then
  # PostToolUse fires only after the tool succeeded, so the flag means the file
  # was genuinely read -- not merely requested and then denied or errored.
  case "$target" in
    *AGENTS.md*) : > "$FLAG" ;;
  esac
  exit 0
fi

# ---- enforce ---------------------------------------------------------------

# Only writes that land in a post or its narration asset are gated.
case "$target" in
  *_posts/*|*audio/posts/*) ;;
  *) exit 0 ;;
esac

# Reads and searches are never gated -- blocking those would deadlock the fix.
case "$tool" in
  Write|Edit|NotebookEdit) ;;
  Bash)
    case "$target" in
      *">"*|*"cp "*|*"mv "*|*"sed -i"*|*"tee "*|*"python3"*|*"python "*) ;;
      *) exit 0 ;;
    esac
    ;;
  *) exit 0 ;;
esac

[ -f "$FLAG" ] && exit 0

cat >&2 <<'MSG'
BLOCKED: read AGENTS.md before writing a post.

You are about to write a post or its narration asset without having opened
AGENTS.md this turn. That file -- not the sample posts you skimmed -- defines
when a post is finished. The last agent to skip it shipped a silent post and
called it done.

Read it, then retry:

    sed -n '45,150p' AGENTS.md

Then, before producing anything, state the rule files you read and the lines you
are relying on. If you cannot cite a line for "this post is done", you have not
checked it, you have assumed it.

The gate clears for the rest of this turn once AGENTS.md is actually read, and
resets on the next user message.
MSG
exit 2
