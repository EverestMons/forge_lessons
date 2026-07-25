# Gate 2 Plan A — DEV Log (DRAFTING_CYCLE.md v1.0 → v1.1)

**Date:** 2026-07-25
**Plan:** 278
**Step:** 2 (DEV)
**Blueprint:** `knowledge/development/gate-2-plan-a-blueprint-2026-07-25.md` — Output Receipt: Complete

---

## Task A0 — Pre-edit Cleanliness Gate

- `git -C /Users/marklehn/Developer/GitHub status --short -- DRAFTING_CYCLE.md` → **empty** (clean)
- Last-touching commit: `2502159371ba4be7c4a00a25b330abdb0344ddc6` — **matches blueprint pin**
- No resume disambiguation needed (clean tree, matching commit)

---

## Task A — M1 Version Bump

Surgical date-swap at :5: `**Version:** 1.0 (2026-07-23)` → `**Version:** 1.1 (2026-07-25)`

**Trailing clause confirmation (D-F1):**
```
5:**Version:** 1.1 (2026-07-25). Amended only through the Iteration Protocol (§6).
```
Full line intact — "Amended only through the Iteration Protocol (§6)." preserved.

---

## Task B — Doc Edits E1–E5

### E1 — §2.2 sub-question 2.4 (187/N1)

Appended inline to §2.2's Sub-questions line. Grep confirmation:
```
$ grep -c '(2.4)' DRAFTING_CYCLE.md
1
$ grep -n '(2.4)' DRAFTING_CYCLE.md
50:- **Sub-questions:** (2.1) what breaks if this ships? (2.2) does any step relax an existing guard, threshold, or assertion? (2.3) is any destructive operation's blast radius bounded and proven *ours* before it runs? (2.4) **for a diagnostic** (read-only, non-mutating): aim Destruction at the downstream plans the diagnostic's findings authorize — a finding a later plan builds on without re-verification (per T-7 / Rule 27) can license a guard-relaxing or destructive change; does any finding over-claim certainty a downstream plan would act on? The skip-condition ("pure-additive plan touching no existing behaviour") does not license skipping Destruction for a diagnostic — a diagnostic is not pure-additive in effect, because its findings authorize downstream change.
```
Located on line 50 in §2.2, before Evidence line. Inline on the Sub-questions line (not a standalone bullet). ✓

### E2 — §2.5 sub-question 5.5 (187/N2–N3)

Appended inline to §2.5's Sub-questions line. Grep confirmation:
```
$ grep -c '(5.5)' DRAFTING_CYCLE.md
1
$ grep -n '(5.5)' DRAFTING_CYCLE.md
68:- **Sub-questions:** (5.1) **Atomicity** — ... (5.4) **Durability** — ... is the surviving record enough to reconstruct what happened? (5.5) **for a diagnostic** (single-step, read-only): Isolation (5.3) is structurally empty (no multi-step schedule to analyze) and Atomicity/Durability degenerate to triviality; aim ACID at the findings as a set — do two findings contradict (Consistency), and is the findings artifact enough to reconstruct the diagnostic's basis for a later author (Durability as record)?
```
Located on line 68 in §2.5, before Evidence line. Inline on the Sub-questions line. ✓

### E3 — §2.7 sequential-fold bullet (188/N4)

New bullet appended after "Sketch one real block." Grep confirmation:
```
$ grep -n 'Sequential-fold rule' DRAFTING_CYCLE.md
82:- **Sequential-fold rule (extends §2.7 "Parallelism" and §2.6 "cumulation lives in the draft").** Run each lens against the draft **as folded by all prior lenses in this walk** — never analyze all lenses against one draft and batch the folds (a batched fork is never seen by the later lenses). The rationalization "this pass is just confirmation, so cumulation doesn't matter here" is a self-check target: it is the same false reasoning that applies to an expected-dry confirming walk (you do not know it is dry until you have run it lens-by-lens).
```
Located on line 82, inside §2.7, after "Sketch one real block" (line 81). ✓

### E5 — §4 cycle_tier bullet extension (190/N6, folded into cycle_tier per blueprint)

