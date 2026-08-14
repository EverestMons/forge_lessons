# QA Report — Fold-Damage Ingest (Plan 411)

**Date:** 2026-08-14
**Plan:** 411 — `cycle-ingest-folddamage-2026-08-14`
**Step:** 2 (QA)
**Agent:** Lessons Forge QA
**DB access:** read-only (`file:…?mode=ro`, absolute path)

## Verification Table

| # | Claim | Status | Measured value | DB source | Evidence |
|---|---|---|---|---|---|
| 0 | Deliverables committed (Rule 17) | ✅ | commit 42d8af7, porcelain empty, exit 0 | git log/status | git output |
| 1 | Targeted suite passes | ✅ | 55 passed | pytest | pytest_targeted.txt |
| 2 | get_unclassified_entries returns exactly 6 ids | ✅ | [339, 340, 341, 342, 343, 344] | lesson_entries via get_unclassified_entries | python output |
| 3 | The 6 landed, only those | ✅ | 6 rows, 338+6=344 reconciled | SELECT id, source_heading WHERE id IN (339-344) | invariants.txt |
| 4 | Plan-204 held, no proposal created | ✅ | stale=3, sentinel 359bf026 match, proposals=346, NT=340,342,346, MAX=346, all 8 buckets unchanged | lesson_proposals status/count/hash | hash-trap.txt |
| 5 | No schema drift | ✅ | DB schema matches src/lessons_forge.py DDL | PRAGMA table_info + .schema | schema.txt |
| 6 | Fingerprint provenance | ✅ | a94061915743eb8e0cdfda6ea17ae8e73c48faa1f391cd6f355db53bdbf4cb1b, LESSONS.md porcelain clean | lesson_entries source_heading, git status | python + git output |
| 7 | Register posture | ✅ | decisions/ has only in-progress-executable-411.md (this plan), FORWARD delta=0 (18 pre, 18 post) | filesystem, grep | ls + grep output |

## Evidence and Narrative

All 8 verification rows pass. The ingest landed exactly 6 entries (339-344) with zero proposals created, zero duplicates, and zero updates. The proposal table is unchanged at 346 rows with the non-terminal set exactly {340, 342, 346} — the live Gate-2 queue is untouched.

**Row 0:** Step 1 deliverable `dev-log-folddamage-step-1-2026-08-14.md` committed at `42d8af7`. Porcelain output empty with exit code 0.

**Row 1:** Full targeted suite `python3 -m pytest src/ -v` — 55 passed in 0.09s. Baseline at authoring was 55 passed — no delta.

**Row 2:** `get_unclassified_entries(conn)` returns `[339, 340, 341, 342, 343, 344]` — exactly the 6 ingested entries. NOT empty — no classification occurred. This is the correct closing state for this ingest-only plan.

**Row 3:** All 6 entries present in DB with correct headings. Entry 340's apostrophe-bearing heading verified via parameterized query. Total entries = 344, reconciling 338 + 6 = 344.

**Row 4:** Every invariant held:
- Stale count: 3 (unchanged)
- Sentinel entry 338 hash: `359bf0267d500f50e67b4748a974b468620d8eb25c58b1fd4c046d0fabffaf9a` (match)
- Total proposals: 346 (unchanged from P0)
- NT set: exactly {340, 342, 346} by id (not just count)
- MAX(lesson_proposals.id): 346
- All 8 status buckets unchanged: implemented 279, superseded 28, reference 18, rejected 15, stale 3, accepted 3, proposed 0, ambiguous 0
- Duplicates post-338: 0
- Receipt dict: updated_count=0, terminal_proposals_flagged=[]

**Row 5:** PRAGMA table_info and `.schema` for both tables match the DDL in `src/lessons_forge.py`. No drift.

**Row 6:** Batch fingerprint recomputed from DB headings in id order: `a94061915743eb8e0cdfda6ea17ae8e73c48faa1f391cd6f355db53bdbf4cb1b` — matches plan pin. `LESSONS.md` porcelain still clean at root.

**Row 7:** `knowledge/decisions/` non-Done contents: `in-progress-executable-411.md` (this plan's own file) and `archived-halted-plans/` directory — expected. FORWARD.md baseline: 18 (Step 1 captured 18, QA measured 18) — delta 0, no new rows.

## Receipt

**Status: Complete**
**Cycle result dict (from Step 1):**
```
ingested_count=6
updated_count=0
unchanged_count=281
duplicates_marked_count=0
needs_classification=[339, 340, 341, 342, 343, 344]
terminal_proposals_flagged=[]
cycle_timestamp=2026-08-14T16:43:54.707046+00:00
```

### Ledger Updates

#### Prompt Feedback

None.

#### Forward Register

NONE.

============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/411/knowledge/qa/evidence/cycle-ingest-folddamage-2026-08-14/
Files verified: 4
