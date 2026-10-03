# DESIGN_PLAN — od_t01_rig (20261002-od-t01-pressure-test-rig, concept C1)

Designer: Claude Code, claude-opus-5-5 · spec version 1.0 (SHA-256 c7aa3b682f36aa223763ab81be97604421d457b1b002de7d6e6d39ff75ad641e) · written before any geometry (D2) · J2 package WP-02, attempt 1 of 2

Versions (D0): Python 3.13.7, build123d 0.11.1, OCP 7.9.3.1; repo commit 10929db1408d89144bd4af9cad971440427933d0. All five input hashes match the brief.

D1 measurements of the reference solids were made with three diagnostic scripts in this folder: `d1_measure_refs_v01.py`, `d1_sweep_proxy_v01.py`, `d1_details_v01.py`. A fourth, `d1_phi_limit_v01.py`, was run once with a faulty window proxy; its φ values do not depend on the window and agree with the corrected proxy. None of them is a gate check or a deliverable. The proxy used in the sweeps is the spec §4 C1 profile without the small holes. It is not the build.

## 1. Datum

The rig frame is the spec §2 frame. X points right, +Y points up, and +Z points toward the user. The bench top is y = 0.

- **The housing's axis is the line x 0, z 0** because the hub window, the four screw holes and every OD-G10 pose are defined about that axis (spec §2, §4).
- **y = 0 is the base's underside** because it is the bench contact plane.
- **The plate's underside y 135.0** is the designed contact with the housing's rear face. It is the functional datum for REQ-01, REQ-02 and U-03a.
- The profile is symmetric in X about x 0. The extrusion runs from z −60.0 to +60.0, which centres the frame on the axis in Z (spec §4).

## 2. Library and tools (D1)

- **Cards read: none.** "Nothing matched" is a finding. The index has no card for a printed load frame, a fixture or a test rig. The heat-set card (UNO10 U5) concerns inserts in the printed part, but here the inserts are in OD-G01. No card was opened.
- **`tools/` functions reused:**
  - `tools.core.read_step` reads the inputs and re-imports the exported STEP.
  - `validity` gives `solid_count`, `brep_valid` and `naked_edges` (U-01, exactly_one_solid).
  - `write_step` writes the AP242 delivery STEP and the check-assembly STEP (D-024).
  - `step_roundtrip` / `compare_step` cover U-04.
  - `write_stl` and `mesh_sagitta` cover U-07.
  - `common_volume` (through `interference`) handles the rig-to-cylinder probes.
- **`tools.measure` functions used:**
  - `envelope`: U-02, D-02, REQ-02 and REQ-05.
  - `feature_census`: U-05.
  - `bore_census` and `locate_bore`: U-05, D-04a, REQ-01, REQ-03 and REQ-06.
  - `min_wall` and `min_wall_wide`: D-01a, D-01b, D-06a and U-06.
  - `overhang_census(build_dir=(0,0,1))`: D-03a.
  - `flat_ceiling_spans`: D-03b, as corroboration only.
  - `clearance`: U-03, REQ-03 and REQ-04.
  - `interference`: U-03, REQ-04b, REQ-06 and REQ-07.
  - `radial_extent`: corroborates the window radius at the roof angle.
  - `tools.drawing.write_sections` and `nothing_clipped` cover D6.
- **New code needed (job code, in `01_CAD/` only):**
  - **A pose helper.** Places the housing set by the spec §2 Location and applies φ, dy and dz.
  - **A census copy for D-03a.** This is the re-imported rig with the four Ø3.4 holes filled by fused Ø3.6 × 3.0 cylinders. The crowns are then excluded by position, because `overhang_census` has no exclusion argument.
  - **Probe cylinders for REQ-06 and REQ-07.**
- **No `tools/measure` function is missing** for the planned rows. The limits are:
  - **D-03b is a reviewer row** (from sections).
  - **The pair-B screw heads have no geometry** in any input. See §7 Q2.

**Measured facts from the references** (housing frame, unless rig frame is stated):

