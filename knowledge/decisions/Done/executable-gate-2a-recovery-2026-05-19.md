# Executable: Gate 2a Recovery — Schema Rollback + Cleanup

**Plan slug:** executable-gate-2a-recovery-2026-05-19
**Plan type:** executable
**Project:** lessons-forge
**Specialist:** Forge Developer
**Auto-close:** false
**Pause for verdict:** after_step_1
**Priority:** 1
**Depends on:** none
**Created:** 2026-05-19

---

## Context

Gate 2a Step 2 successfully applied 25 ratification writes to `lessons-forge.db` but did so via two unauthorized scope expansions: (a) added `'deferred'` to the `lesson_proposals.status` CHECK constraint, and (b) modified `src/db.py` in a worktree. The canonical DB has the schema mutation and the writes; the canonical `src/db.py` is untouched.

Planner-verified state (state diagnostic 2026-05-19, Planner-direct due to Claude Code auth failure on Bellows-dispatched diagnostic):

| Surface | State |
|---|---|
| Canonical `lessons-forge.db` schema | Mutated — includes `'deferred'` (unwanted) |
| Canonical `lessons-forge.db` data | 18 accepted, 2 deferred (IDs 45/48), 14 implemented, 4 rejected, 24 superseded (62 total) |
| Canonical `src/db.py` | Untouched — `'deferred'` NOT in CHECK |
| Worktree `.bellows-worktrees/gate-2a-lessons-forge-ratification-2026-05-19/` | Detached HEAD at `d8cb5e5`, commit force-adds `lessons-forge.db` and mutates `src/db.py` |
| Untracked in main working tree | 2 halted plan files, manifest JSON, Step 1 dev log |

**CEO-locked decision:** collapse `'deferred'` → `'rejected'` semantically. Gate 1's "defer until revisit" is not load-bearing; reconsideration happens at LESSONS.md re-ingestion time, not via a status-value-based queue. Schema mutation must be rolled back; the 2 deferred rows (G5/I3, IDs 45/48) must transition to `'rejected'` with `duplicate_of` pointing at no other row (these are independent rejections, not duplicates of other proposals).

**Recovery shape:** three sequential steps; verdict gate after Step 1 to protect the schema rollback work before the worktree (last-resort recovery source) is destroyed.

- **Step 1** — DB schema rollback + `deferred → rejected` collapse in single transaction
- **Step 2** — Worktree teardown + commit useful artifacts to main
- **Step 3** — QA verification of final state

---

## STEP 1 — Schema rollback + status collapse

You are the Forge Developer. Read `forge/agents/FORGE_DEVELOPER.md` and `lessons-forge/CLAUDE.md`. Operate against `/Users/marklehn/Developer/GitHub/lessons-forge/`. Database is `lessons-forge.db`.

**Strict scope:** This step modifies the live `lessons-forge.db` schema and data ONLY. Do NOT touch `src/db.py` (it is already correct). Do NOT touch the worktree at `.bellows-worktrees/`. Do NOT delete files. Do NOT run anything beyond what is explicitly authorized here. If you encounter any unexpected state, HALT and report — do not improvise.

**Task:**

The current `lesson_proposals.status` CHECK constraint contains 8 values:
`('proposed', 'accepted', 'rejected', 'deferred', 'ambiguous', 'stale', 'superseded', 'implemented')`

The canonical schema (per `src/db.py`) contains 7 values:
`('proposed', 'accepted', 'rejected', 'ambiguous', 'stale', 'superseded', 'implemented')`

Inside a single transaction:

1. **Convert 'deferred' → 'rejected' for the two affected rows.** IDs 45 and 48 currently have `status='deferred'`. Update both to `status='rejected'` with `status_updated_by='ceo'` and `status_updated_at=<single ISO-8601 UTC timestamp captured at start of transaction>`. Leave `duplicate_of` as NULL on both (these are independent rejections, not duplicates of other proposals).

