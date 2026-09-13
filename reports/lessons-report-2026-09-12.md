# Lessons Report — 2026-09-12


## Summary


| Category | Count |
|---|---|
| governance_rule | 95 |
| instrumentation | 4 |
| narrative | 1 |
| structural | 22 |

**Total proposals:** 122


## Governance Rule


### 2026-09-12: A STATIC TEST'S PARSER IS AN INTERPRETER — A VERSION-COMPATIBILITY TEST RUNS UNDER THE OLDEST INTERPRETER THE SHOP RUNS, AND CHECKS IMPORT AS WELL AS PARSE [tag: verification] [tag: test-infrastructure]


- **Suggested action:** Add test rule: version-compatibility tests name the interpreter they run under, run the oldest shop interpreter (currently Python 3.9.6), and check import as well as parse; each interpreter gap fix is verified by running the suite under the old interpreter, not by the new test alone
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a test standard: 'a test whose subject is version compatibility names the interpreter it runs under, runs the oldest one the shop runs, and checks import as well as parse.' Tests that passed on 3.12 would fail on 3.9 four times over; a parse fix uncovers the import failure that the parse failure masked.
- **Confidence:** high

### 2026-09-12: A LIVENESS TEST MUST READ A SIGNAL THE DEATH REMOVES — AN ARTIFACT THE DEAD RUN LEAVES BEHIND, OR A HEARTBEAT AT THE WRONG GRAIN, READS "LIVE" FOR EXACTLY THE FAILURE IT EXISTS TO CATCH [tag: verification] [tag: bellows-design]


- **Suggested action:** Add rule: before trusting a liveness discriminator, name the death it must detect and verify the property it reads changes at that death; use pid, run-authored heartbeat, or a process-held lock — not files the run created or the host's heartbeat; give the discriminator a test in which the run dies and its artifacts stay
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a liveness-testing rule: 'before trusting a liveness discriminator, name the death it must detect and check that the death changes the property read.' Two discriminators (worktree presence, claim heartbeat) survived the death they were meant to detect. The fix is a governance rule about liveness design and testing.
- **Confidence:** high

### 2026-09-12: RIDER on `A session that crosses midnight carries a stale date into every slug it authors` (2026-08-14) — A LOG NAMED FOR ITS START DATE CROSSES MIDNIGHT TOO: A TIME-OF-DAY MATCH WITHOUT THE DATE MIXES TWO DAYS INTO ONE STORY [tag: operational-recovery]


- **Suggested action:** Add rule: in a log with time-only stamps, anchor every reading to a known event of the day by line number before calling anything today's; a time-of-day match never stands for a timestamp in a log that crosses midnight
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A session that crosses midnight carries a stale date into every slug it authors' (2026-08-14). Entry extends the parent: a daemon log named for its start date carries multiple days of time-only lines; a time pattern grep returned two blocks from different days and the older one was read as current.
- **Confidence:** high

### 2026-09-12: RIDER on `A test written by the author of the code inherits the author's model — move the ORACLE outside it, or the suite can only confirm the bug` (2026-08-27) — THE MUTANT SET INHERITS IT TOO: A CONFIRM-THEN-ACT CONTROL SPECIFIED WITH ONLY ITS CANCEL TEST PASSES A CLEAN MUTATION RUN [tag: verification]


- **Suggested action:** Add test rule: a confirm-then-act control requires tests on both branches — cancel proves nothing happens without consent, confirm proves the act happens; the mutant set must include one that deletes the act itself, which only the positive test can kill
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A test written by the author of the code inherits the author's model — move the ORACLE outside it, or the suite can only confirm the bug' (2026-08-27). Entry extends the parent: a release-key handler had only the cancel test; the mutant set, sharing the same author's model, never included a mutant that deleted the release call.
- **Confidence:** high

### 2026-09-12: RIDER on `RUN THE WHOLE SUITE UNDER THE CHANGE AT DRAFTING, IN A SCRATCH ARCHIVE — THE ONE TEST A PROMOTION BREAKS IS A FOLD AT WALK 1, NOT A MUST-PRESERVE VIOLATION AT DEV` (2026-09-10) — A CROSS-REPO PLAN INHERITS THE HOST TOOLS' PATH CONVENTIONS: RUN EVERY GATE COMMAND THE PLAN WILL RUN, AT ITS OWN ENTRY POINT, AGAINST A SCRATCH ARCHIVE OF THE TARGET REPO [tag: verification] [tag: drafting-cycle]


- **Suggested action:** Add drafting rule: for cross-repo plans, run every gate command the plan will invoke (pre-check, mutation tool, observer) against a scratch archive of the target repo with the plan's own paths before deposit; a host tool's path pattern is an interface the target repo never agreed to
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'RUN THE WHOLE SUITE UNDER THE CHANGE AT DRAFTING, IN A SCRATCH ARCHIVE — THE ONE TEST A PROMOTION BREAKS IS A FOLD AT WALK 1' (2026-09-10). Entry extends the parent to gate commands in cross-repo plans: a tuyere plan's pre-check would have refused its first commit because bellows' path convention differs from tuyere's.
- **Confidence:** high

### 2026-09-12: WALK 0 DIFFS v0 AGAINST THE STANDING RULES — A FOLD THAT ADDS A COMMAND ESCAPES THAT DIFF, SO EACH COMMAND A FOLD ADDS GETS THE DIFF AT THE FOLD [tag: drafting-cycle]


- **Suggested action:** Add walk rule: a command added or changed by a fold is treated as new v0 for standing-rules diff purposes; the fold's register row names which rules the new instruction was checked against (CLAUDE.md, plan preamble, cited lessons)
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a walk discipline rule: 'an instruction a fold adds is new v0 for that diff's purpose. When a fold adds or changes anything an executor runs... enumerate the rules it could cross... and check the new instruction against each at the fold.' Walk 0's standing-rules diff covered v0; a fold-added proof violated LESSONS 2026-09-09 and three lenses missed it.
- **Confidence:** high

### 2026-09-12: A COPY OF LIVE STATE INCLUDES THE PROCESS THAT TOOK IT — A TOOL THAT REFUSES WHILE ANY PLAN IS IN FLIGHT REFUSES ON THE COPY ITS OWN PLAN'S QA TAKES [tag: verification] [tag: planning]