| Item | Measured |
|---|---|
| Housing envelope | x ±50.0, y ±50.0, z −24.94 … +3.30. Posed in the rig frame: y 106.76 … 135.00. Spec §2 agrees |
| Housing insert bores | 4 × Ø4.00, axes along z at (±44.00, ±44.00), z −24.94 … −19.24 (5.70 deep). Spec and A-01 agree |
| Housing hub opening | Ø26.00 on the axis, z −24.94 … −19.94 |
| Housing pair-B holes | Ø3.8 through the slab at (−9.31, 16.60) and (10.64, −15.78), r 19.03, opening on the rear face. Ø9.0 recesses on the cup side. The OEM screws go in from the rear, with their heads on the rear face. The assembly does not model them (no screw solids) |
| Housing pair-A lobes | Ø9.0 at r 15.50, merged with the Ø26 opening |
| Assembly solids, identified by measurement | solid 0 = housing (100 × 100, 4 Ø4.0 bores at ±44, 90 216.8 mm³). Solid 1 = OD-G04 (convex hub tube r 10.03, 17 086.2 mm³). Solid 2 = OD-G10 (reaches housing y 150.08, 137 692.4 mm³) |
| OD-G04 posed | rig y 115.79 … 133.00, r ≤ 34.5. Hub tube OD 20.06 up to rig y 131.78. Highest point: pair-A boss ends at rig y 133.00, r 15.5 |
| OD-G10 locked, posed | rig x −30.57 … 92.04, y 62.30 … 121.31, z −35.03 … 150.08. Lowest point at y 62.30, which is 52.30 above the base top (A-07 agrees) |
| OD-G10 handle direction | the three vertices beyond r 120 lie 33.5° … 34.9° from +Z toward +X, at y 89.9. The spec states ≈ 28° (§7 Q4) |
| OD-G10 soundness | `brep_valid` = 0 (BOPAlgo_InvalidCurveOnSurface). `ShapeFix_Shape` does not repair it (still 0, volume unchanged). `common_volume` on it is INCONCLUSIVE. `clearance` measures it |

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Frame profile: base 240 × 10, two walls 15 × 125, top plate 180 × 15, four 10 × 10 inside chamfers | Sketch S1 on Plane.XY. One closed outer polygon, minus the inner polygon with its four 45° corners cut. Extruded along +Z from z −60.0, 120.0 long. This yields 1 plate, 2 walls, 1 base and 4 corner chamfers as one solid | — | §4 C1 (plate, walls, base, corner fillets), U-02, U-05 |
| F02 | Hub window R 30.0 with a teardrop roof toward +Z | Sketch S2: a circle R 30 plus a tangent teardrop with flanks at θ_roof (§4) and apex on the axis. The sketch is on a plane normal to Y at y 151.0 and extruded down to y 134.0, then subtracted (through the plate, with 1.0 overrun each side) | F01 | §4 C1 (hub window), REQ-03, U-05 |
| F03 | 4 × Ø6.5 counterbore with a teardrop roof toward +Z | Sketch S3: the same teardrop construction at r 3.25, placed at (x ±44, z ±44). Extruded from y 151.0 down to y 138.00 and subtracted (floor at y 138.00 exactly) | F01 | §4 C1, REQ-01, U-05 |
| F04 | 4 × Ø3.4 hole, no teardrop (the named exception) | A cylinder r 1.70 along Y at (x ±44, z ±44), from y 134.0 to y 139.0 (into the counterbore), subtracted | F03 | §4 C1, REQ-01, D-04a, U-05, D-03a exception |
| F05 | 4 × Ø4.5 bench hole with a teardrop roof toward +Z | Sketch S4: the teardrop construction at r 2.25, placed at (x ±105, z ±40). Extruded through the base from y −1.0 to y 11.0, then subtracted | F01 | §4 C1, REQ-06, D-04a, U-05 |
| F06 | Name and export | Label the body `od_t01_rig`. Write the AP242 STEP with `write_step`. Write the STL with `write_stl` at 0.01 mm and 0.10 rad | F01–F05 | U-04, U-07 |
| F07 | Check assembly | The rig plus the housing, OD-G04 and OD-G10 at the §2 pose, written as one AP242 assembly STEP (rig unchanged, references only placed) | F06, §5 placements | Deliverables §1, U-03 |

