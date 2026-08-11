#!/usr/bin/env python3
# Gate-2 batch 2 builder - PLANNER_TEMPLATE v4.85 -> v4.86.
# All-or-nothing: reads SRC once, asserts every anchor count==1 BEFORE any
# mutation, applies all ten edits in memory, writes DST once at the end.
# An assertion failure anywhere aborts with ZERO bytes written.
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

D = "2026-08-11"
def rule(num, pid, title, body):
    return f"### {num}. {title}\n\n{body}\n\n*Source: proposal {pid}, codified {D} (Gate 2 batch 2)*\n"

NEW_RULES = "\n".join([
rule(65, 223, "Verify a mandated block in the SECTION the parser reads, not merely present in the deposit",
"A daemon-parsed block (Ledger Updates, Forward Register, Prompt Feedback) counts as delivered only when its text sits inside the section the parser scopes to — correctly formatted and correctly located are different claims, and a cross-reference satisfies a text-capturing check as well as content does. Verification of any channel emission asserts the block's position against the parser's input scope (which section, which heading level), never bare presence in the deposit. Measured: the Forward Register lost every item of an emission because the substantive block was written outside the Ledger Updates section — the channel's third distinct failure mode."),

rule(66, 225, "A mandated requirement lives in the step that must comply",
"For every mandated requirement, name the step that must COMPLY and confirm the requirement's text is in that step's prompt — presence anywhere in the plan is not compliance-reachable, and a rule enforced by a QA row must also be stated where the artifact is produced. Sweep both directions: producer-missing (the check exists, the producing step never heard the rule) and consumer-missing (the producing step complies, nothing would notice a violation). Measured: three instances in one drafting cycle of a requirement written into the checking step only, each with a structural home — in the wrong step — so the structural-home rule (54) never fired."),

rule(67, 228, "Before authoring verification for a delivery channel, read the delivering code and state which artifact it consumes",
"A check aimed at a different artifact is a proxy no matter how exactly it reproduces the consumer's logic. Before authoring any verification for a delivery channel, read the delivering code to find WHICH ARTIFACT it consumes (transcript vs deposit vs DB row), and state that artifact in the check itself. Measured: a channel failed four distinct ways across three sessions because every check read the deposited file while the daemon reads the transcript — a green check over a total loss."),

rule(68, 229, "Channel items are single physical lines; downstream of a splitter, compare content, not counts",
"Constrain the shape that makes silent loss possible: no Forward Register (or other channel) item may wrap onto a second physical line, because line-pattern splitters keep only lines matching the bullet pattern and drop continuations. A cardinality assertion is blind to loss WITHIN an item — five written, five recovered, exit zero, and every item truncated. When items carry substance, verification compares content, not counts (the intra-item form of the count-is-not-a-value-guard lesson)."),

rule(69, 236, "A parser-terminator fix belongs to the class, not the instance",
"When a fix turns on a parser's terminator, enumerate every construct that parser terminates the same way and fix the whole set — in an ordered set of parsed subsections, the LAST one is structurally the exposed one (it terminates only by blank line or end-of-stream). Measured: a terminator fix applied to one subsection while the mechanism was subsection-generic; the fold landed where the defect was noticed, not where the mechanism lives — the fourth instance of that class."),

rule(70, 239, "A declared-outputs block lists only what the step produces on EVERY path",
"Name conditional artifacts in prose, where the tolerant gate can still see them — never in the Deposits block, where the strict gate will demand them on paths that don't produce them. When two checks read the same declaration, establish each one's polarity separately: the scope check TOLERATES extras and fails unnamed changes; the deposit check REQUIRES every name and fails absences. One list read with opposite polarities means a conditional entry guarantees a failure on some path. (Extends Rule 26's block convention with the polarity discipline.)"),

rule(71, 242, "Audit every new verification referent for true independence",
"A referent is independent only if it exists BEFORE the actor acts and OUTSIDE the actor's control. A referent sourced from the actor's own record — a diff compared against the deltas the actor recorded, a hash compared against a baseline the actor supplied — reproduces the circularity it exists to break, with the form of verification and none of its content. Audit each new referent against this test at authoring. Measured: two of three referents in one edit were circular in exactly this way."),

rule(72, 255, "Declare polarity for every two-direction number in a diagnostic",
"When a diagnostic question reports a number that can move in two directions, state which direction is good and for whom — or state explicitly that both movements are legitimate and the weighing is not the question's to make. Without the declaration, individually-correct patches accumulate contradictions: one check killing a proposal on WIDE firing while its sibling kills it on NARROW, and a third pricing the identical movement as a virtue. One quantity, two legitimately opposed values, no verdicts in any question."),

rule(73, 257, "Record a constraint and its violation-catching check in the same edit",
"A rule in prose — in LESSONS.md or in the plan's own ledger — has no mechanical consequence, and the author is the least reliable enforcer of a rule they have just written. When a constraint is recorded in a plan, add the check that would catch its violation in the SAME edit. Treat recurrence of an already-recorded lesson as evidence it needs MECHANISING — route it to the forge as a mechanization candidate rather than restating it in prose. Measured: four recurrences in one cycle of the same author's own recorded constraints."),

rule(74, 264, "A directional insert anchors on a COMPLETE line, and a mechanism fix sweeps for its mirror",
"An insert-after or insert-before edit anchors on a COMPLETE physical line with the full final composition spelled out in the new text — anchoring on a line prefix inserts at the prefix boundary and can split the line, and every presence grep, count, and date pin then passes on the intact fragments. After fixing a mechanism defect at one site, sweep the plan for the same mechanism in mirror form (insert-after has an insert-before twin). Add one verification that SPANS the would-be damage point, so a split cannot pass unnoticed."),

rule(75, 265, "Path-scope the COMMIT, not just the add, and assert the commit's contents",
"`git add <path> && git commit` is not a path-scoped commit: a bare `git commit` commits the ENTIRE index, so any foreign change already staged rides in silently — and in a root repo that is a live working area, pre-staged entries are a normal state. Use `git commit -m '...' -- <path>` with the pathspec on the COMMIT, and pair it with the post-commit assertion `git show --name-only --format= HEAD` printing exactly the intended paths. Content-hash and log checks do not catch this: the hash reads only the intended blob, and the log check sees only commits touching the intended path."),

rule(76, 266, "Before editing a doc, grep the codebase for line-number citations of it",
"A `:NN`-style line citation inside running code is a hard constraint on a doc edit's map: any edit changing the line count above NN breaks the citation silently. Before editing a doc, grep the codebase for `:NN` citations of that file and design around each — in-place rewrites above cited lines, insertions only below them — then verify BY VALUE (the cited line still says the cited thing), never by arithmetic. When authoring new checks, cite doctrine by section anchor or literal text, never by line number."),

rule(77, 267, "Sweep the source deposit's closing sections for directives addressed to a future plan",
"A diagnostic's deposit may close with instructions addressed to the plan that will implement it — a required literal phrase, a mandated check, a naming convention the daemon parses. Those directives are REQUIREMENTS, not commentary, and they are invisible to every review of the intermediate artifacts (baton, decision record): only a diff against the SOURCE deposit finds them. When authoring a plan that implements a diagnostic's findings, sweep the deposit's closing sections; machine-parsed conventions deserve a grep-verifiable check at deposit time. (Extends Rule 27's citation discipline to the directive sweep.)"),

rule(78, 268, "Construct the mid-band cases for every threshold or quantifier clause before shipping",
"For any threshold, quantifier, or every/most/any clause, construct the mid-band cases BEFORE shipping: most-but-not-all, sibling verbs the clause's own verb does not cover, aggregates of individually-small parts. Price each constructed case as caught, dropped-and-accepted, or dropped-and-unpriced — and record each acceptance in the artifact with a boundary test. Measured: a clause priced only at its poles (the census cases and the constructed 100% case) silently reclassified a most-rows mutation, a full-table DELETE under a sibling verb, and a schema migration."),

rule(79, 274, "A halt that offers options banners the inferred choice at the next gate",
"The verdict grammar is one bit — a continue issued for ANY reason is structurally identical to every other continue, and no later step can distinguish the intents. When a halt offers the CEO options, the accepting branch must BANNER which option it inferred, in its chat message and Output Receipt, at the next gate the CEO reads — so a mis-read costs one verdict gate rather than the run. (The verdict-channel constraint itself is bellows-owned; this is the authoring half.)"),

rule(80, 277, "An authoring-time id is a prediction; the verify-at-deposit clause names every site",
"Any plan id read from `id_sequence` at authoring is a PREDICTION — an in-window deposit by another terminal consumes it. Carry a verify-at-deposit clause that NAMES every site the id token appears in: backup globs, copy-asides, resume-glob guards, deposit filenames. At deposit: re-read `id_sequence`, re-token every named site to the actual id, and record the drift as retraction history. A bare 'verify the id' leaves the glob tokens stale — the clause works only because it enumerates. Measured live: a plan authored against 310 deposited as 311."),

rule(81, 280, "Census every copy of an enum before adding a value",
"A recognized-value set lives in more copies than the branch being edited: code branches, lint token sets, claim validators, and governance prose. Before adding any enum value, census EVERY copy with `grep -F` across the repo AND the template; ship all copies in one plan or enumerate the deferral explicitly. Treat the census as the plan's own Site list with a both-edits-or-neither clause per copy-pair. Measured: a new mode shipped in one branch while three other copies drifted, one of them a hard-FAIL lint check."),

rule(82, 281, "Price a change at its IN-population rate and argue against the strongest counterexample",
"For any headline rate justifying a change, compute the rate over the IN-population — the rows the change actually affects — and present that number first; a cross-population average dilutes the effect with rows that stay untouched. Then name the strongest single counterexample FROM the in-population and argue against it specifically, not against the average case. Measured: a mechanization priced at a 3.08% cross-population rate was actually 4.1% in-population, and the strongest counterexample (a tranche plan saved by a rote-looking pause) sat exactly in the opt-in target slice."),

rule(83, 282, "State the exact enforcement tier when correcting enforcement claims",
"When correcting stale doc claims about what is enforced, read the ENFORCEMENT implementation first and state its exact tier — reject, warn, or silent, and at which lifecycle point (deposit, claim, runtime). Overstatement and understatement are the same defect: each replaces one falsehood with another. Sweep the correcting plan's OWN prose for the banned claim shapes before deposit. Measured: a correction plan was itself about to carve three new false tiers ('hard-checks at deposit', 'ignores STOP prose entirely', 'warn-only' on a three-tier validator)."),

rule(84, 284, "Run the current implementation on every degenerate fixture before asserting its expected outcome",
"A test fixture that specifies a wrong expected outcome FORCES a literal developer to weaken the guard it is testing. For every degenerate or edge fixture, run the CURRENT implementation on the input first and assert its measured behaviour, carving out only the delta the change intends to alter. A fixture no correct implementation can satisfy is a defect in the PLAN, at the same severity as a defect in code. Measured: a fixture asserting exit 0 on an unparseable header, where the shipped check correctly exits 1."),

rule(85, 288, "Commit compounds start with cd-absolute and end with a toplevel assert",
"Every command compound touching a repo starts with `cd /abs/path` as its FIRST token — never trust cwd persistence between invocations, never lead with `cp`. Every commit compound ends by printing `git rev-parse --show-toplevel`, and a wrong or missing print is treated as NOT COMMITTED regardless of what `git log -1` shows: a relative-path compound can land the commit in whichever repo the cwd actually was, and the log check then reports the new hash — in the wrong repo. Measured: three culminations committed to the shop root this way in one session."),

rule(86, 289, "Never promise a verdict the grammar lacks",
"The Bellows verdict grammar is a closed set — `continue` and `stop`, nothing else. Read `verdict.py` before naming options at any gate; a plan that promises 'redo', 'retry', or any third verdict has authored an unreachable branch. A redo is expressed as: stop, then a corrected re-deposit under the stable slug whose A0 branch keys on the CONCRETE recorded half-state — greppable facts, never narrative. (The grammar itself is bellows-owned; this is the authoring half.)"),

rule(87, 293, "A severity or reversibility label is a CLAIM with a probe",
"Treat 'irreversible', 'load-bearing', 'blast radius', 'trivial' and their kin as claims requiring probes, not framing: each shapes risk posture, machinery, and step count, yet no factual-claim rule fires on an adjective. On a clone diff, re-derive the parent's risk adjectives exactly as its factual claims are re-derived. Measured: an inherited 'irreversible' survived 125 findings, three walks, three ACID passes and a five-seat panel, then dissolved in one query — the write touched 4 of 15 columns, none content, reversal a single statement."),

rule(88, 297, "Prefer derived expectations over constants in QA assertions",
"Before shipping any 'exactly N' assertion, confirm N is what a CORRECT run produces — including under re-entry (a legitimate resume adds a commit), concurrent actors, and later plan edits that change the count (a split leaves a stale deposit total). Prefer expectations DERIVED at run time from the plan's own declarations: read the Deposits blocks and count them; compute commit counts from the recorded re-entry state. A constant guard dies at exactly the moment it was supposed to work, and it dies by consent. Measured: three assertions in one plan would each have failed a correct execution."),

rule(89, 303, "A census over a corrected corpus states which half it measures",
"Final states of closed plans are post-fold by construction: matches there are dominated by prose DESCRIBING the defect class, not instances of committing it. Frequency measured on final states answers 'how often do plans discuss this?' and is misread as 'how often do plans commit this?'. Use final states to price the FALSE-POSITIVE surface and intermediate revisions to price TRUE positives — and never blend the two populations into one accuracy figure."),

rule(90, 305, "At every verdict gate, compare the steps table against commits and deposits",
"`pause_for_verdict` is a header contract the runtime does not police (FORWARD 46, bellows-owned): an agent can execute every step in one dispatch while the daemon records one row — and the 'independent' QA step then re-measures its own work minutes later. The authoring half: at EVERY verdict gate, before writing the verdict, compare the `steps` table's recorded progress against the observed commit and deposit counts; a one-step record over a multi-step evidence trail is the signature. Cheap, mechanical, and it restores the independence assumption every re-measure item silently rests on."),

rule(91, 306, "When an independence guard is missing, assess the bias direction before voiding the result",
"The bias an independence check guards against is an author confirming what they hoped. A result that DEMOLISHES the author's prior work is not that failure mode: a negative, self-marked finding backed by row-level re-checkable evidence is worth accepting with the gap recorded, rather than voided and re-run. Assess which direction the missing guard would have pushed before discarding work. Measured: a self-measured census that killed the author's own four drafted checks — zero true positives, 376 false — accepted on spot-checked raw evidence."),

rule(92, 307, "Confirm the known positives are inside a census's population before scanning",
"Precision over a population with no positives in it is unfalsifiable — any matcher scores zero, including a perfect one. Before running a census on a defect class, build the labelled positive set FIRST, from whatever artifact recorded the instances (often the walk register), and confirm those positives are inside the population being scanned. Report recall and precision as a PAIR; a disposition citing one without the other is incomplete. Measured: a census whose scan population excluded both cycles that generated its hypothesis returned an unfalsifiable zero."),

rule(93, 310, "Each mandate names its QA observer inline",
"Mandates live in the DEV step and observers live in the QA step, so every new mandate starts life unpaired — and a constraint with no check that can FAIL on its violation is prose, not a guard. Each mandate names its observing QA item inline at the point of imposition — '(observed by Item 8)' — so an unpaired mandate is visible at writing time rather than a walk later. Then verify the pairing by CONSTRUCTING the violation and confirming the named item reports it. (The lint mechanism detecting unpaired mandates is FORWARD 52, forge-owned; this is the authoring half.) Measured: the same unpaired-mandate class four times across three walks, each fix a lens late."),

rule(94, 314, "Author every task as ordered sub-items from the first draft",
"Every fold appends a sentence to the task it corrects; each sentence is right, and nothing ever removes one — past some length the block stops being an instruction and becomes a passage, and the agent executes part of it. Author every task as ORDERED SUB-ITEMS from the first draft, so a fold lands in a slot rather than at the end of a paragraph. After collapsing a wall of prose, put its region back on the next walk: a re-formed wall means the fix addressed the symptom while the accretion mechanism kept running. (The sentence-count lint mechanism is FORWARD 54, plan_lint-owned; this is the authoring half.) Measured across two cycles, including one wall that re-formed beneath the sub-steps its collapse had just created."),
])

