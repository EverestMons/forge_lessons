# Lessons Report — 2026-09-02


## Summary


| Category | Count |
|---|---|
| governance_rule | 25 |

**Total proposals:** 25


## Governance Rule


### 2026-09-02: A PROBE'S LOCATION IS PART OF ITS ENVIRONMENT — code whose answer depends on where the tree SITS must be proven in the shape the daemon runs in, not in a scratch clone [tag: verification] [tag: multi-machine]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a change makes behavior depend on filesystem position, the proof runs in the canonical checkout AND in a worktree under it; a scratch clone in /tmp is a different environment for location-sensitive code; state the parent directory each probe resolved in the walk register
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a verification rule for location-sensitive code: 'when a change makes behaviour depend on filesystem position, the proof runs in the canonical checkout AND in a worktree UNDER it; a scratch clone in /tmp is a different machine for that purpose.' Five independent proofs (walk-0 clone, two cold scouts, execution-seat worktree replica, Planner /tmp worktree) all shared one blind spot: none sat under ~/Developer where tuyere lives, so the resolver returned 'unresolvable' and 4 seam tests passed—then failed on merge to main. Plan 100012 fixed the tests.
- **Confidence:** high

### 2026-09-02: A SEARCH WINDOW THAT CONTAINS A MACHINE-WRITTEN SUMMARY LINE CREDITS EVERY SYMBOL THE SUMMARY NAMES — bound the window at the summary before believing a hit rate [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before counting symbol mentions in a search window, enumerate machine-written lines (manifests, summaries, validation stanzas, tables of expected values) and exclude or bound them; a prototype count is not a pin
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a verification methodology rule: 'before counting mentions of a symbol, enumerate the machine-written lines in the window and exclude or bound them; a summary names what it was built to name.' The measured case: a pricing diagnostic search from '## Drafting Cycle' to EOF included the Cycle Manifest's 'validation: cycle_check=..., plan_lint=..., fold_check=...' line, which names three tools in every stanza'd plan; the count was 51 (Planner prototype) vs 39 (agent with correct window bounded at '## Cycle Manifest'). The plan's numbers discipline correctly gave the agent's count precedence.
- **Confidence:** high

### 2026-09-02: IDENTITY THROUGH A SYMLINK IS TRIVIAL — inspect the directory ENTRY and compare inodes before calling two paths copies [tag: verification] [tag: multi-machine]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a 'copies' claim requires three facts—directory entry type (ls -la on the parent, or stat -f %HT), inode comparison of both paths (stat -f %i), and a difference that is possible in principle; cmp between a path and the same path via a symlink cannot fail and proves nothing
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a verification rule for copy/symlink claims: 'a copies claim needs three facts: the directory entry's type, the inodes of both paths, and a difference that is possible in principle—cmp between a path and the same path via a link cannot fail and proves nothing.' The measured failure: ~/.claude/eluvian is a symlink to the repo directory (created at mini setup), cmp reported IDENTICAL and the plan recorded 'regular files, not links'—an hour went to hunting the process that 'rewrote the copies' the second a merge landed. Kin to the 2026-08-13 case-insensitivity inode-guard entry.
- **Confidence:** high

### 2026-09-02: A COLD SEAT'S FINDING THAT CONTRADICTS A STANDING RULING IS A CEO QUESTION, NOT A FOLD — record the answer in the ruling's own file before folding [tag: drafting-cycle] [tag: process-integrity]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a cold seat finding would change what a ruling decided, pause the fold, state the evidence and the fork to the CEO, record the answer under the ruling's own id (e.g. R4a), push it, fold, then re-pin every in-flight plan that cites the file
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a governance rule for the drafting cycle: 'a plan implements within a ruling's letter, never against it; the panel exists to surface where the letter and the measured world diverge.' The measured case (2026-08-26 fork-1 cycle): a DISCOVERY seat proved the claim-act-heartbeat design was a de-facto TTL—the mechanism R4 had declined. The correct procedure (pause, CEO question, R4a addendum, push, fold, re-pin) was executed; folding silently would have rewritten the ruling without record.
- **Confidence:** high

