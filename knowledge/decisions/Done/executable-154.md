# Lessons Forge — Classifier dedup against recently-implemented proposals (surface for review)
**Date:** 2026-07-09 | **Tier:** Medium | **Dispatch Mode:** bellows | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always | **Test Scope:** both

## CEO Context

**Gate 2 carried thread (b), flagged in the v4.71 changelog and the lessons-forge baton: "dedup candidates against recently-implemented proposals, not just live template text — Gate 2 caught 2 already-covered proposals (131/135) only via manual git blame."**

**The gap (demonstrated):** In the 2026-07-06 cycle, proposals **131** (entry 123) and **135** (entry 127) were **fully subsumed** — their `suggested_action` was already live in PLANNER_TEMPLATE (131 ≈ the Guardrails recurring-bug bullet added 2026-06-07; 135 ≈ Checklist #22 added 2026-06-11 — both the *immediately prior* cycles). The automated `detect_duplicates` (`src/lessons_forge.py:253`) **missed both**: it matches new entries only against reference-file (PLANNER_TEMPLATE) **text** via tag overlap + `source_heading` substring, and never consults the forge's own proposal history. The misses were caught only because the classifier agent **manually ran `git blame`** during Gate 2.

**CEO decision 2026-07-09: SURFACE overlaps for review (not mechanical auto-dedup).** Because the 131/135 misses were *semantic* (same substance, different framing), a mechanical auto-dedup risks both misses and false positives. Instead, automate the *surfacing* the human did by hand: for each candidate entry, compute an overlap report against **recently-implemented** proposals and render it into the Gate-1 review artifact so the reviewer/classifier sees potential subsumption without manual git-blame. **The dedup is ADVISORY ONLY — it MUST NOT change any proposal status or insert any proposal.**

**Data available:** `lesson_proposals` has 97 `implemented` rows with `suggested_action`, `reasoning`, `category`, `target_artifact`, and `status_updated_at` (recency) — everything needed.

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-classifier-recently-implemented-dedup-2026-07-09.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible chat message confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer. Read `agents/FORGE_LESSONS_AGENT.md` first for domain context (skip with a note if absent). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Scope:**
> - `src/lessons_forge.py`
> - `src/test_lessons_forge.py`
>
> **Locked contract:**
> - **Advisory-only.** The new dedup MUST NOT mutate proposal `status`, MUST NOT insert any proposal (including `category='duplicate'`), and MUST NOT write to the DB at all. It only READS and produces overlap data for surfacing. (This is the CEO's "surface for review, not auto-dedup" decision — do not extend `detect_duplicates`'s insert path.)
> - **Recall-oriented.** Tune the match to err toward surfacing (a false surface costs a reviewer one glance; a miss costs a wasted Gate-2 cycle). The known 131/135 case MUST be caught by your validation (Task D).
>
> **Task A — new detection function.** Add `detect_recently_implemented_overlaps(conn, entry_ids, recency_days=45)` (mirror the shape/docstring style of `detect_duplicates` at line 253). For each `entry_id`: read the entry (`source_heading`, `tags`) from `lesson_entries`; query `lesson_proposals WHERE status='implemented' AND status_updated_at >= date('now', '-' || ? || ' days')`; for each such implemented proposal, compute an overlap score between the entry (tags + keywords from `source_heading`) and the proposal (keywords from `suggested_action` + `reasoning`, plus `category` and `target_artifact`). Surface a match when overlap crosses a low, recall-oriented threshold (you choose the exact heuristic — e.g. normalized keyword/tag Jaccard over a small floor, boosted when `category`/`target_artifact` align). Return a list of dicts: `{"entry_id": int, "proposal_id": int, "implemented_at": str, "overlap_reason": str}` (empty list when `entry_ids` empty or no matches). Default `recency_days=45` covers ~2 cycles (131/135 were ~25–30 days out); make it a parameter.
>
> **Task B — wire into the pipeline (read-only).** In `run_pipeline` (~line 380–462), after the duplicate-detection block, call `detect_recently_implemented_overlaps(conn, candidate_ids)` and add the result to the returned dict under a new key `recently_implemented_overlaps` (a list). Do NOT insert proposals from it. Keep `detect_duplicates`/duplicate-insertion behavior unchanged.
>
> **Task C — render in the review artifact.** In `generate_lessons_report` (~line 467), for each rendered proposal whose `entry_id` has one or more recently-implemented overlaps, append an advisory line under that proposal, e.g. `- ⚠️ **Recently-implemented overlap:** proposal #{proposal_id} (implemented {implemented_at}) — {overlap_reason} — verify not already subsumed before codifying.` Compute the overlaps inside `generate_lessons_report` (call `detect_recently_implemented_overlaps` for the entries it renders) so the report is self-contained. Proposals with no overlap render exactly as before (no empty line, no regression).
>
> **Task D — validation against the known miss (dev-log, read-only).** Run `detect_recently_implemented_overlaps` against the LIVE `lessons-forge.db` for entries **123** (proposal 131) and **127** (proposal 135) with a recency window wide enough to include the 2026-06-07 / 2026-06-11 implementations relative to the 2026-07-06 cycle, and record in the dev-log whether the known subsuming implemented proposals are surfaced (catch = success). If NOT caught, tune the heuristic until they are, then re-run. This is a one-off validation (live-DB dependent) — document it in the dev-log; do NOT commit it as a test.
>
> **Tests (`src/test_lessons_forge.py`).** Add unit tests using a synthetic in-memory/temp DB (do NOT depend on the live DB): (1) an entry whose tags/heading overlap a RECENTLY-implemented proposal is surfaced; (2) the same entry vs an OLD implemented proposal (status_updated_at outside `recency_days`) is NOT surfaced; (3) a non-overlapping entry is NOT surfaced; (4) **advisory-only guard** — calling the function makes ZERO changes to `lesson_proposals` (assert row count + statuses unchanged before/after); (5) `generate_lessons_report` renders the overlap advisory line when an overlap exists and renders unchanged when none. Mirror one test on the 131/135 shape (synthetic entry + synthetic recently-implemented proposal with word-for-word overlapping suggested_action).
>
> **Self-verify.** Run the FULL suite `python3 -m pytest src/ -v` (use `python3 -m pytest`, NOT the `timeout` binary — unavailable on macOS). Read the tail to an explicit pass/fail; confirm 0 regressions (the existing `detect_duplicates`/pipeline tests must stay green). **Commit** with a descriptive message, e.g. `feat(forge): surface recently-implemented-proposal overlaps in classifier review (advisory)`.
>
> **Deposit:** a dev-log with the detection design + chosen heuristic/threshold, the Task D live-validation result (131/135 caught: yes/no + evidence), the full-suite tail, commit hash, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback` (daemon-owned; do NOT edit any feedback file directly).
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifier-recently-implemented-dedup-2026-07-09.md`
> - `lessons-forge/src/lessons_forge.py`
> - `lessons-forge/src/test_lessons_forge.py`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — QA

---

> **FIRST — post a short visible chat message confirming you are starting Step 2 (QA) and your immediate next action.** Do NOT rename the plan file.
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` for domain context if useful (skip with a note if absent). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **Verification + reporting only — no product-code changes.** If you find a blocker, STOP and report it.
>
> **Scope:**
> - `knowledge/qa/classifier-recently-implemented-dedup-qa-2026-07-09.md`
>
> **Verify:**
> 1. **Advisory-only contract (critical):** confirm `detect_recently_implemented_overlaps` performs NO DB writes and `run_pipeline` does NOT insert proposals or change statuses from its output — by reading the code AND confirming test #4 (row-count/status unchanged) exists and passes.
> 2. **Recency window:** overlaps against RECENTLY-implemented proposals are surfaced; against OLD ones (outside `recency_days`) are not — confirm tests #1/#2 cover both.
> 3. **Known-miss catch:** read the Step-1 dev-log Task-D validation and confirm the 131/135 (entries 123/127) subsuming implemented proposals are surfaced by the live-DB validation.
> 4. **Report rendering + no regression:** `generate_lessons_report` shows the advisory line when an overlap exists and is byte-identical to before when none (test #5); existing `detect_duplicates`/pipeline/report tests still green.
> 5. **Full suite** `python3 -m pytest src/ -v` (`python3 -m pytest`, NOT `timeout`): record exact pass/fail counts, confirm 0 regressions vs pre-plan baseline. Apply mechanical Rule 20 / Rule 22 gates.
>
> **MANDATORY — Rule 20 self-check banner.** Your QA deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`.
>
> **Deposit:** `lessons-forge/knowledge/qa/classifier-recently-implemented-dedup-qa-2026-07-09.md` — per-item verdict (PASS/FAIL + evidence), the full-suite tail with counts, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback` (daemon-owned). Update `lessons-forge/PROJECT_STATUS.md`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/classifier-recently-implemented-dedup-qa-2026-07-09.md`
>
> **STOP. Wait for CEO verdict.**
