# DESIGN_PLAN — od_c14_grommet_half (20261002-od-c14-cord-grommet, concept C1)

Designer: Claude Code, claude-opus-5-5 · spec version 1.0 (ratified 2026-10-02) · written before any geometry (D2) · brief WP-02 (J2 package, attempt 1 of 2)

Versions (D0): Python 3.13.7, build123d 0.11.1, OCP 7.9.3.1, repo commit 10929db1408d89144bd4af9cad971440427933d0.
Input hashes checked against the brief: OD-C11_back_panel.step 8ac0df9c…0d33db and OD-C01_base_frame.step 7b5688af…195805 both match.

D1 measurement scripts (diagnostics only, they gate nothing): `01_CAD/d1_measure_interfaces.py`, `01_CAD/d1_measure_interfaces_b.py`.

## 0. Interfaces measured at D1 (from the B-rep of the input STEPs)

| Quantity | Measured | Spec §2 | Agrees |
|---|---|---|---|
| OD-C11 validity | 1 solid, brep_valid 1, naked edges 0 | — | — |
| Cord hole (`locate_bore` near (95, 30, −300.5) along Z) | Ø12.000, axis (95.000, 30.000) along Z, offset 0.000, z −302.000 … −299.000, length 3.000, through | Ø12.0 at (95, 30), through | yes |
| Wall faces | outer face plane z −302.000 (normal −Z), inner face plane z −299.000 (normal +Z), both continuous over x −116 … 116, y 0 … 215 | 3.0 wall, z −302 / −299 | yes |
| Right floor flange | x 72.0 … 104.0, y 0.0 … 4.0, z −299.0 … −277.0; two Ø3.4 holes along Y at (81, −282) and (95, −282) | x 72 … 104, y 0 … 4, z −299 … −277 | yes |
| Outer gusset | x 100.0 … 104.0, sloping face from y 4 at z −283 to y 22.0 at the wall (z −299) | x 100 … 104 to y 22 | yes |
| Inner gusset (not named in §2) | x 72.0 … 76.0, sloping face from y 4 at z −283 to y 34.0 at the wall | — | finding, no conflict (19 mm from the axis in X) |
| OD-C01 | y −6.0 … 0.0 (top face y 0), z −305.0 … 100.0, x −120 … 120 | top y 0, rear edge z −305 | yes |
| Probe: neck/groove/collar envelope Ø11.4, z −299.2 … −291 to OD-C11 | 0.300 at (100.7, 30, −299.2) | 0.30 (D-04d) | yes |
| Probe: inside body to the floor flange and gussets | 3.734 at (98.02, 25.17, −299.0) | ≥ 0.5 | yes |
| Probe: tie ring Ø10.2/12.8, z −299.0 … −294.2, to the floor flange and gussets | 3.034 at (98.39, 24.57, −299.0) | ≥ 0.5 | yes |
| Probe: tie ring to OD-C11 | 0.000 at the inner face (designed contact) | 0 | yes |
| Probe: tie ring to OD-C01 | 23.6 | ≥ 10 | yes |
| Probe: Ø20 flange disc to OD-C01 | 20.0 (the lower half's flange at y 20.0) | ≥ 10 | yes |
| Probe: tie head box 5 × 5 × 5 above the band at +Y, its Z span starting at z −299.1 / −299.0 / −298.5 | 0.000 / 0.000 / 0.500 to OD-C11's inner face | ≥ 0.5 (REQ-04) | **no, see §7 Q2** |

## 1. Datum

The part is modelled in the spec's frame, the OD-C01 machine frame (X right, +Y up,
+Z front, plate top y 0), so that it, OD-C11, and OD-C01 share one frame at the
identity. It is built in a local frame and placed by one joint:

- Local origin: the point where the cord hole's axis crosses the wall's outer face,
  because that is the functional seat (the flange's inner face bears there and the
  axis is what both halves share). Local +Z along the hole axis, pointing into the
  machine. Local Y = machine Y (the split direction).
- Placement: `Location((x_h, y_h, z_h))` with `(x_h, y_h, z_h)` the `start` point of
  the bore `locate_bore` returns on OD-C11 (measured (95.000, 30.000, −302.000))
  and the axis direction from that bore (measured (0, 0, 1)); no rotation, because
  the measured axis is parallel to machine Z (checked, not assumed: the check
  script refuses an axis more than 1e-6 off Z).

