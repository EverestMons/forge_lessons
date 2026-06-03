# Lessons Report — 2026-06-03


## Summary


| Category | Count |
|---|---|
| governance_rule | 21 |
| narrative | 2 |

**Total proposals:** 23


## Governance Rule


### 2026-06-02: "Known-good" plan headers have a freshness axis — a header that parsed months ago can predate a current gate  [tag: planner-discipline] [tag: plan-authoring] [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: verify every new plan header with gates._parse_plan_header against the current parser before deposit; never certify a header by pattern-matching old Done/ artifacts.
- **Reasoning:** Entry explicitly proposes a freshness-axis discipline: 'Validity is on a *freshness* axis, not a familiarity axis. Verify every new plan header with gates._parse_plan_header against the **current** parser before deposit; never certify a header by visual resemblance to Done/ examples.' This is a documentary rule change for plan authoring.
- **Confidence:** high

### 2026-06-02: Never edit a project's working tree while a Bellows plan is in-flight for that project — even a blueprint or knowledge file  [tag: planner-discipline] [tag: bellows-integration] [tag: worktree]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md Bellows Operational Workarounds: defer ALL working-tree edits (source, blueprints, knowledge deposits) until no plan is in-flight for that project.
- **Reasoning:** Entry documents dual damage from mid-flight edits: '(1) the uncommitted change trips _teardown_worktree dirty-tree pre-check (worktree_teardown_dirty_tree), so the plan cannot complete teardown; AND (2) the edit lands on local main, never reaching the step detached-HEAD worktree, so the in-flight agent never sees it.' The fix is a Planner discipline rule, not a tooling change.
- **Confidence:** high

### 2026-06-02: A QA "full suite passes / N passing" headline is the least independently-verifiable claim in a report — confirm the run was watched or reproduce it under a wall-clock bound  [tag: planner-discipline] [tag: rule-22] [tag: qa-verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md QA verification: substance-check feature assertions individually via Rule 22; never accept a full-suite pass-count headline as independent verification.
- **Reasoning:** Entry documents that 'a full-suite pass-count rests on a single long run nobody observed and cannot be reconstructed from the report' — a hung-then-killed and a slow-then-completed run produce the same headline. The lesson proposes verifying feature assertions individually rather than trusting aggregate counts.
- **Confidence:** high

### 2026-06-02: `pytest --timeout=N` bounds per-test execution only — it cannot catch collection/import or session-fixture hangs  [tag: planner-discipline] [tag: testing] [tag: diagnostic-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md testing discipline: use a wall-clock bound external to pytest (shell timeout) plus --collect-only for collection-time isolation; pytest --timeout=N only bounds per-test execution.
- **Reasoning:** Entry documents that 'pytest-timeout --timeout=N arms a timer per test item' and cannot catch '(1) hangs during collection/import, (2) session/module-scoped fixture setup hangs, or (3) C-level or non-main-thread blocking.' The fix is a documentary rule specifying wall-clock bounds and --collect-only as standard testing practice.
- **Confidence:** high

### 2026-06-01: Name deposit file paths literally in plan step bodies — scope_check authorizes from named paths; the "don't name from memory" rule is about assertions, not deposit targets  [tag: planner-discipline] [tag: plan-authoring] [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md plan authoring: name all deposit file paths literally in plan step bodies — scope_check authorizes from named paths, not inferred ones.
- **Reasoning:** Entry documents that 'scope_check authorizes a step file modifications from the literal file paths named in that step body' and provides a reproduction where indirect reference ('add to the test module that covers _consume_verdicts ... locate it via grep') caused a scope_check FAIL despite DEV modifying the correct file.
- **Confidence:** high

### 2026-05-31: Read the verdict-request Gate Result JSON before every verdict — the `gates step N: passed=True` log line predates teardown  [tag: bellows-integration] [tag: planner-discipline] [tag: verdict-mechanics]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md verdict mechanics: read the verdict-request Gate Result JSON and Pause Reason Code before issuing any verdict — the terminal log line predates teardown and misses post-log failures.
- **Reasoning:** Entry documents that 'the daemon emits gates step N: passed=True, failures=0 in run_plan BEFORE it calls _teardown_worktree' and teardown failures are 'INVISIBLE in the terminal log — it surfaces only in the verdict-request Gate Result JSON.' Clear documentary rule for Planner verdict discipline.
- **Confidence:** high

