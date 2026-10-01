# DESIGN_PLAN — od_c05_carrier_v02 (20260930-od-c05-group-head-carrier, concept C4)

Designer: Claude Code, Opus 5.5 · spec version 2.0 · brief WP-05 (J3 with its own plan, build attempt 1 of 2, fix_cycles 3) · written before any geometry (D2)

Versions (D0): Python 3.13.7, build123d 0.11.1, OCP (cadquery-ocp-novtk) 7.9.3.1.1, repository commit d7ea010502a30dd025c5123992847da1b15f3ee3. Input hashes checked against the brief (WP-05 → WP-03): OD-G01 f8865cd1…4407b02 and OD-G04 19b4a140…98d6ad2 match; the v01 plan `01_CAD/DESIGN_PLAN.md` 41b80f84…232eced is unchanged and is not edited.

**Status: two spec-value conflicts with D-03a / D-03b, found at planning (§8, K-3 and K-4), to be measured on the build (D5).** Every other feature and gate row is planned below. The brief says to stop only when a spec value cannot be met; §8 shows that K-3 cannot be met in any of the six axis-aligned orientations, so the build is made, measured, and then stopped (D9) unless the measurement contradicts §8.

## 1. Datum

The spec 2.0 §2 frame, identical to the OD-G01 build v02 STEP so the overlay is the identity. The origin is on the group head axis and z = 0 is the housing's lug top pad plane. That frame is kept because the carrier's only designed contact is the housing's rear face: with the frame unchanged, the contact sits on a measured plane (z −24.94) and the four insert axes on measured points (±44, ±44), with no transform to get wrong. In the machine −Z is up, +Z (the mouth) down, +Y the front, +X the user's right (A-02). The floor is the plane z = +180.06 (A-03). Print frame: on its side, the x = −55 face on the bed, build direction +X (A-13).

The measured input facts of the v01 plan §1 are unchanged (same STEP files, same frame) and are reused, not re-probed: OD-G01 sound (1/1/0), envelope x ±50, y ±50, z −24.94 … +3.30; rear face the plane z −24.94 (normal −Z, 9232.65 mm², R 8 corners about (±42, ±42)); nothing of OD-G01 at z < −24.94; four insert bores Ø4.000 × 5.700 at (±44.0000, ±44.0000); all rear-face openings within r 20.93. OD-G04 as placed (+6.05° about Z, then z −6.82): sound, envelope z −22.940 … −5.730, nothing at z < −24.94, largest radius below the flange z −19.94 r 22.52. RV01 re-measured the same facts independently (its §2, U-03).

## 2. Library and tools (D1)

- Cards read: none. As at v01, nothing in `library/INDEX.md` matches a printed bracket with clearance holes and a window by tag. Finding: nothing matched.
- `tools/` functions reused:
  - `tools.core.validity`: U-01 and `exactly_one_solid`; OD-G01 and OD-G04 before any boolean with them.
  - `tools.core.write_step` (AP242), `compare_step`, `read_step`: D-024 export, U-04, every re-import.
  - `tools.core.write_stl`, `mesh_sagitta`; `tools.measure.mesh_census`: U-07.
  - `tools.measure.envelope`: U-02, `envelope_within_spec`, D-02, REQ-03 (min_z), REQ-05 (max_z), REQ-07 (min_y).
  - `tools.measure.feature_census`, `bore_census`, `locate_bore`: U-05, D-04a, REQ-01, REQ-02, REQ-03 (hole + counterbore length), REQ-05 (foot hole length), REQ-06.
  - `tools.measure.clearance`, `interference` (on `tools.core.common_volume`): U-03, REQ-08.
  - `tools.measure.min_wall` (and `detail["wide"]`): D-01a, D-01b, D-06a, U-06.
  - `tools.measure.overhang_census(build_dir=(1, 0, 0))`: D-03a, with the named-exception faces left out by position (the v01 selector, moved to the twelve bores along Z).
  - `tools.measure.radial_extent`, whole ray, side inner: REQ-04 (RV01 F4).
  - `tools.measure.mass_properties`: reported only (A-12, 1070 kg/m³).
  - `tools.drawing.write_sections` (`nothing_clipped`): D6.
  - `tools.result.gate`: every comparison, band from GATES §0 (0.005 mm, 0.001°, 0.001 mm³, 0 for counts).
