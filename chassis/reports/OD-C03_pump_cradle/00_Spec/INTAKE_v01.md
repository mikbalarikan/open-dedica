# INTAKE v01 — 20260930-od-c03-pump-cradle

Intake: Claude Code, claude-sonnet-5 · data class PUBLIC · brief `briefs/WP-01_intake.md` · 2026-09-30

<!--
Everything the job's inputs say, as tables, one row per value (PLAYBOOK §1 intake,
J0). Nothing here is confirmed: the orchestrator turns §2 and §3 rows into A-##
ledger rows in DESIGN_SPEC §6, and only the Usta confirms one (rule 5). Values
keep their original form and source. No prose summaries, no averaging, no
resolved conflicts, no persona text. A new batch of inputs gets a new version;
an earlier version is never overwritten.
-->

## §1 Files

| # | Path (relative to the workspace) | SHA-256 | Bytes | Type | Pages or views | Read how |
|---|---|---|---|---|---|---|
| 1 | 00_Spec/inputs/OD-H01_ulka_ep5_pump.step | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | 824180 | STEP CAD | n/a | listed and hashed only (rule 6); geometry measured later with tools/measure |
| 2 | 00_Spec/inputs/REQUEST.md | 198d1bd3339e88ababf1a14c3a247e328f8a55d5dddcb234a2485e431bdb159e | 1186 | Markdown | 1 page | full text |
| 3 | 00_Spec/inputs/PROJECT_RULES.md | 97e1cf7097e8b8b57c4e99cd796a080a519f58904f6038ad8a023ef0ecc3970f | 6787 | Markdown | 1 page | full text |
| 4 | 00_Spec/inputs/bom_rows.csv | 56da76c4034df9c19bfa0857ab9035c11e897b63b08d27ba504f897dddbb10d9 | 914 | CSV | 10 data rows | full text |
| 5 | 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/README.md | 52b06473b31a2365a638bf0daa993d2dfa32f1121a0caefbb74ff58c72657fa2 | 4549 | Markdown | 1 page | full text |
| 6 | 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/params.json | 21e02bf5c06fefb1f4fa9d4ade7810cfdcdc89ec533a29939c6aa624ba61c43c | 2014 | JSON | 104 keys | full text |
| 7 | 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/expected.json | 752907be9ea4cced726a4fdf8f7386624fc2073d30faa40cb133377f75ef037b | 1019 | JSON | 1 page | full text |
| 8 | 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/export_check.json | 0ac05c25f6f99f1bef0c8a59a134a4ddb1a7af428c59003d07ec8fc073b8899a | 1098 | JSON | 1 page | full text |
| 9 | 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/validator_report.json | be871fc3161b708cb173cc719a04e0471e13ffe6d08fc68185b89ddde542c72d | 2841 | JSON | 1 page | full text |
| 10 | 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/deviation_gate.json | f15afda192173477c7e460dd7ba7539bd65d57de891087465089ce352cb50c11 | 2472 | JSON | 1 page | full text |
| 11 | 00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/alignment_T1.json | cffce039490c0bc93d307c06d9300bca562f87aac175fc4c59b4d5f245429a35 | 383 | JSON | 1 page | full text |
| 12 | 00_Spec/inputs/scan/OD-H01_ulka_ep5_pump/README.md | 6fc2e4f226b7fb3053a1a185949f59f506a5fed5a915ea4e974905be333879be | 1087 | Markdown | 1 page | full text |
| 13 | 00_Spec/inputs/scan/OD-H01_ulka_ep5_pump/calipers.md | abb341dfef49511d6f71ec9c9793fc81ea87b489bbb785bae3d809e4b87b668d | 500 | Markdown | 1 page (empty table) | full text |

