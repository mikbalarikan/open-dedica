# RV01 — od_t01_rig_v01 (20261002-od-t01-pressure-test-rig) — 2026-10-03 UTC

Reviewer: Claude Code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with `briefs/WP-03_designer.md`) · report `01_CAD/REPORT_od_t01_rig_v01.md`

**VERDICT: APPROVED (assumption-conditional)**
Blocking findings: 0 · open assumptions relied on: A-01, A-05, A-07, A-08, A-09, A-10, A-11, A-12

One valid 240 x 150 x 120 solid; every hard row of spec 1.2 re-measured and met (least margins: REQ-03 pair-B +0.100, D-03a +0.100 deg, D-01b +1.000, REQ-04a +6.755), resting on A-01, A-05, A-07, A-08, A-09, A-10, A-11, A-12; REQ-08 strength is INCONCLUSIVE and the spec's hand calculation overstates the factor (about 1.5, not 3.8, at the window section).

All measurements were made by the reviewer's own scripts in `reviews/RV01_work/` (`rv_part.py`, `rv_geom.py`, `rv_asm.py`, `rv_controls.py`, `rv_sections.py`), on the delivered STEP re-read from disk. The housing set was posed from `od_g01_assembly_C1_v03.step` by spec §2 (housing x → X, y → +Z, z → −Y, origin (0, 110.06, 0); a proper rotation, verified by mapping the axes), with the solids identified by measurement: housing = the 100 × 100 solid with four Ø4.0 bores at (±44, ±44); OD-G10 = the solid longer than 120 (185.1); OD-G04 = the remaining one. The designer's assembly file was not used for any gate. Band per GATES §0: 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts. No CAD code, sweep folder, or designer JSON was read.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_t01_rig_C1_v01.step` | cc6b1c721fd34f74232c4cee504c95c0852573fa351411ca12a02c27904c9f5c | yes |
| `02_STEP_STL/od_t01_rig_C1_v01.stl` | 1b2985d19a6fe86930bdf4ec448b78576ec830f6ee1f5c513a1ae2e63077d3a5 | yes |
| `02_STEP_STL/od_t01_assembly_C1_v01.step` | 407386d44f5483aa2d2e6eab7eb72a47749aafbdb06252de5dbecfc3acf7774b | yes |
| `01_CAD/REPORT_od_t01_rig_v01.md` | d44d3356664af278e29003e388db94c2aec862bc9a2b4a574604a3f50ca056b1 | yes (brief; not listed in the REPORT) |
| `01_CAD/DESIGN_PLAN.md` | 544bde71e61f60d81c0d2c6b3868a6d9a017457f29aa9d5d96560a5212c10a5d | yes |
| `00_Spec/DESIGN_SPEC.md` | 0036578bbb64a9fe6fac276b06938b135a37e9afc9de4e906ac8d5cfaa6db9f4 | yes (brief; not listed in the REPORT) |
| `00_Spec/inputs/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | yes (brief; not listed in the REPORT) |
| `00_Spec/inputs/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | yes (brief; not listed in the REPORT) |
| `03_Sections/od_t01_rig_v01_z0_assembly.png` | 777d644c8467745a38f7357d8e9e8e546c1150b9865b933c3ccd928309b9910d | yes |
| `03_Sections/od_t01_rig_v01_z44_assembly.png` | 388c579e5ee53f010d6f9b46fce46ca521ba0ccb037b52c876bf8360189aaf09 | yes |
| `03_Sections/od_t01_rig_v01_x44.png` | 40a86f731c369c5b458a87ddb685e7b3bb28daa47f6cf22e9b3d85d518f61c9b | yes |
| `03_Sections/od_t01_rig_v01_y5.png` | 29ad37abb3054b15a07cef2be1dc8ec25c5e51de687dcdc4bd1046c9fb19b9a3 | yes |
| `03_Sections/od_t01_rig_v01_y142.png` | 7a88b8025e5b7ade3fbf65842432f2ab761a6a4ea7a1420c8b16750f0a838116 | yes |

The delivery must carry exactly the STEP and STL bytes above. A reviewer re-mesh of the STEP at 0.01 mm / 0.10 rad reproduces the delivered STL byte for byte.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 bool | solid_count = 1, brep_valid = 1, naked_edges = 0 | 0 | solid_count 1, brep_valid 1 (BOPAlgo faults none), naked_edges 0 of 147 edges; 0 loose shells or faces | PASS | `tools.core.validity` | — |
| U-02 | 240.0 mm | 240.0 x 150.0 x 120.0 each in [spec - 0.1, spec + 0.1] | +0.1 | size 240.000 x 150.000 x 120.000 (each margin +0.100); position x -120.000 .. 120.000, y 0.000 .. 150.000, z -60.000 .. 60.000 (on the datum) | PASS | `envelope` | — |
| U-03 | 0.0 mm | (a) seat clearance = 0; interference <= 0 mm3 every pair; rig to housing elsewhere, OD-G04, OD-G10 >= 2.0; (b) offer-up dy 0..-30, steps <= 2.0: interference <= 0 | +0 | (a) seat clearance 0.000 at (21.25, 135.00, 21.18) plate underside / housing rear face; interference rig|housing 0.000 mm3, rig|OD-G04 0.000 mm3; elsewhere: rig below y 135 to housing 15.000 (+13.0, (-65.0, 135.0, 40.0) chamfer root), rig to OD-G04 5.000 (+3.0, (-21.25, 135.0, 21.18) window edge over the pair-A boss y 130), rig to OD-G10 13.689 not inside (+11.689, (21.25, 135.0, 21.18)); (b) 31 poses dy 0..-30 every 1.0: interference rig|housing and rig|OD-G04 0.000 mm3 at every pose, OD-G10 least 13.689 (dy 0), never inside | PASS (assumed: A-01) | `clearance, interference (common_volume); OD-G10 clearance fallback (REQ-04 text)` | A-01 |
| U-04 | 0.0 mm3 | named body re-read unchanged, no stray shells, valid after re-import | +0 | delivered STEP: AP242, 1 solid, label od_t01_rig, brep_valid 1, 0 stray shells / faces; reviewer re-export of the read solid: volume delta 0.000 mm3, faces delta 0 (54), labels equal, valid after | PASS | `compare_step, step_roundtrip` | — |
| U-05 | 13 count | plan counts: 1 plate, 2 walls (z -60..+40), 1 base, 4 corner chamfers, 4 x 3.4 holes + 4 x 6.5 counterbores (teardrop), 1 hub window (R 30 + teardrop), 4 x 4.5 bench holes (teardrop) | 0 | faces 41 planar + 13 concave cylinders, 0 other; 13 bores: 4 x 3.400 (360 deg), 4 x 6.500, 1 x 60.000, 4 x 4.500 (each 269.8 deg + 2 flanks); 4 chamfer planes 10 x 10; wall inner faces x +-75 z -60.000..40.000 | PASS | `feature_census, bore_census, locate_bore` | — |
| U-06 | 3.0 mm | >= 2.0 (Soft) | +1 | (-45.10, 135.00, -47.04) plate under the (-44,-44) counterbore | PASS | `min_wall_wide` | — |
| U-07 | 0.004997 mm | STL at tol 0.01, angular <= 4 acos(1 - 0.01/30) = 0.1033 rad; stl_max_sagitta <= 0.01 | +0.005003 | reviewer re-mesh at 0.01 mm / 0.10 rad is byte-identical to the delivered STL (SHA 1b2985d1...); 5752 triangles; sagitta 0.0050 at (-21.63, 138.75, 20.78); STL 1 body, 0 naked edges, winding consistent, volume +7.8 mm3 vs B-rep; mesh_deviation 0.0050; 3MF at J5 | PASS | `write_stl, stl_max_sagitta, mesh_census, mesh_deviation` | — |
| U-08 | — | applies to threaded parts; this target has none | — | — | N/A: the row applies to other parts | `N/A by the spec row` | — |
| D-01a | 3.0 mm | >= 0.8 | +2.2 | (-45.10, 135.00, -47.04) plate under a counterbore | PASS | `min_wall` | — |
| D-01b | 3.0 mm | >= 2.0 (webs between counterbores and window, and around bench holes, included) | +1 | (-45.10, 135.00, -47.04) plate under a counterbore; mesh corroboration min_wall_mesh 3.000 | PASS (assumed: A-08) | `min_wall` | A-08 |
| D-02 | 240.0 mm | each size <= 420 x 420 x 500 lying on the rear face: 240 x 150 on the bed, 120 tall | +180 | bed 240.000 x 150.000 (margins +180, +270), height 120.000 (+380) | PASS (assumed: A-09) | `envelope` | A-09 |
| D-03a | 45.1 deg | >= 45 (build +Z); crowns of the four 3.4 holes excepted by position | +0.1 | least 45.100 at (21.25, 135.00, 21.18) window teardrop flank, on a copy with the four 3.4 holes plugged (r 1.8, y 135..138); sampling bound 0.009 deg, 0 samples below 45; unplugged: least 0.0 at (-44.0, 135.0, -42.3) on a 3.4 crown, the named exception; the 216 samples below 45 all vanish with the plugs | PASS (assumed: A-10) | `overhang_census(build_dir=(0,0,1))` | A-10 |
| D-03b | 3.4 mm | span <= 5: the four 3.4 crowns bridge <= 3.4; nothing else bridges | +0 | flat_ceiling_spans 0.000 (no flat ceiling); crowns are 3.400 bores (360 deg) along Y, 3.0 long, seen in reviewer sections y 136.5 and x 44 | PASS (assumed: A-10) | `flat_ceiling_spans, bore_census, reviewer sections` | A-10 |
| D-04a | 3.4 mm | screw holes >= 3.25; bench holes >= 4.25 | +0.15 | 4 x 3.400 at (+-44, 135..138, +-44); 4 x 4.500 at (+-105, 0..10, +-40) (+0.250) | PASS | `bore_census, locate_bore` | — |
| D-06a | 3.0 mm | >= 1.0 | +2 | (-45.10, 135.00, -47.04) | PASS | `min_wall` | — |
| D-07 | — | none: clearance holes only | — | — | N/A: the row applies to other parts | `N/A by the spec row` | — |
| J-05 | — | applies to threaded holes in this part; it has none | — | — | N/A: the row applies to other parts | `N/A by the spec row` | — |
| REQ-01 | 0.0 mm | 4 x 3.4 +- 0.1 at (+-44, +-44), offset <= 0.10 from the posed insert bores, through; 6.5 +- 0.1 counterbores y 150.0 to 138.00 +- 0.10; 3.0 +- 0.1 under each head | +0.1 | hole axes offset 0.000 from the posed insert-bore axes (4.000, y 129.3..135.0); 4 x 3.400 open both ends y 135.000..138.000; 4 x 6.500 y 138.000..150.000, floor closed; plate under head 3.000; every sub-margin +0.100 | PASS (assumed: A-01) | `locate_bore, bore_census` | A-01 |
| REQ-02 | 135.0 mm | underside one plane at y 135.00 +- 0.10 over x +-50, z +-50; housing rear face on it | +0.1 | one -Y planar face at y 135.000 (x +-90, z +-60); 6960 grid points over x, z +-50 off the holes: material at y 135.002 and air at y 134.998 at every point; seat clearance 0 (U-03) | PASS (assumed: A-01) | `envelope, BRep classifier grid, clearance` | A-01 |
| REQ-03 | 10.97 mm | R 30.0 +- 0.1; roof 45.1 +- 1 deg toward +Z, apex z 42.51 +- 0.15; OD-G04 hub tube >= 2.0; pair-B axes >= 10.87 from the window face | +0.1 | pair-B axis (10.64, -15.78) to window face 10.970 at (16.78, 135.0, -24.87) (+0.100); other pair-B axis (-9.31, 16.60) 11.689; window 60.000 offset 0.000, through (R margin +0.100); flanks 45.100 deg (+0.99997); apex z 42.5006 (+0.1406); OD-G04 to rig 5.000 (+3.000) | PASS (assumed: A-05, A-12) | `bore_census, locate_bore, plane-normal flank analysis, clearance, reviewer sections` | A-05, A-12 |
| REQ-04 | 11.755 mm | (a) phi -60..+15 deg, steps <= 5: clearance >= 5.0; (b) phi -50, dy -15, dz 0..200, steps <= 5.0: interference <= 0 read as clearance > 0, not inside | +6.755 | (a) 76 poses every 1 deg: least 11.755 at phi +15 at (75.0, 90.4, 40.0) +X wall front end, never inside; phi > 0 turns the handle to +X (max_x 67.7 / 92.0 / 114.6 at -10 / 0 / +10); (b) 81 poses every 2.5: least 28.689 at dz 50, never inside; lift phi -50, dy -15..0: least 13.689 | PASS (assumed: A-07) | `clearance (OD-G10 fallback)` | A-07 |
| REQ-05 | 52.296 mm | >= 50.0 above the base top y 10 | +2.296 | OD-G10 locked lowest point y 62.296 | PASS (assumed: A-07) | `envelope` | A-07 |
| REQ-06 | 0.0 mm3 | 4 x 4.5 +- 0.1 at (+-105, +-40), offset <= 0.10; four 8 cylinders y 10..300 interference = 0 | +0 | 4 x 4.500 offset 0.000, through y 0..10 (+0.100); probes common volume 0.000 mm3 each | PASS (assumed: A-11) | `locate_bore, common_volume` | A-11 |
| REQ-07 | 0.0 mm3 | four 6 cylinders y 150..300 on the screw axes: interference = 0 | +0 | common volume 0.000 mm3 each; least clearance 0.250 to the counterbore rims | PASS | `common_volume, clearance` | — |
| REQ-08 | — | Soft: holds 3.06 kN on four screws with no visible yield or crack (bench) | — | not geometric; see finding F1 | INCONCLUSIVE (Soft, bench; rated in F1) | `bench test (A-02 hand calculation re-checked)` | A-02 |

Motion: U-03b swept the housing set dy 0 … −30 every 1.0 (31 poses); REQ-04a φ −60° … +15° every 1° (76 poses); REQ-04b dz 0 … 200 every 2.5 at φ −50°, dy −15 (81 poses); the joining lift φ −50°, dy −15 … 0 every 1.0 (16 poses). The insertion path from first contact (dz 200) to the locked pose is covered: translate (b), lift, rotate (a). OD-G10 rows use the spec's `clearance > 0` with `inside == False` reading (OD-G10 `brep_valid` 0, confirmed).

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 frame profile (plate, 2 walls, base, 4 chamfers) | plate y 135..150 x +-90; walls x +-(75..90) z -60..+40; base y 0..10 x +-120; 4 chamfer planes 10 x 10 at 45 deg; 41 planar faces (spec 1.1) | plate, base and walls at those coordinates; wall end faces at z 40.000; 4 chamfer planes width 14.142 (10 x 10); 41 planar faces | PASS |
| F02 hub window R 30 + teardrop | 1 bore 60.0 along Y through the plate, 2 flanks 45.1 deg, apex z 42.51 | 60.000, y 135..150, open both ends, 269.8 deg; flanks 45.100 deg, apex z 42.501 | PASS |
| F03 4 x 6.5 counterbore + teardrop | 4 bores 6.5, y 138.00..150, floor closed, 8 flanks, apex 4.61 | 4 x 6.500 at (+-44, +-44), y 138.000..150.000, bottom closed; 8 flanks 45.100 deg; apex 4.604 from the axis | PASS |
| F04 4 x 3.4 hole (no teardrop) | 4 bores 3.4 360 deg, y 135..138 | 4 x 3.400, 360 deg, y 135.000..138.000, open into the counterbore | PASS |
| F05 4 x 4.5 bench hole + teardrop | 4 bores 4.5 through the base at (+-105, +-40), 8 flanks, apex 3.19 | 4 x 4.500, y 0..10 through; 8 flanks 45.100 deg; apex 3.188 | PASS |
| F06 name and export | body od_t01_rig, AP242 STEP, STL 0.01 mm / 0.10 rad | label od_t01_rig, AP242; STL byte-identical to the reviewer re-mesh at 0.01 / 0.10 | PASS |
| F07 check assembly | rig + housing + OD-G04 + OD-G10 at the spec 2 pose | file present, hash matches; not used for any gate (reviewer posed the set from the v03 input) | PASS |

## 4. Plausibility (`GATES.md` §P, one line each)

From the reviewer's sections in `reviews/RV01_work/sections/` (z 0 and z 44 and x 0 with the housing set; y 142.5, y 136.5, y 5, x 44, z 50 of the rig; nothing_clipped 0 on all eight).

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | gravity | Base 240 x 120 on the bench at y 0, centre of mass (0, 72.5, -4.2) inside the footprint; the housing hangs under the plate on four screws and the brew load pulls it down into them, as on OD-C05. | YES |
| P2 | function chains | Screw heads on 3.0 of plate, axes 0.000 off the inserts; hub reached through the R 30 window from above; load path plate - walls - base - bench holes closed (sections z0, z44). | YES |
| P3 | moving parts | OD-G10 turns phi -60..+15 with >= 11.755 to the rig, goes in at phi -50 along +Z with >= 28.689 and lifts with >= 13.689; the housing set offers up 30 with no interference. | YES |
| P4 | grip, reach, insertion | Screw axes and bench-screw axes clear to y 300 (6 and 8 probes); the handle leaves at the open front where the walls stop at z +40; 52.3 under the portafilter for a cup. | YES |
| P5 | absurdity | A 240 x 150 x 120 PLA frame of 1.19 kg holding a 100 x 100 group head reads as an ordinary bench test fixture. | YES |
| P6 | floating, embedded, mirrored, upside-down | Housing seat clearance 0.000 with 0.000 mm3 interference; the pose is a proper rotation (x->X, y->+Z, z->-Y); teardrops point +Z, the build direction (section y 142.5); handle on +X at 34 deg as in v03. | YES |

## 5. Positive controls

| Check | Mutant of this job's part | Got |
|---|---|---|
| validity (solid_count) | rig plus a copy relocated 300 in X: 2 solids | FAIL |
| validity (naked_edges) | rig with one face removed: open shell, 6 naked edges | FAIL |
| envelope | base resized +1.0 at +X: size_x 241.0 | FAIL |
| feature_census / bore_census | 3.4 hole at (44, 44) removed: 12 bores, 12 cylinders | FAIL |
| locate_bore (offset) | 3.4 hole at (44, 44) relocated +0.5 in X: offset 0.500 | FAIL |
| locate_bore (diameter) | 3.4 hole at (44, 44) resized to 3.2 (D-04a) | FAIL |
| min_wall | counterbore (-44, -44) deepened to y 135.6: 0.600 under the head (D-01a, D-01b) | FAIL |
| min_wall_wide | same deepened counterbore: 0.600 (U-06) | FAIL |
| overhang_census (crowns plugged) | plugged copy with a 10-wide flat-roofed slot through the plate at x 55..65, z 0..5: 0.0 deg | FAIL |
| flat_ceiling_spans | same slot: span 10.000 | FAIL |
| clearance (REQ-04 sweep) | block x 62..75, y 80..100, z 25..40 on the +X wall's inner front: least 2.655 over phi -60..+15 | FAIL |
| clearance (REQ-03 pair-B) | rig relocated (-0.35, 0, +0.35): pair-B distance 10.484 | FAIL |
| clearance (U-03 seat contact) | housing relocated 0.2 down: seat clearance 0.200 | FAIL |
| interference (common_volume) | housing relocated 0.5 up into the plate: 3436.3 mm3; boss on a screw axis above the plate: REQ-07 282.7 mm3 | FAIL |
| compare_step | re-export with the deepened counterbore compared with the delivered shape: volume delta 57.85 mm3, faces delta 1 | FAIL |
| stl_max_sagitta | rig re-meshed at 0.1 mm / 0.5 rad: sagitta 0.0495 | FAIL |
| mesh_census | delivered STL with its last triangle removed: 3 naked edges | FAIL |
| underside grid classifier (REQ-02) | 0.5-deep pocket x 45..49, z -20..-10 in the underside: 55 grid points not material | FAIL |
| flank-plane apex (REQ-03) | rig relocated +0.5 in Z: apex 43.001 | FAIL |

Every check family used in §2 FAILs on its mutant (mutants in `reviews/RV01_work/mutants/` and built in `rv_controls.py`), so no gate rests on a blind check.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-08 | SOFT_GATE_MISS | not measurable (bench) → holds 3.06 kN on four screws with no yield or crack (bench) | — | plate section at x 0 through the hub window (y 135..150) | no | MEDIUM | spec 4's hand calculation uses the full 120 x 15 plate section (Z 4500 mm3, sigma 10.5 MPa, factor 3.8), but between the screw lines the window leaves 47.5 of the 120 (z -60..-30 and 42.5..60): Z 1781 mm3, sigma 26.6 MPa simply supported, factor about 1.5 against an unsourced 40 MPa for PLA (lower with end fixity from the walls); the M3 heads also bear on 3.0 of plate across the layers. | Redo A-02 with the window section (and the head pull-through) before the test; if the factor stays near 1.5, thicken the plate or add ribs beside the window, or raise the test pressure in steps behind a shield. |
| F2 | REQ-03 | OBSERVATION | 42.5006 mm → apex z 42.51 +- 0.15 | +0.1406 | window apex (0, 135..150, 42.50) | no | LOW | the delivered apex has +0.141 margin; spec 1.2's band holds the R 30.0 +- 0.1 stack only through the 0.005 band (R 29.9 gives apex 42.358 against 42.36), and pair-B at R 29.9 is exactly 10.870; no function depends on the apex. | None for the part; if the spec is revised again, widen the apex band to +- 0.16 or state it as a consequence of R. |

REPORT §4 sweep findings rated against spec 1.2: the window_r REQ-03 FAILs no longer hold (R 29.9 gives pair-B 10.870 against ≥ 10.87, margin 0.000, and apex 42.358 against 42.36, inside the 0.005 band; R 30.1 gives apex 42.642 against ≤ 42.66). The two D-03a locator FAILs were in the designer's locator, not the part (see §7). No other sweep row reached a limit. These are statements about tolerance, not deviations of the delivered part.

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. REQ-03 has no tolerance on the window radius | Spec 1.2 now carries apex +- 0.15 and pair-B >= 10.87. Measured R 30.000, apex 42.501 (+0.141), pair-B 10.970 (+0.100): PASS. The REPORT's window_r sweep values (apex 42.359 / 42.642, pair-B 10.870) now pass, the low apex only inside the 0.005 band (F2). |
| 2. The D-03a exception is located by position | Independent route: the four 3.4 holes plugged (all four axes measured 0.000 off nominal) and the census re-run: least 45.100 deg at the window flank, 0 samples below 45; the 216 samples below 45 on the unplugged part are all on the crowns. Sections y 136.5 and x 44 show only the crowns. The REPORT's swept-locator FAILs are a script artefact, not an overhang. |
| 3. OD-G10 is not a sound solid | Confirmed brep_valid 0 on the posed OD-G10 (housing and OD-G04 are 1). Every OD-G10 row used the spec's clearance > 0, not inside fallback: least 13.689 (U-03, lift), 11.755 (REQ-04a), 28.689 (REQ-04b), never inside; the clearance check FAILs on its mutant. |
