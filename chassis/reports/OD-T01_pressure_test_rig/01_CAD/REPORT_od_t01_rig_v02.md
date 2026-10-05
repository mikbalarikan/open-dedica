# REPORT — od_t01_rig v02 (20261002-od-t01-pressure-test-rig)

Designer: designer subagent (Claude Code) · spec version 1.3 (SHA-256 9f329e11…1330195) · plan `01_CAD/DESIGN_PLAN.md` (SHA-256 544bde71…0a5d) · 2026-10-03 UTC · J3 package WP-05, build attempt 2 of 2, concept C1, fix_cycles 0 of 3

<!-- Placed by the orchestrator from the designer's returned text: a session hook blocked the designer's own write of this file. -->

Before any work, every input was checked against the brief: the brief, the spec, the plan, and the eleven files in `00_Spec/inputs/` (WP-02 values). All hashes matched. The v01 files are untouched, and their hashes still match REPORT v01 §1. The v02 scripts are copies of the v01 scripts with `_v02` in their names, changed only as §8 states.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/build_od_t01_rig_v02.py` | 537aae6dc66c361343fc6adb99bdc06adbe3f85f5cb417806a4c9a7a60f78b07 | parametric script, Algebra mode, one `Params` structure (plate_y1 160.0, cbore_floor_y 140.0) |
| `01_CAD/check_od_t01_rig_v02.py` | cc94c52be8f9ddce5b3047e0e34a7ec462c211edd1cd14d2c7be277779dd4c10 | checks, updated to spec 1.3 §5 before the build (D3) |
| `01_CAD/sweep_od_t01_rig_v02.py` | 8987669578028c8011287d7804e513e3ab68bc07918c22c20d93a092759d0333 | D7 sweep driver |
| `01_CAD/sections_od_t01_rig_v02.py` | 95419cbfa29893ed8bce595fc8833fff1f5bc7770c1c2d70b19832cb64214ef2 | D6 sections |
| `02_STEP_STL/od_t01_rig_C1_v02.step` | 18c9de8f013cb7ce84eba3ce104ab6fb01fc84f79f8524140cfadb9d3feaf810 | AP242 (`tools.core.write_step`), body `od_t01_rig`, re-imported for every measurement |
| `02_STEP_STL/od_t01_rig_C1_v02.stl` | 183e58f0eda9287450d79d1a15aa3a4dabcf694449a6b82ae3a9ef9f24bfbd3f | meshed from the re-imported STEP after clearing the cached triangulation; tolerance 0.01 mm, angular 0.10 rad, 5752 triangles, max sagitta 0.0050 mm |
| `02_STEP_STL/od_t01_assembly_C1_v02.step` | c6caa17478e570e0b9200d813ee69fa674d68d2f9d6a91db216f4a5a1f18c072 | check assembly: rig + OD-G01 housing + OD-G04 + OD-G10 (locked), at the spec §2 pose on the measured seat y 135.000 |
| `03_Sections/od_t01_rig_v02_z0_assembly.png` | 7b37fd6df626973922208a3ab41d34c29418313a9028223cf6a7826898dbe96b | z 0 through the axis, with the housing set; nothing_clipped 0 |
| `03_Sections/od_t01_rig_v02_z44_assembly.png` | b93398a4d4617a43bebaaf6a8ba366fc9e450b97ad79cc4e571e42efce95cfb7 | z +44 through two counterbores, with the housing set; nothing_clipped 0 |
| `03_Sections/od_t01_rig_v02_x44.png` | 20f241a6cdc4deef5b6397a1e7d0f2ea11895c2877f000c3cd60b41e9009cb33 | x +44 through two screw holes: counterbores 20 deep, 5.0 of plate under each; nothing_clipped 0 |
| `03_Sections/od_t01_rig_v02_x0.png` | 4d95cd78d17258d41d1f9b776a85cdfe45ad407591926a06a44c5d43d7cc5e5a | x 0 through the hub window: the plate section of REQ-08 / A-02; nothing_clipped 0 |
| `03_Sections/od_t01_rig_v02_y5.png` | 9ea632d7cbf6e3c9c9901269be5b5b54a501dc95b7e20ad5108fc6387a2efd29 | y 5 through the base and the bench holes; nothing_clipped 0 |
| `03_Sections/od_t01_rig_v02_y147.png` | 0ceb47485189140a97e0728a5c98ded17ff94b60b12e3d2f8ad0c89dd84df4df | y 147.5 (mid-plate): window and counterbore teardrops; nothing_clipped 0 |
| `01_CAD/gates_od_t01_rig_v02.json` | 8b3fa3372ff4e37126f4cac7adece4f8dd232f140463a828faa59342787b0843 | all 173 check rows on the delivered STEP |
| `01_CAD/check_v02.log` | cbe04b062e7ac2acbc3fba7fa9ee9ac9a5a8d63ea1dbea300f03a321d93852dd | console output of that check |
| `01_CAD/od_t01_rig_C1_v02.params.json` | 48449c6f08185de3b6815cb610df5b6ea33c74b1c72431e802aea0ed5d583b38 | the build's parameters (used by U-04) |
| `01_CAD/od_t01_rig_C1_v02.mesh.json` | 9200b2e751b44c8dcb6ed71d484dbffe1d602f6130eb7fc0c9058fe2763b4f9b | STL record (U-07) |
| `01_CAD/sections_v02.json` | a4e115b277baf082aa398a8b14729e32fb452713ca761381b3df95428569aa07 | section record |
| `01_CAD/sweep_v02/sweep_index.json` | a3ac0412f005312929509524ad393a31e9db5b2dd8cb2c0696fbaadb93490331 | 20 sweep runs |
| `01_CAD/sweep_v02/sweep_summary.json` | 1d1070b1d8caed95a33da78b8b6590aedca51dfb8fe279a9731944a513961f92 | per-run status and worst margins |
| `01_CAD/sweep_v02.log` | 81fb71e05442a716754ac9c8c5692d9ec69a505c5c65e582d563b01baf871798 | console output of the sweep |

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1 · tools from the repo (`tools.core`, `tools.measure`, `tools.drawing`, `tools.result`) · repo commit 10929db1408d89144bd4af9cad971440427933d0

## 3. Gate self-check

All values were measured on the re-imported `02_STEP_STL/od_t01_rig_C1_v02.step`, and on the housing set placed by the measured seat. Bands are from GATES §0: mm 0.005, deg 0.001, rad 0.00002, mm³ 0.001, counts 0. Where a gate has several rows, the row shown is the least margin. Every row is in `gates_od_t01_rig_v02.json`. A self-check clears no HARD gate.

| Gate | Measured | Required (spec 1.3 §5) | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 solid | 1 | 0 | — | PASS | — |
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1, 1, 0 | 0 | — | PASS | — |
| U-02 | 240.000 × 160.000 × 120.000 | each in [spec − 0.1, spec + 0.1] | +0.100 | — | PASS | — |
| envelope_within_spec | size 240.000 × 160.000 × 120.000; position (reported apart) x −120.000 … 120.000, y 0.000 … 160.000, z −60.000 … 60.000 | size and position each ± 0.1 | +0.100 | — | PASS | — |
| U-03a | Housing contact clearance 0.000, nearest point y 135.000. Posed housing top y 135.0000001 against the underside 135.000 (−1e−7, in band). Interference rig with housing 0.000 mm³, rig with OD-G04 0.000 mm³. Rig below y 135 to the housing 15.010. Rig to OD-G04 5.000. Rig to OD-G10 13.689, not inside | contact = 0; interference ≤ 0; elsewhere ≥ 2.0 | +3.000 (OD-G04) | (−21.25, 135.00, 21.18), OD-G04 top | PASS (assumed: A-01) | A-01 |
| U-03b | 16 poses, dy 0 … −30 in 2.0 steps. Interference with the housing and with OD-G04 0.000 mm³ at every pose. OD-G10 least clearance 13.689 (at dy 0), never inside | interference ≤ 0 at every step (OD-G10: clearance > 0, not inside) | 0.000 mm³ | — | PASS (assumed: A-01) | A-01 |
| U-04 | AP242; 1 solid; volume delta 6.7e−8 mm³; face delta 0; label `od_t01_rig`; valid after re-import; 0 stray shells | unchanged, named, no stray shells, valid | −6.7e−8 mm³ (in band) | — | PASS | — |
| U-05 / feature_census | Faces: 41 planar, 13 concave cylinders, 0 convex, 0 other. Bores along Y: 4 × Ø3.4, 4 × Ø6.5, 1 × Ø60, 4 × Ø4.5. Corner chamfer planes 4. Wall inner faces 2, each z −60.000 … +40.000 | 1 plate, 2 walls (z −60 … +40), 1 base, 4 chamfers, 4 + 4 holes and counterbores, 1 window, 4 bench holes | 0 | — | PASS | — |
| U-06 (Soft) | min_wall wide 5.000 | ≥ 2.0 | +3.000 | (−45.10, 135.00, −47.04), plate under a counterbore | PASS | — |
| U-07 | chordal 0.01; angular 0.10 rad; stl_max_sagitta 0.0050 (re-meshed from the STEP, 5752 triangles = delivered STL); delivered STL 1 body, 0 naked edges, winding consistent | tol ≤ 0.01; angular ≤ 4·acos(1 − 0.01/30) = 0.1033 rad; sagitta ≤ 0.01 | +0.0050 (sagitta) | — | PASS | — |
| U-08 | — | N/A by its row (no threads) | — | — | N/A | — |
| D-01a | min_wall 5.000 | ≥ 0.8 | +4.200 | (−45.10, 135.00, −47.04) | PASS | — |
| D-01b | min_wall 5.000 | ≥ 2.0 | +3.000 | (−45.10, 135.00, −47.04) | PASS (assumed: A-08) | A-08 |
| D-02 | 240.0 × 160.0 on the bed, 120.0 tall | ≤ 420 × 420 × 500 | +180.0 (least: bed X) | — | PASS (assumed: A-09) | A-09 |
| D-03a | Least downward angle 45.100° (build +Z), measured on the census copy with the four Ø3.4 holes filled (one solid); per kind: cylinder 45.1, plane 45.1. Unfilled: least 0.0° at (−44.0, 135.0, −42.3). This point lies on a Ø3.4 crown (the named exception), located against the measured hole axes and ends | ≥ 45° (Ø3.4 crowns excepted) | +0.100° | (21.25, 135.00, 21.18), window teardrop flank | PASS (assumed: A-10) | A-10 |
| D-03b | flat_ceiling_spans 0; Ø3.4 crown chord 3.400 | ≤ 5 (crowns ≤ 3.4); reviewer row from sections | +0.100 | — | PASS (assumed: A-10); reviewer row | A-10 |
| D-04a | screw holes 4 × Ø3.400; bench holes 4 × Ø4.500 | ≥ 3.25; ≥ 4.25 | +0.150 | — | PASS | — |
| D-06a | min_wall 5.000 | ≥ 1.0 | +4.000 | — | PASS | — |
| D-07 | — | N/A by its row (clearance holes only) | — | — | N/A | — |
| J-05 | — | N/A by its row (no threaded holes) | — | — | N/A | — |
| REQ-01 | 4 × Ø3.400. Axis offset from the posed insert bores 0.000. Each hole opens at y 135.000 and runs through into its counterbore. 4 × Ø6.500 counterbores, offset 0.000, from y 160.000 to a floor at y 140.000. Plate under each head 5.000 | Ø3.4 ± 0.1; offset ≤ 0.10; Ø6.5 ± 0.1 from y 160.0 to y 140.00 ± 0.10; 5.0 ± 0.1 under the head | +0.100 | — | PASS (assumed: A-01) | A-01 |
| REQ-02 | One underside plane at y 135.000. The housing square's corners and edge midpoints (x ±50, z ±50) lie on it, 0.000 off. Contact clearance 0 (U-03a) | y 135.00 ± 0.10, one plane over x ±50, z ±50 | +0.100 | — | PASS (assumed: A-01) | A-01 |
| REQ-03 | Window Ø60.000, offset 0.000 from the axis, through the plate. Two roof flanks at 45.100°. Apex z +42.501 (radial_extent at y 147.5). OD-G04 to the rig 5.000. Pair-B axes to the window face: 10.970 at (+10.64, −15.78) and 11.689 at (−9.31, +16.60) | R 30.0 ± 0.1; 45.1° ± 1°; apex 42.51 ± 0.16; OD-G04 ≥ 2.0; pair-B axes ≥ 10.87 | +0.100 (R; pair-B) | (16.78, 135.00, −24.87) | PASS (assumed: A-05, A-12) | A-05, A-12 |
| REQ-04 | (a) φ −60° … +15° in 5° steps: least clearance 11.755, at φ +15°. φ > 0 turns the handle toward +X (verified). (b) φ −50°, dy −15, dz 0 … 200 in 5.0 steps: least clearance 28.689 at dz 50, never inside (the OD-G10 fallback) | (a) ≥ 5.0; (b) interference ≤ 0, read as clearance > 0, not inside | +6.755 (a) | (75.0, 90.4, 40.0), the +X wall's front end | PASS (assumed: A-07) | A-07 |
| REQ-05 | OD-G10 lowest point y 62.296, base top y 10.000: headroom 52.296 | ≥ 50.0 | +2.296 | OD-G10 lowest point | PASS (assumed: A-07) | A-07 |
| REQ-06 | 4 × Ø4.500, offset 0.000, through. The Ø8 driver probes from y 10 to y 300 interfere with the rig by 0.000 mm³ | Ø4.5 ± 0.1; offset ≤ 0.10; interference = 0 | +0.100 | — | PASS (assumed: A-11) | A-11 |
| REQ-07 | The Ø6 probes from y 160 to y 300 on the 4 screw axes interfere with the rig by 0.000 mm³ | = 0 | 0 | — | PASS | — |
| REQ-08 (Soft) | Not geometric. Measured plate section at x 0 (through the hub window, y 135.0 … 160.0): area 1187.48 mm², centroid y 147.500, I 61 848.1 mm⁴, Z 4947.85 mm³ (§4 hand value 4948). σ = 47.4 N·m / Z = 9.58 MPa (hand ≈ 9.6), a factor of 4.18 against ≈ 40 MPa (hand ≈ 4.2) | the bench test | — | plane x 0 | INCONCLUSIVE (Soft, bench; risk low against the hand calculation, A-02) | A-02 |

The check script tags the U-03a and U-03b rows without A-01. Spec §5 lists A-01 for U-03, so this REPORT carries them as PASS (assumed: A-01).

**REQ-08 against the hand numbers.** The measured section matches §4.
- At x 0 the two plate pieces either side of the window are z −60.0 … −30.0 and z +42.50 … +60.0. Together they are 47.50 of the 120 width, 25.0 deep.
- The section area is 1187.48 mm², against 47.5 × 25 = 1187.5.
- Z is 4947.85 mm³ against the hand 4948, and σ is 9.58 MPa against the hand ≈ 9.6.

The bending moment is §4's value; it is not measured. The PLA strength is §4's common printed value and is not sourced (A-02). The head pull-through (τ ≈ 8.5 MPa on 5.0 of plate) rests on the measured 5.000 under each head.

## 4. Robustness sweep (D7)

Each run rebuilds the part at one parameter's low or high value, exports it to `01_CAD/sweep_v02/`, and runs every predicate of `check_od_t01_rig_v02.py` on the re-imported export. That includes the motion checks U-03b and REQ-04 (a) and (b) in full, giving 173 rows per run. Nominal is the delivered export (§3). **All 20 runs built exactly one solid, and every gate passed in every run.** No run gave a FAIL. The only INCONCLUSIVE row is the Soft REQ-08 row.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |
|---|---|---|---|---|
| screw_d | 3.3 · 3.4 · 3.5 | yes | D-04a Ø3.300 (low); REQ-01 Ø at band edge | +0.050; 0.000 |
| cbore_d | 6.4 · 6.5 · 6.6 | yes | REQ-01 Ø6.4 / Ø6.6 at band edge | 0.000 |
| cbore_floor_y | 139.9 · 140.0 · 140.1 | yes | D-01b min_wall 4.900 (low); REQ-01 floor and plate under the head (4.900 / 5.100) at band edge | +2.900; 0.000 |
| screw_xz (radial offset 0.10) | 43.929 · 44.0 · 44.071 per axis | yes | REQ-01 offset 0.100 | −4.6e−7 (in band) |
| window_r | 29.9 · 30.0 · 30.1 | yes | REQ-03 pair-B axis 10.870 (low); apex 42.359 (low), 42.643 (high) | −2e−8 (pair-B, in band); +0.009 (apex, low) |
| theta_roof | 45.05 · 45.1 · 45.14 | yes | D-03a 45.050° (low) | +0.050° |
| bench_d | 4.4 · 4.5 · 4.6 | yes | REQ-06 Ø at band edge | 0.000 |
| plate_y0 (housing pose moved with it) | 134.9 · 135.0 · 135.1 | yes | REQ-05 52.196 (low) | +2.196 |
| wall_x_in | 74.9 · 75.0 · 75.1 | yes | REQ-04 (a) 11.685 at φ +15° (low) | +6.685 |
| depth_z1 | 59.9 · 60.0 · 60.1 | yes | U-02 size_z 119.9 / 120.1 at band edge | 0.000 |

Worst value per gate over all 21 runs (nominal and 20 swept):
- U-03a 5.000 (OD-G04; set by OD-G04, not by any rig parameter)
- U-03b 0.000 mm³; OD-G10 least 13.689
- D-01b 4.900
- D-03a 45.050°
- D-04a 3.300
- REQ-01: offset 0.100; plate under the head 4.900
- REQ-03: pair-B 10.870; apex 42.359
- REQ-04 (a) 11.685
- REQ-04 (b) 28.689
- REQ-05 52.196
- every other gate is in its band at every run

**Two v01 sweep failures are gone:**
- **REQ-03 (REPORT v01 §4 note 2).** Spec 1.3's apex band (± 0.16) now stacks with R ± 0.1. R 29.9 and R 30.1 put the apex at 42.359 and 42.643, both inside 42.35 … 42.67. The pair-B axis reads 10.870 at R 29.9, which is exactly the 1.2 threshold.
- **The D-03a exception-locator rows (REPORT v01 §4 note 1).** The screw_xz low and plate_y0 low runs gave FAIL rows in v01. The locator now uses the measured hole axes and ends (§8), and both runs pass.

## 5. Build facts

- Envelope 240.000 × 160.000 × 120.000 (x ±120, y 0 … 160, z ±60).
- Volume 1 143 747.2 mm³; mass 1418 g at 1240 kg/m³ (PLA, §3, A-08).
- Fillets: none requested. The four inside corners are 10 × 10 45° chamfers in the wall profile (spec §4), census 4 planes. No fillet ladder was run, so there is no achieved radius to report.
- Teardrops are at 45.1° throughout. The window apex measures z +42.501. The counterbore apex is 4.61 and the bench-hole apex 3.19 (design values).
- The plate spans y 135.000 … 160.000 (25.0 thick).
- The counterbores run from y 160.000 to y 140.000 (20.0 deep), leaving 5.000 of plate under each head.
- The walls run z −60.000 … +40.000 (measured). The plate and the base run z −60 … +60.
- Placements are unchanged from v01:
  - **OD-G01 housing.** Its rear-face plane sits on the plate's measured underside (y 135.000), with the spec §2 rotation (housing x → X, y → +Z, z → −Y). The joint is rigid, axis (0, 1, 0) through x 0, z 0. The 4 insert-bore axes measure on the Ø3.4 axes with offset 0.000.
  - **OD-G04.** Rigid with the housing, at the v03 assembly's pose.
  - **OD-G10.** Rigid with the housing at the v03 locked pose. φ is a revolute about (0, 1, 0) through x 0, z 0, and its direction is verified by max_x.
  - Assembly solids are identified by measurement.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity | The rig stands on its 240 × 120 base at y 0, with the housing hung under the 25 thick plate. The brew load pulls the housing down into the four screws, whose heads bear on 5.0 of plate. As printed, the part lies on its rear face as a 120 deep prism with no unsupported island. |
| P2 | Function chains | The load runs from the screw head on 5.0 of plate (x44 section), through the M3 × 10 into the insert in OD-G01, then through the housing lugs and the locked OD-G10 to the blind basket. The plate, the two walls, the base and the bench screws close the ring (z0 and z44 sections). |
| P3 | Motion clearance | The portafilter locks and unlocks over φ −60° … +15° with at least 11.755 to the rig. It goes in and out at φ −50°, 15 low, along +Z through the open front, with at least 28.689. The housing set offers up from 30 below with no interference. |
| P4 | Human factors | The four screw heads sit 20 down their Ø6.5 counterbores, and the hub sits 25 down the R 30 window. The screw axes are clear from above (Ø6 probes from y 160 to 300), so a driver reaches them. The bench-screw axes are clear for a driver (Ø8 to y 300). The handle leaves at the open front. The 52.3 under the portafilter takes a catch tray. Whether the water connection fits down the deeper window is A-05's open question. |
| P5 | Absurdity next to a real product | A 240 × 160 × 120 closed frame of about 1.4 kg PLA holds a 100 × 100 group head. That is a bench press-fixture sized for a 3 kN hydrostatic load: §4 gives a factor of ≈ 4.2, and the measured section gives 4.18. |
| P6 | Floating, embedded, mirrored, upside-down | The housing touches the plate at y 135.000 with zero interference, so it neither floats nor is embedded. The teardrop roofs point to +Z, the build direction (y147 section). The walls end at z +40. The handle is on +X, as in the v03 assembly. Nothing of the rig lies above y 160. |

## 7. Library and tools used

- Cards: none ("nothing matched" was a D1 finding, plan §2).
- `tools.core`: `read_step`, `write_step` (AP242, fixed timestamp 2026-10-03T00:00:00), `write_stl`, `validity`, `solid_count`, `compare_step`.
- `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `min_wall` (with `wide`), `overhang_census(build_dir=(0,0,1))`, `flat_ceiling_spans`, `clearance`, `interference`, `radial_extent`, and `mesh_census` (corroboration only).
- `tools.drawing`: `write_sections`, `nothing_clipped`.
- New job code, in `01_CAD/` only:
  - the pose helper;
  - the D-03a census copy, with the exception locator on the measured holes;
  - the probe cylinders;
  - the REQ-08 section measurement at x 0 (OCP `BRepAlgoAPI_Common` of the plate with the plane x 0, then `BRepGProp` surface properties). It is reported and never gated.
