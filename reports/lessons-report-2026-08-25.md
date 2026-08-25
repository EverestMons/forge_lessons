# Lessons Report — 2026-08-25


## Summary


| Category | Count |
|---|---|
| governance_rule | 33 |
| instrumentation | 13 |
| structural | 11 |

**Total proposals:** 57


## Governance Rule


### 2026-08-25: A precedent's CONTEXT BOUNDARY is part of the precedent — a capability proven in one execution context is a CLAIM in every other  [tag: bellows-integration] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when citing a precedent as evidence that a capability works, verify the precedent's EXECUTION CONTEXT matches the current one — a capability proven under one permission model is a claim under another.
- **Reasoning:** [AUTHOR-CONFLICT] Entry describes: "E1 measured that a worktree agent's Bash could write ~/.claude. E5's build inherited it — and the daemon-dispatched DEV agent's four cp attempts were ALL sandbox-denied: the E1 agent had run under a Planner session's permissions, and the precedent silently crossed from that context into the daemon's sandboxed one, where it is false." Proposes qualifying precedents by their execution context.
- **Confidence:** high

### 2026-08-25: Resurrect removed code WITH its hardening history — the birth commit of a removed guard is usually the version that needed fixing  [tag: code-archaeology]


- **Suggested action:** Add rule: when resurrecting removed code, trace its git history for hardening commits (bug fixes, filter additions) after its birth commit — the birth version is usually the one that needed fixing.
- **Reasoning:** [AUTHOR-CONFLICT] Entry describes: "the plan initially specced resurrection from the guard's BIRTH commit. A panel scout measured that the production guard had gained a lifecycle-artifact ignore filter in a LATER commit — the day-one form would have blocked every future teardown." Proposes a governance rule about code archaeology.
- **Confidence:** high

### 2026-08-24: Folding a tool-finding into the artifact is not adopting it — the instruction changed and the practice did not  [tag: process-discipline] [tag: drafting-cycle]


- **Suggested action:** Add rule: when a finding reveals a misread practice, verify the BEHAVIOR changed — folding the finding into the artifact corrects the text but does not correct the habit; add a mechanical check or modify the callsite.
- **Reasoning:** Entry describes: "The Planner author-verified it, folded it into the plan as a warning, and then continued reading exit codes from that same checker for the remainder of the cycle. The artifact was corrected; the habit was not." Proposes a governance rule distinguishing artifact correction from behavior change.
- **Confidence:** high

### 2026-08-24: A fold aimed at what a finding DESCRIBED, not at what it MEASURED, survives every later pass  [tag: drafting-cycle] [tag: verification]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md: a fold must target what the finding MEASURED (the root cause), not what it DESCRIBED (the symptom) — a symptom-targeted fold leaves the root cause intact for later rediscovery.
- **Reasoning:** Entry describes: "The Planner rewrote the Cycle Log's CONTENT. The cause was elsewhere: the walk-7+ series sat on lens lines named - Weak spots (w7):, and the lens-line parser does not accept a suffixed lens NAME, so it skipped them silently." A fold aimed at the description, not the measurement.
- **Confidence:** high

### 2026-08-23: Read a checker's implementation before trusting its verdict — and in BOTH directions, because a blind spot produces false clears and false alarms from the same gap  [tag: verification] [tag: bellows-integration] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before relying on a checker's output, read its implementation to identify blind spots (skipped values, uncounted input patterns) — a blind spot produces both false clears and false alarms.
- **Reasoning:** Entry describes five instances: "propagation_check deliberately skips single-digit declared values, so a symbol pinned at 3 was restated twice with nothing able to see it. cycle_check parses only the five canonical lens names, so a sixth Conformance: line was silently uncounted — which produced BAR_MET on a walk that had an instruction-class finding." Proposes a governance rule about reading checker implementations.
- **Confidence:** high

### 2026-08-23: A mechanism cannot enforce a lesson about that mechanism's own insufficiency — the demonstration is circular and reads as proof  [tag: verification] [tag: governance-meta] [tag: process-discipline]


- **Suggested action:** Add rule: when a lesson describes a mechanism's limitation, the enforcement gate for that lesson must be OUTSIDE that mechanism — using the flawed mechanism to gate the lesson about its own flaw is circular.
- **Reasoning:** Entry describes: "it promoted three entries whose CONTENT is that the cited mechanism does not catch the thing. One reads An honest QA failure passes the Rule 20 self-check and was promoted on the Rule 20 gate." The enforcement is circular and the lesson proposes a governance rule about gate placement.
- **Confidence:** high

### 2026-08-23: A session wrap cannot append to an artifact a dispatched plan is mid-flight on — the append is lost, or it moves a count that plan's QA asserts  [tag: process-discipline] [tag: bellows-integration] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: do not perform a session wrap while a dispatched plan is mid-flight on any artifact the wrap would modify — the append can be lost or shift a count the plan asserts.
- **Reasoning:** Entry describes: "A wrap was requested while an executable was dispatched against that same file, and the collision has two distinct shapes: During the DEV step the plan's builder reads the register, an append landing between its read and its write is simply gone. Between the steps the plan pins the count." Proposes a governance rule about wrap timing.
- **Confidence:** high

