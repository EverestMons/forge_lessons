# Dev Log — Route Column on `lesson_proposals`

**Date:** 2026-07-06
**Plan:** executable-128 (route-field-lesson-proposals)
**Scope:** `src/db.py`, `src/lessons_forge.py`, `src/test_lessons_forge.py`

---

## Changes

### Change 1 — Schema (`src/db.py`)

Added `route TEXT CHECK(route IS NULL OR route IN ('codify', 'backlog', 'reference'))` to the `lesson_proposals` CREATE TABLE, positioned after `duplicate_of`.

**Migration approach:** Guarded `ALTER TABLE ADD COLUMN` inside `init_db()`, gated by `PRAGMA table_info` check — fires only when the `route` column is absent. Chose this over a separate migration file because `init_db()` already serves as the single schema-management entry point (no migration framework exists in this codebase). The ALTER TABLE includes the same CHECK constraint as the CREATE TABLE DDL. `init_db()` remains idempotent — the PRAGMA gate prevents double-add errors.

**Old:**
```python
conn.commit()
```

**New:**
```python
# Migration: add route column to existing DBs that lack it
cols = {row[1] for row in conn.execute("PRAGMA table_info(lesson_proposals)").fetchall()}
if "route" not in cols:
    conn.execute(
        "ALTER TABLE lesson_proposals ADD COLUMN "
        "route TEXT CHECK(route IS NULL OR route IN ('codify', 'backlog', 'reference'))"
    )

conn.commit()
```

### Change 2 — Insert Path (`src/lessons_forge.py`)

Added `route: str | None = None` parameter to `insert_proposal()`. Python-level validation raises `ValueError` before the DB is touched. The INSERT statement now includes the `route` column.

### Change 3 — Disposition Path (`src/lessons_forge.py`)

Added `set_proposal_route(conn, proposal_id, route)` — a small standalone helper. Chose this over extending an existing update helper because no generic `update_proposal()` helper exists; status updates happen via raw SQL in `ingest_lesson_entries`. A standalone function is the minimal-surface option (6 lines). Same three-value-or-None validation via `_VALID_ROUTES` frozenset shared with `insert_proposal()`.

### Change 4 — Report (`src/lessons_forge.py`)

Extended the SELECT in `generate_lessons_report()` to include `p.route`. The per-proposal rendering adds `- **Route:** {route}` only when `route is not None` — NULL rows render without it (no placeholder noise).

### Change 5 — Tests (`src/test_lessons_forge.py`)

| Test Name | Rationale |
|---|---|
| `test_insert_proposal_with_valid_route[codify]` | Insert with valid route persists and reads back |
| `test_insert_proposal_with_valid_route[backlog]` | (parametrized — same for each valid value) |
| `test_insert_proposal_with_valid_route[reference]` | (parametrized) |
| `test_insert_proposal_route_none_default` | Omitting route keyword leaves NULL |
| `test_insert_proposal_invalid_route_raises` | Invalid route raises ValueError at Python layer |
| `test_route_check_constraint_rejects_invalid_sql` | Direct SQL with invalid value rejected by CHECK |
| `test_migration_idempotence_double_init` | init_db() twice on one DB does not error |
| `test_migration_adds_route_to_pre_existing_db` | init_db() on pre-route schema adds the column |
| `test_set_proposal_route_persists` | Disposition-path route set persists and can be updated/cleared |
| `test_set_proposal_route_invalid_raises` | Invalid value on disposition path raises ValueError |
| `test_report_renders_route_where_present` | Route appears in report only for non-NULL proposals |

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

============================== 40 passed in 0.24s ==============================
```

**Commit:** `643e9e7` — `feat(lessons-forge): route column on lesson_proposals — routing outcome capture [128]`

---

### Ledger Updates

#### Prompt Feedback

No prompt feedback to report this step. Execution was straightforward — plan instructions were clear and matched actual code shape.

---

## Output Receipt

| Field | Value |
|---|---|
| **Status** | Complete |
| **Tests** | 40/40 passed (29 pre-existing unchanged + 11 new) |
| **Files Modified** | `src/db.py`, `src/lessons_forge.py`, `src/test_lessons_forge.py` |
| **Commit** | `643e9e7` |
| **Blockers** | None |
