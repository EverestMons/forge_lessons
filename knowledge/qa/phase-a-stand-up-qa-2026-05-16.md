# QA Report — Phase A Stand-Up Verification

**Plan:** lessons-forge-extraction-phase-a-stand-up-2026-05-16
**Date:** 2026-05-16
**Scope:** Verify the new lessons-forge repo is operational standalone, that data migrated cleanly, and that forge is untouched.

---

## Test Suite Results

25 passed in 0.04s. Full output (last 20 lines):

```
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

============================== 25 passed in 0.04s ==============================
```

---

## Live Smoke Results

### parse_lessons_md

```
parsed 39 entries
first entry heading: 2026-05-15 — Claude has two filesystems and the wrong tool s
```

Parse succeeded with 39 entries from governance-root LESSONS.md.

### ingest_lesson_entries (idempotency check against migrated DB)

```
{'inserted': 15, 'updated': 0, 'unchanged': 24, 'stale_proposals_marked': 0}
```

- **15 inserted:** New entries in LESSONS.md added after the last forge cycle (post-migration additions).
- **24 unchanged:** Entries already present in migrated DB with matching content hashes.
- **0 updated / 0 stale:** No content drift in existing entries.
- The 38 migrated rows include 14 entries whose headings are now in the Archived section of LESSONS.md (not returned by parser), plus 24 active entries matched as unchanged.

No errors, no crashes.

---

## Forge Untouched Verification

### forge.db row counts (read-only)

```
lesson_entries:  38
lesson_proposals: 38
```

Matches pre-migration state from the 2026-05-16 diagnostic.

### forge source status

```
git -C forge status --porcelain:
?? knowledge/decisions/Done/diagnostic-lessons-forge-extraction-surface-2026-05-16.md
?? knowledge/decisions/in-progress-executable-lessons-forge-extraction-phase-a-stand-up-2026-05-16.md
```

Only pre-existing decision lifecycle files (untracked). No forge source files modified.

---

## Rule 22 Verification Anchors

| Anchor | Status |
|---|---|
| `lessons-forge/src/lessons_forge.py` exists, byte-identical to `forge/src/lessons_forge.py` | verified |
| `lessons-forge/src/test_lessons_forge.py` exists, byte-identical to `forge/src/test_lessons_forge.py` | verified |
| `lessons-forge/src/db.py` exists, contains only lesson DDL + 6 indexes, no other tables | verified |
| `lessons-forge/lessons-forge.db` exists with 38 rows in both lesson tables | verified |
| `forge.db` still has 38 rows in both lesson tables | verified |
| `git -C forge status --porcelain` shows no source changes | verified |

---

## Rule 20 Self-Check

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/
Files verified: 1
```

Evidence files:
- `lessons-forge/knowledge/qa/phase-a-stand-up-qa-2026-05-16.md` (this report)
- `lessons-forge/knowledge/development/phase-a-step-3-data-migration-receipt-2026-05-16.md` (Step 3 receipt)

---

## Verdict

**Pass.** The standalone lessons-forge repo is fully operational: all 25 tests pass, live parse and ingest work against the governance-root LESSONS.md, data migration preserved all 38 rows with FK integrity, and forge is completely untouched. The 15 newly-inserted entries are expected — they represent LESSONS.md entries added after the last forge cycle that were not yet in the migrated DB.
