# QA Report: Gate 1 Held-Pair Routing 378+389

**Plan:** 537 — `gate1-route-heldpair`
**Date:** 2026-08-25
**Step 1 commit:** `555b298`

## Q0 — Re-Pin

| Check | Result |
|-------|--------|
| Newest commit touching evidence files | `555b298 [537] Step 1 — gate1 held-pair routing 378+389 (accepted|codify, ceo)` |
| `proposed` count in 354–410 | 0 |

## Verification Table

| # | Claim | Status | Detail |
|---|-------|--------|--------|
| 1 | THE WRITE LANDED | ✅ | 378: `accepted\|codify`, `status_updated_by='ceo'`, `status_updated_at='2026-08-26T00:41:39Z'`. 389: `accepted\|codify`, `status_updated_by='ceo'`, `status_updated_at='2026-08-26T00:41:39Z'`. Both timestamps equal each other AND equal the dev log `:TS` (`2026-08-26T00:41:39Z`). Global `accepted\|codify` = 30. |
| 2 | UNTOUCHED POPULATION | ✅ | Diff shows exactly 2 changed rows (378, 389), 4 changed lines (2 old, 2 new), zero foreign ids, zero `target_artifact` changes. |
| 3 | DUMPS ARE COMMITTED ONES | ✅ | `git show HEAD:<path>` for both pre-dump and post-dump matches working tree byte-for-byte. |
| 4 | FULL SUITE | ✅ | `63 passed in 0.10s` — matches plan measurement of 63; delta = 0. |
| 5 | DB WAS NOT COMMITTED | ✅ | Neither Step 1 commit (`555b298`) nor deposit commit (`022bf3c`) contains `lessons-forge.db`. `git ls-files --error-unmatch lessons-forge.db` exits 1. |
| 6 | NOTHING ELSE MOVED | ✅ | `git status --porcelain` empty. `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `PANEL_SEAT_TEMPLATE.md`, `LESSONS.md`, `knowledge/FORWARD.md` absent from Step 1 commit. |

## Evidence and Narrative

### Check 1 — Routing Verification
Raw DB query output and global count in `evidence/gate1-route-heldpair/routing-verification.txt`. Both rows carry the full target signature: `accepted|codify` with `status_updated_by='ceo'` and matching timestamps. The global `accepted|codify` population is 30, consistent with the plan's 28 → 30 arithmetic.

### Check 2 — Diff Audit
Raw diff output in `evidence/gate1-route-heldpair/diff-audit.txt`. The pre-to-post dump diff shows exactly two `c` (change) hunks at lines 378 and 389. No other id appears in the diff. Row 378 retains `PLANNER_TEMPLATE.md` as `target_artifact`; row 389 retains `-` (NULL).

### Check 3 — Dump Integrity
Both committed dumps verified byte-identical to working tree copies. Results in `evidence/gate1-route-heldpair/diff-audit.txt`.

### Check 4 — Full Suite
Full verbose pytest output in `evidence/gate1-route-heldpair/pytest_full.txt`. 63 passed, 0 failed, 0 errors, 0 warnings.

### Check 5 — DB Untracked
Verification in `evidence/gate1-route-heldpair/routing-verification.txt`. The DB file does not appear in any commit on this branch and `git ls-files --error-unmatch` confirms it is untracked.

### Check 6 — Nothing Else Moved
Working tree clean. Protected files (`DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `PANEL_SEAT_TEMPLATE.md`, `LESSONS.md`, `knowledge/FORWARD.md`) absent from all commits in scope.

### Output Receipt

- **Plan ID:** 537
- **Plan slug:** `gate1-route-heldpair`
- **Step:** 2 (QA)
- **Rows verified:** 378, 389
- **Global `accepted|codify`:** 30
- **Suite:** 63 passed
- **Evidence files:** `pytest_full.txt`, `routing-verification.txt`, `diff-audit.txt`

### Ledger Updates

No ledger updates required. No forward register emitted per plan instruction.

## Rule 20 Self-Check

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/537/knowledge/qa/evidence/gate1-route-heldpair/
Files verified: 3
```
