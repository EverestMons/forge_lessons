# QA Report — Route Column on `lesson_proposals` (v2 — Corrected Verification)

**Date:** 2026-07-06
**Plan:** executable-130 (route-field-qa-correction)
**Supersedes:** Verification row 1 of `knowledge/qa/route-field-lesson-proposals-qa-2026-07-06.md`

---

This report supersedes verification row 1 of `knowledge/qa/route-field-lesson-proposals-qa-2026-07-06.md` (plan 128). That report presented a fresh-`init_db()` throwaway-DB PRAGMA as canonical-DB evidence without disclosing the distinction. The canonical `lessons-forge.db` at `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` does not yet contain the `route` column — which is correct behavior, not a defect: the guarded migration fires when `init_db()` next runs against the canonical DB (at cycle start), and nothing writes routes before a cycle. The original QA report is retained on disk as history; this report corrects the record with properly sourced evidence.

---

## Verification Table

| # | Claim | DB Source | Result | Evidence |
|---|---|---|---|---|
| 1 | `PRAGMA table_info(lesson_proposals)` on canonical DB — `route` column status | Canonical DB via read-only URI: `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro` | **PASS** | Column `route` is **ABSENT**. PRAGMA returned 13 columns (indices 0–12): `id`, `entry_id`, `category`, `subcategory`, `suggested_action`, `reasoning`, `confidence`, `status`, `target_layer`, `target_artifact`, `duplicate_of`, `proposed_at`, `status_updated_at`, `status_updated_by`. This is EXPECTED: the guarded migration fires at the next `init_db()` run against this DB (cycle start); nothing writes routes before a cycle, so absent-now is correct behavior, not a defect. |
| 2 | Fresh throwaway temp DB via `init_db()` shows `route` column with CHECK constraint | Throwaway temp DB (created in `tempfile.mkdtemp()`, destroyed after test) | **PASS** | `route` column present at index 11: `(11, 'route', 'TEXT', 0, None, 0)` — nullable TEXT. CHECK constraint rejects invalid values: `INSERT … route='INVALID'` raised `CHECK constraint failed: route IS NULL OR route IN ('codify', 'backlog', 'reference')`. DDL and migration-path proof confirmed. |
| 3 | Migration tests pass in isolation | Throwaway temp DBs (pytest fixtures) | **PASS** | `test_migration_idempotence_double_init` and `test_migration_adds_route_to_pre_existing_db` both passed (2/2, 0.09s). Migration uses PRAGMA `table_info` gate — fires only when `route` column absent. |
| 4 | Full suite green | Throwaway temp DBs (pytest fixtures) | **PASS** | `python3 -m pytest src/ -v` → `40 passed in 0.17s` — all 29 pre-existing + 11 new tests passed. |

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

============================== 40 passed in 0.17s ==============================
```

---

## Rule 20 — QA Self-Check Results

| # | Check | Result |
|---|---|---|
| 1 | Canonical DB queried via absolute-path read-only URI (not throwaway/temp) | PASS |
| 2 | Every verification row states which DB it ran against | PASS |
| 3 | All 4 verification rows evaluated | PASS |
| 4 | No verification row marked FAIL | PASS |
| 5 | Full suite executed to explicit pass/fail | PASS |
| 6 | QA report deposited at correct path | PASS |

PASSED — SELF-CHECK PASSED

---

### Ledger Updates

#### Project Status

Route-column verification corrected 2026-07-06. The original QA report (plan 128) presented a fresh-`init_db()` throwaway PRAGMA as canonical-DB evidence without disclosure; this v2 report corrects the record. The canonical DB at `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` correctly lacks the `route` column — the guarded migration fires at the next `init_db()` run (cycle start) by design. Nothing writes routes before a cycle, so column absence is expected behavior. The dev deliverable (commit `643e9e7`) is confirmed sound: fresh `init_db()` produces the column with proper CHECK constraint, migration tests pass, and the full suite (40/40) is green.

#### Prompt Feedback

Plan 130 instructions were precise and corrective. The evidence-source rule requiring each PRAGMA row to state which DB it ran against is an effective safeguard against the disclosure gap in the original report.

---

## Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Verification** | 4/4 rows PASS |
| **Tests** | 40/40 passed |
| **Blockers** | None |
