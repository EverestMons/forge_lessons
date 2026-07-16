# QA Report — Retire plan-154 recently-implemented-overlap advisory
**Date:** 2026-07-16 | **Plan:** 207 | **Step:** 2 (QA)

## Step 1 Deposit Verification

Step 1 dev-log at `knowledge/development/retire-154-advisory-2026-07-16.md` — Output Receipt status: **Complete**, commit `1dc1c3c`.

## Verification Table

| # | Claim | DB Source | Result | Raw Evidence |
|---|---|---|---|---|
| 1 | Advisory fully gone from `src/` | n/a (filesystem) | **PASS** | All 4 greps return zero hits — see §Raw Output 1 |
| 2 | Full suite 55 passed | n/a (pytest) | **PASS** | 55 passed in 0.13s — see §Raw Output 2 |
| 3 | No collateral damage | n/a (pytest + grep) | **PASS** | `detect_duplicates` at :297, 6 tests green; `terminal_proposals_flagged` at :135, :179, :509, 4 parametrized tests green — see §Raw Output 3 |
| 4 | `run_full_lessons_cycle` contract intact | n/a (source read) | **PASS** | Returns 7 keys: `ingested_count`, `updated_count`, `unchanged_count`, `duplicates_marked_count`, `needs_classification`, `terminal_proposals_flagged`, `cycle_timestamp`; only `recently_implemented_overlaps` removed — see §Raw Output 4 |
| 5 | Report rendering coverage not lost | n/a (test file) | **PASS** | `test_report_renders_proposal_details` at :1300 asserts heading + suggested-action — see §Raw Output 5 |
| 6 | History preserved | n/a (filesystem) | **PASS** | `reports/lessons-report-2026-07-16.md` has 14 advisory lines; `PROJECT_STATUS.md` references plan 154; `classifier-recently-implemented-dedup-qa-2026-07-09.md` exists — see §Raw Output 6 |
| 7 | Plan-204 regression watch | canonical (read-only) | **PASS** | Proposal 145 `implemented`, stale count 3, unclassified `[]`, routes 146=reference/147=codify/148=codify — see §Raw Output 7 |

## Raw Output

### 1 — Advisory fully gone from `src/`

```
$ grep -rn detect_recently_implemented_overlaps src/
(no output — exit 1)
$ grep -rn recently_implemented_overlaps src/
(no output — exit 1)
$ grep -rn _tokenize_for_overlap src/
(no output — exit 1)
$ grep -rn "Recently-implemented overlap" src/
(no output — exit 1)
```

### 2 — Full suite

