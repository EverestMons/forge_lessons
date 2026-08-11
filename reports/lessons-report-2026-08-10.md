# Lessons Report — 2026-08-10


## Summary


| Category | Count |
|---|---|
| governance_rule | 39 |
| instrumentation | 2 |

**Total proposals:** 41


## Governance Rule


### 2026-08-10: A sweep whose fixes quote what they fixed can never be verified by a count reaching zero [tag: verification]


- **Suggested action:** Codify the verify-by-classification rule in DRAFTING_CYCLE.md §2.7: for any sweep of a phrase or token whose fixes cite the original, verify by classification (listing every hit and marking each operative or correction), never by count. Zero operative hits is the pass condition; the total is meaningless.
- **Reasoning:** The entry documents a measured failure class: "Three times in one drafting cycle, a phrase was swept out of an artifact and the verification was grep -c trending to zero. It never trends to zero: each fold records what it corrected, so the corrected wording survives inside the correction. One recount came back higher than before the fold." The remedy is concrete and self-contained: "verify by classification, not by count: list every hit and mark each operative or correction. Zero operative hits is the pass condition; the total is meaningless."
- **Confidence:** high

### 2026-08-10: A constraint opened mid-cycle is never swept backwards over what already existed [tag: drafting-cycle]


- **Suggested action:** Codify the constraint-sweep-on-open rule in DRAFTING_CYCLE.md §2.8: when a constraint is opened mid-cycle, run its check over the whole artifact immediately as part of opening it — not at the next culmination. Record the sweep result in the constraint row itself. Sibling of entry 268 (constraints opened from the batch's own entries were breached by later folds).
- **Reasoning:** The entry documents a measured gap in constraint lifecycle: "A drafting cycle opened a constraint at walk 1 forbidding non-ASCII characters inside -F probe literals, after a probe grepped two checkbox glyphs. Three walks later the constraint was violated at two load-bearing pins — a version pin carrying § and an anchor carrying an em-dash — both written before the constraint existed. Twenty lens passes read past them." The structural cause: "Opening a constraint feels like closing the class. It is not: it binds what is written after it. Everything already in the artifact is grandfathered in silently."
- **Confidence:** high

### 2026-08-10: A check that fails a correct run is a check an agent will loosen [tag: verification]


- **Suggested action:** Codify the derived-expectations rule in PLANNER_TEMPLATE.md: before shipping any "exactly N" assertion, confirm it matches what a correct run produces — including under re-entry, concurrent actors, and later edits that change the count. Prefer derived expectations over constants (read the Deposits blocks and count them, compute 2+R from the recorded re-entry count). Sibling of entry 303.
- **Reasoning:** The entry documents a measured class of self-defeating guards: "Three separate QA assertions in one plan would have failed on a correct execution: an exactly two commits count that a legitimate re-entry makes three; an exactly N deposits count left stale by a later split; and a path-set comparison where git show --name-only prints repo-relative paths while the declared deposit was absolute." The structural failure: "The guard then dies at exactly the moment it was supposed to work, and it dies by consent." The remedy: "Prefer derived expectations over constants: read the Deposits blocks and count them."
- **Confidence:** high

### 2026-08-10: A guard's stated REASON is part of the guard — correct the premise and the guard is already weakened [tag: planner-discipline]


- **Suggested action:** Codify the premise-correction sweep rule in DRAFTING_CYCLE.md §2.7 (or PLANNER_TEMPLATE.md — Gate 1 decides): when any premise is corrected, grep the artifact for every guard resting on it and re-justify or remove each one. The correction is not complete at the site where the premise was stated.
- **Reasoning:** The entry documents a measured failure where a guard's justification was falsified but the guard survived: "A plan carried a hard guard — the corpus is READ-ONLY here; an agent that flips a row has broken the CEO's standing hold — whose premise was then measured and found false: the hold covered seven proposal ids the plan never touched. The guard's text survived the correction. Its justification did not." The structural insight: "An agent that can see through a guard's stated reason steps over the guard. The rule text is not what carries authority in practice; the reason is, because the reason is what an agent weighs when the rule is inconvenient."
- **Confidence:** high

### 2026-08-10: `LESSONS.md` entries carry no numbers, so an ordinal citation is unverifiable — and one was wrong [tag: process-discipline]


- **Suggested action:** Codify the citation convention in PLANNER_TEMPLATE.md: cite a lesson by date plus a title fragment (greppable with grep -F, stable, self-verifying), never by ordinal. And before citing, run the probe — a lesson that lives only in memory or a baton has not necessarily been appended. Mechanism candidate: a lint check that flags ordinal-only LESSONS.md citations (e.g. "LESSONS 226" with no date or title fragment). Owner: plan_lint or authoring discipline.
- **Reasoning:** The entry documents a measured citation failure: "A plan cited LESSONS 226 twice for a subtractive-cut result and mandated, in its own QA step, that such citations be checked. Measured: entry 226 is a different lesson entirely, and probes for the cited lesson's distinctive phrases returned 0 against a positive control — it is not in LESSONS.md at all, existing only as a memory and a baton note." The structural cause: "The file's headings are dates and titles. An ordinal is derivable only by counting 226 headings, which nobody does, so an ordinal citation is unfalsifiable in practice."
- **Confidence:** high

### 2026-08-10: A changelog says what changed, not which direction — read the diff before calling a change a regression [tag: process-discipline]


- **Suggested action:** Codify the diff-before-direction-claim rule in DRAFTING_CYCLE.md §2.6/§2.7: any claim that a governed text changed (tightened, loosened, added, removed) is established by git show <old>:<file> against the live file, never by the changelog row. Hold a claim about doctrine to the same standard as a claim about a clause. Run one pass over a cycle's own conclusions record at the evidence standard the cycle enforced on its subject.
- **Reasoning:** The entry documents a measured error that survived four walks: "A four-walk drafting cycle published, committed and pushed a headline finding that a doctrine amendment had tightened a precondition and locked the shop's highest-yield instrument out. It had loosened it. The prior version required the walk to go literally dry; the amendment accepted dry or a judged stop — strictly wider." The failure mode: "The claim came from the amendment's own History row: convenes once the bar is met rather than after literal dryness. Accurate, and directionally silent. Rather than X reads as replacement, and a reader supplying the direction supplies the one that fits the story being written. One git show of the two versions falsified it."
- **Confidence:** high

### 2026-08-10: Folding a defect class in one plan does not immunise the next plan against it [tag: drafting-cycle]


- **Suggested action:** Codify the recurrence-to-mechanization routing rule: treat a class folded twice across different artifacts as a mechanization candidate, not a lesson candidate — route it to the census/prototype path rather than to a prose rule. And when drafting a plan, run the previous plan's ledger over the new draft as a checklist. This is flag (G)'s meta-rule — its disposition determines whether the mechanism-shaped entries in this batch get routed to build or to prose. Gate 1 should decide entry 293 first because it is circular and load-bearing.
- **Reasoning:** The entry provides the strongest measured argument for mechanization over documentation: "Three scaffolding classes were found and folded during one plan's drafting cycle: a guard asserting against a value no step captures, a mandated artifact absent from the Scope block, and a reference to an artifact that does not exist at the point it is read. All three recurred in the very next plan drafted the same day by the same author, and survived six walks there before being caught." The interval measurement is the core evidence: "the interval between folding a class and re-committing it was hours, in the same session, by the same person who wrote the lesson."
- **Confidence:** high

### 2026-08-10: A restructuring pass resets the convergence curve — do not read the finding count as progress [tag: drafting-cycle]


- **Suggested action:** Codify in DRAFTING_CYCLE.md §2 or §3: after a restructuring pass (collapse, promotion, sub-step split), the convergence clock resets — the next walk is a first pass over the new arrangement, not a confirming pass. Do not treat a post-collapse finding count as a convergence signal. Route into the §2 doneness cluster rewrite alongside entries 267, 270, 284, 300 (cluster A).
- **Reasoning:** The entry identifies structural edits as convergence-resetting events, measured across two collapses in one cycle. The evidence from the entry's own raw_content: "A collapse is a structural edit, and structural edits are unreviewed by construction: nothing has read the new arrangement. The count rises because the artifact genuinely changed, not because the earlier walks missed things." The remedy prescribes a Cycle Log convention: "the collapse resets the clock: the bar must be met by a walk that restructured nothing."
- **Confidence:** high

### 2026-08-10: A corrected corpus measures the FALSE-positive surface and cannot measure true positives at all [tag: verification]


- **Suggested action:** Codify in PLANNER_TEMPLATE.md under census/diagnostic authoring: when measuring against a corrected corpus, state which half you are measuring — false-positive surface from final states, true-positive surface from intermediate revisions. Never blend into one accuracy figure.
- **Reasoning:** The entry identifies a systematic measurement design error where a census over closed plans conflated two populations. From the entry's raw_content: "matches in a closed corpus are dominated by prose describing the class, not instances of it. Frequency measured there answers 'how often do plans DISCUSS this?' and is read as 'how often do plans COMMIT this?'" The remedy distinguishes the populations explicitly: "Use final states to price the false-positive surface, and intermediate revisions to price true positives. Never blend them into one accuracy figure."
- **Confidence:** high

### 2026-08-10: `pause_for_verdict: always` is a header contract nothing enforces — an agent ran every step of a three-step plan in one dispatch [tag: bellows-integration]


- **Suggested action:** Codify the authoring half in PLANNER_TEMPLATE.md under verdict-gate authoring: at every verdict gate, compare the steps table against commits and deposits before writing the verdict. Rule 46 split — the enforcement half (making pause_for_verdict a runtime-enforced contract rather than advisory) is bellows-owned; FORWARD 46. The mechanism: compare the steps table count against commits and deposits at every gate. Owner: bellows.
- **Reasoning:** The entry demonstrates an unenforced header contract where an agent executed an entire plan in one dispatch. From the entry's raw_content: "The agent executed all three steps in a single dispatch — one step log, 133 turns, three commits, all nine deposits — and the daemon's `steps` table recorded exactly one row: step 1, complete." The cost that matters: "the QA step re-measures work produced by the same agent, in the same context, minutes earlier — so every 're-measure independently rather than reading back' item is satisfied by an agent that already knows the answers."
- **Confidence:** high

### 2026-08-10: When a self-marking agent returns a NEGATIVE result, the missing independence matters far less [tag: verification]


- **Suggested action:** Codify in PLANNER_TEMPLATE.md under verdict adjudication: when an independence guard is missing, assess which direction the bias would have pushed before voiding the result. A negative self-marked finding backed by re-checkable evidence is worth accepting with the gap recorded.
- **Reasoning:** The entry identifies a directional property of independence checks that distinguishes positive from negative self-marked results. From the entry's raw_content: "The finding ran against the author's own hypothesis: a build plan for those four checks had already been drafted and withdrawn, and the census killed all four — zero true positives, 376 false. The bias an independence check guards against is an author confirming what they hoped. A result that demolishes the author's prior work is not the failure mode being guarded."
- **Confidence:** high

### 2026-08-10: A census that measures PRECISION over survivors has not measured the class — the number that decides a check is RECALL against known positives [tag: measurement]


- **Suggested action:** Codify in PLANNER_TEMPLATE.md under diagnostic/census authoring: before running a census on a defect class, confirm the known positives are inside the population being scanned. Report recall and precision as a pair; a disposition citing one without the other is incomplete. Build the labelled positive set first, from whatever artifact recorded the instances.
- **Reasoning:** The entry reports a census whose scan population excluded the hypothesis-generating cycles, rendering its zero result unfalsifiable. From the entry's raw_content: "The covered set excluded both cycles that generated the hypothesis. The build plan's case rested on instances observed in the v2.0 specimen-1 cycle and the collector cycle. Neither appears among the ten drafts scanned." The fundamental measurement error: "Precision over a population with no positives in it is unfalsifiable: any matcher scores zero, including a perfect one." The upstream cause: "The only artifact that preserved these instances was the walk register, and the walk register is not in any measured population."
- **Confidence:** high

### 2026-08-10: A walk's convergence is told by what its findings TOUCH, not by where they came from [tag: drafting-cycle]


- **Suggested action:** Codify in DRAFTING_CYCLE.md §2 as the replacement doneness criterion: classify each walk's findings by what they TOUCH (instruction vs record/commentary), not by origin split. A walk whose findings are nearly all record-class is done. Route into the §2 doneness cluster rewrite as the cluster (A) centerpiece; reconcile with FORWARD 53.
- **Reasoning:** The entry identifies §2's convergence criterion as self-contradictory — the same number serves as both the convergence condition and the noise-floor signature. From the entry's raw_content: "The same number is the doctrine's convergence condition and its noise-floor signature, and at 75% both readings apply. Steering by it cannot distinguish a cycle that is finishing from one that is circling." The measured replacement: "Walk 3: roughly ten of fifteen findings changed instructions an agent executes. Walk 4: two of eight. The instruction surface had converged; the commentary surface had not."
- **Confidence:** high

### 2026-08-10: A gate that reads a token can be silenced by the record RETRACTING that token [tag: mechanization]


- **Suggested action:** Codify the record-authoring half in DRAFTING_CYCLE.md §3: when a record must mention a value a gate keys on, describe it rather than reproduce it, including inside corrections and retractions. After any record edit, re-run the gate and diff the WARN set against its prior state, treating a disappearance as a defect until explained. Rule 46 split — the automated WARN-set diff is bellows plan_lint-owned; FORWARD 50. The mechanism: re-run the gate and diff the WARN set after any record edit. Owner: bellows plan_lint.
- **Reasoning:** The entry identifies a gate-silencing mechanism through legitimate record retraction. From the entry's raw_content: "The check scans the log for a status token and negation-strips a fixed set of prefixes; a struck token inside a retraction is neither a negation nor a claim, and it satisfied the check anyway. The edit touched only the record and changed only the gate's verdict — which is the exact signature §3 names for a log satisfying a check on the step's behalf."
- **Confidence:** high

### 2026-08-10: Mandates and their observers drift because they are written in different places [tag: instruction-design]


- **Suggested action:** Codify in PLANNER_TEMPLATE.md under mandate authoring: each mandate names its QA item inline (e.g. '(observed by Item 8)'), so an unpaired mandate is visible at writing time rather than a walk later. Then verify by constructing the violation and confirming the item reports it. Reconcile with FORWARD 52. The mechanism: a lint check detecting mandates without inline observer references. Owner: authoring + lint.
- **Reasoning:** The entry reports the same defect class — a constraint with no failing observer — appearing four times across three walks. From the entry's raw_content: "a constraint imposed on the executing step with no check anywhere that could fail when it was violated. Each instance was found by a different lens, each fix was individually correct, and each arrived a lens or a whole walk after the mandate it was supposed to guard." The structural cause: "Mandates live in the DEV step and observers live in the QA step, so every new mandate starts life unpaired and stays that way until some later reader happens to notice."
- **Confidence:** high

### 2026-08-10: A mismatched literal probe returns a confident FALSE ABSENCE, and it does it on the verification step [tag: verification]


- **Suggested action:** Codify in DRAFTING_CYCLE.md §2.7: for any absence claim, derive the probe from the target text (open the file and copy the string) rather than composing it from memory. A zero from a composed probe is a hypothesis; a zero from an extracted probe is evidence. Enumerate what IS there and read it rather than asserting what is not.
- **Reasoning:** The entry identifies a systematic probe-construction error that occurred six times in one session, all on verification steps. From the entry's raw_content: "The probe gets written from the phrasing in the author's head — what they meant — rather than from the target text — what they actually wrote. That gap is widest precisely when checking your own prior work, which is when verification matters most and when the author is least able to see it." The mechanism is specific: "Five of the six would have licensed a wrong action: cutting material believed already relocated, or certifying a file that did not conform."
- **Confidence:** high

### 2026-08-10: The walk register is doctrine-ephemeral and practice-permanent — and the permanent copy is the one that did the work [tag: drafting-cycle]


- **Suggested action:** Codify in DRAFTING_CYCLE.md §3: treat the walk register as an output of the cycle, not a scratch buffer — commit it per phase alongside the draft. When a rule directs detail to another location, verify that location outlives the reader the rule anticipates. Reconcile with FORWARD 51.
- **Reasoning:** The entry identifies a doctrine-practice divergence on the walk register's persistence status. From the entry's raw_content: "DRAFTING_CYCLE.md §3 describes the register as a scratchpad file, 'session-local and ephemeral.' Practice has moved the other way: three walk registers were committed on a single day into `governance/knowledge/research/`." The internal contradiction: "If the register does not survive the session, 'move it to the register' is a deletion with extra steps, and the audit trail the bar depends on expires the moment the cycle closes."
- **Confidence:** high

### 2026-08-10: A per-string prohibition did not hold a structural hazard — the record has to leave the gate span, not be worded around it [tag: bellows-integration]


- **Suggested action:** Codify the placement convention in DRAFTING_CYCLE.md §3: record sections (Cycle Log, walk register) must be placed outside any step's span — above the first step heading, not trailing after the last step. When a hazard keeps recurring under a rule that already forbids it, measure recurrence rather than hardening the wording, and ask whether the geometry can change. Rule 46 split — the bellows half is the _extract_step_text span regex fix; FORWARD 45. The mechanism: bound the last step's gate span at a trailing record section. Owner: bellows _extract_step_text.
- **Reasoning:** The entry reports a structural hazard that recurred despite codification, measured four times in one walk. From the entry's raw_content: "The rule is codified, and the class still fired four times in one walk of a single cycle. Different string each time. That is what the rule asks of an author: anticipate every token every gate matches, on the one region that is rewritten every phase and read least often." The geometric fix that worked: "the record sections were moved above `## STEP 1`, out of any step's span."
- **Confidence:** high

### 2026-08-10: A task paragraph accretes correct folds until an agent reads it and acts on a subset [tag: instruction-design]


- **Suggested action:** Codify in PLANNER_TEMPLATE.md under task authoring: author every task as ordered sub-items from the first draft, so a fold lands in a slot rather than at the end of a paragraph. After collapsing a wall, put its region back on the next walk — a re-formed wall means the fix addressed the symptom. Reconcile with FORWARD 54. The mechanism: a check counting instruction-bearing sentences per task block. Owner: plan_lint.
- **Reasoning:** The entry identifies a task-accretion pattern measured across two cycles, where individually correct folds accumulate into unexecutable prose blocks. From the entry's raw_content: "Every fold appends a sentence to the task it corrects. Each sentence is right, and nothing ever removes one. Past some length the block stops being an instruction and becomes a passage — and the agent executes part of it." The recurrence after a fix: "one walk later a fourth had re-formed underneath the sub-steps the collapse had just created. That is the finding: collapsing a wall does not touch the mechanism that builds it."
- **Confidence:** high

### 2026-08-09: The Bellows verdict grammar is continue/stop only — a "redo" is a stop plus a corrected re-deposit, and the correction rides a narrowly-keyed A0 branch [tag: bellows-mechanics]


- **Suggested action:** Codify the verdict-grammar constraint in PLANNER_TEMPLATE.md verdict-gate authoring rules: never promise a verdict the grammar lacks; read verdict.py before naming options at a gate. A redo = stop + re-deposit with a narrowly-keyed A0 branch. Question for Gate 1: Rule 46 split — the verdict grammar itself is bellows-owned; the plan-authoring rule against promising non-existent verdicts is doctrine.
- **Reasoning:** The entry establishes that the Bellows verdict grammar is a closed set (continue/stop only) and prescribes a plan-authoring discipline: "Never promise a verdict the grammar lacks — read verdict.py before naming options at a gate. A redo = stop + re-deposit; the re-deposit's A0 must key on the CONCRETE recorded half-state (greppable facts, not narrative)." This is a governance rule about how verdict gates must be authored in plans — the authoring side of a Rule 46 split where the bellows-owned half is the grammar itself. The incident — "At 328's gate the CEO chose redo and no such verdict exists — check_verdict parses continue|stop, nothing else" — is the measured failure.
- **Confidence:** high

### 2026-08-09: A dash-leading constructed grep pattern parses as an OPTION — exit 2, empty stdout — and a read-the-count rule converts that emptiness into a false answer [tag: probe-integrity]


- **Suggested action:** Codify the constructed-pattern safety rule beside the existing grep -F clause in DRAFTING_CYCLE.md §2.7: every constructed or variable pattern is passed via -e "$PAT" (or after --); and note that two independently-correct hardenings can compose into a trap when one normalizes the symptom of the other.
- **Reasoning:** The entry documents a specific failure class in probe construction: "The sentinel patterns were built at run time by concatenation (correctly, to keep the QA step's own text out of the counts) — but they begin with ---, so grep -c -F "$B" errored as an unrecognized option with NOTHING on stdout." The remedy names a concrete rule: "Every constructed or variable pattern is passed via -e "$PAT" (or after --) — "-F is mandatory" does not cover it." This sits beside the existing grep -F clause in DRAFTING_CYCLE.md §2.7 as a companion safeguard for the same probe-construction region.
- **Confidence:** high

### 2026-08-09: A nine-element compound instruction dropped exactly one element in execution — per-element mechanical asserts are what caught it [tag: instruction-design]


- **Suggested action:** Codify the per-element assert rule in PLANNER_TEMPLATE.md: spec compound outputs as enumerable element lists and give QA one mechanical assert per element. The element most likely to matter (a key another branch consumes) deserves its own named assert. Mechanism candidate: a lint or QA tool that extracts element lists from compound-output specs and generates per-element grep asserts automatically. Owner: plan_lint or QA tooling.
- **Reasoning:** The entry documents compound-drop as a measured recurring class: "328's S2 mandated the History row carry ~nine elements in one long sentence; the executing agent produced a perfect row minus one element (the slug — the re-entry key). Every gate the daemon runs passed; the drop was caught only because QA 1(e) carried a per-element grep." The remedy names a concrete mechanism: "Spec compound outputs as enumerable element LISTS and give QA one mechanical assert per element — the asserts are cheap and the drop class is measured. The element most likely to matter (a key another branch consumes) deserves its own named assert."
- **Confidence:** high

### 2026-08-09: A walk examines the WHOLE artifact, so "no walk has examined this region" is never a true statement — it is the rationalization that hides a cycle folding its own repairs [tag: drafting-cycle]


- **Suggested action:** Route into the §2 doneness-criterion rewrite as part of cluster (A): the entry establishes that §2's rotation-to-unexamined-region criterion silently assumes a STATIC artifact and cannot terminate when every walk folds. The successor criterion must be stated against an artifact that is changing under the reader. Flag (D): v2.0's §2 and §2.7 appear to codify this in full — Gate 1 must measure clause-by-clause whether the current text already carries the substance. Entry names classifying each pass's findings as pre-existing vs fold-introduced and reporting the ratio — a discipline the cycle log must carry, not a mechanism.
- **Reasoning:** The entry provides the strongest measured evidence for cluster (A)'s case: "Categorizing all 19 findings from four confirming passes by origin made it measurable: 14 were defects created by this cycle's own folds; only 5 pre-existed. One pass (walk 4) was 0-for-3 pre-existing — it found nothing but damage from the walk before it." The critical point for §2: "§2's doneness criterion — rotation to an unexamined region coming back dry — silently assumes a STATIC artifact. When every walk folds, a fresh region is always available because folding keeps creating them, so the criterion cannot terminate on its own terms. Any successor criterion has to be stated against an artifact that is changing under the reader."
- **Confidence:** high

### 2026-08-09: An inherited SEVERITY label survives every check that would have caught an inherited factual claim [tag: verification]


- **Suggested action:** Codify the severity-label-as-claim rule: treat a severity or reversibility label as a CLAIM with a probe (not framing), and on a clone diff the parent's risk adjectives too. Target artifact to be decided by Gate 1 — the rule intersects plan-authoring (PLANNER_TEMPLATE.md, where label verification at authoring sits) and cycle methodology (DRAFTING_CYCLE.md §2.7, where clone-diff discipline sits). v2.0 did NOT codify this.
- **Reasoning:** The entry documents a measured failure where a severity label ("irreversible") traveled by clone through 125 findings, three walks, three ACID passes, and a five-seat panel without verification: "It dissolved in one query at the gate, and only because the CEO pushed back on the consequence rather than the claim: the seven rows share exactly one distinct prior state, and the write touches 4 of 15 columns, none of them content. The reversal is a single exact statement." The asymmetry is load-bearing: "The shop has at least three rules that would have caught this as a factual claim... None of them fire on an adjective."
- **Confidence:** high

### 2026-08-08: A recognized-value enum lives in every tool that reads it — ship one copy and the feature fails its own tooling [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md plan-authoring section: before adding any enum value, census EVERY copy — code branches, lint token sets, claim validators, and governance prose — with grep -F across the repo AND the template; ship all copies in one plan or enumerate the deferral explicitly. Treat the census as the plan's own Site list with a both-edits-or-neither clause per copy-pair. Question for Gate 1: could the multi-copy census be mechanized as a lint check that verifies all enum copies are updated together?
- **Reasoning:** The entry identifies the multi-copy enum problem as a systematic class, not a one-off. A new recognized value shipped in one code branch while its copies lived in three other locations. The specific instance: plan 317 added a pause_for_verdict mode to header_says_pause, but "the cold panel found the recognized-value list also lives in scripts/plan_lint.py (hard-FAIL at preverify) and validators.py (claim-time check)." The recurrence at plan 320 — prose copies of the same enum drifting for months — demonstrates that the class is structural (one value, many readers) rather than incidental, and argues for a census-first protocol binding all copies into the plan's Site list.
- **Confidence:** high

### 2026-08-08: Argue a trade from the population the change actually touches — a cross-population headline can understate the real price [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md trade-off argumentation section: for any headline rate justifying a change, compute the rate over the IN-population (the rows the change actually affects) and present that number first. Name the strongest single counterexample from the IN-population and argue against it specifically.
- **Reasoning:** The entry measures the gap between headline and in-population rates: "Plan 317's Why-section priced mechanization at the 3.08% cross-population finding-rate — but 7 of the 10 measured catches fell INSIDE the slice the mode mechanizes, making the IN-population rate 4.1% (higher, because the headline averaged over QA and terminal pauses that stay human)." The counterexample test: "The strongest counterexample (plan 203, a tranche plan saved by a rote-looking pause) sat in exactly the population named as the opt-in target."
- **Confidence:** high

### 2026-08-08: A truth-restoration edit is held to its own standard in both directions — overstating OR understating enforcement carves a new falsehood [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md doc-correction section: when correcting stale doc claims about enforcement, read the ENFORCEMENT implementation first and state its exact tier (reject/warn/silent, and at which lifecycle point); both over- and under-statement are the same defect. Sweep the correcting plan's own prose for the banned claims.
- **Reasoning:** The entry measures enforcement-tier misstatement: "its own drafting cycle caught the plan about to carve three new ones: 'plan_lint hard-checks at deposit' (nothing runs it mechanically — Planner-run only), 'the daemon ignores STOP prose entirely' (a claim-time validator warns on it), and 'claim-time validation, warn-only' (the dispatch_mode field is severity-REJECT — the shipped validator has three tiers). Each replacement had to be re-worded to the exact fact, no stronger and no weaker."
- **Confidence:** high

### 2026-08-08: A filter can silence its own evidence base — re-check evidence coherence after every narrowing fold [tag: drafting]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §2.6: after any fold that narrows a check's candidacy (filter, exclusion, allowlist), re-trace every cited evidence case through the NARROWED spec and confirm each can still fire. A Why-table citation is a claim about the SHIPPED shape, not the prototype's — re-verify the pairing whenever either side moves. Flag (D): the evidence-attack brief exists at v1.7; residue is the after-every-fold cadence.
- **Reasoning:** The entry demonstrates that a narrowing fold can destroy the evidence base for its own justification. The check's cited evidence consisted entirely of cases the new exclusion would filter out: exec-324's check (o) received a Deposits/Scope exclusion, yet "the census's ONLY measured true positives were relative deposit paths, exactly what the exclusion removed from candidacy." The subtlety is that the Why-table citations looked honest — only tracing each cited fire through the shipped filter revealed the silencing. This argues for a mandatory re-trace after any candidacy-narrowing fold, verified against the specific evidence cases, not the abstract justification.
- **Confidence:** high

### 2026-08-08: A specified test fixture can FORCE a guard-weakening — assert degenerate exits against the pre-existing behaviour, not an ideal [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md test-authoring section: for every degenerate fixture, run the CURRENT implementation on the input first and assert its measured behaviour, carving out only what the change intends to alter. Treat a fixture no correct implementation can satisfy as a defect in the PLAN, the same severity as a defect in code.
- **Reasoning:** The entry identifies the test-fixture guard-weakening class: a fixture that specifies a wrong expected outcome can FORCE a developer to weaken the very guard it is testing. In exec-324, a degenerate-input fixture asserted exit 0 on an unparseable header, but the shipped check correctly FAILs that case with exit 1 — so "a literal DEV agent honoring the fixture as written would have had to WEAKEN (a) to make the test pass." The fix is directional: assert the CURRENT measured behaviour first, then carve out only the delta the change intends. A fixture that conflicts with the correct implementation is a plan defect of the same severity as a code defect.
- **Confidence:** high

### 2026-08-08: A checker's mechanics approximate its condition — the gap fires in both directions, and a verifier can be one mesh finer than its check [tag: instrumentation]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §3 beside the earned-phrasing clause: when writing any record a mechanical check reads, state the check's exact matching semantics beside the earned-clear condition, and never satisfy or dodge it by wording the state has not earned. When a verifier is built independent of its target, expect and pre-classify the over-match band — a verifier fire is a QUESTION about which side is right, not automatically a defect in the target.
- **Reasoning:** The entry establishes that the gap between a checker's mechanics and its intended condition is bidirectional: it can both over-match (flagging correct records) and under-match (clearing incorrect ones). Three independent specimens in one session demonstrated this: a closing-fold WARN that "cleared one phase EARLY (the lens line truthfully recorded a dry re-read while the cycle was still open — the mechanics see the line, not the pending pass)," a retraction narration that tripped a phrase-matching check by quoting the caught phrase rather than exhibiting it, and a QA halt check built broader than its exclusion. The prescriptive contribution is the pre-classification: build the over-match band into the check's documentation so each fire is adjudicated against a known taxonomy rather than investigated as a fresh surprise.
- **Confidence:** high

### 2026-08-08: Panel economics, first metered run — HIGHs come from aimed briefs, ~40% of late findings are residue a script could drain [tag: drafting-cycle]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §2.6: aim panel seats at deletion premises and the clone-diff explicitly — the register's plain lenses under-produce cold. Run the mechanical residue battery (lint + consistency sweeps) after every culmination so readers hunt novel defects, not their predecessors' sync debt. Meter every panel with the 563k/45 baseline as the comparator. Flag (D): the seat-brief registry landed at v1.7; residue is the residue-battery cadence and the metering convention.
- **Reasoning:** The entry presents the first metered panel run: "five-seat panel: 94.6k/104k/117.5k/141.6k/105.8k ≈ 563k subagent tokens, 45 findings (7·9·7·9·13), all author-verified real, zero design re-opens — ~12.5k tokens per finding." The composition finding: "every HIGH came from the two AIMED briefs (evidence-base attack; clone-diff against both parents — fourteen recovered 306 hardenings), the lens-replication seats produced MEDIUM hardening."
- **Confidence:** high

### 2026-08-08: Close-commit counts were wrong or absent 4-for-4 — enumerate populations by PATH, reconcile by value, never trust a narrated count [tag: verification]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §2.7: any population a measurement depends on is enumerated mechanically (git log --follow by PATH, SELECT by key range) — a narrated count is a label, never the filter or the gate. When two sections of one artifact each state a total over the same population, emit the reconciliation line at authoring; a reader-visible gap without one is a defect.
- **Reasoning:** The entry measures: "Diag-322 measured every close-commit drafting-count against path enumeration: 311 claimed 30 (path says 16), 317 claimed 21 (14), 315 claimed 9 (8), 320 stated none." The self-referential finding: "Its own deposit then carried the same class inward: Q1's declared finding-units (190) vs Q2's classified rows (174), each printed transparently, never cross-reconciled."
- **Confidence:** high

### 2026-08-08: The shell's cwd resets between calls — three phase commits landed in the WRONG repo while printing success; cd-first plus a toplevel assert is the whole fix [tag: process-discipline]


- **Suggested action:** Codify the cd-first and toplevel-assert commit protocol in PLANNER_TEMPLATE.md: every compound touching a repo starts with cd /abs/path as its first token; every commit compound ends by printing git rev-parse --show-toplevel and treats a wrong or missing print as NOT COMMITTED. Question for Gate 1: the toplevel-assert could be a mechanical check in bellows (Rule 46 split candidate).
- **Reasoning:** The entry prescribes a concrete authoring protocol for commit compounds: "Every compound touching a repo starts with cd /abs/path as its FIRST token — never trust cwd persistence, never lead with cp. End every commit compound by printing the toplevel and treat a missing or wrong print as NOT COMMITTED." This is a plan-authoring rule about how commit steps must be structured, governing the PLANNER_TEMPLATE git-commit mechanics section. The incident — "Relative-path commit compounds landed lens-2/lens-3/a1 culminations in the shop root (its knowledge/ tree absorbed the cp) while git log -1 printed the new hash — in the wrong repo — three times" — establishes the failure class that the rule prevents.
- **Confidence:** high

### 2026-08-07: A continue verdict is a one-bit channel — a plan reading approval from advancement converts every continue into that approval [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md halt-with-options authoring section: when a halt offers options, the accepting branch must banner WHICH option it inferred at the next gate the CEO reads, so a mis-read costs one verdict gate rather than the run. Question for Gate 1: Rule 46 split — the verdict-channel constraint (continue/stop is one bit) is bellows-owned; only the authoring-side rule (banner the inferred option) belongs in PLANNER_TEMPLATE.md. Route the bellows-owned half to the owning register.
- **Reasoning:** The entry measures the structural limit of the verdict channel: "a continue issued for ANY reason ('investigate meanwhile', the standing benign-gate-failure habit) is structurally identical, and no later step can distinguish the intents." The mitigation was visibility: "every step running under the inferred state opens its chat message and Receipt with an OPERATING-UNDER banner naming the conversion, so a mis-read costs one verdict gate, not the run."
- **Confidence:** high

### 2026-08-07: The confirming pass measured composition-clean and literal-dirty in the same pass, then ran dry [tag: drafting-cycle]


- **Suggested action:** Route into the §2 doneness-criterion rewrite (cluster A): add rule to DRAFTING_CYCLE.md §2/§3 requiring confirming-pass yields to be reported BY CLASS (machinery vs record), with a record-only yield recognized as the signature that the artifact converged before its account of itself did. Cluster (A) entry — route as part of the §2 coherent rewrite with entries 270, 284, 294, 300.
- **Reasoning:** The entry separates two distinct bars for confirming-pass evaluation. The composition bar asks whether any finding changes what an agent will DO; the literal dry bar asks whether findings reached zero. Plan 311 measured the divergence: "By the composition bar (no finding changes what an agent will DO) the pass was clean; by the literal dry bar it was not." This is the third measured instance, and the first where a single culmination of record-only folds bridges the gap — establishing that record decay is a predictable phase, not an anomaly, and that the two bars serve different verification purposes.
- **Confidence:** high

### 2026-08-07: Three constraints opened from the batch's own entries were breached by the folds that followed [tag: drafting-cycle]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §2.8: after ANY fold, re-check it against the ledger's newest constraints specifically — the newest are the most breached because subsequent folds were drafted under the old habits. Three same-cycle breaches of freshly-opened constraints is the strongest evidence for pricing mechanization of a constraint over another prose restatement.
- **Reasoning:** The entry identifies a temporal vulnerability in constraint governance: constraints opened FROM the batch being processed are the ones most likely to be breached by later folds, because the habits those folds embody predate the constraint. Three distinct constraints exhibited this pattern in one cycle: "C14 (producer-sited rules), C15 (name the consumer's artifact), and C17 (manifest-pinned tranches) were each opened from the very batch being ingested — and each was then violated by a LATER fold in the same cycle." The recurrence pattern (three independent breaches of independently-opened constraints) argues for a systematic post-fold re-check rather than treating each as isolated.
- **Confidence:** high

### 2026-08-07: id_sequence at authoring is a prediction — an in-window dispatch consumed it [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md deposit-discipline section: treat any authoring-time id as a prediction carrying a verify-at-deposit clause that NAMES every site the id appears in (backup glob, copy-aside, resume-glob guard, filenames). At deposit: re-read id_sequence, re-token all sites to the actual id, and record the drift as retraction history.
- **Reasoning:** The entry reports a near-miss: "The cycle plan was authored against id_sequence 310; between authoring and deposit the CEO deposited an invoice-pulse diagnostic that claimed 310, and the plan deposited as executable-311 only because its own verify-at-deposit clause mandated the re-read and named every filename site the id token appears in." The key insight: "The clause only works if it enumerates the sites — a bare 'verify the id' leaves the glob tokens stale."
- **Confidence:** high

### 2026-08-07: The untargeted confirming pass caught the record's own three-line decay [tag: drafting-cycle]


- **Suggested action:** Route into the §2 doneness-criterion rewrite (cluster A): add rule to DRAFTING_CYCLE.md §2.7/§3 requiring the confirming pass to be untargeted (precisely because record decay hides from aimed passes) and requiring any phase that completes a tracked structure to sweep the record lines that track it in the same culmination. Flag (D): v2.0 codified the closing-record re-read and the Cycle-Log-as-covered-region; residue is the sweep-the-tracking-lines clause. Cluster (A) entry with 267, 284, 294, 300.
- **Reasoning:** The entry documents record decay invisible to aimed passes: "Only the untargeted whole-artifact confirming pass found them: every earlier pass had been aimed at machinery, and the record is the one region no finding-driven pass ever re-reads." The specific failure: "the Cycle Log's Walks header still read 'the cold panel owed', the Conflicts line predated the panel, and the Closing listed future targets for work already done differently — three lines in the most-rewritten region, contradicting the state every other line certified."
- **Confidence:** high

### 2026-08-07: The three-tranche split held classification quality — no inter-tranche cliff at 3.2x the record batch [tag: process-discipline]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md cycle-methodology section: for large classification batches, prefer manifest-pinned tranches over a single saturated step; carry the per-tranche depth distribution (floor, ceiling, ratio range) as the standing calibration instrument across cycles. The split is validated at 3.2x the record batch with no inter-tranche cliff.
- **Reasoning:** The entry measures: "QA row 9's per-tranche depth distributions: A 100-206/0.155-0.361, B 59-188/0.102-0.303, C 91-266/0.145-0.439 — no inter-tranche cliff, no tail decay, batch minimum match 59 against the 40 floor." The key finding: "the measured risk at this scale was never classification quality but RESUME complexity, where all of the cycle's high-severity drafting findings lived."
- **Confidence:** medium

## Instrumentation


### 2026-08-10: Measure how many DIALECTS a record has before computing anything from it [tag: instrumentation]


- **Suggested action:** Codify in DRAFTING_CYCLE.md §2.7: before computing from a record, count its dialects — sample the shape, not just the presence. Make 'unparseable' a reported outcome with the offending line attached, never a skip. Ask structural questions with structural probes, not file-level searches.
- **Reasoning:** The entry reports a concrete instrumentation failure where a parser encountered multiple record forms in a single corpus. From the entry's raw_content: "the corpus carries at least three distinct forms of the same record — canonical (`w1 2 folded; w2 dry`), an arrow form (`w1 → v1: 4 folded`), and a bare status word (`Destruction: pending.`)" A second measurement compounded the error: "the field the collector existed to gather appeared in 0 of 61 logs in machine-readable form. Two plans 'had' it — in narrative prose on a running-tally line, which a file-level `grep -l` reports as present and a structural parse correctly does not."
- **Confidence:** high

### 2026-08-09: plan_lint's expected-WARN set is LOCATION-dependent, so declaring it from the drafting path declares the wrong thing [tag: instrumentation]


- **Suggested action:** Codify the lint-at-deposit-resolution rule in DRAFTING_CYCLE.md §5: lint at the deposit path resolution before declaring the expected state, and state the location beside the declaration. Mechanism: bellows or plan_lint should enforce that the expected-WARN declaration names the resolution it was measured at, and re-run at deposit. Owner: bellows (deposit pipeline).
- **Reasoning:** The entry documents a measured location-dependence in plan_lint: "Plan 334 declared exactly three WARNs, measured with the draft sitting in scratchpad/. At the deposit filename in a temp directory it returned one. At the real deposit resolution it returned two. All three runs were of the same bytes." The mechanism is identified precisely: "project_root is derived as the path segment before /knowledge/, falling back to a walk up to the nearest .git. The (o1) path-existence check then resolves every candidate against that root." The remedy names a concrete practice: "Lint at the DEPOSIT path resolution before declaring the expected state."
- **Confidence:** high
