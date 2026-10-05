# RV02 — od_c01_frame_v03 (20260930-od-c01-base-frame) — 2026-10-05 UTC

Reviewer: Claude Code, Opus 5 · independent re-measurement; designer numbers are not trusted
Spec 1.3 · plan `01_CAD/DESIGN_PLAN.md` (with the amendments of `briefs/WP-03`, `WP-04`, `WP-06`) · report `01_CAD/REPORT_od_c01_frame_v03.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-02, A-03, A-04, A-09, A-10, A-11, A-12, A-13, A-14, A-17, A-18, A-19, A-20

Every value below was measured by the reviewer's own scripts in `reviews/RV02_work/`
(`r2_part.py`, `r3_holes.py`, `r4_walls.py`, `r5_asm.py`, `r6_rings.py`, `r7_mesh.py`,
`r8_3mf.py`, `r9_asm2.py`, `r10_sections.py`, `r11_mysections.py`, `r13_more.py`,
`r14_zones.py`, `c_fast.py`, `c_slow.py`, `c_clip.py`, `c_census.py`; results in the
matching `*.json`), run on the exported STEP, STL and 3MF files and on the delivered
input STEPs as placed in the check assembly. No designer script was read. Band
(GATES §0, as the spec and plan carry it): mm 0.005, mm³ 0.001, degrees 0.001, counts
and 1/0 facts 0. `min_wall`, `min_wall_wide` and `overhang_census` ran at spacing 0.7.

## 1. Files reviewed

All 48 files named in the brief are present and every SHA-256 matches the brief and
the REPORT. The principal ones:

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `00_Spec/DESIGN_SPEC.md` | e3a5f212e3a5c329fb4b8ae87356740db1e539d56dc81b5b215df718e8f18368 | yes |
| `01_CAD/DESIGN_PLAN.md` | 086dde812dcc207fa171977fb45f9d2ed5a8df324099bce8c813eb3651aa7217 | yes |
| `01_CAD/REPORT_od_c01_frame_v03.md` | 3b09d9015d14397d628740c11e4cd38c696123a52bdd3c55b746e08edac14bea | yes |
| `01_CAD/check_od_c01_frame_v03.json` | 7f8fa24be207662026f7bc852ce2256e3bd286036899d51f6058b27a7a1119d4 | yes |
| `01_CAD/build_record_v03.json` | 14578f5f82db4d6dfa67dc7fa3b182cfa0c69d3dab0b0cbe951909a010865467 | yes |
| `01_CAD/sections_v03.json` | d8918c006e9da6c26ac5721ed910194fbd20fce75a608d1f0c2bdb1fa976ee93 | yes |
| `01_CAD/sweep_v03/sweep_summary_v03.json` | dfa7b5270131c3ab10226f0f33a5659fe53e3ff339b884a15309ffcfee4a9867 | yes |
| `02_STEP_STL/od_c01_frame_C1_v03.step` | 87877a649306995965d4640f54cbf83c20715888b29eb057b18e2f2d2933d29b | yes |
| `02_STEP_STL/od_c01_assembly_C1_v03.step` | 44d2120be386438de18bc05f260043f49dbb9ae18ba7a4157fc553a0e56c4e74 | yes |
| `02_STEP_STL/od_c01_frame_C1_v03.stl` | 34d24746c62a6e1220544ce465d2714aa8f3b9631e3bf08d18e69937616af963 | yes |
| `02_STEP_STL/od_c01_frame_C1_v03.3mf` | 73ea066873137a834f4c45d25787160c2fbeaf5cc9cd4820272ed54206d0eef3 | yes (orchestrator step) |

The 23 section PNGs, the three plan briefs, `reviews/RV01_od_c01_frame_v02.md` and the
ten reference input STEPs also hash as the brief states. The delivery must carry
exactly these bytes.

**Revision B is exactly what it claims.** Against the v02 numbers recorded in RV01,
v03 differs by three arithmetic identities that admit only eighteen added Ø4.0 × 6.0
through-holes and nothing else: volume 580 355.904 → 578 998.736 mm³, a difference of
1 357.168 mm³ = 18 × π × 2.0² × 6.0 (1 357.168); top-face area 96 725.984 → 96 499.789
mm², a difference of 226.195 mm² = 18 × π × 2.0² (226.195); faces 36 → 54, a difference
of 18 cylindrical faces. The envelope, the outline, the thickness, the governing wall
(5.000 at (−115, −5.7, −42)) and the twenty v02 hole positions are unchanged, each of
the twenty measured at its spec position with offset 0.000. The material change (PETG
1270 → PLA 1240, A-10) moves only the mass figure, 737.05 → 717.958 g.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 / 1 / 0 | solid_count 1, brep_valid 1, naked_edges 0 | 0 | whole solid, label `od_c01_frame` | PASS | `validity` | — |
| U-02 | 240.000 × 6.000 × 405.000 mm | each in [spec − 0.1, spec + 0.1] | +0.100 | position reported apart: x −120.000 … 120.000, y −6.000 … 0.000, z −305.000 … 100.000 | PASS | `envelope` | — |
| U-03 | 0.000 mm | (a) designed contacts clearance = 0, interference ≤ 0 mm³; mount holes coaxial ≤ 0.10, the 1.3 parts ≤ 0.20; plate\|OD-H01 ≥ 2.0; plate\|OD-H11 ≥ 10.0; OD-C03\|OD-C04 ≥ 2.0; OD-H11 max z ≤ −85.0; OD-G01 ≥ 2.0 to everything; (b) N/A | 0 | thirteen seated parts each contact y 0 at clearance 0.000 with 0.000 mm³ shared (OD-C03, OD-C04, OD-C07, OD-C08, OD-C09, OD-C11, six OD-C16, the A-01 foot box); every coaxial offset 0.000 on all 26 plate-facing Ø3.4 holes; plate\|OD-H01 16.250; plate\|OD-H11 16.4925 (+6.4925, gated on distance: its boolean is INCONCLUSIVE by the row, OD-C04 A-14); OD-C03\|OD-C04 8.000; OD-H11 max z −89.210 (+4.210); OD-G01 read back rear face y 205.000, mouth y 176.760, x ±50.000, z −18.000 … 82.000, least clearance 8.776 to OD-C09 (+6.776); assembly path: clearance = lift exactly at 10, 1, 0.1 and 0 mm with 0.000 mm³ shared at every station, all thirteen lowered together along −Y | PASS (assumed: A-01 … A-03, A-17 … A-20) | `clearance`, `common_volume`, `bore_census` + `locate_bore` on both solids, `envelope` | A-01, A-02, A-03, A-17, A-18, A-19, A-20 |
| U-04 | 0.000 mm³ | named body re-read unchanged, no stray shells, valid after re-import | 0 (band 0.001) | plate STEP: AP242, mm, 1 solid, volume delta 0.000 mm³, faces delta 0 (54), label `od_c01_frame` kept, valid after 1. Check assembly (not the gated target): 17 labels kept, volume delta 0.000 mm³, faces delta 0; `valid_after` 0 because OD-H11 is brep_valid 0 on input (F3) | PASS | `compare_step`, `validity` | — |
| U-05 | 44 bores | 1 plate; 38 Ø4.0, 4 Ø3.4, 2 Ø8.0 through-holes | 0 | 38 Ø4.000 + 4 Ø3.400 + 2 Ø8.000 = 44, every one through, length 6.000; 6 planar and 48 cylindrical faces (44 concave, 4 convex), 0 cone / sphere / torus / B-spline / other | PASS | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 | 5.000 mm | ≥ 2.0 (Soft, `min_wall` wide) | +3.000 | (−115.0, −5.7, −42.0), the web from the OD-C07 insert hole at x −113 to the edge x −120; spacing 0.7 | PASS | `min_wall_wide(spacing=0.7)` | — |
| U-07 | 0.004975 mm | STL at tol 0.01, angular ≤ 4·acos(1 − 0.01/6.0) = 0.230972 rad; `stl_max_sagitta` ≤ 0.01; the 3MF carries the same mesh | +0.005025 | delivered STL vs B-rep `mesh_deviation` 0.0049750 at (−77.664, −3.000, −226.753); reviewer re-mesh at tol 0.01 / 0.20 rad reproduces 11 676 triangles with sagitta 0.0049723 and an identical census, so the delivery is the D5 export from a cleared triangulation; STL 11 676 triangles, 1 body, 0 naked edges, winding consistent, volume 579 003.604 vs B-rep 578 998.736 (+4.868 mm³, inside the chordal tolerance), box x ±120.000, y −6.000 … 0.000, z −305.000 … 100.000; 3MF: unit millimetre, 5 752 vertices, 11 676 triangles, every triangle equal to the STL's to 1.0e-5 mm (the 3MF's 5-decimal text), volume 579 003.604 mm³ | PASS | `write_stl`, `mesh_sagitta`, `mesh_deviation`, `mesh_census`, reviewer 3MF parse | — |
| U-08 | — | N/A by the row: it applies to threaded parts and this target has none | — | — | N/A | — | — |
| D-01a | 5.000 mm | ≥ 0.8 | +4.200 | (−115.0, −5.7, −42.0); spacing 0.7 | PASS | `min_wall(spacing=0.7)` | — |
| D-01b | 5.000 mm | ≥ 2.0 | +3.000 | (−115.0, −5.7, −42.0); spacing 0.7 | PASS | `min_wall(spacing=0.7)` | — |
| D-02 | 405.000 mm | each envelope size ≤ 420 × 420 × 500, flat | +15.000 | 240.0 × 405.0 on the bed, 6.0 tall | PASS (assumed: A-09) | `envelope` | A-09 |
| D-03a | 90.000 deg | ≥ 45 (build +Y) | +45.000 | nothing downward off the bed: every face is the bed face, the top face, a vertical side or a vertical bore wall; spacing 0.7 | PASS (assumed: A-14) | `overhang_census(build_dir=(0,1,0), spacing=0.7)` | A-14 |
| D-03b | 0.000 mm | span ≤ 5 | +5.000 | no flat ceiling off the bed; the reviewer's own plan section at y −3 and the twelve plate sections show one connected plate with 44 vertical through-holes and nothing overhead | PASS | `flat_ceiling_spans(build_dir=(0,1,0), max_span=5.0, spacing=0.7)`; reviewer sections | — |
| D-04a | 3.400 mm | the four feet holes Ø ≥ 3.25 | +0.150 | (±110.0, −6 … 0, +90.0) and (±110.0, −6 … 0, −295.0), offset 0.000, through, length 6.000 | PASS (assumed: A-12) | `locate_bore` | A-12 |
| D-05a | 14.000 mm | material ≥ 8.0 across around each Ø4.0 hole | +6.000 | least over 38 holes × 72 rays (2 736 rays, 1 unread): least material radius 7.000 at (−113.0, −0.5, −42.0) and (−113.0, −0.5, −148.5) at 180°, toward the edge x −120; next least 14.000 across at (106, −78 / −222) | PASS (assumed: A-11) | `radial_extent` | A-11 |
| D-05b | 4.000 mm | 38 holes Ø 4.0 ± 0.05, depth ≥ 5.7 (through) | +0.050 (Ø); +0.300 (depth) | all 38 read Ø4.000, length 6.000, through, offset 0.000 from their spec axes | PASS (assumed: A-11) | `bore_census`, `locate_bore` | A-11 |
| D-06a | 5.000 mm | ≥ 1.0 | +4.000 | (−115.0, −5.7, −42.0); spacing 0.7 | PASS | `min_wall(spacing=0.7)` | — |
| D-07 | — | N/A by the row: no fit-critical bore on this part | — | — | N/A | — | — |
| J-05 | 5.000 mm | ≥ 3.0 around each of the thirty-eight insert holes | +2.000 | `min_wall` 5.000 at (−115.0, −5.7, −42.0); the located ring wall (least material radius − 2.000) is 5.000 at (−113, −0.5, −42) and (−113, −0.5, −148.5) at 180°, 12.000 at (106, −78 / −222), ≥ 13.5 at every other new hole | PASS | `min_wall(spacing=0.7)`, `radial_extent` | — |
| E-06 | — | N/A by the row: no bosses on this part | — | — | N/A | — | — |
| REQ-01 | 4.000 mm | 4 × Ø4.0 ± 0.05 through along Y at (±35, −40), (±35, −60), offset ≤ 0.10 | +0.050 (Ø); +0.100 (offset) | all four Ø4.000, offset 0.000, length 6.000, through | PASS (assumed: A-01, A-11) | `locate_bore` | A-01, A-11 |
| REQ-02 | 4.000 mm | 4 × Ø4.0 ± 0.05 at (±40, −148), (±40, −114), offset ≤ 0.10, coaxial with OD-C04 | +0.050; +0.100 | all four Ø4.000, offset 0.000; OD-C04's four Ø3.4 holes coaxial, offset 0.000 each | PASS (assumed: A-02, A-11) | `locate_bore` | A-02, A-11 |
| REQ-03 | 4.000 mm | 4 × Ø4.0 ± 0.05 at (−4, −239), (−4, −171), (37, −239), (37, −171), offset ≤ 0.10, coaxial with OD-C03 | +0.050; +0.100 | all four Ø4.000, offset 0.000; OD-C03's four Ø3.4 holes coaxial, offset 0.000 each | PASS (assumed: A-03, A-11) | `locate_bore` | A-03, A-11 |
| REQ-04 | 4.000 mm | 4 × Ø4.0 ± 0.05 at (65, −45 / −105 / −165 / −225), offset ≤ 0.10 | +0.050; +0.100 | all four Ø4.000, offset 0.000, through (see F4 on their fastener) | PASS (assumed: A-04, A-11) | `locate_bore` | A-04, A-11 |
| REQ-05 | 3.400 mm | 4 × Ø3.4 ± 0.1 at (±110, +90), (±110, −295), offset ≤ 0.10 | +0.100; +0.100 | all four Ø3.400, offset 0.000, through | PASS (assumed: A-12) | `locate_bore` | A-12 |
| REQ-06 | 8.000 mm | 2 × Ø8.0 ± 0.1 at (−80, −120), (−80, −230), offset ≤ 0.10 | +0.100; +0.100 | both Ø8.000, offset 0.000, through, in the wet zone | PASS (assumed: A-13) | `locate_bore` | A-13 |
| REQ-07 | 0.000 mm | top face y = 0.00 ± 0.10, 6.0 ± 0.1 thick, the whole top face one plane | +0.100 (y); +0.100 (thickness) | `envelope` max_y 0.000, size_y 6.000; exactly one planar face whose normal is +Y, its own y extent 0.000 … 0.000, area 96 499.789 mm² (= 240 × 405 − 4 × (4 − π) × 10² /4 corners − 44 bore mouths, and 226.195 mm² less than v02's for the eighteen new holes) | PASS | `envelope`, face listing, reviewer sections | — |
| REQ-08 | −89.210 mm | OD-H11 max z ≤ −85.0 and clearance(plate, OD-H11) ≥ 10.0 | +4.210 (z); +6.4925 (clearance) | OD-H11 as placed: envelope z −140.000 … −89.210 (the outlet pins), min_y 16.4925 above the plate; clearance measured on distance, not on a boolean | PASS (assumed: A-02) | `envelope`, `clearance` | A-02 |
| REQ-09 | — | Soft: the printed plate stays flat enough for the mounts to seat without rocking | — | not a geometric quantity; no bench print exists | INCONCLUSIVE (F1, risk MEDIUM) | — (bench, by the row) | A-10, A-14 |
| REQ-10 | 4.000 mm | 4 × Ø4.0 ± 0.05 at (−113, −42), (−71, −42), (−113, −148.5), (−71, −148.5), offset ≤ 0.10, coaxial with OD-C07 ≤ 0.20 | +0.050; +0.100; +0.200 | all four Ø4.000, offset 0.000; the delivered OD-C07 placed by the A-17 joint reads back x −117.000 … −67.000, y 0.000 … 48.000, z −154.000 … −35.000, contact 0.000, 0.000 mm³ shared, its four Ø3.400 footprint holes coaxial, offset 0.000 each | PASS (assumed: A-17, A-11) | `locate_bore`, `clearance`, `common_volume` | A-17, A-11 |
| REQ-11 | 4.000 mm | 4 × Ø4.0 ± 0.05 at (88, −222), (106, −222), (88, −78), (106, −78), offset ≤ 0.10, coaxial with OD-C08 ≤ 0.20; ≥ 6.0 centre to centre; ≥ 8.0 from the plate edge | +0.050; +0.100; +12.000 (c-c); **+6.000 (edge)** | all four Ø4.000, offset 0.000; OD-C08 at the identity: contact 0.000, 0.000 mm³, four Ø3.400 flange holes coaxial, offset 0.000; least centre to centre 18.000; least to the outline **14.000** at x 106 (the side x = 120), the governing edge distance of the whole part | PASS (assumed: A-18, A-11) | `locate_bore`, `bore_census` axes, outline distance | A-18, A-11 |
| REQ-12 | 4.000 mm | 4 × Ø4.0 ± 0.05 at (±81, −282), (±95, −282), offset ≤ 0.10, coaxial with OD-C11 ≤ 0.20; ≥ 8.0 from the plate edge | +0.050; +0.100; +15.000 (edge); +8.000 (c-c, WP-06) | all four Ø4.000, offset 0.000; OD-C11 at the identity: contact 0.000, 0.000 mm³, four Ø3.400 flange holes coaxial, offset 0.000; least centre to centre 14.000; to the outline 23.000 each (the rear edge z = −305) | PASS (assumed: A-18, A-11) | `locate_bore`, `bore_census` axes, outline distance | A-18, A-11 |
| REQ-13 | 4.000 mm | 6 × Ø4.0 ± 0.05 at (±104.5, −262), (±104.5, −15), (±104.5, +62), offset ≤ 0.10, coaxial with the six OD-C16 ≤ 0.20; ≥ 8.0 from the edge; ≥ 6.0 centre to centre | +0.050; +0.100; +7.500 (edge); +11.755 (c-c) | all six Ø4.000, offset 0.000; the six brackets at the A-19 poses (right (117, 0, z_c); left 180° about Y then (−117, 0, z_c)): each contact 0.000, 0.000 mm³, its Ø3.400 hole coaxial, offset 0.000; least centre to centre 17.755; to the outline 15.500 each (the sides x = ±120) | PASS (assumed: A-19, A-11) | `locate_bore`, `bore_census` axes, outline distance | A-19, A-11 |
| REQ-14 | 4.000 mm | 4 × Ø4.0 ± 0.05 at (±85, +77), (±95, +77), offset ≤ 0.10, coaxial with OD-C09 ≤ 0.20; ≥ 8.0 from the edge; ≥ 6.0 centre to centre | +0.050; +0.100; +15.000 (edge); **+4.000 (c-c)** | all four Ø4.000, offset 0.000; OD-C09 at the identity: contact 0.000, 0.000 mm³, four Ø3.400 flange holes coaxial, offset 0.000; least centre to centre **10.000** (the ±85 / ±95 pairs), the tightest hole spacing on the part, a 6.000 web wall to wall; to the outline 23.000 each (the front edge z = +100) | PASS (assumed: A-20, A-11) | `locate_bore`, `bore_census` axes, outline distance | A-20, A-11 |

Outline distances are measured to the plate's real boundary, the rounded rectangle
whose core is x ∈ [−110, 110], z ∈ [−295, 90] dilated by R 10, so the four corner arcs
are included and only their own quadrant counts; the reviewer's first, naive formula
(distance to each corner's full circle) read 9.849 at (±95, −282) and was wrong — the
nearest point of that circle is not on the arc. Every hole's centre-to-centre figure is
the distance from its measured `bore_census` axis to the nearest other measured axis.

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 plate | 1 solid, 240 × 6 × 405, corners R 10, top at y 0 | 1 solid, 240.000 × 6.000 × 405.000, 4 convex cylinders of r 10.000 at the corners, 6 planar faces, one +Y plane at y 0.000 | PASS |
| F02 carrier insert holes ×4 | Ø4.0 through along Y at (±35, −40), (±35, −60) | 4 × Ø4.000, through, length 6.000, offset 0.000 | PASS |
| F03 thermoblock-mount insert holes ×4 | Ø4.0 through at (±40, −148), (±40, −114) | 4 × Ø4.000, through, offset 0.000 | PASS |
| F04 pump-cradle insert holes ×4 | Ø4.0 through at (−4, −239), (−4, −171), (37, −239), (37, −171) | 4 × Ø4.000, through, offset 0.000 | PASS |
| F05 bulkhead insert holes ×4 | Ø4.0 through at (65, −45 / −105 / −165 / −225) | 4 × Ø4.000, through, offset 0.000 | PASS |
| F05a OD-C07 insert holes ×4 (spec 1.1, REQ-10) | Ø4.0 through at (−113, −42), (−71, −42), (−113, −148.5), (−71, −148.5) | 4 × Ø4.000, through, offset 0.000 | PASS |
| F05c OD-C08 tray inserts ×4 (WP-06, REQ-11) | Ø4.0 through at (88, −222), (106, −222), (88, −78), (106, −78) | 4 × Ø4.000, through, offset 0.000 | PASS |
| F05d OD-C11 back-panel inserts ×4 (WP-06, REQ-12) | Ø4.0 through at (±81, −282), (±95, −282) | 4 × Ø4.000, through, offset 0.000 | PASS |
| F05e OD-C16 bracket inserts ×6 (WP-06, REQ-13) | Ø4.0 through at (±104.5, −262), (±104.5, −15), (±104.5, +62) | 6 × Ø4.000, through, offset 0.000 | PASS |
| F05f OD-C09 front-panel inserts ×4 (WP-06, REQ-14) | Ø4.0 through at (±85, +77), (±95, +77) | 4 × Ø4.000, through, offset 0.000 | PASS |
| F06 feet holes ×4 | Ø3.4 through at (±110, +90), (±110, −295) | 4 × Ø3.400, through, offset 0.000 | PASS |
| F07 drain holes ×2 | Ø8.0 through at (−80, −120), (−80, −230) | 2 × Ø8.000, through, offset 0.000 | PASS |
| F08 clean-up | one solid, no stray faces | `solid_count` 1, `brep_valid` 1, `naked_edges` 0; 54 faces, 0 cone / sphere / torus / B-spline / other | PASS |

Totals: 38 Ø4.0 + 4 Ø3.4 + 2 Ø8.0 = 44 bores, every one through along Y, in a single
solid. No plan feature is missing and nothing unplanned is present.

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity: does every part rest and mount the way the product is used? | The plate lies flat on four feet at (±110, +90) and (±110, −295) and all thirteen placed parts stand on its top face y 0 at clearance 0.000 with 0.000 mm³ shared; the feet rectangle 220 × 385 encloses the centre of mass (0.038, −3.000, −102.370) and every placed part's footprint, so the machine cannot tip on its feet. | YES |
| P2 | Function chains connected and aimed (air, drive, liquid, cable)? | Each mount's and panel's Ø3.4 foot hole is coaxial (offset 0.000) with a Ø4.0 plate hole taking an M3 × 5.7 insert driven from the top, so every screw enters from above; the OD-C16 bracket carries the chain on to the side panel sideways; the four feet take M3 × 12 through Ø3.4 from the top; a leak leaves by the two Ø8.0 drains at x −80 in the wet zone, one at (−80, −120) under OD-C07's hose window. | YES |
| P3 | Moving parts oriented for their motion, with clearance? | Nothing on this plate moves; the assembly motion was swept by lowering all thirteen seated parts together along −Y, and clearance equals the lift exactly at 10, 1, 0.1 and 0 mm with 0.000 mm³ shared at every station, so each reaches its seat without meeting plate material on the way. | YES |
| P4 | Human factors: grip, reach, insertion direction obvious? | Every insert hole is a through-hole entered from the top, so the insert iron and the driver work from above with the panels off; the tightest reach is 14.000 mm from a hole axis to the plate edge (x 106) and 10.000 mm between two hole axes (±85 / ±95 at z +77); the bracket counterbores face up (reviewer section x 104.5), so their screws also go downward; the group head mouth faces down at y 176.760 over the tray zone. | YES |
| P5 | Next to a comparable real product, does anything look absurd? | A 240 × 405 × 6 mm, 718 g flat printed base carrying a pump, a thermoblock, a group head at y 175, an electronics bay, two side brackets per side and front and back panels is in proportion with a De'Longhi Dedica's footprint; it is wider because every panel screws to it, and the only odd figure is 6 mm over a 405 mm span, which is exactly what REQ-09 asks the first print. | YES |
| P6 | Nothing floating, embedded, mirrored, or upside-down? | Every seated part touches y 0 with 0.000 mm³ shared, so nothing is embedded and nothing floats; the OEM parts stand off by design (pump 16.250, thermoblock 16.4925); the six brackets sit three per side at x ±117 with their counterbores up, the left three turned 180° about Y so neither side is mirrored into the plate; the back panel is at z −302 … −277 and the front panel at z +72 … +97, each on its own end; the reviewer's plan section at y −3 shows one connected plate with all 44 holes inside the outline. | YES |

No NO. The reviewer's own sections (`reviews/RV02_work/sections/`) reproduce the
designer's cut areas exactly: plan y −3 96 499.789 mm², plate z +77 1 344.000, plate
x 104.5 2 326.251, assembly x 0 9 598.605, assembly z +77 1 982.684, assembly z −282
1 545.600, assembly x 104.5 4 775.351. All 23 delivered section PNGs read
`nothing_clipped` 0.

## 5. Positive controls

Every mutant is this job's own plate (or its placed neighbour) altered by the
reviewer's scripts `c_fast.py`, `c_slow.py`, `c_clip.py` and `c_census.py`; the
mutants are in `reviews/RV02_work/mutants/`. Four families are covered: resize,
relocate, remove/add, degrade.

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` (U-01) | add: a detached 10 mm cube 50 mm above the plate | FAIL — `solid_count` 2 (need 1) |
| `envelope` (U-02, D-02, REQ-07, REQ-08) | resize: a 0.5 mm strip added on the front edge | FAIL — size_z 405.500 (need 405.0 ± 0.1) |
| `locate_bore` offset (U-03, U-05, REQ-01 … REQ-06, REQ-10 … REQ-14) | relocate: the whole plate moved +0.5 mm in x, so every hole sits 0.5 mm off its spec position | FAIL — offset 0.5000 mm at the REQ-13 hole (104.5, −15) (need ≤ 0.10) |
| `locate_bore` diameter (D-04a, D-05b) | degrade: the REQ-11 hole (88, −78) opened out to Ø6.0 | FAIL — Ø6.000 (need 4.0 ± 0.05) |
| `bore_census`, `feature_census` (U-05) | add: an extra Ø4.0 through-hole at (92, +77) | FAIL — 45 bores and 49 cylindrical faces (need 44 and 48) |
| `compare_step` volume and faces (U-04) | remove: the delivered solid read back against the opened-hole STEP | FAIL — volume delta 94.248 mm³ (need ≤ 0, band 0.001) |
| `compare_step` labels (U-04) | remove: the body relabelled `not_od_c01_frame` | FAIL — labels 0 (need the name kept) |
| `clearance` (U-03, REQ-08) | relocate: OD-C04 lifted 1 mm off the plate | FAIL — contact clearance 1.0000 mm (need = 0) |
| `common_volume` / interference (U-03) | relocate: OD-C04 sunk 1 mm into the plate | FAIL — 4 948.2 mm³ shared (need ≤ 0) |
| coaxiality: `bore_census` + `locate_bore` on both solids (U-03) | relocate: OD-C08 shifted 0.5 mm in x over its plate holes | FAIL — coaxial offset 0.5000 mm (need ≤ 0.20) |
| `min_wall` (D-01a, D-01b, D-06a, J-05) | degrade: an extra Ø4.0 insert hole at (−117.5, −42), 0.5 mm from the left edge | FAIL — 0.5000 mm at (−119.5, −0.3, −42.0) (need ≥ 2.0, ≥ 3.0, ≥ 1.0, ≥ 0.8) |
| `min_wall_wide` (U-06) | the same thinned-web mutant | FAIL — 0.5000 mm (need ≥ 2.0) |
| `radial_extent` (D-05a, J-05 ring wall) | the same thinned-web mutant | FAIL — 5.000 mm across, ring 0.500 mm (need ≥ 8.0 and ≥ 3.0) |
| `overhang_census` (D-03a) | degrade: a 10 × 2 mm pocket milled into the bed face at z −160, leaving a flat ceiling 2 mm above the bed | FAIL — least 0.0° at (−5.0, −4.0, −190.0) (need ≥ 45°) |
| `flat_ceiling_spans` (D-03b) | the same pocket mutant | FAIL — span 10.500 mm at (−0.25, −4.0, −170.95) (need ≤ 5) |
| `write_stl` / `mesh_sagitta` (U-07) | degrade: the part remeshed at tolerance 0.05 mm | FAIL — sagitta 0.023448 mm (need ≤ 0.01) |
| `mesh_deviation` (U-07, V-05) | the coarse STL against the B-rep | FAIL — 0.023447 mm (need ≤ 0.01) |
| `mesh_census` (U-07, V-05) | remove: 20 triangles dropped from the delivered STL | FAIL — 22 naked edges (need one closed shell, 0) |
| 3MF parse against the STL (U-07) | degrade: the delivered 3MF compared with the coarse (tol 0.05) mesh | FAIL — 11 676 vs 4 980 triangles (need the same triangle set) |
| hole spacing from `bore_census` axes (REQ-11 … REQ-14) | add: an extra Ø4.0 hole at (92, +77), 3.0 mm from the REQ-14 hole at (95, +77) | FAIL — nearest centre to centre 3.0000 mm (need ≥ 6.0) |
| `nothing_clipped` (D6 sections) | degrade: the plan section redrawn with a −30 mm margin | FAIL — 907 clipped px (need 0) |

