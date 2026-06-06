# Lessons Report — 2026-06-06


## Summary


| Category | Count |
|---|---|
| governance_rule | 8 |
| structural | 1 |

**Total proposals:** 9


## Governance Rule


### 2026-06-06: `pause_for_verdict` must be validated against the daemon's accepted enum before deposit [tag: planner-discipline, bellows-architecture]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: at plan authoring time, confirm pause_for_verdict is one of the three accepted tokens (always, after_step_1, after_qa_step) by copying from a known-good plan. For per-step gating use 'always'. Read the parsed value from gates._parse_plan_header output — it does NOT validate the enum.
- **Reasoning:** Entry documents a silent failure: 'An invalid value (this session: after_each_step) is silently treated as no-pause — the daemon ran a multi-step plan straight through to completion with no verdict gates.' The fix has both a structural aspect (parser should reject invalid values) and a governance aspect (Planner must validate at authoring time). Confidence is medium because the structural parser fix is arguably the more robust solution, but the entry frames the discipline as the primary action: 'at authoring time confirm pause_for_verdict is one of the three accepted tokens.'
- **Confidence:** medium

### 2026-06-06: Gate-enforced QA steps must be made unmissable in the prompt, not listed last [tag: planner-discipline, qa-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: any gate-enforced QA action (e.g. Rule 20 self-check) must have a MANDATORY callout at the TOP of the QA step that (a) names the gate, (b) quotes the byte-exact banner the gate looks for, (c) states the verification table does NOT satisfy it, and (d) ends with a self-grep so the agent cannot finish without it.
- **Reasoning:** Entry documents a concrete failure: 'the agent ran the other six [QA items], wrote a clean verification table, and skipped it — gate FAILED, plan halted, full re-dispatch.' The discipline is explicit: 'any gate-enforced QA action gets a MANDATORY callout at the TOP of the QA step.' This is a plan-authoring rule about how QA steps are structured in executables — squarely governance_rule. Tags 'planner-discipline, qa-discipline' confirm governance routing.
- **Confidence:** high

### 2026-06-06: Run the FULL test suite during DEV and Planner review — Bellows gates do not include suite-green [tag: planner-discipline, qa-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: DEV self-verify and Planner review must each run the full pytest suite to a pass/fail result and read the tail output. Never infer green from a collect count or target-file subset. Bellows gates do NOT include suite-green — it must be enforced by plan authoring.
- **Reasoning:** Entry documents a gap: 'The Bellows daemon gates... do NOT include pytest is green. A plan can close with failing tests if no one runs the suite.' The concrete failure was '5 red tests rode through a Gate Passed=True step.' The discipline is: 'DEV self-verify and Planner review must each run pytest tests/ to a pass/fail result and read the tail.' This is a governance rule about plan authoring and Planner review behavior. Tags 'planner-discipline, qa-discipline' confirm.
- **Confidence:** high

### 2026-06-06: Don't inherit the baton's framing — find root cause and downstream effects, cut what doesn't work [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when handed a proposed fix (baton, prior session, or own first instinct), verify it against the actual root cause and trace downstream effects before building. Prefer the cut that removes a failure class over the patch that suppresses one symptom.
- **Reasoning:** Entry prescribes a general Planner discipline: 'when handed a proposed fix... verify it against the actual root cause and trace downstream effects before building; prefer the cut that removes a failure class over the patch that suppresses one symptom.' Two concrete examples are cited — (1) auto-stash was a bandaid vs. replacing cherry-pick with git merge, (2) rebase would have reintroduced SHA divergence vs. --no-ff merge. This is a meta-level governance rule about how the Planner evaluates inherited solutions. Tag 'planner-discipline' confirms.
- **Confidence:** high

### 2026-06-03: Lessons Forge `run_full_lessons_cycle` returns every parsed entry in `needs_classification`, not the unclassified subset [tag: lessons-forge, planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: any consumer of run_full_lessons_cycle() must derive the classification work list from get_unclassified_entries(conn) — the stale-aware DB helper — not from the needs_classification field. Never loop needs_classification verbatim.
- **Reasoning:** Entry prescribes a discipline rule: 'any consumer of run_full_lessons_cycle().needs_classification MUST intersect it with the DB-authoritative unclassified set... Never loop needs_classification verbatim.' The over-reporting was latent — the 2026-05-18 cycle did not hit it because LESSONS.md had been fully rewritten. CRITICAL NOTE FOR GATE 2 CODIFICATION: the entry's prescribed DB query uses 'WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id=e.id)' which is the buggy non-stale-aware form. This query drops entries whose only proposal is 'stale' (the edit-requeue path). The correct implementation is now get_unclassified_entries(conn) in src/lessons_forge.py, which uses 'p.status != stale' in the NOT EXISTS clause. When this lesson is codified, the governance rule MUST reference the helper, not the buggy SQL from the entry text.
- **Confidence:** high

