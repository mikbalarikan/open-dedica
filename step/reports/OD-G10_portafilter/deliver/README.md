# OD-G11_portafilter — STL → STEP reverse-engineering delivery

**Verdict: `BAND_NOT_MET`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 2 of 3 (earlier iterations kept: `_it1_SUPERSEDED/`).  
**Verification independence (CHK-INDEP):** pass — Fresh context; see independence. No builder numbers used.  

> **A deviation band was NOT met.** Delivered only under the recorded human acceptance below (by Ikbal (owner, session message), 2026-09-28, record `decisions/accept_band.md`).

## 1. The part

![reference photo](../input/photos/1.webp)

Espresso portafilter scanned as one assembly: cast cup with three bayonet lugs, two spout bosses with pan-head screws and a centre screw, open-bottom arch neck, tapered grip with collar and end cap, a pressurised insert (funnel floor, outlet trough, U rib, two V ribs, outlet pockets) and a round-wire retaining spring. Delivered as ONE fused solid (owner decision).

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-G11_portafilter_datum.step` | datum | 1 | yes | yes | 202 | 137692.5651 | max: [165.9484, 35.1788, 0]; min: [-35.7734, -35.0208, -59.0155]; size: [201.7218, 70.1996, 59.0155] |
| `build/OD-G11_portafilter.step` | scan | 1 | yes | yes | 202 | 137692.5651 | max: [100.4501, 83.0961, -176.1893]; min: [-83.6202, -26.6377, -289.4978]; size: [184.0703, 109.7338, 113.3084] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Datum: cup rim end face (gasket seat) is z = 0 with +Z out of the opening; cup axis from wall-face circle fits; handle end-cap normal clocks the handle to +X.
2. Scan-only parameters: every value is a primitive fit on the aligned scan (lines, circles, spheres, cones, planes) kept as measured; see the source column. No calipers.
3. build123d: revolved cup profile minus a revolved cavity cut by a funnel cone and an outlet trough; lugs with two ramp planes, pad, arch neck, neck/collar/grip revolves, spouts, drafted ribs, screws, wire arcs; one valid solid exported in the datum and scan frames.
4. Two independent verifications on the full-resolution scan under regime baseline-skill; iteration 1 REVISE, iteration 2 BAND_NOT_MET, band miss accepted by the owner.

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | cup axis (outer wall) ∩ rim end-face plane | — | — |
| primary (plane) | cup rim end face (sealing face, incl. lug tops in the same plane) | 0.0224 / 0.0976 | the rim end face seats against the group-head gasket; it is the functional axial datum of a portafilter |
| secondary (axis) | cup outer wall (drafted) + cup rim bore above the basket flange | 0.0269 / 0.1266 | the cast cup is turned about this axis; lugs and handle sit on it / coaxial bore of the same casting (tilt cross-check) |
| clock | plane_normal: handle end-cap flat normal -> +X (angle -25.4231°) | — | — |

Measured tilt: 0.2625° (common slope, per-feature intercept, 15 stations over 2 feature(s), z -35.000..-6.050 vs frame Z). Scale factor applied: 1. Scan noise floor: 0.0224 mm (rms of RANSAC+SVD plane on cup rim end face (sealing face, incl. lug tops in the same plane) (3756 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
-0.783298   0.416892  -0.461135  -52.417884
 0.345726   0.908638   0.234201   25.861116
 0.516642   0.024023  -0.855865  -232.226971
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: assumed 7, scan 150 (total 157). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `arch_foot_centre_v` | 7.4338 | mm | 7.4338 | keep-measured | scan | 0.05 | no | measure/figures/arch_feet.json |
| `arch_foot_centre_w` | -5.4698 | mm | -5.4698 | keep-measured | scan | 0.05 | no | measure/figures/arch_feet.json |
| `arch_foot_round_R` | 1.2131 | mm | 1.2131 | keep-measured | scan | 0.0484 | no | measure/figures/arch_feet.json |
| `arch_foot_w` | -6.7847 | mm | -6.7847 | keep-measured | scan | 0.05 | no | measure/figures/neck_pad.json#foot_min_w |
| `arch_outer_r` | 9.7324 | mm | 9.7324 | keep-measured | scan | 0.05 | no | measure/figures/neck_pad.json#arch_outer_r |
| `bore_dr_dz` | 0.0521 | mm | 0.0521 | keep-measured | scan | 0.0406 | no | measure/figures/body_profile.json#bore_upper |
| `bore_r_at_z0` | 27.8964 | mm | 27.8964 | keep-measured | scan | 0.0406 | yes | measure/figures/body_profile.json#bore_upper |
| `bottom_corner_R` | 4.6773 | mm | 4.6773 | keep-measured | scan | 0.0328 | no | measure/figures/body_profile.json#bottom_corner |
| `channel_end_t` | 41.659 | mm | 41.659 | keep-measured | scan | 0.1 | no | measure/figures/neck_pad.json#channel_end_x |
| `channel_halfwidth` | 6.1527 | mm | 6.1527 | keep-measured | scan | 0.05 | no | measure/figures/neck_pad.json#channel_halfwidth |
| `channel_roof_r` | 5.8403 | mm | 5.8403 | keep-measured | scan | 0.05 | no | measure/figures/neck_pad.json#channel_roof_r |
| `channel_start_t` | 29.5725 | mm | 29.5725 | keep-measured | scan | 0.1 | no | measure/figures/neck_pad.json#roof_x_extent |
| `collar_back_t` | 49.15 | mm | 49.15 | keep-measured | scan | 0.1 | no | measure/figures/handle_profile.json#collar_back_t |
| `collar_flank_axis_dy` | -0.0592 | mm | -0.0592 | keep-measured | scan | 0.0439 | no | measure/figures/neck_collar.json#collar_flank |
| `collar_flank_axis_dz` | -0.1343 | mm | -0.1343 | keep-measured | scan | 0.0439 | no | measure/figures/neck_collar.json#collar_flank |
| `collar_flank_dr_dt` | 0.571 | mm | 0.571 | keep-measured | scan | 0.0061 | no | measure/figures/neck_collar.json#collar_flank |
| `collar_flank_r_at_t0` | -11.7331 | mm | -11.7331 | keep-measured | scan | 0.0061 | no | measure/figures/neck_collar.json#collar_flank |
| `collar_peak_r` | 15.6137 | mm | 15.6137 | keep-measured | scan | 0.05 | no | measure/figures/handle_profile.json#collar_peak_r |
| `collar_step_t` | 44.45 | mm | 44.45 | keep-measured | scan | 0.1 | no | measure/figures/handle_profile.json#collar_step_t |
| `collar_top_round_R` | 0.6 | mm | — | assumed | assumed | 0.5 | no | measure/figures/handle_meridian.png |
| `cscrew_disc_r` | 4.0221 | mm | 4.0221 | keep-measured | scan | 0.1 | no | measure/figures/spouts_screw.json#centre_screw |
| `cscrew_disc_raise` | 0.1933 | mm | 0.1933 | keep-measured | scan | 0.05 | no | measure/figures/spouts_screw.json#centre_screw |
| `cscrew_x` | -2.9763 | mm | -2.9763 | keep-measured | scan | 0.1 | no | measure/figures/spouts_screw.json#centre_screw |
| `cscrew_y` | -0.0403 | mm | -0.0403 | keep-measured | scan | 0.1 | no | measure/figures/spouts_screw.json#centre_screw |
| `dome_R` | 100.5362 | mm | 100.5362 | keep-measured | scan | 0.0169 | no | measure/figures/body_profile.json#dome |
| `dome_centre_z` | 51.1 | mm | 51.1 | keep-measured | scan | 0.0169 | no | measure/figures/body_profile.json#dome |
| `end_chamfer_dr_dt` | -0.5573 | mm | -0.5573 | keep-measured | scan | 0.008 | no | measure/figures/handle_profile.json#end_chamfer |
| `end_chamfer_r_at_t0` | 104.3019 | mm | 104.3019 | keep-measured | scan | 0.008 | no | measure/figures/handle_profile.json#end_chamfer |
| `end_face_t` | 165.8674 | mm | 165.8674 | keep-measured | scan | 0.05 | yes | measure/figures/handle_profile.json#end_face_t |
| `end_round_R` | 0.6 | mm | — | assumed | assumed | 0.5 | no | measure/figures/handle_meridian.png |
| `floor_fillet_R` | 2.7058 | mm | 2.7058 | keep-measured | scan | 0.1733 | no | measure/figures/body_profile.json#floor_fillet |
| `funnel_apex_z` | -42.6473 | mm | -42.6473 | keep-measured | scan | 0.1061 | no | measure/figures/ribs_floor.json#floor_funnel_cone |
| `funnel_axis_x` | 19.5231 | mm | 19.5231 | keep-measured | scan | 0.1061 | no | measure/figures/ribs_floor.json#floor_funnel_cone |
| `funnel_axis_y` | -0.5046 | mm | -0.5046 | keep-measured | scan | 0.1061 | no | measure/figures/ribs_floor.json#floor_funnel_cone |
| `funnel_slope` | 0.1563 | mm | 0.1563 | keep-measured | scan | 0.1061 | no | measure/figures/ribs_floor.json#floor_funnel_cone |
| `grip_dr_dt` | 0.0187 | mm | 0.0187 | keep-measured | scan | 0.0255 | no | measure/figures/handle_axis.json#r_linear |
| `grip_r_at_t0` | 12.1427 | mm | 12.1427 | keep-measured | scan | 0.0255 | no | measure/figures/handle_axis.json#r_linear |
| `groove_apex_z` | -3.3445 | mm | -3.3445 | keep-measured | scan | 0.1 | no | measure/figures/wire_groove.json |
| `groove_depth` | 0.7321 | mm | 0.7321 | keep-measured | scan | 0.1 | no | measure/figures/wire_groove.json |
| `groove_lower_z` | -3.6737 | mm | -3.6737 | keep-measured | scan | 0.1 | no | measure/figures/wire_groove.json |
| `groove_theta_end` | 170 | deg | 170 | keep-measured | scan | 2.5 | no | measure/figures/wire_groove.json |
| `groove_theta_start` | 5 | deg | 5 | keep-measured | scan | 2.5 | no | measure/figures/wire_groove.json |
| `groove_upper_z` | -2.5833 | mm | -2.5833 | keep-measured | scan | 0.1 | no | measure/figures/wire_groove.json |
| `handle_axis_dy_dx` | -0.0041 | mm | -0.0041 | keep-measured | scan | 0.02 | no | measure/figures/handle_axis.json |
| `handle_axis_dz_dx` | -0.0062 | mm | -0.0062 | keep-measured | scan | 0.02 | no | measure/figures/handle_axis.json |
| `handle_axis_y0` | 0.0382 | mm | 0.0382 | keep-measured | scan | 0.02 | no | measure/figures/handle_axis.json |
| `handle_axis_z0` | -30.408 | mm | -30.408 | keep-measured | scan | 0.02 | no | measure/figures/handle_axis.json |
| `insert_wall_dr_dz` | 0.0294 | mm | 0.0294 | keep-measured | scan | 0.062 | no | measure/figures/body_profile.json#insert_wall |
| `insert_wall_r_at_z0` | 24.675 | mm | 24.675 | keep-measured | scan | 0.062 | no | measure/figures/body_profile.json#insert_wall |
| `ledge_taper_dr_dz` | 0.2631 | mm | 0.2631 | keep-measured | scan | 0.0391 | no | measure/figures/body_profile.json#ledge_taper |
| `ledge_taper_r_at_z0` | 28.5447 | mm | 28.5447 | keep-measured | scan | 0.0391 | no | measure/figures/body_profile.json#ledge_taper |
| `ledge_z` | -11.5267 | mm | -11.5267 | keep-measured | scan | 0.0224 | yes | measure/figures/body_profile.json#ledge_z |
| `lug1_centre_deg` | 59.5 | deg | 59.5 | keep-measured | scan | 0.288 | no | measure/figures/lugs_notches.json#lugs |
| `lug1_leadout_dz_per_deg` | 0.3311 | mm | 0.3311 | keep-measured | scan | 0.0215 | no | measure/figures/lug_ends.json |
| `lug1_leadout_z_centre` | -9.0617 | mm | -9.0617 | keep-measured | scan | 0.0215 | yes | measure/figures/lug_ends.json |
| `lug1_r_outer` | 35.9647 | mm | 35.9647 | keep-measured | scan | 0.05 | yes | measure/figures/lugs_notches.json#lugs |
| `lug1_span_deg` | 37 | deg | 37 | keep-measured | scan | 0.576 | no | measure/figures/lugs_notches.json#lugs |
| `lug1_under_dz_per_deg` | 0.0254 | mm | 0.0254 | keep-measured | scan | 0.0715 | no | measure/figures/details.json#lug_ramps |
| `lug1_under_z_centre` | -5.1276 | mm | -5.1276 | keep-measured | scan | 0.0715 | yes | measure/figures/details.json#lug_ramps |
| `lug2_centre_deg` | 180 | deg | 180 | keep-measured | scan | 0.288 | no | measure/figures/lugs_notches.json#lugs |
| `lug2_leadout_dz_per_deg` | 0.304 | mm | 0.304 | keep-measured | scan | 0.0513 | no | measure/figures/lug_ends.json |
| `lug2_leadout_z_centre` | -8.5268 | mm | -8.5268 | keep-measured | scan | 0.0513 | yes | measure/figures/lug_ends.json |
| `lug2_r_outer` | 35.7734 | mm | 35.7734 | keep-measured | scan | 0.05 | yes | measure/figures/lugs_notches.json#lugs |
| `lug2_span_deg` | 36 | deg | 36 | keep-measured | scan | 0.576 | no | measure/figures/lugs_notches.json#lugs |
| `lug2_under_dz_per_deg` | 0.026 | mm | 0.026 | keep-measured | scan | 0.0609 | no | measure/figures/details.json#lug_ramps |
| `lug2_under_z_centre` | -5.1021 | mm | -5.1021 | keep-measured | scan | 0.0609 | yes | measure/figures/details.json#lug_ramps |
| `lug3_centre_deg` | 300.5 | deg | 300.5 | keep-measured | scan | 0.288 | no | measure/figures/lugs_notches.json#lugs |
| `lug3_leadout_dz_per_deg` | 0.3335 | mm | 0.3335 | keep-measured | scan | 0.0269 | no | measure/figures/lug_ends.json |
| `lug3_leadout_z_centre` | -8.7638 | mm | -8.7638 | keep-measured | scan | 0.0269 | yes | measure/figures/lug_ends.json |
| `lug3_r_outer` | 35.942 | mm | 35.942 | keep-measured | scan | 0.05 | yes | measure/figures/lugs_notches.json#lugs |
| `lug3_span_deg` | 35 | deg | 35 | keep-measured | scan | 0.576 | no | measure/figures/lugs_notches.json#lugs |
| `lug3_under_dz_per_deg` | 0.0259 | mm | 0.0259 | keep-measured | scan | 0.0523 | no | measure/figures/details.json#lug_ramps |
| `lug3_under_z_centre` | -5.0175 | mm | -5.0175 | keep-measured | scan | 0.0523 | yes | measure/figures/details.json#lug_ramps |
| `neck_cone_axis_dy` | 0.0423 | mm | 0.0423 | keep-measured | scan | 0.0559 | no | measure/figures/neck_collar.json#neck_cone |
| `neck_cone_axis_dz` | -0.4071 | mm | -0.4071 | keep-measured | scan | 0.0559 | no | measure/figures/neck_collar.json#neck_cone |
| `neck_cone_dr_dt` | 0.568 | mm | 0.568 | keep-measured | scan | 0.0425 | no | measure/figures/neck_collar.json#neck_cone |
| `neck_cone_r_at_t0` | -12.0307 | mm | -12.0307 | keep-measured | scan | 0.0425 | no | measure/figures/neck_collar.json#neck_cone |
| `notch1_centre_deg` | 90 | deg | 90 | keep-measured | scan | 0.5061 | no | measure/figures/lugs_notches.json#rim_notches |
| `notch1_floor_z` | -1.1238 | mm | -1.1238 | keep-measured | scan | 0.1 | no | measure/figures/lugs_notches.json#rim_notches |
| `notch1_span_deg` | 14 | deg | 14 | keep-measured | scan | 0.5061 | no | measure/figures/lugs_notches.json#rim_notches |
| `notch2_centre_deg` | 270 | deg | 270 | keep-measured | scan | 0.5061 | no | measure/figures/lugs_notches.json#rim_notches |
| `notch2_floor_z` | -1.0936 | mm | -1.0936 | keep-measured | scan | 0.1 | no | measure/figures/lugs_notches.json#rim_notches |
| `notch2_span_deg` | 14 | deg | 14 | keep-measured | scan | 0.5061 | no | measure/figures/lugs_notches.json#rim_notches |
| `outer_wall_dr_dz` | 0.0449 | mm | 0.0449 | keep-measured | scan | 0.0285 | no | measure/figures/body_profile.json#outer_wall |
| `outer_wall_r_at_z0` | 30.5864 | mm | 30.5864 | keep-measured | scan | 0.0285 | yes | measure/figures/body_profile.json#outer_wall |
| `pad_R_at_z0` | 30.8847 | mm | 30.8847 | keep-measured | scan | 0.0544 | no | measure/figures/pad_fit.json#cone_vertical_axis |
| `pad_axis_x` | -0.3178 | mm | -0.3178 | keep-measured | scan | 0.0544 | no | measure/figures/pad_fit.json#cone_vertical_axis |
| `pad_axis_y` | 0.0205 | mm | 0.0205 | keep-measured | scan | 0.0544 | no | measure/figures/pad_fit.json#cone_vertical_axis |
| `pad_dR_dz` | -0.0492 | mm | -0.0492 | keep-measured | scan | 0.0544 | no | measure/figures/pad_fit.json#cone_vertical_axis |
| `pad_halfwidth_at_z0` | 15.9061 | mm | 15.9061 | keep-measured | scan | 0.0275 | no | measure/figures/details.json#pad_halfwidth |
| `pad_halfwidth_dz` | 0.0986 | mm | 0.0986 | keep-measured | scan | 0.0275 | no | measure/figures/details.json#pad_halfwidth |
| `pad_underchamfer_dx_dz` | 0.5171 | mm | 0.5171 | keep-measured | scan | 0.3467 | no | measure/figures/details.json#pad_underchamfer |
| `pad_underchamfer_x_at_z0` | 46.0992 | mm | 46.0992 | keep-measured | scan | 0.3467 | no | measure/figures/details.json#pad_underchamfer |
| `pocket_bore_bottom_z` | -54 | mm | — | assumed | assumed | 0.5 | no | build/MODELING_PLAN.md |
| `pocket_bore_r` | 3.5 | mm | — | assumed | assumed | 0.5 | no | measure/figures/floor_heightmap_max_z.npy |
| `recess_arm` | 1.5237 | mm | 1.5237 | keep-measured | scan | 0.2 | no | measure/figures/spouts_screw.json#centre_screw |
| `recess_depth` | 2.2074 | mm | 2.2074 | keep-measured | scan | 0.2 | no | measure/figures/spouts_screw.json#centre_screw |
| `recess_width` | 0.9 | mm | — | assumed | assumed | 0.5 | no | measure/figures/spouts_screw.png |
| `rim_inner_round_R` | 0.8541 | mm | 0.8541 | keep-measured | scan | 0.0368 | no | measure/figures/body_profile.json#rim_inner_round |
| `rim_inner_round_cr` | 28.6733 | mm | 28.6733 | keep-measured | scan | 0.0368 | no | measure/figures/body_profile.json#rim_inner_round |
| `rim_outer_round_R` | 0.3272 | mm | 0.3272 | keep-measured | scan | 0.0413 | no | measure/figures/body_profile.json#rim_outer_round |
| `rim_top_z` | 0 | mm | -0.0219 | round-within-noise | scan | 0.0224 | yes | measure/figures/body_profile.json#rim_top_z |
| `spout1_head_z_r3p2` | -57.6461 | mm | -57.6461 | keep-measured | scan | 0.05 | no | measure/figures/details.json |
| `spout1_ring_z` | -56.3777 | mm | -56.3777 | keep-measured | scan | 0.05 | no | measure/figures/details.json |
| `spout1_tip_z` | -59.0626 | mm | -59.0626 | keep-measured | scan | 0.05 | yes | measure/figures/spouts_screw.json#spout_0 |
| `spout1_wall_dr_dz` | 0.0985 | mm | 0.0985 | keep-measured | scan | 0.02 | no | measure/figures/details.json |
| `spout1_wall_r_at_z0` | 11.3428 | mm | 11.3428 | keep-measured | scan | 0.02 | no | measure/figures/details.json |
| `spout1_x` | 9.9363 | mm | 9.9363 | keep-measured | scan | 0.02 | yes | measure/figures/spouts_screw.json#spout_0 |
| `spout1_y` | 14.906 | mm | 14.906 | keep-measured | scan | 0.02 | yes | measure/figures/spouts_screw.json#spout_0 |
| `spout2_head_z_r3p2` | -57.6954 | mm | -57.6954 | keep-measured | scan | 0.05 | no | measure/figures/details.json |
| `spout2_ring_z` | -56.3218 | mm | -56.3218 | keep-measured | scan | 0.05 | no | measure/figures/details.json |
| `spout2_tip_z` | -59.0335 | mm | -59.0335 | keep-measured | scan | 0.05 | yes | measure/figures/spouts_screw.json#spout_1 |
| `spout2_wall_dr_dz` | 0.1026 | mm | 0.1026 | keep-measured | scan | 0.02 | no | measure/figures/details.json |
| `spout2_wall_r_at_z0` | 11.5417 | mm | 11.5417 | keep-measured | scan | 0.02 | no | measure/figures/details.json |
| `spout2_x` | 9.8992 | mm | 9.8992 | keep-measured | scan | 0.02 | yes | measure/figures/spouts_screw.json#spout_1 |
| `spout2_y` | -15.1116 | mm | -15.1116 | keep-measured | scan | 0.02 | yes | measure/figures/spouts_screw.json#spout_1 |
| `spout_boss_root_R` | 1.5 | mm | — | assumed | assumed | 0.5 | no | measure/figures/spouts_screw.png |
| `spout_head_r` | 3.5 | mm | — | assumed | assumed | 0.5 | no | measure/figures/spouts_screw.png |
| `trough_rc` | 17.757 | mm | 17.757 | keep-measured | scan | 0.3034 | no | measure/figures/trough.json#const |
| `trough_rho` | 6.0167 | mm | 6.0167 | keep-measured | scan | 0.3034 | no | measure/figures/trough.json#const |
| `trough_zc` | -36.7663 | mm | -36.7663 | keep-measured | scan | 0.3034 | no | measure/figures/trough.json#const |
| `uplat_dz_dx` | 0.1747 | mm | 0.1747 | keep-measured | scan | 0.0421 | no | measure/figures/ribs_floor.json#floor_in_U_plane |
| `uplat_dz_dy` | 0.0051 | mm | 0.0051 | keep-measured | scan | 0.0421 | no | measure/figures/ribs_floor.json#floor_in_U_plane |
| `uplat_z0` | -33.8305 | mm | -33.8305 | keep-measured | scan | 0.0421 | no | measure/figures/ribs_floor.json#floor_in_U_plane |
| `urib_inner_absy` | 5.093 | mm | 5.093 | keep-measured | scan | 0.05 | no | measure/figures/details.json |
| `urib_open_end_x` | -15.014 | mm | -15.014 | keep-measured | scan | 0.1 | no | measure/figures/details.json |
| `urib_outer_absy` | 6.4873 | mm | 6.4873 | keep-measured | scan | 0.1 | no | measure/figures/details.json |
| `urib_round_end_outer_x` | 7.0149 | mm | 7.0149 | keep-measured | scan | 0.1 | no | measure/figures/details.json |
| `urib_top_z` | -26.9158 | mm | -26.9158 | keep-measured | scan | 0.05 | no | measure/figures/ribs_floor.json#U_top_z |
| `vrib1_joint` | [10.7119, 7.9175] | mm | [10.7119, 7.9175] | keep-measured | scan | 0.1017 | no | measure/figures/vrib_segments.json#V_pos |
| `vrib1_outer_end` | [-5.248, 21.9657] | mm | [-5.248, 21.9657] | keep-measured | scan | 0.0938 | no | measure/figures/vrib_segments.json#V_pos |
| `vrib1_tip` | [12.7631, 3.3925] | mm | [12.7631, 3.3925] | keep-measured | scan | 0.1017 | no | measure/figures/vrib_segments.json#V_pos |
| `vrib1_top_z` | -28.9511 | mm | -28.9511 | keep-measured | scan | 0.05 | no | measure/figures/ribs_floor.json#V_pos |
| `vrib2_joint` | [10.5673, -7.7531] | mm | [10.5673, -7.7531] | keep-measured | scan | 0.1042 | no | measure/figures/vrib_segments.json#V_neg |
| `vrib2_outer_end` | [-5.9017, -21.7111] | mm | [-5.9017, -21.7111] | keep-measured | scan | 0.1042 | no | measure/figures/vrib_segments.json#V_neg |
| `vrib2_tip` | [12.478, -3.6545] | mm | [12.478, -3.6545] | keep-measured | scan | 0.0779 | no | measure/figures/vrib_segments.json#V_neg |
| `vrib2_top_z` | -28.9984 | mm | -28.9984 | keep-measured | scan | 0.05 | no | measure/figures/ribs_floor.json#V_neg |
| `vrib_width_base` | 2.3634 | mm | 2.3634 | keep-measured | scan | 0.1 | no | measure/figures/vrib_flanks.json |
| `vrib_width_top` | 1.5637 | mm | 1.5637 | keep-measured | scan | 0.1 | no | measure/figures/vrib_flanks.json |
| `vrib_width_z_base` | -37.5 | mm | -37.5 | keep-measured | scan | 0.5 | no | measure/figures/vrib_flanks.json |
| `vrib_width_z_top` | -29.5 | mm | -29.5 | keep-measured | scan | 0.5 | no | measure/figures/vrib_flanks.json |
| `wire1_R` | 75.5433 | mm | 75.5433 | keep-measured | scan | 0.1171 | no | measure/figures/wire.json#segments |
| `wire1_cx` | -42.1295 | mm | -42.1295 | keep-measured | scan | 0.1171 | no | measure/figures/wire.json#segments |
| `wire1_cy` | -28.4015 | mm | -28.4015 | keep-measured | scan | 0.1171 | no | measure/figures/wire.json#segments |
| `wire1_theta_span` | [359.9898, 67.1112] | deg | [359.9898, 67.1112] | keep-measured | scan | 1 | no | measure/figures/wire.json#segments |
| `wire1_zc` | -3.0144 | mm | -3.0144 | keep-measured | scan | 0.1171 | no | measure/figures/wire.json#segments |
| `wire2_R` | 71.8468 | mm | 71.8468 | keep-measured | scan | 0.3229 | no | measure/figures/wire.json#segments |
| `wire2_cx` | 34.0872 | mm | 34.0872 | keep-measured | scan | 0.3229 | no | measure/figures/wire.json#segments |
| `wire2_cy` | -33.5594 | mm | -33.5594 | keep-measured | scan | 0.3229 | no | measure/figures/wire.json#segments |
| `wire2_theta_span` | [92.6449, 173.6401] | deg | [92.6449, 173.6401] | keep-measured | scan | 1 | no | measure/figures/wire.json#segments |
| `wire2_zc` | -3.8668 | mm | -3.8668 | keep-measured | scan | 0.3229 | no | measure/figures/wire.json#segments |
| `wire3_R` | 68.2484 | mm | 68.2484 | keep-measured | scan | 0.4371 | no | measure/figures/wire.json#segments |
| `wire3_cx` | 2.259 | mm | 2.259 | keep-measured | scan | 0.4371 | no | measure/figures/wire.json#segments |
| `wire3_cy` | 42.9912 | mm | 42.9912 | keep-measured | scan | 0.4371 | no | measure/figures/wire.json#segments |
| `wire3_theta_span` | [235.0639, 298.6866] | deg | [235.0639, 298.6866] | keep-measured | scan | 1 | no | measure/figures/wire.json#segments |
| `wire3_zc` | -3.1317 | mm | -3.1317 | keep-measured | scan | 0.4371 | no | measure/figures/wire.json#segments |
| `wire_r` | 0.5838 | mm | 0.5838 | keep-measured | scan | 0.1171 | no | measure/figures/wire.json#segments |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

| id | feature | params |
|---|---|---|
| F01 | cup outer revolve (dome, drafted wall, rim) | [dome_centre_z, dome_R, outer_wall_r_at_z0, outer_wall_dr_dz] |
| F02 | cavity: bore, ledge, taper, insert wall, funnel floor, outlet trough | [bore_r_at_z0, ledge_z, insert_wall_r_at_z0, funnel_apex_z, trough_rc] |
| F04 | spout bosses with screw heads, pockets | [spout1_x, spout1_tip_z, pocket_bore_r] |
| F06 | U plateau, U rib, V ribs | [uplat_z0, urib_inner_absy, vrib1_joint, vrib_width_top] |
| F09 | three bayonet lugs with ramp and lead-out, rim notches | [lug1_centre_deg, lug1_under_z_centre, lug1_leadout_z_centre, notch1_centre_deg] |
| F11 | pad, arch neck with rounded feet, neck cone, collar, grip, end cap | [pad_R_at_z0, arch_outer_r, arch_foot_round_R, neck_cone_r_at_t0, grip_r_at_t0, end_face_t] |
| F14 | screw recesses, wire groove, wire arcs | [recess_depth, groove_depth, wire1_R, wire_r] |

## 7. Tier-1 — caliper dims re-measured on the STEP

Band: ±— mm (`baseline/skills/stl2step-build123d/SKILL.md:87`, from `qa/gate.json#tier1.band_abs_mm`). Coverage: 0 of 8 gated; absent: [ENV-X rim centre to handle end, ENV-Y cup OD at z~-10, ENV-Z rim face to spout tip, F01 rim bore ID just above the ledge, F02 ledge depth from the rim, F03 lug under-face height at both ends of a lug, F04 spout centre distance, F05 grip OD at collar end and at cap].

