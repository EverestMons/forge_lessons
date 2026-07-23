# Classifications Summary — Part 2 (2026-07-22)

## Classifications (Entries 172–178, remaining 7 of 15)

### Entry 172 — "Restructuring a plan for DRY trades duplication for a consistency surface"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: before splitting or extracting shared content, diff the candidate-shared regions and move only byte-identical clauses; after extraction, walk the seam as its own surface — the ACID and destruction lenses have the most purchase there. State the four-part extraction contract: what moves, what stays, how the moved content is retrieved, and what the retrieval promises.
- **Reasoning:** Entry documents how DRY restructuring of plans relocates defects into seams. States: "Both moves reduced size and were correct — and both relocated the hardest defects into the seam. Every seam defect had one shape: two representations of a single fact that can disagree." Identifies the governing rule as "single-source what is IDENTICAL between the parts; keep inline what DIFFERS. Unifying things that differ is the false-sharing bug; duplicating things that are identical is the drift bug." Prescribes a four-part extraction contract: "what moves, what stays, how the moved content is retrieved, and what the retrieval promises (over-return, under-return, an absent source). Each unstated part is a separate defect."

### Entry 173 — "Generalising a concrete guard into an inference waters it down"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when moving a guard into a reusable or generic form, keep the mechanism generic but require the caller to pin the specifics; make the absence of a pin a hard failure.
- **Reasoning:** Entry documents how extracting a shared audit contract caused a blast-radius guard to degrade. States: "the plans' C7 blast-radius guard — an explicit six-repo list — became the contract's generic 'every repo this plan reads and the root.' Neither plan then re-stated the concrete set, so the guard degraded to 'whatever repos the agent infers it read.'" The failure: "one plan reads a repo (for a cross-reference) that holds none of its target files, and an agent inferring the set from file locations would silently drop that repo." Concludes: "A concrete enumerated list is the guard; a generic description is a prompt to re-derive it, and re-derivation can undercount."

### Entry 174 — "The finished deliverable's physical shape is a question none of the instruction-lenses asks"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: before deposit, sketch one real block of the finished deliverable and confirm the mandated format can hold everything the plan requires per item. Where per-item output is rich, prefer a block-per-item structure with a compact summary index over a table.
- **Reasoning:** Entry identifies a blind spot: adversarial lenses examine the procedure but not the output form. States: "Twelve drafting-cycle walks examined whether a diagnostic's instructions were correct, safe, answerable, and mutually consistent. None asked what the finished report would physically look like." Consequence: "the mandated output format (a markdown table, one row per work item) structurally could not hold the per-item evidence the entire plan existed to capture: quoted verdict prose, a DB-flag-vs-filesystem pair, a three-part live-work burden. The format requirement silently defeated every content requirement." Concludes: "A plan can have flawless instructions that assemble into an unusable artifact."

### Entry 175 — "Read the record before deriving"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: run the integration-vs-record scan early — before building a method from scratch, grep the template's named sections, LESSONS.md, and especially any file the plan already references for another purpose.
- **Reasoning:** Entry documents repeated re-derivation of already-codified facts. States: "Three times in one cycle: the DB-as-index / filesystem-as-ground-truth protocol was rediscovered across three lenses before someone read the Lifecycle DB Read Protocol section; the git --no-pager requirement was derived after a timeout when it was a codified Compression Principle; and the halted-plan successor method (three greps + a landed-check) was reconstructed over three lenses when BACKLOG-ARCHIVE.md — a file the plan already cited for a different fact — states it outright, with an outcome prior (9 of 16 had successors, 7 did not) the empirical work lacked." Prescribes: "run the integration-vs-record scan EARLY, not as lens four" and "When you cite a file, read the rest of it."

### Entry 176 — "Bellows-dispatched step's OUTPUT files must be written at paths relative to the agent's own working tree"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md Bellows dispatch section: split path rules by operation — READS of shared state take an absolute path; WRITES of the step's own deposits take a path relative to the agent's working tree. Never use a blanket "run from X" instruction.
- **Reasoning:** Entry codifies the plan-225 worktree-teardown lesson. States: "A plan that runs under worktree isolation but instructs the agent to write its deposit to an absolute main-tree path lands the file in the main tree, where the worktree's own commit cannot see it: teardown commits nothing, main gains an untracked file, and the cherry-pick collides with a byte-identical untracked copy — the R2 failure shape." Root cause: "The plan-225 incident came from a single 'commands run from the main tree' line that was right for canonical-DB access and wrong for file output." Prescribes: "read the world by absolute path; write your own output where you stand."

### Entry 177 — "The five adversarial lenses do not check a plan against the codified authoring rules"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add a mechanical conformance pass to PLANNER_TEMPLATE.md § The Drafting Cycle (distinct from the five lenses): run plan_lint, then walk the plan against the Orchestration Plan Rules and the Plan Authoring Checklist by scope; do it once the plan's shape is stable, before the closing walk.
- **Reasoning:** Entry identifies a gap between adversarial review and mechanical conformance. States: "Weak-spots, destruction, vulnerabilities, integration-vs-record, and ACID all interrogate the plan's reasoning; none systematically checks it against the codified authoring surface (the Orchestration Plan Rules, the Plan Authoring Checklist, plan_lint)." Evidence: "A dedicated mechanical conformance pass, run mid-cycle, caught what the adversarial lenses had missed across several walks: a missing declared Scope: block (Checklist 23), absent Rule-41 liveness anchors on a long SA step, a ## How to Run block that violated Rule 35 for Bellows dispatch, and a stale marker count." Concludes: "These are not defects of reasoning — they are conformance failures, invisible to lenses that ask 'is this correct?' rather than 'does this match the rules?'"

### Entry 178 — "A plan's pre-stated conclusions anchor the executing agent toward them"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: pre-state a conclusion only with (1) named, agent-runnable verification anchors and explicit licence to disagree; (2) a statement that the pre-resolutions are a fact about which items were investigated, not a distribution; and (3) equal evidence burden on every disposition.
- **Reasoning:** Entry documents three compounding failure modes from pre-stated conclusions. States: "Anchoring: the pre-resolutions become a forecast — the agent infers the un-resolved items are probably the same, biasing toward the pre-stated answer. Direction: every over-reach in the cycle ran toward archive, the cheap disposition that closes an item, because the plan's whole method was built to recognise 'shipped/dead' and anything ambiguous fell toward it. Wrong-direction risk: one pre-resolution (a duplicate-pair survivor) was initially framed as live work and was in fact archive — the Planner had been confidently wrong about that exact pair once already." Concludes: "The value of a pre-resolution (it saves the agent real work) is only safe if it cannot launder an assertion into an audited finding."

## Ambiguous Entries

None — all 7 entries classified as governance_rule with high confidence.
