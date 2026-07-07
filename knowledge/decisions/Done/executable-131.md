# Lessons Forge — Cycle Run 2026-07-06 (ingest 06-08 → 07-06 backlog)
**Date:** 2026-07-06 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (DEV) → Step 2 (Lessons Agent) → Step 3 (DEV) → Step 4 (QA) | **qa_steps:** 4 | **pause_for_verdict:** always

## CEO Context

First cycle since 2026-06-06/08 (28+ days dormant — diagnostic-127; the new cycle-nudge trigger fired on 114 plans closed since last ingestion). This cycle ingests every LESSONS.md entry accumulated since, including two 2026-07-06 entries captured today (qa-discipline evidence-source substitution; planner-discipline DB-source contract). MIGRATION ORDERING IS LOAD-BEARING: plan 128 (commit 643e9e7) added a `route` column that `insert_proposal()` now writes unconditionally, but the canonical `lessons-forge.db` has NOT yet migrated (verified 2026-07-06, plan 130) — the guarded migration fires at `init_db()`. Step 1 therefore runs `init_db()` against the canonical DB and PRAGMA-verifies the column BEFORE the cycle; skipping this breaks every proposal insert. The classifier does NOT assign routes this cycle (`route=None` at insert) — route-assignment criteria are not yet codified; the CEO assigns routes at Gate 1 disposition via `set_proposal_route()`. Gate 1 disposition and Gate 2 codification are separate sessions, out of scope. Unlike the 2026-06-06 cycle, no expected work list is pinned — Step 1 reports the helper-derived list and the Planner reviews it at the verdict pause before classification proceeds.

## How to Run This Plan