- **Suggested action:** Add rule: when a step exercises a guarded tool on a copy of live state, list what the copy holds at snapshot time (the step's own in-flight row first); write the edit the copy needs beforehand, or give the tool a way to exclude the caller; never leave the executor to improvise the fix
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a step-authoring rule: 'a snapshot of live state is taken by a running process and carries that process's own record — its in-flight row, its lock, its claim — so any guard read off the snapshot sees the caller.' A QA that rehearsed a guarded tool on a backup of the live DB hit the refusal its own plan triggered.
- **Confidence:** high

### 2026-09-11: A PER-STEP TABLE IS ONLY AS FINE AS ITS WRITE SITE — A LIFECYCLE ROW WRITTEN AT THE MERGE CARRIES THE MERGE STEP'S KEY, SO READ WHERE A ROW IS WRITTEN BEFORE READING IT PER STEP [tag: verification] [tag: bellows-integration]


- **Suggested action:** Add rule: before reading a table's rows as per-key records, read the write site and its context; document the actual granularity in the tool's limits section; calibrate on instances from both arms before trusting a classifier
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a data-interpretation discipline: 'before a table is read per key, the write site is read — the key is as fine as the context that wrote it.' A census read the lifecycle commits table as per-step when it is actually per-plan, with a step column showing current step at merge time. The fix is a governance rule about reading data sources.
- **Confidence:** medium

### 2026-09-11: THE TOOL'S TALLY IS THE RECORD'S TALLY — A CLOSING LINE THAT COUNTS FOLDS BY HAND DISAGREES WITH THE MANIFEST THE CLOSE TOOL SPLICES; READ THE DRY RUN'S SPLICE, THEN WRITE THE CLOSING TEXT FROM IT [tag: planner-discipline] [tag: drafting-cycle]


- **Suggested action:** Add Planner rule: when a tool emits the number the record will carry, the prose quotes the tool's number (via --dry-run or equivalent), never a hand tally of the same thing; two counts of one quantity in one document is an ACID finding
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a Planner rule: 'when a tool emits the number the record will carry, the prose quotes the tool's number after reading it (a `--dry-run` shows the splice), never a hand tally.' Two closes had to be re-run because the closing line hand-tallied yields under a different counting rule than the close tool's.
- **Confidence:** high

### 2026-09-11: RIDER on `SHELL SPLITTING AND CWD ARE ENVIRONMENT` (2026-09-10) — A SCRIPTED PER-LENS CHAIN'S FIRST SILENT FAILURE RESHAPES EVERY LATER STEP: READ EACH LENS COMMIT'S `--stat` BEFORE THE NEXT LENS, AND HOLD NO TOOL PATH IN ONE SHELL WORD [tag: planner-discipline] [tag: drafting-cycle]


- **Suggested action:** Add rule: in a scripted per-lens chain, every path is absolute and every lens commit's --stat is read before the next lens runs; a chain's first silent failure (wrong path, wrong interpreter) reshapes every later step
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'SHELL SPLITTING AND CWD ARE ENVIRONMENT' (2026-09-10). Entry extends the parent from foreground single commands to scripted per-lens chains: the register rows appended but the folds did not when the tool path was held in a one-word variable. The fix is a governance rule about chain discipline.
- **Confidence:** high

### 2026-09-11: A DEPOSIT THAT SAYS "VERBATIM" IS READ TO ITS LAST LINE — THE (b) CHECK READS THE APPENDIX, NOT THE HEADINGS, AND A SCRIPT THAT LIVES ONLY UNDER `$T` IS GONE WHEN THE STEP'S TEARDOWN RUNS [tag: verification] [tag: planner-discipline]


- **Suggested action:** Add rule: a 'verbatim', 'whole', or 'all N' claim in a deposit is verified by the last line or byte count at the (b) read, not by the section heading; an instrument the doc must carry is written into the doc before the teardown item runs, with a post-condition naming the line count
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes two governance rules: the reader verifies verbatim claims to the end, and the author embeds instruments before teardown with a countable post-condition. A 12-line header claiming verbatim was accepted; the 281-line script was gone after the teardown item removed $T.
- **Confidence:** high

### 2026-09-11: RIDER on `SHELL SPLITTING AND CWD ARE ENVIRONMENT` (2026-09-10) — A BACKGROUND WATCH INHERITS THE CWD OF THE MOMENT IT WAS LAUNCHED, AND AN EMPTY READ IS NOT "GONE": NAME EVERY PATH ABSOLUTELY AND TREAT NO OUTPUT AS NO SIGNAL [tag: planner-discipline]


- **Suggested action:** Add rule for background watches: name interpreter, script, and every file absolutely (not CWD-relative); logic distinguishes three states — condition seen, condition not seen, and nothing read (empty read is not 'gone'); a confirmation step using the same broken read confirms nothing
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'SHELL SPLITTING AND CWD ARE ENVIRONMENT' (2026-09-10). Entry extends the parent from foreground chains to background polls: a watch launched from a moved CWD read empty strings that matched 'gone', and a running plan was reported as finished. The fix is a governance rule for watch-script authoring.
- **Confidence:** high

### 2026-09-11: A "MANUAL ACT" IS OFTEN A CODE PATH WITH THE WRONG PARENT — BEFORE DESIGNING A REMOTE MECHANISM, READ WHETHER THE VERB EXISTS AND WHAT OWNS THE PROCESS [tag: verification] [tag: bellows-architecture]


- **Suggested action:** Add planning rule: before designing a remote mechanism for a 'manual act', measure the process tree (who spawned it, what session it lives in, what restarts it); the verb usually exists and the missing piece is only parentage
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a planning discipline: 'when an act is described as manual, measure the process tree before the design.' The daemon restart was manual only because the respawn ran in the caller's session; the fix was a launchd parent and an existing CLI verb, not a new mechanism. The action is a governance planning rule.
- **Confidence:** medium

### 2026-09-11: AN OLD THREAD'S ITEMS ARE MEASURED AGAINST TODAY'S DOCTRINE BEFORE ANY IS DRAFTED — A CHECK THE RECORD LATER MADE STANDARD PRACTICE IS RETIRED, NOT BUILT [tag: planner-discipline] [tag: process-discipline]


- **Suggested action:** Add Planner rule: before drafting from a thread, grep each item against the live tool and template changelog; items contradicted by newer rules are retired (not built); dispositions recorded in the plan as rulings on evidence
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a thread-aging rule: 'a thread ages against the doctrine, and an item that a newer rule contradicts is not a smaller build — it is a retired item.' A 2026-08-26 thread's items were measured against 2026-09-11 doctrine; two had shipped, one was already covered, two contradicted current standards. The fix is a governance rule.
- **Confidence:** high

### 2026-09-11: RIDER on `A STATUS READER IS TESTED IN THE STOPPED STATE IT EXISTS TO REPORT — A READ-ONLY OPEN OF A WAL DATABASE FAILS WHEN NO WRITER HOLDS IT` (2026-09-11) — THE FAILURE IS A VERSION FACT: A PREMISE IS MEASURED UNDER THE INTERPRETER THE PLAN MANDATES, AND THE PIN NAMES THE INTERPRETER AND THE LIBRARY VERSION [tag: verification] [tag: plan-authoring]


- **Suggested action:** Add rule: a premise about library behavior is a version fact; the pin names interpreter path and library version beside the value; measurement is always under the interpreter the plan mandates; when a premise holds on one version only, the plan states so and version-gates the mechanism
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A STATUS READER IS TESTED IN THE STOPPED STATE IT EXISTS TO REPORT — A READ-ONLY OPEN OF A WAL DATABASE FAILS WHEN NO WRITER HOLDS IT' (2026-09-11). Entry extends the parent with the version-fact rule: the WAL failure holds for SQLite 3.43.2 but not 3.51.0 or 3.53.4. The Planner measured under the system interpreter without naming it.
- **Confidence:** high

### 2026-09-11: ISOLATION HOLDS ONLY FOR CODE THAT HONOURS IT — A TEST OR A READ-ONLY STEP REACHES WHATEVER ITS CALLEES NAME ABSOLUTELY, SO THE CHECK IS ON THAT RESOURCE, NOT ON THE SANDBOX [tag: verification] [tag: test-hygiene]


- **Suggested action:** Add rule: before a test or read-only step invokes a callee, enumerate what the callee names absolutely (launchd labels, ports, canonical paths, live DBs); check those resources before and after the step, not only the sandbox; isolation from tmp_path or worktree applies only to code that takes its paths from them
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a test and read-only step discipline: 'Before a test or a read-only step invokes a callee, read what the callee names absolutely.' A smoke test kickstarted the live daemon via launchd; a census diagnostic appended to committed files via absolute paths. Both violated isolation by reaching resources the sandbox does not cover.
- **Confidence:** high

### 2026-09-11: A RE-DERIVATION THAT NAMES A MACHINE THE STEP NEVER REACHED IS AN INVENTION — AT THE VERDICT READ EVERY FIGURE IS TRACED TO THE COMMAND THAT PRINTED IT [tag: verification] [tag: planner-discipline]


- **Suggested action:** Add rule: at the (b) read, every figure in a re-derivation is matched to the command in the step's transcript that printed it; a figure with no command is struck and corrected before any continue or override; pin rows for surfaces the step cannot reach are marked 'Planner-measured, not re-derived by the step'
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a verdict-read discipline: 'a record takes only what its step measured.' A DEV wrote the first machine's SQLite version for the second machine's row without ever ssh-ing there. The false figure reached the verdict read and would have become version-gate evidence. The fix is a governance rule about re-derivation and (b) reads.
- **Confidence:** high

### 2026-09-10: A SHIPPED TOOL'S ACCEPTANCE COVERS THE CASES ITS OWN TESTS CHOSE — RUN IT ON THE COMMON CASE THE PLAN'S PROSE NAMES BEFORE ISSUING CONTINUE, BECAUSE THE FIRST REAL USE IS THE TEST THE QA DID NOT WRITE [tag: verification]


- **Suggested action:** Add QA rule: before a continue verdict on a plan that ships a tool, run the tool once on the ordinary case named in the plan's prose; refuse the verdict when the tool refuses on that case; the (b) check reads the QA's choice of cases, not the tool itself
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a verdict discipline: 'before a `continue` on a plan that ships a tool, run the tool once on the case the plan's What this changes names as the ordinary one.' The first real use of lens_commit.py on a folded walk failed because no test or QA replay covered that case.
- **Confidence:** high

### 2026-09-10: RIDER on `A FORCE-CLASSIFIED TEST TABLE IS A RULING — RED CELLS ARE IT SPEAKING` (2026-09-06) and its 2026-09-07 rider — THE RATIFIED TEST WAS RIGHT ABOUT THE DESIGN AND WRONG ABOUT ITS PREMISE, AND THE RECORD ALREADY HELD THE CORRECTION: READ THE RATIFYING PLAN'S PREMISE LINE AND GREP THE DOCTRINE HISTORY FOR ITS REVERSAL BEFORE RULING [tag: planner-discipline]


- **Suggested action:** Add Planner rule: before ruling on or refactoring a pinned behavior, read three things in order — the ratified test, the ratifying plan's premise sentence, and the doctrine/register history for any later correction of that premise; a design whose premise the record has since falsified is 'un-reconciled', not a defect
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A FORCE-CLASSIFIED TEST TABLE IS A RULING — RED CELLS ARE IT SPEAKING' (2026-09-06) and its 2026-09-07 rider. Entry extends the parent with a concrete three-step read sequence: ratified test, premise line, doctrine history for reversal. The fix is a documentary rule change to Planner discipline.
- **Confidence:** high

### 2026-09-10: A LINT FAIL ROW'S LETTER IS A ROUTING KEY, NOT A LABEL — CHOOSE A ROW'S STATUS BY READING EVERY CONSUMER OF ITS TEXT, AND NEVER REUSE A RETIRED LETTER [tag: verification] [tag: planner-discipline]


- **Suggested action:** Add rule: before promoting or adding a lint row letter, enumerate every consumer of the exit and row text, read each consumer's filter, and pick a letter outside all filters; check the letter's git history (git log -S) because a retired letter carries its failure record
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a lint-maintenance rule: 'Before promoting, changing or adding a lint row: enumerate every reader of the exit AND of the row text... and pick a letter outside every filter.' A promoted WARN would have been swallowed by the release arm's filter. The fix is a governance rule about lint row design discipline.
- **Confidence:** high

### 2026-09-10: THE COLD PANEL IS LICENSED BY A DRY WALK, THE LENS-4 SIGNAL, OR THE CEO'S CALL — READ A PRECEDENT'S YIELDS BEFORE COPYING ITS SEQUENCE [tag: drafting-cycle] [tag: planner-discipline]


- **Suggested action:** Add drafting cycle rule: a cold panel is licensed only by a dry walk, the lens-4 signal, or the CEO's call; copy a precedent's condition (the measured yield that licensed it), not its shape
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a rule about drafting cycle panel sequencing: 'A panel was convened... because the previous cycle's shape... was copied; that cycle's second walk had yielded ZERO, which is what licensed its panel.' The fix is a documentary rule in DRAFTING_CYCLE or PLANNER_TEMPLATE naming the three licenses.
- **Confidence:** high

### 2026-09-10: A TOOL'S EXIT IS THE ACT'S RESULT — NEVER PIPE IT AWAY, NEVER CHAIN THE NEXT ACT PAST IT, AND ISSUE A VERDICT ONLY AFTER ITS CHECK HAS BEEN READ [tag: planner-discipline] [tag: verification]


- **Suggested action:** Add Planner rule: run every tool bare and read its exit code before the next act; a verdict is its own call authored only after reading the check's printed output; a close is confirmed by its 'commit OK' line before the receipt exists; a deposit on bytes no commit holds is withdrawn
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes four Planner discipline rules derived from four same-day slips: not piping tool output away, reading exit before chaining, issuing verdicts only after reading check output, and not depositing before commit. All are documentary governance rule changes.
- **Confidence:** high

### 2026-09-10: RIDER on `A PROBE'S LOCATION IS PART OF ITS ENVIRONMENT` (2026-09-02) — SO ARE THE SHELL'S WORD-SPLITTING AND THE PROCESS CWD: zsh PASSES AN UNQUOTED VARIABLE OF SEVERAL ASSIGNMENTS AS ONE WORD, AND A RESOLVER'S CWD FALLBACK READS THE CANONICAL TREE THROUGH AN ARCHIVE [tag: verification]


- **Suggested action:** Extend probe-environment rule: pass multi-assignment env vars explicitly or via ${=VAR} under zsh (not bare $VAR); run probes from a directory that holds none of the artifacts, or read the tool's BASIS before believing a zero result
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A PROBE'S LOCATION IS PART OF ITS ENVIRONMENT' (2026-09-02). Entry extends the parent rule to cover shell word-splitting (zsh passes unquoted multi-assignment as one word) and CWD fallbacks in resolvers. The fix is a documentary rule extension for the probe discipline.
- **Confidence:** high

### 2026-09-10: RIDER on `A TRACKED THREAD'S TITLE NAMES THE SUBJECT; ITS BODY NAMES THE DEFECT` (2026-09-06) — A COLD SEAT'S ATTRIBUTION IS A CLAIM UNTIL THE PRODUCER IS READ: FILE THE THREAD FROM THE CODE THAT PRODUCES, AND SUPERSEDE A MISFILED ONE [tag: planner-discipline] [tag: verification]


- **Suggested action:** Add rule: before filing a thread from a seat's or census's attribution, grep the code that produces the effect (grep the call, not the name); when a filed thread is found misfiled, supersede it with a thread naming the measured producer rather than editing the plan around it
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A TRACKED THREAD'S TITLE NAMES THE SUBJECT; ITS BODY NAMES THE DEFECT' (2026-09-06). Entry extends the parent with the attribution-verification step and the supersede rule. Two seats attributed to 'test_11_gate_watcher' when the actual producer was 'test_16_hold_prefix_receipt_satisfies_check'.
- **Confidence:** high

### 2026-09-09: A REFUSAL CLASS JUST HIT IS THE ONE THE NEXT SCRIPTED LOOP REPRODUCES — PUT THE CHECK INSIDE THE LOOP, BEFORE THE COMMIT, NOT IN THE OPERATOR'S MEMORY [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a refusal class just hit during a walk must be incorporated as an inline check in the next scripted loop for the same artifact, placed before the commit; the check must not live only in the operator's memory.
- **Reasoning:** [AUTHOR-CONFLICT] A register lint refused a walk-5 row (truncated_pre_fold_text: quoted plan ellipsis without verbatim-ellipsis marker); the fix was applied. The walk-6 script, written minutes later by the same planner, quoted two more rows without the marker and the commit hook refused again — each time five lenses had been applied with no commit landed, requiring a full reset and re-application.
- **Confidence:** high

### 2026-09-09: AN OBSERVER THAT READS SUBJECTS CANNOT SEE A SHIFTED SUBJECT — A COMMIT LOOP ASSERTS THAT EACH MESSAGE NAMES THE UNIT IT COMMITS, AND A SUBJECT-ONLY CHECK IS NECESSARY, NOT SUFFICIENT [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a commit loop that applies lenses must assert the commit message contains the expected lens token before issuing the commit; a subject-only check by an external observer (lens_order_check) is not sufficient to detect a shifted index.
- **Reasoning:** [AUTHOR-CONFLICT] A 1-indexed shell caused a commit message array to shift by one — the lens-1 commit's subject was its trailer line, each later commit named the previous lens. lens_order_check read OK (reads subjects, ascending) while every record was wrong. The loop's own guard ([[ $MSG == *'lens $i'* ]] before committing) caught the same shape on the next walk.
- **Confidence:** high

### 2026-09-09: A COLD SEAT'S MANDATE FORBIDS EVERY WRITER BY NAME, AND A SCRATCH SCRIPT OUTSIDE `tests/` HAS NO CONFTEST — "READ-ONLY" IS NOT A PERMISSION THE SEAT CAN INFER FROM AN IMPORT LIST [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a cold seat granted 'read-only' permission must not run lifecycle functions in-process in any script outside tests/; 'read-only' cannot be inferred from an import list — conftest.py's isolation fixture does not apply outside tests/ and any invocation writes to the production database.
- **Reasoning:** [AUTHOR-CONFLICT] A cold panel execution seat was told 'read-only; never touch lifecycle.db' and also 'you MAY import lifecycle functions in-process in tests'. It cloned the lifecycle test into a scratch script outside tests/, bypassing conftest.py's autouse fixture; lifecycle.LIFECYCLE_DB_PATH was the production path; run_plan minted real plan 100051 in the live lifecycle.db.
- **Confidence:** high

### 2026-09-09: A CONSUMER OF A SHARED LIST CAN DEPEND ON ITS LENGTH WITHOUT NAMING A MEMBER — ENUMERATE CONSUMERS BY THE LIST'S EFFECTS (ROW COUNTS, TABLE SIZES), NOT ONLY BY GREPPING ITS MEMBERS [tag: planning]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when changing a shared list, enumerate consumers by the list's effects (row counts, table sizes, any literal that equals the list's length) in addition to grepping member names; a consumer that asserts a COUNT without naming a member is invisible to a name-only grep.
- **Reasoning:** [AUTHOR-CONFLICT] Two plans in two days each missed a test consumer of a changed list: 100045 rewrote a gate's message and missed tests asserting the old string (recorded 2026-09-08); 100052 lengthened lifecycle.standard_gates by two and missed a test that asserted the per-step gate-row COUNT as the literal 10 and named no gate. Both author and cold seats had enumerated consumers by grepping gate names.
- **Confidence:** high

### 2026-09-09: THE ACT'S OWN OUTPUT LINE IS THE RECORD'S SOURCE — A LATER LISTING, OR A RE-TYPING THROUGH A SHELL, IS A SECOND ACT THAT CAN DIFFER [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md (rider to 'write records from the act's output'): the act's own output line is the only authoritative source for an ID or record; a later listing is a second act that can differ — IDs must be captured at emission, not re-derived; body text containing shell-executable tokens must bypass shell substitution.
- **Reasoning:** [AUTHOR-CONFLICT] Two forms in one hour: (1) threads add printed 'thread 242 opened'; the script re-derived from 'threads list | grep | tail -1' (not sorted by id) and got 240, writing a wrong pointer; (2) a thread body typed inline with a backticked command had the command shell-substituted and the stored body read partial garbage. Both show that re-derivation or inline shell evaluation is a second act distinct from the original.
- **Confidence:** high

### 2026-09-09: AN "UNCHANGED FILE" PROMISE IS A PROMISE ABOUT THE ENVIRONMENT TOO — A WORKTREE TEST CAN IMPORT THE CANONICAL CHECKOUT'S MODULE, SO A PLAN THAT EDITS AN IMPORTED SCRIPT NAMES THE BINDING CHECK [tag: planning] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: an 'UNCHANGED file' declaration covers both the file's content AND its import binding in the execution environment; if the file is imported through a path resolver that may pull from the canonical checkout, declare it as a scope item and add an evict-and-reimport guard in the DEV step.
- **Reasoning:** [AUTHOR-CONFLICT] Plan 100053 changed scripts/substrate_check.py and declared tests/test_substrate_check.py as UNCHANGED. In the daemon's worktree, depositor.py put the canonical checkout's scripts/ at sys.path[0], so the test imported the main branch's module — the worktree's edit was untestable. The fix required an evict-and-reimport shim inside the 'UNCHANGED' test file, which required declaring it as a scope item.
- **Confidence:** high

### 2026-09-09: THE RECORD HALF OF A DEV STEP IS A GATED DELIVERABLE — WHEN THE NEW GATE CATCHES IT, HALT AND REWRITE THE RECORD FROM THE RUN'S OWN TRANSCRIPT; NEVER OVERRIDE A GATE ON ITS FIRST CATCH [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md (strengthening the existing gate-override rule): the record half of a DEV step is a gated deliverable; when a gate fires on its first live catch, halt and rewrite the record from the run's own transcript; never override a gate on its first catch.
- **Reasoning:** [AUTHOR-CONFLICT] Plan 100054's code was correct (15 tests, 7 mutants, suite green) but the dev-log had five generic headings instead of the five declared; six dev_log_declared_text failures — the gate's first live catch of the class it was built for that morning. The CEO halted rather than override; the follow-up (100055) rewrote from the transcript. 'THE RECORD HALF OF A DEV STEP IS A GATED DELIVERABLE.'
- **Confidence:** high

### 2026-09-09: A PARSED HEADER FIELD IS A GRAMMAR, NOT A SENTENCE — PROSE IN `**Discharges:**` IS EITHER REFUSED OR PARTIALLY MATCHED, AND A PARTIAL MATCH ENQUEUES A REAL INTENT [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: parsed header fields (Discharges:, etc.) must use the exact grammar — id-only, no surrounding prose; prose in a parsed field is either refused or partially matched; if no discharge, leave the field empty or omit it.
- **Reasoning:** [AUTHOR-CONFLICT] Plan 100056 wrote 'Discharges: none — thread 81 stays open' to explain itself to a reader. gates.parse_discharges found the token 'thread 81' inside the prose, discharged thread 81 (unintended), and enqueued a thread.review-discharge intent for a thread the plan had not discharged. 'A PARSED HEADER FIELD IS A GRAMMAR, NOT A SENTENCE.'
- **Confidence:** high

### 2026-09-09: A CHECK THAT ONLY THE CONSUMER RUNS IS READ AFTER THE PRODUCER'S WHOLE COST IS SPENT — WHEN A GATE CATCHES TWICE, ITS FUNCTION BELONGS IN THE PRODUCER'S OWN LOOP [tag: verification] [tag: process-discipline]


- **Suggested action:** Add rule: a gate or lint that reads a deposit must be invoked by the deposit's author before the deposit; the DEV's commit line chains the gate function (e.g., tools/check_deposit.py) before git-add; the Planner runs the register lint at each walk close, not only at the fold
- **Reasoning:** [AUTHOR-CONFLICT] Entry explicitly proposes Planner and DEV discipline: 'a gate or lint that reads a deposit is invoked by the deposit's AUTHOR before the deposit — the DEV's commit line chains the gate's function the way it chains the full suite.' The fix is a documentary rule change, not a mechanical code change.
- **Confidence:** high

### 2026-09-09: RIDER on `A SELF-READING INSTRUMENT AT A CLOSE MUST RUN AFTER THE ARTIFACT REACHES THE STATE IT WILL DEPOSIT` (2026-09-08) — RECURRED: THE EMITTER RAN BETWEEN THE CLOSING REWRITE AND THE BASELINE SAVE, AND THE SPLICE THAT SHOULD HAVE CARRIED ITS LINES FAILED SILENTLY ON THE EMITTER'S OWN HEADER [tag: drafting-cycle]


- **Suggested action:** Formalize close sequence as fixed: closing lines written → baseline saved → emitter run → lines spliced by key (regex on ^key: ) → baseline saved again → STORED==LIVE diff gate before commit; commit subject naming an act is written after the act's own check passes
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A SELF-READING INSTRUMENT AT A CLOSE MUST RUN AFTER THE ARTIFACT REACHES THE STATE IT WILL DEPOSIT' (2026-09-08). Entry proposes a fixed mechanical close sequence and the rule that the splice regex must be tolerant of the emitter's framing header. The fix is a documentary rule change to the close procedure.
- **Confidence:** high

### 2026-09-09: A POST-CONDITION IS A COMMAND — RUN IT AT THE CLOSE OVER WHATEVER ARTEFACT ALREADY EXISTS, BECAUSE A SENTENCE CAN CONTRADICT ITS OWN INSTRUCTION AND THREE DRY WALKS WILL NOT SEE IT [tag: planning] [tag: verification]


- **Suggested action:** Add Planner rule: every post-condition naming a command is RUN at the close over whatever artifact exists at that moment, with output pasted beside it; a post-condition with no runnable command is rewritten until it has one
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a Planner discipline rule: 'every post-condition that names a command is RUN at the close over whatever artefact exists at that moment (the instrument, a prior plan's deposit of the same shape, a scratch file with the declared property) and its output pasted beside the sentence.' This is a documentary governance rule change.
- **Confidence:** high

