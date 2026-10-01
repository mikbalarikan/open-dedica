# REPORT — od_c03_cradle v01 (20260930-od-c03-pump-cradle)

Designer: Claude Code, claude-opus-5-5 · spec version 1.1 · plan `01_CAD/DESIGN_PLAN.md` (WP-02) with the WP-03 amendments · build package WP-03, attempt 1 of 2 · 2026-09-30 UTC

Every number below is measured by `01_CAD/check_od_c03_cradle.py` on the re-imported STEP files (the full 137 gate rows, with nearest points and reasons, are in `01_CAD/check_od_c03_cradle_v01.json`). Self-checks do not clear a hard gate; the reviewer's measurement does.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c03_cradle.py` | 9a0570dd5dc3f18382a7e00f30f89381fb37dfff1d0847244be0a1ab2c0d4dce | parametric script (Algebra mode), places OD-H01 and the sleeve, exports, runs the checks; `sweep` mode for D7 |
| `01_CAD/check_od_c03_cradle.py` | 6faede056f61d0ec7ac45c151d6c011f2a2dd873c59e25e69c9653e76d8069d5 | checks, written before the build (D3); one selector corrected in fix cycle 1 (§8) |
| `01_CAD/check_od_c03_cradle_v01.json` | c46068d7c469414f7200ce8d8ec57a51b2fe9225c8b3a77e604541410d67e66d | all gate rows of the deliverable, the assembly facts, mass properties, export hashes |
| `01_CAD/sections_od_c03_cradle.py` | a3b867d94e19d624749c7aa1e7bf6c970bfcd9e54ec65b4272de13f0e1014467 | D6 section script (`tools.drawing.write_sections`) |
| `01_CAD/sections_od_c03_cradle_v01.json` | 7856b0a860c0b51701464b361ed6701bfc03ab554caa575d6af5c498bb13ea77 | per-section plane, cut area, `nothing_clipped` |
| `01_CAD/sweep_v01/SHA256SUMS.txt` | 27ab219850802b246f28d28e3a2bfc097ae5bf0be15577ada21c8e780721ee54 | SHA-256 of the 64 sweep files (16 variants × part STEP, assembly STEP, STL, result JSON) |
| `02_STEP_STL/od_c03_cradle_C1_v01.step` | c4b028e130a3ee29324c5cd31543e44ec7ee6bb5e2489f8dc55c6b018a4aefbd | AP242 (`tools.core.write_step`), one solid labelled `od_c03_cradle`, re-imported for every measurement |
| `02_STEP_STL/od_c03_assembly_C1_v01.step` | 6ce49e9220d6737d0cd9e95d385b1f7de80ced7e64e7616e562e47bb5280cebf | AP242 check assembly: `od_c03_cradle` (re-imported part file), `OD_H01_ulka_ep5_pump` (identity joint), `od_h02_sleeve_assumed_A03` |
| `02_STEP_STL/od_c03_cradle_C1_v01.stl` | b95aab55d1efb1706f41bb7c4c2a9e8c6e50a2ccf0a8e9fa3a5bd38af6dcae8c | from the re-imported STEP, cached triangulation cleared; tolerance 0.01 mm / angular 0.1 rad, 2540 triangles, measured sagitta 0.00489 mm |
| `03_Sections/od_c03_cradle_v01_xy_z18p0.png` | 6026c0bc98de01d1247d3738a1097fd6d831ca283b5cd6fa2587a615babd3f22 | XY at z 18.0: rib 1, web, both posts, foot; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v01_xy_z28p0.png` | dcb202aa0c0badf040899673aa6f03fbb7d39d4c8be76dacb6ccaa4e5c5a8119 | XY at z 28.0: rib 2; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v01_yz_x0p0.png` | 25df58f08d72acfef2676a63b60cd810b20396cfb9118b1e18a5352e4cd24072 | YZ at x 0: rib faces z 15/21/25/31, foot 3.0; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v01_yz_x31p5.png` | f464a2577d1dc4ff079f4acd9a0f0cbe0fdf4aea79170d3b544c4207aba31986 | YZ at x 31.5: +X post block, both gabled slots, ligaments; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v01_yz_x34p0.png` | f51f03846c0f003bef9cf8caff76b7567f719b8b315de9378650950208eae4b1 | YZ at x 34.0: the two +X frame holes through the foot; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v01_xz_y7p0.png` | 6ef1f55c114f986b4c186561af43e4f5e40eb8868f7c12733fe82830688dba65 | XZ at y 7.0: slot centre plane through both posts; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v01_xz_y38p5.png` | 144b0776717f332a26987361ac900c06299c71a04f252aa55b5bb9d56395a115 | XZ at y 38.5: foot with the four holes; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v01_assembly_xy_z18p0.png` | f42595ad12ffb6770772bbec40dd72a2d5ed9219a0afdcee64b55c1753dfce90 | check assembly, XY at z 18.0: cradle, sleeve, coil, side plates; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v01_assembly_yz_x0p0.png` | bd8a2a1c5c74aa52dee5cefd3191443ea60fcf37d0d1328c315acc1267adf1f2 | check assembly, YZ at x 0; nothing clipped (0) |

