# Executable: classification cycle for entries 307–318 (the session-36 twelve) — classify, propose, report; the corpus intake for the post-arc lessons

**Type:** Executable
**Project:** lessons-forge
**Depends on:** executable-339 + executable-340 (lessons-forge, Done — the clone origin pair: the split classification cycle whose machinery this plan inherits at 12/41 scale), executable-348 (Done — v2.4 governs this cycle: the FIRST plan drafted under the touch bar), the session-36 direct ingest (CEO-instructed 2026-08-11: 12 inserted 307–318, 0 updated, 0 staled; backup `pre-ingest-s36-20260811_233218.db` beside the DB), LESSONS.md at parser count 261 (precondition, checked at A0)
**Created:** 2026-08-11
**Author:** Planner
**Slug:** `classify-307-318-2026-08-11`
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T1
**qa_steps:** 2
**Test Scope:** targeted (Rule 21 — single test module, verified this session ×4; QA row 6 re-derives; baseline 55/0)

⚠️ **ID NOTE:** id read from `id_sequence` at deposit (`next_id` read **349** at authoring — a PREDICTION; 347 was consumed in-window by a parallel terminal TODAY, the live proof).

## Why — twelve entries await classification; the pipeline is proven; the batch is pinned

The session-36 sweep found twelve LESSONS entries un-ingested; the CEO-instructed direct ingest landed them as **entries 307–318** (the work list from `get_unclassified_entries`, measured: exactly `[307..318]`, n=12). This plan runs the classification half the ingest deliberately excluded — per-entry proposals + the cycle report — via the 339/340 machinery at a third the batch size. Among the twelve: **317 (the dropped edit-anchor declared addition, now on the §6-proper route)** and **318 (the panel's four doctrine defects, pre-packaged as governance_rule candidates)**.

**Tier justification (T1, stated):** T-6 does not fire — no doctrine file is touched; the writes are corpus-proposal INSERTs (new rows, no flips) plus one report file. The 339/340 batch ran walks at 41 entries with a destructive-step split; this batch is 12 with NO destructive write (INSERT-only — nothing existing changes). T-8 does not fire (proven machinery, third run). **This is the first cycle drafted under the v2.4 bar** — both splits recorded per walk; the touch bar governs the close.

⚠️ **THE BATCH FINGERPRINT IS PINNED AND THE WRAP HAZARD IS LIVE (entry 308 — one of this very batch):** parser count **261**, LESSONS.md sha `f79ea236…` (full sha at A1), last commit `e8a51b5`. **Do not append to LESSONS.md while this plan is deposited un-run** — the A0 delta check HALTs on a moved fingerprint, by design.

## Scope

- **DB writes: INSERT-only** — one+ `lesson_proposals` rows per entry via `insert_proposal` (the module API, same as the lineage), `status='proposed'`, `route` NULL. **No UPDATE to any existing row; no flip; no LESSONS.md touch; no FORWARD touch.** Proposals insert at ids **315+** (proposals MAX(id)=314, measured — the proposal and entry id spaces are separate tables and both sit in the 310s; every log line names WHICH table's id it means).
- **One report:** `reports/lessons-report-2026-08-11.md` via `generate_lessons_report`.
- **Classification rubric (the lineage's, with the live flags):** per entry — category (schema CHECK set), confidence, target_layer/artifact, suggested_action, reasoning; **flag (G) applied per entry** (mechanism-shaped vs discipline-shaped, entry 293's meta-rule — live since Gate 1 2026-08-11); entries already codified by v2.1–v2.4 (312-collapse, 313-reclassify, 315-walk-damage at minimum) are classified HONESTLY as such in the reasoning (the flag-D form) rather than re-proposed as new work.
- ⚠️ **Serialized-dispatch assumption (C14 form):** no concurrent corpus writer; the guards that don't depend on it: A0's counts, the capture, QA's re-derivation.

### Environment facts (the standing four, verbatim from the 346/348 lineage)
1. ugrep shim: `-F` every literal; zero-match `grep -c` prints 0 and exits 1 — the count is the assertion.
2. No shell-state persistence — same-invocation scratch dirs.
3. `find`, never a glob.
4. Canonical absolute DB path only — a bare relative name CREATES an empty DB.

## Freeze checklist (executed at the deposit path, in order, before the copy)
1. Re-token `<LESSONS_SHA…>` to the live `shasum -a 256` of LESSONS.md; region assert: the A1 line carries a 64-hex sha and no angle-bracket token.
2. Read `id_sequence` and substitute at the ONE `<id>` site (the bootstrap line); region assert: the line carries the numeric id and no angle-bracket token.
3. Final `plan_lint` at the deposit-shaped path — WARN set must match the Conformance paragraph exactly.
4. Re-run the A0-fresh checks (work list still exactly the twelve; parser still 261; proposals MAX still 314) — in-window drift shows up HERE, not at dispatch.

## Conflict Ledger
- **C1** anchors/probes count-asserted; **C2** the work list is DERIVED (`get_unclassified_entries`), never hand-typed, and must equal `[307..318]` exactly — more OR fewer → HALT (Rule 47 + the fingerprint); **C3** backup adjacent to the first INSERT, `BK: unclassified=12` restorability by value (`?immutable=1` — the WAL lesson); **C4** per-entry INSERT sentinel: `changes()=1` per call, running tally printed, final `INSERTED=N` with N≥12 and every entry covered ≥1; **C5** capture: pre-state of `lesson_proposals` MAX(id) + count, post-state both, delta = N — no existing row touched proven by `COUNT(*) WHERE status_updated_at IS NOT NULL AND id<=314` unchanged; **C6** the report is generated LAST, from the DB, never hand-edited; **C7** commit pathspec-scoped + name-only assert + cd-first/toplevel per Rule 85 both halves; **C8** Receipt sentinels BY NAME: WORKLIST, PARSER_COUNT, BK, INSERTED, ENTRIES_COVERED, POST_UNCLASSIFIED(=0), PROPOSALS_MAX_POST.

## How to Run This Plan
**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-349.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```
⚠️ HALT ROUTING: Step 1 reads this plan, `/Users/marklehn/Developer/GitHub/LESSONS.md` (fingerprint only), the canonical DB, `lessons-forge/src/lessons_forge.py`. Step 2 reads this plan, the dev-log, the DB (read-only), the merged captures, `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`.

## STEP 1 — DEV (classify the twelve, insert, report)

> **FIRST — visible chat message; do NOT rename this plan file.** You are the Developer.
> **A0 (first match wins):** (1) all 12 entries already have proposals (per-entry `COUNT(*)` from `lesson_proposals WHERE entry_id=E` all ≥1) → verify report exists, RECOVERY receipt, report complete. (2) partial coverage (some entries proposed, some not) → classify ONLY the uncovered remainder, list both sets in the receipt, continue. (3) fresh — `get_unclassified_entries` returns exactly `[307,308,309,310,311,312,313,314,315,316,317,318]` AND `python3` parse of LESSONS.md returns **261** entries AND `sha` of LESSONS.md = the A1 pin → proceed. Any other state (work list ≠ the twelve; parser ≠ 261) → **HALT with the observed values** — a fingerprint delta means the register moved under the pin (entry 308's hazard, detected by design).
> **A1 — pins:** LESSONS.md `shasum -a 256` = `f79ea236bb2ca8614c4c3c96ea7ca04b8f6c56c1d63a91fd240e728dc0c64f69`; `lesson_proposals` MAX(id)=314, `lesson_entries` MAX(id)=318 (measured 2026-08-11; drift → report, and if proposals MAX>314 an in-window writer landed → HALT).
> **B — backup:** `.backup` to `pre-classify-s36-<UTC>.db` beside the DB; restorability BY VALUE via `?immutable=1`: `SELECT 'BK='||COUNT(*) FROM lesson_entries WHERE id BETWEEN 307 AND 318` → **BK=12**.
> **CLASSIFY — for each of the twelve, in id order:** read `raw_content` from the DB (never from LESSONS.md — the corpus is the source); write category/subcategory/confidence/target_layer/target_artifact/suggested_action/reasoning per the 311/342 house rubric; **apply flag (G) in the reasoning** (mechanism vs discipline, with the named observable if mechanism); **apply flag (D) honestly** — 312/313/315 (and any other) whose substance v2.1–v2.4 already codified say so and point at the codifying version rather than proposing duplicate work; insert via `insert_proposal` (module API, one transaction per entry, `changes()=1` asserted per call, running tally). An entry may yield >1 proposal where its halves have different owners (the 267/274 precedent). ⚠️ **Quote-ratio ceiling (the 311/339 lineage guard, dropped by no one this time): per proposal, quoted entry content ≤ 0.80 of the suggested_action+reasoning text, **method stated (Rule 61 ext.): character count of verbatim-copied entry text over total proposal text, agent-computed and reported per proposal plus the batch max — REPORT, never force** (carried calibration: 311's 51 measured 0.102–0.439; the 41-batch peaked 0.748 against the ceiling — the margin now lives at the ceiling end).
> **CAPTURE + sentinels:** pre/post `lesson_proposals` COUNT + MAX(id); `POST_UNCLASSIFIED=0` via the same helper; `COUNT(*) WHERE id<=314 AND status<>'proposed'` unchanged pre→post (no existing row touched — INSERT-only proven, the C5 guard). Deposit raw.
> **REPORT:** `generate_lessons_report(conn, cycle_date='2026-08-11', …)` → `reports/lessons-report-2026-08-11.md`; assert it surfaces ≥12.
> **Receipt** with the SEVEN C8-named sentinels, each BY NAME (an earlier revision said eight of what are seven — the 348 receipt-count class, caught by counting at walk 2) · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`.
> **FINAL ACTION** — commit deposits, cd-first + pathspec + name-only + toplevel print.
>
> **Scope:**
> - `knowledge/development/dev-log-classify-307-318-step-1-2026-08-11.md`
> - `knowledge/qa/evidence/classify-307-318-2026-08-11/pre-post-capture.txt`
> - `knowledge/qa/evidence/classify-307-318-2026-08-11/proposals-readback.txt`
> - `reports/lessons-report-2026-08-11.md`
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-classify-307-318-step-1-2026-08-11.md`
> - `lessons-forge/knowledge/qa/evidence/classify-307-318-2026-08-11/pre-post-capture.txt`
> - `lessons-forge/knowledge/qa/evidence/classify-307-318-2026-08-11/proposals-readback.txt`
> - `lessons-forge/reports/lessons-report-2026-08-11.md`

## STEP 2 — QA

> **FIRST — do NOT rename this plan file. Deliverable Verification (Rule 8/17)**, ✅/❌ table, any ❌ → HALT. **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`; `plan_slug`: `classify-307-318-2026-08-11`; `qa_report_path`: `<tree>/knowledge/qa/classify-307-318-qa-2026-08-11.md`; `evidence_dir`: `<tree>/knowledge/qa/evidence/classify-307-318-2026-08-11/`; `required_evidence_files`: `[qa-db-checks.txt, pytest_targeted.txt]`; both deposited BEFORE the block; literal stdout: the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, byte-exact). Then `## Evidence and Narrative`. ONE read-only DB form; RAW evidence.
> **1.** Per-entry coverage re-derived: every id 307–318 has ≥1 proposal, listed `entry_id|proposal_id|category|confidence|target_artifact`. → `qa-db-checks.txt`
> **2.** `get_unclassified_entries` against the live DB → **empty**, paired with a POSITIVE CONTROL on the same instrument: run the SAME helper against Step 1's pre-classify backup (locate via prefix-only `find /Users/marklehn/Developer/GitHub/lessons-forge -maxdepth 1 -name 'pre-classify-s36-*.db'` — never a glob, env fact 3) via `file:<path>?immutable=1` → returns exactly the twelve — the instrument proven to speak against a known-positive state (⚠️ the pre-INGEST backup returns 0, not 12 — measured at walk 1; the pre-CLASSIFY backup is the control's only valid source). → `qa-db-checks.txt`
> **3.** INSERT-only proven: `COUNT(*) WHERE id<=314 AND status<>'proposed'` equals the Step-1 pre-capture value; total proposals = 314 + INSERTED; every new row `status='proposed'`, `route` NULL. → `qa-db-checks.txt`
> **4.** Report: exists, surfaces ≥12, its per-entry lines match the DB rows (spot-check 3 incl. 317 and 318 by content). → `qa-db-checks.txt`
> **5.** Flag coverage: every new proposal's reasoning carries a flag-(G) reading; the flag-(D) entries (at minimum 312/313/315) cite their codifying version. → `qa-db-checks.txt`
> **6.** Rule 21 premise re-derived (single module) then pytest vs 55/0 — delta reported, never asserted. → `pytest_targeted.txt`
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits, cd-first + pathspec + name-only + toplevel.
>
> **Scope:**
> - `knowledge/qa/classify-307-318-qa-2026-08-11.md`
> - `knowledge/qa/evidence/classify-307-318-2026-08-11/qa-db-checks.txt`
> - `knowledge/qa/evidence/classify-307-318-2026-08-11/pytest_targeted.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/classify-307-318-qa-2026-08-11.md`
> - `lessons-forge/knowledge/qa/evidence/classify-307-318-2026-08-11/qa-db-checks.txt`
> - `lessons-forge/knowledge/qa/evidence/classify-307-318-2026-08-11/pytest_targeted.txt`

