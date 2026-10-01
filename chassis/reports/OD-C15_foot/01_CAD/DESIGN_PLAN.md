# DESIGN_PLAN — od_c15_foot (20261001-od-c15-feet, concept C1)

Designer: Claude Code (Opus 5.5), designer role · spec version 1.0 (ratified 2026-10-01) · brief WP-02 (J2, attempt 1 of 2) · written before any geometry (D2)

D0 record: Python 3.13.7, build123d 0.11.1, OCP 7.9.3.1 (OCCT 7.9.3), repo `oguz-atolye` commit `10929db1408d89144bd4af9cad971440427933d0`. Input hash checked: `00_Spec/inputs/OD-C01_base_frame.step` = `7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805` (matches the brief).

### D1 measurement of OD-C01 (re-imported with `tools.core.read_step`, measured with `tools.measure`)

| Quantity | Measured | Spec A-01 | Agrees |
|---|---|---|---|
| validity | 1 solid, brep_valid 1, naked edges 0 | — | — |
| envelope | X −120.0 … 120.0, Y −6.0 … 0.0, Z −305.0 … 100.0 (240 × 6 × 405) | 240 × 405 × 6.0, top y 0, underside y −6.0 | yes |
| plate top / underside | one plane each, y 0.0000 (normal +Y) and y −6.0000 (normal −Y), each one face of 96 726 mm² spanning the full outline | flat around each hole | yes (one unbroken plane) |
| feet holes (`bore_census`, `locate_bore` with a point on each expected axis, direction Y) | four Ø3.4000 through-bores, axis (0, 1, 0), length 6.0, at (±110.0, ·, +90.0) and (±110.0, ·, −295.0), offset 0.0000 from each expected axis | Ø3.4 at (±110, +90), (±110, −295) | yes |
| corner arcs | four convex cylinders R10.000, axes (±110, ·, +90) and (±110, ·, −295): coaxial with the feet holes | R10 centred on each hole | yes |
| other bores | 22 more (Ø4.0 ×20, Ø8.0 ×2); nearest to a foot hole is Ø4 at (−113, −42), 132 mm away | — | no conflict |
| plate centre of mass (`mass_properties`) | (0.089, −3.000, −102.371) | — | inside the feet rectangle |

No spec value is contradicted by the measurement.

## 1. Datum

The centre of the foot's top face, on the screw axis, is at the origin because that
face bears on the plate underside and the axis is the axis of the plate's Ø3.4 hole:
both are the features that locate the foot (spec §2). +Z runs down in the machine,
away from the plate, and is the print build direction (top face on the bed); the
foot occupies z 0 … 10. +X is parallel to the OD-C01 X axis, and one pair of hex
pocket flats is parallel to X. This is the spec §2 foot frame.

Joint to OD-C01 (machine frame, X right, +Y up, +Z front, plate top y 0): foot x → X,
foot y → +Z, foot z → −Y, a proper rotation of +90° about X (Rx(+90°) sends (0,1,0) to
(0,0,1) and (0,0,1) to (0,−1,0)), then a translation to the measured hole axis at the
measured underside, (±110.0, −6.0, +90.0) and (±110.0, −6.0, −295.0).

## 2. Library and tools (D1)

- Cards read (one): UNO10 U5 tank heat-set (tags fdm, boss, bore, chamfer): its
  plane-census pattern and "keep size and position apart in envelope maths". Finding:
  nothing in the library matches a TPU foot or a captive hex-nut pocket; no geometry
  is reused from a card.
- `tools/` functions reused:
  - `tools.core.validity` (solid_count, brep_valid, naked_edges): U-01, exactly_one_solid.
  - `tools.core.write_step`, `step_roundtrip`, `read_step`, `compare_step`: D5 export (AP242), U-04.
  - `tools.core.write_stl` and its `checks["max_sagitta"]` (`stl_max_sagitta`, `tools.core.mesh_sagitta`): U-07.
  - `tools.core.common_volume` through `tools.measure.interference`: U-03 (a), (b).
  - `tools.measure.clearance`: U-03 (a) designed contacts, D-04c, REQ-03.
  - `tools.measure.engaged_area`: corroborates that each U-03 (a) contact is the designed face (not an edge touch).
  - `tools.measure.envelope`: U-02, D-02, REQ-01, REQ-04, REQ-05 (straight edges), REQ-06, REQ-07, envelope_within_spec.
  - `tools.measure.feature_census`, `bore_census`, `locate_bore`: U-05, D-04a, J-06, REQ-02, REQ-03 (seat height), joint input.
  - `tools.measure.min_wall` (and `detail["wide"]`): D-01a, D-01b, D-06a, U-06, J-05.
  - `tools.measure.radial_extent`, `radial_profile`: REQ-03 (flats, orientation, centring, mouth chamfer), REQ-04 (chamfers), REQ-05 (corner arc), J-05 corroboration.
  - `tools.measure.overhang_census`: D-03a. `tools.measure.flat_ceiling_spans`: D-03b corroboration.
  - `tools.measure.mass_properties`: REQ-06 (plate centre of mass), foot mass for the REPORT.
  - `tools.drawing.write_sections`, `nothing_clipped`: D6 sections.