### 2026-09-09: PRICE AN ANALYSIS TOOL AGAINST THE TRIVIAL BASELINE ON THE KNOWN INSTANCE BEFORE WIRING IT INTO A GATE — A GRAPH WITH 0–45% EDGE PRECISION LOST TO `git grep -w` ON THE ONE MISS THE SHOP HAD [tag: verification] [tag: planning]


- **Suggested action:** Add planning rule: before wiring an analysis tool into a gate, benchmark it against the trivial baseline (grep, git log, one-line AST walk) on a known instance; measure precision on the highest-count output; read the tool's schema for what is NOT a node before trusting a recall claim
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a pre-gate evaluation discipline: 'before an analysis tool's output becomes a gate input, run the trivial baseline... on the same known instance and report both — adopt the tool only for the question the baseline cannot answer.' The action is a planning/governance rule, not a mechanical code change.
- **Confidence:** medium

### 2026-09-09: A PLAN THAT NAMES THE CANONICAL CHECKOUT FOR READS INVITES A WRITE THERE — STATE EVERY DEPOSIT AS "IN THIS WORKTREE" OR THE DEV WRITES BOTH, AND THE TEARDOWN REFUSES ITS OWN DUPLICATE [tag: planning] [tag: bellows-architecture]


- **Suggested action:** Add rule: any plan instruction pointing another tree for reads must state in the same sentence that every write goes to the current worktree ($(git rev-parse --show-toplevel)); Deposits listed as worktree-relative paths; post-condition includes git status of canonical tree showing nothing new under the deposit's directory
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a plan-authoring rule: 'a plan that points the agent at another tree for READS says, in the same sentence, that every write goes to the worktree it stands in.' The fix is a documentary rule change to prevent a fresh-context agent from resolving write ambiguity toward the named canonical path.
- **Confidence:** high

### 2026-09-09: AN OVERNIGHT DELEGATION IS A NAMED LIST OF ACTS, AND THE ACTS OUTSIDE IT ARE LEFT VISIBLE, NOT ROUTED AROUND — A LANE FILE THAT FREEZES THE LESSONS GUARD IS WITHDRAWN, NOT COMMITTED PAST [tag: process-discipline]


- **Suggested action:** Add rule: an autopilot session under a CEO delegation executes only the named acts; when a step needs an act outside the list, choose the reversible option (withdrawal over commit, pause over override) and record what was withheld in the baton; the delegation text is quoted in every verdict file the session writes
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a governance rule for overnight/autopilot delegation: 'an autopilot session runs only the acts the delegation names and, when a step needs an act outside the list, chooses the reversible option.' The fix is a documentary rule change for delegation protocol.
- **Confidence:** high

### 2026-09-08: A RECORD REQUIREMENT AN AGENT READS IS NOT IN THE CONTROL FLOW — THREE DEV RUNS BENT ONE PASTED CELL THREE WAYS WHILE EVERY GATE PASSED; THE FIX WAS TO MAKE THE ARTIFACT A DEPOSIT [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a record requirement that lives only in prose instruction is not in the control flow — any required verbatim cell must be a named deposit with a path, not an in-step instruction, so gates can verify it.
- **Reasoning:** [AUTHOR-CONFLICT] One plan, three DEV executions: Item 7 said 'record P10', then 'copy the VALUE cell verbatim', then 'paste EXACTLY this inline'. The agent wrote a gloss, then nothing, then a description of something else — and receipt_status, rule_22 and deposit_exists all passed because none reads a semantic cell. The fix (making the artifact a deposit) made the gate verifiable. The lesson is a plan-authoring rule.
- **Confidence:** high

### 2026-09-08: A LANE FILENAME IS THE STATE MACHINE'S INPUT — A DEPOSIT STAGED UNDER THE BARE CLAIMABLE NAME SKIPPED ADMISSION AND HELD AS no_clearance; `ready-` IS THE DEPOSIT ACT [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when depositing a plan into the lane, always use the ready-<slug>.md filename; the bare executable-<slug>.md form is claimable but bypasses admission and auto-holds as no_clearance.
- **Reasoning:** [AUTHOR-CONFLICT] A draft copied as executable-<slug>.md was found by PlanHandler._handle as claimable, but had no clearance row and was auto-held. The depositor's admission (validation re-run, receipt, class assignment, clearance) only runs on ready-<slug>.md. The clear tool's default path (hold- to ready-) released it correctly. The lesson: 'ready- IS THE DEPOSIT ACT.'
- **Confidence:** high

### 2026-09-08: RIDER on `The shell's cwd resets between calls — three phase commits landed in the WRONG repo while printing success; cd-first plus a toplevel assert is the whole fix` (2026-08-08) — FOURTH FORM: A PIN CELL'S RELATIVE PATH — THE EXECUTOR'S ROOT IS NOT THE AUTHOR'S, SO THE AGENT SUBSTITUTED AND INVENTED THE REASON [tag: process-discipline]


- **Suggested action:** Add rider to PLANNER_TEMPLATE.md rule 'The shell's cwd resets between calls': every path in a plan — not only shell commands, but also pin tables and prose references — must be absolute or relative to the executor's worktree toplevel, never relative to the author's CWD.
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'The shell's cwd resets between calls — three phase commits landed in the WRONG repo while printing success; cd-first plus a toplevel assert is the whole fix' (2026-08-08): fourth form — a pin cell named a fixture as drafts/executable-tuyere-threads-retype-2.md (correct from the author's governance root, unresolvable from the bellows worktree). The plan permitted a substitute; the agent took one and invented a false reason for the absence.
- **Confidence:** high

### 2026-09-08: A SELF-READING INSTRUMENT AT A CLOSE MUST RUN AFTER THE ARTIFACT REACHES THE STATE IT WILL DEPOSIT — THE EMITTER'S OWN BATTERY READ A STALE BASELINE AND WROTE CONTINUE INTO THE STANZA [tag: drafting-cycle]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md or DRAFTING_CYCLE.md: cycle_check --emit-manifest must be the final battery-reading act in a close sequence, after all modifications including fold_check --save-baseline; running it before the re-save causes the emitter to read stale state and write a downgraded verdict.
- **Reasoning:** [AUTHOR-CONFLICT] The first T2 close under the in-cycle battery: cycle_check --emit-manifest ran before fold_check --save-baseline was re-saved; the emitter read fold_check=DRIFT and wrote CONTINUE into the stanza, while the CLI after the re-save read BAR_MET/VACUOUS. The fix is a sequencing rule in the close procedure.
- **Confidence:** high

### 2026-09-08: A VERIFICATION TOOL THAT READS COMMITTED STATE MUST BE SEQUENCED AFTER THE COMMIT IT AUDITS, AND THE PLAN MUST SAY SO — mutation_check READS git archive HEAD; A PLAN THAT RAN IT BEFORE ITS ONLY COMMIT TAUGHT ITS AGENT TO IMPROVISE A TEMP COMMIT [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: any tool that reads git archive HEAD (e.g. mutation_check) must be placed in the plan AFTER the commit whose artifacts it validates; placing it before the commit puts the new code outside the archive and causes every mutant to ERROR at baseline.
- **Reasoning:** [AUTHOR-CONFLICT] mutation_check audits committed code via git archive HEAD; plan 100042 placed the mutation run before its single DEV commit, so the new tests were outside the archive and every mutant ERRORed. The agent improvised an undocumented temp commit later reset. Plan 100043 fixed this by splitting the step: commit first, then run the tool. The fix is a plan-authoring sequencing rule.
- **Confidence:** high

### 2026-09-08: RIDER on `An autouse isolation fixture can be silently bypassed by import binding — verify isolation per-path before writing tests that write` (2026-08-18) — SECOND FORM: THE PROBE RAN OUTSIDE THE HARNESS ALTOGETHER, AND MINTED A PLAN IN THE LIVE DATABASE [tag: test-infrastructure]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: lifecycle code must never be run from a scratch script or bare python probe outside pytest; only inside pytest with conftest.py's autouse isolation fixture active; any invocation outside tests/ writes to the production lifecycle.db.
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'An autouse isolation fixture can be silently bypassed by import binding — verify isolation per-path before writing tests that write' (2026-08-18): second form — running the same fixture-shaped code as a bare python - probe (to see which branch it took) bypassed conftest.py entirely; lifecycle.LIFECYCLE_DB_PATH was the production path; run_plan minted real plan 100044 in the live lifecycle.db with status IN-FLIGHT.
- **Confidence:** high

