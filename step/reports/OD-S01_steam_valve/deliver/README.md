# OD-S01_steam-valve — STL → STEP reverse-engineering delivery

**Verdict: `BAND_NOT_MET`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 2 of 3 (earlier iterations kept: `_it1_SUPERSEDED/`).  
**Verification independence (CHK-INDEP):** pass — fresh agent, own scripts; see independence  

> **A deviation band was NOT met.** Delivered only under the recorded human acceptance below (by Ikbal (owner, question card), 2026-09-28, record `decisions/accept_band.md`).

## 1. The part

![reference photo](../input/photos/4.png)

De'Longhi-type rotary steam valve assembly (cap with splined spindle and 3-fold cam ring, valve body with top clip port, two side hose ports, hose barb, microswitch), scanned as one mesh and delivered as one fused solid.

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-S01_steam-valve_datum.step` | datum | 1 | yes | yes | 351 | 15837.5497 | max: [18, 18.4357, 48.57]; min: [-20.44, -21.92, -14.76]; size: [38.44, 40.3557, 63.33] |
| `build/OD-S01_steam-valve.step` | scan | 1 | yes | yes | 351 | 15837.5497 | max: [-0.2895, 7.6482, -167.3879]; min: [-48.7089, -40.0755, -222.5775]; size: [48.4194, 47.7236, 55.1896] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Intake: scan hash and health, working copy, datum = cap disc outer face (z 0, +Z into the body), upper valve column axis, microswitch face normal to +X (intake/alignment.json).
2. Measure: sections, unwrapped r(theta,z) maps, IRLS cylinder fits and plane percentiles on the aligned scan; every value in measure/params.json with its estimator and evidence.
3. Rebuild: one (r,z) revolve plus a 3-fold cam ring of sector solids, drafted port tubes and plates, barb, microswitch, cut tools subtracted once; one valid closed solid, all faces analytic.
4. Verify: two independent QA agents (iteration one REVISE, iteration two BAND_NOT_MET), each with its own ICP, two-way full-resolution deviation, zones, masks, overlays, verdict under the declared regime.
5. Deliver: README, MANIFEST, fresh-process reproducibility, one zip with deliverables and all source files.

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | upper valve column axis ∩ cap disc outer face | — | — |
| primary (plane) | cap disc outer face (knob side, perpendicular to the splined spindle) | 0.0343 / 0.1039 | the cap disc outer face is the flat the control knob side seats against; it is perpendicular to the splined spindle (rotation axis of the valve) |
| secondary (axis) | upper valve column OD (r~5.3) | 0.0448 / 0.5205 | valve spool column, coaxial with the spindle |
| clock | plane_normal: microswitch outer face normal -> +X (angle -160.6241°) | — | — |

Measured tilt: 0.7612° (common slope, per-feature intercept, 10 stations over 1 feature(s), z 37.709..41.800 vs frame Z). Scale factor applied: 1. Scan noise floor: 0.036 mm (rms of RANSAC+SVD plane on cap disc outer face (knob side, perpendicular to the splined spindle) (3497 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
-0.896297   0.012040   0.443291   61.276642
 0.210509  -0.868270   0.449215   77.492535
 0.390304   0.495947   0.775693   189.844183
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: scan 111 (total 111). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `bar330` | [12.3, -6.74, -5.6, 10.85, 12.22] | mm | [12.3, -6.737, -5.6, 10.846, 12.222] | round-within-noise | scan | 0.1 | no | measure/figures/rz_b.png |
| `barb_axis_xz` | [-0.09, 30.76] | mm | [-0.086, 30.762] | round-within-noise | scan | 0.036 | yes | measure/figures/sec_ybarb.png |
| `barb_back_y` | -18.45 | mm | -18.5..-18.4 | keep-measured | scan | 0.1 | no | measure/figures/sec_ybarb.png |
| `barb_bore_r` | 1.42 | mm | 1.42 | keep-measured | scan | 0.1 | no | measure/figures/sec_ybarb.png |
| `barb_collar` | [-8.67, -7.3, 4.88] | mm | [-8.667, -7.298, 4.88] | round-within-noise | scan | 0.036 | no | measure/figures/sec_ybarb.png |
| `barb_crest` | [-19.25, 3.45] | mm | [-19.25, 3.45] | keep-measured | scan | 0.036 | yes | measure/figures/sec_ybarb.png |
| `barb_rib` | [-0.32, 0.23, -8.67, 36.85, -4.5, 37.53] | mm | [-0.317, 0.231, -8.67, 36.85, -4.5, 37.527] | round-within-noise | scan | 0.15 | no | measure/figures/sec_ybarb.png |
| `barb_shaft_r` | 2.7 | mm | 2.695 | round-within-noise | scan | 0.036 | yes | measure/figures/sec_ybarb.png |
| `barb_tip` | [-21.92, 1.95] | mm | [-21.92, 1.95] | keep-measured | scan | 0.036 | no | measure/figures/sec_ybarb.png |
| `blk120_lo` | [100, 150, 14, 12.4] | mm | [100, 150, 14, 12.39] | round-within-noise | scan | 0.2 | no | measure/figures/rz_b.png |
| `blk120_slope` | [104, 12, 125, 15.05] | mm | [104, 12, 125, 15.048] | round-within-noise | scan | 0.5 | no | measure/figures/unwrap_low.png |
| `blk120_up` | [104, 142, 10.05, 14, 15.05] | mm | [104, 142, 10.05, 14, 15.048] | round-within-noise | scan | 0.2 | no | measure/figures/rz_b.png |
| `blk240` | [212, 269, 12.6, 12.3] | mm | [212, 269, 12.6, 12.3] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `brk_box` | [-0.29, 8.37, 8.3, 13.35, 15.75, 23.31] | mm | [-0.29, 8.37, 8.3, 13.35, 15.75, 23.31] | keep-measured | scan | 0.2 | no | measure/figures/sec_y_pos.png |
| `cam_flank_z` | [2.5, 8] | mm | [2.5, 8] | keep-measured | scan | 0.1 | no | measure/figures/unwrap_low.png |
| `cam_floor_1` | [10.58, 6] | mm | [10.58, 6] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `cam_floor_2` | [9.5, 8.2] | mm | [9.5, 8.2] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `cam_phase` | 1 | deg | [1, 121.3, 240] | symmetry | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `cam_post_half` | 32.1 | deg | [32.2, 32.5, 31.2] | symmetry | scan | 0.3 | no | measure/figures/unwrap_low.png |
| `cam_post_r` | 12.65 | mm | 12.63..12.78 | keep-measured | scan | 0.1 | no | measure/figures/unwrap_low.png |
| `cam_tooth_half_bot` | 22.6 | deg | [22.6, 22.6, 22.55] | symmetry | scan | 0.3 | no | measure/figures/unwrap_low.png |
| `cam_tooth_half_top` | 13.3 | deg | [13.4, 13.5, 12.9] | symmetry | scan | 0.3 | no | measure/figures/unwrap_low.png |
| `cam_tooth_r` | 12.49 | mm | 12.34..12.59 | keep-measured | scan | 0.12 | no | measure/figures/unwrap_low.png |
| `cam_top_z` | 8.2 | mm | 8.16..8.3 | keep-measured | scan | 0.1 | no | measure/figures/unwrap_low.png |
| `cap_r` | 14.36 | mm | 14.364 | round-within-noise | scan | 0.036 | yes | measure/figures/sec_zlow.png |
| `cap_slot_1` | [3.16, 8.69, 131.7, 5, 2.1] | mm | [3.04, 8.83, 131.5, 4.6, 2.22] | symmetry | scan | 0.3 | no | measure/figures/sec_z_cap.png |
| `cap_slot_2` | [3.16, -8.69, 48.3, 5, 2.1] | mm | [3.28, -8.55, 48.1, 5.77, 2.58] | symmetry | scan | 0.3 | no | measure/figures/sec_z_cap.png |
| `cap_slot_3` | [-10.87, 0.13, 88.3, 2, 0.8] | mm | [-10.87, 0.13, 88.3, 2, 0.8] | keep-measured | scan | 0.5 | no | intake/figures/view_mz.png |
| `cap_top_z` | 2.13 | mm | 2.131 | round-within-noise | scan | 0.036 | no | measure/figures/rz_a.png |
| `col_top_fillet` | 1.5 | mm | 1.4..1.6 | keep-measured | scan | 0.15 | no | measure/figures/profiles.json#column_top |
| `col_window_cone_1` | [8.75, 10.2] | mm | [8.75, 10.2] | keep-measured | scan | 0.12 | no | measure/figures/profiles.json#window_180 |
| `col_window_cone_2` | [6.15, 14.4] | mm | [6.15, 14.4] | keep-measured | scan | 0.12 | no | measure/figures/profiles.json#window_180 |
| `col_window_cone_3` | [6.15, 15.4] | mm | [6.15, 15.4] | keep-measured | scan | 0.12 | no | measure/figures/profiles.json#window_180 |
| `col_windows_1` | [160, 205] | deg | [160, 205] | keep-measured | scan | 2 | no | measure/figures/unwrap_low.png |
| `col_windows_2` | [340, 385] | deg | [340, 385] | keep-measured | scan | 2 | no | measure/figures/unwrap_low.png |
| `collar_sectors_1` | [328, 388, 9.45] | mm | [328, 388, 9.45] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `collar_sectors_2` | [152, 210, 9.85] | mm | [152, 210, 9.85] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `collar_sectors_3` | [270, 288, 9.55] | mm | [270, 288, 9.55] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `collar_sectors_4` | [72, 99, 9.42] | mm | [72, 99, 9.42] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `collar_z` | 10.2 | mm | 10.0..10.4 | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `column_r` | 8.6 | mm | 8.603 | round-within-noise | scan | 0.036 | yes | measure/figures/rz_a.png |
| `column_top_z` | 27.67 | mm | 27.67 | round-within-noise | scan | 0.036 | no | measure/figures/rz_a.png |
| `fin` | [12.79, -4.76, -3.52, 8.52] | mm | [12.794, -4.758, -3.523, 8.518] | round-within-noise | scan | 0.1 | no | measure/figures/sec_zlow.png |
| `finger_slot` | [10.5, 6.5] | mm | [10.5, 6.5] | keep-measured | scan | 0.3 | no | measure/figures/unwrap_low.png |
| `groove_profile_1` | [5.35, 32.9] | mm | [5.35, 32.9] | keep-measured | scan | 0.08 | no | measure/figures/profiles.json#neck_groove |
| `groove_profile_2` | [4.85, 34] | mm | [4.85, 34] | keep-measured | scan | 0.08 | no | measure/figures/profiles.json#neck_groove |
| `groove_profile_3` | [4.02, 34.75] | mm | [4.02, 34.75] | keep-measured | scan | 0.08 | no | measure/figures/profiles.json#neck_groove |
| `groove_profile_4` | [4.02, 35.35] | mm | [4.02, 35.35] | keep-measured | scan | 0.08 | no | measure/figures/profiles.json#neck_groove |
| `groove_profile_5` | [4.63, 36] | mm | [4.63, 36] | keep-measured | scan | 0.08 | no | measure/figures/profiles.json#neck_groove |
| `groove_profile_6` | [5.21, 36.8] | mm | [5.21, 36.8] | keep-measured | scan | 0.08 | no | measure/figures/profiles.json#neck_groove |
| `groove_profile_7` | [5.38, 37.3] | mm | [5.38, 37.3] | keep-measured | scan | 0.08 | no | measure/figures/profiles.json#neck_groove |
| `holder_edge` | [3.86, 7, 6.6, 4.9] | mm | [3.86, 7, 6.6, 4.9] | keep-measured | scan | 0.3 | no | measure/figures/sec_z_brk.png |
| `holder_y0` | -4.97 | mm | -4.974 | round-within-noise | scan | 0.2 | no | measure/figures/sec_z_brk.png |
| `lug320` | [312.1, 328.5, 10.41, 22.26, 23.16] | mm | [312.1, 328.5, 10.41, 22.26, 23.163] | round-within-noise | scan | 0.1 | no | measure/figures/rz_b.png |
| `neck_lo_r` | 5.35 | mm | 5.346 | round-within-noise | scan | 0.036 | no | measure/figures/rz_a.png |
| `neck_up_r` | 5.38 | mm | 5.382 | round-within-noise | scan | 0.036 | yes | measure/figures/rz_a.png |
| `pl_axis_yz` | [-14.05, 18.17] | mm | [-14.05, 18.17] | keep-measured | scan | 0.036 | yes | measure/figures/sec_xport_lo.png |
| `pl_plate_edge_1` | [-20.1, -7.25] | mm | [-20.1, -7.25] | keep-measured | scan | 0.3 | no | measure/figures/sec_zplates.png |
| `pl_plate_edge_2` | [-8.61, -2.72] | mm | [-8.61, -2.72] | keep-measured | scan | 0.3 | no | measure/figures/sec_zplates.png |
| `pl_plate_faces_1` | [-6.5, 24.221, -13.5, 23.689, 0.929] | mm | [-6.5, 24.221, -13.5, 23.689, 0.929] | keep-measured | scan | 0.08 | no | measure/figures/sec_xport_lo.png |
| `pl_plate_faces_2` | [-5.5, 15.717, -8.5, 15.598, 0.896] | mm | [-5.5, 15.717, -8.5, 15.598, 0.896] | keep-measured | scan | 0.08 | no | measure/figures/sec_xport_lo.png |
| `port_bore_r` | 4 | mm | 3.932..4.048 | keep-measured | scan | 0.036 | yes | measure/figures/sec_xport_up.png |
| `port_col_x` | -0.12 | mm | [-0.129, -0.117] | mean-of-n | scan | 0.05 | no | measure/figures/sec_xport_up.png |
| `port_end_x` | -20.44 | mm | -20.47..-20.41 | keep-measured | scan | 0.036 | yes | measure/figures/sec_xport_up.png |
| `port_junction_x0` | -4 | mm | -4 | keep-measured | scan | 0.5 | no | measure/figures/sec_xport_up.png |
| `port_orifice_r` | 2 | mm | 1.94..2.09 | keep-measured | scan | 0.1 | no | measure/figures/sec_xport_up.png |
| `port_r_end` | 5.47 | mm | 5.461..5.478 | keep-measured | scan | 0.036 | yes | measure/figures/sec_xport_up.png |
| `port_r_root` | 5.58 | mm | 5.568..5.586 | keep-measured | scan | 0.036 | no | measure/figures/sec_xport_up.png |
| `port_trim` | [-5, 13.52, -13.3] | mm | [-5, 13.52, -13.3] | keep-measured | scan | 0.2 | no | measure/figures/sec_xport_up.png |
| `port_web_x0` | -15.5 | mm | [-15.5, -15.5] | mean-of-n | scan | 0.15 | no | measure/figures/sec_xport_up.png |
| `port_web_x1` | -13.625 | mm | [-13.5, -13.75] | mean-of-n | scan | 0.15 | no | measure/figures/sec_xport_up.png |
| `port_window` | [-8, 4] | mm | [-8, 4] | keep-measured | scan | 0.5 | no | measure/figures/zoom_up_py.png |
| `pu_axis_yz` | [12.92, 30.06] | mm | [12.92, 30.06] | keep-measured | scan | 0.036 | yes | measure/figures/sec_xport_up.png |
| `pu_lip` | [-1.34, 9.4, 22.6] | mm | [-1.337, 9.4, 22.595] | round-within-noise | scan | 0.1 | no | measure/figures/sec_xport_up.png |
| `pu_plate_edge_1` | [-19.38, 6.25] | mm | [-19.38, 6.25] | keep-measured | scan | 0.2 | no | measure/figures/sec_zplates.png |
| `pu_plate_edge_2` | [-9.74, 2.96] | mm | [-9.74, 2.96] | keep-measured | scan | 0.2 | no | measure/figures/sec_zplates.png |
| `pu_plate_faces_1` | [6.5, 36.316, 12.5, 35.632, 0.868] | mm | [6.5, 36.316, 12.5, 35.632, 0.868] | keep-measured | scan | 0.08 | no | measure/figures/sec_xport_up.png |
| `pu_plate_faces_2` | [6.5, 24.05, 12.5, 24.487, 0.928] | mm | [6.5, 24.05, 12.5, 24.487, 0.928] | keep-measured | scan | 0.08 | no | measure/figures/sec_xport_up.png |
| `rib_sectors_1` | [17, 28, 9.36] | mm | [17, 28, 9.36] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `rib_sectors_2` | [72, 99, 9.42] | mm | [72, 99, 9.42] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `rib_sectors_3` | [151, 160, 9.56] | mm | [151, 160, 9.56] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `rib_sectors_4` | [201, 210, 9.9] | mm | [201, 210, 9.9] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `rib_sectors_5` | [270, 287, 9.55] | mm | [270, 287, 9.55] | keep-measured | scan | 0.2 | no | measure/figures/unwrap_low.png |
| `rib_top_z` | 13 | mm | 12.8..13.4 | keep-measured | scan | 0.3 | no | measure/figures/unwrap_low.png |
| `spindle_flat_x` | 2.43 | mm | 2.40..2.47 | keep-measured | scan | 0.036 | yes | measure/figures/sec_spindle.png |
| `spindle_key_x` | 3.82 | mm | 3.82 | keep-measured | scan | 0.036 | yes | measure/figures/sec_spindle.png |
| `spindle_key_y` | [-0.74, 0.76] | mm | [-0.74, 0.759] | round-within-noise | scan | 0.036 | yes | measure/figures/sec_spindle.png |
| `spindle_r` | 3.7 | mm | 3.68..3.75 | keep-measured | scan | 0.12 | yes | measure/figures/spline_pitch.json |
| `spindle_tip_chamfer` | 0.7 | mm | 0.6..0.8 | keep-measured | scan | 0.1 | no | measure/figures/rz_a.png |
| `spindle_tip_z` | -14.76 | mm | -14.756 | round-within-noise | scan | 0.036 | no | measure/figures/sec_spindle.png |
| `sw_blade_top_z` | 33.3 | mm | 33.295 | round-within-noise | scan | 0.036 | no | measure/figures/sec_x_sw.png |
| `sw_blade_x` | [10.51, 14.09] | mm | [10.514, 14.085] | round-within-noise | scan | 0.036 | no | measure/figures/sec_x_sw.png |
| `sw_blade_y_1` | [-0.76, -0.26] | mm | [-0.758, -0.264] | round-within-noise | scan | 0.036 | no | measure/figures/sec_x_sw.png |
| `sw_blade_y_2` | [7.94, 8.46] | mm | [7.941, 8.459] | round-within-noise | scan | 0.036 | no | measure/figures/sec_x_sw.png |
| `sw_bump` | [10.7, 13.9, 1.79, 3.84, 14.39] | mm | [10.7, 13.895, 1.794, 3.837, 14.387] | round-within-noise | scan | 0.1 | no | measure/figures/sec_z_brk.png |
| `sw_tab` | [8.6, 18, 10, 11.51, 18.02, 21.11] | mm | [8.6, 18, 10, 11.51, 18.02, 21.11] | keep-measured | scan | 0.036 | no | measure/figures/sec_y_pos.png |
| `sw_x` | [9.73, 15.65] | mm | [9.732, 15.652] | round-within-noise | scan | 0.036 | no | measure/figures/sec_x_sw.png |
| `sw_y` | [-9.66, 10.02] | mm | [-9.66, 10.023] | round-within-noise | scan | 0.036 | no | measure/figures/sec_x_sw.png |
| `sw_z` | [15.74, 25.11] | mm | [15.739, 25.112] | round-within-noise | scan | 0.036 | no | measure/figures/sec_x_sw.png |
| `top_blk_bot_z` | 43.36 | mm | 43.358 | round-within-noise | scan | 0.036 | no | measure/figures/sec_ztop.png |
| `top_blk_edge_r` | 1.7 | mm | 1.5..1.9 | keep-measured | scan | 0.2 | no | measure/figures/sec_x_top.png |
| `top_blk_top_z` | 47.4 | mm | 47.2..47.6 | keep-measured | scan | 0.2 | no | measure/figures/sec_ztop.png |
| `top_blk_x` | [-6.36, 6.33] | mm | [-6.356, 6.326] | round-within-noise | scan | 0.036 | yes | measure/figures/sec_ztop.png |
| `top_blk_y` | [-6.26, 6.16] | mm | [-6.263, 6.162] | round-within-noise | scan | 0.036 | yes | measure/figures/sec_ztop.png |
| `top_bore2` | [3.61, 43] | mm | [3.61, 43.007] | round-within-noise | scan | 0.15 | no | measure/figures/sec_ztop.png |
| `top_bore_bot_z` | 43.9 | mm | 43.8..44.0 | keep-measured | scan | 0.3 | no | measure/figures/sec_ztop.png |
| `top_bore_r` | 4.97 | mm | 4.974 | round-within-noise | scan | 0.125 | yes | measure/figures/sec_ztop.png |
| `top_cbore` | [5.45, 46.8] | mm | [5.45, 46.8] | keep-measured | scan | 0.25 | no | measure/figures/sec_ztop.png |
| `top_round_r` | 6.61 | mm | 6.613 | round-within-noise | scan | 0.036 | no | measure/figures/sec_ztop.png |
| `top_slot` | [0.85, 4.45, 44.63, 45.87] | mm | [0.84, 4.57, 44.61, 45.9] | symmetry | scan | 0.1 | no | measure/figures/sec_x_top.png |
| `top_z` | 48.57 | mm | 48.573 | round-within-noise | scan | 0.036 | yes | measure/figures/sec_ztop.png |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

| id | feature | params |
|---|---|---|
| F02 | core revolve: cap disc, cam pocket floors, column, neck, groove | [cap_r, cam_floor_1, cam_floor_2, column_r, neck_lo_r, groove_profile_1, neck_up_r] |
| F01 | spindle with D-flat and key | [spindle_r, spindle_flat_x, spindle_key_x, spindle_key_y] |
| F09 | 3-fold cam ring, shoulder blocks, collar, ribs | [cam_phase, cam_post_half, cam_tooth_half_bot, cam_tooth_half_top, blk120, blk240] |
| F03 | top clip port with slots and bore | [top_blk_x, top_blk_y, top_bore_r, top_slot] |
| F04/F05 | side ports: drafted tubes, plates, orifice webs, U-windows | [pu_axis_yz, pl_axis_yz, port_r_end, port_bore_r, port_window] |
| F06 | hose barb | [barb_axis_xz, barb_shaft_r, barb_crest] |
| F07/F08 | microswitch, blades, tab, bracket, holder | [sw_x, sw_y, sw_z, brk_box] |

## 7. Tier-1 — caliper dims re-measured on the STEP

**Tier-1 not run: no caliper dimensions exist.** Every dimension is scan authority (or operator spec); see the source column in §5. Absent is not passed.

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), iterations 41/60, converged yes, correction 0.1345° / 0.064 mm.  
Unobservable CAD fraction: 0.0277.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 250308 | 0.2131 | 0.0747 | 0.4495 | 0.8128 | 1.9395 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 250308 | 0.2131 | 0.0747 | 0.4495 | 0.8128 | 1.9395 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 0.4048 | 0.08 | 0.9336 | 1.7625 | 3.4655 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 279090 | 0.3551 | 0.0734 | 0.7774 | 1.5571 | 3.4651 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 19446 | 0.357 | 0.0765 | 0.7609 | 1.6318 | 2.8896 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.4495 max 1.9395 (n 250308) | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 0.7609 max 2.8896 (n 19446) | FAIL |
| zone:Z1_spindle:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.2838 max 1.3378 (n 16768) | FAIL |
| zone:Z2_cap_cam_ring:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.6148 max 1.5933 (n 46719) | FAIL |
| zone:Z3_top_clip_port:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.4248 max 0.89 (n 17649) | FAIL |
| zone:Z4_side_ports:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.2716 max 0.9564 (n 42323) | FAIL |
| zone:Z5_barb:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.1521 max 0.7638 (n 7270) | PASS |
| zone:Z6_microswitch:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.4741 max 0.8835 (n 25290) | FAIL |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| B1_z_below_0 | region | scan_to_cad | reported | reported | n 16768 · p95 0.2838 · max 1.3378 | n 16768 · p95 0.2838 · max 1.3378 | z bucket: spindle |
| B1_z_below_0 | region | cad_to_scan | reported | reported | n 12347 · p95 0.2887 · max 0.7853 | n 12171 · p95 0.2817 · max 0.605 | z bucket: spindle |
| B2_z_0_8p2 | region | scan_to_cad | reported | reported | n 46719 · p95 0.6148 · max 1.5933 | n 46719 · p95 0.6148 · max 1.5933 | z bucket: cap + cam ring |
| B2_z_0_8p2 | region | cad_to_scan | reported | reported | n 57601 · p95 0.6188 · max 1.651 | n 52376 · p95 0.5471 · max 1.2184 | z bucket: cap + cam ring |
| B3_z_8p2_15p4 | region | scan_to_cad | reported | reported | n 31120 · p95 0.4716 · max 1.5587 | n 31120 · p95 0.4716 · max 1.5587 | z bucket: collar, ribs, windows, switch base |
| B3_z_8p2_15p4 | region | cad_to_scan | reported | reported | n 37793 · p95 1.1319 · max 3.4655 | n 33817 · p95 0.8308 · max 3.4651 | z bucket: collar, ribs, windows, switch base |
| B4_z_15p4_27p7 | region | scan_to_cad | reported | reported | n 84036 · p95 0.424 · max 1.9395 | n 84036 · p95 0.424 · max 1.9395 | z bucket: column, lower port, switch |
| B4_z_15p4_27p7 | region | cad_to_scan | reported | reported | n 102894 · p95 0.8558 · max 3.0008 | n 97957 · p95 0.6161 · max 3.0008 | z bucket: column, lower port, switch |
| B5_z_27p7_43p4 | region | scan_to_cad | reported | reported | n 54016 · p95 0.3119 · max 1.8766 | n 54016 · p95 0.3119 · max 1.8766 | z bucket: neck, groove, upper port, barb |
| B5_z_27p7_43p4 | region | cad_to_scan | reported | reported | n 70685 · p95 1.2938 · max 2.9197 | n 65504 · p95 1.2655 · max 2.9197 | z bucket: neck, groove, upper port, barb |
| B6_z_above_43p4 | region | scan_to_cad | reported | reported | n 17649 · p95 0.4248 · max 0.89 | n 17649 · p95 0.4248 · max 0.89 | z bucket: top clip port |
| B6_z_above_43p4 | region | cad_to_scan | reported | reported | n 18680 · p95 0.7611 · max 2.097 | n 17265 · p95 0.6661 · max 2.097 | z bucket: top clip port |
| I1_top_bore_interior | interior | scan_to_cad | reported | reported | n 2725 · p95 0.5156 · max 0.89 | n 2725 · p95 0.5156 · max 0.89 | INTAKE §3: top-port bore r 2.9..4.9, z 42.6..46.7, open boundary loop; partly occluded |
| I1_top_bore_interior | interior | cad_to_scan | reported | reported | n 3034 · p95 2.2894 · max 2.8985 | n 1239 · p95 1.9599 · max 2.6505 | INTAKE §3: top-port bore r 2.9..4.9, z 42.6..46.7, open boundary loop; partly occluded |
| I2_column_windows_below_switch | interior | scan_to_cad | reported | reported | n 808 · p95 0.7223 · max 1.0694 | n 808 · p95 0.7223 · max 1.0694 | INTAKE §3: column surface below the switch hidden by switch and holder; conical window 340..25 |
| I2_column_windows_below_switch | interior | cad_to_scan | reported | reported | n 1706 · p95 1.3017 · max 1.5831 | n 734 · p95 0.6972 · max 1.4006 | INTAKE §3: column surface below the switch hidden by switch and holder; conical window 340..25 |
| Z1_spindle | whole | scan_to_cad | FAIL | FAIL | n 16768 · p95 0.2838 · max 1.3378 | n 16768 · p95 0.2838 · max 1.3378 | INTAKE §4 Z1 splined spindle, D-flat, key (E01, z -14.85..0) |
| Z1_spindle_c2s | region | cad_to_scan | reported | reported | n 12347 · p95 0.2887 · max 0.7853 | n 12171 · p95 0.2817 · max 0.605 | report only |
| Z2_cap_cam_ring | whole | scan_to_cad | FAIL | FAIL | n 46719 · p95 0.6148 · max 1.5933 | n 46719 · p95 0.6148 · max 1.5933 | INTAKE §4 Z2 cap disc + cam ring posts/teeth (E02, E03, z 0..8.2) |
| Z2_cap_cam_ring_c2s | region | cad_to_scan | reported | reported | n 57601 · p95 0.6188 · max 1.651 | n 52376 · p95 0.5471 · max 1.2184 | report only |
| Z3_top_clip_port | whole | scan_to_cad | FAIL | FAIL | n 17649 · p95 0.4248 · max 0.89 | n 17649 · p95 0.4248 · max 0.89 | INTAKE §4 Z3 top clip port block, rim, bore, slots (E08, z 43.4..48.6) |
| Z3_top_clip_port_c2s | region | cad_to_scan | reported | reported | n 18680 · p95 0.7611 · max 2.097 | n 17265 · p95 0.6661 · max 2.097 | report only |
| Z4_side_ports | whole | scan_to_cad | FAIL | FAIL | n 42323 · p95 0.2716 · max 0.9564 | n 42323 · p95 0.2716 · max 0.9564 | INTAKE §4 Z4 side hose ports along -X beyond the column/collar radius (E09, E10) |
| Z4_side_ports_c2s | region | cad_to_scan | reported | reported | n 58236 · p95 0.4469 · max 1.7523 | n 55242 · p95 0.3225 · max 1.7312 | report only |
| Z5_barb | whole | scan_to_cad | PASS | PASS | n 7270 · p95 0.1521 · max 0.7638 | n 7270 · p95 0.1521 · max 0.7638 | INTAKE §4 Z5 hose barb along -Y (E11, axis z 30.76), beyond the column/neck radius |
| Z5_barb_c2s | region | cad_to_scan | reported | reported | n 11005 · p95 1.3219 · max 1.631 | n 10369 · p95 1.322 · max 1.631 | report only |
| Z6_microswitch | whole | scan_to_cad | FAIL | FAIL | n 25290 · p95 0.4741 · max 0.8835 | n 25290 · p95 0.4741 · max 0.8835 | INTAKE §4 Z6 microswitch box, blades, tab (E12, x 9.7..18); purchased part |
| Z6_microswitch_c2s | region | cad_to_scan | reported | reported | n 18494 · p95 0.4022 · max 0.9121 | n 18424 · p95 0.4028 · max 0.9121 | report only |

### Masks (masked and unmasked are both shown above)

| mask | direction | why | fraction removed | stats inside |
|---|---|---|---|---|
| M1 open boundary | cad_to_scan | a CAD point whose nearest scan point lies within 0.8 mm of a scan hole edge measures the distance to the edge of a coverage gap (22 open loops: port-web orifices, bore interiors, column windows, cap slots), not a surface deviation | 0.0697 | n: 20910; rms: 0.8171; mean: 0.6007; p50: 0.4443; p95: 1.7569; p99: 2.5176; max: 3.4655 |

### Mask sensitivity

| band | direction | stats | variant |
|---|---|---|---|
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.6336; max_over_by: 2.6655 | cad_to_scan | n: 300000; rms: 0.4048; mean: 0.2067; p50: 0.08; p95: 0.9336; p99: 1.7625; max: 3.4655 | all masks except M1 open boundary |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.5838; max_over_by: 2.6651 | cad_to_scan | n: 297881; rms: 0.3858; mean: 0.1987; p50: 0.0791; p95: 0.8838; p99: 1.616; max: 3.4651 | M1 open boundary radius 0.0 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.5421; max_over_by: 2.6651 | cad_to_scan | n: 292504; rms: 0.371; mean: 0.1898; p50: 0.0771; p95: 0.8421; p99: 1.568; max: 3.4651 | M1 open boundary radius 0.2 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.5085; max_over_by: 2.6651 | cad_to_scan | n: 287457; rms: 0.3622; mean: 0.1833; p50: 0.0755; p95: 0.8085; p99: 1.5589; max: 3.4651 | M1 open boundary radius 0.4 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.4774; max_over_by: 2.6651 | cad_to_scan | n: 279090; rms: 0.3551; mean: 0.1772; p50: 0.0734; p95: 0.7774; p99: 1.5571; max: 3.4651 | M1 open boundary radius 0.8 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.4867; max_over_by: 2.6651 | cad_to_scan | n: 264949; rms: 0.3561; mean: 0.1755; p50: 0.0718; p95: 0.7867; p99: 1.5695; max: 3.4651 | M1 open boundary radius 1.5 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.4951; max_over_by: 2.6651 | cad_to_scan | n: 226277; rms: 0.3624; mean: 0.1748; p50: 0.0701; p95: 0.7951; p99: 1.6306; max: 3.4651 | M1 open boundary radius 2.5 mm |

### Over-band point clusters, scan → CAD (> 0.8 mm)

2638 points (0.0105 fraction) in 26 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 790 | [-1.847, 6.56, 29.085] | [5.297, 8.329] | [98.1, 121] | 1.9395 | NEW IN IT2, REAL GEOMETRY ERROR (CAD excess, fixable). Upper side port junction box by the neck: 790 scan points all INSIDE the CAD (mean scan normal -X/-Y), x -3.2..-1.0, y 4.7..7.7, z 27.3..32.3, up to 1.94 mm. The it2 junction box (x -4..-0.12, MODELING_PLAN F10) fills the space between the port underside and the neck where the scan shows a sloped -X-facing wall running from the port (y ~7.7) down to the neck (r ~5.3). Overlays Z=29, Z=30.8 (CAD rectangle vs scan diagonal), y=6.0, x=-2.0. The it1 end-wall cluster at x ~-0.1 is gone, but this box over-fills. Largest single cluster; the scan->CAD max comes from here. |
| 1 | 381 | [-7.999, 5.547, 7.838] | [8.564, 12.011] | [135.9, 149.2] | 1.5933 | DECLARED SIMPLIFICATION, still over band. Shoulder block on post 120, sloped top: 381 pts INSIDE the CAD (was 657 in it1), theta 136..149, r 8.6..12.0, z 4.2..11.6, up to 1.59 mm, scan normal outward/up. The it2 planar slope (params simplifications 'shoulder block upper shell') does not follow the scanned surface near its lower/outer edge; overlays radial 135, x=-7, y=6.0. |
| 2 | 196 | [-1.087, 9.857, 6.592] | [9.446, 10.822] | [93.2, 99.5] | 1.542 | DECLARED SIMPLIFICATION ('cam x~0 step walls ... not modelled'), same as it1 cluster 6: +X-facing step wall at x -1.6..-0.6, theta 93..100, z 5.9..7.4, 196 pts INSIDE the CAD, up to 1.54 mm. Overlays radial 96, Z=6.5. |
| 3 | 134 | [-0.412, -10.311, 6.459] | [9.62, 11.171] | [266, 269] | 1.207 | DECLARED SIMPLIFICATION, same as it1 cluster 7: cam x~0 step wall at theta 266..269, z 4.7..7.5, 134 pts INSIDE the CAD, up to 1.21 mm. Overlay radial 270. |
| 4 | 120 | [1.097, 8.92, 21.342] | [8.165, 10.744] | [74.6, 87.3] | 1.3561 | CAD EXCESS at the switch-holder / +Y bracket junction, unchanged from it1 cluster 11 (120 pts INSIDE the CAD, x 0.4..2.5, y 8.2..10.7, z 18.4..22.5, up to 1.36 mm); the it2 holder opening did not reach this face. c2s cluster 7 (x 2.3..3.9, y 7.7..8.3, up to 2.49 mm) is the same CAD material with no scan behind it. Overlays Z=18, Z=23, radial 80. |
| 5 | 91 | [8.852, 4.075, 6.788] | [9.375, 10.46] | [14.3, 28.6] | 1.2748 | CAM RING FLANK (declared 'cam ring flanks and edges ... 0.3..1.0 mm'): post/tooth flank at theta 14..29, r 9.4..10.5, z 5.9..7.4, 91 pts INSIDE the CAD, up to 1.27 mm (CAD flank placed ~1 mm into the scanned pocket). Overlays radial 20, Z=6.5. |
| 6 | 82 | [-0.779, 10.384, 3.269] | [9.96, 10.883] | [92.7, 95.8] | 1.3156 | DECLARED SIMPLIFICATION, cam x~0 step wall family (theta 93..96, z 2.7..4.0, 82 pts INSIDE the CAD, up to 1.32 mm), lower level of cluster 2. |
| 7 | 64 | [-10.12, 16.353, 32.313] | [18.207, 20.158] | [120.3, 123.4] | 0.9114 | DECLARED SIMPLIFICATION ('port plate inner-edge lips and hooks'): upper port clip plate edge at x -10.8..-9.3, y 15.6..17.1, z 31.6..33.0, 64 pts OUTSIDE the CAD, up to 0.91 mm (lip not modelled). Overlay y=12.9 / Z=30.8. |
| 8 | 63 | [8.223, -4.054, 17.783] | [8.731, 9.856] | [331.7, 335.4] | 1.0411 | HOLDER FACE (fixable, small): scan face y ~-4.05 (normal -Y) at x 7.7..8.9, z 17.1..19.3 lies INSIDE the CAD: the CAD holder/fin -Y face stands ~0.9 mm proud of the scan here, 63 pts, up to 1.04 mm. Overlay Z=18. |
| 9 | 61 | [-1.662, -11.813, 22.984] | [11.297, 12.756] | [257.9, 265.3] | 1.2531 | LOWER PORT JUNCTION (fixable, same family as cluster 0): x -2.7..-0.9, y -12.5..-11.3, z 22.2..23.4, 61 pts INSIDE the CAD, up to 1.25 mm - top edge of the it2 lower junction box; c2s clusters 0/8 are the matching CAD-with-no-scan. Overlay Z=23. |
| 10 | 61 | [-0.8, -0.161, -13.681] | [0.421, 1.121] | [126, 233.3] | 1.3378 | DECLARED NOT MODELLED: spindle tip hole (r 0.4..1.1, z -13.9..-13.4), 61 pts INSIDE the CAD (CAD solid where the scan has a hole), up to 1.34 mm. INTAKE E01 'tip hole ... not modelled'; photos 2/4 show it. Would need a ~r0.9 hole of known depth (depth partly unscanned). |
| 11 | 52 | [-2.802, 9.312, 11.205] | [9.493, 10.082] | [104.6, 108.3] | 1.2997 | COLLAR / SHOULDER-BLOCK EDGE (fixable, small): theta 105..108, r 9.5..10.1, z 10.9..11.6, 52 pts INSIDE the CAD, up to 1.30 mm - the collar sector edge next to the post-120 block stands proud of the scan (CAD excess). Overlays radial 110, Z=11.5. |

### Over-band point clusters, CAD → scan (> 0.8 mm)

19174 points (0.0639 fraction) in 38 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 4284 | [-4.675, -8.618, 16.858] | [8.599, 14.952] | [215.1, 270] | 3.4655 | **UNEXPLAINED** |
| 1 | 3289 | [-0.093, -13.387, 30.859] | [8, 20.993] | [259.3, 279.4] | 2.6521 | **UNEXPLAINED** |
| 2 | 3012 | [-6.685, 7.5, 34.565] | [4.02, 20.652] | [102.1, 156.6] | 1.9431 | **UNEXPLAINED** |
| 3 | 1583 | [2.516, -0.033, 43.696] | [0.112, 6.494] | [0, 360] | 2.8985 | **UNEXPLAINED** |
| 4 | 718 | [-1.265, 12.693, 35.119] | [10.776, 14.064] | [90.5, 106.3] | 2.9197 | **UNEXPLAINED** |
| 5 | 478 | [-5.993, -16.743, 13.781] | [15.878, 20.005] | [243.7, 254.2] | 2.8896 | **UNEXPLAINED** |
| 6 | 462 | [-6.073, -16.853, 22.554] | [15.938, 19.793] | [244.5, 254.3] | 2.957 | **UNEXPLAINED** |
| 7 | 452 | [3.317, 8.09, 18.629] | [8.599, 9.153] | [63.3, 74.8] | 2.4941 | **UNEXPLAINED** |
| 8 | 403 | [-0.831, -12.878, 22.979] | [11.714, 13.512] | [259.8, 269.5] | 2.093 | **UNEXPLAINED** |
| 9 | 380 | [9.328, -0.779, 23.446] | [8.599, 10.672] | [0, 360] | 1.3581 | **UNEXPLAINED** |
| 10 | 379 | [-6.081, 15.856, 25.73] | [15.173, 18.736] | [106.8, 116.9] | 2.8152 | **UNEXPLAINED** |
| 11 | 361 | [-13.203, -17.505, 18.175] | [20.838, 22.602] | [227, 235.9] | 1.7523 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 0.2562°, origin offset 0.1656 mm, point disagreement p95 0.1881 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (OUTSIDE).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| whole part scan->CAD (gated) | p95 and max over band (numbers in the gate table; it1 vs it2 in the generated table at the end). 10.8 % of scan points are over 0.30 mm (p95 <= 0.30 needs <= 5 %) and 1.05 % over 0.80 mm in 26 clusters >= 20 pts plus 65 points in small clusters (qa/probe/over_share_it2.json). Scan is clean (noise ~0.04 mm), full-res, datum/ICP not implicated. Over-0.30 share by z band: cam ring z 0..8.2 29 %, column/lower port z 15.4..27.7 33 %, collar band z 8.2..15.4 15 %, neck/upper port 11 %, top clip port 10 %, spindle 2 %. Two populations: (a) >0.8 mm clusters on named regions - it2 port junction boxes over-filling by the neck (cluster 0, new regression, 790 pts), shoulder-block slope (1), declared cam x~0 steps (2, 3, 6), holder/bracket junction (4), cam flanks (5, 12), declared spindle tip hole (10), cap slots, plate lips; (b) a diffuse 0.3..0.8 mm face-placement population (cam flanks and pocket floors, top-port lug outline rounded vs rectangular CAD - overlay Z=45.5, collar sectors) that is NOT concentrated at sharp edges (qa/probe/edge_share.json: excluding points within 1 mm of sharp CAD edges does not lower p95). Hypothetical upper bound (probe, not a gate): making EVERY >0.8 mm cluster neighbourhood perfect (bbox +1.5 mm, 10 % of the scan) would still leave p95 ~0.34 and max ~1.09. | (1) ACCEPT-BAND now (owner decision in DECISIONS.md citing this gate.json hash and a band_fails name), delivering it2 with this per-region list. (2) Loop 3 (last) on the fixable items: trim the it2 port junction boxes to the scanned sloped wall (cluster 0/9/13, c2s 0/4/8), refit the shoulder-block slope (1), open the holder/bracket junction (4, c2s 7), model the cam x~0 steps (2/3/6), tip hole (10), plate lips (7, c2s 5/6/10/11), cam flank placement (5/12), top-port lug outline. Realistic expectation: p95 falls toward ~0.35-0.40 and max toward ~1.1-1.3 mm; the probe bound says p95 0.30 and max 0.80 are NOT reachable by cluster fixes alone and would also need a full refit of the diffuse 0.3..0.8 mm face placement plus features the scan cannot define (spline tooth count unresolved, cap slots/dimples partly scanned). (3) Supply calipers/measurements or a different regime - an owner decision, never QA's. |
| whole part CAD->scan, observable subset (gated) | p95 and max over band. Unobservable fraction is small (~2.8 %), so this is not mainly a coverage artefact: the biggest contributors are CAD material with no scan behind it at the port junction boxes and lower/upper port plates (c2s 0, 4, 5, 6, 8, 10, 11, up to ~3.5 mm), the holder/bracket junction remnant (c2s 7) and the holder top under the switch (c2s 9); the barb/port bore interiors (c2s 1, 2) and the top-bore counterbore walls (c2s 3) are unscanned and count only where the ray test found line of sight. | same as above; trimming the junction boxes and plate inner edges to the scanned outline is the main fixable lever; bore interiors cannot be graded without more scan data. |
| Z2_cap_cam_ring (gated, whole band) | p95 and max over band, essentially unchanged from it1: shoulder-block slope (cluster 1, smaller than it1), declared cam x~0 step walls (2, 3, 6), cam flank placement (5, 12), cap slot walls (probe 16/18/21/24), declared dimples; 16.6 % of this zone is over 0.30 mm. | model the x~0 steps and per-pocket floors, refit post/tooth flanks per instance (not one 120-degree pattern), refit the block slope; or accept. |
| Z6_microswitch (gated) | p95 and max both improved strongly vs it1 (bump and bar 330 now modelled; see the it1/it2 table) but both stay over band: max is at the switch outer face y ~9.1 (probe cluster 15, 41 pts OUTSIDE the CAD, moulded marks/labels, declared) and the p95 residual is spread over the plain sharp-edged box (switch edge rounds and labels declared not modelled). | model the switch box edge rounds and raised marks, or accept (purchased part). |
| Z3_top_clip_port (gated) | p95 over band, max just over (0.89): bore floor fixed in it2, remaining miss is the lug outline (scan rounded/irregular vs CAD rectangle with 1.7 mm rounds, overlay Z=45.5) and averaged internal ribs (declared). | model the lug outline from the scan section; ribs need better scan coverage. |
| Z1_spindle (gated) | p95 passes, max over band at the declared-not-modelled tip hole (cluster 10) and spline teeth (median cylinder; tooth count unresolved, CHK-COUNT). | model the tip hole; teeth need a tooth count (photo/caliper) or stay a declared miss. |
| Z4_side_ports (gated) | p95 passes, max over band at plate lips (cluster 7, declared) and plate/junction edges. | model plate lips/hooks; trim junction boxes. |

Missed band(s): `scan_to_cad:masked: p95 0.449 max 1.940 vs 0.3/0.8`; `cad_to_scan_observable: p95 0.761 max 2.890 vs 0.3/0.8`; `zone:Z1_spindle:scan_to_cad: p95 0.284 max 1.338 vs 0.3/0.8`; `zone:Z2_cap_cam_ring:scan_to_cad: p95 0.615 max 1.593 vs 0.3/0.8`; `zone:Z3_top_clip_port:scan_to_cad: p95 0.425 max 0.890 vs 0.3/0.8`; `zone:Z4_side_ports:scan_to_cad: p95 0.272 max 0.956 vs 0.3/0.8`; `zone:Z6_microswitch:scan_to_cad: p95 0.474 max 0.883 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | no Tier-1 (no calipers, DECISIONS.md MEASUREMENTS scan-only); nothing to attribute |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | pass | grading gate = QA's own ICP on the raw full-res scan against the frozen it2 STEP; T_refine is QA-only and not written back to intake/alignment.json; no expected value taken from params.json. Builder self-check numbers in MODELING_PLAN §8 are a consistency check, not independent evidence, and were not used. |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 12 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | finding | it1 findings closed: switch underside bump (E16), column lug at 320 (E17), bar at 330 (E18), barb top rib all now in the CAD; their it1 clusters are gone (qa/probe/over_share_it2.json regions R4/R5/R6 now max <= 0.68). No new unenumerated scan feature found: every one of the 26 scan->CAD clusters >= 20 pts (qa/probe/cluster_probe.json) sits on an enumerated feature. Remaining finding: CAD material with no scan behind it at the it2 port junction boxes (s2c cluster 0: 790 scan pts INSIDE the CAD by up to 1.94 mm at x -3.2..-1.0, y 4.7..7.7, z 27.3..32.3; c2s clusters 0/4/8) - the it2 junction box between the upper port and the neck fills a region where the scan shows a -X-facing sloped wall (overlays Z=29, Z=30.8, y=6.0, x=-2.0). Declared-not-modelled features stay over band: spline teeth, spindle tip hole (cluster 10), cap dimples, cam x~0 step walls (clusters 2, 3, 6), switch labels, plate lips. |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | pass | build/export_check.json + fillets.json: 3/3 OK (col_top_fillet 1.5, spindle_tip_chamfer 0.7, top_blk_edge_r 1.7 x4 edges), target == used, 0 FAILED/REDUCED/NO_EDGES/SELECTOR_ERROR. No other edge rounds are modelled (declared sharp edges); qa/probe/edge_share.json shows the 0.3..0.8 mm population is not an edge-only effect. |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | fresh agent, own scripts; see independence |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | pass | it1 vs it2 use the same protocol: same regime file content, same scan (sha256 98cd1183...), identical alignment matrix (max abs diff 0.0; the alignment.json hash differs only by its re-written header), same datum_spec/zones/masks (copied verbatim), same ICP parameters (3M/seed 11, 300k/seed 13, 70 deg, 0.8 mm, 3.0 mm, cap 60, tol 1e-6), same deviation sampling (all scan verts, 300k CAD samples seed 2, k 8, n_samp 3M, seed 0; observability 20k seed 5, 0.5 mm, 60 deg), same tessellation tolerance. Only the CAD changed, so it1->it2 deltas are geometry changes, not protocol. Overlays add panels (Z=29, theta 20/110, x=-2.0, y=6.0) for new clusters; the it1 panels are all kept. Side-by-side table: qa/probe/like4like_it1_it2.json and the generated section at the end of VERDICT.md. |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | pass | no pass depends on a mask |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | pass | QA census (qa/step_check.json): 351 faces, 100 % analytic area (plane 254, cylinder 76, cone 20, torus 1), 0 B-spline/ruled faces; plane median area ~5.9 mm2 (face_stats.json, reported not gated). grep of build/model.py for loft\|ruled\|Polyline: 0 hits. No faceted skin. |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | finding | photos 1..5 (catalogue, low-res, no scale) walked by this QA agent: splined spindle with tip hole (1,2,4), cap disc with slots and dimples (2,4), cam ring/teeth (2,3,4,5), two side ports with clip plates (1,3,5), barb (3,5), top clip port (1,3,5), microswitch with blades and bracket (1,2,4) are all present in the CAD; nothing in the CAD is absent from photos+scan except the interior material inside the column and the port junction boxes (buried/assumed, MODELING_PLAN §6). Photographed but not modelled (declared): spline teeth, spindle tip hole, cap dimples. |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict BAND_NOT_MET |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 6 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L0 | Band NOT met under the declared regime (baseline-skill plastic): scan->CAD p95 0.4495 / max 1.9395 mm and observable CAD->scan p95 0.7609 mm; only the barb zone passes. The misses sit in the cam ring, the top clip port, the microswitch, the spindle spline and the port junction by the neck (an it2 regression there sets the whole-part max). Accepted for delivery by the owner (ACCEPT-BAND, decisions/accept_band.md). | calipers supplied, or a request to spend the third loop on the named regions | qa/VERDICT.md; qa/gate.json#band_fails |
| L1 | no Tier-1 (no calipers run): scan-only by owner decision. Every row of intake/MEASUREMENTS.md is ABSENT, not passed. | any caliper reading supplied | DECISIONS.md MEASUREMENTS; qa/gate.json#limitations |
| L2 | Absolute scale not caliper-verified (CHK-SCALE FLAG). A QA uniform-scale probe on the same scan read a fraction of a percent, so scale does not explain the miss. | one caliper reading of any overall dimension | intake/alignment.json#checks; qa/gate.json#limitations |
| L3 | Datum audit is outside the RE_SPEC reference band (report-only, never blocking); the QA ICP correction is small and the datum-frame and post-ICP deviations agree, so the datum is not the cause of the miss. | a new intake alignment with a changed spec | qa/gate.json#datum_audit |
| L4 | The QA overlays are drawn in the builder's alignment frame (overlay.py has no registration option); the gate itself is post-ICP. | overlay.py gains a registration option | qa/overlays/ |
| L5 | deviation_gate.py keeps only the top twelve scan->CAD clusters in gate.json; the smaller remaining clusters are characterised in the QA probe files, not individually in gate.json. | fix of the cluster cap in deviation_gate.py, then re-run QA | qa/probe/cluster_probe.json |
| L6 | Spindle spline teeth are not modelled: the tooth count is not resolved by the scan (CHK-COUNT finding), so the spindle is its median cylinder with the measured D-flat and key. It will not mate with a splined knob as modelled. | a tooth count or the mating knob | measure/params.json#checks; measure/figures/spline_pitch.json |
| L7 | The scan is an assembly (cap, body, microswitch with blades) and is delivered as ONE fused solid; the interior (valve bore, spool, passages) was not scanned and is solid in the model. | a request for a multi-body STEP or interior geometry (a separate job) | intake/INTAKE_CARD.md#8; build/MODELING_PLAN.md#6 |
| L8 | Declared simplifications with their measured costs (cap dimples and slots, cam flank edges and pocket floors, microswitch labels, blade holes, plate lips, top-port ribs, small rounds) are listed in measure/params.json#simplifications and PARAM_TABLE.md. | a higher-fidelity request for any listed region | measure/params.json#simplifications |

