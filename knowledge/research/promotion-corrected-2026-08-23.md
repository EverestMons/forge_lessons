# Corrected Learned Promotion Set — 2026-08-23

**Diagnostic:** 504 — CORRECTIVE to 503. Settle the `learned` promotion set by stating the two rules 503 left implicit and re-deriving the set against 503's own classifications.

**Corpus identity:** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — 1,593,344 bytes, `lesson_entries` = 370 rows (confirmed via `sqlite3 "file:...?immutable=1"`).

**Symbol table verification:** N=327, X=239, D6=370. All confirmed via grep / sqlite3 against live files.

---

## Q1 — Reproduce the defect

### Sets derived from 503's Q2 mapping

**A (candidates mapped to a demonstrated mechanism, [learned]):** 22 distinct corpus ids.

**F (FULLY enforced, [learned]):** 16 entries.
98, 106, 61, 85, 90, 70, 191, 120, 184, 231, 111, 89, 119, 140, 142, 340.

**R (PARTLY enforced, [learned]):** 6 entries.
109, 96, 121, 62, 114, 339.

A = F + R = 16 + 6 = 22.

**V (distinct entries in 503's deposited TSV):** 19 entries.
98, 106, 61, 85, 90, 70, 191, 120, 184, 231, 111, 89, 119, 140, 142, 340, 96, 121, 109.
Confirmed: `awk -F'\t' 'NR>1{print $1}' learned-promotion-2026-08-23.tsv | sort -u | wc -l` → 19.

**V = F + exactly three of R.**
Promoted R entries (in V): 109, 96, 121.
Demoted R entries (not in V): 62, 114, 339.

**Does 503 give ANY basis for this split?** No. 503's Q4 says "Only entries mapped to a DEMONSTRATED mechanism may be promoted" — but ALL six R entries are mapped to DEMONSTRATED mechanisms. The FULLY/PARTLY classification is about coverage, not about demonstration status. 503's Q2 instruction says "a lesson only partly enforced is not completion," and its Q4 silently overrides that instruction for three of six PARTLY entries without stating why. The Q4 set arithmetic (demote X, promote the set) never distinguishes between FULLY and PARTLY — it references "this plan's DEMONSTRATED set" as a monolith. **There is no stated basis for including {109, 96, 121} while excluding {62, 114, 339}.**

503's prose figure of 15 distinct entries (Q4 text) disagrees with the TSV's actual 19. The TSV is right about its own contents. Neither figure is the concern — the concern is that the set corresponds to no class 503 defines.

### W entries — pending but FULLY enforced

503's Q2 mapped two entries by LINE rather than by corpus id, both tagged `[pending]` and classified FULLY:

| Line | Heading | Corpus ID | Status | Mechanism | Coverage |
|------|---------|-----------|--------|-----------|----------|
| 1130 | Rule 22 (d) hedging-keyword detector false-positive on domain terminology | 83 | [pending] | `_gate_rule_22_verification` (G7) | FULLY |
| 4599 | A function that computes a LOOKUP KEY must be the identity | (not ingested) | [pending] | `test_key_heading_annotated_matches_unannotated` (T1) | FULLY |

503's Q4 excluded both by scoping the promotion set to entries already labelled `learned`. Under the CEO's ruling that scoping is backwards — `learned` means a mechanism enforces the rule, not that the entry was previously guessed to be finished — both are candidates.

Entry at line 4599 has no corpus id: the latest ingested entry is id 370 (dated 2026-08-19); this lesson is from 2026-08-22 and has not been ingested. Its mechanism (T1) was ASSERTED in 503 (A2–A8), not DEMONSTRATED. These are two separate issues: the classification rules (Q2–Q3 below) determine whether it SHOULD be promoted; the corpus gap and the ASSERTED status determine whether it CAN be applied by the executable today.

### Entries not re-opened

The 217 entries in X (=239) that 503 mapped to NO demonstrated mechanism are not candidates. They had no mechanism at all and this plan does not supply one. This is "not a candidate," not "considered and rejected."

---

## Q2 — RULE ONE: Does PARTLY count as completion?

503's Q2 instruction: "a lesson only partly enforced is not completion." That instruction was folded into 503 at walk 1, before it ran, specifically to stop a partial mechanism reading as completion. The rule was intended and stated; what failed was applying it. Below, each R entry is tested against the lesson body (from LESSONS.md), not just the heading.

### Entry 109 — "Strict Bellows convention strings must be copied from a known-good artifact, never authored from memory" (line 227)
**Mechanism:** `_gate_rule_20_self_check` (G6) + `plan_lint (c)`.
**What the mechanism covers:** Item 2 of three failures: the QA Rule 20 banner string. G6 rejects reports without the canonical banner/PASSED pair; plan_lint(c) rejects plans missing the banner strings.
**What the mechanism does NOT cover:** (1) Plan header field-line position (item 1) — the lesson documents a header shape failure that `_parse_plan_header` catches, NOT G6 or plan_lint(c). (2) Deposits block format `**Deposits:**` vs `### Deposits` (item 3) — caught by `_extract_plan_required_deposits`, not by G6 or plan_lint(c). Two of three failure modes are entirely outside the demonstrated mechanism's scope.
**Verdict:** Substantively partial. Not completion.

### Entry 96 — "A QA 'full suite passes' headline is the least independently-verifiable claim" (line 17)
**Mechanism:** `_gate_rule_22_verification` (G7).
**What the mechanism covers:** Hedging keywords in QA verification tables. G7 catches phrases like "should pass" or "pending" in positive-status rows.
**What the mechanism does NOT cover:** The lesson's core rule: that a full-suite pass-count "rests on a single long run nobody observed and cannot be reconstructed from the report." G7 cannot tell whether a test run was observed or reproduced. It catches hedging LANGUAGE about the claim but cannot catch a faithfully-reported-but-unverifiable claim. The lesson says "treat the headline full-suite count as provisional until reproduced under a watched, wall-clock-bounded run" — G7 enforces none of that.
**Verdict:** Substantively partial. Not completion.

### Entry 121 — "Run the FULL test suite during DEV and Planner review — Bellows gates do not include suite-green" (line 1443)
**Mechanism:** `_gate_qa_test_result` (G8).
**What the mechanism covers:** Test failures exceeding `known_failures` threshold on QA steps.
**What the mechanism does NOT cover:** The lesson says "DEV self-verify and Planner review must each run `pytest tests/`" — G8 runs on QA steps only, not on DEV steps or Planner review. The lesson's core claim is that "a plan can close with failing tests if no one runs the suite" during DEV — G8 closes the gap at QA time but the DEV/Planner gap remains exactly as the lesson describes.
**Verdict:** Substantively partial. Not completion.

### Entry 62 — "scope_check trip identified the WRONG file in CEO context" (line 581)
**Mechanism:** `_gate_scope_check` (G9).
**What the mechanism covers:** Out-of-scope file detection.
**What the mechanism does NOT cover:** The lesson is about HUMAN misinterpretation of scope_check's output — the CEO misidentified which file was flagged because multiple artifacts share a slug. scope_check fired correctly; the lesson is about reading the Files Changed list literally before authoring a diagnostic. The mechanism cannot prevent misreading its own output.
**Verdict:** Substantively partial. Not completion.

### Entry 114 — "Non-monotonic STEP header labels cause positional/literal misalignment" (line 394)
**Mechanism:** `plan_lint (e)`.
**What the mechanism covers:** Step heading case — rejects `## Step N` (lowercase) in favor of `## STEP N` (uppercase).
**What the mechanism does NOT cover:** The lesson is about non-monotonic numbering (`2A`, `2B`), not about case. L-e checks case; the lesson is about the daemon's positional indexing vs. the agent's literal lookup when headers are numbered non-monotonically. A plan with `## STEP 2A` passes L-e (correct case) but triggers the exact failure the lesson describes.
**Verdict:** Substantively partial. Not completion.

### Entry 339 — "A fold is the only edit in the system with no post-condition" (line 4077)
**Mechanism:** `fold_check.py` (S3).
**What the mechanism covers:** Machine-readable state drift after a fold — diffs plan_lint/propagation_check/etc. results before and after.
**What the mechanism does NOT cover:** The lesson's scope is broader: "six rules govern it and all six key on the wrong unit." fold_check addresses one post-condition (machine-readable state unchanged). The lesson describes five additional rules that fail: re-run the finding lens on its own fix; enumerate applicable sites before applying; sweep record lines; re-verify factual claims; diff reclassifying folds. These five are unchecked by fold_check.
**Verdict:** Substantively partial. Not completion.

### Summary

All six R entries are substantively partial. None is trivially or immaterially partial. In every case, the mechanism leaves a material part of the lesson's scope uncovered.

**Is PARTLY a third state or is it codified?** It is `codified`. 503's own Q2 instruction stated this correctly: "a lesson only partly enforced is not completion." The six cases bear this out — in each, the gap between what the mechanism catches and what the lesson teaches is substantive and material, not a technicality. A PARTLY-enforced lesson's mechanism catches SOME violations but allows the core failure the lesson documents. That is `codified` — the lesson has a mechanism, but the mechanism does not complete the rule.

---

## Q3 — RULE TWO: Can a mechanism enforce a lesson about that mechanism's own insufficiency?

### The discriminator

For each (entry, mechanism) pair, the question is: **does the demonstrated mechanism REJECT A VIOLATION OF THIS LESSON, or is the mechanism merely the lesson's SUBJECT MATTER?**

A lesson is circular with respect to a mechanism when:
- The lesson describes the mechanism's behavior, semantics, failure modes, or insufficiency.
- The mechanism fires for its own reasons, independent of whether the lesson was ever written.
- Demonstrating the mechanism firing proves the mechanism works — it does NOT prove that the lesson's teaching is enforced.

The inverse — NOT circular — is when:
- The lesson teaches an authoring practice or operational rule.
- The mechanism rejects violations of that practice (incorrect inputs, missing outputs, format errors).
- Without the mechanism, violations of the lesson would succeed silently.

### Systematic pass over all candidates

**Entry 98 — Name deposit file paths literally.**
Mechanisms: G5, G9. The lesson teaches plan authors to name deposit paths explicitly. G5 rejects missing deposits; G9 rejects out-of-scope files. Both reject violations of the authoring practice. **Not circular.**

**Entry 106 — scope_check false-positive on plan-required evidence files.**
Mechanism: G9. The lesson describes scope_check's false-positive behavior and says Planner override is the right response. G9 IS the lesson's subject — the lesson exists because G9 fires incorrectly. Demonstrating G9 on a real out-of-scope file shows G9 works; it does not show that the lesson about G9's false positives is enforced. The lesson teaches HUMAN response to G9's behavior; G9 cannot enforce that. **CIRCULAR.**

**Entry 61 — Inline Deposits blocks silently fail.**
Mechanism: G5. The lesson teaches the correct Deposits block format. G5 rejects plans with unparseable or missing deposits. **Not circular.**

**Entry 85 — QA-step deposits blocks must declare exactly one .md.**
Mechanism: G5. Same analysis as 61. **Not circular.**

**Entry 90 — Use Deposits blocks for ALL agent deposits.**
Mechanism: G5. Same analysis as 61. **Not circular.**

**Entry 70 — QA-step prompts must reference RULE_20_SELF_CHECK_BLOCK.md.**
Mechanisms: G6, plan_lint(c). The lesson teaches authors to reference the canonical block. G6 rejects reports without the banner; plan_lint(c) rejects plans without the banner strings. Both reject violations of the authoring rule. **Not circular.**

**Entry 191 — An honest QA failure passes the Rule 20 self-check.**
Mechanism: G6. The lesson describes G6's semantics — specifically that PASSED does not mean QA passed, only that the self-check's evidence and hedging checks passed. The lesson IS about what G6 does and does not verify. Demonstrating G6 shows G6 works; it does not enforce understanding of G6's semantics. 503 itself noted this entry was "FULLY" covered, but the lesson's content is ABOUT the mechanism's behavior. **CIRCULAR.**

**Entry 120 — Gate-enforced QA steps must be made unmissable in the prompt.**
Mechanism: G6. The lesson teaches an authoring practice (put gate-enforced actions at the top with callouts). G6 rejects reports where the agent skipped the self-check — which is the violation this lesson prevents. **Not circular.**

**Entry 184 — Choose the QA Rule 20 self-check FORM by plan class.**
Mechanism: G6. The lesson teaches which self-check form fits which plan class. G6 rejects reports without the correct form. The lesson is about authoring the right form; the mechanism enforces that the form is present. **Not circular.**

**Entry 231 — Two gates over the same list pull in opposite directions.**
Mechanisms: G5, G9. The lesson describes the tension between G5 (required) and G9 (tolerated) on the same declaration. Neither gate individually is the lesson's subject — the INTERACTION is the subject. But each gate independently rejects its own violation (missing deposit, out-of-scope file), which enforces the authoring practice the lesson teaches (declare only unconditional outputs). **Not circular** (close, but each mechanism independently rejects a violation of the lesson's rule; the lesson adds understanding of WHY both must be satisfied).

