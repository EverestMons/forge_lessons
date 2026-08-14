# Lessons Report — 2026-08-14


## Summary


| Category | Count |
|---|---|
| governance_rule | 4 |
| structural | 2 |

**Total proposals:** 6


## Governance Rule


### 2026-08-14: Narrating a severance re-introduces the severed content [tag: drafting-cycle]


- **Suggested action:** Add a DRAFTING_CYCLE.md §2.7 rule: honor a severance by absence in the artifact, not by narration — when a record must refer to removed content, use a description or pointer, never reproduce it. Candidate owner: §2.7 retraction/edit-anchor orbit.
- **Reasoning:** Entry identifies a class where narrating a severance re-introduces the severed content: a History row explaining that content was removed named the removed content verbatim, reversing the severance in the artifact while honoring it in intent. The mechanism generalizes (strike notes quoting structural tokens, retraction text as a literal instance). The fix is a documentary discipline rule — not a tool — because the defect class is in what the author WRITES, which only a rule can govern. Paired with entry 343 (record-hygiene pair): 341 is about re-introducing severed content through narration; 343 is about a marker token colliding with text about the marker.
- **Confidence:** high

### 2026-08-14: A clone is diffed section-by-section, never token-swapped — 17 of 18 findings were origin-carried and one would have halted a correct run [tag: drafting-cycle]


- **Suggested action:** Bind the Planner's own clone-derivation process: diff a clone section-by-section against its origin at token level, report per section (dropped, mis-adapted, faithfully carried, re-added), and rebuild probe batteries from the new mechanism's own post-condition list. Candidate owner: PLANNER_TEMPLATE.md clone-derivation rules or DRAFTING_CYCLE.md §2.6 clone-diff process.
- **Reasoning:** Entry documents that a token-swap clone derivation missed 17 of 18 findings (all origin-carried), including a blocker where the origin's probe battery asserted a version literal measuring 0 after a correct apply. The fix — section-by-section diff at token level — is mechanism-shaped: a structured procedure that could be mechanized. DEDUP CAVEAT: 'section-by-section at token level' already counts 1 in live DRAFTING_CYCLE.md in §2.6's clone-diff BRIEF, binding the cold SEAT. Entry 342's claim is distinct: it binds the PLANNER's own derivation at walk 0, not the cold seat's review. The distinction between planner-derivation binding and cold-seat-review binding is the whole proposal; Gate 1 decides whether this is an extension or a duplicate.
- **Confidence:** high

### 2026-08-14: The marker-collision fired on the first artifact written after it shipped [tag: verification]


- **Suggested action:** When a mechanism keys on the presence of a token in human-authored text, price the collision as a certainty — not a risk — and make attesting rows state so explicitly. Candidate owner: walk-register schema's annotation rule or DRAFTING_CYCLE.md §2.7.
- **Reasoning:** Entry documents that the walk-register v0.3 verbatim-ellipsis annotation collided on its very first use: a row DESCRIBING the annotation class was read as attesting, and the verdict happened to be correct by accident. A correct verdict from an accidental mechanism is the dangerous mode — with elided bytes it would have silently certified a real truncation. The fix is a discipline rule about annotation-mechanism design. Paired with entry 341 (record-hygiene pair): 343 is about a marker token colliding with text about the marker; 341 is about re-introducing severed content through narration.
- **Confidence:** high

### 2026-08-14: A session that crosses midnight carries a stale date into every slug it authors [tag: operational-recovery]


- **Suggested action:** Measure the date at each plan's authoring (date and date -u, which can disagree), never inherit it from the session's opening context; when a stale date has already propagated, strike the factual claims and leave the identifiers alone. Candidate owner: PLANNER_TEMPLATE.md deposit conventions (the id-at-deposit rule's sibling).
- **Reasoning:** Entry documents that a session crossing midnight carried a stale date into every slug authored the next morning because the date was inherited from the baton rather than measured. The slugs are identifiers and stay byte-stable, but factual claims about WHEN were a day wrong. The fix is a discipline rule about deposit conventions — measure at authoring, not inherit from context. This is the read-id-sequence-at-deposit pattern in a different variable.
- **Confidence:** high

## Structural


### 2026-08-14: A fold is the only edit in the system with no post-condition — six rules govern it and all six key on the wrong unit [tag: drafting-cycle]


- **Suggested action:** Build a mechanized fold_check that diffs the machine-readable state (plan_lint, gates.py, probe battery outputs) against a pre-fold baseline after every fold, and add one DRAFTING_CYCLE.md §2.7 bullet making the fold — not the culmination — the unit carrying the post-condition. Owner: fold_check tooling + DRAFTING_CYCLE.md §2.7.
- **Reasoning:** Entry proposes that the fold is the only mutating act in the system with no post-condition — six rules govern folds and all six key on the culmination, so damage lands and survives until the next cold-seat reader arrives. The fix is mechanical: a tool that re-runs the artifact's machine readers after each fold and diffs the result set, catching defects invisible to human reading. The CEO-approved remedy (2026-08-14, 'proceed as recommended') is a mechanized fold_check plus one §2.7 bullet; the remedy is approved and not yet built (measured: fold_check 0, machine-readable state 0 in live DRAFTING_CYCLE.md). Paired with entry 340 (fold-safety pair): 339 addresses the missing post-condition on folds; 340 addresses the machine-contract breakage channel.
- **Confidence:** high

### 2026-08-14: A fold's own prose can break a machine contract — three times in one cycle, every one invisible to reading [tag: verification]


- **Suggested action:** After ANY fold to a machine-read artifact, re-run every reader (plan_lint, gates.py, probe battery) and diff the result set against the pre-fold baseline — a fold must not change the machine-readable state except in the direction it intends. Owner: fold_check tooling (the same mechanism as entry 339's; this entry supplies the machine-contract-breakage evidence).
- **Reasoning:** Entry documents three instances in one cycle where a fold's prose broke a machine contract — deleting a literal plan_lint requires, silencing a lens check leg, and tripping a test-scope check — all invisible to reading because the audience is a regex. The fix is the same mechanized fold_check as entry 339: diffing machine-readable state pre- and post-fold. The CEO-approved remedy (2026-08-14) is a mechanized fold_check plus one §2.7 bullet; the remedy is approved and not yet built (measured: fold_check 0, machine-readable state 0 in live DRAFTING_CYCLE.md). Paired with entry 339 (fold-safety pair): 340 supplies the machine-contract-breakage evidence while 339 frames the missing post-condition.
- **Confidence:** high
