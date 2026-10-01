# RV01 — od_c15_foot_v01 (20261001-od-c15-feet) — 2026-10-01 UTC

Reviewer: Claude Code, reviewer role · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with `briefs/WP-03_designer.md`) · report `01_CAD/REPORT_od_c15_foot_v01.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-02, A-03, A-04, A-05, A-06, A-08

Method: every row was re-measured with my own scripts (`reviews/RV01_work/m01` … `m06`) on the exported STEP and STL and on my own placement of the foot against the OD-C01 input. The placement uses the spec §2 joint (foot x → X, y → +Z, z → −Y, Rx(+90°); the point (1, 2, 3) maps to (111, −9, 92) at pose 1), not the assembly file. I then compared the designer's assembly file with my placement: all 12 placed parts coincide (symmetric difference 0.000 mm³), and its plate matches the input. Band per GATES §0: 0.005 mm, 0.001°, 0.001 mm³, 0 for counts. No CAD code was read.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c15_foot_C1_v01.step` | 830f80268050b3b40ff38dffde5f68dc158952d47917ffa28e0f98b7704b46d7 | yes |
| `02_STEP_STL/od_c15_foot_C1_v01.stl` | cc66c8c8961c9becda42111b1d3c0246c81940d4fc9fb98fe94036c4d8e4f20c | yes |
| `02_STEP_STL/od_c15_assembly_C1_v01.step` | e3228ea2f667eeb98ef1add9c37c38c8bbab9adb7d7a85bed61105f58d261d8f | yes |
| `01_CAD/REPORT_od_c15_foot_v01.md` | df020639538f2faa6f406485432f0d52f25ebf3cf57fbc8ae6f9dfbbb089a242 | yes (brief) |
| `00_Spec/DESIGN_SPEC.md` (1.2) | a24c23f25b2f02b916d89beb76e3db5c899d02d518c3775c402b5ed27e0e496f | yes (brief) |
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | yes |
| `03_Sections/od_c15_foot_v01_front.png` | fbf888202a8f4c282c5c9e2d5f80a8b80776b99947d418038ea57ebd4dc6e184 | yes |
| `03_Sections/od_c15_foot_v01_left.png` | 385a31c5822e531a26ff159b6d8de22cb78cd5a77eea941809e1fb164f0163de | yes |
| `03_Sections/od_c15_foot_v01_top.png` | 4e47ba6451f0f09d7920e855b1268f933b6d912bdc5b79b7b5fd2935d4d22d0e | yes |
| `03_Sections/od_c15_assembly_pose1_v01_left.png` | 6e5e5dcd5fe15409742a47cd5a478779b40d9328ec0eb5eff339473ae1eb9701 | yes |
| `03_Sections/od_c15_assembly_pose1_v01_top.png` | 920a82e982264c5a66700c47e799dbd0f076500d631f28c908748ceb9f1f36b4 | yes |