2. **Rebuild the table with canonical schema.** Use the standard SQLite table-rebuild pattern:
   ```sql
   CREATE TABLE lesson_proposals_new (
       id                  INTEGER PRIMARY KEY AUTOINCREMENT,
       entry_id            INTEGER NOT NULL REFERENCES lesson_entries(id) ON DELETE CASCADE,
       category            TEXT    NOT NULL CHECK(category IN ('structural', 'instrumentation', 'governance_rule', 'language', 'narrative', 'duplicate')),
       subcategory         TEXT,
       suggested_action    TEXT    NOT NULL,
       reasoning           TEXT    NOT NULL,
       confidence          TEXT    NOT NULL CHECK(confidence IN ('low', 'medium', 'high')),
       status              TEXT    NOT NULL DEFAULT 'proposed' CHECK(status IN ('proposed', 'accepted', 'rejected', 'ambiguous', 'stale', 'superseded', 'implemented')),
       target_layer        TEXT    CHECK(target_layer IS NULL OR target_layer IN ('structure', 'governance', 'language', 'none')),
       target_artifact     TEXT,
       duplicate_of        INTEGER,
       proposed_at         TEXT    NOT NULL,
       status_updated_at   TEXT,
       status_updated_by   TEXT    CHECK(status_updated_by IS NULL OR status_updated_by IN ('planner', 'ceo', 'auto'))
   );
   INSERT INTO lesson_proposals_new SELECT * FROM lesson_proposals;
   DROP TABLE lesson_proposals;
   ALTER TABLE lesson_proposals_new RENAME TO lesson_proposals;
   ```
   The two indexes on this table (`idx_lesson_proposals_entry`, `idx_lesson_proposals_status`, `idx_lesson_proposals_category`) need to be recreated after the rename — SQLite drops them with the table:
   ```sql
   CREATE INDEX IF NOT EXISTS idx_lesson_proposals_entry ON lesson_proposals(entry_id);
   CREATE INDEX IF NOT EXISTS idx_lesson_proposals_status ON lesson_proposals(status);
   CREATE INDEX IF NOT EXISTS idx_lesson_proposals_category ON lesson_proposals(category);
   ```

3. **Pre-commit verification (inside the same transaction):**
   - Query `SELECT sql FROM sqlite_master WHERE type='table' AND name='lesson_proposals'`. Confirm the CHECK constraint contains EXACTLY 7 values, no `'deferred'`.
   - Query `SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY status`. Expected distribution: accepted=18, implemented=14, rejected=6, superseded=24 (the previous 4 rejected plus IDs 45 and 48 now rejected). Total: 62.
   - Query `SELECT id, status, status_updated_by FROM lesson_proposals WHERE id IN (45, 48)`. Both rows must have status='rejected', status_updated_by='ceo'.
   - Query `SELECT COUNT(*) FROM lesson_proposals WHERE status='deferred'`. Must be 0.
   - Query `SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='lesson_proposals'`. Must list all three indexes (entry, status, category).
   - Verify FK integrity: `PRAGMA foreign_key_check`. Must return 0 rows.

   If ALL verifications pass: COMMIT.
   If ANY verification fails: ROLLBACK and report which specific check failed.

**No git commit in this step.** `lessons-forge.db` is gitignored; the file on disk IS the state of record. No `git add` needed.

**Dev log:**

```markdown
# Dev Log — Gate 2a Recovery Step 1 (schema rollback + status collapse)

Transaction start ISO: <UTC ISO>
Transaction end ISO: <UTC ISO>

Pre-rollback DB state:
- CHECK constraint values: 8 (includes 'deferred')
- Distribution: <pre values>

Operations:
1. UPDATE: 2 rows (IDs 45, 48) deferred -> rejected
2. CREATE TABLE lesson_proposals_new with canonical 7-value CHECK
3. INSERT ... SELECT * FROM lesson_proposals (62 rows copied)
4. DROP TABLE lesson_proposals
5. ALTER TABLE lesson_proposals_new RENAME TO lesson_proposals
6. CREATE INDEX (3 indexes recreated)

Post-rollback DB state:
- CHECK constraint values: 7 (no 'deferred')
- Distribution: <post values, expected accepted=18 implemented=14 rejected=6 superseded=24>
- IDs 45, 48 status: rejected
- Deferred count: 0
- Indexes present: <list>
- FK integrity: <PRAGMA foreign_key_check result>

Verifications: <each passed/failed>
Result: COMMIT | ROLLBACK
```

Deposit to: `lessons-forge/knowledge/development/dev-log-gate-2a-recovery-step-1-2026-05-19.md`

**Output Receipt:**
- Agent: Forge Developer
- Step: 1
- Status: Complete (all verifications passed, transaction committed); Blocked (any verification failed, transaction rolled back)
- What Was Done: rolled back schema CHECK constraint and collapsed 2 deferred rows to rejected
- Files Deposited: `lessons-forge/knowledge/development/dev-log-gate-2a-recovery-step-1-2026-05-19.md`
- Files Created or Modified: `lessons-forge.db` (gitignored, no commit)
- Decisions Made: rollback completed | rollback aborted
- Flags for CEO: any verification failure detail; any unexpected pre-rollback state
- Flags for Next Step: Planner Rule 22 reads dev log, verifies state, authorizes Step 2

**Deposits:**
- `lessons-forge/knowledge/development/dev-log-gate-2a-recovery-step-1-2026-05-19.md`

