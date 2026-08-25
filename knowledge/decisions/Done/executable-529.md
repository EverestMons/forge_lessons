# lessons-forge — executable: the post-08-19 ingest — 32 new entries, fingerprint-gated, no migration

**Date:** 2026-08-25 | **Project:** lessons-forge | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (one library-call ingest with sentinel gating; evidence deposit) | **Execution:** Step 1 (DEV) | **Priority:** 1

**auto_close:** false
**pause_for_verdict:** after_step_1

**Depends on:** `knowledge/research/forge-heading-key-migration-2026-08-25.md` (diagnostic-528 — BINDING: its M-3 batch fingerprint and M-4 spec are this plan verbatim; its scratch-DB rehearsal already produced exactly this result). **Ruling applied (528 M-6 Q1, recommended option under the standing directive):** the 57 removed-from-file entries stay as historical corpus — this plan does NOT touch them.

## Why this exists

The cycle-nudge (56 plans closed since 2026-08-19) is answered by ingesting the true batch the diagnostic measured: **32 new entries, 0 updates, 313 unchanged** — the heading-key hazard the Planner feared was already fixed by plans 499/500's `_key_heading`, so this is a clean append.

## What this plan does NOT do

- **No heading migration, no UPDATE, no proposal manipulation** (528 M-2/M-4: the update path never fires — would_update 0).
- **No classification cycle** (Gate 1/Gate 2 work is its own future plan class; this is ingest only — `ingested_at` moves, the nudge quiets).
- **No deletion or retirement of the 57 historical rows.**

## Numbers discipline

⚠️ **All values are 528's rehearsal-measured fingerprint (M-3, scratch-DB run of the REAL functions); the step RE-DERIVES each live and GATES the commit on exact match — a mismatch means the world moved since the census, and the answer is rollback + halt, never proceed.**

| id | pin | value | probe |
|---|---|---|---|
| I1 | pre-state | entries **370**, proposals **378**, MAX(id) **370**, MAX(ingested_at) 2026-08-19T17:18:13 | SELECTs before anything |
| I2 | the fingerprint | inserted **32** / updated **0** / unchanged **313** / stale_proposals_marked **0** / terminal_proposals_flagged **[]** | the return of the REAL `ingest_lesson_entries` |
| I3 | post-state | entries **402**, proposals **378** (unchanged), new id band **371-402** sequential | SELECTs after commit |
| I4 | parser | `parse_lessons_md` yields **345** entries from the register | the parser is the authority — never grep counts |
| I5 | the DB | `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — UNTRACKED; ⚠️ ABSENT from your worktree | ALL DB operations against this absolute path — this plan's SANCTIONED live-state write, backup-gated |
| I6 | the register | `/Users/marklehn/Developer/GitHub/LESSONS.md` — root repo, outside your worktree | absolute path read |

## MUST-PRESERVE

- ⚠️ **THE GREP SHIM IS BROKEN (every form errors): `/usr/bin/grep` only; zero-match exits 1, never &&-chain. But this plan's probes are SELECTs and the parser — prefer those.**
- ⚠️ **BACKUP BEFORE ANY WRITE:** `cp /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db /Users/marklehn/Developer/GitHub/lessons-forge/pre-ingest-2026-08-25-<HHMMSS>.db` — verify the copy's size equals the source before proceeding (the house `pre-<slug>-<ts>.db` convention).
- ⚠️ **TRANSACTION-WRAPPED, SENTINEL-GATED:** the ingest runs inside one transaction; print the returned fingerprint BEFORE commit; commit ONLY on exact I2 match; ANY deviation → `ROLLBACK`, report the measured values, END THE STEP as blocked — never commit a mismatched ingest, never retry.
- ⚠️ **The evidence deposit carries RAW output** (the printed fingerprint, the pre/post SELECTs, the id-band listing) — not summaries.
- ⚠️ **EVERY DATE IS A FIXED LITERAL. Worktree dispatch; the deposit write is project-relative; the DB and register are absolute (I5/I6).**

## STEP 1 — DEV: backup, ingest, verify

**Role:** DEV.

1. **Pre-state (I1):** `sqlite3` SELECTs against the live DB (absolute path): entry count, proposal count, MAX(id), MAX(ingested_at). All four must match I1 — a mismatch means another actor touched the corpus since the census: STOP, report, do not proceed.
2. **Backup** per MUST-PRESERVE; record the filename and byte size.
3. **Ingest:** python against the absolute paths — `sys.path.insert` the project's `src/`, `parse_lessons_md(<I6>)` (assert len == 345 per I4), open the live DB read-write, `BEGIN`, `ingest_lesson_entries(conn, entries)`, PRINT the returned dict, compare to I2 exactly; on match `COMMIT`, on any deviation `ROLLBACK` and stop as blocked.
4. **Post-verification (I3):** entry count 402; proposal count 378; `SELECT id, substr(source_heading,1,70) FROM lesson_entries WHERE id >= 371 ORDER BY id` — 32 rows, sequential band, all dated 2026-08-19..2026-08-25; MAX(ingested_at) is now today's timestamp (quote it — this is the value that quiets the cycle-nudge).
5. **Evidence deposit:** `knowledge/research/forge-ingest-32-evidence-2026-08-25.md` (project-relative in your worktree) with the raw output of every numbered item above.

> **QA SELF-CHECK — Rule 20.** Post the block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` verbatim, under the banner **`Rule 20 — QA Self-Check Results`**, and close with **`PASSED — SELF-CHECK PASSED`** only if every check genuinely passed. ⚠️ Both literals are matched by `plan_lint` check (c) and neither may be paraphrased.

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/forge-ingest-32-evidence-2026-08-25.md`

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/forge-ingest-32-evidence-2026-08-25.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`
- `/Users/marklehn/Developer/GitHub/lessons-forge/pre-ingest-2026-08-25-*.db`

