# Executable: Gate 2 batch 1 — the §3 walk-register doctrine amendment (proposal 312 / bellows Forward row 51): DRAFTING_CYCLE v2.1 → v2.2, then flip 312 to `implemented`

**Type:** Executable
**Project:** lessons-forge
**Depends on:** **executable-342** (lessons-forge, Done — the Gate-1 routing plan that WROTE `status='accepted', route='codify'` on proposal 312; its transaction stamped `status_updated_at='2026-08-11T13:42:09+00:00'`, the exact value this plan's G2 sentinel pins as the prior-value exclusion and A0 branch 5 checks ⚠️ **note the representation: an OFFSET-form timestamp, NOT the `Z` form the clone origin pinned** — see Environment fact 5), **executable-330** (lessons-forge, Done — the clone origin: the newest true Gate-2 codification batch, from which the A0 state machine, the backup/rehearsal/sentinel/read-back mechanism and the QA table are cloned), executable-338 (bellows, Done — shipped `knowledge/architecture/walk-register-schema.md`, which E1's AFTER text cites as the register's conforming schema; a live-existence precondition checked at A1), DRAFTING_CYCLE.md at v2.1 (precondition, checked at A0)
**Created:** 2026-08-11
**Author:** Planner
**Slug:** `gate2-s3-register-2026-08-11` (authoring-time; stable across any crash-redo re-deposit — the A0 re-entry key and the Rule 20 `plan_slug`)
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T2
**qa_steps:** 2
**Test Scope:** targeted (Rule 21 — see the justification below)

⚠️ **ID NOTE — the deposit filename is decided AT DEPOSIT.** Slug+date name form; id read from `id_sequence` at deposit, never at authoring (the thrice-proven consumed-in-window class; `next_id` read **344** at authoring, which is a PREDICTION and not a pin).

---

## Why this exists — doctrine describes a practice the shop retired, and four rules point at a file the doctrine says will not exist

Proposal **312** (entry 304, `governance_rule`, confidence `high`, routed `accepted|codify` at Gate 1) and **bellows Forward row 51** are one edit. §3 currently states that full walk-by-walk analysis lives in a scratch file that is *session-local and ephemeral*.

**That claim is false, and it was measured false rather than argued false** (2026-08-11, at source):

- **Four walk registers are COMMITTED** under `governance/knowledge/research/` — `group4-rescope`, `cycle-run-339`, `lint-class-recall`, `walk-register-schema` — all dated 2026-08-10.
- **Exactly one register is uncommitted**, at `scratchpad/walk-register-gate2-s5-conformance-2026-08-09.md`, in a directory `git status` reports as `?? scratchpad/`. It is the **oldest** of the five.
- So this is not doctrine-vs-practice divergence holding steady. **Practice already moved**, on 2026-08-10, and every register written since is committed. Doctrine describes the retired behaviour.

**The defect is not cosmetic, and this is the part a naming sweep alone would miss.** Four separate rules in this file direct per-finding detail *to* the register: §2.6's fold-note attribution, §2.7's per-fold evidence detail **and its closing-record re-read**, §2.8's region tally, and §3's own judged-stop residue clause. If the register is genuinely ephemeral, each of those is a **DELETION rather than a relocation** — and the closing-record re-read, which §2.7 mandates at *every* close, is a cross-session read by construction and therefore unreachable. Plan 338's record is the live proof in the other direction: the bytes that repaired its walk register were recovered **from the walk-0 commit**, which an ephemeral register would not have had.

**Provenance of the wrong clause, measured:** `git log -L 142,142:DRAFTING_CYCLE.md` returns **`3c327e3` [287]**. The sentence has survived amendments 298, 309, 330, 334 and 343 unexamined — it is old, not recently introduced, and nothing since has read it.

**Routing:** the corpus path proper (§6 amend-only-through-the-corpus) — LESSONS.md → forge ingest → cycle 311/342 classification → Gate 1 route `codify` → this Gate-2 plan. **No §6 deviation to declare.** ⚠️ A DRAFTING-CYCLE deviation IS declared and is recorded in the `## Drafting Cycle` block below with its cost — it is a *partial* deviation (the §2.0 context pin ran; the walks did not), taken on measured evidence, and it is not the same act as 343's.

⚠️ **Forward row 51 is NOT closed by this plan's Output Receipt.** Row 51 lives in **`bellows/knowledge/FORWARD.md`**, and `_append_forward_row(project_path, …)` resolves a Receipt emission to **`<project>/knowledge/FORWARD.md`** — this plan's project is lessons-forge, so its Receipt cannot reach bellows' register, and Rule 42 authorises **status updates only**, performed Planner-direct at session wrap. Row 51's flip to `closed-by-plan-<id>` is therefore a **wrap action, not a step action**. No step of this plan touches any FORWARD register. Its `#### Forward Register` section reads `NONE`.

## Scope — one doctrine file, seven edits; one scoped 1-row flip; nothing else

- **Edits exactly ONE existing file:** `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` (root repo), via edits E1–E7 below. The AFTER text is GIVEN — the agent PLACES it, never composes it.
- **One DB write:** a scoped `UPDATE` flipping proposal **312** `accepted → implemented` at the canonical absolute path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`.
- **No code edit.** No `.py`, no gate, no template, no other doc. Needing one means the premise failed → HALT. (The two declared `.sql` deposit files are DATA for sqlite `.read` — writing them is in scope, not a code edit.)
- ⚠️ **§6 coordinate-doctrine-and-gate: NO gate edit is owed, and this is discharged BY MEASUREMENT, not by assertion** (2026-08-11): `grep -cF` over `bellows/scripts/plan_lint.py` and `bellows/gates.py` returns **0** for `scratchpad`, **0** for `walk register`, **0** for `walk_register` in both files. **Positive control on the same instrument and file: `Drafting Cycle` in `plan_lint.py` = 11.** The amendment touches §3 prose only and changes nothing `plan_lint` parses; §4 is unchanged and remains in lockstep. Re-verified at QA row 8.
- **No LESSONS.md touch.** No step reads or writes it.
- **No FORWARD register touch** by any step (see the note above). No `walk-register-*.md` file is created, moved or committed by this plan — **the amendment states where registers belong from now on; it does not migrate the existing five.** Migrating the one uncommitted register is deliberately OUT of scope: it belongs to a closed plan's cycle, and moving another plan's record is not this plan's authority.
- ⚠️ **DOWNSTREAM EFFECT OF THE FLIP, NAMED — it is not status-cosmetic.** `accepted` is NOT in `_TERMINAL_STATUSES`; `implemented` IS (`lessons-forge/src/lessons_forge.py:31`, read 2026-08-11: `frozenset(('implemented', 'rejected', 'superseded', 'reference'))`). A later EDIT to entry 304 will therefore be **flagged** rather than **staled**, and will no longer re-queue for re-proposal. **That is the intended meaning of "codified" and the reason the flip exists** — but it is a live behavioural change to a consumer, so it is stated here and VERIFIED at QA row 9 rather than assumed.
- ⚠️ **THE 74-ROW STALE HAZARD — the standing Gate-2 guard, and this plan's PRE check is where it fires.** Because `accepted` is non-terminal, a lessons-forge ingest run before Gate-2 codification silently stales every `accepted|codify` row. **Measured at authoring: 74.** G1's rehearsal asserts `ACC=74` **before** any write; **fewer than 74 → HALT, do not proceed on the remainder** (bellows Forward row 12 records the underlying defect). Proceeding on a reduced set would codify a corpus that had already lost rows.
- ⚠️ **The doctrine edit lands in the REAL governance root, outside any bellows worktree** — `_gate_scope_check` is cwd-scoped and cannot see it; the QA doctrine-integrity rows are the only guard and they fail closed. Every command touching the doctrine file uses the ABSOLUTE operand. **PLACEMENT vs VERIFICATION tooling (explicit license):** file tools (Read + Edit) MAY be used to PLACE the edits — E1's ~1,300-char single-line AFTER text is quoting-hostile to sed/perl; VERIFICATION is Bash-only (`grep -F` / `shasum` / `awk`), never a file-tool read.
- ⚠️ **Verdict-window posture:** from the Step-1 doctrine commit until close, v2.2 GOVERNS the shop. A HALT holds it live for the CEO — never `git restore`/`revert` anything on a HALT; the root repo carries unrelated working state and a parallel terminal may be live. Rollback is a CEO decision, not an agent action.
- **Deposit basenames are DECLARED — do not re-date any at run time** (the 320/329 clause); the only place a live date appears is G2's in-statement `strftime`.
- ⚠️ **Expected `plan_lint` state at deposit:** recorded in the `## Drafting Cycle` block's Conformance paragraph, measured at the DEPOSIT PATH before the copy (the lint state is location-dependent — `project_root` is the path before `/knowledge/`). Any WARN or FAIL not named there is unexplained → do not deposit.

### Rule 21 — justification for `Test Scope: targeted`

This plan changes **no source code**: its deliverables are prose edits to one governance markdown file plus one scoped single-row `UPDATE`. No module, schema, or route is touched, so a full-suite run would exercise nothing this plan can break. **Targeted scope = the lessons-forge suite** (`lessons-forge/src/test_lessons_forge.py`), which covers the corpus helpers that read `lesson_proposals` — and, this repo having a single test module, the targeted run IS the full run. ⚠️ "Targeted = full" is a **PREMISE about the repo's shape, not a fact about this plan**: `find` over `src/` returned exactly `test_lessons_forge.py`, measured 2026-08-11. QA row 7 re-derives it at run time rather than inheriting it, because a second test module added before dispatch would silently make the targeted run a partial one. ⚠️ Per the DEV-step lesson the suite is deliberately NOT authored into Step 1; it lives in QA.

### ⚠️ Environment facts — observed, not predicted

1. `grep` is a ugrep shim: **`-F` for every literal**; a non-`-F` search can exit 1 SILENTLY on a present line. A zero-match `grep -c` prints `0` and exits 1 — the printed count is the assertion; do not `&&`-chain zero-count probes.
2. Shell state does NOT persist between commands — assign and use in the same invocation. (The flip's timestamp is computed in-statement, so no shell variable carries it; the one shell variable the plan uses — Task G's scratch dir — is created and consumed in the same invocation.)
3. zsh aborts on an unmatched glob and both remedies fail — use `find`, never a glob.
4. The DB is **gitignored and absent from any worktree**: a bare relative `sqlite3 lessons-forge.db` silently CREATES an empty file. Canonical absolute path only; every read-only query uses the single `-readonly` form fixed below.
5. ⚠️ **THE CORPUS CARRIES FOUR TIMESTAMP REPRESENTATIONS, and a probe cloned from 330 would be a confident false negative.** Measured 2026-08-11 across all 314 rows: `Z`-form **147**, `+00:00` offset-form **99**, and 68 legacy rows in two further shapes (`2026-05-13T14:23:18`, `2026-05-13 16:07:24`). The 74 `accepted|codify` rows split **exactly on the Gate-1 boundary — 42 `Z`-form (written by plan 326) and 32 offset-form (written by plan 342)**. **Proposal 312 carries the OFFSET form.** Verified empirically rather than reasoned: 330's `Z`-terminated GLOB run against 312's live value returns **0**. Consequence, and it is favourable: because the prior value is structurally non-matching, the `Z`-GLOB alone is already a value guard here — but the explicit prior-value exclusion is kept as defence in depth, **pinned to the real value `2026-08-11T13:42:09+00:00` and NOT to the clone origin's `2026-08-09T01:20:01Z`, which matches nothing in this corpus.**

---

## The seven edits — AFTER text GIVEN

⚠️ **READ THIS BEFORE PLACING ANYTHING.** Line 142 is a **710-character single physical line carrying FOUR independent rules** — the compact-form mandate, the register-location clause, the fold-count prohibition, and the record-not-instructions rule. E1 replaces **only the second of the four**, starting at **column 90**. It is a **mid-line surgical replacement**, not a paragraph swap. An anchor on the section heading, or any edit keyed to "the paragraph", destroys three rules this plan never intended to touch. *(This exact geometry — an anchor matching an earlier mention of a heading — destroyed a draft on 2026-08-11; it is the reason the pin measures start columns.)*

**E1 — §3 line 142, MID-LINE clause replacement.** Anchor (unique, `grep -cF` = **1** measured 2026-08-11) — replace this exact substring, and nothing outside it:

> `Full walk-by-walk analysis lives in a scratchpad file (\`scratchpad/\`, session-local and ephemeral); only the per-lens summary lines appear in the plan's \`## Drafting Cycle\` block.`

with:

> Full walk-by-walk analysis lives in the **walk register — an OUTPUT of the cycle, not a scratch buffer**: a file named `walk-register-<plan-slug>.md`, conforming to the walk register schema (`bellows/knowledge/architecture/walk-register-schema.md`), **committed per phase alongside the draft** and committed to `governance/knowledge/research/` regardless of which project the plan targets — the register is a governance record, not a project deliverable; only the per-lens summary lines appear in the plan's `## Drafting Cycle` block. **The register must outlive the session, and that is what makes the rules pointing at it executable:** every rule in this file that directs detail there — §2.6 fold-note attribution, §2.7's per-fold evidence detail and the closing-record re-read, §2.8's region tally, and the judged-stop residue below — is a DELETION rather than a relocation if the register does not survive the session, and the closing-record re-read is a cross-session read by construction. **When a rule directs detail to another location, verify that location outlives the reader the rule anticipates.** (Proposal 312 / bellows Forward row 51, codified 2026-08-11.)

⚠️ **C11 post-condition for E1:** the three co-tenant rules on line 142 must survive byte-intact — `grep -cF "The compact form is **load-bearing**"` → 1, `grep -cF "Do not keep a running fold-count in the Cycle Log"` → 1, `grep -cF "record, not instructions"` → 1. All three measured present before AND after on the authoring dry-run.

**E2 — §3 line 146, naming sweep.** Anchor (`grep -cF` = 1): `The per-finding detail stays in the scratchpad register` → **`The per-finding detail stays in the committed walk register`**.

**E3/E4/E5 — the three dependent naming sites, ONE uniform token swap.** The literal `scratchpad walk register` counts **exactly 3** (measured 2026-08-11 — §2.7 line 38, §2.6 line 101, §2.8 line 131) → replace all three with **`committed walk register`**. ⚠️ **A replace-all is CORRECT here and is licensed only because the count was asserted first:** assert `grep -cF 'scratchpad walk register'` → **3** immediately before, and → **0** immediately after. A count other than 3 → HALT; do not swap a subset.

**E6 — version line.** LENGTHENED anchor (`grep -cF` = **1** measured): `**Version:** 2.1 (2026-08-11). Amended only through the Iteration Protocol` — within that line only, swap the version token to `2.2 (2026-08-11)`. ⚠️ The bare string `2.1 (2026-08-11)` counts **2** in the file (version line + History row); a replace-all destroys the changelog. ⚠️ The date is **deliberately the same as v2.1's** — both amendments land 2026-08-11; this is correct, not a copy error.

**E7 — History row, PREPEND as the FIRST bullet under `## History`** (ordering confirmed newest-first at authoring):

> - **2.2 (2026-08-11):** slug gate2-s3-register-2026-08-11; Gate-2 codification of proposal 312 (bellows Forward row 51) — the corpus path proper, no §6 deviation. §3: the walk register is an OUTPUT of the cycle, committed per phase to `governance/knowledge/research/` under the schema plan 338 shipped, rather than a session-scoped buffer in an untracked directory; the unit also carries the general rule that a location a rule directs detail to must outlive the reader that rule anticipates. The ephemerality clause is struck — it was written by plan 287 and survived five amendments unexamined while practice moved past it: four registers are committed under governance and only the oldest remains uncommitted. The naming reference is swept at all four dependent sites (§2.6 fold notes, §2.7 closing-record re-read, §2.8 region tally, §3 judged-stop residue), since a register that is no longer a scratch buffer must not still be called one. §6 coordinate-doctrine-and-gate discharged by measurement: the retired directory token and both spellings of the register name return 0 in both `plan_lint.py` and `gates.py` (positive control: `Drafting Cycle` in `plan_lint.py` = 11), so no gate edit is owed and §4 remains in lockstep. DB: proposal 312 → implemented (scoped one-row flip, lessons-forge). Inheritors: the `gate2-s3-register` re-draft is DISCHARGED by this row rather than resumed; the remaining Gate-2 batches (PLANNER_TEMPLATE.md, 37 items; DRAFTING_CYCLE.md, 36 items) and the §2 rewrite.

⚠️ **E7 is deliberately worded to DESCRIBE the two retired strings and never QUOTE them.** An earlier authoring revision quoted both; the dry-run caught that it left `scratchpad` at 1 and `session-local and ephemeral` at 1 **after a correct and complete edit**, which would have made QA's two strongest post-conditions unsatisfiable on a correct run. This is the clone origin's own QA-row-4 trap in mirror image, and it is why those two probes are safe to assert at 0.

⚠️ **E7 must NOT contain the string `2.1 (2026-08-11)`** (refer to predecessors by number alone) — QA's count row depends on it going 2 → 1.

**Measured line deltas [EXECUTED HERE — 2026-08-11, dry-run `git diff --no-index --numstat` on a scratch copy with all seven edits applied]: `7 added / 6 deleted`** (six lines rewritten in place — 5, 38, 101, 131, 142, 146 — plus E7's one new line). QA row 3 compares the real commit's numstat against THIS pinned pair, not against the dev-log.

---

## Conflict Ledger — run-time constraints

- **C1** — every edit anchored on a QUOTED UNIQUE string, never a line number. `grep -cF '<anchor>'` must return the count this plan states (1 for E1/E2/E6/E7; **3** for the E3/E4/E5 swap). Any other value → HALT. Line numbers in this plan are ORIENTATION for the reader, never operands.
- **C2** — the version edit is a surgical swap against the lengthened anchor; never replace-all.
- **C3** — doctrine committed BEFORE the DB flip (the 291:428 convention) — a die-between is detectable from the doctrine pins alone.
- **C4** — the backup is ADJACENT to the flip: created immediately before Task G and after the commit, so it inverts exactly one write. ⚠️ **Scoped, not absolutist** — A0 state 2 legitimately REUSES a backup from a crashed prior dispatch. The `BK=1` restorability assert is what restores this row's guarantee there. **Verification, not recency, is what makes the backup an inverse.**
- **C5** — the flip is scoped `WHERE id = 312 AND status='accepted'`; no whole-corpus predicate. `status_updated_by='ceo'` (the Gate-1 decision's actor; schema CHECK allows it).
- **C6** — `changes()` must equal exactly **1** (⚠️ **ONE, not two — this is a single-row flip and the clone origin's `=2` is wrong here**) AND `status_updated_at` must GLOB-match. Both printed as in-transaction sentinels the agent READS before trusting the run. The protection is STRUCTURAL, not conditional (sqlite scripts cannot conditionally ROLLBACK): G1's rehearsal proves the predicate matches exactly 1, the scoped `AND status='accepted'` bounds the write, and a wrong sentinel → HALT with the adjacent Task-B backup as the CEO's recovery instrument.
- **C7** — the timestamp is computed IN-STATEMENT via `strftime('%Y-%m-%dT%H:%M:%SZ','now')` — no shell variable carries it, so the empty-`$TS` failure class cannot arise for it. ⚠️ Scoped claim: Task G's stderr capture DOES use a shell variable, governed instead by same-invocation creation (Environment fact 2).
- **C8** — the outside-range capture is taken inside **G2's flip transaction, before the UPDATE** — same-instant set identity with the flip. ⚠️ **QA's comparison BASELINE is always the DEPOSITED capture — never a QA-time reconstruction of it.**
- **C9** — the commit is path-scoped to exactly `DRAFTING_CYCLE.md` at the root repo; never `git add -A`. `git -C` absolute; post-commit name-only assertion.
- **C10** — SQLite access sets `busy_timeout`; `database is locked` is a HALT, not a retry loop.
- **C11** — every verification asserts the POST-condition per edit kind: E1 (mid-line replacement) old-clause-absent AND new-present AND **all three co-tenant rules byte-intact**; E2–E5 old-token-count 0 AND new-token-count 4; E6 old-token-absent-at-line AND new-present; E7 (pure addition) new-present plus the prior first row intact immediately below.
- **C12** — **SCHEDULE ORDER IS LOAD-BEARING. Do not reorder:** A0 → A1 → E1 → E2 → E3/E4/E5 → E6 → E7 → E0(denylist) → DOC_SHA pin → F(commit) → F2(post-commit verify) → B(backup) → G1(rehearsal) → G2(flip txn: capture → UPDATE → sentinels → COMMIT) → G3(readback) → deposits. ⚠️ **E1 runs before the E3/E4/E5 swap deliberately:** E1's old text contains `scratchpad file`, not `scratchpad walk register`, so the two do not interact — but running the swap first would change the count the swap itself asserts if any future edit blurs that boundary. Order makes the assertion stable.
- **C13** — E7's History row asserts the flip in past tense from Task F onward, EARNED only at G2 minutes later in the same step; a stop inside the F→G2 window leaves it unearned, and **A0 state 2 is that half-state's designated completion path.**
- **C14** — **SERIALIZED BELLOWS DISPATCH IS AN ASSUMPTION DOING LOAD-BEARING WORK, stated rather than hidden:** two agents must not write root doctrine or the corpus concurrently. The guards that do NOT depend on it: A1's pin, E0's porcelain read, F2's content verify, G1's PRE/ACC counts, and QA rows 1/6.
- **C15** — **the 74-row stale-hazard guard is a PRE-WRITE HALT, not a report.** `ACC` ≠ 74 at G1 → HALT before the flip. It is placed in the rehearsal, not in QA, because after the flip the correct value is 73 and the hazard is no longer distinguishable from this plan's own work.

---

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

Step 1 (DEV) → verdict gate → Step 2 (QA). `pause_for_verdict: always`. No step renames this file.

⚠️ **HALT ROUTING — the inputs each step reads; if any is missing or unreadable, HALT the step that needs it and NAME it, never improvise.** **Step 1 reads** this plan file, the live `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md`, and the canonical DB. **Step 2 reads** this plan file, the Step-1 dev-log, the live doctrine file, the canonical DB (read-only form), the merged Step-1 evidence captures, and `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`. ⚠️ An unreadable deposited capture is NOT license to re-derive it — that re-opens the open-ended comparison QA row 6 exists to close; it is a HALT (distinct from the crash-recovery DECLARED FALLBACK, which fires only when the Step-1 receipt itself reports the capture lost).

---
---

## STEP 1 — DEV (place the seven edits, commit, then flip)

---

> **FIRST — post a short visible chat message (1–2 sentences) confirming you are starting this plan.** Do NOT rename this plan file. You are the Developer. ⚠️ **The doctrine edit lands in the REAL governance root at the ABSOLUTE path `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` — not in your worktree; no teardown cleans it up.** If you HALT after editing has begun, SAY SO LOUDLY in the same breath: leave the tree exactly as it is (no restore — CEO inspects), report which of E1–E7 landed and `git -C /Users/marklehn/Developer/GitHub status --porcelain -- DRAFTING_CYCLE.md`.
>
> **⚠️ TASK A0 — PRE-EDIT STATE CLASSIFICATION. Evaluate IN THIS ORDER; FIRST match wins (most-advanced-first):**
> 1. **Flip already done** — proposal 312 reads `implemented` (query at the canonical absolute DB path, `-readonly`) → verify the doctrine commit exists (`git -C /Users/marklehn/Developer/GitHub log --oneline -5 -- DRAFTING_CYCLE.md`, newest message must name the slug `gate2-s3-register-2026-08-11`; C3 says docs precede the flip, but a crash may have violated it — a missing commit here is a REPORTABLE anomaly, not a license to re-edit). ⚠️ **Then check whether the crashed run's deposits SURVIVED:** if `outside-range-ids.txt` is not in the merged tree you CANNOT reconstruct it (same-instant is unrecoverable by definition) — deposit a RECOVERY dev-log naming exactly which artifacts are missing, produce the G3 read-back fresh (that one IS reproducible), and state in the receipt that QA row 6 must take its DECLARED FALLBACK. Never fabricate a capture after the fact. Then report complete. ⚠️ The daemon's deposit-existence gate will flag the missing capture — **that gate failure is the CORRECT signal for the human read of a crash recovery, not a defect to engineer around.**
> 2. **Docs committed, flip not done** — newest doctrine commit names the slug AND 312 still reads `accepted` → **skip to TASK B (backup), then TASK G (the flip)** — NOT to Task F. ⚠️ **DOC_SHA on this path is taken FROM THE COMMIT, never from the live file** — `git -C /Users/marklehn/Developer/GitHub show <that-commit>:DRAFTING_CYCLE.md | shasum -a 256` — and your dev-log says so explicitly. A DOC_SHA hashed from the live tree here would make QA row 1's three-way agreement compare the live file against itself. ⚠️ A `pre-gate2-s3-` backup MAY already exist: rediscover it with the PREFIX-ONLY form — `find /Users/marklehn/Developer/GitHub/lessons-forge -maxdepth 1 -name 'pre-gate2-s3-*.db'` with NO `-newer` clause — REUSE what it finds; if none, run Task B normally. ⚠️ **Either way run Task B's `BK=1` restorability assert against the backup you end up holding** — creation is skippable on this path, verification is not. ALSO re-run the doctrine porcelain check: if `DRAFTING_CYCLE.md` is dirty ON TOP of the commit, a foreign edit landed post-commit — report LOUDLY and proceed to the flip (the flip never touches doctrine), never sweep it into any commit.
> 3. **Docs modified-uncommitted** — `git -C /Users/marklehn/Developer/GitHub status --porcelain -- DRAFTING_CYCLE.md` non-empty → **HALT.** Recovery route: run a per-edit `grep -F` sweep of the seven AFTER texts against the live file, DEPOSIT the landed/not-landed table at `knowledge/qa/evidence/gate2-s3-register-2026-08-11/resume-sweep.txt` (chat output is not durable), and report. The CEO directs restore-and-redo or complete-forward; do not restore on your own initiative.
> 4. **Fresh-with-unexplained-backup** — a backup matching prefix `pre-gate2-s3-` exists (find via `find`, never a glob) with no doctrine commit and 312 `accepted` → **HALT.** With the backup adjacent to the flip, an unexplained one is evidence of an ATTEMPTED corpus mutation, not harmless setup residue.
> 5. **Fresh** — porcelain clean for the doctrine path; live version line reads `2.1`; no `pre-gate2-s3-` backup; **312 reads `accepted` / `codify` / `2026-08-11T13:42:09+00:00` / `ceo`** → proceed to A1.
>
> ⚠️ **Version-line cross-check on every path:** if the version reads neither `2.1` nor a `2.2` whose FIRST History bullet names this plan's slug — match by SLUG, not id — an in-window bump by another actor landed → **HALT; the edits and History row need re-basing.**
>
> ⚠️ **If the observed state matches NONE of the five branches** → **HALT and report the full observed triple: the porcelain output, the version line + first History bullet, and the per-id status/route read-back.** Never improvise a route.
>
> **⚠️ TASK A1 — RE-VERIFY THE AUTHORING PIN BEFORE EDITING.** `shasum -a 256 /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` must equal
> `c4f5c1bff455761cdd0d7b4ec0524a9a70976de0800eea7abbac8b68d41dc60d`
> **Any mismatch → HALT** (every anchor below was proven against these bytes). Then re-prove each anchor count with `grep -cF`, and HALT on any mismatch, quoting the matches:
> | probe | expected |
> |---|---|
> | `Full walk-by-walk analysis lives in a scratchpad file` | 1 |
> | `The per-finding detail stays in the scratchpad register` | 1 |
> | `scratchpad walk register` | **3** |
> | `**Version:** 2.1 (2026-08-11). Amended only through the Iteration Protocol` | 1 |
> | `2.1 (2026-08-11)` | 2 |
> | `## History` | 1 |
> | History bullets — `awk '/^## History/{f=1;next} f&&/^## /{f=0} f&&/^- /{n++} END{print n+0}'` | **11** |
>
> ⚠️ **Also confirm E1's cited schema file EXISTS before citing it** (a reference to something that doesn't exist when read is a folded class): `ls -l /Users/marklehn/Developer/GitHub/bellows/knowledge/architecture/walk-register-schema.md` → exit 0 and a real size. Absent → HALT; E1's AFTER text would ship a dangling citation. ⚠️ **`ls` is mandated here rather than the obvious file-predicate builtin, and the reason is mechanical:** `plan_lint`'s scope check matches that builtin's bare name as a word anywhere in a step's text and fires a false WARN on it. The clone origin lints clean, so this plan does too — the divergence is removed rather than absorbed as "known-benign".
>
> **TASKS E1 → E2 → E3/E4/E5 → E6 → E7 — APPLY THE EDITS** exactly as given above, **IN THAT ORDER** (C12), absolute operand; before applying each, confirm this plan's AFTER text is what you are placing — you compose nothing.
> ⚠️ **E1 IS A MID-LINE REPLACEMENT INSIDE A 710-CHARACTER LINE.** Replace the quoted substring only. Do NOT key the edit to the line, the paragraph, or the section heading — three unrelated rules share that line and are not in scope.
> ⚠️ **ONE-PHYSICAL-LINE MANDATE:** E1's replacement text and E7's History row each land as exactly ONE physical line — no hard wraps, no reflow; the numstat pin (`7 6`) is computed on that assumption, and a wrapped-but-correct edit false-HALTs at Task F.
> ⚠️ **E3/E4/E5:** assert `grep -cF 'scratchpad walk register'` → **3** immediately before the swap and → **0** immediately after. Any other before-count → HALT; never swap a subset.
> Verify each landed via `grep -F`/`awk`, never a file-tool read. **Post-conditions (C11), all measured on the authoring dry-run:**
> | probe | expected after |
> |---|---|
> | `scratchpad` (bare token, whole file) | **0** |
> | `session-local and ephemeral` | **0** |
> | `committed walk register` | **4** |
> | `an OUTPUT of the cycle, not a scratch buffer` | 1 |
> | `The register must outlive the session` | 1 |
> | `verify that location outlives the reader the rule anticipates` | 1 |
> | `Proposal 312 / bellows Forward row 51, codified 2026-08-11` | 1 |
> | `The compact form is **load-bearing**` (co-tenant, byte-intact) | 1 |
> | `Do not keep a running fold-count in the Cycle Log` (co-tenant) | 1 |
> | `record, not instructions` (co-tenant) | 1 |
> | `2.1 (2026-08-11)` | **1** (down from 2) |
> | `**Version:** 2.2 (2026-08-11). Amended only through the Iteration Protocol` | 1 |
> | History bullets (same awk) | **12** |
>
> **⚠️ TASK E0 — PRE-COMMIT DENYLIST, scoped to the governance doctrine set.** `git -C /Users/marklehn/Developer/GitHub status --porcelain` → expect `DRAFTING_CYCLE.md` modified. **HALT iff any of the OTHER governance doctrine files is dirty: `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `READONLY_AUDIT_CONTRACT.md`, `SPECIALIST_TEMPLATE.md`, `INTERMEDIATE_DECISION_PHRASES.md`** — foreign governance activity in-window is a re-base risk. Any OTHER dirty root file (baton/session files, gitlinks, the untracked `scratchpad/`) is REPORTED, never a HALT: the Task-F commit is path-scoped and F2's name-only assertion PROVES nothing else entered it.
>
> **⚠️ TASK DOC_SHA — PIN BEFORE THE COMMIT.** `shasum -a 256` the edited file; record as **DOC_SHA** in your dev-log. A pin taken after the commit certifies whatever the commit contains.
>
> **TASK F — COMMIT, path-scoped, BEFORE touching the DB (C3):** `git -C /Users/marklehn/Developer/GitHub add DRAFTING_CYCLE.md && git -C /Users/marklehn/Developer/GitHub commit -m "[<id>] gate2(gate2-s3-register-2026-08-11): §3 walk register is a committed output (312) — doctrine 2.1 -> 2.2" -- DRAFTING_CYCLE.md` (add-before-pathspec-commit, the 309/320 convention; `<id>` = this plan's deposited id, read from your own plan filename). Record `git -C /Users/marklehn/Developer/GitHub diff HEAD^ HEAD --numstat -- DRAFTING_CYCLE.md` — ⚠️ the `-C` is load-bearing: your cwd is a lessons-forge worktree, and the bare form diffs the WRONG repo → guaranteed false HALT. Expect `7	6	DRAFTING_CYCLE.md` per the authoring dry-run; a different pair → HALT and report, do not rationalize (a wrapped-but-correct edit is the likely cause).
>
> **TASK F2 — POST-COMMIT VERIFY:** `git -C /Users/marklehn/Developer/GitHub show HEAD:DRAFTING_CYCLE.md | shasum -a 256` must equal DOC_SHA; `git -C /Users/marklehn/Developer/GitHub show HEAD --name-only --format=` must list exactly `DRAFTING_CYCLE.md`. Mismatch → HALT (a write landed in the E0→F window and is inside this plan's commit).
>
> **TASK B — BACKUP, HERE and not earlier (C4):** `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".backup /Users/marklehn/Developer/GitHub/lessons-forge/pre-gate2-s3-$(date -u +%Y%m%d_%H%M%S).db"` — assert exit 0 and empty stderr. Then `find /Users/marklehn/Developer/GitHub/lessons-forge -maxdepth 1 -name 'pre-gate2-s3-*.db' -newer /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md | head -1` and `ls -la` the found path. ⚠️ The backup filename's date token is incidental naming, not a resume key — locate it by `find`, never reconstruct.
>
> ⚠️⚠️ **ASSERT THE BACKUP IS RESTORABLE, NOT MERELY PRESENT — ON EVERY PATH THAT REACHES THE FLIP, INCLUDING A0 STATE 2's REUSE.** This file is the CEO's ONLY recovery instrument for the flip, and "exists and is non-empty" proves neither that it opens as a database nor that it holds the pre-flip state — a check that cannot fail is not a guard. Run against the FOUND path: `sqlite3 -bail -readonly "<found-backup>" ".timeout 5000" "SELECT 'BK='||COUNT(*) FROM lesson_proposals WHERE id = 312 AND status='accepted';"` → must print **`BK=1`**, exit 0, empty stderr. Anything else → **HALT before the flip.**
>
> **TASK G — THE FLIP: rehearsal → flip → read-back, three invocations.** ⚠️ **NO heredocs (the #1 forbidden op). Author each SQL file via your file-WRITE tool** in your worktree, then run `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".read <absolute-path-to-file>"`. ⚠️⚠️ **`-bail` IS MANDATORY on every sqlite3 invocation here, and each is asserted `exit 0` with EMPTY stderr** (capture stderr to a fresh scratch dir OUTSIDE every git tree, then assert the file is empty — ⚠️ shell state does NOT persist, so create and use the scratch dir IN THE SAME invocation, e.g. `S=$(mktemp -d) && sqlite3 -bail … 2>"$S/g-stderr.txt"; echo "exit=$?"; cat "$S/g-stderr.txt"`). **Measured rationale: WITHOUT `-bail`, a daemon-held lock makes `.read` SKIP the failed `BEGIN IMMEDIATE`, run the UPDATE in autocommit once the lock clears, and print the sentinels green — a committed un-bracketed flip on a green-looking run.** Non-zero exit or non-empty stderr → HALT (C10). ⚠️ **The DB is at the canonical absolute path; the CAPTURES land in YOUR OWN TREE.** `mkdir -p` your tree's evidence dir first and derive its ABSOLUTE path from `pwd` when you author the `.sql` files — sqlite `.output` must receive that derived absolute path, never a guessed one.
>
> **G1 — REHEARSAL (read-only by construction; file `knowledge/development/gate2-s3-flip-rehearsal.sql`), content exactly:**
> ```
> BEGIN IMMEDIATE;
> SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id = 312 AND status='accepted' AND route='codify';
> SELECT 'ACC='||COUNT(*) FROM lesson_proposals WHERE status='accepted' AND route='codify';
> SELECT 'MAXID='||MAX(id) FROM lesson_proposals;
> ROLLBACK;
> ```
> Assert: **`PRE=1`**, **`ACC=74`**, **`MAXID=314`**, exit 0, empty stderr. This is both the predicate proof C6/C14 rest on and a live `BEGIN IMMEDIATE` lock probe. ⚠️ **The rehearsal is load-bearing and must not be skipped as redundant: it HALTS BEFORE any write.** The `CHANGES` sentinel can only REPORT a bad predicate after the UPDATE has committed — prevention and reporting are not the same guard.
> - `PRE` ≠ 1 → **HALT and report 312's current status/route.**
> - ⚠️ **`ACC` < 74 → HALT (C15, the standing stale hazard). Do NOT proceed on the remainder.** Report the observed count and the ids that are no longer `accepted|codify`. `ACC` > 74 means a Gate-1 routing landed in-window → HALT and report; the batch composition this plan was authored against has changed.
> - `MAXID` > 314 means an in-window forge cycle inserted rows; that is expected-benign and is REPORTED, not a HALT — but it changes G2's capture bound, so **record the observed MAXID and use `id <= 314` regardless** (the bound is deliberately pinned to authoring, so in-window inserts are excluded by construction).
>
> **G2 — THE FLIP, with the capture INSIDE the same transaction (file `knowledge/development/gate2-s3-flip.sql`), content exactly** (the `.output` path is your tree's evidence dir, derived from `pwd` when you author the file):
> ```
> BEGIN IMMEDIATE;
> .output <your-tree-abs>/knowledge/qa/evidence/gate2-s3-register-2026-08-11/outside-range-ids.txt
> SELECT id||'|'||category||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'')||'|'||COALESCE(status_updated_by,'') FROM lesson_proposals WHERE id <= 314 AND id != 312 ORDER BY id;
> .output stdout
> UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id = 312 AND status='accepted';
> SELECT 'CHANGES='||changes();
> SELECT 'GLOBOK='||COUNT(*) FROM lesson_proposals WHERE id = 312 AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z' AND status_updated_at <> '2026-08-11T13:42:09+00:00';
> COMMIT;
> ```
> ⚠️ **The `<> '2026-08-11T13:42:09+00:00'` clause is pinned to the value plan 342 actually wrote — an OFFSET-form timestamp.** Do NOT substitute the clone origin's `2026-08-09T01:20:01Z`: that value appears nowhere on this row, so the exclusion would be vacuous. ⚠️ **Favourable asymmetry, stated so a later reader does not "simplify" it away:** because the prior value is offset-form, the `Z`-terminated GLOB already excludes it structurally (measured: the GLOB returns **0** against 312's live value), so the GLOB alone is a value guard here. The explicit exclusion is kept as defence in depth, not because the GLOB is insufficient.
> Assert the capture file exists with **313 lines** (corpus measured 314 rows, MAX(id)=314, ids contiguous, 2026-08-11). ⚠️ **This assert is read AFTER the transaction has committed, so a mismatch does NOT mean "abort the flip" — the flip has already landed.** Below 313 means a corpus row was DELETED between authoring and this run; above 313 means the contiguity premise no longer holds. Either way: **do not re-run G2, do not edit the capture** — record the observed count, name which ids differ from the expectation, and HALT for a CEO read with the flip reported as landed.
> ⚠️ **Known mechanism limit, priced:** sqlite scripts cannot conditionally ROLLBACK, so the sentinels print before a COMMIT that will happen regardless. The protection is STRUCTURAL: G1 just proved exactly 1 row matches, and the `AND status='accepted'` predicate makes the UPDATE unable to touch anything else. **Read both sentinels: `CHANGES=1` and `GLOBOK=1`. Either off → HALT, report both values and 312's current status; the backup is the CEO's restore instrument, not yours.** ⚠️⚠️ **THE ID IS AN IMMUTABLE INPUT: a sentinel mismatch is NEVER resolved by editing it, widening the predicate, or adding an id. The only response is HALT with the numbers.**
>
> **G3 — READ-BACK.** Same invocation discipline (this is a read, so add `-readonly`): `sqlite3 -bail -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" "SELECT id||'|'||status||'|'||status_updated_by||'|'||status_updated_at FROM lesson_proposals WHERE id = 312;"` → deposit the RAW output in your tree's evidence dir as `flip-readback.txt` — the row must read `implemented|ceo|<timestamp>`, with the timestamp `Z`-form and differing from `2026-08-11T13:42:09+00:00`.
>
> **Output Receipt required** — DOC_SHA, the commit hash, the numstat pair, PRE/ACC/MAXID/CHANGES/GLOBOK sentinel values, and every file deposited. **End the dev-log with `### Ledger Updates` and `#### Prompt Feedback` sections** (the daemon parses these per step; a Step-1 observation with no section never reaches the ledger).
>
> **⚠️ FINAL ACTION OF THIS STEP — COMMIT YOUR DEPOSITS IN THE WORKTREE** (separate from Task F, which commits the doctrine file in the ROOT repo): stage exactly the files your Scope block lists **for the A0 path you took** and commit with **the pathspec on the COMMIT naming exactly those paths**, then assert `git show --name-only --format= HEAD` prints exactly them. ⚠️ **Committing is what carries the captures through the teardown merge into the QA step's tree — the `deposit_uncommitted` gate FAILS an uncommitted deposit, and an unmerged capture strands QA row 6 on its crash-recovery fallback.** ⚠️ **`lessons-forge.db` and the `pre-gate2-s3-*.db` backup are deliberately ABSENT from Scope and from the commit — the DB is UNTRACKED by shop policy (plan 30); `git add`ing either would re-track it AGAINST that policy.**
>
> **Scope:**
> - `knowledge/development/dev-log-gate2-s3-register-step-1-2026-08-11.md`
> - `knowledge/development/gate2-s3-flip-rehearsal.sql`
> - `knowledge/development/gate2-s3-flip.sql`
> - `knowledge/qa/evidence/gate2-s3-register-2026-08-11/outside-range-ids.txt`
> - `knowledge/qa/evidence/gate2-s3-register-2026-08-11/flip-readback.txt`
>
> ⚠️ On the A0 state-3 recovery path ONLY, `knowledge/qa/evidence/gate2-s3-register-2026-08-11/resume-sweep.txt` joins this Scope list (and the commit assertion then names it too).
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-gate2-s3-register-step-1-2026-08-11.md`
> - `lessons-forge/knowledge/development/gate2-s3-flip-rehearsal.sql`
> - `lessons-forge/knowledge/development/gate2-s3-flip.sql`
> - `lessons-forge/knowledge/qa/evidence/gate2-s3-register-2026-08-11/outside-range-ids.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-s3-register-2026-08-11/flip-readback.txt`
>
> ⚠️ `resume-sweep.txt` is produced ONLY on A0 state 3 and is named here so that path's deposit is in scope rather than a surprise. The doctrine file is modified in the ROOT repo and is NOT a deposit of this step — it is committed at Task F and verified at F2.

## STEP 2 — QA

---

> **FIRST — Deliverable Verification (Rule 8 / Rule 17).** Open the Step-1 dev-log, confirm its Output Receipt is Complete, then verify every file it claims exists and carries the described change. Table: `| Deliverable | Expected | Status (✅/❌) | Evidence |`. Any ❌ → report and HALT; make no edits yourself.
>
> **MANDATORY — Rule 20 self-check (canonical block, Checklist #4 — the exact template, NOT a paraphrase).** Run the canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path). Fill: `plan_slug`: `gate2-s3-register-2026-08-11`; `qa_report_path`: `<your-own-tree-abs>/knowledge/qa/gate2-s3-register-qa-2026-08-11.md`; `evidence_dir`: `<your-own-tree-abs>/knowledge/qa/evidence/gate2-s3-register-2026-08-11/` (derive from `pwd`, NOT hardcoded); `required_evidence_files`: `[doc-integrity.txt, db-invariants.txt, gate-neutrality.txt, pytest_targeted.txt]`. Deposit **all four** BEFORE running the block — the block `sys.exit(1)`s on any missing name, so a count that disagrees with the list false-HALTs a correct run after both writes have landed. **Include the block's literal stdout: the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line must both appear byte-exact (em-dash U+2014).**
>
> ⚠️ **REPORT STRUCTURE — the verification section never closes on its own: immediately after the verification table, write exactly `## Evidence and Narrative`**, and keep the Rule 20 stdout, the Output Receipt and `### Ledger Updates` under `##`-level headings.
>
> **Evidence rule:** RAW command output, never a summary. The doctrine file is read at its absolute root path.
>
> ⚠️ **ONE read-only DB form, used for EVERY query in this step — do not mix mechanisms:** `sqlite3 -bail -readonly "/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db" ".timeout 5000" "<SQL>"` — canonical absolute path, `-readonly`, `.timeout 5000` per C10 (a `database is locked` in the verdict window is a HALT with the error verbatim, never a retry loop), `-bail` and an exit-0/empty-stderr assert as in Step 1.
>
> **Verification table, one row per claim (HALT on any FAIL).** ⚠️ **FAIL means an assertion this table makes is FALSE.** Two rows carry explicit branches that are NOT failures — row 6's outside-range concurrent activity and row 7's scope widening — where the assertion still holds and the observation is REPORTED with its detail. Everything else that does not assert true is a HALT.
>
> **1. DOC INTEGRITY — GIT IS THE PRIMARY REFERENT, the dev-log only drift-detection.** Discover the doctrine commit INDEPENDENTLY: `git -C /Users/marklehn/Developer/GitHub log --format='%H %s' -20 -- DRAFTING_CYCLE.md`, take the newest commit whose message names the slug `gate2-s3-register-2026-08-11`. Then assert the three-way agreement: `git -C /Users/marklehn/Developer/GitHub show <that-commit>:DRAFTING_CYCLE.md | shasum -a 256` == `shasum -a 256` of the LIVE file == the dev-log's DOC_SHA. ⚠️ The `-C` is load-bearing on the `show` too: the bare form fatals from your worktree cwd and `shasum` then hashes EMPTY input at pipeline exit 0 — the empty-input signature is `e3b0c442…`; treat that sha as "the show failed", never as a real value. Also: `git -C /Users/marklehn/Developer/GitHub status --porcelain -- DRAFTING_CYCLE.md` EMPTY; `git -C /Users/marklehn/Developer/GitHub show <that-commit> --name-only --format=` lists exactly `DRAFTING_CYCLE.md`. → `doc-integrity.txt`
> **2. THE SWEEP POST-CONDITION — BOTH RETIRED TOKENS AT ZERO, AND THE REPLACEMENT AT FOUR.** `grep -cF 'scratchpad'` → **0** and `grep -cF 'session-local and ephemeral'` → **0** (⚠️ these are whole-file assertions and they are only safe because E7 deliberately DESCRIBES rather than QUOTES both strings — if either returns 1, first check whether the History row quotes it before concluding the sweep failed); `grep -cF 'committed walk register'` → **4**; `grep -cF 'scratchpad walk register'` → 0; `grep -cF 'scratchpad register'` → 0. → `doc-integrity.txt`
> **3. E1 CONTENT — THE CODIFICATION ITSELF, PROBED DIRECTLY, PLUS THE CO-TENANTS IT MUST NOT HAVE TOUCHED.** New text present: `grep -cF 'an OUTPUT of the cycle, not a scratch buffer'` → 1; `grep -cF 'committed to \`governance/knowledge/research/\`'` → 1; `grep -cF 'The register must outlive the session'` → 1; `grep -cF 'verify that location outlives the reader the rule anticipates'` → 1; `grep -cF 'Proposal 312 / bellows Forward row 51, codified 2026-08-11'` → 1. ⚠️ **AND the three co-tenant rules that share line 142 byte-intact — this is the row that catches an over-wide E1:** `grep -cF 'The compact form is **load-bearing**'` → 1, `grep -cF 'Do not keep a running fold-count in the Cycle Log'` → 1, `grep -cF 'record, not instructions'` → 1. All five new probes measured **0 pre-edit** on the authoring dry-run, so each is EARNABLE and satisfied only by this edit landing. → `doc-integrity.txt`
> **4. NUMSTAT vs THE PLAN'S PIN.** Using `<that-commit>` as discovered in row 1 (one token, one referent, across rows 1/4/5): `git -C /Users/marklehn/Developer/GitHub diff <that-commit>^ <that-commit> --numstat -- DRAFTING_CYCLE.md` → exactly `7	6` (the authoring dry-run pin; the dev-log is not the referent). → `doc-integrity.txt`
> **5. VERSION + CHANGELOG INTEGRITY.** `grep -cF '**Version:** 2.2 (2026-08-11). Amended only through the Iteration Protocol'` → 1 (probed, not eyeballed); `grep -cF '2.1 (2026-08-11)'` → **1** (down from 2 — the v2.1 History row, intact); the new 2.2 row is the FIRST History bullet, names the slug, and does NOT contain `2.1 (2026-08-11)`; the prior first row (`- **2.1 (2026-08-11):** slug dc-direction-verdict-2026-08-11`) is intact immediately below it. ⚠️ **E7's SUBSTANTIVE TAIL is probed, not just its head** — `grep -cF 'the remaining Gate-2 batches'` → **1** (E7's final clause; measured **0** in the doctrine pre-edit, so it is EARNABLE and satisfied only by the row landing WHOLE — without it, a History row truncated after its opening passes every other check here). Row-count via THIS exact command (method is part of the pin): `awk '/^## History/{f=1;next} f&&/^## /{f=0} f&&/^- /{n++} END{print n+0}' /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` → **12** (baseline 11, measured 2026-08-11). → `doc-integrity.txt`
> **6. FLIP READ-BACK + BLAST RADIUS AT VALUE LEVEL, INDEPENDENTLY RE-DERIVED, WITH THE VERDICT-WINDOW PARTITION.** (a) Per-id: 312 reads `status='implemented'`, `status_updated_by='ceo'`, `status_updated_at` GLOB-matching `20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z` **AND differing from `2026-08-11T13:42:09+00:00`**; exactly 1 row; `category` preserved `governance_rule`. (b) `SELECT COUNT(*) … WHERE status='accepted' AND route='codify'` → **73** (74 minus this one) — ⚠️ **a LOWER value is NOT automatically this plan's doing: report the count and, if it is below 73, name which ids left the set** (the stale hazard's post-flip signature). (c) Re-run the EXACT capture projection yourself (`WHERE id <= 314 AND id != 312 ORDER BY id`) — do NOT reuse Step 1's output — and `diff` it against the Step-1 deposited `outside-range-ids.txt` (313 lines). **PARTITION every differing line: (i) any line whose id is 312 is impossible by the projection's own predicate — its appearance means the capture or the comparison is malformed → HALT; (ii) any id PRESENT in the capture but ABSENT from your re-derivation is a DELETED corpus row → HALT — a row vanishing is corpus damage, not concurrent work; (iii) every other differing line is CONCURRENT ACTIVITY — NAME each with its id and before/after status, confirm none is 312, and do NOT halt.** Do NOT widen the predicate to id > 314 — in-window inserts at 315+ are out of scope by construction. → `db-invariants.txt` ⚠️ **DECLARED FALLBACK (fires ONLY when the Step-1 receipt reports the capture lost to a crashed worktree):** the same-instant comparison is then unverifiable and is REPORTED as such, never silently passed; run the degraded sweep instead and label the row `DEGRADED`: (i) `SELECT COUNT(*) FROM lesson_proposals WHERE id <= 314` → 314 (no deletions); (ii) `SELECT id, status FROM lesson_proposals WHERE status_updated_at = (SELECT status_updated_at FROM lesson_proposals WHERE id = 312)` → must include 312, `implemented`. ⚠️ **A second id sharing that one-second instant is REPORTED, not automatically a HALT** — bulk writes at second granularity are normal in this corpus (Gate-1 stamped 41 rows on one value) — HALT only if such a row is one this plan should never have touched *and* its status moved to `implemented`.
> **7. TARGETED TESTS — AND THE PREMISE THAT MAKES THEM SUFFICIENT.** First re-check the Rule 21 premise instead of inheriting it: `find /Users/marklehn/Developer/GitHub/lessons-forge/src -name 'test_*.py'` → must list **exactly** `test_lessons_forge.py`. A second module means "targeted = full" is FALSE for this run — report it and run the whole `src/` suite instead (a scope widening is reportable, never a HALT). Then `python3 -m pytest src/test_lessons_forge.py -q` from the lessons-forge tree → **zero regressions against the recorded baseline (55 passed / 0 skipped, measured 2026-08-11 — verify the live counts; if the baseline itself moved, report the delta rather than asserting the number)**. → `pytest_targeted.txt`
> **8. GATE-NEUTRALITY, FULL-SURFACE WITH POSITIVE CONTROL.** (a) The E7 no-gate-edit claim, re-measured: `grep -cF 'scratchpad'`, `grep -cF 'walk register'` and `grep -cF 'walk_register'` against **both** `/Users/marklehn/Developer/GitHub/bellows/scripts/plan_lint.py` and `/Users/marklehn/Developer/GitHub/bellows/gates.py` → **0 in all six**. Any nonzero means a live coupling exists and the E7 claim is FALSE → HALT. (b) `grep -rn -F 'DRAFTING_CYCLE' /Users/marklehn/Developer/GitHub/bellows --include='*.py'` → **classify EVERY hit**; expected classes: WARN-message citation strings + comments in `plan_lint.py`, fixture text in `tests/test_plan_lint.py`, and **zero hits in `gates.py`** — any hit outside those classes → HALT. (c) POSITIVE CONTROL proving the instrument speaks (a bare negative supports nothing): `grep -cF 'Drafting Cycle' /Users/marklehn/Developer/GitHub/bellows/scripts/plan_lint.py` → **11** (same instrument, same file, known-present token, measured 2026-08-11). (d) A zero-match `grep -c` prints `0` and exits 1 — the printed count is the assertion. ⚠️ The shim injects `--ignore-files`, so (b)'s recursive sweep skips gitignored paths — immaterial today (only `__pycache__` is ignored under bellows), stated so the coverage bound is known. → `gate-neutrality.txt`
> **9. CONSUMER SEMANTICS — the flip's EFFECT, not just its row values.** The flip moves proposal 312 across the terminal/non-terminal boundary, changing what the ingest update path does to entry 304. Verify from source and from the live corpus: (a) read `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` and confirm `implemented` IS in `_TERMINAL_STATUSES` and `accepted` is NOT — **quote line 31 verbatim**; (b) run `get_unclassified_entries` against the canonical DB (read-only) and confirm entry **304** is ABSENT from the work list — it was dispositioned before the flip and must stay dispositioned after it. **A flip that re-queued its own entry for re-proposal would be a silent regression no row-value check can see.** Paste both the source quote and the raw helper output. → `db-invariants.txt`
> **10. THE AMENDMENT IS TRUE OF THE SHOP IT DESCRIBES — the claim-vs-world check.** E1 now states registers are committed to `governance/knowledge/research/`. Assert that directory exists and holds at least the four registers measured at authoring: `find /Users/marklehn/Developer/GitHub/governance/knowledge/research -maxdepth 1 -name 'walk-register-*.md' | wc -l` → **≥ 4**. ⚠️ **This row REPORTS, it does not HALT on a higher count** (a register added in-window is normal and expected). Below 4 → HALT: the doctrine would be asserting a location the shop does not use, which is the exact defect this plan exists to fix. ⚠️ **This plan migrates nothing** — the one uncommitted register under the root `scratchpad/` is deliberately left in place and its continued presence is NOT a failure of this row. → `doc-integrity.txt`
>
> **Then `## Evidence and Narrative`, then the Output Receipt.**
>
> ⚠️ **`### Ledger Updates` — the channel has SIX documented failure modes; all guarded here:** author via `Write`/`Edit` (the daemon parses assistant text + Write/Edit content, NOT Bash), EXACTLY ONCE, complete, never re-edit; `##`-level scope after `## Evidence and Narrative`; substance INSIDE the section; end with a blank line after the last subsection; one row per bullet with no second physical line (dup-append and null-parse are both known modes).
>
> **`#### Forward Register`: the word `NONE`.** ⚠️ **This is a DELIBERATE non-emission, not an oversight.** bellows Forward row 51 is the row this plan discharges, but it lives in **bellows'** register and a Receipt emission resolves to **this project's** (`lessons-forge/knowledge/FORWARD.md`) — the wrong file. Row 51's flip to `closed-by-plan-<id>` is a Planner-direct Rule 42 status update at session wrap. Do NOT emit it here, and do NOT edit any FORWARD.md directly. A genuinely NEW item discovered at run time replaces `NONE` and follows the one-row-per-bullet contiguous form.
>
> **⚠️ FINAL ACTION — COMMIT YOUR DEPOSITS**, pathspec on the COMMIT naming exactly the Scope files, then assert `git show --name-only --format= HEAD` prints exactly them. **`lessons-forge.db` is never staged.**
>
> **Scope:**
> - `knowledge/qa/gate2-s3-register-qa-2026-08-11.md`
> - `knowledge/qa/evidence/gate2-s3-register-2026-08-11/doc-integrity.txt`
> - `knowledge/qa/evidence/gate2-s3-register-2026-08-11/db-invariants.txt`
> - `knowledge/qa/evidence/gate2-s3-register-2026-08-11/gate-neutrality.txt`
> - `knowledge/qa/evidence/gate2-s3-register-2026-08-11/pytest_targeted.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate2-s3-register-qa-2026-08-11.md`
> - `lessons-forge/knowledge/qa/evidence/gate2-s3-register-2026-08-11/doc-integrity.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-s3-register-2026-08-11/db-invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-s3-register-2026-08-11/gate-neutrality.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-s3-register-2026-08-11/pytest_targeted.txt`

