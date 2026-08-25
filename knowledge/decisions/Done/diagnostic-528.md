# lessons-forge — diagnostic: the relabel broke the corpus keys — heading migration census + the real ingestion batch, settled before any ingest runs

**Date:** 2026-08-25 | **Project:** lessons-forge | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (read-only diagnostic; writes one research doc) | **Execution:** Step 1 (DIAGNOSTIC) | **Priority:** 1

**auto_close:** false
**pause_for_verdict:** after_step_1

**Depends on:** the 15:25 cycle-nudge (56 plans closed since the 2026-08-19 ingestion) and the Planner's pre-authoring dry run that BLOCKED the naive ingest. **The measured hazard this settles:** the 2026-08-23 relabel-codified campaign rewrote `LESSONS.md` heading lines with `[status: …]` / `[target: …]` suffixes AFTER the last forge ingestion — the corpus's `UNIQUE(source_file, source_heading)` keys now mismatch the file almost totally (dry run, real parser: 345 parsed, 370 DB rows, would_insert **331**, unchanged **14**, db-only **356**). Running `ingest_lesson_entries` today would insert 331 near-duplicates and orphan 356 keyed rows with their 378 proposals — corpus corruption, not ingestion. The relabel arc's own QA guarded only "no forge cycle ran between steps" (D12=370); the key migration is UNOWNED until this diagnostic specs it.

## Why this exists

The heading is the corpus's JOIN KEY, and the relabel changed the keys in the file without migrating them in the DB — the never-combine-differing-sets class at corpus scale. The fix is a key MIGRATION (update `source_heading` in place, ids and proposals untouched) followed by the genuine post-08-19 ingest — but the mapping, its collisions, the content-drift residue, and the interaction with the known trailing-separator hash trap must be measured before an executable mutates 356 rows.

## What this plan does NOT do

- **It runs NO ingest and NO migration.** Read-only: the DB via `mode=ro`, the register read, one research deposit.
- **It does not touch LESSONS.md or the relabel deposits.**

## Numbers discipline

⚠️ **Measured 2026-08-25 by the Planner with the REAL parser/normalizer against the live DB (mode=ro); RE-DERIVE each — yours supersede and you say so.**

