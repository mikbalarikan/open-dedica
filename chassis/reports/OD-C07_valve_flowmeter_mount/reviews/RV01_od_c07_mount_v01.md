# RV01 — od_c07_mount_v01 (20260930-od-c07-valve-flowmeter-mount) — 2026-09-30 UTC

Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted
Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with `briefs/WP-03_designer.md`, `briefs/WP-04_designer.md`) · report `01_CAD/REPORT_od_c07_mount_v02.md`

**VERDICT: REVISE**
Blocking findings: 4 (F1–F4, arising from two geometric deviations) · open assumptions relied on: A-02, A-03, A-04, A-06, A-07, A-08, A-09, A-10, A-12, A-13, A-14, A-15, A-16, A-18, A-19

Geometry is as the spec draws it and every dimensional, print, snap and path row passes. REQ-01, REQ-02, U-03 and D-04c fail at 0.297 mm (recess edge to OD-H24 rib) and 0.377 mm (ring root round to cup) against 0.5; the REPORT's contact cut at r 13.68, z 0.5 hid both. Risk LOW.

Method. Every row was re-measured on `02_STEP_STL/od_c07_mount_C1_v01.step` as re-read, with OD-H24 placed at mount + (0, 0, 10.0) and OD-H22 at mount + (62.0, 0, 48.0) (spec §2). The assembly STEP holds the same three solids at the same places (volumes and bounding boxes identical to my placement). Bands (GATES §0): mm 0.005, deg 0.001, mm³ 0.001, counts 0. No designer script was read. My scripts, logs and sections are in `reviews/RV01_work/`.

Contact neighbourhoods. The spec does not define "away from the designed contacts". I took the OD-H24 rim contact as A-06's rim annulus r 13.98 … 15.71 up to z_H24 0.3, the height where the rim's edge rounds end (measured). I took the OD-H22 flange contact as everything at or above its flange back face. REPORT v02 cut OD-H24 wider, at r 13.68 … 16.21 up to z_H24 0.5. That cut removes the rib ends and the cup's foot, and with them the two gaps in F1–F4.

## 1. Files reviewed

| File | SHA-256 | Matches REPORT |
|---|---|---|
| `02_STEP_STL/od_c07_mount_C1_v01.step` | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c | yes |
| `02_STEP_STL/od_c07_assembly_C1_v01.step` | 50d126c13b945edca3cfd9a5082189ddbd6380bfbb6e59cd24bc71c546f6c9d7 | yes |
| `02_STEP_STL/od_c07_mount_C1_v01.stl` | 41bccd61c1fb0e82a7a8171c85da2128d0c01ca6906f80c03c5ffebf83de3c38 | yes |
| `01_CAD/REPORT_od_c07_mount_v02.md` | 2b4a50f0a3ed54a9479c22234f6d1087d1970658c05c81416bf24f72ab8a5084 | yes |
| `03_Sections/od_c07_assembly_v01_front_y0.png` | c82c911de5ea50f00c486ac232a3be73757d6b618e02b364fed83a3ebfa0bb0a | yes |
| `03_Sections/od_c07_assembly_v01_left_x62.png` | 627480207b47ba5bec15e2fc71f72661d680b644b339740bcd878d75cb8677ec | yes |
| `03_Sections/od_c07_mount_v01_front_y0.png` | 07e3dfaa6dcf1b66c63899d01e3e4f22878b5607994d31a2c61d4437616f20d4 | yes |
| `03_Sections/od_c07_mount_v01_left_x62.png` | b22fd218abd547d0ba49e597cf9e241d62e97b3a596b721367456e593aac7586 | yes |
| `03_Sections/od_c07_mount_v01_left_x7p48.png` | fe7e47b4f7fbb36c9674d2bd284c5ecebc51b4768d126f86413e527c99fe0538 | yes |
| `03_Sections/od_c07_mount_v01_left_xm11p78.png` | 26f17982ec3da2d0029652a472feeb629874bed6157806c6d542f558eeadd891 | yes |
| `03_Sections/od_c07_mount_v01_top_z10p25.png` | 12227a9402aac63b16f00cf593480dc9c4e76d17f5e9ef5ddef015f1fb6901cd | yes |
| `03_Sections/od_c07_mount_v01_top_z47.png` | 58e1855969367303edd2ba843912635c0572643e92e9308d2740bc6d571c09cc | yes |
| `00_Spec/inputs/OD-H22_3way_valve.step` | bc0ffd003bcba248c7c8c4d68b198994726ee34b6c7e96ac97fbfd6490920028 | yes |
| `00_Spec/inputs/OD-H24_flowmeter.step` | 1b4cbdafd03e0edafcc900b8c8c0894b382a48bd71850b59b06201a1fb45696a | yes |

