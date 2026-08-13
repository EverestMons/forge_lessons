# Lessons Forge — Cycle Run 2026-08-13, PLAN B: classify the 4 session-40 sweep entries, deposit the report

**Date:** 2026-08-13 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (classify all 4) → Step 2 (DEV — report) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-classify-s40sweep-2026-08-13`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Classification and report only.** Plan A (id 381, `cycle-ingest-s40sweep-2026-08-13`) ingested the 4 session-40 sweep entries; this plan turns them into proposals 333–336 (predicted; the DB assigns) and deposits the report. Gate 1 (route disposition) and Gate 2 (codification) remain separate plans with CEO decisions between. Clone origin: **359** (the newest same-class Plan B; its single-tranche shape carries directly at 4-entry scale).

**This plan contains NO destructive write** (359's own property, re-verified): `insert_proposal` only adds rows; no ingest, no UPDATE, no delete. Risk profile: false halts costing dispatches, not damage.

**Tier: T1** — same computation as 359: parent cycle closed dry (Plan A's walks closed dry at walk 3, both gates first-run clean), additive-only production-data writes (T-2) compute T1; structure-for-structure clone of shipped 359 keeps T-8 silent.

### What Plan A established — each item RE-MEASURED at authoring 2026-08-13, read-only

| fact | measured now |
|---|---|
| the 4 entries exist | ids **325–328**, `MAX(lesson_entries.id)` 328, COUNT 328, `sqlite_sequence` agrees |
| no proposals exist for them | `entry_id > 324` → **0 rows** |
| `P0` = **332** and did NOT move | `MAX(lesson_proposals.id)` 332, `sqlite_sequence` 332 — the split's invariant, re-measured not inherited |
| the work list | `get_unclassified_entries()` = **exactly [325, 326, 327, 328]**, ascending (ORDER BY in the SQL, source-verified) |
| the Gate-2 queue | `accepted` = **0** (nothing to protect; G-queue machinery has no object, verified subtraction carried from 357/359) |
| `STALE_COUNT` | **3** (proposals 98/121/130, settled) |
| `SURFACEABLE_BASE` | **0** (no `proposed`/`ambiguous` row exists) |
| batch `raw_content` range | **1216–1534** chars |
| ⚠️ DB `tags` column | **NULL for all four** — the tag lives in the heading text (2× `[tag: drafting-cycle]`, 1× `[tag: operational-recovery]`, 1× `[tag: verification]`); report the heading-embedded tag, never assert the column |
| report predicate | `WHERE p.status IN ('proposed','ambiguous')` — source-verified `src/lessons_forge.py:541`; **surfaced expectation = SURFACEABLE_BASE + 4 = 4** |
| `insert_proposal` | `src/lessons_forge.py:202` — five required positionals BY NAME in order (`conn, entry_id, category, suggested_action, reasoning, confidence`); a sixth positional binds to CHECK-constrained `status` and fails; `status`/`target_layer`/`target_artifact`/`route`/`subcategory` are keywords (signature re-verified live, `subcategory` present) |
| no 2026-08-13 report exists | `reports/` newest is `lessons-report-2026-08-12.md` |
| sentinel | entry 324 content-hash `04d2bff7a7bfd9552ef5aab0fd099d81214ed97b8fa1a9ee8082e9c218c88c4a` (Plan A's sentinel, carried) |
| FORWARD.md baseline | **18** pipe-lines by `grep -c "^| "` — same probe form at every gate |

### ⚠️ NUMBERING
- **`lesson_entries.id` 325–328** — created by Plan A; this plan never writes entries.
- **`lesson_proposals.id` 333–336** — the 4 proposals this plan creates (predicted; the DB assigns).
- Pairing `entry 325+k → proposal 333+k` (offset **+8**) is a DERIVATION, never an operand. **Never write a bare numeral in 325–336 without its namespace.**
- **`lesson_proposals.id` ≤ 332** — PRE-EXISTING. Touch none of them.

### Flag (G) — mechanism-versus-discipline, the batch's live instrument (producer: Step 1's disposition lines)
**The four are NOT one cluster** (the delta from 359's single-cluster batch): two `drafting-cycle` siblings plus two singletons, three clusters total. The Planner's authoring-time read, handed as EXPECTATION not gate — the classifier applies the test to each entry's own `How to apply:` and may disagree (licence stated):
- **entry 325 reads MECHANISM-shaped, owner named:** a §2.6 capstone-seat/fold-set-reader clause (owner: `DRAFTING_CYCLE.md` §2.6 + the `PANEL_SEAT_TEMPLATE.md` new-surface handoff slot).
- **entry 326 reads MECHANISM-shaped, owner named:** the per-walk-commit record clock, the strike form, and a mechanized record-coherence check in the walk-0 battery (owner: `DRAFTING_CYCLE.md` §2.0/§3 + the walk-register schema). **325 and 326 are the pair-cluster** — both extend the same doctrine surfaces; name the pairing in both disposition lines so Gate 1 routes them together.
- **entry 327 reads DISCIPLINE-shaped with a mechanism candidate:** the ops-compound open/close contract (cd-absolute + location assert; post-condition verify) is operator practice today; if routed mechanism, the owner is `PLANNER_TEMPLATE.md` (an ops-compound clause beside the commit-compound rule). Singleton.
- **entry 328 reads DISCIPLINE-shaped with a mechanism candidate:** the paired-value source spot-check could become a standing QA-row convention (owner if mechanism: the QA row conventions / RULE_20 block's orbit). Singleton.
**Cluster synthesis for Gate 1** (Step 1 deposits it; no other step owns it): *"4 entries, three clusters: the drafting-cycle pair (entries 325/326 — §2.6 capstone + §2.0/§3 record discipline, one doctrine-fold candidate together), the ops-compound singleton (entry 327, discipline with a PLANNER_TEMPLATE clause candidate), the transcription-verification singleton (entry 328, discipline with a QA-row candidate). Tags heading-embedded, DB column NULL."*
**Do NOT dedup against doctrine during classification** — Gate 1 dedups against live `DRAFTING_CYCLE.md` v2.7 (which already carries the scout seat and panel machinery these entries EXTEND; the classifier's job is the proposal, the boundary is Gate 1's).

**Scope discipline:** classification + report only. Routes stay NULL at insert (Gate 1 assigns). Do NOT edit doctrine files, `plan_lint.py`, `gates.py`, or `LESSONS.md`. Do NOT touch proposals with id ≤ 332. Do NOT touch entries (no ingest — Plan A's mutation is done). **⚠️ The LESSONS.md freeze lifted when 381 reached Done; it re-engages while THIS plan sits deposited-but-un-run** (v4.87's rule; the daemon's same-second claim makes the window seconds wide).

**Concurrency:** deposit ONLY after plan 381 reaches Done (single lessons-forge cycle in flight; the Planner holds this file at the scratchpad until then). **⚠️ THE NONE-ROW DAEMON ARTIFACT IS FIXED — the expectation FLIPS from 359:** plan 376 shipped the Forward-Register NONE/empty-guard and the daemon restarted onto it (live at pid 3969's lineage). 359 pre-adjudicated one junk row per step; THIS plan expects **ZERO new FORWARD.md rows at every gate** (baseline 18 pipe-lines, same probe form). **A `NONE.`-item row appearing is a REGRESSION of 376's fix — record it, name it as the finding, and surface it at the verdict; do not adjudicate it as the known artifact. Any row with real item text remains a foreign-writer finding.**

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict.
- At every gate: `accepted` count still 0 (or in-window Gate-1 dispositions of THIS batch's proposals — `ceo` actor, in-window stamp — recorded and carried, per Step 2's carve-out).
- FORWARD.md delta per the flipped rule above (expected ZERO; any delta is a finding).
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle

**Tier:** T1 — see the computation above. Clone of 359 (newest same-class Plan B) at 4-entry scale, single tranche carried; every inherited fact re-measured (the table above); Plan A (381)'s cycle record is the adjacent parent.

**Walk 0 (context pin):** the re-measured table IS the pin — worklist [325–328], P0 332, predicate `:541`, `insert_proposal` `:202` signature re-verified (incl. `subcategory` keyword), no 2026-08-13 report, sentinel entry-324 `04d2bff7…`, STALE 3, SURFACEABLE 0, FORWARD 18 pipe-lines, tags NULL 4/4, hostile headings 2 (entries 325/326), tests 55 collected. Clone-diff vs 359: flag (G) rebuilt for this batch (three clusters vs 359's one — the pair + two singletons; expectations re-derived from each entry's own `How to apply:`); the NONE-row pre-adjudication INVERTED with its premise measured changed (376's guard shipped and live — a junk row is now a regression finding, not a known artifact); the report step's derived expectations re-derived (surfaced = 0+4 = 4; zero route lines); numbering bands re-tokened (333–336, wall ≤ 332); QA register-posture row rewritten for clean `decisions/` (334 archived by 374/375, premise measured). **Scout seat: DECLINED — T1, small surface, proven-clone shape, per the 376/377/379 precedent.**

**Walk 1** (whole artifact, five lenses, sequential):
- Weak spots:          w1 1 folded — instruction, clone-adaptation (Step 2's below-expectation arm (i) carried 359's "naming Plan A's pristine backup" with 359's backup token; re-pointed to THIS lineage's backup `lessons-forge-pre-cycle-381-…Z.db` as recorded in 381's receipt, path re-verified on disk at authoring).
- Destruction:         w1 dry (no destructive write exists; the ≤ 332 wall, the freeze note, and the doctrine-edit prohibitions all carried; the NONE-row inversion ADDS a reporting duty, relaxes nothing).
- Vulnerabilities:     w1 executed — worklist/P0/predicate/signature all re-verified live this session (the table); the route-grep form carries `-F` + `--` + exit-code semantics verbatim from 359; two shell-hostile headings (entries 325/326 — apostrophes) bound as parameters at every site; report `output_dir` cwd trap carried; `subcategory` keyword confirmed in the live signature.
- Integration-record:  w1 dry (v4.87 freeze cross-reference verified live — PT sha unchanged second cycle; the 376-fix flip verified against the shipped plan and the live daemon lineage; numbering bands consistent with the DB reads; deposits blocks name every expected file inline).
- ACID:                w1 dry (three steps, two gate windows, additive-only shared-store writes; per-insert commits make a mid-list death cost the remainder only; every step carries dispatch-state determination + idempotent re-dispatch + deposit-completion resume, carried verbatim from 359 with re-tokened operands).

**Walk-1 split: instruction 1 / record 0.** Direction verdict: **PROCEED**. Re-opens; walk 2 owed.

**Walk 2** (whole artifact; new surface = the walk-1 fold):
- All five lenses:     w2 dry — the backup re-point verified against 381's committed receipt text and the on-disk file; no other 359-token survives (mechanical sweep: no `319`, `327+`-as-entry, `326`-as-P0, `2026-08-12`-dated deposit names, `1e3eb3de`, `cold-panel` slug tokens); ACID schedule untouched.

**Walk-2 split: instruction 0 / record 0 — DRY. The walk phase meets the §2 bar on the dry branch; T1, no panel owed.**

**Conformance (§5):** run post-walk-2 at the faithful scratchpad mirror (four real files copied in: `src/test_lessons_forge.py`, `src/db.py`, `agents/FORGE_LESSONS_AGENT.md`, `knowledge/FORWARD.md`; for (q) the mirror is faithful BY CONSTRUCTION — the resolver reads the `Project:` header). **Measured: EXIT 0, ZERO WARNs, 10 PASS; (q) telemetry: the two sentinel tokens `ambiguous` (correct — DB content-hash values, no file to verify).** Last run: at deposit.

**Closing:** walk 2 dry — instruction 0 / record 0; closed on the dry branch after 2 walks; clone-diff at walk 0 per §2.0; scout declined with reasoning at walk 0; residue: none.

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```

