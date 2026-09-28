# OD-S02_steam-rod — STL → STEP reverse-engineering delivery

**Verdict: `BAND_NOT_MET`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 3 of 3 (earlier iterations kept: `_it1_SUPERSEDED/`, `_it2_SUPERSEDED/`).  
**Verification independence (CHK-INDEP):** pass — fresh agent; see independence  

> **A deviation band was NOT met.** Delivered only under the recorded human acceptance below (by Ikbal (owner, question card), 2026-09-28, record `decisions/accept_band.md`).

## 1. The part

![reference photo](../input/photos/photo_1.webp)

Coffee-machine steam wand assembly (black connector rod with O-ring seats, knob with lever paddle, sleeve and sealing band, bent steel tube, white bushing, steel tip), scanned as one mesh and delivered as ONE fused solid (owner decision).

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-S02_steam-rod_datum.step` | datum | 1 | yes | yes | 122 | 13753.4894 | max: [50.149, 9.1532, 67.257]; min: [-21.486, -16.0674, -57.9338]; size: [71.635, 25.2206, 125.1908] |
| `build/OD-S02_steam-rod.step` | scan | 1 | yes | yes | 122 | 13753.4894 | max: [68.9868, 12.6413, -150.2085]; min: [-38.4698, -55.3636, -222.4944]; size: [107.4566, 68.0048, 72.286] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Datum: rod spigot axis is +Z (axis primary, section-circle refined cone fit), origin on the knob top face, the steel tube leaving the elbow clocks +X.
2. Scan-only parameters (no calipers): per-axis section-circle fits for rod, sleeve, tubes, tip and bushing; ellipse sections for the knob fairing; planes and sphere caps for the lever; the bushing spoke count by rotational-order FFT.
3. build123d sub-bodies on their measured axes, fused: revolves, one fitted non-ruled loft (knob fairing), one sweep for the bent tube, sphere-cap dishes, window pockets; both frames exported and re-imported.
4. Independent verification in a fresh agent with its own ICP, two-way deviation on the full-resolution scan, regime baseline-skill.

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | rod axis ∩ knob top face (annulus around the rod, facing the rod tip) | — | — |
| primary (axis) | rod taper spigot (black connector, z 44..75 above the knob) | 0.0255 / 0.2385 | the rod is the machine interface: tapered spigot + O-ring seats that plug into the steam outlet; every turned feature of the rod and the knob dome is coaxial with it |
| secondary (axis) | rod taper + rod collar cylinder | 0.0214 / 0.4394 | coaxial check along the spigot / second coaxial feature for CHK-TILT |
| clock | axis_direction: steel tube leaving the elbow (Ø6 segment between the sleeve O-ring and the bend) -> +X (angle -3.0635°) | — | — |

Measured tilt: 0.053° (common slope, per-feature intercept, 40 stations over 2 feature(s), z 16.500..63.000 vs frame Z; NOT RESOLVABLE (heuristic): 'rod collar cylinder' (0.71 deg @ -54.3 deg) vs 'rod taper' (0.05 deg @ 32.0 deg) differ by 0.71 deg > combined stderr 0.06 deg). Scale factor applied: 1. Scan noise floor: 0.0187 mm (rms of RANSAC+SVD plane on knob top face (annulus around rod) (6283 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
 0.116682   0.017706  -0.993011  -170.035387
 0.553403   0.829081   0.079810   19.629710
 0.824700  -0.558848   0.086940  -3.476981
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: assumed 2, scan 86 (total 88). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `band_fall_r` | [4.75, 4.07] | mm | [4.75, 4.07] | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `band_r` | 5.0103 | mm | 4.9822..5.0340 | keep-measured | scan | 0.05 | no | measure/figures/measurements.json |
| `band_t` | [20.55, 22.4, 23, 23.5, 23.8] | mm | [20.55, 22.4, 23, 23.5, 23.8] | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `bend_R` | 11.6 | mm | 10.4..12.8 | keep-measured | scan | 0.2 | no | measure/figures/measurements.json |
| `bend_cl_x` | [30.6426, 32.5718, 34.4441, 36.1953, 37.7426, 38.9722, 39.8889, 40.4484, 40.6266, 40.607] | mm | [30.6426, 32.5718, 34.4441, 36.1953, 37.7426, 38.9722, 39.8889, 40.4484, 40.6266, 40.607] | keep-measured | scan | 0.05 | no | measure/figures/measure_it3.json |
| `bend_cl_y` | [0.3197, 0.2385, 0.1028, -0.1106, -0.3969, -0.8098, -1.26, -1.7904, -2.3346, -2.8584] | mm | [0.3197, 0.2385, 0.1028, -0.1106, -0.3969, -0.8098, -1.26, -1.7904, -2.3346, -2.8584] | keep-measured | scan | 0.05 | no | measure/figures/measure_it3.json |
| `bend_cl_z` | [-13.9784, -14.5046, -15.2105, -16.1723, -17.4354, -18.9924, -20.7305, -22.5971, -24.5336, -26.4687] | mm | [-13.9784, -14.5046, -15.2105, -16.1723, -17.4354, -18.9924, -20.7305, -22.5971, -24.5336, -26.4687] | keep-measured | scan | 0.05 | no | measure/figures/measure_it3.json |
| `bend_tube_r` | 2.9098 | mm | 2.8832..2.9686 | keep-measured | scan | 0.03 | no | measure/figures/measure_it3.json |
| `bend_vertex` | [41.2526, 0.2992, -15.4061] | mm | [41.2526, 0.2992, -15.4061] | keep-measured | scan | 0.1 | no | measure/figures/measurements.json |
| `bush_barrel_r` | [5.9995, 6.6433, 7.3617, 7.8632, 8.2545, 8.4943, 8.6415, 8.7867, 8.6025, 8.3711, 8.1777] | mm | [5.9995, 6.6433, 7.3617, 7.8632, 8.2545, 8.4943, 8.6415, 8.7867, 8.6025, 8.3711, 8.1777] | keep-measured | scan | 0.1 | no | measure/figures/measurements.json |
| `bush_barrel_t` | [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 4.5] | mm | [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 4.5] | keep-measured | scan | 0 | no | measure/figures/measurements.json |
| `bush_bottom` | [8.2, 4.907] | mm | [8.2, 4.907] | keep-measured | scan | 0.1 | no | measure/figures/measurements.json |
| `bush_c_t` | 25.0019 | mm | 25.0019 | keep-measured | scan | 0.1 | no | measure/figures/measurements.json |
| `bush_dir_down` | [-0.1376, -0.2904, -0.9469] | mm | [-0.1376, -0.2904, -0.9469] | keep-measured | scan | 0.01 | no | measure/figures/measurements.json |
| `bush_flange_r` | 5.8828 | mm | 5.8255..5.9035 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `bush_frame_x` | [0, -0.956, 0.2932] | mm | [0, -0.956, 0.2932] | keep-measured | scan | 0 | no | measure/figures/measurements.json |
| `bush_point` | [38.9661, -6.6886, -39.3299] | mm | [38.9661, -6.6886, -39.3299] | keep-measured | scan | 0.15 | no | measure/figures/measurements.json |
| `bush_spoke_count` | 6 | count | 6 | keep-measured | scan | 0 | no | measure/figures/count_bushing_spokes.json |
| `bush_spoke_phase` | 49.433 | deg | 49.433 | keep-measured | scan | 1 | no | measure/figures/count_bushing_spokes.json |
| `bush_spoke_w` | 0.8022 | mm | 0.8022 | keep-measured | scan | 0.3 | no | measure/figures/measurements.json |
| `bush_top_cone` | [3.5, -7.084] | mm | [3.5, -7.084] | keep-measured | scan | 0.15 | no | measure/figures/measurements.json |
| `bush_top_t` | -7.5925 | mm | -7.639..-7.546 | keep-measured | scan | 0.15 | no | measure/figures/measurements.json |
| `bush_window_depth` | 2.52 | mm | 2.524 | keep-measured | scan | 0.2 | no | measure/figures/revise_it2_probe.json |
| `bush_window_r` | [4.5, 7] | mm | [4.5, 7] | keep-measured | scan | 0.25 | no | measure/figures/measurements.json |
| `dish_c` | [-11.5695, -16.6736] | mm | [-11.5695, -16.6736] | keep-measured | scan | 0.0449 | no | measure/figures/measurements.json |
| `dish_depth` | 0.9019 | mm | 0.9019 | keep-measured | scan | 0.0449 | no | measure/figures/measurements.json |
| `dish_sphere_r` | 17.972 | mm | 17.972 | keep-measured | scan | 0.5 | no | measure/figures/measurements.json |
| `fair_ay` | [9.0206, 8.8848, 8.5334, 7.8436, 7.1032, 6.7628] | mm | [9.0206, 8.8848, 8.5334, 7.8436, 7.1032, 6.7628] | keep-measured | scan | 0.1371 | no | measure/figures/measurements.json |
| `fair_az` | [9.7773, 9.9643, 10.0739, 9.0583, 7.7486, 7.0012] | mm | [9.7773, 9.9643, 10.0739, 9.0583, 7.7486, 7.0012] | keep-measured | scan | 0.1371 | no | measure/figures/measurements.json |
| `fair_x` | [0, 1.5, 3, 4.5, 6, 7] | mm | [0, 1.5, 3, 4.5, 6, 7] | keep-measured | scan | 0 | no | measure/figures/measurements.json |
| `fair_yc` | [0.078, 0.0816, 0.1229, 0.2029, 0.34, 0.433] | mm | [0.078, 0.0816, 0.1229, 0.2029, 0.34, 0.433] | keep-measured | scan | 0.1371 | no | measure/figures/measurements.json |
| `fair_zc` | [-3.8094, -3.9499, -4.2058, -5.4863, -7.0443, -7.9801] | mm | [-3.8094, -3.9499, -4.2058, -5.4863, -7.0443, -7.9801] | keep-measured | scan | 0.1371 | no | measure/figures/measurements.json |
| `knob_bottom_z` | -14.4 | mm | — | assumed | assumed | 0.5 | no | measure/figures/measurements.json |
| `knob_meridian_r` | [9.1007, 9.0497, 9.0018, 8.967, 8.9024, 8.8064, 8.6891, 8.5434, 8.3843, 8.1819, 7.9651, 7.7062, 7.4279, 6.9863, 6.5862, 6.1405, 5.6379, 5.0289, 4.2527, 3.4354, 2.8382] | mm | [9.1007, 9.0497, 9.0018, 8.967, 8.9024, 8.8064, 8.6891, 8.5434, 8.3843, 8.1819, 7.9651, 7.7062, 7.4279, 6.9863, 6.5862, 6.1405, 5.6379, 5.0289, 4.2527, 3.4354, 2.8382] | keep-measured | scan | 0.15 | no | measure/figures/measurements.json |
| `knob_meridian_z` | [-3.5, -4, -4.5, -5, -5.5, -6, -6.5, -7, -7.5, -8, -8.5, -9, -9.5, -10, -10.5, -11, -11.5, -12, -12.5, -13, -13.5] | mm | [-3.5, -4, -4.5, -5, -5.5, -6, -6.5, -7, -7.5, -8, -8.5, -9, -9.5, -10, -10.5, -11, -11.5, -12, -12.5, -13, -13.5] | keep-measured | scan | 0 | no | measure/figures/measurements.json |
| `knob_r` | 9.1532 | mm | 8.9736..9.2920 | keep-measured | scan | 0.12 | no | measure/figures/measurements.json |
| `knob_top_z` | 0 | mm | -0.0291 | keep-measured | scan | 0.03 | no | measure/figures/measurements.json |
| `lug_corner_r` | 0.6 | mm | — | assumed | assumed | 0.3 | no | measure/figures/measurements.json |
| `lug_r_top` | 8.3406 | mm | 8.3406 | keep-measured | scan | 0.1 | no | measure/figures/measurements.json |
| `lug_theta` | -90.92 | deg | -96.25..-90.25 | keep-measured | scan | 0.2 | no | measure/figures/measurements.json |
| `lug_width` | 3.3983 | mm | 3.3983 | keep-measured | scan | 0.1 | no | measure/figures/measurements.json |
| `lug_z` | [3.2059, 5.6543] | mm | [3.2059, 5.6543] | keep-measured | scan | 0.1 | no | measure/figures/measurements.json |
| `paddle_edge_fillet_r` | 1.946 | mm | [1.8704, 2.0216] | mean-of-n | scan | 0.1 | no | measure/figures/measure_it3.json |
| `paddle_end_c` | [-11.4525, -16.8839] | mm | [-11.4525, -16.8839] | keep-measured | scan | 0.0917 | no | measure/figures/measurements.json |
| `paddle_end_r` | 10.0335 | mm | 10.0335 | keep-measured | scan | 0.0917 | no | measure/figures/measurements.json |
| `paddle_face_neg` | [0.0395, 0.01, -2.4007] | mm | [0.0395, 0.01, -2.4007] | keep-measured | scan | 0.0636 | no | measure/figures/measurements.json |
| `paddle_face_pos` | [0.0368, 0.0197, 2.8676] | mm | [0.0368, 0.0197, 2.8676] | keep-measured | scan | 0.0656 | no | measure/figures/measurements.json |
| `paddle_lower_end` | [8.8916, -15.2594] | mm | [8.8916, -15.2594] | keep-measured | scan | 0.2 | no | measure/figures/measurements.json |
| `paddle_upper_line` | [0.6897, 3.1217] | mm | [0.6897, 3.1217] | keep-measured | scan | 0.0695 | no | measure/figures/measurements.json |
| `rod_bead_r` | [6.4667, 6.4006, 6.4832, 6.6433, 6.566, 6.5647, 6.3465, 6.2241, 6.1213, 6.1339, 6.2013, 6.322, 6.4647] | mm | [6.4667, 6.4006, 6.4832, 6.6433, 6.566, 6.5647, 6.3465, 6.2241, 6.1213, 6.1339, 6.2013, 6.322, 6.4647] | keep-measured | scan | 0.05 | no | measure/figures/measurements.json |
| `rod_bead_z` | [9.75, 10, 10.25, 10.5, 10.75, 11, 11.25, 11.5, 11.75, 12, 12.25, 12.5, 12.75] | mm | [9.75, 10, 10.25, 10.5, 10.75, 11, 11.25, 11.5, 11.75, 12, 12.25, 12.5, 12.75] | keep-measured | scan | 0 | no | measure/figures/measurements.json |
| `rod_body_r` | 6.4782 | mm | 6.4551..6.5709 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_collar_r` | 6.4454 | mm | 6.4044..6.4879 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_collar_z1` | 6.8 | mm | 6.75..6.85 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_cone1_r0` | 5.7564 | mm | [5.7564, 5.7564] | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_cone1_r1` | 4.8112 | mm | [4.8112, 4.8112] | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_cone1_z` | [21.75, 25.75] | mm | [21.75, 25.75] | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_flare_r` | 6.8726 | mm | 6.8628..6.8823 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_flare_z0` | 17.5 | mm | 17.25..17.75 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_groove_r` | 5.1269 | mm | 5.1131..5.1920 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_groove_z2` | 9.15 | mm | 9.1..9.2 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_oring_center` | [4.67, 27.3] | mm | [4.67, 27.3] | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_oring_cord_r` | 1.1 | mm | 1.05..1.12 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_step_z` | 21.1 | mm | 21.0..21.2 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_taper_drdz` | -0.0437 | mm | -0.0437 | keep-measured | scan | 0.001 | no | measure/figures/measurements.json |
| `rod_taper_r_z30` | 4.6065 | mm | 4.6065 | keep-measured | scan | 0.0082 | yes | measure/figures/measurements.json |
| `rod_tip_round_r` | 2 | mm | 1.9..2.1 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `rod_tip_z` | 67.257 | mm | 67.257 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `sleeve_dir` | [0.9848, 0.0046, -0.1738] | mm | [0.9848, 0.0046, -0.1738] | keep-measured | scan | 0.003 | no | measure/figures/measurements.json |
| `sleeve_drdt` | -0.0348 | mm | -0.0348 | keep-measured | scan | 0.003 | no | measure/figures/measurements.json |
| `sleeve_end_t` | 20.55 | mm | 20.5..20.6 | keep-measured | scan | 0.0187 | no | measure/figures/measurements.json |
| `sleeve_point` | [14.8842, 0.2448, -11.1813] | mm | [14.8842, 0.2448, -11.1813] | keep-measured | scan | 0.0921 | no | measure/figures/measurements.json |
| `sleeve_r_at_point` | 3.8795 | mm | 3.8795 | keep-measured | scan | 0.0921 | no | measure/figures/measurements.json |
| `tip_bore_depth` | 13.6 | mm | 13.600 | keep-measured | scan | 0.3 | no | measure/figures/revise_it2_probe.json |
| `tip_bore_r` | 2.032 | mm | 2.032 | keep-measured | scan | 0.05 | no | measure/figures/measurements.json |
| `tip_chamfer` | [1.1, 0.5] | mm | [1.1, 0.5] | keep-measured | scan | 0.05 | no | measure/figures/measurements.json |
| `tip_dir_down` | [-0.1376, -0.2904, -0.9469] | mm | [-0.1376, -0.2904, -0.9469] | keep-measured | scan | 0.01 | no | measure/figures/measurements.json |
| `tip_end_t` | 3.9 | mm | 3.869..3.95 | keep-measured | scan | 0.05 | no | measure/figures/measurements.json |
| `tip_neck_r` | [2.587, 2.4977, 2.5002, 2.5464, 2.596, 2.8048, 2.9422, 2.9779] | mm | [2.587, 2.4977, 2.5002, 2.5464, 2.596, 2.8048, 2.9422, 2.9779] | keep-measured | scan | 0.05 | no | measure/figures/measure_it3.json |
| `tip_neck_t` | [-9.6, -9.4, -9.2, -9, -8.8, -8.6, -8.4, -8.2] | mm | [-9.6, -9.4, -9.2, -9, -8.8, -8.6, -8.4, -8.2] | keep-measured | scan | 0 | no | measure/figures/measure_it3.json |
| `tip_point` | [36.9138, -11.0194, -53.4502] | mm | [36.9138, -11.0194, -53.4502] | keep-measured | scan | 0.089 | no | measure/figures/measurements.json |
| `tip_r` | 2.9598 | mm | 2.7191..2.9884 | keep-measured | scan | 0.089 | no | measure/figures/measurements.json |
| `tubeB_dir` | [0.9891, 0.0006, -0.1471] | mm | [0.9891, 0.0006, -0.1471] | keep-measured | scan | 0.002 | no | measure/figures/measurements.json |
| `tubeB_point` | [-0.0002, 0.358, -9.2949] | mm | [-0.0002, 0.358, -9.2949] | keep-measured | scan | 0.0518 | no | measure/figures/measurements.json |
| `tubeC_dir_up` | [0.0587, 0.2677, 0.9617] | mm | [0.0587, 0.2677, 0.9617] | keep-measured | scan | 0.002 | no | measure/figures/measurements.json |
| `tube_r` | 2.9967 | mm | 2.9875..3.0059 | keep-measured | scan | 0.05 | yes | measure/figures/measurements.json |
| `under_dish_R` | 19.2634 | mm | 19.2634 | keep-measured | scan | 0.5 | no | measure/figures/measurements.json |
| `under_dish_c` | [-10.289, -21.4172, -16.4812] | mm | [-10.289, -21.4172, -16.4812] | keep-measured | scan | 0.0489 | no | measure/figures/measurements.json |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

