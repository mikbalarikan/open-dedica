# REPORT — od_t01_rig v01 (20261002-od-t01-pressure-test-rig)

Designer: designer subagent (Claude Code) · spec version 1.1 (SHA-256 c3508387…7285) · plan `01_CAD/DESIGN_PLAN.md` (SHA-256 544bde71…0a5d) · 2026-10-03 UTC · J3 package WP-03, build attempt 1 of 2, concept C1

<!-- Placed verbatim by the orchestrator from the designer's returned text: a session hook blocked the designer's own write of this file. Only the model name in the line above was removed. -->

This run resumes WP-03 after a container restart. The exported files, the gate check, the sections and the sweep below all come from one final build. That build reproduced the earlier partial export byte for byte, because the STEP timestamp is fixed. The partial sweep was discarded, and all 20 sweep runs were rebuilt and re-checked.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_t01_rig.py` | 3a99ee1a027cc2f0060da44275ca5ff70ca8509734d9f28a21ffe40f5222f739 | parametric script, Algebra mode, one `Params` structure |
| `01_CAD/check_od_t01_rig.py` | 0361be0454271d79a1cba023d121d08aadebc7e1bc24ada71dd91ebb25e3b34f | checks, written before the build (D3) |
| `01_CAD/sweep_od_t01_rig.py` | 6412372d4cf91b96de60e815385e679daf380306104646b58ed1bcd1477a19a4 | D7 sweep driver |
| `01_CAD/sections_od_t01_rig.py` | b70b8e724876149060a55638594eea6f75cae03dd6ef4404be9207bef10d78f7 | D6 sections |
| `02_STEP_STL/od_t01_rig_C1_v01.step` | cc6b1c721fd34f74232c4cee504c95c0852573fa351411ca12a02c27904c9f5c | AP242 (`tools.core.write_step`), body `od_t01_rig`, re-imported for every measurement |
| `02_STEP_STL/od_t01_rig_C1_v01.stl` | 1b2985d19a6fe86930bdf4ec448b78576ec830f6ee1f5c513a1ae2e63077d3a5 | meshed from the re-imported STEP after clearing the cached triangulation; tolerance 0.01 mm, angular 0.10 rad, 5752 triangles, max sagitta 0.0050 mm |
| `02_STEP_STL/od_t01_assembly_C1_v01.step` | 407386d44f5483aa2d2e6eab7eb72a47749aafbdb06252de5dbecfc3acf7774b | check assembly: rig + OD-G01 housing + OD-G04 + OD-G10 (locked), at the spec §2 pose |
| `03_Sections/od_t01_rig_v01_z0_assembly.png` | 777d644c8467745a38f7357d8e9e8e546c1150b9865b933c3ccd928309b9910d | z 0 through the axis, with the housing set; nothing_clipped 0 |
| `03_Sections/od_t01_rig_v01_z44_assembly.png` | 388c579e5ee53f010d6f9b46fce46ca521ba0ccb037b52c876bf8360189aaf09 | z +44 through two counterbores, with the housing set; nothing_clipped 0 |
| `03_Sections/od_t01_rig_v01_x44.png` | 40a86f731c369c5b458a87ddb685e7b3bb28daa47f6cf22e9b3d85d518f61c9b | x +44 through two screw holes; nothing_clipped 0 |
| `03_Sections/od_t01_rig_v01_y5.png` | 29ad37abb3054b15a07cef2be1dc8ec25c5e51de687dcdc4bd1046c9fb19b9a3 | y 5 through the base and the bench holes; nothing_clipped 0 |
| `03_Sections/od_t01_rig_v01_y142.png` | 7a88b8025e5b7ade3fbf65842432f2ab761a6a4ea7a1420c8b16750f0a838116 | y 142.5 through the plate: window and counterbore teardrops; nothing_clipped 0 |
| `01_CAD/gates_od_t01_rig_v01.json` | e64d579756537b9106480164cddd28fe655ad9f72da018ed7fa800bf71c39087 | all 167 check rows on the delivered STEP |
| `01_CAD/check_v01.log` | 5ba2ae68463435bb5cbc041f462ad480b6bea019d00a1bca3d5f69ca6e8531f9 | console output of that check |
| `01_CAD/od_t01_rig_C1_v01.params.json` | 0531e75f9e1a1282741da7292fe3d576dc54664294cec8ea88d90dbc858a3424 | the build's parameters (used by U-04) |
| `01_CAD/od_t01_rig_C1_v01.mesh.json` | 4b94f72f17d5ebd48597f6aed97d9005c657df36f8f9075d17b3fdff564d510d | STL record (U-07) |
| `01_CAD/sections_v01.json` | 4ee29ccd81c643c5a69196f05b39a5edb37e71cd2358979ca0e22948d4b0ec60 | section record |
| `01_CAD/sweep_v01/sweep_index.json` | 9e12270c1590aa5bce8fd5573602e93988412334e0222adee98d726c3fe38e20 | 20 sweep runs |
| `01_CAD/sweep_v01/sweep_summary.json` | c3a04bd6264736feba47d91a1c3373aee42470de17070aaff875ff01ec8ac09d | per-run status and worst margins |

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1 · tools from the repo (`tools.core`, `tools.measure`, `tools.drawing`, `tools.result`) · repo commit 10929db1408d89144bd4af9cad971440427933d0

## 3. Gate self-check

All values were measured on the re-imported `02_STEP_STL/od_t01_rig_C1_v01.step` and on the housing set placed by the measured seat. Bands are from GATES §0: mm 0.005, deg 0.001, rad 0.00002, mm³ 0.001, counts 0. Where a gate has several rows, the row shown is the least margin. Every row is in `gates_od_t01_rig_v01.json`. A self-check clears no HARD gate.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 solid | 1 | 0 | — | PASS | — |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1, 1, 0 | 0 | — | PASS | — |
| U-02 | 240.000 × 150.000 × 120.000 | each in [spec − 0.1, spec + 0.1] | +0.100 | — | PASS | — |
| envelope_within_spec | size 240.000 × 150.000 × 120.000; position x −120.000 … 120.000, y 0.000 … 150.000, z −60.000 … 60.000 | size and position each ± 0.1 | +0.100 | — | PASS | — |
| U-03a | Housing contact clearance 0.000 (nearest point y 135.000). Interference rig with housing 0.000 mm³, rig with OD-G04 0.000 mm³. Rig below y 135 to housing 15.010. Rig to OD-G04 5.000. Rig to OD-G10 13.689, not inside | contact = 0; interference ≤ 0; elsewhere ≥ 2.0 | +3.000 (OD-G04) | OD-G04 top, y 133.0 | PASS (assumed: A-01) | A-01 |
| U-03b | 16 poses, dy 0 … −30 in steps of 2.0. Interference with housing and with OD-G04 0.000 mm³ at every pose. OD-G10 least clearance 13.689 (at dy 0), never inside | interference ≤ 0 at every step (OD-G10: clearance > 0, not inside) | 0.000 mm³ | — | PASS (assumed: A-01) | A-01 |
| U-04 | AP242; 1 solid; volume delta 6.5e−8 mm³; face delta 0; label `od_t01_rig`; valid after re-import; 0 stray shells | unchanged, named, no stray shells, valid | −6.5e−8 mm³ (in band) | — | PASS | — |
| U-05 / feature_census | Faces: 41 planar, 13 concave cylinders, 0 convex, 0 other. Bores along Y: 4 × Ø3.4, 4 × Ø6.5, 1 × Ø60, 4 × Ø4.5. Corner chamfer planes 4. Wall inner faces 2, each z −60.000 … +40.000 | per plan §3 as amended by spec 1.1 | 0 | — | PASS | — |
| U-06 (Soft) | min_wall wide 3.000 | ≥ 2.0 | +1.000 | (−45.10, 135.00, −47.04), plate under a counterbore | PASS | — |
| U-07 | chordal 0.01; angular 0.10 rad; stl_max_sagitta 0.0050 (re-meshed from the STEP, 5752 triangles = delivered STL); delivered STL 1 body, 0 naked edges, winding consistent | tol ≤ 0.01; angular ≤ 4·acos(1 − 0.01/30) = 0.1033 rad; sagitta ≤ 0.01 | +0.0050 (sagitta) | — | PASS | — |
| U-08 | — | N/A by its row (no threads) | — | — | N/A | — |
| D-01a | min_wall 3.000 | ≥ 0.8 | +2.200 | (−45.10, 135.00, −47.04) | PASS | — |
| D-01b | min_wall 3.000 | ≥ 2.0 | +1.000 | (−45.10, 135.00, −47.04) | PASS (assumed: A-08) | A-08 |
| D-02 | 240.0 × 150.0 on the bed, 120.0 tall | ≤ 420 × 420 × 500 | +180.0 (least: bed X) | — | PASS (assumed: A-09) | A-09 |
| D-03a | Least downward angle 45.100° (build +Z) on the census copy with the four Ø3.4 holes filled; the census copy is 1 solid. Unfilled: the least is 0.0° at (−44.0, 135.0, −42.3), on a Ø3.4 crown, which is the named exception | ≥ 45° (crowns of the Ø3.4 holes excepted) | +0.100° | (21.25, 135.00, 21.18), window teardrop flank | PASS (assumed: A-10) | A-10 |
| D-03b | flat_ceiling_spans 0; Ø3.4 crown chord 3.400 | ≤ 5 (crowns ≤ 3.4); reviewer row from sections | +0.100 | — | PASS (reviewer row) | A-10 |
| D-04a | screw holes 4 × Ø3.400; bench holes 4 × Ø4.500 | ≥ 3.25; ≥ 4.25 | +0.150 | — | PASS | — |
| D-06a | min_wall 3.000 | ≥ 1.0 | +2.000 | — | PASS | — |
| D-07 | — | N/A by its row (clearance holes only) | — | — | N/A | — |
| J-05 | — | N/A by its row (no threaded holes) | — | — | N/A | — |
| REQ-01 | 4 × Ø3.400. Axis offset from the posed insert bores 0.000. Each hole opens at y 135.000 and runs through into its counterbore. 4 × Ø6.500 counterbores, offset 0.000, from y 150.000 to a floor at y 138.000. Plate under each head 3.000 | Ø3.4 ± 0.1; offset ≤ 0.10; Ø6.5 ± 0.1; floor 138.00 ± 0.10; 3.0 ± 0.1 | +0.100 (diameters, offsets, floor) | — | PASS (assumed: A-01) | A-01 |
| REQ-02 | One underside plane at y 135.000. The housing square's corners and edge midpoints (x ±50, z ±50) lie on it, 0.000 off. Contact clearance 0 (U-03a) | y 135.00 ± 0.10, one plane over x ±50, z ±50 | +0.100 | — | PASS (assumed: A-01) | A-01 |
| REQ-03 | Window Ø60.000, offset 0.000 from the axis, through. Two roof flanks at 45.100°. Apex z +42.501. OD-G04 to the rig 5.000. Pair-B axes to the window face: 10.970 at (+10.64, −15.78) and 11.689 at (−9.31, +16.60) | R 30.0 ± 0.1; 45.1° ± 1°; apex 42.51 ± 0.1; OD-G04 ≥ 2.0; pair-B axis ≥ 10.97 | −2e−8 (pair-B, in band) | (16.78, 135.00, −24.87) | PASS (assumed: A-05, A-12) | A-05, A-12 |
| REQ-04 | (a) φ −60° … +15° in 5° steps: least clearance 11.755, at φ +15°. φ > 0 turns the handle toward +X (verified). (b) φ −50°, dy −15, dz 0 … 200 in steps of 5.0: least clearance 28.689 at dz 50, never inside (the OD-G10 fallback) | (a) ≥ 5.0; (b) interference ≤ 0, read as clearance > 0, not inside | +6.755 (a) | (75.0, 90.4, 40.0), the +X wall's front end | PASS (assumed: A-07) | A-07 |
| REQ-05 | OD-G10 lowest point y 62.296, base top y 10.000: headroom 52.296 | ≥ 50.0 | +2.296 | OD-G10 lowest point | PASS (assumed: A-07) | A-07 |
| REQ-06 | 4 × Ø4.500, offset 0.000, through. The Ø8 driver probes from y 10 to y 300 interfere with the rig by 0.000 mm³ | Ø4.5 ± 0.1; offset ≤ 0.10; interference = 0 | +0.100 | — | PASS (assumed: A-11) | A-11 |
| REQ-07 | The Ø6 probes from y 150 to y 300 on the 4 screw axes interfere with the rig by 0.000 mm³ | = 0 | 0 | — | PASS | — |
| REQ-08 (Soft) | not geometric | the bench test | — | — | INCONCLUSIVE (Soft; hand calculation σ ≈ 10.5 MPa against ≈ 40 MPa, factor ≈ 3.8, A-02) | A-02 |

The check script tags U-03a and U-03b rows without A-01. Spec §5 lists A-01 for U-03, so the REPORT carries them as PASS (assumed: A-01).

## 4. Robustness sweep (D7)

Each run rebuilds the part at one parameter's low or high value, exports it to `01_CAD/sweep_v01/`, and runs every predicate of `check_od_t01_rig.py` on the re-imported export. The predicates include the motion checks U-03b and REQ-04 (a) and (b) in full, and each run has 167 rows. Nominal is the delivered export (§3). All 20 runs built exactly one solid and passed U-01, U-04 and U-05.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| screw_d | 3.3 · 3.4 · 3.5 | yes | D-04a Ø3.300 (low); D-03b crown 3.500 (high) | +0.050; REQ-01 Ø at band edge 0.000 |
| cbore_d | 6.4 · 6.5 · 6.6 | yes | REQ-01 Ø6.4 / Ø6.6 at band edge | 0.000 |
| cbore_floor_y | 137.9 · 138.0 · 138.1 | yes | D-01b min_wall 2.900 (low) | +0.900; REQ-01 floor and under-head at band edge 0.000 |
| screw_xz (radial offset 0.10) | 43.929 · 44.0 · 44.071 per axis | yes | REQ-01 offset 0.100 | −4.6e−7 (in band). Low run: D-03a exception-locator row FAIL (note 1) |
| window_r | 29.9 · 30.0 · 30.1 | yes | REQ-03 FAIL both sides. Low: apex 42.359, pair-B 10.870. High: apex 42.642 | −0.100 (pair-B, low); −0.051 (apex, low); −0.032 (apex, high) |
| theta_roof | 45.05 · 45.1 · 45.14 | yes | D-03a 45.050° (low); REQ-03 apex 42.464 / 42.531 | +0.050° |
| bench_d | 4.4 · 4.5 · 4.6 | yes | REQ-06 Ø at band edge | 0.000 |
| plate_y0 (housing pose moved with it) | 134.9 · 135.0 · 135.1 | yes | REQ-05 52.196 (low); D-01b 2.900 (high) | +2.196; +0.900. Low run: D-03a exception-locator row FAIL (note 1) |
| wall_x_in | 74.9 · 75.0 · 75.1 | yes | REQ-04 (a) 11.685 at φ +15° (low) | +6.685 |
| depth_z1 | 59.9 · 60.0 · 60.1 | yes | U-02 size_z 119.9 / 120.1 | 0.000 |

Worst value per gate over all 21 runs (nominal and 20 swept):
- U-03a: 5.000 (OD-G04, set by OD-G04, not by any rig parameter).
- U-03b: 0.000 mm³.
- D-01b: 2.900.
- D-03a: 45.050°.
- D-04a: 3.300.
- REQ-01 offset: 0.100.
- REQ-03: FAIL in the window_r runs.
- REQ-04 (a): 11.685.
- REQ-04 (b): 28.689.
- REQ-05: 52.196.
- Every other gate is in its band at every run.

**REQ-03 passes only at nominal window_r.** Note 2 explains why.

Note 1. The two D-03a FAIL rows are the exception locator, not an overhang. The gated D-03a row, the census with the Ø3.4 holes filled, reads 45.100° in both runs. The locator confirms that the unfilled least angle (0.0°) lies on a Ø3.4 crown. It accepts the crown only within r 1.75 of the nominal spec axes (±44, ±44) and between y 134.99 and 138.01. Two swept runs move the crown outside that window by construction:
- In the screw_xz low run the hole axes moved 0.10 inward. The 0.0° point (−43.929, 135.0, −42.229) is exactly r 1.70 from the swept axis but 1.772 from the nominal axis.
- In the plate_y0 low run the underside is y 134.9. The 0.0° point is at y 134.9, on the swept crown at the swept underside.

In both runs the 0.0° point is the crown of a Ø3.4 hole, which is the named exception. The locator did not move with the swept geometry.

Note 2. These are spec tolerances that do not stack:
- The apex is r / cos 45.1°, so ±0.1 on R moves the apex by ±0.141 against its own ±0.1 band.
- The pair-B threshold 10.97 is exactly 30.0 − 19.03, so any window smaller than R 30 reads below it. At R 29.9, a Ø17.9 head (A-12) clears the window by 1.92 instead of 2.0.

The nominal part meets both. No tolerance on R keeps REQ-03 true.

## 5. Build facts

- **Envelope** 240.000 × 150.000 × 120.000 (x ±120, y 0 … 150, z ±60).
- **Volume** 959 176.3 mm³; mass 1189 g at 1240 kg/m³ (PLA, §3, A-08).
- **Fillets:** none were requested. The four inside corners are 10 × 10 45° chamfers in the wall profile (spec §4), census 4 planes. There is no fillet ladder and no radius achieved to report.
- **Teardrops** are at 45.1° throughout:
  - window apex measured z +42.501;
  - counterbore apex 4.61 (design);
  - bench-hole apex 3.19 (design).
- **Walls** are z −60.000 … +40.000, measured. The plate and the base are z −60 … +60.
- **Placements:**
  - **OD-G01 housing:** placed by its rear-face plane on the plate's measured underside (y 135.000), with the spec §2 rotation (housing x → X, y → +Z, z → −Y). It is a rigid joint, axis (0, 1, 0) through x 0, z 0. Measured: the 4 insert-bore axes land on the Ø3.4 axes with offset 0.000.
  - **OD-G04:** rigid with the housing, at the v03 assembly's pose.
  - **OD-G10:** rigid with the housing at the v03 locked pose. φ is a revolute about (0, 1, 0) through x 0, z 0; φ > 0 turns the handle toward +X, verified by max_x.
  - **Solid identification:** the assembly solids are identified by measurement: the housing is the 100 × 100 solid, OD-G10 the one longer than 120, and OD-G04 the remaining one.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The rig stands on its 240 × 120 base at y 0 with the housing hung under the plate. The brew load pulls the housing down, away from the plate, into the four screws, as on OD-C05. When printed, the part lies on its rear face, a 120-deep prism with no unsupported island. |
| P2 | Function chains | Screw head on 3.0 of plate, into the insert in OD-G01, then the housing's lugs, the locked OD-G10, and the blind basket. The load path is closed by the plate, the two walls, the base, and the bench screws (z0 and z44 sections). |
| P3 | Motion clearance | The portafilter locks and unlocks over φ −60° … +15° with at least 11.755 to the rig. It goes in and out at φ −50°, 15 low, along +Z through the open front with at least 28.689. The housing set offers up from 30 below with no interference. |
| P4 | Human factors | The four screw heads and the hub are open from above (Ø6 probes clear to y 300). The bench-screw axes are clear for a driver (Ø8 to y 300). The handle leaves at the open front. 52.3 under the portafilter takes a catch tray or cup. |
| P5 | Absurdity next to a real product | A 240 × 150 × 120 closed frame, about 1.2 kg of PLA, holding a 100 × 100 group head. Its proportions are those of a bench press-fixture, sized for a 3 kN hydrostatic load (§4 factor about 3.8). |
| P6 | Floating, embedded, mirrored, upside-down | The housing touches the plate at y 135.000 with zero interference (not floating, not embedded). The teardrop roofs point to +Z, the build direction (y142 section). The walls end at z +40, so the z44 section cuts only the plate and base. The handle is on the +X side as in the v03 assembly. |

## 7. Library and tools used

- **Cards:** none, and "nothing matched" was a finding at D1 (plan §2).
- **`tools.core`:**
  - `read_step` for import;
  - `write_step` (AP242, fixed timestamp);
  - `write_stl` (clears the cached triangulation with BRepTools.Clean; also returns the max sagitta);
  - `validity` and `solid_count`;
  - `compare_step` for U-04.
- **`tools.measure`:**
  - `envelope`, `feature_census`, `bore_census`, `locate_bore`;
  - `min_wall` (with its `wide` detail);
  - `overhang_census(build_dir=(0,0,1))`, `flat_ceiling_spans`;
  - `clearance`, `interference`, `radial_extent`;
  - `mesh_census` (corroboration only).
- **`tools.drawing`:** `write_sections` and `nothing_clipped`.
- **New job code (in `01_CAD/` only):**
  - the pose helper;
  - the D-03a census copy, with the Ø3.4 holes filled by fused Ø3.6 cylinders between their measured ends;
  - the probe cylinders.
- **Missing tools:** no `tools/measure` function is missing.

## 8. Deviations from the plan

- **Spec 1.1 amendments carried as briefed:**
  - The walls run z −60 … +40, so U-05 expects 41 planar faces rather than the plan's 40.
  - Every teardrop is at 45.1° with the window apex at 42.51 ± 0.1.
  - REQ-03's pair-B axis check is ≥ 10.97 (A-12).
  - The OD-G10 interference is read through the `clearance` fallback.
- **Sweep driver:** the driver runs each swept check as three parallel processes (U-03b, REQ-04, and the rest). It merges their rows into one gates file per run, with the predicates unchanged, to fit the job's command limits after the restart.
- **REQ-01 opening row:** the hole's opening at y 135 is gated against the measured underside within the 0.005 band, which is tighter than the plan's ±0.10.
- No change to the geometry. Fix cycles used: 0 (no FAIL on the delivered part).

## 9. What I am least sure of

1. **REQ-03 has no tolerance on the window radius.** The pair-B axis-to-window distance measures 10.970 against a required 10.97: zero margin, passing inside the 0.005 band. In the sweep, R 29.9 reads 10.870 (FAIL), and R 29.9 / 30.1 put the apex at 42.359 / 42.642, outside 42.51 ± 0.1. A printed window that comes out slightly small reads as non-conforming. The underlying need is a Ø ≤ 17.9 head clearing by 2.0, which leaves 1.92 at R 29.9. The orchestrator may want to look at the REQ-03 tolerance stack or A-12.
2. **The D-03a exception is located by position.** The gated census fills the four Ø3.4 holes and reads 45.100°, a margin of 0.1°. The locator that confirms the unfilled 0.0° is a crown uses the nominal axes. It reads FAIL in two swept runs, although the point lies on the swept crown in both (§4 note 1). The reviewer should confirm the exclusion from the y142 and x44 sections.
3. **OD-G10 is not a sound solid** (brep_valid 0). Every OD-G10 interference row (U-03a, U-03b, REQ-04 (b)) is the accepted `clearance > 0, not inside` fallback, not a volume. The margins are large (13.689, 28.689), but no volume measurement backs them.

## 10. Stop

Not stopped. Every hard gate is met at nominal. The sweep findings in §4 and §9 are reported.

The machine-readable twin of this REPORT (schema `oguz-report-v1`, the same gate rows, sweep and least-sure list) was returned with the text; its gate rows are those of `01_CAD/gates_od_t01_rig_v01.json`.
