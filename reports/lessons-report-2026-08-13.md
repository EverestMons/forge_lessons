# Lessons Report — 2026-08-13


## Summary


| Category | Count |
|---|---|
| governance_rule | 4 |
| instrumentation | 3 |
| structural | 3 |

**Total proposals:** 10


## Governance Rule


### 2026-08-13: One action per ops compound — the close-compound carries a POST-CONDITION, and an unrouted clause is a Gate-1 bypass even when it is right [tag: drafting-cycle]


- **Suggested action:** Codify the one-action-per-compound rule with mandatory post-condition close into PLANNER_TEMPLATE.md (already shipped as Rule 85 in PT v4.88 via plan 389). Also codify the severance discipline: doctrine text that surfaces during drafting enters through routing (LESSONS corpus → Gate 1 → gates), never by inlining mid-draft — the severance-and-corpus-path is the correct disposition.
- **Reasoning:** Entry names two rules: (1) every ops compound performs ONE state change and CLOSES by verifying its post-condition — measured twice in session (386 C5, 389), shipped as PT v4.88 Rule 85; (2) when drafting surfaces a rule worth keeping, route it through the corpus, never inline it — the scout caught an unrouted clause and severed it. Both are governance-level disciplines for plan authoring. The compound rule is mechanism-shaped with a named owner (PLANNER_TEMPLATE.md Rule 85). The severance rule is a Gate-1-routing discipline.
- **Confidence:** high

### 2026-08-13: A summary line attested a lint run that never happened — the attestation was written from intention, not output [tag: drafting-cycle]


- **Suggested action:** Write result-describing lines only from captured output (paste-adjacent, then compress to summary); treat every pre-classification of gate/lint output as a prediction that the closing run must confirm, and correct the text from the measured set before deposit — recording the correction rather than overwriting silently. Candidate owner: DRAFTING_CYCLE.md section 2.7's lens-attestation bullet.
- **Reasoning:** Entry documents a summary line that attested a lint run before it happened — the closing-record re-read caught it against actual command history (391 cycle). The class extends the attestation-integrity rule: a summary sentence describing tool output IS an attestation, and writing it before the run leaves a window where the record certifies a fiction. 392 repeated from the other side: the close lint FALSIFIED the draft's 'no expected advisories' pre-classification (six (o2) advisories are the true set). A pre-classification is a claim about a future mechanical result. Part of the attestation-integrity pair with entry 337.
- **Confidence:** high

### 2026-08-13: A strike note that QUOTES a section header becomes a second anchor match — describe tokens, don't exhibit them, in records that carry retractions [tag: drafting-cycle]


- **Suggested action:** In registers, strike notes, and fold commentary, reference structural tokens by description ('the section header above') or with a deliberate spelling break — never exhibit them verbatim. Keep the count-1 anchor assert on every scripted edit, because it is the instrument that turns this class from silent corruption into a loud halt. Candidate owner: DRAFTING_CYCLE.md section 2.7's edit-anchor bullet.
- **Reasoning:** Entry documents a register strike note that quoted the '## Deviations' header token verbatim; a later scripted edit anchored on that header matched the QUOTE first and tripped the count-1 assert (correct behavior — the assert exists for exactly this). Every quoted structural token in a register is a decoy for future anchors. The class joins the edit-anchor rule with the retraction-classification rule: a well-run cycle accumulates text ABOUT its own structure, and each verbatim token is an anchor collision waiting to happen.
- **Confidence:** high

### 2026-08-13: The daemon claims an uncommitted deposit within one second — commit the claimed rename, and predict ids, never mint [tag: operational-recovery]


- **Suggested action:** The deposit compound is always: fresh id read, copy, attempt commit, on failure restore-staged and commit the daemon's rename. Never pre-write the id anywhere the freeze does not re-derive, and treat a failed deposit commit as the EXPECTED path, not an error. Largely already carried by PLANNER_TEMPLATE and operational memory; Gate 1 should dedup against live doctrine.
- **Reasoning:** Entry documents the deposit claim-race firing identically at 391 and 392: the daemon renamed the just-copied deposit to in-progress within one second of the git commit, and the defensive sequence (commit attempt, restore --staged on failure, commit the on-disk claimed state) handled both cleanly. The id-consumption window is also real: 391's authoring-time read said 390, the parallel terminal consumed it in-window, and the at-deposit re-read caught it. The fix is a governance-level procedure (discipline-shaped) largely already carried by PLANNER_TEMPLATE + operational memory.
- **Confidence:** high

## Instrumentation


### 2026-08-13: Every sqlite sentinel prints BEFORE the COMMIT — a rollback run produces perfect evidence with nothing written [tag: verification]


- **Suggested action:** Every transactional write step must end with a separate fresh-invocation read-back whose expected values are asserted — in-transaction sentinels prove intent, not durability. The step's record must state this distinction explicitly. A verdict or QA item citing only in-transaction sentinels has verified nothing. Strong mechanism candidate: a QA-row convention for post-COMMIT read-back alongside DRAFTING_CYCLE.md section 2.7's execute-against-real-data bullet.
- **Reasoning:** Entry proves that every sentinel SELECT in a transactional flip script executes and prints before COMMIT — a run ending in ROLLBACK emits byte-identical success evidence with nothing written (386 panel proof S3-2, 389 re-measurement). The evidence is real output from real queries about a transaction that never became durable. The only proof of durability is a post-COMMIT read-back from a fresh connection. The fix is a new verification step (discipline-shaped today), not a documentary rule change. Part of the probe-integrity pair with entry 336.
- **Confidence:** high