Inputs checked against the brief before any work: OD-H01 STEP b05302af…3fb62, params.json 21e02bf5…c43c, README.md 52b06473…7fa2, all three match.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1.1 (cadquery-ocp-novtk, OCCT 7.9.3) · repo commit 70826895ab7666f9e5aee3f77ce88f099995f3c1

## 3. Gate self-check

Margin is signed, positive inside the limit; the worst row of each gate is shown, all rows are in the JSON file.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | — | PASS | — |
| U-02 | 80.000 × 40.000 × 52.000 mm | each in [spec − 0.1, spec + 0.1] | +0.100 | size; position below | PASS | — |
| U-02 position (reported apart) | x −40.000 … 40.000, y 0.000 … 40.000, z −10.000 … 42.000 | x ±40.0, y 0.0 … 40.0, z −10.0 … 42.0 | 0.000 each | — | PASS | — |
| U-03 (a) cradle\|OD-H01 | clearance 2.300 mm; interference 0.0 mm³ (OD-H01 sound: 1/1/0 on re-import) | ≥ 2.0; ≤ 0 | +0.300; 0 | (−29.500, 0.000, 33.000) on the −X post to (−27.200, 0.000, 33.000) on the −X side plate | PASS (assumed: A-01, A-03) | A-01, A-03 |
| U-03 (a) cradle\|sleeve | clearance 6.9e-13 mm; interference 0.0 mm³ | = 0; ≤ 0 | −6.9e-13 (inside the 0.005 band) | (−18.844, 18.844, 15.000), r 26.650, θ 135.0° (saddle arc edge of rib 1) | PASS (assumed: A-03) | A-03 |
| U-03 (b) | no motion variable | — | — | — | NOT_APPLICABLE (by its row: ties not modelled) | — |
| U-04 | schema AP242 1, solids 1, volume_delta 1.8e-10 mm³, faces_delta 0, labels 1, valid_after 1 | 1, 1, ≤ 0.001, 0, 1, 1 | 0 | — | PASS | — |
| U-05 | feature_census: plane 48, cylinder 6, cone/sphere/torus/bspline/other 0, concave cylinders 6, convex 0, bores 4; by position: 2 saddle arcs, 2 post blocks, 4 slots, 4 holes located, 1 foot underside | the same (spec 1.1 §6 re-tally) | 0 | — | PASS | — |
| U-06 (soft) | min_wall at 45°: 2.000 mm | ≥ 2.0 | −3e-15 (inside the band) | (−33.318, 6.101, 33.000), slot ligament to the post end face | PASS | — |
| U-07 | sagitta 0.00489 mm (fresh mesh of the re-imported STEP); angular 0.1000 rad; delivered STL 2540 triangles = re-mesh, 1 body, 0 naked edges | ≤ 0.01; ≤ 0.1000026 rad | +0.0051; +2.6e-6 | (−18.477, 19.198, 19.500) | PASS | — |
| U-08 | no threads | — | — | — | NOT_APPLICABLE (by its row) | — |
| D-01a | min_wall 2.000 mm | ≥ 0.8 | +1.200 | (−33.318, 6.101, 33.000) | PASS | — |
| D-01b | min_wall 2.000 mm | ≥ 2.0 | −3e-15 (inside the band) | (−33.318, 6.101, 33.000) | PASS | — |
| D-02 | 80.0 (X) × 52.0 (Z) on the bed, 40.0 (Y) tall | ≤ 420 × 420 × 500 | +340.0 / +368.0 / +460.0 | — | PASS (assumed: A-10) | A-10 |
| D-03a | least downward angle 45.000° (the four gable roofs; nothing else faces the bed) | ≥ 45 | 0.000 | (−29.500, 5.750, 21.000) | PASS (assumed: A-13) | A-13 |
| D-03b | largest flat downward face 0.0 mm (no flat ceiling; gable apex is an edge) | ≤ 5 | +5.0 | designer reading; reviewer from sections | PASS | — |
| D-04a | four holes Ø3.400 mm | ≥ 3.25 | +0.150 | (±34.0, 37.0, −4.0), (±34.0, 37.0, 37.0) | PASS | — |
| D-04c | clearance to OD-H01 2.300 mm | ≥ 0.5 | +1.800 | as U-03 (a) | PASS (assumed: A-01) | A-01 |
| D-06a | min_wall 2.000 mm | ≥ 1.0 | +1.000 | as D-01b | PASS | — |
| D-07 | clearance holes only | — | — | — | NOT_APPLICABLE (by its row) | — |
| REQ-01 | inner radius min 26.650, max 26.650 mm in both windows (θ 50 … 130 step 5; z 15.5 … 20.5 and 25.5 … 30.5, 0.1 steps, margin 0) | in [26.60, 26.70] | +0.050 | (17.130, 20.415, 15.550) | PASS (assumed: A-03) | A-03 |
| REQ-02 | inner r at θ 50° and 130°, z 18 and 28: 26.650 mm; window r ≤ 32.0 at θ 40° and 140°: INCONCLUSIVE "no material" (the expected reading, recorded); first material on the whole ray there 38.510 mm (the post at x ±29.5); rib faces z 15.000, 21.000, 25.000, 31.000 | ≤ 26.70; no material within r ≤ 32.0; faces ± 0.10 | +0.050; +6.510; +0.100 | (17.130, 20.415, 18.000); (29.500, 24.753, 18.000) | PASS (assumed: A-06) | A-06 |
| REQ-03 | clearance(cradle, OD-H01) 2.300 mm; by region: −X post 2.300, +X post 2.650, ribs 2.788 (to the coil at (−16.878, 16.868, 15.0)) | ≥ 2.0 | +0.300 | (−29.500, 0.000, 33.000) to (−27.200, 0.000, 33.000) | PASS (assumed: A-01, A-03) | A-01, A-03 |
| REQ-04 | clearance(cradle, sleeve) 6.9e-13 mm, nearest point r 26.650 mm θ 135.0° on the saddle arc; interference 0.0 mm³ | = 0 on a saddle arc; ≤ 0 | −6.9e-13 (inside the band) | (−18.844, 18.844, 15.000) | PASS (assumed: A-03) | A-03 |
| REQ-05 | four slots: clear 6.000 (Z) × 2.500 (Y), centres y 7.000, z 18.000 / 28.000, through 4.000 along X, roofs 45.000° from horizontal, ligament 2.000 mm (worst; 4.000 between slots, 2.750 above the apex) | ≥ 6.0 × 2.5; y 7.0 ± 0.5; z ± 0.5; roofs ≥ 45°; ligament ≥ 2.0 | 0.000 (clear, roof, ligament) | slots at x ±(29.5 … 33.5) | PASS (assumed: A-07) | A-07 (A-13 for the roofs) |
| REQ-06 | inner faces \|x\| 29.500 (both), z 13.000 … 33.000 (both); post clearance 2.300 (−X), 2.650 (+X) | 29.5 ± 0.1, 13.0 / 33.0 ± 0.1; ≥ 2.0 | +0.100; +0.300 | (±29.5, 19.356, 23.0) | PASS (assumed: A-06) | A-06 |
| REQ-07 | four bores Ø3.400 mm, axis ±Y, offset 0.000 mm, through 1, at (±34.0, z −4.0) and (±34.0, z 37.0) | Ø3.4 ± 0.1; offset ≤ 0.10; through | +0.100 | as D-04a | PASS (assumed: A-11) | A-11 |
| REQ-08 | underside max_y 40.000 mm; thickness 3.000 mm (foot top face y 37.000) | 40.00 ± 0.10; 3.0 ± 0.1 | +0.100 | — | PASS (assumed: A-11) | A-11 |
| REQ-09 | bench gate, not geometric | — | — | — | INCONCLUSIVE (until the first run) | A-03, A-05 |
| exactly_one_solid | 1 | 1 | 0 | — | PASS | — |
| feature_census | as U-05 | plan §6 re-tallied: 48 planar faces (foot 6, ribs 2 × 6, post blocks 2 × (5 + 2 × 5)), 6 concave cylinders, 4 bores | 0 | — | PASS | — |
| envelope_within_spec | size 80.000 × 40.000 × 52.000; position x −40.000 … 40.000, y 0.000 … 40.000, z −10.000 … 42.000 | as U-02 | +0.100 size; 0.000 position | — | PASS | — |