Every other file REPORT v02 §1 lists (scripts, logs, check JSON, probes) also matches its SHA-256; I hashed them only and read none of the scripts.

## 2. Gate table

| Gate | Measured | Required | Margin | At | Status | Method | Assumes |
|---|---|---|---|---|---|---|---|
| U-01 | 1 count | solid_count = 1, brep_valid = 1, naked_edges = 0 | 0 | solid_count 1, brep_valid 1, naked_edges 0; the file holds 1 shell, no loose shell or face | PASS | `validity` | — |
| U-02 | 48 mm | 119.0 x 50.0 x 48.0 each in [spec - 0.1, spec + 0.1]; min x -25, min y -25, min z 0 reported apart | 0.1 | size 119.000 x 50.000 x 48.000 (each margin 0.1); min (-25.000, -25.000, 0.000) | PASS | `envelope` | — |
| U-03 | 0.297 mm | (a) contacts clearance = 0 with interference <= 0; every other pair clearance >= 0.5 away from the contacts; (b) OD-H24 -Z path and OD-H22 -Y slide at +5.0 then 5.0 drop, interference <= 0 | -0.203 | (0.761, -14.170, 9.890) recess edge chamfer to OD-H24 rib end (0.750, -13.960, 10.100), rib/hub inside the rim radius r 13.98 (A-06); contacts: rim/pedestal 0 at (14.4, 0, 10.0), flange/deck 0 at (50.15, 1.2, 48.0), 3 catches 0 at z 29.9; interference 0 mm3 with both OEM solids; H22 below its flange 0.503; path (b): OD-H24 51 poses 0 mm3 (hooks exempt), OD-H22 100 slide + 21 drop poses 0 mm3 with mount and with OD-H24, least slide clearance 0.858 at y +15.5 | FAIL | `clearance, common_volume, own path sweep` | A-02, A-03, A-06, A-07 |
| U-04 | 0 mm3 | named body re-read unchanged, no stray shells, valid after re-import | 0 | compare_step to the file: schema AP242, 1 solid, volume delta 0, faces delta 0, label od_c07_mount, valid after; own round trip of the re-read body: volume delta 1.2e-9 mm3 | PASS | `compare_step, step_roundtrip` | — |
| U-05 | 15 count | 15 feature kinds per the plan (U-05 list) | 0 | all 15 present with their counts; bores 12 (4 footprint, 2 pin, 2 clearance, 2 insert, recess, ring inner); no closed stem bore | PASS | `feature_census, bore_census, locate_bore, own probes` | — |
| U-06 | 1.6 mm | min_wall wide >= 1.5 (Soft) | 0.1 | (-16.679, 8.825, 31.500) hook 160 deg catch tip | PASS | `min_wall_wide` | — |
| U-07 | 0.00396 mm | STL at tol 0.01, angular <= 4 acos(1 - 0.01/R_max); stl_max_sagitta <= 0.01 | 0.00604 | own re-mesh of the STEP at 0.01 mm / 0.05 rad (limit 0.1112 rad at R_max 25.87, hook-root torus) reproduces the delivered bytes; 92262 triangles, 1 body, 0 naked edges, winding 1; mesh_deviation to the STEP 0.0048; mesh wall 1.7214 vs B-rep 1.7224 | PASS | `write_stl, mesh_sagitta, mesh_census, mesh_deviation` | — |
| U-08 | —  | threads cosmetic; applies to threaded parts | — | no threads on this target (inserts take the thread) | N/A: by its row | `N/A by its row` | — |
| D-01a | 1.7224 mm | min_wall >= 0.8 | 0.9224 | (-16.101, 2.520, 10.255) ring wall base between the 0.3 root round and the 60 deg lip chamfer | PASS | `min_wall` | — |
| D-01b | 1.7224 mm | min_wall >= 1.5 | 0.2224 | (-16.101, 2.520, 10.255) ring wall base; deck wedges from section rays at z 47.999: 1.789 (-X, hole at 46.662) and 1.898 (+X, hole at 77.447) | PASS | `min_wall; radial_extent section rays` | — |
| D-02 | 119 mm | each envelope size <= 220 x 220 x 250, bottom face down | 101 | 119.0 x 50.0 x 48.0 against 220 x 220 x 250 | PASS (assumed: A-12) | `envelope` | A-12 |
| D-03a | 60.0184 deg | every downward face >= 45 deg except the named supported faces and bridges | 15.0184 | (-11.865, -13.599, 10.083) ring lip chamfer cone; exactly 9 flat downward faces, all named: 3 notch ceilings z 10.5, 3 catch undersides z 29.9, deck underside z 40.3, 2 insert-bore ceilings z 46.0 | PASS (assumed: A-16) | `overhang_census in slabs, flat-face census` | A-16 |
| D-03b | 4 mm | span <= 5 | 1 | insert-bore ceilings Ø4.000 at z 46.0 (46.662, 0) and (77.447, 0); notch ceilings 2.000 wide x 0.5 at z 10.5 | PASS (assumed: A-16) | `bore_census, radial_extent rays, sections` | A-16 |
| D-04a | 3.4 mm | Ø >= 3.25 (4 footprint + 2 screw clearance holes) | 0.15 | all six Ø3.400 | PASS | `locate_bore` | — |
| D-04c | 0.297 mm | >= 0.5 per side between the mount and each OEM solid away from the designed contacts | -0.203 | (0.761, -14.170, 9.890) recess edge to OD-H24 rib (see U-03); ring root round toe (-10.584, -11.999, 10.000) to OD-H24 cup 0.377; OD-H22 below its flange 0.503 at (55.053, -1.200, 43.766); hooks to pipes 13.346, to connector 4.939 | FAIL | `clearance` | A-02, A-03, A-06, A-07 |
| D-04d | 0.3773 mm | ring gap and pin holes >= 0.30 per side | 0.0773 | ring root round toe (-10.584, -11.999, 10.000) to cup; pin holes 0.500 each | PASS (assumed: A-06, A-07) | `clearance` | A-06, A-07 |
| D-05a | 16.274 mm | material >= 8.0 across around each Ø4.0 insert bore | 8.274 | least of 36 diameters x 6 depths, z 45.99, both bores | PASS (assumed: A-13) | `radial_extent` | A-13 |
| D-05b | 5.7 mm | Ø 4.0 +- 0.05, depth >= 5.7 from the deck underside | 0 | both bores Ø4.000, 5.700 deep from z 40.3, open on the underside | PASS (assumed: A-13) | `bore_census, locate_bore` | A-13 |
| D-06a | 1.7224 mm | minimum feature >= 1.0 | 0.7224 | (-16.101, 2.520, 10.255) ring wall base | PASS | `min_wall` | — |
| D-07 | —  | applies to reamed fit bores | — | none on this part | N/A: by its row | `N/A by its row` | — |
| J-01 | 0.6708 % | eps = 1.5 y t / (L^2 Q) <= 1.5 % | 0.8292 | each hook: y = 20.37 - 18.870 = 1.500, t = 2.000, L = 29.900 - 4.000 = 25.900, L/t 12.95 so Q = 1 | PASS (assumed: A-15) | `radial_extent, vertical rays, arithmetic` | A-15 |
| J-02 | 2 mm | beam thickness >= 1.0 | 1 | each hook at z 6, 15, 25 | PASS | `radial_extent` | — |
| J-03 | 2 ratio | catch/root thickness ratio reported; binding only if eps within 0.2 % of the limit | 1.5 | catch radial length 4.000 / beam 2.000; eps 0.67 % is 0.83 % from its limit, so the taper rule does not bind | PASS | `radial_extent` | — |
| J-04 | 0 mm3 | each hook undeflected: interference <= 0 with OD-H24; catch underside clearance = 0 | 0 | hooks 70/160/320: 0 mm3, catch underside 0 at z 29.9, beam to flange 0.510 | PASS (assumed: A-06, A-08) | `common_volume, clearance` | A-06, A-08 |
| J-05 | 3.612 mm | wall >= 3.0 around each insert bore over its 5.7 depth | 0.612 | insert bore (46.662, 0) toward +X at z 45.99 (the slit end); (77.447, 0) 3.721 | PASS | `radial_extent` | — |
| J-06 | —  | printed threads | — | none (inserts) | N/A: by its row | `N/A by its row` | — |
| E-06 | 16 count | insert pads are the deck tied to the legs; hooks and ring root-filleted to plate and pedestal | — | deck continuous into both legs (x 38 and 86: material z 0 to 48); root rounds: ring 0.3 (3 pieces), pedestal 1.0, hook roots 1.5 inner and outer (x3 each), legs 3.0 (x6) | PASS | `reviewer, face census and rays` | — |
| REQ-01 | 0.3773 mm | pedestal top z 10.0 +- 0.1; ring inner R in [16.30, 16.40] at z 10.5..12.5; ring top z 13.0 +- 0.1; clearance(ring, OD-H24 cup) in [0.50, 0.70] | -0.1227 | ring root round toe (-10.584, -11.999, 10.000) to OD-H24 cup (-10.393, -11.781, 10.241), cup taken outside the A-06 rim annulus r 15.71; 0.413 with the cup from z_H24 0.3; ring wall above the round 0.531; pedestal top 10.000, ring inner R 16.300 (0..359 deg), ring top 13.000 | FAIL | `clearance, radial_profile, vertical rays` | A-06 |
| REQ-02 | 0.297 mm | pin bores Ø4.8 / Ø3.8 +0.1/-0, offset <= 0.10, length 9.4 +- 0.1; clearance to each pin >= 0.5; recess R 14.10 +- 0.1, floor z 9.40 +- 0.05; clearance recess to OD-H24 ribs and hub >= 0.5 | -0.203 | (0.761, -14.170, 9.890) recess edge chamfer to rib (0.750, -13.960, 10.100); 0.243 to the rib face's end at r 14.056; bores Ø4.800 / Ø3.800, offset 0, length 9.400, through; pin clearances 0.500 / 0.500; recess R 14.100..14.150, floor 9.400 | FAIL | `locate_bore, clearance, radial_profile` | A-07 |
| REQ-03 | 0 mm3 | hooks at 70/160/320 +- 1 deg; beam inner R 20.87 +- 0.1 over z 6..26; catch underside z 29.9 +- 0.1 reaching R 18.87 +- 0.1; catch lands outside slots and windows (clearance = 0); chamfer 45 +- 1 deg | 0 | void under each catch 0 mm3 (sector r 18.87..19.70, 2.65 deep); centres 70.000/160.000/320.000; beam inner 20.870; catch underside 29.900; reach 18.870; chamfer 45.000; catch clearance 0 | PASS (assumed: A-06, A-08, A-09) | `radial_profile, radial_extent, common_volume, clearance` | A-06, A-08, A-09 |
| REQ-04 | 7.05 mm | deck top z 48.0 +- 0.1 flat under the flange; U-slot 14.1 +0.1/-0, profile 180..360 deg at z 41..47 in [7.05, 7.10], walls y +-(7.05 +0.05/-0) open to +Y, length 7.7 +- 0.1; slits 2.40 +- 0.1 reaching 62 +- (11.85 +0.1/-0); clearance(mount, OD-H22) >= 0.5 away from the flange | 0 | slot 7.050 at every ray outside the two slit windows (180..360 below z 43.3; 190..350 over z 41..47); literal window reads 10.72 at 186 deg z 46.875 inside the slit (F5); walls 7.050 at y 2.5..14; open to +Y 0 mm3; deck z 40.3..48.0; one +Z plane above z 40, at 48.000; slits 2.400 wide, reach 11.850, taper 43.42 deg; clearance to OD-H22 0.503 | PASS (assumed: A-03) | `radial_profile, radial_extent, common_volume, clearance` | A-03 |
| REQ-05 | 4 mm | Ø3.4 +- 0.1 at (77.447, 0), (46.662, 0), 2.0 +- 0.1 deep, offset <= 0.10; coaxial Ø4.0 +- 0.05, 5.7 +- 0.1 deep from the underside | 0.05 | both: Ø3.400 x 2.000 (z 46..48), Ø4.000 x 5.700 (z 40.3..46.0), offsets 0.000 | PASS (assumed: A-02, A-13, A-18) | `locate_bore` | A-02, A-13, A-18 |
| REQ-06 | 3.4 mm | four Ø3.4 +- 0.1 through-holes at (-18, +-21), (88.5, +-21), offset <= 0.10, length 4.0 +- 0.1 | 0.1 | all four Ø3.400, offset 0.000, length 4.000, through | PASS (assumed: A-14) | `locate_bore` | A-14 |
| REQ-07 | 40 mm | window x 40..84, y -25..25 through the plate; leg inner faces at x 40.0 and 84.0 +- 0.1 | 0.1 | plate pieces x -25..40 and 84..94 over y +-25; 0 mm3 in x 40.001..83.999 below the deck; leg inner faces 40.000 / 84.000 at 9 points | PASS (assumed: A-04, A-19) | `envelope, common_volume, radial_extent` | A-04, A-19 |
| REQ-08 | 48 mm | no material above z 48.1; none within r 12 of the valve axis above the deck top | 0.1 | max z 48.000; 0 mm3 in r 12 about (62, 0) above z 48.0 | PASS (assumed: A-10) | `envelope, common_volume` | A-10 |
| REQ-09 | 2 mm | up-facing pockets drain; three notches 2.0 +- 0.1 wide x 0.5 +- 0.1 high at 25/115/225 +- 1 deg | 0.1 | notches 2.000 x 0.500 (z 10.0..10.5) at 25.000/115.000/225.000, 0 mm3 in each; pin holes through from the recess floor z 9.4; window through | PASS | `radial_extent, common_volume, sections` | — |

