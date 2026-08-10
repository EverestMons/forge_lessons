# Dev Log — Step 1: shape-amendment-2026-08-09

**Plan:** 334
**Slug:** shape-amendment-2026-08-09
**Step:** 1 — DEV (place the seven doctrine edits + version/History row)
**Path taken:** FRESH

## Environment

**TREE:** `/Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/334`
**Remote:**
```
origin	git@github.com:EverestMons/forge_lessons.git (fetch)
origin	git@github.com:EverestMons/forge_lessons.git (push)
```

**TWO REPOS, TWO COMMITS:** The doctrine file lives in the ROOT repo (`/Users/marklehn/Developer/GitHub`) and is committed with `git -C /Users/marklehn/Developer/GitHub`. The deposits live in the dispatch tree (TREE above), a bellows worktree.

## A0 — Pre-edit Preconditions

### A0(1) — Slug re-entry probe
`grep -c -F "shape-amendment-2026-08-09" /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` → **0**
Path: FRESH.

### A0(2) — Cleanliness
`git -C /Users/marklehn/Developer/GitHub status --porcelain -- DRAFTING_CYCLE.md` → empty (clean).

### A0(3) — Version
`**Version:** 1.8 (2026-08-09). Amended only through the Iteration Protocol (§6).` → version **1.8**, correct for FRESH path.

### A0(3b) — BOTH-PATH / NONE-MATCH
Observed triple: (slug count=0, version=1.8, porcelain=empty) → matches FRESH path expectations. No NONE-MATCH.

### A0(4) — Anchor uniqueness (FRESH)
All `grep -c -F` against `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md`:
- A1 (`over a region the previous walk did not touch`): **1**
- A5 (`aim the next walk at the other step deliberately — review-target rotation prevents the quiet step`): **1**
- A6 (`After the sequential walk goes dry, rotate the`): **1**
- E2-anchor (`Execute against real data.`): **1**
- E4-anchor (`The compact form is`): **1**
- E8-anchor (`**Closing:** full walk 3 dry`): **1**
- History anchor (`## History`): **1**

All exactly 1. ✓

### A0(4b) — Clause-key integrity
Each of the seven Step-2 clause keys verified as substring of this plan's A-prime block:
- 233 (`twenty-seven sections for roughly the token budget of one targeted round`): **2** in plan ✓
- 246 (`3 findings leaving twelve regions unreached`): **2** in plan ✓
- 238 (`is the noise floor, not progress`): **2** in plan ✓
- 247 (`ten of ten ACID passes catching a culmination-introduced defect`): **2** in plan ✓
- 259 (`a normal outcome, not a deviation`): **3** in plan ✓
- 258 (`The record is rewritten more often than any other region`): **2** in plan ✓
- 271 (`the closing prose is written after the last pass has run`): **2** in plan ✓

All ≥1. ✓

### A0(5) — Post-condition earnability (FRESH)
Each `grep -c -F` against pre-edit doctrine returns **0**:
- `fold-introduced`: **0**
- `covers, it does not target`: **0**
- `Re-read the closing record`: **0**
- `part of the artifact, and every walk covers it`: **0**
- `RE-OPENS THE WALK`: **0**
- `Once the sequential walk meets`: **0**
- `judged stop`: **0**

All 0 — every post-condition CAN fail before the edit. ✓

## Edits — Before/After

### E1 — §2 doneness criterion (REPLACE)

**Before (A1):**
`Walk the lenses **in order, one pass per lens per walk.** Fold all accepted findings after each pass. Re-run a lens only on a **subsequent** walk — a fold's defect is usually caught by a *different* lens on different evidence. The cycle is **done** when a full walk returns zero or only-minor findings **over a region the previous walk did not touch**. ⚠️ **A falling finding-count is NOT the convergence signal** — severity falls because the same regions are being re-read, not because the artifact is sound. Budget for a cold panel's yield staying **flat**: a five-lens sequential panel returned 11 / 12 / 12 / 12 / 12 with no decay, roughly a third of each round being defects the immediately preceding round's folds introduced. The signal is **rotation**: a walk aimed at a previously unexamined region coming back dry. The **last event before deposit must be a lens pass, not a fold**; if the final pass folded anything, a brief confirming pass supplies the closing lens pass (expected dry; a new material finding re-opens the walk). Fold-and-deposit **exactly once**.`