BLOCK_ANCHOR = "*Source: proposal 220, lesson 2026-08-03*"
rep(BLOCK_ANCHOR, BLOCK_ANCHOR + "\n\n" + NEW_RULES.rstrip("\n"), 1, "E1-block-65-94")

rep("### 53. Region-scoped metrics must be computed with scope applied end to end",
"**Gate-behaviour sentences are inherited claims of exactly this class (proposal 226, codified " + D + "):** any sentence asserting what a gate matches, enforces, or rejects is a claim to RE-RUN against the gate's source before it shapes a disposition — inheriting it from a parent plan reproduces the parent's errors with the parent's confidence (measured: a banner-string claim about `gates.py` survived five warm walks, five ACID passes and a lint run because every pass read the assertion instead of running the gate). And a calibration range is a claim about a SAMPLE: record it with its sample size beside the threshold it justifies, so a n=6 range meeting a 16-item batch is visibly thin rather than silently authoritative.\n\n### 53. Region-scoped metrics must be computed with scope applied end to end",
1, "E2-rule52-ext")

rep("### 56. Resume machinery is justified only when the interrupted work is not reproducible",
"**An absence-result check requires a positive control on the same instrument in the same run (proposal 244, codified " + D + "):** when a check's PASSING result is an absence — a zero-difference diff, an empty grep, a no-rows query — that result is indistinguishable from a broken comparison: a bad query, a mismatched sort, a wrong file and an empty read all print the same nothing. Pair every absence-result check with a positive control run on the SAME instrument in the SAME run, demonstrating the instrument can detect a difference it is claimed to be sensitive to.\n\n### 56. Resume machinery is justified only when the interrupted work is not reproducible",
1, "E3-rule55-ext")

