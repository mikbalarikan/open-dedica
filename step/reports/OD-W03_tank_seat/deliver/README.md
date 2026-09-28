# OD-W03 — STL → STEP reverse-engineering delivery

**Verdict: `BAND_NOT_MET`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 1 of 3 (earlier iterations kept: none).  
**Verification independence (CHK-INDEP):** pass — fresh context; did not build the model  

> **A deviation band was NOT met.** Delivered only under the recorded human acceptance below (by Ikbal (owner, decision card), 2026-09-28, record `decisions/accept_band.md`).

## 1. The part

![reference photo](../input/photos/OD-W03_photo1.png)

Water tank valve cover (translucent moulded plastic): stadium flange with skirt, two valve cups with conical shoulders and single-barb hose nipples, a middle boss with a top hole, four ribs, and an L-shaped ear with a fixing hole at each end.

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-W03_datum.step` | datum | 1 | yes | yes | 106 | 6260.7716 | max: [42.408, 14.574, 28.312]; min: [-42.388, -14.858, -3.1]; size: [84.796, 29.432, 31.412] |
| `build/OD-W03.step` | scan | 1 | yes | yes | 106 | 6260.7716 | max: [37.2121, 9.8217, -180.3208]; min: [-29.1922, -54.4786, -222.9984]; size: [66.4043, 64.3004, 42.6776] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Intake: full-resolution scan (owner-confirmed), nothing removed; datum = flange top face (z = 0), origin = midpoint of the two cup axes, +X from cup A to cup B (align.py feature_line clock).
2. Measure: meridian profiles, binned-median line fits, IRLS circles and open-boundary loops on the aligned scan; per-cup and per-ear values kept where they differ beyond noise; tops re-measured as cones after a builder self-check.
3. Rebuild: build123d, revolved cup and boss meridians, stadium flange extrude, planar ribs, tapered tab prisms and slot lugs, one cut-tool set for the hollow shell (owner decision); 5 fillets logged, all at target.
4. Verify: independent agent, own ICP, two-way full-res deviation under regime baseline-skill; verdict BAND_NOT_MET, accepted by the owner.

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | midpoint of cup A and cup B axes ∩ flange top face | — | — |
| primary (plane) | flange top face (stadium plate top around the cups) | 0.0409 / 0.1026 | flange plate top: the plate's underside (not scanned) seats on the tank; the top is the largest clean moulded flat, parallel to it, and every cup, boss and ear rises from it |
| secondary (axis) | cup A outer wall (-X cup) + cup B outer wall (+X cup) | 0.0829 / 0.6564 | the two valve cups are the functional features; their axes define the pitch line. Band z 1.2-3.6 = the cleanest wall band (higher bands carry +/-0.15 mm scan ripple on the translucent wall) / second cup axis; origin = midpoint of the two cup axes (combine=midpoint) |
| clock | feature_line: cup A axis -> cup B axis along +X (angle 119.7623°) | — | — |

Measured tilt: 0.27° (common slope, per-feature intercept, 6 stations over 2 feature(s), z 1.600..3.200 vs frame Z). Scale factor applied: 1. Scan noise floor: 0.0409 mm (rms of RANSAC+SVD plane on flange top face (stadium plate top between/around the cups) (23812 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
-0.690088  -0.681052  -0.244839  -61.160043
 0.301585  -0.578144   0.758153   136.577919
-0.657894   0.449353   0.604365   142.204498
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: assumed 1, scan 44 (total 45). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `barb_bore_r` | 1.214 | mm | 1.214 | keep-measured | scan | 0.21 | no | measure/figures/m04_ears_webs.json#hole_loops.barbB |
| `barb_flare_z0` | [23.178, 23.012] | mm | [23.178, 23.012] | keep-measured | scan | 0.15 | no | measure/figures/m03_profile_fits.json#cup*.barb_flare_r_vs_z |
| `barb_lip_r` | [3.439, 3.419] | mm | [3.439, 3.419] | keep-measured | scan | 0.07 | yes | measure/figures/m03_profile_fits.json#cup*.lip_r_top50_median |
| `barb_lip_z` | [24.552, 24.482] | mm | [24.552, 24.482] | keep-measured | scan | 0.1 | no | measure/figures/m03_profile_fits.json#cup*.lip_z_at_rmax |
| `barb_shank_r` | [2.683, 2.549] | mm | [2.683, 2.549] | keep-measured | scan | 0.14 | yes | measure/figures/m03_profile_fits.json#cup*.shank_r_p50 |
| `barb_tip_r` | [2.871, 2.751] | mm | [2.871, 2.751] | keep-measured | scan | 0.12 | yes | measure/figures/m03_profile_fits.json#cup*.barb_taper_r_vs_z |
| `barb_top_z` | [28.271, 28.312] | mm | [28.271, 28.312] | keep-measured | scan | 0.05 | no | measure/figures/m03_profile_fits.json#cup*.barb_top_z_p50 |
| `boss_draft_deg` | 0.614 | deg | 0.614 | keep-measured | scan | 0.1 | no | measure/figures/m03_profile_fits.json#boss.wall_r_vs_z |
| `boss_hole_r` | 2.078 | mm | 2.078 | keep-measured | scan | 0.14 | no | measure/figures/m04_ears_webs.json#hole_loops.boss |
| `boss_r0` | 6.253 | mm | 6.253 | keep-measured | scan | 0.1 | no | measure/figures/m03_profile_fits.json#boss.wall_r_vs_z |
| `boss_top_round_r` | 0.378 | mm | 0.378 | keep-measured | scan | 0.17 | no | measure/figures/m03_profile_fits.json#boss.top_corner_round |
| `boss_top_slope_deg` | 3.715 | deg | 3.715 | keep-measured | scan | 0.03 | no | measure/figures/m08_top_annulus.json#boss |
| `boss_top_z_r4` | 12.341 | mm | 12.341 | keep-measured | scan | 0.03 | no | measure/figures/m08_top_annulus.json#boss |
| `cup_lower_draft_deg` | [3.58, 3.794] | deg | [3.58, 3.794] | keep-measured | scan | 0.03 | no | measure/figures/m06_refine.json#cup*.lower_wall |
| `cup_lower_r0` | [12.037, 11.995] | mm | [12.037, 11.995] | keep-measured | scan | 0.03 | yes | measure/figures/m06_refine.json#cup*.lower_wall; m02_cup_profile.png |
| `cup_pitch` | 38.97 | mm | 38.97 | keep-measured | scan | 0.01 | yes | intake/alignment.json#clock.detail.separation_mm |
| `cup_step_z_hi` | [7.925, 8.075] | mm | [7.925, 8.075] | keep-measured | scan | 0.05 | no | measure/figures/m06_refine.json#cup*.step_z_hi |
| `cup_step_z_lo` | [7.175, 7.275] | mm | [7.175, 7.275] | keep-measured | scan | 0.05 | no | measure/figures/m06_refine.json#cup*.step_z_lo |
| `cup_top_round_r` | [0.653, 0.469] | mm | [0.653, 0.469] | keep-measured | scan | 0.17 | no | measure/figures/m03_profile_fits.json#cup*.top_corner_round |
| `cup_top_slope_deg` | [8.67, 8.291] | deg | [8.67, 8.291] | keep-measured | scan | 0.03 | no | measure/figures/m08_top_annulus.json#cup* |
| `cup_top_z_r9` | [12.378, 12.279] | mm | [12.378, 12.279] | keep-measured | scan | 0.03 | no | measure/figures/m08_top_annulus.json#cup* |
| `cup_upper_draft_deg` | [4.119, 6.09] | deg | [4.119, 6.09] | keep-measured | scan | 0.04 | no | measure/figures/m06_refine.json#cup*.upper_wall |
| `cup_upper_r0` | [11.743, 11.96] | mm | [11.743, 11.96] | keep-measured | scan | 0.04 | no | measure/figures/m06_refine.json#cup*.upper_wall |
| `end_face_x` | [-34.119, 34.271] | mm | [-34.119, 34.271] | keep-measured | scan | 0.1 | no | measure/figures/m04_ears_webs.json#*.tab_outer_face_x |
| `flange_centre_y` | -0.142 | mm | -0.142 | keep-measured | scan | 0.08 | no | measure/figures/m01_flange.json |
| `flange_end_arc_cx` | [-19.466, 19.719] | mm | [-19.466, 19.719] | keep-measured | scan | 0.14 | no | measure/figures/m01_flange.json#ends.*.arc_fit |
| `flange_half_width` | 14.716 | mm | 14.716 | keep-measured | scan | 0.08 | no | measure/figures/m01_flange.json#skirt_y_top,skirt_y_bot |
| `flange_top_z` | 0 | mm | -0.004 | round-within-noise | scan | 0.0409 | no | intake/alignment.json#primary; measure/figures/m01_flange.json#flange_top_z_p50 |
| `lug_bottom_z` | [12.207, 12.212] | mm | [12.207, 12.212] | keep-measured | scan | 0.15 | no | measure/figures/m06_refine.json#lug_side_*_z |
| `lug_end_x` | [-42.388, 42.408] | mm | [-42.388, 42.408] | keep-measured | scan | 0.1 | no | measure/figures/m04_ears_webs.json#*.lug_end_x_extreme_p99 |
| `lug_half_width` | [3.692, 3.852] | mm | [3.692, 3.852] | keep-measured | scan | 0.08 | no | measure/figures/m04_ears_webs.json#*.lug_side_* |
| `lug_hole_cx` | [-38.553, 38.508] | mm | [-38.553, 38.508] | keep-measured | scan | 0.1 | yes | measure/figures/m04_ears_webs.json#*.lug_hole_fit |
| `lug_hole_cy` | [-0.08, -0.142] | mm | [-0.08, -0.142] | keep-measured | scan | 0.1 | no | measure/figures/m04_ears_webs.json#*.lug_hole_fit |
| `lug_hole_r` | [2.079, 2.107] | mm | [2.079, 2.107] | keep-measured | scan | 0.1 | yes | measure/figures/m04_ears_webs.json#*.lug_hole_fit |
| `lug_top_z` | [15.046, 14.963] | mm | [15.046, 14.963] | keep-measured | scan | 0.06 | no | measure/figures/m04_ears_webs.json#*.lug_top_z |
| `shank_fillet_r` | [0.646, 0.657] | mm | [0.646, 0.657] | keep-measured | scan | 0.23 | no | measure/figures/m03_profile_fits.json#cup*.shank_fillet |
| `shoulder_angle_deg` | [30.884, 31.132] | deg | [30.884, 31.132] | keep-measured | scan | 0.12 | no | measure/figures/m03_profile_fits.json#cup*.shoulder_z_vs_r |
| `shoulder_z_at_r5` | [14.204, 14.152] | mm | [14.204, 14.152] | keep-measured | scan | 0.12 | no | measure/figures/m03_profile_fits.json#cup*.shoulder_z_vs_r |
| `skirt_bottom_z` | -3.1 | mm | -3.17..-3.03 | keep-measured | scan | 0.07 | no | measure/figures/m01_flange.json#skirt_wall_z; intake/alignment.json#sanity_landmarks[3] |
| `tab_half_width_z0` | [4.668, 4.672] | mm | [4.668, 4.672] | keep-measured | scan | 0.05 | no | measure/figures/m04_ears_webs.json#*.tab_side_* |
| `tab_inner_x` | [-32.658, 32.586] | mm | [-32.658, 32.586] | keep-measured | scan | 0.15 | no | measure/figures/m04_ears_webs.json#*.tab_inner_face_x* |
| `tab_side_draft_deg` | [3.663, 2.957] | deg | [3.663, 2.957] | keep-measured | scan | 0.05 | no | measure/figures/m04_ears_webs.json#*.tab_side_* |
| `wall_t` | 1.2 | mm | — | assumed | assumed | — | no | DECISIONS.md OTHER interior design intent; intake/coverage.json |
| `web_half_width` | 0.964 | mm | [0.922, 0.958, 0.883, 0.994, 1.018, 0.985, 1.014, 0.936] | symmetry | scan | 0.07 | no | measure/figures/m04_ears_webs.json#*.web_*_side_* |
| `web_top_z` | 12.412 | mm | [12.504, 12.354, 12.42, 12.371] | symmetry | scan | 0.06 | no | measure/figures/m04_ears_webs.json#*.web_*_top_z |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

_No `feature_tree` was declared in `deliver/limitations.json`; see `build/MODELING_PLAN.md` for the ordered feature plan._

## 7. Tier-1 — caliper dims re-measured on the STEP

Band: ±— mm (`baseline/skills/stl2step-build123d/SKILL.md:87`, from `qa/gate.json#tier1.band_abs_mm`). Coverage: 0 of 12 gated; absent: [ENV-X, ENV-Y, ENV-Z, F01, F02, F03, F04, F05, F06, F07, F08, W01].

