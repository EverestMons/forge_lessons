#!/usr/bin/env python3
# Section-2 rewrite builder - DRAFTING_CYCLE v2.3 -> v2.4.
# All-or-nothing: single read, every anchor asserted, single write.
import io, sys

SRC = sys.argv[1]
DST = sys.argv[2]
s = io.open(SRC, encoding='utf-8').read()
edits_applied = []

def rep(old, new, expect=1, label=""):
    global s
    got = s.count(old)
    assert got == expect, f"ANCHOR COUNT {label}: expected {expect}, got {got} for {old[:60]!r}"
    s = s.replace(old, new, expect)
    edits_applied.append(label)

# ---------------- E1: the bar rewrite - the whole single-line paragraph at line 38,
# anchored by its unique opening (the full 3,593-char line is matched by prefix+suffix
# via the two unique fragments; the replacement is composed as SEVEN paragraphs).
lines = s.split('\n')
idx = next(i for i, l in enumerate(lines) if l.startswith("Walk the lenses **in order, one pass per lens per walk.**"))
OLD_LINE = lines[idx]
assert len(OLD_LINE) > 3000, f"bar line unexpectedly short: {len(OLD_LINE)}"
assert s.count(OLD_LINE) == 1

NEW_BAR = """Walk the lenses **in order, one pass per lens per walk.** Fold all accepted findings after each pass — that fold set is a **culmination**, the unit the residue-battery and newest-constraint cadences (§2.6, §2.8) key on. Re-run a lens only on a **subsequent** walk — a fold's defect is usually caught by a *different* lens on different evidence.

**The cycle is DONE when a full walk's findings, classified by the surface each TOUCHES, are all record-class — zero instruction-class findings.** An **instruction-class** finding changes what an executing agent DOES: a step's command, a guard, a post-condition, a branch, a value a gate acts on. A **record-class** finding changes only the artifact's account of itself: the Cycle Log, ledger rows, fold commentary, changelog prose. **Classify by the edit the fold would make, not by the sentence's location** — a Cycle-Log line a gate matches is instruction-class (the gate acts on it — §3's gate-span absorption, which holds until bellows Forward row 45's regex fix ships), and a rationale sentence inside a step that no agent or gate reads is record-class. The walk's per-class split is stated as numbers in the Cycle Log (`instruction 0 / record 5`). *(Measured, and the reason the bar reads TOUCH: one cycle's walk 3 changed instructions in roughly ten of fifteen findings, walk 4 in two of eight — the instruction surface was closing while the commentary surface was not, and structurally cannot, because every fold adds explanation and the explanation is itself reviewable by the next walk. A cycle steered by any whole-artifact count keeps finding work forever, all of it real, none of it changing what an agent does. Proposal 308; entry 300. ⚠️ A stated resolution, not an oversight: 308's remedy reads "nearly all record-class is done"; the bar adopts sibling 275's stricter record-ONLY form because "nearly" is the unauditable judgement the auditable-stop clause below exists to remove — under this bar the measured walk 4, at two instruction findings, signals the transition and does not itself close.)*

**The origin split (pre-existing vs fold-introduced) is DEMOTED to a diagnostic — it is no longer a condition of the bar.** Report it as numbers alongside the per-class split (`N of M fold-introduced` — the declared-once numeric form §2.7's count-in-prose rule requires), because it still says where findings come from — but it cannot tell a finishing cycle from a circling one: **the prior bar's "predominantly fold-introduced" condition and the section's own noise-floor warning were the same number read in opposite directions** (measured: 28% → 68% → 67% → 75% across four walks of one cycle, both readings applying from walk 2 on; bellows Forward row 53, resolved by this rewrite). A pass whose findings are mostly its predecessor's fold damage remains the **noise-floor signature** — a reason to suspect circling, never a licence to close (measured: 14 of 19 confirming-pass findings at exec-330 were the cycle's own fold damage, walk 4 running 0-for-3 pre-existing; 3 of 4 at exec-332; ten of ten ACID passes each catching a culmination-introduced defect).

⚠️ **A falling total finding-count is NOT the convergence signal, and no pass may be justified by naming an "unexamined region"** — after walk 1 there is none; a walk is every lens over the whole artifact (§2.7). A pass instead names the **new surface the last culmination created** and reports both splits of what it found. Budget for a cold panel's yield staying **flat**: a five-lens sequential panel returned 11 / 12 / 12 / 12 / 12 with no decay, roughly a third of each round being defects the immediately preceding round's folds introduced.

**After a RESTRUCTURING pass — a collapse, a promotion, a sub-step split — the convergence clock RESETS: the next walk is a FIRST pass over the new arrangement, never a confirming pass, and its finding count is not a convergence signal — and the bar is met only by a walk that restructured nothing: a bar-meeting walk that contains a restructuring fold does not close.** *(Proposal 302; entry 294.)* **A confirming pass is UNTARGETED by construction** — record decay hides from aimed passes precisely because attention follows what changed *(proposal 278; §2.7's covers-not-targets rule is the general form)* — and **its yield is reported by class: a confirming pass returning record-class only is the signature that the artifact converged before its account of itself did.** Close on it (absent any restructuring fold — the clock-reset rule above takes precedence); do not schedule another walk to confirm the confirmation. *(Proposal 275; entry 267.)*

**The last event before deposit is either a dry lens pass or a declared judged stop meeting the bar above — a judged stop is a normal outcome, not a deviation,** recorded with its reasoning. ⚠️ **An instruction-class finding RE-OPENS THE WALK:** the bar is unmet and the cycle continues. Folds made on a closing walk that DOES meet the bar are record-class by the bar's own condition; those landing in the closing record are read by the closing-record re-read (§2.7), and **any that land elsewhere are enumerated individually in the residue list** — the re-read covers the record, not the whole artifact, and must not be cited as though it did. ⚠️ **This is a stated relaxation, not an oversight:** a qualifying close may deposit with record-class edits no lens has read. On T2 the cold panel supplies that reader (§2.6 — the panel is not waived by a judged stop). **On T1 there is no such reader, so a T1 judged stop rests on the residue enumeration and the closing-record re-read alone.**

⚠️ **A judged stop is auditable or it is not a stop.** The touch classification is the author's own judgement, and the author is the party who wants to finish, so a bare assertion of record-class-ness is not a close — show the work. **The Closing line carries the per-class split as numbers and NAMES each residue finding's class in a clause apiece** (`instruction 0 / record 3: two count-word lags, one stale label`); the per-finding detail — what each was, where, which fold produced it, and the classification's reasoning wherever it is not obvious — lives in the committed walk register, which the closing-record re-read reads. ⚠️ **This is the ONE bounded exception to §3's compact-form rule, and §3 states it** — the bar cannot be audited from a log that may not name what it stopped on. Fold-and-deposit **exactly once**."""

