# DESIGN_PLAN — od_c03_cradle (20260930-od-c03-pump-cradle, concept C1)

Designer: Claude Code (claude-opus-5-5), WP-02 J2 package, attempt 1 of 2 · spec version 1.0 · written before any geometry (D2)

Versions (D0): Python 3.13.7, build123d 0.11.1, OCP 7.9.3.1 (OCCT 7.9.3); repository commit 70826895ab7666f9e5aee3f77ce88f099995f3c1.
Inputs checked against the brief: all three SHA-256 values match.

**Status of this plan: BLOCKED by one spec conflict (§8, C-01).** The post as spec §4 states
it (6.0 wide along Z) with the strap slot as §4 and REQ-05 state it (6.0 clear along Z)
leaves no material beside the slot, so the post top above the slot is a separate body
(U-01 and `exactly_one_solid` fail by construction). Every other row below is complete;
§3, §4 and §6 mark the rows that change with the amendment.

## 1. Datum

The pump axis is at the origin with +Z along it because the spec (§2) makes the cradle's
frame identical to the OD-H01 STEP frame, so the check assembly is the identity overlay:
+Z toward the inlet hose fitting, X the normal of the frame's side plates, θ
counter-clockwise about +Z from +X, +Y down in the machine. The saddle arcs are centred
on this axis (the sleeve A-03 sits on the pump axis), and the foot's underside is the
plane y = +40.0 (REQ-08). The cradle is built directly in this frame; nothing is
moved after the build.

## 2. Library and tools (D1)

- Cards read: none. Finding: no card in `library/INDEX.md` matches a saddle cradle or
  strap retention for an imported cylindrical component; the heat-set card (UNO10 U5)
  is not relevant because the inserts are in OD-C01, not in this part.
- `tools/` functions reused:
  - `tools.core.read_step`, `validity`, `write_step` (AP242, D-024), `step_roundtrip`, `compare_step`, `write_stl`, `mesh_sagitta`, `common_volume`.
  - `tools.measure.envelope`, `feature_census`, `bore_census`, `locate_bore`, `min_wall`, `min_wall_wide`, `overhang_census`, `clearance`, `interference`, `radial_extent`, `radial_profile`, `mass_properties` (A-09 mass, information only).
  - `tools.result.gate` with the GATES.md §0 bands: 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts and 1/0 facts.
  - `tools.core.fillet_ladder`: not used (no fillets planned, §4 `fillet_r`).
- New code needed: none in the repo. Job-local helpers in `check_od_c03_cradle.py` only select faces (for example the post inner faces by normal and position) and pass them to `envelope`; they gate nothing on their own.

## 2a. D2 measurements of OD-H01 (probes, not deliverables)

Probe scripts and their output: `01_CAD/probes/probe_pump_frame_v01.py` (+ `.out.json`),
`01_CAD/probes/probe_frame_ends_v01.py` (+ `.out.json`). All values below are measured on
the B-rep of the input STEP.

| Quantity | Measured | How |
|---|---|---|
| `validity(OD-H01)` | solid_count 1, brep_valid 1, naked_edges 0: **sound**, so U-03's boolean on cradle|OD-H01 can run | `tools.core.validity` |
| OD-H01 envelope | x −27.20 … 26.85, y −31.40 … 23.75, z −66.45 … 55.50 | `envelope` |
| Side plates | **two**, not one: −X plate x −27.20 … −24.10 and +X plate x 23.75 … 26.85, each y −16.20 … 16.20, z −12.17 … 37.42 (bend tangents), 3.10 thick | thin-slab sections at z 3, 15, 27, 33; slab through each plate; rays at θ 0° and 180° |
| End plates | z −12.4 … −9.3 and 34.55 … 37.65, full width between the side plates, y ±16.2, outer bends R4.5 at all four XZ corners; notches 6.6 wide (y ±3.3) at z ≈ −9.2 … −8 in both side plates | sections at z −12.3 … −8.0 and 33.0 … 37.6 |
| Frame corners in the XY plane (rib planes) | (−27.20, ±16.20), (−24.10, ±16.20), (23.75, ±16.20), (26.85, ±16.20) | sections at z 0, 3, 6, 24, 27, 30 |
| Pump material at y > 16.2 (the cradle side) | the coil only: x −17.52 … 17.12, y ≤ 23.75, z −8.8 … 34.5 | slab x ±30, y 16.2 … 36.2, z −12.4 … 37.65 |
| Pump outer radius near the sector edges (z 3 and 27) | θ 40°: 23.56; 45°: 23.58; 90°: 23.75; 135°: 23.86; 140°: 23.87 (coil, centre off-axis); θ 30° and 150° read 31.00 and 31.41 (plate corners) | `radial_extent` outer |
| Clearance of the planned C1 volumes (spec §4 values) to OD-H01 | rib 1: 2.787 (to the coil at (−16.72, 17.03, 0.0)); rib 2: 2.787 (z 24.0); posts on −X: 2.300 (to the −X plate face x −27.20); posts on +X: 2.650 (to x 26.85); foot: 13.250 | `clearance` on probe solids |
| Assumed sleeve (A-03) against OD-H01 | common volume **4760.0 mm³**: the tube r 23.65 … 26.65, z −6 … 32 passes through both side plates (x 23.75 / 24.10 … 26.65) and the off-axis coil; not a §5 pair, reported for P6 | `common_volume` |

