# Lessons Forge — Gate 2: codify proposals 207–222 into three doctrine files, then flip all sixteen to `implemented`
**Date:** 2026-08-03 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (SA) → Step 2 (DEV) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always | **cycle_tier:** T2

## CEO Context

Gate 1 (plan 297, closed 2026-08-03) routed all sixteen proposals `codify` with five riders. This plan codifies them into **three** doctrine files and flips all sixteen `proposed → implemented`. **No Plan B** — every one of the sixteen is prose; no `plan_lint` half is owed, so there is no bellows dependency to declare.

**⚠️ PROVENANCE CONVENTION.** `[EXECUTED HERE — <date>]` · `[INHERITED FROM <plan> — NOT RE-EXECUTED]` with its reason. **There is no third marker** (`297:116`). Governs EXECUTION claims, not measured values, which are re-confirmed at run time (Checklist #29).

**⚠️ THE INHERITED CLAIMS, MARKED — an unmarked cited claim is neither executed nor inherited, which the convention forbids:**
- **`[INHERITED FROM 291 — NOT RE-EXECUTED]`** `291:428` — Gate 2 commits every doctrine edit BEFORE touching the DB. *Reason: it describes a shipped plan's task ordering, observable only by reading that plan, which is what C4 encodes.*
- **`[INHERITED FROM 297 — NOT RE-EXECUTED]`** `297:26` — a lessons-forge cycle running inside a verdict gate is normal shop behaviour. *Reason: a claim about historical dispatch patterns; not reproducible on demand. It is load-bearing for precondition 3 and C12's forensic signature.*
- **`[INHERITED FROM 297 — NOT RE-EXECUTED]`** `297:82` — 211 and 219 are two halves of one contract. *Reason: a Gate-1 routing judgement, not a measurement.*
- **`[INHERITED FROM 297 — NOT RE-EXECUTED]`** `297:446` — `in_verification_section` is never cleared by `###`/`####`. *Reason: a parser behaviour measured by 297; re-executing it needs a live QA report, which does not exist until Step 3.*
- **`[INHERITED FROM 246 — NOT RE-EXECUTED]`** plan 246's verdict record retaining diminishing-returns as outer framing. *Reason: a historical verdict, immutable by nature. ⚠️ The sweep that measures its BLAST RADIUS was executed here (see E1).*

### Rule 21 — justification for `Test Scope: targeted`

This plan changes **no source code**. Its deliverables are prose edits to three governance markdown files plus one scoped `UPDATE` on `lesson_proposals`. No module, schema, or route is touched, so a full-suite run would exercise nothing this plan can break. **Targeted scope = the lessons-forge suite**, which covers the corpus-integrity helpers that read `lesson_proposals`. ⚠️ Per the DEV-step lesson, the full suite is deliberately NOT authored into a DEV step; the targeted run lives in QA.

### ⚠️ Concurrency preconditions — and the DETECTION for each

Steps are separated by arbitrarily-long verdict gates over **three shared stores**: the root doctrine files, the lessons-forge DB, and two git repos. **Each precondition names its detector; none is assumed.**

| # | precondition | detection |
|---|---|---|
| 1 | **No other plan edits the three doctrine files** between authoring and this plan's commit | Step 1 hash pin (Task S0) **and** Step 2 Task A1 **and** Task E0's pre-commit re-verify — three checks, not one |
| 2 | **No Gate-2-class plan for 207–222 runs in-window** | Step 2 A0 state 5 (the sixteen already `implemented`) and QA row 22 |
| 3 | **A lessons-forge cycle MAY legitimately run in-window** — `297:26` records this as normal shop behaviour | ⚠️ **NOT a violation.** It adds proposals at 223+ and may stale one of the sixteen. Detected by C12 (`changes()` must equal 16) and accommodated by the **pinned outside-range id set** (QA row 23) |
| 4 | **Serialized bellows dispatch** — two agents must not write root doctrine concurrently | ⚠️ **This is an ASSUMPTION doing load-bearing work, stated rather than hidden.** Task E0's pre-commit re-verify is the guard that does not depend on it |

**FORENSIC SIGNATURE:** if Task A1 passes but Task E0 fails, a foreign edit landed *during* Step 2 — it is not this plan's and must not be swept into its commit.

### ⚠️ Scope discipline

**This plan writes three files OUTSIDE its own dispatch tree.** It is dispatched from `lessons-forge` and edits `/Users/marklehn/Developer/GitHub/{DRAFTING_CYCLE,PLANNER_TEMPLATE,RULE_20_SELF_CHECK_BLOCK}.md`. **No other file in the root is touched.** The commit at Task F is **path-scoped to exactly those three paths** — never `git add -A`, never `git add .`.

**⚠️ `_gate_scope_check` is cwd-scoped and submodule-blind** (`297:469`): a root doctrine edit made from a submodule-dispatched plan is **invisible to every gate**. 297 carried that exposure while editing *nothing*; this plan edits three root files. **The QA doctrine-integrity rows are the ONLY guard. They fail closed.**

**⚠️ VERIFY EDITS VIA BASH, NOT FILE TOOLS.** With the daemon up, a file-tool read can lag a bellows-managed tree. Every "the edit landed" confirmation uses `shasum -a 256` or `grep -F`.

### ⚠️⚠️ AUTHORING SOURCE — there is NO edit map for this batch

291 authored from diagnostic 290's edit map under Rule 27. **No diagnostic was run for 207–222 and no edit map exists.** Sources, in order:
1. **The live DB** — **[EXECUTED HERE — 2026-08-03]** `suggested_action` / `reasoning` for ids 207–222, read from the canonical path (`?mode=ro`). PRIMARY source, not a deviation as in 291.
2. **Plan 297's disposition table (`297:38–90`) and five riders (`297:74–90`)** — cited under Rule 27.
3. **Live doctrine** — **[EXECUTED HERE — 2026-08-03]** every dedup anchor re-opened and confirmed.

**⚠️ Do NOT let the SA or DEV compose doctrine prose at run time.** The AFTER text for all **twenty-two** edits is GIVEN below. The SA **places** it.

### ⚠️⚠️ THIS PLAN EDITS `RULE_20_SELF_CHECK_BLOCK.md` — REVERSING A DECLARED SUBTRACTION

`291:12` dropped 287's fenced-block extraction check on the stated premise that **291 did not touch that file**, leaving a note: *"A future clone must not 'restore' the extraction machinery without first re-checking whether its plan edits that file."*

**[EXECUTED HERE — 2026-08-03] Re-checked. This plan DOES edit it (proposal 211), so the premise is false here and the machinery is RESTORED — a declared reversal.** A whole-file hash cannot serve as the pin because the file legitimately changes.

⚠️ **THE PIN IS FENCE-BASED, AND THE EXTRACTION METHOD IS SPECIFIED** — a pin whose method is unstated is unreproducible and fails closed on the honest path. **[EXECUTED HERE — 2026-08-03]:**
- fence lines in the file: **2** (exactly one fenced block)
- extracted block: **67 lines / 3030 bytes**
- **`BLOCK_SHA` = `d399f9330802025eddebb5e627cd8efaa93752cc9f41fe3b9f763bca98e2b73f`**

**The extraction command — use exactly this, byte for byte:**

~~~
awk '/^`{3}/{n++; next} n==1' /Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md | shasum -a 256
~~~

⚠️⚠️ **THE COMMAND'S CORRECTNESS IS BUILD-DEPENDENT — verify your `awk` before trusting it.** `` `{3} `` is an ERE interval, and **BWK awk historically did NOT support intervals**; on such a build the pattern matches nothing, the extraction returns EMPTY, and the hash comparison HALTs a **correct** run. **[EXECUTED HERE — 2026-08-03] `awk version 20200816` supports intervals: the interval form and a literal three-backtick form both return 3030 bytes, identically.** **If your `awk` differs, confirm both forms agree before proceeding; if they do not, HALT rather than adapting the command.**

⚠️ **The block above is TILDE-fenced and the pattern uses `` `{3} `` deliberately** — a command containing three literal backticks cannot be quoted inside a backtick-fenced markdown document without the fences colliding. **This is Rule 64 (E17 below) applied reflexively to this plan's own instructions.**

### ⚠️ THE ROW-0 GUARD INVERTS — and "intended ways" is ENUMERATED

`297:469` pins doctrine **UNCHANGED, absolutist**, because a *routing* plan must not touch doctrine. **This plan edits doctrine by design** → "changed only in the intended ways." ⚠️ **Do not import 297's absolutist variant** (false-HALTs every correct run), nor 291's unexamined (291 edited two files and pinned the third absolutist; **this plan edits all three**).

⚠️ **"Intended ways" = exactly the TWENTY-TWO edits E1–E22 below, and nothing else.** **[EXECUTED HERE — 2026-08-03] The count was enumerated from the labels, not asserted:** 12 in `DRAFTING_CYCLE.md` (E1–E12), 9 in `PLANNER_TEMPLATE.md` (E13–E21), 1 in `RULE_20_SELF_CHECK_BLOCK.md` (E22). **Every edit is its own integer — there are no sub-lettered edits.**

**Three independent referents, all required — and NONE is dev-log-sourced:**
- **(i) per-proposal content rows** (QA rows 3–18) — each asserts the specific AFTER text **from this plan**;
- **(ii) per-file line-delta bounds** — ⚠️ **computed and recorded by the SA in the BLUEPRINT** (hash-pinned, CEO-reviewed at the Step-1 gate), and compared by QA **against the blueprint, never against the dev-log**. A dev-log referent is circular: the agent that made the edits also writes the number;
- **(iii) `BLOCK_SHA`** above — pinned at authoring, not by the DEV.

### ⚠️ THIS PLAN REWRITES THE RULES GOVERNING ITS OWN DRAFTING CYCLE — nine of them

§2 doneness (210+216), §2.6 ×3 (214, 216, 217), §2.7 ×3 (207, 208, 212), §2.8 ×2 (213, 217), §3 (215). **The cycle this plan runs under is v1.3 as it stands today.** An agent noticing the Cycle Log does not satisfy the *amended* text is observing the intended state.

### §6 AND `## When this file changes` BOTH GOVERN — explicit §4 deferral

**215 amends §3.** ⚠️ **§6 requires the deferral be SAID:** 215's sub-claims are prose about *when to re-run the check* and impose no new structure `plan_lint` §4 parses, so **§4 is unchanged and remains in lockstep — stated, not assumed.**

### ⚠️ NUMBERING — THREE OVERLAPPING SPACES, offset +8

`297:61`: proposal_id = entry_id **+ 8**, sequences OVERLAP in 207–214. Proposal 207 → entry 199; proposal **215** → entry **207**. **Check every pair individually.** ⚠️ A THIRD space: the v1.3 History row's `(206)` is a proposal id from the PRIOR batch — **not** this batch's entry 206 (= proposal 214).

**New rule numbers, CEO-decided 2026-08-03: 209 → Rule 63, 220 → Rule 64.** **[EXECUTED HERE — 2026-08-03]** scope-applied per §5: Orchestration Plan Rules max **62**; Plan Authoring Checklist max **33**; Procedures max **6**. ⚠️ **Never grep `### N.` unscoped.**

### ⚠️ `RULE_20_SELF_CHECK_BLOCK.md` HAS NO VERSION LINE AND NO HISTORY SECTION

**[EXECUTED HERE — 2026-08-03]** 140 lines, no `**Version:**`, no `## History`. **The SA must not improvise one.** E22 carries no version bump and no changelog row.

### ⚠️ VERSION-STRING COLLISIONS — MEASURED; ANCHORS LENGTHENED ACCORDINGLY

**[EXECUTED HERE — 2026-08-03]** `grep -Fc '1.3 (2026-08-02)' DRAFTING_CYCLE.md` → **2**; `grep -Fc '4.82' PLANNER_TEMPLATE.md` → **3**.

**A replace-all destroys a governance changelog entry, and "gained exactly one row" cannot see a REWRITTEN one.** **Every version edit names a LENGTHENED anchor inline.**

⚠️⚠️ **AND THE NEW CHANGELOG ROWS MUST NOT CONTAIN THE PRIOR VERSION STRINGS.** E12's v1.4 row must not contain `1.3 (2026-08-02)`; E21's v4.83 row must not contain `4.82`. **A row reading "supersedes 1.3 (2026-08-02)" makes QA row 21's post-edit count 2 instead of 1 and FAILS a correct run.** Refer to predecessors by number alone ("since 1.3"), never by the full pinned string.

**⚠️ VERSION DATE — DECLARED, do not recompute.** All four version/changelog edits carry the literal date **`2026-08-03`**, the date the CEO took the routing and placement decisions. **A version stamps the DECISION, not the keystroke.** The DEV uses the literal string and does not substitute today's date. (Plan 246 tokenized with `<EXECUTION-DATE>`; deliberately NOT followed here.)

### ⚠️ THIS PLAN DOES NOT APPEND TO `LESSONS.md`

The register stands at **172** with a **15-entry batch pinned** for the next cycle. An append would break that delta and halt the next cycle plan. **No step touches `LESSONS.md`.**

---

## The dedup record — FOUR PARTIALS, exhaustive over the batch

**[EXECUTED HERE — 2026-08-03] re-opened and re-confirmed**; inherited from `297:65–72`.

| proposal | already-present text | consequence |
|---|---|---|
| **215** | `DRAFTING_CYCLE.md:112` — *"After compacting **or editing** the log, re-run the gate…"* | **Write TWO sub-claims, not three.** |
| **217** | `DRAFTING_CYCLE.md:108` — *"Do not keep a running fold-count … not as a separate running tally."* | **RECONCILE** per-lens with per-region. |
| **218** | `PLANNER_TEMPLATE.md:1349` — *"verify the construction actually produces the expected delta"* | scoped extension. |
| **207** | `DRAFTING_CYCLE.md:87` — *"verify the subsumption against live data — per item, not in aggregate"* | scoped extension. |

**All other TWELVE: no existing coverage.** **Rule 58(2): this record is EXHAUSTIVE over the batch**, not a sample.

⚠️ **Licence to disagree (Rule 58(1)):** if the SA's live read disagrees with any row, **HALT and report**.

---

## The twenty-two edits — AFTER text is GIVEN; the SA places it

### DRAFTING_CYCLE.md — E1–E12

**E1 — 210 + 216 → §2 doneness criterion (`:38`). ONE merged edit.**
⚠️⚠️ **EXACT REPLACED SPAN — this is a SENTENCE replacement, not a parenthetical one.** Replace from `The cycle is **done** when` through **and including the terminal period** of `(that IS the diminishing-returns signal).` — and nothing else in that paragraph. ⚠️ **THE PERIOD IS INSIDE THE SPAN.** **[EXECUTED HERE — 2026-08-03]** the live text reads `…signal). The **last event…`, and the AFTER text below supplies its own closing period; a span ending at the parenthesis would leave `…coming back dry.. The **last event…` with a doubled period. **[EXECUTED HERE] span-end uniqueness: `grep -Fc '(that IS the diminishing-returns signal).'` → 1; opening-anchor uniqueness → 1.** **[EXECUTED HERE — 2026-08-03] the span is one contiguous sentence on `:38`.** ⚠️ **An earlier draft called this "replace the parenthetical" while supplying a full-sentence AFTER text — anchoring on the parenthetical alone produces a mangled sentence, and this is the edit that reverses a deliberately-preserved prior decision, so an ambiguous span is worst placed here.**
⚠️⚠️ **A DELETION THAT REVERSES A DELIBERATE PRIOR DECISION — declared in advance** per §2.7 subtractive-trim and `297:114`. **[EXECUTED HERE — 2026-08-03] Sweep:** `diminishing-returns signal` occurs **1×** in `DRAFTING_CYCLE.md`, **0×** in `PLANNER_TEMPLATE.md`, **0×** in bellows code — **no mechanical breakage.** But **plan 246's verdict record states it was deliberately PRESERVED**: *"diminishing-returns retained as outer framing."* **Premise for reversal:** proposals 210 and 216 are the measurement that falsifies the falling-curve reading. **Blast radius is every future plan's closing condition — that is the intent.** AFTER:

> The cycle is **done** when a full walk returns zero or only-minor findings **over a region the previous walk did not touch**. ⚠️ **A falling finding-count is NOT the convergence signal** — severity falls because the same regions are being re-read, not because the artifact is sound. Budget for a cold panel's yield staying **flat**: a five-lens sequential panel returned 11 / 12 / 12 / 12 / 12 with no decay, roughly a third of each round being defects the immediately preceding round's folds introduced. The signal is **rotation**: a walk aimed at a previously unexamined region coming back dry.

**⚠️ §2.6 TAKES THREE APPENDS (E2/E3/E4) — anchors and resulting order SPECIFIED.**

**E2 — 217b → §2.6**, anchor `A "bounded" or "proven-clone" framing is not licence to down-tier or skip the cold panel`. New sentence at that paragraph's end:
> **Ask the inverse question too: has a shipped sibling already DELETED this machinery?** A "do not re-add" note in a `Done/` plan is invisible unless someone diffs against it, and a clone that re-adds deleted machinery reproduces a defect its parent already paid to remove.

**E3 — 216b → §2.6**, anchor `review-target rotation prevents the quiet step from accumulating unexamined risk`. New sentence at that paragraph's end:
> **The panel's yield does not decay, and that is structural.** Every fold is an unreviewed edit, so folding N findings creates a fresh unreviewed surface of N edits which the next reader is the first to see. Do not read a flat or rising round as panel failure, and do not read a falling one as convergence.

**E4 — 214 → §2.6**, a NEW paragraph after E3's, the last in §2.6 before `### 2.7`:
> **Aim the panel at the premises that LICENSE a deletion.** Hand cold readers the plan's deletion premises explicitly and ask them to falsify each against live data. A premise licensing a removal is the highest-value target — it is where the author has already convinced themselves — and it is sharpest under a "proven clone" framing, where the clone's deletions are exactly where its judgement diverges from its shipped parent.

**Resulting §2.6 order: intro ¶ → clone ¶ (+E2) → rotation ¶ (+E3) → E4 ¶ → `### 2.7`.**

**E5 — 207 → §2.7 subtractive-trim bullet**, anchor `Never compute an edit boundary from a delimiter on line-oriented markup`. Appended:
> **A count is not a value guard.** When a trim replaces a value-level assertion with a count over the same scope, the subsumption is not established by argument — **construct the change the surviving check is supposed to catch and confirm it FAILS.** A `COUNT(*) WHERE col IS NOT NULL` cannot see a row moving between two non-NULL values: it passes unchanged while the capability it replaced is gone.

**E6 — 208 → §2.7 lens-attestation bullet**, anchor `without it a later reader trusts an attestation that was never honest`. Appended:
> **Price the re-run before writing an INHERITED marker.** Marking a claim inherited makes it honest, not true — the reason given for not re-executing is itself an unverified claim. Assess the literal cost first; most "impractical to test" reasons dissolve into a `cp` plus one command.

**E7 — 212 → §2.7 execute-against-real-data bullet**, anchor `pair it with its exit code, or with an input known to make it speak`. Appended:
> **`grep -F` is mandatory for every literal search, and a search not run with `-F` is invalid evidence regardless of its exit code.** On this shim a `*`-bearing pattern run without `-F` exits **1, silently, on a file where the searched line is present** — so the unsafe invocation is forbidden outright rather than governed by exit-code interpretation rules.

**E8 — 213 → §2.8**, NEW bullet after the deletion bullet:
> **The ledger records violations; it does not prevent them.** A Conflict Ledger can carry a constraint correctly and still watch the edit phase re-violate it — measured across six ACID passes, every one of which found defects introduced by the culmination immediately before it, including culminations whose entire purpose was repair. **After any fold, re-run the mechanical check that reads the touched region.** Read the record-without-prevent asymmetry as the argument for MECHANIZING a constraint rather than only documenting it.

**E9 — 217a → §2.8 deletion bullet**, anchor `the same whole-artifact sweep an addition would need`. Appended — ⚠️ **RECONCILED with §3:**
> **Count folds per REGION, not per plan** — a per-plan count hides the region-level accumulation this bullet turns on. ⚠️ **This is a drafting-time judgement tally kept in the scratchpad walk register, NOT a Cycle Log entry:** §3 forbids a running fold-count in the log and mandates the compact per-lens form, and that prohibition is **unchanged**.

**E10 — 215 → §3. TWO sub-claims.** Anchor `the log has satisfied a check on the step's behalf`. Appended:
> ⚠️ **Phrasing the line so it cannot match until earned is necessary but NOT sufficient** — a check satisfied by wording rather than by the condition changing is still silenced. And **the prohibition on quoting gate-matching tokens applies reflexively**, including to the sentence that warns against quoting them.

**E11 — version line.** ⚠️ **LENGTHENED ANCHOR.** Anchor `**Version:** 1.3 (2026-08-02). Amended only through the Iteration Protocol` → within that line only, `1.3 (2026-08-02)` → `1.4 (2026-08-03)`.

**E12 — `## History`, PREPEND a v1.4 row** as the FIRST row under the heading. **[EXECUTED HERE — 2026-08-03] Ordering confirmed newest-first (1.3 → 1.2 → 1.1), so PREPEND is correct.** Names all nine proposals with sections, states **the lens count deliberately stays five**, records the §4-lockstep deferral. ⚠️ **Must NOT contain the string `1.3 (2026-08-02)`.**

### PLANNER_TEMPLATE.md — E13–E21

**E13 — 219 → Rule 17**, anchor `deliverable verification is the safety net`. Appended:
> **A row whose honest disposition is "note" does not belong in this table.** The gate requires every row to carry a pass/fail glyph, so a note-shaped row has no expressible correct answer — deciding a row is note-shaped is the signal to **move it out of the table**, not to write `NOTE` into a column the gate parses.

**Proposal 221 → Rule 55, as E14 (title) and E15 (body). CEO DECISION (c), TAKEN 2026-08-03: codify the PRINCIPLE; demote `ps -p` to the worked example.**
⚠️ *This is a shared rationale heading, not an edit — it deliberately does not begin with an `E<n>` label, so that enumerating edit headers yields exactly twenty-two.*

⚠️ **Rationale, recorded because it departs from a literal reading of the routed text.** 221's thesis is Rule 55(a)'s — *assert on a positive signal; empty output is not an answer.* The `ps -p` line is that thesis's **illustration**. **[EXECUTED HERE — 2026-08-03] a live counter-example was measured during drafting:** the baton's recorded daemon pid **86216** was dead (`ps -p` → exit 1), which under a literal reading means *"the daemon is down."* **It was not** — `bellows.py` was live as pid **96240**, restarted after the session-19 wrap. **A stale record reports a live process as dead: the same false-negative class 221 exists to kill, relocated from the pattern to the record.** Codifying the principle rather than the mechanism closes this without widening what Gate 1 routed — **narrower in mechanism, broader in principle.** **The measurement is evidence, not a rule: it goes to the Forward Register, not doctrine.**

**E14 — TITLE.** Anchor `### 55. Assert a positive signal from the repo or tree that holds the state — empty output is not verification`. AFTER:
> ### 55. Assert a positive signal from the source that holds the state — empty output is not verification

⚠️ **[EXECUTED HERE — 2026-08-03] TITLE-CHANGE BLAST RADIUS SWEPT — NIL inside doctrine.** `grep -Fc` for `Rule 55`, `rule 55`, `55(a)` → **0 / 0 / 0** across all three files; the only hit is the heading itself. Seven shipped `Done/` plans reference it (288, 296, 297; governance 250, 251, 276, 260) — **historical records, not live governance**, not rewritten.

**E15 — BODY**, appended to Rule 55:
> **Process state is in scope, and the principle governs — not any one command.** `pgrep` returns exit 1 for "no match", which is indistinguishable from "not running", so every failure mode presents as the answer "the daemon is down." **Require a positive confirmation that RESOLVES** — a PID that is then confirmed live, a row that is then read back — and never treat an empty result as an answer. ⚠️ **`ps -p` against a recorded PID is the worked example, not the rule:** a recorded PID goes stale across a restart, and a stale record reports a live process as dead — the same false negative, relocated from the pattern to the record. When the positive confirmation fails, re-establish the record before concluding absence.

**E16 — 209 → NEW Rule 63**, inserted after Rule 62's `Source:` line:
> ### 63. Read the DELIVERY code before theorising about non-arrival
> When a mechanism's output does not arrive, **read the code that delivers it before proposing a cause.** Non-arrival has at least three candidate causes — never sent, sent-and-lost, and sent to an unconfigured destination — and they are indistinguishable from the receiving end; only the delivering code separates them. Evidence: the same missing register row was blamed on the emitting plan, then on the daemon, before a read of `bellows.py:1417` showed the destination resolving to a path that did not exist, logged and skipped.
> *Source: proposal 209, lesson 2026-08-01*

**E17 — 220 → NEW Rule 64**, after E16. **CEO-decided placement — explicitly NOT Rule 18**, which governs evidence FILES:
> ### 64. A pipe-bearing command never goes in a markdown table cell
> A command containing `|` must never be placed in a table cell — put it in a fenced block above the table and have the row cite its result. A delimiter-bearing command inside a delimiter-structured document is a collision in which **escaping changes the semantics**: escaping to `\|` to survive the cell turns ERE alternation into a literal pipe that matches nothing. The failure is silent when the command's "no match" and "not running" exits are the same value.
> *Source: proposal 220, lesson 2026-08-03*

**E18 — 218 + 222 → Checklist #32. ONE merged edit.** Anchor `not through the real entry point`. Appended:
> **The instrument must assert on the POST-condition, never on the presence of the thing being changed** — a check that greps for the text it is trying to remove reports OK on that text's survival. Any scripted edit asserts **`after != before`**, not merely that an anchor matched. **And when a canary is owed, pay for it with real pending work rather than a synthetic probe:** use the actual backlog as the payload, and pair the live observation with an in-process prediction of the same value, so agreement proves the path while disagreement localises the fault.

**E19 — version line `:5`.** ⚠️ **LENGTHENED ANCHOR.** `**Version:** 4.82` → `**Version:** 4.83`.
**E20 — `:6`.** `**Last Updated:** 2026-08-02 (v4.82)` → `**Last Updated:** 2026-08-03 (v4.83)`.
**E21 — `## Lessons Learned`, PREPEND a v4.83 row.** **[EXECUTED HERE — 2026-08-03] Ordering confirmed newest-first.** Names proposals 209, 218, 219, 220, 221, 222; records Rules 63/64 and 221's principle-over-mechanism decision. ⚠️ **Must NOT contain the string `4.82`.**

### RULE_20_SELF_CHECK_BLOCK.md — E22, no version bump

**E22 — 211 → the "Status column" paragraph.** ⚠️ **The one-token sentence is ALREADY THERE — the new content is the CONSEQUENCE.** Anchor `the token must be the entire cell value`. Appended:
> ⚠️ **An annotated cell therefore asserts nothing and escapes BOTH gates.** Because matching is by cell equality, a cell carrying a token plus a note is not a positive row — it is never scanned for hedging keywords — and it carries no failure glyph for `_gate_rule_22_verification` either. The row is neither passing nor failing and both gates ignore it. **The status cell holds exactly one token and nothing else.**

**⚠️ The lint 211 proposes is bellows-owned and CONVERGES on the already-deferred status-cell glyph lint — recorded as convergence, NOT a new item** (`297:81`). **Nothing here ships a lint.**
**⚠️ 211 + 219 are two halves of one contract across two artifacts** (`297:82`) — **E22 and E13 sequenced together; QA verifies them as a pair (row 19).**

---

## Conflict Ledger — RUN-TIME constraints

- **C1** — every edit anchored on a QUOTED UNIQUE string, never a line number. `grep -Fc '<anchor>'` must return exactly **1**. ⚠️ **`>1` → lengthen the anchor. `0` → HALT** — zero means the text is ABSENT and the file has changed; lengthening cannot help.
- **C2** — version edits are surgical swaps against LENGTHENED anchors; **never** replace-all.
- **C3** — the canonical Python block is **byte-identical** after the edit, extracted **BY FENCE using the exact command in CEO Context**, never by line range, and compared against the **authoring-pinned `BLOCK_SHA`**.
- **C4** — doctrine edits committed BEFORE the DB flip (`291:428`).
- **C5** — the flip is scoped to ids 207–222 with `AND status='proposed'`; **no whole-corpus predicate**.
- **C6** — `status_updated_by='ceo'` (live schema `CHECK`).
- **C7** — category is **NON-UNIFORM**: 222 is `instrumentation`. **A uniformity assertion cloned from 289 false-HALTs.**
- **C8** — `$TS` / `$BK` assigned and used in the SAME invocation. An empty `$TS` writes `''` and **exits 0**.
- **C9** — backup: **FIND it, do not reconstruct**; reuse on resume; prefix scoped to id **298**. ⚠️ **And it runs ADJACENT to the flip (Task B sits immediately before Task G), never before the doctrine edits** — a backup separated from the write it inverts by an arbitrary interval restores state that was correct at snapshot time and wrong at restore time.
- **C10** — `grep -F` on every literal; never pipe to `head`.
- **C11** — no glob may reach `ls`; use `find`.
- **C12** — the flip's rowcount must equal exactly **16** ⚠️ **AND `status_updated_at` must GLOB-match a timestamp on all sixteen — BOTH asserted BEFORE commit, in the same transaction, with ROLLBACK on either failure.** An empty `$TS` yields rowcount 16 and passes a rowcount-only guard; after commit the rows read `implemented` and `AND status='proposed'` makes repair impossible.
- **C13** — every verification asserts the **POST-condition**, ⚠️ **and the post-condition differs by edit KIND:** for a **replacement or deletion** (E1) it is `after != before` — the old text ABSENT and the new text present; for a **pure addition** (E2–E10, E13–E18, E22) it is the new text present **plus the surrounding region unchanged**, because there is no "before" to differ from. ⚠️ **Do NOT "apply C13" by rewriting the sixteen addition rows into difference checks — they are already in their correct form.** Never assert the mere presence of the thing being *changed*.
- **C14** — the commit is **path-scoped to the three doctrine paths**; never `git add -A`.
- **C15** — SQLite access uses `busy_timeout` and tolerates the daemon holding the WAL; a `database is locked` failure is a HALT, not a silent retry loop.
- **C16 — THE SCHEDULE ORDER IS LOAD-BEARING AND SERIALIZABLE. Do not reorder it.**
  **A0 → A1 → [C–D: 22 edits] → E0 → E1(DOC_SHA) → F(commit) → F2(post-commit verify) → B(backup) → G(txn: capture P′ · UPDATE · assert 16 · assert TS · COMMIT).**
  Each object is governed by one discipline end to end: **D** by validated optimistic concurrency — every read-to-dependent-write window closed by a revalidation (S0, S9, A1, E0, F2), so a concurrent writer is always detected and never silently interleaved; **P and P′** by a single transaction, where the two assertions are the validation and ROLLBACK is the abort, so a concurrent cycle commits strictly before or after and never inside. ⚠️ **Two cross-object constraints hold simultaneously in this order and in no other: the doctrine commit PRECEDES the DB transaction (C4 / `291:428`, so a die-between is detectable from the doctrine pins alone), and the backup is ADJACENT to it (C9, so the restore is a true inverse).**

### Authoring-time constraints (Planner-owned — NOT addressed to any executing agent)
- **A1** — doctrine AFTER text composed at authoring from the DB.
- **A2** — E14/E15 ship under CEO decision (c). **The SA does not re-open it.**
- **A3** — declared subtractions from 291/297: **ONE, a REVERSAL** (the extraction machinery, restored). ⚠️ **Re-audited after the step bodies existed; one further gap was found and folded — see A4.**
- **A4** — ⚠️ **287/291 carry a guard that an existing backup on a FRESH run is UNEXPLAINED → HALT.** An earlier draft weakened it into a benign reuse. **Per `297:114` an undeclared subtraction found by review is REVERSED, not retroactively justified** — A0 now separates *resume* from *fresh-with-unexplained-backup* (states 4 and 4b).
- **A6** — ⚠️ **DECLARED RELAXATION (one, and this is it).** Task E0's unscoped check was widened from *"any fourth modified path → HALT"* to a **denylist on root `*.md`**. **Premise:** the plan cannot determine before dispatch whether the root sees a modified `lessons-forge` gitlink, so an allowlist guesses the topology and fails in both directions. **Declared here rather than left implicit, per `297:114` — an undeclared relaxation found by review is REVERSED, not retroactively justified.**
- **A7** — ⚠️ **ONE DECLARED RULE 27 DEVIATION, enumerated so QA can count it.** **(1) 221 is codified as its PRINCIPLE with `ps -p` demoted to a worked example**, rather than as a literal transcription of the routed `suggested_action` — CEO decision (c), 2026-08-03, with the live counter-example measured at authoring (see E14/E15). **There is no second deviation.** The doctrine text for the other fifteen is composed from the DB `suggested_action` rows without departure.
- **A5** — ⚠️ **DO NOT add a version-bump-first atomic resume marker.** 287 carried it; the 11-gap keep-or-drop table **deliberately DROPPED it** (item 11) and 291 shipped without it. **Re-adding it is exactly the defect E2 codifies.** Recorded so a later reader does not "restore" it.

---

## How to Run This Plan

Step 1 (SA) → verdict gate → Step 2 (DEV) → verdict gate → Step 3 (QA). `pause_for_verdict: always`. **No step renames this file.**

---

## STEP 1 — SA (blueprint the exact edits; NO writes)

---

> **FIRST — post a short visible chat message (1–2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename this plan file. You are the Solution Architect. **This step is READ-ONLY — you write one blueprint file and nothing else. No doctrine file is touched in this step.**
>
> **⚠️ TASK S0 — PIN THE THREE FILES BEFORE ANY ANCHOR WORK.** `shasum -a 256` each and byte-compare against the authoring pins:
> ```
> 2d5cf9ab7c3a87ed825a1e1edcafea9a9b2598f30b29a7e48868558874a18ee0  DRAFTING_CYCLE.md
> e8289d50f28711fdbf7c5319d812c229d3e7d2e255fc77f7ce868c19c01b6783  PLANNER_TEMPLATE.md
> 3accbce0c8d2b44586edc6c5f95582f775d0bce14276966b7ca90724e0ca5644  RULE_20_SELF_CHECK_BLOCK.md
> ```
> **Any mismatch → HALT.** Every anchor you are about to prove unique would be proven against different bytes than this plan was authored from, and Step 2's A1 would then fail against a blueprint already built on the drift.
>
> **Your job: convert each of the TWENTY-TWO edits E1–E22 into an EXACT, ANCHORED before/after pair the DEV applies without judgement. The AFTER text is GIVEN — you PLACE it, you do not compose it.**
>
> **⚠️⚠️ ANCHOR DISCIPLINE.** Anchor on a QUOTED UNIQUE STRING, never a line number — this plan's line numbers are authoring-time and drift. **`grep -Fc '<anchor>' <file>` must return exactly 1, and you must RECORD that count per anchor.** ⚠️ **A count `>1` → lengthen the anchor and blueprint the lengthened form. A count of `0` → HALT** — zero means absent, not ambiguous, and lengthening makes it worse. An anchor matching two places does not fail loudly: the DEV edits whichever it finds first and every downstream presence grep still passes.
>
> **⚠️ RE-MEASURE THE TWO VERSION COLLISIONS AND RECORD THE COUNTS.** Expected **2** and **3**. **If either differs, HALT.**
>
> **⚠️ DERIVE THE PER-FILE LINE DELTAS BY DRY-RUN — DO NOT PREDICT THEM.** `cp` the three doctrine files to **`/tmp/gate2-298-dryrun/`** — ⚠️ **a path OUTSIDE every git tree; never the repo, never your worktree, or the copies become committable artifacts** — apply all twenty-two edits **to the copies**, run `diff -u` / `git diff --no-index --numstat` against the originals, record the per-file deltas, then **delete the scratch directory and confirm it is gone.** **Write no doctrine file in place — this step remains read-only.**
>
> ⚠️ **A PREDICTED NUMBER FAILS A CORRECT RUN.** Most of these edits append a sentence to an *existing* paragraph line, which `numstat` reports as `1 deleted + 1 added` rather than as a pure addition; a prediction off by one makes QA row 1 fail on honest work. **A measured delta needs no hedge and a predicted one does.** ⚠️ **And the cost of measuring is a `cp` plus one command — which is exactly the calculation E6/208 requires before any claim is marked inherited.** **This is independent referent (ii): QA compares against YOUR blueprint, never against the DEV's dev-log.**
>
> **⚠️ §2.6 TAKES THREE APPENDS (E2/E3/E4); §2.8 TAKES TWO (E8/E9); Rule 55 TAKES TWO (E14/E15).** Blueprint each with its specified anchor and record the resulting order. Do not interleave by judgement.
>
> **⚠️ E22's file is pinned BY FENCE.** Run the exact extraction command from CEO Context and confirm it reproduces `BLOCK_SHA` **and** that the file contains exactly two fence lines. **If the count is not 2, or the hash does not reproduce, HALT** — C3's pin is no longer usable and QA row 20 cannot be written.
>
> **⚠️ LICENCE TO DISAGREE (Rule 58(1)).** If your live read disagrees with any dedup row or any anchor, **HALT and report** — this plan does not override the live file.
>
> **⚠️⚠️ TASK S9 — CLOSING RE-PIN. RE-RUN S0's THREE HASHES AS YOUR LAST ACT AND CONFIRM ALL THREE ARE UNCHANGED.**
> S0 pinned the files at the START of this step, and the dry-run above touches twenty-two edit sites. **A pin taken before the work does not protect work that lands after it** — an edit misapplied to an ORIGINAL instead of a copy is invisible here, because S0 already passed, and Step 2's A1 would then HALT with the blame pointing at drift rather than at this step. **Any mismatch → HALT and say which file you modified.** ⚠️ **This is the same principle as Step 2's Task E0, swept to its sibling site** — E0 was added first and this site was missed, which is the fold-sweep failure this plan's own §2.6 amendment exists to catch.
>
> **Deposit** the blueprint, then commit it. ⚠️ **Committing it is what carries it into the later steps' trees through the teardown merge — QA reads it for referent (ii).** **Output Receipt required.**
>
> **Deposits:**
> - `knowledge/development/gate2-298-blueprint-2026-08-03.md`
> - `knowledge/development/dev-log-gate2-298-step-1-2026-08-03.md`

## STEP 2 — DEV (apply the blueprint faithfully, then flip)

---

> **Read the Step-1 blueprint** and confirm its Output Receipt is Complete; else halt. **⚠️ Record `shasum -a 256` of the blueprint you read and quote it in your dev-log** (Rule 61 — **drift detection, not fail-closed**). Post a short visible chat message. You are the Developer.
>
> **⚠️⚠️ THESE EDITS LAND IN THE REAL GOVERNANCE ROOT — NOT IN YOUR WORKTREE.** No teardown cleans them up; no isolation from any future plan reading those files.
>
> **⚠️ IF YOU HALT AFTER EDITING HAS BEGUN, SAY SO LOUDLY IN THE SAME BREATH.** **Leave the tree exactly as it is** (do NOT restore — the CEO may need to inspect it), and report: that the three files are modified and uncommitted, **which of E1–E22 completed**, and `git -C /Users/marklehn/Developer/GitHub status --porcelain -- <the three paths>`. A halt that omits this reads as "nothing happened."
>
> **⚠️ TASK A0 — PRE-EDIT STATE CLASSIFICATION. Name your state before any write.**
>
> ⚠️⚠️ **THE STATES ARE NOT MUTUALLY EXCLUSIVE. EVALUATE IN THIS ORDER AND THE FIRST MATCH WINS: 6 → 2 → 3 → 5 → 4 → 1.** Most-advanced-first. **A crash between Task F and Task G matches state 2 AND state 4 simultaneously** — Task B runs before F, so a backup always exists on that path — and taking state 4 would route back through A1 and into **re-applying all twenty-two edits to already-edited files.** Ordering is what prevents that; do not classify by whichever description you notice first.
>
> 1. **Fresh** — three files match the A1 pins, **no `pre-298-` backup exists**, and the sixteen still read `proposed` → proceed to A1.
> 2. **Docs committed, flip not done** — `git -C /Users/marklehn/Developer/GitHub log --grep='[298]' --oneline` returns this plan's commit → **skip to TASK B (backup), then TASK G (the flip).** ⚠️ **Not to Task F — Task F is the commit and it has already happened.** ⚠️⚠️ **And do NOT skip Task B: the backup now runs adjacent to the flip, so in this state NO backup exists yet — correctly, because nothing has touched the DB.**
> 3. **Docs modified-uncommitted** — porcelain non-empty → **HALT and report.** ⚠️ **Recovery procedure, so this state routes somewhere:** run a per-edit `grep -F` sweep of all twenty-two AFTER texts against the three files and report **which landed and which did not**. ⚠️ **DEPOSIT that table at `knowledge/qa/evidence/gate2-298-2026-08-03/resume-sweep.txt` in your own tree — chat output is not a durable artifact, and this table is the only record of which edits landed.** The CEO then directs restore-and-redo or complete-forward. **Do not restore on your own initiative.** ⚠️ **This state also covers partial edits; state 4 does NOT.**
> 4. **Resume with backup, tree clean** — a `pre-298-` backup exists **AND** a Step-2 dev-log from a prior dispatch exists **AND** porcelain is clean → **reuse the backup, do NOT overwrite**; proceed to A1. ⚠️ **"Partial edits" is deliberately NOT a trigger here — that is state 3.** A partially-edited tree cannot pass A1's authoring pins, so routing it here would guarantee a HALT one task later and disguise state 3 as a resume.
> 5. **⚠️ Fresh run, but a `pre-298-` backup EXISTS and there is no evidence this plan ran** → **HALT.** An unexplained backup under this plan's prefix means something else wrote it or a prior dispatch vanished without trace. **(287/291 carry this guard; it is deliberately restored here.)** ⚠️⚠️ **THIS GUARD IS NOW SHARPER THAN IT WAS.** With the backup relocated adjacent to the flip, **a `pre-298-` backup can only exist if the flip was already ATTEMPTED** — it is no longer a routine early-step artifact. **An unexplained one is therefore evidence of an attempted corpus mutation, not of a harmless aborted setup.** Treat it accordingly.
> 6. **Flip already done** — the sixteen read `implemented` → **verify this plan's doctrine commit exists** (C4 says docs precede the flip, but a crash may have violated it), then skip to the Output Receipt and report complete.
>
> **⚠️ TASK A1 — RE-VERIFY THE AUTHORING PINS BEFORE EDITING.** `shasum -a 256` the three files against the pins in Step 1's Task S0. **Any mismatch → HALT.**
>
> **⚠️⚠️ THREE ENVIRONMENT FACTS — every one observed, not predicted.**
> **(1) `grep` is a ugrep shim; a pattern beginning with `**` is a REGEX ERROR** printing to stderr and **NOTHING to stdout** — which reads as "not found → PASS" having verified nothing. **Use `grep -F` for every literal.** Never pipe to `head`.
> **(2) Shell state does NOT persist between commands.** Assign and use in the same invocation (join with `&&`). An empty `$TS` writes `status_updated_at=''` and **exits 0**.
> **(3) zsh aborts on an unmatched glob, and both remedies fail** — `2>/dev/null || true` does not suppress a shell-level expansion error, and `NULL_GLOB` degenerates `ls -t <glob>` into a bare `ls -t` listing the cwd. **Use `find`, never a glob.**
>
> ⚠️⚠️ **TASK B (BACKUP) DOES NOT RUN HERE. It runs immediately before Task G — see below.** A backup taken before the twenty-two doctrine edits and a git commit is separated from the write it exists to invert by an arbitrarily long stretch, during which **a lessons-forge cycle may legitimately write foreign rows** (precondition 3). Restoring such a backup would roll back that cycle's real work. **Backup and flip are adjacent, or the restore is not an inverse.**
>
> **TASKS C–D — APPLY E1–E22** exactly as blueprinted. ⚠️ **Before applying each edit, confirm the blueprint's AFTER text matches this plan's AFTER text for that edit** — if they differ, HALT; the blueprint drifted and QA would not catch it until after commit. **Verify each edit landed via `grep -F` or `shasum`, never a file-tool read.** ⚠️ **For E1, a REPLACEMENT: assert the OLD parenthetical is GONE *and* the new text is present (C13).**
>
> **⚠️ TASK E0 — PRE-COMMIT RE-VERIFY. RUN BOTH FORMS — neither alone works.** Immediately before Task F:
> - **(a) PATH-SCOPED:** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- <the three doctrine paths>` → expect exactly those three modified.
> - **(b) UNSCOPED, AS A DENYLIST — not an allowlist:** `git -C /Users/marklehn/Developer/GitHub status --porcelain` → **HALT if ANY root-level `*.md` other than the three appears.** Report everything else you observe (a moved `lessons-forge` gitlink is expected — Step 1's blueprint commit and your own dev-log deposit both move it) **without failing on it.**
>
> ⚠️ **The denylist form is deliberate.** Whether the root sees a modified gitlink at all depends on whether you are running inside a bellows worktree overlay, **which this plan cannot determine before dispatch.** An allowlist that guesses the topology fails in both directions — too tight false-HALTs a correct run, too loose lets a foreign edit through. **A denylist on root `*.md` is checkable without knowing the topology, and root `*.md` is exactly the blast surface this plan writes into.**
>
> ⚠️ **A1 was taken at the START of this step; a foreign edit landing since then would otherwise be swept into this plan's commit and then certified by QA row 0b.** ⚠️⚠️ **AND THE TWO FORMS ARE BOTH REQUIRED FOR OPPOSITE REASONS: the path-scoped form structurally CANNOT see a foreign edit, which is E0's whole purpose; the unscoped form WILL show a modified `lessons-forge` gitlink, because Step 1 committed the blueprint inside that submodule — so an unscoped-only check with a "any fourth path → HALT" rule false-HALTs every correct run.** **[EXECUTED HERE — 2026-08-03] root porcelain was clean at authoring, so the gitlink move is attributable to Step 1 and to nothing else.**
>
> **⚠️⚠️ TASK E1 — PIN DOC_SHA BEFORE THE COMMIT, NOT AFTER IT.** Immediately after E0 and **before any `git add`**, compute `shasum -a 256` of the three files and record them as **DOC_SHA**. ⚠️ **DOC_SHA taken AFTER the commit certifies whatever the commit contains — including a foreign write that landed in the E0→F window.** Pinning before makes the commit a *validated* write instead of a laundering step.
>
> **TASK F — COMMIT, BEFORE TOUCHING THE DB (C4).** **Path-scoped to exactly the three doctrine paths (C14) — never `git add -A`.** Record per-file `git diff --numstat`.
>
> **⚠️ TASK F2 — POST-COMMIT VERIFY (closes the last D window).** For each of the three paths, run `git show HEAD:<path> | shasum -a 256` and byte-compare against **DOC_SHA**. **Any mismatch → HALT: a write landed between E0 and the commit and is now inside this plan's commit.** ⚠️ **This is the only check that sees that window; QA row 0b cannot, because it compares the live tree against DOC_SHA and both would already agree.**
>
> **⚠️⚠️ TASK B — BACKUP. RUNS HERE, IMMEDIATELY BEFORE THE FLIP — NOT EARLIER (see Tasks C–D).** `.backup` to a path prefixed `pre-298-` at the canonical absolute DB path, with `busy_timeout` set (C15). **FIND it via `find`, do not reconstruct its name.** Guard with `ls -la` — an empty `$BK` makes `.backup ''` exit 0 and write nothing. **Adjacency is the point: the backup must invert exactly one write, and the only DB write this plan makes is the flip below.**
>
> **TASK G — THE FLIP. ONE transaction, and the outside-range capture is INSIDE it:**
> ```
> BEGIN IMMEDIATE;
>   -- capture P' FIRST, inside the transaction: this is what makes row 24's
>   -- "same-instant set identity" structurally true rather than aspirational
>   SELECT id FROM lesson_proposals WHERE id NOT BETWEEN 207 AND 222 ORDER BY id;
>   UPDATE lesson_proposals SET status='implemented', status_updated_at=<TS>, status_updated_by='ceo'
>   WHERE id BETWEEN 207 AND 222 AND status='proposed';
>   -- both assertions here, before COMMIT
> COMMIT;
> ```
> ⚠️ **BEFORE COMMIT, assert BOTH (C12): `changes()` == 16, AND `status_updated_at` GLOB-matches a timestamp on all sixteen. ROLLBACK and HALT on either.** Rowcount alone cannot see an empty `$TS`. Then read back all sixteen per-id and deposit the RAW output.
>
> ⚠️⚠️ **FORENSIC SIGNATURE — A ROWCOUNT BELOW 16 IS MOST LIKELY NORMAL, NOT CORRUPTION.** Precondition 3 states that a lessons-forge cycle running inside the verdict gate is this shop's normal behaviour and **may legitimately stale one of the sixteen**. On `changes() < 16`, after the ROLLBACK, **identify WHICH ids are no longer `proposed` and report their current status.** If a missing id reads `stale` or `superseded`, that is **precondition-3 realisation** — report it as such and let the CEO re-scope the range; it is not corruption and the remedy is not a restore. If a missing id reads `implemented`, an in-window Gate-2 ran (precondition 2) and the remedy is entirely different. **The rowcount alone cannot distinguish these; do not report "the flip failed" without naming which.**
>
> **⚠️ DEPOSIT THE OUTSIDE-RANGE ID SET** captured inside the transaction above, to raw evidence, and record the path in your dev-log. ⚠️ **It MUST be the in-transaction capture, not a fresh query after COMMIT** — a post-commit read is not same-instant with the flip, and a cycle inserting or modifying a foreign row in between would land inside the pinned set. ⚠️ **QA row 24 compares row images against THIS pinned set and cannot construct it itself** — by Step 3 an in-window cycle may have added ids that were never in scope. A requirement with no producer is a requirement with no home (Rule 54).
>
> **Output Receipt required** — every file modified, the DOC_SHA triple, the numstat deltas, the flip rowcount.
>
> **Deposits:**
> - `knowledge/development/dev-log-gate2-298-step-2-2026-08-03.md`
> - `knowledge/qa/evidence/gate2-298-2026-08-03/flip-readback.txt`
> - `knowledge/qa/evidence/gate2-298-2026-08-03/outside-range-ids.txt`
> - `knowledge/qa/evidence/gate2-298-2026-08-03/resume-sweep.txt`
>
> ⚠️ **`resume-sweep.txt` is produced ONLY on A0 state 3** and is named here so that, if that path fires, the deposit is in scope rather than an unnamed surprise. ⚠️ **The three doctrine files are modified in the ROOT repo, not this tree, and are therefore NOT deposits of this step** — they are committed at Task F and verified at Task F2.

## STEP 3 — QA

---

> **FIRST — Deliverable Verification (Rule 8 / Rule 17).** Open the Step-2 dev-log, confirm its Output Receipt is Complete, then verify every file it claims to have modified exists and carries the described change. Table: `| Deliverable | Expected | Status (✅/❌) | Evidence |`. Any ❌ → report and HALT; make no edits yourself.
>
> **MANDATORY — Rule 20 self-check (canonical block, Checklist #4 — the exact template, NOT a paraphrase).** Run the canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path). Fill: `plan_slug`: `gate2-298-2026-08-03`; `qa_report_path`: `<your-own-tree-abs>/knowledge/qa/gate2-298-qa-2026-08-03.md`; `evidence_dir`: `<your-own-tree-abs>/knowledge/qa/evidence/gate2-298-2026-08-03/` (derive from `pwd`, NOT hardcoded); `required_evidence_files`: `[doc-integrity.txt, db-invariants.txt, pytest_targeted.txt]`. Deposit all three BEFORE running the block. **Include the block's literal stdout: the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line must both appear byte-exact (em-dash U+2014).**
>
> ⚠️ **THOSE TWO STRINGS ARE QUOTED DELIBERATELY, AND THAT IS THE §3 SCOPE WORD WORKING AS DESIGNED.** `plan_lint` check (c) does a WHOLE-PLAN substring search and HARD-FAILS if either is absent; the QA step is where they must live. The prohibition is scoped to the `## Drafting Cycle` block — the RECORD. ⚠️ **This plan AMENDS §3 (E10), making the distinction MORE load-bearing: E10 adds that the prohibition applies reflexively, and that reflexivity is likewise scoped to the record.** Do not "apply 215" by removing them.
>
> ⚠️⚠️ **REPORT STRUCTURE — THE VERIFICATION SECTION NEVER CLOSES, SO CLOSE IT YOURSELF** (`297:446`). `in_verification_section` is **never cleared by a `###` or `####` heading.** **Immediately after the verification table, write exactly `## Evidence and Narrative`**, and keep the Rule 20 stdout, the Output Receipt and `### Ledger Updates` under `##`-level headings. A `####` block placed after the table stays inside the verification scope, is scanned for hedging keywords, and never reaches the ledger channel.
>
> **Evidence rule:** deposit RAW command output, never a summary.
>
> **⚠️ EVERY DB QUERY USES THE CANONICAL ABSOLUTE PATH** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`, read-only (`file:…?mode=ro`). **The DB is gitignored and does NOT exist in your worktree**: a bare `sqlite3 lessons-forge.db` silently CREATES an empty file and fails `no such table` — or you "recover" against another store and verify a corpus that was never flipped. Read the backup read-only (`?immutable=1`).

**Verification table, one row per claim (HALT on any FAIL):**

> **0a. Blueprint identity.** `shasum -a 256` the committed blueprint; compare against the hash the dev-log records reading. Mismatch → HALT.
>
> **0b. DOC INTEGRITY.** `shasum -a 256` all three files against **DOC_SHA**; `git status --porcelain -- <the three paths>` must be **EMPTY**. Any mismatch → HALT: every row below greps the LIVE files.
>
> **1. Line-delta bounds — against the BLUEPRINT, not the dev-log.** Re-derive `git diff --numstat` per file for this plan's commit and compare against **the expected deltas the SA recorded in the blueprint**. ⚠️ Comparing against the dev-log is circular — the agent that made the edits also writes that number. Independent referent **(ii)**.
>
> **2. E1 POST-CONDITION (C13).** The OLD parenthetical is **ABSENT** *and* the new rotation text is **PRESENT** — `after != before`. A presence-only row certifies a fold that never landed.
>
> **3–18. Per-proposal content rows — one per CONTENT edit** (E2–E10, E13, E14, E15, E16, E17, E18, E22 = 16 rows), each asserting its specific AFTER text via `grep -F`. Independent referent **(i)**.
>
> **19. The 211 + 219 PAIR (`297:82`).** E22 and E13 verified together; either alone is a FAIL.
>
> **20. THE FENCE PIN (C3).** Run the exact extraction command from CEO Context; confirm the file still has exactly two fence lines; compare the hash against the **authoring-pinned `BLOCK_SHA` `d399f933…`** — **not** against any value the dev-log supplies. Independent referent **(iii)**.
>
> **21. E10 did not disturb what E9 depends on.** Confirm §3's no-running-tally prohibition is byte-present after E10. ⚠️ E9 asserts that prohibition is unchanged while E10 edits the same section; nothing else checks it.
>
> **22. Version + changelog integrity.** `DRAFTING_CYCLE.md` reads **1.4 (2026-08-03)**; `PLANNER_TEMPLATE.md` reads **4.83** at both `:5` and `:6`. ⚠️ **Prior rows INTACT:** `grep -Fc '1.3 (2026-08-02)'` → **1** (down from 2) and `grep -Fc '4.82'` → **1** (down from 3). ⚠️ **AND row-count both changelog tables against their AUTHORING baselines** — the version-string counts guard only the immediately-prior row, leaving every older row unprotected. ⚠️⚠️ **THE COUNT IS METHOD-DEPENDENT, SO THE METHOD IS PART OF THE PIN — use these commands exactly:**

~~~
awk '/^## History/{f=1;next} f&&/^## /{f=0} f&&/^- /{n++} END{print n+0}' DRAFTING_CYCLE.md          # baseline 4  -> expect 5
awk '/^## Lessons Learned/{f=1;next} f&&/^## /{f=0} f&&/^\| 20/{n++} END{print n+0}' PLANNER_TEMPLATE.md  # baseline 105 -> expect 106
~~~

⚠️⚠️ **BOTH COMMANDS ARE HEADING-ANCHORED, NEVER LINE-NUMBERED — and that is load-bearing here.** **[EXECUTED HERE — 2026-08-03] E16/E17 insert Rules 63 and 64 immediately after Rule 62 (`:1125`), roughly 770 lines ABOVE `## Lessons Learned` (`:1898`)** — so this plan's own edits shift that section down, and any `NR>…&&NR<…` range would name the wrong span by QA time. **The heading-anchored form was verified at authoring to return the same 105 as the range it replaced.**

**[EXECUTED HERE — 2026-08-03] Method sensitivity, measured:** `## History` returns **4 under all three** candidate methods (`^- \*\*`, `^- `, any non-blank) — insensitive. **`## Lessons Learned` returns 105 / 107 / 109** depending on whether the header and separator rows are counted. **"105 → 106" is true under exactly ONE method**, so a QA agent counting any other way fails a correct run. ⚠️ **This is the same defect class as an unstated fence-extraction method, swept to its sibling site.**
>
> **23. FLIP.** Per-id read-back of 207–222: `status='implemented'`, `status_updated_by='ceo'`, `status_updated_at` non-empty and GLOB-matching. **Exactly 16 rows.**
>
> **24. BLAST RADIUS AT VALUE LEVEL, AGAINST A PINNED ID SET.** ⚠️ **Do NOT compare an open-ended "everything outside 207–222."** **[EXECUTED HERE — 2026-08-03] `MAX(id)` = 222 and `COUNT(*)` = 222**, so any proposal a cycle creates in-window lands at 223+ and would change an open-ended outside-range image on a **correct** run — the exact false-HALT `297:26` warns about. **Read the outside-range id set THE DEV DEPOSITED at Task G** (raw evidence, path recorded in the dev-log) **and compare row images only for those ids.** ⚠️ **Do not construct the set yourself — by the time you run, an in-window cycle may have added ids that were never in scope, and re-deriving it here would silently re-open the open-ended comparison this row exists to close.** Same-instant set identity; every foreign non-`implemented` row byte-identical. ⚠️ **A count cannot see a row moving between two non-NULL values.**
>
> **25. Category preserved and NON-UNIFORM** — 222 remains `instrumentation`, the other fifteen `governance_rule` (C7).
>
> **26. Targeted tests** — the lessons-forge suite; zero regressions against the recorded baseline.

**Then `## Evidence and Narrative`, then the Output Receipt.**

> ⚠️⚠️ **`### Ledger Updates` — THE CHANNEL HAS FIVE DOCUMENTED FAILURE MODES. All five are guarded here.**
> - **Author it via `Write`/`Edit`, EXACTLY ONCE, complete, and NEVER re-edit it.**
> - **End it with a blank line after its last subsection's content** — a subsection flush against the end of the edit absorbs the next chat part, and **the exposed one is always the LAST subsection**.
> - ⚠️ **The daemon parses `_all_assistant_text` — assistant text plus `Write` content plus `Edit` strings, and NOT Bash.** A ledger block written by a Python file-write or a heredoc is **invisible to the channel**.
> - **It must sit at `##`-level scope, after `## Evidence and Narrative`** — never inside the verification section.
> - **The substance goes INSIDE the section, not above it** — a well-formed block one heading too high is discarded silently (session-18 failure mode).
> - `#### Prompt Feedback` belongs in the same section.
>
> **`#### Forward Register` — one row per bullet, contiguous:**
> - `PLANNER_TEMPLATE.md` Rule 55 — a recorded PID goes stale across a daemon restart, so `ps -p` on a stale record reports a live process as dead; the positive confirmation must resolve, and the record be re-established when it does not. Measured 2026-08-03: recorded pid 86216 dead, live daemon 96240. ⚠️ **Those PIDs are a point-in-time observation and are evidence, not current state — any liveness check you need must be re-run now, never inherited from this line.**
> - `sanitize_items` retains a literal leading `- ` on appended rows, so rows after the first render inconsistently with row 1.

**Deposits:**
- `knowledge/qa/gate2-298-qa-2026-08-03.md`
- `knowledge/qa/evidence/gate2-298-2026-08-03/doc-integrity.txt`
- `knowledge/qa/evidence/gate2-298-2026-08-03/db-invariants.txt`
- `knowledge/qa/evidence/gate2-298-2026-08-03/pytest_targeted.txt`

---

## Drafting Cycle

**Tier:** T2 — triggers fired: T-6 (governance surface: three doctrine files), T-8 (novel: no edit map for this batch).

- **Weak spots:** w1 6 folded; w2 7 folded (a resume state routed to the commit task instead of the flip; the flip guarded rowcount but not timestamp validity; the edit count was short by two; the SA had no pin) — verified negatives in both walks.
- **Destruction:** w1 4 folded, w2 3 folded. The §2 deletion was found to reverse a deliberately-preserved element of a prior arc; premise declared in advance. A title-widening sweep was EXECUTED and returned nil inside doctrine.
- **Vulnerabilities:** w1 4 folded, w2 3 folded — including a pin whose extraction method was unstated and therefore unreproducible, and a mandated command that quoted the delimiter it searched.
- **Integration-vs-record:** w1 4 folded, w2 5 folded — the ledger channel's protocol had been carried as one sentence where the newest sibling carries five guarded failure modes.
- **ACID:** a1 12 findings, a2 11 findings, each run alone against the merged draft. **a1: 6 of 9 substantive findings were introduced by the culmination immediately preceding it** — including two circular referents inside the very fold that existed to remove circularity. **a2: 8 of 8.** The proportion rose as the inherited regions were walked and the new machinery was not.

**Conflicts:** C13 (post-condition assertions) vs the inherited presence-row form — joint-resolved in one move by rewriting the rows. A5 records a deletion that must NOT be reversed.

**Sweeps:** ⚠️ **Two fold-sweep failures were measured and both are now swept to every site.** (1) *a pin taken at a step's START does not protect writes landing at its END* — fixed in Step 2 (Task E0), missed in Step 1, now fixed there (Task S9). (2) *a pin whose method is unstated is unreproducible* — fixed for the fence extraction, missed for the changelog row counts, now fixed there. **In both cases the fix and the unswept sibling were authored in the same edit session.**

- **ACID a3 (CEO-scoped to sub-question 5.3 — determine the serializable schedule order):** 4 findings, 3 HIGH. DOC_SHA was pinned on the wrong side of the commit, leaving the E0→commit window able to launder a foreign write through QA's own integrity row; the outside-range capture was not same-instant with the flip it certifies; and the backup sat an arbitrary interval away from the only write it inverts. **The order is now fixed as C16 and is conflict-serializable per object.** ⚠️ The low count records the narrow scope, not the artifact's state.

**Closing:** four walks and three ACID passes have run; culmination 5 applied the schedule reordering. ⚠️ **Walk 4 — the first pass over an artifact with no unexamined region, and therefore the first whose dry result would have meant anything — was NOT dry**, and both its HIGHs were fixes from culmination 4 breaking what they repaired. **The CEO reviewed the measured curve (18 / 12 / 18 / 11 / 13 / 8 across six phases, with culmination-introduced defects rising from 6-of-9 to 8-of-8 to 2-of-2 HIGH) and directed a scoped close: fold walk 4's two HIGHs only — both single-line textual corrections with no design content — then settle the schedule order.** That is what this draft is. **The five MEDIUMs and one LOW from walk 4 are record-integrity items that do not change what executes, and they are deliberately NOT folded — named here rather than silently dropped: A6's relaxation count, the C13 scoping declaration, rows 3–18 enumeration, the incomplete inherited-claims block, the scratch-directory absence assertion, and the A5/A6/A7 ordering.**

⚠️⚠️ **ONE EARNED `plan_lint` WARN, DEPOSITED WITH IT RATHER THAN SILENCED: *"T2 plan missing cold-panel line in Drafting Cycle block."* IT IS TRUE.** §2.6 runs the cold panel **after the sequential walk goes dry**, and this walk never went dry — so no cold panel ran and there is no honest line to write. **Authoring one to clear the WARN is precisely the wording-satisfies-the-check defect E10/215 codifies in this very plan.** ⚠️ **The §5 mechanical conformance pass was run at deposit: three `(b) step deposits` FAILs were found and FIXED (the `**Deposits:**` blocks were missing entirely); all other checks PASS.**

**Prior closing state, retained for the record:** three walks and two ACID passes had run; culmination 4 applied thirteen findings. ⚠️ **The finding curve ran 18 / 18 / 13 and that decline is NOT read as convergence** — it records that the inherited regions have been walked three times while the newest machinery was walked once. **Every section has now been read by lenses 1–4, so after this culmination no unexamined region remains — the next walk is the first one whose dry result would mean what it says.** **This plan is NOT ready for deposit.**
