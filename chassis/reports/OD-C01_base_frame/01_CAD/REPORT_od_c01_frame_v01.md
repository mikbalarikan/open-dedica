# REPORT — od_c01_frame v01 (20260930-od-c01-base-frame)

Designer: Claude Code, Opus 5.5 · spec version 1.0 · plan `01_CAD/DESIGN_PLAN.md` (086dde81…aa7217) · brief WP-03 (J3, build attempt 1 of 2, fix_cycles 3) · 2026-09-30 UTC

Every number below was measured by `01_CAD/check_od_c01_frame.py` on the re-imported STEP files `02_STEP_STL/od_c01_frame_C1_v01.step` and `02_STEP_STL/od_c01_assembly_C1_v01.step`. The full rows (262, each with the measured value, margin, location, and reason) are in `01_CAD/check_od_c01_frame_v01.json`. The table in §3 gives each §5 row's governing (least-margin) sub-row. All eleven input hashes of WP-02 and the plan hash of WP-03 were checked before the build, and all of them match.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c01_frame.py` | 56ca631ea13ac5747e3c31d570dbe43c746f438ef17454f54d09af943474d160 | parametric script (plate and check assembly), Algebra mode |
| `01_CAD/check_od_c01_frame.py` | d63ebfbf8820e0bbfb61a7f230ac4f755d580a35d0cb9860e4d54010d722d58f | checks, written before the build (D3); U-04 assembly rows reclassified once before any sweep (§8) |
| `01_CAD/sections_od_c01_frame.py` | 46927a0673632ad9dbebc2418d0c1560567794719e4ac7d2ec07e095d00567e8 | D6 sections |
| `01_CAD/sweep_od_c01_frame.py` | cdf8620815cc42bf3a46b3ee6b905682b445921526b250c82e4cf48b30957528 | D7 sweep |
| `01_CAD/build_record_v01.json` | 885a2a9536362e366538034cd103807127abc34ad4e427ca3dc6d7f1070b11eb | parameters, export hashes, placements |
| `01_CAD/check_od_c01_frame_v01.json` | 4077465a9c86dcc03141ec7ee9ca7d9d6d615bd387a4a1f45f42feded91f6d0d | check results (all rows, facts) |
| `01_CAD/check_od_c01_frame_v01.log` | 7409daf59c8738ecc52c01d0a6f1ea1937c7dcd3e00a4c61eef4b8d313576085 | check console |
| `01_CAD/sections_v01.json` | 39732fea5904818e83e0d54e941fd7aa26bfc2a5d84e4d930cb60002f3129d8c | section planes, cut areas, nothing_clipped |
| `01_CAD/sweep_v01/sweep_summary_v01.json` | ee040e84a0feb56e1426dea11d30ac72648b4d9db4d8854dfd1955c6babce059 | sweep: per-variant status, worst margin per gate row |
| `01_CAD/sweep_v01_run.log` | 0ff89c22200aabf77d22e8d4a57d0d01044ab7905a3c296a3df74f14e64d02bc | sweep console |
| `02_STEP_STL/od_c01_frame_C1_v01.step` | 3337d684f655915c0ed5cb0cec33d03a94a5a29b61e9889a20d050851075e07c | AP242 (`tools.core.write_step`), one solid `od_c01_frame` |
| `02_STEP_STL/od_c01_assembly_C1_v01.step` | 632e52d9ef69175da3e205c40daf9c53c3dc5e4795bcf4933a72323ae51e841c | AP242 check assembly, 7 labelled solids (§5) |
| `02_STEP_STL/od_c01_frame_C1_v01.stl` | 2656262ec1f08f778a45386d6eee3699aa90e0a34018b618770231f10eafa21e | binary STL, `tools.core.write_stl` after clearing the triangulation; tolerance 0.01 mm / angular 0.20 rad; 6044 triangles |
| `03_Sections/od_c01_frame_v01_top_z-40_carrier.png` | 790711dd0e9b828aaecb8dac4efa3c7f4f89a3a9ed5e7bd1f32fc60bbe8a64e5 | z −40, carrier inserts; cut 1392.0 mm²; nothing clipped (0) |
| `03_Sections/od_c01_frame_v01_top_z-148_c04.png` | cd237979174e245cb5e44717b18a84e700f60c90cca3bdb2ca7c34b2a1ab74f1 | z −148, OD-C04 inserts; 1392.0 mm²; 0 |
| `03_Sections/od_c01_frame_v01_left_x37_c03.png` | 22f67e462e0a531cd5a5a6c3f186209efde4316d5a06b534c193ac59de7f8232 | x 37, OD-C03 inserts; 2382.0 mm²; 0 |
| `03_Sections/od_c01_frame_v01_left_x65_bulkhead.png` | 9eab0f9877f70f42b7c1a6977708d73ddaa77988b6d48cdf058356b00ca28a68 | x 65, bulkhead line; 2334.0 mm²; 0 |
| `03_Sections/od_c01_frame_v01_top_z-120_drain.png` | c2bc5868baafde783c81566102bc0e819cf7029d8e2d31e22f3783492f7ec44b | z −120, drain; 1392.0 mm²; 0 |
| `03_Sections/od_c01_frame_v01_top_z90_feet.png` | 38df1d08d7309cbd3334f7be0a6728d92172d8452eece7ff309cc0a9de34e57b | z +90, front feet holes; 1399.2 mm²; 0 |
| `03_Sections/od_c01_frame_v01_front_y-3_plan.png` | 4c8ac8d44ff575f5b2e50b5107c1fa193157e12c9ee7ed1c120c490715ff8aa4 | y −3 plan, all 22 holes; 96 776.25 mm²; 0 |
| `03_Sections/od_c01_frame_v01_left_asm_x0.png` | fc4f6154f8221f3b60c52dea2115d1c74f0fd3e1c33c5b8a3c810e170ad33f36 | assembly x 0: foot box, OD-C04 + OD-H11, OD-C03 + OD-H01, OD-G01; 0 |
| `03_Sections/od_c01_frame_v01_top_asm_z-148.png` | d9efaf597c92df4b6e04069d16ef8b67b112781efd29bba468710515cce2af37 | assembly z −148: OD-C04 foot on the plate; 0 |
| `03_Sections/od_c01_frame_v01_left_asm_x37.png` | bdae30bde6e4ad79b87b37bf1f9b4139b5f74682c3fab1993e8377e6df3f65f0 | assembly x 37: OD-C03 foot and holes on the plate; 0 |

