# OD-G10_porta_filter_holder — STL → STEP reverse-engineering delivery

**Verdict: `HALT`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 1 of 3 (earlier iterations kept: none).  
**Verification independence (CHK-INDEP):** pass — fresh agent; see independence  

## 1. The part

![reference photo](../input/photos/2.webp)

Espresso-machine portafilter holder (group-head collar), moulded plastic: a cup with three internal bayonet lugs (stop block, ramped underside, top channel), a stepped shelf with under-lug pockets, a lip ring and a bottom plate with a two-lobed water opening and two screw bosses.

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-G10_porta_filter_holder_datum.step` | datum | 1 | yes | yes | 182 | 40425.3755 | max: [40.11, 40.11, 3.298]; min: [-40.11, -40.11, -27.835]; size: [80.22, 80.22, 31.133] |
| `build/OD-G10_porta_filter_holder.step` | scan | 1 | yes | yes | 182 | 40425.3755 | max: [64.1641, 25.9675, -201.7327]; min: [-18.6841, -58.9234, -251.3427]; size: [82.8482, 84.8908, 49.61] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Intake: scan hashed, working copy, noise floor on the lug top pads, coverage map (C1-C6), feature list from mesh and both photos, band regime declared by the owner (baseline-skill plastic), scan-only.
2. Datum: lug top pads -> XY at z = 0; outer cup wall axis -> Z; 3-fold lug phase -> clock; tilt measured.
3. Measure: r-z and theta-z maps on the full-res scan, per-lug angular extents, line and cylinder fits (bore draft, lug underside edge, concave under-lug floors), photo-inferred plate interior; every value with source and rule in measure/params.json.
4. Rebuild: one revolved profile + revolved sectors per gap and per lug + three lug instances at 120 deg pitch + cut tools; build123d, one closed solid, all-analytic faces, datum- and scan-frame STEP.
5. Verify in a fresh agent: returned HALT because its own ICP did not converge (gate INVALID). The owner chose to take delivery as is; the verdict stays HALT.

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | cup outer-wall axis ∩ bayonet lug top plane | — | — |
| primary (plane) | bayonet lug top pads | 0.0405 / 0.0988 | three moulded bayonet lug pads, coplanar and square to the cup axis; they carry the portafilter bayonet (function) and are the cleanest flat that is square to the axis (the floor plate is tilted/warped ~0.3 deg vs the axis, see INTAKE_CARD) |
| secondary (axis) | outer cup wall faces | 0.0572 / 0.5252 | cup outer cylinder = portafilter/bayonet rotation axis; cleanest cylinder (round within +-0.09 over the ~270 deg the scan covers) |
| clock | fourier_mass: bayonet lug 1 centre -> +X (angle 34.7586°) | — | — |

Measured tilt: 0.2046° (common slope, per-feature intercept, 8 stations over 1 feature(s), z -23.500..-2.500 vs frame Z). Scale factor applied: 1. Scan noise floor: 0.0405 mm (rms of RANSAC+SVD plane on lugtop (2529 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
 0.666850  -0.706995   0.235519   26.633628
 0.738142   0.670054  -0.078575  -23.574393
-0.102259   0.226244   0.968688   212.963966
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: assumed 3, photo-inferred 15, scan 49 (total 67). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `BORE_DRAFT_DEG` | 0.645 | deg | 0.645 | keep-measured | scan | 0.0815 | no | measure/figures/misc_fits.json#bore_gap_line |
| `BORE_RECESS_R` | 37.379 | mm | 37.294..37.508 | keep-measured | scan | 0.1 | no | measure/figures/valley_fit.json#bore_recess |
| `BORE_R_Z0` | 37.074 | mm | 37.074 | keep-measured | scan | 0.0815 | yes | measure/figures/misc_fits.json#bore_gap_line |
| `BOSS_H` | 0.6 | mm | — | assumed | assumed | 0.5 | no | input/photos/1.webp |
| `BOSS_HOLE_D` | 3.4 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `BOSS_OD` | 8 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `BOSS_PCR` | 20 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `BOSS_PITCH_DEG` | 180 | deg | — | photo-inferred | photo-inferred | 10 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `BOSS_THETA_1` | 66 | deg | — | photo-inferred | photo-inferred | 10 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `CHANNEL_END_OFF_DEG` | 44.5 | deg | [43.5, 45, 45] | mean-of-n | scan | 0.5 | no | measure/figures/lugs.json#channel_floor |
| `CHANNEL_INNER_R` | 34.455 | mm | [34.436, 34.623, 34.305] | mean-of-n | scan | 0.16 | no | measure/figures/lugs.json#lugs |
| `CHANNEL_START_OFF_DEG` | 3.83 | deg | [4, 3, 4.5] | mean-of-n | scan | 0.5 | no | measure/figures/lugs.json#channel_floor |
| `CHANNEL_Z` | -2.911 | mm | -2.911 | keep-measured | scan | 0.0405 | no | measure/figures/levels.json#lug_channel |
| `FLOOR_Z` | -19.937 | mm | -19.937 | keep-measured | scan | 0.0405 | yes | measure/figures/instances.json#floor_z_p50 |
| `GROOVE_BOTTOM_Z` | -15.571 | mm | [-15.514, -15.577, -15.614, -15.578] | mean-of-n | scan | 0.2 | no | measure/figures/misc_fits.json#groove_lug |
| `GROOVE_R_IN` | 36.7 | mm | 36.6..36.8 | keep-measured | scan | 0.1 | no | measure/figures/misc_fits.json#groove_lug |
| `KEY_CENTRAL_R` | 13 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_A_REACH` | 23.5 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_A_THETA` | 133 | deg | — | photo-inferred | photo-inferred | 10 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_A_WIDTH` | 7.2 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_B_REACH` | 20.5 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_B_THETA` | 310 | deg | — | photo-inferred | photo-inferred | 10 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_B_WIDTH` | 10.5 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `LIP_LOWER_R` | 31.33 | mm | 31.307..31.362 | keep-measured | scan | 0.05 | no | measure/figures/rz_profile.json#lip_gap_r_vs_z |
| `LIP_LUG_R` | 30.74 | mm | 30.716..30.757 | keep-measured | scan | 0.05 | no | measure/figures/rz_profile.json#lip_lug_r_vs_z |
| `LIP_STEP_Z` | -17.9 | mm | -18.1..-17.75 | keep-measured | scan | 0.15 | no | measure/figures/rz_profile.json#lip_gap_r_vs_z |
| `LIP_UPPER_R` | 30.82 | mm | 30.742..30.936 | keep-measured | scan | 0.08 | no | measure/figures/rz_profile.json#lip_gap_r_vs_z |
| `LOWER_WALL_R_IN` | 37 | mm | — | assumed | assumed | 1 | no | intake/INTAKE_CARD.md#3 |
| `LUG1_START_DEG` | 336 | deg | 336 | keep-measured | scan | 0.25 | no | measure/figures/lugs.json#lug_top |
| `LUG_COUNT` | 3 | count | 3 | keep-measured | scan | 0 | no | measure/figures/count_lugs.json |
| `LUG_INNER_R` | 31.682 | mm | 31.682 | keep-measured | scan | 0.0487 | yes | measure/figures/instances.json#lug_inner_faces_circle |
| `LUG_PITCH_DEG` | 120 | deg | [120, 120, 120] | symmetry | scan | 0.25 | no | measure/figures/lugs.json#lug_top |
| `LUG_SPAN_DEG` | 54 | deg | [54, 53.5, 54] | symmetry | scan | 0.25 | no | measure/figures/lugs.json#lugs |
| `NOTCH1_START_OFF_DEG` | 5 | deg | [5, 5, 5] | mean-of-n | scan | 0.5 | no | measure/figures/lugs.json#rim_ledge_at_lip_radius |
| `NOTCH2_START_OFF_DEG` | 34.83 | deg | [35, 34.5, 35] | mean-of-n | scan | 0.5 | no | measure/figures/lugs.json#rim_ledge_at_lip_radius |
| `NOTCH_FLOOR_Z` | 2.515 | mm | [2.499, 2.55, 2.529, 2.526, 2.497, 2.492] | mean-of-n | scan | 0.03 | no | measure/figures/underside_notch.json#rim_notch_floor_z |
| `NOTCH_WIDTH_DEG` | 7.5 | deg | [7.5, 7.5, 7.5, 7.5, 7.5, 7.5] | mean-of-n | scan | 0.5 | no | measure/figures/lugs.json#rim_ledge_at_lip_radius |
| `PLATE_T` | 2.5 | mm | — | assumed | assumed | 1 | no | input/photos/1.webp |
| `POCKET_END_OFF_DEG` | 58.5 | deg | [58, 59] | mean-of-n | scan | 0.5 | no | measure/figures/lugs.json#pocket_inner_floor |
| `POCKET_INNER_RC` | [209, 217.8, 169.3] | mm | [209, 217.8, 169.3] | keep-measured | scan | 0.057 | no | measure/figures/valley_fit.json#pocket_inner |
| `POCKET_INNER_THETA_C` | [1.44, 121.63, 248.68] | deg | [1.44, 121.63, 248.68] | keep-measured | scan | 0.5 | no | measure/figures/valley_fit.json#pocket_inner |
| `POCKET_INNER_ZMIN` | [-16.808, -16.665, -16.794] | mm | [-16.808, -16.665, -16.794] | keep-measured | scan | 0.057 | no | measure/figures/valley_fit.json#pocket_inner |
| `POCKET_RISER_R` | 34.391 | mm | 34.391 | keep-measured | scan | 0.15 | no | measure/figures/misc_fits.json#pocket_riser_r |
| `POCKET_START_OFF_DEG` | -5 | deg | [-5.5, -5, -4.5] | mean-of-n | scan | 0.5 | no | measure/figures/lugs.json#pocket_inner_floor |
| `RAMP_START_OFF_DEG` | 41.84 | deg | 41.84 | keep-measured | scan | 1 | no | measure/figures/underside_notch.json |
| `RAMP_Z_AT_54` | -1.149 | mm | -1.149 | keep-measured | scan | 0.0941 | no | measure/figures/underside_notch.json#underside_ramp |
| `RIM_LEDGE_Z_AT_38p5` | 2.618 | mm | 2.618 | keep-measured | scan | 0.05 | no | measure/figures/misc_fits.json#rim_ledge_line_z_vs_r |
| `RIM_LEDGE_Z_AT_39p8` | 2.348 | mm | 2.348 | keep-measured | scan | 0.05 | no | measure/figures/misc_fits.json#rim_ledge_line_z_vs_r |
| `RIM_LIP_FILLET_R` | 0.3 | mm | 0.2..0.4 | keep-measured | scan | 0.1 | no | measure/figures/prof_rim.png |
| `RIM_LIP_OUTER_R` | 38.5 | mm | 38.422..38.72 | keep-measured | scan | 0.15 | no | measure/figures/misc_fits.json |
| `RIM_LIP_TOP_Z` | 3.298 | mm | 3.298 | keep-measured | scan | 0.0405 | no | measure/figures/levels.json#rim_lip_top |
| `RIM_OUTER_FILLET_R` | 0.4 | mm | 0.3..0.5 | keep-measured | scan | 0.1 | no | measure/figures/prof_rim.png |
| `SHELF_EDGE_FILLET_R` | [2.426, 2.483, 1.961] | mm | [2.426, 2.483, 1.961] | keep-measured | scan | 0.13 | no | measure/figures/valley_fit.json#shelf_edge |
| `SHELF_Z` | [-14.101, -13.44, -14.233] | mm | [-14.101, -13.44, -14.233] | keep-measured | scan | 0.0405 | no | measure/figures/instances.json#gaps |
| `SIDE_HOLE_D` | 6 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `SIDE_HOLE_R` | 20.8 | mm | — | photo-inferred | photo-inferred | 3 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `SIDE_HOLE_THETA` | 269 | deg | — | photo-inferred | photo-inferred | 10 | no | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `STOP_BOTTOM_Z` | -10.524 | mm | [-10.663, -10.338, -10.57] | mean-of-n | scan | 0.2 | no | measure/figures/lugs.json#lugs |
| `STOP_END_OFF_DEG` | 5.76 | deg | [5.2, 6.54, 5.54] | mean-of-n | scan | 0.5 | no | measure/figures/lugs.json#lugs |
| `STOP_ROOT_FILLET_R` | 1 | mm | 0.8..1.2 | keep-measured | scan | 0.2 | no | measure/figures/prof_stop_start.png |
| `UNDERSIDE_Z_AT_7` | -6.574 | mm | -6.574 | keep-measured | scan | 0.1105 | no | measure/figures/underside_notch.json#underside_shallow |
| `UNDERSIDE_Z_AT_RAMP` | -5.588 | mm | -5.588 | keep-measured | scan | 0.1105 | no | measure/figures/underside_notch.json#underside_shallow |
| `VALLEY_OUTER_RC` | [237.2, 209.8, 207.5] | mm | [237.2, 209.8, 207.5] | keep-measured | scan | 0.097 | no | measure/figures/valley_fit.json#outer_valley |
| `VALLEY_OUTER_THETA_C` | [2.14, 119.46, 250.61] | deg | [2.14, 119.46, 250.61] | keep-measured | scan | 0.5 | no | measure/figures/valley_fit.json#outer_valley |
| `VALLEY_OUTER_ZMIN` | [-15.267, -15.036, -15.085] | mm | [-15.267, -15.036, -15.085] | keep-measured | scan | 0.097 | no | measure/figures/valley_fit.json#outer_valley |
| `WALL_R_OUT` | 40.11 | mm | 40.067..40.156 | keep-measured | scan | 0.05 | yes | measure/figures/rz_profile.json#outer_wall_r_vs_z |
| `Z_BOTTOM` | -27.835 | mm | -27.835 | keep-measured | scan | 0.0405 | no | intake/alignment.json#bounds_aligned |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

| id | feature | params |
|---|---|---|
| F01 | revolved cup profile (outer wall, stepped rim, drafted bore, plate, lower wall) | [WALL_R_OUT, RIM_LIP_TOP_Z, BORE_R_Z0, BORE_DRAFT_DEG, FLOOR_Z, PLATE_T] |
| F02 | 3 gap sectors: shelf per gap + lip with fitted edge rounding | [SHELF_Z, SHELF_EDGE_FILLET_R, LIP_UPPER_R, LIP_LOWER_R] |
| F03 | 3 lug sectors cut by fitted concave cylinders (pocket floors) | [VALLEY_OUTER_ZMIN, POCKET_INNER_ZMIN, POCKET_RISER_R] |
| F04 | 3 bayonet lugs: stop block, two underside planes, channel | [LUG1_START_DEG, LUG_SPAN_DEG, LUG_INNER_R, STOP_END_OFF_DEG, RAMP_START_OFF_DEG] |
| F05 | 6 rim notches | [NOTCH1_START_OFF_DEG, NOTCH2_START_OFF_DEG, NOTCH_WIDTH_DEG] |
| F06 | bore recess + groove behind each lug | [BORE_RECESS_R, GROOVE_BOTTOM_Z] |
| F07 | plate keyhole, bosses, holes (photo-inferred) | [KEY_CENTRAL_R, BOSS_PCR, SIDE_HOLE_D] |

## 7. Tier-1 — caliper dims re-measured on the STEP

**Tier-1 not run: no caliper dimensions exist.** Every dimension is scan authority (or operator spec); see the source column in §5. Absent is not passed.

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), iterations 500/500, converged no, correction 0.9039° / 0.9887 mm.  
Unobservable CAD fraction: 0.0451.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 202623 | 0.5974 | 0.5284 | 0.9715 | 1.0827 | 1.8257 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 202623 | 0.5974 | 0.5284 | 0.9715 | 1.0827 | 1.8257 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 3.472 | 0.9215 | 8.9205 | 12.1459 | 15.6293 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 147863 | 0.7931 | 0.5727 | 1.5158 | 2.5999 | 4.5493 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 19098 | 3.502 | 0.9014 | 9.0083 | 12.2952 | 15.583 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.9715 max 1.8257 (n 202623) | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 9.0083 max 15.583 (n 19098) | FAIL |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| I1 lug inner faces | functional_interface | scan_to_cad | reported | reported | n 4228 · p95 0.5676 · max 1.1 | n 4228 · p95 0.5676 · max 1.1 | r ~31.7, 3 x 54 deg (INTAKE_CARD §4 I1) |
| I1 lug inner faces | functional_interface | cad_to_scan | reported | reported | n 7539 · p95 1.015 · max 1.5765 | n 6570 · p95 0.9845 · max 1.3887 | r ~31.7, 3 x 54 deg (INTAKE_CARD §4 I1) |
| I2 lug undersides (hidden) | interior | cad_to_scan | reported | reported | n 6677 · p95 2.9267 · max 3.7261 | n 0 | C4: hidden, not gateable (I2/F08) |
| I3 lug stops | functional_interface | scan_to_cad | reported | reported | n 4437 · p95 0.9352 · max 1.0616 | n 4437 · p95 0.9352 · max 1.0616 | theta_s .. theta_s+6.5, down to z -10.5 (I3/F07) |
| I3 lug stops | functional_interface | cad_to_scan | reported | reported | n 4996 · p95 2.8686 · max 4.1418 | n 3313 · p95 2.6763 · max 4.1418 | theta_s .. theta_s+6.5, down to z -10.5 (I3/F07) |
| I4 bore | functional_interface | scan_to_cad | reported | reported | n 12422 · p95 0.6655 · max 0.8789 | n 12422 · p95 0.6655 · max 0.8789 | r ~37.0 drafted, gap sectors (I4/F04) |
| I4 bore | functional_interface | cad_to_scan | reported | reported | n 24132 · p95 1.8674 · max 2.9993 | n 22295 · p95 1.0818 · max 2.9993 | r ~37.0 drafted, gap sectors (I4/F04) |
| I5 shelf and pockets | functional_interface | scan_to_cad | reported | reported | n 19888 · p95 0.8921 · max 1.4266 | n 19888 · p95 0.8921 · max 1.4266 | z -13.4 .. -16.6 (I5/F09/F10) |
| I5 shelf and pockets | functional_interface | cad_to_scan | reported | reported | n 15204 · p95 1.6531 · max 4.3709 | n 12561 · p95 0.9861 · max 4.3709 | z -13.4 .. -16.6 (I5/F09/F10) |
| I6 plate top | functional_interface | scan_to_cad | reported | reported | n 1296 · p95 0.3594 · max 0.3627 | n 1296 · p95 0.3594 · max 0.3627 | z ~ -19.94, scanned part r >= 24 (I6/F12) |
| I6 plate top | functional_interface | cad_to_scan | reported | reported | n 13394 · p95 2.6638 · max 4.9884 | n 4853 · p95 1.0255 · max 1.0691 | z ~ -19.94, scanned part r >= 24 (I6/F12) |
| band z -14 to -7 | region | scan_to_cad | reported | reported | n 29450 · p95 0.9411 · max 1.3583 | n 29450 · p95 0.9411 · max 1.3583 | — |
| band z -14 to -7 | region | cad_to_scan | reported | reported | n 44451 · p95 2.7554 · max 5.435 | n 32057 · p95 2.2935 · max 4.5493 | — |
| band z -20.3 to -14 | region | scan_to_cad | reported | reported | n 60887 · p95 0.9633 · max 1.5559 | n 60887 · p95 0.9633 · max 1.5559 | — |
| band z -20.3 to -14 | region | cad_to_scan | reported | reported | n 78095 · p95 8.8793 · max 15.5302 | n 40614 · p95 1.058 · max 4.3709 | — |
| band z -7 to 0.1 | region | scan_to_cad | reported | reported | n 52865 · p95 0.9745 · max 1.8257 | n 52865 · p95 0.9745 · max 1.8257 | — |
| band z -7 to 0.1 | region | cad_to_scan | reported | reported | n 59752 · p95 2.5776 · max 4.3801 | n 41067 · p95 1.1031 · max 3.694 | — |
| below z -20.3 | region | scan_to_cad | reported | reported | n 25948 · p95 1.0028 · max 1.136 | n 25948 · p95 1.0028 · max 1.136 | — |
| below z -20.3 | region | cad_to_scan | reported | reported | n 92833 · p95 10.8501 · max 15.6293 | n 12017 · p95 0.9538 · max 0.996 | — |
| outer wall C6 sector | region | scan_to_cad | reported | reported | n 3510 · p95 0.791 · max 1.0521 | n 3510 · p95 0.791 · max 1.0521 | — |
| outer wall C6 sector | region | cad_to_scan | reported | reported | n 29865 · p95 10.3364 · max 12.2952 | n 0 | — |
| outer wall scanned sectors | region | scan_to_cad | reported | reported | n 34017 · p95 0.5786 · max 0.8593 | n 34017 · p95 0.5786 · max 0.8593 | — |
| outer wall scanned sectors | region | cad_to_scan | reported | reported | n 63325 · p95 0.9522 · max 3.6964 | n 57943 · p95 0.9152 · max 1.2801 | — |
| rim z above 0.1 | region | scan_to_cad | reported | reported | n 33473 · p95 0.9485 · max 1.1198 | n 33473 · p95 0.9485 · max 1.1198 | — |
| rim z above 0.1 | region | cad_to_scan | reported | reported | n 24869 · p95 1.1711 · max 2.0259 | n 22108 · p95 1.1133 · max 1.4295 | — |

### Masks (masked and unmasked are both shown above)

| mask | direction | why | fraction removed | stats inside |
|---|---|---|---|---|
| M1 C1 downward-facing CAD | cad_to_scan | the scan has almost no downward-facing surface (scanned from above): CAD faces facing down (lug undersides, plate underside, bottom closure) have no scan behind them; their CAD->scan distance is a coverage fact, not a surface deviation | 0.1968 | n: 59054; rms: 4.8012; mean: 3.8004; p50: 2.7834; p95: 10.689; p99: 12.8238; max: 15.6293 |
| M2 C2 below plate top inside wall | cad_to_scan | no scan exists inside the outer wall below the plate top: the plate underside, the assumed lower inner wall and the closure at the scan extent are assumed geometry (MODELING_PLAN §6) with nothing to compare against | 0.2288 | n: 68635; rms: 5.3438; mean: 4.3806; p50: 3.2999; p95: 11.0367; p99: 13.8621; max: 15.6293 |
| M3 C3 plate interior | cad_to_scan | the plate inside r ~24 is not in the scan; the keyhole, bosses and side hole there are photo-inferred, so no scan distance is meaningful | 0.1026 | n: 30766; rms: 7.8478; mean: 6.9697; p50: 6.648; p95: 13.2332; p99: 14.9149; max: 15.6293 |
| M4 C6 outer wall unscanned sector | cad_to_scan | the outer cup wall is not scanned at all over this sector (cup joined to the machine housing there, photos 1-2); the CAD continues the cylinder (assumed) with no scan behind it | 0.0995 | n: 29865; rms: 4.8055; mean: 3.8087; p50: 2.4398; p95: 10.3364; p99: 11.6965; max: 12.2952 |
| M5 open boundary | cad_to_scan | distance from CAD to a scan hole EDGE is not a surface deviation (the scan is open: 5,151 boundary edges / 16 loops) | 0.3465 | n: 103951; rms: 5.0329; mean: 3.708; p50: 2.4924; p95: 11.0969; p99: 13.7657; max: 15.6293 |

### Mask sensitivity

| band | direction | stats | variant |
|---|---|---|---|
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.6484; max_over_by: 3.7493 | cad_to_scan | n: 151442; rms: 0.8327; mean: 0.6491; p50: 0.5806; p95: 1.9484; p99: 2.6945; max: 4.5493 | all masks except M1 C1 downward-facing CAD |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 2.1666; max_over_by: 8.2899 | cad_to_scan | n: 157366; rms: 1.244; mean: 0.8013; p50: 0.6033; p95: 2.4666; p99: 6.033; max: 9.0899 | all masks except M2 C2 below plate top inside wall |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.2146; max_over_by: 3.7493 | cad_to_scan | n: 147868; rms: 0.7931; mean: 0.6258; p50: 0.5727; p95: 1.5146; p99: 2.5999; max: 4.5493 | all masks except M3 C3 plate interior |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 2.5969; max_over_by: 11.3935 | cad_to_scan | n: 167472; rms: 1.859; mean: 1.0241; p50: 0.6313; p95: 2.8969; p99: 9.4647; max: 12.1935 | all masks except M4 C6 outer wall unscanned sector |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.7386; max_over_by: 4.1884 | cad_to_scan | n: 178711; rms: 0.9202; mean: 0.7068; p50: 0.6089; p95: 2.0386; p99: 2.9675; max: 4.9884 | all masks except M5 open boundary |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.5649; max_over_by: 4.1231 | cad_to_scan | n: 168221; rms: 0.8257; mean: 0.6485; p50: 0.5835; p95: 1.8649; p99: 2.6907; max: 4.9231 | M5 open boundary radius 0.0 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.2012; max_over_by: 4.1069 | cad_to_scan | n: 157549; rms: 0.7976; mean: 0.6278; p50: 0.5709; p95: 1.5012; p99: 2.6265; max: 4.9069 | M5 open boundary radius 0.2 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.0957; max_over_by: 3.7493 | cad_to_scan | n: 153665; rms: 0.7942; mean: 0.6255; p50: 0.5704; p95: 1.3957; p99: 2.6163; max: 4.5493 | M5 open boundary radius 0.4 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.2158; max_over_by: 3.7493 | cad_to_scan | n: 147863; rms: 0.7931; mean: 0.6258; p50: 0.5727; p95: 1.5158; p99: 2.5999; max: 4.5493 | M5 open boundary radius 0.8 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.5457; max_over_by: 3.5709 | cad_to_scan | n: 136501; rms: 0.7872; mean: 0.6233; p50: 0.5732; p95: 1.8457; p99: 2.5668; max: 4.3709 | M5 open boundary radius 1.5 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.6222; max_over_by: 3.5709 | cad_to_scan | n: 119016; rms: 0.801; mean: 0.6294; p50: 0.5769; p95: 1.9222; p99: 2.5835; max: 4.3709 | M5 open boundary radius 2.5 mm |

### Over-band point clusters, scan → CAD (> 0.8 mm)

39959 points (0.1972 fraction) in 35 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 6860 | [6.818, -37.574, -16.935] | [39.102, 39.31] | [248.6, 307] | 1.0074 | outer wall theta 249-307, z ~-17: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 1 | 6794 | [1.947, 35.684, -6.955] | [37.053, 38.419] | [35.5, 132] | 1.316 | bore/rim theta 35-132: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 2 | 5580 | [9.297, -21.995, -20.877] | [23.077, 30.685] | [223.4, 337.7] | 1.136 | lip ring / plate edge theta 223-338: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 3 | 3535 | [-15.293, -29.739, -2.887] | [32.484, 36.552] | [217.3, 267.6] | 1.4632 | lug-3 top and channel theta 217-268: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 4 | 2916 | [-3.919, -29.916, 1.566] | [37.889, 39.308] | [183.8, 329.4] | 1.1198 | rim theta 184-329: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 5 | 2093 | [-13.264, -26.429, -4.372] | [30.55, 36.258] | [214.4, 272.5] | 1.8257 | lug-3 inner/channel theta 214-273: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 6 | 1780 | [-25.742, -17.864, -15.81] | [31.539, 36.778] | [170.3, 264.2] | 1.2313 | shelf/pockets theta 170-264: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 7 | 1727 | [-4.817, 28.193, -17.39] | [31.54, 32.865] | [49.9, 146.2] | 1.1855 | lip ring theta 50-146: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 8 | 1370 | [21.152, -25.89, -15.105] | [32.244, 36.461] | [284.5, 329.9] | 1.0813 | shelf/pockets theta 284-330: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 9 | 1032 | [9.428, 30.299, -19.674] | [32.021, 32.405] | [51.6, 90.2] | 1.0778 | lip ring theta 52-90: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 10 | 955 | [-10.96, 30.327, -3.209] | [32.481, 32.714] | [97.4, 130.4] | 1.0333 | lug-2 inner face theta 97-130: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |
| 11 | 804 | [-16.59, 34.307, -13.886] | [38.176, 38.436] | [105.4, 127] | 1.0575 | bore theta 105-127 z ~-14: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878). |

### Over-band point clusters, CAD → scan (> 0.8 mm)

170059 points (0.5669 fraction) in 27 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 134102 | [-1.83, 3.315, -19.393] | [12.999, 40.11] | [0, 360] | 15.6293 | **UNEXPLAINED** |
| 1 | 9353 | [-7.062, 33.214, -5.64] | [32.91, 37.66] | [55.1, 148.6] | 4.6667 | **UNEXPLAINED** |
| 2 | 8292 | [6.286, -38.468, -17.882] | [39.941, 40.11] | [247.9, 307.1] | 0.996 | **UNEXPLAINED** |
| 3 | 4613 | [34.894, 1.251, -7.727] | [32.183, 37.379] | [0, 360] | 3.1427 | **UNEXPLAINED** |
| 4 | 4378 | [-3.486, -31.079, 2.619] | [37.099, 40.11] | [186.8, 334.3] | 1.4206 | **UNEXPLAINED** |
| 5 | 2595 | [-5.687, 27.072, -17.42] | [29.62, 32.539] | [52, 154.5] | 1.4958 | **UNEXPLAINED** |
| 6 | 1876 | [-14.225, -29.697, -0.844] | [31.68, 37.051] | [216, 270] | 1.5813 | **UNEXPLAINED** |
| 7 | 1664 | [-11.349, 28.843, -3.237] | [31.679, 34.084] | [96, 150] | 1.2592 | **UNEXPLAINED** |
| 8 | 803 | [-16.551, 29.621, -2.408] | [34.452, 36.691] | [99.8, 140.5] | 2.0339 | **UNEXPLAINED** |
| 9 | 701 | [-16.424, 28.916, -15.189] | [34.389, 35.054] | [92.6, 150.9] | 1.3569 | **UNEXPLAINED** |
| 10 | 328 | [31.003, -13.801, -7.612] | [31.681, 36.225] | [336, 336.2] | 0.9985 | **UNEXPLAINED** |
| 11 | 245 | [-30.411, 11.795, -13.76] | [30.883, 34.391] | [154.5, 167.9] | 1.2583 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 1.8901°, origin offset 0.0049 mm, point disagreement p95 1.3257 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (OUTSIDE).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| whole part scan->CAD (datum frame, inspection only) | p95 0.244 passes; max 0.878 > 0.80 from 6 points (no cluster >= 20) at the lug-3 end, theta 270.7, r 33.4-34.3, z -1.7 (overlay panel theta 270.7 shows a thin scan trace past the modelled lug end); lugs are one instance copied at 120 deg pitch. | measure the lug-3 end angle on the scan and model per-instance lug spans, or declare it as edge fuzz with photo evidence |
| CAD->scan observable (both frames) | coverage, not geometry: unscanned CAD surfaces the ray test calls observable (C6 outer wall sector, C4 bore behind the lugs, cavity below the plate) -- datum frame observable p95 9.31 / max 14.61; masked (M1-M5) p95 0.357 / max 5.13, residual dominated by the hidden bore behind the lugs (r 36.4-37.7, z -14..-3.5, lug sectors). | more scan coverage, or a human decision to grade CAD->scan on the scanned region only; geometry changes cannot fix it |
| post-ICP gate (INVALID) | unconverged, contaminated ICP pose shifts the scan ~0.9 mm; every post-ICP band misses for this reason (scan->CAD p95 0.97 / max 1.83). | see L3 |

Missed band(s): `scan_to_cad:masked: p95 0.971 max 1.826 vs 0.3/0.8`; `cad_to_scan_observable: p95 9.008 max 15.583 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | no Tier-1 reading, so no Tier-1 miss to attribute |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | finding | QA grading is independent: own ICP (not written back), own datum audit, no expected value from this scan (Tier-1 has none). Finding on the builder record: MODELING_PLAN §8 iterated geometry against its own scan self-check (NOT QA) to max 0.761 -- a consistency check, not independent evidence; QA's datum-frame max on the full-res scan is 0.878. The intake noise floor was measured on the same lug pads that set the primary datum (INTAKE_CARD §6, self-referential). |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 12 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | finding | intake F01-F17 ticked against CAD, overlays and photos 1-2: F01-F12 present and track the scan in the overlays; F13-F15 keyhole, 2 bosses with holes, side hole present (photo-inferred, no scan); dimples not modelled (cosmetic, declared); F16 flange not modelled (outside scan, declared); F17 simplified in gap sectors (declared). No CAD feature lacks photo/scan support. Finding: photo 1 shows a small rectangular window at the base of the outer cup wall (front right, at the flange junction) that the intake list does not enumerate; the scan has no evidence of it (outer-wall coverage tapers at the ragged lower scan edge z -27.8..-24, no scan->CAD cluster), and it is not modelled. |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | pass | build/export_check.json: 7 fillets (6 fillet_2d profile + F04b 3D stop-root R1.0), every status OK, target == used, both frames |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | fresh agent; see independence |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | n/a | first QA run (it1); no superseded qa/. Builder self-check numbers (MODELING_PLAN §8) use a different protocol and are not compared as an improvement. |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | pass | no pass depends on a mask |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | pass | census: 182 faces, 100 % analytic area (plane 98, cylinder 57, cone 8, torus 19), no B-spline/ruled faces; model.py grep: no loft/ruled; Wire.make_polygon used only for parameter-driven (r,z) revolve profiles of 4-~20 named points, not stacks of scan slices; matches MODELING_PLAN (revolve/split/boolean only) |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | pass | photos 1 (3/4 view) and 2 (top view) walked: 3 lugs with L-shaped top channels and stops, 6 rim notches, shelf + pocket arcs, lip ring, plate with two-lobed keyhole, 2 screw bosses, bright through-hole, dimples -- CAD is plausible against both; see CHK-ENUM for the one unenumerated photo feature |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict HALT |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 3 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L0 | NO OFFICIAL GRADE. Verdict HALT: the independent ICP did not converge, so the full-res Tier-2 gate is INVALID. The numbers in this README are inspection-only: datum-frame scan to CAD p95 0.2435 / max 0.878 mm against the p95 0.3 / max 0.8 band. Delivered on the owner's explicit override, not because a gate passed. | tier2_icp.py fixed to exclude the declared CAD-side coverage regions and antiparallel-normal pairs -> re-run verify in a fresh agent | decisions/owner_override_2026-09-28.md; qa/gate.json#registration |
| L1 | Tier-1 not run (no calipers): tier1 partial, none of the requested dims measured; absent is not passed. | filled input/MEASUREMENTS.md with caliper readings -> re-run verify | qa/gate.json#tier1; intake/MEASUREMENTS.md |
| L2 | Absolute scale not caliper-verified (CHK-SCALE not run; units assumed mm). | one caliper reading of ENV-D (outer cup diameter) and ENV-Z2 -> re-run verify | intake/alignment.json#checks |
| L3 | Independent ICP did not converge (see verify's diagnosis): unscanned CAD faces pair with the opposite wall with antiparallel normals and pull the registration; the post-ICP numbers are biased and the datum-frame vs post-ICP scan_to_cad p95 differ by more than the band (datum finding reported by verify). | human decision on the registration protocol, e.g. an ICP that excludes the declared coverage regions -> re-run verify | qa/gate.json#auto_limitations: datum-frame vs post-ICP scan_to_cad p95 differ by 0.728 mm (> band 0.3 mm); qa/icp_diagnose.json |
| L4 | Coverage: the scan has no underside, no outer wall over theta 38-151 deg, nothing below the scan extent and no plate interior; the CAD surfaces there are not evidence-backed and the observable CAD to scan number is dominated by coverage, not geometry. | a scan with the C6 sector, the underside and the under-lug region covered -> re-run verify | intake/INTAKE_CARD.md#3; qa/gate.json#limitations L4 |
| L5 | Photo-inferred and assumed geometry is not graded: plate keyhole, bosses and side hole (photo-only), plate thickness, lower wall, lug undersides and stop radial depth (hidden). | caliper readings F-KEY, F-BOSS, F-PLATE, F-LUGT, F-STOP or a photo with a scale -> re-run verify | measure/params.json (photo-inferred / assumed rows) |
| L6 | Datum audit (report-only): axis and origin agree with the builder; the 3-fold Fourier clock differs by 1.8901 deg overall and is region-sensitive on this part. | a clock datum on a named flat face (e.g. a lug stop face) agreed with the owner -> re-run datum audit | qa/datum_audit.json; qa/datum_audit_clock_sens.json |
| L7 | Full resolution is an agent declaration, not an owner statement. | owner says the upload was decimated -> re-run verify on the original | DECISIONS.md OTHER 2026-09-28 |
| L8 | Unenumerated feature: photo 1 shows a small rectangular window at the base of the outer cup wall (flange junction), below the scanned region; it is not modelled. | a scan or caliper reading of the lower wall -> add the feature and re-run | qa/gate.json#checks.CHK-ENUM |
| L9 | Builder iterations inside it1 were steered by a builder self-check against the same scan (consistency check, not independent evidence); the independent datum-frame number is the one quoted above. | a converged independent ICP gate -> quote only the official numbers | build/MODELING_PLAN.md#8; qa/gate.json#checks.CHK-CIRCULAR |

## 12. Assumptions and invented geometry

Parameters not measured on the scan or by caliper (source tag from `measure/params.json`):

| parameter | value | source | evidence |
|---|---|---|---|
| `BOSS_H` | 0.6 | assumed | input/photos/1.webp |
| `BOSS_HOLE_D` | 3.4 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `BOSS_OD` | 8 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `BOSS_PCR` | 20 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `BOSS_PITCH_DEG` | 180 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `BOSS_THETA_1` | 66 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_CENTRAL_R` | 13 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_A_REACH` | 23.5 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_A_THETA` | 133 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_A_WIDTH` | 7.2 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_B_REACH` | 20.5 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_B_THETA` | 310 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `KEY_LOBE_B_WIDTH` | 10.5 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `LOWER_WALL_R_IN` | 37 | assumed | intake/INTAKE_CARD.md#3 |
| `PLATE_T` | 2.5 | assumed | input/photos/1.webp |
| `SIDE_HOLE_D` | 6 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `SIDE_HOLE_R` | 20.8 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |
| `SIDE_HOLE_THETA` | 269 | photo-inferred | input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching |

- The inner stepped ring (shelf, pockets, lip) is modelled as part of the one solid; it may be a separate rubber gasket. _(source: assumed; intake/INTAKE_CARD.md#8)_
- Outer wall continues as the same cylinder over the unscanned sector; the solid is closed by a flat face at the scan extent (not a real face). _(source: assumed; measure/params.json#Z_BOTTOM)_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** Anything that needs an official deviation grade: the gate is INVALID (HALT).
- **Not fit for:** Manufacture, tooling or fit-critical use (bayonet engagement): scale and all dimensions are uncalipered; lug undersides, stop depth, plate underside and everything below the plate are assumed; the plate keyhole, bosses and holes are photo-inferred.
- **Not fit for:** Evidence of the outer wall over theta 38-151 deg or below the scan extent (unscanned).
- Fit for: A design-intent parametric starting model (build/model.py + measure/params.json) to be refined with calipers and a fuller scan.
- Fit for: Visual and packaging studies of the scanned upper cup region.
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): No official Tier-2 grade: the QA registration did not converge, so the full-res gate is INVALID; datum-frame numbers are inspection only. Not fit for manufacture, tooling or fit-critical use (bayonet engagement): scale and all dimensions are uncalipered, the lug undersides/ramps, stop depth, plate underside and everything below the plate are assumed, and the plate keyhole/bosses/holes are photo-inferred. Not evidence of the outer wall over theta 37-152 or below z -27.84 (unscanned).

## 14. Reproduction

```
cd build && python3 model.py --params ../measure/params.json --alignment ../intake/alignment.json --out . --part OD-G10_porta_filter_holder --scripts <skills>/stl-re-rebuild-build123d/scripts
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-G10_porta_filter_holder.step | 40425.3755 | 0 | 0 | yes | yes | no |
| OD-G10_porta_filter_holder_datum.step | 40425.3755 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 15. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | a415ac1263b6cb0d8e020fb40ff6403ab5c9500502a4f744a9a417edad758a84 |
| `measure/params.json` | 3ff6ce4d12f11b7d9c79677371f500410d1acc882ccf89fa9789575a79262710 |
| `build/export_check.json` | 3f4018b1b86969ac2aa9a8c0fbd9142f0c3673879fbeed15f90bc91d2bce02f1 |
| `intake/alignment.json` | f17c3c04898f9354b69f4699e22944fb9dfbbfb40c0480315c6a0fa3d13608c4 |
| `deliver/repro.json` | 27bcb715c047984ea0d76cc4f131e1d320ba96d9e040c47f4fb9c5a91dafbd6b |
| `deliver/limitations.json` | 21eb22f8fe17d7f156b0813abeeffdfbe228cf2f7d576b15f8abe4727b36dbe2 |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
