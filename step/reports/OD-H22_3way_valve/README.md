# OD-H22 3-way valve — scan → STEP reverse-engineering report

![scan vs CAD overlay](qa/overlays/overlay.png)

| | |
|---|---|
| Part | `OD-H22` (ref 43, OEM AS00004266) — molded plastic 3-way valve body |
| Input | [`scans/OD-H22_3way_valve/OD-H22_3way_valve_raw.stl`](../../../scans/OD-H22_3way_valve/) — 495 881 triangles, full resolution, + 4 photos |
| Method | staged pipeline — intake → measure → build (build123d, features F01–F12 from 52 parameters) → **independent verifier** (own ICP, zones, masks) → deliver |
| Caliper data | **none** — scan-only (48 parameters from the scan, 4 assumed) |
| Verdict | **`BAND_NOT_MET` — accepted by the owner for delivery** ([`decisions/accept_band.md`](decisions/accept_band.md)) |

**Full report: [`deliver/README.md`](deliver/README.md)** (method, frames, all parameters, per-zone deviation, masks, clusters, limitations, reproduction, provenance).

## Delivered STEP

| File in this repo | = file in the run | Frame |
|---|---|---|
| [`step/OD-H22_3way_valve.step`](../../OD-H22_3way_valve.step) — **use in CAD** | `build/OD-H22_3-way-valve_datum.step` | datum: flange back face = Z 0, valve axis = +Z, ear axis = +X |
| *(not published)* | `build/OD-H22_3-way-valve.step` | original scan coordinates — apply the inverse of `intake/alignment.json#matrix_4x4` to the datum STEP to overlay it on the raw scan |

The repo copy differs from the run files only in the STEP product / solid name (`OD-H22 3-way valve`), so the sha256 values in `deliver/MANIFEST.json` refer to the run original.
The run's meshes (`input/scan.stl`, `intake/*.stl`, `build/*_cad.stl`) are not duplicated here — the raw scan is in `scans/OD-H22_3way_valve/`.

Re-import check: 1 valid closed solid, 162 faces (93 plane, 60 cylinder, 8 torus, 1 cone — 100 % analytic), volume 6 395.6 mm³, datum bbox 41.75 × 39.88 × 44.55 mm.

## Deviation gate (independent verifier, `qa/VERDICT.md`)

| Gate | Band | Measured | Result |
|---|---|---|---|
| scan → CAD (masked) | p95 ≤ 0.30 / max ≤ 0.80 | p95 **0.235** / max 1.43 | FAIL (max only) |
| CAD → scan (observable) | p95 ≤ 0.30 / max ≤ 0.80 | p95 1.48 / max 4.86 | FAIL |
| Validity, datum audit, ICP registration | — | — | PASS |

- **scan → CAD p95 0.235 mm passes** — the best surface fit of the rebuilds so far (flowmeter 0.359, pump 0.448, thermoblock 0.474).
- The max 1.43 mm is stray scan material inside the +X ear screw hole, which the photos show as open.
- CAD → scan fails because of bore interiors the scanner never reached (16 % of CAD points sit next to scan holes).
- The +X ear tip of this specimen is damaged; the CAD follows the intact −X ear by symmetry (mask M1). Photo 4 suggests the ear-tip lump may be a real pip — open question.
- Port interiors are modeled as plain bores (assumed); photo 4 shows internal structure there.

Functional-interface zones, scan → CAD p95: flange back face + ear holes 0.17 · drive tube + collar 0.22 · ports + clip blocks 0.30.
Fine for chassis layout and the valve mount (`OD-C07`); confirm ear-hole spacing, port OD and drive-tube OD with calipers before freezing the mount.

## Folder map

`intake/` datum + alignment + noise · `measure/` `params.json`, `PARAM_TABLE.md`, figures + scripts · `build/` `model.py`, `MODELING_PLAN.md`, export checks · `qa/` verdict, gate, deviation, overlays · `decisions/`, `DECISIONS.md` owner decisions · `deliver/` report, manifest, limitations, repro · `input/` photos + input hashes.