rep("### 57. Generalizing a guard: keep the mechanism generic, require the caller to pin the specifics",
"**Walk the RESUME path before the crash path (proposal 230, codified " + D + "):** for any new durability artifact, a write that is correct on a fresh run is a CLOBBER on a re-run unless it is explicitly non-destructive — a dispatcher that re-runs a dead step from the top will rewrite the before-image with post-mutation values, destroying exactly the state the artifact exists to preserve. The durable posture: if the artifact already exists, cite it as authoritative rather than rewriting it.\n\n**A backup and the write it inverts are adjacent (proposal 243, codified " + D + "):** nothing that can touch the same store may sit between them, and each backup states which SINGLE write it inverts. A backup separated from its write by other work spans a window in which another process may legitimately write the same store — correct at snapshot time, wrong at restore time. Adjacency also strengthens an unrelated guard: an unexplained backup becomes evidence of an attempted mutation rather than ignorable residue.\n\n### 57. Generalizing a guard: keep the mechanism generic, require the caller to pin the specifics",
1, "E4-rule56-ext")

rep("### 62. Establish that a recovered-from state is reachable before authoring recovery machinery",
"**Every pin ships its extraction command (proposal 240, codified " + D + "):** a pinned value whose extraction method is unstated fails closed on honest work — a verifier extracting any other way computes a different value and reports a mismatch on work that is entirely correct (measured twice in one artifact, plus a row-count baseline that varied by four depending on unstated counting rules). Ship the EXACT extraction command beside the pinned value, and confirm the method is portable across tool builds before pinning with it.\n\n### 62. Establish that a recovered-from state is reachable before authoring recovery machinery",
1, "E5-rule61-ext")

