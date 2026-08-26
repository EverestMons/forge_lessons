# lessons-forge — executable: cycle W=3 — ingest + classify the three new corpus entries (NO routing; Gate 1 follows outside, split by authorship)

**Date:** 2026-08-26 | **Project:** lessons-forge | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (the pins + fresh-connection post-conditions are the instrument; the suite ran green at 549) | **Execution:** Step 1 (DEV — ingest+classify) → Step 2 (QA — report + probes) | **qa_steps:** 2 | **pause_for_verdict:** always

**auto_close:** false

**Depends on:** the CEO's directive ("act on lessons.md, taking the items to the proposed resting place"); the 529/530 clone lineage (ingest/classify split COMBINED here — declared deviation, W=3); plan 549 (canonical-heading keying — the backfill is ingest-invisible, READ from the code at walk 0); the 536-542 arc (every prior proposal terminal — the queue this cycle feeds starts EMPTY).

## CEO Context

**Ingest + classify only — NO ROUTING.** The three proposals this plan mints leave `route` NULL and `status` `proposed`. Gate 1 follows OUTSIDE this plan, split by the 459 non-author law: the 2026-08-25 entry (superset-proof) was authored by session c1f03a88 → the current Planner routes it as non-author (the 536/537 precedent); the two 2026-08-26 entries (doctrine-drift, record-integrity) were authored by THIS session's Planner at its wrap → **the CEO is Gate 1 for those two** (their proposals carry `[AUTHOR-CONFLICT]` markers, date-keyed `entry_date='2026-08-26'`).

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared; measured 2026-08-26 read-only; the agent re-measures each pre-flight; mismatch → HALT with measured vs expected.**