Completeness: every §5 row is answered in REPORT §3, and every listed file is present with a matching hash. The REPORT was written against spec 1.1; the brief asks for the rating against 1.2, which differs only in REQ-03's per-side parenthetical.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 solid, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | foot file; OD-C01 input and each of the 13 assembly parts 1 solid | PASS | `validity` | — |
| U-02 | 18.000 × 18.000 × 10.000 mm | each in [spec − 0.1, spec + 0.1] | +0.100 | min (−9.000, −9.000, 0.000), max (9.000, 9.000, 10.000) | PASS | `envelope` | — |
| U-03 | 0.000 mm³ (all pairs), contacts 0.000 mm | (a) contacts = 0, pairs ≤ 0; (b) slide ≤ 0 | 0.000 | (a) four own poses: foot on underside (111.7, −6.0, 90.0), nut on seat (111.588, −8.5, 92.75), head on top (112.85, 0.0, 90.0), and likewise at the other poses; 24 pairs 0.000. (b) 33 poses, nut top z 10.5 → 2.5, × nut s {5.32, 5.50} × pocket af {5.60, 5.65}: max 0.000 | PASS (assumed: A-01, A-02) | `clearance`, `interference`, own slide script | A-01, A-02 |
| U-04 | volume_delta 0.000 mm³ | re-read unchanged, no stray shells, valid | 0 | AP242, label `od_c15_foot`, 1 solid, 1 shell; round trip of a detached copy and `compare_step` against the delivered file: faces_delta 0, labels 1, valid_after 1 | PASS | `step_roundtrip`, `compare_step` | — |
| U-05 | 19 faces | plan counts (see §3) | 0 | planes 15, cylinders 2 (convex 1, concave 1), cones 2, other kinds 0, bores 1 | PASS | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 (Soft) | 2.500 mm | wide `min_wall` ≥ 2.0 | +0.500 | (−3.054, 0.0, 2.5), the lid | PASS | `min_wall` `detail["wide"]` | — |
| U-07 | 0.00659 mm | tol 0.01, angular ≤ 0.18858 rad, sagitta ≤ 0.01 | +0.00341 | delivered STL to B-rep, worst at (−5.023, 6.846, 9.5); own re-mesh at 0.01 mm / 0.18 rad gives the same 1194 triangles and the same vertex set (largest vertex distance 0.000), sagitta 0.00661; 1 body, 0 naked edges, winding 1, volume 2282.616 mm³ (B-rep 2284.451); `min_wall_mesh` 2.500 | PASS | `write_stl`, `stl_max_sagitta`, `mesh_census`, `mesh_deviation` | — |
| U-08 | — | applies to threaded parts | — | no helical or freeform faces; one plain Ø3.4 bore | N/A: by its row (the target has no threads) | — | — |
| D-01a | 2.500 mm | ≥ 0.8 | +1.700 | (−3.054, 0.0, 2.5), the lid | PASS | `min_wall` | — |
| D-01b | 2.500 mm | ≥ 2.0 | +0.500 | same | PASS (assumed: A-03) | `min_wall` | A-03 |
| D-02 | 18.000 mm (largest of 18 × 18 × 10) | ≤ 220 × 220 × 250, top face down | +202.0 | print frame, z 0 on the bed | PASS (assumed: A-08) | `envelope` | A-08 |
| D-03a | 59.886° | ≥ 45° | +14.886 | (8.758, 0.0, 0.083), the bed-edge chamfer, which is the only downward face; sampling bound 0.0052°, 0 samples below 45° | PASS | `overhang_census` | — |
| D-03b | 0.000 mm | span ≤ 5 | +5.000 | no flat ceiling off the bed: seat, counter face and mouth chamfer face up (own sections) | PASS | `flat_ceiling_spans`, own sections | — |
| D-04a | Ø3.400 mm | ≥ 3.25 | +0.150 | lid bore (0, 0, 0) → (0, 0, 2.5) | PASS | `bore_census`, `locate_bore` | — |
| D-04c | 1.300 mm | ≥ 0.5 per side | +0.800 | flat edge at (2.425, 1.4, 2.5) to the Ø3.0 shank segment z 2.5 … 6.0 | PASS (assumed: A-02) | `clearance` | A-02 |
| D-06a | 2.500 mm | ≥ 1.0 | +1.500 | (−3.054, 0.0, 2.5), the lid | PASS | `min_wall` | — |
| D-07 | — | applies to reamed fit bores | — | the only bore is the Ø3.4 clearance hole | N/A: by its row (the part has no fit bores) | — | — |
| J-05 | 4.189 mm | ≥ 3.0 on the ring z 2.5 … 10 | +1.189 | mouth-chamfer corner (3.811, 0, 10.0) to the counter-chamfer edge (8.0, 0, 10.0); `min_wall` on the ring reads 5.911 at (−8.965, 0.790, 2.681); radial material at the corners 5.767 below z 9.0, 4.192 at z 9.999 | PASS | `min_wall` on the foot cut at z 2.5; face-to-face distance; `radial_extent` | — |
| J-06 | 1 plain bore | no threaded bore | 0 | Ø3.4, 0 helical or freeform faces | PASS | `bore_census`, `feature_census` | — |
| REQ-01 | Ø17.420 mm | one plane at z 0.0 ± 0.1, annulus to Ø17.42, normal −Z | 0.000 | one plane at z 0.000, area 229.255 mm² = π/4 (17.42² − 3.4²); outer edge r 8.710 at 12 angles | PASS | `envelope`, `feature_census`, `radial_extent` | — |
| REQ-02 | Ø3.400 mm | Ø3.4 ± 0.1 through z 0 … 2.5, offset ≤ 0.10 | +0.100 | through, z 0.000 → 2.500; offset to the outer axis 0.000; offset to each plate hole axis at the four own poses 0.000 | PASS (assumed: A-01) | `locate_bore`, `radial_profile` | A-01 |
| REQ-03 | af 5.600 mm | 5.60 +0.05 / −0 (0.05 … 0.165 per side); flats ∥ X ± 1°; centre ≤ 0.10; seat 2.50 ± 0.1; open; chamfer 0.5 | 0.000 | af 5.600 on all three pairs at z 2.6, 4, 6, 8, 9.4; rotation 0.000°; centre 0.000; seat z 2.500; open at z 10 (r 3.299 at z 9.999); mouth chamfer 0.5 × 0.5. Per side: 0.050 (nut s 5.50), 0.140 (s 5.32); af 5.65 variant 0.075 / 0.165 | PASS (assumed: A-06) | `radial_extent`, `clearance`, `feature_census`, sections | A-06 |
| REQ-04 | Ø18.000 mm | Ø18.0 ± 0.1, h 10.0 ± 0.1, chamfers 0.50 × 0.29 and 1.0 × 1.0 ± 0.1 | +0.100 | 36 angles over z 0.6 … 8.9; height 10.000; bed chamfer z 0 → 0.5, r 8.710 → 9.0 (59.886°); counter chamfer z 9.0 → 10.0, r 9.0 → 8.0 | PASS (assumed: A-05) | `radial_profile`, `radial_extent`, `envelope` | A-05 |
| REQ-05 | 1.000 mm | ≥ 0.9 | +0.100 | all four poses: 1.000 to the X edge, 1.000 to the Z edge, and 1.000 to the R10 arc (plate R 10.000 over the outward sector, foot R 9.000, axis offset 0.000) | PASS (assumed: A-01) | `envelope`, `radial_profile`, `locate_bore` | A-01 |
| REQ-06 | y −16.000 mm | −16.00 ± 0.10; feet enclose the plate's centre of mass | +0.100 | all four counter faces at y −16.000; plate centre of mass (0.089, −3.000, −102.371) inside the rectangle of the axes, least margin 109.911 | PASS (assumed: A-01, A-04) | `envelope`, `mass_properties` | A-01, A-04 |
| REQ-07 | tip z 6.000 mm | 6.0 ± 0.1; ≥ 0.5 past z 4.9; ≥ 2.0 above the counter face | +0.100 | screw envelope max z 6.000 in the foot frame (plate measured 6.000 thick): 1.100 past the nut face, 4.000 above the counter face | PASS (assumed: A-02) | `envelope` | A-02 |

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 body Ø18.0 × 10.0 | 1 convex cylinder r 9.0 | 1 convex cylinder r 9.000, z 0.5 … 9.0 between the chamfers | PASS |
| F02 bed-edge chamfer (spec 1.1: 0.50 × 0.29, 60°) | 1 cone, z 0 … 0.5 | 1 cone, z 0.000 → 0.500, r 8.710 → 9.000, 59.886° | PASS |
| F03 counter-edge chamfer 1.0 × 45° | 1 cone, z 9 … 10 | 1 cone, z 9.000 → 10.000, r 9.000 → 8.000, 45° | PASS |
| F04 lid hole Ø3.4, z 0 … 2.5 | 1 concave cylinder, 1 through bore on Z | 1 bore Ø3.400, (0, 0, 0) → (0, 0, 2.5), through, offset 0.000 | PASS |
| F05 hex pocket af 5.60, flats ∥ X | 6 planar flats at 2.80 | 6 vertical planes at 2.800, normals at 30°, 90° and 150° (one pair parallel to X), z 2.5 … 9.5 | PASS |
| F06 nut seat z 2.5 | 1 plane | 1 plane at z 2.500, 18.079 mm² | PASS |
| F07 mouth chamfer 0.5 × 45° | 6 planes, z 9.5 … 10 | 6 planes at 45°, z 9.500 → 10.000 | PASS |
| End faces | top annulus and counter annulus | z 0.000, 229.255 mm²; z 10.000, 163.338 mm² (Ø16 less the af 6.6 mouth) | PASS |
| F08 name and export | `od_c15_foot`, AP242, STL | label `od_c15_foot`, AP242, mm; STL with 1194 triangles | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity: does every part rest and mount the way the product is used? | In my own pose-1 section the foot hangs under the plate, with its top face on the underside at y −6.0 and its counter face down at y −16.0 | YES |
| P2 | Function chains connected and aimed? | Head on the plate top → plate Ø3.4 → lid Ø3.4 → nut on the seat, all coaxial (offset 0.000); the tip ends inside the pocket | YES |
| P3 | Moving parts oriented for their motion, with clearance? | The nut slides from the mouth to the seat with 0.000 mm³ at 33 poses for every nut and pocket tolerance corner, and the flats stop it turning | YES |
| P4 | Human factors: grip, reach, insertion direction obvious? | The nut drops in from the open counter side through the 0.5 chamfer, and the screw is driven from the plate top; the Ø5.7 head stays inside the A-09 Ø8 keep-out | YES |
| P5 | Next to a comparable real product, does anything look absurd? | A Ø18 × 10 mm, 2.76 g screw-on TPU foot under a 240 × 405 mm base is ordinary for a small appliance | YES |
| P6 | Nothing floating, embedded, mirrored, or upside-down? | Contacts are 0 and interference is 0 at every pose; the pocket opens away from the plate, the small chamfer is on the plate side, and the flats are parallel to X | YES |