### 2026-06-03: Never re-dispatch a Bellows plan while local `main` carries uncommitted state — it trips the dirty-tree teardown pre-check [tag: planner-discipline, bellows-architecture]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before depositing or re-dispatching any Bellows-watched plan, ensure local main is clean — commit or stash all working-tree changes (modified tracked files AND untracked deposits/lifecycle artifacts). A stop→fix→re-dispatch loop must land the stopped run's substance before the re-dispatch.
- **Reasoning:** Entry explicitly states a discipline rule: 'before depositing or re-dispatching any Bellows-watched plan, ensure local main is clean.' The failure mode is documented — dirty-tree teardown pre-check (b2) refuses cherry-pick, stranding the worktree commit. Entry notes this 'generalizes the 2026-05-22 note from one file to the whole working tree' and is the 'operational mitigation for BACKLOG Gap 3 (dirty-tree teardown auto-stash) until that ships.' Tags 'planner-discipline, bellows-architecture' with the discipline being the load-bearing action item.
- **Confidence:** high

### 2026-05-29: Bellows `scope_check` gate cannot evaluate plans that delegate file lists to a referenced blueprint [tag: bellows-architecture, planner-discipline]


- **Suggested action:** Add interim discipline rule to PLANNER_TEMPLATE.md: when authoring SA→DEV→QA executables that delegate file enumeration to a blueprint, expect Step 2 to fail scope_check with a false positive; execute Rule 22(b) substance check against the blueprint and dev log to confirm alignment before issuing continue. Do not escalate to CEO when substance is sound.
- **Reasoning:** Entry documents a known false-positive pattern in Bellows' scope_check gate when plans delegate file lists to blueprints: 'The gate failure was a false positive. Every file DEV modified was explicitly specified in the blueprint.' Two structural fixes are queued as BACKLOG items (teach scope_check to follow references; require inline Target Files block). The entry's actionable discipline is an interim governance rule for Planner behavior: 'budget ~5 minutes of Planner time at Step 2 pause for walking the DEV-modified files against the blueprint sections.' Confidence is medium because the entry spans structural (Bellows code) and governance (interim discipline), but the structural fix is explicitly deferred.
- **Confidence:** medium

### 2026-05-27: Schema migrations shipped in `src/db.py` are not applied to production DB by code commit alone [tag: schema-discipline, forge-architecture]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when shipping a schema migration to a project with a committed runtime DB (forge.db, lessons-forge.db), the executable plan MUST include (a) code commit of the migration in src/db.py AND (b) a separate run-against-production step that applies init_db to the live DB, verifies the new table/column via PRAGMA table_info, and commits the modified DB file.
- **Reasoning:** Entry explicitly prescribes a discipline rule for migration-shipping plans: 'the executable plan that ships it must include an explicit python3 -c ... step against the production DB, with a PRAGMA table_info verification deposited as evidence.' The failure was structural (schema not applied), but the fix is a documentary governance rule about how plans are authored — not a code change. The entry frames this as a cross-project discipline (forge, anvil, lessons-forge) targeting plan authoring templates. Tags 'schema-discipline, forge-architecture' confirm governance-layer routing.
- **Confidence:** high

## Structural


### 2026-06-06: `__file__`-relative root constants break under git-worktree execution — resolve via marker walk-up [tag: bellows-architecture, planner-discipline]


- **Suggested action:** Replace __file__-relative root constants (GOVERNANCE_ROOT, BELLOWS_ROOT, ANVIL_ROOT) with a shared marker walk-up resolver that finds a stable marker file (e.g. COMPANY.md) by traversing parent directories. Audit all __file__-relative roots across bellows, forge, and anvil for worktree-reachability.
- **Reasoning:** Entry documents a recurring code-level failure: 'GOVERNANCE_ROOT = Path(__file__).parent.parent... point into .bellows-worktrees/<wt>/ when the module runs from a worktree — so resources at the real root are silently not found.' This is the 'third instance of the same worktree-root-confusion class.' The fix is mechanical/code-level: 'resolve repo/governance roots by walking up to a stable marker rather than counting .parent hops from __file__; prefer a single shared resolver over per-module constants.' This routes to Anvil/structural — a tooling code change, not a documentary rule edit.
- **Confidence:** high
