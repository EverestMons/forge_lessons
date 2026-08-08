# Lessons Report — 2026-08-07


## Summary


| Category | Count |
|---|---|
| governance_rule | 51 |

**Total proposals:** 51


## Governance Rule


### 2026-08-07: A conformance probe must match the REPRESENTATION, not the spec's prose [tag: verification]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §2.7 beside the grep -F clause: a conformance probe must match the artifact's representation (regex, table, computed form), not the spec's prose literals; before recording absence, read the implementation site; the positive control must use the same representation as the target.
- **Reasoning:** The entry measures: "grep -F 'triggers fired' and grep -F 'proven-clone' both exited 1 against plan_lint.py — the two panel-critical hardenings looked ABSENT from the shipped code. Both were present and faithful: the spec's literals ship as regexes, and a literal probe cannot see a spec literal implemented as a pattern." The false alarm was caught only because option (D) forced reading the actual check bodies. No Family line; placement derived from body. governance_rule because the fix is a documentary verification rule about probe construction, not a tooling change.
- **Confidence:** high

### 2026-08-07: A fix can break its own DESCRIPTION — re-verify the describing sentence after the fold [tag: drafting]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §2.7: after any fold, re-verify every factual claim in the fold's own text against the post-fold artifact (counts, presences, behaviours); when a fix must reference the hazardous token it removes, reference it by description or measurement, never by exhibiting it; author-verify a proposed fix by the same method that found the defect.
- **Reasoning:** The entry measures three instances in one session: "Plan 306's delimiter fold replaced a glyph with words — and the replacement sentence still claimed the glyph occurred 'exactly once'; the fold had removed the occurrence it counted." And: "A cold reader's proposed fix for that same defect spelled the NEW delimiter as a glyph — which would have re-planted the bomb the fix existed to remove." The class is identified as: "a fold edits the artifact AND silently invalidates the prose describing the fold." No Family line; placement derived from body. governance_rule because the fix is a documentary post-fold verification rule, not a tooling change.
- **Confidence:** high

### 2026-08-07: A directional insert on a PREFIX anchor lands on the wrong side and passes the line-count proof [tag: mechanics]


- **Suggested action:** Add new rule to PLANNER_TEMPLATE.md (edit-mechanics area): a directional insert anchors on a COMPLETE line with the full composition spelled in the new_string; after fixing a mechanism defect at one site, sweep the plan for the same mechanism in mirror form; add one check that spans the would-be damage point.
- **Reasoning:** The entry measures: "Plan 307's E4 anchored 'insert AFTER' on the first 60 chars of a 780-char line: the natural anchored-edit form inserts BEFORE the prefix" — and a mirror-image defect survived at E6 where "mis-landing SPLITS the anchor line and every mandated check passes on the split (the presence grep, the count, every date pin — all live inside the intact fragments)." No Family line; placement derived from body. governance_rule because the fix is a documentary rule about how directional edits are anchored in plans, not a tooling change.
- **Confidence:** high

### 2026-08-07: Commit scoping lives on the COMMIT, not the add [tag: mechanics]


- **Suggested action:** Add new rule to PLANNER_TEMPLATE.md (git-commit rules area): git commit -m '...' -- <path> with the pathspec on the COMMIT, never a bare commit after git add; pair with post-commit assertion git show --name-only --format= HEAD printing exactly the intended paths.
- **Reasoning:** The entry measures: "git add <path> && git commit is not a path-scoped commit: a bare git commit commits the ENTIRE index, so any foreign change already staged rides into the commit silently — and in a root repo that is the CEO's live working area, pre-staged entries are a normal state." It notes that every check passed on this failure because "the content hash reads only the intended blob; the log check sees only commits touching the intended path." No Family line; placement derived from body. governance_rule because the fix is a new documentary rule about commit scoping, codified nowhere currently.
- **Confidence:** high

### 2026-08-07: Line numbers cited inside shipped code are load-bearing couplings for every doc edit [tag: instrumentation]


- **Suggested action:** Add new rule to PLANNER_TEMPLATE.md (doc-edit rules area): before editing a doc, grep the codebase for :NN-style line-number citations of it — each is a hard constraint on the edit map; prefer in-place rewrites above cited lines, insert only below; verify by value not arithmetic (the cited line still says the cited thing); when writing new checks, cite by section anchor or literal, not line number.
- **Reasoning:** The entry measures: "The shipped (k) WARN text cites doctrine BY LINE NUMBER — (§2.6 :75) — so any doctrine edit that changes the line count above 75 breaks a citation inside running code, silently." It describes the consequence: "Plan 307's entire edit map was designed around this: in-place rewrites above the cited line, insertions only below it, and QA asserting the coupling BY VALUE." No Family line; placement derived from body. governance_rule because the fix is a new documentary rule about how doc edits interact with code citations, not a tooling change or procedural mechanism.
- **Confidence:** high

### 2026-08-07: A parent deposit can carry a DIRECTIVE to a future plan — sweep for them when authoring the successor [tag: drafting]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md (Rule 27/58 area): when authoring a plan that implements a diagnostic's findings, sweep the source deposit's closing sections for directives addressed to a future plan — they are requirements, not commentary; machine-parsed conventions (e.g. 'implements diagnostic N') deserve a grep-verifiable check at deposit time.
- **Reasoning:** The entry measures: "Diag-300's deposit closed with an instruction addressed to a plan that did not exist yet: 'their plan must contain the literal phrase implements diagnostic 300 — the daemon parses it at claim.' The landing plan (307) was drafted three sessions later from the baton and the decision record — and the directive lives in neither." It identifies the structural issue: "A directive addressed to a future plan is invisible to every review of the plans in between; only a diff against the SOURCE deposit finds it." No Family line; placement derived from body. governance_rule because the fix is a documentary authoring rule about sweeping parent deposits.
- **Confidence:** high

