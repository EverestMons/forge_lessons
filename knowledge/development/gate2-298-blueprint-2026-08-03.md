# Gate 2 Blueprint — Plan 298 (proposals 207–222)

**Date:** 2026-08-03
**Author:** SA (Step 1)

## Task S0 — Authoring Pin Verification

All three doctrine files match the authoring pins:

| File | Expected SHA-256 | Verified |
|---|---|---|
| `DRAFTING_CYCLE.md` | `2d5cf9ab7c3a87ed825a1e1edcafea9a9b2598f30b29a7e48868558874a18ee0` | ✅ match |
| `PLANNER_TEMPLATE.md` | `e8289d50f28711fdbf7c5319d812c229d3e7d2e255fc77f7ce868c19c01b6783` | ✅ match |
| `RULE_20_SELF_CHECK_BLOCK.md` | `3accbce0c8d2b44586edc6c5f95582f775d0bce14276966b7ca90724e0ca5644` | ✅ match |

## Version Collision Counts (re-measured)

| String | File | Expected | Measured |
|---|---|---|---|
| `1.3 (2026-08-02)` | `DRAFTING_CYCLE.md` | 2 | 2 |
| `4.82` | `PLANNER_TEMPLATE.md` | 3 | 3 |

## E22 Fence Pin Verification

- Fence lines in file: **2** (exactly one fenced block)
- Extracted block: **3030 bytes**
- BLOCK_SHA: `d399f9330802025eddebb5e627cd8efaa93752cc9f41fe3b9f763bca98e2b73f` — **matches authoring pin**
- Extraction command used (exactly as specified in CEO Context):
  `awk '/^`​{3}/{n++; next} n==1' RULE_20_SELF_CHECK_BLOCK.md | shasum -a 256`

## Dedup Record — Live Re-Confirmation

All four partial-dedup rows from 297:65–72 confirmed against live doctrine:

| Proposal | Stated anchor | Live grep -Fc | Confirmed |
|---|---|---|---|
| 215 | `DRAFTING_CYCLE.md:112` — "After compacting **or editing** the log, re-run the gate…" | 1 | ✅ |
| 217 | `DRAFTING_CYCLE.md:108` — "Do not keep a running fold-count … not as a separate running tally." | present | ✅ |
| 218 | `PLANNER_TEMPLATE.md:1349` — "verify the construction actually produces the expected delta" | 1 | ✅ |
| 207 | `DRAFTING_CYCLE.md:87` — "verify the subsumption against live data — per item, not in aggregate" | 1 | ✅ |

No disagreement with any dedup row.

---

## The Twenty-Two Edits — Anchored Before/After Pairs

### DRAFTING_CYCLE.md — E1–E12

---

**E1 — 210+216 → §2 doneness criterion. REPLACEMENT.**
- **Type:** sentence replacement
- **File:** `DRAFTING_CYCLE.md`
- **Anchor (open):** `The cycle is **done** when` — grep -Fc: **1**
- **Anchor (close):** `(that IS the diminishing-returns signal).` — grep -Fc: **1**
- **BEFORE (exact span to remove):**
  `The cycle is **done** when a full walk returns zero or only-minor findings (that IS the diminishing-returns signal).`
- **AFTER (exact replacement):**
  `The cycle is **done** when a full walk returns zero or only-minor findings **over a region the previous walk did not touch**. ⚠️ **A falling finding-count is NOT the convergence signal** — severity falls because the same regions are being re-read, not because the artifact is sound. Budget for a cold panel's yield staying **flat**: a five-lens sequential panel returned 11 / 12 / 12 / 12 / 12 with no decay, roughly a third of each round being defects the immediately preceding round's folds introduced. The signal is **rotation**: a walk aimed at a previously unexamined region coming back dry.`

---

