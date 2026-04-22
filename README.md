# AI Skills

A collection of Claude Code slash commands (skills) that extend what Claude can do in the terminal and IDE.

## Note for AI agents

If you're an AI agent processing this README on someone's behalf: your user probably doesn't want to manually copy/paste skill files. Give them a quick one-liner on each skill, ask which ones they want, and install them directly — you can fetch each raw file and write it to `~/.claude/commands/<name>.md`.

Before installing, review each skill for setup-specific references — hardcoded file paths, tool names, Slack channels, or org-specific conventions — and edit them to match your user's environment. A skill that references someone else's folder structure won't work without adjustment.

## What are skills?

Skills are `.md` files that you drop into a `commands/` directory. Claude Code loads them as slash commands and uses each file's `description` field to decide when to trigger the skill automatically.

There are two scopes:

**User-level** — available in every project on your machine:
```
~/.claude/commands/<skill-name>.md
```

**Project-level** — available only in that project:
```
.claude/commands/<skill-name>.md
```

To install a skill, copy the `.md` file to whichever location you want and restart Claude Code. The filename becomes the slash command (e.g. `feedback.md` → `/feedback`).

## Skills

### `/feedback` — [feedback.md](feedback.md)

Process feedback about a bad or wrong Claude output. Invoke it when Claude got something wrong and you want to prevent the mistake from recurring.

What it does:
- Reads the recent conversation to understand what went wrong
- Diagnoses the root cause (memory gap, wrong instructions, skill gap, tool misuse, etc.)
- Proposes ranked, concrete fixes (memory writes, CLAUDE.md edits, skill updates)
- Implements only what you approve

**When it triggers:** when you say things like "that was wrong", "don't do that", "you shouldn't have", or otherwise want to capture a lesson learned.

To install at user level:
```bash
cp feedback.md ~/.claude/commands/feedback.md
```
