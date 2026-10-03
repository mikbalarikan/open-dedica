# DESIGN_PLAN — od_c09_front (20261002-od-c09-front-panel, concept C1)

Designer: Claude Code (claude-opus-5-5) · spec version 1.0 (SHA-256 8206704f…ba69c, matches the brief) · written before any geometry (D2) · package WP-02, J2, attempt 1 of 2

Versions recorded at D0: Python 3.13.7, build123d 0.11.1, OCP 7.9.3.1 (OCCT 7.9.3), repo commit 10929db. Every input SHA-256 in the brief was checked and matches.

D1 measurements behind every "measured" value below were taken on the input STEPs as posed by spec §2, with the scripts in `01_CAD/plan_v01/` (`poses.py` holds the two §2 transforms, checked on four points each; `standin.py` is a planning probe of boxes and cylinders, never exported). They are leads for the plan; every gate is measured again at D5 on the exported STEP.

## 1. Datum

The OD-C01 machine frame, unchanged (spec §2): the plate's top face is y = 0 and the origin is on it, on the machine's centre plane x = 0, because the panel stands on that face and every chassis part (OD-C01, OD-C10, OD-C11) is delivered in this frame, so every overlay is the identity. X to the user's right, +Y up, +Z toward the user. The panel's outer face is the plane z = +97.0 and its inner face z = +94.0 (§2). The housing-frame parts and OD-E02 are brought into this frame by the §2 poses, never by bounding boxes:

- housing frame → machine: x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0); measured: housing origin maps to (0, 180.06, 32.0), +y to +Z.
- OD-E02 board frame → machine: x → −Y, y → −X, z → −Z, origin (−99.0, 140.0, 69.35); measured: board +x maps to −Y, +y to −X, +z to −Z.
- OD-G10 "rotated by φ": a rotation about the line (x 0, z 32) along +Y; φ > 0 turns +Z toward +X (right hand about +Y).

## 2. Library and tools (D1)

- Cards read (at most two): UNO10 U5 tank heat-set (index row and card entry only): a heat-set boss with a blind bore, plane census, two-tier QA. Its lesson used here: keep "how big" and "where" apart in the envelope check, and widen probe windows past the nominal cut. No second card matched (no library card covers a large flat printed panel or a scanned OEM board placed by a pose): a finding.
- `tools/` functions reused:
  - `tools.core.read_step`, `solids`, `validity` (`solid_count`, `brep_valid`, `naked_edges`): U-01, every reference solid's soundness.
  - `tools.core.write_step` (AP242, D-024), `step_roundtrip` / `compare_step`: U-04, the part and the check assembly STEP.
  - `tools.core.write_stl`, `mesh_sagitta`: U-07.
  - `tools.core.common_volume` through `tools.measure.interference`: U-03, REQ-03, REQ-05 (b), REQ-06, REQ-07.
  - `tools.measure.clearance`: U-03 (a) gaps and contacts, E-01, REQ-05 (a), the fallback of §7 Q6.
  - `tools.measure.envelope`: U-02, D-02, REQ-01, REQ-02, REQ-04 (cap foremost points), REQ-07.
  - `tools.measure.feature_census`, `bore_census`, `locate_bore`: U-05, D-04a, D-05a, D-05b, E-05, REQ-01, REQ-04.
  - `tools.measure.min_wall`, `min_wall_wide`: D-01a, D-01b, D-06a, J-05, U-06.
  - `tools.measure.radial_extent`: D-05a (material across each insert bore, read at 0°…330° every 30° at three levels).
  - `tools.measure.overhang_census(build_dir=(0, 0, -1))`: D-03a; `flat_ceiling_spans(build_dir=(0, 0, -1), max_span=5.0)`: D-03b corroboration for the reviewer.
  - `tools.drawing.write_sections`, `nothing_clipped`: D6 sections (planes listed in §6).
  - `tools.result.gate` with the GATES §0 bands: every comparison.
- New code needed (job-local, under `01_CAD/`, never in the repo):
  - the two §2 poses as `gp_Trsf` (`plan_v01/poses.py`, to be copied into `check_od_c09_front.py`): no tool places a part by a stated frame mapping;
  - the OD-G10 travel loop (rotation about the housing axis, the lowering and the +Z carry of REQ-05 (b)), and the lowering loop of U-03 (b): a loop over `clearance` / `interference`, nothing new measured;
  - the E-01 exclusion of the two designed contacts (§7 Q7);
  - the fallback for the two unsound reference solids (§7 Q6).
  No missing `tools/measure` function is needed for any gate.

