# Lessons Forge — Cycle Run 2026-08-19, PLAN B: classify the consolidation batch and deposit the report (Gate-1 routing held to Plan C)

**Date:** 2026-08-19 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — classify) → Step 2 (DEV — report) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always
**cycle_tier:** T1 — T-8 (clone of `executable-425`).
**Slug:** `cycle-classify-consolidation-batch-2026-08-19`
**Project:** lessons-forge
**Author:** Planner
**dispatch_mode:** bellows
**Priority:** 1

## CEO Context

**Classify only.** This plan classifies the **`W`** unclassified corpus entries that plan **456** ingested, and deposits the cycle report. **It routes nothing.** Every proposal it creates leaves `route` **NULL** and `status` **`proposed`**; Gate-1 routing is **Plan C** and belongs to a NON-AUTHOR.

⚠️⚠️ **THE AUTHOR-CONFLICT IS LARGER HERE THAN AT ANY PRIOR CYCLE, AND IT IS THE REASON THIS PLAN EXISTS SEPARATELY.** 425 classified **one** entry and flagged it `[AUTHOR-CONFLICT]`. This batch contains **five entries the Planner wrote on 2026-08-19**, each arguing for a change to `DRAFTING_CYCLE.md` or `PLANNER_TEMPLATE.md` that the Planner authored, evidenced, proposed the remedy for, and benefits from — including the retirement of PT v4.89's project-bin arm. **The classifier may propose; only Gate 1 may accept, and Gate 1 is not the Planner.** Every proposal derived from those five carries the `[AUTHOR-CONFLICT]` disclosure marker, and the plan asserts their presence mechanically rather than trusting the agent to have thought about it.

**Clone lineage — measured, not recalled:** 423 (Plan A) → **425 (Plan B, the direct origin)** → 427 (QA-only corrective) → 428 (Gate-1 write). ⚠️ **425 is HALTED and is still sitting in `decisions/` as `halted-executable-425.md`.** Cloning a halted plan is legitimate here — its steps 1 and 2 completed with every gate passing — but the reason it halted is inherited machinery and is re-stated below rather than left to be rediscovered.

### ⚠️⚠️ WHY THE CLONE ORIGIN HALTED — inherited and re-measured 2026-08-19

