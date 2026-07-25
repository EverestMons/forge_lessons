# Gate 2 Plan A — SA Blueprint (DRAFTING_CYCLE.md v1.0 → v1.1)

**Date:** 2026-07-25
**Plan:** 278
**Step:** 1 (SA)
**Proposals:** 187, 188, 189, 190 — all confirmed `proposed`/`codify` via DB join

---

## Pinned Commits

- **Governance root HEAD:** `006e8e2effb0743c1cc0e5b1eff842f464565cf6`
- **DRAFTING_CYCLE.md last-touching commit:** `2502159371ba4be7c4a00a25b330abdb0344ddc6`

DEV re-checks the latter before applying (A0).

---

## Dedup Greps (each against live v1.0 DRAFTING_CYCLE.md)

| Edit | Grep | Count | Result |
|------|------|-------|--------|
| E1 | `(2.4)` literal | 0 | No existing 2.4 sub-question |
| E2 | `(5.5)` literal | 0 | No existing 5.5 sub-question |
| E3 | `no.batch\|as.folded\|sequential.fold` | 1 (at :89 in §2.8, "sequential folding" in conflict resolution — NOT §2.7) | No competing no-batch clause in §2.7 |
| E4 | `last lens line\|last.lens.line` | 0 | No existing last-lens-line wording |
| E5 | `collapsed.*T0\|T0.*collapsed` | 0 | No existing collapsed-T0 note in §4 |

---

## Count-Phrase Confirmation (three phrases, all "five", no edit touches them)

| Line | Phrase | Confirmed |
|------|--------|-----------|
| :29 | "run the **full five-lens walk** (§2.1–§2.5)" | ✓ present, reads "five" |
| :73 | "run the five lenses **cold**" | ✓ present, reads "five" |
| :123 | "one result line per **required** lens (all five for T1/T2, ACID included)" | ✓ present, reads "five" |

No edit in this blueprint touches lines 29, 73, or 123. 2.4 and 5.5 are sub-questions of existing lenses 2 and 5, not new lenses.

---

## Anti-Watering-Down Gate (E3, Destruction w1; pinned per Rule 57)

### :79 verbatim
`- **Parallelism within a lens, never across.** Concurrent readers feeding one fold is fine; concurrent *lenses* sever cumulation (that is a panel pass — label it).`

### :73 verbatim
`After the sequential walk goes dry, rotate the **reviewer**, not the lens: run the five lenses **cold** — fresh-context readers given only the artifact plus repo read access, **sequentially** (a concurrent cold run is a panel pass, not a walk — cumulation lives in the draft, so sequential preserves it). Author-verify cold findings; a cold reader can misread deliberate design as a defect.`

### (a)/(b) criteria — BOTH confirmed present in E3

**(a) AS-FOLDED sequencing of the folds:** E3 states "Run each lens against the draft **as folded by all prior lenses in this walk** — never analyze all lenses against one draft and batch the folds." This is DISTINCT from :79, which forbids concurrent lens *execution*. The batch failure E3 addresses is different: lenses can run one at a time (sequential, satisfying :79) but each read the SAME un-folded draft — sequential execution with batched analysis. :79 doesn't catch it because the lenses aren't concurrent; :73 states the principle ("cumulation lives in the draft") but doesn't make the prohibition explicit.

**(b) Named rationalization as self-check target:** E3 states '"this pass is just confirmation, so cumulation doesn't matter here" is a self-check target.' This rationalization is ABSENT from both :79 and :73. Neither line names a specific false reasoning pattern to watch for.

**Gate PASSES** — E3 carries both (a) and (b); it is an extension, not a restatement or competitor.

---

## E5 SA Choice (flagged for QA)