rep("### 63. Read the DELIVERY code before theorising about non-arrival",
"**A bypass branch enumerates every downstream reader of what it skips (proposal 269, codified " + D + "):** when adding a bypass or recovery branch, enumerate every downstream consumer of the bypassed block's outputs — each needs the branch to supply an equivalent, or the branch is correct about the PAST and silent about the FUTURE (measured: a recovery branch skipped the commit block where DOC_SHA gets pinned, and the QA step consumed DOC_SHA unconditionally — the exact death-state the branch was built for would have reached QA missing the value QA halts without). Test the recovery path's artifacts against the CONSUMER'S checks, not the happy path's.\n\n### 63. Read the DELIVERY code before theorising about non-arrival",
1, "E6-rule62-ext")

rep("Source: proposal 149, lesson 2026-07-16",
"**Every number a plan states is produced by the plan's own mandated method (proposal 250, codified " + D + "):** a number obtained any other way is a prediction wearing a measurement's clothes and carries the same verify-clause obligation — measured: a count taken without the mandated strip method overstated by half, and the wrong count was taken by a fresh cold reader who had JUST read the strip rule. The corollary: a discipline reapplied at many call sites belongs INSIDE the instrument (the script, the query, the one-liner), not left for each caller to remember.\n\nSource: proposal 149, lesson 2026-07-16",
1, "E7-checklist29-ext")

