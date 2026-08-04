# Lessons Forge — Gate 1 Route Disposition 2026-08-03 (route the 16 session-17/18 proposals)
**Date:** 2026-08-03 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (DEV — route + verify) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T2

## CEO Context

Gate 1 for the 16 proposals cycle 296 produced (entries 199–214 → proposals 207–222). **CEO disposition, taken 2026-08-03: all 16 → `codify`**, with five riders below. Gate 2 is a separate plan with a CEO decision between.

**⚠️ THIS GATE WRITES `route` ONLY — NO status change.** All 16 keep `status='proposed'`. The status distribution is byte-identical before/after — an invariant to CHECK, not assume. The only delta is `route` NULL→`codify` on exactly sixteen rows.

**⚠️⚠️ NO HAND-WRITTEN SQL WRITES.** Every write is `set_proposal_route(conn, id, 'codify')`.

**[EXECUTED HERE — 2026-08-03]** `src/lessons_forge.py:256` read at authoring. Parameterised (`UPDATE lesson_proposals SET route = ? WHERE id = ?`), validates against `_VALID_ROUTES` (`:199`), **does NOT commit internally**, **does NOT check `rowcount`**, and **returns `None`** — a call naming a nonexistent id is a **SILENT NO-OP**. It validates the route *value*; **nothing validates the *id*.**

### Rule 21 — justification for `Test Scope: targeted`

**[EXECUTED HERE — 2026-08-03]** The repo has exactly ONE test module, `src/test_lessons_forge.py`, and `--collect-only -q` reports **55 tests collected**. **Targeted and full are therefore the same run here**; `targeted` is declared because this plan writes no code and the suite is a regression check only. ⚠️ **The suite runs on `:memory:` and never opens the canonical corpus** (all connects verified `:memory:`), so **it is NOT evidence for any corpus row.**

### Concurrency preconditions — and the DETECTION for each

⚠️⚠️ **BOTH are scoped to the whole plan, from dispatch until it CLOSES — not merely to dispatch.**

1. **No other lessons-forge cycle in flight.** A whole-corpus ingest between Step 1 and Step 2 can stale proposals. **DETECTION: QA row 1**, which asserts `status` AND both audit columns per row from a single read. ⚠️ **The corpus-wide `proposed` LIST COMPARISON is REPORTED under `## Evidence and Narrative`, not adjudicated — a legitimate in-gate cycle moves it, so it produces narrative for the CEO at the gate rather than a failing row.**
2. **No Gate-2 plan for 207–222 dispatched until this closes.** ⚠️ **Task A is what makes these sixteen Gate-2-ELIGIBLE**, so unlike a foreign batch this one becomes reachable *because of* this plan. **DETECTION: row 1 AND row 7 — two independent detections.** ⚠️ **Row 7 is not optional here: `291:428` shows Gate 2 commits every doctrine edit BEFORE it touches the DB, so a Gate 2 that lands its doc commits and dies before the flip is invisible to row 1 and detectable ONLY by the doctrine pins.**

⚠️⚠️ **THE PREMISE THAT MADE THESE OPTIONAL IN THE PARENT IS FALSIFIED, MEASURED.** 289 accepted "no in-window Gate-2 disposition is reachable" as a residual. **Plan 291 (Gate 2) shipped 2026-08-03 08:32 — one day after 289 closed. Plan 296 (a cycle) shipped the same day as this draft.** `291:414` records the general case: *"an unscoped corpus-wide count here false-HALTs a correct run, because a lessons-forge cycle during the arbitrarily-long Step-1→Step-2 gate legitimately adds proposals."* **A cycle inside a verdict gate is this shop's normal behaviour.**

**FORENSIC SIGNATURE for the CEO:** if **row 1** shows the targets moved `proposed → implemented`, that is a **violated precondition** (an in-window Gate 2), not corpus corruption. If **row 4(b)** fails alone, see Task C-b(ii)'s two-cause clause.

### Scope discipline

**Do NOT** edit `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `bellows/scripts/plan_lint.py` or `bellows/gates.py`. **Do NOT** change any `status`. **Do NOT** touch `src/`. **Do NOT** write any proposal outside 207–222. **Do NOT** append to `LESSONS.md` while this plan is deposited-but-un-run. **Rule 8: do NOT move this plan to `Done/`** — the agent is not the actor (`unauthorized_done_move` fires at `bellows.py:720,843`).

**Deposit-once discipline:** to be deposited exactly once; `knowledge/decisions/` was grepped for an existing plan of this class before authoring and holds only `Done/`.

**Authoring self-check:** `plan_lint.py` RUN at authoring against v4, and **the record states which checks fired**, not merely the exit code. ⚠️ **A clean exit is NOT evidence the §4 Drafting-Cycle block ran — that block is warn-only** (`296:186`). **Measured at authoring: exit 0, EIGHT PASS lines, ONE WARN** — `PASS` on (a) header / dispatch_mode / pause_for_verdict, (b) step 1 deposits, (b) step 2 deposits, (c) QA banner pair, (d) step 1 scope, (d) step 2 scope; `WARN: Drafting Cycle closing indicates fold as last event`. ⚠️ **That WARN is itself the evidence the §4 block executed** — which a clean exit code alone cannot establish. It is correct and deliberate while the cycle is open.

### The disposition table

**All 16 → `codify`.** ⚠️ **The riders are routing metadata the Gate-2 plan INHERITS.**

| # | entry | category | artifact | landing site | rider |
|---|---|---|---|---|---|
| 207 | 199 | governance_rule | DRAFTING_CYCLE.md | §2.7 subtractive-trim | **SCOPE — R5** |
| 208 | 200 | governance_rule | DRAFTING_CYCLE.md | §2.7 lens attestation | — |
| 209 | 201 | governance_rule | PLANNER_TEMPLATE.md | new rule → **63** | — |
| 210 | 202 | governance_rule | DRAFTING_CYCLE.md | §2 doneness parenthetical | **MERGE w/ 216** |
| 211 | 203 | governance_rule | RULE_20_SELF_CHECK_BLOCK.md | cell-equality contract | **SPLIT — R2** |
| 212 | 204 | governance_rule | DRAFTING_CYCLE.md | §2.7 command-output evidence | — |
| 213 | 205 | governance_rule | DRAFTING_CYCLE.md | §2.8 ledger management | — |
| 214 | 206 | governance_rule | DRAFTING_CYCLE.md | §2.6 cold-panel targeting | — |
| 215 | 207 | governance_rule | DRAFTING_CYCLE.md | §3 | **SCOPE — R1** |
| 216 | 208 | governance_rule | DRAFTING_CYCLE.md | §2 parenthetical + §2.6 | **MERGE w/ 210** |
| 217 | 209 | governance_rule | DRAFTING_CYCLE.md | §2.8 **AND** §2.6 | **TWO SECTIONS — R3** |
| 218 | 210 | governance_rule | PLANNER_TEMPLATE.md | Checklist #32 | **SCOPE — R4; MERGE-SITE w/ 222** |
| 219 | 211 | governance_rule | PLANNER_TEMPLATE.md | Rule 17 | **pairs w/ 211 — R2** |
| 220 | 212 | governance_rule | PLANNER_TEMPLATE.md | **Rule 18 *or* a new rule near 17/18** | placement OPEN |
| 221 | 213 | governance_rule | PLANNER_TEMPLATE.md | Rule 55(a) | **title amendment owed** |
| 222 | 214 | **instrumentation** | PLANNER_TEMPLATE.md | Checklist #32 | **MERGE-SITE w/ 218** |

⚠️⚠️ **THE id→entry_id MAPPING IS A CONTIGUOUS +8 OFFSET AND THE SEQUENCES OVERLAP IN 207–214.** Proposal 207 → entry 199; proposal **215** → entry **207**. **A reader seeing "207" must know which space it is in. Check every pair individually** — an off-by-one shifts every disposition by one row and the overlap hides it.

⚠️ **220's placement is deliberately left OPEN.** The proposal reads *"Rule 18 (or as a new rule near 17/18)"*; flattening it to "Rule 18" would hand Gate 2 a settled choice the proposal did not settle.

### The dedup record — the basis of the routing

**[EXECUTED HERE — 2026-08-03]** Rule 58(1) requires *"named, agent-runnable verification anchors **and explicit licence to disagree** — the pre-resolution cannot launder an assertion into an audited finding."* ⚠️ **THE LICENCE IS GRANTED: if A0-pre's live read disagrees with any row of the disposition table, the plan HALTS and the CEO re-decides — the table does not override the corpus.** ⚠️⚠️ **AND RULE 58(2), STATED EXPLICITLY: all sixteen proposals were investigated and this record is EXHAUSTIVE over the batch — four partials and twelve with no existing coverage. ⚠️ **Stated in the exhaustive form because it IS exhaustive; an earlier draft cloned 296's "no claim is made about anything not listed" wording, which is the honest form only for a record that sampled.**** The dedup pass against live doctrine found **FOUR PARTIALS and no full duplicates**:
- **215 → `DRAFTING_CYCLE.md:112`** already reads *"After compacting **or editing** the log, re-run the gate…"*, and the v1.3 History row (`:171`) records it as *"re-checked after any edit to the log (206)."* ⚠️ **That `(206)` is a PROPOSAL id from the PRIOR numbering space (entry 198) — it is NOT this batch's entry 206, which is proposal 214. A third numbering space overlaps here; do not read it as a self-reference.** → **R1.**
- **217 → `:108`** already mandates per-lens fold counts and forbids a running tally. → **R3.**
- **218 → Checklist #32's clause at `PLANNER_TEMPLATE.md:1349`** already reads *"verify the construction actually produces the expected delta."* → **R4.**
- **207 → `DRAFTING_CYCLE.md:87`** already reads *"Before removing a check on the premise that another check covers it, verify the subsumption against live data — per item, not in aggregate … until each item has been tested through the surviving check."* **That is the same test**, missing only 207's value→count framing and its confirm-it-fails direction. → **a scoped extension, not a clean-slate codification.**
All other TWELVE: no existing coverage found (re-checked against live text at round 5). **Anchors are the file:line citations above; re-runnable by opening each.**

### The five riders

**R1 — 215 is a TWO-sub-claim extension, not three.** Sub-claim (2), the broader trigger scope, is **already codified** (dedup anchor above). The genuinely absent pair: *necessary-but-not-sufficient*, and *the reflexive application of the no-quoting prohibition*.

**R2 — 211 SPLITS, and 219 is its other half.**
- The **authoring rule** routes `codify` into `RULE_20_SELF_CHECK_BLOCK.md`. **[EXECUTED HERE]** the contract lives there: `is_positive_row` at `:67`, prose at `:39`.
- ⚠️ **`:39` already says *"the token must be the entire cell value."* 211's genuinely NEW content is the CONSEQUENCE** — an annotated cell is neither a positive row nor a failing one, so **both** gates ignore it. **A Gate-2 author who lands only the "one token" sentence writes a duplicate.**
- The **mechanizable lint** is bellows-owned and **CONVERGES on the already-deferred status-cell glyph lint** — recorded as convergence, **not a new item**.
- **211 + 219 are two halves of one contract across two artifacts. Gate 2 sequences them together.**

**R3 — 217 lands in §2.8 **and** §2.6, and collides with §3's counting rule** (dedup anchor above). Gate 2 must RECONCILE per-lens with per-region.

**R4 — 218 is a scoped extension** of #32's existing delta clause, not an introduction of the delta principle.

**R5 — 207 is a scoped extension, not a clean-slate codification.** `DRAFTING_CYCLE.md:87` already carries the subtractive-trim-verified-against-live-data rule; 207 adds only the value→count framing and the confirm-it-fails direction. ⚠️ **Recorded as a rider because the riders are what Gate 2 inherits — an earlier draft left this finding in a prose bullet with `—` in 207's rider cell, which would have had Gate 2 codify it clean-slate and write a duplicate.**

⚠️ **AND A SECOND SAME-TARGET COLLISION: 218 and 222 BOTH land on Checklist #32** — 218 the post-condition assertion form, 222 canary-design guidance. Same sequencing hazard as 210+216.

### ⚠️ What Gate 1 is NOT deciding

**[EXECUTED HERE]** All 16 `#### Scout dispositions` lines (`knowledge/development/dev-log-cycle-step-1-2026-08-03.md:135–150`) read `agreed`; zero divergences. **But 296 bound the stricter evidence burden to only the four rare-tag proposals (216, 217, 218, 222).** For the other twelve, agreeing carried the light burden. Rule 58(3) (`PLANNER_TEMPLATE.md:1095`): *"equal evidence burden on every disposition, so the cheap/default one is not the low-effort path."* **The CEO weighed the 16/16 as an artifact of asymmetric burden and routed on the dedup record above.**