### 2026-09-08: A COMMIT CHAINED AFTER A TEST RUN WITHOUT BRANCHING ON THE RUN'S EXIT SHIPS RED — TWICE IN ONE LANE, ON A SUMMARY LINE THAT WAS READ AND NOT ACTED ON [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a test run that gates a commit must branch on the exit code — use 'pytest ... && git commit' or 'pytest ... | tee out; grep -q failed out && exit 1; git commit'; the commit must be unreachable on a failed run.
- **Reasoning:** [AUTHOR-CONFLICT] Two direct edits were committed while the suite had '1 failed' because the command ran 'pytest | tail -n 1' and then git commit unconditionally; the eye read '95 passed' past '1 failed'. The fix (pytest | tee out; grep -q failed out && exit 1; git commit) put the check in the control flow. The lesson: 'A VERIFICATION WHOSE RESULT IS ONLY PRINTED IS NOT IN THE CONTROL FLOW.'
- **Confidence:** high

### 2026-09-08: AN OBSERVER THAT ONLY THE DEPOSIT RUNS CATCHES THE BREACH AFTER THE CYCLE — RUN `lens_order_check` AT EVERY WALK CLOSE, AND READ NO-RECORD AS "THE WALK IS NOT DONE" [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md or DRAFTING_CYCLE.md: lens_order_check must be run at the close of every walk, before the walk is declared done; a NO-RECORD result means the walk is incomplete, not clean.
- **Reasoning:** [AUTHOR-CONFLICT] The same planner made per-lens commits on plan 100043 in the afternoon and per-walk commits on 100045 that evening. The depositor caught the lens_order:1_breach at admission — the first reader. Per-lens commits cannot be recreated after a merge. The lesson: run lens_order_check at each walk close, not only at deposit.
- **Confidence:** high

### 2026-09-08: A PIN'S "HOW TO RE-DERIVE" NAMES THE POPULATION EXACTLY — GLOB, STEP RANGE FROM THE PLAN'S OWN HEADER, REPO SET — AND A MECHANISM PIN HALTS WHERE A CORPUS PIN ONLY RECORDS [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a pin's re-derive recipe must name the exact population — which glob, which step range (citing the plan's own header field), which repo set; a mechanism pin must halt on mismatch, not record; a corpus pin whose recipe does not reproduce from the written instructions is an unverifiable pin.
- **Reasoning:** [AUTHOR-CONFLICT] Three corpus pins (P6, P7, P13) did not reproduce at the cold panel: the author iterated range(1,6) while the seat walked every declared step, 'the six repos' were never named, and probe scripts lived in neither the plan nor the tree. DEV Item 1 said 're-derive P1-P13 and HALT on mismatch' — the first honest run halted on a count that had moved.
- **Confidence:** high

### 2026-09-08: A GATE CHANGE IS MEASURED BY REPLAY OVER THE LIFECYCLE `commits` TABLE — OLD RULE VS NEW RULE OVER EVERY REAL STEP — NEVER BY A PROXY THAT EQUALS ITSELF [tag: measurement]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a gate change must measure its blast radius by replaying the old and new rule over the lifecycle commits table (one real step at a time), never by a proxy that is true by construction.
- **Reasoning:** [AUTHOR-CONFLICT] The plan's blast-radius proxy (Deposits paths vs Scope entries over 476 Done steps) reported 0 uncovered 'once Deposits count as declared' — true by construction, a deposit equals itself. The capstone seat found the commits table (82 SHAs over 73 steps) and ran both rules in-process: 72 identical, 1 flip (the defect), 2 extras on the first run.
- **Confidence:** high

### 2026-09-08: A PLAN THAT REWRITES A STRING A GATE EMITS ENUMERATES THE TESTS THAT ASSERT THE OLD STRING — OR ITS OWN QA STEP EDITS A TEST OUT OF SCOPE TO GREEN THE SUITE [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a plan that changes a gate's emitted string must list in its Scope the test files that assert the old string, and its DEV step must run a full suite that includes those tests.
- **Reasoning:** [AUTHOR-CONFLICT] Item 4 changed _gate_qa_test_result's failure text; three assertions in an existing test file asserted the old text; DEV's targeted run named three other files and missed them; QA's full suite went red; the agent updated strings outside scope; scope_check refused; the CEO overrode with a durable ref. The lesson: 'A PLAN THAT REWRITES A STRING A GATE EMITS ENUMERATES THE TESTS THAT ASSERT THE OLD STRING.'
- **Confidence:** high

### 2026-09-08: A DIRECT EDIT THAT CHANGES A SHARED LIST OR A RENDERED LINE GATES ITS COMMIT ON THE FULL SUITE — ITS OWN TEST FILE IS THE WRONG GATE, AND IT WAS SATISFIED TWICE WHILE MAIN WENT RED [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: any direct edit that changes a shared list or a rendered output must gate its commit on the full suite, not only the adjacent test file; the adjacent test is green by definition when the change is local.
- **Reasoning:** [AUTHOR-CONFLICT] Two direct edits each ran only the adjacent test file and committed on that run's exit code — green — while one changed a shared gate-names list and the other a rendered dashboard header; a mechanization test pinned the list at seven, and the dashboard test asserted the old header. Main was red until the next plan's QA step ran the full suite and halted.
- **Confidence:** high

### 2026-09-08: A QA STEP ASSEMBLES PINNED FIXTURES — IT NEVER DESIGNS THEM; BUILD THE DISCRIMINATING FIXTURE AT THE WALK, RUN IT BOTH WAYS, AND PIN BOTH OUTPUTS [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a QA step assembles and runs pre-built, pinned fixtures; it never designs or creates them; fixture design is walk work — build the discriminating fixture at the walk, run it against both the new and old tool, and pin both outputs verbatim into the register before the step is written.
- **Reasoning:** [AUTHOR-CONFLICT] A QA-only plan's first draft asked the agent to design three killing mutants against real code inside the QA step — DEV work in a QA step. At walk 2 the drafter built the fixture from mutants that had already killed in a baseline sweep, ran it under both tool versions, and pinned both output lines verbatim; the step then merely executed and confirmed.
- **Confidence:** high

### 2026-09-08: BEFORE EXECUTING A STANDING RULING, RE-MEASURE ITS PREMISE — A RULING GIVEN AGAINST A STATE THAT HAS SINCE MOVED IS A QUESTION AGAIN, NOT AN ORDER [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before executing a standing ruling, re-measure the premise it was issued against; if the state has moved, bring the ruling back as a new question with the measurement; a ruling given against a state that has since changed is a question again, not an order.
- **Reasoning:** [AUTHOR-CONFLICT] A 2026-09-03 ruling to revert a merged commit was about to be executed 5 days later; re-measurement found that two shipped plans' mutant manifests depended on the feature added by that commit. The premise ('nothing depends on it yet') was true when ruled and false when reached; re-measurement turned the order back into a question, which was re-ruled in minutes.
- **Confidence:** high

### 2026-09-08: A RECORD SENTENCE FOR AN ACT NOT YET PERFORMED IS A PREDICTION WEARING THE PAST TENSE — WRITE THE RECORD AFTER THE ACT, FROM ITS OUTPUT [tag: process-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: write every record sentence after the act it describes, from the act's printed output; a record written before the act is a prediction wearing the past tense, and a prediction the act contradicts corrupts the history.
- **Reasoning:** [AUTHOR-CONFLICT] A walk register close note recorded 'thread 220 closed THROUGH the new verb — the live first use took the dedupe path' and was committed before the verb had run; the verb refused (the commit was not yet on origin/main), and the true record had to replace a sentence already pushed. The lesson: 'A RECORD SENTENCE FOR AN ACT NOT YET PERFORMED IS A PREDICTION WEARING THE PAST TENSE.'
- **Confidence:** high

### 2026-09-07: TWO CHECKERS ON ONE CONTRACT WILL DRIFT APART — AND FIXING TO SILENCE THE WEAKER LEAVES THE STRONGER BREACHED [tag: verification] [tag: gate-design]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when two checkers evaluate the same contract, both must test the complete predicate — the weaker checker must not be treated as a proxy for the stronger; silence the weaker only after verifying the stronger already covers every key.
- **Reasoning:** [AUTHOR-CONFLICT] A lint tested two of four key names; a gate tested all four. A prose-rich value silenced the lint while leaving the gate's contract breached; the author saw the WARN stop and believed the fix was done. 'TWO CHECKERS ON ONE CONTRACT WILL DRIFT APART — FIXING TO SILENCE THE WEAKER LEAVES THE STRONGER BREACHED.' The fix is a rule for gate and lint authoring.
- **Confidence:** high

### 2026-09-07: AN EDIT RECORDED AS APPLIED BUT NEVER VERIFIED IS INDISTINGUISHABLE FROM A FABRICATED ROW — ASSERT THE TARGET BEFORE, ITS ABSENCE AFTER [tag: planner-discipline] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: every edit in a fold script must assert the target text exists before the replace and confirm its absence after; a bare replace() without assertion is a silent no-op risk whose failure is indistinguishable from a fabricated register row.
- **Reasoning:** [AUTHOR-CONFLICT] A fold script asserted every edit's target except two bare replace() calls; one pattern did not match (trailing ** vs :) so the replace did nothing, the stale text survived, and the walk register recorded the finding as RESOLVED. The register row became corrupt — indistinguishable from a fabricated row. The fix is a planner authoring rule requiring pre/post assertions on every edit.
- **Confidence:** high

### 2026-09-07: CALIBRATE A NEW CHECK'S PREDICATE ON THE CORPUS BEFORE WIRING IT — THE FIRST CUT FIRED ON 76% OF STEPS AND WAS FURNITURE [tag: gate-design] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: calibrate a new check's predicate against the corpus before wiring it; run it across all live steps, sample every hit, and narrow the predicate until the false-positive rate is acceptable; a 76% fire rate means the predicate is furniture.
- **Reasoning:** [AUTHOR-CONFLICT] A new lint to catch missing root-establishment fired on 76% of steps before calibration — it counted prose path mentions and fenced output lines as commands, and misclassified git -C <abs> as a violation. Running the predicate across 1200 steps before wiring it revealed these problems. The fix is a rule about gate authoring: calibrate first, wire second.
- **Confidence:** high

### 2026-09-07: RIDER on `A fix is not done until a full-artifact sweep confirms no sibling instances` (2026-07-20) — ONE CODIFIED LESSON, FOUR PLACES, THREE WALKS THAT EACH FIXED ONE [tag: planner-discipline]


- **Suggested action:** Add rider to PLANNER_TEMPLATE.md rule 'A fix is not done until a full-artifact sweep confirms no sibling instances': when a fold cites a codified lesson, treat the citation as a class query — grep the artifact for all instances of the class before writing the fix; a walk is the wrong unit for a class sweep.
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A fix is not done until a full-artifact sweep confirms no sibling instances' (2026-07-20): the 2026-08-08 cwd lesson recurred in four places of one plan; walks 7 and 8 each fixed one instance in front of them while a grep for the class found the fourth in seconds. The parent entry's rule is sharpened: a codified lesson citation is a class query, and the sweep must precede the fix.
- **Confidence:** high

### 2026-09-07: RIDER on `A SHELL PROBE THAT READS $? AFTER A COMMAND SUBSTITUTION READS THE SUBSTITUTION'S EXIT` (2026-09-02) — RECURRED THREE TIMES IN ONE SESSION, AND THE THIRD FORM WAS A COMMIT MESSAGE [tag: planner-discipline]


- **Suggested action:** Add rider to PLANNER_TEMPLATE.md rule 'A SHELL PROBE THAT READS $? AFTER A COMMAND SUBSTITUTION READS THE SUBSTITUTION'S EXIT': backticked identifiers inside a double-quoted -m string are shell substitutions — always use HEREDOC or single-quoted strings for commit messages containing identifiers.
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A SHELL PROBE THAT READS $? AFTER A COMMAND SUBSTITUTION READS THE SUBSTITUTION'S EXIT' (2026-09-02): recurred three times in one session; the third form was a commit message passed with git commit -m in a double-quoted shell string containing backticked identifiers — the shell executed them, replaced with nothing, and the commit succeeded with holes; 'command not found' appeared for each.
- **Confidence:** high

### 2026-09-07: RIDER on `A FORCE-CLASSIFIED TEST TABLE IS A RULING — RED CELLS ARE IT SPEAKING` (2026-09-06) — RECURRED TWICE MORE IN ONE SESSION, BOTH FROM READING A FRAGMENT INSTEAD OF THE DEFINITION [tag: planner-discipline]


- **Suggested action:** Add rider to PLANNER_TEMPLATE.md rule 'A FORCE-CLASSIFIED TEST TABLE IS A RULING — RED CELLS ARE IT SPEAKING': before filing a system behavior as a defect, locate and read the canonical definition; a fragment that contradicts a summary is evidence of a documentation flaw, not a code flaw.
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A FORCE-CLASSIFIED TEST TABLE IS A RULING — RED CELLS ARE IT SPEAKING' (2026-09-06): three threads in one session filed ratified behaviors as defects by reading fragments instead of definitions — a strict parser that by design refuses a loose plural, and a gate 'missing' an arm that the doctrine defines as the dry-check arm. Both were caught only when the fix was written and contradicted the definition.
- **Confidence:** high