## 3. Feature order

All features are one solid, built in build123d Algebra mode with named intermediates (U-14). No fillets: the spec names none and asks for square corners at the opening; U-06 is then read on sharp corners only.

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Wall, 3.0 thick, x −116 … +116, y 0 … 215, z +94 … +97 | box (rectangle on the XY plane at z +94, extruded +3.0 along Z) | — | §4 wall; REQ-02, U-02 |
| F02 | Brew opening = tray slot (x ±75, y 0 … 50) ∪ portafilter window (x −57.5 … +75, y 0 … 188), square corners | one cut of the union of two boxes through the wall along Z (each box z +93 … +98, open at y 0) | F01 | §4 brew opening; REQ-03, REQ-05 |
| F03 | Return ribs R1…R5, 3.0 thick, z +84 … +94 | five boxes fused to the wall's inner face: R1 x −60.5 … +78, y 188 … 191; R2 x +75 … +78, y 0 … 191; R3 x −60.5 … −57.5, y 50 … 191; R4 x −78 … −75, y 0 … 53; R5 x −78 … −57.5, y 50 … 53 | F02 | §4 return ribs; U-05, D-01b, REQ-07, U-03 (≥ 2.0 to the brew area) |
| F04 | Floor flanges ×2, 4.0 thick, y 0 … 4, z +72 … +94, x −104 … −76 and +76 … +104 | two boxes fused to the wall | F01 | §4 floor flanges; U-03 (contact on OD-C01), REQ-01 |
| F05 | Gussets ×4, 4.0 thick, at x ±(76 … 80) and ±(100 … 104): right triangles in YZ, vertices (y 4, z 78), (y 4, z 94), (y 34, z 94) | triangle sketched on a YZ plane, extruded 4.0 along X, fused | F04 | §4 gussets; E-06, D-03a (hypotenuse faces up in print) |
| F06 | Flange holes ×4, Ø3.4 through along Y (y 0 … 4) at (x ±85, z +77) and (x ±95, z +77) | four cylinders cut along Y | F04 | §4; REQ-01, D-04a, REQ-06; D-03a named exception |
| F07 | Board bosses ×2, Ø11.0, axes along Z through the board's two screw holes as measured (L (−91.055, 153.235), R (−90.999, 127.251)), from the wall's inner face z +94 back to the end level (§4 table `boss_end_z`, §7 Q2) | two cylinders fused to the wall | F01 | §4 board bosses; E-05, U-03 (contact), E-06 |
| F08 | Boss collar reliefs ×2 (only if Q4 is answered (a)): each boss cut by a cylinder about the neighbouring cap collar's axis, radius collar + 0.5, from the boss end to the collar's front + 0.5 | two cylinder cuts | F07 | E-01 (§7 Q4) |
| F09 | Insert bores ×2, Ø4.0 × 6.0 blind from each boss end face, coaxial with the boss | two cylinder cuts | F07, F08 | §4; D-05a, D-05b, J-05, E-05 |
| F10 | Button holes ×3, Ø15.0 round, through the wall along Z, on the measured cap axes (B1 (−94.248, 166.514), B2 (−98.991, 139.901) at z +95.5, B3 (−93.765, 113.426)) | three cylinder cuts along Z, z +93 … +98 | F01 | §4 button holes; REQ-04, E-01 |
| F11 | Steam knob place (phase 2): Ø32 along Z about (+95.5, 140.0), z +60 … +93.8 kept free | no geometry; a keep-out the check reads | F03 | §4; REQ-07, A-13 |
| F12 | Keep-outs: nothing at z < +72, nothing in the tray slot box | no geometry; checked | all | §4; REQ-07 |
| F13 | Top edge y 215 on which OD-C10's front skirt stands (line contact along z +97) | is F01's top face; no extra operation | F01 | §4; U-03 (contact), A-07 |

## 4. Parameters

