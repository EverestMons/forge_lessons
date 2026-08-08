# Classifications — Cycle 2026-08-07 — Tranche B (Part 2)

**Plan:** executable-311
**Step:** 3 — Classification tranche B (entries 232–248)
**Date:** 2026-08-07

## Per-Entry Classification Reasoning

### Entry 232 (Proposal 240) — `verification` → `governance_rule`

**Substance:** A verification pin whose extraction method is unstated fails closed on honest work. The hash was correct but the plan never said how to extract the region — fence-inclusive vs fence-exclusive, trailing newline kept vs stripped — all produce different bytes. Two pins in one artifact and a row-count baseline all carried the same defect.

**Category justification (precedent-poor tag `verification`, 1 prior):** The fix is a documentary authoring rule — "The method IS part of the pin. Ship the exact command beside the value, not the value alone" — extending Rule 61 in PLANNER_TEMPLATE.md. The entry proposes no code change, no procedural step, no tooling fix; the entire recommendation is a rule change constraining how verification pins are documented.

**Target:** `PLANNER_TEMPLATE.md` (Rule 61 extension). No Family line present; placement derived from body.

### Entry 233 (Proposal 241) — `planner-discipline` → `governance_rule`

**Substance:** Two high-severity findings of the same shape were correctly fixed at the site where noticed and not carried to the sibling site — written minutes earlier. The intuition that a sweep is most reliable while the principle is fresh is exactly backwards.

**Target:** `DRAFTING_CYCLE.md` §2.7 fold-sweep section. Family line: "the fold-sweep discipline, measured failing under the conditions most favourable to it."

### Entry 234 (Proposal 242) — `verification` → `governance_rule`

**Substance:** A verification's "independent referents" were sourced from the actor's own record. Two of three new referents were circular in exactly the same way — the fix reproduced the defect it existed to remove, twice, in the same edit.

**Category justification (precedent-poor tag `verification`):** The entry proposes a verifiable authoring principle — audit every new referent against the independence test: "Independence means the referent exists before the actor acts and outside its control." This is a new documentary rule near Rule 55, not a tooling change.

**Target:** `PLANNER_TEMPLATE.md` (new rule near 55). No Family line present; placement derived from body.

### Entry 235 (Proposal 243) — `planner-discipline` → `governance_rule`

**Substance:** A backup separated from its protected write by twenty-two file edits spanned a window where another process was legitimately writing the same store. Restoring would have rolled back real work. The adjacency requirement also strengthens the state machine elsewhere.

**Target:** `PLANNER_TEMPLATE.md` (Rule 56 area). No Family line present; placement derived from body.

### Entry 236 (Proposal 244) — `verification` → `governance_rule`

**Substance:** A zero-difference blast-radius check is indistinguishable from a broken comparison — a bad query, wrong file, or empty read all produce the same silence. The check became evidence only when the same comparison was run against the target range to show the instrument could see a difference.

**Category justification (precedent-poor tag `verification`):** The entry proposes a general positive-control principle for absence-result checks as a documentary rule extending Rule 55 — not a tooling change. "Any check whose passing result is an absence needs a positive control on the same instrument in the same run."

**Target:** `PLANNER_TEMPLATE.md` (Rule 55 extension). No Family line present; placement derived from body.

### Entry 237 (Proposal 245) — `planner-discipline` → `governance_rule`

**Substance:** Six adversarial review phases and roughly a hundred findings provided zero coverage of mechanical conformance — the conformance pass immediately found three hard failures. The two layers are complementary by construction.

**Target:** `DRAFTING_CYCLE.md` §5. Cluster (E) with entry 224 (proposal 232) — one §5 scheduling edit, not two. No Family line present; placement derived from body.

### Entry 238 (Proposal 246) — `planner-discipline` → `governance_rule` — SHAPE-DECISION CLUSTER (A)

**Substance:** The finding-count/aim relationship measured directly — the count ROSE when the aim came off. Walk 5 aimed at three untouched regions found 3 findings with twelve unreached cells; walk 6 untargeted found 8 with zero unreached. This is the first direct measurement of the inverse.

**Routes into the reserved CEO decision on drafting-cycle shape per baton item 2.** The entry is core evidence; no independent codification. No Family line present; placement derived from body.

### Entry 239 (Proposal 247) — `planner-discipline` → `governance_rule` — SHAPE-DECISION CLUSTER (A)

**Substance:** Ten consecutive ACID passes each found a defect created by the culmination immediately before it — at n=10 this is the measured behaviour, not a tendency. The failure class drifted from logic to record defects — the judged-stop signal.

**Routes into the reserved CEO decision on drafting-cycle shape per baton item 2.** Core shape-decision evidence establishing class drift as the progress signal. No Family line present; placement derived from body.

### Entry 240 (Proposal 248) — `planner-discipline` → `governance_rule`

