# Dev Log — Cycle Run 339, Step 1 (Ingest) — 2026-08-10

Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)

**Dispatch determination:** FRESH — dev log absent from HEAD (exit 128), working tree (exit 1), and `git log --all` (exit 0, empty output; positive control on `knowledge/FORWARD.md` confirmed output appears). No `bellows-preserved/*` branches found.

## Restore Point

Pristine backup path: `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-339-20260810T234901Z.db`
- Integrity check: `ok`
- BACKUP_ENTRIES=265, BACKUP_PROPOSALS=273 (matches live DB)

## Baseline Captures

E0=265
P0=273

### Sentinel (entry 265)

SENTINEL_HASH=c30fdaff226570c030e544648af0bc6096ff633452795387abada9d00a07fa83

### STALE_COUNT

STALE_COUNT=3

### SURFACEABLE_BASE

SURFACEABLE_BASE=0 (proposed=0, ambiguous=0)

### Status Distribution (zero-emitting, pre-ingest)

```
accepted|42
ambiguous|0
implemented|171
proposed|0
reference|14
rejected|15
stale|3
superseded|28
```

### Category Distribution (pre-ingest)

```
duplicate|19
governance_rule|228
instrumentation|11
narrative|5
structural|10
```

### NT Capture (raw)

NT_COUNT=42

