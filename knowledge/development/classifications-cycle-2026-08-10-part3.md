# Classification Reasoning — Cycle 2026-08-10, Part 3 (Tranche C: entries 294–306)

## Per-entry classification reasoning

### Entry 294 — A restructuring pass resets the convergence curve (drafting-cycle)

**Category:** governance_rule | **Target:** DRAFTING_CYCLE.md | **Confidence:** high

The entry identifies structural edits (collapses, promotions, sub-step splits) as convergence-resetting events. A cycle's per-walk yield fell steadily then rose after two collapses — not from noise, but because the artifact genuinely changed. The finding count after a restructuring pass is a first-pass count over new arrangement, not a convergence signal. The remedy prescribes a Cycle Log convention and a re-read of the close bar. Cluster (A) member — routes into the §2 doneness criterion rewrite alongside entries 267, 270, 284, 300.

### Entry 295 — A corrected corpus measures the FALSE-positive surface (verification)

**Category:** governance_rule | **Target:** PLANNER_TEMPLATE.md | **Confidence:** high

A census over closed plans conflated two populations: final-state matches are dominated by prose describing corrected defects, not instances of them. The measurement answers "how often do plans DISCUSS this?" but is read as "how often do plans COMMIT this?" The remedy requires stating which half is being measured and never blending final-state and intermediate-revision counts into one accuracy figure. Target PLANNER_TEMPLATE.md for census/diagnostic authoring methodology.

### Entry 296 — Measure how many DIALECTS a record has (instrumentation)

**Category:** instrumentation | **Target:** DRAFTING_CYCLE.md | **Confidence:** high

A parser reported 36% of block-derived rows as unparseable because the corpus carried at least three distinct record forms. The entry prescribes a procedural instrumentation safeguard: count dialects before computing, make "unparseable" a reported outcome with the offending line attached (never a skip), and use structural probes for structural questions. Category instrumentation matches the tag's corpus precedent and the substance — a procedural safeguard for measurement tooling.

### Entry 297 — `pause_for_verdict: always` is unenforced (bellows-integration)

**Category:** governance_rule | **Target:** PLANNER_TEMPLATE.md | **Confidence:** high

An agent executed all three steps of a plan in one dispatch while `pause_for_verdict: always` was set. The header declares intent the runtime does not police. The most damaging cost: the QA step re-measured work by the same agent that produced it. The authoring-side remedy — compare the steps table against commits and deposits at every verdict gate — belongs in PLANNER_TEMPLATE.md. Rule 46 split: the runtime enforcement half is bellows-owned (FORWARD 46). **Mechanism named: steps-table vs commits/deposits comparison at every gate. Owner: bellows.**

### Entry 298 — Negative self-marked results and independence (verification)

**Category:** governance_rule | **Target:** PLANNER_TEMPLATE.md | **Confidence:** high

When a self-marking agent returns a result that demolishes the author's own prior work — zero true positives killing a pre-drafted build plan — the bias an independence check guards against (confirming what one hoped) is not the operative failure mode. A negative finding backed by re-checkable raw evidence and a spot-check that holds is worth accepting with the gap recorded. The rule applies directionally: positive self-marked findings remain low-value.

### Entry 299 — RECALL decides a check, not precision over survivors (measurement)

**Category:** governance_rule | **Target:** PLANNER_TEMPLATE.md | **Confidence:** high

A census scanned 1695 Done/ plans and 139 pre-fold commits but excluded both cycles that generated the hypothesis. The known positives existed only in the walk register, outside the scan population. Precision over a population with no positives is unfalsifiable. The remedy prescribes building the labelled positive set first, confirming known positives are inside the scan population, and reporting recall and precision as a pair. Category governance_rule because the entry prescribes a binding methodological rule about census design (measurement tag has zero corpus precedent; the substance is a prescriptive governance rule about diagnostic methodology — build labelled positive set first, report recall and precision as a pair, a disposition citing one without the other is incomplete).

### Entry 300 — Convergence by what findings TOUCH, not by origin (drafting-cycle)

**Category:** governance_rule | **Target:** DRAFTING_CYCLE.md | **Confidence:** high

The entry identifies §2's convergence criterion as self-contradictory: the origin-split percentage (fold-introduced vs pre-existing) serves as both the convergence condition and the noise-floor signature, and at 75% both readings apply. Steering by it cannot distinguish finishing from circling. The measured replacement: classify findings by what they change — instruction vs record/commentary. Walk 3 changed ten instructions; walk 4 changed two. The instruction surface had converged. Cluster (A) centerpiece — routes into the §2 doneness criterion rewrite. FORWARD 53.