---

## Drafting Cycle

**Tier:** T2 — trigger fired: T-6 (governance surface: one doctrine file + the proposal corpus). Clone lineage: machinery cloned from **executable-330**, established by measurement as the newest true Gate-2 codification batch (`git log --oneline -- DRAFTING_CYCLE.md` → 343, 334, **330**; the two newer commits are direct amendments carrying neither a corpus flip nor a cycle, so cloning either would inherit a deviation posture instead of the mechanism). Diffed against the origin throughout; every inherited constant re-measured rather than carried.

**Walks:** ⚠️ **ZERO. THIS IS A DECLARED DRAFTING-CYCLE DEVIATION and it is recorded here with its cost, per the standing requirement that a deviation be declared in the artifact rather than in conversation.**

**What ran:** §2.0's **context pin, in full** — all five measurements, executed. The walk register (walk 0 + verdict) is **committed at `governance/knowledge/research/walk-register-gate2-s3-register-2026-08-11.md`** (root commit `d3cf251`) — the location this plan's own E1 mandates, applied to itself before being codified. **Direction verdict: PROCEED**, none of the three forcing findings fired (clone origin confirmed at source; edit mechanism confirmed as a mid-line surgical replacement with anchor count 1; scope-licensing premise confirmed — 312 is `accepted|codify`, Forward row 51 open).

