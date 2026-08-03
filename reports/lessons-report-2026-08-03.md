# Lessons Report — 2026-08-03


## Summary


| Category | Count |
|---|---|
| governance_rule | 15 |
| instrumentation | 1 |

**Total proposals:** 16


## Governance Rule


### 2026-08-03: The cold panel's yield does not decay, and a third of it is the previous round's folds [tag: drafting-cycle]


- **Suggested action:** Amend DRAFTING_CYCLE.md section 2's doneness parenthetical (merged with entry 202's amendment) and add to section 2.6: do not treat a falling finding-count as the convergence signal; budget for the panel's yield staying flat. The signal is a dry pass aimed at a region the previous round did not touch.
- **Reasoning:** Entry 208 provides the measurement falsifying the falling-curve convergence assumption: "A five-lens sequential cold panel on one plan returned 11 / 12 / 12 / 12 / 12 findings — 59 total, no decay across rounds." The cause is structural: "roughly a third of each round's findings were defects introduced by the immediately preceding round's folds. Every fold is an unreviewed edit, so folding N findings creates a fresh unreviewed surface of N edits." This entry and entry 202 both target the same parenthetical gloss in section 2; Gate 2 must merge them as a single edit.
- **Confidence:** high

### 2026-08-03: Seven folds on one region is not a patching problem, it is evidence for deletion [tag: drafting-cycle]


- **Suggested action:** Extend DRAFTING_CYCLE.md in two sections: (1) section 2.8 — add that folds should be counted per REGION not per plan, since a per-plan count hides region-level accumulation; (2) section 2.6 — add the inverse question to the existing clone-against-newest guidance: check whether a shipped sibling already DELETED the same machinery, since a 'do not re-add' note in a Done/ plan is invisible unless someone diffs against it.
- **Reasoning:** Entry 209 traces seven findings landing on one region across four rounds, where "Every individual patch was correct. The region kept producing defects anyway." The region was deleted and replaced with a simpler fail-closed check, which "removed four of the open findings at once, and the plan shrank while gaining guards." Section 2.8 already carries the core claims but lacks the counting method; the sibling-check half targets section 2.6 and is the inverse of its current question: "The newest same-class shipped plan had already resolved the identical problem the same way and carried a note telling clones not to re-add the machinery; the clone re-added it anyway."
- **Confidence:** high

### 2026-08-03: A verification that tests something adjacent to the change can certify a fold that never landed [tag: verification]


- **Suggested action:** Extend PLANNER_TEMPLATE.md Checklist #32 (observed-delta rule) with the verification-instrument form: a check must assert on the POST-condition, never on the presence of the thing being changed. Any scripted edit must assert after != before, not merely that an anchor matched.
- **Reasoning:** Entry 210 catalogues eight marker-based verification failures from one session, all caused by patterns chosen for convenience rather than scoped to the measured change. Two failures are the starkest: "A retention check grepped for the DEFECT's own text (checkout HEAD -- ...) to confirm the defect had been REMOVED, and reported OK on its continued presence" and "A batch replacement incremented its success counter on the match condition rather than on the replacement changing the file, printing 'applied 2/2' for one edit that silently did nothing." Checklist #32's observed-delta rule is the natural home for this verification-instrument form.
- **Confidence:** high

### 2026-08-03: A note-shaped verification row cannot live in a glyph-required table [tag: bellows-integration]


- **Suggested action:** Extend PLANNER_TEMPLATE.md Rule 17 (verification table format) to state that a row whose honest disposition is 'note' belongs outside the verification table — deciding a row is note-shaped is a signal to move it, not to write NOTE into a table the gate parses.
- **Reasoning:** Entry 211 records that a plan specified a QA row as a reconcile-note and the agent wrote NOTE in the status column, which "rule_22_verification then failed the gate, because it requires every verification-table row to carry a pass/fail glyph. The agent did nothing wrong; the plan created a row whose correct answer the gate cannot express." The fix is an authoring rule about what belongs in the verification table, which Rule 17 (governing table format and the Status column) is the natural home for.
- **Confidence:** high

### 2026-08-03: A command containing a pipe cannot be quoted verbatim inside a markdown table cell [tag: bellows-integration]


- **Suggested action:** Add to PLANNER_TEMPLATE.md Rule 18 (or as a new rule near 17/18) that a command containing a pipe character must never be placed in a markdown table cell — put it in a fenced block above the table and have the row cite its result. A delimiter-bearing command inside a delimiter-structured document is a collision where escaping changes the semantics.
- **Reasoning:** Entry 212 traces a silent failure: a QA step was told to run a pgrep command with pipe alternation in a verification table cell. "To survive the pipe-delimited cell, the agent escaped the pipe to \| — which in ERE stops being alternation and becomes a literal pipe character, matching nothing. The agent reported 'no daemon is running' while the daemon was running." The breakage is silent — pgrep exits 1 for both 'no match' and 'not running' — and the plan's pattern was correct until the table cell rewrote its semantics.
- **Confidence:** high

### 2026-08-03: Daemon liveness is `ps -p` against a recorded PID, not a pgrep pattern [tag: bellows-integration]


