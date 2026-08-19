# Lessons Report — 2026-08-19


## Summary


| Category | Count |
|---|---|
| governance_rule | 19 |
| instrumentation | 3 |
| structural | 3 |

**Total proposals:** 25


## Governance Rule


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
