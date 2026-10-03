# RV01 — od_c11_back_v03 (20261001-od-c11-back-panel) — 2026-10-01 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` as amended by `01_CAD/DESIGN_PLAN_v02.md` and `01_CAD/DESIGN_PLAN_v03.md` · report `01_CAD/REPORT_od_c11_back_v03.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-02, A-03, A-04, A-05, A-06, A-07, A-08, A-09

The submission is complete. Every §5 row is answered in the REPORT. All 36 files in the brief are present, and each matches its SHA-256. The four reference inputs (OD-C01, OD-C02, OD-C03, OD-H01) match the hashes in WP-02.

Bands for every comparison (GATES §0, as the plan carries them): mm 0.005, deg 0.001, mm³ 0.001, counts and bool 0. No CAD script was read. My scripts, mutants, re-mesh and sections are in `reviews/RV01_work/`.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c11_back_C1_v03.step` | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db | yes |
| `02_STEP_STL/od_c11_back_C1_v03.stl` | 8fa761335a2bb2aaf5bb75e388c8151f75131bc5b652e19c3f7144625965f96a | yes |
| `02_STEP_STL/od_c11_assembly_C1_v03.step` | 900c822e2b05cf5d3d67d8ca7874900a845713c9be2d70628e9ad26be95bed73 | yes |
| `02_STEP_STL/od_c11_back_C1_v03.3mf` | 7b18dc32d0aaa85669380cda0c2ed9086e7d70ae4395687b677d7f18f964d91d | not in the REPORT (written by the orchestrator); matches the brief |

The delivery must carry exactly these bytes.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 solid; brep_valid 1; naked edges 0 | 1, 1, 0 | 0 | whole part | PASS | `validity` | — |
| U-02 | 232.000 × 215.000 × 25.000 mm. Position: x −116.000 … 116.000, y 0.000 … 215.000, z −302.000 … −277.000 | each in [spec − 0.1, spec + 0.1] | +0.100 | — | PASS | `envelope` | — |
| U-03 | (a) plate contact: clearance 0.000, common 0.000 mm³. Footprint (2067.683 mm²): 0.000 mm² outside the outline, 0.000 mm² over plate holes. **Footprint to outline 0.780** (governing). Wall foot to the feet-hole rims 2.300. Flanges to the rims 4.300 (26 plate bores along Y checked). Plate material missing under each flange-hole plug (Ø3.4 × 6): 0.000 mm³. Nearest existing hole, centre to centre: 19.849. Clearances: OD-C02 37.014, OD-C03 43.863, OD-H01 61.540; common volume 0.000 mm³ with each. (b) lowered from +40 in 1.0 steps (41 poses): worst 0.000 mm³ with all four | ≥ 0.5; wall foot ≥ 2.0; flanges ≥ 3.0; c-c ≥ 6.0; neighbours ≥ 20.0; interference ≤ 0 | +0.280 (outline); +0.300 (wall foot) | (116.0, 0.0, −302.0) wall corner to the R 10 arc; rims at (±110, 0, −295); neighbours at (72, 0, −277) | PASS (assumed: A-01, A-02, A-07) | `clearance`, `common_volume`, `bore_census`; footprint and rim distances by my own code (BRepExtrema on the y 0 underside split at z −299) | A-01, A-02, A-07 |
| U-04 | Part: AP242, mm, label `od_c11_back`, 1 solid, valid. Round trip: volume delta 0.000 mm³, faces delta 0, labels 1, valid after. Assembly: 5 named solids, each valid. Each child is identical to my own placement of the inputs (common volume = volume) | unchanged, no stray shells, valid | 0 | — | PASS | `compare_step`, `step_roundtrip` | — |
| U-05 | bores 9: 4 Ø3.4 along Y through, 2 Ø4.0 along Y blind, 3 Ø12.0 along Z through. Planar 46, cylindrical 19 (concave 19), other 0 | plan §3 counts | 0 | — | PASS | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 (Soft) | 3.000 mm | wide ≥ 2.0 | +1.000 | (76, 34, −302) | PASS | `min_wall_wide` (spacing 0.7) | — |
| U-07 | Max sagitta 0.00499 mm. Delivered STL: 3928 triangles, 1 body, 0 naked edges, winding 1. Volume 165 531.487 mm³ against the B-rep's 165 529.565. Bounding box equals the B-rep's. `mesh_deviation` 0.00499. My re-mesh at 0.01 mm / 0.20 rad gives 3928 triangles on the same 1942 vertices; 12 planar diagonals differ. 3MF: millimetre, 3928 triangles, watertight, the same triangle set as the STL | tol 0.01; angular ≤ 0.23097 rad (R_max 6.0); sagitta ≤ 0.01; 3MF = STL | +0.00501 | — | PASS | `mesh_census`, `mesh_deviation`, `write_stl`, `mesh_sagitta` | — |
| U-08 | — | applies to threaded parts | — | — | N/A: the row applies to threaded parts, and this target has none | — | — |
| D-01a | 3.000 mm | ≥ 0.8 | +2.200 | (116, 0, −299) wall | PASS | `min_wall` (spacing 0.7) | — |
| D-01b | 3.000 mm | ≥ 2.0 | +1.000 | (116, 0, −299) wall | PASS | `min_wall` (spacing 0.7) | — |
| D-02 | 232.000 × 215.000 on the bed, 25.000 tall | ≤ 420 × 420, ≤ 500 | +188.000 | — | PASS (assumed: A-09) | `envelope` | A-09 |
| D-03a | 90.0° outside the exception (the six exception holes plugged by position: 57 faces, valid). No downward face lies off the bed. The exception crowns read 0.0° at (−95.0, 0.0, −280.3) and are reported apart | ≥ 45° | +45.0 | — | PASS (assumed: A-08) | `overhang_census(build_dir=(0,0,1), spacing=0.7)` | A-08 |
| D-03b | Widest horizontal hole Ø4.000 (insert bores); flange holes Ø3.400; flat ceilings 0.000 | ≤ 5.0 (holes ≤ 4.0) | +1.000 | (±90, 209 … 215, −293) | PASS (assumed: A-08) | `bore_census`, `flat_ceiling_spans(max_span=5.0)`, my sections | A-08 |
| D-04a | 3.400 mm (all four) | ≥ 3.25 | +0.150 | (±81 / ±95, 0, −282) | PASS | `bore_census`, `locate_bore` | — |
| D-05a | Across X 12.000 (6.0 + 6.0); across Z 15.000 (9.0 + 6.0), both bosses | ≥ 8.0 | +4.000 | (84 … 96, 210, −293) | PASS (assumed: A-05) | `radial_extent` | A-05 |
| D-05b | Ø 4.000; depth 6.000; blind | Ø 4.0 ± 0.05; depth 6.0 ± 0.1, ≥ 5.7 | +0.050 | (±90, 209 … 215, −293) | PASS (assumed: A-05) | `bore_census`, `locate_bore` | A-05 |
| D-06a | 3.000 mm | ≥ 1.0 | +2.000 | (116, 0, −299) | PASS | `min_wall` | — |
| D-07 | — | fit-critical bores: none on this target | — | — | N/A: the spec row says this target has no fit-critical bore | — | — |
| J-05 | +X 4.000, −X 4.000, +Z 4.000, −Z 7.000 (both bores, y 210; y 213 the same or more) | ≥ 3.0 | +1.000 | (96, 210, −293) | PASS | `radial_extent` | — |
| E-06 | 7 of 7 tied. At x ±93, boss, wall and ledge are one region. At x ±74 and x ±102, gusset, wall and flange are one region. At x 0, ledge and wall are one region | each boss tied into the wall and ledge; each flange tied by two gussets | 0 | sections x ±93, ±74, ±102, 0 | PASS | my sections (cut regions plus point-in-region) | — |
| E-11 | Rays along +Z at all 5 slot centres and all 3 hole axes meet no material. A Ø12 cylinder from z −299 to −277 behind each hole: 0.000 mm³. Vents at x 76 … 112, y 100 … 180 | grommet hole for the cord; vents open the bay's rear | 0 | — | PASS (assumed: A-03, A-06) | `radial_extent`, `common_volume`, my sections | A-03, A-06 |
| REQ-01 | Ø 3.400, offset 0.000, length 4.000, through (all four). Underside is one planar face at y 0.000 | Ø 3.4 ± 0.1; offset ≤ 0.10; 4.0 ± 0.1; 1 plane at 0.00 ± 0.10 | +0.100 | (±81 / ±95, 0 … 4, −282) | PASS (assumed: A-01) | `locate_bore`, `envelope`, face list | A-01 |
| REQ-02 | Outer face −302.000 and inner face −299.000 at x −40, 0, 40 and y 50, 200. x −116.000 / 116.000 | ± 0.10; ± 0.1 | +0.100 | rays from (x, y, −300.5) | PASS (assumed: A-02) | `radial_extent`, `envelope` | A-02 |
| REQ-03 | Ø 12.000, offset 0.000, through | 12.0 ± 0.1; ≤ 0.10 | +0.100 | (95, 30) | PASS (assumed: A-03) | `locate_bore` | A-03 |
| REQ-04 | Ø 12.000, offset 0.000, through (both) | 12.0 ± 0.1; ≤ 0.10 | +0.100 | (−100, 30), (−84, 30) | PASS (assumed: A-04) | `locate_bore` | A-04 |
| REQ-05 | max z −277.000; keep-out box common 0.000 mm³ | ≤ −277.0; = 0 | 0.000 | flange fronts z −277 | PASS (assumed: A-07) | `envelope`, `common_volume` | A-07 |
| REQ-06 | Each slot: 4.000 wide (2.000 + 2.000), 80.000 tall (y 100.000 … 180.000), centre 0.000 off, through | ± 0.1 each | +0.100 | rays at (x_c, 140, −300.5) | PASS (assumed: A-06) | `feature_census`, `radial_extent` | A-06 |
| REQ-07 | Ø 4.000, depth 6.000, offset 0.000, blind. The top is one planar face at y 215.000 over z −302 … −287 | Ø 4.0 ± 0.05; 6.0 ± 0.1; ≤ 0.10 | +0.050 | (±90, 215, −293) | PASS (assumed: A-05) | `locate_bore`, `bore_census`, face list | A-05 |
| REQ-08 | 0.000 mm³ for all four Ø6 cylinders from y 4 to 260. Above y 4.5 the nearest material is the flange top (0.5) | = 0 | 0 | (±81 / ±95, −282) | PASS | `common_volume`, `clearance` | — |
| REQ-09 (Soft) | not measured: a bench row | no visible drumming or flex | — | — | INCONCLUSIVE (Soft, bench) | — | A-11 |
| exactly_one_solid | 1 | 1 | 0 | — | PASS | `validity` | — |
| feature_census | planar 46, cylindrical 19, bores 9 | plan §3 | 0 | — | PASS | `feature_census` | — |
| envelope_within_spec | 232.000 × 215.000 × 25.000; every position bound 0.000 off | ± 0.1 | +0.100 | — | PASS | `envelope` | — |

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 wall | 1 slab, x ±116, z −302 … −299 | Outer face z −302 (47 957.876 mm²) and inner face z −299 (46 213.876 mm²), each one plane; ends at x ±116 | PASS |
| F02 floor flanges | 2, x ±(72 … 104), y 0 … 4, to z −277 | 2 fronts z −277 (128 mm² each); 2 tops y 4 (557.842 mm²) | PASS |
| F03 gussets | 4 (inner wall leg 30, outer 18, flange leg 16) | Inner: y 4 … 34, normal (0, 0.4706, 0.8824). Outer: y 4 … 22, normal (0, 0.6644, 0.7474) | PASS |
| F04 top ledge | 1, x ±114, y 211 … 215, to z −287 | Front z −287; underside in 3 pieces (216 / 2016 / 216 mm²) | PASS |
| F05 insert bosses | 2, x ±(84 … 96), y 203 … 211 | 2 undersides at y 203 (144 mm²) | PASS |
| F06 flange holes | 4 × Ø3.4 along Y, through | 4 × Ø3.400, length 4.000, offset 0.000 | PASS |
| F07 insert bores | 2 × Ø4.0 × 6.0, blind | 2 × Ø4.000, depth 6.000; floors at y 209 | PASS |
| F08 pass-throughs | 3 × Ø12.0 along Z, through | 3 × Ø12.000, offset 0.000 | PASS |
| F09 vent slots | 5, 4 × 80, ends R 2.0 | 10 concave R 2.0 half-cylinders and 10 sides; each 4.000 × 80.000, through | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity | The panel stands on the plate's top face at y 0 (clearance 0.000, common 0.000 mm³). It prints on its outer face, and everything else rises along +Z | YES |
| P2 | Function chains | Cord and tube holes are through, with nothing behind them to z −277; vents are open behind the bay; insert bores open upward; driver axes are clear | YES |
| P3 | Moving parts | There are none. The lowering path, 41 poses from +40, is clear of every neighbour | YES |
| P4 | Grip, reach, insertion | A straight Ø6 driver reaches all four screws from above, 2.0 clear of the ledge front and the boss faces. The panel drops straight down onto the plate | YES |
| P5 | Next to a real product | It reads as an ordinary appliance back panel: wall, top ledge with inserts, gusseted floor tabs, grommet holes, vent grille | YES |
| P6 | Floating, embedded, mirrored, upside-down | One solid, embedded in nothing. Cord is at +X (right) and tubes at −X (left), as in §4. Features are on the +Z side; the ledge is on top | YES |

## 5. Positive controls

Every mutant was built by me from the exported STEP or STL (`reviews/RV01_work/mutants/`).

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` | loose 5 mm cube beside the panel: solid_count 2 | FAIL |
| `envelope` | +X wall end extended 0.5 mm: size_x 232.5 | FAIL |
| `feature_census` | vent slot at x 110 filled: cylindrical faces 17 | FAIL |
| `bore_census` | flange hole (−81, −282) filled: bores 8 | FAIL |
| `locate_bore` | flange hole (81, −282) moved 0.5 mm along +X: offset 0.500 | FAIL |
| `radial_extent` | boss at x 90 cut back 1.5 mm on +X: bore wall 2.500 | FAIL |
| `min_wall` | 20 × 20 pocket, 1.5 deep, in the outer face at (0, 60): 1.500 | FAIL |
| `min_wall_wide` | same pocket: 1.500 | FAIL |
| `overhang_census` | pocket mutant with the exception holes plugged: 0.0° | FAIL |
| `flat_ceiling_spans` | pocket mutant: span 19.700 | FAIL |
| `common_volume` (keep-out box) | 5 mm cube in the tank zone at (0, 50): 120.000 mm³ | FAIL |
| `common_volume` (lowering path) | tab reaching z −235 into OD-C02: 100.000 mm³ | FAIL |
| `common_volume` (driver cylinders) | 6 × 2 × 10 rib over the axis (95, −282): 56.549 mm³ | FAIL |
| `clearance` | panel moved 18 mm toward +Z: 19.026 to OD-C02 | FAIL |
| footprint rim distance (my code) | flange end extended to x 107: 1.300 to the feet-hole rim | FAIL |
| `compare_step` | the +0.5 mm envelope mutant against the delivered file: 322.500 mm³ | FAIL |
| `mesh_census` | delivered STL with 2 triangles removed: 4 naked edges | FAIL |
| `mesh_sagitta` / `mesh_deviation` | re-mesh at 0.1 mm / 0.5 rad: 0.04375 | FAIL |
| section regions (E-06) | boss at x 90 cut free of the wall and ledge by 0.5 gaps: not tied | FAIL |
| through ray (E-11, REQ-06) | vent at x 110 filled: material on the ray | FAIL |

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-09 | SOFT_GATE_MISS | not measurable from CAD → no visible drumming or flex (bench) | — | whole wall; free edges at x ±116 over y 0 … 215 | no | MEDIUM | A 3.0 mm PETG wall, 232 × 215, is held at four floor screws and two top inserts. Both side edges stay free until OD-C12/C13 exist, so it may drum with the pump's vibration. Only the first print can tell (A-11) | Bench-test the first print with the top panel on. If it drums, add a vertical rib or tie the free edges once the side panels are designed |

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| Tube holes' 2.0 gap to the gussets (1.950 at Ø12.1) | Measured: 2.000 from the −100 hole to the −X outer gusset top at (−100, 22, −299); 2.000 from the −84 hole to the inner gusset face at x −76; 3.434 for the cord hole. With Ø12.1 holes each gap is 1.950. No §5 row sets this gap. A grommet rear flange wider than about Ø16 would sit on a gusset; that question stays with A-04 |
| Wall foot margin: +0.300 nominal, +0.200 at wall_z +0.1 | Measured 2.300 against the 2.0 limit. My own variant with the inner face at z −298.9 reads 2.200. This holds only while OD-C01's feet holes stay Ø3.4 at (±110, −295); re-measure after the OD-C01 revision for A-01 |
| Region split is job code | My own split at z −299 gives the same numbers: wall foot 696.0 mm² at 2.300, flanges 1371.683 mm² at 4.300. The rim code FAILs on a mutant (1.300), so the reading can fail |
