# Classifications — Cycle 2026-08-07, Tranche A (Proposals 223–239)

**Plan:** executable-311
**Step:** 2
**Tranche:** A (entries 215–231, proposals 223–239)
**Date:** 2026-08-07

## Classification Reasoning

### Proposal 223 (entry 215) — `governance_rule` → `PLANNER_TEMPLATE.md`

Entry documents the Forward Register channel's third distinct failure mode: a correctly formatted block placed outside `### Ledger Updates` where the parser reads. The block format was never the problem — the bullet splitter never saw a payload because `lu_body` scopes to that section body only. The authoring rule half requires verification of block location in the parser's input scope, not merely block presence. The parser defect half (`lu_body` scoping in `parser.py`) is bellows-owned — Rule 46 question for Gate 1. Cluster (B) with entries 220/221/228: four lessons on one channel, each with an authoring-rule half and a bellows-owned parser half.

### Proposal 224 (entry 216) — `governance_rule` → `DRAFTING_CYCLE.md`

Entry documents a Conflict-Ledger constraint that oscillated through three individually well-reasoned formulations. The tell was the second reversal: a constraint corrected in one direction then the other is enumerating, not converging. The surviving form states the principle instead of the list: "a capture a LATER step, row, or resume branch must read is deposited; a value consumed within the step that produces it needs no home." This is a constraint-authoring rule for §2.8, governing how ledger constraints are formulated and revised.

### Proposal 225 (entry 217) — `governance_rule` → `PLANNER_TEMPLATE.md`

Entry documents three instances in one drafting cycle where a requirement was authored in the verifier rather than the producer. An agent could satisfy every instruction it was given and fail the row. The class was never swept across five walks — existing doctrine requires a requirement to have a structural home but does not say the home must sit in the step that does the work. This plan (311) already practices the rule; it is codified nowhere. Proposes a new rule near 54/58.

### Proposal 226 (entry 218) — `governance_rule` → `PLANNER_TEMPLATE.md`

Entry documents a `##`-banner claim about `gates.py` that survived five warm walks, five ACID passes, and a `plan_lint` run because every pass read the assertion rather than running the gate. The banner constant at `gates.py:567` is the bare string without `##`. The two characters are neither emitted nor enforced. Proposes extending Rule 52: any gate-enforcement claim is a claim to re-run, not inherit. Secondary finding: a calibration range from n=6 was applied to a 16-item batch — record sample sizes beside thresholds.

### Proposal 227 (entry 219) — `governance_rule` → `DRAFTING_CYCLE.md`

Entry documents a clone-lineage error where "newest same-class plan" was asserted from memory rather than measured. A sibling had shipped one day later, and an ACID pass spent a finding rediscovering a hardening the newer sibling had already shipped and marked as executed. The draft further asserted "no prior draft said so," which the newer sibling's text directly contradicts. Proposes a measured-line requirement for §2.6: sort the shipped set by ship date and name the winner.

### Proposal 228 (entry 220) — `governance_rule` → `PLANNER_TEMPLATE.md`

Entry documents a channel that failed in four ways across three sessions because every check reads the deposited file while the daemon reads `_all_assistant_text` assembled from assistant text blocks plus `Write` tool content plus `Edit` replacement strings — and nothing else. The consequence is a green check over a total loss. Cluster (B) with entries 215/221/228. Parser half bellows-owned — Rule 46 question for Gate 1. Proposes a channel-verification authoring rule for PLANNER_TEMPLATE.md.

### Proposal 229 (entry 221) — `governance_rule` → `PLANNER_TEMPLATE.md`

**Precedent-poor tag `verification` (1 prior).** Entry documents a five-item block where cardinality agreed (five in, five out, exit zero) but items arrived truncated because the splitter drops continuation lines. The entry proposes two fixes: constrain item shape (no wrapping onto a second physical line) and compare content not counts. Both are documentary authoring rules about how plan blocks are constrained and verified — governance file edits to PLANNER_TEMPLATE.md, not tooling changes or procedural workflow additions. Cluster (B) with entries 215/220/228.

### Proposal 230 (entry 222) — `governance_rule` → `PLANNER_TEMPLATE.md`

Entry documents durability machinery that clobbers its own artifact on the resume path. The dispatcher re-runs a dead step from the top, so the resumed step re-measures a now-post-write corpus and rewrites the before-image with vacuous values. The fix is a posture: if the file exists, do not rewrite it. Proposes extending Rule 56/62 resume rules. Clusters with entry 261.

