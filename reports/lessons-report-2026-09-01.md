# Lessons Report — 2026-09-01


## Summary


| Category | Count |
|---|---|
| governance_rule | 23 |
| instrumentation | 2 |
| structural | 3 |

**Total proposals:** 28


## Governance Rule


### 2026-09-01: EXECUTING A PLAN'S COMMANDS IS NOT EXECUTING THE GATES THAT JUDGE ITS STEPS — a missing deposit is invisible to every command and visible only to `gates.check()` [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: after executing a plan's step commands, run gates.check() to verify deposit existence; a missing deposit is invisible to every command and visible only to the gate.
- **Reasoning:** [AUTHOR-CONFLICT] 'A doc-only plan ran ten drafting-cycle walks, a non-author cold Gate-1 read, and two full EXECUTION passes... The plan then dispatched, and step 2 failed its gate on the first attempt: qa_test_result: no .txt evidence deposit found — cannot certify test result; pausing.' The gate '_gate_qa_test_result fires on ANY QA step and has no exemption for a plan declaring no test scope.' Every command passed; 'a missing deposit is invisible to every command and visible only to gates.check().' Rule: executing commands is not the same as satisfying gates; gates.check() must be run explicitly.
- **Confidence:** high

### 2026-09-01: A POST-CONDITION BUILT ON A HAND-ENUMERATED LIST IS ONLY AS COMPLETE AS ITS AUTHOR — and the author's own mutation test cannot reach what the list omits [tag: verification] [tag: drafting-cycle]


- **Suggested action:** Add rule: post-conditions that verify structural completeness must use mechanical enumeration (code or tooling) rather than hand-enumerated lists authored by the same person who wrote the structure.
- **Reasoning:** [AUTHOR-CONFLICT] 'A restructuring edit was guarded by a post-condition that re-derived every cross-reference's position from the post-edit text... The check was real, it ran, and it was mutation-tested... It was still unsound, because the constraint set it checked against was typed by hand. A mechanical enumeration found ten relation parentheticals where the author had listed eight.' The two missed were 'a companion clause distinguished only by an em-dash continuation instead of the word above, and a rule naming its parent by section rather than direction.' Rule: structural post-conditions must use mechanical enumeration; hand-enumerated lists are bounded by the author's model.
- **Confidence:** high

### 2026-09-01: A LOSSLESS REORDER PRESERVES TRUTH AND DESTROYS PROXIMITY — "the clause above" stays true at distance 23 [tag: drafting-cycle]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when restructuring a document containing directional cross-references ("the clause above", "see below"), verify per-pair referential distance post-reorder, not only the truth of the invariant.
- **Reasoning:** [AUTHOR-CONFLICT] 'Reordering a document to group related rules moved 52 items under subject headings without altering one byte of any item. Every cross-reference of the form the clause above remained TRUE — the referent still preceded the referrer, and a post-condition proved it. Truth was the wrong invariant. One pair went from adjacent (distance 1) to 23 items and a section boundary apart: still accurate, and a reader now has to hunt for what used to be the previous line.' Twelve reference pairs measured: total referential distance 259 → 82, but one pair regressed from 1 to 23. Rule: verify per-pair distance, not only truth.
- **Confidence:** high

### 2026-09-01: A WORK POOL DEFINED BY A TAGGING CONVENTION MEASURES THE CONVENTION, NOT THE SUBJECT [tag: process-integrity] [tag: verification]


- **Suggested action:** Add rule: when constructing a work pool from a tagging convention, first verify the tagging convention is current by spot-checking recent entries; complement tag-based queries with content-based verification against untagged entries.
- **Reasoning:** [AUTHOR-CONFLICT] 'A census of every lesson about X was built by selecting entries carrying X's tag. The pool came back 24 entries... The tagging convention had lapsed five weeks earlier. Thirty-two later entries carried no tag at all... ten were unambiguously about X, one of them a sharper statement of a rule the census had just shipped in weaker form.' The compounding failure: 'the same pass edited those untagged entries — backfilling their missing status markers — and never re-ran the pool against them.' Rule: tag-based pools measure the convention, not the subject; verify the convention's currency before trusting the pool.
- **Confidence:** high

### 2026-08-31: A VARIABLE YOUR HARNESS INJECTS IS NOT PRESENT FOR THE DAEMON THE HARNESS SPAWNS — test the dispatch environment, not the shell you are typing in [tag: verification]


