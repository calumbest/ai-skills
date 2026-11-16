---
name: editor
description: Edit a piece the user wrote (blog post, essay, memo) by leaving comments and tracked-change suggestions on its Google Doc, in rounds - argument first, then line edits, then polish on request. Never changes the text directly. Use for /editor, "edit my post", or "give me comments on this doc".
---

# /editor — Edit Your Writing in a Google Doc

> **What I use it for:** Blog posts and memos I've drafted myself and want a real editor on. It reads the whole piece, tells me whether the argument holds together before it touches a sentence, then leaves comments and tracked changes in the Google Doc for me to accept or reject. The writing stays mine.

Edit a piece the user wrote by leaving comments and tracked-change suggestions on the Google Doc for them to engage with. The piece stays theirs: the editor never changes the text directly.

**Argument:** a Google Doc link, plus optionally a round: `argument`, `line` or `polish`. With no round, look in the records folder for this doc (see Mechanics) and run the next one (no record means `argument`). If the piece is in a local file or a notes app, move it into a Doc first, because the back-and-forth happens in Docs.

## Setup

- **Reading the Doc and its comments:** any Google Docs and Drive access works (the `gws` CLI or a connector). Read footnotes and existing comments too.
- **Comments:** posted through the Drive comments API, anchored to quoted text.
- **Tracked changes:** need a way to write suggestions to a Doc. The Docs API's suggestion mode is a Developer Preview at the time of writing, so most setups won't have it. Without it, run every round with comments only: quote the passage and give the proposed wording in the comment.
- **Records:** pick a folder for per-doc records (the examples below use `tracking/editor/<doc-id>/`).

## What I want from an edit

The things I care most about, in order:

1. **Internal coherence.** Am I saying contradictory things? Does the argument hold together when it's laid out simply? Do I understand what I'm saying, and is the steelman version of my argument good?
2. **Transparency and plainness.** Is the argument legible to a reader? My models are Luke Muehlhauser's Reasoning Transparency and GiveWell's house style.
3. **No obtuse language or bad metaphors**, as in Orwell's "Politics and the English Language".
4. **Concision.**

Spend the hardest thinking on the hardest problems, and raise structural issues first, because fixing one of those can make a dozen small comments moot. Change this list to fit what you care about.

## How a good editor works

These come from professional editing practice. They are the reasons behind the procedure below, so use them to judge cases the procedure doesn't cover.

- **The piece is the author's.** The job is to help them say what they mean to the reader they have chosen, not to produce the piece Claude would have written. A style guide for their work writing is not a standard to enforce on their posts.
- **Biggest problems first.** Editors work from structure inward (developmental, then line, then copy), because sentence polish is wasted on a passage that gets cut or rebuilt. This is why the rounds are separate.
- **Diagnose before prescribing.** Say what goes wrong for the reader and why it matters, then offer a way out. A fix with no diagnosis teaches nothing and is hard to argue with. A diagnosis with no fix leaves the author the work.
- **The lightest change that solves it.** Keep their words wherever they work. Prefer cutting to rewriting, and rewriting a clause to rewriting a sentence.
- **Never make it wrong.** An edit that changes the meaning or adds an error is worse than no edit. When it's unclear what they mean, ask. Don't guess and rewrite.
- **Good queries are easy to answer.** One issue per comment. Write about the text and the reader, not about the author ("a reader could take this two ways", not "you're being unclear"). The best query can be answered with a yes or a short fact, and offers wording they could accept. Before posting, check the comment needs raising at all and that it would sound fine said to their face.
- **Say what works.** Name the strongest parts so they survive revision.

## Round 1: argument

No sentence-level edits in this round, however tempting. The output is a small number of comments and a short summary.

1. **Read everything**, footnotes and existing comments included. Work out who the piece is for and what it's meant to do to them. The author usually says; ask only if the text doesn't.
2. **Lay the argument out simply.** Write the thesis in one sentence, then the steps that get there as a numbered list in plain words that are not the author's phrasing. Mark each step as stated, implied or missing, and note what support the text gives it. If this is hard to do, that difficulty is the first finding.
3. **Get a cold read.** Spawn one fresh agent with only the text and ask it for: the thesis in a sentence, the main steps, who it's for, where it got lost, and what it would object to. Give it none of your own analysis. Where its account differs from yours, a real reader's will too.
4. **Test coherence.**
   - Contradictions: two passages that can't both be true, or a caveat that takes back the claim it qualifies. Quote both.
   - Shifting terms: a key word that means one thing early and another later.
   - Steps that don't follow, and claims the conclusion depends on that the text never supports.
   - Overreach: a conclusion or recap that claims more than the body established.
   - Analogies and examples: does the comparison hold at the point where the argument leans on it?
   - Gestures: a phrase standing where a specific claim should be. Ask "what exactly is being claimed here?" If the text can't answer, ask the author.
   - The strongest objection a sceptical member of the target audience would raise, and whether the piece meets it.
5. **Steelman it.** Write the strongest version of the argument in a short paragraph. Then say where the draft is weaker than that version (a missing step, weak support used where stronger exists, a concession that gives away too much) and where even the strongest version has a problem. Say the second kind plainly.
6. **Check reasoning transparency**, scaled to the genre. A blog post doesn't need a research report's apparatus. The test is whether a reader could answer "how should I update on this?"
   - Does the reader learn early what the claim is and where the piece is going?
   - Is it clear which considerations carry the conclusion and which are secondary?
   - For each major claim, can the reader tell how confident the author is and what kind of support they have: their own experience, a number of conversations, expert opinion they can or can't assess, a simple argument, an intuition? Where they can't give their reasoning, do they say so?
   - Do caveats sit next to the claims they qualify? Tell calibration ("seems likely, I haven't checked") from hedging that only protects the writer.
