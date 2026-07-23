# Lessons Report — 2026-07-22


## Summary


| Category | Count |
|---|---|
| governance_rule | 15 |

**Total proposals:** 15


## Governance Rule


### 2026-07-22: Finding a halted plan's successor is a three-rung ladder, and the rung is chosen by the title's shape [tag: planner-discipline]


- **Suggested action:** Add a successor-search procedure to PLANNER_TEMPLATE.md (or the halted-plan triage section): define the three-rung ladder (1. slug-reference grep in Done/, 2. term-search for technical identifiers, 3. date-adjacency with body-confirmation); state that each rung's result is bounded, that slug must be qualified, and that date-adjacent is candidate-only requiring body confirmation.
- **Reasoning:** Entry 166 documents a three-rung method for finding halted plan successors. It states the existing record "does not say is that the slug search fails outright on a whole class of plan, and that the failure is silent." Evidence from testing against "24 live halted-* artifacts, 2026-07-22" shows: Rung 1 (slug-reference) is "Precise and self-confirming" but "Recall is low — anvil-bellows-cycle-1 returns nothing at all"; "The slug must be qualified: bare 216 matches 5 files on incidental digits." Rung 2 (term-search) "works only when the title names a function, table or flag" and "Roughly half the legacy-named plans have no technical identifier whatsoever." Rung 3 (date-adjacency) is the fallback: "the filename date → same/adjacent-date entries in Done/ → git log --since/--until" but "A date-adjacent plan is a CANDIDATE only — confirm by reading its body."
- **Confidence:** high

### 2026-07-22: A diagnostic's substance is FINDINGS, not code — disposition methods built for executables mis-handle them silently [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md halted-plan triage: classify the artifact type before choosing the disposition test; for executables ask whether the code shipped; for diagnostics ask whether the QUESTIONS were answered — look in Done/diagnostic-*, knowledge/research/ deposits, and for restated questions in successor plans; source code is not evidence either way for diagnostics.
- **Reasoning:** Entry 167 identifies a category error in disposition methods applied to diagnostics. It states: "Every natural test for 'did this halted plan's work land' asks some version of does the code exist — the deposit's landed flag, a successor plan that shipped the feature, the feature visible in source. Applied to a halted diagnostic, all three are category errors, and each one fails toward archive — the disposition that discards." Evidence: "A module existing proves the area was built, never that these questions were answered: the _staging-diagnostic-action-queue-aggregation draft has invoice-pulse/web/action_queue.py sitting in production, which is entirely compatible with its aggregation questions never having been asked." The entry prescribes: "classify the artifact before choosing the test. For an executable, ask whether the code shipped. For a diagnostic, ask whether the QUESTIONS were answered."
- **Confidence:** high

### 2026-07-22: A directory-declared deposit makes `landed` and path-resolution unfalsifiable — it needs a third outcome, not a boolean [tag: qa-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md deposit/verification section: a directory-declared deposit is neither present nor missing — record it as 'unmeasurable' and fall through to evidence that can discriminate (look inside the directory for a file attributable to that plan; let the verdict text override the landed flag).
- **Reasoning:** Entry 168 documents how directory deposits defeat boolean existence checks. It states: "Rule 37 permits a Deposits: entry to name a parent directory when the filename is unknown at authoring time. The consequence is that every downstream existence check on that deposit passes unconditionally, because the directory exists whatever the plan did." Evidence: "bellows/lifecycle.db records plan 198's deposit as knowledge/research/ with landed=1. The directory resolves, so a -d test reports the deposit present. Plan 198's own stop verdict reads 'Diagnostic incomplete — no findings deposited. Step 1 hit a BLOCKING permission denial.' Nothing landed." The entry concludes: "a directory-declared deposit is neither present nor missing — record it as unmeasurable and fall through to evidence that can discriminate."
- **Confidence:** high

