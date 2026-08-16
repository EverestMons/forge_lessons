# Lessons Forge — Cycle Run 2026-08-15, PLAN B: classify the 1 residual-bucket entry, deposit the report

**Date:** 2026-08-15 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — classify) → Step 2 (DEV — report) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-classify-residual-bucket-2026-08-15`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Classification and report only.** Plan A (id **423**, Done 2026-08-15) ingested the residual-bucket entry as **345**; this plan turns it into proposal **353** (predicted; the DB assigns) and deposits the report. **Gate 1 and Gate 2 remain separate plans with CEO decisions between.** Clone origin AND newest same-class: **414** (`cycle-classify-folddamage-2026-08-14`, Done 2026-08-14).

⚠️ **Derived by READING 414 SECTION BY SECTION, not by token-swapping it.** 414's own header records why: the rule mandating that derivation was itself entry 342 of the batch 414 classified, earned at a cost of 17 origin-carried findings.

**No destructive write.** `insert_proposal` only adds rows; no ingest, no UPDATE, no delete. ⚠️ **But see FALSE-HERE item 1 — this plan class CAN destroy a shipped artifact, and the midnight rollover is what arms it.**

### ⚠️⚠️ THE SELF-INTEREST DISCLOSURE — the reason this plan exists at all
Entry 345 is the Planner's own lesson, and its remedy is a `PLANNER_TEMPLATE` change **the Planner authored, evidenced, and benefits from** — the rule decides what lands in the Planner's private memory versus a shared bin. The whole arc took the corpus path *instead of* an available direct doctrine edit **precisely so a non-author routes it at Gate 1.** ⚠️ **The classifier must therefore state, in `reasoning`, that the proposal's author is also the author of its evidence and of the drafted remedy** — Gate 1 routes from that disclosure rather than rediscovering it. **This is an input, NOT a verdict.** A plausible Gate-1 outcome is `rejected` or `reference`, and that outcome would be the mechanism working, not a failure.

### What Plan A established — each item RE-MEASURED at authoring 2026-08-15, read-only

| fact | measured now |
|---|---|
| the entry exists | id **345**, `MAX(lesson_entries.id)` 345, COUNT 345 |
| no proposal exists for it | `entry_id > 344` → **0 rows** |
| `P0` = **352** and did NOT move | `MAX(lesson_proposals.id)` 352, COUNT 352 |
| the work list | `get_unclassified_entries()` = **exactly `[345]`** |
| `STALE_COUNT` | **3** (98/121/130) |
| `SURFACEABLE_BASE` | **0** (no `proposed`/`ambiguous` row) |
| entry `raw_content` | **2388** chars |
| DB `tags` column | **NULL**; heading-embedded: **`governance-design`** |
| report predicate | `status IN ('proposed','ambiguous')` at `src/lessons_forge.py:541` (docstring `:519`); **surfaced expectation = 0 + 1 = 1** |
| `insert_proposal` | `:202`, signature re-verified live by `inspect.signature` — **six** required positionals (`conn, entry_id, category, suggested_action, reasoning, confidence`) *(scout S1-20: the draft said five and listed six)* then keywords |
| sentinel | entry **344**, content-hash `e7b607bde3cdaf801fe266d06137b549bab7786accb99356e4eda315351e723d` |
| FORWARD.md baseline | **18** pipe-lines by `grep -c "^| "` |
| backup glob population | **15** (`.db`-scoped). ⚠️ Consumer named *(scout S1-19: the draft carried this pin with no arm reading it)*: Plan A's restore point is `data/backups/lessons-forge-pre-cycle-423-20260815T143540Z.db`. **This plan writes no backup** — it makes no destructive DB write — so a 16th file appearing under this glob during the run means a foreign writer → report it. |
| `decisions/` non-Done | **0** |

### ⚠️⚠️ INHERITED FACTS FROM 414 THAT ARE FALSE HERE

1. **⚠️⚠️ THE DATE ROLLED OVER, AND THAT ARMS A DESTRUCTIVE OVERWRITE.** The session crossed midnight: Plan A closed `2026-08-15T10:41`, and this plan is authored **2026-08-15**. **`reports/lessons-report-2026-08-14.md` EXISTS — it is 414's shipped report, 7256 bytes.** `reports/lessons-report-2026-08-15.md` does NOT exist. **An agent that inherits this lineage's `2026-08-14` date — from the clone parent, from a filename, or from a stale slug — REGENERATES OVER 414'S SHIPPED REPORT.** Step 2 therefore generates for **`"2026-08-15"`** explicitly, and the date is passed as an operand, never defaulted. ⚠️ **The lesson that names this exact failure is entry 344, the sentinel of the cycle that produced entry 345** — applying it to its own successor is deliberate, not decorative. Report absent → generate; report present → copy aside FIRST, then regenerate.
2. **⚠️ `accepted` IS 5, NOT 3.** 414 measured the Gate-2 queue as `{340, 342, 346}`; plan 416 added **350** and **352** the same day. The queue is **`{340, 342, 346, 350, 352}`** and this plan must leave all five untouched. Every check keys on the **id set**, never the count — a count-only check passes a foreign row that displaced one of ours, and this lineage has now watched that count move twice.
3. **THE BATCH IS 1, AND THERE IS ONE CLUSTER, NOT FOUR.** 414's Flag (G) partitioned six entries into four clusters. Here there is a single entry, so the cluster apparatus collapses — see Flag (G) below, which is correspondingly one paragraph and not a taxonomy.
4. **`raw_content` is 2388 chars — OUTSIDE 414's measured 991–1705 band** (and far outside 399's 847–1155). A per-entry length expectation carried from either parent would mis-fire.
5. **THE HOSTILE CHARACTER IS A DOUBLE QUOTE, not an apostrophe.** The heading contains `"everything else"`. ⚠️ In the `sqlite3` CLI `"` is **identifier quoting**, so an interpolated heading can silently resolve as a column name rather than erroring. Bind headings as query parameters everywhere; never interpolate this heading into a `sqlite3` CLI invocation.
6. **THE TAG IS `governance-design`** — not in 414's measured set (`drafting-cycle` ×3, `verification` ×2, `operational-recovery` ×1). The DB `tags` column is NULL, as it was there.
7. **FLAG (H') DOES NOT CARRY — its condition inverted.** 414's approved-but-unbuilt subset marked entries whose CEO-approved remedy did not yet exist; `fold_check` has since shipped. **Here the state is different again and must not be conflated with either prior form — see Flag (H'') below.**
8. **Numbering re-tokened:** entry 345 → proposal 353 (offset **+8**, a DERIVATION never an operand — the same offset 414 carried, which is coincidence and not a rule); the pre-existing wall is `id ≤ 352`.

### ⚠️ NUMBERING
- **`lesson_entries.id` 345** — created by Plan A (423); this plan never writes entries.
- **`lesson_proposals.id` 353** — the ONE this plan creates (predicted; the DB assigns).
- **`lesson_proposals.id` ≤ 352** — PRE-EXISTING. Touch none, and **340/342/346/350/352** are the live Gate-2 queue.
- **Never write a bare numeral in 345–353 without its namespace.**

### Flag (G) — the single cluster (producer: Step 1's disposition line)
**One entry, one proposal.** Planner's authoring read, handed as EXPECTATION not gate; **licence to disagree is granted — a disagreement is a finding, not an error.** Entry 345 says a residual "everything else" bucket silently absorbs the class that deserved its own bin, evidenced by wrap step 7's two-door routing sending project-domain knowledge to the Planner's memory by elimination. **GOVERNANCE-RULE-shaped**, candidate owner `PLANNER_TEMPLATE.md` Session Wrap step 7. ⚠️ **Dedup caveat the classifier must state:** the wrap step already names two destinations, so this is an EXTENSION of an existing rule rather than a new one — say so, and let Gate 1 decide whether that makes it `codify`, `reference` (the rule exists, the bin does not), or `rejected`.

### ⚠️ Flag (H'') — THE REMEDY IS DRAFTED, GATED, AND AUTHORED BY THE PROPOSER
Distinct from 414's (H') and from 399's (H). **The remedy for entry 345 is not unbuilt and not shipped — it is DRAFTED and deliberately BLOCKED on this plan's own downstream Gate-1 routing:** an executable taking `PLANNER_TEMPLATE` 4.88 → 4.89 (three logical edits — step 7 gains a third destination; Source B gains a standing read; version + History), whose builder is committed and whose own text states it does not dispatch until a proposal derived from this entry is routed `accepted|codify`, with the proposal and entry ids as required builder arguments. **The classifier writes the disposition line into its dev log in EXACTLY this form, one line, byte-exact prefix:**
`DISPOSITION | entry=345 | proposal=<id> | remedy: drafted-and-gated (PT 4.88->4.89) | markers: [DEDUP] [REMEDY-GATED] [AUTHOR-CONFLICT]`
and states in `reasoning` that the mechanism cannot run ahead of the routing. ⚠️ **QA row 8 reads that line** — *(scout S1-8: the draft named a disposition-line producer with no format and no reader, so nothing would have checked it existed)*. ⚠️ **This is an input, NOT a verdict** — Gate 1 owns the routing, and the disclosure above means a non-`codify` outcome is a legitimate result the arc must absorb, not an obstacle to route around.