- Missing tools: none.

## 8. Deviations from the plan

- **Spec 1.3 amendments, as briefed (RV01 F1, F2):**
  - plate_y1 goes from 150 to 160, so U-02 size_y and position max_y are now 160.
  - cbore_floor_y goes from 138 to 140. REQ-01 now checks 5.0 ± 0.1 of plate under the head and a counterbore from y 160. The sweep runs cbore_floor_y at 139.9 / 140.1.
  - REQ-03 uses apex ± 0.16 and pair-B ≥ 10.87 (A-12 Ø17.7), from spec 1.2 and 1.3.
  - The REQ-07 probes run y 160 … 300.
  - The window measuring points, the pair-B probe and the flank filter take the plate's measured top and underside instead of fixed y values.
- **D-03a exception locator, a deviation from v01's check.** The locator now accepts the unfilled 0° point against the measured hole axes, radii and ends, within the 0.005 band. In v01 it used the nominal axes and a fixed y window, which gave FAIL rows on correct crowns in two swept runs (REPORT v01 §4 note 1). The gated census, with the holes filled, is unchanged.
- **New REQ-08 rows.** Six rows report the measured section at x 0 against §4's hand numbers, as the brief asks. Their status is REPORTED and they gate nothing.
- **Sections.** The plate section moved from y 142.5 to y 147.5 (mid-plate). An x 0 section was added for REQ-08.
- **Script names.** The v02 scripts carry `_v02` so the v01 scripts stay byte-identical (L-11). A `__pycache__` folder from the imports may exist in `01_CAD/`.
- No other change. Fix cycles used: 0 (no FAIL on the delivered part).