### 2026-08-21: Before hand-building a classification, registry, or index, check whether the system already maintains one — the existing pipeline may be further along than the one you are designing  [tag: planner-discipline] [tag: verification] [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before designing a new classification, registry, or index, query the existing pipeline's database for overlapping coverage — the existing system may already implement what you are building.
- **Reasoning:** Entry describes: "I hand-classified 132 memory entries before discovering that lessons-forge.db already carried lesson_proposals with target_layer, target_artifact, route, status for 378 proposals over 370 ingested entries, covering a SUPERSET of the file." The lesson is a governance rule about checking for existing infrastructure.
- **Confidence:** high

### 2026-08-21: CEO DECISION — `glossary.md` is the per-repo home for DOMAIN KNOWLEDGE; `CLAUDE.md` stays operating protocol  [tag: governance-design] [tag: process-discipline]


- **Suggested action:** Create glossary.md in each repo that needs domain vocabulary; CLAUDE.md remains operating protocol only and does not house domain knowledge.
- **Reasoning:** Entry records a CEO decision: "each repo that needs one gets a glossary.md housing its domain knowledge. CLAUDE.md remains what it already is in practice — operating protocol." Measured: "NO glossary.md existed in any repo, and every CLAUDE.md contained zero domain vocabulary."
- **Confidence:** high

### 2026-08-19: The sibling-sweep discipline has a measured floor — when pre-existing yield hits zero while total yield does not fall, stop walking and run a mechanical check [tag: drafting-cycle]


- **Suggested action:** Add mechanical-check trigger to DRAFTING_CYCLE.md: when pre-existing-class yield is 0 on a walk AND total yield did not fall, stop walking and run the propagation check.
- **Reasoning:** Entry measures: "fourteen instances of one class survived eleven walks, a mechanical literal sweep, and a three-seat cold panel." The trigger is "mechanical and both halves are already measured per walk under walk-register schema v0.3: pre-existing-class yield is 0 on a walk AND total yield did not fall." Extends the 2026-08-03 sibling-sweep entry's remedy with its measured floor. [AUTHOR-CONFLICT] — entry dated 2026-08-19, authored by the Planner, proposes a change to DRAFTING_CYCLE.md that the Planner authored and benefits from. Adequacy is Gate 1's judgement. [DEDUP] — entry self-identifies: "This is the successor to ## 2026-08-03: The sweep fails at maximum context."
- **Confidence:** high

### 2026-08-19: The last fold round before a deposit has no executor — folds made after the execution seat are never run by anyone [tag: drafting-cycle]


- **Suggested action:** Add post-execution fold re-run requirement: treat the fold set produced after the execution seat as unexecuted code; before deposit, run every command those folds touched.
- **Reasoning:** Entry identifies: "In the Fork-C full panel the order is DISCOVERY → EXECUTION → CAPSTONE. Folds made in response to the EXECUTION seat and to the CAPSTONE are therefore never executed before deposit." Measured: "two live gate failures, both from folds made after the EXECUTION seat closed" — deposit_uncommitted and qa_test_result. "Both were invisible to reading and to the capstone's interaction read; both would have been caught by running the commands once." [AUTHOR-CONFLICT] — entry dated 2026-08-19, authored by the Planner, proposes a change to the drafting-cycle panel process that the Planner authored and benefits from. Adequacy is Gate 1's judgement. [REMEDY-GATED] — the remedy (a closing execution pass scoped to the fold set) requires a design decision about panel structure and recursion bounds.
- **Confidence:** high

### 2026-08-19: A cold seat's proposed FIX is an unexecuted hypothesis, and the seat's own report often already contains the real one [tag: drafting-cycle]


- **Suggested action:** Add fix-verification requirement to PANEL_SEAT_TEMPLATE.md: read a seat's FIX field as a hypothesis to verify — author-verify the fix runs before folding it.
- **Reasoning:** Entry measures: "PANEL_SEAT_TEMPLATE.md asks every seat for a 'smallest honest FIX'. No brief asks the seat to verify the fix runs." A DISCOVERY seat proposed "Task E reports its commit hash; Step 2 binds it" — folded verbatim — and the EXECUTION seat then proved it "unexecutable — bellows passes no values between steps." The correct fix "was already inside the first seat's own report, in a different section." [AUTHOR-CONFLICT] — entry dated 2026-08-19, authored by the Planner, proposes a change to PANEL_SEAT_TEMPLATE.md that the Planner authored and benefits from. Adequacy is Gate 1's judgement.
- **Confidence:** high

### 2026-08-19: A cross-step carrier cannot live inside the commit whose hash it carries [tag: bellows-integration]


- **Suggested action:** Add two-commit requirement for cross-step value channels: the work commit, then a commit of the carrier that names the hash; name the carrier in the producing step's Deposits.
- **Reasoning:** Entry identifies a structural impossibility: "if that artifact records the commit hash of the step's own commit, it cannot be inside that commit: the hash does not exist until the commit is made." Consequence: "a declared deposit permanently uncommitted — and deposit_uncommitted correctly fails it." The parent plan solved it and "the clone dropped the solution." [AUTHOR-CONFLICT] — entry dated 2026-08-19, authored by the Planner, proposes a change to plan-authoring governance that the Planner authored and benefits from. Adequacy is Gate 1's judgement.
- **Confidence:** high

