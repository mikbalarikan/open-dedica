# DESIGN_PLAN — od_c05_carrier_v01 (20260930-od-c05-group-head-carrier, concept C1)

Designer: Claude Code, Opus 5.5 · spec version 1.0 · brief WP-02 (J2, attempt 1 of 2) · written before any geometry (D2)

Versions (D0): Python 3.13.7, build123d 0.11.1, OCP (cadquery-ocp-novtk) 7.9.3.1.1, repository commit d7ea010502a30dd025c5123992847da1b15f3ee3. Input hashes checked against the brief: all five match (OD-G01 f8865cd1…, OD-G04 19b4a140…, OD-H11 e2d186f2…, REPORT_v02 02ee81de…, DESIGN_SPEC_v1.3 55841f6b…); INTAKE_v01 hashes b6b190cb…c5118d5b.

**Status: two spec-value conflicts, measured on probe coupons, stop the J3 build until answered (§8).** Every other feature and gate row is planned below.

## 1. Datum

The spec §2 frame, identical to the OD-G01 build v02 STEP so the overlay is the identity. The origin is on the group head axis and z = 0 is the housing's lug top pad plane because the carrier's only designed contact is the housing's rear face: taking the housing's frame unchanged puts that contact at a measured plane (z −24.94) and the four insert axes at measured points (±44, ±44), with no transform to get wrong. +Z toward the user, +Y up in the machine (A-02), θ counter-clockwise about +Z from +X. Print frame: the foot underside y = −150.0 on the bed, build direction +Y (A-13).

Measured on the inputs (probe `01_CAD/probe/probe_inputs_v01.py`, results `probe_inputs_v01.json`, `probe_g04_hub_v01.json`):

| Fact | Measured | Expected | Note |
|---|---|---|---|
| OD-G01 `validity` | solid_count 1, brep_valid 1, naked_edges 0 | sound | U-03's boolean may run on it |
| OD-G01 envelope | 100.0 × 100.0 × 28.24; x ±50.0, y ±50.0, z −24.94 … +3.30 | A-01 | |
| OD-G01 rear face | one planar face, normal −Z, z = −24.94, area 9232.6476 mm², 7 openings; outline 100 × 100 with four R 8.00 arcs centred (±42.0, ±42.0) | A-01 | the carrier's front face is a full-face contact |
| OD-G01 material behind z −24.94 | 0.000 mm³ | nothing | nothing protrudes behind the rear face |
| OD-G01 insert bores | four Ø4.000 along +Z at (±44.0000, ±44.0000), offset 0.000, from z −24.94 (open on the rear face) to −19.24, length 5.700 | Ø4.0 × 5.7 | `bore_census` reads them through because they open into the boss top above the floor |
| OD-G01 hub opening | Ø26.000 on the axis, offset 0.000, through, z −24.94 … −19.94; on the rear face it merges with the two pair-A Ø9.0 lobes (r 15.50) into one keyhole opening 40.0 × 26.0 reaching r 20.00 | Ø26 | |
| OD-G01 pair-B holes on the rear face | Ø3.800 at r 19.03 (centres (10.6414, −15.7766), (−9.3129, 16.5955)), reaching r 20.93 | r 19.03 | the OEM screw heads bear on the rear face here, inside the R 30 window |
| Largest opening radius on the rear face | 20.93 | ≤ 30 | all openings lie inside the hub window |
| OD-G04 `validity` | solid_count 1, brep_valid 1, naked_edges 0 | sound | |
| OD-G04 own frame | plate back face z = 0.000 (largest +Z plane, 1154.161 mm²); envelope z −16.12 … +1.09 | X-33, X-34 | |
| OD-G04 as placed (+6.05° about Z, then z −6.82) | envelope z −22.940 … −5.730; hub tube OD 20.06 (r 10.03 at 36 angles), ID 16.76, bottom z −22.550 (a torus end); pair A bottoms z −22.94 (r 12.01 … 18.99); pair B bottoms z −21.70; largest radius of any OD-G04 material below the floor z −19.94: r 22.52 (θ 304°) | X-35 … X-38 | agrees with the OD-G01 REPORT v02 §5 |
| OD-G04 material behind z −24.94 | 0.000 mm³ | nothing | the r ≤ 30 window has nothing of OD-G04 to clear behind the rear face |
| Pre-build estimate, placed OD-G04 to a probe slab z −29.94 … −24.94 with an R 30 window | 5.000 mm, at OD-G04's flange bottom (30.43, 3.23, −19.94) | U-03 ≥ 2.0 | an estimate on a probe body, not a gate; margin expected +3.0 |
| Pre-build estimate, OD-G01 to the same probe slab | clearance 0.000, common volume 0.000 mm³ | U-03 contact | estimate only |

