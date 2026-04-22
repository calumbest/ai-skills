# Feedback Skill

*Source: `/Users/crichards/.claude/commands/feedback.md`*

## Your job

The user is reporting something that went wrong in a recent interaction. Do this:

1. **Read the recent conversation carefully** — understand exactly what happened
2. **Diagnose the root cause** — don't just accept the user's framing at face value
3. **Generate concrete, specific recommendations** — across all relevant fix categories
4. **Let the user approve each one** — implement only what's confirmed

## Root cause categories

Evaluate all of these before deciding which apply:

**Memory gap** — Claude didn't recall something it should have (a preference, setup detail, or lesson already learned). Fix: write or update a memory file in the project's `memory/` directory or user memory.

**Missing/wrong instructions** — The behavior follows from absent or contradictory instructions in a CLAUDE.md file. Fix: propose specific edits to the relevant CLAUDE.md (project or user level).

**Skill or command gap** — A slash command is missing, incomplete, or steers Claude incorrectly. Fix: propose edits to the relevant skill/command file, or propose creating a new one.

**MCP tool misuse** — Claude used an MCP tool incorrectly: wrong parameters, hallucinated tool name, misread a result, or used a tool that doesn't support the intended operation. Fix: document the correct pattern in memory or instructions.

**Inaccurate Bash/terminal pattern** — Claude used a wrong command, flag, path convention, or chained commands in a way that broke. Fix: document the correct pattern in memory or CLAUDE.md.

**User expectation mismatch** — The output was actually correct and the user's expectation or recollection may be off. Flag this diplomatically — don't just agree to be agreeable. Explain why you think the output was defensible.

## Output format

Start with a 2-3 sentence diagnosis: what went wrong and which root cause(s) apply.

Then list recommendations, ranked by impact (most likely to prevent recurrence first):

> **[N] [Type]: [Short title]**
> What: [Exactly what to change or add — be specific enough to act on]
> Why: [Why this prevents the error from recurring]
> Approve? (yes / skip)

Cap at 3-5 recommendations. Vague recommendations ("be more careful") are not acceptable — every recommendation must be a concrete, implementable change.

After the user responds, implement all approved items immediately: write memory files, edit skill/command files, update CLAUDE.md as needed. Report what was changed.

## Tone

- Be honest if the user might be wrong — sycophantic agreement is a disservice
- Be specific — name the exact file, tool, command, or pattern involved
- Be concise — this is a diagnostic, not a postmortem essay