| id | feature | params |
|---|---|---|
| F01 | rod + knob revolves (knob meridian spline, rod profile with O-ring seats, spigot taper, round nose) | [knob_meridian_r, rod_taper_r_z30, rod_tip_z] |
| F02 | O-ring cord, knob fairing loft (6 ellipse sections), collar lug | [rod_oring_center, fair_ay, lug_theta] |
| F04 | lever plate between two fitted planes, perimeter round, top and underside sphere dishes | [paddle_end_r, paddle_face_pos, dish_depth, under_dish_R] |
| F07 | sleeve cone and sealing band on their own axes | [sleeve_dir, band_r] |
| F09 | steel tube: one sweep line B, bend arc, line C | [tube_r, bend_R, bend_vertex] |
| F12 | bushing on the tip axis with 6 underside windows, tip with chamfer and bore | [bush_barrel_r, bush_spoke_count, tip_r, tip_bore_r] |

## 7. Tier-1 — caliper dims re-measured on the STEP

**Tier-1 not run: no caliper dimensions exist.** Every dimension is scan authority (or operator spec); see the source column in §5. Absent is not passed.

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), iterations 44/60, converged yes, correction 0.0531° / 0.0586 mm.  
Unobservable CAD fraction: 0.0172.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 251631 | 0.3578 | 0.0663 | 0.3122 | 2.0561 | 4.5184 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 234665 | 0.1147 | 0.0627 | 0.2363 | 0.3662 | 0.7374 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 0.3651 | 0.0698 | 0.8955 | 1.6925 | 2.6173 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 240232 | 0.2254 | 0.0581 | 0.2751 | 1.0596 | 2.6023 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 19656 | 0.3466 | 0.0672 | 0.7662 | 1.6984 | 2.6012 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.2363 max 0.7374 (n 234665) | PASS |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 0.7662 max 2.6012 (n 19656) | FAIL |
| zone:Z1 rod spigot taper + O-ring seats:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.1306 max 0.565 (n 39907) | PASS |
| zone:Z1 rod spigot taper + O-ring seats:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.1329 max 0.6926 (n 48538) | PASS |
| zone:Z2 steel tube B-bend-C:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.2286 max 0.5805 (n 26716) | PASS |
| zone:Z2 steel tube B-bend-C:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.2142 max 0.3451 (n 23764) | PASS |
| zone:Z3 lever paddle:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.134 max 0.2475 (n 20978) | PASS |
| zone:Z3 lever paddle:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.1301 max 0.2347 (n 23232) | PASS |
| zone:Z4 bushing + tip:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.3008 max 0.7374 (n 54593) | FAIL |
| zone:Z4 bushing + tip:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 1.0629 max 2.6023 (n 47622) | FAIL |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| R knob + sleeve + band junction | region | scan_to_cad | reported | reported | n 72677 · p95 1.6444 · max 4.5184 | n 55711 · p95 0.2525 · max 0.4787 | region bucket, reported; contains D1 |
| R knob + sleeve + band junction | region | cad_to_scan | reported | reported | n 70322 · p95 0.4181 · max 2.1129 | n 56135 · p95 0.2588 · max 0.7411 | region bucket, reported; contains D1 |
| R rod lower (collar, groove, bead, lug) | region | scan_to_cad | reported | reported | n 35685 · p95 0.2362 · max 0.5071 | n 35685 · p95 0.2362 · max 0.5071 | region bucket, reported |
| R rod lower (collar, groove, bead, lug) | region | cad_to_scan | reported | reported | n 46029 · p95 0.4606 · max 2.0817 | n 38130 · p95 0.2112 · max 0.6456 | region bucket, reported |
| Z1 rod spigot taper + O-ring seats | whole | scan_to_cad | PASS | PASS | n 39907 · p95 0.1306 · max 0.565 | n 39907 · p95 0.1306 · max 0.565 | machine interface (intake Z1, z 21..67); gated at the regime p95/max as the intake table states |
| Z1 rod spigot taper + O-ring seats | whole | cad_to_scan | FAIL | PASS | n 57398 · p95 0.5012 · max 1.6893 | n 48538 · p95 0.1329 · max 0.6926 | machine interface (intake Z1, z 21..67); gated at the regime p95/max as the intake table states |
| Z2 steel tube B-bend-C | whole | scan_to_cad | PASS | PASS | n 26716 · p95 0.2286 · max 0.5805 | n 26716 · p95 0.2286 · max 0.5805 | intake Z2; box starts after the sealing band (x>23.5) and ends above the bushing (z>-31) |
| Z2 steel tube B-bend-C | whole | cad_to_scan | FAIL | PASS | n 26372 · p95 0.2283 · max 0.8018 | n 23764 · p95 0.2142 · max 0.3451 | intake Z2; box starts after the sealing band (x>23.5) and ends above the bushing (z>-31) |
| Z3 lever paddle | whole | scan_to_cad | PASS | PASS | n 20978 · p95 0.134 · max 0.2475 | n 20978 · p95 0.134 · max 0.2475 | intake Z3; paddle outboard of the knob |
| Z3 lever paddle | whole | cad_to_scan | PASS | PASS | n 24256 · p95 0.1349 · max 0.7438 | n 23232 · p95 0.1301 · max 0.2347 | intake Z3; paddle outboard of the knob |
| Z4 bushing + tip | whole | scan_to_cad | FAIL | FAIL | n 54593 · p95 0.3008 · max 0.7374 | n 54593 · p95 0.3008 · max 0.7374 | intake Z4; includes the bushing underside windows and the tip bore mouth (partly unobservable) |
| Z4 bushing + tip | whole | cad_to_scan | FAIL | FAIL | n 72226 · p95 1.5711 · max 2.6173 | n 47622 · p95 1.0629 · max 2.6023 | intake Z4; includes the bushing underside windows and the tip bore mouth (partly unobservable) |

