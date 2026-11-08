---
name: handoff
description: Write or update handoff.md so a fresh session (Claude, Codex, or a labmate) can continue the current task. Use when the user says "handoff", "wrap up", "save progress", "I'll continue later", or when the context window is getting full.
user-invocable: true
argument-hint: "[output_path]"
---

# Handoff Writer

Write a concise, structured `handoff.md` capturing the current state of the task, so someone with zero context can continue in under a minute.

## Arguments

- `$0` = output path (default: `handoff.md` in the project root). If the file exists, update it in place: keep still-valid content, revise what changed, refresh the timestamp.

## Steps

1. Review the conversation and the working tree (`git status`, `git diff --stat`, recent logs) to determine what was actually done. Do not rely on memory alone.
2. Write the file using the template below. Be specific: file paths with line numbers, job IDs, exact commands, numbers.
3. Keep it under ~80 lines. Link to files instead of pasting their contents.
4. Print the path and a 3-line summary to the user.

## Template

```markdown
# Handoff: <task name>  (updated <YYYY-MM-DD HH:MM>)

## Goal
<1–2 sentences: the end result, and how we'll know it's done>

## Current state
- Done: ...
- In progress: ... (<file:line>, what is half-finished)
- Not started: ...

## Key decisions (and why)
- <decision>: <reason>

## What we tried that did NOT work
- <attempt>: <why it failed / what we learned>

## Open questions / blockers
- ...

## Next steps (in order)
1. ...

## Key files / commands
- <entry-point script>, <results dir>, <log files / SLURM job IDs>
- To reproduce current state: `<command>`
```

## Rules

- The "did NOT work" section is mandatory. Write "none yet" if empty. It prevents the next session from repeating dead ends.
- Never include secrets, tokens, or individual-level controlled-access data.
- Do not invent progress. If something is unverified, say "unverified".
