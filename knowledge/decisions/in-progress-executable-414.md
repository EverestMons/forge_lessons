# Lessons Forge — Cycle Run 2026-08-14, PLAN B: classify the 6 fold-damage entries, deposit the report

**Date:** 2026-08-14 | **Tier:** Small | **Dispatch Mode:** bellows | **Execution:** Step 1 (classify all 6) → Step 2 (DEV — report) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-classify-folddamage-2026-08-14`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Classification and report only.** Plan A (id 411, Done) ingested the 6 fold-damage entries as **339–344**; this plan turns them into proposals **347–352** (predicted; the DB assigns) and deposits the report. Gate 1 and Gate 2 remain separate plans with CEO decisions between. Clone origin AND newest same-class: **399** (`cycle-classify-s42sweep`, Done 2026-08-14).

⚠️ **Derived by READING 399 SECTION BY SECTION, not by token-swapping it** — entry **342** of the very batch this plan classifies is the rule that mandates exactly that, and it earned its place at a cost of 17 origin-carried findings. Applying it to the plan that classifies it is deliberate.

**No destructive write.** `insert_proposal` only adds rows; no ingest, no UPDATE, no delete. ⚠️ **And unlike the origin, no file is overwritten either — see FALSE-HERE item 1.**

### What Plan A established — each item RE-MEASURED at authoring 2026-08-14, read-only

| fact | measured now |
|---|---|
| the 6 entries exist | ids **339–344**, `MAX(lesson_entries.id)` 344, COUNT 344 |
| no proposals exist for them | `entry_id > 338` → **0 rows** |
| `P0` = **346** and did NOT move | `MAX(lesson_proposals.id)` 346, `sqlite_sequence` agrees |
| the work list | `get_unclassified_entries()` = **exactly [339, 340, 341, 342, 343, 344]** |
| `STALE_COUNT` | **3** (98/121/130) |
| `SURFACEABLE_BASE` | **0** (no `proposed`/`ambiguous` row) |
| batch `raw_content` range | **991–1705** chars (399's 847–1155 does NOT carry) |
| DB `tags` column | **NULL for all six**; heading-embedded: 3× `drafting-cycle`, 2× `verification`, 1× `operational-recovery` |
| report predicate | `status IN ('proposed','ambiguous')` at `src/lessons_forge.py:541`; **surfaced expectation = 0 + 6 = 6** |
| `insert_proposal` | `:202`, signature re-verified live by `inspect.signature` — five required positionals then keywords |
| sentinel | entry **338** content-hash `359bf0267d500f50e67b4748a974b468620d8eb25c58b1fd4c046d0fabffaf9a` |
| FORWARD.md baseline | **18** pipe-lines by `grep -c "^| "` |

### ⚠️⚠️ INHERITED FACTS FROM 399 THAT ARE FALSE HERE

1. **⚠️ THE REPORT COLLISION IS GONE — the premise INVERTS BACK.** 399's largest item was that a `2026-08-13` report already existed (382's), which promoted the copy-aside from an exception branch to the EXPECTED path. **Measured: `reports/lessons-report-2026-08-14.md` does NOT exist.** This plan generates for **`"2026-08-14"`**, so it CREATES a new file and overwrites nothing. **Carrying 399's copy-aside arm unexamined would send an agent hunting for a file that is not there**; Step 2's pre-check is restored to the origin-of-the-origin form (382's): report absent → generate; report present → copy aside first, then regenerate.
2. **⚠️ `accepted` IS 3, NOT 0.** 399's QA row 6 expected `accepted` still 0 with a carve-out. The Gate-2 queue is legitimately open — **340, 342, 346 stand `accepted|codify`** — and this plan must leave all three untouched. Every check keys on the **id set**, never the count (a count-only check passes a foreign row that displaced one of ours).
3. **ONE hostile heading, not two** — entry **340** (apostrophe). Bind headings as query parameters everywhere.
4. **Numbering re-tokened:** entries 339–344 → proposals 347–352 (offset **+8**, a DERIVATION never an operand); the pre-existing wall is `id ≤ 346`.

### ⚠️ NUMBERING
- **`lesson_entries.id` 339–344** — created by Plan A; this plan never writes entries.
- **`lesson_proposals.id` 347–352** — the 6 this plan creates (predicted; the DB assigns).
- **`lesson_proposals.id` ≤ 346** — PRE-EXISTING. Touch none, and 340/342/346 are the live Gate-2 queue.
- **Never write a bare numeral in 339–352 without its namespace.**

### Flag (G) — mechanism-versus-discipline (producer: Step 1's disposition lines)
**Six entries, FOUR clusters.** Planner's authoring read, handed as EXPECTATION not gate; **licence to disagree is granted — a disagreement is a finding, not an error**:
- **Cluster 1 — the fold-safety pair (entries 339, 340):** the fold has no post-condition; a fold's prose breaks a machine contract. **MECHANISM-shaped, owner named — see Flag (H').** Name the pairing in both lines.
- **Cluster 2 — the record-hygiene pair (entries 341, 343):** narrating a severance re-adds the severed content; a marker-collision fires on first use. DISCIPLINE-shaped; candidate owners are §2.7's retraction/edit-anchor orbit (341) and the walk-register schema's annotation rule (343).
- **Cluster 3 — the clone-derivation singleton (entry 342):** MECHANISM-shaped with a **dedup caveat the classifier must state**: `section-by-section at token level` already counts **1** in live `DRAFTING_CYCLE.md` — but it sits in §2.6's clone-diff BRIEF, binding the cold SEAT. Entry 342's claim is that it binds the **PLANNER's own derivation** at walk 0. That distinction is the whole proposal; state it, and let Gate 1 decide whether it is an extension or a duplicate.
- **Cluster 4 — the date singleton (entry 344):** DISCIPLINE-shaped; candidate owner the PT deposit conventions (the id-at-deposit rule's sibling).

### ⚠️ Flag (H') — THE APPROVED-BUT-UNBUILT SUBSET (new; distinct from 399's flag (H))
399's flag (H) marked entries whose remedies had ALREADY SHIPPED. **Here the state is different and must not be conflated: entries 339 and 340 have a CEO-APPROVED remedy that DOES NOT YET EXIST** — the directive of 2026-08-14 ("proceed as recommended") approved (a) a mechanized `fold_check` diffing the machine-readable state against a pre-fold baseline and (b) ONE §2.7 bullet making the fold the unit carrying the post-condition, and explicitly declined a sixth lens. Measured: `fold_check` counts **0** and `machine-readable state` counts **0** in live `DRAFTING_CYCLE.md` — nothing is built. **The classifier records `| approved-unbuilt: <what the CEO approved>` on those two lines and states the fact in `reasoning`, so Gate 1 routes from the decision record rather than rediscovering it.** This is an input, NOT a verdict — Gate 1 owns the routing, and a plausible outcome is `accepted|codify` for both with the tool riding Gate 2.

**Scope discipline:** classification + report only. Routes stay NULL at insert. Do NOT edit doctrine files, `plan_lint.py`, `gates.py`, or `LESSONS.md`. Do NOT touch proposals ≤ 346 — especially 340/342/346. **⚠️ The `LESSONS.md` freeze re-engages while THIS plan sits deposited-but-un-run.**

**Concurrency:** no other lessons-forge cycle in flight (411 Done). A parallel terminal ships invoice-pulse work in the shared ROOT repo — store-disjoint; the `decisions/` and FORWARD posture rows are the in-window detectors.

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict.
- At every gate the non-terminal set is still exactly **{340, 342, 346}** PLUS this plan's own new `proposed` rows — by id, never by count.
- FORWARD.md delta ZERO against the Step-1 baseline; any row is a finding.
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle

**Tier:** T1 — additive-only production writes (T-2); structure-for-structure clone of shipped 399 keeps T-8 silent; parent cycle (411) closed with both gates first-run clean.

**Walk register:** `governance/knowledge/research/walk-register-cycle-classify-folddamage-2026-08-14.md` (schema 0.3), committed per phase.

**Walk 0 (context pin):** the re-measured tables ARE the pin — worklist [339–344], P0 346, batch proposals 0, accepted 3 = {340,342,346}, stale 3, surfaceable 0, raw_content 991–1705, tags NULL 6/6 with the 3/2/1 mix, predicate `:541` and `insert_proposal` `:202` re-verified live, sentinel entry-338 `359bf026…`, FORWARD 18, **no `2026-08-14` report on disk**, dedup probes (`section-by-section at token level` 1 — in the SEAT brief; `fold_check` 0; `machine-readable state` 0). **Clone-diff vs 399, read section-by-section:** the report-collision premise INVERTED BACK (item 1) with the copy-aside restored to a conditional arm; the `accepted`-is-0 premise inverted (item 2) with every check re-keyed to the id set; flag (G) rebuilt (four clusters vs seven); **flag (H') is NEW and deliberately distinct from 399's (H)** — approved-but-unbuilt is not already-shipped; hostile headings 2→1; bands re-tokened. **Scout: DECLINED** — T1, proven-clone shape, additive-only; the two premise inversions were caught by the section-by-section read at walk 0, which is where a scout's value would have been spent.

**Walks (2 warm):**
- Weak spots:          w1 dry (pre-flight, manifest-first, per-insert commit, the resume arms and every derived number re-read against the measured tables; the 342 dedup caveat is mandated rather than left to discovery); w2 dry.
- Destruction:         w1 dry (no destructive write; the `id <= 346` wall plus the named Gate-2 queue; the report path CREATES rather than overwrites — verified by `ls`); w2 dry.
- Vulnerabilities:     w1 executed at authoring (worklist, P0, signature, predicate, dedup probes, the report-absence check, the `.db`-scoped backup form); w2 dry.
- Integration-record:  w1 dry (Deposits project-prefixed with Scope repo-relative per the lessons-forge convention; bands consistent with the DB reads; stray-origin-token sweep for `s42sweep`/`329`/`336`/`2026-08-13` — zero operative hits); w2 dry.
- ACID:                w1 dry (three steps, two gate windows, additive-only; per-insert commits bound a mid-list death to the remainder).

**Splits: w1 instruction 0 / record 0 — DRY (the five clone-diff findings all landed at walk 0) · w2 dry.**

**Conformance (§5):** faithful-mirror `plan_lint` at the deposit-shaped scratchpad mirror — NEVER the real `decisions/`. The measured set at the close run is what freeze item 3 binds to; the placeholder-lens WARN clears when this Walks block fills.

**Closing:** walk 2 read dry on every lens — **instruction 0 / record 1: this Cycle-Log fill itself, written at close with measured content** (0 of 1 fold-introduced). The section-by-section clone-diff at walk 0 is where the yield landed (5 findings, 2 premise inversions); scout declined with reasoning; fold-and-deposit exactly once.

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```

