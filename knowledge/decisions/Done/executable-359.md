# Lessons Forge — Cycle Run 2026-08-12, PLAN B: classify the 6 cold-panel entries, deposit the report

**Date:** 2026-08-12 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (classify all 6) → Step 2 (DEV — report) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-classify-cold-panel-2026-08-12`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Classification and report only.** Plan A (id 357, Done 2026-08-12, both gates clean) ingested the 6 cold-panel entries; this plan turns them into proposals 327–332 (predicted) and deposits the report. Gate 1 (route disposition) and Gate 2 (codification) remain separate plans with CEO decisions between. Clone origin: **340** (the newest same-class Plan B; its tranche machinery collapses to ONE classify step at 6-entry scale — the tranches existed for 41).

**This plan contains NO destructive write** (340's own property, re-verified): `insert_proposal` only adds rows; no ingest, no UPDATE, no delete. Risk profile: false halts costing dispatches, not damage.

**Tier: T1 — a measured down-tier from 340's T2, with the reason 340 refused it now ABSENT:** 340 stayed T2 because it derived from a cycle that did not converge (ten unfolded walk-8 findings). This plan's parent cycle (357's) closed LITERAL DRY at walk 2 with zero unfolded findings, and T-2 (production-data mutation, additive-only) computes T1. §2.6's no-down-tier clause bars "bounded/proven-clone" framings as licence; a measured absence of the up-tier's cause is not a framing.

### What Plan A established — each item RE-MEASURED at authoring 2026-08-12, read-only

| fact | measured now |
|---|---|
| the 6 entries exist | ids **319–324**, `MAX(lesson_entries.id)` 324, `sqlite_sequence` agrees |
| no proposals exist for them | `entry_id > 318` → **0 rows** |
| `P0` = **326** and did NOT move | `MAX(lesson_proposals.id)` 326, `sqlite_sequence` 326 — the split's invariant, re-measured not inherited |
| the work list | `get_unclassified_entries()` = **exactly [319, 320, 321, 322, 323, 324]**, ascending (ORDER BY in the SQL, source-verified) |
| the Gate-2 queue | `accepted` = **0** (drained by plan 356; nothing to protect — 340's 42-row machinery has no object, verified subtraction) |
| `STALE_COUNT` | **3** (proposals 98/121/130, settled) |
| `SURFACEABLE_BASE` | **0** (no `proposed`/`ambiguous` row exists) |
| batch `raw_content` range | **799–3035** chars |
| ⚠️ DB `tags` column | **NULL for all six** — the tag lives in the heading text (`[tag: drafting-cycle]`, 6 of 6); report the heading-embedded tag, never assert the column |
| report predicate | `WHERE p.status IN ('proposed','ambiguous')` — source-verified `src/lessons_forge.py:541`; **surfaced expectation = SURFACEABLE_BASE + 6 = 6** |
| `insert_proposal` | `src/lessons_forge.py:202` — five required positionals BY NAME in order (`conn, entry_id, category, suggested_action, reasoning, confidence`); a sixth positional binds to CHECK-constrained `status` and fails; `status`/`target_layer`/`target_artifact`/`route` are keywords |
| no 2026-08-12 report exists | `reports/` newest is `lessons-report-2026-08-11.md` |

### ⚠️ NUMBERING
- **`lesson_entries.id` 319–324** — created by Plan A; this plan never writes entries.
- **`lesson_proposals.id` 327–332** — the 6 proposals this plan creates (predicted; the DB assigns).
- Pairing `entry 319+k → proposal 327+k` (offset **+8**) is a DERIVATION, never an operand. **Never write a bare numeral in 319–332 without its namespace.**
- **`lesson_proposals.id` ≤ 326** — PRE-EXISTING. Touch none of them.

### Flag (G) — mechanism-versus-discipline, the batch's live instrument (producer: Step 1's disposition lines)
The six are ONE COHERENT CLUSTER (the cold-panel doctrine-debt batch, authored from the gate2-pt3 panel's measured record). The Planner's authoring-time read, handed as EXPECTATION not gate — the classifier applies the test to each entry's own `How to apply:` and may disagree (licence stated):
- **entries 319/320/321/322/324 read MECHANISM-shaped, owners named:** 319 names `PANEL_SEAT_TEMPLATE.md` + a §2.6 seat-prompt contract clause (owner: governance/DRAFTING_CYCLE + a new root template artifact); 320 a §2.6 meter-at-convene sentence + a template meter slot; 321 an execution brief in the §2.6 registry; 322 register schema 0.2 (owner: the walk-register schema, DRAFTING_CYCLE-adjacent); 324 the four §2.6 structures (panel-0, machine-readable pins + scripted battery, hunk maps, new-surface handoffs) — **and 324 is the stated HOW behind 320/321/322: name the bundle in its disposition line so Gate 1 routes them together.**
- **entry 323 is the batch's routing decision:** its own `How to apply:` says **do NOT fold as a §2.6 bullet — route as a decision packet** to the shape session. A classifier routing it to plain `codify` converts a shape decision into a sentence; its disposition line must carry the packet flag.
**Cluster synthesis for Gate 1** (Step 1 deposits it; no other step owns it): *"6 entries, all `drafting-cycle` (heading-embedded; DB tags NULL), one cluster; five mechanism-shaped with owners named (all §2.6/registry/template surfaces); one explicit shape-packet routing (entry 323); entry 324 the HOW behind 320/321/322 — bundle candidates: one §2.6 codification plan, one new-artifact build (PANEL_SEAT_TEMPLATE), one decision packet."*
**Do NOT dedup against doctrine during classification** — Gate 1 dedups against live `DRAFTING_CYCLE.md` v2.5 (which already carries the meter mandate and seat-brief registry these entries EXTEND; the classifier's job is the proposal, the boundary is Gate 1's).

**Scope discipline:** classification + report only. Routes stay NULL at insert (Gate 1 assigns). Do NOT edit doctrine files, `plan_lint.py`, `gates.py`, or `LESSONS.md`. Do NOT touch proposals with id ≤ 326. Do NOT touch entries (no ingest — Plan A's mutation is done). **⚠️ The LESSONS.md freeze lifted when 357 reached Done; it re-engages while THIS plan sits deposited-but-un-run** (v4.87's rule; the daemon's same-second claim makes the window seconds wide).

**Concurrency:** no other lessons-forge cycle in flight (single-writer probes in every step; plan 358 runs in a parallel session on a DIFFERENT project — expected, not a collision). **Known daemon artifact, expected and pre-adjudicated:** the post-merge Forward-Register parser converts a literal `NONE.` declaration into a junk register row (rows 14–17 of `lessons-forge/knowledge/FORWARD.md`, diagnosed at 357's step-2 verdict). **Each step of this plan will likely append one more junk row via the same defect — the Planner reconciles at each gate: a `NONE.`-item row is the KNOWN artifact (record, continue); any row with real item text is the finding.** The parser fix is queued separately (bellows-owned); this plan must not attempt it.

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict.
- At every gate: `accepted` count still 0 (or in-window Gate-1 dispositions of THIS batch's proposals — `ceo` actor, in-window stamp — recorded and carried, per Step 2's carve-out).
- FORWARD.md delta per the known-artifact rule above.
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle

**Tier:** T1 — down-tier measured (parent converged dry; 340's stated up-tier cause absent; additive-only writes). Clone lineage: 340 (newest same-class) with the tranche machinery collapsed 3→1 and every inherited fact re-measured (the table above); 357's cycle record is the adjacent parent.

**Walk 0 (context pin):** the re-measured table IS the pin. Clone-diff vs 340: tranches 3→1 (batch 41→6, the tranche map's premise); the 42-row Gate-2 protection machinery subtracted with its premise measured false (`accepted` = 0); flag (G) rebuilt for this batch's six (five mechanism + one packet-routing); the three deferred walk-8 findings 340 folded (QA dispatch-state determination, resume-regenerable flag-(G) lines, pre-flight/self-report agreement) CARRIED into Steps 1/3; the report step's two derived expectations re-derived (surfaced = 0+6 = 6; zero route lines); the NONE-row daemon artifact newly pre-adjudicated (it postdates 340).

**Walk 1** (whole artifact, five lenses, sequential):
- Weak spots:          w1 1 folded — instruction, clone-adaptation (the report step's below-expectation arm cited 340's "recorded 41" operand at one site while this plan's anchor is the 6-id list; swept to "the recorded 6" and the Gate-2 id-for-id check REMOVED with its premise stated — there is no queue to check, `accepted` = 0 measured, and the arm now reads: any of OUR 6 proposals `accepted|codify|ceo` in-window = record + CONTINUE with adjusted expectation).
- Destruction:         w1 dry (no destructive write exists; the subtractions carry their measured-false premises inline; nothing relaxed — the freeze note, the ≤ 326 wall, and the doctrine-edit prohibitions all carried).
- Vulnerabilities:     w1 executed — worklist/P0/predicate/signature all re-verified live this session (the table); the route-grep form carries `-F` + `--` + exit-code semantics verbatim from 340; three shell-hostile headings (entries 319/320/324) bound as parameters at every site; report `output_dir` cwd trap carried.
- Integration-record:  w1 dry (v4.87 freeze cross-reference verified live; the NONE-row artifact's pre-adjudication matches the 357 verdict record verbatim; numbering bands consistent with the DB reads).
- ACID:                w1 dry (three steps, two gate windows, additive-only shared-store writes; per-insert commits make a mid-list death cost the remainder only; every step carries dispatch-state determination + idempotent re-dispatch + deposit-completion resume — 340's folded findings carried, including flag-(G) line regeneration marked `re-derived on resume`).

**Walk-1 split: instruction 1 / record 0.** Re-opens; walk 2 owed.

**Walk 2** (whole artifact; new surface = the walk-1 sweep):
- All five lenses:     w2 dry — the "recorded 6" sweep verified at every arm site (grep-enumerated); battery stable; lint at the FAITHFUL four-file mirror **EXIT 0, ZERO WARNs** (measured on the deposit-shaped bytes at the scratchpad mirror — never the real `decisions/`; the daemon claims AND DISPATCHES same-second, proven live at the gate2-pt3 incident); Closing asserts the dry close.

**Walk-2 split: instruction 0 / record 0 — DRY. The walk phase meets the §2 bar on the dry branch; T1, no panel owed.**

**Conformance (§5):** run at shape-stability post-walk-1, re-run post-walk-2 and at deposit, at the faithful scratchpad mirror (four real files copied in: `src/test_lessons_forge.py`, `src/db.py`, `agents/FORGE_LESSONS_AGENT.md`, `knowledge/FORWARD.md`). **Measured: EXIT 0, ZERO WARNs.** Last run: at deposit.

**Closing:** walk 2 dry — instruction 0 / record 0; closed on the dry branch after 2 walks; clone-diff at walk 0 per §2.6; residue: none.

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
> **Step 0 — dispatch state** (three-place probe on this step's dev log `knowledge/development/dev-log-classify-step-1-2026-08-12.md`; probe-3 positive control against `knowledge/FORWARD.md`; state the determination first). **Single-writer check:** work list stable across two reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — this plan's own file is the normal state, zero matches = broken probe, any OTHER lessons/cycle match → HALT.
>
> **Pre-flight (read-only):** `get_unclassified_entries()` == `[319, 320, 321, 322, 323, 324]` exactly. Fewer with proposals already present for the missing ids → deposit-completion resume (below). More, or different ids → HALT. `MAX(lesson_proposals.id)` == 326 on FRESH (greater → foreign in-window insert → reconcile: if the extra rows have `entry_id ≤ 318` and a non-this-plan provenance, record + HALT for CEO; this plan's own ids on a resume → resume arms).
>
> **Manifest FIRST:** write + commit the 6-id manifest (the work-list read verbatim) into the dev log stub BEFORE the first insert (`Status: Partial — in flight`).
>
> **Per entry, ids ascending:** read `id, source_heading, raw_content, entry_date` FROM THE DB ROW (⚠️ `tags` is NULL for all six — the tag is heading-embedded, `[tag: drafting-cycle]`); apply ADR-002 on a BODY read; call `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, ...)` — **five required positionals BY NAME in that order; a sixth positional binds to CHECK-constrained `status` and fails**; `status`/`target_layer`/`target_artifact`/`route` as keywords; **route stays NULL**; **`conn.commit()` after EACH insert** (a mid-list death costs the remainder, not the batch). Shell-hostile headings (319/320/324 — apostrophes): bind as parameters, never interpolate.
>
> **Flag (G)'s PRODUCER — every disposition line:** `| remedy: mechanism | owner: <named or "unnamed">` or `| remedy: discipline`, from the entry's own `How to apply:` (observed by Step 3 row 3). Where mechanism: `suggested_action` states the mechanism AND owner in its own words (Gate 1 routes from `suggested_action`). **Entry 323's line carries the packet flag** — its own text routes it to a decision packet, not a bullet; a plain-codify disposition here must be a deliberate disagreement, stated. **Entry 324's line names the 320/321/322 bundle.** The Planner's expectations are in CEO Context; **licence to disagree is granted — a disagreement is a finding, not an error.**
>
> **Deposit** the dev log: the manifest; per-proposal disposition lines (`- proposal=<id> entry=<id> category=<…> confidence=<…> | remedy: … | …`); the cluster synthesis (verbatim from CEO Context, corrected by anything classification surfaced); the created-proposal id list; `MAX(lesson_proposals.id)` after (expect 332). **Deposit-completion resume:** manifest present + all 6 proposals in DB + dev log incomplete → regenerate disposition lines from DB rows (`reason: not recorded (regenerated)`), **flag-(G) fields re-derived from the entries' own `How to apply:` and marked `remedy: re-derived on resume`** (they live in no DB column), re-deposit, stop. Canonical Python file-write; explicit-pathspec commit; name-only + toplevel asserts. `#### Prompt Feedback` · `#### Forward Register`: `NONE`.
>
> **Scope:**
> - `knowledge/development/dev-log-classify-step-1-2026-08-12.md`
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-classify-step-1-2026-08-12.md`
>
> **STOP. Wait for verdict.**

## STEP 2 — DEV (generate the report)

> **Before starting: Step 1's Receipt carries a PROCEED-value** (allowlist: Complete / Complete-idempotent). Post a visible message. Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — skip with a note if absent). Own tree; canonical DB **read-only** (`?mode=ro`).
>
> **Pre-check — branch, never an unconditional HALT** (340's brick-the-run lesson carried): report exists AND this step's dev log committed AND that log opens with a PROCEED-value → idempotent re-dispatch (append a `### Re-dispatch note`, stop). Report exists, deposit absent → **copy the report aside FIRST** to `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-report-pre-regen-<id>-<UTC-stamp>.md` (`<id>` = ACTUAL plan id; main tree, outside Scope; record as `copy-aside (pre-regen): <abs path>` — Step 3 row 0 cross-checks the token), then deposit-completion. Verified at authoring: no 2026-08-12 report exists.
>
> Run `generate_lessons_report(conn, "2026-08-12")` — whole-corpus; the date is filename/title only. **`output_dir` defaults to `"reports"` RELATIVE TO CWD** — `pwd` first; state the returned absolute path; filename matches Scope.
>
> **Two derived expectations** (operands: Step 1's recorded 6-proposal list; missing/unparseable → STOP, no literal fallback):
> 1. **Surfaced proposals = 6** — derivation `SURFACEABLE_BASE (0, Plan A's stub) + 6 classified` against the report predicate `status IN ('proposed','ambiguous')` (source-verified `src/lessons_forge.py:541`). Outside-the-6 surfaced row → reconcile-note + CONTINUE if attributable; unattributable → HALT. **Below 6 → check IN ORDER:** (i) any of the recorded 6 `status='stale'` (printed count token) → the staling signature → HALT naming Plan A's pristine backup; (ii) any of the recorded 6 `accepted|codify` with `ceo` actor + in-window stamp → a legitimate in-window Gate-1 → record + CONTINUE with the adjusted expectation. Neither explaining it → HALT.
> 2. **Zero `- **Route:**` lines** — count with `grep -Fc -- '- **Route:**' <report>; echo "ROUTE-GREP-EXIT=$?"` (**both `-F` and `--`; never pipe to `head`**): exit 1 = the expected zero; exit 0 = matches (attribute by `source_heading` via the DB join with BOUND parameters — three headings are shell-hostile; a route on one of OUR 6 with status still `proposed` → in-window Gate 1 → record + CONTINUE; any other → HALT); exit ≥2 = the check did not run → HALT, never record zero.
> - Any `Recently-implemented overlap:` line (same grep form + exit codes) → HALT (plan-207 regression detector).
>
> **Deposit:** report + dev log (`Status:` line first — Step 3 reads it; files-modified; report length; surfaced count; route-line count + exit codes; overlap count + exit code). Canonical Python write; explicit-pathspec commit; name-only + toplevel. `#### Forward Register`: `NONE`.
>
> **Scope:**
> - `reports/lessons-report-2026-08-12.md`
> - `knowledge/development/dev-log-classify-step-2-2026-08-12.md`
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-08-12.md`
> - `lessons-forge/knowledge/development/dev-log-classify-step-2-2026-08-12.md`
>
> **STOP. Wait for verdict.**

## STEP 3 — QA

> **⚠️ STEP 0 — DISPATCH-STATE DETERMINATION FIRST** (the step class that historically lacked it): three-place probe on `knowledge/qa/cycle-classify-qa-2026-08-12.md` with the positive control; a hit on ANY → idempotent re-dispatch (append `### Re-dispatch note`, leave the committed report untouched, STOP — a bare daemon retry re-emitting the register block is the dup-append defect). FRESH → state it first.
>
> **Before starting: Steps 1–2 Receipts BOTH PROCEED-values** (allowlist, named). Post a visible message. Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`); own tree; DB read-only; **verification + reporting only; no Monitor; no fixes.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-classify-cold-panel-2026-08-12`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-classify-qa-2026-08-12.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-classify-cold-panel-2026-08-12/`; `required_evidence_files` `["pytest_targeted.txt", "proposals.txt", "report.txt", "schema.txt"]`. All four files AND the report with its table BEFORE the block; append stdout; the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line byte-exact in the deposited report; self-grep. Rule 19 verbatim; one glyph per status cell; no `|` in cells; `## Evidence and Narrative` directly after the table.
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows, then halt if owed:
> 0. **Deliverables (Rule 17)** — Steps 1–2 committed deposits: `git log --oneline -1 -- <path>` (empty = ❌) + porcelain with echoed exit; the copy-aside token cross-check iff Step 2 recorded one.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` only (baseline 55; delta reported never asserted).
> 2. **`get_unclassified_entries(conn)` == `[]`** — the classify-plan inversion of Plan A's row 2: a NON-empty list means classification is incomplete; quote with a count token. Non-empty → ❌ Critical.
> 3. **Six proposals, exactly ours** — `SELECT p.id, p.entry_id, p.category, p.status, p.route, p.confidence FROM lesson_proposals WHERE p.entry_id > 318 ORDER BY p.id` → 6 rows; entry_ids exactly 319–324; ids match Step 1's recorded list (predicted 327–332; the RECORD is the operand); every `status='proposed'` (or in-window `accepted|codify|ceo` — reconcile per the carve-out, named ids); every `route` NULL (same carve-out); **every disposition line in Step 1's dev log carries the flag-(G) field** (grep the committed dev log; a missing field = ❌ by id); entry 323's line carries the packet flag. Total `lesson_proposals` == **332** (326 + 6); above → name foreign ids, reconcile. → `proposals.txt`
> 4. **Report integrity** — report exists at the Scope path; surfaced count == the Step-2 recorded expectation (6, or its recorded in-window adjustment); the route-grep + overlap-grep exit codes from Step 2's dev log re-run fresh (same `-F`/`--`/exit-code form); report references the 6 by heading (spot-check 2 with bound-parameter joins). → `report.txt`
> 5. **No schema drift** — PRAGMA + constraints vs `src/db.py`; raw `.schema` → `schema.txt`.
> 6. **Corpus preservation** — entries still 324/324; sentinel entry-318 hash `260857bbc71e818b74f503f2984f2b6e5c2854e84e97e4522f9e74b2ccdd0cb8` unchanged; stale still 3 (98/121/130); `accepted` still 0 OR only the row-3 carve-out ids; the 8-status zero-emitting distribution delta is EXACTLY +6 `proposed` (or the carve-out split), every other bucket unchanged. → `proposals.txt`
> 7. **Register posture** — `decisions/` non-Done contents: `halted-executable-334.md` + this plan's own `in-progress-*` file only; FORWARD.md delta since Step 1 consists ONLY of `NONE.`-item rows (the known daemon artifact, pre-adjudicated — count them, record, ✅ with note; any row with real item text = ❌ naming it). → `report.txt`
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Scope:**
> - `knowledge/qa/cycle-classify-qa-2026-08-12.md`
> - `knowledge/qa/evidence/cycle-classify-cold-panel-2026-08-12/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-classify-cold-panel-2026-08-12/proposals.txt`
> - `knowledge/qa/evidence/cycle-classify-cold-panel-2026-08-12/report.txt`
> - `knowledge/qa/evidence/cycle-classify-cold-panel-2026-08-12/schema.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-classify-qa-2026-08-12.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-cold-panel-2026-08-12/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-cold-panel-2026-08-12/proposals.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-cold-panel-2026-08-12/report.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-cold-panel-2026-08-12/schema.txt`
