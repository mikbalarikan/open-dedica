# REPORT — od_c15_foot v01 (20261001-od-c15-feet)

Designer: Claude Code, designer role · spec 1.1 · plan `01_CAD/DESIGN_PLAN.md` (1770a3c3…ccdf) · brief WP-03 (J3, attempt 1 of 2, fix_cycles 3) · 2026-10-01 UTC

Placement note: the designer's write of this file was blocked by the session's file hook; the orchestrator placed the designer's returned text here verbatim, with the runtime model name removed (repository rule). Nothing else changed.

Every number was measured by `01_CAD/check_od_c15_foot.py` on the re-imported `02_STEP_STL/od_c15_foot_C1_v01.step` and `02_STEP_STL/od_c15_assembly_C1_v01.step`. All 224 rows are in `01_CAD/check_results_v01.json`: 94 PASS, 116 PASS_ASSUMED, 2 N/A, 0 FAIL, 0 INCONCLUSIVE, plus 12 ungated corroboration rows.

## 1. Files

| File | SHA-256 |
|---|---|
| `01_CAD/check_od_c15_foot.py` | 8d4b57c27a44add3f3e493b6439adeeda32a05846dd5dd835dee6f24c9a781a6 |
| `01_CAD/build_od_c15_foot.py` | 7dc8a6e4410325cad17eab3679cac1ec4ffac63bb321d09f240965e9f834e3be |
| `01_CAD/build_check_assembly.py` | 7f7e7780ef9560450f66315f584b5f55e334a4dfbd548c0fd147e1ea9cf83656 |
| `01_CAD/sections_od_c15_foot.py` | b63aac46da163c89fa74eeb0dc1f9cc7d3cfbfd1323205215d741d061b75d07f |
| `01_CAD/sweep_od_c15_foot.py` | 095dccfa708ed379f754d413d48777cc9131946235d1ac23b32e4a6e4c83b1d2 |
| `02_STEP_STL/od_c15_foot_C1_v01.step` | 830f80268050b3b40ff38dffde5f68dc158952d47917ffa28e0f98b7704b46d7 |
| `02_STEP_STL/od_c15_foot_C1_v01.stl` | cc66c8c8961c9becda42111b1d3c0246c81940d4fc9fb98fe94036c4d8e4f20c |
| `02_STEP_STL/od_c15_assembly_C1_v01.step` | e3228ea2f667eeb98ef1add9c37c38c8bbab9adb7d7a85bed61105f58d261d8f |
| `03_Sections/od_c15_foot_v01_front.png` | fbf888202a8f4c282c5c9e2d5f80a8b80776b99947d418038ea57ebd4dc6e184 |
| `03_Sections/od_c15_foot_v01_left.png` | 385a31c5822e531a26ff159b6d8de22cb78cd5a77eea941809e1fb164f0163de |
| `03_Sections/od_c15_foot_v01_top.png` | 4e47ba6451f0f09d7920e855b1268f933b6d912bdc5b79b7b5fd2935d4d22d0e |
| `03_Sections/od_c15_assembly_pose1_v01_left.png` | 6e5e5dcd5fe15409742a47cd5a478779b40d9328ec0eb5eff339473ae1eb9701 |
| `03_Sections/od_c15_assembly_pose1_v01_top.png` | 920a82e982264c5a66700c47e799dbd0f076500d631f28c908748ceb9f1f36b4 |
| `01_CAD/check_results_v01.json` | 026e03b3a4c5e87c57ac3287cff396986ad6b3dd332cfaf15e4c3706f1b3c813 |
| `01_CAD/sweep_v01/summary.json` | f78b84c648560fcc88af8dd9e62985bcc8d28b07834518566907f96d9551ff94 |

- Foot STEP: AP242 through `tools.core.write_step` / `step_roundtrip`, label `od_c15_foot`.
- Foot STL: `write_stl` at tolerance 0.01 mm and angular 0.18 rad, 1194 triangles, sagitta 0.00661 mm.
- Assembly STEP: AP242 with `plate`, `foot_1…4`, `screw_1…4`, `nut_1…4`.
- Sections: five PNGs, all with `nothing_clipped` = 0. The assembly sections cut the plate to a 40 mm window around the pose-1 hole.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · cadquery-ocp-novtk 7.9.3.1.1 (OCCT 7.9.3) · trimesh 5.1.0 · ezdxf 1.4.4 · repo commit 10929db1408d89144bd4af9cad971440427933d0. The spec, plan and OD-C01 input hashes all match the brief.

## 3. Gate self-check

Bands from GATES §0: 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts. Each row is the least-margin row of its gate.

