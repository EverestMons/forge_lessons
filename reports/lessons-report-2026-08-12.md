# Lessons Report — 2026-08-12


## Summary


| Category | Count |
|---|---|
| governance_rule | 3 |
| instrumentation | 3 |

**Total proposals:** 6


## Governance Rule


### 2026-08-12: Meter the panel from seat 0 — a meter added at seat 4 permanently lost seat 1's cost [tag: drafting-cycle]


- **Suggested action:** Add one sentence to DRAFTING_CYCLE.md §2.6: the meter line is created when the panel convenes (before seat 1 is dispatched), and each seat cost is recorded at its fold, not at panel close. The seat-prompt template carries a meter slot per seat, making omission visible at dispatch time.
- **Reasoning:** Entry documents a measured loss: the gate2-pt3 panel meter was added at seat 4, permanently losing seat 1 token count (recorded as LOST, unrecoverable). The How-to-apply prescribes a single governance sentence in §2.6 fixing the timing, plus a template slot. The fix is a documentary rule change to DRAFTING_CYCLE.md specifying when the meter must be created — a governance_rule edit with a mechanism carrier (the template meter slot).
- **Confidence:** high

### 2026-08-12: The executing seat has no brief — six-for-six HIGHs came from RUNNING the machinery, and the streak broke exactly where the machinery was already run five times [tag: drafting-cycle]


- **Suggested action:** Add an execution brief to the §2.6 registry: run every stated probe/command/rehearsal scratch-only, log expected-vs-measured per command, aim at whatever the cycle has not yet executed, and carry the scratch contract verbatim (DB copies by absolute path, builder scratch-to-scratch, never-name-the-live-file-as-output, mirror rule). Layer on the vulnerabilities seat by default.
- **Reasoning:** Entry identifies that the vulnerabilities seat HIGH streak (six consecutive panels) traces to EXECUTING machinery other seats only read, yet §2.6 registry carries no execution brief — so scratch-only guardrails are re-spelled ad hoc in every prompt. The gate2-pt3 seat 3 ran 36 scratch-only rehearsals returning 0 HIGH on a clone whose machinery three walks and two prior seats had already executed — confirming execution yield concentrates where nothing has executed before. The How-to-apply prescribes a new brief entry in the §2.6 registry (a documentary addition to a governance file) with defined guardrails.
- **Confidence:** high

### 2026-08-12: Cold-front timing is a SHAPE decision, not a bullet — cold passes return 7× the pre-existing yield while warm walks find their own fold damage [tag: drafting-cycle]


- **Suggested action:** Route as a decision packet to the shape session — do NOT fold as a §2.6 bullet. The packet carries: the origin table, the 7x cold-vs-warm yield numbers, the gate2-pt3 walk-vs-panel split, and the fresh-readers register as evidence. The shape session decides how to re-allocate between warm-walk and cold-panel phases. The standing heuristic holds as practice until then.
- **Reasoning:** Entry explicitly says "do NOT fold this as a §2.6 bullet — it re-shapes the walk/panel boundary the whole doctrine is built on." The cold-front timing question (cold passes returning 7x the pre-existing yield while warm walks generate fold damage, 31 of 50 warm findings being the warm cycle own fold damage) is a shape decision affecting the entire §2.6 structure, not a single-sentence codification. Classification as governance_rule with medium confidence reflects the entry own routing: a CEO decision packet, not an agent-actionable edit.
- **Confidence:** medium

## Instrumentation


### 2026-08-12: The cold panel's operational layer is lore — seat prompts carry the safety contract and no artifact carries the seat prompts [tag: drafting-cycle]


- **Suggested action:** Create PANEL_SEAT_TEMPLATE.md carrying the invariant seat-prompt body (read-only contract, environment facts, mirror-lint mandate, incremental-report format, report schema) with per-seat slots for lens, brief, and artifacts. Add a §2.6 seat-prompt contract clause naming the template as the mandatory source for all panel seat prompts, so the mirror-lint mandate binds every future panel.
- **Reasoning:** Entry proposes mechanizing the seat-prompt operational layer via a new artifact. The How-to-apply explicitly names a PANEL_SEAT_TEMPLATE.md and a §2.6 clause — a new procedural mechanism (the template) plus a governance handle (the clause). The core problem is that seat prompts carrying safety-bearing content (the contract, the mirror rule, the incident mandate from the gate2-pt3 daemon-claim event) exist only in session lore and are rebuilt from doctrine each time, creating unreviewed re-derivations of safety artifacts. The fix is instrumentation: a template artifact that makes the invariant body reviewable and versionable.
- **Confidence:** high

### 2026-08-12: Panel registers coarsen to one-row-per-seat in every instance — a deviation declared by ALL members of a class is a schema amendment owed [tag: drafting-cycle]


- **Suggested action:** Amend the walk-register schema to 0.2: (1) a sanctioned per-seat panel row form (seat, brief, counts by severity and class, origins, sites) replacing the per-finding form both panels independently converged on; (2) the Deviations line commit-range convention carries a defined open tail ("plus the closing commit, named in the wrap") instead of per-cycle improvisation.
- **Reasoning:** Entry observes that every panel instance filed the same deviation from register schema 0.1 (coarsening from per-finding to per-seat rows), and the Deviations line structurally cannot name its own closing commit. When every instance of a class deviates the same way, the schema is wrong, not the instances. The How-to-apply prescribes schema 0.2 — a new format definition (instrumentation) for the walk register, codifying what both registers converged on independently.
- **Confidence:** high

### 2026-08-12: The warm walk's mechanical/judgment split transfers to the panel — four structures that cut the replication layer without touching discovery [tag: drafting-cycle]


- **Suggested action:** Implement four panel-mechanism transfers from warm walks to cut the replication layer: (1) panel-0 pin table as claims-to-attack with paired measure commands; (2) machine-readable pins plus a scripted inter-seat battery draining the MATCH class after every fold; (3) pre-built hunk maps for the clone-diff seat; (4) new-surface handoffs via per-seat commit diffs. These are the HOW behind entries 320/321/322 — bundle as one §2.6 codification plan. Seat fusion (five seats to three) stays CEO-reserved, route to shape packet with entry 323.
- **Reasoning:** Entry proposes four specific mechanisms transferring the warm walk mechanical/judgment split to the panel, sized at a ~35% panel cost cut (458k to ~240k) with the discovery layer untouched. The How-to-apply names these as the HOW behind the meter (entry 320), execution brief (entry 321), and schema (entry 322) entries. The line-to-hold: script only the MECHANICAL layer — the artifact read, aimed-brief judgment, and author-verify stay fully cold, and the executing seat still runs mutating machinery end-to-end once. These are new procedural mechanisms (instrumentation), not documentary rule changes.
- **Confidence:** high
