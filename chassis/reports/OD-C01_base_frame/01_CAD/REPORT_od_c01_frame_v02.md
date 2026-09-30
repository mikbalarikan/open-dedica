# REPORT — od_c01_frame v02 (20260930-od-c01-base-frame)

Designer: Claude Code, Opus 5.5 · spec version 1.2 · plan `01_CAD/DESIGN_PLAN.md` (086dde81…aa7217) with brief WP-03's notes and brief WP-04's amendments · brief WP-04 (J3, build attempt 2 of 2, fix_cycles 3) · 2026-09-30 UTC

Every number below was measured by `01_CAD/check_od_c01_frame_v02.py` on the re-imported STEP files `02_STEP_STL/od_c01_frame_C1_v02.step` and `02_STEP_STL/od_c01_assembly_C1_v02.step`. The full rows (292, each with measured value, margin, location and reason) are in `01_CAD/check_od_c01_frame_v02.json`; §3 gives each §5 row's governing (least-margin) sub-row. All eleven input hashes of WP-02 and the plan hash of WP-03 were re-checked before the build: every one matches. The v01 files are untouched; v02 has its own scripts (`*_v02.py`), started from the v01 scripts and changed only where WP-04's amendments say.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c01_frame_v02.py` | 65bb103fb32414dbca66057767facc0550fc20a2a79e8862de8f9dcc66108519 | parametric script (plate and check assembly), Algebra mode |
| `01_CAD/check_od_c01_frame_v02.py` | 1b17e65833118243422182e27a1ad871c65ee63fa62cb3f5c88633805f20b5ac | checks, written before the build (D3) |
| `01_CAD/sections_od_c01_frame_v02.py` | 1a701812e5aa464e9e7a8c06df5258342666aebe8125483067555a458db80c88 | D6 sections |
| `01_CAD/sweep_od_c01_frame_v02.py` | 9f730619e086301d19d7afbb218213d57f5a73e97837dd0f1843401447d494aa | D7 sweep |
| `01_CAD/build_record_v02.json` | d3efabdd7a6fe5362089182e9f65ca4569aeb3a11e4b0a827e21e77cb868807c | parameters, export hashes, placements |
| `01_CAD/check_od_c01_frame_v02.json` | e629e5555b94a10952302443ca89b1bcd73b89e40a2e27c0c3104d29dba19728 | check results (292 rows, facts) |
| `01_CAD/check_od_c01_frame_v02.log` | 383dcaf32f9610011a36ac3cf696cdfb0c8f683fd15361eed20e2bccaaeb8373 | check console |
| `01_CAD/sections_v02.json` | 67b31897473368a6e9b70abae088c605d49dfb4ddddddcec85ad84197f3cb173 | section planes, cut areas, nothing_clipped |
| `01_CAD/sweep_v02/sweep_summary_v02.json` | 38bfd098bf06cd107577c145d3e2c3ca2e6448976611a8ddf837a9f188a3a6e7 | sweep: per-variant status, worst margin per gate row |
| `01_CAD/sweep_v02_run.log` | 0ff89c22200aabf77d22e8d4a57d0d01044ab7905a3c296a3df74f14e64d02bc | sweep console |
| `02_STEP_STL/od_c01_frame_C1_v02.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | AP242 (`tools.core.write_step`), one solid `od_c01_frame` |
| `02_STEP_STL/od_c01_assembly_C1_v02.step` | 07560bb0caafc1e986434eede5ae22abaef9f599437948145a8a3c18e2129749 | AP242 check assembly, 7 labelled solids (§5) |
| `02_STEP_STL/od_c01_frame_C1_v02.stl` | 26bf61039e5fcbc210643fb38cd188e31a66e7b5b6e065da6eb93ffa216125db | binary STL, `tools.core.write_stl` after clearing the triangulation; tolerance 0.01 mm / angular 0.20 rad; 7068 triangles |
| `03_Sections/od_c01_frame_v02_top_z-40_carrier.png` | 4f5e942c25f9f3876aa1098ddec6d4a84c648506a6b9e8daa15556588764d7a1 | z = -40.00 mm; cut 1392.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_top_z-148_c04.png` | 7a49c0f651bc62ca766083d6a75211154f7f16c4e0af16fa721c9109dbfc9136 | z = -148.00 mm; cut 1345.52 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_left_x37_c03.png` | f277220f4e3d3e253c14fc5473606fa57f1169138a512c865ede0e7a1b374390 | x = 37.00 mm; cut 2382.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_left_x65_bulkhead.png` | e0696dd0380a374523a56c29db2fa4d6ce4c7a33190308c5064eb7d270eecb87 | x = 65.00 mm; cut 2334.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_top_z-120_drain.png` | 830ff2b0ce9de90e13805289c4ea33e06df474e3c406a5ea62754e7b031df3d8 | z = -120.00 mm; cut 1392.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_top_z90_feet.png` | 56ebdb7cefd23dbb3645f2f482f9ac66d4659d6cd40a341f38677dbcb626f0d4 | z = 90.00 mm; cut 1399.20 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_top_z-42_valve.png` | 69de67f64fdd19acb87af1e2e083ded63d9b55661cd495081842a6cf3bbd56dd | z = -42.00 mm; cut 1392.00 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_left_x-113_valve.png` | 5002f1a3966f5b237d8a8f1078d2f6d176e18e0535aed58ee2624c0277be86a9 | x = -113.00 mm; cut 2376.47 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_front_y-3_plan.png` | 88b9cbd2ec70692def33d72d97840269a2f51e02f23887b8e44a9900b778611a | y = -3.00 mm; cut 96725.98 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_left_asm_x0.png` | 3134671c9368d087f859d8a8b0fbb7bdc6e12c08c95ef92eb5d827fd4cee6afb | x = 0.00 mm; cut 8794.61 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_top_asm_z-148.png` | 7af641ca4644a3b94eab4a29e570131f839209ead0ed8561281c38be0ff3332b | z = -148.00 mm; cut 1846.32 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_left_asm_x37.png` | 4fe5dd02ceaadde3f871166e53edd1bf72f65d1b23823abea05f56af58f05d35 | x = 37.00 mm; cut 6663.34 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v02_top_asm_z32_mouth.png` | e6826257791fe8263b8f9d32a55170bec8dc4b797a7ce0f81266b96658c2a2b6 | z = 32.00 mm; cut 2106.22 mm²; nothing clipped (0) |