rep(OLD_LINE, NEW_BAR, 1, "E1-bar-rewrite")

# ---------------- E2: section 2.8 oscillation clause re-base (stale against the new bar)
rep("or the per-lens finding count stops trending toward dry",
    "or the per-lens instruction-class count stops trending toward zero",
    1, "E2-s28-rebase")

# ---------------- E3: section 2.7 bullet - 278's tracking-line sweep clause
rep("- **Per-phase commits.**",
    "- **Any phase that completes a tracked structure sweeps the record lines that track it, in the SAME culmination.** A count, a status word, or a tally that tracks a structure decays the moment the structure moves — and the phase that moved it is the only one that knows. Sweeping later means a finding-driven pass must rediscover the lag, and record decay hides from aimed passes. *(Proposal 278; entry 270 — the sweep half; the untargeted-confirming-pass half lives in §2's bar.)*\n- **Per-phase commits.**",
    1, "E3-s27-tracking-sweep")

# ---------------- E4: section 3 judged-stop exception - re-base "alongside the origin split"
rep("names each residue finding's CLASS in a clause apiece on the Closing line, alongside the origin split.",
    "names each residue finding's CLASS in a clause apiece on the Closing line, alongside the per-class split (and the origin split as its diagnostic).",
    1, "E4-s3-exception-rebase")