### 2026-08-07: A threshold clause written at a POLE silently drops the mid-band [tag: design]


- **Suggested action:** Add general rule to PLANNER_TEMPLATE.md: for any threshold or quantifier clause, construct the mid-band cases BEFORE shipping (most-but-not-all, sibling verbs, aggregate-of-small-parts); price each as caught, dropped-and-accepted, or dropped-and-unpriced; record acceptance in the artifact with a boundary test. The specific T-1/T-2 mid-band is SETTLED (1.5 History, consequence 4) — scope to the general rule only.
- **Reasoning:** The entry measures the every-row clause preserving T2 at the 100% pole: "Cold seat 2 constructed the band it drops: a most-rows mutation (200 of 222), a full-table DELETE ('mutates' vs the trigger's own 'deletes' verb), a schema migration, multi-table narrow writes. All compute T2 today; all compute T1 under the clause." The core finding: "The record had priced only the poles — the census cases and the constructed 100% case — never the band between them." No Family line; placement derived from body. governance_rule because the fix is a general authoring principle about constructing mid-band test cases for threshold clauses.
- **Confidence:** high

### 2026-08-07: A recovery branch must produce everything the downstream consumers read [tag: design]


- **Suggested action:** Extend Rule 56/62 area in PLANNER_TEMPLATE.md: when adding a bypass/recovery branch, enumerate every downstream reader of the bypassed block's outputs — each needs the branch to supply an equivalent; test recovery path's artifacts against the consumer's checks, not the happy path's. Cluster with entry 222.
- **Reasoning:** The entry measures: "Plan 307's A0-PRE recovery branch ('work already committed — skip the edits, deposit the log') skipped the commit block — which is where DOC_SHA gets pinned. Step 2's Q0 consumes DOC_SHA unconditionally." The consequence: "The exact death-state the branch was built for would have reached QA with a dev log missing the value QA halts without — the recovery path was correct about the PAST and silent about the FUTURE." No Family line; placement derived from body. governance_rule because the fix extends the existing recovery-branch rules with a downstream-reader enumeration requirement.
- **Confidence:** high

### 2026-08-07: `grep -c` counts LINES — an intra-line duplicate is invisible to it [tag: verification]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §2.7 beside the count-is-not-value clause: a presence check for content that can duplicate intra-line uses the occurrence form (grep -Fo | wc -l), never -c; validate the instrument against a CONSTRUCTED failure, not only the success path.
- **Reasoning:** The entry measures: "An in-place tail-extension edit re-applied lands both copies of the new content on ONE line: every grep -Fc presence count still prints 1, wc -l is unchanged, and a sha pin then certifies the corruption." The occurrence form is proven: "grep -Fo -- <substring> <FILE> | wc -l prints 2/1/0 across doubled/correct/absent (validated by execution)." The general principle: "a check's instrument must be able to REPRESENT the failure state it guards." No Family line; placement derived from body. governance_rule because the fix is a documentary verification rule about which instrument to use for presence checks.
- **Confidence:** high

### 2026-08-07: The closing record is pass-unexamined BY CONSTRUCTION [tag: drafting]


- **Suggested action:** SHAPE-DECISION CLUSTER (A): routes into the reserved CEO decision on drafting-cycle shape (baton item 2). The substance — the closing record is pass-unexamined by construction and needs an adversarial re-read of just the closing prose — is evidence for how the drafting cycle's terminal blind spot should be governed post-shape-decision. Sibling of entry 244.
- **Reasoning:** The entry measures: "The shop's first post-dry-close ACID pass (exec-309, run for the measurement) raised 2 — BOTH in closing prose written after the final pass ran; one claimed exactly what its cited precedent declines to claim." The structural finding: "A dry confirming pass certifies everything except the paragraph that records it: the terminal blind spot is structural, not accidental." No Family line; placement derived from body. governance_rule because the fix proposes a post-close re-read rule — a documentary discipline for the drafting cycle's closing process.
- **Confidence:** high

### 2026-08-07: A foreign constraint id cited by bare number binds to the LOCAL ledger [tag: drafting]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §2.8: foreign constraint and finding ids are ALWAYS namespaced (e.g. '301's C24(a)', 'diag-302's C7'); when a fold applies a rule, verify the rule has a LOCAL ledger row — applying an unledgered rule is how a repeatedly-violated constraint stays invisible.
- **Reasoning:** The entry measures: "A fold cited '(C7)' meaning another plan's C7 (single-siting); the local C7 was an unrelated premise — the cite pointed at the wrong constraint and the rule actually applied was ledgered nowhere, leaving a twice-violated constraint without a row." The fix is twofold: namespace foreign ids always, and verify applied rules have local ledger rows. No Family line; placement derived from body. governance_rule because the fix is a documentary rule about constraint-id namespacing and ledger-row verification in the drafting process.
- **Confidence:** high

### 2026-08-07: A true record invisible to the checker's grammar reads as false — write records in the checker's representation [tag: instrumentation]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §3 beside the earned-phrasing clause: when a gate misreads an honest record, read the check's implementation and reword the record only when the truer statement is also the legible one — never satisfy a checker with wording the state has not earned; the reword must increase accuracy, not just legibility. Sibling of entry 252.
- **Reasoning:** The entry measures: "Exec-309's dry confirming pass was first recorded in prose rows the closing-check's lens-line regex cannot match, so the gate kept WARNing off the last ACID row despite the honest dry close. Recording the dry pass PER-LENS was simultaneously more accurate and checker-legible; the WARN cleared earned." The principle: "Probe-must-match-representation applies to WRITING records, not only reading them." No Family line; placement derived from body. governance_rule because the fix is a documentary rule about how records are written to be both accurate and machine-legible.
- **Confidence:** high