rep("**Version:** 4.85", "**Version:** 4.86", 1, "E8-version")
rep("**Last Updated:** 2026-08-08 (v4.85)", "**Last Updated:** 2026-08-11 (v4.86)", 1, "E9-lastupdated")

CHANGELOG_ROW = ("| 2026-08-11 | v4.86: Gate 2 batch 2 (gate2-template-batch-2026-08-11) — 37 proposals codified, the largest corpus batch to date "
"(21 routed by the 2026-08-09 gate via plan 326, 16 by the 2026-08-11 gate via plan 342; all 37 flipped accepted-to-implemented by this plan). "
"Thirty NEW rules 65-94, appended in proposal-id order as one contiguous block (223, 225, 228, 229, 236, 239, 242, 255, 257, 264, 265, 266, 267, 268, "
"274, 277, 280, 281, 282, 284, 288, 289, 293, 297, 303, 305, 306, 307, 310, 314). Seven EXTENSIONS: Rule 52 gains gate-behaviour-claims-are-re-run-claims "
"plus calibration-with-sample-size (226); Rule 55 gains the absence-result positive-control requirement (244); Rule 56 gains resume-path-before-crash-path (230) "
"and backup-write adjacency (243); Rule 61 gains ship-the-extraction-command (240); Rule 62 gains the bypass-branch downstream-reader enumeration (269); "
"Checklist #29 gains numbers-by-mandated-method-only plus disciplines-inside-the-instrument (250). Rule-46 splits recorded where proposals carried them: the "
"bellows-owned halves of 274 (verdict channel), 289 (verdict grammar), 305 (pause_for_verdict enforcement, FORWARD 46) and the forge/lint-owned mechanisms of "
"310 (FORWARD 52) and 314 (FORWARD 54) are NOT codified here — each rule's text names its split. Numbering append-only per the 4.83 precedent (63/64). |")
rep("| Date | Lesson |\n|---|---|\n", "| Date | Lesson |\n|---|---|\n" + CHANGELOG_ROW + "\n", 1, "E10-changelog")

io.open(DST, 'w', encoding='utf-8').write(s)
print(f"OK — {len(edits_applied)} edits applied: {', '.join(edits_applied)}")