---

## Drafting Cycle

**Tier:** T1 — no trigger fires (no doctrine touch, INSERT-only corpus writes, third run of proven machinery); justification in the Why. Clone lineage: 339/340 (the split cycle) at 12/41 scale with no destructive step, flip discipline cross-checked against the 344–348 arc. **The FIRST cycle drafted under the v2.4 bar — the close reads the touch split.**

**Walk 0 (context pin, §2.0):** work list DERIVED = `[307..318]` exactly (n=12); parser count 261; LESSONS sha pinned (re-tokened at freeze); proposals MAX(id)=314 / entries MAX(id)=318 — **the two id spaces collide numerically in the 310s; every sentinel names its table** (pin finding: this is the batch's sharpest confusion hazard); backup lineage verified (`?immutable=1`); no doctrine file in scope → no gate coupling (`plan_lint`/`gates.py` untouched by construction). Register: `governance/knowledge/research/walk-register-classify-307-318-2026-08-11.md`.

**Direction verdict (after walk 1): PROCEED** — no forcing finding: clone origin sound (339/340 Done, machinery API-stable — `insert_proposal` signature verified at source), mechanism sound (module API + INSERT-only), scope licensed (CEO instruction + Rule 47 derivation, work list measured exact).

**Walks:** 3 (swept per culmination).
- Weak spots:          w1 2 folded — instruction 2 / record 0, both pre-existing (the plan had NO freeze checklist while carrying two placeholder classes — the 348 seat-5 class, caught at walk 1 this time; QA row 2's positive control was vague prose — concretized to the helper-against-pre-classify-backup form, and the walk MEASURED the trap: the pre-INGEST backup returns 0, not 12 — only the pre-CLASSIFY backup is a valid control source).
- Destruction:         w1 1 folded — instruction, pre-existing (the lineage's quote-ratio ceiling was DROPPED — restored with the carried calibration: 311's 0.102–0.439, the 41-batch's 0.748 peak against 0.80).
- Vulnerabilities:     w1 executed — no report-path collision (2026-08-11 free); `insert_proposal` signature read at source and matches the rubric fields; the control mechanism proven live against both backup vintages.
- Integration-record:  w1 dry (register schema-conformant from birth; Scope paths match lineage forms; log and register synced this culmination).
- ACID:                w1 dry beyond the freeze fold (INSERT-only means re-runs cannot corrupt existing rows; A0 state 2 prevents duplicate coverage; backup-before-first-INSERT ordering confirmed).

**Walk-1 split: instruction 3 / record 0; origin 3 of 3 pre-existing.** Under the v2.4 bar: instruction-class findings re-open the walk; walk 2 owed.

**Walk 2** (whole artifact; new surface = walk 1's folds):
- Weak spots:          w2 2 folded — instruction 2 / record 0 (the receipt claimed EIGHT of C8's SEVEN named sentinels — counted at the lens, the 348 receipt-count class; QA row 2's backup located via prefix-only `find` per env fact 3, a gap walk 1's own fold introduced).
- Destruction:         w2 dry (walk-1 folds relax nothing; the freeze checklist only adds).
- Vulnerabilities:     w2 executed — the sentinel-name count run as a command (7 measured); lint EXIT 0 stable post-folds.
- Integration-record:  w2 1 folded — instruction (the quote-ratio clause shipped without its method — Rule 61 ext. applied; fold-introduced by walk 1's F2).
- ACID:                w2 dry (the QA-2 control's teardown survival confirmed structural: backups live beside the DB, outside every worktree).

**Walk-2 split: instruction 3 / record 0; origin 2 of 3 fold-introduced, 1 pre-existing.** The walk re-opens; walk 3 owed.

**Walk 3** (whole artifact; new surface = walk 2's folds):
- Weak spots:          w3 dry (walk-2 folds re-read against their sites — the find path matches Task B's destination; the seven-name list internally consistent; A0 ordering intact).
- Destruction:         w3 dry (all walk-2 folds additive).
- Vulnerabilities:     w3 executed — the battery: work list still 12, proposals MAX still 314, parser still 261, LESSONS sha unchanged, lint EXIT 0 with ZERO warnings — the missing-lens WARN cleared EARNED as the per-lens lines landed.
- Integration-record:  w3 1 folded — record, pre-existing (the Conformance paragraph was a placeholder while four lint runs had actually happened — the record catching up to reality; filled with the true history including the earned clear and the zero-warning state). ⚠️ One transient recorded honestly: the walk-3 register rows committed one culmination ahead of these log lines — a tooling abort split the intended single culmination in two; reconciled here, same session, no reader in between.
- ACID:                w3 dry (walk-2's three folds are independent sites; freeze/A0/close ordering re-derived — the close precedes freeze in this plan's own sequence).

**Walk-3 split: instruction 0 / record 1; origin 1 of 1 pre-existing.** ⚠️⚠️ **THE v2.4 BAR IS MET — its first live close: zero instruction-class findings; the record-only yield is the converged-before-its-account signature the bar names.** T1 close: no panel; the close rests on the residue enumeration and the closing-record re-read.

**Closing:** w3 met the v2.4 bar — instruction 0 / record 1: one Conformance-placeholder catch-up, pre-existing, the record lagging four real lint runs; origin split 1 of 1 pre-existing, diagnostic. Residue enumerated: record-class (a) the freeze checklist carries no Closing-form assert — mitigated by ordering, this close precedes the freeze in the same session, and freeze step 3's zero-warning match would flag a placeholder Closing as WARN-set drift; record-class (b) this Closing itself is the close's unreviewed edit, read by the closing-record re-read; record-class (c) the register/log culmination split noted above. Closing-record re-read run: walk splits recompute from the register's seven fold rows — 3/3/1 across walks, instruction 6 / record 1 total; the Walks tracker reads 3; the Conformance history matches the four executed runs. Judged close on the touch bar, fold-and-deposit exactly once.

**Conformance (§5) — run FROM BIRTH (the 348 lesson mechanized into practice): v0, post-walk-1, post-walk-2, walk-3 battery — four runs, EXIT 0 every time.** Zero Scope/deposit/path warnings ever (the 348 catches pre-empted at authoring). The missing-lens WARN stood honestly through v0 and cleared EARNED when the walk-1/2 per-lens lines landed — the §3 disappearance rule's explanation: the lenses genuinely ran. **Current state: EXIT 0, ZERO warnings — the first fully-clean lint state in the lineage** (no conditional resume-sweep artifact is declared, so the standing o1 class has no site). Freeze step 3 matches THIS zero-warning set.

**Closing:** *(written after the final pass; carries `instruction N / record M` per the v2.4 bar.)*
