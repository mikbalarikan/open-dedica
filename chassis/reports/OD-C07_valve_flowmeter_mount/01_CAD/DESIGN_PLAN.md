# DESIGN_PLAN — od_c07_mount (20260930-od-c07-valve-flowmeter-mount, concept C1)

Designer: Claude Code, claude-opus-5-5 · spec version 1.0 (ratified 2026-09-30) · brief `briefs/WP-02_designer.md` (J2, attempt 1 of 2) · written before any geometry (D2)

Versions (D0): Python 3.13.7, build123d 0.11.1, OCP 7.9.3.1 (OCCT 7.9.3), repo commit 70826895ab7666f9e5aee3f77ce88f099995f3c1.

Input hashes checked (D0), all match the brief and INTAKE_v01 §1:

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-H22_3way_valve.step` | bc0ffd003bcba248c7c8c4d68b198994726ee34b6c7e96ac97fbfd6490920028 |
| `00_Spec/inputs/OD-H24_flowmeter.step` | 1b4cbdafd03e0edafcc900b8c8c0894b382a48bd71850b59b06201a1fb45696a |
| `00_Spec/inputs/reports/OD-H22_3way_valve/PARAM_TABLE.md` | 1c994fcee911047b81a9e6710ddd4f8fe700e0011858b0119ada21f66f662c73 |
| `00_Spec/inputs/reports/OD-H22_3way_valve/params.json` | 2e8f4dafed0892b59b70ffa463751eb6bfe480df0ebec3b29801f6cd5c06eb82 |
| `00_Spec/inputs/reports/OD-H24_flowmeter/params.json` | be313d27ea9a5f42868ab654aa36bd775402c65d9f5ad3092ed8ea6927ae9b1d |
| `00_Spec/inputs/reports/OD-H24_flowmeter/tubes.json` | 94751607485990934a4165ab58e77f51c0ce8034c2c4a09836596b022fbf135e |

**Status of this plan: it cannot be built to pass as the spec stands.** The D1
measurements of the two reference solids show one hard gate that C1 as written
cannot meet (U-03(b): OD-H22 cannot be lowered onto a closed deck) and four spec
values that contradict other §5 rows. They are §7 Q1 to Q5. §3 to §6 plan the
spec's geometry as written, and name the proposed change for each question. The J3
package should not go out until the orchestrator and the Usta have answered §7.

## 1. Datum

The origin is on the OD-H24 flowmeter axis, at the mount's bottom face (z = 0),
because the bottom face is the face that rests on the OD-C01 floor and is the print
bed face, and the flowmeter axis is the axis of the pedestal, ring, pin holes, and
hooks. +Z is up in the machine and is the print direction. +X runs from the
flowmeter toward the valve, whose axis is the line (62.0, 0). θ is counter-clockwise
about +Z from +X. This is the spec §2 frame exactly: the OD-H24 datum frame is the
mount frame translated by (0, 0, 10.0), and the OD-H22 datum frame is the mount
frame translated by (62.0, 0, 48.0), neither rotated.

## 2. Library and tools (D1)

- Cards read (two, by tag): `library/uno10/CARD.md#u2-classic-box` (fdm, petg,
  cantilever-snap: the lesson that root strain falls with the square of the arm
  length; its CAD source is deleted, nothing to reuse) and
  `library/uno10/CARD.md#u5-tank-heat-set` (heat-set, boss, fdm: boss, blind bore,
  plane census). No card covers a bracket that seats two scanned OEM solids by
  joints; that is a finding.
- `tools/` functions reused:
  - `tools.core`: `read_step` (reference solids and the re-import), `write_step`
    (AP242 export, D-024), `step_roundtrip`, `compare_step`, `validity`,
    `solid_count`, `brep_valid`, `naked_edges`, `fillet_ladder` (all root fillets),
    `write_stl`, `mesh_sagitta`, `common_volume`.
  - `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`,
    `min_wall`, `min_wall_wide`, `overhang_census`, `interference`, `clearance`,
    `radial_extent`, `radial_profile`, `mass_properties` (reported only).
  - `tools.drawing.write_sections`, `nothing_clipped` (D6 sections).
  - `tools.result.gate` for every comparison, with the GATES §0 bands: mm 0.005,
    degrees 0.001, mm³ 0.001, counts and % 0.
