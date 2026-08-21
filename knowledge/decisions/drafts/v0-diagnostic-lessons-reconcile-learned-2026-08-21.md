# lessons-forge — diagnostic: reconcile LESSONS.md against the forge corpus and design the queryable build queue
**Date:** 2026-08-21 | **Tier:** Medium | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (read-only diagnostic) | **Execution:** Step 1 (READ-ONLY DIAGNOSTIC) | **Priority:** 1

**auto_close:** false
**pause_for_verdict:** after_step_1

## The objective (CEO, 2026-08-21) — QUERYABILITY, not size

> *"I want to be able to query LESSONS.md and know exactly what needs implementation. I don't care about the number of entries."*
> *"Lessons/procedures stored in memory should be added into LESSONS.md as an item to build — the goal being to not rely on memory for proper system execution."*

⚠️ **This supersedes an earlier framing that optimized for SHRINKAGE.** Size was a proxy; the real requirement is that a grep answers *what still needs building*. That changes the design in three ways, all favourable:
- **Annotate, do not delete.** Marking an entry `implemented` is additive and reversible; a wrong mark costs a re-check, whereas a wrong DELETE destroys the record. Retirement to a `learned_lessons` log becomes OPTIONAL housekeeping rather than the point.
- **The detector's precision bar drops accordingly** (see Q2) — it now gates a label, not a deletion.
- **`LESSONS.md` becomes the SINGLE build queue**, absorbing memory's un-built items so that no operational knowledge lives in recall.

### The unified queue (Planner-computed 2026-08-21 — RE-VERIFY)

| source | count | disposition |
|---|---:|---|
| `LESSONS.md` pending | **63** | stays, marked `pending` |
| `LESSONS.md` never ingested | **7** | triage, then marked |
| migrated from memory (CODE 48 + DOCTRINE 39 + per-repo 16) | **103** | added as build items |
| **= TOTAL NEEDING BUILD** | **173** | the answer a query must return |
| `LESSONS.md` already implemented | 250 | marked `learned` |
| memory history | 15 | dropped |
| memory project status | 14 | to the baton |

**Operational content remaining in memory afterwards: 0.**

## Context — the finding that reframes the whole effort

**CEO principle:** a lesson is finished when the system enforces it and the note becomes redundant. `LESSONS.md` is a staging QUEUE, not a log; its size is a debt metric.

**Measured 2026-08-21 — the pipeline exists and half-works.** `lessons-forge/lessons-forge.db` already carries `lesson_entries` (370, all sourced from `LESSONS.md`, 2026-04-14 → 2026-08-19) and `lesson_proposals` (378) with `target_layer`, `target_artifact`, `route`, `status`, `duplicate_of`. **Routing was mechanized. The SHRINK step never was.**

| measure | value |
|---|---|
| entries currently in `LESSONS.md` | **320** |
| matched to the forge by normalized heading | **313 (98%)** |
| **in-file AND already `implemented`** | **250** |
| in-file, proposals but none implemented (the REAL queue) | **63** |
| in-file, never ingested | **7** |
| entries in the DB but no longer in the file | ~50 (removal HAS precedent) |

**⇒ `LESSONS.md` should be ~70 entries. A 78% shrink, available now, on work already done.**

**The second finding — the pipeline routes to DOCS, not to the system.** `target_artifact`: `PLANNER_TEMPLATE.md` 204, `DRAFTING_CYCLE.md` 101, and **7 total to code** (`bellows.py` 3, `walk_register_lint.py` 2, `plan_lint.py` 1, `runner.py` 1). `target_layer` is 334 `governance` / 20 `structure` — **there is no CODE, glossary, CLAUDE.md or DELETE rung in the taxonomy.** That is why `PLANNER_TEMPLATE.md` is 420 KB and `DRAFTING_CYCLE.md` 129 KB: lessons have been faithfully converted into more prose. Shrinking `LESSONS.md` without fixing this just moves the bytes.

## The `learned_lessons` design question (CEO-directed artifact)

The log is to record what was implemented, so the queue can shed it. ⚠️ **`lesson_entries.raw_content` ALREADY stores the full text of all 370 entries** — so removing an entry from `LESSONS.md` loses nothing today. The log is therefore mostly a VIEW over data already held.

