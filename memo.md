---
name: memo
description: Draft a memo or working doc in the user's voice through an outline-first, iterative process. Use for concept docs, recommendations, summaries of where thinking landed, discussion guides, or a memo built from a meeting transcript.
---

# /memo — Outline-First Memo Drafting

> **What I use it for:** Most of the memos and working docs I write start here - recommendations for my manager, write-ups of where a conversation landed, and memos built straight from a meeting transcript. The outline-first step is the main point: it stops Claude from writing three pages I'd mostly delete.

**Context:** $ARGUMENTS

## What this is

This skill is about the *process* for getting from idea to finished memo, usually in the user's own first-person voice and usually for a specific reader. Prose-level style belongs in a separate writing style guide if the user keeps one (check CLAUDE.md for its location); this is the workflow around it. It's meant to develop over time.

## Core principles

- **Outline first, always.** Before writing a full draft, propose a short outline (the sections, a one-line intent for each, and rough depth) and ask which to skip, cut, or treat lightly. The user can tell you in ten seconds what's not worth your effort; an outline saves you from over-producing sections they'll just delete.
- **Calibrate weight and ownership up front.** Who's the reader, who owns it, how heavy should it be? A light memo for one person should *read* light. Don't default to a formal white-paper register.
- **Don't over-produce, especially in the user's voice.** Comprehensive, authoritative-sounding detail in domains the user can't personally vouch for (current legal or regulatory specifics, vetted-looking lists of real people, draft outreach emails) reads as a liability, not value. Either flag uncertainty plainly ("Legal stuff: I don't know much here") or keep deep or unverified research as a clearly labeled separate section or artifact. Never weave it into their first-person voice as if they vouch for it.
- **Lead with a summary that stands alone.** The top should pass the "one page for a busy reader" test: the take, the core idea, the main risk, and the ask, readable without the rest. For a rough working doc, a good top is a one-line plain "What is this?" (descriptive, not a narration of the doc) followed by a "Bottom line" that states the take in a few bullets.
- **Readability and scannability are the goal, especially for rough working docs.** Cut anything that describes the doc rather than being it, say each idea once, use bullets for anything that's a list of facts, merge overlapping sections rather than running parallel ones, don't number headers by default, and match formatting weight to the doc's stakes (plain bold labels beat big headings for a rough doc).
- **State a take; argue pragmatically.** Give a recommendation, not a neutral survey. Prefer the pragmatic case over "this fits our values" justifications.
- **Push asides into footnotes** to keep the main line clean.
- **Match the ask to how far the thinking got.** If the source reached decisions, state them plainly. If it only reached leanings, describe where things landed and close with one feedback ask ("I'd appreciate your reactions before I start on X"), not a numbered list of decisions for the reader to adjudicate. A decision list signals the thinking is further along than it is.
- **One author.** The memo is in the user's "I", even when it summarizes a two-person conversation. Credit the other person's distinct points by name ("Sam suggested two criteria…") and keep "we" for genuinely joint views. Address a known reader as "you".
- **List any sensitive cuts.** If you omit or soften anything (personnel matters, need-to-know material, pointed criticism), say exactly what and why alongside the draft, so nothing disappears silently. If the source is clearly sensitive, ask how to handle it in the step 1 questions.

## Steps

**Everything lives in a markdown file, opened for the user.** From the first outline on, write the memo's working file to `docs/<short-slug>.md` and open it (`open <file>` on macOS); never print the outline, questions or draft only to chat. Step 1's questions go at the top of that file with the step 2 outline, under a "Questions" heading; later rounds update the same file and reopen it. Chat gets a one-line pointer to the file plus anything that needs attention outside it.

### 1. Clarify weight, reader, ownership, and type

Confirm who the memo is for, whether it's in the user's first-person voice, how heavy it should be, and what kind of memo it is: a **proposal** (recommends a decision; lead with it), a **summary** (captures where thinking landed; order for flow, rarely has next steps) or a **discussion guide** (structures a meeting; session goals up front). Ask only what isn't obvious, in one batched round.

In the same round, decide whether an interview is needed (step 1a). Offer it when the user arrives with only a rough idea; skip it when they bring a transcript, notes, or a clear take.

### 1a. Interview (optional)

Get the content out of the user's head before outlining.

1. Ask for the 30-second version: the topic and what's on their mind, unorganized. Don't ask clarifying questions yet.
2. From the dump, find the core question, the angles they covered, the angles a good memo would need that they didn't, and any implicit assumptions. Ask **4–6 numbered questions**, ordered easiest to most stretching, spread across different angles, with at least one that challenges an assumption or surfaces a tradeoff. Tell them to skip any that don't help.
3. If a critical angle is still thin after their answers, ask **one** follow-up. Otherwise move on. If they want to skip straight to drafting, do that.

Treat the whole exchange as the source material for the outline.

### 1b. From a meeting (transcript mode)

When the source is a meeting (e.g. a Granola or other meeting-notes recording), pull the full transcript, not just the AI summary, when owners, wording or where things landed matter. Then:

- **Synthesize, don't transcribe.** State where things ended up and the main reasons, not who said what in order. Coin short labels for recurring ideas and reuse them.
- **Next steps and open questions only if discussed.** Include them only when the conversation actually raised them. Never infer or invent them.
- Let the user update facts that have moved since the meeting, and link related docs inline; never invent developments yourself.

### 2. Propose an outline

Lay out the sections with a one-line intent and rough depth for each. Explicitly ask: which to skip, cut, go light on, or go deep on? Flag any section that would need research or claims the user may not want to own, and ask whether to do it at all or keep it separate and clearly labeled as unvetted. Wait for their steer before drafting.

### 3. Load writing context

Read the user's writing style guide if they have one. For broad research you can fan out subagents, but keep their output clearly separated from the user's voice until they've vetted it.

### 4. Draft to the agreed outline

Write only what the outline approved. Lead with a self-contained summary. Footnotes for asides. Flag uncertainty plainly rather than padding with confident filler.

**Concision pass (required before presenting).** Reread the draft asking: can this be simpler, and what can move further down? Cut what the reader doesn't need, push detail into footnotes, and move long catalogs (brainstormed options, candidate lists, menus of projects) into a linked appendix so the body carries only what needs the reader's attention. Then do a style pass against the style guide.

### 5. Iterate

Update the file with the draft, reopen it, and expect concision edits. The user may edit the file directly: reread it before each round and keep their changes. Take the cuts and don't re-inflate.

### 6. Capture learnings

After the memo settles, offer to fold prose-level patterns into the style guide and process learnings back into this skill.
