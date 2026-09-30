# DESIGN_PLAN — od_c04_mount (20260930-od-c04-thermoblock-mount, concept C1)

Designer: Claude Code designer subagent, claude-opus-5-5 · spec version 1.0 · written before any geometry (D2) · package WP-02 (J2, plan only), attempt 1 of 2

**Status: BLOCKED on two spec conflicts measured at D2 (section 0). Every other row of this plan is settled; the J3 package cannot start until the orchestrator and the Usta answer Q1 and Q2.**

Versions (D0): Python 3.13.7, build123d 0.11.1, OCP 7.9.3.1 (OCCT 7.9.3), repository commit 70826895ab7666f9e5aee3f77ce88f099995f3c1.

Input hashes: all four inputs hash to a 64-character SHA-256 whose first 63 characters equal the 63-character value in the brief (the brief's values are one character short; the spec §2 cell is abbreviated). Full values:

| File | SHA-256 (measured) |
|---|---|
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff |
| `00_Spec/inputs/reports/OD-H11_thermoblock/params.json` | 46f1b43a54e82c08a96b2463d88622e9d5a5ae71245ccc3440c1d960ba1c5203 |
| `00_Spec/inputs/reports/OD-H11_thermoblock/ports.json` | 77fbb8b2a53e929216ddea4752a7b18e67f6f57ba1ba3864ec24e179cf224fd5 |
| `00_Spec/inputs/reports/OD-H11_thermoblock/README.md` | 61061c517ac0c20dfe1fa86a5e75dbf959eb52d272a843b2c613d77da4dddec0 |

## 0. D2 measurements of OD-H11 and the conflicts they show

All numbers come from the B-rep of the OD-H11 STEP (probe scripts and their JSON in `01_CAD/probe/`); the primitive solids used for feasibility are spec-sized cylinders and boxes, not the part.

| Item | Measured | Tool | Probe |
|---|---|---|---|
| `validity(OD-H11)` | solid_count 1, naked_edges 0, **brep_valid 0**: BOPAlgo_InvalidCurveOnSurface, curve-on-surface 0.00116 mm against the limit 0.000146 mm (BRepCheck alone passes) | `validity` | probe_odh11_v01 |
| Envelope | x −43.270 … 42.839, y −53.508 … 53.381, z 0.000 … 50.790 (min_z −1e-7) | `envelope` | probe_odh11_v01 |
| Rearmost surface | the base face, z = 0.000; nothing below it | `envelope` min_z | probe_odh11_v01 |
| Screw hole S1 (Ø3.6) | axis along Z at (−19.620, 20.180), offset 0.000 from the spec point; bore cylinder z 3.0 … 8.0, blind end at z 8.0 (material from z 8.0 up on the axis); **opens toward −Z**. Its rim lies partly on the base face z 0.00 (hole-relative angles about 225° … 345°) and partly in the U-notch, floor z 3.20 (angles 0° … 105°). A Ø7.0 spacer first meets OD-H11 at **z 0.00** (a Ø7.0 × 10.0 spacer ending at z 3.2, as §4 supposed, overlaps the casting: `clearance` 0, inside true) | `bore_census`, `locate_bore`, line–solid intersection, `clearance` | probe_odh11_v01, probe_odh11_axes_v01 |
| Screw hole S2 (Ø3.5) | axis along Z at (25.010, 9.080), offset 0.000; bore z 27.6 … 33.2, open at z 27.6, closed at 33.2; **opens toward −Z on the mid-lug underside, z 27.60** (the Ø7.0 spacer seats on it all round) | same | same |
| Nearest casting to the S2 axis below the lug | body wall 6.41 mm from the S2 axis for z 0 … 27.6 (nearest point (19.749, 5.417, 17.610)) | `clearance` | probe_odh11_axes_v01 |
| **Body axis** | **(x −8.330, y −14.130)**, not the origin: the three top pins' circle centre (−8.3301, −14.1299), PCD 49.9996; body circle fits at z 20 and 30 about it, R 34.47 / 34.44; the 3-lobe bore is 120° periodic about it | section at z 49–50, `radial_extent` | probe_odh11_axis_v01, probe_odh11_polar_v01 |
| Pads θ 262.5° and 339.0° | about the measured axis: pad base R 35.05 (z 15 … 25), rib crest R 36.25 (z 10, 30 … 40), ear block **R 39.40** (z 5; the outermost), both angles alike: the README's values. About the origin the same rays read 48.29 … 49.44 (θ 262.5°) and 25.52 … 32.08 (θ 339.0°): not pads | `radial_extent` | probe_odh11_pads_axis_v01, probe_odh11_pads_v01 |
| Plate slab (z −17 … −12, x ±50, y −70 … 40) to OD-H11 | 12.000 (nearest on the base face) | `clearance` | probe_odh11_axes_v01 |
| Foot slab (y −70 … −66, z −17 … 33, x ±50) to OD-H11 | 12.492 (nearest at y −53.508) | `clearance` | probe_odh11_axes_v01 |

### Conflict 1 (hard, S2): REQ-01 against REQ-03 / A-05

- Spec geometry: S2 standoff Ø12.0 from z −12.0 to the tip at 27.6 − 10.0 = 17.6. Measured `clearance` to OD-H11: **0.411 mm** against REQ-01 ≥ 10.0 (margin −9.589). The standoff rises beside the body wall, which stands 6.41 mm from the S2 axis all the way from z 0 to the lug; no printed standoff with a Ø4.0 bore can come above z ≈ −10 there and keep 10.0.
- S2 standoff tip at z −10.0 instead: `clearance` **10.090 mm** (PASS), but the spacer is then 27.6 − (−10.0) = **37.6 mm**, not the 10.0 of A-05 and REQ-03.
- Options for the Usta (only the spec can change): (a) S2 spacer Ø7.0 × 37.6 (tip z −10.0), REQ-03 for S2 reads 37.6 and A-04's screw becomes about 5 + 2 + 37.6 + 5 ≈ 50 mm; (b) keep the 10.0 spacer and sign a named exception (U-18) to REQ-01 for the S2 standoff (0.41 mm gap to a >100 °C casting: not recommended); (c) give up S2 and hold the thermoblock by S1 plus the OEM brackets (concept change toward C3, needs A-06).

### Conflict 2 (frame): §2 "the origin is on the axis" is not true of the STEP

- The STEP's body axis is at (−8.330, −14.130), 16.40 mm from the origin; z = 0 base face and +Z are as stated. The hole coordinates, the plate, the foot, the frame holes, and the envelope are all in STEP coordinates and are unaffected.
- Affected: REQ-07 ("r ≤ 45.0 from the axis") and every θ in the spec (the pads at 262.5° and 339.0° are pads only about the measured axis). The plan measures REQ-07 about the measured axis (−8.330, −14.130) and reports the origin reading beside it; the planned geometry (gussets kept to r ≥ 56.5 from the measured axis and ≥ 72.8 from the origin within z 0 … 47.64) meets both, so the choice changes no geometry, only the gate's wording. The spec must say which.

### S1 (settled by the spec's own rule, but the orchestrator should see it)

- §4 set the S1 tip at −6.8 only "if the hole opens on the notch floor at z 3.2". Measured: a Ø7.0 spacer bears on the base face at z 0.00, so the tip is at 0.00 − 10.0 = **−10.00**; the S1 standoff at that tip reads `clearance` **10.000 mm** (margin 0.000, PASS with the 0.005 band); the spacer (z −10.0 … 0.0) touches the base face only (`clearance` 0, inside false). The spec's −6.8 would give 6.800 mm (FAIL). The spacer bears on a crescent of the base face about 120° wide, the rest of its end face is over the notch: see risk R3.

## 1. Datum

The origin, axes, and θ are those of the OD-H11 STEP (spec §2: the overlay is the identity). z = 0 is the thermoblock's base face, measured as its rearmost surface (min_z 0.000), because REQ-01 and REQ-04 measure the plate from it; +Z points toward the outlet face (top face 47.64, pins 50.79, measured size_z 50.790); −Y is down in the machine, so the foot's underside is the plane y = −70.0 (REQ-05). The mount is not built about the thermoblock's body axis: the only features located in x and y are the two screw-hole axes (measured at (−19.620, 20.180) and (25.010, 9.080)) and the frame pattern, all given in STEP coordinates. REQ-07's radius is taken about the measured body axis (−8.330, −14.130) per conflict 2.

## 2. Library and tools (D1)

- Cards read (at most two): UNO10 U5 tank heat-set (tags fdm, boss): the boss + bore pattern and the lesson "keep how big and where apart in envelope maths". No card matches a heat-shielded mount; "nothing matches the spacer / air-gap arrangement" is a finding.
- `tools/` functions reused:
  - `tools.core`: `read_step` (re-import), `write_step` (AP242, the delivery writer), `step_roundtrip` / `compare_step` (U-04), `validity` (U-01 and OD-H11's soundness), `write_stl` + `mesh_sagitta` (U-07), `common_volume` via `interference` (U-03), `fillet_ladder` (root fillets, E-06).
  - `tools.measure`: `envelope` (U-02, D-02, REQ-04, REQ-05, REQ-03 tip faces), `bore_census` + `locate_bore` (U-05, D-04a, REQ-02, REQ-06), `feature_census` (U-05), `min_wall` / `min_wall_wide` (D-01a, D-01b, D-06a, U-06), `overhang_census` (D-03a), `clearance` (REQ-01, REQ-03, U-03), `interference` (U-03), `radial_profile` (REQ-07, as a keep-out scan).
  - `tools.drawing.write_sections` and `nothing_clipped` (D6 sections, J3).
- New code needed: none in `tools/`. REQ-07 is a "no material inside r 45.0 in a z window" question; `radial_profile(side="inner", r_min=0, r_max=45.0)` about the measured axis answers it (every ray reading "no material" is INCONCLUSIVE by that function's contract), so the check script scans instead with `common_volume(mount, keep-out cylinder r 45.0 × z 0 … 47.64 minus the standoff and spacer columns)` and gates it `<= 0` mm³; the reviewer confirms from sections as the row says.

## 3. Feature order

Geometry below uses the tip heights of the recommended resolution (both tips at z −10.0); if the Usta picks another option, only F05's tip heights and E-06 change.

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Rear plate 100.0 × 110.0 × 5.0, z −17.0 … −12.0, x ±50, y −70 … +40 | extrude of sketch S1 (rectangle on Plane XY at z −17, +Z by 5.0) | — | §4 C1, REQ-04, U-02 |
| F02 | Plate corners R 5.0 | the two free corners at y +40 rounded in sketch S1; the two at y −70 lie inside the foot's footprint (F03 spans x ±50, y −70 … −66 from z −17) and stay square | F01 | §4 C1 |
| F03 | Foot 100.0 × 4.0 × 50.0, y −70.0 … −66.0, z −17.0 … +33.0, x ±50 | extrude of a rectangle on Plane XZ at y −70, +Y by 4.0; fused to F01 | F01 | §4 C1, REQ-05, U-02 |
| F04 | Gussets ×2, 4.0 thick at x 44.0 … 48.0 and −48.0 … −44.0 | right triangle in the YZ plane, legs 20.0 along the plate's front face (y −66 → −46 at z −12) and 20.0 up the foot (z −12 → +8 at y −66), extruded 4.0 along X; fused | F01, F03 | §4 C1, U-05 |
| F05 | Standoffs S1, S2: Ø12.0 cylinders on the plate front face along +Z, axes at (−19.62, 20.18) and (25.01, 9.08), tips at z −10.00 (S1: base face 0.00 − 10.0; S2: see conflict 1) | extrude of two circles on Plane XY at z −12.0 by 2.0; fused | F01 | §4 C1, REQ-03, E-06 |
| F06 | Standoff root fillets | `fillet_ladder` on the concave circular edge of each standoff at z −12.0: radii 1.0, 0.8, 0.5, radius achieved recorded | F05 | E-06 |
| F07 | Standoff bores Ø4.0 ×2, through plate and standoff (z −17.0 … −10.0) | cut of two Ø4.0 cylinders along Z on the F05 axes, length beyond both ends | F06 | REQ-02, D-04a, U-05 |
| F08 | Frame holes Ø3.4 ×4 along Y through the foot at (x ±40.0, z −8.0) and (x ±40.0, z 26.0) | cut of a teardrop profile (Ø3.4 circle, two roof lines tangent at 50° from horizontal meeting above the centre toward +Z) on Plane XZ, extruded through y −71 … −65 | F03 | REQ-06, D-04a, D-03a, U-05 |

Solid assembly for the U-03 / REQ-03 checks (not part of the part file): OD-H11 at the identity pose; spacer SP1 Ø7.0 × 10.0 with a Ø4.0 bore on the S1 axis, z −10.0 … 0.0; spacer SP2 Ø7.0 with a Ø4.0 bore on the S2 axis, z −10.0 … 27.6 (length 37.6 under option (a); 10.0 × z 17.6 … 27.6 under option (b)). They are the designer's modelled spacers (A-05), named `spacer_S1`, `spacer_S2`.

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| plate_x | ±50.0 | mm | ±0.1 | §4 C1, U-02 | no |
| plate_y | −70.0 … +40.0 | mm | ±0.1 | §4 C1, U-02 | no |
| plate_back_z | −17.0 | mm | ±0.10 | §4 C1, REQ-04 | yes |
| plate_front_z | −12.0 | mm | ±0.10 | §4 C1, REQ-04 (A-02); measured base face z 0.000, so REQ-01 margin at the plate 2.0 | yes |
| plate_corner_r | 5.0 | mm | — | §4 C1 | no |
| foot_y | −70.0 … −66.0 | mm | ±0.10 | §4 C1, REQ-05 (A-10) | yes |
| foot_z | −17.0 … +33.0 | mm | ±0.1 | §4 C1, U-02 | no |
| frame_hole_d | 3.4 | mm | ±0.1 (≥ 3.25, D-04a) | §4 C1, REQ-06 (A-10) | yes |
| frame_hole_xz | (±40.0, −8.0), (±40.0, 26.0) | mm | offset ≤ 0.10 | §4 C1, REQ-06 (A-10) | yes |
| teardrop_roof_deg | 50 | ° from horizontal | — | derivation: D-03a needs every downward face ≥ 45° with build direction +Z; the hole axis is horizontal, so a round crown would read 0°; roof lines tangent at 50° keep the census 5° clear of the limit and leave a 260° arc, which `bore_census` still counts as a Ø3.4 bore (> 180°) | no |
| gusset_x | ±46.0 (44.0 … 48.0) | mm | — | §4 C1 (x ±46, 4.0 thick) | no |
| gusset_legs | 20.0 × 20.0 | mm | — | derivation: 4 × the plate thickness along the plate, the same up the foot; top at z +8 keeps ≥ 56.5 from the measured axis and ≥ 72.8 from the origin (REQ-07 window z 0 … 47.64) and clear of the frame holes (hole edge x 41.7 vs gusset 44.0); a 30 × 30 trial measured `clearance` 13.18 to OD-H11, so 20 × 20 is farther | no |
| standoff_d | 12.0 | mm | — | §4 C1 | no |
| standoff_xy S1 | (−19.62, 20.18) | mm | offset ≤ 0.10 | §4 C1, A-03; measured axis offset 0.000 | yes |
| standoff_xy S2 | (25.01, 9.08) | mm | offset ≤ 0.10 | §4 C1, A-03; measured axis offset 0.000 | yes |
| seat_z S1 | 0.00 | mm | — | measured (section 0): the base face, where a Ø7.0 spacer first meets OD-H11 | — |
| seat_z S2 | 27.60 | mm | — | measured: the mid-lug underside | — |
| spacer_len | 10.0 | mm | ±0.10 | A-05, REQ-03 | yes |
| tip_z S1 | −10.00 | mm | ±0.10 | derivation: seat_z S1 − spacer_len | yes |
| tip_z S2 | **−10.00 (option a) — open, Q1** | mm | ±0.10 | derivation: REQ-01 (10.090 measured at −10.0); REQ-03 as written would put it at 17.60 (0.411 measured) | yes |
| standoff_bore_d | 4.0 | mm | ±0.1 (≥ 3.75, D-04a) | §4 C1, REQ-02, A-04 | yes |
| root_fillet_r | ladder 1.0, 0.8, 0.5 | mm | — | derivation: E-06 asks for a root fillet; 1.0 is half the 2.0 standoff height, so the tip face keeps a flat seat for the spacer | no |
| spacer_d / bore | 7.0 / 4.0 | mm | — | A-05 | no |
| stl_tol / angular | 0.01 / 0.2309 | mm / rad | — | U-07: 4·acos(1 − 0.01/6.0) = 0.23097 | no |

Sweep at D7 (nominal, low, high, Usta U-15): plate_front_z (±0.10), plate_back_z (±0.10), foot_y (±0.10), frame_hole_d (3.3 / 3.5), frame_hole_xz (±0.10 in x and z), standoff_xy (±0.10 in x and y), standoff_bore_d (3.9 / 4.1), tip_z (±0.10), exported to `01_CAD/sweep_v01/`. REQ-01 is expected to fail at tip_z high (−9.90: the S1 standoff reads 9.900): the tip tolerance of REQ-03 and the 10.0 of REQ-01 cannot both hold at S1 over the band. The sweep reports it as found; see Q3.

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-H11 thermoblock | `00_Spec/inputs/OD-H11_thermoblock.step` (e2d186f2…4038ff) | its own frame (spec §2: identity), confirmed by the measured base face z 0.000 and the hole axes at offset 0.000 from the spec points | RigidJoint at the origin, axis +Z (identity) | nothing directly: ≥ 10.0 air everywhere (REQ-01) |
| spacer_S1 (modelled, A-05) | none (built in `build_assembly_v01.py`) | S1 bore axis from `locate_bore` on OD-H11 (start point, axis +Z) and the measured seat z 0.00 | RigidJoint: spacer end face on the seat, axis on the bore axis; other end on the S1 tip face | S1 tip face (z −10.0) and OD-H11 base face (z 0.0) |
| spacer_S2 (modelled, A-05) | none | S2 bore axis from `locate_bore` (start (25.01, 9.08, 27.6)) and the lug underside z 27.60 | RigidJoint as above | S2 tip face and the lug underside |

## 6. Checks planned (D3)

Every predicate re-imports the exported STEP with `read_step`, gates `validity` first, and compares with `tools.result.gate` using the GATES.md §0 band: 0.005 for mm, 0.001 for mm³ and degrees, 0 for counts. `check_od_c04_mount_v01.py` covers the part; `check_assembly_v01.py` covers U-03, REQ-01, REQ-03 on the placed parts.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | solid_count == 1 on the re-imported part | `solid_count` | 0 |
| U-01 | solid_count = 1, brep_valid = 1, naked_edges = 0 | `validity` | 0 |
| envelope_within_spec / U-02 | size_x 100.0, size_y 110.0, size_z 50.0 each in [spec − 0.1, spec + 0.1]; position min/max x, y, z against ±50.0, −70.0 … 40.0, −17.0 … 33.0 reported apart | `envelope` | 0.005 |
| U-03 (a) | clearance(mount, OD-H11) ≥ 10.0 (REQ-01 governs); interference(mount, OD-H11) ≤ 0 reported INCONCLUSIVE because `validity(OD-H11)` brep_valid = 0 (the spec row says so); clearance(mount, spacer_i) = 0 and interference ≤ 0; clearance(spacer_i, OD-H11) = 0 and interference(spacer_i, OD-H11) INCONCLUSIVE for the same reason | `clearance`, `interference` | 0.005 mm, 0.001 mm³ |
| U-03 (b) | no motion variable: N/A by the row, stated | — | — |
| U-04 | write_step AP242, re-read: schema, solids 1, volume_delta, faces_delta 0, name unchanged, valid after | `step_roundtrip` | 0.001 mm³, 0 |
| U-05 / feature_census | 1 plate, 1 foot, 2 gussets, 2 standoffs from the face census against F01 … F08 (convex cylinders 4: 2 standoffs + 2 plate corners; torus faces 2: root fillets; bores 6); `bore_census` == 6: 2 Ø4.0 along Z, 4 Ø3.4 along Y, each located | `feature_census`, `bore_census`, `locate_bore` | 0 |
| U-06 (soft) | min_wall wide ≥ 2.0 | `min_wall_wide` | 0.005 |
| U-07 | STL at 0.01 mm, angular 0.2309 rad, cached triangulation cleared; mesh_sagitta ≤ 0.01; triangle count recorded | `write_stl`, `mesh_sagitta` | 0.005 |
| U-08 | no threads: N/A by the row | — | — |
| D-01a | min_wall ≥ 0.8 | `min_wall` | 0.005 |
| D-01b | min_wall ≥ 2.0 | `min_wall` | 0.005 |
| D-02 | each envelope size ≤ 220 × 220 × 250 (A-09) → PASS_ASSUMED A-09 at best | `envelope` | 0.005 |
| D-03a | least downward angle ≥ 45° with build_dir (0, 0, 1); bed samples at z −17 left out | `overhang_census(build_dir=(0,0,1), min_deg=45)` | 0.001 |
| D-03b | bridge span ≤ 5: reviewer from sections; the plan has no bridge (teardrop holes, no horizontal ceilings) | — (sections) | — |
| D-04a | frame holes Ø ≥ 3.25; standoff holes Ø ≥ 3.75 | `locate_bore` diameter | 0.005 |
| D-06a | min feature ≥ 1.0 | `min_wall` | 0.005 |
| D-07 | N/A by its row | — | — |
| E-06 | each standoff has a root fillet (radius achieved from `fillet_ladder`, torus face present at z −12.0); no standoff longer than 20 (length 2.0 measured from `envelope` of the tip face), so no gusset; reviewer | `fillet_ladder` record, `feature_census`, `envelope` | 0.005 |
| REQ-01 | clearance(mount, OD-H11) ≥ 10.0 at the identity pose, nearest points reported | `clearance` | 0.005 |
| REQ-02 | two Ø4.0 ± 0.1 bores along Z at (−19.62, 20.18) and (25.01, 9.08), offset ≤ 0.10, through = 1, length 7.0 (z −17 … −10) | `locate_bore` | 0.005 |
| REQ-03 | each tip face's z from `envelope` of the planar face at the standoff top, distance to its seat (S1 0.00, S2 27.60) 10.0 ± 0.10; clearance(spacer_i, mount) = 0 and clearance(spacer_i, OD-H11) = 0 | `envelope`, `clearance` | 0.005 |
| REQ-04 | plate front face z −12.00 ± 0.10, back face −17.00 ± 0.10 (the largest planar faces normal to ±Z, located by `envelope` of each) | `envelope` | 0.005 |
| REQ-05 | min_y −70.00 ± 0.10; foot thickness 4.0 ± 0.1 (the planar face normal to +Y at the foot's inside, y −66.00) | `envelope` | 0.005 |
| REQ-06 | four Ø3.4 ± 0.1 bores along Y at (±40.0, z −8.0) and (±40.0, z 26.0), offset ≤ 0.10, through = 1 | `locate_bore` | 0.005 |
| REQ-07 | common volume of the mount with the keep-out cylinder r 45.0 about (−8.330, −14.130), z 0 … 47.64, less the standoff columns, ≤ 0 mm³; the same about the origin reported beside it; reviewer from sections | `interference` (`common_volume`), `envelope` | 0.001 mm³ |
| REQ-08 | bench gate: INCONCLUSIVE until the first heating run (A-08); no geometric check | — | — |

## 7. Risks

- R1 (conflict 1): S2 cannot meet REQ-01 with a 10.0 spacer; the plan carries option (a) until Q1 is answered.
- R2 (conflict 2): REQ-07 and every θ in the spec rest on an axis at the origin; the STEP's axis is at (−8.330, −14.130). No geometry changes; the gate's wording does.
- R3: the S1 spacer bears on a crescent of the base face (about 120° of its end face); the rest overhangs the U-notch, whose floor is 3.2 higher. The clamp load goes through that crescent. A stepped spacer (Ø7.0 to z 0, a smaller spigot into the notch) or a spacer of a smaller diameter would bear better; it needs the Usta's spacer choice (A-05).
- R4 (Q3): the S1 standoff at tip −10.0 reads clearance 10.000 with zero margin; with REQ-03's ±0.10 on the tip, the tip-high sweep (−9.90) is expected to read 9.900 at S1 and 9.990 at S2 (10.000 and 10.090 less 0.10) and fail REQ-01. The nominal part passes; the part does not pass across the band unless the tip is lowered (e.g. −10.10, spacer 10.1) or REQ-01's limit accepts the tolerance.
- R5: OD-H11 is not sound under the BOP analyzer (curve-on-surface 0.00116 mm), so every boolean with it (U-03 interference, REQ-07 is on the mount only and is unaffected) is INCONCLUSIVE by rule; the clearances still measure.
- R6: the frame-hole screw heads (M3 socket, Ø5.5) at z −8.0 clear the plate's front face by 1.25 mm, and the heads at z 26.0 are reachable only before OD-H11 is fitted (the thermoblock covers them from +Y): assembly order is foot screws first, then the thermoblock through the plate (P4, J3 D6).
- R7: the fillet ladder on a 2.0 tall standoff: 1.0 should fit; 0.5 is the floor rung.

## 8. Questions for the orchestrator (stop)

- Q1 (conflict 1): S2 — spacer 37.6 with the tip at z −10.0 (option a), a signed exception to REQ-01 for S2 (b), or drop S2 (c)? Measured: tip 17.6 gives 0.411 mm; tip −10.0 gives 10.090 mm.
- Q2 (conflict 2): measure REQ-07 (and read every θ) about the measured body axis (−8.330, −14.130), as the plan proposes, or about the origin? Either way §2's "the origin is on the axis" needs amending.
- Q3: S1 at zero REQ-01 margin — accept (nominal only), or lower both tips to −10.10 (spacers 10.1) so the ±0.10 tip band keeps 10.0?