**Commit:** `git add knowledge/research/forge-ingest-32-evidence-2026-08-25.md && git commit -m "[<id>] ingest: 32 post-08-19 entries (fingerprint-gated; 370->402, proposals 378 unchanged)"` in YOUR worktree cwd — the DB and backup are untracked by policy and are NOT added.

## Drafting Cycle
**Tier:** T1 computed — one sentinel-gated library call, rehearsed by 528 on a scratch copy.
**Walk register:** `governance/knowledge/research/walk-register-executable-forge-ingest.md`
**Walks:** walk 0 pinned; **walks 1–2 complete** — five lenses each; walk 1 folded 1 (the manifest backup-name form), walk 2 dry across all five lenses.
**Direction verdict (after walk 1): PROCEED.** Tested, not judged.
- Weak spots:          w1 dry; w2 dry
- Destruction:         w1 dry; w2 dry
- Vulnerabilities:     w1 dry; w2 dry
- Integration-record:  w1 dry; w2 dry — close obligations discharged at this freeze
- ACID:                w1 1 folded — record 1 / instruction 0; w2 dry
**Cold panel: NOT convened, decided with reasoning** — the operation is 528's rehearsal replayed against the live DB with the identical fingerprint gate; the panel's cost exceeds the residual risk the backup+rollback+sentinel stack leaves.
**Conformance (§5):** recorded at the freeze from actual runs: walk_register_lint CONFORMANT (verdict channel, branched-on); cycle_check BAR_MET post-finalization (verdict channel, branched-on); plan_lint 0 FAIL at the lintmirror deposit path.
**Closing:** **walk 2 met the bar — all five lenses dry.** Instruction series **1 → 0**. Receipt BEFORE staging (structural since 527) → shop-infra hold → release under the CEO's ingestion directive → claim.

## Cycle Manifest
tier: T1
target: lessons-forge.db
class: shop-infra
reads: /Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py, /Users/marklehn/Developer/GitHub/LESSONS.md, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/forge-heading-key-migration-2026-08-25.md
writes: lessons-forge.db, pre-ingest-2026-08-25-HHMMSS.db, knowledge/research/forge-ingest-32-evidence-2026-08-25.md
open_forks: none — 528's Q1 ruled (keep historical) under the standing directive
walks: 2
yields: 1, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=N/A
coherence: N/A

## Rule 20 — QA Self-Check Block

Single DEV step; the Rule 20 block is posted inside the evidence deposit per item 5.