| dim | caliper | CAD re-measured | Δ | result | flags |
|---|---|---|---|---|---|
| F01 rim bore ID just above the ledge (CAD only, ungated) | — | 54.6436 | — | ungated | — |

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), iterations 66/400, converged yes, correction 0.1708° / 0.0328 mm.  
Unobservable CAD fraction: 0.038.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 250812 | 0.1391 | 0.055 | 0.2839 | 0.5555 | 1.3455 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 250812 | 0.1391 | 0.055 | 0.2839 | 0.5555 | 1.3455 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 0.5512 | 0.0548 | 0.9097 | 2.9496 | 5.7948 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 280776 | 0.4086 | 0.0508 | 0.3592 | 2.596 | 5.6806 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 19241 | 0.3091 | 0.0518 | 0.3783 | 1.5407 | 4.9016 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.2839 max 1.3455 (n 250812) | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 0.3783 max 4.9016 (n 19241) | FAIL |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| BORE | functional_interface | scan_to_cad | reported | reported | n 9675 · p95 0.2435 · max 1.109 | n 9675 · p95 0.2435 · max 1.109 | rim bore and basket ledge (z~-11.5); z window stops below the wire arcs |
| BORE | functional_interface | cad_to_scan | reported | reported | n 9896 · p95 0.2388 · max 1.0746 | n 9568 · p95 0.2319 · max 0.7672 | rim bore and basket ledge (z~-11.5); z window stops below the wire arcs |
| CENTRE_SCREW | region | scan_to_cad | reported | reported | n 1163 · p95 0.2234 · max 0.4351 | n 1163 · p95 0.2234 · max 0.4351 | centre screw with cross recess on the bottom |
| CENTRE_SCREW | region | cad_to_scan | reported | reported | n 1105 · p95 0.3613 · max 0.7861 | n 1094 · p95 0.3594 · max 0.7861 | centre screw with cross recess on the bottom |
| CUP_OUTER | region | scan_to_cad | reported | reported | n 45972 · p95 0.0948 · max 0.2285 | n 45972 · p95 0.0948 · max 0.2285 | drafted cup outer wall away from the neck/pad |
| CUP_OUTER | region | cad_to_scan | reported | reported | n 47281 · p95 0.0983 · max 0.2206 | n 47281 · p95 0.0983 · max 0.2206 | drafted cup outer wall away from the neck/pad |
| HANDLE | region | scan_to_cad | reported | reported | n 58507 · p95 0.1271 · max 0.3973 | n 58507 · p95 0.1271 · max 0.3973 | collar, tapered grip, end cap (x >= 50) |
| HANDLE | region | cad_to_scan | reported | reported | n 87418 · p95 0.1729 · max 5.2742 | n 83118 · p95 0.1131 · max 4.9228 | collar, tapered grip, end cap (x >= 50) |
| INSERT_FLOOR | interior | scan_to_cad | reported | reported | n 42334 · p95 0.4354 · max 1.2234 | n 42334 · p95 0.4354 · max 1.2234 | black pressurised insert: funnel floor, U rib, V ribs, 2 outlet pockets; rib flanks and pocket interiors partly occluded/unscanned |
| INSERT_FLOOR | interior | cad_to_scan | reported | reported | n 58897 · p95 2.2109 · max 5.7948 | n 47390 · p95 1.5576 · max 5.6806 | black pressurised insert: funnel floor, U rib, V ribs, 2 outlet pockets; rib flanks and pocket interiors partly occluded/unscanned |
| LUGS | functional_interface | scan_to_cad | reported | reported | n 6042 · p95 0.6046 · max 0.9673 | n 6042 · p95 0.6046 · max 0.9673 | 3 bayonet lugs: outer radius and ramped under-faces (59.5/180/300.5 deg) |
| LUGS | functional_interface | cad_to_scan | reported | reported | n 6143 · p95 0.7243 · max 1.4426 | n 6093 · p95 0.7235 · max 1.4426 | 3 bayonet lugs: outer radius and ramped under-faces (59.5/180/300.5 deg) |
| NECK | region | scan_to_cad | reported | reported | n 22323 · p95 0.3805 · max 0.8513 | n 22323 · p95 0.3805 · max 0.8513 | pad + open-bottom arch neck + channel (x 29..50) |
| NECK | region | cad_to_scan | reported | reported | n 22851 · p95 0.4373 · max 1.4289 | n 22442 · p95 0.424 · max 1.0999 | pad + open-bottom arch neck + channel (x 29..50) |
| RIM | functional_interface | scan_to_cad | reported | reported | n 6605 · p95 0.1897 · max 0.2997 | n 6605 · p95 0.1897 · max 0.2997 | rim end face z=0 incl. lug tops (gasket seat, datum primary) |
| RIM | functional_interface | cad_to_scan | reported | reported | n 6727 · p95 0.297 · max 1.2367 | n 6707 · p95 0.2943 · max 1.2367 | rim end face z=0 incl. lug tops (gasket seat, datum primary) |
| SPOUTS | functional_interface | scan_to_cad | reported | reported | n 10833 · p95 0.4219 · max 1.0985 | n 10833 · p95 0.4219 · max 1.0985 | two spout bosses, pan-head screw heads and tips (simplified heads, owner PART-CLASS) |
| SPOUTS | functional_interface | cad_to_scan | reported | reported | n 13587 · p95 3.3316 · max 5.7948 | n 12439 · p95 3.2272 · max 5.6806 | two spout bosses, pan-head screw heads and tips (simplified heads, owner PART-CLASS) |
| WIRE | region | scan_to_cad | reported | reported | n 12228 · p95 0.3928 · max 1.325 | n 12228 · p95 0.3928 · max 1.325 | retaining wire spring arcs seen through the bore (ends dive out of sight) |
| WIRE | region | cad_to_scan | reported | reported | n 9077 · p95 0.6226 · max 1.5325 | n 7096 · p95 0.3208 · max 1.4257 | retaining wire spring arcs seen through the bore (ends dive out of sight) |
| ZB_0_10 | region | scan_to_cad | reported | reported | n 47374 · p95 0.3837 · max 1.3455 | n 47374 · p95 0.3837 · max 1.3455 | z-band bucket |
| ZB_0_10 | region | cad_to_scan | reported | reported | n 43214 · p95 0.4652 · max 1.5325 | n 40823 · p95 0.3814 · max 1.4426 | z-band bucket |
| ZB_10_20 | region | scan_to_cad | reported | reported | n 46066 · p95 0.1769 · max 0.4219 | n 46066 · p95 0.1769 · max 0.4219 | z-band bucket |
| ZB_10_20 | region | cad_to_scan | reported | reported | n 50285 · p95 0.1578 · max 0.4179 | n 50164 · p95 0.1575 · max 0.4179 | z-band bucket |
| ZB_20_30 | region | scan_to_cad | reported | reported | n 47373 · p95 0.2087 · max 0.8513 | n 47373 · p95 0.2087 · max 0.8513 | z-band bucket |
| ZB_20_30 | region | cad_to_scan | reported | reported | n 61979 · p95 0.2208 · max 1.5112 | n 60397 · p95 0.1913 · max 1.5044 | z-band bucket |
| ZB_30_40 | region | scan_to_cad | reported | reported | n 54828 · p95 0.3953 · max 1.2234 | n 54828 · p95 0.3953 · max 1.2234 | z-band bucket |
| ZB_30_40 | region | cad_to_scan | reported | reported | n 75220 · p95 1.9841 · max 5.2742 | n 63604 · p95 0.7411 · max 4.9228 | z-band bucket |
| ZB_40_50 | region | scan_to_cad | reported | reported | n 47228 · p95 0.2399 · max 0.9825 | n 47228 · p95 0.2399 · max 0.9825 | z-band bucket |
| ZB_40_50 | region | cad_to_scan | reported | reported | n 60687 · p95 1.0898 · max 5.7948 | n 57486 · p95 0.2524 · max 5.6806 | z-band bucket |
| ZB_50_60 | region | scan_to_cad | reported | reported | n 7943 · p95 0.4928 · max 1.0985 | n 7943 · p95 0.4928 · max 1.0985 | z-band bucket |
| ZB_50_60 | region | cad_to_scan | reported | reported | n 8615 · p95 2.804 · max 3.2686 | n 8302 · p95 2.8082 · max 3.2667 | z-band bucket |