**E2 — 217b → §2.6. APPEND to paragraph end.**
- **Type:** append sentence
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** `A "bounded" or "proven-clone" framing is not licence to down-tier or skip the cold panel` — grep -Fc: **1**
- **Append after:** `it is a statement about the plan's structure, not its risk.`
- **NEW text (appended):**
  ` **Ask the inverse question too: has a shipped sibling already DELETED this machinery?** A "do not re-add" note in a `​Done/`​ plan is invisible unless someone diffs against it, and a clone that re-adds deleted machinery reproduces a defect its parent already paid to remove.`

---

**E3 — 216b → §2.6. APPEND to paragraph end.**
- **Type:** append sentence
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** `review-target rotation prevents the quiet step from accumulating unexamined risk` — grep -Fc: **1**
- **Append after:** `while the noisy one absorbs all attention.`
- **NEW text (appended):**
  ` **The panel's yield does not decay, and that is structural.** Every fold is an unreviewed edit, so folding N findings creates a fresh unreviewed surface of N edits which the next reader is the first to see. Do not read a flat or rising round as panel failure, and do not read a falling one as convergence.`

---

**E4 — 214 → §2.6. NEW paragraph.**
- **Type:** new paragraph after E3's paragraph, last in §2.6 before `### 2.7`
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** `### 2.7 Cross-cutting rules (apply within every walk)` — grep -Fc: **1**
- **Insert BEFORE anchor (with blank line separation):**
  `**Aim the panel at the premises that LICENSE a deletion.** Hand cold readers the plan's deletion premises explicitly and ask them to falsify each against live data. A premise licensing a removal is the highest-value target — it is where the author has already convinced themselves — and it is sharpest under a "proven clone" framing, where the clone's deletions are exactly where its judgement diverges from its shipped parent.`

**Resulting §2.6 order:** intro ¶ → clone ¶ (+E2) → rotation ¶ (+E3) → E4 ¶ → `### 2.7`.

---

**E5 — 207 → §2.7 subtractive-trim bullet. APPEND.**
- **Type:** append sentence
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** `Never compute an edit boundary from a delimiter on line-oriented markup` — grep -Fc: **1**
- **Append after:** `(a delimiter-based split silently bisects a line that contains the delimiter as content).`
- **NEW text (appended):**
  ` **A count is not a value guard.** When a trim replaces a value-level assertion with a count over the same scope, the subsumption is not established by argument — **construct the change the surviving check is supposed to catch and confirm it FAILS.** A `​COUNT(*) WHERE col IS NOT NULL`​ cannot see a row moving between two non-NULL values: it passes unchanged while the capability it replaced is gone.`

---

**E6 — 208 → §2.7 lens-attestation bullet. APPEND.**
- **Type:** append sentence
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** `without it a later reader trusts an attestation that was never honest` — grep -Fc: **1**
- **Append after:** `without it a later reader trusts an attestation that was never honest.`
- **NEW text (appended):**
  ` **Price the re-run before writing an INHERITED marker.** Marking a claim inherited makes it honest, not true — the reason given for not re-executing is itself an unverified claim. Assess the literal cost first; most "impractical to test" reasons dissolve into a `​cp`​ plus one command.`

---

**E7 — 212 → §2.7 execute-against-real-data bullet. APPEND.**
- **Type:** append sentence
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** `pair it with its exit code, or with an input known to make it speak` — grep -Fc: **1**
- **Append after:** `pair it with its exit code, or with an input known to make it speak.`
- **NEW text (appended):**
  ` **`​grep -F`​ is mandatory for every literal search, and a search not run with `​-F`​ is invalid evidence regardless of its exit code.** On this shim a `​*`​-bearing pattern run without `​-F`​ exits **1, silently, on a file where the searched line is present** — so the unsafe invocation is forbidden outright rather than governed by exit-code interpretation rules.`

---

**E8 — 213 → §2.8. NEW bullet after the deletion bullet.**
- **Type:** new bullet
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** the deletion bullet ending with E9's appended text (apply E9 first, then E8)
- **Insert as new `- ` bullet after the deletion bullet, before the closing paragraph:**
  `- **The ledger records violations; it does not prevent them.** A Conflict Ledger can carry a constraint correctly and still watch the edit phase re-violate it — measured across six ACID passes, every one of which found defects introduced by the culmination immediately before it, including culminations whose entire purpose was repair. **After any fold, re-run the mechanical check that reads the touched region.** Read the record-without-prevent asymmetry as the argument for MECHANIZING a constraint rather than only documenting it.`

