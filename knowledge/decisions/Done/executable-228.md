# Lessons Forge — Gate 2 Codification (cycle 2026-07-17): the Drafting Cycle + 4 rules → PLANNER_TEMPLATE v4.75
**Date:** 2026-07-18 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** none | **Execution:** Step 1 (SA) → Step 2 (DEV) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always

## CEO Context

Gate 2 of the 2026-07-17 cycle. Gate 1 closed 2026-07-18 (plan 227): six proposals (149–154) all routed `codify`. This plan codifies them as **FIVE edits** to governance-root `PLANNER_TEMPLATE.md` (live **v4.74**, the dedup baseline): one new named-process SECTION and four rule/checklist additions. **All six proposals → `implemented`; zero superseded, zero rejected** (150 and 152 are co-authors of one section — both implemented, neither supersedes the other).

**Integration-vs-record pass applied at authoring (dogfooding the rule this plan codifies):** the Planner grepped the live template for existing coverage of all six topics — ZERO hits. No dedup/supersede against live text (unlike v4.74, which rejected 148's already-covered clause). Insertion points confirmed: highest Rule = 52, highest Checklist = 28, no `## Drafting Cycle` section exists.

**⭐ CEO DECISION embedded (the Gate-1-reserved trigger criteria) — the Drafting Cycle is TIERED, not binary:**
- **Mandatory FLOOR — every diagnostic and executable:** before deposit, run the **integration-vs-record pass** — scan the drafted plan against LESSONS.md, `knowledge/decisions/Done/`, `knowledge/research/`, and the actual code for precedent conflicts, convention violations, and the "is this actually trivial?" check. Confirms clean → deposit. Surfaces entanglement or non-trivial blast radius → ESCALATE.
- **ESCALATE to the full four-pass cycle** when the floor pass surfaces entanglement, OR the plan is inherently high-stakes: production-data mutation, a CEO-run tool, a money-affecting write path, or a cross-machine / irreversible action.
- **The full cycle** = draft OFF-QUEUE (outside `decisions/`; deposit = dispatch) → the four named lenses, each a distinct pass (1: weak-spots — correctness/safety of the plan itself; 2: destruction/mitigating-rewrites — harm to existing functionality + agent watering-down; 3: vulnerabilities — adversarial/degenerate conditions; 4: integration-vs-record — against the corpus) → fold ALL accepted findings → repeat until a pass honestly reports **diminishing returns** → fold-and-deposit exactly once.

**Rationale to preserve in the section (CEO reasoning, 2026-07-18):** trivial-looking plans have repeatedly caused retroactive fixes because no analysis preceded them; the floor pass makes analysis universal without four heavy passes on a one-liner, and preserves the cycle's own diminishing-returns stop signal (which mandatory-max would contradict). The drafting cycle hardens the PLAN; Planner verification at the verdict gate hardens the DELIVERABLE (the 216→217 boundary — cite it).

**Gate 2 is itself a governance edit with NO test suite — Planner verification IS the safety net (Test Scope: none).** SA blueprints exact insertion text; DEV applies verbatim; QA verifies structure. PLANNER_TEMPLATE lives in the governance ROOT (not this repo) — the DEV edits it in place; it stays UNCOMMITTED (the Planner commits it cross-repo at wrap, plan-134/208 precedent). Statuses transition on the CANONICAL lessons-forge DB via `set_proposal_status` semantics.

**Deposit-once discipline:** deposited exactly once.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-gate-2-2026-07-18.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — SA (Solution Architect)

---

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Solution Architect. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`; the target file is the governance-root `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (READ-ONLY this step — you blueprint, DEV applies). Read the six proposals' `suggested_action` and `reasoning` VERBATIM from canonical (`sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT id, suggested_action, reasoning FROM lesson_proposals WHERE id BETWEEN 149 AND 154"`) and the SOURCE lesson bodies from `/Users/marklehn/Developer/GitHub/LESSONS.md` (entries 141–146). Read the live template to fix exact anchors and match prose register.
>
> **Scope:**
> - `knowledge/development/gate-2-blueprint-2026-07-17.md`
>
> **Blueprint the FIVE edits — exact insertion text + exact anchor (the line to insert after), each dedup-checked against the live template:**
> 1. **New section `## The Drafting Cycle`** — placement: the plan-authoring-process cluster, AFTER `## Quick Fix Protocol` and BEFORE `## Output Format` (~line 314). Content: the TIERED trigger (floor / escalate / full-cycle) exactly as CEO Context specifies; the four named lenses with their one-line scopes; off-queue drafting (deposit = dispatch); fold-all-then-repeat; the diminishing-returns stop signal; deposit-once; the CEO rationale (trivial-bites-later) and the plan-hardens / verdict-gate-hardens-deliverable distinction. Cite the production evidence: plan 224 (first full four-lens cycle, first-dispatch clean) and the 216→217 boundary. Source: proposals 150 + 152 (both implemented — the section IS both).
> 2. **New Rule 53 (Orchestration Plan Rules, after Rule 52)** — region-scoped metrics: any semantically-scoped metric (region, carrier, contract, config, time-window) must be computed with that scope applied END TO END — every aggregate in the chain, not just the final comparison; a single unscoped aggregate silently converts "this entity's value" into "everyone's" and the verdict inherits the error; when two tools disagree, the scope-carrying one is authority. Source: proposal 153. Sibling framing to Rule 52.
> 3. **New Checklist #29 (Plan Authoring Checklist, after #28)** — never state a bare expected number in plan text: pair every prediction with a verify-and-explain clause ("verify and report actual, never force"); where the number gates a destructive step, name the catastrophic signature too. Source: proposal 149.
> 4. **New Checklist #30** — schema/migration QA rows: a worktree QA step CANNOT verify a live-DB migration against an untracked canonical DB (it fresh-builds and reports 19); schema-bump QA rows must name the ABSOLUTE canonical path and show PRE- and POST-migration version (a fresh build cannot show the pre-version — that asymmetry is the tell); the Planner verifies canonical by absolute path at the verdict gate BEFORE composing the verdict; activation is PENDING per machine until each app restart. Source: proposal 151.
> 5. **New Checklist #31** — schema-version bumps: any plan bumping `CURRENT_SCHEMA_VERSION` must, in the SAME DEV step, grep for every version-pinned assertion, enumerate them in plan text before dispatch, classify each as tripwire (update) vs migration-precondition (PRESERVE), and re-grep after editing. Source: proposal 154.
>
> Also blueprint: version bump `4.74 → 4.75`; ONE new changelog row at the TOP of the changelog table naming all five edits and the six→implemented mapping; confirm NO renumbering of existing rules/checklist items (new items are 53 / 29 / 30 / 31).
>
> **Deposit:** `knowledge/development/gate-2-blueprint-2026-07-17.md` — for each of the 5 edits: the exact insertion text (ready to paste), the exact anchor line, and the dedup note (what you grepped, zero hits). Plus the version/changelog text and the status-transition list (all six → implemented). Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-2-blueprint-2026-07-17.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — DEV

---

> **Before starting, read the Step 1 blueprint and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2.
>
> You are the Forge Developer. Apply the Step-1 blueprint to `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (governance root) VERBATIM — you are a faithful applicator, not a re-author; if the blueprint and live template disagree on an anchor, halt and report rather than improvise. Then transition the six proposals' status on the canonical lessons-forge DB.
>
> **Scope:**
> - `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (edit in place; leave UNCOMMITTED — the Planner commits at wrap)
> - `knowledge/development/gate-2-codification-dev-2026-07-18.md`
>
> **Task A — apply the 5 edits** from the blueprint: the new `## The Drafting Cycle` section at its anchor; Rule 53; Checklist #29/#30/#31; version `4.74 → 4.75` (both header lines); one new changelog row at the top. NO renumbering of existing items. NO edits beyond the blueprint.
>
> **Task B — status transitions on canonical** (`/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`, absolute path): set proposals 149, 150, 151, 152, 153, 154 to `status='implemented'` (`status_updated_by='ceo'`, `status_updated_at=now`). Verify: all six `implemented`, routes still `codify`, and the full status distribution moved exactly `proposed 6 → 0`, `implemented 99 → 105` (verify and report actual; on any other delta, halt).
>
> **Deposit:** `knowledge/development/gate-2-codification-dev-2026-07-18.md` — the applied-edit confirmation (grep each new anchor: `## The Drafting Cycle`, `### 53.`, `### 29.`/`### 30.`/`### 31.`, `v4.75`), the before/after proposal-status distribution, and an Output Receipt. Canonical Python file-write pattern — no heredoc. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
> - `lessons-forge/knowledge/development/gate-2-codification-dev-2026-07-18.md`
>
> **STOP. Do NOT proceed to Step 3. Wait for CEO verdict.**

---
---

## STEP 3 — QA

---

> **Before starting, read the Step 2 deposit and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 3 (QA).
>
> You are Lessons Forge QA. **Verification + reporting only — no edits.** Do NOT use the Monitor tool.
>
> **Rule 20 self-check is gate-enforced.** Your deposit MUST contain, verbatim, `## Rule 20 — QA Self-Check Results` and a line reading exactly `**PASSED — SELF-CHECK PASSED**`; end with a self-grep confirming it.
>
> **Evidence-source rule:** every DB row states its DB; canonical reads via `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. RAW output only.
>
> **Scope:**
> - `knowledge/qa/gate-2-codification-qa-2026-07-18.md`
>
> Verification table, one row per claim: (1) version is `4.75` on both header lines of `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`; (2) the new `## The Drafting Cycle` section exists, contains the TIERED trigger (floor / escalate / full-cycle), the four named lenses, and the diminishing-returns stop — quote the trigger paragraph; (3) Rule 53 present and is region-scoped-metrics; Checklist #29 (bare-number), #30 (schema/migration QA rows), #31 (schema version pins) present; (4) NO renumbering — the pre-existing highest Rule was 52 and highest Checklist 28; confirm existing items unchanged and new items are exactly 53/29/30/31; (5) exactly ONE new changelog row, at the top, naming the five edits; v4.73/v4.72 rows intact beneath; (6) canonical statuses: proposals 149–154 all `implemented` with route `codify`; distribution `implemented 105, proposed 0, superseded 28, rejected 15, stale 3, reference 3` (verify actual, quote raw); (7) **the template is MODIFIED but UNCOMMITTED** in the governance root (`git status --short PLANNER_TEMPLATE.md` shows ` M`) — a committed template is a FAIL (cross-repo commit is the Planner's at wrap). Any failing row: report and halt.
>
> **Deposit:** `knowledge/qa/gate-2-codification-qa-2026-07-18.md` — the table with raw evidence, Rule 20 banner + PASSED line, Output Receipt. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (Gate 2 2026-07-17 complete: PLANNER_TEMPLATE v4.75 — the Drafting Cycle codified as a tiered named process + Rule 53 + Checklist 29/30/31; six proposals implemented; `proposed` now 0; the drafting cycle is standing governance); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate-2-codification-qa-2026-07-18.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
