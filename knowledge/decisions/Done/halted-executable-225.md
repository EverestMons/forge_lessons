# Lessons Forge — Cycle Run 2026-07-17 (ingest the six-lesson batch: drafting cycle ×2, worktree-QA, bare-number, region-scope, schema-pins)
**Date:** 2026-07-17 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (DEV) → Step 2 (Lessons Agent) → Step 3 (DEV) → Step 4 (QA) | **qa_steps:** 4 | **pause_for_verdict:** always

## CEO Context

**Six LESSONS.md entries await ingestion — the largest batch since the corpus-integrity fix, and the batch that carries the CEO's parked DRAFTING CYCLE governance toward Gate 2.** Appended since cycle 2026-07-16 (plan 205), in file order: (1) never state a bare expected number (2026-07-16); (2) the drafting cycle (2026-07-16); (3) worktree QA cannot verify a live-DB migration (2026-07-17); (4) drafting cycle pass 4 — integration-vs-record, AMENDS entry (2) and must reach Gate 2 with it (2026-07-17); (5) region-scoped metrics computed unscoped (2026-07-17); (6) schema-bump version pins (2026-07-17).

**Pre-flight verified 2026-07-17 (CEO session, read-only, canonical absolute path):** 140 entries / 148 proposals, `proposed = 0` (every prior proposal dispositioned: implemented 99, superseded 28, rejected 15, stale 3, reference 3). `get_unclassified_entries(conn)` returns `[]` pre-ingest — the six new entries are the entire expected work list once ingested (expected IDs 141–146; verify and report actual, never force). Full suite **55 passed**. No schema hazard: no migrations pending on the forge DB.

