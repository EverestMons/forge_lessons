# Dev Log — Retire plan-154 recently-implemented-overlap advisory
**Date:** 2026-07-16 | **Plan:** 207 | **Step:** 1 (DEV)

## What Was Removed

### From `src/lessons_forge.py`

| Item | Former Lines | Type |
|---|---|---|
| `_OVERLAP_STOP` | :416-426 | constant (frozenset) |
| `_OVERLAP_WORD_RE` | :428 | constant (compiled regex) |
| `_tokenize_for_overlap` | :431-434 | helper function |
| `detect_recently_implemented_overlaps` | :437-549 | advisory function |
| Step 5 call in `run_full_lessons_cycle` | :635-638 | call site |
| `recently_implemented_overlaps` return key | :648 | return dict key |
| `overlap_map` construction in `generate_lessons_report` | :685-689 | call site |
| Advisory rendering loop in `generate_lessons_report` | :733-740 | rendering block |

### From `src/test_lessons_forge.py`

| Test | Former Lines |
|---|---|
| `_seed_implemented_proposal` (helper) | :1304-1317 |
| `test_overlap_recent_match` | :1320-1339 |
| `test_overlap_old_not_surfaced` | :1342-1359 |
| `test_overlap_non_overlapping` | :1362-1380 |
| `test_overlap_advisory_only_no_writes` | :1383-1416 |
| `test_report_renders_overlap_advisory` | :1419-1458 |
| `test_report_no_overlap_unchanged` | :1461-1488 |
| `test_overlap_131_135_shape` | :1491-1542 |

Import of `detect_recently_implemented_overlaps` also removed from the test import block.

## `_tokenize_for_overlap` No-Other-Caller Confirmation

`grep -rn _tokenize_for_overlap src/` confirmed all 6 call sites were within `detect_recently_implemented_overlaps` (lines 477, 478, 480, 482, 505, 510) plus the definition at line 431. Zero callers outside that function.

## `test_report_no_overlap_unchanged` Coverage Decision

**Decision: replaced with `test_report_renders_proposal_details`.**

`test_report_no_overlap_unchanged` asserted three things:
1. No "Recently-implemented overlap" in content (advisory-specific, moot after removal)
2. `### 2026-07-01` heading present (per-proposal rendering)
3. `- **Suggested action:** Fix something unique` present (per-proposal rendering)

Assertions 2 and 3 are the only tests in the suite that verify per-proposal report rendering (heading + suggested-action line). No other test (`test_generate_lessons_report_multi_category` checks category sections/counts; `test_report_renders_route_where_present` checks the Route line) covers this. Dropping them would lose baseline report-rendering coverage.

Replaced with `test_report_renders_proposal_details` keeping assertions 2 and 3, dropping assertion 1.

## `detect_duplicates` + `terminal_proposals_flagged` Untouched Confirmation

- `detect_duplicates` remains at its original location (:297-413 post-edit), unchanged.
- `terminal_proposals_flagged` remains in `ingest_lesson_entries` return (:135, :179) and in `run_full_lessons_cycle` return (:509 post-edit), unchanged.
- All `detect_duplicates` tests pass (6 tests). All `terminal_status_guard` tests pass (4 parametrized).

## Task C — Zero-Hit Grep Output

```
$ grep -rn detect_recently_implemented_overlaps src/
(no output)
$ grep -rn recently_implemented_overlaps src/
(no output)
$ grep -rn _tokenize_for_overlap src/
(no output)
$ grep -rn "Recently-implemented overlap" src/
(no output)
```

All four queries return zero hits in `src/`. Historical references in `reports/`, `knowledge/`, and `PROJECT_STATUS.md` are preserved.

## Full Suite Tail

```
55 passed in 0.13s
```

**Count explanation:** 61 (baseline) - 7 (removed plan-154 tests) + 1 (added `test_report_renders_proposal_details`) = 55.

## Commit

```
1dc1c3c revert(forge): retire plan-154 recently-implemented-overlap advisory [207]
```

### Ledger Updates

#### Prompt Feedback

No prompt feedback this step.

---

### Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Plan** | 207 |
| **Step** | 1 (DEV) |
| **Date** | 2026-07-16 |
| **Commit** | 1dc1c3c |
| **Files Modified (Code)** | `src/lessons_forge.py`, `src/test_lessons_forge.py` |
| **Files Created (Knowledge)** | `knowledge/development/retire-154-advisory-2026-07-16.md` |
| **Tests** | 55 passed (61 - 7 + 1), 0 failed |
| **DB Touched** | No — code-only step, in-memory test DBs only |
