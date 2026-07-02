# QA Report — `needs_classification` Return-Shape Fix
**Date:** 2026-07-02 | **Plan:** 116 | **Step:** 2 (QA) | **Dev Commit:** `4235f85`

## Verification Table

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | `run_full_lessons_cycle` contains exactly one `needs_classification` assignment and it is `get_unclassified_entries(conn)`, positioned after the duplicate-proposal insertion loop | PASS | Line 437: `needs_classification = get_unclassified_entries(conn)` — immediately after the duplicate-proposal insertion loop (lines 420–435). No other assignment to `needs_classification` exists in the function. Code excerpt: `duplicates_marked_count += 1` (line 435) → blank line → `needs_classification = get_unclassified_entries(conn)` (line 437) → `return {` (line 439). |
| 2 | Old minus-duplicates loop is gone | PASS | `grep -rn 'all entry IDs minus those with duplicate proposals' src/` returns 0 hits. The old comment and loop (lines 436–444 in pre-fix code) are fully removed. |
| 3 | Regression test (a) exists and asserts a dispositioned entry is absent — passes in isolation | PASS | `test_needs_classification_excludes_dispositioned_entry` (line 795): inserts an `implemented` proposal for an entry, re-runs cycle, asserts `entry_id not in result2["needs_classification"]` and `len(result2["needs_classification"]) == 1`. Ran in isolation: `1 passed in 0.11s`. |
| 4 | Stale-only inclusion test (b) exists and passes in isolation | PASS | `test_needs_classification_includes_stale_only_entry` (line 821): inserts a `stale` proposal for an entry, re-runs cycle, asserts `entry_id in result2["needs_classification"]`. Ran in isolation: `1 passed in 0.04s`. |
| 5 | Both pre-existing cycle tests pass with assertions untouched | PASS | `git diff 4235f85~1..4235f85 -- src/test_lessons_forge.py` shows additions only (3 new test functions, 70 lines added). No existing assertion lines were modified. Both `test_run_full_lessons_cycle_fresh` and `test_run_full_lessons_cycle_with_duplicates` pass. |
| 6 | Both docstrings updated per plan | PASS | **`get_unclassified_entries` docstring** (lines 215–217): `"This is the canonical work list. As of 2026-07-02, run_full_lessons_cycle() delegates its needs_classification field to this helper, so the two are consistent. This helper remains the canonical source (Rule #47)."` — old over-report warning replaced. `NOT EXISTS` warning retained (line 219). **`run_full_lessons_cycle` return-key description** (lines 388–391): `"needs_classification: list[int] — entry IDs requiring classification, computed via get_unclassified_entries(conn) after duplicate-proposal insertion. DB-wide (not parse-scoped); matches the canonical Rule #47 work list."` |
| 7 | Full suite green | PASS | `python3 -m pytest src/ -v --timeout=600` — **29 passed in 0.15s**. |

## Full Suite Tail (verbatim)

```
src/test_lessons_forge.py::test_run_full_lessons_cycle_fresh PASSED      [ 72%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_with_duplicates PASSED [ 75%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_idempotent PASSED [ 79%]
src/test_lessons_forge.py::test_needs_classification_excludes_dispositioned_entry PASSED [ 82%]
src/test_lessons_forge.py::test_needs_classification_includes_stale_only_entry PASSED [ 86%]
src/test_lessons_forge.py::test_needs_classification_plus_duplicates_equals_total PASSED [ 89%]
src/test_lessons_forge.py::test_generate_lessons_report_empty PASSED     [ 93%]
src/test_lessons_forge.py::test_generate_lessons_report_multi_category PASSED [ 96%]
src/test_lessons_forge.py::test_generate_lessons_report_writes_file PASSED [100%]

============================== 29 passed in 0.15s ==============================
```

## Rule 20 — QA Self-Check Results

| Check | Result |
|---|---|
| Verification table present with 7 rows | PASSED |
| All 7 verification rows show PASS | PASSED |
| Full suite tail included verbatim | PASSED |
| No existing test assertions modified | PASSED |
| Baton close-out applied to NEXT_SESSION.md | PASSED |

PASSED — SELF-CHECK PASSED

### Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Dev Commit Verified** | `4235f85` |
| **Tests** | 29 passed, 0 failed |
| **Verification Rows** | 7/7 PASS |
| **Baton** | `needs_classification` over-report horizon item closed in NEXT_SESSION.md |

### Ledger Updates

#### Project Status

`needs_classification` over-report closed 2026-07-02. The producer (`run_full_lessons_cycle`) now delegates its `needs_classification` field to the canonical Rule #47 helper `get_unclassified_entries(conn)`, positioned after duplicate-proposal insertion. Regression-tested with three new tests covering dispositioned-entry exclusion, stale-only re-queue inclusion, and the fresh-DB invariant. Rule #47 remains in force as defense-in-depth.

#### Prompt Feedback

No prompt feedback this session.
