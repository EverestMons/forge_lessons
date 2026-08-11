# Classifications — Cycle 2026-08-10, Part 2 (Tranche B: entries 280–293)

14 entries classified. All derived from the entry's own `raw_content` body — no entry in this batch carries a `**Family:**` line (0 of 41, measured). Every placement comes from the body alone.

---

## Entry 280 (proposal 288) — `process-discipline` → `governance_rule`

**Heading:** The shell's cwd resets between calls — three phase commits landed in the WRONG repo while printing success; cd-first plus a toplevel assert is the whole fix

**Category:** `governance_rule` — the entry prescribes a plan-authoring protocol for commit compounds (cd-first, toplevel-assert). The `process-discipline` tag has two prior corpus uses, both classified `instrumentation`; category justified by the prescriptive, rule-shaped nature of the How-to-apply clauses ("Every compound touching a repo starts with cd /abs/path as its FIRST token") which belong in the plan template as a git-commit mechanics rule, not as a procedural checklist.

**Target:** `PLANNER_TEMPLATE.md` — git-commit mechanics section. Agreed with scout.

**Remedy:** discipline — the cd-first and toplevel-assert protocol are practices a plan author must remember; there is no named mechanism or tool owner.

---

## Entry 281 (proposal 289) — `bellows-mechanics` → `governance_rule`

**Heading:** The Bellows verdict grammar is continue/stop only — a "redo" is a stop plus a corrected re-deposit, and the correction rides a narrowly-keyed A0 branch

**Category:** `governance_rule` — the entry prescribes a plan-authoring rule about verdict gates: never promise a verdict the grammar lacks. Zero corpus precedent for `bellows-mechanics`; category justified by the substance being a doctrine constraint on how plans author verdict gates, not a bellows code change or a checklist. Rule 46 split: the grammar itself is bellows-owned; the authoring rule is doctrine.

**Target:** `PLANNER_TEMPLATE.md` — verdict-gate authoring rules. Agreed with scout.

**Remedy:** discipline — the remedy is "read verdict.py before naming options" and "a redo = stop + re-deposit," which are authoring disciplines. The bellows-owned grammar is the Rule 46 split half, not this proposal's scope.

---

## Entry 282 (proposal 290) — `probe-integrity` → `governance_rule`

**Heading:** A dash-leading constructed grep pattern parses as an OPTION — exit 2, empty stdout — and a read-the-count rule converts that emptiness into a false answer

**Category:** `governance_rule` — the entry prescribes a rule for probe construction (use -e or -- with variable patterns). Zero corpus precedent for `probe-integrity`; category justified by the prescriptive nature of the How-to-apply clause: "Every constructed or variable pattern is passed via -e \"$PAT\" (or after --)" — this is a governance rule for probe authoring, not a structural code change or a checklist.

**Target:** `DRAFTING_CYCLE.md` — §2.7, beside the existing `grep -F` clause. Agreed with scout.

**Remedy:** discipline — the remedy names a pattern-passing convention a plan author must follow; no tool or automated checker is named.

---

## Entry 283 (proposal 291) — `instruction-design` → `governance_rule`

**Heading:** A nine-element compound instruction dropped exactly one element in execution — per-element mechanical asserts are what caught it

**Category:** `governance_rule` — the entry prescribes how compound outputs must be specified and verified in plans: enumerable element lists with one mechanical assert per element. Zero corpus precedent for `instruction-design`; category justified by the prescriptive plan-authoring rule about output specification and QA assertion design. The substance is a governance rule about how plans must be authored.

**Target:** `PLANNER_TEMPLATE.md` — per-element QA asserts. Agreed with scout.

**Remedy:** mechanism | owner: plan_lint or QA tooling — the entry names "per-element mechanical asserts" as the concrete mechanism, and the How-to-apply clause prescribes "one mechanical assert per element." The element-list extraction and assert generation are automatable.

---