- **Suggested action:** Add rule: before shipping a plan that uses an environment variable, verify the variable is present in the DISPATCH environment (daemon process) by inspecting the daemon's process environment, not the interactive shell.
- **Reasoning:** 'A plan's DEV step hardcoded an absolute path to a builder script. The fix looked obvious: resolve it from $ELUVIAN_WRAP_ROOT... with ${VAR:?message} so an unset variable fails loudly rather than silently. Measured before shipping it, and the fix was strictly worse than the defect it replaced.' The variable was set in the interactive shell and declared in the harness settings, so it reaches sessions the harness starts, but 'ps eww <daemon-pid> | tr " " "\n" | grep -c "^ELUVIAN_WRAP_ROOT=" → 0.' Rule: test env vars in the dispatch environment, not the shell.
- **Confidence:** high

### 2026-08-31: ENABLING A WATCHER OVER A DIRECTORY RETROACTIVELY PROMOTES EVERYTHING ALREADY IN IT TO AN INPUT — inventory the directory before arming, not after [tag: process-integrity]


- **Suggested action:** Add rule: before adding a directory to a daemon's watched_projects, inventory its existing contents for `executable-`, `diagnostic-`, or `qa-` prefixed files that would immediately be claimed, and resolve each before arming.
- **Reasoning:** 'Adding a project's knowledge/decisions/ to a daemon's watched_projects is a one-line config change that reads as start watching for new work. It is not: the watcher evaluates what is already there.' Pre-flight check found 'reporting-phase2-cycle-query-blueprint-2026-07-01.md sat there with a bare filename' and 'plan_lint parses its header as a PASS, so a shape check would pass too.' (Note: entry 428 corrects that bare filenames are not claimable, but the general rule — inventory before arming — remains sound for genuinely-prefixed files.) Rule: inventory before enabling a watcher.
- **Confidence:** high

### 2026-08-31: ⛔ CORRECTS THE ENTRY ABOVE — `is_runnable_plan` IS AN ALLOWLIST, AND THE LESSON THAT PRECEDED THIS ONE RE-IMPLEMENTED ITS RULE INVERTED [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: claims about code behavior derived from source reading must be labeled as hypotheses and verified by running the code. 'Verified from source' is not a verification result.
- **Reasoning:** 'The entry immediately above... states that a bare filename is exactly the shape the daemon treats as claimable... Both are wrong, and the entry was written by me, hours earlier, from a mental model I never checked against the code.' The actual code: 'return bool(re.match(r"^(parallel-\d+-)?(executable|diagnostic|qa)-.*\.md$", filename))' — it is an allowlist. The entry prescribes: 'Run against the real function before writing it into a lesson' and 'an executable question answered by reading will plausibly be wrong.' This reinforces the rule from entry 418 and adds a specific guard against publishing unexecuted behavioral claims.
- **Confidence:** high

### 2026-08-31: A NORMATIVE DOCUMENT'S WORKED EXAMPLE IS NOT A KNOWN-GOOD ARTIFACT WHEN A MACHINE COMPARATOR IS THE AUTHORITY — measure the shipped corpus, not the doc [tag: mechanization]


- **Suggested action:** Add rule: normative document worked examples that feed machine comparators must be verified against the shipped corpus and updated when the emitter's spelling changes; file doc defects rather than quietly conforming to the corpus.
- **Reasoning:** 'DRAFTING_CYCLE.md:262 gives the manifest's validation line, verbatim, as validation: cycle_check=bar-met, plan_lint=0-fail. depositor.py:518 compares that declared value to cycle_check's actual output with a case-sensitive exact string compare, and cycle_check emits BAR_MET.' A plan copying the doc's example 'is held on deposit — measured live: hold_reason: validation_mismatch:cycle_check expected=bar-met got=BAR_MET.' The corpus settles it: '47/47 shipped plans declare cycle_check=BAR_MET; 45 declare plan_lint=0_FAIL. The document every Planner is told to copy from is the single outlier.' Rule: worked examples feeding comparators are code and must be kept in sync.
- **Confidence:** medium