- New code needed (job code in `01_CAD/`, never in the repo):
  - the U-03(b) insertion sweep: a loop over poses calling `interference` (no
    tool does a path sweep);
  - the J-01 strain arithmetic from measured t, y, L;
  - contact-exclusion helpers that cut each OEM solid into "contact
    neighbourhood" and "rest" with a box or annulus before `clearance` (§6
    note A).
  - No `tools/measure` function is missing for any gate that has a scripted check.
    D-03b, J-03, E-06, and REQ-09 are reviewer rows by the spec and get section
    evidence only.
- D1 measurement scripts (diagnostics, not gate checks):
  `01_CAD/plan_probes_v01/probe_m1_v01.py` … `probe_m5_v01.py`. They read the two
  reference STEPs and use simple probe solids built from the spec's numbers; §5
  and §7 quote their output.

## 3. Feature order

Build in build123d Algebra mode, one parameter structure at the top, named
intermediates, no index selectors. The baseline is the spec's C1 as written. Rows
marked **P-** are proposed changes that go into the build only if the matching §7
question is answered yes.

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Plate, 4.0 thick, x −25 … 94, y ±25 | extrude of rectangle sketch S1 on XY, 0 → 4.0 | — | §4 C1, U-02 |
| F02 | Plate window x 40 … 84, full Y width | subtract box x 40 … 84, y ±(25 + 1), z −1 … 5 (overcut past both faces and both edges) | F01 | §4, REQ-07, U-05 |
| F03 | 4 footprint holes Ø3.4 at (−18, ±21), (88.5, ±21) | subtract 4 cylinders along Z, through the plate | F01 | §4, REQ-06, D-04a, U-05 |
| F04 | Pedestal disc R 18.0, z 4 → 10.0 | extrude circle sketch on the plate top | F01 | §4, REQ-01, U-05 |
| F05 | Ring wall, R 16.30 … 18.30, z 10.0 → 13.0 | extrude annulus sketch on the pedestal top | F04 | §4, REQ-01, U-05 |
| F05b | 45° chamfer 0.30 × 0.30 on the ring's outer lower edge where it overhangs the pedestal (R 18.0 → 18.3) | subtract a revolved triangle; derivation in §4 `ring_lip_chamfer` | F05 | D-03a |
| F06 | Pin clearance holes Ø4.8 at (0.185, 0.093) and Ø3.8 at (−11.78, 0.14), z 0 → 10 | subtract 2 cylinders along Z through pedestal and plate | F04 | §4, REQ-02, REQ-09, U-05 |
| F07 | 3 snap hooks at θ 70°, 160°, 290° | per hook: revolve the RZ profile (beam R 20.87 … 22.87 from z 4.0 to 32.9; catch R 18.87 … 20.87 from z 29.9 to 30.9, then a 45° lead-in from (R 18.87, z 30.9) to (R 20.87, z 32.9)) through the hook's angular width, centred on θ; union | F01 | §4, REQ-03, J-01 … J-04, U-05 |
| F08 | 2 legs, x 36 … 40 and 84 … 88, y ±15, z 4 → 48 | extrude rectangles on the plate top | F01 | §4, REQ-07, U-05 |
| F09 | Deck x 40 … 84, y ±15, z 40.3 → 48.0 | extrude rectangle between the legs; union | F08 | §4, REQ-04, U-05 |
| F10 | Stem through-bore Ø14.1 on (62, 0) | subtract cylinder along Z through the deck | F09 | §4, REQ-04, U-05 |
| F11 | 2 gusset slits, 2.3 wide (y ±1.15), from the bore to x = 62 ± 11.6 at the deck top, ends falling inward at 43.4° | sketch the slit profile in the XZ plane (top edge 62 → 62 ± 11.6 at z 48, end line at 43.42° below horizontal down to the bore), extrude ±1.15 along Y, subtract | F10 | §4, REQ-04, U-05 |
| F12 | 2 screw clearance holes Ø3.4 at (77.447, 0) and (46.662, 0), z 46.0 → 48.0 | subtract 2 cylinders from the deck top, depth 2.0 | F09 | §4, REQ-05, D-04a, U-05 |
| F13 | 2 M3 insert bores Ø4.0, z 40.3 → 46.0, coaxial with F12 | subtract 2 cylinders from the deck underside, depth 5.7 | F09 | §4, REQ-05, D-05a, D-05b, J-05, U-05 |
| F14 | Root fillets | `fillet_ladder` per group, descending radii (§4): hook roots on the plate top; pedestal root on the plate top; leg roots on the plate top (outer and Y-end sides; the inner sides are flush with the window edge and have no root); ring inner root on the pedestal top | all | §4 "fillets at every root", E-06 |
| P-1 | (Q1) Deck opening: a slot from the stem bore to the deck's +Y edge, the stem-and-gusset outline swept along Y, so the valve slides in along −Y at its seated height | subtract a Y extrusion of the bore-plus-slit XZ profile from y 0 to y 15 + 1 | F11 | U-03(b), REQ-04 |
| P-2 | (Q2) Gusset slits widened to 2.40 and reaching x = 62 ± 11.85 at the top | F11 with the new values | F10 | D-04c, REQ-04 |
| P-3 | (Q3) Relief recess R 14.10, 0.60 deep, in the pedestal top inside the OD-H24 rim | subtract cylinder z 9.4 → 10.0; the pin holes open in its floor | F04, F06 | U-03(a), D-04c, REQ-02, REQ-09 |
| P-4 | (Q4) Third hook at θ 320° instead of 290° | F07 with θ = 320° | F07 | REQ-03, A-08, A-09 |
| P-5 | (Q5) 3 drain notches 2.0 wide × 0.5 high through the ring wall at the pedestal top, at θ 25°, 115°, 225° (between hooks, clear of the pipes) | subtract 3 boxes radially through the ring, z 10.0 → 10.5 | F05 | REQ-09 |