| dim | caliper | CAD re-measured | Δ | result | flags |
|---|---|---|---|---|---|
| ENV-X length over the two ear lug ends | — | 84.796 | — | ungated | — |
| ENV-Y flange width over straight skirt sides (mid-length) | — | 29.432 | — | ungated | — |
| F02 barb A shank OD z=20 | — | 5.366 | — | ungated | — |
| F04 cup A outer OD z=1 (jaws off the webs) | — | 23.9489 | — | ungated | — |
| F06 lug hole ID (+X) z=14 | — | 4.2139 | — | ungated | — |

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), SIGNED normal agreement (QA workaround qa/scripts/tier2_icp_signed.py; tier2_icp.py:52 is sign-free), iterations 29/60, converged yes, correction 0.0856° / 0.0272 mm.  
Unobservable CAD fraction: 0.0135.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 202383 | 0.1507 | 0.0818 | 0.3203 | 0.4875 | 1.1129 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 199176 | 0.1453 | 0.0808 | 0.3073 | 0.4616 | 0.7854 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 0.864 | 0.3044 | 1.5265 | 1.9359 | 3.0849 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 238679 | 0.8305 | 0.1984 | 1.4385 | 1.7159 | 3.0269 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 19730 | 0.8559 | 0.2957 | 1.5124 | 1.9444 | 3.0626 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.3073 max 0.7854 (n 199176) | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 1.5124 max 3.0626 (n 19730) | FAIL |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| B1 z -3.3..0.3 skirt+plate | region | scan_to_cad | reported | reported | n 40450 · p95 0.3474 · max 0.7031 | n 40450 · p95 0.3474 · max 0.7031 | — |
| B1 z -3.3..0.3 skirt+plate | region | cad_to_scan | reported | reported | n 88314 · p95 1.6391 · max 3.0626 | n 58674 · p95 1.5377 · max 3.0269 | — |
| B2 z 0.3..7 lower walls | region | scan_to_cad | reported | reported | n 51012 · p95 0.2858 · max 0.7854 | n 51012 · p95 0.2858 · max 0.7854 | — |
| B2 z 0.3..7 lower walls | region | cad_to_scan | reported | reported | n 77585 · p95 1.4626 · max 3.0849 | n 66126 · p95 1.365 · max 2.4024 | — |
| B3 z 7..12.6 upper walls+tops | region | scan_to_cad | reported | reported | n 61895 · p95 0.3141 · max 0.7093 | n 61551 · p95 0.313 · max 0.7093 | — |
| B3 z 7..12.6 upper walls+tops | region | cad_to_scan | reported | reported | n 86564 · p95 1.4431 · max 2.2684 | n 76548 · p95 1.3908 · max 2.268 | — |
| B4 z 12.6..18 shoulders+lugs | region | scan_to_cad | reported | reported | n 32741 · p95 0.3667 · max 0.865 | n 30540 · p95 0.3001 · max 0.6774 | — |
| B4 z 12.6..18 shoulders+lugs | region | cad_to_scan | reported | reported | n 30333 · p95 1.4022 · max 1.9744 | n 25344 · p95 1.4327 · max 1.9744 | — |
| B5 z 18..29 barbs | region | scan_to_cad | reported | reported | n 16285 · p95 0.2947 · max 1.1129 | n 15623 · p95 0.2883 · max 0.5133 | — |
| B5 z 18..29 barbs | region | cad_to_scan | reported | reported | n 17204 · p95 1.6702 · max 2.1272 | n 11987 · p95 1.7385 · max 2.1272 | — |
| I1 underside + skirt inner (unscanned) | interior | scan_to_cad | reported | reported | n 820 · p95 0.4322 · max 0.7031 | n 820 · p95 0.4322 · max 0.7031 | INTAKE §3 row 1 (not scanned at all) + MODELING_PLAN §6 (under-plate pocket, wall_t 1.2 assumed) |
| I1 underside + skirt inner (unscanned) | interior | cad_to_scan | reported | reported | n 44343 · p95 1.7833 · max 3.0626 | n 27528 · p95 1.6448 · max 3.0269 | INTAKE §3 row 1 (not scanned at all) + MODELING_PLAN §6 (under-plate pocket, wall_t 1.2 assumed) |
| I2 downward-facing interior (cavity ceilings, inner shoulders) | interior | scan_to_cad | reported | reported | n 982 · p95 0.5578 · max 0.5993 | n 982 · p95 0.5578 · max 0.5993 | INTAKE §3 row 2 (cup/boss interiors not scanned) + MODELING_PLAN §6 (cavities = skin offset by wall_t). Below z 19 inside \|x\|<32 no outer face points down |
| I2 downward-facing interior (cavity ceilings, inner shoulders) | interior | cad_to_scan | reported | reported | n 20884 · p95 1.3862 · max 1.9744 | n 20242 · p95 1.3876 · max 1.9744 | INTAKE §3 row 2 (cup/boss interiors not scanned) + MODELING_PLAN §6 (cavities = skin offset by wall_t). Below z 19 inside \|x\|<32 no outer face points down |
| I3 barb bores | interior | scan_to_cad | reported | reported | n 662 · p95 0.6412 · max 1.1129 | n 0 | INTAKE §3 row 3 (opening only) + MODELING_PLAN §6 (depth assumed through). Box \|dx\|,\|y\| <= 1.35 about each cup axis (corner r 1.91 < barb tip skin) |
| I3 barb bores | interior | cad_to_scan | reported | reported | n 6354 · p95 1.9341 · max 2.1272 | n 4467 · p95 1.9665 · max 2.1272 | INTAKE §3 row 3 (opening only) + MODELING_PLAN §6 (depth assumed through). Box \|dx\|,\|y\| <= 1.35 about each cup axis (corner r 1.91 < barb tip skin) |
| I4 boss hole | interior | scan_to_cad | reported | reported | n 224 · p95 0.4377 · max 0.5968 | n 224 · p95 0.4377 · max 0.5968 | INTAKE §3 row 4 (opening + ~1 mm wall) + MODELING_PLAN §6 (depth assumed through) |
| I4 boss hole | interior | cad_to_scan | reported | reported | n 169 · p95 0.4182 · max 0.7108 | n 0 | INTAKE §3 row 4 (opening + ~1 mm wall) + MODELING_PLAN §6 (depth assumed through) |
| Z1 flange top + skirt outline | functional_interface | scan_to_cad | reported | reported | n 31742 · p95 0.3637 · max 0.5997 | n 31742 · p95 0.3637 · max 0.5997 | INTAKE §4 Z1 (seat/locate). Flange top z±0.3 facing up, plus outward-facing skirt faces z -3.3..-0.3 (outward = normal points away from the part centre; excludes the invented pocket/skirt inner faces) |
| Z1 flange top + skirt outline | functional_interface | cad_to_scan | reported | reported | n 37419 · p95 0.7831 · max 3.0052 | n 25581 · p95 0.1609 · max 1.3561 | INTAKE §4 Z1 (seat/locate). Flange top z±0.3 facing up, plus outward-facing skirt faces z -3.3..-0.3 (outward = normal points away from the part centre; excludes the invented pocket/skirt inner faces) |
| Z2 barb nipples A+B | functional_interface | scan_to_cad | reported | reported | n 24284 · p95 0.3165 · max 1.1129 | n 23622 · p95 0.3117 · max 0.5133 | INTAKE §4 Z2 (hose connections): shank, flare, lip, tip, z>=14.5 within 4.5 mm of each cup axis in y. CAD side also contains the invented through-bore wall (see I3) |
| Z2 barb nipples A+B | functional_interface | cad_to_scan | reported | reported | n 24516 · p95 1.6973 · max 2.1272 | n 18803 · p95 1.7284 · max 2.1272 | INTAKE §4 Z2 (hose connections): shank, flare, lip, tip, z>=14.5 within 4.5 mm of each cup axis in y. CAD side also contains the invented through-bore wall (see I3) |
| Z3 ear lugs + holes | functional_interface | scan_to_cad | reported | reported | n 9844 · p95 0.3408 · max 0.6774 | n 9844 · p95 0.3408 · max 0.6774 | INTAKE §4 Z3 (screw/peg fixing): \|x\| 34.5..43, z 11..15.5. Lug underside only partly seen (INTAKE §3) |
| Z3 ear lugs + holes | functional_interface | cad_to_scan | reported | reported | n 10353 · p95 1.5334 · max 2.2684 | n 3280 · p95 0.2843 · max 2.268 | INTAKE §4 Z3 (screw/peg fixing): \|x\| 34.5..43, z 11..15.5. Lug underside only partly seen (INTAKE §3) |
| Z4 cup outer walls | functional_interface | scan_to_cad | reported | reported | n 56785 · p95 0.3069 · max 0.6257 | n 56785 · p95 0.3069 · max 0.6257 | INTAKE §4 Z4 (valve housing): side walls \|x\| 7..32, \|y\|>=1.5 (off the webs), z 0.3..11.8, near-vertical normals. CAD side also contains cavity walls behind (invented) |
| Z4 cup outer walls | functional_interface | cad_to_scan | reported | reported | n 83624 · p95 1.3667 · max 2.1177 | n 80175 · p95 1.3424 · max 1.7898 | INTAKE §4 Z4 (valve housing): side walls \|x\| 7..32, \|y\|>=1.5 (off the webs), z 0.3..11.8, near-vertical normals. CAD side also contains cavity walls behind (invented) |

