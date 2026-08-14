# Dev Log — Fold-Damage Ingest, Step 1 (Plan 411)

**Date:** 2026-08-14
**Plan:** 411 — `cycle-ingest-folddamage-2026-08-14`
**Status: Partial — in flight (pre-ingest stub)**
**Dispatch:** FRESH

## Backup

**Path:** `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-411-20260814T164032Z.db`
**Integrity:** `ok` (via `PRAGMA integrity_check` with `file:…?immutable=1`)

## Baselines

- **E0 = 338**
- **P0 = 346**
- **NT = 340,342,346** (all `accepted`)
- **STALE_COUNT = 3**
- **SURFACEABLE_BASE = 0** (proposed + ambiguous; distinct from NT — they have come apart this cycle)
- **FORWARD baseline:** 18 (probe: `grep -c "^| "`)
- **TOTAL_ENTRIES = 338**

### Status Distribution (all eight statuses, zero-emitting)

| Status | Count |
|---|---|
| implemented | 279 |
| superseded | 28 |
| reference | 18 |
| rejected | 15 |
| stale | 3 |
| accepted | 3 |
| proposed | 0 |
| ambiguous | 0 |

### Proposals by Category

| Category | Count |
|---|---|
| governance_rule | 287 |
| instrumentation | 21 |
| duplicate | 19 |
| structural | 14 |
| narrative | 5 |

### Sentinel

- **Entry 338 content_hash:** `359bf0267d500f50e67b4748a974b468620d8eb25c58b1fd4c046d0fabffaf9a`
- **Parsed match count:** verified at 1a-bis

## Doctrine Pins

```
943971f5f909b089cfb276de31ea8eaf2b2680b4e1ccc5378413f8df8fccb941  /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md
4f33c3884b426189ba9f019c0722681a4446e5f9223b1f0f10c117f7de0691a0  /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md
d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0  /Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md
```