### 2026-08-06: A success criterion must declare its polarity — and three individually-correct patches mean the REGION is wrong, not the patches [tag: planner-discipline]


- **Suggested action:** Add a polarity-declaration rule to PLANNER_TEMPLATE.md in the diagnostic-authoring area: when a question reports a number that can move in two directions, state which direction is good and for whom, or state that both are legitimate and the weighing is not the question's. Scoped to the polarity residue; the per-region half (three patches means the region is wrong) is already codified in §2.8 (1.4).
- **Reasoning:** The entry measures that three individually-correct patches to a question block turned out to be the same defect — polarity contradictions where "C2 killed the proposal on WIDE firing while C3 killed it on NARROW" and C4 priced breadth as a virtue where C2 treated the identical movement as fatal. The resolution was one declared rule: one quantity, two legitimate opposed values, no verdicts in any question. The proposed polarity-declaration rule is a documentary rule change for diagnostic authoring in the governance template.
- **Confidence:** high

### 2026-08-06: The error that FLATTERS your own argument is the one no gate catches [tag: planner-discipline]


- **Suggested action:** Add a self-flattering-error rule to DRAFTING_CYCLE.md §2.7: re-read populations from the upstream table row by row between sections; diff same-population sites; ask whether convenient facts make your own argument work before trusting them.
- **Reasoning:** The entry measures that a flattering substitution in a motivating claim survived a walk, a culmination, an ACID pass, and a second culmination — "The substitution was not random. 274's finding IS clone-drift; 281's is not characterised as drift at all. Swapping the two made the motivating claim true." No gate catches this class because plan_lint reads structure and consumer sweeps probe wording. The proposed fix is a documentary rule change requiring row-by-row population re-reads and same-population diffs.
- **Confidence:** high

### 2026-08-06: A recorded lesson does not bind the author who recorded it — measured four times in one cycle [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a constraint is recorded in a plan, add the check that would catch its violation in the same edit; treat recurrence of a recorded lesson as evidence it needs mechanising and route to the forge rather than restating in prose. Gate 1 should also consider whether the recurrence-to-mechanisation routing principle belongs as a standing Gate-1 instruction.
- **Reasoning:** The entry measures four recurrences in one cycle of the same author's own recorded constraints and concludes: "a rule in prose — in LESSONS.md or in the plan's own ledger — has no mechanical consequence" and "the author is the least reliable enforcer of a rule they have just written." It proposes preferring executable rules over remembered ones and treating recurrence after recording as evidence the lesson needs mechanising. This is a governance_rule because the actionable fix is a documentary authoring principle — add checks alongside constraints, never rely on memory alone — not a tooling change or procedural checklist.
- **Confidence:** high

### 2026-08-06: The Cycle Log is the LEAST-examined region precisely because it is rewritten every phase [tag: drafting-cycle]


- **Suggested action:** SHAPE-DECISION CLUSTER (A): routes into the reserved CEO decision on drafting-cycle shape (baton item 2). The substance — walk the Cycle Log as a region on a schedule, label narrative blocks with their phase, name coverage rules not counts, count record-decay separately — is evidence for how the cycle log should be governed post-shape-decision.
- **Reasoning:** The entry measures: "Walk 3 of diagnostic 301 was aimed at the Cycle Log, which no lens had ever read. Six of its eight findings landed there, and every one was the RECORD decaying while the artifact converged." It identifies that attention followed what each phase changed, never what changes accumulated into: "The region rewritten most often was the region reviewed least." No Family line; placement derived from body. The substance proposes scheduled region-walks and phase-labelled narrative blocks — governance_rule because the fix is documentary rules about how the Cycle Log is reviewed and maintained.
- **Confidence:** high

### 2026-08-06: The dry condition is unreachable by construction — four consecutive plans have closed without it [tag: drafting-cycle]


- **Suggested action:** SHAPE-DECISION CLUSTER (A) — CENTERPIECE: this IS the shape decision. Routes into the reserved CEO decision on drafting-cycle shape (baton item 2). The entry proposes closing on composition rather than dryness, measuring the cycle across plans for convergence, and treating judged stops as the normal outcome.
- **Reasoning:** The entry measures that the dry condition is unreachable: "every culmination creates new unexamined surface — folding N findings is N edits no lens has read — and the artifact grows while doing it. The termination condition is stated in terms of a state the mechanism actively prevents." Four consecutive plans (296, 298, 300, 301) closed without meeting it. It proposes: "Close on COMPOSITION, not dryness: stop when a full walk produces no finding that changes what an agent will DO." No Family line; placement derived from body. governance_rule because it proposes a fundamental change to the drafting cycle's termination criterion.
- **Confidence:** high

### 2026-08-06: An UN-walked plan lints CLEAN while a fully-walked one WARNs — measured on one artifact across one cycle [tag: instrumentation]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md §3: when declaring a tier whose gate you cannot yet satisfy, phrase the status line so it CANNOT match the gate's pattern until the condition is true; rewrite to canonical only once earned. An earned WARN ships unsilenced. The gate half (not-run token treated as failing) is bellows-owned — Rule 46 question for Gate 1, route to bellows FORWARD.
- **Reasoning:** The entry measures: "Diagnostic 301 at v0 — zero lens passes, every lens line reading 'not run' — returned 3 PASS / 0 WARN, because 'not run' contains no fold-token. The same file after three walks, three ACID passes and six culminations returns 2 WARN / 3 PASS." The key insight is that "the gate is silent on the plan that has had no review and speaks on the plan that has had the most." No Family line; placement derived from body. governance_rule because the codifiable residue — phrasing status lines so gates cannot prematurely pass, shipping earned WARNs — is a documentary authoring discipline, not a tooling change.
- **Confidence:** high

