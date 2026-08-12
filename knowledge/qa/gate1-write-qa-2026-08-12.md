# QA Report — Gate-1 Routing Write for Proposals 327–332

**Plan:** `gate1-write-327-332-2026-08-12`
**Step:** 2 — QA
**Date:** 2026-08-12
**Executor:** A0 (Bellows agent, plan 360)

## Deliverable Verification

| # | Check | Expected | Actual | Status |
|---|-------|----------|--------|--------|
| 1 | Routes landed (per-id readback) | 327/328/329/330/332 `accepted\|codify\|ceo` Z-stamped; 331 `reference\|backlog\|ceo` Z-stamped | All six match; fresh diff vs deposited readback: empty | ✅ |
| 2 | Blast radius (outside-range capture) | 326 lines, diff vs deposited empty | 326 lines, diff empty; no impossible-id, no deleted-row, no concurrent changes | ✅ |
| 3 | Corpus shape | `accepted\|codify`=5, `proposed`=0, `reference` status=16 (9 reference + 7 backlog), `stale`=3 (98/121/130), total=332 | ACCEPTED_CODIFY=5, PROPOSED=0, REFERENCE_STATUS=16, REF_ROUTE_REFERENCE=9, REF_ROUTE_BACKLOG=7, STALE=3 (98/121/130), TOTAL=332 | ✅ |
| 4 | Tests (single-module, baseline 55/0) | 55 passed, 0 failed | 55 passed, 0 failed (delta: 0) | ✅ |
| 5 | Consumer semantics | `get_unclassified_entries` → `[]`; entries 319–324 present; entry-318 hash sentinel intact | UNCLASSIFIED=0; ENTRIES_319_324=6; ENTRY318_HASH=`260857bbc71e818b74f503f2984f2b6e5c2854e84e97e4522f9e74b2ccdd0cb8` (matches) | ✅ |

## Evidence and Narrative

All five verification rows pass. The Gate-1 routing write landed atomically — five proposals routed to `accepted|codify` and one to `reference|backlog`, with no blast-radius impact on the remaining 326 rows. The corpus shape matches every predicted count including the walk-2-corrected route split (9 reference + 7 backlog). The test suite is stable at 55/0. Consumer semantics confirm no entries were un-classified by the routing write and the entry-318 hash sentinel is intact.

**Evidence files:**
- `db-invariants.txt` — blast radius diff, corpus shape counts, consumer semantics
- `outside-range-ids.txt` — 326-line capture (deposited by Step 1, re-verified by QA)
- `routing-readback.txt` — per-id readback (deposited by Step 1, re-verified by QA)
- `pytest_targeted.txt` — pytest output (55 passed, 0 failed)

## Receipt

### Sentinel Summary
All five QA rows verified with raw evidence deposited.

### Ledger Updates

#### Forward Register
NONE