**Planner recommendation (argue it, do not assume it):** make `learned_lessons` a TABLE/VIEW in the forge DB — `entry_id`, `heading`, `entry_date`, `target_artifact`, `implemented_at`, `proposal_id`, `verification_evidence` — plus an on-demand report generator. ⚠️ **Do NOT create a `LEARNED_LESSONS.md` holding all 250 entries**: at ~480 KB that recreates the exact problem in a new file. If a browsable artifact is wanted, generate it on request rather than maintaining it.

## Drafting Cycle
**Tier:** T1 — triggers COMPUTED against §1, not asserted: **T-7 FIRES** (a later executable builds the schema, the migration and the batch plans on these findings without re-verification). T-6 does NOT fire: this plan is read-only and edits no doctrine, gate, template or contract — though its OUTPUT rewires both, so the DOWNSTREAM executables inherit T-6 and are T2. T-1/T-2/T-5 do not fire (read-only, no data mutation, nothing to revert). T-8 does not fire: this is a structural clone of `Done/diagnostic-495.md`. ⇒ **T1: full five-lens walk, no cold panel required.**
**Walk 0 (context pin) — REAL (2026-08-21):**
1. Newest same-class: `bellows/knowledge/decisions/Done/diagnostic-495.md` — read-only diagnostic designing a downstream change. Clone-diffed for form (single READ-ONLY step, `pause_for_verdict: after_step_1`, `auto_close: false`, findings doc into `knowledge/research/`). **Deliberate divergence:** 495's inputs were all inside its target repo; BOTH of this plan's inputs are outside the worktree, which is why the read/write path rules are stated explicitly.
2. ⚠️ **Target-project pin — the plan was MOVED during walk 1.** It was drafted under `bellows/knowledge/decisions/drafts/` while every deposit path targets `lessons-forge`. Deposit location determines `plans.target_project` and therefore the worktree, so the deposits would have resolved outside the agent's tree. Now staged under `lessons-forge/knowledge/decisions/drafts/`. `lessons-forge` is a watched project (verified in `bellows/config.json`).
3. Live pins (agent RE-VERIFIES): `lessons-forge.db` is UNTRACKED and gitignored (`git ls-files --error-unmatch` fails; `check-ignore` matches) → absent from any worktree. `LESSONS.md` is in the governance ROOT repo, not lessons-forge. `lessons-forge/knowledge/research/` exists. No un-run cycle plan in `lessons-forge/knowledge/decisions/` → the LESSONS.md append gate is CLEAR.
4. Corpus counts are Planner-measured (320 / 313 / 250 / 63 / 7) and are PREDICTIONS for the agent to reproduce, not facts to inherit.
- Cold scout (T1, §2.0): Planner's call — **not run**. The defect is already reproduced from live data rather than predicted, and the open questions are the agent's job.