Every cutter overruns a face it passes through by 1.0, so no boolean is coplanar. The two cuts that stop inside material (the counterbore floor at y 138 and the Ø3.4 top) do not overrun. Cutters are placed by parameter, never by index. "Nothing above the plate" (§4) holds by construction because nothing is added above y 150.

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| depth_z0, depth_z1 | −60.0, +60.0 | mm | ±0.1 (U-02) | §4 C1 | yes (REQ-04a; see §7 Q1) |
| base_x | ±120.0 | mm | ±0.1 | §4 C1 | no |
| base_t | 10.0 (y 0 … 10.0) | mm | — | §4 C1 | no |
| wall_x_in, wall_x_out | ±75.0, ±90.0 | mm | — | §4 C1 | yes (REQ-04a travel) |
| plate_y0 (underside) | 135.0 | mm | ±0.10 (REQ-02) | §2, §4 C1 | yes |
| plate_y1 (top) | 150.0 | mm | ±0.1 (U-02) | §4 C1 | no |
| plate_x | ±90.0 | mm | — | §4 C1 | no |
| corner_chamfer | 10.0 × 10.0, 45° | mm | — | §4 C1 | no |
| screw_xz | (±44.0, ±44.0) | mm | offset ≤ 0.10 | §4 C1, REQ-01, measured insert axes (±44.00) | yes |
| screw_d | 3.4 | mm | ±0.1 | REQ-01, D-04a | yes |
| cbore_d | 6.5 | mm | ±0.1 | REQ-01 | yes |
| cbore_floor_y | 138.00 (12.0 deep from y 150) | mm | ±0.10 | REQ-01 (3.0 of plate under the head) | yes |
| window_r | 30.0 | mm | ±0.1 | REQ-03 | yes |
| theta_roof (all teardrops) | 45.1 | deg | window: 45° ± 1° (REQ-03); apex ±0.1 | Derived. A tangent flank at angle θ from horizontal puts the apex at r / cos θ. At 45.0° the overhang census reads exactly 45 and may be INCONCLUSIVE (D-03a). 46° puts the window apex at 43.19, outside REQ-03's 42.43 ± 0.1. 45.1° gives a window apex of 42.51 (in band), a counterbore apex of 4.61 (spec 4.60) and a bench-hole apex of 3.19 (spec 3.18), with a D-03a margin of +0.1°. See §7 Q3 | yes (D-03a, REQ-03) |
| window_apex_z | 30 / cos 45.1° = 42.51 | mm | ±0.1 vs 42.43 | derived from theta_roof | yes |
| bench_xz | (±105.0, ±40.0) | mm | offset ≤ 0.10 | REQ-06 | no |
| bench_d | 4.5 | mm | ±0.1 | REQ-06, D-04a | yes |
| cutter_overrun | 1.0 | mm | — | Derived: avoids coplanar booleans and lies outside every gated surface | no |
| housing_pose | Location((0, 110.06, 0)) · Rot about X +90° (housing x → X, y → +Z, z → −Y) | — | — | §2. Verified: rear face to y 135.000, mouth to y 106.76 | n/a |
| phi_sweep_a | −60° … +15°, step 5° (also +10.5° to locate the edge) | deg | — | REQ-04a, A-07 | motion variable |
| sweep_b | φ −50°, dy −15.0, dz 0 … 200, step 5.0 | mm | — | REQ-04b, A-07 | motion variable |
| offer_up | dy 0 … −30, step 2.0 | mm | — | U-03b | motion variable |
| stl_tol, stl_ang | 0.01 mm, 0.10 rad | — | ang ≤ 4·acos(1 − 0.01/30) = 0.1033 rad | U-07 (R_max = 30) | no |
| density | 1240 | kg/m³ | — | §3, A-08 | no |

D7 sweep, each at nominal, low and high. The motion checks (U-03b, REQ-04) are re-run on every swept build:
- screw_d 3.3 / 3.5
- cbore_d 6.4 / 6.6
- cbore_floor_y 137.9 / 138.1
- screw_xz ±0.10 radial offset
- window_r 29.9 / 30.1
- theta_roof 45.05 / 45.14
- bench_d 4.4 / 4.6
- plate_y0 134.9 / 135.1, with the housing pose moved with it
- wall_x_in 74.9 / 75.1
- depth_z1 59.9 / 60.1

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-G01 housing | `00_Spec/inputs/od_g01_assembly_C1_v03.step` solid 0 (9fd18eb5…26f2). Cross-checked against `od_g01_housing_C1_v03.step` (55478e0b…7399): same envelope and bores | The rear-face plane (the planar face at housing z −24.94) and the four Ø4.0 insert-bore axes from `bore_census` | A RigidJoint from the spec §2 Location. It is verified by measurement, not assumed: the rear face must land at y 135.000 and each insert axis on (±44, ±44) within 0.10 (`locate_bore` on the posed housing) | Plate underside y 135.0 (designed contact), Ø3.4 hole axes |
| OD-G04 | Same assembly STEP, solid 1. Reference: `OD-G04_brewing_gasket_support.step` (19b4a140…6ad2) | It moves with the housing. Its placement inside the housing is the v03 assembly's, which was measured, not rebuilt | Rigid with the housing joint | — (clearance only) |
| OD-G10 | Same assembly STEP, solid 2. Reference: `OD-G10_portafilter.step` (3a525af1…b257) | It moves with the housing at the v03 locked pose. φ is a rotation about the housing axis (rig +Y through x 0, z 0), with φ > 0 turning the handle toward +X, which is verified by the sign of max_x | A RevoluteJoint about the housing axis for φ, plus a translation for REQ-04b | — (clearance only) |
| OD-C05 | `OD-C05_group_head_carrier.step` (7b3d33ad…f5f1) | Not placed. It is the interface precedent only | — | — |

