# Classifications — Cycle 2026-08-03 (Plan 296)

16 entries ingested from LESSONS.md (session 16/17 batch), all classified in ascending id order per `get_unclassified_entries`.

## Cycle dict

```
ingested_count: 16
updated_count: 0
unchanged_count: 141
duplicates_marked_count: 0
needs_classification: [199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214]
terminal_proposals_flagged: []
cycle_timestamp: 2026-08-03T16:13:21.295544+00:00
```

## Tag distribution (measured)

- `planner-discipline`: 5 (entries 199, 200, 202, 205, 206)
- `bellows-integration`: 7 (entries 201, 203, 204, 207, 211, 212, 213)
- `drafting-cycle`: 2 (entries 208, 209)
- `verification`: 1 (entry 210)
- `process-discipline`: 1 (entry 214)

Matches expected 5/7/2/1/1.

## Category distribution (classified)

- `governance_rule`: 15 (proposals 207–221)
- `instrumentation`: 1 (proposal 222, entry 214)

## Classifications

### Proposal 207 — Entry 199

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md

**Source heading:** 2026-08-01: A COUNT is not a VALUE guard — trading one for the other passes every check and loses the capability

**Reasoning:** Entry demonstrates that a count-based guard is strictly weaker than a value-based one. A COUNT(*) WHERE route IS NOT NULL cannot see a row moving between two non-NULL values. The measured failure: flipping a row from one non-codify route to codify left the count at 70 and every surviving guard passing. The fix targets section 2.7's subtractive-trim verification guidance.

**Suggested action:** Extend DRAFTING_CYCLE.md section 2.7 to require that when a trim replaces a value-level assertion with a count, the subsumption must be verified by constructing the change the surviving check is supposed to catch and confirming it fails.

---

### Proposal 208 — Entry 200

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md

**Source heading:** 2026-08-01: Marking a claim as INHERITED makes it honest, not true — the reason for not re-running it is itself an unverified claim

**Reasoning:** Entry records a provenance convention applied correctly in form but violated in substance. A cold reader refuted the stated reason for not re-executing in one command. The lesson: a marker pointing at a false reason is worse than no marker. Targets section 2.7's attestation integrity.

**Suggested action:** Extend section 2.7 to require that before writing an INHERITED marker with a reason for not re-executing, the author must assess the literal cost of re-running the check.

---

### Proposal 209 — Entry 201

**Category:** governance_rule | **Confidence:** high | **Target:** PLANNER_TEMPLATE.md

**Source heading:** 2026-08-01: When something does not arrive, read the DELIVERY code before theorising about who dropped it

**Reasoning:** Same evidence was misdiagnosed three times; only reading bellows.py:1417 revealed the actual cause — the destination path did not exist. The entry proposes a general rule about diagnosing non-delivery. No existing rule is a clean fit; reads as a new rule near 55/62.

**Suggested action:** Add a new rule to PLANNER_TEMPLATE.md requiring that when a mechanism's output does not arrive, the delivery code must be read before theorising about the cause.

---

### Proposal 210 — Entry 202

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md

**Source heading:** 2026-08-01: Falling severity across walks is not convergence — ROTATION is

**Reasoning:** Convergence predicted from a falling curve was wrong twice. Walk 4 was the thinnest so far; walk 5 produced four MEDIUMs, every one in a previously unexamined region. Severity fell because the same regions were being re-read. The amendment targets the parenthetical gloss in section 2's doneness sentence. Must be merged with entry 208's amendment.

**Suggested action:** Amend section 2's doneness parenthetical and add a rotation qualifier: the signal for done is a walk aimed at a previously unexamined region coming back dry.

---

### Proposal 211 — Entry 203

**Category:** governance_rule | **Confidence:** high | **Target:** RULE_20_SELF_CHECK_BLOCK.md

**Source heading:** 2026-08-01: An annotated status cell passes BOTH gates while asserting nothing — a third verdict value is an invisible one

**Reasoning:** is_positive_row matches by cell equality, not substring, so an annotated cell escapes the hedging-keyword scan entirely while carrying no failure glyph for rule_22_verification either. The row is neither passing nor failing and both gates ignore it. Proposes a mechanizable lint; Gate 1 should determine whether this is a tooling request (Rule 46) or an authoring rule.

**Suggested action:** Extend the cell-equality contract in RULE_20_SELF_CHECK_BLOCK.md to document that the status cell holds exactly one token. Flag the proposed lint for Gate 1 decision.

---

### Proposal 212 — Entry 204

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md

**Source heading:** 2026-08-01: A guard's exit-code semantics must be EXECUTED against the failure it names, not the failure that inspired it

