# Hash Normalization Fix — QA Report (Plan 204)

**Date:** 2026-07-16
**Plan:** 204 — Fix whitespace-only hash flips silently staling implemented proposals
**Step:** 3 (QA — verification and reporting only)

## Pre-flight

- Step 1 Output Receipt: **Complete** (commit `eb90935`)
- Step 2 Output Receipt: **Complete** (83 entries re-hashed, proposal 145 restored)

## Verification Table

| # | Claim | Result | DB Source | Evidence |
|---|---|---|---|---|
| 1 | Full suite passes, 0 regressions | **PASS** | N/A (synthetic DBs) | 61 passed in 0.28s (baseline 52 + 9 new). See raw output below. |
| 2 | Regression fixed: trailing-separator-only delta produces identical hash | **PASS** | N/A (synthetic) | `test_hash_trailing_separator_invariant` PASSED |
| 3 | Corpus integrity: proposal status distribution matches pre-corruption baseline | **PASS** | canonical (`file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro`) | `implemented=97, reference=2, rejected=15, stale=3, superseded=28` — exact match |
| 4 | Backfill touched only hashes — no `lesson_proposals` mutation | **PASS** | Script inspection + Step 2 deposit | Script issues only `UPDATE lesson_entries SET content_hash = ? WHERE id = ?`; only `SELECT` on `lesson_proposals`. Step 2 before/after distributions identical. |
| 5 | `raw_content` unnormalized in storage — entry 137 retains trailing separator | **PASS** | canonical (read-only) | Hex dump confirms `raw_content` ends with `---\n\n\n` (bytes `2d2d2d 0a0a0a`) |
| 6 | Loop closed — `get_unclassified_entries` returns exactly [138, 139, 140] | **PASS** | canonical (read-only) | Entry 137 absent from work list; only genuine new entries remain |
| 7 | Terminal-status guard covers all 4 statuses, `terminal_proposals_flagged` surfaces through `run_full_lessons_cycle` | **PASS** | N/A (synthetic) | Tests parametrized: `[implemented, reference, rejected, superseded]` all PASSED. `terminal_proposals_flagged` propagated at `src/lessons_forge.py:649`. |
| 8 | No schema drift — canonical schemas match `src/db.py` DDL | **PASS** | canonical (read-only) vs `src/db.py` | Both `lesson_entries` and `lesson_proposals` schemas match. `route` column present, `reference` in status CHECK. No delta. |

## Raw Full-Suite Output