## 2. Library and tools (D1)

- Cards read: none. **Nothing matched** (finding): no card covers a revolved split
  grommet, a cable-tie seat, or a two-half clamp; the nearest, UNO10 U5 (bore and
  chamfer), is a boss in a box and adds nothing the profile here needs.
- Traps read in `library/BUILD123D-NOTES.md`: `export_step()` never used
  (AP214, header); `export_stl()` relative tolerance; `split(..., keep=Keep.TOP)`
  keeps the side the plane normal points to (used with normal +Y to keep y ≥ 30.4).
- `tools/` functions reused:
  - `tools.core.read_step`: OD-C11, OD-C01, and the re-imported half.
  - `tools.core.validity` (solid_count, brep_valid, naked_edges): U-01, exactly_one_solid.
  - `tools.core.write_step` (AP242), `step_roundtrip` / `compare_step`: U-04.
  - `tools.core.write_stl`, `mesh_sagitta`: U-07.
  - `tools.core.common_volume` through `tools.measure.interference`: U-03.
  - `tools.measure.bore_census`, `locate_bore`: the joint (§1, §5), J-06.
  - `tools.measure.feature_census`: U-05, feature_census.
  - `tools.measure.envelope`: U-02, D-02, REQ-01 z spans, REQ-03, REQ-04, envelope_within_spec.
  - `tools.measure.radial_extent`, `radial_profile`: REQ-01 diameters and coaxiality, REQ-02 bore radius and chamfers, U-03 squeeze.
  - `tools.measure.clearance`: U-03, D-04d, REQ-04.
  - `tools.measure.min_wall`, `min_wall_wide`: D-01a, D-01b, D-06a, U-06.
  - `tools.measure.overhang_census`: D-03a.
  - `tools.measure.flat_ceiling_spans`: D-03b corroboration (the gate itself is the reviewer's, from sections).
  - `tools.measure.mesh_census`, `min_wall_mesh`: corroboration only (D-025).
  - `tools.drawing.write_sections`, `nothing_clipped`: D6 sections.
  - `tools.result.gate`: every comparison, band from GATES §0.
- New code needed: none in the repo. Job-local helpers in the check script only:
  a half-space clip (the half intersected with a box) to separate the designed
  flange contact from the neck-to-hole clearance (`clearance` returns one minimum
  per pair), and the cord, tie, and head-zone envelopes.

## 3. Feature order

Local z below (0 = wall's outer face, machine z = local z − 302.0). The whole
grommet is one closed profile in the (r, z) half-plane, revolved 360° about local
Z; the seam lies in the half-plane at ±X (machine y 30.0), which the split removes,
so each revolved surface comes back as one face.

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Profile sketch S1 (r, z): outer boundary flange r 10.0 z −2.0 … 0, neck r 5.7 z 0 … 2.8, step to groove r 5.1 z 2.8 … 8.0, flank r 5.1 → 5.7, collar r 5.7 to z 11.0; inner boundary bore r 3.5 with the outside chamfer (r 3.79 at z −2.0 to r 3.5 at z −1.5) and the inside chamfer (r 3.5 at z 10.5 to r 4.0 at z 11.0) | polyline in the XZ plane, closed | — | §4 C1, REQ-01, REQ-02 |
| F02 | Flange Ø20.0 × 2.0 | part of the revolve of S1 | F01 | §4, REQ-01, U-05 |
| F03 | Neck Ø11.4 × 2.8 | part of the revolve of S1 | F01 | §4, REQ-01, D-04d |
| F04 | Tie groove Ø10.2, 5.2 wide | part of the revolve of S1 | F01 | §4, REQ-01, REQ-04, D-01b |
| F05 | Collar flank, 60° (see §7 Q1) | conical segment of the revolve of S1 | F01 | §4, REQ-01, D-03a |
| F06 | Collar Ø11.4 to z 11.0 (machine −291.0) | part of the revolve of S1 | F01 | §4, REQ-01 |
| F07 | Bore Ø7.0 through | inner boundary of S1 | F01 | §4, REQ-02 |
| F08 | Inside bore chamfer 0.5 × 45° | inner boundary vertex of S1 | F07 | §4, REQ-02, E-11 |
| F09 | Outside bore chamfer 0.50 axial × 0.29 radial | inner boundary vertex of S1 | F07 | §4, REQ-02, E-11, D-03a |
| F10 | Whole grommet `whole` | `revolve(S1, Axis.Z, 360)` | F01–F09 | §4 |
| F11 | The half `half_local` | `split(whole, bisect_by=Plane(origin=(0, 0.4, 0), z_dir=(0, 1, 0)), keep=Keep.TOP)`: the split face y 30.4 | F10 | §4, REQ-02, A-05, U-05 |
| F12 | Placement `half` | `Location(hole start)` from `locate_bore` on OD-C11 | F11 | §1, §2 |
| F13 | Copy `half_b` (check assembly only) | `half` rotated 180° about the measured hole axis | F12 | §2, REQ-03, U-03 |
| F14 | Check assembly | OD-C11, OD-C01 (identity), `half`, `half_b`, cord envelope (Ø7.0 on the axis, z −330 … −260), tie envelope (ring Ø10.2/12.8, z −299.0 … −294.2, its z from the measured inner face) | F12, F13 | §1 deliverables, U-03 |

No fillets: the spec names none, so no fillet ladder runs; edges stay sharp except
the two bore chamfers. Printing: standing on the flange's outer face (A-06).

## 4. Parameters

All in mm, local frame (machine z = local z − 302.0). Sweep range (D7) for each
fit-critical row = the REQ-01 / REQ-02 tolerance of that row (derivation: the
spec's own band is the variation it accepts).

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| hole_axis | (95.000, 30.000) along Z | mm | — | measured on OD-C11 (`locate_bore`); §2, A-01 | — (input) |
| wall_outer_z / wall_inner_z | −302.000 / −299.000 | mm | — | measured on OD-C11; §2 | — (input) |
| hole_d | 12.000 | mm | — | measured; §2, A-01 | — (input) |
| flange_d | 20.0 | mm | ± 0.1 | §4, REQ-01 | no |
| flange_t | 2.0 (local z −2.0 … 0) | mm | ± 0.1 | §4, REQ-01 | no |
| neck_d | 11.4 | mm | ± 0.05 | §4, REQ-01; D-04d (12.0 − 2 × 0.30) | yes |
| neck_len | 2.8 (local 0 … 2.8, machine −302.0 … −299.2) | mm | ± 0.1 | §4, REQ-01 | yes (the groove's outer side and the tie on the wall) |
| groove_d | 10.2 | mm | ± 0.05 | §4, REQ-01, D-01b (2 × (3.5 + 1.6)) | yes |
| groove_w | 5.2 (local 2.8 … 8.0, machine −299.2 … −294.0) | mm | ± 0.1 | §4, REQ-04 (4.8 tie + 0.4) | yes |
| flank_angle | 60° from horizontal (see §7 Q1) | deg | ± 1° | §4, REQ-01, D-03a | no |
| flank_h | 0.346 per §4 text, or 1.039 for 60° from horizontal (see §7 Q1) | mm | ± 0.1 | §4 vs D-03a | no |
| collar_d | 11.4 | mm | ± 0.05 | §4, REQ-01, D-04d | yes |
| collar_top_z | 11.0 (machine −291.0) | mm | ± 0.1 | §4, REQ-01 | no |
| bore_d | 7.0 (r 3.50) | mm | r ± 0.05 | §4, REQ-02, A-02 | yes |
| chamfer_in | 0.5 × 45° (r 3.5 → 4.0 over local 10.5 … 11.0) | mm | ± 0.1 | §4, REQ-02 | no |
| chamfer_out | 0.50 axial × 0.29 radial (r 3.79 at local −2.0 → 3.5 at −1.5; atan(0.50/0.29) = 59.9° from horizontal) | mm | ± 0.1 | §4, REQ-02 | no |
| split_y | +0.40 local (machine y 30.40) | mm | ± 0.02 | §4, REQ-02, A-05 | yes |
| cord_d | 7.0 | mm | — | §2, A-02 (check envelope only) | — |
| tie_ring | Ø10.2 in, Ø12.8 out, z −299.0 … −294.2 | mm | — | §5 U-03, A-04 (check envelope only) | — |
| tie_head_zone | 5 × 5 × 6 above the band at +Y (axis assignment and Z position: §7 Q2) | mm | — | §5 REQ-04, A-04 | — |
| stl_tol / stl_ang | 0.01 / 0.10 rad (limit 4·acos(1 − 0.01/10.0) = 0.1789 rad) | mm, rad | — | §5 U-07 | — |
| path_steps | 20.0 → 0 in 2.0 steps (11 poses) | mm | — | §5 U-03 (c) | — |
| close_shift | 0.4 per half toward the axis along Y | mm | — | §2, §5 U-03 (b) | — |

Derived values the checks will compare (arithmetic, not measured yet):
- The half's X extent is at its split face: 2·√(10.0² − 0.4²) = 19.984 (U-02, REQ-03 within ± 0.1), position x 85.008 … 104.992.
- Neck to hole at the closed pose: 6.0 − √(5.7² − 0.4²) = 0.314 (U-03 b, ≥ 0.30).
- Groove floor wall: 5.1 − 3.5 = 1.600 (D-01b at zero margin).
- Half-bore arc 180° − 2·asin(0.4/3.5) = 166.9° < 180°, so `bore_census` reads 0 bores and the bore counts as 1 concave cylinder.

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-C11 back panel | `00_Spec/inputs/OD-C11_back_panel.step` (8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db) | identity (spec §2); its cord hole located by `locate_bore` | fixed (identity) | the half's flange face (outer wall face), neck (hole), tie envelope (inner wall face) |
| OD-C01 base frame | `00_Spec/inputs/OD-C01_base_frame.step` (7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805) | identity (spec §2) | fixed (identity) | none (clearance ≥ 10 only) |
| od_c14_grommet_half (upper) | built | local origin = measured hole `start` (wall outer face on the axis) | RigidJoint at the hole start, axis = measured bore axis | OD-C11 hole and outer face; cord envelope |
| od_c14_grommet_half (lower copy) | same solid | the measured hole axis | the upper half rotated 180° about the measured axis | the upper half (0.8 gap open, 0 closed) |
| Cord envelope | built in the check script | the measured hole axis | coaxial | both half-bores (tangent at the open pose) |
| Tie envelope | built in the check script | the measured axis and the measured inner face z | coaxial, its outer-side face on the inner face | both groove floors, OD-C11 inner face |

Closed pose: each half moved 0.4 along Y toward the axis. Path: both halves at the
open pose moved by −20.0, −18.0, … 0 along the measured axis.

## 6. Checks planned (D3)

Band (GATES §0, L-21): 0.005 mm for lengths; 0.001 for degrees and mm³; 0 for
counts and 1/0 facts. Every check re-imports `02_STEP_STL/od_c14_grommet_half_C1_v01.step`;
the assembly checks place that re-imported solid. Any exception or missing value
gives INCONCLUSIVE.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | solid_count == 1 on the re-imported half | `tools.core.validity` | 0 |
| U-01 | solid_count = 1, brep_valid = 1, naked_edges = 0 | `tools.core.validity` | 0 |
| U-02 | size_x, size_y, size_z each in [spec − 0.1, spec + 0.1] of 20.0, 9.6, 13.0; min/max x, y, z reported apart against x 85.0 … 105.0, y 30.4 … 40.0, z −304.0 … −291.0 (predicted x 85.008 … 104.992) | `envelope` | 0.005 |
| envelope_within_spec | as U-02, size and position as separate results | `envelope` | 0.005 |
| U-03 (a) | designed contacts = 0 and interference ≤ 0: flange region (half ∩ z ≤ −301.9) to OD-C11, each half's bore to the cord, tie to each groove floor, tie to OD-C11; half ∩ z ≥ −301.9 to OD-C11 ≥ 0.30; half to half 0.80 ± 0.05; half and tie to OD-C11 ∩ z ≥ −298.99 (floor flange, gussets) ≥ 0.5; half and tie to OD-C01 ≥ 10; tie outer Ø (envelope) > 12.0 | `clearance`, `interference`, `envelope` | 0.005 mm; 0.001 mm³ |
| U-03 (b) | closed pose: half to half clearance = 0 and interference ≤ 0; half ∩ z ≥ −301.9 to OD-C11 ≥ 0.30 (predicted 0.314); squeeze = 3.50 − inner radius of each moved half at 90° / 270° from +X about the cord axis, 0.40 ± 0.05 | `clearance`, `interference`, `radial_extent(side="inner", r_min=0)` | 0.005 mm; 0.001 mm³ |
| U-03 (c) | 11 poses, offsets −20.0 … 0 step 2.0 along +Z: interference of each half against OD-C11 and OD-C01 ≤ 0 at every step; worst step reported | `interference` | 0.001 mm³ |
| U-04 | named body re-read unchanged: volume_delta 0, faces_delta 0, labels unchanged, valid_after 1, one solid, no stray shells | `tools.core.step_roundtrip` / `compare_step` | 0.001 mm³; 0 counts |
| U-05 / feature_census | planar 6 (flange bottom, flange top, groove step at z −299.2, collar top, split face as 2 coplanar faces at y 30.40, see §7 Q3), cylindrical 5 (convex 4: flange, neck, groove floor, collar; concave 1: half-bore), conical 3 (flank, both chamfers), every other kind 0, bores 0; total 14; plus each face's plane / radius matched to its feature with `radial_extent` | `feature_census`, `radial_extent` | 0 |
| U-06 | `min_wall` `detail["wide"]` ≥ 1.6 | `min_wall`, `min_wall_wide` | 0.005 |
| U-07 | STL at tolerance 0.01, angular 0.10 rad ≤ 0.1789; max sagitta ≤ 0.01; triangle count recorded; `mesh_census` corroborates | `tools.core.write_stl`, `mesh_sagitta`, `mesh_census` | 0.005 |
| U-08 | N/A by its row (no threads) | — | — |
| D-01a | min_wall ≥ 0.8 | `min_wall` | 0.005 |
| D-01b | min_wall ≥ 1.6 (predicted 1.600 at the groove floor) | `min_wall` | 0.005 |
| D-02 | size 20.0 × 9.6 × 13.0 within 220 × 220 × 250 standing on the flange, PASS (assumed: A-07) | `envelope` | 0.005 |
| D-03a | least downward angle ≥ 45°, build_dir (0, 0, 1), the half oriented with the flange's outer face down (machine frame as built, since the part is already +Z up from the flange) | `overhang_census` | 0.001 deg |
| D-03b | bridge span ≤ 5; reviewer gate from sections; corroborated by `flat_ceiling_spans(max_span=5)` (predicted 0, nothing flat overhead) | `flat_ceiling_spans` | 0.005 |
| D-04d | neck and collar to the Ø12.0 hole ≥ 0.30 per side, open pose: clearance(half ∩ z ≥ −301.9, OD-C11) and 6.000 − `radial_profile` max over the neck band z −302 … −299.2; collar along the path (its pass through the hole) from U-03 (c) poses | `clearance`, `radial_profile` | 0.005 |
| D-06a | min_wall ≥ 1.0 | `min_wall` | 0.005 |
| D-07 | N/A by its row | — | — |
| J-06 | printed threads none: `bore_census` 0 and no B-spline or other helical faces in `feature_census` | `bore_census`, `feature_census` | 0 |
| E-11 | reviewer, from sections: squeeze (U-03 b), tie on the inner face, flange on the outer face, both chamfers present; designer supplies sections and the measured values | sections; `radial_extent`, `clearance` | — |
| REQ-01 | outer radius by `radial_profile` over angles 10° … 170° (the half's arc, ref +X, axis = cord axis) at levels inside each band: flange 10.0 ± 0.05 r (Ø ± 0.1), neck 5.70 ± 0.025, groove 5.10 ± 0.025, collar 5.70 ± 0.025; each band's z ends from `envelope` of the half and radial jumps (± 0.1); flank angle from two `radial_extent` readings across the flank, 60° ± 1°; coaxiality: max − min of each band's radius over angles ≤ 0.05 | `radial_extent`, `radial_profile`, `envelope` | 0.005 mm; 0.001 deg |
| REQ-02 | bore radius 3.50 ± 0.05 (`radial_extent(side="inner")` at 90° and at 20°, 160°, mid-length); split face: planar faces at y with min_y of the half = 30.40 ± 0.02; chamfers: inner radius at the inside end (4.0 → 0.5 radial) and the outside end (3.79 → 0.29 radial), each ± 0.1, with their axial lengths | `radial_extent`, `envelope`, `feature_census` | 0.005 |
| REQ-03 | union of the half and its 180° copy at the closed pose: size_x 20.0 ± 0.1 (predicted 19.984), size_y 20.0 − 0.8 = 19.2 ± 0.1, size_z 13.0 ± 0.1 | `envelope` | 0.005 |
| REQ-04 | groove floor width 5.2 ± 0.1 (z ends of the groove-floor cylinder face); tie outer Ø 12.8 > 12.0; head-zone box to OD-C11 ≥ 0.5 (placement per §7 Q2) | `envelope`, `clearance` | 0.005 |
| REQ-05 | Soft, bench: INCONCLUSIVE with a risk rating (medium: PLA halves stiff, squeeze all from the tie, A-03, A-05) | — | — |

Sections planned (D6, J3): YZ through the axis (x 95.0), XZ at y 32.0 (across the
half, parallel to the split), XY at z −296.6 (across the groove and tie), each
with OD-C11 and the cord and tie envelopes; `nothing_clipped` on each.

Sweep planned (D7): nominal, low, high of neck_d, neck_len, groove_d, groove_w,
collar_d, bore_d, split_y, one at a time for geometry (no motion variables; the
assembly path is swept at every pose of each run). Predicted at the band ends:
D-04d 0.275 at neck_d / collar_d high (FAIL), D-01b 1.55 at bore r 3.55 and 1.575
at groove_d 10.15 (FAIL): the spec sets both gates at the nominal value, so the
part will be reported as passing only at nominal on those rows (§7 Q4).

## 7. Risks and questions for the orchestrator

Questions (spec values the measurement or arithmetic contradicts; not changed in the plan):

- **Q1 (D-03a / REQ-01, blocking J3).** The collar flank is specified as "60°,
  from Ø10.2 at z −294.0 to Ø11.4 at z −293.654": 0.600 radial over 0.346 axial is
  atan(0.346/0.600) = 30.0° from horizontal, 60° from the axis. D-03a requires
  every downward face ≥ 45° from horizontal and names the flank at 60°. As
  written, `overhang_census` would read 30.0° and D-03a FAILs. 60° from horizontal
  needs 0.600·tan 60° = 1.039 axial, ending at z −292.961 (collar cylinder 1.961
  long). The bore chamfer (0.50 axial × 0.29 radial = 59.9° from horizontal) uses
  the from-horizontal reading, which suggests the flank's 0.346 is the slip.
  Which governs: z −293.654 or 60° from horizontal?
- **Q2 (REQ-04 vs U-03 a, blocking J3).** The tie envelope bears on OD-C11's
  inner face (z −299.0, designed contact), and its head sits on the band. A
  5-long head zone centred on the 4.8 band spans z −299.1 … −294.1, i.e. 0.1 into
  the wall: measured clearance 0.000; started at the band's edge (z −299.0), also
  0.000. Clearance ≥ 0.5 is met only with the zone starting at z ≥ −298.5
  (measured 0.500), 0.5 off the band. Which of the head's 5 × 5 × 6 is along Z,
  where along Z is the zone, and should the gate be against the wall at all (the
  head against the wall inside is the expected installed state)?
- **Q3 (U-05 wording).** The split plane y 30.4 cuts through the bore, so the
  split is one plane carried by two disjoint planar faces (either side of the
  bore). The plan counts 2 coplanar faces at y 30.40 as "1 split face". Confirm.
- **Q4 (sweep and zero-margin gates).** D-04d (0.30) and D-01b (1.6) equal the
  nominal geometry exactly, so any sweep across the REQ-01/02 tolerance fails
  one end. Confirm that the sweep range is the REQ tolerance band and that
  "passes only at nominal" is the expected report, or give the sweep range.
- **Q5 (text only).** §4 says the neck ends "0.2 beyond the wall's inner face";
  the numbers (neck to z −299.2, wall inner face measured at z −299.000) put the
  neck end 0.2 short of the inner face, inside the hole. The plan follows the
  numbers, which is what lets the tie bear on the wall.

Risks:

- The 0.4 split chord makes the half's X extent 19.984, not 20.0, and puts the
  neck's split edges 0.314 from the hole at the closed pose: inside the bands,
  stated so the reviewer does not read them as errors.
- A revolve seam inside the kept half would split faces and break the census; the
  profile is placed so the seam lies at y 30.0, which the split removes. If the
  census still shows extra faces, the check reports them; no unify step is applied
  silently.
- `clearance(half, OD-C11)` returns 0 from the flange contact and hides the neck
  gap; the clipped-region check (half ∩ z ≥ −301.9) separates them, and its cut
  face lies 0.1 inside the hole, so its distance to the hole wall is the radial gap.
- The inner gusset (x 72 … 76, to y 34 at the wall) is not in spec §2; measured
  19 mm off the axis in X, no effect, reported as a finding.
- REQ-05 (grip) and A-03 (PLA halves under the tie) are untested by geometry; the
  first fitting answers them.
