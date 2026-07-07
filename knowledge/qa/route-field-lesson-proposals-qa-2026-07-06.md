# QA Report — Route Column on `lesson_proposals`

**Date:** 2026-07-06
**Plan:** executable-128 (route-field-lesson-proposals)
**Dev Log:** `knowledge/development/route-field-lesson-proposals-2026-07-06.md`
**Dev Log Status:** Complete

---

## Verification Table

| # | Claim | Result | Evidence |
|---|---|---|---|
| 1 | `PRAGMA table_info(lesson_proposals)` shows `route` column | **PASS** | Column at index 11: `(11, 'route', 'TEXT', 0, None, 0)` — nullable TEXT, no default, no NOT NULL |
| 2 | CHECK constraint rejects invalid route value | **PASS** | Direct SQL INSERT with `route='INVALID'` on throwaway temp DB raised: `CHECK constraint failed: route IS NULL OR route IN ('codify', 'backlog', 'reference')` |
| 3 | `insert_proposal()` accepts `route` keyword; existing call sites unchanged | **PASS** | Signature: `def insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, status='proposed', target_layer=None, target_artifact=None, duplicate_of=None, subcategory=None, route=None)` — `route` is keyword-optional with default `None`. Production call site at `src/lessons_forge.py:443` (`insert_proposal()` in `run_full_lessons_cycle`'s duplicate-detection path) does not pass `route` — valid, uses default `None`. |
| 4 | Disposition-path route set exists and test passes in isolation | **PASS** | `set_proposal_route(conn, proposal_id, route)` at `src/lessons_forge.py:211` — standalone 6-line helper with `_VALID_ROUTES` validation. `test_set_proposal_route_persists` passed in isolation (1/1). |
| 5 | Migration idempotence tests pass in isolation | **PASS** | `test_migration_idempotence_double_init` and `test_migration_adds_route_to_pre_existing_db` both passed in isolation (2/2). Migration uses PRAGMA table_info gate — fires only when `route` column absent. |
| 6 | `generate_lessons_report()` renders route where present, no placeholder on NULL rows | **PASS** | At `src/lessons_forge.py:535-536`: `if route is not None: lines.append(f"- **Route:** {route}")` — conditional render, NULL rows skip entirely (no placeholder). |
| 7 | Pre-existing tests pass with assertions untouched — additions only | **PASS** | `git diff HEAD~1 -- src/test_lessons_forge.py` shows zero deletion lines (no `^-` lines excluding `^---` header). All changes are additions only. |
| 8 | Full suite green | **PASS** | `python3 -m pytest src/ -v` → `40 passed in 0.25s` — all 29 pre-existing + 11 new tests passed. |

---

## Full Suite Tail

```
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[codify] PASSED [ 75%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[backlog] PASSED [ 77%]
src/test_lessons_forge.py::test_insert_proposal_with_valid_route[reference] PASSED [ 80%]
src/test_lessons_forge.py::test_insert_proposal_route_none_default PASSED [ 82%]
src/test_lessons_forge.py::test_insert_proposal_invalid_route_raises PASSED [ 85%]
src/test_lessons_forge.py::test_route_check_constraint_rejects_invalid_sql PASSED [ 87%]
src/test_lessons_forge.py::test_migration_idempotence_double_init PASSED [ 90%]
src/test_lessons_forge.py::test_migration_adds_route_to_pre_existing_db PASSED [ 92%]
src/test_lessons_forge.py::test_set_proposal_route_persists PASSED       [ 95%]
src/test_lessons_forge.py::test_set_proposal_route_invalid_raises PASSED [ 97%]
src/test_lessons_forge.py::test_report_renders_route_where_present PASSED [100%]

============================== 40 passed in 0.25s ==============================
```

---

## Rule 20 — QA Self-Check Results

| # | Check | Result |
|---|---|---|
| 1 | Dev log Output Receipt status is Complete | PASS |
| 2 | All 8 verification rows evaluated | PASS |
| 3 | No verification row marked FAIL | PASS |
| 4 | Full suite executed to explicit pass/fail | PASS |
| 5 | QA report deposited at correct path | PASS |

PASSED — SELF-CHECK PASSED

---

### Ledger Updates

#### Project Status

Route column shipped 2026-07-06 (plan 128, commit `643e9e7`). The `lesson_proposals` table now captures routing outcomes via a nullable `route TEXT` column constrained to `codify`, `backlog`, or `reference`. Routes can be set at insert time (`insert_proposal(route=...)`) or at disposition time (`set_proposal_route()`). The report surfaces route values where present; historical rows remain NULL by design (pre-route history, no backfill). This closes gap 1 from diagnostic-127's learning-loop routing audit.

#### Prompt Feedback

No prompt feedback to report this step. Plan instructions were precise and verification proceeded without ambiguity.

---

## Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Verification** | 8/8 rows PASS |
| **Tests** | 40/40 passed |
| **Blockers** | None |
