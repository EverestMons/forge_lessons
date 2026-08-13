# Executable: Gate-1 routing write for proposals 333–336 — all four → `accepted|codify`, per the s40sweep packet

**Type:** Executable
**Project:** lessons-forge
**Depends on:** executable-382 (Done — classified the four, stamps NULL), executable-381 (Done — ingested the batch)
**Created:** 2026-08-13
**Author:** Planner
**Slug:** `gate1-write-333-336-2026-08-13`
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T1
**qa_steps:** 2
**Test Scope:** targeted (Rule 21 — single module, session-verified; QA row 4 re-derives; baseline 55/0)

⚠️ **ID NOTE:** id read at deposit (`next_id` read fresh at the freeze — a PREDICTION, never a mint; the daemon mints at claim).

## Why

Gate 1 for the four is DECIDED — **CEO instruction "proceed with gate 1 as recommended", 2026-08-13, this session, on the packet `gate1-packet-2026-08-13.md` (root `ec3af5a`)** — reversible on CEO review: **A-set `333,334,335,336` → `accepted|codify`**. Per the packet: 333 → DRAFTING_CYCLE §2.6 (the capstone closing condition — partial-carried, residue real); 334 → DRAFTING_CYCLE §2.0/§3 + walk-register schema (record clock + strike — absent by grep); 335 → PLANNER_TEMPLATE (the Rule-85 ops-compound widening); 336 → PLANNER_TEMPLATE QA conventions (the paired-value source check, with the enumeration-tension wording caution carried in-row for Gate 2). **There is NO P-set and NO FORWARD row this run** — nothing routes backlog; the clone origin's Rule-44 pinned-row machinery is dropped with its premise absent (stated at walk 0).