### Masks (masked and unmasked are both shown above)

| mask | direction | why | fraction removed | stats inside |
|---|---|---|---|---|
| M1 barb-tip bridging membrane | scan_to_cad | scanner bridging film across the open barb bore mouth (translucent tip): scan material inside a through hole is not a surface of the part | 0.0033 | n: 662; rms: 0.2654; mean: 0.1909; p50: 0.1377; p95: 0.6412; p99: 0.8862; max: 1.1129 |
| M2 tab-lug junction junk facets | scan_to_cad | junk scan facets where the tab inner face meets the lug underside (occluded re-entrant corner, partly seen): scanner artefact, not part surface | 0.0126 | n: 2545; rms: 0.3673; mean: 0.3133; p50: 0.3138; p95: 0.6508; p99: 0.8114; max: 0.865 |
| M3 open boundary | cad_to_scan | distance from CAD to a scan hole EDGE is not a surface deviation (25 open loops incl. the 358° skirt lower-edge loop) | 0.2044 | n: 61321; rms: 0.9835; mean: 0.7651; p50: 0.6833; p95: 1.8489; p99: 2.4325; max: 3.0849 |

### Mask sensitivity

| band | direction | stats | variant |
|---|---|---|---|
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.0078; max_over_by: 0.3129 | scan_to_cad | n: 199838; rms: 0.1459; mean: 0.1076; p50: 0.0809; p95: 0.3078; p99: 0.4637; max: 1.1129 | all masks except M1 barb-tip bridging membrane |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.0196; max_over_by: 0.065 | scan_to_cad | n: 201721; rms: 0.1502; mean: 0.1099; p50: 0.0817; p95: 0.3196; p99: 0.4849; max: 0.865 | all masks except M2 tab-lug junction junk facets |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.2265; max_over_by: 2.2849 | cad_to_scan | n: 300000; rms: 0.864; mean: 0.6273; p50: 0.3044; p95: 1.5265; p99: 1.9359; max: 3.0849 | all masks except M3 open boundary |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.167; max_over_by: 2.2666 | cad_to_scan | n: 281475; rms: 0.8309; mean: 0.5943; p50: 0.2321; p95: 1.467; p99: 1.7813; max: 3.0666 | M3 open boundary radius 0.0 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.1461; max_over_by: 2.2626 | cad_to_scan | n: 261111; rms: 0.8255; mean: 0.5868; p50: 0.2025; p95: 1.4461; p99: 1.7346; max: 3.0626 | M3 open boundary radius 0.2 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.1416; max_over_by: 2.2626 | cad_to_scan | n: 252634; rms: 0.8258; mean: 0.5867; p50: 0.1977; p95: 1.4416; p99: 1.724; max: 3.0626 | M3 open boundary radius 0.4 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.1385; max_over_by: 2.2269 | cad_to_scan | n: 238679; rms: 0.8305; mean: 0.5919; p50: 0.1984; p95: 1.4385; p99: 1.7159; max: 3.0269 | M3 open boundary radius 0.8 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.1315; max_over_by: 1.6024 | cad_to_scan | n: 219171; rms: 0.8412; mean: 0.6074; p50: 0.2186; p95: 1.4315; p99: 1.6986; max: 2.4024 | M3 open boundary radius 1.5 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 1.1189; max_over_by: 1.4117 | cad_to_scan | n: 193092; rms: 0.8519; mean: 0.6238; p50: 0.2522; p95: 1.4189; p99: 1.6797; max: 2.2117 | M3 open boundary radius 2.5 mm |