The sweep exports (11 variants: STEP, assembly STEP, STL, build record, check results) are under `01_CAD/sweep_v01/<variant>/`, 49 MB, and are not deliverables. The cut areas agree with hand arithmetic from spec §4 (for example z −40: 240 × 6 − 2 × 4.0 × 6 = 1392).

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP (cadquery-ocp-novtk) 7.9.3.1.1 · ocpsvg 0.6.0 · repo commit d7ea010502a30dd025c5123992847da1b15f3ee3 (`tools/` clean)

## 3. Gate self-check

Bands are from GATES §0: mm 0.005, mm³ 0.001, degrees 0.001, counts and 1/0 facts 0. The margin is signed (positive inside). `min_wall`, `min_wall_wide` and `overhang_census` ran at **spacing 0.7 mm** (plan §4). The tool refuses the default spacing on the 405 × 240 face, and every value marked "sp 0.7" below came from that spacing.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | == 1 | 0 | — | PASS | — |
| feature_census | 6 planar, 26 cylindrical (22 concave, 4 convex), 0 cone / sphere / torus / B-spline / other, 22 bores | plan §3 counts | 0 | — | PASS | — |
| envelope_within_spec | size 240.000 × 6.000 × 405.000; position x −120.000 … 120.000, y −6.000 … 0.000, z −305.000 … 100.000 | each ± 0.1 | +0.1 | — | PASS | — |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | — | PASS | — |
| U-02 | 240.000 × 6.000 × 405.000 mm; position reported apart (above) | each in [spec − 0.1, spec + 0.1] | +0.1 | — | PASS | — |
| U-03 (a) plate\|OD-C03 | clearance 0.000; common volume 0.000 mm³; four holes coaxial, offset 0.000 each | = 0; ≤ 0; ≤ 0.10 | 0; 0; +0.10 | nearest (42, 0, −165) | PASS (assumed: A-03) | A-03 |
| U-03 (a) plate\|OD-C04 | clearance 0.000; 0.000 mm³; four holes coaxial, offset 0.000 each | = 0; ≤ 0; ≤ 0.10 | 0; 0; +0.10 | | PASS (assumed: A-02) | A-02 |
| U-03 (a) plate\|OD-H01 | clearance 16.250; common volume 0.000 mm³ | ≥ 2.0; ≤ 0 | +14.25 | | PASS (assumed: A-03) | A-03 |
| U-03 (a) plate\|OD-H11 | clearance 16.4925; boolean INCONCLUSIVE (OD-H11 brep_valid 0, OD-C04 A-14), as the row states | ≥ 10.0 | +6.4925 | | PASS (assumed: A-02); boolean INCONCLUSIVE by the row | A-02 |
| U-03 (a) OD-C03\|OD-C04 | clearance 8.000 | ≥ 2.0 | +6.0 | (42, 0, −165) / (42, 0, −157) | PASS (assumed: A-02, A-03) | A-02, A-03 |
| U-03 (a) OD-H11 max z | −89.210 | ≤ −85.0 | +4.21 | | PASS (assumed: A-02) | A-02 |
| U-03 (a) OD-G01 v02 at (0, 175, 0) | clearance to plate 125.000, OD-C03 169.425, OD-H01 166.286, OD-C04 127.942, OD-H11 73.554, carrier foot box 121.000; common volume 0.000 mm³ with every sound solid; with OD-H11 INCONCLUSIVE by the row | ≥ 2.0; ≤ 0 | +71.55 (least) | | PASS (assumed: A-01) | A-01 |
| U-03 (a) plate\|carrier foot box | clearance 0.000; 0.000 mm³ | = 0; ≤ 0 | 0 | | PASS (assumed: A-01) | A-01 |
| U-03 (a) assembly path (L-10) | OD-C03, OD-C04 and the foot box lowered along −Y: clearance to the plate 10.000, 1.000, 0.100, 0.000 at lifts 10, 1, 0.1, 0 | = lift | ≥ −6e-15 | | PASS (assumed: A-01 … A-03) | A-01 … A-03 |
| U-03 (b) | — | N/A by the row | — | — | N/A | — |
| U-04 part | schema AP242; 1 solid; volume delta 1.6e-7 mm³; faces delta 0 (32); label `od_c01_frame` kept; valid after 1 | 1; 1; ≤ 0; 0; 1; 1 | −1.6e-7 (inside band) | — | PASS | — |
| U-04 assembly | schema AP242; 7 solids; faces delta 0 (839); 7 labels kept; per part: plate, OD-C03, OD-H01, OD-C04, OD-G01 and foot box volume delta ≤ 1.6e-7 mm³, faces delta 0, valid after 1. OD-H11: faces delta 0, validity unchanged (0 → 0), **volume delta 0.0524 mm³ INCONCLUSIVE by OD-C04 A-14** (see §9) | as above | — | — | PASS for the part and 6 of 7 assembly parts; OD-H11 volume row INCONCLUSIVE | — |
| U-05 | 1 plate; 16 Ø4.000, 4 Ø3.400, 2 Ø8.000 through-holes; 22 bores | 1; 16; 4; 2 | 0 | — | PASS | — |
| U-06 (Soft) | `min_wall` wide 6.000 (sp 0.7) | ≥ 2.0 | +4.0 | (−119.65, −6.0, 91.97) | PASS | — |
| U-07 | STL sagitta 0.004972 at tol 0.01, angular 0.20 rad (limit 0.2310); delivered STL 1 body, 0 naked edges, consistent winding. 3MF clause: orchestrator step (brief WP-03) | ≤ 0.01; ≤ 0.2310 | +0.005028; +0.031 | (−82.79, −6.0, −232.86) | PASS (sagitta); 3MF: orchestrator step | — |
| U-08 | — | N/A by the row | — | — | N/A | — |
| D-01a | `min_wall` 6.000 (sp 0.7) | ≥ 0.8 | +5.2 | (−119.65, −6.0, 91.97) | PASS | — |
| D-01b | 6.000 (sp 0.7) | ≥ 2.0 | +4.0 | same | PASS | — |
| D-02 | 240.0 × 405.0 on the bed, 6.0 tall | ≤ 420 × 420 × 500 | +15.0 (z) | — | PASS (assumed: A-09) | A-09 |
| D-03a | least downward angle 90.0° off the bed (sp 0.7, build +Y) | ≥ 45° | +45.0 | — | PASS (assumed: A-14) | A-14 |
| D-03b | no downward face off the bed (D-03a: 0 samples under 45°), so span 0.0; every hole vertical (sections) | ≤ 5 | +5.0 | — | PASS (reviewer confirms from sections) | — |
| D-04a | four feet holes Ø3.400 | ≥ 3.25 | +0.15 | (±110, −6, 90 / −295) | PASS (assumed: A-12) | A-12 |
| D-05a | 36.000 across (least material radius 18.000 about an insert axis, 1776 rays, 0 unread) | ≥ 8.0 | +28.0 | (35, −0.5, −40) at 90°, toward (35, −60) | PASS (assumed: A-11) | A-11 |
| D-05b | 16 holes Ø4.000, length 6.000, through | 4.0 ± 0.05; ≥ 5.7 | +0.05; +0.3 | | PASS (assumed: A-11) | A-11 |
| D-06a | 6.000 (sp 0.7) | ≥ 1.0 | +5.0 | | PASS | — |
| D-07 | — | N/A by the row | — | — | N/A | — |
| J-05 | `min_wall` 6.000 (sp 0.7); located ring wall 16.000 | ≥ 3.0 | +3.0; +13.0 | ring: (35, −0.5, −40) | PASS | — |
| E-06 | — | N/A by the row | — | — | N/A | — |
| REQ-01 | 4 × Ø4.000 through, offset 0.000 at (±35, −40), (±35, −60) | 4.0 ± 0.05; ≤ 0.10 | +0.05; +0.10 | | PASS (assumed: A-01, A-11) | A-01, A-11 |
| REQ-02 | 4 × Ø4.000 through, offset 0.000; coaxial with OD-C04 (U-03) | same | +0.05; +0.10 | | PASS (assumed: A-02, A-11) | A-02, A-11 |
| REQ-03 | 4 × Ø4.000 through, offset 0.000; coaxial with OD-C03 (U-03) | same | +0.05; +0.10 | | PASS (assumed: A-03, A-11) | A-03, A-11 |
| REQ-04 | 4 × Ø4.000 through, offset 0.000 at (65, −45 / −105 / −165 / −225) | same | +0.05; +0.10 | | PASS (assumed: A-04, A-11) | A-04, A-11 |
| REQ-05 | 4 × Ø3.400 through, offset 0.000 | 3.4 ± 0.1; ≤ 0.10 | +0.10; +0.10 | | PASS (assumed: A-12) | A-12 |
| REQ-06 | 2 × Ø8.000 through, offset 0.000 | 8.0 ± 0.1; ≤ 0.10 | +0.10; +0.10 | | PASS (assumed: A-13) | A-13 |
| REQ-07 | max_y 0.000; thickness 6.000; 1 planar +Y face, own y extent 0.000, area 96 776.250 mm² (derived 96 776.250, information) | 0.00 ± 0.10; 6.0 ± 0.1; 1 plane | +0.10; +0.10; 0 | | PASS (assumed: A-01 … A-03 on top_y) | A-01 … A-03 |
| REQ-08 | OD-H11 max z −89.210; clearance(plate, OD-H11) 16.4925 | ≤ −85.0; ≥ 10.0 | +4.21; +6.4925 | | PASS (assumed: A-02) | A-02 |
| REQ-09 (Soft) | not geometric (bench) | flat in service | — | — | INCONCLUSIVE; risk MEDIUM (§9) | A-10, A-14 |

