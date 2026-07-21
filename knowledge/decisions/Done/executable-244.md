# Lessons Forge — Gate 1 Route Disposition (cycle 2026-07-20)
**Date:** 2026-07-20 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

## CEO Context

Gate 1 for the 5 proposals from cycle 2026-07-20 (plan 243). **CEO dispositions are final and embedded below: 5 codify, 0 reference, 0 backlog.**

**Disposition table (authoritative for both steps):**

| Proposal | Entry | Category | Route |
|---|---|---|---|
| 155 | 147 | governance_rule | **codify** |
| 156 | 148 | governance_rule | **codify** |
| 157 | 149 | governance_rule | **codify** |
| 158 | 150 | governance_rule | **codify** |
| 159 | 151 | governance_rule | **codify** |

**All five routed `codify` — dedup against the LIVE template (2026-06-07 discipline) done at Gate 1 authoring; none is already codified:**
- **155** (verdict-added requirements need a structural home — numbered row / named test / gate; location before numbering): not present in the template.
- **156** (grep presence ≠ effect; verify a wired call by an observed behaviour change through the real entry point): the template has only the NARROWER daemon-write-path live-canary rule (`PLANNER_TEMPLATE.md:1539`). **CEO decision 2026-07-20: codify the GENERAL rule; the line-1539 canary becomes its worked example.** Not a duplicate.
- **157** (ACID as a fifth Drafting Cycle lens): not present — the only "ACID" in the template is unrelated (atomic plan deposits, :1388).
- **158** (diagnostic-shaped escalation triggers for the Drafting Cycle): not present — the triggers are executable-only.
- **159** (Drafting Cycle stop condition): the template has "diminishing returns" (:337); this proposal supersedes it. See the Gate-2 note below.