E5 (190/N6, collapsed T0 acceptance) is folded into §4 as an extension of the existing `cycle_tier` declaration bullet (line 122), NOT as a standalone note. Rationale: the T0 acceptance is about the tier declaration parser (the same feature the existing bullet describes), so extending that bullet is the most natural placement. §3's T0 example at :114 is left UNCHANGED — Plan B's `\b` regex already makes it pass. **QA row 6 evaluates this as case (b): folded into the cycle_tier bullet.**

---

## Edit Blueprint — Five Doc Edits + Two Mechanical Edits

### E1 — §2.2 Destruction: append sub-question 2.4 (187/N1)

**Type:** INSERTION — append inline to the end of the existing `**Sub-questions:**` line in §2.2 (line 50), before the `**Evidence:**` line. Extends the single line, NOT a new bullet.

**Anchor (unique, grep count=1):** `is any destructive operation's blast radius bounded and proven *ours* before it runs?`

**Appended text (including the leading space before the parenthetical):**
```
 (2.4) **for a diagnostic** (read-only, non-mutating): aim Destruction at the downstream plans the diagnostic's findings authorize — a finding a later plan builds on without re-verification (per T-7 / Rule 27) can license a guard-relaxing or destructive change; does any finding over-claim certainty a downstream plan would act on? The skip-condition ("pure-additive plan touching no existing behaviour") does not license skipping Destruction for a diagnostic — a diagnostic is not pure-additive in effect, because its findings authorize downstream change.
```

**After E1, the full Sub-questions line reads:** `- **Sub-questions:** (2.1) what breaks if this ships? (2.2) does any step relax an existing guard, threshold, or assertion? (2.3) is any destructive operation's blast radius bounded and proven *ours* before it runs? (2.4) **for a diagnostic** (read-only, non-mutating): aim Destruction at the downstream plans the diagnostic's findings authorize — a finding a later plan builds on without re-verification (per T-7 / Rule 27) can license a guard-relaxing or destructive change; does any finding over-claim certainty a downstream plan would act on? The skip-condition ("pure-additive plan touching no existing behaviour") does not license skipping Destruction for a diagnostic — a diagnostic is not pure-additive in effect, because its findings authorize downstream change.`

---

### E2 — §2.5 ACID: append sub-question 5.5 (187/N2–N3)

**Type:** INSERTION — append inline to the end of the existing `**Sub-questions:**` line in §2.5 (line 68), before the `**Evidence:**` line. Extends the single line, NOT a new bullet.

**Anchor (unique, grep count=1):** `is the surviving record enough to reconstruct what happened?`

**Appended text (including the leading space before the parenthetical):**
```
 (5.5) **for a diagnostic** (single-step, read-only): Isolation (5.3) is structurally empty (no multi-step schedule to analyze) and Atomicity/Durability degenerate to triviality; aim ACID at the findings as a set — do two findings contradict (Consistency), and is the findings artifact enough to reconstruct the diagnostic's basis for a later author (Durability as record)?
```

**After E2, the full Sub-questions line reads:** `- **Sub-questions:** (5.1) **Atomicity** — the state set if this half-completes; is every member acceptable? (5.2) **Consistency** — which invariant closes each gap, and is it stated or accidental? (5.3) **Isolation** — for a multi-step schedule (steps separated by verdict gates of arbitrary wall-clock time over shared stores), enumerate each step's reads/writes; find the between-step windows where a concurrent actor can interleave a conflicting R-W / W-R / W-W; require an explicit guard (pin, byte-match, locked txn) per window. (5.4) **Durability** — what survives a crash, and is the surviving record enough to reconstruct what happened? (5.5) **for a diagnostic** (single-step, read-only): Isolation (5.3) is structurally empty (no multi-step schedule to analyze) and Atomicity/Durability degenerate to triviality; aim ACID at the findings as a set — do two findings contradict (Consistency), and is the findings artifact enough to reconstruct the diagnostic's basis for a later author (Durability as record)?`

---

### E3 — §2.7 Cross-cutting rules: new sequential-fold bullet (188/N4)