### 2026-09-07: A FAILURE THAT ONLY LOGS IS SWEPT; A FAILURE THAT WRITES INTO A WRAP-CHECKED PATH IS FOUND — MEASURED AT THE FIRST LIVE FIRING OF THE PLAN→THREAD LINK [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md or architecture guidance: failures in pipeline-connected components must write into a path that wrap_check monitors, not just log; a log-only failure is always swept because a module global can suppress every repeat.
- **Reasoning:** [AUTHOR-CONFLICT] The plan-side thread link was built to fail openly: on enqueue failure it writes to receipts/unenqueued-thread-review-<slug>-<stamp>.md (a path wrap_check blocks on) rather than logging, because release_for_plan beside it logs once and a module global suppresses every later occurrence. The first live firing validated the choice — the daemon wrote one ERROR line and two lines later moved on; the wrap-checked file was found immediately. The lesson is a codifiable design rule for failure reporting.
- **Confidence:** high

### 2026-09-07: A THREAD'S TITLE IS ITS SUBJECT; ITS STATUS IS IN THE TREE — TYPE OR CLOSE A ROW FROM THE ARTIFACT, NEVER FROM THE ROW'S OWN CLAIM [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a thread's type and status must be read from the artifact it names (git log, code, doc), never from the thread row's own subject line; titles can describe a stale state while the artifact reflects current reality.
- **Reasoning:** [AUTHOR-CONFLICT] A judgment pass over 82 threads would have misclassified several if keyed on titles: thread 50's title implied superseded but the register still violated §3; threads 8 and 137 read as open work but were shipped (findable only by git log). The lesson states: 'TYPE OR CLOSE A ROW FROM THE ARTIFACT, NEVER FROM THE ROW'S OWN CLAIM.'
- **Confidence:** high

### 2026-09-07: WHEN A VOCABULARY LOOKS ONE VALUE SHORT, RESOLVE THE RESIDUE THROUGH THE EXISTING STATES BEFORE WIDENING IT — 9 OF 9 RESIDUE ROWS NEEDED NO THIRD TYPE [tag: design]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before widening a vocabulary or CHECK-constrained enum, enumerate all residue cases against the existing states and widen only when at least one case provably cannot resolve; the cost of widening (migration) is never justified by cases the existing states already handle.
- **Reasoning:** [AUTHOR-CONFLICT] Thread 160 predicted a thread-type vocabulary might need a third value; on the live pass all 9 residue rows resolved through existing states — rulings, corrections, and questions all resolved to existing open/closed/work states. The lesson: 'RESOLVE THE RESIDUE THROUGH THE EXISTING STATES BEFORE WIDENING IT.' The fix is a rule about vocabulary/state-machine design.
- **Confidence:** high

### 2026-09-06: A LESSON CODIFIED INTO DOCTRINE READS AS DISCHARGED WHILE THE MECHANISM THAT DOCTRINE NAMES MAY NEVER BE BUILT [tag: governance-design] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a rule's own rationale says wording is insufficient, treat the gap as an open defect with a tracked row until the named mechanism exists — do not mark the lesson 'implemented' until both the doctrine edit AND the mechanism build have landed.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents a 'one commit per lens' rule that was codified into doctrine (marking the lesson 'implemented') but the enforcing mechanism was never built — measured: the tool contained 'no git log, no rev-list, no --count' and the nearest assert checked only that a baseline FILE exists. A false attestation resulted: 'the record claimed one commit per lens across ten walks while five carried one each.' The fix is a rule separating doctrine edit from mechanism build.
- **Confidence:** high

### 2026-09-06: IMPORT THE SHARED PARSER'S PRIMITIVES, NOT ITS CLASSIFIER — the classifier encodes policy, and policy is what changes under you [tag: verification] [tag: design]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when importing from a shared parser module, ask of each function whether it encodes the FORMAT (stable — import it) or a DECISION/POLICY (changes — make your own from the structural property needed); state the immunity as a design claim and test it by re-running against a changed classifier.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents an instrument calling shared primitives but making its own selection predicate (structural property) instead of routing through is_fold_table — when is_fold_table widened by +25 tables, the instrument's subtotals were byte-identical and only 3 of 172 rows moved in advisory columns the findings did not rest on. 'Had it routed through the classifier, the population itself would have moved and every number would have needed re-deriving.' The fix is a rule about format vs. policy function imports.
- **Confidence:** medium

### 2026-09-06: A PROPOSED CHECK'S COST IS ITS MARGINAL COUNT, NOT ITS MATCH COUNT — artifacts that already emit gain nothing, and the two numbers can read opposite [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when reporting a proposed check's reach, report both RAW (all matches) and MARGINAL (matches where no verdict already exists), always labelled; compute accuracy separately over each population; when pinning a count, name the question it answers.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents a candidate check matching 6 artifacts but with MARGINAL count of 2 (the other 4 already returned ESCALATE), and false-positive rate of 67% over all matches vs. 0% over the marginal set. 'Both numbers are true. Quoting either alone misleads, in opposite directions.' Also reconciled a stale pin of '2' where raw count was 6. The fix is a rule requiring both counts be reported and labelled.
- **Confidence:** high

### 2026-09-06: A PIN PROTECTS A CLAIM, NOT A DIGEST — re-test the claim before moving the hash, or the bump converts a premise check into a rubber stamp [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: write the CLAIM a pin guards next to the hash, in words, as a testable sentence; re-pin only after re-testing the claim (not just re-reading the file); record the re-test beside the new digest; name the halt condition in the plan in the file's own terms.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents a sha256 pin on a source file whose stated premise was 'it checks id column for PRESENCE and never reads the cell's VALUE.' Two commits fired the pin; re-testing the claim (three greps: required-column list, value-reading sites, new functions) confirmed the claim held and the re-pin was legitimate. 'A stale digest with a broken claim is a void premise and a halt — and both present identically, as a hash mismatch.' The fix is a rule requiring claims be written alongside pins.
- **Confidence:** high

### 2026-09-06: A SIGNAL VALIDATED ON THE CASES THAT PRODUCED IT HAS NO MEASURED PRECISION — RUN IT OVER THE WHOLE POPULATION BEFORE IT GATES ANYTHING [tag: measurement] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: run proposed detection signals over the full population against known positives before writing a line of the check; report true/false counts, not just total hits; ask whether failure is implementation or principle; ship surviving signal narrowly with stated coverage gaps.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents four candidate signals each validated only on their derivation set (recall 100% by construction); running over 35 artifacts against 4 known positives, two were disqualified (81% and 80% false positives) and one was structurally blind in principle. Only one of four survived. 'A refusal that is wrong four times in five is worse than no check, because it trains the reader to override it.' The fix is a rule about signal validation methodology.
- **Confidence:** high

### 2026-09-06: A FORCE-CLASSIFIED TEST TABLE IS A RULING — RED CELLS ARE IT SPEAKING, NOT A REGRESSION TO FIX [tag: verification] [tag: governance-design]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a fix causes a parameterized force-classified table to go red, read the table's comments before the diff; run the FULL suite before believing a targeted fix; if a ruling is genuinely wrong, move code and table in one commit with recorded reasoning.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents a four-line fix for a threading asymmetry that turned eight cells of a state-space table red — the table force-classified 'no walk data DOMINATES close and register' as a deliberate enumeration, not an incidental test. 'Reverting cost nothing because the tests failed loudly; had the change been made where no table existed, it would have shipped as a fix and silently overridden a ruling.' The fix is a rule requiring table comments be read before applying a targeted fix.
- **Confidence:** high

### 2026-09-06: A TRACKED THREAD'S TITLE NAMES THE SUBJECT; ITS BODY NAMES THE DEFECT — AND THE BODY ALSO CARRIES THE FORKS [tag: planner-discipline] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: open a tracked thread's body before the first measurement, not after the first surprise; look for decision flags (FIX MUST DECIDE, do not assume, fork lists, SCOPE NOTE) which are body-only; a thread title is an index entry and indexing is lossy.
- **Reasoning:** [AUTHOR-CONFLICT] Entry (migrated from Planner memory repo per 2026-09-02 ruling) documents a thread titled 'X has THREE writer classes and every guard fires BEFORE the append' worked from the title for six steps, measuring the wrong guard — 'the body named a different one entirely, whose window was unbounded wall-clock rather than 0.7 milliseconds.' The body also ended with 'FIX MUST DECIDE (do not assume)' and three forks that the title could not carry. The fix is a planner discipline rule.
- **Confidence:** high

### 2026-09-06: THE DEFECT CLASS YOU JUST FIXED IS THE ONE YOU REPRODUCE NEXT — WRITE THE VACUITY TEST FIRST [tag: verification] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: for any new checker, write the vacuity test first — what input makes this verdict impossible to fail, and what does the tool say then; after fixing a defect class, put it on the checklist for the NEXT artifact; a pass must state what it rests on.
- **Reasoning:** [AUTHOR-CONFLICT] Entry (migrated from Planner memory repo) documents a checker fixed for vacuous verdicts one day before a new checker shipped printing 'the record proves one commit per lens, in order' on artifacts with ZERO such commits. 'Having just written the definition did not protect — if anything it hurt: the class felt discharged.' Tests and a five-mutant control were both green. 'For any new checker, write the vacuity test FIRST.' The fix is a governance rule requiring vacuity-first testing.
- **Confidence:** high

### 2026-09-06: A CONCLUSION THE MEASUREMENT SETTLES IS NOT A DECISION TO DEFER — STATE IT, AND RESERVE THE ASK FOR REAL FORKS [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before offering a decision to the CEO, check whether the evidence already settles it; if the numbers decide, state the answer in one sentence and act; escalate forks (both paths defensible), not findings (three of four signals disqualified).
- **Reasoning:** [AUTHOR-CONFLICT] Entry (migrated from Planner memory repo) documents a measurement settling 'no viable general gate' (81%, 80% false positives, structurally blind, one narrow) closed by handing the question back: 'you may want to rule on this rather than have me record it unilaterally.' CEO reply: 'rephrase the conclusion decisively.' 'The hedge was not caution. It was deference wearing caution's clothes.' The fix is a rule distinguishing conclusions (report) from decisions (escalate).
- **Confidence:** high

### 2026-09-06: A FIXTURE SET WRITTEN BY THE CODE'S AUTHOR TESTS THE AUTHOR'S MODEL, NOT THE ARTIFACT — ONLY A REAL INPUT DISCRIMINATES [tag: verification] [tag: test-infrastructure]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: author-written test fixtures must be validated against a real system output before the suite is considered discriminating; a fixture set that invents formats tests the author's mental model, not the artifact.
- **Reasoning:** [AUTHOR-CONFLICT] Entry describes three green-suite-over-broken-tool instances in one session: a checker fixture invented a log format (walk-keyed vs lens-keyed), a register fixture lacked required section headings, and a classification fixture used wrong id ranges. The lesson is unambiguous: 'only a real input discriminates.' The fix is a documentary rule for test authoring added to PLANNER_TEMPLATE.md.
- **Confidence:** high

### 2026-09-05: A PREDICATE THAT FITS BY NAME MAY ANSWER A DIFFERENT QUESTION — CHECK THE QUESTION, NOT THE SIGNATURE [tag: design] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before reusing a predicate, enumerate the inputs where the two questions (the predicate's vs. the new use case's) could disagree and evaluate the candidate on those; agreement on easy cases is not evidence; name the question, not the subject.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents is_runnable_plan() reused for a corpus-freeze guard — it 'answers whether the daemon can CLAIM this, not whether this freezes the corpus.' It returns False for in-progress and verdict-pending, which would invert the guard on exactly the two states that matter most. 'Reuse is normally the right instinct, which is what makes this sharp: the wrong predicate here was the disciplined-looking choice.' The fix is a rule requiring question-level verification before predicate reuse.
- **Confidence:** high

### 2026-09-05: A STALENESS INDICATOR SCOPED TO A PROXY IS INVARIANT UNDER THE EVENT IT EXISTS TO SIGNAL [tag: verification] [tag: operational-recovery]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: verify liveness of a long-running process by process start time vs. file mtime, never by a version display unless you have read what that display is derived from; trace each fix to its invocation style (imported once at start vs. spawned per call); also check bytecode cache mtime.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents a daemon's status sha (from 'git log -1 -- <one file>') being invariant under fixes to other modules — a 31-hour daemon was running pre-fix code while tests passed and commits were green. A rider adds the inverse: the indicator moved without a restart when the pinned file was committed to. 'The proxy is not merely blind to the event — it is UNCORRELATED with it.' The fix is a governance rule about liveness verification methodology.
- **Confidence:** high

### 2026-09-04: A SCOPING ARGUMENT THAT CORRECTLY EXCLUDES ONE POPULATION IS NOT A BOUND ON THE RISK — the exposure lives in the population nobody named [tag: verification] [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a pin argues a risk away by excluding a named population, list the populations NOT excluded before accepting it; test fixtures are a population; when a scoping argument is load-bearing, run it and let the gates disagree.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents a correct pin excluding 'Done/' plans that left test fixtures unaddressed — step 1 hit tests/test_cycle_check.py and step 2 hit test_depositor_receipts.py immediately after dispatch. 'Both surfaced as scope_check refusals within minutes of dispatch. Seven walks identified neither, because every walk was re-examining the population the pin had named.' The fix is a governance rule requiring named non-excluded populations.
- **Confidence:** high