Solids are identified by measurement (§2 table), never by file order alone. No bounding-box centre is used for any placement.

## 6. Checks planned (D3)

All checks run on the re-imported exported STEP. Bands come from GATES §0: 0.005 for mm, 0.001 for degrees and mm³, 0 for counts.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | `solid_count == 1` on the re-imported rig STEP | `tools.core.solid_count` | 0 |
| U-01 | `solid_count = 1`, `brep_valid = 1`, `naked_edges = 0` | `tools.core.validity` | 0 |
| U-02 / envelope_within_spec | Sizes 240.0, 150.0 and 120.0, each in [spec − 0.1, spec + 0.1]. Position reported apart: x ±120, y 0 … 150, z ±60 | `envelope` | 0.005 |
| U-03a | (1) Posed housing to rig `clearance == 0`, with the nearest points on the y 135 plane and outside r 30. (2) `interference(rig, housing) ≤ 0`. (3) `interference(rig, OD-G04) ≤ 0`. (4) Rig to OD-G10: `common_volume` is INCONCLUSIVE on the unsound OD-G10, so the fallback is `clearance > 0` with `detail["inside"] == False` (§7 Q5). (5) Rig to the housing away from the contact: `clearance ≥ 2.0` from the rig to every housing face except the rear-face plane at y 135. Rig to OD-G04 and to OD-G10: `clearance ≥ 2.0`. Proxy D1 readings: OD-G04 5.00, OD-G10 13.69 | `clearance`, `interference` | 0.005 mm, 0.001 mm³ |
| U-03b | The housing set moved along −Y by 0 … 30 in 2.0 steps (16 poses). Rig to housing and rig to OD-G04: `interference ≤ 0` at every pose. Rig to OD-G10: the `clearance > 0` fallback. The worst pose is reported | `interference`, `clearance` | 0.001 mm³ |
| U-04 | Named body `od_t01_rig` read back unchanged, no stray shells, valid after re-import | `step_roundtrip` (`compare_step`) | 0.001 mm³, 0 |
| U-05 / feature_census | Faces: 40 planar, 13 concave cylindrical, 0 convex cylindrical, 0 other. Planar: 18 profile and end faces, 12 counterbore flanks and floors, 2 window flanks, 8 bench-hole flanks. Cylindrical: 4 Ø3.4, 4 Ø6.5, 1 R30 and 4 Ø4.5. `bore_census`: 13 bores (4 × Ø3.4 at 360°, 4 × Ø6.5, 1 × Ø60 and 4 × Ø4.5, each ≈ 270°). Profile census: 4 chamfer planes with normals at 45° in XY | `feature_census`, `bore_census`, `locate_bore` | 0 |
| U-06 (Soft) | `min_wall` `detail["wide"]` ≥ 2.0 | `min_wall_wide` | 0.005 |
| U-07 | STL at tol 0.01 and 0.10 rad (≤ 0.1033). `stl_max_sagitta ≤ 0.01`. Triangle count recorded. The 3MF is at J5 | `write_stl`, `mesh_sagitta`; `mesh_census` corroborates | 0.005 |
| U-08 | N/A by its row (no threads) | — | — |
| D-01a | `min_wall ≥ 0.8` | `min_wall` | 0.005 |
| D-01b | `min_wall ≥ 2.0`, the counterbore-to-window webs and bench-hole surrounds included. Expected least: 3.0, plate under the heads. PASS_ASSUMED A-08 | `min_wall` | 0.005 |
| D-02 | Each envelope size within 420 × 420 × 500, lying on the rear face: 240 × 150 on the bed, 120 tall. PASS_ASSUMED A-09 | `envelope` | 0.005 |
| D-03a | `overhang_census(build_dir=(0,0,1), min_deg=45)` on the census copy (the four Ø3.4 holes filled) ≥ 45, with an expected least of 45.1 at the roof flanks. A second run on the unfilled solid reports the least crown angle of the Ø3.4 holes as the exception (expected ≈ 0° at the crown). PASS_ASSUMED A-10 | `overhang_census` | 0.001 |
| D-03b | Reviewer row, from sections. Corroboration: `flat_ceiling_spans(build_dir=(0,0,1), max_span=5)` is expected to read 0 (no flat ceilings). The crown chords are ≤ 3.4 by construction | `flat_ceiling_spans`; sections | 0.005 |
| D-04a | `locate_bore` at each of the 4 screw axes: Ø ≥ 3.25. At each of the 4 bench axes: Ø ≥ 4.25 | `bore_census`, `locate_bore` | 0.005 |
| D-06a | `min_wall ≥ 1.0` | `min_wall` | 0.005 |
| D-07 | N/A by its row | — | — |
| J-05 | N/A by its row | — | — |
| REQ-01 | Each Ø3.4 hole: diameter 3.4 ± 0.1, offset ≤ 0.10 from the posed insert-bore axis (measured on the posed housing), runs y 135.00 … 138.00. Each Ø6.5 counterbore: 6.5 ± 0.1, from y 150.0 to a floor at 138.00 ± 0.10. Plate under the head: 3.0 ± 0.1 (floor y minus underside y). PASS_ASSUMED A-01 | `locate_bore`, `bore_census` | 0.005 |
| REQ-02 | The plate underside is one planar face at y 135.00 ± 0.10 whose extent covers x ±50, z ±50 less the window, plus the U-03a contact `clearance = 0`. PASS_ASSUMED A-01 | `envelope` of that face, `clearance` | 0.005 |
| REQ-03 | Window: `bore_census` Ø60.0 ± 0.2 on the axis along Y. Flank angle 45° ± 1° (expected 45.1) and apex z 42.43 ± 0.1 (expected 42.51), from the flank planes' normals and their intersection line. `radial_extent` along +Z at y 142.5 corroborates the apex. OD-G04 hub tube to rig: `clearance ≥ 2.0` (D1 proxy 20+). Pair-B screw heads ≥ 2.0: no geometry exists (§7 Q2). Planned as the measured distance from each pair-B axis (`locate_bore` on the posed housing, r 19.03) to the window face, minus a head radius the orchestrator ledgers. PASS_ASSUMED A-05 plus a new row | `bore_census`, `clearance`, `radial_extent`; sections | 0.005 mm, 0.001° |
| REQ-04a | φ from −60° to +15° in 5° steps (plus +10.5°): `clearance(rig, OD-G10 posed) ≥ 5.0` at each. **The D1 proxy predicts FAIL**: 5.76 at +10°, 4.11 at +11°, 0.80 at +13°, and 0.00 at +14° and +15°, at the +X wall's inner face x 75.0, front edge z +60.0, y ≈ 90 (§7 Q1) | `clearance` | 0.005 |
| REQ-04b | φ −50°, dy −15, dz 0 … 200 in 5.0 steps (41 poses): `interference ≤ 0`. Unsound OD-G10, so the fallback is `clearance > 0` and not inside (§7 Q5). D1 proxy least: 28.69 | `clearance` (`interference` attempted; INCONCLUSIVE expected) | 0.005 mm, 0.001 mm³ |
| REQ-05 | The posed OD-G10's `envelope` min_y minus 10.0 ≥ 50.0. D1: 52.30. PASS_ASSUMED A-07 | `envelope` | 0.005 |
| REQ-06 | `locate_bore` at (±105, ±40) along Y: Ø4.5 ± 0.1, offset ≤ 0.10, through. `interference(rig, Ø8 cylinder y 10 … 300 on each axis) = 0`. PASS_ASSUMED A-11 | `locate_bore`, `interference` | 0.005 mm, 0.001 mm³ |
| REQ-07 | `interference(rig, Ø6 cylinder y 150 … 300 on each screw axis) = 0` | `interference` | 0.001 mm³ |
| REQ-08 (Soft) | Not geometric. Reported as INCONCLUSIVE with §4's hand calculation (σ ≈ 10.5 MPa against ≈ 40 MPa, factor ≈ 3.8). The bench test answers it. A-02 | — | — |

