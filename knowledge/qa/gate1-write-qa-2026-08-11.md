# QA Report — Gate-1 Routing Write for Proposals 315–326

**Plan:** `gate1-write-315-326-2026-08-11`
**Step:** 2 — QA
**Date:** 2026-08-12

## Deliverable Verification

| # | Deliverable | Status |
|---|-------------|--------|
| 1 | `knowledge/development/dev-log-gate1-write-step-1-2026-08-11.md` | ✅ |
| 2 | `knowledge/development/gate1w-rehearsal.sql` | ✅ |
| 3 | `knowledge/development/gate1w-flip.sql` | ✅ |
| 4 | `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/outside-range-ids.txt` (314 lines) | ✅ |
| 5 | `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/flip-readback.txt` (12 rows) | ✅ |

## QA Checks

| Row | Check | Expected | Actual | Status |
|-----|-------|----------|--------|--------|
| 1 | A-set (315,316,317,318,319,324,325,326) status/route | 8/8 `accepted\|codify` | 8/8 `accepted\|codify` | ✅ |
| 1 | A-set `status_updated_by` | all `ceo` | all `ceo` | ✅ |
| 1 | A-set Z-stamped | all ISO 8601 Z | all `2026-08-12T00:29:31Z` | ✅ |
| 1 | R-set (320,321,322,323) status/route | 4/4 `reference\|reference` | 4/4 `reference\|reference` | ✅ |
| 1 | R-set `status_updated_by` | all `ceo` | all `ceo` | ✅ |
| 1 | R-set Z-stamped | all ISO 8601 Z | all `2026-08-12T00:29:31Z` | ✅ |
| 1 | 325 `target_artifact` | `DRAFTING_CYCLE.md` | `DRAFTING_CYCLE.md` | ✅ |
| 1 | Other eleven targets unchanged from classification | match backup | all match | ✅ |
| 2 | `accepted\|codify` count | 8 | 8 | ✅ |
| 2 | `reference\|reference` count | 9 | 9 | ✅ |
| 2 | `proposed` count | 0 | 0 | ✅ |
| 2 | Positive control: backup `proposed` (315–326) | 12 | 12 | ✅ |
| 2 | Positive control: backup `accepted\|codify` | 0 | 0 | ✅ |
| 2 | Positive control: backup `reference\|reference` | 5 | 5 | ✅ |
| 3 | Blast radius diff vs deposited capture | identical | identical | ✅ |
| 3 | Capture line count | 314 | 314 | ✅ |
| 4 | pytest targeted (55/0 baseline) | 55 passed, 0 failed | 55 passed, 0 failed | ✅ |
| 4 | Delta | reported | passed Δ=0, failed Δ=0 | ✅ |

## Rule 20 Self-Check

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/350/knowledge/qa/evidence/gate1-write-315-326-2026-08-11/
Files verified: 2
```

## Evidence and Narrative

All four QA rows pass. The Gate-1 routing write landed atomically: eight proposals moved to `accepted|codify`, four to `reference|reference`, and 325's target_artifact reversed from `PLANNER_TEMPLATE.md` to `DRAFTING_CYCLE.md` per the packet. Corpus totals match expectations (8 accepted|codify, 9 reference|reference including 5 pre-existing, 0 proposed). The blast-radius capture is byte-identical to the Step 1 deposit (314 rows, no concurrent changes). Pytest holds at 55/0.

**Evidence files:**
- `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/qa-db-checks.txt`
- `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/pytest_targeted.txt`
- `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/outside-range-ids.txt` (Step 1 deposit, re-verified)
- `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/flip-readback.txt` (Step 1 deposit)

## Receipt

All 18 QA table rows: ✅

### Ledger Updates
NONE

#### Forward Register
NONE