### 2026-08-30: WHEN ONE DEFECT CLASS FIRES ON CONSECUTIVE REVIEW PASSES, THE REVIEW HAS BECOME SAMPLING — STOP WALKING AND ENUMERATE THE CLASS AGAINST ITS PRODUCERS [tag: process-integrity]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when the same defect class fires on two or more consecutive review passes, stop walking and enumerate ALL instances of that class against the plan's full text, rather than continuing sampling walks.
- **Reasoning:** 'Walks 10, 11, 12 and 13 of one drafting cycle each returned EXACTLY ONE instruction-class finding, and every one was the same class: a value correct when written, whose producer later moved, with the citing site left behind.' The entry: 'Walk 12 predicted this and did not stop.' The prescribed fix: 'when one defect class fires on consecutive review passes, the review has BECOME SAMPLING — STOP WALKING AND ENUMERATE THE CLASS AGAINST ITS PRODUCERS.' This is a rule change to the drafting cycle.
- **Confidence:** high

### 2026-08-27: A test written by the author of the code inherits the author's model — move the ORACLE outside it, or the suite can only confirm the bug [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: acceptance tests for a fix must include at least one test authored or reviewed by a non-author to provide an oracle outside the author's mental model.
- **Reasoning:** Exec-572 'shipped a guard whose premise was false... It passed 7/7 gates and eight dedicated tests. The tests were worthless for the same reason the code was wrong: I wrote both from one model, so every assertion re-expressed the misunderstanding.' The entry states: 'The single test that would have caught it — arm over an UNRESOLVED request and assert a normal pause — was not merely missing, it was unthinkable inside the model that produced the code.' The rule implied: a non-author oracle is required for acceptance tests on code fixes.
- **Confidence:** high

### 2026-08-27: A DORMANT CLASSIFICATION BECOMES POLICY the moment a new mechanism starts reading it — audit every latent quirk before wiring a gate to an existing label [tag: multi-artifact-coherence]


- **Suggested action:** Add rule: before wiring a new gate or mechanism to an existing field or classification label, audit every consumer of that field to understand how the new gate changes behavior for historically-classified items.
- **Reasoning:** A depositor's class assigner 'had carried a small heuristic for months' that was 'harmless, because the only consumer was a hold that a human released in one command.' Then 'a cross-machine claim lock shipped, and it read class as an ELIGIBILITY GATE. Nothing about the heuristic changed. Overnight it meant that any plan editing a project's own root-level governance document was undispatchable on the machine that owns that project.' The general shape: 'a classification that exists only for human consumption becomes a machine gate without intent or audit.' The fix is a documentary rule about auditing field consumers before wiring gates.
- **Confidence:** medium

### 2026-08-27: A STOP ARM must key on the claim that would make the work worthless — not on the observation that motivated it [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a STOP ARM must be keyed on the claim that would make the work worthless (a provable premise), not on an observation whose outcome is statistically variable.
- **Reasoning:** A plan 'told its agent: if the flakiness does not reproduce on your run, STOP. The agent's run did not reproduce it, so it stopped — correctly, and a correct fix was halted for a full cycle.' The condition was statistically variable (three runs produced three different outcomes). But 'the premise was never actually in doubt. It was provable from a FILE FORMAT: a .pyc header stores the source mtime as a 32-bit seconds field, so sub-second resolution is discarded.' The entry prescribes keying STOP ARMs on provable claims, not variable observations.
- **Confidence:** high

### 2026-08-27: BEFORE OPTIMIZING A SYSTEM'S LIFECYCLE, CONFIRM WHAT THE SYSTEM IS FOR — and measure the mode you would remove on the machine where it actually happens [tag: process-integrity]


- **Suggested action:** Add rule: before proposing a lifecycle-mode change to a running system, confirm the system's purpose in one sentence and measure the mode you would remove on the machine where it actually runs.
- **Reasoning:** A proposal to convert an always-on daemon to on-demand 'was refuted at walk 1 by asking a single question: what is the engine FOR? Conflict serializability.' An engine that lives for one unit of work 'must either keep watching for the next plan, which is being always-on, or refuse it.' The entry prescribes: 'Measure usage where the usage happens. If the evidence lives on a machine you cannot read, the finding is unmeasured, never unused — and say which in the record.' A rule for plan authoring: name the system's purpose before proposing lifecycle changes.
- **Confidence:** medium

