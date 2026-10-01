# DESIGN_PLAN — od_c08_tray (20261001-od-c08-electronics-bay-tray, concept C1)

Designer: Claude Code, claude-opus-5-5 · spec version 1.0 · written before any geometry (D2), package WP-02 (J3 with its own plan)

## 1. Datum

The part is built directly in the OD-C01 machine frame of spec §2 (X to the
user's right, +Y up, +Z toward the front, the plate's top face y = 0), because
every interface of this part is given in that frame: the flange stands on the
plate's top face (y = 0), the wall keeps its distance from the bulkhead's base
rail (+X face x 71.0), and the standoffs meet the board at the joint of §4. The
flange's underside is at y = 0 because it is the designed contact with OD-C01's
top face (measured y 0.0, probe below). The wall's outer face is at x 73.0 because
it is the print bed face (A-08) and keeps 2.0 of air to the rail's +X face x 71.0
(A-06). The standoff tops are at the board's solder face, measured on the placed
OD-E01 at x 82.438 (= 84.0 − 1.562; the spec's 82.44 rounded), because the solder
face on the standoff tops is the designed contact (U-03 (a)).

Inputs measured for the plan (`01_CAD/probe/probe_inputs.py` → `01_CAD/probe/probe_inputs.json`):

| Fact | Measured | Spec §4 |
|---|---|---|
| OD-E01: solids, faces, validity | 1 solid, 1233 faces, brep_valid 1, naked_edges 0 | one fused envelope solid |
| OD-E01 placed: envelope | x 82.438 … 109.262, y 24.000 … 83.869, z −195.002 … −94.838 | x 82.44 … 109.26, y 24.0 … 83.87, z −195.0 … −94.84 |
| Solder face (largest −X plane) | x 82.438, 5947.04 mm², y 24.0 … 83.869, z −195.002 … −94.838 | x 82.44 |
| H1 (`locate_bore`, along X) | Ø4.044 at (y 80.001, z −100.003), through, 1.562 long | (80.00, −100.00) |
| H2 | Ø4.012 at (y 27.991, z −100.013) | (27.99, −100.01) |
| H5 | Ø2.486 at (y 81.976, z −157.519) | (81.98, −157.52) |
| H6 | Ø2.460 at (y 30.992, z −157.511) | (30.99, −157.51) |
| Board at x < 82.44 (solder side below the board) | nothing: no face of OD-E01 reaches x < 82.40; the minimum x is the solder face 82.438 (the solder side is invented flat, A-05; the heatsink's solder-side screw heads X-35, X-36 are not in the model) | standoffs must clear it |
| Highest point in x | x 109.262 (heatsink) | 109.26 |
| OD-C01 plate top in the zone | one planar +Y face at y 0.000 spanning x −120 … 120, z −305 … 100; no hole under the tray (its nearest bores Ø4.0 at x 65, z −225 / −165 / −105 / −45) | y 0; new inserts A-01 |
| OD-C02 +X faces | base rail x 71.0 (y 0 … 12), electric face x 67.0 (y 12 … 207), top rail x 70.5 (y 207 … 215), z −240 … −30 | 71.0 / 67.0 / 70.5 |

## 2. Library and tools (D1)

- Cards read (at most two): UNO10 U5 tank heat-set (tags heat-set, boss, fdm): the
  boss-plus-blind-bore pattern and the lesson "keep how big and where apart in the
  envelope". Nothing else matched an on-edge PCB carrier.
- `tools/` functions reused: `tools.core.write_step` (AP242 part and assembly),
  `write_stl` (STL, sagitta), `read_step`, `validity`, `compare_step`,
  `common_volume`; `tools.measure.envelope`, `bore_census`, `locate_bore`,
  `feature_census`, `min_wall`, `min_wall_wide` (spacing 0.7, brief),
  `overhang_census(build_dir=(1,0,0))`, `flat_ceiling_spans`, `clearance`,
  `radial_extent`, `mass_properties`, `mesh_census`;
  `tools.measure.features.cylinder` (axis of the convex pin faces);
  `tools.drawing.write_sections` (D6, with `nothing_clipped`).
- New code needed (job code only, in `01_CAD/`): region solids cut from the
  re-imported STEP by boxes (pins; the standoff seat layer) so the board's designed
  contacts are measured apart from the rest of the tray; the four driver
  cylinders and the faston box of REQ-04 / REQ-05; the U-03 (b) path loop; the
  plate-material probe under the four flange holes (A-01). No `tools/measure`
  function is missing for a gated row; `bore_census` does not find convex pins, so
  the pins are located from their cylindrical faces' axes.

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Wall + floor flange (one L section) | extrude along Z of the L profile (x 73…112 × y 0…4, x 73…76 × y 0…92), z −230 … −70 | — | §4 Wall, Floor flange; U-02, REQ-03 |
| F02 | Gussets ×4 | extrude along Z of a right triangle (legs 20 up x 76 and 20 along y 4), unioned | F01 | §4 Gussets; E-06 |
| F03 | Insert standoffs ×2 (H1, H2) Ø10 | cylinder along +X from x 76.0 to the seat x 82.438, unioned | F01 | §4 Standoffs; REQ-02, D-05a, J-05 |
| F04 | Pin standoffs ×2 (H5, H6) Ø6 | cylinder along +X from x 76.0 to x 82.438, unioned | F01 | §4 Standoffs; REQ-02 |
| F05 | Locating pins ×2 Ø1.8 × 2.5 | cylinder along +X from x 82.438 to 84.938 on F04, unioned | F04 | REQ-02, D-04d, D-06a |
| F06 | Insert bores ×2 Ø4.0 × 6.0 blind | cylinder cut along −X from x 82.438 (cutter 1.0 past the top) | F03 | REQ-02, D-05b |
| F07 | Flange holes ×4 Ø3.4 through | cylinder cut along Y through the flange (cutter 1.0 past each face) | F01 | REQ-01, D-04a |
| F08 | Tie slots ×4, 2.0 (z) × 4.0 (y) | box cut through the wall along X (1.0 past each face) | F01 | §4 Tie points; E-11 |

No fillets: the spec asks for none (U-06 reads the bare corners).

Expected face census (U-05, `feature_census`): planes 42 (L section 8, gussets 10:
3 each for the two inner ones, 2 each for the two flush with the ends; standoffs
8: four seat faces, two bore floors, two pin tops; slots 16), cylinders 12
(convex 6: four standoff sides and two pins; concave 6: two insert bores and four
flange holes), cones, spheres, tori, B-splines and other 0; bores 6 (two blind
along X, four through along Y).

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| wall_x0, wall_x1 | 73.0, 76.0 | mm | — | §4 Wall | no |
| wall_y1 | 92.0 | mm | — | §4 Wall | no |
| z_min, z_max | −230.0, −70.0 | mm | ±0.1 (U-02, REQ-03) | §4 Wall, Floor flange | no |
| flange_x1, flange_t | 112.0, 4.0 | mm | ±0.1 (REQ-01 length) | §4 Floor flange | no |
| hole_d | 3.4 | mm | ±0.1 (REQ-01), ≥ 3.25 (D-04a) | §4, REQ-01 | yes |
| hole_xz | (88, −222), (106, −222), (88, −78), (106, −78) | mm | offset ≤ 0.10 | §4, REQ-01, A-01 | no |
| gusset_t, gusset_leg | 3.0, 20.0 | mm | — | §4 Gussets | no |
| gusset_z0 | −230.0, −212.0, −88.0, −73.0 | mm | — | §4 Gussets | no |
| seat_x | 82.438 | mm | ±0.05 (REQ-02) | derivation: the measured solder face of the placed OD-E01 (84.0 − 1.562, X-24), so the seat contact reads clearance 0 and interference 0; the spec's 82.44 is this rounded | yes |
| insert_boss_d | 10.0 | mm | — | §4 Standoffs, D-05a, J-05 | no |
| bore_d, bore_depth | 4.0, 6.0 | mm | ±0.05, ±0.1 (D-05b) | §4, REQ-02, A-07 | yes |
| insert_yz | (80.00, −100.00), (27.99, −100.01) | mm | offset ≤ 0.10 | REQ-02 (X-25, X-26) | yes (E-05) |
| pin_boss_d | 6.0 | mm | — | §4 Standoffs | no |
| pin_d, pin_len | 1.8, 2.5 | mm | ±0.05, ±0.1 (REQ-02) | §4, REQ-02, D-04d | yes |
| pin_yz | (81.98, −157.52), (30.99, −157.51) | mm | offset ≤ 0.10 | REQ-02 (X-29, X-30) | yes (D-04d, E-05) |
| slot_w_z, slot_h_y | 2.0, 4.0 | mm | — | §4 Tie points | no |
| slot_y0 | 86.0 | mm | — | §4 Tie points | no |
| slot_zc | −176, −168, −122, −114 | mm | — | §4 Tie points | no |
| overshoot | 1.0 | mm | — | derivation: cutters pass 1.0 beyond a free face so no zero-thickness skin is left | no |
| board_joint | origin (84.0, 80.0, −100.0); board x → −Z, z → +X (y → +Y) | — | — | §4 Board joint, A-03 | — |
| stl_tol, stl_ang | 0.01, 0.20 | mm, rad | — | U-07: 0.20 ≤ 4·acos(1 − 0.01/5.0) = 0.2530 (R_max 5.0, the Ø10 standoff) | no |
| density | 1270 | kg/m³ | — | §3, A-10 | no |

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-E01 power PCB | `00_Spec/inputs/OD-E01_power_pcb.step` (90780af3…bfd869) | its datum frame (origin on H1's axis at the component face, +Z out of the component side); confirmed on the placed solid: H1 axis at (y 80.001, z −100.003), solder face x 82.438 | RigidJoint on the tray at Location(Plane(origin (84, 80, −100), x_dir (0, 0, −1), z_dir (1, 0, 0))) → the board's own frame | solder face on the four standoff seats; pins in H5, H6; M3 screws in H1, H2 |
| OD-C01 base frame | `00_Spec/inputs/OD-C01_base_frame.step` (7b5688af…195805) | identity (its frame is the machine frame); plate top measured y 0.0 | RigidJoint at the identity | flange underside on the plate top |
| OD-C02 bulkhead | `00_Spec/inputs/OD-C02_bulkhead.step` (1e36348a…14bdc) | identity; base rail +X face measured x 71.0 | RigidJoint at the identity | none (clearance ≥ 1.5) |

## 6. Checks planned (D3)

Band from GATES §0: mm 0.005, mm³ 0.001, deg 0.001, counts 0. Spacing 0.7 for
`min_wall` and `overhang_census` (brief: the tools refuse the large faces at the default).

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| U-01 | one solid, brep_valid 1, naked_edges 0 | `validity` | count 0 |
| U-02 | sizes 39.0 × 92.0 × 160.0 each ± 0.1; position x 73 … 112, y 0 … 92, z −230 … −70 apart | `envelope` | mm 0.005 |
| U-03 (a) | flange to OD-C01 clearance 0 and interference ≤ 0; seat layer (top 0.538 of each standoff) to OD-E01 clearance 0; tray to OD-E01 interference ≤ 0; pins to OD-E01 ≥ 0.30; tray less pins and seat layer to OD-E01 ≥ 0.5; tray to OD-C02 ≥ 1.5; OD-E01 to OD-C02 ≥ 10.0; OD-E01 envelope in x 70 … 117, z −240 … −30, y ≥ 10; plate material under each flange hole (footprint over solid plate, ≥ 6.0 from every existing plate hole, ≥ 8.0 from the plate edge; A-01) | `clearance`, `common_volume`, `envelope`, `bore_census`, `radial_extent` on the assembly STEP's parts | mm 0.005, mm³ 0.001 |
| U-03 (b) | OD-E01 moved +X by 5.0, 4.5 … 0 (steps 0.5) to the seat: interference with the tray ≤ 0 at each step (clearance beside it) | `common_volume`, `clearance` | mm³ 0.001 |
| U-04 | part re-read: solids 1, volume_delta 0, faces_delta 0, valid after, label; assembly re-read: 4 solids, labels, faces_delta 0 | `compare_step` | mm³ 0.001, count 0 |
| U-05 | census of §3 (42 planes, 12 cylinders: 6 convex, 6 concave, 6 bores); bores: 2 blind along X, 4 through along Y; 2 pins; 4 slots (planar faces of the slot sides) | `feature_census`, `bore_census`, `locate_bore` | count 0 |
| U-06 (Soft) | `min_wall_wide` ≥ 2.0 on the solid without the pins (D-01b exception), whole part reported | `min_wall_wide` | mm 0.005 |
| U-07 | STL at 0.01 / 0.20 rad; angular ≤ 0.2530; sagitta ≤ 0.01 (re-meshed from the re-imported STEP); mesh one closed body | `write_stl`, `mesh_census` | mm 0.005 |
| U-08 | N/A by its row | — | — |
| D-01a | `min_wall` ≥ 0.8 (whole part) | `min_wall` | mm 0.005 |
| D-01b | `min_wall` ≥ 2.0 on the solid without the two pins (cut at x 82.438 inside the Ø6 standoffs) | `min_wall` | mm 0.005 |
| D-02 | 92.0 × 160.0 on the bed, 39.0 tall ≤ 220 × 220 × 250 (A-09) | `envelope` | mm 0.005 |
| D-03a | least overhang ≥ 45° (build +X) on the solid with the four flange holes refilled by position; the crowns' least angle reported apart | `overhang_census` | deg 0.001 |
| D-03b | reviewer row; designer's reading: widest flat ceiling (`flat_ceiling_spans`, max 5.0) and the widest horizontal bore (3.4) ≤ 5 | `flat_ceiling_spans`, `bore_census` | mm 0.005 |
| D-04a | four flange holes Ø ≥ 3.25 | `locate_bore` | mm 0.005 |
| D-04c, E-01 | tray less pins and seat layer to OD-E01 ≥ 0.5 | `clearance` | mm 0.005 |
| D-04d | each pin to OD-E01 ≥ 0.30 | `clearance` | mm 0.005 |
| D-05a | across each insert bore ≥ 8.0 (rays ±Y, ±Z at mid-depth) | `radial_extent` | mm 0.005 |
| D-05b | insert bores Ø 4.0 ± 0.05, depth 6.0 ± 0.1, ≥ 5.7, blind | `locate_bore` | mm 0.005 |
| D-06a | `min_wall` ≥ 1.0 (whole part: the pins) | `min_wall` | mm 0.005 |
| D-07 | N/A by its row | — | — |
| J-05 | wall around each insert bore ≥ 3.0 (ray radius − bore radius, four directions) | `radial_extent` | mm 0.005 |
| E-05 | tray insert bore axes vs OD-E01 H1, H2 axes; pin axes vs H5, H6 axes: offset ≤ 0.10 | `locate_bore` on both solids, pin face axes | mm 0.005 |
| E-06 | reviewer row; designer's reading: one solid, four gussets present (census), each standoff's base on the wall face x 76.0 | `feature_census`, faces | count 0 |
| E-11 | reviewer row; designer's reading: four tie slots through the wall above y 83.87; REQ-05 box empty (open on +X) | faces, `common_volume` | count 0 |
| REQ-01 | four holes Ø3.4 ± 0.1, offset ≤ 0.10, 4.0 ± 0.1 long, through; underside one plane at y 0.00 ± 0.10 | `locate_bore`, `envelope`, faces | mm 0.005 |
| REQ-02 | four seat faces at x 82.44 ± 0.05; bore and pin positions offset ≤ 0.10; pins Ø1.8 ± 0.05, 2.5 ± 0.1 | faces, `locate_bore`, pin face axes | mm 0.005 |
| REQ-03 | `envelope` min_x ≥ 73.0; max_z −70.0 ± 0.1 | `envelope` | mm 0.005 |
| REQ-04 | four Ø8 × 116 cylinders (y 4 … 120) on the hole axes: interference with tray and with OD-E01 = 0 | `common_volume` | mm³ 0.001 |
| REQ-05 | box x 85 … 117, y 4 … 92, z −195 … −95: interference with the tray = 0 | `common_volume` | mm³ 0.001 |
| REQ-06 (Soft) | bench gate: INCONCLUSIVE by its row | — | — |
| exactly_one_solid | solid_count = 1 | `validity` | count 0 |
| feature_census | §3 counts | `feature_census` | count 0 |
| envelope_within_spec | size and position apart (= U-02) | `envelope` | mm 0.005 |

## 7. Risks

- Booleans against OD-E01 (1233 faces) may be slow or fail: a failed
  `common_volume` is reported INCONCLUSIVE with its reason, and the same pair is
  also gated on `clearance`.
- The seat is an exact contact on a scanned face (82.438): any rounding of the seat
  to 82.44 would read as 0.002 interference; the seat is taken from the
  measurement, not the rounded spec number.
- The pin clearance in H6 is 0.33 nominal; a position error of 0.03 or more toward
  the hole wall drops it under 0.30. The sweep shifts the standoffs to show the margin.
- The flange holes' crowns are the only downward faces (named exception); if the
  refill does not give one clean solid the D-03a reading is INCONCLUSIVE.
