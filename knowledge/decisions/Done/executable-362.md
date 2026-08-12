# Executable: QA-only corrective for the Gate-1 routing write (plan 360's step 2) — the Rule 20 block that never ran

**Type:** Executable
**Project:** lessons-forge
**Depends on:** executable-360 (HALTED at step 2 — its STEP 1 IS COMMITTED AND CORRECT: the routing writes verified per id by the Planner at both gates; only the QA process failed), executable-359/357 (Done — the batch lineage)
**Created:** 2026-08-12
**Author:** Planner
**Slug:** `gate1-write-327-332-2026-08-12-qa-corrective`
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T1
**qa_steps:** 1
**Test Scope:** targeted (Rule 21 — single module; row 4 re-derives; baseline 55/0)

⚠️ **ID NOTE:** id read at deposit (`next_id` **362** at authoring — a PREDICTION; 358/361 went to the parallel terminal; the freeze reads fresh).

## Why
Plan 360's step 2 gate-failed on `rule_20_self_check` and the failure was VERIFIED REAL: the deposited QA report carries no Rule 20 banner — the mandatory block never ran. The substantive verification was otherwise present, and **step 1's writes are committed and Planner-verified per id** (327/328/329/330/332 `accepted|codify|ceo`, 331 `reference|backlog|ceo`, all stamped `2026-08-12T17:12:07Z`). Per the QA-process-failure convention (the 328→329 precedent): **stop + a QA-ONLY corrective against the committed state — never re-run the full plan onto already-written rows.** This plan is that corrective: ONE QA step, the same five verification rows, with the Rule 20 machinery this time — commit-evidence-first, foreground suite, no Monitor.

## Scope
- **Read-only everywhere:** the canonical DB via `?mode=ro` ABSOLUTE path only; no writes to any table, any doctrine file, LESSONS.md, or any FORWARD register.
- The QA report path OVERWRITES plan 360's incomplete report (same path — the complete version, with the banner; the incomplete one is preserved in git history).
- Env facts: the standing four (ugrep `-F` + zero-count exit-1; same-invocation state; `find` never glob; absolute DB path).

## Freeze checklist (deposit path — items 1–3 BEFORE the copy, item 4 immediately AFTER)
1. Substitute the read id at the bootstrap `<id>` site; probe: `grep -oF -- '<id' <deposit-path> | wc -l` → **2** (both residual tokens on this checklist line).
2. **Diff the draft against the mirror immediately before the copy** — empty diff is the deposit precondition.
3. Final `plan_lint` at the FAITHFUL scratchpad mirror — WARN set matches the Conformance paragraph. A0-fresh: the six rows still in their routed states (per-id).
4. Post-copy, same minute: `ls` the real `decisions/` — the claim carries the item-1 id.

## Conflict Ledger
**C1** the six routed rows are READ, never written — a mismatch HALTs, nothing repairs. **C2** the report overwrite is the intended deliverable (git history preserves the incomplete predecessor). **C3** commits cd-first + pathspec + name-only + bare toplevel; post-commit asserts pin the printed hash, never `HEAD`.

