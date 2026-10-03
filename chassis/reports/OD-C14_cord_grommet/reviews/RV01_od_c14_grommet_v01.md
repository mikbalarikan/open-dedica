# RV01 — od_c14_grommet_v01 (20261002-od-c14-cord-grommet) — 2026-10-02 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with the WP-03 answers) · report `01_CAD/REPORT_od_c14_grommet_v01.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-02, A-03, A-04, A-05, A-06, A-07

The submission was complete. Every §5 row is answered in the REPORT, every listed file is present, and every SHA-256 matches the brief and the REPORT. Every value below was measured by my own scripts in `reviews/RV01_work/` (`m1_part.py` … `m6_mesh_rt.py`, results in `m*.json`) from the exported STEP and the two input STEPs. I built my own check assembly: my own copy of the half, turned 180° about the hole axis measured on OD-C11 by `bore_census`/`locate_bore` (Ø12.000 at (95.000, 30.000), z −302 … −299, through), and my own envelopes from spec §5. These are a cord of Ø 2 × the measured bore radius (3.500), a tie ring of Ø10.3/12.9 over z −298.8 … −294.0, and a head box at x 92.5 … 97.5, y 36.45 … 42.45, z −298.8 … −293.8. Band (GATES §0 as the plan carries it): 0.005 mm, 0.001 deg and mm³, 0 for counts. No CAD code was read.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c14_grommet_half_C1_v01.step` | 55ce2a3e6a68458e6f97f26a58b05d4691bd69f310105551f98b28fcdb0a0680 | yes |
| `02_STEP_STL/od_c14_grommet_half_C1_v01.stl` | 645a8dde3b824729be2fe225589561b529c879c2bf9fbb5b10d927f102eafaa8 | yes |
| `02_STEP_STL/od_c14_assembly_C1_v01.step` | a21a8f9d88d7f1ec8a97103c980ec2f16a798c9376a0d124be1c3b3b8a8b992b | yes (reference only; not used for any gate) |

Also checked against the brief: the spec (180292d0…2b7d), plan (731a8495…0e4b), REPORT (35dc2fd8…e821), OD-C11 (8ac0df9c…3db), OD-C01 (7b5688af…805), and the six sections (hashes as REPORT §1).

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | solid_count 1, brep_valid 1, naked_edges 0; free shells 0, free faces 0 | 1 / 1 / 0 | 0 | whole half | PASS | `validity` | — |
| U-02 | 19.984 × 9.600 × 13.000 mm; position x 85.008 … 104.992, y 30.400 … 40.000, z −304.000 … −291.000 (reported apart; x is 0.008 in from the split chord) | each in [spec − 0.1, spec + 0.1] | +0.084 | size_x at the split face | PASS | `envelope` | — |
| U-03 | see the U-03 rows below; governing value: halves 0.800 mm apart | (a), (b), (c) of spec §5 | +0.050 | (98.769, 30.4 / 29.6, −304.0) | PASS (assumed: A-01, A-02, A-04) | `clearance`, `interference`, `common_volume`, `radial_extent`, `envelope` | A-01, A-02, A-04 |
| U-04 | re-read: 1 solid labelled `od_c14_grommet_half`, AP242, MM, 0 free shells or faces; `step_roundtrip` of that solid: volume delta 1.1e-13 mm³, faces delta 0, labels 1, valid after 1 | unchanged, no stray shells, valid | 0 | — | PASS | `compare_step`, `step_roundtrip` | — |
| U-05 | plane 6, cylinder 5 (4 convex, 1 concave), cone 3, others 0, bores 0; each face matched to its feature (§3) | plan counts | 0 | — | PASS | `feature_census`, `radial_extent` | — |
| U-06 (Soft) | 1.650 mm (45°) | ≥ 1.6 | +0.050 | (90.029, 31.346, −298.614) groove floor | PASS | `min_wall_wide` | — |
| U-07 | delivered STL sagitta 0.00584 mm; 1658 triangles, 1 body, 0 naked edges, winding 1, volume 538.319 mm³ (B-rep 538.555); a re-mesh at 0.01 mm / 0.10 rad (≤ 0.1789) gives 1658 triangles and 0.00584 | ≤ 0.01 | +0.00416 | (95.806, 35.333, −293.167) collar flank | PASS | `mesh_deviation`, `mesh_census`, `write_stl` | — |
| U-08 | — | threads cosmetic | — | — | N/A: the row applies to threaded parts; this target has none | — | — |
| D-01a | 1.650 mm | ≥ 0.8 | +0.850 | (90.029, 31.346, −298.614) groove floor | PASS | `min_wall` | — |
| D-01b | 1.650 mm (mesh corroborates 1.6485 ≥ 1.650 − 0.01) | ≥ 1.6 | +0.050 | groove floor, as above | PASS (assumed: A-03) | `min_wall`, `min_wall_mesh` | A-03 |
| D-02 | 19.984 × 9.600 × 13.000 mm, standing on the flange | within 220 × 220 × 250 | +200.016 | — | PASS (assumed: A-07) | `envelope` | A-07 |
| D-03a | 59.886° (flank 60.000°); build_dir +Z; sampling bound 0.006° | ≥ 45° | +14.886 | (91.549, 30.581, −303.500) bed-side bore chamfer | PASS (assumed: A-06) | `overhang_census` | A-06 |
| D-03b | 0.0 mm: no flat ceiling; my sections x 95, y 32, z −296.6 show none | ≤ 5 | +5.0 | — | PASS (assumed: A-06) | `flat_ceiling_spans`; reviewer sections | A-06 |
| D-04d | 0.350 mm open pose (neck); collar on the path 0.350 | ≥ 0.30 | +0.050 | (100.636, 30.400, −301.900) neck at the split edge | PASS (assumed: A-01) | `clearance`, `radial_profile` | A-01 |
| D-06a | 1.650 mm | ≥ 1.0 | +0.650 | groove floor | PASS | `min_wall` | — |
| D-07 | — | none | — | — | N/A: the row names no fit-critical bore for this part | — | — |
| J-06 | bore_census 0; B-spline and other faces 0 | no printed threads | 0 | — | PASS | `bore_census`, `feature_census` | — |
| E-11 | squeeze 0.400 mm each half; tie 0.200 off the inner face, OD 12.900 over the Ø12.000 hole; flange 0.000 on the outer face; inside chamfer r 3.5 → 4.0, outside r 3.5 → 3.79; sections | gripped, retained both ways, no sharp edge | +0.070 (squeeze) | my sections x 95, z −296.6 | PASS (assumed: A-02, A-04, A-05) | reviewer sections; `radial_extent`, `clearance` | A-02, A-04, A-05 |
| REQ-01 | flange Ø20.000, neck and collar Ø11.300, groove Ø10.300, spread 0.000 over 10° … 170°; z −304.000 / −302.000 / −298.800 / −293.600 / −292.734 / −291.000; flank 60.000°; every axis at (95.000, 30.000) | Ø ± 0.1 / ± 0.05; z ± 0.1; 60 ± 1°; offset ≤ 0.05 | +0.050 (neck/collar/groove Ø) | — | PASS (assumed: A-01) | `radial_profile`, `radial_extent`, `envelope` | A-01 |
| REQ-02 | split: 2 faces in the plane y 30.400; bore r 3.500 (min = max over 17 angles × 120 levels); inside chamfer 0.50 radial × 0.50 axial; outside 0.29 radial × 0.50 axial | y 30.40 ± 0.02; r 3.50 ± 0.05; chamfers ± 0.1 | +0.020 (split) | — | PASS (assumed: A-02, A-05) | `radial_profile`, `radial_extent`, `envelope`, `feature_census` | A-02, A-05 |
| REQ-03 | my 180° copy; closed pair 19.984 × 19.200 × 13.000 mm, union one valid solid | 20.0 / 19.2 / 13.0 ± 0.1 | +0.084 | — | PASS | `envelope` | — |
| REQ-04 | groove width 5.200 mm; tie OD 12.900; head box to OD-C11 gussets and flange 14.677 | 5.2 ± 0.1; > 12.0; ≥ 0.5 | +0.100 | (97.5, 36.45, −298.8) head box | PASS (assumed: A-04) | `envelope`, `clearance` | A-04 |
| REQ-05 (Soft) | — | holds against a firm hand pull and does not turn (bench) | — | — | INCONCLUSIVE (bench; F1) | — | A-05 |

**U-03 rows (my assembly; OD-C11 and OD-C01 at the identity):**

| Row | Measured | Required | Margin |
|---|---|---|---|
| (a) flange face to OD-C11 outer face, A / B | 0.000 / 0.000 | = 0 | 0 |
| (a) bore to cord, A / B | 0.000 / 0.000 (2.6e-13) | = 0 (tangent) | 0 |
| (a) tie to groove floor, A / B | 0.000 / 0.000 | = 0 | 0 |
| (a) half beyond the flange (z ≥ −301.9) to OD-C11, A / B | 0.350 / 0.350 | ≥ 0.30 | +0.050 |
| (a) tie / head box to the inner face | 0.200 / 0.200 | 0.20 ± 0.10 | +0.100 |
| (a) halves to each other | 0.800 | 0.80 ± 0.05 | +0.050 |
| (a) to OD-C11 gussets and floor flange: A / B / tie / head | 8.411 / 3.010 / 2.9995 / 14.677 | ≥ 0.5 | +2.4995 |
| (a) to OD-C01: A / B / tie / head | 30.400 / 20.000 / 23.550 / 36.450 | ≥ 10 | +10.000 |
| (a) tie OD over the hole | 12.900 | > 12.0 | +0.900 |
| (a) interference, 21 pairs of A, B, OD-C11, OD-C01, cord, tie, head | 0 mm³ each | ≤ 0 | 0 |
| (b) measured split offsets A / B | 0.400 / 0.400 | — | — |
| (b) halves at the closed pose | 0.000 mm, 0 mm³ | = 0, ≤ 0 | 0 |
| (b) half beyond the flange to OD-C11, A / B | 0.364 / 0.364 | ≥ 0.30 | +0.064 |
| (b) squeeze at 90° / 270°, four z levels, A / B | 0.400 / 0.400 (cord overlap 34.71 mm³ each: the designed squeeze) | 0.40 ± 0.07 | +0.070 |
| (c) path dz −20 … 0 in 0.5 steps, with the closing of 0 / 0.2 / 0.4 swept together (123 poses) | worst 0 mm³ against OD-C11 and OD-C01; least gap before the seat 0.350 (collar and neck in the hole) | ≤ 0 mm³ | 0 |

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F02 flange | convex cylinder r 10.0, z −304 … −302; bed and wall faces | cylinder r 10.000, z −304.000 … −302.000; planes z −304.000, −302.000 | PASS |
| F03 neck | convex cylinder r 5.65 (spec 1.1), z −302 … −298.8 | cylinder r 5.650, z −302.000 … −298.800; step plane z −298.800 | PASS |
| F04 tie groove | convex cylinder r 5.15, 5.2 wide | cylinder r 5.150, z −298.800 … −293.600 | PASS |
| F05 collar flank | cone, 60° from horizontal, r 5.15 → 5.65 | cone semi-angle 30.000° (60.000° from horizontal), z −293.600 … −292.734 | PASS |
| F06 collar | convex cylinder r 5.65 to z −291.0, top plane | cylinder r 5.650, z −292.734 … −291.000; plane z −291.000 | PASS |
| F07 bore | 1 concave cylinder r 3.5 (half-bore, so 0 bores) | concave cylinder r 3.500, z −303.5 … −291.5; bore_census 0 | PASS |
| F08 inside chamfer | cone 0.5 × 45° | cone 45.000°, r 3.5 → 4.0 over z −291.5 … −291.0 | PASS |
| F09 outside chamfer | cone 0.50 axial × 0.29 radial | cone semi-angle 30.11°, r 3.79 → 3.5 over z −304.0 … −303.5 | PASS |
| F11 split face | one plane at y 30.40, in 2 faces | 2 planar faces, normal +Y, at y 30.400 | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | Gravity: does every part rest and mount the way the product is used? | The flange bears on the wall's outer face (0.000) and the tie sits inside, so the grommet holds in any orientation. It prints standing on its flat flange face. | YES |
| P2 | Function chains connected and aimed (air, drive, liquid, cable)? | The cord runs straight through the bore on the measured hole axis, 2.50 from the hole wall, with nothing across its path (sections x 95 and z −296.6). | YES |
| P3 | Moving parts oriented for their motion, with clearance? | Insertion and closing were swept together over 123 poses: 0 mm³ against OD-C11 and OD-C01, least gap 0.350. The closed halves touch at 0 mm³. | YES |
| P4 | Human factors: grip, reach, insertion direction obvious? | The halves go round the cord and push in along +Z until the flange stops them. The tie head sits at +Y, 14.7 clear of the gusset, and can be reached from inside. | YES |
| P5 | Next to a comparable real product, does anything look absurd? | It reads as an ordinary split strain-relief bushing with a cable tie: a 20 mm flange, 13 mm long, for a 7 mm cord. | YES |
| P6 | Nothing floating, embedded, mirrored, or upside-down? | Every contact reads 0.000 with 0 mm³. The copy is my own 180° rotation, not a mirror. The flange is outside and the collar inside (section x 95). | YES |

## 5. Positive controls

| Check | Mutant of this job's part | Got |
|---|---|---|
| `validity` | collar-top face removed (open shell): naked_edges 4 against 0 | FAIL |
| `envelope` | flange resized to Ø21.2: size_x 21.185 against 20.0 ± 0.1 | FAIL |
| `feature_census` | tie groove filled to Ø11.3: 4 cylinder faces against 5 | FAIL |
| `bore_census` | Ø3 through-hole in the flange at (95, 37.5): 1 bore against 0 | FAIL |
| `radial_profile` | bore radius 3.50 → 3.60: 3.600 against 3.50 ± 0.05 | FAIL |
| `radial_extent` | bore r 3.60: closed-pose squeeze 0.300 against 0.40 ± 0.07 | FAIL |
| `min_wall` | groove floor thinned to 1.40 (Ø9.8): 1.400 against ≥ 1.6 | FAIL |
| `min_wall_wide` | the same mutant, 45° reading: 1.400 against ≥ 1.6 | FAIL |
| `overhang_census` | flat ledge ring on the collar top to Ø15: 0.0° against ≥ 45° | FAIL |
| `flat_ceiling_spans` | 11 mm bridge on two posts above the flange: 9.0 against ≤ 5 | FAIL |
| `clearance` | half moved 0.5 along +X: neck to hole 0.000 against ≥ 0.30 | FAIL |
| `interference` | half moved 0.5 along +X: 1.194 mm³ into OD-C11 against ≤ 0 | FAIL |
| `common_volume` | the same relocated half against OD-C11: 1.194 mm³ | FAIL |
| `mesh_sagitta` (`write_stl`) | STL written at 0.1 mm / 0.5 rad: 0.0457 against ≤ 0.01 | FAIL |
| `mesh_deviation` | the same coarse STL against the B-rep: 0.0457 against ≤ 0.01 | FAIL |
| `mesh_census` | the delivered STL with 10 triangles removed: 12 naked edges against 0 | FAIL |
| `compare_step` | bore r 3.60 solid against the delivered STEP: volume delta 12.56 mm³ against 0 | FAIL |

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-05 | SOFT_GATE_MISS | not measurable (bench) → holds against a firm hand pull and does not turn | — | — | no | MEDIUM | Grip and anti-rotation rest only on the tie closing stiff PLA halves by 0.400 per side (A-03, A-05). A round Ø11.3 neck in the Ø12.0 hole has nothing keyed against turning. | Answer it at the first fitting with a pull and twist test. If the grommet slips or turns, cut the halves further from the axis or key the neck, or print in TPU as the BOM says. |
| F2 | D-01b | OBSERVATION | 1.575 at the combined REQ-01/REQ-02 tolerance corner (groove Ø10.25, bore r 3.55) → ≥ 1.6; the delivered part reads 1.650 | −0.025 (corner) / +0.050 (delivered) | groove floor | no | LOW | The delivered nominal wall is 1.650 and passes. Only the combined corner, which the one-at-a-time sweep did not build, gives 1.575. The spec's D-01b basis gives 1.60 for that corner. | Correct the D-01b basis arithmetic, or tighten the groove or bore tolerance so the combined corner holds 1.60. This build needs no geometry change. |

Not findings, recorded for the delivery: the delivered STL has the same triangle count and sagitta as my own re-mesh at 0.01 mm / 0.10 rad, but its bytes differ, which is consistent with meshing the in-memory build rather than the re-imported solid. The delivery must carry the reviewed bytes (645a8dde…faa8).

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. The axial play band 0.20 ± 0.05 is tighter than REQ-01's ± 0.1 | Spec 1.2 sets 0.20 ± 0.10. I measure 0.200 for both the tie and the head box. The REPORT's neck_len ends (0.100 and 0.300) now sit on the band edges and pass. Resolved. |
| 2. The rigid cord contact and closed pose against the bore and split tolerances; D-01b 1.600 at bore high | Spec 1.2 sizes the cord on the measured bore (r 3.500, tangent 0.000) and moves each half by its measured split offset (0.400 / 0.400). The halves touch at 0 mm³ and the squeeze is 0.400. At the sweep ends the squeeze equals the split offset, 0.38 to 0.42, inside 0.40 ± 0.07, so the REPORT's U-03a and U-03b sweep FAILs no longer apply under spec 1.2. The D-01b corner is F2. |
| 3. REQ-05 and A-03: grip, anti-rotation, and PLA at the 1.65 groove wall | Geometry cannot answer this. The groove wall measures 1.650, and nothing keys the neck against turning. F1 stays MEDIUM until the first fitting. |