Only the names below appear in `build_od_c09_front.py`; nothing numeric below the parameter block. Fit-critical rows are swept at D7 (nominal, low, high).

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| wall_x_half | 116.0 | mm | ±0.1 | §4 wall; REQ-02 | yes (side panels, plate corners) |
| wall_z_in / wall_z_out | 94.0 / 97.0 | mm | ±0.10 | §2 frame; REQ-02 | yes (OD-C10 skirt, OD-C15 keep-outs touch z 94) |
| wall_top_y | 215.0 | mm | ±0.10 | §4; OD-C10 skirt bottom measured y 215.0 (§2) | yes (A-07 contact) |
| slot_x_half, slot_top_y | 75.0, 50.0 | mm | ±0.1 | §4; A-06 | yes (REQ-03, REQ-07: 0.2 to the tray box) |
| win_x_left, win_x_right, win_top_y | −57.5, +75.0, 188.0 | mm | ±0.1 | §4; A-05 | yes (REQ-05) |
| rib_t, rib_z_back | 3.0, 84.0 | mm | — | §4 | yes (≥ 2.0 to the brew area: carrier and housing flange end at z 82.0) |
| R1…R5 extents | as F03 | mm | — | §4 | no |
| flange_t, flange_z_back, flange_x_in, flange_x_out | 4.0, 72.0, 76.0, 104.0 | mm | — | §4 | no |
| gusset_t, gusset_leg_z, gusset_leg_y | 4.0, 16.0, 30.0 | mm | — | §4 | no |
| flange_hole_d | 3.4 | mm | ±0.1 | §4; REQ-01, D-04a (≥ 3.25) | yes |
| flange_hole_xz | (±85, 77), (±95, 77) | mm | offset ≤ 0.10 | §4; A-01 | yes (REQ-01) |
| boss_d | 11.0 | mm | — | §4; D-05a, J-05 (3.5 wall) | yes (E-01 against the cap collars, §7 Q4) |
| boss_axis_L, boss_axis_R | (−91.055, 153.235), (−90.999, 127.251) | mm | E-05 ≤ 0.10 | measured: `bore_census` of the posed OD-E02, the Ø3.538 and Ø3.441 through bores, both along Z (equal x, y at both ends to 0.001) | yes |
| boss_end_z | 85.485 (both) — proposed, pending §7 Q2 (spec text: near 81.2 / 81.8) | mm | contact = 0 | measured: the flat of the posed OD-E02 around each hole, first hit along −Z, 85.485 at r 3.6 … 6.0 over 80° … 280° on both holes | yes (U-03 contact, E-01) |
| relief_r_L, relief_r_R | collar radius + 0.5 about the B1 / B3 collar axes (B1 collar r 8.09, B3 r 8.19, report values to be re-measured on the STEP at D3) | mm | — | derivation for E-01 ≥ 0.5 (§7 Q4) | yes |
| insert_bore_d, insert_bore_depth | 4.0, 6.0 | mm | ±0.05, ±0.1 | §2 OD-F01; D-05b | yes |
| button_hole_d | 15.0 (all three) | mm | — | §4; derivation in §7 Q5: least measured wall-to-board gap 1.136 (at B2) ≥ 0.5 | yes (E-01) |
| B1, B2, B3 hole axes | (−94.248, 166.514), (−98.991, 139.901), (−93.765, 113.426) | mm | REQ-04 ≤ 0.25 | measured: B2 section centroid at z 95.5; B1, B3 the axes of their elliptical cap prisms (`OD-E02_REPORT.md` `cap_B1_ellipse`, `cap_B3_ellipse`, posed; section centroids at z 91 agree within 0.02) | yes |
| knob_place | Ø32 about (+95.5, 140.0), z +60 … +93.8 | mm | — | §4, A-13 | no (keep-out) |
| print build_dir | (0, 0, −1), front face on the bed | — | — | §4, A-09 | — |
| stl_tol, stl_ang | 0.01 mm; a ≤ 4·acos(1 − 0.01/R_max), R_max = 7.5 (the Ø15 holes) → a ≤ 0.2066 rad, used 0.2 | — | — | U-07 | — |

## 5. Placements