# ---------------- E5: section 3 worked judged-stop form - both splits
rep("each per-lens line carries its origin split (`w4 3 folded — 1 pre-existing, 2 fold-introduced`)",
    "each per-lens line carries its per-class split with the origin split as diagnostic (`w4 3 folded — instruction 0 / record 3; 1 pre-existing, 2 fold-introduced`)",
    1, "E5-s3-worked-form")

rep("`**Closing:** w4 met the bar — 3 findings, all record-class (two count-word lags, one stale label), 2 of 3 fold-introduced;",
    "`**Closing:** w4 met the bar — instruction 0 / record 3: two count-word lags, one stale label; 2 of 3 fold-introduced (diagnostic);",
    1, "E5b-s3-closing-exhibit")

# ---------------- E6/E7: version + History
rep("- Weak spots:          w1 2 folded; w2 dry; w3 dry.",
    "- Weak spots:          w1 2 folded — instruction 1 / record 1; w2 dry; w3 dry.",
    1, "E8-s3-dry-form-example")

rep("the final QA step's gate span absorbs it, so a gate-matching string quoted in the log is evaluated as if the QA step had said it.",
    "the final QA step's gate span absorbs it (until the gate-span regex fix ships — bellows Forward row 45; the record-placement rule below is the authoring-side guard meanwhile), so a gate-matching string quoted in the log is evaluated as if the QA step had said it.",
    1, "E9-s3-gatespan-currency")

rep("**Version:** 2.3 (2026-08-11). Amended only through the Iteration Protocol",
    "**Version:** 2.4 (2026-08-11). Amended only through the Iteration Protocol", 1, "E6-version")

HIST = "## History\n"
ROW = ("- **2.4 (2026-08-11):** slug s2-rewrite-2026-08-11; the §2 doneness-bar REWRITE — cluster (A) of the 2026-08-10 gate "
"(proposals 275, 278, 292, 302, 308; entries 267, 270, 284, 294, 300), routed as one unit, landed as one coherent rewrite; corpus path proper, no §6 deviation. "
"THE BAR NOW READS TOUCH: done = a full walk with zero instruction-class findings, per-class split stated as numbers; the origin split is DEMOTED to a diagnostic, "
"resolving the self-contradiction bellows Forward row 53 recorded (the fold-introduced fraction was simultaneously the convergence condition and the noise-floor "
"signature — measured 28/68/67/75% with both readings applying). Restructuring passes reset the convergence clock (302); confirming passes are untargeted and "
"report by class, record-only yield = converged-before-its-account (275); §2.7 gains the tracking-line sweep clause and §2's bar the untargeted half (278); "
"292's static-artifact correction confirmed already carried by v2.0 text, ratio-reporting discipline retained; the record-ONLY form is 275's, adopted over 308's nearly-all wording as the auditable of the two (stated resolution, panel seat 1); the §3 dry-form example carries the per-class number and the gate-span sentence its Forward-45 currency marker. §2.8's oscillation clause re-based (finding-count-"
"toward-dry → instruction-class-toward-zero); §3's judged-stop exception and worked form re-based to carry both splits. "
"DB: proposals 275/278/292/302/308 flipped reference|backlog → implemented|codify, AND the seven rows of the 2026-08-09 cluster (A) — 233, 238, 246, 247, 258, 259, 271 — "
"flipped reference|backlog → implemented|codify, completing plan 334's held Step 2 on CEO release 2026-08-11 (the hold's condition, a real cycle or two under v2.0+, met "
"many times over; 258 and 259 flip PARTIAL per 334's mapping — 258's phase-labelling quarter and 259's cross-plan-measurement middle ask (D5, funnel-routed) remain "
"unbuilt and are recorded here rather than silently absorbed). Inheritors: every future cycle; the in-flight s2-rewrite cycle itself closed under the PRIOR bar (v2.3), "
"stated for the audit trail.\n")
rep(HIST, HIST + ROW, 1, "E7-history")

io.open(DST, 'w', encoding='utf-8').write(s)
print(f"OK — {len(edits_applied)} edits applied: {', '.join(edits_applied)}")