- New code needed (job code, in the check script, not the repo): an analytic downward-angle listing per B-rep face (plane normals; cylinder normals over the face's u range), reported beside the census for D-03a because `overhang_census` cannot settle a face at exactly 45° (RV01 F3); a bridge listing for D-03b from the same downward faces. Neither stands in for a gate check on its own: D-03a is gated on the census, the listing corroborates.

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Plate | sketch on the XY plane at z −29.94: rectangle x ±55.0, y −58.0 … +50.0, the two vertices at y +50 filleted R 6.0 (centres (±49.0, 44.0)); extrude +Z 5.0 to z −24.94 | — | §4 C4, REQ-03, U-02 |
| F02 | Wall | box x ±55.0, y −58.0 … −52.0, z −29.94 … +180.06; fused | F01 | §4 C4, REQ-08, U-02 |
| F03 | Foot | box x ±55.0, y −102.0 … −58.0, z +176.06 … +180.06; fused | F02 | §4 C4, REQ-05, REQ-07 |
| F04 | Front gussets ×2 | right triangle in the YZ plane (y −52.0, z −24.94), (y −12.0, z −24.94), (y −52.0, z +15.06), extruded x +51 … +55 and −55 … −51; fused | F01, F02 | §4 C4, E-06, REQ-08 |
| F05 | Rear gussets ×2 | right triangle (y −58.0, z +176.06), (y −98.0, z +176.06), (y −58.0, z +136.06), same x ranges; fused | F02, F03 | §4 C4, E-06 |
| F06 | Hub window | circle R 30.0 about (0, 0) united with the 45° gable toward +X (tangent points (21.2132, ±21.2132), apex (42.4264, 0)); cut through the plate along Z | F01 | §4 C4, REQ-04, D-03a |
| F07 | Housing holes ×4 | Ø3.4 through the plate along Z at (±44.0, ±44.0) | F01 | REQ-01, D-04a |
| F08 | Counterbores ×4 | Ø6.5 × 2.0 from the top face z −29.94 toward +Z, coaxial with F07 | F07 | REQ-02 |
| F09 | Foot holes ×4 | Ø3.4 through the foot along Z at (±35.0, −72.0) and (±35.0, −92.0) | F03 | REQ-06, D-04a |
| F10 | Clean-up | `clean()` to merge coplanar faces, then exactly one solid | F01 … F09 | U-01, U-05 |

No fillet other than the two spec R 6 corners (sketch arcs). No edge goes through a fillet ladder; the REPORT will say so.

Feature census the check compares (U-05, after F10; predicted, confirmed on the build, and any difference reported as a deviation, never edited to match):
- 24 planar faces: side faces x −55 and x +55 (each one face over plate, wall, foot and the two outer gusset faces) 2; plate top z −29.94 1; plate underside z −24.94 1; plate front edge y +50 1; wall front y −52 1; wall and plate rear y −58 1; foot and wall underside z +180.06 1; foot top z +176.06 1; foot rear y −102 1; gusset inner faces |x| 51 4; gusset hypotenuses 4; window gable flats 2; counterbore floors 4.
- 15 cylindrical faces: 13 concave (4 Ø3.4 plate holes, 4 Ø6.5 counterbores, 4 Ø3.4 foot holes, the R 30 window arc of 270°) and 2 convex (the R 6 corners).
- 13 bores: the twelve along Z and the window arc (it spans more than 180°).
- no cone, sphere, torus, B-spline or other face.

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| z_top | −29.94 | mm | ± 0.10 (REQ-03) | §4 C4, REQ-03 | no (follows z_contact and plate_t) |
| z_contact | −24.94 | mm | ± 0.10 (REQ-03) | §4 C4, A-01; measured OD-G01 rear face −24.94 | no: the designed contact plane; moving it breaks U-03 by definition |
| plate_t | 5.0 | mm | — | §4 C4 | no |
| half_x | 55.0 | mm | U-02 ± 0.1 | §4 C4 | no |
| y_front | +50.0 | mm | U-02 ± 0.1 | §4 C4 | no |
| corner_r | 6.0 about (±49.0, 44.0) | mm | — | §4 C4 | no; see conflict K-4 |
| hole_d | 3.4 | mm | ± 0.1 (REQ-01) | §4 C4, REQ-01 | yes: 3.3 / 3.4 / 3.5 |
| hole_xy | ±44.0 | mm | offset ≤ 0.10 (REQ-01) | §4 C4; measured OD-G01 inserts (±44.0000, ±44.0000) | yes: 43.95 / 44.00 / 44.05 (all four together) |
| cb_d | 6.5 | mm | ± 0.1 (REQ-02) | §4 C4, A-09 | yes: 6.4 / 6.5 / 6.6 |
| cb_depth | 2.0 | mm | ± 0.1 (REQ-02) | §4 C4, A-09 | yes: 1.9 / 2.0 / 2.1 |
| hub_r | 30.0 | mm | ≥ 30.0 (REQ-04) | §4 C4, A-06 | yes: 30.0 / 30.1 (one-sided: REQ-04 is a floor) |
| hub_apex_x | 42.43 | mm | — | derivation: hub_r·√2 (45° gable toward +X) | no (follows hub_r) |
| wall_y | −58.0 … −52.0 | mm | front ≥ 2.0 from the housing (REQ-08) | §4 C4 | yes, front face one-sided: −52.0 / −52.1 (REQ-08's 2.0 is met with margin 0 at nominal) |
| z_floor | +180.06 | mm | ± 0.10 (REQ-05) | §4 C4, A-03 | no (the floor datum) |
| foot_t | 4.0 | mm | ± 0.1 (REQ-05) | §4 C4, REQ-05 | yes: 3.9 / 4.0 / 4.1 (underside fixed at +180.06) |
| foot_y_rear | −102.0 | mm | min_y ≥ −102.0 (REQ-07) | §4 C4, REQ-07, A-05 | yes, one-sided: −102.0 / −101.9 (nothing beyond −102.0) |
| foot_hole_d | 3.4 | mm | ± 0.1 (REQ-06) | §4 C4, A-04 | yes: 3.3 / 3.4 / 3.5 |
| foot_hole_x | ±35.0 | mm | offset ≤ 0.10 (REQ-06) | §4 C4, A-04 | yes: 34.95 / 35.00 / 35.05 |
| foot_hole_y | −72.0, −92.0 | mm | offset ≤ 0.10 (REQ-06) | §4 C4, A-04 | yes: ± 0.05 together |
| gusset_x_in | 51.0 (gussets |x| 51 … 55) | mm | ≥ 1.0 from the housing (REQ-08) | §4 C4 | yes, one-sided: 51.0 / 51.1 (REQ-08's 1.0 is met with margin 0 at nominal) |
| gusset_t | 4.0 | mm | — | §4 C4 (follows half_x − gusset_x_in) | no |
| gusset_leg | 40.0 (both legs, 45° hypotenuse) | mm | — | §4 C4 | no |
| stl_tol | 0.01 | mm | — | U-07 | no |
| stl_ang | 0.20 | rad | ≤ 4·acos(1 − 0.01/6.0) = 0.2310 | derivation from U-07: a round figure below the limit (as v01) | no |
| density | 1070 | kg/m³ | — | §3, A-12 (reported only) | no |

## 5. Placements

Unchanged from the v01 plan §5 (the housing frame is the same; only the up direction changed).

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-G01 housing build v02 | `00_Spec/inputs/OD-G01_housing_C1_v02.step` (f8865cd1…4407b02) | its rear face (plane z −24.94, normal −Z) and its four insert bore axes (±44.0000, ±44.0000), measured | RigidJoint at the identity, checked, not assumed: `locate_bore` on both solids and `clearance` = 0 at the face | the plate's underside z −24.94 (designed contact, A-01); the four Ø3.4 holes coaxial with the insert bores |
| OD-G04 gasket support | `00_Spec/inputs/OD-G04_brewing_gasket_support.step` (19b4a140…98d6ad2) | its plate back face (z = 0.000) and tab 1, per the OD-G01 REPORT v02 §5 | rotate +6.05° about Z, then translate z −6.82 | none: `clearance` ≥ 2.0 (U-03) |
| OD-H11 thermoblock | `00_Spec/inputs/OD-H11_thermoblock.step` | — | not placed (A-05, REQ-07) | none |

The check assembly STEP holds `od_c05_carrier`, `od_g01_housing`, `od_g04_brewing_gasket_support` as placed.

## 6. Checks planned (D3)

`01_CAD/check_od_c05_carrier_v02.py` re-imports the exported STEP and gates every row through `tools.result.gate` with the GATES §0 band. A raised exception or a missing value is INCONCLUSIVE.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | solid_count == 1 | `validity` | 0 |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | `validity` | 0 |
| U-02 / envelope_within_spec | size 110.0 × 152.0 × 210.0 each ± 0.1; position reported apart: x ±55.0, y −102.0 … +50.0, z −29.94 … +180.06 | `envelope` | 0.005 mm |
| U-03 (a) carrier\|OD-G01 | contact clearance == 0 (at z −24.94); interference ≤ 0; hole axes to the insert bore axes ≤ 0.10 | `clearance`, `interference`, `bore_census` + `locate_bore` on both solids | 0.005 mm, 0.001 mm³ |
| U-03 (a) carrier\|OD-G04 | clearance ≥ 2.0 with nearest points; interference ≤ 0 | `clearance`, `interference` | 0.005 mm, 0.001 mm³ |
| U-03 (b) | N/A: no motion variable | — | — |
| U-04 | round trip: schema, 1 solid, volume delta 0, faces delta 0, valid after, label `od_c05_carrier` | `compare_step`, `read_step` | 0.001 mm³, 0 |
| U-05 / feature_census | §3 counts (24 / 15 / 13 / 2 / 13); the twelve bores located one by one | `feature_census`, `bore_census`, `locate_bore` | 0 |
| U-06 (Soft) | wide wall ≥ 2.0 | `min_wall` `detail["wide"]` | 0.005 mm |
| U-07 | STL tol 0.01, angular 0.20 (≤ 0.2310); sagitta ≤ 0.01; one body, 0 naked edges, winding 1; triangle count, volume and bounding box reported for the orchestrator's 3MF | `write_stl`, `mesh_sagitta`, `mesh_census` | 0.005 mm |
| U-08 | N/A: no threads | — | — |
| D-01a / D-01b / D-06a | min_wall ≥ 0.8 / ≥ 2.0 / ≥ 1.0 | `min_wall` | 0.005 mm |
| D-02 | 152.0 × 210.0 on the bed (y, z) ≤ 220 × 220, 110.0 tall (x) ≤ 250 | `envelope` | 0.005 mm; A-08 |
| D-03a | least downward angle off the bed ≥ 45°, build direction +X, the twelve bore faces along Z left out by position and their least reported apart; the analytic per-face listing beside it (gable 45.000°) | `overhang_census(build_dir=(1, 0, 0))`; analytic listing | 0.001°; A-13 |
| D-03b | bridges ≤ 5 outside the named exception; crowns ≤ 6.6 inside it | downward-face listing (horizontal faces and their span) and bore diameters; reviewer from sections | 0.005 mm |
| D-04a | all eight Ø3.4 holes Ø ≥ 3.25 | `locate_bore` | 0.005 mm |
| D-07 | N/A: no fit bores | — | — |
| E-06 | four gussets fused into the one solid (four inner faces at |x| 51, each gusset's volume 3200 mm³ by `common_volume` with its box) | face selection by position, `common_volume` | 0.001 mm³ |
| REQ-01 | four Ø3.4 ± 0.1 through along Z at (±44, ±44), offset ≤ 0.10 from nominal and from the OD-G01 insert bores in the check assembly | `bore_census` + `locate_bore` (point z −26.44) on both solids | 0.005 mm; A-01 |
| REQ-02 | four Ø6.5 ± 0.1, depth 2.0 ± 0.1, open at z −29.94, coaxial ≤ 0.10 | `bore_census` + `locate_bore` (point z −29.44) | 0.005 mm; A-09 |
| REQ-03 | top face z −29.94 ± 0.10 (`envelope` min_z and the counterbores' open end); underside z −24.94 ± 0.10 (counterbore start + hole + counterbore lengths = 5.0) | `envelope`, `locate_bore` | 0.005 mm; A-01 |
| REQ-04 | innermost material on the whole ray ≥ 30.0 at every 10° on five levels z −29.9, −29.44, −27.44, −25.44, −24.98 (180 rays); θ 0° reads 42.43 (apex), θ 90° reads 30.0 | `radial_extent(side="inner")`, no r_max | 0.005 mm; A-06 |
| REQ-05 | underside z +180.06 ± 0.10 (`envelope` max_z); thickness 4.0 ± 0.1 (length of each foot hole) | `envelope`, `locate_bore` | 0.005 mm; A-03, A-04 |
| REQ-06 | four Ø3.4 ± 0.1 through along Z at (±35, −72 / −92), offset ≤ 0.10 | `bore_census` + `locate_bore` (point z +178.06) | 0.005 mm; A-04 |
| REQ-07 | `envelope` min_y ≥ −102.0 | `envelope` | 0.005 mm; A-05 |
| REQ-08 | the housing against the carrier's front gussets (the carrier ∩ {y > −52, z > −24.94}) ≥ 1.0 and against the wall part (the carrier ∩ {y < −52, z > −24.94}) ≥ 2.0, nearest points reported; the plate contact reported apart under U-03 | `clearance` on the parts cut by position from the re-imported STEP | 0.005 mm; A-01 |
| REQ-09 | **Soft bench gate**: INCONCLUSIVE with a risk rating, answered by the first print; the geometry (cantilever 96 to the front screws, wall 6.0, four gussets) reported (RV01 F2) | — (bench) | A-11 |

Sweep (D7): every fit-critical row of §4 at its low, nominal and high rung (one-sided where marked), exported into `01_CAD/sweep_v02/`, each run through the same predicates; worst margin per gate reported.

Sections (D6), from the exported STEP, into `03_Sections/` with `_v02`: y = 0 (the L profile: plate, wall, foot, gussets); x = 0 (window, plate over the housing); x = 44 (holes and counterbores); x = 53 (a gusset pair); z = −27.44 (plate plan: gable, holes); z = +178 (foot holes); assembly y = 0 and x = 0 with OD-G01 and OD-G04.

## 7. Risks

- **K-3 and K-4 (D-03a, D-03b):** §8. Predicted from the geometry; the build measures them.
- **REQ-08 at margin 0 by construction:** the gussets at |x| 51 clear the housing's sides at |x| 50 by exactly 1.0 and the wall at y −52 its rear side at y −50 by exactly 2.0; the band absorbs float noise only. The one-sided sweep rungs show the direction.
- **D-03a at exactly 45°:** the gable flats are 45.000° by construction and the R 30 arc is tangent to them; `overhang_census` may read INCONCLUSIVE at the tangent line (RV01 F3). The analytic listing is reported beside it; an INCONCLUSIVE census is never reported as PASS.
- **U-03 coplanar boolean:** the plate's underside and the housing's rear face are coplanar; `common_volume` read 0.000 cleanly at v01 on the same faces. If INCONCLUSIVE, it is reported as such.
- **Feature census counts** are predicted: OCCT may split the side faces or the window arc at a seam, or `clean` may leave coplanar faces apart. Any difference is a reported deviation with its cause.
- **Sharp inside corners** at the plate-wall and wall-foot roots: no fillet is specified; the gussets carry the moment (A-11, REQ-09 Soft). Not changed without a spec amendment.

## 8. Conflicts

**K-3: D-03a and D-03b cannot be met by the two gussets at x +51 … +55 in the spec's print orientation.** A gusset is a prism along X, but the two on the +X side start at x = +51 in open air: nothing of the carrier lies at x < +51 under their triangles (the front pair's space is the housing's side gap, the rear pair's is above the foot top). Their inner faces at x = +51 have the outward normal −X, which with build direction +X points straight at the bed: a downward face at 0° from horizontal (D-03a ≥ 45°), each a 40 × 40 right triangle (800 mm²) carried only along its two legs (plate underside and wall front face; foot top and wall rear face), so a bridge of up to 56.57 along the hypotenuse direction (D-03b ≤ 5). The −X pair's inner faces at x = −51 face up and are fine. Every axis-aligned orientation was checked against the spec geometry:
- +X (spec): the +X gussets' inner faces, 0°.
- −X (x = +55 on the bed): the −X gussets' inner faces, 0° (mirror image).
- +Z (plate top on the bed): the foot's top face z +176.06 faces the bed, a 44 × 110 shelf held only by the two rear gussets, 0°.
- −Z (foot on the bed): the plate's underside z −24.94 faces the bed, 108 × 110 cantilevered from the wall, 0°.
- +Y (foot rear edge on the bed): the wall's rear face y −58 above the foot, 110 × 166, 0°.
- −Y (plate front edge on the bed): the wall's front face y −52 below the plate, 110 × 205, 0°.
Options for the Usta (none taken by the designer):
  1. Extend the named exception (D-03a, D-03b) to the two +X gusset inner faces, bridged by the slicer between their two carried legs (sag of the first layers expected; the faces are 1.0 from the housing's sides at the front pair).
  2. Allow slicer support under those two faces only (a support column from the bed at x −55 up to x +51, about 106 tall, inside the housing's side gap and over the foot); changes "nothing supported" in D-03a.
  3. A concept change (Oğuz, a new spec value): side walls or ribs that start on the bed side, for example the +X gussets replaced by a 45° rib under the plate and behind the wall whose downward face is the hypotenuse in the print, or the carrier printed in two parts.

**K-4: D-03a cannot be met by the front corner R 6.0 about (−49.0, 44.0) in the spec's print orientation.** It is a convex round next to the bed face x = −55. Its outward normal turns from −X (straight down) at the bed line to +Y, so its lower half faces down at angles from 0° to 45° over the first 1.76 of print height (x −55.00 … −53.24), overhanging up to 4.24 in +Y past the first layer. `overhang_census` leaves out only the samples within 0.01 of the bed, so the least off the bed is predicted near 3.3°. The corner about (+49.0, 44.0) faces up and is fine. Options:
  1. The −X corner (or both, for symmetry) becomes a 45° chamfer 6 × 6, or an R 6 arc with a 45° tangent flat to the bed face (a teardrop corner); changes §4 C4.
  2. Extend the named exception to that corner (a small overhang at the bed, printed with a slight droop).
  3. Square front corners (the housing's R 8 corners stay inside the plate's outline either way).

**K-5 (text, no stop): spec §5 D-03a's check column reads `overhang_census(build_dir=(0,1,0))`, left from spec 1.x.** The same row's threshold, §4 and A-13 say build direction +X, as does the brief. The check uses `build_dir=(1, 0, 0)`; the (0, 1, 0) reading is not a gate for this concept (it would read the wall's rear face at 0°, the ±Y case above).
