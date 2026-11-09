---
name: vet
description: Independent fact-checking pass on any written product (memo, working doc, report, announcement with numbers in it, donor- or external-facing document) before it ships. Uses fresh-context verifier agents, a per-claim ledger with quoted evidence, and a fix-and-re-vet loop. Use when the user says /vet, "fact-check this", "vet this" or "is this accurate".
---

# /vet — Independent Vetting Pass on Any Written Product

> **What I use it for:** Anything with facts or figures I'll have to stand behind once it's sent - especially external- or donor-facing documents, and internal updates that a decision hangs on. Fresh agents check each claim against its source and quote what they found, so I only re-read the handful of claims that fail.

**Argument:** a file path (or several), a Google Doc link, or "the draft above", plus any context the user wants to add (destination, known-shaky figures, sources of truth). No argument → ask what to vet.

**Anchor principle:** when we send something, we stand behind it. Nothing ships until the Still-open list is empty or every remaining item is explicitly accepted by the owner.

**Cost asymmetry (the tiebreaker for every judgment call below):** the cost of a false positive is a minute of the user's review; the cost of a false dismissal is a wrong claim in a shipped document. When in doubt, retain the finding.

## Procedure

### 1. Build the vetting context block

Fill the context block below before spawning anything. Infer what you can from the target and the conversation; ask the user **at most one batched round** (multiple-choice where possible) for what you can't:

1. **Destination/stakes** → picks the tier: external or donor-facing → Tier 3; recurring internal product → Tier 2; working draft or quick check → Tier 1 plus a light single-verifier pass. Say which tier you picked and why; the user can override.
2. **Authoritative sources:** where should each class of claim in this document trace to?
3. **Suspicious items and declared-intentional choices:** which figures is the user least sure of; what's deliberate and shouldn't be flagged.

If the user keeps a vetting-pitfalls ledger (a file of false-positive patterns, false-negative patterns and severity calibrations from prior vets), read it first and apply every relevant entry.

