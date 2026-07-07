# Reference Status Migration — DEV Deposit

**Plan:** 135 | **Date:** 2026-07-07 | **Author:** Forge DEV

---

## Migration Design

### Problem
Proposals 140 and 141 (reference-routed, cycle 2026-07-06) remained `status='proposed'` with `route='reference'` as an implicit terminal marker. The status CHECK constraint on `lesson_proposals` did not include `'reference'`, leaving `status='proposed'` ambiguous between "awaiting disposition" and "terminally reference-routed."

### Solution — Guarded Table Rebuild
SQLite cannot ALTER a CHECK constraint on an existing table. A table-rebuild migration adds `'reference'` to the status CHECK.

**Rebuild steps:**
1. Read `sqlite_master` SQL for `lesson_proposals`
2. Guard: if `'implemented', 'reference'` already present in the schema SQL, skip (idempotent — the string is unique to the status CHECK since `'reference'` also appears in the route CHECK)
3. `PRAGMA foreign_keys=OFF`
4. Create `lesson_proposals_new` with identical schema + `'reference'` in status CHECK
5. `INSERT INTO lesson_proposals_new SELECT * FROM lesson_proposals`
6. `DROP TABLE lesson_proposals`
7. `ALTER TABLE lesson_proposals_new RENAME TO lesson_proposals`
8. Recreate all three indexes
9. `PRAGMA foreign_keys=ON`
10. `conn.commit()`

**Guard condition:** `"'implemented', 'reference'" not in schema_sql` — matches the status CHECK uniquely (the route CHECK contains `'reference'` but not preceded by `'implemented',`).

**Files changed:**
- `src/db.py` — `CREATE TABLE` DDL updated (status CHECK includes `'reference'`), new migration block after route migration
- `src/lessons_forge.py` — `insert_proposal` docstring updated to list `reference` as valid status
- `src/test_lessons_forge.py` — 5 new tests added

---

## Test Additions

| Test | Purpose |
|---|---|
| `test_reference_status_migration_idempotence` | `init_db()` twice, no error, schema correct |
| `test_reference_status_migration_pre_existing_db` | Old schema (no `'reference'` in status CHECK) → rebuild adds it, data preserved |
| `test_reference_status_check_accepts_reference` | `INSERT` with `status='reference'` succeeds |
| `test_reference_status_check_still_rejects_invalid` | `INSERT` with `status='bogus_status'` still raises `IntegrityError` |
| `test_reference_status_migration_preserves_row_count` | 5 seeded rows survive rebuild with correct IDs |

---

## Canonical DB Application Evidence

**DB path:** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`

- Rebuild detected as needed: `True`
- Schema after migration: `'implemented', 'reference'` present in status CHECK
- UPDATE applied: `UPDATE lesson_proposals SET status='reference', status_updated_at='2026-07-07', status_updated_by='ceo' WHERE id IN (140,141) AND route='reference'`
- **Rows changed: 2**
- After update: `(140, 'reference', '2026-07-07', 'ceo', 'reference')`, `(141, 'reference', '2026-07-07', 'ceo', 'reference')`
- **`SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed'` → 0**

---

## Suite Tail

```
src/test_lessons_forge.py::test_reference_status_migration_idempotence PASSED [ 91%]
src/test_lessons_forge.py::test_reference_status_migration_pre_existing_db PASSED [ 93%]
src/test_lessons_forge.py::test_reference_status_check_accepts_reference PASSED [ 95%]
src/test_lessons_forge.py::test_reference_status_check_still_rejects_invalid PASSED [ 97%]
src/test_lessons_forge.py::test_reference_status_migration_preserves_row_count PASSED [100%]

============================== 45 passed in 0.18s ==============================
```

---

### Ledger Updates

#### Project Status

Reference terminal status is live: `'reference'` added to the `lesson_proposals.status` CHECK constraint via guarded table-rebuild migration. Proposals 140 and 141 (cycle 2026-07-06, entries 132/133) updated to `status='reference'`, `status_updated_by='ceo'`, `status_updated_at='2026-07-07'`. The `status='proposed'` backlog is now at 0, restoring its semantic meaning to exactly "awaiting disposition."

#### Prompt Feedback

No new prompt feedback generated during this step.

---

### Output Receipt

| Field | Value |
|---|---|
| Plan | 135 |
| Step | 1 (DEV) |
| Status | COMPLETE |
| Files changed | `src/db.py`, `src/lessons_forge.py`, `src/test_lessons_forge.py` |
| Deposit | `knowledge/development/reference-status-migration-2026-07-07.md` |
| Canonical DB | migrated + proposals 140/141 applied |
| Suite | 45 passed, 0 failed |
