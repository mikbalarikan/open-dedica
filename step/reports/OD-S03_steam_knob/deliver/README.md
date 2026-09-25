# OD-S03_steam-knob — STL → STEP reverse-engineering delivery

**Verdict: `BAND_NOT_MET`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 2 of 3 (earlier iterations kept: `_it1_SUPERSEDED/`).  
**Verification independence (CHK-INDEP):** pass — fresh verifier context, own ICP and scripts  

> **A deviation band was NOT met.** Delivered only under the recorded human acceptance below (by Ikbal (owner, decision card), 2026-09-25, record `decisions/accept_band.md`).

## 1. The part

![reference photo](../input/photos/1.png)

Steam-valve knob of an espresso machine: a chrome cap with one lever and a drafted slot pocket, a chrome collar, a white four-rib stem and a chrome threaded sleeve with a splined bore that locates on the valve spindle. Reverse-engineered from one full-resolution scan and five catalogue photos (no scale reference), scan-only (no caliper readings).

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-S03_steam-knob_datum.step` | datum | 1 | yes | yes | 83 | 11655.6425 | max: [27.775, 13.1248, 38.1043]; min: [-13.1879, -13.315, 0]; size: [40.9629, 26.4398, 38.1043] |
| `build/OD-S03_steam-knob.step` | scan | 1 | yes | yes | 83 | 11655.6425 | max: [-8.1005, 27.1401, -191.2945]; min: [-39.5557, -12.1785, -228.5675]; size: [31.4552, 39.3186, 37.273] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Intake: scan stats, orientation and holes; datum frame with the cap crown face as z = 0 (+Z toward the sleeve), origin on the sleeve/cap axis, lever clocked to +X (area-weighted Fourier clock, DECISIONS.md OTHER); feature enumeration E01-E20; regime baseline-skill plastic declared before any gate numbers.
2. Measure: every parameter taken from the scan by scripted fits in measure/figures/src (station circles, meridians, plane and cone fits, ripple and ramp fits); sub-body axes kept as measured positions; simplifications and open questions recorded in measure/params.json.
3. Rebuild: params-driven build123d model (build/model.py, plan build/MODELING_PLAN.md F01-F15): drafted cap and lever, loop fillets, pocket, collar/stem/spigot revolves, four ribs, helical end ramps; exported in the datum frame and the scan frame.
4. Iteration 1 was sent back (REVISE, non-watertight tessellation at the rib foot and under the sleeve bottom ramp); iteration 2 changed only those two constructions, parameters unchanged.
5. Verify in a fresh, independent agent context (CHK-INDEP pass): own ICP, two-way deviation with pre-declared masks and zones, over-band cluster attribution, overlays, photo plausibility. Verdict BAND_NOT_MET, accepted in writing by the owner (decisions/accept_band.md).

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | spigot/cap common axis (median of section centres) ∩ cap crown face plane | — | — |
| primary (plane) | cap crown face, flat field only (normals within 3 deg: excludes the onset of the crown edge round at r>10; coplanar lever top included) | 0.0146 / 0.098 | largest moulded flat perpendicular to the knob axis; the cap and lever are referenced from it; its normal is the turning axis direction |
| secondary (axis) | spigot thread envelope sections (closed loops) + cap outer wall faces (drafted) | 0.0431 / 0.3507 | the threaded spigot is the functional interface to the valve spindle / cap body; long axial span for CHK-TILT |
| clock | fourier_mass: lever wing centreline -> +X (area-weighted face-centre phase, run via intake/workaround/align_areaw.py) (angle -147.8263°) | — | — |

Measured tilt: 1.5006° (common slope, per-feature intercept, 25 stations over 2 feature(s), z 3.350..36.700 vs frame Z; NOT RESOLVABLE (heuristic): 'cap outer wall faces (drafted)' (1.46 deg @ 103.9 deg) vs 'spigot thread envelope sections (closed loops)' (2.57 deg @ 157.1 deg) differ by 2.06 deg > combined stderr 0.99 deg). Scale factor applied: 1. Scan noise floor: 0.0187 mm (rms of RANSAC+SVD plane on lever -Y flank (flat chrome side face of the lever wing) (12006 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
-0.549588   0.055972  -0.833559  -183.317611
 0.823392  -0.132522  -0.551783  -93.039758
-0.141349  -0.989598   0.026746   27.808765
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: scan 71 (total 71). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `bore_R` | 4.0884 | mm | 4.0884 | keep-measured | scan | 0.064 | yes | measure/figures/measurements.json#bore_R |
| `bore_floor_r` | 2.8185 | mm | 2.8185 | keep-measured | scan | 0.1 | no | measure/figures/measurements.json#bore_shoulder_slope,bore_seen_min_z |
| `bore_floor_z` | 34.6734 | mm | 34.6734 | keep-measured | scan | 0.1 | no | measure/figures/measurements.json#bore_seen_min_z |
| `bore_shoulder_top_z` | 35.8325 | mm | 35.8325 | keep-measured | scan | 0.1854 | no | measure/figures/measurements.json#bore_shoulder_slope |
| `cap_R_z0` | 12.5298 | mm | 12.5298 | keep-measured | scan | 0.0234 | no | measure/figures/measurements.json#cap_R_z0 |
| `cap_cx` | 0.032 | mm | 0.032 | keep-measured | scan | 0.0234 | no | measure/figures/measurements.json#cap_cx |
| `cap_cy` | -0.0951 | mm | -0.0951 | keep-measured | scan | 0.0234 | no | measure/figures/measurements.json#cap_cy |
| `collar_R` | 11.1163 | mm | 11.1163 | keep-measured | scan | 0.0271 | no | measure/figures/measurements.json#collar_R |
| `collar_bot_round_R` | 0.5685 | mm | 0.5685 | keep-measured | scan | 0.0425 | no | measure/figures/measurements.json#collar_bot_round_R |
| `collar_bot_z` | 16.6034 | mm | 16.6034 | keep-measured | scan | 0.0286 | no | measure/figures/measurements.json#collar_bot_z |
| `collar_cx` | -0.1166 | mm | -0.1166 | keep-measured | scan | 0.0271 | no | measure/figures/measurements.json#collar_cx |
| `collar_cy` | -0.0469 | mm | -0.0469 | keep-measured | scan | 0.0271 | no | measure/figures/measurements.json#collar_cy |
| `collar_top_round_R` | 0.3257 | mm | 0.3257 | keep-measured | scan | 0.0348 | no | measure/figures/measurements.json#collar_top_round_R |
| `crown_round_R` | 2.4591 | mm | [2.4361, 2.482] | mean-of-n | scan | 0.1136 | no | measure/figures/measurements.json#crown_round_R,lever_crown_round_R |
| `crown_z` | 0 | mm | 0.0008 | round-within-noise | scan | 0.0134 | no | measure/figures/measurements.json#crown_z |
| `draft_deg` | 3.0062 | deg | [3.0038, 3.1324, 2.8824] | mean-of-n | scan | 0.0299 | no | measure/figures/measurements.json#cap_draft_deg,lever_flank_py_draft_deg,lever_flank_my_draft_deg |
| `flange_z` | 17.0701 | mm | 16.8488..17.1682 | keep-measured | scan | 0.0917 | no | measure/figures/measurements.json#flange_z |
| `groove_in_R` | 0.6784 | mm | 0.4954..0.7356 | keep-measured | scan | 0.0907 | no | measure/figures/measurements.json#groove_in_R |
| `groove_in_bottom_z` | 15.9901 | mm | 15.7943..16.2384 | keep-measured | scan | 0.1862 | no | measure/figures/measurements.json#groove_in_bottom_z |
| `groove_in_rc` | 6.2376 | mm | 6.0455..6.3056 | keep-measured | scan | 0.1037 | no | measure/figures/measurements.json#groove_in_rc |
| `groove_out_R` | 0.7199 | mm | 0.5447..1.8936 | keep-measured | scan | 0.4045 | no | measure/figures/measurements.json#groove_out_R |
| `groove_out_bottom_z` | 16.2785 | mm | 15.7700..16.3688 | keep-measured | scan | 0.2126 | no | measure/figures/measurements.json#groove_out_bottom_z |
| `groove_out_rc` | 9.5394 | mm | 8.5397..9.6028 | keep-measured | scan | 0.3323 | no | measure/figures/measurements.json#groove_out_rc |
| `lever_blend_R_my_z0` | 7.0146 | mm | 7.0146 | keep-measured | scan | 0.1567 | no | measure/figures/measurements.json#lever_blend_R_z0 |
| `lever_blend_R_py_z0` | 6.1045 | mm | 6.1045 | keep-measured | scan | 0.2722 | no | measure/figures/measurements.json#lever_blend_R_z0 |
| `lever_flank_my_plan_deg` | 0.7377 | deg | 0.7377 | keep-measured | scan | 0.0049 | no | measure/figures/measurements.json#lever_flank_my_plan_deg |
| `lever_flank_my_y0` | -4.6779 | mm | -4.6779 | keep-measured | scan | 0.0049 | no | measure/figures/measurements.json#lever_flank_my_y18_z0,lever_flank_my_plan_deg |
| `lever_flank_py_plan_deg` | -0.3063 | deg | -0.3063 | keep-measured | scan | 0.0047 | no | measure/figures/measurements.json#lever_flank_py_plan_deg |
| `lever_flank_py_y0` | 4.6087 | mm | 4.6087 | keep-measured | scan | 0.0047 | no | measure/figures/measurements.json#lever_flank_py_y18_z0,lever_flank_py_plan_deg |
| `lever_tip_cx` | 22.6482 | mm | 22.6482 | keep-measured | scan | 0.0712 | no | measure/figures/measurements.json#lever_tip_cx |
| `mouth_chamfer_r_in` | 11.7564 | mm | 11.7564 | keep-measured | scan | 0.0379 | no | measure/figures/measurements.json#mouth_chamfer_r_in |
| `mouth_chamfer_r_out` | 12.4062 | mm | 12.4062 | keep-measured | scan | 0.0379 | no | measure/figures/measurements.json#mouth_chamfer_r_out |
| `mouth_ring_z` | 14.1039 | mm | 14.1039 | keep-measured | scan | 0.0284 | no | measure/figures/measurements.json#mouth_ring_z |
| `neck_R` | 4.7357 | mm | 4.7357 | keep-measured | scan | 0.052 | no | measure/figures/measurements.json#neck_R |
| `neck_bot_z` | 29.6 | mm | 29.6 | keep-measured | scan | 0.1 | no | measure/figures/measurements.json#neck_bot_z |
| `pocket_corner_R` | 0.6111 | mm | 0.6111 | keep-measured | scan | 0.1254 | no | measure/figures/measurements.json#pocket_corner_R |
| `pocket_draft_deg` | 3.986 | deg | [3.0027, 5.5746, 3.3806] | mean-of-n | scan | 0.14 | no | measure/figures/measurements.json#pocket_y_plus_draft_deg,pocket_y_minus_draft_deg,pocket_x_inner_draft_deg |
| `pocket_end_cx` | 20.1479 | mm | 20.1479 | keep-measured | scan | 0.0872 | no | measure/figures/measurements.json#pocket_end_cx |
| `pocket_floor_z` | 8.535 | mm | 8.535 | keep-measured | scan | 0.12 | no | measure/figures/measurements.json#pocket_floor_z |
| `pocket_x_inner_at_step` | 13.1956 | mm | 13.1956 | keep-measured | scan | 0.0082 | no | measure/figures/measurements.json#pocket_x_inner_at_step |
| `pocket_y_minus_at_step` | -2.1942 | mm | -2.1942 | keep-measured | scan | 0.0063 | no | measure/figures/measurements.json#pocket_y_minus_at_step |
| `pocket_y_plus_at_step` | 2.3121 | mm | 2.3121 | keep-measured | scan | 0.0081 | no | measure/figures/measurements.json#pocket_y_plus_at_step |
| `rib_count` | 4 | count | 4 | keep-measured | scan | 0 | no | measure/figures/count_ribs.json |
| `rib_theta_deg` | [-0.9033, 90.7332, 179.4017, -90.3892] | deg | [-0.9033, 90.7332, 179.4017, -90.3892] | keep-measured | scan | 0.5 | yes | measure/figures/measurements.json#rib_theta_deg |
| `rib_tip_r_flange` | [6.6342, 6.3765, 6.4813, 6.5263] | mm | [6.6342, 6.3765, 6.4813, 6.5263] | keep-measured | scan | 0.05 | no | measure/figures/measurements.json#rib_tip_r_z18,rib_tip_r_z27,flange_z |
| `rib_tip_r_top` | [6.2771, 5.8421, 6.4803, 6.3198] | mm | [6.2771, 5.8421, 6.4803, 6.3198] | keep-measured | scan | 0.05 | no | measure/figures/measurements.json#rib_tip_r_z18,rib_tip_r_z27,rib_top_z |
| `rib_top_z` | [28.3091, 28.2107, 28.2427, 28.1708] | mm | [28.3091, 28.2107, 28.2427, 28.1708] | keep-measured | scan | 0.05 | no | measure/figures/measurements.json#rib_top_z |
| `rib_width` | [1.0731, 0.9163, 1.2439, 1.0224] | mm | [1.0731, 0.9163, 1.2439, 1.0224] | keep-measured | scan | 0.05 | yes | measure/figures/measurements.json#rib_width |
| `sleeve_bottom_ramp_end_deg` | 255.3913 | deg | 255.3913 | keep-measured | scan | 0.0729 | no | measure/figures/measurements.json#sleeve_bottom_ramp_end_deg |
| `sleeve_bottom_ramp_h` | 1.0591 | mm | 1.0591 | keep-measured | scan | 0.0729 | no | measure/figures/measurements.json#sleeve_bottom_ramp_h |
| `sleeve_bottom_ramp_start_deg` | 132.6486 | deg | 132.6486 | keep-measured | scan | 0.0729 | no | measure/figures/measurements.json#sleeve_bottom_ramp_start_deg |
| `sleeve_bottom_z` | 32.3068 | mm | 32.3068 | keep-measured | scan | 0.0729 | no | measure/figures/measurements.json#sleeve_bottom_z |
| `sleeve_crest_R` | 5.9522 | mm | 5.9522 | keep-measured | scan | 0.0405 | yes | measure/figures/measurements.json#sleeve_crest_R |
| `sleeve_first_crest_z` | 32.9449 | mm | 32.9449 | keep-measured | scan | 0.0405 | no | measure/figures/measurements.json#sleeve_first_crest_z |
| `sleeve_ripple_pitch` | 1.2309 | mm | 1.2309 | keep-measured | scan | 0.0405 | yes | measure/figures/measurements.json#sleeve_ripple_pitch |
| `sleeve_ripple_rho` | 1.1371 | mm | 1.1371 | keep-measured | scan | 0.0405 | no | measure/figures/measurements.json#sleeve_ripple_rho |
| `sleeve_tail_r_in` | 4.6116 | mm | 4.6116 | keep-measured | scan | 0.1 | no | measure/figures/measurements.json#sleeve_tail_r_in |
| `sleeve_top_ramp_end_deg` | 245.4311 | deg | 245.4311 | keep-measured | scan | 0.0556 | no | measure/figures/measurements.json#sleeve_top_ramp_end_deg |
| `sleeve_top_ramp_h` | 0.9076 | mm | 0.9076 | keep-measured | scan | 0.0556 | no | measure/figures/measurements.json#sleeve_top_ramp_h |
| `sleeve_top_ramp_start_deg` | 124.6179 | deg | 124.6179 | keep-measured | scan | 0.0556 | no | measure/figures/measurements.json#sleeve_top_ramp_start_deg |
| `sleeve_top_z` | 37.2166 | mm | 37.2166 | keep-measured | scan | 0.0556 | no | measure/figures/measurements.json#sleeve_top_z |
| `stem_axis_dir_deg` | -24.0523 | deg | -24.0523 | keep-measured | scan | 0.0418 | no | measure/figures/axis_stations.json#stem_group_line |
| `stem_axis_tilt_deg` | 0.7539 | deg | 0.7539 | keep-measured | scan | 0.0418 | no | measure/figures/axis_stations.json#stem_group_line |
| `stem_axis_x0` | -0.4592 | mm | -0.4592 | keep-measured | scan | 0.0418 | no | measure/figures/axis_stations.json#stem_group_line |
| `stem_axis_y0` | 0.2355 | mm | 0.2355 | keep-measured | scan | 0.0418 | no | measure/figures/axis_stations.json#stem_group_line |
| `stem_base_z` | 17.4 | mm | 17.4 | keep-measured | scan | 0.1 | no | measure/figures/measurements.json#stem_base_z |
| `stem_core_R_base` | 5.3172 | mm | 5.3172 | keep-measured | scan | 0.087 | no | measure/figures/measurements.json#stem_core_R_z18,stem_core_R_z28,stem_base_z |
| `stem_core_R_top` | 5.1535 | mm | 5.1535 | keep-measured | scan | 0.087 | no | measure/figures/measurements.json#stem_core_R_z18,stem_core_R_z28,stem_core_top_z |
| `stem_core_top_z` | 28.4 | mm | 28.4 | keep-measured | scan | 0.1 | no | measure/figures/measurements.json#stem_core_top_z |
| `step_edge_R` | 0.5344 | mm | [0.4502, 0.6185] | mean-of-n | scan | 0.0999 | no | measure/figures/measurements.json#step_edge_R,lever_under_edge_R |
| `step_z` | 13.6892 | mm | [13.6687, 13.7097] | mean-of-n | scan | 0.0224 | no | measure/figures/measurements.json#step_z |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

| id | feature | params |
|---|---|---|
| F01 | cap cylinder, crown to step | [cap_R_z0, crown_z, step_z] |
| F02 | lever plan sketch + extrude (tip arc tangent to flanks) | [lever_flank_py_y0, lever_flank_py_plan_deg, lever_flank_my_y0, lever_flank_my_plan_deg, lever_tip_cx] |
| F03 | union cap and lever | [] |
| F04 | lever-cap blend fillets | [lever_blend_R_py_z0, lever_blend_R_my_z0] |
| F05 | one mould draft on all side faces | [draft_deg] |
| F06 | crown loop fillet | [crown_round_R] |
| F07 | step-face outer loop fillet | [step_edge_R] |
| F08 | drafted lever slot pocket (assumed flat floor) | [pocket_x_inner_at_step, pocket_end_cx, pocket_y_plus_at_step, pocket_y_minus_at_step, pocket_floor_z, pocket_corner_R, pocket_draft_deg] |
| F09 | collar revolve with mouth chamfer, rounds and outer groove | [mouth_chamfer_r_out, mouth_chamfer_r_in, mouth_ring_z, collar_R, collar_top_round_R, collar_bot_round_R, collar_bot_z, groove_out_rc, groove_out_R, groove_out_bottom_z, flange_z] |
| F10 | stem revolve with inner groove (one revolved crevice) | [groove_in_rc, groove_in_R, groove_in_bottom_z, stem_base_z, stem_core_R_base, stem_core_R_top, stem_core_top_z, neck_R, neck_bot_z] |
| F11 | four ribs along the measured tip lines | [rib_count, rib_theta_deg, rib_width, rib_tip_r_flange, rib_tip_r_top, rib_top_z] |
| F12 | spigot revolve: neck, sleeve with torus crest rings, bore, shoulder cone, assumed bore floor | [sleeve_bottom_z, sleeve_top_z, sleeve_crest_R, sleeve_ripple_rho, sleeve_ripple_pitch, sleeve_first_crest_z, bore_R, bore_shoulder_top_z, bore_floor_r, bore_floor_z] |
| F13 | sleeve bottom helical ramp cut | [sleeve_bottom_ramp_start_deg, sleeve_bottom_ramp_end_deg, sleeve_bottom_ramp_h] |
| F14 | sleeve top helical tail | [sleeve_top_ramp_start_deg, sleeve_top_ramp_end_deg, sleeve_top_ramp_h, sleeve_tail_r_in] |
| F15 | union all sub-bodies, export datum and scan frames | [cap_cx, cap_cy, collar_cx, collar_cy, stem_axis_x0, stem_axis_y0, stem_axis_tilt_deg, stem_axis_dir_deg] |

## 7. Tier-1 — caliper dims re-measured on the STEP

**Tier-1 not run: no caliper dimensions exist.** Every dimension is scan authority (or operator spec); see the source column in §5. Absent is not passed.

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), iterations 35/60, converged yes, correction 0.073° / 0.0237 mm.  
Unobservable CAD fraction: 0.002.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 182580 | 0.0902 | 0.0258 | 0.1502 | 0.278 | 2.3484 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 182580 | 0.0902 | 0.0258 | 0.1502 | 0.278 | 2.3484 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 0.2668 | 0.0353 | 0.4578 | 1.4132 | 2.987 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 252457 | 0.0723 | 0.0284 | 0.1545 | 0.2752 | 0.7534 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 19960 | 0.2667 | 0.0348 | 0.4385 | 1.4439 | 2.792 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.1502 max 2.3484 (n 182580) | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 0.4385 max 2.792 (n 19960) | FAIL |
| zone:Z1 threaded sleeve OD:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.1878 max 0.2925 (n 13837) | PASS |
| zone:Z1 threaded sleeve OD:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.182 max 0.517 (n 18672) | PASS |
| zone:Z2 sleeve bore visible:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.1677 max 0.3715 (n 1703) | PASS |
| zone:Z2 sleeve bore visible:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.1691 max 0.5178 (n 2946) | PASS |
| zone:Z3 stem ribs and core:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.158 max 0.5176 (n 26609) | PASS |
| zone:Z3 stem ribs and core:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.2133 max 0.5674 (n 38192) | PASS |
| zone:Z4 crown cap wall lever:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.1113 max 2.3484 (n 105799) | FAIL |
| zone:Z4 crown cap wall lever:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.1036 max 0.3897 (n 135627) | PASS |
| zone:Z5 step face and collar:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.1404 max 0.7203 (n 21240) | PASS |
| zone:Z5 step face and collar:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.1366 max 0.462 (n 35494) | PASS |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| B z 0-5 | region | scan_to_cad | reported | reported | n 59587 · p95 0.1073 · max 0.3943 | n 59587 · p95 0.1073 · max 0.3943 | — |
| B z 0-5 | region | cad_to_scan | reported | reported | n 80556 · p95 0.3751 · max 2.1095 | n 67632 · p95 0.107 · max 0.3897 | — |
| B z 13.2-17 | region | scan_to_cad | reported | reported | n 27418 · p95 0.2265 · max 1.0914 | n 27418 · p95 0.2265 · max 1.0914 | — |
| B z 13.2-17 | region | cad_to_scan | reported | reported | n 58138 · p95 0.4425 · max 1.1428 | n 45779 · p95 0.1556 · max 0.6939 | — |
| B z 17-29.5 | region | scan_to_cad | reported | reported | n 27519 · p95 0.1484 · max 0.3364 | n 27519 · p95 0.1484 · max 0.3364 | — |
| B z 17-29.5 | region | cad_to_scan | reported | reported | n 46876 · p95 0.3254 · max 0.9463 | n 41051 · p95 0.2289 · max 0.7534 | — |
| B z 29.5-32.2 neck | region | scan_to_cad | reported | reported | n 4361 · p95 0.2206 · max 0.4648 | n 4361 · p95 0.2206 · max 0.4648 | — |
| B z 29.5-32.2 neck | region | cad_to_scan | reported | reported | n 6312 · p95 0.24 · max 0.5596 | n 5783 · p95 0.2412 · max 0.5596 | — |
| B z 32.2-38.4 sleeve | region | scan_to_cad | reported | reported | n 17483 · p95 0.1902 · max 0.5957 | n 17483 · p95 0.1902 · max 0.5957 | — |
| B z 32.2-38.4 sleeve | region | cad_to_scan | reported | reported | n 29515 · p95 1.0469 · max 2.987 | n 24217 · p95 0.2026 · max 0.6233 | — |
| B z 5-13.2 | region | scan_to_cad | reported | reported | n 46212 · p95 0.117 · max 2.3484 | n 46212 · p95 0.117 · max 2.3484 | — |
| B z 5-13.2 | region | cad_to_scan | reported | reported | n 78603 · p95 0.7165 · max 2.754 | n 67995 · p95 0.1011 · max 0.2522 | — |
| I1 lever pocket floor | interior | scan_to_cad | reported | reported | n 2493 · p95 0.3057 · max 0.6751 | n 2493 · p95 0.3057 · max 0.6751 | INTAKE §3: pocket floor not reached by the scanner |
| I1 lever pocket floor | interior | cad_to_scan | reported | reported | n 9015 · p95 2.0341 · max 2.754 | n 2962 · p95 0.105 · max 0.2522 | INTAKE §3: pocket floor not reached by the scanner |
| I2 stem collar crevice | interior | scan_to_cad | reported | reported | n 6374 · p95 0.41 · max 1.0914 | n 6374 · p95 0.41 · max 1.0914 | INTAKE §3: annular crevice floor unobserved |
| I2 stem collar crevice | interior | cad_to_scan | reported | reported | n 28300 · p95 0.6536 · max 1.1428 | n 13323 · p95 0.2927 · max 0.7534 | INTAKE §3: annular crevice floor unobserved |
| I3 bore below visible depth | interior | scan_to_cad | reported | reported | n 268 · p95 0.3345 · max 0.5957 | n 268 · p95 0.3345 · max 0.5957 | INTAKE §3: bore interior below z~35 unscanned |
| I3 bore below visible depth | interior | cad_to_scan | reported | reported | n 3920 · p95 2.2936 · max 2.987 | n 23 · p95 0.1586 · max 0.162 | INTAKE §3: bore interior below z~35 unscanned |
| Z1 threaded sleeve OD | whole | scan_to_cad | PASS | PASS | n 13837 · p95 0.1878 · max 0.2925 | n 13837 · p95 0.1878 · max 0.2925 | INTAKE §4 Z1: screws/locates on the valve side; gated at regime p95/max per intake |
| Z1 threaded sleeve OD | whole | cad_to_scan | PASS | PASS | n 18805 · p95 0.1832 · max 0.517 | n 18672 · p95 0.182 · max 0.517 | INTAKE §4 Z1: screws/locates on the valve side; gated at regime p95/max per intake |
| Z2 sleeve bore visible | whole | scan_to_cad | PASS | PASS | n 1703 · p95 0.1677 · max 0.3715 | n 1703 · p95 0.1677 · max 0.3715 | INTAKE §4 Z2: bore r~4.0, visible to z~35.5 only |
| Z2 sleeve bore visible | whole | cad_to_scan | PASS | PASS | n 4091 · p95 0.2123 · max 0.5178 | n 2946 · p95 0.1691 · max 0.5178 | INTAKE §4 Z2: bore r~4.0, visible to z~35.5 only |
| Z3 stem ribs and core | whole | scan_to_cad | PASS | PASS | n 26609 · p95 0.158 · max 0.5176 | n 26609 · p95 0.158 · max 0.5176 | INTAKE §4 Z3: rotational drive/guide |
| Z3 stem ribs and core | whole | cad_to_scan | FAIL | PASS | n 43438 · p95 0.4315 · max 0.9463 | n 38192 · p95 0.2133 · max 0.5674 | INTAKE §4 Z3: rotational drive/guide |
| Z4 crown cap wall lever | whole | scan_to_cad | FAIL | FAIL | n 105799 · p95 0.1113 · max 2.3484 | n 105799 · p95 0.1113 · max 2.3484 | INTAKE §4 Z4: hand interface (includes the lever pocket walls) |
| Z4 crown cap wall lever | whole | cad_to_scan | FAIL | PASS | n 159159 · p95 0.5034 · max 2.754 | n 135627 · p95 0.1036 · max 0.3897 | INTAKE §4 Z4: hand interface (includes the lever pocket walls) |
| Z5 step face and collar | whole | scan_to_cad | PASS | PASS | n 21240 · p95 0.1404 · max 0.7203 | n 21240 · p95 0.1404 · max 0.7203 | INTAKE §4 Z5: seats against the machine panel (inferred) |
| Z5 step face and collar | whole | cad_to_scan | PASS | PASS | n 39289 · p95 0.1892 · max 0.5841 | n 35494 · p95 0.1366 · max 0.462 | INTAKE §4 Z5: seats against the machine panel (inferred) |

### Masks (masked and unmasked are both shown above)

| mask | direction | why | fraction removed | stats inside |
|---|---|---|---|---|
| M1 open boundary | cad_to_scan | CAD->scan distance measured to the EDGE of a scan hole (17 chrome-reflection holes, unscanned pocket floor, crevice floor, deep bore) is a coverage gap, not a surface deviation | 0.1571 | n: 47144; rms: 0.6516; mean: 0.4248; p50: 0.2292; p95: 1.5332; p99: 2.2367; max: 2.987 |
| M2 skin normal | cad_to_scan | a CAD point whose nearest scan point faces >70 deg away is corresponding to a different (occluded/opposite) wall, not an outer-skin deviation | 0.0065 | n: 1939; rms: 0.5278; mean: 0.4476; p50: 0.4506; p95: 0.8882; p99: 1.2293; max: 1.5498 |

**CHK-MASK: mask-dependent pass(es):** [whole part cad_to_scan, zone Z3 stem ribs and core cad_to_scan, zone Z4 crown cap wall lever cad_to_scan].

### Mask sensitivity

| band | direction | stats | variant |
|---|---|---|---|
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.1306; max_over_by: 2.187 | cad_to_scan | n: 298061; rms: 0.2643; mean: 0.104; p50: 0.035; p95: 0.4306; p99: 1.4167; max: 2.987 | all masks except M1 open boundary |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.1875 | cad_to_scan | n: 252856; rms: 0.0728; mean: 0.0468; p50: 0.0284; p95: 0.1553; p99: 0.2773; max: 0.9875 | all masks except M2 skin normal |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 2.0767 | cad_to_scan | n: 288770; rms: 0.1681; mean: 0.0752; p50: 0.0332; p95: 0.2698; p99: 0.7516; max: 2.8767 | M1 open boundary radius 0.0 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 1.6226 | cad_to_scan | n: 273146; rms: 0.0943; mean: 0.0543; p50: 0.0307; p95: 0.181; p99: 0.3454; max: 2.4226 | M1 open boundary radius 0.2 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.9403 | cad_to_scan | n: 265054; rms: 0.0778; mean: 0.0495; p50: 0.0297; p95: 0.1636; p99: 0.291; max: 1.7403 | M1 open boundary radius 0.4 mm |
| p95_band: 0.3; max_band: 0.8; pass: yes | cad_to_scan | n: 252457; rms: 0.0723; mean: 0.0466; p50: 0.0284; p95: 0.1545; p99: 0.2752; max: 0.7534 | M1 open boundary radius 0.8 mm |
| p95_band: 0.3; max_band: 0.8; pass: yes | cad_to_scan | n: 229017; rms: 0.0682; mean: 0.0436; p50: 0.0266; p95: 0.146; p99: 0.2619; max: 0.6233 | M1 open boundary radius 1.5 mm |
| p95_band: 0.3; max_band: 0.8; pass: yes | cad_to_scan | n: 191935; rms: 0.064; mean: 0.0404; p50: 0.0244; p95: 0.1351; p99: 0.2505; max: 0.6233 | M1 open boundary radius 2.5 mm |

### Over-band point clusters, scan → CAD (> 0.8 mm)

230 points (0.0013 fraction) in 2 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 206 | [-2.716, 10.982, 9.34] | [10.633, 12.064] | [99.6, 108.9] | 2.3484 | SCAN ARTEFACT (scan wrong, CAD right); identical to it1 cluster 0. 206 scan pts, r 10.6-12.1, z 6.9-11.1, theta 100-109, d up to 2.35 mm: a curled skin flap hanging 1-2 mm inside the cap wall at the edge of a chrome-reflection hole. All points <=0.75 mm from a scan open boundary (qa/cluster_probe.json); overlays theta=104 and Z=9.3/11.0 show the flap detached from the wall; photos 1,2,4,5 show a smooth intact cap wall. Not modelled; not maskable after the fact. |
| 1 | 24 | [2.81, -4.756, 15.177] | [5.247, 5.883] | [295.1, 307.6] | 1.0914 | REAL SCAN GEOMETRY the CAD lacks (CAD approximation); same as it1 cluster 1. 24 scan pts, r 5.25-5.9, z 14.9-15.4, theta 295-308, d up to 1.09 mm: at theta ~300 the stem wall continues down to z~15 inside the collar/stem crevice, deeper than the CAD's axisymmetric inner-groove arc (bottom ~16.0); overlay theta=300 shows it, theta 45/104/120 match. Photos 2/4/5 show only a dark gap (depth not resolvable). Points <=0.55 mm from a scan open boundary (crevice floor partly unscanned). |

### Over-band point clusters, CAD → scan (> 0.8 mm)

7608 points (0.0254 fraction) in 13 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 3131 | [18.068, -0.539, 8.928] | [13.503, 22.216] | [0, 360] | 2.754 | **UNEXPLAINED** |
| 1 | 1896 | [0.376, 0.001, 34.69] | [0.083, 3.158] | [0, 359.6] | 2.987 | **UNEXPLAINED** |
| 2 | 1131 | [-4.466, 11.819, 4.859] | [12.526, 12.856] | [101.6, 127.1] | 2.1095 | **UNEXPLAINED** |
| 3 | 929 | [8.865, 8.62, 1.938] | [12.027, 13.071] | [23.9, 66.4] | 1.8135 | **UNEXPLAINED** |
| 4 | 137 | [17.753, 4.523, 1.75] | [17.032, 19.725] | [13.2, 15.2] | 1.2263 | **UNEXPLAINED** |
| 5 | 80 | [-6.482, -2.556, 16.791] | [6.868, 7.065] | [191.7, 207.3] | 0.9463 | **UNEXPLAINED** |
| 6 | 68 | [-6.431, 2.715, 16.439] | [6.857, 7.126] | [147.9, 163.9] | 0.9521 | **UNEXPLAINED** |
| 7 | 54 | [3.002, -5.673, 16.136] | [6.025, 6.654] | [293.3, 302.8] | 1.1428 | **UNEXPLAINED** |
| 8 | 48 | [23.148, 4.509, 2.029] | [22.659, 24.627] | [10.1, 11.7] | 1.0071 | **UNEXPLAINED** |
| 9 | 32 | [-3.215, 6.116, 16.224] | [6.815, 7.038] | [108.7, 124.5] | 0.9116 | **UNEXPLAINED** |
| 10 | 29 | [2.184, 6.517, 16.58] | [6.794, 6.976] | [65.7, 78.3] | 0.9037 | **UNEXPLAINED** |
| 11 | 23 | [6.196, 2.366, 16.345] | [6.446, 6.798] | [17.6, 32.9] | 0.9516 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 3.8752°, origin offset 0.0206 mm, point disagreement p95 1.632 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (OUTSIDE).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| whole part scan->CAD max 2.348 (band 0.8) / zone Z4 cap wall scan->CAD max 2.348, theta 100-109, z 6.9-11.1 | scan artefact: chrome skin flap at a reflection hole (cluster 0); CAD matches the photos. p95 passes everywhere (0.150 whole, 0.111 Z4). | (a) owner records ACCEPT-BAND naming this miss and citing this gate; (b) rescan the cap with matting spray and re-run verify unchanged; a scan-side mask added now would be after the fact and is not offered. |
| stem/collar crevice theta ~295-308, z 14.9-15.4 (scan->CAD cluster 1, max 1.09) | non-axisymmetric as-assembled crevice modelled as one revolve groove; floor partly unscanned. | (a) accept as a declared simplification under ACCEPT-BAND; (b) a local deepening of the inner groove near theta 300 in a geometry loop (loop 3 of 3) would remove this cluster but would NOT clear the band, which cluster 0 still fails; not recommended on its own. |
| observable CAD->scan p95 0.438 / max 2.792 (band 0.3/0.8); CAD->scan clusters at lever pocket floor z~8.5-11.5 and bore floor disc z~34.7 | CAD surfaces with no scan behind them (assumed pocket floor, assumed bore floor, chrome holes on the cap wall z 1-8); the ray test counts them observable (L4). With the pre-declared masks CAD->scan is p95 0.154 / max 0.753 (passes). | (a) ACCEPT-BAND naming cad_to_scan_observable; (b) supply depth readings (caliper/depth gauge) for the pocket floor and bore floor, rebuild those closures and re-verify; (c) fix observability.py (L4) and re-run the gate; no geometry change from the scan alone can fix it. |

Missed band(s): `scan_to_cad:masked: p95 0.150 max 2.348 vs 0.3/0.8`; `cad_to_scan_observable: p95 0.438 max 2.792 vs 0.3/0.8`; `zone:Z4 crown cap wall lever:scan_to_cad: p95 0.111 max 2.348 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | no Tier-1 dims (scan-only) |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | pass | graded after QA's own ICP (35/60 its, converged, 0.073 deg / 0.024 mm); T_refine not written back; no expected value from params.json or the builder; datum audited on the raw scan |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 2 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | finding | E01-E19 present in CAD and consistent with photos 1-5 and overlays (unchanged from it1); E20 bore notch at theta~180 (z 36-37, visible in overlay Z=36.5) not modelled (plan-declared). Assumed closures (bore floor disc z~34.7, lever pocket floor z~8.5) are CAD->scan clusters 1/0 with no scan behind them. Scan->CAD cluster 1 (crevice, theta ~300) is real scan material the CAD lacks. |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | pass | export_check.json: 4 fillet ops (F04 x2, F06, F07), target == used, all OK |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | fresh verifier context, own ICP and scripts |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | pass | it1 vs it2 under the same protocol (qa/it1_vs_it2.json): regime/masks/zones/icp_scan_masks/datum_spec byte-identical to _it1_SUPERSEDED/qa, same deviation sampling + seeds, same ICP params, same observability params, both OFFICIAL (full-res). Differences are geometry: it1 VALIDITY fail (non-manifold tessellation) cleared; whole CAD->scan masked max 0.893 -> 0.753 and zone Z1 CAD->scan max 0.893 -> 0.517 come from removing the unintended sleeve wedge under the bottom ramp (it1 max located at z 32.4, r 5.7, theta 240-248; qa/c2s_masked_locate.json). Zone Z3 CAD->scan max 0.469 -> 0.567 and B z17-29.5 0.469 -> 0.753 are CAD re-sampling at the collar-mouth/crevice lip z~17.07 (same place it1 had unmasked 0.90), not a new defect. scan->CAD unchanged (p95 0.150, max 2.348). |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | finding | whole part cad_to_scan; zone Z3 stem ribs and core cad_to_scan; zone Z4 crown cap wall lever cad_to_scan |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | pass | census 83 faces (it1 88), QA analytic area 97.6%, 9 B-spline faces only on the helical sleeve ramps (plan-declared helicoids); no loft/ruled/polyline/slice in model.py (grep); model.py diff vs it1 is exactly the two plan-declared construction changes (F11 rib foot -OV, F13 ramp tool floor -h). Tessellation (qa/tess_probe.json): it2 watertight, 0 open / 0 non-manifold edges at 0.003/0.005/0.01/0.02 mm x 0.1 rad and 0.005/0.01 mm x 0.05 rad, both frames. Independent confirmation that it1 had TWO defects: rib foot z 15.99 (all settings) and sleeve bottom z 32.31, r 5.36, theta 192.2 (only at 0.1 rad; it1's single-setting probe missed it). Report-only: BOPAlgo_ArgumentAnalyzer flags 6 InvalidCurveOnSurface pairs (helical ramps z 32.9-37.5, shoulder z 29.2-29.6) in BOTH it1 and it2 (it1 had a 7th at the rib foot, now gone); QA-measured curve-on-surface deviation <= 2.8e-6 mm, below every edge tolerance (qa/cos_dev.json), BRepCheck valid -> analyzer false positive, not a validity fail. |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | pass | photos 1-5 walked: chrome cap with one lever and through-slot pocket (2,4,5), chrome collar rings, white 4-rib stem with a dark gap at the collar (crevice), chrome threaded sleeve, white splined bore (5). Cap wall smooth and intact in every view: the inward scan flap at theta ~100-109 is not a real dent. |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict BAND_NOT_MET |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 6 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L7 | Sleeve thread form is a SIMPLIFICATION, not a true thread: the scan shows planar ring turns (pitch 1.2309 mm, crest radius 5.9522 mm, scanner-smoothed ripple), modelled as touching torus rings plus right-hand helical ramps only on the two sleeve end faces. The real thread profile and spec (formed coil or cut thread, depth, handedness over the full length) are UNVERIFIED on this chrome scan and remain an open owner question. The spindle interface (thread and bore, bore radius 4.0884 mm) is the highest-risk feature. | Thread spec from the owner/manufacturer, or a thread gauge / pitch-gauge reading and a caliper reading over the crests on the physical knob -> rebuild the sleeve as a true helical thread and re-verify. | measure/params.json#open_questions,simplifications (sleeve ripple as rings, sleeve end ramps); build/MODELING_PLAN.md F12-F14 |
| L1 | Tier-1 not run: no Tier-1 (no calipers run), owner chose scan-only. Every dimension is ABSENT, not passed; the parameter table carries scan values only. | any caliper reading supplied -> re-run Tier-1 and this gate | qa/gate.json#limitations L1, #auto_limitations; DECISIONS.md MEASUREMENTS |
| L2 | Absolute scale UNVERIFIED (CHK-SCALE FLAG at intake): units assumed mm, scale factor 1 (none applied). The photos carry no scale reference. | one caliper reading on any feature (e.g. sleeve OD over crests or cap OD) | qa/gate.json#limitations L2; intake/alignment.json#scale_factor |
| L8 | ASSUMED closures: the lever-pocket floor (flat, at z 8.535 mm, seen by only a few scan faces, uncertainty 0.12 mm) and the bore floor (flat disc at z 34.6734 mm, radius 2.8185 mm, at the deepest observed scan point) are not surfaces the scanner reached. The bore below that depth and the internal splines seen in photo 5 are not modelled; the solid interior is assumed solid. These closures are the CAD->scan over-band clusters (max 2.754 mm at the pocket floor) that drive the cad_to_scan_observable miss. | a depth-rod reading of the lever-pocket floor and of the bore depth (or a sectioned/rescanned bore) -> rebuild those closures and re-verify. | build/MODELING_PLAN.md section 6; measure/params.json#open_questions; qa/gate.json#deviation.over_band_clusters.cad_to_scan |
| L9 | Scan->CAD max NOT MET from a scan artefact: a chrome skin flap hanging inside the cap wall at a reflection hole (cluster 0, max 2.3484 mm vs band 0.8 mm) makes whole-part and zone Z4 scan->CAD max fail while p95 passes (0.1502 mm vs 0.3 mm). The CAD holds the smooth, intact cap wall the photos show; the flap is not modelled. Accepted by the owner (ACCEPT-BAND). | rescan the chrome cap with matting spray and re-run verify unchanged. | qa/gate.json#miss_explanations.0, #deviation.over_band_clusters.scan_to_cad.clusters.0; qa/cluster_probe.json; decisions/accept_band.md |
| L4 | Observability ray test (known defect) counts open-mouthed unscanned regions (lever pocket floor, bore floor, crevice floor) as observable: unobservable fraction only 0.002, so the gated observable CAD->scan number (p95 0.4385 / max 2.792 mm) is inflated and is NOT MET. A QA coverage proxy (not the gate) keeps CAD->scan outside scan-hole neighbourhoods near band except a few points at the unscanned crevice floor. | observability.py fixed to treat unreached cavities as unobservable -> re-run deviation_gate.py | qa/gate.json#limitations L4; qa/c2s_residual_probe.json (coverage proxy, not the gate) |
| L6 | MASKED PASS (mask-dependent pass): whole-part CAD->scan (unmasked p95 0.4578 / max 2.987 mm; masked p95 0.1545 / max 0.7534 mm), zone Z3 CAD->scan (unmasked p95 0.4315 / max 0.9463 mm) and zone Z4 CAD->scan (unmasked p95 0.5034 / max 2.754 mm) pass only with the pre-declared M1 open-boundary / M2 skin-normal masks. These are not clean passes. | rescan closing the chrome holes / pocket and bore floors -> re-run without masks | qa/gate.json#limitations L6, #auto_limitations, #deviation.mask_dependent_passes, #deviation.masks |
| L10 | SIMPLIFICATION, non-rotational crevice: the stem/collar crevice is modelled as one revolved inner groove (median depth over sectors), but the scanned crevice floor varies around the axis; near theta 300 deg the scan wall continues deeper than the CAD groove (scan->CAD cluster 1, max 1.0914 mm). Crevice floor partly unscanned. | a photo or depth reading of the crevice floor around the full circumference (or a rescan of the stem/collar joint) -> model a local, non-rotational groove and re-verify (would remove this cluster, not the cap-wall miss). | qa/gate.json#miss_explanations.1, #deviation.over_band_clusters.scan_to_cad.clusters.1; measure/params.json#simplifications (groove depths) |
| L11 | UNMODELLED feature: the bore notch E20 (theta about 180 deg, near the sleeve top, visible in the scan and the Z overlay) is not modelled; the CAD bore is plain. Also not modelled: the sleeve top inner lip, rib root fillets. Each is a declared simplification with its measured cost in measure/params.json. | the owner confirms the notch is functional (keying the spindle) or supplies its size -> model it and re-verify. | measure/params.json#simplifications (bore notch (E20) not modelled, sleeve top inner lip, rib ends and roots); qa/VERDICT.md CHK-ENUM |
| L5 | Datum audit clock differs by 3.8752 deg (report-only, outside the reference band): datum_audit.py's Fourier clock is vertex-count weighted (known defect); QA area-weighted Fourier and a lever-flank bisector reproduce the builder clock closely. Axis 0.0205 deg, origin 0.0206 mm. | datum_audit.py fourier clock made area-weighted -> re-run audit | qa/gate.json#limitations L5, #datum_audit; qa/clock_crosscheck.json |
| L3 | scan_resolution 'full' is an orchestrator inference (DECISIONS.md OTHER), not owner-confirmed. | owner states the scan is a decimated copy -> relabel INSPECTION ONLY | qa/gate.json#limitations L3; input/INPUT_HASHES.json#scan_resolution |