### 2026-09-02: ADJUDICATING AGAINST A SEAT IS LEGITIMATE, AND A DECLINE THAT IS NOT WRITTEN DOWN IS INDISTINGUISHABLE FROM A MISS [tag: drafting-cycle]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: every seat finding gets exactly one disposition—folded, adjudicated-not-folded with the reason and the measurement that decided it, or recorded-unresolved; a silent decline is indistinguishable from a miss in the record
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a mandatory disposition rule for panel findings: 'a panel finding is evidence, not a verdict.' Three instances confirm the pattern: 2026-08-26 (halt path and run_plan outer except correctly declined, recorded with reasoning); 2026-09-01 ('re-root widening' adjudicated as parity with existing behaviour); 2026-09-02 ('simulation artifact' verified by running the real worktree shape). 'Verify the decline the way a fold is verified—run the thing the seat could not (the real shape, the live consumer) and quote it.'
- **Confidence:** high

### 2026-09-02: WHEN YOU REINTERPRET DOCTRINE TO KEEP THE CHEAPER FORM, THAT IS THE FINDING — sever the plan so the licence holds literally, never defend the reading [tag: drafting-cycle]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: hand every cold reader the claim that buys something (the tier, the form, the skip) and ask it to falsify the claim against the doctrine's literal text; when the honest answer is 'the arm does not hold', change the plan until it holds rather than defending the reading
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a planner discipline rule: 'when you reinterpret doctrine to keep the cheaper form, that is the finding—sever the plan so the licence holds literally, never defend the reading.' The measured failure (2026-08-27, R4b: Planner narrowed 'no hand edits' to permit 4 hand-authored tests; the cold scout filed a DIRECTION-class HIGH; severing by moving tests into the builder was cheaper than arguing) and its recurrence (2026-09-01, 100011 hooks premise) establish this as a recurring class. The author benefits from the reading and is the wrong party to make it.
- **Confidence:** high

### 2026-09-02: ENUMERATE AN EDIT SURFACE FROM THE CALLEE, NEVER FROM ONE CALL'S SPELLING — then ask what other exits reach the same end state without calling it [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: enumerate an edit surface from the callee definition and count its callers; then list state transitions that reach the end state without calling it; if the count rises on each fresh read, derive it mechanically in the same run rather than re-reading
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a verification enumeration methodology rule: 'grep the DEFINITION and count its callers; then read each state transition the callee exists to accompany and list the transitions that happen without it.' The measured failure (fork-1 cycle, 2026-08-26): 'every terminal site' counted 3, then 6, then 7—each correction from a fresh reader. The first count grepped one call's argument form (variable name) and missed sites using differently-named variables; two of seven were exits that reached the terminal state without the call at all. Kin to the 2026-09-01 hand-enumerated-list entry.
- **Confidence:** high

### 2026-09-02: THE BIG FINDINGS COME FROM SEATS THAT READ SOMETHING NEW, NOT FROM MORE LENSES — budget the scout, the execution seat and the fold-set read; warm passes after the freeze return near zero [tag: drafting-cycle]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: budget the scout (cheapest HIGH per token), the execution seat (irreplaceable), and the capstone (keeps panel's own damage from shipping); cut warm walks before cutting any of these; give each seat something new to read
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a panel budget governance rule based on cross-cycle measurement: 'every HIGH came from one of three readers: the walk-0 scout, the EXECUTION seat, or the CAPSTONE reading the FOLD SET.' Data from four full-form panels (2026-08-26, two T2 cycles) and the 2026-09-01/02 cycles confirms warm walks after the freeze yield almost nothing. 'A seat that re-reads what a prior seat read is a warm pass with a cold label.'
- **Confidence:** high