**What did not run:** lenses 1–5, any walk, and the T2 cold panel.

**The authority and the reasoning.** CEO direction, 2026-08-11, on the measured evidence in `drafting-cycle-findings-2026-08-11.md` — eight findings from three plans run end-to-end: **62% of one plan's warm-walk findings (31 of 50) were damage the walk itself created**; cold seats returned 7× the findings and 7× the HIGH per pass, all pre-existing; and **every foundation defect was readable before walk 1 by five commands in ~30 seconds**, while two cold seats spent ~333k tokens re-finding four of them. The shop is currently operating *off* that collected evidence, and running the full cycle on this plan would spend the measured failure mode rather than test the remedy. ⚠️ **This is a PARTIAL deviation and differs in kind from plan 343's** — 343 ran no cycle at all because its subject *was* the cycle; here the highest-yield phase ran and the phases the evidence prices as low-yield-on-a-small-artifact did not.

**What the pin caught that a walk would otherwise have been credited with — the deviation's return, stated as specifics rather than as a claim:**
1. The clone origin was **not** the newest commit on the target file (343 → actually 330).
2. The baton's batch sizes were **stale** — 10/12 stated, **37/37** measured.
3. The `Z`-form timestamp GLOB inherited from the origin **returns 0** against the live row; the corpus carries **four** timestamp representations and the 74 `accepted|codify` rows split 42/32 exactly on the Gate-1 boundary.
4. `changes()=2` in the origin is **wrong here** — this is a one-row flip.
5. The target clause sits **mid-line at column 90 of a 710-character line carrying four independent rules** — the geometry that destroyed a draft earlier the same day.
6. The fold has **five sites, not one**; four are dependent rules that would have been left calling the register a scratch buffer.

