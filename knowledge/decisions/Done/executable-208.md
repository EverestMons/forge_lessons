# Lessons Forge — Gate 2 Codification (cycle 2026-07-16): 2 edits + version bump from 2 codify-routed proposals
**Date:** 2026-07-16 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** none | **Execution:** Step 1 (DEV) → Step 2 (DEV) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always

## CEO Context

Gate 2 of the 2026-07-16 cycle. Gate 1 closed today (plan 206): 146→`reference`, 147→`codify`, 148→`codify`. This plan codifies the 2 codify-routed proposals as **2 edits** to governance-root `PLANNER_TEMPLATE.md`, bumps the version, and gives all three proposals their terminal status. Same DEV → QA shape as `Done/executable-134.md` (the structural precedent for footer convention, prose register, and the cross-repo no-commit rule).

**⚠️ THE LIVE TEMPLATE IS v4.73, NOT v4.71.** Both batons say v4.71 — they are **stale by two versions** (Planner-verified on disk 2026-07-16). v4.72 and v4.73 both landed 2026-07-09. **The dedup baseline for this Gate is v4.73, and the Planner's analysis below was performed against it.** This staleness is itself an instance of the failure mode Rule 52 (below) codifies — see the Dogfood note.

**CEO dispositions are final and embedded below.**

| Proposal | Entry | Disposition | Edit unit |
|---|---|---|---|
| 147 | 139 | **codify** → new **Rule 52** | Orchestration Plan Rules |
| 148 | 140 | **codify (residue only)** → **refine Checklist #16** | Plan Authoring Checklist |
| 146 | 138 | — | no edit; status→`reference` (Step 2) |

### Why 147 → a NEW rule, scoped BROADLY (CEO decision 2026-07-16)

**The gap is real and precisely located.** `Rule 39` (`:800`) already re-verifies stale SA-derived claims — but **only before an EDIT**, by the acting agent, scoped to the SA's declared queries. **Nothing protects a DISPOSITION.** Entry 139's FORGE_QA.md case involved no edit at all: a classifier's stale "file does not exist" flag (wrong for three weeks) nearly shaped a Gate 2 authoring decision. Rule 39 would never have fired.