## Entry 284 (proposal 292) — `drafting-cycle` → `governance_rule`

**Heading:** A walk examines the WHOLE artifact, so "no walk has examined this region" is never a true statement — it is the rationalization that hides a cycle folding its own repairs

**Category:** `governance_rule` — the entry proposes a change to §2's doneness criterion and the cycle log methodology. Cluster (A) centerpiece alongside entries 267, 270, 294, 300.

**Target:** `DRAFTING_CYCLE.md` — §2 doneness criterion. Agreed with scout. Flag (A) convention: target is the doctrine file, route-into-§2-rewrite noted.

**Flag (D):** v2.0's §2 and §2.7 appear to codify this in full — the entry's substance (classify findings as pre-existing vs fold-introduced, report the ratio) may already be carried. Gate 1 must measure clause-by-clause against the live file.

**Remedy:** discipline — the entry names classifying findings by origin and reporting ratios in the cycle log, practices a cycle author must remember. No tool or automated mechanism is named.

---

## Entry 285 (proposal 293) — `verification` → `governance_rule`

**Heading:** An inherited SEVERITY label survives every check that would have caught an inherited factual claim

**Category:** `governance_rule` — the entry prescribes treating severity/reversibility labels as claims with probes, and diffing a parent's risk adjectives on clone.

**Target:** `PLANNER_TEMPLATE.md` — diverged from scout's split option (`DRAFTING_CYCLE.md §2.7 or PLANNER_TEMPLATE.md`). The substance is about how a plan author verifies risk labels at authoring and at gates, which belongs in the plan template. v2.0 did NOT codify this (noted in scout).

**Remedy:** discipline — the remedy names probing severity labels and diffing risk adjectives on clone; no automated checker is named, though the practice could be mechanized.

---

## Entry 286 (proposal 294) — `instrumentation` → `instrumentation`

**Heading:** plan_lint's expected-WARN set is LOCATION-dependent, so declaring it from the drafting path declares the wrong thing

**Category:** `instrumentation` — the entry prescribes a procedural safeguard in the deposit pipeline: lint at the deposit-path resolution before declaring the expected state. The `instrumentation` tag has corpus precedent classifying to `instrumentation`. The substance is a workflow mechanism for the lint-declare-deposit cycle.

**Target:** `DRAFTING_CYCLE.md` — §5 (record the exit code and the resolution). Agreed with scout.

**Remedy:** mechanism | owner: bellows (deposit pipeline) — the entry identifies a concrete mechanism: lint must run at the deposit path resolution, not the drafting path. The How-to-apply clause names a specific practice that bellows's deposit pipeline should enforce: "Lint at the DEPOSIT path resolution before declaring the expected state."

---

## Entry 287 (proposal 295) — `verification` → `governance_rule`

**Heading:** A sweep whose fixes quote what they fixed can never be verified by a count reaching zero

**Category:** `governance_rule` — the entry prescribes a verification methodology rule: verify by classification (operative vs correction), not by count.

**Target:** `DRAFTING_CYCLE.md` — §2.7 (verification methodology). Agreed with scout.

**Remedy:** discipline — the remedy names a classification technique (list every hit, mark each operative or correction) that a cycle author must apply. No automated tool is named.

---

## Entry 288 (proposal 296) — `drafting-cycle` → `governance_rule`

**Heading:** A constraint opened mid-cycle is never swept backwards over what already existed

**Category:** `governance_rule` — the entry prescribes a constraint-lifecycle rule for §2.8: sweep the whole artifact when opening a constraint, not at the next culmination. Sibling of entry 268.

**Target:** `DRAFTING_CYCLE.md` — §2.8. Agreed with scout.

**Remedy:** discipline — the remedy names "run its check over the whole artifact immediately, as part of opening it" — a practice the cycle author must follow. No automated mechanism is named.

---

## Entry 289 (proposal 297) — `verification` → `governance_rule`

