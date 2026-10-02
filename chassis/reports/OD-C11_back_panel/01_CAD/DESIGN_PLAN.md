# DESIGN_PLAN — od_c11_back (20261001-od-c11-back-panel, concept C1)

Designer: Claude Code, claude-opus-5-5 · spec version 1.0 · written before any geometry (D2) · brief WP-02 (J3 package with its own plan), build attempt 1 of 2, fix_cycles 3

## 1. Datum

The OD-C01 machine frame of spec §2, the identity to every overlay: X to the user's right, +Y up, +Z toward the front, the plate's top face at y = 0. The panel's underside is at y = 0 because the wall's and the flanges' undersides stand on the plate's top face (the designed contact of U-03 (a)); the outer face is the plane z = −302.0 and the inner face z = −299.0 because the spec places the wall 3.0 inside the plate's rear edge z −305 (A-02); the panel is symmetric about x = 0, the plate's mid-plane, except for the pass-throughs and vents (§4). Probe `01_CAD/probe/probe_placements_v01.json` measured on the delivered plate: top face y 0.000000 (one planar face, 96 725.984 mm²), rear face z −305.000 over x −110 … +110, side faces x ±120.000 over z −295 … +90, corner cylinders R 10.000 about (±110, −295) along Y, the rear edge at x ±116 at z −303.0004 and at x ±114 at z −304.1654, the feet holes Ø3.400 through at (±110, −295) (offset 0.000), and 26 bores in all (none at the four new insert positions, as A-01 says). No part of this job moves the frame.

## 2. Library and tools (D1)

- Cards read (one): UNO10 U5 tank heat-set (tags heat-set, boss, fdm): its lesson "keep how big and where apart in the envelope" is followed in U-02 (size and position gated apart). No geometry is reused; the spec fixes every boss value. Nothing in the index matches a flat printed panel; that is a finding only in that no card covers a wall panel.
- Precedent named by the brief (read-only): `/home/claude/open-dedica/chassis/reports/OD-C02_bulkhead/01_CAD/` (build, check and probe v02): the script shape, the joints by `Location(Plane(...))` and `RigidJoint`, the refill-by-position of the named-exception bores for D-03a.
- `tools/` functions reused: `tools.core` `read_step`, `write_step` (AP242, D-024), `write_stl`, `validity`, `compare_step`, `common_volume`; `tools.measure` `envelope`, `bore_census`, `locate_bore`, `feature_census`, `min_wall` and `min_wall_wide` (spacing 0.7, brief note: the default spacing refuses the large faces), `overhang_census(build_dir=(0,0,1), spacing=0.7)`, `flat_ceiling_spans` (D-03b designer reading), `radial_extent`, `clearance`, `mass_properties`, `mesh_census`; `tools.result.gate` with the GATES.md §0 bands (mm 0.005, deg 0.001, mm³ 0.001, counts and other units 0); `tools.drawing.write_sections` (D6).
- New code (job code only, never in the repo): the planar-face readings of the underside (REQ-01) and the ledge top (REQ-07); the footprint-against-plate reading of U-03 (a) (the panel's underside face intersected with the plate's top face and with that face's outer outline, plus the distance from the footprint's edges to the outline); the refill-by-position of the six named-exception holes for D-03a and the per-face split of the downward faces; the lowering path of U-03 (b); the keep-out boxes of REQ-05 and the driver cylinders of REQ-08.
- Missing tool: none for a gated number. D-03b, E-06 and E-11 are reviewer rows (from sections); the designer gives a reading only.

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Wall x −116.0 … +116.0, y 0 … 215.0, z −302.0 … −299.0 | box | — | §4 C1, REQ-02, U-02 |
| F02 | Floor flanges ×2, x ±(72.0 … 114.0), y 0 … 4.0, z −299.0 … −283.0 | box ×2, fused | F01 | §4, REQ-01, REQ-05, E-06 |
| F03 | Gussets ×4, 4.0 thick at x ±(72.0 … 76.0) and ±(110.0 … 114.0): right triangle in YZ, vertices (y 4, z −299), (y 4, z −283), (y 34, z −299) | triangle sketched on a YZ plane, extruded 4.0 along X, fused | F01, F02 | §4, E-06, D-03a (hypotenuse faces +Y +Z, up in the print) |
| F04 | Top ledge x −114.0 … +114.0, y 211.0 … 215.0, z −299.0 … −287.0 | box, fused | F01 | §4, REQ-07, E-06 |
| F05 | Insert bosses ×2, x ±(84.0 … 96.0), y 203.0 … 211.0, z −299.0 … −287.0 | box ×2, fused | F01, F04 | §4, D-05a, J-05, E-06 |
| F06 | Flange holes ×4, Ø3.4 through along Y at (x ±81.0, z −290.0) and (x ±100.0, z −290.0), cutter y −1.0 … 5.0 | cylinder, cut | F02, F03 | REQ-01, D-04a, U-05 |
| F07 | Insert bores ×2, Ø4.0 × 6.0 blind along −Y from y 215.0 at (x ±90.0, z −293.0), cutter y 209.0 … 216.0 (flat floor at y 209.0) | cylinder, cut | F04, F05 | REQ-07, D-05b, U-05 |
| F08 | Pass-throughs ×3, Ø12.0 through the wall along Z: cord (95.0, 30.0), tubes (−100.0, 30.0) and (−84.0, 30.0), cutter z −303.0 … −298.0 | cylinder, cut | F01 | REQ-03, REQ-04, E-11, U-05 |
| F09 | Vent slots ×5 through the wall along Z, 4.0 wide (X) × 80.0 tall (Y) overall, ends R 2.0 (arc centres y 102.0 and 178.0), centres x 78, 86, 94, 102, 110, cutter z −303.0 … −298.0 | stadium sketch (`SlotCenterToCenter`) extruded, cut | F01 | REQ-06, E-11, U-05 |

