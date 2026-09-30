# REPORT — od_c03_cradle v02 (20260930-od-c03-pump-cradle)

Designer: Claude Code, claude-opus-5-5 · spec version 1.2 · plan `01_CAD/DESIGN_PLAN.md` (WP-02) with the WP-03 (spec 1.1) and WP-05 (spec 1.2) amendments · build package WP-05, attempt 1 of 2, the round after RV01 · 2026-09-30 UTC

Every number below is measured by `01_CAD/check_od_c03_cradle_v02.py` on the re-imported STEP files (all 135 gate rows, with nearest points and reasons, are in `01_CAD/check_od_c03_cradle_v02.json`). Self-checks do not clear a hard gate; the reviewer's measurement does. Every v01 file is unchanged (88 files under `01_CAD/`, `02_STEP_STL/`, `03_Sections/` re-hashed after the v02 run, all match).

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_c03_cradle_v02.py` | 9c1995ab49819c5fd2b149f14670de7a05a1b44220dfea803254a01a82b70d56 | the v01 build with the spec 1.2 parameters (rib 1 z0 −3.0, post z0 12.0, slot centres z 17.0 / 28.0); Algebra mode; places OD-H01 and the sleeve; exports; runs the checks; `sweep` mode for D7 |
| `01_CAD/check_od_c03_cradle_v02.py` | 95dc64b0fca5ce7007e9332a357a7a913b8815c4feedb85cc56789a19bbf5d57 | the v01 checks with the spec 1.2 limits, written before the v02 build (D3); REQ-09 as Soft; information added: region clearances, OD-H01 centroid, REQ-02 segment distances (§8) |
| `01_CAD/check_od_c03_cradle_v02.json` | 915202548c8c46c3b2f9adc0103ab2a63f915384913fd9fecf131d8b83373921 | all 135 gate rows of the deliverable, assembly information, mass properties, export hashes |
| `01_CAD/sections_od_c03_cradle_v02.py` | fa42d4e468ea729950c1c298ca48e9618a784559c32d9cf53ca08856f7bd77a0 | D6 section script (`tools.drawing.write_sections`) |
| `01_CAD/sections_od_c03_cradle_v02.json` | 50193e6b41dfdbea8d7d5c3ddeb9642399d2836d3821802b58ecb37b45e3d007 | per section: plane, cut area, `nothing_clipped` |
| `01_CAD/sweep_v02/SHA256SUMS.txt` | 7ac3677893b05869ed3e7781a3a57686a1499d6f31a56baea96154f9f4c9be28 | SHA-256 of the 64 sweep files (16 variants × part STEP, assembly STEP, STL, result JSON) |
| `02_STEP_STL/od_c03_cradle_C1_v02.step` | 8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034 | AP242 (`tools.core.write_step`), one solid labelled `od_c03_cradle`, re-imported for every measurement |
| `02_STEP_STL/od_c03_assembly_C1_v02.step` | 8e1a6ea8ff66acecdd2cffdde41c1d7635541f4b34e9034f55ce6c4efaf43a14 | AP242 check assembly: `od_c03_cradle` (the re-imported part file), `OD_H01_ulka_ep5_pump` (identity joint), `od_h02_sleeve_assumed_A03` |
| `02_STEP_STL/od_c03_cradle_C1_v02.stl` | 529a0cc2033cddb00ee16715448a8e0e546f08eb05eb6bd1e6c20ce8a3776be4 | from the re-imported STEP with the cached triangulation cleared; tolerance 0.01 mm / angular 0.1 rad, 2540 triangles, measured sagitta 0.00489 mm |
| `03_Sections/od_c03_cradle_v02_xy_z0p0.png` | 51dc7f09bbf3b3e95a6b6623decb2430445b9504e50ab4a9decb1f602895faa7 | XY at z 0.0: rib 1, web, foot (no post at this level); nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_xy_z17p0.png` | 603139490d9c8a947e45d2f8aeb257b0a6ecad102d47e89d3987367439825df3 | XY at z 17.0: both post blocks through the front slots; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_xy_z28p0.png` | 4364ee45b5b8a12674cf4f0d509e7dd901cde4352e25421d9acff4333d056502 | XY at z 28.0: rib 2, both posts through the rear slots; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_yz_x0p0.png` | 3f1dbbc197ea6daef045738ba8ad42f889c5aa3f93ad38d2eb65a687163d7328 | YZ at x 0: rib faces z −3 / 3 / 25 / 31, foot 3.0; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_yz_x31p5.png` | 1f75434f7b2887c7321dbc50545af88d24e5f705f7e0d5fdc7a233177a588504 | YZ at x 31.5: +X post block z 12 … 33, both gabled slots, ligaments; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_yz_x34p0.png` | 577bc611c4691e5ddcc7118f907404b2a8eee2303356ef7c6fc4dbfbd73e1fd5 | YZ at x 34.0: the two +X frame holes through the foot; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_xz_y7p0.png` | 1f44f2bbdb0390b6380bf0f7b29e18f4b0a10364e5ee45ef2899a237491ee3c5 | XZ at y 7.0: slot centre plane through both posts; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_xz_y38p5.png` | 8ad305e86b536a0132bfac697ec2d0f56694afd3187a5fe40e7332ff48a602cc | XZ at y 38.5: foot with the four holes; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_assembly_xy_z0p0.png` | e36596521f8a6c8d0cca5d8bcddc8c58cf6708fc2192c48223fe1fc9379b7b24 | check assembly, XY at z 0.0: rib 1 on the sleeve, coil, side plates, spade tabs on −Y; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_assembly_xy_z28p0.png` | 4e58b33781602ce7e7833dbfa77a0f16055c3ba4fd5c22052b318775e65b2083 | check assembly, XY at z 28.0; nothing clipped (0) |
| `03_Sections/od_c03_cradle_v02_assembly_yz_x0p0.png` | 86a77ec2317d2f64fdfc5878ebac31b9492b3dd6837bcd53db906ae3348123cf | check assembly, YZ at x 0; nothing clipped (0) |

