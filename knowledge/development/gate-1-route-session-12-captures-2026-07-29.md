# Gate 1 Route — Session 12 Captures (2026-07-29)

## Summary

Routed all 8 session-12 proposals (193–200) to `codify` via `set_proposal_route(conn, id, 'codify')`. Single transaction, single `conn.commit()`. No status changes. No code modifications.

## Task A — Route Writes

```
set_proposal_route(conn, 193, "codify") — done
set_proposal_route(conn, 194, "codify") — done
set_proposal_route(conn, 195, "codify") — done
set_proposal_route(conn, 196, "codify") — done
set_proposal_route(conn, 197, "codify") — done
set_proposal_route(conn, 198, "codify") — done
set_proposal_route(conn, 199, "codify") — done
set_proposal_route(conn, 200, "codify") — done
conn.commit() — done, all 8 routes written
```

## Task B1 — Read-Back (absolute, no before-anchor)

```
id   entry_id  status    route   category         target_artifact            
---  --------  --------  ------  ---------------  ---------------------------
193  185       proposed  codify  governance_rule  PLANNER_TEMPLATE.md        
194  186       proposed  codify  governance_rule  DRAFTING_CYCLE.md          
195  187       proposed  codify  governance_rule  DRAFTING_CYCLE.md          
196  188       proposed  codify  governance_rule  PLANNER_TEMPLATE.md        
197  189       proposed  codify  governance_rule  DRAFTING_CYCLE.md          
198  190       proposed  codify  instrumentation  DRAFTING_CYCLE.md          
199  191       proposed  codify  instrumentation  RULE_20_SELF_CHECK_BLOCK.md
200  192       proposed  codify  governance_rule  DRAFTING_CYCLE.md
```

All 8: `route='codify'`, `status='proposed'`, category and target_artifact match disposition table per row.

## Task B2 — Status Distribution (anchored to before-item (1))

```
implemented|137
superseded|28
rejected|15
proposed|10
reference|7
stale|3
```

Byte-identical to before-item (1). No status moved.

## Task B3 — Same-Instant Identity (anchored to before-item (2))

```
total_route_not_null|70
outside_range_route_not_null|62
```

Identity: 70 == 62 + 8. PASS.
Rise over before-item (2): 70 - 62 = 8 (equal to 8, within bound of <= 8).

## Task C2 — Outside-Range Count (anchored to before-item (4))

```
62
```

Unchanged from before-item (4) = 62. PASS.

## Task C3 — Unclassified Entries (anchored to before-item (3))

```
[]
```

Unchanged from before-item (3) = `[]`. PASS.

## Task C4 — Parked Pair (absolute, no before-anchor; compared to before-item (4b))

```
191|proposed|codify|DRAFTING_CYCLE.md
192|proposed|codify|PLANNER_TEMPLATE.md
```

Unchanged from before-item (4b). Both `status='proposed'`, `route='codify'`, target_artifacts unchanged. PASS.

## Output Receipt

Status: Complete

1. **Before-item (1) — status distribution (pre-write):**
```
implemented|137
superseded|28
rejected|15
proposed|10
reference|7
stale|3
```

2. **Before-item (2) — TOTAL route-NOT-NULL count (pre-write):** `62`

3. **Before-item (3) — get_unclassified_entries(conn) (pre-write):** `[]`

4. **Before-item (4) — OUTSIDE-RANGE route-NOT-NULL count (pre-write):** `62`

4b. **Before-item (4b) — parked pair row (pre-write):**
```
191|proposed|codify|DRAFTING_CYCLE.md
192|proposed|codify|PLANNER_TEMPLATE.md
```

5. **After-values:**
   - **B1** (absolute, no before-anchor): All 8 rows `route='codify'`, `status='proposed'`, categories and target_artifacts match disposition table per row. Raw output above.
   - **B2** (anchored to before-item (1)): Status distribution byte-identical to before-item (1). `proposed` still 10.
   - **B3** (anchored to before-item (2)): Same-instant identity 70 == 62 + 8. Rise over before-item (2) = 8 (within bound <= 8).
   - **C2** (anchored to before-item (4)): Outside-range count = 62, unchanged from before-item (4).
   - **C3** (anchored to before-item (3)): `get_unclassified_entries(conn)` = `[]`, unchanged from before-item (3).
   - **C4** (absolute, no before-anchor; compared to before-item (4b)): Parked pair 191/192 unchanged from before-item (4b). Both `proposed|codify`, target_artifacts unchanged.

6. **Backup path and verification:**
   - Path: `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-284-20260730T001726Z.db`
   - `PRAGMA integrity_check`: `ok`
   - Backup counts: `lesson_entries` 192, `lesson_proposals` 200
   - Live counts: `lesson_entries` 192, `lesson_proposals` 200
   - Counts match. Backup verified.

7. **No flags or HALT conditions encountered.**

#### Files Created or Modified

- `knowledge/development/gate-1-route-session-12-captures-2026-07-29.md`

### Ledger Updates

#### Prompt Feedback

No prompt feedback for this step.