### 2026-08-27: ROUTE A QUESTION BY WHETHER A COMMAND CAN ANSWER IT — reading a consumer's source is a hypothesis, not a verification [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a question about code behavior is executable, run the code to answer it. Mark 'verified from source' only as a hypothesis, never as a verification result.
- **Reasoning:** 'Two defects survived all nine walks and were then caught by machinery in under a second each, and both share a property worth naming: they were executable questions that I answered by reading.' One walk 'recorded, as DRY, verified from source, that the depositor would class the plan app-feature. It classes it shop-infra.' The entry states: 'reading a consumer's source is a hypothesis, not a verification.' The rule: route executable questions to execution (run the code), not to source reading.
- **Confidence:** high

### 2026-08-27: A SHIPPED ARTIFACT IS A POOR TEACHER ABOUT ITS OWN MISTAKES — diff a clone against the project's rules and the parent's WALK REGISTER, not only against the parent [tag: process-integrity]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when cloning a plan, diff the clone against the project's own CLAUDE.md/rules AND the parent's walk register, not only against the parent plan text.
- **Reasoning:** 'Two plans shipped hours apart on the same file, the second cloned from the first with a deliberate clone-diff at walk 0. That diff caught two of the parent's operational defects and inherited two more, and the two it missed failed in the same way: the parent's shipped text contained no evidence they existed.' One miss: '[580]'s DEV step chained five git commands with &&; the project's own .claude/CLAUDE.md forbids it outright — a rule written because chaining had caused repeated hangs and corrupted index state.' The rule: clone-diff must include the project's own rules and the parent's walk register.
- **Confidence:** high

### 2026-08-27: PROVING A GUARD COVERS A RULE REQUIRES VIOLATING THE RULE — running the mechanism in its correct state proves NON-REGRESSION, not coverage [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: verification of a subtractive trim (MUST-PRESERVE reduction) requires writing one violation test per ledger row and confirming each test fires, not only re-running mechanisms in their correct state.
- **Reasoning:** A MUST-PRESERVE trim 'carried a §2.7 subtractive-trim verification: re-run every mechanism, confirm green. It came back green... and the trim shipped.' But 'a cold seat then wrote ONE violation test per ledger row. Four of ten rows were FALSE. Three clauses ended with no carrier at all, the worst being the arm runs inside the advisory-lock transaction — the isolation invariant the whole cross-machine design rested on.' The rule: 'proving a guard covers a rule REQUIRES VIOLATING THE RULE — running the mechanism in its correct state proves NON-REGRESSION, not coverage.'
- **Confidence:** high

### 2026-08-27: A DOCTRINE EDIT RIDING A CODE PLAN IMPOSES THE DOCTRINE'S TIER ON THE CODE — split on TIER, which is mechanical; not on SIZE, which the data does not support [tag: process-integrity]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a plan contains items with different tier triggers, split the plan on TIER (the mechanical boundary), not on size. A doctrine-tier item forces its tier on the entire plan.
- **Reasoning:** 'A plan carried a schema migration, a config mode, a claim arm, and a GOVERNANCE.md amendment. The amendment was its ONLY T-6 trigger, and T-6 mandates a cold panel... So one doctrine edit imposed a mandatory cold panel on a code change that never needed one.' Splitting the amendment into its own plan 'recomputed the code half to T1 — full five-lens walk, no panel — in about ten minutes.' The rule: 'split on TIER, which is mechanical; not on SIZE, which the data does not support.'
- **Confidence:** high

### 2026-08-27: A DETECTOR'S FIRE COUNT IS A RATIO — measure how much of its population it could EVALUATE, because "the condition is rare" and "the detector went blind" print the same number [tag: verification]


- **Suggested action:** Add rule: when evaluating a detector for retirement, measure its fire count as a fraction of its evaluable population, not of total plans, because silent population exclusion produces a fire rate indistinguishable from genuine rarity.
- **Reasoning:** A `plan_lint` check fired 3 times (1.2%) over 246 plans. 'On that number it retires.' But the check's evaluable population was only 53 clone-framed plans, and '36 (68%) never reached the comparison at all — the check's segment bound requires the literal triggers? fired:, and it silently skips any tier line lacking it.' The entry: 'the condition is rare and the detector went blind print the same number.' The rule: measure fire count as a ratio of the evaluable population, not the total set.
- **Confidence:** high

### 2026-08-27: WHEN A DATUM IS OPTIONAL, ITS CONSUMERS WILL SILENTLY DISAGREE ABOUT ABSENCE — enumerate them and force-classify each as skip, default, or fail-closed [tag: verification]