### 2026-09-02: A REFUSED VERDICT IS A QUESTION ABOUT THE ACCEPTING PATH — read what acceptance would DO before reaching for the override [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before overriding a refusing bellows gate, read the code path that runs after acceptance and confirm it produces the intended outcome; override only a formal failure whose substance was independently verified, with the derivation in --ref
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a governance rule about bellows gate-override discipline: 'before overriding any refusing gate, read the code path that runs AFTER acceptance and confirm it produces the outcome you want.' The measured failure (2026-08-25 mini first dispatch): a continue on a terminal step means close-to-Done—overriding would have closed the plan as complete with its deposit never written. The inverse (2026-08-26, 2026-09-01 100013): override IS right when acceptance semantics produce the wanted outcome AND the failing gate is formal while the substance is independently verified, with evidence in --ref.
- **Confidence:** high

### 2026-09-02: INFRASTRUCTURE LIFETIME MUST MATCH ITS OWNER'S — a daemon hosted as a session's background task dies with the session, and its death masquerades as gate failures [tag: operational-recovery] [tag: multi-machine]


- **Suggested action:** Update MACHINE_SETUP.md (already begun at §4) and add rule to PLANNER_TEMPLATE.md: host long-running processes under an owner with matching lifetime (a terminal the operator owns, or launchd); never a session's background task for anything that must outlive the session
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes an operational governance rule already partially applied (MACHINE_SETUP.md §4 updated with the dashboard as the daemon's owner): 'host long-running processes under an owner whose lifetime is the job's: a terminal the operator owns, or launchd.' The measured failure: a bellows daemon hosted as a Claude session's background task SIGTERM-reaped after ~38 minutes with the session's process group, killing the dispatched claude -p agent mid-step (exit 143) and surfacing as five gate failures. 'When a step dies with a signal-shaped exit and a burst of gate failures, read the process's own facts before reading the gates.'
- **Confidence:** high

### 2026-09-02: A GATE THAT SELECTS ITS TARGET BY POSITION MAKES ORDER LOAD-BEARING — the parts of a plan form that look like formatting may be gate contracts [tag: bellows-integration]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: treat the order of declared paths and the per-step split of Deposits blocks as gate contracts when cloning a plan form; run the deposit extractor dry-run at walk 0 (§2.0 consumer dry-run) and quote what it picks; state the selection rule in MUST-PRESERVE until the gate documents it
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a governance rule about plan form discipline: 'when cloning a plan form, treat the ORDER of declared paths and per-step split of blocks as contracts until the gate's selection rule is read.' The measured case: bellows Rule 20 scans the FIRST .md in a step's Deposits block for the QA banner; a shared Deposits list with GOVERNANCE.md first caused the gate to scan doctrine for a self-check banner. The fix is structural—per-step Deposits blocks with the QA report first—and the extractor's preference for a full-suite .txt is the same class (2026-09-01, plans 100009–100016 all declare it).
- **Confidence:** high

### 2026-09-02: A RULING'S PROMISE CAN EXCEED ANY SOUND IMPLEMENTATION — supersede the record with evidence and ship the honest deliverable, never the unsound thing the text promised [tag: process-integrity]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when implementation shows a ruling promised more than is sound, ship the honest smaller deliverable plus a superseding note in the ruling's record, pushed before the plan closes; never let the plan title carry the ruling's promise when the body delivers less
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a ruling-integrity governance rule: 'the deliverable is the honest smaller thing PLUS a superseding note in the ruling's record, pushed before the plan closes.' The measured case (2026-08-26): R2 promised a registry read 'closes' the phantom-debt class; the panel proved no sound consumer could substitute for the local check (other machines' rows cannot prove THIS machine wrapped). Two wrong moves were available (build the unsound consumer, or ship less silently); the correct one was to supersede the ruling and name the deliverable honestly.
- **Confidence:** high