**Reasoning:** A rule built from one observed failure was inverted for the exact pattern class it named. On this machine (grep is a ugrep shim) a **-bearing pattern WITHOUT -F exits 1 silently on a file where the line is present. The corrected form: -F is mandatory and a search not run with -F is invalid evidence regardless of exit code. Targets section 2.7's command-output evidence guidance.

**Suggested action:** Extend section 2.7 to require grep -F unconditionally for literal-string searches, forbidding the unsafe invocation outright.

---

### Proposal 213 — Entry 205

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md

**Source heading:** 2026-08-01: The edit phase manufactures defects even when the edit is a REPAIR — and a ledger records that rather than preventing it

**Reasoning:** Six ACID passes each found defects from the preceding culmination, including repair-purpose culminations. Two were re-violations of the plan's own Conflict Ledger entries. The ledger records constraints correctly without preventing their re-violation — the asymmetry is the argument for mechanizing constraints rather than documenting them. Targets section 2.8's ledger management.

**Suggested action:** Extend section 2.8 to document the ledger's limits and require re-running the mechanical check on the touched region after any fold.

---

### Proposal 214 — Entry 206

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md

**Source heading:** 2026-08-01: Aim the cold panel at the premises that LICENSE a deletion — that is where the author has already convinced themselves

**Reasoning:** Five warm walks and six ACID passes missed two premise failures that a cold panel found, because all three concerned justifications the author had already accepted — warm passes re-read the reasoning while cold readers tested it. Clean placement as a targeting rule for section 2.6.

**Suggested action:** Append a cold-panel targeting rule to section 2.6: hand cold readers the deletion premises explicitly and ask them to falsify each against live data.

---

### Proposal 215 — Entry 207

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md

**Source heading:** 2026-08-01: A true warning silenced by wording is not a cleared warning — re-run the check after every edit to the block it reads

**Reasoning:** A correct plan_lint WARN was silenced four separate times, always by wording and never by the condition changing. Section 3 (shipped by plan 291 from proposal 206) already carries the three core claims. Three sub-claims are absent: earned-phrasing is necessary-but-not-sufficient; the trigger is every edit to the block the check reads, not only compaction; the prohibition applies reflexively. This is a scoped extension.

**Suggested action:** Extend section 3 with the three absent sub-claims: necessary-but-not-sufficient, broader trigger scope, and reflexive application.

---

### Proposal 216 — Entry 208

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md

**Source heading:** 2026-08-03: The cold panel's yield does not decay, and a third of it is the previous round's folds

**Reasoning (tag: `drafting-cycle` — no corpus precedent, category from substance):** Entry provides the measurement: "A five-lens sequential cold panel on one plan returned 11 / 12 / 12 / 12 / 12 findings — 59 total, no decay across rounds." The cause is structural: "roughly a third of each round's findings were defects introduced by the immediately preceding round's folds." This falsifies the falling-curve convergence assumption. Classified as governance_rule because the fix is a documentary amendment to section 2's doneness sentence and section 2.6's panel guidance — the same artifacts that carry existing governance rules about cold-panel practice. Must be merged with entry 202's amendment as a single edit.

**Suggested action:** Amend section 2's parenthetical (merged with entry 202) and add to section 2.6: budget for the panel's yield staying flat.

---

### Proposal 217 — Entry 209

**Category:** governance_rule | **Confidence:** high | **Target:** DRAFTING_CYCLE.md

**Source heading:** 2026-08-03: Seven folds on one region is not a patching problem, it is evidence for deletion

**Reasoning (tag: `drafting-cycle` — no corpus precedent, category from substance):** Entry traces seven findings landing on one region, where "Every individual patch was correct. The region kept producing defects anyway." It was deleted and replaced with a fail-closed check that "removed four of the open findings at once, and the plan shrank while gaining guards." Classified as governance_rule because the fix requires documentary edits to two sections of DRAFTING_CYCLE.md: section 2.8 (add the counting method — folds per REGION not per plan) and section 2.6 (add the inverse question about shipped siblings that already deleted the same machinery). This splits across two sections within the same target artifact.

**Suggested action:** Extend section 2.8 with per-region fold counting and section 2.6 with the shipped-sibling deletion check.

---

### Proposal 218 — Entry 210

**Category:** governance_rule | **Confidence:** high | **Target:** PLANNER_TEMPLATE.md

**Source heading:** 2026-08-03: A verification that tests something adjacent to the change can certify a fold that never landed

**Reasoning (tag: `verification` — no corpus precedent, category from substance):** Entry catalogues eight marker-based verification failures, all caused by patterns scoped to something adjacent rather than to the measured change. Two reported a fold as applied when the file was unchanged: a retention check that grepped for the defect's text to confirm removal, and a batch replacement that counted on the match condition rather than on the file changing. Classified as governance_rule because the fix is a documentary extension of Checklist #32's observed-delta rule in PLANNER_TEMPLATE.md — a governance-level authoring standard for how verification assertions must be scoped.

