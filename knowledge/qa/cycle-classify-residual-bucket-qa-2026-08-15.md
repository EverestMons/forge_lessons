# QA Report — cycle-classify-residual-bucket-2026-08-15-qa-corrective

**Plan:** 427 (QA-only corrective for plan 425's step 3)
**Date:** 2026-08-15
**Agent:** Lessons Forge QA
**Working directory:** /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/427
**DB:** file:///Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro (read-only, absolute path)

## A0 Precondition

**Determination: PROCEED (arm 1)**
- Proposal 353 exists: id=353, entry_id=345, status='proposed', route=None
- COUNT(*) FROM lesson_proposals = 353
- get_unclassified_entries(conn) = []
- Main HEAD contains 8bfb954

## Verification Table

| # | Claim | Status | Measured value | DB source | Evidence |
|---|---|---|---|---|---|
| 0 | Deliverables (Rule 17) | ✅ | All 3 tracked, porcelain clean | git log/status | recovery.txt |
| 1 | Targeted suite | ✅ | 55 passed | pytest | pytest_targeted.txt |
| 2 | Proposal 353 correctly shaped | ✅ | id=353 entry_id=345 status=proposed route=None COUNT=353 | lesson_proposals | proposal.txt |
| 3 | Gate-2 queue untouched | ✅ | NT {340,342,346,350,352} all accepted/codify; STALE=3; sentinel=e7b607bd; entries=345 | lesson_proposals, lesson_entries | queue-untouched.txt |
| 4 | Reasoning carries 3 markers | ✅ | [DEDUP]=1 [REMEDY-GATED]=1 [AUTHOR-CONFLICT]=1 | lesson_proposals.reasoning | proposal.txt |
| 5 | get_unclassified_entries == [] | ✅ | [] | lesson_entries, lesson_proposals | proposal.txt |
| 6 | At-risk artifact survived | ✅ | f1807cf266b3…=match; 08-15 report 2593B, 1 proposal | shasum main-repo, report file | report.txt |
| 7 | Report content | ✅ | Route=0 Recently-implemented=0 everything-else=1 | report file, lesson_entries.source_heading | report.txt |
| 8 | 8-status distribution | ✅ | impl=281 super=28 ref=20 rej=15 acc=5 prop=1 stale=3 amb=0 total=353 | lesson_proposals | queue-untouched.txt |
| 9 | No schema drift | ✅ | DB schema matches src/db.py DDL | sqlite_master, PRAGMA table_info | schema.txt |
| 10 | R2 recovery clean | ✅ | No 425 worktree; 8bfb954 in HEAD; main porcelain empty; decisions/ correct | git worktree, git status, find | recovery.txt |
| 11 | DISPOSITION line | ✅ | Count=1, carries proposal=353 and all 3 markers | dev-log step 1 | proposal.txt |
| 12 | Register posture | ✅ | FORWARD=18 rows | FORWARD.md | recovery.txt |

## Evidence and Narrative

All 13 verification rows pass. Plan 425's steps 1 and 2 landed correctly via R2 recovery — the classification of entry 345 into proposal 353 committed at c9974d0, the report generation at 8bfb954, and the at-risk 08-14 report survived byte-identical at f1807cf2. The Gate-2 queue is untouched, the 8-status distribution matches the pinned baseline exactly, and the test suite holds at 55 passed with no delta.

The R2 recovery itself is clean: no 425 worktree remains, main's porcelain is empty, and decisions/ contains exactly the expected files (halted-executable-425.md and this plan's in-progress-executable-427.md).

### Receipt

- **Plan:** 427
- **Subject:** plan 425 (halted at step 2 gate, steps 1-2 landed)
- **Rows checked:** 13 (0-12)
- **Rows passed:** 13
- **Rows failed:** 0
- **Findings:** None

### Ledger Updates

#### Prompt Feedback

None.

#### Forward Register

NONE.

============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/427/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/
Files verified: 6
