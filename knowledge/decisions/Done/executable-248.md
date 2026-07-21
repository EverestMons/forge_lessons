# Lessons Forge — Gate 1 Route Disposition (cycle 2026-07-21)
**Date:** 2026-07-21 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

## CEO Context

Gate 1 for the 12 proposals from cycle 2026-07-21 (plan 247). **CEO dispositions are final and embedded below: 9 codify, 1 reference, 2 backlog.**

**Disposition table (authoritative for both steps):**

| Proposal | Entry | Topic | Route | Status after |
|---|---|---|---|---|
| 160 | 152 | conflict-serializability lens | **codify** | `proposed` (unchanged) |
| 161 | 153 | plan-shape lens skip-rules | **backlog** | **`reference`** |
| 162 | 154 | fix-sweep-siblings | **codify** | `proposed` (unchanged) |
| 163 | 155 | the lens set is OPEN | **codify** | `proposed` (unchanged) |
| 164 | 156 | walk-the-list | **reference** | **`reference`** |
| 165 | 157 | vacuous `git -C` | **codify** | `proposed` (unchanged) |
| 166 | 158 | parallelism within-not-across | **codify** | `proposed` (unchanged) |
| 167 | 159 | guards observe the live tree | **codify** | `proposed` (unchanged) |
| 168 | 160 | resume vs restore-and-redo | **codify** | `proposed` (unchanged) |
| 169 | 161 | manual-era `Done/` boilerplate | **backlog** | **`reference`** |
| 170 | 162 | novel lens ships broken mechanism | **codify** | `proposed` (unchanged) |
| 171 | 163 | context saturation / rotate the reviewer | **codify** | `proposed` (unchanged) |

**⚠️ THIS GATE 1 WRITES STATUS AS WELL AS ROUTE — the prior Gate 1 (244) did NOT.** Do not carry 244's "status distribution must be byte-identical before/after" invariant into this plan; here it is **a predicted delta**, not identity. Exactly three proposals change status (`161`, `164`, `169` → `reference`); the other nine keep `proposed` because they are Gate-2-bound. See Task B for the exact expected distribution.

