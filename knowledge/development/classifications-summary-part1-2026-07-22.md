# Classifications Summary — Part 1 (2026-07-22)

## Cycle Dict (from run_full_lessons_cycle)

```
ingested_count: 15
updated_count: 0
unchanged_count: 106
duplicates_marked_count: 0
needs_classification: [164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178]
terminal_proposals_flagged: []
cycle_timestamp: 2026-07-23T15:05:12.523171+00:00
```

## Classifications (Entries 164–171, first 8 of 15)

### Entry 164 — "A verification check that can FALSE-FAIL is a different risk class"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: before depositing a plan containing a text-parsing verification check, execute it against real data from the corpus it will judge and confirm the expected verdict; prefer extraction-free comparison (canonicalize then longest-common-substring) over parse-then-match; record the measured range in the plan.
- **Reasoning:** Entry documents a false-FAIL incident on plan 247's QA row 9. States: "A QA row that halts on failure has asymmetric costs. A false PASS lets one bad deliverable through; a false FAIL halts good work and manufactures a defect that must then be disproved." The check "FALSE-FAILED 2 of the 3 proposals it checked — both verbatim-correct" due to nested quotation marks and markdown emphasis markers. Prescribes: "before depositing a plan containing a text-parsing verification check, EXECUTE it against real data drawn from the corpus it will judge."

### Entry 165 — "The drafting cycle cannot validate an executable check"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: treat any executable check inside a plan (grep, containment test, computed gate) as requiring execution against real data before deposit; when a lens pass hardens such a check rather than rewriting it, read that as a signal to execute it, not as evidence it is sound.
- **Reasoning:** Entry identifies a structural blind spot in the five-lens drafting cycle. States: "Adversarial reading verifies claims, prose, and reasoning. It cannot verify that a piece of CODE embedded in a plan does what its description says, because every lens reads the description." Plan 247's QA row 9 "passed through six full walks of the five-lens cycle" and Walk 3's hardening "REDUCED the chance of finding it, by converting an obviously-thin check into a plausibly-complete one." Concludes: "A partially-fixed check is the most dangerous state it can occupy."

### Entry 166 — "Finding a halted plan's successor is a three-rung ladder"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add a successor-search procedure to PLANNER_TEMPLATE.md: define the three-rung ladder (1. slug-reference grep in Done/, 2. term-search for technical identifiers, 3. date-adjacency with body-confirmation); state that each rung's result is bounded, that slug must be qualified, and that date-adjacent is candidate-only requiring body confirmation.
- **Reasoning:** Entry documents a method tested against "24 live halted-* artifacts, 2026-07-22." Rung 1 is "Precise and self-confirming" but "Recall is low — anvil-bellows-cycle-1 returns nothing at all"; slug "must be qualified: bare 216 matches 5 files on incidental digits." Rung 2 "works only when the title names a function, table or flag" and "Roughly half the legacy-named plans have no technical identifier whatsoever." Rung 3 is the fallback: "the filename date → same/adjacent-date entries in Done/ → git log --since/--until" but "A date-adjacent plan is a CANDIDATE only — confirm by reading its body."

### Entry 167 — "A diagnostic's substance is FINDINGS, not code"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md halted-plan triage: classify the artifact type before choosing the disposition test; for executables ask whether the code shipped; for diagnostics ask whether the QUESTIONS were answered — look in Done/diagnostic-*, knowledge/research/ deposits, and for restated questions in successor plans.
- **Reasoning:** Entry identifies a category error in disposition methods. States: "Every natural test for 'did this halted plan's work land' asks some version of does the code exist — Applied to a halted diagnostic, all three are category errors, and each one fails toward archive — the disposition that discards." Evidence: "A module existing proves the area was built, never that these questions were answered: the _staging-diagnostic-action-queue-aggregation draft has invoice-pulse/web/action_queue.py sitting in production, which is entirely compatible with its aggregation questions never having been asked."

### Entry 168 — "A directory-declared deposit makes landed and path-resolution unfalsifiable"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md deposit/verification section: a directory-declared deposit is neither present nor missing — record it as 'unmeasurable' and fall through to evidence that can discriminate (look inside the directory for a file attributable to that plan; let the verdict text override the landed flag).
- **Reasoning:** Entry documents how directory deposits defeat boolean existence checks. States: "Rule 37 permits a Deposits: entry to name a parent directory when the filename is unknown at authoring time. The consequence is that every downstream existence check on that deposit passes unconditionally, because the directory exists whatever the plan did." Evidence: "bellows/lifecycle.db records plan 198's deposit as knowledge/research/ with landed=1" but "Plan 198's own stop verdict reads 'Diagnostic incomplete — no findings deposited.'" The "-d accommodation was added specifically to handle plan 198's directory deposit, and it is what manufactures the false positive on plan 198."

