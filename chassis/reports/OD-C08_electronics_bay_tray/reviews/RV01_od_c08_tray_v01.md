# RV01 — od_c08_tray_v01 (20261001-od-c08-electronics-bay-tray) — 2026-10-01 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.0 · plan `01_CAD/DESIGN_PLAN.md` · report `01_CAD/REPORT_od_c08_tray_v01.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-02, A-03, A-06, A-07, A-08, A-09, A-11

How I measured: I called `tools/measure` and `tools/core` on the exported files only, using my own scripts in `reviews/RV01_work/` (r01 … r10). I placed OD-E01 myself from `00_Spec/inputs/OD-E01_power_pcb.step` at the spec §4 joint, a proper rotation with origin (84, 80, −100). That board coincides with the board in the delivered assembly: their common volume equals the full 20609.895 mm³. The tray, OD-C01 and OD-C02 in the assembly also each equal their own files. Band (GATES §0, as carried by the plan): mm 0.005, mm³ 0.001, deg 0.001, counts 0. `min_wall`, `min_wall_wide` and `overhang_census` ran at spacing 0.7 (largest step 0.696). I read no CAD code.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c08_tray_C1_v01.step` | 63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91 | yes |
| `02_STEP_STL/od_c08_assembly_C1_v01.step` | 21e6f254048e2239216b63e493d764510f7e002180ba0498bf91406c56ecc9aa | yes |
| `02_STEP_STL/od_c08_tray_C1_v01.stl` | 2ac2db7f63d8ffc91c9d0e3af809a9964152b68826eba5e76eb237d36c22df49 | yes |
| `02_STEP_STL/od_c08_tray_C1_v01.3mf` | 24ac0b1122c6a5ee18293ef45d9dab17485d05515f3b034c7658fe5de802d945 | not in the REPORT (written by the orchestrator); matches the brief |
| `01_CAD/DESIGN_PLAN.md` | 08cce6b90703d0d0ed6b62e0feddab77f624b354940881f46850d45c7261ae31 | yes |
| `01_CAD/REPORT_od_c08_tray_v01.md` | 7e73a0d3bb2d03f52ffc3fb42a51d7cb8fcf3ae5715feac378510aab77fc1b86 | (itself); matches the brief |
| `01_CAD/check_od_c08_tray_v01.json`, `build_record_v01.json`, `sections_v01.json`, `probe/probe_inputs.json` | as the brief | yes |
| `03_Sections/*.png` (16) | as the brief | yes |

Every SHA-256 in the brief matched the file on disk. The REPORT answers every §5 row, so the submission is complete.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 solid, valid 1, naked 0 | solid_count 1, brep_valid 1, naked_edges 0 | 0 | tray; each of the 4 assembly parts also one valid solid | PASS | `validity` | — |
| U-02 | 39.000 × 92.000 × 160.000 mm | each ± 0.1 | 0.1 | x 73.000 … 112.000, y 0.000 … 92.000, z −230.000 … −70.000 | PASS | `envelope` | — |
| U-03 (a) seat contact | overlap 0.000 mm; clearance 0 on each of 4 seats | clearance 0, interference ≤ 0 | 0 | tray less pins reaches x 82.4380 = board min x 82.4380 | PASS (assumed: A-02, A-03, A-06) | decomposition: `envelope` + `clearance` | A-02, A-03, A-06 |
| U-03 (a) plate contact | clearance 0; 0 mm³ | clearance 0, interference ≤ 0 | 0 | (73, 0, −230), flange underside | PASS (assumed: A-01) | `clearance`, `common_volume` | A-01 |
| U-03 (a) pins | 0.3278 mm (H6); 0.3389 (H5) | ≥ 0.30 | 0.0278 | (82.438, 30.185, −157.108) | PASS (assumed: A-02, A-03) | `clearance` | A-02, A-03 |
| U-03 (a) rest of board | 1.000 mm | ≥ 0.5 | 0.5 | (81.438, 32.99, −100.01); wall, flange and gussets alone 6.438 at (76, 24, −94.838) | PASS (assumed: A-02) | `clearance` | A-02 |
| U-03 (a) tray to OD-C02 | 2.000 mm; 0 mm³ | ≥ 1.5 | 0.5 | (73, 0, −230) to the base rail | PASS (assumed: A-06) | `clearance`, `common_volume` | A-06 |
| U-03 (a) OD-E01 to OD-C02 | 15.438 mm | ≥ 10.0 | 5.438 | (82.438, 24, −94.838) | PASS (assumed: A-02, A-06) | `clearance` | A-02, A-06 |
| U-03 (a) board zone | x 82.438 … 109.262, z −195.002 … −94.838, y min 24.000 | x 70 … 117, z −240 … −30, y ≥ 10 | 7.738 (x max) | OD-E01 envelope | PASS (assumed: A-02, A-06) | `envelope` | A-02, A-06 |
| U-03 (a) plate under holes | missing 0 mm³ (Ø10 × 6 column) | plate material under each hole | 0 | 4 holes; nearest plate edge or void 12.0 from the Ø4 insert hole (x 106) | PASS (assumed: A-01) | `common_volume`, `clearance` | A-01 |
| U-03 (b) path | clearance ≥ 0.250 mm at dx 5.0 … 0.25 (20 poses); 0 mm³ at all 21 poses | interference ≤ 0, steps ≤ 0.5 | 0.249 | seat at dx 0.25; pins 0.328 from dx 2.5 down | PASS (assumed: A-02, A-03, A-06) | `clearance`, `common_volume` | A-02, A-03, A-06 |
| U-04 | volume Δ 0 mm³, faces Δ 0 | re-read unchanged, no stray shells, valid | 0 | AP242, unit MM, label `od_c08_tray`, 1 MANIFOLD_SOLID_BREP / 1 CLOSED_SHELL, no open shell; assembly has 4 named parts | PASS | `compare_step`, `step_roundtrip`, `read_schema` | — |
| U-05 | 42 planes, 12 cylinders (6 convex, 6 concave), 6 bores | plan §3 | 0 | see §3 | PASS | `feature_census`, `bore_census`, `locate_bore` | — |
| U-06 (Soft) | 1.800 mm | wide ≥ 2.0 | −0.200 | (82.688, 31.519, −158.238), Ø1.8 pin; tray less pins reads 2.000 | FAIL (Soft) → F1 | `min_wall_wide` | — |
| U-07 | 0.00489 mm | STL tol 0.01, angular ≤ 0.2530, sagitta ≤ 0.01, 3MF = STL | 0.0051 | (82.438, 30.980, −104.018) | PASS | `mesh_deviation`, `write_stl`/`mesh_sagitta`, `mesh_census` | — |
| U-08 | — | threaded parts only | — | — | N/A: the row applies to threaded parts and this one has none | — | — |
| D-01a | 1.800 mm | ≥ 0.8 | 1.000 | (82.688, 31.519, −158.238), pin | PASS | `min_wall` | — |
| D-01b | 2.000 mm | ≥ 2.0 (pins and 0.44 floors excepted) | 0.000 | (75.75, 92.0, −113.478), web above the tie slot | PASS | `min_wall` on the tray less its pins | — |
| D-02 | 160.0 mm | ≤ 220 × 220 × 250 | 60.0 | bed 92 × 160, height 39 | PASS (assumed: A-09) | `envelope` | A-09 |
| D-03a | 90.0 deg | ≥ 45 (crowns of the four flange holes excepted) | 45.0 | holes refilled: nothing downward off the bed; whole part 0.0 only on the 4 crowns, e.g. (89.7, 0, −78) | PASS (assumed: A-08) | `overhang_census(build_dir=(1,0,0))` | A-08 |
| D-03b | 3.4 mm | ≤ 5 | 1.6 | the 4 Ø3.4 hole crowns; flat ceilings 0 | PASS (assumed: A-08) | `flat_ceiling_spans`, `bore_census`, sections | A-08 |
| D-04a | 3.400 mm | ≥ 3.25 | 0.150 | all 4 flange holes | PASS | `bore_census`, `locate_bore` | — |
| D-04c | 1.000 mm; interference 0 | ≥ 0.5 | 0.500 | as U-03 (a), rest of board | PASS (assumed: A-02) | `clearance`, decomposition | A-02 |
| D-04d | 0.3278 mm | ≥ 0.30 | 0.0278 | H6 (82.438, 30.185, −157.108); H5 0.3389 | PASS (assumed: A-02) → F4 | `clearance` | A-02 |
| D-05a | 10.000 mm | ≥ 8.0 across | 2.000 | both bores, 12 diameters × 3 depths | PASS (assumed: A-07) | `radial_extent` | A-07 |
| D-05b | Ø4.000, depth 6.000, blind | Ø4.0 ± 0.05, 6.0 ± 0.1, ≥ 5.7 | 0.050 | x 76.438 … 82.438 at H1, H2 | PASS (assumed: A-07) → F3 | `bore_census`, `locate_bore` | A-07 |
| D-06a | 1.800 mm | ≥ 1.0 | 0.800 | both pins (exact cylinders) | PASS | `min_wall`, cylinder axes | — |
| D-07 | — | none on this part | — | — | N/A: the row lists no fit-critical bore on this part | — | — |
| J-05 | 3.000 mm | ≥ 3.0 | 0.000 | both bores, 24 rays × 3 depths, least at (76.938, 85, −100) | PASS | `radial_extent` | — |
| E-01 | 1.000 mm | = D-04c | 0.500 | as D-04c | PASS (assumed: A-02) | `clearance` | A-02 |
| E-05 | 0.0041 mm | ≤ 0.10 | 0.0959 | H5; H1 0.0032, H2 0.0032, H6 0.0022 | PASS (assumed: A-02, A-03) | `bore_census`/`locate_bore` on both solids, cylinder axes | A-02, A-03 |
| E-06 | 4 + 4 | standoffs from the wall; 4 gussets | 0 | standoffs start at x 76.000, each sections as one face with wall and flange; gussets one face, area 620 | PASS | sections, cylinder faces | — |
| E-11 | 4 slots | two pairs above the board; open on +X, ±Z, above | 0 | slots y 86 … 90, z −177/−169/−123/−115 … +2, 2.131 above the board top; 4 open boxes 0 mm³ | PASS (assumed: A-11) | sections, `common_volume` | A-11 |
| REQ-01 | Ø3.400, offset 0.000, 4.000 long, through | Ø3.4 ± 0.1, ≤ 0.10, 4.0 ± 0.1; underside y 0 ± 0.1 | 0.100 | 4 holes; underside one plane y 0.000 (6203.68 mm²); plate material complete | PASS (assumed: A-01) | `locate_bore`, faces, `common_volume` | A-01 |
| REQ-02 | seats x 82.4380 (×4, spread 0) | 82.44 ± 0.05; bores Ø4.0; pins Ø1.8 ± 0.05 × 2.5 ± 0.1; offsets ≤ 0.10 | 0.048 | pins Ø1.800 × 2.500 (x 82.438 … 84.938), offsets 0.000 | PASS (assumed: A-02, A-03) | faces, `bore_census`, `locate_bore`, cylinder axes | A-02, A-03 |
| REQ-03 | 73.000 mm | ≥ 73.0; front z −70.0 ± 0.1 | 0.000 | max z −70.000 | PASS (assumed: A-06) | `envelope` | A-06 |
| REQ-04 | 0 mm³ | 4 Ø8 × 116 cylinders: 0 with the tray and the board | 0 | board at least 13.307 from a cylinder (x 88, z −78) | PASS (assumed: A-03) | `common_volume`, `clearance` | A-03 |
| REQ-05 | 0 mm³ | box x 85 … 117, y 4 … 92, z −195 … −95: 0 | 0 | box empty | PASS (assumed: A-03) | `common_volume` | A-03 |
| REQ-06 (Soft) | — | board does not flex visibly under a faston push (bench) | — | farthest tab z −188, 30.5 past the H6 standoff | INCONCLUSIVE → F2 | bench | A-04, A-12 |
| exactly_one_solid | 1 | = 1 | 0 | — | PASS | `validity` | — |
| feature_census | as U-05 | plan §3 | 0 | — | PASS | `feature_census` | — |
| envelope_within_spec | as U-02 | ± 0.1 | 0.1 | — | PASS | `envelope` | — |

Mesh detail (U-07). The delivered STL has 3244 triangles, one body, 0 naked edges, consistent winding and 70594.55 mm³ (B-rep 70596.00). I re-meshed the STEP freshly at 0.01 mm / 0.2 rad (0.2 ≤ 4·acos(1 − 0.01/5) = 0.2530): sagitta 0.00489, 3244 triangles, and its surface coincides with the delivered STL (1.8e-8 mm both ways; only the diagonals on flat faces differ). That makes the STL the D5 export. The 3MF holds one object in mm with 3244 triangles, and every one equals an STL triangle (8e-7 mm, same winding); it is watertight. `min_wall_mesh` reads 1.7975, matching the B-rep 1.800 within the chordal tolerance.

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 wall + flange | L section, envelope 39 × 92 × 160 | section area 420.000 at z −150 and −120 | PASS |
| F02 gussets ×4 | 20 × 20 × 3 at z −230, −212, −88, −73 | 4 hypotenuse faces x 76 … 96, y 4 … 24 at those z ranges; section area 620 | PASS |
| F03 insert standoffs ×2 Ø10 | r 5, x 76 … 82.438 | 2 cylinders r 5.000 at (80.00, −100.00), (27.99, −100.01) | PASS |
| F04 pin standoffs ×2 Ø6 | r 3, x 76 … 82.438 | 2 cylinders r 3.000 at (81.98, −157.52), (30.99, −157.51) | PASS |
| F05 pins ×2 Ø1.8 × 2.5 | r 0.9, x 82.438 … 84.938 | 2 cylinders r 0.900, coaxial with F04 | PASS |
| F06 insert bores ×2 | Ø4.0 × 6.0 blind along X | 2 bores, floor closed | PASS |
| F07 flange holes ×4 | Ø3.4 through along Y | 4 bores, through | PASS |
| F08 tie slots ×4 | 2.0 × 4.0 through the wall | 4 holes in the sections at x 73.2, 74.5 and 75.8 | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity | The flange lies on the plate top (clearance 0, interference 0) and takes four screws. The 0.1 kg board sits on four standoffs off a wall with four gussets. In the print the tray lies on its wall face and everything rises from it as a prism. | YES |
| P2 | Function chains | Screw: each Ø3.4 hole is over complete plate material (the inserts are still to be added, A-01). Board: seated on its solder face, insert bores coaxial with H1/H2 within 0.004. Wires: four slots 2.13 above the board top. The faston box on +X is empty. | YES |
| P3 | Moving parts | No moving part in service. On the mounting path the clearance stays ≥ 0.25 over 20 poses and the board meets the seats only at dx 0. | YES |
| P4 | Grip, reach, insertion | All four Ø8 driver paths are clear of the tray and the board. The board goes on along −X over the two pins, then two screws go in from the component side. | YES |
| P5 | Absurdity | A 3 mm PETG wall, 6.4 mm standoffs and a 90 g part make an ordinary on-edge PCB bracket. Only the Ø1.8 pins are slender, and they only locate. | YES |
| P6 | Floating, embedded, mirrored, upside-down | The tray is one solid and each standoff sections as one face with the wall. The board I placed equals the assembly's board. Its solder face points toward the bulkhead and its heatsink toward +X. | YES |

The sections are my own, written with `write_sections` into `reviews/RV01_work/sections/` with nothing clipped: z −100 / −157.5 / −222 for the assembly, and the gusset, slot and flange sections of the tray.

## 5. Positive controls

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` (U-01) | degrade: shell with one face removed | FAIL |
| `envelope` (U-02, REQ-03, D-02) | resize: wall top raised to y 92.5 | FAIL |
| `feature_census` (U-05) | remove: tie slot z −176 filled | FAIL |
| `bore_census`/`locate_bore` (REQ-01, D-04a, D-05b, REQ-02) | relocate: flange hole x 88, z −222 moved 0.5 | FAIL |
| `min_wall` (D-01a/b, D-06a) | resize: web above the slots 2.0 → 1.5 | FAIL |
| `min_wall_wide` (U-06) | same | FAIL |
| `overhang_census` (D-03a) | degrade: 20 × 20 cap on a stem, ceiling facing the bed | FAIL |
| `flat_ceiling_spans` (D-03b) | same cap (span 22.6) | FAIL |
| `radial_extent` (D-05a, J-05) | resize: H1 boss Ø10 → Ø7.8 (7.8 across, wall 1.9) | FAIL |
| `clearance` (D-04d, U-03, E-01, D-04c) | relocate: H6 pin moved 0.10 in z (0.229) | FAIL |
| `clearance` = 0 (seat contact) | resize: H1 seat lowered 0.05 | FAIL |
| `clearance` (tray to OD-C02) | relocate: tray moved 2.5 in −X | FAIL |
| seat-face reading (REQ-02) | resize: H1 seat raised 0.06 (82.498) | FAIL |
| decomposition (U-03, D-04c) | resize: H1 standoff rebuilt 0.06 taller (overlap 0.060) | FAIL |
| `common_volume`, whole tray × OD-E01 | resize: H1 standoff rebuilt 0.06 taller (3.65 mm³); relocate: tray +0.06 in X (9.95 mm³) | FAIL |
| `common_volume`, whole tray × OD-E01 | resize: a 0.06 (also 0.5) disc fused onto the H1 seat face | PASS: blind spot, F5; no gate rests on this check alone |
| `common_volume` along the path (U-03 b) | relocate: H5 pin moved 0.5 | FAIL |
| `clearance` along the path (U-03 b) | relocate: H5 pin moved 0.5 | FAIL |
| `common_volume` × OD-C01 (whole tray and flange region) | relocate: tray sunk 0.05 (310.18 mm³) | FAIL |
| `common_volume` (REQ-04) | degrade: rib across the x 88, z −78 driver path | FAIL |
| `common_volume` (REQ-05, E-11) | degrade: rib into the faston box | FAIL |
| sections (E-06; E-11) | remove: gusset z −88; tie slot filled | FAIL; FAIL |
| `compare_step` (U-04) | resize: wall raised 0.5 against the delivered file | FAIL |
| `mesh_census` (U-07) | degrade: one STL triangle removed | FAIL |
| `mesh_deviation`, `mesh_sagitta` (U-07) | degrade: meshed at 0.1 mm / 0.5 rad (0.036) | FAIL |
| 3MF-to-STL comparison (U-07) | relocate: one 3MF vertex moved 0.05 | FAIL |
| `min_wall_mesh` (corroboration) | resize: STL of the web-1.5 mutant | FAIL |

The tray × OD-E01 interference rows rest on the decomposition, and the path on clearance pose by pose. Both have controls that FAIL. I also ran a region-cut `common_volume`, but its only control used the fused mutant, so no gate uses it.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | U-06 | SOFT_GATE_MISS | 1.800 → ≥ 2.0 mm (wide) | −0.200 | (82.688, 31.519, −158.238), Ø1.8 pins | no | LOW | The reading is the pins' own diameter, which passes under D-06a. The part has no rounds, and the tray less its pins reads 2.000. The spec exempts the pins under D-01b only. | The Usta names the pins as a U-06 exception, or the pins grow to Ø2.0 (that takes D-04d to about 0.23). |
| F2 | REQ-06 | SOFT_GATE_MISS | not measurable → no visible flex under a faston push | — | tabs y ≈ 29.5, z −136 … −188; farthest 30.5 past the H6 standoff | no | MEDIUM | INCONCLUSIVE by its row. The board is held by two pins and two screws, and the tab row overhangs the last support by up to 30.5 with 6.44 of air behind it (A-04, A-12). | Bench-test at first assembly. If the board flexes, add a plain rest pad near z −185, y 30, clear of solder-side mains (A-05). |
| F3 | D-05b | OBSERVATION | screw tip x 76.0 → short of the floor x 76.438 | −0.438 | H1/H2 bores | no | MEDIUM | An M3 × 8 through the 1.562 board reaches 0.438 past the 6.0 bore floor without a washer, so it bottoms before it clamps the board. It fits only with the ≥ 0.44 washer A-04 assumes. | State a washer ≥ 0.5 in A-04, or use M3 × 6, or deepen the bores to ≥ 6.5 by a D-05b change. |
| F4 | D-04d | OBSERVATION | 0.3278 → ≥ 0.30, with E-05 allowing 0.10 | 0.0278 | H6 pin | no | LOW | A 0.10 pin offset reads 0.229 (control) while E-05 still passes, so the two rows conflict. The pin still enters with up to about 0.33 of combined error. The hole positions are scan values (A-02). | The Usta reconciles D-04d with E-05, and calipers check H5/H6 (A-02). |
| F5 | U-03 | OBSERVATION | 0 mm³ reported → real overlap of 3.65 mm³ | — | H1 seat, fused-disc mutant | no | LOW | Tool finding, not a part deviation: `common_volume` returned MEASURED 0 for a real overlap in fused topology at the seat plane. The delivered rows rest on the decomposition and on clearance, whose controls FAIL. | Tool maintainers: fail closed on an empty result when the operands overlap beyond contact, and add this mutant to the mutation manifest. |

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. D-04d against E-05 | Confirmed: 0.3389 (H5) and 0.3278 (H6). A pin moved 0.10 reads 0.229 and fails D-04d while E-05 still passes, so D-04d tolerates about 0.03 of position error (F4). A-02 calipers are needed. |
| 2. Seat at x 82.438 on a scanned flat solder face | The four seats sit at x 82.4380 with spread 0, equal to the board's lowest x, and the overlap is 0. The heatsink screw holes in the board model, (y 46.6, z −148.1) and (72.1, −148.2), are 10.6 and 15.3 from the nearest standoff edge. Their heads clear the wall only if under 6.44 tall: A-05, open. |
| 3. Walls at their limits | The web reads 2.000 (D-01b, margin 0) and the boss wall 3.000 on every ray (J-05, margin 0). Both pass as built and neither has a build tolerance. The Ø4.05 case (2.975) needs an oversize printed hole, which is the less likely error in FDM. |