**Dedup against live doctrine (packet, grep-verified 2026-08-13 — licence to disagree granted: A0's live read overrides, HALT + CEO re-decides on any mismatch):** 333 partial-carried (§2.6's new-surface-handoffs bullet lacks the CLOSING condition); 334 absent (`strike`/`record-coherence`/row-at-event: grep 0 in DC); 335 extends Rule 85 (commit compounds covered, ops compounds not); 336 has no carrier (PT's enumeration principle is a different axis — scope coverage vs transcription fidelity; Gate-2 wording must scope both).

⚠️ **Sentinel posture — the cleanest case, RE-MEASURED not inherited: all four prior stamps are NULL** (382's classifier set `proposed_at` only; measured per id 2026-08-13, `status_updated_by` also NULL), so `status_updated_at IS NOT NULL` via the bare Z-GLOB is a complete value guard with **no prior-value exclusion needed**. The GLOB provably matches the representation the UPDATE writes — both rehearsed in one scratch run (GLOBOK_A=4 on the same `strftime('%Y-%m-%dT%H:%M:%SZ','now')` the flip uses); the four-timestamp-forms trap cannot fire here.

## Scope

- **One DB write session, ONE scoped UPDATE in ONE transaction** at the canonical absolute path; `status_updated_by='ceo'` (the Gate-1 authority, lineage convention). No doctrine touch, no LESSONS touch, no FORWARD touch by any step (receipts say `NONE`).
- Env facts: the standing four (ugrep `-F` + zero-count exit-1, printed count is the assertion; same-invocation state; `find` never glob; canonical absolute DB path — a bare relative name CREATES an empty file).
- **Post-write expected corpus (every number measured 2026-08-13, live):** `accepted|codify` = **4** (the new Gate-2 queue), `proposed` = **0**, `reference` STATUS = **15** with route split **9 `reference` + 6 `backlog`** (UNCHANGED — this run writes no reference/backlog row; the six pre-existing backlog-route ids are 161/169/291/294/299/301), `stale` = 3 (98/121/130), implemented = 271, total **336**.

## Freeze checklist (deposit path — items 1–4 BEFORE the copy, item 5 immediately AFTER it)

1. Substitute the read id at the bootstrap `<id>` site; probe, OCCURRENCE form: `grep -oF -- '<id' <deposit-path> | wc -l` → **2** (both residual tokens on this checklist line: the named site and the probe's own literal — measured at the freeze, correcting the drafted 1; the predicted-number class caught by running the probe).
2. **Diff the draft against the mirror immediately before the copy** — an empty diff is the deposit precondition.
3. Final `plan_lint` at the FAITHFUL scratchpad mirror (NEVER the real `decisions/` — the daemon claims AND DISPATCHES same-second, proven live) — WARN set matches the Conformance paragraph.
4. A0-fresh re-check: all four still `proposed` with NULL stamps; `accepted|codify` still 0.
5. Post-copy, same minute: `ls` the real `decisions/` — the claim reads `in-progress-executable-<READ-ID>.md` with the item-1 id (mismatch = foreign in-window consumption — report, never re-copy).

## Conflict Ledger

**C1** the id-set is immutable — a sentinel mismatch is never resolved by editing it. **C2** backup adjacent, `BK=4` by value via `?immutable=1` against THE FOUND BACKUP's absolute path. **C3** capture inside the transaction, before the UPDATE: `id <= 336 AND id NOT IN (333,334,335,336)` → **332 rows** (contiguity measured live). **C4** sentinels BY NAME: PRE, BK, CHANGES_A, GLOBOK_A — FOUR, counted; plus the capture line-count. **C5** commits cd-first + pathspec + name-only + toplevel, post-commit asserts `-C`-pinned to the printed hash, never `HEAD`. **C6** serialized dispatch on THIS project stated — no lessons-forge plan in flight at authoring; **plan 383 (invoice-pulse, parallel terminal) IS in flight and expected: different project, no shared store, not a collision** (the 359-precedent note); non-dependent guards at A0/QA.

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-384.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```
⚠️ HALT ROUTING: Step 1 reads this plan + the canonical DB. Step 2 reads this plan, the dev-log, the DB (read-only), the deposited captures, `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`.

---

## Drafting Cycle

**Tier:** T1 — scoped 4-row routing write, the 350→360 lineage's smallest instance (T-2 fires; structure-for-structure clone keeps T-8 silent); clone of 360's final form — 360 is the direct origin AND the newest same-class Gate-1 routing write (its successor 362 is QA-only corrective, a different class; 362's hardening is carried into Step 2) — with the set, sentinels and capture re-derived from live measurement.

**Walk 0 (context pin):** four rows `proposed|NULL-stamp|NULL-actor` measured per id; capture bound 336−4=**332** (contiguity measured); `accepted|codify`=0, `reference`=15 (route split 9+6 measured, NOT recalled — 360's walk-2 lesson applied at authoring), `stale`=3, implemented=271, total=336; route CHECK admits `codify` (source-read `src/db.py`, the CHECK line); **the full G1/G2 rehearsal ran on a scratch copy at authoring: PRE=4, CHANGES_A=4, GLOBOK_A=4, RERUN_CHANGES=0 (idempotence fail-safe), CAP=332, POST_ACC=4, POST_PROP=0 — every sentinel exact.** Clone-diff vs 360: the P-set machinery DROPPED with its premise absent (no backlog route this run — all four codify; stated in Why); the Rule-44 pinned FORWARD row DROPPED with the same premise (no deferred-work row owed); sentinel count 8→4 (each dropped sentinel named: PRE_A/PRE_P collapse into PRE — one set; CHANGES_P/GLOBOK_P have no object); the reference-split guard carries 360's walk-2 lesson as a MEASURED 9+6 with "unchanged" as the assertion; **362's QA hardening baked in: no Monitor anywhere, pytest FOREGROUND, evidence committed before the Rule 20 block runs**. Scout seat: DECLINED — T1, small surface, the lineage's smallest instance, per precedent.

**Walk 1** (whole artifact, five lenses, sequential):
- Weak spots:          w1 dry (each step's pre/post-conditions carry rehearsed values; the A0 branches cover landed/fresh/other; no unstated assumption found — the decision venue/date is IN the Why per the 373 S1-1 lesson).
- Destruction:         w1 dry (one transaction, all-or-nothing; the two subtractions each carry their measured-absent premise inline; the sentinel reduction is enumerated per dropped sentinel; nothing relaxed — the RERUN=0 fail-safe carried).
- Vulnerabilities:     w1 executed — the rehearsal IS this lens's battery (run at walk 0 on a scratch copy, all sentinels exact); zero-count probes never `&&`-chained; the Z-GLOB/representation identity proven in the same rehearsal; canonical absolute DB path at every site.
- Integration-record:  w1 dry (the decision record cites the packet + commit + CEO wording; dedup table carried from the packet's grep-verified reads; numbering namespaced; deposits blocks name every file).
- ACID:                w1 dry (single write step + QA behind one gate; the NULL-stamp value guard complete without exclusions; half-states owned by A0's branches; backup is the durability floor; capture-inside-transaction carried).

**Walk-1 split: instruction 0 / record 0 — DRY.** Direction verdict: **PROCEED** (clone angle verified; premises measured). ⚠️ A dry walk 1 does not close a cycle that has not yet met the bar on a walk over folded surface — walk 2 confirms.

**Walk 2** (whole artifact; confirming pass, untargeted):
- All five lenses:     w2 dry — instruction 0 / record 0; token sweep clean (no `327`, `331`-as-P-set, `pre-g1cp` residue, `2026-08-12`-dated names, eight-sentinel claims); the confirming pass returned record-class only findings: none at all.

**Walk-2 split: instruction 0 / record 0 — DRY on the artifact as then written.**

**Conformance (§5), first run (freeze item 3):** faithful mirror EXIT 0, ONE (k) WARN — the Tier line's clone framing did not carry the literal newest-same-class naming (the comparison WAS run at walk 0; the naming was absent). Folded: the Tier line now names 360 as origin AND newest same-class with 362 disambiguated as a different class. **Same freeze window: the fresh `next_id` read returned 384, not the session-inferred 383 — plan 383 is the parallel terminal's in-flight invoice-pulse plan; the C6 concurrency premise ("queues empty") was STALE and is corrected to name 383 as expected non-collision. The premise correction is instruction-class — walk 3 owed.**

**Walk 3** (whole artifact; new surface = the two freeze folds):
- All five lenses:     w3 dry — the Tier-line naming is record-accurate (360's successors enumerated, none same-class); the C6 correction relaxes nothing (the single-writer probes remain the guard against lessons-forge collisions; 383 shares no store); no other site carries the stale queues-empty claim (grep-verified); sentinels, sets, and schedule untouched.

**Walk-3 split: instruction 0 / record 0 — DRY. The §2 bar met on the dry branch; T1, no panel owed.**

**Conformance (§5), final run (at deposit):** faithful mirror EXIT 0, **ZERO WARNs** — (k) cleared EARNED; (q) telemetry: the entry-324 sentinel token `ambiguous` (DB value, correct).

**Closing:** walk 3 dry — instruction 0 / record 0; closed on the dry branch after 3 walks; clone-diff at walk 0 per §2.0; scout declined with reasoning; residue: none.

---

## STEP 1 — DEV (the routing write, one transaction)

> **FIRST — visible chat message; do NOT rename this plan file.**
>
> **A0 (first match wins):** (1) the set landed (all four `accepted|codify|ceo`, Z-stamped) → verify per id, RECOVERY receipt if captures lost, report complete. ⚠️ **A partial set-state is UNREACHABLE — G2 is ONE transaction, ONE UPDATE.** (2) fresh — all four `proposed`, stamps NULL, `accepted|codify`=0 → proceed; ⚠️ **a `pre-g1s40-*.db` backup already on this path** (a crash before G2's COMMIT leaves one with nothing written) → REUSE via prefix-only `find` (never a second; >1 match → HALT) and run the `BK=4` assert against it. (3) Other observed state → HALT with the per-id read-back.
>
> **B — backup**, exactly: `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".backup /Users/marklehn/Developer/GitHub/lessons-forge/pre-g1s40-$(date -u +%Y%m%d_%H%M%S).db"` (exit 0, empty stderr); locate via prefix-only `find`; `?immutable=1` assert: `SELECT 'BK='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 333 AND 336 AND status='proposed';` → **BK=4**; else HALT.
>
> **G1 — rehearsal** (runner for G1/G2 alike: `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".read <abs>"`, exit 0 + empty stderr per invocation; file `knowledge/development/g1s40-rehearsal.sql`, exactly):
> ```
> BEGIN IMMEDIATE;
> SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 333 AND 336 AND status='proposed' AND status_updated_at IS NULL;
> ROLLBACK;
> ```
> Assert **PRE=4**; off → HALT naming the ids read back.
>
> **G2 — the write** (`mkdir -p` the evidence dir FIRST; file `knowledge/development/g1s40-flip.sql`, exactly; `.output` absolute from `pwd`):
> ```
> BEGIN IMMEDIATE;
> .output <tree-abs>/knowledge/qa/evidence/gate1-write-333-336-2026-08-13/outside-range-ids.txt
> SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 336 AND id NOT IN (333,334,335,336) ORDER BY id;
> .output stdout
> UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (333,334,335,336) AND status='proposed';
> SELECT 'CHANGES_A='||changes();
> SELECT 'GLOBOK_A='||COUNT(*) FROM lesson_proposals WHERE id IN (333,334,335,336) AND status='accepted' AND route='codify' AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
> COMMIT;
> ```
> **Sentinels CHANGES_A=4, GLOBOK_A=4** (the NULL prior stamps make the bare Z-GLOB a complete value guard — no exclusion, per the Why); any off → HALT with numbers. Capture **332 lines**, read post-commit — mismatch = record + HALT with the write landed, never re-run. The id-set is IMMUTABLE.
>
> **G3 — read-back**, exactly: `sqlite3 -bail -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" "SELECT id||'|'||category||'|'||status||'|'||COALESCE(route,'')||'|'||status_updated_by||'|'||status_updated_at FROM lesson_proposals WHERE id BETWEEN 333 AND 336 ORDER BY id;"` → RAW to `routing-readback.txt`: all four `accepted|codify|ceo|<Z>`.
>
> **Receipt** with FOUR named sentinels — PRE, BK, CHANGES_A, GLOBOK_A — plus the capture line-count (the receipt IS BK's observer) · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: `cd <your-tree-abs>` first token, pathspec on the COMMIT, name-only assert, bare `git rev-parse --show-toplevel` last.
>
> **Scope:**
> - `knowledge/development/dev-log-gate1-write-333-336-2026-08-13.md`
> - `knowledge/development/g1s40-rehearsal.sql`
> - `knowledge/development/g1s40-flip.sql`
> - `knowledge/qa/evidence/gate1-write-333-336-2026-08-13/outside-range-ids.txt`
> - `knowledge/qa/evidence/gate1-write-333-336-2026-08-13/routing-readback.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-gate1-write-333-336-2026-08-13.md`
> - `lessons-forge/knowledge/development/g1s40-rehearsal.sql`
> - `lessons-forge/knowledge/development/g1s40-flip.sql`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-333-336-2026-08-13/outside-range-ids.txt`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-333-336-2026-08-13/routing-readback.txt`
>
> **STOP. Do NOT proceed to Step 2. Wait for verdict.**

## STEP 2 — QA

> **FIRST — do NOT rename this plan file. ⚠️ 362's hardening, verbatim contract: NO Monitor call anywhere in this step; pytest runs FOREGROUND; every evidence file is written AND committed BEFORE the Rule 20 self-check block runs.** Deliverable Verification (Rule 8/17), ✅/❌ table, any ❌ → HALT.
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`; `plan_slug`: `gate1-write-333-336-2026-08-13`; `qa_report_path`: `<tree>/knowledge/qa/gate1-write-qa-2026-08-13.md`; `evidence_dir`: `<tree>/knowledge/qa/evidence/gate1-write-333-336-2026-08-13/`; `required_evidence_files`: `[db-invariants.txt, outside-range-ids.txt, routing-readback.txt, pytest_targeted.txt]`, all four BEFORE the block; literal stdout: the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, byte-exact). `## Evidence and Narrative` after the table. ONE read-only DB form; RAW evidence.
>
> 1. **THE ROUTES LANDED** — per id: 333/334/335/336 `accepted|codify|ceo` Z-stamped. → `routing-readback.txt` (re-run fresh, diff vs the deposited)
> 2. **BLAST RADIUS** — re-run the EXACT capture SELECT (COPY from G2, never re-type), diff vs the deposited 332-line file; partition (impossible-id → HALT; deleted-row → HALT; else concurrent, named, no halt). → `db-invariants.txt`
> 3. **CORPUS SHAPE** — `accepted|codify` = **4** (the new Gate-2 queue); `proposed` = **0**; `reference` STATUS = **15** with route split **9 `reference` + 6 `backlog` UNCHANGED** (the six backlog ids 161/169/291/294/299/301; ⚠️ the value guard is the SPLIT, not the status count); `stale` = 3 (98/121/130); implemented = 271; total = 336. Zero-emitting forms; printed counts are the assertions. → `db-invariants.txt`
> 4. **TESTS** — single-module premise re-derived (`find <tree-abs>/src -name 'test_*.py'` → exactly one; a second = report + run whole `src/`, never HALT); pytest FOREGROUND vs 55/0, delta reported never asserted. → `pytest_targeted.txt`
> 5. **CONSUMER SEMANTICS** — `get_unclassified_entries` (read-only) still `[]` (routing does not un-classify); the four source entries 325–328 present and unchanged (sentinel: entry-324 content-hash `04d2bff7a7bfd9552ef5aab0fd099d81214ed97b8fa1a9ee8082e9c218c88c4a` intact). → `db-invariants.txt`
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits, cd-first + pathspec + name-only + bare toplevel.
>
> **Scope:**
> - `knowledge/qa/gate1-write-qa-2026-08-13.md`
> - `knowledge/qa/evidence/gate1-write-333-336-2026-08-13/db-invariants.txt`
> - `knowledge/qa/evidence/gate1-write-333-336-2026-08-13/pytest_targeted.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate1-write-qa-2026-08-13.md`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-333-336-2026-08-13/db-invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-333-336-2026-08-13/pytest_targeted.txt`