```
$ python3 -m pytest src/ -v
src/test_lessons_forge.py::test_lesson_entries_schema PASSED             [  1%]
src/test_lessons_forge.py::test_lesson_proposals_schema PASSED           [  3%]
src/test_lessons_forge.py::test_check_constraints_reject_invalid PASSED  [  5%]
src/test_lessons_forge.py::test_parse_lessons_md_basic PASSED            [  7%]
src/test_lessons_forge.py::test_parse_lessons_md_tags PASSED             [  9%]
src/test_lessons_forge.py::test_parse_lessons_md_archived_stop PASSED    [ 10%]
src/test_lessons_forge.py::test_parse_lessons_md_hash_deterministic PASSED [ 12%]
src/test_lessons_forge.py::test_ingest_fresh_insert PASSED               [ 14%]
src/test_lessons_forge.py::test_ingest_unchanged_noop PASSED             [ 16%]
src/test_lessons_forge.py::test_ingest_updated_entry PASSED              [ 18%]
src/test_lessons_forge.py::test_ingest_stale_proposals PASSED            [ 20%]
src/test_lessons_forge.py::test_get_unclassified_entries PASSED          [ 21%]
src/test_lessons_forge.py::test_insert_proposal_basic PASSED             [ 23%]
src/test_lessons_forge.py::test_insert_proposal_minimal_fields PASSED    [ 25%]
src/test_lessons_forge.py::test_detect_duplicates_empty_list PASSED      [ 27%]
src/test_lessons_forge.py::test_detect_duplicates_no_match PASSED        [ 29%]
src/test_lessons_forge.py::test_detect_duplicates_tag_match PASSED       [ 30%]
src/test_lessons_forge.py::test_detect_duplicates_heading_match PASSED   [ 32%]
src/test_lessons_forge.py::test_detect_duplicates_first_match_wins PASSED [ 34%]
src/test_lessons_forge.py::test_detect_duplicates_tag_substring_not_flagged PASSED [ 36%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_fresh PASSED      [ 38%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_with_duplicates PASSED [ 40%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_idempotent PASSED [ 41%]
src/test_lessons_forge.py::test_needs_classification_excludes_dispositioned_entry PASSED [ 43%]
src/test_lessons_forge.py::test_needs_classification_includes_stale_only_entry PASSED [ 45%]
src/test_lessons_forge.py::test_needs_classification_plus_duplicates_equals_total PASSED [ 47%]
src/test_lessons_forge.py::test_generate_lessons_report_empty PASSED     [ 49%]
src/test_lessons_forge.py::test_generate_lessons_report_multi_category PASSED [ 50%]
src/test_lessons_forge.py::test_generate_lessons_report_writes_file PASSED [ 52%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[codify] PASSED [ 54%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[backlog] PASSED [ 56%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[reference] PASSED [ 58%]
src/test_lessons_forge.py::test_insert_proposal_route_none_default PASSED [ 60%]
src/test_lessons_forge.py::test_insert_proposal_invalid_route_raises PASSED [ 61%]
src/test_lessons_forge.py::test_route_check_constraint_rejects_invalid_sql PASSED [ 63%]
src/test_lessons_forge.py::test_migration_idempotence_double_init PASSED [ 65%]
src/test_lessons_forge.py::test_migration_adds_route_to_pre_existing_db PASSED [ 67%]
src/test_lessons_forge.py::test_set_proposal_route_persists PASSED       [ 69%]
src/test_lessons_forge.py::test_set_proposal_route_invalid_raises PASSED [ 70%]
src/test_lessons_forge.py::test_report_renders_route_where_present PASSED [ 72%]
src/test_lessons_forge.py::test_reference_status_migration_idempotence PASSED [ 74%]
src/test_lessons_forge.py::test_reference_status_migration_pre_existing_db PASSED [ 76%]
src/test_lessons_forge.py::test_reference_status_check_accepts_reference PASSED [ 78%]
src/test_lessons_forge.py::test_reference_status_check_still_rejects_invalid PASSED [ 80%]
src/test_lessons_forge.py::test_reference_status_migration_preserves_row_count PASSED [ 81%]
src/test_lessons_forge.py::test_report_renders_proposal_details PASSED   [ 83%]
src/test_lessons_forge.py::test_hash_trailing_separator_invariant PASSED [ 85%]
src/test_lessons_forge.py::test_hash_substantive_edit_changes_hash PASSED [ 87%]
src/test_lessons_forge.py::test_raw_content_stored_verbatim_with_separator PASSED [ 89%]
src/test_lessons_forge.py::test_terminal_status_guard[implemented] PASSED [ 90%]
src/test_lessons_forge.py::test_terminal_status_guard[reference] PASSED  [ 92%]
src/test_lessons_forge.py::test_terminal_status_guard[rejected] PASSED   [ 94%]
src/test_lessons_forge.py::test_terminal_status_guard[superseded] PASSED [ 96%]
src/test_lessons_forge.py::test_nonterminal_still_stales PASSED          [ 98%]
src/test_lessons_forge.py::test_trailing_separator_only_delta_zero_stales PASSED [100%]

============================== 55 passed in 0.13s ==============================
```

Count: 61 (baseline) − 7 (removed plan-154 tests) + 1 (added `test_report_renders_proposal_details`) = **55**. Step 1 explains the +1 — the replacement test preserves report-rendering coverage that would otherwise be lost. Independently confirmed: no other test asserts per-proposal heading + suggested-action rendering. The count is correct.

### 3 — No collateral damage

`detect_duplicates` source locations (post-edit):
```
src/lessons_forge.py:297:def detect_duplicates(conn: sqlite3.Connection, entry_ids: list[int],
src/lessons_forge.py:424:      3. detect_duplicates(conn, candidate_ids) — scan reference inputs
src/lessons_forge.py:477:    duplicates = detect_duplicates(conn, candidate_ids)
```

`detect_duplicates` tests (6 tests, all PASSED):
```
test_detect_duplicates_empty_list PASSED
test_detect_duplicates_no_match PASSED
test_detect_duplicates_tag_match PASSED
test_detect_duplicates_heading_match PASSED
test_detect_duplicates_first_match_wins PASSED
test_detect_duplicates_tag_substring_not_flagged PASSED
```