7. **Check structure.** Order of sections, sections that don't serve the thesis, material in a footnote that the argument depends on (move it up), body material that is an aside (move it down or cut), the opening and the ending, length in proportion to importance.
8. **Choose what to raise.** Post about five comments, seven at most: the ones that would most change the piece, or that would make many smaller issues disappear. Put everything else in the records folder's `notes.md` for later rounds.
9. **Report in chat**, briefly:
   - The argument as you read it (thesis and steps). If the author says "that's not what I meant", that is the most useful result of the round.
   - The steelman, and where the draft falls short of it.
   - The issues you raised, most important first, each in a line.
   - What's working.
   - Roughly what you held back for round 2.

## Round 2: line

Run this after the author has reworked the piece or told you to go ahead. Re-read the whole doc fresh, since it has changed.

1. **Answer the round 1 threads first.** Read the replies, reply in the thread where they asked something, and drop any point they have decided against. Skip passages still under structural discussion.
2. **Edit for plain language.** Orwell's tests, applied to each sentence that feels off:
   - Stale figures of speech: a metaphor or simile seen in print many times. Either say the thing literally or find an image the author would actually picture. Mixed metaphors show the writer wasn't picturing anything.
   - Padding verbs and phrases: "make contact with", "give rise to", "with respect to", "the fact that", "in terms of". Use the single verb or preposition.
   - Inflated words: a long or Latinate word where a short one says the same.
   - Words that point at nothing: abstractions and insider terms the target reader couldn't define, and words used so loosely they could mean several things.
   - Passives that hide who did it.
   - Ready-made phrases that arrived whole. They often cover a thought that hasn't been worked out, so ask what the author means before rewording.
   - Orwell's last rule applies to all of these: break any of them sooner than write something stiff. A plain sentence in the author's voice beats a correct one in nobody's.
3. **Edit for concision.** Words that can go without loss, a sentence that repeats the one before, a point made twice in different sections, throat-clearing before the point, stacked hedges, a footnote that isn't worth the reader's detour.
4. **Edit for sentence-level transparency.** Vague quantities where the author knows the number, claims missing a confidence word, "people say" where they could say who.
5. **Edit for consistency and correctness.** One name per thing, consistent capitalisation and spelling, typos, grammar, broken links.
6. **Keep to clear wins.** Leave taste-level and marginal edits for round 3.

How to post line edits:
- A cut, a simpler word or a typo goes in as a bare tracked change (or, with comments only, a comment that quotes the passage and gives the new wording).
- Add an explanation only when the author would otherwise wonder why, or when the edit might shift their meaning.
- If an edit would change what they're claiming, don't suggest it. Comment and ask.

## Round 3: polish

Only when asked. Taste-level word choices, rhythm, marginal cuts, headings and title, formatting, a final proofread. Say in the chat summary that these are matters of taste, so the author can reject freely.

## The author's voice

A casual register in a personal post is usually deliberate: abbreviations, exclamation marks, emoji, stretched words. Leave it alone by default. Comment only where the register undercuts the point: a joke or shrug attached to a claim the reader needs to take seriously, intensifiers piling up in one sentence, or an aside that could put off the reader the piece is trying to persuade. Never quietly normalise it.

## Mechanics

- **Posting:** plan the comments and suggestions first, then post comments before suggestions and anchor them to text no suggestion touches. End every comment with a marker such as `— via Claude`, so the author can tell them from a human's. Never assign a comment to anyone.
- **Known limits of suggestions:** don't suggest edits to the title paragraph (comment instead). Keep match strings clear of footnote markers. Raise a footnote problem in a comment anchored to the body sentence that carries the footnote, quoting the footnote text. Bullets can't be created by a suggestion.
- **When to post without showing the author first:** running `/editor` on a doc is the go-ahead for comments and tracked changes when the doc is theirs and shared with nobody else (check the doc's permissions). If others can see the doc, or someone else owns it, show the comments and edits in chat first.
- **Records:** save each round's planned edits as `round-N.json` in the records folder, and keep `notes.md` there with the argument outline and the issues held back. These are what let a later round see what was accepted and rejected.
- **Not a fact-check.** Flag a claim that needs a source or looks wrong, but verifying claims is a separate job (see `/vet`).

## Learning the author's taste

At the start of a later round, compare the last round's record with the doc: which suggestions were accepted, which rejected, what was said in threads. Don't re-raise what was rejected. When a pattern shows up (they keep rejecting a kind of edit, or keep accepting one), ask one concrete question about it before writing it down as a lesson, and read those lessons at the start of every run.

## Sources

- Luke Muehlhauser, [Reasoning Transparency](https://coefficientgiving.org/research/reasoning-transparency/)
- George Orwell, [Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/)
- ACES, [Author queries for the nonfiction editor](https://aceseditors.org/news/2021/author-queries-for-the-nonfiction-editor-how-to-raise-em-and-how-to-phrase-em) and [The 3 essential elements of author queries](https://aceseditors.org/news/2019/the-3-essential-elements-of-author-queries)
- Bay Area Editors' Forum, [Querying the Author Effectively](https://www.editorsforum.org/forum_index_articles/editing_01_16_01.php)
