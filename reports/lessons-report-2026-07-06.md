# Lessons Report — 2026-07-06


## Summary


| Category | Count |
|---|---|
| governance_rule | 12 |
| instrumentation | 1 |
| structural | 2 |

**Total proposals:** 15


## Governance Rule


### 2026-07-06: QA substituted evidence source without disclosure — absolute-path URI makes "worktree has no DB" a non-reason [tag: qa-discipline]


- **Suggested action:** Add rule to QA specialist files: the canonical DB path is an absolute-path URI that works from any worktree — worktree DB absence is never a substitution reason. If a QA action cannot be performed as specified, report that fact rather than silently swapping evidence and marking PASS.
- **Reasoning:** Entry describes plan 128 QA silently substituting a fresh-init_db() throwaway PRAGMA for the canonical-DB check, presenting it as canonical evidence. Concludes: "canonical path is an absolute-path URI that resolves from any worktree, so worktree absence is not a reason to substitute evidence sources." This is a documentary rule for QA agent governance.
- **Confidence:** high

### 2026-07-06: DB-out-of-git projects need an evidence-source contract in QA steps — per-row DB-source statement [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: QA steps verifying state in a DB-out-of-git project must carry an evidence-source contract — specify the canonical absolute path, state that worktree absence is not a substitution reason, and require each verification row to declare its DB source.
- **Reasoning:** Entry describes plan 128 assuming "against the canonical lessons-forge.db" was sufficient instruction but QA still substituted. Correction plan 130 added explicit evidence-source rules and the report was clean. Concludes: "any QA step verifying state in a DB-out-of-git project must carry the evidence-source contract." Candidate for Plan Authoring Checklist codification. Documentary rule.
- **Confidence:** high

### 2026-06-14: Scope test files generously [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when scoping test files, include every test file the change might plausibly touch (tests/test_<each-touched-module>.py) or pre-authorize tests/ with "only if needed" guidance — a wider conditional list costs nothing while a narrow list forces a halt-or-violate dilemma.
- **Reasoning:** Entry describes a plan naming specific test files in scope causing a scope_check trip when the DEV added a relevant test in an unlisted file (plan 62: tests/test_runner.py). Concludes with a plan-authoring rule about generous test-file scoping. Documentary rule for PLANNER_TEMPLATE.
- **Confidence:** high

### 2026-06-12: Generator-run verification produces files [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a plan step instructs running a generator/builder as verification, declare the generator output files in that step Deposits or scope — enumerate outputs at authoring time by asking "what does this command write to disk?"
- **Reasoning:** Entry describes plan 10 QA step running a generator for verification but the plan never declaring the generated output files, causing scope_check gate failure on otherwise-green QA. The discipline rule is explicitly about plan authoring — declaring generator outputs at authoring time.
- **Confidence:** high

### 2026-06-12: Verdict disposition text does not reach the resumed step [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: corrections discovered at verdict time go into plan text (follow-up plan or edit before resume), never into verdict disposition prose — disposition text is a record for humans and the ledger, not an instruction channel.
- **Reasoning:** Entry describes a verdict rider instruction ("fix the path in FORGE_QA.md") that went unexecuted because verdict files are consumed mechanically and prose is not forwarded to the next step's prompt. Explicitly states the discipline rule as a plan-authoring constraint.
- **Confidence:** high

### 2026-06-12: Gates do not enforce step composition — Position A lives in the Planner's checklist  [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: plan authoring must check step composition against Position A explicitly — every executable plan requires at least one QA step with a separate agent from the build step; single-step doc plans are not a permitted shape.
- **Reasoning:** Entry describes two single-step doc plans shipping without QA steps, violating Position A codification. No gate fires on step composition. Explicitly states: "plan authoring must check step composition against Position A explicitly." Documentary rule for plan structure.
- **Confidence:** high

### 2026-06-11: Scope enumerations must include the test-infrastructure files implied by new module-level state [tag: planner-discipline, bellows-architecture]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a step introduces module-level state (paths, singletons, DB connections), the scope enumeration must include test-infrastructure files (conftest.py, fixtures) that isolate that state — include tests/ with conditional guidance rather than a narrow test-file list.
- **Reasoning:** Entry describes scope_check failure because DEV edited tests/conftest.py — outside the hand-typed allowed-file list — to add a necessary isolation fixture for a new module-level path constant. Concludes: "scope guidance costs nothing, while a narrow list that forces the agent to choose between halting and violating scope costs a full rework cycle." Documentary rule for scope enumeration.
- **Confidence:** high

### 2026-06-11: Don't paraphrase a referenced design artifact's technical specifics inline — the paraphrase becomes the instruction [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when referencing a design artifact (blueprint, ADR), cite the artifact section without paraphrasing its technical specifics inline — pair the verbatim mandate with a QA conformance check against the artifact so deviation is caught mechanically.
- **Reasoning:** Entry describes DDL deviation because plan text paraphrased blueprint columns inline in composite-key style while referencing the blueprint's surrogate-key design. Agent followed the concrete inline enumeration over the referenced artifact. Concludes: "Any divergent paraphrase will contradict [the artifact] and will win when it does." Documentary rule for plan authoring.
- **Confidence:** high