**Scope discipline:** classification + report only. Routes stay NULL at insert. Do NOT edit doctrine files, `plan_lint.py`, `gates.py`, or `LESSONS.md`. Do NOT touch proposals ≤ 352 — especially 340/342/346/350/352. **⚠️ The `LESSONS.md` freeze re-engages while THIS plan sits deposited-but-un-run.**

**Concurrency:** no other lessons-forge cycle in flight (423 Done). A parallel terminal ships invoice-pulse work in the shared ROOT repo — store-disjoint; the `decisions/` and FORWARD posture rows are the in-window detectors. ⚠️ **Re-measured 2026-08-15:** ids **422** (invoice-pulse diagnostic, closed), **423** (this arc's Plan A, closed) and **424** (invoice-pulse dispute-outcome sizing probe, **IN PROGRESS at authoring**) are consumed; `id_sequence` reads **425**. **This plan's id is therefore a prediction that will move again** — re-read `id_sequence` at deposit and re-token every filename id site. *(scout S1-14: the draft cited 422 as the latest and pointed at "the id prediction below", which did not exist.)*

### ⚠️ Freeze checklist (run immediately before deposit) *(scout S1-13: absent from this whole lineage — 397/399/411/414 all ship without it while grandparent 389 carries it; the predecessor cycle recorded the same gap one day ago as its w8-1)*
0. `plan_lint` at a faithful deposit-shaped mirror; the measured `(o1)` set is the declared expected state.
1. A0-fresh re-verify immediately before the copy: E0/P0, the NT id-set, `LESSONS.md` porcelain, `decisions/` empty.
2. ⚠️ **Read `id_sequence` AT deposit** (read-only) and re-token every filename id site — it read 425 at authoring and has moved twice already in this arc.
3. Defensive claim-race commit sequence; the daemon claims within the same second.
4. Post-deposit `ls` of the deposited path, and commit the daemon's rename so the tree is clean while the plan is in flight.

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict.
- At every gate re-assert the non-terminal set is **exactly `{340, 342, 346, 350, 352}`** — a changed COUNT alone is not the test.
- After QA, confirm `lessons-forge/knowledge/FORWARD.md` is still **18** rows against the Step-1 baseline.
- ⚠️ **Confirm `reports/lessons-report-2026-08-14.md` is byte-unchanged at every gate** — it is the artifact FALSE-HERE item 1 puts at risk.
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle
**Tier:** T1 — additive, non-destructive writes (one `insert_proposal`, one new report file); structure-for-structure clone of shipped 414, so T-8 silent. ⚠️ T-5 was CONSIDERED and does not fire: nothing is deleted or overwritten **provided** item 1's date operand holds — which is why that item is a gate, not a note.
**Walk register:** `governance/knowledge/research/walk-register-cycle-classify-residual-bucket-2026-08-15.md` (schema v0.3 — ⚠️ **this cycle's register WILL be schema-conformant**; the predecessor's was `PRE-SCHEMA`, which left `walk_register_lint` inert on it for ten walks).
**Status:** cycle OPEN — walk 0 complete (a warm clone-diff against 414 plus a cold scout); its folds are live in the body and each carries its own `(w0-1 …)` or `(scout S1-n)` attribution. ⚠️ **This line states no count and no verdict** — the register is the single site. *(scout S1-15: the draft still read "cycle NOT STARTED. No walk has read this artifact" while four self-annotated folds sat in its body — the same sentence, under the same circumstances, that the predecessor cycle recorded at its w2-4.)*

**Per-lens lines** *(required by §3 and by `plan_lint`, which checks the five lens NAMES; kept compact — findings, ids and dispositions live only in the register)* *(scout S1-16)*:
- **Weak spots:** the cold scout's HIGH set — a missing `conn.commit()`, an undefined RESUME branch, and steps with no dispatch-state probe.
- **Destruction:** the report guard protected the wrong file by a relative path, and named no recovery commit; both corrected.
- **Vulnerabilities:** `output_dir` resolves against CWD and the agent runs in a worktree — the highest-value finding of the pass, and invisible to every check that used the same relative prefix.
- **Integration-record:** eleven omissions against the two parents, the clone's dominant failure mode; an omission leaves no token for a diff to catch.
- **ACID:** the one production write was uncommitted, so every post-condition would have read true from inside a doomed transaction.

**Conformance (§5):** `plan_lint` at a FAITHFUL deposit-shaped scratch mirror — never the real `decisions/`. **Measured at close: exit 0, `(o1)` candidates fired ZERO, and the only WARN is the Closing line, which this block now supplies.**

**Closing:** the final walk read **DRY on all five lenses — instruction 0 / record 0**, with no restructuring fold, so §2's bar is met on a dry pass and **there is no residue to enumerate.** Evidenced, not asserted: **16 of 16** load-bearing values re-verified against live state at close (E0, P0, the entries count, the proposals count, the empty proposal set for entry>344, the work list, the NT id-set, STALE, `raw_content` length, the NULL tags column, the sentinel hash, `insert_proposal`'s six required positionals by `inspect.signature`, FORWARD, the at-risk 08-14 report present, the 08-15 report absent so the copy-aside arm is dead, and the hedged 353 prediction); all nine deposits across three steps confirmed inside their declared scope **using `gates._extract_plan_scope` itself**, not a hand-rolled check; the two folds touching `data/backups/` confirmed to compose (the S1-19 detector is `.db`-scoped, the copy-aside is `.md`); `fold_check` CLEAN. Fold-and-deposit exactly once.
**Walks:** recorded in the walk register, which is the single site for walk count, fold count and per-finding detail. This line names no count and enumerates no walk.

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```

---

## STEP 1 — Lessons Agent (classify the ONE; no report, no routing)

> **FIRST — post a short visible chat message (1-2 sentences).** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. **Its DB paths are relative and you run in a worktree** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it.**
>
> **⚠️ NO ROUTING.** `route` stays `NULL` at insert; Gate 1 is a separate plan with a CEO decision before it. **NO ingest, no UPDATE, no delete.**
>
> **Step 0 — dispatch state.** Three-place probe on `knowledge/development/dev-log-classify-residual-bucket-step-1-2026-08-15.md` (committed HEAD; working tree; `git log --all` + `branch --list 'bellows-preserved/*'`), each with its exit code captured; probe 3's exit carries NO signal — pair it with a positive control against `knowledge/FORWARD.md`. Any hit → **RESUME**; all absent → **FRESH**. ⚠️ **RESUME is defined, not assumed** *(scout S1-5: the draft branched to a word it never defined)*: a prior dispatch of THIS step wrote its dev log, so re-verify what already landed before doing anything — if `SELECT COUNT(*) FROM lesson_proposals WHERE entry_id = 345` is **1**, the classification already happened; do NOT insert a second, record `RESUME (classification already landed)`, re-run the post-conditions read-only, and deposit. If it is **0**, the prior dispatch died before the write: proceed as FRESH but say so.
>
> **Single-writer check** *(scout S1-21, dropped in the clone)*: `get_unclassified_entries` stable across TWO reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — THIS PROJECT ONLY; this plan's own file is normal, ZERO matches means the probe is broken, any OTHER match → HALT.
>
> **Pre-flight (read-only, raw output for each):** `get_unclassified_entries(conn)` == exactly `[345]` — **if it is `[]`, something already classified this entry → HALT**; `SELECT COUNT(*) FROM lesson_proposals WHERE entry_id > 344` == **0**; `E0` == 345; `P0` == 352; the NT id-list == `340,342,346,350,352`; `STALE_COUNT` == 3; sentinel entry-344 hash == `e7b607bd…`; FORWARD `grep -c "^| "` == 18. Any mismatch → HALT, reporting measured vs expected.
>
> **Scope:**
> - `knowledge/development/dev-log-classify-residual-bucket-step-1-2026-08-15.md`
>
> **Read the entry.** `SELECT raw_content, source_heading, tags FROM lesson_entries WHERE id = 345` — **bind 345 as a parameter; the heading contains DOUBLE QUOTES and must never be interpolated into a `sqlite3` CLI string.** 2388 chars at authoring.
>
> **Classify — ONE proposal.** Call `insert_proposal` (`:202`) with `route=None` and `status` left at its default. Its **six** required positionals are `conn, entry_id, category, suggested_action, reasoning, confidence` — ⚠️ **a seventh positional would bind to `status`; pass everything after `confidence` BY KEYWORD** — **re-verify the signature live with `inspect.signature` before calling and print it**; a changed signature → HALT. ⚠️ **The `reasoning` field MUST OPEN with these three MARKER TOKENS, byte-exact, each followed by your own prose** *(scout S1-17: "verbatim in substance" is self-cancelling — it pins no literal, so QA could only transcribe the field, not verify it. Adequacy of the prose is GATE 1's to judge; PRESENCE is what QA checks, and presence needs a literal)*:
> - `[DEDUP]` — then: this EXTENDS wrap step 7's existing two-destination rule rather than creating a new one.
> - `[REMEDY-GATED]` — then: the remedy is drafted, its builder committed, and it cannot dispatch until this proposal is routed; the ids are required builder arguments.
> - `[AUTHOR-CONFLICT]` — then: the proposal's author also authored its evidence and its drafted remedy and benefits from the outcome. Flag (G) is an expectation, not a gate: **disagreeing with the category or confidence is a finding to record, not an error.**
>
> ⚠️⚠️ **THEN COMMIT — `insert_proposal` DOES NOT.** Its docstring (`:211`) states verbatim: *"Thin DB-insert helper. Does NOT call conn.commit() — callers manage transactions."* **Call `conn.commit()` explicitly and print confirmation.** ⚠️ **And re-read the row from a FRESH connection afterwards**: every post-condition below would otherwise read TRUE from inside the same uncommitted transaction, and a rollback would leave perfect evidence with nothing written. *(scout S1-4. This is DC v2.11's pre-COMMIT sentinel class — proposal 341, entry 333 — re-tripped by a plan whose own corpus contains it.)*
>
> **Post-conditions — ⚠️ EVERY ONE READ FROM THE FRESH POST-COMMIT CONNECTION, never the writing one** *(w1-3: the S1-4 fold mandated the commit and the fresh read-back but did not bind these checks to it, so they could still have run inside the doomed transaction — the exact failure S1-4 exists to prevent, left one paragraph away from its own remedy)* **(all raw):** `MAX(lesson_proposals.id)` == **353**; exactly ONE new row with `entry_id = 345`, `route IS NULL`, `status = 'proposed'`; **the NT id-set is now `340,342,346,350,352,353`** — the five pre-existing untouched plus this one; `COUNT(*) FROM lesson_proposals` == 353; entries still 345; sentinel hash unchanged. **⚠️ `reports/lessons-report-2026-08-14.md` byte-unchanged** (`shasum -a 256`, recorded raw) — this step writes no report at all, so any change is a defect.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-classify-residual-bucket-step-1-2026-08-15.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for verdict.**

---

## STEP 2 — DEV (generate the report)

> **Before starting: Step 1's Receipt status must be a PROCEED-value** (allowlist: `Status: Complete`). Anything else → HALT. **Dispatch-state probe first:** three-place probe on this step's dev log (committed HEAD; working tree; `git log --all`), exit codes captured, probe 3 paired with a positive control. Any hit → RESUME: the report may already exist, so re-verify before generating and never regenerate over your own prior output. *(scout S1-6: steps 2 and 3 had no dispatch-state probe and no PROCEED gate, so a bellows re-dispatch would re-run the generator with no idempotency branch.)*
>
> Post a short visible chat message. You are the Forge Developer.
>
> **⚠️⚠️ TWO OPERANDS DECIDE WHETHER THIS STEP DESTROYS A SHIPPED ARTIFACT — and the dangerous one is NOT the date.** Call **`generate_lessons_report(conn, cycle_date, output_dir)`** (`src/lessons_forge.py:514`) with **BOTH** arguments explicit.
> - **`cycle_date="2026-08-15"`** — a required positional with no default, so it cannot be silently wrong; it can only be wrong by inheritance. ⚠️ **`"2026-08-14"` appears 31 times in the clone parent** — never copy the date from the lineage. *(scout S1-1: this step previously named no function at all, deleting the countermeasure while naming the hazard.)*
> - **⚠️ `output_dir` — THE ACTUAL HAZARD.** It defaults to the RELATIVE `"reports"` (`:515`) and is passed straight to `os.makedirs` (`:591`), so it resolves against CWD — **and you run in a worktree** (`.bellows-worktrees/<id>`). **Run `pwd` FIRST, print it, and pass `output_dir` as an ABSOLUTE path** rooted at `/Users/marklehn/Developer/GitHub/lessons-forge/reports`. *(scout S1-2: both parents mandated a `pwd` first and this clone dropped it. Every protective `shasum` below used the same relative prefix, so pre-check and post-check would have agreed with each other while measuring a file that is not the one at risk.)* `reports/lessons-report-2026-08-14.md` **EXISTS (7256 bytes at authoring) and is plan 414's shipped report** — regenerating for that date would overwrite it. **Pre-check, in this order, every path ABSOLUTE:** (1) `pwd`, printed; (2) `shasum -a 256 /Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-report-2026-08-14.md` recorded raw — this is the artifact at risk and the pre-image of the guard; (3) `ls /Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-report-2026-08-15.md` — **absent → generate** (the expected path); **present → copy aside FIRST** to `<abs>/data/backups/lessons-report-2026-08-15-superseded-<UTC>.md`, then regenerate. ⚠️ **The copy-aside target is `data/backups/`, NOT `reports/`** — `gates.py:820`'s dir-mention rule cannot authorize a same-dir sibling and `scope_check` would fail the step *(scout S1-11)*. After generating, **re-run the 08-14 shasum against the same ABSOLUTE path and assert byte-identity with (2)** — any change → HALT. ⚠️ **Recovery point if it is ever damaged: commit `e96f9b5`** (`[414] Step 2 Complete: generated lessons-report-2026-08-14.md`), verified to contain that file. *(scout S1-3: the draft had a detector conditioned on the 08-15 file — which is absent, so the arm was dead — and never protected the 08-14 file at all; and it named no recovery commit where 399 named one.)*
>
> ⚠️ **Zero `Recently-implemented` lines in the generated report** — `grep -Fc -- 'Recently-implemented' <report>; echo "EXIT=$?"`. That section is a REMOVED feature (still **0** occurrences in `src/lessons_forge.py`, re-measured at authoring), so a hit means it came back → HALT. *(scout S1-9: the sentinel was dropped in the clone; parent 414 carries it and it is still a live regression guard.)*
>
> ⚠️ **Zero `- **Route:**` lines in the generated report** — `grep -Fc -- '- **Route:**' <report>; echo "ROUTE-GREP-EXIT=$?"` — **both `-F` and `--` are load-bearing, and never pipe to `head`**; exit 1 with output `0` is the EXPECTED zero. A Route line means something routed, which this plan forbids → HALT. *(w0-1: dropped in the clone.)*
>
> **Scope:**
> - `reports/lessons-report-2026-08-15.md`
> - `knowledge/development/dev-log-classify-residual-bucket-step-2-2026-08-15.md`
> - `data/backups/` — ⚠️ declared as a PREFIX, not a filename, because the copy-aside target carries a runtime UTC timestamp and cannot be named exactly. *(w2-1: the S1-3/S1-11 fold moved the copy-aside here and the S1-12 fold added these Scope blocks; neither knew about the other, so the target was left authorized only by incidental text mention — the very weakness S1-12 was folded to remove. Verified with `gates._extract_plan_scope`, not by reading.)* The copy-aside arm is dead on the measured state (the 08-15 report is absent), and S1-19's consumer already detects an unexpected write under this prefix.
>
> **Surfaced expectation: 1** (`SURFACEABLE_BASE` 0 + this cycle's 1), per the predicate `status IN ('proposed','ambiguous')` at `src/lessons_forge.py:541`. A different count → HALT and report both numbers; do not adjust the report.
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-08-15.md`
> - `lessons-forge/knowledge/development/dev-log-classify-residual-bucket-step-2-2026-08-15.md`
>
> **STOP. Wait for verdict.**

