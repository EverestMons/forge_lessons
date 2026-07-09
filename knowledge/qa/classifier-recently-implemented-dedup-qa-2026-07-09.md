# QA Report — Classifier Recently-Implemented Dedup (Advisory)

**Plan:** 154 — Surface recently-implemented-proposal overlaps in classifier review
**Date:** 2026-07-09
**Step:** 2 (QA)
**Scope:** Verification + reporting only — no product-code changes.

---

## Verification Items

### 1. Advisory-only contract (critical) — PASS

**Code review evidence:**

- `detect_recently_implemented_overlaps` (src/lessons_forge.py:393-505): performs only `SELECT` queries (lines 420-426 and 445-448). No `INSERT`, `UPDATE`, or `DELETE` statements anywhere in the function. Return value is a plain `list[dict]` — no connection mutations.

- `run_full_lessons_cycle` (src/lessons_forge.py:592-604): calls `detect_recently_implemented_overlaps(conn, candidate_ids)` at line 592 and stores the result in the returned dict under key `recently_implemented_overlaps` at line 604. The function does NOT call `insert_proposal` from this output, does NOT change any proposal status, and does NOT write to the DB from it. The existing `insert_proposal` calls (line 580-588) remain scoped to the `detect_duplicates` path only — unchanged.

- `generate_lessons_report` (src/lessons_forge.py:640-694): calls `detect_recently_implemented_overlaps` at line 643 to build `overlap_map`, then reads from it at line 688 to append advisory lines. No DB writes — the function only reads proposals and writes a markdown file.

**Test evidence:**

- `test_overlap_advisory_only_no_writes` (src/test_lessons_forge.py:1381-1414): snapshots `COUNT(*)` and `(id, status)` tuples from `lesson_proposals` before and after calling `detect_recently_implemented_overlaps`. Asserts both are identical. **PASSES** in the suite.

**Verdict: PASS** — The advisory-only contract is enforced at all three integration points (function, pipeline, report). Zero DB mutation paths exist.

---

### 2. Recency window — PASS

- **Test #1** `test_overlap_recent_match` (src/test_lessons_forge.py:1318-1337): creates an entry with tags `planner-discipline, recurring-bug` and a recently-implemented proposal (default `status_updated_at="2026-06-07T00:00:00+00:00"`) with matching keywords. Uses `recency_days=9999` to ensure the proposal is within the window. Asserts `len(result) >= 1` and correct `entry_id`. **PASSES.**

- **Test #2** `test_overlap_old_not_surfaced` (src/test_lessons_forge.py:1340-1357): creates the same entry shape but with `status_updated_at="2025-01-01T00:00:00+00:00"` and `recency_days=1`. Asserts `result == []`. **PASSES.**

- The recency filter in the SQL query (src/lessons_forge.py:424) uses `date('now', '-' || ? || ' days')` which correctly excludes proposals outside the window.

**Verdict: PASS** — Both inside-window and outside-window cases are tested and pass.

---

### 3. Known-miss catch (131/135 live validation) — PASS

**Dev-log Task D evidence (knowledge/development/classifier-recently-implemented-dedup-2026-07-09.md, lines 37-50):**

| Entry | Caught? | Overlapping Proposals | Match Mechanism |
|---|---|---|---|
| 123 (proposal 131) | **YES** | #1, #127, #128 | tag overlap: planner-discipline; keyword overlap: discipline, planner |
| 127 (proposal 135) | **YES** | #1, #127, #128 | tag overlap: planner-discipline; keyword overlap: discipline, planner |