### Entry 169 — "The shell's grep is ignore-aware, so completeness sweeps silently under-report"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: for completeness sweeps, use /usr/bin/grep explicitly and state which binary; bound with exclusions/includes and report them; state the result as a bounded negative per Rule 36; use --exclude-dir=.git,.bellows-worktrees,logs plus --include globs for performance.
- **Reasoning:** Entry documents undocumented environment facts. States: "which -a grep resolves to a wrapper dispatching ugrep … --ignore-files, which honours .gitignore." Evidence: "Sweeping five repos for one filename returned 9 hits via the shimmed grep and 28 via /usr/bin/grep — the extras being gitignored logs and DB files." Performance: "/usr/bin/grep -rn across those repos measured 21.7s per filename (≈520s for 24, against Bellows' 600s step_inactivity_timeout_seconds)" but bounded to "2.3s per repo." Concludes: "A bounded sweep reported as exhaustive is worse than no sweep."

### Entry 170 — "A remedy for a correctly-identified defect reliably carries a new defect"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: after folding a fix, re-run the lens that found the original defect on the fix itself; where the fix contains an executable step, run it against real data before accepting it; treat a fix as a new draft that no pass has examined.
- **Reasoning:** Entry identifies a pattern across 30+ drafts. States: "The most repeated failure of a very long drafting cycle (30+ drafts on one diagnostic): a fix for a real problem shipped a new problem that only surfaced when the fix itself was executed." Examples: "The marker-escape written to stop a daemon-write channel moved an inert marker into firing position. The /usr/bin/grep mandated to fix .gitignore under-reporting ran ~22s/file and risked a 600s step timeout." Sharpest form: "an accommodation written for one edge case often produces the defect ON that exact edge case." Prescribes: "Treat a fix as a new draft that no pass has examined, not as a closed finding."

### Entry 171 — "Verify a plan by RUNNING its procedure on real data, not by checking whether its claims are true"
- **Category:** governance_rule
- **Confidence:** high
- **Target:** governance / PLANNER_TEMPLATE.md
- **Suggested action:** Add rule to PLANNER_TEMPLATE.md § The Drafting Cycle: for any plan with a repeatable procedure over items, run that procedure on the hardest one or two real items before deposit — not to verify claims, but to confirm the method produces an answer.
- **Reasoning:** Entry generalizes the executable-check lesson. States: "Eight full drafting-cycle walks and ten cold readers verified every factual assertion in a diagnostic — counts, code line numbers, commit shas, DB rows — and all held. None caught that the plan's core procedure, the successor-search method, collapses on half its target population." The failure: "roughly half the legacy items have no technical identifier in their title, so the mandated term-search returns the entire repo. It was found on the ninth walk, in one probe, by executing the method on a real item." Concludes: "a plan can be factually impeccable and procedurally broken."

## Cluster Synthesis for Gate 1

### Cluster 1: Drafting-Cycle Refinements (entries 164, 165, 170, 171)

Four entries refine **§ The Drafting Cycle** in PLANNER_TEMPLATE.md. All arise from the same arc: plan 247's 30+ draft diagnostic cycle, where the five-lens adversarial review verified every factual claim while missing procedurally broken checks.

- **164 + 165** form a pair: 164 names the specific failure (false-FAIL from text-parsing checks) and prescribes execution against real data; 165 identifies the structural reason (the cycle reads descriptions, not code) and warns that hardening a check reduces the chance of finding its defect.
- **170** generalizes to all fixes: a remedy reliably carries a new defect, so re-run the finding lens on the fix.
- **171** generalizes further: run the whole procedure on real items, not just executable checks — factual correctness and procedural soundness are separate questions.

These four may consolidate into one or two PLANNER_TEMPLATE rules about mandatory execution of plan procedures/checks before deposit, rather than four separate additions. Gate 1 should decide whether they enter as a cluster or individually.

### Cluster 2: Halted-Triage Method (entries 166, 167, 168, 169)

Four entries refine the **halted-plan triage** process, all from the 24-artifact halted-archival audit of 2026-07-22.

- **166** provides the successor-search method (three-rung ladder: slug-reference, term-search, date-adjacency).
- **167** identifies a category error: disposition tests built for executables (does the code exist?) silently mis-handle diagnostics (whose substance is findings, not code).
- **168** documents how directory-declared deposits make existence checks unfalsifiable — proposes a third outcome ('unmeasurable') instead of boolean.
- **169** documents the grep-shimming environment fact (ignore-aware default binary) that silently bounds completeness sweeps.

These four together define the method for halted-plan triage: how to find successors, how to classify the artifact type, and what to do when the standard checks are unfalsifiable or bounded. Gate 1 should consider routing them as a coherent method block.

## Ambiguous Entries

None — all 8 entries classified as governance_rule with high confidence.