Motion (U-03 b). Each path was swept with all of its motion variables together, from first contact to the final pose.
- **OD-H24:** lowered along −Z from +25 in 0.5 mm steps (51 poses): 0 mm³ against the mount with the three hook sectors exempt. The hooks overlap the flange from +9.5 down to the seat, which is the snap deflection (catch overlap 1.5).
- **OD-H22:** slid along −Y at +5.0 from y +45 to 0 (1 mm steps, 0.25 mm over y 18 … 0; 100 poses), then dropped 5.0 in 0.25 mm steps (21 poses): 0 mm³ against the mount and against the seated OD-H24 at every pose. The least slide clearance is 0.858 at y +15.5, at the slot mouth corner (54.95, 15.0, 48.0). On the drop the gap holds 0.503 (stem to slot) down to +0.75, then closes onto the flange contact.

Deck wedges (brief). I measured these from sections of the exported STEP: exact rays from each Ø3.4 clearance-hole wall to the slit end over ±30° at z 47.999 … 46.01. At the deck top the wedges are **1.789 mm** (−X, hole at 46.662) and **1.898 mm** (+X, hole at 77.447). They widen with depth, to 3.891 / 4.000 at z 46.01. Both pass D-01b's 1.5. `min_wall` does not see them, because the faces are not opposed within 25°.