## 12. Assumptions and invented geometry

- The column interior (valve bore, spool, flow passages) was not scanned and is modelled solid below the top-port bore; nothing was invented there. _(source: assumed; build/MODELING_PLAN.md#6)_
- Sub-body connectors (port tubes and plates run into the column, barb root inside the neck, holder buried in the column) sit inside the column and are not visible. _(source: assumed; build/MODELING_PLAN.md#6)_
- The assembly (cap, body, microswitch and blades) is one fused solid as scanned; it is not a multi-body STEP. _(source: assumed; intake/INTAKE_CARD.md#8)_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** manufacture, tooling or a mould release: no caliper verified any dimension and the absolute scale is unverified
- **Not fit for:** the knob or spindle fit: the spline is modelled as its median cylinder and the tooth count is not resolved
- **Not fit for:** anything that needs the interior (spool bore, passages): it was not scanned
- Fit for: packaging, envelope and clearance studies at the scan's accuracy
- Fit for: positioning of the ports, barb, top clip port and microswitch in an assembly model
- Fit for: a starting model for a calipered re-run
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): Not an approved model. This QA result grades iteration 2 against the owner's baseline-skill plastic band (p95 <= 0.30 / max <= 0.80 mm) on the scan only: the band is missed in both gated directions and in 5 of 6 zones. It is not evidence of any dimension (no calipers, scale unverified), says nothing about the unscanned interior (bores, spool, passages are not modelled and not graded), and is not fit for tooling, manufacture or mating-part design. Delivery needs a recorded ACCEPT-BAND. Zone Z5 (barb) passing is a local result and does not excuse the whole part.

## 14. Human acceptance of the band miss

Accepted by **Ikbal (owner, question card)** on 2026-09-28 (`DECISIONS.md`, ACCEPT-BAND): Accept and deliver: accepts scan_to_cad:masked, cad_to_scan_observable and zones Z1/Z2/Z3/Z4/Z6 band fails, gate 19f6d742b0ae (created 2026-09-28T08:12:03+00:00); scan->CAD p95 0.449 max 1.94, observable CAD->scan p95 0.761 max 2.89; loop 3 judged unable to reach the band (QA probe). Record: `decisions/accept_band.md` (sha256 `ad905f36fe979b5253484d1633df1007b3d6016e29f215b9b4ffee8d71e01907`).

## 15. Reproduction

```
cd build && python model.py
python <skills>/stl-re-deliver/scripts/repro_check.py --run <run>
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-S01_steam-valve.step | 15837.5497 | 0 | 0 | yes | yes | no |
| OD-S01_steam-valve_datum.step | 15837.5497 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 16. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | 19f6d742b0ae76dcaa8a74d7457777b6eb4dd4f8935dae3fda2d75cf83175211 |
| `measure/params.json` | 19aee3e5fbabcedada3f072e2c223e5e05f7833d02830d4b4b86a4f36448d60a |
| `build/export_check.json` | 374a7006ebed0dfe6b3e8d0eeadf72c406dd48791246adb604b40eee6f928d92 |
| `intake/alignment.json` | fff8c3ae96c69e11fd6baafe2cd4edfd5d47d7a4e7a10e6910d54391fd68abf4 |
| `deliver/repro.json` | 75ef5fade80ee62519fb2473ad60cb608dbe603a85d1a36ffeedb5c48d210042 |
| `deliver/limitations.json` | fa97abe0bdb1c39150232b22781d74e559a9c4a5ed7768d6b97ae8ea80e75f18 |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