## 4. Robustness sweep (D7)

Each variant rebuilt, exported to `01_CAD/sweep_v01/`, re-imported, and run through the same predicates, including the check assembly with OD-H01 and the sleeve. Every variant built exactly one valid solid. No motion variable exists (U-03 b).

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| foot_t (underside held at 40.0) | 2.9 · 3.0 · 3.1 | yes | D-01b / REQ-05 ligament (unchanged) | 0.000 |
| r_in (saddle) | 26.60 · 26.65 · 26.70 | yes | REQ-04 / U-03 (a) cradle\|sleeve: FAIL at both ends (low: interference 25.09 mm³; high: gap 0.050 mm); REQ-01 passes at both | −25.09 mm³ (low), −0.050 mm (high) |
| th0 / th1 (sector) | 47/133 · 45/135 · 43/137 | yes | REQ-04 nearest-point θ row: 137.0° at 43/137, outside the spec's 45 … 135 sector (the row reads the sector parameter itself); REQ-02 θ 40°/140° still no material within r ≤ 32; REQ-03 2.300 | −2.0° (high) |
| post_x_in | 29.4 · 29.5 · 29.6 | yes | REQ-03 2.200 / 2.300 / 2.400 | +0.200 |
| slot_h | 2.5 · 2.5 · 2.7 | yes | D-01b / REQ-05 ligament (unchanged) | 0.000 |
| slot_w | 6.0 · 6.0 · 6.2 | yes | D-01b, U-06, REQ-05 ligament 1.900: FAIL at 6.2 | −0.100 (high) |
| slot_yc | 6.5 · 7.0 · 7.5 | yes | D-01b / REQ-05 ligament (unchanged) | 0.000 |
| hole_d | 3.3 · 3.4 · 3.5 | yes | D-01b / REQ-05 ligament (unchanged) | 0.000 |