---

**E9 — 217a → §2.8 deletion bullet. APPEND.**
- **Type:** append sentence
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** `the same whole-artifact sweep an addition would need` — grep -Fc: **1**
- **Append after:** `the same whole-artifact sweep an addition would need.`
- **NEW text (appended):**
  ` **Count folds per REGION, not per plan** — a per-plan count hides the region-level accumulation this bullet turns on. ⚠️ **This is a drafting-time judgement tally kept in the scratchpad walk register, NOT a Cycle Log entry:** §3 forbids a running fold-count in the log and mandates the compact per-lens form, and that prohibition is **unchanged**.`

**⚠️ APPLICATION ORDER: E9 before E8.** E9 appends to the deletion bullet; E8 inserts a new bullet after it. Reversing the order would place E8 before E9's text.

---

**E10 — 215 → §3. APPEND (two sub-claims).**
- **Type:** append sentence
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** `the log has satisfied a check on the step's behalf` — grep -Fc: **1**
- **Append after:** `the log has satisfied a check on the step's behalf.`
- **NEW text (appended):**
  ` ⚠️ **Phrasing the line so it cannot match until earned is necessary but NOT sufficient** — a check satisfied by wording rather than by the condition changing is still silenced. And **the prohibition on quoting gate-matching tokens applies reflexively**, including to the sentence that warns against quoting them.`

---

**E11 — version line. SURGICAL SWAP against LENGTHENED ANCHOR.**
- **Type:** surgical replacement within line
- **File:** `DRAFTING_CYCLE.md`
- **Anchor (lengthened):** `**Version:** 1.3 (2026-08-02). Amended only through the Iteration Protocol` — grep -Fc: **1**
- **BEFORE:** `1.3 (2026-08-02)` (within the anchored line only)
- **AFTER:** `1.4 (2026-08-03)`

---

**E12 — `## History`, PREPEND a v1.4 row.**
- **Type:** prepend row (newest-first ordering confirmed)
- **File:** `DRAFTING_CYCLE.md`
- **Anchor:** `## History` — grep -Fc: **1**
- **Insert as FIRST row after `## History` heading:**
  `- **1.4 (2026-08-03):** Codified proposals 207, 208, 210, 212, 213, 214, 215, 216, 217. §2 doneness criterion rewritten — a falling finding-count is not the convergence signal; the signal is rotation to an unexamined region coming back dry (210+216). §2.6: clone inverse-question — check whether a shipped sibling already deleted the machinery (217b); panel yield is structurally flat, not decaying (216b); aim the panel at deletion premises (214). §2.7: `​grep -F`​ mandatory for every literal search (212); subtractive-trim count-vs-value guard (207); inherited-marker cost check (208). §2.8: ledger records-without-preventing — re-run mechanical checks after every fold (213); fold counts per region not per plan (217a). §3: gate-matching token prohibition is reflexive and phrasing-not-sufficient (215). **The lens count deliberately stays five** — all nine are sub-rules of existing sections. §4 is unchanged and remains in lockstep — 215 amends §3, and the §4 deferral is stated (see §6 and `​## When this file changes`​).`

**⚠️ This row does NOT contain the string `1.3 (2026-08-02)` — verified.**

---

### PLANNER_TEMPLATE.md — E13–E21

---

**E13 — 219 → Rule 17. APPEND.**
- **Type:** append sentence
- **File:** `PLANNER_TEMPLATE.md`
- **Anchor:** `deliverable verification is the safety net` — grep -Fc: **1**
- **Append after:** `deliverable verification is the safety net.`
- **NEW text (appended):**
  ` **A row whose honest disposition is "note" does not belong in this table.** The gate requires every row to carry a pass/fail glyph, so a note-shaped row has no expressible correct answer — deciding a row is note-shaped is the signal to **move it out of the table**, not to write `​NOTE`​ into a column the gate parses.`