**The cost, recorded rather than argued.** ⚠️ **One defect of exactly the class a lens catches DID reach the artifact and was caught by the authoring dry-run instead:** the first History row **quoted** both retired strings, which left `scratchpad` and `session-local and ephemeral` at 1 after a complete and correct edit — making QA's two strongest post-conditions unsatisfiable on a correct run. It is the clone origin's own QA-row-4 pre-satisfaction trap in mirror image. **It was caught because the dry-run executes the edits and measures the result, not because anyone read the draft.** A lens would plausibly have caught it too; nothing else in this cycle would have. **The honest reading: the mechanical dry-run substituted for a lens here, and that is one instance, not a demonstration.** Anything a dry-run cannot execute — a wrong premise stated in prose, an unsatisfiable QA assertion, a mis-scoped guard — remains unchecked by anything in this plan's process, and the residue below is enumerated on that understanding.

**Residue, enumerated by class (the judged-stop form):** (a) **no adversarial read of the AFTER text as doctrine prose** — E1's wording has been checked for probe earnability and byte-level effect, never for whether it says the right thing to a future reader; (b) **no independent check of the QA table AS A SYSTEM** — each row was authored against a measurement, but no pass asked whether the ten rows have asymmetric depth (the origin's own walk-6 finding); (c) **no cold-panel clone-diff**, so a guard 330 carries that this clone silently dropped would not have been detected — the class that produced nine findings in one prior panel; (d) **§2.8 oscillation is untestable here** — with no walks there are no folds and no fold interactions, which removes a risk rather than leaving one.