## §2 Dimensions

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | outlet tip z (bbox min z) | -66.45 | mm | -66.45 | — | #6 params.json | params.json:tip_z | table | scan-derived, not caliper-checked |
| X-02 | outlet tip chamfer | 0.4 | mm | 0.4 | — | #6 params.json | params.json:tip_chamfer | table | scan-derived, not caliper-checked |
| X-03 | nozzle radius (outlet tip) | 7 | mm | 7 | — | #6 params.json | params.json:r_nozzle | table | scan-derived, not caliper-checked |
| X-04 | nozzle z position | -60 | mm | -60 | — | #6 params.json | params.json:z_nozzle | table | scan-derived, not caliper-checked |
| X-05 | nozzle OD (cross-check, diameter) | 14 | mm | 14 | ±0.15mm | #7 expected.json | expected.json:critical_dims[nozzle_od_scan] | table | scan-derived, not caliper-checked |
| X-06 | nozzle OD measured (validator) | 24 | mm | 24 | ±0.2mm | #9 validator_report.json | validator_report.json:dim:nozzle_od_scan | table | scan-derived, not caliper-checked; pass=True |
| X-07 | outlet bore radius | 4.55 | mm | 4.55 | — | #6 params.json | params.json:bore_r | table | hidden/estimated geometry, not caliper-checked |
| X-08 | outlet bore depth | 7 | mm | 7 | — | #6 params.json | params.json:bore_depth | table | hidden/estimated geometry, not caliper-checked |
| X-09 | nozzle bore OD (cross-check, diameter) | 9.1 | mm | 9.1 | ±0.2mm | #7 expected.json | expected.json:critical_dims[nozzle_bore_scan] | table | scan-derived, not caliper-checked |
| X-10 | nozzle bore OD measured (validator) | 20.5 | mm | 20.5 | ±0.2mm | #9 validator_report.json | validator_report.json:dim:nozzle_bore_scan | table | scan-derived, not caliper-checked; pass=True |
| X-11 | taper step 1 radius | 6.92 | mm | 6.92 | — | #6 params.json | params.json:r_t1 | table | scan-derived, not caliper-checked |
| X-12 | taper step 1 z | -54 | mm | -54 | — | #6 params.json | params.json:z_t1 | table | scan-derived, not caliper-checked |
| X-13 | taper step 2 radius | 6.78 | mm | 6.78 | — | #6 params.json | params.json:r_t2 | table | scan-derived, not caliper-checked |
| X-14 | taper step 2 z | -40.7 | mm | -40.7 | — | #6 params.json | params.json:z_t2 | table | scan-derived, not caliper-checked |
| X-15 | taper step 3 radius | 6.57 | mm | 6.57 | — | #6 params.json | params.json:r_t3 | table | scan-derived, not caliper-checked |
| X-16 | taper step 3 z | -36 | mm | -36 | — | #6 params.json | params.json:z_t3 | table | scan-derived, not caliper-checked |
| X-17 | taper step 4 radius | 6.74 | mm | 6.74 | — | #6 params.json | params.json:r_t4 | table | scan-derived, not caliper-checked |
| X-18 | step radius (r_s1, at z_step) | 10.25 | mm | 10.25 | — | #6 params.json | params.json:r_s1 | table | scan-derived, not caliper-checked |
| X-19 | step OD (cross-check, diameter) | 20.5 | mm | 20.5 | ±0.2mm | #7 expected.json | expected.json:critical_dims[step_od_scan] | table | scan-derived, not caliper-checked |
| X-20 | step OD measured (validator) | 47.3 | mm | 47.3 | ±0.3mm | #9 validator_report.json | validator_report.json:dim:step_od_scan | table | scan-derived, not caliper-checked; pass=True |
| X-21 | z_step (taper step 4 / step radius z level) | -32.75 | mm | -32.75 | — | #6 params.json | params.json:z_step | table | scan-derived, not caliper-checked |
| X-22 | cone start z | -26.4 | mm | -26.4 | — | #6 params.json | params.json:z_cone0 | table | scan-derived, not caliper-checked |
| X-23 | cone end z | -24.5 | mm | -24.5 | — | #6 params.json | params.json:z_cone1 | table | scan-derived, not caliper-checked |
| X-24 | body radius | 12 | mm | 12 | — | #6 params.json | params.json:r_body | table | scan-derived, not caliper-checked |
| X-25 | body OD (cross-check, diameter) | 24 | mm | 24 | ±0.2mm | #7 expected.json | expected.json:critical_dims[body_od_scan] | table | scan-derived, not caliper-checked |
| X-26 | body OD measured (validator) | 121.95 | mm | 121.95 | ±0.5mm | #9 validator_report.json | validator_report.json:dim:body_od_scan | table | scan-derived, not caliper-checked; pass=True |
| X-27 | wrench flats A/F | 11.6 | mm | 11.6 | — | #6 params.json | params.json:flat_af | table | scan-derived, not caliper-checked |
| X-28 | wrench flats z0 | -53.7 | mm | -53.7 | — | #6 params.json | params.json:flat_z0 | table | scan-derived, not caliper-checked |
| X-29 | wrench flats z1 | -47.6 | mm | -47.6 | — | #6 params.json | params.json:flat_z1 | table | scan-derived, not caliper-checked |
| X-30 | rear washer z (rear body datum) | 37.65 | mm | 37.65 | — | #6 params.json | params.json:z_rear | table | scan-derived, not caliper-checked |
| X-31 | rear washer radius | 7.85 | mm | 7.85 | — | #6 params.json | params.json:r_washer | table | scan-derived, not caliper-checked |
| X-32 | rear washer z | 38.15 | mm | 38.15 | — | #6 params.json | params.json:z_washer | table | scan-derived, not caliper-checked |
| X-33 | boss radius (inlet neck) | 6.5 | mm | 6.5 | — | #6 params.json | params.json:r_boss | table | scan-derived, not caliper-checked |
| X-34 | boss z | 42.2 | mm | 42.2 | — | #6 params.json | params.json:z_boss | table | scan-derived, not caliper-checked |
| X-35 | inlet boss OD (cross-check, diameter) | 13 | mm | 13 | ±0.15mm | #7 expected.json | expected.json:critical_dims[inlet_boss_od_scan] | table | scan-derived, not caliper-checked |
| X-36 | inlet boss OD measured (validator) | 14 | mm | 14 | ±0.15mm | #9 validator_report.json | validator_report.json:dim:inlet_boss_od_scan | table | scan-derived, not caliper-checked; pass=True |
| X-37 | ring radius (inlet collar) | 6.85 | mm | 6.85 | — | #6 params.json | params.json:r_ring | table | scan-derived, not caliper-checked |
| X-38 | ring z | 43.6 | mm | 43.6 | — | #6 params.json | params.json:z_ring | table | scan-derived, not caliper-checked |
| X-39 | barb radius | 2.95 | mm | 2.95 | — | #6 params.json | params.json:r_barb | table | scan-derived, not caliper-checked |
| X-40 | barb OD (cross-check, diameter) | 5.9 | mm | 5.9 | ±0.2mm | #7 expected.json | expected.json:critical_dims[barb_od_scan] | table | scan-derived, not caliper-checked |
| X-41 | barb OD measured (validator) | 9.1 | mm | 9.1 | ±0.2mm | #9 validator_report.json | validator_report.json:dim:barb_od_scan | table | scan-derived, not caliper-checked; pass=True |
| X-42 | barb ridge radius | 3.48 | mm | 3.48 | — | #6 params.json | params.json:r_barb_ridge | table | scan-derived, not caliper-checked |
| X-43 | barb 1 z | 47.3 | mm | 47.3 | — | #6 params.json | params.json:z_barb1 | table | scan-derived, not caliper-checked |
| X-44 | barb ridge 1 z | 47.9 | mm | 47.9 | — | #6 params.json | params.json:z_ridge1 | table | scan-derived, not caliper-checked |
| X-45 | barb 2 z | 50.25 | mm | 50.25 | — | #6 params.json | params.json:z_barb2 | table | scan-derived, not caliper-checked |
| X-46 | barb ridge 2 z | 50.9 | mm | 50.9 | — | #6 params.json | params.json:z_ridge2 | table | scan-derived, not caliper-checked |
| X-47 | inlet tip z (bbox max z) | 55.5 | mm | 55.5 | — | #6 params.json | params.json:z_tip_in | table | scan-derived, not caliper-checked |
| X-48 | inlet bore radius | 1.5 | mm | 1.5 | — | #6 params.json | params.json:r_in_bore | table | hidden/estimated geometry, not caliper-checked |
| X-49 | coil radius | 23.65 | mm | 23.65 | — | #6 params.json | params.json:r_coil | table | scan-derived, not caliper-checked; README notes coil is slightly conical/wavy, r 23.50-23.84, fitted as single cylinder |
| X-50 | coil OD (cross-check, diameter) | 47.3 | mm | 47.3 | ±0.3mm | #7 expected.json | expected.json:critical_dims[coil_od_scan] | table | scan-derived, not caliper-checked |
| X-51 | coil OD measured (validator) | 121.95 | mm | 121.95 | ±0.3mm | #9 validator_report.json | validator_report.json:dim:coil_od_scan | table | scan-derived, not caliper-checked |
| X-52 | coil centre offset X | -0.2 | mm | -0.2 | — | #6 params.json | params.json:coil_cx | table | scan-derived, not caliper-checked; README states centre '0.2 mm off-axis' as single figure, conflicts with two-component value here |
| X-53 | coil centre offset Y | 0.1 | mm | 0.1 | — | #6 params.json | params.json:coil_cy | table | scan-derived, not caliper-checked; see coil centre offset X flag |
| X-54 | coil z range start | -8.8 | mm | -8.8 | — | #6 params.json | params.json:z_coil0 | table | scan-derived, not caliper-checked |
| X-55 | coil z range end | 34.5 | mm | 34.5 | — | #6 params.json | params.json:z_coil1 | table | scan-derived, not caliper-checked |
| X-56 | coil edge fillet radius | 1 | mm | 1 | — | #6 params.json | params.json:coil_fillet | table | scan-derived, not caliper-checked |
| X-57 | core tube radius (hidden, not visible in scan) | 8 | mm | 8 | — | #6 params.json | params.json:r_core | table | hidden/estimated geometry, not caliper-checked |
| X-58 | frame outer X min | -27.2 | mm | -27.2 | — | #6 params.json | params.json:fx0 | table | scan-derived, not caliper-checked |
| X-59 | frame outer X max | 26.85 | mm | 26.85 | — | #6 params.json | params.json:fx1 | table | scan-derived, not caliper-checked |
| X-60 | frame Y half-extent (fy) | 16.2 | mm | 16.2 | — | #6 params.json | params.json:fy | table | scan-derived, not caliper-checked; README states full width 32.4mm (Y) = 2x fy |
| X-61 | frame outer Z min | -12.4 | mm | -12.4 | — | #6 params.json | params.json:fz0 | table | scan-derived, not caliper-checked |
| X-62 | frame outer Z max | 37.65 | mm | 37.65 | — | #6 params.json | params.json:fz1 | table | scan-derived, not caliper-checked |
| X-63 | sheet thickness | 3.1 | mm | 3.1 | — | #6 params.json | params.json:ft | table | hidden/estimated geometry, not caliper-checked |
| X-64 | outer bend radius | 4.5 | mm | 4.5 | — | #6 params.json | params.json:fr_out | table | hidden/estimated geometry, not caliper-checked |
| X-65 | front-edge notch half-width (notch_y) | 3.3 | mm | 3.3 | — | #6 params.json | params.json:notch_y | table | scan-derived, not caliper-checked; README states notch width 6.6mm = 2x notch_y |
| X-66 | front-edge notch X position | 22.4 | mm | 22.4 | — | #6 params.json | params.json:notch_x | table | scan-derived, not caliper-checked |
| X-67 | front-edge notch Z position | -6.75 | mm | -6.75 | — | #6 params.json | params.json:notch_z | table | scan-derived, not caliper-checked |
| X-68 | front-plate U-slot width | 2.6 | mm | 2.6 | — | #6 params.json | params.json:slot_front_w | table | scan-derived, not caliper-checked |
| X-69 | front-plate U-slot Y0 | 11.5 | mm | 11.5 | — | #6 params.json | params.json:slot_front_y0 | table | scan-derived, not caliper-checked |
| X-70 | rear-plate U-pocket width | 4.2 | mm | 4.2 | — | #6 params.json | params.json:rear_slot_w | table | scan-derived, not caliper-checked |
| X-71 | rear-plate U-pocket Y0 | 12 | mm | 12 | — | #6 params.json | params.json:rear_slot_y0 | table | scan-derived, not caliper-checked |
| X-72 | rear-plate U-pocket depth | 0.85 | mm | 0.85 | — | #6 params.json | params.json:rear_slot_depth | table | scan-derived, not caliper-checked |
| X-73 | diamond flange hub radius (dia_r_center) | 12.05 | mm | 12.05 | — | #6 params.json | params.json:dia_r_center | table | scan-derived, not caliper-checked; README states hub Ø24.1 (r=12.05, matches) |
| X-74 | diamond flange lobe radius | 3.9 | mm | 3.9 | — | #6 params.json | params.json:dia_lobe_r | table | scan-derived, not caliper-checked |
| X-75 | diamond flange lobe X offset | 19.2 | mm | 19.2 | — | #6 params.json | params.json:dia_lobe_x | table | scan-derived, not caliper-checked |
| X-76 | diamond flange z0 | -12.4 | mm | -12.4 | — | #6 params.json | params.json:dia_z0 | table | scan-derived, not caliper-checked |
| X-77 | diamond flange z1 | -18.7 | mm | -18.7 | — | #6 params.json | params.json:dia_z1 | table | scan-derived, not caliper-checked |
| X-78 | flange pocket rim width (pocket_rim) | 1.2 | mm | 1.2 | — | #6 params.json | params.json:pocket_rim | table | hidden/estimated geometry, not caliper-checked; README separately states pocket is '2.2-deep', no matching 2.2 param found — see §4 |
| X-79 | flange pocket boss radius | 5.1 | mm | 5.1 | — | #6 params.json | params.json:boss_r | table | hidden/estimated geometry, not caliper-checked |
| X-80 | flange pocket z | -16.5 | mm | -16.5 | — | #6 params.json | params.json:pocket_z | table | hidden/estimated geometry, not caliper-checked |
| X-81 | flange U-window width | 2.4 | mm | 2.4 | — | #6 params.json | params.json:win_w | table | scan-derived, not caliper-checked |
| X-82 | flange U-window Y position | 10.3 | mm | 10.3 | — | #6 params.json | params.json:win_y | table | scan-derived, not caliper-checked |
| X-83 | flange U-window z0 | -16.9 | mm | -16.9 | — | #6 params.json | params.json:win_z0 | table | scan-derived, not caliper-checked |
| X-84 | flange U-window z1 | -13.8 | mm | -13.8 | — | #6 params.json | params.json:win_z1 | table | scan-derived, not caliper-checked |
| X-85 | flange screw 1 centre X | 19 | mm | 19 | — | #6 params.json | params.json:screw_centers[0][0] | table | scan-derived, not caliper-checked |
| X-86 | flange screw 1 centre Y | -0.3 | mm | -0.3 | — | #6 params.json | params.json:screw_centers[0][1] | table | scan-derived, not caliper-checked |
| X-87 | flange screw 2 centre X | -19.2 | mm | -19.2 | — | #6 params.json | params.json:screw_centers[1][0] | table | scan-derived, not caliper-checked |
| X-88 | flange screw 2 centre Y | 0.15 | mm | 0.15 | — | #6 params.json | params.json:screw_centers[1][1] | table | scan-derived, not caliper-checked |
| X-89 | flange screw dome radius | 3.85 | mm | 3.85 | — | #6 params.json | params.json:screw_r | table | scan-derived, not caliper-checked; README states screw dome Ø7.7 (r=3.85, matches) |
| X-90 | flange screw z1 (dome top) | -21.9 | mm | -21.9 | — | #6 params.json | params.json:screw_z1 | table | scan-derived, not caliper-checked |
| X-91 | screw-head recess angle 1 | 70 | deg | 70 | — | #6 params.json | params.json:recess_ang[0] | table | cosmetic/internal detail, approximated per README |
| X-92 | screw-head recess angle 2 | 60 | deg | 60 | — | #6 params.json | params.json:recess_ang[1] | table | cosmetic/internal detail, approximated per README |
| X-93 | screw-head recess width | 1.3 | mm | 1.3 | — | #6 params.json | params.json:recess_w | table | cosmetic/internal detail, approximated per README |
| X-94 | screw-head recess length | 4.6 | mm | 4.6 | — | #6 params.json | params.json:recess_l | table | cosmetic/internal detail, approximated per README |
| X-95 | screw-head recess z | -20.3 | mm | -20.3 | — | #6 params.json | params.json:recess_z | table | cosmetic/internal detail, approximated per README |
| X-96 | terminal block X0 | -23.05 | mm | -23.05 | — | #6 params.json | params.json:tb_x0 | table | scan-derived, not caliper-checked |
| X-97 | terminal block X1 | 22.65 | mm | 22.65 | — | #6 params.json | params.json:tb_x1 | table | scan-derived, not caliper-checked; README states block width 45.7mm = tb_x1-tb_x0 (matches) |
| X-98 | terminal block Y0 | -31.4 | mm | -31.4 | — | #6 params.json | params.json:tb_y0 | table | scan-derived, not caliper-checked |
| X-99 | terminal block Y-step | -22.3 | mm | -22.3 | — | #6 params.json | params.json:tb_ystep | table | scan-derived, not caliper-checked |
| X-100 | terminal block Y1 | -9 | mm | -9 | — | #6 params.json | params.json:tb_y1 | table | scan-derived, not caliper-checked; README states block depth 22.4mm = tb_y1-tb_y0 (matches) |
| X-101 | terminal block Z0 | -9.4 | mm | -9.4 | — | #6 params.json | params.json:tb_z0 | table | scan-derived, not caliper-checked |
| X-102 | terminal block Z0b | -8.85 | mm | -8.85 | — | #6 params.json | params.json:tb_z0b | table | scan-derived, not caliper-checked |
| X-103 | terminal block Z1 | -3.3 | mm | -3.3 | — | #6 params.json | params.json:tb_z1 | table | scan-derived, not caliper-checked; README states block height ~6mm; ~ tb_z0 to tb_z1 give height 6.1mm |
| X-104 | terminal block Z1b | -3.3 | mm | -3.3 | — | #6 params.json | params.json:tb_z1b | table | scan-derived, not caliper-checked |
| X-105 | terminal block step X1 | 3 | mm | 3 | — | #6 params.json | params.json:tb_step_x1 | table | scan-derived, not caliper-checked |
| X-106 | terminal block step Y1 | -26.5 | mm | -26.5 | — | #6 params.json | params.json:tb_step_y1 | table | scan-derived, not caliper-checked |
| X-107 | terminal block step Z | -3.78 | mm | -3.78 | — | #6 params.json | params.json:tb_step_z | table | scan-derived, not caliper-checked |
| X-108 | terminal block fillet radius | 1.5 | mm | 1.5 | — | #6 params.json | params.json:tb_fillet | table | scan-derived, not caliper-checked |
| X-109 | tab pocket Y1 | -29.6 | mm | -29.6 | — | #6 params.json | params.json:tabpk_y1 | table | cosmetic/internal detail, approximated per README |
| X-110 | tab pocket Z0 | -6.35 | mm | -6.35 | — | #6 params.json | params.json:tabpk_z0 | table | cosmetic/internal detail, approximated per README |
| X-111 | spade tab Y0 | -30.95 | mm | -30.95 | — | #6 params.json | params.json:tab_y0 | table | cosmetic/internal detail, approximated per README |
| X-112 | spade tab Y1 | -30.15 | mm | -30.15 | — | #6 params.json | params.json:tab_y1 | table | cosmetic/internal detail, approximated per README; README states tabs 6.5x0.8mm — tab_y1-tab_y0=0.8mm matches thickness |
| X-113 | spade tab Z1 | 5.5 | mm | 5.5 | — | #6 params.json | params.json:tab_z1 | table | cosmetic/internal detail, approximated per README |
| X-114 | spade tab A position X | -18.4 | mm | -18.4 | — | #6 params.json | params.json:tabA[0] | table | cosmetic/internal detail, approximated per README |
| X-115 | spade tab A position Y | -11.9 | mm | -11.9 | — | #6 params.json | params.json:tabA[1] | table | cosmetic/internal detail, approximated per README |
| X-116 | spade tab B position X | -5.6 | mm | -5.6 | — | #6 params.json | params.json:tabB[0] | table | cosmetic/internal detail, approximated per README |
| X-117 | spade tab B position Y | 0.8 | mm | 0.8 | — | #6 params.json | params.json:tabB[1] | table | cosmetic/internal detail, approximated per README; tabA-tabB spacing does not obviously equal README's 6.5mm tab length — see §4 |
| X-118 | inclined rib X range start | -10.2 | mm | -10.2 | — | #6 params.json | params.json:rib_x[0] | table | scan-derived, not caliper-checked |
| X-119 | inclined rib X range end | -8.6 | mm | -8.6 | — | #6 params.json | params.json:rib_x[1] | table | scan-derived, not caliper-checked |
| X-120 | slot box centre X (hs_cx) | 12.89 | mm | 12.89 | — | #6 params.json | params.json:hs_cx | table | scan-derived, not caliper-checked |
| X-121 | slot box centre Y (hs_cy) | -22.59 | mm | -22.59 | — | #6 params.json | params.json:hs_cy | table | scan-derived, not caliper-checked |
| X-122 | slot box rotation angle | 29.6 | deg | 29.6 | — | #6 params.json | params.json:hs_ang | table | scan-derived, not caliper-checked; README states slot box rotated 29.6° (matches) |
| X-123 | slot box length | 11.5 | mm | 11.5 | — | #6 params.json | params.json:hs_l | table | scan-derived, not caliper-checked |
| X-124 | slot box width | 5 | mm | 5 | — | #6 params.json | params.json:hs_w | table | scan-derived, not caliper-checked |
| X-125 | slot box Z1 | 13.6 | mm | 13.6 | — | #6 params.json | params.json:hs_z1 | table | scan-derived, not caliper-checked |
| X-126 | slot box fillet radius | 0.9 | mm | 0.9 | — | #6 params.json | params.json:hs_fillet | table | scan-derived, not caliper-checked |
| X-127 | datum bbox min X | -27.2 | mm | -27.2 | — | #8 export_check.json | export_check.json:exports.datum.bbox_min[0] | table | — |
| X-128 | datum bbox min Y | -31.4 | mm | -31.4 | — | #8 export_check.json | export_check.json:exports.datum.bbox_min[1] | table | — |
| X-129 | datum bbox min Z | -66.45 | mm | -66.45 | — | #8 export_check.json | export_check.json:exports.datum.bbox_min[2] | table | — |
| X-130 | datum bbox max X | 26.85 | mm | 26.85 | — | #8 export_check.json | export_check.json:exports.datum.bbox_max[0] | table | — |
| X-131 | datum bbox max Y | 23.75 | mm | 23.75 | — | #8 export_check.json | export_check.json:exports.datum.bbox_max[1] | table | — |
| X-132 | datum bbox max Z | 55.5 | mm | 55.5 | — | #8 export_check.json | export_check.json:exports.datum.bbox_max[2] | table | — |
| X-133 | solid volume | 114903 | mm^3 | 114903 | — | #8 export_check.json | export_check.json:exports.datum.volume_mm3 | table | — |
| X-134 | surface area | 29258.9 | mm^2 | 29258.9 | — | #8 export_check.json | export_check.json:exports.datum.area_mm2 | table | — |
| X-135 | face count | 213 | count | 213 | — | #8 export_check.json | export_check.json:exports.datum.faces | table | — |
| X-136 | solid count | 1 | count | 1 | — | #8 export_check.json | export_check.json:exports.datum.solids | table | — |
| X-137 | expected bbox X | 54.05 | mm | 54.05 | ±0.3mm | #7 expected.json | expected.json:bbox_mm.x | table | — |
| X-138 | expected bbox Y | 55.2 | mm | 55.2 | ±0.5mm | #7 expected.json | expected.json:bbox_mm.y | table | conflicts with X-## export_check bbox Y 55.15mm and validator measured 55.15mm — see §4 |
| X-139 | expected bbox Z | 121.95 | mm | 121.95 | ±0.5mm | #7 expected.json | expected.json:bbox_mm.z | table | — |
| X-140 | validator measured bbox X | 54.05 | mm | 54.05 | — | #9 validator_report.json | validator_report.json:measured.bbox_mm[0] | table | — |
| X-141 | validator measured bbox Y | 55.15 | mm | 55.15 | — | #9 validator_report.json | validator_report.json:measured.bbox_mm[1] | table | conflicts with expected.json bbox Y 55.2mm — see §4 |
| X-142 | validator measured bbox Z | 121.95 | mm | 121.95 | — | #9 validator_report.json | validator_report.json:measured.bbox_mm[2] | table | — |
| X-143 | deviation scan→CAD RMS | 0.217446 | mm | 0.217446 | — | #10 deviation_gate.json | deviation_gate.json:scan_to_cad.rms | table | — |
| X-144 | deviation scan→CAD p95 | 0.447768 | mm | 0.447768 | — | #10 deviation_gate.json | deviation_gate.json:scan_to_cad.p95 | table | README: consumer-plastic band (p95≤0.30) not met |
| X-145 | deviation scan→CAD p99 | 0.674489 | mm | 0.674489 | — | #10 deviation_gate.json | deviation_gate.json:scan_to_cad.p99 | table | — |
| X-146 | deviation scan→CAD max | 2.4934 | mm | 2.4934 | — | #10 deviation_gate.json | deviation_gate.json:scan_to_cad.max | table | README: consumer-plastic band (max≤0.80) not met |
| X-147 | deviation scan→CAD mean | 0.151842 | mm | 0.151842 | — | #10 deviation_gate.json | deviation_gate.json:scan_to_cad.mean | table | — |
| X-148 | deviation CAD→scan (all surfaces) RMS | 1.60754 | mm | 1.60754 | — | #10 deviation_gate.json | deviation_gate.json:cad_to_scan.rms | table | includes unobservable surfaces per README |
| X-149 | deviation CAD→scan (all surfaces) p95 | 3.43028 | mm | 3.43028 | — | #10 deviation_gate.json | deviation_gate.json:cad_to_scan.p95 | table | includes unobservable surfaces per README |
| X-150 | deviation CAD→scan (all surfaces) p99 | 5.45262 | mm | 5.45262 | — | #10 deviation_gate.json | deviation_gate.json:cad_to_scan.p99 | table | includes unobservable surfaces per README |
| X-151 | deviation CAD→scan (all surfaces) max | 9.02691 | mm | 9.02691 | — | #10 deviation_gate.json | deviation_gate.json:cad_to_scan.max | table | includes unobservable surfaces per README |
| X-152 | deviation CAD→scan (all surfaces) mean | 0.874023 | mm | 0.874023 | — | #10 deviation_gate.json | deviation_gate.json:cad_to_scan.mean | table | includes unobservable surfaces per README |
| X-153 | regional deviation p95, outlet tube (z<-24.5) | 0.389445 | mm | 0.389445 | — | #10 deviation_gate.json | deviation_gate.json:scan_to_cad_regions.outlet_tube | table | README rounds to 0.39mm |
| X-154 | regional deviation p95, front body/flange (-24.5..-9.6) | 0.488649 | mm | 0.488649 | — | #10 deviation_gate.json | deviation_gate.json:scan_to_cad_regions.front_body | table | README rounds to 0.49mm |
| X-155 | regional deviation p95, coil+frame (-9.6..37.7) | 0.445095 | mm | 0.445095 | — | #10 deviation_gate.json | deviation_gate.json:scan_to_cad_regions.coil+frame | table | README rounds to 0.45mm |
| X-156 | regional deviation p95, inlet fitting (z>=37.7) | 0.272859 | mm | 0.272859 | — | #10 deviation_gate.json | deviation_gate.json:scan_to_cad_regions.inlet | table | README rounds to 0.27mm |
| X-157 | CAD→scan p95, scanner-observable surfaces only | 0.567108 | mm | 0.567108 | — | #10 deviation_gate.json | deviation_gate.json:cad_to_scan_observable.p95 | table | — |
| X-158 | CAD→scan max, scanner-observable surfaces only | 8.64805 | mm | 8.64805 | — | #10 deviation_gate.json | deviation_gate.json:cad_to_scan_observable.max | table | — |
| X-159 | fraction of CAD surface unobservable to scanner | 0.2565 | fraction | 0.2565 | — | #10 deviation_gate.json | deviation_gate.json:cad_to_scan_unobservable_fraction | table | README states 25.6% |