- **Suggested action:** Extend PLANNER_TEMPLATE.md Rule 55(a) (assert on a positive signal) into the process-state domain: daemon liveness should be checked with ps -p against a recorded PID, not with pgrep pattern matching. If a pattern must be used, require a positive confirmation (a PID that then resolves) rather than treating an empty result as an answer.
- **Reasoning:** Entry 213 documents three separate pgrep failures within two hours, all sharing one property: "pgrep returns exit 1 for 'no match', which is indistinguishable from 'not running' — so every failure mode presents as the answer 'the daemon is down.'" This is Rule 55(a)'s thesis ("assert on a positive signal, never merely empty output, which absence also produces") applied to process state rather than repo/tree state. The entry's fix — record the PID and check with ps -p — is the process-state analogue of Rule 55(a)'s file/tree guidance.
- **Confidence:** high

### 2026-08-01: A COUNT is not a VALUE guard — trading one for the other passes every check and loses the capability [tag: planner-discipline]


- **Suggested action:** Extend DRAFTING_CYCLE.md section 2.7 (subtractive-trim verification) to require that when a trim replaces a value-level assertion with a count over the same scope, the subsumption must be verified against live data by constructing the change the surviving check is supposed to catch and confirming it fails.
- **Reasoning:** Entry 199 demonstrates that a count-based guard is strictly weaker than a value-based one: "A COUNT(*) WHERE route IS NOT NULL cannot see a row moving between two non-NULL values." The entry traces a concrete failure where "flipping any one of them to codify left the count at 70 and every surviving guard passing" — proving the capability loss. The fix is a documentary rule change to the subtractive-trim verification guidance in section 2.7, which already covers per-item verification of trims.
- **Confidence:** high

### 2026-08-01: Marking a claim as INHERITED makes it honest, not true — the reason for not re-running it is itself an unverified claim [tag: planner-discipline]


- **Suggested action:** Extend DRAFTING_CYCLE.md section 2.7 (lens attestation integrity) to require that before writing an INHERITED marker with a reason for not re-executing, the author must assess the literal cost of re-running the check, since most 'impractical to test' reasons dissolve into a copy plus one command.
- **Reasoning:** Entry 200 records that a provenance convention was applied correctly in form but violated in substance: "The plan stated that reproducing a sidecar-absent SQLite DB 'would require removing the live production DB's WAL sidecars, which is not an acceptable thing to do to verify a documentation point.' A cp does not copy WAL sidecars." A cold reader reproduced the condition in one command. The fix is an attestation-integrity rule: a marker pointing at a false reason is worse than no marker.
- **Confidence:** high

### 2026-08-01: When something does not arrive, read the DELIVERY code before theorising about who dropped it [tag: bellows-integration]


- **Suggested action:** Add a new rule to PLANNER_TEMPLATE.md (near Rules 55/62) requiring that when a mechanism's output does not arrive, the delivery code must be read before theorising about the cause — non-arrival has at least three candidate causes (never sent, sent-and-lost, sent to an unconfigured destination) and only the delivering code distinguishes them.
- **Reasoning:** Entry 201 describes the same evidence being misdiagnosed three times: the prior plan was blamed for not emitting a block, then the daemon was blamed, but the actual cause was "bellows.py:1417 resolves the destination to <this plan's project>/knowledge/FORWARD.md, which for lessons-forge does not exist, so it logs 'no FORWARD.md in project, skipping forward append' and returns." A reading from the code was the only correct diagnosis. The lesson proposes a general rule about diagnosing non-delivery.
- **Confidence:** high

### 2026-08-01: Falling severity across walks is not convergence — ROTATION is [tag: planner-discipline]


- **Suggested action:** Amend DRAFTING_CYCLE.md section 2's doneness sentence to replace the parenthetical gloss equating the diminishing-returns signal with falling counts. Add a rotation qualifier: the signal for done is a walk aimed at a previously unexamined region coming back dry, not successive quieter walks over covered ground.
- **Reasoning:** Entry 202 falsifies the falling-curve reading of convergence with a concrete measurement: "Walk 4 was the thinnest walk to that point (one MEDIUM, six verified negatives) and was reported as the diminishing-returns signal; walk 5 then produced four MEDIUMs, every one in a region no prior walk had aimed at." The entry traces the cause: "Severity fell because the same regions were being re-read, not because the artifact was sound." The amendment is surgical — the main clause of section 2's criterion is correct; the parenthetical gloss is what these measurements falsify.
- **Confidence:** high

### 2026-08-01: An annotated status cell passes BOTH gates while asserting nothing — a third verdict value is an invisible one [tag: bellows-integration]


- **Suggested action:** Extend the cell-equality contract in RULE_20_SELF_CHECK_BLOCK.md to document that the status cell holds exactly one token and nothing else — an annotated cell escapes both gates. Additionally flag the proposed mechanizable lint (every status cell is exactly one of the two permitted tokens) as a question for Gate 1: is this a tooling request or an authoring rule?
- **Reasoning:** Entry 203 identifies a gap in the gate contract: "is_positive_row matches positive-status tokens by cell equality, not substring, so an annotated cell is not a positive row at all — it escapes the hedging-keyword scan entirely — while carrying no failure glyph for _gate_rule_22_verification either. The row would be neither passing nor failing, and both gates would ignore it." The fix is an authoring rule (one token per cell) rather than a gate logic change, and the entry proposes a mechanizable lint.
- **Confidence:** high