## 4. Parameters

Frame values in the mount frame. "Fit" = fit-critical, swept at D7.

| Name | Value | Unit | Tolerance | Source | Fit |
|---|---|---|---|---|---|
| `plate_t` | 4.0 | mm | ±0.1 | §4 C1; REQ-06 length | no |
| `plate_x` | −25.0 … 94.0 | mm | ±0.1 | §4; U-02 size 119.0 | no |
| `plate_y` | ±25.0 | mm | ±0.1 | §4; U-02 size 50.0 | no |
| `window_x` | 40.0 … 84.0 | mm | ±0.1 | §4; REQ-07 | no |
| `foot_hole_d` | 3.4 | mm | ±0.1 | §4; REQ-06; D-04a ≥ 3.25 | yes |
| `foot_hole_xy` | (−18, ±21), (88.5, ±21) | mm | offset ≤ 0.10 | §4; REQ-06; A-14 | no (A-14, design choice interface) |
| `ped_r` | 18.0 | mm | — | §4 | no |
| `ped_top_z` | 10.0 | mm | ±0.1 | §4; §2 frame; REQ-01 | yes |
| `ring_ri` | 16.30 | mm | [16.25, 16.35] | §4; REQ-01; A-06 (cup r 15.77 at 3 above the rim + 0.5) | yes |
| `ring_ro` | 18.30 | mm | — | §4 (wall 2.0 = D-01b) | no |
| `ring_top_z` | 13.0 | mm | ±0.1 | §4; REQ-01 | no |
| `ring_lip_chamfer` | 0.30 × 45° | mm | — | derivation: the ring outer R 18.30 overhangs the pedestal R 18.0 by 0.30, a flat downward lip at z 10.0 that D-03a does not list as supported; a 45° chamfer makes it pass D-03a without changing any spec value | no |
| `pin1_d`, `pin1_xy` | 4.8 at (0.185, 0.093) | mm | ±0.1, offset ≤ 0.10 | §4; REQ-02; A-07 (pin Ø3.8 + 2 × 0.5) | yes |
| `pin2_d`, `pin2_xy` | 3.8 at (−11.78, 0.14) | mm | ±0.1, offset ≤ 0.10 | §4; REQ-02; A-07 (pin Ø2.8 + 2 × 0.5) | yes |
| `hook_theta` | 70°, 160°, 290° | deg | ±1° | §4; REQ-03; A-09 (Q4 proposes 320° for the third) | no |
| `hook_ri` | 20.87 | mm | ±0.1 | §4; REQ-03; A-06 (flange r 20.37 + 0.5) | yes |
| `hook_t` | 2.0 | mm | — | §4; J-02; D-01b | yes (J-01) |
| `hook_w` | 6.0 chord at R 21.87 (15.77° of arc) | mm | — | §4 "6.0 wide (tangential)"; derivation: the beam is a cylindrical sector so its inner face is R 20.87 across its whole width, keeping the 0.51 gap to the flange at the beam's edges too (a flat beam's edges would sit at R 21.08) | no |
| `hook_root_z` | 4.0 | mm | — | §4 (plate top) | no |
| `catch_under_z` | 29.9 | mm | ±0.1 | §4; REQ-03; A-06 (flange top 19.9 + 10.0) | yes |
| `catch_ri` | 18.87 | mm | ±0.1 | §4; REQ-03 (reach 2.0) | yes |
| `catch_land` | 1.0 | mm | — | derivation: the catch's vertical inner land above the underside; D-06a minimum feature 1.0; the spec gives no catch height | no |
| `catch_lead_in` | 45°, from R 18.87 at z 30.9 to R 20.87 at z 32.9 | deg | ±1° | §4; REQ-03 | no |
| `hook_top_z` | 32.9 | mm | — | derivation: 29.9 + land 1.0 + chamfer rise 2.0 | no |
| `leg_x` | 36 … 40 and 84 … 88 | mm | inner faces ±0.1 | §4; REQ-07; A-02 (ear tips r 20.93 + 1.0 = 22 from the axis) | yes |
| `leg_y` | ±15.0 | mm | — | §4 | no |
| `deck_z` | 40.3 … 48.0 | mm | top ±0.1, thickness 7.7 ± 0.1 | §4; REQ-04; §2 frame; A-03 | yes |
| `stem_bore_d` | 14.1 | mm | ±0.1 | §4; REQ-04; A-03 (stem R 6.547 + 0.5) | yes |
| `slit_w` | 2.30 (Q2 proposes 2.40) | mm | ±0.1 | §4; REQ-04; A-03 (gusset 1.306) | yes |
| `slit_x_top` | ±11.6 from the valve axis (Q2 proposes ±11.85) | mm | ±0.1 | §4; REQ-04; A-03 | yes |
| `slit_angle` | 43.42 | deg | — | A-03 (gusset 43.4° below horizontal); measured 43.42° in D1 | no |
| `screw_xy` | (77.447, 0), (46.662, 0) | mm | offset ≤ 0.10 | §4; REQ-05; A-02 (measured 15.447 / −15.338 in D1) | yes |
| `screw_clear_d`, depth | 3.4, 2.0 from the deck top | mm | ±0.1 | §4; REQ-05; D-04a | yes |
| `insert_d`, depth | 4.0, 5.7 from the deck underside | mm | ±0.05, ±0.1 | §4; REQ-05; D-05b; A-13 | yes |
| `fillet_hook_root` | ladder 1.5, 1.0, 0.5 | mm | achieved radius reported | derivation: 2.87 between the pedestal side (R 18.0) and the hook inner face (R 20.87), shared with the pedestal root | no |
| `fillet_ped_root` | ladder 1.0, 0.5 | mm | achieved | same gap as above | no |
| `fillet_leg_root` | ladder 3.0, 2.0, 1.0 | mm | achieved | derivation: ≥ 4.3 from the leg's Y ends to the footprint holes | no |
| `fillet_ring_root` | ladder 0.3, 0.2 | mm | achieved | derivation: the ring gap is 0.53; the rung is accepted only if REQ-01's clearance stays ≥ 0.50 | no |
| `recess` (P-3) | R 14.10, 0.60 deep (floor z 9.40) | mm | — | derivation: OD-H24 underside ribs at H24 z 0.1 up to r 14.056 (D1) need ≥ 0.5 → floor ≤ z 9.40 − 0; R 14.10 keeps the rim's flat face (r ≥ 14.28) fully on the pedestal | yes |
| STL tolerance | 0.01 mm, angular ≤ 4·acos(1 − 0.01/22.87) = 0.1183 rad | — | — | U-07; R_max = 22.87 (hook outer face) | no |
| density | 1270 | kg/m³ | — | §3; A-11 | no |