| id | pin | value | probe |
|---|---|---|---|
| F1 | the dry-run diff | parsed 345 / DB 370 / would_insert 331 / would_update 0 / unchanged 14 / db-only 356 | `parse_lessons_md` + `_normalize_for_hash` (src/lessons_forge.py:59, :34) against `/Users/marklehn/Developer/GitHub/LESSONS.md` and the DB's (source_heading, content_hash) set |
| F2 | the divergence class, exemplified | DB `…full stop  [tag: bellows-integration] [tag: planner-discipline]` vs FILE same + ` [status: codified] [target: PLANNER_TEMPLATE.md]` — the file heading EXTENDS the DB heading | the relabel campaign's suffix grammar; measured on the `Verdict response directory` entry |
| F3 | the key constraint | `UNIQUE(source_file, source_heading)`; `lesson_proposals` reference `entry_id` (heading changes cannot break the FK — verify, don't assume) | `.schema lesson_entries`; `.schema lesson_proposals` |
| F4 | proposals at risk | **378** proposals in the DB | `SELECT COUNT(*) FROM lesson_proposals` |
| F5 | the hash-trap history | the trailing-separator whitespace-hash trap was ROOT-CAUSE-FIXED 2026-07-16 (`_normalize_for_hash` at :34; the staling guard story in NEXT_SESSION.md's headline) | read both; the migration analysis leans on normalized hashes being whitespace-stable |
| F6 | last ingestion | `MAX(ingested_at)` = 2026-08-19T17:18:13 | the cycle-nudge's own source (bellows.py `_get_last_ingestion_ts`) |
| F7 | forge DB location | `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — UNTRACKED (shop policy; CLAUDE.md) | ⚠️ the split-path law: absent from any dispatch worktree; ALL DB reads via the absolute live path, `mode=ro` |

## MUST-PRESERVE

- ⚠️ **READ-ONLY.** The single deposit is the write set. DB strictly `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro"`. Any scratch-DB rehearsal works on a `cp` under your scratch dir, absolute paths, same invocation as use.
- ⚠️ **THE GREP SHIM IS BROKEN (every form errors `unknown option '-G'`): `/usr/bin/grep` for ALL probes; zero-match exits 1 — never &&-chain; an errored probe is the shim, not an absence.**
- ⚠️ **THE SPLIT-PATH LAW (F7):** the DB, `LESSONS.md` (root repo), and the governance relabel deposits all live OUTSIDE your worktree — absolute paths for every read. Your deposit write is project-relative in the worktree.
- ⚠️ **Every claim cites file:line or a run command with raw output; every absence claim carries a positive control. EVERY DATE IS A FIXED LITERAL.**

## STEP 1 — DIAGNOSTIC: the mapping census, the migration spec, the true batch

**Role:** DIAGNOSTIC.

Produce `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/forge-heading-key-migration-2026-08-25.md` (project-relative in your worktree) settling AT LEAST the following, with a Rule 27 gap table:

**M-1 — the mapping census.** Using the REAL `parse_lessons_md` + `_normalize_for_hash`: for every db-only row, attempt the match against parsed entries by (a) suffix-stripped heading equality (define the strip grammar from the relabel's actual token set — measure which suffix tokens occur: `[status: …]`, `[target: …]`, others?) and (b) normalized content hash. Classify EVERY db-only row into: **heading-migrated** (suffix-only change, content hash equal), **heading-migrated+content-drifted** (heading maps but hash differs — measure the drift: the F5 trailing-separator class should be EXTINCT post-fix; anything else is real and listed), **removed-from-file** (no mapping — enumerate; the file may legitimately have retired entries), **ambiguous** (multiple candidates — the fatal class for an UPDATE; must be zero or each resolved by hand in the deposit). Symmetrically classify every parsed-new row: **migration-counterpart** vs **genuinely-new** (the true post-F6 batch — list them ALL with dates; expect the 2026-08-21/23/24/25 sweep-era entries).
**M-2 — the migration mechanics.** The executable's UPDATE shape: `UPDATE lesson_entries SET source_heading = ? WHERE id = ?` per mapped row (id-keyed, never heading-keyed — the value being changed is the worst possible WHERE key, the assert-after-mutation lesson); the UNIQUE-collision pre-check (no target heading may already exist — measure now); proposals untouched by construction (F3 — verify the FK direction with the schema, state it); the content-drifted arm's handling (update heading AND hash? or heading only, letting the follow-up ingest's update path refresh content — ⚠️ trace `ingest_lesson_entries`'s update path's PROPOSAL-STALING side effect (the F5 story's `WHERE entry_id=? AND status != 'stale'` demotion) and state whether it still demotes on content updates — this decides whether the migration must refresh hashes itself to avoid staling proposals).
**M-3 — the true ingestion batch.** After a SCRATCH-DB rehearsal of the migration (cp the DB, apply the M-1 mapping, re-run the dry diff): the residual would_insert/would_update/unchanged — the honest batch the follow-up executable ingests. Expected shape: would_insert == the genuinely-new count, would_update == the drifted arm, unchanged == the rest.
**M-4 — the executable spec.** Steps, verification arms (the 397-precedent disciplines: parser-diff authority, id-band statements, the batch fingerprint, dry-run-then-live with rollback file), and the safety rails (pre-migration DB backup file per the house `pre-<slug>-<ts>.db` convention visible in the repo root).
**M-5 — the relabel-side residue.** Did the relabel campaign leave OTHER consumers keyed on old headings (the 506/507 TSV mapping's `entry_heading` column — measure whether its 14 rows match the CURRENT file headings post-relabel, or whether that deposit is now stale too)? List every heading-keyed consumer found (`/usr/bin/grep -rln -F "entry_heading"` run over `/Users/marklehn/Developer/GitHub/lessons-forge/` and `/Users/marklehn/Developer/GitHub/governance/knowledge/research/`) and classify each.
**M-6 — open questions.** Forks needing a ruling — LISTED, never decided silently (candidate: the removed-from-file rows' disposition — keep as historical corpus vs mark retired).

**Post-conditions:** every M-section grounded in run commands with raw output; the F-pins re-derived or superseded with measurement shown; M-1's classification covers all 356+331 rows with ZERO unexplained; the Rule 27 gap table enumerates the executable's change sites.

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/forge-heading-key-migration-2026-08-25.md`

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/forge-heading-key-migration-2026-08-25.md`

**Commit:** `git add knowledge/research/forge-heading-key-migration-2026-08-25.md && git commit -m "[<id>] diag: forge heading-key migration — relabel broke the corpus keys; mapping census + migration spec + true batch"` in YOUR worktree cwd.

## Drafting Cycle
**Tier:** T1 computed — read-only single-deposit diagnostic.
**Walk register:** `governance/knowledge/research/walk-register-diagnostic-forge-key-migration.md`
**Walks:** walk 0 pinned; **walks 1–2 complete** — five lenses each; walk 1 folded 1 (the M-5 command), walk 2 dry across all five lenses.
**Direction verdict (after walk 1): PROCEED.** Tested, not judged.
- Weak spots:          w1 1 folded — instruction 1 / record 0; w2 dry
- Destruction:         w1 dry; w2 dry
- Vulnerabilities:     w1 dry; w2 dry
- Integration-record:  w1 dry; w2 dry — close obligations discharged at this freeze
- ACID:                w1 dry; w2 dry
**Cold panel: NOT convened, decided with reasoning** — the E-family rule; read-only diagnostics close on warm walks (515-526 precedent).
**Conformance (§5):** recorded at the freeze from actual runs: walk_register_lint CONFORMANT (verdict channel, branched-on); cycle_check BAR_MET post-finalization (verdict channel, branched-on); plan_lint 0 FAIL at the lintmirror deposit path.
**Closing:** **walk 2 met the bar — all five lenses dry.** Instruction series **1 → 0**. The deposit travels the lane with the receipt ritual — ⚠️ now STRUCTURALLY ENFORCED (527 live): receipt BEFORE staging, and this deposit is the arm's happy-path canary → predicted depositor auto-clear (class read-only) → claim.

## Cycle Manifest
tier: T1
target: knowledge/research/forge-heading-key-migration-2026-08-25.md
class: read-only
reads: /Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py, /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db, /Users/marklehn/Developer/GitHub/LESSONS.md, /Users/marklehn/Developer/GitHub/lessons-forge/NEXT_SESSION.md, /Users/marklehn/Developer/GitHub/governance/knowledge/research/relabel-codified-qa-2026-08-23.md, /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/Done/executable-397.md
writes: knowledge/research/forge-heading-key-migration-2026-08-25.md
open_forks: none authored here — M-6 carries any that surface
walks: 2
yields: 1, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=N/A
coherence: N/A

## Rule 20 — QA Self-Check Block

This step is DIAGNOSTIC-only; no QA agent runs. The Rule 20 self-check block is N/A for this step. Verification happens at the Planner's Rule 22 substance check after verdict consumption.
