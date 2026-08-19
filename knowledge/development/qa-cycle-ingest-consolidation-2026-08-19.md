# QA Report — Cycle Ingest Consolidation Batch 2026-08-19

**Plan:** 456 | **Step:** 2 (QA) | **Date:** 2026-08-19

## Verification Table

| # | Check | Expected | Measured | Status |
|---|---|---|---|---|
| N1 | Batch size (entries with id > E0) | 25 | 25 | ✅ |
| N2 | Corpus count E (= E0 + N1) | 370 | 370 | ✅ |
| N3 | would_update (persisted: pre-existing rows with post-ingest ingested_at) | 0 | 0 | ✅ |
| N4 | Unchanged (structural: N7 - N1 - N3) | 288 | 288 | ✅ |
| N5 | Proposals count P | 353 | 353 | ✅ |
| N6 | Non-terminal set by id | {340,342,346,350,352} | {340,342,346,350,352} | ✅ |
| N7 | Parser total (parse_lessons_md) | 313 | 313 | ✅ |
| G1 | NT by id (independent re-run) | NT=340,342,346,350,352 | NT=340,342,346,350,352 | ✅ |
| G2 | P == N5 (independent re-run) | 353 | 353 | ✅ |
| G3 | E == N2 | 370 | 370 | ✅ |
| G4 | Persisted update check (ids <= 345 with ingested_at > ingest start) | 0 | 0 | ✅ |
| G5 | Sentinel entry 345 content_hash | 8df4331b…ed9de962 | 8df4331b…ed9de962 | ✅ |
| G7 | FORWARD unchanged | 18 | 18 | ✅ |
| BK1 | Backup exists and passes integrity_check | ok | ok | ✅ |
| BK2 | Backup MAX(lesson_entries.id) = E0 | 345 | 345 | ✅ |
| BK3 | Backup MAX(lesson_proposals.id) = P0 | 353 | 353 | ✅ |
| CL1 | No classification ran: P == N5 | 353 | 353 | ✅ |
| CL2 | get_unclassified_entries count = UNCLASSIFIED_BASE + N1 | 0 + 25 = 25 | 25 | ✅ |
| ST1 | Step 1 commit touched only declared deposits | 2 files (dev-log + evidence) | 2 files (dev-log + evidence) | ✅ |
| DIST | Proposal distribution SUM = P0 | 353 | 353 | ✅ |
| STALE | Stale proposal count | 3 | 3 | ✅ |

## Deposits

- `knowledge/development/qa-cycle-ingest-consolidation-2026-08-19.md`
- `knowledge/development/qa-evidence-cycle-ingest-2026-08-19.txt`

## Evidence

All raw command outputs are in `knowledge/development/qa-evidence-cycle-ingest-2026-08-19.txt`.

## Rule 20 — QA Self-Check Results

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/development/
Files verified: 2
```