### 2026-09-02: A STATUS INDICATOR'S SCOPE CAN BE NARROWER THAN ITS LABEL — read the implementation of any version-ish field before acting on its value [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before a precondition keys on a displayed version, sha, count or state field, read the code that produces the field and state its scope in the plan; prove a restart by process facts (start time, pid) plus a canary through the changed path, not by a label
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a verification discipline rule about status indicator scope: 'before a precondition keys on a displayed version, sha, count or state, read the code that produces the field and state its scope in the plan.' The measured failure: status.py's header sha covers only bellows.py changes (git log -1 -- bellows.py), not the running daemon's checkout state—after a genuine restart onto new depositor and gates code the field still read the old sha, nearly blocking an already-satisfied precondition. Recurred 2026-09-01 (daemon reported 6b892a3 while main was at bff05d4).
- **Confidence:** high

### 2026-09-02: KEEP THE CONFIRMATION HARNESS-GENERATED WHEN SMOOTHING AN APPROVAL PATH — the plan's author must not also be its approver [tag: process-integrity]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when automating a human approval step, keep what the human sees generated by the harness (the literal command, the permission prompt), not paraphrased by the party wanting the approval; quote standing authorizations verbatim with date and session in each plan that relies on them
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes an approval-process governance rule: 'keep the thing the human sees generated by the harness, not paraphrased by the party who wants the approval.' The measured case (2026-08-27): allow vs ask for release commands—with allow, the gate's integrity rests on the Planner's summary being honest, and that gate exists precisely so the author is not the approver; ask was implemented (permissions.ask matching the absolute-path invocation). The 2026-09-01 standing release sentence is the same principle from the authorization side.
- **Confidence:** high

### 2026-09-02: A MIGRATION TO A BETTER SUBSTRATE DROPS THE OLD ONE'S FREE GUARANTEES — enumerate them and re-provide each before calling the migration done [tag: multi-machine] [tag: design]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: at any system-of-record migration, enumerate what the old substrate provided for free (history, durability, audit, replication, tooling) and re-provide each explicitly before calling the migration done; a snapshot is not a backup until it has been restored once
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a migration governance rule: 'list what the old substrate provided for free and re-provide each explicitly—for git to DB: backups with a restore test, retention, a second machine.' The measured failure (2026-08-24/25): moving thread state from git-synced markdown to Postgres fixed the collision problem and silently dropped git's free durability—no backup configured until someone asked, Time Machine had no destination. The lessons-forge DB move applied this rule (snapshots in knowledge/research/, fingerprint-proven identical). Kin to the 2026-08-25 superset-proof entry.
- **Confidence:** high

### 2026-09-02: A REMOTE TOOL SURFACE IS CACHED BY ITS CLIENTS — verify a surface change from the client's view, never by proving the server correct [tag: multi-machine]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: after changing what a server exposes, verify the surface from the client's view (list the client's tool set, --help, or environment) and re-attach or restart the client when the listing is stale; name the client-side step in the plan that changes the server
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a multi-machine verification governance rule: 'after changing what a server exposes, list the surface FROM the client and quote it; re-attach or restart the client when the listing is stale.' The measured failure (2026-08-25): tuyere MCP server tool list changed, clients kept the stale list—the connector advertised an obsolete tool until removed and re-added. Proving the server side correct said nothing about what any client saw. The same class governs: a client's tool listing, a harness's hook list, a session's environment.
- **Confidence:** high

### 2026-09-02: A CLAIM DOING ARGUMENTATIVE WORK GETS CHECKED BEFORE IT IS OFFERED — a recalled fact repeated as the basis for a recommendation is a fresh assertion each time [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before offering a recalled fact as the basis for a recommendation, run the command that would falsify it; a recalled fact repeated as the basis for a recommendation is a fresh assertion each time, not a cached one
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a planner discipline rule: 'before a fact is offered as the reason for a recommendation, run the one command that would falsify it; the cost of being wrong scales with each repetition, because each is a fresh assertion the listener cannot audit.' The measured failure (2026-09-01 cycle): the Planner told the CEO 'the builder has not moved since walk 0' at walks 6, 7, and 8 as basis for stopping; git log on the file showed three commits, first run at walk 9 when a lens asked. Kin to the 2026-08-13 attestation entry (record written from intention); this is the rule for a claim offered as evidence in conversation.
- **Confidence:** high

