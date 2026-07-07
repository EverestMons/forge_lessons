# Gate 1 Route Disposition QA — Cycle 2026-07-06

## Verification Table

All queries ran against the canonical DB via read-only URI: `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro"`.

| # | Claim | Query | Expected | Actual | DB Source | Result |
|---|---|---|---|---|---|---|
| 1 | All `status='proposed'` rows have non-NULL `route`; count = 15 | `SELECT COUNT(*), SUM(CASE WHEN route IS NOT NULL THEN 1 ELSE 0 END) FROM lesson_proposals WHERE status='proposed'` | 15 total, 15 routed | 15 total, 15 routed | canonical DB (read-only URI) | PASS |
| 2 | Route counts: codify=13, reference=2, backlog=0 | `SELECT route, COUNT(*) FROM lesson_proposals WHERE status='proposed' GROUP BY route` | codify=13, reference=2 | codify=13, reference=2 | canonical DB (read-only URI) | PASS |
| 3 | Per-entry routes match CEO disposition table exactly | `SELECT id, entry_id, route FROM lesson_proposals WHERE status='proposed' ORDER BY entry_id` | See per-row check below | All 15 match — 0 mismatches | canonical DB (read-only URI) | PASS |
| 4 | No collateral writes: rows with `status != 'proposed'` AND `route IS NOT NULL` = 0 | `SELECT COUNT(*) FROM lesson_proposals WHERE status != 'proposed' AND route IS NOT NULL` | 0 | 0 | canonical DB (read-only URI) | PASS |
| 5 | Targeted tests pass in isolation | `python3 -m pytest` (4 tests, see below) | 4 passed | 4 passed | temp-DB (pytest fixtures) | PASS |

### Check 3 — Per-Entry Route Detail

| entry_id | proposal_id | Expected Route | Actual Route | Match |
|---|---|---|---|---|
| 123 | 131 | codify | codify | YES |
| 124 | 132 | codify | codify | YES |
| 125 | 133 | codify | codify | YES |
| 126 | 134 | codify | codify | YES |
| 127 | 135 | codify | codify | YES |
| 128 | 136 | codify | codify | YES |
| 129 | 137 | codify | codify | YES |
| 130 | 138 | codify | codify | YES |
| 131 | 139 | codify | codify | YES |
| 132 | 140 | reference | reference | YES |
| 133 | 141 | reference | reference | YES |
| 134 | 142 | codify | codify | YES |
| 135 | 143 | codify | codify | YES |
| 136 | 144 | codify | codify | YES |
| 137 | 145 | codify | codify | YES |

Mismatches: **0**

### Check 5 — Targeted Test Output

Tests ran against temp-DB fixtures (not canonical DB):

```
src/test_lessons_forge.py::test_migration_idempotence_double_init PASSED [ 25%]
src/test_lessons_forge.py::test_migration_adds_route_to_pre_existing_db PASSED [ 50%]
src/test_lessons_forge.py::test_set_proposal_route_persists PASSED       [ 75%]
src/test_lessons_forge.py::test_set_proposal_route_invalid_raises PASSED [100%]

4 passed in 0.10s
```

---

## Rule 20 — QA Self-Check Results

- Verification table present with per-row DB-source declarations: YES
- All 5 checks executed and passed: YES
- Per-entry route detail table with 15 rows, 0 mismatches: YES
- Targeted test output included with temp-DB label: YES
- Rule 20 banner present in this document: YES

**PASSED — SELF-CHECK PASSED**

---

### Output Receipt

- **Status:** COMPLETE
- **Scope:** 15 proposals (entries 123-137), all routes verified against CEO disposition table
- **Checks:** 5/5 passed — row count, route counts, per-entry match, collateral-write absence, targeted tests
- **DB:** canonical `lessons-forge.db` (read-only URI) for checks 1-4; temp-DB fixtures for check 5

### Ledger Updates

#### Project Status

Gate 1 route dispositions verified against the canonical DB: 15/15 proposals routed (13 codify, 2 reference), all matching the CEO disposition table with zero mismatches. No collateral writes detected. Targeted tests (migration idempotence, route-to-pre-existing-DB migration, `set_proposal_route` persistence and validation) all pass.

#### Prompt Feedback

No prompt feedback to report. The evidence-source rule (read-only URI to canonical DB from any working directory) and Rule 20 self-check requirements were clear and followed without issue.