### 2026-08-06: The negative-result standard was adopted for agents that morning and never applied to my own probes [tag: verification]


- **Suggested action:** Gate 1 should measure clause-by-clause against 1.6's (D) clause to determine what is already codified. Residue candidates for PLANNER_TEMPLATE.md or DRAFTING_CYCLE.md §2.7: the zsh no-word-split trap (a probe that fails identically to a true negative), path-relativity of recorded fields (a stored relative path rarely resolves against the current repo), and the principle that a standard written for an agent binds the Planner too.
- **Reasoning:** The entry records the author producing four confident NOT FOUND lines that were all wrong: "All four existed, correctly archived." Two compounding probe errors made this invisible: "The path field was relative to each plan's own target project — three different repositories — and the search covered only one" and "zsh does not word-split unquoted parameter expansions, so the first variable took the whole string, the second came out empty." The entry itself notes it is the source of 1.6's (D) clause. governance_rule because the residue proposes documentary verification rules beyond the already-codified positive-control requirement.
- **Confidence:** high

### 2026-08-05: Naive probes degrade as an artifact accumulates its own retraction history [tag: verification]


- **Suggested action:** Add a probe classification rule to DRAFTING_CYCLE.md §2.7 beside the existing probe rules: any probe over a plan that carries retractions must classify each hit as instruction or retraction-of-instruction before reporting.
- **Reasoning:** The entry measures that §2.7's retraction-in-place discipline structurally degrades probes — "a well-run cycle deliberately accumulates text of the form 'an earlier form said X — X was wrong.' Every such retraction is a literal instance of X sitting in the file." Two of seven probes fired false alarms because retraction text matched the detection pattern, and at least one would have been folded without checking. The fix is a documentary rule change requiring hit classification before reporting. This is governance_rule because it proposes a verification methodology rule for plan drafting.
- **Confidence:** high

### 2026-08-05: A closing line written before the cycle's last phase is wrong by construction [tag: planner-discipline]


- **Suggested action:** The entry has two halves. The shape-decision half (cluster A) routes into the reserved CEO decision on drafting-cycle shape per baton item 2. The independently codifiable half: add a closing-line ordering rule to DRAFTING_CYCLE.md §2.7/§3 requiring the sequence walk → culminate → final ACID → then close, with counts stated as of a named completed phase.
- **Reasoning:** The entry measures that a closing line written one phase early stated stale counts and a falsified last-event assertion — "Written one phase early it is not merely incomplete — it is flattering by precisely the margin the missing phase would have removed." A fifth ACID pass was still owed and found all three claims defective. The closing line is load-bearing under §2.7 and writing it before the last phase produces systematic optimistic bias. The closing-line ordering rule is independently codifiable in DRAFTING_CYCLE.md; the evidence about the gap between taking a stop and having finished is shape-decision evidence. No Family line present, placement derived from body.
- **Confidence:** high

### 2026-08-05: An overloaded token appears in prose far more often than in its real position — first-match probes land hundreds of lines early [tag: verification]