### 2026-07-22: The shell's `grep` is ignore-aware, so completeness sweeps silently under-report — and the un-ignored form is slow enough to time a step out [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: for completeness sweeps, use /usr/bin/grep explicitly and state which binary; bound with exclusions/includes and report them as part of the finding; state the result as a bounded negative per Rule 36, never as exhaustive; use --exclude-dir=.git,.bellows-worktrees,logs plus --include globs to keep runtime under step-timeout limits.
- **Reasoning:** Entry 169 documents two undocumented environment facts about grep. It states: "which -a grep resolves to a wrapper dispatching ugrep … --ignore-files, which honours .gitignore." Evidence: "Sweeping five repos for one filename returned 9 hits via the shimmed grep and 28 via /usr/bin/grep — the extras being gitignored logs and DB files. So any 'grep proves no other references exist' conclusion drawn with the default binary is bounded without saying so." On performance: "/usr/bin/grep -rn across those repos measured 21.7s per filename (≈520s for 24, against Bellows' 600s step_inactivity_timeout_seconds)." The fix: "Bounding it with --exclude-dir=.git --exclude-dir=.bellows-worktrees --exclude-dir=logs plus --include globs brought it to 2.3s per repo." The entry concludes: "A bounded sweep reported as exhaustive is worse than no sweep."
- **Confidence:** high

### 2026-07-22: A remedy for a correctly-identified defect reliably carries a new defect — test the fix against the same lens and data that found the original [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: after folding a fix, re-run the lens that found the original defect on the fix itself; where the fix contains an executable step (grep, guard, command), run it against real data before accepting it; treat a fix as a new draft that no pass has examined.
- **Reasoning:** Entry 170 identifies a pattern where fixes introduce new defects. It states: "The most repeated failure of a very long drafting cycle (30+ drafts on one diagnostic): a fix for a real problem shipped a new problem that only surfaced when the fix itself was executed." Multiple examples cited: "The marker-escape written to stop a daemon-write channel moved an inert marker into firing position. The /usr/bin/grep mandated to fix .gitignore under-reporting ran ~22s/file and risked a 600s step timeout." The sharpest form: "an accommodation written for one edge case often produces the defect ON that exact edge case." The entry prescribes: "after folding a fix, do not move on — re-run the lens that found the original defect, and where the fix contains an executable step … run it against real data before accepting it. Treat a fix as a new draft that no pass has examined, not as a closed finding."
- **Confidence:** high

### 2026-07-22: Verify a plan by RUNNING its procedure on real data, not by checking whether its claims are true — the two are different audits [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: for any plan that hands an agent a repeatable procedure over a set of items, run that procedure on the hardest one or two real items before deposit — not to verify the claims, but to confirm the method produces an answer; 'the instructions are correct' and 'the instructions work' are separate questions.
- **Reasoning:** Entry 171 generalizes the executable-check lesson to full plan procedures. It states: "Eight full drafting-cycle walks and ten cold readers verified every factual assertion in a diagnostic — counts, code line numbers, commit shas, DB rows — and all held. None caught that the plan's core procedure, the successor-search method, collapses on half its target population." The failure: "roughly half the legacy items have no technical identifier in their title, so the mandated term-search returns the entire repo. It was found on the ninth walk, in one probe, by executing the method on a real item." The entry concludes: "a plan can be factually impeccable and procedurally broken, and the adversarial lenses (which read the plan) are structurally blind to the second failure. Only execution reveals it." The prescription: "run that procedure yourself against the hardest one or two real items before deposit."
- **Confidence:** high

### 2026-07-22: Restructuring a plan for DRY (splitting, or extracting shared content) trades duplication for a consistency surface that then needs its own hardening [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: before splitting or extracting shared content, diff the candidate-shared regions and move only byte-identical clauses; after extraction, walk the seam as its own surface — the ACID and destruction lenses have the most purchase there. State the four-part extraction contract: what moves, what stays, how the moved content is retrieved, and what the retrieval promises.
- **Reasoning:** Entry documents how DRY restructuring of plans relocates defects into seams. States: "Both moves reduced size and were correct — and both relocated the hardest defects into the seam. Every seam defect had one shape: two representations of a single fact that can disagree." Identifies the governing rule as "single-source what is IDENTICAL between the parts; keep inline what DIFFERS. Unifying things that differ is the false-sharing bug; duplicating things that are identical is the drift bug." Further prescribes a four-part extraction contract: "what moves, what stays, how the moved content is retrieved, and what the retrieval promises (over-return, under-return, an absent source). Each unstated part is a separate defect."
- **Confidence:** high