### Masks (masked and unmasked are both shown above)

| mask | direction | why | fraction removed | stats inside |
|---|---|---|---|---|
| M1 D1 torn flash | scan_to_cad | torn rubber flash/flap at the knob/sleeve junction is specimen damage, not design geometry, and is deliberately not modelled; points there are not a surface deviation of the modelled part | 0.0674 | n: 16966; rms: 1.3103; mean: 0.8211; p50: 0.2751; p95: 2.9842; p99: 3.9607; max: 4.5184 |
| M1 D1 torn flash | cad_to_scan | torn rubber flash/flap at the knob/sleeve junction is specimen damage, not design geometry, and is deliberately not modelled; points there are not a surface deviation of the modelled part | 0.0407 | n: 12223; rms: 0.5292; mean: 0.3347; p50: 0.1604; p95: 1.3056; p99: 1.761; max: 2.1129 |
| M2 open boundary | cad_to_scan | CAD->scan distance measured to a scan hole EDGE (33 open-boundary loops, intake coverage.json) is not a surface deviation | 0.1694 | n: 50834; rms: 0.7194; mean: 0.4868; p50: 0.2664; p95: 1.6247; p99: 2.2393; max: 2.6173 |

**CHK-MASK: mask-dependent pass(es):** [whole part scan_to_cad, zone Z1 rod spigot taper + O-ring seats cad_to_scan, zone Z2 steel tube B-bend-C cad_to_scan].