**Walk 1 — warm lens-by-lens, folds applied:**
- Weak spots (1.4):   w1 2 folded — instruction 2 (W1 the plan was staged in the WRONG REPO — deposit dir determines target project, so its lessons-forge deposits would have resolved outside the bellows worktree; moved. W2 the corpus DB is UNTRACKED by shop policy, so the system of record for 370 lessons has no diff, no revert and no git recovery — surfaced, plus a new **Q6b** asking whether the DB is a system of record or a derived index, because the answer decides whether Q3b's annotations must live in the FILE rather than the DB).
- Destruction (2.4):  w1 1 folded — instruction 1 (D1 **both primary inputs are unreachable from the worktree** — the DB is gitignored so it does not exist there, and `LESSONS.md` is in a different repository. A relative DB name would CREATE an empty file and every query would return a confident, empty, WRONG answer. Absolute reads mandated, plus a resolve-check with byte counts before any analysis, and an explicit STOP rather than regenerating a missing corpus).
- Vulnerabilities:    w1 1 folded — instruction 1 (V1 the write path INVERTS the read path: reads must be absolute because the inputs live outside the worktree, but the DEPOSIT must be written relative to cwd INSIDE it — and writing to the main checkout instead passes both `deposit_exists` and `scope_check` silently while the teardown-merge never picks the file up).
- Integration-record: w1 1 folded — instruction 0 / record 1 (I1 the plan's own account of itself was stale: the v0 authoring notes said walk 0 and the tier computation were "not done" while walk 0 was in fact producing the two ship-blockers above → this block).

- ACID (alone, on the four-lens-folded draft): w1 1 folded — instruction 1 (A1 lens 1's own fold created an ordering defect: the new **Q6b** decides whether the corpus is a system of record or a derived index, which GATES both Q3b's schema and Q4's `learned_lessons` design — but it sits AFTER them in document order, so an agent answering top-to-bottom would bake in the assumption Q6b exists to test. Explicit ANSWER ORDER added, declared authoritative over document order).
**Walk 1 STATUS:** 6 folded — instruction 5 / record 1 — NOT dry. Two were ship-blockers found before a lens ran (wrong repo; both inputs unreachable from the worktree), and one was damage created by this walk's own first fold.

**Walk 2 — lens-by-lens over the whole artifact:**
- Weak spots (1.4):   w2 2 folded — instruction 2 (W2-1 Q1 asked the agent to REPRODUCE five counts without stating the method precisely enough — a differing number would have been unattributable between a data difference and a method difference; the exact regex, normalization and the 313-both-ways result are now given, with `content_hash` named as the stronger key that OVERRIDES the Planner if it disagrees. W2-2 the hand-verification sample of 30 was an inherited guess with no power reasoning; the agent must now state the precision it needs, size the sample to measure it, and report a confidence interval).
- Destruction (2.4):  w2 dry — the write surface is one file; reads are read-only by absolute path; the DB is opened `mode=ro`; MUST-PRESERVE already forbids creating `learned_lessons` in this plan. The expensive half of Q2 (hand verification) is already sampled, and the automated half runs in code over 370 rows, so there is no runaway cost path.
- Vulnerabilities:    w2 dry — verified rather than assumed that the deposit's parent survives worktree dispatch: `git ls-files knowledge/research` returns 21 tracked files, so the directory EXISTS in the worktree and no `mkdir` is owed (the omission that cost a step earlier today). ⚠️ Noted and accepted: `knowledge/research/agent-prompt-feedback.md` is the shared append file that collides when sibling plans run concurrently — no concurrent lessons-forge plan is queued, so the risk is not live.
- Integration-record: w2 dry — the unified-queue table (63 + 7 + 103 = 173) reconciles with the reconciliation table (320 / 313 / 250 / 63 / 7) and with the memory audit's routing (CODE 48 + DOCTRINE 39 + per-repo 16 = 103); the ANSWER ORDER line agrees with the Q6b-gates-Q3b/Q4 dependency it was written to enforce.
- ACID (alone, on the four-lens-folded draft): w2 dry — walk 2's two folds both tighten Q1/Q2's measurement contract and touch no other question, no probe, and no path rule; nothing from walk 1 is re-opened.
**Walk 2 STATUS:** 2 folded — instruction 2 / record 0 — NOT dry. Yield 6 → 2, and both folds are measurement-contract items rather than defects in the plan's substance.

**Walk 3 — closing walk, lens-by-lens over the whole artifact:**
- Weak spots (1.4):   w3 1 folded — instruction 1 (W3-1 ⚠️ the plan carried its own v0 SCAFFOLDING — a title prefixed `⚠️ v0 DRAFT`, a banner reading **"NOT cycled, NOT deposit-ready"**, and an authoring-notes section labelled "delete before deposit". Deposited unchanged, the dispatched agent would have read an instruction that its own plan must not be run. Scaffolding stripped and the title restated; the record of what the cycle did remains in this block, which is where it belongs).
- Destruction (2.4):  w3 dry — stripping the scaffolding removed only self-referential prose; no instruction, path, question, deposit or MUST-PRESERVE clause was touched (verified by re-reading the step and gate sections after the cut, per the subtractive-cut discipline).
- Vulnerabilities:    w3 dry — gate surface re-verified MECHANICALLY after the cut rather than by eye: `plan_lint` exit 0, one `## STEP`, Scope ≡ Deposits at 1/1, the single deposit unconditional, `pause_for_verdict: after_step_1` recognized.
- Integration-record: w3 dry — with the scaffolding gone the plan's account of itself is now consistent: the Drafting Cycle block records three walks and a computed tier, and nothing in the file still claims the plan is un-cycled.
- ACID (alone, on the four-lens-folded draft): w3 dry — the sole fold is subtractive and self-referential; it re-opens no earlier fold and changes no probe, count or ordering rule.
**Walk 3 STATUS:** 1 folded — instruction 1 / record 0 — NOT dry. Yield 6 → 2 → 1.

**Walk 4 — closing walk, lens-by-lens over the whole artifact:**
- Weak spots (1.4):   w4 dry — every question now carries its own failure mode: Q1 the exact matching method with `content_hash` as the overriding key, Q2 a justified sample and a stated precision bar, Q3b a parser-compatibility check, Q6b the gate on Q3b/Q4, and Q4 an explicit instruction to ARGUE the table-vs-file recommendation rather than inherit it.
- Destruction (2.4):  w4 dry — write surface is one file inside the worktree; both reads are absolute and read-only (`LESSONS.md` 611,049 bytes and the corpus DB 1,593,344 bytes both re-verified to resolve at this moment); MUST-PRESERVE forbids creating `learned_lessons` (token verified present) and forbids deleting any lesson.
- Vulnerabilities:    w4 dry — gate surface verified MECHANICALLY, not by eye: `plan_lint` exit 0, `## STEP` count 1, Scope ≡ Deposits 1/1 and set-equal, the deposit path absolute and unconditional, `pause_for_verdict: after_step_1` in the recognized set, and the ANSWER ORDER clause present.
- Integration-record: w4 dry — the yield series in the STATUS lines (6 → 2 → 1 → 0) matches the per-lens records; the two surviving `v0` mentions sit inside walk records as fold provenance, not as instructions, and the title and banner no longer contradict the plan's deposit-readiness.
- ACID (alone, on the four-lens-folded draft): w4 dry — no fold re-opens another; the one cross-question dependency (Q6b gates Q3b and Q4) is stated from both ends, in the ANSWER ORDER clause and in Q6b itself.
**Walk 4 STATUS:** 0 folded — instruction 0 / record 0 — **DRY**. Yield 6 → 2 → 1 → 0; the last event before deposit is a dry pass and the final walk carries zero INSTRUCTION-class findings (§2 bar met on the class test).

## MUST-PRESERVE

- **READ-ONLY.** This plan proposes and measures. It does not delete a single line of `LESSONS.md`, does not write to the forge DB, and does not create `learned_lessons`. Those are a later, reviewable executable.
- ⚠️⚠️ **`status='implemented'` IS A MARKER, AND THIS SESSION PROVED MARKERS UNRELIABLE.** The memory audit found `SHIPPED`/`FIXED`/`COMPLETE` to be exactly the class that lies. **No entry may be marked `learned` on the strength of its status alone** — the label requires evidence that the target artifact actually contains the rule, cited `file:line`. Anything undecidable is marked `unknown`. And since the objective is queryability rather than size, **prefer marking over deleting in every case**: a deletion that turns out wrong cannot be queried back.
- Do not append to `LESSONS.md` while a lessons-forge cycle plan is un-run (checked 2026-08-21: only `halted-executable-425`, so clear — RE-VERIFY).
- DB reads only via `file:<abs>?mode=ro`, ABSOLUTE path (`/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`) — ⚠️ a bare relative DB name CREATES an empty file, and sibling `forge.db`/`lessons.db` are 0-byte decoys that return confident FALSE absences.
- ⚠️⚠️ **THE CORPUS IS UNTRACKED.** `lessons-forge.db` is local operational state, deliberately untracked since 2026-06-12 (`lessons-forge/CLAUDE.md:33`). So the system of record for 370 lessons has **no diff, no revert, and no git recovery** — the same T-5 exposure the wrap-hook layer had before it was vendored. This plan is read-only and so is safe; **the follow-on executable that creates `learned_lessons` would mutate an unversioned file, and must address backup/versioning before it does.** Surface this as a fork rather than designing around it.

## STEP 1 — READ-ONLY DIAGNOSTIC

**Role:** DEV (read-only audit). Contract: `/Users/marklehn/Developer/GitHub/READONLY_AUDIT_CONTRACT.md`.

⚠️⚠️ **BOTH OF THIS PLAN'S PRIMARY INPUTS ARE OUTSIDE YOUR WORKTREE — verified 2026-08-21. Read them by ABSOLUTE path and never by a relative one.**
- **`lessons-forge.db` is untracked AND gitignored**, so it does NOT exist in `.bellows-worktrees/<id>/`. Read it at `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro`. ⚠️ A relative name would CREATE a new empty database and every query would return a confident, empty, WRONG answer — and sibling `forge.db`/`lessons.db` are 0-byte decoys with the same property.
- **`LESSONS.md` is in the governance ROOT repo** (`/Users/marklehn/Developer/GitHub/LESSONS.md`), a DIFFERENT repository from your target project. It is not in your worktree either.
- Your worktree is for your DEPOSIT only. Everything you read comes from the main checkouts by absolute path. **Before answering anything, verify both inputs resolve: `ls -la` each and report the byte counts.** If either is missing, STOP — do not proceed with a partial corpus, and do not "helpfully" regenerate one.

⚠️ **ANSWER ORDER — Q1 → Q2 → Q3 → Q6b → Q3b → Q4 → Q5 → Q6 → Q7 → Q8.** The questions are LETTERED for reference, not sequenced for execution. **Q6b (is the DB a system of record or a derived index?) GATES both Q3b and Q4**: if the corpus is recoverable by re-ingesting `LESSONS.md`, the annotations belong in the FILE and the DB is a convenience; if the DB holds state the file cannot reconstruct, the schema decision inverts. Answering Q3b first would bake in an assumption Q6b exists to test. Report in the numbered order, but ANSWER in this one, and say so.

**Q1 — Reproduce the reconciliation.** Independently re-derive the 320 / 313 / 250 / 63 / 7 figures above. Report your own numbers; if they differ, yours supersede. **The Planner's method, stated precisely so a difference in your numbers means a difference in the DATA and not in the method:** parse `LESSONS.md` headings with `^## (\d{4}-\d{2}-\d{2}): (.+?)$`; take `source_heading` from `lesson_entries`; normalize BOTH sides by stripping `\[tag:[^\]]*\]`, collapsing whitespace to single spaces, trimming, and lowercasing; match on the normalized string. Exact-heading matching gave 313/320 and normalization gave the same 313 — so the 7 misses are genuinely absent, not formatting artifacts. ⚠️ **Evaluate `content_hash` as a stronger key** and report whether it agrees; if it disagrees, the hash is authoritative and the Planner's count is wrong. Report the failure modes of whichever key you adopt.

**Q2 — BUILD AND MEASURE THE RETIREMENT DETECTOR. This is the load-bearing question.** For an entry marked `implemented`, decide whether the target artifact REALLY contains the rule. Propose the check, run it over all 250, and report how many PASS, FAIL, and are UNDECIDABLE. Then hand-verify a random sample by reading both the lesson and its target, and report the detector's PRECISION against that sample. ⚠️ **Choose and JUSTIFY the sample size** — the figure 30 was a Planner guess with no power reasoning behind it. State the precision you need in order to trust the label (the bar is lower than it would be for deletion, since a wrong label is recoverable), then size the sample to measure it, and report the confidence interval rather than a bare percentage. ⚠️ Because the detector now sets a LABEL rather than authorizing a deletion, a moderate precision is workable — but it must still be MEASURED and stated, and entries it cannot decide must be marked `unknown`, never silently `learned`. A query that returns a confidently wrong build list is worse than one that admits uncertainty.

**Q3 — What happened to the ~50 already-removed entries?** They were ingested but are no longer in the file. Determine whether removal was deliberate (precedent to follow) or accidental (a data-loss event to understand). Cite git history.

**Q3b — DESIGN THE QUERYABLE ENTRY SCHEMA. This is now the primary deliverable.** Propose the machine-readable fields every `LESSONS.md` entry carries so a grep answers "what needs implementation" exactly — at minimum a state (`pending` / `learned` / `unknown`) and a target (the artifact that would enforce it). Entries today carry `[tag: ...]`; propose whether to extend that convention or add a distinct line, and show the EXACT query for each of: what needs building, what needs building in `plan_lint.py`, what was learned and where it landed. ⚠️ Verify the format survives the forge's ingest parser — a schema that breaks ingestion trades one problem for another. Show the parser path you checked.

**Q3c — Plan the memory migration (103 items).** The memory index carries 103 un-built operational items (CODE 48, DOCTRINE 39, per-repo 16) that must become `LESSONS.md` build entries so nothing operational depends on recall. Propose the transform: how a memory file becomes an entry, what date it carries (observed vs migrated), how its existing `[[wiki-links]]` are preserved or rewritten, and how to avoid double-entry where a memory and a lesson already describe the same rule — ⚠️ measure that overlap rather than assuming it is zero. Routing per item is in `governance/knowledge/research/memory-to-system-audit-2026-08-21.md`; treat it as a STARTING POINT to verify, not as truth.

**Q4 — Design `learned_lessons` (now OPTIONAL — argue whether it is needed at all).** Propose the schema, its population query, and the retirement protocol: what must be true before an entry moves. Argue the table-vs-file question above rather than inheriting the recommendation. State how a reader answers "why is this lesson gone?" a year from now.

**Q5 — Characterize the 63 that remain.** These are the genuine queue. Group them by what would enforce them, using the extended ladder (CODE / glossary / CLAUDE.md / DOCTRINE / BACKLOG / DELETE). This is the input to the batch plans.

**Q6 — Fix the taxonomy.** `target_layer` has no CODE, glossary, CLAUDE.md or DELETE rung. Propose the extension and the migration for the 378 existing proposals. ⚠️ Of the 305 routed to `PLANNER_TEMPLATE.md`/`DRAFTING_CYCLE.md`, estimate how many should have been CODE — that number is the ongoing leak, and it matters more than the one-time shrink.

**Q6b — The corpus has no version control. Is that tenable?** `lessons-forge.db` is untracked by shop policy. Weigh: is the corpus recoverable by re-ingesting `LESSONS.md` (in which case the file is the record and the DB is a derived index — and the annotations in Q3b must live in the FILE, not only the DB), or does the DB hold state the file cannot reconstruct (proposal status, routing, `duplicate_of`) — in which case it is a system of record with no backup? ⚠️ This determines whether Q3b's schema is the primary artifact or a convenience. Answer it before the `learned_lessons` design is finalized.

**Q7 — The 7 un-ingested entries.** Why did ingestion miss them? Is the ingest path lossy, and does that undermine the corpus as a system of record?

**Q8 — Sequence it.** Propose the executables that follow, in order, with what each retires.

**Findings document:** Q1–Q8 with command output or `file:line` per answer. Close with `## What could not be measured` (empty is legitimate, MISSING is not), `## Open forks`, and `## Recommended executables`.

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/lessons-reconcile-learned-2026-08-21.md`

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/lessons-reconcile-learned-2026-08-21.md`

**Commit:** ⚠️ **WORKTREE DISCIPLINE — the absolute path in Scope/Deposits names the file by IDENTITY, not by the checkout you write to.** You are dispatched into `lessons-forge/.bellows-worktrees/<id>/` and your cwd is that worktree. **Write your findings file at the SAME relative path under YOUR cwd** (`knowledge/research/lessons-reconcile-learned-2026-08-21.md`) and commit it there, in the repo-asserting form: `git -C <your-worktree> add knowledge/research/<file> && git -C <your-worktree> commit -m "..."`. ⚠️ Do NOT write to `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/` directly — that is the MAIN checkout, outside your worktree, and `gates._resolve_deposit_path` falls back to "path as-is" while `_check_deposit_uncommitted` swallows the out-of-worktree git error, so writing to the wrong checkout passes both gates SILENTLY and the daemon's teardown-merge never picks your file up. ⚠️ This is the one place the absolute-path rule INVERTS: absolute for everything you READ (both inputs live outside the worktree), relative-to-cwd for the one thing you WRITE. Your final operation is the commit.
