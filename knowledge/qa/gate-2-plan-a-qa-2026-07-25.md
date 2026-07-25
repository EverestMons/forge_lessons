# Gate 2 Plan A — QA Report (DRAFTING_CYCLE.md v1.0 → v1.1)

**Date:** 2026-07-25
**Plan:** 278
**Step:** 3 (QA)
**Blueprint:** `knowledge/development/gate-2-plan-a-blueprint-2026-07-25.md` — Output Receipt: Complete
**Dev-log:** `knowledge/development/gate-2-plan-a-dev-2026-07-25.md` — Output Receipt: Complete

---

## Verification Table

| Row | Claim | Status | DB Source | Evidence |
|-----|-------|--------|-----------|----------|
| 0 | Doc integrity — shasum matches Step-2 hash | PASS | n/a | `d8f17394c08d7dc72e550df133baba28ae897f1faf89ab2d5c78ab7efcd111ea` — byte-match against dev-log |
| 0b | Independent diff — only intended hunks, no collateral | PASS | n/a | 7 hunks (M1, E1, E2, E3, E5, E4, M2), no non-ASCII corruption on untouched lines |
| 1 | Version 1.1 on :5, full line intact | PASS | n/a | `**Version:** 1.1 (2026-07-25). Amended only through the Iteration Protocol (§6).` — trailing clause preserved |
| 2 | E1 — sub-question 2.4 in §2.2 Destruction | PASS | n/a | Line 50: `(2.4) **for a diagnostic** (read-only, non-mutating): aim Destruction at the downstream plans the diagnostic's findings authorize — a finding a later plan builds on without re-verification (per T-7 / Rule 27) can license a guard-relaxing or destructive change; does any finding over-claim certainty a downstream plan would act on? The skip-condition ("pure-additive plan touching no existing behaviour") does not license skipping Destruction for a diagnostic — a diagnostic is not pure-additive in effect, because its findings authorize downstream change.` Pre-existing 2.1/2.2/2.3 intact. |
| 3 | E2 — sub-question 5.5 in §2.5 ACID | PASS | n/a | Line 68: `(5.5) **for a diagnostic** (single-step, read-only): Isolation (5.3) is structurally empty (no multi-step schedule to analyze) and Atomicity/Durability degenerate to triviality; aim ACID at the findings as a set — do two findings contradict (Consistency), and is the findings artifact enough to reconstruct the diagnostic's basis for a later author (Durability as record)?` Pre-existing 5.1/5.2/5.3/5.4 intact. |
| 4 | E3 — §2.7 sequential-fold (no-batch) bullet | PASS | n/a | Line 82: `- **Sequential-fold rule (extends §2.7 "Parallelism" and §2.6 "cumulation lives in the draft").** Run each lens against the draft **as folded by all prior lenses in this walk** — never analyze all lenses against one draft and batch the folds (a batched fork is never seen by the later lenses). The rationalization "this pass is just confirmation, so cumulation doesn't matter here" is a self-check target: it is the same false reasoning that applies to an expected-dry confirming walk (you do not know it is dry until you have run it lens-by-lens).` Cross-references :79/:73 as EXTENSION, does not restate/contradict. |
| 5 | E4 — §4 closing-check describes shipped last-lens-line check | PASS | n/a | Line 126: `- the check finds the **last lens result line** (the last `- <Lens>: …` line in the Drafting Cycle block before the `**Closing:**` line) and reads its whole-line status: it WARNs iff that line contains a fold-token (`fold`) but not `dry` — reading the structured last lens line, not keyword-matching the closing prose. The closing-line prose check is retained only as a legacy fallback when no structured lens line is parseable.` Old wording GONE (grep count=0). Cross-checked against `git -C /Users/marklehn/Developer/GitHub/bellows show HEAD:scripts/plan_lint.py`: shipped code matches (lens_line_re, region before Closing, whole-line has_fold/has_dry, fallback to prose). No "segment-after-`;`" mechanism described. |
| 6 | E5 — collapsed T0 acceptance (case (b): folded into cycle_tier bullet) | PASS | n/a | Line 123: `(the collapsed T0 form — **cycle_tier:** T0 (no trigger); … — is also accepted; the parser matches word-boundary, not end-of-string)`. SA flagged case (b) in blueprint. §3 T0 example UNCHANGED at :115 (original :114, shifted +1 by E3 insertion). |
| 7 | Count phrases at :29/:73/:124 intact, all "five" | PASS | n/a | :29 "full five-lens walk", :73 "five lenses **cold**", :124 "all five for T1/T2" — all unaltered |
| 8 | Changelog row M2 for v1.1 | PASS | n/a | Line 157: names four proposals (187–190), units changed, Plan-B pairing (277, bellows), lens-count-stays-five. v1.0 row intact at :158, not rewritten. |
| 9 | 187–190 → implemented | PASS | `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` | `187\|implemented\|2026-07-25 21:26:20\|ceo`, `188\|implemented\|2026-07-25 21:26:20\|ceo`, `189\|implemented\|2026-07-25 21:26:20\|ceo`, `190\|implemented\|2026-07-25 21:26:20\|ceo` — byte-match against Step-2 dev-log block |
| 10 | Corpus totals: proposed=0 | PASS | `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` | `implemented\|137, reference\|7, rejected\|15, stale\|3, superseded\|28` — no `proposed` row (count=0) |
| 11 | No src/ change, no schema drift | PASS | n/a | `git status --porcelain -- src/` → empty (own working tree) |