**After (A1′):**
`Walk the lenses **in order, one pass per lens per walk.** Fold all accepted findings after each pass. Re-run a lens only on a **subsequent** walk — a fold's defect is usually caught by a *different* lens on different evidence. The cycle is **done** when a full walk returns findings that are **record-class only** — nothing that would change what an executing agent DOES — **and predominantly fold-introduced**, meaning defects this cycle's own folds created rather than defects that pre-existed it. **Both conditions are required, and the origin split is stated as a number in the Cycle Log** (` + "`" + `N of M fold-introduced` + "`" + `). ⚠️ **A falling finding-count is NOT the convergence signal** — severity falls because the same regions are being re-read, not because the artifact is sound. Budget for a cold panel's yield staying **flat**: a five-lens sequential panel returned 11 / 12 / 12 / 12 / 12 with no decay, roughly a third of each round being defects the immediately preceding round's folds introduced. **The signal is the noise floor, not an unexamined region:** after walk 1 there is none — a walk is every lens over the whole artifact — so no pass may be justified by naming one. A pass instead names the **new surface the last culmination created**, and reports the origin split of what it found; a pass whose findings are mostly its predecessor's fold damage is the noise floor, not progress (measured: 14 of 19 at exec-330, walk 4 at 0-for-3 pre-existing; 3 of 4 at exec-332; ten of ten ACID passes catching a culmination-introduced defect). The **last event before deposit is either a dry lens pass or a declared judged stop meeting the bar above** — **a judged stop is a normal outcome, not a deviation**, recorded with its reasoning. ⚠️ **A finding that is not record-class RE-OPENS THE WALK:** the bar is unmet and the cycle continues. Folds made on a closing walk that DOES meet the bar are record-class by the bar's own condition; those landing in the closing record are read by the closing-record re-read (§2.7), and **any that land elsewhere are enumerated individually in the residue list** — the re-read covers the record, not the whole artifact, and must not be cited as though it did. ⚠️ **This is a stated relaxation, not an oversight:** the prior criterion required a further confirming pass whenever the final pass folded anything, so a qualifying close may now deposit with record-class edits no lens has read. On T2 the cold panel supplies that reader (§2.6 — the panel is not waived by a judged stop). **On T1 there is no such reader, so a T1 judged stop rests on the residue enumeration and the closing-record re-read alone.** ⚠️ **A judged stop is auditable or it is not a stop.** Both of the bar's conditions are the author's own judgement, and the author is the party who wants to finish, so a bare assertion of record-class-ness is not a close — the older criterion was checkable by anyone (zero findings is observable) and its replacement stays checkable only by showing the work. **The Closing line therefore carries the origin split as a number and NAMES each residue finding's class in a clause apiece** (` + "`" + `3 record-class: two count-word lags, one stale label` + "`" + `); the per-finding detail — what each was, where, and which fold produced it — lives in the scratchpad walk register, which the closing-record re-read reads. ⚠️ **This is the ONE bounded exception to §3's compact-form rule, and §3 states it** — the bar cannot be audited from a log that may not name what it stopped on. Fold-and-deposit **exactly once**.`

### E2 — §2.7 coverage-not-aim (INSERT after Execute bullet)

**Before:** (nothing — insertion)
**After (A2′):** `- **A walk covers, it does not target.** A walk is every lens over the WHOLE artifact; a pass aimed at selected regions is not a walk and may not be recorded as one. Aim manufactures a falling count that reads as convergence and is not: same artifact, same reader, same day, the only variable being aim — the aimed pass returned 3 findings leaving twelve regions unreached, and the untargeted pass that followed returned 8 with zero unreached. The cost argument for aiming does not survive either — a complete five-lens walk covered twenty-seven sections for roughly the token budget of one targeted round, and a CRITICAL defect had by then survived nine aimed rounds in the one region no reader was ever pointed at. **Coverage is the unit of a walk; a count is not.** Directing extra attention within full coverage is legitimate; narrowing the pass is not.`

### E3 — §2.7 closing-record re-read (INSERT after A2′)

**Before:** (nothing — insertion)
**After (A3′):** `- **Re-read the closing record after the close.** A walk certifies everything except the paragraph that records it — the closing prose is written after the last pass has run, so it is pass-unexamined **by construction**, a structural blind spot rather than an oversight. After the final pass and its folds, re-read the closing record alone — the Closing line, the per-lens summary lines, the status header — adversarially and against the artifact. This is a short read of a paragraph, never a walk, and it is **mandatory at EVERY close — dry or judged stop alike.** It is most load-bearing on a judged stop, because the bar's own condition guarantees the residue is record-class; but the blind spot is structural, so a dry close does not escape it. (Measured: the shop's first post-**dry**-close re-read raised 2, both in closing prose, one claiming what its cited precedent declines to claim — the measurement comes from the DRY branch, which is why the rule may not be scoped to the other one.)`