## 2. Library and tools (D1)

- Cards read: none. Nothing in `library/INDEX.md` matches a printed bracket with clearance holes and windows by tag; the nearest (UNO10 U5, heat-set boss) is about the insert side, which is the housing's, not this part's. Finding: nothing matched.
- `tools/` functions reused:
  - `tools.core.validity`: U-01 on the carrier, and on OD-G01 and OD-G04 before any boolean with them.
  - `tools.core.write_step` / `step_roundtrip`: the AP242 part and assembly STEP (D-024), U-04.
  - `tools.core.read_step`: every check re-imports the exported STEP.
  - `tools.core.write_stl`, `mesh_sagitta`: U-07.
  - `tools.core.common_volume` via `tools.measure.interference`: U-03 interference.
  - `tools.measure.clearance`: U-03 contact (= 0) and OD-G04 clearance (≥ 2.0), with nearest points.
  - `tools.measure.bore_census`, `locate_bore`: U-05, D-04a, REQ-01, REQ-02, REQ-03 (rear face from the counterbore start), REQ-05 (foot thickness from the Y-hole length), REQ-06.
  - `tools.measure.feature_census`: U-05.
  - `tools.measure.envelope`: U-02, D-02, REQ-03, REQ-05, REQ-07.
  - `tools.measure.min_wall` (and `detail["wide"]`): D-01a, D-01b, D-06a, U-06.
  - `tools.measure.overhang_census(build_dir=(0, 1, 0))`: D-03a.
  - `tools.measure.radial_extent`: REQ-04, REQ-08 and their positive controls.
  - `tools.measure.mass_properties`: reported only (A-12 density 1070).
  - `tools.drawing.write_sections`, `nothing_clipped`: D6 sections.
  - `tools.result.gate`: every comparison, band from GATES §0 (0.005 mm, 0.001°, 0.001 mm³, 0 for counts).
- New code needed: none for the gates. The OD-G04 placement is a build123d rotate and translate in the assembly script from the REPORT's measured joint.

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Wall | sketch on the XY plane at z −29.94: rectangle x ±50, y −150.0 … +50.0 with the two top corners R 8.0 (centres (±42, 42)); extrude +Z 5.0 to z −24.94 | — | §4 C1, REQ-03, U-02 |
| F02 | Foot | box x ±50, y −150.0 … −146.0, z −69.94 … −24.94, fused to F01 (its front strip coplanar with the wall front, merged by `clean`) | F01 | §4 C1, REQ-05, REQ-07, U-05 |
| F03 | Gussets ×2 | right-triangle sketch in the YZ plane, vertices (y −146.0, z −29.94), (y −106.0, z −29.94), (y −146.0, z −69.94); extruded x +46.0 … +50.0 and −50.0 … −46.0; fused | F01, F02 | §4 C1, E-06, U-05 |
| F04 | Hub window | cut through the wall along Z: circle R 30.0 about (0, 0) united with the 45° gable (tangent lines at θ 45° and 135° meeting at the apex (0, 42.43)) | F01 | §4 C1, REQ-04, D-03a, U-05 |
| F05 | Lower window | the same profile, R 25.0 about (0, −95.0), apex (0, −59.64); cut through the wall along Z | F01 | §4 C1, REQ-08, D-03a, U-05 |
| F06 | Housing holes ×4 | Ø3.4 through the wall along Z at (±44.0, ±44.0) | F01 | REQ-01, D-04a, U-05 |
| F07 | Counterbores ×4 | Ø6.5 × 2.0 from the rear face z −29.94 toward +Z, coaxial with F06 | F06 | REQ-02, U-05 |
| F08 | Frame holes ×4 | Ø3.4 through the foot along Y at (x ±35.0, z −40.0) and (x ±35.0, z −60.0) | F02 | REQ-06, D-04a, U-05 |
| F09 | Clean-up | `clean()` to merge coplanar faces, then `exactly_one_solid` | F01 … F08 | U-01, U-05 |