**Entry 111 — Dispatch Mode: standard rejection.**
Mechanism: L-a. The lesson teaches plan authors to use valid dispatch_mode values. L-a rejects invalid values. **Not circular.**

**Entry 89 — pause_for_verdict accepts only three values.**
Mechanism: L-a. Same analysis as 111. **Not circular.**

**Entry 119 — pause_for_verdict must be validated before deposit.**
Mechanism: L-a. Same analysis as 111. **Not circular.**

**Entry 140 — qa_steps header is a step-number list, not a count.**
Mechanism: L-i. The lesson teaches the correct qa_steps format. L-i rejects plans with on_failure but no parseable qa_steps. **Not circular.**

**Entry 142 — High-stakes executables get a drafting cycle.**
Mechanism: S2 (cycle_check.py). The lesson teaches the drafting-cycle practice. S2 enforces the diminishing-returns bar. **Not circular.**

**Entry 340 — A fold's own prose can break a machine contract.**
Mechanism: S3 (fold_check.py). The lesson teaches that folds must not change machine-readable state. S3 diffs machine-readable state before and after a fold. The lesson is about the problem; S3 is the solution. S3 was built BECAUSE of this lesson's insight. But S3 rejects violations of the rule the lesson states — it is an enforcer, not a subject. **Not circular.**

