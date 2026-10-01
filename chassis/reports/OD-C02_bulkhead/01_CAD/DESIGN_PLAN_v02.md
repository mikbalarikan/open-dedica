# DESIGN_PLAN amendment v02 — od_c02_bulkhead (20260930-od-c02-bulkhead, concept C1)

Designer: Claude Code, claude-opus-5-5 · spec version 1.1 · brief WP-03 (J3 package, build attempt 2 of 2) · written before any v02 geometry (D3 follows)

This file amends `01_CAD/DESIGN_PLAN.md` (spec 1.0, left unchanged as the v01 record) with the plan amendments of brief WP-03 and spec 1.1 §4 and §5. Sections 1 (datum) and 5 (placements) of the base plan stand unchanged: the OD-C01 machine frame, identity to every overlay, and the same RigidJoints for OD-C01, OD-C03 + OD-H01, OD-C04 + OD-H11, OD-G01 v02 and the OD-C05 foot box. Everything below replaces sections 2, 3, 4, 6 and 7 of the base plan.

## 2. Library and tools (D1)

- Card: UNO10 U5 tank heat-set (as v01: size and position gated apart in U-02). No second card.
- `tools/` functions reused: `tools.core` `read_step`, `write_step` (AP242), `write_stl`, `validity`, `compare_step`, `common_volume`, `file_sha256`; `tools.measure` `envelope`, `bore_census`, `locate_bore`, `feature_census`, `min_wall`, `min_wall_wide` (spacing 0.7), `overhang_census(build_dir=(0,0,1), spacing=0.7)`, `radial_extent`, `clearance`, `mass_properties`, `mesh_census`; `tools.result.gate`; `tools.drawing.write_sections`.
- Job code (never in the repo): the D-03a census outside the named exception is `overhang_census` run on the re-imported solid with the six Ø4.0 insert bores refilled by position (each refill a Ø(measured + 0.2) cylinder on the bore's measured axis, from its mouth to 0.05 past its floor), so the named-exception crowns leave the census and nothing else changes (face count of the refilled solid checked against the plan: the part less 12 bore faces); the crowns' own least angle comes from the per-face split by position (reported apart). Coaxiality with the plate: the plate hole located at the point of the bulkhead bore's measured axis 3.0 below the plate top (y −3), so `locate_bore`'s offset is the perpendicular distance between the two axes.
- Missing tool: none for a gated number. D-03b has no tool (reviewer from sections); the designer reports the widest horizontal bore diameter measured by `bore_census` as the bridge span.

## 3. Feature order (v02)

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Wall x 63.0 … 67.0, y 0 … 215.0, z −240.0 … −30.0 | box | — | §4 C1, REQ-02, U-02 |
| F02 | Base rail x 59.0 … 71.0, y 0 … 12.0, full length | box, fused | F01 | §4, REQ-03, REQ-05, REQ-08, E-06 |
| F03 | Top rail x 59.5 … 70.5, y 207.0 … 215.0, full length | box, fused | F01 | §4, REQ-06, REQ-08, E-06 |
| F04 | Wire windows ×4 along X, outline in (Y, Z): lower half-circle Ø14.0 about the centre, straight sides at ±7.0 from the centre height up to 7.0 above the centre, 45° gable roof to the apex 14.0 above the centre (7.0 beyond the circle's +Z edge); cut x 62.0 … 68.0 (1.0 past both wall faces) at (y 150, z −200), (150, −130), (150, −60), (60, −55) | extrude of the outline, cut | F01 | §4, REQ-04, D-03a |
| F05 | Ø4.0 × 6.0 blind insert bores ×4 along +Y from the rail underside y 0 at (65.0, z −45 / −105 / −165 / −225); cutter y −1.0 … 6.0 | cylinder, cut | F02 | REQ-01, D-05a, D-05b, J-05 |
| F06 | Ø4.0 × 6.0 blind insert bores ×2 along −Y from y 215.0 at (65.0, z −60 / −210); cutter y 209.0 … 216.0 | cylinder, cut | F03 | REQ-07, D-05a, D-05b, J-05 |

Predicted census (U-05, `feature_census` on the re-imported solid):
- Planar faces 36: the I-profile extruded along Z has 12 side faces (rail underside, rail sides x 59 and x 71, rail top left and right, wall faces x 63 and x 67, top-rail underside left and right, top-rail sides x 59.5 and x 70.5, top face) plus the two end faces z −240 and z −30 = 14; each window adds 2 straight sides and 2 roof planes = 16; each bore adds its flat floor = 6.
- Cylindrical faces 10, all concave: 4 window half-cylinders R 7.0 and 6 bore walls R 2.0. Convex cylinders 0; other kinds 0; total faces 46.
- `bore_census`: 6 bores, all Ø4.0, blind; 4 along +Y with their mouth at y 0, 2 along −Y with their mouth at y 215. The window half-cylinders span 180°, which `bore_census` does not count; their round part is read by three `radial_extent` rays.
- Rail underside: one planar face at y 0 with four inner wires (the bore mouths); front end z −30: one planar face (window 4 closes inside the wall).

## 4. Parameters (v02)

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| wall_x0 / wall_x1 | 63.0 / 67.0 | mm | ±0.10 | §2, §4, REQ-02, A-01 | yes |
| z_min / z_max | −240.0 / −30.0 | mm | ±0.1 | §4, U-02 | no |
| y_top | 215.0 | mm | ±0.1 | §4, REQ-06, A-06 | no |
| brail_x0 / brail_x1 / brail_h | 59.0 / 71.0 / 12.0 | mm | ±0.10; x0 ≥ 59.0 (REQ-05), x1 ≤ 71.0 (REQ-08) | §4, REQ-02, REQ-03, REQ-05, REQ-08, A-07 | yes |
| trail_x0 / trail_x1 / trail_y0 | 59.5 / 70.5 / 207.0 | mm | — | §4, REQ-08, A-07 | no |
| win_d | 14.0 | mm | ±0.1 | REQ-04, A-04 | no |
| win_centres (y, z) | (150, −200), (150, −130), (150, −60), (60, −55) | mm | offset ≤ 0.10 | §4, REQ-04 | no |
| win_apex_rise | 7.0 beyond the circle's +Z edge | mm | — | REQ-04; derivation as the base plan (the two 45° roof lines through the apex 14.0 above the centre cross the vertical tangents y = ±7 at 7.0 above the centre) | no |
| win_cut_x | 62.0 … 68.0 | mm | — | derivation: 1.0 past each wall face | no |
| bore_d / bore_depth | 4.0 / 6.0 (all six) | mm | ±0.05 / ±0.1 | REQ-01, REQ-07, D-05b, A-03, A-05 | yes |
| base_bore_xz | (65.0, −45 / −105 / −165 / −225) | mm | offset ≤ 0.10 | REQ-01, A-01 | yes |
| top_bore_xz | (65.0, −60 / −210) | mm | offset ≤ 0.10 | REQ-07, A-05 | yes |
| overshoot | 1.0 | mm | — | derivation: cutters pass 1.0 beyond a free face | no |
| stl_tol / stl_ang | 0.01 / 0.20 | mm / rad | — | U-07: 0.20 ≤ 4·acos(1 − 0.01/6.0) = 0.2310 | no |
| density | 1070 | kg/m³ | — | §3, A-09 (reported only) | no |

Sweep (D7), low · nominal · high: bore_d 3.95 · 4.00 · 4.05; bore_depth 5.9 · 6.0 · 6.1; bore position shift (dx, dz) all six together (−0.07, −0.07) · 0 · (+0.07, +0.07) (a radial offset of 0.099, inside 0.10); wall_x0/wall_x1 together −0.10 · 0 · +0.10; brail_x0 58.9 · 59.0 · 59.1 and brail_x1 70.9 · 71.0 · 71.1 (the REQ-02 band; REQ-05 and REQ-08 make the band one-sided, reported as found). Every run exports into `01_CAD/sweep_v02/` and runs the full check.

## 6. Checks planned (D3), v02

As the base plan §6 with these rows changed:

| Gate | Predicate | `tools/measure` function | Band |
|---|---|---|---|
| U-02 | 12.0 × 215.0 × 210.0 each ±0.1; position x 59 … 71, y 0 … 215, z −240 … −30 reported apart | `envelope` | mm 0.005 |
| U-03 (a) | plate contact 0 and common volume ≤ 0; the four base bores coaxial with the plate's Ø4.0 holes ≤ 0.10; neighbours ≥ 3.0 with nearest points (OD-H11 boolean INCONCLUSIVE by the row); carrier box ≥ 4.0 | `clearance`, `common_volume`, `bore_census`, `locate_bore` | mm 0.005, mm³ 0.001 |
| U-05 / feature_census | planar 36, cylindrical 10, concave 10, convex 0, bores 6 (4 from below, 2 from above), window half-cylinders R 7.0: 4 | `feature_census`, `bore_census`, `locate_bore` | count 0 |
| D-01a / D-01b / D-06a | min_wall ≥ 0.8 / ≥ 2.0 / ≥ 1.0 | `min_wall` sp 0.7 | mm 0.005 |
| D-03a | census outside the named exception ≥ 45° (the refilled solid, see §2); whole-part census and the crowns' least angle reported apart | `overhang_census` sp 0.7 | deg 0.001 |
| D-03b | designer's reading: widest horizontal bore ≤ 5.0; windows gabled (REQ-04); reviewer from sections | `bore_census` | mm 0.005 |
| D-04a | N/A by its row | — | — |
| D-05a | material across each of the six bores along X ≥ 8.0 (two `radial_extent` outer rays at 0° and 180° at mid-depth) | `radial_extent` | mm 0.005 |
| D-05b | six bores Ø4.0 ± 0.05, depth 6.0 ± 0.1 and ≥ 5.7 | `locate_bore` | mm 0.005 |
| J-05 | per bore and side: outer ray less the measured radius ≥ 3.0 | `radial_extent`, `locate_bore` | mm 0.005 |
| REQ-01 | four bores along +Y from y 0: Ø4.0 ± 0.05, depth 6.0 ± 0.1, blind, offset ≤ 0.10 from the nominal axis and from the plate's holes | `locate_bore`, `bore_census` | mm 0.005 |
| REQ-03 | underside one planar face at y 0.00 ± 0.10 over x 59 … 71, z −240 … −30, four inner wires; rail top y 12.0 ± 0.1 at x 60 and x 69 | B-rep faces, `radial_extent` | mm 0.005 |
| REQ-04 | four windows at the spec centres: round part Ø14.0 ± 0.1 and offset ≤ 0.10 (three rays), apex 14.0 above the centre, front end one planar face; no collar (no R 9.0 face) | `radial_extent`, B-rep faces | mm 0.005 |
| REQ-07 | two bores along −Y from y 215: Ø4.0 ± 0.05, depth 6.0 ± 0.1, blind, offset ≤ 0.10 | `locate_bore` | mm 0.005 |
| REQ-08 | max_x ≤ 71.0; wall electric face ≤ 70 | `envelope`, `radial_extent` | mm 0.005 |

## 7. Risks (v02)

1. REQ-05 min_x ≥ 59.0 and REQ-08 max_x ≤ 71.0 sit exactly at the spec values; the carrier box clearance (≥ 4.0) is at its limit with the rail's wet face at x 59. Margin 0 by the spec's own numbers; the sweep shows the one-sided band.
2. The D-03a named exception has no Usta signature yet (spec §5: "for the Usta to confirm").
3. Spec ledger text lags §4 in two rows: A-05 names the top inserts at x 67.5 and A-04 names window 4 at z −40; §4 and REQ-07 / REQ-04 (x 65, z −55) govern the build.