### 2026-08-19: A knowledge destination that is not ingested cannot improve the system — route by what ACTS on the knowledge, not only by who must not be wrong [tag: planner-discipline]


- **Suggested action:** Add ingest-path check to destination routing: route on "does this destination feed a system that acts on it?" in addition to "who must not be wrong next time?" Retire PT v4.89's per-project LESSONS.md bin.
- **Reasoning:** Entry measures: "all five entries in the only bin that ever existed were shop-class, and the bin held zero project-domain content for its entire life." Two defects: (1) "v4.89 diagnosed it as a READ problem and fixed it with a standing-read mandate. That was necessary and insufficient." (2) "The bin is not forge-ingested. Everything routed there is invisible to the corpus, to duplicate detection, and to Gate 1 and Gate 2." Also duplicated an existing destination. [AUTHOR-CONFLICT] — entry dated 2026-08-19, authored by the Planner, proposes retiring PT v4.89's project-bin arm, a change to PLANNER_TEMPLATE.md that the Planner authored and benefits from. Adequacy is Gate 1's judgement. [REMEDY-GATED] — retirement of the per-project bin arm requires a design decision the classifier cannot make.
- **Confidence:** high

### 2026-08-19: A clone-diff needs THREE passes — facts, artefacts, structure — and each finds what the others structurally cannot [tag: drafting-cycle]


- **Suggested action:** Add requirement to DRAFTING_CYCLE.md that clone-diffs run three passes: facts (are stated claims still true?), artefacts (are named mechanisms present in the clone?), and structure (do the surviving parts compose correctly?).
- **Reasoning:** Entry proposes a three-pass methodology for clone-diffs: "Facts (walk 0, 5 found) — are the parent's stated claims still true? Blind to anything ABSENT." "Artefacts (walk 6, 4 found) — enumerate the parent's named mechanisms and count each in the clone." The lesson explicitly states each pass finds what the others structurally cannot, establishing a governance rule for the drafting cycle.
- **Confidence:** high

### 2026-08-19: Anchor a path where its file LIVES FOR GIT — tracked to the worktree, untracked to main [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: output paths in plan instructions must be anchored to the execution context (worktree root via $(pwd)), never to the main repo absolute path.
- **Reasoning:** Entry describes a plan halt: "its instruction mandated an output path rooted at the MAIN repo while the agent ran in a worktree. The write landed outside the sandbox, teardown's merge refused to overwrite." The fix is a documentary rule change about how plan instructions should reference file paths.
- **Confidence:** high

### 2026-08-19: A shipped, correctly-routed shop rule can produce the WRONG action in a specific context — and nothing in the cycle asks which of our own rules would mislead [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when applying a codified lesson to a plan, verify the lesson's remedy applies to the current context — a rule governing a dynamic value may be wrong when applied to a fixed value.
- **Reasoning:** Entry shows "A plan hard-coded cycle_date for a report generator. This shop carries a lesson instructing an author to measure the date at authoring and never inherit it. An agent applying that rule would recompute the date and be wrong." The lesson proposes qualifying rule application by context.
- **Confidence:** high

### 2026-08-19: A correction can OPEN a gap — removing a false belief without installing the true requirement it implied [tag: drafting-cycle]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md: when a walk disproves a claim, ask the consequent question — if the assumed property is false, what replaces it? A correction that removes a guard without installing the real one opens a gap.
- **Reasoning:** Entry describes: "Neither walk asked the consequent question: if the function does not commit, who does? The step's single mutation had no commit instruction at all." A correction removed a false belief without installing the true requirement it implied.
- **Confidence:** high

### 2026-08-19: A periodic task at an un-guarded loop boundary must own its exception guard — never inherit a hoped-for one [tag: drafting-cycle, bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: any function called from an un-guarded loop must own its own try/except — never assume the loop or its callees handle exceptions internally.
- **Reasoning:** Entry describes: "A new helper was to run from the daemon's while True loop, which has no try/except around its body. Its docstring asserted never raises — both callees degrade internally. That was false: one callee does bare os.remove/os.rename with no internal guard." The lesson is a documentary rule change about exception ownership.
- **Confidence:** high

### 2026-08-18: A CEO decision folded into a plan is an unread fold round, and behaves exactly like one [tag: drafting-cycle]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md: treat a CEO decision fold as a fold ROUND requiring the same sweep, reader and probe re-derivation as any other fold round.
- **Reasoning:** Entry measures: "Folding those three decisions into the plan produced nine findings on the very next walk, eight of them instruction-class — including three HIGHs." Cause: "the plan's premises, guards, synthesis and scope block had all been written while those forks were open, so a decision that closed one silently invalidated text elsewhere." Four specific invalidation sites named. The remedy is a documentary rule change to cycle governance.
- **Confidence:** high

### 2026-08-18: Price a finding's severity against evidence, not against how alarming it reads [tag: verification]