No fillet other than the two spec R 8 corners (which are sketch arcs, not a ladder). No edge is filleted by `fillet_ladder`; the REPORT will say so.

Feature census the check compares (U-05, after F09; to be confirmed on the first build and any difference reported as a deviation): 20 planar faces (front 1, rear 1, top 1, sides 2, foot top 1, foot underside 1, foot rear 1, gusset inner faces 2, gusset hypotenuses 2, window gable flats 4, counterbore floors 4); 16 cylindrical faces, 14 concave (4 Ø3.4 along Z, 4 Ø6.5, 4 Ø3.4 along Y, the R 30 and R 25 window arcs, each 270°) and 2 convex (the R 8 corners); 14 bores (the 12 holes and counterbores, and the two window arcs, which span more than 180°).

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| z_front | −24.94 | mm | ± 0.10 (REQ-03) | §4 C1, A-01; measured OD-G01 rear face −24.94 | yes: sweep −24.94 only (a contact plane; moving it breaks U-03 by definition), reported |
| wall_t | 5.0 | mm | — | §4 C1 | no |
| z_rear | −29.94 | mm | ± 0.10 (REQ-03) | derivation: z_front − wall_t | yes (follows wall_t) |
| wall_x | ±50.0 | mm | U-02 ± 0.1 | §4 C1 | no |
| y_top | +50.0 | mm | U-02 ± 0.1 | §4 C1 | no |
| y_floor | −150.0 | mm | ± 0.10 (REQ-05) | §4 C1, A-03 | no (datum of the bed) |
| corner_r | 8.0 | mm | — | §4 C1, INTAKE X-04; measured OD-G01 R 8.00 at (±42, ±42) | no; see conflict K-1 |
| hole_d (along Z) | 3.4 | mm | ± 0.1 (REQ-01) | §4 C1, REQ-01 | yes: 3.3 / 3.4 / 3.5 |
| hole_xy | ±44.0 | mm | offset ≤ 0.10 (REQ-01) | §4 C1; measured OD-G01 inserts (±44.0000, ±44.0000) | yes: 43.95 / 44.00 / 44.05 (all four together) |
| cb_d | 6.5 | mm | ± 0.1 (REQ-02) | §4 C1, A-09 (head Ø5.7 ISO 7380 or Ø5.5 DIN 912) | yes: 6.4 / 6.5 / 6.6 |
| cb_depth | 2.0 | mm | ± 0.1 (REQ-02) | §4 C1, A-09 (3.0 of wall under the head; 8 − 3.0 = 5.0 into the 5.7 insert) | yes: 1.9 / 2.0 / 2.1 |
| hub_r | 30.0 | mm | ≥ 30.0 (REQ-04) | §4 C1, A-06 | yes: 30.0 / 30.1 (one-sided: REQ-04 is a floor, so a low rung below 30.0 fails by definition and is not swept) |
| hub_apex_y | 42.43 | mm | — | derivation: hub_r·√2 (45° gable) | no (follows hub_r) |
| low_r | 25.0 | mm | ≥ 25.0 (REQ-08) | §4 C1, A-07 | yes: 25.0 / 25.1 (one-sided, as hub_r) |
| low_c_y | −95.0 | mm | — | §4 C1, A-07 | no |
| low_apex_y | −59.64 | mm | — | derivation: low_c_y + low_r·√2 | no |
| foot_t | 4.0 | mm | ± 0.1 (REQ-05) | §4 C1, REQ-05 | yes: 3.9 / 4.0 / 4.1 (underside fixed at −150.0) |
| foot_z | −24.94 … −69.94 | mm | min_z ≥ −70.0 (REQ-07) | §4 C1, REQ-07, A-05 | yes: rear edge −69.94 / −69.99 (high end at the REQ-07 limit side; nothing beyond −70.0) |
| foot_hole_d | 3.4 | mm | ± 0.1 (REQ-06) | §4 C1, A-04 | yes: 3.3 / 3.4 / 3.5 |
| foot_hole_x | ±35.0 | mm | offset ≤ 0.10 (REQ-06) | §4 C1, A-04 | yes: 34.95 / 35.00 / 35.05 |
| foot_hole_z | −40.0, −60.0 | mm | offset ≤ 0.10 (REQ-06) | §4 C1, A-04 | yes: ± 0.05 together |
| gusset_t | 4.0 (x ±46 … ±50) | mm | — | §4 C1 | no |
| gusset_leg | 40.0 (both legs, 45° hypotenuse) | mm | — | §4 C1 | no |
| stl_tol | 0.01 | mm | — | U-07 | no |
| stl_ang | 0.20 | rad | ≤ 4·acos(1 − 0.01/6.0) = 0.2310 | derivation from U-07: a round figure below the limit | no |
| density | 1070 | kg/m³ | — | §3, A-12 (reported only) | no |

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-G01 housing build v02 | `00_Spec/inputs/OD-G01_housing_C1_v02.step` (f8865cd1…4407b02) | its rear face (plane z −24.94, normal −Z, measured) and its four insert bore axes (measured at (±44.0000, ±44.0000)); the identity pose by the spec §2 frame | RigidJoint at the identity; checked, not assumed: `locate_bore` on both solids and `clearance` = 0 at the face | the wall's front face z −24.94 (designed full-face contact, A-01); the four Ø3.4 holes coaxial with the insert bores |
| OD-G04 gasket support | `00_Spec/inputs/OD-G04_brewing_gasket_support.step` (19b4a140…98d6ad2) | its own plate back face (z = 0.000, measured) and tab 1 per the OD-G01 REPORT v02 §5 (its own −3.3°) | rotate +6.05° about Z, then translate z −6.82 (OD-G01 REPORT v02 §5, OD-G01 spec A-12, A-13); read back: envelope z −22.940 … −5.730, hub bottom −22.550 | none: no carrier contact; `clearance` ≥ 2.0 (U-03) |
| OD-H11 thermoblock | `00_Spec/inputs/OD-H11_thermoblock.step` | — | not placed (A-05, REQ-07) | none |