## 3. Feature census against the plan

| Plan feature | Expected | Found | Status |
|---|---|---|---|
| F01 plate 4.0, x -25..94, y +-25 | 1 plate, z 0..4 | z 0..4.000 over x -25..94, y +-25 | PASS |
| F02 plate window x 40..84, full Y | 1 window splitting the plate | 2 plate pieces x -25..40 and 84..94; 0 mm3 in the window | PASS |
| F03 footprint holes Ø3.4 x4 | 4 through, length 4.0 | 4 x Ø3.400 through, 4.000, offsets 0 | PASS |
| F04 pedestal R 18.0, z 4..10 | 1 convex cylinder R 18.0, top z 10.0 | R 18.000, top 10.000 | PASS |
| F05 ring wall R 16.30..18.30, z 10..13 | 1 ring | inner 16.300, outer 18.300, top 13.000 | PASS |
| F05b ring lip chamfer (REPORT §8: 0.30 x 0.52 at 60 deg) | 1 cone under the 0.3 overhang | cone 60.02 deg from horizontal, z 10.0..10.52 | PASS |
| F06 pin clearance holes Ø4.8, Ø3.8 | 2 through, 9.4 long (P-3) | Ø4.800 and Ø3.800 through, 9.400, offsets 0 | PASS |
| F07 snap hooks at 70/160/320 deg (P-4) | 3 | 3, centred 70.000/160.000/320.000 | PASS |
| F08 legs x 36..40, 84..88, y +-15, z 4..48 | 2 | 2, material z 0..48 at x 38 and 86, y +-15.000 | PASS |
| F09 deck x 40..84, y +-15, z 40.3..48 | 1 | 1, z 40.300..48.000, y +-15.000 | PASS |
| F10/P-1 stem U-slot 14.1 open to +Y (no closed bore) | 1 U-slot | R 7.050 semicircle on -Y, walls 7.050, 0 mm3 in the +Y channel | PASS |
| F11/P-2 gusset slits 2.40 to 62 +- 11.85 | 2 | 2, 2.400 wide, reach 11.850, taper 43.42 deg | PASS |
| F12 screw clearance holes Ø3.4 | 2, 2.0 deep | 2 x Ø3.400, 2.000, offsets 0 | PASS |
| F13 insert bores Ø4.0 | 2, 5.7 deep, open below | 2 x Ø4.000, 5.700, open on the underside | PASS |
| F14 root fillets | hooks, pedestal, legs, ring | ring 0.3 (3 pieces), pedestal 1.0, hooks 1.5 inner and outer x3, legs 3.0 x6 | PASS |
| P-3 pedestal recess R 14.10 x 0.60 | 1 | R 14.100, floor 9.400, plus a 0.2 edge chamfer (REPORT §8) | PASS |
| P-5 ring drain notches 2.0 x 0.5 | 3 at 25/115/225 deg | 3, 2.000 x 0.500 at 25/115/225 | PASS |