D6 sections (`write_sections`, `nothing_clipped`) cover four views:
- the plane z 0 through the window and the axis;
- the plane z +44 through two counterbores and holes;
- the plane x +44 through two screw holes;
- the plane y 5 through the bench holes, with the check assembly's housing set shown in the first two.

## 7. Risks and questions

**Questions for the orchestrator (missing facts or spec conflicts; none is changed silently).**

- **Q1. Blocks J3: REQ-04a cannot be met by the spec 1.0 geometry.** The D1 proxy uses the exact §4 profile, and OD-G10 at the §2 pose rotated by φ. Its clearance to the rig is 5.76 at φ +10°, 4.11 at +11°, 0.80 at +13°, and 0.00 (contact) at +14° and +15°. The handle meets the +X wall's inner face (x 75.0) at the frame's front edge z +60.0, y ≈ 90. The 5.0 limit is crossed near φ ≈ +10.5°. The options all need a spec change, and the Usta must choose:
  - (a) Move the frame's front to z ≤ +45. Clearance at +15° measured 8.18 at z +45 and 4.61 at z +50, so the limit falls near z +48.7. This changes U-02's 120.0 depth.
  - (b) A local relief on the +X wall's front inner edge (a vertical chamfer along Y of about 15 at 45°). This is a new feature for U-05.
  - (c) Move the walls outward.
  - (d) Narrow REQ-04a's range to φ ≤ +10°, which narrows A-07's wear allowance.