## 5. Placements

Both frames were confirmed by measurement at D1 (`probe_m1_v01.py`,
`probe_m2_v01.py`) before any seat was planned on them.

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-H24 flowmeter | `00_Spec/inputs/OD-H24_flowmeter.step` (1b4cbdaf…696a) | Rim face: the planar −Z face at z 0.000, area 105.96 mm², r ≤ 15.416. Axis: the concave cylinder r 13.98 (rim inner, `bore_census`) on (0, 0). +X: the connector side (planar +Z face at z 24.04 spans x −0.43 … 17.0); pins Ø3.8 at (0.185, 0.093) to z −7.03 and Ø2.8 at (−11.78, 0.14) to z −5.46 measured on z-slices, matching A-07 | `RigidJoint` on OD-H24 at its rim-face origin; `RigidJoint` on the mount at (0, 0, 10.0), identity rotation; connect | pedestal top (rim face, contact); ring (REQ-01); pin holes; hook catches on the flange top z 19.9 |
| OD-H22 3-way valve | `00_Spec/inputs/OD-H22_3way_valve.step` (bc0ffd00…0028) | Flange back face: the planar −Z face at z 0.000, area 277.91 mm², x −18.954 … 19.063, y ±9.832. Axis: the drive-tube bore Ø9.122 on (0, 0), +Z. +X: the two through ear holes Ø3.872 at (15.447, 0) and (−15.338, 0) (`bore_census`) | `RigidJoint` on OD-H22 at its flange-back-face origin; `RigidJoint` on the mount at (62.0, 0, 48.0), identity rotation; connect | deck top (flange back face, contact); stem bore; gusset slits; screw holes on the ear holes |