**Type:** INSERTION — new bullet appended after the last existing bullet in §2.7 (line 81, "Sketch one real block…"). New line after line 81.

**Anchor (unique, grep count=1):** `Sketch one real block.`

**New bullet (full line):**
```
- **Sequential-fold rule (extends §2.7 "Parallelism" and §2.6 "cumulation lives in the draft").** Run each lens against the draft **as folded by all prior lenses in this walk** — never analyze all lenses against one draft and batch the folds (a batched fork is never seen by the later lenses). The rationalization "this pass is just confirmation, so cumulation doesn't matter here" is a self-check target: it is the same false reasoning that applies to an expected-dry confirming walk (you do not know it is dry until you have run it lens-by-lens).
```

---

### E4 — §4 Self-Check: replace closing-check bullet (189/N5)

**Type:** REPLACEMENT — replace the entire line 125.

**Anchor (unique, grep count=1):** `the **closing** line asserts a dry lens pass as the last event (not a fold).`

**Old text:**
```
- the **closing** line asserts a dry lens pass as the last event (not a fold).
```

**New text:**
```
- the check finds the **last lens result line** (the last `- <Lens>: …` line in the Drafting Cycle block before the `**Closing:**` line) and reads its whole-line status: it WARNs iff that line contains a fold-token (`fold`) but not `dry` — reading the structured last lens line, not keyword-matching the closing prose. The closing-line prose check is retained only as a legacy fallback when no structured lens line is parseable.
```

**Authored from shipped code:** `git -C /Users/marklehn/Developer/GitHub/bellows show HEAD:scripts/plan_lint.py` — the shipped mechanism (plan_lint.py lines ~184–202 of the show output): (1) `lens_line_re` matches `^- <Lens>:` lines; (2) iterates the region before `**Closing:**` to find the LAST matching line; (3) checks the whole line: `has_fold = 'fold' in ll_lower` and `has_dry = 'dry' in ll_lower`; WARNs iff `has_fold and not has_dry`; (4) falls back to the closing-line prose heuristic only when `last_lens_line is None`. The E4 text describes this shipped whole-line mechanism, NOT the superseded "segment-after-`;`" design from the edit map's Q2.

---

### E5 — §4 Self-Check: collapsed T0 acceptance (190/N6) — folded into cycle_tier bullet

**Type:** REPLACEMENT — extend the existing `cycle_tier` declaration bullet (line 122).

**Anchor (unique, grep count=1):** `the plan header declares \`**cycle_tier:** T{0,1,2}\``

**Old text:**
```
- the plan header declares `**cycle_tier:** T{0,1,2}`;
```

**New text:**
```
- the plan header declares `**cycle_tier:** T{0,1,2}` (the collapsed T0 form — `**cycle_tier:** T0 (no trigger); …` — is also accepted; the parser matches word-boundary, not end-of-string);
```

**SA choice:** E5 folded into the cycle_tier bullet rather than a standalone note (flagged for QA — row 6 case (b)). §3's T0 example at :114 is UNCHANGED.

---

### M1 — Version bump (surgical date-swap at :5)

**Type:** REPLACEMENT — replace ONLY the version+date substring, NOT the whole line. The trailing `. Amended only through the Iteration Protocol (§6).` is PRESERVED by scoping the replacement to the anchor substring.

**Anchor (unique, grep count=1 for `**Version:** 1.0 (2026-07-23)`):**
```
**Version:** 1.0 (2026-07-23)
```

**Old text:** `**Version:** 1.0 (2026-07-23)`
**New text:** `**Version:** 1.1 (2026-07-25)`

**After M1, full line 5 reads:** `**Version:** 1.1 (2026-07-25). Amended only through the Iteration Protocol (§6).`

---

### M2 — Changelog row (append after 1.0 row at :156)

**Type:** INSERTION — new line appended after the existing 1.0 History row (line 156). The 1.0 row is NEVER rewritten.

