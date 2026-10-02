# DESIGN_PLAN — od_side_panels_v01: OD-C13 right panel, OD-C12 left panel, OD-C16 bracket, check assembly (20261002-od-c12-c13-c16-side-panels, concept C1)

Designer: Claude Code (claude-opus-5-5), designer doctrine · spec version 1.0 (ratified 2026-10-02) · written before any geometry (D2) · package WP-02, J2, attempt 1 of 2

Versions (D0): Python 3.13.7, build123d 0.11.1, OCP 7.9.3.1, repo commit 10929db1408d89144bd4af9cad971440427933d0.
Input hashes: all eight inputs of the brief match their SHA-256 (checked 2026-10-02).
Reference measurement script: `01_CAD/measure_refs_v01.py` (reads the inputs at their §2 poses; planning evidence, decides no gate).

## 1. Datum

- **Machine frame (spec §2), for the panels, the references and the check assembly.** The origin and axes are OD-C01's: X to the user's right, +Y up, +Z toward the user, the plate's top face at y = 0. The panels are modelled at their installed pose (identity) because every panel dimension in spec §4 is given in this frame and the panel's two contacts (underside on the plate top, top face under the lid's skirt) are planes of this frame. Measured on the delivered OD-C01: one top face at y 0.000 over x ±120, z −305 … +100; side faces x ±120.000 over z −295 … +90; four convex R 10.000 corner faces about (±110, −295) and (±110, +90). The datum the panel takes from the plate is therefore measured, not assumed.
- **Bracket frame (spec §4).** The origin is on the bracket's outer face (x 0) at the plate's top (y 0) and at mid-length (z 0), because the outer face is the bracket's contact with the panel's inner face and the underside its contact with the plate: placed at (±117.0, 0, z_c) both contacts land on measured planes (panel inner face x ±117, plate top y 0). The block is symmetric about z = 0, so the left pose (180° about Y) is the same part.

## 2. Library and tools (D1)

- Cards read (one): UNO10 U5 tank heat-set (tag heat-set, boss): blind insert bore practice; its lesson "keep size and position separate in envelope math" and "widen probe windows beyond the nominal cut" are applied in §6. Its mouth chamfer is not used: the spec gives a plain Ø4.0 × 6.0 bore and a chamfer would add a feature the census does not plan.
- `tools/` functions reused:
  - `tools.core.read_step`: re-import of every exported STEP and of the eight inputs.
  - `tools.core.write_step` (AP242): every part STEP and the assembly STEP (D-024).
  - `tools.core.write_stl`: each part's STL at tol 0.01 and the U-07 angular tolerance; its `checks["max_sagitta"]` is the U-07 sagitta (the spec's `stl_max_sagitta`); `tools.core.mesh_sagitta` as the same reading.
  - `tools.core.validity`, `step_roundtrip` / `compare_step`, `common_volume`.
  - `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `min_wall` (with `detail["wide"]`), `overhang_census`, `flat_ceiling_spans`, `clearance`, `interference`, `radial_extent`, `radial_profile`.
  - `tools.measure.drawing.write_sections` and `nothing_clipped` at D6 (sections only, no renders).
  - `tools.result.gate` with the GATES §0 bands.
- New code needed (job code only, under `01_CAD/`): the placement helper (a `Location(Plane(origin, x_dir, z_dir))` per §5 joint), the assembly-path stepper for U-03 (b), and the access/keep-out cylinders of REQ-07. No `tools/measure` function is missing for any gate; J-05 and D-05a are composed from `radial_profile` and `bore_census` (§6), because no single function measures "the wall around one named bore".

## 3. Feature order

### OD-C13 right panel (`build_od_c13_right.py`)

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Wall profile S1 in the plane y 0: inner line x 117.0 from z −299.0 to +94.0; end line z +94.0 to x 119.165; arc R 10 about (110, +90) to (120, 90); line x 120.0 to z −295.0; arc R 10 about (110, −295) to (119.165, −299.0); end line back to x 117.0 | sketch | — | §4 Wall; REQ-01 |
| F02 | Wall | extrude S1 along +Y, 0 … 215.0 | F01 | §4 Wall; REQ-01; U-02 |
| F03 | Top rail | box x 114.0 … 117.0, y 205.0 … 215.0, z −280.0 … +80.0, fused to F02 | F02 | §4 Top rail; E-06 |
| F04 | Lip | box x 114.0 … 116.6, y 215.0 … 225.0, z −280.0 … +80.0, fused to F03 | F03 | §4 Lip; REQ-02; D-04d |
| F05 | Merge coplanar faces | `clean()` after the fuses (wall top + rail strip into one y 215 face; rail and lip x 114 and end faces merged) | F04 | U-05 census |
| F06 | Three bracket holes Ø3.4 along X | cylinder cut, through x 114 … 120 (only the wall is crossed), axes at (y 10.0, z −262.0 / −15.0 / +62.0) | F05 | §4 Bracket holes; REQ-03; D-04a |

### OD-C12 left panel (`build_od_c12_left.py`)

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F11 | Right panel F01 … F06 rebuilt from the shared parameters | call of the right-panel builder | — | §4 OD-C12 |
| F12 | Mirror about x = 0 | `mirror(Plane.YZ)` | F11 | §4 OD-C12 |
| F13 | Valve-mount relief | box cut x −118.0 … −117.0, y 0 … 55.0, z −160.0 … −29.0 (opens through the underside) | F12 | §4 relief; REQ-04; D-01b |

### OD-C16 bracket (`build_od_c16_bracket.py`, bracket frame)

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F21 | Block | box x −19.0 … 0, y 0 … 16.0, z −8.0 … +8.0 | — | §4 OD-C16; REQ-05 |
| F22 | Plate-screw clearance hole Ø3.4 along Y at (x −12.5, z 0) | cylinder cut y 0 … 16.0 | F21 | REQ-05; D-04a |
| F23 | Counterbore Ø6.5 from y 16.0 to its floor at y 3.0 | cylinder cut y 3.0 … 16.0 (flat floor) | F22 | REQ-05 |
| F24 | Insert bore Ø4.0 × 6.0 blind along −X from x 0 at (y 10.0, z 0) | cylinder cut x −6.0 … 0, flat floor at x −6.0 (derivation: the spec gives a depth, not a drill point; a flat floor makes the depth one measured number) | F21 | REQ-05; D-05a; D-05b; J-05 |

No fillets are planned on any part: the spec gives none, and each would change the U-05 census. The fillet ladder is therefore not used; REPORT "radii achieved" will read "none planned".

### Check assembly (`assemble_od_side_panels.py`)

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F31 | Place the references (§5 table) | `Location(Plane(...))` per §2 joint | inputs | §2; U-03 |
| F32 | Place six brackets at (±117.0, 0, z_c), z_c ∈ {−262.0, −15.0, +62.0}; left side rotated 180° about Y | joint per §2 | F21 … F24 | §2; U-03; REQ-05 |
| F33 | Place the two panels (identity) | — | F06, F13 | §2 |
| F34 | Assembly STEP of all placed solids, one named occurrence each | `write_step` | F31 … F33 | §1 deliverables |
| F35 | Keep-out and access solids (not exported): four Ø8 × 2.0 cylinders above the feet holes; six r 4.0 cylinders on the bracket-screw axes, y 16.0 … 215.0; six r 4.0 cylinders on the panel-hole axes, from the outer face to 20.0 outside | built in the check script | F31 … F33 | REQ-07 |

Outputs (D5): `02_STEP_STL/od_c13_right_C1_v01.step` and `.stl`, `od_c12_left_C1_v01.step` and `.stl`, `od_c16_bracket_C1_v01.step` and `.stl`, `od_side_panels_C1_v01.step` (assembly). Sweeps into `01_CAD/sweep_v01/`. Sections `03_Sections/<part>_v01_<plane>.png`.

## 4. Parameters

All in one frozen structure, `01_CAD/params_od_side_panels.py`, imported at the top of each build and check script; no number below it.

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| wall_inner_x | 117.0 | mm | ± 0.10 | §4 Wall; REQ-01 | no (designed contact with the brackets at the §2 pose; see note 1) |
| wall_outer_x | 120.0 | mm | ± 0.10 | §4; REQ-01; measured OD-C01 side face x 120.000 | no |
| wall_y0, wall_top_y | 0.0, 215.0 | mm | ± 0.05 | §4; REQ-01; measured OD-C10 skirt bottom y 215.000 | no (designed contacts) |
| wall_z_rear, wall_z_front | −299.0, +94.0 | mm | ± 0.10 | §4; REQ-01 | no |
| corner_r, corner_centres | 10.0; (110, −295), (110, +90) | mm | ± 0.1 | §4; REQ-01; measured OD-C01 corner faces R 10.000 at those axes | no |
| end_arc_x | 119.165 | mm | derived | derivation: 110 + √(10² − 4²) = 119.1652 (the arc at 4.0 beyond the arc centres' z) | no |
| rail x, y, z | 114.0 … 117.0, 205.0 … 215.0, −280.0 … +80.0 | mm | — | §4 Top rail | no |
| lip_inner_x | 114.0 | mm | ± 0.1 | §4 Lip; REQ-02 | no |
| lip_outer_x | 116.6 | mm | ± 0.05 (from the REQ-02 gap 0.40 ± 0.05) | §4 Lip; REQ-02; D-04d; measured OD-C10 skirt inner face x ±117.000 | **yes** |
| lip_y | 215.0 … 225.0 | mm | ± 0.1 | §4; REQ-02 | no |
| lip_z | −280.0 … +80.0 | mm | ± 0.1 | §4; REQ-02 | no |
| panel_hole_d | 3.4 | mm | ± 0.1 | §4; REQ-03; D-04a (≥ 3.25) | **yes** |
| panel_hole_y, panel_hole_z | 10.0; −262.0, −15.0, +62.0 | mm | offset ≤ 0.10 | §4; REQ-03; A-07 | **yes** (coaxial with the bracket's insert bore) |
| relief_floor_x | −118.0 | mm | ± 0.10 | §4; REQ-04; A-04 | **yes** (OD-C07 clearance; D-01b wall; see §7 Q4) |
| relief y, z | 0 … 55.0; −160.0 … −29.0 | mm | ± 0.1 | §4; REQ-04 | no |
| block | x −19.0 … 0, y 0 … 16.0, z −8.0 … +8.0 | mm | size ± 0.1 | §4; REQ-05; U-02 | no |
| br_hole_d | 3.4 | mm | ± 0.1 | REQ-05; D-04a | **yes** |
| br_hole_x, br_hole_z | −12.5, 0 | mm | offset ≤ 0.10 | REQ-05 (puts the plate hole at ±104.5) | **yes** (on the new OD-C01 insert, A-01) |
| cbore_d | 6.5 | mm | ± 0.1 | REQ-05 (head Ø5.7, §2 fasteners) | **yes** |
| cbore_floor_y | 3.0 | mm | ± 0.10 | REQ-05 | **yes** |
| insert_bore_d | 4.0 | mm | ± 0.05 | REQ-05; D-05b; A-12 | **yes** |
| insert_bore_depth | 6.0 | mm | ± 0.1 | D-05b (≥ 5.7, the insert length) | **yes** |
| insert_bore_y, insert_bore_z | 10.0, 0 | mm | offset ≤ 0.10 | REQ-05 | **yes** (coaxial with the panel hole) |
| bracket_origin_x | ±117.0 | mm | — | §2 poses | no |
| z_c | −262.0, −15.0, +62.0 | mm | — | §2 poses; A-07 | no |
| stl_tol | 0.01 | mm | — | U-07 | no |
| stl_ang_panels | 0.1789 | rad | ≤ | U-07: 4·acos(1 − 0.01/10.0), R_max = 10.0 (the corner arcs) | no |
| stl_ang_bracket | 0.3139 | rad | ≤ | U-07: 4·acos(1 − 0.01/3.25), R_max = 3.25 (the counterbore) | no |
| step_timestamp | 2026-10-02T00:00:00 | — | — | derivation: pinned, the job date (write_step needs one) | no |

Note 1. The panel's inner face and the brackets' outer faces are a designed contact on one plane fixed by §2 (bracket origin x ±117.0). Sweeping one side alone moves a pose the spec fixes and reads interference or a gap by construction; the D7 sweep therefore does not move `wall_inner_x`, and the REPORT says so. Sweep plan (D7), each at nominal, low and high of its band above: `lip_outer_x` 116.55 / 116.65; `panel_hole_d` 3.3 / 3.5; panel hole position ± 0.10 in y and z (moved together, L-09); `relief_floor_x` −117.9 / −118.1; `br_hole_d` 3.3 / 3.5; bracket hole position ± 0.10; `cbore_d` 6.4 / 6.6; `cbore_floor_y` 2.9 / 3.1; `insert_bore_d` 3.95 / 4.05; `insert_bore_depth` 5.9 / 6.1; insert bore position ± 0.10 in y and z (moved together with the panel hole's high/low in the coaxiality check, all four corners).

## 5. Placements

All placements are a rigid joint `Location(Plane(origin, x_dir = image of local x, z_dir = image of local z))`, taken from the §2 rows; each rotation was checked right-handed (x × y = z). Measured envelopes as placed confirm each.

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-C01 base frame | `00_Spec/inputs/OD-C01_base_frame.step` (7b5688af…5805) | identity; top face y 0.000, side faces x ±120.000, corner faces R 10.000 about (±110, −295 / +90), 26 bores (measured) | fixed | panel undersides, bracket undersides |
| OD-C02 bulkhead | `OD-C02_bulkhead.step` (1e36348a…4bdc) | identity; measured x 59.0 … 71.0, y 0 … 215, z −240 … −30 | fixed | none of the new parts (clearance ≥ 0.5) |
| OD-C05 carrier | `OD-C05_group_head_carrier.step` (7b3d33ad…a5f1) | x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0); measured x ±55.0, y 0 … 210, z −70 … +82 | rigid | none |
| OD-C07 valve mount | `OD-C07_valve_flowmeter_mount.step` (55c1c361…3c) | x → −Z, y → −X, z → +Y, origin (−92, 0, −60); measured x −117.000 … −67.0, y 0 … 48.0, z −154.0 … −35.0; at x −117.000 only two pads, y 0 … 4.0, z −100 … −35 and −154 … −144 | rigid | OD-C12 relief (clearance ≥ 0.5) |
| OD-C08 tray | `OD-C08_electronics_bay_tray.step` (63686c46…da91) | identity; measured x 73.0 … 112.0, y 0 … 92.0, z −230 … −70 | fixed | none (5.0 to the right panel) |
| OD-C10 top panel | `OD-C10_top_panel.step` (0f85c4d7…b89f) | identity; skirt bottom face y 215.000 (one ring face); side-skirt inner faces x ±117.000 over y 215 … 247, z −295 … +90; rear/front skirt inner faces z −302.0 / +97.0, inner corner arcs R 7.0 | fixed | panel top faces (contact), lips (0.40) |
| OD-C11 back panel | `OD-C11_back_panel.step` (8ac0df9c…3db) | identity; wall x ±116.0, z −302.0 … −299.0, y 0 … 215; ledge x ±114.0, y 211 … 215, z −299 … −287; flanges x ±(72 … 104), z −299 … −277 | fixed | none (1.0 to the panel's rear end) |
| OD-C15 feet × 4 | `OD-C15_foot.step` (830f8026…46d7) | x → X, y → +Z, z → −Y, origins (±110, −6, +90), (±110, −6, −295); measured each 18 × 10 × 18 under the plate (y −16 … −6) | rigid | none |
| OD-C16 brackets × 6 | `02_STEP_STL/od_c16_bracket_C1_v01.step` (at D5) | right: x → X, y → Y, z → Z, origin (117.0, 0, z_c); left: x → −X, y → Y, z → −Z, origin (−117.0, 0, z_c) | rigid | plate top (contact), panel inner face (contact), panel hole coaxial with insert bore |
| OD-C12, OD-C13 | `02_STEP_STL/od_c1#_…_C1_v01.step` (at D5) | identity | fixed | plate top, lid skirt bottom, brackets |