| id | pin | before | after | probe |
|---|---|---|---|---|
| M1 | ingest result | — | EXACTLY `{inserted: 3, updated: 0, unchanged: 345}` | the dict returned by `ingest_lesson_entries` — `updated` > 0 → HALT listing the updated ids (the upsert's update arm is unreachable for this batch: canonical keys + untouched bodies, read from the code) |
| M2 | unclassified | **0** → 3 post-ingest | **0** (the inversion) | `get_unclassified_entries(conn)` on a FRESH read-only connection |
| M3 | P0 proposals | **410, ALL terminal** | 413 | `SELECT COUNT(*) FROM lesson_proposals` |
| M4 | new-proposal band | — | route NULL AND status `proposed`, all 3 | `SELECT COUNT(*) FROM lesson_proposals WHERE id > :MAXP AND (route IS NOT NULL OR status <> 'proposed')` → **0** (MAXP = the captured pre-flight MAX(id), 410 expected — bound, never hard-coded) |
| M5 | pre-existing terminal set | the full `(id, status, route)` triple-set for ids <= 410, captured pre-flight | **SET-IDENTICAL** post (a count cannot see a value move) | full triple-set select, compared as sets |
| M6 | E0 entries | **402** | **405** | `SELECT COUNT(*) FROM lesson_entries` |
| M7 | `[AUTHOR-CONFLICT]` markers | — | **2** (the `entry_date='2026-08-26'` pair, NEVER an id range) | parameter-bound COUNT over the new band's reasoning LIKE '%[AUTHOR-CONFLICT]%' |
| M8 | corpus | 348 parsed; LESSONS.md sha-prefix `f80937e06472600872c2` | **byte-unchanged** | `shasum -a 256 /Users/marklehn/Developer/GitHub/LESSONS.md` — this plan READS the corpus, never writes it |
| M9 | prior reports | 08-25 `0984fdd3521e682c3c0a`; 08-19 `7f9b283bf42a31eb9fca` | **byte-identical** | worktree-anchored shasum; recovery `git checkout -- reports/<file>` (tracked) |
| M10 | today's report | ABSENT | exists at `"$(pwd)/reports/lessons-report-2026-08-26.md"`, none of M9 | ls + shasum, worktree-anchored (⚠️ the 425 trap: NEVER the main-repo absolute path) |

## STEP 1 — DEV (ingest + classify; ONE commit; fresh-connection posts)

> **Task A — worktree discipline + pre-flight.** ⚠️ Your cwd IS the claimed tree — never cd to `/Users/marklehn/Developer/GitHub/lessons-forge`. Open: `cd "$(git rev-parse --show-toplevel)" && test -f src/lessons_forge.py && echo TREE_OK` — HALT unless TREE_OK. ⚠️ The DB is the LIVE `lessons-forge.db` at the MAIN repo — untracked by policy, NOT in the worktree: resolve it as `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (the ONE deliberate absolute operand, matching every prior cycle plan). Pre-flight (read-only connection): M3=410 all-terminal (capture M5's triple-set to the dev log), M6=402, M2=0, M8's sha, AND capture **MAXP** = `SELECT MAX(id) FROM lesson_proposals` (410 expected) and **MAXE** = `SELECT MAX(id) FROM lesson_entries` (⚠️ bind the MEASURED values — a COUNT and a MAX can diverge; every id-band probe below uses the captured MAX, never the count). Any mismatch → HALT with both values. State branch: M3 already 413 AND M2=0 → the cycle landed on a prior run: go to Task C, RECONSTRUCTING the lost in-run values honestly — M5's pre-set = the current triple-set minus the 3 new ids; the M1 dict is unrecoverable verbatim, so the dev log records the POST state with its derivation, LABELED `RECONSTRUCTED (post-commit re-entry)`, never presented as the run's own output.
>
> **Task B — ONE python script (writing connection; NO commit until the end).** (1) `parse_lessons_md('/Users/marklehn/Developer/GitHub/LESSONS.md')` → assert 348 entries; (2) `ingest_lesson_entries(conn, entries)` → assert the M1 dict EXACTLY (`updated` nonzero → rollback, HALT, list the ids); (3) fetch the 3 new entry ids (`SELECT id, source_heading, entry_date FROM lesson_entries WHERE id > :MAXE ORDER BY id` — the captured pre-flight MAX, parameter-bound) → assert exactly 3 rows; (4) for EACH, `insert_proposal(conn, entry_id, category, reasoning)` — categories by the entries' own content: the superset-proof entry → `governance_rule` (a migration-discipline rule candidate); the doctrine-drift entry → `governance_rule` (mechanism-ship sweep rule candidate; note its fix-INSTANCE already discharged by proposal 401's codification — say so in the reasoning); the record-integrity entry → `governance_rule` (the routing law; note its six-site work order already DISCHARGED by plan 552 — the reasoning must say the class half is what remains). Prepend `[AUTHOR-CONFLICT] ` to the reasoning for the two `entry_date='2026-08-26'` rows. Route stays NULL, status stays `proposed`. (5) ONE `conn.commit()`. (6) POSTS on a FRESH read-only connection: M2=0, M3=413, M4=0, M6=405, M7=2, M5 triple-set SET-IDENTICAL.
>
> **Task C — dev log + commit.** `knowledge/development/dev-log-cycle-w3-2026-08-26.md`: the M5 pre-flight triple-set, the M1 dict verbatim, one `DISPOSITION | entry=<id> | proposal=<id> | category=<c> | markers: <AUTHOR-CONFLICT-or-NONE>` line PER entry (byte-exact prefix, exactly three), the fresh-connection post raws. Commit (WORKTREE toplevel): `cd "$(git rev-parse --show-toplevel)" && git add knowledge/development/dev-log-cycle-w3-2026-08-26.md && git commit -m "[<id from your plan filename>] forge-cycle-w3(forge-cycle-w3-2026-08-26): ingest 3 + classify 3 — route NULL, 2 author-conflict markers" -- knowledge/development/dev-log-cycle-w3-2026-08-26.md && git rev-parse HEAD` — **CAPTURE_COMMIT**.
>
> **Deposits:**
> - `knowledge/development/dev-log-cycle-w3-2026-08-26.md`
>
> **Scope:**
> - `knowledge/development/dev-log-cycle-w3-2026-08-26.md`

## STEP 2 — QA (report + probes)

> **Item 1 — the report.** `cd "$(git rev-parse --show-toplevel)"`; python: `generate_lessons_report(conn, "2026-08-26", output_dir=os.path.join(os.getcwd(), "reports"))` (⚠️ the 425 trap — worktree-anchored, NEVER the main-repo path); M10 probes (exists, none of M9); M9 shasums byte-identical; commit the report: `git add reports/lessons-report-2026-08-26.md && git commit -m "[<id>] forge-cycle-w3: cycle report" -- reports/lessons-report-2026-08-26.md`.
> **Item 2 — DB probes on a FRESH read-only connection:** M2/M3/M4/M6/M7 re-run raw; M5 triple-set re-selected SET-IDENTICAL vs the dev log's capture; M8's corpus sha unchanged. Raw → `knowledge/qa/evidence/forge-cycle-w3-2026-08-26/probes-raw.txt`.
> **Item 3 — hygiene + receipt** `knowledge/qa/evidence/forge-cycle-w3-2026-08-26/qa-receipt.md`: numstats (step-1 commit 1 file; report commit 1 file); toplevel; reflog `-n 5` → 0 amends; per-item table + the Rule 20 block.
>
> ⚠️ **Gate note (pre-declared):** probe-battery QA, no pytest scope — the benign class (18th precedent); the Planner overrides with reference here.
>
> **Deposits:**
> - `reports/lessons-report-2026-08-26.md`
> - `knowledge/qa/evidence/forge-cycle-w3-2026-08-26/probes-raw.txt`
> - `knowledge/qa/evidence/forge-cycle-w3-2026-08-26/qa-receipt.md`
>
> **Scope:**
> - `reports/lessons-report-2026-08-26.md`
> - `knowledge/qa/evidence/forge-cycle-w3-2026-08-26/probes-raw.txt`
> - `knowledge/qa/evidence/forge-cycle-w3-2026-08-26/qa-receipt.md`

Rule 20 banner (byte-exact, inside the QA receipt's verification section):

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
```

## Drafting Cycle

**Tier:** T1 — the 529/530 lineage combined (declared deviation, W=3); the inherited halt-autopsy restated at walk 0; every write-path claim read from the code.

**Walk register:** `lessons-forge/knowledge/research/walk-register-forge-cycle-w3-2026-08-26.md`

**Walk 0 (context pin, measured):** P0=410 all-terminal; E0=402; unclassified 0; corpus 348 sha-pinned READ-ONLY; ingest result pinned EXACTLY {3,0,345} from the code's own write path; markers date-keyed =2; the 425 report trap restated; the corpus-freeze inversion declared (this deposit IS the freeze); id prediction 556.

**Walks:**
- Weak spots:          w1 1 folded — (C1) the new-row fetches keyed on `id > <count>` where COUNT and MAX(id) can diverge (the count-is-not-a-value-guard class): both bands re-keyed on pre-flight-captured MAXE/MAXP, parameter-bound.
- Destruction:         w1 1 folded — (C2) a post-commit death loses the in-memory M1 dict and M5 pre-set: the re-entry arm reconstructs with the derivation, LABELED, never presented as the run's own output (the no-fabrication law applied to lifecycle records).
- Vulnerabilities:     w1 dry — the ingest's update arm pinned to 0 fail-loud with the write-path derivation; the trailing-separator hash invariance READ from `_normalize_for_hash`'s own docstring; category `governance_rule` validated by the 542-arc precedent.
- Integration-record:  w1 dry — the Gate-1 authorship split stated in CEO Context with per-entry destinations; the discharged-instance notes (401 for doctrine-drift, 552 for record-integrity) mandated INTO the proposal reasonings so Gate 1 reads them.
- ACID:                w1 dry — one commit; fresh-connection posts; the M5 set-identity guard carried from 530's M6.
- **Walk 1 total: two findings, both folded.**
- Weak spots:          w2 dry — the bound-parameter forms re-read; every pin re-verified against the live DB this authoring.
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
class: register-writing
reads: /Users/marklehn/Developer/GitHub/LESSONS.md, /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db, /Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py
writes: lessons-forge.db (untracked), knowledge/development/dev-log-cycle-w3-2026-08-26.md, reports/lessons-report-2026-08-26.md, knowledge/qa/evidence/forge-cycle-w3-2026-08-26/probes-raw.txt, knowledge/qa/evidence/forge-cycle-w3-2026-08-26/qa-receipt.md
open_forks: Gate 1 (outside this plan, split by authorship: the 08-25 proposal → this Planner as non-author; the two 08-26 proposals → the CEO); Gate 2 codification for whatever Gate 1 accepts
walks: 2
yields: 2, 0
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=N/A
coherence: N/A