The check assembly STEP holds `od_c05_carrier`, `od_g01_housing`, `od_g04_brewing_gasket_support` as placed.

## 6. Checks planned (D3)

`01_CAD/check_od_c05_carrier.py` re-imports the exported STEP and gates every row through `tools.result.gate` with the GATES §0 band (mm 0.005, degrees 0.001, mm³ 0.001, counts 0). A raised exception or a missing value is INCONCLUSIVE.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | solid_count == 1 | `tools.core.validity` | 0 |
| U-01 | solid_count = 1, brep_valid = 1, naked_edges = 0 | `validity` | 0 |
| U-02 / envelope_within_spec | size_x, size_y, size_z each in [100.0, 200.0, 45.0] ± 0.1; position (min/max x, y, z) reported apart against x ±50.0, y −150.0 … +50.0, z −69.94 … −24.94 | `envelope` | 0.005 mm |
| U-03 (a) carrier\|OD-G01 | clearance == 0 at the rear face; interference ≤ 0 mm³; four carrier holes coaxial with the insert bores (offset between the two measured axes ≤ 0.10); `validity` of OD-G01 read first (measured sound, so the boolean is admissible) | `clearance`, `interference`, `bore_census` + `locate_bore` on both solids | 0.005 mm, 0.001 mm³ |
| U-03 (a) carrier\|OD-G04 | clearance ≥ 2.0 with nearest points reported; interference ≤ 0 mm³; OD-G04 `validity` read first (sound) | `clearance`, `interference` | 0.005 mm, 0.001 mm³ |
| U-03 (b) | N/A: no motion variable | — | — |
| U-04 | STEP round trip: volume delta 0, faces delta 0, valid after, name `od_c05_carrier` kept | `step_roundtrip` / `compare_step` | 0.001 mm³, 0 |
| U-05 / feature_census | 1 wall, 1 foot, 2 gussets, 2 windows (per §3 face counts: 20 planar, 16 cylindrical, 14 concave, 2 convex, 14 bores); 4 Ø3.4 through along Z, 4 Ø6.5 counterbores, 4 Ø3.4 through along Y located one by one | `feature_census`, `bore_census`, `locate_bore` | 0 (counts) |
| U-06 (Soft) | 45° wall ≥ 2.0 | `min_wall` `detail["wide"]` wrapped as a Result | 0.005 mm |
| U-07 | STL at tol 0.01, angular 0.20 rad (≤ 0.2310); `max_sagitta` ≤ 0.01; 3MF from the same mesh (triangle count equal) | `write_stl`, `mesh_sagitta` | 0.005 mm |
| U-08 | N/A: no threads | — | — |
| D-01a | min_wall ≥ 0.8 | `min_wall` | 0.005 mm |
| D-01b | min_wall ≥ 2.0 | `min_wall` | 0.005 mm |
| D-02 | 100.0 × 45.0 on the bed and 200.0 tall within 220 × 220 × 250 | `envelope` | 0.005 mm; PASS_ASSUMED A-08 |
| D-03a | least downward angle ≥ 45° with build direction +Y | `overhang_census(build_dir=(0, 1, 0))` | 0.001°; A-13 |
| D-03b | bridges ≤ 5, with the named exception (hole and counterbore crowns ≤ 6.5) | reviewer, from sections through the holes and windows | — |
| D-04a | all eight Ø3.4 holes Ø ≥ 3.25 | `locate_bore` | 0.005 mm |
| D-06a | min feature ≥ 1.0 | `min_wall` | 0.005 mm |
| D-07 | N/A: no fit bores | — | — |
| E-06 | the wall tied to the foot by two gussets; no free boss | reviewer, from sections (plane x = 48) | — |
| REQ-01 | four Ø3.4 ± 0.1 through along Z at (±44.0, ±44.0), offset ≤ 0.10 from the OD-G01 insert bores measured in the check assembly | `bore_census` + `locate_bore` on both solids (point z −26.44 inside the Ø3.4 segment) | 0.005 mm; A-01 |
| REQ-02 | four Ø6.5 ± 0.1 counterbores, depth 2.0 ± 0.1 (bore length), start at z −29.94, coaxial with REQ-01 | `bore_census` + `locate_bore` (point z −28.94) | 0.005 mm; A-09 |
| REQ-03 | front face z −24.94 ± 0.10 (`envelope` max_z); rear face z −29.94 ± 0.10 (the counterbores' start point z, and Ø3.4 + counterbore lengths summing 5.0) | `envelope`, `locate_bore` | 0.005 mm; A-01 |
| REQ-04 | r ≤ 30.0 empty over the wall: `radial_extent(axis (0,0,0), dir +Z, ref +X, r_max 30.0)` at every 10° at z −29.5, −27.44, −25.4 reads INCONCLUSIVE "no material" (the expected reading, recorded as such); positive control on the whole ray at θ 90°, z −27.44, side inner: first material 42.43 (gable apex); a second control at θ 0°: 30.0 | `radial_extent` | 0.005 mm; A-06 |
| REQ-05 | foot underside y −150.00 ± 0.10 (`envelope` min_y); thickness 4.0 ± 0.1 (length of each Y hole) | `envelope`, `locate_bore` | 0.005 mm; A-03, A-04 |
| REQ-06 | four Ø3.4 ± 0.1 through along Y at (±35.0, z −40.0 / −60.0), offset ≤ 0.10 | `bore_census` + `locate_bore` (point y −148.0) | 0.005 mm; A-04 |
| REQ-07 | `envelope` min_z ≥ −70.0 | `envelope` | 0.005 mm; A-05 |
| REQ-08 | `radial_extent` about (0, −95.0), dir +Z, r_max 25.0, every 10°, z −29.5, −27.44, −25.4: "no material"; positive controls θ 90° inner = 35.36 (apex), θ 270° inner = 25.0; "nothing else missing below y −50" from the feature census (no extra bore or face) and the reviewer's section | `radial_extent`, `feature_census` | 0.005 mm; A-07 |
| REQ-09 | **Soft bench gate**: not geometric; reported INCONCLUSIVE with a risk rating, answered by the first print | — (bench) | A-11 |

Sweep (D7): every fit-critical row of §4 at its low, nominal and high rung, exported to `01_CAD/sweep_v01/`, each run through all the predicates above; worst margin per gate reported.

Sections (D6): x = 0 (both windows, the foot), y = 44 (the two upper holes and counterbores), y = −95 (the lower window), x = 48 (gusset), x = 35 (the frame holes), assembly section x = 0 with OD-G01 and OD-G04.

## 7. Risks

- **K-1 (measured, blocks D-01b):** see §8. The web between the Ø6.5 counterbore and the R 8 corner arc at the two top holes reads 1.9216 mm on a coupon built to the spec values.
- **K-2 (measured, blocks D-03a):** see §8. The crowns of the horizontal Ø3.4 holes and Ø6.5 counterbores read 0° from horizontal with build direction +Y.
- **D-03a at exactly 45°:** the window gables are planar faces at 45.000° by construction; the band is 0.001°, so float noise is absorbed, but a margin of 0.000 will show. Fallback: none needed unless the census reads below 44.999°; then the gable is steepened, which changes the apex (a spec value) and is a question, not a fix.
- **U-03 coplanar boolean:** the carrier's front face and the housing's rear face are coplanar; `common_volume` on coplanar contact can fail to finish. The probe slab read 0.000 mm³ cleanly. If it is INCONCLUSIVE on the built part, it is reported as such, never passed.
- **Feature census counts** are predicted, not yet measured: OCCT may split a face at a seam or `clean` may leave the foot front strip separate. Any difference is reported as a deviation with its cause, and the plan's count is not edited to match.
- **Sharp wall-to-foot root:** no fillet is specified; the gussets carry the moment (A-11, REQ-09 Soft). Not changed without a spec amendment.

## 8. Conflicts (stop before J3)

**K-1: D-01b cannot be met with the spec's corner radius, hole position and counterbore diameter.** The top two counterbores (Ø6.5, centre (±44, 44)) sit 2.8284 from the R 8 corner-arc centres (±42, 42), so the web is 8.0 − 2.8284 − 3.25 = 1.9216 over the 2.0 depth of the counterbore. Measured with `min_wall` on a coupon of the wall's top corner built to those values (`01_CAD/probe/probe_conflicts_v01.py`): 1.9216 mm at (47.657, 47.657, −29.761), 45° reading the same; at the sweep's high rung Ø6.6: 1.8716 mm. D-01b requires ≥ 2.0 (margin −0.078); U-06 (Soft) reads the same. D-01a (≥ 0.8) and D-06a (≥ 1.0) pass. Options for the Usta (none taken by the designer):
  1. Counterbore Ø6.2 (web 2.07 nominal, 2.02 at Ø6.3): the ISO 7380 head Ø5.7 keeps 0.25 radial clearance; changes REQ-02 and A-09.
  2. Top corner radius R 6.0 about (±44, 44) (web 2.75): the carrier's corners then stand up to about 0.8 outside the housing's R 8 corners in view; changes §4 C1.
  3. D-01b lowered for this web to ≥ 1.9 with its reason (GATES D-01b allows a spec value ≥ D-01a), or a named exception.

**K-2: D-03a cannot be met while the Z holes and counterbores are round, and the named exception covers D-03b only.** With build direction +Y, the crowns of the four Ø3.4 holes and four Ø6.5 counterbores along Z are downward faces at 0° from horizontal. Measured with `overhang_census(build_dir=(0, 1, 0))` on a coupon wall with one such hole and counterbore: least 0.0° at the counterbore crown (0, 3.25, −29.94), 131 samples below 45°. D-03a requires ≥ 45° with "nothing supported"; the spec's named exception (Usta U-18) names D-03b for these crowns, not D-03a. Options:
  1. The Usta extends the named exception to D-03a for the crowns of the eight horizontal holes and counterbores (the check then excludes those eight cylindrical faces by position and reports their least angle inside the exception).
  2. Teardrop the eight holes (45° roof over each circle): replaces a spec feature, changes REQ-01 / REQ-02's round bores and D-03b's exception text.