```
$ python3 -m pytest src/ -v
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
cachedir: .pytest_cache
rootdir: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/204
plugins: anyio-4.12.1, xdist-3.8.0, timeout-2.4.0, cov-7.0.0
collecting ... collected 61 items

src/test_lessons_forge.py::test_lesson_entries_schema PASSED             [  1%]
src/test_lessons_forge.py::test_lesson_proposals_schema PASSED           [  3%]
src/test_lessons_forge.py::test_check_constraints_reject_invalid PASSED  [  4%]
src/test_lessons_forge.py::test_parse_lessons_md_basic PASSED            [  6%]
src/test_lessons_forge.py::test_parse_lessons_md_tags PASSED             [  8%]
src/test_lessons_forge.py::test_parse_lessons_md_archived_stop PASSED    [  9%]
src/test_lessons_forge.py::test_parse_lessons_md_hash_deterministic PASSED [ 11%]
src/test_lessons_forge.py::test_ingest_fresh_insert PASSED               [ 13%]
src/test_lessons_forge.py::test_ingest_unchanged_noop PASSED             [ 14%]
src/test_lessons_forge.py::test_ingest_updated_entry PASSED              [ 16%]
src/test_lessons_forge.py::test_ingest_stale_proposals PASSED            [ 18%]
src/test_lessons_forge.py::test_get_unclassified_entries PASSED          [ 19%]
src/test_lessons_forge.py::test_insert_proposal_basic PASSED             [ 21%]
src/test_lessons_forge.py::test_insert_proposal_minimal_fields PASSED    [ 22%]
src/test_lessons_forge.py::test_detect_duplicates_empty_list PASSED      [ 24%]
src/test_lessons_forge.py::test_detect_duplicates_no_match PASSED        [ 26%]
src/test_lessons_forge.py::test_detect_duplicates_tag_match PASSED       [ 27%]
src/test_lessons_forge.py::test_detect_duplicates_heading_match PASSED   [ 29%]
src/test_lessons_forge.py::test_detect_duplicates_first_match_wins PASSED [ 31%]
src/test_lessons_forge.py::test_detect_duplicates_tag_substring_not_flagged PASSED [ 32%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_fresh PASSED      [ 34%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_with_duplicates PASSED [ 36%]
src/test_lessons_forge.py::test_run_full_lessons_cycle_idempotent PASSED [ 37%]
src/test_lessons_forge.py::test_needs_classification_excludes_dispositioned_entry PASSED [ 39%]
src/test_lessons_forge.py::test_needs_classification_includes_stale_only_entry PASSED [ 40%]
src/test_lessons_forge.py::test_needs_classification_plus_duplicates_equals_total PASSED [ 42%]
src/test_lessons_forge.py::test_generate_lessons_report_empty PASSED     [ 44%]
src/test_lessons_forge.py::test_generate_lessons_report_multi_category PASSED [ 45%]
src/test_lessons_forge.py::test_generate_lessons_report_writes_file PASSED [ 47%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[codify] PASSED [ 49%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[backlog] PASSED [ 50%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[reference] PASSED [ 52%]
src/test_lessons_forge.py::test_insert_proposal_route_none_default PASSED [ 54%]
src/test_lessons_forge.py::test_insert_proposal_invalid_route_raises PASSED [ 55%]
src/test_lessons_forge.py::test_route_check_constraint_rejects_invalid_sql PASSED [ 57%]
src/test_lessons_forge.py::test_migration_idempotence_double_init PASSED [ 59%]
src/test_lessons_forge.py::test_migration_adds_route_to_pre_existing_db PASSED [ 60%]
src/test_lessons_forge.py::test_set_proposal_route_persists PASSED       [ 62%]
src/test_lessons_forge.py::test_set_proposal_route_invalid_raises PASSED [ 63%]
src/test_lessons_forge.py::test_report_renders_route_where_present PASSED [ 65%]
src/test_lessons_forge.py::test_reference_status_migration_idempotence PASSED [ 67%]
src/test_lessons_forge.py::test_reference_status_migration_pre_existing_db PASSED [ 68%]
src/test_lessons_forge.py::test_reference_status_check_accepts_reference PASSED [ 70%]
src/test_lessons_forge.py::test_reference_status_check_still_rejects_invalid PASSED [ 72%]
src/test_lessons_forge.py::test_reference_status_migration_preserves_row_count PASSED [ 73%]
src/test_lessons_forge.py::test_overlap_recent_match PASSED              [ 75%]
src/test_lessons_forge.py::test_overlap_old_not_surfaced PASSED          [ 77%]
src/test_lessons_forge.py::test_overlap_non_overlapping PASSED           [ 78%]
src/test_lessons_forge.py::test_overlap_advisory_only_no_writes PASSED   [ 80%]
src/test_lessons_forge.py::test_report_renders_overlap_advisory PASSED   [ 81%]
src/test_lessons_forge.py::test_report_no_overlap_unchanged PASSED       [ 83%]
src/test_lessons_forge.py::test_overlap_131_135_shape PASSED             [ 85%]
src/test_lessons_forge.py::test_hash_trailing_separator_invariant PASSED [ 86%]
src/test_lessons_forge.py::test_hash_substantive_edit_changes_hash PASSED [ 88%]
src/test_lessons_forge.py::test_raw_content_stored_verbatim_with_separator PASSED [ 90%]
src/test_lessons_forge.py::test_terminal_status_guard[implemented] PASSED [ 91%]
src/test_lessons_forge.py::test_terminal_status_guard[reference] PASSED  [ 93%]
src/test_lessons_forge.py::test_terminal_status_guard[rejected] PASSED   [ 95%]
src/test_lessons_forge.py::test_terminal_status_guard[superseded] PASSED [ 96%]
src/test_lessons_forge.py::test_nonterminal_still_stales PASSED          [ 98%]
src/test_lessons_forge.py::test_trailing_separator_only_delta_zero_stales PASSED [100%]

============================== 61 passed in 0.28s ==============================
```

