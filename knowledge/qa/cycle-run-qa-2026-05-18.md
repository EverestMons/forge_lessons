# QA Report — Lessons Forge Cycle Run (2026-05-18)

**Plan:** executable-lessons-forge-cycle-run-2026-05-18, Step 4
**Specialist:** Forge Developer (acting as QA)
**Date:** 2026-05-16

---

## (a) Test Suite Regression

```
$ cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -m pytest src/test_lessons_forge.py -v

src/test_lessons_forge.py::test_lesson_entries_schema PASSED             [  4%]
src/test_lessons_forge.py::test_lesson_proposals_schema PASSED           [  8%]
src/test_lessons_forge.py::test_check_constraints_reject_invalid PASSED  [ 12%]
src/test_lessons_forge.py::test_parse_lessons_md_basic PASSED            [ 16%]
src/test_lessons_forge.py::test_parse_lessons_md_tags PASSED             [ 20%]
src/test_lessons_forge.py::test_parse_lessons_md_archived_stop PASSED    [ 24%]
src/test_lessons_forge.py::test_parse_lessons_md_hash_deterministic PASSED [ 28%]
src/test_lessons_forge.py::test_ingest_fresh_insert PASSED               [ 32%]
src/test_lessons_forge.py::test_ingest_unchanged_noop PASSED             [ 36%]
src/test_lessons_forge.py::test_ingest_updated_entry PASSED              [ 40%]
src/test_lessons_forge.py::test_ingest_stale_proposals PASSED            [ 44%]
src/test_lessons_forge.py::test_insert_proposal_basic PASSED             [ 48%]
src/test_lessons_forge.py::test_insert_proposal_minimal_fields PASSED    [ 52%]
src/test_lessons_forge.py::test_detect_duplicates_empty_list PASSED      [ 56%]
src/test_lessons_forge.py::test_detect_duplicates_no_match PASSED        [ 60%]
src/test_lessons_forge.py::test_detect_duplicates_tag_match PASSED       [ 64%]
src/test_lessons_forge.py::test_detect_duplicates_heading_match PASSED   [ 68%]
src/test_lessons_forge.py::test_detect_duplicates_first_match_wins PASSED [ 72%]
src/test_lessons_forge.py::test_detect_duplicates_tag_substring_not_flagged PASSED [ 76%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_fresh PASSED      [ 80%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_with_duplicates PASSED [ 84%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_idempotent PASSED [ 88%]
src/test_lessons_forge.py::test_generate_lessons_report_empty PASSED     [ 92%]
src/test_lessons_forge.py::test_generate_lessons_report_multi_category PASSED [ 96%]
src/test_lessons_forge.py::test_generate_lessons_report_writes_file PASSED [100%]

25 passed in 0.06s
```

| Check | Result |
|---|---|
| Tests collected | 25 |
| Tests passed | 25 |
| Tests failed | 0 |
| Verdict | PASS |

---

## (b) DB Invariants

```
orphan entries (should be 0): 0
dangling proposals (should be 0): 0
proposals with invalid category (should be 0): 0
proposals with invalid confidence (should be 0): 0
---
lesson_entries total: 57
lesson_proposals total: 62
proposals by status:
  proposed 25
  superseded 23
  implemented 14
proposals by category:
  governance_rule 30
  duplicate 19
  instrumentation 7
  structural 6
```

| Invariant | Expected | Actual | Verdict |
|---|---|---|---|
| Orphan entries | 0 | 0 | PASS |
| Dangling proposals | 0 | 0 | PASS |
| Invalid category | 0 | 0 | PASS |
| Invalid confidence | 0 | 0 | PASS |

Post-cycle totals: 57 entries, 62 proposals.

---

## (c) Schema Drift Check

**Live DB `lesson_entries`:**
```sql
CREATE TABLE lesson_entries (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file     TEXT    NOT NULL,
    source_heading  TEXT    NOT NULL,
    entry_date      TEXT,
    raw_content     TEXT    NOT NULL,
    content_hash    TEXT    NOT NULL,
    tags            TEXT,
    ingested_at     TEXT    NOT NULL,
    UNIQUE(source_file, source_heading)
);
```

**Live DB `lesson_proposals`:**
```sql
CREATE TABLE lesson_proposals (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_id            INTEGER NOT NULL REFERENCES lesson_entries(id) ON DELETE CASCADE,
    category            TEXT    NOT NULL CHECK(category IN ('structural', 'instrumentation', 'governance_rule', 'language', 'narrative', 'duplicate')),
    subcategory         TEXT,
    suggested_action    TEXT    NOT NULL,
    reasoning           TEXT    NOT NULL,
    confidence          TEXT    NOT NULL CHECK(confidence IN ('low', 'medium', 'high')),
    status              TEXT    NOT NULL DEFAULT 'proposed' CHECK(status IN ('proposed', 'accepted', 'rejected', 'ambiguous', 'stale', 'superseded', 'implemented')),
    target_layer        TEXT    CHECK(target_layer IS NULL OR target_layer IN ('structure', 'governance', 'language', 'none')),
    target_artifact     TEXT,
    duplicate_of        INTEGER,
    proposed_at         TEXT    NOT NULL,
    status_updated_at   TEXT,
    status_updated_by   TEXT    CHECK(status_updated_by IS NULL OR status_updated_by IN ('planner', 'ceo', 'auto'))
);
```

Both table DDLs and all 6 indexes match `src/db.py` canonical schema byte-for-byte (modulo `IF NOT EXISTS` creation guard).

| Check | Verdict |
|---|---|
| lesson_entries schema | PASS |
| lesson_proposals schema | PASS |
| Indexes (6 total) | PASS |

---

## (d) Rule 20 Self-Check

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: knowledge/development/
Files verified: 7
```

Files checked:
- `knowledge/development/cycle-result-2026-05-18.json`
- `knowledge/development/dev-log-cycle-run-step-1-2026-05-18.md`
- `knowledge/development/classifications-summary-2026-05-18.md`
- `knowledge/development/dev-log-cycle-run-step-2-2026-05-18.md`
- `knowledge/development/dev-log-cycle-run-step-3-2026-05-18.md`
- `reports/lessons-report-2026-05-18.md`
- `knowledge/qa/cycle-run-qa-2026-05-18.md`

---

## Final Verdict

**PASS** — All four QA checks pass. 25/25 tests green, all DB invariants hold, no schema drift, Rule 20 self-check output appended below.

---

## Output Receipt

**Plan:** executable-lessons-forge-cycle-run-2026-05-18, Step 4
**Specialist:** Forge Developer (QA)
**Status:** Complete

**Files Created:**
- `knowledge/qa/cycle-run-qa-2026-05-18.md` (this file)
- `knowledge/development/dev-log-cycle-run-step-4-2026-05-18.md`

**Files Verified (all plan deposits):**
- `knowledge/development/cycle-result-2026-05-18.json` (Step 1)
- `knowledge/development/dev-log-cycle-run-step-1-2026-05-18.md` (Step 1)
- `knowledge/development/classifications-summary-2026-05-18.md` (Step 2)
- `knowledge/development/dev-log-cycle-run-step-2-2026-05-18.md` (Step 2)
- `reports/lessons-report-2026-05-18.md` (Step 3)
- `knowledge/development/dev-log-cycle-run-step-3-2026-05-18.md` (Step 3)

**Database State (data only, no schema changes):**
- lesson_entries: 57 (38 pre-cycle + 19 ingested)
- lesson_proposals: 62 (38 pre-cycle + 24 classified)

**Tests Run:** 25 passed, 0 failed
**Errors/Warnings:** None