All 15 U-05 features are present. Two changes from the plan are both declared in REPORT §8: the recess edge chamfer 0.2 and the catch land 1.6.

## 4. Plausibility (`GATES.md` §P, one line each)

| # | Question | Answer | Status |
|---|---|---|---|
| P1 | gravity | the plate rests on its bottom face; centre of mass (34.89, -0.13, 17.58) inside the footprint; OD-H24 on its rim on the pedestal (0 gap, 0 mm3) and OD-H22 on its flange back face on the deck (0 gap, 0 mm3) | YES |
| P2 | function chains | valve ports hang +-Y under the deck between the legs over an empty window (0 mm3 below the deck); flowmeter pipes leave toward -Y 13.3 from the nearest hook; ear holes over coaxial clearance and insert bores (offset 0); annulus and recess drain through the notches and pin holes | YES |
| P3 | moving parts | assembly only: OD-H24 drops 25 mm with 0 mm3 off the hooks, whose 45 deg lead-ins face up so the flange cams them out; OD-H22 slides -Y at +5 and drops 5 with 0 mm3 (121 poses), least slide gap 0.858 | YES |
| P4 | grip, reach, insertion | nothing above z 48.0 and 0 mm3 within r 12 of the valve axis above the deck, so the OPV is open from above; screws from above; valve in along -Y into a slot open to +Y; hook catches reachable from outside at R 22.87 | YES |
| P5 | absurdity | a 119 x 50 x 48 mm, 51.5 g PETG bracket with a 4 mm plate, 4 mm legs and 2 x 25.9 mm snap beams: ordinary proportions for a printed bracket | YES |
| P6 | floating, embedded, mirrored, upside-down | one solid; the assembly STEP places both OEM solids exactly where the spec joints put them (bounding boxes and volumes identical to my own placement); drive tube up to z 61.68, slot semicircle on -Y, 0 mm3 overlap | YES |