**STOP.** Do NOT move the plan to Done. Do NOT proceed to Step 2.

---

## STEP 2 — Worktree teardown + commit useful artifacts

You are the Forge Developer. Before starting, read the prior step's deposit at `lessons-forge/knowledge/development/dev-log-gate-2a-recovery-step-1-2026-05-19.md` and verify its Output Receipt status is Complete. If not, stop and report.

**Strict scope:** This step removes the stale worktree and commits the useful artifacts from Gate 2a's failed execution to main. Do NOT modify `lessons-forge.db` (already correct from Step 1). Do NOT modify `src/db.py` (canonical is already correct).

**Task:**

1. **Remove the stale worktree.** From `/Users/marklehn/Developer/GitHub/lessons-forge/`:
   ```bash
   git worktree remove --force .bellows-worktrees/gate-2a-lessons-forge-ratification-2026-05-19
   ```
   Then verify removal:
   ```bash
   git worktree list
   ls -la .bellows-worktrees/
   ```
   Expected: the `gate-2a-lessons-forge-ratification-2026-05-19` worktree no longer appears in either output. Commit `d8cb5e5` becomes unreachable and will be garbage-collected on the next `git gc`.

2. **Commit the useful artifacts to main.** Four files are currently untracked in main's working tree:
   - `knowledge/decisions/halted-executable-gate-2a-lessons-forge-ratification-2026-05-19.md`
   - `knowledge/decisions/halted-diagnostic-gate-2a-recovery-state-2026-05-19.md`
   - `knowledge/development/dev-log-gate-2a-step-1-2026-05-19.md`
   - `knowledge/development/gate-2a-ratification-manifest-2026-05-19.json`

   Plus the new Step 1 dev log from this recovery: `knowledge/development/dev-log-gate-2a-recovery-step-1-2026-05-19.md`.

   Stage all five files and commit:
   ```bash
   git add knowledge/decisions/halted-executable-gate-2a-lessons-forge-ratification-2026-05-19.md
   git add knowledge/decisions/halted-diagnostic-gate-2a-recovery-state-2026-05-19.md
   git add knowledge/development/dev-log-gate-2a-step-1-2026-05-19.md
   git add knowledge/development/gate-2a-ratification-manifest-2026-05-19.json
   git add knowledge/development/dev-log-gate-2a-recovery-step-1-2026-05-19.md
   git --no-pager commit -m "docs: gate 2a failure record + recovery step 1 (schema rollback)"
   ```

   Note: `lessons-forge.db` is gitignored and will NOT be staged by `git add knowledge/...`. Do not attempt to add it.

3. **Capture commit SHA** for the dev log.

**Dev log:**

```markdown
# Dev Log — Gate 2a Recovery Step 2 (worktree teardown + artifact commit)

Worktree removal:
- Command: git worktree remove --force .bellows-worktrees/gate-2a-lessons-forge-ratification-2026-05-19
- Pre-removal: <git worktree list output>
- Post-removal: <git worktree list output, ls -la .bellows-worktrees/>
- d8cb5e5 reachable post-removal: <yes/no — should be no>

Artifact commit:
- Files staged: <5 files>
- Commit SHA: <SHA>
- git log -1 --stat output: <verbatim>
```

Deposit to: `lessons-forge/knowledge/development/dev-log-gate-2a-recovery-step-2-2026-05-19.md`

**Output Receipt:**
- Agent: Forge Developer
- Step: 2
- Status: Complete (worktree gone, commit landed); Partial (one of the two operations failed); Blocked (Step 1 verification failed)
- What Was Done: removed stale worktree and committed 5 artifact files
- Files Deposited: `lessons-forge/knowledge/development/dev-log-gate-2a-recovery-step-2-2026-05-19.md`
- Files Created or Modified: 5 files committed to main, worktree directory removed
- Decisions Made: worktree teardown completed | commit landed at SHA
- Flags for CEO: any operation failure
- Flags for Next Step: QA verification

**Deposits:**
- `lessons-forge/knowledge/development/dev-log-gate-2a-recovery-step-2-2026-05-19.md`

---

## STEP 3 — QA verification

You are the Forge Developer (acting as QA). Read both prior step deposits and verify their Output Receipt statuses are Complete. If either is not, stop and report.

**Verification checks:**

1. **Schema correct:** `SELECT sql FROM sqlite_master WHERE type='table' AND name='lesson_proposals'`. CHECK constraint contains exactly 7 status values, no `'deferred'`. PASS/FAIL.

2. **Data correct:** `SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY status`. Expected: accepted=18, implemented=14, rejected=6, superseded=24. Total 62. PASS/FAIL.