### 2026-07-22: Generalising a concrete guard into an inference waters it down when the specific value carried information the general phrasing does not [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when moving a guard into a reusable or generic form, keep the mechanism generic but require the caller to pin the specifics; make the absence of a pin a hard failure. Ask of any generalisation: did the concrete version carry information (a list, a count, a name) that the general version turns into a judgment call? If so, the specifics must be re-supplied at the point of use.
- **Reasoning:** Entry documents how extracting a shared audit contract caused a blast-radius guard to degrade. States: "the plans' C7 blast-radius guard — an explicit six-repo list — became the contract's generic 'every repo this plan reads and the root.' Neither plan then re-stated the concrete set, so the guard degraded to 'whatever repos the agent infers it read.'" Identifies the asymmetric failure: "one plan reads a repo (for a cross-reference) that holds none of its target files, and an agent inferring the set from file locations would silently drop that repo from the one check that watches blast radius." Concludes: "A concrete enumerated list is the guard; a generic description is a prompt to re-derive it, and re-derivation can undercount."
- **Confidence:** high

### 2026-07-22: The finished deliverable's physical shape is a question none of the instruction-lenses asks — inspect the output form separately [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: before deposit, sketch one real block of the finished deliverable — the actual rows, cells, or sections a single item produces — and confirm the mandated format can hold everything the plan requires per item. Where per-item output is rich, prefer a block-per-item structure with a compact summary index over a table.
- **Reasoning:** Entry identifies a blind spot in the five adversarial lenses: they examine the procedure but not the output form. States: "Twelve drafting-cycle walks examined whether a diagnostic's instructions were correct, safe, answerable, and mutually consistent. None asked what the finished report would physically look like." The consequence: "the mandated output format (a markdown table, one row per work item) structurally could not hold the per-item evidence the entire plan existed to capture: quoted verdict prose, a DB-flag-vs-filesystem pair, a three-part live-work burden. The format requirement silently defeated every content requirement." Concludes: "A plan can have flawless instructions that assemble into an unusable artifact."
- **Confidence:** high

### 2026-07-22: Read the record before deriving — three times in one cycle a method or fact was reconstructed empirically that was already codified, twice in a file the plan already cited [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: run the integration-vs-record scan early, before building a method from scratch — grep the template's named sections, LESSONS.md, and especially any file the plan already references for another purpose. Empirical derivation should confirm and sharpen the codified answer, not substitute for finding it.
- **Reasoning:** Entry documents repeated re-derivation of already-codified facts within a single cycle. States: "Three times in one cycle: the DB-as-index / filesystem-as-ground-truth protocol was rediscovered across three lenses before someone read the Lifecycle DB Read Protocol section; the git --no-pager requirement was derived after a timeout when it was a codified Compression Principle; and the halted-plan successor method (three greps + a landed-check) was reconstructed over three lenses when BACKLOG-ARCHIVE.md — a file the plan already cited for a different fact — states it outright, with an outcome prior (9 of 16 had successors, 7 did not) the empirical work lacked." Prescribes: "run the integration-vs-record scan EARLY, not as lens four" and "When you cite a file, read the rest of it."
- **Confidence:** high

### 2026-07-22: A Bellows-dispatched step's OUTPUT files must be written at paths relative to the agent's own working tree; absolute main-tree paths are correct for canonical-DB READS and wrong for deposit WRITES [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md Bellows dispatch section: split path rules by operation — READS of shared state (canonical DB, other repos, config) take an absolute path; WRITES of the step's own deposits take a path relative to the agent's working tree. Never use a blanket "run from X" instruction.
- **Reasoning:** Entry codifies the plan-225 worktree-teardown lesson. States: "A plan that runs under worktree isolation but instructs the agent to write its deposit to an absolute main-tree path lands the file in the main tree, where the worktree's own commit cannot see it: teardown commits nothing, main gains an untracked file, and the cherry-pick collides with a byte-identical untracked copy — the R2 failure shape." Identifies root cause: "The plan-225 incident came from a single 'commands run from the main tree' line that was right for canonical-DB access and wrong for file output." Prescribes: "read the world by absolute path; write your own output where you stand."
- **Confidence:** high

