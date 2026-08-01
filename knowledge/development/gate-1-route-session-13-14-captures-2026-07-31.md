# Gate 1 Route — Session 13/14 Proposals (Plan 289, Step 1)

## Task A — Route Writes

Six `set_proposal_route(conn, id, 'codify')` calls executed in a single transaction:

```
set_proposal_route(conn, 201, 'codify')
set_proposal_route(conn, 202, 'codify')
set_proposal_route(conn, 203, 'codify')
set_proposal_route(conn, 204, 'codify')
set_proposal_route(conn, 205, 'codify')
set_proposal_route(conn, 206, 'codify')
conn.commit()
```

## Task B — Absolute Post-State Verification

### B1 — Read-back of all 6 rows (absolute — no before-anchor)

```
id   entry_id  status    route   category         target_artifact    
---  --------  --------  ------  ---------------  -------------------
201  193       proposed  codify  governance_rule  PLANNER_TEMPLATE.md
202  194       proposed  codify  governance_rule  DRAFTING_CYCLE.md  
203  195       proposed  codify  governance_rule  PLANNER_TEMPLATE.md
204  196       proposed  codify  governance_rule  DRAFTING_CYCLE.md  
205  197       proposed  codify  governance_rule  PLANNER_TEMPLATE.md
206  198       proposed  codify  governance_rule  DRAFTING_CYCLE.md
```

### B2 — Status distribution (anchor: before-item (1))

```
implemented|147
superseded|28
rejected|15
reference|7
proposed|6
stale|3
```

Byte-identical to before-item (1). No status moved.

### B3 — Same-instant identity (one statement, one snapshot)

Command: `SELECT (SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL), (SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL AND id NOT BETWEEN 201 AND 206);`

```
76|70
```

Identity: 76 == 70 + 6. HOLDS.
Rise over before-item (2): 76 - 70 = 6 (equals 6, within bound of <= 6).

## Task C — Blast Radius

### C1(a) — Outside-range count (anchor: before-item (4))

```
70
```

Equals before-item (4) = 70. UNCHANGED.

### C1(b) — Outside-range row image (anchor: before-item (4b))

```
131:codify
132:codify
133:codify
134:codify
135:codify
136:codify
137:codify
138:codify
139:codify
140:reference
141:reference
142:codify
143:codify
144:codify
145:codify
146:reference
147:codify
148:codify
149:codify
150:codify
151:codify
152:codify
153:codify
154:codify
155:codify
156:codify
157:codify
158:codify
159:codify
160:codify
161:backlog
162:codify
163:codify
164:reference
165:codify
166:codify
167:codify
168:codify
169:backlog
170:codify
171:codify
172:codify
173:codify
174:codify
175:codify
176:codify
177:codify
178:codify
179:codify
180:codify
181:codify
182:codify
183:reference
184:codify
185:codify
186:codify
187:codify
188:codify
189:codify
190:codify
191:codify
192:codify
193:codify
194:codify
195:codify
196:codify
197:codify
198:codify
199:codify
200:codify
```

Byte-identical to before-item (4b). UNCHANGED.

### C2 — get_unclassified_entries (anchor: before-item (3))

```
[]
```

Unchanged from before-item (3) = `[]`.

---

## Output Receipt

**Status: Complete**

### Item 0 — A0-pre set-identity assertion (pre-write)

Raw output of `SELECT id FROM lesson_proposals WHERE status='proposed' ORDER BY id`:

```
201
202
203
204
205
206
```

Exactly 6 rows, exactly {201, 202, 203, 204, 205, 206}.

### Item 0b — Resume Declaration

RESUME: no

### Item 1 — before-item (1): full status distribution (pre-write)

```
implemented|147
superseded|28
rejected|15
reference|7
proposed|6
stale|3
```

Total: 206.

### Item 2 — before-item (2): TOTAL route-NOT-NULL count (pre-write)

```
70
```

### Item 3 — before-item (3): get_unclassified_entries (pre-write)

```
[]
```

### Item 4 — before-item (4): OUTSIDE-RANGE route-NOT-NULL count (pre-write)

```
70
```

Distinct from item (2) even though both read the same number at this snapshot — they diverge after the write (total becomes 76, outside-range stays 70).

### Item 4b — before-item (4b): OUTSIDE-RANGE row image (pre-write)

```
131:codify
132:codify
133:codify
134:codify
135:codify
136:codify
137:codify
138:codify
139:codify
140:reference
141:reference
142:codify
143:codify
144:codify
145:codify
146:reference
147:codify
148:codify
149:codify
150:codify
151:codify
152:codify
153:codify
154:codify
155:codify
156:codify
157:codify
158:codify
159:codify
160:codify
161:backlog
162:codify
163:codify
164:reference
165:codify
166:codify
167:codify
168:codify
169:backlog
170:codify
171:codify
172:codify
173:codify
174:codify
175:codify
176:codify
177:codify
178:codify
179:codify
180:codify
181:codify
182:codify
183:reference
184:codify
185:codify
186:codify
187:codify
188:codify
189:codify
190:codify
191:codify
192:codify
193:codify
194:codify
195:codify
196:codify
197:codify
198:codify
199:codify
200:codify
```

70 rows.

### Item 5 — After-values (B1/B2/B3/C1/C2)

- **B1** (absolute — no before-anchor): All 6 rows `route='codify'`, `status='proposed'`, category and target_artifact match disposition table per row. PASS.
- **B2** (anchor: before-item (1)): Status distribution byte-identical. PASS.
- **B3** (same-instant identity): `76|70` → 76 == 70 + 6. PASS. Rise over item (2): 6.
- **C1(a)** (anchor: before-item (4)): Outside-range count = 70, unchanged. PASS.
- **C1(b)** (anchor: before-item (4b)): Row image byte-identical, 70 rows. PASS.
- **C2** (anchor: before-item (3)): `[]`, unchanged. PASS.

### Item 6 — Restore point

Absolute path: `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate1-289-20260801T172238Z.db`

Verification:
- Size: 937,984 bytes (non-zero)
- `PRAGMA integrity_check` → `ok`
- Backup counts: lesson_entries 198, lesson_proposals 206
- Live counts: lesson_entries 198, lesson_proposals 206
- Match confirmed.

### Item 7

#### Files Created or Modified

- `knowledge/development/gate-1-route-session-13-14-captures-2026-07-31.md`

### Item 8 — Flags and HALT conditions

No HALT conditions encountered. No flags raised. All tasks A00, A0-iso, A0-pre, A0-snap, A, B1, B2, B3, C1(a), C1(b), C2 completed cleanly.

---

## Execution Notes

- A0-iso interval: 11 seconds between quiescence reads (12:23:03 → 12:23:14). Both reads identical.
- A0-iso positive signal: `in-progress-executable-289.md` found in `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/`. No other in-progress or verdict-pending plan present.
- All before-snapshots match authoring expectations (no drift detected).
- This is a cheap sanity read, not a concurrency guard.

### Ledger Updates

#### Prompt Feedback

None.