Inputs checked against the brief before any work: OD-H01 STEP b05302af…3fb62, params.json 21e02bf5…c43c, README.md 52b06473…7fa2, all three match.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1 (OCCT 7.9.3) · repo commit d7ea010502a30dd025c5123992847da1b15f3ee3

## 3. Gate self-check

Margin is signed, positive inside the limit; the worst row of each gate is shown, all rows are in the JSON file.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | — | PASS | — |
| U-02 | 80.000 × 40.000 × 52.000 mm | each in [spec − 0.1, spec + 0.1] | +0.100 | size; position below | PASS | — |
| U-02 position (reported apart) | x −40.000 … 40.000, y 0.000 … 40.000, z −10.000 … 42.000 | x ±40.0, y 0.0 … 40.0, z −10.0 … 42.0 | 0.000 each | — | PASS | — |
| U-03 (a) cradle\|OD-H01 | clearance 2.300 mm; interference 0.0 mm³ (OD-H01 sound: 1/1/0 on re-import) | ≥ 2.0; ≤ 0 | +0.300; 0 | (−29.500, 0.000, 33.000) on the −X post to (−27.200, 0.000, 33.000) on the −X side plate | PASS (assumed: A-01, A-03) | A-01, A-03 |
| U-03 (a) cradle\|sleeve | clearance 6.9e-13 mm; interference 0.0 mm³ | = 0; ≤ 0 | −6.9e-13 (inside the 0.005 band) | (−18.844, 18.844, −3.000), r 26.650, θ 135.0° (saddle arc edge of rib 1) | PASS (assumed: A-03) | A-03 |
| U-03 (b) | no motion variable | — | — | — | NOT_APPLICABLE (by its row: ties not modelled) | — |
| U-04 | schema AP242 1, solids 1, volume_delta 1.7e-10 mm³, faces_delta 0, labels 1, valid_after 1 | 1, 1, ≤ 0.001, 0, 1, 1 | 0 | — | PASS | — |
| U-05 | feature_census: plane 48, cylinder 6, cone/sphere/torus/bspline/other 0, concave cylinders 6, convex 0, bores 4; by position: 2 saddle arcs, 2 post blocks, 4 slots, 4 holes located, 1 foot underside | the same (plan §6 as re-tallied for spec 1.1, unchanged in 1.2) | 0 | — | PASS | — |
| U-06 (soft) | min_wall at 45°: 2.000 mm | ≥ 2.0 | −3e-15 (inside the band) | (−33.318, 6.101, 33.000), slot ligament to the post end face | PASS | — |
| U-07 | sagitta 0.00489 mm (fresh mesh of the re-imported STEP); angular 0.1000 rad; delivered STL 2540 triangles = re-mesh, 1 body, 0 naked edges | ≤ 0.01; ≤ 0.1000026 rad | +0.0051; +2.6e-6 | (−18.477, 19.198, 1.500) | PASS | — |
| U-08 | no threads | — | — | — | NOT_APPLICABLE (by its row) | — |
| D-01a | min_wall 2.000 mm | ≥ 0.8 | +1.200 | (−33.318, 6.101, 33.000) | PASS | — |
| D-01b | min_wall 2.000 mm | ≥ 2.0 | −3e-15 (inside the band) | (−33.318, 6.101, 33.000) | PASS | — |
| D-02 | 80.0 (X) × 52.0 (Z) on the bed, 40.0 (Y) tall | ≤ 420 × 420 × 500 | +340.0 / +368.0 / +460.0 | — | PASS (assumed: A-10) | A-10 |
| D-03a | least downward angle 45.000° (the eight gable roof faces; nothing else faces the bed) | ≥ 45 | 0.000 | (−29.500, 5.750, 20.000) | PASS (assumed: A-13) | A-13 |
| D-03b | largest flat downward face 0.0 mm (no flat ceiling; each gable apex is an edge) | ≤ 5 | +5.0 | designer reading; reviewer from sections | PASS | — |
| D-04a | four holes Ø3.400 mm | ≥ 3.25 | +0.150 | (±34.0, 37.0, −4.0), (±34.0, 37.0, 37.0) | PASS | — |
| D-04c | clearance to OD-H01 2.300 mm | ≥ 0.5 | +1.800 | as U-03 (a) | PASS (assumed: A-01) | A-01 |
| D-06a | min_wall 2.000 mm | ≥ 1.0 | +1.000 | as D-01b | PASS | — |
| D-07 | clearance holes only | — | — | — | NOT_APPLICABLE (by its row) | — |
| REQ-01 | inner radius min 26.650, max 26.650 mm in both windows (θ 50 … 130 step 5; z −2.5 … 2.5 and 25.5 … 30.5, 0.1 steps, margin 0) | in [26.60, 26.70] | +0.050 | (17.130, 20.415, −2.450) | PASS (assumed: A-03) | A-03 |
| REQ-02 | inner r at θ 50° and 130°, z 0 and 28: 26.650 mm; window r ≤ 32.0 at θ 40° and 140°, z 0 and 28: INCONCLUSIVE "no material" (the expected reading, recorded as such); positive control on the whole ray at z 28: first material 38.510 mm (the post at x ±29.5); at z 0 no post spans the level, so the whole-ray control is not run there (§8); the distance from the cradle to the ray segment r 0 … 32 is 2.323 mm at both angles and both levels (to the rib end edge at θ 45° / 135°); rib faces z −3.000, 3.000, 25.000, 31.000 | ≤ 26.70; no material within r ≤ 32.0; faces ± 0.10 | +0.050; +6.510 (z 28); +0.100 | (17.130, 20.415, 0.000); (29.500, 24.753, 28.000) | PASS (assumed: A-06) | A-06 |
| REQ-03 | clearance(cradle, OD-H01) 2.300 mm; by region: −X post 2.300, +X post 2.650, rib 1 2.788 (to the coil at (−16.878, 16.868, −3.0)), rib 2 2.788, foot ≥ 13.15 | ≥ 2.0 | +0.300 | (−29.500, 0.000, 33.000) to (−27.200, 0.000, 33.000) | PASS (assumed: A-01, A-03) | A-01, A-03 |
| REQ-04 | clearance(cradle, sleeve) 6.9e-13 mm, nearest point r 26.650 mm θ 135.0° on the saddle arc of rib 1; interference 0.0 mm³ | = 0 on a saddle arc; ≤ 0 | −6.9e-13 (inside the band) | (−18.844, 18.844, −3.000) | PASS (assumed: A-03) | A-03 |
| REQ-05 | four slots: clear 6.000 (Z) × 2.500 (Y), centres y 7.000, z 17.000 / 28.000, through 4.000 along X, roofs 45.000° from horizontal, ligament 2.000 mm (worst: slot to post end face at z 12 and 33; 5.000 between the two slots) | ≥ 6.0 × 2.5; y 7.0 ± 0.5; z ± 0.5; roofs ≥ 45°; ligament ≥ 2.0 | 0.000 (clear, roof, ligament) | slots at x ±(29.5 … 33.5) | PASS (assumed: A-07) | A-07 (A-13 for the roofs) |
| REQ-06 | inner faces \|x\| 29.500 (both), z 12.000 … 33.000 (both); post clearance 2.300 (−X), 2.650 (+X) | 29.5 ± 0.1, 12.0 / 33.0 ± 0.1; ≥ 2.0 | +0.100; +0.300 | (±29.5, 19.313, 22.5) | PASS (assumed: A-06) | A-06 |
| REQ-07 | four bores Ø3.400 mm, axis ±Y, offset 0.000 mm, through 1, at (±34.0, z −4.0) and (±34.0, z 37.0) | Ø3.4 ± 0.1; offset ≤ 0.10; through | +0.100 | as D-04a | PASS (assumed: A-11) | A-11 |
| REQ-08 | underside max_y 40.000 mm; thickness 3.000 mm (foot top face y 37.000) | 40.00 ± 0.10; 3.0 ± 0.1 | +0.100 | — | PASS (assumed: A-11) | A-11 |
| REQ-09 (Soft) | bench row, not geometric (spec 1.2: Soft); nothing a build measures | no unacceptable vibration with the OEM sleeve | — | — | INCONCLUSIVE (Soft, bench: answered by the first run; not a hard failure) | A-03, A-05 |
| exactly_one_solid | 1 | 1 | 0 | — | PASS | — |
| feature_census | as U-05 | 48 planar faces (foot 6, ribs 2 × 6, post blocks 2 × (5 + 2 × 5)), 6 concave cylinders, 4 bores | 0 | — | PASS | — |
| envelope_within_spec | size 80.000 × 40.000 × 52.000; position x −40.000 … 40.000, y 0.000 … 40.000, z −10.000 … 42.000 | as U-02 | +0.100 size; 0.000 position | — | PASS | — |

