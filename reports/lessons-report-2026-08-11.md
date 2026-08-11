# Lessons Report — 2026-08-11


## Summary


| Category | Count |
|---|---|
| governance_rule | 10 |
| instrumentation | 1 |
| structural | 1 |

**Total proposals:** 12


## Governance Rule


### 2026-08-11: A clone-diff finds defects the ORIGIN carries, not only what the clone dropped [tag: drafting-cycle]


- **Suggested action:** Amend the clone-diff instruction to run before walk 1 and to verify carried guards against live data: for every guard inherited from the parent, state what it is for and confirm it does that against the live state, rather than trusting the parent's shipped status as evidence of correctness.
- **Reasoning:** Flag (G): mechanism-shaped — the named observable is the clone-diff output against the newest same-class parent (identifiable via git log), run before walk 1 so origin defects surface before they generate warm-walk findings. Flag (D): the clone-diff is already codified in DRAFTING_CYCLE.md §2.6; this entry argues for a timing change (before walk 1, not at convergence) and for verifying carried guards against live data rather than inheriting them on shipped status.
- **Confidence:** high

### 2026-08-11: Price what a guard is FOR before building it — an unpriced argument cost five of six walks [tag: drafting-cycle]


- **Suggested action:** Add a pricing gate to the fold-in process: before incorporating machinery into a plan, measure what it protects and what losing it would cost (typically one query). If a guard's region generates findings in consecutive walks while the plan's subject stays dry, treat the guard as the defect.
- **Reasoning:** Flag (G): mechanism-shaped — the named observable is the per-walk finding distribution by region: a guard region that generates findings in consecutive walks while the plan's actual subject stays dry is mechanically detectable by counting findings per region per walk. The entry documents a specific case where an unpriced recovery instrument consumed five of six walks while the core transaction was dry from walk 2 onward, and one query at walk 7 retired the entire region.
- **Confidence:** high

### 2026-08-11: A fix that RECLASSIFIES a state silently widens what proceeds — three consecutive walks, one item [tag: drafting-cycle]


- **Suggested action:** Add a control-flow diff requirement for reclassification folds: when a fold reclassifies, reorders, merges or deletes a branch, diff the control flow by enumerating input values, naming the branch each took before and after, and confirming each still terminates the same way. A stop that disappears is the primary failure mode.
- **Reasoning:** Flag (G): mechanism-shaped — the named observable is the per-input-value branch/termination table (before vs after), mechanically derivable from the edit. Three consecutive instances documented where a correct diagnosis produced a fix that silently removed a HALT, caught each time only by the sequential next lens. Flag (D): v2.3 codified the sequential-lens requirement that catches this class reactively; this entry argues for a proactive control-flow diff at reclassification time rather than relying on the next lens to catch the damage. The reactive guard exists; the proactive prevention does not.
- **Confidence:** high

### 2026-08-11: Only one lens reads outside the artifact, and it does not converge with the others [tag: drafting-cycle]


- **Suggested action:** Move the integration-vs-record lens's context reads (clone origin, live target, daemon source, corpus) to walk 0, so its supply of pre-existing findings is consumed before warm walks begin. Do not close on a falling total count while lens 4 still returns pre-existing findings — that signal means the context is under-read, not that the artifact is converging.
- **Reasoning:** Flag (G): mechanism-shaped — the named observable is the per-walk finding-origin tag (pre-existing vs fold-introduced, tracked in the walk register); lens 4 returning pre-existing findings is a mechanically detectable signal that the convergence reading is premature. Measured data: 14→14→13→9 count with fold-introduced share stalling because lens 4 returned 3 pre-existing per walk while other lenses consumed their own folds.
- **Confidence:** high

### 2026-08-11: 62% of warm-walk findings are the warm walk's own damage — the foundation defects are readable at walk 0 [tag: drafting-cycle]


- **Suggested action:** Codify a mechanical context pin at walk 0: (1) git log for the true newest same-class plan, (2) per anchor fragment its line number, line total length and start column, (3) file-wide grep -c for every replaced token, (4) per target line which plan last wrote it and that plan's lifecycle_state, (5) target file sha. Run before walking.
- **Reasoning:** Flag (G): mechanism-shaped — the named observables are five specific commands each producing a verifiable artifact before walk 1. Measured: 31/50 warm findings (62%) were fold-introduced; cold seats returned 7x findings and 7x HIGH per pass with 0 fold-introduced — every warm fold that followed from wrong foundations was wasted motion. Flag (D): v2.4 codifies the walk-0 context pin derived from this entry; the five-point checklist is the specific operationalization that v2.4 inherits. Classification honest: the substance is already codified in v2.4.
- **Confidence:** high

### 2026-08-11: A step body has exactly ONE reader — a sentence addressed to anyone else is an instruction the wrong party will follow [tag: planner-discipline]


- **Suggested action:** Add a drafting rule: every sentence in a step body must be addressed to the step's executor. Material addressed to the Planner belongs in the deposit note or Cycle Log, not the step. Where a step carries two audiences, name the boundary explicitly in the text.
- **Reasoning:** Flag (G): mechanism-shaped — the named observable is the audience test per sentence (who executes this sentence?) applied at drafting and review time. The entry documents a case where a Planner-addressed instruction to update a pin sat beside an agent-addressed instruction to halt on mismatch, granting the agent permission to defeat the pin. Both sentences individually correct; the defect is co-location with an implicit audience switch.
- **Confidence:** high