---

## STEP 1 — Classify all 4 (the whole work list; ONE tranche)

> **FIRST — post a short visible chat message (1-2 sentences).** Do NOT rename the plan file. You are the Forge Lessons Agent (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB by ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (`forge/forge.db` is a different database — never open it).
>
> **Step 0 — dispatch state** (three-place probe on this step's dev log `knowledge/development/dev-log-classify-step-1-2026-08-13.md`; probe-3 positive control against `knowledge/FORWARD.md`; state the determination first). **Single-writer check:** work list stable across two reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — this plan's own file is the normal state, zero matches = broken probe, **any OTHER match of any kind → HALT** (`decisions/` measured clean of parked files at authoring; no carve-out exists).
>
> **Pre-flight (read-only):** `get_unclassified_entries()` == `[325, 326, 327, 328]` exactly. Fewer with proposals already present for the missing ids → deposit-completion resume (below). More, or different ids → HALT. `MAX(lesson_proposals.id)` == 332 on FRESH (greater → foreign in-window insert → reconcile: if the extra rows have `entry_id ≤ 324` and a non-this-plan provenance, record + HALT for CEO; this plan's own ids on a resume → resume arms).
>
> **Manifest FIRST:** write + commit the 4-id manifest (the work-list read verbatim) into the dev log stub BEFORE the first insert (`Status: Partial — in flight`).
>
> **Per entry, ids ascending:** read `id, source_heading, raw_content, entry_date` FROM THE DB ROW (⚠️ `tags` is NULL for all four — the tag is heading-embedded: 2× `[tag: drafting-cycle]`, 1× `[tag: operational-recovery]`, 1× `[tag: verification]`); apply ADR-002 on a BODY read; call `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, ...)` — **five required positionals BY NAME in that order; a sixth positional binds to CHECK-constrained `status` and fails**; `status`/`target_layer`/`target_artifact`/`route`/`subcategory` as keywords; **route stays NULL**; **`conn.commit()` after EACH insert** (a mid-list death costs the remainder, not the batch). Shell-hostile headings (entries 325/326 — apostrophes): bind as parameters, never interpolate.
>
> **Flag (G)'s PRODUCER — every disposition line:** `| remedy: mechanism | owner: <named or "unnamed">` or `| remedy: discipline`, from the entry's own `How to apply:` (observed by Step 3 row 3). Where mechanism: `suggested_action` states the mechanism AND owner in its own words (Gate 1 routes from `suggested_action`). **Entries 325 and 326's lines each name the pair-cluster** (both extend §2.6/§2.0-§3 doctrine surfaces — Gate 1 routes them together). **Entries 327 and 328 are singletons with mechanism candidates** (PLANNER_TEMPLATE ops-compound clause; QA-row convention) — if classified discipline, state the candidate in the disposition line anyway. The Planner's expectations are in CEO Context; **licence to disagree is granted — a disagreement is a finding, not an error.**
>
> **Deposit** the dev log: the manifest; per-proposal disposition lines (`- proposal=<id> entry=<id> category=<…> confidence=<…> | remedy: … | …`); the cluster synthesis (verbatim from CEO Context, corrected by anything classification surfaced); the created-proposal id list; `MAX(lesson_proposals.id)` after (expect 336). **Deposit-completion resume:** manifest present + all 4 proposals in DB + dev log incomplete → regenerate disposition lines from DB rows (`reason: not recorded (regenerated)`), **flag-(G) fields re-derived from the entries' own `How to apply:` and marked `remedy: re-derived on resume`** (they live in no DB column), re-deposit, stop. Canonical Python file-write; explicit-pathspec commit; name-only + toplevel asserts. `#### Prompt Feedback` · `#### Forward Register`: `NONE`.
>
> **Scope:**
> - `knowledge/development/dev-log-classify-step-1-2026-08-13.md`
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-classify-step-1-2026-08-13.md`
>
> **STOP. Wait for verdict.**

## STEP 2 — DEV (generate the report)

> **Before starting: Step 1's Receipt carries a PROCEED-value** (allowlist: Complete / Complete-idempotent). Post a visible message. Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — skip with a note if absent). Own tree; canonical DB **read-only** (`?mode=ro`).
>
> **Pre-check — branch, never an unconditional HALT** (340's brick-the-run lesson carried): report exists AND this step's dev log committed AND that log opens with a PROCEED-value → idempotent re-dispatch (append a `### Re-dispatch note`, stop). Report exists, deposit absent → **copy the report aside FIRST** to `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-report-pre-regen-<id>-<UTC-stamp>.md` (`<id>` = ACTUAL plan id; main tree, outside Scope; record as `copy-aside (pre-regen): <abs path>` — Step 3 row 0 cross-checks the token), then deposit-completion. Verified at authoring: no 2026-08-13 report exists.
>
> Run `generate_lessons_report(conn, "2026-08-13")` — whole-corpus; the date is filename/title only. **`output_dir` defaults to `"reports"` RELATIVE TO CWD** — `pwd` first; state the returned absolute path; filename matches Scope.
>
> **Two derived expectations** (operands: Step 1's recorded 4-proposal list; missing/unparseable → STOP, no literal fallback):
> 1. **Surfaced proposals = 4** — derivation `SURFACEABLE_BASE (0, re-measured at authoring) + 4 classified` against the report predicate `status IN ('proposed','ambiguous')` (source-verified `src/lessons_forge.py:541`). Outside-the-4 surfaced row → reconcile-note + CONTINUE if attributable; unattributable → HALT. **Below 4 → check IN ORDER:** (i) any of the recorded 4 `status='stale'` (printed count token) → the staling signature → HALT naming Plan A's pristine backup (`data/backups/lessons-forge-pre-cycle-381-20260813T163031Z.db`, from 381's receipt); (ii) any of the recorded 4 `accepted|codify` with `ceo` actor + in-window stamp → a legitimate in-window Gate-1 → record + CONTINUE with the adjusted expectation. Neither explaining it → HALT.
> 2. **Zero `- **Route:**` lines** — count with `grep -Fc -- '- **Route:**' <report>; echo "ROUTE-GREP-EXIT=$?"` (**both `-F` and `--`; never pipe to `head`**): exit 1 = the expected zero; exit 0 = matches (attribute by `source_heading` via the DB join with BOUND parameters — two headings are shell-hostile; a route on one of OUR 4 with status still `proposed` → in-window Gate 1 → record + CONTINUE; any other → HALT); exit ≥2 = the check did not run → HALT, never record zero.
> - Any `Recently-implemented overlap:` line (same grep form + exit codes) → HALT (plan-207 regression detector).
>
> **Deposit:** report + dev log (`Status:` line first — Step 3 reads it; files-modified; report length; surfaced count; route-line count + exit codes; overlap count + exit code). Canonical Python write; explicit-pathspec commit; name-only + toplevel. `#### Forward Register`: `NONE`.
>
> **Scope:**
> - `reports/lessons-report-2026-08-13.md`
> - `knowledge/development/dev-log-classify-step-2-2026-08-13.md`
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-08-13.md`
> - `lessons-forge/knowledge/development/dev-log-classify-step-2-2026-08-13.md`
>
> **STOP. Wait for verdict.**

## STEP 3 — QA

> **⚠️ STEP 0 — DISPATCH-STATE DETERMINATION FIRST** (the step class that historically lacked it): three-place probe on `knowledge/qa/cycle-classify-qa-2026-08-13.md` with the positive control; a hit on ANY → idempotent re-dispatch (append `### Re-dispatch note`, leave the committed report untouched, STOP — a bare daemon retry re-emitting the register block is the dup-append defect). FRESH → state it first.
>
> **Before starting: Steps 1–2 Receipts BOTH PROCEED-values** (allowlist, named). Post a visible message. Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`); own tree; DB read-only; **verification + reporting only; no Monitor; no fixes.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-classify-s40sweep-2026-08-13`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-classify-qa-2026-08-13.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-classify-s40sweep-2026-08-13/`; `required_evidence_files` `["pytest_targeted.txt", "proposals.txt", "report.txt", "schema.txt"]`. All four files AND the report with its table BEFORE the block; append stdout; the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line byte-exact in the deposited report; self-grep. Rule 19 verbatim; one glyph per status cell; no `|` in cells; `## Evidence and Narrative` directly after the table.
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows, then halt if owed:
> 0. **Deliverables (Rule 17)** — Steps 1–2 committed deposits: `git log --oneline -1 -- <path>` (empty = ❌) + porcelain with echoed exit; the copy-aside token cross-check iff Step 2 recorded one.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` only (baseline 55; delta reported never asserted).
> 2. **`get_unclassified_entries(conn)` == `[]`** — the classify-plan inversion of Plan A's row 2: a NON-empty list means classification is incomplete; quote with a count token. Non-empty → ❌ Critical.
> 3. **Four proposals, exactly ours** — `SELECT p.id, p.entry_id, p.category, p.status, p.route, p.confidence FROM lesson_proposals p WHERE p.entry_id > 324 ORDER BY p.id` → 4 rows; entry_ids exactly 325–328; ids match Step 1's recorded list (predicted 333–336; the RECORD is the operand); every `status='proposed'` (or in-window `accepted|codify|ceo` — reconcile per the carve-out, named ids); every `route` NULL (same carve-out); **every disposition line in Step 1's dev log carries the flag-(G) field** (grep the committed dev log; a missing field = ❌ by id); entries 325/326's lines carry the pair-cluster naming. Total `lesson_proposals` == **336** (332 + 4); above → name foreign ids, reconcile. → `proposals.txt`
> 4. **Report integrity** — report exists at the Scope path; surfaced count == the Step-2 recorded expectation (4, or its recorded in-window adjustment); the route-grep + overlap-grep exit codes from Step 2's dev log re-run fresh (same `-F`/`--`/exit-code form); report references the 4 by heading (spot-check 2 with bound-parameter joins — both hostile headings among them). → `report.txt`
> 5. **No schema drift** — PRAGMA + constraints vs `src/db.py`; raw `.schema` → `schema.txt`.
> 6. **Corpus preservation** — entries still 328/328; sentinel entry-324 content-hash `04d2bff7a7bfd9552ef5aab0fd099d81214ed97b8fa1a9ee8082e9c218c88c4a` unchanged; stale still 3 (98/121/130); `accepted` still 0 OR only the row-3 carve-out ids; the 8-status zero-emitting distribution delta is EXACTLY +4 `proposed` (or the carve-out split), every other bucket unchanged. → `proposals.txt`
> 7. **Register posture** — `decisions/` non-Done contents: this plan's own `in-progress-*` file ONLY (any other = in-window deposit, report names); **FORWARD.md delta since authoring baseline (18 pipe-lines by `grep -c "^| "`) is ZERO — the NONE-guard shipped (plan 376); ANY new row is a finding: a `NONE.`-item row = 376-regression (❌ naming it), a real-text row = foreign writer (❌ naming it).** → `report.txt`
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Scope:**
> - `knowledge/qa/cycle-classify-qa-2026-08-13.md`
> - `knowledge/qa/evidence/cycle-classify-s40sweep-2026-08-13/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-classify-s40sweep-2026-08-13/proposals.txt`
> - `knowledge/qa/evidence/cycle-classify-s40sweep-2026-08-13/report.txt`
> - `knowledge/qa/evidence/cycle-classify-s40sweep-2026-08-13/schema.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-classify-qa-2026-08-13.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-s40sweep-2026-08-13/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-s40sweep-2026-08-13/proposals.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-s40sweep-2026-08-13/report.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-s40sweep-2026-08-13/schema.txt`