### Clone lineage — the diff, and WHICH plans it ran against

**[EXECUTED HERE — 2026-08-03] The shipped set was SORTED by commit date rather than recalled:**

| plan | shipped | class |
|---|---|---|
| 289 | 2026-08-01 16:48 | Gate 1 routing — the **structural** parent |
| 291 | 2026-08-03 08:32 | Gate 2 codification |
| **296** | **2026-08-03 11:59** | cycle run — **the newest lessons-forge corpus-mutating plan** |

⚠️⚠️ **AN EARLIER DRAFT ASSERTED 289 WAS BOTH THE ORIGIN AND THE NEWEST SAME-CLASS PLAN, AND THAT WAS FALSE.** It diffed against the **oldest of three**, and the machinery has been *strengthening* across them: `shasum` 3 → 12 → 11, `grep -F` 5 → 24 → 11, `immutable=1` **0 → 5 → 2**. **The `?immutable=1` hardening this plan carries was rediscovered by an ACID pass and asserted as novel; `291:414` had already shipped it, marked executed.** The diff now runs against **all three**: 289 for the Gate-1 state machine, 291 and 296 for current machinery.

⚠️ **TWO PLACES WHERE CLONING 289 FAITHFULLY IS THE ERROR:**
1. **`category` uniformity.** 289 asserts uniform and warns *"DO NOT 'CORRECT' IT BACK"* — about ITS batch. **This batch is non-uniform: 222 is `instrumentation`.** A faithful clone false-HALTs on 222.
2. **The Forward Register channel.** 289 states `lessons-forge/knowledge/FORWARD.md` does not exist and that only `lines[0]` survives. **Both are now false** — the file exists with 2 data rows, and `sanitize_items` splits ≥2 bullets into N rows. **A clone trusting 289 would emit its Receipt block as ceremony.**

⚠️ **AND A NOTE 291 LEAVES FOR CLONES, invisible without diffing** (`291:12`): *"A future clone must not 'restore' the extraction machinery without first re-checking whether its plan edits that file."* **Honoured below at QA row 7**, which takes the **routing-plan absolutist form**, not 291's weaker variant.

**⚠️⚠️ SUBTRACTION DISCIPLINE (`291:12`).** A subtraction from a parent must be **declared with its premise in advance**; an **undeclared** subtraction found by review is **REVERSED, not retroactively justified**. **This draft declares ZERO subtractions from 289/291/296. Everything a parent carries is either present here or named in the Ledger as a reversal.**

**⚠️⚠️ PROVENANCE CONVENTION.** `[EXECUTED HERE — <date>]` · `[INHERITED FROM <plan> — NOT RE-EXECUTED]` with the reason. ⚠️ **There is no third marker.** An earlier draft invented `[UNTESTED BRANCH]` for A00's derivation; a cold reader ran it in three commands across eight cases. **A marker whose meaning is "I did not run this" is the same marker regardless of its spelling** — 289 had already retracted this exact excuse. **Governs EXECUTION claims, not measured values**, which are confirmed at run time (Checklist #29).

---

## The authoring baseline

**[EXECUTED HERE — 2026-08-03]**, live, read-only:

| measure | value |
|---|---|
| entries / proposals | 214 / 222 |
| status distribution | implemented 153, superseded 28, proposed 16, rejected 15, reference 7, stale 3 |
| route distribution | NULL 146, codify 69, backlog 2, reference 5 |
| route NOT NULL — total | 76 |
| route NOT NULL — **outside** 207–222 | 76 |
| outside-range ROW IMAGE | 76 rows |
| `get_unclassified_entries(conn)` | `[]` |
| 207–222 with route NOT NULL | 0 |
| `status_updated_by IS NULL` | 16 — exactly `207…222` |
| `proposed` set | exactly `207…222` |

**DOCTRINE PINS — `shasum -a 256` run from the repo root (output shows root-relative names), measured at authoring. ⚠️ A0-snap and QA row 7 mandate the ABSOLUTE-path form and compare by 12-hex PREFIX, so the differing display form is immaterial:**
```
2d5cf9ab7c3a87ed825a1e1edcafea9a9b2598f30b29a7e48868558874a18ee0  DRAFTING_CYCLE.md
e8289d50f28711fdbf7c5319d812c229d3e7d2e255fc77f7ce868c19c01b6783  PLANNER_TEMPLATE.md
3accbce0c8d2b44586edc6c5f95582f775d0bce14276966b7ca90724e0ca5644  RULE_20_SELF_CHECK_BLOCK.md
```
⚠️ **Real measured values, not placeholders** — invented authoring pins are a recorded past defect.

⚠️ **EVERY VALUE IS RE-MEASURED AT RUN TIME; A MISMATCH IS A HALT, NOT AN ADJUSTMENT.**

⚠️⚠️ **TOTAL and OUTSIDE-RANGE are DIFFERENT MEASUREMENTS that both read 76 pre-write.** After the write they diverge: total → 92, outside stays 76. Report separately; crossing them passes for the wrong reason.

⚠️ **WHY 4(b) IS ADJUDICATED WHILE THE CORPUS-WIDE `proposed` LIST COMPARISON IS ONLY REPORTED — stated, because it read as inconsistent:** an in-gate lessons-forge cycle INSERTS proposals with `route=NULL`, so they never enter the outside-range image at all, while they do move the corpus-wide `proposed` count. **4(b) is immune to the legitimate in-gate event; the corpus-wide `proposed` count is not.**

⚠️⚠️⚠️ **NEITHER COUNT IS A VALUE GUARD** (entry 199, routed here as 207). **[EXECUTED HERE] The seven foreign rows with a non-`codify` route, BY ID:** `backlog` → **161, 169**; `reference` → **140, 141, 146, 164, 183**. Flipping any one to `codify` leaves the outside count at 76 with every count-based check passing. **The row image (4b / Task C-b(ii)) is the only detector.**

## Conflict Ledger — RUN-TIME constraints

**These are addressed to the executing agent and cited by the steps.**

| id | constraint | origin |
|---|---|---|
| C1 | A00 precedes every other task. | origin diff |
| C2 | Every outside-range guard is VALUE-level; a count is a corroborator only. | entry 199 |
| C3 | Nothing written to disk before A0-iso identifies this plan's own file. | origin diff |
| C4 | No assertion CLAIMS THE WRITE PATH WROTE a column it does not touch; asserting such a column is UNCHANGED is required, not forbidden. | marker M2 |
| C5 | `category` / `target_artifact` are NON-uniform, verified per row. | origin diff |
| C6 | Every mandated print varies with the thing it checks. | proposal 218 |
| C7 | Forward Register bullets are CONTIGUOUS and **each is ONE physical line**. | walk 1 + panel |
| C8 | Commands separated by `;` never `&&`; exit codes captured; never piped to `head`. | walk 1 (the `;`-vs-`&&` half) + `291:152` (the `grep -F` and `head` halves) |
| C9 | Every mandated capture has a named producer AND a named reader. | walk 1 |
| C10 | Every `.backup` read uses `?immutable=1`. | ACID |
| C11 | The irreplaceable before-image is deposited BEFORE the mutation — **non-destructively**. | ACID + panel |
| C12 | A guard's expected value derives from MEASURED behaviour. | ACID |
| **C13** | **A routing plan pins the three doctrine files UNCHANGED (absolutist).** Only a plan that edits doctrine by design uses "changed only in the intended ways". | **`291:83`** |
| **C14** | **A value measured once is CITED by COPY sites, never re-measured by them — but the ADJUDICATING reader re-measures live.** A comparison whose two operands are the same capture is a tautology. | **DECLARED REVERSAL of `296:283`'s cite-model** — 283 is the source of the copy-site half only, and states the absolutist form this plan does not adopt |
| **C15** | **Every check names the artifact it reads; a check aimed at a different artifact than the consumer is necessary, not sufficient.** | **panel X6** |
| ~~C16~~ | *(moved to the authoring-time table below)* — **An undeclared subtraction found by review is RESTORED, not retroactively declared.** | **`291:12`** |
| ~~C17~~ | *(moved to the authoring-time table below)* — **Every precondition names its detection row.** | **`296:182`** |
| **C18** | **No whole-corpus predicate is asserted against an authoring literal; scope to this plan's ids or anchor to a captured before-value.** | panel X19 |

### Authoring-time constraints (Planner-owned — NOT addressed to any executing agent)

| id | constraint |
|---|---|
| **C16** | An undeclared subtraction found by review is RESTORED, not retroactively declared. |
| **C17** | Every precondition names its detection row. |

⚠️ **Separated because an eighteen-row table handed to an executing agent, rows of which are instructions to the Planner, is a comprehension cost with no run-time payoff.**

⚠️ **C1 vs C3 — joint-resolved:** A00 writes a gitignored `.db`, never a tracked deposit. Different artifacts.
⚠️ **C3 vs C11 — joint-resolved:** A0-dep runs after A0-iso, so no pre-confirmation write occurs.
⚠️ **C11 vs the resume path — joint-resolved:** A0-dep is **non-destructive** (below), so a re-dispatch cannot clobber the original.

---

## How to Run This Plan

Bellows dispatches this plan automatically when deposited; no manual bootstrap required. (Rule 35 requires this section to be omitted or replaced with exactly this note for `dispatch_mode: bellows`.)

---
---

## STEP 1 — DEV (route the 16, then verify)