### Masks (masked and unmasked are both shown above)

| mask | direction | why | fraction removed | stats inside |
|---|---|---|---|---|
| M1 open boundary | cad_to_scan | distance from a CAD point to a scan hole EDGE is not a surface deviation: the scan has 15 open-boundary loops (spout/outlet pockets inside the insert, neck-channel roof end, bore/wire gaps, a slit along the grip) | 0.0596 | n: 17884; rms: 1.5485; mean: 1.1135; p50: 0.7562; p95: 3.3559; p99: 4.397; max: 5.7948 |
| M2 skin normal | cad_to_scan | a CAD point whose nearest scan triangle faces >70 deg away is matched to an occluded/other surface (one fused solid of an assembly: internal faces, pocket walls in shadow, rib flanks in shadow), not an outer-skin deviation | 0.009 | n: 2713; rms: 1.6166; mean: 1.1335; p50: 0.682; p95: 3.5922; p99: 4.5185; max: 5.6474 |

### Mask sensitivity

| band | direction | stats | variant |
|---|---|---|---|
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.4873; max_over_by: 4.9948 | cad_to_scan | n: 297287; rms: 0.5318; mean: 0.1852; p50: 0.0542; p95: 0.7873; p99: 2.8936; max: 5.7948 | all masks except M1 open boundary |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.0743; max_over_by: 4.8806 | cad_to_scan | n: 282116; rms: 0.4136; mean: 0.1355; p50: 0.051; p95: 0.3743; p99: 2.611; max: 5.6806 | all masks except M2 skin normal |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.2571; max_over_by: 4.9948 | cad_to_scan | n: 293391; rms: 0.4633; mean: 0.1604; p50: 0.0533; p95: 0.5571; p99: 2.7018; max: 5.7948 | M1 open boundary radius 0.0 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.1577; max_over_by: 4.9948 | cad_to_scan | n: 289201; rms: 0.4365; mean: 0.1476; p50: 0.0523; p95: 0.4577; p99: 2.6497; max: 5.7948 | M1 open boundary radius 0.2 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.0955; max_over_by: 4.9948 | cad_to_scan | n: 285417; rms: 0.4196; mean: 0.1389; p50: 0.0515; p95: 0.3955; p99: 2.6177; max: 5.7948 | M1 open boundary radius 0.4 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.0592; max_over_by: 4.8806 | cad_to_scan | n: 280776; rms: 0.4086; mean: 0.1333; p50: 0.0508; p95: 0.3592; p99: 2.596; max: 5.6806 | M1 open boundary radius 0.8 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.0369; max_over_by: 4.8806 | cad_to_scan | n: 275081; rms: 0.4027; mean: 0.13; p50: 0.0502; p95: 0.3369; p99: 2.5917; max: 5.6806 | M1 open boundary radius 1.5 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; p95_over_by: 0.02; max_over_by: 4.8806 | cad_to_scan | n: 266460; rms: 0.4004; mean: 0.1277; p50: 0.0496; p95: 0.32; p99: 2.6007; max: 5.6806 | M1 open boundary radius 2.5 mm |