Measured facts used by the seats (D1, OEM frames): OD-H22 stem R 6.547 from z 0
to −4.0 (then a cone to R 4.074 at −7.7); gussets y ±0.653, reaching x ±11.085
at z 0 and x ±7.1 at z −3.771 (43.42°); nothing below z −7.7 wider than
x ±6.162, but the ports reach y −19.81 … +20.065 between z −14 and −30.87; ear
tips x −20.822 / +20.931; drive-tube top z 13.68 (mount z 61.68). OD-H24 cup
r 15.769 at z 3; flange r 20.252 (z 13) to 20.339 (z 18), 20.36 at most; flange
top flat to r 19.76 at z 19.9; four slot floors at z 17.25; underside ribs and hub
at z 0.1 (faces of 75.11 and 1.12 mm², out to r 14.056).

## 6. Checks planned (D3)

Written first as `01_CAD/check_od_c07_mount.py`; every predicate re-imports the
exported STEP (`read_step`), measures, and compares with `tools.result.gate`. An
exception or a missing value gives INCONCLUSIVE. Assembly rows place the two OEM
solids by the §5 joints on the re-imported mount.

Note A (contact exclusion). "Away from the designed contacts" is made scriptable
by cutting each OEM solid before `clearance`: OD-H22 → its material at H22
z ≤ −0.001 (everything under the flange back face); OD-H24 → its material at
H24 z ≥ 0.001, minus the rim-contact annulus r 13.68 … 16.21, z ≤ 0.5 (the
contact face ± 0.3 and the rim fillets), and, for the hooks only, minus the
flange-top patches under each catch (r 18.87 … 20.37, z 19.9 − 0.001 …
19.9 + 0.001, the catch's angular span). The contacts themselves are gated by
`clearance = 0` together with `interference ≤ 0` (touching, not overlapping).

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | re-imported mount holds 1 solid | `solid_count` | 0 (count) |
| envelope_within_spec | size 119.0 × 50.0 × 48.0 each in [spec − 0.1, spec + 0.1]; min x −25, min y −25, min z 0 reported apart | `envelope` | 0.005 mm |
| feature_census | faces per kind against §3: bores (U-05 list, below), plane, cylinder, cone, torus counts recorded from the plan's feature list and compared exactly | `feature_census`, `bore_census` | 0 (count) |
| U-01 | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | `validity` | 0 |
| U-02 | as envelope_within_spec | `envelope` | 0.005 mm |
| U-03a | contacts: `clearance = 0` and `interference ≤ 0` for rim face/pedestal top, flange back face/deck top, each catch underside/flange top; every other pair: `interference ≤ 0` mount vs each OEM solid and `clearance ≥ 0.5` on the Note-A cuts (hooks against H24 are the J-04 pair) | `interference`, `clearance` | 0.001 mm³; 0.005 mm |
| U-03b | OD-H24 translated +d along Z, d ∈ {25, 20, 15, 10, 5, 2, 0.5, 0}; OD-H22 translated +d, d ∈ {40, 30, 20, 15, 10, 7.8, 5, 2, 0.5, 0}; at every pose `interference ≤ 0` between the mount (hooks removed for H24) and the solid. With P-1, OD-H22's path is instead −Y from y +40 to 0 at the seated height, ≥ 5 poses | `interference` (loop in the check script) | 0.001 mm³ |
| U-04 | STEP re-read: solids 1, volume delta 0, faces delta 0, valid after, name kept | `step_roundtrip`, `compare_step` | 0.001 mm³; 0 |
| U-05 | 1 window (plate `envelope` split into two pieces at x 40/84); `bore_census`: 4 × Ø3.4 through (length 4.0), 2 pin holes (Ø4.8, Ø3.8), 1 × Ø14.1 through, 2 × Ø3.4 depth 2.0, 2 × Ø4.0 depth 5.7; 3 hooks, 2 legs, 1 deck, 1 pedestal, 1 ring, 2 slits located by `radial_extent` / `envelope` probes at their planned positions | `feature_census`, `bore_census`, `locate_bore`, `radial_extent` | 0 (count) |
| U-06 (Soft) | `min_wall` `detail["wide"]` ≥ 2.0 | `min_wall_wide` | 0.005 mm |
| U-07 | STL at 0.01 mm, angular 0.1183 rad; `stl_max_sagitta ≤ 0.01`; triangles reported | `write_stl`, `mesh_sagitta` | 0.005 mm |
| U-08 | N/A by its row (no threads) | — | — |
| D-01a | `min_wall ≥ 0.8` | `min_wall` | 0.005 mm |
| D-01b | `min_wall ≥ 2.0` | `min_wall` | 0.005 mm |
| D-02 | envelope sizes ≤ 220 × 220 × 250, bottom face down | `envelope` | 0.005 mm |
| D-03a | least overhang ≥ 45° over all downward faces except the supported set (deck underside, 3 catch undersides) and the two insert-bore ceilings, which are D-03b bridges (Q6); the excluded faces are named with their areas | `overhang_census` (per face) | 0.001 deg |
| D-03b | bridge spans ≤ 5: insert-bore ceilings Ø4.0 (and P-5 notch ceilings 2.0); reviewer from sections; my number from `bore_census` diameters | `bore_census`; sections | 0.005 mm |
| D-04a | the 4 footprint and 2 screw clearance holes Ø ≥ 3.25 | `locate_bore` | 0.005 mm |
| D-04c | `clearance ≥ 0.5` on the Note-A cuts, per OEM solid, nearest points reported | `clearance` | 0.005 mm |
| D-04d | ring gap and pin-hole radial gaps ≥ 0.30 | `clearance` (ring vs H24 cup above z 0.5; pin-hole walls vs each pin) | 0.005 mm |
| D-05a | material ≥ 8.0 across around each Ø4.0 bore: `radial_extent` outer from the bore axis at 8 angles (4 opposite pairs) at z 41, 43, 45.5; across = the sum of each opposite pair's outer radii, least pair reported | `radial_extent` | 0.005 mm |
| D-05b | Ø 4.0 ± 0.05, depth ≥ 5.7 from the deck underside, open on the underside | `bore_census`, `locate_bore` | 0.005 mm |
| D-06a | `min_wall ≥ 1.0` | `min_wall` | 0.005 mm |
| D-07 | N/A by its row | — | — |
| J-01 | ε = 1.5·y·t/(L²·Q) ≤ 1.5 %: t from `min_wall` on the beam, y = 20.37 − catch inner R measured, L = catch underside z − plate top z measured, Q from L/t | `min_wall`, `radial_extent`, `envelope` of the hook; arithmetic | 0 (%) |
| J-02 | beam `min_wall ≥ 1.0` (beam cut out by its angular sector) | `min_wall` | 0.005 mm |
| J-03 | catch-to-root thickness ratio reported; ε margin to 1.5 % reported (taper rule applies only within 0.2 %) | `radial_extent` at root and catch; reviewer | 0.005 mm |
| J-04 | engaged pose: `interference ≤ 0` each hook vs H24; `clearance = 0` catch underside to flange top | `interference`, `clearance` | 0.001 mm³; 0.005 mm |
| J-05 | wall ≥ 3.0 around each Ø4.0 bore at z 40.5, 43.15, 45.8: `radial_extent` inner/outer ring of material, least over 16 angles | `radial_extent`, `min_wall` | 0.005 mm |
| J-06 | N/A by its row | — | — |
| E-06 | reviewer: pads are the deck tied to the legs; fillet radii achieved on hook, pedestal, ring roots reported | sections; REPORT §fillets | — |
| REQ-01 | pedestal top z 10.0 ± 0.1 (`envelope` of the pedestal top face); ring inner `radial_profile` inner, angles 0 … 359 step 1, band z 10.5 … 12.5, margin (0, 0), in [16.25, 16.35]; ring top z 13.0 ± 0.1; `clearance(ring, OD-H24 cup)` in [0.50, 0.70] | `radial_profile`, `envelope`, `clearance` | 0.005 mm |
| REQ-02 | `locate_bore` at (0.185, 0.093) Ø4.8 ± 0.1 and (−11.78, 0.14) Ø3.8 ± 0.1, offset ≤ 0.10, through, length 10.0 ± 0.1; `clearance` to each pin ≥ 0.5 | `locate_bore`, `clearance` | 0.005 mm |
| REQ-03 | each hook centred at θ ± 1° (mid-angle of its side faces); `radial_profile` inner on the centre ray z 6 … 26 = 20.87 ± 0.1; catch underside z 29.9 ± 0.1; catch inner R 18.87 ± 0.1 (`radial_extent`); lead-in 45° ± 1° (face normal angle); catch lands off the slots: common volume of the catch's downward prism (to the slot floor z 17.25 + 10) with H24 equals the full-flange value (probe-measured 20.69 mm³ for an unobstructed catch) | `radial_profile`, `radial_extent`, `clearance`, `interference` | 0.005 mm; 0.001 deg; 0.001 mm³ |
| REQ-04 | deck top z 48.0 ± 0.1, planar under the whole flange outline (`envelope` of the flange back face projected, x −18.954 … 19.063, y ±9.832, all inside the deck top face minus the bore and slits); `locate_bore` Ø14.1 ± 0.1 on (62, 0), through, length 7.7 ± 0.1; slit width 2.3 ± 0.1 and top reach 62 ± 11.6 ± 0.1 by `radial_extent` rays in ±X at z 47.95; `clearance(mount, H22 cut)` ≥ 0.5 with nearest points | `locate_bore`, `envelope`, `radial_extent`, `clearance` | 0.005 mm |
| REQ-05 | `locate_bore` Ø3.4 ± 0.1 at (77.447, 0), (46.662, 0), depth 2.0 ± 0.1 from the top, offset ≤ 0.10; coaxial Ø4.0 ± 0.05, depth 5.7 ± 0.1, open on the underside, offset ≤ 0.10 | `locate_bore` | 0.005 mm |
| REQ-06 | `locate_bore` × 4, Ø3.4 ± 0.1, offset ≤ 0.10, length 4.0 ± 0.1, through | `locate_bore` | 0.005 mm |
| REQ-07 | plate pieces' `envelope` (x max 40.0, x min 84.0, full Y); leg inner faces at x 40.0 and 84.0 ± 0.1 by `radial_extent` rays along X at z 20 | `envelope`, `radial_extent` | 0.005 mm |
| REQ-08 | `envelope` max z ≤ 48.1; nothing within r 12 of (62, 0) above z 48.0: `common_volume` of the mount with a cylinder r 12, z 48.001 … 70 on (62, 0) ≤ 0 mm³ | `envelope`, `common_volume` | 0.005 mm; 0.001 mm³ |
| REQ-09 | reviewer from sections: pin holes and window through (REQ-02, REQ-07 numbers); sections through the ring seat and recess | sections | — |

Sweep (D7, planned): nominal, low, high of every "Fit" row in §4 at the ends of its
stated tolerance, into `01_CAD/sweep_v01/`, every run one solid and the same
predicates. The two insertion paths (U-03b) are re-run at every sweep point.

## 7. Risks and questions

Measured blockers and contradictions (D1 probes; the orchestrator's decision needed
before J3):

- **Q1 (blocker, U-03(b) Hard).** OD-H22 cannot be lowered onto the C1 deck. Its
  ports sit below the flange at y −19.81 … +20.07 (z −14 … −30.87), but the deck
  (y ±15, closed around a Ø14.1 bore) lies between the flange and the ports. The
  probe (`probe_m4_v01.py`: deck with bore, OD-H22 raised d above its seat) gives
  interference 4.4 mm³ at d 30, 750 at 20, 943 at 15, 251 at 10, 40.7 at 7.8.
  No value inside the spec's tolerances fixes it. Options: (a) P-1, a slot open to
  +Y so the valve slides in along −Y at its seated height (the ports pass under the
  deck between the legs: x ±6.16 against leg inner faces at ±22). This changes
  REQ-04 "flat under the whole flange outline" (the flange then bears on the two
  deck arms and the −Y web), U-05 (no closed bore), U-03(b) (a −Y path), and it
  lets the valve slide out when the two screws are loose. (b) A separate clamp
  plate: a second part, changes spec §1 "one solid". (c) C2. This is a concept
  decision for the Usta.
- **Q2 (REQ-04 against D-04c and the REQ-04 clearance clause).** With the slits at
  2.3 wide and x ±11.6 at the top, the gap to the gusset is 0.497 per side (1.15 −
  0.653) and 0.357 at the gusset's sloped edge (probe, nearest point (11.331,
  0.653, −0.259) in the H22 frame), against ≥ 0.5. A 0.5 gap needs width ≥ 2.31
  (2.40 proposed, inside REQ-04's ± 0.1) and a top reach ≥ 11.812 (11.85
  proposed, outside REQ-04's ± 0.1). At 11.85 the wedge of deck between each
  screw clearance hole and its slit end is 1.79 (−X) and 1.90 (+X) wide at the
  deck top, below D-01b's 2.0 (the faces meet at 46.6°, so `min_wall` at 25° may
  not report it). Decide: change REQ-04 to 2.40 / 11.85 and accept the wedge, or
  sign an exception for the 0.357 gap.