- New code needed (job code under `01_CAD/` only, never in the repo):
  - the check-assembly builder (plate + 4 feet + 4 screw envelopes + 4 nut envelopes placed by joints);
  - the U-03 (b) nut slide pose loop (GATES U-03: "no tool yet");
  - arithmetic on tool Results: across-flats from two opposite `radial_extent` readings, flat orientation from two readings either side of a flat normal, pocket centre offset from the three opposite pairs, J-05 local ring.
- Missing tool behaviour (finding, see §7 Q1): `overhang_census` cannot settle a cone at exactly 45° (it returns INCONCLUSIVE at every spacing tried; probe in §7).
- Missing tool: no 3MF writer in `tools/` (spec §1 lists a 3MF); see §7 Q3.

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | body: cylinder Ø18.0 × 10.0 on the Z axis, z 0 … 10 | `Cylinder(r=body_d/2, h=height)`, aligned to z min 0 | — | §4 Body; REQ-04, U-02, U-05 |
| F02 | top-edge chamfer 0.5 × 45° (z 0, bed side, elephant-foot relief) | `chamfer` on the circular edge selected by position (the outer circle at z 0) | F01 | §4 Body; REQ-01, REQ-04, D-03a, U-05 |
| F03 | counter-edge chamfer 1.0 × 45° (z 10) | `chamfer` on the outer circular edge at z 10 selected by position | F01 | §4 Body; REQ-04, U-05 |
| F04 | lid hole Ø3.4 on the axis, z 0 … 2.5 | subtract `Cylinder(r=lid_hole_d/2)` spanning z −1 … lid_t + 1 (overshoot into the pocket void, no coplanar faces) | F01 | §4 Lid; D-04a, REQ-02, U-05 |
| F05 | hex nut pocket, across flats 5.60, flats parallel to X, from the seat z 2.5 to z 10 (open) | subtract a prism: `extrude` of a `RegularPolygon(radius=pocket_af/2, side_count=6, major_radius=False)` rotated so one flat pair is parallel to X (verified by measurement, not assumed), from z lid_t to z height + 1 (overshoot through the counter face) | F01 | §4 Nut pocket; REQ-03, J-05, U-05 |
| F06 | nut seat (the plane at z 2.5 between the lid hole and the flats) | results from F04 + F05; no own operation | F04, F05 | §4; REQ-03, U-03 (a), U-05 |
| F07 | pocket entry chamfer 0.5 × 45° at the mouth (z 10) | `chamfer` on the six hex edges at z 10 selected by position (edges in plane z = height with all points at radius < body_d/2 − counter_chamfer) | F03, F05 | §4 Nut pocket; REQ-03, U-03 (b), U-05 |
| F08 | name and export | label `od_c15_foot`; AP242 via `tools.core.write_step`; STL via `write_stl` | F01–F07 | U-04, U-07 |

Order note: F02 and F03 are cut on the plain cylinder before the pocket so that
chamfer edges are single circles; F07 runs last on the hex edges.

Fillets: none in the spec; the fillet ladder is not used.

Check assembly (`01_CAD/build_check_assembly.py`, not a part):