## How to Run This Plan
**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-362.md (the daemon renames on claim). Execute Step 1 ONLY. This is the plan's only step.
```

---

## Drafting Cycle

**Tier:** T1 — read-only single-step QA corrective; the mutating work is DONE and verified, this plan writes only its own report/evidence.

**Walk 0 (context pin):** the six rows re-measured per id at authoring (all in routed states, stamps `2026-08-12T17:12:07Z`); `accepted|codify`=5, `proposed`=0, `reference` 16 with the 9+7 route split; capture file 326 lines on main; entry sentinel 318 intact; the incomplete QA report + both evidence files on main from 360's step 2 (git-preserved). Clone origin: 360's own step-2 text (this plan IS that step, corrected) — the ONE change class: the Rule 20 machinery made first-class with its ordering spelled, and A0 narrowly keyed to the committed writes.

**Walk 1** (whole artifact, five lenses, sequential):
- Weak spots:          w1 dry (the A0 key is per-id, not a count; every expected value carries its measured source).
- Destruction:         w1 dry (read-only plan; the report overwrite is deliberate and git-preserved — stated).
- Vulnerabilities:     w1 executed — all five row queries rehearsed live read-only at authoring (values as pinned); the Rule 20 block's four placeholders resolve; the ordering trap (report-then-block-then-append) spelled from RULE_20_SELF_CHECK_BLOCK.md's own sys.exit behavior.
- Integration-record:  w1 dry (the corrective convention followed: stable slug + `-qa-corrective` suffix, narrowly-keyed A0, never-rerun-the-full-plan stated; the 360 halt disposition cross-referenced).
- ACID:                w1 dry (one read-only step; the only write is its own deposit; no window).

**Walk-1 split: instruction 0 / record 0 — DRY at walk 1. The §2 bar met on the dry branch; T1, no panel owed.**

**Conformance (§5):** run at shape-stability and at deposit, at the faithful mirror — fidelity here requires `knowledge/development/g1cp-flip.sql` copied in (row 2 references it; it lives on the real main from 360's step 1; a bare mirror shows one (o1) path WARN, a fidelity artifact). **Measured: EXIT 0, ZERO WARNs at the faithful mirror.** Last run: at deposit.

**Closing:** walk 1 dry — instruction 0 / record 0; closed on the dry branch after 1 walk (a single-step read-only corrective of an already-twice-verified state); residue: none.

---

## STEP 1 — QA (the only step)

> **FIRST — visible chat message; do NOT rename this plan file.**
> **A0 (narrowly keyed — first match wins):** (1) the six rows read EXACTLY: 327/328/329/330/332 `accepted|codify|ceo|2026-08-12T17:12:07Z` and 331 `reference|backlog|ceo|2026-08-12T17:12:07Z` → proceed. (2) ANY other per-id state → **HALT with the read-back — this plan repairs nothing.**
> **⚠️ ORDER IS LOAD-BEARING (the machinery plan 360's QA skipped, spelled):** (i) run all row checks and write ALL FOUR evidence files; (ii) write the QA REPORT with its complete `## Verification Table`; (iii) THEN run the Rule 20 canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path) — it `sys.exit(1)`s if the report or any evidence file is missing, which is WHY the order matters; (iv) APPEND the block's stdout to the report; (v) self-grep the banner into evidence. Placeholders: `plan_slug`: `gate1-write-327-332-2026-08-12-qa-corrective`; `qa_report_path`: `<tree-abs>/knowledge/qa/gate1-write-qa-2026-08-12.md`; `evidence_dir`: `<tree-abs>/knowledge/qa/evidence/gate1-write-327-332-2026-08-12/`; `required_evidence_files`: `["db-invariants.txt", "outside-range-ids.txt", "routing-readback.txt", "pytest_targeted.txt"]`. The banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line must appear byte-exact in the deposited report. Rule 19 verbatim: an incompletable check is `❌` with a reason, never a hedged `✅`. One glyph per status cell; no `|` in cells; `## Evidence and Narrative` directly after the table.
> **The five rows (table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |`; ONE read-only DB form; RAW evidence):**
> **1. THE ROUTES LANDED** — per id, fresh: 327/328/329/330/332 `accepted|codify|ceo` Z-stamped; 331 `reference|backlog|ceo` Z-stamped. → `routing-readback.txt` (fresh run; diff vs the step-1 deposited copy, identical expected)
> **2. BLAST RADIUS** — re-run the EXACT capture SELECT (COPY from 360's G2 block in `knowledge/development/g1cp-flip.sql` on main, never re-type), diff vs the deposited 326-line file; partition (impossible-id → HALT; deleted-row → HALT; else concurrent, named, no halt). → `db-invariants.txt`
> **3. CORPUS SHAPE** — `accepted|codify` = **5**; `proposed` = **0**; `reference` STATUS = **16** with route split **9 `reference` + 7 `backlog`**; `stale` = 3 (98/121/130); total = 332. Zero-emitting forms; printed counts are the assertions. → `db-invariants.txt`
> **4. TESTS** — single-module premise re-derived (`find <tree-abs>/src -name 'test_*.py'` → exactly one; a second = report + run whole `src/`, never HALT); `python3 -m pytest src/ -v` FOREGROUND (no Monitor, no backgrounding), raw tail; vs 55/0, delta reported never asserted. → `pytest_targeted.txt`
> **5. CONSUMER SEMANTICS** — `get_unclassified_entries` still `[]`; entries 324/324; sentinel entry-318 hash `260857bbc71e818b74f503f2984f2b6e5c2854e84e97e4522f9e74b2ccdd0cb8` intact. → `db-invariants.txt`
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION — commit-evidence-first:** commit ALL deposits (report + four evidence files) by explicit pathspec BEFORE the receipt's closing statement; cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Scope:**
> - `knowledge/qa/gate1-write-qa-2026-08-12.md`
> - `knowledge/qa/evidence/gate1-write-327-332-2026-08-12/db-invariants.txt`
> - `knowledge/qa/evidence/gate1-write-327-332-2026-08-12/routing-readback.txt`
> - `knowledge/qa/evidence/gate1-write-327-332-2026-08-12/outside-range-ids.txt`
> - `knowledge/qa/evidence/gate1-write-327-332-2026-08-12/pytest_targeted.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate1-write-qa-2026-08-12.md`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-327-332-2026-08-12/db-invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-327-332-2026-08-12/routing-readback.txt`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-327-332-2026-08-12/outside-range-ids.txt`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-327-332-2026-08-12/pytest_targeted.txt`