### Over-band point clusters, scan → CAD (> 0.8 mm)

469 points (0.0019 fraction) in 8 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 159 | [-3.996, 25.986, -5.442] | [25.459, 26.825] | [92.5, 110] | 1.3455 | WIRE ARC 1 (declared simplification), STILL OPEN / unchanged vs it1 cluster 4 (it1 162 pts max 1.353 -> it2 159 pts max 1.346): r 25.5-26.8, theta 92.5-110, z -6.2..-4.9, lower side of the wire arc where it dives behind the bore. On well-scanned surface (median 5.0 mm from any scan hole edge, qa/edge_dist_it2.json), so a real shape difference: the CAD torus arc (constant R, one z) does not follow the wire's real 3D path there (overlays theta=92/110, Z=-5.5). This is the whole-part scan->CAD max. Fixable only by modelling the wire as a swept 3D path; the owner's PART-CLASS allowed the wire to be simplified. |
| 1 | 44 | [2.322, -22.002, -36.743] | [20.901, 22.82] | [270.4, 281.8] | 1.2234 | SCAN HOLE EDGE, insert wall-to-floor corner at theta 270-282 (44 pts, max 1.223; r 20.9-22.8, z -37.8..-35.4). All points within 0.63 mm of a scan open-boundary vertex (qa/edge_dist_it2.json; whole-scan median 11.3 mm) -- the edge of open-boundary loop 0 (INTAKE_CARD section 3: r 10.4-23.4, theta 256-351, z -44..-29). Overlay theta=276: the scan wall curls inward and stops where the gutter floor was not captured. Present at the same level in it1 (43 pts, 1.211; not in it1's top-12 list). Not a missing feature; not fixable without coverage of the gutter floor. No scan-side open-boundary mask exists in the protocol (it1 declared CAD->scan masks only), so these points stay in the gated statistic. |
| 2 | 40 | [12.909, 3.112, -39.179] | [12.916, 13.687] | [12.5, 14.2] | 0.9825 | V-RIB 1 crest/flank, IMPROVED vs it1 cluster 1 (306 pts max 1.374 -> 40 pts max 0.982): r 12.9-13.7, theta 12.5-14.2, z -41.3..-35.2, the rib's lower outer end next to the floor. Within 1.1-1.8 mm of a scan hole (shadowed flank, loop 2), overlay theta=13 shows a residual ~0.9 mm at the rib foot. Small, partly unobserved; fixable only marginally. |
| 3 | 40 | [8.065, 13.7, -56.671] | [15.399, 16.462] | [53.3, 62.6] | 1.0985 | SPOUT 1 SCREW HEAD (declared simplification), unchanged vs it1 (same box: 40 pts, 1.083 -> 1.099): r 15.4-16.5, theta 53-63, z -57.3..-56.2, the pan-head crown / cross-recess rim. Well scanned (12.7 mm from holes). Overlay Z=-57: the scan recess lobes are not on the CAD's axis-aligned cross (recess orientation/width assumed, MODELING_PLAN section 4). Fixable from the scan (orient/size the recess) but part of the owner-allowed screw-head simplification. |
| 4 | 26 | [7.739, 31.834, -2.509] | [30.846, 35.164] | [75.8, 76.7] | 0.9673 | LUG 1 trailing end, IMPROVED vs it1 cluster 9 (103 pts max 1.394 -> 26 pts max 0.967): r 30.8-35.2, theta 75.8-76.7, z -3.1..-2.0, the lead-out plane added in it2 sits ~0.9 mm off the scan at its top end (overlay theta=76). Well scanned (17.6 mm from holes): a real, small, fixable geometric residual (lead-out plane angle/height). |
| 5 | 24 | [7.635, -15.707, -56.906] | [16.887, 19.147] | [295.2, 297.6] | 1.0304 | SPOUT 2 SCREW HEAD (declared simplification), unchanged vs it1 (same box: 22 pts 1.024 -> 24 pts 1.030): r 16.9-19.1, theta 295-298, z -57.4..-56.4; same cause as cluster 3 (recess orientation assumed; overlay Z=-57). |
| 6 | 23 | [-1.164, 21.835, -36.617] | [20.814, 22.742] | [87.9, 97.6] | 1.1944 | SCAN HOLE EDGE, insert wall-to-floor corner at theta 88-98 (23 pts, max 1.194; r 20.8-22.7, z -37.4..-35.3): all within 0.37 mm of a scan open-boundary vertex, edge of open-boundary loop 2 (theta 15-101). Same cause as cluster 1; present in it1 at the same level (22 pts, 1.164). Not fixable without coverage. |
| 7 | 20 | [-21.737, -4.9, -34.579] | [21.408, 22.873] | [188.1, 198.5] | 1.1622 | SCAN HOLE EDGE, -X floor-to-wall corner at theta 188-198 (20 pts, max 1.162; r 21.4-22.9, z -35.2..-33.7): within 1.1 mm of open-boundary loop 6 (theta 188-203, r 12.4-23.0, z -36.7..-28.2). Overlay theta=180/193: the scan corner is rounder than the CAD fillet next to the hole. Paired with CAD->scan clusters 4/6 (U plateau round end, 1.74/1.61, unchanged vs it1 clusters 10/11). Partly unobserved; unchanged from it1 (19 pts, 1.157). |

### Over-band point clusters, CAD → scan (> 0.8 mm)

15974 points (0.0532 fraction) in 16 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 4811 | [6.916, -14.703, -42.561] | [11.176, 23.79] | [255, 349.6] | 4.9538 | **UNEXPLAINED** |
| 1 | 4758 | [7.734, 14.15, -42.247] | [13.835, 23.755] | [19.2, 102.8] | 5.7948 | **UNEXPLAINED** |
| 2 | 3179 | [-0.98, 5.358, -34.86] | [6.487, 17.927] | [0.2, 360] | 4.7906 | **UNEXPLAINED** |
| 3 | 2215 | [136.964, 13.6, -34.723] | [105.821, 159.832] | [4.3, 7.2] | 5.2742 | **UNEXPLAINED** |
| 4 | 112 | [-15.029, -4.659, -36.094] | [14.001, 18.494] | [191.5, 201.3] | 1.7443 | **UNEXPLAINED** |
| 5 | 109 | [-8.035, 24.481, -3.465] | [24.52, 27.013] | [98.8, 119.6] | 1.2989 | **UNEXPLAINED** |
| 6 | 102 | [-22.004, -5.45, -35.455] | [21.089, 23.671] | [188.1, 199.8] | 1.605 | **UNEXPLAINED** |
| 7 | 72 | [41.455, -5.444, -28.687] | [41.089, 42.096] | [351.4, 355.2] | 1.4289 | **UNEXPLAINED** |
| 8 | 67 | [7.184, 33.341, -2.323] | [31.713, 35.964] | [76.9, 78] | 1.1559 | **UNEXPLAINED** |
| 9 | 67 | [13.393, 2.435, -38.677] | [12.906, 14.333] | [9.1, 12.5] | 0.9813 | **UNEXPLAINED** |
| 10 | 56 | [-11.762, -24.835, -4.231] | [26.242, 27.721] | [239.2, 248.8] | 1.5325 | **UNEXPLAINED** |
| 11 | 44 | [26.168, 23.034, -5.178] | [31.352, 35.965] | [41, 42.8] | 1.4426 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 0.0025°, origin offset 0.0626 mm, point disagreement p95 0.063 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (within).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| Whole part scan->CAD max (p95 0.284 PASSES, max 1.346 vs 0.80) | 469 of 250812 scan points (0.19 %) over 0.8 mm, in 8 clusters >= 20 pts (it1: 2713 pts, 18 clusters). Breakdown: wire arc 1, declared simplification, 159 pts, max 1.346 (unchanged vs it1); scan hole edges at the insert wall-to-floor corner (theta 90/190/276), 87 pts, max 1.223 (unchanged vs it1, not a modelling miss); spout screw heads, declared simplification, 64 pts, max 1.099; fixable small residuals on scanned surfaces: V-rib 1 foot 40 pts max 0.982, lug 1 end 26 pts max 0.967, lug 2 end 16 pts max 0.923. | Accept (ACCEPT-BAND citing this gate). Or a final loop 3 (REVISE, the last one): swept-path wire arc 1, oriented screw recesses, lug lead-out planes -- would lower the max to ~1.22 (hole-edge points) but cannot reach 0.80 without coverage data or a pre-declared scan-side open-boundary mask. |
| Whole part CAD->scan observable (p95 0.378 vs 0.30, max 4.902 vs 0.80) | Dominated by unscanned regions (L2): of 394 observable over-band points, 137 are the grip strip (max 4.902) and 215 the pocket bores / U-rib centre open-boundary region. Without those four clusters (diagnostic only, qa/obs_residual_it2.json) p95 0.284 / max 1.461; the remaining observable over-band points (42) are: U plateau round end / -X floor corner at open-boundary loop 6 (1.461, 1.375; unchanged vs it1 CAD->scan clusters 10/11), wire arcs (1.220), lug 1 leading end theta 41-43 (1.150), spout-1 head (1.138), centre post r~5 (1.083), lug 1 lead-out (1.077), neck-pad hole edge theta 351-355 (1.066). Outside the observable subsample the full CAD->scan set also shows the rim notch at 270 deg outer edge (34 pts, max 1.237) and lug 1 leading end (44 pts, max 1.443, unchanged vs it1). | Not fixable by geometry: the grip strip and pocket interiors need a rescan. Accept (ACCEPT-BAND) or rescan; geometry work can only trim the secondary residuals. |
| LUGS (functional interface; no interface band in this regime, reported) | Improved: scan->CAD p95 0.740->0.605, max 1.394->0.967; CAD->scan max 1.935->1.443. Remaining: lug 1 leading end theta 41-43 (CAD->scan 44 pts, 1.443, unchanged), lug 1 trailing lead-out theta 76-78 (0.967 / 1.156), lug 2 lead-out theta 197 (1.097). | Caliper/feeler reading of F03 (lug under-face at both ends) would arbitrate; geometry trim of lead-out planes in a loop 3 if the owner wants the lugs within 0.8. |
| INSERT_FLOOR (interior, reported) | Largely fixed: scan->CAD p95 0.727->0.435, max 2.441->1.223 (it1 floor ring, both troughs, centre post, V-rib 2 fixed; V-rib 1 improved). Residual max is scan-hole-edge points (clusters 1/6/7). | None by geometry; rescan the gutter floor. |

Missed band(s): `scan_to_cad:masked: p95 0.284 max 1.346 vs 0.3/0.8`; `cad_to_scan_observable: p95 0.378 max 4.902 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | No Tier-1 reading exists (scan-only run): no Tier-1 miss to attribute. F01 re-measured CAD-only (54.644, ungated). |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | pass | Datum audited on the raw full-res scan from INTAKE_CARD/alignment descriptions (0.0025 deg / 0.063 mm, identical to it1: alignment.json unchanged, sha 0a2b0dbc). QA ICP T_refine is evaluation-only, never written back. No expected value from params.json or this scan; the builder self-check in MODELING_PLAN.md is a consistency check, not independent evidence, and was not used. |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 8 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | finding | All 11 INTAKE_CARD section-5 feature families exist in the CAD (cup, bore/ledge, 3 lugs, 2 rim notches, pad, arch neck+collar+grip+cap, 2 spouts with screw heads, centre screw, insert floor/U rib/V ribs/2 outlet pockets+trough, 3 wire arcs; it2 adds a wire groove in the bore, consistent with it1 wire-end clusters 6/7/11 now gone). Cast lettering not modelled (declared cosmetic). Invented only where declared (pocket bores to z -54, grip strip). Finding: some features exist but are misshaped vs the scan: spout-head cross recesses (orientation/width assumed; Z=-57 overlay shows the scan recess lobes not on the CAD's axis-aligned cross), wire arc 1 near 90-110 deg, lug 1 ends (41-43 and 76-78 deg), rim notch at 270 deg outer edge -- see cluster explanations. |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | finding | build/fillets.json / export_check: 11 OK (target == used), 1 REDUCED: 'F13 cone-part leg-foot rounds' target 1.213 -> used 0.970 (0.8x, fillet failed at target; declared plan section 6 fallback). The it1 finding (dropped arch-foot round) is addressed: overlay x=40 now shows rounded CAD feet following the scan; CAD foot bottom sits ~0.3 mm below the scan foot; zone NECK scan->CAD max 0.851 (4 points over 0.8). |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | Fresh context; see independence. No builder numbers used. |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | pass | Same protocol as it1: qa/regime.json, masks.json, zones.json, datum_spec.json, icp_scan_masks.json, dims.json and both helper scripts are byte-identical to _it1_SUPERSEDED/qa (sha256 prefixes 80f0aece, f93a3988, 060414e8, 9a66a838, f9748b2c, 953c29bd, 3b394b45, 2fc6ea14); same full-res scan (9eb34045); ICP params identical (60-cap run first: not converged in both iterations; cap raised once to 400 in both); deviation sampling/seeds identical; observability params identical (only the data-dependent helper-switch count 47->48 differs); same low-memory wrapper. Only the STEP changed, so every it1->it2 delta is geometry, not protocol. Per-cluster comparison in qa/it1_vs_it2_clusters.json (same bbox, both arrays). Side by side (qa/it1_vs_it2_gated.json, qa/it1_vs_it2_clusters.json): scan->CAD p95 0.365 -> 0.284, max 2.441 -> 1.346, points over 0.8: 2713 -> 469; CAD->scan observable p95 0.464 -> 0.378, max 4.984 -> 4.902; CAD->scan masked p95 0.432 -> 0.359; ICP 85/400 its 0.176 deg/0.047 mm -> 66/400 its 0.171 deg/0.033 mm; datum audit unchanged (0.003 deg/0.063 mm). it1 scan->CAD clusters (over-0.8 pts / max in the same box, it1 -> it2): 0 floor ring 645/1.961 -> 0/0.779 FIXED; 1 V-rib 1 306/1.374 -> 40/0.982 IMPROVED, open; 2 trough pocket 1 277/2.441 -> 9/0.918 IMPROVED, near-closed; 3 trough pocket 2 219/2.321 -> 0/0.750 FIXED; 4 wire arc 90-110 deg 162/1.353 -> 159/1.346 STILL OPEN (unchanged); 5 centre post 158/1.192 -> 0/0.690 FIXED; 6 wire/rim notch 90 124/0.960 -> 0/0.418 FIXED; 7 wire end 111/1.183 -> 0/0.614 FIXED; 8 lug 2 end 104/1.298 -> 16/0.923 IMPROVED, open; 9 lug 1 end 103/1.394 -> 26/0.967 IMPROVED, open; 10 V-rib 2 99/1.403 -> 1/0.890 FIXED (1 pt); 11 wire end 67/1.189 -> 0/0.523 FIXED. it1 CAD->scan clusters: 0-3 unscanned (pockets, U-rib centre, grip strip) unchanged (max 4.93/5.73/4.80/5.21 -> 4.95/5.80/4.79/5.27); 4 floor ring 1057/2.716 -> 0/0.761 FIXED; lug ends 5/6/7 190/1.995, 147/1.733, 137/1.858 -> 67/1.156, 35/1.097, 21/0.998 IMPROVED; 8 wire 110/1.320 -> 109/1.299 unchanged; 9 centre post 109/1.574 -> 0/0.754 FIXED; 10/11 U plateau round end / -X corner (hole edge, loop 6) 109/1.745, 93/1.621 -> 112/1.744, 102/1.605 unchanged. Improvement is geometry, not protocol. |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | pass | no pass depends on a mask |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | pass | QA census (qa/step_check.json): 202 faces, analytic area 95.4 %, 16 B-spline (fillet) faces, 108 planes (builder face_stats median plane area 2.85 mm2), 0 ruled-like; within the plan's expected 150-300. model.py has no loft(/ruled/polyline stack; the 3 Wire.make_polygon calls (model.py:239 V-rib drafted section, :346 handle revolve profile, :421 wire-arc wedge) are single closed profiles, not stacks of scan slices. |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | pass | Photo 1 (top/inside): rim, 3 lugs, wire spring arcs across the bore, black insert with U rib, neck, collar ring, tapered black grip, cream end cap -- all present in CAD. Photo 2 (bottom): two spout bosses with cross-recess screws, centre cross screw, lugs, arch neck, collar, grip, cap -- all present. Rim notches not visible in photos (mesh-only, accepted at intake). Nothing in the CAD absent from both photos and scan except the declared invented pocket bores. |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict BAND_NOT_MET |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 3 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L1 | Tier-1 not run (tier1 partial: none of the requested dims has a caliper reading, owner chose scan-only); absolute scale is not caliper-verified (CHK-SCALE flag). All requested dims are absent, not passed. | any caliper reading (rim bore ID, ledge depth, lug under-face heights, spout spacing): fill input/MEASUREMENTS.md, rehash, re-run verify | qa/gate.json#limitations |
| L2 | Unscanned or occluded regions carry invented or interpolated CAD and set the observable CAD->scan miss (max 4.9016 mm): the two outlet-pocket bores (depth assumed), the insert floor inside the U rib (open scan region) and a strip along the grip that the scanner missed. | a rescan covering the pocket interiors, the insert floor inside the U rib and the grip strip, or a depth-gauge reading of the pocket depth | qa/gate.json#limitations |
| L3 | The fine tessellation of both STEPs has two zero-area triangles each (spout-1 root / bottom-round junction and the insert floor near the trough); the B-rep itself is one valid closed solid with no naked edges. | any rebuild: re-run step_check and the tessellation probe | qa/gate.json#limitations |
| L4 | Verify ICP needed its iteration cap raised once (same as iteration 1); both runs and the no-ICP datum-frame run agree, so the gate numbers do not depend on it. | any rebuild: re-run ICP at the default cap first | qa/gate.json#limitations |
| L5 | One fused solid of an assembly: internal interfaces between cup, insert, grip, cap, screws and wire are not represented; the wire is three planar arcs and the screw heads are simplified. The wire arc sets the scan->CAD max 1.3455 mm. | an owner decision to model the wire as a swept path, orient the screw recesses, or model the bodies separately | qa/gate.json#limitations |
| L6 | The verify deviation gate ran through a memory-only wrapper (smaller observability ray chunk) because the unmodified script was killed for lack of memory; the per-point result is identical. | observability chunk size exposed on the deviation_gate.py CLI: re-run it directly | qa/gate.json#limitations |
| L7 | Protocol carried unchanged from iteration 1: masks apply to CAD->scan only, so scan points on scan-hole edges stay in the gated scan->CAD statistic, and the observable CAD->scan subset is unmasked. | a protocol decision declared before the next gate (for example a scan-side open-boundary mask), then re-run verify reporting both | qa/gate.json#limitations |
| L8 | CHK-FILLET: the leg-foot rounds on the flared neck-cone part were built REDUCED (1.2131 mm target, a smaller declared fallback used; see export_check.json fillets); all other fillets are at their target radius. | a rebuild of the neck that splits the cone-part foot edges so the full radius applies | build/export_check.json#fillets |

## 12. Assumptions and invented geometry

Parameters not measured on the scan or by caliper (source tag from `measure/params.json`):

| parameter | value | source | evidence |
|---|---|---|---|
| `collar_top_round_R` | 0.6 | assumed | measure/figures/handle_meridian.png |
| `end_round_R` | 0.6 | assumed | measure/figures/handle_meridian.png |
| `pocket_bore_bottom_z` | -54 | assumed | build/MODELING_PLAN.md |
| `pocket_bore_r` | 3.5 | assumed | measure/figures/floor_heightmap_max_z.npy |
| `recess_width` | 0.9 | assumed | measure/figures/spouts_screw.png |
| `spout_boss_root_R` | 1.5 | assumed | measure/figures/spouts_screw.png |
| `spout_head_r` | 3.5 | assumed | measure/figures/spouts_screw.png |

- Spout pocket bore radius and depth below the insert floor are invented (the scan has open holes there). _(source: assumed; measure/params.json#pocket_bore_bottom_z)_
- Screw cross-recess width and orientation, spout screw head rim radius, collar crest and end-face rounds were read by eye from section figures. _(source: assumed; measure/params.json)_
- Material between the outer and inner scanned surfaces is filled solid (one fused solid of cast cup, plastic insert, grip, cap, screws and wire). _(source: assumed; DECISIONS.md PART-CLASS)_
- Units assumed millimetres; no scale applied (no calipers). _(source: assumed; intake/alignment.json#checks)_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** manufacture, tooling or fit-critical use: the band was NOT met (max and observable CAD->scan) and no dimension is caliper-verified
- **Not fit for:** modelling the separate bodies (cup, insert, grip, screws, wire): this is one fused solid
- **Not fit for:** the pocket interiors and the grip strip, which are invented or interpolated
- Fit for: visualisation, packaging and fixture design around the portafilter envelope
- Fit for: a design-intent starting point (cup, rim, lugs, bore, handle agree with the scan within the p95 band)
- Fit for: re-measurement with calipers against the named parameters
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): Not a pass under baseline-skill plastic (p95<=0.30 / max<=0.80): QA does not certify this STEP for fit, tooling or manufacture. Scan->CAD p95 now meets 0.30 but both maxima and the observable CAD->scan p95 miss; the cup outer wall (p95 0.095), rim face, bore and handle agree with the scan well -- a regional observation, not a grade. No dimension is caliper-verified (absolute scale unverified); the one fused solid does not model the separate bodies; pocket interiors, the insert floor inside the U rib and a strip of the grip are invented/interpolated; wire and screw heads are simplified. Delivery needs a recorded ACCEPT-BAND decision.

## 14. Human acceptance of the band miss

Accepted by **Ikbal (owner, session message)** on 2026-09-28 (`DECISIONS.md`, ACCEPT-BAND): "tamam, band kaçarsa kabul ediyorum, teslim et": accepts scan_to_cad:masked (max) and cad_to_scan_observable (p95, max) misses for delivery, gate 0f2d41f2bdd2 (created 2026-09-28T11:17:26+00:00).. Record: `decisions/accept_band.md` (sha256 `52f337f1406dc33a77cb1d3efd5104a7348e19248cbf477e0b313a38b0d39cd4`).

## 15. Reproduction

```
cd build && python3 model.py --params ../measure/params.json --alignment ../intake/alignment.json --out . --part OD-G11_portafilter --scripts <stl-re-rebuild-build123d/scripts>
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-G11_portafilter.step | 137692.5651 | 0 | 0 | yes | yes | no |
| OD-G11_portafilter_datum.step | 137692.5651 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 16. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | 0f2d41f2bdd29d6c21ee9db91ef1f3242a715fd09dac0614170b76a3d5fcb894 |
| `measure/params.json` | bf59c5866c0bc367bb2457269e66a0b67197dc516065d29c3c55400304ee3738 |
| `build/export_check.json` | ae92e56d50bf60fe933157852f5e173af33e9510bb16e0955078c6196e87bfe2 |
| `intake/alignment.json` | 0a2b0dbca01e7d48b144991ff743a06bcf0a6f8f466f5ddbbb9198c4f5380e0a |
| `deliver/repro.json` | e34ed6ce350c83b7d0e32ef752467f1518adb607299df45dd42d36045965d197 |
| `deliver/limitations.json` | c03b290aba414306fb3312b17cf9f6438aecef587fb5bf0634f357a4bd931420 |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