| A## | Item | Operation | Source |
|---|---|---|---|
| A01 | OD-C01 plate | imported unchanged, own frame = machine frame | brief inputs |
| A02 | foot ×4 | the D5 foot STEP re-imported, placed by joint (§5) | §2 joint |
| A03 | screw envelope ×4 | one solid: head Ø5.7 × 1.65 on y 0 … 1.65 + shank Ø3.0 from y 0 to the tip at y −12.0, coaxial with the measured hole axis | U-03, A-02 |
| A04 | nut envelope ×4 | hexagon s 5.5 (e 6.35) × m 2.4 with a Ø3.0 bore, flats parallel to X, top face on the foot's measured seat (foot z 2.5 … 4.9, machine y −8.5 … −10.9) | U-03, A-02, A-06 |
| A05 | assembly STEP | `write_step` of the named compound (plate, foot_1…4, screw_1…4, nut_1…4) | §1 deliverables |

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| body_d | 18.0 | mm | ±0.1 | §4 Body; REQ-04; derivation: R9 = R10 corner arc − 1.0 inside the outline (REQ-05) | yes (REQ-05) |
| height | 10.0 | mm | ±0.1 | §4 Body; REQ-04; A-04 | yes (REQ-06, REQ-07) |
| top_chamfer | 0.5 (45°) | mm | ±0.1 | §4 Body; REQ-04 | no |
| counter_chamfer | 1.0 (45°) | mm | ±0.1 | §4 Body; REQ-04 | no |
| lid_t (seat z) | 2.5 | mm | ±0.1 | §4 Lid; REQ-03 | yes (REQ-07, D-01b) |
| lid_hole_d | 3.4 | mm | ±0.1 (≥ 3.25 by D-04a) | §4 Lid; REQ-02; D-04a | yes (D-04a, U-03 shank pair) |
| pocket_af | 5.60 | mm | +0.05 / −0 | §4 Nut pocket; REQ-03; A-06 | yes (REQ-03, U-03 (b)) |
| pocket_rot | flats parallel to X | ° | ±1 | §2 frame; REQ-03 | no |
| mouth_chamfer | 0.5 (45°) | mm | — | §4; REQ-03 | no |
| overshoot | 1.0 | mm | — | derivation: tool bodies run 1.0 past each face they open, so no coplanar boolean faces | no |
| hole_xz | (±110.0, +90.0), (±110.0, −295.0) | mm | measured offset 0.0000 | A-01; measured in D1 | — (input) |
| plate_underside_y | −6.0 | mm | measured | A-01; measured in D1 | — (input) |
| screw head | Ø5.7 × 1.65 | mm | — | U-03; A-02 (ISO 7380 M3) | no (envelope) |
| screw shank, tip | Ø3.0, tip y −12.0 (foot z 6.0) | mm | ±0.1 on the tip (REQ-07) | U-03; REQ-07; A-02 (M3×12 from y 0) | no (envelope) |
| nut s, e, m, bore | 5.5, 6.35, 2.4, Ø3.0 | mm | s 5.32 … 5.50 (ISO 4032) | U-03; REQ-03; A-02 | yes, as the swept mating envelope (U-03 (b), REQ-03) |
| density | 1210 | kg/m³ | — | §3; A-03 | no |
| stl_tol | 0.01 | mm | — | U-07 | no |
| stl_angular | 0.18 | rad | ≤ 0.18858 | U-07: 4·acos(1 − 0.01/9.0) = 0.18858 rad, R_max 9.0 | no |
| step_timestamp | pinned per version | — | — | `write_step` (D-024) | no |

Sweep (D7) into `01_CAD/sweep_v##/`, one parameter at its low and high with the
others nominal, then the assembly-path pair jointly:

| Parameter | low | nominal | high |
|---|---|---|---|
| body_d | 17.9 | 18.0 | 18.1 |
| height | 9.9 | 10.0 | 10.1 |
| lid_t | 2.4 | 2.5 | 2.6 |
| lid_hole_d | 3.3 | 3.4 | 3.5 |
| pocket_af × nut s (joint, L-09) | {5.60, 5.65} × {5.32, 5.50}, all four corners | 5.60 × 5.50 | — |

Runs at a tolerance limit (height 9.9 / 10.1, body_d 17.9 / 18.1, lid_t 2.4 / 2.6)
are expected to read margin 0.000 on U-02 / REQ-04 / REQ-03 / REQ-06; every run must
still build one solid and pass every predicate.

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-C01 plate | `00_Spec/inputs/OD-C01_base_frame.step` (7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805) | its own frame = machine frame (D1: top y 0.0, underside y −6.0) | fixed (ground) | — |
| foot_1 … foot_4 | `02_STEP_STL/od_c15_foot_C1_v01.step` (hash at D5) | plate: each Ø3.4 hole axis from `locate_bore` (start point at the underside, direction) and the underside plane y from the hole's start; foot: its top-face plane (z 0) and its lid-hole axis from `locate_bore` on the foot | `RigidJoint` on the plate at Location(hole axis ∩ underside, Rx(+90°)) to the foot's `RigidJoint` at its origin; the rotation is the one spec §2 states (foot x → X, y → +Z, z → −Y), not a bounding-box fit | foot top face ↔ plate underside; foot axis ↔ hole axis |
| screw_1 … screw_4 | built in the check assembly (envelope) | the same measured hole axis; plate top y from the hole's end point | `RigidJoint` at hole axis ∩ top face | head underside ↔ plate top |
| nut_1 … nut_4 | built in the check assembly (envelope) | each placed foot's seat: the measured end of its lid-hole bore (z 2.5 in the foot frame), mapped by the foot's joint | `RigidJoint` at the seat point on the axis, flats parallel to X | nut top face ↔ foot nut seat |

