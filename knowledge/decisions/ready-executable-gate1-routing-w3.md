# lessons-forge — executable: Gate-1 routing W=3 — proposals 411/412/413 flip proposed → accepted|codify (411 planner-as-non-author; 412/413 CEO-ruled)

**Date:** 2026-08-26 | **Project:** lessons-forge | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (structural SQL gates are the instrument — the 538-542 flip form) | **Execution:** Step 1 (DEV — the flip) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

**auto_close:** false

**Depends on:** plan 556 (Done — the three proposals exist, route NULL, status proposed, 2 AUTHOR-CONFLICT markers); the Gate-1 rulings of 2026-08-26: **411** accept|codify by the current Planner AS NON-AUTHOR (entry 403 = session c1f03a88's authorship — the 536/537 precedent; the superset class verified absent from doctrine before ruling); **412 and 413** accept|codify by the **CEO** (this session authored their entries — the 459 law; rulings given in-session, verbatim: both "accept | codify (Recommended)" selections).

## CEO Context

This plan writes the THREE routing rows exactly as ruled and nothing else. Gate-2 codification (PT rules + the accepted→implemented flip) is the SERIAL follow-up plan.

## Numbers discipline

⚠️ **Measured 2026-08-26; the agent re-measures pre-flight; mismatch → HALT.**

| id | pin | before | after | probe |
|---|---|---|---|---|
| M1 | the band {411,412,413} | all `proposed`, route NULL | all `accepted`, route `codify` | per-row select |
| M2 | stamps | — | 411 `status_updated_by='planner'`; 412/413 `='ceo'`; one shared UTC `status_updated_at` | per-row select |
| M3 | everything else | every id <= 410 terminal | **untouched** — the full (id,status,route) triple-set for id <= 410 SET-IDENTICAL pre/post | full select, compared as sets |
| M4 | totals | P=413; accepted=0 | P=413; accepted=3 | COUNT probes |

## STEP 1 — DEV (the flip under structural gates)

> **Task A — worktree + pre-flight.** `cd "$(git rev-parse --show-toplevel)" && test -f src/lessons_forge.py && echo TREE_OK` — HALT unless TREE_OK. DB = `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (the one absolute operand). Pre-flight read-only: the band all proposed/NULL; accepted=0; capture M3's triple-set to the dev log. Already accepted=3 with the M2 stamps → prior run: skip to Task C's commit-check.
>
> **Task B — the flip SQL, ONE `sqlite3 -bail` invocation** (⚠️ `-bail` LOAD-BEARING — without it a failed CHECK still commits; **CHANGES_F is the only wrong-write betrayer**). Write `knowledge/development/g1w3-flip.sql`:
>
> ```sql
> BEGIN IMMEDIATE;
> CREATE TEMP TABLE g_pre(x INTEGER CHECK(x=3));
> INSERT INTO g_pre SELECT COUNT(*) FROM lesson_proposals WHERE id IN (411,412,413) AND status='proposed' AND route IS NULL;
> UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='planner' WHERE id = 411 AND status='proposed';
> UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (412,413) AND status='proposed';
> SELECT 'CHANGES_F='||changes();
> CREATE TEMP TABLE g_post(x INTEGER CHECK(x=0));
> INSERT INTO g_post SELECT COUNT(*) FROM lesson_proposals WHERE id IN (411,412,413) AND NOT (status='accepted' AND route='codify');
> SELECT 'ACC='||COUNT(*) FROM lesson_proposals WHERE status='accepted';
> COMMIT;
> ```
>
> Run: `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".read $(pwd)/knowledge/development/g1w3-flip.sql"` — expect **CHANGES_F=2** on the second UPDATE's changes() print (⚠️ changes() reports the LAST statement only: the 411 UPDATE is 1 row, the pair UPDATE is 2 — the printed value is 2; the g_post CHECK is the full-band guard), ACC=3, exit 0. Any CHECK failure aborts pre-COMMIT with full rollback. POSTS on a FRESH read-only connection: M1/M2/M4 per-row + counts, M3 triple-set SET-IDENTICAL.
>
> **Task C — dev log + commit.** `knowledge/development/dev-log-g1w3-2026-08-26.md` (the rulings restated with their sources, M3 pre-set, raw SQL output, fresh-connection posts). Commit (WORKTREE toplevel): `cd "$(git rev-parse --show-toplevel)" && git add knowledge/development/g1w3-flip.sql knowledge/development/dev-log-g1w3-2026-08-26.md && git commit -m "[<id from your plan filename>] gate1-routing-w3(gate1-routing-w3-2026-08-26): 411/412/413 proposed -> accepted|codify (planner x1 non-author, ceo x2)" -- knowledge/development/g1w3-flip.sql knowledge/development/dev-log-g1w3-2026-08-26.md && git rev-parse HEAD` — **CAPTURE_COMMIT**.
>
> **Deposits:**
> - `knowledge/development/g1w3-flip.sql`
> - `knowledge/development/dev-log-g1w3-2026-08-26.md`
>
> **Scope:**
> - `knowledge/development/g1w3-flip.sql`
> - `knowledge/development/dev-log-g1w3-2026-08-26.md`

## STEP 2 — QA

> **Item 1 — fresh-connection probes:** M1 per-row (three rows verbatim), M2 stamps (411 planner / 412 ceo / 413 ceo; three IDENTICAL status_updated_at values), M3 triple-set vs the dev log's capture, M4 counts (P=413, accepted=3). Raw → `knowledge/qa/evidence/gate1-routing-w3-2026-08-26/probes-raw.txt`.
> **Item 2 — flip replay aborts:** re-running the committed SQL on the live DB must abort at the g_pre INSERT (`CHECK constraint failed` — x=0 against CHECK(x=3)) with zero state change (paste the abort + a re-select proving no drift).
> **Item 3 — hygiene + receipt** `knowledge/qa/evidence/gate1-routing-w3-2026-08-26/qa-receipt.md`: numstat 2 files; toplevel; reflog `-n 4` → 0 amends; per-item table, then the Rule 20 block INSIDE a section whose heading contains the word "Verification" (⚠️ the 556 placement artifact: the gate scans only verification-headed sections).
>
> ⚠️ **Gate note (pre-declared):** probe-battery QA, no pytest scope — the benign class (19th precedent); the Planner overrides with reference here.
>
> **Deposits:**
> - `knowledge/qa/evidence/gate1-routing-w3-2026-08-26/probes-raw.txt`
> - `knowledge/qa/evidence/gate1-routing-w3-2026-08-26/qa-receipt.md`
>
> **Scope:**
> - `knowledge/qa/evidence/gate1-routing-w3-2026-08-26/probes-raw.txt`
> - `knowledge/qa/evidence/gate1-routing-w3-2026-08-26/qa-receipt.md`

Rule 20 banner (byte-exact, inside the QA receipt's VERIFICATION section — see Item 3's placement law):

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
```

## Drafting Cycle

**Tier:** T1 — the 538-542 flip form at W=3; the 556 banner-placement artifact folded as a stated Item-3 law.

**Walk register:** `lessons-forge/knowledge/research/walk-register-gate1-routing-w3-2026-08-26.md`

**Walk 0 (context pin, measured):** the band verified proposed/NULL live; stamps law from the schema's own CHECK constraint; the changes()-reports-last-statement caveat stated at the CHANGES_F pin; id prediction 557.

**Walks:**
- Weak spots:          w1 1 folded — ⚠️ (R1, CRITICAL) the drafted gates used `CASE/CAST('…' AS INTEGER)`, which SQLite evaluates to 0 SILENTLY — both structural gates were DECORATIVE (a check you print but don't branch on, in SQL form). Refit to the proven 538-552 mechanism: `CREATE TEMP TABLE g(x INTEGER CHECK(...)); INSERT … SELECT COUNT(*)` — the INSERT itself fails the CHECK and `-bail` aborts pre-COMMIT (the 552 EXECUTION seat rehearsed exactly this abort live).
- Destruction:         w1 dry — one transaction; replay aborts at the g_pre INSERT; the prior-run resume arm keys on the M2 stamps.
- Vulnerabilities:     w1 dry — the two-statement UPDATE split keeps per-actor stamps honest; CHANGES_F=2 pinned WITH the changes()-reports-last-statement derivation; g_post is the full-band guard.
- Integration-record:  w1 dry — both CEO rulings + the non-author ruling restated with sources; the 556 banner-placement law folded into Item 3.
- ACID:                w1 dry — M3 set-identity carried; fresh-connection posts.
- **Walk 1 total: one finding (critical), folded.**
- Weak spots:          w2 dry — the refit SQL traced statement-by-statement; the CHECK-INSERT abort path is the 552-rehearsed mechanism.
- Destruction:         w2 dry.
- Vulnerabilities:     w2 dry.
- Integration-record:  w2 dry.
- ACID:                w2 dry.
- **Walk 2 total: 0 findings — all five lenses dry.**

**Closing:** ✅ **BAR MET at walk 2 — dry confirming pass, all five lenses.** T1 two-walk form; no direction-class finding; close is MANUAL (CEO-lane verdicts).

**Fold-and-deposit exactly once.**

## Cycle Manifest
tier: T1
target: lessons-forge/lessons-forge.db
class: shop-infra
reads: /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db
writes: lessons-forge.db (untracked), knowledge/development/g1w3-flip.sql, knowledge/development/dev-log-g1w3-2026-08-26.md, knowledge/qa/evidence/gate1-routing-w3-2026-08-26/probes-raw.txt, knowledge/qa/evidence/gate1-routing-w3-2026-08-26/qa-receipt.md
open_forks: Gate-2 codification (PT v4.96: the three rules + the accepted->implemented flip) — the SERIAL follow-up
walks: 2
yields: 1, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=N/A
coherence: N/A