Extended the cycle_tier bullet. Grep confirmation:
```
$ grep -n 'collapsed T0' DRAFTING_CYCLE.md
123:- the plan header declares `**cycle_tier:** T{0,1,2}` (the collapsed T0 form — `**cycle_tier:** T0 (no trigger); …` — is also accepted; the parser matches word-boundary, not end-of-string);
```
Located on line 123 in §4. ✓

### E4 — §4 closing-check replacement (189/N5)

Replaced the old closing-check bullet with last-lens-line text. Grep confirmations:
```
$ grep -n 'last lens result line' DRAFTING_CYCLE.md
126:- the check finds the **last lens result line** (the last `- <Lens>: …` line in the Drafting Cycle block before the `**Closing:**` line) and reads its whole-line status: it WARNs iff that line contains a fold-token (`fold`) but not `dry` — reading the structured last lens line, not keyword-matching the closing prose. The closing-line prose check is retained only as a legacy fallback when no structured lens line is parseable.
$ grep -c 'the \*\*closing\*\* line asserts' DRAFTING_CYCLE.md
0
```
New text on line 126 in §4. Old wording gone (count=0). ✓

---

## Task B2 — M2 Changelog Row

New v1.1 row appended after 1.0 row:
```
$ grep -n '1\.1 (2026-07-25):' DRAFTING_CYCLE.md
157:- **1.1 (2026-07-25):** Codified proposals 187–190. §2.2: sub-question 2.4 ...
$ grep -n '1\.0 (2026-07-23):' DRAFTING_CYCLE.md
158:- **1.0 (2026-07-23):** Extracted and restructured from ...
```
v1.1 row on line 157, v1.0 row intact on line 158 (never rewritten). ✓

---

## Task B3 — Count Guard

All three count phrases confirmed intact and reading "five":

```
$ grep -n 'full five-lens walk' DRAFTING_CYCLE.md
29:- **T1 — Standard cycle.** Any of T-1, T-3, T-4, T-7, T-8 fires → run the **full five-lens walk** (§2.1–§2.5).
$ grep -n 'five lenses \*\*cold\*\*' DRAFTING_CYCLE.md
73:After the sequential walk goes dry, rotate the **reviewer**, not the lens: run the five lenses **cold** — ...
$ grep -n 'all five for T1/T2' DRAFTING_CYCLE.md
124:- for **T1+**: a `## Drafting Cycle` block is present, with one result line per **required** lens (all five for T1/T2, ACID included);
```
Lines 29, 73, 124 — all unaltered, all read "five". ✓

---

## Task B4 — Diff-Is-Only-Intended-Hunks

Full diff (7 hunks, all intended — M1, E1, E2, E3, E5, E4, M2):

```diff
diff --git a/DRAFTING_CYCLE.md b/DRAFTING_CYCLE.md
index 77ed74d..6b145f1 100644
--- a/DRAFTING_CYCLE.md
+++ b/DRAFTING_CYCLE.md
@@ -2,7 +2,7 @@
 
 **Single source of truth.** This file publishes the Drafting Cycle: the adversarial pre-deposit analysis every orchestration plan passes through. `PLANNER_TEMPLATE.md`'s `## The Drafting Cycle` section references this file and does not restate it. Modelled on `RULE_20_SELF_CHECK_BLOCK.md` and `READONLY_AUDIT_CONTRACT.md` — one canonical location, referenced not inlined.
 
-**Version:** 1.0 (2026-07-23). Amended only through the Iteration Protocol (§6).
+**Version:** 1.1 (2026-07-25). Amended only through the Iteration Protocol (§6).
 
 **The two-layer contract this belongs to.** The Drafting Cycle hardens the **plan** *before* deposit. Planner verification at the verdict gate hardens the **deliverable** *after* each step. Both are required; neither substitutes for the other. Leaning on the second to catch what the first should is a known failure mode — the 216→217 boundary established the distinction. This file codifies the first layer as a mechanical system: **compute the tier (§1) → run the lenses that tier requires (§2) → record the Cycle Log (§3) → the self-check enforces it (§4).**
 