None of these is part of the panel; they are placed for the check assembly and every assembly gate by the §2 poses.

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-C01 base frame | `00_Spec/inputs/OD-C01_base_frame.step` (7b5688af…5805) | identity (its own machine frame); measured plate y −6 … 0, x ±120, z −305 … +100; 26 bores, only (±110, +90) Ø3.4 near this panel | identity | wall and flange undersides on its top face y 0 (contact) |
| OD-C05 carrier | `00_Spec/inputs/OD-C05_group_head_carrier.step` (7b3d33ad…f1) | housing frame, §2 pose; measured x ±55, y 0 … 210, z −70 … +82 (z > 70 only its top plate, y 205 … 210) | fixed by the §2 pose | none (≥ 2.0; stand-in panel reads 12.0) |
| OD-G01 housing, OD-G04, OD-G10 locked | `00_Spec/inputs/od_g01_assembly_C1_v03.step` (9fd18eb5…f2) | housing frame, §2 pose; three solids, identified by measurement: housing (90 217 mm³, x ±50, y 176.76 … 205; body to z 75.1, its flange y 195 … 205 to z 82.0), OD-G04 (17 086 mm³, z ≤ 66.5), OD-G10 (137 692 mm³, the one reaching y 191.3 and z 182.1; handle at the wall x 19.7 … 52.7, y 146.9 … 174.0) | fixed by the §2 pose; OD-G10 also rotated / moved per REQ-05 | none (housing, OD-G04 ≥ 2.0; OD-G10 per REQ-05) |
| OD-C10 top panel | `00_Spec/inputs/OD-C10_top_panel.step` (0f85c4d7…af89f) | identity; front skirt z 97 … 100 down to y 215.0 | identity | its skirt bottom on the wall's top face, along the line z +97 (A-07) |
| OD-E02 board | `00_Spec/inputs/OD-E02_control_board.step` (4e570b4a…5385) | board frame, §2 pose (pending §7 Q1); measured extents x −115.17 … −61.53, y 101.84 … 178.63, z 50.40 … 98.56 | fixed by the §2 pose; the bosses are placed on its measured hole axes | the two boss end faces on its front flat (contact) |
| OD-C11, OD-S03 | reference only | — | not placed | — |

## 6. Checks planned (D3)