Answer to the brief: the spec's sector θ 45° … 135° and the post inner faces at |x| = 29.5
keep ≥ 2.0 to every part of the pump (least 2.300, posts on −X). No stop for the sector or
the posts. The spine question has a measured answer the spec did not expect: the frame
carries a side plate on **both** long X edges (A-04 says one); the governing plate for
the posts is the −X plate at x −27.20.

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Foot plate 80.0 × 3.0 × 50.0 (x ±40, y 37.0 … 40.0, z −10 … 40) | box from parameters | — | §4 C1, U-02, REQ-08 |
| F02 | Rib 1 with web (z 0.0 … 6.0) | XY profile extruded +Z by `rib_t`: inner arc r 26.65 over θ 45° … 135°, radial end faces at θ 45° and 135° from r 26.65 to 32.0, then vertical faces x = ±`r_out`·cos 45° (±22.627) down to the foot top y 37.0; fused to F01 | F01 | §4 C1, REQ-01, REQ-02, REQ-04 |
| F03 | Rib 2 with web (z 24.0 … 30.0) | the same profile, extruded from z 24.0; fused | F01 | §4 C1, REQ-01, REQ-02, REQ-04 |
| F04 | Four posts, x from ±29.5 to ±33.5, y 0.0 … 37.0 | box per post, Z extent per §4 (6.0, the rib's width) **or as amended (C-01)**; fused to F01 | F01 | §4 C1, REQ-06, U-05 |
| F05 | Four strap slots, one per post, through along X | cut: YZ profile of clear section `slot_w` (Z) × `slot_h` (Y) centred y 7.0, with a 45° gable roof (apex `slot_w`/2 above the clear top), extruded along X through the post | F04 | §4 C1, REQ-05, D-03a, D-03b |
| F06 | Four Ø3.4 through-holes along Y at (±34.0, z −4.0) and (±34.0, z 34.0) | cylinder cut through F01 along Y | F01 | §4 C1, REQ-07, D-04a |
| F07 | Check assembly: cradle + OD-H01 + sleeve solid | compound of three named parts, each at the identity pose | F01–F06 | U-03, REQ-03, REQ-04 |

No fillets or chamfers (stated choice, §4 `fillet_r`).

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| foot_x | 80.0 (x −40.0 … 40.0) | mm | U-02 ±0.1 | §4 C1, U-02 | no |
| foot_z0, foot_z1 | −10.0, 40.0 | mm | U-02 ±0.1 | §4 C1, U-02 | no |
| foot_y0, foot_y1 | 37.0, 40.0 (3.0 thick) | mm | REQ-08 ±0.1 | §4 C1, REQ-08, A-11 | yes (sweep 2.9 / 3.1 thickness, underside held at 40.0) |
| r_in (saddle) | 26.65 | mm | REQ-01 [26.60, 26.70] | §4 C1, A-03 (sleeve OD 53.3 / 2) | yes (sweep 26.60 / 26.70) |
| r_out (rib) | 32.0 | mm | — | §4 C1 | no |
| theta0, theta1 | 45.0, 135.0 | deg | REQ-02 | §4 C1, A-06; measured clearance 2.787 at nominal (§2a) | yes (sweep ±2°: 43/137 and 47/133; REQ-02 and REQ-03 re-read) |
| web_half_x | 22.627 | mm | — | derivation: r_out · cos 45°, so the web's side faces start at the rib's outer end corner and no material reaches θ < 45° within r ≤ 32.0 (REQ-02 at θ 40°) | no |
| rib_t | 6.0 | mm | REQ-02 ±0.10 | §4 C1 | no |
| rib1_z0, rib2_z0 | 0.0, 24.0 | mm | REQ-02 ±0.10 | §4 C1 | no |
| post_x_in | 29.5 | mm | REQ-06 ±0.1 | §4 C1, A-06; measured clearance 2.300 to the −X plate | yes (sweep 29.4 / 29.6) |
| post_t (X) | 4.0 | mm | — | §4 C1 | no |
| post_y_top | 0.0 | mm | — | §4 C1 (axis height) | no |
| post_w (Z) | **6.0 per §4: CONFLICT C-01** | mm | — | §4 C1 | — |
| slot_w (Z) × slot_h (Y) | 6.0 × 2.5 | mm | REQ-05 ≥ | §4 C1, REQ-05, A-07 | yes (sweep slot_h 2.5 / 2.7; slot_w 6.0 / 6.2 once C-01 allows) |
| slot_yc | 7.0 | mm | REQ-05 ±0.5 | §4 C1 | yes (sweep 6.5 / 7.5) |
| slot_roof | 45° gable, apex 3.0 above the clear top (y 2.75) | deg | D-03a ≥ 45 | §4 C1, A-13; derivation: a flat 6.0 roof would be a 6.0 bridge (D-03b ≤ 5) | no |
| hole_d | 3.4 | mm | REQ-07 ±0.1, D-04a ≥ 3.25 | §4 C1, REQ-07, A-11 | yes (sweep 3.3 / 3.5) |
| hole_xz | (±34.0, −4.0), (±34.0, 34.0) | mm | REQ-07 offset ≤ 0.10 | §4 C1, REQ-07, A-11 | no |
| fillet_r | none | mm | — | stated choice: §4 names no round; every gated face stays analytic and exact | no |
| sleeve (assumed OD-H02) | tube ID 47.3, OD 53.3, z −6.0 … 32.0, on the pump axis | mm | — | A-03, brief | no (it is the assumption itself) |
| stl_tol, stl_ang | 0.01, 0.1000 (= 4·acos(1 − 0.01/32.0) = 0.100003, taken at 0.1000) | mm, rad | U-07 | U-07 | no |
| density | 1270 | kg/m³ | — | §3, A-09 | no |

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-H01 pump | `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` (b05302af…3fb62) | its own datum frame, which spec §2 declares identical to the cradle frame; verified at D2: side plates at x −27.20 / 26.85 and coil top y 23.75 read in that frame (§2a) | RigidJoint at the origin, axis +Z, identity (brief) | nothing (≥ 2.0 clearance, REQ-03) |
| OD-H02 sleeve (assumed solid, named `od_h02_sleeve_assumed_A03`) | none: built in the check script from A-03 | the pump axis (origin, +Z) | RigidJoint at the origin, identity | the two saddle arcs (designed contact, REQ-04) |

## 6. Checks planned (D3)

All predicates in `01_CAD/check_od_c03_cradle.py`, each on the re-imported STEP; `validity` first; any exception or empty value gives INCONCLUSIVE. Bands per GATES.md §0.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | solid_count == 1 | `tools.core.solid_count` | 0 |
| U-01 | solid_count = 1, brep_valid = 1, naked_edges = 0 | `validity` | 0 |
| envelope_within_spec / U-02 | size_x, size_y, size_z in [79.9, 80.1], [39.9, 40.1], [49.9, 50.1]; position reported apart: min/max x vs ±40.0, y 0.0 … 40.0, z −10.0 … 40.0 | `envelope` | 0.005 mm |
| U-03 (a) | cradle|OD-H01: clearance ≥ 2.0 (REQ-03 governs) and interference ≤ 0 (OD-H01 measured sound, so the boolean runs); cradle|sleeve: clearance == 0 and interference ≤ 0; all on the check assembly as placed. PASS_ASSUMED A-01, A-03 | `clearance`, `interference` | 0.005 mm; 0.001 mm³ |
| U-03 (b) | no motion variable (ties not modelled): recorded N/A by the row | — | — |
| U-04 | re-read: schema AP242, solids 1, volume_delta 0, faces_delta 0, labels unchanged, valid after | `step_roundtrip` | 0.001 mm³; 0 counts |
| feature_census / U-05 | per-feature tally against §3: concave cylinders 6 (2 saddle arcs r 26.65, 4 bores Ø3.4), convex cylinders 0, bores 4 (`bore_census`), each hole located (`locate_bore`, through); planar faces: foot 6 + ribs 2 × 6 + posts and slots 4 × (5 + 5) = 58 at the amended post (C-01), re-tallied from the frozen feature list if the amendment changes a face; 2 ribs, 4 posts, 4 slots and 1 foot confirmed by face position (rib inner arcs at z 0…6 and 24…30, post inner faces at |x| 29.5, slot floors at y 8.25, foot underside at y 40.0) | `feature_census`, `bore_census`, `locate_bore` | 0 |
| U-06 (soft) | min_wall wide ≥ 2.0 | `min_wall_wide` | 0.005 mm |
| U-07 | STL written at tol 0.01, angular 0.1000 rad after clearing the cached triangulation; mesh_sagitta ≤ 0.01; triangle count recorded | `write_stl`, `mesh_sagitta` | 0.005 mm |
| U-08 | N/A by its row (no threads) | — | — |
| D-01a | min_wall ≥ 0.8 | `min_wall` (spacing 0.4, 25°) | 0.005 mm |
| D-01b | min_wall ≥ 2.0 | `min_wall` | 0.005 mm |
| D-02 | size_x ≤ 420, size_z ≤ 420, size_y (vertical, foot down) ≤ 500: PASS_ASSUMED A-10 | `envelope` | 0.005 mm |
| D-03a | least downward angle ≥ 45° printed along −Y (foot at y 40 on the bed) | `overhang_census(build_dir=(0,−1,0), min_deg=45)` | 0.001 deg |
| D-03b | largest unsupported bridge ≤ 5: none planned (slot roofs gabled); reviewer from sections | reviewer | — |
| D-04a | each frame hole diameter ≥ 3.25 | `locate_bore` diameter | 0.005 mm |
| D-04c | clearance cradle|OD-H01 ≥ 0.5 (REQ-03 raises to 2.0, gated there) | `clearance` | 0.005 mm |
| D-06a | min_wall ≥ 1.0 | `min_wall` | 0.005 mm |
| D-07 | N/A by its row | — | — |
| REQ-01 | inner radius about (origin, +Z, ref +X), θ 50 … 130 step 5, z bands (0.5, 5.5) and (24.5, 29.5), margin 0, z_step 0.1: min and max in [26.60, 26.70] | `radial_profile(side="inner")` | 0.005 mm |
| REQ-02 | z 3.0 and 27.0: `radial_extent` inner at θ 50° and 130° ≤ 26.70; at θ 40° and 140° with r_max 32.0 the expected reading is INCONCLUSIVE "no material", recorded as such (never counted as PASS by the script; the reviewer confirms from sections); positive control on the whole ray: first material at θ 40° / 140° is the post at r = 29.5 / cos 40° = 38.51; rib faces at z 0.0, 6.0, 24.0, 30.0 ± 0.10 from the envelopes of the rib side faces and from sections | `radial_extent`, `envelope` | 0.005 mm |
| REQ-03 | clearance(cradle, OD-H01) ≥ 2.0 with nearest points; predicted from D2 probes: 2.300 at the −X posts | `clearance` | 0.005 mm |
| REQ-04 | clearance(cradle, sleeve) == 0 with nearest points on a saddle arc (r 26.65, θ 45 … 135); interference ≤ 0 | `clearance`, `interference` | 0.005 mm; 0.001 mm³ |
| REQ-05 | per slot: envelope of the slot faces: clear Z ≥ 6.0, clear Y ≥ 2.5, centre y 7.0 ± 0.5, through along X (4 faces meet both post X faces); roof faces at 45° (D-03a); reviewer from sections | `envelope` on selected faces, `overhang_census` | 0.005 mm; 0.001 deg |
| REQ-06 | post inner face planes at |x| = 29.5 ± 0.1 (envelope of each face selected by normal ±X and position), and post clearance to OD-H01 ≥ 2.0 (inside REQ-03) | `envelope`, `clearance` | 0.005 mm |
| REQ-07 | four bores: Ø3.4 ± 0.1, axis ±Y, offset ≤ 0.10 from (±34.0, y, −4.0) and (±34.0, y, 34.0), through | `bore_census`, `locate_bore` | 0.005 mm |
| REQ-08 | max_y = 40.00 ± 0.10; foot thickness 3.0 ± 0.1 from the envelope of the foot top face (planar face, normal −Y, at y 37) against max_y; reviewer from sections | `envelope` | 0.005 mm |
| REQ-09 | bench gate, not geometric: INCONCLUSIVE until the first run (A-03, A-05) | — | — |

Sweep (D7) into `01_CAD/sweep_v01/`: the fit-critical rows of §4 at nominal, low and
high, each run one solid and the same predicates; no motion variable exists (U-03 b).
Sections (D6) at z 3.0 and z 27.0 (XY, through rib, web, posts and slots), x = 31.5 (YZ,
through the posts and slot profiles), and x = 34.0 (YZ, through the holes).

## 7. Risks

1. C-01 (§8) blocks the post and slot as written; nothing else in the plan depends on it except the plane tally in U-05.
2. The saddle arc and the sleeve's outer cylinder are coincident (both r 26.65 on the same axis): `common_volume` on coincident faces may read a small positive volume or fail. A D2 probe with a 64-chord polygon read 0.336 mm³ per rib, which is the chord error of the probe, not of the true arc. The build uses true arcs; if the boolean still reads > 0.001 mm³ the result is reported as measured, never hidden.
3. REQ-03 has 0.300 margin at the −X posts, less than the scan's p95 error (A-01, 0.448): a real frame could sit closer. Swept at post_x_in 29.4 / 29.6.
4. D-03a on the gable roof reads exactly 45.000°: a planar face has no sampling bound, but a value inside the 0.001° band is reported with its negative margin.
5. The assumed sleeve solid overlaps OD-H01 by 4760.0 mm³ (it passes through both side plates). Not a §5 pair; the check assembly will show it (P6 "embedded"). The real OEM sleeve cannot pass through the plates, so A-03's shape is likely wrong between the plates, not on the saddle sector (y > 18.8), which is clear of the plates.
6. Strap path (P2): at the rib 1 plane (z 0 … 6) the pump's −Y side carries the spade tabs (y to −30.95, z to 5.5) and the inclined slot box (z to 13.6), not only the terminal block that ends at z −3.3. A tie over rib 1 rides on the tabs rather than on the sleeve. Not a cradle gate (ties are not modelled); reported for A-07.
7. REQ-02's θ 40°/140° reading is INCONCLUSIVE by design; the script cannot turn it into a PASS, so that half of REQ-02 rests on the reviewer's sections.

## 8. Conflicts to resolve before J3

**C-01 — post width versus slot width (spec §4 C1, REQ-05).** The post is 6.0 wide along
Z and its through-slot along X has a clear width of 6.0 along Z. The ligament left on each
side of the slot is (6.0 − 6.0) / 2 = 0.0, against D-01b min_wall ≥ 2.0; the part of each
post above the slot (y 0.0 … 2.75 at the roof apex) is then a separate body, so U-01 and
`exactly_one_solid` fail by construction. A working post needs post_w ≥ slot_w + 2 × 2.0 = 10.0.
The designer does not change a spec value. Options for the spec amendment:

- (a) Post 10.0 wide centred on the rib (z −2.0 … 8.0 and 22.0 … 32.0). The hole edges
  (z −2.3, 32.3) then sit 0.3 from the post faces and an M3 screw head (Ø5.5, radius
  2.75) overlaps the post, so the holes must move (REQ-07, A-11), for example to
  z −6.0 and 36.0 (pattern 68.0 × 42.0; 2.3 wall to the foot ends).
- (b) Post 10.0 wide grown away from the hole only: rib 1 posts z 0.0 … 10.0, rib 2
  posts z 20.0 … 30.0, slots centred at z 5.0 and 25.0 (2.0 off each rib's centre
  plane). Holes and envelope unchanged; head-to-post gap stays 1.25 (as §4 today); the
  tie crosses the sleeve at a 2.0 axial offset from the saddle.
- (c) Keep post_w 6.0 and narrow the slot: not possible within REQ-05 (≥ 6.0) and D-01b;
  a slot of 2.0 would not pass the 4.8 tie (A-07).
