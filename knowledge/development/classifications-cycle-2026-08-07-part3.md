# Classifications — Cycle 2026-08-07, Part 3 (Tranche C: entries 249–265)

**Plan:** executable-311
**Step:** 4 — Classification tranche C (the remainder)
**Date:** 2026-08-07

---

## Entry 249 (proposal 257) — `planner-discipline` → `governance_rule`

**Target:** PLANNER_TEMPLATE.md

The entry measures four recurrences in one cycle of constraints the author had just recorded: a quote cited from memory dropped a clause, a plan population was recalled incorrectly, and two constraints written into the plan were violated immediately after being written. The core finding is that prose rules — in LESSONS.md or in the plan's own ledger — have no mechanical consequence, and the author is the least reliable enforcer. The proposed fix is a governance_rule because it establishes a new authoring principle: prefer executable rules over remembered ones, add the violation-catching check in the same edit that records a constraint, and treat recurrence after recording as evidence the lesson needs mechanising (routing to the forge rather than another prose restatement). The scout noted this could be `reference` or a Gate-1 routing principle; I classify as governance_rule because the entry contains four concrete actionable recommendations that could become PLANNER_TEMPLATE.md rules, and Gate 1 will decide the routing question.

## Entry 250 (proposal 258) — `drafting-cycle` → `governance_rule` — CLUSTER (A)

**Target:** DRAFTING_CYCLE.md (routes into the reserved CEO shape decision, baton item 2)

The entry measures that walk 3 of diagnostic 301 was aimed at the Cycle Log — a region no lens had ever read — and six of eight findings landed there, all record-decay class. Attention had followed what each phase changed, never what the changes accumulated into. The proposed rules (walk the Cycle Log as a region on a schedule, label narrative blocks with their phase, name coverage rules not counts, count record-decay separately) are all governance_rule because they are documentary rules about how the drafting cycle's Cycle Log is reviewed and maintained. This is cluster (A) evidence: the Cycle Log's review schedule and the record-decay/instruction-defect distinction are both inputs to the shape decision the CEO has reserved.

## Entry 251 (proposal 259) — `drafting-cycle` → `governance_rule` — CLUSTER (A) CENTERPIECE

**Target:** DRAFTING_CYCLE.md (routes into the reserved CEO shape decision, baton item 2)

This IS the shape decision. The entry measures that the dry condition — a full walk returning dry over a region the previous walk did not touch — is structurally unreachable because every culmination creates new unexamined surface. Four consecutive plans (296, 298, 300, 301) closed on judged stops with the condition unmet. The proposed replacement criterion — close on COMPOSITION (no finding that changes what an agent will DO) rather than dryness — is governance_rule because it proposes a fundamental change to §2's termination condition. The entry also proposes measuring convergence ACROSS plans (does walk 1 on a new plan find less than walk 1 on the last?) and treating judged stops as the normal outcome rather than a deviation. All of this is core shape-decision evidence.

## Entry 252 (proposal 260) — `instrumentation` → `governance_rule`

**Target:** DRAFTING_CYCLE.md

The entry measures that an un-walked plan lints clean (3 PASS / 0 WARN) while a fully-walked one WARNs (2 WARN / 3 PASS), because "not run" contains no fold-token that triggers the WARN. The codifiable residue after the bellows-owned half (the not-run token treated as failing — a Rule 46 question for Gate 1) is governance_rule: phrase status lines so they cannot match the gate's pattern until the condition is true, rewrite to canonical only once earned, and ship earned WARNs unsilenced. These are documentary authoring rules about the interaction between records and checkers, not a tooling change or procedural mechanism. The bellows-owned gate defect is noted in suggested_action for Rule 46 routing.

## Entry 253 (proposal 261) — `verification` → `governance_rule`

**Target:** DRAFTING_CYCLE.md

The entry records the author producing four confident NOT FOUND lines that were all wrong — all four existed, correctly archived. Two compounding probe errors: relative paths across three repositories with only one searched, and zsh's non-word-splitting of unquoted parameter expansions causing every search to run against a nonexistent directory. The entry itself notes it is the source of 1.6's (D) clause. governance_rule because the residue beyond the already-codified positive-control requirement proposes documentary verification rules: check what a path is relative to before searching, prefer probes that report what they searched, and apply the same standard to oneself that one writes for agents. Gate 1 should measure clause-by-clause against 1.6's (D) to determine what remains uncodified.

## Entry 254 (proposal 262) — `verification` → `governance_rule`

**Target:** DRAFTING_CYCLE.md

The entry measures grep -F "triggers fired" and grep -F "proven-clone" both exiting 1 against plan_lint.py — both present and faithful, but implemented as regexes rather than literal strings. The false alarm was caught only because option (D) forced reading the actual check bodies. governance_rule because it proposes a documentary verification rule: probe the artifact's representation (regex, table, computed form), not the spec's prose; before recording absence, read the implementation site; the positive control must use the same representation as the target. Extension beside the existing grep -F clause in §2.7.