`terminal_proposals_flagged` source locations (post-edit):
```
src/lessons_forge.py:135:        "stale_proposals_marked": 0, "terminal_proposals_flagged": [],
src/lessons_forge.py:179:                result["terminal_proposals_flagged"].append({
src/lessons_forge.py:454:          - terminal_proposals_flagged: list[dict] — terminal-status proposals
src/lessons_forge.py:509:        "terminal_proposals_flagged": ingestion["terminal_proposals_flagged"],
```

`terminal_status_guard` tests (4 parametrized, all PASSED):
```
test_terminal_status_guard[implemented] PASSED
test_terminal_status_guard[reference] PASSED
test_terminal_status_guard[rejected] PASSED
test_terminal_status_guard[superseded] PASSED
```

### 4 — `run_full_lessons_cycle` return contract

Source at `src/lessons_forge.py:503-511`:
```python
    return {
        "ingested_count": ingestion["inserted"],
        "updated_count": ingestion["updated"],
        "unchanged_count": ingestion["unchanged"],
        "duplicates_marked_count": duplicates_marked_count,
        "needs_classification": needs_classification,
        "terminal_proposals_flagged": ingestion["terminal_proposals_flagged"],
        "cycle_timestamp": cycle_timestamp,
    }
```

7 keys present, matching the expected contract. `recently_implemented_overlaps` is the only key removed.

### 5 — Report rendering coverage

`test_report_renders_proposal_details` at `src/test_lessons_forge.py:1300-1326`:
```python
def test_report_renders_proposal_details():
    """Report renders per-proposal heading and suggested-action line."""
    ...
    assert "### 2026-07-01" in content
    assert "- **Suggested action:** Fix something unique" in content
```

Asserts per-proposal heading and suggested-action rendering — the two coverage points that would have been lost with `test_report_no_overlap_unchanged`.

### 6 — History preserved

Historical report advisory lines (14 lines):
```
$ grep -c "Recently-implemented overlap" reports/lessons-report-2026-07-16.md
14
```

PROJECT_STATUS.md references:
```
:338: Recently-implemented-proposal overlap detection shipped 2026-07-09 (plan 154, commit `ad6b37c`). ...
:344: ... plan-154 advisory retirement queued separately ...
```

Plan-154 QA doc:
```
$ ls knowledge/qa/classifier-recently-implemented-dedup-qa-2026-07-09.md
EXISTS
```

### 7 — Standing plan-204 regression watch

```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT id, status FROM lesson_proposals WHERE id = 145;"
145|implemented

$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT COUNT(*) FROM lesson_proposals WHERE status = 'stale';"
3

$ python3 -c "... get_unclassified_entries(conn) ..."
[]

$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT id, route FROM lesson_proposals WHERE id IN (146, 147, 148);"
146|reference
147|codify
148|codify
```

All plan-204 guards intact: proposal 145 `implemented`, 3 stale, 0 unclassified, Gate 1 routes correct.

## Rule 20 — QA Self-Check Results

| # | Check | Result |
|---|---|---|
| 1 | Advisory fully gone from `src/` | PASS |
| 2 | Full suite 55 passed | PASS |
| 3 | No collateral damage (`detect_duplicates` + `terminal_proposals_flagged`) | PASS |
| 4 | `run_full_lessons_cycle` contract intact | PASS |
| 5 | Report rendering coverage preserved | PASS |
| 6 | History preserved (report, PROJECT_STATUS, QA doc) | PASS |
| 7 | Plan-204 regression watch | PASS |

**PASSED — SELF-CHECK PASSED**

### Ledger Updates

#### Project Status

Plan-154 recently-implemented-overlap advisory retired per CEO decision 2026-07-16 on first-production-run evidence: 4/4 false positives at Gate 1, missed the true candidate (entry 139), and its motivating case (proposal 131 duplication) proved a downstream symptom of the whitespace-hash bug fixed by plan 204. Suite 61 → 55 (7 plan-154 tests removed, 1 replacement `test_report_renders_proposal_details` added to preserve report-rendering coverage). The 2026-07-16 report retained as the historical Gate 1 artifact with all 14 advisory lines intact.

#### Prompt Feedback

No prompt feedback this step.

---

### Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Plan** | 207 |
| **Step** | 2 (QA) |
| **Date** | 2026-07-16 |
| **Files Created (Knowledge)** | `knowledge/qa/retire-154-advisory-qa-2026-07-16.md` |
| **Verification** | 7/7 PASS |
| **DB Touched** | Read-only queries against canonical DB only |