- **Suggested action:** Add severity-pricing guidance: before filing a structural finding as instruction-class, identify the run-time mechanism by which an agent does the wrong thing; a big number alone is not a mechanism.
- **Reasoning:** Entry demonstrates mispricing: "A capstone reported that a fold had dropped 3,023 characters of instruction... Filed instruction-class, ship-blocking." But measurement of the clone parent — "a plan that had been dispatched, completed and CLOSED — found it carried 13 content lines outside its own step blockquote. The prefix was therefore cosmetic in that plan class." Corrected from instruction 2 / record 1 to instruction 1 / record 2. A documentary rule about severity classification.
- **Confidence:** medium

### 2026-08-18: A watcher must key on the signal the system actually emits, not the state you expect it to write [tag: bellows-integration]


- **Suggested action:** Add watcher-design rule: before arming a watcher, identify which byte on disk or row in the DB changes when the target event fires, and key on that signal — not on the state name that ought to change.
- **Reasoning:** Entry measures: "A gate-watcher armed at deposit polled plans.lifecycle_state for awaiting_verdict and never fired. Bellows signals verdict-readiness by renaming the plan file to verdict-pending-<name>.md; the row stays in_progress." The watcher "would have polled indefinitely, and its silence was indistinguishable from work in progress." The remedy is a documentary rule about watcher design.
- **Confidence:** high

### 2026-08-18: A predicted deposit filename must be derived from the code that stamps it, not from the local session date [tag: planner-discipline]


- **Suggested action:** Add rule: when a plan predicts an artifact's filename, derive the format from the line of code that generates it — especially the timezone. Prefer glob/shape checks over exact predicted names in deposit gates.
- **Reasoning:** Entry demonstrates: "An Anvil cycle plan declared its deposit as audit-findings-2026-08-18.md, using the local session date. The code that writes the file stamps the name with datetime.now(timezone.utc)... so the cycle correctly wrote audit-findings-2026-08-19.md." The deposit_exists gate failed a correct deposit. "A wrong predicted name propagates: audit every downstream step." A governance rule about plan authoring.
- **Confidence:** high

### 2026-08-18: A domain pattern that looks like corrupted data may be the contract — confirm with the domain owner before "correcting" it [tag: verification]


- **Suggested action:** Add domain-verification rule: when a data value contradicts a related field's name, confirm with the domain owner before building a sweep or fix — the name may describe a mechanism while the value describes a negotiated parameter.
- **Reasoning:** Entry measures a near-miss: a fuel contract's "effective_day differed from what the timing_rule name implied (prior_monday with a non-Monday effective day). This was treated as an inconsistency... The CEO caught it: differing effective days are legitimate, negotiated per contract." The remedy is a governance rule about domain verification.
- **Confidence:** medium

### 2026-08-18: When a validator rejects an extraction, suspect the extraction before relaxing the validator [tag: verification]


- **Suggested action:** Add validation rule: before relaxing a validator, check whether later attempts on the same input succeeded — a success minutes later means the failure is an extraction artifact, not a schema gap.
- **Reasoning:** Entry measures: "A fuel bracket table's final row had no price_ceiling, and the validator rejected it. The immediate reading was that the validator was too strict." But "the CEO had re-prompted the copilot minutes later and got a complete table... Row counts 31 → 34 → 64 across three attempts confirmed the 31-row extraction was truncated, not open-ended." Making price_ceiling optional "would have silently imported truncated fuel tables as complete, on a field driving real money." A governance rule about validation hygiene.
- **Confidence:** medium

### 2026-08-16: A fold lands where the defect was NOTICED — and by the third reviewer that failure has moved BETWEEN the folds [tag: drafting-cycle]


- **Suggested action:** Add fold-set review rule to DRAFTING_CYCLE.md: after folding, re-read folds as a set for composition and sibling-site coverage; when three or more amendments touch one region, re-author it whole.
- **Reasoning:** Entry explicitly extends "the known class" — fold repairs land only where the defect was noticed — to a deeper failure mode: "once a plan has been folded by several reviewers, the unswept sites are no longer in the original draft — they are in the folds themselves." Measured: "A capstone seat found 9 of its 15 findings were defects in the panel's own folds." The remedy is a documentary rule change to the drafting-cycle governance about fold-set composition review. [DEDUP] — entry self-identifies as extending a known class about fold-repair locality.
- **Confidence:** high

### 2026-08-16: A guard that observes an EXIT CODE has not observed its EFFECT [tag: verification]


- **Suggested action:** Add verification rule: a guard must assert its post-condition as the EFFECT (e.g. file sha equals pin), never infer success from an exit code alone.
- **Reasoning:** Entry demonstrates that "exit 0" is an unreliable guard signal: "Executed in three constructed states, it exits 0 in all three — including the one where it restored nothing." Multiple sibling instances cited: changes() returning 0 for both success and no-match; plan_lint exiting 0 on PIN-CHECK mismatch. The remedy — "State a guard's post-condition as the EFFECT, then assert it" — is a documentary rule change to governance about guard design.
- **Confidence:** high

### 2026-08-16: The probe must match the INSTRUMENT the plan prescribes, not just the target [tag: verification]