**The 204-fix regression signal (watch it, don't assume it):** every append since plan 204's `_normalize_for_hash` fix has left prior entries' hashes stable — `updated_count` is EXPECTED to be 0 this cycle. If `updated_count > 0`, that is either a genuine content edit to an old entry or a NEW hash-stability bug: do not proceed silently — report which entries updated and their headings, and flag for the Planner at the verdict pause. (Under the pre-204 code, this six-append batch would have staled multiple implemented proposals; zero updates is the fix proving itself at batch scale.)

**No dedup advisory exists anymore** — plan 207 retired it. `run_full_lessons_cycle` returns no overlap key; the report renders no advisory lines. Do not miss it, do not rebuild it.

**Classifier discipline (codified since the last cycle — these now bind):** Rule 52 (v4.74) — re-verify inherited claims against ground truth before they inform classification; any filesystem-state claim in reasoning is disk-verified first (`ls`/`git log`), and CITED IDENTIFIERS in lesson text (function names, file paths) are spot-checked against the repos they reference before being repeated in reasoning — the `_parse_session_limit_reset` fabrication is the cautionary case. Routes are NOT assigned (`route=None`; Gate 1 is the CEO's). No `category='duplicate'`; `ambiguous` only for genuine no-fit. Note for synthesis: entries (2) and (4) are one governance item (4 amends 2) — classify each on its own merits but state the linkage for Gate 1.

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-cycle-2026-07-17.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2 or move the plan to Done.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Developer. Read `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` first (cross-repo; skip with a note if absent). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. All canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute or skip a verification.
>
> **Scope:**
> - `knowledge/development/cycle-result-2026-07-17.json`
> - `knowledge/development/dev-log-cycle-step-1-2026-07-17.md`
>
> **Part A — run the cycle.** Import `run_full_lessons_cycle` and `get_unclassified_entries` from `src.lessons_forge`, connect to the canonical DB by absolute path, call `run_full_lessons_cycle(conn)`, then **commit**. Expected: `ingested_count` = 6 (verify and report actual — if 0, HALT and flag: the ingest saw nothing; any other number is reported with the headings actually ingested, not forced). Expected: `updated_count` = 0 (the 204-fix signal — if nonzero, report WHICH entries and their headings, and flag prominently for the Planner; do not halt, do not proceed past Step 1 silently).
>
> **Part B — derive the authoritative work list.** `get_unclassified_entries(conn)` (Orchestration Rule #47 — never a hand-copied list). Print it. Pre-ingest it was `[]`, so the list should be exactly the newly-ingested entries.
>
> **Deposit:** write `{cycle_result, worklist, worklist_headings}` to `knowledge/development/cycle-result-2026-07-17.json`, and a dev log at `knowledge/development/dev-log-cycle-step-1-2026-07-17.md` with verbatim cycle counts, the work list with headings, the updated_count signal statement, and an Output Receipt with status (work list in the receipt). Canonical Python file-write pattern — no heredoc. Commit both deposits together. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/cycle-result-2026-07-17.json`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-07-17.md`
>
> **STOP. Do NOT proceed to Step 2. Do NOT move the plan to Done. Wait for CEO verdict.**

---
---

## STEP 2 — Lessons Agent

---

> **Before starting, read the Step 1 deposits and check the Output Receipt status. If not Complete, halt and report the blocker.**
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first (ADR-002 six-value taxonomy). All commands from `/Users/marklehn/Developer/GitHub/lessons-forge`; canonical DB by absolute path only.
>
> **Scope:**
> - `knowledge/development/classifications-summary-2026-07-17.md`
> - `knowledge/development/dev-log-cycle-step-2-2026-07-17.md`
>
> Derive the work list yourself via `get_unclassified_entries(conn)` (Rule #47); cross-check against Step 1's JSON; on mismatch, halt and flag. For each entry: read `id, source_heading, raw_content, tags, entry_date`, apply the ADR-002 taxonomy, `insert_proposal(conn, ...)` with per-entry `reasoning` citing specific `raw_content` text. Do NOT pass `route`. No `category='duplicate'`; `ambiguous` only for genuine no-fit. Commit after inserting.
>
> **Rule 52 binds this step (it is live governance, v4.74):** disk-verify every filesystem claim before it enters reasoning; spot-check cited identifiers (function names, paths) in the lesson bodies against the actual repos before repeating them — record each verification in the summary. In the synthesis: state the (drafting cycle)+(pass 4 amendment) linkage as ONE Gate-2 governance item; call out expected clusters (planner-discipline dominates this batch).
>
> **Deposit:** `knowledge/development/classifications-summary-2026-07-17.md` — count, category/confidence distribution, the amendment linkage, verification log, cluster synthesis for CEO Gate 1; plus dev log `knowledge/development/dev-log-cycle-step-2-2026-07-17.md` with an Output Receipt (total classified, distribution, flags). Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-summary-2026-07-17.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-2-2026-07-17.md`
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
> - `reports/lessons-report-2026-07-17.md`
> - `knowledge/development/dev-log-cycle-step-3-2026-07-17.md`
>
> Run `generate_lessons_report(conn, "2026-07-17")` against the canonical DB. All route values are NULL this cycle — zero `- **Route:**` lines (plan-128 conditional render); if any appears, halt and flag. The plan-207 retirement means zero advisory lines exist in the codepath — if any `Recently-implemented overlap` text appears, halt and flag (it would mean retired code resurrected). Print the report head (~80 lines) for the transcript.
>
> **Deposit:** the report plus `knowledge/development/dev-log-cycle-step-3-2026-07-17.md` with an Output Receipt (report length, proposal count surfaced, route-line count = 0). Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-07-17.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-3-2026-07-17.md`
>
> **STOP. Do NOT proceed to Step 4. Wait for CEO verdict.**

---
---

## STEP 4 — QA

---

> **Before starting, read the Step 3 deposits and confirm Output Receipt status Complete; otherwise halt and report.**
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` first. All commands from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Rule 20 self-check is gate-enforced on this step.** Your report MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` and a line reading exactly `**PASSED — SELF-CHECK PASSED**`; end with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule (codified — entries 136/137):** every SQL row states which DB it ran against; canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. Worktree DB absence is never a substitution reason. Deposit RAW output, never summaries.
>
> **Scope:**
> - `knowledge/qa/cycle-qa-2026-07-17.md`
>
> Verification table, one row per claim, DB-source column on each: (1) full suite — `python3 -m pytest src/ -v` (never the `timeout` binary) to explicit pass/fail with tail; baseline **55 passed**, verify and report actual; (2) `get_unclassified_entries(conn)` on canonical returns `[]`; (3) invariants on canonical: dangling proposals 0, invalid category 0, invalid confidence 0, all proposals created this cycle have `route IS NULL`; (4) the 204-fix signal held — `updated_count` was 0 in Step 1's JSON (quote it) and no proposal changed status to `stale` this cycle (stale count still 3); (5) schema drift — `.schema` both tables vs `src/db.py` DDL (route column + reference CHECK value expected; any other delta fails); (6) report exists, proposal counts match DB, zero route lines, zero advisory lines; (7) post-cycle DB counts (entries total, proposals by status and category — expected entries 146, proposals 154, proposed 6; verify and report actual, never force). Any failing row: report and halt.
>
> **Deposit:** `knowledge/qa/cycle-qa-2026-07-17.md` — the table, full-suite tail, Rule 20 banner + PASSED line, Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph: cycle 2026-07-17 complete (N ingested incl. the drafting-cycle pair, M classified, 204-fix signal held at batch scale, report deposited; Gate 1 disposition pending — the drafting-cycle governance is now one Gate away from PLANNER_TEMPLATE); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-qa-2026-07-17.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
