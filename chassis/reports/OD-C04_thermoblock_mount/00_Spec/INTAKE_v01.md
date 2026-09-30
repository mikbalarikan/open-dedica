# INTAKE v01 — 20260930-od-c04-thermoblock-mount

Intake: Claude Code, Claude Sonnet 5 · data class PUBLIC · brief `briefs/WP-01_intake.md` · 2026-09-30 UTC

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
| 1 | 00_Spec/inputs/OD-H11_thermoblock.step | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038f | 2400893 | STEP (CAD) | 1 solid | hashed only (rule 6; geometry measured later with tools/measure) |
| 2 | 00_Spec/inputs/REQUEST.md | 8d2d1e43a785ffe2780ba3362386a82661d792f146acfcaf0d2b29040f7f0f9 | 1225 | Markdown | 1 | full text |
| 3 | 00_Spec/inputs/PROJECT_RULES.md | 97e1cf7097e8b8b57c4e99cd796a080a519f58904f6038ad8a023ef0ecc3970 | 6787 | Markdown | 1 (3 excerpted sources) | full text |
| 4 | 00_Spec/inputs/bom_rows.csv | b594e276d2bbeb6466241f47380f8e75abd4cf703e7c1f01aa61dc9922c6974 | 1621 | CSV | 17 rows | full text |
| 5 | 00_Spec/inputs/reports/OD-H11_thermoblock/README.md | 61061c517ac0c20dfe1fa86a5e75dbf959eb52d272a843b2c613d77da4dddec | 5385 | Markdown | 1 | full text |
| 6 | 00_Spec/inputs/reports/OD-H11_thermoblock/params.json | 46f1b43a54e82c08a96b2463d88622e9d5a5ae71245ccc3440c1d960ba1c520 | 7091 | JSON | 1 (50 top-level keys) | full text |
| 7 | 00_Spec/inputs/reports/OD-H11_thermoblock/export_check.json | ecba71c6aebb34c59dd7bcb61d67f09662d07954a724ae3729171bc1fc547a7 | 1326 | JSON | 1 | full text |
| 8 | 00_Spec/inputs/reports/OD-H11_thermoblock/deviation_report.json | 8208319ab4e1d36140855558ea6681d27db04dce0005f16410e51da9bb989ff | 2663 | JSON | 1 | full text |
| 9 | 00_Spec/inputs/reports/OD-H11_thermoblock/ports.json | 77fbb8b2a53e929216ddea4752a7b18e67f6f57ba1ba3864ec24e179cf224fd | 3865 | JSON | 1 (2 pipes, 2 terminals) | full text |
| 10 | 00_Spec/inputs/scan/OD-H11_thermoblock/README.md | 71737a61742eef1ef2ac7f36ece62e62ae96a305fe80206efe94c6c3c1eaa75 | 1156 | Markdown | 1 | full text |
| 11 | 00_Spec/inputs/scan/OD-H11_thermoblock/calipers.md | 761d29432f8db6afe181247b16b8f23a7c5a1033a394dd5a81e3c12ae623c44 | 536 | Markdown | 1 (table empty) | full text |

