# Dev Log — Cycle v2 Step 1 (2026-06-06)

## What was done

**Part A — Stale-aware work-list helper**

Added `get_unclassified_entries(conn)` to `src/lessons_forge.py` (placed after `insert_proposal`, before `detect_duplicates`). The function queries for entry IDs with no non-stale proposal, correctly including entries whose only proposals are `stale` — fixing the silent undercount bug where `NOT EXISTS (any proposal)` dropped stale-only entries.

Added `test_get_unclassified_entries` to `src/test_lessons_forge.py` covering three cases: entry with no proposal (included), entry with only stale proposal (included), entry with implemented proposal (excluded).

**Helper diff summary:** +25 lines in `lessons_forge.py`, +47 lines in `test_lessons_forge.py`.

**Part B — Cycle run + authoritative work list**

Ran `run_full_lessons_cycle(conn)` — idempotent as expected (0 ingested, 0 updated). Called `get_unclassified_entries(conn)` to derive the authoritative work list.

## Test result

```
26 passed in 0.09s
```

(25 prior + 1 new `test_get_unclassified_entries`)

## Part B stdout

```
ingested: 0 updated: 0
WORKLIST ( 9 ): [93, 116, 117, 118, 119, 120, 121, 122, 123]
```

## Output Receipt

- **What was done:** Added `get_unclassified_entries` helper + unit test; ran cycle (idempotent); derived authoritative work list via helper.
- **Files deposited:**
  - `knowledge/development/cycle-result-v2-2026-06-06.json` — cycle result + worklist (Step 2 input)
  - `knowledge/development/dev-log-cycle-v2-step-1-2026-06-06.md` — this file
- **Test result:** 26 passed / 0 failed
- **Authoritative worklist:** `[93, 116, 117, 118, 119, 120, 121, 122, 123]` (9 entries)
- **Flags for CEO:** None
- **Flags for Next Step:** Worklist confirmed at 9 entries. Step 2 should call `get_unclassified_entries(conn)` directly to re-derive the list (do not copy).
