# Executable: Gate-1 routing write for proposals 315–326 — 8 → `accepted|codify`, 4 → `reference|reference`, per the 2026-08-11 packet

**Type:** Executable
**Project:** lessons-forge
**Depends on:** executable-349 (Done — inserted the twelve as `proposed`, stamps NULL), executable-342 (Done — the routing-write lineage), the Gate-1 packet `/Users/marklehn/Developer/GitHub/gate1-packet-2026-08-11.md` (the decisions; provenance — the plan pins the sets, no step reads it), executable-348 (v2.4 governs)
**Created:** 2026-08-11
**Author:** Planner
**Slug:** `gate1-write-315-326-2026-08-11`
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T1
**qa_steps:** 2
**Test Scope:** targeted (Rule 21 — single module, session-verified ×5; QA row 4 re-derives; baseline 55/0)

⚠️ **ID NOTE:** id read at deposit (`next_id` **350** at authoring — a PREDICTION).

## Why
Gate 1 for the twelve is DECIDED (packet, 2026-08-11, CEO-instructed, Planner-taken, reversible): **A-set** `315,316,317,318,319,324,325,326` → `accepted|codify`; **R-set** `320,321,322,323` → `reference|reference`. This plan writes it — two scoped UPDATEs, both sets IMMUTABLE INPUTS. ⚠️ **The cleanest sentinel case in the lineage: all twelve prior stamps are NULL** (349's classifier inserts set `proposed_at` only — measured), so `status_updated_at IS NOT NULL AND` Z-GLOB is a complete value guard with **no prior-value exclusion needed** — stated so nobody clones one in.

## Scope
- **One DB write session, two scoped UPDATEs** at the canonical absolute path; `status_updated_by='ceo'` (the Gate-1 authority, lineage convention). No doctrine touch, no LESSONS touch, no FORWARD touch, no report.
- Env facts: the standing four (ugrep `-F`/zero-count exit-1; same-invocation state; `find` never glob; absolute DB path).
- **Post-write expected corpus:** `accepted|codify`=8, `reference|reference`=9 (5+4), `proposed`=0.

## Freeze checklist (at the deposit path, before the copy)
1. Substitute the read id at the ONE `<id>` site (bootstrap); region assert: numeric id, no angle-bracket token.
2. Final `plan_lint` — WARN set must match the Conformance paragraph.
3. A0-fresh re-check: all twelve still `proposed` with NULL stamps; `accepted|codify` still 0.

## Conflict Ledger
**C1** both id-sets immutable — a sentinel mismatch is never resolved by editing them. **C2** backup adjacent, `BK=12` by value via `?immutable=1`. **C3** capture inside the first UPDATE's transaction, before it: `id <= 326 AND id NOT IN (<the twelve>)` → **314 rows** (326 − 12; ids contiguous, measured). **C4** sentinels BY NAME: PRE, PRE_A, PRE_R, BK, CHANGES_A, GLOBOK_A, CHANGES_T, CHANGES_R, GLOBOK_R — NINE, counted (T = the 325 target reversal). **C5** commit cd-first + pathspec + name-only + toplevel (Rule 85 both halves). **C6** serialized-dispatch stated; non-dependent guards: A0 counts, capture, QA re-derivation.

## How to Run This Plan
**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-350.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```
⚠️ HALT ROUTING: Step 1 reads this plan + the canonical DB. Step 2 reads this plan, the dev-log, the DB (read-only), the merged captures, `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`.

## STEP 1 — DEV (the two routing writes)

> **FIRST — visible chat message; do NOT rename this plan file.**
> **A0 (first match wins):** (1) all three writes landed (A-set `accepted|codify`, R-set `reference|reference`, 325's target `DRAFTING_CYCLE.md`) → verify, RECOVERY receipt if captures lost, report complete. ⚠️ **A partial set-state (A done, R not) is UNREACHABLE — G2 is ONE transaction; all three UPDATEs commit atomically** (walk 2 removed the branch v0 carried for it, Rule 62's unreachable-machinery class). (2) fresh — all twelve `proposed`, stamps NULL, `accepted|codify`=0 → proceed; ⚠️ **if a `pre-gate1w-*.db` backup already exists on this path** (a crash before G2's COMMIT leaves one with nothing written), REUSE it via prefix-only `find` and run the `BK=12` assert against it rather than minting a second. Other observed state → HALT with the values.
> **B — backup**, exactly: `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".backup /Users/marklehn/Developer/GitHub/lessons-forge/pre-gate1w-$(date -u +%Y%m%d_%H%M%S).db"` (exit 0, empty stderr); locate via prefix-only `find`; `?immutable=1` assert `SELECT 'BK='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 315 AND 326 AND status='proposed'` → **BK=12**; else HALT.
> **G1 — rehearsal** — runner form for G1 and G2 alike: `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".read <abs-path>"`, exit 0 + empty stderr asserted per invocation (same-invocation scratch dir outside git trees). **(file `knowledge/development/gate1w-rehearsal.sql`, exactly):**
> ```
> BEGIN IMMEDIATE;
> SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 315 AND 326 AND status='proposed' AND status_updated_at IS NULL;
> SELECT 'PRE_A='||COUNT(*) FROM lesson_proposals WHERE id IN (315,316,317,318,319,324,325,326) AND status='proposed';
> SELECT 'PRE_R='||COUNT(*) FROM lesson_proposals WHERE id IN (320,321,322,323) AND status='proposed';
> ROLLBACK;
> ```
> Assert **PRE=12, PRE_A=8, PRE_R=4**; any off → HALT naming the set.
> **G2 — the writes (file `knowledge/development/gate1w-flip.sql`, exactly; `.output` absolute from `pwd`, `mkdir -p` the evidence dir FIRST):**
> ```
> BEGIN IMMEDIATE;
> .output <tree-abs>/knowledge/qa/evidence/gate1-write-315-326-2026-08-11/outside-range-ids.txt
> SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 326 AND id NOT IN (315,316,317,318,319,320,321,322,323,324,325,326) ORDER BY id;
> .output stdout
> UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (315,316,317,318,319,324,325,326) AND status='proposed';
> SELECT 'CHANGES_A='||changes();
> SELECT 'GLOBOK_A='||COUNT(*) FROM lesson_proposals WHERE id IN (315,316,317,318,319,324,325,326) AND status_updated_at IS NOT NULL AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
> UPDATE lesson_proposals SET target_artifact='DRAFTING_CYCLE.md' WHERE id = 325 AND target_artifact='PLANNER_TEMPLATE.md';
> SELECT 'CHANGES_T='||changes();
> UPDATE lesson_proposals SET status='reference', route='reference', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (320,321,322,323) AND status='proposed';
> SELECT 'CHANGES_R='||changes();
> SELECT 'GLOBOK_R='||COUNT(*) FROM lesson_proposals WHERE id IN (320,321,322,323) AND status_updated_at IS NOT NULL AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
> COMMIT;
> ```
> **Sentinels: CHANGES_A=8, GLOBOK_A=8, CHANGES_T=1 (the 325 target reversal — packet routes the edit-anchor rule to DRAFTING_CYCLE §2.7 against the classifier's PLANNER_TEMPLATE, the 293-precedent, walk-1 catch), CHANGES_R=4, GLOBOK_R=4; any off → HALT with the numbers.** Capture **314 lines**, read post-commit — mismatch = record + HALT with the writes landed, never re-run. `-bail` + exit-0 + empty-stderr per invocation (same-invocation scratch dir outside git trees). NO prior-value exclusion — the twelve's stamps were NULL (measured); IS-NOT-NULL + GLOB is complete.
> **G3 — read-back** (`-readonly`), exactly: `sqlite3 -bail -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" "SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(target_artifact,'')||'|'||status_updated_by||'|'||status_updated_at FROM lesson_proposals WHERE id BETWEEN 315 AND 326 ORDER BY id;"` → RAW to `flip-readback.txt`; the A-set rows `accepted|codify|ceo|<Z>`, the R-set `reference|reference|ceo|<Z>`.
> **Receipt** with the NINE C4-named sentinels · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits (cd-first, pathspec, name-only, toplevel).
>
> **Scope:**
> - `knowledge/development/dev-log-gate1-write-step-1-2026-08-11.md`
> - `knowledge/development/gate1w-rehearsal.sql`
> - `knowledge/development/gate1w-flip.sql`
> - `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/outside-range-ids.txt`
> - `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/flip-readback.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-gate1-write-step-1-2026-08-11.md`
> - `lessons-forge/knowledge/development/gate1w-rehearsal.sql`
> - `lessons-forge/knowledge/development/gate1w-flip.sql`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-315-326-2026-08-11/outside-range-ids.txt`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-315-326-2026-08-11/flip-readback.txt`

## STEP 2 — QA

> **FIRST — do NOT rename this plan file. Deliverable Verification (Rule 8/17)**, ✅/❌, any ❌ → HALT. **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`; `plan_slug`: `gate1-write-315-326-2026-08-11`; `qa_report_path`: `<tree>/knowledge/qa/gate1-write-qa-2026-08-11.md`; `evidence_dir`: `<tree>/knowledge/qa/evidence/gate1-write-315-326-2026-08-11/`; `required_evidence_files`: `[qa-db-checks.txt, pytest_targeted.txt]`, both deposited BEFORE the block; literal stdout incl. the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, byte-exact). Then `## Evidence and Narrative`. ONE read-only DB form; RAW evidence.
> **1.** Per-set read-back re-derived: A-set 8/8 `accepted|codify`, R-set 4/4 `reference|reference`, all `ceo`, all Z-stamped; set comparison BY IDS, not counts — **and 325's `target_artifact` = `DRAFTING_CYCLE.md`** (the Gate-1 reversal; the other eleven targets unchanged from classification, asserted per id). → `qa-db-checks.txt`
> **2.** Corpus totals: `accepted|codify`=8, `reference|reference`=9, `proposed`=0 — each WITH a positive control on the same instrument (the pre-gate1w backup via `?immutable=1`, located via prefix-only `find`, shows the twelve `proposed`). → `qa-db-checks.txt`
> **3.** Blast radius: re-run the EXACT capture SELECT from G2's block (COPY it, never re-type), diff vs the deposited 314-line file; partition (impossible-id → HALT; deleted-row → HALT; else concurrent, named, no halt). → `qa-db-checks.txt`
> **4.** Rule 21 premise re-derived; pytest vs 55/0, delta reported never asserted. → `pytest_targeted.txt`
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits (cd-first, pathspec, name-only, toplevel).
>
> **Scope:**
> - `knowledge/qa/gate1-write-qa-2026-08-11.md`
> - `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/qa-db-checks.txt`
> - `knowledge/qa/evidence/gate1-write-315-326-2026-08-11/pytest_targeted.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate1-write-qa-2026-08-11.md`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-315-326-2026-08-11/qa-db-checks.txt`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-315-326-2026-08-11/pytest_targeted.txt`

---

## Drafting Cycle

**Tier:** T1 — no trigger fires (no doctrine touch; a 12-row two-set status write with proven machinery — the 342 lineage at fifth run). Clone lineage: 342 (the routing write) with every hardening from the 344–349 arc applied at authoring.

**Walk 0 (context pin, §2.0):** sets pinned from the committed packet (`d08110b`); prior stamps measured **all NULL** (the no-exclusion sentinel case, stated); capture bound 326−12=**314** (contiguity measured); `accepted|codify`=0 pre-write; backup lineage `?immutable=1`; no gate coupling (no doctrine tokens in scope). Register: `governance/knowledge/research/walk-register-gate1-write-2026-08-11.md`.

**Direction verdict (after walk 1): PROCEED** — no forcing finding: origin sound (342 lineage, fifth run), mechanism sound (two-set UPDATE + sentinels), licence sound (the committed packet). Walk 1's target-reversal catch is a scope CORRECTION inside the licence, not a licence failure.

**Walks:** 3 (swept per culmination).
- Weak spots:          w1 1 folded — instruction, pre-existing (the three sqlite invocations were referenced, not spelled — runner forms now verbatim with `.timeout 5000`).
- Destruction:         w1 1 folded — instruction, pre-existing, THE CATCH: **the plan wrote no `target_artifact` reversal while the packet routes 325 to DRAFTING_CYCLE against the classifier's PLANNER_TEMPLATE** (queried: the mismatch is real; the other eleven match). The 293-precedent applied: a third scoped UPDATE with its own CHANGES_T=1 sentinel; sentinels now NINE, counted; G3 and QA row 1 carry the target column.
- Vulnerabilities:     w1 executed — the A-set targets queried against the packet (one mismatch found = the fold above); `reference|reference`=5 confirmed; lint EXIT 0 post-folds.
- Integration-record:  w1 dry (register conformant from birth; synced this culmination).
- ACID:                w1 dry post-fold (UPDATE-T rides the same transaction between A and R; its predicate self-guards re-runs; A0 states cover the new half-state via the existing partial branch).

**Walk-1 split: instruction 2 / record 0; origin 2 of 2 pre-existing.** The walk re-opens; walk 2 owed.

**Walk 2** (whole artifact; new surface = walk 1's folds):
- Weak spots:          w2 1 folded — instruction, pre-existing (A0's partial state was UNREACHABLE — G2 is one transaction, verified by construction; the branch removed per Rule 62, and the real crash residue — a backup with nothing written — gains its REUSE path).
- Destruction:         w2 dry (walk-1 folds relax nothing; the A0 restructure removes only unreachable machinery and adds a guard).
- Vulnerabilities:     w2 executed — battery: twelve still proposed/NULL, `accepted|codify` 0, `reference|reference` 5; lint EXIT 0.
- Integration-record:  w2 1 folded — record, pre-existing (the Conformance placeholder filled with the real from-birth history — one walk earlier than 349's identical catch-up).
- ACID:                w2 dry (the two-state machine + single transaction re-derived; nine sentinels consistent across G2/C4/Receipt/QA).

**Walk-2 split: instruction 1 / record 1; origin 2 of 2 pre-existing.** The walk re-opens on the instruction finding; walk 3 owed.

**Walk 3** (whole artifact; new surface = walk 2's folds):
- Weak spots:          w3 dry (the restructured A0 read whole: two states + REUSE, BK on both paths; nine sentinels counted consistent at all four sites).
- Destruction:         w3 dry — the removed-branch sweep EXECUTED: zero references to the excised state survive anywhere in the plan.
- Vulnerabilities:     w3 executed — battery stable (twelve proposed/NULL, acc 0); lint EXIT 0 with ZERO warnings (the missing-lens WARN cleared EARNED as the walk lines landed).
- Integration-record:  w3 dry (log/register synced; Conformance already current from walk 2's warm fill).
- ACID:                w3 dry (single-transaction atomicity + the two-state machine re-derived unchanged).

**Walk-3 split: instruction 0 / record 0 — a LITERAL DRY PASS, the bar's first branch.** The cycle closes dry.

**Closing:** full walk 3 dry — instruction 0 / record 0; last event = lens pass. The v2.4 bar's second live close, and the FIRST on the dry branch (349 closed on record-only). Trajectory instruction 2→1→0 across three walks, all six findings pre-existing, zero fold-introduced the whole cycle — the cleanest register of the lineage. Closing-record re-read run: the four register fold rows recompute to the stated splits (2/2 across walks 1–2), the Walks tracker reads 3, the Conformance history matches the four executed lint runs, sentinel counts consistent at every site. Residue: none owed beyond this Closing itself, which the re-read covers. Fold-and-deposit exactly once.

**Conformance (§5) — run from birth: v0 (caught the compacted header as a deposit-blocking FAIL before any walk — the parser reads line-per-field), post-walk-1, walk-2 battery — EXIT 0 since the header fix, ONE earned WARN (missing per-lens lines) clearing as the walk lines land.** Filled at walk 2, one walk earlier than 349 managed — the record catching up while the cycle is still warm.

**Closing:** *(after the final pass, v2.4 form.)*
