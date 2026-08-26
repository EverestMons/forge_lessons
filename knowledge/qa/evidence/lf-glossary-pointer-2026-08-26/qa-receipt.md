# QA Receipt — lf-glossary-pointer (plan 544, Step 2)

**Date:** 2026-08-26
**CAPTURE_COMMIT:** fa16f6b
**Test Scope:** none (doc-only; probe-battery QA)

## Verification Table

| Item | Check | Expected | Measured | Result |
|---|---|---|---|---|
| 1a | `grep -cF "RETIRED"` (committed extraction) | 1 | 1 | PASS |
| 1b | `grep -c "^## "` (regex, committed extraction) | 0 | 0 | PASS |
| 1c | `grep -cF "[project: lessons-forge]"` | >= 2 | 2 | PASS |
| 1d | `grep -cF "plans 542 + 543"` | 1 | 1 | PASS |
| 1e | `wc -l` vs dev note recorded value | 9 | 9 | PASS |
| 1f | `cmp` extraction vs live file | exit 0 | exit 0 (CMP_OK) | PASS |
| 2a | MATCH Gate 1 (routing) (CHECK-ONLY re-run) | MATCH | MATCH | PASS |
| 2b | MATCH DISPOSITION line (CHECK-ONLY re-run) | MATCH | MATCH | PASS |
| 3a | numstat file count | 2 | 2 | PASS |
| 3b | toplevel is worktree (not live tree) | .bellows-worktrees/544 | .bellows-worktrees/544 | PASS |
| 3c | reflog amend count | 0 | 0 | PASS |

**All 11 checks PASS.**

## Evidence Files

- `probes-raw.txt` — raw probe output (this directory)
- `knowledge/dev-logs/lf-glossary-pointer-dev-2026-08-26.md` — dev note (Step 1 deposit)

============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/544/knowledge/qa/evidence/lf-glossary-pointer-2026-08-26/
Files verified: 2