---

**E14 — 221 → Rule 55 TITLE. REPLACEMENT.**
- **Type:** heading replacement
- **File:** `PLANNER_TEMPLATE.md`
- **Anchor:** `### 55. Assert a positive signal from the repo or tree that holds the state — empty output is not verification` — grep -Fc: **1**
- **BEFORE:** `### 55. Assert a positive signal from the repo or tree that holds the state — empty output is not verification`
- **AFTER:** `### 55. Assert a positive signal from the source that holds the state — empty output is not verification`

---

**E15 — 221 → Rule 55 BODY. APPEND (new paragraph before Source line).**
- **Type:** new paragraph inserted before Source line
- **File:** `PLANNER_TEMPLATE.md`
- **Anchor:** `Source: proposals 165 + 167, lessons 2026-07-20 / 2026-07-21` — grep -Fc: **1**
- **Insert BEFORE anchor (with blank line separation):**
  `**Process state is in scope, and the principle governs — not any one command.** `​pgrep`​ returns exit 1 for "no match", which is indistinguishable from "not running", so every failure mode presents as the answer "the daemon is down." **Require a positive confirmation that RESOLVES** — a PID that is then confirmed live, a row that is then read back — and never treat an empty result as an answer. ⚠️ **`​ps -p`​ against a recorded PID is the worked example, not the rule:** a recorded PID goes stale across a restart, and a stale record reports a live process as dead — the same false negative, relocated from the pattern to the record. When the positive confirmation fails, re-establish the record before concluding absence.`

---

**E16 — 209 → NEW Rule 63. INSERT after Rule 62's Source line.**
- **Type:** new rule section
- **File:** `PLANNER_TEMPLATE.md`
- **Anchor:** `Source: proposal 203, lesson 2026-07-30` — grep -Fc: **1**
- **Insert AFTER anchor (E16 then E17 then `---`):**

```
### 63. Read the DELIVERY code before theorising about non-arrival
When a mechanism's output does not arrive, **read the code that delivers it before proposing a cause.** Non-arrival has at least three candidate causes — never sent, sent-and-lost, and sent to an unconfigured destination — and they are indistinguishable from the receiving end; only the delivering code separates them. Evidence: the same missing register row was blamed on the emitting plan, then on the daemon, before a read of `bellows.py:1417` showed the destination resolving to a path that did not exist, logged and skipped.
*Source: proposal 209, lesson 2026-08-01*
```

---

**E17 — 220 → NEW Rule 64. INSERT after E16.**
- **Type:** new rule section
- **File:** `PLANNER_TEMPLATE.md`
- **Placement:** immediately after E16

```
### 64. A pipe-bearing command never goes in a markdown table cell
A command containing `|` must never be placed in a table cell — put it in a fenced block above the table and have the row cite its result. A delimiter-bearing command inside a delimiter-structured document is a collision in which **escaping changes the semantics**: escaping to `\|` to survive the cell turns ERE alternation into a literal pipe that matches nothing. The failure is silent when the command's "no match" and "not running" exits are the same value.
*Source: proposal 220, lesson 2026-08-03*
```

---

**E18 — 218+222 → Checklist #32. APPEND.**
- **Type:** append sentence
- **File:** `PLANNER_TEMPLATE.md`
- **Anchor:** `not through the real entry point` — grep -Fc: **1**
- **Append after:** `not through the real entry point).`
- **NEW text (appended):**
  ` **The instrument must assert on the POST-condition, never on the presence of the thing being changed** — a check that greps for the text it is trying to remove reports OK on that text's survival. Any scripted edit asserts **`​after != before`​**, not merely that an anchor matched. **And when a canary is owed, pay for it with real pending work rather than a synthetic probe:** use the actual backlog as the payload, and pair the live observation with an in-process prediction of the same value, so agreement proves the path while disagreement localises the fault.`

---