The part passes every gate at nominal; two rows pass only at nominal: REQ-04 (a designed zero-gap contact, so any saddle radius other than 26.65 fails it by construction) and the slot ligament (D-01b, U-06, REQ-05: the spec's 20.0 post block with two 6.0 slots at z 18 and 28 leaves exactly 2.0 at each end, so any widening of a slot fails it). Both are spec values at zero margin, not build choices.

## 5. Build facts

- Envelope 80.000 × 40.000 × 52.000 mm; volume 25 162.5 mm³; mass 31.96 g at 1270 kg/m³ (A-09); centre of mass (0.000, 31.863, 19.556).
- Fillets: none requested (plan §4 `fillet_r`), none built; every gated face is analytic.
- Placements: OD-H01 placed by a RigidJoint on the cradle at the origin, axis +Z, identity (`pump_axis` to the pump's `datum`), checked on re-import (side plates at x −27.20 / 26.85 read in place, REQ-03 nearest point). The sleeve `od_h02_sleeve_assumed_A03` placed by the same joint; it is two solids (the tube ID 47.3 cut at |x| ≤ 23.5 < 23.65 separates into a +Y and a −Y arc), 13 993.1 mm³.
- Construction: the rib webs and the post blocks overlap the foot by 1.0 so each union is a volume overlap, not a face contact; the finished faces are unchanged (the foot top face reads y 37.000).
- Information, not a §5 pair: the assumed sleeve shares 1427.2 mm³ with OD-H01 (the coil is 0.2 off-axis and slightly conical while the sleeve ID equals the fitted coil OD on the axis).

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The foot is under the pump in the machine (+Y down); the sleeve-clad coil rests in the two saddles centred on +Y, so the pump's weight goes saddle → rib web → foot → four M3 screws into OD-C01. |
| P2 | Function chains | Each tie runs from a post slot (y 7.0) up past the outer faces of the frame side plates and over the −Y side of the sleeve; at z 15.5 … 30.5 the pump's −Y side between θ 225° and 315° is the coil only (outer radius 23.44 … 23.72, probed), so the tie rides on the sleeve, not on the terminal block or spade tabs (which end at z 13.6). |
| P3 | Motion clearance | No moving part; the vibrating pump keeps 2.300 (−X post), 2.650 (+X post), 2.788 (ribs to coil) and 13.25 (foot) from the cradle at the identity pose. |
| P4 | Human factors | The four holes lie outside the pump's \|x\| ≤ 27.2 and beyond the post blocks in z, so a driver reaches every screw head from above (−Y); the 6.0 × 2.5 slots pass a 4.8 × 1.4 tie. |
| P5 | Absurdity next to a real product | An 80 × 52 × 40 mm, 32 g PETG cradle for a 0.5 kg vibratory pump on a rubber sleeve is in proportion with OEM pump brackets. |
| P6 | Nothing floating, embedded, mirrored or upside-down | One solid; nothing floats. The assumed sleeve is embedded in the coil by 1427.2 mm³ (an A-03 shape limit, §5). Section pictures draw +Y up (foot at the top of the XY sections); the model itself is in the spec frame, not mirrored or inverted. |

## 7. Library and tools used

- Cards: none (plan §2: no card matches a saddle cradle with strap retention).
- `tools.core`: `read_step`, `write_step` (AP242), `compare_step`, `validity`, `write_stl` (with its `mesh_sagitta`).
- `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `min_wall` (with its 45° reading for U-06), `overhang_census(build_dir=(0,−1,0))`, `radial_profile`, `radial_extent`, `clearance`, `interference`, `mesh_census`, `mass_properties`; `tools.measure.features.cylinder` to select the saddle faces.
- `tools.drawing.write_sections` and its `nothing_clipped`; `tools.result.gate`.
- New code: job-local only (the three scripts in `01_CAD/`); nothing in the repo. No missing `tools/measure` function.

## 8. Deviations from the plan

1. Spec 1.1 amendments (brief, checked by the orchestrator), built as given: foot z −10.0 … 42.0 (envelope 80.0 × 40.0 × 52.0); holes at (±34.0, −4.0) and (±34.0, 37.0); ribs over z 15.0 … 21.0 and 25.0 … 31.0 (REQ-01 windows and REQ-02 levels moved with them); one post block per side, z 13.0 … 33.0, 4.0 thick, inner face |x| 29.5, top y 0.0, with two gabled 6.0 × 2.5 slots at z 18.0 / 28.0 (answers C-01); the sleeve cut back to |x| ≤ 23.5; the census re-tallied to 48 planar faces (the plan's 58 assumed four posts).
2. Sections: planes moved with the ribs (z 18.0 and 28.0 instead of 3.0 and 27.0); added YZ at x 0, XZ at y 7.0 and y 38.5, and two check-assembly sections.
3. Checks added beyond the plan: REQ-02 positive control (first material on the whole ray at θ 40°/140°, so "no material within r ≤ 32" is also a measured number); REQ-04 nearest-point radius and angle rows; U-07 gated by re-meshing the re-imported STEP at the delivery settings in a temporary folder and matching the delivered STL's triangle count.
4. Fix cycle 1 (check script only, no geometry change): in the sweep, the slot_yc 6.5 / 7.5 variants read "U-05 strap slots 0" because the slot-floor selector accepted floors strictly within 0.5 of y 8.25, while REQ-05 allows the centre ± 0.5. The selector now accepts ≤ 0.5 + 0.01 and a floor narrower than 5.0 along X. The deliverable was re-checked from the files already exported (no re-export; hashes unchanged; same 137 rows, same results) and the slot_yc sweep was rerun (both variants pass).
5. Construction overlap of 1.0 into the foot for the rib webs and posts (stated derivation in the build parameters; no face moves).

## 9. What I am least sure of

1. REQ-03 margin of 0.300 at the −X post (to the −X side plate at x −27.20) is below the scan's p95 deviation 0.448 (A-01); the post_x_in sweep gives 2.200 at 29.4. A real frame plate 0.3 further out would make this a contact; calipers on the frame (A-04) retire it.
2. The saddle contact (REQ-04) and the sleeve shape rest wholly on A-03: the assumed sleeve overlaps the coil by 1427.2 mm³ and is two separate arcs, so the zero-gap contact is exact only against a model; ±0.05 on the saddle radius turns it into a 0.05 gap or a 25 mm³ overlap.
3. Four rows sit at exactly zero margin by the spec's own dimensions: slot ligament 2.000 (D-01b, U-06, REQ-05), slot clear section 6.000 × 2.500, and the 45.000° gable roofs (D-03a). As printed, FDM slot shrinkage or growth will move them either way. Also the ties pass round the outside of the metal side plates between the slot and the −Y side, so a tie may bear on the frame as well as the sleeve (REQ-09).

## 10. Stop

Not stopped.

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20260930-od-c03-pump-cradle",
  "part": "od_c03_cradle",
  "tag": "v01",
  "spec_version": "1.1",
  "files": [
    {"path": "01_CAD/build_od_c03_cradle.py", "sha256": "9a0570dd5dc3f18382a7e00f30f89381fb37dfff1d0847244be0a1ab2c0d4dce"},
    {"path": "01_CAD/check_od_c03_cradle.py", "sha256": "6faede056f61d0ec7ac45c151d6c011f2a2dd873c59e25e69c9653e76d8069d5"},
    {"path": "01_CAD/check_od_c03_cradle_v01.json", "sha256": "c46068d7c469414f7200ce8d8ec57a51b2fe9225c8b3a77e604541410d67e66d"},
    {"path": "01_CAD/sections_od_c03_cradle.py", "sha256": "a3b867d94e19d624749c7aa1e7bf6c970bfcd9e54ec65b4272de13f0e1014467"},
    {"path": "01_CAD/sections_od_c03_cradle_v01.json", "sha256": "7856b0a860c0b51701464b361ed6701bfc03ab554caa575d6af5c498bb13ea77"},
    {"path": "01_CAD/sweep_v01/SHA256SUMS.txt", "sha256": "27ab219850802b246f28d28e3a2bfc097ae5bf0be15577ada21c8e780721ee54"},
    {"path": "02_STEP_STL/od_c03_cradle_C1_v01.step", "sha256": "c4b028e130a3ee29324c5cd31543e44ec7ee6bb5e2489f8dc55c6b018a4aefbd"},
    {"path": "02_STEP_STL/od_c03_assembly_C1_v01.step", "sha256": "6ce49e9220d6737d0cd9e95d385b1f7de80ced7e64e7616e562e47bb5280cebf"},
    {"path": "02_STEP_STL/od_c03_cradle_C1_v01.stl", "sha256": "b95aab55d1efb1706f41bb7c4c2a9e8c6e50a2ccf0a8e9fa3a5bd38af6dcae8c"},
    {"path": "03_Sections/od_c03_cradle_v01_xy_z18p0.png", "sha256": "6026c0bc98de01d1247d3738a1097fd6d831ca283b5cd6fa2587a615babd3f22"},
    {"path": "03_Sections/od_c03_cradle_v01_xy_z28p0.png", "sha256": "dcb202aa0c0badf040899673aa6f03fbb7d39d4c8be76dacb6ccaa4e5c5a8119"},
    {"path": "03_Sections/od_c03_cradle_v01_yz_x0p0.png", "sha256": "25df58f08d72acfef2676a63b60cd810b20396cfb9118b1e18a5352e4cd24072"},
    {"path": "03_Sections/od_c03_cradle_v01_yz_x31p5.png", "sha256": "f464a2577d1dc4ff079f4acd9a0f0cbe0fdf4aea79170d3b544c4207aba31986"},
    {"path": "03_Sections/od_c03_cradle_v01_yz_x34p0.png", "sha256": "f51f03846c0f003bef9cf8caff76b7567f719b8b315de9378650950208eae4b1"},
    {"path": "03_Sections/od_c03_cradle_v01_xz_y7p0.png", "sha256": "6ef1f55c114f986b4c186561af43e4f5e40eb8868f7c12733fe82830688dba65"},
    {"path": "03_Sections/od_c03_cradle_v01_xz_y38p5.png", "sha256": "144b0776717f332a26987361ac900c06299c71a04f252aa55b5bb9d56395a115"},
    {"path": "03_Sections/od_c03_cradle_v01_assembly_xy_z18p0.png", "sha256": "f42595ad12ffb6770772bbec40dd72a2d5ed9219a0afdcee64b55c1753dfce90"},
    {"path": "03_Sections/od_c03_cradle_v01_assembly_yz_x0p0.png", "sha256": "bd8a2a1c5c74aa52dee5cefd3191443ea60fcf37d0d1328c315acc1267adf1f2"}
  ],
  "versions": {"python": "3.13.7", "build123d": "0.11.1", "ocp": "7.9.3.1.1 (OCCT 7.9.3)", "repo_commit": "70826895ab7666f9e5aee3f77ce88f099995f3c1"},
  "gates": [
    {"gate": "U-01", "measured": 1, "unit": "count", "required": "solid_count 1, brep_valid 1, naked_edges 0", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-02", "measured": 80.0, "unit": "mm", "required": "80.0 x 40.0 x 52.0 each +-0.1 (worst: size_x)", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-03 (a)", "measured": 2.3, "unit": "mm", "required": "cradle|OD-H01 >= 2.0 and interference <= 0; cradle|sleeve = 0 and interference <= 0", "margin": 0.3, "at": "(-29.5000, 0.0000, 33.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-03"]},
    {"gate": "U-03 (b)", "measured": null, "unit": "", "required": "no motion variable", "margin": null, "at": null, "status": "NOT_APPLICABLE", "assumes": []},
    {"gate": "U-04", "measured": 1.8e-10, "unit": "mm3", "required": "volume_delta <= 0.001; schema, solids, faces, labels, valid_after", "margin": -1.8e-10, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-05", "measured": 48, "unit": "count", "required": "plane 48, cylinder 6, concave cylinders 6, bores 4; 2 ribs, 2 post blocks, 4 slots, 4 holes, 1 foot", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-06", "measured": 2.0, "unit": "mm", "required": ">= 2.0 (soft)", "margin": -3e-15, "at": "(-33.3182, 6.1011, 33.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "U-07", "measured": 0.00489, "unit": "mm", "required": "sagitta <= 0.01; angular <= 0.1000026 rad", "margin": 0.00511, "at": "(-18.4766, 19.1984, 19.5000) mm", "status": "PASS", "assumes": []},
    {"gate": "U-08", "measured": null, "unit": "", "required": "threaded parts only", "margin": null, "at": null, "status": "NOT_APPLICABLE", "assumes": []},
    {"gate": "D-01a", "measured": 2.0, "unit": "mm", "required": ">= 0.8", "margin": 1.2, "at": "(-33.3182, 6.1011, 33.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "D-01b", "measured": 2.0, "unit": "mm", "required": ">= 2.0", "margin": -3e-15, "at": "(-33.3182, 6.1011, 33.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "D-02", "measured": 80.0, "unit": "mm", "required": "<= 420 x 420 x 500", "margin": 340.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-10"]},
    {"gate": "D-03a", "measured": 45.0, "unit": "deg", "required": ">= 45", "margin": 0.0, "at": "(-29.5000, 5.7500, 21.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-13"]},
    {"gate": "D-03b", "measured": 0.0, "unit": "mm", "required": "<= 5 (reviewer from sections)", "margin": 5.0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "D-04a", "measured": 3.4, "unit": "mm", "required": ">= 3.25", "margin": 0.15, "at": "(-34.0000, 37.0000, -4.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "D-04c", "measured": 2.3, "unit": "mm", "required": ">= 0.5", "margin": 1.8, "at": "(-29.5000, 0.0000, 33.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "D-06a", "measured": 2.0, "unit": "mm", "required": ">= 1.0", "margin": 1.0, "at": "(-33.3182, 6.1011, 33.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "D-07", "measured": null, "unit": "", "required": "fit-critical bores: none on this part", "margin": null, "at": null, "status": "NOT_APPLICABLE", "assumes": []},
    {"gate": "REQ-01", "measured": 26.65, "unit": "mm", "required": "in [26.60, 26.70]", "margin": 0.05, "at": "(17.1303, 20.4151, 15.5500) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]},
    {"gate": "REQ-02", "measured": 26.65, "unit": "mm", "required": "<= 26.70 at 50/130 deg; no material r <= 32.0 at 40/140 deg (expected INCONCLUSIVE window reading recorded; first material 38.510); rib faces +-0.10", "margin": 0.05, "at": "(17.1303, 20.4151, 18.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]},
    {"gate": "REQ-03", "measured": 2.3, "unit": "mm", "required": ">= 2.0", "margin": 0.3, "at": "(-29.5000, 0.0000, 33.0000) mm to (-27.2, 0.0, 33.0)", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-03"]},
    {"gate": "REQ-04", "measured": 6.9e-13, "unit": "mm", "required": "clearance = 0 on a saddle arc; interference <= 0 (measured 0.0 mm3)", "margin": -6.9e-13, "at": "(-18.8444, 18.8444, 15.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]},
    {"gate": "REQ-05", "measured": 6.0, "unit": "mm", "required": ">= 6.0 x 2.5 clear, centres +-0.5, roofs >= 45 deg, ligament >= 2.0", "margin": 0.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-07"]},
    {"gate": "REQ-06", "measured": 29.5, "unit": "mm", "required": "|x| 29.5 +-0.1, z 13.0 ... 33.0 +-0.1, clearance >= 2.0", "margin": 0.1, "at": "(-29.5000, 19.3562, 23.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]},
    {"gate": "REQ-07", "measured": 3.4, "unit": "mm", "required": "4 x 3.4 +-0.1 through, offset <= 0.10 (measured 0.000)", "margin": 0.1, "at": "(-34.0000, 37.0000, -4.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-11"]},
    {"gate": "REQ-08", "measured": 40.0, "unit": "mm", "required": "max_y 40.00 +-0.10; thickness 3.0 +-0.1 (measured 3.000)", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-11"]},
    {"gate": "REQ-09", "measured": null, "unit": "", "required": "bench", "margin": null, "at": null, "status": "INCONCLUSIVE", "assumes": ["A-03", "A-05"]},
    {"gate": "exactly_one_solid", "measured": 1, "unit": "count", "required": "== 1", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "feature_census", "measured": 48, "unit": "count", "required": "plan tally re-tallied for spec 1.1", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "envelope_within_spec", "measured": 80.0, "unit": "mm", "required": "sizes +-0.1; position x +-40.0, y 0.0 ... 40.0, z -10.0 ... 42.0", "margin": 0.0, "at": null, "status": "PASS", "assumes": []}
  ],
  "sweep": [
    {"parameter": "foot_t", "values": [2.9, 3.0, 3.1], "all_built": true, "worst_gate": "D-01b", "worst_margin": 0.0},
    {"parameter": "r_in", "values": [26.60, 26.65, 26.70], "all_built": true, "worst_gate": "REQ-04 (fails at low and high)", "worst_margin": -25.09},
    {"parameter": "th0/th1", "values": [47.0, 45.0, 43.0], "all_built": true, "worst_gate": "REQ-04 nearest-point theta (high)", "worst_margin": -2.0},
    {"parameter": "post_x_in", "values": [29.4, 29.5, 29.6], "all_built": true, "worst_gate": "REQ-03", "worst_margin": 0.2},
    {"parameter": "slot_h", "values": [2.5, 2.5, 2.7], "all_built": true, "worst_gate": "D-01b", "worst_margin": 0.0},
    {"parameter": "slot_w", "values": [6.0, 6.0, 6.2], "all_built": true, "worst_gate": "D-01b (fails at high)", "worst_margin": -0.1},
    {"parameter": "slot_yc", "values": [6.5, 7.0, 7.5], "all_built": true, "worst_gate": "D-01b", "worst_margin": 0.0},
    {"parameter": "hole_d", "values": [3.3, 3.4, 3.5], "all_built": true, "worst_gate": "D-01b", "worst_margin": 0.0}
  ],
  "least_sure": [
    "REQ-03 margin 0.300 at the -X post is below the scan p95 0.448 (A-01)",
    "REQ-04 contact and the sleeve shape rest wholly on A-03; the assumed sleeve overlaps the coil by 1427.2 mm3",
    "zero-margin rows by spec dimensions: slot ligament 2.000, slot clear 6.0 x 2.5, gable roofs 45.000 deg; ties bear on the side plates' outer faces"
  ],
  "stopped": false
}
```