| Gate | Measured | Status |
|---|---|---|
| exactly_one_solid | foot 1 solid; each of 13 assembly parts 1 solid | PASS |
| U-01 | 1 solid, brep_valid 1, naked edges 0 | PASS |
| U-02 / envelope_within_spec | 18.000 × 18.000 × 10.000 (margin 0.100); min x −9.000, y −9.000, z 0.000 | PASS |
| U-03 (a) | 4 poses match the spec §2 joint (8.9e-11 mm³ not shared); contacts foot–plate underside, nut–seat, head–plate top each clearance 0.000; 20 interference pairs 0.000 mm³ | PASS (assumed: A-01, A-02) |
| U-03 (b) | nut slid mouth → seat at 8 poses (top z 10.0 … 2.5) on 4 feet: 0.000 mm³ | PASS (assumed: A-02) |
| U-04 | AP242, 1 solid, volume delta 9.0e-11 mm³, faces delta 0, labels unchanged, valid | PASS |
| U-05 / feature_census | planes 15 (top, counter, seat, 6 flats, 6 mouth chamfers), cylinders 2 (1 convex, 1 concave), cones 2, bores 1, freeform 0; lid bore offset 0.000 | PASS |
| U-06 (Soft) | wide `min_wall` 2.500 at the lid (−3.05, 0, 2.50) | PASS |
| U-07 | angular 0.18 ≤ 0.18858; sagitta 0.00661 ≤ 0.01; STL 1 body, 0 naked edges, deviation 0.00659 | PASS |
| U-08, D-07 | — | N/A by their rows |
| D-01a / D-01b / D-06a | `min_wall` 2.500 at the lid | PASS / PASS (assumed: A-03) / PASS |
| D-02 | 18 × 18 × 10 against 220 × 220 × 250 | PASS (assumed: A-08) |
| D-03a | `overhang_census` 59.886° at the bed chamfer (8.758, 0, 0.083) | PASS |
| D-03b | span 0.0 | PASS |
| D-04a | lid hole Ø3.400 | PASS |
| D-04c | 1.300 per side, foot above the seat to the shank below it, 4 poses | PASS (assumed: A-02) |
| J-05 | ring z 2.5 … 10 `min_wall` 5.911; radial material at the six hex corners 4.243 (z ≤ 9.975) | PASS |
| J-06 | one plain Ø3.4 bore, 0 helical faces | PASS |
| REQ-01 | one plane facing −Z at z 0.000; annulus Ø3.400 … Ø17.420 (band 17.12 … 17.72 composed from REQ-04) | PASS |
| REQ-02 | Ø3.400, z 0.000 … 2.500 through; offset to outer axis 0.000; plate hole axis to pose 0.000 at 4 poses | PASS (assumed: A-01) |
| REQ-03 | across flats 5.600 on 3 pairs (5.60 … 5.65); rotation 0.000°; centre 0.000; seat z 2.500; mouth open, chamfer 0.500 × 0.500; nut envelope to each flat 0.050 | PASS (assumed: A-06) |
| REQ-04 | Ø18.000 (36 angles × 15 levels), height 10.000, bed chamfer 0.500 × 0.290, counter chamfer 1.000 × 1.000 | PASS (assumed: A-05) |
| REQ-05 | 1.000 to the X edge, the Z edge and the R10 arc at 4 poses | PASS (assumed: A-01) |
| REQ-06 | counter faces y −16.000 at 4 poses; plate COM (0.089, −102.371) inside the feet, least margin 109.911 | PASS (assumed: A-01, A-04) |
| REQ-07 | tip z 6.000: 1.100 past the nut face 4.900, 4.000 above the counter | PASS (assumed: A-02) |

Corroboration, not gated (`engaged_area` at depth 0.01): nut on seat 17.118 mm²; head on plate 16.438 mm²; foot on plate INCONCLUSIVE by the tool's own rule (229.414 at 0.01, 229.334 at 0.005, extrapolating to 229.25 = π/4 (17.42² − 3.4²); the 60° chamfer lies within the probe depth); that contact is gated by clearance = 0.

## 4. Sweep (D7)

Each run in `01_CAD/sweep_v01/<run>/`; all 12 runs built one solid, every assembly part one solid.

- body_d 17.9 / 18.1: REQ-04 and U-02 at the tolerance limit (margin 0.000); REQ-05 0.950 at 18.1 (+0.050).
- height 9.9 / 10.1: U-02 size_z and REQ-06 (−15.9 / −16.1) at the limit; REQ-07 tip above the counter 3.9 / 4.1.
- lid_t 2.4 / 2.6: REQ-03 seat and REQ-02 bore end at the limit; D-01b 2.4 (+0.40); REQ-07 tip past the nut 1.2 / 1.0; D-04c 1.300.
- lid_hole_d 3.3 / 3.5: REQ-02 at the limit; D-04a 3.3 (+0.050).
- pocket_af {5.60, 5.65} × nut s {5.32, 5.50}, jointly: U-03 (b) 0.000 mm³ everywhere; J-05 ≥ 4.214; REQ-03 per side 0.140 at 5.60 × 5.32, 0.075 at 5.65 × 5.50, 0.050 at 5.60 × 5.50; **at 5.65 × 5.32 it reads 0.165 against the parenthetical 0.05 … 0.16: FAIL on 4 of 6 flats per pose (16 rows, margin −0.005).**