- **Suggested action:** Add rule: when declaring a field optional, enumerate every consumer and explicitly classify each as skip, default, or fail-closed on absence. Document this classification at the point of the optional declaration.
- **Reasoning:** 'Doctrine mandated a ten-field manifest stanza on every plan. The lint that reads it is annotated presence-optional in its own source: the whole check sits behind if manifest_m:, so a plan that omits the heading is not checked at all.' Of 40 plans since the mandate with no stanza, '32 had completed their drafting cycle and simply never pasted it. Nothing had ever warned.' Three consumers 'of the same missing datum behaved three different ways, and no one had ever seen them side by side.' Rule: enumerate consumers and force-classify each as skip/default/fail-closed.
- **Confidence:** medium

### 2026-08-26: A verification instrument's DEFAULTS are part of the pin — name the algorithm and flags in the pin itself [tag: verification-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: every verification pin names its instrument verbatim (e.g. `shasum -a 256`, `grep -o … | wc -l`) and notes the divergent default where one exists.
- **Reasoning:** Three concrete instances in one session show the defect surface is the instrument's default, not the artifact: (1) bare `shasum` (SHA-1) against a SHA-256 pin correctly HALTed a healthy file; (2) `grep -c` counted lines while arithmetic counted occurrences; (3) `grep -cF "^## "` made the caret literal and returned zero. The entry states: 'In each case the defect surface was the instrument's default, not the artifact.' The how-to-apply prescribes that 'a pin states its instrument verbatim' — a documentary rule change to verification authoring standards.
- **Confidence:** high