Evidence: my sections in `reviews/RV01_work/sections/` (deck top z 47.99, notches z 10.25, insert bore x 46.662, assembly at x 62 / y 0, the rib at x 0.75, the ring root at y −12). Each has 0 px clipped.

## 5. Positive controls

| Check | Mutant of this job's part | Got |
|---|---|---|
| validity.solid_count | exported part plus a loose 10 mm cube | FAIL |
| validity.naked_edges | exported part with one face removed (open shell) | FAIL |
| envelope | 0.5 mm pad added on the deck top at (43, -13) | FAIL |
| envelope (REQ-08 max z) | same pad | FAIL |
| locate_bore offset | footprint hole (-18, 21) moved 0.5 mm to (-17.5, 21) | FAIL |
| bore_census diameter | insert bore (46.662, 0) resized Ø4.0 -> Ø4.2 | FAIL |
| feature_census bores | footprint hole (-18, 21) removed (filled) | FAIL |
| common_volume (interference) | 0.2 mm pad on the deck top under the OD-H22 flange | FAIL |
| clearance | ring inner radius reduced 16.30 -> 16.10 | FAIL |
| radial_profile | same ring mutant | FAIL |
| radial_extent (J-05 wall) | insert bore (46.662, 0) moved 1.0 mm toward the slit | FAIL |
| J-01 arithmetic (radial_extent) | hook 70° catch extended inward to R 16.87 | FAIL |
| min_wall | ring wall thinned to 0.7 mm (outer R 18.3 -> 17.0 over z 10.6..13) | FAIL |
| min_wall_wide | same thinned ring | FAIL |
| overhang_census | 2 mm flat ledge added on the -X leg's outer face at z 20 | FAIL |
| flat downward face census | same ledge | FAIL |
| compare_step | the ledge mutant compared with the delivered STEP | FAIL |
| U-03(b) OD-H22 slide sweep | 1 mm bridge across the U-slot mouth at y 13..15 | FAIL |
| U-03(b) OD-H24 drop sweep | pin-1 hole filled from z 5.0 to 9.4 | FAIL |
| deck flatness (+Z planes) | 0.3 mm pocket in the deck top under the flange | FAIL |
| notch probe (common_volume) | notch at 25° filled | FAIL |
| catch landing void | hook 320° relocated to 300° (over the 296.5° slot) | FAIL |
| mesh_sagitta | STL re-meshed at 0.2 mm / 0.5 rad | FAIL |
| mesh_census naked_edges | delivered STL with its last 10 triangles removed | FAIL |
| validity.brep_valid | exported part turned inside out (reversed solid) | FAIL |
| mesh_deviation | STL re-meshed at 0.2 mm / 0.5 rad | FAIL |
| min_wall_mesh | STL of the thinned-ring mutant | FAIL |