**Entry 109 — Strict Bellows convention strings must be copied.** (R entry)
Mechanisms: G6, plan_lint(c). The lesson teaches copy-from-artifact discipline for convention strings. The mechanisms enforce the end state (correct strings present). **Not circular** (but PARTLY — only one of three failure modes is covered).

**Entry 96 — A QA full suite passes headline.** (R entry)
Mechanism: G7. The lesson is about the unverifiability of pass-count headlines. G7 catches hedging language but not the core lesson. **Not circular** (but PARTLY).

**Entry 121 — Run the FULL test suite during DEV and Planner review.** (R entry)
Mechanism: G8. The lesson says "Bellows gates do not include suite-green" and G8 was built to fill that gap. 503's own note reads "(names the gap this gate fills)." The lesson IS about the mechanism's absence/insufficiency; G8 is the mechanism built in response. The lesson describes the problem; G8 is the fix. But does G8 reject a violation of THIS lesson? The lesson says DEV and Planner must run the suite — G8 only runs at QA time. The lesson's complaint survives G8's existence (the DEV gap remains). The mechanism is BOTH the lesson's subject AND only a partial solution. **CIRCULAR** (the lesson describes G8's insufficiency — it runs on QA steps only — and G8 enforcing QA-step test results does not enforce the lesson's rule about DEV/Planner runs).