### 2026-08-13: The probe was authored from prediction and would have halted a CORRECT run — measure every expected value ON the pinned artifact [tag: verification]


- **Suggested action:** Every expected count or value in a probe battery must be derived by executing the probe against the pinned source artifact at authoring time — and re-derived after ANY fold that touches that artifact. A probe value with no derivation command next to it is a prediction wearing a probe's clothes. Strong mechanism candidate: a probe-derivation clause alongside DRAFTING_CYCLE.md section 2.7's execute-against-real-data bullet.
- **Reasoning:** Entry documents a probe that expected 3 occurrences where the pinned reference measured 2 (392 scout finding) — the number was written from the author's mental model rather than by running the grep. On dispatch, a CORRECT apply would have failed the probe, triggered the restore arm, and halted the plan: the guard destroying the work it guards. The fix is a probe-authoring procedure (discipline-shaped today): derive by execution, re-derive after every fold. Part of the probe-integrity pair with entry 333.
- **Confidence:** high

### 2026-08-13: Deliverable counts in templates go stale when the deliverable grows — sweep every count-carrying template site after a late addition [tag: drafting-cycle]


- **Suggested action:** After any fold that changes a deliverable's cardinality, grep the draft for the OLD count and re-derive every hit — commit messages, QA arithmetic, prose claims. Where a count must appear in multiple sites, the post-fold sweep is the price of that duplication. Candidate owner: DRAFTING_CYCLE.md section 2.7 (alongside the declare-once rule's companion).
- **Reasoning:** Entry documents 392 shipping 8 new tests while its commit-message template and QA Item-4 arithmetic both still said 7 — written before the scout's fold added test 8 and never re-swept. The header expectation WAS updated (to 1025), so the plan carried an internal contradiction. The QA agent caught it live and classified against the diff (8 test functions, 27 = 19+8). The class: the count lives in N sites, the fold updates the one the author is looking at, and the others decay. Part of the attestation-integrity pair with entry 334.
- **Confidence:** high

## Structural


### 2026-08-13: Register DUP-APPEND — one bullet in, two identical rows out, in the cycle's own record [tag: drafting-cycle]


- **Suggested action:** The walk_register_lint v0.3 duplicate_row guard mechanizes detection of byte-identical duplicate data rows in walk registers (already shipped via plan 392). Run the v0.3 lint per culmination; treat any duplicate-row WARN as a record defect to strike. When building new guards, validate against the real corpus before trusting output — the false-positive shape (header repeats producing 34 false hits in the first prototype) was invisible to reasoning and obvious only to execution.
- **Reasoning:** Entry documents the DUP-APPEND channel class recurring in walk registers: 389's capstone pass found a duplicated open-tail line (F2-1), and the class was measured twice in one register during the s40sweep arc. A duplicated record line is invisible to every content probe — both copies are individually correct. The fix is mechanical: walk_register_lint v0.3's duplicate_row guard flags byte-identical data rows as UNCONFORMANT. Part of the register/validator pair with entry 331 (both shipped via plan 392's schema v0.3 and walk_register_lint guards).
- **Confidence:** high

### 2026-08-13: Headerless table rows are INVISIBLE to a header-anchored parser — 46 committed rows had never been validated [tag: verification]


- **Suggested action:** The walk_register_lint v0.3 headerless_rows guard detects fold-shaped pipe rows outside any parsed table, including files with no parsed table at all (already shipped via plan 392). Any headerless row flips the file UNCONFORMANT. When a tool's recognition rule can silently EXCLUDE malformed instances of the thing it validates, add a guard for the excluded shape — ask 'what does my parser silently skip?' and measure over the real corpus.
- **Reasoning:** Entry documents the silent-exclusion failure: 46 committed headerless fold rows across 4 registers had never been validated because the header-anchored parser skipped them entirely — including 16 panel-seat rows in 386's register that no validator run had ever read. The fix is mechanical: v0.3's headerless_rows guard catches any fold-shaped pipe row outside a parsed table (the worst case — files with no parsed table at all — was caught by the scout). Part of the register/validator pair with entry 330 (both shipped via plan 392's schema v0.3 and walk_register_lint guards).
- **Confidence:** high

### 2026-08-13: A case-insensitive filesystem defeats a realpath guard — compare inodes, not strings [tag: verification]


- **Suggested action:** Every path-identity guard must test by inode (os.path.samefile), never by string equality of resolved paths — a case-insensitive filesystem (macOS default) defeats the string test. Retain the realpath test for the non-existing-file case and add a directory-prefix rejection when the write must leave the tree entirely. This is a builder-authoring convention with no single owning artifact today; the fix was applied to builders 389/391/392.
- **Reasoning:** Entry demonstrates the bypass: 389's execution seat showed a realpath-string comparison passing a differently-cased path to the same file on a case-insensitive filesystem — the guard said 'different file' while the write destroys the live artifact. Closed with os.path.samefile alongside the realpath test, plus a root-subtree rejection. The fix is mechanical (inode-level identity) and has been applied to each subsequent builder, but the convention has no single named owner — it applies to every builder that guards a path identity.
- **Confidence:** high