### Mask sensitivity

| band | direction | stats | variant |
|---|---|---|---|
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.0122; max_over_by: 3.7184 | scan_to_cad | n: 251631; rms: 0.3578; mean: 0.134; p50: 0.0663; p95: 0.3122; p99: 2.0561; max: 4.5184 | all masks except M1 D1 torn flash |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 1.8023 | cad_to_scan | n: 249166; rms: 0.2344; mean: 0.1109; p50: 0.0595; p95: 0.2997; p99: 1.0893; max: 2.6023 | all masks except M1 D1 torn flash |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.5813; max_over_by: 1.8173 | cad_to_scan | n: 287777; rms: 0.3565; mean: 0.1678; p50: 0.0679; p95: 0.8813; p99: 1.6876; max: 2.6173 | all masks except M2 open boundary |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.1829; max_over_by: 1.8023 | cad_to_scan | n: 275234; rms: 0.2731; mean: 0.1308; p50: 0.0638; p95: 0.4829; p99: 1.387; max: 2.6023 | M2 open boundary radius 0.0 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.0048; max_over_by: 1.8023 | cad_to_scan | n: 258680; rms: 0.2366; mean: 0.1121; p50: 0.0598; p95: 0.3048; p99: 1.0875; max: 2.6023 | M2 open boundary radius 0.2 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 1.8023 | cad_to_scan | n: 252080; rms: 0.2284; mean: 0.1085; p50: 0.059; p95: 0.2881; p99: 1.0655; max: 2.6023 | M2 open boundary radius 0.4 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 1.8023 | cad_to_scan | n: 240232; rms: 0.2254; mean: 0.106; p50: 0.0581; p95: 0.2751; p99: 1.0596; max: 2.6023 | M2 open boundary radius 0.8 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 1.8023 | cad_to_scan | n: 220226; rms: 0.2255; mean: 0.104; p50: 0.0566; p95: 0.2673; p99: 1.0713; max: 2.6023 | M2 open boundary radius 1.5 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 1.8023 | cad_to_scan | n: 191467; rms: 0.192; mean: 0.0923; p50: 0.0544; p95: 0.237; p99: 0.9035; max: 2.6023 | M2 open boundary radius 2.5 mm |