**Conformance (§5) — last run at the pre-deposit freeze, `plan_lint` → EXIT 0.** Run at a path whose `project_root` resolves exactly as the deposit path will (the location-dependent-lint rule: `project_root` is the path before `/knowledge/`), and warning parity was confirmed rather than assumed — each cited path below is absent from the real `lessons-forge` tree too, so the staged run and the deposit run produce the same set. **All 8 checks PASS. FIVE warnings stand, each classified; there are no unexplained ones:**

1. **The missing-lens-lines warning (all five per-lens result lines absent from this block)** — ⚠️ **the declared deviation, correctly detected.** This warning is EARNED and is left standing deliberately; silencing it by authoring result lines for passes that never ran would be the exact wording-satisfiable-gate failure §3 forbids. ⚠️ **Its text is DESCRIBED here rather than quoted, and that is load-bearing, not style:** the check is a case-insensitive substring search over this very block, so quoting the warning's own citation of the five names satisfies the check on the walks' behalf and the warning vanishes — measured live during authoring: an earlier revision of this paragraph quoted it, the WARN disappeared from the next lint run with no lens having run, and §3's re-lint-after-editing-the-log rule is what caught it.
2. **`T2 plan missing cold-panel line`** — same class, same reason, same deliberate non-silencing.
3. **`(o1) missing path knowledge/architecture/walk-register-schema.md`** — a **cross-project citation**: the file is real at `bellows/knowledge/architecture/walk-register-schema.md` (verified present at authoring, and re-verified at Task A1 before E1 cites it), but check (o1) resolves extracted paths against THIS plan's project root, which is lessons-forge. Benign by construction.
4. **`(o1) missing path knowledge/qa/evidence/gate2-s3-register-2026-08-11/resume-sweep.txt`** — the conditional A0-state-3 recovery artifact, produced only on that path. **This is the identical known-benign warning the clone origin declared and shipped with.**
5. **`(o1) missing path tests/test_plan_lint.py`** — cross-project citation again (bellows), cited in QA row 8's hit-classification list.