## §2 Dimensions

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-01 | coneA | [33.78, 34.95] | mm | 33.78 -> 34.95 | - | #6 | coneA | params.json key | scan-derived, not caliper-confirmed |
| X-02 | coneB | [34.97, 33.85] | mm | 34.97 -> 33.85 | - | #6 | coneB | params.json key | scan-derived, not caliper-confirmed |
| X-03 | sectorB | [69.0, 172.0] | deg | 69.0 -> 172.0 | - | #6 | sectorB | params.json key | scan-derived, not caliper-confirmed |
| X-04 | body_chamfer_bottom | 0.5 | mm | 0.5 | - | #6 | body_chamfer_bottom | params.json key | scan-derived, not caliper-confirmed |
| X-05 | body_chamfer_top | 0.4 | mm | 0.4 | - | #6 | body_chamfer_top | params.json key | scan-derived, not caliper-confirmed |
| X-06 | bore_bottom_chamfer | 1.3 | mm | 1.3 | - | #6 | bore_bottom_chamfer | params.json key | scan-derived, not caliper-confirmed |
| X-07 | z_web0 | 34.5 | mm | 34.5 | - | #6 | z_web0 | params.json key | scan-derived, not caliper-confirmed |
| X-08 | z_web1 | 37.8 | mm | 37.8 | - | #6 | z_web1 | params.json key | scan-derived, not caliper-confirmed |
| X-09 | d_web_hole | 6.0 | mm dia | 6.0 | - | #6 | d_web_hole | params.json key | scan-derived, not caliper-confirmed |
| X-10 | web_hole_chamfer | 0.6 | mm | 0.6 | - | #6 | web_hole_chamfer | params.json key | scan-derived, not caliper-confirmed |
| X-11 | r_cb_floor | 14.13 | mm | 14.13 | - | #6 | r_cb_floor | params.json key | scan-derived, not caliper-confirmed |
| X-12 | r_cb_top | 14.99 | mm | 14.99 | - | #6 | r_cb_top | params.json key | scan-derived, not caliper-confirmed |
| X-13 | cb_top_chamfer | 1.3 | mm | 1.3 | - | #6 | cb_top_chamfer | params.json key | scan-derived, not caliper-confirmed |
| X-14 | groove_r | 4.25 | mm | 4.25 | - | #6 | groove_r | params.json key | scan-derived, not caliper-confirmed |
| X-15 | groove_pitch | 36.75 | mm | 36.75 | - | #6 | groove_pitch | params.json key | scan-derived, not caliper-confirmed |
| X-16 | grooves | [[9.8,0.0,35.3],[49.8,0.0,35.3],[189.4,0.0,42.4]] | deg / mm | theta 9.8,49.8,189.4; z 35.3,35.3,42.4 | - | #6 | grooves | params.json key | scan-derived, not caliper-confirmed |
| X-17 | pin_pcd_r | 25.0 | mm (radius) | 25.0 (r); diam 50.0 | - | #6 | pin_pcd_r | params.json key | scan-derived, not caliper-confirmed |
| X-18 | pin_angles | [9.1, 129.1, 249.1] | deg | 9.1, 129.1, 249.1 | - | #6 | pin_angles | params.json key | scan-derived, not caliper-confirmed |
| X-19 | pin_d0 | 3.9 | mm dia | 3.9 | - | #6 | pin_d0 | params.json key | scan-derived, not caliper-confirmed |
| X-20 | pin_d1 | 3.35 | mm dia | 3.35 | - | #6 | pin_d1 | params.json key | scan-derived, not caliper-confirmed |
| X-21 | pin_top | 50.79 | mm (z) | 50.79 | - | #6 | pin_top | params.json key | scan-derived, not caliper-confirmed |
| X-22 | pad_profile | polyline, 20 (u,v) points, R30.0/35.05/36.25/39.4 radii, z 0-47.64 | mm | see value as given | - | #6 | pad_profile | params.json key | scan-derived, not caliper-confirmed |
| X-23 | padA | theta 262.5; left/right edges; notch_v [-3.65,1.55]; notch_u 33.0; hole_u [33.0,37.4] | deg / mm | see value as given | - | #6 | padA | params.json key | scan-derived, not caliper-confirmed |
| X-24 | padB | theta 339.0; left/right_block/right_rib edges; notch_v [-4.45,0.5]; notch_u 32.45; hole_u [33.0,37.4] | deg / mm | see value as given | - | #6 | padB | params.json key | scan-derived, not caliper-confirmed |
| X-25 | pad_notch_z | [[0.0,3.5],[44.3,47.64]] | mm | 0.0-3.5, 44.3-47.64 | - | #6 | pad_notch_z | params.json key | scan-derived, not caliper-confirmed |
| X-26 | pad_hole_z | [[3.5,6.2],[41.4,44.3]] | mm | 3.5-6.2, 41.4-44.3 | - | #6 | pad_hole_z | params.json key | scan-derived, not caliper-confirmed |
| X-27 | flatB | theta 339.0; poly 6 pts; z [0.5,47.64] | deg / mm | see value as given | - | #6 | flatB | params.json key | scan-derived, not caliper-confirmed |
| X-28 | side_theta | 107.5 | deg | 107.5 | - | #6 | side_theta | params.json key | scan-derived, not caliper-confirmed |
| X-29 | side_block | z [11.8,27.6]; u_top [40.95,39.95]; poly 7 pts | mm | see value as given | - | #6 | side_block | params.json key | scan-derived, not caliper-confirmed |
| X-30 | side_tab | z [[32.9,38.6],[43.9,47.2]]; poly 9 pts | mm | see value as given | - | #6 | side_tab | params.json key | scan-derived, not caliper-confirmed |
| X-31 | side_tab_slots | z [32.9,38.6]; v [[-7.98,-4.6],[4.0,7.4]]; u0 37.4 | mm | see value as given | - | #6 | side_tab_slots | params.json key | scan-derived, not caliper-confirmed |
| X-32 | side_gaps | 2 entries: z[27.6,32.9] v[-9.45,9.4] u0 33.4; z[38.6,43.9] v[-9.3,9.1] u0 33.15 | mm | see value as given | - | #6 | side_gaps | params.json key | scan-derived, not caliper-confirmed |
| X-33 | top_lug | z [36.3,47.64]; poly 9 pts | mm | see value as given | - | #6 | top_lug | params.json key | scan-derived, not caliper-confirmed |
| X-34 | mid_lug | z [27.6,36.3]; poly 14 pts | mm | see value as given | - | #6 | mid_lug | params.json key | scan-derived, not caliper-confirmed |
| X-35 | pipe_lug | z [0.0,9.5]; poly 18 pts | mm | see value as given | - | #6 | pipe_lug | params.json key | scan-derived, not caliper-confirmed |
| X-36 | pipe_lug_step | z [9.5,11.8]; poly 15 pts | mm | see value as given | - | #6 | pipe_lug_step | params.json key | scan-derived, not caliper-confirmed |
| X-37 | lug_notch | z [0.0,3.2]; poly 12 pts | mm | see value as given | - | #6 | lug_notch | params.json key | scan-derived, not caliper-confirmed |
| X-38 | slot_L | 11.9 | mm | 11.9 | - | #6 | slot_L | params.json key | scan-derived, not caliper-confirmed |
| X-39 | slot_W | 3.6 | mm | 3.6 | - | #6 | slot_W | params.json key | scan-derived, not caliper-confirmed |
| X-40 | top_slots | 3 entries: [[-28.2,-30.46],39.7,40.8]; [[-12.36,11.53],101.9,41.0]; [[2.22,-37.96],113.5,41.6] | mm / deg | see value as given | - | #6 | top_slots | params.json key | scan-derived, not caliper-confirmed |
| X-41 | bottom_slots | 2 entries: [[1.19,10.5],69.3,8.4]; [[8.0,-34.32],129.9,9.2] | mm / deg | see value as given | - | #6 | bottom_slots | params.json key | scan-derived, not caliper-confirmed |
| X-42 | bottom_rect | c[-33.73,-18.16], L4.76, W3.62, ang 9.8deg, r0.8, z1 7.2 | mm / deg | 4.76 x 3.62 | - | #6 | bottom_rect | params.json key | scan-derived, not caliper-confirmed |
| X-43 | bottom_recess_depth | 0.6 | mm | 0.6 | - | #6 | bottom_recess_depth | params.json key | scan-derived, not caliper-confirmed |
| X-44 | bottom_recesses | 4 entries (c, dia): [-28.54,0.51] Ø5.7; [-27.2,-30.05] Ø5.9; [-23.55,10.09] Ø7.9; [-17.34,-37.6] Ø11.4 | mm | Ø5.7, Ø5.9, Ø7.9, Ø11.4 | - | #6 | bottom_recesses | params.json key | scan-derived, not caliper-confirmed |
| X-45 | top_recess_depth | 0.45 | mm | 0.45 | - | #6 | top_recess_depth | params.json key | scan-derived, not caliper-confirmed |
| X-46 | top_recess_circle | c[-31.68,-5.3], Ø11.8 | mm | Ø11.8 | - | #6 | top_recess_circle | params.json key | scan-derived, not caliper-confirmed |
| X-47 | top_label | c[15.43,-23.92], L20.4, W6.4, ang 69.1deg, r1.0 | mm / deg | 20.4 x 6.4 | - | #6 | top_label | params.json key | scan-derived, not caliper-confirmed |
| X-48 | spotface_d | 11.4 | mm dia | 11.4 | - | #6 | spotface_d | params.json key | scan-derived, not caliper-confirmed |
| X-49 | blind_holes | 2 entries: c[25.01,9.08] Ø3.5 z[27.0,33.2]; c[-19.62,20.18] Ø3.6 z[3.0,8.0] | mm | Ø3.5 (depth 6.2), Ø3.6 (depth 5.0) | - | #6 | blind_holes | params.json key | scan-derived, not caliper-confirmed |
| X-50 | lug_top_pocket | c[-35.76,15.55], L3.66, W2.86, ang 43.0deg, z[5.8,10.0] | mm / deg | 3.66 x 2.86 | - | #6 | lug_top_pocket | params.json key | scan-derived, not caliper-confirmed |
| X-51 | Water pipe 1 - anchor position a (datum frame) | [39.321, 27.174, 42.7] | mm | [39.321, 27.174, 42.7] | - | #9 | ports.json > pipes[0].a | json field | scan-derived, not caliper-confirmed |
| X-52 | Water pipe 1 - axis direction d (unit vector) | [-0.35899, -0.93334, 0.0] | unitless | [-0.35899, -0.93334, 0.0] | - | #9 | ports.json > pipes[0].d | json field | scan-derived, not caliper-confirmed |
| X-53 | Water pipe 1 - bore section diameter and length | prof t -3.3 to 9.85 @ r2.5 | mm | Ø5.0, length 13.15 | - | #9 | ports.json > pipes[0].prof | profile (t,r) pairs, r->2r converted | scan-derived, not caliper-confirmed |
| X-54 | Water pipe 1 - collar section diameter and length | prof t 9.85 to 17.9 @ r4.45 | mm | Ø8.9, length 8.05 | - | #9 | ports.json > pipes[0].prof | profile (t,r) pairs, r->2r converted | scan-derived, not caliper-confirmed |
| X-55 | Water pipe 1 - clip flats width and axial range | half_width 2.8, t0 12.15, t1 16.25 | mm | width 5.6, range 12.15-16.25 (length 4.1) | - | #9 | ports.json > pipes[0].clip_flats | 2x half_width converted | scan-derived, not caliper-confirmed |
| X-56 | Water pipe 1 - tip bore diameter and depth | bore_r 1.95, bore_depth 2.3 | mm | Ø3.9, depth 2.3 | - | #9 | ports.json > pipes[0].bore_r/bore_depth | r->2r converted | scan-derived, not caliper-confirmed |
| X-57 | Water pipe 2 - anchor position a (datum frame) | [-16.058, 49.403, 5.3] | mm | [-16.058, 49.403, 5.3] | - | #9 | ports.json > pipes[1].a | json field | scan-derived, not caliper-confirmed |
| X-58 | Water pipe 2 - axis direction d (unit vector) | [-0.35899, -0.93334, 0.0] | unitless | [-0.35899, -0.93334, 0.0] | - | #9 | ports.json > pipes[1].d | json field | scan-derived, not caliper-confirmed |
| X-59 | Water pipe 2 - bore section diameter and length | prof t -3.3 to 9.85 @ r2.5 | mm | Ø5.0, length 13.15 | - | #9 | ports.json > pipes[1].prof | profile (t,r) pairs, r->2r converted | scan-derived, not caliper-confirmed |
| X-60 | Water pipe 2 - collar section diameter and length | prof t 9.85 to 17.9 @ r4.45 | mm | Ø8.9, length 8.05 | - | #9 | ports.json > pipes[1].prof | profile (t,r) pairs, r->2r converted | scan-derived, not caliper-confirmed |
| X-61 | Water pipe 2 - clip flats width and axial range | half_width 2.8, t0 12.15, t1 16.25 | mm | width 5.6, range 12.15-16.25 (length 4.1) | - | #9 | ports.json > pipes[1].clip_flats | 2x half_width converted | scan-derived, not caliper-confirmed |
| X-62 | Water pipe 2 - tip bore diameter and depth | bore_r 1.95, bore_depth 2.3 | mm | Ø3.9, depth 2.3 | - | #9 | ports.json > pipes[1].bore_r/bore_depth | r->2r converted | scan-derived, not caliper-confirmed |
| X-63 | Heater terminal 1 - anchor position a (datum frame) | [-0.558, 32.64, 5.2] | mm | [-0.558, 32.64, 5.2] | - | #9 | ports.json > terminals[0].a | json field | scan-derived, not caliper-confirmed |
| X-64 | Heater terminal 1 - axis direction d (unit vector) | [-0.58599, -0.81031, 0.0] | unitless | [-0.58599, -0.81031, 0.0] | - | #9 | ports.json > terminals[0].d | json field | scan-derived, not caliper-confirmed |
| X-65 | Heater terminal 1 - pin section diameter and length | prof t 9.2 to -4.2 @ r3.3 | mm | Ø6.6, length 13.4 | - | #9 | ports.json > terminals[0].prof | profile (t,r) pairs, r->2r converted | scan-derived, not caliper-confirmed |
| X-66 | Heater terminal 1 - shoulder section diameter and length | prof t -4.2 to -5.2 @ r3.45 | mm | Ø6.9, length 1.0 | - | #9 | ports.json > terminals[0].prof | profile (t,r) pairs, r->2r converted; not named in README | scan-derived, not caliper-confirmed |
| X-67 | Heater terminal 1 - neck section diameter and length | prof t -5.2 to -8.2 @ r2.5 | mm | Ø5.0, length 3.0 | - | #9 | ports.json > terminals[0].prof | profile (t,r) pairs, r->2r converted | scan-derived, not caliper-confirmed |
| X-68 | Heater terminal 1 - spade tab thickness | thick 0.8 | mm | 0.8 | - | #9 | ports.json > terminals[0].blade.thick | json field | scan-derived, not caliper-confirmed |
| X-69 | Heater terminal 1 - spade tab hole diameter | hole_d 1.7 | mm dia | 1.7 | - | #9 | ports.json > terminals[0].blade.hole_d | json field | scan-derived, not caliper-confirmed |
| X-70 | Heater terminal 1 - spade tab hole local position (u,v) | [-1.153740826828713, 4.0630085801930775] | mm | [-1.1537, 4.0630] | - | #9 | ports.json > terminals[0].blade.hole_uv | json field | scan-derived, not caliper-confirmed |
| X-71 | Heater terminal 1 - spade tab local base point | [7.899473878319654, 38.900705991137116, 7.66240023126458] | mm | [7.8995, 38.9007, 7.6624] | - | #9 | ports.json > terminals[0].blade.base | json field | scan-derived, not caliper-confirmed |
| X-72 | Heater terminal 1 - spade tab local axes n, e1, e2 | n[-0.29725,0.17038,0.93947]; e1[-0.95455,-0.03076,-0.29645]; e2[-0.02161,-0.98490,0.17178] | unitless | see value as given | - | #9 | ports.json > terminals[0].blade.n/e1/e2 | json field; not a dimension, orientation only | scan-derived, not caliper-confirmed |
| X-73 | Heater terminal 1 - spade tab outline (local u,v polygon, 17 pts) | [[-9.65,1.86],[-9.31,3.21],...,[2.11,-8.02]] | mm | see value as given | - | #9 | ports.json > terminals[0].blade.outline_uv | json field, polygon | scan-derived, not caliper-confirmed |
| X-74 | Heater terminal 2 - anchor position a (datum frame) | [17.032, 25.811, 42.5] | mm | [17.032, 25.811, 42.5] | - | #9 | ports.json > terminals[1].a | json field | scan-derived, not caliper-confirmed |
| X-75 | Heater terminal 2 - axis direction d (unit vector) | [0.10407, 0.99457, 0.0] | unitless | [0.10407, 0.99457, 0.0] | - | #9 | ports.json > terminals[1].d | json field | scan-derived, not caliper-confirmed |
| X-76 | Heater terminal 2 - pin section diameter and length | prof t -9.2 to 2.7 @ r3.35 | mm | Ø6.7, length 11.9 | - | #9 | ports.json > terminals[1].prof | profile (t,r) pairs, r->2r converted | scan-derived, not caliper-confirmed |
| X-77 | Heater terminal 2 - shoulder section diameter and length | prof t 2.7 to 3.8 @ r3.5 | mm | Ø7.0, length 1.1 | - | #9 | ports.json > terminals[1].prof | profile (t,r) pairs, r->2r converted; not named in README | scan-derived, not caliper-confirmed |
| X-78 | Heater terminal 2 - neck section diameter and length | prof t 3.8 to 7.3 @ r2.35 | mm | Ø4.7, length 3.5 | - | #9 | ports.json > terminals[1].prof | profile (t,r) pairs, r->2r converted | scan-derived, not caliper-confirmed |
| X-79 | Heater terminal 2 - spade tab thickness | thick 0.8 | mm | 0.8 | - | #9 | ports.json > terminals[1].blade.thick | json field | scan-derived, not caliper-confirmed |
| X-80 | Heater terminal 2 - spade tab hole diameter | hole_d 2.1 | mm dia | 2.1 | - | #9 | ports.json > terminals[1].blade.hole_d | json field | scan-derived, not caliper-confirmed |
| X-81 | Heater terminal 2 - spade tab hole local position (u,v) | [3.8025720640529643, 5.740923513968519] | mm | [3.8026, 5.7409] | - | #9 | ports.json > terminals[1].blade.hole_uv | json field | scan-derived, not caliper-confirmed |
| X-82 | Heater terminal 2 - spade tab local base point | [15.134688505215305, 34.967883874738895, 39.98778051422177] | mm | [15.1347, 34.9679, 39.9878] | - | #9 | ports.json > terminals[1].blade.base | json field | scan-derived, not caliper-confirmed |
| X-83 | Heater terminal 2 - spade tab local axes n, e1, e2 | n[-0.37253,0.05836,0.92618]; e1[-0.71582,0.61710,-0.32680]; e2[-0.59062,-0.78472,-0.18811] | unitless | see value as given | - | #9 | ports.json > terminals[1].blade.n/e1/e2 | json field; not a dimension, orientation only | scan-derived, not caliper-confirmed |
| X-84 | Heater terminal 2 - spade tab outline (local u,v polygon, 17 pts) | [[-6.7,-0.12],[-6.19,0.12],...,[-5.34,-2.0]] | mm | see value as given | - | #9 | ports.json > terminals[1].blade.outline_uv | json field, polygon | scan-derived, not caliper-confirmed |
| X-85 | Ear notch width, pad A (theta 262.5 deg) | 5.2 | mm | 5.2 | - | #5 | feature tree item 3 | text (feature tree) | consistent with padA.notch_v range in params.json (X-23), not an independent params.json key |
| X-86 | Ear notch width, pad B (theta 339.0 deg) | 4.95 | mm | 4.95 | - | #5 | feature tree item 3 | text (feature tree) | consistent with padB.notch_v range in params.json (X-24), not an independent params.json key |
| X-87 | Central bore lobe root radius, base to web | 15.3 -> 13.8 | mm | 15.3 -> 13.8 | - | #5 | feature tree item 7 | text (feature tree) | not a params.json key; see Q6 (4) |
| X-88 | Central bore lobe tip radius, base to web | 18.1 -> 17.7 | mm | 18.1 -> 17.7 | - | #5 | feature tree item 7 | text (feature tree) | not a params.json key; see Q6 (4) |
| X-89 | Central bore periodicity and fold RMS | 120 deg periodic, fold RMS 0.03 | deg / mm | 120; 0.03 | - | #5 | feature tree item 7 | text (feature tree) | descriptive, not a params.json key |
| X-90 | Water pipe diameter (rounded text) | Ø5.0 | mm | 5.0 | - | #5 | feature tree item 11 | text (feature tree) | cross-checked against ports.json X-53/X-59 (5.0) |
| X-91 | Water pipe collar diameter (rounded text) | Ø8.9 | mm | 8.9 | - | #5 | feature tree item 11 | text (feature tree) | cross-checked against ports.json X-54/X-60 (8.9) |
| X-92 | Water pipe clip flats (rounded text) | 5.6 mm | mm | 5.6 | - | #5 | feature tree item 11 | text (feature tree) | cross-checked against ports.json X-55/X-61 (5.6) |
| X-93 | Water pipe tip bore (rounded text) | Ø3.9 x 2.3 (as far as visible) | mm | 3.9 x 2.3 | - | #5 | feature tree item 11 | text (feature tree) | cross-checked against ports.json X-56/X-62 (3.9 x 2.3) |
| X-94 | Heater terminal pin diameter (rounded text) | Ø6.6 / 6.7 | mm | 6.6 / 6.7 | - | #5 | feature tree item 12 | text (feature tree) | cross-checked against ports.json X-65/X-76 (6.6, 6.7) |
| X-95 | Heater terminal neck diameter (rounded text) | Ø5.0 / 4.7 | mm | 5.0 / 4.7 | - | #5 | feature tree item 12 | text (feature tree) | cross-checked against ports.json X-67/X-76 (5.0, 4.7); README omits the shoulder step seen in ports.json (X-66/X-77) |
| X-96 | Heater terminal spade tab (rounded text) | 6.3 x 0.8 | mm | 6.3 x 0.8 | - | #5 | feature tree item 12 | text (feature tree) | 0.8 (thickness) matches ports.json blade.thick (X-68/X-79); the 6.3 width is not itself a ports.json field (outline_uv only) |
| X-97 | Heater terminal hole diameter (rounded text) | Ø1.7 / Ø2.1 | mm | 1.7 / 2.1 | - | #5 | feature tree item 12 | text (feature tree) | matches ports.json blade.hole_d exactly (X-69/X-78) |
| X-98 | Rib crest radius (text) | R36.25 | mm | 36.25 | - | #5 | feature tree item 2 | text (feature tree) | matches pad_profile (X-22) coordinate values |
| X-99 | Ear block radius and chamfer (text) | R39.4, 45 deg chamfer | mm / deg | 39.4; 45 | - | #5 | feature tree item 2 | text (feature tree) | 39.4 matches pad_profile (X-22); the 45 deg angle is not an explicit params.json field |
| X-100 | Pad base radius (text) | R35.05 | mm | 35.05 | - | #5 | feature tree item 2 | text (feature tree) | matches pad_profile (X-22) coordinate values |
| X-101 | Top pins PCD (text, diameter form) | PCD Ø50 | mm | 50.0 | - | #5 | feature tree item 10 | text (feature tree) | = 2 x pin_pcd_r (X-17, r=25.0); different form of the same value, not a conflict |
| X-102 | Datum export - bbox min | [-43.27, -53.508, -0.0] | mm | [-43.27, -53.508, -0.0] | - | #7 | exports.datum.bbox_min | json field | - |
| X-103 | Datum export - bbox max | [42.839, 53.381, 50.79] | mm | [42.839, 53.381, 50.79] | - | #7 | exports.datum.bbox_max | json field | - |
| X-104 | Datum export - volume | 159766.5 | mm3 | 159766.5 | - | #7 | exports.datum.volume_mm3 | json field | - |
| X-105 | Datum export - face count | 406 | count | 406 | - | #7 | exports.datum.faces | json field | - |
| X-106 | Datum export - surface types: PLANE | 284 | count | 284 | - | #7 | exports.datum.surface_types.PLANE | json field | - |
| X-107 | Datum export - surface types: CONE | 43 | count | 43 | - | #7 | exports.datum.surface_types.CONE | json field | - |
| X-108 | Datum export - surface types: CYLINDER | 73 | count | 73 | - | #7 | exports.datum.surface_types.CYLINDER | json field | - |
| X-109 | Datum export - surface types: BSPLINE | 6 | count | 6 | - | #7 | exports.datum.surface_types.BSPLINE | json field | - |
| X-110 | Datum export - solids / closed / valid | solids 1, valid true, closed true | - | 1 solid; closed; valid | - | #7 | exports.datum.solids/valid/closed | json field | - |
| X-111 | Datum export - file size | 2.4 | MB | 2.4 | - | #7 | exports.datum.size_MB | json field | - |
| X-112 | Scan-frame export - bbox min | [-60.941, -69.977, -244.032] | mm | [-60.941, -69.977, -244.032] | - | #7 | exports.scan.bbox_min | json field | scan-frame coords, not axis-aligned to part |
| X-113 | Scan-frame export - bbox max | [21.486, 34.815, -154.917] | mm | [21.486, 34.815, -154.917] | - | #7 | exports.scan.bbox_max | json field | scan-frame coords, not axis-aligned to part |
| X-114 | Scan-frame export - volume | 159766.5 | mm3 | 159766.5 | - | #7 | exports.scan.volume_mm3 | json field | same solid re-exported in scan frame; matches datum volume X-104 |
| X-115 | Scan -> datum transform matrix T_scan_to_datum | 4x4 matrix, rotation + translation [145.181, -5.622, 158.108] | mm (translation) / unitless (rotation) | see value as given | - | #7 | T_scan_to_datum | json field | coordinate transform, not itself a physical dimension |
| X-116 | Datum bbox size (rounded text) | 86.11 x 106.89 x 50.79 | mm | 86.11 x 106.89 x 50.79 | - | #5 | deliverables section | text (feature tree) | matches export_check.json bbox extents (X-102/X-103) to 2 decimals |
| X-117 | Volume, rebuilt CAD (rounded text) | 159 767 | mm3 | 159767 | - | #5 | deliverables section | text (feature tree) | vs export_check.json 159766.5 (X-104) - rounding only, see Q5 |
| X-118 | Volume, repaired scan mesh (rounded text) | 160 289 | mm3 | 160289 | - | #5 | deliverables section | text (feature tree) | distinct measurement (repaired scan, not the CAD rebuild) - see Q5 |
| X-119 | Scanner-frame bounding box (not axis-aligned) | 82.2 x 104.3 x 87.9 | mm | 82.2 x 104.3 x 87.9 | - | #10 | table row 'Bounding box' | text | different frame from datum bbox (X-102/X-103); not directly comparable, see Q5 |
| X-120 | Scan mesh triangle count | ~0.98 M (988 798 stated in reports README) | count | ~988798 | - | #10 | table row 'Mesh' | text | - |
| X-121 | Scanner fusion voxel size | 0.1 | mm | 0.1 | - | #10 | table row 'Scanner' | text | - |
| X-122 | Deviation scan->CAD (120 000 pts): RMS/p95/p99/max/frac<=0.3 | RMS 0.252, p95 0.474, p99 1.049, max 2.706, frac<=0.3 0.8884 | mm (frac unitless) | same as given | - | #8 | scan->CAD | json field | - |
| X-123 | Deviation CAD->scan (all): RMS/p95/p99/max/frac<=0.3 | RMS 0.506, p95 0.662, p99 2.382, max 6.839, frac<=0.3 0.8733 | mm (frac unitless) | same as given | - | #8 | CAD->scan (all) | json field | - |
| X-124 | Deviation CAD->scan (scanned surface only): RMS/p95/p99/max/frac<=0.3 | RMS 0.268, p95 0.43, p99 0.97, max 4.765, frac<=0.3 0.9128 | mm (frac unitless) | same as given | - | #8 | CAD->scan (scanned surface only) | json field | - |
| X-125 | CAD area on no-scan-data patches | 0.0231 | fraction | 0.0231 | - | #8 | CAD area on no-scan-data patches (fraction) | json field | - |
| X-126 | CAD area in bore sector restored by 3-fold symmetry | 0.0202 | fraction | 0.0202 | - | #8 | CAD area in bore sector restored by 3-fold symmetry (fraction) | json field | - |
| X-127 | Deviation scan->CAD, region: bottom face features (z<1) | n 15220, RMS 0.172, p95 0.369, p99 0.549, max 1.156, frac<=0.3 0.8973 | mm | same as given | - | #8 | scan->CAD by region > bottom face features | json field | - |
| X-128 | Deviation scan->CAD, region: lug/pipes/terminals | n 20682, RMS 0.251, p95 0.54, p99 1.139, max 1.656, frac<=0.3 0.8835 | mm | same as given | - | #8 | scan->CAD by region > lug / pipes / terminals | json field | - |
| X-129 | Deviation scan->CAD, region: main body | n 68902, RMS 0.279, p95 0.529, p99 1.254, max 2.706, frac<=0.3 0.8794 | mm | same as given | - | #8 | scan->CAD by region > main body | json field | - |
| X-130 | Deviation scan->CAD, region: top face features (z>46.8) | n 15196, RMS 0.179, p95 0.335, p99 0.579, max 0.823, frac<=0.3 0.9271 | mm | same as given | - | #8 | scan->CAD by region > top face features | json field | - |
| X-131 | Deviation CAD->scan (scanned only), region: bottom face features | n 7450, RMS 0.251, p95 0.466, p99 1.038, max 2.883, frac<=0.3 0.8834 | mm | same as given | - | #8 | CAD->scan (scanned only) by region > bottom face features | json field | - |
| X-132 | Deviation CAD->scan (scanned only), region: lug/pipes/terminals | n 7808, RMS 0.248, p95 0.528, p99 1.204, max 1.802, frac<=0.3 0.8909 | mm | same as given | - | #8 | CAD->scan (scanned only) by region > lug / pipes / terminals | json field | - |
| X-133 | Deviation CAD->scan (scanned only), region: main body | n 34488, RMS 0.29, p95 0.416, p99 1.024, max 4.765, frac<=0.3 0.9199 | mm | same as given | - | #8 | CAD->scan (scanned only) by region > main body | json field | - |
| X-134 | Deviation CAD->scan (scanned only), region: top face features | n 7659, RMS 0.19, p95 0.357, p99 0.642, max 1.309, frac<=0.3 0.9317 | mm | same as given | - | #8 | CAD->scan (scanned only) by region > top face features | json field | - |
| X-135 | Deviation gate table row: scan->CAD (120 000 points) | RMS 0.252, p95 0.474, p99 1.05, max 2.71 | mm | same as given | - | #5 | deviation gate table | text (feature tree) | rounds deviation_report.json X-122 (scan->CAD); consistent, not a conflict |
| X-136 | Deviation gate table row: CAD->scan, scanned surface | RMS 0.268, p95 0.430, p99 0.97, max 4.77 | mm | same as given | - | #5 | deviation gate table | text (feature tree) | rounds deviation_report.json X-124 (CAD->scan scanned only); consistent, not a conflict |
| X-137 | Regional scan->CAD p95 (text) | base 0.37, top face 0.34, main body 0.53, lugs/pipes/terminals 0.54 | mm | 0.37 / 0.34 / 0.53 / 0.54 | - | #5 | deviation gate section | text (feature tree) | rounds deviation_report.json regional p95 rows X-127/X-130/X-129/X-128; consistent, not a conflict |