Both entries are tagged `` `planner-discipline` ``. The tag-match boost pathway (score raised to >= 0.15 when a full compound tag like `planner-discipline` is found in the proposal's concatenated text) fires reliably. This is well above the 0.08 threshold.

**Synthetic test:** `test_overlap_131_135_shape` (src/test_lessons_forge.py:1489-1539) mirrors the 131/135 case with word-for-word overlapping `suggested_action` text and asserts both synthetic entries are caught. **PASSES.**

**Verdict: PASS** — The known 131/135 misses are caught by both live-DB validation and synthetic test.

---

### 4. Report rendering + no regression — PASS

- **Test #5a** `test_report_renders_overlap_advisory` (src/test_lessons_forge.py:1417-1456): creates a `proposed` proposal for an entry that overlaps a recently-implemented proposal. Generates a report and asserts:
  - `"⚠️ **Recently-implemented overlap:**"` is in the content
  - `"proposal #N"` (with the correct implemented proposal ID) is in the content
  - `"verify not already subsumed"` is in the content
  **PASSES.**

- **Test #5b** `test_report_no_overlap_unchanged` (src/test_lessons_forge.py:1459-1486): creates a `proposed` proposal for an entry with NO overlapping implemented proposals. Generates a report and asserts:
  - `"Recently-implemented overlap"` is NOT in the content
  - Normal rendering (`"### 2026-07-01"` and `"- **Suggested action:** Fix something unique"`) is present
  **PASSES.**

- **Report rendering code** (src/lessons_forge.py:688-695): the overlap advisory line is only emitted via `for ov in overlap_map.get(entry_id, [])` — when `overlap_map` has no entry for a given `entry_id`, the loop body never executes, producing byte-identical output to the pre-plan behavior.

- **Existing tests:** all 45 pre-plan tests pass, including `test_generate_lessons_report_empty`, `test_generate_lessons_report_multi_category`, `test_generate_lessons_report_writes_file`, and `test_report_renders_route_where_present`. Zero regressions.

**Verdict: PASS** — Advisory line renders when overlap exists, renders unchanged when none, and all pre-existing report tests remain green.

---

### 5. Full suite — PASS

```
src/test_lessons_forge.py::test_lesson_entries_schema PASSED             [  1%]
src/test_lessons_forge.py::test_lesson_proposals_schema PASSED           [  3%]
src/test_lessons_forge.py::test_check_constraints_reject_invalid PASSED  [  5%]
src/test_lessons_forge.py::test_parse_lessons_md_basic PASSED            [  7%]
src/test_lessons_forge.py::test_parse_lessons_md_tags PASSED             [  9%]
src/test_lessons_forge.py::test_parse_lessons_md_archived_stop PASSED    [ 11%]
src/test_lessons_forge.py::test_parse_lessons_md_hash_deterministic PASSED [ 13%]
src/test_lessons_forge.py::test_ingest_fresh_insert PASSED               [ 15%]
src/test_lessons_forge.py::test_ingest_unchanged_noop PASSED             [ 17%]
src/test_lessons_forge.py::test_ingest_updated_entry PASSED              [ 19%]
src/test_lessons_forge.py::test_ingest_stale_proposals PASSED            [ 21%]
src/test_lessons_forge.py::test_get_unclassified_entries PASSED          [ 23%]
src/test_lessons_forge.py::test_insert_proposal_basic PASSED             [ 25%]
src/test_lessons_forge.py::test_insert_proposal_minimal_fields PASSED    [ 26%]
src/test_lessons_forge.py::test_detect_duplicates_empty_list PASSED      [ 28%]
src/test_lessons_forge.py::test_detect_duplicates_no_match PASSED        [ 30%]
src/test_lessons_forge.py::test_detect_duplicates_tag_match PASSED       [ 32%]
src/test_lessons_forge.py::test_detect_duplicates_heading_match PASSED   [ 34%]
src/test_lessons_forge.py::test_detect_duplicates_first_match_wins PASSED [ 36%]
src/test_lessons_forge.py::test_detect_duplicates_tag_substring_not_flagged PASSED [ 38%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_fresh PASSED      [ 40%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_with_duplicates PASSED [ 42%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_idempotent PASSED [ 44%]
src/test_lessons_forge.py::test_needs_classification_excludes_dispositioned_entry PASSED [ 46%]
src/test_lessons_forge.py::test_needs_classification_includes_stale_only_entry PASSED [ 48%]
src/test_lessons_forge.py::test_needs_classification_plus_duplicates_equals_total PASSED [ 50%]
src/test_lessons_forge.py::test_generate_lessons_report_empty PASSED     [ 51%]
src/test_lessons_forge.py::test_generate_lessons_report_multi_category PASSED [ 53%]
src/test_lessons_forge.py::test_generate_lessons_report_writes_file PASSED [ 55%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[codify] PASSED [ 57%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[backlog] PASSED [ 59%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[reference] PASSED [ 61%]
src/test_lessons_forge.py::test_insert_proposal_route_none_default PASSED [ 63%]
src/test_lessons_forge.py::test_insert_proposal_invalid_route_raises PASSED [ 65%]
src/test_lessons_forge.py::test_route_check_constraint_rejects_invalid_sql PASSED [ 67%]
src/test_lessons_forge.py::test_migration_idempotence_double_init PASSED [ 69%]
src/test_lessons_forge.py::test_migration_adds_route_to_pre_existing_db PASSED [ 71%]
src/test_lessons_forge.py::test_set_proposal_route_persists PASSED       [ 73%]
src/test_lessons_forge.py::test_set_proposal_route_invalid_raises PASSED [ 75%]
src/test_lessons_forge.py::test_report_renders_route_where_present PASSED [ 76%]
src/test_lessons_forge.py::test_reference_status_migration_idempotence PASSED [ 78%]
src/test_lessons_forge.py::test_reference_status_migration_pre_existing_db PASSED [ 80%]
src/test_lessons_forge.py::test_reference_status_check_accepts_reference PASSED [ 82%]
src/test_lessons_forge.py::test_reference_status_check_still_rejects_invalid PASSED [ 84%]
src/test_lessons_forge.py::test_reference_status_migration_preserves_row_count PASSED [ 86%]
src/test_lessons_forge.py::test_overlap_recent_match PASSED              [ 88%]
src/test_lessons_forge.py::test_overlap_old_not_surfaced PASSED          [ 90%]
src/test_lessons_forge.py::test_overlap_non_overlapping PASSED           [ 92%]
src/test_lessons_forge.py::test_overlap_advisory_only_no_writes PASSED   [ 94%]
src/test_lessons_forge.py::test_report_renders_overlap_advisory PASSED   [ 96%]
src/test_lessons_forge.py::test_report_no_overlap_unchanged PASSED       [ 98%]
src/test_lessons_forge.py::test_overlap_131_135_shape PASSED             [100%]

============================== 52 passed in 0.13s ==============================
```

**Counts:** 52 passed, 0 failed, 0 errors, 0 warnings.
**Pre-plan baseline:** 45 tests. **New tests:** 7. **Regressions:** 0.

**Verdict: PASS** — Full suite green, zero regressions.

---

## Rule 20 — QA Self-Check Results

All 5 verification items reviewed with code-level evidence (file paths, line numbers, and logic tracing). Each item assessed independently against both code reading and test execution results.

| Check | Item | Evidence Source | Result |
|---|---|---|---|
| 1 | Advisory-only contract | Code (3 integration points) + test #4 | PASS |
| 2 | Recency window | Tests #1/#2 + SQL filter | PASS |
| 3 | Known-miss catch | Dev-log Task D + test #7 | PASS |
| 4 | Report rendering + no regression | Tests #5a/#5b + code + existing tests | PASS |
| 5 | Full suite | 52/52 passed, 0 regressions | PASS |

**PASSED — SELF-CHECK PASSED**

---

## Rule 22 — Verification

All verification claims are substantiated by direct code reading (file:line citations) and test execution output. No claims are based on assumption or inference without evidence. The test suite was executed fresh (not cached) and the full output is captured above.

---

### Ledger Updates

#### Prompt Feedback

- The plan's verification item 1 ("by reading the code AND confirming test #4 exists and passes") is well-structured — requiring both static analysis and dynamic verification prevents false confidence from either alone.
- The dev-log's Task D validation section (entries 123/127) is clear and actionable for QA cross-reference. Reporting overlapping proposal IDs and match mechanisms provides verifiable evidence without requiring QA to re-run the live-DB query.

---

## Output Receipt

| Field | Value |
|---|---|
| **Plan** | 154 — Classifier recently-implemented dedup (advisory) |
| **Step** | 2 (QA) |
| **Status** | COMPLETE |
| **Verification** | 5/5 PASS |
| **Tests** | 52 passed, 0 failed, 0 regressions (45 pre-plan + 7 new) |
| **Rule 20** | PASSED — SELF-CHECK PASSED |
| **Rule 22** | All claims substantiated with code:line evidence |
| **Deposits** | `knowledge/qa/classifier-recently-implemented-dedup-qa-2026-07-09.md` |