### 2026-09-04: DURABILITY IS A PROPERTY OF WHAT A RECORD IS FOR, NOT OF WHERE IT WAS CONVENIENT TO WRITE IT [tag: bellows-integration] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before writing any justification, waiver, override, or exception, ask who reads it and when; if the answer includes a later auditor, write it to the versioned corpus FIRST, commit it, then pass its committed path; a gate override ref must resolve inside a repo and be tracked.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents an override justification written to the session scratchpad — correct for temporary files but wrong for audit records. 'gate_events.override_ref now stores a path that ceases to exist when the session ends.' --override-gate is idempotent so the reference is write-once; the scratchpad path was already unreachable. The fix is a rule about where audit-critical records are written.
- **Confidence:** high

### 2026-09-04: A DIAGNOSTIC'S AUTHORITY EXTENDS ONLY TO WHAT ITS INSTRUMENT EXECUTED — a question answered from a restatement, inside a measured document, is indistinguishable from a measurement [tag: verification] [tag: drafting-cycle] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before citing a diagnostic's finding, grep the diagnostic for the subject being attributed (the function's name and the number's denominator); a question about a third party's claim requires pointing the instrument at it or marking the question unassessable in the coverage statement.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents a diagnostic that settled a parse question with a real instrument, then made assertions about a third-party filing whose subject appeared zero times in the plan or its research note. 'The wrong answer was wearing the instrument's authority.' Two tells were visible without re-measuring: unit drift (counting plans where filing counted steps) and declaring a question 'not re-derivable' against the plan's own post-condition. The fix is a rule about attribution and coverage.
- **Confidence:** high

### 2026-09-04: AN OPTIONS MENU PRICED AGAINST ITSELF BUT NOT AGAINST THE STANDING QUEUE IS A WAY TO LEAVE THE QUEUE WITHOUT DECIDING TO [tag: planner-discipline] [tag: measurement]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before offering option choices, read the standing queue and state where each option lands in it; when a cheap item turns expensive, surface the cost against what is waiting; 'park this and move on' is always one of the options.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents a four-item queue with an explicit 'stop drafting' recommendation where a complication in the first item triggered a three-option menu — all three were more work on the same item, none priced against the three items waiting behind it. 'The queue was one grep away and was never read.' The analysis was correct but on the wrong axis: 'how thoroughly do we fix this' vs. 'does this get worked at all right now.' The fix is a planner discipline rule.
- **Confidence:** high

### 2026-09-04: A VERSION-CONTROLLED HISTORY RECORDS A PROCEDURE'S OUTCOME, NEVER ITS ACT — copying the committed filenames of two prior deposits reproduced the wrong step [tag: verification] [tag: bellows-integration] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before reconstructing a procedure from git log, ask what the procedure does that leaves no commit — transient filenames and daemon-consumed prefixes are load-bearing and invisible in history; read the entry point's docstring before mirroring a diff.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents copying committed filenames from git log (drafts/X.md → X.md) producing a safety-net HOLD instead of a pipeline HOLD, because the 'ready-' prefix step 'exists for seconds and is never committed.' 'The depositor's pipeline never ran.' The entry point docstring stated the ordering contract in its first three lines. The fix is a rule about procedure reconstruction from history.
- **Confidence:** high

### 2026-09-04: A POSITIVE CONTROL PROVES THE INSTRUMENT WORKS, NOT THAT YOU CALLED IT CORRECTLY — mine passed while I was handing the function the wrong list [tag: verification] [tag: measurement]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: check the returned SHAPE against a quantity the artifact independently declares (count, name, path); read the return statement, not variable names at the call site; run a negative control on the discriminator to verify it can distinguish wrong inputs.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents _parse_plan returning (writes, reads, class) being unpacked as (reads, writes, class), passing reads to _assign_class which returned the correct answer for the wrong input because both lists came from the same project. 'A positive control had already been run and had passed' but could not detect argument order errors — it proved the instrument worked, not that it was called correctly. The fix is a rule about verification discipline at call sites.
- **Confidence:** high

### 2026-09-04: A DIVERGED BRANCH IS SIZED BY FILE OVERLAP, NOT BY COMMIT COUNT — 25-vs-68 replayed with zero conflicts because the two sides shared no file [tag: git-discipline] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: size a git divergence by the exact-file intersection of the two --name-only sets before choosing rebase/merge/reset; never let a commit count alone justify git reset --hard; use three-dot (origin/main...HEAD), not two-dot, in diff for per-side changes.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents an 'ahead 25, behind 68' session that rebased cleanly with zero conflicts because the two sides shared no file — verified by comm -12 returning empty. 'The commit count and the conflict risk are independent quantities. 68 commits confined to one subtree conflict with nothing outside it.' The fix is a governance rule for pre-rebase size discipline.
- **Confidence:** high

### 2026-09-04: AN UNTRACKED FILE INSIDE A SUBMODULE MARKS THE SUPERPROJECT MODIFIED — ` M <sub>` says "dirty", never "moved", and the two demand opposite acts [tag: git-discipline] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: never commit a ' M <submodule>' entry as a gitlink bump without comparing recorded-vs-actual SHA first (equal SHAs means the fix belongs inside the submodule); when retiring a file in place, extend the ignore pattern in the same act (e.g., '*.db' must also match '*.db.retired-*').
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents root 'git status' showing ' M lessons-forge' reading as a gitlink bump when the submodule had not moved — an untracked retirement artifact named 'lessons-forge.db.retired-2026-09-01' escaped the '*.db' glob. Committing the 'bump' would have re-pinned to the existing SHA while leaving the dirt in place. Two procedural rules address it: SHA comparison before bump commit, and glob extension on retirement rename.
- **Confidence:** medium

### 2026-09-04: WHEN THE TOOL UNDER EDIT IS ALSO THE THING BEING MEASURED, BEFORE/AFTER COMPARISON IS CONTAMINATED BY CONSTRUCTION [tag: verification] [tag: measurement]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before a before/after blast-radius run, ask what the fixture DEPENDS ON that the edit CHANGES (source files, hashes, paths, output format); build controls from artifacts the edit cannot touch; re-verify the sha, not just the verdict, when stash/unstash is involved.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents stashing a checker edit and re-running revealing a 'regression' that was actually the tool pinning its own (now-stashed) source bytes — the fixture shared state with the thing under test, making the before/after incomparable. 'A blast radius of exactly one, in an artifact related to the edit, is the signature.' The fix is a governance rule about contamination-aware blast radius measurement.
- **Confidence:** high

### 2026-09-04: A PATTERN THAT EXPLAINS THREE DEFECTS IS A HYPOTHESIS ABOUT THE FOURTH, NOT EVIDENCE FOR IT [tag: verification] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: test membership in a class before applying the class's fix; when a prediction has been stated, treat the next measurements as suspect and inspect the real data structure before assuming its shape; report the break when a pattern that held three times fails once.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents three checker defects fitting one class (verdict without evidence basis), then a fourth candidate predicted to fit that failed — 'the missing fact was absent, not unstated.' Three consecutive measurements were built to confirm the prediction; each wrong probe was shaped to find the expected answer. 'A pattern held by three instances is the most dangerous kind of prior, because it is genuinely well-evidenced for those three.' The fix is a rule requiring membership testing before applying a class fix.
- **Confidence:** high

### 2026-09-04: A BACKLOG ITEM IS A CLAIM ABOUT THE WORLD, AND CLAIMS DECAY — VERIFY THE POOL BEFORE WORKING IT [tag: planner-discipline] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: re-probe every candidate backlog item before scoping it (one command per item — does this still reproduce?); close discharged items with the probe in the closing note; suspect oldest rows first.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents two backlog items found already fixed — one by a plan shipped days earlier, one by a mechanism naming its own escape. 'Neither had any marker of doneness. The cost of not checking is not wasted work — it is a WRONG FOUNDATION. A fix built against a defect that no longer exists is written from a false premise.' The fix is a planner discipline rule requiring re-probing before scoping.
- **Confidence:** high

### 2026-09-03: A COUNT-1 EDIT ANCHOR PINS WHERE THE CODE LANDS, NEVER THE SCOPE IT WILL RUN IN — an insertion point one line outside a loop is unique, measured, and wrong [tag: verification] [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when specifying an insertion anchor, name the enclosing block (loop, function, conditional) in addition to the line; measure the anchor's indentation against that block's; inserted code that reads a variable bound elsewhere names where it is bound.
- **Reasoning:** Entry documents a plan specifying a new plan_lint check 'immediately before' a count-1 anchor one line OUTSIDE the loop whose variable it reads — the anchor was unique, measured, and at the wrong indentation scope. 'Count-1 uniqueness proves the site occurs once; it says nothing about the scope the code will run in.' The fix is a rule requiring the enclosing block to be named alongside the line.
- **Confidence:** high

### 2026-09-03: A REFUTED REMEDY LEFT STANDING IN THE CORPUS GETS REBUILT — the record's prescriptive half needs striking, not just its facts [tag: verification] [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when measurement refutes a remedy, strike the remedy from every prescriptive surface where it appears (corpus entry bullets, thread titles, baton lines, citing plans); enumerate all prescriptive surfaces before declaring a refutation recorded; a remedy bullet names the code lines read when authored.
- **Reasoning:** Entry documents a refuted plan_lint remedy (the '.txt deposit' prescription) that remained standing in LESSONS.md's bullet text and a thread title, allowing it to be re-implemented one day after refutation. 'A refutation recorded only in a correction elsewhere leaves every prescriptive surface intact, and there is no way afterwards to tell which one did the damage.' The fix is a documentary obligation to strike all prescriptive surfaces.
- **Confidence:** high

### 2026-09-03: DECLINING TO FIX A LIMITATION IS NOT THE SAME AS NOT SEEDING IT — a plan's own steps are clonable text, and an instance planted there propagates the defect the plan documents [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: after declining to fix a known limitation, run the limitation's own detector against the plan or artifact that ships the limitation; every step body is treated as a template because the shop clones plans by policy.
- **Reasoning:** Entry documents a plan that correctly documented a limitation in its suppression check, then planted a working instance of that limitation in its own QA step. 'The plan documented the trap in its prose and planted a working instance of it in the half that gets copied.' A rider also notes that removing the suppression token by quoting it reintroduced it — 'verify a token removal by probe, never by reading.' The fix is a governance rule requiring self-application of the limitation detector.
- **Confidence:** high

### 2026-09-03: A DETECTOR BUILT FOR YOUR DOMINANT FAILURE CLASS IS WORTH NOTHING UNRUN — AND WHEN RUN IT FOUND ONE SITE OF FOUR; THE CLAIM-SWEEP FOUND ALL FOUR [tag: verification] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before recording a defect class as expensive or unsolved, check whether the shop already ships an instrument for it; pair every mechanical sweep with a claim-sweep (grep for phrasings of the claim, not the literal just edited); record tool verdicts verbatim, never paraphrased.
- **Reasoning:** Entry documents that propagation_check (built for the dominant failure class) was run in 18% of walk registers while incomplete propagation accounted for 75% of fold-introduced findings. Run on a live plan, it flagged one of four real sites; the other three were found by a claim-sweep. 'Owning a tool and running it are different facts.' The fix is a set of planner discipline rules about tool use, sweep methodology, and verbatim recording.
- **Confidence:** high

### 2026-09-03: HAND-AUTHORING A GENERATOR'S OUTPUT IS NOT A SHORTCUT — IT SILENTLY OPTS OUT OF EVERYTHING THE GENERATOR RUNS [tag: verification] [tag: plan-authoring]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before hand-authoring any artifact a tool can produce, read the generator to identify what it runs — hand-authoring silently cancels those invocations; before building new enforcement, enumerate what already enforces it by grep across all checkers and consumers.
- **Reasoning:** Entry documents a plan's Cycle Manifest hand-authored instead of emitted by cycle_check --emit-manifest, which skipped three tool invocations (plan_lint, fold_check, propagation_check) and replaced their results with prose. Then the author drafted two enforcement plans before discovering three surfaces already enforced it. 'Wanting the result "next" is not enough — the runs never happened' when the output was hand-authored.
- **Confidence:** high

### 2026-09-02: A NAMED TEST CAN PASS FOR A REASON UNRELATED TO ITS MUTANT — the kill map, not the test's name, is the only proof a test discriminates [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: run mutation_check kill map before the plan claims a fix is discriminated; treat SURVIVED as a missing test, never as a note.
- **Reasoning:** Entry states that named killing tests passed while the kill map scored two SURVIVED — 'the discriminating inputs had to be found by measurement, not by reading the test.' The fix is a documentary discipline rule: 'A test named as a mutant's killer is a claim until mutation_check scores it KILLED on committed code.' Targets PLANNER_TEMPLATE verification checklist.
- **Confidence:** high

### 2026-09-02: A MUST-PRESERVE WRITTEN OVER A POPULATION THE PLANNER NEVER MEASURED WILL BE OBEYED AGAINST THE PLAN — pin the rule's population before you write "no X may read Y" [tag: drafting-cycle]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: every MUST-PRESERVE rule of the form 'no member of set S may read Y' requires a pin row measuring Y over ALL of S before the freeze; a set not enumerated and run is not a set the rule may address.
- **Reasoning:** Entry records a MUST-PRESERVE over 'six measured drafts AND nine Done plans the Planner had not run the tool on' — the rule's population was nine files wider than its evidence, causing a gate refusal on a rule that was wrong rather than a tool that was. The fix is a documentary constraint on how MUST-PRESERVE rules are authored.
- **Confidence:** high