**Anchor (unique, grep count=1):** `- **1.0 (2026-07-23):**`

**New row (full line):**
```
- **1.1 (2026-07-25):** Codified proposals 187–190. §2.2: sub-question 2.4 (diagnostic-mode Destruction residue — aim the lens at downstream plans the diagnostic's findings authorize; the skip-condition does not license skipping Destruction for a diagnostic). §2.5: sub-question 5.5 (diagnostic-mode ACID residue — for a single-step read-only plan, aim ACID at the findings as a set). §2.7: sequential-fold rule (explicit no-batch clause extending the existing cumulation principles at §2.7 "Parallelism" and §2.6 "cumulation lives in the draft"). §4: closing check now reads the last lens result line's whole-line status, not the closing prose; collapsed T0 header form accepted. Paired with Plan B (277, bellows) which shipped the corresponding `plan_lint.py` edits for 189/N5 (last-lens-line check) and 190/N6 (`^T([012])\b` regex). **The lens count deliberately stays five** — 2.4 and 5.5 are sub-questions of existing lenses 2 and 5, not new lenses.
```

---

## Edit Application Order for DEV

1. **M1** — version bump (`:5`), so even an early death leaves `1.1` for A0's anchor test
2. **E1** — §2.2 sub-question 2.4
3. **E2** — §2.5 sub-question 5.5
4. **E3** — §2.7 sequential-fold bullet
5. **E5** — §4 cycle_tier bullet extension (before E4 since both are in §4; E5 is on :122, E4 is on :125)
6. **E4** — §4 closing-check replacement
7. **M2** — changelog row (last, since it summarizes what was added)

---

## Output Receipt

| Field | Value |
|-------|-------|
| Plan | 278 — Gate 2 Plan A |
| Step | 1 (SA) |
| Status | **Complete** |
| Proposals read | 187, 188, 189, 190 — all `proposed`/`codify` (4 rows, DB join confirmed) |
| Edit map source | `governance/knowledge/research/gate2-architecture-edit-map-2026-07-25.md` (diag-276) |
| Shipped code source | `git -C /Users/marklehn/Developer/GitHub/bellows show HEAD:scripts/plan_lint.py` |
| Governance root HEAD | `006e8e2effb0743c1cc0e5b1eff842f464565cf6` |
| Doc last-touching commit | `2502159371ba4be7c4a00a25b330abdb0344ddc6` |
| Edits blueprinted | E1, E2, E3, E4, E5 (folded into cycle_tier bullet), M1, M2 |
| Count phrases confirmed | :29 "five-lens walk", :73 "five lenses cold", :123 "all five" — all intact, no edit touches them |
| Anti-watering-down gate | PASSED — E3 carries both (a) AS-FOLDED sequencing and (b) named rationalization; distinct from :79/:73 |
| Dedup greps | All 5 clear — no pre-existing substance for any edit |
| Anchors | All 7 unique (grep count=1 each) |

### Ledger Updates

#### Prompt Feedback

- The plan's instruction to read proposals by DB join with `p.status`/`p.route` in the projection (Cold-panel F1) was well-designed — the confirmation is performable from the query output, not asserted.
- The anti-watering-down gate's (a)/(b) criteria (pinned per Rule 57) made the E3 distinctness test mechanical: (a) tests for AS-FOLDED sequencing of folds (distinct from :79's concurrent-execution prohibition), (b) tests for the named rationalization (absent from both :79 and :73). Without these criteria, "distinct from existing rules" would be a freehand judgment.
- The E4 instruction to read from `git show HEAD:scripts/plan_lint.py` rather than the working tree was load-bearing — it pins the doc text to the SHIPPED code, not an in-progress edit.
- The M1 "surgical date-swap" instruction (Cold-panel D-F1) prevented a whole-line replacement that would have required reproducing the trailing "Amended only through the Iteration Protocol (§6)." clause — scoping the anchor to the version+date substring makes the replacement safe.