### Over-band point clusters, scan → CAD (> 0.8 mm)

5721 points (0.0227 fraction) in 2 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 3857 | [10.336, -3.767, -5.904] | [8.458, 13.944] | [0, 360] | 4.5184 | D1 torn rubber flash, -y side of the sleeve (centroid x 10.3, z -5.9): specimen damage pre-declared at intake, visible in photo_1/photo_2 and overlay x=10 / Z=-8; inside mask M1. Artefact, not a missing feature (same as it1/it2 cluster 0). |
| 1 | 1864 | [9.077, 6.139, -8.991] | [9, 12.823] | [26.1, 42.1] | 3.1901 | D1 torn rubber flash, +y side of the sleeve (centroid x 9.1, z -9.0): same flap, same evidence; inside mask M1 (same as it1/it2 cluster 1). |

### Over-band point clusters, CAD → scan (> 0.8 mm)

18561 points (0.0619 fraction) in 10 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 8240 | [38.771, -7.429, -42.061] | [32.23, 46.308] | [338.7, 359] | 2.6173 | **UNEXPLAINED** |
| 1 | 5751 | [37.399, -9.689, -49.83] | [36.365, 41.741] | [339.4, 350.6] | 2.2397 | **UNEXPLAINED** |
| 2 | 1374 | [-2.435, -2.629, 52.854] | [3.074, 4.292] | [209.5, 243.6] | 1.6893 | **UNEXPLAINED** |
| 3 | 967 | [-3.469, -3.732, 9.022] | [5.127, 6.54] | [167.1, 278.6] | 2.0817 | **UNEXPLAINED** |
| 4 | 923 | [7.528, -4.055, -9.371] | [7.368, 11.635] | [321.4, 343.3] | 2.1129 | **UNEXPLAINED** |
| 5 | 607 | [7.226, 4.881, -8.932] | [8.11, 9.767] | [22.5, 42] | 1.8539 | **UNEXPLAINED** |
| 6 | 350 | [-3.53, -3.247, 26.17] | [4.772, 5.557] | [189.9, 260.9] | 1.5267 | **UNEXPLAINED** |
| 7 | 283 | [-3.847, -5.348, 18.947] | [6.477, 6.774] | [221.6, 247.3] | 1.8955 | **UNEXPLAINED** |
| 8 | 38 | [-3.248, -5.242, 12.045] | [6.121, 6.311] | [232.9, 244.1] | 1.1312 | **UNEXPLAINED** |
| 9 | 25 | [9.056, -0.503, -4.017] | [9.008, 9.144] | [353.8, 359.8] | 1.0105 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 0.4216°, origin offset 0.3259 mm, point disagreement p95 0.6566 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (OUTSIDE).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| Z4 bushing + tip scan->CAD (p95 0.301 > 0.30 by <0.001 mm; max 0.737 in band) -- GEOMETRIC cause, fixable by a rebuild, not fixed (loop limit reached; owner accepted per DECISIONS.md), marginal | Coherent, one-signed residual groups, all with the scan OUTSIDE the CAD (CAD too small): (1) the tube-C entry on the bushing top: nearest face 64 (bushing top cone) 895 of 3477 points > 0.3 mm, 100 % outside, d max 0.724, plus 122 points on the tube C end (face 60), t -22.3..-21.4 / r 2.2..6.6 about the tip axis; overlay Z=-33.5 shows a smooth bulge 0.3-0.7 mm beyond the CAD around the tube entry and photo_1 shows a raised collar there - a missing feature, not modelled. 75 % of these points lie within 0.8 mm of a scan-hole edge (hole loop r 35.5..37.9, z -33..-30.4), so part could be edge curl, but the sign is 100 % one-sided and the photo supports a collar. (2) The bushing barrel underside rim (face 68, t -12.8..-8.6, r 7.5..10.2): 597 points > 0.3, 78 % outside - named in it2 ('barrel/rim r 5..9.5') and not addressed in it3. Report-only what-if (qa/attribution_probe.json): either group at the zone median gives Z4 p95 0.272/0.273. The it3 tip neck fixed the hub (it2 cells t -10..-8, r<3.5: 632 points > 0.3 -> 79). Z4 scan->CAD away from scan-hole edges reads p95 0.247. The miss is frame-sensitive (datum frame 0.297, not gated). | Rebuild (would need a 4th, owner-authorised loop): model the bushing-top collar around the tube entry (measure it from sections Z=-32..-35 and x=40) and refit the barrel underside rim; or a supplementary scan of the bushing top to confirm the collar vs hole-edge curl; or accept the <0.001 mm p95 excess (ACCEPT-BAND). Owner chose accept (DECISIONS.md). |
| Whole-part observable CAD->scan (p95 0.766 / max 2.601) and Z4 CAD->scan (p95 1.063 masked / 1.571 unmasked, max 2.602/2.617) -- NOT fixable by geometry | CAD surface with no scan behind it. Z4: 13892 of 13992 over-0.8 CAD samples lie on the 32 window-pocket/bore faces introduced in it2 (unchanged in it3); the other Z4 faces away from scan holes read p95 0.241 / max 0.511 (qa/attribution_probe.json). Whole part: with D1, scan-hole-adjacent (0.8 mm) and bore points removed CAD->scan reads p95 0.233 / max 2.602, the max being the window floors (unscanned; overlays x=44.4, Z=-43.5, Z=-44.4). Hole-adjacent samples: 50870, p95 1.628. The it3 changes (bend, paddle, neck) do not touch these surfaces; observable p95 moved 0.736 -> 0.766 because the ICP and the seeded CAD samples changed (same protocol, different CAD). | cannot be fixed by geometry: any pocket/bore depth leaves an unscanned floor/wall. Pin-gauge/depth readings of the bore and one window (then model the measured depth), a supplementary scan of the bushing underside, or accept with L3 declared (ACCEPT-BAND). A shallower model brings back the it1 scan->CAD clusters. |
| Whole-part scan->CAD UNMASKED (p95 0.312 / max 4.518; gated masked number passes) -- NOT fixable by geometry | D1 torn flash (clusters 0 and 1: 5721 of 5721 over-band points), specimen damage, deliberately not modelled. | rescan a clean specimen, or accept with M1 declared (ACCEPT-BAND). |