## 4. Robustness sweep (D7)

There are ten variants plus a nominal rebuild, one parameter at a time. The mounts stay at their fixed joints, and every variant runs the full predicate set, the assembly and path rows included. All 11 built exactly one solid. **No gate row failed in any variant.** The only rows that did not pass are the five that are INCONCLUSIVE or an orchestrator step by their own rows: the OD-H11 booleans ×2, OD-H11's assembly volume row, the whole-assembly volume, the 3MF clause, and REQ-09.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| plate_t (top held at y 0) | 5.9 · 6.0 · 6.1 | yes | U-02 / REQ-07 size_y 5.9; D-05b depth 5.9; J-05 min_wall 5.9 | 0.0 (in band); +0.2; +2.9 |
| insert_d | 3.95 · 4.00 · 4.05 | yes | REQ-01 … REQ-04, D-05b diameter 3.95 / 4.05 | 0.0 (at the tolerance edge, in band); D-05a 35.95, +27.95 |
| foot_d | 3.30 · 3.40 · 3.50 | yes | REQ-05 diameter; D-04a 3.30 | 0.0; +0.05 |
| drain_d | 7.90 · 8.00 · 8.10 | yes | REQ-06 diameter | 0.0 |
| all hole groups shifted (dx, dz) | (−0.05, −0.05) · 0 · (+0.05, +0.05) | yes | REQ-01 … REQ-06 offset, U-03 coaxiality 0.0707 | +0.0293 |

