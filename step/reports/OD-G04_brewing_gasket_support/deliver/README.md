# OD-G04_brewing-gasket-support — STL → STEP reverse-engineering delivery

**Verdict: `BAND_NOT_MET`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 1 of 3 (earlier iterations kept: none).  
**Verification independence (CHK-INDEP):** pass — fresh agent context; own scripts; builder numbers not used  

> **A deviation band was NOT met.** Delivered only under the recorded human acceptance below (by Ikbal (owner, decision card), 2026-09-25, record `decisions/accept_band.md`).

## 1. The part

![reference photo](../input/photos/1.png)

Brew-group gasket support disc: a moulded plastic cup with a flat back face, back bead and conical centre recess; on the front a stepped hub tube, six radial ribs, two ring-rib arcs, four screw bosses and two boss webs; an outer flange with a beaded gasket lip and three bayonet tabs at equal pitch.

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-G04_brewing-gasket-support_datum.step` | datum | 1 | yes | yes | 174 | 17086.2442 | max: [34.52, 34.52, 1.09]; min: [-31.1763, -34.48, -16.12]; size: [65.6963, 69, 17.21] |
| `build/OD-G04_brewing-gasket-support.step` | scan | 1 | yes | yes | 174 | 17086.2442 | max: [11.7015, 20.6811, -190.8562]; min: [-56.2304, -29.8851, -238.1192]; size: [67.9319, 50.5662, 47.263] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Intake: hashed the full-resolution scan, decimated a working copy, and aligned it to a datum frame (plate back face = z 0, cup outer wall axis = +Z, bayonet tab 1 toward +X).
2. Measure: derived every parameter from the scan (scan-only, no calipers; four catalogue photos for feature identification), with probe scripts and figures kept in measure/figures.
3. Build: build123d model.py built one revolve profile plus tabs, ribs, ring arcs, bosses, webs and cut tools from params.json and exported datum-frame and scan-frame STEP.
4. Verify: an independent agent re-registered the scan by its own ICP and graded two-way full-resolution deviation against the baseline-skill plastic band.
5. Deliver: packaged the owner-accepted BAND_NOT_MET result with a fresh-process reproducibility check and a delivery zip.

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | cup outer wall axis ∩ plate back face plane | — | — |
| primary (plane) | plate back face (flat outer face of the support disc) | 0.0489 / 0.1097 | largest clean moulded flat; the back face that seats against the brew-group piston/gasket stack, all features stand off it |
| secondary (axis) | outer cylindrical wall of the support cup (R~22.9, ~270 deg scanned) | 0.0198 / 3.0729 |  |
| clock | fourier_mass: 3 bayonet tabs on the outer rim (angle -6.8266°) | — | — |

Measured tilt: 0.277° (common slope, per-feature intercept, 4 stations over 1 feature(s), z -5.281..-2.469 vs frame Z). Scale factor applied: 1. Scan noise floor: 0.0489 mm (rms of RANSAC+SVD plane on plate back face (flat outer face of the support disc, R<19) (9868 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
 0.814965  -0.338986  -0.470021  -84.615798
 0.557588   0.679655   0.476618   118.365353
 0.157885  -0.650505   0.742910   150.286705
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: photo-inferred 1, scan 66 (total 67). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `bead_R_in` | 20.33 | mm | 20.333 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#bead inner wall |
| `bead_R_out` | 21.47 | mm | 21.469 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#bead outer wall |
| `bead_top_z` | 1.09 | mm | 1.091 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#back bead top; probe_p14.txt#bead top |
| `bossA_bot_z` | -16.12 | mm | [-16.107, -16.174, -16.066, -16.143] | mean-of-n | scan | 0.05 | no | measure/figures/probe_p6.txt |
| `bossA_r` | 15.5 | mm | [15.455, 15.545] | mean-of-n | scan | 0.05 | no | measure/figures/probe_p6.txt |
| `bossA_theta_deg` | [-6.55, 172.95] | deg | [-6.55, 172.95] | keep-measured | scan | 0.1 | no | measure/figures/probe_p6.txt |
| `bossB_bot_z` | -14.88 | mm | [-14.844, -14.824, -14.937, -14.916] | mean-of-n | scan | 0.05 | no | measure/figures/probe_p6.txt |
| `bossB_r` | 19.03 | mm | [18.96, 19.09] | mean-of-n | scan | 0.05 | no | measure/figures/probe_p6.txt |
| `bossB_theta_deg` | [113.27, -62.02] | deg | [113.27, -62.02] | keep-measured | scan | 0.1 | no | measure/figures/probe_p6.txt |
| `boss_R_out` | 3.49 | mm | [3.494, 3.489, 3.491, 3.504, 3.488, 3.482, 3.475, 3.493] | mean-of-n | scan | 0.01 | no | measure/figures/probe_p6.txt |
| `boss_cb_depth` | 1 | mm | 0.9..1.1 | keep-measured | scan | 0.25 | no | measure/figures/probe_p15.txt |
| `boss_cb_r` | 2 | mm | [2.03, 2.01, 2, 2] | mean-of-n | scan | 0.05 | no | measure/figures/probe_p15.txt |
| `boss_hole_depth` | 2.75 | mm | 2.7..2.8 | keep-measured | scan | 0.15 | no | measure/figures/probe_p6.txt |
| `boss_hole_r` | 1.53 | mm | [1.52, 1.54, 1.55, 1.51] | mean-of-n | scan | 0.03 | no | measure/figures/probe_p15.txt |
| `centre_bore_r` | 1.3 | mm | 1.302 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p12.txt#centre bore wall |
| `centre_post_R_out` | 2.5 | mm | — | photo-inferred | photo-inferred | — | no | input/photos/1.png |
| `centre_post_bot_z` | -5.64 | mm | -5.64 | keep-measured | scan | 0.1 | no | measure/figures/probe_p2.txt#centre r<3.5 |
| `cone_R_top` | 4.7 | mm | 4.7 | keep-measured | scan | 0.05 | no | measure/figures/probe_p2.txt#cone fit |
| `cone_slope` | 0.924 | mm | 0.924 | keep-measured | scan | 0.02 | no | measure/figures/probe_p2.txt#cone fit |
| `cup_R_in` | 20.6 | mm | 20.598 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#cup inner wall |
| `cup_R_out` | 22.95 | mm | 22.952 | round-within-noise | scan | 0.0489 | yes | measure/figures/probe_p1.txt#cup outer wall |
| `flange_R_out` | 30.8 | mm | 30.796 | round-within-noise | scan | 0.0489 | yes | measure/figures/probe_p1.txt#lip outer wall below tabs |
| `flange_bot_z` | -13.12 | mm | -13.122 | round-within-noise | scan | 0.0489 | yes | measure/figures/probe_p1.txt#flange bottom |
| `flange_inner_round_R` | 2.65 | mm | 2.65 | keep-measured | scan | 0.18 | no | measure/figures/probe_p18.txt#constrained tangent-arc |
| `flange_lip_fillet_R` | 1.084 | mm | 1.084 | keep-measured | scan | 0.05 | no | measure/figures/probe_p18.txt#flange-lip inner fillet |
| `flange_outer_round_R` | 0.196 | mm | 0.196 | keep-measured | scan | 0.07 | no | measure/figures/probe_p14.txt#flange outer-bottom round |
| `flange_top_z` | -10.76 | mm | -10.755 | round-within-noise | scan | 0.0489 | yes | measure/figures/probe_p1.txt#flange top |
| `hub_bore_R_lower` | 8.38 | mm | 8.384 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p17.txt#hub bore lower; probe_p16.txt |
| `hub_bore_R_upper` | 7.81 | mm | 7.811 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p17.txt#hub bore upper; probe_p16.txt |
| `hub_bore_step_z` | -10.45 | mm | -10.445 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p17.txt#hub bore step face |
| `hub_ring_R_out` | 6.13 | mm | [6.116, 6.141] | mean-of-n | scan | 0.0489 | no | measure/figures/probe_p1.txt#hub ring outer wall; probe_p12.txt#slot inner wall |
| `hub_ring_top_z` | 0.94 | mm | 0.942 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#hub ring top |
| `hub_tube_R_out` | 10.03 | mm | 10.027 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p17.txt#hub tube outer all z |
| `hub_tube_bot_z` | -15.73 | mm | -15.73 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#hub tube bottom; probe_p14.txt#hub tube bottom U |
| `lip_R_in` | 29.32 | mm | 29.317 | round-within-noise | scan | 0.0489 | yes | measure/figures/probe_p1.txt#lip inner wall |
| `lip_bead_R` | 31.175 | mm | 31.175 | keep-measured | scan | 0.0489 | no | measure/figures/probe_p20.txt |
| `lip_bead_z` | -8.3 | mm | -8.4..-8.2 | keep-measured | scan | 0.1 | no | measure/figures/probe_p20.txt |
| `lip_bead_z_hi` | -7.6 | mm | -7.6 | keep-measured | scan | 0.1 | no | measure/figures/probe_p20.txt |
| `lip_bead_z_lo` | -9.1 | mm | -9.2..-9.0 | keep-measured | scan | 0.1 | no | measure/figures/probe_p20.txt |
| `lip_top_z` | -7.03 | mm | -7.034 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#lip top; probe_p14.txt#lip top |
| `plate_back_z` | 0 | mm | -0.02 | round-within-noise | scan | 0.0489 | yes | measure/figures/probe_p1.txt#plate back |
| `plate_edge_round_R` | 0.316 | mm | 0.316 | keep-measured | scan | 0.054 | no | measure/figures/probe_p14.txt#plate outer edge round |
| `plate_under_z` | -2.59 | mm | -2.589 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p2.txt#underside sector 0-95 |
| `rib_count` | 6 | count | 6 | keep-measured | scan | 0 | no | measure/figures/ribs_lines.json; count_ribs.json |
| `rib_phase_deg` | 22.9 | deg | [23.14, 22.76, 21.5, 22.86, 23.33, 23.86] | mean-of-n | scan | 0.3 | no | measure/figures/ribs_lines.json |
| `rib_pitch_deg` | 60 | deg | [59.62, 58.74, 61.36, 60.47, 60.53, 59.28] | symmetry | scan | 0.3 | no | measure/figures/ribs_lines.json |
| `rib_shallow_bot_z` | -10.68 | mm | -10.68 | keep-measured | scan | 0.05 | no | measure/figures/probe_p5.txt |
| `rib_step_r` | 14.55 | mm | [14.6, 14.47, 14.43, 14.46, 14.58, 14.67] | mean-of-n | scan | 0.1 | no | measure/figures/probe_p10.txt#deep bottom along r |
| `rib_t` | 1.35 | mm | [1.406, 1.309, 1.375, 1.392, 1.296, 1.321] | mean-of-n | scan | 0.05 | no | measure/figures/probe_p10.txt |
| `ring_rib_R_in` | 14.85 | mm | 14.853 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#ring rib inner |
| `ring_rib_R_out` | 16.09 | mm | 16.086 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#ring rib outer |
| `ring_rib_arcs_deg` | [26, 141, 205, 321] | deg | [26, 141, 205, 321] | keep-measured | scan | 0.3 | no | measure/figures/probe_p8b.txt |
| `ring_rib_bot_z` | -10.67 | mm | -10.671 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p1.txt#ring rib bottom |
| `slot_R_out` | 7.5 | mm | 7.501 | round-within-noise | scan | 0.0489 | no | measure/figures/probe_p12.txt#slot outer wall |
| `slot_count` | 4 | count | 4 | keep-measured | scan | 0 | no | measure/figures/probe_p13.txt |
| `slot_phase_deg` | -4.9 | deg | [-4.5, -3.5, -5.5, -6] | mean-of-n | scan | 1 | no | measure/figures/probe_p13.txt |
| `slot_span_deg` | 40.25 | deg | [41, 41, 39, 40] | mean-of-n | scan | 1 | no | measure/figures/probe_p13.txt |
| `tab_R_out` | 34.52 | mm | 34.519 | round-within-noise | scan | 0.0489 | yes | measure/figures/probe_p21.txt |
| `tab_bot_z` | -9.52 | mm | -9.524 | round-within-noise | scan | 0.0489 | yes | measure/figures/probe_p1.txt#tab bottom |
| `tab_count` | 3 | count | 3 | keep-measured | scan | 0 | yes | measure/figures/count_tabs.json |
| `tab_phase_deg` | -3.3 | deg | [-3.29, -3.22, -3.44] | mean-of-n | scan | 0.1 | no | measure/figures/probe_p8.txt#end faces |
| `tab_pitch_deg` | 120 | deg | [120.07, 119.78, 120.15] | symmetry | scan | 0.1 | no | measure/figures/probe_p8.txt#end faces |
| `tab_span_deg` | 61.08 | deg | [60.94, 61.2, 61.09] | mean-of-n | scan | 0.1 | no | measure/figures/probe_p8.txt#end faces |
| `tab_top_z` | -7.76 | mm | -7.761 | round-within-noise | scan | 0.0489 | yes | measure/figures/probe_p1.txt#tab top |
| `wall_flange_fillet_R` | 0.38 | mm | 0.38 | keep-measured | scan | 0.06 | no | measure/figures/probe_p14.txt#wall-flange top fillet |
| `webA_bot_z` | -10.69 | mm | [-10.73, -10.654] | mean-of-n | scan | 0.05 | no | measure/figures/probe_p19.txt |
| `webA_t` | 1.18 | mm | [1.196, 1.159] | mean-of-n | scan | 0.05 | no | measure/figures/probe_p19.txt; probe_p22.txt |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

| id | feature | params |
|---|---|---|
| F01 | revolve profile: plate, bead, hub ring, cone, centre bore/post, stepped hub tube, cup wall, flange, lip | [plate_under_z, bead_R_in, cup_R_out, flange_bot_z, lip_R_in, hub_bore_R_upper] |
| F01b | lip outer bead | [lip_bead_R, lip_bead_z] |
| F02 | 3 bayonet tabs | [tab_R_out, tab_span_deg, tab_phase_deg] |
| F03 | 6 radial ribs (stepped bottom) | [rib_t, rib_phase_deg, rib_step_r] |
| F04 | 2 ring-rib arcs | [ring_rib_R_in, ring_rib_arcs_deg] |
| F05 | 4 screw bosses + 2 webs | [boss_R_out, bossA_theta_deg, bossB_theta_deg, webA_t] |
| F06 | cut: counterbored boss holes + 4 back slots | [boss_hole_r, boss_cb_r, slot_span_deg] |

## 7. Tier-1 — caliper dims re-measured on the STEP

**Tier-1 not run: no caliper dimensions exist.** Every dimension is scan authority (or operator spec); see the source column in §5. Absent is not passed.

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), iterations 200/300, converged yes, correction 0.337° / 0.3325 mm.  
Unobservable CAD fraction: 0.0624.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 245660 | 0.2005 | 0.1359 | 0.3756 | 0.4501 | 0.8316 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 245660 | 0.2005 | 0.1359 | 0.3756 | 0.4501 | 0.8316 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 1.0848 | 0.2413 | 2.5939 | 3.5552 | 4.8136 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 300000 | 1.0848 | 0.2413 | 2.5939 | 3.5552 | 4.8136 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 18753 | 0.9217 | 0.2193 | 2.3247 | 3.274 | 4.5923 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.3756 max 0.8316 (n 245660) | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 2.3247 max 4.5923 (n 18753) | FAIL |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| B1_zband_plate | region | scan_to_cad | reported | reported | n 46209 · p95 0.3603 · max 0.6257 | n 46209 · p95 0.3603 · max 0.6257 | — |
| B1_zband_plate | region | cad_to_scan | reported | reported | n 66836 · p95 2.3835 · max 2.873 | n 66836 · p95 2.3835 · max 2.873 | — |
| B2_zband_mid | region | scan_to_cad | reported | reported | n 116220 · p95 0.3587 · max 0.8316 | n 116220 · p95 0.3587 · max 0.8316 | — |
| B2_zband_mid | region | cad_to_scan | reported | reported | n 164577 · p95 3.0347 · max 4.8136 | n 164577 · p95 3.0347 · max 4.8136 | — |
| B3_zband_front | region | scan_to_cad | reported | reported | n 83231 · p95 0.4007 · max 0.8166 | n 83231 · p95 0.4007 · max 0.8166 | — |
| B3_zband_front | region | cad_to_scan | reported | reported | n 68587 · p95 0.4181 · max 1.3624 | n 68587 · p95 0.4181 · max 1.3624 | — |
| I1_hub_interior | interior | scan_to_cad | reported | reported | n 2054 · p95 0.2105 · max 0.3516 | n 2054 · p95 0.2105 · max 0.3516 | intake §3: hub interior unscanned except centre bore |
| I1_hub_interior | interior | cad_to_scan | reported | reported | n 1644 · p95 2.4265 · max 3.133 | n 1644 · p95 2.4265 · max 3.133 | intake §3: hub interior unscanned except centre bore |
| I2_plate_underside_unscanned_sectors | interior | scan_to_cad | reported | reported | n 0 | n 0 | intake §3: plate underside scanned only at theta 20-80 |
| I2_plate_underside_unscanned_sectors | interior | cad_to_scan | reported | reported | n 12326 · p95 2.5456 · max 2.8316 | n 12326 · p95 2.5456 · max 2.8316 | intake §3: plate underside scanned only at theta 20-80 |
| I3_outer_wall_gap | interior | scan_to_cad | reported | reported | n 3121 · p95 0.3202 · max 0.3594 | n 3121 · p95 0.3202 · max 0.3594 | intake §3: outer wall/flange-top scan gap theta -69..+27 (reported as a coverage region, not a mask) |
| I3_outer_wall_gap | interior | cad_to_scan | reported | reported | n 11141 · p95 3.8745 · max 4.8136 | n 11141 · p95 3.8745 · max 4.8136 | intake §3: outer wall/flange-top scan gap theta -69..+27 (reported as a coverage region, not a mask) |
| Z1_back_face_bead | functional_interface | scan_to_cad | reported | reported | n 32326 · p95 0.3663 · max 0.4297 | n 32326 · p95 0.3663 · max 0.4297 | plate back face + back bead (seats against brew-group stack) |
| Z1_back_face_bead | functional_interface | cad_to_scan | reported | reported | n 33406 · p95 0.3799 · max 1.0055 | n 33406 · p95 0.3799 · max 1.0055 | plate back face + back bead (seats against brew-group stack) |
| Z2_flange_lip | functional_interface | scan_to_cad | reported | reported | n 79465 · p95 0.3832 · max 0.5505 | n 79465 · p95 0.3832 · max 0.5505 | flange + gasket lip + lip bead (gasket seat) |
| Z2_flange_lip | functional_interface | cad_to_scan | reported | reported | n 79008 · p95 0.4609 · max 2.7607 | n 79008 · p95 0.4609 · max 2.7607 | flange + gasket lip + lip bead (gasket seat) |
| Z3_bayonet_tabs | functional_interface | scan_to_cad | reported | reported | n 20554 · p95 0.4192 · max 0.8316 | n 20554 · p95 0.4192 · max 0.8316 | 3 bayonet tabs (locking) |
| Z3_bayonet_tabs | functional_interface | cad_to_scan | reported | reported | n 15488 · p95 0.7269 · max 2.0949 | n 15488 · p95 0.7269 · max 2.0949 | 3 bayonet tabs (locking) |
| Z4_boss_holes | functional_interface | scan_to_cad | reported | reported | n 6804 · p95 0.3665 · max 0.5447 | n 6804 · p95 0.3665 · max 0.5447 | 4 screw bosses with counterbored holes, 4.6 mm boxes round each boss axis |
| Z4_boss_holes | functional_interface | cad_to_scan | reported | reported | n 3828 · p95 0.8537 · max 1.3624 | n 3828 · p95 0.8537 · max 1.3624 | 4 screw bosses with counterbored holes, 4.6 mm boxes round each boss axis |

### Masks (masked and unmasked are both shown above)

No masks were applied.

### Over-band point clusters, scan → CAD (> 0.8 mm)

3 points (0 fraction) in 0 clusters ≥ 20 pts.

### Over-band point clusters, CAD → scan (> 0.8 mm)

66525 points (0.2218 fraction) in 26 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 8399 | [19.03, -5.926, -6.368] | [22.948, 25.669] | [0, 360] | 4.8136 | **UNEXPLAINED** |
| 1 | 8359 | [0.028, 0.714, -4.008] | [1.3, 7.81] | [0.1, 360] | 4.0075 | **UNEXPLAINED** |
| 2 | 4906 | [14.653, -5.881, -4.764] | [10.029, 20.6] | [324.8, 351.8] | 4.4385 | **UNEXPLAINED** |
| 3 | 4853 | [-14.687, 6.413, -4.686] | [10.029, 20.6] | [144.8, 171.3] | 3.8358 | **UNEXPLAINED** |
| 4 | 4769 | [-15.529, -2.364, -4.674] | [10.029, 20.6] | [174.6, 201] | 4.0779 | **UNEXPLAINED** |
| 5 | 4742 | [15.786, 2.758, -4.711] | [10.029, 20.6] | [0, 360] | 4.531 | **UNEXPLAINED** |
| 6 | 4285 | [-4.93, 11.348, -4.59] | [10.029, 14.85] | [85.5, 140.3] | 4.6886 | **UNEXPLAINED** |
| 7 | 4247 | [5.017, -11.379, -4.603] | [10.029, 14.85] | [265.5, 320.3] | 4.6336 | **UNEXPLAINED** |
| 8 | 4102 | [-10.164, -13.825, -3.77] | [16.089, 20.6] | [204.8, 261] | 3.7684 | **UNEXPLAINED** |
| 9 | 3242 | [-7.104, -10.047, -3.968] | [10.029, 14.85] | [205.5, 260.3] | 3.7949 | **UNEXPLAINED** |
| 10 | 2674 | [2.408, -17.826, -4.302] | [16.089, 20.6] | [264.8, 291.8] | 4.0403 | **UNEXPLAINED** |
| 11 | 2666 | [-1.667, 18.259, -4.586] | [16.089, 20.6] | [84.8, 107.1] | 3.882 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 1.3095°, origin offset 0.0311 mm, point disagreement p95 0.7523 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (OUTSIDE).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| whole part scan->CAD p95 (0.376 vs 0.30) | registration, not geometry: default QA ICP matched CAD faces to the opposite skin across 2.3-2.6 mm walls (sign-free normal test, 3 mm correspondence) and shifted the CAD 0.29 mm in z; even the flat back face Z1 reads p95 0.366 post-ICP vs 0.146 in the builder datum frame. Datum frame p95 0.218 and diagnostic ICP (max_corr 1.0) p95 0.194 both pass. | accept on the datum-frame/diagnostic evidence (human ACCEPT-BAND), or re-grade after a skill-level decision on ICP correspondence distance |
| whole part scan->CAD max (0.832 vs 0.80) | 3 isolated scan points of 245,660 (no cluster >=20): one on a bayonet-tab end corner r 35.35 theta 257.6 z -8.55 (scan extends ~0.8 mm beyond the CAD tab radius 34.52 locally), two at r 21.6 theta 263 z -13.5 at the cup-wall/flange root. Persists in every frame (datum 0.833, diagnostic 0.857). | REVISE tab end/root geometry locally (small), or accept as scan edge fuzz; a caliper reading of tab outer radius would arbitrate |
| CAD->scan observable (p95 2.325 / max 4.592 vs 0.30/0.80) | coverage: the front cavity (plate underside outside 20-80 deg, rib sides, cup inner wall, hub interior) and the outer wall gap theta -69..+27 were not scanned (INTAKE_CARD §3); the ray test counts them as observable. Where the scan exists it overlays the CAD (overlays). Not fixable by geometry. | rescan the front cavity/outer wall, or calipers on plate thickness, rib heights and wall thickness; or human acceptance of the unscanned-region extrapolation |

Missed band(s): `scan_to_cad:masked: p95 0.376 max 0.832 vs 0.3/0.8`; `cad_to_scan_observable: p95 2.325 max 4.592 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | Tier-1 not run (no calipers) |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | finding | QA gate independent: own ICP (T_refine QA-only, not written back), no expected values used. Finding: the builder's plan-change loop used a scan->CAD self-comparison on 100k samples (MODELING_PLAN §0) and every param is scan-derived (scan-only run) - that record is a consistency check, not independent evidence. |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 0 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | finding | intake E1-E13 all present in CAD and visible in overlays/photos (6 ribs, 2 ring arcs, 4 bosses, 2 webs, 3 tabs, hub tube, 4 back slots, centre post); nothing hallucinated. Finding: E14 moulded text and the ejector-pin dimples on the flange (photo 1) are not modelled (declared/cosmetic); no scan->CAD over-band cluster >=20 pts |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | pass | export_check fillets [] (no fillet ops); all rounds are tangent arcs in revolve profiles, declared in MODELING_PLAN §0/§5; rib/boss root fillets declared not modelled (not silent) |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | fresh agent context; own scripts; builder numbers not used |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | n/a | iteration 1; no _itN_SUPERSEDED to compare |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | pass | no pass depends on a mask |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | pass | QA census: 174 faces, analytic area 100% (plane 107, cylinder 54, torus 12, cone 1), 0 freeform; grep of build/model.py: no loft/ruled/polyline |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | pass | 4 catalogue photos walked: front (ribs, arcs, bosses, hub, tabs), back (plate, bead, conical recess, 4 slots, centre bore) and side views agree with CAD overlays; no scale reference |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict BAND_NOT_MET |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 5 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L1 | Tier-1 not run: no caliper sheet was supplied (scan-only run, DECISIONS.md MEASUREMENTS); no Tier-1 dimension is verified. | any caliper reading | qa/gate.json#limitations; qa/gate.json#auto_limitations: no Tier-1 (no calipers run); DECISIONS.md |
| L2 | Absolute scale not caliper-verified (CHK-SCALE not run; units assumed mm). | any caliper reading | qa/gate.json#limitations |
| L3 | The gated scan-to-CAD p95 (0.3756 mm) comes from the verifier's default ICP, which paired faces across the thin walls and shifted the CAD along z; the datum-frame grade and a diagnostic ICP with a tighter correspondence distance both stay inside the p95 band (qa/deviation_datum.json, qa/diagnostic/). The gate number is reported as graded. | a skill decision on the ICP correspondence distance for thin-walled parts, then re-run verify | qa/gate.json#limitations; qa/VERDICT.md 'Misses, per region' |
| L4 | CAD-to-scan observable miss (2.3247 / 4.5923 mm) is driven by surfaces the scanner never reached (front cavity: plate underside outside the scanned sector, rib sides, hub interior; outer-wall gap); the observability test counts them as observable. The model extrapolates those regions from the scanned ones. | a rescan covering the front cavity and the outer wall gap | qa/gate.json#limitations; intake/INTAKE_CARD.md section 3 |
| L5 | Verify ran the observability step through a call wrapper with a smaller ray chunk to avoid running out of memory (identical per-ray results; no skill script edited). | none needed unless the skill changes the ray engine | qa/gate.json#limitations |
| L6 | Scan-to-CAD max (0.8316 mm) is three isolated scan points (no cluster): one on a bayonet-tab end corner, two at the cup-wall/flange root. | a caliper reading of the across-tabs dimension | qa/VERDICT.md 'Misses, per region' |
| L7 | Centre post outer radius (2.5 mm) is photo-inferred; the plate underside is scanned only in one sector and assumed planar elsewhere at plate_under_z. | a caliper reading of plate thickness or the centre post | measure/params.json#centre_post_R_out, plate_under_z |
| L8 | Declared simplifications: equal tab heights (tab 1 measured lower), equal rib pitch (measured scatter kept in params), straight walls instead of mould draft, moulded text, ejector-pin marks and small rib/boss root fillets not modelled. | a functional fit issue on the tabs or a request for draft-exact geometry | measure/params.json#simplifications; qa/gate.json#checks.CHK-ENUM |
| L9 | The builder's own scan-to-CAD self-comparison that drove plan changes is a consistency check, not independent evidence (CHK-CIRCULAR); only the verifier's gate is evidence. | none; informative | qa/gate.json#checks.CHK-CIRCULAR; build/MODELING_PLAN.md section 0 |