Order note: every fused feature (F01–F05) comes before every cut (F06–F09), so no cut is refilled; the cutters of F08 and F09 stop at z −298.0, which is clear of every fused feature at those (x, y) (F02 and F03 end at y 34 at |x| ≥ 72, the bosses start at y 203).

Expected census (U-05, derived from F01–F09 face by face; coplanar faces merge on `clean()`):
- planar faces 46: wall outer, inner, underside (wall and flanges, one plane), top (wall and ledge, one plane), 2 wall ends (6); per flange top (between its gussets), front, and 2 ends merged with the outer gusset faces (8); gusset inner faces 4 and hypotenuses 4 (8); ledge front merged with the 2 boss fronts, ledge underside in 3 pieces, 2 ledge ends (6); boss undersides 2 and boss sides 4 (6); bore floors 2; slot sides 10.
- cylindrical faces 19, all concave, none convex: 4 flange holes, 2 insert bores, 3 pass-throughs, 10 slot-end half-cylinders; no cone, sphere, torus or B-spline face.
- bores (`bore_census`, more than 180° of arc) 9: 4 × Ø3.4 along Y through, 2 × Ø4.0 along Y blind, 3 × Ø12.0 along Z through. The slot ends are 180° arcs and are not bores; each slot is read with `radial_extent` rays.
- Refilled solid for D-03a (the six named-exception holes plugged by position): planar 44, cylindrical 13, 57 faces.

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| wall_x_half | 116.0 | mm | ±0.1 | §4, REQ-02, A-02 | no |
| wall_z_out / wall_z_in | −302.0 / −299.0 | mm | ±0.10 | §2, §4, REQ-02, A-02 | yes (the wall's foot inside the plate's rear edge: 1.0 behind it at x ±116) |
| y_bottom / y_top | 0.0 / 215.0 | mm | ±0.10 | §4, REQ-01, REQ-07, A-05 (OD-C02 A-06) | yes (y_top: the top panel's seat) |
| flange_x0 / flange_x1 | 72.0 / 114.0 (both sides) | mm | — | §4, REQ-05, A-07 | no |
| flange_t / flange_z1 | 4.0 / −283.0 | mm | ±0.1 | §4, REQ-01, REQ-05 | no |
| gusset_t / gusset legs | 4.0 / 16.0 along the flange, 30.0 up the wall | mm | — | §4, E-06 | no |
| gusset_x | ±(72.0 … 76.0), ±(110.0 … 114.0) | mm | — | §4 | no |
| ledge y / z / x | 211.0 … 215.0 / −299.0 … −287.0 / ±114.0 | mm | ±0.1 | §4, REQ-07 | no |
| boss x / y / z | ±(84.0 … 96.0) / 203.0 … 211.0 / −299.0 … −287.0 | mm | — | §4, D-05a, J-05 | no |
| flange_hole_d | 3.4 | mm | ±0.1 | REQ-01, D-04a (≥ 3.25), A-01 | yes |
| flange_hole_xz | (±81.0, −290.0), (±100.0, −290.0) | mm | offset ≤ 0.10 | REQ-01, A-01 | yes (coaxial with the four new OD-C01 inserts) |
| insert_d / insert_depth | 4.0 / 6.0 | mm | ±0.05 / ±0.1 | REQ-07, D-05b, A-05 | yes |
| insert_xz | (±90.0, −293.0) | mm | offset ≤ 0.10 | REQ-07, A-05 | yes (the top panel's screws) |
| pass_d | 12.0 | mm | ±0.1 | REQ-03, REQ-04, A-03, A-04 | yes (grommet and tube fit, A-03, A-04) |
| pass_xy | cord (95.0, 30.0); tubes (−100.0, 30.0), (−84.0, 30.0) | mm | offset ≤ 0.10 | REQ-03, REQ-04 | no |
| vent_w / vent_y0 / vent_y1 / vent_r | 4.0 / 100.0 / 180.0 / 2.0 | mm | ±0.1 | REQ-06, A-06 | no |
| vent_x | 78, 86, 94, 102, 110 | mm | ±0.1 | REQ-06, A-06 | no |
| overshoot | 1.0 | mm | — | derivation: a cutter passes 1.0 beyond every free face it opens, for clean booleans; the insert bores' cutters start exactly at their floor y 209.0 | no |
| stl_tol / stl_ang | 0.01 / 0.20 | mm / rad | — | U-07: R_max = 6.0 (the pass-throughs), 4·acos(1 − 0.01/6.0) = 0.2310 rad ≥ 0.20 | no |
| density | 1270 | kg/m³ | — | §3, A-10 (reported only) | no |
| timestamp | 2026-10-01T00:00:00 | — | — | derivation: the job date, pinned so the same build gives the same bytes | no |

No fillets: the spec names none, so the descending-radius ladder is not used.

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-C01 plate | `00_Spec/inputs/OD-C01_base_frame.step` (7b5688af…5805) | its own frame is the machine frame (probe: top face y 0.000, rear face z −305.000, corners R 10.000 about (±110, −295)) | RigidJoint at the origin, identity | the panel's underside on the top face y 0 (designed contact); flange holes over the four new insert positions (A-01) |
| OD-C02 bulkhead | `00_Spec/inputs/OD-C02_bulkhead.step` (1e36348a…4bf78) | its own frame is the machine frame (probe envelope x 59 … 71, y 0 … 215, z −240 … −30) | RigidJoint at the origin, identity | none (clearance ≥ 20.0; probe: 43.0 from the plane z −283) |
| OD-C03 cradle | `00_Spec/inputs/OD-C03_pump_cradle.step` (8d6f60ba…7034) | OD-C01 §4 A-03 joint: local x → +Z, y → −Y, z → +X, origin (0, 40, −205), built as `Location(Plane(origin, x_dir=(0,0,1), z_dir=(1,0,0)))` (a proper rotation; probe: local x → (0,0,1), y → (0,−1,0), z → (1,0,0)); probe: the foot's underside lands on y 0.000000, rear-most z −245.0 | RigidJoint | none (clearance ≥ 20.0; probe: 38.0 from the plane z −283) |
| OD-H01 pump | `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` (b05302af…fb62) | at OD-C03's identity, then OD-C03's placement (same Location) | RigidJoint | none (clearance ≥ 20.0; probe: rear-most z −232.2, 50.8 from the plane z −283) |
| OD-W03 tank seat | `00_Spec/inputs/OD-W03_tank_seat.step` (55162e2d…0c51c69ba) | reference only (brief), not placed | — | — |

The check assembly `02_STEP_STL/od_c11_assembly_C1_v01.step` holds the panel, OD-C01, OD-C02, OD-C03 and OD-H01 as placed above, each a named child.

## 6. Checks planned (D3)

Every predicate re-imports the exported STEP (part and assembly), measures with `tools.core` / `tools.measure`, and compares through `tools.result.gate` with the GATES.md §0 band of the result's unit. Thresholds come from spec §5 only; any exception or missing value is INCONCLUSIVE.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| U-01 | solid_count = 1, brep_valid = 1, naked_edges = 0 | `validity` | 0 (counts) |
| exactly_one_solid | solid_count = 1 | `validity` | 0 |
| U-02 / envelope_within_spec | sizes 232.0 × 215.0 × 19.0 each in [spec − 0.1, spec + 0.1]; position min/max x, y, z against ±116.0, 0 … 215.0, −302.0 … −283.0 (± 0.1) reported apart | `envelope` | 0.005 mm |
| U-03 (a) | panel to plate: clearance = 0 and common volume ≤ 0; footprint: area outside the plate's outline = 0, area over plate holes inside the outline = 0 ("wholly over plate material"), least distance from the footprint's edges to the outline ≥ 0.5; under each flange hole: a Ø3.4 × 6.0 plug on the hole's measured axis wholly in plate material (common volume = plug volume) and centre ≥ 6.0 from every existing plate hole centre; clearance panel to OD-C03, OD-H01, OD-C02 ≥ 20.0; common volume with each ≤ 0 | `clearance`, `common_volume`, `bore_census` (both parts), job code for the footprint | 0.005 mm; 0.001 mm³; area mm² band 0 |
| U-03 (b) | the panel moved +40.0 … 0 along Y in 2.0 steps (21 poses): common volume ≤ 0 with OD-C01, OD-C02, OD-C03, OD-H01 at every pose; worst pose reported | `common_volume` | 0.001 mm³ |
| U-04 | part: volume_delta in [0, 0], faces_delta = 0, solids = 1, valid_after = 1; assembly: 5 solids, labels kept, faces_delta = 0, per-child volume delta in [0, 0] | `compare_step` | 0.001 mm³; 0 |
| U-05 / feature_census | planar 46, cylindrical 19 (concave 19, convex 0), cone/sphere/torus/B-spline/other 0, bores 9; bores by axis and size: 4 Ø3.4 along Y through, 2 Ø4.0 along Y blind, 3 Ø12.0 along Z through; 10 R 2.0 slot-end faces; 1 wall, 2 flanges, 4 gussets, 1 ledge, 2 bosses by positional face readings (gusset hypotenuses 4, boss undersides 2, flange fronts 2, ledge underside pieces 3) | `feature_census`, `bore_census`, `locate_bore` | 0 |
| U-06 (Soft) | wide wall ≥ 2.0 | `min_wall_wide` (spacing 0.7) | 0.005 mm |
| U-07 | STL: angular tolerance ≤ 4·acos(1 − 0.01/6.0); max sagitta ≤ 0.01 measured on a fresh re-mesh of the re-imported STEP at the build's settings; mesh one closed body | `write_stl`, `mesh_census` | 0.005 mm; 0.00002 rad |
| U-08 | N/A by its row (no threads) | — | — |
| D-01a, D-01b, D-06a | min_wall ≥ 0.8, ≥ 2.0, ≥ 1.0 | `min_wall` (spacing 0.7) | 0.005 mm |
| D-02 | size_x ≤ 420, size_y ≤ 420 on the bed, size_z ≤ 500 tall (A-09) | `envelope` | 0.005 mm |
| D-03a | least overhang ≥ 45° outside the named exception: the six horizontal holes refilled by position (refilled solid 57 faces, one solid), census on it; the whole part's census and each exception crown's least angle reported apart | `overhang_census(build_dir=(0,0,1), spacing=0.7)` | 0.001 deg |
| D-03b | reviewer row; designer reading: widest horizontal hole ≤ 5.0 (bore census) and flat ceiling span ≤ 5.0 | `bore_census`, `flat_ceiling_spans(max_span=5.0)` | 0.005 mm |
| D-04a | the four flange holes Ø ≥ 3.25 | `locate_bore` | 0.005 mm |
| D-05a | across each insert bore along X and along Z ≥ 8.0, from rays at the bore's measured axis at mid-depth | `radial_extent` | 0.005 mm |
| D-05b | the two insert bores Ø in [3.95, 4.05], depth in [5.9, 6.1] and ≥ 5.7 | `locate_bore` | 0.005 mm |
| D-07 | N/A by its row | — | — |
| J-05 | material from each insert bore's wall ≥ 3.0 along +X, −X, +Z, −Z | `radial_extent` | 0.005 mm |
| E-06, E-11 | reviewer rows (sections); designer reading in the REPORT | — | — |
| REQ-01 | four Ø3.4 ± 0.1 holes along Y, offset ≤ 0.10, length 4.0 ± 0.1, through; underside one planar face at y 0.00 ± 0.10 | `locate_bore`, job code (planar faces at min y) | 0.005 mm; 0 |
| REQ-02 | outer face z −302.00 ± 0.10 and inner face z −299.00 ± 0.10 at y 50 and y 200 (rays along ±Z from z −300.5 at x −40, 0, +40); x ±116.0 ± 0.1 | `radial_extent`, `envelope` | 0.005 mm |
| REQ-03, REQ-04 | Ø12.0 ± 0.1 along Z, offset ≤ 0.10, through, at the three positions | `locate_bore` | 0.005 mm |
| REQ-05 | max_z ≤ −283.0; common volume of the box x ±70, y 0 … 100, z −299 … −250 with the panel = 0 | `envelope`, `common_volume` | 0.005 mm; 0.001 mm³ |
| REQ-06 | per slot: width 4.0 ± 0.1 and height 80.0 ± 0.1 from rays inside the slot at z −300.5 (±X at y 140; ±Y at the slot's centre x), centre x ± 0.1 and y ends 100.0 / 180.0 ± 0.1 | `radial_extent` | 0.005 mm |
| REQ-07 | two Ø4.0 ± 0.05 bores along −Y from y 215.0, depth 6.0 ± 0.1, offset ≤ 0.10, blind; the top one planar face at y 215.00 ± 0.10 spanning z −299 … −287 | `locate_bore`, job code (planar faces at max y) | 0.005 mm |
| REQ-08 | four Ø6.0 cylinders y 4 … 211 on the flange holes' nominal axes: common volume with the panel = 0 | `common_volume` | 0.001 mm³ |
| REQ-09 (Soft) | bench gate: INCONCLUSIVE by the row (A-11) | — | — |

Facts beside the gates (not gated): mass at 1270 kg/m³; the plate's edge distance from each new insert position (the brief asks for ≥ 8.0, which spec §5 does not state); a driver line tilted toward +Z past the ledge (REQ-08 stops at y 211, under the ledge); the STL's triangle count, volume and bounding box.

## 7. Risks

- The flanges (x ±(72 … 114), z −299 … −283) cover OD-C01's feet holes Ø3.4 at (±110, −295) (probe), so the footprint is not wholly over plate material and anything the feet fasten with on the plate's top face sits under the flange; U-03 (a) may fail on its own words. The spec fixes the flange's extent (§4), so the build keeps it and the REPORT reports what is measured.
- The top ledge (z −299 … −287) lies over all four flange screws (z −290): a straight driver from above meets the ledge; REQ-08 is written up to y 211 only. A tilted-driver reading is reported as a fact.
- REQ-08 at x ±81: the Ø6 cylinder is tangent to the bosses' faces x ±84; a tangent boolean may read a sliver. The clearance is reported beside it.
- The large wall faces may be refused by `min_wall` and `overhang_census` at spacing 0.7; then the gate is INCONCLUSIVE and the spacing that fits is named.