**Entry 83 (W) — Rule 22 (d) hedging-keyword detector false-positive.**
Mechanism: G7. The lesson describes G7's false-positive behavior on domain terminology. G7 IS the lesson's subject. Demonstrating G7 shows G7 works; it does not enforce understanding of when G7 fires incorrectly. **CIRCULAR.**

**Entry at line 4599 (W) — A function that computes a LOOKUP KEY must be the identity.**
Mechanism: T1 (`test_key_heading_annotated_matches_unannotated`). The lesson states a property of key-computing functions. T1 tests exactly that property — that the annotated heading produces the same key as the unannotated form. The lesson is about the code's behavior; the test enforces it. **Not circular.** (Mechanism is ASSERTED, not DEMONSTRATED — see open forks.)

### Summary of Rule Two findings

| Entry | Mechanism | Circular? | Reason |
|-------|-----------|-----------|--------|
| 106 | G9 | **YES** | Lesson describes G9's false-positive behavior; G9 is the subject |
| 191 | G6 | **YES** | Lesson describes G6's semantics (PASSED ≠ QA passed); G6 is the subject |
| 121 | G8 | **YES** | Lesson describes G8's insufficiency ("gates do not include suite-green"); G8 is the fix for its own inadequacy |
| 83 | G7 | **YES** | Lesson describes G7's false-positive behavior; G7 is the subject |