Worst D-05a across the sweep is 35.901 (holes_xz_low, +27.90). The worst STL sagitta is 0.004934 to 0.004972 (margin ≥ +0.00503). The OD-H11 clearance (16.4925), the OD-H11 max z (−89.21) and every clearance between mounts are the same in every variant, because the mounts do not move. The diameter margins of 0.0 are by construction: those variants sit exactly on the spec's tolerance limits. The part passes over the whole swept range, not only at nominal.

## 5. Build facts

- Envelope 240.000 × 6.000 × 405.000 mm (x −120 … 120, y −6 … 0, z −305 … 100). Volume 580 657.497 mm³. Mass 737.4 g at 1270 kg/m³ (PETG, A-10). Centre of mass (0.041, −3.000, −102.367).
- Fillets: none. The four R 10.0 corners are sketch arcs (`RectangleRounded`), not a fillet ladder, as plan §3 says.
- STL (the reference for the orchestrator's 3MF): 6044 triangles (header and `mesh_census` agree), 302 284 bytes, volume 580 659.617 mm³ (`mesh_census`; B-rep 580 657.497), bounding box x −120.000 … 120.000, y −6.000 … 0.000, z −305.000 … 100.000 (read from the STL's vertices), 1 body, 0 naked edges, consistent winding, SHA-256 2656262e…eafa21e.
- Placements. Each component is placed by a `RigidJoint` on the plate at the spec §4 joint, connected to the component's own STEP origin:
  - OD-C03 and OD-H01: `Location(Plane(origin=(0, 40, −205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))`, read back as orientation (0, 90, 180). Local x → +Z, y → −Y, z → +X, determinant +1 (plan §1). Foot underside measured on y 0 (clearance 0 to the top face, 0 mm³ common). Holes measured at (−4, −239), (−4, −171), (37, −239), (37, −171), Ø3.400.
  - OD-C04 and OD-H11: identity at (0, 70, −140). Holes Ø3.400 at (±40, −148), (±40, −114).
  - OD-G01 v02: identity at (0, 175, 0). Envelope x ±50.0, y 125.0 … 225.0, z −24.94 … +3.30.
  - Carrier foot box `od_c05_foot_reference_A01`: x ±50, y 0 … 4, z −69.94 … −24.94. It is a reference solid of the check assembly only (A-01), not a solid of the deliverable.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The plate lies flat, and every placed part stands on its top face. The feet (±110, +90 / −295) enclose every placed part and the centre of mass (0.04, −102.4), so the machine cannot tip on its feet. |