- **Suggested action:** Add rule requiring instrument alignment: state the measuring tool beside every pinned number, and verify pins with the exact command the plan prescribes.
- **Reasoning:** Entry identifies "the probe's measuring tool must match the one the plan mandates": grep -cF counts LINES (read 3), while str.count() counts occurrences (read 4). "A QA agent obeying the plan exactly would have failed a correct edit." The rule about instrument-target alignment is governance. [DEDUP] — entry self-identifies: "The known class is that a probe's literal must match the target's representation; this is its other half."
- **Confidence:** high

### 2026-08-16: The freeze checklist is the least-sticky section in a clone — dropped four times in one day [tag: planner-discipline]


- **Suggested action:** Add clone-diff heading-level check to Planner workflow in PLANNER_TEMPLATE.md: diff a clone against its parent by SECTION HEADINGS first, since an omitted section leaves no token for a text diff.
- **Reasoning:** Entry measures: "Four consecutive plans cloned from parents that carry a freeze/deposit checklist, and all four dropped it" because "the block is Planner-facing rather than agent-facing, so no QA row reads it and no gate misses it." The fix — heading-level clone-diff — is a documentary addition to the Planner's workflow.
- **Confidence:** medium

### 2026-05-22: Phase 1.5 must scan halted-* plans, not just research/feedback [tag: planner-discipline]


- **Suggested action:** Add halted-plan scan to Phase 1.5 in PLANNER_TEMPLATE.md: ls knowledge/decisions/halted-* for every project with active Bellows dispatch.
- **Reasoning:** Entry measures: "Four consecutive plans were rejected by Bellows for the same missing Dispatch Mode field... The Planner's Phase 1.5 read of recent research and feedback did NOT scan decisions/ for halted-* plans, so the recurring authoring failure went undetected across sessions." The fix is a documentary addition to the Phase 1.5 checklist.
- **Confidence:** high

### 2026-05-22: Diagnostics that depend on production data must gate on data availability [tag: planner-discipline]


- **Suggested action:** Add production-data availability gate: before dispatching a diagnostic whose deliverable depends on production data, confirm the data is available in the target environment.
- **Reasoning:** Entry measures: "A discovery step running 5 SQL queries against invoice_pulse.db was dispatched despite knowing the Mac dev environment held no production data. Both fuel tables returned 0 rows; the threshold question gating Phase B was unanswerable." The fix is a governance rule about diagnostic dispatch preconditions.
- **Confidence:** high

### 2026-05-22: Amendment plans should scope sections to revise, not re-do the work [tag: planner-discipline]


- **Suggested action:** Add amendment-plan guidance: when a blueprint has 1-3 specific weaknesses, prefer an amendment plan scoping sections to revise over a full rewrite; do not use amendment-style when the premise is wrong.
- **Reasoning:** Entry describes a positive pattern: "Rather than reject and rewrite, the Planner authored an amendment plan scoping three sections to revise... The result was better than a full rewrite because correct sections were undisturbed." The suggested action codifies this as a governance rule for plan authoring. Confidence medium because the entry is partly a positive observation.
- **Confidence:** medium

### 2026-05-20: Bellows verdict and pause mechanics — three failures in one session [tag: bellows-integration]


- **Suggested action:** Add bellows authoring rules: pause_for_verdict is single-valued (use "always" for multiple pauses); verdict body is informational only; do not list optional deliverables in Deposits.
- **Reasoning:** Entry records three Planner-authoring failures "all rooted in treating Bellows' parser as more forgiving than it is": (1) comma-separated pause_for_verdict matched nothing; (2) verdict continue on a final step is irreversible closure "regardless of body text"; (3) "(optional)" parenthetical in Deposits is unparsed prose. Three documentary rules for plan authoring.
- **Confidence:** high

## Instrumentation


### 2026-08-24: A tool's verdict CHANNEL is part of its contract — reading the exit code of a checker that always exits 0 certifies nothing  [tag: verification] [tag: process-discipline]


- **Suggested action:** Add verification requirement: when consuming a checker's result, identify its verdict CHANNEL (exit code vs stdout vs stderr) by reading the implementation — a checker that always exits 0 cannot be verified by exit code.
- **Reasoning:** Entry describes: "walk_register_lint prints CONFORMANT/UNCONFORMANT to stderr and always exits 0. the Planner read exit=0 and reported the register clean; it was UNCONFORMANT throughout." Proposes a procedural safeguard about identifying and using the correct verdict channel.
- **Confidence:** high

### 2026-08-24: A check whose result you PRINT but do not BRANCH on is not a check — the gate has to be in the control flow  [tag: verification] [tag: process-discipline]


- **Suggested action:** Add rule: every verification check in a plan step must have its verdict in the control flow (an explicit conditional that halts on failure) — printing a result without branching on it certifies nothing.
- **Reasoning:** Entry describes: "the next scripts ran the lint, printed register: UNCONFORMANT, and committed anyway, twice, because the verdict was echoed into the transcript and nothing consumed it. The commit was never conditional on it." Proposes a control-flow enforcement requirement.
- **Confidence:** high

### 2026-08-24: A review covers the plan's FILE LIST; a contract change's blast radius is its CONSUMERS — sweep them or the suite finds them for you  [tag: drafting-cycle] [tag: testing]