@@ -47,7 +47,7 @@ Each lens states its **core question**, its **standing sub-questions** (numbered
 
 ### 2.2 Lens 2 — Destruction / mitigating rewrites
 - **Core:** what existing functionality could this harm, and where might an agent water down a constant, contract, or invariant?
-- **Sub-questions:** (2.1) what breaks if this ships? (2.2) does any step relax an existing guard, threshold, or assertion? (2.3) is any destructive operation's blast radius bounded and proven *ours* before it runs?
+- **Sub-questions:** (2.1) what breaks if this ships? (2.2) does any step relax an existing guard, threshold, or assertion? (2.3) is any destructive operation's blast radius bounded and proven *ours* before it runs? (2.4) **for a diagnostic** (read-only, non-mutating): aim Destruction at the downstream plans the diagnostic's findings authorize — a finding a later plan builds on without re-verification (per T-7 / Rule 27) can license a guard-relaxing or destructive change; does any finding over-claim certainty a downstream plan would act on? The skip-condition ("pure-additive plan touching no existing behaviour") does not license skipping Destruction for a diagnostic — a diagnostic is not pure-additive in effect, because its findings authorize downstream change.
 - **Evidence:** the harm surface + the mitigation folded in.
 - **Skip:** only a pure-additive plan touching no existing behaviour — and state why.
 
@@ -65,7 +65,7 @@ Each lens states its **core question**, its **standing sub-questions** (numbered
 
 ### 2.5 Lens 5 — ACID (runs last)
 - **Core:** examine the plan's accepted requirements **as a system** — do any conflict, and which properties are stated vs merely lucky?
-- **Sub-questions:** (5.1) **Atomicity** — the state set if this half-completes; is every member acceptable? (5.2) **Consistency** — which invariant closes each gap, and is it stated or accidental? (5.3) **Isolation** — for a multi-step schedule (steps separated by verdict gates of arbitrary wall-clock time over shared stores), enumerate each step's reads/writes; find the between-step windows where a concurrent actor can interleave a conflicting R-W / W-R / W-W; require an explicit guard (pin, byte-match, locked txn) per window. (5.4) **Durability** — what survives a crash, and is the surviving record enough to reconstruct what happened?
+- **Sub-questions:** (5.1) **Atomicity** — the state set if this half-completes; is every member acceptable? (5.2) **Consistency** — which invariant closes each gap, and is it stated or accidental? (5.3) **Isolation** — for a multi-step schedule (steps separated by verdict gates of arbitrary wall-clock time over shared stores), enumerate each step's reads/writes; find the between-step windows where a concurrent actor can interleave a conflicting R-W / W-R / W-W; require an explicit guard (pin, byte-match, locked txn) per window. (5.4) **Durability** — what survives a crash, and is the surviving record enough to reconstruct what happened? (5.5) **for a diagnostic** (single-step, read-only): Isolation (5.3) is structurally empty (no multi-step schedule to analyze) and Atomicity/Durability degenerate to triviality; aim ACID at the findings as a set — do two findings contradict (Consistency), and is the findings artifact enough to reconstruct the diagnostic's basis for a later author (Durability as record)?
 - **Evidence:** the schedule + any contradiction between earlier-folded requirements.
 - **Skip:** T0 only.
 
@@ -79,6 +79,7 @@ After the sequential walk goes dry, rotate the **reviewer**, not the lens: run t
 - **Parallelism within a lens, never across.** Concurrent readers feeding one fold is fine; concurrent *lenses* sever cumulation (that is a panel pass — label it).
 - **Extraction contract.** Before splitting shared content, diff the regions and move only byte-identical clauses; state what moves, what stays, how it is retrieved, and what the retrieval promises.
 - **Sketch one real block.** Before deposit, draw the actual rows / cells a single item produces and confirm the mandated format holds everything the plan requires per item.
+- **Sequential-fold rule (extends §2.7 "Parallelism" and §2.6 "cumulation lives in the draft").** Run each lens against the draft **as folded by all prior lenses in this walk** — never analyze all lenses against one draft and batch the folds (a batched fork is never seen by the later lenses). The rationalization "this pass is just confirmation, so cumulation doesn't matter here" is a self-check target: it is the same false reasoning that applies to an expected-dry confirming walk (you do not know it is dry until you have run it lens-by-lens).
 
 ### 2.8 Conflict Ledger (keeps cross-lens folds from oscillating)
 
@@ -119,10 +120,10 @@ For **T0** the block collapses to a single line in the header context: `**cycle_
 
 `bellows/scripts/plan_lint.py` gains a Drafting-Cycle check that runs at deposit and reports on the structure below:
 
-- the plan header declares `**cycle_tier:** T{0,1,2}`;
+- the plan header declares `**cycle_tier:** T{0,1,2}` (the collapsed T0 form — `**cycle_tier:** T0 (no trigger); …` — is also accepted; the parser matches word-boundary, not end-of-string);
 - for **T1+**: a `## Drafting Cycle` block is present, with one result line per **required** lens (all five for T1/T2, ACID included);
 - for **T2**: a cold-panel line is present;
-- the **closing** line asserts a dry lens pass as the last event (not a fold).
+- the check finds the **last lens result line** (the last `- <Lens>: …` line in the Drafting Cycle block before the `**Closing:**` line) and reads its whole-line status: it WARNs iff that line contains a fold-token (`fold`) but not `dry` — reading the structured last lens line, not keyword-matching the closing prose. The closing-line prose check is retained only as a legacy fallback when no structured lens line is parseable.
 
 **Landing posture — warn-first (deliberate).** The check lands as a **warning**: it names a missing tier declaration, block, required-lens line, or a closing fold, but does **not** block the deposit. It flips to blocking only after a short break-in period, once the log format is proven on real plans — establishing the baseline first and adding teeth where we've learned they belong, rather than asserting hard enforcement up front. The self-check never gates on the Conflict Ledger (§2.8) — a plan with no cross-lens conflict has nothing to log.
 
@@ -153,4 +154,5 @@ This file is the **base**; lessons refine it without rewriting it.
 - Keep the `plan_lint` self-check (§4) in lockstep with §1/§3 — the gate's tests are part of the change.
 
 ## History
+- **1.1 (2026-07-25):** Codified proposals 187–190. §2.2: sub-question 2.4 (diagnostic-mode Destruction residue — aim the lens at downstream plans the diagnostic's findings authorize; the skip-condition does not license skipping Destruction for a diagnostic). §2.5: sub-question 5.5 (diagnostic-mode ACID residue — for a single-step read-only plan, aim ACID at the findings as a set). §2.7: sequential-fold rule (explicit no-batch clause extending the existing cumulation principles at §2.7 "Parallelism" and §2.6 "cumulation lives in the draft"). §4: closing check now reads the last lens result line's whole-line status, not the closing prose; collapsed T0 header form accepted. Paired with Plan B (277, bellows) which shipped the corresponding `plan_lint.py` edits for 189/N5 (last-lens-line check) and 190/N6 (`^T([012])\b` regex). **The lens count deliberately stays five** — 2.4 and 5.5 are sub-questions of existing lenses 2 and 5, not new lenses.
 - **1.0 (2026-07-23):** Extracted and restructured from `PLANNER_TEMPLATE.md §The Drafting Cycle` (v4.79) into a mechanical system — the Rigor-Tier Gate (§1), the Lens Register with numbered sub-questions (§2), the compact Cycle Log (§3), and the `plan_lint` self-check (§4). Motivated by a session in which the doctrine ran at the floor and under-escalated on CEO-run-tool plans; the verdict-gate layer caught the deliverable defects but the plan-hardening layer had no teeth. Sub-questions 3.1 / 3.2 / 3.3 and 4.4 encode that session's lessons (cp1252 target environment; observe-the-effect; from-import isolation; domain-premise correction). The Conflict Ledger (§2.8) addresses the non-converging-draft-count problem (plan 239's "5 → 4 → 5 → 4 → 4"): record each fold's constraint, resolve cross-lens conflicts jointly in one move, escalate genuine contradictions — with persistent oscillation as a judgment signal, NOT a hard draft-count limit. Sub-question 1.4 preserves the diag-229 diagnostic-weak-spots guidance carried over from the v4.79 template section (its one extraction judgment call, resolved by the CEO to keep it). The §4 self-check lands warn-first, flipping to blocking only once the format proves out. **This 1.0 is a baseline to iterate on, not a finished rulebook** — mechanisms and judgment signals now; hard rules added only where real runs show they belong.
```

No collateral changes. All non-ASCII characters (`—`, `→`, `§`, `⭐`) intact on untouched lines. No encoding corruption. ✓

---

## Task C0 — DB Precondition

```
$ sqlite3 "file:/.../lessons-forge.db?mode=ro" "SELECT id, status, route FROM lesson_proposals WHERE id IN (187,188,189,190) ORDER BY id"
187|proposed|codify
188|proposed|codify
189|proposed|codify
190|proposed|codify
```
All four `proposed`/`codify`. ✓

---

## Task C — Status Transition

### Restore Point

- **Method:** `sqlite3 ".backup"` (WAL-safe, per plan-275 pattern)
- **Path:** `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-preA-20260725T212611Z.db`
- **Size:** 851968 bytes (non-zero)
- **Git status:** absent (gitignored via `*.db`)

### UPDATE

```sql
UPDATE lesson_proposals SET status='implemented', status_updated_at=datetime('now'), status_updated_by='ceo' WHERE id IN (187,188,189,190) AND status='proposed';
```
Exit code: 0.

### Post-Task-C Per-ID Read-Back (RAW)

```
$ sqlite3 "file:/.../lessons-forge.db?mode=ro" "SELECT id, status, status_updated_at, status_updated_by FROM lesson_proposals WHERE id IN (187,188,189,190) ORDER BY id"
187|implemented|2026-07-25 21:26:20|ceo
188|implemented|2026-07-25 21:26:20|ceo
189|implemented|2026-07-25 21:26:20|ceo
190|implemented|2026-07-25 21:26:20|ceo
```

### Status Distribution (RAW)

```
$ sqlite3 "file:/.../lessons-forge.db?mode=ro" "SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY status"
implemented|137
reference|7
rejected|15
stale|3
superseded|28
```
`proposed` is now **0** — the four were the last.

---

## Post-Edit Doc Hash

```
$ shasum -a 256 /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md
d8f17394c08d7dc72e550df133baba28ae897f1faf89ab2d5c78ab7efcd111ea  /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md
```

---

## Output Receipt

| Field | Value |
|-------|-------|
| Plan | 278 — Gate 2 Plan A |
| Step | 2 (DEV) |
| Status | **Complete** |
| Blueprint | `knowledge/development/gate-2-plan-a-blueprint-2026-07-25.md` — Complete |
| A0 gate | PASSED — clean tree, last-touching commit matches pin `2502159` |
| Edits applied | M1 (version bump), E1 (2.4), E2 (5.5), E3 (§2.7 bullet), E5 (cycle_tier extension), E4 (closing-check replacement), M2 (changelog row) |
| Count guard (B3) | PASSED — :29/:73/:124 all read "five", unaltered |
| Diff check (B4) | PASSED — 7 hunks, all intended, no collateral, no encoding corruption |
| DB precondition (C0) | PASSED — 187–190 all `proposed`/`codify` |
| DB transition (C) | 187–190 → `implemented`, `status_updated_by='ceo'`, timestamp `2026-07-25 21:26:20` |
| Restore point | `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-preA-20260725T212611Z.db` (851968 bytes, gitignored) |
| Doc hash | `d8f17394c08d7dc72e550df133baba28ae897f1faf89ab2d5c78ab7efcd111ea` |
| `proposed` count | **0** |
| Doc committed | **NO** — left uncommitted per plan (Planner commits at wrap) |

### Ledger Updates

#### Prompt Feedback

- The blueprint's edit-application order (M1 first, E5 before E4 since both are in §4) avoided line-number drift between edits — each anchor was still unique when its turn came.
- The surgical date-swap approach for M1 (scoping the Edit anchor to the version+date substring, not the whole line) worked cleanly — the trailing clause survived without needing to be reproduced.
- The C0 precondition check immediately before the write, separate from Step 1's SA confirmation, is well-placed — it catches a concurrent status change between SA and DEV.
- The `.backup` method for the restore point is the right choice over `cp` for a WAL-mode DB.
