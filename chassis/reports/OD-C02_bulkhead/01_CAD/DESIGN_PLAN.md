# DESIGN_PLAN — od_c02_bulkhead (20260930-od-c02-bulkhead, concept C1)

Designer: Claude Code, claude-opus-5-5 · spec version 1.0 · written before any geometry (D2) · brief WP-02 (J3 package with its own plan)

## 1. Datum

The OD-C01 machine frame of spec §2, identity to every overlay: X to the user's right, +Y up, +Z toward the front, origin on the plate's top face under the group head's front axis line. The plate's top face is at y = 0 because the bulkhead's base rail stands on it (REQ-03, the designed contact of U-03); the wall's mid-plane is x = 65 because the OD-C01 bulkhead inserts lie on that line (OD-C01 A-04, spec A-01). Probe `01_CAD/probe/probe_placements_v01.json` measured the delivered plate's top face at y 0.000000 (one planar face, 96 725.984 mm²) and the four bulkhead inserts at (65, −45 / −105 / −165 / −225) at Ø4.000, offset 0.000 from the nominal axes, through, 6.0 long. No part of this job moves the frame.

## 2. Library and tools (D1)

- Cards read (one): UNO10 U5 tank heat-set (tags heat-set, boss, fdm): its lesson "keep how big and where apart in the envelope" is followed in U-02 (size and position gated apart). Its geometry is not reused; the spec fixes every boss value.
- Precedent named by the brief: `20260930-od-c01-base-frame/01_CAD/` (probe, `build_od_c01_frame_v02.py`, check and sections scripts): the joints and the script shape are reused.
- `tools/` functions reused: `tools.core` `read_step`, `write_step` (AP242, D-024), `write_stl`, `validity`, `compare_step`, `common_volume`, `mesh_sagitta`; `tools.measure` `envelope`, `bore_census`, `locate_bore`, `feature_census`, `min_wall` / `min_wall_wide` (spacing 0.7, brief note), `overhang_census(build_dir=(0,0,1), spacing=0.7)`, `radial_extent`, `clearance`, `interference`, `mass_properties`, `mesh_census`; `tools.result.gate` with the GATES.md §0 bands; `tools.drawing.write_sections`.
- New code needed (job code only, never in the repo): the face-by-position split of the downward faces (named-exception regions of D-03a, reported apart; a diagnostic beside the census, which cannot take a region); the planar-face reading of the rail underside and the front end face (REQ-03, REQ-04 window 4), read from the re-imported B-rep faces.
- Missing tool: none for a gated number. D-03b (bridge span) has no tool (GATES D-03b): reviewer from sections, as the row states.

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Wall x 63.0 … 67.0, y 0 … 215.0, z −240.0 … −30.0 | box | — | §4 C1, REQ-02, U-02 |
| F02 | Base rail x 59.0 … 70.0, y 0 … 12.0, full length | box, fused to F01 | F01 | §4, REQ-03, E-06 |
| F03 | Top rail x 62.0 … 73.0, y 207.0 … 215.0, full length | box, fused | F01 | §4, REQ-06, E-06 |
| F04 | Collars ×4, x 61.0 … 63.0: the window outline (F05) offset 2.0 outward, sharp joins, clipped to the envelope z ≤ −30.0 | extrude of the offset outline along +X, fused | F01 | §4, REQ-04, E-06 |
| F05 | Wire windows ×4 along X: lower half-circle Ø14.0 about the centre, vertical sides to 7.0 above the centre (the circle's top level), 45° gable roof to the apex 14.0 above the centre (7.0 above the circle's top); cut x 60.0 … 68.0 (collar and wall, before the ribs) | extrude of the outline, cut | F01, F04 | §4, REQ-04, D-03a |
| F06 | Ribs ×2 on the electric face, x 67.0 … 72.0, y 12.0 … 207.0, z −72 … −68 and −202 … −198 | box, fused after F05 | F01–F03 | §4, E-06 |
| F07 | Ø3.4 through-holes ×4 along Y at (65.0, z −45 / −105 / −165 / −225), cut y −1.0 … 5.0 | cylinder, cut | F02 | REQ-01, D-04a |
| F08 | Ø6.5 × 8.0 counterbores ×4 from the rail top, cut y 4.0 … 12.0 exactly (the wall stands above y 12) | cylinder, cut | F02, F07 | REQ-01 |
| F09 | Ø4.0 × 6.0 blind insert bores ×2 along −Y from y 215.0 at (67.5, z −60 / −210), cut y 209.0 … 216.0 | cylinder, cut | F03 | REQ-07, D-05b |