- **Suggested action:** Add drafting-cycle rule: when a plan changes a function signature, schema, or admission predicate, sweep its CONSUMERS (grep callers, test fixtures, depositors) — not just the plan's write set.
- **Reasoning:** Entry describes: "QA still stopped the arc with 40 red tests, every one a PRE-EXISTING fixture that deposited plans the old way and now met the new law. scout, discovery, execution and capstone all reviewed the plan's write set and the design's decisions; NONE asked who else consumes this interface." Proposes a consumer-sweep procedure.
- **Confidence:** high

### 2026-08-24: A schema enum value is a FEATURE CLAIM — if no code writes it, the feature does not exist; grep the writers of every enum arm  [tag: bellows-integration] [tag: verification]


- **Suggested action:** Add verification requirement: for every enum arm in a DDL CHECK constraint, grep the codebase for writers of that value — an unwritten arm reads as a feature that does not exist.
- **Reasoning:** Entry describes: "The clearances DDL shipped with cleared_by CHECK (cleared_by IN ('depositor','clear_tool')) — and nothing anywhere wrote 'clear_tool'. so under the live admission flip NO shop-infra plan could ever dispatch again: the shop's entire self-modification path was gone, invisibly." Proposes a verification procedure for schema enum completeness.
- **Confidence:** high

### 2026-08-23: An identity that DERIVES one of its terms cannot discriminate — it balances for every value of the thing you are checking  [tag: verification] [tag: planner-discipline] [tag: qa-discipline]


- **Suggested action:** Add verification rule: when a post-condition uses a sum or identity, check that each term is independently measured — if any term is derived as the residual of another, the identity is tautological and proves nothing.
- **Reasoning:** Entry describes: "A diagnostic produced a promotion set of G entries and checked itself with G + (X - G) + P + Q = N. It balanced. It balanced because the second term is DEFINED as the residual of the first — so the sum reaches N for any value of G whatsoever, including the wrong one." Proposes a procedural check for tautological identities.
- **Confidence:** high

### 2026-08-22: A single-arm probe against a drifting corpus is uninterpretable — run a controlled A/B so the change's effect separates from pre-existing noise  [tag: verification] [tag: planner-discipline] [tag: qa-discipline]


- **Suggested action:** Add verification rule: when testing a fix against a corpus, run a controlled A/B — measure the unchanged corpus first (control arm), then apply the fix (treatment arm), and compare the delta rather than interpreting a raw count.
- **Reasoning:** Entry describes: "my first probe annotated three headings, ran the ingest against a corpus copy, and reported inserted=51. I nearly read that as a plain failure." The lesson proposes a procedural safeguard: controlled A/B testing against drifting data.
- **Confidence:** high

### 2026-08-22: Write the regression guard BEFORE the fix and watch it fail — a guard authored afterwards and only ever seen green discriminates nothing  [tag: qa-discipline] [tag: verification] [tag: process-discipline]


- **Suggested action:** Add QA requirement: write the regression test BEFORE applying the fix, capture the RED output as evidence, then apply the fix and capture GREEN — a test authored after a fix has never proven it would catch the defect.
- **Reasoning:** Entry describes: "A corrective plan mandated the order explicitly: add the failing test while the code is still at the defective commit, capture the RED output, then apply the fix, then capture the GREEN. a test written after a fix is confirmed only against the world in which the fix already exists." Proposes a procedural safeguard for QA.
- **Confidence:** high

### 2026-08-21: A workflow can be correctly mechanized and still be wrong at the destination — check what the pipeline's target set CONTAINS, not just that it runs  [tag: process-discipline] [tag: governance-design] [tag: planner-discipline]


- **Suggested action:** Add pipeline audit step: after a cycle run, inspect the distribution of target_artifact and target_layer values — a pipeline that classifies everything to a single destination signals an incomplete destination ladder.
- **Reasoning:** Entry describes: "its target_artifact distribution is PLANNER_TEMPLATE.md 204, DRAFTING_CYCLE.md 101, and 7 to actual code — and target_layer offers only governance (334) and structure (20). There is no CODE rung, no per-repo rung, no DELETE rung." Proposes inspection of pipeline output distributions as a procedural safeguard.
- **Confidence:** medium

### 2026-08-19: A declaration/consumer pair fails in BOTH directions, and fixing one half tends to break the other [tag: verification]


- **Suggested action:** Add a pre-commit verification step: for every plan, check that each declaration in the numbers table is consumed by at least one step, and each step reference resolves to a declaration.
- **Reasoning:** Entry describes "Two defects in one plan: Consumers citing a missing declaration — three sections cited the three report shas from Numbers and those hashes appeared zero times. Declarations with no consumer — five pins were declared and referenced by no step." Proposes a procedural cross-reference check.
- **Confidence:** high

### 2026-08-19: A malformed sqlite3 URI silently CREATES a decoy database, and no gate audits for stray files [tag: verification]