**Delta against v01.**

| Item | v01 (spec 1.1/1.2) | v02 (spec 1.3) |
|---|---|---|
| Plate | y 135 … 150, 15 thick | y 135.000 … 160.000, 25 thick |
| Counterbore floor | y 138.000, 3.000 under the head (M3 × 8) | y 140.000, 5.000 under the head (M3 × 10) |
| Envelope | 240 × 150 × 120 | 240.000 × 160.000 × 120.000 |
| Volume, mass | 959 176.3 mm³, 1189 g | 1 143 747.2 mm³, 1418 g |
| min_wall (D-01a/b, D-06a, U-06) | 3.000 | 5.000 |
| Window section at x 0 (A-02) | hand Z 1781 mm³, σ 26.6 MPa | measured Z 4947.85 mm³, σ 9.58 MPa |
| REQ-03 sweep at R 29.9 / 30.1 | FAIL (apex ± 0.1; pair-B 10.97) | PASS (apex 42.359 / 42.643 in ± 0.16; pair-B 10.870 ≥ 10.87) |
| D-03a locator in the sweep | 2 FAIL rows on correct crowns | 0 |
| Faces, features, motion gates | 41 planar / 13 cylinders; REQ-04 (a) 11.755, (b) 28.689; REQ-05 52.296 | unchanged |
| Check rows | 167 | 173 (6 REQ-08 section rows) |