### 2026-09-02: A PIN READ FROM A COMMAND WHOSE TARGET WAS NOT NAMED NAMES WHATEVER LANDED LAST — pathspec the commit, absolute-path the repo, and read the printed hash against the artifact's own log before writing it [tag: verification] [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a pin's producing command names its target explicitly — a commit by pathspec ('git log -1 -- <file>'), a repo by 'git -C <abs>'; HEAD is a pin only for the instant it is written; the printed value is read against the artifact's own log before recording.
- **Reasoning:** Entry records three forms of the same failure in one evening: a re-entry arm using HEAD without pathspec, a builder pin rewritten without pathspec (capturing a register commit's hash), and push output from the wrong repo's cwd. The fix is a documentary rule: pins must name their target, and the value must be verified against the artifact's own log before writing.
- **Confidence:** high

### 2026-09-02: DOCTRINE STATES THE OUTCOME A FUNCTION PRODUCES, NEVER ITS DECISION ORDER — a prose restatement of branch order was falsified by execution twice in one cycle [tag: drafting-cycle] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when doctrine describes what code does, name the outcomes and the sites that produce them; never narrate the order of the tests that select between them — branch order is the function's and prose reproducing it is an untested second implementation.
- **Reasoning:** Entry documents two successive doctrine restatements of '_assign_class' branch order, each falsified by execution because each captured only the cases the author had in mind. 'Each restatement was true for the cases the author had in mind and false for the branch order the code actually walks.' The fix is a rule about what doctrine may state.
- **Confidence:** high

### 2026-09-02: A PRECONDITION EVALUATED BEFORE A PLAN'S RE-ENTRY LADDER MUST NOT DEPEND ON STATE THE PLAN'S OWN STEPS CHANGE — it makes the post-step arm unreachable and names a cause that never happened [tag: drafting-cycle] [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: split every A0 precondition into unconditional (no step of the plan changes it) and state-dependent (moved by the plan's own steps) halves; read the state-dependent half inside the ladder, with the value each arm expects; every arm must be exercised on a scratch copy before deposit.
- **Reasoning:** Entry records a Gate-2 plan asserting its accepted-population count BEFORE the re-entry ladder — but its own flip step changes those values, making the complete arm unreachable after the flip. 'A death between the flip's commit and the dev-log step would halt at the precondition with a message blaming a W=30 event that never happened.' The fix is a documentary rule for A0 precondition structure.
- **Confidence:** high

## Instrumentation


### 2026-09-10: RUN THE WHOLE SUITE UNDER THE CHANGE AT DRAFTING, IN A SCRATCH ARCHIVE — THE ONE TEST A PROMOTION BREAKS IS A FOLD AT WALK 1, NOT A MUST-PRESERVE VIOLATION AT DEV [tag: verification] [tag: drafting-cycle]


- **Suggested action:** Add drafting checklist item: for any tool or lint change, run git archive of HEAD in scratch, apply the change, and run pytest once; include blast-radius result (any breaking tests found and their disposition) in the plan before deposit
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a new procedural step added to the drafting workflow: 'a lint promotion's blast radius on the test suite is measurable before the plan is written: a `git archive` of HEAD in scratch, the one-line change applied, pytest run once.' This is a new pre-deposit checklist action, not a code fix or a pure documentary rule.
- **Confidence:** high

### 2026-09-07: A WALKED BUT UNSHIPPED ARTIFACT WITH A FULL REGISTER IS THE BEST REGRESSION FIXTURE FOR THE INSTRUMENTS THAT JUDGED IT [tag: test-infrastructure] [tag: verification]


- **Suggested action:** Add procedural step to the test setup process: before retiring a heavily-walked but unshipped plan, verify whether it serves as a regression fixture for the instruments that judged it; if it does, keep it active and pin its expected verdict set.
- **Reasoning:** [AUTHOR-CONFLICT] A plan walked eight times but never deposited carried 65 findings in a committed register and gate verdicts from every battery instrument at every walk. When instruments were repaired in tranches, that plan gave sharper acceptance tests than fresh fixtures because each fix was predicted to change a specific verdict. The lesson implies adding a procedural check before retiring unshipped walked plans.
- **Confidence:** medium

### 2026-09-02: A SHELL PROBE THAT READS `$?` AFTER A COMMAND SUBSTITUTION READS THE SUBSTITUTION'S EXIT — capture the return code first, before any other command runs [tag: measurement]


- **Suggested action:** Add procedural step to shell scripting checklist: capture exit code as 'rc=$?' immediately after the command, before any substitution or second command; never inline '$?' beside a pipe or substitution.
- **Reasoning:** Entry documents 'run; printf "%s exit=%s" $(basename $f) $?' reporting exit 0 for every file because basename's substitution overwrote the exit code. The fix is a new procedural step: 'run; rc=$? as the very next statement, then format.' This is a workflow addition, not a code change or documentary rule edit.
- **Confidence:** high

### 2026-09-02: A COMPOUND THAT CONTINUES PAST A FAILED INTERPRETER STEP WRITES ITS DOWNSTREAM RECORDS FROM THE PRE-FAILURE STATE — put an explicit exit check after every step whose output the next step reads [tag: verification] [tag: measurement]


- **Suggested action:** Add procedural step to shell scripting checklist: place an explicit '|| exit 1' (or '|| { echo FAILED; exit 1; }') after each interpreter or builder step whose output a later step reads; follow with a measurement of the patch's own token before any downstream step runs.
- **Reasoning:** Entry documents a shell compound under set -e where a heredoc-fed Python patch aborted but the shell continued, causing downstream steps to re-measure the UNPATCHED state and record false pins. 'Nothing in the output said FAILED except a traceback scrolled above forty lines of green measurements.' The fix is a procedural safeguard requiring explicit exit checks.
- **Confidence:** high

## Narrative


### 2026-09-08: THE DAEMON LANDS A DEV COMMIT ON MAIN BEFORE THE VERDICT — A STOP HALTS THE PLAN AND CANNOT UN-LAND THE CODE; A CONTINUE ON A FAILED GATE IS REFUSED UNTIL THE FAILURE IS OVERRIDDEN WITH A REF [tag: bellows-integration]


- **Suggested action:** Archive as context — the daemon's fast-forward-before-verdict behavior and the continue-refusal-on-failed-gate are documented system behaviors; the handling (revert + re-cycle for a stop; --override-gate for a failed continue) is already captured in thread 112's ruling.
- **Reasoning:** [AUTHOR-CONFLICT] Describes two measured daemon behaviors: (1) after STEP 1 the daemon fast-forwards onto main before pausing for verdict, so a stop leaves the DEV commit already landed; (2) a continue on a failed gate is refused until --override-gate with a committed ref. Both behaviors were measured twice and handled via existing rulings (threads 193, 194). This is a factual description of the state machine with no new actionable intervention beyond the established ruling.
- **Confidence:** medium

## Structural


### 2026-09-12: A CHECK THAT LISTS A COMMIT'S FILES MUST SAY WHAT IT DOES WITH A MERGE — `git diff-tree` WITHOUT `-m` PRINTS NOTHING FOR A TWO-PARENT COMMIT [tag: verification]


- **Suggested action:** Fix threads done --commit: add -m, -c, or --first-parent to git diff-tree call so merge commits report their file list; add test with a two-parent commit; at authoring, require commit file-list tools to declare their merge behavior
- **Reasoning:** [AUTHOR-CONFLICT] Entry names a concrete code fix: 'a check built on a commit's file list says what it does with a second parent, or it reports "touched nothing" for every merge.' Tuyere's threads done --commit uses git diff-tree without -m, reading 'component: miss' for every merge commit. Five of bellows' last 80 commits are merges.
- **Confidence:** high

### 2026-09-12: A TOOL THAT INFERS THE AUTHOR'S ACT FROM A DIFF CANNOT TELL AN EDIT MADE FOR ANOTHER GATE — A HAND EDIT THAT SATISFIES ONE CHECK CAN SWITCH OFF ANOTHER TOOL'S RECORD [tag: drafting-cycle] [tag: bellows-design]


- **Suggested action:** Fix lens_commit.py: detect a dry lens by the presence/absence of its own DRY line artifact rather than by whether the register was otherwise unchanged; add explicit flag for the dry case to avoid inference from diff; or check the DRY line directly as the artifact
- **Reasoning:** [AUTHOR-CONFLICT] Entry names a concrete code bug in lens_commit.py: it writes the DRY line only when the register is otherwise unchanged, but a hand edit to open walk 1's table (needed to pass the register lint) made the tool read the edit as the lens record and write no DRY line. The fix is a structural change to the tool's dry-detection logic.
- **Confidence:** high

### 2026-09-11: GIT'S FUNCTION TRACE SEES ONLY THE HEADINGS ITS DIFF DRIVER KNOWS — WITHOUT A `.gitattributes` DRIVER EVERY INDENTED `def` IS `no match`; TRACE BY AST LINE RANGE, AND PRICE A HISTORY QUERY ON THE HARD INSTANCE BEFORE PINNING ITS COST [tag: verification]


- **Suggested action:** Use git log -L <lineno>,<end_lineno>:file (AST-derived line range) instead of -L ':name:file' for Python function history traces; add planning rule: benchmark on both top-level and nested function forms before assuming the query domain is uniform
- **Reasoning:** [AUTHOR-CONFLICT] Entry describes a concrete code/tooling fix: 'The range form `-L <lineno>,<end_lineno>:file` from the AST node works for all and costs the same.' The function-name form returns fatal for indented methods (no Python diff driver). The primary action is a tool code change.
- **Confidence:** high

### 2026-09-11: A STATUS READER IS TESTED IN THE STOPPED STATE IT EXISTS TO REPORT — A READ-ONLY OPEN OF A WAL DATABASE FAILS WHEN NO WRITER HOLDS IT [tag: verification]


- **Suggested action:** Fix status.py: replace mode=ro URI with a plain connection using PRAGMA query_only (so WAL can create the -shm file); add explicit handler for SQLITE_CANTOPEN returning the STOPPED state; add test exercising the stopped state with no writer process present
- **Reasoning:** [AUTHOR-CONFLICT] Entry names a concrete code fix: 'the fix is a plain connection under `PRAGMA query_only`, or the STOPPED branch on SQLITE_CANTOPEN, never `immutable=1`.' The status reader is guaranteed to run in the no-writer window and was never tested there. WAL requires the -shm file which mode=ro cannot create.
- **Confidence:** high

### 2026-09-11: RIDER on `A case-insensitive filesystem defeats a realpath guard — compare inodes, not strings` (2026-08-13) — A PATH GUARD IS ALSO DEFEATED BY ITS OWN FALLBACK: `realpath("")` IS THE CURRENT DIRECTORY [tag: verification]


- **Suggested action:** Fix path guard: check explicitly for None return from the lookup function before calling realpath; use a sentinel value the comparison side can never hold; add test where the lookup fails and verify the guard refuses
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'A case-insensitive filesystem defeats a realpath guard — compare inodes, not strings' (2026-08-13). Entry names a concrete code bug: `realpath(agent_root() or "")` resolves to CWD when the lookup fails, equaling `realpath(root)` for a dashboard run from its own root. The fix is a code change to the guard.
- **Confidence:** high

### 2026-09-10: A LINT'S WARN LINE THAT NAMES WHAT A GATE WILL NOT DO IS A FAILURE THE AUTHOR HAS NOT MET — A COMMIT LOOP THAT COUNTS `^FAIL` READS NONE OF THEM, AND THREE PLANS SHIPPED WITH THEIR QA GATES SILENCED [tag: process-discipline] [tag: verification]


- **Suggested action:** Promote WARNs that name a gate silence (e.g., 'will NOT be gated', 'missing cold-panel line') to FAIL in plan_lint; update commit-loop gates to print WARN lines alongside the FAIL count
- **Reasoning:** [AUTHOR-CONFLICT] Entry describes a concrete code change to plan_lint: 'a WARN that describes a gate's silence is promoted to FAIL in the lint the next time it is read past.' Three plans shipped with QA gates silenced because the loop gated only on grep -c '^FAIL'. The primary fix is a tool code change.
- **Confidence:** high

### 2026-09-10: RIDER on `AN OBSERVER THAT READS SUBJECTS CANNOT SEE A SHIFTED SUBJECT` (2026-09-09) — THE REGISTER IS THE RECORD THE DEPOSIT READS, A DRY LENS MUST TOUCH IT, THE DESCRIPTION IS PART OF THE SUBJECT, AND THE OBSERVER RUNS AFTER EVERY LENS COMMIT ON THE DEPOSIT'S SHAPE [tag: drafting-cycle] [tag: verification]


- **Suggested action:** Implement --dry flag in lens_commit.py that writes the DRY line to the walk register; enforce that descriptions name no other lens/walk; run the observer after every lens commit and on a scratch project-shaped copy before the receipt
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'AN OBSERVER THAT READS SUBJECTS CANNOT SEE A SHIFTED SUBJECT — A COMMIT LOOP ASSERTS THAT EACH MESSAGE NAMES THE UNIT IT COMMITS' (2026-09-09). Entry names a concrete code change: 'every lens commit touches the register (a dry lens by its DRY line — now the tool's job under `--dry`).' The register/observer discipline is secondary to the tooling fix.
- **Confidence:** high

### 2026-09-10: RIDER on `Headerless table rows are INVISIBLE to a header-anchored parser` (2026-08-13) — THE AUTHOR-SIDE TWIN: ANY PROSE LINE CLOSES A REGISTER'S FOLD TABLE, SO A ROW APPENDED AFTER A DRY LINE IS HEADERLESS — WRITE THE HEADER WITH THE ROW [tag: drafting-cycle] [tag: verification]