<!--
Method: text · table · drawing callout · title block · scaled from drawing ·
photo · message · json field · params.json key · profile (t,r) pairs.
Flags: scan-derived, not caliper-confirmed (every X-01..X-135 row here, since
calipers.md, file #11, is entirely empty: "none yet - every dimension comes from
the scan", scan README.md file #10) · not confirmable for fit from a scan alone
(same reason as a photo, per intake rule 3, for any lug hole, PCD, pipe, or
terminal value used for a fit) · conflicts with X-## · cross-referenced against X-##.
-->

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-R01 | Every 3D-printable part of Open Dedica is designed with the oguz-atolye pipeline: a parametric build script, STEP, STL/3MF and an independent review verdict | "design every 3D-printable part of Open Dedica (OD-G01, OD-C01…C16, OD-T01) with the oguz-atolye pipeline; each part needs a parametric build script, STEP, STL/3MF and an independent review verdict" | #2 | standing instruction, para 1 |
| X-R02 | Every value from a scan or report is an assumption until the Usta confirms it; calipers beat scans; a fit-critical value cannot be confirmed from an image | "every value from a scan or report is an A-## assumption until the Usta confirms it; calipers beat scans; a fit-critical value cannot be confirmed from an image" | #2 | standing instruction, para 1 |
| X-R03 | Data class: PUBLIC (CC BY 4.0) | "data class PUBLIC (CC BY 4.0)" | #2 | standing instruction, para 1 |
| X-R04 | OD-C04 scope: thermoblock mount, material ASA / PC, printed, >=10 mm air gap to printed walls | "This job: OD-C04 thermoblock mount (bom.csv: "Thermoblock mount (≥10 mm air gap to printed walls)", ASA / PC, printed)" | #2 | para 2 |
| X-R05 | OD-C04 is designed against OD-H11 (scanned); OD-H17 (NTC bracket) and OD-H19 (TCO bracket) are not scanned and are carried as assumption rows until their scans land | "The NTC fixing bracket OD-H17 and the TCO fixing bracket OD-H19 are not scanned (chassis/README.md order-of-work row 4: "brackets not scanned"), so they are carried as assumption rows and the part is revisited when their scans land" | #2 | para 2 |
| X-R06 | OD-C01 (base frame) and OD-C05 (group head carrier) are not designed yet; the mount's interface to the frame is a design choice of this job, recorded as an assumption for OD-C01 to follow | "OD-C01 (base frame) and OD-C05 (group head carrier) are not designed yet: the mount's interface to the frame is a design choice of this job, recorded as an assumption for OD-C01 to follow" | #2 | para 2 |
| X-R07 | Every printed part needs one parametric build script, STEP (mm, one named solid) and STL/3MF, with its print orientation and material stated | "one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated" | #3 | chassis/README.md > Goal |
| X-R08 | Order-of-work row 4: OD-C04 thermoblock mount is designed against OD-H11 with its NTC/TCO brackets (OD-H17, H19); blocked by brackets not scanned | "OD-C04 thermoblock mount / OD-H11 with its NTC/TCO brackets (OD-H17, H19) / brackets not scanned" | #3 | chassis/README.md > Order of work, row 4 |
| X-R09 | Order-of-work row 2: OD-C05 group head carrier is designed against OD-G01's rear flange and OD-H11's outlet side, blocked by OD-G01 | "OD-C05 group head carrier / OD-G01's rear flange, OD-H11 outlet side / OD-G01" | #3 | chassis/README.md > Order of work, row 2 |
| X-R10 | Order-of-work row 7: OD-C01 base frame is designed against the footprints of parts 2-6 (incl. OD-C04), blocked by the drip tray not being scanned | "OD-C01 base frame / floor plate / the footprints of 2–6 / drip tray not scanned" | #3 | chassis/README.md > Order of work, row 7 |
| X-R11 | Target machine profiles: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large panels: PETG); build volumes to be read into atolye/machines/ | "Machine profiles: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large panels: PETG); build volumes to be read into `oguz-atolye/atolye/machines/`" | #3 | chassis/README.md > Order of work, footer |
| X-R12 | Thermoblock skin runs well above 100 C: keep >=10 mm air gap to any printed part, mount it on its OEM bracket geometry, use ABS/ASA/PC (not PETG, never PLA) for anything within radiant range | "thermoblock skin runs well above 100 °C. Keep ≥10 mm air gap to any printed part, mount it on its OEM bracket geometry, and use ABS/ASA/PC (not PETG, never PLA) for anything within radiant range" | #3 | docs/SOURCING_GUIDE.md §3.2, chassis note |
| X-R13 | Thermal cutoff (TCO), 192 C, must never be omitted | "Thermal cutoff / TCO 192 °C, code 511876 (#68) + bracket 6013211951 (#69) — **never omit this**" | #3 | docs/SOURCING_GUIDE.md §3.2, table |
| X-R14 | NTC sensor 5217100200 (#55) has fixing bracket 6113211071 (#66); this is OD-H17 | "Sensor / NTC sensor 5217100200 (#55) + fixing bracket 6113211071 (#66)" | #3 | docs/SOURCING_GUIDE.md §3.2, table |
| X-R15 | Thermoblock is De'Longhi code 5513226671 "GENERATOR (230V 1300W + plastic connector)" (#60) | "De'Longhi code / 5513226671 "GENERATOR (230V 1300W + plastic connector)" (#60) — EC680/EC685 listings also appear as "generator/thermoblock EC680"" | #3 | docs/SOURCING_GUIDE.md §3.2, table |
| X-R16 | Safety: keep the wet side separated from the electric side; keep the 192 C TCO in circuit; test behind an RCD/GFCI; never print load-bearing or heat-adjacent parts in PLA | "Keep the wet side separated from the electric side, keep the 192 °C thermal cutoff (TCO) in circuit, test behind an RCD/GFCI, and never print load-bearing or heat-adjacent parts in PLA." | #3 | README.md safety note |
| X-R17 | BOM row OD-C04: Thermoblock mount, >=10 mm air gap to printed walls, material ASA / PC, process print, status proposed, issue #2 | "OD-C04,OD-C00,PRINT,Thermoblock mount (≥10 mm air gap to printed walls),,,1,DESIGN,ASA / PC,printed,print,#2,proposed" | #4 | bom_rows.csv row 15 |
| X-R18 | BOM row OD-H11: thermoblock (generator 230V 1300W + plastic connector), ref 60, OEM 5513226671, qty 1, cad method SCAN, material aluminium casting, status modeled | "OD-H11,OD-H10,OEM,Thermoblock (generator 230 V 1300 W + plastic connector),60,5513226671,1,SCAN,aluminium casting,AliExpress `EC680 thermoblock` / espressocoffeeshop,25–40,#2,modeled" | #4 | bom_rows.csv row 3 |
| X-R19 | BOM row OD-H17: NTC fixing bracket, ref 66, OEM 6113211071, qty 1, cad method SCAN, material steel, status todo, issue #2 | "OD-H17,OD-H10,OEM,NTC fixing bracket,66,6113211071,1,SCAN,steel,FixPart,3,#2,todo" | #4 | bom_rows.csv row 9 |
| X-R20 | BOM row OD-H19: TCO fixing bracket, ref 69, OEM 6013211951, qty 1, cad method SCAN, material steel, status todo, issue #2 | "OD-H19,OD-H10,OEM,TCO fixing bracket,69,6013211951,1,SCAN,steel,FixPart,3,#2,todo" | #4 | bom_rows.csv row 11 |
| X-R21 | BOM row OD-H18: TCO 192 C thermal cutoff - mandatory, ref 68, OEM 511876, qty 1 + 1 spare, status todo, issue #2 | "OD-H18,OD-H10,OEM,TCO 192 °C thermal cutoff — **mandatory**,68,511876,1 (+1 spare),CALIPER,,FixPart,5,#2,todo" | #4 | bom_rows.csv row 10 |
| X-R22 | BOM fastener rows: M3 heat-set insert (brass M3, ~40 pcs) and M3x8 screw (ISO 7380 / DIN 912 A2, ~40 pcs), both status todo | "OD-F01,OD-000,STD,M3 heat-set insert,,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo / OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo" | #4 | bom_rows.csv rows 16-17 |
| X-R23 | The scan report judges the CAD good enough for chassis envelope and thermoblock-mount design (OD-C04, >=10 mm air gap), but says pipe, terminal and mounting interfaces must be confirmed with calipers before the mount is frozen | "Good enough for **chassis envelope and thermoblock-mount design** (`OD-C04`, ≥ 10 mm air gap). Pipe, terminal and mounting interfaces must be confirmed with calipers before the mount is frozen." | #5 | Deviation gate section |
| X-R24 | NTC (OD-H16/H17) and TCO (OD-H18/H19) brackets are explicitly not part of this scanned model | "**NTC (`OD-H16/H17`) and TCO (`OD-H18/H19`) brackets are not part of this model.**" | #5 | Assumptions / open questions |
| X-R25 | Suggested caliper checks named by the report: body diameter (top ~69.9 / bottom ~67.6), height 47.64, counterbore diameter 28.3 (at base), pipe diameter / positions, terminal positions, lug hole diameter | "Suggested caliper checks: body Ø (top ~69.9 / bottom ~67.6), height 47.64, counterbore Ø28.3 (at base), pipe Ø / positions, terminal positions, lug hole Ø." | #5 | Assumptions / open questions |
| X-R26 | It is unknown whether the NTC/TCO brackets were fitted to the thermoblock during the scan | "Unknown whether the NTC (OD-H16/H17) and TCO (OD-H18/H19) brackets were fitted during the scan — note it here when confirmed." | #10 | Known mesh defects |
| X-R27 | The mesh (and hence the rebuilt CAD) is for the envelope only; calipers win on every fit, and calipers.md has not been filled in | "[calipers.md] — interface dimensions (the mesh is for the envelope only; calipers win on every fit)" | #10 | Still missing for this scan |

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-R05, X-R19, X-R20, X-R24 | OD-H17 (NTC fixing bracket) and OD-H19 (TCO fixing bracket) clip onto OD-H11 but are not scanned: what is their shape, and where exactly do they clip onto the thermoblock body (which pad, lug, or groove)? No input gives this geometry. |
| 2 | X-R05, X-R19, X-R20, X-R24 | What volume do OD-H17 and OD-H19 occupy once fitted? OD-C04's >=10 mm air-gap clearance and any cutout for these brackets cannot be designed without their envelope. |
| 3 | calipers.md row 4, X-R23, X-R27 | Which OD-H11 features does the OEM De'Longhi chassis actually screw into? calipers.md row 4 ("Mounting holes / bosses — pattern, Ø, thread") is blank; the candidates in this intake (blind_holes X-49: Ø3.5 at z27.0-33.2 and Ø3.6 at z3.0-8.0; d_web_hole X-09: Ø6.0; top pins X-17/X-101: PCD Ø50) are not identified as mounting features by any input. |
| 4 | — | What is the thermoblock's orientation inside the finished machine (which face points forward/down, how it sits relative to the group head and the base frame)? No input states this. |
| 5 | X-R06 | OD-C01 (base frame) is not designed yet; REQUEST.md says OD-C04's interface to it is "a design choice of this job," but no input gives OD-C01's mounting interface (bolt pattern, standoff heights, or datum) for OD-C04 to bolt to. |
| 6 | X-87 (bore lobe root), X-88 (bore lobe tip), X-89 (periodicity) | The central bore lobe root/tip radii and the 120 deg periodicity are only in README.md's prose (feature tree item 7); they are not keys in params.json. Are they tracked in bore_prof.json (named in the report's src/ folder but not included among this job's inputs)? |
| 7 | X-119 (scanner-frame bbox) | The scan README's scanner-frame bounding box (82.2 x 104.3 x 87.9 mm) does not match the datum-frame bbox extents (86.11 x 106.89 x 50.79 mm, X-102/X-103/X-116) because the two are in different, non-aligned frames. Confirming this is only a frame difference (not a modeling discrepancy) needs the Usta's read of the source data. |
| 8 | X-104, X-117, X-118 | export_check.json's datum-export volume (159766.5 mm3) and README's rebuilt-CAD volume text ("159 767") differ by 0.5 mm3 (rounding); README also separately states a "repaired scan" volume of 160 289 mm3. Which volume, if any, should govern later mass/print-time estimates for OD-C04's design against this envelope? |
| 9 | X-17, X-101 | params.json's pin_pcd_r is a radius (25.0 mm); README states the same feature as "PCD Ø50" (a diameter). They are numerically consistent (50 = 2 x 25) but are recorded from two different sources in two different forms — the Usta should confirm they describe the same pin circle before either is used as a design datum. |
| 10 | all X-01..X-137 | calipers.md (file #11) is completely empty — every one of the 8 rows it defines (port Ø/length, port positions, mounting hole pattern, terminal spade width/positions, NTC boss position, TCO bracket position, overall envelope) is unfilled. Every dimension in this intake therefore comes from the scan reconstruction only; per the standing instruction (X-R02, "calipers beat scans; a fit-critical value cannot be confirmed from an image"), none of OD-C04's fit-critical values (lug/blind-hole positions, pin PCD, pipe/terminal position and diameter, mounting pattern) can be treated as confirmed until calipers are taken. |
| 11 | deviation gate, README.md §Deviation gate | The scan-to-CAD deviation gate verdict is PARTIAL (p95 <= 0.30 / max <= 0.80 mm band not met; see X-122/X-124/X-135/X-136). The report itself says this is "good enough for chassis envelope and thermoblock-mount design" but that "pipe, terminal and mounting interfaces must be confirmed with calipers before the mount is frozen" (X-R23) — does the Usta accept the current scan accuracy for an unfrozen/assumption-carrying first design pass of OD-C04, or should the job wait for calipers first? |
| 12 | X-66, X-77 (shoulder sections) | ports.json's terminal profiles each include an intermediate 'shoulder' diameter step (terminal 1: Ø6.9 over 1.0 mm; terminal 2: Ø7.0 over 1.1 mm, see X-66/X-77) that README's rounded text (X-95) does not mention at all. Is this shoulder a real physical feature (e.g., a crimp collar) or a scan/reconstruction artifact? |

<!-- Also information the spec will need that no input gives, as a question, never as an answer. -->

## §5 Unreadable

None of the listed inputs were unreadable. One note on how they were read:

- `00_Spec/inputs/OD-H11_thermoblock.step` (#1) was listed and hashed only, per intake rule 6 and the brief: its geometry is measured later with `tools/measure`, not read here.
- Images referenced from inside the read files (`views_cad.png`, `deviation_signed_map.png` in reports/OD-H11_thermoblock/README.md; `preview.png` in scan/OD-H11_thermoblock/README.md) are not themselves listed in the brief's input list and were not read.
- `calipers.md` (#11) was read in full; its measurement table is present but every value cell is empty (see §4, gap 10).
