# QA Report — Gate-1 Routing Write for Proposals 327–332

**Plan:** `gate1-write-327-332-2026-08-12-qa-corrective`
**Step:** 1 — QA (the only step)
**Date:** 2026-08-12
**Executor:** A0 (Bellows agent, plan 362)

## Verification Table

| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |
|---|-------|---------------|----------------|-----------|----------|
| 1 | Routes landed (per-id readback) | ✅ | 327/328/329/330/332 `accepted\|codify\|ceo\|2026-08-12T17:12:07Z`; 331 `reference\|backlog\|ceo\|2026-08-12T17:12:07Z` | `SELECT id,category,status,route,status_updated_by,status_updated_at FROM lesson_proposals WHERE id IN (327..332)` | routing-readback.txt |
| 2 | Blast radius (outside-range capture) | ✅ | 326 lines; diff vs deposited: empty; no impossible-id, no deleted-row, no concurrent changes | `SELECT id,status,route,status_updated_at FROM lesson_proposals WHERE id<=332 AND id NOT IN (327..332)` | db-invariants.txt, outside-range-ids.txt |
| 3 | Corpus shape | ✅ | ACCEPTED_CODIFY=5, PROPOSED=0, REFERENCE_STATUS=16, REF_ROUTE_REFERENCE=9, REF_ROUTE_BACKLOG=7, STALE=3 (98/121/130), TOTAL=332 | per-status/route COUNT queries | db-invariants.txt |
| 4 | Tests (single-module, baseline 55/0) | ✅ | 55 passed, 0 failed (delta: 0) | `python3 -m pytest src/ -v` foreground | pytest_targeted.txt |
| 5 | Consumer semantics | ✅ | UNCLASSIFIED=0; ENTRIES_319_324=6; ENTRY318_HASH=`260857bbc71e818b74f503f2984f2b6e5c2854e84e97e4522f9e74b2ccdd0cb8` (matches) | `get_unclassified_entries` equivalent + entry hash query | db-invariants.txt |

## Evidence and Narrative

All five verification rows pass. The Gate-1 routing write landed atomically — five proposals routed to `accepted|codify` and one to `reference|backlog`, with no blast-radius impact on the remaining 326 rows. The corpus shape matches every predicted count including the route split (9 reference + 7 backlog). The test suite is stable at 55/0. Consumer semantics confirm no entries were un-classified by the routing write and the entry-318 hash sentinel is intact.

**Evidence files:**
- `routing-readback.txt` — fresh per-id readback (diff vs step-1 deposited: empty)
- `db-invariants.txt` — blast radius diff, corpus shape counts, consumer semantics
- `outside-range-ids.txt` — fresh 326-line capture (diff vs step-1 deposited: empty)
- `pytest_targeted.txt` — pytest output (55 passed, 0 failed)

## Receipt

### Sentinel Summary
All five QA rows verified with raw evidence deposited.

### Ledger Updates

#### Prompt Feedback
NONE

#### Forward Register
NONE

### Rule 20 Self-Check

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/362/knowledge/qa/evidence/gate1-write-327-332-2026-08-12/
Files verified: 4
```