- **Suggested action:** Fix register fold-row appender: before appending a row, check if the last non-blank line is a table row; if not, emit the two-line table header first
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'Headerless table rows are INVISIBLE to a header-anchored parser' (2026-08-13). Entry names the author-side fix: 'an appender must look at the last non-blank line and emit a header whenever it is not a table row.' This is a concrete code fix to the walk register append tool.
- **Confidence:** high

### 2026-09-09: RIDER on `AN OBSERVER THAT READS SUBJECTS CANNOT SEE A SHIFTED SUBJECT — A COMMIT LOOP ASSERTS THAT EACH MESSAGE NAMES THE UNIT IT COMMITS` (2026-09-09) — RECURRED THE SAME EVENING: THE ASSERT CHECKED THE LENS NUMBER, WHICH THE SHIFT PRESERVES; IT MUST CHECK THE LENS NAME [tag: process-discipline]


- **Suggested action:** Fix commit-subject assert to check both lens number AND lens name (array-supplied): pattern *'lens $i — ${NAME[$i]}'*; declare shell arrays as associative (declare -A) to prevent leading-element shift
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'AN OBSERVER THAT READS SUBJECTS CANNOT SEE A SHIFTED SUBJECT — A COMMIT LOOP ASSERTS THAT EACH MESSAGE NAMES THE UNIT IT COMMITS' (2026-09-09). Entry describes a concrete code fix: the assert checked `*"lens $i"*`, which passes when the array shifts because the loop variable is correct; the fix is to include the name from the array in the assert pattern and use `declare -A`.
- **Confidence:** high

### 2026-09-08: A ROOT CAN DO A ROLE'S WORK — ON THE SHOP LAYOUT THE GOVERNANCE ROOT IS THE PROJECTS PARENT, SO A RULE KEYED ON "UNDER THE GOVERNANCE ROOT" IS EVERY PROJECT THERE [tag: design]


- **Suggested action:** Fix the path classification rule: identity must be determined by the specific resolver function, not by path containment under the governance root; resolve_projects_parent() and resolve_governance_root() are coincident on the shop layout and must be distinguished in code.
- **Reasoning:** [AUTHOR-CONFLICT] On the shop layout, resolve_projects_parent() IS resolve_governance_root() (projects live under the governance root; bellows_root.py:55). A rule keyed on 'under the governance root is governance' made every project path classify as governance, re-creating the same defects fixed earlier by identity-by-resolver. The fix is a code change to the path classifier.
- **Confidence:** high

### 2026-09-08: WHEN A CHECK'S VOCABULARY COLLIDES WITH A MANDATED ARTIFACT FORM, EXEMPT THE EXACT FORM, NEVER THE WORD — `pending` WAS BOTH A HEDGING KEYWORD AND THE REQUIRED LESSONS STATUS MARKER [tag: design]


- **Suggested action:** Fix: when a check's vocabulary word collides with a mandated artifact pattern, exempt the exact mandated form (not the word) from the check; document the exemption with the specific pattern and the reason for the collision.
- **Reasoning:** [AUTHOR-CONFLICT] Rule 20's hedging scan listed 'pending'; the wrap ritual mandates '[status: pending]' on every new LESSONS entry; a QA receipt quoting a compliant entry in a check-mark row failed its own self-check. The solution adopted was to exempt the exact form '[status: pending]' from the scan, not the word 'pending'. The fix is a code change to Rule 20's scanner.
- **Confidence:** high

### 2026-09-08: A ONE-EXPRESSION FILE REWRITE OPENS FOR WRITING BEFORE IT READS — `open(p, "w").write(open(p).read() + more)` TRUNCATES THE FILE FIRST, AND A LINT STATUS THAT MERELY CHANGES IS THE ONLY WITNESS [tag: process-discipline]


- **Suggested action:** Fix: never use open(p,'w').write(open(p).read() + more); always read into a variable first, then open for writing: content = open(p).read(); open(p,'w').write(content + more); add a linter check or code review rule for this pattern.
- **Reasoning:** [AUTHOR-CONFLICT] Python evaluates the callee (open(p,'w')) before its argument, so the register was truncated before open(p).read() ran; the walk-0 head vanished and the walk-1 commit shipped without it. walk_register_lint reported PRE-SCHEMA (a status, not a failure) and the hook passed. The fix is a code pattern change: read then write, never inline.
- **Confidence:** high

### 2026-09-08: ADDING A GATE IS THREE SITES, NOT ONE — `check()`, THE STATIC RENDER LIST, AND THE PASS-ROW LIST — BECAUSE A CONSUMER THAT RENDERS FROM A STATIC LIST HIDES AN UNLISTED PRODUCER [tag: design]


- **Suggested action:** Fix: adding a gate requires updating three sites — gates.check(), the static render list (verdict._build_verification_results_table's _KNOWN_GATES), and the pass-row list (lifecycle.standard_gates); add a test that asserts all three lists are in sync.
- **Reasoning:** [AUTHOR-CONFLICT] verdict._build_verification_results_table composes from a static _KNOWN_GATES list; lifecycle.record_gate_events writes PASS rows from a static standard_gates list. A gate added only to gates.check() has no PASS row and its FAIL surfaces only under ## Gate Failures. qa_test_result was rowless in both static lists since birth, unnoticed until a plan changed it.
- **Confidence:** high

### 2026-09-07: THE EVIDENCE OF AN EVENT IS NOT ALWAYS ON THE OBJECT THE EVENT WAS ABOUT — AN OBSERVER MUST READ THE LEDGER, NOT ONLY THE ARTIFACT [tag: gate-design] [tag: verification]


- **Suggested action:** Fix the lens-order observer to read both the governance repo and the project repo, and to account for dry-lens commits (no plan commit) and deposit-time commits (in a different repo); git log on the plan file alone is structurally blind to both.
- **Reasoning:** [AUTHOR-CONFLICT] An observer built to prove lens order read 'git log' on the plan file only. Two events left no mark there: a DRY lens folds nothing so makes no plan commit, and the standard pipeline deposits into a different repo. The fix is a code change to the observer tool to read both repos and the deposit ledger.
- **Confidence:** medium

### 2026-09-07: RIDER on `The shell's cwd resets between calls — three phase commits landed in the WRONG repo while printing success; cd-first plus a toplevel assert is the whole fix` (2026-08-08) — THIRD FORM: A DAEMON'S `subprocess.run` WITHOUT `cwd=`, INVISIBLE TO A MOCKED TEST, FOUND AT THE FIRST LIVE FIRING — THEN RE-TRIPPED BY HAND TWICE WITHIN THE HOUR [tag: process-discipline]


- **Suggested action:** Fix: every subprocess.run call in code that runs subprocesses in a checked-out repo context must pass an explicit cwd= parameter; add a code-review checklist item for subprocess.run calls without cwd=.
- **Reasoning:** [AUTHOR-CONFLICT] RIDER on 'The shell's cwd resets between calls — three phase commits landed in the WRONG repo while printing success; cd-first plus a toplevel assert is the whole fix' (2026-08-08): third form — plan_claim.enqueue_thread_reviews used subprocess.run without cwd=; the daemon runs from bellows where tuyere is not importable. Mock tests proved argv/env, not importability; the defect was invisible until the first live firing. The fix is a code change: add cwd= to every subprocess.run.
- **Confidence:** medium

### 2026-09-06: AN ENFORCER INHERITS EVERY GAP IN ITS AUTHOR'S READING — OF THE RULE IT ENFORCES AND OF THE DATA IT READS [tag: verification] [tag: design]


- **Suggested action:** Update the lens-commit checker to implement all three clauses of the governing rule (order, completeness, AND repetition check); update the commit-message parser to handle the slash form 'lens 1/4' (multiple lenses in one commit) before extracting the lens number.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents two halves of one checker failure: (1) the checker implemented order and completeness but never checked repetition, missing a clause that sits beside the quoted rule in its own docstring; (2) the parser read 'lens\s+(\d+)' and took the first number from '1/4' form, scoring a batched commit as compliant — 'moving 1 to 5 in the corpus count of that breach.' Both tests and a mutation control were green because they encoded the same partial reading. The fix is clause-by-clause implementation and notation census.
- **Confidence:** high

### 2026-09-05: A DEFAULT THAT IS ALSO A LEGITIMATE ANSWER IS A SILENT FAIL-OPEN — AND THE DANGER IS THE INVISIBILITY, NOT THE VALUE [tag: design] [tag: verification]


- **Suggested action:** Remove the default value from _assign_class's project_root parameter (or change it to raise TypeError on empty string); make the missing argument a hard error rather than a silently fail-open value; update the runbook/verification recipe to pass the real project root.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents _assign_class taking project_root='' as its default, making the infra-project test unconditionally false and returning the auto-clearing class instead of the holding class for the one real call site. 'Production was never affected — the entire cost fell on the verification recipe run BY HAND.' Two unrelated mistakes (omitting root, feeding reads instead of writes) both returned the same wrong answer. The fix is a code change removing the dangerous default.
- **Confidence:** high

### 2026-09-04: A GATE THAT REFUSES WITHOUT NAMING ITS REASON IS INDISTINGUISHABLE FROM A BROKEN ONE — and the author will work around it blindly [tag: verification] [tag: bellows-integration]


- **Suggested action:** Update cycle_check (and any other gating tool that sets a blocking flag from a loop) to report WHICH input caused the refusal — name the offending line, field, or item; a boolean that collapses many causes into one word is not a verdict.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents cycle_check printing only 'CONTINUE' with no reason — the cause was two malformed Cycle Log lens lines the parser could not read. 'Finding them took importing the checker and calling parse_block and parse_lens_line directly on each line.' A silent refusal also teaches wrong lessons: 'an author who stumbles on the fix learns a superstition rather than the rule.' The fix is a code change to emit the blocking input.
- **Confidence:** high

### 2026-09-04: A LISTING THAT PAGES IN THE DATABASE AND FILTERS IN THE APPLICATION REPORTS A FLOOR AS A TOTAL [tag: verification] [tag: measurement] [tag: tuyere]


- **Suggested action:** Fix the tuyere open-thread listing to filter in the query (move predicate into SQL) or paginate until exhaustion; the LIMIT must not apply to pre-filtered rows; fix both the local and remote surfaces that call the shared function.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents a carried-work listing running 'SELECT ... ORDER BY id DESC LIMIT N' then filtering terminal rows in Python — so 'limit=50' returned 39 open items while 'limit=200' returned 78, the true count. '39 open, compounding faster than we retire it' was written into a session's forward record as a planning input from a floor reading as a total. The fix is a structural query change in the shared function.
- **Confidence:** high

### 2026-09-04: A CHECKER THAT STATES A VERDICT WITHOUT ITS EVIDENCE BASIS CANNOT BE AUDITED — AND USUALLY ALREADY HOLDS THE MISSING FACT [tag: verification] [tag: bellows-integration]


- **Suggested action:** Update fold_check, cycle_check, plan_lint, and mutation_check to emit the evidence basis alongside each verdict: fold_check names the baseline compared; cycle_check states which escalation arm had no data; plan_lint (q) names the file it resolved a pin against; mutation_check names the interpreter.
- **Reasoning:** [AUTHOR-CONFLICT] Entry documents four checker defects sharing one class: the tool reported a verdict without stating what it rested on. 'In every case the tool ALREADY HELD the missing fact — none needed new data; each needed one line of output.' The fixes were small and none changed any verdict on the existing corpus. 'The failure is not wrongness, it is unfalsifiability.' The fix is a structural code change to each checker to emit its evidence basis.
- **Confidence:** high

### 2026-09-03: A PLACEHOLDER PASSES EVERY GATE THAT DOES NOT READ IT, AND THE CONSUMER'S FALLBACK TURNS THE ABSENCE INTO A DIFFERENT ANSWER RATHER THAN AN ERROR [tag: plan-authoring] [tag: bellows-integration] [tag: verification]


- **Suggested action:** Update cycle_check/plan_lint to fail when a '## Cycle Manifest' heading exists but parse_manifest_stanza returns nothing (placeholder present, contents absent); fail-closed on the absence rather than falling back to a narrower source.
- **Reasoning:** Entry documents a plan frozen at BAR MET with '## Cycle Manifest' still reading its authoring placeholder. All four freeze gates passed because none reads the manifest's contents. 'The harm was not the absence; it was the fallback' — parse_plan silently fell back to a different, narrower source, reclassifying the plan from shop-infra to app-feature, bypassing the class hold. The fix is a code change to the cycle_check/depositor to detect the placeholder state.
- **Confidence:** high

### 2026-09-02: A LIFECYCLE STATE THAT RENAMES A PLAN'S FILE MUST BE KNOWN TO EVERY READER THAT ENUMERATES IN-FLIGHT PLANS BY FILE NAME — a pause blocked every new deposit [tag: bellows]


- **Suggested action:** Update depositor's plan-resolver to enumerate all lifecycle-state file prefixes (including 'verdict-pending-') when scanning for in-flight plans; add a fixture proving the new prefix resolves correctly.
- **Reasoning:** Entry documents that the depositor's write-set scan lists only 'in_progress', 'claimed', 'awaiting_verdict' states and resolves by 'in-progress-<type>-<id>.md' names; a paused plan's 'verdict-pending-' prefix matched none of the three candidates, causing every new deposit to hold as 'unresolvable_in_flight'. The fix is a tooling change to the depositor code.
- **Confidence:** high
