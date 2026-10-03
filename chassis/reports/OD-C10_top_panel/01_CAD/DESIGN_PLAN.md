# DESIGN_PLAN — od_c10_top (20261001-od-c10-top-panel, concept C1)

Designer: Claude Code (Claude Agent SDK), claude-opus-5-5 · spec version 1.1 · written before any geometry (D2)

Inputs probed (D2, measure only): `01_CAD/probe/probe_inputs_v01.py` -> `01_CAD/probe/probe_inputs_v01.json`.
Versions (D0): Python 3.13.7, build123d 0.11.1, OCP (cadquery-ocp-novtk) 7.9.3.1.1, repo commit
10929db1408d89144bd4af9cad971440427933d0.

## 1. Datum

The OD-C01 machine frame of spec §2, every reference at its stated placement: X to the
user's right, +Y up, +Z toward the front. The origin is the middle of the plate's top
face edge line x 0, y 0, z 0 because every neighbour (OD-C02, OD-C11, OD-C05, OD-C07) is
delivered or placed in that frame, so the lid's interfaces (insert axes, rail and ledge
tops, the carrier's plate top) are read in the same numbers the spec writes. The lid's top
face is the plane y 250.0; the print frame is the same solid turned upside down (build
direction −Y, A-08), never a second model.

Probed facts the plan rests on (probe JSON, all MEASURED):

| Reference | Measured as placed | Spec says |
|---|---|---|
| OD-C01 | one valid solid; x −120 … 120, z −305 … 100, top face y 0.0 (one face); four vertical R 10.0 arcs about (±110, −295) and (±110, 90) | §2 row 1: matches |
| OD-C02 (identity) | top-rail face y 215.0 over x 59.5 … 70.5, z −240 … −30; insert bores Ø4.0 × 6.0 blind along −Y from y 215 at (65, −60) and (65, −210), offset 0.000; envelope x 59 … 71 | §2 row 2, A-01: matches |
| OD-C11 v02 (identity, unreviewed) | top face y 215.0, one face over the wall x −116 … 116, z −302 … −299 and the ledge x −114 … 114, z −299 … −287; insert bores Ø4.0 × 6.0 blind at (±90, −293), offset 0.000; back face z −302.0 over x ±116, y 0 … 215 | §2 row 5, A-02: matches |
| OD-C05 (local x→X, y→+Z, z→−Y, origin (0, 180.06, 32.0)) | axes map as stated; plate top y 210.000 over x ±55, z −70 … 82; hub window Ø60.0 about (0, 32), through y 205 … 210; housing-screw counterbores Ø6.5 y 208 … 210 over Ø3.4 at (±44, −12) and (±44, 76) | §2 row 3, A-03: matches |
| OD-C07 (local x→−Z, y→−X, z→+Y, origin (−92, 0, −60)) | axes map as stated; one solid, x −117 … −67, y 0 … 48.0 (highest point), z −154 … −35 | §2 row 4, A-13: matches |

## 2. Library and tools (D1)

- Cards read: none. Finding: nothing in `library/INDEX.md` matches a lid that seats on
  another part's inserts through screw columns with counterbores (UNO10 U5's heat-set
  boss carries the insert itself; here the inserts are in OD-C02 and OD-C11).
- `tools/` functions reused: `tools.core.read_step` (inputs, re-import), `write_step`
  (AP242 part and assembly), `write_stl` (fresh mesh, measured sagitta), `validity`,
  `compare_step` (U-04), `common_volume` (interference, REQ-06, REQ-07, U-03 (b));
  `tools.measure.envelope`, `feature_census`, `bore_census`, `locate_bore`,
  `clearance`, `radial_extent`, `min_wall` and `min_wall_wide` (spacing 0.7: the
  default 0.4 refuses the 240 × 405 skin face), `overhang_census(build_dir=(0, −1, 0))`,
  `flat_ceiling_spans`, `mesh_census`, `mass_properties`; `tools.drawing.write_sections`.