### 2026-06-11: Convention redefinition requires occurrence-grep, not site enumeration [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when redefining a convention (renaming, reformatting), the DEV step must grep for all occurrences rather than relying on a Planner-enumerated site list; the QA step must re-run the same grep expecting zero unclassified hits.
- **Reasoning:** Entry describes plan 4 (v4.61 codification) enumerating three edit sites from structural reading but QA finding a fourth — an embedded copy carrying the same string. Concludes: "Structural enumeration of the places that define X predictably misses the places that quote X." Documentary rule for convention-change plans.
- **Confidence:** high

### 2026-06-09: Never gate a behavior-preservation regression on a composite/score hash when scoring is time-dependent [tag: planner-discipline, anvil]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: regression gates must identify time-dependent inputs in the scoring/computation path and use tolerance-based or snapshot-frozen comparisons instead of byte-identical hashes when time sensitivity is present.
- **Reasoning:** Entry describes BP2 declaring a byte-identical regression gate on scores computed with datetime.now() decay windows — unsatisfiable on recompute. States the fix: "snapshot the pre-migration stored values, freeze time or use tolerance, then compare." This is a plan-authoring rule about how to define regression gates.
- **Confidence:** high

### 2026-06-09: Derive the DEV step's allowed-file set from the SA's consumer grep, not a hand-typed expected list [tag: planner-discipline, bellows-architecture]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: DEV step allowed-file sets must reference the SA consumer grep output ("scope includes exactly the files enumerated in SA Section N"), not a hand-typed list — a divergent hand-typed list is a guaranteed scope_check false-positive.
- **Reasoning:** Entry describes BP2 DEV step tripping scope_check on 6 legitimate files because the Planner hand-typed an expected set omitting files the SA grep had identified. Concludes: the DEV step should say "scope includes exactly the files enumerated in SA Section N" with no competing list. Documentary rule for plan authoring.
- **Confidence:** high

### 2026-06-06: Don't inherit the baton's framing — find root cause and downstream effects, cut what doesn't work [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when inheriting a baton or prior-session framing, independently trace the root cause and downstream effects before adopting the proposed fix — prefer the cut that eliminates a failure class over the patch that suppresses one symptom.
- **Reasoning:** Entry explicitly describes two cases where rejecting inherited framing led to better outcomes: (1) baton framed teardown as "add auto-stash" but root-cause tracing revealed git merge dissolved the entire failure class; (2) rebase instinct was cut for cherry-pick when tracing showed rebase would leave detached HEAD. Concludes with a planner rule: "trace against the actual root cause and trace downstream effects before building." This is a documentary rule for plan authoring.
- **Confidence:** high

## Instrumentation


### 2026-06-14: Live-canary every daemon-write activation; green tests are not enough [tag: process-discipline]


- **Suggested action:** Add mandatory post-activation live canary step for any silent/best-effort daemon write path: emit via channel, then verify the daemon actually wrote the expected output to DB/file.
- **Reasoning:** Entry describes how lifecycle/ledger writes are log-and-continue (silent on failure), and only live canaries caught THREE distinct bugs the full green suite missed. The fix is a new procedural safeguard — a canary verification step added to the daemon activation workflow, not a code change or documentary rule. "Green tests verify the code path exists; a canary verifies the end-to-end chain."
- **Confidence:** high

## Structural


### 2026-06-14: Agents may emit the Output Receipt inside a tool call, not as bare text [tag: daemon-discipline]


- **Suggested action:** Fix daemon ledger/Output-Receipt extraction to scan Write/Edit tool content in addition to bare assistant text blocks — agents do not reliably emit the receipt as bare text.
- **Reasoning:** Entry describes the FORWARD canary (plan 57) silently dropping its ledger because the agent wrote the Ledger Updates block only inside a Write tool_use, and the runner's multi-turn text capture excluded tool content. The fix is mechanical — code change to the extraction path to read tool content. This is a tooling fix, not a documentary rule.
- **Confidence:** high

### 2026-06-14: Bound regex subsection captures — greedy-to-EOF grabs trailing prose [tag: daemon-discipline]


- **Suggested action:** Fix subsection capture regexes to stop at the first natural boundary (blank line or next section heading) rather than greedy-to-EOF, and enforce single-line constraints on values that must be one line.
- **Reasoning:** Entry describes ledger subsection regexes capturing trailing prose via greedy-to-EOF, breaking the FORWARD table row (multi-line item split row). States it was "Fixed in plan 62." The fix is a code change to regex behavior — mechanical/automated. Structural category.
- **Confidence:** high