### Entry 301 — A gate silenced by record retraction (mechanization)

**Category:** governance_rule | **Target:** DRAFTING_CYCLE.md | **Confidence:** high

A retraction under the attestation-integrity rule struck a status token, and the gate's WARN disappeared — the check matched the struck token inside the retraction. The edit touched only the record and changed only the gate's verdict, which is the exact signature §3 names for a log satisfying a check on the step's behalf. The doctrine-side remedy: describe tokens, never reproduce them. Rule 46 split: the automated WARN-set diff is bellows plan_lint-owned (FORWARD 50). Category governance_rule because the entry prescribes a record-authoring convention and a gate-integrity rule (mechanization tag has zero corpus precedent; the substance is a prescriptive governance rule about how records and gates interact — describe rather than reproduce, diff the WARN set after any record edit).

**Mechanism named: re-run the gate and diff the WARN set after any record edit. Owner: bellows plan_lint.**

### Entry 302 — Mandates drift from their observers (instruction-design)

**Category:** governance_rule | **Target:** PLANNER_TEMPLATE.md | **Confidence:** high

The same defect class — a mandate with no failing observer — appeared four times across three walks. Mandates live in the DEV step, observers in QA, so every new mandate starts unpaired and stays that way until a later reader notices. The remedy: name the QA item inline in the mandate, then construct the violation and confirm the item reports it. FORWARD 52. Category governance_rule because the entry prescribes an authoring convention for mandate–observer pairing (instruction-design tag has zero corpus precedent; the substance is a prescriptive plan-authoring rule requiring inline observer references and constructing the violation to confirm failure).

**Mechanism named: a lint check detecting mandates without inline observer references. Owner: authoring + lint.**

### Entry 303 — A mismatched literal probe returns false absence (verification)

**Category:** governance_rule | **Target:** DRAFTING_CYCLE.md | **Confidence:** high

Six grep -F probes in one session reported content as missing that was present — all on verification steps. The mechanism: the probe is composed from the author's memory of what they wrote rather than extracted from the target text. The gap is widest when checking one's own prior work. Five of six would have licensed a wrong action. The remedy: derive the probe from the target (open and copy), or enumerate what IS there. Sibling of entry 289.

### Entry 304 — The walk register is doctrine-ephemeral, practice-permanent (drafting-cycle)

**Category:** governance_rule | **Target:** DRAFTING_CYCLE.md | **Confidence:** high

§3 calls the register "session-local and ephemeral" while practice has committed three registers in one day into governance/knowledge/research/. The committed copy is what two separate pieces of work actually read — a census's labelled positive set and a plan's byte-level recovery. If the register does not survive the session, "move it to the register" is a deletion with extra steps. The remedy: treat the register as an output, commit per phase alongside the draft. FORWARD 51.

### Entry 305 — Per-string prohibition did not hold a structural hazard (bellows-integration)

**Category:** governance_rule | **Target:** DRAFTING_CYCLE.md | **Confidence:** high