Expected census (U-05): 1 solid; `bore_census` finds 10 bores (4 × Ø3.4, 4 × Ø6.5, 2 × Ø4.0). The window's lower half-circle is a 180° concave cylinder, which `bore_census` does not count (it needs more than 180°), so each window's round part is read with `radial_extent` (inner radius on rays at 200°, 270° and 340° from +Y about +X at x 65; the circle through the three points gives the diameter and the centre offset). Feature counts per surface kind (`feature_census`) are compared with this plan's F01–F09: 4 concave window half-cylinders, 4 convex collar half-cylinders, 10 bores.

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| wall_x0 / wall_x1 | 63.0 / 67.0 | mm | ±0.10 | §2, §4, REQ-02, A-01 | yes |
| z_min / z_max | −240.0 / −30.0 | mm | ±0.1 | §4, U-02 | no |
| y_top | 215.0 | mm | ±0.1 | §4, REQ-06, A-06 | no |
| brail_x0 / brail_x1 / brail_h | 59.0 / 70.0 / 12.0 | mm | ±0.10 | §4, REQ-02, REQ-03, REQ-05 | yes (x0: 3.5 to OD-H01 measured by the probe) |
| trail_x0 / trail_x1 / trail_y0 | 62.0 / 73.0 / 207.0 | mm | — | §4, REQ-08, A-07 | no |
| rib_t / rib_x1 / rib_z | 4.0 / 72.0 / (−70.0, −200.0) | mm | — | §4, A-07 | no |
| collar_h / collar_w | 2.0 / 2.0 (OD 18.0 on the round part) | mm | — | §4, REQ-04 | no |
| win_d | 14.0 | mm | ±0.1 | REQ-04, A-04 | no |
| win_centres (y, z) | (150, −200), (150, −130), (150, −60), (60, −40) | mm | offset ≤ 0.10 | REQ-04, A-04 | no |
| win_gable_deg / win_apex_rise | 45.0 / 7.0 above the circle's top | deg / mm | — | REQ-04 (apex 7.0 above the circle's top); derivation: two 45° lines through the apex 14.0 above the centre cross the circle's vertical tangents y = ±7 at 7.0 above the centre, so the sides run straight up from the centre height to there | no |
| win_cut_x | 60.0 … 68.0 | mm | — | derivation: 1.0 past the collar face x 61 and the electric face x 67, cut before the ribs are fused so a rib behind a window stays whole (§4: ribs y 12 … 207) | no |
| hole_d / hole_xz | 3.4 / (65, −45 / −105 / −165 / −225) | mm | ±0.1; offset ≤ 0.10 | REQ-01, D-04a, A-01, A-03 | yes |
| cbore_d / cbore_depth | 6.5 / 8.0 from y 12.0 | mm | ±0.1 | REQ-01, A-03 | yes |
| insert_d / insert_depth / insert_xz | 4.0 / 6.0 / (67.5, −60 / −210) | mm | ±0.05; ±0.1 | REQ-07, D-05b, A-05 | yes |
| overshoot | 1.0 | mm | — | derivation: cutters pass 1.0 beyond a free face for clean booleans; the counterbore stops exactly at y 12 (the wall is above) | no |
| stl_tol / stl_ang | 0.01 / 0.20 | mm / rad | — | U-07: 0.20 ≤ 4·acos(1 − 0.01/6.0) = 0.2310 | no |
| density | 1070 | kg/m³ | — | §3, A-09 (reported only) | no |

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-C01 plate | `00_Spec/inputs/OD-C01_base_frame.step` (7b5688af…5805) | its own frame = the machine frame (top face y 0.000, inserts at x 65 measured) | identity (RigidJoint at the origin) | base rail underside y 0 on the top face; holes coaxial with the inserts |
| OD-C03 cradle + OD-H01 pump | `OD-C03_pump_cradle.step` (8d6f60ba…7034), `OD-H01_ulka_ep5_pump.step` (b05302af…fb62) | OD-C01 §4 joint: local x → +Z, y → −Y, z → +X, origin (0, 40, −205); OD-H01 at OD-C03's identity | RigidJoint | none (clearance ≥ 3.0; probe: OD-H01 max x 55.5, 3.5 from x 59) |
| OD-C04 mount + OD-H11 thermoblock | `OD-C04_thermoblock_mount.step` (31904ca8…a221), `OD-H11_thermoblock.step` (e2d186f2…38ff) | identity rotation at (0, 70, −140); OD-H11 at OD-C04's identity; OD-H11 unsound (brep_valid 0) | RigidJoint | none (probe: 9.0 and 16.16 from x 59) |
| OD-G01 housing v02 | `OD-G01_housing_C1_v02.step` (f8865cd1…7b02) | local x → X, y → +Z, z → −Y at (0, 180.06, 32) | RigidJoint | none (probe: 18.25 from the envelope) |
| OD-C05 foot box | none (reference box `od_c05_foot_reference_A02`) | x ±55, y 0 … 210, z −70 … −26 (brief, spec §2) | box from values | none (probe: 4.0 from x 59) |

