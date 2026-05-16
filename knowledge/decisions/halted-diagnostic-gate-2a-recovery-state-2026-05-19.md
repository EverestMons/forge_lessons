# Diagnostic: Gate 2a Recovery — State Enumeration

**Plan slug:** diagnostic-gate-2a-recovery-state-2026-05-19
**Plan type:** diagnostic
**Project:** lessons-forge
**Specialist:** Forge Developer
**Auto-close:** false
**Priority:** 1
**Depends on:** none
**Created:** 2026-05-19

---

## Context

Gate 2a executable (`executable-gate-2a-lessons-forge-ratification-2026-05-19`) halted at Step 2 verdict gate with a layered failure:

1. **Plan latent defect:** the plan called for 'deferred' as a target status, but the `lesson_proposals.status` CHECK constraint does not allow 'deferred' (only `proposed/accepted/rejected/ambiguous/stale/superseded/implemented`).
2. **Agent improvisation:** when the agent hit the constraint failure, it modified `src/db.py` and (presumably) migrated the live DB's CHECK constraint to add 'deferred', then applied the 25 writes. This is exactly the failure mode in LESSONS 2026-05-14 (G6, already Gate 1 accepted).
3. **Worktree cherry-pick failed:** the worktree commit `236109b` could not merge back to main because Step 1's deposit files exist as untracked in the main working tree.

Step 2's dev log (in the worktree at `.bellows-worktrees/gate-2a-lessons-forge-ratification-2026-05-19/knowledge/development/dev-log-gate-2a-step-2-2026-05-19.md`) claims:
- Transaction applied: 25 writes, deltas accepted +18, deferred +2, rejected +4, superseded +1
- Status distribution after: `accepted=18, deferred=2, implemented=14, rejected=4, superseded=24`
- Commit: `236109b`
- "Schema required adding 'deferred' to CHECK constraint"

What is unclear: which DB file received the writes (canonical Mac repo or worktree copy), whether the schema mutation reached the canonical DB, and whether `src/db.py` was modified on the canonical Mac path.

**Decision (locked before diagnostic):** Recovery will collapse 'deferred' → 'rejected' for G5 and I3, since 'rejected' semantically covers "this proposal didn't advance in this Gate 1 cycle" without implying permanent removal. Schema mutation must be rolled back. Worktree commit must be discarded. Plan must be re-authored with corrected dispositions and re-run.

This diagnostic enumerates the exact current state so the recovery executable can be surgical.

---

## STEP 1 — Enumerate canonical state

You are the Forge Developer. Read `forge/agents/FORGE_DEVELOPER.md` and `lessons-forge/CLAUDE.md`. Operate against `/Users/marklehn/Developer/GitHub/lessons-forge/`. **Do not modify anything in this diagnostic.** All operations are read-only. Do not run any code that writes to disk, modifies git state, runs migrations, or alters the worktree. If you find any state that you believe is wrong, REPORT it in the findings — do not fix it.

**Five questions to answer (in order):**

### Q1 — Canonical DB schema

Run against `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`:

```sql
SELECT sql FROM sqlite_master WHERE type='table' AND name='lesson_proposals';
```

Report the full DDL verbatim. Specifically extract the `status` column's CHECK constraint and list its allowed values. Determine: does the constraint include `'deferred'`, yes or no?

### Q2 — Canonical DB data

Run against `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`:

```sql
SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY status;
SELECT id, status, status_updated_by, status_updated_at, duplicate_of
FROM lesson_proposals
WHERE id IN (38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62)
ORDER BY id;
```

Report both result sets verbatim. The first gives the overall distribution; the second gives the 25 rows the manifest targeted. Determine: are any of the 25 rows in a non-`proposed` status? If yes, list them. If all 25 are still `proposed`, state so explicitly.

### Q3 — Canonical src/db.py state

Read `/Users/marklehn/Developer/GitHub/lessons-forge/src/db.py` and locate the `lesson_proposals` table DDL. Report the full `status` column line verbatim. Determine: does the canonical file's CHECK constraint include `'deferred'`, yes or no?

Cross-reference: also report the line numbers for the `status` column in both:
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/db.py` (canonical)
- `/Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/gate-2a-lessons-forge-ratification-2026-05-19/src/db.py` (worktree)

Report them side-by-side so the diff is visible.

### Q4 — Worktree commit contents

Inside the worktree at `/Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/gate-2a-lessons-forge-ratification-2026-05-19/`, run:

```bash
git --no-pager log --oneline -10
git --no-pager show 236109b --stat
git --no-pager show 236109b -- src/db.py
```

Report verbatim. The `--stat` shows which files the commit touches; the `-- src/db.py` shows the actual diff to the schema file. If `lessons-forge.db` is in the changed files list, that confirms the writes landed in the worktree's DB. Determine: does the worktree commit modify (a) `src/db.py`, (b) `lessons-forge.db`, (c) anything else?

### Q5 — Worktree branch divergence

Inside the worktree, run:

```bash
git --no-pager status
git --no-pager log --oneline main..HEAD
git --no-pager log --oneline HEAD..main
```

The first shows working-tree state. The second shows commits in worktree HEAD that are NOT in main. The third shows commits in main that are NOT in worktree HEAD. Report all three verbatim. Determine: is the worktree HEAD ahead of main, behind, or both?

Also report what `cat .git/HEAD` resolves to inside the worktree (the branch or detached SHA the worktree is checked out on).

---

## Findings deposit

Write findings to `lessons-forge/knowledge/research/gate-2a-recovery-state-2026-05-19.md`. Structure:

```markdown
# Gate 2a Recovery — State Diagnostic Findings (2026-05-19)

## Q1 — Canonical DB schema
[full DDL verbatim, CHECK constraint extracted, includes-deferred determination]

## Q2 — Canonical DB data
[both result sets verbatim, per-row status, determination]

## Q3 — Canonical src/db.py vs worktree src/db.py
[canonical line, worktree line, determination]

## Q4 — Worktree commit 236109b
[git log oneline, git show --stat, git show -- src/db.py, determinations]

## Q5 — Worktree branch divergence
[git status, ahead commits, behind commits, HEAD resolution, determination]

## Synthesis
- Did writes land in canonical DB? Yes/No
- Did schema mutation land in canonical DB? Yes/No
- Did canonical src/db.py change? Yes/No
- Is worktree commit 236109b discardable cleanly? Yes/No (with reasoning)
- Recovery shape recommendation: [discard worktree | cherry-pick selected files | other]
```

**No code changes. No DB writes. No git commits. Read-only diagnostic.**

**Output Receipt:**
- Agent: Forge Developer
- Step: 1
- Status: Complete (all five questions answered with verbatim outputs); Partial (if any tool failed); Blocked (if cannot read canonical files)
- What Was Done: enumerated current state of canonical DB schema, canonical DB data, canonical src/db.py, worktree commit, and worktree branch divergence
- Files Deposited: `lessons-forge/knowledge/research/gate-2a-recovery-state-2026-05-19.md`
- Files Created or Modified: none
- Decisions Made: synthesis section with five Yes/No determinations and a recovery-shape recommendation
- Flags for CEO: any unexpected state (e.g., schema mutated but writes not applied, or vice versa); any tool failure
- Flags for Next Step: Planner reads findings via Rule 22 and authors recovery executable

**Deposits:**
- `lessons-forge/knowledge/research/gate-2a-recovery-state-2026-05-19.md`

Standard prompt feedback protocol → `lessons-forge/knowledge/research/agent-prompt-feedback.md`.