### 2026-07-22: The five adversarial lenses do not check a plan against the codified authoring rules — a mechanical conformance pass belongs in the drafting cycle [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: add a mechanical conformance pass (distinct from the five lenses) — run plan_lint, then walk the plan against the Orchestration Plan Rules and the Plan Authoring Checklist by scope; do it once the plan's shape is stable, before the closing walk.
- **Reasoning:** Entry identifies a gap between adversarial review and mechanical conformance. States: "Weak-spots, destruction, vulnerabilities, integration-vs-record, and ACID all interrogate the plan's reasoning; none systematically checks it against the codified authoring surface (the Orchestration Plan Rules, the Plan Authoring Checklist, plan_lint)." Evidence: "A dedicated mechanical conformance pass, run mid-cycle, caught what the adversarial lenses had missed across several walks: a missing declared Scope: block (Checklist 23), absent Rule-41 liveness anchors on a long SA step, a ## How to Run block that violated Rule 35 for Bellows dispatch, and a stale marker count." Concludes: "These are not defects of reasoning — they are conformance failures, invisible to lenses that ask 'is this correct?' rather than 'does this match the rules?'"
- **Confidence:** high

### 2026-07-22: A plan's pre-stated conclusions anchor the executing agent toward them — and toward the cheapest disposition; each must carry the same evidence burden and a mandatory verification the agent can falsify [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: pre-state a conclusion only with (1) named, agent-runnable verification anchors and explicit licence to disagree; (2) a statement that the pre-resolutions are a fact about which items were investigated, not a distribution; and (3) equal evidence burden on every disposition, so the cheap/default one is not the low-effort path.
- **Reasoning:** Entry documents three compounding failure modes from pre-stated conclusions in plans. States: "Anchoring: the pre-resolutions become a forecast — the agent infers the un-resolved items are probably the same, biasing toward the pre-stated answer. Direction: every over-reach in the cycle ran toward archive, the cheap disposition that closes an item, because the plan's whole method was built to recognise 'shipped/dead' and anything ambiguous fell toward it. Wrong-direction risk: one pre-resolution (a duplicate-pair survivor) was initially framed as live work and was in fact archive — the Planner had been confidently wrong about that exact pair once already." Concludes: "The value of a pre-resolution (it saves the agent real work) is only safe if it cannot launder an assertion into an audited finding."
- **Confidence:** high

### 2026-07-21: A verification check that can FALSE-FAIL is a different risk class — execute it against live data before the plan ships [tag: qa-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: before depositing a plan containing a text-parsing verification check, execute it against real data from the corpus it will judge and confirm the expected verdict; prefer extraction-free comparison (canonicalize then longest-common-substring) over parse-then-match; record the measured range in the plan.
- **Reasoning:** Entry 164 documents a false-FAIL incident on plan 247's QA row 9 and proposes a governance rule for executable checks. It states: "A QA row that halts on failure has asymmetric costs. A false PASS lets one bad deliverable through; a false FAIL halts good work and manufactures a defect that must then be disproved." The evidence describes the row "FALSE-FAILED 2 of the 3 proposals it checked — both verbatim-correct" due to nested quotation marks and markdown emphasis markers. The recommendation is explicit: "before depositing a plan containing a text-parsing verification check, EXECUTE it against real data drawn from the corpus it will judge" and "Prefer extraction-free comparison (canonicalize, then longest-common-substring) over parse-then-match; the parse step is where false FAILs are born."
- **Confidence:** high

### 2026-07-21: The drafting cycle cannot validate an executable check — and a fold that "hardens" one cements its blind spot [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: treat any executable check inside a plan (grep, containment test, computed gate) as requiring execution against real data before deposit; when a lens pass hardens such a check rather than rewriting it, read that as a signal to execute it, not as evidence it is sound.
- **Reasoning:** Entry 165 identifies a structural blind spot in the five-lens drafting cycle. It states: "Adversarial reading verifies claims, prose, and reasoning. It cannot verify that a piece of CODE embedded in a plan does what its description says, because every lens reads the description." The evidence describes how plan 247's QA row 9 "passed through six full walks of the five-lens cycle" and Walk 3's hardening "REDUCED the chance of finding it, by converting an obviously-thin check into a plausibly-complete one." The entry concludes: "treat any executable check inside a plan … as requiring EXECUTION against real data before deposit" and warns that "A partially-fixed check is the most dangerous state it can occupy, because it buys confidence without buying coverage."
- **Confidence:** high