Every check family the gate table rests on appears above and every one FAILs on its
mutant, so no gate is left resting on an unproven check. REQ-09 has no check family:
it is a bench row by its own wording.

### Notes on two measurements

- **The OD-H11 boolean.** `common_volume(plate, OD-H11)` returned MEASURED 0.000 mm³ in
  this review rather than INCONCLUSIVE, although OD-H11 reads `brep_valid` 0. Spec §5
  U-03 and the brief both pre-declare that boolean INCONCLUSIVE (OD-C04 A-14), so the
  plate-to-OD-H11 rows are gated on distance only: clearance 16.4925 mm (≥ 10.0, +6.4925)
  and envelope max z −89.210 (≤ −85.0, +4.210). Nothing in this verdict rests on an
  OD-H11 boolean or on its volume.
- **D-05a's rays.** 2 736 rays were cast (38 holes × 72 angles) and one came back
  INCONCLUSIVE, a ray running along a face. The governing figure, 14.000 mm across at
  (−113, −0.5, −42), is confirmed independently by `min_wall` 5.000 at (−115, −5.7, −42),
  which is the same web, so the single unread ray does not reach the gate.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-09 | SOFT_GATE_MISS | not geometric → the printed plate stays flat enough for the mounts to seat without rocking | — | the whole 240 × 405 × 6 mm plate, printed flat (A-14) in PLA (A-10) | no | MEDIUM | An unribbed 6.0 mm plate 405 mm long has no geometric defence against warp, and revision B puts eighteen more holes exactly where a lifted corner shows most: the six bracket holes 15.500 mm from a side edge, the OD-C09 and OD-C11 holes 23.000 mm from the front and rear edges; a lifted corner moves those holes out of plane against panels that are themselves flat. Nothing on the B-rep can answer it. | Answer it on the first print: measure flatness under the three mounts and at the four new hole groups; the ribbed concept C2 is the deferred geometric answer. |