### 2026-05-31: Never leave stray uncommitted non-lifecycle files in a watched repo root — they fail every teardown  [tag: bellows-integration] [tag: planner-discipline] [tag: operational-recovery]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md Bellows operational discipline: keep watched repo roots clean of uncommitted non-lifecycle files between plans; commit or remove stray files before depositing new plans.
- **Reasoning:** Entry documents that '_teardown_worktree step (b2) runs a dirty-tree pre-check on local main and raises worktree_teardown_dirty_tree if any uncommitted file is NOT a Bellows lifecycle artifact.' Stray files 'block the cherry-pick on EVERY plan teardown until committed or removed.' Clear Planner discipline rule.
- **Confidence:** high

### 2026-05-29: Restarting the daemon mid-plan arms the (n) orphan-guard verdict-replay — archive prior processed verdicts before the terminal verdict  [tag: bellows-integration] [tag: operational-recovery] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md Bellows operational workaround: before depositing the terminal verdict after a daemon restart, archive prior processed-verdict files from verdicts/resolved/ to prevent orphan-guard (n) verdict-replay loops.
- **Reasoning:** Entry documents that restarting the daemon mid-plan 'arms the (n) orphan-guard verdict-replay' because 'the fresh daemon orphan-guard pre-scan can renormalize the step-(N-1) verdict back to canonical, re-consume it as a fresh continue, and re-dispatch step N in a ~2-minute loop.' This is a Planner-side workaround for a known daemon bug (BACKLOG item n); root fix is daemon-side.
- **Confidence:** medium

### 2026-05-29: Never name specific tests, files, or values from session memory in plan body assertions — soften to count-or-shape or copy from artifact  [tag: planner-discipline] [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md plan authoring: never name specific tests, files, or values from session memory in plan body assertions — soften to count-or-shape predicates or copy verbatim from a fresh artifact read.
- **Reasoning:** Entry documents that 'the Planner sometimes names specific test names, file paths, line numbers, or fixed-value counts inside an assertion' from session memory, causing failures 'not because substance broke, but because the Planner mis-quoted the artifact.' Provides a same-day reproduction where a test name was mis-quoted.
- **Confidence:** high

### 2026-05-29: Planner-side writes to project directories during in-flight Bellows dispatch create dirty-tree teardown failures  [tag: planner-discipline] [tag: bellows-integration] [tag: operational-recovery]


- **Suggested action:** Strengthen existing PLANNER_TEMPLATE.md rule on no-writes-during-dispatch: quantify recovery cost (~5-10 min per dirty-tree cycle) and extend to all project directory writes, not just source edits.
- **Reasoning:** Entry documents that 'Any write to a [project] directory between depositing a Bellows-dispatched executable and that executable plan file reaching Done/ creates uncommitted state on local main that blocks Bellows worktree teardown cherry-pick.' Closely related to entry 95 (same root discipline); this entry adds recovery-cost data and broader scope (any directory write, not just source). Potential consolidation candidate with entry 95.
- **Confidence:** medium

### 2026-05-29: SA blueprints that add a value to a recognized-set must verify all downstream consumers handle the new value [tag: sa-discipline, blueprint-completeness]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md SA discipline: blueprints that add a value to a recognized-set must verify all downstream consumers (branches, validators, lookup functions) handle the new value.
- **Reasoning:** Entry documents that an SA blueprint 'added same_week to the validator _RECOGNIZED_TIMING_RULES set' and 'specified the verbatim insertion code for the new branch' but 'did NOT specify: _find_eia_price in the same file had a separate elif timing_rule in (ship_week, current) branch that performs the actual EIA lookup logic.' A clear SA discipline rule requiring downstream consumer verification.
- **Confidence:** high

### 2026-05-29: Bellows `scope_check` gate cannot evaluate plans that delegate file lists to a referenced blueprint [tag: bellows-architecture, planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md plan authoring: inline target file paths in DEV step bodies rather than delegating to a referenced blueprint — scope_check cannot follow cross-step blueprint references.
- **Reasoning:** Entry documents that scope_check 'failed with out-of-scope files listing every file DEV had touched' because 'the Step 2 header line plus the first ~80 characters of the body' was the gate's plan step context and did not include the blueprint's file list. Root cause is a daemon architecture limitation; the Planner-side fix is inlining file paths. Related to entry 98 (same scope_check path-naming discipline).
- **Confidence:** medium