One script `01_CAD/check_od_c09_front.py`: it re-imports `02_STEP_STL/od_c09_front_C1_v01.step`, gates `validity` first, measures with `tools/measure`, compares with `tools.result.gate` using GATES §0 bands: **0.005 mm** for mm, **0.001 mm³** for interference, **0.001°** for angles, **0** for counts and 1/0 facts. The limit is always the §5 value. Any exception or missing value is INCONCLUSIVE. Unsound reference solids (OD-G10, OD-E02, §7 Q6) are handled as Q6 says, never read as a pass.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | `solid_count == 1` | `tools.core.solid_count` | 0 |
| U-01 | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | `tools.core.validity` | 0 |
| envelope_within_spec / U-02 | sizes 232.0 × 215.0 × 25.0 each within ±0.1 (gated as two one-sided rows each); position reported apart: x ±116.0, y 0 … 215.0, z +72.0 … +97.0 | `envelope` | 0.005 mm |
| U-03 (a) contacts | `clearance = 0` (≤ 0.005 band, read as `== 0`): wall and both flange undersides to OD-C01; each boss end face to OD-E02 (§7 Q6 for the solid); OD-C10 to the wall's top edge | `clearance` | 0.005 mm |
| U-03 (a) interference | every pair of {panel, OD-C01, OD-C05, housing, OD-G04, OD-G10, OD-C10, OD-E02} as placed `≤ 0` mm³ (pairs with OD-G10 or OD-E02 per §7 Q6) | `interference` | 0.001 mm³ |
| U-03 (a) footprint | the panel's section at y 0 … 0.01 inside the plate outline, `clearance` from the panel's foot to the plate's front and side faces and the two corner arcs ≥ 0.5 (measured as the distance from the foot section to a skin solid 0.01 thick outside the plate's outline; design reading 0.78 at the corner (116, 97) to the R10 arc) | `clearance` | 0.005 mm |
| U-03 (a) holes | flanges to the edge of every existing OD-C01 hole ≥ 3.0, the wall's foot ≥ 2.0 (each hole as a cylinder Ø of its bore, y −6 … 0, then `clearance` to the flange solids and to the wall's foot band y 0 … 0.5); the four flange hole centres ≥ 6.0 from every existing hole centre (`bore_census` of both parts, XZ distance) | `clearance`, `bore_census` | 0.005 mm |
| U-03 (a) brew area | panel to OD-C05, to the housing and to OD-G04 ≥ 2.0 | `clearance` | 0.005 mm |
| U-03 (a) OD-C15 keep-outs | Ø8 × 2.0 cylinders at (±110, +90), y 0 … 2.0, `interference ≤ 0` with the panel (they touch the wall's inner face z 94: expected 0 mm³ at zero gap, §7 risk 4) | `interference` | 0.001 mm³ |
| U-03 (b) | the panel moved +40.0 along Y and lowered to its seat in steps of 2.0 (21 poses), OD-C10 and OD-E02 absent: `interference ≤ 0` with OD-C01, OD-C05 and each solid of the OD-G01 assembly at every step; the worst step reported | `interference` (OD-G10 per §7 Q6) | 0.001 mm³ |
| U-04 | write, re-read: `schema`, `solids`, `volume_delta`, `faces_delta`, `labels` (name `od_c09_front`), `valid_after` | `tools.core.step_roundtrip` | per GATES V-03 rows: 0.001 mm³, 0 |
| feature_census / U-05 | counts against §3: 1 wall with 1 brew opening (the opening's 8 side faces, read on a section at z +95.5: one inner loop); 5 ribs; 2 flanges; 4 gussets (inclined planar faces: exactly 4 with normal (0, ±0.47, −0.88) family); bores: 4 × Ø3.4 along Y, 3 × Ø15 along Z, 2 × Ø4.0 blind along Z; 2 convex cylinders Ø11 (bosses; split faces counted by axis); the face count per kind recorded at D5 as the reference | `feature_census`, `bore_census`, `locate_bore` | 0 |
| U-06 (Soft) | `min_wall_wide` ≥ 2.0 | `min_wall_wide` (`detail["wide"]`) | 0.005 mm |
| U-07 | STL at tolerance 0.01 mm, angular 0.2 rad (≤ 0.2066 from R 7.5); `max_sagitta ≤ 0.01`; triangle count recorded | `tools.core.write_stl`, `mesh_sagitta` | 0.005 mm |
| U-08 | N/A by its row (no threads) | — | — |
| D-01a | `min_wall ≥ 0.8` | `min_wall` (spacing 0.4; a face too large for it is INCONCLUSIVE and re-run at the spacing it names) | 0.005 mm |
| D-01b | `min_wall ≥ 2.0` over the whole solid; design readings: wall and ribs 3.0, flanges and gussets 4.0, boss wall 3.5 (3.05 at a relief, §7 Q4), flange-hole webs (≥ 3.0 to the gussets) | `min_wall` | 0.005 mm |
| D-02 | sizes against the A-10 build volume 420 × 420 × 500, lying on the front face: bed 232 × 215, height 25 | `envelope` | 0.005 mm |
| D-03a | least downward angle ≥ 45° with `build_dir = (0, 0, −1)`, the four flange-hole crowns (cylinders Ø3.4 about (x ±85 / ±95, z 77), y 0 … 4) excluded by position and their least angle reported | `overhang_census(build_dir=(0,0,-1))` on the solid, then on the solid with the four hole regions filled for the gated reading | 0.001° |
| D-03b | reviewer, from sections: the flange-hole bridges ≤ 3.4; corroborated by `flat_ceiling_spans(build_dir=(0,0,-1), max_span=5.0)` expected 0 elsewhere | `flat_ceiling_spans` (lead) | 0.005 mm |
| D-04a | each flange hole Ø ≥ 3.25 | `bore_census`, `locate_bore((±85 / ±95, 2.0, 77), (0, 1, 0))` | 0.005 mm |
| D-05a | material across each Ø4.0 bore ≥ 8.0: `radial_extent` outer from the bore axis at 0° … 330° every 30°, at three levels along the bore, `r_min` = 2.0, `r_max` = 7.0; across = r(θ) + r(θ + 180°), least reported | `radial_extent`, `bore_census` | 0.005 mm |
| D-05b | each insert bore Ø 4.0 ± 0.05, depth 6.0 ± 0.1, blind | `bore_census`, `locate_bore(boss end point + 3.0 along the bore, (0, 0, 1))` | 0.005 mm |
| D-06a | `min_wall ≥ 1.0` (the same reading as D-01a) | `min_wall` | 0.005 mm |
| D-07 | N/A by its row | — | — |
| J-05 | wall around each insert bore ≥ 3.0: least `radial_extent` outer − 2.0 over the same grid as D-05a | `radial_extent` (and `min_wall` near the bosses as corroboration) | 0.005 mm |
| E-01 | panel to the posed OD-E02 ≥ 0.5 everywhere except the two boss end faces, as §7 Q7: (i) `clearance(panel without the two bosses, OD-E02)`; (ii) per boss `clearance(boss ∩ {z ≥ end + 0.5}, OD-E02)` gated ≥ 0.5, plus the same at end + 2.0 reported as the lateral gap | `clearance` | 0.005 mm |
| E-05 | each insert bore axis to its posed board hole axis ≤ 0.10 (`locate_bore` on the panel's census at the board hole's axis point) | `bore_census`, `locate_bore` | 0.005 mm |
| E-06 | reviewer from sections: bosses on and tied into the wall; each flange tied by two gussets. Corroboration: each boss and gusset shares its face with the wall in `feature_census` (one solid, U-01) | sections (D6) | — |
| REQ-01 | four Ø3.4 ± 0.1 holes along Y at (±85, 77), (±95, 77), offset ≤ 0.10, length 4.0 ± 0.1, through; underside one plane at y 0.00 ± 0.10 (`envelope` min_y and the planar faces at y 0) | `bore_census`, `locate_bore`, `envelope` | 0.005 mm |
| REQ-02 | outer face z 97.00 ± 0.10 and inner z 94.00 ± 0.10 on sections at y 100 and y 200 (on the left pillar x −100 and the right pillar x +100: `radial_extent`-free line probes along Z through the solid, exact line-solid hits); x ±116.0 ± 0.1 and top y 215.00 ± 0.10 by `envelope` | `envelope`; line probes; sections for the reviewer | 0.005 mm |
| REQ-03 | `interference` of the two opening boxes, each shrunk 0.2 per side, z +93.8 … +97.2, with the panel = 0; edges from the section at z +95.5 ± 0.1 | `interference`; `write_sections` | 0.001 mm³; 0.005 mm |
| REQ-04 | each cap's foremost point (`envelope` max_z of the posed OD-E02 clipped to each cap's box) ≥ 97.5; each button hole coaxial with its cap axis at z 95.5, offset ≤ 0.25 | `envelope`, `bore_census`, `locate_bore` | 0.005 mm |
| REQ-05 (a) | OD-G10 at the locked pose rotated by φ = −55 … +10 every 5° (14 poses): `clearance` to the panel ≥ 2.0 and to OD-E02 ≥ 2.0; worst φ reported | `clearance` | 0.005 mm |
| REQ-05 (b) | OD-G10 rotated −50°, lowered 15.0, carried along +Z from axis z 32 to z 182 every 5.0 (31 poses): `interference ≤ 0` with the panel and with OD-E02 at every pose (OD-G10 per §7 Q6) | `interference` / Q6 fallback | 0.001 mm³ |
| REQ-06 | six Ø6 cylinders along Y: the flange-hole axes y 4.0 … 260.0, the OD-C15 axes (±110, 90) y 2.0 … 260.0: `interference` with the panel = 0 | `interference` | 0.001 mm³ |
| REQ-07 | `envelope` min_z ≥ 72.0; `interference` = 0 of the tray box x ±74.8, y 0 … 49.8, z −15 … +120 and of the knob cylinder Ø32 about (95.5, 140), z 60 … 93.8 | `envelope`, `interference` | 0.005 mm; 0.001 mm³ |
| REQ-08 (Soft) | bench: not geometric; the REPORT states INCONCLUSIVE with a risk rating | — | — |

Sections at D6 (`03_Sections/od_c09_front_v01_<plane>.png`): z 95.5 (opening, button holes), y 100 and y 200 (REQ-02), y 2.0 (flanges, flange holes), x ±85 and ±95 (flange holes, gussets), x −91.0 (bosses, insert bores, board), y 153.2 and y 127.3 (each boss and its board seat), x 36 (handle at the wall), each with the placed reference parts beside the panel where the gate is assembly-side.

Sweep at D7 (`01_CAD/sweep_v01/`): nominal, low, high of every fit-critical row in §4, one at a time for the panel's own dimensions (`win_*`, `slot_*` ±0.1; `flange_hole_d` ±0.1; `flange_hole_xz` ±0.1; `insert_bore_d` ±0.05; `insert_bore_depth` ±0.1; `button_hole_d` ±0.2; `boss_end_z` ±0.1; `boss_d` ±0.1; `wall_z_*`, `wall_top_y` ±0.1); every run builds one solid and passes the same predicates. The REQ-05 travel already sweeps φ and the carry together (L-09); U-03 (b) checks the lowering path from first contact to seat (L-10).

## 7. Risks

Questions and stated derivations the orchestrator must settle before J3. Numbers are D1 measurements on the inputs as posed by §2.

- **Q1 — REQ-04 cannot pass with the §2 pose (spec value contradicted).** The foremost points of the posed caps are B2 z 98.565 (1.57 proud, as the spec says) but **B1 z 95.333 and B3 z 95.345**, 1.67 behind the front face z 97 and 2.17 short of REQ-04's ≥ 97.5. A-04's "B1 and B3 stand proud by more" does not hold: their tops are inclined (normal 20° off the board axis) and lower than B2's. Options: (a) move the OD-E02 pose +Z by 2.5 (origin z 71.85): B1 / B3 at 97.83 (0.83 proud), B2 at 101.07 (4.07 proud), boss ends at 87.985, the board's next-highest part (the cap collars, front at 88.46 → 90.96) still 3.0 behind the wall; (b) amend REQ-04 to B2 only and accept B1 / B3 recessed 1.67 in their Ø15 holes; (c) another pose or a different wall locally (the Usta's choice). J3 cannot meet REQ-04 as written.
- **Q2 — Boss end level (spec value contradicted).** The levels "near z +81.2 and +81.8" are the floors of a Ø6.76 (L) / Ø6.65 (R) pocket in front of each screw hole, 4.30 / 3.67 deep, offset 0.31 / 0.30 from the hole axis. The board is **not flat to Ø11** around either hole: a flat at z 85.485 over 80° … 280° (the −X side), and on the +X side a slope down from 85.48 to 81.2 at r 5.5 (≈ 1 mm per mm). A Ø11 boss ending at 81.19 / 81.82 overlaps the board. Proposed: both boss ends at the flat, z 85.485 (equal on both holes), seating on the −X half-annulus between r 3.4 and 5.5; the +X slope stays clear below. The boss is then 8.5 long (94.0 − 85.485).
- **Q3 — Screw length (A-03).** Head seat: the board's rear counterbores (Ø7.58 / Ø7.48, z 69.35 … 72.266), floor at z 72.266; boss end at 85.485 (Q2): grip 13.22. ISO 7380 M3 × 16 reaches 2.78 into a 5.7 insert (≈ 5 threads); M3 × 20 reaches 6.78, past the 6.0 bore (D-05b) and bottoms out. Proposed M3 × 16 ISO 7380, engagement 2.78; the alternative is an M3 × 18 of another head standard with a head ≤ Ø7.4. The Usta's choice (BOM row).
- **Q4 — Ø11 bosses against the cap collars (E-01).** Measured lateral gap of a full Ø11 boss to OD-E02 (above the seat): L boss 0.049 to the B1 collar (collar r 8.09 about (−94.17, 166.51), centre distance 13.64), R boss 0.287 to the B3 collar; E-01 needs 0.5. Options: (a) keep Ø11 and cut each boss by a cylinder about the collar's axis, radius collar + 0.5, from the boss end to z 88.96: wall to the insert bore there 3.05 (L) / 3.29 (R), J-05 ≥ 3.0 met with 0.05 margin on L; material across the bore ≥ 10.5 (D-05a ≥ 8.0); (b) a Ø10 boss: lateral gap ≥ 0.5 measured, J-05 wall exactly 3.0 (zero margin), a change of §4's Ø11 and U-05's count text. Proposed (a). If Q1 (a) moves the board, the relative geometry is unchanged.
- **Q5 — Button hole size (stated derivation, the brief's open point).** Ø15 suffices for all three: B1 and B3 are elliptical prisms along the board's Z (semi-axes 5.92 × 6.36 per the report) with inclined tops, not tilted bodies; B2 is round r 6.34, its axis 0.9° off Z. With all three holes on the measured axes (§4), the least gap from the wall (with its holes) to the board is 1.136, at B2 on the wall's inner face (−94.69, 146.05, 94.0); with the board moved +2.5 (Q1 a) it is 1.096. Both ≥ 0.5. B2's hole axis at z 95.5 is (−98.991, 139.901), 0.10 from the spec's (−99.0, 140.0): within REQ-04's 0.25. No larger hole is needed.
- **Q6 — Two reference solids are unsound, so `common_volume` refuses them.** OD-G10 (`od_g01_assembly_C1_v03.step` solid 3) and OD-E02 both fail `brep_valid` (BOPAlgo_InvalidCurveOnSurface; OD-G10's pcurve 0.00085 mm off against a 0.00023 limit); BRepCheck alone passes them. Every interference row with them (U-03 (a) pairs, U-03 (b) with OD-G10, REQ-05 (b)) is then INCONCLUSIVE. Proposed fallback, run and reported beside the INCONCLUSIVE row, never instead of it: `clearance` > 0 with `detail["inside"]` false at every pose (no overlap and neither inside the other); or a `ShapeFix`-healed copy of each solid in `01_CAD/` with its SHA-256 and volume change, on which `common_volume` runs. The orchestrator decides which reading may gate.
- **Q7 — How E-01 excludes the two designed contacts (stated derivation).** (i) `clearance(panel minus the two bosses, OD-E02) ≥ 0.5` covers the wall, ribs, flanges and the caps in their holes; (ii) per boss, `clearance(boss ∩ {z ≥ end + 0.5}, OD-E02) ≥ 0.5` reads the lateral gap and the seat plane at 0.5 below (so it can read at most 0.5: a pass at zero margin by construction); the same at end + 2.0 is reported as the true lateral gap. The end face itself is gated by U-03's contact row (`clearance = 0`).
- **Risk 1 — REQ-05 (portafilter travel), derived far enough to know it passes** (`01_CAD/plan_v01/m9_g10_sweep.py`, stand-in panel with the Ø15 holes and the bosses at 85.485, clearance only per Q6). (a) φ −55 … +10 every 5°: least gap to the panel 2.511 at φ +10, at the window's right edge (75.0, 160.3, 97.0); 11.010 at +5, 10.256 at −55 (window's left edge), 12.36 … 14.02 between; to OD-E02 ≥ 28.669 (φ −55). The right-edge gap falls fast past +5° (≈ 1.7 per degree), so the +10° gasket-wear allowance (A-05) is the binding pose: margin 0.51 at nominal, ≈ 0.41 with the window's right edge at its low sweep value. (b) φ −50, lowered 15, carried z 32 → 182 every 5.0: least gap to the panel 11.689 (R1's underside, y 188), never inside; to OD-E02 ≥ 29.915. Both pass on the stand-in; J3 re-measures on the built panel.
- **Risk 2 — housing value in §4**: the spec says the housing's front face ends at z +75.1; its body does, but its flange (y 195 … 205, r 50) reaches z 82.0 like the carrier. The ribs at z 84 keep 8.78 from the housing and 12.0 from the carrier (stand-in panel): no change needed.
- **Risk 3 — U-03 (b) lowering**: on the stand-in, the least gaps on the way down are 2.00 to OD-C05 (at +20) and 2.00 to the housing (at +10): no interference, small margins; OD-G10 per Q6.
- **Risk 4 — zero-margin touches by design**: the OD-C15 keep-out cylinders (r 4 about (±110, 90)) touch the wall's inner face z 94 (interference 0 mm³, gap 0); the OD-C10 skirt stands on the wall's top edge as a line contact (A-07). Both read PASS at zero margin.
- **Risk 5 — A-11 PLA near the group head** and **A-12 stiffness** (REQ-08 Soft) stay open; nothing in this plan changes them.
- **Risk 6 — `min_wall` on a 232 × 215 face** at spacing 0.4 may be refused as undersampled: the check re-runs at the spacing `min_wall` names and reports it (never a silent coarser grid).
- **Fallbacks:** no fillets are planned, so no fillet ladder is needed; if Q4 (a) leaves a sliver at the relief's ends, the relief runs the boss's full length instead (same wall to the bore).
