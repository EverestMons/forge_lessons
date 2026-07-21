# Gate 1 Route Disposition — Dev Log (cycle 2026-07-21)

**Plan:** 248 | **Step:** 1 (DEV) | **Date:** 2026-07-21

---

## Task A00 — Restore Point

Backup taken via SQLite `.backup` command (WAL-safe):

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  ".backup '/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-20260721T230444Z.db'"
```

**Backup path:** `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-20260721T230444Z.db`
**Size:** 798720 bytes (verified non-empty via `ls -la`).
**Gitignored:** confirmed — `git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain` shows no backup file.

---

## Task A0 — Isolation Pre-flight

**Main-tree decisions listing** (`ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/`):
- Only `in-progress-executable-248.md` matched `in-progress-*` or `verdict-pending-*`.
- **Positive signal:** own plan file present as `in-progress-executable-248.md`. ✓

**Stability re-read:** status distribution and route-NOT-NULL count read twice ~1 second apart — both identical. No concurrent writer.

### Before-Snapshots (captured pre-write)

**Status distribution:**
```
implemented: 110
superseded:   28
rejected:     15
proposed:     12
reference:     3
stale:         3
TOTAL:       171
```
Matches authoring-time expectation exactly.

**Route-NOT-NULL count:** 29 (matches authoring-time expectation).

### Precondition Check

All 12 proposals (id 160–171) verified:

```
id=160, entry_id=152, status=proposed, route=None
id=161, entry_id=153, status=proposed, route=None
id=162, entry_id=154, status=proposed, route=None
id=163, entry_id=155, status=proposed, route=None
id=164, entry_id=156, status=proposed, route=None
id=165, entry_id=157, status=proposed, route=None
id=166, entry_id=158, status=proposed, route=None
id=167, entry_id=159, status=proposed, route=None
id=168, entry_id=160, status=proposed, route=None
id=169, entry_id=161, status=proposed, route=None
id=170, entry_id=162, status=proposed, route=None
id=171, entry_id=163, status=proposed, route=None
```

- id→entry_id mapping: correct (160→152 through 171→163, contiguous). ✓
- All statuses: `proposed` (fresh run). ✓
- All routes: `NULL` (fresh run). ✓

---

## Task A — Route Assignment

Called `set_proposal_route(conn, proposal_id, route)` from `src.lessons_forge`:

```python
set_proposal_route(conn, 160, 'codify')
set_proposal_route(conn, 162, 'codify')
set_proposal_route(conn, 163, 'codify')
set_proposal_route(conn, 165, 'codify')
set_proposal_route(conn, 166, 'codify')
set_proposal_route(conn, 167, 'codify')
set_proposal_route(conn, 168, 'codify')
set_proposal_route(conn, 170, 'codify')
set_proposal_route(conn, 171, 'codify')
set_proposal_route(conn, 164, 'reference')
set_proposal_route(conn, 161, 'backlog')
set_proposal_route(conn, 169, 'backlog')
```

9 codify, 1 reference, 2 backlog — matches disposition table.

---

## Task A2 — Status Changes (hand-written SQL)

Exact SQL executed:

```sql
UPDATE lesson_proposals
SET status = 'reference', status_updated_by = 'ceo', status_updated_at = '2026-07-21T23:05:25Z'
WHERE id IN (161, 164, 169)
```

Parameterised via `conn.execute(sql, ('reference', 'ceo', '2026-07-21T23:05:25Z', 161, 164, 169))`.

**Single `conn.commit()` issued after BOTH Task A and Task A2** — routes and statuses landed atomically.

---

## Task B — Post-state Verification

### B1 — Absolute Target Distribution

```
implemented: 110
superseded:   28
rejected:     15
proposed:      9
reference:     6
stale:         3
TOTAL:       171
```

Matches target exactly. ✓

### B2 — Delta Cross-check (fresh run)

A0 showed `proposed 12 / reference 3` → fresh run.

```
proposed delta:     -3 (expected -3) ✓
reference delta:    +3 (expected +3) ✓
implemented delta:   0 (expected  0) ✓
superseded delta:    0 (expected  0) ✓
rejected delta:      0 (expected  0) ✓
stale delta:         0 (expected  0) ✓
```

### B2 — Read-back of All 12 Proposals (raw output)

```
id=160, entry_id=152, status=proposed,  route=codify
id=161, entry_id=153, status=reference, route=backlog
id=162, entry_id=154, status=proposed,  route=codify
id=163, entry_id=155, status=proposed,  route=codify
id=164, entry_id=156, status=reference, route=reference
id=165, entry_id=157, status=proposed,  route=codify
id=166, entry_id=158, status=proposed,  route=codify
id=167, entry_id=159, status=proposed,  route=codify
id=168, entry_id=160, status=proposed,  route=codify
id=169, entry_id=161, status=reference, route=backlog
id=170, entry_id=162, status=proposed,  route=codify
id=171, entry_id=163, status=proposed,  route=codify
```

Every row matches the disposition table on both columns. Nine `codify` rows retain `status=proposed`. Three terminal rows (161, 164, 169) show `status=reference` with `status_updated_by=ceo` and `status_updated_at=2026-07-21T23:05:25Z`. ✓

---

## Task C — Blast Radius

| Metric | Before | After | Delta | Max Allowed | Result |
|---|---|---|---|---|---|
| route-NOT-NULL count | 29 | 41 | +12 | +12 | ✓ |
| status='reference' count | 3 | 6 | +3 | +3 | ✓ |
| total proposals | 171 | 171 | 0 | 0 | ✓ |
| route-NOT-NULL for id < 160 | 29 | 29 | 0 | 0 | ✓ |
| status='reference' for id < 160 | 3 | 3 | 0 | 0 | ✓ |

No rows outside 160–171 were affected. ✓

---

### Ledger Updates

#### Prompt Feedback

No new prompt feedback to record from this step. The plan's Task A00/A0/A/A2/B/C structure executed cleanly; the single-commit discipline for Task A + A2 was well-motivated and straightforward to implement.

---

## Output Receipt

- **Status:** Complete
- **Plan:** 248, Step 1 (DEV)
- **Scope Adherence:** No `src/` changes. No `PLANNER_TEMPLATE.md` changes. DB-only writes via `set_proposal_route` helper and parameterised SQL.
- **Files Created or Modified (Data):**
  - Canonical DB (`lessons-forge.db`): 12 routes set, 3 status changes (proposals 161/164/169 → `reference`)
- **Files Created (Deposits):**
  - `knowledge/development/gate-1-route-disposition-2026-07-21.md` (this file)
- **Files Created (Backups):**
  - `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-20260721T230444Z.db`
- **Verification:** All Task B and Task C checks pass.
