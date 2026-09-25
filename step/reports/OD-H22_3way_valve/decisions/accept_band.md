# Owner acceptance of BAND_NOT_MET — OD-H22_3-way-valve

- **Who accepted:** Ikbal (project owner).
- **When:** 2026-09-25 11:48 UTC.
- **How:** decision card in the project thread, option "Accept and deliver" chosen.

## Gate this acceptance is tied to

- `qa/gate.json` sha256 (full): `89a14a86f4d4880e036cd1a47f20416782db9419d725f667f0a01825618ef557`
- `qa/gate.json` `created`: `2026-09-25T11:45:11+00:00`

## Bands missed (verbatim from `qa/gate.json#band_fails`)

- `scan_to_cad:masked: p95 0.235 max 1.427 vs 0.3/0.8`
- `cad_to_scan_observable: p95 1.484 max 4.858 vs 0.3/0.8`

## Reasons shown to the owner on the decision card

- scan→CAD p95 0.235 passes ≤0.30.
- max 1.43 vs ≤0.80 comes from stray scan material inside the +X ear hole, which the photos show as open.
- CAD→scan fails (p95 1.48) because of bores the scanner never reached.
- A rebuild without new data cannot fix either miss.

## Decision

Ikbal chose "Accept and deliver" on the decision card described above, accepting the
`scan_to_cad` and `cad_to_scan_observable` band misses recorded in gate
`89a14a86f4d4` (created 2026-09-25T11:45:11+00:00), for the reasons shown to him on
that card, quoted verbatim above. Nothing beyond what the card stated and what the
owner chose is recorded here.