Paste the bootstrap prompt into Claude Code. The agent reads the full plan file and executes Step 1 ONLY, then STOPS for CEO confirmation. Never skip steps, auto-chain, or move the plan to Done before all steps including QA complete.

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-cycle-2026-07-06.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2 or move the plan to Done.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Developer. Read your specialist file at `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` first (cross-repo). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. All canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute.
>
> **Scope:**
> - `knowledge/development/cycle-result-2026-07-06.json`
> - `knowledge/development/dev-log-cycle-step-1-2026-07-06.md`
>
> **Part A — fire the route migration, then verify.** Run `db.init_db()` against the canonical DB (import from `src.db`, connect to the absolute path), then `PRAGMA table_info(lesson_proposals)` on the same connection and print the full column list. HALT if the `route` column is absent after init_db — that means the plan-128 migration did not fire, and every insert in Step 2 would fail.
>
> **Part B — run the cycle.** `run_full_lessons_cycle(conn)` on the canonical DB, commit, then derive the authoritative work list via `get_unclassified_entries(conn)` (Orchestration Rule #47 — never a hand-copied query, never any other field). Real ingestion is EXPECTED this run (LESSONS.md entries 2026-06-08 through 2026-07-06, roughly 8-14 entries incl. two dated 2026-07-06) — if `ingested_count` is 0, halt and flag: the ingest path did not see the new entries. Write `{cycle_result, worklist, pragma_columns}` to `knowledge/development/cycle-result-2026-07-06.json`. Print ingested/updated counts and the work list — the Planner reviews the list at this step's verdict before classification proceeds.
>
> **Deposit:** `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-07-06.md` — init_db + PRAGMA output verbatim, cycle counts, work list, and an Output Receipt with status (include the work list in the receipt). Use the canonical Python file-write pattern — no heredoc. Commit both deposits together. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/cycle-result-2026-07-06.json`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-07-06.md`
>
> **STOP. Do NOT proceed to Step 2. Do NOT move the plan to Done. Wait for CEO verdict before continuing.**

---
---

## STEP 2 — Lessons Agent

---

> **Before starting, read the Step 1 deposits (`knowledge/development/cycle-result-2026-07-06.json` and the dev log) and check the Output Receipt status. If status is not Complete, halt and report the blocker.**
>
> You are the Forge Lessons Agent. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first (ADR-002 six-value taxonomy). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`; canonical DB by absolute path only.
>
> **Scope:**
> - `knowledge/development/classifications-summary-2026-07-06.md`
> - `knowledge/development/dev-log-cycle-step-2-2026-07-06.md`
>
> Derive the work list yourself by calling `get_unclassified_entries(conn)` directly (Rule #47 — never trust a copied list). Cross-check against Step 1's JSON; on mismatch, halt and flag. For each entry ID: read `id, source_heading, raw_content, tags, entry_date` from `lesson_entries`, apply the ADR-002 taxonomy, and `insert_proposal(conn, ...)` with per-entry `reasoning` citing specific `raw_content` text. Do NOT pass `route` (leave default `None`) — route assignment is a Gate 1 CEO disposition, not a classifier judgment. Do NOT assign `category='duplicate'`; `status='ambiguous'` only for genuine no-fit. Do NOT dedup against PLANNER_TEMPLATE — Gate 1 dedups against the LIVE template (2026-06-07 discipline); your job is classification only. In the synthesis, call out cross-batch clusters (expect qa-discipline and daemon-discipline clusters from the 06-08/06-14 and 07-06 entries).
>
> **Deposit:** `lessons-forge/knowledge/development/classifications-summary-2026-07-06.md` — count, category/confidence distribution, cluster synthesis for CEO Gate 1, plus dev log at `lessons-forge/knowledge/development/dev-log-cycle-step-2-2026-07-06.md` with an Output Receipt (total classified, distribution, flags). Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-summary-2026-07-06.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-2-2026-07-06.md`
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
> - `reports/lessons-report-2026-07-06.md`
> - `knowledge/development/dev-log-cycle-step-3-2026-07-06.md`
>
> Run `generate_lessons_report(conn)` against the canonical DB and write it to `reports/lessons-report-2026-07-06.md`. All route values are NULL this cycle — the report must render without route lines (plan-128 conditional render); if any `- **Route:**` line appears, halt and flag. Print the report head (~80 lines) for the transcript.
>
> **Deposit:** the report plus `lessons-forge/knowledge/development/dev-log-cycle-step-3-2026-07-06.md` with an Output Receipt (report length, proposal count surfaced). Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-07-06.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-3-2026-07-06.md`
>
> **STOP. Do NOT proceed to Step 4. Wait for CEO verdict.**

---
---

## STEP 4 — QA

---

> **Before starting, read the Step 3 deposits and confirm Output Receipt status Complete; otherwise halt and report.**
>
> You are Lessons Forge QA. Read `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Rule 20 self-check is gate-enforced on this step.** Your QA report MUST include the byte-exact banner `Rule 20 — QA Self-Check Results` and a `PASSED — SELF-CHECK PASSED` line; the verification table does NOT by itself satisfy the gate — end with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule:** every PRAGMA/SQL row states which DB it ran against. Canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"` — worktree DB absence is never a substitution reason.
>
> **Scope:**
> - `knowledge/qa/cycle-qa-2026-07-06.md`
>
> Verification table, one row per claim: (1) full suite green — `python3 -m pytest src/ -v` to explicit pass/fail, tail shown; (2) `get_unclassified_entries(conn)` on canonical returns `[]` (all classified); (3) invariants on canonical: dangling proposals 0, invalid category 0, invalid confidence 0, all new proposals this cycle have `route IS NULL`; (4) schema drift — `.schema lesson_entries` and `.schema lesson_proposals` on canonical vs `src/db.py` DDL: the `route` column IS expected in both (plan 128 + Step 1 migration); any other delta is a failure; (5) report exists, proposal counts match DB, zero `- **Route:**` lines; (6) post-cycle DB counts (entries total, proposals by status and category). If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `lessons-forge/knowledge/qa/cycle-qa-2026-07-06.md` — verification table with DB-source column, full-suite tail, Rule 20 self-check block, Output Receipt with status. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph: cycle run 2026-07-06 complete (N entries ingested, M classified, route migration fired on canonical, report deposited; Gate 1 disposition pending); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-qa-2026-07-06.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
