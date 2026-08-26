# Dev Log — forge-cycle-w3 — 2026-08-26

## Pre-flight (read-only)

| pin | measured | expected |
|---|---|---|
| M3 (proposal count) | 410 | 410 |
| M3 (all terminal) | yes (implemented:311, superseded:29, rejected:38, stale:3, reference:29) | all terminal |
| M6 (entry count) | 402 | 402 |
| M2 (unclassified) | 0 | 0 |
| MAXP | 410 | 410 |
| MAXE | 402 | — |
| M8 (corpus sha256) | f80937e06472600872c2a4b36fddc1d03471e8d6cba7ae90cae2f0368db7ed4f | prefix f80937e06472600872c2 |

## M5 pre-flight triple-set (ids 1–410)

410 triples captured. Status distribution: implemented:311, superseded:29, rejected:38, stale:3, reference:29. Route distribution: None:156, codify:224, reference:20, backlog:10.

## Ingest result (M1)

```json
{"inserted": 3, "updated": 0, "unchanged": 345}
```

## Dispositions

```
DISPOSITION | entry=403 | proposal=411 | category=governance_rule | markers: NONE
DISPOSITION | entry=404 | proposal=412 | category=governance_rule | markers: AUTHOR-CONFLICT
DISPOSITION | entry=405 | proposal=413 | category=governance_rule | markers: AUTHOR-CONFLICT
```

## Fresh-connection post probes

| pin | measured | expected |
|---|---|---|
| M2 (unclassified) | 0 | 0 |
| M3 (proposal count) | 413 | 413 |
| M4 (new non-proposed) | 0 | 0 |
| M6 (entry count) | 405 | 405 |
| M7 (AUTHOR-CONFLICT markers) | 2 | 2 |
| M5 (set-identical) | True | True |