---

## STEP 3 — QA

> **Before starting: Step 2's Receipt status must be a PROCEED-value** (allowlist: `Status: Complete`). Anything else → HALT. **Dispatch-state probe first**, same three-place form. *(scout S1-6)*
>
> Post a short visible chat message. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB **read-only** (`?mode=ro`, absolute path). **Verification + reporting only; a failing check is reported, never fixed. No Monitor. No routing.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-classify-residual-bucket-2026-08-15`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-classify-residual-bucket-qa-2026-08-15.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/`; `required_evidence_files` `["pytest_targeted.txt", "proposal.txt", "queue-untouched.txt", "report.txt", "schema.txt"]`. All five files AND the report with its table written BEFORE the block; APPEND the stdout; banner `Rule 20 — QA Self-Check Results` + `PASSED — SELF-CHECK PASSED` verbatim; end with the self-grep. Rule 19 verbatim; one glyph per status cell; no `|` in cells; `## Evidence and Narrative` immediately after the table.
>
> **Scope:**
> - `knowledge/qa/cycle-classify-residual-bucket-qa-2026-08-15.md`
> - `knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/`
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows before halting:
> 0. **Deliverables (Rule 17)** — per path `git log --oneline -1 -- <path>` (empty = ❌) AND `git status --porcelain -- <path>`.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` ONLY. **Baseline measured by this row's own mandated command at authoring: `55 passed`.** A delta is reported with both numbers, never asserted away.
> 2. **Exactly ONE proposal, correctly shaped** — `SELECT id, entry_id, category, confidence, status, route FROM lesson_proposals WHERE id = 353` → one row, `entry_id=345`, `route IS NULL`, `status='proposed'`; `COUNT(*)` == 353. → `proposal.txt`
> 3. ⚠️⚠️ **The Gate-2 queue is UNTOUCHED** — the pre-existing five `340,342,346,350,352` all still `accepted|codify` **by id set, not by count**; `STALE` still 3; sentinel entry-344 hash unchanged; entries still 345. → `queue-untouched.txt`
> 4. **`reasoning` carries all three required disclosures** — the dedup caveat, the drafted-and-gated remedy, and **the self-interest disclosure**. Quote the field raw. A missing disclosure is ❌ Critical: Gate 1 would route without it. → `proposal.txt`
> 5. ⚠️⚠️ **414's report is byte-unchanged** — `shasum -a 256 reports/lessons-report-2026-08-14.md` equals Step 2's pre-check value; and `reports/lessons-report-2026-08-15.md` exists and surfaces **1** proposal. → `report.txt`
> 6. ⚠️⚠️ **`get_unclassified_entries(conn)` == `[]` — THE CLASSIFY-PLAN INVERSION.** Plan A's correct closing state was `[345]`; this plan's is the EMPTY list. A non-empty list means classification did not complete. Quote it with a count token. Non-empty → ❌ Critical. *(w0-1: dropped in the clone. It is the definitive post-condition of this plan's entire purpose — the one row that proves the work happened — and its absence was invisible because an omission leaves no token for a diff to catch.)*
> 7. **No schema drift** — PRAGMA table_info + constraints vs `src/db.py` DDL; raw `.schema` both tables → `schema.txt`. *(w0-1: also dropped. Restored rather than argued away: "423's QA checked it an hour ago" is a subsumption claim about an interval in which a migration COULD have run, and the check costs one command.)*
> 8. **The disposition line and the three markers** — `grep -F "DISPOSITION | entry=345"` the Step-1 dev log (exit echoed) → exactly 1; and `grep -Fc` each of `[DEDUP]`, `[REMEDY-GATED]`, `[AUTHOR-CONFLICT]` in the `reasoning` field read from the DB → each **1**. ⚠️ **Presence only. Whether the prose behind each marker is ADEQUATE is Gate 1's judgement, not QA's** *(scout S1-8, S1-17)*. → `proposal.txt`
> 9. **The hostile heading round-tripped** — join the report against the DB heading **bound as a query parameter** and confirm the `"everything else"` double-quoted phrase appears intact in the generated report. A count alone does not show the quoting survived *(scout S1-18)*. → `report.txt`
> 10. **The 8-status distribution delta** — the full zero-emitting distribution before/after: every terminal bucket UNCHANGED, `proposed` +1. ⚠️ A total-count check cannot see a row moving between two terminal buckets, and this plan says three times that a count is not the guard *(scout S1-10)*. → `queue-untouched.txt`
> 11. **Register posture** — `decisions/` non-Done contents are this plan's own file only; `knowledge/FORWARD.md` delta against Step 1's baseline is **ZERO** by the same probe form. ⚠️ **The probe is `grep -c "^| "` WITHOUT `-F`** — `-F` makes `^` a literal and returns 0/exit 1. Do not "fix" it by adding `-F`.
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-classify-residual-bucket-qa-2026-08-15.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/proposal.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/queue-untouched.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/report.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-residual-bucket-2026-08-15/schema.txt`
