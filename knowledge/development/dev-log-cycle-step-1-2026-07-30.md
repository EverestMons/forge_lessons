# Dev Log — Cycle Step 1 (2026-07-30) — Plan 288

Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)

**Dispatch determination:** FRESH — all three probes negative (HEAD exit=128, working tree absent exit=1, git log empty + no bellows-preserved branches).

## Pre-ingest Anchors

**Pristine backup path:** `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-288-20260731T175142Z.db`

**E0=192**
**P0=200**

### NT capture (pre-ingest)

```
NT_COUNT=0
```

Raw NT query output (zero rows):
```
(empty — query ran, returned no rows; NT_COUNT=0 confirms via positive signal)
```

### Stale baseline

```
STALE_COUNT=3
```

### Entry-192 sentinel hash

```
ENTRY_192_HASH=23fb7a1e5b7b62f975339733aca57434cf947f1b214a1b5592588835de5a80c7
```

### Baseline distributions

**Proposals by status:**
```
status=implemented count=147
status=reference count=7
status=rejected count=15
status=stale count=3
status=superseded count=28
```

**Proposals by category:**
```
category=duplicate count=19
category=governance_rule count=156
category=instrumentation count=10
category=narrative count=5
category=structural count=10
```

**Total lesson_entries:** 192
**Total lesson_proposals:** 200

## Ingest Dict (first dispatch)

```
ingested_count: 6
updated_count: 0
unchanged_count: 135
duplicates_marked_count: 0
needs_classification: [193, 194, 195, 196, 197, 198]
terminal_proposals_flagged: []
cycle_timestamp: 2026-07-31T17:54:17.077111+00:00
```