<!--
Method: text · table · drawing callout · title block · scaled from drawing ·
photo · message. Flags: photo or scaled, not confirmable for fit · conflicts
with X-## · unit assumed · illegible.
-->

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-160 | material: PETG | "OD-C03,OD-C00,PRINT,Pump cradle (sleeve + spring suspension),,,1,DESIGN,PETG,printed,print,#1,proposed" (material_spec column) | #4 bom_rows.csv | row OD-C03 |
| X-161 | process: printed | "OD-C03,OD-C00,PRINT,...,DESIGN,PETG,printed,print,#1,proposed" (type=PRINT, source=printed) | #4 bom_rows.csv | row OD-C03 |
| X-162 | quantity: 1 | "OD-C03,...,1,DESIGN,PETG,..." (qty column) | #4 bom_rows.csv | row OD-C03 |
| X-163 | mounting concept: rubber sleeve + spring, copy the OEM concept | "the Dedica suspends the pump in a rubber sleeve + spring to damp vibration... Copy the OEM mounting concept in the printed chassis." | #3 PROJECT_RULES.md | docs/SOURCING_GUIDE.md §3.1, Chassis note |
| X-164 | rigid mount fails: vibration | "The thesis's first rigid printed pump mount produced \"unacceptable levels of vibration\"; the second iteration replicated the OEM sleeve-and-spring suspension and fixed it." | #3 PROJECT_RULES.md | docs/SOURCING_GUIDE.md §3.1, Chassis note |
| X-165 | wet/electric separation | "Keep the wet side separated from the electric side, keep the 192 °C thermal cutoff (TCO) in circuit, test behind an RCD/GFCI, and never print load-bearing or heat-adjacent parts in PLA." | #3 PROJECT_RULES.md | README.md safety note |
| X-166 | never PLA for load-bearing/heat-adjacent parts | "never print load-bearing or heat-adjacent parts in PLA" | #3 PROJECT_RULES.md | README.md safety note |
| X-167 | ≥10 mm air gap rule (stated for thermoblock, applicability to pump cradle unconfirmed — see §4) | "Keep ≥10 mm air gap to any printed part, mount it on its OEM bracket geometry, and use ABS/ASA/PC (not PETG, never PLA) for anything within radiant range." | #3 PROJECT_RULES.md | docs/SOURCING_GUIDE.md §3.2, Chassis note (thermoblock) |
| X-168 | order-of-work: OD-C03 designed against OD-H01; sleeve OD-H02 and spring OD-H03 blocked by "not scanned (calipers)" | "3 \| `OD-C03` pump cradle \| OD-H01; sleeve OD-H02 and spring OD-H03 \| H02/H03 not scanned (calipers)" | #3 PROJECT_RULES.md | chassis/README.md, Order of work table row 3 |
| X-169 | order-of-work general rule: a part whose OEM neighbour is not scanned carries it as an assumption row and is revisited when the scan lands | "Each part is designed against the scanned OEM parts it touches. A part whose OEM neighbour is not scanned yet carries that neighbour as an assumption row and is revisited when the scan lands." | #3 PROJECT_RULES.md | chassis/README.md, Order of work |
| X-170 | deliverables per part: parametric build script, STEP, STL/3MF, print orientation and material stated | "one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated" | #3 PROJECT_RULES.md | chassis/README.md, Goal |
| X-171 | standing instruction: parametric build script, STEP, STL/3MF and an independent review verdict for every part | "each part needs a parametric build script, STEP, STL/3MF and an independent review verdict" | #2 REQUEST.md | standing instruction, project instructions 2026-09-30 |
| X-172 | every scan/report value is an A-## assumption until the Usta confirms it | "every value from a scan or report is an A-## assumption until the Usta confirms it" | #2 REQUEST.md | standing instruction, project instructions 2026-09-30 |
| X-173 | calipers beat scans | "calipers beat scans" | #2 REQUEST.md | standing instruction, project instructions 2026-09-30 |
| X-174 | a fit-critical value cannot be confirmed from an image | "a fit-critical value cannot be confirmed from an image" | #2 REQUEST.md | standing instruction, project instructions 2026-09-30 |
| X-175 | data class: PUBLIC (CC BY 4.0) | "data class PUBLIC (CC BY 4.0)" | #2 REQUEST.md | standing instruction, project instructions 2026-09-30 |
| X-176 | OD-C01 (base frame) not designed yet; the cradle's mounting interface to it is this job's design choice, recorded as an assumption for OD-C01 to follow | "OD-C01 (base frame) is not designed yet: the cradle's mounting interface to it is a design choice of this job, recorded as an assumption for OD-C01 to follow." | #2 REQUEST.md | job note, 2026-09-30 |
| X-177 | H02/H03 not scanned; carried as assumption rows, part revisited when scans land | "the rubber pump protector OD-H02 and the suspension spring OD-H03 are not scanned (chassis/README.md order-of-work row 3: \"H02/H03 not scanned (calipers)\"), so they are carried as assumption rows and the part is revisited when their scans land." | #2 REQUEST.md | job note, 2026-09-30 |
| X-178 | fastener: M3 heat-set insert, ~40 qty, brass M3, chassis-wide (OD-000 parent) | "OD-F01,OD-000,STD,M3 heat-set insert,,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo" | #4 bom_rows.csv | row OD-F01 |
| X-179 | fastener: M3×8 screw, ~40 qty, ISO 7380 / DIN 912 A2, chassis-wide (OD-000 parent) | "OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo" | #4 bom_rows.csv | row OD-F02 |
| X-180 | OD-H02 (rubber sleeve): SCAN method column shows "SCAN" but no scan exists yet; material rubber; source AliExpress/FixPart; price 4 EUR | "OD-H02,OD-H00,OEM,Pump protector (rubber sleeve),41,5213211161,1,SCAN,rubber,AliExpress / FixPart,4,#1,todo" | #4 bom_rows.csv | row OD-H02 |
| X-181 | OD-H03 (suspension spring): CAD method column shows "CALIPER"; material steel; source FixPart/4delonghi; price 3 EUR | "OD-H03,OD-H00,OEM,Pump suspension spring,42,6113210761,1,CALIPER,steel,FixPart / 4delonghi,3,#1,todo" | #4 bom_rows.csv | row OD-H03 |
| X-182 | single-body caveat: coil, frame, plastic body, screws and spades are fused into one solid in OD-H01's STEP (no sub-body split) | "Single body: coil, frame, plastic body, screws and spades are fused into one solid. A multi-body STEP would be a separate task." | #5 README.md | Assumptions to verify |
| X-183 | validator is a consistency check only, not independent evidence; the deviation gate is the independent evidence | "The validator (13/13 PASS) compares against scan-derived expectations — a consistency check, not independent evidence. The deviation gate is the independent evidence." | #5 README.md | Assumptions to verify |
| X-184 | mating features (spigots, flange, terminals) must be confirmed with calipers before OD-C03 is frozen | "Good enough for chassis envelope and pump-cradle design. Mating features (spigots, flange, terminals) must be confirmed with calipers before the cradle (`OD-C03`) is frozen." | #5 README.md | Deviation gate section |
| X-185 | scale assumption: STL assumed mm (122 mm length matches ULKA EX5 datasheet), not caliper-checked | "Scale: STL assumed mm (122 mm length matches ULKA EX5 datasheet) — not caliper-checked." | #5 README.md | Assumptions to verify |
| X-186 | scan does not include OD-H02 (rubber protector) or OD-H03 (spring); they still need their own scan/calipers | "Pump only — the rubber protector sleeve (OD-H02) and spring (OD-H03) are not in this scan; they still need their own scan / calipers for #1." | #12 README.md (scan) | Known mesh defects |
| X-187 | outlet spigot surface noisy; take its diameter and thread from calipers | "The outlet spigot surface is noisy; take its diameter and thread from calipers." | #12 README.md (scan) | Known mesh defects |
| X-188 | caliper sheet not yet filled: coil housing, inlet spigot, outlet spigot/thread, body flange, spade terminals, overall length, EP5 vs EX5 all blank | "1 \| Coil housing Ø / length \| \| ... 7 \| EP5 (plastic outlet) or EX5 (brass outlet)? \| \|" (all value cells empty) | #13 calipers.md | rows 1-7 |

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-128, X-131, X-138, X-141 | expected.json's bbox_mm.y is 55.2 mm (±0.5 mm) but export_check.json's datum bbox min Y (-31.4) to max Y (23.75) spans 55.15 mm, and validator_report.json's measured bbox also gives 55.15 mm: which value (or is 55.15 simply inside the ±0.5 mm band of 55.2, so no conflict) governs the cradle's Y clearance? |
| 2 | X-52, X-53, README §Model tree item 2 | README's model tree states the coil centre is "0.2 mm off-axis (measured, not snapped)" as a single figure, but params.json gives two components, coil_cx = -0.2 mm and coil_cy = 0.1 mm (vector magnitude ≈0.224 mm): which is the intended value for the cradle's coil-bore clearance — the prose 0.2 mm, or the vector from the two components? |
| 3 | X-78 (pocket_rim), README §Model tree item 5 | README states the diamond-flange pocket is "2.2-deep" but no params.json key equals 2.2 (pocket_rim = 1.2 mm, dia_z0 to dia_z1 span = 6.3 mm, pocket_z = -16.5 mm); which params.json key (if any) is the pocket depth README calls out, or is it missing from the exported parameter set? |
| 4 | X-111, X-112, X-114–X-117 (tab_y0, tab_y1, tabA, tabB), README §Model tree item 6 | README states the spade tabs are "6.5 × 0.8" but params.json's tabA (-18.4, -11.9) to tabB (-5.6, 0.8) span does not obviously reduce to a 6.5 mm tab length (tab_y1 - tab_y0 = 0.8 mm matches the thickness); what is the correct spade-tab length, and does the cradle need clearance around both tabs or just their pocket? |
| 5 | X-01–X-159 (all params.json/export_check.json/expected.json rows), X-184 | The deviation gate's own verdict is that the consumer-plastic band (p95 ≤ 0.30 mm, max ≤ 0.80 mm) is not met (X-144 p95 0.448 mm, X-146 max 2.49 mm), and README (X-184) says mating features (spigots, flange, terminals) must be confirmed with calipers before OD-C03 is frozen, yet calipers.md (file #13) is entirely empty. Can the cradle's build script proceed on the scan-derived params.json values as A-## assumptions, or must calipers land first for every mating feature before any geometry is cut? |
| 6 | (gap, no rows exist) | OD-H02 (rubber pump protector / sleeve): no dimensions exist anywhere in the inputs (ID, OD, wall thickness, free length, durometer/material spec beyond "rubber"). Which section of the pump does it wrap (coil per X-53/X-54, body per X-27, or both), and does it sit between pump and cradle bore, or between pump and a separate sleeve-retaining feature of the cradle? |
| 7 | (gap, no rows exist) | OD-H03 (suspension spring): no dimensions exist anywhere in the inputs (free length, wire diameter, coil diameter, spring rate) beyond "steel" (X-181). Which end of the spring is fixed to the pump/sleeve and which to the cradle/frame, and along which axis does it act (axial along pump Z, radial, or both)? |
| 8 | (gap) | OD-C01 (base frame) is not designed yet (X-176). What mounting interface (screw pattern, spigot, snap feature) should OD-C03 expose for OD-C01 to follow, given no OD-C01 geometry exists to design against yet? |
| 9 | X-167 | The ≥10 mm air gap rule is stated in PROJECT_RULES.md only for the thermoblock (heat-adjacent parts, X-167 location: docs/SOURCING_GUIDE.md §3.2). Does this clearance rule also apply to OD-C03 around the pump (which is not a heat source, only a vibration source), or is it thermoblock-specific and inapplicable here? |
| 10 | X-178, X-179 | bom_rows.csv's M3 heat-set insert (OD-F01) and M3×8 screw (OD-F02) rows are parented to OD-000 (whole assembly), not to OD-C03 specifically, and no qty or fastener count is assigned to this part. Are these the fasteners intended for the cradle-to-OD-C01 joint and/or the cradle's own flange-screw retention, or generic chassis-wide stock not yet allocated to any specific joint? |
| 11 | X-188 | calipers.md (file #13) is a template with all 7 rows blank, including row 7 "EP5 (plastic outlet) or EX5 (brass outlet)?". bom_rows.csv (X-160 source row) and REQUEST.md both call the part "ULKA EP5/EX5" without settling which variant was scanned. Does the scanned OD-H01 represent the EP5 (plastic outlet, per SOURCING_GUIDE default) or the EX5 (brass outlet) variant, and does that choice change any outlet-side dimension (X-01–X-23) the cradle must clear? |

## §5 Unreadable

None. All 13 listed inputs were read in full (the STEP file, #1, was listed and hashed only per intake rule 6; its geometry is measured later with `tools/measure`, not read here).