| F2 | U-03 / A-07 tank zone (reported, not gated) | OBSERVATION | 97 020 mm³ of OD-C11 inside the A-07 tank-zone prism → 0 mm³ | −97 020 | OD-C11's wall and floor flanges, z −302.000 … −277.000, over the prism's x ±70, z −305 … −250 | no | MEDIUM | The back panel takes the rear 25 mm of a 55 mm-deep reserved zone, leaving z −277 … −250, so a tank drawn to A-07 would not fit inside the machine. Nothing in this build breaks today: the dock OD-C06 is deferred and the tank stands on the table (the Usta, 2026-10-02), and spec §4 states the reserved zones are not gated. | Redraw A-07's prism to z −277 … −250, or move the tank zone forward, when OD-C06 is designed; no change to this plate. |
| F3 | U-04 (check assembly) | OBSERVATION | `valid_after` 0 on the re-read assembly → 1 | −1 | check-assembly body `od_h11_thermoblock`, brep_valid 0 as an input (OD-C04 A-14) | no | LOW | U-04 gates the target's named body, and the plate's `od_c01_frame` re-reads with volume delta 0.000 mm³, faces delta 0, label kept and valid after 1; the assembly's 0 comes only from the unsound OD-H11 input, whose own volume integral moves 0.0524 mm³ on the first write. Every OD-H11 row in this verdict rests on distances, not on a boolean or a volume. Carried from RV01 F2. | Repair or re-export OD-H11 in its own job (OD-C04 A-14); no change to this plate. |
| F4 | REQ-04 | OBSERVATION | Ø4.000 insert hole → Ø4.0 ± 0.05 insert hole here, Ø ≥ 3.25 clearance hole for an M3 × 12 from below in OD-C02 spec 1.1 | +0.050 | the four bulkhead holes at (65, −45), (65, −105), (65, −165), (65, −225) | no | LOW | The same Ø4.000 through-hole in a 6.000 plate meets D-05b and J-05 read as an insert hole and exceeds D-04a's 3.25 read as an M3 clearance hole, so this plate serves either fastener and no measurement changes; only A-04's wording and OD-C02 spec 1.1 disagree, and the two uses are mutually exclusive once an insert is pressed in. | Settle the fastener in A-04 against OD-C02 spec 1.1 and align the wording; no change to this plate. |
| F5 | J-05 / D-05a | OBSERVATION | 5.000 mm web → ≥ 3.0 mm | +2.000 | (−115.0, −5.7, −42.0), the web from the OD-C07 inserts at x −113 to the edge x −120; also at z −148.5 | no | MEDIUM | The gate is met with +2.000, but after a Ø4.6 heat-set insert about 4.7 mm of material remains to a free edge, now in PLA rather than PETG (A-10), which softens sooner under the iron; it is also the hole group most likely to move, because A-17's OD-C07 pattern is still open and the sweep's ±0.05 hole shift already takes the ring to 4.951. | Press those two inserts at a lower iron temperature, or add a local boss if the first press bulges the edge; alternatively hold the OD-C07 pattern 2 mm further in when A-17 retires. No change needed for the gate. |
| F6 | U-03 / A-06 tray zone (reported, not gated) | OBSERVATION | 0.000 mm³ of OD-C09 inside the A-06 tray-zone prism → 0 mm³ | 0.000 | OD-C09 front panel z +72.000 … +97.000 against the prism x ±75, z −15 … +85, height 36.9 | no | LOW | The REPORT records OD-C09 as standing inside the tray-zone prism on a clearance reading of 0.0; re-measured, the clearance is 0.000 but the shared volume is 0.000 mm³, so the panel only touches the prism's front plane: its floor flanges sit at \|x\| ≥ 80, outside the prism's x ±75, and the tray loses no room. The zone is free. | None needed; correct the REPORT's §5 reading when the tray scan lands and A-06 retires. |

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. The 5.0 web from the OD-C07 outer inserts (x −113) to the left edge, now in PLA | Confirmed: `min_wall` at spacing 0.7 reads 5.000 mm at (−115.0, −5.7, −42.0), and `radial_extent` reads a least material radius of 7.000 at 180°, so the ring wall is 5.000 and D-05a is 14.000 across. J-05 +2.000, D-05a +6.000, U-06 / D-01a / D-01b / D-06a all governed by the same 5.000. The gate is met; the PLA-and-iron concern is real but not geometric and is recorded as F5 (risk MEDIUM). It rests on A-11 and A-17. |
| 2. REQ-09 flatness, now with eighteen more holes | Confirmed INCONCLUSIVE, recorded as F1 with risk MEDIUM. The positions the REPORT worries about are re-measured: the six bracket holes 15.500 mm from the side edges, OD-C09's and OD-C11's 23.000 mm from the front and rear edges, and the ±85 / ±95 pair at z +77 10.000 mm centre to centre, a 6.000 mm web — the tightest hole spacing on the plate. Every one meets its gate; none of them can be answered without a print. |
| 3. The spacing clause for REQ-12 | The reviewer reads spec §5 the same way: REQ-12 names only "≥ 8.0 from the plate edge"; the ≥ 6.0 centre-to-centre clause comes from WP-06's amendment table and from the identical clause in REQ-11, REQ-13 and REQ-14. Measured 14.000 mm centre to centre and 23.000 mm to the outline, so the row passes under either wording and nothing turns on it. No finding. |
| 4. U-04 on the check assembly for OD-H11 | Confirmed and recorded as F3 (OBSERVATION, LOW). The reviewer's own `compare_step` on the assembly reads AP242, 17 solids, volume delta 0.000 mm³, faces delta 0, 17 labels kept and `valid_after` 0 — the 0 traced to OD-H11, brep_valid 0 as an input (OD-C04 A-14). The gated target, the plate's named body `od_c01_frame`, re-reads with volume delta 0.000 mm³, faces delta 0, label kept and valid after 1. INCONCLUSIVE rather than FAIL is the right call. |