- New code needed (job code in `01_CAD/`, never in the repo): a refill of the four
  counterbores by position for the D-03a census outside the named exception (the
  census takes no region); exclusion volumes by position (columns, pads, rear skirt)
  for U-03 (a)'s "away from the designed contacts" clearances; the contact patch of
  the skirt bottom on OD-C11's top face by face intersection. No `tools/measure`
  function is missing for a gate.

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Top skin y 247 … 250 over the outline x ±120, z −305 … 100, vertical corners R 10 | extrude of the rounded-rectangle sketch S1 (plane y 247) by 3.0 along +Y | — | §4 C1, REQ-01, REQ-02, U-02 |
| F02 | Perimeter skirt 3.0 thick, outer face on S1, y 215 … 247 | extrude of S1 minus its 3.0 inward offset (inner corners R 7 about the same centres) from y 215 by 32.0, union | F01 | §4, REQ-02, A-04 |
| F03 | Four screw columns Ø12.0, y 215 … 247, at (65, −60), (65, −210), (90, −293), (−90, −293) | cylinders along +Y, union | F01 | §4, REQ-03, REQ-04 |
| F04 | Bulkhead-column ribs: two per column along ±X, 3.0 thick about the column's z, right-triangle profile (vertical leg on the axis from y 247 down to 222.0, horizontal leg on the skin to 20.0 from the axis) | extrude of the triangle sketch by 3.0 (symmetric), union | F01, F03 | §4, E-06 |
| F05 | Rear-column ribs: two per column, parallel to Z, 3.0 thick, centred at x = xc ± 4.0; profile in the YZ plane: from 1.0 inside the rear skirt (z −303) to the column axis (z −293) at bottom y 216.0, then a hypotenuse up to the skin at z −273 | extrude of the quadrilateral sketch by 3.0 along X, union | F02, F03 | §4 (rear two into the rear skirt), E-06 |
| F06 | Two rest pads Ø10.0 at (±48, 30), y 210.5 … 247 | cylinders along +Y, union | F01 | §4, REQ-05, A-03 |
| F07 | Four Ø3.4 through-holes on the column axes, y 215 … 218 | cylinder cut (1.0 overshoot below y 215) | F03–F05 | REQ-03, REQ-04, D-04a |
| F08 | Four Ø6.5 counterbores from y 250 down to the floor y 218.0 | cylinder cut (1.0 overshoot above y 250) | F07 | REQ-03, REQ-04, REQ-07, A-05 |