### 2026-08-26: A plan authored on one machine carries its layout's absolute paths into another machine's gates [tag: multi-machine]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: plans intended for cross-machine dispatch must declare deposit paths repo-relative or via env-override forms ($ELUVIAN_WRAP_ROOT, <bellows>), never the authoring machine's absolute layout.
- **Reasoning:** The shop's first cross-machine dispatch (exec-560) 'failed FIVE gate rows purely on path literals: Deposits declared at ~/Developer/bellows (the authoring machine's layout) while the work landed correctly at the executing machine's layout.' The gates `deposit_exists`, `rule_20_self_check`, `rule_22_verification`, and `qa_test_result` all check plan's literal strings on the EXECUTING machine. The fix is a documentary rule change to plan-authoring standards.
- **Confidence:** high

### 2026-08-26: A live canary must be fired in the STATE the tool exists to discriminate — a canary in the ordinary state proves plumbing, not judgment [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a live verification probe (canary/gate) must be fired in the STATE it is designed to discriminate, not only the nominal/running state.
- **Reasoning:** A new gate-watcher 'shipped with 7/7 gates green, a 1531-test suite green, nine dedicated unit tests, and THREE honest live probes against the real database. It could not do its job: it polled plans.lifecycle_state for a pause, and that column never takes the pause value.' Every check passed because 'every check was run while the plan was RUNNING — the live probe returned WATCH: in_progress id=569, which is correct, honest, and says nothing about whether the tool can detect the state it was built to detect.' The rule implied: fire verification probes in the discriminating state.
- **Confidence:** medium

### 2026-08-26: A ruling amended MID-CYCLE moves the artifact its in-flight plans pin — re-pin every consumer at the amendment, or the plan halts on its own precondition [tag: multi-artifact-coherence]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a pinned dependency artifact is amended mid-cycle, every in-flight plan citing it (including SHA pins) must be re-pinned at the moment of amendment.
- **Reasoning:** A cold panel seat proved a design defect; 'the addendum was appended to the rulings file the in-flight plan named in its own Depends on line WITH A SHA.' The fold updated the plan's instructions but 'left the sha alone.' The plan 'was then internally correct and externally dead: its A0 precondition says re-derive the dependency shas; HALT on mismatch, and the dependency had moved.' The general shape: 'an artifact is amended; its consumers' references are left stale.' Rule: re-pin all consumers at the moment of amendment.
- **Confidence:** high

## Instrumentation


### 2026-08-27: EARNABILITY IS NOT DISCRIMINATION — a suite that fails without the fix can still fail to notice a WRONG fix, and a new predicate in front of an old guard silently retires the old guard's coverage [tag: verification]


- **Suggested action:** Add QA checklist step: for any fix whose acceptance rests on a test, enumerate 2-3 plausible wrong fixes (off-by-one strictness, dropped conjunct, inverted default), construct each mutant, and confirm each fails a named test. Report the kill map, not the pass count.
- **Reasoning:** A fix shipped with six tests proving fail-without/pass-with. 'A cold execution seat then built the two most plausible WRONG fixes and ran the same suite against each. Both survived, green.' One mutant 'deleted the older guard the new predicate sits in front of — and that mutant released live claimants, the precise harm the whole arc existed to prevent.' The entry prescribes: 'enumerate the two or three plausible WRONG fixes — the off-by-one strictness, the dropped conjunct, the inverted default — construct each, and confirm each fails a NAMED test.' This is a new procedural QA step, not a rule change to governance docs.
- **Confidence:** medium

### 2026-08-27: Jointly-sufficient guards are individually UN-mutation-testable — redundancy trades testability for robustness [tag: verification]


- **Suggested action:** Add an expected-outcome field (expect: killed|survived) to mutation test configurations for redundant guards, with the test run failing on mismatch in EITHER direction, converting a redundant-guard mutant into a positive assertion.
- **Reasoning:** 'Two independent mechanisms were added to force the same invariant. Either alone is sufficient. Mutation testing then reports that removing either one changes nothing — both single-guard mutants SURVIVE — because the survivor covers for the removed guard.' The entry prescribes: 'an expected-outcome field (expect: killed|survived) with the run failing on a MISMATCH in either direction — which converts a redundant-guard mutant into a positive assertion that the redundancy still holds.' Warning: 'Any such expectation field is a silencing mechanism if it only fails one way.' This is a new procedural safeguard for mutation test configurations.
- **Confidence:** medium

## Structural


### 2026-08-31: AN EMPTY DIRECTORY SATISFIES A PATH CHECK, AND `git -C` INSIDE AN UNINITIALIZED SUBMODULE RESOLVES TO THE PARENT REPO — assert the scope resolves to the repo you meant, before trusting anything the check says about it [tag: verification]


- **Suggested action:** Fix wrap/gate scope checks to assert that the git working tree resolves to the EXPECTED repository (by comparing git rev-parse --show-toplevel output to a known root) before trusting any git-derived output.
- **Reasoning:** 'A wrap gate located its sibling repo as BELLOWS = ROOT / "bellows". On a second machine the same repo is a sibling checkout, and ROOT/bellows is an uninitialized submodule directory — present, and empty.' Both halves matter: 'The directory EXISTS, so every is_dir() / path test passed.' And 'git -C <empty-submodule-dir> resolves up to the PARENT repo. Measured: git -C <root>/bellows rev-parse --show-toplevel printed the governance root.' The fix is structural: assert git working tree identity (--show-toplevel matches expected path) before trusting git output from that path.
- **Confidence:** high

### 2026-08-27: VALIDATE-THEN-WRITE IS NOT ALL-OR-NOTHING — a safety property promised in an operator instruction must be enforced in the code path that can violate it [tag: tooling-integrity]


- **Suggested action:** Fix the multi-file builder to make its write phase atomic: write all files to temporaries, then rename in a single pass, or implement rollback on any write failure so partial writes cannot persist.
- **Reasoning:** 'A multi-file builder validated every anchor before touching anything, then flushed its files in a loop.' A cold seat made one target read-only and 'measured the truth — the builder wrote the first file, then died on an uncaught permission error with an exit code the plan's own table did not classify, leaving a half-edited tree behind a promise of atomicity.' The validation phase was airtight; 'the failure lived entirely in the phase after it.' The fix is a code change: the write phase must be atomic or implement rollback on failure.
- **Confidence:** high

### 2026-08-27: A CHECK WHOSE TWO OPERANDS COME FROM THE SAME SOURCE CAN NEVER FIRE — name each operand's substrate and confirm they can diverge [tag: verification]


- **Suggested action:** Fix the /eluvian daemon sha check to read the running daemon process's actual commit SHA (e.g., from a startup-written file or process environment variable) rather than comparing repo state against repo state.
- **Reasoning:** The /eluvian alignment ritual instructs: 'compare the RUNNING daemon's sha against the new HEAD.' But 'status.py's get_sha() runs git log -1 --format=%h -- bellows.py — repo state. HEAD is also repo state. After a pull both move together, so the comparison is the repository against itself.' The entry confirms: 'The align hook, measured, never even implements the comparison; it lives only as ritual prose resting on a field that cannot answer the question.' The fix is structural: the check must read the running process's loaded SHA, not the repo.
- **Confidence:** high