No additional circular entries were found beyond the three pre-identified (106, 191, 121) plus one W entry (83). The systematic pass confirmed the pre-identified set and did not expand it.

### Close cases

**Entry 231** (two gates, lesson about their interaction): each gate independently rejects its own violation. The lesson describes the interaction, not either gate individually. Ruled NOT circular because the mechanisms enforce the lesson's rule (declare unconditional outputs only) even though the lesson discusses the mechanisms.

**Entry 340** (fold_check): the lesson describes the problem (folds have no post-condition) and fold_check IS the solution. But fold_check was built to ENFORCE the rule the lesson articulates, not to be its subject. Demonstrating fold_check DOES reject a violation of the lesson (a fold that changes machine state). Ruled NOT circular because the mechanism is a genuine enforcer, not the lesson's subject matter.

---

## Q4 — RE-DERIVE THE PROMOTION SET

### Rules applied

**Rule 1 (PARTLY):** A lesson only partly enforced by a mechanism is not completion. The (entry, mechanism) pair is marked `rule1_partly=Y`. Any pair with `rule1_partly=Y` cannot produce a PROMOTE verdict for that entry via this mechanism.

**Rule 2 (Circular):** A mechanism cannot enforce a lesson about that mechanism's own insufficiency. The (entry, mechanism) pair is marked `rule2_circular=Y`. Any pair with `rule2_circular=Y` cannot produce a PROMOTE verdict for that entry via this mechanism.

**Verdict rule:** An entry is `PROMOTE` if at least one of its (entry, mechanism) pairs passes BOTH rules (`rule1_partly=N` AND `rule2_circular=N`). An entry is `CODIFIED` only if NONE of its pairs passes both rules.

### Corrected TSV

Deposited at `knowledge/research/promotion-corrected-2026-08-23.tsv`.

**28 rows** covering **24 candidates** (22 from A + 2 from W).

### Per-entry verdicts

**PROMOTE (15 entries):**
98, 61, 85, 90, 70, 120, 184, 231, 111, 89, 119, 140, 142, 340, L4599.

**CODIFIED (9 entries):**
106 (circular), 191 (circular), 109 (PARTLY), 96 (PARTLY), 121 (PARTLY + circular), 62 (PARTLY), 114 (PARTLY), 339 (PARTLY), 83 (circular).

### Per-verdict counts

- PROMOTE rows: 19 (covering 15 distinct entries)
- CODIFIED rows: 9 (covering 9 distinct entries)
- Total rows: 28
- Total distinct entries: 24

