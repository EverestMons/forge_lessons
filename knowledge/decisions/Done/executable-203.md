# Lessons Forge — Cycle Run 2026-07-16 (ingest the 2026-07-07 backlog; first live dedup-advisory exercise)
**Date:** 2026-07-16 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (DEV) → Step 2 (Lessons Agent) → Step 3 (DEV) → Step 4 (QA) | **qa_steps:** 4 | **pause_for_verdict:** always

## CEO Context

Small cycle — **3 entries pending**, the three dated 2026-07-07 in LESSONS.md (session-limit 429 defeats runner retry-once [bellows]; classifier file-existence claims must be disk-verified [planner-discipline]; qa_steps header is a step-number list, not a count [planner-discipline]). The 2026-07-07 baton predicted exactly these and no cycle has run since 2026-07-06.

**Pre-flight verified 2026-07-16 (CEO session, read-only):** canonical DB holds 137 entries / 145 proposals with `proposed=0` — every prior proposal is dispositioned (implemented 97, superseded 28, rejected 15, stale 3, reference 2). `get_unclassified_entries(conn)` returns `[]` **pre-ingest**, so the 3 new entries are the entire work list once ingested (expected IDs 138–140). Full suite **52 passed** — this also answers the baton's open "session-end suite: verify at next session start." The `route` column is present on canonical, so **there is no migration hazard this cycle** (unlike plan 131, whose Step 1 had to fire the plan-128 migration). Working tree clean.

**What makes this cycle worth watching — first live exercise of the plan-154 advisory.** Plan 154 (Done 2026-07-09) shipped `detect_recently_implemented_overlaps` and wired it read-only into `run_full_lessons_cycle` (returns key `recently_implemented_overlaps`) and into `generate_lessons_report` (renders a ⚠️ advisory line per overlapping proposal). No cycle has run since it shipped, so this is its **first production run**. The default `recency_days=45` measured from 2026-07-16 reaches back to ~2026-06-01, which **covers the 2026-07-07 Gate 2 codification** (plan 134 implemented 8 rules). Overlap advisories are therefore EXPECTED, plausibly on the two `planner-discipline` entries. **Surfacing an overlap is a success signal, not a failure** — the helper is deliberately recall-oriented, and a false surface costs one reviewer glance. The advisory is **ADVISORY ONLY**: it must not change any proposal status or insert any proposal. If a run of this plan mutates status from overlap output, halt — that is a plan-154 contract breach.

**Known shape, not a defect (do not "fix" it):** `run_full_lessons_cycle` computes overlaps over `candidate_ids` = **every** entry parsed from LESSONS.md (~140), not just the new ones, so Step 1's `recently_implemented_overlaps` may be long. `generate_lessons_report` scopes its own overlap computation to entries with `proposed`/`ambiguous` proposals (the 3 new ones), which is the reviewer-facing surface. Step 1 reports the total count plus the slice for the new entries; observations about the breadth go in the dev-log for a future plan, not a code change here.

**Capture-rate observation for CEO (not blocking):** LESSONS.md has received **no new entries since 2026-07-07** despite nine days of shop work (exec-196 → exec-201, the auto-park guard fix, the schema-v17 fix). The corpus is fed by hand, so a thin cycle may reflect capture drift rather than a quiet shop. Noted for Gate 1, not actionable inside this plan.

**Scope discipline:** this is a cycle run only. Gate 1 route disposition and Gate 2 codification are separate sessions. The classifier does NOT assign routes (`route=None` at insert) — the CEO assigns routes at Gate 1 via `set_proposal_route()`. The baton's `plan_lint qa_steps cross-check` thread is a separate plan and is out of scope here, even though entry 140 is its source lesson.

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

## How to Run This Plan