The sweep exports (11 variants: plate STEP, assembly STEP, STL, build record, check results) are under `01_CAD/sweep_v02/<variant>/` and are not deliverables. The cut areas agree with hand arithmetic from spec §4: z −42: 240 × 6 − 2 × 4.0 × 6 = 1392.0; z −148 also cuts the two OD-C07 holes at z −148.5 as 3.873 chords: 1440 − 48 − 46.48 = 1345.52; x −113: 405 × 6 − 2 × 4.0 × 6 − 2 × 0.461 × 6 (corner arcs) = 2376.47.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP (cadquery-ocp-novtk) 7.9.3.1.1 · ocpsvg 0.6.0 · repo commit d7ea010502a30dd025c5123992847da1b15f3ee3 (`tools/` clean)

## 3. Gate self-check

Bands are from GATES §0: mm 0.005, mm³ 0.001, degrees 0.001, counts and 1/0 facts 0. Margins are signed (positive inside). `min_wall`, `min_wall_wide` and `overhang_census` ran at **spacing 0.7 mm** (plan §4, WP-04 "spacing 0.7"); every value marked "sp 0.7" came from that spacing.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | == 1 | 0 | — | PASS | — |
| feature_census | 6 planar; 30 cylindrical (26 concave, 4 convex); 0 cone / sphere / torus / B-spline / other; 26 bores | WP-04: 6 planar, 30 cylindrical (26 concave, 4 convex), 26 bores | 0 | — | PASS | — |
| envelope_within_spec | size 240.000 × 6.000 × 405.000; position x −120.000 … 120.000, y −6.000 … 0.000, z −305.000 … 100.000 | each ± 0.1 | +0.1 | — | PASS | — |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | — | PASS | — |
| U-02 | 240.000 × 6.000 × 405.000; position reported apart (above) | each in [spec − 0.1, spec + 0.1] | +0.1 | — | PASS | — |
| U-03 (a) plate\|OD-C03 | clearance 0.000; common volume 0.000 mm³; four holes coaxial, offset 0.000 each | = 0; ≤ 0; ≤ 0.10 | 0; 0; +0.10 | (−2, 0, −171) | PASS (assumed: A-03) | A-03 |
| U-03 (a) plate\|OD-C04 | clearance 0.000; 0.000 mm³; four holes coaxial, offset 0.000 each | = 0; ≤ 0; ≤ 0.10 | 0; 0; +0.10 | (−38, 0, −114) | PASS (assumed: A-02) | A-02 |
| U-03 (a) plate\|OD-H01 | clearance 16.250; 0.000 mm³ | ≥ 2.0; ≤ 0 | +14.25 | | PASS (assumed: A-03) | A-03 |
| U-03 (a) plate\|OD-H11 | clearance 16.4925; boolean INCONCLUSIVE (OD-H11 brep_valid 0, OD-C04 A-14), as the row states | ≥ 10.0 | +6.4925 | | PASS (assumed: A-02); boolean INCONCLUSIVE by the row | A-02 |
| U-03 (a) OD-C03\|OD-C04 | clearance 8.000 | ≥ 2.0 | +6.0 | | PASS (assumed: A-02, A-03) | A-02, A-03 |
| U-03 (a) OD-H11 max z | −89.210 | ≤ −85.0 | +4.21 | | PASS (assumed: A-02) | A-02 |
| U-03 (a) OD-G01 v02 pose (joint of §4: x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0)) | read back: rear face max_y 205.000, a downward planar face at y 176.760 (the mouth, facing −Y), x −50.000 … 50.000, z −18.000 … 82.000 (all within 1e-7) | 205.0; 176.76; ±50; −18 … +82 (spec §4) | ≥ −1e-7 (in band) | | PASS (assumed: A-01) | A-01 |
| U-03 (a) OD-G01 v02 to everything else | clearance to plate 176.760, OD-C03 211.057, OD-H01 201.111, OD-C04 155.916, OD-H11 110.780, carrier foot box 173.401; common volume 0.000 mm³ with every sound solid; with OD-H11 INCONCLUSIVE by the row | ≥ 2.0; ≤ 0 | +108.78 (least) | | PASS (assumed: A-01) | A-01 |
| U-03 (a) plate\|carrier foot box (x ±55, y 0 … 4, z −70 … −26) | clearance 0.000; 0.000 mm³ | = 0; ≤ 0 | 0 | (−33, 0, −40) | PASS (assumed: A-01) | A-01 |
| U-03 (a) assembly path (L-10) | OD-C03, OD-C04 and the foot box lowered along −Y: clearance to the plate 10.000, 1.000, 0.100, 0.000 at lifts 10, 1, 0.1, 0 | = lift | ≥ −6e-15 | | PASS (assumed: A-01 … A-03) | A-01 … A-03 |
| U-03 (b) | — | N/A by the row | — | — | N/A | — |
| U-04 part | AP242; 1 solid; volume delta 1.6e-7 mm³; faces delta 0 (36); label `od_c01_frame` kept; valid after 1 | 1; 1; ≤ 0; 0; 1; 1 | −1.6e-7 (in band) | — | PASS | — |
| U-04 assembly | AP242; 7 solids; faces delta 0; 7 labels kept; per part: plate, OD-C03, OD-H01, OD-C04, OD-G01, foot box volume delta ≤ 1.6e-7 mm³, faces delta 0, valid after 1. OD-H11: faces delta 0, validity unchanged (0 → 0), **volume delta 0.0524 mm³ INCONCLUSIVE by OD-C04 A-14** (second generation 2.9e-9) | as above | — | — | PASS for the part and 6 of 7 assembly parts; OD-H11 volume row and the whole-assembly volume INCONCLUSIVE | — |
| U-05 | 1 plate; 20 Ø4.000, 4 Ø3.400, 2 Ø8.000 through-holes; 26 bores | 1; 20; 4; 2 | 0 | — | PASS | — |
| U-06 (Soft) | `min_wall` wide 5.000 (sp 0.7) | ≥ 2.0 | +3.0 | (−115, −5.7, −42) | PASS | — |
| U-07 | STL sagitta 0.004972 at tol 0.01, angular 0.20 rad (limit 0.2310); delivered STL 1 body, 0 naked edges, consistent winding. 3MF clause: orchestrator step (WP-03, WP-04) | ≤ 0.01; ≤ 0.2310 | +0.005028; +0.031 | | PASS (sagitta); 3MF: orchestrator step | — |
| U-08 | — | N/A by the row | — | — | N/A | — |
| D-01a | `min_wall` 5.000 (sp 0.7) | ≥ 0.8 | +4.2 | (−115, −5.7, −42): web from the OD-C07 hole x −113 to the edge x −120 | PASS | — |
| D-01b | 5.000 (sp 0.7) | ≥ 2.0 | +3.0 | same | PASS | — |
| D-02 | 240.0 × 405.0 on the bed, 6.0 tall | ≤ 420 × 420 × 500 | +15.0 (z) | — | PASS (assumed: A-09) | A-09 |
| D-03a | least downward angle 90.0° off the bed (sp 0.7, build +Y) | ≥ 45° | +45.0 | — | PASS (assumed: A-14) | A-14 |
| D-03b | no downward face off the bed (D-03a), so span 0.0; every hole vertical (sections) | ≤ 5 | +5.0 | — | PASS (reviewer confirms from sections) | — |
| D-04a | four feet holes Ø3.400 | ≥ 3.25 | +0.15 | (±110, −6, 90 / −295) | PASS (assumed: A-12) | A-12 |
| D-05a | 14.000 across (least material radius 7.000 about an insert axis; 2220 rays on all twenty holes, 0 unread) | ≥ 8.0 | +6.0 | (−113, −0.5, −42) at 180°, toward the edge x −120 | PASS (assumed: A-11) | A-11 |
| D-05b | 20 holes Ø4.000, length 6.000, through | 4.0 ± 0.05; ≥ 5.7 | +0.05; +0.3 | | PASS (assumed: A-11) | A-11 |
| D-06a | 5.000 (sp 0.7) | ≥ 1.0 | +4.0 | (−115, −5.7, −42) | PASS | — |
| D-07 | — | N/A by the row | — | — | N/A | — |
| J-05 | `min_wall` 5.000 (sp 0.7); located ring wall 5.000 around the twenty insert holes | ≥ 3.0 | +2.0; +2.0 | ring: (−113, −0.5, −42) at 180° (also (−113, −148.5)) | PASS | — |
| E-06 | — | N/A by the row | — | — | N/A | — |
| REQ-01 | 4 × Ø4.000 through, offset 0.000 at (±35, −40), (±35, −60) | 4.0 ± 0.05; ≤ 0.10 | +0.05; +0.10 | | PASS (assumed: A-01, A-11) | A-01, A-11 |
| REQ-02 | 4 × Ø4.000 through, offset 0.000; coaxial with OD-C04 (U-03) | same | +0.05; +0.10 | | PASS (assumed: A-02, A-11) | A-02, A-11 |
| REQ-03 | 4 × Ø4.000 through, offset 0.000; coaxial with OD-C03 (U-03) | same | +0.05; +0.10 | | PASS (assumed: A-03, A-11) | A-03, A-11 |
| REQ-04 | 4 × Ø4.000 through, offset 0.000 at (65, −45 / −105 / −165 / −225) | same | +0.05; +0.10 | | PASS (assumed: A-04, A-11) | A-04, A-11 |
| REQ-05 | 4 × Ø3.400 through, offset 0.000 | 3.4 ± 0.1; ≤ 0.10 | +0.10; +0.10 | | PASS (assumed: A-12) | A-12 |
| REQ-06 | 2 × Ø8.000 through, offset 0.000 | 8.0 ± 0.1; ≤ 0.10 | +0.10; +0.10 | | PASS (assumed: A-13) | A-13 |
| REQ-07 | max_y 0.000; thickness 6.000; 1 planar +Y face, own y extent 0.000, area 96 725.984 mm² (derived for 26 holes 96 725.984, information) | 0.00 ± 0.10; 6.0 ± 0.1; 1 plane | +0.10; +0.10; 0 | | PASS (assumed: A-01 … A-03 on top_y) | A-01 … A-03 |
| REQ-08 | OD-H11 max z −89.210; clearance(plate, OD-H11) 16.4925 | ≤ −85.0; ≥ 10.0 | +4.21; +6.4925 | | PASS (assumed: A-02) | A-02 |
| REQ-09 (Soft) | not geometric (bench) | flat in service | — | — | INCONCLUSIVE; risk MEDIUM (§9) | A-10, A-14 |
| REQ-10 | 4 × Ø4.000 through, offset 0.000 at (−113, −42), (−71, −42), (−113, −148.5), (−71, −148.5); against the pattern (no OD-C07 STEP yet) | 4.0 ± 0.05; ≤ 0.10 | +0.05; +0.10 | | PASS (assumed: A-17, A-11) | A-17, A-11 |