**Suggested action:** Extend Checklist #32 with the verification-instrument form: assert on the POST-condition, not on the presence of the thing being changed.

---

### Proposal 219 — Entry 211

**Category:** governance_rule | **Confidence:** high | **Target:** PLANNER_TEMPLATE.md

**Source heading:** 2026-08-03: A note-shaped verification row cannot live in a glyph-required table

**Reasoning:** Entry records that a plan specified a row as a reconcile-note, the QA agent wrote NOTE in the status column, and rule_22_verification failed the gate because it requires a pass/fail glyph. The agent did nothing wrong; the plan created a row whose answer the gate cannot express. The fix is an authoring rule about what belongs in the verification table, targeting Rule 17. No Family line in this entry.

**Suggested action:** Extend Rule 17 to state that a note-shaped row belongs outside the verification table or must carry a glyph with nuance in the evidence column.

---

### Proposal 220 — Entry 212

**Category:** governance_rule | **Confidence:** high | **Target:** PLANNER_TEMPLATE.md

**Source heading:** 2026-08-03: A command containing a pipe cannot be quoted verbatim inside a markdown table cell

**Reasoning:** Entry traces a silent failure: escaping a pipe to \| in a table cell changed ERE alternation to a literal pipe, matching nothing. The agent reported "no daemon is running" while the daemon was running. The plan's pattern was correct until the table cell rewrote its semantics. The fix is a command-quoting rule near Rules 17/18.

**Suggested action:** Add to Rule 18 (or as a new rule near 17/18) that a pipe-bearing command must never be placed in a markdown table cell.

---

### Proposal 221 — Entry 213

**Category:** governance_rule | **Confidence:** high | **Target:** PLANNER_TEMPLATE.md

**Source heading:** 2026-08-03: Daemon liveness is `ps -p` against a recorded PID, not a pgrep pattern

**Reasoning:** Three separate pgrep failures within two hours, all sharing one property: "pgrep returns exit 1 for 'no match', which is indistinguishable from 'not running' — so every failure mode presents as the answer 'the daemon is down.'" This is Rule 55(a)'s thesis (assert on a positive signal, never merely empty output) applied to process state. The fix extends 55(a) into a second domain. No Family line in this entry.

**Suggested action:** Extend Rule 55(a) into the process-state domain: use ps -p against a recorded PID, not pgrep pattern matching.

---

### Proposal 222 — Entry 214

**Category:** instrumentation | **Confidence:** high | **Target:** PLANNER_TEMPLATE.md

**Source heading:** 2026-08-03: A post-activation live canary can be paid for by the backlog it records

**Reasoning (tag: `process-discipline` — one prior entry id 134, classified instrumentation):** Entry describes a canary pattern where real pending work served as the payload: "the canary's payload was the two real deferred items still owed to that project's register. The measurement that proved the mechanism (26 to 28 rows, one row per bullet, two distinct items) also emptied the queue the mechanism exists to serve." The entry names itself as "the constructive form of the Checklist #32 / Workaround #15 discipline." Classified as instrumentation (not governance_rule) because it describes a concrete procedural safeguard — a canary design pattern — following the parent entry 134's instrumentation classification for the same process-discipline tag. The fix adds canary-design guidance to a checklist (a new procedural mechanism extending an existing checklist item), not a documentary rule change.

**Suggested action:** Add canary-design guidance to Checklist #32: use real pending work as the canary payload and pair the live observation with an in-process prediction.

---

## Cluster synthesis for Gate 1

16 entries from the session-16/17 cycles — 5 planner-discipline authoring refinements, 7 bellows-integration mechanics findings, 2 drafting-cycle measurements, 1 verification-instrument finding, 1 process-discipline canary pattern; MIXED targets across 3 artifacts (DRAFTING_CYCLE.md, PLANNER_TEMPLATE.md, RULE_20_SELF_CHECK_BLOCK.md); TWO entries (207, 209) MEASURED as partially codified already by plan 291, both routing as scoped extensions rather than reference, with 209 splitting across two sections; ONE surgical section 2 amendment (entries 202/208 vs the doneness sentence's parenthetical gloss, NOT its criterion) that Gate 2 must apply as a single merged edit; and THREE tag values the corpus has never classified before (drafting-cycle, verification, process-discipline).

Entries 203, 211 and 212 all govern what may occupy a cell of the QA verification table, sent to three different homes (RULE_20_SELF_CHECK_BLOCK.md, Rule 17, Rule 18). Gate 2 should weigh a single consolidated cell-contract clause against three surgical edits.

Entry 214 classified as instrumentation (the only non-governance_rule in this batch), following parent entry 134's precedent for the process-discipline tag.

## Ambiguous entries

None. All 16 classified with high confidence.
