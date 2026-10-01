# RV01 — od_c05_carrier_v01 (20260930-od-c05-group-head-carrier) — 2026-09-30 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with the WP-03 amendments) · report `01_CAD/REPORT_od_c05_carrier_v01.md`

**VERDICT: REVISE**
Blocking findings: 1 (F1, plausibility P1 / P5) · open assumptions relied on: A-01, A-03, A-04, A-05, A-06, A-07, A-08, A-09, A-13

Every §5 row was re-measured from the exported STEP (and the STL / 3MF) with my own scripts in `reviews/RV01_work/`. The band is GATES §0 (0.005 mm, 0.001°, 0.001 mm³, 0 for counts). All hard rows PASS or PASS (assumed). D-03a is settled by the analytic face angle at 45.000°. The build blocks on §P only: the spec frame hangs the group head with its axis horizontal (F1). No CAD code was read.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c05_carrier_C1_v01.step` | 3555600be58771b0efba7b2f2b5a48439bb442db58d5b5eb92fdd6a6fe410362 | yes |
| `02_STEP_STL/od_c05_assembly_C1_v01.step` | b6fdbea9466703e81d63938840ce82853cddcac9c4f537d7e5d721f55817e1c3 | yes |
| `02_STEP_STL/od_c05_carrier_C1_v01.stl` | aee6d05a1573742d131cb949e86b98acceb6fca179dc2cd46394a4918c8fe48a | yes (also byte-identical to my own re-mesh of the STEP at 0.01 mm / 0.20 rad) |
| `02_STEP_STL/od_c05_carrier_C1_v01.3mf` | f9d795230b0e3269a107513fa79d7507fcec1dda591edbc0e21b5edb90edc15a | yes (the ledger's hash; same triangle set as the STL) |
| `01_CAD/REPORT_od_c05_carrier_v01.md` | 6f730d02d7f9fa1fcee9826332e42473b2408e2a86c1b1e7f5a544362a305356 | yes (brief) |
| `01_CAD/DESIGN_PLAN.md` | 41b80f841cb6ee700fe5dc7590b8b1db5403458e469af64b5673cf5f0232eced | yes |
| `01_CAD/check_od_c05_carrier_v01.json` | 1c57b36c81835e0774266f800d9c3d333f0e66638e2d4bbcbf7ca2105866e03d | yes |
| `01_CAD/build_od_c05_carrier_v01.json` | d3457f40ea3fcf9a7d10e3ae7f1ca808c85d1f6dabbeb4a2917994211bd75102 | yes |
| `01_CAD/sections_od_c05_carrier_v01.json` | 298b88918bd3cc23b4e1d8a25083b5d7591753fa30ca7d2a21fcd9f9d2c7f8bc | yes |
| `01_CAD/sweep_v01/SHA256SUMS_v01.txt` | 2cbc6e99df38bb23293aa1e11ff4d629748c4a97060ac7eea4453f29fb1805ca | yes |
| `03_Sections/od_c05_assembly_x0_v01_left.png` | 45c952415736c7a6bdad835d995b0f4f21af525050efb8a02efac15f14e57ecf | yes |
| `03_Sections/od_c05_carrier_x0_v01_left.png` | ff005505cf4bffe0b1fe8002cbaea64f9961c2a69184a484a0d6a1e25b9a13dd | yes |
| `03_Sections/od_c05_carrier_x35_v01_left.png` | edf5390642a14c4dd97241fd525ae097c3ad1305768cdb093727a3c0eab477c8 | yes |
| `03_Sections/od_c05_carrier_x44_v01_left.png` | 7972feb30a6f1a93646deca2bfe23305cc489a611111c9b6e3650f34375062d7 | yes |
| `03_Sections/od_c05_carrier_x48_v01_left.png` | 7d95e4c21d402ead81af662b28df7eea4e04ca042f7f0061b88683c8584e762c | yes |
| `03_Sections/od_c05_carrier_y44_v01_front.png` | 400b0fbacba5c85ebc25ca1aecfeaa2fa5ee024be96bbc49e77ea8eb8fefdbfe | yes |
| `03_Sections/od_c05_carrier_ym110_v01_front.png` | 537c6d019dd9ff66a5758ad7a169dd3a47c903e395f3bf67883901129cd82dec | yes |
| `03_Sections/od_c05_carrier_zm27p44_v01_top.png` | 49e475ca672c694dab36d477b1545de225eb4103a352b13575cf50d62f827d83 | yes |
| `00_Spec/inputs/OD-G01_housing_C1_v02.step` | f8865cd194bbd655a93944637923b4f5aa155487df5cf9777c368d0cd4407b02 | yes (input) |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | yes (input) |

The submission is complete: every §5 row is answered in the REPORT, and every listed file is present with a matching hash.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 | 1 / 1 / 0 | 0 | whole part; 0 loose shells or faces | PASS | `validity` | — |
| U-02 | 100.000 × 225.000 × 45.000 mm | each ± 0.1 | +0.100 each | x −50.000 … 50.000, y −175.000 … 50.000, z −69.940 … −24.940 | PASS | `envelope` | — |
| U-03 | carrier\|OD-G01: clearance 0.000 mm, interference 0.000 mm³, hole-to-insert offsets 0.000 mm; carrier\|OD-G04: clearance 5.000 mm, interference 0.000 mm³ | contact = 0, ≤ 0 mm³, ≤ 0.10; ≥ 2.0 | 0 (contact); +0.100 (offsets); +3.000 (OD-G04) | contact at (−50.0, −42.0, −24.94); OD-G04 nearest points (−21.2132, 21.2132, −24.94) on the carrier and (−21.2132, 21.2132, −19.94) on OD-G04. Path: housing offered along −Z from 30 mm to the seat, interference 0 at every step. The delivered assembly STEP matches my own placement (carrier and OD-G04 common volume equal to their volume; housing: same envelope and centroid) | PASS (assumed: A-01, A-06) | `clearance`, `interference`, `bore_census` + `locate_bore` on both solids | A-01, A-06 |
| U-03 (b) | — | N/A by its row (no motion) | — | — | covered by U-03 | — | — |
| U-04 | label `od_c05_carrier`, AP242, 1 solid; `step_roundtrip` volume delta 2.3e-10 mm³, faces delta 0, valid after 1 | re-read unchanged, no stray shells, valid | 0 | — | PASS | `read_step`, `step_roundtrip` | — |
| U-05 | 20 planar, 16 cyl. (14 concave, 2 convex R 6.000), 14 bores; all 12 holes located | plan §3 as amended | 0 | §3 below | PASS | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 (Soft) | 2.750 mm | ≥ 2.0 | +0.750 | (50.000, 44.006, −28.361), counterbore web | PASS | `min_wall` detail["wide"] | — |
| U-07 | sagitta / deviation 0.00498 mm; 4264 triangles; 1 body, 0 naked edges, winding 1; STL volume 108716.928 mm³ (B-rep 108712.078); 3MF 4264 triangles, same triangle set, 108716.928 mm³, unit mm | tol 0.01, angular ≤ 0.2310 rad (0.20 used), sagitta ≤ 0.01, 3MF same mesh | +0.00502 | (24.655, −105.861, −27.44), lower window arc | PASS | `write_stl` (my re-mesh is byte-identical), `mesh_sagitta`, `mesh_census`, `mesh_deviation`, 3MF parse | — |
| U-08 | — | threaded parts only | — | — | N/A: no threads, by its row | — | — |
| D-01a | 2.750 mm | ≥ 0.8 | +1.950 | (50.000, 44.006, −28.361) | PASS | `min_wall` | — |
| D-01b | 2.750 mm (STL 2.746 ≥ 2.750 − 0.010) | ≥ 2.0 | +0.750 | same | PASS | `min_wall`, `min_wall_mesh` | — |
| D-02 | 225.0 tall; 100.0 × 45.0 on the bed | ≤ 250; ≤ 220 × 220 | +25.0 (height) | foot down | PASS (assumed: A-08) | `envelope` | A-08 |
| D-03a | least outside the exception 44.99999999997° | ≥ 45° | −3.3e-11 (inside the 0.001° band) | window arcs at their gable tangent lines, (17.6777, −92.3223) and (21.2132, 21.2132); gables 45.000000° | PASS (assumed: A-13) | analytic angle per B-rep face; sections z −27.44, −28.94; `overhang_census` on the part with the eight crowns plugged (INCONCLUSIVE 45.0000, 0 samples under 45) | A-13 |
| D-03b | widest crown 6.500 mm (named exception); outside it 0 mm | ≤ 5; crowns ≤ 6.6 | +0.100 | counterbores (±44, ±44, −29.94 … −27.94) | PASS | bridge span from the downward-face list and sections | — |
| D-04a | 3.400 mm (all eight) | ≥ 3.25 | +0.150 | Z holes (±44, ±44); Y holes (±35, z −40 / −60) | PASS | `locate_bore` | — |
| D-06a | 2.750 mm | ≥ 1.0 | +1.750 | (50.000, 44.006, −28.361) | PASS | `min_wall` | — |
| D-07 | — | fit bores only | — | — | N/A: clearance holes only, by its row | — | — |
| E-06 | 2 gussets, each 3200.000 mm³ (full 40 × 40 triangle, 4 thick), fused into the one solid; no boss | tied to the foot, no free boss | 0 | x ±46 … ±50, y −171 … −131, z −69.94 … −29.94 | PASS | `common_volume` with the gusset boxes; sections x 0, ±48 | — |
| REQ-01 | Ø3.400, through, 3.000 long; offset 0.000 from nominal and from the OD-G01 inserts (Ø4.000 × 5.700, z −24.94 … −19.24) | Ø3.4 ± 0.1, ≤ 0.10 | +0.100 | (±44, ±44) | PASS (assumed: A-01) | `bore_census` + `locate_bore` on both solids | A-01 |
| REQ-02 | Ø6.500, 2.000 deep, open at z −29.940, coaxial 0.000 | Ø6.5 ± 0.1, 2.0 ± 0.1 | +0.100 | (±44, ±44) | PASS (assumed: A-09) | `bore_census`, `locate_bore`; section z −28.94 | A-09 |
| REQ-03 | front z −24.940 (max_z); rear z −29.940 (counterbore starts); 3.000 + 2.000 = 5.000 | ± 0.10 | +0.100 | — | PASS (assumed: A-01) | `envelope`, `locate_bore` | A-01 |
| REQ-04 | innermost material 30.000 mm over 36 angles × 5 depths | r ≤ 30.0 empty | −7e-15 (inside band) | θ 10°, z −29.9; θ 90° first material 42.426 (apex) | PASS (assumed: A-06) | `radial_extent`, whole ray | A-06 |
| REQ-05 | underside y −175.000; foot 4.000 thick | ± 0.10; 4.0 ± 0.1 | +0.100 | Y holes y −175 … −171 | PASS (assumed: A-03, A-04) | `envelope`, `locate_bore` | A-03, A-04 |
| REQ-06 | Ø3.400 through, offset 0.000 (all four) | Ø3.4 ± 0.1, ≤ 0.10 | +0.100 | (±35, z −40 / −60) | PASS (assumed: A-04) | `bore_census` + `locate_bore` | A-04 |
| REQ-07 | min_z −69.940 | ≥ −70.0 | +0.060 | foot rear edge | PASS (assumed: A-05) | `envelope` | A-05 |
| REQ-08 | innermost material about (0, −110) 25.000 mm; apex 35.355; below y −50 the sections show no other opening | R 25 empty, nothing else missing | −1.8e-14 (inside band) | θ 250°, z −29.9 | PASS (assumed: A-07) | `radial_extent` whole ray; sections z −27.44, −28.94 | A-07 |
| REQ-09 (Soft) | — | no visible flex (bench) | — | — | INCONCLUSIVE (Soft bench gate; risk MEDIUM, F2) | bench, first print | A-11 |

**D-03a, settled by my own method.** The brief asked for a reading of each window arc at its gable junction. My list of every downward face from the B-rep uses plane normals, and each cylinder's normal at its u bounds and at its interior extremum. It found 15 downward faces:
- the bed face (y −175, left out as the bed);
- four gable planes, each 45.000000°;
- the two window arcs, R 30 and R 25, whose least lies on their u-bound edge, the tangent line: 44.99999999997°, which is 45° within the band;
- eight cylinders under 45°. These are exactly the 4 × R 1.7 and 4 × R 3.25 crowns along Z at (±44, ±44), the named exception, with a least of 0.0°.

In section z −27.44, each arc's end tangent (0.707107, ∓0.707107) is parallel to its gable line, so the junction is smooth at exactly 45°. The sections x 0 and z −27.44 (PNG) show the same thing.

`overhang_census`, run on the part with only those eight crowns plugged (a closed solid, independent of the designer's open-shell helper), reads the same INCONCLUSIVE: 45.0000° against a bound of 0.009°, with 0 samples under 45°.

**D-03b.** Only the crowns bridge: the Ø6.500 counterbores are 2.0 deep and the Ø3.400 holes 3.0 deep. Both are ≤ 6.6 under spec 1.2's exception. Nothing else faces down at less than 45°.

**A-09 screw arithmetic.** An M3 × 8 passes 3.000 of wall under the Ø6.5 × 2.0 counterbore, which leaves 5.0 in the insert bore. That bore is 5.700 deep (z −24.94 … −19.24), so the tip stops at z −19.94, 0.70 short of the bore's end.
- ISO 7380 head (Ø5.7, 1.65 high): 0.40 radial clearance, and the head sits 0.35 below the rear face.
- DIN 912 head (Ø5.5, 3.0 high): stands 1.0 proud, at z −30.94, still 54 from the z −85 zone.

The arithmetic holds.

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 wall, R 6 top corners about (±44, 44) | z −29.94 … −24.94, x ±50, y −175 … 50; 2 convex R 6 | front −24.940, rear −29.940; 2 convex R 6.000 arcs centred (±44.0, 44.0) | PASS |
| F02 foot | y −175 … −171, x ±50, z −69.94 … −24.94 | min_y −175.000, min_z −69.940, Y holes 4.000 long | PASS |
| F03 gussets ×2 | 4 thick at x ±46 … ±50, legs 40 | 3200.000 mm³ each (= 4 × 40 × 40 / 2) | PASS |
| F04 hub window | R 30 about (0, 0), 45° gable, apex y 42.43 | bore Ø60.000, 270°, through; gables (21.2132, 21.2132) → (0, 42.4264) at 45.000000°, tangent | PASS |
| F05 lower window | R 25 about (0, −110), 45° gable, apex y −74.64 | bore Ø50.000 about (0, −110), 270°, through; gables to (0, −74.6447) at 45.000000°, tangent | PASS |
| F06 Z holes ×4 | Ø3.4 through at (±44, ±44) | 4 × Ø3.400, through, offset 0.000 | PASS |
| F07 counterbores ×4 | Ø6.5 × 2.0 from z −29.94 | 4 × Ø6.500 × 2.000, offset 0.000 | PASS |
| F08 Y holes ×4 | Ø3.4 through at (±35, z −40 / −60) | 4 × Ø3.400 × 4.000, through, offset 0.000 | PASS |
| F09 totals | 20 planar, 16 cyl. (14 / 2), 14 bores, 1 solid | 20 / 16 / 14 / 2 / 14, 1 solid, no other kind | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity: does every part rest and mount the way the product is used? | The carrier stands correctly on its foot. But the spec frame (+Y up, with +Z, the group head axis toward the mouth, horizontal toward the user) hangs the group head on its side. An espresso group head needs its axis vertical with the mouth down, so the grounds stay in the basket and the brew runs down into the mug. See F1 | NO |
| P2 | Function chains connected and aimed? | The hub window (innermost r 30.000) clears the housing's openings (r ≤ 20.93) and OD-G04 (5.000). The lower window is open for TUBE 7 and a hand. The screws are coaxial with the inserts (0.000) | YES |
| P3 | Moving parts oriented for their motion, with clearance? | The carrier has no motion, and nothing of it lies in front of z −24.94, where the portafilter turns. The housing seats along −Z with interference 0 over the whole path | YES |
| P4 | Human factors: grip, reach, insertion direction obvious? | Housing screws go in along +Z from behind, with 55 mm of free space to the z −85 zone for a key. Foot screws go in along −Y from above | YES |
| P5 | Next to a comparable real product, does anything look absurd? | Yes: next to the De'Longhi Dedica the project copies, a group head mounted on its side with a horizontal portafilter is absurd. Same cause as P1 (F1) | NO |
| P6 | Nothing floating, embedded, mirrored, or upside-down? | One solid, interference 0 with both neighbours. The counterbores face away from the housing and the gables point up the print direction. The 90° turn of the whole layout is P1 | YES |

## 5. Positive controls

Mutants are my own and were cut from the exported STEP (`reviews/RV01_work/m5_controls.py`, `mutants/`).

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` (U-01) | front face removed: open shell (naked 6, solids 0) | FAIL |
| `envelope` (U-02, REQ-07, D-02) | foot rear edge to z −71.0 (size_z 46.06, min_z −71.0); wall raised to 255 tall | FAIL |
| `compare_step` / `step_roundtrip` (U-04) | the file against a shape with hole (+44, +44) moved 0.5: volume delta 168.7 mm³ | FAIL |
| `feature_census` (U-05) | counterbore (+44, −44) filled: 13 bores | FAIL |
| `bore_census` + `locate_bore` (U-05, REQ-01/02/06, D-04a) | hole (+44, +44) moved 0.5 (offset 0.500); counterbore filled (finds Ø3.4); foot hole Ø3.2 | FAIL |
| `min_wall` incl. wide (D-01a/b, D-06a, U-06) | counterbore (+44, +44) enlarged to Ø10.6: web 0.700 | FAIL |
| analytic face angle (D-03a) | R 6 teardrop at (0, −40) with a tangent 44.0° gable: 44.000°; plain Ø6 hole: 0.000° | FAIL |
| `overhang_census` (D-03a corroboration) | the 44.0° teardrop, crowns plugged: 44.000° | FAIL |
| bridge span (D-03b) | plain Ø6 hole along Z at (0, −40): 6.0 > 5 | FAIL |
| `radial_extent`, whole ray, innermost (REQ-04, REQ-08) | 4 × 5 bars into the windows to r 26 and r 21 | FAIL |
| `radial_extent`, bounded r ≤ window (the plan's reading) | the same bars read "crossing the bound", INCONCLUSIVE like the nominal "no material"; not used for the gates (F4) | INCONCLUSIVE |
| `interference` (U-03) | carrier moved +3.1 along Z: 21301.8 mm³ with OD-G01 | FAIL |
| `clearance` (U-03) | +3.1 along Z: 1.900 to OD-G04; −0.5 along Z: contact 0.500 ≠ 0 | FAIL |
| gusset `common_volume` (E-06) | both gussets removed: 0 mm³ | FAIL |
| `mesh_sagitta` / `mesh_deviation` (U-07) | STL meshed at 0.1 mm / 0.5 rad: 0.0495 | FAIL |
| `mesh_census` (U-07) | delivered STL with one triangle dropped: 3 naked edges | FAIL |
| 3MF / STL triangle comparison (U-07) | coarse STL, 1708 triangles, against the 3MF's 4264 | FAIL |

Known-good check of the analytic angle: an R 6 teardrop with a tangent 45.0° gable reads 44.99999999997°, the same as the nominal arcs.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | P1 (and P5) | PLAUSIBILITY_NO | group head axis horizontal → vertical, mouth (+Z) down | — | spec 1.2 §2 frame and A-02: +Y up, +Z horizontal toward the user | yes | HIGH | With the axis horizontal, the basket stands on its side: dry grounds fall out on insertion and the brew leaves sideways, not into a mug under it. The carrier is built exactly to this frame, so the part fits the spec and not the machine | The Usta settles the machine's up direction first (A-02). In the Dedica, −Z is up with the mouth down, which puts the thermoblock above the housing along −Z. Then re-concept the carrier for a vertical axis, for example the flange hung under a horizontal plate or bracket with the hub window above. Re-derive A-03 (mug height) from the portafilter spouts |
| F2 | REQ-09 | OBSERVATION | — → no visible flex (Soft, bench) | — | wall y −131 … +44, between the gusset tops and the housing screws | no | MEDIUM | Soft bench gate, INCONCLUSIVE. Hand estimate: a 50 N sideways handle force about 45 mm in front of the wall twists the open 5 mm wall about Y (J ≈ 2000–4000 mm⁴ over ≈ 130 mm, G ≈ 0.75 GPa). That is several degrees, so visible flex is plausible. The locking torque about Z is in-plane and stiff | Bench the first print. If it flexes, close the section (edge flanges or ribs up to the housing screws, or a thicker wall), which is a spec change |
| F3 | D-03a | OBSERVATION | 44.99999999997° → ≥ 45° | −3.3e-11 (inside band) | window arcs at their tangent lines | no | LOW | `overhang_census` cannot close a curved face tangent at exactly 45°, by design. The row was settled by the analytic angle, and its controls FAIL at 44°. The roofs print as true 45° | Tools: evaluate analytic cylinders exactly at their boundary edges in `overhang_census` |
| F4 | REQ-04, REQ-08 | OBSERVATION | 30.000 / 25.000 → r ≤ 30 / 25 empty | ≈ 0 (inside band) | both windows | no | LOW | The plan's bounded-ray reading ("no material" INCONCLUSIVE taken as the expected result) cannot fail: a bar in the window reads "crossing", also INCONCLUSIVE. Gated here on the innermost radius over the whole ray, which FAILs on the bar | Check scripts: gate the innermost material radius over the whole ray (≥ 30.0, ≥ 25.0) |
| F5 | U-02 (appearance) | OBSERVATION | corners 0.83 outside the housing outline → none stated | — | diagonal: carrier (48.24, 48.24) against housing (47.66, 47.66) | no | LOW | The R 6 corners about (±44, 44), accepted in spec 1.1 K-1, stand 0.83 outside the housing's R 8 corners. This is a visible step only; no fit depends on it | None needed; the Usta may confirm the look |

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1 D-03a INCONCLUSIVE | Settled. The analytic angle of both arcs at their tangent lines is 44.99999999997° (inside the 0.001° band), and their section tangents are parallel to the 45.000000° gables. D-03a PASS (assumed: A-13); the controls FAIL at 44°. The tool's limitation stays open (F3). |
| 2 D-03b at the Ø6.6 rung | Spec 1.2 reads ≤ 6.6. The delivered crowns are Ø6.500 (margin +0.100), and a Ø6.6 rung would sit on the limit. Nothing else bridges. |
| 3 Face-exclusion helper; printing | Confirmed independently: exactly eight faces off the bed are under 45°, the R 1.7 and R 3.25 cylinders along Z at (±44, ±44). The plugged closed solid reads the same INCONCLUSIVE 45.0000° with 0 samples under 45°. Warping of the 225 × 5 wall and flex under load are left for the first print (REQ-09, F2). |