**Substance:** A retraction claimed it corrected a claim "in three places" and had reached one. A consumer sweep then missed a fifth site holding the same claim as a paraphrase — the probe was the literal string from the edited sentence. Two failures compose: false-count retractions and self-worded sweeps.

**Target:** `DRAFTING_CYCLE.md` §2.7 (claim-level probe rule). No Family line present; placement derived from body.

### Entry 241 (Proposal 249) — `verification` → `governance_rule`

**Substance:** A guard was safe only by the accident of an incidental backtick — removing it or adding a space would have let the gate capture prose as the deposit list. Reasoning dismissed it; executing the real regexes revealed the safety was accidental.

**Category justification (precedent-poor tag `verification`):** The fix is a documentary rule requiring execution of the gate's actual matcher and reporting which branch fired — "run the guard's actual matcher rather than reasoning about it." This is a verification authoring rule for plan drafting, not a tooling change.

**Target:** `DRAFTING_CYCLE.md` §2.7. No Family line present; placement derived from body.

### Entry 242 (Proposal 250) — `verification` → `governance_rule`

**Substance:** A measurement taken without the mandated strip method overstated by half (six files where the answer was four), and a fresh cold reader who had just read the strip rule still skipped it. The discipline cannot survive call-site repetition.

**Category justification (precedent-poor tag `verification`):** The fix extends Checklist #29 — "Every number stated in a plan must be produced by the plan's own mandated method; if it was not, it is a prediction and must carry a verify-clause." A documentary rule change, not tooling.

**Target:** `PLANNER_TEMPLATE.md` (Checklist #29 extension). No Family line present; placement derived from body.

### Entry 243 (Proposal 251) — `verification` → `governance_rule`

**Substance:** §2.7's retraction-in-place discipline structurally degrades probes — a well-run cycle accumulates retraction text matching the patterns probes detect. Two of seven probes fired false alarms, and at least one would have been folded without checking.

**Category justification (precedent-poor tag `verification`):** The fix is a documentary probe classification rule — "classify each hit as instruction or retraction-of-instruction before reporting" — for DRAFTING_CYCLE.md §2.7. A verification methodology rule, not a tooling change.

**Target:** `DRAFTING_CYCLE.md` §2.7 (probe rules). No Family line present; placement derived from body.

### Entry 244 (Proposal 252) — `planner-discipline` → `governance_rule`

**Substance:** A closing line written one phase early stated stale counts and a falsified last-event assertion. A fifth ACID pass was still owed and found all three claims defective. The closing line is load-bearing under §2.7 and writing it early produces systematic optimistic bias.

**Two halves:** The shape-decision half (cluster A) is evidence for the reserved CEO decision — the gap between taking a stop and having finished. The closing-line ordering rule (walk → culminate → final ACID → then close) is independently codifiable in DRAFTING_CYCLE.md §2.7/§3. Sibling of entry 263.

**Target:** `DRAFTING_CYCLE.md` §2.7/§3. No Family line present; placement derived from body.

### Entry 245 (Proposal 253) — `verification` → `governance_rule`

**Substance:** Nine prose mentions of a heading token caused four misfired measurements in one session, including the mechanical conformance check reporting two false FAILs 251 lines early. The density of decoys is highest in exactly the files most likely to be measured.

**Category justification (precedent-poor tag `verification`):** The fix is a documentary probe-anchoring rule — "Anchor every structural search line-anchored, strip fenced blocks and blockquotes before matching." A verification authoring rule for plan-drafting, not a tooling change.

**Target:** `DRAFTING_CYCLE.md` §2.7 (sibling of entry 243's probe rules). No Family line present; placement derived from body.

### Entry 246 (Proposal 254) — `planner-discipline` → `governance_rule`

**Substance:** Clone-drift measured at three depths — guards absent, guards present but unqualified, and corrections reaching some sites but not all. A restored guard imported the parent's pre-fold version, which would have blocked three questions unnecessarily.

**Target:** `DRAFTING_CYCLE.md` §2.6 (clone-drift rules extension). No Family line present; placement derived from body.

### Entry 247 (Proposal 255) — `planner-discipline` → `governance_rule`

**Substance:** Three individually-correct patches to a question block turned out to be the same polarity-contradiction defect. The resolution was one declared rule: one quantity, two legitimate opposed values, no verdicts in any question. Scout says split — the polarity half is new; the per-region half (three patches means the region is wrong) is already codified in 1.4 §2.8.

**Target:** `PLANNER_TEMPLATE.md` (diagnostic-authoring, polarity residue). No Family line present; placement derived from body.

### Entry 248 (Proposal 256) — `planner-discipline` → `governance_rule`

**Substance:** A flattering substitution in a motivating claim — swapping plan 281 for plan 274, making the motivating claim true — survived a walk, a culmination, an ACID pass, and a second culmination. No gate catches this class: plan_lint reads structure, consumer sweeps probe wording.

**Target:** `DRAFTING_CYCLE.md` §2.7. No Family line present; placement derived from body.