⚠️ **One warning was NOT absorbed as benign but removed at source:** the first run also emitted `step 1 mentions tests but declares no test scope`, triggered by the shell file-predicate builtin appearing as a bare word in Task A1. The origin lints clean, so the divergence was traced (`plan_lint.py:145`) and the command swapped to `ls` rather than declared away. **The distinction matters: a warning is benign when its cause is understood and structural, not when it is merely familiar.**

**Closing:** ⚠️ **This plan does NOT meet §2's doneness bar and does not claim to.** The bar requires a full walk returning record-class-only, predominantly fold-introduced findings with the origin split stated as a number; **no walk ran, so there is no split to state and the bar is inapplicable rather than met.** It is deposited as a **declared deviation with its residue enumerated**, which §2's RE-DRAFT/judged-stop grammar treats as a normal reportable outcome — not as a close that earned its gate. **The freeze-time re-verification that DID run, all re-derived against the live file:** authoring SHA `c4f5c1bf…`, dry-run numstat `7 6`, `2.1 (2026-08-11)` 2 → 1, both retired tokens 0 post-edit, `committed walk register` 4, History bullets 11 → 12, all five E1 probes and E7's tail probe measured 0 pre-edit (earnable), the three line-142 co-tenants byte-intact. Fold-and-deposit exactly once.