Expected topology of the finished solid (U-05 census; derived from F01–F08):
planar 59 (top 1; outer skirt 4; inner skirt 4; skirt bottom 1; skin underside 3 = the
main face plus one pocket between each rear column's ribs; column bottoms 4;
counterbore floors 4; pad bottoms 2; bulkhead-rib sides 8 and hypotenuses 4; rear-rib
sides 16, bottoms 4, hypotenuses 4); cylindrical 22 (convex: 4 outer corners R 10,
4 columns R 6, 2 pads R 5; concave: 4 inner corners R 7, 4 holes R 1.7, 4 counterbores
R 3.25); cone, sphere, torus, B-spline 0; bores 8 (4 Ø3.4 through along Y, 4 Ø6.5 blind
along Y). If OCCT splits a periodic face on a boolean, the census reads it and the
REPORT says so (§8 deviation), never a re-count to fit.

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| x_half | 120.0 | mm | ±0.1 | §4 C1 skin; REQ-02; OD-C01 probe | no |
| z_min / z_max | −305.0 / 100.0 | mm | ±0.1 | §4; REQ-02 | no |
| corner_r | 10.0 | mm | ±0.1 | §4 (the plate's corners, probed R 10.0 about (±110, −295), (±110, 90)); REQ-02 | no |
| y_top | 250.0 | mm | ±0.1 | §2 frame; REQ-01 | no |
| skin_t | 3.0 | mm | ±0.1 | §4; REQ-01 (underside y 247.0) | no |
| skirt_t | 3.0 | mm | ±0.1 | §4; REQ-02 | no |
| skirt_inner_r | 7.0 | mm | — | derivation: corner_r − skirt_t about the same centres keeps the skirt 3.0 thick round the corner (REQ-02 "all round") | no |
| skirt_bottom_y | 215.0 | mm | ±0.1 | §4; REQ-02; A-04 | yes (meets OD-C11's wall top, U-03) |
| col_d | 12.0 | mm | ±0.1 | §4; REQ-03, REQ-04 | no |
| col_xz | (65, −60), (65, −210), (90, −293), (−90, −293) | mm | offset ≤ 0.10 | §4; REQ-03 (A-01), REQ-04 (A-02); probed insert axes | yes (coaxial with the inserts) |
| col_bottom_y | 215.0 | mm | ±0.05 | §4; REQ-03, REQ-04 (on OD-C02's rail and OD-C11's ledge, probed y 215.0) | yes (designed contact) |
| hole_d | 3.4 | mm | ±0.1; ≥ 3.25 | §4; REQ-03; D-04a; M3 clearance | yes |
| cbore_d | 6.5 | mm | ±0.1 | §4; REQ-03; REQ-07 (ISO 7380 head Ø5.7, A-05) | yes |
| cbore_floor_y | 218.0 | mm | ±0.1 | §4; REQ-03 (3.0 of column under the head; M3 × 8 reaches 5.0 into the 5.7 insert, A-05) | yes |
| pad_d | 10.0 | mm | ±0.1 | §4; REQ-05 | no |
| pad_xz | (±48.0, 30.0) | mm | offset ≤ 0.10 | §4; REQ-05 (A-03) | no (REQ-05 margins measured) |
| pad_bottom_y | 210.5 | mm | ±0.05 | §4; REQ-05 (0.5 above the probed plate top y 210.0, A-03) | yes |
| rib_t | 3.0 | mm | — | §4 (E-06) | no |
| rib_reach | 20.0 | mm | — | derivation: from the axis, 14.0 beyond the column's radius 6.0 along the skin; the bulkhead ribs toward −X end at x 45.0, outside REQ-06's box (|x| ≤ 42) by 3.0 | no |
| rib_root_y | 222.0 | mm | — | derivation: the bulkhead ribs' vertical leg 25.0 of the column's 32.0 (y 247 → 222), so the rib's lowest material (at the column surface, y ≈ 229.3) stays ≥ 7 above OD-C02's rail y 215 (U-03 ≥ 0.5) | no |
| rear_rib_bottom_y | 216.0 | mm | — | derivation: 1.0 above OD-C11's ledge top y 215.0 (U-03 (a) asks ≥ 0.5 away from the column bottoms; 0.5 of margin) | no |
| rear_rib_dx | 4.0 | mm | — | derivation: each rib's faces at 2.5 and 5.5 from the axis: inside the column's radius 6.0, so a rib face cuts the cylinder cleanly (at 6.0 it would be tangent) and both ribs pass the column on its flanks | no |
| rear_rib_z | −303.0 … −293.0 bottom edge, hypotenuse to −273.0 at the skin | mm | — | derivation: 1.0 into the rear skirt (z −305 … −302) so the union fuses; to the axis at the bottom; rib_reach forward along the skin | no |
| overshoot | 1.0 | mm | — | derivation: every cutter passes 1.0 beyond the free face it opens | no |
| stl_tol | 0.01 | mm | — | U-07 | no |
| stl_ang | 0.17 | rad | ≤ 4·acos(1 − 0.01/10.0) = 0.1789 | U-07, R_max = 10.0 (the outer corners) | no |
| density | 1270 | kg/m³ | — | §3 (PETG, A-10) | no |

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-C01 base frame | `00_Spec/inputs/OD-C01_base_frame.step` (7b5688af…5805) | identity (probed top face y 0.0, outline x ±120, z −305 … 100) | RigidJoint on the lid at the identity → the part's own frame | nothing (≥ 3.0, U-03) |
| OD-C02 bulkhead | `00_Spec/inputs/OD-C02_bulkhead.step` (1e36348a…4bdc) | identity (probed rail top y 215.0, insert axes (65, −60), (65, −210)) | RigidJoint at the identity | the two bulkhead columns' bottoms (contact), their holes coaxial with the inserts |
| OD-C05 carrier | `00_Spec/inputs/OD-C05_group_head_carrier.step` (7b3d33ad…a5f1) | OD-C01 A-01: local x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0); checked: plate top lands at y 210.000 | RigidJoint at `Location(Plane(origin=(0, 180.06, 32), x_dir=(1, 0, 0), z_dir=(0, −1, 0)))` | the pads, 0.5 above the plate top |
| OD-C07 valve mount | `00_Spec/inputs/OD-C07_valve_flowmeter_mount.step` (55c1c361…583c) | OD-C01 A-17: local x → −Z, y → −X, z → +Y, origin (−92, 0, −60); checked: highest point y 48.0 | RigidJoint at `Location(Plane(origin=(−92, 0, −60), x_dir=(0, 0, −1), z_dir=(0, 1, 0)))` | nothing (≥ 3.0) |
| OD-C11 back panel v02 (unreviewed) | `00_Spec/inputs/OD-C11_back_panel_v02.step` (80803f53…6235) | identity (probed top face y 215.0, insert axes (±90, −293), back face z −302) | RigidJoint at the identity | the two rear columns' bottoms on the ledge (contact), their holes coaxial with the inserts; the rear skirt's bottom inner edge on the wall's top outer edge (line contact, U-03 (a) 1.1) |

## 6. Checks planned (D3)

Every row reads the re-imported STEP (`02_STEP_STL/od_c10_top_C1_v01.step`) and the
check assembly STEP; band from GATES.md §0: mm 0.005, mm³ 0.001, deg 0.001, rad
0.00002, counts and every other unit 0.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | `validity` | 0 |
| exactly_one_solid | 1 solid | `validity` (solid_count) | 0 |
| U-02 / envelope_within_spec | sizes 240.0 × 39.5 × 405.0 each ±0.1; position x ±120.0, y 210.5 … 250.0, z −305.0 … 100.0 reported apart | `envelope` | mm |
| U-03 (a) | clearance 0 and common volume ≤ 0 at the four column seats; hole axis offset from the insert bore ≤ 0.10 (`locate_bore` on the lid's census and on OD-C02's / OD-C11's census at the lid hole's measured axis point); clearance(lid, OD-C05) in 0.45 … 0.55 with the nearest point on a pad, and clearance(lid less the pads, OD-C05) ≥ 0.5; clearance to OD-C07 ≥ 3.0 and to OD-C01 ≥ 3.0; clearance(lid less the four column volumes (r 6.05), OD-C02) ≥ 0.5; clearance(lid less the column volumes and the rear skirt slab z ≤ −301.95, OD-C11) ≥ 0.5; rear skirt line contact: clearance(lid, OD-C11) = 0 and common volume ≤ 0 with the contact faces and their area by face intersection reported | `clearance`, `common_volume`, `bore_census`, `locate_bore` | mm, mm³ |
| U-03 (b) | the lid moved +40.0 … 0 along Y in 21 steps of 2.0: common volume ≤ 0 with every reference at every step (references cropped to y ≥ 200 near the lid, a crop that holds the lid's whole swept box) | `common_volume` | mm³ |
| U-04 | part and assembly round trip: schema AP242, solids, volume_delta 0, faces_delta 0, labels, valid after | `compare_step` | per unit |
| U-05 / feature_census | faces per kind against §3's expected topology; bores 8 (4 Ø3.4 through, 4 Ø6.5 blind, all along Y); by position: 1 top face at y 250, 1 skirt bottom face at y 215 spanning the outline, 4 column cylinders R 6, 2 pad cylinders R 5, 12 rib side planes … (rib faces 36 in all) | `feature_census`, `bore_census`, `locate_bore` | 0 |
| U-06 (Soft) | min_wall wide ≥ 2.0 | `min_wall_wide` (spacing 0.7) | mm |
| U-07 | STL tolerance 0.01, angular 0.17 ≤ 0.1789; measured sagitta ≤ 0.01 on a fresh mesh of the re-imported STEP; mesh census one closed shell | `write_stl`, `mesh_census` | mm, rad |
| U-08 | N/A by its row (no threads) | — | — |
| D-01a | min_wall ≥ 0.8 | `min_wall` (spacing 0.7) | mm |
| D-01b | min_wall ≥ 2.0 | `min_wall` (spacing 0.7) | mm |
| D-02 | envelope sizes on the bed (x 240, z 405 ≤ 420) and tall (y 39.5 ≤ 500) | `envelope` | mm |
| D-03a | least overhang ≥ 45° with the four counterbores refilled by position (Ø6.5 + 0.2 from y 217.9 to 250); whole-part census and the exception floors' area reported apart | `overhang_census(build_dir=(0, −1, 0), spacing 0.7)` | deg |
| D-03b | designer reading: widest flat ceiling ≤ 5 (only the counterbore floors expected); the row is the reviewer's from sections | `flat_ceiling_spans(build_dir=(0, −1, 0), max_span 5, spacing 0.7)` | mm |
| D-04a | four column holes Ø ≥ 3.25 | `bore_census`, `locate_bore` | mm |
| D-05a, D-05b, D-07, J-05 | N/A by their rows | — | — |
| D-06a | min_wall ≥ 1.0 | `min_wall` | mm |
| E-06 | reviewer row from sections; designer evidence: one solid, rib faces by position at each column, pads fused to the skin | sections; `feature_census` | — |
| REQ-01 | one planar face at max y, y 250.00 ± 0.10; skin 3.0 ± 0.1: rays up and down from y 248.5 at five open points of the skin (top 250, underside 247) | `envelope`, `radial_extent` | mm |
| REQ-02 | envelope x ±120.0, z −305.0 / 100.0 ± 0.1; corners: outer radius 10.0 ± 0.1 from each centre at 15°, 45°, 75° (rays at y 230); skirt 3.0 ± 0.1 at the corners (inner 7.0) and on each side (rays at y 230); skirt bottom face y 215.00 ± 0.10 | `envelope`, `radial_extent` | mm |
| REQ-03, REQ-04 | per column: Ø12.0 ± 0.1 (cylinder face radius and rays at y 215.5); axis offset ≤ 0.10; bottom y 215.00 ± 0.05; hole Ø3.4 ± 0.1 through, coaxial with the insert (offset ≤ 0.10); counterbore Ø6.5 ± 0.1 open at y 250, floor y 218.0 ± 0.1 | `bore_census`, `locate_bore`, `radial_extent` | mm |
| REQ-05 | per pad: Ø10.0 ± 0.1; offset ≤ 0.10 from (±48, 30); bottom y 210.50 ± 0.05; clearance(pad, OD-C05) 0.50 ± 0.05; pad edge to hub window centre r ≥ 40.0; pad edge to each housing-screw counterbore edge ≥ 20.0 (centres and radii measured on OD-C05) | `clearance`, `bore_census`, `locate_bore` | mm |
| REQ-06 | common volume(lid, box x ±42, y 200 … 247, z −70 … 70) = 0 | `common_volume` | mm³ |
| REQ-07 | per screw: counterbore Ø6.5 open at y 250 down to its floor (locate_bore length 32.0); common volume(lid, Ø6.0 driver from y 218.05 to 260 on the nominal axis) = 0 | `locate_bore`, `common_volume` | mm, mm³ |
| REQ-08 (Soft) | bench gate: INCONCLUSIVE by its row | — | — |

## 7. Risks

1. **U-03 (a) at OD-C11's wall corners.** §4's outline (R 10 about (±110, −295)), the
   3.0 skirt with its bottom at y 215 and OD-C11's wall top (x ±116, z −302 … −299,
   y 215) overlap in plan over x 110 … 116 near each rear corner: the skirt's corner
   arc (r 7 … 10 about the corner centre) lies over the wall top there, so the lid
   bears on the wall over two small patches (≈ 5.9 mm² each by calculation) as well as
   along the line §5 names. Nothing in §4 lets the skirt avoid it (thickness, radius
   and bottom height are all REQ-02 values). The check measures it; if it reads as
   contact off the named line, it is reported as the measured failure (D9) with the
   options.
2. The rear ribs leave a closed pocket 5.0 wide between them, behind each rear
   column (open downward, toward OD-C11's ledge): printable upside down (it opens
   away from the bed), but a dirt trap; noted, not a gate.
3. Run time: the 240 × 405 skin at min_wall spacing 0.7 and the descent's 21 × 5
   booleans; the references are cropped near the lid and the sweep runs the quick
   check where a parameter cannot move a wall.
4. Fit-critical contacts (column bottoms, skirt bottom) pass only at nominal by their
   nature (clearance = 0 is exact); the sweep reports that, it is not hidden.
