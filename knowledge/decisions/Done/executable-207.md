# Lessons Forge — Retire the plan-154 recently-implemented-overlap advisory
**Date:** 2026-07-16 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

## CEO Context

**CEO decision 2026-07-16: RETIRE the plan-154 advisory.** This removes `detect_recently_implemented_overlaps`, its helper, its two call sites, its report rendering, and its tests. This is a deliberate un-shipping of a feature that shipped 2026-07-09 — not a bug fix.

**Why retire rather than narrow — the evidence.** Plan 154 (Done 2026-07-09) added an advisory to surface candidate proposals subsumed by recently-implemented ones. Cycle 2026-07-16 (plan 205) was its **first and only production run**. It failed on both sides of the ledger:

- **False positives:** 353 overlaps DB-wide; 14 advisory lines across 3 proposals (~4.7 each). **4 of 4 hits examined at Gate 1 were false positives, 0 true positives.** It flagged the *same two* proposals (127/128) against *both* entries 139 and 140 purely on shared `planner-discipline` tag equality — 127 is about mandatory QA callouts, 128 about full-suite runs; neither relates to disk-verification or `qa_steps` semantics.
- **It also MISSES the true candidate.** Proposal 139 (entry 131, tagged `planner-discipline`, `implemented` 2026-07-07 — well inside the 45-day window) is the nearest genuinely adjacent implemented proposal to entry 140's `qa_steps` lesson. The advisory does **not** surface it. So it is not merely noisy — **it is anti-correlated with relevance**, which is worse than silence: an advisory firing ~5x per proposal on tag equality trains reviewers to skip warnings, and this one would train them to skip the warning that mattered.
- **Its justification has dissolved.** Plan 154's motivating case — proposal 131 being a subsumed duplicate — is now known to be a **downstream symptom of the whitespace-hash bug fixed by plan 204**. The bug manufactured duplicates by staling the prior cycle's last entry; plan 154 automated *coping* with those duplicates. With the generator fixed at the root (plan 204, verified: work list is now exactly the genuine new entries), the machinery has no remaining job.

**This is a clean excision — Planner-verified surface area (2026-07-16, read-only):** `_tokenize_for_overlap` (`src/lessons_forge.py:431`) is called **only** from within `detect_recently_implemented_overlaps` (`:437-551`); both go. Two call sites: `run_full_lessons_cycle` (`:636`, plus the `recently_implemented_overlaps` return key at `:648`) and `generate_lessons_report` (`:688` + the rendering at `:735`). **No consumer outside `src/`** — grep confirms nothing else in the repo calls `run_full_lessons_cycle` or `generate_lessons_report` programmatically, and the halted plan 203 (the only plan text that read the return key) is **fully superseded by the closed plan 205**, so removing the key strands nothing live.