**CEO widened the scope beyond entry 139's literal "filesystem state".** The baton flagged 139's rule as possibly too narrow, and this session produced **three** instances of the failure mode, **only one of them filesystem-shaped**: (a) the FORGE_QA.md stale flag; (b) the plan-205 classifier citing `_parse_session_limit_reset`, **a function that does not exist** (the real one is `_parse_session_reset`, `bellows/runner.py:36`) — a fabricated *identifier*, not a file; (c) the Planner refreshing both batons at 2026-07-16 ~10:30 carrying **two already-dead threads** (the session-end evidence-file convention, retired v4.72; the Workaround #3 factual tension, corrected v4.73) plus a two-version-stale template number — inherited from the prior baton without re-reading the template. Rule 52 therefore covers **any claim inherited from a generated artifact**, not just file existence.

**Dogfood note (state it in the rule's Why):** instance (c) was committed by the Planner **one hour after** authoring the verdict that flagged this same class of error, while writing the baton that carries this very Gate 2 agenda. The failure mode is not exotic and does not spare the person who just named it — which is exactly why it needs to be mechanical rather than remembered.

### Why 148 → refine Checklist #16, NOT a new qa_steps rule (CEO decision 2026-07-16)

**The qa_steps semantics were NEVER missing.** Line `:407` already states it verbatim: *"listing the step numbers that are QA-gated, as a comma-separated list of integers (e.g., `qa_steps: 2` or `qa_steps: 2,4`)"*. Line `:1193` reinforces it. **Proposal 148's first clause is already-covered — reject it on blame evidence, per the 131/135 precedent from the prior Gate 2.** Do NOT add a duplicate qa_steps rule.

**The novel residue is a refinement of Checklist #16, which ENABLED the trap.** #16 (`:1125`) says strict convention strings must be copied *"from a known-good artifact (a recent `Done/` plan, ...)"*. Plan 130 **was** known-good — and also **degenerate**: a single-step QA plan where the "count" and "step-number" readings of `qa_steps` coincide, so it could not teach the semantics. The Planner copied `qa_steps: 1` from it into plan 133, which then gated the DEV step as QA and skipped the real QA step's Rule 20/22 gates. **#16's own advice walked the Planner into the trap.** Known-good is necessary but NOT sufficient — the exemplar must also be semantically *distinguishable*. That refinement is uncodified anywhere (Planner-verified: zero hits for "degenerate", "copying a convention", "exemplar").

### Out of scope (deliberate)

- **The `plan_lint` qa_steps cross-check** — proposal 148's second clause. It is a **code** change to `bellows/scripts/plan_lint.py`, already tracked as its own baton thread. This plan codifies the discipline rule only; do NOT touch `plan_lint.py`.
- **The "never state a bare expected number" rule candidate.** Strong evidence (4/4 Planner-predicted numbers wrong across plans 203-207; all caught only by the paired verify clause). **CEO decision 2026-07-16: route it through the corpus** — LESSONS.md → cycle → Gate 1 → Gate 2 — **not** codified here. Gate 2 codifies what Gate 1 routed; it is not a side door for un-routed rules. The Planner adds the LESSONS.md entry separately. **Do NOT codify it in this plan.**
- **Baton corrections** (the stale v4.71 + two dead threads) are Planner-owned wrap work, not agent work.

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-gate-2-2026-07-16.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — DEV

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Developer. Read `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` first (cross-repo; skip with a note if absent). Commands run from `/Users/marklehn/Developer/GitHub/lessons-forge` unless a path says otherwise.
>
> **This step edits the GOVERNANCE ROOT by absolute path. It MUST NOT touch the canonical DB** (status transitions are Step 2) and **MUST NOT touch `plan_lint.py`**.
>
> **Scope:**
> - `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
> - `knowledge/development/gate-2-codification-2026-07-16.md`
>
> **Pre-edit verification — re-run each query BEFORE any edit.** (This plan codifies the re-verify-inherited-claims rule; it will not exempt itself from it. The line numbers below are Planner claims from 2026-07-16 and may have drifted.) If any output differs materially: **edit NOTHING**, set Output Receipt status to Partial, populate Flags with the mismatch evidence, and end the step.
>
> 1. **Claim:** live version is 4.73 — **Query:** `sed -n '5p' /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — **Expected:** `**Version:** 4.73`
> 2. **Claim:** Rule 51 is the highest Orchestration rule and ends with its Source footer — **Query:** `grep -n "^Source: proposal 138, lesson 2026-07-06" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — **Expected:** exactly ONE hit (~line 1013)
> 3. **Claim:** Checklist #16's Source line exists verbatim and exactly once — **Query:** `grep -c "^Source: proposal 114, lesson 2026-06-03; proposal 126, lesson 2026-06-07" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — **Expected:** `1`
> 4. **Claim:** qa_steps step-number semantics are ALREADY covered (the dedup basis for rejecting 148's first clause) — **Query:** `grep -c "listing the step numbers that are QA-gated" /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — **Expected:** `1`. **If this returns 0, HALT** — the whole 148 disposition rests on it.
>
> **Edit A — new Rule 52 (from proposal 147).** Insert immediately AFTER Rule 51's `Source: proposal 138, lesson 2026-07-06` footer and BEFORE the next `## ` section heading. Author it in the register of the surrounding rules (a `### 52. <title>` heading, a normative paragraph, a `**Why this rule exists:**` paragraph, and the Source footer). It must say, in your own prose:
> - **The normative rule:** any claim about the state of the world that is INHERITED from a generated artifact — classifier output, a Lessons Forge report, a baton/next-session file, a prior plan's findings, a PROJECT_STATUS entry — must be re-verified against ground truth (the filesystem, the live DB, the code, `git log`) **before it informs a disposition, a routing decision, or a plan's shape**. Generated artifacts describe the world as of their generation time; ground truth is the filesystem and the code.
> - **Its relationship to Rule 39 (state this explicitly):** Rule 39 protects an EDIT — the acting agent re-runs the SA's declared queries before editing. Rule 52 protects a DECISION — no edit need be involved. They are siblings covering different moments; neither subsumes the other. Cite Rule 39 by number.
> - **Why it exists** — all three 2026-07-16 instances from the CEO Context above: the three-week-stale FORGE_QA.md "does not exist" flag that nearly shaped a Gate 2 decision; the plan-205 classifier citing `_parse_session_limit_reset`, a **function that does not exist** (real: `_parse_session_reset`, `bellows/runner.py:36`); and the Planner's own baton refresh carrying two already-dead threads plus a two-version-stale template number, **one hour after authoring the verdict that flagged this same class of error**. Include that last detail — the rule exists because the failure does not spare someone who has just named it.
> - Footer: `Source: proposal 147, lesson 2026-07-07`
>
> **Edit B — refine Checklist #16 (from proposal 148, residue only).** In-place strengthen of `### 16. Copy strict convention strings from known-good artifacts` (~`:1125`). Add to its body — do NOT rewrite what is there — the refinement: **known-good is necessary but NOT sufficient; the exemplar must also be one where the convention's semantics are DISTINGUISHABLE.** Use the evidence: `qa_steps: 1` was copied from plan 130 — a genuinely known-good plan whose *only* step was its QA step, so the "count" and "step-number" readings coincide and the example cannot teach which one is meant. Copied into plan 133 it gated the DEV step as QA (Rule 20 banner demanded from a DEV deposit) and let the real QA step run with Rule 20/22 gates skipped. **The discipline: when an exemplar is degenerate for the convention you are copying, find a non-degenerate one or read the rule itself.** Extend the existing Source line to `Source: proposal 114, lesson 2026-06-03; proposal 126, lesson 2026-06-07; proposal 148, lesson 2026-07-07`. **Do NOT add a new qa_steps semantics rule** — `:407` already covers it (verified above); duplicating it is the failure this Gate rejected.
>
> **Edit C — version + changelog.** Set `**Version:** 4.74` and `**Last Updated:** 2026-07-16 (v4.74)` (lines ~5-6). Add ONE row to the TOP of the changelog table (it is newest-first — the current top row is the 2026-07-09 v4.73 row): `| 2026-07-16 | v4.74: Gate 2 ratification, 2026-07-16 cycle. ... |` summarizing both edits, and stating that proposal 148's qa_steps clause was **rejected as already-covered** (`:407`) with only its degenerate-exemplar residue codified into Checklist #16.
>
> **Occurrence-grep discipline:** these edits introduce no new convention string and rename nothing. Confirm that in the receipt. **Do NOT renumber any rule.**
>
> **DO NOT COMMIT the governance-root file** — `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` lives in the root repo; the Planner commits cross-repo at session wrap (plan-134 precedent). Commit ONLY your lessons-forge dev-log deposit.
>
> **Deposit:** `knowledge/development/gate-2-codification-2026-07-16.md` — the 4 pre-edit verification results verbatim, per-edit line ranges touched, the full text of Rule 52 as written, the #16 diff, version/changelog confirmation, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-2-codification-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — DEV (proposal status transitions)

---

> **Before starting, read the Step 1 deposit and confirm Output Receipt status Complete — if it is Partial, HALT** (a Partial means the template was not edited, so no status transition is honest). Post a short visible chat message confirming you are starting Step 2.
>
> You are the Forge Developer. Commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **All canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute.
>
> **This step changes the DB only. Do NOT touch `PLANNER_TEMPLATE.md`** (Step 1 owns it).
>
> **Scope:**
> - `knowledge/development/gate-2-status-transitions-2026-07-16.md`
>
> **Task A — transition the three proposals.** Gate 2 is where status moves (Gate 1 set routes only). Use direct SQL (there is no `set_proposal_status` API — verify that claim with `grep -n "def set_proposal" src/lessons_forge.py` before writing SQL; if such an API exists, USE IT instead and say so). Set `status_updated_at` to now and `status_updated_by='ceo'` (**the CHECK constraint allows only `planner`/`ceo`/`auto`** — do not invent a value):
> - **147** → `implemented` (Rule 52 is live in the template).
> - **148** → `implemented`. **Reasoning to record, because this one is subtle:** its *suggested_action's first clause* was rejected as already-covered, but a governance rule **derived from entry 140** (the Checklist #16 refinement) is now live. Proposals are the vehicle for their entry's disposition; recording 148 as `rejected` would make the corpus lie about where the #16 refinement came from. `implemented` is the honest status. Its `plan_lint` clause remains a separate live thread — note that, do not let it block the status.
> - **146** → `reference` (the plan-135 precedent: an honest terminal state for a proposal whose fix already shipped). Its route is already `reference` from Gate 1. **The `reference` status is legal** — plan 135 added it to the CHECK constraint; verify with `grep -n "reference" src/db.py` before writing.
>
> **Task B — prove the blast radius.** Capture the full status distribution BEFORE and AFTER. Expected AFTER: `implemented 99, superseded 28, rejected 15, stale 3, reference 3, proposed 0` — i.e. implemented 97→99, reference 2→3, proposed 3→0. **Verify rather than assume and report the ACTUAL numbers**; if they differ, report and explain rather than forcing them. Assert nothing outside {146,147,148} changed status. **Do NOT touch proposals 98/121/130** — CEO decision is they stay `stale`; confirm they did.
>
> **Task C — routes unchanged.** Confirm 146/147/148 still carry `reference`/`codify`/`codify`. Gate 2 moves status, not route.
>
> **Deposit:** `knowledge/development/gate-2-status-transitions-2026-07-16.md` — the API-vs-SQL check, before/after distributions, per-proposal read-back, 98/121/130 untouched confirmation, and an Output Receipt. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-2-status-transitions-2026-07-16.md`
>
> **STOP. Do NOT proceed to Step 3. Wait for CEO verdict.**

---
---

## STEP 3 — QA

---

> **Before starting, read the Step 1 and Step 2 deposits and confirm both Output Receipt statuses are Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 3 (QA).
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` for domain context (skip with a note if absent). Commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`. **Verification + reporting only — no product-code or template changes.** If you find a blocker, STOP and report it.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule + Rule 52's own discipline (this is the Gate that codified it — do not be its first violation).** Every SQL row states which DB it ran against; canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. Deposit **RAW command output**, never a summary. **Every identifier, line number, or file you assert must be grepped before you assert it** — the plan-205 classifier fabricated `_parse_session_limit_reset` while classifying the very lesson about unverified claims.
>
> **Scope:**
> - `knowledge/qa/gate-2-codification-qa-2026-07-16.md`
>
> Verification table, one row per claim, with a source column:
> 1. **Rule 52 is live** — present in `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`, numbered 52, carries `Source: proposal 147, lesson 2026-07-07`, and **explicitly cites Rule 39 and distinguishes edit-time from decision-time**. Quote the rule.
> 2. **Checklist #16 refined, not replaced** — the original known-good-artifact guidance survives, the degenerate-exemplar refinement is added, and the Source line now names proposals 114, 126, AND 148.
> 3. **No duplicate qa_steps rule was added (the rejected clause)** — `grep -c "listing the step numbers that are QA-gated"` still returns **1**, not 2. A second copy means Edit B overreached into the rejected clause: **FAIL**.
> 4. **Version + changelog** — `**Version:** 4.74`, `**Last Updated:** 2026-07-16 (v4.74)`, exactly ONE new changelog row at the TOP of the table, and the pre-existing v4.73/v4.72 rows intact below it.
> 5. **No renumbering** — Rules 1-51 and Checklist items 1-28 keep their numbers; only 52 is new. Confirm the highest rule is now 52 and the highest checklist item is still 28.
> 6. **Statuses transitioned** — 147=`implemented`, 148=`implemented`, 146=`reference`; distribution `implemented 99, superseded 28, rejected 15, stale 3, reference 3, proposed 0`. **`proposed` must be 0** — every proposal from the 2026-07-16 cycle is now dispositioned. Report actual numbers.
> 7. **Routes unchanged + 98/121/130 untouched** — 146/147/148 still `reference`/`codify`/`codify`; 98/121/130 still `stale`.
> 8. **Standing plan-204 regression watch** — proposal 145 still `implemented`; `get_unclassified_entries()` still `[]`; suite `python3 -m pytest src/ -v` still **55 passed** (`python3 -m pytest`, NOT the `timeout` binary — unavailable on macOS). This plan changes no code; a delta here means something else moved.
> 9. **Governance root NOT committed** — `git status --short` shows `PLANNER_TEMPLATE.md` as **modified but uncommitted** (the Planner commits cross-repo at wrap, per the plan-134 precedent). A committed template is a FAIL.
>
> If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/gate-2-codification-qa-2026-07-16.md` — verification table with source column, raw output, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (Gate 2 2026-07-16 complete: PLANNER_TEMPLATE v4.73→v4.74, Rule 52 codified from proposal 147, Checklist #16 refined from 148's residue with its qa_steps clause rejected as already-covered, proposals 146/147/148 dispositioned, `proposed` now 0 — the 2026-07-16 cycle is fully closed); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate-2-codification-qa-2026-07-16.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