---

## STEP 1 — Classify all 6 (the whole work list; ONE tranche)

> **FIRST — post a short visible chat message (1-2 sentences).** Do NOT rename the plan file. You are the Forge Lessons Agent (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB by ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (`forge/forge.db` is a different database — never open it).
>
> **Step 0 — dispatch state** (three-place probe on `knowledge/development/dev-log-classify-fd-step-1-2026-08-14.md`; probe-3 positive control against `knowledge/FORWARD.md`; state the determination first). **Single-writer check:** work list stable across two reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — **THIS PROJECT ONLY**; this plan's own file is normal, zero matches = broken probe, any OTHER match → HALT.
>
> **Pre-flight (read-only):** `get_unclassified_entries()` == `[339, 340, 341, 342, 343, 344]` exactly. Fewer with proposals already present for the missing ids → deposit-completion resume. More, or different ids → HALT. `MAX(lesson_proposals.id)` == 346 on FRESH. **AND the non-terminal id set is exactly `{340, 342, 346}`** — an extra id is in-window foreign routing → record + HALT; a missing id means a queue row was consumed → HALT.
>
> **Manifest FIRST:** write + commit the 6-id manifest (the work-list read verbatim) into the dev log stub BEFORE the first insert (`Status: Partial — in flight`).
>
> **Per entry, ids ascending:** read `id, source_heading, raw_content, entry_date` FROM THE DB ROW (⚠️ `tags` is NULL for all six — the tag is heading-embedded); apply ADR-002 on a BODY read; call `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, ...)` — **five required positionals BY NAME in that order; a sixth positional binds to CHECK-constrained `status` and fails**; `status`/`target_layer`/`target_artifact`/`route`/`subcategory` as keywords; **route stays NULL**; **`conn.commit()` after EACH insert.** Entry **340**'s heading carries an apostrophe — bind as a parameter, never interpolate.
>
> **Flag (G)'s PRODUCER — every disposition line:** `| remedy: mechanism | owner: <named or "unnamed">` or `| remedy: discipline`, from the entry's own `How to apply:` (observed by Step 3 row 3). Where mechanism, `suggested_action` states the mechanism AND owner in its own words. **Name the pairing on 339/340 and on 341/343.** ⚠️ **Entry 342's line MUST carry the dedup caveat** — `section-by-section at token level` already exists in §2.6's clone-diff brief binding the cold SEAT; 342's claim is that it binds the PLANNER's own derivation. State the distinction; do not silently treat it as novel OR as a duplicate.
> **Flag (H')'s PRODUCER:** entries **339 and 340** additionally carry `| approved-unbuilt: <the CEO-approved remedy>` and state in `reasoning` that the remedy is approved and not yet built (measured: `fold_check` 0, `machine-readable state` 0 in live DC). **This is NOT a reason to skip or pre-route them — Gate 1 owns the dedup and the routing.**
>
> **Deposit** the dev log: the manifest; per-proposal disposition lines (`- proposal=<id> entry=<id> category=<…> confidence=<…> | remedy: … | …`); the cluster synthesis; the created-proposal id list; `MAX(lesson_proposals.id)` after (expect 352); and the **post-insert non-terminal id set** (expect `{340, 342, 346}` plus the six new `proposed` ids). **Deposit-completion resume:** manifest present + all 6 proposals in DB + dev log incomplete → regenerate disposition lines from DB rows (`reason: not recorded (regenerated)`), flag-(G)/(H') fields re-derived from the entries' own `How to apply:` and marked `re-derived on resume`, re-deposit, stop. Canonical Python file-write; explicit-pathspec commit; name-only + toplevel asserts. `#### Prompt Feedback` · `#### Forward Register`: `NONE`.
>
> **Scope:**
> - `knowledge/development/dev-log-classify-fd-step-1-2026-08-14.md`
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-classify-fd-step-1-2026-08-14.md`
>
> **STOP. Wait for verdict.**

## STEP 2 — DEV (generate the report)

> **Before starting: Step 1's Receipt carries a PROCEED-value** (allowlist: Complete / Complete-idempotent). Post a visible message. Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — skip with a note if absent). Own tree; canonical DB **read-only** (`?mode=ro`).
>
> **Pre-check — branch, never an unconditional HALT:** this step's dev log committed AND opening with a PROCEED-value → idempotent re-dispatch (append a `### Re-dispatch note`, stop). **Otherwise: `ls reports/lessons-report-2026-08-14.md`.** ⚠️ **Measured at authoring: it does NOT exist, so the normal path CREATES it and no copy-aside is owed** (the origin 399 overwrote a same-date report and made the copy-aside its expected path — that premise does not hold here). **If it DOES exist** (a concurrent writer), copy it aside FIRST to `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-report-pre-regen-<id>-<UTC-stamp>.md`, verify with `cmp` + echoed exit, record `copy-aside (pre-regen): <abs path>`, THEN regenerate.
>
> Run `generate_lessons_report(conn, "2026-08-14")` — ⚠️ **the date is `2026-08-14`, NOT the origin's `2026-08-13`**; whole-corpus, the date is filename/title only. **`output_dir` defaults to `"reports"` RELATIVE TO CWD** — `pwd` first; state the returned absolute path; filename matches Scope.
>
> **Two derived expectations** (operands: Step 1's recorded 6-proposal list; missing/unparseable → STOP, no literal fallback):
> 1. **Surfaced proposals = 6** — derivation `SURFACEABLE_BASE (0, re-measured) + 6 classified` against the predicate at `:541`. ⚠️ **The three `accepted` rows (340/342/346) are NOT surfaced — the predicate covers `proposed`/`ambiguous` only.** Outside-the-6 surfaced row → reconcile-note + CONTINUE if attributable; unattributable → HALT. **Below 6 → check IN ORDER:** (i) any of the recorded 6 `status='stale'` → the staling signature → HALT naming Plan A's pristine backup (`data/backups/lessons-forge-pre-cycle-411-*.db`, resolved by `.db`-scoped `find` — ⚠️ a bare prefix matches `-wal`/`-shm` sidecars); (ii) any of the recorded 6 `accepted|codify` with `ceo` actor + in-window stamp → a legitimate in-window Gate-1 → record + CONTINUE with the adjusted expectation. Neither explaining it → HALT.
> 2. **Zero `- **Route:**` lines** — `grep -Fc -- '- **Route:**' <report>; echo "ROUTE-GREP-EXIT=$?"` (**both `-F` and `--`; never pipe to `head`**): exit 1 = the expected zero; exit 0 = matches (attribute by `source_heading` via a BOUND-parameter DB join — entry 340's heading is shell-hostile; a route on one of OUR 6 with status still `proposed` → in-window Gate 1 → record + CONTINUE; any other → HALT); exit ≥2 = the check did not run → HALT, never record zero.
> - Any `Recently-implemented overlap:` line (same grep form + exit codes) → HALT. ⚠️ **Sentinel for a REMOVED feature** — the string does not occur in `src/lessons_forge.py` (measured); zero is the pass and a hit means the feature returned. Do not read the zero as evidence a comparison ran.
>
> **Deposit:** report + dev log (`Status:` line first; files-modified; the copy-aside token only if one was taken; report length; surfaced count; route-line count + exit codes; overlap count + exit code). Canonical Python write; explicit-pathspec commit; name-only + toplevel. `#### Forward Register`: `NONE`.
>
> **Scope:**
> - `reports/lessons-report-2026-08-14.md`
> - `knowledge/development/dev-log-classify-fd-step-2-2026-08-14.md`
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-08-14.md`
> - `lessons-forge/knowledge/development/dev-log-classify-fd-step-2-2026-08-14.md`
>
> **STOP. Wait for verdict.**

## STEP 3 — QA

> **⚠️ STEP 0 — DISPATCH-STATE DETERMINATION FIRST:** three-place probe on `knowledge/qa/cycle-classify-fd-qa-2026-08-14.md` with the positive control; a hit on ANY → idempotent re-dispatch (append `### Re-dispatch note`, leave the committed report untouched, STOP). FRESH → state it first.
>
> **Before starting: Steps 1–2 Receipts BOTH PROCEED-values** (allowlist, named). Post a visible message. Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`); own tree; DB read-only; **verification + reporting only; no Monitor; no fixes.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-classify-folddamage-2026-08-14`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-classify-fd-qa-2026-08-14.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-classify-folddamage-2026-08-14/`; `required_evidence_files` `["pytest_targeted.txt", "proposals.txt", "report.txt", "schema.txt"]`. All four files AND the report with its table BEFORE the block; append stdout; banner `Rule 20 — QA Self-Check Results` and `PASSED — SELF-CHECK PASSED` byte-exact; self-grep. Rule 19 verbatim; one glyph per status cell; no `|` in cells; `## Evidence and Narrative` directly after the table.
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows, then halt if owed:
> 0. **Deliverables (Rule 17)** — Steps 1–2 committed deposits: `git log --oneline -1 -- <path>` (empty = ❌) + porcelain with echoed exit; the copy-aside token cross-check **only if Step 2 recorded one** (measured at authoring: none owed).
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` only (baseline 55 passed; delta reported never asserted).
> 2. **`get_unclassified_entries(conn)` == `[]`** — the classify-plan inversion; a NON-empty list means classification is incomplete; quote with a count token. Non-empty → ❌ Critical.
> 3. **Six proposals, exactly ours** — `SELECT p.id, p.entry_id, p.category, p.status, p.route, p.confidence FROM lesson_proposals p WHERE p.entry_id > 338 ORDER BY p.id` → 6 rows; entry_ids exactly 339–344; ids match Step 1's recorded list (predicted 347–352; the RECORD is the operand); every `status='proposed'` (or in-window `accepted|codify|ceo` — reconcile, named ids); every `route` NULL; **every disposition line in Step 1's dev log carries the flag-(G) field** (grep the committed dev log; a missing field = ❌ by id); **entries 339/340 carry the flag-(H') `approved-unbuilt` note**; **entry 342's line carries the dedup caveat**; the two pairings (339/340, 341/343) named in both of their lines. Total `lesson_proposals` == **352** (346 + 6). → `proposals.txt`
> 4. **Report integrity** — report exists at `reports/lessons-report-2026-08-14.md`; surfaced count == the Step-2 recorded expectation (6, or its recorded in-window adjustment); the route-grep + overlap-grep exit codes re-run fresh (same `-F`/`--`/exit-code form); report references the 6 by heading (spot-check 2 with bound-parameter joins — include entry 340, the hostile one). → `report.txt`
> 5. **No schema drift** — PRAGMA + constraints vs `src/db.py`; raw `.schema` → `schema.txt`.
> 6. **Corpus preservation** — entries still 344/344; sentinel entry-338 content-hash `359bf026…` unchanged; stale still 3 (98/121/130); ⚠️ **the pre-existing `accepted` set is still EXACTLY `{340, 342, 346}` by id** (a count is not the guard — the id set is); the 8-status zero-emitting distribution delta is EXACTLY +6 `proposed`, every other bucket unchanged. → `proposals.txt`
> 7. **Register posture** — lessons-forge `decisions/` non-Done contents: this plan's own `in-progress-*` file ONLY (other repos out of scope); **FORWARD.md delta since the Step-1 baseline (18 pipe-lines by `grep -c "^| "`) is ZERO; ANY new row is a finding** — a `NONE.`-item row = a regression of plan 376's guard, a real-text row = foreign writer. → `report.txt`
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Scope:**
> - `knowledge/qa/cycle-classify-fd-qa-2026-08-14.md`
> - `knowledge/qa/evidence/cycle-classify-folddamage-2026-08-14/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-classify-folddamage-2026-08-14/proposals.txt`
> - `knowledge/qa/evidence/cycle-classify-folddamage-2026-08-14/report.txt`
> - `knowledge/qa/evidence/cycle-classify-folddamage-2026-08-14/schema.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-classify-fd-qa-2026-08-14.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-folddamage-2026-08-14/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-folddamage-2026-08-14/proposals.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-folddamage-2026-08-14/report.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-folddamage-2026-08-14/schema.txt`
