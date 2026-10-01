# DESIGN_PLAN — od_c01_frame_v01 (20260930-od-c01-base-frame, concept C1)

Designer: Claude Code, Opus 5.5 · spec version 1.0 · brief WP-02 (J2, attempt 1 of 2, fix_cycles 3 not used in J2) · written before any geometry (D2)

Versions (D0): Python 3.13.7, build123d 0.11.1, OCP (cadquery-ocp-novtk) 7.9.3.1.1, repository commit d7ea010502a30dd025c5123992847da1b15f3ee3. All eleven input hashes checked against the brief: every one matches.

**Status: no conflict found.** Every spec feature and every §5 row is planned below. Every placement lands where spec §4 puts it. Two figures in spec §4 describe the inputs slightly differently from what the probes measure (§7 K-1, K-2). Neither is a gate value, and neither changes the build. One Hard-gate clause has no `tools` function (§2, U-07's 3MF clause).

Probes (placements only; the plate is represented by a plain reference slab x ±120, y −6 … 0, z −305 … +100 for pre-build estimates, never a gate):
`01_CAD/probe/probe_placements_v01.py` → `probe_placements_v01.json`; `probe_g01_low_v01.py` → `probe_g01_low_v01.json`; `probe_sampling_v01.py` → `probe_sampling_v01.json`; `versions_v01.py`.

## 1. Datum

The spec §2 machine frame, unchanged. The origin is on the floor plane, directly below the group head axis. y = 0 is the plate's top face because it is the floor plane every mount's foot stands on (OD-C03 y +40, OD-C04 y −70 and OD-C05 y −175 all land on it by the §4 joints). Taking that face as y = 0 puts every designed contact on one measured plane. x = 0 is the group head axis' vertical plane because the carrier and the thermoblock mount are symmetric about it. X is to the user's right, +Y is up, and +Z is toward the user. The plate occupies y −6.0 … 0. Print frame: the bottom face y −6.0 on the bed, build direction +Y (A-14).

Measured on the inputs as placed by the joints of spec §4:

| Fact | Measured | Expected (brief / spec §4) | Note |
|---|---|---|---|
| OD-C03 rotation (local x → +Z, y → −Y, z → +X) | columns (0,0,1), (0,−1,0), (1,0,0); determinant **+1.000000000**; local (34, 40, −4) → (−4.0, 0.0, −171.0) | proper | built as `Location(Plane(origin=(0,40,−205), x_dir=(0,0,1), z_dir=(1,0,0)))` |
| OD-C03 `validity` | solid_count 1, brep_valid 1, naked_edges 0 | sound | booleans admissible |
| OD-C03 own envelope | x ±40, y 0 … 40, z −10 … 42 | spec 1.2 §4 | |
| OD-C03 as placed: foot underside | one plane, y **0.0000**, normal (0, −1, 0), 4123.683 mm² | y 0.00, −Y | |
| OD-C03 as placed: holes | four Ø3.400 along Y, through, length 3.0, at (−4, −239), (−4, −171), (37, −239), (37, −171), offset **0.000** each | same | |
| OD-C03 as placed: envelope | x −10.0 … 42.0, y 0.0 … 40.0, z −245.0 … −165.0 | x −10 … 42, z −245 … −165 | |
| OD-C04 `validity` | 1 / 1 / 0 | sound | |
| OD-C04 as placed (identity, origin (0, 70, −140)): foot underside | one plane, y **0.0000**, normal −Y, 4959.995 mm² | y 0.00 | |
| OD-C04 as placed: holes | four Ø3.400 along Y, through, length 4.0, at (±40, −148), (±40, −114), offset **0.000** each | same | |
| OD-C04 as placed: envelope | x ±50.0, y 0.0 … 110.0, z −157.0 … −107.0 | x ±50, z −157 … −107 | |
| OD-H01 `validity` | 1 / 1 / 0 | sound | plate\|OD-H01 boolean admissible |
| OD-H01 as placed (OD-C03's joint) | x **−66.45 … +55.50**, y 16.25 … 71.40, z −232.20 … −178.15 | x −66.45 … +55.5 | |
| OD-H01 lowest point above the plate | **16.25** (at (33.5, 16.25, −205.2)); estimate to the slab 16.250 | ≥ 2.0 (U-03) | |
| OD-H11 `validity` | solid_count 1, **brep_valid 0**, naked_edges 0 | unsound (OD-C04 A-14) | every boolean against OD-H11 is INCONCLUSIVE; `clearance` still measures |
| OD-H11 as placed (OD-C04's joint) | x −43.27 … 42.84, y 16.4925 … 123.38, z −140.00 … **−89.21** | max z ≤ −85.0 | margin +4.21 |
| OD-H11 lowest point above the plate | **16.4925** (at (−9.66, 16.49, −140.0)); estimate to the slab 16.4925 | ≥ 16.5 (brief), ≥ 10.0 (REQ-08) | see K-2: 0.0075 under the spec's rounded 16.5; REQ-08 margin +6.49 |
| OD-G01 v02 `validity` | 1 / 1 / 0 | sound | |
| OD-G01 as placed (identity, origin (0, 175, 0)) | x ±50.0, y **125.0** … 225.0, z −24.94 … **+3.30** | mouth z +3.30, lowest y 131.9 | see K-1: the rear flange reaches y 125.0; the round body is at 131.9 |
| OD-C05 foot reference box (A-01) | x ±50, y 0 … 4, z −69.94 … −24.94 | brief item 5 | a box for U-03, **not a solid of the deliverable**; OD-C05's delivered solid replaces it (A-01) |

Clearances between the placed solids (probe, BRepExtrema; pre-build):

| Pair | Measured mm | Nearest points | Requirement |
|---|---|---|---|
| OD-C03 \| OD-C04 | **8.000** | (42, 0, −165) / (42, 0, −157) | ≥ 2.0 (U-03) |
| OD-C04 \| carrier foot box | **37.060** | (−50, 0, −107) / (−50, 0, −69.94) | info |
| OD-H11 \| carrier foot box (thermoblock zone, REQ-08) | **25.666** | (−9.66, 16.49, −92.36) / (−9.66, 4.0, −69.94) | info; casting 19.27 behind the box in z |
| OD-C03 \| OD-H01 | 2.300 | as OD-C03 spec A-06 | OD-C03's own REQ-03, not this job's |
| OD-C04 \| OD-H11 | 10.100 | as OD-C04 spec | OD-C04's own REQ-01 |
| OD-H01 \| OD-C04 | 21.150 | | info |
| OD-H01 \| OD-H11 | 38.150 | | info |
| OD-C03 \| OD-H11 | 28.409 | | info |
| OD-C03 \| carrier foot box | 95.060 | | info |
| OD-H01 \| carrier foot box | 110.007 | | info |
| OD-G01 \| OD-C03, OD-H01, OD-C04, OD-H11, foot box | 169.425, 166.286, 127.942, 73.554, 121.000 | | ≥ 2.0 (U-03) |
| OD-C03, OD-C04 \| slab | 0.000, common volume 0.000 mm³ each | foot underside on y 0 | U-03 contact (estimate) |

Reserved zones (spec §4, A-05 … A-08; prisms y 0 … 400 over the zone; `clearance` of each placed solid; 0 would mean entering):

| Zone | OD-C03 | OD-H01 | OD-C04 | OD-H11 | OD-G01 | foot box |
|---|---|---|---|---|---|---|
| tray x ±75, z +10 … +100 | 175.0 | 188.15 | 117.0 | 99.21 | **6.70** | 34.94 |
| tank x ±70, z −305 … −250 | **5.00** | 17.80 | 93.0 | 110.0 | 225.06 | 180.06 |
| valves x −120 … −70, z −160 … −60 | 60.21 | 38.20 | 20.0 | 26.73 | 40.36 | 20.0 |
| electronics x 70 … 120, z −240 … −30 | 28.0 | **14.50** | 20.0 | 27.16 | 20.63 | 20.0 |

No placed solid enters a reserved zone. Bulkhead line x = 65, z −240 … −30: the largest x inside that band is OD-H01 55.50 (margin 9.50 to the plane; 7.0 to a 5-thick wall centred on it), OD-C04 50.0, the foot box 50.0, OD-C03 42.0, and OD-H11 42.84 (from its envelope). OD-G01 lies outside the band. Nothing crosses the line.

Hole webs (brief item 7; a derivation from spec §4 coordinates, exact for circles; insert r 2.0, foot r 1.7, drain r 4.0; the outline x ±120, z −305 … +100, corners R 10 centred (±110, +90) and (±110, −295)):

| Pair | Web mm | Requirement |
|---|---|---|
| nearest two inserts: (±35, −40) – (±35, −60) | **16.00** | J-05 ≥ 3.0; D-05a Ø8 boss (r 4) clear of the neighbour's hole: 20 − 4 − 2 = 14 |
| insert (40, −148) – insert (37, −171) | 19.19 | |
| insert (40, −114) – insert (65, −105) | 22.57 | |
| nearest insert to the edge: (65, −105) | 53.00 to x = 120 | J-05 |
| feet holes to the edge | **8.30** each; every foot hole lies on its corner arc's centre, so the web is uniform, R 10 − 1.7 | D-01b ≥ 2.0 |
| drain (−80, −120) to the edge | 36.00 | |

J-05 and D-05a hold with large margins. The thinnest wall on the plate is the 6.0 thickness (reference slab `min_wall` 6.000 at spacing 0.7).

## 2. Library and tools (D1)

- Cards read: none. `library/INDEX.md` has no flat printed plate carrying placed mounts. UNO10 U5 (heat-set boss) is about bosses and bores, and this plate takes the insert in its own 6.0 thickness with the hole size set by the spec (A-11). Finding: nothing matched.
- `tools/` functions reused:
  - `tools.core.read_step`: every input, and every check re-imports the exported STEP.
  - `tools.core.validity`: U-01, and on every placed input before any boolean against it.
  - `tools.core.write_step` (AP242) and `step_roundtrip` / `compare_step`: the part STEP and the check assembly STEP (D-024); U-04.
  - `tools.core.write_stl`, `mesh_sagitta`: U-07.
  - `tools.core.common_volume` via `tools.measure.interference`: U-03 interference.
  - `tools.measure.clearance`: U-03 contacts (= 0) and gaps (≥ 2.0, ≥ 10.0), REQ-08.
  - `tools.measure.bore_census`, `locate_bore`: U-05, D-04a, D-05b, REQ-01 … REQ-06, U-03 coaxiality.
  - `tools.measure.feature_census`: U-05.
  - `tools.measure.envelope`: U-02, D-02, REQ-07, REQ-08 (OD-H11 max z), U-03.
  - `tools.measure.min_wall(spacing=0.7)` and `min_wall_wide(spacing=0.7)`: D-01a, D-01b, D-06a, J-05, U-06. **Spacing 0.7 is required:** at the default 0.4 the 405 × 240 face is refused (INCONCLUSIVE, "0.63 mm fits"; probe_sampling_v01). At 0.7 the slab read 6.000 in 50 s.
  - `tools.measure.overhang_census(build_dir=(0, 1, 0), spacing=0.7)`: D-03a. At the default 0.5 it is refused the same way; at 0.7 the slab read 90.0 in 15 s.
  - `tools.measure.radial_extent`: D-05a and J-05 corroboration around each insert axis. The coupon in `probe_placements_v01` confirms the reading: `detail["material"]` = [[2.0, 10.3], [13.7, 20.0]] toward a Ø3.4 hole 12 away, so the first stretch's end gives the boss radius.
  - `tools.measure.mass_properties`: reported only (A-10, 1270 kg/m³).
  - `tools.drawing.write_sections`, `nothing_clipped`: D6 sections.
  - `tools.result.gate`: every comparison, with the GATES §0 bands (mm 0.005, mm³ 0.001, degrees 0.001, counts and 1/0 facts 0).
- New code needed: none for the geometry gates. The joints are build123d `Location`s written from spec §4 and read back by measurement (§5).
- **Missing tool:** nothing in `tools/` writes or reads a 3MF (`grep -i 3mf tools` finds nothing). The 3MF will be written with build123d's `Mesher` from the same tessellation settings. U-07's clause "the 3MF carries the same mesh" has no `tools` check, so it reads **INCONCLUSIVE**, naming the missing function (a 3MF writer or reader in `tools.core`, or `mesh_census` on a 3MF). A read-back comparison (triangle count and bounding box against the STL) is reported as a lead only (rule 8). The sagitta clause of U-07 is gated normally.

## 3. Feature order

| F## | Feature | Operation | Depends on | Spec clause or gate |
|---|---|---|---|---|
| F01 | Plate | sketch S1 on a plane at y −6.0 with normal +Y: rectangle x −120 … +120, z −305 … +100, the four corners R 10.0 (sketch arcs centred (±110, +90), (±110, −295)); extrude +Y 6.0 to y 0 | — | §4 C1, U-02, REQ-07 |
| F02 | Carrier insert holes ×4 | Ø4.0 through along Y at (±35.0, −40.0), (±35.0, −60.0) | F01 | REQ-01, D-05a, D-05b, J-05, U-05 |
| F03 | Thermoblock-mount insert holes ×4 | Ø4.0 through along Y at (±40.0, −148.0), (±40.0, −114.0) | F01 | REQ-02, U-03, D-05a, D-05b, J-05, U-05 |
| F04 | Pump-cradle insert holes ×4 | Ø4.0 through along Y at (−4.0, −239.0), (−4.0, −171.0), (37.0, −239.0), (37.0, −171.0) | F01 | REQ-03, U-03, D-05a, D-05b, J-05, U-05 |
| F05 | Bulkhead insert holes ×4 | Ø4.0 through along Y at (65.0, −45.0), (65.0, −105.0), (65.0, −165.0), (65.0, −225.0) | F01 | REQ-04, D-05a, D-05b, J-05, U-05 |
| F06 | Feet holes ×4 | Ø3.4 through along Y at (±110.0, +90.0), (±110.0, −295.0) | F01 | REQ-05, D-04a, U-05 |
| F07 | Drain holes ×2 | Ø8.0 through along Y at (−80.0, −120.0), (−80.0, −230.0) | F01 | REQ-06, U-05 |
| F08 | Clean-up | `clean()`, then `exactly_one_solid` | F01 … F07 | U-01, U-05 |
| — | Reserved zones (tray, tank, valves, electronics), bulkhead line | none on the plate (spec §4: documented, not gated; A-04 … A-08); reported as zone clearances in the REPORT | — | §4 C1 |

The holes are cut as one list of `Cylinder`s along Y, placed from the parameter table (length 6.0 + 2 × 1.0 overshoot, centred at y −3.0). No fillet ladder is used. The corner R 10 is a sketch arc, not a fillet, and the spec names no other round. Top and bottom hole edges stay sharp: the spec names no chamfer, and inserts are driven from the top (A-11).

Feature census the check compares (U-05; the first build confirms it, and any difference is reported as a deviation with its cause, never by editing this count): **6 planar faces** (top, bottom, 4 sides); **26 cylindrical faces**: 22 concave (16 Ø4.0, 4 Ø3.4, 2 Ø8.0) and 4 convex (the R 10 corners); 0 of any other kind; **22 bores** (bore_census), each through, length 6.0. Top face: one planar face at y 0, normal +Y, area 97 200 − (400 − 100π) − 107.56π = **96 776.250 mm²** (derivation: rectangle less four corner losses less the 22 hole areas).

## 4. Parameters

| Name | Value | Unit | Tolerance | Source | Fit-critical |
|---|---|---|---|---|---|
| y_top | 0.0 | mm | ± 0.10 (REQ-07) | §2 frame, §4 C1 | contact plane of three mounts: held at 0.0, not swept (moving it breaks U-03 by definition) |
| plate_t | 6.0 | mm | ± 0.1 (REQ-07, U-02) | §4 C1 | yes: 5.9 / 6.0 / 6.1 (top held at 0; D-05b depth ≥ 5.7 holds at 5.9) |
| x_half | 120.0 | mm | U-02 ± 0.1 | §4 C1 | no |
| z_min, z_max | −305.0, +100.0 | mm | U-02 ± 0.1 | §4 C1 | no |
| corner_r | 10.0 | mm | — | §4 C1 | no |
| insert_d | 4.0 | mm | ± 0.05 (D-05b, REQ-01 … REQ-04) | §4 C1, A-11 | yes: 3.95 / 4.00 / 4.05 |
| carrier_xz | (±35.0, −40.0), (±35.0, −60.0) | mm | offset ≤ 0.10 (REQ-01) | §4 C1, A-01; OD-C05 spec §4 | yes: group shifted (+0.05, +0.05) and (−0.05, −0.05) |
| c04_xz | (±40.0, −148.0), (±40.0, −114.0) | mm | offset ≤ 0.10 (REQ-02) | §4 C1, A-02; measured OD-C04 holes as placed, offset 0.000 | yes: as carrier_xz |
| c03_xz | (−4.0, −239.0), (−4.0, −171.0), (37.0, −239.0), (37.0, −171.0) | mm | offset ≤ 0.10 (REQ-03) | §4 C1, A-03; measured OD-C03 holes as placed, offset 0.000 | yes: as carrier_xz |
| bulkhead_xz | (65.0, −45.0), (65.0, −105.0), (65.0, −165.0), (65.0, −225.0) | mm | offset ≤ 0.10 (REQ-04) | §4 C1, A-04 | yes: as carrier_xz |
| foot_d | 3.4 | mm | ± 0.1 (REQ-05); ≥ 3.25 (D-04a) | §4 C1, A-12 | yes: 3.30 / 3.40 / 3.50 |
| foot_xz | (±110.0, +90.0), (±110.0, −295.0) | mm | offset ≤ 0.10 (REQ-05) | §4 C1, A-12 | yes: as carrier_xz |
| drain_d | 8.0 | mm | ± 0.1 (REQ-06) | §4 C1, A-13 | yes: 7.90 / 8.00 / 8.10 |
| drain_xz | (−80.0, −120.0), (−80.0, −230.0) | mm | offset ≤ 0.10 (REQ-06) | §4 C1, A-13 | yes: as carrier_xz |
| hole_overshoot | 1.0 each side | mm | — | derivation: a cutter longer than the plate by 1.0 each end, so no coincident cap faces remain | no |
| stl_tol | 0.01 | mm | — | U-07 | no |
| stl_ang | 0.20 | rad | ≤ 4·acos(1 − 0.01/6.0) = 0.2310 | derivation from U-07: a round figure below the limit | no |
| wall_spacing | 0.7 | mm | — | derivation: the smallest round figure above the 0.63 mm the tool names for the 405 × 240 face (probe_sampling_v01) | no |
| density | 1270 | kg/m³ | — | §3, A-10 (reported only) | no |

Sweep (D7): nine plate variants, each changing one row and exported to `01_CAD/sweep_v01/`: plate_t 5.9 and 6.1; insert_d 3.95 and 4.05; foot_d 3.30 and 3.50; drain_d 7.90 and 8.10; and one variant with every hole group shifted by (+0.05, +0.05). The shift variant is also run with (−0.05, −0.05). A ±0.05 shift keeps the REQ offset ≤ 0.10 with margin 0.029, since a shift of 0.05 in both x and z is 0.0707 off axis. Every variant must build one solid and pass the same predicates, the U-03 assembly rows included, with the mounts at their fixed joints. The worst margin is reported per gate. No motion variable exists (U-03 (b) N/A). The assembly path is the mounts lowered straight down −Y onto y 0: `clearance` from each mount to the plate is checked at lifts of 10, 1, 0.1 and 0 mm to show that no plate material lies in their way (L-10).

## 5. Placements

| Component | File (SHA-256) | Frame from (measured feature) | Joint | Mates with |
|---|---|---|---|---|
| OD-C03 pump cradle | `00_Spec/inputs/OD-C03_pump_cradle.step` (8d6f60ba…e037034) | its foot underside (one plane, its y +40.0, normal +Y in its frame, measured) and its four Ø3.4 hole axes (measured at x ±34, z −4 / 37 in its frame) | `Location(Plane(origin=(0, 40, −205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))`: local x → +Z, y → −Y, z → +X, determinant +1 (A-03); read back: underside y 0.0000, holes offset 0.000 | plate top face y 0 (designed contact, `clearance` = 0, `interference` ≤ 0); its holes coaxial with F04 |
| OD-H01 pump | `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` (b05302af…3fb62) | its frame is OD-C03's (OD-C03 spec §2: identity overlay) | the same `Location` as OD-C03 | none: `clearance` ≥ 2.0 to the plate (U-03); measured 16.25 |
| OD-C04 thermoblock mount | `00_Spec/inputs/OD-C04_thermoblock_mount.step` (31904ca8…fa221) | its foot underside (its y −70.0, measured) and four Ø3.4 hole axes (x ±40, z −8 / 26 in its frame) | `Location((0, 70, −140))`, identity rotation (A-02); read back: underside y 0.0000, holes offset 0.000 | plate top face y 0 (contact); holes coaxial with F03 |
| OD-H11 thermoblock | `00_Spec/inputs/OD-H11_thermoblock.step` (e2d186f2…4038ff) | its frame is OD-C04's (OD-C04 spec §2) | the same `Location` as OD-C04 | none: `clearance` ≥ 10.0 to the plate (REQ-08; measured 16.49); booleans INCONCLUSIVE (brep_valid 0, OD-C04 A-14) |
| OD-G01 housing v02 | `00_Spec/inputs/OD-G01_housing_C1_v02.step` (f8865cd1…4407b02) | its frame is OD-C05's (OD-C05 spec §2: identity overlay); read back: mouth z +3.30, rear face z −24.94 | `Location((0, 175, 0))`, identity rotation (A-01) | none in this job: `clearance` ≥ 2.0 to every other solid (U-03). Its designed contact is with the OD-C05 wall, which is not built |
| OD-C05 carrier foot (reference box) | none (spec §4 values) | the OD-C05 spec 1.1 foot outline in the machine frame | box x ±50, y 0 … 4, z −69.94 … −24.94 (A-01) | plate top face y 0 (contact, reference only). Used in the check script only; **not written into the check assembly STEP**, and replaced by OD-C05's delivered solid when it lands (A-01) |

The check assembly STEP holds `od_c01_frame`, `od_c03_cradle`, `od_h01_pump`, `od_c04_mount`, `od_h11_thermoblock`, `od_g01_housing` as placed (spec §1). It is built by `01_CAD/assemble_od_c01_frame.py` from the exported plate STEP and the input STEPs with the Locations above. The reference box is never exported.

## 6. Checks planned (D3)

`01_CAD/check_od_c01_frame.py` re-imports `02_STEP_STL/od_c01_frame_C1_v01.step` and the assembly STEP. It gates every row through `tools.result.gate` with the GATES §0 band (mm 0.005, mm³ 0.001, degrees 0.001, counts and 1/0 facts 0). A raised exception or a missing value is INCONCLUSIVE. Every located claim uses a located measurement.

| Gate | Predicate | `tools/measure` function | Tolerance band |
|---|---|---|---|
| exactly_one_solid | solid_count == 1 | `tools.core.validity` | 0 |
| U-01 | solid_count = 1, brep_valid = 1, naked_edges = 0 | `validity` | 0 |
| U-02 / envelope_within_spec | size_x 240.0, size_y 6.0, size_z 405.0 each within ± 0.1; position reported apart: min/max x ±120.0, y −6.0 … 0.0, z −305.0 … +100.0 | `envelope` | 0.005 mm |
| U-03 (a) plate\|OD-C03 | `validity(OD-C03)` first; `clearance` == 0 (nearest point on y 0); `interference` ≤ 0 mm³; each of OD-C03's four Ø3.4 axes (its placed `bore_census`, start point) against the plate's `locate_bore` at the same (x, z): offset ≤ 0.10 | `clearance`, `interference`, `bore_census` + `locate_bore` on both | 0.005 mm, 0.001 mm³ |
| U-03 (a) plate\|OD-C04 | as for OD-C03, with OD-C04's four holes | same | same |
| U-03 (a) plate\|OD-H01 | `clearance` ≥ 2.0, nearest points; `interference` ≤ 0 (OD-H01 sound) | `clearance`, `interference` | same |
| U-03 (a) plate\|OD-H11 | `clearance` ≥ 10.0; `interference` reported **INCONCLUSIVE** by OD-C04 A-14 (brep_valid 0), never passed | `clearance`, `interference` | same |
| U-03 (a) OD-C03\|OD-C04 | `clearance` ≥ 2.0 (probe 8.000) | `clearance` | 0.005 mm |
| U-03 (a) OD-H11 max z | `envelope(OD-H11 as placed)` max_z ≤ −85.0 (probe −89.21) | `envelope` | 0.005 mm |
| U-03 (a) OD-G01 | `clearance` ≥ 2.0 to the plate, OD-C03, OD-H01, OD-C04, OD-H11 and the carrier foot box; `interference` ≤ 0 with every sound one | `clearance`, `interference` | same |
| U-03 (a) carrier foot box | plate\|box `clearance` == 0, `interference` ≤ 0 (reference, A-01) | `clearance`, `interference` | same |
| U-03 path (L-10) | each of OD-C03, OD-C04 and the box lifted by +10, +1, +0.1 and 0 along +Y: `clearance` to the plate equals the lift | `clearance` | 0.005 mm |
| U-03 (b) | N/A: no motion variable | — | — |
| U-04 | part and assembly STEP round trip: volume delta 0, faces delta 0, valid after, name `od_c01_frame` kept, no stray shells; the assembly's OD-H11 is compared by volume and faces only, since its validity was 0 on input | `step_roundtrip` / `compare_step` | 0.001 mm³, 0 |
| U-05 / feature_census | 6 planar, 26 cylindrical (22 concave, 4 convex), 0 other kinds; 22 bores, all through; then 16 Ø4.0, 4 Ø3.4, 2 Ø8.0 located one by one (REQ-01 … REQ-06); one plate (exactly_one_solid) | `feature_census`, `bore_census`, `locate_bore` | 0 (counts) |
| U-06 (Soft) | 45° wall ≥ 2.0 | `min_wall_wide(spacing=0.7)` | 0.005 mm |
| U-07 | STL at tolerance 0.01, angular 0.20 rad (≤ 0.2310); `max_sagitta` ≤ 0.01 from `write_stl`'s check and `mesh_sagitta`; triangle count recorded. 3MF clause: **INCONCLUSIVE** (no tools function, §2), with a trimesh read-back as a lead | `write_stl`, `mesh_sagitta` | 0.005 mm |
| U-08 | N/A by its row: no threads | — | — |
| D-01a | `min_wall` ≥ 0.8 | `min_wall(spacing=0.7)` | 0.005 mm |
| D-01b | `min_wall` ≥ 2.0 | `min_wall(spacing=0.7)` | 0.005 mm |
| D-02 | 240.0 × 405.0 on the bed and 6.0 tall, each ≤ 420 × 420 × 500 | `envelope` | 0.005 mm; PASS_ASSUMED A-09 |
| D-03a | least downward angle ≥ 45° with build +Y (bed face excluded) | `overhang_census(build_dir=(0, 1, 0), spacing=0.7)` | 0.001°; PASS_ASSUMED A-14 |
| D-03b | no bridge (every hole vertical, no roof) | reviewer, from sections | — |
| D-04a | four feet holes Ø ≥ 3.25 | `locate_bore` | 0.005 mm; A-12 |
| D-05a | around each of the 16 Ø4.0 holes, material continuous from r 2.0 to ≥ r 4.0 (≥ 8.0 across) on 36 rays (every 10°) plus one ray aimed at the nearest other hole, at y −0.5, −3.0, −5.5; measured = 2 × the least first-stretch end | `bore_census`, `radial_extent` (`detail["material"]`) | 0.005 mm; A-11 |
| D-05b | 16 insert holes Ø4.0 ± 0.05, length ≥ 5.7, through | `bore_census`, `locate_bore` | 0.005 mm; A-11 |
| D-06a | `min_wall` ≥ 1.0 | `min_wall(spacing=0.7)` | 0.005 mm |
| D-07 | N/A by its row | — | — |
| J-05 | `min_wall` ≥ 3.0 (the part's thinnest wall bounds every wall around an insert), with the located reading from D-05a's rays: least (first-stretch end − 2.0) ≥ 3.0 | `min_wall(spacing=0.7)`, `radial_extent` | 0.005 mm |
| E-06 | N/A by its row: no bosses | — | — |
| REQ-01 | four Ø4.0 ± 0.05 through along Y at (±35.0, −40.0), (±35.0, −60.0), offset ≤ 0.10 | `locate_bore` at (x, −3.0, z), direction (0, 1, 0) | 0.005 mm; PASS_ASSUMED A-01 |
| REQ-02 | four Ø4.0 at (±40.0, −148.0), (±40.0, −114.0), offset ≤ 0.10; coaxial with OD-C04 as placed (U-03 row) | `locate_bore` | 0.005 mm; A-02 |
| REQ-03 | four Ø4.0 at (−4.0, −239.0), (−4.0, −171.0), (37.0, −239.0), (37.0, −171.0), offset ≤ 0.10; coaxial with OD-C03 as placed | `locate_bore` | 0.005 mm; A-03 |
| REQ-04 | four Ø4.0 at (65.0, −45.0 / −105.0 / −165.0 / −225.0), offset ≤ 0.10 | `locate_bore` | 0.005 mm; A-04 |
| REQ-05 | four Ø3.4 ± 0.1 through at (±110.0, +90.0), (±110.0, −295.0), offset ≤ 0.10 | `locate_bore` | 0.005 mm; A-12 |
| REQ-06 | two Ø8.0 ± 0.1 through at (−80.0, −120.0), (−80.0, −230.0), offset ≤ 0.10 | `locate_bore` | 0.005 mm; A-13 |
| REQ-07 | `envelope` max_y 0.00 ± 0.10; size_y 6.0 ± 0.1; exactly one planar face with normal +Y at max_y (a count, band 0), its area reported beside the derived 96 776.250 mm² as information, not gated; reviewer from sections | `envelope`, face listing on the re-imported STEP | 0.005 mm; 0 (count) |
| REQ-08 | `envelope(OD-H11 as placed)` max_z ≤ −85.0 and `clearance(plate, OD-H11)` ≥ 10.0 | `envelope`, `clearance` | 0.005 mm; PASS_ASSUMED A-02 |
| REQ-09 | **Soft bench gate**: not geometric. The REPORT gives it INCONCLUSIVE with a risk rating (PETG warp on a 405 plate, A-10, A-14); the first print answers it | — (bench) | — |

Sections (D6), each through functional features with nothing clipped: z = −40 (carrier holes, with the foot box outline), z = −148 (OD-C04 holes, with OD-C04), x = 37 (OD-C03 holes, with OD-C03 and OD-H01), x = 65 (bulkhead holes), z = −120 (drain), z = +90 (feet holes), and an assembly section at x = 0. §P plausibility (P1 … P6) is answered in the REPORT.

## 7. Risks

- **K-1 (a spec description; changes nothing in the build):** spec §4 says the housing's lowest point is at y 131.9. The OD-G01 v02 solid as placed reaches **y 125.0** at its square rear flange (x ±50, z −24.94 … −19.94; material still reaches y 125.25 over z −19.94 … −15.0). The round body in front of it (z −15 … +3.30, x ±43.1) bottoms at **y 131.9**, which matches the spec's figure (probe_g01_low_v01). The flange is at least 25 behind the tray zone's rear edge (z +10), so a mug on the tray sees 131.9, and A-06's ≥ 95 mm arithmetic holds as the spec states it. This is for the orchestrator's record. No gate reads the housing's lowest y, and U-03 holds by 6.7 to the tray zone.
- **K-2 (rounding; no gate affected):** OD-H11's lowest point above the plate measures **16.4925**, 0.0075 under the 16.5 in spec §4 and the brief. The spec rounds OD-C04 A-10's −53.5 (measured −53.5075). The governing gate REQ-08 (≥ 10.0) has margin +6.49.
- **OD-H11 unsound (A-14):** every boolean with OD-H11 is INCONCLUSIVE and reported as such. The assembly STEP writer and `compare_step` may also refuse or mis-read it. Fallback: report U-04 on the assembly per part and name the part, never drop OD-H11 from the assembly.
- **Sampling on the 405 × 240 face:** `min_wall` and `overhang_census` need spacing ≥ 0.63. The plan uses 0.7, which the probe showed works (50 s and 15 s on the slab). If the holed plate is refused at 0.7, the spacing the tool names is used and stated. Nothing is passed on INCONCLUSIVE.
- **U-07's 3MF clause** reads INCONCLUSIVE for lack of a tools function (§2). U-07 is Hard, so this is flagged now: the orchestrator decides whether a tools function lands before J3 or the review carries the INCONCLUSIVE.
- **Feature census counts** are predicted. OCCT could split a hole cylinder at its seam into two faces. Any difference is reported as a deviation with its cause.
- **Carrier not built (A-01):** U-03 uses the foot reference box. REQ-01 is checked on the plate alone. The carrier's real solid and OD-G01's designed contact with it come with OD-C05's delivery.
- **REQ-09 warp:** a 240 × 405 × 6 PETG plate without ribs can lift at the corners (A-10, A-14). C2 (ribbed) is the deferred answer. It is reported as a Soft risk, not fixed by an unspecified rib.
- **Scan fidelity (A-15):** the OD-H01 and OD-H11 envelopes carry p95 0.45 to 0.47. The smallest margins that rest on them are OD-H01 to the electronics zone (14.5) and OD-H11 to the carrier box (25.7). Both are far above the scan error.