### E4 — §3 Cycle Log as covered region (INSERT after compact-form paragraph)

**Before:** (nothing — insertion)
**After (A4′):** `**The Cycle Log is part of the artifact, and every walk covers it — name it explicitly in the walk's coverage rather than assuming it was swept.** The record is rewritten more often than any other region and read less often: attention follows what each phase changed, never what the changes accumulated into. (Measured: a walk that finally read a Cycle Log no lens had covered returned six of its eight findings there, every one the record decaying while the artifact converged.) **Count record-decay findings separately from artifact findings** in the per-lens lines — they are the class §2's bar reads, and merging them into one total hides exactly the signal it needs. ⚠️ **One bounded exception to the compact form above:** a cycle closing on a judged stop names each residue finding's CLASS in a clause apiece on the Closing line, alongside the origin split. The per-finding detail stays in the scratchpad register; what enters the block is a class list, not narrative.`

### E5 — §2.6 aim/coverage reconciliation (REPLACE)

**Before (A5):** `Before each walk, identify which step mutates and when it was last examined. If a walk's folds all land in one step, aim the next walk at the other step deliberately — review-target rotation prevents the quiet step from accumulating unexamined risk while the noisy one absorbs all attention. **The panel's yield does not decay, and that is structural.** Every fold is an unreviewed edit, so folding N findings creates a fresh unreviewed surface of N edits which the next reader is the first to see. Do not read a flat or rising round as panel failure, and do not read a falling one as convergence.`

**After (A5′):** `Before each walk, identify which step mutates and when it was last examined. If a walk's folds all land in one step, give the other step deliberate attention on the next walk (**review-target rotation**) — **within full coverage, never instead of it** (§2.7's covers-not-targets rule): directing attention is legitimate, narrowing the pass is not, and the quiet step must not accumulate unexamined risk while the noisy one absorbs all attention. **The panel's yield does not decay, and that is structural.** Every fold is an unreviewed edit, so folding N findings creates a fresh unreviewed surface of N edits which the next reader is the first to see. Do not read a flat or rising round as panel failure, and do not read a falling one as convergence.`

### E7 — §2.6 panel precondition (REPLACE)

**Before (A6):** `After the sequential walk goes dry, rotate the **reviewer**, not the lens: run the five lenses **cold** — fresh-context readers given only the artifact plus repo read access, **sequentially** (a concurrent cold run is a panel pass, not a walk — cumulation lives in the draft, so sequential preserves it). Author-verify cold findings; a cold reader can misread deliberate design as a defect.`

**After (A6′):** `Once the sequential walk meets §2's bar — dry, or a judged stop with its residue enumerated — rotate the **reviewer**, not the lens: run the five lenses **cold** — fresh-context readers given only the artifact plus repo read access, **sequentially** (a concurrent cold run is a panel pass, not a walk — cumulation lives in the draft, so sequential preserves it). Author-verify cold findings; a cold reader can misread deliberate design as a defect. ⚠️ **The panel is not waived by a judged stop** — a stop reached on record-class residue is exactly the state a cold reader is best placed to examine, and the panel's own findings re-open the walk on the same terms as any other lens pass.`

### E8 — §3 worked form for judged-stop close (INSERT after example block)

**Before:** (nothing — insertion)
**After (A8′):** `A cycle closing on a **judged stop** rather than a dry pass records the same block with two additions: each per-lens line carries its origin split (` + "`" + `w4 3 folded — 1 pre-existing, 2 fold-introduced` + "`" + `), and the Closing line states the bar it met, enumerates the residue by class, and gives the reasoning — for example, ` + "`" + `**Closing:** w4 met the bar — 3 findings, all record-class (two count-word lags, one stale label), 2 of 3 fold-introduced; closing-record re-read run, dry; judged stop, deposited once.` + "`" + ` The dry form above remains valid and remains the default; this is the form for the other legitimate outcome.`

### E6 — Version + History (REPLACE version line; INSERT History row)

**Before (version):** `**Version:** 1.8 (2026-08-09). Amended only through the Iteration Protocol (§6).`
**After (version):** `**Version:** 2.0 (2026-08-09). Amended only through the Iteration Protocol (§6).`

**History row (INSERT, new first bullet):** See the committed doctrine at `## History`; one physical line opening with `**2.0 (2026-08-09):**`, covering all twelve mandated elements: (1) version+date, (2) slug, (3) seven proposal ids, (4) new bar description avoiding the exact clause key, (5) D2 pair mandatory, (6) D3 covers-not-targets, (7) corpus path / no §6 deviation, (8) 259 premise correction, (9) §4/plan_lint divergence + register row, (10) amended units §2/§2.6/§2.7/§3, (11) inheritors dc-s4-prose + DC-surgical batch, (12) DB disposition 7 proposals → implemented|codify with 259/258 partial noted.