The final step's span regex runs to end-of-file, so a trailing record block sits inside the QA step's gate span. The codified rule (describe, don't quote) fired four times in one walk despite existing. The geometric fix — placing records above the first step heading — worked where wording hardening did not. Rule 46 split: the bellows half is the _extract_step_text span regex fix (FORWARD 45). The doctrine half is the placement convention for §3.

**Mechanism named: bound the last step's gate span at a trailing record section. Owner: bellows _extract_step_text.**

### Entry 306 — Task paragraphs accrete until an agent acts on a subset (instruction-design)

**Category:** governance_rule | **Target:** PLANNER_TEMPLATE.md | **Confidence:** high

Every fold appends a sentence to the task it corrects; past some length the block becomes a passage and the agent executes part of it. Measured across two cycles — one diagnostic collapsed its Task C at ~900 words/8 instructions, and one walk later a fourth wall had re-formed under the freshly created sub-steps. The mechanism that builds walls — folds landing at the end of prose — survives the collapse. The remedy: author tasks as ordered sub-items from the first draft, and count instruction-bearing sentences per block. FORWARD 54. Category governance_rule because the entry prescribes a task-authoring convention (instruction-design tag has zero corpus precedent; the substance is a prescriptive authoring rule: ordered sub-items from the first draft, count instruction-bearing sentences per block).

**Mechanism named: a check counting instruction-bearing sentences per task block. Owner: plan_lint.**

---

## Whole-batch cluster synthesis update (all 41 entries, for Gate 1)

### Tag distribution (measured, all 41)

| Tag | Count | Expected | Match |
|-----|-------|----------|-------|
| `drafting-cycle` | 10 | 10 | YES |
| `verification` | 10 | 10 | YES |
| `process-discipline` | 5 | 5 | YES |
| `bellows-integration` | 3 | 3 | YES |
| `instruction-design` | 3 | 3 | YES |
| `instrumentation` | 3 | 3 | YES |
| `planner-discipline` | 2 | 2 | YES |
| `bellows-mechanics` | 1 | 1 | YES |
| `drafting` | 1 | 1 | YES |
| `measurement` | 1 | 1 | YES |
| `mechanization` | 1 | 1 | YES |
| `probe-integrity` | 1 | 1 | YES |

All 12 tags match expected counts exactly.

### Category distribution (all 41 proposals)

- governance_rule: 39
- instrumentation: 2 (proposals 294/entry 286, 304/entry 296 — both `instrumentation` tag)
- ambiguous: 0

### Target distribution (all 41 proposals)

- DRAFTING_CYCLE.md: 23
- PLANNER_TEMPLATE.md: 18

### Divergence tally (all three tranches)

**Total divergences: 4** (all on target_artifact, zero on category).

- Tranche A: 2 divergences
  - proposal 279 (entry 271): scouted `reference` (route, no file target) → set DRAFTING_CYCLE.md
  - proposal 284 (entry 276): scouted DRAFTING_CYCLE.md or PLANNER_TEMPLATE.md → set PLANNER_TEMPLATE.md
- Tranche B: 2 divergences
  - proposal 293 (entry 285): scouted DRAFTING_CYCLE.md §2.7 or PLANNER_TEMPLATE.md → set PLANNER_TEMPLATE.md
  - proposal 301 (entry 293): scouted routing principle (no file target) → set DRAFTING_CYCLE.md
- Tranche C: 0 divergences

### Flag status update

**(A) THE §2 DONENESS CLUSTER** — entries 267, 270, 284, 294, 300. All classified to DRAFTING_CYCLE.md (except 284 which classified to PLANNER_TEMPLATE.md for its test-authoring substance). Entry 300 (this tranche, cluster centerpiece) carries the measured replacement criterion: classify findings by what they touch (instruction vs record/commentary). Adjacent entries 268, 288 also classified to DRAFTING_CYCLE.md. Status: **intact, ready for Gate 1 as a routing unit**.

**(B) THE FORWARD-ROW CLUSTER** — entries 300→FORWARD 53, 301→FORWARD 50, 302→FORWARD 52, 304→FORWARD 51, 305→FORWARD 45, 306→FORWARD 54. All six in this tranche, all six disposition lines name their FORWARD row. Status: **complete, ready for Gate 1 reconciliation**.

**(C) RULE 46 CANDIDATES** — entries 266, 281, 297, 301, 305. All classified. Entries 297, 301, 305 (this tranche) carry the Rule 46 split in both disposition line and suggested_action, with the bellows-owned half named. Status: **complete**.

**(D) PARTIALLY OR FULLY CODIFIED BY v2.0** — entries 270, 275, 278, 284. All classified in tranches A and B. Status: **complete, Gate 1 measures clause-by-clause against live files**.

**(E) PRECEDENT-POOR TAGS** — 12 proposals across 6 zero-precedent tags + process-discipline. All carry the category-justifying reason in their disposition lines. Per-tag: `instruction-design` (3: proposals 291, 310, 314), `bellows-mechanics` (1: proposal 289), `probe-integrity` (1: proposal 290), `measurement` (1: proposal 307), `mechanization` (1: proposal 309), `process-discipline` (5: proposals 279, 280, 288, 299, 300). Status: **complete, precedent set**.

**(F) BATCH DESCRIBES THIS PLAN** — entries 269, 271, 291, 306. All classified without softening to match this plan's own practices. Status: **complete**.

**(G) MECHANISM-SHAPED ENTRIES** — 5 of the 9 core mechanism entries are in this tranche: 297 (bellows), 301 (bellows plan_lint), 302 (authoring + lint), 305 (bellows _extract_step_text), 306 (plan_lint). All carry `| remedy: mechanism | owner: <named>` in their disposition lines and name the mechanism in suggested_action. The other 4 from tranches A–B: 272/proposal 280 (unnamed), 283/proposal 291 (plan_lint or QA tooling), 286/proposal 294 (bellows deposit pipeline), 291/proposal 299 (plan_lint or authoring discipline). Total mechanism dispositions across all 41: **9**. Total discipline dispositions: **32**. Status: **complete, Gate 1 decides routing per entry 293's meta-rule**.