Missed band(s): `cad_to_scan_observable: p95 0.766 max 2.601 vs 0.3/0.8`; `zone:Z4 bushing + tip:scan_to_cad: p95 0.301 max 0.737 vs 0.3/0.8`; `zone:Z4 bushing + tip:cad_to_scan: p95 1.063 max 2.602 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | no Tier-1 (no calipers) |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | finding | QA grading is independent: own ICP of the it3 CAD onto the full-res scan (T_refine QA-only, never written back), datum re-derived from the raw scan, no expected value taken from builder params. Finding (carried from it1/it2): the builder's record (MODELING_PLAN §0/§8 self-check passes; it3 re-measurements in measure/figures/measure_it3.json of the same scan) is a scan-derived consistency check, not independent evidence. |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 2 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | finding | all 12 intake features exist in the it3 CAD (overlays); D1 not modelled by declaration; the it3 tip neck under the bushing is new and is supported by the scan (Z4 hub cells t -10..-8, r<3.5 no longer over band; zone_probe). Finding: a coherent one-signed scan->CAD group at the tube-C entry on the bushing top (nearest CAD face 64, bushing top cone, 895 of 3477 points > 0.3 mm, 100 % scan OUTSIDE the CAD, d max 0.724; tube C end face 60 adds 122 more) shows material the CAD lacks: overlay Z=-33.5 shows the scan bulging 0.3-0.7 mm beyond the CAD around the tube entry, and photo_1 shows a raised collar on the bushing top around the tube. Not modelled -> part of the Z4 scan->CAD miss. |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | pass | build/export_check.json (it3): F03 lug corner 0.6 target = 0.6 used OK; F05 plate perimeter round 1.946 target = 1.946 used OK (it2: 1.2 assumed). Z3 now reads p95 0.134 scan->CAD (zone_probe: perimeter mean signed +0.048 vs +0.177 in it2), so the measured radius is confirmed by the gate. Lug radius still ASSUMED. |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | fresh agent; see independence |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | pass | it2 -> it3 compared under the SAME protocol as it1/it2: qa/regime.json (cp of intake/regime.json), masks.json (M1 pre-declared D1 box x 6.5..13 z -15..-1, both directions; M2 open boundary 0.8 mm, CAD->scan, QA-added at it1), zones.json, icp_scan_masks.json and datum_spec.json are byte-identical copies of _it2_SUPERSEDED/qa/ (which were byte-identical to it1). ICP params identical (ns 3M seed 11, nc 300k seed 13, normal 70 deg, boundary 0.8, corr 3.0, cap 60, tol 1e-6); deviation sampling identical (all 251631 scan verts, c2s 300k seed 2, k 8, n_samp 3M seed 0, no vertex candidates); observability identical (20000 seed 5, far 0.5, cone 60, 6 rays, offset 0.05, unbounded); sweep radii 0,0.2,0.4,0.8,1.5,2.5 and cluster params (0.8 mm, eps 1.0, min 20) identical; the it2 overlay panel sets re-drawn identically (overlay_rod, overlay_lower, overlay_it2_extra) plus 8 new it3 panels (overlay_it3_extra). Datum audit and datum_crosscheck reproduce it2 exactly (same alignment.json). Not like-for-like by construction: ICP re-run on the new CAD (it2 49 its 0.060 deg/0.053 mm, it3 44 its 0.053 deg/0.059 mm) and seeded CAD samples fall on a different surface, so M2 and the observable subsample select different points. Probe changes: zone_probe.py chunk 20000 -> 2000 (OOM on the finer it3 tessellation; chunking does not change results); attribution_probe.py adds a scan->CAD Z4 face attribution. Improvements in Z2/Z3 come from geometry (STEP diff confines the change to the bend, the paddle and the tip neck), not from protocol. |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | finding | whole part scan_to_cad; zone Z1 rod spigot taper + O-ring seats cad_to_scan; zone Z2 steel tube B-bend-C cad_to_scan |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | finding | census (QA, both frames): 122 faces (it2 109); plane 47, cone 33, cylinder 31, bspline 5, revolution 3, sphere 2, torus 1; analytic share 77.2 % by QA's count (it2 83.3 %; the bend torus was replaced by one bspline sweep face, area 331). No loft(ruled=True) (model.py:140 ruled=False, the planned fairing loft); no slice stack. New in it3: the bend is ONE sweep of a circle along a spline through 10 scanned centreline stations (model.py:249-258) - a fitted path, not a slice stack, accepted. Minor findings: (a) the bend radius bend_tube_r differs from the straight tube radius, which leaves two small annular ledges (qa/it2_it3_diff.json: two new PLANE faces of 1.61 mm2 at the bend ends) - a modelling artefact, not a scanned feature; (b) carried from it1: the rod bead/groove z 9.75..12.75 is a revolved measured (z,r) polyline. |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | pass | photo_1, photo_2 walked by this agent: tapered rod with O-rings, knob, paddle with dish, sleeve + sealing band, steel tube with one bend, white bushing (ribbed/windowed tip-side face and a raised collar where the tube enters, photo_1), steel tip with open bore - all present in CAD except the bushing-top collar (see CHK-ENUM). Torn flap at the knob/sleeve junction visible in both photos (supports M1/D1). Window floors and bore depth not visible. No scale reference. |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict BAND_NOT_MET |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 3 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L1 | Scan-only: no calipers. no Tier-1 (no calipers run); absolute scale not caliper-verified (units assumed mm). | any caliper reading (>=3 envelope dims for a scale test) -> re-run Tier-1 and scale check | qa/gate.json#limitations; qa/VERDICT.md |
| L2 | Masks, mask-dependent pass: the whole-part scan-to-CAD pass holds only with mask M1 (the pre-declared torn-flash box D1); unmasked it is over the band (torn flash). Zone Z1 and zone Z2 CAD-to-scan pass only with the QA-added open-boundary mask M2. Masked and unmasked numbers are side by side in qa/VERDICT.md. | rescan with the torn flap trimmed or pressed back (or a replacement part), and a supplementary scan covering the 33 hole loops (rod theta 180..260, bushing top / tube entry) -> re-run unmasked | qa/gate.json#limitations; qa/VERDICT.md |
| L3 | Unobservable or uncovered CAD surface: the tip bore interior and the bushing window pockets (both modelled to the depth the scan proves, as lower bounds), the hidden assembly interfaces and the scan holes. The observability ray test counts most of them as visible, so they sit inside the gated observable CAD-to-scan number and cause its miss. | a pin-gauge/depth reading of the tip bore and of one window pocket, or a supplementary scan of the bushing underside -> re-run CAD->scan | qa/gate.json#limitations; qa/VERDICT.md |
| L4 | Datum audit (report-only) is outside the RE_SPEC reference with the normals-eigen method; the QA section-circle cross-check agrees with the builder datum. The Z4 scan-to-CAD p95 is at the band edge and frame-sensitive (passes in the builder frame, misses after ICP). | any datum change at intake -> re-run the whole QA | qa/gate.json#limitations; qa/VERDICT.md |
| L5 | Overlays are drawn in the builder alignment frame (no registration input in overlay.py); the ICP correction is below the line widths. | if the ICP correction ever exceeds the overlay line width (see qa/VERDICT.md L5) -> redraw overlays in the registered frame | qa/gate.json#limitations; qa/VERDICT.md |
| L6 | Known unmodelled geometry: the raised collar on the bushing top where tube C enters, and the barrel underside rim. They cause the Z4 scan-to-CAD band miss, which the owner accepted instead of a fourth loop. | any rebuild of the bushing (collar/rim modelled), a caliper reading of the collar, or a supplementary scan of the bushing top -> re-run the full verify | qa/gate.json#limitations; qa/VERDICT.md |
| L7 | Datum STOP rule passed on the self-referential path: the rod spigot (the cleanest surface) residual exceeds the one-loop IRLS circle noise floor, a different estimator; recorded in DECISIONS.md. | a noise-floor estimator matching the datum residual (QUESTIONS.md section F), or any datum change -> re-run intake and verify | DECISIONS.md; intake/alignment.json#findings |
| L8 | Torn rubber flash at the knob/sleeve junction (specimen damage D1) is not modelled; the intact surface under it is modelled from the neighbouring scan. | a rescan of an undamaged part or with the flap removed -> re-run measure (fairing, sleeve root) and verify | intake/INTAKE_CARD.md section 2 |
| L9 | Process: the intake card and measurement request were rendered after the measure pass, and the modelling plan after the self-check builds (declared, no number changed). | none needed for the geometry; any audit of the run order reads DECISIONS.md | DECISIONS.md; build/MODELING_PLAN.md section 0 |

## 12. Assumptions and invented geometry

Parameters not measured on the scan or by caliper (source tag from `measure/params.json`):

| parameter | value | source | evidence |
|---|---|---|---|
| `knob_bottom_z` | -14.4 | assumed | measure/figures/measurements.json |
| `lug_corner_r` | 0.6 | assumed | measure/figures/measurements.json |

- Hidden interfaces between the assembly parts (inside the knob, sleeve, bushing) are not modelled: the STEP is one fused outer solid. _(source: assumed; DECISIONS.md PART-CLASS)_
- The torn rubber flash at the knob/sleeve junction (specimen damage, photos) is not modelled. _(source: assumed; intake/INTAKE_CARD.md section 2 (D1))_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** any use that needs the declared band: the band is NOT met and was accepted by the owner (DECISIONS.md ACCEPT-BAND)
- **Not fit for:** manufacture or tooling of any single component: the parts of the assembly are fused and their hidden interfaces are not modelled
- **Not fit for:** fit-critical use of the spigot or tube diameters until calipered (absolute scale not caliper-verified)
- Fit for: visual and packaging/clearance models of the whole steam wand
- Fit for: a starting point for splitting into component models once calipers and part boundaries are supplied
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): Iteration-3 CAD is BAND_NOT_MET (not approved), delivered only on the owner's recorded acceptance. It is a scan-only, uncalipered reconstruction of a damaged assembly specimen: not fit for tooling or for the fit-critical machine interface (rod spigot / O-ring seats) until calipered; the tip bore depth (13.6) and window depth (2.52) are scan lower bounds, not measured depths; the bushing-top collar at the tube entry is not modelled; hidden internal interfaces are not modelled; the one-fused-solid STEP is not a multi-body assembly. The whole-part scan->CAD pass and the Z1/Z2 CAD->scan passes are masked passes.

## 14. Human acceptance of the band miss

Accepted by **Ikbal (owner, question card)** on 2026-09-28 (`DECISIONS.md`, ACCEPT-BAND): Accept and deliver: accepts cad_to_scan_observable, zone:Z4 bushing + tip:scan_to_cad and zone:Z4 bushing + tip:cad_to_scan band misses, gate 34a11505e84d (created 2026-09-28T09:57:42+00:00); unscanned window floors/bore and scan holes cannot be fixed by geometry, the marginal Z4 scan->CAD cause (bushing-top collar) is declared as L6.. Record: `decisions/accept_band.md` (sha256 `53baed091d9c138cfd50818c1702d9fbf6e9159bb9c9d00d79b1d54beccce1ed`).

## 15. Reproduction

```
cd build && python3 model.py --params ../measure/params.json --alignment ../intake/alignment.json --out . --part OD-S02_steam-rod --scripts <skills>/stl-re-rebuild-build123d/scripts
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-S02_steam-rod.step | 13753.4894 | 0 | 0 | yes | yes | no |
| OD-S02_steam-rod_datum.step | 13753.4894 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 16. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | 34a11505e84d1f296ffffbd7cfa913e59b508110925d1b2aa46c0b58515c87e9 |
| `measure/params.json` | a39aa148455ef3e4e6a90f6d91c7e28065356d3ce92f03926b742dba016fc102 |
| `build/export_check.json` | 6819a0c4cb8e4016f794594e18e733c81c16925e26084e8fff341d054b4c821b |
| `intake/alignment.json` | 17596743e9e2f8950aa01f5cf943f26bbeeebaea6fb411191c29e6622dffc292 |
| `deliver/repro.json` | 5f3940c769949f6db1dac8faf6be9a6350defa122cee14eae7d74edbf52a7299 |
| `deliver/limitations.json` | 8e140f6c13b53d999c6a568dd84dbae83158a677068bb04d4ee0bdf5782aeed0 |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