- **Suggested action:** Add verification checklist item: when using sqlite3 CLI with URI parameters (?mode=ro), prefix the path with file: — without it, the entire string is a filename. Post-step: check for stray 0-byte database files.
- **Reasoning:** Entry describes: "A QA step ran sqlite3 'lessons-forge.db?mode=ro' without the file: prefix. Without it the entire string is a filename, so sqlite3 created a 0-byte file. The directory already held two 0-byte decoys of exactly this kind." Proposes a procedural safeguard against URI misuse.
- **Confidence:** high

### 2026-08-18: Fold damage is POSITIONAL, and presence probes are structurally blind to it [tag: drafting-cycle]


- **Suggested action:** Add structural-assertion step after every fold: assert document structure (e.g. every content line in a blockquoted step begins with "> ") rather than just text presence.
- **Reasoning:** Entry proposes a new mechanical check: "assert STRUCTURE, not just presence: for a blockquoted step, every content line between the step heading and the next top-level heading must begin with > . One awk; it reported 0 immediately and would have failed three walks earlier." Fold damage was "positional rather than semantic — the inserted text was correct every time and landed in the wrong place." Five walks of reading could not substitute for one mechanical structural check.
- **Confidence:** high

### 2026-08-18: A UTF-8 dev machine cannot reproduce a cp1252 failure — the only guard is an ASCII-assertion test [tag: execution-environment]


- **Suggested action:** Add ASCII-assertion test (text.encode("ascii") or assert all(ord(c) < 128 for c in text)) to cross-platform scripts whose output runs on a cp1252 machine.
- **Reasoning:** Entry proposes a new testing mechanism: "The regression guard is an ASCII-assertion test... not a re-run — this tests the property directly on the Mac." The failure: "A non-ASCII character in a script's output — a single ≠ (U+2260) — crashed the script [on Windows] while passing every Mac test." A new procedural safeguard (ASCII assertion) rather than a code fix.
- **Confidence:** high

### 2026-08-16: A decision table's correctness is a property of its STATE SPACE — enumerate it in code, because reading cannot [tag: verification]


- **Suggested action:** Add state-space enumeration step to verification procedures: any branch structure with more than three arms must have its truth table written as code enumerating every input combination.
- **Reasoning:** Entry proposes a new verification mechanism: "write the truth table as code, enumerate every input combination, and assert exactly-one-arm coverage plus a catch-all." Measured: "An arm collision surfaced the instant its 54 states were enumerated in a dozen lines of Python" — a collision that "three cold seats and two Planner passes READ" without finding. The fix is a new procedural step (code-enumerated truth tables), not a documentary rule change.
- **Confidence:** high

## Structural


### 2026-08-25: A shared deposit FILENAME is a SEQUENTIAL collision — successive plans reusing one evidence name silently block each other's teardown  [tag: bellows-integration]


- **Suggested action:** Uniquify QA deposit filenames (e.g. include plan_id) so successive plans' evidence files do not collide at teardown merge — a shared name causes silent merge failure and stranded commits.
- **Reasoning:** [AUTHOR-CONFLICT] Entry describes: "Every QA step deposits pytest_full.txt under the same name. Plan 520's teardown-merge found the live tree already carrying 518-era content at that path, refused to overwrite, and FAILED SILENTLY — no worktree_teardown gate row, no log ERROR." The fix is a code change to uniquify deposit filenames.
- **Confidence:** high

### 2026-08-25: A correct, indexed instruction did not survive its third encounter — when an act keeps failing against documentation, mechanize the ACT  [tag: process-integrity]


- **Suggested action:** When an instruction fails repeatedly despite correct documentation, mechanize the act — convert the instruction into a tool-enforced check that fires at the moment of the act, not a memory entry consulted at the author's discretion.
- **Reasoning:** [AUTHOR-CONFLICT] Entry describes: "The verdict-act memory entry documented both form faults in advance, recorded its own prior failure, was three days old and indexed — and the operator still committed BOTH faults. The fix that held was" converting the instruction to a tool check. The lesson proposes mechanization over documentation.
- **Confidence:** high

### 2026-08-24: A watched directory's safety property is its daemon's ADMISSION PREDICATE, not the directory you avoid  [tag: bellows-architecture] [tag: planner-discipline]


- **Suggested action:** Document that deposit safety depends on the daemon's admission predicate (bellows.is_runnable_plan regex), not on directory avoidance — a non-matching filename in the watched directory is inert.
- **Reasoning:** Entry describes: "The guard this shop adopted is a LOCATION rule: mirror only at a non-claimable scratchpad. The location is not what makes it safe. bellows.is_runnable_plan admits exactly the regex pattern." The lesson identifies the true safety property as structural (the admission predicate in code).
- **Confidence:** high

### 2026-08-24: An affirmation gate keyed on TODAY'S DATE is satisfied by yesterday's author, if yesterday was today  [tag: verification] [tag: process-discipline]


- **Suggested action:** Fix wrap_check to key on the current SESSION's sweep, not on today's calendar date — an append-only baton scanned for today's date matches any session that ran on the same calendar day.
- **Reasoning:** Entry describes: "wrap_check fails unless shop_next_session.md carries a Lessons-swept: line containing datetime.date.today().isoformat(). It scans the WHOLE baton, and the baton is append-only. So the predicate it actually computes is not this session swept but some session swept on this calendar date." The fix is a code change to the gate predicate.
- **Confidence:** high

