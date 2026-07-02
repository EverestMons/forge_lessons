# Lessons Forge — `needs_classification` Return-Shape Fix (delegate to canonical helper)
**Date:** 2026-07-02 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (DEV) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always

## CEO Context

Closes the baton horizon item "`run_full_lessons_cycle` `needs_classification` over-report refactor" (entry 117's deferred "candidate code fix"). Current behavior: `run_full_lessons_cycle` (src/lessons_forge.py:353) computes `needs_classification` at lines 436–444 as ALL parsed entry IDs minus only those carrying a `category='duplicate'` proposal — so entries already dispositioned in prior cycles (`implemented`/`rejected`/`proposed`/etc.) are still reported as needing classification. The consumer side is already protected (Orchestration Rule #47: work lists come from `get_unclassified_entries(conn)`, src/lessons_forge.py:205, whose docstring warns against the over-reporting field). This plan fixes the producer: the function's `needs_classification` delegates to the canonical helper. Key design fact the DEV must preserve: the helper call goes AFTER cycle Step 4 (duplicate-proposal insertion), because the just-inserted duplicate proposals have `status='proposed'` and are therefore excluded by the helper automatically — the 436–444 loop collapses into one call. Semantic change (intended): the field becomes DB-wide unclassified entries rather than parse-scoped — which is what Rule #47's canonical work list already means. Rule #47 itself stays in force as defense-in-depth; PLANNER_TEMPLATE.md is NOT touched by this plan.

## How to Run This Plan

Paste the bootstrap prompt into Claude Code. The agent reads the full plan file and executes Step 1 ONLY. After completing Step 1, the agent STOPS and waits for CEO confirmation before proceeding to Step 2. The agent must never skip steps, auto-chain, or move the plan to Done without completing all steps including QA.

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-cycle-needs-classification-return-shape-2026-07-02.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2 or move the plan to Done.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are the Lessons Forge Developer. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.
>
> **Change 1 — delegate the field to the canonical helper.** In `src/lessons_forge.py`, replace the `needs_classification` computation block (the comment line `# Compute needs_classification: all entry IDs minus those with duplicate proposals` plus the loop through its append, currently lines 436–444) with a single call placed at the same position (after cycle Step 4's duplicate-proposal insertion loop): `needs_classification = get_unclassified_entries(conn)`. Position is load-bearing — the helper excludes the duplicate proposals Step 4 just inserted only because they exist by the time it runs. Remove the now-unused `duplicate_entry_ids` set ONLY if nothing else reads it — check first; if it is still read anywhere, leave it.
>
> **Change 2 — docstring truth maintenance.** (a) In `run_full_lessons_cycle`'s docstring, update the `needs_classification` return-key description to state it is computed via `get_unclassified_entries(conn)` after duplicate-proposal insertion, is DB-wide (not parse-scoped), and matches the canonical Rule #47 work list. (b) In `get_unclassified_entries`'s docstring, the sentence warning "Do NOT derive a work list from run_full_lessons_cycle().needs_classification — it over-reports every parsed entry" becomes stale — replace it with a note that as of 2026-07-02 the cycle's field delegates to this helper, and this helper remains the canonical source. Keep the `NOT EXISTS (any proposal)` warning sentence — that hazard is unchanged.
>
> **Change 3 — tests.** In `src/test_lessons_forge.py`: the two existing cycle tests (`test_run_full_lessons_cycle_fresh`, `test_run_full_lessons_cycle_with_duplicates`) exercise fresh DBs where old and new semantics coincide — they should pass UNCHANGED. If either fails, halt and report in the Output Receipt; do NOT rewrite their assertions to make them pass. Add new tests: (a) an entry with a pre-existing non-stale proposal (e.g. status `implemented`) is EXCLUDED from `needs_classification` on a subsequent cycle run — this is the over-report regression test and it must fail against the old code's semantics (assert the dispositioned entry id is absent); (b) an entry whose only proposal has status `stale` IS included (re-queued-edit path); (c) the invariant from the existing duplicates test still holds on a fresh DB (needs_classification + duplicates_marked_count == total parsed entries).
>
> **Self-verify.** Run the FULL suite with `timeout 600 python3 -m pytest src/ -v` to an explicit pass/fail and READ THE TAIL — never infer green from a subset or collect count. All tests must pass including the three new ones.
>
> **Commit** with a descriptive message (e.g. `fix(lessons-forge): needs_classification delegates to get_unclassified_entries — over-report closed`).
>
> **Deposit:** `lessons-forge/knowledge/development/lessons-cycle-needs-classification-return-shape-2026-07-02.md` — dev log with: the exact diff hunks (or verbatim old/new blocks), the docstring edits, the three new test names + one-line rationale each, the full-suite tail verbatim, commit hash, and an Output Receipt with status. Use the canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback` (daemon-owned; do NOT edit any feedback file directly).
>
> **STOP. Do NOT proceed to Step 2. Do NOT move the plan to Done. Wait for CEO verdict before continuing.**

---
---

## STEP 2 — QA

---

> **Before starting, read the Step 1 dev-log deposit at `lessons-forge/knowledge/development/lessons-cycle-needs-classification-return-shape-2026-07-02.md` and check its Output Receipt status. If status is not Complete, halt and report the blocker before proceeding.**
>
> You are Lessons Forge QA. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first.
>
> **Rule 20 self-check is gate-enforced on this step.** Your QA report MUST include the byte-exact banner `Rule 20 — QA Self-Check Results` and a `PASSED — SELF-CHECK PASSED` line; the verification table below does NOT by itself satisfy the gate — end with a self-grep confirming the banner is present in your deposited report.
>
> Verify the return-shape fix. Produce a verification table, one row per claim: (1) `run_full_lessons_cycle` contains exactly one `needs_classification` assignment and it is `get_unclassified_entries(conn)`, positioned after the duplicate-proposal insertion loop — prove with a quoted code excerpt; (2) the old minus-duplicates loop is gone (grep for the old comment string `all entry IDs minus those with duplicate proposals` returns 0 hits in src/); (3) regression test (a) exists and asserts a dispositioned entry is absent from the returned list — run it in isolation to a pass; (4) stale-only inclusion test (b) exists and passes; (5) both PRE-EXISTING cycle tests pass with assertions untouched — verify via `git diff HEAD~1 -- src/test_lessons_forge.py` that no existing assertion lines were modified (additions only); (6) both docstrings updated per the plan (helper's stale warning replaced, cycle's return-key description states helper delegation) — quote them; (7) full suite green: re-run `timeout 600 python3 -m pytest src/ -v` to an explicit pass/fail and show the tail. If any row fails, report it and halt — do not pass a broken deliverable.
>
> **Baton close-out (in-repo direct edit — NEXT_SESSION.md is not a daemon-owned ledger).** In `lessons-forge/NEXT_SESSION.md`, annotate the horizon item closed. Exact-string edit — `old_string` (the paragraph line under `### \`run_full_lessons_cycle\` \`needs_classification\` over-report refactor (BACKLOG candidate) [carried]`):
>
> ```
> The consumer-side fix (the helper) is codified and sufficient for correctness. The function still returns every parsed entry in `needs_classification` — the deeper return-shape root (entry 117's "candidate code fix, separate"). File in lessons-forge/Bellows BACKLOG; not blocking.
> ```
>
> `new_string`:
>
> ```
> The consumer-side fix (the helper) is codified and sufficient for correctness. The function still returns every parsed entry in `needs_classification` — the deeper return-shape root (entry 117's "candidate code fix, separate"). File in lessons-forge/Bellows BACKLOG; not blocking. **CLOSED 2026-07-02:** `needs_classification` now delegates to `get_unclassified_entries(conn)` post-duplicate-insertion; over-report regression test added; Rule #47 remains in force as defense-in-depth.
> ```
>
> **Deposit:** `lessons-forge/knowledge/qa/lessons-cycle-needs-classification-return-shape-qa-2026-07-02.md` — verification table, full-suite tail, the Rule 20 self-check block, and an Output Receipt with status. Commit the QA report + baton edit together. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph: needs_classification over-report closed 2026-07-02, producer now delegates to the canonical Rule #47 helper, regression-tested; `#### Prompt Feedback` — standard. On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