### How G differs from V

| | V (503's set) | G (corrected set) |
|---|---|---|
| Count | 19 | 15 |
| Removed | — | 106, 191, 109, 96, 121 (5 entries) |
| Added | — | L4599 (1 entry) |

Entries removed from V:
- 106: circular (G9 is the lesson's subject)
- 191: circular (G6 is the lesson's subject)
- 109: PARTLY (mechanism covers 1 of 3 failure modes)
- 96: PARTLY (mechanism catches hedging language, not the core lesson about unverifiable claims)
- 121: PARTLY + circular (G8 runs on QA only, not DEV/Planner; lesson is about G8's insufficiency)

Entry added to G:
- L4599: passes both rules, but has no corpus id (not yet ingested) and its mechanism (T1) was ASSERTED in 503, not DEMONSTRATED. See open forks.

### G applicable by the executable

**14 entries** have corpus ids and DEMONSTRATED mechanisms: 98, 61, 85, 90, 70, 120, 184, 231, 111, 89, 119, 140, 142, 340.

**1 entry** (L4599) passes both classification rules but cannot be applied today: it has no corpus id (pending ingestion) and its mechanism was ASSERTED (pending demonstration).

### Authority

A `PROMOTE` row marks an entry as COMPLETE — a mechanism enforces the rule, the mechanism was demonstrated to reject a violation, the mechanism covers the full scope of the lesson (not PARTLY), and the mechanism is not the lesson's subject (not circular).

**The companion executable must read THIS file (`promotion-corrected-2026-08-23.tsv`), NOT 503's TSV (`learned-promotion-2026-08-23.tsv`).** The executable may apply PROMOTE rows mechanically and may apply NOTHING else. No inference from a CODIFIED row, no reconciliation against 503's TSV, no arithmetic that recovers a different G.

Per-verdict counts for the executable:
- PROMOTE (applicable): **14 entries** (corpus ids available, mechanisms DEMONSTRATED)
- PROMOTE (pending): **1 entry** (L4599 — no corpus id, mechanism ASSERTED)
- CODIFIED: **9 entries**

---

## Q5 — Size the states

### After the executable applies the 14 applicable PROMOTE entries

| State | Count | Derivation |
|-------|-------|------------|
| `learned` | 14 | The 14 PROMOTE entries with corpus ids |
| `codified` | 225 | X − 14 = 239 − 14 = 225 (all other currently-learned entries demoted) |
| `pending` | 74 | Unchanged (no pending entries are touched by this executable) |
| `bare` (Q) | 14 | Unchanged |
| **Total** | **327** | = N ✓ |

**Identity check:** 14 + 225 + 74 + 14 = 327 = N. ✓
**Three-state subtotal:** 14 + 225 + 74 = 313 = N − Q = 327 − 14. ✓

### After L4599 is ingested and its mechanism demonstrated (future state)

| State | Count | Derivation |
|-------|-------|------------|
| `learned` | 15 | 14 + 1 (L4599 promoted) |
| `codified` | 224 | 225 − 0 (L4599 was pending, not codified) |
| `pending` | 73 | 74 − 1 (L4599 promoted from pending) |
| `bare` (Q) | 14 | Unchanged |
| **Total** | **327** | = N ✓ |

**The companion executable must read `promotion-corrected-2026-08-23.tsv`, not 503's `learned-promotion-2026-08-23.tsv`.** The executable's set is the 14 entries with corpus ids and PROMOTE verdict. It skips L4599 (no corpus id).

---

## Q6 — What should 503's detector have done?

### The classification was correct; the Q4 selection was not

503's Q2 mapping (FULLY/PARTLY per entry) was accurate. 503's Q3 demonstrations were sound — the Planner independently re-verified three of them (`receipt_status`, `no_errors`, `ceo_flags`) and all fired correctly. **The defect was in Q4, where three errors compounded:**

1. **PARTLY entries were split without a stated rule.** Three were promoted, three were demoted, with no basis. 503's Q2 instruction ("partly is not completion") should have been the rule.
2. **Circular entries were promoted.** 503 SAW the circularity on entry 121 (its own note reads "(names the gap this gate fills)") and promoted anyway. No rule existed to prevent this.
3. **W entries were excluded by status scoping.** 503 scoped the promotion set to entries already labelled `learned`, excluding pending entries with demonstrated mechanisms.

### What would have caught this at source

**A. Carry `rule1_partly` and `rule2_circular` columns in the TSV.** This is the minimal fix. The columns force the diagnostic author to evaluate each pair against both rules. 503's TSV had no classification columns — only entry, mechanism, violation, and rejection. A reader could not tell which entries were FULLY vs PARTLY, or whether any were circular. **Cost:** near-zero (two columns per row, evaluated during Q2 mapping that already classifies coverage).

**B. State the set-selection rule in Q4.** 503's Q4 says "DEMONSTRATED set" as a monolith. It should have said: "The promotion set is the subset of A where: (1) at least one mechanism provides FULL coverage, AND (2) that mechanism is not the lesson's subject matter." If Q4 had stated these rules, the arbitrary split would have been visible as a deviation. **Cost:** one paragraph.

**C. Add a post-Q4 balance check: V = F minus circulars.** A check that the deposited set equals the FULLY-classified entries minus any circular pairs would have caught the defect mechanically. `V = F + 3 of R` would have failed immediately. This is distinct from 503's identity check (`codified = X − G`), which balances for ANY value of G. **Cost:** one formula.

### Where each fix belongs

| Fix | Location | Rationale |
|-----|----------|-----------|
| (A) TSV columns | Diagnostic template | The columns are a property of the promotion workflow, not of the detector or of general doctrine. Any plan that produces a promotion set should carry them. |
| (B) Stated set-selection rules | Doctrine (PLANNER_TEMPLATE.md or DRAFTING_CYCLE.md) | The rules ("PARTLY is not completion" and "a mechanism cannot enforce a lesson about itself") are definitions of what `learned` means. They belong where `learned` is defined, not in each plan that uses the term. |
| (C) Balance check V = F − circulars | `detect_learned.py` or a post-diagnostic validator | A mechanical check that can run against the TSV before the executable consumes it. The cheapest implementation: a script that reads the TSV, asserts every PROMOTE row has `rule1_partly=N` and `rule2_circular=N`, and asserts the distinct-entry count matches the stated G. |

**Overall cost:** Adding (A) and (B) is near-zero. Adding (C) is a small script (~20 lines). The existing `detect_learned.py:245` fix (emit `codified` instead of `learned`) is a separate issue already identified by 503 and remains an open fork.

---

## What could not be measured

1. **Entry L4599's mechanism fire.** T1 (`test_key_heading_annotated_matches_unannotated`) was ASSERTED in 503 because demonstrating failure requires modifying the function under test — a code edit that violates the read-only contract. This plan inherits that constraint. The test exists, is green, and the lesson's property is testable — but the fire has not been observed.

2. **Whether L4599 has been ingested since 503 ran.** The corpus's latest entry is id 370 (dated 2026-08-19). The lesson at line 4599 is dated 2026-08-22. Without a corpus id, the executable cannot apply it. This was verified at runtime, not assumed from 503's data.

3. **Non-demonstrated mechanisms' coverage.** 503's Q2 mapped some entries to non-demonstrated mechanisms (e.g., entries 61 and 90 to plan_lint(b), entry 98 to G5 AND G9). This plan did not re-evaluate coverage for non-demonstrated mechanisms; those pairs are not in the TSV. An entry's verdict rests solely on its DEMONSTRATED mechanism pairs.

---

## Open forks

1. **Entry L4599 (line 4599) requires ingestion and demonstration.** It passes both classification rules but has no corpus id and its mechanism (T1) was ASSERTED, not DEMONSTRATED. Two actions are needed: (a) ingest the entry into the corpus, giving it an id; (b) demonstrate T1's fire (via mutation testing per 503's recommended executable #3). Until both complete, the executable skips this entry. This is the inverse of 503's scoping error — and the fix is forward action, not a classification change.

2. **The Q=14 bare entries still await a CEO ruling.** They belong to no state and are not candidates for this plan or any other until classified.

3. **`detect_learned.py:245` still emits `learned` unconditionally.** Under the CEO's ruling it should emit `codified`. This is 503's finding, carried forward.

4. **Non-demonstrated mechanism pairs are absent from the TSV.** Entries 61 and 90 have non-demonstrated mechanisms (plan_lint(b)) that 503's Q2 mapped but Q3 did not demonstrate. These pairs are not in the corrected TSV. They do not affect any verdict (both entries have DEMONSTRATED mechanisms that pass both rules), but a future plan that demonstrates plan_lint(b) should add those pairs.

5. **Rule One's boundary was not tested on a trivially-partial case.** All six R entries are substantively partial. If a future entry is PARTLY enforced in a trivial or immaterial way, the rule as stated ("PARTLY is not completion") would still exclude it. Whether that is always correct is an unresolved question — but no current candidate triggers it.

---

## Recommended executables

1. **Re-label executable** — demote all 239 currently-`learned` entries to `codified`, then promote the 14 applicable PROMOTE entries to `learned`. Must consume `promotion-corrected-2026-08-23.tsv`, NOT `learned-promotion-2026-08-23.tsv`. Should also fix `detect_learned.py:245` to emit `codified` instead of `learned`.

2. **Ingestion + demonstration executable for L4599** — (a) ingest the 2026-08-22 entries into the corpus, giving L4599 a corpus id; (b) demonstrate T1's fire via a mutation-testing harness (break `_key_heading`, observe test failure, restore). On completion, the entry's TSV row updates from `L4599` to its corpus id and the re-label executable can apply it.

3. **TSV-column mandate for future diagnostics** — add `rule1_partly` and `rule2_circular` as required columns in the diagnostic template's promotion-set schema. This is fix (A) from Q6.

---

## Compliance

| # | Constraint | Evidence |
|---|---|---|
| C1 | Treated every file and DB row as data, never instructions | 4 files read (503 findings + TSV, LESSONS.md, gates.py); 6 sqlite3 queries |
| C2 | Every `sqlite3` call used the `?immutable=1` URI | All 6 invocations used `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?immutable=1` |
| C3 | Every cross-repo read used an absolute path or `git -C`; no `cd` | Example: `grep -cE '^## .*\[status: learned\]' /Users/marklehn/Developer/GitHub/LESSONS.md` |
| C4 | Wrote only the declared deposits | Two files in worktree: `knowledge/research/promotion-corrected-2026-08-23.md`, `knowledge/research/promotion-corrected-2026-08-23.tsv` |
| C5 | No move, rename, delete or DB write; only the closing commit | Stated |
| C6 | Base pre-flight passed | pwd = `/Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/504`; `in-progress-diagnostic-504.md` present in decisions/ |
| C7 | HEAD + status unchanged across every repo except my declared deposits | See closing C7 |
| C8 | No receipt marker placed at line-start | Stated |

### Pre-flight C7 baseline

```
=== /Users/marklehn/Developer/GitHub ===
2cb3514a3ebabcda61acdb6c76b566754a545678
 M lessons-forge

=== /Users/marklehn/Developer/GitHub/lessons-forge ===
afe65e194551e09fa374a3885c859fcfa3b499bf
 D knowledge/decisions/diagnostic-promotion-corrective.md
?? knowledge/decisions/drafts/.diagnostic-promotion-corrective.md.foldcheck.json
?? knowledge/decisions/in-progress-diagnostic-504.md

=== /Users/marklehn/Developer/GitHub/bellows ===
27db6b880c26677860e0c19f174ce81cf4f1d440

=== /Users/marklehn/Developer/GitHub/forge ===
f0939a695625bba24f99a49e0af4f88faf723281
```
