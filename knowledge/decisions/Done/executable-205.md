# Lessons Forge — Cycle Run 2026-07-16 (re-dispatch after the plan-204 root-cause fix)
**Date:** 2026-07-16 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (Lessons Agent) → Step 2 (DEV) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always

## CEO Context

**Re-dispatch of plan 203, which was halted at its Step 1 verdict on a corpus-integrity finding. Plan 204 (closed 2026-07-16) fixed the root cause. This plan finishes the cycle.**

**Why 203 halted, in one line:** appending lessons to LESSONS.md gave the previous last entry a trailing `---`, flipping its `content_hash` over 7 bytes of whitespace, which staled its `implemented` proposal and manufactured a rejected-duplicate every cycle (100% waste across entries 93/116/123). Plan 204 normalized the hash input, guarded terminal statuses from silent demotion, backfilled 83 hashes, and restored proposal 145. Corpus verified back at the pre-corruption baseline (`implemented 97, reference 2, rejected 15, stale 3, superseded 28`), suite 52 → 61, 0 regressions.

**⚠️ INGESTION ALREADY HAPPENED — DO NOT TREAT `ingested_count == 0` AS A FAILURE.** Plan 203's Step 1 committed the ingest before halting: entries **138, 139, 140** already exist in canonical. This plan starts at CLASSIFICATION. There is no ingest step and none is needed. (Plan 203's Step 1 instructed a halt on `ingested_count == 0`; that instruction is void here — it was written for a pre-ingest cycle.)

**The work list is exactly [138, 139, 140]** — verified on canonical 2026-07-16 after the 204 fix. Entry 137 is correctly ABSENT (its proposal 145 is `implemented` again, no longer staled). If your derived list contains 137, or anything else, **halt and flag** — that would mean the 204 fix regressed.

The three entries, all dated 2026-07-07:
- **138** — Session-limit 429 defeats runner retry-once — pause-and-hold needed `[tag: bellows]`
- **139** — Classifier file-existence claims must be disk-verified before disposition `[tag: planner-discipline]`
- **140** — qa_steps header is a step-number list, not a count `[tag: planner-discipline]`

**On the plan-154 dedup advisory — it is KNOWN NOISY; do not over-weight it.** Its first production run (plan 203 Step 1) measured **353 overlaps DB-wide**, and for entry 138 returned **10 hits all reading `tag overlap: bellows; keyword overlap: bellows`** — the heuristic degenerates to tag equality. CEO decision 2026-07-16: **note and defer** its fate to Gate 1; it is advisory-only and harmless. Do NOT modify `detect_recently_implemented_overlaps`, and do NOT let a tag-equality hit talk you out of classifying an entry. Its motivating case (proposal 131) is now known to have been a symptom of the bug 204 fixed, so treat its output as a weak prior at best.

**Capture-rate observation for CEO (not actionable here):** LESSONS.md has had no new entries since 2026-07-07 despite nine days of shop work (exec-196 → 201, auto-park guard fix, schema-v17 fix). The corpus is hand-fed; the thin cycle likely reflects capture drift rather than a quiet shop.

