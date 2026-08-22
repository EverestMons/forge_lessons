# lessons-forge — ingest: normalize the heading KEY so annotating LESSONS.md cannot duplicate corpus rows
**Date:** 2026-08-21 | **Tier:** Small–Medium | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** targeted (DEV) → full suite + ingest canary (QA) | **Execution:** Step 1 (DEV) → Step 2 (QA) | **Priority:** 1 | **qa_steps:** 2 | **Depends on:** Done/diagnostic-498 (identified the defect)

**auto_close:** false
**pause_for_verdict:** always

## Context

Diagnostic-498 designed a queryable schema for `LESSONS.md`: each entry gains `[status: pending|learned|unknown]` and `[target: <artifact>]` markers on its heading line, so a `grep` answers *what still needs building*. It also found the blocker: **the ingest upsert keys on `(source_file, source_heading)`, so adding a marker CHANGES THE KEY** — the lookup misses and a duplicate row is inserted instead of the existing one being matched. Annotating all 320 entries would silently double the corpus.

**⚠️ THE DIAGNOSTIC CITED ONE SITE. THERE ARE THREE** (Planner-verified 2026-08-21, `src/lessons_forge.py` — note the `src/` prefix, which 498's findings omitted):
1. **`:141-142`** — ingest lookup `WHERE source_file = ? AND source_heading = ?`, and the INSERT at `:149-151` that stores the heading.
2. **`:470-471`** — a SECOND heading-keyed lookup in the pipeline's duplicate-check step, collecting `candidate_ids`. Missed by 498. A fix applied only to site 1 leaves this one mismatching, so every annotated entry silently drops out of duplicate detection.
3. **`:375-378`** — `source_heading` is split on the em-dash to derive `heading_title`, which feeds the proposal-matching substring test at `:308`. Markers would land inside the derived title and corrupt matching.

**⚠️ MEASURED NEGATIVE — the stale-marking branch is NOT a concern, do not "fix" it.** `content_hash` is computed over `raw_content`, and the parser assigns `current_heading` from the match and then starts `current_body_lines = []` (`:106-112`) — so **raw_content is BODY-ONLY and excludes the heading line** (confirmed against live rows, which begin `**Source:** ...`). Annotating a heading therefore does NOT flip the hash, does NOT take the "changed" branch, and does NOT mark the 250 implemented proposals stale. Leave `_normalize_for_hash` alone.

**Recovery exists:** `knowledge/research/corpus-snapshot-2026-08-21.sql` is a verified-restorable snapshot (370 entries / 378 proposals / 284 CEO decisions) taken 2026-08-21.

## MUST-PRESERVE

- ⚠️ **NEVER write to the live corpus DB** (`/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`). It is UNTRACKED, it is the sole system of record for 378 proposals and 284 CEO routing decisions, and this plan does not need to touch it. All ingest exercises run against a `cp`-made scratch copy by absolute path.
- ⚠️ **Do not modify `LESSONS.md`.** Annotating it is a LATER plan; this one only makes annotation safe. Canary inputs are scratch copies.
- Existing rows carry `[tag: ...]` markers inside `source_heading`. **The normalizer must strip ONLY `[status: ...]` and `[target: ...]` and must leave `[tag: ...]` intact** — stripping tags would fail to match all 370 existing rows and would re-create the very defect being fixed.
- Do not change `_normalize_for_hash` or the hash semantics (see the measured negative above).

## Drafting Cycle
**Tier:** T1 — triggers computed: **T-2 FIRES** (the ingest path writes the corpus DB, and a wrong key duplicates rows in production data). T-5 does NOT fire — the code is tracked and a verified corpus snapshot exists. T-6 no (not governance code), T-8 no (a targeted key-normalization fix, not a novel pattern), T-7 no. ⇒ T1: full five-lens walk, no cold panel.
**Walk 0 (context pin) — REAL (2026-08-21):**
1. Newest same-class: no recent lessons-forge code plan; nearest is the 2026-07-16 `backfill_normalized_hashes` script, which solved the sibling problem (hash instability) by normalizing before comparison — the same shape as this fix, applied to the other key.
2. Pre-edit pins (agent RE-VERIFIES): three call sites as listed; `_EM_DASH_SEP` used at `:375`; `src/test_lessons_forge.py` exists as the test home.
3. All 370 existing `source_heading` values contain NO `[status:`/`[target:` markers, so the normalizer is the identity function on today's data — the migration is a no-op and existing rows keep matching.

**Walk 1 — warm lens-by-lens, folds applied:**
- Weak spots (1.4):   w1 1 folded — instruction 1 (W1 **`source_file` is a KEY, not a path** (`:121`, default `"LESSONS.md"`): the canary said "run the ingest against the copied DB" without pinning it, and passing the copy's filesystem path would make EVERY row miss — `inserted` 320 instead of 0 — failing the canary on correct code. Now pinned to the literal, with the parse entry point `parse_lessons_md` named).
- Destruction (2.4):  w1 1 folded — instruction 1 (D1 `src/test_lessons_forge.py` carries **28** `source_heading` references, several asserting the stored value round-trips (`:339-340`) or comparing parsed headings (`:229`/`:233`/`:256`). Canonicalizing what the INSERT stores can legitimately break them, so forced updates are expected and each diff must be verified as ONLY the forced change — with an explicit STOP if a test breaks for any other reason. This is the split-pair `scope_check` class caught earlier today, applied before it fires).
- Vulnerabilities:    w1 1 folded — instruction 1 (V1 the canary's scratch DB and annotated `LESSONS.md` copies had no location constraint; inside the worktree they become unnamed changed files that trip `scope_check` on a clean step, and a 1.6 MB binary could reach a commit → scratch goes to the step's tmp dir, outside the repo).
- Integration-record: w1 dry — Scope ≡ Deposits per step (2/2, 3/3), the QA step's Deposits block carries a literal `.txt`, the Rule 20 banner pair is present verbatim, and the three call sites in the Context match the three in Step 1. `plan_lint` exit 0 / 8 PASS / 0 FAIL on the first authoring pass.
- ACID (alone, on the four-lens-folded draft): w1 dry — the three folds are independent (a key-semantics pin, a test-breakage expectation, a scratch-location rule); none touches another's probe, and none re-opens the walk-0 finding that the normalizer is the identity on all 370 existing rows.
**Walk 1 STATUS:** 3 folded — instruction 3 / record 0 — NOT dry. All three would have produced a false failure or a gate trip on otherwise-correct execution.

## STEP 1 — DEV: normalize the heading key at all three sites

**Role:** DEV. ⚠️ You run in a worktree (`lessons-forge/.bellows-worktrees/<id>/`) — edit and commit INSIDE it, using the same relative paths. The corpus DB is untracked and therefore ABSENT from your worktree; you do not need it, and you must not reach out to the live one.

1. Add a module-level helper beside `_normalize_for_hash`, e.g. `_key_heading(heading: str) -> str`: strip `\[status:[^\]]*\]` and `\[target:[^\]]*\]` (case-insensitive), collapse runs of whitespace to a single space, and `.strip()`. ⚠️ Do NOT strip `[tag: ...]`.
2. Apply it at **site 1** — both the `SELECT ... WHERE source_heading = ?` lookup (`:141-142`) AND the `INSERT` that stores the heading (`:149-151`), so the stored value is canonical and a later lookup matches.
3. Apply it at **site 2** (`:470-471`), the duplicate-check `candidate_ids` lookup.
4. Apply it at **site 3** (`:375-378`) so `heading_title` is derived from the canonical heading and the `:308` substring match is unaffected by markers.
5. ⚠️ Python version: this repo's other modules use `from __future__ import annotations` or plain annotations — match the file's existing style rather than introducing PEP 604 syntax; the shop's `/usr/bin/python3` is 3.9.6.
6. ⚠️ **EXPECT EXISTING TESTS TO NEED UPDATING, AND VERIFY EACH DIFF IS ONLY THE FORCED CHANGE.** `src/test_lessons_forge.py` references `source_heading` **28 times**, including assertions that read the stored value back (`:339-340` selects by it) and that compare parsed headings (`:229`, `:233`, `:256`). Canonicalizing what the INSERT stores can legitimately break such assertions. Update them — that is correct work, not scope creep — but confirm each changed line is ONLY the forced normalization, and quote the diff in your Receipt. ⚠️ If a test breaks for any OTHER reason, STOP: that is the fix changing behavior it should not touch. (The test file is named in Scope precisely so this does not trip `scope_check`.)
7. **New targeted tests** in `src/test_lessons_forge.py`: (a) ingesting an entry whose heading gained `[status: learned] [target: X]` MATCHES the pre-existing row and inserts NOTHING; (b) the same ingest reports `unchanged`, not `updated`, and marks NO proposal stale; (c) `[tag: ...]` markers survive normalization and still participate in matching; (d) a heading with markers still yields the correct `heading_title` at site 3; (e) the normalizer is the IDENTITY on a heading with no markers (the 370-row no-op guarantee). Use a scratch/in-memory DB.

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py`
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/test_lessons_forge.py`

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py`
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/test_lessons_forge.py`

**Commit:** repo-asserting absolute form against YOUR worktree, explicit pathspec, add before commit. Your final operation is the commit.

## STEP 2 — QA: full suite + the no-duplicate ingest canary

**Role:** QA.

**MANDATORY Rule 20 self-check banner** — the deposited QA report MUST contain, verbatim, the heading `## Rule 20 — QA Self-Check Results` and, below it, `**PASSED — SELF-CHECK PASSED**`. Canonical block: `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`. `plan_slug: ingest-heading-key-normalization-2026-08-21`; `qa_report_path: /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/ingest-heading-key-qa-2026-08-21.md`; `evidence_dir: /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-2026-08-21/`; `required_evidence_files: [pytest_full.txt, canary.txt]`. FAILED → halt.

0. `mkdir -p` the evidence directory before writing into it.
1. **Full suite**, foreground, raw output to `pytest_full.txt`; quote the counts line verbatim. Report failures by IDENTITY against any pre-existing baseline, not by count alone.
2. **No-duplicate ingest canary** — raw output to `canary.txt`. ⚠️ **Against a `cp` COPY of the live corpus DB, by absolute path, NEVER the original.** ⚠️ **Put every scratch artifact — the DB copy, the annotated `LESSONS.md` copy — in the step's TMP directory, OUTSIDE the repository and outside your worktree.** A `.db` or `.md` copy left inside the worktree becomes an unnamed changed/untracked file and trips `scope_check` on an otherwise clean step; it would also risk a 1.6 MB binary reaching a commit. Only the three declared deposits may appear in the repo. Steps: copy the DB and record its row counts; take a copy of `LESSONS.md`; annotate **3** of its headings with `[status: learned] [target: X]`; parse the copy with `parse_lessons_md(<abs path to the copy>)` and feed the result to `ingest_lesson_entries(conn_to_the_COPIED_db, entries, source_file="LESSONS.md")`.
   ⚠️⚠️ **`source_file` is a KEY, not a path** (`:121`, default `"LESSONS.md"`). The lookup is `WHERE source_file = ? AND source_heading = ?`, so if you pass the copy's filesystem path as `source_file`, EVERY row misses, `inserted` becomes 320, and the canary FAILS on correct code. Pass the literal `"LESSONS.md"` no matter where the copied file lives, and state in the report that you did. Assert ALL of:
   - `inserted == 0` — no duplicate rows created (this is the defect under test)
   - total `lesson_entries` count is UNCHANGED from the pre-run number
   - `stale_proposals_marked == 0` — the 250 implemented proposals are untouched
   - the 3 annotated entries still resolve to their ORIGINAL row ids
   - ⚠️ **A FAILING canary looks like:** `inserted == 3`, or a row-count increase, or any proposal marked stale. Report each assertion separately; a combined verdict is not acceptable.
3. Confirm the live corpus DB is byte-identical to before the step (`shasum -a 256` before and after, both pasted) — proof that MUST-PRESERVE held.

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/ingest-heading-key-qa-2026-08-21.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-2026-08-21/pytest_full.txt`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-2026-08-21/canary.txt`

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/ingest-heading-key-qa-2026-08-21.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-2026-08-21/pytest_full.txt`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-2026-08-21/canary.txt`

**Commit:** repo-asserting absolute form against YOUR worktree, explicit pathspec. Your final operation is the commit.