## 9. What I am least sure of

1. **REQ-03 pair-B at R 29.9 has zero margin.** The pair-B axis-to-window distance is 10.970 at nominal and 10.870 at R 29.9, against a required 10.87. At R 29.9 it passes only inside the 0.005 band. That is by construction, since the threshold is R 29.9 − 19.03. A printed window under R 29.9 would read as non-conforming. The underlying need, a head ≤ Ø17.7 clearing by 2.0, rests on A-12, and no head has been measured.
2. **The D-03a margin is 0.1°, and the exception is excluded by position.** The filled census reads 45.100° (45.050° at the sweep's low θ). The locator now follows the measured holes, but the reviewer should still confirm from the y147 and x44 sections that the Ø3.4 crowns are the only sub-45° faces. Each of the four counterbores, now 20 deep, prints 20 of horizontal teardrop roof.
3. **REQ-08 rests on the hand moment and an unsourced PLA strength.** The measured section confirms §4's geometry (Z 4947.85 against 4948). The moment (simply supported between x ±75, 1.53 kN at x ±44) and the ≈ 40 MPa strength are §4's assumptions (A-02). Separately, OD-G10 is still an unsound solid, so every OD-G10 interference row is the clearance fallback (margins 13.689 and 28.689).

## 10. Stop

Not stopped. Every hard gate is met at nominal and in all 20 swept runs.

```json
{
  "schema": "oguz-report-v1",
  "job_id": "20261002-od-t01-pressure-test-rig",
  "part": "od_t01_rig",
  "tag": "v02",
  "spec_version": "1.3",
  "files": [
    {"path": "01_CAD/build_od_t01_rig_v02.py", "sha256": "537aae6dc66c361343fc6adb99bdc06adbe3f85f5cb417806a4c9a7a60f78b07"},
    {"path": "01_CAD/check_od_t01_rig_v02.py", "sha256": "cc94c52be8f9ddce5b3047e0e34a7ec462c211edd1cd14d2c7be277779dd4c10"},
    {"path": "01_CAD/sweep_od_t01_rig_v02.py", "sha256": "8987669578028c8011287d7804e513e3ab68bc07918c22c20d93a092759d0333"},
    {"path": "01_CAD/sections_od_t01_rig_v02.py", "sha256": "95419cbfa29893ed8bce595fc8833fff1f5bc7770c1c2d70b19832cb64214ef2"},
    {"path": "02_STEP_STL/od_t01_rig_C1_v02.step", "sha256": "18c9de8f013cb7ce84eba3ce104ab6fb01fc84f79f8524140cfadb9d3feaf810"},
    {"path": "02_STEP_STL/od_t01_rig_C1_v02.stl", "sha256": "183e58f0eda9287450d79d1a15aa3a4dabcf694449a6b82ae3a9ef9f24bfbd3f"},
    {"path": "02_STEP_STL/od_t01_assembly_C1_v02.step", "sha256": "c6caa17478e570e0b9200d813ee69fa674d68d2f9d6a91db216f4a5a1f18c072"},
    {"path": "03_Sections/od_t01_rig_v02_z0_assembly.png", "sha256": "7b37fd6df626973922208a3ab41d34c29418313a9028223cf6a7826898dbe96b"},
    {"path": "03_Sections/od_t01_rig_v02_z44_assembly.png", "sha256": "b93398a4d4617a43bebaaf6a8ba366fc9e450b97ad79cc4e571e42efce95cfb7"},
    {"path": "03_Sections/od_t01_rig_v02_x44.png", "sha256": "20f241a6cdc4deef5b6397a1e7d0f2ea11895c2877f000c3cd60b41e9009cb33"},
    {"path": "03_Sections/od_t01_rig_v02_x0.png", "sha256": "4d95cd78d17258d41d1f9b776a85cdfe45ad407591926a06a44c5d43d7cc5e5a"},
    {"path": "03_Sections/od_t01_rig_v02_y5.png", "sha256": "9ea632d7cbf6e3c9c9901269be5b5b54a501dc95b7e20ad5108fc6387a2efd29"},
    {"path": "03_Sections/od_t01_rig_v02_y147.png", "sha256": "0ceb47485189140a97e0728a5c98ded17ff94b60b12e3d2f8ad0c89dd84df4df"},
    {"path": "01_CAD/gates_od_t01_rig_v02.json", "sha256": "8b3fa3372ff4e37126f4cac7adece4f8dd232f140463a828faa59342787b0843"},
    {"path": "01_CAD/check_v02.log", "sha256": "cbe04b062e7ac2acbc3fba7fa9ee9ac9a5a8d63ea1dbea300f03a321d93852dd"},
    {"path": "01_CAD/od_t01_rig_C1_v02.params.json", "sha256": "48449c6f08185de3b6815cb610df5b6ea33c74b1c72431e802aea0ed5d583b38"},
    {"path": "01_CAD/od_t01_rig_C1_v02.mesh.json", "sha256": "9200b2e751b44c8dcb6ed71d484dbffe1d602f6130eb7fc0c9058fe2763b4f9b"},
    {"path": "01_CAD/sections_v02.json", "sha256": "a4e115b277baf082aa398a8b14729e32fb452713ca761381b3df95428569aa07"},
    {"path": "01_CAD/sweep_v02/sweep_index.json", "sha256": "a3ac0412f005312929509524ad393a31e9db5b2dd8cb2c0696fbaadb93490331"},
    {"path": "01_CAD/sweep_v02/sweep_summary.json", "sha256": "1d1070b1d8caed95a33da78b8b6590aedca51dfb8fe279a9731944a513961f92"},
    {"path": "01_CAD/sweep_v02.log", "sha256": "81fb71e05442a716754ac9c8c5692d9ec69a505c5c65e582d563b01baf871798"}
  ],
  "versions": {"python": "3.13.7", "build123d": "0.11.1", "ocp": "7.9.3.1", "repo_commit": "10929db1408d89144bd4af9cad971440427933d0"},
  "gates": [
    {"gate": "exactly_one_solid", "measured": 1, "unit": "count", "required": "== 1", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-01", "measured": "1 / 1 / 0", "unit": "count", "required": "solid_count 1, brep_valid 1, naked_edges 0", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-02", "measured": "240.000 x 160.000 x 120.000", "unit": "mm", "required": "240 x 160 x 120 each +-0.1", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "envelope_within_spec", "measured": "x -120..120, y 0..160, z -60..60", "unit": "mm", "required": "+-0.1", "margin": 0.1, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-03a", "measured": 5.0, "unit": "mm", "required": "contact 0; interference <= 0; elsewhere >= 2.0", "margin": 3.0, "at": "(-21.25, 135.00, 21.18)", "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "U-03b", "measured": 0.0, "unit": "mm3", "required": "interference <= 0 over dy 0..-30 step 2", "margin": 0.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "U-04", "measured": 6.7e-08, "unit": "mm3", "required": "unchanged, named, valid, no stray shells", "margin": -6.7e-08, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-05", "measured": "41 planar, 13 concave cyl, 13 bores, 4 chamfers, 2 walls", "unit": "count", "required": "plan census", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "feature_census", "measured": "as U-05", "unit": "count", "required": "plan census", "margin": 0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-06", "measured": 5.0, "unit": "mm", "required": ">= 2.0 (Soft)", "margin": 3.0, "at": "(-45.10, 135.00, -47.04)", "status": "PASS", "assumes": []},
    {"gate": "U-07", "measured": 0.0050, "unit": "mm", "required": "sagitta <= 0.01; tol 0.01; ang <= 0.1033", "margin": 0.0050, "at": null, "status": "PASS", "assumes": []},
    {"gate": "U-08", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "D-01a", "measured": 5.0, "unit": "mm", "required": ">= 0.8", "margin": 4.2, "at": "(-45.10, 135.00, -47.04)", "status": "PASS", "assumes": []},
    {"gate": "D-01b", "measured": 5.0, "unit": "mm", "required": ">= 2.0", "margin": 3.0, "at": "(-45.10, 135.00, -47.04)", "status": "PASS_ASSUMED", "assumes": ["A-08"]},
    {"gate": "D-02", "measured": "240 x 160 x 120", "unit": "mm", "required": "<= 420 x 420 x 500", "margin": 180.0, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-09"]},
    {"gate": "D-03a", "measured": 45.1, "unit": "deg", "required": ">= 45 (Ø3.4 crowns excepted)", "margin": 0.1, "at": "(21.25, 135.00, 21.18)", "status": "PASS_ASSUMED", "assumes": ["A-10"]},
    {"gate": "D-03b", "measured": 3.4, "unit": "mm", "required": "<= 5; crowns <= 3.4; reviewer row", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-10"]},
    {"gate": "D-04a", "measured": 3.4, "unit": "mm", "required": ">= 3.25 (screw), >= 4.25 (bench 4.5)", "margin": 0.15, "at": null, "status": "PASS", "assumes": []},
    {"gate": "D-06a", "measured": 5.0, "unit": "mm", "required": ">= 1.0", "margin": 4.0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "D-07", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "J-05", "measured": null, "unit": "", "required": "N/A", "margin": null, "at": null, "status": "N/A", "assumes": []},
    {"gate": "REQ-01", "measured": "Ø3.400, offset 0.000, Ø6.500, y 160.000 -> 140.000, under head 5.000", "unit": "mm", "required": "Ø3.4+-0.1; offset <= 0.10; Ø6.5+-0.1; floor 140.00+-0.10; 5.0+-0.1", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "REQ-02", "measured": 135.0, "unit": "mm", "required": "135.00 +-0.10, one plane over x+-50, z+-50", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-01"]},
    {"gate": "REQ-03", "measured": "R 30.000, 45.100 deg, apex 42.501, OD-G04 5.000, pair-B 10.970", "unit": "mm", "required": "R 30.0+-0.1; 45.1+-1; apex 42.51+-0.16; >= 2.0; >= 10.87", "margin": 0.1, "at": "(16.78, 135.00, -24.87)", "status": "PASS_ASSUMED", "assumes": ["A-05", "A-12"]},
    {"gate": "REQ-04", "measured": 11.755, "unit": "mm", "required": "(a) >= 5.0; (b) clearance > 0 not inside (28.689)", "margin": 6.755, "at": "(75.0, 90.4, 40.0)", "status": "PASS_ASSUMED", "assumes": ["A-07"]},
    {"gate": "REQ-05", "measured": 52.296, "unit": "mm", "required": ">= 50.0", "margin": 2.296, "at": "OD-G10 lowest point y 62.296", "status": "PASS_ASSUMED", "assumes": ["A-07"]},
    {"gate": "REQ-06", "measured": "Ø4.500, offset 0.000, probes 0.000 mm3", "unit": "mm", "required": "Ø4.5+-0.1; offset <= 0.10; interference 0", "margin": 0.1, "at": null, "status": "PASS_ASSUMED", "assumes": ["A-11"]},
    {"gate": "REQ-07", "measured": 0.0, "unit": "mm3", "required": "Ø6 probes y 160..300 interference 0", "margin": 0.0, "at": null, "status": "PASS", "assumes": []},
    {"gate": "REQ-08", "measured": "Z 4947.85 mm3, sigma 9.58 MPa, factor 4.18", "unit": "-", "required": "Soft, bench", "margin": null, "at": "plane x 0", "status": "INCONCLUSIVE", "assumes": ["A-02"]}
  ],
  "sweep": [
    {"parameter": "screw_d", "values": [3.3, 3.4, 3.5], "all_built": true, "worst_gate": "D-04a / REQ-01", "worst_margin": 0.0},
    {"parameter": "cbore_d", "values": [6.4, 6.5, 6.6], "all_built": true, "worst_gate": "REQ-01", "worst_margin": 0.0},
    {"parameter": "cbore_floor_y", "values": [139.9, 140.0, 140.1], "all_built": true, "worst_gate": "REQ-01", "worst_margin": 0.0},
    {"parameter": "screw_xz_radial", "values": [43.929, 44.0, 44.071], "all_built": true, "worst_gate": "REQ-01 offset", "worst_margin": -4.6e-07},
    {"parameter": "window_r", "values": [29.9, 30.0, 30.1], "all_built": true, "worst_gate": "REQ-03 pair-B", "worst_margin": -2e-08},
    {"parameter": "theta_roof", "values": [45.05, 45.1, 45.14], "all_built": true, "worst_gate": "D-03a", "worst_margin": 0.05},
    {"parameter": "bench_d", "values": [4.4, 4.5, 4.6], "all_built": true, "worst_gate": "REQ-06", "worst_margin": 0.0},
    {"parameter": "plate_y0", "values": [134.9, 135.0, 135.1], "all_built": true, "worst_gate": "REQ-05", "worst_margin": 2.196},
    {"parameter": "wall_x_in", "values": [74.9, 75.0, 75.1], "all_built": true, "worst_gate": "REQ-04 (a)", "worst_margin": 6.685},
    {"parameter": "depth_z1", "values": [59.9, 60.0, 60.1], "all_built": true, "worst_gate": "U-02", "worst_margin": 0.0}
  ],
  "least_sure": [
    "REQ-03 pair-B axis distance is exactly at the 10.87 threshold at R 29.9 (A-12 head unmeasured)",
    "D-03a margin 0.1 deg; Ø3.4 crowns excluded by position (reviewer to confirm from sections)",
    "REQ-08 rests on the hand moment and an unsourced PLA strength (A-02); OD-G10 rows are the clearance fallback"
  ],
  "stopped": false
}
```