### 2026-05-28: Verdict response directory — `resolved/`, full stop  [tag: bellows-integration] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md verdict mechanics: always write verdict response files to verdicts/resolved/ — no other directory is consumed by Bellows.
- **Reasoning:** Entry documents a mid-session error: 'I misread [a benign WARN] as directory wrong and wrote my next verdict to pending/. Bellows shipped a clarifying WARN immediately: verdict file in wrong directory — expected location: verdicts/resolved/ — file will be silently ignored.' Clear documentary rule specifying the canonical verdict directory.
- **Confidence:** high

### 2026-05-28: `scope_check` false-positive on plan-required evidence files — Planner override is the right disposition  [tag: bellows-integration] [tag: gate-overrides] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md gate overrides: scope_check false-positives on collectively-referenced evidence files in plan Deposits blocks warrant Planner override per Rule 22(d).
- **Reasoning:** Entry documents that 'scope_check passed full-suite.txt and flagged the 5 others as out-of-scope' even though 'The plan literally instructed those exact deposits at those exact paths' via collective reference. The Planner override (not a daemon fix) is identified as 'the right disposition.'
- **Confidence:** high

### 2026-05-28: `_seen` slug cache not cleared on Done/ transition — diagnostic→executable handoff at same slug requires rename workaround  [tag: bellows-integration] [tag: recovery] [tag: slug-collision]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md Bellows operational workaround: when depositing a follow-on plan at the same slug as a just-completed plan, use a distinct slug variant (e.g., -v2-) to evade the _seen slug cache.
- **Reasoning:** Entry documents that '_seen slug cache not cleared on Done/ transition' causes Bellows to ignore fresh plans at the same slug: 'Bellows logged heartbeat: idle for 4+ minutes and never claimed the new file.' This is a Planner-side workaround for a daemon bug (_seen cache invalidation); the root fix is daemon-side.
- **Confidence:** medium

### 2026-05-28: R2 sub-variant Planner-direct close is the working recovery shape for "substance shipped, teardown cherry-pick conflicts on lifecycle artifacts" — two sessions running  [tag: bellows-integration] [tag: recovery] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md recovery procedures: document R2 Planner-direct close as the standard recovery shape for 'substance shipped, teardown cherry-pick conflicts on lifecycle artifacts' — two sessions confirm the pattern is mechanical and reliable.
- **Reasoning:** Entry promotes the R2 recovery to documented pattern: 'Sessions 13 and 14 both encountered the same shape of teardown failure on consecutive sessions, on different plans, and the same recovery pattern closed both cleanly.' The fix is a documented recovery procedure in governance, not a tooling change.
- **Confidence:** high

### 2026-05-28: Strict Bellows convention strings must be copied from a known-good artifact, never authored from memory — three failures in one session  [tag: planner-discipline] [tag: plan-authoring] [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md plan authoring: strict Bellows convention strings (header fields, dispatch modes, directory names) must be copied verbatim from a known-good artifact, never authored from memory.
- **Reasoning:** Entry documents three failures in one session sharing one root cause: 'I specified a strict, machine-checked Bellows convention string from memory rather than copying it verbatim from a verified artifact.' Cites plan header field-line position, dispatch mode, and directory name failures. Clear documentary rule for plan authoring.
- **Confidence:** high

### 2026-05-27: R2 recovery shape for worktree teardown cherry-pick conflict on agent's own claim-rename — second occurrence in 5 days, recovery is mechanical  [tag: bellows-integration] [tag: planner-discipline] [tag: operational-recovery]


- **Suggested action:** Strengthen PLANNER_TEMPLATE.md R2 recovery procedure: document the agent claim-rename variant where the cherry-pick conflict is on the agent's own in-progress- rename rather than a Planner edit.
- **Reasoning:** Entry documents 'second occurrence in 5 days' of R2 recovery for worktree teardown cherry-pick conflict, specifically when 'the local main working tree has uncommitted state that would be overwritten by the merge — most commonly a transient lifecycle artifact (the agent own claim-rename of executable-* to in-progress-*).' Closely related to entry 108 (same R2 recovery shape); this entry adds the claim-rename variant. Potential consolidation candidate with entry 108.
- **Confidence:** medium