## Raw Canonical DB Queries

### Proposal status distribution
```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY status;"
implemented|97
reference|2
rejected|15
stale|3
superseded|28
```

### Unclassified entries (work list)
```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT le.id FROM lesson_entries le LEFT JOIN lesson_proposals lp ON le.id = lp.entry_id \
   WHERE lp.id IS NULL OR lp.status IN ('proposed', 'ambiguous') GROUP BY le.id ORDER BY le.id;"
138
139
140
```

### Entry 137 raw_content trailing bytes (hex)
```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT substr(raw_content, length(raw_content)-20) FROM lesson_entries WHERE id=137;" | xxd | tail -5
00000000: 722d 6469 7363 6970 6c69 6e65 600a 0a0a  r-discipline`...
00000010: 2d2d 2d0a 0a0a                           ---...
```

### Canonical lesson_entries schema
```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".schema lesson_entries"
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
CREATE INDEX idx_lesson_entries_source ON lesson_entries(source_file);
CREATE INDEX idx_lesson_entries_date ON lesson_entries(entry_date);
CREATE INDEX idx_lesson_entries_hash ON lesson_entries(content_hash);
```

### Canonical lesson_proposals schema
```
$ sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".schema lesson_proposals"
CREATE TABLE IF NOT EXISTS "lesson_proposals" (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_id            INTEGER NOT NULL REFERENCES lesson_entries(id) ON DELETE CASCADE,
    category            TEXT    NOT NULL CHECK(category IN ('structural','instrumentation','governance_rule','language','narrative','duplicate')),
    subcategory         TEXT,
    suggested_action    TEXT    NOT NULL,
    reasoning           TEXT    NOT NULL,
    confidence          TEXT    NOT NULL CHECK(confidence IN ('low','medium','high')),
    status              TEXT    NOT NULL DEFAULT 'proposed' CHECK(status IN ('proposed','accepted','rejected','ambiguous','stale','superseded','implemented','reference')),
    target_layer        TEXT    CHECK(target_layer IS NULL OR target_layer IN ('structure','governance','language','none')),
    target_artifact     TEXT,
    duplicate_of        INTEGER,
    route               TEXT    CHECK(route IS NULL OR route IN ('codify','backlog','reference')),
    proposed_at         TEXT    NOT NULL,
    status_updated_at   TEXT,
    status_updated_by   TEXT    CHECK(status_updated_by IS NULL OR status_updated_by IN ('planner','ceo','auto'))
);
CREATE INDEX idx_lesson_proposals_entry ON lesson_proposals(entry_id);
CREATE INDEX idx_lesson_proposals_status ON lesson_proposals(status);
CREATE INDEX idx_lesson_proposals_category ON lesson_proposals(category);
```

Both schemas match `src/db.py` DDL exactly. The `route` column (plan 128) and `reference` status CHECK value (plan 135) are present in both — expected, not a delta.

## Rule 20 — QA Self-Check Results

**PASSED — SELF-CHECK PASSED**

## Output Receipt

| Field | Value |
|---|---|
| Status | **Complete** |
| Plan | 204 Step 3 (QA) |
| Full suite | 61 passed, 0 failures (baseline 52 + 9 new) |
| Corpus integrity | implemented=97, stale=3 — pre-corruption baseline restored |
| All 8 verification rows | PASS |
| Blockers | None |

### Ledger Updates

#### Project Status

Root cause of the duplicate-proposal loop fixed: whitespace-only hash flips from trailing markdown separators no longer stale proposals (`_normalize_for_hash` strips trailing separators before hashing). Terminal statuses (implemented, rejected, superseded, reference) are independently guarded from stale demotion. 83 entry hashes backfilled to normalized form without touching any proposal. Proposal 145 (entry 137) restored to `implemented`. Corpus integrity verified: `implemented=97, stale=3` matches pre-corruption baseline. Work list is exactly `[138, 139, 140]` — the three genuine new entries from cycle 203, ready for re-dispatch. Proposals 98/121/130 audit complete (Step 2 Task E) — pending CEO Gate 1 decision.

#### Prompt Feedback

None — execution followed plan precisely.
