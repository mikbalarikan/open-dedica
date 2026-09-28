# OD-E02_control-button-board — STL → STEP reverse-engineering delivery

**Verdict: `BAND_NOT_MET`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 3 of 3 (earlier iterations kept: `_it1_SUPERSEDED/`, `_it2_SUPERSEDED/`).  
**Verification independence (CHK-INDEP):** pass — fresh agent, own scripts; see independence  

> **A deviation band was NOT met.** Delivered only under the recorded human acceptance below (by Ikbal (owner, question card), 2026-09-28, record `decisions/accept_band.md`).

## 1. The part

![reference photo](../input/photos/2.png)

Front control button board of a DeLonghi espresso machine: stepped moulded housing with a snap-fitted back cover, PCB connector shroud, two screw holes, bent mounting tab, four latch hoops and three push-button caps (1 cup, 2 cups, steam), delivered as one fused solid of the assembly as scanned.

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-E02_control-button-board_datum.step` | datum | 1 | yes | yes | 374 | 36865.1716 | max: [38.16, 16.1729, 18.9511]; min: [-38.6285, -37.4736, -29.2147]; size: [76.7885, 53.6465, 48.1658] |
| `build/OD-E02_control-button-board.step` | scan | 1 | yes | yes | 374 | 36865.1716 | max: [18.8744, 23.9569, -145.3627]; min: [-52.707, -48.1972, -189.6159]; size: [71.5815, 72.1541, 44.2532] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Intake: sha256 of the scan, working copy, noise floor on the mounting-tab top face, datum = back cover floor (XY), origin on the middle button collar axis, +X from the housing end face.
2. Measure: every dimension from the full-resolution scan in the frozen datum frame (scan-only, no calipers); the housing tiers are offsets of one core outline whose corner centres were fitted once; edge rounds measured from the scan distance at the sharp corners.
3. Rebuild: build123d, plan-first; tier prisms from the offset core, a fitted chamfer plane, sub-bodies for band, collars, caps, shroud, tab and hoops, cut tools for pocket, recesses, holes; every fillet logged; one valid closed solid exported in the datum and the scan frame.
4. Verify: an independent agent re-ran its own ICP and the two-way full-resolution deviation under the declared regime.
5. Deliver: README and manifest rendered from the JSON records, fresh-process reproducibility check, one zip with deliverables and all source files.

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | middle button collar axis ∩ back cover floor plane | — | — |
| primary (plane) | back cover floor (flat rear face inside the rim wall) | 0.0218 / 0.0997 | the back cover is the board plane: the three button axes, the screw-boss holes and the connector shroud are all normal to it; largest clean moulded flat (logos excluded by the RANSAC trim) |
| secondary (axis) | middle button collar (housing bore boss around the espresso-2-cups button) | 0.0294 / 0.0954 | housing feature that guides the middle button; the part is mirror-symmetric about it (side buttons at +/-27 mm). The loose button cap itself sits 1.6 deg tilted in its bore and is rougher (circle rms 0.03-0.08), so it is not used as the datum |
| clock | plane_normal: +X end face of the housing rim/steps (end nearest the steam button) -> +X (angle 111.4904°) | — | — |

Measured tilt: 1.7577° (common slope, per-feature intercept, 9 stations over 1 feature(s), z -18.700..-16.400 vs frame Z). Scale factor applied: 1. Scan noise floor: 0.0265 mm (rms of RANSAC+SVD plane on mounting-tab top face (moulded flat, parallel to the back floor, 18.9 mm above it) (1638 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
-0.623783  -0.777291  -0.081936  -33.067528
 0.527173  -0.495808   0.690118   111.909077
-0.577047   0.387289   0.719044   115.027167
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: assumed 2, scan 118 (total 120). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `T0_R_bump` | 5.4723 | mm | 5.4723 | keep-measured | scan | 0.0834 | no | measure/figures/m_all.json#tiers.T0 |
| `T0_R_main` | 5.8363 | mm | 5.8363 | keep-measured | scan | 0.1004 | no | measure/figures/m_all.json#tiers.T0 |
| `T0_bottom_z` | -7.5969 | mm | -7.5969 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.T0_bottom |
| `T0_concave_r` | 1.1067 | mm | 1.1067 | keep-measured | scan | 0.0291 | no | measure/figures/m_all.json#concave.T0 |
| `T2_R_bump` | 3.3099 | mm | 3.3099 | keep-measured | scan | 0.0372 | no | measure/figures/m_all.json#tiers.T2 |
| `T2_R_main` | 3.65 | mm | 3.65 | keep-measured | scan | 0.0893 | no | measure/figures/m_all.json#tiers.T2 |
| `T2_bottom_z` | -10.1215 | mm | -10.1215 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.T2_bottom |
| `T2_concave_r` | [2.2241, 1.9535] | mm | [2.2241, 1.9535] | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#concave.T2 |
| `T3_R_bump` | 2.1832 | mm | 2.1832 | keep-measured | scan | 0.1263 | no | measure/figures/m_all.json#tiers.T3 |
| `T3_R_main` | 2.3823 | mm | 2.3823 | keep-measured | scan | 0.199 | no | measure/figures/m_all.json#tiers.T3 |
| `T3_bottom_z` | -13.1911 | mm | -13.1911 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.T3_bottom |
| `T3_concave_r` | [3.003, 2.8232] | mm | [3.003, 2.8232] | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#concave.T3 |
| `band_bottom_z` | -16.1349 | mm | -16.1349 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.band_bottom |
| `band_disk_L` | [-26.7231, -4.8071, 8.1524] | mm | [-26.7231, -4.8071, 8.1524] | keep-measured | scan | 0.0167 | no | measure/figures/m_all.json#band.end_disk_L |
| `band_disk_R` | [26.3142, -5.2418, 8.326] | mm | [26.3142, -5.2418, 8.326] | keep-measured | scan | 0.0214 | no | measure/figures/m_all.json#band.end_disk_R |
| `band_top_y` | [3.261, 2.9692] | mm | [3.261, 2.9692] | keep-measured | scan | 0.03 | no | measure/figures/m_all.json#band.top_line_* |
| `boss_mY_L` | [-31.1336, -17.4341, -16.0391] | mm | [-31.1336, -17.4341, -16.0391] | keep-measured | scan | 0.08 | no | measure/figures/m_all.json#bosses.mY_L |
| `boss_mY_R` | [16.9185, 30.6476, -16.03] | mm | [16.9185, 30.6476, -16.03] | keep-measured | scan | 0.08 | no | measure/figures/m_all.json#bosses.mY_R |
| `boss_pY_R` | [16.9587, 30.6859, 4.2802] | mm | [16.9587, 30.6859, 4.2802] | keep-measured | scan | 0.08 | no | measure/figures/m_all.json#bosses.pY_R |
| `boss_top_z` | 3.4799 | mm | 3.4799 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.boss_top |
| `bump_TL` | [-20.0741, 8.994] | mm | [-20.0741, 8.994] | keep-measured | scan | 0.3881 | no | measure/figures/m_all.json#core.bumpTL |
| `bump_TR` | [10.8061, 8.7833] | mm | [10.8061, 8.7833] | keep-measured | scan | 0.1477 | no | measure/figures/m_all.json#core.bumpTR |
| `cap_B1_ellipse` | [-26.5135, -4.7522, 5.9182, 6.3589, 13.7633] | mm | [-26.5135, -4.7522, 5.9182, 6.3589, 13.7633] | keep-measured | scan | 0.0326 | yes | measure/figures/m_all.json#caps.B1.ellipse |
| `cap_B1_top_normal` | [-0.3412, -0.0601, -0.9381] | mm | [-0.3412, -0.0601, -0.9381] | keep-measured | scan | 0.0391 | no | measure/figures/m_all.json#caps.B1.top |
| `cap_B1_top_offset` | 31.9729 | mm | 31.9729 | keep-measured | scan | 0.0391 | no | measure/figures/m_all.json#caps.B1.top |
| `cap_B2_axis_dir` | [-0.0128, -0.009, 0.9999] | mm | [-0.0128, -0.009, 0.9999] | keep-measured | scan | 0.03 | no | measure/figures/m_all.json#caps.B2.axis |
| `cap_B2_axis_xy0` | [-0.2362, -0.2446] | mm | [-0.2362, -0.2446] | keep-measured | scan | 0.03 | no | measure/figures/m_all.json#caps.B2.axis |
| `cap_B2_r` | 6.3395 | mm | 6.3395 | keep-measured | scan | 0.04 | yes | measure/figures/m_all.json#caps.B2 |
| `cap_B2_top_normal` | [0.0103, 0.0055, -0.9999] | mm | [0.0103, 0.0055, -0.9999] | keep-measured | scan | 0.0362 | no | measure/figures/m_all.json#caps.B2.top |
| `cap_B2_top_offset` | 29.1492 | mm | 29.1492 | keep-measured | scan | 0.0362 | no | measure/figures/m_all.json#caps.B2.top |
| `cap_B3_ellipse` | [26.5737, -5.2348, 5.934, 6.3955, -10.9268] | mm | [26.5737, -5.2348, 5.934, 6.3955, -10.9268] | keep-measured | scan | 0.0419 | yes | measure/figures/m_all.json#caps.B3.ellipse |
| `cap_B3_top_normal` | [0.3498, -0.0781, -0.9336] | mm | [0.3498, -0.0781, -0.9336] | keep-measured | scan | 0.0392 | no | measure/figures/m_all.json#caps.B3.top |
| `cap_B3_top_offset` | 32.1747 | mm | 32.1747 | keep-measured | scan | 0.0392 | no | measure/figures/m_all.json#caps.B3.top |
| `chamfer_normal` | [-0.0064, -0.7088, -0.7053] | mm | [-0.0064, -0.7088, -0.7053] | keep-measured | scan | 0.0456 | no | measure/figures/m_all.json#chamfer |
| `chamfer_offset` | 18.0023 | mm | 18.0023 | keep-measured | scan | 0.0456 | no | measure/figures/m_all.json#chamfer |
| `collar_B1` | [-26.5131, -4.828, 8.0898] | mm | [-26.5131, -4.828, 8.0898] | keep-measured | scan | 0.05 | yes | measure/figures/m_all.json#collars.B1 |
| `collar_B1_cut_plane` | [0.44, 0.1022, 0.8922, -29.3653] | mm | [0.44, 0.1022, 0.8922, -29.3653] | keep-measured | scan | 0.0857 | no | measure/figures/m_all.json#collars.B1.cut_plane |
| `collar_B1_floor_sector_deg` | [174.4734, 217.1657] | deg | [174.4734, 217.1657] | keep-measured | scan | 0 | no | measure/figures/m_all.json#collars.B1.floor_sector_deg |
| `collar_B1_recess` | [7.6533, -17.9697] | mm | [7.6533, -17.9697] | keep-measured | scan | 0.1 | no | measure/figures/m_all.json#recess.B1 |
| `collar_B1_recess_floor_sector_deg` | [150, 250] | deg | [150, 250] | keep-measured | scan | 0 | no | measure/figures/m_all.json#recess.B1 |
| `collar_B1_recess_mid_1` | [120, 150, -16.2106] | mm | [120, 150, -16.2106] | keep-measured | scan | 0.1 | no | measure/figures/m_all.json#recess.B1_mid |
| `collar_B1_recess_ramp_plane` | [0.5323, 0.1007, 0.8406, -30.1273] | mm | [0.5323, 0.1007, 0.8406, -30.1273] | keep-measured | scan | 0.2661 | no | measure/figures/m_all.json#recess.B1_ramp |
| `collar_B1_sector_floor_z` | -15.0636 | mm | -15.0636 | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#collars.B1.sector_floor |
| `collar_B2_r` | 8.1939 | mm | 8.1939 | keep-measured | scan | 0.03 | yes | measure/figures/m_all.json#collars.B2 |
| `collar_B2_recess` | [7.4064, -18.2353] | mm | [7.4064, -18.2353] | keep-measured | scan | 0.1 | no | measure/figures/m_all.json#recess.B2 |
| `collar_B3` | [26.4568, -5.2691, 8.1907] | mm | [26.4568, -5.2691, 8.1907] | keep-measured | scan | 0.05 | yes | measure/figures/m_all.json#collars.B3 |
| `collar_B3_cut_plane` | [-0.4553, 0.0974, 0.885, -29.6148] | mm | [-0.4553, 0.0974, 0.885, -29.6148] | keep-measured | scan | 0.1003 | no | measure/figures/m_all.json#collars.B3.cut_plane |
| `collar_B3_floor_sector_deg` | [-24.1881, -2.8978] | deg | [-24.1881, -2.8978] | keep-measured | scan | 0 | no | measure/figures/m_all.json#collars.B3.floor_sector_deg |
| `collar_B3_recess` | [7.6381, -17.7484] | mm | [7.6381, -17.7484] | keep-measured | scan | 0.1 | no | measure/figures/m_all.json#recess.B3 |
| `collar_B3_recess_floor_sector_deg` | [-90, 40] | deg | [-90, 40] | keep-measured | scan | 0 | no | measure/figures/m_all.json#recess.B3 |
| `collar_B3_recess_mid_1` | [40, 50, -15.6689] | mm | [40, 50, -15.6689] | keep-measured | scan | 0.1 | no | measure/figures/m_all.json#recess.B3_mid |
| `collar_B3_sector_floor_z` | -14.7494 | mm | -14.7494 | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#collars.B3.sector_floor |
| `collar_bottom_z` | -19.1069 | mm | -19.1069 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.collar_bottom |
| `core_BL` | [-32.7922, -12.7062] | mm | [-32.7922, -12.7062] | keep-measured | scan | 0.1092 | no | measure/figures/m_all.json#core.BL |
| `core_BR` | [32.3237, -13.1173] | mm | [32.3237, -13.1173] | keep-measured | scan | 0.1267 | no | measure/figures/m_all.json#core.BR |
| `core_TL` | [-32.7317, 1.486] | mm | [-32.7317, 1.486] | keep-measured | scan | 0.092 | no | measure/figures/m_all.json#core.TL |
| `core_TR` | [32.2973, 1.0667] | mm | [32.2973, 1.0667] | keep-measured | scan | 0.0822 | no | measure/figures/m_all.json#core.TR |
| `header_pad_1` | [-16.7467, -14.6228, 2.4613, 0.0329] | mm | [-16.7467, -14.6228, 2.4613, 0.0329] | keep-measured | scan | 0.1 | no | measure/figures/m_all.json#shroud.header_pads |
| `header_pad_2` | [-6.6845, -4.5535, 2.2001, 0.1486] | mm | [-6.6845, -4.5535, 2.2001, 0.1486] | keep-measured | scan | 0.1 | no | measure/figures/m_all.json#shroud.header_pads |
| `hoop_H1` | [-28.7075, -19.6107, -26.872, -21.4957, -3.4558, 4.688, -20.3633] | mm | [-28.7075, -19.6107, -26.872, -21.4957, -3.4558, 4.688, -20.3633] | keep-measured | scan | 0.08 | no | measure/figures/m_all.json#hoops.H1 |
| `hoop_H1_ramp_plane` | [0.0056, -0.7617, 0.6479, 12.8228] | mm | [0.0056, -0.7617, 0.6479, 12.8228] | keep-measured | scan | 0.0559 | no | measure/figures/m_all.json#hoops.H1.window_ramp |
| `hoop_H2` | [19.2954, 28.3688, 21.0902, 26.4221, -2.5416, 4.7268, -20.3846] | mm | [19.2954, 28.3688, 21.0902, 26.4221, -2.5416, 4.7268, -20.3846] | keep-measured | scan | 0.08 | no | measure/figures/m_all.json#hoops.H2 |
| `hoop_H2_ramp_plane` | [0.0681, 0.8036, -0.5913, -12.589] | mm | [0.0681, 0.8036, -0.5913, -12.589] | keep-measured | scan | 0.0658 | no | measure/figures/m_all.json#hoops.H2.window_ramp |
| `hoop_H3` | [-20.7166, -11.687, -18.9135, -13.5487, -2.6655, 4.6764, 16.1729] | mm | [-20.7166, -11.687, -18.9135, -13.5487, -2.6655, 4.6764, 16.1729] | keep-measured | scan | 0.08 | no | measure/figures/m_all.json#hoops.H3 |
| `hoop_H3_ramp_plane` | [0.0023, 0.4089, 0.9126, 3.2873] | mm | [0.0023, 0.4089, 0.9126, 3.2873] | keep-measured | scan | 0.0316 | no | measure/figures/m_all.json#hoops.H3.window_ramp |
| `hoop_H4` | [19.3352, 28.3032, 21.1156, 26.4588, -3.0193, 4.7127, 8.7329] | mm | [19.3352, 28.3032, 21.1156, 26.4588, -3.0193, 4.7127, 8.7329] | keep-measured | scan | 0.08 | no | measure/figures/m_all.json#hoops.H4 |
| `hoop_H4_ramp_plane` | [0.0117, 0.3336, 0.9426, -0.3117] | mm | [0.0117, 0.3336, 0.9426, -0.3117] | keep-measured | scan | 0.0309 | no | measure/figures/m_all.json#hoops.H4.window_ramp |
| `hoop_bottom_z` | -5.5662 | mm | -5.5662 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.hoop_bottom |
| `pocket_concave_r` | [2.9999, 2.7905] | mm | [2.9999, 2.7905] | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#rim_junctions.pocket |
| `rim_concave_r` | [1.1943, 1.4009] | mm | [1.1943, 1.4009] | keep-measured | scan | 0.1374 | no | measure/figures/m_all.json#rim_junctions.outer |
| `rim_in_R_bump` | 4.0792 | mm | 4.0792 | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#rim_in |
| `rim_in_R_main` | 4.43 | mm | 4.43 | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#rim_in |
| `rim_out_R_bump` | 5.3929 | mm | 5.3929 | keep-measured | scan | 0.0877 | no | measure/figures/m_all.json#tiers.rim_out |
| `rim_out_R_main` | 5.6065 | mm | 5.6065 | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#tiers.rim_out |
| `rim_top_z` | 4.94 | mm | 4.94 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.rim_top |
| `round_T0_bottom_edge` | 1.6993 | mm | 1.6993 | keep-measured | scan | 0.0705 | no | measure/figures/m_edges.json#T0_bottom_edge |
| `round_T2_bottom_edge` | 0.5335 | mm | 0.5335 | keep-measured | scan | 0.0429 | no | measure/figures/m_edges.json#T2_bottom_edge |
| `round_T3_bump_bottom_edge` | 1.6379 | mm | 1.6379 | keep-measured | scan | 0.0558 | no | measure/figures/m_edges.json#T3_bump_bottom_edge |
| `round_band_top_bottom_edge` | 1.9973 | mm | 1.9973 | keep-measured | scan | 0.0528 | no | measure/figures/m_edges.json#band_top_bottom_edge |
| `round_cap_B1_top_edge` | 0.7803 | mm | 0.7803 | keep-measured | scan | 0.2247 | no | measure/figures/m_edges.json#cap_B1_top_edge |
| `round_cap_B2_top_edge` | 0.7756 | mm | 0.7756 | keep-measured | scan | 0.1025 | no | measure/figures/m_edges.json#cap_B2_top_edge |
| `round_cap_B3_top_edge` | 0.7758 | mm | 0.7758 | keep-measured | scan | 0.2628 | no | measure/figures/m_edges.json#cap_B3_top_edge |
| `round_rim_top_inner_edge` | 0.6488 | mm | 0.6488 | keep-measured | scan | 0.1762 | no | measure/figures/m_edges.json#rim_top_inner_edge |
| `round_rim_top_outer_edge` | 0.5451 | mm | 0.5451 | keep-measured | scan | 0.1675 | no | measure/figures/m_edges.json#rim_top_outer_edge |
| `round_shroud_inner_vertical_corner` | 1.2593 | mm | 1.2593 | keep-measured | scan | 0.086 | no | measure/figures/m_edges.json#shroud_inner_vertical_corner |
| `round_shroud_top_inner_edge` | 0.6254 | mm | 0.6254 | keep-measured | scan | 0.1277 | no | measure/figures/m_edges.json#shroud_top_inner_edge |
| `round_shroud_top_outer_edge` | 0.6138 | mm | 0.6138 | keep-measured | scan | 0.1746 | no | measure/figures/m_edges.json#shroud_top_outer_edge |
| `round_tab_end_top_edge` | 1.3871 | mm | 1.3871 | keep-measured | scan | 0.0218 | no | measure/figures/m_edges.json#tab_end_top_edge |
| `screw_L_cb_r` | 3.788 | mm | 3.788 | keep-measured | scan | 0.03 | yes | measure/figures/m_all.json#holes.L |
| `screw_L_front` | [-12.9534, -7.8192, 3.3781] | mm | [-12.9534, -7.8192, 3.3781] | keep-measured | scan | 0.05 | yes | measure/figures/m_all.json#holes.L.front_stations |
| `screw_L_front_top_z` | -11.8357 | mm | -11.8357 | keep-measured | scan | 0.3 | no | measure/figures/m_all.json#holes.L |
| `screw_L_through_r` | 1.7688 | mm | 1.7688 | keep-measured | scan | 0.05 | yes | measure/figures/m_all.json#holes.L |
| `screw_L_xy` | [-13.2349, -7.9445] | mm | [-13.2349, -7.9445] | keep-measured | scan | 0.03 | yes | measure/figures/m_all.json#holes.L |
| `screw_R_cb_r` | 3.7418 | mm | 3.7418 | keep-measured | scan | 0.03 | yes | measure/figures/m_all.json#holes.R |
| `screw_R_front` | [13.0483, -8.0557, 3.3248] | mm | [13.0483, -8.0557, 3.3248] | keep-measured | scan | 0.05 | yes | measure/figures/m_all.json#holes.R.front_stations |
| `screw_R_front_top_z` | -12.4694 | mm | -12.4694 | keep-measured | scan | 0.3 | no | measure/figures/m_all.json#holes.R |
| `screw_R_through_r` | 1.7206 | mm | 1.7206 | keep-measured | scan | 0.05 | yes | measure/figures/m_all.json#holes.R |
| `screw_R_xy` | [12.7485, -8.0013] | mm | [12.7485, -8.0013] | keep-measured | scan | 0.03 | yes | measure/figures/m_all.json#holes.R |
| `screw_cb_floor_z` | -2.9158 | mm | -2.9158 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.screw_cb_floor |
| `shroud_inner` | [-21.5183, 4.5011, 0.9798, 10.661] | mm | [-21.5183, 4.5011, 0.9798, 10.661] | keep-measured | scan | 0.08 | no | measure/figures/m_all.json#shroud |
| `shroud_inner_floor_z` | -2.3134 | mm | -2.3134 | keep-measured | scan | 0.3 | no | measure/figures/m_all.json#shroud |
| `shroud_outer` | [-22.6105, 5.5799, -0.1439, 11.7071] | mm | [-22.6105, 5.5799, -0.1439, 11.7071] | keep-measured | scan | 0.08 | yes | measure/figures/m_all.json#shroud |
| `shroud_outer_corner_r` | 0.6516 | mm | 0.6516 | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#shroud |
| `shroud_slot_note` | 0 | mm | — | assumed | assumed | 0 | no | intake/coverage.json loop 2; measure probe in make_params docstring |
| `shroud_top_z` | 10.4956 | mm | 10.4956 | keep-measured | scan | 0.0265 | no | measure/figures/m_all.json#z.shroud_top |
| `tab_end_under_edge_note` | 0 | mm | — | assumed | assumed | 0 | no | measure/figures/m_edges.json#tab_end_under_edge |
| `tab_end_y` | -37.4736 | mm | -37.4736 | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#tab.end_y |
| `tab_flange_bottom_z` | -1.9598 | mm | -1.9598 | keep-measured | scan | 0.05 | no | measure/figures/m_all.json#tab.flange_bottom |
| `tab_flange_incline_plane` | [0.0023, -0.7184, -0.6956, 19.6738] | mm | [0.0023, -0.7184, -0.6956, 19.6738] | keep-measured | scan | 0.0224 | no | measure/figures/m_all.json#tab.flange_lower_incline |
| `tab_flange_inner_neg_plane` | [0.999, 0.0077, -0.0434, -14.2827] | mm | [0.999, 0.0077, -0.0434, -14.2827] | keep-measured | scan | 0.022 | no | measure/figures/m_all.json#tab.flange_inner_x.neg |
| `tab_flange_inner_pos_plane` | [-0.9986, 0.003, -0.052, -13.8073] | mm | [-0.9986, 0.003, -0.052, -13.8073] | keep-measured | scan | 0.0176 | no | measure/figures/m_all.json#tab.flange_inner_x.pos |
| `tab_flange_outer_neg_plane` | [-0.999, -0.0066, 0.0452, 16.2506] | mm | [-0.999, -0.0066, 0.0452, 16.2506] | keep-measured | scan | 0.0227 | no | measure/figures/m_all.json#tab.flange_outer_x.neg |
| `tab_flange_outer_pos_plane` | [0.9987, 0.0015, 0.0516, 15.6597] | mm | [0.9987, 0.0015, 0.0516, 15.6597] | keep-measured | scan | 0.0237 | no | measure/figures/m_all.json#tab.flange_outer_x.pos |
| `tab_hole` | [-0.218, -32.7639, 1.6428] | mm | [-0.218, -32.7639, 1.6428] | keep-measured | scan | 0.0325 | yes | measure/figures/m_all.json#tab.hole |
| `tab_incline_lower_plane` | [0.0011, -0.7179, -0.6962, 9.1071] | mm | [0.0011, -0.7179, -0.6962, 9.1071] | keep-measured | scan | 0.0117 | no | measure/figures/m_all.json#tab.incline_lower |
| `tab_incline_upper_plane` | [-0.0023, 0.7155, 0.6987, -7.2239] | mm | [-0.0023, 0.7155, 0.6987, -7.2239] | keep-measured | scan | 0.0105 | no | measure/figures/m_all.json#tab.incline_upper |
| `tab_leg_inner_plane` | [-0.0003, 0.9999, 0.017, -16.5912] | mm | [-0.0003, 0.9999, 0.017, -16.5912] | keep-measured | scan | 0.0088 | no | measure/figures/m_all.json#tab.leg_inner |
| `tab_leg_outer_plane` | [-0.001, -0.9997, -0.0227, 18.5305] | mm | [-0.001, -0.9997, -0.0227, 18.5305] | keep-measured | scan | 0.0083 | no | measure/figures/m_all.json#tab.leg_outer |
| `tab_top_plane` | [-0.0019, 0.0114, 0.9999, 18.5383] | mm | [-0.0019, 0.0114, 0.9999, 18.5383] | keep-measured | scan | 0.0225 | no | measure/figures/m_all.json#tab.top |
| `tab_under_plane` | [0.0014, -0.0116, -0.9999, -16.0036] | mm | [0.0014, -0.0116, -0.9999, -16.0036] | keep-measured | scan | 0.02 | no | measure/figures/m_all.json#tab.under |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

| id | feature | params |
|---|---|---|
| F01-F02 | rim + pocket (offset core outline), inner latch bosses | [core_BL, rim_out_R_main, rim_in_R_main, rim_top_z, boss_mY_L] |
| F03-F05 | stepped tiers T0/T2/T3 with junction fillets and the -Y chamfer plane | [T0_R_main, T2_R_main, T3_R_main, chamfer_normal, chamfer_offset] |
| F06-F10 | button band, collars, outer collar cuts, cap clearance recesses | [band_top_y, band_disk_L, collar_B2_r, collar_B1_cut_plane, collar_B2_recess] |
| F11-F12 | button caps (B2 round and tilted as scanned, B1/B3 oval with inclined tops) | [cap_B2_r, cap_B2_axis_dir, cap_B1_ellipse, cap_B1_top_normal] |
| F13-F15 | connector shroud, shroud interior, screw holes | [shroud_outer, shroud_inner, screw_L_xy, screw_L_cb_r, screw_L_front] |
| F16 | mounting tab (plate, leg, drafted side flanges, hole) | [tab_top_plane, tab_incline_upper_plane, tab_flange_outer_neg_plane, tab_hole] |
| F17 | latch hoops with catch ramps | [hoop_H1, hoop_H1_ramp_plane] |

## 7. Tier-1 — caliper dims re-measured on the STEP

**Tier-1 not run: no caliper dimensions exist.** Every dimension is scan authority (or operator spec); see the source column in §5. Absent is not passed.

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), iterations 33/60, converged yes, correction 0.0866° / 0.0227 mm.  
Unobservable CAD fraction: 0.0152.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 294367 | 0.1089 | 0.0442 | 0.2365 | 0.3947 | 0.9223 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 294367 | 0.1089 | 0.0442 | 0.2365 | 0.3947 | 0.9223 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 0.5575 | 0.0434 | 0.9305 | 3.1749 | 5.4724 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 270144 | 0.2637 | 0.0378 | 0.2832 | 1.2228 | 5.4059 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 19695 | 0.5371 | 0.0427 | 0.6326 | 3.1674 | 5.4217 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.2365 max 0.9223 (n 294367) | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 0.6326 max 5.4217 (n 19695) | FAIL |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| I1 shroud interior | interior | scan_to_cad | reported | reported | n 1665 · p95 0.3011 · max 0.5743 | n 1665 · p95 0.3011 · max 0.5743 | INTAKE_CARD §3 connector shroud interior (header, pins) occluded |
| I1 shroud interior | interior | cad_to_scan | reported | reported | n 5427 · p95 4.6453 · max 5.4724 | n 719 · p95 4.706 · max 5.4059 | INTAKE_CARD §3 connector shroud interior (header, pins) occluded |
| I2 cap-collar gaps | interior | scan_to_cad | reported | reported | n 12049 · p95 0.3217 · max 0.9223 | n 12049 · p95 0.3217 · max 0.9223 | INTAKE_CARD §3 narrow gaps around the caps |
| I2 cap-collar gaps | interior | cad_to_scan | reported | reported | n 8782 · p95 0.5576 · max 1.1364 | n 6215 · p95 0.3895 · max 0.8116 | INTAKE_CARD §3 narrow gaps around the caps |
| Z1 back cover floor | functional_interface | scan_to_cad | reported | reported | n 19834 · p95 0.0771 · max 0.5554 | n 19834 · p95 0.0771 · max 0.5554 | INTAKE_CARD §4 Z1, primary datum plane |
| Z1 back cover floor | functional_interface | cad_to_scan | reported | reported | n 28966 · p95 0.1483 · max 2.8037 | n 27472 · p95 0.0725 · max 2.8037 | INTAKE_CARD §4 Z1, primary datum plane |
| Z2 housing tiers | functional_interface | scan_to_cad | reported | reported | n 108878 · p95 0.2289 · max 0.737 | n 108878 · p95 0.2289 · max 0.737 | INTAKE_CARD §4 Z2, T0..T4 below the floor (includes hoops, band bar, screw-hole walls in this z range) |
| Z2 housing tiers | functional_interface | cad_to_scan | reported | reported | n 106394 · p95 2.3636 · max 5.4724 | n 91236 · p95 0.2686 · max 5.4059 | INTAKE_CARD §4 Z2, T0..T4 below the floor (includes hoops, band bar, screw-hole walls in this z range) |
| Z3 caps and collars | functional_interface | scan_to_cad | reported | reported | n 46334 · p95 0.2081 · max 0.9223 | n 46334 · p95 0.2081 · max 0.9223 | INTAKE_CARD §4 Z3, collars z -16.1..-19.1 and caps B1-B3 |
| Z3 caps and collars | functional_interface | cad_to_scan | reported | reported | n 36613 · p95 0.3467 · max 1.1364 | n 31742 · p95 0.156 · max 0.892 | INTAKE_CARD §4 Z3, collars z -16.1..-19.1 and caps B1-B3 |
| Z4 mounting tab | functional_interface | scan_to_cad | reported | reported | n 38865 · p95 0.1342 · max 0.3957 | n 38865 · p95 0.1342 · max 0.3957 | INTAKE_CARD §4 Z4, above the rim top on the -Y side |
| Z4 mounting tab | functional_interface | cad_to_scan | reported | reported | n 44247 · p95 0.1214 · max 0.5786 | n 43860 · p95 0.1176 · max 0.5786 | INTAKE_CARD §4 Z4, above the rim top on the -Y side |
| Z5 screw holes | functional_interface | scan_to_cad | reported | reported | n 5970 · p95 0.1544 · max 0.4398 | n 5970 · p95 0.1544 · max 0.4398 | INTAKE_CARD §4 Z5, bore walls around (+-13, -8) |
| Z5 screw holes | functional_interface | cad_to_scan | reported | reported | n 9232 · p95 3.3016 · max 4.454 | n 3809 · p95 0.2111 · max 0.6792 | INTAKE_CARD §4 Z5, bore walls around (+-13, -8) |
| Z6 connector shroud | functional_interface | scan_to_cad | reported | reported | n 25033 · p95 0.2749 · max 0.7615 | n 25033 · p95 0.2749 · max 0.7615 | INTAKE_CARD §4 Z6, walls x -22.6..5.6, y -0.2..11.5 located on the scan |
| Z6 connector shroud | functional_interface | cad_to_scan | reported | reported | n 30450 · p95 1.0484 · max 2.8389 | n 26429 · p95 0.7096 · max 2.4341 | INTAKE_CARD §4 Z6, walls x -22.6..5.6, y -0.2..11.5 located on the scan |
| zb band z-16.2--13.2 | region | scan_to_cad | reported | reported | n 19650 · p95 0.2388 · max 0.6791 | n 19650 · p95 0.2388 · max 0.6791 | — |
| zb band z-16.2--13.2 | region | cad_to_scan | reported | reported | n 19180 · p95 0.4093 · max 1.0908 | n 17244 · p95 0.264 · max 0.8116 | — |
| zb caps z<-19.2 | region | scan_to_cad | reported | reported | n 26032 · p95 0.1294 · max 0.7367 | n 26032 · p95 0.1294 · max 0.7367 | — |
| zb caps z<-19.2 | region | cad_to_scan | reported | reported | n 21592 · p95 0.1093 · max 0.2181 | n 21535 · p95 0.1093 · max 0.2151 | — |
| zb collars z-19.2--16.2 | region | scan_to_cad | reported | reported | n 20302 · p95 0.2906 · max 0.9223 | n 20302 · p95 0.2906 · max 0.9223 | — |
| zb collars z-19.2--16.2 | region | cad_to_scan | reported | reported | n 15021 · p95 0.5579 · max 1.1364 | n 10207 · p95 0.3052 · max 0.892 | — |
| zb rim z0-5 | region | scan_to_cad | reported | reported | n 68937 · p95 0.2982 · max 0.7235 | n 68937 · p95 0.2982 · max 0.7235 | — |
| zb rim z0-5 | region | cad_to_scan | reported | reported | n 93204 · p95 0.9972 · max 3.0006 | n 84301 · p95 0.4065 · max 2.816 | — |
| zb tab z>5 | region | scan_to_cad | reported | reported | n 54977 · p95 0.1721 · max 0.7615 | n 54977 · p95 0.1721 · max 0.7615 | — |
| zb tab z>5 | region | cad_to_scan | reported | reported | n 61464 · p95 0.1804 · max 0.8166 | n 60876 · p95 0.1764 · max 0.8166 | — |
| zb tiers z-13.2-0 | region | scan_to_cad | reported | reported | n 104469 · p95 0.2156 · max 0.737 | n 104469 · p95 0.2156 · max 0.737 | — |
| zb tiers z-13.2-0 | region | cad_to_scan | reported | reported | n 89539 · p95 2.6565 · max 5.4724 | n 75981 · p95 0.2722 · max 5.4059 | — |

### Masks (masked and unmasked are both shown above)

| mask | direction | why | fraction removed | stats inside |
|---|---|---|---|---|
| M3 open boundary | cad_to_scan | distance from CAD to the edge of a scan hole (23 open loops, INTAKE_CARD §2-§3) is not a surface deviation | 0.0887 | n: 26608; rms: 1.6433; mean: 1.0983; p50: 0.5675; p95: 3.7301; p99: 4.5877; max: 5.4724 |
| M4 skin normal | cad_to_scan | a CAD point whose nearest scan triangle faces >70 deg away is an occluded/opposite-wall correspondence, not a skin deviation | 0.024 | n: 7191; rms: 1.5864; mean: 1.0935; p50: 0.6182; p95: 3.4744; p99: 4.4826; max: 5.4035 |

### Mask sensitivity

| band | direction | stats | variant |
|---|---|---|---|
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.3482; max_over_by: 4.6724 | cad_to_scan | n: 292809; rms: 0.5066; mean: 0.1642; p50: 0.0419; p95: 0.6482; p99: 2.9894; max: 5.4724 | all masks except M3 open boundary |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 4.6059 | cad_to_scan | n: 273392; rms: 0.2798; mean: 0.0977; p50: 0.0384; p95: 0.2976; p99: 1.2892; max: 5.4059 | all masks except M4 skin normal |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.0467; max_over_by: 4.6567 | cad_to_scan | n: 283616; rms: 0.3159; mean: 0.1084; p50: 0.0398; p95: 0.3467; p99: 1.3179; max: 5.4567 | M3 open boundary radius 0.0 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 4.6567 | cad_to_scan | n: 277388; rms: 0.2765; mean: 0.0963; p50: 0.0386; p95: 0.2931; p99: 1.2506; max: 5.4567 | M3 open boundary radius 0.2 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 4.6567 | cad_to_scan | n: 274953; rms: 0.2691; mean: 0.0944; p50: 0.0383; p95: 0.2877; p99: 1.2303; max: 5.4567 | M3 open boundary radius 0.4 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 4.6059 | cad_to_scan | n: 270144; rms: 0.2637; mean: 0.0928; p50: 0.0378; p95: 0.2832; p99: 1.2228; max: 5.4059 | M3 open boundary radius 0.8 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 4.5549 | cad_to_scan | n: 257883; rms: 0.2567; mean: 0.0903; p50: 0.0367; p95: 0.2758; p99: 1.2203; max: 5.3549 | M3 open boundary radius 1.5 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 4.5549 | cad_to_scan | n: 237599; rms: 0.224; mean: 0.0807; p50: 0.0352; p95: 0.2534; p99: 0.7465; max: 5.3549 | M3 open boundary radius 2.5 mm |

### Over-band point clusters, scan → CAD (> 0.8 mm)

9 points (0 fraction) in 0 clusters ≥ 20 pts.

### Over-band point clusters, CAD → scan (> 0.8 mm)

15903 points (0.053 fraction) in 7 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 7639 | [-9.212, 5.312, -1.527] | [0.98, 23.593] | [16, 177.2] | 5.4724 | **UNEXPLAINED** |
| 1 | 4179 | [-11.121, 12.277, 1.416] | [11.707, 26.076] | [72, 161.4] | 2.816 | **UNEXPLAINED** |
| 2 | 1938 | [-13.362, -8.333, -8.817] | [12.734, 19.118] | [199.3, 224] | 3.7451 | **UNEXPLAINED** |
| 3 | 1905 | [12.563, -8.18, -9.687] | [12.029, 18.47] | [315.8, 336.8] | 4.454 | **UNEXPLAINED** |
| 4 | 74 | [21.576, -8.617, -17.958] | [21.635, 26.856] | [335.1, 342.4] | 1.1364 | **UNEXPLAINED** |
| 5 | 53 | [-28.91, -11.154, -15.412] | [30.232, 33.005] | [198.6, 203.5] | 1.0908 | **UNEXPLAINED** |
| 6 | 29 | [-19.605, -18.793, 0.917] | [26.825, 27.541] | [223.2, 224.6] | 0.9344 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 0.0676°, origin offset 0.0135 mm, point disagreement p95 0.0561 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (within).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| whole part CAD->scan observable (p95 0.633 > 0.30, max 5.422 > 0.80) | 15,903 of 300,000 CAD samples (5.30%) over 0.8 mm; 15,661 (98.5%) lie in four unscanned openings (shroud interior 7639, shroud-to-rim slot 4179, screw bores 1938 + 1905) whose CAD surfaces are assumptions with no scan behind them; 74 on the B3 recess ceiling, 53 on the B1 wedge floor, 29 at a scan hole on the -Y hoop notch wall, 86 in small groups. Only 1.52% of the CAD is ray-unobservable, so the observable split does not remove the openings. Informational (not a gate, not a mask): CAD->scan raw outside the four opening boxes reads p95 0.276 / max 1.136 (242 pts > 0.8). Datum frame reads p95 0.628 / max 5.416, so not a registration effect. Three geometry loops moved this p95 only 0.674 -> 0.650 -> 0.633: geometry built from this scan cannot close it. | (a) owner accepts BAND_NOT_MET with the openings declared as assumed geometry (ACCEPT-BAND in DECISIONS.md citing this gate.json); (b) supply data: a re-scan of the shroud interior, slot and bores, or depth / pin-gauge readings, then re-run; (c) HALT. Not REVISE: loop 3 of 3 is used and no geometry change from the existing scan can clear it. |
| whole part scan->CAD max (0.922 > 0.80; p95 0.237 passes; unmasked = masked, no scan masks) | 9 of 294,367 scan vertices (0.003%) over 0.8 mm, one group of < 20 pts at the tip of the B1 side-collar tilted cut inside the B1 cap-collar gap (-28.9, 1.15, -16.6): the scanned surface curves where the CAD cut is a plane (max 0.122 over band). it1 81 pts / 1.690, it2 24 / 1.062, it3 9 / 0.922. Datum frame max 0.911. This is a geometry approximation of real scan material in an occluded ~1 mm gap, not a data gap; in principle a finer side-collar cut would clear it, but loop 3 of 3 is used, and fixing it alone would not pass the part because of the CAD->scan miss above. | (a) owner accepts the 9-point, 0.12 mm over-band residual inside the B1 cap-collar gap (ACCEPT-BAND); (b) owner authorises one extra geometry loop beyond the 3-loop limit to shape the B1 side-collar cut tip (would not clear the CAD->scan miss); (c) HALT. |

Missed band(s): `scan_to_cad:masked: p95 0.237 max 0.922 vs 0.3/0.8`; `cad_to_scan_observable: p95 0.633 max 5.422 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | no Tier-1 (scan-only job, no calipers) |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | pass | QA datum not ICP'd to its own CAD; gate uses QA's own ICP on the raw full-res scan; no expected value taken from params.json or the builder. The builder self-check in MODELING_PLAN §8 (datum frame, 200k samples) is a consistency check, not independent evidence, and is not compared. |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 0 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | finding | Every intake feature E01-E18 is present in CAD sections. Finding (carried from it2, reduced not removed): the scanned surface at the tip of the B1 side-collar tilted cut inside the B1 cap-collar gap, around (-28.9, 1.15, -16.6), curves where the CAD cut is a straight plane; 9 scan pts over 0.8 (max 0.922, it2 24 pts / 1.062). Logos/icons (E13) not modelled (declared cosmetic). No invented CAD feature except assumed closures in unscanned regions (shroud interior floor z -2.33, slot floor, through-bores, recess ceilings). |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | finding | export_check.json (datum and scan frames) and fillets.json: 22 fillets, 20 OK, 2 REDUCED: F02 rim top outer edge 0.5451 -> 0.4777, F13 shroud top inner edge 0.6254 -> 0.5031 (wall too thin for both measured rounds), declared in MODELING_PLAN §0. Unchanged from it1/it2. No FAILED/NO_EDGES. |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | fresh agent, own scripts; see independence |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | pass | Same protocol as it2 (and it1): regime.json, zones.json, masks.json, datum_spec.json, icp_scan_masks.json byte-identical to _it2_SUPERSEDED/qa; ICP params identical (3M/seed 11, 300k/seed 13, 70 deg, 0.8 mm, 3.0 mm, cap 60, tol 1e-6); sampling identical (all scan verts, 300k CAD seed 2, k 8, n_samp 3M seed 0; observability 20k seed 5, 0.5 mm, 60 deg cone); same overlay panel set. Only the CAD changed. After ICP it1 -> it2 -> it3: scan->CAD p95 0.243 -> 0.243 -> 0.237, max 1.690 -> 1.062 -> 0.922, scan pts >0.8 81 -> 24 -> 9; CAD->scan observable p95 0.674 -> 0.650 -> 0.633, max 5.119 -> 5.358 -> 5.422; CAD->scan raw p95 0.973 -> 0.943 -> 0.931; CAD pts >0.8 16,672 -> 16,189 -> 15,903. Improvement is geometry (it3: sloped recess profiles, B1/B3 middle sectors), not protocol. |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | pass | no pass depends on a mask |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | pass | 374 faces, analytic area share 95.4% (plane 201, cylinder 110, torus 36, cone 3, revolution 6, extrusion 2, bspline 16). model.py grep: no loft(, ruled, Polyline, sweep, spline; Wire.make_polygon builds the tab YZ profile (fitted plane-line intersections) and, new in it3, a 5-point (r,z) recess profile that is revolved (recess_cone -> planes + cones), not a scan-slice stack. |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | pass | photo 1 (back + 3/4 front) and photo 2 (front) walked: shroud with white pin header, 2 screw holes, tab with hole and side flanges, 4 latch hoops, stepped tiers, 3 caps with slanted side tops, collars; all present in CAD except the header pins and logos/icons (declared). |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict BAND_NOT_MET |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 3 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L1 | Scan-only: no calipers, so Tier-1 did not run (absent, not passed) and absolute scale is not caliper-verified (CHK-SCALE flag at intake). no Tier-1 (no calipers run). | any caliper reading (envelope X/Y, a cap diameter, the tab hole) | qa/gate.json#limitations |
| L2 | Unscanned regions are modelled from assumptions: connector shroud interior depth, shroud-to-rim slot floor, screw through-bores, cap-collar recess ceilings. They hold almost all of the observable CAD-to-scan band miss, which the owner accepted (decisions/accept_band.md). | a re-scan covering the shroud interior, the slot and the bores, or depth / pin-gauge readings of them | qa/VERDICT.md |
| L3 | The functional zones Z1-Z6 are reported per zone only: the baseline-skill regime has no interface band. | a project spec that bands the interfaces | qa/gate.json#limitations |
| L4 | Two fillets were built smaller than measured because the wall is thinner than the two measured top rounds together: rim top outer edge and shroud top inner edge (REDUCED in build/export_check.json). | a caliper reading of the rim and shroud wall thickness | build/export_check.json#datum.fillets |
| L5 | The loose button caps are fused to the housing at their scanned pose (the middle cap sits slightly tilted in its bore); the solid is the assembly as scanned. | owner request for a per-part STEP or the nominal cap pose | qa/gate.json#limitations |
| L6 | Overlays and zoom sections are drawn in the builder datum frame, before the verifier's ICP correction of 0.0227 mm. | an ICP correction above the overlay tolerance on a re-run | qa/gate.json#deviation.registration |

## 12. Assumptions and invented geometry

Parameters not measured on the scan or by caliper (source tag from `measure/params.json`):

| parameter | value | source | evidence |
|---|---|---|---|
| `shroud_slot_note` | 0 | assumed | intake/coverage.json loop 2; measure probe in make_params docstring |
| `tab_end_under_edge_note` | 0 | assumed | measure/figures/m_edges.json#tab_end_under_edge |

- Connector shroud interior (header, pins, floor) is not scanned; the interior pocket is cut down to the deepest scanned wall point. _(source: assumed; measure/params.json#shroud_inner_floor_z)_
- Screw through-bore between the back counterbore and the front bore is not scanned; it is assumed continuous at the measured bore radius, and the front bore stops where the scan stops seeing it. _(source: assumed; measure/params.json#screw_L_front_top_z)_
- The narrow slot between the connector shroud and the rim is closed at the floor plane (no scan below it). _(source: assumed; measure/params.json#shroud_slot_note)_
- The loose button caps are fused to the housing at their scanned pose; the clearance between each cap and its bore is modelled only as far up as the scan saw it. _(source: assumed; build/MODELING_PLAN.md)_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** manufacture or tooling of any part of the assembly until the functional interfaces (caps, collars, screw holes, tab hole, connector shroud) are calipered
- **Not fit for:** separate-part use: housing, cover and caps are fused into one solid; a multi-body STEP is a separate job
- **Not fit for:** the connector interior (header and pins were not scanned)
- Fit for: envelope, packaging and fit studies of the scanned assembly in the machine front panel
- Fit for: a design-intent starting model for the housing (parametric build123d source and parameter table included)
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): Not an approved model. Not fit for tooling, manufacture or fit-critical use of the connector shroud interior, the shroud-to-rim slot, the screw bores or the cap-collar gaps (assumed, unscanned geometry). Scale is not caliper-verified. The outer housing, tab, caps and back floor agree with the scan within p95 0.30 mm scan->CAD (whole-part scan->CAD p95 0.237, max 0.922 at one 9-point spot); that is the only claim.

## 14. Human acceptance of the band miss

Accepted by **Ikbal (owner, question card)** on 2026-09-28 (`DECISIONS.md`, ACCEPT-BAND): Accept and deliver: accepts scan_to_cad:masked (max) and cad_to_scan_observable (p95, max) band misses, gate 1e9b7dcea587 (created 2026-09-28T08:54:19+00:00); 98.5% of the CAD->scan miss is in unscanned openings (shroud interior, shroud-to-rim slot, screw bores).. Record: `decisions/accept_band.md` (sha256 `5e5024e70a6e51563f47995f49fd83b9eccae9caa185af142f66b66f79b36e46`).

## 15. Reproduction

```
cd build && python model.py
python <skills>/stl-re-deliver/scripts/repro_check.py --run <run>
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-E02_control-button-board.step | 36865.1716 | 0 | 0 | yes | yes | no |
| OD-E02_control-button-board_datum.step | 36865.1716 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 16. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | 1e9b7dcea5876e4ea32e9ca8b2c01778b1eb9dcfdc6b413d423b8f514eee6332 |
| `measure/params.json` | a58fe74b34a502f3b45887df566acec3d2af3d16ed231ed0c98766059982dd4d |
| `build/export_check.json` | 2d238aa0fb933a899e0e4c7aec100c08f52dd633317b71b3b6411c8b2773015d |
| `intake/alignment.json` | 2e300002ef7139dcb81437f825bf7d668fc56cc3107a75f2d3b521e9630ff57e |
| `deliver/repro.json` | 21f10a65ae34e92393cfb5ad00d250518d0fbc5d54d16ac2e094670683a84b6e |
| `deliver/limitations.json` | 79dc2b776c5a1ebe5856a42a96cfe50625cf9b6b686c64e46265f818c1b0b89c |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