All rows PASS.

---

## Rule 20 — QA Self-Check

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/278/knowledge/qa/evidence/gate-2-plan-a-2026-07-25/
Files verified: 2
```

Self-grep confirmation:
```
$ grep 'Rule 20 — QA Self-Check Results' knowledge/qa/gate-2-plan-a-qa-2026-07-25.md
Rule 20 — QA Self-Check Results
```

---

## Output Receipt

| Field | Value |
|-------|-------|
| Plan | 278 — Gate 2 Plan A |
| Step | 3 (QA) |
| Status | **Complete** |
| Blueprint | `knowledge/development/gate-2-plan-a-blueprint-2026-07-25.md` — Complete |
| Dev-log | `knowledge/development/gate-2-plan-a-dev-2026-07-25.md` — Complete |
| Verification rows | 0, 0b, 1–11 — all PASS |
| Doc hash confirmed | `d8f17394c08d7dc72e550df133baba28ae897f1faf89ab2d5c78ab7efcd111ea` — matches Step-2 |
| DB status confirmed | 187–190 → `implemented`, `status_updated_by='ceo'` |
| proposed count | **0** |
| Evidence files | `db-invariants.txt`, `doc-integrity.txt` |

### Ledger Updates

#### Project Status

Gate 2 Plan A complete — DRAFTING_CYCLE.md **v1.1**, proposals 187–190 implemented. The two diagnostic-mode sub-questions (2.4 in §2.2 Destruction, 5.5 in §2.5 ACID), the §2.7 sequential-fold rule, and the §4 last-lens-line closing check + collapsed-T0 acceptance are now codified. The lens count deliberately stays five. `proposed` is now 0 — the four were the last proposed entries. The DRAFTING_CYCLE.md hardening arc is COMPLETE.

#### Prompt Feedback

- The plan's instruction to cross-check E4's doc text against the shipped `plan_lint.py` code (Row 5) was load-bearing — it verifies the doc describes the ACTUAL mechanism, not the superseded edit-map design.
- The E5 three-case structure (standalone / folded / SA-omitted) made QA row 6 mechanical: identify which case the SA chose, then verify accordingly.
- The "own working tree" instruction for Row 11 (`git status --porcelain -- src/`) correctly avoids the vacuous `-C <main>` trap on a worktree run.
- The evidence-file structure (db-invariants.txt for rows 9–10, doc-integrity.txt for rows 0/0b/1–8) cleanly maps the Rule 20 block's required_evidence_files to the verification rows.
