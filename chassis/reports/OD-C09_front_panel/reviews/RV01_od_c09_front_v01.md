# RV01 — od_c09_front_v01 (20261002-od-c09-front-panel) — 2026-10-03 UTC

Reviewer: Claude Code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.1 · plan `01_CAD/DESIGN_PLAN.md` · report `01_CAD/REPORT_od_c09_front_v01.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-02, A-03, A-04, A-05, A-06, A-07, A-09, A-10, A-11, A-13, A-14

Completeness: every §5 row is answered in the REPORT, every listed file is present, and every SHA-256 in the brief matches its file (spec 6aaf9a01…, plan 277daf91…, REPORT 4111981b…, WP-03 4d4f43ed…, all seven input STEPs). Bands used (the plan's GATES §0 bands, through `tools.result.gate`): 0.005 mm, 0.001 mm³, 0.001°, 0 for counts. The reference solids were placed by my own code (`reviews/RV01_work/common.py`) from spec §2, never from the designer's assembly. OD-C01 and OD-C10 are at the identity. OD-C05 and the three OD-G01 solids use the housing pose. Inside the OD-G01 assembly, the housing was identified by volume against the housing-alone file (90 216.79 mm³ both), OD-G10 as the remaining solid with the largest max Z (182.083, 137 692 mm³), and OD-G04 as the third (17 086 mm³). OD-E02 uses the board pose. OD-G10 and OD-E02 read `brep_valid` 0 (the panel, OD-C01, OD-C05, OD-C10, the housing and OD-G04 read 1), so every interference row with them uses the §5 `clearance` fallback. No CAD script of the designer was read.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c09_front_C1_v01.step` | 0d688d24b7954e959291b171fa6e464dd30834e3f737eb73b696dfc992148ab5 | yes |
| `02_STEP_STL/od_c09_front_C1_v01.stl` | 086c7c7e4f1c98472b1800dfce3bf73e83ef240311986df454bd2e1a7c740498 | yes |
| `02_STEP_STL/od_c09_assembly_C1_v01.step` | e451a3854cb1dd22d29c9ba8871367f3be17341e9e3c06fecdffc3701406984c | yes (hashed only; every assembly row was measured on my own placement) |

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0 (loose shells 0, loose faces 0) | 1, 1, 0 | 0 | — | PASS | `validity` | — |
| U-02 | 232.000 × 215.000 × 25.000 mm; position x −116.000 … +116.000, y 0.000 … 215.000, z +72.000 … +97.000 | each spec ± 0.1 | +0.100 | — | PASS | `envelope` | — |
| U-03 | (a) contacts: wall foot 0.0000, flange L 0.0000, flange R 0.0000 to OD-C01; OD-C10 skirt 0.0000 at (110, 215, 97); boss ends 0.0001 / 0.0001 to OD-E02 (panel moved +0.001 / +0.005 along Z reads 0.0011 / 0.0051, not inside). Sound pairs (15, panel and references): 0.000 mm³ each. Fallback pairs (13 with OD-G10 or OD-E02): clearance > 0 and not inside, least panel-OD-G10 14.021, OD-G10-housing 3.6e-15 (reference pair, F4). Footprint to the plate edge and R10 arcs 0.780 at (−116, 0, 97); flanges to OD-C01 holes 4.300, wall foot 2.300, flange-hole centres 19.849; panel to OD-C05 12.000, housing 8.776, OD-G04 18.053; OD-C15 keep-outs 0.000 / 0.000 mm³ (touch at z 94). (b) lowered from +40 in 21 steps of 2.0: OD-C01, OD-C05, housing, OD-G04 0.000 mm³ at every step, least side gap 2.000 to OD-C05 and to the housing; OD-G10 ≥ 14.021, never inside | contacts = 0; ≤ 0 mm³; ≥ 0.5; ≥ 3.0 / 2.0 / 6.0; ≥ 2.0; keep-outs ≤ 0; (b) ≤ 0 every step | −0.0001 (contact, inside band) | boss end (−93.217, 122.219, 85.485); others in the row | PASS (assumed: A-01, A-02, A-03, A-05, A-07) | `clearance`, `interference` / `common_volume`, `bore_census`, `envelope` | A-01, A-02, A-03, A-05, A-07 |
| U-04 | the delivered STEP re-read: AP242, 1 solid, label `od_c09_front`, valid; a fresh write of the re-read solid into `RV01_work/` and back: volume delta 5.5e-10 mm³, faces delta 0, labels equal, valid after 1 | per row | 0 | — | PASS | `compare_step`, `step_roundtrip` | — |
| U-05 | all plan features present (§3): 9 bores (4 Ø3.4 along Y through, 3 Ø15.0 along Z through, 2 Ø4.0 blind along Z), 2 convex Ø11.0 cylinders, 2 concave relief arcs r 8.590 / 8.691; 40 plane + 13 cylinder faces | plan counts | 0 | — | PASS | `feature_census`, `bore_census`, `locate_bore`, point classification | — |
| U-06 (Soft) | `min_wall` wide 3.000 mm | ≥ 2.0 | +1.000 | (−115.776, 0.224, 97.0) | PASS | `min_wall_wide` (spacing 0.45) | — |
| U-07 | sagitta 0.00489 mm; a fresh `write_stl` of the re-read STEP at 0.01 mm / 0.15 rad is byte-identical to the delivered STL (3932 triangles); 0.15 ≤ 4·acos(1 − 0.01/8.6907) = 0.1919 rad (R_max 8.6907, the B3 relief); STL to B-rep deviation 0.00489; one closed shell (bodies 1, naked 0, winding 1); mesh volume 95 755.62 against B-rep 95 755.14 mm³; `min_wall_mesh` 3.000 against B-rep 3.000. The 3MF is written at J5 | ≤ 0.01 | +0.00511 | (−86.987, 168.392, 95.5) | PASS | `write_stl`, `mesh_sagitta`, `mesh_census`, `mesh_deviation`, `min_wall_mesh` | — |
| U-08 | — | threads cosmetic | — | — | N/A: the row applies to threaded parts; this target has none | — | — |
| D-01a | 3.000 mm | ≥ 0.8 | +2.200 | (−115.776, 0.224, 97.0) | PASS | `min_wall` (spacing 0.45) | — |
| D-01b | 3.000 mm | ≥ 2.0 | +1.000 | (−115.776, 0.224, 97.0) | PASS (assumed: A-11) | `min_wall` | A-11 |
| D-02 | 232.0 × 215.0 on the bed, 25.0 tall | ≤ 420 × 420 × 500 | +188.0 | — | PASS (assumed: A-10) | `envelope` | A-10 |
| D-03a | 90.0° with the four flange-hole crowns plugged (no downward face off the bed); unplugged, the least is 0.0° at (−95.0, 4.0, 75.3), only on the four Ø3.4 crowns (the named exception) | ≥ 45° | +45.0 | — | PASS (assumed: A-09) | `overhang_census(build_dir=(0,0,-1))` | A-09 |
| D-03b | the Ø3.4 hole bridges 3.400 mm (census and section `rv_y2`); `flat_ceiling_spans` 0.000 on the part, plugged or not | ≤ 5 | +1.600 | (±85 / ±95, 0 … 4, 77) | PASS (assumed: A-09) | sections; `flat_ceiling_spans` | A-09 |
| D-04a | 4 × Ø3.400 mm | ≥ 3.25 | +0.150 | (±85 / ±95, 0, 77) | PASS | `bore_census`, `locate_bore` | — |
| D-05a | material across each insert bore: upper 10.550, lower 10.788 mm (least of r(θ) + r(θ + 180°), every 2°, 24 levels) | ≥ 8.0 | +2.550 | upper boss, 104° / 284°, 0.125 from the end | PASS (assumed: A-03) | `radial_profile`, `bore_census` | A-03 |
| D-05b | both bores Ø4.000, depth 6.000 (z 85.485 … 91.485), blind (open at the end face only) | Ø 4.0 ± 0.05; 6.0 ± 0.1 | +0.050 | (−91.056, 153.235) and (−90.999, 127.252) | PASS (assumed: A-03) | `bore_census`, `locate_bore` | A-03 |
| D-06a | 3.000 mm | ≥ 1.0 | +2.000 | (−115.776, 0.224, 97.0) | PASS | `min_wall` | — |
| D-07 | — | none | — | — | N/A: the row names no fit-critical bore on this target | — | — |
| J-05 | wall around the insert bore: upper 3.049, lower 3.287 mm (both at the collar reliefs; refined 0.05° × 0.1 mm); `min_wall` over the part 3.000 | ≥ 3.0 | +0.049 | (−92.208, 158.151, 85.535) | PASS | `radial_profile`; `min_wall` corroborates | — |
| E-01 | each boss from 0.5 in front of its end face 0.5000 / 0.5000 (also at end + 2.0: 0.5000 / 0.5000, the collar reliefs); panel without its bosses to OD-E02 1.136, not inside | ≥ 0.5 | −4e-13 (inside band) | (−90.573, 158.714, 85.985); 1.136 at (−94.678, 146.037, 94.0) | PASS (assumed: A-03) | `clearance` | A-03 |
| E-05 | insert-bore axis to posed board-hole axis 0.0000 / 0.0000 mm (board holes Ø3.538 at (−91.0555, 153.2349), Ø3.441 at (−90.9987, 127.2515)) | ≤ 0.10 | +0.100 | — | PASS (assumed: A-03) | `bore_census` of the posed OD-E02, `locate_bore` | A-03 |
| E-06 | 6 of 6 ties: both bosses run from the wall's inner face to z 85.485 as one with the wall (`rv_xm91`, `rv_y153`, `rv_y127`); each flange carries two gussets on wall and flange (`rv_x80`, `rv_x102`, `rv_xm78`, `rv_z89`); point probes IN in all four gussets and both bosses | each boss on and tied to the wall; two gussets per flange | 0 | — | PASS | reviewer, from my own sections (`write_sections`) | — |
| REQ-01 | 4 holes Ø3.400, offset 0.000, length 4.000, through; every −Y face at y 0.000 (envelope min y −3.8e-16) | Ø3.4 ± 0.1; ≤ 0.10; 4.0 ± 0.1; y 0 ± 0.10 | +0.100 | (±85 / ±95, 0, 77) | PASS (assumed: A-01) | `locate_bore`, `envelope` | A-01 |
| REQ-02 | outer 97.000 and inner 94.000 at (−100, 100), (100, 100), (−100, 200), (0, 200), (100, 200), (±110, 30); x ±116.000; top 215.000 | ± 0.10 | +0.100 | — | PASS (assumed: A-02) | `radial_extent` line probes, `envelope`, sections | A-02 |
| REQ-03 | edges at z 95.5 (exact section): slot x −75.000 / +75.000, top 50.000; window x −57.500 / +75.000, top 188.000; the shrunk boxes ∩ panel 0.000 / 0.000 mm³; 0.2-wide bands across each edge hit material | ± 0.1; = 0 | 0 | — | PASS (assumed: A-05, A-06) | section, `interference` / `common_volume` | A-05, A-06 |
| REQ-04 | B2 foremost 98.565 (1.565 proud); B1 95.333, B3 95.345 (1.667 / 1.655 recessed); hole to cap axis at z 95.5: B1 0.002, B2 0.000, B3 0.002 | B2 ≥ 97.5; B1, B3 ≥ 95.0, ≤ 2.0 recessed; ≤ 0.25 | +0.248 | B1 top (−95.080, 161.441, 95.333) | PASS (assumed: A-03, A-04) | `clearance` to a slab over each hole; section centroids of the posed OD-E02; `bore_census` | A-03, A-04 |
| REQ-05 | (a) φ −55 … +10 every 5° plus 7.5, 8.5, 9.0, 9.5: least 2.511 mm to the panel at φ +10 (window's right edge), to OD-E02 ≥ 28.669; (b) φ −50, lowered 15 in 2.5 steps, then carried z 32 → 182 every 5.0 (31 poses): least 11.689 to the panel, ≥ 29.915 to OD-E02, never inside | (a) ≥ 2.0; (b) clearance > 0, not inside | +0.511 | (75.0, 160.297, 97.0) | PASS (assumed: A-05) | `clearance` (fallback) | A-05 |
| REQ-06 | six Ø6 cylinders ∩ panel 0.000 mm³ each (flange-hole axes y 4 … 260; OD-C15 axes y 2 … 260, 1.000 clear) | = 0 | 0 | — | PASS (assumed: A-14) | `interference` / `common_volume` | A-14 |
| REQ-07 | min z 72.000; tray box ∩ panel 0.000 mm³ (gap 0.200); knob place ∩ panel 0.000 mm³ (gap 0.200) | ≥ 72.0; = 0 | 0 | (−104 … +104, 0 … 4, 72.0) flange ends | PASS (assumed: A-06, A-13) | `envelope`, `common_volume` | A-06, A-13 |
| REQ-08 (Soft) | not geometric (bench) | no visible flex under a press or pump drum | — | — | INCONCLUSIVE | — (bench, first print) | A-12 |

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 wall | 3.0 thick, x ±116, y 0 … 215, z 94 … 97 | probes IN at (±100, 100), (0, 200); faces at z 94.000 / 97.000; envelope 232 × 215 | PASS |
| F02 brew opening | slot ∪ window, square corners | one U-shaped outline at z 95.5 with 10 straight edges at the spec values; probes OUT at (0, 25), (0, 120), (−66, 25), (70, 180) | PASS |
| F03 return ribs R1 … R5 | 5 ribs, 3.0 thick, z 84 … 94 | probes IN in all five; OUT past R1's end (79, 189.5) and behind it (z 83.9) | PASS |
| F04 floor flanges | 2, y 0 … 4, z 72 … 94 | probes IN at (±90, 2, 85); OUT at y 4.1 | PASS |
| F05 gussets | 4 right triangles (y 4 … 34, z 78 … 94) | probes IN in all four; OUT above the hypotenuse; sections `rv_x80`, `rv_x102`, `rv_xm78` | PASS |
| F06 flange holes | 4 × Ø3.4 through along Y at (±85, 77), (±95, 77) | 4 bores Ø3.400, length 4.000, through, offset 0.000 | PASS |
| F07 board bosses | 2 × Ø11 on the board-hole axes, z 85.485 … 94 | 2 convex cylinders r 5.500; boss solids z 85.485 … 94 | PASS |
| F08 collar reliefs | 2, radius collar + 0.5 | 2 concave arcs r 8.590 (B1) / 8.691 (B3), z 85.485 … 88.957; lateral gap 0.5000 measured | PASS |
| F09 insert bores | 2 × Ø4.0 × 6.0 blind | 2 bores Ø4.000 × 6.000, open at the end face only | PASS |
| F10 button holes | 3 × Ø15 through on the cap axes | 3 bores Ø15.000 through, at (−94.248, 166.514), (−98.991, 139.901), (−93.765, 113.426) | PASS |
| F11 steam-knob place | kept free | Ø32 cylinder ∩ panel 0.000 mm³; probe OUT at (95.5, 140, 90) | PASS |
| F12 keep-outs | nothing at z < 72, nothing in the tray box | min z 72.000; tray box 0.000 mm³ | PASS |
| F13 top edge | the wall's top face at y 215 | max y 215.000; OD-C10 contact 0.0000 | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity: does every part rest and mount the way the product is used? | The wall foot and both flanges sit on the plate's top face (0.0000), with four M3 screws from above; the lid's skirt rests on the top edge (0.0000). | YES |
| P2 | Function chains connected and aimed (air, drive, liquid, cable)? | Each cap stands in its Ø15 hole on its own axis (offsets ≤ 0.002), and the board sits on the two bosses with the insert bores coaxial to its holes (0.0000). | YES |
| P3 | Moving parts oriented for their motion, with clearance? | The portafilter swings φ −55 … +10 with ≥ 2.511, is lowered and carried out with ≥ 11.689, and the tray slot keeps 0.200 to the tray box. | YES |
| P4 | Human factors: grip, reach, insertion direction obvious? | B2 stands 1.565 proud. B1 and B3 sit 1.66 deep in Ø15 holes, which a fingertip reaches. The flange screws are driven straight down and clear (REQ-06). The board goes on after the panel (A-14). | YES |
| P5 | Next to a comparable real product, does anything look absurd? | No: a flat fascia with a framed brew opening, a tray slot at the plate and a button column is usual on single-group machines. | YES |
| P6 | Nothing floating, embedded, mirrored, or upside-down? | One solid. The ribs, bosses and gussets are behind the wall (z < 94), the front face is the plane z 97, the flanges point to the rear over the plate, and the caps point out through the holes. | YES |

## 5. Positive controls

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` | the panel plus a separate 10 mm box (2 solids) | FAIL (solid_count 2) |
| `envelope` | a 0.5 nub behind the left flange to z 71.5 | FAIL (min z 71.5; size z 25.5) |
| `compare_step` | the B2 hole filled, compared with the delivered STEP | FAIL (volume delta 530.1 mm³, faces delta 1) |
| `feature_census` / `bore_census` | the B2 hole filled | FAIL (8 bores) |
| `locate_bore` | flange hole (−85, 77) moved 0.5 along X | FAIL (offset 0.500) |
| `locate_bore` diameter | flange hole (−85, 77) recut at Ø3.2 | FAIL (Ø3.200) |
| `clearance` (contacts) | the panel raised 0.5 off the plate | FAIL (0.500) |
| `clearance` (E-01) | upper boss grown to Ø12.4 | FAIL (0.000) |
| `clearance` (REQ-05 a) | the window's right edge moved 3.0 to the left | FAIL (0.233 at φ +10) |
| `clearance` fallback (REQ-05 b, unsound OD-G10) | window top lowered to y 170 over x −30 … 30 | FAIL (0.000, inside, at axis z 77 … 117). A first mutant at y 170 … 188 read only at axis z 182 was outside the carried path (49.25): reported, not counted. |
| `interference` / `common_volume` | rib R2 thickened 0.5 into the tray slot | FAIL (147.0 mm³) |
| `radial_profile` | upper insert bore enlarged to Ø5.2 | FAIL (wall 2.450) |
| `radial_extent` | a 2.5 deep pocket in the top bar's inner face at (0, 200) | FAIL (inner face 96.5) |
| `overhang_census` | an 8 × 10 × 2 ledge off rib R2 at z 84 … 86 | FAIL (0.0°) |
| `flat_ceiling_spans` | the same ledge | FAIL (16.0 mm) |
| `min_wall` | the top bar thinned to 0.5 at (0, 200) | FAIL (0.500) |
| `mesh_census` | the delivered STL with one triangle dropped | FAIL (naked edges 3) |
| `mesh_deviation` | the delivered STL against the part moved 0.1 along X | FAIL (0.104) |
| `write_stl` / sagitta | the part meshed at 0.1 mm / 0.5 rad | FAIL (0.0605) |

E-06 and D-03b are section readings and have no mutant control. My own point probes and `flat_ceiling_spans` corroborate them, and both have controls above.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-08 | SOFT_GATE_MISS | not measurable → no visible flex under a button press or pump drum (bench) | — | left pillar (button column); top bar y 188 … 215 | no | MEDIUM | a 232 × 215 × 3 PLA plate with free side edges until OD-C12/C13 exist and a top edge only resting under the lid; geometry cannot tell (A-12) | press each button and run the pump on the first print; if it flexes, tie the side edges or add a rib behind the left pillar |
| F2 | REQ-05 | OBSERVATION | 2.511 → ≥ 2.0 mm at φ +10; 0.796 at +11°, 0.000 (touch) at +12° | +0.511 | window's right edge (75.0, 160.3, 97.0) | no | MEDIUM | the gap closes about 1.7 mm per degree past +5°; a lock that wears beyond ≈ +11.5° (A-05 allows +10) puts the handle on the edge before the lock completes | confirm the wear angle on the first locked portafilter (A-05); if more is needed, move the window's right edge toward +X within the steam-knob place |
| F3 | J-05 | OBSERVATION | 3.049 → ≥ 3.0 mm | +0.049 | upper boss at the B1 collar relief (−92.208, 158.151, 85.535) | no | LOW | the thin web runs only z 85.485 … 88.957, 3.47 of the 6.0 bore, over a narrow arc; it passes, and a Ø4.05 bore still leaves 3.024 | accept; if the web splits on insertion, insert cooler or slower |
| F4 | U-03 | OBSERVATION | OD-G10 to housing 3.6e-15 mm, not inside → `clearance > 0` (fallback) | ≈ 0 | (30.876, 186.511, 24.906), reference pair | no | LOW | a touch between two delivered parts that the fallback cannot tell from a shallow overlap; a ShapeFix copy of OD-G10 is still unsound, so `common_volume` cannot confirm it; the panel is not in the pair | the OD-G01 thread re-exports a sound OD-G10 so the pair can be read as a volume |
| F5 | E-05 | OBSERVATION | the posed OD-E02 has a third through bore Ø3.286 along Z at (−66.236, 140.218), z 50.41 … 52.99, which the spec does not name; the panel holds the board on two bosses only | — | (−66.236, 140.218, 50.41) | no | LOW | presses act at x −94 … −99, 3 … 8 from the boss axes; the board's far end (x −61.5) overhangs about 30 mm and carries no button | when the board is calipered (A-03), check whether the OEM fixed it there; a third boss on that axis would stand only about 0.2 from rib R3 |

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. Zero-margin rows that hold only as designed contacts | Confirmed, each at nominal. Boss ends 0.0001 to the scanned flat (no overlap: +0.001 along Z reads 0.0011). Lateral gap 0.5000 at both reliefs (E-01, margin −4e-13 inside the band). J-05 is 3.049 (F3). The OD-C15 keep-outs touch the wall's inner face at 0 mm³, and the OD-C10 skirt touches the top edge at 0.0000. All pass, by construction, with no margin. |
| 2. The `clearance > 0` fallback passes OD-G10 to housing on 3.6e-15 | Confirmed: 3.55e-15, not inside. ShapeFix does not make OD-G10 sound, so no volume reading is possible (F4). The panel's own fallback pairs read ≥ 11.689 (OD-G10) and contact-plus-0.001 (OD-E02). |
| 3. REQ-05 (a) at φ +10 | Confirmed: 2.511 at +10°, 0.796 at +11°, touch at +12° (F2). |
| REPORT §4 sweep (rated, not re-run) | The only ±0.1 failures are on the zero-gap rows. Boss end ±0.1 gives a 0.1 gap that the screws close, or a 0.1 press: LOW. Top edge −0.1 leaves a 0.1 gap under the lid skirt, a rattle risk on A-07: LOW. Top edge +0.1 gives a 1.18 mm³ overlap that lifts the lid 0.1: LOW. Wall −0.1 in z gives 0.24 mm³ in the OD-C15 keep-out: LOW (feet not designed). The others keep their gates: REQ-05 0.435 with the right edge 0.1 lower, J-05 3.025 with a Ø4.05 bore, D-04a 3.300. |
