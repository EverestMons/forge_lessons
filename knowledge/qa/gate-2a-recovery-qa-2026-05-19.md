# QA Report — Gate 2a Recovery (2026-05-19)

**Date:** 2026-05-16
**Agent:** Forge Developer (QA)
**Scope:** Gate 2a recovery — schema rollback, status collapse, worktree teardown

---

## Check 1 — Schema correct

**Command:** `SELECT sql FROM sqlite_master WHERE type='table' AND name='lesson_proposals'`

**Output:**
```sql
CREATE TABLE "lesson_proposals" (
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
)
```

**Determination:** CHECK constraint contains exactly 7 status values, no `'deferred'`. **PASS**

---

## Check 2 — Data correct

**Command:** `SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY status`

**Output:**
```
('accepted', 18)
('implemented', 14)
('rejected', 6)
('superseded', 24)
```

**Determination:** accepted=18, implemented=14, rejected=6, superseded=24. Total=62. **PASS**

---

## Check 3 — No deferred rows anywhere

**Command:** `SELECT COUNT(*) FROM lesson_proposals WHERE status='deferred'`

**Output:**
```
0
```

**Determination:** 0 deferred rows. **PASS**

---

## Check 4 — Cross-reference intact

**Command:** `SELECT id, duplicate_of FROM lesson_proposals WHERE id IN (38, 62)`

**Output:**
```
(38, 62)
(62, 38)
```

**Determination:** 38→62, 62→38. **PASS**

---

## Check 5 — G16 acceptance preserved

**Command:** `SELECT id, status FROM lesson_proposals WHERE id=62`

**Output:**
```
(62, 'accepted')
```

**Determination:** status=accepted. **PASS**

---

## Check 6 — Indexes present

**Command:** `SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='lesson_proposals' ORDER BY name`

**Output:**
```
idx_lesson_proposals_category
idx_lesson_proposals_entry
idx_lesson_proposals_status
```

**Determination:** All 3 indexes present. **PASS**

---

## Check 7 — Test suite still passes

**Command:** `python3 -m pytest src/test_lessons_forge.py -v`

**Output:**
```
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
collected 25 items

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

============================== 25 passed in 0.05s ==============================
```

**Determination:** 25/25 PASSED. **PASS**

---

## Check 8 — No stale worktree

**Command:** `git worktree list`

**Output:**
```
/Users/marklehn/Developer/GitHub/lessons-forge                                                 4cd57d6 [main]
/Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/gate-2a-recovery-2026-05-19  b8c056f (detached HEAD)
```

**Determination:** No `gate-2a-lessons-forge-ratification-2026-05-19` worktree. Only main and this recovery session's worktree. **PASS**

---

## Check 9 — `src/db.py` canonical untouched

**Command:** `git --no-pager log --oneline -5 -- src/db.py`

**Output:**
```
e1c9825 feat: migrate lessons-forge code from forge (Phase A step 2)
```

**Determination:** Most recent commit touching `src/db.py` is `e1c9825` (Phase A, pre-dates 2026-05-19). No recovery-side modifications. **PASS**

---

## Check 10 — Working tree clean

**Command:** `git status`

**Output:**
```
On branch main
Your branch is ahead of 'origin/main' by 1 commit.

Untracked files:
  knowledge/decisions/in-progress-executable-gate-2a-recovery-2026-05-19.md
  knowledge/development/dev-log-gate-2a-recovery-step-2-2026-05-19.md

nothing added to commit but untracked files present
```

**Determination:** No uncommitted changes to tracked files. Untracked files are the in-progress plan file and the Step 2 dev log (expected). **PASS**

---

## Summary

| # | Check | Result |
|---|-------|--------|
| 1 | Schema correct (7 values, no deferred) | PASS |
| 2 | Data correct (18+14+6+24=62) | PASS |
| 3 | No deferred rows | PASS |
| 4 | Cross-reference intact (38↔62) | PASS |
| 5 | G16 acceptance preserved (id=62 accepted) | PASS |
| 6 | Indexes present (3/3) | PASS |
| 7 | Test suite (25/25) | PASS |
| 8 | No stale worktree | PASS |
| 9 | src/db.py untouched | PASS |
| 10 | Working tree clean | PASS |

**Verdict: 10/10 PASS**