### Over-band point clusters, scan → CAD (> 0.8 mm)

48 points (0.0002 fraction) in 0 clusters ≥ 20 pts.

### Over-band point clusters, CAD → scan (> 0.8 mm)

130910 points (0.4364 fraction) in 7 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 122423 | [0.079, -0.199, 4.773] | [2.409, 34.518] | [0, 360] | 3.0849 | **UNEXPLAINED** |
| 1 | 3748 | [-34.948, -0.772, 8.833] | [30.471, 42.305] | [174.1, 187.2] | 2.4024 | **UNEXPLAINED** |
| 2 | 2388 | [36.148, 0.131, 10.456] | [34.271, 42.408] | [0, 360] | 2.1047 | **UNEXPLAINED** |
| 3 | 786 | [-32.268, 1.778, 3.571] | [31.155, 32.825] | [174.2, 178.3] | 1.916 | **UNEXPLAINED** |
| 4 | 749 | [32.262, -1.783, 3.914] | [31.034, 32.76] | [354.1, 358.3] | 1.9219 | **UNEXPLAINED** |
| 5 | 715 | [32.055, 1.456, 2.642] | [31.062, 32.747] | [1.7, 5.7] | 2.1339 | **UNEXPLAINED** |
| 6 | 32 | [-32.746, 1.63, 14.96] | [32.667, 33.157] | [175.6, 178.6] | 1.1248 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 0.0197°, origin offset 0.0031 mm, point disagreement p95 0.0103 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (within).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| whole part scan->CAD (p95 band 0.30) | Masked p95 0.307 (unmasked 0.320) is a small, distributed overshoot. Attribution (qa/scripts/attribution.json, not a mask): (1) skirt lower band z < -1.5, where the scan lies INSIDE the CAD by a median -0.24..-0.36 mm growing with depth (2,315 pts > 0.30; p95 without it 0.288) — either an unmodelled draft/edge break on the skirt's lower outer edge or scan curl at the ragged open boundary (scan stops at z -2.0..-3.17), undecidable from the scan; (2) cup B upper wall z 9.5-11.8, scan OUTSIDE the CAD by median +0.11 / p95 +0.40 (p95 without it 0.296) — CAD cup B upper radius short near the top: a measurable geometry error; (3) tab/lug junction and tab side faces (p95 0.44-0.57 at x 32-35, z 11-15.5); (4) the translucent cup-wall ripple ±0.15 mm raises the floor everywhere (INTAKE §2). | (a) REVISE route=geometry/measure: re-measure cup B upper-wall radius/draft near the top; add a skirt lower-edge draft or break ONLY if an underside photo or an ENV-Y caliper at seat vs top confirms it; (b) one caliper pass (ENV-Y at the skirt bottom and top, F04) arbitrates skirt-curl vs real taper; (c) human ACCEPT-BAND of 0.307 vs 0.30. |
| whole part scan->CAD max (band 0.80), unmasked only | Unmasked max 1.113 mm = bridging film across barb A's bore mouth (M1); next 0.865 = junk facets at the tab/lug junction (M2). Masked max 0.785 passes, so the max is a masked pass (declared as a limitation). Not a geometry error. | rescan the barb tips and ear junction (matt spray on the translucent part) and re-run unmasked; or accept with the masks declared. |
| CAD->scan observable (p95 1.512 / max 3.063 vs 0.30 / 0.80) | Dominated by the invented hollow shell (owner decision: 1.2 mm walls, pocket under the plate, cavities, through bores; cluster c2s_0, 122k pts, d_p50 1.22): it was never scanned, yet the ray-cone observability heuristic counts it observable (only 1.35 % unobservable) because rays leave through the open underside. Remaining clusters are coverage gaps under the lug overhangs and inside the 1.3-1.5 mm slots. More geometry cannot fix this without data. | (a) scan the underside/interiors (or section the part) and rebuild the shell from data; (b) caliper W01 wall thickness + F03 bore; (c) human ACCEPT-BAND with the invented interior declared; (d) if the interior is not needed downstream, the owner may choose a different interior decision (e.g., solid) — an owner decision, not a QA fix. |