## 12. Assumptions and invented geometry

- Units are millimetres; no scale was applied (scan-only, no caliper). _(source: assumed; intake/alignment.json#scale_factor; DECISIONS.md MEASUREMENTS)_
- Lever-pocket floor is flat at the sparsely seen floor level, with no floor fillet or mouth round. _(source: assumed; measure/params.json#pocket_floor_z, #simplifications)_
- Bore is closed by a flat floor disc at the deepest observed scan point; splines below are not modelled. _(source: assumed; build/MODELING_PLAN.md section 6; measure/params.json#open_questions)_
- Interior (cap/stem/sleeve internal interfaces) is modelled solid; the scan is an outer skin. The four coaxial sub-bodies are joined with a documented burial overlap (OV in build/model.py), which is construction clearance, not geometry. _(source: assumed; build/MODELING_PLAN.md section 6; build/model.py header)_
- Sleeve ripple is treated as planar rings with helical crossovers only at the end faces (formed coil reading of the scan), not a continuous helical thread. _(source: assumed; measure/params.json#simplifications, #open_questions)_
- One mould draft for cap wall, lever flanks, tip and blends; lever tip arc tangent to both flanks. _(source: assumed; measure/params.json#simplifications)_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** Not fit for manufacture or tooling of the spindle interface (sleeve thread form, bore splines and notch) until the thread spec is known and the sleeve and bore are calipered.
- **Not fit for:** Not fit for any use that depends on absolute size, pocket depth or bore depth: scale and depths are not caliper-verified (scan-only).
- **Not fit for:** Not a clean pass: the plastic band (p95 0.3 / max 0.8 mm) is NOT MET and was accepted by the owner; physical interchangeability requires mating-part or physical fit verification.
- Fit for: Visualisation, packaging and envelope/clearance work on the outer shape (cap, lever, collar, stem, sleeve envelope).
- Fit for: A design-intent starting point: build/model.py driven by measure/params.json, to be updated when caliper readings or the thread spec arrive.
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): Scan-only reconstruction under baseline-skill plastic bands, band not met (scan artefacts and unobserved floors). Geometry is one valid, watertight solid. Not fit for manufacture or tooling of the spindle interface (sleeve thread form, bore splines), pocket/bore depths or absolute size until calipered; fit for visual/packaging/envelope use once the owner accepts the listed misses.

## 14. Human acceptance of the band miss

Accepted by **Ikbal (owner, decision card)** on 2026-09-25 (`DECISIONS.md`, ACCEPT-BAND): Accept and deliver: accepts scan_to_cad:masked, cad_to_scan_observable and zone:Z4 crown cap wall lever:scan_to_cad misses, gate f70ad05cf7ed (created 2026-09-25T15:11:43+00:00); scan->CAD p95 passes, max from a cap-wall scan artefact, CAD->scan observable from unreached assumed floors.. Record: `decisions/accept_band.md` (sha256 `ae29d1e549ea239ea4c3fc485b072a87b1f804fcae3cfe87683aaa9297d90ab9`).

## 15. Reproduction

```
python3 build/model.py --params measure/params.json --alignment intake/alignment.json --out build --part OD-S03_steam-knob   # from the run root
python3 <skills>/stl-re-deliver/scripts/repro_check.py --run <run> -- python3 build/model.py --params measure/params.json --alignment intake/alignment.json --out build --part OD-S03_steam-knob
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-S03_steam-knob.step | 11655.6425 | 0 | 0 | yes | yes | no |
| OD-S03_steam-knob_datum.step | 11655.6425 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 16. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | f70ad05cf7edc26706c3c5a8fae476ee97239cf4ac096fea7f07fe2fe8fdb2e4 |
| `measure/params.json` | cb75654a2a1a0c50ae039a2bfc3b686defab8409125de5df50cc268ff2713560 |
| `build/export_check.json` | 017d92c512ae950b0b87ea424614a93231fb92ce638da5e4bd3c4d4efafef715 |
| `intake/alignment.json` | da75c108fad2f778fe0fe76926c6be9cdeabb6c16ec1a287e629054c0b1e583e |
| `deliver/repro.json` | 5d35294c691cad73c2ee9a48c2d69b42688ef2c15ec4996657252b84035da39f |
| `deliver/limitations.json` | 21bdeb6bbcb11550bdf93bbe454c43fc0ad42fe497acbb78154132f9931288cf |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