## 6. Checks planned (D3)

Every check re-imports the exported STEP (`read_step`), gates `validity` first, and compares with `tools.result.gate` using the GATES §0 band: **0.005** for mm, **0.001** for degrees and mm³, **0** for counts and 1/0 facts. A raise or a missing value is INCONCLUSIVE. Scripts: `check_od_c13_right.py`, `check_od_c12_left.py`, `check_od_c16_bracket.py`, `check_od_side_panels_assembly.py`.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | each part file: solid count = 1 | `validity["solid_count"]` | 0 |
| U-01 | each part: solid_count = 1, brep_valid = 1, naked_edges = 0 | `validity` | 0 |
| envelope_within_spec / U-02 | size: OD-C13, OD-C12 6.0 × 225.0 × 393.0, OD-C16 19.0 × 16.0 × 16.0, each in [spec − 0.1, spec + 0.1]; position reported apart: min/max x, y, z against §5 U-02 | `envelope` | 0.005 |
| U-03 (a) contacts | each panel underside / plate, each bracket underside / plate, each bracket outer face / panel inner face, OD-C10 / each panel top: `clearance` = 0 and `interference` ≤ 0 | `clearance`, `interference` | 0.005 mm; 0.001 mm³ |
| U-03 (a) lip | `clearance`(each panel, OD-C10) read at the lip (the nearest points' x = ±116.6) = 0.40 ± 0.05; whole-panel `clearance` to OD-C10 is 0 (the seat), so the lip reading uses the lip region: `clearance`(panel ∩ box y > 215.0, OD-C10) | `clearance` | 0.005 |
| U-03 (a) others | every other pair, new part × {OD-C01 … OD-C15 feet, other new parts}: `clearance` ≥ 0.5 (pairs listed in the script, not by loop over bounding boxes) | `clearance` | 0.005 |
| U-03 (a) coaxiality | each of the six: `locate_bore` on the placed bracket (insert bore) and the panel (Ø3.4) at the point (±118.5, 10.0, z_c) along X; offset of each axis from the other ≤ 0.10 | `bore_census`, `locate_bore` | 0.005 |
| U-03 (b) path | (1) each bracket from y +20.0 to 0 in 2.0 steps (11 poses) with every delivered part present; (2) each panel from x ±20.0 outside its seat to 0 in 2.0 steps with the six brackets in place; (3) OD-C10 from y +40.0 to 0 in 2.0 steps (21 poses) with panels and brackets in place: `interference` ≤ 0 against every solid at every pose; worst pose reported | `interference` | 0.001 mm³ |
| U-04 | each part: `compare_step` after `write_step`: schema AP242, solids 1, volume_delta 0, faces_delta 0, label unchanged, valid after | `step_roundtrip` | 0.001 mm³; 0 counts |
| U-05 | `feature_census` exact (derived from §3, after `clean()`): OD-C13 plane 12, cylinder 5 (convex 2 = the R 10 corners, concave 3), bores 3 (Ø3.4 along X, through); OD-C12 plane 16, cylinder 5 (2 convex, 3 concave), bores 3; OD-C16 plane 8, cylinder 3 (concave 3), bores 3 (Ø3.4 along Y through, Ø6.5 along Y open at y 16 closed at y 3, Ø4.0 along X open at x 0 closed at x −6) | `feature_census`, `bore_census`, `locate_bore` | 0 |
| U-06 | `min_wall` `detail["wide"]` ≥ 2.0 per part, wrapped as a Result (missing key INCONCLUSIVE) | `min_wall` | 0.005 |
| U-07 | `write_stl` at tol 0.01, angular 0.1789 rad (panels), 0.3139 rad (bracket); `checks["max_sagitta"]` ≤ 0.01; triangles recorded | `write_stl`, `mesh_sagitta` | 0.005 (allowance in the limit, per GATES) |
| U-08 | N/A by its row (no threads) | — | — |
| D-01a | `min_wall` ≥ 0.8 per part | `min_wall` | 0.005 |
| D-01b | `min_wall` ≥ 2.0 per part; expected: OD-C13 2.165 (end), OD-C12 2.0 (relief), OD-C16 3.0 (counterbore floor, the global least; the 3.25 web is J-05's) | `min_wall` | 0.005 |
| D-02 | panel envelope 393.0 × 225.0 on the bed, 6.0 tall ≤ Kobra Max 3 (A-09: 420 × 420 × 500); bracket 19 × 16 × 16 ≤ K1C (A-10: 220 × 220 × 250): PASS_ASSUMED A-09 / A-10 | `envelope` | 0.005 |
| D-03a | panels `overhang_census(build_dir=(−1,0,0))` (OD-C13), `(1,0,0)` (OD-C12) ≥ 45°; bracket `(0,1,0)`: least over every face but the insert bore ≥ 45° (per-kind least for planes; every other cylinder is along +Y and cannot face down, read from `bore_census`), the insert-bore crown's least angle reported as the named exception. **Expected FAIL on both panels as the spec stands: §7 Q1, Q2** | `overhang_census`, `bore_census` | 0.001° |
| D-03b | bridges ≤ 5: reviewer from sections; `flat_ceiling_spans(max_span=5.0)` corroborates (bracket expected: the Ø4.0 crown is curved, not a flat ceiling; panels expected 20.0 at the lip, §7 Q1) | `flat_ceiling_spans`; sections | 0.005 |
| D-04a | the three Ø3.4 holes of each panel and the Ø3.4 hole of the bracket, diameter ≥ 3.25 | `bore_census`, `locate_bore` | 0.005 |
| D-04d | lip to OD-C10 skirt inner face ≥ 0.30 per side (the U-03 lip reading) | `clearance` | 0.005 |
| D-05a | material across the insert bore ≥ 8.0: `radial_profile` about the bore axis (origin (0, 10, 0), dir −X), angles every 15°, band over the bore depth with 0.1 margin, `r_min` = 2.0; 2 × the least outer radius | `radial_profile`, `bore_census` | 0.005 |
| D-05b | insert bore diameter 4.0 ± 0.05, length 6.0 ± 0.1 (≥ 5.7), open at x 0, closed at x −6 | `bore_census`, `locate_bore` | 0.005 |
| D-06a | `min_wall` ≥ 1.0 per part | `min_wall` | 0.005 |
| D-07 | N/A by its row | — | — |
| J-05 | wall around the insert bore ≥ 3.0: least of (a) `radial_profile` least outer radius − bore radius (expected 4.0, to the top face) and (b) the axial web = (bore floor x −6.0 to counterbore axis x −12.5) − counterbore radius, both from `bore_census` (expected 3.25). The global `min_wall` (3.0, the counterbore floor, not around this bore) is reported beside it, never instead | `radial_profile`, `bore_census`, `min_wall` | 0.005 |
| E-06 | reviewer from sections: one solid (U-01), lip tied into rail, rail into wall; sections at z −100 (XY plane) through wall, rail and lip, and through each bracket at z 0 | `write_sections`, `nothing_clipped` | — |
| REQ-01 | outer face x ±120.00 ± 0.10, inner face x ±117.00 ± 0.10 over z −295 … +90 (the two planar faces located by their normals and read by `envelope` of each face; sections at y 50 and y 200); underside one plane y 0.00 ± 0.05; top face y 215.00 ± 0.05 over x ±(116.6 … 120); end faces z −299.00 / +94.00 ± 0.10; corner faces R 10.0 ± 0.1: `radial_extent` about (±110, y, −295 / +90) along Y at 0°, 45°, 90° of each quarter and y 1, 107, 214; footprint over the plate: `common_volume`(panel footprint extruded to y −6 … 0, OD-C01) = footprint area × 6 (wholly over material) | `envelope`, `radial_extent`, `common_volume`, sections | 0.005 |
| REQ-02 | lip envelope x ±(114.0 … 116.6) ± 0.1, y 215 … 225 ± 0.1, z −280 … +80 ± 0.1 (lip region by `envelope` of panel ∩ box y > 215); `clearance` 0.40 ± 0.05; the seat as U-03 (a) | `envelope`, `clearance` | 0.005 |
| REQ-03 | three Ø3.4 ± 0.1 through along X at (y 10, z −262 / −15 / +62), offset ≤ 0.10, through = 1 | `locate_bore`, `bore_census` | 0.005 |
| REQ-04 | relief envelope (OD-C12 ∩ box x −118.5 … −117.0 removed region: the floor face x −118.00 ± 0.10 located by face census, y 0 … 55, z −160 … −29 ± 0.1); `clearance`(OD-C12, OD-C07) ≥ 0.5 (expected 1.0) | `envelope`, `feature_census`, `clearance` | 0.005 |
| REQ-05 | block size; Ø3.4 through along Y at (x −12.5, z 0), offset ≤ 0.10; Ø6.5 ± 0.1 counterbore, floor y 3.00 ± 0.10 (its closed end); Ø4.0 bore along −X at (y 10, z 0), offset ≤ 0.10; at the six poses the plate holes at (±104.5, z_c) ± 0.10 (`locate_bore` on the placed bracket) | `locate_bore`, `bore_census`, `envelope` | 0.005 |
| REQ-06 | each (±104.5, z_c): ≥ 8.0 from the plate edge; ≥ 6.0 centre to centre from the 26 measured OD-C01 bores and the handed-over inserts (OD-C08 (88/106, −222/−78), OD-C11 (±81/±95, −282)); plate solid in a Ø8 circle (`common_volume` of a Ø8 × 6 cylinder with OD-C01 = its volume). Measured at D1: least edge distance 15.5, least to an existing bore 28.31 ((−113, −42) Ø4.0), least to a handed-over insert 22.14 ((±95, −282)), disc fill 301.593 of 301.593 mm³ at all six | `bore_census`, `common_volume` | 0.005; 0.001 mm³ |
| REQ-07 | `interference` = 0 of the new parts with the four Ø8 × 2.0 keep-outs; of the six bracket-screw access cylinders (r 4.0, y 16 … 215) with every solid but the panels and OD-C10 (D1 screen: 16.0 clear of everything, the plate below); of the six panel-hole access cylinders (r 4.0, outer face to 20.0 outside) with every solid | `interference` | 0.001 mm³ |
| REQ-08 | Soft, bench: reported INCONCLUSIVE with a risk rating (A-13) | — | — |

## 7. Risks and questions

### Questions for the orchestrator (spec values my measurement contradicts)

- **Q1 (blocking D-03a and D-03b, both Hard).** Spec §4 and D-03a say the panels, printed on their outer face, have "no downward face" and that "rail, lip and the end faces rise as vertical prisms". They do not: in that orientation the lip (y 215 … 225) stands beyond the wall's top edge, and its face x ±116.6 is a flat ceiling 3.4 above the bed, 10.0 deep and 360 long, carried only along y 215 by the rail; the gap under it (x ±116.6 … ±120, y 215 … 225) is where the lid's skirt goes, so it cannot be filled. On an in-memory proxy of the spec geometry (nothing exported) `overhang_census(build_dir=(−1,0,0))` reads **0.0°** at (116.6, 225.0, −280.0) against ≥ 45, and `flat_ceiling_spans(max_span=5)` reads **20.0** (carried on one side, 2 × 10) against ≤ 5. As written the spec cannot pass D-03a/D-03b on either panel. Options for the Usta: (a) sign supports under the lip (A-11 amended, a named exception); (b) another print orientation (e.g. standing on the underside, build +Y: the lip becomes a vertical prism, but the rail's underside y 205 becomes a 3.0 cantilever, needing a 45° chamfer under the rail, and the three Ø3.4 holes turn horizontal with crown exceptions; 393 × 6 on the bed, 225 tall); (c) a separate lip strip fastened to the rail (a new part). I will not choose; J3 should not start until the spec says which.
- **Q2 (blocking D-03a).** The outer corner faces R 10 lift off the bed in the same orientation: they face downward from 0° at x 120 to 23.6° at the end faces, rising to 0.835 above the bed over the last 4.0 of each end (geometry: 10 − 9.165). The proxy reads 5.9° at a 1.0 spacing (the refined least will be lower). REQ-01 fixes the arc, so this needs a named exception (a sliver within the first 0.84 of the print) or another orientation (Q1 b removes it).
- **Q3 (non-blocking, wording).** §4 says the lip "ends 15 short of the lid's rear and front skirts". Measured on OD-C10: rear and front skirt inner faces at z −302.0 and +97.0 and inner corner arcs R 7.0, so the lip ends at z −280 / +80 are 22.0 / 17.0 from the flat inner faces and 17.3 / 12.3 from the inner arcs at x ±116.6. I follow the REQ-02 z range −280.0 … +80.0; please confirm the "15" is descriptive only.
- **Q4 (non-blocking, zero margin).** D-01b ≥ 2.0 meets OD-C12's relief wall at exactly 2.0 (x −120 to −118); REQ-04 allows the relief floor ± 0.10, so the D7 high sweep (−118.1) reads 1.9 and fails D-01b. The part will be reported as passing at nominal and low only, unless the Usta moves the floor (e.g. −117.9 keeps 0.9 to OD-C07 and 2.1 of wall; OD-C07 touches x −117 only with two pads at y 0 … 4).

### Interface values confirmed by measurement (D1)

OD-C01 outline x ±120.000, z −305 … +100, top y 0, R 10.000 corners about (±110, −295 / +90), feet holes Ø3.4 at (±110, −295 / +90), 26 bores, none at the six new positions; OD-C10 side skirt inner faces x ±117.000, skirt bottom y 215.000, nothing of the lid within x ±(113 … 117), y 200 … 247, z −285 … +85 (`common_volume` 0.000 mm³; the 102.97 mm³ over the full length is the rear and front skirts beyond the lip's ends); OD-C11 wall x ±116.0, z −302 … −299 (1.0 to the panel's end); OD-C07 as placed reaches x −117.000 (two pads at y 0 … 4); OD-C08 x 73 … 112, y 0 … 92, z −230 … −70; feet 18 × 10 × 18 under the plate at the four poses. Proxy boxes of the spec's wall, rail, lip and brackets: the only readings under 1.0 are the designed contacts (0.0 with OD-C01 and OD-C10), the lip's 0.400 to OD-C10, and the left wall's 0.0 to OD-C07 that the relief removes.

### Build risks

- `clean()` may not merge every coplanar pair; the census in §6 is then off by the unmerged faces. Fallback: build the panel cross-section with the rail and lip in one profile where possible; report any residual split as a deviation, never as a census change without a note.
- The mirror (F12) must give an outward-oriented solid; `brep_valid`'s positive-volume stage checks it.
- Assembly path U-03 (b): 6 × 11 + 2 × 11 + 21 poses against up to 17 solids; runtime is the only risk (booleans are prefiltered by box in `common_volume`).