Never the bounding-box centre; never an assumed rotation (the one rotation is the spec's).

## 6. Checks planned (D3)

All checks re-import the exported STEP (`read_step`) and gate through
`tools.result.gate` with the GATES §0 band: 0.005 mm for lengths, 0.001° for degrees,
0.001 mm³ for volumes, 0 for counts and 1/0 facts. Foot-frame numbers are measured on
the part file; machine-frame numbers on the check assembly as placed.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | `solid_count == 1` on the re-imported foot STEP (and on each part of the assembly) | `tools.core.solid_count` | 0 |
| U-01 | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | `tools.core.validity` | 0 |
| U-02 / envelope_within_spec | sizes 18.0, 18.0, 10.0 each in [spec − 0.1, spec + 0.1]; position reported apart: min x −9.0, min y −9.0, min z 0.0 | `envelope` | 0.005 mm |
| U-03 (a) designed contacts | at the four poses: `clearance(foot_i, plate) = 0`, `clearance(nut_i, foot_i) = 0` (top face on seat), `clearance(screw_i, plate) = 0` (head on top); each corroborated by `engaged_area` along the seating direction (depth 0.01): expected ≈ 217.9 mm² (foot annulus Ø17 − Ø3.4), ≈ 17.1 mm² (nut hex − Ø3.4), ≈ 16.4 mm² (head Ø5.7 − Ø3.4) | `clearance`, `engaged_area` | 0.005 mm (clearance); area is corroboration, not gated |
| U-03 (a) interference | per pose: foot\|plate, foot\|nut, foot\|screw, nut\|plate, screw\|plate `≤ 0` mm³ (20 pairs) | `interference` (`common_volume`) | 0.001 mm³ |
| U-03 (b) assembly path | per foot, the nut envelope slid along the measured pocket axis from first contact (nut top at z 10.0) and from the mouth pose (nut bottom at z 10.0, top 7.6) to the seat (top 2.5): 8 poses (top z 10.0, 7.6, 6.75, 5.9, 5.05, 4.2, 3.35, 2.5); `interference(nut, foot) ≤ 0`; swept jointly over pocket_af {5.60, 5.65} × nut s {5.32, 5.50} | `interference` in a job pose loop | 0.001 mm³ |
| U-04 | `step_roundtrip`: volume_delta 0, faces_delta 0, valid_after 1, label `od_c15_foot` read back unchanged, solids 1 (no stray shells) | `tools.core.step_roundtrip`, `compare_step` | 0.001 mm³; 0 for counts |
| U-05 / feature_census | planned counts: planar 15 (top annulus 1, counter annulus 1, seat 1, hex flats 6, mouth-chamfer planes 6), conical 2 (top and counter chamfers), cylindrical 2 (convex 1: Ø18; concave 1: Ø3.4), bores 1 (Ø3.4, axis Z, z 0 … 2.5, through to the pocket), all other kinds 0; total faces 19 | `feature_census`, `bore_census`, `locate_bore` | 0 |
| U-06 (Soft) | `min_wall` `detail["wide"]["measured"]` wrapped as `Result("min_wall_wide", …)` ≥ 2.0; missing key INCONCLUSIVE; expected ≈ 2.5 (the lid) | `min_wall` | 0.005 mm |
| U-07 | `write_stl(tol 0.01, angular 0.18 rad)` after clearing the triangulation; `stl_max_sagitta ≤ 0.01`; triangle count recorded | `tools.core.write_stl`, `mesh_sagitta` (`stl_max_sagitta`) | 0.005 mm |
| U-08 | N/A by its row: no threads in the part; confirmed by `feature_census` (no B-spline or helical faces) and `bore_census` (one plain Ø3.4 bore) | — | — |
| D-01a | `min_wall ≥ 0.8` (whole foot); expected 2.5 | `min_wall` | 0.005 mm |
| D-01b | `min_wall ≥ 2.0` (whole foot); expected 2.5 → PASS_ASSUMED A-03 | `min_wall` | 0.005 mm |
| D-02 | each envelope size ≤ 220, 220, 250 with the top face on the bed (part frame) → PASS_ASSUMED A-08 | `envelope` | 0.005 mm |
| D-03a | least overhang angle ≥ 45° over downward faces, build_dir (0, 0, 1); only the top-edge chamfer is downward (nut seat, counter face, counter chamfer, mouth chamfer all face up). Expected: INCONCLUSIVE (see §7 Q1); reviewer from sections per the row | `overhang_census(build_dir=(0,0,1), min_deg=45)` | 0.001° |
| D-03b | no bridge: `flat_ceiling_spans(max_span=5)` reads 0 with no `at` (no flat ceiling off the bed); reviewer from sections | `flat_ceiling_spans` | 0.005 mm |
| D-04a | lid hole Ø ≥ 3.25: `locate_bore(census, (0,0,1.25), (0,0,1))["diameter"]` | `bore_census`, `locate_bore` | 0.005 mm |
| D-04c | ≥ 0.5 per side, foot to the shank below the nut seat: `clearance` between the foot material above the seat (foot ∩ half-space z ≥ lid_t) and the shank envelope segment z lid_t … 6.0, in the foot frame; expected 1.30 (flat 2.80 − shank 1.50). The lid hole (0.20 per side to the Ø3.0 envelope) is D-04a's, not this row's → PASS_ASSUMED A-02 | `clearance` | 0.005 mm |
| D-06a | `min_wall ≥ 1.0` (whole foot); expected 2.5 | `min_wall` | 0.005 mm |
| D-07 | N/A by its row: no reamed fit bores (the pocket is REQ-03) | — | — |
| J-05 | wall around the nut pocket ≥ 3.0: `min_wall` of the ring above the seat (foot ∩ half-space z ≥ lid_t); expected ≈ 4.19 at the counter face (mouth-chamfer corner r 3.81 to counter chamfer r 8.0) and 5.77 below it (corner r 3.233 to R9). Corroborated by the material stretch from `radial_extent` at the six corner angles (0°, 60° … 300°) over z lid_t … height | `min_wall`, `radial_extent` | 0.005 mm |
| J-06 | no threaded bore: `bore_census` count 1 (Ø3.4 plain), no helical / B-spline faces in `feature_census` | `bore_census`, `feature_census` | 0 |
| REQ-01 | the face at z 0.0 ± 0.1 is one plane, normal −Z, an annulus Ø3.4 … Ø17.0: `envelope` min_z 0.0; feature census of planes at z 0 = 1; `radial_extent(side="outer")` at z 0 (0.001 inside) → 8.5 at 12 angles; inner edge from `locate_bore` diameter 3.4 | `envelope`, `feature_census`, `radial_extent`, `locate_bore` | 0.005 mm; 0 for counts |
| REQ-02 | lid hole Ø3.4 ± 0.1, z 0 … 2.5, coaxial offset ≤ 0.10 to the outer cylinder axis: `locate_bore` diameter, start/end z, `offset` from the point (0, 0, 1.25); outer-cylinder axis from `radial_profile(side="outer")` at z 5 (max − min ≤ noise, so its centre is the Z axis) → PASS_ASSUMED A-01 | `locate_bore`, `radial_profile` | 0.005 mm |
| REQ-03 | across flats = `radial_extent(side="inner", r_max=5)` at 90° + 270°, 30° + 210°, 150° + 330° at z 6.0: each 5.60 +0.05 / −0; flats parallel to X ± 1°: orientation from readings at 80° and 100° (r = d / cos(θ − 90° − φ), solved for φ); centre ≤ 0.10 from the three opposite-pair differences; seat z 2.50 ± 0.1 from the lid-hole bore's end z; pocket open at z 10 (`radial_extent` inner at z 9.999 → 3.3 at 90°, the 0.5 entry chamfer); clearance nut envelope to each flat in the assembly ≥ 0 (expected 0.05) → PASS_ASSUMED A-06 | `radial_extent`, `bore_census`, `locate_bore`, `clearance` | 0.005 mm; 0.001° |
| REQ-04 | outer Ø18.0 ± 0.1 (`radial_profile` outer, z 1 … 9, 36 angles); height 10.0 ± 0.1 (`envelope` size_z); chamfers: outer radius at z 0.001 → 8.5 (0.5) and at z 9.999 → 8.0 (1.0), each ± 0.1; sections corroborate → PASS_ASSUMED A-05 | `radial_profile`, `radial_extent`, `envelope` | 0.005 mm |
| REQ-05 | at each pose, least distance foot outer cylinder → plate edge ≥ 0.9: straight edges from `envelope` of the placed foot against the plate envelope (x 120 − 119 = 1.0; z 100 − 99 = 1.0 and −305 vs −304); corner arc: `radial_profile(plate, hole axis, side="outer")` over the outward 90° sector (19 angles, y −5.999 … −0.001) minus the placed foot's max outer radius minus the `locate_bore` axis offset; expected 1.0 → PASS_ASSUMED A-01 | `envelope`, `radial_profile`, `locate_bore` | 0.005 mm |
| REQ-06 | four counter faces at y −16.00 ± 0.10 (`envelope` min_y of each placed foot); plate centre of mass (`mass_properties`, x 0.089, z −102.371) inside the rectangle of the four measured foot axes; signed margins reported (≈ 109.9, 192.4, 192.6) → PASS_ASSUMED A-01, A-04 | `envelope`, `mass_properties`, `locate_bore` | 0.005 mm |
| REQ-07 | screw tip in the foot frame (screw envelope mapped by the inverse of the foot joint): `envelope` max_z = 6.0 ± 0.1; tip − nut lower face (seat z + 2.4 = 4.9) ≥ 0.5 (expected 1.1); counter face − tip ≥ 2.0 (expected 4.0) → PASS_ASSUMED A-02 | `envelope`, `locate_bore` | 0.005 mm |

D6 sections (`write_sections`, `nothing_clipped`): foot XZ and YZ through the axis
(flats and corners), XY at z 6.0 (pocket); assembly section through one foot axis
(plate, foot, screw, nut). P1–P6 answered in the REPORT.

## 7. Risks and questions

**Q1 (needs an orchestrator decision before J3): D-03a cannot read PASS with the
spec's exact 45° chamfer.** A probe of the tool on a generic Ø18 × 10 cylinder with
a 0.5 × 45° bed-edge chamfer (not the target; scratchpad diagnostic) gave
`overhang_census` INCONCLUSIVE at spacing 0.5, 0.25, 0.1 and 0.05: "the least,
45.0000°, lies within its sampling bound (0.0083 … 0.0099°) above min_deg"
(`below_min_deg` 0, per kind cone 45.0). INCONCLUSIVE is never PASS. Options:
(a) amend spec §4 / D-03a so the bed-edge chamfer is steeper than 45° from
horizontal (for example 0.5 radial × 0.87 high, 60°), which keeps the elephant-foot
relief and gives a 15° margin; (b) keep 45° and let the reviewer settle D-03a from
sections, as the row's check column allows, with my REPORT reading INCONCLUSIVE;
(c) a tools change outside this job (an exact angle for a cone coaxial with the
build direction). Planned default if no answer: (b), build to spec as written.

**Q2 (confirm the reading): J-05 and D-04c are measured locally.** A whole-part
`min_wall` reads the lid (2.5), which is below J-05's 3.0 although the wall around
the pocket is 4.19 … 5.77; a whole-part `clearance(foot, shank)` reads the lid hole
(0.20 per side), which is below D-04c's 0.5 although the shank in the pocket has
1.30. The plan measures each on the region the row names (foot material above the
seat plane; shank from the seat to its tip). Confirm this is the intended reading.

**Q3: 3MF deliverable.** Spec §1 lists a 3MF of one foot; `tools/` has no 3MF
writer, and this role does not write packages. The plan exports STEP and STL only;
who produces the 3MF?

Risks and fallbacks:
- Hex orientation of `RegularPolygon`: whether a vertex or a flat lies on +X is not
  assumed; REQ-03's orientation check measures it and the build rotates by 30° if needed.
- Coplanar boolean faces at the seat and counter face: tool bodies overshoot 1.0.
- Coincident Ø3.0 surfaces (nut bore on shank) may upset the boolean; that pair is
  not a §5 pair and is not gated; reported as information only.
- Exact-limit sweep runs (margin 0.000 within the 0.005 band) are expected and
  reported, not widened.