## 4. Robustness sweep (D7)

Ten variants plus a nominal rebuild, one parameter at a time (plan §4; the hole-shift variants move all six hole groups, the four new OD-C07 holes included). The mounts and the housing stay at their fixed joints; every variant runs the full predicate set, the assembly, pose and path rows included. **All 11 built exactly one solid and no gate row failed in any variant.** The only rows not passed are the six that are INCONCLUSIVE or an orchestrator step by their own rows, in every variant alike: the two OD-H11 booleans, OD-H11's assembly volume row, the whole-assembly volume, the 3MF clause, and REQ-09.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| plate_t (top held at y 0) | 5.9 · 6.0 · 6.1 | yes | U-02 / REQ-07 / envelope size_y 5.9; D-05b depth 5.9 | 0.0 (on the tolerance edge, in band); +0.2 |
| insert_d (all twenty) | 3.95 · 4.00 · 4.05 | yes | REQ-01 … REQ-04, REQ-10, D-05b diameter 3.95 / 4.05 | 0.0 (on the tolerance edge, in band) |
| foot_d | 3.30 · 3.40 · 3.50 | yes | REQ-05 diameter; D-04a 3.30 | 0.0; +0.05 |
| drain_d | 7.90 · 8.00 · 8.10 | yes | REQ-06 diameter | 0.0 |
| all hole groups shifted (dx, dz) | (−0.05, −0.05) · 0 · (+0.05, +0.05) | yes | REQ-01 … REQ-06, REQ-10 offset and U-03 coaxiality 0.0707; J-05 / D-01b / U-06 `min_wall` 4.950 and ring wall 4.9506 at the OD-C07 hole x −113.05 to the edge | +0.0293; J-05 +1.95 |