### 2026-09-02: READ A TOOL'S ARGUMENT SURFACE BEFORE RUNNING OR QUOTING ONE OF ITS ARMS — a tool with several arms runs the wrong one silently and successfully [tag: planner-discipline]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: before quoting or running a command whose effect matters, read its --help or module docstring and name the arm; when a tool's default arm is a loop or re-entry, the checklist names the non-default arm explicitly
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a planner discipline rule: 'before quoting a command to the CEO or running one whose effect matters, read its --help or docstring and name the arm in the plan text.' The measured failure: clear_plan.py <hold_file> ran the DEFAULT arm (re-entry, renames hold- to ready-) rather than --release-class-hold; the depositor re-held the plan within seconds. Same session: cycle_check run against the register path when it takes the plan path. MACHINE_SETUP.md §6 now names each act's tool AND arm—this entry generalizes that to a PLANNER_TEMPLATE rule.
- **Confidence:** high

### 2026-09-02: A WORD THAT NAMES BOTH A MACHINE AND A ROLE WILL CARRY THE MACHINE INTO DOCTRINE — define the role, name the machine, and never let one word do both [tag: multi-machine]


- **Suggested action:** Update COMPANY.md to clarify: define the role (e.g. 'shop'), name the machine (e.g. 'the Air', 'the mini'); never let one word serve both as role and machine name; when a ruling changes a word's meaning, sweep every in-flight artifact as a DC fold round (DC §2.7)
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes a vocabulary governance rule: 'when a term names a role, doctrine defines the ROLE and prose names the MACHINE; a sentence that says the <role> for a machine is stale the moment a second machine holds the role.' The measured failure: 'the shop' meant the governance-root role in COMPANY.md (2026-05-19) and, by habit, the MacBook Air; when the mini came up, baton, MACHINE_SETUP.md and bellows/CLAUDE.md all wrote 'the shop' for the Air, and a plan drafted under that usage carried 'the shop's state' into a governance file's replacement text the same day the CEO retired the usage (2026-09-02). Caught and folded as a DC round (eleven sites).
- **Confidence:** high

### 2026-09-02: A PANEL ROUND RECORDED AS A WARM WALK TRIPS THE CONVERGENCE CHECKER — panel yield is structural, so it lives on the cold-panel line, never on a `wN` lens line [tag: drafting-cycle]


- **Suggested action:** Add rules to PLANNER_TEMPLATE.md: (1) record panel rounds on the cold-panel line with per-seat counts and instruction/record split; keep wN lens lines for warm walks only; (2) place the ## Drafting Cycle block above the first step heading
- **Reasoning:** [AUTHOR-CONFLICT] Entry proposes two specific formatting governance rules for PLANNER_TEMPLATE: 'record panel rounds on the cold-panel line...keep wN lens lines for warm walks only, so the convergence checker reads convergence' and 'place the ## Drafting Cycle block above the first step heading; a trailing block is read as step text by the last-step extractors.' The measured failure: five execution-seat folds recorded as w2 lens lines after a two-fold walk 1 caused cycle_check to return ESCALATE:yield-rising on a converging cycle; moving the round to the cold-panel line returned CONTINUE then BAR_MET. The trailing-block WARN was measured the same day.
- **Confidence:** high

### 2026-09-01: TWO RECORDS OF ONE FACT WILL DIVERGE UNLESS ONE IS A PROJECTION OF THE OTHER — a status written from READING contradicted the routing record, and the reader never knew there was a record [tag: process-integrity] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: designate one record as the authoritative source for any shared fact; make every other representation a projection derived by tooling, never hand-edited
- **Reasoning:** Entry proposes the projection rule: 'pick the record that machinery ACTS on as the authority and make every other copy a PROJECTION of it.' The measured failure—313 headings with status stored as both a file marker (3 values) and a DB column (7 values) diverging silently, leaving the backlog at 5x its true size—demonstrates the need for a governance rule mandating single-source authority. The fix is documentary: PLANNER_TEMPLATE must name the pattern and require projections to use the authority's vocabulary.
- **Confidence:** high