Paste the bootstrap prompt into Claude Code. The agent reads the full plan file and executes Step 1 ONLY, then STOPS for CEO confirmation. Never skip steps, auto-chain, or move the plan to Done before all steps including QA complete.

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-cycle-2026-07-16.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2 or move the plan to Done.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Developer. Read your specialist file at `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` first (cross-repo). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. All canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute or to skip a verification.
>
> **Scope:**
> - `knowledge/development/cycle-result-2026-07-16.json`
> - `knowledge/development/dev-log-cycle-step-1-2026-07-16.md`
>
> **Part A — run the cycle.** Import `run_full_lessons_cycle` and `get_unclassified_entries` from `src.lessons_forge`, connect to the canonical DB by absolute path, call `run_full_lessons_cycle(conn)`, then **commit**. Ingestion of **exactly 3 new entries is EXPECTED** (the three 2026-07-07 LESSONS.md entries; expected IDs 138–140). **HALT and flag if `ingested_count` is 0** — that means the ingest path did not see the new entries. If `ingested_count` is neither 0 nor 3, do NOT halt: record the actual count and the headings ingested, and flag it in the receipt for the Planner to review at the verdict pause (LESSONS.md may have grown since the plan was authored — that is a legitimate outcome, not an error).
>
> **Part B — derive the authoritative work list.** Call `get_unclassified_entries(conn)` (Orchestration Rule #47 — never a hand-copied query, never any other field). Print it. Pre-ingest this returned `[]`, so the list should be exactly the newly-ingested entries.
>
> **Part C — record the dedup advisory (read-only, no action).** From the cycle result, report `len(recently_implemented_overlaps)` (computed DB-wide over all parsed entries — a long list is expected and is NOT a defect) AND the filtered slice whose `entry_id` is in the Part B work list. The slice is the reviewer-facing signal Step 2/3 care about. Do NOT act on it, do NOT insert or mutate any proposal from it, and do NOT modify `src/` — this step changes no product code.
>
> **Deposit:** write `{cycle_result, worklist, overlaps_total, overlaps_for_worklist}` to `knowledge/development/cycle-result-2026-07-16.json`, and a dev log at `knowledge/development/dev-log-cycle-step-1-2026-07-16.md` containing the verbatim cycle counts, the work list, the overlap total + work-list slice (with each `overlap_reason`), and an Output Receipt with status (include the work list in the receipt). Use the canonical Python file-write pattern — no heredoc. Commit both deposits together. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/cycle-result-2026-07-16.json`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 2. Do NOT move the plan to Done. Wait for CEO verdict before continuing.**

---
---

## STEP 2 — Lessons Agent

---

> **Before starting, read the Step 1 deposits (`knowledge/development/cycle-result-2026-07-16.json` and the dev log) and check the Output Receipt status. If status is not Complete, halt and report the blocker.**
>
> You are the Forge Lessons Agent. Read your specialist file at `agents/FORGE_LESSONS_AGENT.md` first (ADR-002 six-value taxonomy). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`; canonical DB by absolute path only.
>
> **Scope:**
> - `knowledge/development/classifications-summary-2026-07-16.md`
> - `knowledge/development/dev-log-cycle-step-2-2026-07-16.md`
>
> Derive the work list yourself by calling `get_unclassified_entries(conn)` directly (Rule #47 — never trust a copied list). Cross-check against Step 1's JSON; on mismatch, halt and flag. For each entry ID: read `id, source_heading, raw_content, tags, entry_date` from `lesson_entries`, apply the ADR-002 taxonomy, and `insert_proposal(conn, ...)` with per-entry `reasoning` citing specific `raw_content` text. **Do NOT pass `route`** (leave default `None`) — route assignment is a Gate 1 CEO disposition, not a classifier judgment. Do NOT assign `category='duplicate'`; `status='ambiguous'` only for genuine no-fit. Do NOT dedup against PLANNER_TEMPLATE — Gate 1 dedups against the LIVE template (2026-06-07 discipline); your job is classification only. Commit after inserting.
>
> **Disk-verify every filesystem claim (entry 139 is literally this lesson).** If your reasoning asserts that a file exists, does not exist, or moved, verify it with `ls`/`git log` against disk BEFORE writing the claim, and say in the summary that you did. The 2026-07-06 classifier carried a stale "FORGE_QA.md does not exist" flag for three weeks; do not reproduce that miss while classifying the entry that reports it.
>
> **Use the Step 1 dedup advisory as input, not as a verdict.** For each work-list entry with a `recently_implemented_overlaps` hit, read the named implemented proposal and state in your per-entry reasoning whether the entry is genuinely subsumed by it or merely adjacent. **You still classify the entry either way** — you have NO authority to skip, drop, or mark it superseded on overlap evidence; subsumption is a CEO Gate 1 call. Surfacing your assessment is the whole point of plan 154 — record it so Gate 1 does not need a manual `git blame`.
>
> **Deposit:** `knowledge/development/classifications-summary-2026-07-16.md` — count, category/confidence distribution, per-entry overlap assessment (subsumed vs adjacent, with the proposal ID), and cluster synthesis for CEO Gate 1 (expect a `planner-discipline` cluster: entries 139/140 are both verification-discipline lessons). Plus a dev log at `knowledge/development/dev-log-cycle-step-2-2026-07-16.md` with an Output Receipt (total classified, distribution, flags). Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-summary-2026-07-16.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-2-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 3. Wait for CEO verdict.**

---
---

## STEP 3 — DEV

---

> **Before starting, read the Step 2 deposits and confirm Output Receipt status Complete; otherwise halt and report.**
>
> You are the Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md`). All commands from `/Users/marklehn/Developer/GitHub/lessons-forge`; canonical DB by absolute path.
>
> **Scope:**
> - `reports/lessons-report-2026-07-16.md`
> - `knowledge/development/dev-log-cycle-step-3-2026-07-16.md`
>
> Run `generate_lessons_report(conn, "2026-07-16")` against the canonical DB (it writes to `reports/`). All route values are NULL this cycle — the report must render without route lines (plan-128 conditional render); if any `- **Route:**` line appears, halt and flag.
>
> **Verify the plan-154 advisory rendering — this is its first production run.** Count the `Recently-implemented overlap:` lines in the report and reconcile them against the Step 2 per-entry overlap assessment: the report renders overlaps for entries with `proposed`/`ambiguous` proposals, so it should match the Step 1 work-list slice. Report the count either way. **Zero advisory lines is a legitimate outcome — do NOT halt on it, and do NOT tune the heuristic to manufacture a hit** (that is out of scope and would be product-code change on a report step). Just record the count and, if zero, note it against the CEO Context expectation so the Planner can judge whether the 45-day window behaved as predicted.
>
> Print the report head (~80 lines) for the transcript.
>
> **Deposit:** the report plus `knowledge/development/dev-log-cycle-step-3-2026-07-16.md` with an Output Receipt (report length, proposal count surfaced, advisory-line count, route-line count = 0). Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-07-16.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-3-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 4. Wait for CEO verdict.**

---
---

## STEP 4 — QA

---

> **Before starting, read the Step 3 deposits and confirm Output Receipt status Complete; otherwise halt and report.**
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **Verification + reporting only — no product-code changes.** If you find a blocker, STOP and report it.
>
> **Rule 20 self-check is gate-enforced on this step.** Your QA report MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. The verification table does NOT by itself satisfy the gate — end with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule (entries 136/137 are this lesson — do not reproduce the miss).** Every PRAGMA/SQL row states which DB it ran against. Canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"` — worktree DB absence is never a substitution reason. Deposit RAW command output, never a summary of it.
>
> **Scope:**
> - `knowledge/qa/cycle-qa-2026-07-16.md`
>
> Verification table, one row per claim, each with a DB-source column: (1) full suite green — `python3 -m pytest src/ -v` (use `python3 -m pytest`, NOT the `timeout` binary — unavailable on macOS) to an explicit pass/fail with the tail shown; baseline is **52 passed** as of 2026-07-16, confirm 0 regressions; (2) `get_unclassified_entries(conn)` on canonical returns `[]` (all classified); (3) invariants on canonical: dangling proposals 0, invalid category 0, invalid confidence 0, and all proposals created this cycle have `route IS NULL`; (4) **plan-154 advisory-only contract held** — the count of `lesson_proposals` rows and their statuses changed ONLY by this cycle's classifier inserts; no proposal status was mutated from overlap output, and no `category='duplicate'` row was inserted from the advisory path; (5) schema drift — `.schema lesson_entries` and `.schema lesson_proposals` on canonical vs `src/db.py` DDL: the `route` column and the `reference` value in the `status` CHECK constraint ARE expected in both (plans 128/135); any other delta is a failure; (6) report exists, proposal counts match DB, zero `- **Route:**` lines, and the advisory-line count matches the Step 3 dev-log; (7) post-cycle DB counts (entries total, proposals by status and category). If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/cycle-qa-2026-07-16.md` — verification table with DB-source column, full-suite tail, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph: cycle run 2026-07-16 complete (N entries ingested, M classified, first live plan-154 advisory run with K overlaps surfaced, report deposited; Gate 1 disposition pending); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-qa-2026-07-16.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