- **Q3 (REQ-02 length against U-03(a) / D-04c).** A flat pedestal top leaves
  0.10 mm under the OD-H24 underside ribs and hub (faces at H24 z 0.1, out to
  r 14.056; probe gives clearance 0.100 with the pin holes cut). P-3 (a recess
  R 14.10, 0.60 deep) gives 0.70, but then the pin holes are 9.40 long, not
  REQ-02's 10.0 ± 0.1, and U-05 gains a feature. Decide: accept P-3 with REQ-02
  length 9.4, or accept the 0.10 gap under the ribs.
- **Q4 (REQ-03, A-08, A-09).** The hook at θ 290° puts its catch (±7.88° at
  R 18.87) over the OD-H24 slot at 296.5° (282.7° … 310.3°): the flange under the
  catch is 18.51 mm³ against 20.69 for an unobstructed catch (probe_m5), so "lands
  outside its slots" fails. Its gap to the upper pipe is 3.33 mm, not A-09's ≥ 5.
  At θ 320° the catch has the full 20.69 mm³ under it and 13.35 mm to the pipes;
  315° gives 19.90 mm³ (still over the slot). Proposed: P-4, θ 320°.
- **Q5 (REQ-09).** The annulus between the OD-H24 rim (r 15.71) and the ring
  (r 16.30) on the pedestal top is an up-facing pocket with no drain; the rim
  contact separates it from the pin holes. Proposed: P-5, three 2.0 × 0.5 notches
  at the ring base (below REQ-01's z 10.5 … 12.5 band, so REQ-01 is unaffected).
- **Q6 (D-03a against D-03b).** The two insert-bore ceilings (annulus r 1.7 …
  2.0 at z 46.0) are flat downward faces. D-03a lists only the deck underside and
  the catch undersides as supported; D-03b treats the ceilings as Ø4.0 bridges.
  The plan gates them under D-03b and excludes them from D-03a by name; please
  confirm.

Notes (no decision needed):

- A-03 gives the flange back face as 261 mm²; the STEP's face is 277.91 mm².
- J-01: the flange-to-catch overlap is 20.37 − 18.87 = 1.5, not the 2.0 that §4's
  arithmetic uses: ε = 1.5·1.5·2.0/25.9² = 0.67 % (Q = 1), inside 1.5 %.
- The ring outer (R 18.30) overhangs the pedestal (R 18.0) by 0.30. F05b's 45°
  chamfer handles it with no spec value changed.

Build risks and fallbacks:

- Ring inner root fillet: the 0.53 ring gap leaves room for at most about 0.3.
  The ladder accepts a rung only if REQ-01's clearance stays ≥ 0.50; if no rung
  passes, that root is left sharp and reported under E-06.
- Hook roots: the fillet stiffens the root and shortens the free length. J-01 is
  taken from the plate top as the spec states, with the fillet radius reported.
- Scan-derived OEM geometry (A-01): every seat gap is 0.5 to 0.6. A scale error
  of 0.3 % on the 40 mm flange moves its edge by 0.06. The D7 sweep covers the
  printed side only.