## Post-edit Verification

All seven earnability probes now return ≥1 against the post-edit doctrine:
- `fold-introduced`: **3**
- `covers, it does not target`: **1**
- `Re-read the closing record`: **1**
- `part of the artifact, and every walk covers it`: **1**
- `RE-OPENS THE WALK`: **1**
- `Once the sequential walk meets`: **1**
- `judged stop`: **6**

All seven clause keys present exactly once in the post-edit doctrine:
- 233 (`twenty-seven sections for roughly the token budget of one targeted round`): **1**
- 246 (`3 findings leaving twelve regions unreached`): **1**
- 238 (`is the noise floor, not progress`): **1**
- 247 (`ten of ten ACID passes catching a culmination-introduced defect`): **1**
- 259 (`a normal outcome, not a deviation`): **1**
- 258 (`The record is rewritten more often than any other region`): **1**
- 271 (`the closing prose is written after the last pass has run`): **1**

Sentinel check: `---BEGIN PINNED TEXT---` count in doctrine = **0**, `---END PINNED TEXT---` count = **0**. ✓

## E0 — Pre-commit Denylist

`git -C /Users/marklehn/Developer/GitHub status --porcelain -- PLANNER_TEMPLATE.md RULE_20_SELF_CHECK_BLOCK.md READONLY_AUDIT_CONTRACT.md SPECIALIST_TEMPLATE.md INTERMEDIATE_DECISION_PHRASES.md` → empty (all clean). ✓

## Commit Record

**Doctrine commit (ROOT repo):**
- Hash: `759b17116fad531abfc1630a1e9bd6e8b7508750`
- Message: `[334] shape-amendment-2026-08-09: DRAFTING_CYCLE v1.8 → v2.0 — §2 doneness bar (record-class + fold-introduced + judged stop), §2.7 covers-not-targets + closing-record re-read, §2.6 panel precondition + rotation reconciled, §3 Cycle Log coverage + judged-stop worked form`
- Pathspec: `DRAFTING_CYCLE.md` only
- `--numstat`: **11 insertions, 4 deletions**

**DOC_SHA:** `0964e1a70d6752f8656051b865ebcbdf76cb3e35e1b12415e547b54c45e4a7c7`
**PLAN_SHA:** `30c524f18420713f4b02bc51b6f17156aae421a95136963b0597f97a0045a053`

## Retained-material Keys

Three pre-existing sentences quoted verbatim from regions no edit touches:
1. (§1) `Escalation is **computed, not judged.** Before drafting, the Planner walks the trigger list; the highest tier any firing trigger demands sets the required tier.`
2. (§4) `` `bellows/scripts/plan_lint.py` gains a Drafting-Cycle check that runs at deposit and reports on the structure below: ``
3. (§6) `This file is the **base**; lessons refine it without rewriting it.`

## Owed BELLOWS Register Row (Rule 42 direct edit at wrap)

The following row is owed to `bellows/knowledge/FORWARD.md` — NOT to this project's register, because the deferred work is on `bellows/scripts/plan_lint.py`, whose queue lives at `bellows/knowledge/FORWARD.md`:

`- plan_lint §4 closing check vs the v2.0 judged-stop close: v2.0 requires each per-lens line to state its origin split, which contains the substring fold, while a judged stop carries no dry token. The check evaluates the LAST LENS RESULT LINE before the Closing line (lens_line_re over the Drafting Cycle block), not the Closing line itself, so its fold-without-dry condition fires on a CORRECT plan — systematically, because the doctrine mandates the trigger token. Measured by construction 2026-08-09: a canonical single-lens line stating the split WARNs; the same line without the split does not (but is non-compliant); a multi-lens All-lenses line is unparseable by the lens regex and falls through to the legacy closing-prose branch, which fires unless the Closing line carries a dry token that v2.0 does not require. Row 39 is the parse half and now has a second reason to close. Warn-first blocks nothing, so this is deferred rather than urgent, but the gate half of the §6 doctrine-and-gate pair is owed: teach the check to recognise a declared judged stop, or key it on the origin-split line instead. Deferred per §6, slug shape-amendment-2026-08-09.`

## Output Receipt: Complete

Deliverables produced:
- `knowledge/development/shape-amendment-dev-log-step-1-2026-08-09.md` (this file)

### Ledger Updates

#### Prompt Feedback

(none)

#### Forward Register

NONE