## Entry 255 (proposal 263) — `drafting` → `governance_rule`

**Target:** DRAFTING_CYCLE.md

The entry measures three instances of a fix breaking its own description: a delimiter fold whose replacement sentence still claimed the removed glyph occurred "exactly once," a cold reader's fix that re-planted the bomb it removed, and a degenerate-case spec claiming "fenced" while the implementation leaves content visible. governance_rule because it proposes documentary post-fold verification rules: re-verify factual claims in the fold's own text after the fold, reference hazardous tokens by description rather than exhibition, and author-verify proposed fixes by the same method that found the defect. Sibling of entries 240/244.

## Entry 256 (proposal 264) — `mechanics` → `governance_rule`

**Target:** PLANNER_TEMPLATE.md

The entry measures a directional insert on a prefix anchor landing on the wrong side (plan 307's E4, 60 chars of a 780-char line), and the same mechanism surviving in mirror image at E6 where mis-landing splits the anchor line while every mandated check passes on the split. governance_rule because it proposes new documentary rules about edit mechanics: anchor directional inserts on complete lines, sweep for mirror-form defects after fixing one site, add a check spanning the damage point. A new rule in the edit-mechanics area of PLANNER_TEMPLATE.md.

## Entry 257 (proposal 265) — `mechanics` → `governance_rule`

**Target:** PLANNER_TEMPLATE.md

The entry measures that git add followed by a bare git commit commits the entire index, not just the added path — so pre-staged entries silently ride into the commit, and every content check passes because it scopes to the intended path. governance_rule because it proposes a new documentary rule about commit scoping: use the pathspec on the COMMIT (git commit -m "..." -- <path>), pair with a post-commit assertion (git show --name-only), and note that scoping the precondition does not scope the commit. This rule is codified nowhere currently.

## Entry 258 (proposal 266) — `instrumentation` → `governance_rule`

**Target:** PLANNER_TEMPLATE.md

The entry measures that shipped code cites doctrine by line number (§2.6 :75), creating a hard coupling that any doc edit changing line counts above the cited line silently breaks. governance_rule because it proposes new documentary rules about doc-edit constraints: grep for :NN-style citations before editing, prefer in-place rewrites above cited lines, verify by value not arithmetic (the cited line still says the cited thing), and cite by section anchor or literal when writing new checks. A new rule in the doc-edit area of PLANNER_TEMPLATE.md.

## Entry 259 (proposal 267) — `drafting` → `governance_rule`

**Target:** PLANNER_TEMPLATE.md

The entry measures a parent deposit (diag-300) carrying a directive to a future plan that the landing plan (307) never found because the directive lives in neither the baton nor the decision record — only in the deposit's closing sections. governance_rule because it proposes new documentary rules: sweep source deposits' closing sections for directives when authoring a successor, and give machine-parsed conventions a grep-verifiable check at deposit time. Extension in the Rule 27/58 area of PLANNER_TEMPLATE.md.

## Entry 260 (proposal 268) — `design` → `governance_rule`

**Target:** PLANNER_TEMPLATE.md

The entry measures a threshold clause (the every-row trigger) written at the 100% pole that silently drops the mid-band: most-rows mutations, full-table DELETEs, schema migrations, and multi-table narrow writes all compute differently under the clause, but the record had priced only the poles. governance_rule because it proposes a general authoring principle: construct mid-band cases before shipping any threshold or quantifier clause, price each as caught/dropped-and-accepted/dropped-and-unpriced, and record acceptance in the artifact with a boundary test. The specific T-1/T-2 mid-band is SETTLED (1.5 History, consequence 4) — scoped to the general rule only.

## Entry 261 (proposal 269) — `design` → `governance_rule`

**Target:** PLANNER_TEMPLATE.md

The entry measures plan 307's recovery branch skipping the commit block where DOC_SHA gets pinned, while QA consumes DOC_SHA unconditionally — the exact death-state the branch was built for would reach QA with a missing value. governance_rule because it proposes extending the Rule 56/62 area: when adding a bypass/recovery branch, enumerate every downstream reader of the bypassed block's outputs, scope output requirements by path, and test recovery artifacts against the consumer's checks. Clusters with entry 222.

## Entry 262 (proposal 270) — `verification` → `governance_rule`

**Target:** DRAFTING_CYCLE.md

The entry measures that grep -c counts lines, not occurrences — an in-place tail-extension edit re-applied lands both copies on one line, and every grep -Fc count still prints 1 while wc -l is unchanged. The occurrence form (grep -Fo | wc -l) prints 2/1/0 across doubled/correct/absent, validated by execution. governance_rule because it proposes documentary verification rules: use the occurrence form for intra-line-duplicable content, and validate any instrument against a constructed failure state. Extension beside the count-is-not-value clause in §2.7.

## Entry 263 (proposal 271) — `drafting` → `governance_rule` — CLUSTER (A)

**Target:** DRAFTING_CYCLE.md (routes into the reserved CEO shape decision, baton item 2)

The entry measures the shop's first post-dry-close ACID pass (exec-309) raising 2 findings, both in closing prose written after the final pass ran. The terminal blind spot is structural: a dry confirming pass certifies everything except the paragraph that records it. governance_rule because it proposes a post-close re-read rule — adversarial re-read of just the closing prose against the record above it. This is cluster (A) evidence: the class is evidence for the record-vs-phase-count mechanization candidate within the shape decision. Sibling of entry 244.

## Entry 264 (proposal 272) — `drafting` → `governance_rule`

**Target:** DRAFTING_CYCLE.md

The entry measures a fold citing "(C7)" that meant another plan's C7, while the local C7 was an unrelated premise — the cite pointed at the wrong constraint, and the rule actually applied was ledgered nowhere. governance_rule because it proposes documentary rules for §2.8: foreign constraint and finding ids are always namespaced ("301's C24(a)"), and when a fold applies a rule, verify the rule has a local ledger row. The entry is short (622 chars) but the defect class is precise: unnamespaced foreign ids and unledgered applied rules.

## Entry 265 (proposal 273) — `instrumentation` → `governance_rule`

**Target:** DRAFTING_CYCLE.md

The entry measures exec-309's dry confirming pass recorded in prose rows the closing-check's lens-line regex cannot match, causing the gate to keep WARNing despite an honest dry close. Recording the pass per-lens was simultaneously more accurate and checker-legible. governance_rule because it proposes a documentary rule about record authorship: when a gate misreads an honest record, reword only when the truer statement is also the legible one, and never satisfy a checker with wording the state has not earned. Extension beside the earned-phrasing clause in §3. Sibling of entry 252.

---

## Whole-batch cluster-synthesis UPDATE for Gate 1

### Actual tag counts vs expected

| Tag | Expected | Actual | Match |
|---|---|---|---|
| `planner-discipline` | 19 | 19 | ✓ |
| `verification` | 13 | 13 | ✓ |
| `bellows-integration` | 4 | 4 | ✓ |
| `drafting-cycle` | 4 | 4 | ✓ |
| `drafting` | 4 | 4 | ✓ |
| `instrumentation` | 3 | 3 | ✓ |
| `mechanics` | 2 | 2 | ✓ |
| `design` | 2 | 2 | ✓ |

All 8 tag counts match the plan's expectation exactly.

### Divergence tally across all three tranches

- **Tranche A (Step 2):** 17 agreed, 0 diverged
- **Tranche B (Step 3):** 17 agreed, 0 diverged
- **Tranche C (Step 4):** 17 agreed, 0 diverged
- **Total:** 51 agreed, 0 diverged across all three tranches

### Ambiguous ids

None. All 51 proposals classified as `status='proposed'`, zero `ambiguous`.

### Category distribution

All 51 proposals classified as `governance_rule`. This is consistent with the tag-arm analysis: `planner-discipline` (19) maps directly to `governance_rule`; `bellows-integration` (4) permits `governance_rule` within its arm ({governance_rule, instrumentation}); the six minor tags (28 total) all permit `governance_rule` within their arm ({governance_rule, instrumentation, structural, narrative}). No category divergence from any arm's set.

### Flag-(A)–(F) picture after classification

- **(A) SHAPE-DECISION CLUSTER:** 7 entries (225, 230, 238, 239, 244-half, 250, 251, 263) — all classified with `target_artifact=DRAFTING_CYCLE.md` and the route-into-decision flag in `suggested_action`. No change from the plan's identification.
- **(B) FORWARD-REGISTER CHANNEL CLUSTER:** 4 entries (215, 220, 221, 228) — all classified. The parser halves noted in suggested_action for Rule 46 routing. No change.
- **(C) RULE 46 CANDIDATES:** entries 215, 228, 252 (gate half), 220 (parser half) — all classified with the Rule 46 question noted. No change.
- **(D) PARTIALLY-CODIFIED:** entries 223, 229, 238, 241, 247, 252, 253, 260 — all classified with residue identified in reasoning and suggested_action. No change.
- **(E) CONFORMANCE-ORDERING CLUSTER:** entries 224, 237 — both classified targeting DRAFTING_CYCLE.md §5. No change.
- **(F) PRECEDENT-POOR FIVE:** 24 proposals across `verification` (13), `drafting` (4), `instrumentation` (3), `mechanics` (2), `design` (2) — all classified as `governance_rule` with category-justifying reasons in the disposition lines. `drafting-cycle` (4, two priors) shares the category bound but not the heightened burden. No change to the picture.

No new clusters or flags surfaced during classification.
