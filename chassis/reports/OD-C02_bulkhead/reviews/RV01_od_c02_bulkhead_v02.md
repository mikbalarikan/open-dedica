# RV01 — od_c02_bulkhead_v02 (20260930-od-c02-bulkhead) — 2026-09-30 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` + `01_CAD/DESIGN_PLAN_v02.md` + `briefs/WP-03_designer.md` amendments · report `01_CAD/REPORT_od_c02_bulkhead_v02.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-02, A-03, A-04, A-05, A-06, A-07, A-08, A-10

Completeness: every §5 row is answered in the REPORT, every file in the brief is present, and every SHA-256 matches, the six reference inputs included. No designer script was read. Bands are the GATES §0 bands: mm 0.005, deg and mm³ 0.001, counts 0. `min_wall`, `min_wall_wide` and `overhang_census` ran at spacing 0.7 (largest step 0.697674). My scripts, mutants, and sections are in `reviews/RV01_work/`.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c02_bulkhead_C1_v02.step` | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | yes |
| `02_STEP_STL/od_c02_assembly_C1_v02.step` | 7d2e760590973fdfe529338231b117a9fc456d246b886a0217c4785f61d37141 | yes |
| `02_STEP_STL/od_c02_bulkhead_C1_v02.stl` | e48afe62c8beb97acc76da990d75ab7e4e2bfbd5416b9cf3f38a0f65d573e18e | yes |
| `02_STEP_STL/od_c02_bulkhead_C1_v02.3mf` | 8a82334c463566c6ac2d57616d59a2c432be3dd9a9246526e926670b183cf082 | yes, against the brief's table (the orchestrator wrote it, so the REPORT does not list it) |
| `01_CAD/REPORT_od_c02_bulkhead_v02.md` | afcf6b68b21166862ac6c388f4403e643c095951d8fa2663f3f50817c039fb82 | brief |
| `01_CAD/DESIGN_PLAN.md`, `01_CAD/DESIGN_PLAN_v02.md` | 119de1e7…4005, cc39c89c…1e25 | yes |
| `01_CAD/check_…_v02.json`, `build_record_v02.json`, `sections_v02.json`, `sweep_v02/sweep_summary_v02.json` | e25653f3…2a96, 29df8e6a…fcbc, a0f85af7…04cc, 835489ee…2b7f | yes / brief |
| `03_Sections/od_c02_bulkhead_v02_*.png` (19) | as in the brief | yes |

The delivery must carry exactly these bytes.

## 2. Gate table

Every value comes from my own calls on the exported STEP. The neighbours were placed by me from `00_Spec/inputs/` with the OD-C01 §4 joints; their volumes and boxes match the assembly STEP's solids.

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 solid, valid 1, naked 0 | 1 / 1 / 0 | 0 | whole part, 114 edges, 0 BOP faults | PASS | `validity` | — |
| U-02 | 12.000 × 215.000 × 210.000 mm | each ±0.1 | 0.1 | x 59…71, y 0…215, z −240…−30 (position exact) | PASS | `envelope` | — |
| U-03 | carrier box 4.000 mm (governing) | contact 0, ≤ 0 mm³, coax ≤ 0.10, ≥ 3.0, box ≥ 4.0 | 0.0 | box (59, 0, −30); plate clearance 0.000 at (67, 0, −225), common 0.000; coax 0.000 ×4; OD-H01 7.500 (63, 40, −202.4); OD-C04 9.000; OD-C03 17.000; OD-G01 18.683; OD-H11 20.161 (63, 99.36, −97.3) | PASS (assumed: A-01, A-02) | `clearance`, `common_volume`, `locate_bore` | A-01, A-02 |
| U-04 | 0.000 mm³ | re-read unchanged, no stray shells, valid | 0 | AP242, 1 solid `od_c02_bulkhead`, valid after, 0 loose shells; volume = analytic plan volume within 3e-10; my re-export: Δ 4.7e-10 mm³, faces Δ 0 | PASS | `compare_step`, `step_roundtrip` | — |
| U-05 | 6 bores, 46 faces | plan census | 0 | see §3 | PASS | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 (Soft) | 2.000 mm | ≥ 2.0 | 0.0 | (63, 207, −60) to (63, 209, −60) | PASS | `min_wall_wide` | — |
| U-07 | 0.004896 mm | tol 0.01, ≤ 0.2310 rad, sagitta ≤ 0.01; 3MF same mesh | 0.005104 | STL 2308 triangles, 1 closed shell, winding consistent; my re-mesh at 0.01 / 0.20 gives the same 2308 triangles and vertices; 3MF: mm, no transform, 2308/2308 triangles identical | PASS | `mesh_deviation`, `mesh_census`, `write_stl` | — |
| U-08 | — | threaded parts only | — | — | N/A: no threads, by its row | — | — |
| D-01a | 2.000 mm | ≥ 0.8 | 1.2 | (63, 207, −60) | PASS | `min_wall` | — |
| D-01b | 2.000 mm | ≥ 2.0 | 0.0 | (63, 207, −60) to (63, 209, −60), top-bore floor to flange underside; same at z −210 | PASS | `min_wall` | — |
| D-02 | 215.0 mm | ≤ 220 × 220 × 250 | 5.0 | bed 12 × 215, 210 tall | PASS (assumed: A-08) | `envelope` | A-08 |
| D-03a | 45.000 deg | ≥ 45 outside the crowns | 0.0 | (67, 150, −186) window 1 gable; 8 roof normals (0, ±0.707107, −0.707107); refilled census: bound 0, 0 samples below 45; whole part 0.0 at the crowns (65, 0, −223), the named exception | PASS (assumed: A-10) | `overhang_census(build_dir=(0,0,1))` on my refilled solid; B-rep normals | A-10 |
| D-03b | 4.000 mm | span ≤ 5 | 1.0 | the six Ø4.0 bores; windows gabled; nothing else under 45° | PASS | `bore_census`, refilled census, sections | — |
| D-04a | — | none on this part | — | — | N/A: by its row | — | — |
| D-05a | 11.000 mm | ≥ 8.0 across | 3.0 | top bores x 59.5…70.5; base bores 12.0 | PASS (assumed: A-05) | `radial_extent`, `radial_profile` | A-05 |
| D-05b | Ø4.000 mm, depth 6.000 | Ø4.0 ± 0.05, 6.0 ± 0.1 | 0.05 | all six, blind | PASS (assumed: A-05) | `bore_census`, `locate_bore` | A-05 |
| D-06a | 2.000 mm | ≥ 1.0 | 1.0 | (63, 207, −60) | PASS | `min_wall` | — |
| D-07 | — | none | — | — | N/A: by its row | — | — |
| J-05 | 3.500 mm | ≥ 3.0 | 0.5 | (70.5, 209.25, −60): least outer radius 5.5 over 36 angles × 12 levels, less r 2.0; base bores 4.0 | PASS | `radial_profile`, `locate_bore` | — |
| E-06 | 210.0 mm | rails over the whole length, no free boss | 0.0 | sections x 61 and x 69: 2 cuts each, 4200 mm² = (12 + 8) × 210; all bores inside a rail | PASS | `write_sections`, `bore_census` | — |
| REQ-01 | Ø4.000 mm | Ø4.0 ± 0.05, 6.0 ± 0.1, offset ≤ 0.10 to plate | 0.05 | (65, 0, −45/−105/−165/−225): depth 6.000, blind, offset 0.000 to nominal and to the plate's Ø4.000 through holes | PASS (assumed: A-01, A-03) | `bore_census`, `locate_bore` on both solids | A-01, A-03 |
| REQ-02 | 63.000 / 67.000 mm | ±0.10; rail 59.00 ± 0.10 | 0.1 | 858 rays along X, y 12.5…205: every one reads 63.000 and 67.000; min_x 59.000 | PASS (assumed: A-01) | rays (`radial_extent`), `envelope` | A-01 |
| REQ-03 | y 0.000 mm | 0.00 ± 0.10, one face; top 12.0 ± 0.1 | 0.1 | one planar face with 5 wires, 2469.73 mm² = 2520 less four Ø4 mouths; rail tops 12.000 | PASS (assumed: A-01) | B-rep faces, rays | A-01 |
| REQ-04 | Ø14.000 mm | Ø14.0 ± 0.1, offset ≤ 0.10, 45° gable, apex +7 | 0.1 | 54-ray circle fit per window: Ø14.000, offset < 1e-10; apex 14.000 above centre; w4 apex z −41, front end one face of 1012 mm²; convex cylinders 0 | PASS (assumed: A-04) | `radial_extent`, B-rep faces | A-04 |
| REQ-05 | 59.000 mm | ≥ 59.0; wet clearances ≥ 3.0 | 0.0 | min_x; nearest wet part OD-H01 7.500 | PASS (assumed: A-02) | `envelope`, `clearance` | A-02 |
| REQ-06 | 215.000 mm | 215.0 ± 0.1; wall reaches top rail | 0.1 | Y rays at x 64 and x 66 continuous to 215 outside the windows | PASS (assumed: A-06) | `envelope`, rays | A-06 |
| REQ-07 | Ø4.000 mm | Ø4.0 ± 0.05, 6.0 ± 0.1, offset ≤ 0.10 | 0.05 | (65, 215, −60), (65, 215, −210): depth 6.000, blind, offset 0.000 | PASS (assumed: A-05) | `bore_census`, `locate_bore` | A-05 |
| REQ-08 | 71.000 mm | ≤ 71.0; wall face ≤ 70 | 0.0 | base rail x 71; electric face 67.000 | PASS (assumed: A-07) | `envelope`, rays | A-07 |
| REQ-09 (Soft) | — | bench | — | — | INCONCLUSIVE: bench row, risk MEDIUM (F1) | — | A-11 |

**My ruling on OD-H11 (U-03, U-04).** Interference: OD-H11's box ends at x 42.839 and the bulkhead's starts at x 59.0. The boxes are disjoint, so `common_volume` returns 0.000 mm³ without running a boolean on the unsound solid. That is a measured zero, not an INCONCLUSIVE. Clearance by distance: 20.161. U-04 gates the named body, the bulkhead, and it passes. In the assembly STEP, the OD-H11 body differs by 0.052 mm³ from the input placed by its joint. That comes from re-writing an unsound input and is recorded as F5. It is not a U-04 miss of the target.

**Tool note (not a build finding).** In `tools/measure/wall.py`, `min_wall` reuses the name `found` inside its ray loop. As a result, `detail["solids"]` reports 4 on this one-solid part. The measured value is not affected.

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 wall | faces x 63, x 67, 4.0 thick | 63.000 / 67.000, 40054.12 mm² each, 5 wires | PASS |
| F02 base rail x 59…71, y 0…12 | underside, sides, tops, full length | underside 1 face y 0; sides 2520 mm²; tops y 12, 840 mm² each | PASS |
| F03 top rail x 59.5…70.5, y 207…215 | top, sides, undersides, full length | top 2284.87 mm²; sides 1680; undersides 735 each | PASS |
| F04 windows ×4, gabled | 4 concave R7.0 half-cylinders, 8 sides, 8 roofs at 45° | 4 × R7.000 at (150, −200), (150, −130), (150, −60), (60, −55); 8 sides; 8 roofs at 45.000° | PASS |
| F05 Ø4.0 × 6.0 bores from below ×4 | open at y 0 | 4 × Ø4.000 × 6.000, blind, x 65, z −45/−105/−165/−225 | PASS |
| F06 Ø4.0 × 6.0 bores from above ×2 | open at y 215 | 2 × Ø4.000 × 6.000, blind, x 65, z −60/−210 | PASS |
| totals | planar 36, cyl 10, concave 10, convex 0, bores 6, faces 46 | same | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity | The rail sits on the plate (clearance 0, common volume 0) and is held by four M3 × 12 screws from below into coaxial inserts. In the print it stands on a 1012 mm² I-profile end, with the centre of mass over the footprint. It is a slender fin (210/12), which is the A-10 risk (F7). | YES |
| P2 | Function chains | The dam is one continuous underside over z −240…−30, broken only by the blind bore mouths. The windows are open through both faces. The top bores open at y 215. The dam ends are open (A-12, F6). | YES |
| P3 | Moving parts, assembly path | No moving parts. The footprint lowered along −Y (swept from y 0 to y 500) clears OD-H01 by 3.500, the carrier by 4.000, OD-C04 by 9.0, OD-H11 by 16.16, OD-C03 by 17.0 and OD-G01 by 18.25. | YES |
| P4 | Grip, reach, insertion | Each screw goes in from below on the bore axis. The head seats flat (gap 0, common 0). A Ø6 driver column is 3.0 from the plate and ≥ 11.4 from every neighbour. The machine goes on its side (A-03). The screw tip lands on the bore floor (F2). | YES |
| P5 | Next to a real product | A printed 4 mm partition with rails and grommet windows is ordinary. Only its stiffness (F1) and the screw length (F2) invite comment. | YES |
| P6 | Floating, embedded, mirrored, upside-down | One solid, interference 0 with every neighbour, gables pointing +Z, and the neighbours match my own joint placements. | YES |

## 5. Positive controls

Every mutant was made from the exported part (or its STL/3MF) in `reviews/RV01_work/m9_controls.py` and `m11_3mf_control.py`.

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` solid_count | part + a loose 5 mm cube (2 solids) | FAIL |
| `validity` naked_edges | front end face left out (12 naked edges) | FAIL |
| `envelope` | base rail wet face at x 58.5 (min_x 58.5, size 12.5) | FAIL |
| `feature_census` / `bore_census` | base bore z −225 filled (5 bores) | FAIL |
| `locate_bore` offset | base bore z −165 moved to x 65.5 (0.5) | FAIL |
| `locate_bore` diameter / depth | bore opened to Ø4.2 / deepened to 6.5 | FAIL / FAIL |
| `min_wall` | 20 × 20 wet-face pocket leaving 0.6 | FAIL |
| `min_wall_wide` | same (0.6 < 2.0) | FAIL |
| `overhang_census` | window 1 cut square with a flat roof, bores refilled (0.0°) | FAIL |
| `radial_extent` window | window 1 opened to Ø15.0 | FAIL |
| `radial_extent` J-05 / D-05a | top rail narrowed to x 62…68 (wall 1.0) | FAIL |
| `clearance` | moved 5 mm to −X (2.5 to OD-H01) | FAIL |
| `clearance` contact | lifted 0.5 off the plate | FAIL |
| `common_volume` | moved 10 mm to −X (53.96 mm³ in OD-H01) | FAIL |
| `locate_bore` coaxiality | moved 0.5 along +Z (offset 0.5) | FAIL |
| `mesh_deviation` | re-meshed at 0.2 mm / 0.8 rad (0.086) | FAIL |
| `mesh_census` | one triangle dropped (3 naked edges) | FAIL |
| 3MF triangle-set comparison | one 3MF vertex moved 0.05 (2289/2308 match) | FAIL |
| `compare_step` | part against a re-export with the pocket (1360 mm³) | FAIL |
| face rays (REQ-02/03/06) | 0.5 boss on the wet face (reads 62.5) | FAIL |

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-09 | SOFT_GATE_MISS | INCONCLUSIVE → no visible flex (bench) | — | wall between the rails | no | MEDIUM | Hand estimate (E 2 GPa): about 0.07 mm/N at mid-span with the top panel on, about 1.5 mm/N at the top as a cantilever before the panel is fitted | Answer on the first print. If it flexes, add ribs along Y on the electric face or go to a 5 mm wall |
| F2 | A-03 (no row) | OBSERVATION | screw tip 0.000 above the bore floor → clear | 0.0 | (65, 6, −45/−105/−165/−225) | no | MEDIUM | An M3 × 12 with its head on the plate (y −6) ends at y 6.000, the bore floor. A long screw or melt below the insert bottoms out before the joint clamps | Usta, under A-03: M3 × 10 (4 mm into the 5.7 insert), or bores about 7.0 deep (REQ-01) |
| F3 | D-01b | OBSERVATION | 2.000 → ≥ 2.0 | 0.0 | (63, 207…209, −60 / −210) | no | LOW | Passes at a point where the bore's floor rim meets the wall-face line, with the full wall below. REQ-07's +0.1 depth band would read 1.9 | Spec: top-bore depth 6.0 −0.1/+0, or top-rail underside at y 206 |
| F4 | REQ-05 / REQ-08 / U-03 | OBSERVATION | 59.000 / 71.000 / 4.000 → on the limits | 0.0 | rail faces x 59 and x 71 | no | LOW | Exact in CAD. A printed rail may exceed these limits by tenths; nothing moves there and the pump is 3.5 away | None for this build. For print margin, rail x 59.2…70.8 |
| F5 | U-04 (assembly) | OBSERVATION | OD-H11 Δ 0.052 mm³ → unchanged | — | assembly STEP, `od_h11_thermoblock` | no | LOW | Re-writing an unsound input changes it by 3e-7 relative. The target and the other six solids are exact | None; retires with OD-C04 A-14 |
| F6 | A-12 | OBSERVATION | dam z −240…−30 (210) → continuous | 0.0 | dam ends; plate z −305…100 | no | UNKNOWN | Water can run round either end on a flat plate. Drains and tilt are not in any file | First wet test; dam returns or a plate lip if needed |
| F7 | A-10 | OBSERVATION | footprint 1012 mm², 12 deep, 210 tall | — | bed face z −240 | no | MEDIUM | A tall ASA fin: warp and knock-over risk in the top layers | Brim or mouse ears, enclosed printer, slow top layers; confirm on the first print |

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. D-01b / U-06 at margin 0 on the top-rail bores | Confirmed at 2.000 from (63, 207, −60) to (63, 209, −60), same at z −210. PASS in the band at margin 0. The spec's REQ-07 depth band conflicts with D-01b (F3, LOW). |
| 2. D-03a gated on a refilled solid | My own refill (valid, 34 faces, 0 bores) reads 45.0° at (67, 150, −186), with bound 0 and no sample below 45°. The roofs are analytically 45.000°. The crowns (0°) are the named exception in ratified §5. |
| 3. Envelope rows on their limits; ledger lag | Confirmed 59.000 / 71.000 / 4.000, all PASS at margin 0 (F4, LOW). Spec 1.2's A-04 and A-05 now match the build (window 4 at z −55, top bores at x 65). |