| P2 | Function chains | Mount foot → M3 × 8 screw → insert in a Ø4.0 plate hole coaxial with the mount's Ø3.4 hole (offset 0.000). Plate → feet through Ø3.4. A leak → drains at x −80, on the wet side, away from the electric zone x ≥ 70. |
| P3 | Motion clearance | Nothing moves. Lowered straight down, the mounts meet no plate material before y 0 (clearance = lift at 10, 1, 0.1, 0). |
| P4 | Human factors | Inserts are driven from the top. The feet screw from below. The tray zone at the front gets 131.9 mm under the housing's round body (K-1). The drains are reachable from below. |
| P5 | Absurdity next to a real product | A 240 × 405 × 6 mm, 737 g printed base under a compact espresso machine with a pump, thermoblock and group head is in proportion. For its span it is thin (REQ-09 risk, §9). |
| P6 | Floating, embedded, mirrored, upside-down | Every mount touches y 0 with 0 mm³ overlap. The OEM parts float above by design (16.25 and 16.49 to the plate). The OD-C03 rotation is proper (det +1) with the pump outlet toward −X. The x 0 and x 37 assembly sections show every part upright and on the plate. |

## 7. Library and tools used

- Cards: none (plan §2: nothing matched).
- `tools.core`: `read_step`, `write_step` (AP242, part and assembly), `write_stl`, `compare_step`, `validity`, `common_volume`, `file_sha256`.
- `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `clearance`, `min_wall` / `min_wall_wide` (spacing 0.7), `overhang_census` (build_dir (0, 1, 0), spacing 0.7), `radial_extent` (D-05a, J-05 rings), `mesh_census`, `mass_properties`.
- `tools.drawing`: `write_sections` with `nothing_clipped`. `tools.result.gate` for every comparison.
- New code: only the job scripts. The STL bounding box was read with a small struct parser in the check script (a corroboration for the 3MF step, not a gate).
- Missing tool: nothing in `tools/` writes or reads a 3MF. By brief WP-03, the 3MF clause of U-07 is the orchestrator's step, using the reference facts in §5.
- K-1 (a measured fact against spec §4 prose): OD-G01 v02 at the carrier's pose reaches **y 125.0** (envelope min_y 124.9999999) at its rear flange (x ±50, z −24.94 … −19.94). The spec's "lowest point y 131.9" is the round body in front of the flange (plan K-1). No geometry change.
- K-2 (a measured fact against spec §4 prose): OD-H11's lowest point sits **16.4925** above the plate (envelope min_y 16.49249; `clearance` 16.4925), 0.0075 under the spec's rounded 16.5. REQ-08 (≥ 10.0) holds by +6.4925. No geometry change.

## 8. Deviations from the plan

1. **The carrier foot box is in the assembly STEP**, as `od_c05_foot_reference_A01`. Plan §5 kept it out of the STEP. Brief WP-03 asks for it and names it. It remains a reference solid, not a deliverable.
2. **No 3MF was written.** Plan §2 and §6 planned a build123d `Mesher` 3MF with an INCONCLUSIVE clause. Per brief WP-03, the orchestrator writes it, and the check marks the clause "ORCHESTRATOR_STEP".
3. **U-04 on the assembly is gated per part.** Plan §6 compared OD-H11 by volume and faces. OD-H11's volume changes by 0.0524 mm³ on the first write, so that row, and the whole-assembly volume that contains it, read INCONCLUSIVE by OD-C04 A-14, with the measured value in the reason. Every other part is gated at the mm³ band. The reclassification was made in the check script after its first run (a light run, before the full check and the sweep). It is not a fix cycle: no geometry changed and nothing was re-exported.
4. **The assembly is built inside `build_od_c01_frame.py`** (`build_assembly`), not in a separate `assemble_od_c01_frame.py`. It uses the same Locations as plan §5, and the brief lists the build and check scripts only.
5. **D-03b** gets a derived reading from D-03a (no downward face off the bed, so span 0), as in the OD-C04 precedent. The plan's "reviewer, from sections" still stands.
6. **Sections:** a y −3 plan section and two more assembly sections (z −148, x 37) were added. The planned z −40 carrier section is plate-only; the foot box appears in the x 0 assembly section.

## 9. What I am least sure of

1. **U-04 on the check assembly, for OD-H11.** The delivered part round-trips exactly (volume delta 1.6e-7 mm³, 32 faces, label kept, valid). In the assembly, OD-H11's volume drops by 0.0524 mm³ (3.3e-7 of 159 766 mm³) on the first write, with faces unchanged. A second write of the re-read solid changes it by 2.9e-9 mm³. The volume is also frame-invariant (same at identity and placed), so the writer's rebuild of OD-H11's off-edge pcurve (its A-14 defect) is the likely cause. I gated that row INCONCLUSIVE, not FAIL, because OD-H11 is an unsound input solid, the same way the spec treats its booleans. The reviewer should decide whether that reading of U-04 is acceptable for a third-party solid in a check artifact.
2. **REQ-09 (Soft), flatness.** This is a plain 6.0 mm PETG plate, 240 × 405 mm, with no ribs, printed flat (A-10, A-14). Corner lift during printing and creep under the 1 kg tank are credible. I rate the risk MEDIUM. The deferred C2 (ribbed) is the geometric answer, and the first print answers the gate.
3. **The wall readings rest on spacing 0.7.** The 6.000 `min_wall` reading and the 90° overhang reading come from a coarser grid than the tool's default. The tool refuses the default on this face. The exact face-pair stage of `min_wall` and the located `radial_extent` rings (1776 rays, 0 unread: least ring wall 16.0 between (35, −40) and (35, −60)) cover the thin webs a coarse grid could miss.

## 10. Stop

Not stopped.

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20260930-od-c01-base-frame",
  "part": "od_c01_frame",
  "tag": "v01",
  "spec_version": "1.0",
  "files": [
    {"path": "01_CAD/build_od_c01_frame.py", "sha256": "56ca631ea13ac5747e3c31d570dbe43c746f438ef17454f54d09af943474d160"},
    {"path": "01_CAD/check_od_c01_frame.py", "sha256": "d63ebfbf8820e0bbfb61a7f230ac4f755d580a35d0cb9860e4d54010d722d58f"},
    {"path": "01_CAD/sections_od_c01_frame.py", "sha256": "46927a0673632ad9dbebc2418d0c1560567794719e4ac7d2ec07e095d00567e8"},
    {"path": "01_CAD/sweep_od_c01_frame.py", "sha256": "cdf8620815cc42bf3a46b3ee6b905682b445921526b250c82e4cf48b30957528"},
    {"path": "01_CAD/build_record_v01.json", "sha256": "885a2a9536362e366538034cd103807127abc34ad4e427ca3dc6d7f1070b11eb"},
    {"path": "01_CAD/check_od_c01_frame_v01.json", "sha256": "4077465a9c86dcc03141ec7ee9ca7d9d6d615bd387a4a1f45f42feded91f6d0d"},
    {"path": "01_CAD/check_od_c01_frame_v01.log", "sha256": "7409daf59c8738ecc52c01d0a6f1ea1937c7dcd3e00a4c61eef4b8d313576085"},
    {"path": "01_CAD/sections_v01.json", "sha256": "39732fea5904818e83e0d54e941fd7aa26bfc2a5d84e4d930cb60002f3129d8c"},
    {"path": "01_CAD/sweep_v01/sweep_summary_v01.json", "sha256": "ee040e84a0feb56e1426dea11d30ac72648b4d9db4d8854dfd1955c6babce059"},
    {"path": "01_CAD/sweep_v01_run.log", "sha256": "0ff89c22200aabf77d22e8d4a57d0d01044ab7905a3c296a3df74f14e64d02bc"},
    {"path": "02_STEP_STL/od_c01_frame_C1_v01.step", "sha256": "3337d684f655915c0ed5cb0cec33d03a94a5a29b61e9889a20d050851075e07c"},
    {"path": "02_STEP_STL/od_c01_assembly_C1_v01.step", "sha256": "632e52d9ef69175da3e205c40daf9c53c3dc5e4795bcf4933a72323ae51e841c"},
    {"path": "02_STEP_STL/od_c01_frame_C1_v01.stl", "sha256": "2656262ec1f08f778a45386d6eee3699aa90e0a34018b618770231f10eafa21e"},
    {"path": "03_Sections/od_c01_frame_v01_top_z-40_carrier.png", "sha256": "790711dd0e9b828aaecb8dac4efa3c7f4f89a3a9ed5e7bd1f32fc60bbe8a64e5"},
    {"path": "03_Sections/od_c01_frame_v01_top_z-148_c04.png", "sha256": "cd237979174e245cb5e44717b18a84e700f60c90cca3bdb2ca7c34b2a1ab74f1"},
    {"path": "03_Sections/od_c01_frame_v01_left_x37_c03.png", "sha256": "22f67e462e0a531cd5a5a6c3f186209efde4316d5a06b534c193ac59de7f8232"},
    {"path": "03_Sections/od_c01_frame_v01_left_x65_bulkhead.png", "sha256": "9eab0f9877f70f42b7c1a6977708d73ddaa77988b6d48cdf058356b00ca28a68"},
    {"path": "03_Sections/od_c01_frame_v01_top_z-120_drain.png", "sha256": "c2bc5868baafde783c81566102bc0e819cf7029d8e2d31e22f3783492f7ec44b"},
    {"path": "03_Sections/od_c01_frame_v01_top_z90_feet.png", "sha256": "38df1d08d7309cbd3334f7be0a6728d92172d8452eece7ff309cc0a9de34e57b"},
    {"path": "03_Sections/od_c01_frame_v01_front_y-3_plan.png", "sha256": "4c8ac8d44ff575f5b2e50b5107c1fa193157e12c9ee7ed1c120c490715ff8aa4"},
    {"path": "03_Sections/od_c01_frame_v01_left_asm_x0.png", "sha256": "fc4f6154f8221f3b60c52dea2115d1c74f0fd3e1c33c5b8a3c810e170ad33f36"},
    {"path": "03_Sections/od_c01_frame_v01_top_asm_z-148.png", "sha256": "d9efaf597c92df4b6e04069d16ef8b67b112781efd29bba468710515cce2af37"},
    {"path": "03_Sections/od_c01_frame_v01_left_asm_x37.png", "sha256": "bdae30bde6e4ad79b87b37bf1f9b4139b5f74682c3fab1993e8377e6df3f65f0"}
  ],
  "versions": {"python": "3.13.7", "build123d": "0.11.1", "ocp": "cadquery-ocp-novtk 7.9.3.1.1", "repo_commit": "d7ea010502a30dd025c5123992847da1b15f3ee3"},
  "gates": [
    {"gate": "exactly_one_solid", "measured": 1, "unit": "count", "required": "== 1", "margin": 0.0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "feature_census", "measured": 22, "unit": "count", "required": "6 planar, 26 cylindrical (22 concave, 4 convex), 0 other, 22 bores", "margin": 0.0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "envelope_within_spec", "measured": 240.0, "unit": "mm", "required": "240.0 x 6.0 x 405.0 each +-0.1; position x +-120, y -6..0, z -305..100", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-01", "measured": 1, "unit": "bool", "required": "solid_count 1, brep_valid 1, naked_edges 0", "margin": 0.0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-02", "measured": 240.0, "unit": "mm", "required": "each in [spec - 0.1, spec + 0.1]", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-03", "measured": 6.4925, "unit": "mm", "required": "contacts 0 / 0 mm3, coaxial <= 0.10, OD-H01 >= 2.0, OD-H11 >= 10.0, C03|C04 >= 2.0, OD-H11 max z <= -85.0, OD-G01 >= 2.0; OD-H11 booleans INCONCLUSIVE by the row", "margin": 4.21, "at": "least clearance margin: plate|OD-H11 16.4925; least z margin OD-H11 max z -89.21", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]},
    {"gate": "U-04", "measured": 1.6e-07, "unit": "mm3", "required": "part: re-read unchanged, valid, label kept; assembly per part", "margin": -1.6e-07, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-04.assembly.od_h11_thermoblock.volume_delta", "measured": null, "unit": "mm3", "required": "<= 0", "margin": null, "at": null, "status": "INCONCLUSIVE", "assumes": [], "reason": "OD-H11 unsound (OD-C04 A-14); measured 0.0524 mm3 on the first write, 2.9e-9 on the second"},
    {"gate": "U-05", "measured": 22, "unit": "count", "required": "1 plate, 16 x 4.0, 4 x 3.4, 2 x 8.0 through", "margin": 0.0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-06", "measured": 6.0, "unit": "mm", "required": ">= 2.0 (Soft; spacing 0.7)", "margin": 4.0, "at": "(-119.65, -6.0, 91.97)", "status": "PASS", "assumes": []},
    {"gate": "U-07", "measured": 0.004972, "unit": "mm", "required": "sagitta <= 0.01; angular 0.20 <= 0.2310; 3MF: orchestrator step", "margin": 0.005028, "at": "(-82.79, -6.0, -232.86)", "status": "PASS", "assumes": []},
    {"gate": "U-07.3mf", "measured": null, "unit": "", "required": "the 3MF carries the same mesh", "margin": null, "at": null, "status": "ORCHESTRATOR_STEP", "assumes": []},
    {"gate": "U-08", "measured": null, "unit": "", "required": "N/A by the row", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "D-01a", "measured": 6.0, "unit": "mm", "required": ">= 0.8 (spacing 0.7)", "margin": 5.2, "at": "(-119.65, -6.0, 91.97)", "status": "PASS", "assumes": []},
    {"gate": "D-01b", "measured": 6.0, "unit": "mm", "required": ">= 2.0 (spacing 0.7)", "margin": 4.0, "at": "(-119.65, -6.0, 91.97)", "status": "PASS", "assumes": []},
    {"gate": "D-02", "measured": 405.0, "unit": "mm", "required": "<= 420 x 420 x 500", "margin": 15.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-09"]},
    {"gate": "D-03a", "measured": 90.0, "unit": "deg", "required": ">= 45.0 (build +Y, spacing 0.7)", "margin": 45.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-14"]},
    {"gate": "D-03b", "measured": 0.0, "unit": "mm", "required": "<= 5", "margin": 5.0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "D-04a", "measured": 3.4, "unit": "mm", "required": ">= 3.25", "margin": 0.15, "at": "(110, -6, 90)", "status": "PASS_ASSUMED", "assumes": ["A-12"]},
    {"gate": "D-05a", "measured": 36.0, "unit": "mm", "required": ">= 8.0", "margin": 28.0, "at": "(35, -0.5, -40) at 90 deg", "status": "PASS_ASSUMED", "assumes": ["A-11"]},
    {"gate": "D-05b", "measured": 4.0, "unit": "mm", "required": "4.0 +- 0.05, depth >= 5.7 (6.0), through", "margin": 0.05, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-11"]},
    {"gate": "D-06a", "measured": 6.0, "unit": "mm", "required": ">= 1.0 (spacing 0.7)", "margin": 5.0, "at": "(-119.65, -6.0, 91.97)", "status": "PASS", "assumes": []},
    {"gate": "D-07", "measured": null, "unit": "", "required": "N/A by the row", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "J-05", "measured": 6.0, "unit": "mm", "required": ">= 3.0 (min_wall 6.0; ring 16.0)", "margin": 3.0, "at": "(-119.65, -6.0, 91.97)", "status": "PASS", "assumes": []},
    {"gate": "E-06", "measured": null, "unit": "", "required": "N/A by the row", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "REQ-01", "measured": 4.0, "unit": "mm", "required": "4.0 +- 0.05, offset <= 0.10 (0.000), through", "margin": 0.05, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-01", "A-11"]},
    {"gate": "REQ-02", "measured": 4.0, "unit": "mm", "required": "4.0 +- 0.05, offset <= 0.10 (0.000), through, coaxial with OD-C04", "margin": 0.05, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-02", "A-11"]},
    {"gate": "REQ-03", "measured": 4.0, "unit": "mm", "required": "4.0 +- 0.05, offset <= 0.10 (0.000), through, coaxial with OD-C03", "margin": 0.05, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-03", "A-11"]},
    {"gate": "REQ-04", "measured": 4.0, "unit": "mm", "required": "4.0 +- 0.05, offset <= 0.10 (0.000), through", "margin": 0.05, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-04", "A-11"]},
    {"gate": "REQ-05", "measured": 3.4, "unit": "mm", "required": "3.4 +- 0.1, offset <= 0.10 (0.000), through", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-12"]},
    {"gate": "REQ-06", "measured": 8.0, "unit": "mm", "required": "8.0 +- 0.1, offset <= 0.10 (0.000), through", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-13"]},
    {"gate": "REQ-07", "measured": 0.0, "unit": "mm", "required": "top y 0.00 +- 0.10, 6.0 +- 0.1 thick, one plane", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-01", "A-02", "A-03"]},
    {"gate": "REQ-08", "measured": -89.21, "unit": "mm", "required": "OD-H11 max z <= -85.0; clearance >= 10.0 (16.4925)", "margin": 4.21, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-02"]},
    {"gate": "REQ-09", "measured": null, "unit": "", "required": "Soft bench: flat in service", "margin": null, "at": null, "status": "INCONCLUSIVE", "assumes": ["A-10", "A-14"]}
  ],
  "sweep": [
    {"parameter": "plate_t", "values": [5.9, 6.0, 6.1], "all_built": true, "worst_gate": "U-02.size_y / REQ-07.thickness", "worst_margin": 0.0},
    {"parameter": "insert_d", "values": [3.95, 4.0, 4.05], "all_built": true, "worst_gate": "REQ-01..04 / D-05b diameter", "worst_margin": 0.0},
    {"parameter": "foot_d", "values": [3.3, 3.4, 3.5], "all_built": true, "worst_gate": "REQ-05 diameter (D-04a +0.05)", "worst_margin": 0.0},
    {"parameter": "drain_d", "values": [7.9, 8.0, 8.1], "all_built": true, "worst_gate": "REQ-06 diameter", "worst_margin": 0.0},
    {"parameter": "hole shift (dx, dz)", "values": [-0.05, 0.0, 0.05], "all_built": true, "worst_gate": "REQ-01..06 offset / U-03 coaxial", "worst_margin": 0.0293}
  ],
  "least_sure": [
    "U-04 on the check assembly: OD-H11 volume changes 0.0524 mm3 on the first write (unsound input, OD-C04 A-14), gated INCONCLUSIVE; the part itself round-trips exactly",
    "REQ-09 flatness: an unribbed 240 x 405 x 6 PETG plate may lift at the corners; risk MEDIUM, answered by the first print",
    "Wall and overhang readings at spacing 0.7 (the tool refuses the default on this face); covered by the exact face-pair stage and 1776 located ring rays"
  ],
  "stopped": false
}
```