---

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file. **Do NOT move it to `Done/`.**
>
> You are the Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — skip with a note if absent). **Every canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`.
>
> ⚠️ **DECOY DATABASES — `lessons-forge/` ITSELF contains `forge.db`, `lessons.db` and `lifecycle.db` beside the canonical file, and `forge/forge.db` is a different real DB.** A bare `sqlite3.connect(<relative>)` SILENTLY CREATES a new empty file. **Absolute path, always.**
>
> **Scope:**
> - `knowledge/development/gate-1-route-207-222-prewrite-2026-08-03.md`
> - `knowledge/development/gate-1-route-207-222-captures-2026-08-03.md`
>
> ⚠️ **Paths are PROJECT-RELATIVE, deliberately.** A root-joined form (`lessons-forge/knowledge/…`) breaks QA row 0: from inside the submodule **both** `git log -- <root-joined>` and `git status --porcelain -- <root-joined>` return **empty with exit 0**, so `git log` reads as "never committed" → a false Critical, while porcelain reads PASS. **[EXECUTED HERE — 2026-08-03]** both commands return empty with exit 0 on a root-joined path from inside the submodule, while the project-relative form returns the commit; also measured in the parent (`289:343`).
>
> ⚠️⚠️ **COMMAND DISCIPLINE (C8), every command in this step.** Separate with `;` **never `&&`** — a legitimate zero count exits 1 and an `&&` chain silently skips everything after it. Capture meaning-bearing exit codes: `<cmd>; echo "EXIT=$?"`. ⚠️ **`grep` here is a ugrep SHIM: `-F` is MANDATORY for every literal.** A pattern beginning with `**` is a REGEX ERROR — it prints to stderr and **NOTHING to stdout**, which reads as "not found → PASS" having verified nothing. ⚠️ **NEVER pipe these to `head`, which masks the exit code.**
>
> **⚠️ EXECUTION ORDER.**
> 1. **A00** — restore point, then verify it is real. ⚠️ **FIRST (C1).**
> 2. **A0-iso** — isolation pre-flight.
> 3. **A0-pre** — precondition, *k*, set-identity.
> 4. **A0-snap** — the five before-snapshots **+ the doctrine pins**.
> 5. **A0-dep** — deposit and commit the pre-write snapshot, **non-destructively (C11)**.
> 6. **A** — the sixteen writes, then ONE commit.
> 7. **B**, **C** — read-only post-verification. **Run ALL before halting on any one.**
> 8. Deposit the dev-log and commit.
>
> **Open canonical read-WRITE for the writes** (`sqlite3.connect(<abs path>)`); **do NOT reuse a `?mode=ro` handle.** ⚠️ **[EXECUTED HERE — 2026-08-03] The single-commit form is ATOMIC against a crash:** Python's `sqlite3` issues an implicit `BEGIN` before DML at the default isolation level, so death before `conn.commit()` rolls back all sixteen. **No partial-write state is reachable from a crash** — only from a halt after commit, which *k* handles.
>
> ### Task A00 — RESTORE POINT BEFORE ANY WRITE, THEN VERIFY IT IS REAL
>
> Use `.backup`, NOT `cp` (live WAL). Absolute MAIN-tree path. Build it in a shell variable first.
>
> ```
> D=/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions
> F=$(ls "$D" 2>/dev/null | grep -E '^(in-progress|verdict-pending|halted|parked)-executable-[0-9]+\.md$')
> N=$(printf '%s' "$F" | grep -c .)
> [ "$N" = "1" ] || { echo "HALT: expected exactly 1 own plan file, found $N"; exit 1; }
> PLAN_ID=$(printf '%s' "$F" | sed -E 's/^(in-progress|verdict-pending|halted|parked)-executable-([0-9]+)\.md$/\2/')
> case "$PLAN_ID" in ''|*[!0-9]*) echo "HALT: derived plan id '$PLAN_ID' is not numeric"; exit 1;; esac
> mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-${PLAN_ID}-$(date -u +%Y%m%dT%H%M%SZ).db"
> echo "PLAN_ID=$PLAN_ID"; echo "BK=$BK"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> ```
> ⚠️ **[EXECUTED HERE — 2026-08-03] This block was run verbatim under zsh with the live ugrep shim, across EIGHT cases: 0 / 1 / 2 / 4 matching files, and all FOUR lifecycle prefixes.** Every case behaved as documented — `N=0/2/4` HALT with the count reported; `N=1` derives the id; each prefix yields the id with exit 0. ⚠️ **An earlier draft marked this untested on the ground that no lifecycle file existed at authoring. `D` is a shell variable — pointing it at a scratch directory costs three commands.**
>
> ⚠️ **The single-match guard does NOT assert the file is YOURS.** On a wrong tree A00 writes a backup stamped with a foreign id: gitignored, additive, mutates nothing, no gate sees it — **RECORDED, not guarded. Do NOT "fix" it by moving A00 after A0-iso (C1).**
>
> ⚠️ **A00's guard is STRICTER than A0-iso's, and the cost is real:** A00 halts on any second lifecycle-prefixed file across all four prefixes, while A0-iso forbids only another `in-progress-`/`verdict-pending-`. **A benign foreign `parked-` or `halted-` plan therefore aborts this run with a bare gate failure.** The gate failure IS the signal and it is the correct one; the cost is stated so it is not read as a defect.
>
> ⚠️ **Do NOT inline `$(date …)` between single-quoted parts of the `.backup` argument** — sqlite3 misparses it and writes NO backup. **[INHERITED FROM 289/284 — NOT RE-EXECUTED]** (reproducing it means deliberately issuing a malformed command).
>
> ⚠️⚠️⚠️ **READ THE BACKUP WITH `?immutable=1` — NEVER `?mode=ro` (C10).**
> **[EXECUTED HERE — 2026-08-03]**, each URI against its own fresh untouched `.backup`:
> ```
> ?mode=ro      exit=14   Error: in prepare, unable to open database file (14)
> ?immutable=1  exit=0    222
> plain path    exit=0    222
> ```
> A fresh `.backup` is a WAL-mode DB with **no `-shm`/`-wal` sidecars**, and `mode=ro` cannot create them. ⚠️ **The plain path also works and is DISQUALIFIED ANYWAY: it opens read-WRITE and CREATES `-wal`/`-shm` beside the artifact whose entire job is to be untouched.** ⚠️ **`?mode=ro` is the URI used everywhere else in this plan, so it is what you will reach for. Do not.** **A restore point you have not read back is not a restore point.**
>
> ⚠️ **If the `.backup` command ITSELF errors** (sidecar-less SOURCE): `echo "$BK"` FIRST, then re-run with that SAME LITERAL path without the `?mode=ro` URI. **[INHERITED FROM 289 — NOT RE-EXECUTED]** — 289 measured the failure leaving a **0-BYTE file** at the target. ⚠️ **Do NOT recompute the timestamp. Do NOT `rm` anything on the mandated path.** If two files exist under this plan id, say so and leave both.
>
> **VERIFY, IN THIS ORDER.**
> 1. ⚠️⚠️ **NON-ZERO SIZE FIRST** — `ls -la "$BK"`, byte count > 0. **[EXECUTED HERE — 2026-08-03]** `PRAGMA integrity_check` returns **`ok`, exit 0, on a 0-BYTE FILE** — and **through `?immutable=1` on a NONEXISTENT path it returns `ok` AND CREATES a 0-byte file.** **The size check is load-bearing precisely because the next step manufactures the artifact it checks. Do not reorder it.**
> 2. `sqlite3 "file:$BK?immutable=1" "PRAGMA integrity_check;"` → `ok`.
> 3. `sqlite3 "file:$BK?immutable=1"` counts for `lesson_entries` / `lesson_proposals` equal LIVE at backup time (authoring **214 / 222** — confirm against live, not these literals).
>
> Any failure → HALT before any write.
>
> ⚠️⚠️ **THE BACKUP IS THE PRE-WRITE STATE AND IT IS QUERYABLE.** Every before-item, **including 4b**, is reconstructible from `$BK` with `?immutable=1`. ⚠️ **But `$BK` is the ONLY unconditionally main-tree-durable artifact this step produces:** the canonical DB is written by absolute path and lands on main instantly, while **deposits are committed inside the bellows worktree and reach main only at teardown.** On any recovery the ordering is **`$BK` → the worktree branch → the deposit.**
>
> ⚠️ **RECOVERY IS SURGICAL (Rule 56):** the inverse is a single statement scoped to `id BETWEEN 207 AND 222` setting `route` back to NULL. ⚠️⚠️ **IT IS FOR THE CEO's ADJUDICATION AND IS NOT AUTHORIZED FOR THIS STEP — DO NOT RUN IT, UNDER ANY BRANCH.** Described rather than written out so it cannot be copied out and executed. ⚠️ **A00 does NOT rank or select among backups — it writes and verifies this run's own, nothing more. Selection is A0-dep's single rule, stated once there.** An earlier draft ranked here by size and "earliest survivor", which A0-dep then directly contradicted; the duplicate is deleted rather than reconciled.
>
> ### Task A0-iso — ISOLATION pre-flight
>
> **ABSOLUTE MAIN-TREE path — a worktree-relative `ls` passes VACUOUSLY.** `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/` and assert the POSITIVE signal: **your own plan file MUST appear** (`in-progress-*`, `verdict-pending-*`, `halted-*` **or** `parked-*` — **all FOUR; a two-prefix check false-HALTs every resume of a halted or parked step and reports the flatly wrong cause**) AND no OTHER `in-progress-*`/`verdict-pending-*` lessons plan.
>
> **File absent → wrong tree → HALT, fail-closed: write nothing (C3).**
>
> ⚠️ **There is deliberately NO quiescence probe here.** A 5-second double-read cannot detect anything on a system whose stated concurrency window is hours to days, and its only distinctive outcome is an unclassified HALT if a foreign writer lands inside that slot. **The real detection is Task C-b and QA row 4** — an earlier draft carried the probe while declaring it was not the guard, and it is deleted rather than kept as ceremony. ⚠️ **`get_unclassified_entries()` would be an especially bad quiescence signal — it filters on `status`, never `route`.**
>
> ### Task A0-pre — PRECONDITION
>
> `SELECT id, entry_id, status, category, confidence, route, target_layer, target_artifact FROM lesson_proposals WHERE id BETWEEN 207 AND 222 ORDER BY id` — assert **per row**:
> - exactly **16 rows**;
> - mapping exactly `207→199, 208→200, 209→201, 210→202, 211→203, 212→204, 213→205, 214→206, 215→207, 216→208, 217→209, 218→210, 219→211, 220→212, 221→213, 222→214`. ⚠️⚠️ **CHECK EVERY PAIR. Uniform +8, sequences overlap in 207–214** — an off-by-one shifts every disposition and the overlap hides it;
> - each `status='proposed'`; each `route` **NULL or already `codify`**;
> - `target_layer='governance'`, `confidence='high'` on all 16;
> - ⚠️⚠️ **`category` NON-UNIFORM — `instrumentation` on 222, `governance_rule` on the other fifteen (C5).** **A REVERSAL from 289, whose uniformity warning was about ITS batch.**
> - **`target_artifact` PER ROW** — `DRAFTING_CYCLE.md` for 207, 208, 210, 212, 213, 214, 215, 216, 217 (**9**); `PLANNER_TEMPLATE.md` for 209, 218, 219, 220, 221, 222 (**6**); `RULE_20_SELF_CHECK_BLOCK.md` for 211 (**1**);
> - ⚠️ **PER ROW, NEVER BY AGGREGATE.** A `DISTINCT`/`GROUP BY` proves the multiset and nothing about which id holds which value.
>
> **⚠️⚠️ COMPUTE *k* — THIS TASK IS ITS ONLY PRODUCER (C9).**
> `SELECT COUNT(*) FROM lesson_proposals WHERE id BETWEEN 207 AND 222 AND route = 'codify';` → state `k=<n>`. **Readers: Receipt item 0b and A0-snap's resume clause.**
> **ALSO capture the IN-RANGE row image** — `SELECT id||':'||COALESCE(route,'NULL') FROM lesson_proposals WHERE id BETWEEN 207 AND 222 ORDER BY id`. ⚠️ **`k` is a count; on a resume nobody can tell WHICH rows were already `codify` without this, and the surgical inverse becomes unauditable from the record.** **Producer: this task. Reader: Receipt item 0b, which carries it verbatim (C9).**
> - **k = 0** → fresh. **k > 0** → resume, **SAFE because the write is idempotent per id.** **Stated because it is what licenses continuing rather than halting.**
>
> **⚠️⚠️ SET-IDENTITY — computed in ONE statement (C8/C14):**
> ```
> SELECT (SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed'),
>        (SELECT COUNT(*) FROM lesson_proposals WHERE status='proposed' AND id BETWEEN 207 AND 222);
> ```
> **Both must equal 16.** ⚠️ **Two separate reads can straddle a writer: a proposal inserted between them leaves one reading 16 and the other reading all sixteen targets `proposed` — BOTH PASS while the set is seventeen.** Also deposit the raw `SELECT id … WHERE status='proposed' ORDER BY id`. **HALT on any seventeenth row.**
>
> ⚠️ **This licenses B2's flat status assertion and the absence of bystander machinery.**
>
> **HALT on genuine drift.** ⚠️ **A disagreement means the disposition table describes a corpus that no longer exists — the CEO's decision was made against that table.**
>
> ### Task A0-snap — THE FIVE BEFORE-SNAPSHOTS + THE DOCTRINE PINS
>
> Each on its OWN labelled line:
> 1. full status distribution
> 2. **TOTAL** route-NOT-NULL count
> 3. `get_unclassified_entries(conn)` (authoring `[]`) ⚠️ **open read-only: `sqlite3.connect("file:<abs>?mode=ro", uri=True)`. A bare `sqlite3.connect(<path>)` opens PRODUCTION READ-WRITE.**
> 4. **OUTSIDE-RANGE** route-NOT-NULL count
> 4b. ⚠️⚠️ **OUTSIDE-RANGE ROW IMAGE** — `SELECT id||':'||route … WHERE route IS NOT NULL AND id NOT BETWEEN 207 AND 222 ORDER BY id`, RAW (**76 rows at authoring**). **The only detector of a foreign route VALUE change (C2)** — seven such rows exist (**140, 141, 146, 161, 164, 169, 183**).
> 5. ⚠️⚠️ **THE THREE DOCTRINE PINS — THIS CAPTURE IS THE PRE-GATE OPERAND (C13/C14).** ⚠️ **The parent's absolutist "the only place they are ever measured" (`296:283`) belongs to its CITE model, which this plan DELIBERATELY REVERSES: QA row 7 re-measures live and compares against this capture.** `shasum -a 256` on `/Users/marklehn/Developer/GitHub/{DRAFTING_CYCLE.md,PLANNER_TEMPLATE.md,RULE_20_SELF_CHECK_BLOCK.md}` by absolute root path, raw output. **QA row 7 RE-MEASURES live and compares against this capture** — this capture is the pre-gate operand, not the answer. ⚠️⚠️ **COUNT THE OUTPUT LINES AND HALT UNLESS ALL THREE ARE PRESENT with the expected filenames** — a stub carrying blank or partial pins is worse than one carrying none, because it hands QA row 7 an operand that looks present (`296:283`). Confirm each matches the CEO Context pin **by 12-hex prefix**; a differing prefix means doctrine drifted between authoring and execution → ⚠️⚠️ **HALT, report, and do NOT proceed to Task A.** The baseline rule governs (*a mismatch is a HALT, not an adjustment*); an earlier draft merely "noted" this drift while letting the sixteen writes proceed.
>
> ⚠️ **Items (2) and (4) both read 76 pre-write and are DIFFERENT MEASUREMENTS. Report separately.** After the write: (2) → 92, (4) stays 76. **Report ACTUALS. Do NOT re-read "before" after Task A.**
>
> ⚠️⚠️ **IF *k* > 0 THIS IS A RESUME.** Item (2) reads **76+k**; item (4) still 76. Label the block `resume — snapshot taken post-partial-write`, state k, and **do NOT treat the delta as premise drift.** ⚠️ **On a resume the vacuity question is decided at A0-dep, NOT here — this task runs BEFORE the branch is knowable.** If A0-dep reconstructs the anchor from `$BK`, rows 4(b) and 5 are genuinely verified against it; **only if no candidate qualifies** do they compare the corpus against an anchor drawn from itself — they do not break, they become VACUOUS. **A0-dep decides; Receipt item 0b declares.**
>
> ### ⚠️⚠️ Task A0-dep — DEPOSIT THE PRE-WRITE SNAPSHOT, BEFORE ANY MUTATION (C11)
>
> **Write `knowledge/development/gate-1-route-207-222-prewrite-2026-08-03.md` and COMMIT IT NOW**, carrying: the set-identity single-statement output and the raw `proposed` id list; `k=<n>` **and the in-range row image**; before-items (1)–(4), **(4b)** and **(5) the three pins**, each RAW; and `$BK` with its three verification results.
>
> ⚠️ **WHY THIS IS ITS OWN TASK AND ITS OWN COMMIT.** A crash anywhere between Task A and the final deposit would otherwise destroy the before-image, which exists nowhere else in the running process. **The irreplaceable data is made durable before anything is mutated.** ⚠️ **C3 is satisfied: A0-iso has already identified this tree, so this is not a pre-confirmation write.**
>
> **⚠️⚠️ ON A RESUME (`k` > 0) THERE IS EXACTLY ONE RECOVERY SOURCE — `$BK`. DO NOT LOOK FOR A SURVIVING DEPOSIT.**
>
> Take before-items **(1), (3), (4) and (4b)** from a surviving backup under this plan's id prefix whose **`k` < 16**, and label them `reconstructed from <path>`. Selection, in order:
> 1. `ls -la` every candidate; **DISCARD any of size 0** before opening it. ⚠️ **[MEASURED] `?immutable=1` on a nonexistent path returns `ok` with exit 0 AND CREATES a 0-byte file; on a 0-byte candidate the `SELECT` errors with empty stdout, which a numeric comparison reads as "not < 16".**
> 2. For each survivor run `SELECT COUNT(*) FROM lesson_proposals WHERE id BETWEEN 207 AND 222 AND route='codify'` through **`?immutable=1`**. ⚠️⚠️ **SIZE CANNOT DISCRIMINATE — [MEASURED] pre-write and post-write backups of this corpus are BOTH 999424 bytes**, because this plan writes only `route` on sixteen existing rows. **`k` is the only discriminator** ([MEASURED] pre-write → 0, post-write → 16).
> 3. **Every candidate returning `< 16` is a valid pre-write anchor; if several do they are EQUIVALENT for items (1),(3),(4),(4b) — take any and NAME it.** ⚠️ **Only if NO survivor returns `< 16` is the anchor unrecoverable**, and item 0b then declares those items not independently verified.
>
> ⚠️⚠️ **ITEMS (1),(3),(4),(4b) ARE `route`-INVARIANT, so their agreeing with a candidate is NOT evidence that candidate is pre-write — only the `k` discriminator establishes that.**
>
> ⚠️⚠️ **WHY `$BK` AND NOT A SURVIVING DEPOSIT — this replaces a four-branch design that an ACID pass showed was unsound.** Every dispatch calls `_create_worktree`, which preserves a stranded worktree's HEAD onto `bellows-preserved/<slug>-<ts>` and re-creates the worktree **from main**; teardown-to-main happens only at a COMPLETED step boundary. **So after a mid-step death the prior deposit is on a preservation branch — in neither the new worktree nor main.** `$BK` is written to the main tree by absolute path and is the ONLY unconditionally durable artifact this step produces. **One recovery source, one selection rule, no precedence order to get wrong.**
>
> **Write the same deposit path on every branch, and commit by explicit pathspec. Then, and only then, Task A.**
>
> ### Task A — record the sixteen routes
>
> `set_proposal_route(conn, proposal_id, 'codify')` from `src.lessons_forge` (NOT hand-written SQL) for **207 … 222**. **No status is written.** Then a **SINGLE `conn.commit()`**.
>
> ⚠️⚠️ **ASSERT ON `conn.total_changes` PER CALL (C6/C12).** Read before, call, read after, print `id, before, after, delta`.
>
> **[EXECUTED HERE — 2026-08-03] MEASURED SEMANTICS — why the expectation is flat:**
> ```
> NULL -> codify (real change)      delta=1   rowcount=1
> codify -> codify (NO-OP)          delta=1   rowcount=1
> nonexistent id (SILENT no-op)     delta=0   rowcount=0
> ```
> **SQLite counts rows MATCHED, not rows DIFFERING.**
>
> ⚠️⚠️ **EXPECT SIXTEEN NON-ZERO DELTAS ON EVERY RUN, RESUME OR NOT. ANY DELTA OF 0 IS A HALT** — it means the id does not exist, the silent no-op this guard exists to catch. ⚠️ **An earlier draft wrote "on a resume a row already `codify` yields delta 0" and scaled the expectation to `16 − k`; the premise was false and the tolerance would have swallowed up to k missing ids. *k* does not enter this check.**
>
> **Print all sixteen lines.** A loop printing only a total is indistinguishable from one that wrote nothing.
>
> ### ⚠️ TASKS B AND C ARE READ-ONLY AND MUTUALLY INDEPENDENT — RUN ALL BEFORE HALTING ON ANY ONE
>
> **The write has already happened**, so an early halt does not protect the corpus — it only decides how much the CEO knows about a corpus already changed. **Run every check, record every value, THEN halt and report together.**
>
> ⚠️ **AND DO NOT REPAIR ANYTHING YOU FIND — report it, do not fix it.** This is the one step holding a read-WRITE handle. **Do not re-run `set_proposal_route`, do not hand-write corrective SQL, do not restore from the backup, do not "tidy" a value so the next check passes.** **The restore point exists for the CEO's decision, not for yours.**
>
> **Task B.**
> - **B1** — `SELECT id, entry_id, status, route, category, confidence, target_layer, target_artifact, status_updated_by, status_updated_at FROM lesson_proposals WHERE id BETWEEN 207 AND 222 ORDER BY id`. Each `route='codify'`, `status='proposed'`, category/confidence/target_artifact unchanged from A0-pre. **Absolute — no before-anchor.** ⚠️ **The ONLY observation of the write's effect; A0-pre proves the rows existed, only B1 proves the write landed.** ⚠️ **Do NOT write `route_readback.txt` here — it belongs to Step 2's evidence directory, which is not in this step's Scope. Report this output as Receipt item 6; QA row 1 re-measures independently and writes the evidence file itself.**
> - **B2** — status distribution **byte-identical to before-item (1)**. ⚠️ **Licensed by the set-identity assertion, not inherited.** ⚠️⚠️ **THIS IS AN UNSCOPED WHOLE-CORPUS PREDICATE (C18). Its window is intra-step (A0-pre → here), so a foreign insert is unlikely but not impossible: if it fails while row-1-equivalent per-row checks pass, report it as a PRECONDITION-1 VIOLATION (a concurrent cycle), not as a defect in this write.**
> - **B2b** — **`status_updated_by IS NULL AND status_updated_at IS NULL` on all sixteen (C4).** **[EXECUTED HERE]** `set_proposal_route` touches neither; the module's only writer is the staling path (`:189`, `'auto'`). **Positive proof Gate 1 wrote `route` ONLY.**
>
> **Task C.**
> - **C-b(ii)** — **ROW IMAGE byte-identical to before-item (4b).** ⚠️⚠️ **A COUNT cannot see a route VALUE change; seven such rows exist (140, 141, 146, 161, 164, 169, 183). C-b(ii) is the only detector (Ledger C2).**
> - ⚠️⚠️ **A MISMATCH HAS TWO CAUSES AND YOU MUST NAME BOTH.** **(i)** this plan wrote outside its range; **(ii)** **a third party wrote during the verdict gate** — an arbitrary amount of wall-clock time, and a cycle inside a gate is normal here (291, 296). **The remedies differ.** **Deposit the DIFF; the differing lines are the discriminator.**
> - **C-c** — `get_unclassified_entries(conn)` unchanged from before-item (3), read-only handle.
>
> ⚠️ **This capture is mandated at BOTH C-b and QA row 4.** ⚠️ **Task-C check labels are `C-b(ii)`/`C-c` — the Conflict Ledger owns `C1`…`C18`, and an earlier draft used `C1(b)` for both.** `pause_for_verdict: always` means a C1 halt reaches the CEO **before Step 2 runs** — the mutating step's halt path is where a bare integer is least useful. **Checklist #26: weight the sweep toward the step that MUTATES.** ⚠️ **A Task C-b halt reaches the CEO before Step 2 ever runs, which is why its on-mismatch diff is mandated here and not only at QA row 4.**
>
> ### ⚠️⚠️ HALT DURABILITY — TWO HALVES
>
> ⚠️⚠️ **BOTH HALVES: mark any Receipt item you could not reach as `NOT CAPTURED — halted at <task>` rather than omitting it, and QA row 0(iv) treats a `NOT CAPTURED` marker on a `Status: Partial` receipt as SATISFIED — a legitimate pre-write halt has no k, no item 6 and no item 9, and must not manufacture a Critical.**
>
> **(1) A PRE-WRITE HALT DEPOSITS A NOTE AND COMMITS IT — *EXCEPT* WHEN THE TREE IS UNCONFIRMED, WHERE IT WRITES NOTHING (C3).**
> - **UNCONFIRMED** — A00 derived zero matches, **or two**, or A0-iso found your file absent → **write nothing, commit nothing, halt and report. The gate failure IS the signal and it is correct.** ⚠️ **A00's two-match halt is UNCONFIRMED: it runs before A0-iso and asserts only that one lifecycle file exists, not that it is YOURS.**
> - ⚠️⚠️ **THE HALT NOTE *IS* THE DEV-LOG DEPOSIT — `knowledge/development/gate-1-route-207-222-captures-2026-08-03.md`. Create NO other file:** Step 1 declares exactly two deposits, and an invented `halt-note.md` is an undeclared write that fires `_gate_scope_check`.
> - **CONFIRMED** — A0-pre/A0-snap found drift → **deposit the note (at that path) and commit it**, naming: which guard fired; measured vs expected; **NO DB WRITE occurred**; `#### Files Created or Modified`; **`$BK` and its verification IF A00 ran** — ⚠️ **a halt at A0-iso/A0-pre/A0-snap is AFTER A00 wrote a real restore point, so "no restore point exists" is FALSE there**; and `Status: Partial — HALTED at <task>, <reason>` opening the Receipt.
> - ⚠️⚠️ **AND THE THIRD CLASS: A0-dep FAILING, OR TASK A's OWN `delta=0` HALT.** A0-iso has run on both, so the tree is CONFIRMED — **deposit the note and commit it.** ⚠️⚠️ **A00's VERIFICATION FAILING IS *NOT* IN THIS CLASS — it is UNCONFIRMED, because A00 PRECEDES A0-iso (C3, and A00's own "any failure → HALT before any write"). Write nothing, commit nothing.** ⚠️ **Receipt item 8 lists TWO files only where A0-dep already COMMITTED (the `delta=0` case); on an A0-dep failure it lists ONE.** ⚠️⚠️ **AND IF YOU ARE INSIDE TASK A: CLOSE THE CONNECTION WITHOUT COMMITTING.** **[MEASURED]** the sixteen writes sit in one implicit transaction, so closing without `commit()` rolls back every one — **but STATE IN THE RECEIPT WHETHER YOU ROLLED BACK**, because that is the single fact the CEO needs to choose between re-dispatch and restoring from `$BK`, and "death rolls it back" is a claim about a crash, not about a graceful halt. 
>
> **(2) A HALT AFTER TASK A's `conn.commit()` MUST STILL DEPOSIT AND COMMIT THE DEV-LOG.** ⚠️ **The before-image is already safe — A0-dep committed it pre-mutation (C11).** Still owed: the read-backs completed, which task halted and why, and the after-values reached. ⚠️ **Mark unreached items `NOT CAPTURED — halted at <task>`, and mark item 6 PER SUB-CHECK** — it spans FIVE (B1/B2/B2b + C-b(ii)/C-c), and one blanket marker across them would either discard read-backs you produced or claim ones you did not. ⚠️ **If the prewrite deposit is missing, the before-items are still recoverable from `$BK` with `?immutable=1` — say so rather than marking them lost.**
>
> ### The Output Receipt (in the dev-log)
>
> **OPENS with a status line from this CLOSED SET:** `Status: Complete` · `Status: Partial — HALTED at <task>, <reason>`. **The first is the only proceed-value. A halted status is legitimate — do NOT write `Complete` to look tidy.**
>
> 0. **SET-IDENTITY** — the single-statement output AND the raw `proposed` id list, pre-write. **Reader: QA row 0(iv).**
> 0b. **RESUME DECLARATION** — three fields: `RESUME: yes/no`; **`k`** as measured at A0-pre; and **`ANCHOR: reconstructed from <backup path> | UNRECOVERABLE`**. ⚠️⚠️ **DO NOT ask whether a prior deposit "survived" — under A0-dep's single-source rule it never does; the anchor is always a `.db`, never a markdown file.** **Only on `ANCHOR: UNRECOVERABLE`** write the verbatim sentence **"before-items (3) and (4b) are POST-WRITE; rows 4(b) and 5 are NOT independently verified on this run."** ⚠️ **On a successful reconstruction those two rows ARE genuinely verified — say so, and do NOT emit that sentence.** **Producer: A0-pre and A0-dep. Reader: the clause above Step 2's Verification Table (C9).**
> 1–4b. before-items **(1)–(4)** and **(4b)**, RAW; **cite the prewrite file by path.** ⚠️⚠️ **ITEMS (2) AND (4) ARE REPORTED CONTEXT — no QA row adjudicates on them. They are carried so the CEO can read the rise and the outside-range figure at the verdict gate, and that is their named reader (C9).** Items (1), (3) and (4b) retain adjudicating readers: B2, row 5, and row 4(b).
> 5. **the three doctrine pins**, RAW. **Reader: QA row 7, which re-measures live and compares against this capture (C14).** ⚠️ **This item is the PRE-GATE operand — a committed doctrine edit during the verdict gate is invisible to `porcelain` and detectable only by that comparison.**
> 6. after-values for **B1 / B2 / B2b** and **C-b(ii) / C-c**, each labelled with its anchor: B2 → item (1); B2b → absolute; C-b(ii) → item **(4b)**; C-c → item (3). **B1 is ABSOLUTE — label it so.** **Reader: QA row 0(iv)** — a Step 1 that skipped Tasks B and C entirely and happened to write correctly would otherwise close clean. 
> 7. `$BK` **plus its three verification results**, RAW.
> 8. **`#### Files Created or Modified`** — every **git-tracked** file this step wrote, **project-relative**: **two on a completed run** (the prewrite deposit and the dev-log); **one on a halt BEFORE A0-dep committed** (the halt note only); **two on a halt at or after A0-dep** (the prewrite deposit and the note); **this item is not written at all on an UNCONFIRMED halt**, which writes nothing. ⚠️⚠️ **Do NOT list `$BK` or the canonical DB.** `.gitignore` matches `*.db`, so porcelain is empty (passes) while `git log -1` is empty (fails row 0's "exists AND is committed") — a literal reading manufactures a Critical on a clean run. ⚠️ **`$BK` is therefore a file this step writes that is deliberately absent from `**Deposits:**` (Checklist #2 / Rule 26): its path is timestamp-derived and it is gitignored, so it is neither declarable nor gate-visible. Recorded at item 7 instead.** ⚠️ Rule 17's literal string is `Files Created or Modified (Code)`; **the `(Code)` suffix is deliberately dropped** — this plan's deliverables are markdown and a DB mutation, not code. **Declared so it is not read as an error.**
> 9. any flags **or HALT conditions encountered**, including one hit and cleared. **Reader: QA row 0(iv).**
> 10. **(STEP 2's Receipt carries this item; Step 1 does not)** an explicit statement that the report was created with the `Write` tool and that `### Ledger Updates` was authored in EXACTLY ONE `Write`/`Edit`, complete, spanning through `#### Prompt Feedback`, and NEVER re-edited. ⚠️ **This is the only observation of obligation (a), which `fwcheck.py` structurally cannot see. Reader: QA row 0(v).**
>
> ⚠️ **Every measured value is RAW COMMAND OUTPUT.** Annotate freely; the annotation accompanies the raw output, never replaces it.
>
> **Deposits:**
> - `knowledge/development/gate-1-route-207-222-prewrite-2026-08-03.md`
> - `knowledge/development/gate-1-route-207-222-captures-2026-08-03.md`
> Canonical Python file-write — no heredoc. Commit by explicit pathspec. ⚠️⚠️ **BUT `### Ledger Updates` ITSELF MUST BE AUTHORED VIA THE `Write`/`Edit` TOOL, EXACTLY ONCE AND COMPLETE, ENDING WITH A BLANK LINE AFTER ITS LAST SUBSECTION'S CONTENT** — ⚠️ **[MEASURED] a subsection left flush against the end of the Edit absorbs the next chat part into the parsed value; the exposed one is always the LAST subsection** — the daemon parses `_all_assistant_text`, which captures assistant text plus `Write` content plus `Edit` strings and **NOT Bash**, so a ledger block written by a Python file-write is invisible to the channel (Mode 4 in Step 2's list — the transcript-source mode; it governs this step identically). `#### Prompt Feedback` in `### Ledger Updates`.

---
---

## STEP 2 — QA

---

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting this step.** **Do NOT move this plan to `Done/`** (Rule 8).
>
> **Scope:**
> - `knowledge/qa/gate1-207-222-qa-report-2026-08-03.md`
> - `knowledge/qa/evidence/gate1-207-222-2026-08-03/`
>
> Read Step 1's dev-log.
>
> ⚠️⚠️ **IF ITS RECEIPT OPENS `Status: Partial — HALTED`: "stop" does NOT mean "write nothing."** `pause_for_verdict: always` means the CEO has already seen the halt and authorised this step to obtain a record. **Produce and commit the QA report anyway**, run every row you CAN run for real against live state, mark genuinely unreachable rows `❌` with the halt reason, and **still emit the `#### Forward Register` block** — the Forward Register obligation (`PLANNER_TEMPLATE.md:372-376`, Rule 44) is owed on exactly the run where the record matters most. **Do not mark every row `❌` wholesale; that puts false statements in the CEO's report.**
>
> ⚠️⚠️ **READ RECEIPT ITEM 0b FIRST — ADJUDICATE ON ITS `ANCHOR:` FIELD, NOT ON ANY "survived" LANGUAGE.** `ANCHOR: reconstructed from <path>` → rows 4(b) and 5 adjudicate NORMALLY against the reconstructed before-items. `ANCHOR: UNRECOVERABLE` → mark those two `❌`, with `unverifiable — resume, anchor not recoverable` in Evidence. ⚠️ **If item 0b is MISSING ENTIRELY, treat it as an undeclared resume and mark those two `❌`** — its absence is not evidence of a fresh run.
>
> **Re-measure everything independently from the live DB.** ⚠️ **Do NOT copy Step 1's numbers forward.**
>
> ⚠️⚠️ **EVIDENCE-SOURCE CONTRACT — every SQL row states which DB it ran against, and the canonical DB is ONLY ever this literal absolute URI:**
> ```
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"
> ```
> ⚠️ **DECOY DATABASES: `lessons-forge/` itself contains `forge.db`, `lessons.db` and `lifecycle.db` beside the canonical file, and `forge/forge.db` is a different real DB. A bare `sqlite3.connect(<relative>)` SILENTLY CREATES a new empty file.** ⚠️⚠️ **The canonical DB does NOT exist in your worktree — its absence there is NEVER a substitution reason (Checklist #28(b)). If you cannot reach the absolute path, HALT; do not fall back to anything local.** ⚠️ **If `?mode=ro` errors 14 on the LIVE DB (absent WAL sidecars — not observed at authoring, `journal_mode=wal` with both sidecars present), retry ONCE with the plain absolute path and RECORD that you did; do NOT use `?immutable=1` on the live DB.** ⚠️ **Read-only handle: `sqlite3.connect("file:<abs>?mode=ro", uri=True)`. A bare `sqlite3.connect(<path>)` opens PRODUCTION READ-WRITE — and this step declares NO DB WRITES.** ⚠️ **The `?immutable=1` rule is for BACKUP artifacts only; do not apply it to the live DB.**
>
> ⚠️⚠️ **COMMAND DISCIPLINE (C8):** `;` never `&&`; capture meaning-bearing exit codes; **`grep -F` mandatory for every literal** — a `**`-bearing pattern without `-F` is a regex error printing NOTHING to stdout, which reads as PASS. ⚠️ **Row 0 searches Receipt labels that ARE `**`-bearing.** ⚠️ **Never pipe to `head` — it masks the exit code.** ⚠️ **Prove any anchor unique before relying on it: `grep -Fc '<anchor>' <file>` must return 1, and RECORD the count.**
>
> ⚠️ **RUN EVERY ROW BEFORE HALTING ON ANY ONE.** The rows are mutually independent and read-only; a row-1 failure must not abort the table.
>
> ⚠️ **The verification table MUST sit under a top-level `## ` heading containing "Verification"** — write exactly `## Verification Table`, columns **`| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |`** (Rule 17 `:555` fixes that spelling; Rule 18 mandates the Evidence column citing the evidence file BY PATH). `gates.py:657` tracks sections via `startswith("## ")` only.
>
> ⚠️⚠️ **THE SECTION NEVER CLOSES — close it yourself.** `in_verification_section` is never cleared by `###`/`####`. **Immediately after the table write exactly `## Evidence and Narrative`**, and keep the Rule 20 stdout, Output Receipt and `### Ledger Updates` under `## `-level headings.
>
> ⚠️ **USE ONLY `✅` OR `❌` — no third value. THE STATUS CELL HOLDS EXACTLY ONE GLYPH AND NOTHING ELSE; ANY ANNOTATION GOES IN THE EVIDENCE COLUMN.** ⚠️⚠️ **An earlier draft mandated `❌ (unverifiable)` in three places — an ANNOTATED cell, which is the very defect proposal 211 (routed by this plan) describes, and which is mechanically survivable only because `gates.py:687` happens to test `❌` by substring. That is a property this plan should not depend on: write `❌`, and put `unverifiable — <reason>` in Evidence.** ⚠️⚠️ **AND KNOW WHAT AN `❌` COSTS: any `❌` row fires `rule_22(c)` (`gates.py:687`) and pauses the step. On the resume-unverifiable branch, the halt branch, and an absent-Receipt-item branch, that gate failure is EXPECTED AND BENIGN — state so explicitly in the Receipt so the verdict gate reads it as the signal this plan intends, not as a defect.** ⚠️ **This plan routes 211 and 219, which exist because of this defect — but state it correctly: `is_positive_row` (`RULE_20_SELF_CHECK_BLOCK.md:67`) matches the TEXT tokens (`OK`/`PASS`/`done`/`complete`/`verified`) by CELL EQUALITY, while `✅` is matched by SUBSTRING. So an annotated ✅ cell IS a positive row and IS hedging-scanned; an annotated TEXT-token cell is neither positive nor failing and BOTH gates ignore it.** **A row whose honest disposition is a note belongs under `## Evidence and Narrative`.**
>
> ⚠️ **Rule 19 — a `✅` row whose Evidence column contains any of "pending", "inferred", "extrapolated", "estimated", "approximate", "skipped", "assumed", "close enough", "should pass", "would pass", "not run" is AUTOMATICALLY INVALID.** ⚠️⚠️ **The Rule 20 hedging scan is whole-line substring over every `|`-BEARING POSITIVE-STATUS TABLE ROW** (`is_positive_row` returns False when the line has no `|`), **so a hedging keyword is fatal even as a MEASURED VALUE inside such a row — write row 9's value as `<N> passed` and nothing else.**
>
> ⚠️ **No command containing a `|` goes in a table cell** (proposal 220): put it in a fenced block above the table and have the row cite its result. **Escaping to `\|` turns ERE alternation into a literal and matches nothing — silently.**
>
> ### Verification Table

> ⚠️⚠️ **ROW NUMBERS 2, 3 AND 6 ARE VACANT BY DESIGN** — those checks were deleted as implied by rows 1 and 4(b). **DO NOT RENUMBER:** Step 1's Receipt, this step's preamble, the Rule 18 rationale and the forensic signature all cite the surviving numbers by name.

>
> 0. **Deliverable verification (Rule 17, before the regression check).** Scope is BOTH sets: **(i)** every file Step 1's Receipt item 8 lists; **(ii)** this step's own mandated blocks — **the verification table, `## Evidence and Narrative`, the Rule 20 stdout, the Output Receipt, and `### Ledger Updates`.** ⚠️ **Enumerated because an earlier draft named set (B) and never said what was in it.** Verify **EVERY** listed deliverable — **not sampling**: exists on disk **AND** committed in its CURRENT state — `git log --oneline -1 -- <path>` **AND** `git status --porcelain -- <path>` (must be EMPTY). ⚠️⚠️ **USE THE PATH AS THE RECEIPT DECLARES IT — project-relative. If a path arrives root-joined (`lessons-forge/…`), STRIP the prefix before both commands: from inside the submodule both return empty with exit 0 on a root-joined path, so `git log` reads "never committed" → false Critical while porcelain reads PASS.** ⚠️⚠️ **AN EMPTY `git log` ON A CORRECTLY-STRIPPED PATH HAS A SECOND CAUSE: Step 1's worktree teardown FAILED, leaving its commits on `bellows-wt/<slug>` or `bellows-preserved/<slug>-*` while the plan was still renamed to await your verdict. RUN `git branch --list 'bellows-*'; echo "BRANCH-EXIT=$?"` BEFORE RECORDING A CRITICAL** ⚠️⚠️ **AND KNOW WHAT THE TWO OUTPUTS LOOK LIKE, BECAUSE THEY DIFFER ONLY BY CONTENT: run `git rev-parse --abbrev-ref HEAD` FIRST and name your own branch; ONE line matching it is the CLEAN result. ⚠️ **`git branch --list` exits 0 on zero matches, so its exit code carries no information — adjudicate on the CONTENT.** The signal is a branch OTHER than your own — a second `bellows-wt/*` or any `bellows-preserved/*`. Then assert positively: `git log --oneline -1 <that branch> -- <path>` must show Step 1's commit.** — a merge conflict or dirty-tree overlap at teardown turns a correct Step 1 into a false Critical here.
>    - **(iii)** `$BK` from Receipt item 7 exists and its verification is recorded. ⚠️ **Not git-tracked — do not apply the commit test.**
>    - **(iv)** Receipt items **0**, **0b**, **1**–**4b**, **5**, **6**, **8** and **9** are present and populated. ⚠️ **On a `Status: Partial` receipt a `NOT CAPTURED — halted at <task>` marker COUNTS AS SATISFIED for this clause** — a legitimate pre-write halt has no `k`, no item 6 and no item 9, and must not manufacture a Critical. ⚠️⚠️ **Item 8 is in this set because row 0(A) is DEFINED as "every file item 8 lists": an absent item 8 hands row 0(A) an empty list, which it verifies vacuously and passes** (Rule 55 — assert a positive signal, never merely empty output).
>    - **(v)** the Forward Register block passes the mechanical check below, **AND this step's Receipt item 10 is present and populated** — item 10 is the only observation of obligation (a), which `fwcheck.py` structurally cannot see.
>    ⚠️⚠️ **AND MEASURE THE TWO REPORTED FIGURES — they have no other producer.** Under `## Evidence and Narrative` record (a) the corpus-wide **raw `SELECT id … WHERE status='proposed' ORDER BY id` LIST** now versus Receipt item 0's captured list — ⚠️⚠️ **the LIST, not a count: a count cannot see a compensating insert-plus-stale, and "a count is not a value guard" is entry 199, which this plan routes as proposal 207.** Item 0 already carries the list, so this costs no new query, and (b) the total `route IS NOT NULL` now versus Receipt item (2). **Both are REPORTED, not adjudicated — no row fails on them; they are the CEO's in-gate signal for precondition 1. (C18: both are whole-corpus predicates, and both are anchored to a captured before-value rather than an authoring literal, which is what C18 requires.)** ⚠️ **An earlier draft promised these under Evidence and Narrative after deleting the only row that produced them.**
>    ⚠️ **RECORD IN RULE 17's MANDATED FORM** — row 0 in the main table, evidence under `## Evidence and Narrative` as a `| Deliverable | Expected | Status (✅/❌) | Evidence |` sub-table, ONE ROW PER FILE. ⚠️ Keep those cells short and free of hedging keywords — it is `|`-bearing prose outside the verification section.
> 1. **The sixteen-row image** — `SELECT id, entry_id, status, route, category, confidence, target_layer, target_artifact, status_updated_by, status_updated_at …` — all `route='codify'`, all `status='proposed'`, **`confidence='high'` and `target_layer='governance'` on all sixteen** (⚠️ **stated here inline — the disposition table has NO `confidence` or `target_layer` column, so "per the disposition table" cannot source them**), and category/target_artifact per the disposition table **per row**, **and both audit columns NULL**. ⚠️ **The audit columns are selected HERE and adjudicated HERE.** **Set comparison. Absolute.** ⚠️ **THIS ROW is the producer of `route_readback.txt`** — write your own raw read-back there (C9); do not copy Step 1's.
> 4. **Blast radius.** **4(b)** — the outside-range **ROW IMAGE byte-identical to before-item (4b)**. ⚠️⚠️ **4(a), the count, is the LINE COUNT OF 4(b)'s OWN OUTPUT — not a separate `SELECT`.** Two separate reads can straddle an in-gate insert, leaving a count that corroborates a *different instant* than the image; **a corroborator of another instant is worse than none.** Deriving it removes the window at zero cost. ⚠️ **(a) cannot see a foreign row moving between two non-NULL routes (140, 141, 146, 161, 164, 169, 183); (b) is the only detector.** **Deposit both images RAW to `outside_range_image.txt`.** ⚠️ **If Receipt item (4b) is absent, mark this row `❌` with `unverifiable — Receipt item (4b) absent` in Evidence — fail-closed; it is the plan's only value-level detector and has no substitute.** ⚠️ **On a mismatch DIFF the images, deposit the differing lines RAW, and NAME BOTH CAUSES** — this plan writing out of range, or a third party writing during the verdict gate.
> 5. **`get_unclassified_entries`** unchanged from before-item (3), read-only handle. **Deposit both values RAW to `unclassified.txt`.** ⚠️ **If Receipt item (3) is absent, mark this row `❌` with `unverifiable — Receipt item (3) absent` in Evidence — fail-closed; do not substitute a fresh reading as though it were the anchor.**
> 7. ⚠️⚠️ **THE THREE DOCTRINE FILES ARE UNCHANGED (C13).** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- DRAFTING_CYCLE.md PLANNER_TEMPLATE.md RULE_20_SELF_CHECK_BLOCK.md; echo "PORCELAIN-EXIT=$?"` must be **EMPTY**, **and** you must **RE-MEASURE LIVE NOW, BY ABSOLUTE ROOT PATH** — `shasum -a 256 /Users/marklehn/Developer/GitHub/{DRAFTING_CYCLE.md,PLANNER_TEMPLATE.md,RULE_20_SELF_CHECK_BLOCK.md}`. ⚠️ **[EXECUTED HERE — 2026-08-03] You are running from the lessons-forge worktree, where these three files DO NOT EXIST — a bare filename gives `SHA-EXIT=1` and zero usable lines on a clean run.** ⚠️⚠️ **DO NOT QUOTE THE BRACED PATH — quoting suppresses brace expansion and yields ZERO stdout lines with exit 1.** ⚠️⚠️ **CAPTURE THE EXIT CODE AND COUNT THE LINES: `shasum -a 256 /Users/marklehn/Developer/GitHub/{DRAFTING_CYCLE.md,PLANNER_TEMPLATE.md,RULE_20_SELF_CHECK_BLOCK.md}; echo "SHA-EXIT=$?"` — FEWER THAN THREE LINES IS `❌`, not a partial pass.** A partial `shasum` prints the found hashes and drops the missing one silently, leaving porcelain — which is empty and exit 0 on a clean tree — as the only surviving guard, the exact collapse this row exists to prevent and compare against Receipt item 5. Print BOTH triples and the three pairwise verdicts, **RAW into `doctrine_pins.txt`**. ⚠️⚠️ **DO NOT 'cite' item 5 as the comparison — an earlier draft did, which compared item 5 to itself and left porcelain as the only guard. [EXECUTED HERE — 2026-08-03] `porcelain` is EMPTY and exit 0 on a clean tree, so a COMMITTED doctrine edit during the arbitrarily-long verdict gate passes it and is caught ONLY by the live pin.** ⚠️ **A non-zero exit from either command is a HALT — a mistyped `-C` exits 128 with empty stdout, which reads as PASS.**
>    ⚠️⚠️ **IF RECEIPT ITEM 5 IS ABSENT, OR CARRIES FEWER THAN THREE PINS, THIS ROW IS `❌` with `unverifiable — Receipt item 5 absent or partial` in Evidence — fail-closed. Porcelain alone does NOT satisfy it**, for the reason stated above. ⚠️ **THIS ROW IS THE ONLY GUARD. `_gate_scope_check` is cwd-scoped and submodule-blind, so a root doctrine edit from this submodule-dispatched plan is invisible to every gate.** ⚠️ **`291:83`: routing plans (282/283/284/289 — and this one) pin doctrine UNCHANGED, absolutist, because a routing plan must not touch doctrine.** Only a plan editing doctrine by design uses the weaker "changed only in the intended ways" form — **do not import 291's variant; it is licensed by edits this plan does not make.** ⚠️ **This batch's Gate 2 targets all three files and Step 2 copies the canonical block out of one of them, so the exposure is HIGHER here than in the parent, not lower.** ⚠️⚠️ **A MISMATCH HERE HAS THE SAME TWO CAUSES AS ROW 4 AND YOU MUST NAME BOTH: (i) this plan touched doctrine, a Scope violation; (ii) an in-gate Gate 2 landed its doctrine commits and died before the flip — `291:428` shows Gate 2 commits every doc edit BEFORE touching the DB, which is precisely why this row is precondition 2's only detector. The remedies differ.**
> 8. **`src/` untouched — BY A POSITIVE SIGNAL, NOT BY EMPTY OUTPUT.** `git -C /Users/marklehn/Developer/GitHub/lessons-forge log -5 --format='%H %cI %s' -- src/; echo "SRCLOG-EXIT=$?"` and confirm the newest commit's timestamp PREDATES **this plan's own Step-1 commit**, obtained as `git -C /Users/marklehn/Developer/GitHub/lessons-forge log -1 --format=%cI -- knowledge/development/gate-1-route-207-222-captures-2026-08-03.md` ⚠️ **`--oneline` prints NO date and cannot answer this row — name the reference instant and print timestamps, or the post-condition is unanswerable from the mandated command**; then `git -C … status --porcelain -- src/; echo "SRCPORC-EXIT=$?"` EMPTY. ⚠️⚠️ **Porcelain ALONE cannot see a COMMITTED `src/` edit — Step 2 runs in a fresh worktree created from main AFTER Step 1's commits merged, so a committed change reads as a clean tree. That is the identical defect row 7 diagnoses and fixes with a live pin; an earlier draft left this row with the diagnosis seven lines above it and no fix.** A non-zero exit from either command is a HALT. **Deposit both outputs RAW to `src_untouched.txt`** — this row executes and interprets two commands, which is exactly the Rule 18 trigger stated above.
> 9. **Targeted test run** — `python3 -m pytest src/test_lessons_forge.py -q`, raw output to `pytest_targeted.txt` in the evidence dir (**this row is its producer**; the Rule 20 block is its reader). Baseline **55 collected** at authoring. ⚠️ **Write the value as `<N> passed` and nothing else** (Rule 19). ⚠️ **The suite runs on `:memory:` and never opens the corpus — NOT evidence for any row above.**
>
> ### `### Ledger Updates` — and the mechanical Forward Register check
>
> ⚠️⚠️⚠️ **THE `#### Forward Register` BLOCK GOES INSIDE `### Ledger Updates`, THE HEADING APPEARS EXACTLY ONCE, THE BULLETS ARE CONTIGUOUS, AND EACH ITEM IS ONE PHYSICAL LINE (C7).**
>
> **This channel has failed FOUR distinct ways, numbered 1-4 here** (the session-16/17 modes — unconfigured destination and first-line-only truncation — are RESOLVED and are not restated).
> - **Mode 1 (session 18):** a correct block *outside* `### Ledger Updates` with a pointer stub inside. The daemon extracts in TWO stages — the `### Ledger Updates` body (`parser.py:55`), then the Forward Register regex against **that body only** (`:75`). 1 → 2 rows, **ZERO items.** The format was never the problem.
> - **Mode 2 [EXECUTED HERE]:** the inner capture is terminated by a lookahead including **`\n\s*\n`**. **A blank line between bullets truncates the block to its FIRST item.**
> - **Mode 3 [EXECUTED HERE]:** a **wrapped** item — the daemon's `sanitize_items` keeps only lines matching `BULLET_RE = ^(?:-\s|\d+\.\s)` (`bellows.py:1409`), so a continuation line is **never joined and never delivered**. Count in = count out = 5, and the row lands truncated mid-sentence.
> - **Mode 4 [EXECUTED HERE]:** ⚠️⚠️ **THE DAEMON DOES NOT PARSE YOUR FILE.** `parser.py:53` sources from `_all_assistant_text`, which the runner builds from assistant text blocks **plus `Write` tool content plus `Edit` replacement strings — and nothing else.** **A report written by a Python/Bash file-write is INVISIBLE to this channel** while every file-based check passes green. And `re.search` takes the **FIRST** match in the concatenation, so a drafted-then-edited block diverges from the shipped file.
>
> **THEREFORE, three obligations:**
> **(a)** Create the QA report with the **`Write` tool**, not a Python/Bash file-write. ⚠️⚠️ **AND WRITE `### Ledger Updates` EXACTLY ONCE, AUTHORED COMPLETE, AFTER EVERY OTHER SECTION IS FINAL.** `re.search` takes the **leftmost** match across the concatenated stream, so **an initial `Write` carrying a draft ledger block SHIPS THAT DRAFT** even though later `Edit`s fix the file — and `fwcheck.py`, reading the final file, reports PASS. ⚠️ **A trailing chat re-emission cannot rescue this: the report's `Write` content always precedes the final message in the stream, so the chat copy can never be the match.** ⚠️⚠️ **BUT SINGLE-AUTHORING IS NOT SUFFICIENT ON ITS OWN — VALIDATE BEFORE YOU AUTHOR.** Measured against the real parser: `Write` (no ledger) → `Edit` authoring the ledger with a wrapped bullet → `Edit` repairing the wrap ships the **PRE-REPAIR** block, while `fwcheck.py` on the final file reports `WRAP-CHECK=PASS`, a full `DAEMON-ROWS` count and exit 0 (measured at the five-item count this plan then reduced to four — the item count is immaterial to the mechanism). **Once a defective block is authored it is UNRECOVERABLE in-step** — re-authoring adds a second occurrence and the leftmost still wins. **THEREFORE: compose the block in a scratch file, run `fwcheck.py` against THAT, and author it into the report only once it exits 0.**
>
> ⚠️⚠️⚠️ **AND THE SCRATCH FILE MUST BE WRITTEN WITH A TRANSCRIPT-INVISIBLE TOOL — `Bash` heredoc or a Python file-write, NEVER `Write`/`Edit`. [MEASURED]** `runner.py:427-437` captures `Write` content and `Edit` new_string **with NO PATH FILTER**, so a `Write`-authored scratch enters `_all_assistant_text` exactly like the report — and because `fwcheck.py` requires the literal `### Ledger Updates` heading to exit 0, the scratch necessarily carries it. **The scratch draft then BECOMES the leftmost match, and "iterate until it exits 0" guarantees the FIRST, BROKEN draft is what ships.** Proven against the real parser: the report was perfect, `fwcheck` on it returned `WRAP-CHECK=PASS` / exit 0, and the daemon appended the truncated pre-fix row. ⚠️ **A sentinel heading is not an escape — `### Ledger Updates (SCRATCH)` fails `### Ledger Updates\s*\n` and fwcheck exits 1.**
>
> ⚠️ **The `Write`/`Edit`-ONLY restriction applies to authoring the block INTO THE REPORT — `runner.py` captures those two tool names and no others, so a `MultiEdit` of the report is invisible to the channel.**
> **(b)** Render the items as **`- ` bullets**, contiguous, **one physical line each, no wrapping**, and **put a BLANK LINE after the last bullet.** ⚠️⚠️⚠️ **AND THE SAME PROTECTION IS OWED TO EVERY `####` SUBSECTION, NOT JUST THIS ONE — THE LAST ONE IS THE EXPOSED ONE.** Write the subsections in the order **`#### Forward Register` → `#### Project Status` → `#### Prompt Feedback`**, and **END THE SINGLE `Write`/`Edit` WITH A BLANK LINE AFTER `#### Prompt Feedback`'s CONTENT.** ⚠️ **[MEASURED] `parser.py`'s feedback capture terminates on the same `\n\s*\n` lookahead, and `runner.py:462` joins assistant parts with a single `\n` — so a subsection left flush against the end of the Edit ABSORBS the next chat part.** Measured: an Edit ending flush captured *"…was clear.\nNow re-running fwcheck and the Rule 20 block…"* into `prompt_feedback`; ending with a blank line captured only the intended text. ⚠️ **This is a CLASS rule: the Mode-5 fix landed on the Forward Register where it was noticed, and the same absorption reaches whichever subsection is last.**
>
> ⚠️⚠️ **MODE 5 — [EXECUTED HERE] THE SINGLE EDIT MUST SPAN THROUGH `#### Prompt Feedback`, AND NO LATER ASSISTANT TEXT MAY BEGIN WITH `- ` OR `N. `.** The daemon parses a CONCATENATION of assistant parts, not your file. **Measured: an `Edit` whose `new_string` ends at the last bullet let the NEXT chat part's `- re-ran fwcheck…` lines get absorbed into the capture — a five-item block shipped SEVEN rows, with `fwcheck.py` on the file reporting 5 and exit 0.** The blank line and the through-Prompt-Feedback span both terminate the capture; the no-leading-dash rule covers the ordering step (5) narration.
> **(c)** Run the mechanical check below. ⚠️ **It verifies whichever FILE you pass it and CANNOT observe the transcript, so it is NECESSARY, NOT SUFFICIENT (C15). It prints `FILE=` as its first line — deposit only the run against the REPORT, and keep the scratch run out of the evidence file (C15: every check names the artifact it reads).** — (a) is what covers the channel.
>
> Write to the evidence dir as `fwcheck.py` **using Bash or a Python file-write, NOT the `Write`/`Edit` tools** — ⚠️ **its source contains the literal string `### Ledger Updates`, and a `Write`-authored copy enters `_all_assistant_text` ahead of your report.** Run it, deposit stdout as `forward_register_check.txt`:
> ```python
> import re, sys
> EXPECTED = 4
> BULLET_RE = re.compile(r"^(?:-\s|\d+\.\s)")          # verbatim, bellows.py:1409
> doc = open(sys.argv[1], encoding="utf-8").read()
> lu = re.search(r"### Ledger Updates\s*\n(.*?)(?=\n## |\Z)", doc, re.DOTALL)
> lu_body = lu.group(1) if lu else ""
> fw = re.search(r"#### (?:Forward Register|FORWARD(?: Additions)?)\s*\n(.*?)"
>                r"(?=\n#### |\n### |\n## |\n\s*\n|\Z)", lu_body, re.DOTALL)
> fw_text = (fw.group(1).strip() if fw else "")
> lines   = [l for l in fw_text.splitlines() if l.strip()]
> bullets = [l for l in lines if BULLET_RE.match(l.strip())]
> rows    = ([" ".join(b.split()) for b in bullets] if len(bullets) >= 2
>            else ([" ".join(lines[0].split())] if lines else []))
> wrap_ok = len(lines) == len(bullets)
> print(f"FILE={sys.argv[1]}")
> print(f"LU={bool(lu)} FW={bool(fw)} NONBLANK={len(lines)} BULLETS={len(bullets)} DAEMON-ROWS={len(rows)}")
> print(f"WRAP-CHECK={'PASS' if wrap_ok else 'FAIL - non-bullet line inside block WILL BE DROPPED'}")
> for r in rows: print("   ROW:", r)
> sys.exit(0 if (len(rows) == EXPECTED and wrap_ok) else 1)
> ```
> ⚠️ **[EXECUTED HERE — 2026-08-03] Validated against SIX shapes; it now agrees with the real `sanitize_items` on every one:**
> ```
> four dash bullets       DAEMON-ROWS=4  WRAP PASS   exit 0
> four NUMBERED items     DAEMON-ROWS=4  WRAP PASS   exit 0
> a WRAPPED item          DAEMON-ROWS=4  WRAP FAIL   exit 1
> blank-separated bullets DAEMON-ROWS=1              exit 1
> a --- rule inside       DAEMON-ROWS=4  WRAP FAIL   exit 1
> session-18 shape        DAEMON-ROWS=1              exit 1
> ```
> ⚠️ **An earlier version used `startswith("-")` instead of `BULLET_RE` and had no wrap check — it scored the plan's own NUMBERED items as ZERO and passed a wrapped item green. ⚠️ These controls were RE-MEASURED at the four-item count; an earlier record quoted five-item results that `EXPECTED = 4` had since falsified.** Run it with `; echo "FWCHECK-EXIT=$?"` and record both.
>
> ⚠️⚠️ **RE-RUN `fwcheck.py` AFTER YOUR FINAL EDIT and record both runs.** A recorded result decays with every subsequent edit; the deposited evidence must describe the SHIPPED file.
>
> ⚠️⚠️ **THE "AFTER" ROW COUNT IS NOT OBSERVABLE FROM THIS STEP — DO NOT ASSERT IT.** `_append_forward_row` runs inside the daemon at worktree teardown, after this step's process has exited. **In-step you assert the RECOVERABLE-ITEM count — items-in must equal items-out, FOUR in and four rows out, via `fwcheck.py`. The `FORWARD.md` row-count reconciliation is a POST-CLOSE obligation owed to the session wrap.** Record the BEFORE count — **2 data rows at authoring, row 2 being the junk stub** — and name the reconciliation as owed.
>
> ⚠️ **Rows land carrying their literal `- ` marker** (`sanitize_items` preserves it) while existing row 1 does not. Cosmetic daemon behaviour — **do not read it as a failure.**
>
> **The FOUR items — `- ` bullets, contiguous, one physical line each:** ⚠️ **211's lint convergence is NOT an item — an item whose content is "this is not an item" is the junk class item 4 exists to supersede. It is stated in `#### Project Status` instead.**
> - `generate_lessons_report` (`src/lessons_forge.py:593`) writes with no explicit `encoding=` — verified at authoring, the line is `with open(output_path, "w") as f:`.
> - `detect_duplicates` returns `[]` on a failed reference read, so a read failure is indistinguishable from "no duplicates".
> - `run_full_lessons_cycle` drops the staled-proposal count.
> - Row 2 of this register is a parser artifact recording zero items and should be superseded.
>
> ⚠️ **SCOPE NOTE — items 1–4 are the session-18 backlog, not Gate 1's product.** They require a lessons-forge-dispatched Receipt to reach the right register, and this is one. **CEO-approved 2026-08-03.**
>
> **`#### Project Status`** — one milestone **SCOPED to this plan's sixteen**: Gate 1 complete for entries 199–214 → proposals 207–222; 16 codify / 0 backlog / 0 reference; all sixteen remain `proposed` and Gate-2-bound. ⚠️ **Never a bare corpus-wide `proposed = N`.**
>
> **`#### Prompt Feedback`**
>
> ### Rule 20 self-check
>
> **Run the canonical Rule 20 self-check block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`** — ⚠️ **ABSOLUTE path: it lives at the GOVERNANCE ROOT and does NOT exist in your lessons-forge worktree** (QA row 7 asserts exactly that file is unchanged). **The Planner does not inline the block; this pointer is the only channel (Rule 20, Checklist #4).** **Fill in these four values — do NOT paraphrase the template paragraph and do NOT substitute a "review the file" pointer for the values:**
> - `plan_slug`: `gate1-207-222-2026-08-03`
> - `qa_report_path`: `<abs path to knowledge/qa/gate1-207-222-qa-report-2026-08-03.md>`
> - `evidence_dir`: `<abs path to knowledge/qa/evidence/gate1-207-222-2026-08-03/>`
> - `required_evidence_files`: `["route_readback.txt", "pytest_targeted.txt", "forward_register_check.txt", "outside_range_image.txt", "doctrine_pins.txt", "unclassified.txt", "src_untouched.txt"]`
>
> ⚠️ **The filenames MUST be QUOTED Python strings** — unquoted they raise `NameError`, which the gate reports as "no Rule 20 banner". ⚠️⚠️⚠️ **`required_evidence_files` IS A THREE-LINE STRUCTURE IN THE CANONICAL BLOCK. REPLACE ALL THREE LINES WITH THE SINGLE-LINE ASSIGNMENT ABOVE — or, if you keep the three-line form, paste the seven QUOTED FILENAMES onto the inner `# PLACEHOLDER —` line WITHOUT THE OUTER BRACKETS.** ⚠️⚠️ **[MEASURED] Pasting the bracketed list onto the inner line yields `[[...]]`; `os.path.join` then raises `TypeError: join() argument must be str, bytes, or os.PathLike object, not 'list'`, the block prints NOTHING AT ALL, and `gates.py:588` reports it as "no Rule 20 self-check banner" — the same signature as the unquoted-filename case, and unrecoverable in-step.**
>
> ⚠️ **SEVEN files, matching the list above.** ⚠️⚠️ **Rule 18 makes an evidence file MANDATORY for any check that executes a command and interprets its output — which is notably rows 4(b) (a 76-line image comparison), 7 (two shasum triples), 5, and 8 (two git commands interpreted); rows 1 and 9 likewise deposit theirs. An earlier draft declared three, omitting the plan's own "only value-level detector", so Rule 20's mechanical check certified a set that excluded it.** `fwcheck.py` lives in the evidence directory but is a tool, not evidence — it is not in `required_evidence_files`. ⚠️ **The step-(1b) ledger scratch file goes under `/tmp`, NOT the evidence directory** — it is neither evidence nor a deliverable, and it must not be committed with the declared deposit. **Deposit all SEVEN BEFORE running the block; it `sys.exit(1)`s on any missing or empty.** ⚠️⚠️ **ON ANY `❌`/unverifiable branch THE FILE IS STILL DEPOSITED** — carrying the live reading plus the verbatim reason the anchor is absent. **A missing evidence file is a Rule 20 CRITICAL; an unverifiable row is not, and the fail-closed clauses must not be read as licence to write nothing.**
>
> **Include the block's literal stdout — ⚠️ on a PASSING run only. `RULE_20_SELF_CHECK_BLOCK.md:41` mandates that a FAILED run's raw stdout goes into the EVIDENCE FILE, not the report body; pasting `FAILED` into the report adds a second gate failure on top of the halt.** The banner and the passing line must appear VERBATIM:**
> `Rule 20 — QA Self-Check Results`
> `PASSED — SELF-CHECK PASSED`
> ⚠️ **Both strings are quoted HERE, in the step's instructions, because `plan_lint` check (c) searches the whole plan for them — and they are deliberately kept OUT of the Drafting Cycle block, which is a record, not an instruction.** ⚠️ **Em-dash U+2014, not a hyphen. `gates.py:567` sets the banner WITHOUT a leading `##`** — emit exactly what the canonical block prints.
>
> ⚠️ **ORDERING:** (1) finish every other section; (1b) **compose the ledger block in a scratch file and run `fwcheck.py` against it until it exits 0**; (1c) author `### Ledger Updates` into the report in ONE `Write`/`Edit`, complete, and **never re-edit it**; (2) run row 0(v)'s checks and write results in — **including Receipt item 10, which can only be written truthfully AFTER (1c) and must NEVER be pre-written at (1)**; (3) run the Rule 20 block; (4) paste its stdout into the report; (5) **re-run BOTH `fwcheck.py` and the Rule 20 block. APPEND (`>>`) the second `fwcheck` run to `forward_register_check.txt`** — ⚠️ **append, not overwrite: obligation (c) already deposited run 1 there and a plain write would destroy the record this step mandates keeping.** ⚠️⚠️ **The Rule 20 re-run is a TERMINATING self-check ONLY — do NOT re-paste its stdout. If it does not print the passing line, HALT and report. The (4) stdout is valid precisely because the re-run reproduced it; say so in the Receipt.** — ⚠️ **a FILE write, not a report edit, so recording the re-run cannot stale the thing it records.** ⚠️ **An earlier draft called (4) the "FINAL edit" and then required a record after it, which has no terminating state.** ⚠️ **Obligation (a)'s "author it last" means AFTER every other SECTION is final, not after every edit — steps (2)-(4) still land, and they touch other sections. Uniqueness, not position, is what the daemon reads.**
>
> **Deposits:**
> - `knowledge/qa/gate1-207-222-qa-report-2026-08-03.md`
> - `knowledge/qa/evidence/gate1-207-222-2026-08-03/`
>
> ⚠️ **Rule 26: evidence files are represented by the DIRECTORY as a single bullet.** Listing them individually is forbidden — a mid-table halt commits only the files that exist, and a declared-but-unwritten file is a false `rule_22(a)` failure.
>
> ⚠️ **A HALT MUST STILL LEAVE A COMMITTED RECORD:** finish the report, write the evidence files, commit whatever exists by explicit pathspec.
>
> Commit by EXPLICIT PATHSPEC — `git add <exact paths>` then `git commit -m "…" -- <exact paths>`. **NEVER `git commit -a`, never an unscoped `git add -A`.** ⚠️ **`git add` FIRST — load-bearing for NEW files.**

---

## Drafting Cycle
**Tier:** T2 — triggers fired: T-2 (production-data mutation), T-6 (governance surface), T-8 (novel — the batch shape differs from every parent's).
**Walks:** 1 warm walk; 2 ACID passes run alone; 1 concurrent cold panel (5 readers); 5 sequential cold rounds; 2 closing passes; and 1 COMPLETE five-lens walk over the whole artifact. ⚠️ Rounds are numbered in the order run: sequential 1-3 (weak spots / destruction / vulnerabilities), 4 = ACID, 5 = integration-vs-record, 6 = weak spots again. The ACID passes and the closing passes are counted separately from the sequential rounds.
- Weak spots:          w1 5 folded; sequential round 1 cold, 26 folded (8 of high severity, all in the preceding culmination).
- Destruction:         w1 2 folded, 1 verified negative; sequential round 2 cold, 16 folded (5 high, all in the preceding culmination); premises P1-P5 adjudicated, two falsified.
- Vulnerabilities:     w1 4 folded; sequential round 3 cold, 13 folded (2 high, both in the preceding culmination); every mandated command executed against the live environment.
- Integration-record:  w1 2 folded, 2 verified negative; sequential round 5 cold, 12 folded (3 high). ~~conformance re-checked at every version, lint recorded~~ — **STRUCK 2026-08-03: `plan_lint` had been run at every version, but §5's second half, the by-scope Rules and Checklist walk, had NOT. The clause attested a pass that did not happen.** The walk was then run in round 5 and returned four Checklist FAILs and a Rule 58 PARTIAL, all folded.
- ACID:                run alone against v2 (7 folded); alone against v7 (12 folded, 4 high) — the pass that produced the deletions; alone against v11 (9 folded, 2 high), which found six of its nine in the cut's own repair text.
**Cold panel (T2):** concurrent panel pass on v3 (five readers, ~40 folded) plus three SEQUENTIAL cold rounds on v4/v5/v6 with a culmination between each.
**Origin diff:** run against the structural parent, then RE-RUN against the two newer same-class siblings after the first target proved to be the oldest of three; 9 further gaps folded.
**Conflicts:** C1-C12 through v3; C13-C18 added at v4; C14 re-sourced at v7 as a declared reversal.
**Closing:** v14 - a COMPLETE five-lens walk over the whole artifact (27 sections x 5 lenses, coverage matrix recorded, four coverage limits declared) returned NOT DRY: 16 findings, 4 material. ⚠️ **NONE of the four material findings touched the sixteen writes or their verification**; the two that did were LOW completeness gaps in the QA read, and both are folded. All six are folded. ⚠️⚠️ **SECTION 2's CLOSING CONDITION IS UNMET: the last event was a fold, not a lens pass — deposited on CEO direction, and the plan_lint WARN this earns is correct and expected.** ⚠️ Nine earlier rounds were each aimed at the newest fold rather than at the artifact, which is how a CRITICAL survived to v13 in the one region never examined; the complete walk is what found the remaining class defects.
