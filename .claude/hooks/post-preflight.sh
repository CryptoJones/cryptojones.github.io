#!/usr/bin/env bash
# UserPromptSubmit: reset the per-turn AGENTS.md gate, and when the turn looks
# like post work, demand a pre-flight declaration before any producing starts.
#
# This is the soft half of the pair and it is honest about being soft. The gate
# in post-rules-gate.sh can force a file to be OPENED; nothing can force it to
# be BELIEVED. What this does is make the gap visible early: an agent that has
# to list the rule files it read, with line numbers, discovers the empty list
# while the work is still cheap to redo.
#
# stdout from a UserPromptSubmit hook is injected as additional context.
set -uo pipefail

STATE="${XDG_STATE_HOME:-$HOME/.local/state}/cryptojones-blog"
mkdir -p "$STATE" 2>/dev/null || true

input="$(cat)"

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

# A new user message is a new turn: the previous turn's read does not carry.
rm -f "$STATE/agents-read-$sid" 2>/dev/null || true

prompt="$(field '.prompt')"
[ -n "$prompt" ] || prompt="$(field '.user_prompt')"

# Only speak up when the turn plausibly touches a post. A reminder that fires on
# every prompt is a reminder that gets skimmed -- which is the exact failure this
# is meant to prevent, one level up.
shopt -s nocasematch
case "$prompt" in
  *post*|*blog*|*publish*|*article*|*narrat*|*audio*|*draft*|*writ*) ;;
  *) exit 0 ;;
esac
shopt -u nocasematch

cat <<'MSG'
PRE-FLIGHT (cryptojones.github.io) -- this turn may involve a blog post.

Before you produce anything, state:
  1. Which rule files you read this turn, with the line numbers you are relying
     on. AGENTS.md defines when a post is DONE; CLAUDE.md defines the sensitive
     data scrub. Two sample posts are not a substitute for either.
  2. What "done" requires for this specific piece of work, quoted from the file
     rather than inferred from what other posts happen to look like.

If that list is empty, read the files before writing, not after. An absence is
not evidence: "no post here has X" is a fact about your sample, not a rule.
MSG