**Dedup against the LIVE template (v4.76) was done at Gate 1 authoring — the 2026-06-07 discipline. Findings, each grep-verified:**
- **164 is ALREADY CODIFIED.** "Walk the lens list" shipped into `PLANNER_TEMPLATE.md:341` at v4.76 (`0a6932d`), where it was cited as the evidence for proposal 159. Route `reference` — the corpus keeps the record, the template already has the rule.
- **169's substance is ALREADY CODIFIED, in Rule 8** — which states it emphatically and repeatedly ("The agent does NOT move the plan to Done"; "**STOP.** Do NOT move this plan to Done/ … never by the agent"). **The gap is ENFORCEMENT, not doctrine:** plan 247 carried the violating boilerplate anyway, while the rule was in force. CEO routes **backlog** for the `plan_lint` check entry 161 itself proposes (a Dispatch-Mode-aware lint), not a restatement of Rule 8.
- **162 overlaps Rule 26**, which covers the NARROWER convention-change case (renaming a field, reformatting a header) and already names "places that quote it — embedded copies, examples, documentation, test fixtures." CEO routes **codify as the GENERALIZATION** (any fix of an anti-pattern instance, not only convention changes); **Rule 26 becomes its worked example.** Precedent: proposal 156 at the prior Gate 1 was routed exactly this way against the narrower line-1539 canary rule.
- **161 conflicts with a rule codified ONE SESSION AGO.** Its skip-rules would permit not walking the full lens list, while `:341` says "Walk the full lens list in order — one pass per lens per walk." **CEO routes `backlog`** — defer until more evidence. The cost asymmetry is the reason: walking a dry lens costs one pass; skipping a lens that was not dry ships a defect. (Live datapoint: plan 247's drafting walked destruction on a reversible-write plan, honestly reported it dry, and lost nothing.)
- **The remaining eight (160, 163, 165, 166, 167, 168, 170, 171) are NOT in the template** — each verified by grep at authoring time: `conflict-serializ` 0; `lens set`/`novel lens`/`new lens`/`provisional`/`standing lens` 0; `git -C` 0 and `positive signal` 0; `main-tree`/`main tree` 0; `restore-and-redo`/`resume machinery`/`reproducible` 0; `rotate`/`cold`/`fresh-context`/`saturat` 0. **Three single-hit near-misses were checked and are FALSE ALARMS:** the one `cross-lens` hit (`:341`) is about cross-lens *contradictions*, not cross-lens *parallelism*; the one `vacuous` hit (`:1911`) is a changelog row; there is no `git -C` occurrence at all.

**⚠️ Notes for Gate 2 (NOT this plan's job — routing only here).**
- **160 must not be codified without a FORM decision.** The open question is whether conflict-serializability becomes a **sixth named lens** or the existing ACID lens's Isolation clause **widens** to cover multi-step schedules. The entry itself names both options without resolving. Evidence for that call is in the session-3 baton block; ADR-004's D6 constrains how `## The Drafting Cycle` may be decomposed — read it before Gate 2.
- **163 and 170 are a PAIR** (the lens set is open; a novel lens's fold is provisional and needs a standing-lens sweep behind it). **165 and 167 are a PAIR** (assert a positive signal; run git against the repo/tree that actually holds the state). Codify each pair coherently rather than as scattered edits.
- **162 codifies as a generalization of Rule 26** — amend or cross-reference Rule 26 rather than adding a rule that silently competes with it.

**Scope discipline: routes and the three named statuses ONLY.** Do NOT edit `PLANNER_TEMPLATE.md` — codification is Gate 2 and is the one thing the record explicitly forbids outside the governed route. Do NOT touch `src/` — this plan changes no code. Do not pre-draft template wording in any deposit.

**Deposit-once discipline:** deposited exactly once.

**Authoring self-check (for the verdict gate).** `bellows/scripts/plan_lint.py` was run against this plan at authoring time: **exit 0, all checks PASS, ZERO warnings** (header parsed, dispatch_mode bellows, pause_for_verdict always, both steps' Deposits and Scope resolved, QA banner pair present). Note this plan emits none of the `scope_check`-on-tests WARNs the cycle plan carried — nothing here needs silencing, and no test file belongs in any step's scope (Step 1 is a DB write, Step 2 is verification-only).

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-gate-1-route-disposition-2026-07-21.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer. Read `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` first (cross-repo; skip with a note if absent). All commands run from **your own working tree**. **All canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute or skip a verification. `forge/forge.db` is a REAL but DIFFERENT database — never open it. (The `FORGE_LESSONS_AGENT.md` specialist paths were corrected at `7ce4218` and are now right, but they are written relative to the GitHub ROOT — from your worktree they resolve to nothing. Use the absolute path above.)
>
> **This step changes the canonical DB only. It MUST NOT touch `src/`** — no code changes.
>
> **Open canonical read-WRITE** (`sqlite3.connect(<abs path>)`; default is read-write; do NOT reuse a `?mode=ro` handle for the writes). **⚠️ Task A and Task A2 are ONE transaction: issue a SINGLE `conn.commit()` after BOTH have run, never one commit per task.** A route written without its paired status change is precisely the state QA row 3 calls a FAIL (the durability argument rests on both columns moving together); committing between them makes that broken state durable if the step dies in the gap. One commit means the disposition lands whole or not at all. The helper does not commit internally, and the DB is gitignored so this is a SQLite commit, not a git commit.
>
> **Scope:**
> - `knowledge/development/gate-1-route-disposition-2026-07-21.md`
>
> **Task A00 — TAKE A RESTORE POINT BEFORE ANY WRITE. Do this first, before the isolation pre-flight.**
> Unlike the prior Gate 1 (plan 244), this plan issues a **hand-written SQL `UPDATE`** against the canonical corpus (Task A2). `set_proposal_route` is structurally incapable of damaging a row it was not given; a raw `UPDATE` is not — a missing `WHERE` clause would rewrite the `status` column of all 171 proposals, and there is no code path in this plan that could undo it. Every precedented corpus/DB write in this shop took a restore point (the sentinel repair, the floor-only migration, cycle 247); this one is not the exception.
> **Use SQLite's own `.backup`, not `cp`** — the canonical DB carries a live WAL, so a filesystem copy of the `.db` alone can miss un-checkpointed pages and produce a subtly stale restore point.
> **Write it to the MAIN tree by ABSOLUTE path** — a worktree-local backup is destroyed by teardown, which is exactly when you would need it:
> `mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups && sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-<UTC timestamp>.db'"` (colon-free stamp).
> `.gitignore` matches `*.db`, so it will not be committed — confirm with `git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain` showing the backup absent. **State the absolute backup path in your dev log.**
> **⚠️ If the backup fails for ANY reason — non-zero exit, missing file, or zero bytes — HALT and write nothing.** Verify it exists and is non-empty before proceeding (`ls -la` the path and confirm size > 0). A plan that takes a restore point but continues when the restore point failed has the ceremony without the protection, which is worse than not taking one, because the rest of the plan then relies on a safety net that is not there.
>
> **Task A0 — ISOLATION pre-flight, from the tree where the state actually lives.**
> This plan's check is a `R(before) → W(routes+statuses) → R(after)` schedule whose before/after comparison is only meaningful if NO other transaction writes `lesson_proposals` in between. Assert that explicitly before capturing snapshots.
> **⚠️ Read the lifecycle state by ABSOLUTE MAIN-TREE path — a worktree-relative `ls` passes VACUOUSLY.** Run `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/` and confirm no `in-progress-*` or `verdict-pending-*` lessons plan other than THIS one. Bellows lifecycle renames are uncommitted filesystem operations in the MAIN tree, so a worktree checkout cannot see them **at all — not stale, absent**, and a relative `ls` reporting "none found" is an absence artifact, not a verification. **Assert the POSITIVE signal: your own plan file MUST appear in that listing** (as `in-progress-*` or `verdict-pending-*`). If it does not, you are reading the wrong tree — HALT. (This is not hypothetical: plan 244's A0 ran this check worktree-relative and reported "no in-progress-* found" while its own in-progress file sat in the main tree. Proposal 167, which THIS plan is routing, is that exact lesson.)
> **Do NOT use `get_unclassified_entries()` as the quiescence signal** — it filters on proposal `status`, never `route`, so a concurrent ROUTE write (the exact conflict here) is invisible to it. For a stability re-read, read the dimensions actually at risk — the route-NOT-NULL count and the status distribution — twice a moment apart and confirm both unchanged. If a concurrent writer is possible, **HALT**.
>
> **Task A0 — PRECONDITION: verify the targets match the disposition table BEFORE writing.** Read `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 160 AND 171` and assert all twelve hold:
> - the id→entry_id mapping is exactly `160→152, 161→153, 162→154, 163→155, 164→156, 165→157, 166→158, 167→159, 168→160, 169→161, 170→162, 171→163` (the cycle-247 batch, contiguous);
> - each `status` is `proposed`, **or** already the target `reference` for 161/164/169 (an idempotent re-run of THIS plan — tolerated, not a failure);
> - each `route` is **NULL (fresh) or already this plan's target route** (`codify`/`reference`/`backlog` per the table — an idempotent re-run).
>
> **HALT only on genuine drift:** a missing id, a wrong entry_id, a status outside {`proposed`, the target}, or a route set to something this plan never assigns for that id. This tolerance is what makes A0 consistent with the resume-safe blast-radius check in Task C — a partial prior run must be resumable, not halted.
>
> **Task A0 also CAPTURES the "before" snapshots — pre-write is the only correct time.** Record and KEEP: (1) the full status distribution, and (2) the route-NOT-NULL count. Tasks B and C compare against THESE captured values — do NOT re-read "before" after Task A's write, which would make before == after and silently defeat both checks.
> **Authoring-time expectation, to be confirmed not assumed:** status distribution `implemented 110, superseded 28, rejected 15, proposed 12, reference 3, stale 3` (total 171); route-NOT-NULL count **29**. Report the ACTUAL values; a mismatch is a finding, not a number to adjust to.
>
> **Task A — record the twelve routes.** Use `set_proposal_route(conn, proposal_id, route)` from `src.lessons_forge` — **not hand-written SQL** — applying exactly the CEO disposition table:
> - `codify`: **160, 162, 163, 165, 166, 167, 168, 170, 171** (nine)
> - `reference`: **164** (one)
> - `backlog`: **161, 169** (two)
>
> **Task A2 — record the three status changes. This one REQUIRES hand-written SQL, deliberately.** There is no status-setting helper in `src/lessons_forge.py` (verified at authoring: the module exposes `set_proposal_route` and no status setter), so Task A's "not hand-written SQL" rule does NOT extend here — using SQL for status is correct, not a violation. For **161, 164, and 169 ONLY**, set `status='reference'`, `status_updated_by='ceo'`, and `status_updated_at` to the current UTC timestamp, matching the existing convention on the three pre-existing reference rows (ids 140/141/146, which carry `status_updated_by='ceo'`). Use a parameterised `UPDATE ... WHERE id IN (?,?,?)`; **never a bare `UPDATE lesson_proposals SET status=...` without a WHERE clause.** State the exact SQL you ran in your dev log.
>
> **Why these three are terminal:** `reference` is in `_TERMINAL_STATUSES`, so a future ingest whose entry-hash changes cannot silently stale a CEO disposition. Leaving a backlog item at `proposed` would leave it destructible AND would trip every future cycle's G1 non-terminal precondition. The `route` column carries the backlog semantics; the status carries the durability. This is the CEO's explicit 2026-07-21 decision and the first `backlog` routing in this corpus's history — there is no prior pattern to copy.
>
> **Task B — verify the ABSOLUTE post-state, then the delta as a fresh-run cross-check.**
> ⚠️ **Unlike Gate 1 of the prior cycle (plan 244), the status distribution is NOT expected to be identical** — this plan moves three proposals. But do NOT express the check only as a delta from your A0 snapshot: **on a resume, A0 captures the ALREADY-WRITTEN state**, so before == after and a delta assertion would fail against a perfectly correct database.
>
> **B1 — the primary assertion is the ABSOLUTE target distribution, which holds on a fresh run AND a resume.** Read the distribution now and assert exactly:
> `proposed 9`, `reference 6`, `implemented 110`, `superseded 28`, `rejected 15`, `stale 3` — **total 171**.
> Any other value → **HALT**. (These absolutes are derived from the authoring-time corpus; if the A0 pre-write snapshot did NOT match the authoring-time expectation, say so and halt rather than assuming these targets still apply.)
>
> **B2 — the delta is a FRESH-RUN cross-check only.** If A0 showed `proposed 12 / reference 3` (a fresh run), additionally confirm the movement was `proposed −3` and `reference +3` with `implemented`/`superseded`/`rejected`/`stale` untouched and no rows created or destroyed. **If A0 already showed `proposed 9 / reference 6`, this is a resume: record `B2: N/A (resume — writes already applied)` and let B1 carry the verification.** Do not manufacture a delta that a resume cannot produce. Then read back `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 160 AND 171 ORDER BY id` and confirm every row matches the disposition table on BOTH columns. (Trap: `route` and `status` are DIFFERENT columns — nine rows must show `route='codify'` with `status='proposed'` STILL, and exactly three must show `status='reference'`.)
>
> **Task C — confirm the blast radius.** `set_proposal_route` touches only the id it is given, and the Task A2 UPDATE is `WHERE id IN (161,164,169)`, so pre-existing rows are structurally untouchable; the reachable failures are "wrong id", "missing write", and "unscoped UPDATE". All three are caught by: (1) the Task B read-back of all twelve; (2) the route-NOT-NULL count rising by **at most 12** over the A0 before-count (exactly 12 on a clean run; fewer only if a target was pre-routed on a resume — not a failure); and (3) the count of rows with `status='reference'` rising by **at most 3**. Measure and report all actual counts; do NOT hardcode them.
>
> **Deposit:** `knowledge/development/gate-1-route-disposition-2026-07-21.md` — the `set_proposal_route` calls made, the exact Task A2 SQL, the A0 pre-write before-snapshots and the matching after-values proving the predicted delta, and the read-back of all twelve rows as **RAW command output, not a summarized claim** (the qa-evidence-raw-output discipline), plus an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit the dev-log deposit. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-1-route-disposition-2026-07-21.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — QA

---

> **Before starting, read the Step 1 deposit and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2 (QA).
>
> You are Lessons Forge QA. **Working location:** run commands from your own working tree; canonical DB by ABSOLUTE path is the only exception. **Verification + reporting only — no product-code changes and no DB writes.** If a check fails, **report it — do NOT fix it**. Do NOT use Monitor. Do NOT edit PROJECT_STATUS directly; route it via the receipt.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule.** Every SQL row states which DB it ran against. Canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. Deposit **RAW command output, never a summary of it.**
>
> **Scope:**
> - `knowledge/qa/gate-1-route-disposition-qa-2026-07-21.md`
>
> Verification table, one row per claim, each with a DB-source column:
> 1. **All twelve dispositions applied.** `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 160 AND 171 ORDER BY id` — raw output shown. Assert against the plan's disposition table: `codify` on 160/162/163/165/166/167/168/170/171, `reference` on 164, `backlog` on 161/169. Any mismatch is a **FAIL**.
> 2. **The nine codify proposals are STILL `status='proposed'`** (Gate-2-bound — Gate 1 must not implement them). Any of the nine at a non-`proposed` status is a **FAIL**.
> 3. **The three terminal statuses landed.** 161, 164, 169 each show `status='reference'` AND `status_updated_by='ceo'` AND a non-NULL `status_updated_at`. A route set without the status change (or vice versa) is a **FAIL** — the durability argument depends on both.
> 4. **Status distribution is exactly the target.** The PRIMARY assertion is the absolute post-state, which is resume-invariant: `proposed 9`, `reference 6`, `implemented 110`, `superseded 28`, `rejected 15`, `stale 3`, total **171**. Any other value is a **FAIL**. Then read the A0 before-snapshot from the Step 1 deposit and reconcile: if it shows `proposed 12 / reference 3` the run was fresh and the movement must be −3/+3; if it shows `proposed 9 / reference 6` Step 1 was a resume and B2 is legitimately `N/A` — **that is not a failure, and a Step-1 deposit reporting a resume must not be marked FAIL for a missing delta.** If the before-snapshot is missing entirely, **halt** — the reconciliation is unverifiable without it.
> 5. **Blast radius.** Total proposals still 171 (no rows created/destroyed); route-NOT-NULL count rose by ≤12 from the Step-1 before-count; `status='reference'` count rose by ≤3. Report actuals.
> 6. **No proposal outside 160-171 changed.** Run `SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL AND id < 160` and assert it equals the Step-1 A0 before-snapshot's route-NOT-NULL **total** (29 at authoring). That equality is exact, not approximate: before this plan ran, NO proposal with id >= 160 carried a route, so the before-total counts only ids < 160. Also assert `SELECT COUNT(*) FROM lesson_proposals WHERE status='reference' AND id < 160` equals **3** (the pre-existing 140/141/146). Either differing means an unscoped write — a **FAIL**.
> 7. **`PLANNER_TEMPLATE.md` is UNCHANGED by this gate.** ⚠️ `lessons-forge` is a **submodule**; the template is tracked by the **root** repo and does **not exist** in your worktree — a plain `git diff -- PLANNER_TEMPLATE.md` from where you are finds nothing and passes VACUOUSLY. **This is proposal 165, which this very plan is routing.** Run `git -C /Users/marklehn/Developer/GitHub diff --exit-code -- PLANNER_TEMPLATE.md` and **show the exit code**. Exit 0 is the pass; any diff is a **FAIL**. Codification is Gate 2.
> 8. **`src/` untouched and suite green.** `git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain -- src/` is empty, and `python3 -m pytest src/ -q` passes. **Compute the baseline from `--collect-only` and reconcile against the most recent prior QA report in `knowledge/qa/`; do NOT carry a number forward from this plan's text.** (For reconciliation only: the 2026-07-21 cycle QA recorded 55.) Raw tail shown.
> 9. **`get_unclassified_entries(conn)` still returns `[]`.** Gate 1 assigns routes and three statuses; it must not orphan an entry. ⚠️ Note the interaction: `reference` is a non-stale status, so the three re-statused proposals keep their entries classified — a non-empty result here would mean something else changed. Any non-empty result is a **FAIL**.
>
> If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/gate-1-route-disposition-qa-2026-07-21.md` — verification table with DB-source column, raw query output, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (Gate 1 complete for cycle 2026-07-21: 9 codify / 1 reference / 2 backlog; the nine codify proposals are Gate-2-bound and remain `proposed`; 161/164/169 are terminal at `reference`; Gate 2 owes the conflict-serializability FORM decision); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate-1-route-disposition-qa-2026-07-21.md`
>
> **Do NOT move this plan to `Done/`.** The close path is owned by Bellows on continue-verdict consumption (Rule 8; `bellows.py` final-step branch) — never by the agent. An agent-side move is a Mode-A `unauthorized_done_move` violation that force-recovers the file and flips this step's gates to FAILED. This plan states the rule positively because the corpus it is routing contains the lesson that the manual-era `Done/`-move boilerplate survives in plan text precisely by going unstated (proposal 169, routed `backlog` by this very plan).