### 2026-09-01: THE MACHINE THAT IS NOT WORKING IS THE COLD READER — a non-executing machine has the non-author profile by construction, and the role is dynamic [tag: process-integrity] [tag: multi-machine]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: route every non-author or cold read to the machine holding no active claim at that moment; expect a packet as output, never a direct write; apply the packet where the stores live
- **Reasoning:** Entry proposes a governance rule for Gate-1 non-author selection: 'the role is not a fixed assignment; it is whichever live machine holds no active claim at that moment.' The two deciding facts (heartbeats and plan claims) already live in the shared queue DB, so the selection criterion is mechanically derivable. The measured case (24 proposals routed from git-shared artifacts alone, writes refused by the cold machine's permission layer as designed) validates the packet-based pathway proven for W=28.
- **Confidence:** high

### 2026-09-01: ABSENCE IS THE CORRECT STATE EVERYWHERE BUT THE HOME — a check for a store that lives on ONE machine must know which machine that is, or it becomes a standing false alarm on every other [tag: verification] [tag: multi-machine]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: checks for a single-home store carry the home machine as part of their contract; on any other machine absence is the expected state and the check reports INFO once, not WARN per tick; a resolver returns None when no candidate holds a real store
- **Reasoning:** Entry proposes a verification design rule: 'every check that reads it carries the home as part of its contract: on the home machine absence is a fault; on any other machine absence is the expected state.' The measured failure—the daemon on the Air logging 'cannot read lessons-forge.db' at every tick after the DB moved to the mini—is the false-debt class: a recurring warning about a condition the design guarantees, training the operator to ignore the channel. The fix (resolver returns None, check says INFO once) is a rule for how to write checks for single-home stores.
- **Confidence:** high

### 2026-09-01: TWO INDEPENDENT COLD READERS OF ONE STATE OVERLAP ON ROUGHLY HALF THEIR FINDINGS, AND EACH FINDS WHAT THE OTHER MISSED — a single cold seat measures the artifact; a second measures the first seat's blind spot [tag: drafting-cycle] [tag: verification]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: when a second cold pathway is cheap (idle machine, fresh context, same brief), convene it and read the two reports as a pair; the intersection is the artifact's measured floor; the symmetric difference is the seat's blind-spot size
- **Reasoning:** Entry proposes a governance rule for the drafting cycle panel: 'a cold seat's dry return is a statement about that reader, not about the artifact.' The measured finding—two readers sharing 6 of 19 distinct findings in scout, 1 of 20 in discovery, the symmetric difference as large as the overlap—demonstrates that the seat count is still buying findings when the difference is large. The rule: convene the second seat and read the reports as a pair, treating each reader's dry regions as that reader's instrument limit.
- **Confidence:** high

### 2026-09-01: A DESIGN CAPTURED FROM CONVERSATION IS A HYPOTHESIS ABOUT THE RECORD — survey the live checkouts before the thread, and deposit the surveys beside the analysis [tag: process-integrity] [tag: multi-machine]


- **Suggested action:** Add rule to PLANNER_TEMPLATE.md: a design captured from conversation is a hypothesis; run read-only surveys (fan-out, file:line citations, absences stated with their probe) BEFORE sketching; deposit survey reports under knowledge/research/ as research artifacts and cite them from the analysis
- **Reasoning:** Entry proposes a mandatory sequencing rule for design methodology: 'a design idea is captured in two acts, in this order: the SURVEY (fan-out, read-only, file:line, absences stated with their probe), then the SKETCH.' The measured failure—6 of 6 load-bearing conversation facts wrong (queue had no executor, no headroom datum, liveness/claims split across processes, serialization was Planner discipline not code)—demonstrates that a sketch written first carries wrong premises into the plan. The corrected analysis inverted one of five claims and gated two more.
- **Confidence:** high