**Do NOT regenerate `reports/lessons-report-2026-07-16.md`.** It carries 14 advisory lines and it is the **historical Gate 1 artifact for a Gate that already closed** (plan 206, 2026-07-16). Rewriting it would falsify the record of what the CEO actually reviewed. Leave it exactly as-is. Same for the historical prose references in `PROJECT_STATUS.md` and `knowledge/qa/classifier-recently-implemented-dedup-qa-2026-07-09.md` — those are the record of plan 154 having existed; do not scrub them.

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-retire-154-advisory-2026-07-16.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer. Read `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` first (cross-repo; skip with a note if absent). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **This step changes CODE ONLY. It MUST NOT touch the canonical DB** (`/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`) — no reads that mutate, no cycle runs, no report regeneration. Tests use synthetic in-memory/temp DBs only.
>
> **Scope:**
> - `src/lessons_forge.py`
> - `src/test_lessons_forge.py`
> - `knowledge/development/retire-154-advisory-2026-07-16.md`
>
> **Task A — remove the advisory.** Delete, from `src/lessons_forge.py`:
> - `detect_recently_implemented_overlaps` (~`:437-551`) and its helper `_tokenize_for_overlap` (~`:431`). **Verify before deleting** that `_tokenize_for_overlap` has no other caller (Planner's grep says it does not — confirm, do not assume). Remove any constants that become orphaned with them (e.g. an overlap threshold / stopword set), but ONLY if they have no other consumer.
> - The call + return key in `run_full_lessons_cycle` (~`:636`, `:648`). **All other return keys stay exactly as they are** (`ingested_count`, `updated_count`, `unchanged_count`, `duplicates_marked_count`, `needs_classification`, `terminal_proposals_flagged`, `cycle_timestamp`). `terminal_proposals_flagged` is plan 204's guard output — **do not touch it.**
> - The call + advisory rendering in `generate_lessons_report` (~`:688`, `:735`). Proposals must render exactly as they did before plan 154 — no advisory line, no stray blank line where it used to be.
>
> **Leave `detect_duplicates` completely alone.** It is the separate, older reference-file duplicate detector (`:253`) and is NOT part of plan 154. Confirm in your dev-log that it and its tests are untouched.
>
> **Task B — remove the tests.** Delete the 7 plan-154 tests from `src/test_lessons_forge.py`: `test_overlap_recent_match`, `test_overlap_old_not_surfaced`, `test_overlap_non_overlapping`, `test_overlap_advisory_only_no_writes`, `test_report_renders_overlap_advisory`, `test_report_no_overlap_unchanged`, `test_overlap_131_135_shape`.
>
> **Before deleting `test_report_no_overlap_unchanged`, check what it actually asserts.** If it is the only test covering "a report renders correctly for a proposal with no advisory" (i.e. baseline report rendering, not advisory behaviour), then that coverage must NOT be lost with it — confirm an existing report test still covers plain rendering, or keep an equivalent assertion under a non-advisory name. Report which you did and why in the dev-log. **Do not silently drop report-rendering coverage.**
>
> **Task C — prove nothing dangles.** Grep `src/` for `detect_recently_implemented_overlaps`, `recently_implemented_overlaps`, `_tokenize_for_overlap`, and `Recently-implemented overlap` — all must return **zero hits in `src/`**. Historical references in `PROJECT_STATUS.md`, `knowledge/`, and `reports/` are the record and **must remain** — do not scrub them.
>
> **Self-verify.** Run the FULL suite `python3 -m pytest src/ -v` (use `python3 -m pytest`, NOT the `timeout` binary — unavailable on macOS). Baseline is **61 passed**; expect **54** after removing 7 tests. **Any number other than 54 needs explaining, not accepting** — if a test you did not intend to touch now fails, you have removed something still in use: halt and report rather than deleting the failing test. **Commit** with a descriptive message (e.g. `revert(forge): retire plan-154 recently-implemented-overlap advisory`).
>
> **Deposit:** `knowledge/development/retire-154-advisory-2026-07-16.md` — what was removed (with line references), the `_tokenize_for_overlap` no-other-caller confirmation, the `test_report_no_overlap_unchanged` coverage decision, the Task C zero-hit grep output, confirmation `detect_duplicates` + `terminal_proposals_flagged` are untouched, the full-suite tail showing the count, commit hash, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/src/lessons_forge.py`
> - `lessons-forge/src/test_lessons_forge.py`
> - `lessons-forge/knowledge/development/retire-154-advisory-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — QA

---

> **Before starting, read the Step 1 deposit and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2 (QA).
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` for domain context (skip with a note if absent). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **Verification + reporting only — no product-code changes.** If you find a blocker, STOP and report it.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule.** Every SQL row states which DB it ran against; canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. Deposit **RAW command output**, never a summary. **Disk-verify every filesystem claim** (entry 139's discipline — and note that entry 139's own classification this cycle cited a function name that does not exist; do not repeat that class of miss: any identifier you name, grep for it before asserting it).
>
> **Scope:**
> - `knowledge/qa/retire-154-advisory-qa-2026-07-16.md`
>
> Verification table, one row per claim:
> 1. **Advisory fully gone from `src/`** — zero hits for `detect_recently_implemented_overlaps`, `recently_implemented_overlaps`, `_tokenize_for_overlap`, `Recently-implemented overlap`. Raw grep output.
> 2. **Full suite** — `python3 -m pytest src/ -v` (`python3 -m pytest`, NOT `timeout`). Expect **54 passed** (61 − 7). Raw tail. Any other number is a FAIL unless the Step-1 dev-log explains it and you independently agree.
> 3. **No collateral damage** — `detect_duplicates` and its tests intact and green; plan 204's `terminal_proposals_flagged` still returned by `run_full_lessons_cycle` and still covered by its parametrized terminal-status tests. **This is the row that matters most**: plan 204's guard is what stops the corpus corruption, and it sits in the same function the advisory was removed from.
> 4. **`run_full_lessons_cycle` contract otherwise intact** — returns `ingested_count`, `updated_count`, `unchanged_count`, `duplicates_marked_count`, `needs_classification`, `terminal_proposals_flagged`, `cycle_timestamp`; only `recently_implemented_overlaps` is gone.
> 5. **Report rendering coverage not lost** — confirm plain report rendering is still covered by a test after `test_report_no_overlap_unchanged`'s removal, per the Step-1 decision.
> 6. **History preserved** — `reports/lessons-report-2026-07-16.md` still contains its 14 advisory lines (the historical Gate 1 artifact, deliberately NOT regenerated), and `PROJECT_STATUS.md` / the plan-154 QA doc still reference the advisory. **A scrubbed history is a FAIL, not a cleanup.**
> 7. **Standing plan-204 regression watch** — on canonical: proposal 145 still `implemented`, `stale` count still 3, `get_unclassified_entries()` still `[]`. Gate 1 routes intact (146=`reference`, 147=`codify`, 148=`codify`).
>
> If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/retire-154-advisory-qa-2026-07-16.md` — verification table with DB-source column, raw output, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (plan-154 advisory retired per CEO decision 2026-07-16 on first-production-run evidence: 4/4 false positives, missed the true candidate, and its motivating case proved a symptom of the plan-204 bug; suite 61 → 54; the 2026-07-16 report retained as the historical Gate 1 artifact); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/retire-154-advisory-qa-2026-07-16.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