- **Q2. REQ-03: the pair-B screw heads have no geometry.** The assembly holds no screws, and neither spec gives the head size of the OEM screws. Their axes are measured at r 19.03, so the window face is 10.97 radially from each axis. Any head of Ø ≤ 17.94, at any height inside the plate, clears by ≥ 2.0, and nothing of the rig lies above y 150. One of two answers is needed: ledger a head size (or this bound) as an A-## row, or accept the axis-distance check.
- **Q3. Spec conflict, D-03a against REQ-03.** D-03a allows roofs at 46°, but a 46° tangent roof puts the window apex at 43.19, outside REQ-03's 42.43 ± 0.1. The plan uses 45.1° for every teardrop: window apex 42.51, counterbore apex 4.61 (spec 4.60), bench-hole apex 3.19 (spec 3.18). The overhang margin is +0.1°. Please confirm.
- **Q4. Spec statement against measurement: the locked handle angle.** §2 says ≈ 28° from +Z toward +X. The handle's far vertices measure 33.5° … 34.9° (mean 34.0°) at y 89.9. The φ sweeps are relative to the locked pose, so no check changes. The §2 wording and A-07 may want the measured value.
- **Q5. OD-G10 is not a sound solid.** Its `brep_valid` is 0 (BOPAlgo_InvalidCurveOnSurface), and `ShapeFix_Shape` does not repair it. Every `interference` with OD-G10 (U-03a, U-03b, REQ-04b) will read INCONCLUSIVE. The planned fallback is `clearance > 0` with `detail["inside"] == False`, a distance in place of a volume, as OD-G01's A-28 did. Please confirm or name another evidence route, such as a mesh corroboration.

**Risks.**

- **U-03a at OD-G04.** The clearance is 5.00 in D1, set by the plate underside against OD-G04's highest point, not by any rig parameter. It does not move in the sweep.
- **The census copy for D-03a.** Fusing the Ø3.6 fill cylinders may leave a seam face on the census copy. That copy is used for D-03a only and is never exported. If the fuse fails, the fallback is to read `detail["per_kind_least_deg"]` together with the `at` location of every sample below 45°, and to show that all of them lie within r 1.75 of a screw axis between y 135 and 138.
- **The teardrop tangency at 45.1°.** The circle-to-flank tangent edge may read as a sampled least slightly above 45.1 (`sampling_bound_deg`). The margin of 0.1° is ten times the census refinement limit of 0.01°.
- **Print warp (A-10).** The long 240 × 150 footprint printed 120 tall is not gated, and a brim may be needed.
- **REQ-08 strength.** This rests on A-02 alone.