## 4. Robustness sweep (D7)

Each variant rebuilt from the v02 parameters, exported to `01_CAD/sweep_v02/`, re-imported, and run through the same predicates, including the check assembly with OD-H01 and the sleeve. Every variant built exactly one valid solid. No motion variable exists (U-03 b).

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| foot_t (underside held at 40.0) | 2.9 · 3.0 · 3.1 | yes | D-01b / REQ-05 ligament (unchanged) | 0.000 |
| r_in (saddle) | 26.60 · 26.65 · 26.70 | yes | REQ-04 / U-03 (a) cradle\|sleeve: FAIL at both ends (low: interference 25.09 mm³; high: gap 0.050 mm); REQ-01 and REQ-02 pass at both; rib clearance to OD-H01 2.738 (low) / 2.838 (high) | −25.09 mm³ (low), −0.050 mm (high) |
| th0 / th1 (sector) | 47/133 · 45/135 · 43/137 | yes | REQ-04 nearest-point θ row: 137.0° at 43/137, outside the spec's 45 … 135 sector (the row reads the sector parameter itself); REQ-02 θ 40°/140° still no material within r ≤ 32 (segment distance 1.395 at 43/137, 3.248 at 47/133); rib clearance 2.786 / 2.791; REQ-03 2.300 | −2.0° (high) |
| post_x_in | 29.4 · 29.5 · 29.6 | yes | REQ-03 2.200 / 2.300 / 2.400 | +0.200 |
| slot_h | 2.5 · 2.5 · 2.7 | yes | D-01b / REQ-05 ligament (unchanged) | 0.000 |
| slot_w | 6.0 · 6.0 · 6.2 | yes | D-01b, U-06, REQ-05 ligament 1.900: FAIL at 6.2 | −0.100 (high) |
| slot_yc | 6.5 · 7.0 · 7.5 | yes | D-01b / REQ-05 ligament (unchanged) | 0.000 |
| hole_d | 3.3 · 3.4 · 3.5 | yes | D-01b / REQ-05 ligament (unchanged) | 0.000 |

