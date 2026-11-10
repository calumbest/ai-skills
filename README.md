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

Each skill opens with a short note on what I use it for. They're written for my setup, so check the references to tools, folders and connectors before you rely on them.

### `/memo` — [memo.md](memo.md)

Drafts a memo or working doc in your voice, outline first. It asks who it's for and how heavy it should be, proposes an outline for you to cut, then drafts and iterates in a markdown file. It can also start from a short interview or a meeting transcript.

### `/vet` — [vet.md](vet.md)

Fact-checks a written product before it ships. Fresh-context agents check every claim against its source and quote what they found; higher tiers add an adversarial pair of verifiers, independent re-derivation of headline numbers, and a fix-and-re-vet loop that runs until a pass comes back clean.

### `/expenses` — [expenses.md](expenses.md)

Cleans up Ramp card spend: finds missing memos, receipts and coding, searches every linked inbox (via Superhuman) for receipts and queues forward drafts, and applies plain-English bulk edits. A second mode logs a personally paid productivity benefit to a Google Sheet and fills in the monthly claim form. Needs the Ramp MCP, the Superhuman connector, Claude in Chrome and the `gws` CLI, plus a short profile file of your Ramp coding (see the skill's Setup section). Bundles [`scripts/email_text.py`](scripts/email_text.py) for reading large receipt emails.

### `/constellation-meetings` — [constellation-meetings.md](constellation-meetings.md)

For people who work from Constellation. Books a room in Robin for each of the day's meetings (a call booth by default, a bigger room for group lunches), then deletes the duplicate calendar events Robin creates and notes the room in the real meeting's description. Needs Claude in Chrome logged in to Robin and Google Calendar access (the `gws` CLI or a connector); Slack search is optional.

### `/feedback` — [feedback.md](feedback.md)

Processes feedback about a bad or wrong Claude output. Invoke it when Claude got something wrong and you want to prevent the mistake from recurring.

What it does:
- Reads the recent conversation to understand what went wrong
- Diagnoses the root cause (memory gap, wrong instructions, skill gap, tool misuse, etc.)
- Proposes ranked, concrete fixes (lessons or memory writes, CLAUDE.md edits, skill updates)
- Implements only what you approve

## Installing

To install at user level:
```bash
cp memo.md vet.md expenses.md constellation-meetings.md feedback.md ~/.claude/commands/
```