Every check family FAILs on its mutant. `brep_valid` passes on an open shell because BRepCheck does not catch that case; `naked_edges` does (14 edges). `brep_valid` itself FAILs on the inside-out solid.

## 6. Findings

| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |
|---|---|---|---|---|---|---|---|---|---|
| F1 | REQ-02 | HARD_GATE_FAIL | 0.297 mm → >= 0.5 from the recess to the OD-H24 underside ribs and hub | -0.203 | (0.761, -14.170, 9.890) recess edge chamfer to rib (0.750, -13.960, 10.100); 0.243 to the rib face's end r 14.056; 0.516 only when OD-H24 is cut at r 13.68 as the REPORT did | yes | LOW | static seat: the rib underside sits 0.1 above the bearing plane and meets the rim's inner round, so the gap is a diagonal to the chamfered recess edge; nothing moves or carries load across it, and a touch would put the rib 0.1 above the rim's own bearing plane | not reachable inside the spec: ribs ending at r 14.056 against a recess R 14.10 +- 0.1 give 0.11 (sharp edge) to 0.30; either the Usta names the rib ends on the rim's round as part of the rim contact (spec wording or a U-18 exception), or the recess edge moves out to about r 14.55, which gives up rim bearing from r 14.3 to 14.55 |
| F2 | REQ-01 | HARD_GATE_FAIL | 0.3773 mm → clearance(ring, OD-H24 cup) in [0.50, 0.70] | -0.1227 | ring root round toe (-10.584, -11.999, 10.000) to cup (-10.393, -11.781, 10.241); 0.413 with the cup from z_H24 0.3; 0.531 at the ring top | yes | LOW | only the lowest 0.05 mm of the 0.3 root round is within 0.5 of the cup's foot; the ring wall keeps 0.531 over its height, D-04d's 0.30 holds, and a flowmeter pushed fully sideways would at worst perch on the round until the hooks seat it | ring root round 0.1 instead of 0.3 (computed about 0.55 at the toe, not built); the plan's ladder test used a cut that could not see the root |
| F3 | U-03 | HARD_GATE_FAIL | 0.297 mm → clearance >= 0.5 between the mount and each OEM solid away from the contacts | -0.203 | same pair as F1 (the recess is not delegated to REQ-02 in U-03's text); contacts, interference and both assembly paths pass | yes | LOW | static seat: the rib underside sits 0.1 above the bearing plane and meets the rim's inner round, so the gap is a diagonal to the chamfered recess edge; nothing moves or carries load across it, and a touch would put the rib 0.1 above the rim's own bearing plane | as F1 |
| F4 | D-04c | HARD_GATE_FAIL | 0.297 mm → >= 0.5 per side away from the designed contacts | -0.203 | recess edge to rib 0.297 (F1); ring root round to cup 0.377 (F2); OD-H22 side 0.503 passes | yes | LOW | the two contact-adjacent gaps of F1 and F2; neither is loaded or moving | as F1 and F2 |
| F5 | REQ-04 | OBSERVATION | 10.72 mm → slot profile 180..360 deg at z 41..47 in [7.05, 7.10] | -3.62 | 186 deg, z 46.875: the literal window runs into the gusset slit the same row requires; every ray outside the slit windows reads 7.050 | no | LOW | a wording overlap in the spec row, not a geometry miss: the slits are there by REQ-04 and read 2.40 / 11.85 | spec: exclude the slit windows (about +-10 deg around 180 and 360 deg above z 43.4) from the slot profile |
| F6 | D-01b | OBSERVATION | 1.7224 mm → the D-01b reason says the only region under 2.0 is the deck wedge (1.79 / 1.90) | 0.2224 | ring wall base (-16.101, 2.520, 10.255) 1.722; catch tip 1.600 at 45 deg (-16.679, 8.825, 31.500) | no | LOW | both pass the 1.5 limit; the ring base is thinned by its root round and lip chamfer, the catch tip by the 1.6 land against the 45 deg lead-in; neither carries the snap bending (the beam stays 2.0) | spec: list these two regions in the D-01b reason |
| F7 | U-03 | OBSERVATION | 19.9 mm → REPORT §4: ped_top_z and catch_under_z pass only at nominal | 0 | catch underside 29.900 minus pedestal top 10.000 = 19.900 = OD-H24 rim-to-flange-top 19.9 (A-06) | no | LOW | the flowmeter pose follows the printed pedestal, so the function rests on the 19.9 stack; zero designed play means +-0.1 per face (plus A-08's +-0.2 warp) gives up to 0.4 axial play or a preload that adds about 0.09 % strain per 0.2 mm; either keeps the flowmeter held | none needed for the gate; if play shows at the first print, shorten the stack by 0.1 to preload the hooks |
| F8 | REQ-04 | OBSERVATION | 48 mm → REPORT §4: deck_top_z passes only at nominal | 0.1 | deck top 48.000 | no | LOW | the valve pose follows the printed deck top and is clamped by its ear screws; +-0.1 moves the valve with it and changes no clearance in the real assembly (the sweep's overlap comes from holding the OEM pose fixed) | none |
| F9 | REQ-05 | OBSERVATION | 7.7 mm → REPORT §4: deck_t passes only at nominal | 0.1 | deck 7.700 = 2.0 clearance + 5.7 insert bore exactly | no | LOW | a 0.1 web left at 7.8 is pierced by the M3 screw or the insert; layer quantisation moves the step, not the stack | optional: take the insert bore 0.2 deeper into the clearance hole so the two always overlap |
| F10 | REQ-07 | OBSERVATION | 40 mm → REPORT §4: leg_gap_half passes only at nominal | 0.1 | leg inner faces 40.000 / 84.000 flush with the window edges | no | LOW | a 0.1 ledge from a leg face 0.1 inside the window is a sub-extrusion overhang that prints; no fit depends on it | none |
| F11 | REQ-02 | OBSERVATION | 14.1 mm → REPORT §4: recess_r passes only at nominal | 0 | recess R 14.100..14.150 over z 9.5..9.9 (the 0.2 edge chamfer) | no | LOW | at R 14.0 the rib gap of F1 narrows further; at 14.2 only the chamfer reads 14.25 in the band; the rim still bears from r 14.3 | settle with F1 |

F1–F4 come from two geometric facts. The Usta can accept them knowingly (D-022):
1. **Rib ends.** OD-H24's underside rib plane (z_H24 0.1) runs out to r 14.056 on the rim's inner round. The spec's recess R 14.10 ± 0.1 therefore cannot give 0.5 to it at any radius inside its band. This one needs a spec decision, not a rebuild.
2. **Ring root round.** The 0.3 round at the ring root brings the ring within 0.377 of the cup's foot. A 0.1 round would clear it.

F7–F11 rate REPORT §4's parameters that pass only at nominal, as the brief asks.

## 7. "Least sure of", answered

| REPORT item | What the review found |
|---|---|
| 1. pin clearances 0.49999... against >= 0.5 | re-measured 0.500 at both pins (2.585, 0.093, 9.4) and (-9.880, 0.140, 9.4): PASS inside the 0.005 band, zero margin by design, resting on A-07 and A-01 as stated |
| 2. rib clause depends on where the ribs end | it does: 0.516 only with OD-H24 cut at r 13.68; the rib/hub inside the rim's inner radius r 13.98 reads 0.297 and the rib face's end at r 14.056 reads 0.243 against 0.5: FAIL (F1, F3, F4) |
| 3. seat parameters pass only at nominal; 320 deg catch 4.94 from the connector | rated LOW as F7 to F11: the seat heights are stacks that the OEM parts follow, not clearances; catch-to-connector re-measured 4.939, D-04c passes |