**Scope discipline:** cycle run only. Gate 1 route disposition and Gate 2 codification are separate sessions. Routes stay `None` at insert — the CEO assigns at Gate 1 via `set_proposal_route()`. The baton's `plan_lint qa_steps cross-check` thread is a separate plan and stays out of scope even though entry 140 is its source lesson. The 98/121/130 audit disposition is a CEO Gate 1 call, not this plan's.

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-cycle-redispatch-2026-07-16.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — Lessons Agent

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read your specialist file at `agents/FORGE_LESSONS_AGENT.md` first (ADR-002 six-value taxonomy). All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **All canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute.
>
> **Scope:**
> - `knowledge/development/classifications-summary-2026-07-16.md`
> - `knowledge/development/dev-log-cycle-step-1-2026-07-16.md`
>
> **Derive the work list yourself** by calling `get_unclassified_entries(conn)` directly (Orchestration Rule #47 — never a hand-copied list). It MUST be exactly `[138, 139, 140]`; halt and flag on any deviation (see CEO Context). Do NOT run `run_full_lessons_cycle` — ingestion is already done and this step must not re-run it.
>
> For each entry ID: read `id, source_heading, raw_content, tags, entry_date` from `lesson_entries`, apply the ADR-002 taxonomy, and `insert_proposal(conn, ...)` with per-entry `reasoning` citing specific `raw_content` text. **Do NOT pass `route`** (leave default `None`) — route assignment is a Gate 1 CEO disposition. Do NOT assign `category='duplicate'`; use `status='ambiguous'` only for genuine no-fit. Do NOT dedup against PLANNER_TEMPLATE — Gate 1 dedups against the LIVE template (2026-06-07 discipline); your job is classification only. **Commit** after inserting.
>
> **Disk-verify every filesystem claim — entry 139 IS this lesson.** If your reasoning asserts a file exists, does not exist, or moved, verify with `ls`/`git log` against disk BEFORE writing the claim, and state in the summary that you did. The 2026-07-06 classifier carried a stale "FORGE_QA.md does not exist" flag for three weeks; do not reproduce that miss while classifying the entry that reports it.
>
> **Optional context, weak prior only:** you may consult `detect_recently_implemented_overlaps(conn, [138,139,140])` read-only. Per CEO Context it is known to degenerate to tag equality — record any hit you find genuinely informative, ignore the rest, and classify all three entries regardless. You have NO authority to skip, drop, or supersede an entry on overlap evidence.
>
> **Deposit:** `knowledge/development/classifications-summary-2026-07-16.md` — count, category/confidence distribution, per-entry reasoning, and cluster synthesis for CEO Gate 1 (expect a `planner-discipline` cluster: 139 and 140 are both verification-discipline lessons; 138 is a `bellows` daemon-behaviour lesson whose fix already shipped — note that if you find it). Plus `knowledge/development/dev-log-cycle-step-1-2026-07-16.md` with an Output Receipt (total classified, distribution, work list, flags). Canonical Python file-write pattern — no heredoc. Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-summary-2026-07-16.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — DEV

---

> **Before starting, read the Step 1 deposits and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2.
>
> You are the Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md`; skip with a note if absent). All commands from `/Users/marklehn/Developer/GitHub/lessons-forge`; canonical DB by absolute path.
>
> **Scope:**
> - `reports/lessons-report-2026-07-16.md`
> - `knowledge/development/dev-log-cycle-step-2-2026-07-16.md`
>
> Run `generate_lessons_report(conn, "2026-07-16")` against the canonical DB. All route values are NULL this cycle — the report must render without route lines (plan-128 conditional render); if any `- **Route:**` line appears, halt and flag.
>
> **Advisory lines are EXPECTED and are not a defect.** `generate_lessons_report` calls the plan-154 overlap detector for rendered proposals; per CEO Context that detector is tag-equality noisy, so ⚠️ `Recently-implemented overlap:` lines will likely appear (entry 138 drew 10 hits in the 203 run). Record the count. **Zero is also legitimate — do NOT halt either way, and do NOT tune the heuristic** (out of scope; CEO deferred its fate to Gate 1).
>
> Print the report head (~80 lines) for the transcript.
>
> **Deposit:** the report plus `knowledge/development/dev-log-cycle-step-2-2026-07-16.md` with an Output Receipt (report length, proposals surfaced, advisory-line count, route-line count = 0). Canonical Python file-write pattern — no heredoc. Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-07-16.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-2-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 3. Wait for CEO verdict.**

---
---

## STEP 3 — QA

---

> **Before starting, read the Step 1 and Step 2 deposits and confirm both Output Receipt statuses Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 3 (QA).
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` first. All commands from `/Users/marklehn/Developer/GitHub/lessons-forge`. **Verification + reporting only — no product-code changes.** If you find a blocker, STOP and report it.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule — entries 136/137 are literally this lesson, and 139 demands disk-verification.** Every SQL/PRAGMA row states which DB it ran against. Canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. Worktree DB absence is never a substitution reason. Deposit **RAW command output**, never a summary of it.
>
> **Scope:**
> - `knowledge/qa/cycle-qa-2026-07-16.md`
>
> Verification table, one row per claim, each with a DB-source column:
> 1. **Full suite** — `python3 -m pytest src/ -v` (`python3 -m pytest`, NOT the `timeout` binary — unavailable on macOS) to an explicit pass/fail, raw tail shown. **Baseline is 61 passed** (52 pre-204 + 9 added by plan 204) — NOT 52. Confirm 0 regressions.
> 2. `get_unclassified_entries(conn)` on canonical returns `[]` — all three entries now classified.
> 3. **Invariants** on canonical: dangling proposals 0, invalid category 0, invalid confidence 0, and every proposal created this cycle has `route IS NULL`.
> 4. **The 204 fix still holds (regression watch):** proposal 145 is still `implemented`, entry 137 is still absent from the work list, and `stale` has NOT grown beyond 3. If classification somehow staled anything, halt loudly.
> 5. **Report** exists, proposal counts match DB, zero `- **Route:**` lines; advisory-line count matches the Step 2 dev-log.
> 6. **No schema drift** — `.schema lesson_entries` / `.schema lesson_proposals` on canonical vs `src/db.py` DDL. This plan changes no schema; `route` and the `reference` CHECK value are expected (plans 128/135). Any delta is a FAIL.
> 7. **Post-cycle DB counts** — entries total, proposals by status and category. Expect `implemented 97, superseded 28, rejected 15, stale 3, reference 2` PLUS the 3 new `proposed` rows from this cycle.
>
> If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/cycle-qa-2026-07-16.md` — verification table with DB-source column, raw full-suite tail, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (cycle 2026-07-16 complete: 3 entries classified post-204-fix, report deposited, corpus integrity held; Gate 1 disposition pending, including the 98/121/130 audit and plan-154's advisory fate); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-qa-2026-07-16.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