1. ⛔ **THE WORKTREE ABSOLUTE-PATH TRAP — this is what killed 425.** Its Step 2 mandated `output_dir` as *"an ABSOLUTE path rooted at `/Users/marklehn/Developer/GitHub/lessons-forge/reports`"*. That is the **MAIN repo's** reports directory. The agent runs in a worktree, so the report was written **outside the sandbox**, leaving an untracked file in main that teardown's merge then refused to overwrite — `worktree_teardown` aborted and the plan halted with Step 3 never running. **The instruction was a fix for a real hazard (`output_dir` defaults to a CWD-relative `reports`) that prescribed a remedy worse than the disease.** ⚠️ **The rule, verbatim from 425's step-2 verdict: in a worktree-isolated dispatch an absolute path must be anchored at `pwd` (the worktree root), NEVER at the main repo root. The fix for CWD-relative is not "absolute" — it is "absolute WITHIN the sandbox".** Re-verified 2026-08-19: `lessons-forge/.git` exists and `.bellows-worktrees/` is present, so worktree isolation **does** apply to this project.
2. **`insert_proposal` DOES NOT COMMIT** — the caller must, exactly as `ingest_lesson_entries` does not (plan 456's w7-1, proven there on a scratch copy — as measured in THAT plan, the connection read a post-ingest count while a fresh one read the pre-ingest count). ⚠️ **And the same corollary applies: verify post-conditions on a FRESH connection**, because a read on the writing connection returns the expected values from inside an uncommitted transaction whether or not the commit landed.
3. **THE REPORT DIRECTORY IS DESTRUCTIBLE.** `lessons-forge/reports/` holds `lessons-report-2026-08-13.md`, `-08-14.md` and `-08-15.md`. 425 pinned the prior report's sha before and after; that guard is inherited and the pin is re-measured at walk 0.
4. **THE CLASSIFY-PLAN INVERSION — the definitive proof the work happened.** After classification `get_unclassified_entries()` must return `[]`. ⚠️ 425's clone had **dropped** this check and its walk-0 clone-diff restored it; it is the one post-condition that cannot be satisfied by a partial run.
5. **THE BATCH IS `W`, NOT 1.** 425 classified a single entry. ⚠️⚠️ **AND THAT IS WHY 425 COLLAPSED THE CLUSTER APPARATUS — a reason that does NOT hold here.** 414 partitioned six entries into four clusters via its Flag (G); 425 wrote that *"here there is a single entry, so the cluster apparatus collapses"*. **This clone inherited the collapsed form without re-deciding it, on a batch of `W`.** The classifier is therefore given no instruction about relatedness across `W` entries that include four on drafting-cycle mechanics and two on cold-seat conduct. ⚠️ **Not folded into a cluster mechanism here** — inventing one at walk 6 would be novel machinery in a T1 clone — but **recorded as an explicit, deliberate omission for Gate 1 and for the next clone**, rather than an inherited default nobody examined. *(w6-4.)* `W` is measured at walk 0 below, and the ids are contiguous.

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared** (honing-notes P-5). Every other section references a symbol.

| id | pin | before | after | probe |
|---|---|---|---|---|
| M1 | **`W`** work list | **25** (ids 346–370, contiguous) | **0** | `len(get_unclassified_entries(conn))` — the inversion, on a FRESH connection |
| M2 | **`P0`** proposals | **353** | `P0` + `K`, and ⚠️ **`K` ≥ `W` is DERIVABLE, not assumed** — see below | `select count(*) from lesson_proposals`. ⚠️ **RECORD-ONLY, not a gate**: `K` is not predictable and must never be pinned to a number *(w4-1: QA is told to re-run every pin, which would make an unpinnable row read as a failed check — the defect plan 456 hit at w4-3 with its status distribution)*. |
| M3 | route on every NEW proposal | — | **NULL, every one** | `select count(*) from lesson_proposals where id > P0 and route is not null` → **0** |
| M4 | status on every NEW proposal | — | every one is `proposed` | `select count(*) from lesson_proposals where id > P0 and status <> 'proposed'` → **0** *(w1-4: the bolded-backtick form made `propagation_check` parse `proposed` as a numeric symbol with value 0 and pollute the symbol table)* |
| M5 | **`E0`** corpus entries | **370** | **370 — UNCHANGED** | this plan classifies; it must not ingest |
| M6 | pre-existing non-terminal set | `{340,342,346,350,352}` | **still present, untouched** | the live Gate-2 queue must not move |
| M7 | `[AUTHOR-CONFLICT]` markers | — | **one per Planner-authored entry** | `select count(distinct entry_id) from lesson_proposals where id > <P0 bound in pre-flight> and entry_date_is_2026_08_19 and reasoning like '%[AUTHOR-CONFLICT]%'` → **5**. ⚠️ **Select the five by `entry_date = '2026-08-19'`, never by a hard-coded id range** — measured at walk 2 they are contiguous, but an id range is a coincidence of ingest order while the date is the actual defining property. ⚠️ **Bind `P0` from pre-flight; do not hard-code it** *(w2-3: this probe hard-coded `353`, which silently becomes wrong the moment `P0` moves, and an id endpoint that collides with `E0`'s value)*. *(w2-2: the row previously said "≥ 5" with NO probe and no statement of which entries — an unverifiable pin on the plan's most conflicted surface.)* **Presence asserted mechanically; ADEQUACY is Gate 1's judgement and is not asserted here.** |
| M8 | the three destructible reports | `08-13` **12,212 B** `7cfd7904c8491976…` · `08-14` **7,256 B** `f1807cf266b36954…` · `08-15` **2,593 B** `b21281169ac1a138…` | **all three byte-identical** | `shasum -a 256`, taken with the **same worktree-anchored prefix** the generator uses *(w2-1: three sections cited "the three report shas from §Numbers" and the shas appeared NOWHERE in the plan — the destruction guard pointed at a pin that did not exist)* |
| M10 | **sentinel** — corpus entry **345** | `8df4331b1596f12d…` | **unchanged** | classification writes only `lesson_proposals`; the sentinel turns that from a claim into a measurement *(w6-1: 425 pinned a sentinel and this clone dropped it — found by the artefact pass, not the fact-diff)* |
| M11 | `STALE_COUNT` | **3** (ids 98/121/130) | **3, unchanged** | `select count(*) from lesson_proposals where status='stale'` — a population distinct from M6 that a stray UPDATE would move *(w6-2)* |
| M12 | `SURFACEABLE_BASE` | **0** | `K` — ⚠️ **RECORD-ONLY** | `select count(*) from lesson_proposals where status in ('proposed','ambiguous')`. ⚠️ **Labelled DISTINCTLY from M6**, as 425 insisted: this one is EXPECTED to move to `K`, because every proposal this plan creates is `proposed`. Gating it would false-halt a correct run *(w6-3)* |
| M9 | today's report | **ABSENT** | **exists, and is none of M8** | `ls "$(pwd)/reports/lessons-report-2026-08-19.md"` — ⚠️ **worktree-anchored, like M8.** *(w3-1: this pin used a bare relative `reports/…` in the one plan whose clone origin HALTED on worktree path resolution. In a worktree it would measure the sandbox copy; run from main it would measure a different file — and either way it would look like it worked.)* |

⚠️ **`K` is deliberately unpinned and that is not laziness.** A classifier that must hit a predicted proposal count is a classifier under pressure to fabricate or suppress. **What is pinned is the SHAPE of every proposal it emits (M3, M4, M7), never how many.**

✅ **But a LOWER BOUND is derivable and is therefore asserted: `K` ≥ `W`.** `get_unclassified_entries()` returns every entry with no non-stale proposal, so **M1 == 0 means each of the `W` entries acquired at least one** — the bound follows from the inversion rather than from any prediction about the classifier. **Assert `K` ≥ `W` in QA.** *(w4-2: the plan had this guarantee available from its own machinery and was not using it. An unpinnable quantity is not an unconstrained one.)*

## Scope

Mutates one artifact — the corpus at `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — plus the declared deposits and one new report. ⚠️ **Look-alikes, measured:** `lessons-forge/forge.db` and `lessons-forge/lessons.db` are **0-byte decoys**; `forge/forge.db` is a **real 61.6 MB database from a different project**. Do **not** route any proposal, do **not** re-ingest, do **not** touch `LESSONS.md`, `PLANNER_TEMPLATE.md` or `DRAFTING_CYCLE.md`, and do **not** overwrite any existing report.

## HALT ROUTING

Any measured value outside its stated expectation → **HALT**, quoting every measured input. **Never repair forward.** On any HALT: commit existing deposits by explicit pathspec and record the gate, its measured value, and **whether the classification committed** — that last fact is what a resume needs.

**Authorized writes:** the `insert_proposal` calls **and their single `conn.commit()`**, the report (Step 2), and the declared deposits. Nothing else.

## STEP 1 — Lessons Agent: classify the `W` entries (no report, no routing)

> **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. ⚠️ **Its DB paths are relative and YOU RUN IN A WORKTREE** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL, DIFFERENT, 61.6 MB database — never open it**; `lessons-forge/forge.db` and `lessons-forge/lessons.db` are **0-byte decoys** returning false absences.
>
> **⚠️ NO ROUTING.** `route` stays **NULL** at insert and `status` stays at its default `proposed`. Gate 1 is Plan C and belongs to a non-author. **No ingest, no UPDATE, no delete.**
>
> **Env facts:** `grep` is a ugrep shim — `-F` for literals; **a zero-match `grep -c` prints `0` and EXITS 1** (read stdout, never `$?`). ⚠️ **Batch headings contain a backtick, four apostrophes and a double quote** — **bind every entry id and heading as a PARAMETER; never interpolate a heading into a `sqlite3` CLI string.**
>
> **Deposits:**
> - `knowledge/development/dev-log-classify-consolidation-2026-08-19.md`
> - `knowledge/development/evidence-classify-2026-08-19.txt`
>
> ### Step 0 — dispatch state
> Three-place probe on this step's dev-log path (committed HEAD; working tree; `git log --all` + `branch --list 'bellows-preserved/*'`), each exit code captured. ⚠️ Probe 3's exit carries **no** signal — pair it with a positive control against `knowledge/FORWARD.md`. Any hit → **RESUME**; all absent → **FRESH**. State the determination first.
>
> ⚠️ **RESUME IS DEFINED, NOT ASSUMED, AND THIS BATCH DEFINES IT MORE SHARPLY THAN 425 COULD.** Step 1 commits **once, after all inserts**, so the work list is only ever **`W`** (nothing committed) or **0** (everything committed).
> - work list == `W` → the prior dispatch died before the commit. Proceed as FRESH, say so.
> - work list == 0 → the classification already landed. **Do NOT re-insert.** Record `RESUME (classification already committed)`, re-run the post-conditions read-only, deposit, stop.
> - ⚠️ **work list strictly between 0 and `W` → HALT.** A single-commit design cannot produce a partial work list, so a subset is positive evidence of a **foreign writer**. *(425 had a batch of one and could not express this check at all.)*
>
> **Single-writer check:** `get_unclassified_entries` stable across TWO reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — **THIS PROJECT ONLY**; this plan's own file is normal, **ZERO matches means the probe is broken**, any OTHER match → HALT.
>
> ### Pre-flight (read-only, raw output for each)
> `get_unclassified_entries(conn)` == exactly the `W` entry ids, the contiguous range recorded at walk 0 ⚠️ *(whose upper endpoint coincidentally equals `E0`'s value — they are an ID and a COUNT and must not be conflated; w1-3)* · `SELECT COUNT(*) FROM lesson_proposals WHERE entry_id IN (<the `W` work-list ids>)` == **0** ⚠️ *(w3-2: this hard-coded `entry_id > 345`, a boundary that is only correct because it happens to equal the pre-456 corpus size. Bind the work list — it is the defining property; the boundary is an artefact. Same class as w2-3.)* · `E0` == **M5** · `P0` == **M2 before** · NT id-list == **M6** · **M10** sentinel hash · **M11** `STALE_COUNT` · **M12** `SURFACEABLE_BASE` ⚠️ *(recorded, not gated — it is EXPECTED to become `K`)* · reports dir contains exactly the three artifacts pinned in §Numbers and **no** `lessons-report-2026-08-19.md`. Any mismatch → HALT with measured vs expected.
>
> ### Classify
> For each of the `W` entries, read it with a **parameter-bound** `SELECT raw_content, source_heading, tags FROM lesson_entries WHERE id = ?`, then call `insert_proposal` (`src/lessons_forge.py:202`) with `route=None`.
> ⚠️ **Its six required positionals are `conn, entry_id, category, suggested_action, reasoning, confidence` — a SEVENTH positional binds to `status`. Pass everything after `confidence` BY KEYWORD.**
>
> ⚠️⚠️ **DISCLOSURE MARKERS — mechanically asserted, not left to judgement.** Five entries were authored by the Planner on 2026-08-19 and argue for changes the Planner benefits from. **Every proposal derived from one of those five carries `[AUTHOR-CONFLICT]` in its `reasoning`.** Use `[DEDUP]` where a proposal overlaps an existing corpus class and `[REMEDY-GATED]` where the remedy needs a decision the classifier cannot make. **Presence is this plan's post-condition (M7); ADEQUACY is Gate 1's judgement and explicitly not asserted here.**
>
> ⚠️⚠️ **THE THREE MARKERS ARE NOT SYMMETRIC HERE, AND 425's TREATMENT CANNOT BE COPIED.** 425 asserted all three present exactly once because its single entry genuinely warranted all three. Across `W` entries they differ in kind:
> - **`[AUTHOR-CONFLICT]` is DETERMINISTIC** — it applies to exactly the entries dated 2026-08-19 and to no others. Pinned as **M7**.
> - **`[DEDUP]` and `[REMEDY-GATED]` are CONDITIONAL** — they apply only where a proposal actually overlaps a recorded class, or where its remedy needs a decision the classifier cannot make. ⚠️ **Pinning a count for either would force the classifier to fabricate markers to hit a number** — the same reason `K` is unpinned (§Numbers). **Record their counts raw; assert nothing about how many.**
>
> ### THE DISPOSITION LINE — restored from 425, which this clone had dropped
> ⚠️ **Without it, a missing marker is indistinguishable from a marker the classifier never considered.** For **every** entry in `W`, write one line to the dev log in exactly this form, byte-exact prefix:
> ```
> DISPOSITION | entry=<id> | proposal=<id> | remedy: <one clause> | markers: <those that apply, or NONE>
> ```
> **`markers: NONE` is a legitimate and expected value.** The line's purpose is to make the classifier's judgement VISIBLE per entry, so Gate 1 reads a decision rather than inferring one from silence. **Post-condition: `grep -cF 'DISPOSITION | entry=' <dev log>` == `W`** — one per entry, no more, no fewer. *(w5-1: the clone dropped this record wholesale; my walk-0 clone-diff did not catch it, and it is the only artefact that makes an ABSENT marker auditable. w5-2: the asymmetry above was never stated, so a reader comparing to 425 would expect three pinned markers and find one.)*
>
> ### THE COMMIT
> ⚠️⚠️ **`insert_proposal` DOES NOT COMMIT** (`lessons_forge.py`, three docstrings state it). **Issue exactly ONE `conn.commit()` after all `W` inserts.** Without it the step reports success and writes nothing — proven in this lineage on plan 456, where an uncommitted ingest read correct from inside its own transaction and vanished on close.
>
> ### Post-conditions — ⚠️ ON A FRESH READ-ONLY CONNECTION, NOT THE WRITING ONE
> A read on the writing connection sees the **uncommitted** transaction and returns the expected values whether or not the commit landed. Close, reopen read-only by absolute path, then assert **M1** (the inversion — `get_unclassified_entries()` returns `[]`, the one post-condition a partial run cannot fake), **M3**, **M4**, **M5**, **M6**, **M7**, **M10** (sentinel unchanged) and **M11** (`STALE_COUNT` unchanged), and record **M2** (`K`, asserting only `K` ≥ `W`) and **M12** raw.
>
> ### Deposit
> Write both deposits, `git add` **by explicit pathspec**, commit. **Do not `git add -A`.**

## STEP 2 — DEV: generate the report

> **Step 1's Receipt status must be `Status: Complete`.** Anything else → HALT.
> **Dispatch-state probe first** — three-place probe on this step's dev log, exit codes captured, probe 3 paired with a positive control. Any hit → RESUME: the report may already exist; **re-verify before generating and never regenerate over your own prior output.**
>
> Post a short visible chat message. You are the Forge Developer.
>
> ⚠️⚠️ **THIS IS THE STEP THAT HALTED THE CLONE ORIGIN. READ THIS BEFORE CALLING ANYTHING.**
> Call **`generate_lessons_report(conn, cycle_date, output_dir)`** (`src/lessons_forge.py:514`) with **BOTH** arguments explicit.
> - **`cycle_date="2026-08-19"`** — a required positional with no default. It can only be wrong by **inheritance**; never copy a date from the lineage.
> - ⛔ **`output_dir` — THE HAZARD, AND 425'S REMEDY WAS WORSE THAN THE DISEASE.** It defaults to the RELATIVE `"reports"` (`:515`) and is passed straight to `os.makedirs` (`:591`), resolving against CWD — **and you run in a worktree**. 425 "fixed" this by mandating an absolute path **rooted at the MAIN repo**, which wrote outside the sandbox and left an untracked file that teardown's merge refused to overwrite; the plan halted and its Step 3 never ran.
>   **DO THIS INSTEAD: run `pwd` FIRST and print it; pass `output_dir` as `"$(pwd)/reports"` — absolute, and anchored at the WORKTREE ROOT.** The fix for CWD-relative is not "absolute", it is **"absolute WITHIN the sandbox"**.
>
> **Destruction guard — **M8** and **M9**, re-asserted here before and after:** the reports directory holds three shipped artifacts and **no `lessons-report-2026-08-19.md`**. Take a `shasum -a 256` of all three **before** generating and re-assert all three **after** — ⚠️ **using the same absolute worktree-anchored prefix as the generator**, or the pre- and post-checks will agree with each other while measuring files that are not the ones at risk.
>
> **Deposits:**
> - `knowledge/development/dev-log-report-2026-08-19.md`
> - `reports/lessons-report-2026-08-19.md`
>
> `git add` by explicit pathspec; commit in this step. ⚠️ **The bullet-list form is load-bearing** — `plan_lint` parses paths from bullets and an inline form yields **zero**. *(w1-2: my THIRD instance of this exact defect — plan 451 S1-3(b), plan 456 w2-1, and here. Recorded as a repeated personal defect, not a fresh discovery.)*

## STEP 3 — QA

> **QA SELF-CHECK — Rule 20.** Post the block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` verbatim under the banner `Rule 20 — QA Self-Check Results`, and close with the literal line `PASSED — SELF-CHECK PASSED`. **Both strings are matched literally by `plan_lint` (c).**
>
> Verification only. **Evidence must be RAW command output pasted verbatim.**
>
> **Deposits:**
> - `knowledge/development/qa-classify-consolidation-2026-08-19.md`
> - `knowledge/development/qa-evidence-classify-2026-08-19.txt`
>
> ⚠️ **`qa_test_result` WILL FAIL and that is STRUCTURAL, not a defect.** Read from `bellows/gates.py:735–777`: the gate fires on any QA step, has **no opt-out**, and requires a line matching `(\d+)\s+passed`. **This plan runs no pytest**, so no correct execution can satisfy it. Plan 456's step-2 verdict adjudicated the identical case. ⚠️ **Supplying a `.txt` does NOT fix it** — that only moves the gate from "no .txt evidence deposit found" to "no parseable pytest summary". Expect the pause; the other gates carry the certification.
>
> 1. Re-run every **GATED** pin in `## Numbers discipline` in table order on a **fresh read-only connection**, printing raw output. Do not restate values here. ⚠️ **M2 is RECORD-ONLY** — report `K` raw and assert only the derivable bound `K` ≥ `W`; do not treat an unpinnable row as a failed check. *(w4-1.)*
> 2. Re-assert **M1** (the inversion) independently of Step 1's report.
> 3. Re-assert **M8** (all three shas byte-identical) and **M9** (today's report exists and is none of M8).
> 4. Confirm **no routing occurred**: **M3** and **M4** both zero, and **M6** still present.
> 3b. **The pins walk 6 restored:** re-assert **M10** (sentinel entry 345 unchanged) and **M11** (`STALE_COUNT` unchanged); report **M12** raw. ⚠️ *(w7-1: M8–M12 were declared in the table and referenced by NO step — five pins that could not fail. M8/M9 were reachable through prose; M10–M12 were reachable through nothing at all.)*
> 4b. **The disposition record:** `grep -cF 'DISPOSITION | entry=' <Step-1 dev log>` == `W`, and `grep -Fc` each of `[DEDUP]`, `[REMEDY-GATED]`, `[AUTHOR-CONFLICT]` across the new proposals' `reasoning` fields — ⚠️ **report the first two RAW and gate only `[AUTHOR-CONFLICT]` against M7.** Presence only; adequacy is Gate 1's.
> 5. `git show --stat <this step's commit>` — assert only the declared deposits changed.

## Drafting Cycle

- Weak spots — steps authored from 425's machinery; RESUME defined by the single-commit design, which admits only work list `W` or 0 (w1-6).
- Destruction — the report directory holds three shipped artifacts, pinned by sha before and after; `output_dir` anchored at the worktree root, which is what halted 425.
- Vulnerabilities — backtick/apostrophe/double-quote headings force parameter binding; ugrep exit-1; `insert_proposal` does not commit.
- Integration — clone origin is HALTED and its halt cause is inherited machinery (w0); `qa_test_result` is structurally unpassable here, per plan 456's verdict.
- ACID — one commit after all `W` inserts; post-conditions verified on a FRESH connection because the writing one reads through an uncommitted transaction.

**Walk 0 (context pin):** register `lessons-forge/knowledge/research/walk-register-cycle-classify-consolidation-batch-2026-08-19.md`. Clone-diff against **425 (halted)** run BEFORE lens 1; five inherited facts recorded, the halt cause identified as a plan defect and re-verified live. `W` **25** (ids 346–370) · `P0` **353** · `E0` **370** · worktree isolation **CONFIRMED** (`lessons-forge/.git` present) · reports dir holds three destructible artifacts. **Direction verdict pending walk 1.**
