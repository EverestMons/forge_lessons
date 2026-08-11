# Executable: Gate 2 batch 2 — the PLANNER_TEMPLATE codification batch (37 proposals): v4.85 → v4.86, then flip all 37 to `implemented`

**Type:** Executable
**Project:** lessons-forge
**Depends on:** **executable-344** (lessons-forge, Done — the clone origin: the newest same-class Gate-2 plan, closed 2026-08-11 with 2/2 clean gates; this plan inherits its mechanism and its two measured corrections — the per-vintage timestamp exclusion and the describe-don't-quote History discipline), executable-330 (lessons-forge, Done — the grandparent origin whose flip machinery 344 cloned), **executable-326 + executable-342** (lessons-forge, Done — the two Gate-1 routing plans that WROTE `accepted|codify` on these rows: 326 stamped 21 rows `2026-08-09T01:20:01Z` (Z-form) and 342 stamped 16 rows `2026-08-11T13:42:09+00:00` (offset-form) — BOTH values are pinned prior-value exclusions in G2), PLANNER_TEMPLATE.md at v4.85 (precondition, checked at A0)
**Created:** 2026-08-11
**Author:** Planner
**Slug:** `gate2-template-batch-2026-08-11` (authoring-time; stable across any crash-redo re-deposit — the A0 re-entry key and the Rule 20 `plan_slug`)
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T2
**qa_steps:** 2
**Test Scope:** targeted (Rule 21 — the 344 justification verified anew: this plan changes no source code; the lessons-forge repo has a single test module, `find` over `src/` returned exactly `test_lessons_forge.py` measured 2026-08-11; QA row 7 re-derives the premise at run time; baseline 55 passed / 0 skipped)

⚠️ **ID NOTE — the deposit filename is decided AT DEPOSIT.** Slug+date name form; id read from `id_sequence` at deposit, never at authoring (`next_id` read **345** at authoring — a PREDICTION, not a pin).

---

## Why this exists — the largest Gate-2 batch, and the shape that makes 37 edits safe

Thirty-seven proposals routed `accepted|codify` with `target_artifact='PLANNER_TEMPLATE.md'` are owed codification: **21 routed by the 2026-08-09 gate** (plan 326) and **16 by the 2026-08-11 gate** (plan 342). All 37 are `governance_rule`, all `high` confidence. The batch was measured, not inherited — the baton's "10 items" matched neither vintage nor the total (LESSONS: re-verify inherited claims).

**The shape decision, taken on the 264-class evidence:** thirty of the 37 are NEW rules. They land as **ONE contiguous block insertion at a single anchor** (new Rules 65–94, appended after Rule 64 in proposal-id order, per the 4.83 append-only precedent that added 63/64 at the end) rather than as thirty separate edits — one anchor instead of thirty, and the block's line count is what the numstat pins. The remaining seven are extensions to existing rules (52, 55, 56 ×2, 61, 62) and Checklist #29. With the version pair and the changelog row: **ten mechanical edits.**

**The edit mechanism is a single all-or-nothing script, and that is a deliberate upgrade over ten hand-placed edits.** The plan GIVES the script verbatim (the agent writes it to a file and runs it — data, not composition, exactly as 344's `.sql` files were). The script reads the live file once, asserts every anchor's count `== 1` BEFORE any mutation, applies all ten edits in memory, and writes once at the end — **an anchor mismatch anywhere aborts with zero bytes written.** Re-run after success is self-detecting: the `**Version:** 4.85` anchor no longer exists, so the script aborts rather than double-applying. The mid-line destruction class that required 344's column-90 warnings cannot arise: every anchor here is a complete physical line, asserted unique.

**Routing:** the corpus path proper (§6-equivalent, amend-only-through-the-corpus) — LESSONS.md → forge ingest → classification → Gate 1 `codify` → this Gate-2 plan. **No routing deviation to declare.** A DRAFTING-CYCLE deviation IS declared in the `## Drafting Cycle` block below, the 344 form: the §2.0 context pin ran in full; the walks did not.

**Rule-46 splits, recorded so the batch's boundary is explicit:** the bellows-owned halves of 274 (the verdict channel is one bit), 289 (the verdict grammar itself), 305 (`pause_for_verdict` runtime enforcement — FORWARD 46) and the forge/lint-owned mechanisms of 310 (FORWARD 52) and 314 (FORWARD 54) are **NOT codified here** — each new rule's text names its split inline. Their FORWARD rows ride bellows-project plans per the emitter-owner match rule; **no step of this plan touches any FORWARD register.**

## Scope — one doctrine file, ten script-applied edits; one scoped 37-row flip; nothing else

- **Edits exactly ONE existing file:** `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (root repo), via the GIVEN script below. The AFTER text is GIVEN in the script — the agent PLACES it by running the script, never composes.
- **One DB write:** a scoped `UPDATE` flipping the 37 ids `accepted → implemented` at the canonical absolute path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`.
- **No code edit.** The build script and the two `.sql` files are DATA the plan gives verbatim — writing and running them is in scope, not a code edit. Needing to MODIFY any of them means an anchor failed → HALT, never patch.
- ⚠️ **§6-equivalent coordinate-doctrine-and-gate: NO gate edit owed, discharged BY MEASUREMENT** (2026-08-11): the only template-rule references in bellows code are `Rule 20`, `Rule 22`, `Rule 26` (`gates.py` + `plan_lint.py`, enumerated by grep) — all three untouched; numbering is append-only so no existing number moves; **zero `:NN`-style line citations of PLANNER_TEMPLATE.md exist in bellows `*.py`** (the new Rule 76's own discipline, applied to this edit first). Re-verified at QA row 8.
- **No LESSONS.md touch. No FORWARD register touch by any step.**
- ⚠️ **DOWNSTREAM EFFECT OF THE FLIP, NAMED:** `implemented` IS in `_TERMINAL_STATUSES`, `accepted` is NOT (`lessons-forge/src/lessons_forge.py:31`). After this flip, later edits to the 37 source entries flag rather than stale — intended, verified at QA row 9.
- ⚠️ **THE STALE HAZARD, re-based after 344:** corpus-wide `accepted|codify` measured **73** (74 minus 344's row). G1 asserts `ACC=73` pre-write; **fewer → HALT, never proceed on the remainder.** Post-flip expected: **36**.
- ⚠️ **The doctrine edit lands in the REAL governance root, outside any bellows worktree** — `_gate_scope_check` cannot see it; the QA doc-integrity rows are the only guard and fail closed. Every command touching the doctrine file uses the ABSOLUTE operand. **PLACEMENT is the script (file-write the script, run with python3); VERIFICATION is Bash-only** (`grep -F` / `shasum` / `awk` / `python3` one-liners), never a file-tool read.
- ⚠️ **Verdict-window posture:** from the Step-1 doctrine commit until close, v4.86 GOVERNS the shop. A HALT holds it live for the CEO — never restore/revert on a HALT. Rollback is a CEO decision.
- **Deposit basenames are DECLARED — do not re-date at run time.** The only live date is G2's in-statement `strftime`.
- ⚠️ **Expected `plan_lint` state at deposit:** recorded in the `## Drafting Cycle` block's Conformance paragraph, measured at the deposit-shaped path. Any WARN or FAIL not named there → do not deposit.

### ⚠️ Environment facts — observed, not predicted

1. `grep` is a ugrep shim: **`-F` for every literal**; a zero-match `grep -c` prints `0` and exits 1 — the printed count is the assertion; never `&&`-chain zero-count probes.
2. Shell state does NOT persist between commands — create and use scratch dirs in the same invocation.
3. zsh aborts on an unmatched glob — use `find`, never a glob.
4. The DB is **gitignored and absent from any worktree**: a bare relative `sqlite3 lessons-forge.db` silently CREATES an empty file. Canonical absolute path only.
5. ⚠️ **THE PRIOR-TIMESTAMP EXCLUSION MUST NAME BOTH GATE-1 VALUES, and the Z-GLOB's protective value is INVERTED from plan 344's situation.** Measured 2026-08-11 on the 37 target rows: the 21 326-written rows ALL carry exactly `2026-08-09T01:20:01Z` — **which MATCHES the Z-GLOB**, so for those 21 the bare GLOB is vacuous and only the explicit exclusion guards them. The 16 342-written rows carry `2026-08-11T13:42:09+00:00`, structurally non-matching. G2's GLOBOK therefore excludes **both** pinned values; substituting either alone re-opens a vacuous sentinel on the other vintage. (344's Environment fact 5, generalized: derive the exclusion from the target rows' ACTUAL values, per vintage.)

---

## The ten edits — applied by the GIVEN script, all-or-nothing

**E1** — new Rules **65–94** (30 proposals in id order: 223, 225, 228, 229, 236, 239, 242, 255, 257, 264, 265, 266, 267, 268, 274, 277, 280, 281, 282, 284, 288, 289, 293, 297, 303, 305, 306, 307, 310, 314), one contiguous block inserted after Rule 64's Source line, before the section divider. Each rule: `### NN. Title` + body + `*Source: proposal NNN, codified 2026-08-11 (Gate 2 batch 2)*`.
**E2** — Rule 52 += gate-behaviour claims are re-run claims; calibration ranges carry sample sizes (226).
**E3** — Rule 55 += absence-result checks require a positive control, same instrument, same run (244).
**E4** — Rule 56 += walk the RESUME path before the crash path (230); backup–write adjacency with single-write attribution (243). Two paragraphs.
**E5** — Rule 61 += every pin ships its exact extraction command, portable across tool builds (240).
**E6** — Rule 62 += a bypass branch enumerates every downstream reader of what it skips (269).
**E7** — Checklist #29 += every number by the plan's own mandated method; disciplines inside the instrument (250).
**E8/E9** — `**Version:** 4.85` → `4.86`; `**Last Updated:** 2026-08-08 (v4.85)` → `2026-08-11 (v4.86)`.
**E10** — changelog row prepended as the FIRST data row of the `| Date | Lesson |` table, naming all 37 proposal ids, the two vintages, the append-only precedent, and the Rule-46 splits. ⚠️ **The row DESCRIBES the version tokens it retires and never quotes `**Version:** 4.85` or the old Last-Updated line** (the 344 describe-don't-quote discipline — QA's post-conditions depend on the retired anchors reaching 0).

**Anchors (all complete physical lines, every count measured 1 on 2026-08-11, sha `eb767e32…`):** E1 anchors on Rule 64's Source line; E2–E6 insert BEFORE the next rule's full heading line (53, 56, 57, 62, 63 respectively); E7 inserts before Checklist #29's Source line; E8/E9 swap within unique lines; E10 anchors on the two-line table-header composite. **The script asserts every count before any write — a drifted anchor aborts with zero bytes written.**

**Measured line deltas [EXECUTED 2026-08-11, dry-run on a scratch copy, all ten edits applied]: `197 added / 2 deleted`.** Structural integrity measured on the dry-run result: rules region carries exactly ids 1–94, no gaps, no duplicates, monotonic; all seven co-tenant rule headings (52/55/56/61/62/63/64) still count 1; `## Lifecycle DB Read Protocol (Planner)` still count 1; the checklist extension landed inside item 29 before its Source line; the changelog row is the first data row.

**The script content is deposited by this plan as `knowledge/development/gate2-template-edits.py` — the agent writes it VERBATIM from the plan appendix (§ APPENDIX A below), then runs it.** Any edit to the script is out of scope; a script assertion failure is a HALT, never a patch site.

---

## Conflict Ledger — run-time constraints

- **C1** — every anchor is a complete physical line asserted `count == 1` by the script BEFORE mutation; the script is all-or-nothing (single read, all asserts, single write). Line numbers in this plan are orientation, never operands.
- **C2** — version swaps are surgical against unique full-line anchors; the changelog row describes, never quotes, the retired tokens.
- **C3** — doctrine committed BEFORE the DB flip; a die-between is detectable from the doctrine pins alone.
- **C4** — the backup is ADJACENT to the flip (created after the commit, immediately before Task G) and states the single write it inverts — **this plan now codifies that very rule (243/E4) and complies with it.** A0 state 2 reuse is legitimate; the `BK=37` restorability assert is what restores the guarantee there.
- **C5** — the flip is scoped `WHERE id IN (<the 37>) AND status='accepted'`; `status_updated_by='ceo'`.
- **C6** — `changes()` must equal exactly **37** AND GLOBOK must equal **37**. Sentinels are read before trusting the run; protection is STRUCTURAL (G1 proves the predicate; the `AND status='accepted'` bounds the write).
- **C7** — the timestamp is in-statement `strftime('%Y-%m-%dT%H:%M:%SZ','now')`; no shell variable carries it.
- **C8** — the outside-range capture is taken inside G2's transaction, before the UPDATE. **QA's baseline is always the DEPOSITED capture.**
- **C9** — the commit is path-scoped to exactly `PLANNER_TEMPLATE.md` at the root repo, pathspec ON THE COMMIT (the rule this batch codifies as 75 — comply with it here), post-commit name-only assertion.
- **C10** — SQLite sets `busy_timeout`; `database is locked` is a HALT, not a retry.
- **C11** — post-conditions per edit kind, enumerated in Step 1's table and re-verified independently at QA.
- **C12** — **SCHEDULE ORDER IS LOAD-BEARING:** A0 → A1 → SCRIPT (writes E1–E10) → E0(denylist) → DOC_SHA → F(commit) → F2 → B(backup) → G1 → G2 → G3 → deposits.
- **C13** — E10's changelog row asserts the flip in past tense from Task F onward, earned at G2; A0 state 2 is the F→G2 half-state's designated completion path.
- **C14** — serialized bellows dispatch is a stated assumption; the non-dependent guards: A1's pin, E0's porcelain, F2's verify, G1's PRE/ACC, QA rows 1/6.
- **C15** — **the stale-hazard guard: `ACC` ≠ 73 at G1 → HALT before any write.** Placed in the rehearsal because post-flip the correct value is 36 and the hazard is no longer distinguishable from this plan's own work.
- **C16** — **the ID LIST IS AN IMMUTABLE INPUT** (37 ids, named once in §E1 above, reused verbatim at G1/G2/G3/QA): a sentinel mismatch is NEVER resolved by editing the list. HALT with the numbers.

---

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

Step 1 (DEV) → verdict gate → Step 2 (QA). `pause_for_verdict: always`. No step renames this file.

⚠️ **HALT ROUTING:** **Step 1 reads** this plan file, the live `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`, and the canonical DB. **Step 2 reads** this plan file, the Step-1 dev-log, the live doctrine file, the canonical DB (read-only form), the merged Step-1 evidence captures, and `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`. An unreadable deposited capture is a HALT, not a license to re-derive (distinct from the crash-recovery DECLARED FALLBACK at QA row 6).

---
---

## STEP 1 — DEV (write the script, run it, commit, then flip)

---

> **FIRST — post a short visible chat message (1–2 sentences) confirming you are starting this plan.** Do NOT rename this plan file. You are the Developer. ⚠️ **The doctrine edit lands at the ABSOLUTE path `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — the real governance root, not your worktree.** If you HALT after the script has run, SAY SO LOUDLY: leave the tree as-is (no restore — CEO inspects), report the script's output and `git -C /Users/marklehn/Developer/GitHub status --porcelain -- PLANNER_TEMPLATE.md`.
>
> **⚠️ TASK A0 — PRE-EDIT STATE CLASSIFICATION. FIRST match wins (most-advanced-first):**
> 1. **Flip already done** — all 37 ids read `implemented` (single `COUNT(*)` at the canonical DB path, `-readonly`, `=37`) → verify the doctrine commit exists (newest `git -C /Users/marklehn/Developer/GitHub log --oneline -5 -- PLANNER_TEMPLATE.md` message names the slug `gate2-template-batch-2026-08-11`; missing commit = REPORTABLE anomaly, not license to re-edit). Check whether the crashed run's deposits survived; if `outside-range-ids.txt` is not in the merged tree, deposit a RECOVERY dev-log naming the missing artifacts, produce the G3 read-back fresh, state that QA row 6 takes its DECLARED FALLBACK. Never fabricate a capture. Report complete.
> 2. **Docs committed, flip not done** — newest doctrine commit names the slug AND the 37 still read `accepted` → **skip to TASK B, then TASK G** — NOT Task F. ⚠️ **DOC_SHA on this path from THE COMMIT** (`git -C /Users/marklehn/Developer/GitHub show <that-commit>:PLANNER_TEMPLATE.md | shasum -a 256`), never the live file, and your dev-log says so. A `pre-gate2-template-` backup may exist: rediscover with the PREFIX-ONLY `find` form (no `-newer`), REUSE it; run the `BK=37` restorability assert either way. Re-run the porcelain check; a dirty file ON TOP of the commit is reported LOUDLY, never swept in.
> 3. **Docs modified-uncommitted** — porcelain non-empty for the doctrine path → **HALT.** Recovery route: run the per-edit probe sweep (the ten E-probes from QA rows 2–5) against the live file, DEPOSIT the landed/not-landed table at `knowledge/qa/evidence/gate2-template-batch-2026-08-11/resume-sweep.txt`, report. CEO directs restore-and-redo or complete-forward. ⚠️ The script is all-or-nothing, so a PARTIAL application signature (some probes landed, some not) means a foreign or manual edit — say so explicitly.
> 4. **Fresh-with-unexplained-backup** — a `pre-gate2-template-` backup exists with no doctrine commit and 37 `accepted` → **HALT.**
> 5. **Fresh** — porcelain clean for the doctrine path; live version line reads `4.85`; no `pre-gate2-template-` backup; `COUNT(*) WHERE id IN (<the 37>) AND status='accepted' AND route='codify' AND target_artifact='PLANNER_TEMPLATE.md'` = **37** → proceed to A1.
>
> ⚠️ **Version cross-check on every path:** neither `4.85` nor a `4.86` whose changelog's first data row names this slug → **HALT; re-basing needed.** Match by SLUG. Observed state matching NO branch → HALT with the full triple (porcelain, version line + first changelog row, per-id status read-back).
>
> **⚠️ TASK A1 — RE-VERIFY THE AUTHORING PIN.** `shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` must equal
> `eb767e3284f1a42b70aec9b3a1ab50226a13276f31f854d4117de26de4815b5f`
> **Mismatch → HALT** (every anchor was proven against these bytes; the script will also re-assert each anchor, but the sha is the cheap first gate). The anchor re-proof is the script's job — its asserts ARE the A1 anchor table, executed structurally.
>
> **TASK SCRIPT — WRITE AND RUN THE GIVEN BUILDER.** Write § APPENDIX A's content VERBATIM to `knowledge/development/gate2-template-edits.py` in your worktree via your file-WRITE tool (compose nothing; the appendix is the source of truth). Then run:
> `python3 <your-tree-abs>/knowledge/development/gate2-template-edits.py /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
> (SRC and DST are BOTH the live absolute path — the script reads once, asserts every anchor, mutates in memory, writes once.) Assert: exit 0 and the final line `OK — 10 edits applied: …` naming all ten labels. **Any AssertionError → HALT and quote it verbatim — the file is UNTOUCHED by construction (the write is the script's last statement); do not edit the script, do not retry with modifications.**
> Then verify the post-conditions (C11) via Bash probes — each `grep -cF` against the live absolute path:
> | probe | expected |
> |---|---|
> | `### 65. Verify a mandated block in the SECTION the parser reads, not merely present in the deposit` | 1 |
> | `### 94. Author every task as ordered sub-items from the first draft` | 1 |
> | `codified 2026-08-11 (Gate 2 batch 2)` | **30** |
> | `*Source: proposal 220, lesson 2026-08-03*` (Rule 64 tail, co-tenant intact) | 1 |
> | `Gate-behaviour sentences are inherited claims` | 1 |
> | `An absence-result check requires a positive control` | 1 |
> | `Walk the RESUME path before the crash path (proposal 230` | 1 |
> | `A backup and the write it inverts are adjacent (proposal 243` | 1 |
> | `Every pin ships its extraction command` | 1 |
> | `A bypass branch enumerates every downstream reader of what it skips` | 1 |
> | `Every number a plan states is produced by the plan's own mandated method` | 1 |
> | `**Version:** 4.86` | 1 |
> | `**Version:** 4.85` | **0** |
> | `**Last Updated:** 2026-08-11 (v4.86)` | 1 |
> | `v4.86: Gate 2 batch 2` | 1 |
> | `v4.85:` (old changelog row, history intact) | 1 |
> | `## Lifecycle DB Read Protocol (Planner)` | 1 |
> Plus the structural check, run exactly: `python3 -c "import io,re;L=io.open('/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md',encoding='utf-8').read().split(chr(10));s=L.index('## Orchestration Plan Rules');e=next(i for i,l in enumerate(L) if l.startswith('## Lifecycle DB Read Protocol'));n=[int(re.match(r'### (\d+)\.',l).group(1)) for l in L[s:e] if re.match(r'### \d+\.',l)];print('RULES', len(n), min(n), max(n), n==sorted(n), len(set(n))==len(n))"` → must print `RULES 94 1 94 True True`. Any mismatch → HALT.
>
> **⚠️ TASK E0 — PRE-COMMIT DENYLIST.** Porcelain: expect `PLANNER_TEMPLATE.md` modified. **HALT iff any OTHER governance doctrine file is dirty: `DRAFTING_CYCLE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `READONLY_AUDIT_CONTRACT.md`, `SPECIALIST_TEMPLATE.md`, `INTERMEDIATE_DECISION_PHRASES.md`.** Other dirty root files are REPORTED, never a HALT (the commit is path-scoped; F2 proves the contents).
>
> **⚠️ TASK DOC_SHA — PIN BEFORE THE COMMIT.** `shasum -a 256` the edited file; record as **DOC_SHA**.
>
> **TASK F — COMMIT, path-scoped, BEFORE the DB (C3):** `git -C /Users/marklehn/Developer/GitHub add PLANNER_TEMPLATE.md && git -C /Users/marklehn/Developer/GitHub commit -m "[<id>] gate2(gate2-template-batch-2026-08-11): 37 proposals — 30 new rules 65-94 + 7 extensions — template 4.85 -> 4.86" -- PLANNER_TEMPLATE.md` (`<id>` from your plan filename). Record `git -C /Users/marklehn/Developer/GitHub diff HEAD^ HEAD --numstat -- PLANNER_TEMPLATE.md` — expect **`197	2	PLANNER_TEMPLATE.md`**; different → HALT, do not rationalize. ⚠️ The `-C` is load-bearing; a bare form diffs your worktree's repo.
>
> **TASK F2 — POST-COMMIT VERIFY:** `git -C /Users/marklehn/Developer/GitHub show HEAD:PLANNER_TEMPLATE.md | shasum -a 256` == DOC_SHA; `git -C /Users/marklehn/Developer/GitHub show HEAD --name-only --format=` lists exactly `PLANNER_TEMPLATE.md`. Mismatch → HALT.
>
> **TASK B — BACKUP (C4):** `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".backup /Users/marklehn/Developer/GitHub/lessons-forge/pre-gate2-template-$(date -u +%Y%m%d_%H%M%S).db"` — exit 0, empty stderr. Locate via prefix-only `find`. ⚠️⚠️ **RESTORABILITY ASSERT, EVERY PATH REACHING THE FLIP:** `sqlite3 -bail -readonly "<found-backup>" ".timeout 5000" "SELECT 'BK='||COUNT(*) FROM lesson_proposals WHERE id IN (223,225,226,228,229,230,236,239,240,242,243,244,250,255,257,264,265,266,267,268,269,274,277,280,281,282,284,288,289,293,297,303,305,306,307,310,314) AND status='accepted';"` → **`BK=37`**, exit 0, empty stderr. Anything else → HALT before the flip.
>
> **TASK G — THE FLIP: rehearsal → flip → read-back.** ⚠️ NO heredocs. Author each `.sql` via file-WRITE, run `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".read <abs-path>"`. ⚠️⚠️ **`-bail` MANDATORY on every invocation, each asserted exit 0 + EMPTY stderr** (fresh scratch dir OUTSIDE every git tree, created and used in the same invocation: `S=$(mktemp -d) && sqlite3 -bail … 2>"$S/g-stderr.txt"; echo "exit=$?"; cat "$S/g-stderr.txt"`). Measured rationale (330): without `-bail`, a daemon-held lock skips the failed `BEGIN IMMEDIATE` and commits an un-bracketed flip on a green-looking run. Captures land in YOUR tree's evidence dir — `mkdir -p` first, derive the ABSOLUTE `.output` path from `pwd` when authoring the `.sql`.
>
> **G1 — REHEARSAL (`knowledge/development/gate2-template-flip-rehearsal.sql`), content exactly:**
> ```
> BEGIN IMMEDIATE;
> SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id IN (223,225,226,228,229,230,236,239,240,242,243,244,250,255,257,264,265,266,267,268,269,274,277,280,281,282,284,288,289,293,297,303,305,306,307,310,314) AND status='accepted' AND route='codify';
> SELECT 'ACC='||COUNT(*) FROM lesson_proposals WHERE status='accepted' AND route='codify';
> SELECT 'MAXID='||MAX(id) FROM lesson_proposals;
> ROLLBACK;
> ```
> Assert **`PRE=37`**, **`ACC=73`** (C15: fewer → HALT, the stale hazard; more → HALT, in-window routing landed), **`MAXID=314`** (higher is reported-benign; keep the `id <= 314` bound regardless — in-window inserts are excluded by construction). `PRE` ≠ 37 → HALT naming which ids are off and their current status. **The rehearsal HALTS BEFORE any write; the CHANGES sentinel can only report after commit — prevention and reporting are different guards.**
>
> **G2 — THE FLIP (`knowledge/development/gate2-template-flip.sql`), content exactly** (`.output` path from `pwd`):
> ```
> BEGIN IMMEDIATE;
> .output <your-tree-abs>/knowledge/qa/evidence/gate2-template-batch-2026-08-11/outside-range-ids.txt
> SELECT id||'|'||category||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'')||'|'||COALESCE(status_updated_by,'') FROM lesson_proposals WHERE id <= 314 AND id NOT IN (223,225,226,228,229,230,236,239,240,242,243,244,250,255,257,264,265,266,267,268,269,274,277,280,281,282,284,288,289,293,297,303,305,306,307,310,314) ORDER BY id;
> .output stdout
> UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (223,225,226,228,229,230,236,239,240,242,243,244,250,255,257,264,265,266,267,268,269,274,277,280,281,282,284,288,289,293,297,303,305,306,307,310,314) AND status='accepted';
> SELECT 'CHANGES='||changes();
> SELECT 'GLOBOK='||COUNT(*) FROM lesson_proposals WHERE id IN (223,225,226,228,229,230,236,239,240,242,243,244,250,255,257,264,265,266,267,268,269,274,277,280,281,282,284,288,289,293,297,303,305,306,307,310,314) AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z' AND status_updated_at NOT IN ('2026-08-09T01:20:01Z','2026-08-11T13:42:09+00:00');
> COMMIT;
> ```
> ⚠️ **The two-value `NOT IN` is load-bearing on BOTH sides (Environment fact 5):** the 21 Z-form rows' prior value MATCHES the GLOB, so only the exclusion guards them; the 16 offset rows are structurally non-matching but the exclusion is kept uniform. **Read both sentinels: `CHANGES=37` and `GLOBOK=37`. Either off → HALT with the numbers; the backup is the CEO's restore instrument.** Capture file must exist with **277 lines** (314 rows − 37, ids contiguous, measured 2026-08-11). ⚠️ The line-count assert reads AFTER commit — a mismatch does NOT mean re-run; record, name differing ids, HALT with the flip reported as landed. **The 37-id list is IMMUTABLE (C16).**
>
> **G3 — READ-BACK** (`-readonly` added): `sqlite3 -bail -readonly /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" "SELECT id||'|'||status||'|'||status_updated_by||'|'||status_updated_at FROM lesson_proposals WHERE id IN (223,225,226,228,229,230,236,239,240,242,243,244,250,255,257,264,265,266,267,268,269,274,277,280,281,282,284,288,289,293,297,303,305,306,307,310,314) ORDER BY id;"` → deposit RAW as `flip-readback.txt` — all 37 rows `implemented|ceo|<Z-form timestamp>`, none equal to either pinned prior value.
>
> **Output Receipt required** — DOC_SHA, commit hash, numstat pair, PRE/ACC/MAXID/CHANGES/GLOBOK values, every file deposited. **End with `### Ledger Updates` and `#### Prompt Feedback`.**
>
> **⚠️ FINAL ACTION — COMMIT YOUR DEPOSITS IN THE WORKTREE** (pathspec on the COMMIT naming exactly the Scope files for your A0 path; assert `git show --name-only --format= HEAD` prints exactly them). **`lessons-forge.db` and the `pre-gate2-template-*.db` backup are deliberately ABSENT from Scope — the DB is untracked by shop policy.**
>
> **Scope:**
> - `knowledge/development/dev-log-gate2-template-batch-step-1-2026-08-11.md`
> - `knowledge/development/gate2-template-edits.py`
> - `knowledge/development/gate2-template-flip-rehearsal.sql`
> - `knowledge/development/gate2-template-flip.sql`
> - `knowledge/qa/evidence/gate2-template-batch-2026-08-11/outside-range-ids.txt`
> - `knowledge/qa/evidence/gate2-template-batch-2026-08-11/flip-readback.txt`
>
> ⚠️ On A0 state 3 ONLY, `knowledge/qa/evidence/gate2-template-batch-2026-08-11/resume-sweep.txt` joins Scope. The doctrine file is NOT a deposit — committed at Task F, verified at F2.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-gate2-template-batch-step-1-2026-08-11.md`
> - `lessons-forge/knowledge/development/gate2-template-edits.py`
> - `lessons-forge/knowledge/development/gate2-template-flip-rehearsal.sql`
> - `lessons-forge/knowledge/development/gate2-template-flip.sql`
> - `lessons-forge/knowledge/qa/evidence/gate2-template-batch-2026-08-11/outside-range-ids.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-template-batch-2026-08-11/flip-readback.txt`

## STEP 2 — QA

---

> **FIRST — Deliverable Verification (Rule 8 / Rule 17).** Open the Step-1 dev-log, confirm its Output Receipt is Complete, verify every claimed file exists and carries the described change. Table: `| Deliverable | Expected | Status (✅/❌) | Evidence |`. Any ❌ → HALT; no edits yourself.
>
> **MANDATORY — Rule 20 self-check (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`, exact template).** Fill: `plan_slug`: `gate2-template-batch-2026-08-11`; `qa_report_path`: `<your-tree-abs>/knowledge/qa/gate2-template-batch-qa-2026-08-11.md`; `evidence_dir`: `<your-tree-abs>/knowledge/qa/evidence/gate2-template-batch-2026-08-11/`; `required_evidence_files`: `[doc-integrity.txt, db-invariants.txt, gate-neutrality.txt, pytest_targeted.txt]`. Deposit all four BEFORE running the block. **Include the block's literal stdout: the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, byte-exact (em-dash U+2014).**
>
> ⚠️ **After the verification table, write exactly `## Evidence and Narrative`**; Rule 20 stdout, Output Receipt and `### Ledger Updates` under `##`-level headings.
>
> **Evidence rule:** RAW command output, never a summary. **ONE read-only DB form for every query:** `sqlite3 -bail -readonly "/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db" ".timeout 5000" "<SQL>"`, exit-0/empty-stderr asserted.
>
> **Verification table, one row per claim (HALT on any FAIL; rows 6 and 7 carry explicit report-not-halt branches).**
>
> **1. DOC INTEGRITY — git is the primary referent.** Discover the commit independently (newest `git -C /Users/marklehn/Developer/GitHub log --format='%H %s' -20 -- PLANNER_TEMPLATE.md` naming the slug). Three-way sha agreement: commit content == live file == dev-log DOC_SHA (empty-input signature `e3b0c442…` = "the show failed"). Porcelain EMPTY; `show <commit> --name-only --format=` lists exactly `PLANNER_TEMPLATE.md`. → `doc-integrity.txt`
> **2. THE BLOCK LANDED WHOLE.** `grep -cF '### 65. Verify a mandated block in the SECTION the parser reads, not merely present in the deposit'` → 1; `grep -cF '### 94. Author every task as ordered sub-items from the first draft'` → 1 (head and tail of the 30-rule block — an insertion truncated anywhere between drops the tail); `grep -cF 'codified 2026-08-11 (Gate 2 batch 2)'` → **30** (one per new rule — the per-rule presence count); `grep -cF '*Source: proposal 220, lesson 2026-08-03*'` → 1 (Rule 64's tail, co-tenant intact). **Structural integrity, run exactly the Step-1 python one-liner** → `RULES 94 1 94 True True`. → `doc-integrity.txt`
> **3. THE SEVEN EXTENSIONS LANDED, AND THEIR CO-TENANTS SURVIVED.** Each extension head-phrase → 1: `Gate-behaviour sentences are inherited claims` / `An absence-result check requires a positive control` / `Walk the RESUME path before the crash path (proposal 230` / `A backup and the write it inverts are adjacent (proposal 243` / `Every pin ships its extraction command` / `A bypass branch enumerates every downstream reader of what it skips` / `Every number a plan states is produced by the plan's own mandated method`. AND the receiving/adjacent rule headings each → 1: `### 52. Re-verify inherited claims`, `### 53. Region-scoped metrics`, `### 55. Assert a positive signal`, `### 56. Resume machinery is justified`, `### 57. Generalizing a guard`, `### 61. Pin run-time-copied artifacts`, `### 62. Establish that a recovered-from state`, `### 63. Read the DELIVERY code`. All new-text probes measured **0 pre-edit** (earnable). → `doc-integrity.txt`
> **4. NUMSTAT vs THE PIN.** `git -C /Users/marklehn/Developer/GitHub diff <commit>^ <commit> --numstat -- PLANNER_TEMPLATE.md` → exactly `197	2`. → `doc-integrity.txt`
> **5. VERSION + CHANGELOG.** `grep -cF '**Version:** 4.86'` → 1; `grep -cF '**Version:** 4.85'` → 0; `grep -cF '**Last Updated:** 2026-08-11 (v4.86)'` → 1; `grep -cF 'v4.86: Gate 2 batch 2'` → 1; `grep -cF 'v4.85:'` → 1 (prior row intact); the new row is the FIRST data row after `| Date | Lesson |` + separator (assert via `grep -F -A 2 '| Date | Lesson |'` showing the v4.86 row third); ⚠️ **the row's substantive TAIL probed:** `grep -cF 'Numbering append-only per the 4.83 precedent'` → 1 (measured 0 pre-edit — earnable, satisfied only by the row landing whole). → `doc-integrity.txt`
> **6. FLIP READ-BACK + BLAST RADIUS, RE-DERIVED, PARTITIONED.** (a) All 37 ids `implemented|ceo`, timestamps Z-GLOB-matching AND `NOT IN ('2026-08-09T01:20:01Z','2026-08-11T13:42:09+00:00')`; exactly 37 rows; `category` preserved on all (expect all `governance_rule`). (b) `accepted|codify` count → **36** (73 − 37); lower → name which ids left the set. (c) Re-run the EXACT capture projection (`id <= 314 AND id NOT IN (<the 37>)`), diff against the deposited `outside-range-ids.txt` (277 lines). Partition: (i) any of the 37 ids in a differing line → HALT (malformed); (ii) id present-in-capture but absent-now → HALT (deleted corpus row); (iii) all else = CONCURRENT ACTIVITY — name each id and before/after, confirm none is in the 37, do NOT halt. Predicate never widened past 314. → `db-invariants.txt` ⚠️ **DECLARED FALLBACK (only if Step-1's receipt reports the capture lost):** run the degraded sweep, label `DEGRADED`: (i) `COUNT(*) WHERE id <= 314` → 314; (ii) rows sharing 312's—no, sharing THE FLIP's stamp: `SELECT id FROM lesson_proposals WHERE status_updated_at = (SELECT status_updated_at FROM lesson_proposals WHERE id = 223)` → must include all 37 (statement-stable `'now'`); extra co-stamped ids REPORTED, HALT only if one is a row this plan must never touch AND moved to `implemented`.
> **7. TARGETED TESTS + PREMISE.** `find /Users/marklehn/Developer/GitHub/lessons-forge/src -name 'test_*.py'` → exactly `test_lessons_forge.py` (a second module = report + run whole `src/`, never HALT). `python3 -m pytest src/test_lessons_forge.py -q` → zero regressions vs baseline (55 passed / 0 skipped, measured 2026-08-11; baseline moved → report the delta). → `pytest_targeted.txt`
> **8. GATE-NEUTRALITY WITH POSITIVE CONTROL.** (a) Rule-number coupling: `grep -rohE 'Rule [0-9]+' /Users/marklehn/Developer/GitHub/bellows/gates.py /Users/marklehn/Developer/GitHub/bellows/scripts/plan_lint.py | sort -u` → exactly `Rule 20`, `Rule 22`, `Rule 26` (the authoring measurement; anything new → HALT, a coupling landed in-window). (b) Line-citation sweep (the new Rule 76 applied to its own shipping): `grep -rn -E 'PLANNER_TEMPLATE[^ ]*:[0-9]+' /Users/marklehn/Developer/GitHub/bellows --include='*.py'` → zero hits. (c) POSITIVE CONTROL: `grep -cF 'Rule 20' /Users/marklehn/Developer/GitHub/bellows/gates.py` → nonzero (same instrument, known-present token). (d) Zero-match `grep -c` prints 0 and exits 1 — the count is the assertion. → `gate-neutrality.txt`
> **9. CONSUMER SEMANTICS.** (a) Quote `lessons-forge/src/lessons_forge.py:31` verbatim — `implemented` IS terminal, `accepted` is NOT. (b) Run `get_unclassified_entries` (read-only) → the 37 source entries (215, 217, 218, 220, 221, 222, 228, 231, 232, 234, 235, 236, 242, 247, 249, 256, 257, 258, 259, 260, 261, 266, 269, 272, 273, 274, 276, 280, 281, 285, 289, 295, 297, 298, 299, 302, 306) ALL ABSENT from the work list — dispositioned before, dispositioned after. Paste source quote + raw helper output. → `db-invariants.txt`
> **10. THE TEMPLATE STILL PARSES AS A TEMPLATE.** The heading census: `grep -cE '^## '` → **30, unchanged from pre-edit** (measured 2026-08-11 on both sides of the dry-run; the edits add zero `##`-level headings). And `grep -cE '^### [0-9]+\. '` → **137** (pre-edit 107 + the 30 new rules — both sides measured on the dry-run, per the numbers-by-mandated-method rule this batch itself codifies at Checklist #29). Deviation → HALT: an edit leaked structure. → `doc-integrity.txt`
>
> **Then `## Evidence and Narrative`, then the Output Receipt.**
>
> ⚠️ **`### Ledger Updates`** — author via Write/Edit, EXACTLY ONCE, `##`-level scope after `## Evidence and Narrative`, blank line after the last subsection, one row per bullet, no wrapped items.
>
> **`#### Forward Register`: the word `NONE`.** Deliberate non-emission — no FORWARD rows are owed by this plan (the Rule-46 split halves ride bellows-project plans; Rule 42 status updates are Planner-direct at wrap). A genuinely NEW run-time discovery replaces `NONE`, one physical line per item.
>
> **⚠️ FINAL ACTION — COMMIT YOUR DEPOSITS**, pathspec on the COMMIT, name-only assertion. **`lessons-forge.db` never staged.**
>
> **Scope:**
> - `knowledge/qa/gate2-template-batch-qa-2026-08-11.md`
> - `knowledge/qa/evidence/gate2-template-batch-2026-08-11/doc-integrity.txt`
> - `knowledge/qa/evidence/gate2-template-batch-2026-08-11/db-invariants.txt`
> - `knowledge/qa/evidence/gate2-template-batch-2026-08-11/gate-neutrality.txt`
> - `knowledge/qa/evidence/gate2-template-batch-2026-08-11/pytest_targeted.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate2-template-batch-qa-2026-08-11.md`
> - `lessons-forge/knowledge/qa/evidence/gate2-template-batch-2026-08-11/doc-integrity.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-template-batch-2026-08-11/db-invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-template-batch-2026-08-11/gate-neutrality.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-template-batch-2026-08-11/pytest_targeted.txt`

---

## Drafting Cycle

**Tier:** T2 — trigger fired: T-6 (governance surface: one doctrine file + the proposal corpus). Clone lineage: mechanism cloned from **executable-344** (the newest same-class Gate-2 plan, closed same-day with 2/2 clean gates), whose own origin is executable-330; both of 344's measured corrections are inherited AND re-derived here rather than carried (the per-vintage timestamp exclusion — re-measured, and this batch's exposure is the MIRROR of 344's; the describe-don't-quote History discipline — applied to E10).

**Walks:** ⚠️ **ZERO — the same declared partial DRAFTING-CYCLE deviation as plan 344, by the same standing CEO direction, recorded here with its residue.**

**What ran:** §2.0's context pin in full, plus the batch-composition measurement the pin mandates. Walk register (walk 0 + verdict) committed at `governance/knowledge/research/walk-register-gate2-template-batch-2026-08-11.md` (root commit `e5ae610`) per v2.2 §3. **Direction verdict: PROCEED** — clone origin confirmed at source (344, closed, clean); edit mechanism proven by executed dry-run (all ten anchors count-1, all-or-nothing script, numstat `197 2`, rules integrity 94/monotonic); scope licensing confirmed (37 rows `accepted|codify|PLANNER_TEMPLATE.md`, re-verified after 344's flip moved the corpus floor to 73).

**What the pin caught (the deviation's return, as specifics):**
1. **The batch premise was stale two ways** — the baton said 10 items; measurement says 37 (21+16 across two Gate-1 vintages).
2. **The Z-GLOB's protective value is INVERTED from 344:** there the prior value was structurally non-matching and the GLOB alone sufficed; here 21 of 37 prior values MATCH the GLOB (`2026-08-09T01:20:01Z`), so the explicit two-value `NOT IN` carries the guard. A clone that carried 344's single-value exclusion would have shipped a sentinel vacuous on 21 rows.
3. **The stale-hazard floor moved same-day** (74 → 73 after 344) — a clone inheriting `ACC=74` would false-HALT a correct run.
4. **Zero `:NN` line citations of the template exist in bellows code** (the new Rule 76's own check, run before shipping the rule) — so the 197-line insertion breaks no code coupling; the only rule-number couplings are 20/22/26, all untouched by append-only numbering.
5. **The 264-class shape decision:** one block anchor instead of thirty per-rule anchors — the pin's geometry measurement is what licensed it.

**The cost, recorded:** no adversarial read of the 30 composed rule texts as doctrine prose has occurred — the dry-run proves the edits LAND; nothing in this process reads what the rules SAY the way a lens would. For a batch whose content is thirty new normative rules, that residue is materially larger than 344's single-clause equivalent, and it is the honest price of the deviation. Residue by class: (a) no adversarial prose read of E1's thirty rule bodies (probe earnability and byte effect verified; wording-to-a-future-reader unverified); (b) no independent QA-table-as-a-system pass; (c) no cold-panel clone-diff against 344/330; (d) §2.8 oscillation untestable (no walks, no folds).

**Conformance (§5) — last run at the pre-deposit freeze, `plan_lint` → EXIT 0, measured at the deposit-shaped path (lint state is location-dependent).** All 8 checks PASS. **THREE warnings stand, each classified; none unexplained:** (1) the missing-per-lens-result-lines warning — the EARNED deviation, correctly detected and deliberately left standing; its text is DESCRIBED, never quoted, because the check substring-matches this very block (the vanishing-WARN failure plan 344's authoring measured live); (2) the missing cold-panel-line warning — same class, same deliberate non-silencing; (3) `(o1)` missing-path on the conditional `resume-sweep.txt` — the A0-state-3-only artifact, the standing known-benign class every plan in this lineage declares. ⚠️ A fourth warning — `(o1)` missing-path on the governance walk-register citation — fired on the pre-commit run and **cleared EARNED, not by rewording**: it vanished from the next run because the register was actually committed at the governance root (`e5ae610`), which is exactly the §3 discipline — the condition changed, not the sentence.

**Closing:** ⚠️ **This plan does NOT meet §2's doneness bar and does not claim to** — no walk ran; deposited as a declared deviation with residue enumerated. Freeze-time re-verification, all re-derived against live state: authoring sha `eb767e32…`, dry-run numstat `197 2`, rules integrity `94 1 94 True True`, all block/extension/version/changelog probes earnable (0 pre-edit) and landing at their pinned counts, PRE=37 / ACC=73 / capture=277 / BK=37 all measured at source, both prior-value exclusions verified against the actual 37 rows. Fold-and-deposit exactly once.

---

## APPENDIX A — `gate2-template-edits.py`, the GIVEN builder (write VERBATIM, run once)

```python
#!/usr/bin/env python3
# Gate-2 batch 2 builder - PLANNER_TEMPLATE v4.85 -> v4.86.
# All-or-nothing: reads SRC once, asserts every anchor count==1 BEFORE any
# mutation, applies all ten edits in memory, writes DST once at the end.
# An assertion failure anywhere aborts with ZERO bytes written.
import io, sys

SRC = sys.argv[1]
DST = sys.argv[2]
s = io.open(SRC, encoding='utf-8').read()
edits_applied = []

def rep(old, new, expect=1, label=""):
    global s
    got = s.count(old)
    assert got == expect, f"ANCHOR COUNT {label}: expected {expect}, got {got} for {old[:60]!r}"
    s = s.replace(old, new, expect)
    edits_applied.append(label)

D = "2026-08-11"
def rule(num, pid, title, body):
    return f"### {num}. {title}\n\n{body}\n\n*Source: proposal {pid}, codified {D} (Gate 2 batch 2)*\n"

NEW_RULES = "\n".join([
rule(65, 223, "Verify a mandated block in the SECTION the parser reads, not merely present in the deposit",
"A daemon-parsed block (Ledger Updates, Forward Register, Prompt Feedback) counts as delivered only when its text sits inside the section the parser scopes to — correctly formatted and correctly located are different claims, and a cross-reference satisfies a text-capturing check as well as content does. Verification of any channel emission asserts the block's position against the parser's input scope (which section, which heading level), never bare presence in the deposit. Measured: the Forward Register lost every item of an emission because the substantive block was written outside the Ledger Updates section — the channel's third distinct failure mode."),

rule(66, 225, "A mandated requirement lives in the step that must comply",
"For every mandated requirement, name the step that must COMPLY and confirm the requirement's text is in that step's prompt — presence anywhere in the plan is not compliance-reachable, and a rule enforced by a QA row must also be stated where the artifact is produced. Sweep both directions: producer-missing (the check exists, the producing step never heard the rule) and consumer-missing (the producing step complies, nothing would notice a violation). Measured: three instances in one drafting cycle of a requirement written into the checking step only, each with a structural home — in the wrong step — so the structural-home rule (54) never fired."),

rule(67, 228, "Before authoring verification for a delivery channel, read the delivering code and state which artifact it consumes",
"A check aimed at a different artifact is a proxy no matter how exactly it reproduces the consumer's logic. Before authoring any verification for a delivery channel, read the delivering code to find WHICH ARTIFACT it consumes (transcript vs deposit vs DB row), and state that artifact in the check itself. Measured: a channel failed four distinct ways across three sessions because every check read the deposited file while the daemon reads the transcript — a green check over a total loss."),

rule(68, 229, "Channel items are single physical lines; downstream of a splitter, compare content, not counts",
"Constrain the shape that makes silent loss possible: no Forward Register (or other channel) item may wrap onto a second physical line, because line-pattern splitters keep only lines matching the bullet pattern and drop continuations. A cardinality assertion is blind to loss WITHIN an item — five written, five recovered, exit zero, and every item truncated. When items carry substance, verification compares content, not counts (the intra-item form of the count-is-not-a-value-guard lesson)."),

rule(69, 236, "A parser-terminator fix belongs to the class, not the instance",
"When a fix turns on a parser's terminator, enumerate every construct that parser terminates the same way and fix the whole set — in an ordered set of parsed subsections, the LAST one is structurally the exposed one (it terminates only by blank line or end-of-stream). Measured: a terminator fix applied to one subsection while the mechanism was subsection-generic; the fold landed where the defect was noticed, not where the mechanism lives — the fourth instance of that class."),

rule(70, 239, "A declared-outputs block lists only what the step produces on EVERY path",
"Name conditional artifacts in prose, where the tolerant gate can still see them — never in the Deposits block, where the strict gate will demand them on paths that don't produce them. When two checks read the same declaration, establish each one's polarity separately: the scope check TOLERATES extras and fails unnamed changes; the deposit check REQUIRES every name and fails absences. One list read with opposite polarities means a conditional entry guarantees a failure on some path. (Extends Rule 26's block convention with the polarity discipline.)"),

rule(71, 242, "Audit every new verification referent for true independence",
"A referent is independent only if it exists BEFORE the actor acts and OUTSIDE the actor's control. A referent sourced from the actor's own record — a diff compared against the deltas the actor recorded, a hash compared against a baseline the actor supplied — reproduces the circularity it exists to break, with the form of verification and none of its content. Audit each new referent against this test at authoring. Measured: two of three referents in one edit were circular in exactly this way."),

rule(72, 255, "Declare polarity for every two-direction number in a diagnostic",
"When a diagnostic question reports a number that can move in two directions, state which direction is good and for whom — or state explicitly that both movements are legitimate and the weighing is not the question's to make. Without the declaration, individually-correct patches accumulate contradictions: one check killing a proposal on WIDE firing while its sibling kills it on NARROW, and a third pricing the identical movement as a virtue. One quantity, two legitimately opposed values, no verdicts in any question."),

rule(73, 257, "Record a constraint and its violation-catching check in the same edit",
"A rule in prose — in LESSONS.md or in the plan's own ledger — has no mechanical consequence, and the author is the least reliable enforcer of a rule they have just written. When a constraint is recorded in a plan, add the check that would catch its violation in the SAME edit. Treat recurrence of an already-recorded lesson as evidence it needs MECHANISING — route it to the forge as a mechanization candidate rather than restating it in prose. Measured: four recurrences in one cycle of the same author's own recorded constraints."),

rule(74, 264, "A directional insert anchors on a COMPLETE line, and a mechanism fix sweeps for its mirror",
"An insert-after or insert-before edit anchors on a COMPLETE physical line with the full final composition spelled out in the new text — anchoring on a line prefix inserts at the prefix boundary and can split the line, and every presence grep, count, and date pin then passes on the intact fragments. After fixing a mechanism defect at one site, sweep the plan for the same mechanism in mirror form (insert-after has an insert-before twin). Add one verification that SPANS the would-be damage point, so a split cannot pass unnoticed."),

rule(75, 265, "Path-scope the COMMIT, not just the add, and assert the commit's contents",
"`git add <path> && git commit` is not a path-scoped commit: a bare `git commit` commits the ENTIRE index, so any foreign change already staged rides in silently — and in a root repo that is a live working area, pre-staged entries are a normal state. Use `git commit -m '...' -- <path>` with the pathspec on the COMMIT, and pair it with the post-commit assertion `git show --name-only --format= HEAD` printing exactly the intended paths. Content-hash and log checks do not catch this: the hash reads only the intended blob, and the log check sees only commits touching the intended path."),

rule(76, 266, "Before editing a doc, grep the codebase for line-number citations of it",
"A `:NN`-style line citation inside running code is a hard constraint on a doc edit's map: any edit changing the line count above NN breaks the citation silently. Before editing a doc, grep the codebase for `:NN` citations of that file and design around each — in-place rewrites above cited lines, insertions only below them — then verify BY VALUE (the cited line still says the cited thing), never by arithmetic. When authoring new checks, cite doctrine by section anchor or literal text, never by line number."),

rule(77, 267, "Sweep the source deposit's closing sections for directives addressed to a future plan",
"A diagnostic's deposit may close with instructions addressed to the plan that will implement it — a required literal phrase, a mandated check, a naming convention the daemon parses. Those directives are REQUIREMENTS, not commentary, and they are invisible to every review of the intermediate artifacts (baton, decision record): only a diff against the SOURCE deposit finds them. When authoring a plan that implements a diagnostic's findings, sweep the deposit's closing sections; machine-parsed conventions deserve a grep-verifiable check at deposit time. (Extends Rule 27's citation discipline to the directive sweep.)"),

rule(78, 268, "Construct the mid-band cases for every threshold or quantifier clause before shipping",
"For any threshold, quantifier, or every/most/any clause, construct the mid-band cases BEFORE shipping: most-but-not-all, sibling verbs the clause's own verb does not cover, aggregates of individually-small parts. Price each constructed case as caught, dropped-and-accepted, or dropped-and-unpriced — and record each acceptance in the artifact with a boundary test. Measured: a clause priced only at its poles (the census cases and the constructed 100% case) silently reclassified a most-rows mutation, a full-table DELETE under a sibling verb, and a schema migration."),

rule(79, 274, "A halt that offers options banners the inferred choice at the next gate",
"The verdict grammar is one bit — a continue issued for ANY reason is structurally identical to every other continue, and no later step can distinguish the intents. When a halt offers the CEO options, the accepting branch must BANNER which option it inferred, in its chat message and Output Receipt, at the next gate the CEO reads — so a mis-read costs one verdict gate rather than the run. (The verdict-channel constraint itself is bellows-owned; this is the authoring half.)"),

rule(80, 277, "An authoring-time id is a prediction; the verify-at-deposit clause names every site",
"Any plan id read from `id_sequence` at authoring is a PREDICTION — an in-window deposit by another terminal consumes it. Carry a verify-at-deposit clause that NAMES every site the id token appears in: backup globs, copy-asides, resume-glob guards, deposit filenames. At deposit: re-read `id_sequence`, re-token every named site to the actual id, and record the drift as retraction history. A bare 'verify the id' leaves the glob tokens stale — the clause works only because it enumerates. Measured live: a plan authored against 310 deposited as 311."),

rule(81, 280, "Census every copy of an enum before adding a value",
"A recognized-value set lives in more copies than the branch being edited: code branches, lint token sets, claim validators, and governance prose. Before adding any enum value, census EVERY copy with `grep -F` across the repo AND the template; ship all copies in one plan or enumerate the deferral explicitly. Treat the census as the plan's own Site list with a both-edits-or-neither clause per copy-pair. Measured: a new mode shipped in one branch while three other copies drifted, one of them a hard-FAIL lint check."),

rule(82, 281, "Price a change at its IN-population rate and argue against the strongest counterexample",
"For any headline rate justifying a change, compute the rate over the IN-population — the rows the change actually affects — and present that number first; a cross-population average dilutes the effect with rows that stay untouched. Then name the strongest single counterexample FROM the in-population and argue against it specifically, not against the average case. Measured: a mechanization priced at a 3.08% cross-population rate was actually 4.1% in-population, and the strongest counterexample (a tranche plan saved by a rote-looking pause) sat exactly in the opt-in target slice."),

rule(83, 282, "State the exact enforcement tier when correcting enforcement claims",
"When correcting stale doc claims about what is enforced, read the ENFORCEMENT implementation first and state its exact tier — reject, warn, or silent, and at which lifecycle point (deposit, claim, runtime). Overstatement and understatement are the same defect: each replaces one falsehood with another. Sweep the correcting plan's OWN prose for the banned claim shapes before deposit. Measured: a correction plan was itself about to carve three new false tiers ('hard-checks at deposit', 'ignores STOP prose entirely', 'warn-only' on a three-tier validator)."),

rule(84, 284, "Run the current implementation on every degenerate fixture before asserting its expected outcome",
"A test fixture that specifies a wrong expected outcome FORCES a literal developer to weaken the guard it is testing. For every degenerate or edge fixture, run the CURRENT implementation on the input first and assert its measured behaviour, carving out only the delta the change intends to alter. A fixture no correct implementation can satisfy is a defect in the PLAN, at the same severity as a defect in code. Measured: a fixture asserting exit 0 on an unparseable header, where the shipped check correctly exits 1."),

rule(85, 288, "Commit compounds start with cd-absolute and end with a toplevel assert",
"Every command compound touching a repo starts with `cd /abs/path` as its FIRST token — never trust cwd persistence between invocations, never lead with `cp`. Every commit compound ends by printing `git rev-parse --show-toplevel`, and a wrong or missing print is treated as NOT COMMITTED regardless of what `git log -1` shows: a relative-path compound can land the commit in whichever repo the cwd actually was, and the log check then reports the new hash — in the wrong repo. Measured: three culminations committed to the shop root this way in one session."),

rule(86, 289, "Never promise a verdict the grammar lacks",
"The Bellows verdict grammar is a closed set — `continue` and `stop`, nothing else. Read `verdict.py` before naming options at any gate; a plan that promises 'redo', 'retry', or any third verdict has authored an unreachable branch. A redo is expressed as: stop, then a corrected re-deposit under the stable slug whose A0 branch keys on the CONCRETE recorded half-state — greppable facts, never narrative. (The grammar itself is bellows-owned; this is the authoring half.)"),

rule(87, 293, "A severity or reversibility label is a CLAIM with a probe",
"Treat 'irreversible', 'load-bearing', 'blast radius', 'trivial' and their kin as claims requiring probes, not framing: each shapes risk posture, machinery, and step count, yet no factual-claim rule fires on an adjective. On a clone diff, re-derive the parent's risk adjectives exactly as its factual claims are re-derived. Measured: an inherited 'irreversible' survived 125 findings, three walks, three ACID passes and a five-seat panel, then dissolved in one query — the write touched 4 of 15 columns, none content, reversal a single statement."),

rule(88, 297, "Prefer derived expectations over constants in QA assertions",
"Before shipping any 'exactly N' assertion, confirm N is what a CORRECT run produces — including under re-entry (a legitimate resume adds a commit), concurrent actors, and later plan edits that change the count (a split leaves a stale deposit total). Prefer expectations DERIVED at run time from the plan's own declarations: read the Deposits blocks and count them; compute commit counts from the recorded re-entry state. A constant guard dies at exactly the moment it was supposed to work, and it dies by consent. Measured: three assertions in one plan would each have failed a correct execution."),

rule(89, 303, "A census over a corrected corpus states which half it measures",
"Final states of closed plans are post-fold by construction: matches there are dominated by prose DESCRIBING the defect class, not instances of committing it. Frequency measured on final states answers 'how often do plans discuss this?' and is misread as 'how often do plans commit this?'. Use final states to price the FALSE-POSITIVE surface and intermediate revisions to price TRUE positives — and never blend the two populations into one accuracy figure."),

rule(90, 305, "At every verdict gate, compare the steps table against commits and deposits",
"`pause_for_verdict` is a header contract the runtime does not police (FORWARD 46, bellows-owned): an agent can execute every step in one dispatch while the daemon records one row — and the 'independent' QA step then re-measures its own work minutes later. The authoring half: at EVERY verdict gate, before writing the verdict, compare the `steps` table's recorded progress against the observed commit and deposit counts; a one-step record over a multi-step evidence trail is the signature. Cheap, mechanical, and it restores the independence assumption every re-measure item silently rests on."),

rule(91, 306, "When an independence guard is missing, assess the bias direction before voiding the result",
"The bias an independence check guards against is an author confirming what they hoped. A result that DEMOLISHES the author's prior work is not that failure mode: a negative, self-marked finding backed by row-level re-checkable evidence is worth accepting with the gap recorded, rather than voided and re-run. Assess which direction the missing guard would have pushed before discarding work. Measured: a self-measured census that killed the author's own four drafted checks — zero true positives, 376 false — accepted on spot-checked raw evidence."),

rule(92, 307, "Confirm the known positives are inside a census's population before scanning",
"Precision over a population with no positives in it is unfalsifiable — any matcher scores zero, including a perfect one. Before running a census on a defect class, build the labelled positive set FIRST, from whatever artifact recorded the instances (often the walk register), and confirm those positives are inside the population being scanned. Report recall and precision as a PAIR; a disposition citing one without the other is incomplete. Measured: a census whose scan population excluded both cycles that generated its hypothesis returned an unfalsifiable zero."),

rule(93, 310, "Each mandate names its QA observer inline",
"Mandates live in the DEV step and observers live in the QA step, so every new mandate starts life unpaired — and a constraint with no check that can FAIL on its violation is prose, not a guard. Each mandate names its observing QA item inline at the point of imposition — '(observed by Item 8)' — so an unpaired mandate is visible at writing time rather than a walk later. Then verify the pairing by CONSTRUCTING the violation and confirming the named item reports it. (The lint mechanism detecting unpaired mandates is FORWARD 52, forge-owned; this is the authoring half.) Measured: the same unpaired-mandate class four times across three walks, each fix a lens late."),

rule(94, 314, "Author every task as ordered sub-items from the first draft",
"Every fold appends a sentence to the task it corrects; each sentence is right, and nothing ever removes one — past some length the block stops being an instruction and becomes a passage, and the agent executes part of it. Author every task as ORDERED SUB-ITEMS from the first draft, so a fold lands in a slot rather than at the end of a paragraph. After collapsing a wall of prose, put its region back on the next walk: a re-formed wall means the fix addressed the symptom while the accretion mechanism kept running. (The sentence-count lint mechanism is FORWARD 54, plan_lint-owned; this is the authoring half.) Measured across two cycles, including one wall that re-formed beneath the sub-steps its collapse had just created."),
])

BLOCK_ANCHOR = "*Source: proposal 220, lesson 2026-08-03*"
rep(BLOCK_ANCHOR, BLOCK_ANCHOR + "\n\n" + NEW_RULES.rstrip("\n"), 1, "E1-block-65-94")

rep("### 53. Region-scoped metrics must be computed with scope applied end to end",
"**Gate-behaviour sentences are inherited claims of exactly this class (proposal 226, codified " + D + "):** any sentence asserting what a gate matches, enforces, or rejects is a claim to RE-RUN against the gate's source before it shapes a disposition — inheriting it from a parent plan reproduces the parent's errors with the parent's confidence (measured: a banner-string claim about `gates.py` survived five warm walks, five ACID passes and a lint run because every pass read the assertion instead of running the gate). And a calibration range is a claim about a SAMPLE: record it with its sample size beside the threshold it justifies, so a n=6 range meeting a 16-item batch is visibly thin rather than silently authoritative.\n\n### 53. Region-scoped metrics must be computed with scope applied end to end",
1, "E2-rule52-ext")

rep("### 56. Resume machinery is justified only when the interrupted work is not reproducible",
"**An absence-result check requires a positive control on the same instrument in the same run (proposal 244, codified " + D + "):** when a check's PASSING result is an absence — a zero-difference diff, an empty grep, a no-rows query — that result is indistinguishable from a broken comparison: a bad query, a mismatched sort, a wrong file and an empty read all print the same nothing. Pair every absence-result check with a positive control run on the SAME instrument in the SAME run, demonstrating the instrument can detect a difference it is claimed to be sensitive to.\n\n### 56. Resume machinery is justified only when the interrupted work is not reproducible",
1, "E3-rule55-ext")

rep("### 57. Generalizing a guard: keep the mechanism generic, require the caller to pin the specifics",
"**Walk the RESUME path before the crash path (proposal 230, codified " + D + "):** for any new durability artifact, a write that is correct on a fresh run is a CLOBBER on a re-run unless it is explicitly non-destructive — a dispatcher that re-runs a dead step from the top will rewrite the before-image with post-mutation values, destroying exactly the state the artifact exists to preserve. The durable posture: if the artifact already exists, cite it as authoritative rather than rewriting it.\n\n**A backup and the write it inverts are adjacent (proposal 243, codified " + D + "):** nothing that can touch the same store may sit between them, and each backup states which SINGLE write it inverts. A backup separated from its write by other work spans a window in which another process may legitimately write the same store — correct at snapshot time, wrong at restore time. Adjacency also strengthens an unrelated guard: an unexplained backup becomes evidence of an attempted mutation rather than ignorable residue.\n\n### 57. Generalizing a guard: keep the mechanism generic, require the caller to pin the specifics",
1, "E4-rule56-ext")

rep("### 62. Establish that a recovered-from state is reachable before authoring recovery machinery",
"**Every pin ships its extraction command (proposal 240, codified " + D + "):** a pinned value whose extraction method is unstated fails closed on honest work — a verifier extracting any other way computes a different value and reports a mismatch on work that is entirely correct (measured twice in one artifact, plus a row-count baseline that varied by four depending on unstated counting rules). Ship the EXACT extraction command beside the pinned value, and confirm the method is portable across tool builds before pinning with it.\n\n### 62. Establish that a recovered-from state is reachable before authoring recovery machinery",
1, "E5-rule61-ext")

rep("### 63. Read the DELIVERY code before theorising about non-arrival",
"**A bypass branch enumerates every downstream reader of what it skips (proposal 269, codified " + D + "):** when adding a bypass or recovery branch, enumerate every downstream consumer of the bypassed block's outputs — each needs the branch to supply an equivalent, or the branch is correct about the PAST and silent about the FUTURE (measured: a recovery branch skipped the commit block where DOC_SHA gets pinned, and the QA step consumed DOC_SHA unconditionally — the exact death-state the branch was built for would have reached QA missing the value QA halts without). Test the recovery path's artifacts against the CONSUMER'S checks, not the happy path's.\n\n### 63. Read the DELIVERY code before theorising about non-arrival",
1, "E6-rule62-ext")

rep("Source: proposal 149, lesson 2026-07-16",
"**Every number a plan states is produced by the plan's own mandated method (proposal 250, codified " + D + "):** a number obtained any other way is a prediction wearing a measurement's clothes and carries the same verify-clause obligation — measured: a count taken without the mandated strip method overstated by half, and the wrong count was taken by a fresh cold reader who had JUST read the strip rule. The corollary: a discipline reapplied at many call sites belongs INSIDE the instrument (the script, the query, the one-liner), not left for each caller to remember.\n\nSource: proposal 149, lesson 2026-07-16",
1, "E7-checklist29-ext")

rep("**Version:** 4.85", "**Version:** 4.86", 1, "E8-version")
rep("**Last Updated:** 2026-08-08 (v4.85)", "**Last Updated:** 2026-08-11 (v4.86)", 1, "E9-lastupdated")

CHANGELOG_ROW = ("| 2026-08-11 | v4.86: Gate 2 batch 2 (gate2-template-batch-2026-08-11) — 37 proposals codified, the largest corpus batch to date "
"(21 routed by the 2026-08-09 gate via plan 326, 16 by the 2026-08-11 gate via plan 342; all 37 flipped accepted-to-implemented by this plan). "
"Thirty NEW rules 65-94, appended in proposal-id order as one contiguous block (223, 225, 228, 229, 236, 239, 242, 255, 257, 264, 265, 266, 267, 268, "
"274, 277, 280, 281, 282, 284, 288, 289, 293, 297, 303, 305, 306, 307, 310, 314). Seven EXTENSIONS: Rule 52 gains gate-behaviour-claims-are-re-run-claims "
"plus calibration-with-sample-size (226); Rule 55 gains the absence-result positive-control requirement (244); Rule 56 gains resume-path-before-crash-path (230) "
"and backup-write adjacency (243); Rule 61 gains ship-the-extraction-command (240); Rule 62 gains the bypass-branch downstream-reader enumeration (269); "
"Checklist #29 gains numbers-by-mandated-method-only plus disciplines-inside-the-instrument (250). Rule-46 splits recorded where proposals carried them: the "
"bellows-owned halves of 274 (verdict channel), 289 (verdict grammar), 305 (pause_for_verdict enforcement, FORWARD 46) and the forge/lint-owned mechanisms of "
"310 (FORWARD 52) and 314 (FORWARD 54) are NOT codified here — each rule's text names its split. Numbering append-only per the 4.83 precedent (63/64). |")
rep("| Date | Lesson |\n|---|---|\n", "| Date | Lesson |\n|---|---|\n" + CHANGELOG_ROW + "\n", 1, "E10-changelog")

io.open(DST, 'w', encoding='utf-8').write(s)
print(f"OK — {len(edits_applied)} edits applied: {', '.join(edits_applied)}")
```