## 5. Positive controls

All mutants were made from the exported foot STEP or STL (or, for the centre of mass, the OD-C01 input) by my own scripts (`RV01_work/m05_controls.py`).

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` (U-01) | one face removed: open shell, 7 naked edges | FAIL |
| `envelope` (U-02, D-02, REQ-04 h, REQ-06, REQ-07) | foot scaled ×1.02: 18.36 × 18.36 × 10.2 | FAIL |
| `radial_profile` (REQ-04 Ø) | foot scaled ×1.02: outer R 9.18 | FAIL |
| `radial_profile` on the plate arc (REQ-05) | foot scaled ×1.02 at pose 1: arc margin 0.82 | FAIL |
| `radial_extent` across flats (REQ-03) | foot scaled ×1.02: af 5.712 | FAIL |
| `radial_extent` flat rotation (REQ-03) | foot rotated 2° about its axis: reads 2.0° | FAIL |
| `feature_census` (U-05, REQ-01) | lid hole filled: 0 bores | FAIL |
| `bore_census` (J-06, U-05) | lid hole filled: 0 bores | FAIL |
| `locate_bore` offset (REQ-02) | lid hole moved 0.5 mm in x: offset 0.5 | FAIL |
| `locate_bore` diameter (D-04a, REQ-02) | lid hole resized to Ø3.2 | FAIL |
| `min_wall` (D-01a, D-01b, D-06a) | annular groove 1.8 deep in the top face: lid 0.7 | FAIL |
| `min_wall` wide (U-06) | same mutant: 0.7 | FAIL |
| `min_wall` on the ring (J-05) | pocket opened to af 12.6: ring wall 2.010 | FAIL |
| `overhang_census` (D-03a) | tunnel 6 wide × 1 high across the bed face: 0° | FAIL |
| `flat_ceiling_spans` (D-03b) | same tunnel: span 12.08 | FAIL |
| `clearance` contact (U-03 a) | foot 1 moved 0.5 mm off the underside: 0.5 | FAIL |
| `clearance` (D-04c) | rib 0.9 deep on a pocket flat: 0.40 | FAIL |
| `interference` (U-03 a) | foot 1 moved 0.5 mm into the plate: 118.6 mm³ | FAIL |
| `interference` slide (U-03 b) | nut envelope s 5.7 at z 6.0 in the delivered pocket: 2.35 mm³ | FAIL |
| `mass_properties` (REQ-06 centre of mass) | plate moved +300 in Z: centre of mass outside by 107.6 | FAIL |
| `compare_step` (U-04) | delivered file against the hole-filled mutant: volume_delta 22.70 mm³ | FAIL |
| `stl_max_sagitta` (U-07) | re-meshed at 0.1 mm / 0.5 rad: 0.0493 | FAIL |
| `mesh_census` (U-07) | delivered STL with one triangle removed: 3 naked edges | FAIL |
| `mesh_deviation` (U-07) | delivered STL shifted 0.05 mm in x: 0.0546 | FAIL |

## 6. Findings

None. No §5 row misses its limit under spec 1.2. The REPORT §4 sweep FAIL (af 5.65 × s 5.32 reads 0.165 per side against spec 1.1's 0.16) is not a deviation under spec 1.2. My own af 5.65 variant, cut from the exported part, reads 0.165, which equals the corrected upper limit (5.65 − 5.32) / 2 (margin 0.000). The ungated `engaged_area` reading for the foot on the plate is INCONCLUSIVE, by the tool's own rule (229.334 at 0.005, 229.295 at 0.0025 mm, with the 60° bed chamfer inside the probe depth). That contact is gated by clearance 0.000 and interference 0.000, so this is not a finding.

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. REQ-03 at af 5.65 × s 5.32: 0.165 against 0.16 | My own af 5.65 variant with an s 5.32 nut envelope reads 0.165 per side, equal to the upper limit of spec 1.2: PASS at margin 0.000. Spec 1.2 closes it with no geometry change. |
| 2. A-06: TPU 95A grip on the nut | The geometry is confirmed: 0.050 to 0.165 per side, centred 0.000, rotation 0.000°. Whether the TPU grips the nut cannot be measured in CAD; REQ-03 stays PASS (assumed: A-06) until the first printed foot. |
| 3. J-05 at the mouth (z 10 extrapolated) | Measured directly at z 10: 4.189 (mouth corner to the counter-chamfer edge); radial 4.192 at z 9.999. That is +1.189 over 3.0, so no extrapolation is needed. |