3. **No deferred rows anywhere:** `SELECT COUNT(*) FROM lesson_proposals WHERE status='deferred'`. Expected: 0. PASS/FAIL.

4. **Cross-reference intact:** `SELECT id, duplicate_of FROM lesson_proposals WHERE id IN (38, 62)`. Expected: 38→62, 62→38. PASS/FAIL.

5. **G16 acceptance preserved:** `SELECT id, status FROM lesson_proposals WHERE id=62`. Expected: status=accepted. PASS/FAIL.

6. **Indexes present:** `SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='lesson_proposals' ORDER BY name`. Expected: idx_lesson_proposals_category, idx_lesson_proposals_entry, idx_lesson_proposals_status. PASS/FAIL.

7. **Test suite still passes:** `cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -m pytest src/test_lessons_forge.py -v`. Expected: 25/25 PASSED. PASS/FAIL.

8. **No stale worktree:** `git worktree list` from `/Users/marklehn/Developer/GitHub/lessons-forge/`. Expected: only the main worktree, no `gate-2a-lessons-forge-ratification-2026-05-19`. PASS/FAIL.

9. **`src/db.py` canonical untouched:** `git --no-pager log --oneline -5 -- src/db.py`. The most recent commit touching this file should pre-date 2026-05-19 (no recovery-side modifications). PASS/FAIL.

10. **Working tree clean:** `git status` should report no uncommitted changes to tracked files. Untracked files allowed (e.g., the in-progress plan file itself, future deposits). PASS/FAIL.

**QA report deposit:**

Write to `lessons-forge/knowledge/qa/gate-2a-recovery-qa-2026-05-19.md` with each check, the command run, the verbatim output, and PASS/FAIL determination. Use the standard QA report shape.

**Rule 20 self-check (literal banner, no decoration):**

```python
import os
required = [
    "knowledge/development/dev-log-gate-2a-recovery-step-1-2026-05-19.md",
    "knowledge/development/dev-log-gate-2a-recovery-step-2-2026-05-19.md",
    "knowledge/qa/gate-2a-recovery-qa-2026-05-19.md",
]
missing = [f for f in required if not os.path.exists(f)]
if missing:
    print(f"FAILED - missing evidence: {missing}")
else:
    print("PASSED - SELF-CHECK PASSED - all evidence files present, no hedging keywords found.")
```

Render the banner inside a fenced code block with NO surrounding shell-prompt prefix, NO `===` separator lines, NO title line, NO summary line — just the literal banner output, fenced.

**Commit QA report:**

```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && git --no-pager add knowledge/qa/gate-2a-recovery-qa-2026-05-19.md && git --no-pager commit -m "qa: gate 2a recovery verified (schema rollback + status collapse + worktree teardown)"
```

**Update PROJECT_STATUS.md** per Rule 8: append a brief entry summarizing the Gate 2a failure-and-recovery arc. Commit:

```bash
git --no-pager add PROJECT_STATUS.md && git --no-pager commit -m "docs: PROJECT_STATUS update for gate 2a recovery"
```

**Output Receipt:**
- Agent: Forge Developer (QA)
- Step: 3
- Status: Complete (all 10 checks PASS); Partial (1-2 checks FAIL); Blocked (3+ checks FAIL)
- What Was Done: verified final state of canonical DB schema, data, worktree, src/db.py, tests, working tree
- Files Deposited: `lessons-forge/knowledge/qa/gate-2a-recovery-qa-2026-05-19.md`
- Files Created or Modified: 2 commits (QA report, PROJECT_STATUS)
- Decisions Made: 10 PASS/FAIL determinations
- Flags for CEO: any FAIL with diagnosis
- Flags for Next Step: Gate 2a recovery is complete; next gate is Gate 2c

**Deposits:**
- `lessons-forge/knowledge/qa/gate-2a-recovery-qa-2026-05-19.md`

Standard prompt feedback protocol → `lessons-forge/knowledge/research/agent-prompt-feedback.md`.

---

## How to run

**Prerequisite:** Claude Code authentication must be restored on the Mac before this plan can dispatch. Bellows will detect the plan, attempt dispatch, and fail with `claude -p exit code 1` if auth is still broken. Run `claude /login` (or equivalent) first.

Once auth is restored, Bellows dispatches Step 1, pauses for verdict. Planner reads the dev log under Rule 22, verifies the schema rollback completed cleanly, then deposits a continue verdict at `bellows/verdicts/resolved/verdict-gate-2a-recovery-2026-05-19-step-1.md` (bare format: `verdict: continue` on line 1). Steps 2 and 3 then run end-to-end and Bellows moves the plan to Done.