## 12. Assumptions and invented geometry

Parameters not measured on the scan or by caliper (source tag from `measure/params.json`):

| parameter | value | source | evidence |
|---|---|---|---|
| `centre_post_R_out` | 2.5 | photo-inferred | input/photos/1.png |

- Plate underside outside the scanned sector assumed planar at the scanned level; hub interior between the centre post and the hub bore closed at the plate underside. _(source: assumed; build/MODELING_PLAN.md section 6)_
- Units are millimetres (no caliper check). _(source: assumed; DECISIONS.md MEASUREMENTS)_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** tooling, mould design or mating-interface manufacture until the tabs, flange, lip and plate thickness are calipered
- **Not fit for:** tolerance-grade inspection: Tier-1 was not run and the scale is unverified
- Fit for: form, visual and fit-check prototyping (e.g. 3D-printed replacement trials)
- Fit for: an editable parametric base: build/model.py driven by measure/params.json
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): Not a caliper-verified or tolerance-grade model: no Tier-1, scale unverified, front cavity and hub interior extrapolated from partial scan. Fit for form/visual and fit-check prototyping only; not for tooling or mating-interface manufacture until calipered.

## 14. Human acceptance of the band miss

Accepted by **Ikbal (owner, decision card)** on 2026-09-25 (`DECISIONS.md`, ACCEPT-BAND): Accept and deliver: accepts scan_to_cad and cad_to_scan_observable band misses, gate 6b2ca357f5c3 (created 2026-09-25T14:13:14+00:00). Record: `decisions/accept_band.md` (sha256 `98bda38043085b4348cbcbd4ce3bc9cd60026aef9e904c52032dbe493c456e0e`).

## 15. Reproduction

```
cd build && python3 model.py --params ../measure/params.json --alignment ../intake/alignment.json --out . --part OD-G04_brewing-gasket-support --scripts <path to stl-re-rebuild-build123d/scripts>
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-G04_brewing-gasket-support.step | 17086.2442 | 0 | 0 | yes | yes | no |
| OD-G04_brewing-gasket-support_datum.step | 17086.2442 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 16. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | 6b2ca357f5c3f5250851fb4a32c7ad769973adc8e708dc545300c514ccb2f006 |
| `measure/params.json` | 749756129bf812963194fcd622265cd0cf959683023aeb2aa3539d2f11881b9f |
| `build/export_check.json` | f35998dbd688a426188b5e83b6f420ff13f53e190f753b5fe1a1b0088912261d |
| `intake/alignment.json` | e3b7455c62cdb4f61ee56c503962bfd084c0cb5e0d1b30a623e4840f16bebe74 |
| `deliver/repro.json` | 808171a7b40d25eb4a414416625aee05a89ba9e4ae74a69bea4b80b6cc72aa52 |
| `deliver/limitations.json` | 47e336be163226e504160dbd5bb45c29d2ebf86ed5df3e146049109bb7e85815 |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