The part passes every gate at nominal. As in v01, two rows pass only at nominal, both from the spec's own values: REQ-04 (a designed zero-gap contact, so any saddle radius other than 26.65 fails it by construction) and the slot ligament (D-01b, U-06, REQ-05: the 21.0 post block z 12 … 33 with 6.0 slots centred at z 17 and 28 leaves exactly 2.0 at each end face, so any widening of a slot fails it).

## 5. Build facts

- Envelope 80.000 × 40.000 × 52.000 mm; volume 25 458.5 mm³; mass 32.33 g at 1270 kg/m³ (A-09); centre of mass (0.000, 31.708, 16.917).
- Fillets: none requested (plan §4 `fillet_r`), none built; every gated face is analytic.
- Placements: OD-H01 placed by a RigidJoint on the cradle at the origin, axis +Z, identity (`pump_axis` to the pump's `datum`), checked on re-import (side plates at x −27.20 / 26.85 read in place, REQ-03 nearest point). The sleeve `od_h02_sleeve_assumed_A03` (ID 47.3, OD 53.3, z −6.0 … 32.0, cut to |x| ≤ 23.5) placed by the same joint; it is two solids (the tube cut at |x| ≤ 23.5 < 23.65 separates into a +Y and a −Y arc).
- Construction: the rib webs and the post blocks overlap the foot by 1.0 so each union is a volume overlap, not a face contact; the finished faces are unchanged (the foot top face reads y 37.000).
- Information, not a §5 pair: the assumed sleeve shares 1427.2 mm³ with OD-H01 (as v01; the coil is 0.2 off-axis and slightly conical).

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | Foot under the pump (+Y down); the sleeve-clad coil rests in two saddles centred on +Y, now at z −3 … 3 and 25 … 31, which bracket the OD-H01 centroid at z 7.23 (measured, (−0.067, −0.872, 7.232)); load path saddle → web → foot → four M3 screws. |
| P2 | Function chains | Ties pass through the post slots at z 17 (tie band 14.6 … 19.4) and z 28 over the −Y side of the sleeve; the −Y side features end at z 13.6 (slot box) and 5.5 (spade tabs), so both ties ride on the sleeve; rib 1 (z −3 … 3) lies on +Y, opposite the spade tabs and slot box (assembly section at z 0). The tie loop crosses the side plates' outer faces (RV01 F3, carried in A-07). |
| P3 | Motion clearance | No moving part; the vibrating pump keeps 2.300 (−X post), 2.650 (+X post), 2.788 (rib 1 and rib 2 to the coil) and ≥ 13.15 (foot) from the cradle at the identity pose. |
| P4 | Human factors | The four holes lie outside the pump's \|x\| ≤ 27.2 and beyond the post blocks in z (post block ends at z 12 / 33 against holes at z −4 / 37), so a driver reaches every screw head from above (−Y); the 6.0 × 2.5 slots pass a 4.8 × 1.4 tie. |
| P5 | Absurdity next to a real product | An 80 × 52 × 40 mm, 32 g PETG cradle for a 0.5 kg vibratory pump on a rubber sleeve is in proportion with OEM pump brackets; saddles now at both ends of the coil, like a two-point OEM mount. |
| P6 | Nothing floating, embedded, mirrored or upside-down | One solid; nothing floats. The assumed sleeve is embedded in the coil by 1427.2 mm³ (an A-03 shape limit). Section pictures draw +Y toward the foot; the model is in the spec frame, not mirrored or inverted. |

## 7. Library and tools used; RV01 findings

- Cards: none (plan §2: no card matches a saddle cradle with strap retention).
- `tools.core`: `read_step`, `write_step` (AP242), `compare_step`, `validity`, `write_stl` (with its `mesh_sagitta`).
- `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `min_wall` (with its 45° reading for U-06), `overhang_census(build_dir=(0,−1,0))`, `radial_profile`, `radial_extent`, `clearance` (also against an Edge for the REQ-02 segment information), `interference`, `mesh_census`, `mass_properties`; `tools.measure.features.cylinder` to select the saddle faces.
- `tools.drawing.write_sections` and its `nothing_clipped`; `tools.result.gate`.
- New code: job-local only (the three v02 scripts in `01_CAD/`); nothing in the repo. No missing `tools/measure` function.

RV01 findings (brief):

- F1 REQ-09: spec 1.2 makes the row Soft; reported INCONCLUSIVE (bench), not a hard failure.
- F2 centre of mass: OD-H01 centroid measured at z 7.232 mm (`mass_properties` of the re-imported pump solid, uniform density; x −0.067, y −0.872). The saddle span is now z −3.0 … 31.0 (rib faces measured), so the centroid lies inside it, 10.23 from the front face of rib 1 and 23.77 from the rear face of rib 2. The centroid assumes uniform density; the real pump's mass distribution (coil copper, steel frame) is not in the input.
- F3 tie loop over the side plates: carried in A-07; no geometry change.
- F4 REQ-04 zero gap only at r 26.650: carried in A-03; r kept at 26.65 exactly; the r_in sweep reproduces the v01 reading (§4).
- F5 REQ-03 margin 0.300: carried in A-01, A-04; no change; measured clearance 2.300 between (−29.500, 0.000, 33.000) on the −X post and (−27.200, 0.000, 33.000) on the −X side plate (the same 2.300 also at the post's front end z 12.0).
- F6 zero-margin ligaments and slot section: by the spec's own values; no change.

## 8. Deviations from the plan

1. Spec 1.2 amendments (brief WP-05, checked by the orchestrator), built as given: rib 1 over z −3.0 … 3.0 (rib 2 unchanged, z 25.0 … 31.0; rib faces z −3, 3, 25, 31); REQ-01 windows z −2.5 … 2.5 and 25.5 … 30.5; REQ-02 levels z 0.0 and 28.0; post blocks z 12.0 … 33.0 (inner face |x| 29.5, 4.0 thick, top y 0.0 unchanged); slot centres y 7.0, z 17.0 / 28.0 (clear 6.0 × 2.5, 45° gables); REQ-09 Soft. The spec 1.1 amendments of WP-03 stand as built in v01 (foot z −10 … 42, holes at z −4 / 37, sleeve cut to |x| ≤ 23.5, census 48 planar faces).
2. REQ-02 positive control: the brief names "the post at r 38.51 on the whole ray" for both levels, but at z 0.0 no post block spans the level (posts z 12 … 33, per REQ-06), and the whole ray at θ 40° / 140° holds no material (it passes beyond the foot's x ±40 edge). The whole-ray row is therefore run at z 28.0 only (38.510 at both angles); at z 0.0 and z 28.0 the check records, as information, the measured distance from the cradle to the segment r 0 … 32.0 (2.323 mm, nearest on the rib end edge at θ 45° / 135°). No threshold was invented for this information; the gated half of REQ-02 at θ 40° / 140° remains the recorded INCONCLUSIVE "no material" plus the reviewer's sections.
3. Information added to the check (no gate): clearance of each cradle region (rib 1, rib 2, each post block, foot) to OD-H01, and the OD-H01 centroid against the saddle span (RV01 F2). The foot region box starts at y 36.9, so its 13.15 reads at the box cut through the webs; the foot surface itself is 13.25 from the coil (v01 D2 probe).
4. Sections: planes moved with the ribs and slots (XY at z 0.0, 17.0, 28.0; check-assembly XY at z 0.0 and 28.0), others as v01.
5. Scripts carry `_v02` in their names (the brief); the v01 scripts are left as they were.
6. Construction overlap of 1.0 into the foot for the rib webs and posts (stated derivation in the build parameters; no face moves), as v01.

Fix cycles used: 0 of 3 (the first v02 build passed every gated row at nominal; no re-export).

## 9. What I am least sure of

1. REQ-03 margin 0.300 at the −X post (to the −X side plate at x −27.20) is below the scan's p95 deviation 0.448 (A-01); the post_x_in sweep gives 2.200 at 29.4. The longer v02 post block (z 12 … 33) faces the same plate over a longer run, so a plate bowed or placed 0.3 further out would touch it; calipers on the frame (A-04) retire it.
2. The saddle contact (REQ-04) and the sleeve shape rest wholly on A-03: the zero-gap contact is exact only against a model, and ±0.05 on the saddle radius turns it into a 0.05 gap or a 25 mm³ overlap. Rib 1 at z −3 … 3 sits 3.0 inside the assumed sleeve's front end (z −6.0); if the real OEM sleeve is shorter at the outlet end, rib 1 would bear on the bare coil.
3. The centre-of-mass answer to F2 uses the uniform-density centroid of the scan solid (z 7.23); the real mass distribution is unknown, although any plausible centroid between the two end plates lies inside the saddle span z −3 … 31.

## 10. Stop

Not stopped.

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20260930-od-c03-pump-cradle",
  "part": "od_c03_cradle",
  "tag": "v02",
  "spec_version": "1.2",
  "files": [
    {"path": "01_CAD/build_od_c03_cradle_v02.py", "sha256": "9c1995ab49819c5fd2b149f14670de7a05a1b44220dfea803254a01a82b70d56"},
    {"path": "01_CAD/check_od_c03_cradle_v02.py", "sha256": "95dc64b0fca5ce7007e9332a357a7a913b8815c4feedb85cc56789a19bbf5d57"},
    {"path": "01_CAD/check_od_c03_cradle_v02.json", "sha256": "915202548c8c46c3b2f9adc0103ab2a63f915384913fd9fecf131d8b83373921"},
    {"path": "01_CAD/sections_od_c03_cradle_v02.py", "sha256": "fa42d4e468ea729950c1c298ca48e9618a784559c32d9cf53ca08856f7bd77a0"},
    {"path": "01_CAD/sections_od_c03_cradle_v02.json", "sha256": "50193e6b41dfdbea8d7d5c3ddeb9642399d2836d3821802b58ecb37b45e3d007"},
    {"path": "01_CAD/sweep_v02/SHA256SUMS.txt", "sha256": "7ac3677893b05869ed3e7781a3a57686a1499d6f31a56baea96154f9f4c9be28"},
    {"path": "02_STEP_STL/od_c03_cradle_C1_v02.step", "sha256": "8d6f60ba1b4c3bcc6da1d40037ffa6ac422c4bf78f0f826553f2ffc1de037034"},
    {"path": "02_STEP_STL/od_c03_assembly_C1_v02.step", "sha256": "8e1a6ea8ff66acecdd2cffdde41c1d7635541f4b34e9034f55ce6c4efaf43a14"},
    {"path": "02_STEP_STL/od_c03_cradle_C1_v02.stl", "sha256": "529a0cc2033cddb00ee16715448a8e0e546f08eb05eb6bd1e6c20ce8a3776be4"},
    {"path": "03_Sections/od_c03_cradle_v02_xy_z0p0.png", "sha256": "51dc7f09bbf3b3e95a6b6623decb2430445b9504e50ab4a9decb1f602895faa7"},
    {"path": "03_Sections/od_c03_cradle_v02_xy_z17p0.png", "sha256": "603139490d9c8a947e45d2f8aeb257b0a6ecad102d47e89d3987367439825df3"},
    {"path": "03_Sections/od_c03_cradle_v02_xy_z28p0.png", "sha256": "4364ee45b5b8a12674cf4f0d509e7dd901cde4352e25421d9acff4333d056502"},
    {"path": "03_Sections/od_c03_cradle_v02_yz_x0p0.png", "sha256": "3f1dbbc197ea6daef045738ba8ad42f889c5aa3f93ad38d2eb65a687163d7328"},
    {"path": "03_Sections/od_c03_cradle_v02_yz_x31p5.png", "sha256": "1f75434f7b2887c7321dbc50545af88d24e5f705f7e0d5fdc7a233177a588504"},
    {"path": "03_Sections/od_c03_cradle_v02_yz_x34p0.png", "sha256": "577bc611c4691e5ddcc7118f907404b2a8eee2303356ef7c6fc4dbfbd73e1fd5"},
    {"path": "03_Sections/od_c03_cradle_v02_xz_y7p0.png", "sha256": "1f44f2bbdb0390b6380bf0f7b29e18f4b0a10364e5ee45ef2899a237491ee3c5"},
    {"path": "03_Sections/od_c03_cradle_v02_xz_y38p5.png", "sha256": "8ad305e86b536a0132bfac697ec2d0f56694afd3187a5fe40e7332ff48a602cc"},
    {"path": "03_Sections/od_c03_cradle_v02_assembly_xy_z0p0.png", "sha256": "e36596521f8a6c8d0cca5d8bcddc8c58cf6708fc2192c48223fe1fc9379b7b24"},
    {"path": "03_Sections/od_c03_cradle_v02_assembly_xy_z28p0.png", "sha256": "4e58b33781602ce7e7833dbfa77a0f16055c3ba4fd5c22052b318775e65b2083"},
    {"path": "03_Sections/od_c03_cradle_v02_assembly_yz_x0p0.png", "sha256": "86a77ec2317d2f64fdfc5878ebac31b9492b3dd6837bcd53db906ae3348123cf"}
  ],
  "versions": {"python": "3.13.7", "build123d": "0.11.1", "ocp": "7.9.3.1 (OCCT 7.9.3)", "repo_commit": "d7ea010502a30dd025c5123992847da1b15f3ee3"},
  "gates": [
    {"gate": "U-01", "measured": 1, "unit": "count", "required": "solid_count 1, brep_valid 1, naked_edges 0", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-02", "measured": 80.0, "unit": "mm", "required": "80.0 x 40.0 x 52.0 each +-0.1 (worst: size_x)", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-03 (a)", "measured": 2.3, "unit": "mm", "required": "cradle|OD-H01 >= 2.0 and interference <= 0; cradle|sleeve = 0 and interference <= 0", "margin": 0.3, "at": "(-29.5000, 0.0000, 33.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-03"]},
    {"gate": "U-03 (b)", "measured": null, "unit": "", "required": "no motion variable", "margin": null, "at": null, "status": "NOT_APPLICABLE", "assumes": []},
    {"gate": "U-04", "measured": 1.7e-10, "unit": "mm3", "required": "volume_delta <= 0.001; schema, solids, faces, labels, valid_after", "margin": -1.7e-10, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-05", "measured": 48, "unit": "count", "required": "plane 48, cylinder 6, concave cylinders 6, bores 4; 2 ribs, 2 post blocks, 4 slots, 4 holes, 1 foot", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-06", "measured": 2.0, "unit": "mm", "required": ">= 2.0 (soft)", "margin": -3e-15, "at": "(-33.3182, 6.1011, 33.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "U-07", "measured": 0.00489, "unit": "mm", "required": "sagitta <= 0.01; angular <= 0.1000026 rad", "margin": 0.00511, "at": "(-18.4766, 19.1984, 1.5000) mm", "status": "PASS", "assumes": []},
    {"gate": "U-08", "measured": null, "unit": "", "required": "threaded parts only", "margin": null, "at": null, "status": "NOT_APPLICABLE", "assumes": []},
    {"gate": "D-01a", "measured": 2.0, "unit": "mm", "required": ">= 0.8", "margin": 1.2, "at": "(-33.3182, 6.1011, 33.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "D-01b", "measured": 2.0, "unit": "mm", "required": ">= 2.0", "margin": -3e-15, "at": "(-33.3182, 6.1011, 33.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "D-02", "measured": 80.0, "unit": "mm", "required": "<= 420 x 420 x 500", "margin": 340.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-10"]},
    {"gate": "D-03a", "measured": 45.0, "unit": "deg", "required": ">= 45", "margin": 0.0, "at": "(-29.5000, 5.7500, 20.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-13"]},
    {"gate": "D-03b", "measured": 0.0, "unit": "mm", "required": "<= 5 (reviewer from sections)", "margin": 5.0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "D-04a", "measured": 3.4, "unit": "mm", "required": ">= 3.25", "margin": 0.15, "at": "(-34.0000, 37.0000, -4.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "D-04c", "measured": 2.3, "unit": "mm", "required": ">= 0.5", "margin": 1.8, "at": "(-29.5000, 0.0000, 33.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "D-06a", "measured": 2.0, "unit": "mm", "required": ">= 1.0", "margin": 1.0, "at": "(-33.3182, 6.1011, 33.0000) mm", "status": "PASS", "assumes": []},
    {"gate": "D-07", "measured": null, "unit": "", "required": "fit-critical bores: none on this part", "margin": null, "at": null, "status": "NOT_APPLICABLE", "assumes": []},
    {"gate": "REQ-01", "measured": 26.65, "unit": "mm", "required": "in [26.60, 26.70], theta 50..130 step 5, z -2.5..2.5 and 25.5..30.5", "margin": 0.05, "at": "(17.1303, 20.4151, -2.4500) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]},
    {"gate": "REQ-02", "measured": 26.65, "unit": "mm", "required": "<= 26.70 at 50/130 deg, z 0 and 28; no material r <= 32.0 at 40/140 deg (expected INCONCLUSIVE window reading recorded; first material 38.510 at z 28; segment distance 2.323 at z 0 and 28); rib faces -3, 3, 25, 31 +-0.10", "margin": 0.05, "at": "(17.1303, 20.4151, 0.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]},
    {"gate": "REQ-03", "measured": 2.3, "unit": "mm", "required": ">= 2.0", "margin": 0.3, "at": "(-29.5000, 0.0000, 33.0000) mm to (-27.2, 0.0, 33.0)", "status": "PASS_ASSUMED", "assumes": ["A-01", "A-03"]},
    {"gate": "REQ-04", "measured": 6.9e-13, "unit": "mm", "required": "clearance = 0 on a saddle arc; interference <= 0 (measured 0.0 mm3)", "margin": -6.9e-13, "at": "(-18.8444, 18.8444, -3.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-03"]},
    {"gate": "REQ-05", "measured": 6.0, "unit": "mm", "required": ">= 6.0 x 2.5 clear, centres y 7.0 and z 17.0 / 28.0 +-0.5, roofs >= 45 deg, ligament >= 2.0", "margin": 0.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-07"]},
    {"gate": "REQ-06", "measured": 29.5, "unit": "mm", "required": "|x| 29.5 +-0.1, z 12.0 ... 33.0 +-0.1, clearance >= 2.0", "margin": 0.1, "at": "(-29.5000, 19.3128, 22.5000) mm", "status": "PASS_ASSUMED", "assumes": ["A-06"]},
    {"gate": "REQ-07", "measured": 3.4, "unit": "mm", "required": "4 x 3.4 +-0.1 through, offset <= 0.10 (measured 0.000)", "margin": 0.1, "at": "(-34.0000, 37.0000, -4.0000) mm", "status": "PASS_ASSUMED", "assumes": ["A-11"]},
    {"gate": "REQ-08", "measured": 40.0, "unit": "mm", "required": "max_y 40.00 +-0.10; thickness 3.0 +-0.1 (measured 3.000)", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-11"]},
    {"gate": "REQ-09", "measured": null, "unit": "", "required": "Soft, bench: no unacceptable vibration", "margin": null, "at": null, "status": "INCONCLUSIVE", "assumes": ["A-03", "A-05"]},
    {"gate": "exactly_one_solid", "measured": 1, "unit": "count", "required": "== 1", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "feature_census", "measured": 48, "unit": "count", "required": "plan tally re-tallied for spec 1.1, unchanged in 1.2", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "envelope_within_spec", "measured": 80.0, "unit": "mm", "required": "sizes +-0.1; position x +-40.0, y 0.0 ... 40.0, z -10.0 ... 42.0", "margin": 0.0, "at": null, "status": "PASS", "assumes": []}
  ],
  "rv01_findings": {"F2_od_h01_centroid_z": 7.232, "saddle_span_z": [-3.0, 31.0], "inside_span": true},
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
  "fix_cycles": {"used": 0, "cap": 3},
  "least_sure": [
    "REQ-03 margin 0.300 at the -X post is below the scan p95 0.448 (A-01)",
    "REQ-04 contact and the sleeve shape rest wholly on A-03; rib 1 sits 3.0 inside the assumed sleeve's front end",
    "F2 answered with the uniform-density centroid of the scan solid (z 7.23)"
  ],
  "stopped": false
}
```