### 2026-05-27: `Dispatch Mode: standard` rejection — Planner authoring relies on memory rather than mechanized check despite Rule 35 + Plan Authoring Checklist item 3 coverage  [tag: planner-discipline] [tag: plan-authoring] [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md plan authoring: mechanize dispatch-mode validation by copying the field from a known-good Done/ artifact or running the validator, rather than relying on memory recall of allowed values.
- **Reasoning:** Entry documents that despite 'Rule 35 + Plan Authoring Checklist item 3 coverage,' the Planner still authored 'Dispatch Mode: standard' from memory. 'Four prior rejections across three days documented before this session.' The lesson is that existing governance is insufficient when relying on recall — the fix must mechanize the check.
- **Confidence:** high

### 2026-05-27: Gate 1 routing rule — medium-confidence proposals flagged as "Planner-side workaround for daemon bug" should be rejected and routed to Bellows BACKLOG rather than codified as PLANNER_TEMPLATE governance  [tag: planner-discipline] [tag: lessons-forge] [tag: gate-1-routing]


- **Suggested action:** Add Gate 1 routing rule to PLANNER_TEMPLATE.md: reject medium-confidence proposals flagged as 'Planner-side workaround for daemon bug' and route the underlying bug to Bellows BACKLOG rather than codifying workarounds as governance.
- **Reasoning:** Entry explicitly proposes a routing rule: 'two of the 3 medium-confidence proposals were flagged in classification as Planner-side workaround for daemon bug. Both proposed adding a Planner discipline rule to PLANNER_TEMPLATE that would mitigate a known daemon-side bug.' CEO disposition was reject + route to BACKLOG. Clear governance rule for Gate 1 review process.
- **Confidence:** high

### 2026-05-27: Non-monotonic STEP header labels in Bellows-dispatched plans cause positional/literal misalignment between daemon dispatch and agent prompt lookup  [tag: planner-discipline] [tag: plan-authoring] [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md plan authoring: use strictly monotonic integer STEP header labels (1, 2, 3...) — Bellows step parser is positional; non-monotonic labels (2A, 2B) cause dispatch/prompt misalignment.
- **Reasoning:** Entry documents that 'Bellows step parser is positional and 1-indexed: each ## STEP N — header becomes daemon-step 1, 2, 3, 4 regardless of the label content' and that non-monotonic labels 'caused the agent to run the wrong step body.' Clear plan authoring discipline rule.
- **Confidence:** high

## Narrative


### 2026-05-28: Wall-clock calibration — "small-tier" executables with comprehensive test coverage run closer to medium-tier  [tag: planning-calibration] [tag: bellows-integration]


- **Suggested action:** Archive as context — wall-clock calibration data showing small-tier executables with comprehensive test coverage run closer to medium-tier (~72 min agent runtime).
- **Reasoning:** Entry provides observational wall-clock data: 'Diagnostic Step 1: 11m 51s, Executable Step 1: 40m 28s, Executable Step 2: 20m 06s, Total agent runtime: ~72 minutes.' The entry describes timing reality without proposing a specific documentary rule change — it implies planners should 're-tier' but does not prescribe a concrete fix to PLANNER_TEMPLATE or other governance file.
- **Confidence:** medium

### 2026-05-27: Verdict-response filename prefix tolerance — Bellows consumed verdicts with unstripped `diagnostic-` and `executable-` prefixes despite README specifying prefix strip  [tag: bellows-integration] [tag: documentation-drift]


- **Suggested action:** Archive as context — Bellows tolerates verdict-response filenames with unstripped diagnostic-/executable- prefixes despite README specifying prefix strip; documentation drift between spec and implementation.
- **Reasoning:** Entry observes that 'Both were consumed correctly by Bellows. Plans auto-moved to Done/ on continue-verdict consumption. No unmatched verdict errors.' This is documentation drift — the README says one thing, Bellows does another, but both work. No specific PLANNER_TEMPLATE action is proposed; the observation is about Bellows internal documentation accuracy.
- **Confidence:** medium
