# QA Receipt — Gate-1 Routing W=3: 411/412/413 proposed → accepted|codify

**Date:** 2026-08-26
**Plan:** 557

## Hygiene

**Numstat (HEAD~1):**
```
52	0	knowledge/development/dev-log-g1w3-2026-08-26.md
10	0	knowledge/development/g1w3-flip.sql
```
Files: 2 (matches plan scope).

**Toplevel:** `/Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/557`

**Reflog (-n 4):**
```
f2d226a HEAD@{0}: reset: moving to HEAD
f2d226a HEAD@{1}: commit: [557] gate1-routing-w3(gate1-routing-w3-2026-08-26): 411/412/413 proposed -> accepted|codify (planner x1 non-author, ceo x2)
```
Amends: 0.

**Gate note:** probe-battery QA, no pytest scope — the benign class (19th precedent); Planner override with reference.

## Verification

| Item | Check | Status |
|---|---|---|
| M1 | 411 accepted/codify, 412 accepted/codify, 413 accepted/codify — all three rows verbatim | ✅ |
| M2 | 411 status_updated_by=planner; 412 status_updated_by=ceo; 413 status_updated_by=ceo; all three status_updated_at=2026-08-26T16:57:46Z (identical) | ✅ |
| M3 | Triple-set hash bf94b39d597998b1bfebeeab303d833a — SET-IDENTICAL to dev-log pre-flip and post-flip | ✅ |
| M4 | P=413, accepted=3 | ✅ |
| Replay | Flip SQL re-run aborts: CHECK constraint failed: x=3 (exit 1); post-abort band unchanged | ✅ |
| Numstat | 2 files in scope | ✅ |
| Amends | 0 amends in reflog | ✅ |

============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/557/knowledge/qa/evidence/gate1-routing-w3-2026-08-26/
Files verified: 2