### Proposal 231 (entry 223) — `governance_rule` → `DRAFTING_CYCLE.md`

Entry documents a clone re-importing an identical excuse under a new marker name, laundering it past the governing rule. The clone quoted the cost-test rule approvingly and then violated it. The cost-test clause exists in §2.7; the any-spelling scope does not. Partial overlap — proposes extending the INHERITED-marker clause to cover any marker meaning "I did not run this" regardless of spelling.

### Proposal 232 (entry 224) — `governance_rule` → `DRAFTING_CYCLE.md`

Entry documents six adversarial passes that found content defects while the one-command conformance check never ran and would have caught forty structural drops. The doctrine already separates conformance from adversarial review — §5 shipped at 1.0 and already orders "before the closing walk." The residue is the stronger ordering (before the expensive adversarial passes, when shape stabilises) and recording the linter's exit code. Cluster (E) with entry 237 — one §5 scheduling edit, not two.

### Proposal 233 (entry 225) — `governance_rule` → `DRAFTING_CYCLE.md` [CLUSTER A]

**SHAPE-DECISION CLUSTER (A):** routes into the reserved CEO decision on drafting-cycle shape (baton item 2). Entry provides evidence that nine adversarial rounds with roughly 150 findings left a CRITICAL defect undetected in the one region no reader was pointed at. Severity counts (8, 5, 2, 4, 3) measured aim, not convergence. Coverage is the convergence signal; the complete five-lens walk covered twenty-seven sections for roughly the token budget of one targeted round.

### Proposal 234 (entry 226) — `governance_rule` → `DRAFTING_CYCLE.md`

Entry documents a structural cut where a check's label was deleted but its body (a fenced query and three assertions) survived six lines below, now visually nested under an unrelated neighbour. The post-condition asked only whether the label string was gone. Proposes extending §2.7 subtractive-trim bullet: verify a deletion by the absence of the construct's content, not its label; excise the whole span.

### Proposal 235 (entry 227) — `governance_rule` → `DRAFTING_CYCLE.md`

Entry documents a structural cut producing six dangling cross-references, two orphaned captures, and a stale justification. The renumbering rationale was measurably false: every reference that broke was to a deleted row, which vacancy cannot fix. The arithmetic did not go as projected either — removal notes explaining what used to be there generated six of the next reviewer's nine findings. Proposes a §2.7/§2.8 cut-as-edit rule.

### Proposal 236 (entry 228) — `governance_rule` → `PLANNER_TEMPLATE.md` [CLUSTER B]

Entry documents a parser terminator fix applied to one subsection while the mechanism is subsection-generic. The last subsection in an ordered set is structurally exposed — it terminates only by blank line or end-of-stream. Fourth instance of the fold-lands-where-noticed class on the same channel. Parser defect half bellows-owned — Rule 46 question for Gate 1. Cluster (B).

### Proposal 237 (entry 229) — `governance_rule` → `DRAFTING_CYCLE.md`

**Precedent-poor tag `verification` (1 prior).** Entry documents four independent readers in one session falling prey to the pipe-masking-exit-code error. The shell reports the exit status of the last command in a pipeline, so a formatter's success is read as the checker's. The fix is an explicit documentary rule change to the command-output section of §2.7 — never pipe a command whose exit code carries meaning. This is a governance rule rather than instrumentation or structural because it specifies a documentary constraint on how commands are written in plans, not a tooling change or procedural step.

### Proposal 238 (entry 230) — `governance_rule` → `DRAFTING_CYCLE.md` [CLUSTER A]

**SHAPE-DECISION CLUSTER (A):** routes into the reserved CEO decision on drafting-cycle shape (baton item 2). Entry provides evidence that self-inflicted repair proportion is a convergence-negative signal. Across six review phases the proportion rose from 6-of-9 to 8-of-8 to 2-of-2 high-severity. The artifact genuinely improved but the last rounds returned mostly self-inflicted work. No Family line present — placement derived from body.

### Proposal 239 (entry 231) — `governance_rule` → `PLANNER_TEMPLATE.md`

**Precedent-poor tag `verification` (1 prior).** Entry documents two gates reading the same declared-outputs list with opposite polarity — scope check tolerates extras while deposit check requires every name. The fix is a documentary rule change to PLANNER_TEMPLATE.md about how the Deposits block interacts with consuming gates of different polarity — a governance file edit. This is governance_rule rather than instrumentation because the fix is a rule about block semantics, not a procedural step or tooling change. No Family line present — placement derived from body.