### 2026-08-11: An EDIT ANCHOR is not a probe — assert it is the occurrence you mean before rewriting anything [tag: planner-discipline]


- **Suggested action:** Codify the edit-anchor uniqueness requirement: before any edit that removes or replaces a span, assert the anchor's occurrence count is exactly 1 (or lengthen it until it is; never accept the first one). For structural rewrites, write to a temp file, verify completeness against a named section checklist, then os.replace. Snapshot uncommitted artifacts before structural edits.
- **Reasoning:** Flag (G): mechanism-shaped — the named observables are (a) count==1 assertion on every edit anchor before the edit runs, and (b) temp-file-then-replace protocol for structural rewrites. This is the fourth instance of the whole-file-rewrite class in this shop's record and the first with no recovery path — untracked and unsnapshotted, rebuilt from context. The distinction: a probe returns a wrong answer you can read; an edit anchor decides where bytes are destroyed, and a wrong match destroys them silently.
- **Confidence:** high

### 2026-08-11: Four doctrine defects found by reading doctrine AS PROSE — the panel's prose-debt extension [tag: governance]


- **Suggested action:** Route the four identified doctrine defects as governance_rule candidates: (1) Rule 85 cd-first contradicts git -C blessed practice and its assert is vacuous under -C; (2) Rule 93 lacks a blanket-declaration form; (3) Rules 42/44 leave a FORWARD row channel-less at wrap on owner mismatch; (4) final-ACID closing-line bullet is ambiguous between stand-alone post-walk phase and in-walk lens 5.
- **Reasoning:** Flag (G): mechanism-shaped — the named observable is the prose-debt extension protocol (panel seats reading shipped doctrine as prose, each defect provable against the cited rule text). The method lesson: prose-debt on batch-shipped doctrine is dischargeable by dedicated panel extensions. All four defects were found by fresh readers of text shipped by zero-walk batches. Evidence: s2-rewrite walk register and Cycle Log (panel seats 1/3/4, execution-verified).
- **Confidence:** high

### 2026-08-10: A batch fingerprint and the session-wrap ritual are in direct conflict, and nothing warns you [tag: process-discipline]


- **Suggested action:** Codify the freeze obligation: a deposited-but-un-run cycle plan constitutes a corpus freeze on its pinned file, and the session-wrap checklist must check for deposited plans before appending to LESSONS.md. Either dispatch the cycle to completion before wrap, or hold the lessons for the next batch and record that they are held.
- **Reasoning:** Flag (G): mechanism-shaped — the named observable is the deposited-but-un-run plan file's existence in knowledge/decisions/, checkable by the wrap ritual before appending. The entry documents a measured consequence (six un-ingested entries producing a 41 vs 35 count discrepancy) and identifies a structural conflict between two independently correct procedures that is invisible from either side.
- **Confidence:** high

### 2026-08-10: A subtractive cut is verified by a DIFF REVIEW, and a retained-material checklist cannot do it [tag: verification]


- **Suggested action:** Codify the diff-review requirement for subtractive edits: for any cut, diff the removal and read the removed text line by line against what remains; verify each retained item against live data per item, not in aggregate; open and read every rule the justification cites rather than recalling it.
- **Reasoning:** Flag (G): mechanism-shaped — the named observable is the diff output itself (the actual removed lines vs what remains, readable as the output of a diff command). Two instruments structurally fail for subtractive cuts: a retained-material checklist cannot see what the author did not think to list, and a subsumption test is only as good as the property it checks. The diff review is the instrument that works because it reads what was actually removed.
- **Confidence:** high

## Instrumentation


### 2026-08-10: A rule that names its own rationalization still did not bind — the gap is an observer, not wording [tag: drafting-cycle]


- **Suggested action:** Add a mechanically observable invariant to the sequential-fold rule: require per-lens commits so that sequential execution is provable from the record, rather than relying on the rule's wording to prevent batched walks.
- **Reasoning:** Flag (G): mechanism-shaped — the named observable is per-phase commits (a walk that folded sequentially leaves one commit per lens; a batched one does not). The entry identifies the general class of rules that prohibit a practice but carry no mechanism to detect violations. The sequential-fold rule in §2.7 is the specific instance, but the principle — stop hardening the wording and ask what could have observed the violation — applies wherever the artifact looks identical whether the rule was followed or not.
- **Confidence:** high

## Structural


### 2026-08-11: Collapsing an accreted region beats patching it, and the collapse costs exactly one finding [tag: drafting-cycle]


- **Suggested action:** Codify the collapse protocol for accreted regions: when a region takes folds in consecutive walks, collapse into numbered sub-steps ordered so every value is established before it is used, then run the next lens over the collapse specifically, and verify retention by counting distinctive literals rather than by checklist.
- **Reasoning:** Flag (G): mechanism-shaped — the named observables are (a) consecutive-walk folds on a single region (countable from the walk register) triggering the collapse, and (b) distinctive-literal counting as the retention verifier after the collapse. Flag (D): v2.4 codifies the repeated-folds-on-one-region-means-delete principle from which this entry directly descends; the collapse-into-ordered-sub-steps with literal-counting is the specific technique this entry adds to that principle. Classification honest: the principle is already codified; the technique is the incremental contribution.
- **Confidence:** high