```
223|215|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: The register append succeeded, recorded a pointer, and lost every item — a channel can fail a third distinct way [tag: bellows-integration]
224|216|accepted|codify|DRAFTING_CYCLE.md|2026-08-03: A ledger constraint that ENUMERATES decays as oscillation, not staleness [tag: drafting-cycle]
225|217|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: A rule authored in the VERIFIER is a rule the producer never reads [tag: planner-discipline]
226|218|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: A plan's claim about what a gate enforces is a claim to verify, not to inherit [tag: bellows-integration]
227|219|accepted|codify|DRAFTING_CYCLE.md|2026-08-03: "The newest same-class plan" is a measurement, not something you recall [tag: planner-discipline]
228|220|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: A self-check that reads the DEPOSIT cannot verify a channel that parses the TRANSCRIPT [tag: bellows-integration]
229|221|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: items-in equals items-out, and the item still arrives truncated [tag: verification]
230|222|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: Machinery added to close a durability gap clobbered the artifact it protected, on the exact path it was built for [tag: planner-discipline]
231|223|accepted|codify|DRAFTING_CYCLE.md|2026-08-03: Renaming an excuse launders it past the rule that already forbids it [tag: planner-discipline]
234|226|accepted|codify|DRAFTING_CYCLE.md|2026-08-03: Delete the check, not its label — and verify by the check's absence [tag: planner-discipline]
235|227|accepted|codify|DRAFTING_CYCLE.md|2026-08-03: A structural cut is an edit, and it has its own defect class [tag: planner-discipline]
236|228|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: In a block parsed subsection by subsection, the LAST subsection is the exposed one [tag: bellows-integration]
237|229|accepted|codify|DRAFTING_CYCLE.md|2026-08-03: A pipe masks the exit code, and it caught four independent readers in one session [tag: verification]
239|231|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: Two gates over the same list pull in opposite directions — required versus tolerated [tag: verification]
240|232|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: A pin whose extraction method is unstated is unreproducible, and it fails closed on the honest path [tag: verification]
241|233|accepted|codify|DRAFTING_CYCLE.md|2026-08-03: The sweep fails at maximum context — the fix and the missed sibling get written in the same sitting [tag: planner-discipline]
242|234|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: An independent referent sourced from the actor's own record is not independent [tag: verification]
243|235|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: A backup must sit adjacent to the write it inverts, or it is not an inverse [tag: planner-discipline]
244|236|accepted|codify|PLANNER_TEMPLATE.md|2026-08-03: A zero-difference result needs an inverse control before it means anything [tag: verification]
248|240|accepted|codify|DRAFTING_CYCLE.md|2026-08-04: A retraction that names its own scope can still be incomplete, and a consumer sweep that probes the wording misses the claim [tag: planner-discipline]
249|241|accepted|codify|DRAFTING_CYCLE.md|2026-08-04: A guard can be safe by accident — executing the real check distinguishes design from luck [tag: verification]
250|242|accepted|codify|PLANNER_TEMPLATE.md|2026-08-04: A measurement must be taken by the method the plan mandates, or it is a prediction [tag: verification]
251|243|accepted|codify|DRAFTING_CYCLE.md|2026-08-05: Naive probes degrade as an artifact accumulates its own retraction history [tag: verification]
252|244|accepted|codify|DRAFTING_CYCLE.md|2026-08-05: A closing line written before the cycle's last phase is wrong by construction [tag: planner-discipline]
253|245|accepted|codify|DRAFTING_CYCLE.md|2026-08-05: An overloaded token appears in prose far more often than in its real position — first-match probes land hundreds of lines early [tag: verification]
254|246|accepted|codify|DRAFTING_CYCLE.md|2026-08-05: Copying a guard from a parent plan is not the same as copying its history [tag: planner-discipline]
255|247|accepted|codify|PLANNER_TEMPLATE.md|2026-08-06: A success criterion must declare its polarity — and three individually-correct patches mean the REGION is wrong, not the patches [tag: planner-discipline]
256|248|accepted|codify|DRAFTING_CYCLE.md|2026-08-06: The error that FLATTERS your own argument is the one no gate catches [tag: planner-discipline]
257|249|accepted|codify|PLANNER_TEMPLATE.md|2026-08-06: A recorded lesson does not bind the author who recorded it — measured four times in one cycle [tag: planner-discipline]
260|252|accepted|codify|DRAFTING_CYCLE.md|2026-08-06: An UN-walked plan lints CLEAN while a fully-walked one WARNs — measured on one artifact across one cycle [tag: instrumentation]
261|253|accepted|codify|DRAFTING_CYCLE.md|2026-08-06: The negative-result standard was adopted for agents that morning and never applied to my own probes [tag: verification]
262|254|accepted|codify|DRAFTING_CYCLE.md|2026-08-07: A conformance probe must match the REPRESENTATION, not the spec's prose [tag: verification]
263|255|accepted|codify|DRAFTING_CYCLE.md|2026-08-07: A fix can break its own DESCRIPTION — re-verify the describing sentence after the fold [tag: drafting]
264|256|accepted|codify|PLANNER_TEMPLATE.md|2026-08-07: A directional insert on a PREFIX anchor lands on the wrong side and passes the line-count proof [tag: mechanics]
265|257|accepted|codify|PLANNER_TEMPLATE.md|2026-08-07: Commit scoping lives on the COMMIT, not the add [tag: mechanics]
266|258|accepted|codify|PLANNER_TEMPLATE.md|2026-08-07: Line numbers cited inside shipped code are load-bearing couplings for every doc edit [tag: instrumentation]
267|259|accepted|codify|PLANNER_TEMPLATE.md|2026-08-07: A parent deposit can carry a DIRECTIVE to a future plan — sweep for them when authoring the successor [tag: drafting]
268|260|accepted|codify|PLANNER_TEMPLATE.md|2026-08-07: A threshold clause written at a POLE silently drops the mid-band [tag: design]
269|261|accepted|codify|PLANNER_TEMPLATE.md|2026-08-07: A recovery branch must produce everything the downstream consumers read [tag: design]
270|262|accepted|codify|DRAFTING_CYCLE.md|2026-08-07: `grep -c` counts LINES — an intra-line duplicate is invisible to it [tag: verification]
272|264|accepted|codify|DRAFTING_CYCLE.md|2026-08-07: A foreign constraint id cited by bare number binds to the LOCAL ledger [tag: drafting]
273|265|accepted|codify|DRAFTING_CYCLE.md|2026-08-07: A true record invisible to the checker's grammar reads as false — write records in the checker's representation [tag: instrumentation]
```

### Accepted|codify IDs (the 42)

223, 224, 225, 226, 227, 228, 229, 230, 231, 234, 235, 236, 237, 239, 240, 241, 242, 243, 244, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 272, 273

## Doctrine Pins

```
0964e1a70d6752f8656051b865ebcbdf76cb3e35e1b12415e547b54c45e4a7c7  /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md
eb767e3284f1a42b70aec9b3a1ab50226a13276f31f854d4117de26de4815b5f  /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md
d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0  /Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md
```