**⚠️ Note for Gate 2 (NOT this plan's job — routing only here). Proposal 159 must NOT be codified verbatim.** Entry 151 states a WITHIN-lens iterate-to-dry model; the CEO's 2026-07-20 walk-the-list correction overrides it (one pass per lens; walk the whole list; re-run only on a subsequent walk; done when a full walk returns minor-only). The deciding EVIDENCE for the corrected form is staged at `LESSONS-candidates-from-drafting-cycle-2026-07-20.md` (candidate C1: three cases this cycle where a fold's defect was caught only by a different lens on a subsequent walk, which within-lens iterate-to-dry structurally cannot catch). **Gate 2 codifies the C1 form, and C1 should be in front of Gate 2.** 157/158/159 share the `## The Drafting Cycle` section and interact — codify them coherently at Gate 2.

**Gate 1 changes ROUTES ONLY.** Proposal `status` values are NOT changed here — status transitions to `implemented` happen at Gate 2 (plan-133/206 precedent). All five proposals stay `proposed`.

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-gate-1-2026-07-20.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer. Read `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` first (cross-repo; skip with a note if absent). All commands run from your own working tree. **All canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute or skip a verification. **⚠️ The `FORGE_LESSONS_AGENT.md` specialist file has stale `forge/`/`forge.db` paths — the corpus is `lessons-forge/lessons-forge.db`; `forge/forge.db` is a DIFFERENT database, never open it.**
>
> **This step changes the canonical DB only. It MUST NOT touch `src/`** — no code changes.
>
> **Open canonical read-WRITE** (`sqlite3.connect(<abs path>)`; default is read-write; do NOT reuse a `?mode=ro` handle for the writes). Use `set_proposal_route(conn, proposal_id, route)` from `src.lessons_forge` — **not hand-written SQL** — and `conn.commit()` after (the function does not commit internally; the DB is gitignored so this is a SQLite commit, not a git commit).
>
> **Scope:**
> - `knowledge/development/gate-1-route-disposition-2026-07-20.md`
>
> **Task A0 — ISOLATION pre-flight (conflict-serializability), THEN the precondition.** This plan's check is a `R(before) → W(routes) → R(after)` schedule whose before/after comparison is only meaningful if NO other transaction writes `lesson_proposals` in between — the reads are not held in one locked transaction, so a concurrent writer makes the schedule non-serializable (an unrepeatable read → a false status-identity halt; in the contrived case of a concurrent write to one of 155–159, a silently-lost update). The daemon's one-plan-at-a-time model normally provides this isolation; **assert it explicitly before capturing snapshots.** The PRIMARY guard is that no other lessons-forge cycle/gate plan is in flight: `ls knowledge/decisions/` shows no `in-progress-*` or `verdict-pending-*` lessons plan other than this one. **Do NOT use `get_unclassified_entries()` as the quiescence signal — it filters on proposal `status`, never `route`, so a concurrent ROUTE write (the exact conflict here) is invisible to it.** If you want a stability re-read, read the dimension actually at risk — the route-NOT-NULL count (or the `id,route` of 155–159) — twice a moment apart and confirm it is unchanged. If a concurrent writer is possible, **HALT** — do not capture a before-snapshot that another transaction may invalidate mid-plan. (A status-identity failure that DOES occur is then a genuine signal, not a concurrency artifact.)
>
> **Task A0 — PRECONDITION: verify the targets are what the disposition table assumes, BEFORE writing.** The five IDs are hardcoded; confirm they still map to the intended state before mutating anything. Read `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 155 AND 159` and assert **all five hold**: `status='proposed'`, the id→entry_id mapping is exactly 155→147, 156→148, 157→149, 158→150, 159→151 (the cycle-243 batch), and each `route` is **either `NULL` (fresh) or already `codify` (an idempotent re-run of THIS plan — tolerated, not a failure)**. **HALT only on a genuine drift:** a missing id, a non-`proposed` status, a wrong entry_id, or a route already set to `backlog`/`reference` (a route this plan never assigns → the DB drifted). This tolerance is what makes A0 consistent with the resume-safe blast-radius check in Task C — a partial prior run that already set some targets to `codify` must be resumable, not halted.
>
> **Task A0 also CAPTURES the "before" snapshots — pre-write, here, is the only correct time.** While pre-write, record and keep: (1) the full status distribution, and (2) the route-NOT-NULL count. Tasks B and C compare against THESE captured snapshots — do NOT re-read "before" after Task A's write, which would make before == after and silently defeat both checks (the cycle plan's "capture the baseline before the write; after is worthless" lesson).
>
> **Task A — record the routes.** Apply exactly the CEO disposition table, all five to `codify`:
> - `155` → `codify`
> - `156` → `codify`
> - `157` → `codify`
> - `158` → `codify`
> - `159` → `codify`
>
> **Task B — verify, and prove you changed nothing but the five routes.** Compare the **A0 before-snapshot** of the status distribution against the distribution read now (after) and assert they are **byte-identical** — Gate 1 assigns routes only; if any `status` changed, halt and report. Then read back `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 155 AND 159` and confirm: all five routes are `codify`, and all five are still `status='proposed'`. (Trap: `route='codify'` and `status='proposed'` are DIFFERENT columns — a `status` change is a bug, the route change is the intent.)
> **Why a FULL status-distribution check here but only a per-target read-back for routes (consistency with Task C):** `set_proposal_route` cannot change any status, so like an un-named route, a status change is unreachable via this plan's own operations. The full status-distribution comparison is retained deliberately as **206's broad tripwire** — it catches a status change caused by something OUTSIDE this plan (a concurrent writer, a stray call), which the per-target read-back cannot. 206 kept this tripwire for status and did NOT add a route-map equivalent; this plan follows that proven asymmetry rather than either dropping the status tripwire or re-adding a route map-diff.
>
> **Task C — confirm the blast radius (206's proven tripwire; no heavier).** `set_proposal_route` touches ONLY the id it is given, and this plan gives only 155–159 — so pre-existing routes (149–154 from plan 228, etc.) are structurally untouchable, and the reachable failures are exactly "wrong id" and "missing write." Both are caught by: (1) the Task B read-back showing all five of {155–159} = `route='codify'`, and (2) the route-NOT-NULL count rising by **at most 5** over the A0 before-count (exactly 5 on a clean run; fewer only if a target was pre-`codify` on a resume — not a failure). Measure and report both actual counts; do NOT hardcode them (`before` is non-zero — prior Gate 1s assigned routes). **A full pre-existing-route map-diff is deliberately NOT required** — it would guard only a rogue call the plan never issues (`set_proposal_route` on an un-named id), which is out of proportion for a routes-only plan and heavier than 206's proven tripwire (integration-vs-record decision, cycle 2026-07-20 walk-2).
>
> **Deposit:** `knowledge/development/gate-1-route-disposition-2026-07-20.md` — the `set_proposal_route` calls made, the A0 pre-write before-snapshots (status distribution + route-NOT-NULL count) and the matching after-values **proving status is identical and the count rose by ≤5**, the read-back of all five rows (`SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 155 AND 159`) as RAW output (not a summarized claim — proposal 156 / qa-evidence-raw-output discipline), and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit the dev-log deposit. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-1-route-disposition-2026-07-20.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — QA

---

> **Before starting, read the Step 1 deposit and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2 (QA).
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` for domain context (skip with a note if absent; ⚠️ its `forge/`/`forge.db` paths are stale — the corpus is `lessons-forge/lessons-forge.db`). All commands run from your own working tree. **Verification + reporting only — no product-code changes.** If a test fails, report it — do NOT fix it. If you find a blocker, STOP and report. Do NOT use Monitor.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule.** Every SQL row states which DB it ran against. Canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. Worktree DB absence is never a substitution reason. Deposit **RAW command output**, never a summary.
>
> **Scope:**
> - `knowledge/qa/gate-1-route-disposition-qa-2026-07-20.md`
>
> **Precondition for rows 2 and 3:** both diff against the A0 pre-write before-values (status distribution for row 2, route-NOT-NULL count for row 3) that Step 1 deposited. If Step 1's deposit does not contain those before-values, rows 2 and 3 are **unverifiable — HALT and report** (a "Complete" Output Receipt is not proof the snapshot is present; check the raw deposit).
>
> Verification table, one row per claim, each with a DB-source column:
> 1. **Routes recorded exactly per the CEO table** — 155–159 all `codify`. Raw `SELECT id, entry_id, status, route FROM lesson_proposals WHERE id BETWEEN 155 AND 159` output.
> 2. **Gate 1 changed no status** — the check is an IDENTITY, not a match-to-number. Diff the status distribution Step 1 captured pre-write (A0 before-snapshot) against the distribution on canonical now; assert they are **identical**, and that all five of {155–159} are still `proposed`. Quote both raw distributions. **Do NOT hardcode or match against absolute totals** — a bare predicted distribution is the checklist-#29 anti-pattern and is unnecessary here: before == after is the whole requirement, whatever the corpus totals happen to be. **Trap:** a `status='codify'` anywhere is a FAIL — `codify` is a ROUTE value, not a status; the status→`implemented` transition is Gate 2's, not Gate 1's.
> 3. **Blast radius — re-derive from raw, don't trust the claim.** Read canonical yourself: assert all five of {155–159} carry `route='codify'` (raw `SELECT`), and the route-NOT-NULL count rose by ≤5 over the A0 before-count Step 1 deposited (exactly 5 clean; fewer only on a resume). Report both actual counts. (A full pre-existing-route map-diff is intentionally not required — `set_proposal_route` cannot touch an un-named id, so 155–159=codify + the count delta fully characterize the reachable change; see the Step 1 Task C rationale.)
> 4. **The 204 fix still holds (standing regression watch)** — `get_unclassified_entries()` still `[]`; no proposal moved off a terminal status; and the `stale` count is unchanged. **Do NOT hardcode the stale number** (checklist #29) — its constancy is already proven by row 2's status-distribution identity (`stale` is one of the distribution's buckets), so verify it there, don't assert an absolute count.
> 5. **Template untouched** — this plan makes NO edit to `PLANNER_TEMPLATE.md` (Gate 2's job). `git -C /Users/marklehn/Developer/GitHub diff --exit-code -- PLANNER_TEMPLATE.md` returns exit 0. (Use `git -C <root>` — the template is tracked by the root repo, NOT this submodule; a bare `git diff` from the worktree passes vacuously because the file is absent there.)
> 6. **Targeted tests green — and the selector is NOT vacuous.** `python3 -m pytest src/ -k "route or proposal" -v` (`python3 -m pytest`, NOT the `timeout` binary — unavailable on macOS). **Assert the selector collected a NON-ZERO count** (report it; ~15 today) — a `-k` that matches nothing reports "no tests ran" as green, a vacuous pass. Full suite is not required for a routes-only DB-disposition plan; compute the collected count from `--collect-only` rather than carrying a number.
>
> If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/gate-1-route-disposition-qa-2026-07-20.md` — verification table with DB-source column, raw output, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (Gate 1 2026-07-20 complete: 5 proposals dispositioned all `codify`; statuses unchanged; Gate 2 codification pending — the three Drafting-Cycle amendments 157/158/159 to be codified coherently, 159 in its C1/walk-the-list form not verbatim); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate-1-route-disposition-qa-2026-07-20.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