Every other run: no FAIL, no INCONCLUSIVE.

## 5. Build facts

- 18.000 × 18.000 × 10.000 mm, volume 2284.45 mm³, 2.764 g at 1210 kg/m³ (A-03).
- Fillets: none. Chamfers as built: 0.500 × 0.290 (59.886°), 1.000 × 1.000, mouth 0.500 × 0.500.
- Hex: `RegularPolygon(major_radius=False)` puts a vertex on +X, flat normals at 30°, 90° …; measured rotation 0.000.
- Placement: feet by plate RigidJoints at the measured hole axis ∩ underside (±110, −6, +90 / −295), rotated +90° about X per spec §2, joined to the foot RigidJoint at the measured lid-bore start (0, 0, 0); screws at the hole axis ∩ plate top (y 0); nuts at the measured seat (bore end, z 2.500). Each part is a `copy.deepcopy`, so all four feet keep their own STEP product and label.

## 6. Plausibility (§P)

| # | Answer | Status |
|---|---|---|
| P1 | the foot hangs under the plate, top face on the underside (clearance 0), counter face down at y −16.0; load path plate → lid → counter | YES |
| P2 | screw → plate Ø3.4 → lid Ø3.4 → nut on the seat; flats stop the nut turning; tip ends at z 6.0 inside the pocket | YES |
| P3 | the nut enters mouth → seat with 0 mm³ at 8 poses, 4 feet, all sweep corners | YES |
| P4 | the nut drops in from the counter side through the 0.5 entry chamfer, the screw is driven from the top; the Ø5.7 head stays inside the A-09 Ø8 keep-out | YES |
| P5 | an 18 × 10 mm, 2.8 g foot under a 240 × 405 mm base is in line with OEM pads of this class | YES |
| P6 | nothing floats or is embedded (interference 0); the pocket opens away from the plate; the bed chamfer is on the plate side. The foot-only sections are drawn with Z up (lid at the bottom); the assembly "left" picture has machine +Y to the left | YES |

## 7. Library and tools used

- Card: UNO10 U5, pattern only; no card matches this part.
- tools.core: validity, solid_count, solids, step_roundtrip, compare_step, read_step, write_step, write_stl / mesh_sagitta.
- tools.measure: envelope, feature_census, bore_census, locate_bore, min_wall, overhang_census, flat_ceiling_spans, radial_extent, radial_profile, clearance, interference, engaged_area, mass_properties, mesh_census, mesh_deviation.
- tools.drawing: write_sections.
- New job code in `01_CAD`: the assembly builder with joints; the slide loop; Result arithmetic (across flats, flat rotation, pocket centre, chamfer legs, arc margin, J-05 radial material); the sweep driver.
- No gate needed a missing tool; no 3MF writer (the 3MF is the orchestrator's at J5).

## 8. Deviations from the plan

1. Spec 1.1 bed chamfer built at 0.50 × 0.29 (60°), annulus to Ø17.42; D-03a measurable and passing (the plan expected INCONCLUSIVE).
2. J-05: `min_wall` reads 5.911, not the plan's ≈ 4.19 (the 25° opposed-normal rule does not pair the mouth chamfer with the counter chamfer); the plan's radial corroboration added as a gated row (4.243).
3. REQ-01 Ø17.42 band composed from REQ-04's tolerances (the spec row gives none).
4. REQ-03 per-side clearance gated per flat by radial readings and as the least clearance to the walls above seat + 0.1.
5. Hole-axis fact reported under REQ-02 (≤ 0.10, A-01); the joint-pose volume check under U-03 (a).
6. Fix cycle 1 (of 3): check script only. In the first sweep the height 9.9 run gave four INCONCLUSIVE rows because the mouth and corner probes sat at the spec height 10.0, above the part; the probes now sit on the measured counter face. Nominal check and all 12 sweep runs re-run; geometry not re-exported.
7. Placement log written to `01_CAD`, not beside the STEP.

## 9. Least sure

1. REQ-03 at the tolerance corner af 5.65 × s 5.32: 0.165 against the spec's 0.16. Spec arithmetic: the parenthetical becomes 0.165, or the af tolerance becomes +0.04.
2. A-06: whether TPU 95A grips the nut against turning at 0.05 … 0.165 per side; only a first print answers it.
3. J-05 at the mouth: radial reading sampled to z 9.975 (4.243); the value at z 10 (≈ 4.19) is extrapolated.

## 10. Stop

Not stopped.