### 2026-08-24: A predicted id is not an identity — key watchers and verdicts on the artifact's stable name, never on the counter you read  [tag: bellows-integration] [tag: verification]


- **Suggested action:** Key watchers and verdicts on the artifact's stable name (e.g. plan file path), not on a predicted numeric id — concurrent deposits can consume the predicted sequence value.
- **Reasoning:** Entry describes: "The Planner deposited a plan with id_sequence reading 512, armed a watcher on plan_id=512 — a concurrent session's deposit had consumed the prediction, the Planner's plan claimed as 513, and the watcher's first TERMINAL event was another arc's." The fix is a code/design change to how watchers key on artifacts.
- **Confidence:** high

### 2026-08-24: An observation window anchored at the OBSERVER'S start cannot contain events that precede the observer — test a window's bounds against the timeline of what it must catch  [tag: verification] [tag: design]


- **Suggested action:** Fix the gap-detection window to include events that precede the observer's creation — deposits happen before wrap-arming, so an arm-to-now window is structurally empty for the events it must catch.
- **Reasoning:** Entry describes: "the sentinel is created when the operator types /wrap, hours AFTER every deposit the check exists to catch. The window was structurally empty: deposits precede wrap-arming by construction, so the arm could never fire on anything." The fix is a design/code change to the observation window bounds.
- **Confidence:** high

### 2026-08-22: A function that computes a LOOKUP KEY must be the identity on every value already stored — incidental "hygiene" inside it silently orphans existing rows  [tag: verification] [tag: mechanics] [tag: bellows-integration]


- **Suggested action:** Ensure _key_heading() preserves all whitespace patterns present in existing stored headings — any normalization that rewrites stored values causes false-miss re-insertion on every ingest cycle.
- **Reasoning:** Entry describes: "also collapsed internal whitespace: re.sub(r'\s+', ' ', cleaned).strip(). The house heading style puts TWO spaces before the first [tag:], so 40 of 370 stored headings contained a run the collapse rewrote. The lookup then searched for a canonical form the database did not hold, missed, and RE-INSERTED those rows on every ingest." The fix is a code change.
- **Confidence:** high

### 2026-08-21: `content_hash` detects modification, not identity — it is the wrong key for reconciling a corpus against its source file  [tag: verification] [tag: mechanics]


- **Suggested action:** Use normalized source_heading (not content_hash) as the reconciliation key when matching corpus entries against their source file; reserve content_hash for change detection.
- **Reasoning:** Entry describes: "direct content_hash matching returned 27/320, while normalized-heading matching returned 313/320. The hash is computed over raw_content after normalization, so ANY body edit since ingestion flips it while the heading stays recognizable." The fix is a code/tooling change to the reconciliation key.
- **Confidence:** high

### 2026-08-18: `plan_lint`'s dryness check disagrees with §2's bar, and its false-clean rate RISES as a cycle converges [tag: instrumentation]


- **Suggested action:** Modify plan_lint check (f) to parse the aggregate class split (e.g. "w9 1 folded — instruction 1") rather than only the last lens result line.
- **Reasoning:** Entry identifies a code defect in plan_lint.py:356-372: "check (f) finds the last lens result line in the Drafting Cycle block and warns only if that one line contains 'fold' and not 'dry'. §2's actual bar (DC:40) is a class test over the whole walk: zero instruction-class findings." The disagreement worsens as cycles converge: "ACID and Integration go dry FIRST... so the check is least trustworthy at exactly the moment a Planner most wants to close on it." A tooling code fix. [REMEDY-GATED] — candidate fix (parse aggregate class split) requires implementation decision on the parsing approach.
- **Confidence:** high

### 2026-08-18: An autouse isolation fixture can be silently bypassed by import binding — verify isolation per-path before writing tests that write [tag: test-infrastructure]


- **Suggested action:** Fix test isolation fixture bypass: modules using "from config import BASE_DIR" at import time bind an immutable copy that monkeypatch.setattr cannot reach; prefer lazy config.BASE_DIR resolution.
- **Reasoning:** Entry identifies a code defect in test infrastructure: "An autouse fixture patching config.BASE_DIR via monkeypatch.setattr only reaches code resolving the attribute at call time. A module doing from config import BASE_DIR at import binds its own copy... the patch never touches it." The fix requires code changes to how modules import config values.
- **Confidence:** high

### 2026-05-30: Worktree regression on restart-during-pause; Planner-direct recovery; plan header needs a title line [tag: bellows-integration]


- **Suggested action:** Fix bellows worktree preservation across daemon restarts: a restart during a verdict pause removes the orphaned worktree and re-creates it at main HEAD, losing the paused step's commit.
- **Reasoning:** Entry identifies a bellows code bug: "A daemon restart during the pause caused Bellows to remove the orphaned worktree and re-create it at main HEAD — which did not contain Step 1's commit." Also: "a continue verdict on a gate-failed final step goes to Done (not retry)" and "plans starting directly at the pipe-field line without a # Title first line parse to 0 keys and reject." Three distinct structural issues requiring code fixes.
- **Confidence:** high
