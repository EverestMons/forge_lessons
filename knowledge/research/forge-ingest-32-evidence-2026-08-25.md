# Evidence Deposit: Post-08-19 Ingest — 32 New Entries

**Plan:** executable-529 | **Date:** 2026-08-25 | **Step:** 1 (DEV)

## 1. Pre-state (I1)

```
sqlite3> SELECT COUNT(*) FROM lesson_entries;
370

sqlite3> SELECT COUNT(*) FROM lesson_proposals;
378

sqlite3> SELECT MAX(id) FROM lesson_entries;
370

sqlite3> SELECT MAX(ingested_at) FROM lesson_entries;
2026-08-19T17:18:13.712877+00:00
```

All four match I1 pins: entries 370, proposals 378, MAX(id) 370, MAX(ingested_at) 2026-08-19T17:18:13.

## 2. Backup

```
cp lessons-forge.db pre-ingest-2026-08-25-154425.db
Source size: 1593344
Backup size: 1593344
SIZE MATCH OK
```

## 3. Ingest (fingerprint-gated)

```
PARSER_COUNT=345
INGEST_RESULT={"inserted": 32, "updated": 0, "unchanged": 313, "stale_proposals_marked": 0, "terminal_proposals_flagged": []}
FINGERPRINT_MATCH=TRUE — COMMITTED
```

Parser yielded 345 entries (I4 match). Ingest fingerprint matches I2 exactly: inserted 32, updated 0, unchanged 313, stale_proposals_marked 0, terminal_proposals_flagged []. Transaction committed.

## 4. Post-verification (I3)

```
sqlite3> SELECT COUNT(*) FROM lesson_entries;
402

sqlite3> SELECT COUNT(*) FROM lesson_proposals;
378

sqlite3> SELECT id, substr(source_heading,1,70) FROM lesson_entries WHERE id >= 371 ORDER BY id;
371|2026-08-19: A clone-diff needs THREE passes — facts, artefacts, struct
372|2026-08-19: Anchor a path where its file LIVES FOR GIT — tracked to th
373|2026-08-19: A shipped, correctly-routed shop rule can produce the WRON
374|2026-08-19: A declaration/consumer pair fails in BOTH directions, and 
375|2026-08-19: A correction can OPEN a gap — removing a false belief with
376|2026-08-19: A malformed sqlite3 URI silently CREATES a decoy database,
377|2026-08-19: A periodic task at an un-guarded loop boundary must own it
378|2026-08-21: Before hand-building a classification, registry, or index,
379|2026-08-21: A workflow can be correctly mechanized and still be wrong 
380|2026-08-21: `content_hash` detects modification, not identity — it is 
381|2026-08-21: CEO DECISION — `glossary.md` is the per-repo home for DOMA
382|2026-08-22: A single-arm probe against a drifting corpus is uninterpre
383|2026-08-22: A function that computes a LOOKUP KEY must be the identity
384|2026-08-22: Write the regression guard BEFORE the fix and watch it fai
385|2026-08-23: An identity that DERIVES one of its terms cannot discrimin
386|2026-08-23: Read a checker's implementation before trusting its verdic
387|2026-08-23: A mechanism cannot enforce a lesson about that mechanism's
388|2026-08-23: A session wrap cannot append to an artifact a dispatched p
389|2026-08-24: A tool's verdict CHANNEL is part of its contract — reading
390|2026-08-24: Folding a tool-finding into the artifact is not adopting i
391|2026-08-24: A fold aimed at what a finding DESCRIBED, not at what it M
392|2026-08-24: A check whose result you PRINT but do not BRANCH on is not
393|2026-08-24: A watched directory's safety property is its daemon's ADMI
394|2026-08-24: An affirmation gate keyed on TODAY'S DATE is satisfied by 
395|2026-08-24: A predicted id is not an identity — key watchers and verdi
396|2026-08-24: A review covers the plan's FILE LIST; a contract change's 
397|2026-08-24: An observation window anchored at the OBSERVER'S start can
398|2026-08-24: A schema enum value is a FEATURE CLAIM — if no code writes
399|2026-08-25: A precedent's CONTEXT BOUNDARY is part of the precedent — 
400|2026-08-25: A shared deposit FILENAME is a SEQUENTIAL collision — succ
401|2026-08-25: A correct, indexed instruction did not survive its third e
402|2026-08-25: Resurrect removed code WITH its hardening history — the bi

sqlite3> SELECT MAX(ingested_at) FROM lesson_entries;
2026-08-25T20:44:45.696689+00:00
```

Post-state matches I3: entries 402, proposals 378 (unchanged), 32 rows in sequential band 371–402, dates span 2026-08-19 through 2026-08-25, MAX(ingested_at) is today.

## Verification Summary

| Check | Pin | Measured | Status |
|---|---|---|---|
| Pre-state entry count | 370 | 370 | ✅ |
| Pre-state proposal count | 378 | 378 | ✅ |
| Pre-state MAX(id) | 370 | 370 | ✅ |
| Pre-state MAX(ingested_at) | 2026-08-19T17:18:13 | 2026-08-19T17:18:13.712877+00:00 | ✅ |
| Parser count (I4) | 345 | 345 | ✅ |
| Inserted (I2) | 32 | 32 | ✅ |
| Updated (I2) | 0 | 0 | ✅ |
| Unchanged (I2) | 313 | 313 | ✅ |
| stale_proposals_marked (I2) | 0 | 0 | ✅ |
| terminal_proposals_flagged (I2) | [] | [] | ✅ |
| Post-state entry count (I3) | 402 | 402 | ✅ |
| Post-state proposal count (I3) | 378 | 378 | ✅ |
| New id band (I3) | 371–402 sequential | 371–402 sequential | ✅ |
| Post MAX(ingested_at) | today | 2026-08-25T20:44:45.696689+00:00 | ✅ |
| Backup size match | equal | 1593344 = 1593344 | ✅ |

## Rule 20 — QA Self-Check Results

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/529/knowledge/research/
Files verified: 1
```

PASSED — SELF-CHECK PASSED