## 6. Checks planned (D3)

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | `validity` | count 0 |
| U-02 | sizes 14.0 × 215.0 × 210.0 each ±0.1; position min/max x, y, z against §4 reported apart | `envelope` | mm 0.005 |
| U-03 (a) | rail underside to plate clearance 0 and common volume ≤ 0; four holes coaxial with the plate inserts ≤ 0.10 (`locate_bore` on both); clearance ≥ 3.0 to OD-H01, OD-H11, OD-C03, OD-C04, OD-G01 with nearest points; interference ≤ 0 each (OD-H11 INCONCLUSIVE by the row); ≥ 4.0 to the carrier box. (b) N/A | `clearance`, `interference`, `locate_bore` | mm 0.005, mm³ 0.001 |
| U-04 | part and assembly round trip: schema, solids, volume delta, faces delta, labels, valid after | `compare_step` | mm³ 0.001, count 0 |
| U-05 | census against §3 | `feature_census`, `bore_census`, `locate_bore` | count 0 |
| U-06 (Soft) | min_wall wide ≥ 2.0 | `min_wall_wide` sp 0.7 | mm 0.005 |
| U-07 | STL at 0.01 / 0.20 rad; angular ≤ 0.2310; sagitta ≤ 0.01; mesh closed | `write_stl`, `mesh_sagitta`, `mesh_census` | mm 0.005 |
| U-08 | N/A by its row | — | — |
| D-01a / D-01b / D-06a | min_wall ≥ 0.8 / ≥ 1.75 / ≥ 1.0 | `min_wall` sp 0.7 | mm 0.005 |
| D-02 | 14.0 × 215.0 on the bed ≤ 220 × 220, 210.0 tall ≤ 250 (A-08) | `envelope` | mm 0.005 |
| D-03a | least downward angle ≥ 45°, build dir +Z; the crowns of the ten small bores reported apart by position; the analytic angle of each window gable (45.0°, planar) beside the census | `overhang_census` sp 0.7, plus the job's face split | deg 0.001 |
| D-03b | reviewer from sections; the designer's reading from the census and sections | — | — |
| D-04a | Ø3.4 holes Ø ≥ 3.25 | `locate_bore` | mm 0.005 |
| D-05a | material across each insert bore along X ≥ 8.0 | `radial_extent` at 0° and 180° | mm 0.005 |
| D-05b | insert bores Ø4.0 ± 0.05, depth 6.0 ± 0.1 and ≥ 5.7 | `locate_bore` | mm 0.005 |
| D-07 | N/A by its row | — | — |
| J-05 | wall around each insert bore ≥ 3.0 (outer radius less the bore radius, both sides along X) | `radial_extent`, `locate_bore` | mm 0.005 |
| E-06 | collars and ribs on the wall, rails full length: reviewer; the designer reports each feature's contact with the wall from sections | — | — |
| REQ-01 | four Ø3.4 ± 0.1 through along Y, offset ≤ 0.10 (part and against the plate inserts); Ø6.5 ± 0.1, 8.0 ± 0.1 deep from y 12.0 | `locate_bore`, `bore_census` | mm 0.005 |
| REQ-02 | wet face x 63.00 ± 0.10 and electric face 67.00 ± 0.10 at y 100 and y 200 (`radial_extent`-free: planar faces read from the B-rep and the sections); rail wet face min_x 59.00 ± 0.10 | `envelope`, B-rep faces | mm 0.005 |
| REQ-03 | rail underside y 0.00 ± 0.10, one planar face over x 59 … 70, z −240 … −30; rail top y 12.0 ± 0.1 | `envelope`, B-rep faces | mm 0.005 |
| REQ-04 | lower half Ø14.0 ± 0.1 and offset ≤ 0.10 per window (three `radial_extent` rays on the lower half-circle; `bore_census` does not count a 180° arc); gable apex 14.0 above the centre (`radial_extent` inner toward +Z from the axis at x 65); the front end face at z −30 one planar face (window 4); collar round part OD 18.0 (`radial_extent` outer toward −Z at x 62) | `locate_bore`, `radial_extent`, B-rep faces | mm 0.005 |
| REQ-05 | min_x ≥ 59.0; the U-03 clearances ≥ 3.0 | `envelope`, `clearance` | mm 0.005 |
| REQ-06 | max_y 215.0 ± 0.1 | `envelope` | mm 0.005 |
| REQ-07 | two Ø4.0 ± 0.05 blind along −Y from y 215, depth 6.0 ± 0.1, offset ≤ 0.10 | `locate_bore` | mm 0.005 |
| REQ-08 | max_x ≤ 73.0; wall electric face ≤ 70 | `envelope` | mm 0.005 |
| REQ-09 | Soft bench: INCONCLUSIVE by its row | — | — |
| exactly_one_solid | solid_count == 1 | `validity` | count 0 |
| feature_census | as U-05 | `feature_census` | count 0 |
| envelope_within_spec | as U-02, size and position apart | `envelope` | mm 0.005 |