Missed band(s): `scan_to_cad:masked: p95 0.307 max 0.785 vs 0.3/0.8`; `cad_to_scan_observable: p95 1.512 max 3.063 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | no Tier-1 reading exists (0 of 12 calipered), so no Tier-1 miss to attribute |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | pass | datum re-derived from the raw scan by QA (qa/datum_audit.json); QA ICP T_refine is QA-only and never written back to intake/alignment.json; no expected value taken from params.json or this scan. The builder's own self-checks in MODELING_PLAN §8 (scan->CAD p95 0.308/0.299 on 200k samples) are a consistency check, not independent evidence, and QA's full-vertex number differs (see gate). |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 0 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | pass | INTAKE E01-E10 all present in CAD and visible in overlays (flange, skirt, 2 cups with step, shoulders, barbs with flare/lip/tip, bores, boss + hole, 4 webs, 2 tapered tabs, 2 lugs + holes); E11 parting ridge not modelled (cosmetic, declared); E12 interior invented (owner decision, declared). No scan->CAD over-band cluster >= 20 pts, i.e. no missing feature; every CAD->scan cluster explained below (invented interior or coverage gap). |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | pass | build/export_check.json + fillets.json: 5/5 fillets OK, target == used for every one (0.653, 0.646, 0.469, 0.657, 0.378); no REDUCED/FAILED/NO_EDGES |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | fresh context; did not build the model |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | n/a | iteration 1: no _itN_SUPERSEDED folder, no previous QA gate to compare. Within this QA, the default (sign-free) ICP run is kept as deviation_run1.json and labelled; it is not presented as an improvement. |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | pass | no pass depends on a mask |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | pass | QA census (qa/step_check.json): 106 faces, analytic area 98.6 %; 46 plane (no facet swarm), 35 cone, 17 cylinder, 8 B-spline (1.4 % area; declared in MODELING_PLAN §0 as OCC cone/cone round blends); grep of build/model.py for loft(/ruled/Polyline: no match |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | pass | OD-W03_photo1 (catalogue photo, no scale): stadium flange with skirt, two cups each with a single-barb nipple, small middle boss, webs, L-shaped ears with holes at both ends: all in CAD; nothing in CAD's outer skin is absent from photo+scan. Photo cannot confirm interior/underside (not visible). |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict BAND_NOT_MET |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 2 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L1 | No calipers: tier1 partial, none of the requested dimensions is calipered (ABSENT, not passed), and the absolute scale is not caliper-verified. Every size is scan-derived. | Any caliper reading in input/MEASUREMENTS.md (ENV-X / ENV-Y first, for scale) triggers a re-run of verify. | qa/gate.json#tier1; intake/MEASUREMENTS.md |
| L2 | Interior, underside, wall thickness (1.2 mm), barb-bore and boss-hole depths are assumed (owner decision: hollow shell), not measured. The observable CAD->scan miss comes almost entirely from these unscanned surfaces. | A scan of the underside/interior or a wall-thickness caliper reading triggers a rebuild and re-run. | DECISIONS.md; measure/params.json#wall_t; qa/VERDICT.md |
| L3 | The gate registration is a QA workaround (qa/scripts/tier2_icp_signed.py, signed normal agreement). The shipped tier2_icp.py paired the invented inner walls with the outer skin and converged to a shifted frame; that run is kept and reported (qa/deviation_run1.json). | tier2_icp.py fixed to use signed normal agreement triggers a re-run of the gate. | qa/gate.json#deviation_runs; qa/registration.json |
| L4 | Scan->CAD max passes only masked: M1 (bridging film across the barb A bore mouth) and M2 (junk facets at the tab/lug junction). Unmasked max is 1.1129 mm. Scan->CAD p95 misses the band masked (0.3073) and unmasked (0.3203). | A rescan of the barb tips and ear junctions (matt spray) triggers an unmasked re-run. | qa/masks.json; qa/gate.json#band_fails |
| L5 | The datum audit ran through qa/scripts/datum_audit_pair.py, because datum_audit.py has no two-feature midpoint origin or feature_line clock; it reuses datum_audit.py's own fit functions. | datum_audit.py gains circle-pair origin and feature_line clock support: re-run the audit. | qa/datum_audit.json |
| L6 | Overlays are drawn in the builder's datum frame (overlay.py has no registration option); the ICP correction is below what the panels resolve. | A registration correction larger than the panel resolution: regenerate the overlays in the ICP frame. | qa/overlays/ |
| L7 | Functional-interface zones Z1-Z4 are reported, not gated (baseline-skill has no interface band); the Z2/Z4 CAD->scan zone numbers include invented bore and cavity walls. | A regime with an interface band declared at intake triggers a re-run. | qa/zones.json; qa/gate.json#deviation.zones |
| L8 | Known fixable residuals left in the model by the owner's accept-now decision: cup B upper wall reads short of the scan, and the skirt's lower edge (scan inside the CAD) is either a real draft or scan curl the data cannot separate. | Owner asks for a REVISE loop, or a caliper reading on cup B / the skirt, triggers a measure-route loop 2. | qa/gate.json#miss_explanations; decisions/accept_band.md |

## 12. Assumptions and invented geometry

Parameters not measured on the scan or by caliper (source tag from `measure/params.json`):

| parameter | value | source | evidence |
|---|---|---|---|
| `wall_t` | 1.2 | assumed | DECISIONS.md OTHER interior design intent; intake/coverage.json |

- Hollow moulded shell: cups and boss open from below, plate/skirt/cup walls at the assumed thickness, barb bores through into the cup cavities, boss hole through into its cavity. _(source: assumed; DECISIONS.md; build/MODELING_PLAN.md §6)_
- Lug underside flat at the lowest point where the scan saw the lug side walls (the underside itself is not scanned). _(source: scan bound; measure/params.json#lug_bottom_z)_
- Units assumed mm; no scale correction applied. _(source: assumed; intake/alignment.json#checks.CHK-SCALE)_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** tooling or manufacture release until calipered and the underside is captured
- **Not fit for:** hose, seal or fixing-hole fit decisions (no dimension is caliper-verified; interior invented)
- Fit for: visual / outer-envelope model of the part (the outer skin follows the full-resolution scan)
- Fit for: a starting CAD for a caliper-verified revision
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): This result is NOT a dimensional certification: no dimension is caliper-verified and scale is unverified; the outer skin follows the full-res scan to scan->CAD p95 0.307 mm masked / 0.320 unmasked (band 0.30 missed), and the interior, underside, wall thickness and bore depths are invented. Not fit for tooling, seal/hose fit decisions or manufacture until calipered and the underside is captured; usable as a visual/envelope model of the outer skin only.

## 14. Human acceptance of the band miss

Accepted by **Ikbal (owner, decision card)** on 2026-09-28 (`DECISIONS.md`, ACCEPT-BAND): Accept and deliver now: accepts scan_to_cad and cad_to_scan_observable band misses, gate 2fe9569f1fa0 (created 2026-09-28T08:17:23+00:00); REVISE for the cup B upper wall offered and declined.. Record: `decisions/accept_band.md` (sha256 `231d4b908b6d5c0c4330bf1eca4c693068504208068c1a7557169967e45cc8ab`).

## 15. Reproduction

```
cd build && python3 model.py --params ../measure/params.json --alignment ../intake/alignment.json --out . --part OD-W03 --scripts <skills>/stl-re-rebuild-build123d/scripts
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-W03.step | 6260.7716 | 0 | 0 | yes | yes | no |
| OD-W03_datum.step | 6260.7716 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 16. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | 2fe9569f1fa0d2d3f911e587f7278256490945939ceff4eacdc668946fa21ffd |
| `measure/params.json` | 3adb924332695a96b7328d62e6c5243feae1189adaaaa49b11668db549283329 |
| `build/export_check.json` | b2958447827aef0bf257b3ee058f7c6f8e8fd5dd3c0789540eb89c3abbe20bfd |
| `intake/alignment.json` | 218719d01b7d3a6df1391dc44b12d31a8199de5e58cf294cf4ca35f6abf2c506 |
| `deliver/repro.json` | 73e60139d7c71c1af4945f853d368890dc00d1e692989a62dc41fc10298197c5 |
| `deliver/limitations.json` | 58318e93b0e650274aa566f334d877b7069157890cbc3ef798fc2e68280d9ace |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