**Heading:** A check that fails a correct run is a check an agent will loosen

**Category:** `governance_rule` — the entry prescribes using derived expectations over constants in QA assertions. Sibling of entry 303.

**Target:** `PLANNER_TEMPLATE.md` — derived expectations rule. Agreed with scout.

**Remedy:** discipline — the remedy names preferring derived expectations and confirming assertions match correct runs; no automated tool is named, though the principle supports mechanization (entry 303 is the companion).

---

## Entry 290 (proposal 298) — `planner-discipline` → `governance_rule`

**Heading:** A guard's stated REASON is part of the guard — correct the premise and the guard is already weakened

**Category:** `governance_rule` — the entry prescribes a sweep rule: when a premise is corrected, grep for every guard resting on it and re-justify or remove.

**Target:** `DRAFTING_CYCLE.md` — §2.7. Diverged from scout (scout suggested `DRAFTING_CYCLE.md §2.7` or `PLANNER_TEMPLATE.md`; set `DRAFTING_CYCLE.md` as the primary since the rule governs fold-time behavior in a drafting cycle, specifically the consequence of correcting a premise within an artifact under edit).

**Remedy:** discipline — the remedy names a grep-and-re-justify sweep after premise corrections; no tool or automated checker is named.

---

## Entry 291 (proposal 299) — `process-discipline` → `governance_rule`

**Heading:** `LESSONS.md` entries carry no numbers, so an ordinal citation is unverifiable — and one was wrong

**Category:** `governance_rule` — the entry prescribes a citation convention (date + title fragment, never ordinal). The `process-discipline` tag has two priors classified `instrumentation`; category justified by the prescriptive citation-convention substance ("Cite a lesson by date plus a title fragment — greppable with grep -F, stable, and self-verifying. Never by ordinal.") which is a governance rule about citation form in plans, not a procedural checklist.

**Target:** `PLANNER_TEMPLATE.md` — citation convention. Agreed with scout.

**Remedy:** mechanism | owner: plan_lint or authoring discipline — the entry names a concrete verifiable form (date + title fragment, greppable with `grep -F`) and the anti-pattern (ordinal citation). A lint check that flags ordinal-only LESSONS.md citations is a named mechanism. However, the owner is split between authoring discipline (the convention) and plan_lint (the enforcement).

---

## Entry 292 (proposal 300) — `process-discipline` → `governance_rule`

**Heading:** A changelog says what changed, not which direction — read the diff before calling a change a regression

**Category:** `governance_rule` — the entry prescribes a verification rule: any claim that a governed text changed is established by `git show` against the live file, never by the changelog row. The `process-discipline` tag has two priors classified `instrumentation`; category justified by the prescriptive governance-rule substance about evidence standards for claims about doctrine.

**Target:** `DRAFTING_CYCLE.md` — §2.6 (clone-diff) / §2.7. Agreed with scout.

**Remedy:** discipline — the remedy names a diff-based verification practice that a cycle author must follow; no automated tool is named.

---

## Entry 293 (proposal 301) — `drafting-cycle` → `governance_rule`

**Heading:** Folding a defect class in one plan does not immunise the next plan against it

**Category:** `governance_rule` — the entry proposes a routing meta-rule: treat a class folded twice as a mechanization candidate, not a lesson candidate. This is flag (G)'s meta-rule.

**Target:** `DRAFTING_CYCLE.md` — diverged from scout (scout noted "routing principle, not a doctrine clause" with no file target). The recurrence-to-mechanization routing rule belongs in the cycle methodology as part of the fold-disposition framework. No `**Family:**` line present; target independently derived from the entry's substance about how drafting cycles handle fold disposition.

**Remedy:** discipline — the meta-rule itself ("route to census/prototype path rather than to a prose rule") is a routing discipline Gate 1 must apply. The entry names the mechanization queue as the destination but does not itself name a specific mechanism or tool.