## 7. Risks

Found at D2 from the spec's own numbers (to be measured on the built part, not assumed):

1. **The counterbores lie under the wall.** The Ø6.5 counterbores are centred on x 65 (x 61.75 … 68.25) from the rail top y 12, and the wall x 63 … 67 rises from y 12 over them, so each counterbore's mouth is covered except for two 1.25 mm crescents. An M3 × 8 driven from above cannot reach its counterbore. §4 C3 argues the rail straddles the wall so the heads are clear of the wall; they are not.
2. **Window 4 (y 60, z −40) runs out of the front end z −30.** The gable apex 7.0 above the circle's top lies at z −26; the wall ends at z −30. With a tangent 45° teardrop instead (apex 2.9 above the top) the apex is at −30.10, leaving 0.10 of wall; its collar (2.0 around) cannot close either way.
3. **The ribs are horizontal shelves in the print.** Ribs 4.0 thick along Z, 5.0 deep along X, printed with build direction +Z: each rib underside is a 5 × 195 mm face at 0° from horizontal. §4 calls the ribs prisms along Z; they are not.
4. **The collars' round lower halves face down in the print** (their convex outer surface reaches 0° at the bottom). §4 calls every collar face vertical.
5. **The rib at z −200 crosses the pump window at (y 150, z −200)** on the electric face: the rib (z −202 … −198) runs across the window's mouth.

Fallback: none within the spec. The build follows §4 literally, the checks measure these, and a failing hard gate stops the package (D9) with the trade-off options; no feature is moved, reshaped or dropped.

Other risks: `min_wall` and `overhang_census` refuse the large faces at the default spacing (0.7 used, per the brief); OD-H11 is unsound, so its boolean rows are INCONCLUSIVE and its clearance gates on distance; the D-03a named exception is recorded in §5 for the Usta to confirm (GATES §X asks for a signature); D-01b's 1.75 lands exactly at the limit (margin 0).