- **Suggested action:** Add a structural-search anchoring rule to DRAFTING_CYCLE.md §2.7 beside the count-is-not-value clause: anchor every structural search line-anchored (^## ), strip fenced blocks and blockquotes before matching any token that also appears in prose.
- **Reasoning:** The entry measures that nine prose mentions of a heading token caused four misfired measurements in one session — "the density of decoys is highest in exactly the files most likely to be measured." The mechanical conformance check reported two false FAILs because it landed 251 lines early on a prose mention. The general form: a document about a convention quotes that convention, creating decoys. The fix is a documentary rule for probe anchoring methodology. This is governance_rule because it proposes a verification authoring rule about how structural searches are conducted, not a tooling change.
- **Confidence:** high

### 2026-08-05: Copying a guard from a parent plan is not the same as copying its history [tag: planner-discipline]


- **Suggested action:** Extend DRAFTING_CYCLE.md §2.6 clone-drift rules to add a second question: for every inherited guard, check whether the parent amended it after first writing it. Inherit by diffing the parent's final text, not by rewriting from the guard's purpose.
- **Reasoning:** The entry measures clone-drift at three depths in one plan — "guards absent, guards present but unqualified, and — separately — corrections reaching some of their sites but not all." A restored guard imported the parent's original unscoped form, which would have blocked three questions that needed nothing from the missing input. The parent had scoped that guard mid-cycle, and the clone inherited the pre-fold version. The proposed fix — diff the parent's final text and check the log for folds — is a documentary rule change extending §2.6's existing clone-discipline rules.
- **Confidence:** high

### 2026-08-04: A falling finding-count measures where the reader was sent — proven by removing the aim [tag: planner-discipline]


- **Suggested action:** SHAPE-DECISION CLUSTER (A): routes into the reserved CEO decision on drafting-cycle shape per baton item 2. The entry provides measured evidence that a falling finding-count is an artifact of aim: the count ROSE when the aim came off, proving the untargeted-confirming-walk requirement.
- **Reasoning:** The entry directly measures the finding-count/aim relationship — "same artifact, same reader, same day — the only variable was whether the walk was aimed" — and proves that a falling count was an artifact of targeting. Walk 5 aimed at three untouched regions found 3 findings with twelve unreached cells; walk 6 untargeted found 8 findings with zero unreached cells. The doctrine already states the coverage-map signal; this is the first direct measurement of the inverse. Core evidence for the drafting-cycle shape decision; no Family line present, placement derived from body.
- **Confidence:** high

### 2026-08-04: Ten consecutive ACID passes each found a defect created by the culmination immediately before it [tag: planner-discipline]


- **Suggested action:** SHAPE-DECISION CLUSTER (A): routes into the reserved CEO decision on drafting-cycle shape per baton item 2. The entry establishes at n=10 that ACID finding a culmination-introduced defect is the measured behaviour, and that class drift (logic to record) is the judged-stop signal.
- **Reasoning:** The entry measures at ten consecutive passes that every ACID pass found a defect created by the culmination immediately before it — "ten ACID passes, ten culmination-introduced defects" — and identifies that the failure class drifted from logic defects to record defects. Prior sessions recorded this at 5-of-5 and 6-of-6; at ten it is no longer a tendency but the measured behaviour. The entry proposes recognising class drift as the judged-stop signal rather than waiting for a dry walk that will not come. Core shape-decision evidence; no Family line present, placement derived from body.
- **Confidence:** high

### 2026-08-04: A retraction that names its own scope can still be incomplete, and a consumer sweep that probes the wording misses the claim [tag: planner-discipline]


- **Suggested action:** Add a claim-level probe rule to DRAFTING_CYCLE.md §2.7: a consumer sweep must probe for the CLAIM in any phrasing by enumerating sections that could plausibly hold it, rather than grepping the edited string.
- **Reasoning:** The entry measures that a retraction claimed it had corrected a claim in three places and had reached one, then a consumer sweep missed a fifth site holding the same claim as a paraphrase — "a paraphrase the sweep's probe could not match because the probe was the literal string from the sentence that had been edited." Two distinct failures compose: a retraction that specifies a count gives false confidence, and a sweep built from one's own wording confirms only what was edited. The proposed fix is a documentary rule change to the governance file's sweep rules.
- **Confidence:** high

### 2026-08-04: A guard can be safe by accident — executing the real check distinguishes design from luck [tag: verification]


- **Suggested action:** Add a rule to DRAFTING_CYCLE.md §2.7 requiring that when a guard's safety depends on a claim about text, the guard's actual matcher must be executed rather than reasoned about, and the report must state which branch fired and what it captured.
- **Reasoning:** The entry measures that a guard was safe only by the accident of an incidental backtick — "the only reason the inline matcher fails is that backtick. Remove it, or put a space there, and the gate would capture the question's prose as the declared deposit list." Reasoning said it was probably fine; executing the real regexes revealed the safety was accidental. The fix is a documentary rule requiring execution of the gate's real matcher and reporting which branch fired. This is governance_rule because it proposes a verification authoring rule for plan drafting, not a tooling change.
- **Confidence:** high

### 2026-08-04: A measurement must be taken by the method the plan mandates, or it is a prediction [tag: verification]


- **Suggested action:** Extend Checklist #29 in PLANNER_TEMPLATE.md to require that every number stated in a plan is produced by the plan's own mandated method, and that disciplines reapplied at many call sites are placed inside the instrument rather than left for the caller to remember.
- **Reasoning:** The entry identifies that a measurement taken without the mandated strip method overstated by half — "overstating by half (six files where the correct answer is four)" — and the wrong count was taken by a fresh cold reader who had just read the strip rule. The fix proposes that any number not produced by the mandated method is a prediction and must carry a verify-clause, and that reusable disciplines belong inside the instrument. This is governance_rule because it extends an existing plan-authoring checklist, not a tooling change.
- **Confidence:** high

### 2026-08-03: The register append succeeded, recorded a pointer, and lost every item — a channel can fail a third distinct way [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md (Forward Register emission rules): a mandated block must be verified in the SECTION the parser reads, not merely present in the deposit. A cross-reference satisfies a text-capturing parser as well as content does. The parser defect half (lu_body scoping in parser.py) is bellows-owned — Rule 46 question for Gate 1. Cluster (B) with entries 220/221/228.
- **Reasoning:** Entry documents the Forward Register losing all items because the substantive block was written outside the Ledger Updates section. As the entry states: "a mandated block must be verified in the SECTION THE PARSER READS, not merely present in the deposit — correctly formatted and correctly located are different claims." This is the channel's third distinct failure mode. The fix is a documentary authoring rule in PLANNER_TEMPLATE.md about verifying block location against the parser's input scope. Family line extends the delivery-code lesson from non-arrival to arrival of the wrong thing.
- **Confidence:** high

### 2026-08-03: A ledger constraint that ENUMERATES decays as oscillation, not staleness [tag: drafting-cycle]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md section 2.8: an enumerating constraint decays as oscillation (second reversal is the tell); restate as the principle the list approximates rather than improving the enumeration.
- **Reasoning:** Entry documents a Conflict-Ledger constraint that oscillated through three formulations — too narrow, too broad, too narrow again — each individually well-reasoned. The entry states: "the tell is the SECOND reversal, not the first — a constraint corrected in one direction and then the other is enumerating, not converging" and directs: "restate it as the principle the list was approximating." The fix is a documentary rule governing how constraints are authored and revised, fitting governance_rule. Family line: the oscillation-shaped counterpart to the roster-decay class.
- **Confidence:** high

### 2026-08-03: A rule authored in the VERIFIER is a rule the producer never reads [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md (near Rule 54/58): for every mandated requirement, confirm the text is in the step that must comply; a rule enforced by a QA row must be stated where the artifact is produced; sweep both directions (producer-missing and consumer-missing).
- **Reasoning:** Entry documents three instances in one drafting cycle where a requirement was written into the checking step, not the producing step. As the entry states: "for every mandated requirement, name the step that must COMPLY and confirm the text is in that step's prompt — presence anywhere in the plan is not compliance-reachable." The class was never swept across five walks and existing doctrine did not catch it because each requirement had a structural home — in the wrong step. Family line: the placement-side complement to the structural-home lesson.
- **Confidence:** high

### 2026-08-03: A plan's claim about what a gate enforces is a claim to verify, not to inherit [tag: bellows-integration]


- **Suggested action:** Extend PLANNER_TEMPLATE.md Rule 52: any sentence asserting what a gate matches, enforces, or rejects is a claim to re-run against the gate's source, not to inherit. Record calibration ranges with sample sizes beside thresholds.
- **Reasoning:** Entry documents a banner-string claim about gates.py that survived five warm walks, five ACID passes, and a plan_lint run because every pass read the assertion rather than running the gate. The entry states: "any sentence asserting what a gate matches, enforces or rejects is a claim to RE-RUN against the gate's source — inheriting it from a parent plan reproduces the parent's errors with the parent's confidence." A second instance: a calibration range from n=6 met a 16-item batch with thinner margins. Family line extends the delivery-code lesson to documented behaviour.
- **Confidence:** high

### 2026-08-03: "The newest same-class plan" is a measurement, not something you recall [tag: planner-discipline]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md section 2.6: before claiming any plan is the newest of its class, sort the shipped set by ship date and name the winner with its date, as a measured line in the plan.
- **Reasoning:** Entry documents a clone-lineage error where a plan asserted its parent was both the clone origin and the newest same-class plan, but a sibling had shipped one day later. The entry states: "before claiming any plan is the newest of its class, SORT the shipped set by ship date and name the winner with its date, as a measured line in the plan." The cost: an ACID pass spent a finding rediscovering a hardening the newer sibling had already shipped and marked as executed. Family line: the prior step to the clone-against-the-newest rule.
- **Confidence:** high

### 2026-08-03: A self-check that reads the DEPOSIT cannot verify a channel that parses the TRANSCRIPT [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md (channel-verification area): before authoring verification for a delivery channel, read the delivering code to find WHICH ARTIFACT it consumes and state that artifact in the check. Parser half (transcript vs deposit source) is bellows-owned — Rule 46 question for Gate 1. Cluster (B).
- **Reasoning:** Entry documents a channel that failed in four distinct ways across three sessions because every check reads the deposited file while the daemon reads the transcript. The entry states: "before authoring any verification for a delivery channel, read the delivering code to find WHICH ARTIFACT it consumes, and state that artifact in the check" and "A check aimed at a different artifact is a proxy no matter how exactly it reproduces the consumer's logic." The consequence is a green check over a total loss. Family line extends the delivery-code lesson.
- **Confidence:** high

### 2026-08-03: items-in equals items-out, and the item still arrives truncated [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md (Forward Register block format): constrain item shape so no item wraps onto a second physical line; compare content not just counts downstream of a splitter. Cluster (B) with entries 215/220/228.
- **Reasoning:** Entry documents a block where five items were written and five recovered with exit zero, yet items arrived truncated because the splitter keeps only lines matching its bullet pattern and drops continuation lines. The entry directs: "a cardinality assertion is blind to loss WITHIN an item; when items carry substance, compare content, not counts" and "Constrain the shape that makes the loss possible — here, that no item may wrap onto a second physical line." Classified as governance_rule because the fix is a documentary authoring rule for how plan blocks are constrained and verified — a rule change to PLANNER_TEMPLATE.md, not a tooling change. Family line: the intra-item form of the count-is-not-a-value-guard lesson.
- **Confidence:** high

### 2026-08-03: Machinery added to close a durability gap clobbered the artifact it protected, on the exact path it was built for [tag: planner-discipline]


- **Suggested action:** Extend PLANNER_TEMPLATE.md Rule 56/62 resume rules: for any new durability artifact, walk the RESUME path before the crash path — a write correct on a fresh run is a clobber on a re-run unless explicitly non-destructive. Clusters with entry 261.
- **Reasoning:** Entry documents durability machinery that clobbers its own artifact on the resume path — the dispatcher re-runs a dead step from the top, so the resumed step rewrites the before-image with post-mutation values. The entry states: "for any new durability artifact, walk the RESUME path before the crash path — a write that is correct on a fresh run is a clobber on a re-run unless it is explicitly non-destructive." The fix is not a patch but a posture: if the file exists, cite it as authoritative. Family line: the durability-side complement to the resume-machinery rules.
- **Confidence:** high

### 2026-08-03: Renaming an excuse launders it past the rule that already forbids it [tag: planner-discipline]


- **Suggested action:** Extend DRAFTING_CYCLE.md section 2.7 INHERITED-marker clause: any marker whose practical meaning is 'I did not run this' gets the cost test regardless of its spelling. Partial overlap — the cost-test clause exists; the any-spelling scope does not.
- **Reasoning:** Entry documents a clone that re-imported an identical excuse under a new marker name, laundering it past the governing rule. The entry states: "any marker whose practical meaning is I did not run this is the same marker regardless of its spelling — apply the cost test to all of them, not to the one the rule names." A retraction in a parent failed to inoculate its clone — the clone quoted the rule approvingly and then violated it. Family line: the naming-side evasion of the reason-for-not-running lesson.
- **Confidence:** high

### 2026-08-03: Six adversarial passes found the content defects; the one-command conformance check would have found forty others, and it never ran [tag: planner-discipline]


- **Suggested action:** Extend DRAFTING_CYCLE.md section 5: run the linter and by-scope rules walk BEFORE the adversarial passes (when shape stabilises), not after; record the linter's exit code in the plan. Cluster (E) with entry 237 — one scheduling edit, not two.
- **Reasoning:** Entry documents a plan that went through five lenses, a separate ACID pass, and a five-reader cold panel while the one-command conformance check never ran. The entry states: "run the linter and the by-scope rules walk BEFORE the expensive adversarial passes, not after — they find disjoint classes and one of them costs a command" and "Adversarial review is aimed at whether the plan is RIGHT; conformance is aimed at whether it is ADMISSIBLE." Nearly every cold panel finding was detectable by the linter. Family line: an ordering claim about the existing mechanical-conformance section.
- **Confidence:** high

### 2026-08-03: A walk aimed at the last fold is not a walk — coverage is the convergence signal, not a falling count [tag: drafting-cycle]


- **Suggested action:** SHAPE-DECISION CLUSTER (A): routes into the reserved CEO decision on drafting-cycle shape (baton item 2). Entry provides evidence that a walk aimed at the last fold is not a walk — coverage is the convergence signal, not a falling count. The correction also costs less: a complete five-lens walk covered twenty-seven sections for roughly the token budget of one targeted round.
- **Reasoning:** Entry documents nine adversarial rounds and roughly 150 findings, with a CRITICAL defect surviving all nine rounds in the one region no reader was pointed at. The entry states: "a CRITICAL defect survived all nine rounds in the one substantial region no reader was ever pointed at, and was found only when a complete pass finally covered the whole artifact." The severity counts (8, 5, 2, 4, 3) measured aim, not convergence. Family line: the operational form of the rotation-not-severity lesson.
- **Confidence:** high

### 2026-08-03: Delete the check, not its label — and verify by the check's absence [tag: planner-discipline]


- **Suggested action:** Extend DRAFTING_CYCLE.md section 2.7 subtractive-trim bullet: verify a deletion by the absence of the construct's CONTENT (assertion text, query), never by the absence of its label; excise the whole span of a multi-line construct.
- **Reasoning:** Entry documents a structural cut where a check was deleted by removing its label line while the body — a fenced query and three assertions — survived six lines below. The entry states: "Verify a deletion by the absence of what the thing DID, never by the absence of what it was called" and "removing a multi-line construct by deleting its label line is not a deletion; excise the whole span." The post-condition asked only whether the label string was gone, and it was. Family line: the deletion-side form of the count-versus-composition lesson.
- **Confidence:** high

### 2026-08-03: A structural cut is an edit, and it has its own defect class [tag: planner-discipline]


- **Suggested action:** Add rule to DRAFTING_CYCLE.md section 2.7/2.8: budget a cut as an edit — sweep for references TO removed items and for captures losing their only reader; do not preserve numbering to protect references to removed items.
- **Reasoning:** Entry documents a structural cut that produced six dangling cross-references, two orphaned captures, and a stale justification clause. The entry states: "budget a cut as an edit that will generate findings, not as a subtraction that reduces them" and "After removing anything, sweep for references TO it and for captures that just lost their only reader — those are the two failure modes, and both are mechanical." The renumbering rationale was measurably false: every reference that broke was to a deleted row. Family line extends the repeated-folds-means-delete lesson.
- **Confidence:** high

### 2026-08-03: In a block parsed subsection by subsection, the LAST subsection is the exposed one [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md (Forward Register area): when fixing a parser terminator, enumerate every construct terminated the same way — the last subsection in an ordered set is structurally exposed; terminate the whole block. Parser defect half bellows-owned — Rule 46 question for Gate 1. Cluster (B).
- **Reasoning:** Entry documents a parser terminator fix applied to one subsection while the mechanism is subsection-generic — the last subsection is exposed because it terminates only by blank line or end-of-stream. The entry states: "when a fix turns on a parser's terminator, enumerate every construct that parser terminates the same way — the fix belongs to the class, not to the instance" and "In an ordered set of parsed subsections, the last one is structurally the exposed one." Fourth instance of the fold-lands-where-noticed class. Family line: same channel, same class.
- **Confidence:** high

### 2026-08-03: A pipe masks the exit code, and it caught four independent readers in one session [tag: verification]


- **Suggested action:** Extend DRAFTING_CYCLE.md section 2.7 command-output rule: never pipe a command whose exit code carries meaning; capture output to a variable or file and report the code separately. Partial overlap — never-pipe is implied in existing text, not stated.
- **Reasoning:** Entry documents four independent readers in one session falling prey to the pipe-masking-exit-code error — the shell reports the exit status of the last command in a pipeline, so a formatter's success is read as the checker's. The entry states: "never pipe a command whose exit code carries meaning — capture the output to a variable or a file, then inspect and report the code separately." Classified as governance_rule because the fix is an explicit documentary rule change to the command-output section of DRAFTING_CYCLE.md, not a tooling change or procedural step. Family line: the pipeline form of the exit-code lesson.
- **Confidence:** high

### 2026-08-03: A repair can break what it repaired, at the same severity, in the same region [tag: planner-discipline]


- **Suggested action:** SHAPE-DECISION CLUSTER (A): routes into the reserved CEO decision on drafting-cycle shape (baton item 2). Entry provides evidence that self-inflicted repair proportion is a convergence-negative signal — when findings are dominated by the previous round's own repairs, the process is at its noise floor.
- **Reasoning:** Entry documents six review phases where the self-inflicted proportion rose from 6-of-9 to 8-of-8 to 2-of-2 high-severity. The entry states: "When a review round's findings are dominated by the previous round's repairs, that is a convergence signal in the negative — the process is at its noise floor, not approaching zero" and "A falling count with a rising self-inflicted proportion is not progress." No Family line — placement derived from body: the entry measures the convergence failure mode, which is core evidence for the drafting-cycle shape decision.
- **Confidence:** high

### 2026-08-03: Two gates over the same list pull in opposite directions — required versus tolerated [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md (Rule 26/Deposits rules): a declared-outputs block lists only what the step produces on EVERY path; name conditional artifacts in prose. Establish each consuming gate's polarity (required vs tolerated) separately.
- **Reasoning:** Entry documents two gates reading the same declared-outputs list with opposite polarity — the scope check tolerates extras (unnamed changes fail) while the deposit check requires every name (a conditional file guarantees failure). The entry states: "A declared-outputs block lists only what the step produces on EVERY path. Name conditional artifacts in prose, where the tolerant gate can still see them" and "When two checks read the same declaration, establish each one's polarity separately." Classified as governance_rule because the fix is a documentary rule change to PLANNER_TEMPLATE.md about how the Deposits block interacts with its consuming gates. No Family line — derived from body.
- **Confidence:** high

### 2026-08-03: A pin whose extraction method is unstated is unreproducible, and it fails closed on the honest path [tag: verification]


- **Suggested action:** Extend Rule 61 in PLANNER_TEMPLATE.md to require that every verification pin ships the exact extraction command beside the pinned value, and that the method is verified portable across tool builds.
- **Reasoning:** The entry identifies that a hash pin whose extraction method is unstated fails closed on honest work: "A verifier extracting any other way computes a different hash and reports a mismatch on work that is entirely correct." Two pins in one artifact failed the same way, and a row-count baseline varied by four depending on unstated counting rules. The fix is a documentary authoring rule — ship the extraction command beside the value — extending Rule 61's pin requirements. This is a governance_rule because the proposed change is a plan-authoring rule constraining how verification pins are documented, not a tooling change or procedural step.
- **Confidence:** high

### 2026-08-03: The sweep fails at maximum context — the fix and the missed sibling get written in the same sitting [tag: planner-discipline]


- **Suggested action:** Extend DRAFTING_CYCLE.md §2.7 fold-sweep section to require enumerating every applicable site BEFORE applying a fix anywhere, with heightened sweep weight toward material written in the same session as the fix.
- **Reasoning:** The entry measures that sweeping for related sites fails precisely when the author has just formulated the rule — "The author who has just formulated a rule is the one least likely to re-scan for other instances, because formulating it feels like discharging it." Family line names it as the fold-sweep discipline measured failing under the conditions most favourable to it. Two high-severity findings of the same shape were each correctly fixed at one site while the sibling site was untouched, with the second pin defect added in the same edit session as the fix for the first. The proposed rule change — enumerate sites before applying — is a documentary edit to a governance file.
- **Confidence:** high

### 2026-08-03: An independent referent sourced from the actor's own record is not independent [tag: verification]


- **Suggested action:** Add a new rule near Rule 55 in PLANNER_TEMPLATE.md requiring that every new referent in a verification be audited for true independence: the referent must exist before the actor acts and outside its control.
- **Reasoning:** The entry identifies that independent referents sourced from the actor's own record reproduce the circularity they exist to break — "Two of the three were circular in exactly the same way — one compared a diff against the deltas the actor recorded, the other compared a content hash against a baseline the actor supplied." The fix reproduced the defect it existed to remove, twice, in the same edit. The proposed rule — audit every new referent against the independence test — is a documentary rule change for the governance template. This is governance_rule because the entry proposes a verifiable authoring principle for plan verification, not a tooling fix or procedural step.
- **Confidence:** high

### 2026-08-03: A backup must sit adjacent to the write it inverts, or it is not an inverse [tag: planner-discipline]


- **Suggested action:** Extend the Rule 56 area in PLANNER_TEMPLATE.md to require that a backup and the write it inverts are adjacent with nothing between them that can touch the same store, and that each backup states which single write it inverts.
- **Reasoning:** The entry measures that a backup separated from its protected write by twenty-two file edits and a commit spanned a window where another process was legitimately writing the same store — "Restoring that snapshot would have rolled back the other process's real work. The backup was correct at snapshot time and wrong at restore time." The adjacency requirement also strengthens an unrelated guard: an unexplained backup becomes evidence of an attempted mutation. The proposed rule change is a documentary edit to the governance template's recovery rules.
- **Confidence:** high

### 2026-08-03: A zero-difference result needs an inverse control before it means anything [tag: verification]


- **Suggested action:** Extend Rule 55 in PLANNER_TEMPLATE.md to require that any check whose passing result is an absence includes a positive control on the same instrument in the same run, demonstrating the instrument can detect a difference.
- **Reasoning:** The entry identifies that a zero-difference blast-radius check is indistinguishable from a broken comparison — "a bad query, a mismatched sort, a wrong file, an empty read" all produce the same result. The check became evidence only when run against the target range to show it could detect a difference. The proposed rule — require a positive control for any absence-result check — generalises the positive-control principle as a documentary edit to the governance template. This is governance_rule because the entry proposes a verification authoring rule, not a tooling change.
- **Confidence:** high

### 2026-08-03: The conformance pass catches what adversarial review structurally cannot [tag: planner-discipline]


- **Suggested action:** Edit DRAFTING_CYCLE.md §5 to schedule the mechanical conformance pass when the artifact's shape stabilises (before the adversarial passes), not at deposit, and to record the linter's exit code. Cluster (E) with entry 224 — one §5 scheduling edit, not two.
- **Reasoning:** The entry measures that six adversarial review phases and roughly a hundred findings provided zero coverage of mechanical conformance — "every step referred to depositing outputs and not one had the declaration block the tooling parses." The conformance pass immediately found three hard failures that no lens could have caught because the question is structurally different: "Does this conform to a convention the tooling requires" is not a correctness, safety, or consistency question. The proposed fix is a scheduling edit — run when shape stabilises — which is a documentary rule change to the governance file.
- **Confidence:** high