> **Product:** [what it is, one line]
> **Destination / stakes:** [external / org-wide / team-internal / working draft] → determines tier
> **Authoritative sources:** [the specific docs, sheets and ranges that are the source of truth for this product's claims]
> **Declared-intentional choices:** [framings or figures the owner chose deliberately; do not flag as errors, but verify each actually appears as declared before accepting it]
> **Known sensitivities:** [names that must not appear, unreleased figures, banned terms]
> **Known failure modes for this product:** [from past vets or the pitfalls ledger]
> **Suspicious items:** [the specific figures or claims the caller is least sure of; open-ended "check the numbers" returns much less]

Every verification agent receives this block in its spawn context. A generic vetter is a weak vetter.

### 2. Run the protocol at the chosen tier

Per the protocol below: pre-scan → verifier(s) under the verifier contract → (Tier 3) reconcile, named deep checks and doc-coherence → severity per Nature × Materiality.

### 3. Write the findings doc

`docs/<target-name>-vetting.md` for repo files (or next to the target if it already lives in a project folder; for a chat draft, `docs/vetting/YYYY-MM-DD-<short-desc>-vetting.md`). Per-claim ledger with verdict, quote and location; Still-open list at top; coverage declaration at bottom. Never edit the target itself during the vet; findings are findings until the user or the fix step acts on them.

### 4. Report and loop

Return only the Blockers and Material findings in chat (Blockers first), each with its quote and one-line fix. Then:

- The user decides per item: fix / accept as is (record who accepted, dated) / needs more digging.
- Apply agreed fixes, then run the **fix → re-vet loop** (fresh agent, delta-scoped at Tier 2, full loop-until-clean at Tier 3).
- If a style pass follows, enforce the interlock: verify → style → delta re-verify.
- Close out: harvest calibration candidates and propose pitfalls-ledger entries for the user to vet.

The verdict on completion is binary and stated plainly: **CLEARED** (Still-open empty or every remaining item explicitly accepted) or **NOT CLEARED — [N] blockers**. No soft middle. Favor quality over token cost: don't thin the vet to save time unless the user asks.

# The protocol

## Tiers

Each tier includes everything below it. When in doubt, go up one.

| Tier | Name | When | What runs |
|---|---|---|---|
| 1 | Pre-scan | Any draft, always; it's nearly free | Deterministic pre-scan only |
| 2 | Standard | Recurring internal products | + one independent verifier agent, full claim ledger, delta re-verify loop |
| 3 | Full adversarial | Anything external; anything a decision hangs on | + adversarial A/B pair with reconcile, the named deep checks, doc-coherence gate, fix → re-vet loop until clean |

Something drafted casually that turns external gets re-run at Tier 3: tiers are per shipment, not per document.

## Tier 1 — Deterministic pre-scan

Run before any agent spawns (grep or regex over the deliverable and its supporting docs). Every hit is a finding to confirm or replace, never silently delete:

- **Placeholders:** `FILL_IN`, `TBD`, `TODO`, `placeholder`, `XXX`, `[INSERT`, `to update`, `check this`, `FIXME`
- **Author self-admissions:** `guess`, `made up`, `reverse-engineered`, `from google`, `chatgpt`, `AI summary`, `roughly right`, `I think this is`. Each flags a value needing a real source. (A *documented* "best guess" with a rationale is transparency, not a finding; the finding is an unsourced judgment call with no note at all.)
- **Sensitivities:** names and banned terms from the context block
- **Internal links:** Google Docs, Drive, Box or Slack links in anything public-bound; `/draft/` and `/staging/` URL segments
- **Broken markdown:** empty link targets, unresolved footnote refs

## The verifier contract (binds every verification agent, every tier)

1. **Independence.** Fresh context, no involvement in the build, told to *check independently, not confirm*. Give it the draft and the authoritative sources from the context block. Fresh context is the point: it can't inherit the builder's framing, shortcuts or mistakes.
2. **Evidence discipline: a quote is only a quote if it was actually read.** Every Verified or Contradicted verdict carries the verbatim sentence or cell from the source plus its clickable location. The verdict is still the agent's judgment and may be wrong; the quote is what lets the user check it in one glance. A "Verified" with no quote is downgraded to Could not verify.
3. **The four-part citation test**, for every cited source: **Exists** (a citation is present) → **Links** (it points at a real document) → **Functional** (the link resolves) → **Matches** (the source actually substantiates the claim: right org, right year, right metric, right population). A source that exists and resolves can still fail Matches. *Wrong source* is a different finding from *missing source*; for any dead link, search for the replacement before filing.
4. **Steelman before filing.** Before flagging a claim, write one sentence: what would someone who trusts this claim point to as their evidence? Then test it. Holds up partially → downgrade severity. Fails → file with confidence. Can't construct any defense at all → that itself is strong signal; file.
5. **Bidirectional.** Check for claims that are too *weak* as well as too strong. An understated claim misinforms the same way, and a hedged inference sometimes turns out to be a citable fact. A conservative-looking claim is not automatically correct.
6. **Not-found rules.** "I didn't find it" only establishes it wasn't where you looked. Spot-check any finding that claims a source doesn't exist before reporting it. Conversely, when the context block says a claim or element *should* exist and you can't find it, that absence **is** a finding.
7. **Resolve, don't report.** An apparent inconsistency between sources is a search trigger, not a finding: check the product's other tabs and sections, then a full-text search of the user's docs, before filing. If it still won't resolve, file it as a question with where you looked.
8. **Coverage declaration (mandatory; this is the silent-failure detector).** The agent ends with a structured declaration: which claims and sections it checked, counts per verdict, and what it skipped and why. **Skipped** = ran and found nothing applicable (reason required); **aborted** = errored or couldn't access. If key sources were unreachable, the agent ends `INCOMPLETE — [what it couldn't check]` rather than finishing quietly. **A verifier output with no coverage declaration is a failed run: re-spawn it; do not accept its findings.**
9. **Enumerate every instance of a universal claim.** Universal or quantified claims ("our invites", "all", "most", "three", "we've told X") get a per-instance table: one row per recipient or source, verbatim quote, verdict. The caller's source list is a starting point, not the boundary: search email, chat and meeting notes exhaustively for every instance and state the searches in the coverage declaration.

## Verdicts (one vocabulary, everywhere)

Per claim: **Verified** / **Partially verified** (state exactly which part isn't) / **Could not verify** (looked, couldn't confirm; NOT the same as contradicted) / **Contradicted** (source says otherwise; quote it) / **Needs owner input** (correctness depends on intent or a judgment call).

- Blank means *not assessed*, never "checked and fine". Every claim in the ledger gets an explicit verdict.
- **Partially verified** must list each clause of the claim with its own status, and the fix must correct *every* failing clause, not just the one the finding headlines.
- **Dismissing a finding requires affirmative evidence the claim is correct**, not just failure to confirm it's wrong. "Seems fine in context" and "couldn't reproduce the issue" do not qualify. When intent is the open question, the verdict is Needs owner input, not dismissal.

## Severity

Classify each finding by **Nature × Materiality**, then read off severity:

- **Nature:** *Defect* (objectively wrong) / *Gap* (something required is absent: a source, a caveat, a disclosed choice) / *Judgment* (defensible choice you'd question).
- **Materiality:** *Decision-changing* (a reader would act differently) / *Material* (changes a headline claim or figure) / *Cosmetic*.
- **Severity:** Blocker = any decision-changing item; any Defect or Gap of unknown materiality (**unknown rounds up**). Material = Defect or Gap that's material; Judgment that's decision-changing. Minor = the rest, grouped (one finding per category per document, not one per instance).
- **Bright lines:** a confirmed Defect is never Minor while its impact is unknown. A finding whose explanation hedges ("may", "possibly", "appears to") cannot be a Blocker: confirm it or downgrade it. Blockers block shipping regardless of how well documented the error is.

Finding format: what's wrong / what the correct value or claim is / why it matters. Standalone-readable, 2–3 sentences, with the fix as one imperative sentence containing the exact replacement text or value.

## Tier 3 — Adversarial pair and reconcile

1. **Spawn two independent verifiers, fresh contexts, neither told the other exists.** Same draft, same sources, opposite priors: **A** reads top-down and assumes the document *overstates* (hunt for claims stronger than their sources); **B** works bottom-up from the sources and assumes it *understates or misassembles* (rebuild each claim from the source and compare, prioritizing sections where a claim "looks fine", since that's where a reasonable reviewer rationalizes).
2. **Reconcile** (fresh agent or the orchestrator, re-opening sources itself). A finding caught by only one instance is a *potential miss by the other*, not a resolved disagreement: every divergence gets investigated by re-reading the source. Four determinations: **Retain** / **Dismiss** (three conditions: source re-read this session; the strongest pro-claim argument written and tested; affirmative evidence of correctness found) / **Needs owner input** / **Retain-downgraded** (state why). On severity disagreement, err high.
3. **Synthesis guard.** Never combine two verifiers' partial observations into one confident claim. If a merged finding contains "both instances" or "combining these suggests", downgrade it and label it "Synthesized from partial observations — owner to confirm." A false High built from two partial signals makes the reader distrust the real findings next to it.

## Named deep checks (Tier 3; default on for anything quantitative)

- **Suspicion-first pass** (separate agent, no checklist): read the product holistically and name the 3–5 claims that would most change the conclusion if wrong. State each as a falsifiable claim ("I suspect X because [observation]; this is a real error if [condition]"), then verify. File only confirmed. Things that look suspiciously clean may have been forced to fit rather than derived.
- **Independent re-derivation:** recompute every headline number from the document's own cited leaf inputs, refusing its intermediates. Tolerance: <2% off → nothing; 2–5% → Material; ≥5% → Blocker. Locate the break by finding the first intermediate where your value diverges. Where the method is ambiguous, compute both plausible readings and note both.
- **Sensitivity-ranked interrogation:** rank the document's claims by how much the conclusion changes if each is wrong; **pre-declare the top 5 and the ranking rationale**; give those the deepest verification (fetch the source, read past the snippet or abstract, check cohort, metric and comparison arm). This allocates paranoia on top of the exhaustive ledger; it doesn't replace coverage.
- **Doc-coherence gate:** build an explicit claim map between the deliverable and *every* supporting doc (methods notes, sources lists, READMEs, reconciliation docs), **including NO-MATCH entries in both directions** so orphaned claims surface on either side. Agreement doesn't clear the check (both docs can share the same stale number; verify against the live source). When two presentations legitimately differ (different denominators, different cuts), the finding is the *undocumented inconsistency*, not the choice. State which doc is authoritative.

## The fix → re-vet loop (Tier 3; Tier 2 runs the delta version)

A completed verification covers the draft *as it was, not as it becomes*. After fixes land:

1. A **fresh** agent confirms each fix landed as specified, checks it didn't break an adjacent claim or introduce a new error, and re-verifies all prose that changed. A fix that hides the symptom rather than correcting the claim is itself a Blocker.
2. Re-run the doc-coherence gate: fixes to the deliverable are exactly when supporting docs drift.
3. **Loop until a pass returns clean.** One pass after fixes is often not enough; second passes regularly catch new wording errors introduced by the first round of fixes.
4. Findings log: keep a Still-open list at top; resolve items by annotating RESOLVED (owner and date), never delete them; record decisions with the decider named and dated.

**Tier 2 delta version:** re-run the verifier scoped to everything added or edited since the last pass, and **append** to the same findings doc.

## Writing-style interlock

The style pass never runs last. Sequence: **verify → style → delta re-verify** (scoped to the style diff). The delta pass targets quantifiers and absolutes ("all", "always", "every", "a few", "the three highest", "most recent"), since that is what style edits touch and what post-fix passes keep catching.

## Findings output

Before applying or relaying fixes, read every Partially verified and Contradicted ledger row (not only the Findings list) and confirm each failing clause has a fix. **Before offering to send or save a draft**, re-verify every line changed since the last pass, whoever changed it, by opening the source yourself, not by relaying an agent's report.

Universal requirements: per-claim rows with verdict, quote and clickable location; a Still-open list at top; Blockers returned to the user in chat (only ❌/🔴; they don't need to re-read the ✅ rows); the coverage declaration preserved at the bottom.

## Calibration (how this protocol improves)

After any substantial vet, harvest calibration: false positives the user rejected, misses they caught themselves, severity they re-ranked. Propose entries for the pitfalls ledger and let the user vet them. Observation isn't theory: don't propose causal rules off one incident's evidence, and record rejected rules as anti-lessons so they aren't re-derived. A wrong calibration is worse than none because it gets applied silently for weeks.
