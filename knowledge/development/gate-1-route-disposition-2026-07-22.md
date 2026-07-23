# Gate 1 Route Disposition — cycle 2026-07-22

**Plan:** executable-258 | **Step:** 1 (DEV) | **Date:** 2026-07-23

## Task A00 — Restore Point

Backup created via `.backup` (WAL-safe):

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  ".backup '/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-20260723T160735Z.db'"
```

**Backup path:** `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-20260723T160735Z.db`
**Size:** 835584 bytes | **Exit code:** 0 | **Git status:** gitignored (confirmed absent from `git status --porcelain`)

## Task A0 — Isolation Pre-flight + Preconditions

### Isolation

- `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/` shows `in-progress-executable-258.md` (positive signal) and no other `in-progress-*` or `verdict-pending-*` files.
- Quiescence: two reads a moment apart both returned identical status distribution and route-NOT-NULL count (41). No concurrent writer.

### Precondition: target rows

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 172 AND 186 ORDER BY id;"
```

```
172|164|proposed|
173|165|proposed|
174|166|proposed|
175|167|proposed|
176|168|proposed|
177|169|proposed|
178|170|proposed|
179|171|proposed|
180|172|proposed|
181|173|proposed|
182|174|proposed|
183|175|proposed|
184|176|proposed|
185|177|proposed|
186|178|proposed|
```

All fifteen present, contiguous id→entry_id mapping (172→164 through 186→178), all `status='proposed'`, all `route=NULL`. Precondition PASS.

### Before-snapshots (pre-write)

**Status distribution:**
```
implemented|119
superseded|28
proposed|15
rejected|15
reference|6
stale|3
```
Total: 186. Matches authoring-time expectation.

**Route-NOT-NULL count:** 41. Matches authoring-time expectation.

## Task A — Route Assignment

Connected read-write: `sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')`

Calls made via `set_proposal_route(conn, proposal_id, route)` from `src.lessons_forge`:

```python
set_proposal_route(conn, 172, 'codify')
set_proposal_route(conn, 173, 'codify')
set_proposal_route(conn, 174, 'codify')
set_proposal_route(conn, 175, 'codify')
set_proposal_route(conn, 176, 'codify')
set_proposal_route(conn, 177, 'codify')
set_proposal_route(conn, 178, 'codify')
set_proposal_route(conn, 179, 'codify')
set_proposal_route(conn, 180, 'codify')
set_proposal_route(conn, 181, 'codify')
set_proposal_route(conn, 182, 'codify')
set_proposal_route(conn, 184, 'codify')
set_proposal_route(conn, 185, 'codify')
set_proposal_route(conn, 186, 'codify')
set_proposal_route(conn, 183, 'reference')
```

## Task A2 — Status Change (proposal 183)

Hand-written SQL (no status-setter exists in `src/lessons_forge.py`):

```sql
UPDATE lesson_proposals SET status=?, status_updated_by=?, status_updated_at=? WHERE id=183
-- Params: ('reference', 'ceo', '2026-07-23T16:08:21Z')
```

**Single `conn.commit()`** after both Task A and Task A2.

## Task B — Post-state Verification

### B1 — Status distribution (primary, resume-invariant)

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY COUNT(*) DESC;"
```

```
implemented|119
superseded|28
rejected|15
proposed|14
reference|7
stale|3
```

Total: 186. Matches target exactly: `proposed 14, reference 7, implemented 119, superseded 28, rejected 15, stale 3`. **PASS.**

### B2 — Fresh-run cross-check

A0 showed `proposed 15 / reference 6`. Post-write shows `proposed 14 / reference 7`.
Movement: `proposed -1`, `reference +1`. implemented/superseded/rejected/stale all unchanged. **PASS.**

Read-back of all fifteen rows:

```
sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
  "SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 172 AND 186 ORDER BY id;"
```

```
172|164|proposed|codify
173|165|proposed|codify
174|166|proposed|codify
175|167|proposed|codify
176|168|proposed|codify
177|169|proposed|codify
178|170|proposed|codify
179|171|proposed|codify
180|172|proposed|codify
181|173|proposed|codify
182|174|proposed|codify
183|175|reference|reference
184|176|proposed|codify
185|177|proposed|codify
186|178|proposed|codify
```

Fourteen rows: `route='codify'`, `status='proposed'`. One row (183): `route='reference'`, `status='reference'`. **PASS.**

## Task C — Blast Radius

1. **Read-back:** all fifteen rows confirmed above (Task B2).
2. **Route-NOT-NULL:** 56 (before: 41, rose by 15 — exactly 15 on clean run). **PASS.**
3. **`status='reference'` count:** 7 (before: 6, rose by 1). **PASS.**

---

### Output Receipt

| Field | Value |
|---|---|
| Plan | executable-258 |
| Step | 1 (DEV) |
| Status | **Complete** |
| Proposals routed | 15 (14 codify, 1 reference) |
| Status changes | 1 (proposal 183: proposed → reference) |
| DB backup | `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-20260723T160735Z.db` |
| Before status distribution | implemented 119, superseded 28, proposed 15, rejected 15, reference 6, stale 3 |
| After status distribution | implemented 119, superseded 28, proposed 14, rejected 15, reference 7, stale 3 |
| Route-NOT-NULL | 41 → 56 (+15) |
| Verification | B1 PASS, B2 PASS, C PASS |

### Ledger Updates

#### Prompt Feedback

The plan's Task A00 backup command, Task A0 precondition checks, and single-transaction discipline for Task A + Task A2 were well-structured and executed cleanly. The explicit quiescence check (two reads a moment apart) and the parameterised WHERE clause requirement for Task A2 are good safety guards. The backup-to-main-tree instruction correctly prevents worktree teardown data loss.