D-05a reads 14.000 in every variant: its rays start on the spec axes, so the edge at x −120 stays 7.0 away; the shifted hole wall shows in the J-05 ring wall (4.9506) instead. The STL sagitta is 0.004972 at worst (+0.005028). The OD-H11 clearance (16.4925), OD-H11 max z (−89.21), the OD-G01 pose read-back and every clearance between placed parts are the same in every variant, because none of them moves. The diameter margins of 0.0 are by construction (those variants sit on the spec's tolerance limits). The part passes over the whole swept range, not only at nominal.

## 5. Build facts

- Envelope 240.000 × 6.000 × 405.000 mm (x −120 … 120, y −6 … 0, z −305 … 100). Volume 580 355.904 mm³. Mass 737.05 g at 1270 kg/m³ (PETG, A-10). Centre of mass (0.089, −3.000, −102.371).
- Fillets: none. The four R 10.0 corners are sketch arcs (`RectangleRounded`), as plan §3.
- STL (the reference for the orchestrator's 3MF): **7068 triangles** (header and `mesh_census` agree), 353 484 bytes, **volume 580 358.524 mm³** (`mesh_census`; B-rep 580 355.904), **bounding box x −120.000 … 120.000, y −6.000 … 0.000, z −305.000 … 100.000** (read from the STL vertices), 1 body, 0 naked edges, consistent winding; tolerance 0.01 mm, angular 0.20 rad; written by `tools.core.write_stl` after clearing the cached triangulation.
- Placements (each a `RigidJoint` on the plate at the spec §4 joint, connected to the component's own STEP origin):
  - OD-C03 and OD-H01: `Location(Plane(origin=(0, 40, −205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))`, unchanged from v01. Holes measured at (−4, −239), (−4, −171), (37, −239), (37, −171).
  - OD-C04 and OD-H11: identity at (0, 70, −140), unchanged. Holes at (±40, −148), (±40, −114).
  - OD-G01 v02 (changed, spec 1.2 §4, A-01): `Location(Plane(origin=(0, 180.06, 32.0), x_dir=(1, 0, 0), z_dir=(0, −1, 0)))`, so local x → +X, local y → +Z, local z → −Y (read back as orientation (90, 0, 0), a proper rotation). Measured envelope x −50.000 … 50.000, y 176.760 … 205.000, z −18.000 … 82.000; downward planar faces at y 176.76 (the mouth), 180.06, 194.16 … 202.3.
  - Carrier foot box `od_c05_foot_reference_A01` (changed): x ±55, y 0 … 4, z −70 … −26 (measured envelope identical). A reference solid of the check assembly only (A-01).
- Reserved zones (spec §4, A-05 … A-08; prisms over the zone; heights: tray 36.9 (A-06 cup rest), valve 48 (OD-C07 envelope), tank and electronics 400; `clearance` of each placed solid; 0 would mean entering; **reported, not gated**):

  | Zone | OD-C03 | OD-H01 | OD-C04 | OD-H11 | OD-G01 | foot box |
  |---|---|---|---|---|---|---|
  | tray x ±75, z −15 … +85 | 150.0 | 163.15 | 92.0 | 74.21 | 139.86 | **11.0** |
  | tank x ±70, z −305 … −250 | **5.0** | 17.80 | 93.0 | 110.0 | 232.0 | 180.0 |
  | valve x −117 … −67, z −154 … −35 | 58.05 | 44.01 | 17.0 | 24.26 | 138.73 | 12.0 |
  | electronics x 70 … 120, z −240 … −30 | 28.0 | **14.5** | 20.0 | 27.16 | 26.41 | 15.0 |

  No placed solid enters a zone. The carrier foot box's gap to OD-C04's foot (z −107) is **37.0** (nearest (−50, 0, −70)); to the tray zone **11.0**.
- Hole webs (measured from `bore_census` axis positions: centre distance − r1 − r2; and from the D-05a rays):
  - nearest hole-to-hole on the plate: 16.00, carrier (±35, −40) to (±35, −60), unchanged;
  - the new holes: (−71, −148.5) to the drain (−80, −120) **23.887**; (−113, −148.5) to that drain 37.603; (−71, −42) to (−80, −120) 72.518; (−113, −42) to (−80, −120) 78.694; to the feet hole (−110, +90): 128.334 from (−113, −42), 133.941 from (−71, −42), 234.819 and 237.968 from the rear pair; (−71, −148.5) to OD-C04's (−40, −148) 27.004; (−71, −42) to the carrier's (−35, −40) 32.056; within the OD-C07 pattern 38.0;
  - hole-to-edge: **5.000** from (−113, −42) and (−113, −148.5) to the edge x −120 (ray at 180°), the thinnest wall on the plate (it sets `min_wall` 5.000).

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The plate lies flat and every placed part stands on its top face; the feet (±110, +90 / −295) enclose every placed part and the centre of mass (0.09, −102.4), so the machine cannot tip on its feet. |
| P2 | Function chains | Mount foot → M3 × 8 → insert in a Ø4.0 hole coaxial with the mount's Ø3.4 hole (offset 0.000); OD-C07's future foot → the four new inserts; plate → feet through Ø3.4; a leak → drains at x −80, one of them under OD-C07's hose window. |
| P3 | Motion clearance | Nothing moves; lowered straight down, the mounts meet no plate material before y 0 (clearance = lift at 10, 1, 0.1, 0). |
| P4 | Human factors | Inserts driven from the top; feet screwed from below; the group head mouth faces down at y 176.76 over the tray zone (z −15 … +85, centred under the mouth at z 32); the OD-C07 inserts at x −113 sit 5.0 from the left edge, reachable with the iron. |
| P5 | Absurdity next to a real product | A 240 × 405 × 6 mm, 737 g printed base under a compact espresso machine with the group head 176.76 … 205 above it is in proportion; for its span it is thin (REQ-09, §9). |
| P6 | Floating, embedded, mirrored, upside-down | Every mount touches y 0 with 0 mm³ overlap; the OEM parts float above by design (16.25, 16.49); the housing is upright with its wide rear face at y 205 above its mouth at y 176.76 (z 32 assembly section), a proper rotation; the carrier that joins it to the plate is not built yet (A-01), so the housing floats in the check assembly by design. |

## 7. Library and tools used

- Cards: none (plan §2: nothing matched).
- `tools.core`: `read_step`, `write_step` (AP242, part and assembly), `write_stl`, `compare_step`, `validity`, `common_volume`, `file_sha256`.
- `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `clearance`, `min_wall` / `min_wall_wide` (spacing 0.7), `overhang_census` (build_dir (0, 1, 0), spacing 0.7), `radial_extent` (D-05a, J-05 rings, hole-to-edge webs), `mesh_census`, `mass_properties`.
- `tools.drawing`: `write_sections` with `nothing_clipped`. `tools.result.gate` for every comparison.
- New code: only the job scripts. Missing tool: nothing in `tools/` writes or reads a 3MF; the 3MF clause of U-07 is the orchestrator's step (WP-03, WP-04), with the STL facts in §5 as its reference.
- K-2 (v01, still true): OD-H11's lowest point sits 16.4925 above the plate, 0.0075 under spec §3/§4's rounded 16.5; REQ-08 (≥ 10.0) holds by +6.4925. K-1 of v01 (the housing's lowest point) no longer applies: at the 1.2 pose the housing's lowest point is its mouth face, y 176.76, as spec §4 states.

## 8. Deviations from the plan

1. **Amendments of WP-04 (not deviations, recorded for traceability):** twenty insert holes (F05b, the OD-C07 pattern), census 30 cylindrical faces / 26 bores, top-face area rederived for 26 holes (96 725.984 mm²), OD-G01 at the 1.2 pose with read-back, carrier foot box x ±55, z −70 … −26, zones and webs reported.
2. **Versioned scripts:** v02 uses `build_od_c01_frame_v02.py`, `check_od_c01_frame_v02.py`, `sections_od_c01_frame_v02.py`, `sweep_od_c01_frame_v02.py`, so the v01 scripts stay as they are (WP-04: "leave every v01 file as it is").
3. **Row tags:** hole rows are tagged with `{:+g}` (for example `REQ-10.x-113_z-148.5`), so the half-millimetre OD-C07 z does not round into another hole's tag.
4. **OD-G01 pose read-back is gated** as sub-rows of U-03 (`U-03a.od_g01.pose.*`, band 0.005 mm) against the spec §4 values the U-03 row cites (rear face y 205.0, mouth face y 176.76, x ±50, z −18 … +82).
5. Carried from v01 and unchanged: the foot box in the assembly STEP (WP-03), no 3MF written (orchestrator step), U-04 on the assembly gated per part with OD-H11's volume row INCONCLUSIVE (A-14), D-03b derived from D-03a, the assembly built inside the build script, extra sections. Two sections added for the OD-C07 holes (z −42, x −113) and one assembly section through the vertical group head axis (z 32).
6. Fix cycles used: 0. Nothing failed; no geometry was changed after the first export.

## 9. What I am least sure of

1. **The 5.0 web between the OD-C07 outer inserts and the left edge.** It is the spec's figure (A-17), it passes J-05 (≥ 3.0) by +2.0 and D-05a (14.0 across ≥ 8.0), and it is now the thinnest wall of the plate. With an M3 × 5.7 × Ø4.6 insert (A-11) melted into the Ø4.0 hole, the material left to the edge is about 4.7, and a hot insert 5 mm from a free edge of PETG can bulge that edge. The gate is met; the risk is a print-and-press one the reviewer should weigh with A-11 and A-17.
2. **U-04 on the check assembly, for OD-H11** (as v01): OD-H11's volume changes 0.0524 mm³ on the first write (unsound input, OD-C04 A-14; second generation 2.9e-9), gated INCONCLUSIVE, not FAIL. The plate itself round-trips exactly.
3. **REQ-09 (Soft), flatness:** an unribbed 240 × 405 × 6 PETG plate printed flat may lift at the corners and creep under the tank. Risk MEDIUM; the first print answers it; C2 (ribbed) is the deferred geometric answer.

## 10. Stop

Not stopped.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-c01-base-frame",
 "part": "od_c01_frame",
 "tag": "v02",
 "spec_version": "1.2",
 "files": [
  {
   "path": "01_CAD/build_od_c01_frame_v02.py",
   "sha256": "65bb103fb32414dbca66057767facc0550fc20a2a79e8862de8f9dcc66108519"
  },
  {
   "path": "01_CAD/check_od_c01_frame_v02.py",
   "sha256": "1b17e65833118243422182e27a1ad871c65ee63fa62cb3f5c88633805f20b5ac"
  },
  {
   "path": "01_CAD/sections_od_c01_frame_v02.py",
   "sha256": "1a701812e5aa464e9e7a8c06df5258342666aebe8125483067555a458db80c88"
  },
  {
   "path": "01_CAD/sweep_od_c01_frame_v02.py",
   "sha256": "9f730619e086301d19d7afbb218213d57f5a73e97837dd0f1843401447d494aa"
  },
  {
   "path": "01_CAD/build_record_v02.json",
   "sha256": "d3efabdd7a6fe5362089182e9f65ca4569aeb3a11e4b0a827e21e77cb868807c"
  },
  {
   "path": "01_CAD/check_od_c01_frame_v02.json",
   "sha256": "e629e5555b94a10952302443ca89b1bcd73b89e40a2e27c0c3104d29dba19728"
  },
  {
   "path": "01_CAD/check_od_c01_frame_v02.log",
   "sha256": "383dcaf32f9610011a36ac3cf696cdfb0c8f683fd15361eed20e2bccaaeb8373"
  },
  {
   "path": "01_CAD/sections_v02.json",
   "sha256": "67b31897473368a6e9b70abae088c605d49dfb4ddddddcec85ad84197f3cb173"
  },
  {
   "path": "01_CAD/sweep_v02/sweep_summary_v02.json",
   "sha256": "38bfd098bf06cd107577c145d3e2c3ca2e6448976611a8ddf837a9f188a3a6e7"
  },
  {
   "path": "01_CAD/sweep_v02_run.log",
   "sha256": "0ff89c22200aabf77d22e8d4a57d0d01044ab7905a3c296a3df74f14e64d02bc"
  },
  {
   "path": "02_STEP_STL/od_c01_frame_C1_v02.step",
   "sha256": "7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805"
  },
  {
   "path": "02_STEP_STL/od_c01_assembly_C1_v02.step",
   "sha256": "07560bb0caafc1e986434eede5ae22abaef9f599437948145a8a3c18e2129749"
  },
  {
   "path": "02_STEP_STL/od_c01_frame_C1_v02.stl",
   "sha256": "26bf61039e5fcbc210643fb38cd188e31a66e7b5b6e065da6eb93ffa216125db"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_top_z-40_carrier.png",
   "sha256": "4f5e942c25f9f3876aa1098ddec6d4a84c648506a6b9e8daa15556588764d7a1"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_top_z-148_c04.png",
   "sha256": "7a49c0f651bc62ca766083d6a75211154f7f16c4e0af16fa721c9109dbfc9136"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_left_x37_c03.png",
   "sha256": "f277220f4e3d3e253c14fc5473606fa57f1169138a512c865ede0e7a1b374390"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_left_x65_bulkhead.png",
   "sha256": "e0696dd0380a374523a56c29db2fa4d6ce4c7a33190308c5064eb7d270eecb87"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_top_z-120_drain.png",
   "sha256": "830ff2b0ce9de90e13805289c4ea33e06df474e3c406a5ea62754e7b031df3d8"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_top_z90_feet.png",
   "sha256": "56ebdb7cefd23dbb3645f2f482f9ac66d4659d6cd40a341f38677dbcb626f0d4"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_top_z-42_valve.png",
   "sha256": "69de67f64fdd19acb87af1e2e083ded63d9b55661cd495081842a6cf3bbd56dd"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_left_x-113_valve.png",
   "sha256": "5002f1a3966f5b237d8a8f1078d2f6d176e18e0535aed58ee2624c0277be86a9"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_front_y-3_plan.png",
   "sha256": "88b9cbd2ec70692def33d72d97840269a2f51e02f23887b8e44a9900b778611a"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_left_asm_x0.png",
   "sha256": "3134671c9368d087f859d8a8b0fbb7bdc6e12c08c95ef92eb5d827fd4cee6afb"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_top_asm_z-148.png",
   "sha256": "7af641ca4644a3b94eab4a29e570131f839209ead0ed8561281c38be0ff3332b"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_left_asm_x37.png",
   "sha256": "4fe5dd02ceaadde3f871166e53edd1bf72f65d1b23823abea05f56af58f05d35"
  },
  {
   "path": "03_Sections/od_c01_frame_v02_top_asm_z32_mouth.png",
   "sha256": "e6826257791fe8263b8f9d32a55170bec8dc4b797a7ce0f81266b96658c2a2b6"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "cadquery-ocp-novtk 7.9.3.1.1",
  "repo_commit": "d7ea010502a30dd025c5123992847da1b15f3ee3"
 },
 "gates": [
  {
   "gate": "exactly_one_solid",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 26,
   "unit": "count",
   "required": "6 planar, 30 cylindrical (26 concave, 4 convex), 0 other, 26 bores",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec",
   "measured": 240.0,
   "unit": "mm",
   "required": "240.0 x 6.0 x 405.0 each +-0.1; position x +-120, y -6..0, z -305..100",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01",
   "measured": 1,
   "unit": "bool",
   "required": "solid_count 1, brep_valid 1, naked_edges 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02",
   "measured": 240.0,
   "unit": "mm",
   "required": "each in [spec - 0.1, spec + 0.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-03",
   "measured": 6.4925,
   "unit": "mm",
   "required": "contacts 0 / 0 mm3, coaxial <= 0.10, OD-H01 >= 2.0, OD-H11 >= 10.0, C03|C04 >= 2.0, OD-H11 max z <= -85.0, OD-G01 at the 1.2 pose (read back 205.0 / 176.76 / x +-50 / z -18..82) >= 2.0 to everything else; OD-H11 booleans INCONCLUSIVE by the row",
   "margin": 4.21,
   "at": "least clearance margin plate|OD-H11 16.4925; least z margin OD-H11 max z -89.21; OD-G01 least 110.780 to OD-H11",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "U-03a.plate|od_h11_thermoblock.interference",
   "measured": null,
   "unit": "mm3",
   "required": "<= 0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-02"
   ],
   "reason": "OD-H11 unsound (brep_valid 0, OD-C04 A-14), as the U-03 row states"
  },
  {
   "gate": "U-03a.od_g01|od_h11_thermoblock.interference",
   "measured": null,
   "unit": "mm3",
   "required": "<= 0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-01"
   ],
   "reason": "OD-H11 unsound (OD-C04 A-14); clearance 110.780"
  },
  {
   "gate": "U-04",
   "measured": 1.6e-07,
   "unit": "mm3",
   "required": "part: re-read unchanged, valid, label kept; assembly per part",
   "margin": -1.6e-07,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.od_h11_thermoblock.volume_delta",
   "measured": null,
   "unit": "mm3",
   "required": "<= 0",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [],
   "reason": "OD-H11 unsound (OD-C04 A-14); measured 0.0524 mm3 on the first write, 2.9e-9 on the second"
  },
  {
   "gate": "U-05",
   "measured": 26,
   "unit": "count",
   "required": "1 plate, 20 x 4.0, 4 x 3.4, 2 x 8.0 through",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-06",
   "measured": 5.0,
   "unit": "mm",
   "required": ">= 2.0 (Soft; spacing 0.7)",
   "margin": 3.0,
   "at": "(-115, -5.7, -42)",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07",
   "measured": 0.004972,
   "unit": "mm",
   "required": "sagitta <= 0.01; angular 0.20 <= 0.2310; 3MF: orchestrator step",
   "margin": 0.005028,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.3mf",
   "measured": null,
   "unit": "",
   "required": "the 3MF carries the same mesh",
   "margin": null,
   "at": null,
   "status": "ORCHESTRATOR_STEP",
   "assumes": []
  },
  {
   "gate": "U-08",
   "measured": null,
   "unit": "",
   "required": "N/A by the row",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "D-01a",
   "measured": 5.0,
   "unit": "mm",
   "required": ">= 0.8 (spacing 0.7)",
   "margin": 4.2,
   "at": "(-115, -5.7, -42)",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01b",
   "measured": 5.0,
   "unit": "mm",
   "required": ">= 2.0 (spacing 0.7)",
   "margin": 3.0,
   "at": "(-115, -5.7, -42)",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-02",
   "measured": 405.0,
   "unit": "mm",
   "required": "<= 420 x 420 x 500",
   "margin": 15.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "D-03a",
   "measured": 90.0,
   "unit": "deg",
   "required": ">= 45.0 (build +Y, spacing 0.7)",
   "margin": 45.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "D-03b",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 5",
   "margin": 5.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(110, -6, 90)",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-12"
   ]
  },
  {
   "gate": "D-05a",
   "measured": 14.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 6.0,
   "at": "(-113, -0.5, -42) at 180 deg, toward the edge x -120",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-11"
   ]
  },
  {
   "gate": "D-05b",
   "measured": 4.0,
   "unit": "mm",
   "required": "20 holes 4.0 +- 0.05, depth >= 5.7 (6.0), through",
   "margin": 0.05,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-11"
   ]
  },
  {
   "gate": "D-06a",
   "measured": 5.0,
   "unit": "mm",
   "required": ">= 1.0 (spacing 0.7)",
   "margin": 4.0,
   "at": "(-115, -5.7, -42)",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-07",
   "measured": null,
   "unit": "",
   "required": "N/A by the row",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "J-05",
   "measured": 5.0,
   "unit": "mm",
   "required": ">= 3.0 (min_wall 5.0; ring 5.0, all twenty inserts)",
   "margin": 2.0,
   "at": "(-113, -0.5, -42) at 180 deg",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "E-06",
   "measured": null,
   "unit": "",
   "required": "N/A by the row",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "REQ-01",
   "measured": 4.0,
   "unit": "mm",
   "required": "4.0 +- 0.05, offset <= 0.10 (0.000), through",
   "margin": 0.05,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-11"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 4.0,
   "unit": "mm",
   "required": "4.0 +- 0.05, offset <= 0.10 (0.000), through, coaxial with OD-C04",
   "margin": 0.05,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-11"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 4.0,
   "unit": "mm",
   "required": "4.0 +- 0.05, offset <= 0.10 (0.000), through, coaxial with OD-C03",
   "margin": 0.05,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03",
    "A-11"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 4.0,
   "unit": "mm",
   "required": "4.0 +- 0.05, offset <= 0.10 (0.000), through",
   "margin": 0.05,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04",
    "A-11"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 3.4,
   "unit": "mm",
   "required": "3.4 +- 0.1, offset <= 0.10 (0.000), through",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-12"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 8.0,
   "unit": "mm",
   "required": "8.0 +- 0.1, offset <= 0.10 (0.000), through",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "REQ-07",
   "measured": 0.0,
   "unit": "mm",
   "required": "top y 0.00 +- 0.10, 6.0 +- 0.1 thick, one plane",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01",
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-08",
   "measured": -89.21,
   "unit": "mm",
   "required": "OD-H11 max z <= -85.0; clearance >= 10.0 (16.4925)",
   "margin": 4.21,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "REQ-09",
   "measured": null,
   "unit": "",
   "required": "Soft bench: flat in service",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-10",
    "A-14"
   ]
  },
  {
   "gate": "REQ-10",
   "measured": 4.0,
   "unit": "mm",
   "required": "4.0 +- 0.05, offset <= 0.10 (0.000), through, against the pattern (no OD-C07 STEP)",
   "margin": 0.05,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-17",
    "A-11"
   ]
  }
 ],
 "sweep": [
  {
   "parameter": "plate_t",
   "values": [
    5.9,
    6.0,
    6.1
   ],
   "all_built": true,
   "worst_gate": "U-02.size_y / REQ-07.thickness",
   "worst_margin": 0.0
  },
  {
   "parameter": "insert_d",
   "values": [
    3.95,
    4.0,
    4.05
   ],
   "all_built": true,
   "worst_gate": "REQ-01..04, REQ-10 / D-05b diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "foot_d",
   "values": [
    3.3,
    3.4,
    3.5
   ],
   "all_built": true,
   "worst_gate": "REQ-05 diameter (D-04a +0.05)",
   "worst_margin": 0.0
  },
  {
   "parameter": "drain_d",
   "values": [
    7.9,
    8.0,
    8.1
   ],
   "all_built": true,
   "worst_gate": "REQ-06 diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "hole shift (dx, dz)",
   "values": [
    -0.05,
    0.0,
    0.05
   ],
   "all_built": true,
   "worst_gate": "REQ-01..06, REQ-10 offset / U-03 coaxial (J-05 min_wall 4.95, +1.95)",
   "worst_margin": 0.0293
  }
 ],
 "least_sure": [
  "the 5.0 web from the OD-C07 outer inserts (x -113) to the left edge: the plate's thinnest wall; J-05 +2.0; about 4.7 left beside a Dia 4.6 hot insert (A-11, A-17)",
  "U-04 on the check assembly: OD-H11 volume changes 0.0524 mm3 on the first write (unsound input, OD-C04 A-14), gated INCONCLUSIVE; the plate round-trips exactly",
  "REQ-09 flatness: an unribbed 240 x 405 x 6 PETG plate may lift at the corners; risk MEDIUM, answered by the first print"
 ],
 "stopped": false
}
```