### 2026-08-01: A guard's exit-code semantics must be EXECUTED against the failure it names, not the failure that inspired it [tag: bellows-integration]


- **Suggested action:** Extend DRAFTING_CYCLE.md section 2.7 (command-output evidence) to require that all literal-string searches use grep -F unconditionally, and that a search not run with -F is invalid evidence regardless of exit code. Forbid the unsafe invocation outright rather than encoding exit-code interpretation rules.
- **Reasoning:** Entry 204 demonstrates that a rule built from one observed failure was inverted for the exact pattern class it named: "a **-bearing pattern run WITHOUT -F exits 1, silently, on a file where the searched line is present — the code the rule whitelisted as 'absent'." The corrected form is unconditional: "-F is mandatory, and a search not run with -F is invalid evidence regardless of its exit code." The entry traces the root cause to deriving a rule from a single instance without executing it against the governing case.
- **Confidence:** high

### 2026-08-01: The edit phase manufactures defects even when the edit is a REPAIR — and a ledger records that rather than preventing it [tag: planner-discipline]


- **Suggested action:** Extend DRAFTING_CYCLE.md section 2.8 to document the ledger's limits: a Conflict Ledger records constraints correctly without preventing their re-violation during the edit phase. Add that after any fold, the mechanical check that reads the touched region must be re-run, and cite the ledger's record-without-prevent asymmetry as evidence for mechanizing constraints rather than only documenting them.
- **Reasoning:** Entry 205 measures the edit-phase defect rate across six ACID passes: "Every one found defects introduced by the culmination immediately before it, including culminations whose entire purpose was repairing defects." Two of the violations were re-violations of the plan's own Conflict Ledger entries. The entry identifies the asymmetry: "a ledger that records its own violations without preventing them" is the argument for mechanizing a constraint. This extends section 2.8's existing guidance on ledger management.
- **Confidence:** high

### 2026-08-01: Aim the cold panel at the premises that LICENSE a deletion — that is where the author has already convinced themselves [tag: planner-discipline]


- **Suggested action:** Append a cold-panel targeting rule to DRAFTING_CYCLE.md section 2.6: hand cold readers the deletion premises explicitly and ask them to falsify each against live data. A premise licensing a removal is the highest-value target, especially in a 'proven clone' framing where the clone's deletions are where its judgement diverges from its shipped parent.
- **Reasoning:** Entry 206 records that five warm walks and six ACID passes missed two premise failures that a five-round cold panel found: "(a) the blast-radius premise was false against live data (a count cannot see a value change); (b) the reason given for not re-executing an inherited claim was false and refuted in one command." The entry traces why: "All three concerned justifications the author had already accepted. Warm passes re-read the reasoning; the cold readers tested it." Clean placement as a targeting rule for section 2.6.
- **Confidence:** high

### 2026-08-01: A true warning silenced by wording is not a cleared warning — re-run the check after every edit to the block it reads [tag: bellows-integration]


- **Suggested action:** Extend DRAFTING_CYCLE.md section 3 with three absent sub-claims from this entry: (1) phrasing a check-satisfying line so it cannot match until earned is necessary but not sufficient; (2) the trigger is every edit to the block the check reads, not only compaction; (3) the prohibition against quoting gate-matching tokens applies reflexively — including in the sentence that warns against quoting them.
- **Reasoning:** Entry 207 documents four separate silencings of a correct plan_lint WARN, "always by wording and never by the condition changing." The entry's three core claims are already present in section 3 (shipped by plan 291 from proposal 206), but three sub-claims are absent: the necessary-but-not-sufficient qualification, the broader trigger scope ("every edit to the block it reads" vs only compaction), and the reflexive application of the prohibition. This is a scoped extension, not a clean-slate codification.
- **Confidence:** high

## Instrumentation


### 2026-08-03: A post-activation live canary can be paid for by the backlog it records [tag: process-discipline]


- **Suggested action:** Add canary-design guidance to PLANNER_TEMPLATE.md Checklist #32: when a canary is owed, use real pending work as its payload rather than a synthetic probe. Pair the live observation with an in-process prediction of the same value so that agreement proves the path while disagreement localises the fault.
- **Reasoning:** Entry 214 describes a canary pattern where "the canary's payload was the two real deferred items still owed to that project's register. The measurement that proved the mechanism (26 to 28 rows, one row per bullet, two distinct items) also emptied the queue the mechanism exists to serve." The entry explicitly names itself as "the constructive form of the Checklist #32 / Workaround #15 discipline" and proposes pairing a live observation with an in-process prediction. This is a new procedural safeguard extending an existing checklist item, following the parent entry 134's instrumentation classification for the same process-discipline tag.
- **Confidence:** high