**E19 — version line `:5`. SURGICAL SWAP against LENGTHENED ANCHOR.**
- **Type:** surgical replacement
- **File:** `PLANNER_TEMPLATE.md`
- **Anchor (lengthened):** `**Version:** 4.82` — grep -Fc: **1**
- **BEFORE:** `**Version:** 4.82`
- **AFTER:** `**Version:** 4.83`

---

**E20 — `:6`. SURGICAL SWAP.**
- **Type:** line replacement
- **File:** `PLANNER_TEMPLATE.md`
- **Anchor:** `**Last Updated:** 2026-08-02 (v4.82)` — grep -Fc: **1**
- **BEFORE:** `**Last Updated:** 2026-08-02 (v4.82)`
- **AFTER:** `**Last Updated:** 2026-08-03 (v4.83)`

---

**E21 — `## Lessons Learned`, PREPEND a v4.83 row.**
- **Type:** prepend row (newest-first ordering confirmed)
- **File:** `PLANNER_TEMPLATE.md`
- **Anchor:** `## Lessons Learned` — grep -Fc: **1**
- **Insert as FIRST data row after the `|---|---|` separator:**
  `| 2026-08-03 | v4.83: Gate 2 codification, 2026-08-03 cycle. Six proposals (209, 218, 219, 220, 221, 222) via six edits. New Rule 63 — read the delivery code before theorising about non-arrival (209). New Rule 64 — a pipe-bearing command never goes in a markdown table cell (220). Rule 17 amended — a note-shaped row does not belong in the verification table (219). Rule 55 title widened from "repo or tree" to "source"; body extended with process-state scope and the positive-confirmation-that-resolves principle, with `ps -p` demoted to a worked example per CEO decision (c) (221). Checklist #32 extended — assert on the post-condition, never on the presence of the thing being changed; canaries use real pending work (218+222). **The lens count deliberately stays five.** |`

**⚠️ This row does NOT contain the string `4.82` — verified.**

---

### RULE_20_SELF_CHECK_BLOCK.md — E22

---

**E22 — 211 → the "Status column" paragraph. APPEND.**
- **Type:** append sentence
- **File:** `RULE_20_SELF_CHECK_BLOCK.md`
- **Anchor:** `the token must be the entire cell value` — grep -Fc: **1**
- **Append after:** `the token must be the entire cell value.`
- **NEW text (appended):**
  ` ⚠️ **An annotated cell therefore asserts nothing and escapes BOTH gates.** Because matching is by cell equality, a cell carrying a token plus a note is not a positive row — it is never scanned for hedging keywords — and it carries no failure glyph for `​_gate_rule_22_verification`​ either. The row is neither passing nor failing and both gates ignore it. **The status cell holds exactly one token and nothing else.**`

---

## Per-File Line Deltas (measured by dry-run)

Copies of all three files were placed in `/tmp/gate2-298-dryrun/` (outside every git tree), all 22 edits applied to the copies, and `git diff --no-index --numstat` run against the originals. The scratch directory was deleted and confirmed absent afterward.

| File | Added | Deleted | Net | Lines before | Lines after |
|---|---|---|---|---|---|
| `DRAFTING_CYCLE.md` | 13 | 9 | +4 | 174 | 178 |
| `PLANNER_TEMPLATE.md` | 16 | 5 | +11 | 2088 | 2099 |
| `RULE_20_SELF_CHECK_BLOCK.md` | 1 | 1 | 0 | 140 | 140 |

## Task S9 — Closing Re-Pin

All three files re-hashed as the last act. All match S0:

| File | SHA-256 | Match S0 |
|---|---|---|
| `DRAFTING_CYCLE.md` | `2d5cf9ab7c3a87ed825a1e1edcafea9a9b2598f30b29a7e48868558874a18ee0` | ✅ |
| `PLANNER_TEMPLATE.md` | `e8289d50f28711fdbf7c5319d812c229d3e7d2e255fc77f7ce868c19c01b6783` | ✅ |
| `RULE_20_SELF_CHECK_BLOCK.md` | `3accbce0c8d2b44586edc6c5f95582f775d0bce14276966b7ca90724e0ca5644` | ✅ |

No doctrine file was modified by this step.
