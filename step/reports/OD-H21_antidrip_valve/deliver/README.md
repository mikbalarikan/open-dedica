# OD-H21_antidrip-valve — STL → STEP reverse-engineering delivery

**Verdict: `BAND_NOT_MET`** (from `qa/gate.json`; full reasoning in `qa/VERDICT.md`).  
**Band regime:** baseline-skill — source `baseline/skills/stl2step-build123d/SKILL.md:87`.  
**Iteration:** 2 of 3 (earlier iterations kept: `_it1_SUPERSEDED/`).  
**Verification independence (CHK-INDEP):** pass — fresh context; see independence  

> **A deviation band was NOT met.** Delivered only under the recorded human acceptance below (by Ikbal (owner, session message "del'ver"), 2026-09-28, record `decisions/accept_band.md`).

## 1. The part

![reference photo](../input/photos/photo_2.png)

DeLonghi anti-drip valve (OD-H21): a turned plastic assembly with a snap nozzle and corner lugs, an 8-rib nut, bands, a body with a radial threaded outlet carrying an O-ring, a windowed cap ring and a hose barb on the cap. Scanned as one closed shell; the CAD is one fused solid of the outer envelope plus the observed openings.

## 2. Deliverables

| file | frame | solids | valid | closed | faces | volume mm³ | bbox mm |
|---|---|---|---|---|---|---|---|
| `build/OD-H21_antidrip-valve_datum.step` | datum | 1 | yes | yes | 146 | 19376.4953 | max: [30.0179, 24.7507, 28.3739]; min: [-13.4714, -13.4309, -27.4241]; size: [43.4893, 38.1816, 55.7981] |
| `build/OD-H21_antidrip-valve.step` | scan | 1 | yes | yes | 146 | 19376.4953 | max: [-3.6433, 8.5883, -124.8244]; min: [-51.0701, -25.516, -185.4459]; size: [47.4268, 34.1043, 60.6214] |

Source of the table: `build/export_check.json`. The editable design intent is `build/model.py` driven by `measure/params.json`.

## 3. Method

1. Intake: full working copy, noise floors, coverage map, feature enumeration from mesh and both photos; regime baseline-skill declared by the owner before any gate numbers.
2. Datum: upper band top face (primary, z = 0), nozzle axis as the origin on that face, +X along the side-outlet collar normal (intake/alignment.json).
3. Measure: every parameter from the full-res scan (scan-only, no calipers), each with rule, estimator and evidence (measure/params.json).
4. Rebuild: build123d revolves of fitted (r,u) profiles about each sub-part's measured axis, prisms for lugs, ribs and web, a torus for the O-ring, one fused cut pass; exported in datum and scan frames.
5. Verify: an independent agent with its own ICP, two-way full-res deviation, zones, declared masks and observability; iteration 1 REVISE (three geometric findings), iteration 2 BAND_NOT_MET with no rebuild target left.
6. Owner accepted the remaining band misses for delivery (DECISIONS.md ACCEPT-BAND, decisions/accept_band.md).

## 4. Coordinate frames

Two STEP files carry the same solid (SYNTHESIS D14): the **datum frame** (design frame, below) and the **scan frame** (the original STL coordinates; the CAD overlays the raw scan).

| element | definition | fit residual (rms / max mm) | why |
|---|---|---|---|
| origin | nozzle OD axis ∩ band top face plane | — | — |
| primary (plane) | band top face: up-facing annular step (r 10-11.5) where the body cylinder leaves the band ring | 0.0266 / 0.1016 | flat perpendicular to the valve axis at the band/body assembly interface; the cleanest scanned flat (rms 0.027 over seeds 0-7, vs nozzle shoulder 0.041-0.042 and cap top 0.044-0.046, intake/noise_plane_*.json); its normal agrees with the body-cylinder axis and the nozzle-shoulder normal within ~0.4 deg (rough-frame exploration) |
| secondary (axis) | nozzle OD sections | 0.0313 / 0.113 | nozzle = the plug-in spigot of the valve (the functional insertion axis); cleanest circle on the part |
| clock | plane_normal: side-outlet collar outer face normal -> +X (angle 13.8775°) | — | — |

Measured tilt: 1.2669° (common slope, per-feature intercept, 15 stations over 1 feature(s), z -22.000..-15.000 vs frame Z). Scale factor applied: 1. Scan noise floor: 0.0347 mm (rms of RANSAC+SVD plane on nozzle end face (down-facing moulded annulus at the nozzle tip, r 4.0-5.8, raw offset -78.4..-77.8 along -axis) (964 faces)).

Scan → datum matrix (row-major, `intake/alignment.json#matrix_4x4`); the scan-frame STEP uses its inverse:

```
-0.788645  -0.218663  -0.574652  -110.011810
-0.150680   0.974858  -0.164156  -17.568500
 0.596099  -0.042872  -0.801765  -104.575327
 0.000000   0.000000   0.000000   1.000000
```

## 5. Parameters

Sources: scan 103 (total 103). Rendered from `measure/params.json`; never edited by hand.

| name | value | unit | measured | rule | source | ± mm | critical | evidence |
|---|---|---|---|---|---|---|---|---|
| `band_step_u` | -2.5407 | mm | -2.5407 | keep-measured | scan | 0.0655 | no | measure/figures/fits.json#levels.band_step |
| `bandlo_R0` | 12.2048 | mm | 12.2048 | keep-measured | scan | 0.0611 | no | measure/figures/fits.json#segments.band_lo |
| `bandlo_axis_c` | [-0.096, -0.2359] | mm | [-0.096, -0.2359] | keep-measured | scan | 0.0611 | no | measure/figures/fits.json#segments.band_lo |
| `bandlo_base_u` | -5.6 | mm | -5.6 | keep-measured | scan | 0.1 | no | measure/figures/fits.json#tables_cols; measure/figures/fits.json tables body_frame |
| `bandlo_k` | 0.051 | mm | 0.051 | keep-measured | scan | 0.0611 | no | measure/figures/fits.json#segments.band_lo |
| `bandup_R` | 12.0089 | mm | 12.0089 | keep-measured | scan | 0.044 | no | measure/figures/fits.json#segments.band_up |
| `bandup_axis_c` | [0.1076, -0.196] | mm | [0.1076, -0.196] | keep-measured | scan | 0.044 | no | measure/figures/fits.json#segments.band_up |
| `bandup_top_round_R` | 0.5647 | mm | 0.5647 | keep-measured | scan | 0.0369 | no | measure/figures/fits.json#rounds.band_up_top |
| `barb_R0` | 2.7516 | mm | 2.7516 | keep-measured | scan | 0.0425 | yes | measure/figures/fits.json#barb.tube_taper |
| `barb_axis_d` | [0.5641, 0.8257, 0.0082] | mm | [0.5641, 0.8257, 0.0082] | keep-measured | scan | 0.0478 | no | measure/figures/fits.json#barb |
| `barb_axis_p` | [0.4488, -0.3066, 24.2486] | mm | [0.4488, -0.3066, 24.2486] | keep-measured | scan | 0.0478 | no | measure/figures/fits.json#barb |
| `barb_bore_R` | 1.2518 | mm | 1.2518 | keep-measured | scan | 0.0951 | no | measure/figures/fits.json#barb.end_bore |
| `barb_bore_floor_u` | 27.2827 | mm | 26.6189..27.9464 | keep-measured | scan | 0.4 | no | measure/figures/fits.json#bore_floors.barb |
| `barb_end_u` | 28.3727 | mm | 28.3727 | keep-measured | scan | 0.067 | no | measure/figures/fits.json#barb.end_face |
| `barb_flare_rho0` | 2.823 | mm | 2.823 | keep-measured | scan | 0.2641 | no | measure/figures/fits.json#barb.flare |
| `barb_flare_slope` | 0.6245 | mm | 0.6245 | keep-measured | scan | 0.2641 | no | measure/figures/fits.json#barb.flare |
| `barb_k` | -0.0084 | mm | -0.0084 | keep-measured | scan | 0.0425 | no | measure/figures/fits.json#barb.tube_taper |
| `barb_rear_round_R` | 0.9344 | mm | 0.9344 | keep-measured | scan | 0.0798 | no | measure/figures/fits.json#barb.rear_round |
| `barb_rear_u` | -2.9976 | mm | -2.9976 | keep-measured | scan | 0.0661 | no | measure/figures/fits.json#barb.rear_face |
| `body_R` | 10.0218 | mm | 10.0218 | keep-measured | scan | 0.0601 | no | measure/figures/fits.json#segments.body |
| `body_axis_c` | [0.1495, -0.1614] | mm | [0.1495, -0.1614] | keep-measured | scan | 0.0601 | no | measure/figures/fits.json#segments.body |
| `bulb_R0` | 3.3506 | mm | 3.3506 | keep-measured | scan | 0.067 | yes | measure/figures/fits.json#barb.bulb_cone_offset |
| `bulb_k` | -0.2775 | mm | -0.2775 | keep-measured | scan | 0.067 | no | measure/figures/fits.json#barb.bulb_cone_offset |
| `bulb_offset` | [0.1744, -0.0616] | mm | [0.1744, -0.0616] | keep-measured | scan | 0.067 | no | measure/figures/fits.json#barb.bulb_cone_offset |
| `cap_R` | 12.1411 | mm | 12.1411 | keep-measured | scan | 0.0349 | no | measure/figures/fits.json#segments.cap_part |
| `cap_axis_c` | [0.1136, -0.1879] | mm | [0.1136, -0.1879] | keep-measured | scan | 0.0349 | no | measure/figures/fits.json#segments.cap_part |
| `cap_axis_tilt` | [2.8553, -1.7752] | deg | [2.8553, -1.7752] | keep-measured | scan | 0.0349 | no | measure/figures/fits.json#segments.cap_part |
| `cap_root_R` | 0.4232 | mm | 0.4232 | keep-measured | scan | 0.0373 | no | measure/figures/fits.json#rounds.cap_root |
| `cap_top_round_R` | 0.5583 | mm | 0.5583 | keep-measured | scan | 0.0381 | no | measure/figures/fits.json#rounds.cap_top_edge |
| `cap_top_u` | 23.2744 | mm | 23.2744 | keep-measured | scan | 0.0584 | no | measure/figures/fits.json#levels.cap_top |
| `latch_cut_d` | [5.4247, 5.5724] | mm | [5.4247, 5.5724] | keep-measured | scan | 0.1 | no | measure/figures/fits_it2.json#latch_windows |
| `latch_cut_y0` | [-4.3929, -4.1991] | mm | [-4.3929, -4.1991] | keep-measured | scan | 0.2 | no | measure/figures/fits_it2.json#latch_windows |
| `latch_cut_y1` | [4.0878, 4.0486] | mm | [4.0878, 4.0486] | keep-measured | scan | 0.2 | no | measure/figures/fits_it2.json#latch_windows |
| `latch_through_theta` | [82.9706, 137.9706] | deg | [82.9706, 137.9706] | keep-measured | scan | 1 | no | measure/figures/fits_it2.json#latch_windows |
| `latch_u_hi` | [-24.168, -24.5909] | mm | [-24.168, -24.5909] | keep-measured | scan | 0.1 | no | measure/figures/fits.json#latch_windows |
| `latch_u_lo` | [-25.3037, -25.2525] | mm | [-25.3037, -25.2525] | keep-measured | scan | 0.1 | no | measure/figures/fits.json#latch_windows |
| `lug_c` | [-0.0033, -0.0477] | mm | [-0.0033, -0.0477] | keep-measured | scan | 0.0524 | no | measure/figures/fits.json#lip |
| `lug_corner_R` | 0.4931 | mm | 0.4931 | keep-measured | scan | 0.0524 | no | measure/figures/fits.json#lip |
| `lug_half_a` | 5.634 | mm | 5.634 | keep-measured | scan | 0.0524 | no | measure/figures/fits.json#lip |
| `lug_half_b` | 5.9639 | mm | 5.9639 | keep-measured | scan | 0.0524 | yes | measure/figures/fits.json#lip |
| `lug_phi_deg` | 23.9706 | deg | 23.9706 | keep-measured | scan | 0.0524 | no | measure/figures/fits.json#lip |
| `lug_u_hi` | -23.1261 | mm | -23.1261 | keep-measured | scan | 0.0287 | no | measure/figures/fits.json#lip.corner_z_p1_p99 |
| `lug_u_lo` | -25.7555 | mm | -25.7555 | keep-measured | scan | 0.0947 | no | measure/figures/fits.json#lip.corner_z_p1_p99 |
| `noz_R` | 5.7799 | mm | 5.7799 | keep-measured | scan | 0.034 | yes | measure/figures/fits.json#segments.nozzle |
| `noz_axis_c` | [-0.0036, 0.0049] | mm | [-0.0036, 0.0049] | keep-measured | scan | 0.034 | no | measure/figures/fits.json#segments.nozzle |
| `noz_axis_tilt` | [-0.6193, -1.2119] | deg | [-0.6193, -1.2119] | keep-measured | scan | 0.034 | no | measure/figures/fits.json#segments.nozzle |
| `noz_bore_R` | 3.9415 | mm | 3.9415 | keep-measured | scan | 0.1022 | yes | measure/figures/fits.json#nozzle_bore |
| `noz_bore_floor_u` | -23.4063 | mm | -23.6878..-23.1248 | keep-measured | scan | 0.3 | no | measure/figures/fits.json#bore_floors.nozzle; intake/coverage.json loop 1 |
| `noz_root_R` | 0.5096 | mm | 0.5096 | keep-measured | scan | 0.054 | no | measure/figures/fits.json#rounds.shoulder_root |
| `noz_tip_round_R` | 0.5227 | mm | 0.5227 | keep-measured | scan | 0.0282 | no | measure/figures/fits.json#rounds.nozzle_tip_outer |
| `noz_tip_u` | -27.3016 | mm | -27.3016 | keep-measured | scan | 0.0362 | no | measure/figures/fits.json#levels.nozzle_tip |
| `nut_R0` | 10.8335 | mm | 10.8335 | keep-measured | scan | 0.0314 | no | measure/figures/fits.json#segments.nut |
| `nut_axis_c` | [-0.067, -0.1553] | mm | [-0.067, -0.1553] | keep-measured | scan | 0.0314 | no | measure/figures/fits.json#segments.nut |
| `nut_chamfer_u0` | -6.7794 | mm | -6.7794 | keep-measured | scan | 0.1208 | no | measure/figures/fits.json#nut_chamfer |
| `nut_k` | 0.0311 | mm | 0.0311 | keep-measured | scan | 0.0314 | no | measure/figures/fits.json#segments.nut |
| `nut_shoulder_u` | -14.037 | mm | -14.037 | keep-measured | scan | 0.0581 | no | measure/figures/fits.json#levels.shoulder |
| `nut_top_rho` | 11.6626 | mm | 11.6626 | keep-measured | scan | 0.1208 | no | measure/figures/fits.json#nut_chamfer |
| `nut_top_u` | -6.15 | mm | -6.15 | keep-measured | scan | 0.1208 | no | measure/figures/fits.json#nut_chamfer; #tables body_frame |
| `oring_a` | 0.9153 | mm | 0.9153 | keep-measured | scan | 0.0889 | yes | measure/figures/fits.json#outlet.oring |
| `oring_rho` | 4.4273 | mm | 4.4273 | keep-measured | scan | 0.0889 | yes | measure/figures/fits.json#outlet.oring |
| `oring_u` | 23.5965 | mm | 23.5965 | keep-measured | scan | 0.0889 | yes | measure/figures/fits.json#outlet.oring |
| `out_bore_R` | 1.5923 | mm | 1.5923 | keep-measured | scan | 0.0987 | no | measure/figures/fits.json#outlet.end_bore |
| `out_bore_floor_u` | 29.2112 | mm | 28.3385..30.0840 | keep-measured | scan | 0.6 | no | measure/figures/fits.json#bore_floors.outlet |
| `out_chamfer_rho0` | 4.3882 | mm | 4.3882 | keep-measured | scan | 0.05 | no | measure/figures/fits.json#outlet.end_chamfer |
| `out_chamfer_slope` | -0.4463 | mm | -0.4463 | keep-measured | scan | 0.05 | no | measure/figures/fits.json#outlet.end_chamfer |
| `out_collar_R` | 6.8482 | mm | 6.8482 | keep-measured | scan | 0.0348 | yes | measure/figures/fits.json#outlet |
| `out_collar_in_u` | 20.0062 | mm | 20.0062 | keep-measured | scan | 0.0542 | no | measure/figures/fits.json#outlet.collar_inner_face |
| `out_collar_out_u` | 22.706 | mm | 22.706 | keep-measured | scan | 0.0324 | no | measure/figures/fits.json#outlet.collar_outer_face |
| `out_collar_round_R` | 1.0766 | mm | 1.0766 | keep-measured | scan | 0.0442 | no | measure/figures/fits.json#outlet.collar_round |
| `out_end_u` | 29.9816 | mm | 29.9816 | keep-measured | scan | 0.0359 | no | measure/figures/fits.json#outlet.end_face |
| `out_root_R` | 0.5272 | mm | 0.5272 | keep-measured | scan | 0.0821 | no | measure/figures/fits.json#outlet.root_round |
| `out_thread_R` | 4.4169 | mm | 4.4169 | keep-measured | scan | 0.1829 | yes | measure/figures/fits.json#outlet.thread_rho |
| `out_thread_pitch` | 0.908 | mm | 0.908 | keep-measured | scan | 0.01 | no | measure/figures/fits.json#outlet.thread_pitch |
| `out_tube_R` | 4.6084 | mm | 4.6084 | keep-measured | scan | 0.05 | no | measure/figures/fits.json#outlet.tube |
| `out_tube_u0` | 5 | mm | 5 | keep-measured | scan | 0 | no | measure/figures/fits.json#outlet |
| `outlet_axis_d` | [1, 0.0048, 0.0076] | mm | [1, 0.0048, 0.0076] | keep-measured | scan | 0.05 | no | measure/figures/fits.json#outlet |
| `outlet_axis_p` | [0.0008, -0.1633, 3.4172] | mm | [0.0008, -0.1633, 3.4172] | keep-measured | scan | 0.05 | no | measure/figures/fits.json#outlet |
| `primary_u` | 0.0002 | mm | 0.0002 | keep-measured | scan | 0.028 | no | measure/figures/fits.json#levels.primary |
| `rib_count` | 8 | count | 8 | keep-measured | scan | 0 | no | measure/figures/count_nut_ribs.json |
| `rib_rho_c` | [10.6615, 10.501, 10.5797, 10.6452, 10.4459, 10.5318, 10.5361, 10.601] | mm | [10.6615, 10.501, 10.5797, 10.6452, 10.4459, 10.5318, 10.5361, 10.601] | keep-measured | scan | 0.1 | no | measure/figures/fits.json#ribs |
| `rib_rod_R` | [1.3415, 1.421, 1.4451, 1.4158, 1.5281, 1.4255, 1.433, 1.3824] | mm | [1.3415, 1.421, 1.4451, 1.4158, 1.5281, 1.4255, 1.433, 1.3824] | keep-measured | scan | 0.1 | no | measure/figures/fits.json#ribs |
| `rib_theta_deg` | [-156.3638, -110.9358, -66.0427, -21.1463, 23.8071, 68.7206, 113.6286, 158.6603] | deg | [-156.3638, -110.9358, -66.0427, -21.1463, 23.8071, 68.7206, 113.6286, 158.6603] | keep-measured | scan | 0.3 | no | measure/figures/fits.json#ribs |
| `ring_R` | 13.2709 | mm | 13.2709 | keep-measured | scan | 0.0512 | no | measure/figures/fits.json#segments.cap_part |
| `ring_bottom_round_R` | 0.8026 | mm | 0.8026 | keep-measured | scan | 0.0785 | no | measure/figures/fits.json#rounds.ring_bottom_outer |
| `ring_bottom_u` | 9.5778 | mm | 9.5778 | keep-measured | scan | 0.0863 | no | measure/figures/fits.json#levels.ring_bottom |
| `ring_top_round_R` | 0.5206 | mm | 0.5206 | keep-measured | scan | 0.0405 | no | measure/figures/fits.json#rounds.ring_top_outer |
| `ring_top_u` | 16.817 | mm | 16.817 | keep-measured | scan | 0.0688 | no | measure/figures/fits.json#levels.ring_top |
| `slit_rho_in` | [10.0568, 10.0127] | mm | [10.0568, 10.0127] | keep-measured | scan | 0.1 | no | measure/figures/fits_it2.json#skirt_slits |
| `slit_rho_out` | [10.7359, 10.6312] | mm | [10.7359, 10.6312] | keep-measured | scan | 0.1 | no | measure/figures/fits_it2.json#skirt_slits |
| `slit_theta0_deg` | [-158.135, 151.6072] | deg | [-158.135, 151.6072] | keep-measured | scan | 1 | no | measure/figures/fits_it2.json#skirt_slits |
| `slit_theta1_deg` | [-140.135, 172.6072] | deg | [-140.135, 172.6072] | keep-measured | scan | 1 | no | measure/figures/fits_it2.json#skirt_slits |
| `slit_u_top` | [10.8622, 10.9502] | mm | [10.8622, 10.9502] | keep-measured | scan | 0.1 | no | measure/figures/fits_it2.json#skirt_slits |
| `web_hw_at_10p5` | 3.5278 | mm | 3.5278 | keep-measured | scan | 0.179 | no | measure/figures/fits.json#outlet_ring_web |
| `web_hw_slope` | -1.3759 | mm | -1.3759 | keep-measured | scan | 0.179 | no | measure/figures/fits.json#outlet_ring_web |
| `web_y_centre` | -0.4327 | mm | -0.4327 | keep-measured | scan | 0.179 | no | measure/figures/fits.json#outlet_ring_web |
| `win_deep_floor_rho` | 10.5134 | mm | 10.5134 | keep-measured | scan | 0.3 | no | measure/figures/fits_it2.json#ring_windows |
| `win_deep_theta` | [104, 116] | deg | [104, 116] | keep-measured | scan | 1 | no | measure/figures/fits_it2.json#ring_windows |
| `win_deep_u` | [12.8, 14] | mm | [12.8, 14] | keep-measured | scan | 0.2 | no | measure/figures/fits_it2.json#ring_windows |
| `win_floor_rho` | [11.9258, 12.1263, 11.4953, 11.9058] | mm | [11.9258, 12.1263, 11.4953, 11.9058] | keep-measured | scan | 0.4 | no | measure/figures/fits_it2.json#ring_windows |
| `win_theta0_deg` | [-74.75, -8.25, 103, 174] | deg | [-74.75, -8.25, 103, 174] | keep-measured | scan | 1 | no | measure/figures/fits_it2.json#ring_windows |
| `win_theta1_deg` | [-58.75, 8.75, 121, -173] | deg | [-58.75, 8.75, 121, -173] | keep-measured | scan | 1 | no | measure/figures/fits_it2.json#ring_windows |
| `win_u_hi` | [14.6, 14, 14.4, 14.2] | mm | [14.6, 14, 14.4, 14.2] | keep-measured | scan | 0.2 | no | measure/figures/fits_it2.json#ring_windows |
| `win_u_lo` | [12.4, 12.4, 12.4, 12.6] | mm | [12.4, 12.4, 12.4, 12.6] | keep-measured | scan | 0.2 | no | measure/figures/fits_it2.json#ring_windows |

## 6. Model tree (design intent)

The STEP is a neutral B-Rep; it carries no feature history. The editable design intent is `build/model.py` driven by `measure/params.json`, and the ordered feature plan is `build/MODELING_PLAN.md`.

_No `feature_tree` was declared in `deliver/limitations.json`; see `build/MODELING_PLAN.md` for the ordered feature plan._

## 7. Tier-1 — caliper dims re-measured on the STEP

**Tier-1 not run: no caliper dimensions exist.** Every dimension is scan authority (or operator spec); see the source column in §5. Absent is not passed.

## 8. Deviation gate (scan ↔ CAD)

Regime **baseline-skill** (`baseline/skills/stl2step-build123d/SKILL.md:87`); bands: p95_mm: 0.3; max_mm: 0.8; tier1_abs_mm: —; interface_max_mm: —.

Registration: point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), iterations 39/60, converged yes, correction 0.0463° / 0.0125 mm.  
Unobservable CAD fraction: 0.0009.

| direction | n | rms | p50 | p95 | p99 | max | sampling | source |
|---|---|---|---|---|---|---|---|---|
| scan → CAD **unmasked** | 300181 | 0.0883 | 0.0417 | 0.1781 | 0.2964 | 1.0854 | — | `qa/gate.json#deviation` |
| scan → CAD (masked) | 297874 | 0.0851 | 0.0414 | 0.175 | 0.2838 | 0.7989 | — | `qa/gate.json#deviation` |
| CAD → scan **unmasked** (all) | 300000 | 0.1855 | 0.0442 | 0.2574 | 0.6246 | 3.2296 | — | `qa/gate.json#deviation` |
| CAD → scan (masked) | 289800 | 0.1011 | 0.0428 | 0.216 | 0.3801 | 0.9956 | — | `qa/gate.json#deviation` |
| CAD → scan (observable) | 19982 | 0.1877 | 0.0441 | 0.2554 | 0.6225 | 3.1203 | — | `qa/gate.json#deviation` |

### Gate results (what the verdict was graded on)

| item | band | measured | result |
|---|---|---|---|
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | p95 0.175 max 0.7989 (n 297874) | PASS |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | p95 0.2554 max 3.1203 (n 19982) | FAIL |
| zone:I1 nozzle spigot OD lugs latch:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.2519 max 0.7989 (n 30997) | PASS |
| zone:I1 nozzle spigot OD lugs latch:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.2935 max 0.8674 (n 32011) | FAIL |
| zone:I2 nozzle shoulder:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.1192 max 0.2019 (n 4185) | PASS |
| zone:I2 nozzle shoulder:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.2064 max 0.4617 (n 13178) | PASS |
| zone:I3 outlet thread and O-ring:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.1679 max 0.7199 (n 18820) | PASS |
| zone:I3 outlet thread and O-ring:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.19 max 0.5637 (n 13896) | PASS |
| zone:I4 barb tube and bulb:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.2044 max 0.7745 (n 16777) | PASS |
| zone:I4 barb tube and bulb:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.1633 max 0.4139 (n 16195) | PASS |
| zone:I5 ring windows:scan_to_cad | p95 ≤0.3 / max ≤0.8 | p95 0.2771 max 0.5616 (n 7053) | PASS |
| zone:I5 ring windows:cad_to_scan | p95 ≤0.3 / max ≤0.8 | p95 0.4533 max 0.9956 (n 6081) | FAIL |

### Per zone (unmasked and masked side by side)

| zone | kind | direction | unmasked | masked | unmasked stats | masked stats | note |
|---|---|---|---|---|---|---|---|
| B1 nozzle bore interior | interior | scan_to_cad | reported | reported | n 1189 · p95 0.3578 · max 0.7359 | n 0 | L1: bore wall seen from the tip to z -26.4..-22.8 (ragged), then open/unscanned |
| B1 nozzle bore interior | interior | cad_to_scan | reported | reported | n 5924 · p95 2.3244 · max 3.2296 | n 0 | L1: bore wall seen from the tip to z -26.4..-22.8 (ragged), then open/unscanned |
| B2 outlet end bore interior | interior | scan_to_cad | reported | reported | n 669 · p95 0.872 · max 1.0854 | n 0 | L3: bore mouth ~1.5 mm deep then open (loop x 28.24-29.96, axis y 0.1 z 3.42) |
| B2 outlet end bore interior | interior | cad_to_scan | reported | reported | n 688 · p95 0.8075 · max 0.9943 | n 0 | L3: bore mouth ~1.5 mm deep then open (loop x 28.24-29.96, axis y 0.1 z 3.42) |
| B3 barb end bore interior | interior | scan_to_cad | reported | reported | n 449 · p95 0.6214 · max 0.7614 | n 0 | L6: bore mouth ~1.6 mm deep then open (loop r 26.71-27.91, theta 53.2-56.1, z 24.0-25.2) |
| B3 barb end bore interior | interior | cad_to_scan | reported | reported | n 465 · p95 0.7702 · max 0.913 | n 0 | L6: bore mouth ~1.6 mm deep then open (loop r 26.71-27.91, theta 53.2-56.1, z 24.0-25.2) |
| I1 nozzle spigot OD lugs latch | whole | scan_to_cad | PASS | PASS | n 30997 · p95 0.2519 · max 0.7989 | n 30997 · p95 0.2519 · max 0.7989 | INTAKE §4 I1, E01-E04; bore r<4.3 excluded (see B1) |
| I1 nozzle spigot OD lugs latch | whole | cad_to_scan | FAIL | FAIL | n 32022 · p95 0.2938 · max 0.8674 | n 32011 · p95 0.2935 · max 0.8674 | INTAKE §4 I1, E01-E04; bore r<4.3 excluded (see B1) |
| I2 nozzle shoulder | whole | scan_to_cad | PASS | PASS | n 4185 · p95 0.1192 · max 0.2019 | n 4185 · p95 0.1192 · max 0.2019 | INTAKE §4 I2, E05 nut bottom face z -14.04 |
| I2 nozzle shoulder | whole | cad_to_scan | PASS | PASS | n 13178 · p95 0.2064 · max 0.4617 | n 13178 · p95 0.2064 · max 0.4617 | INTAKE §4 I2, E05 nut bottom face z -14.04 |
| I3 outlet thread and O-ring | whole | scan_to_cad | PASS | PASS | n 18820 · p95 0.1679 · max 0.7199 | n 18820 · p95 0.1679 · max 0.7199 | INTAKE §4 I3, E13-E15 (u 22.7-30); end bore excluded (see B2) |
| I3 outlet thread and O-ring | whole | cad_to_scan | PASS | PASS | n 13923 · p95 0.1908 · max 0.5637 | n 13896 · p95 0.19 · max 0.5637 | INTAKE §4 I3, E13-E15 (u 22.7-30); end bore excluded (see B2) |
| I4 barb tube and bulb | whole | scan_to_cad | PASS | PASS | n 16777 · p95 0.2044 · max 0.7745 | n 16777 · p95 0.2044 · max 0.7745 | INTAKE §4 I4, E19-E20 protruding part beyond the cap (r>12.6); end bore excluded (see B3) |
| I4 barb tube and bulb | whole | cad_to_scan | FAIL | PASS | n 16312 · p95 0.1682 · max 0.8418 | n 16195 · p95 0.1633 · max 0.4139 | INTAKE §4 I4, E19-E20 protruding part beyond the cap (r>12.6); end bore excluded (see B3) |
| I5 ring windows | whole | scan_to_cad | PASS | PASS | n 7053 · p95 0.2771 · max 0.5616 | n 7053 · p95 0.2771 · max 0.5616 | INTAKE §4 I5, E17 windows at theta -67, 0, 112, 180 (+-15 deg), z 11.8-15.3 |
| I5 ring windows | whole | cad_to_scan | FAIL | FAIL | n 7730 · p95 0.5589 · max 1.0436 | n 6081 · p95 0.4533 · max 0.9956 | INTAKE §4 I5, E17 windows at theta -67, 0, 112, 180 (+-15 deg), z 11.8-15.3 |
| R band | region | scan_to_cad | reported | reported | n 38952 · p95 0.1388 · max 0.3199 | n 38952 · p95 0.1388 · max 0.3199 | — |
| R band | region | cad_to_scan | reported | reported | n 40180 · p95 0.1816 · max 0.7636 | n 40180 · p95 0.1816 · max 0.7636 | — |
| R barb above cap | region | scan_to_cad | reported | reported | n 28940 · p95 0.2036 · max 0.7745 | n 28726 · p95 0.1994 · max 0.7745 | — |
| R barb above cap | region | cad_to_scan | reported | reported | n 23843 · p95 0.2054 · max 0.913 | n 23333 · p95 0.193 · max 0.4139 | — |
| R body outlet web | region | scan_to_cad | reported | reported | n 67870 · p95 0.1604 · max 1.0854 | n 67201 · p95 0.1546 · max 0.7199 | — |
| R body outlet web | region | cad_to_scan | reported | reported | n 62585 · p95 0.2296 · max 0.9943 | n 61865 · p95 0.2123 · max 0.8279 | — |
| R cap | region | scan_to_cad | reported | reported | n 49217 · p95 0.1303 · max 0.7235 | n 48982 · p95 0.1266 · max 0.4893 | — |
| R cap | region | cad_to_scan | reported | reported | n 46920 · p95 0.1436 · max 0.5864 | n 46848 · p95 0.1421 · max 0.5864 | — |
| R nozzle | region | scan_to_cad | reported | reported | n 33536 · p95 0.255 · max 0.7989 | n 32347 · p95 0.2495 · max 0.7989 | — |
| R nozzle | region | cad_to_scan | reported | reported | n 39543 · p95 0.8664 · max 3.2296 | n 33507 · p95 0.3 · max 0.8674 | — |
| R nut | region | scan_to_cad | reported | reported | n 38409 · p95 0.1881 · max 0.4524 | n 38409 · p95 0.1881 · max 0.4524 | — |
| R nut | region | cad_to_scan | reported | reported | n 45081 · p95 0.2198 · max 0.5131 | n 45081 · p95 0.2198 · max 0.5131 | — |
| R ring skirt | region | scan_to_cad | reported | reported | n 43257 · p95 0.1888 · max 0.673 | n 43257 · p95 0.1888 · max 0.673 | — |
| R ring skirt | region | cad_to_scan | reported | reported | n 41848 · p95 0.3088 · max 1.0436 | n 38986 · p95 0.2457 · max 0.9956 | — |

### Masks (masked and unmasked are both shown above)

| mask | direction | why | fraction removed | stats inside |
|---|---|---|---|---|
| M1 unscanned bore interiors | scan_to_cad | the three end bores (nozzle, outlet, barb) were seen only 1.5-4 mm deep; beyond that the scanner bridged them with a membrane (scan side: artefact, not a part surface) and the CAD bore wall/floor has no scan behind it (CAD side: coverage gap). Neither is a surface deviation of the modelled part. | 0.0077 | n: 2307; rms: 0.2801; mean: 0.1944; p50: 0.1296; p95: 0.6356; p99: 0.9169; max: 1.0854 |
| M1 unscanned bore interiors | cad_to_scan | the three end bores (nozzle, outlet, barb) were seen only 1.5-4 mm deep; beyond that the scanner bridged them with a membrane (scan side: artefact, not a part surface) and the CAD bore wall/floor has no scan behind it (CAD side: coverage gap). Neither is a surface deviation of the modelled part. | 0.0236 | n: 7077; rms: 0.9984; mean: 0.6718; p50: 0.354; p95: 2.2511; p99: 2.7593; max: 3.2296 |
| M2 open boundary | cad_to_scan | distance from CAD to a scan hole EDGE (7 open loops: bore mouths, 2 ring windows, 2 skirt slits) is not a surface deviation | 0.0265 | n: 7954; rms: 0.9062; mean: 0.6156; p50: 0.3591; p95: 2.1229; p99: 2.7344; max: 3.2296 |

**CHK-MASK: mask-dependent pass(es):** [whole part scan_to_cad, zone I4 barb tube and bulb cad_to_scan].

### Mask sensitivity

| band | direction | stats | variant |
|---|---|---|---|
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.2854 | scan_to_cad | n: 300181; rms: 0.0883; mean: 0.0605; p50: 0.0417; p95: 0.1781; p99: 0.2964; max: 1.0854 | all masks except M1 unscanned bore interiors |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 1.8946 | cad_to_scan | n: 292046; rms: 0.1139; mean: 0.0684; p50: 0.0429; p95: 0.2184; p99: 0.3887; max: 2.6946 | all masks except M1 unscanned bore interiors |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.2436 | cad_to_scan | n: 292923; rms: 0.1057; mean: 0.0687; p50: 0.0432; p95: 0.2245; p99: 0.4013; max: 1.0436 | all masks except M2 open boundary |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.2436 | cad_to_scan | n: 292765; rms: 0.1047; mean: 0.0684; p50: 0.0431; p95: 0.2235; p99: 0.3977; max: 1.0436 | M2 open boundary radius 0.0 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.1956 | cad_to_scan | n: 291871; rms: 0.1028; mean: 0.0676; p50: 0.043; p95: 0.22; p99: 0.3882; max: 0.9956 | M2 open boundary radius 0.2 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.1956 | cad_to_scan | n: 291271; rms: 0.1021; mean: 0.0673; p50: 0.0429; p95: 0.2184; p99: 0.385; max: 0.9956 | M2 open boundary radius 0.4 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.1956 | cad_to_scan | n: 289800; rms: 0.1011; mean: 0.0668; p50: 0.0428; p95: 0.216; p99: 0.3801; max: 0.9956 | M2 open boundary radius 0.8 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.1956 | cad_to_scan | n: 285998; rms: 0.0991; mean: 0.0658; p50: 0.0424; p95: 0.2112; p99: 0.3738; max: 0.9956 | M2 open boundary radius 1.5 mm |
| p95_band: 0.3; max_band: 0.8; pass: no; max_over_by: 0.1956 | cad_to_scan | n: 274827; rms: 0.0972; mean: 0.0647; p50: 0.0419; p95: 0.2068; p99: 0.3678; max: 0.9956 | M2 open boundary radius 2.5 mm |

### Over-band point clusters, scan → CAD (> 0.8 mm)

48 points (0.0002 fraction) in 1 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 48 | [28.3, -0.203, 2.458] | [28.137, 28.431] | [0.1, 360] | 1.0854 | outlet end bore (L3): scanner bridge membrane curling into the bore at x 28.1-28.4, 48 pts, max 1.085 (zoom 'outlet end theta=0'); scanner artefact inside declared mask M1. Unchanged from it1 (the outlet was not rebuilt). The it1 latch cluster is gone. |

### Over-band point clusters, CAD → scan (> 0.8 mm)

2204 points (0.0073 fraction) in 4 clusters ≥ 20 pts.

| # | n | centroid | r range | θ range (deg) | d max | explanation |
|---|---|---|---|---|---|---|
| 0 | 2069 | [0.785, -1.302, -23.673] | [0.202, 3.991] | [0.2, 359.9] | 3.2296 | **UNEXPLAINED** |
| 1 | 39 | [-11.928, -0.711, 14.717] | [11.909, 12.328] | [174.6, 187.5] | 1.0436 | **UNEXPLAINED** |
| 2 | 35 | [29.227, 0.93, 4.721] | [29.2, 29.357] | [0.8, 3] | 0.9943 | **UNEXPLAINED** |
| 3 | 20 | [15.973, 22.156, 25.761] | [27.272, 27.388] | [52.9, 56] | 0.913 | **UNEXPLAINED** |

**Datum audit (report-only, QUESTIONS Q2):** angle 0.0178°, origin offset 0.0072 mm, point disagreement p95 0.0139 mm; reference band ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) (within).

## 9. Band miss: where and what next

| region | cause | options |
|---|---|---|
| cad_to_scan_observable (whole part) - nozzle bore floor and far bore wall (B1, M1) | max 3.120: the CAD bore floor (at the scanner bridge) and the bore wall at theta ~280-340 above z -26 have no scan behind them; the scan's bore wall ends at the ragged mouth z ~-26.1 on that side (qa/overlays/zoom_it2_extra.png 'bore far wall theta=300/315'). COVERAGE FACT, not a through-window error: the through-window cut itself fits the scan (bore wall on the window side theta 60-160 c2s p50 0.04-0.23, max 0.46), and the far wall is the unchanged it1 bore cylinder whose radius matches the scanned wall below z -26 (p50 0.15). The it2 window only opens a new ray path to it, which the OD-H22 #3 ray-test defect then counts as observable. | A) owner ACCEPT-BAND citing this gate hash and 'cad_to_scan_observable'; B) fix the observability test to be scan-coverage-aware / compose declared masks (skill defect) and re-grade; C) sectioned part or depth reading of the bore. |
| zone I1 nozzle spigot, CAD->scan (latch through-window edge, theta ~83, r 4.7, z -24.1) | max 0.867 on 2 points: the upper face of the new through-window near its theta-83 edge sits ~0.87 mm from the scan, whose surface there is the bridge membrane sagging into the window (zoom 'latch edge theta=83'). Scanner fact (membrane), not a fixable geometry error; scan->CAD in I1 now passes (0.799). | accept (ACCEPT-BAND, 'zone:I1'), or a caliper/photo with scale of the latch slot height to arbitrate; no further rebuild recommended (it would follow a membrane). |
| zone I5 ring windows, CAD->scan (windows near theta 121 and 285) | masked p95 0.453 / max 0.996 (unmasked p95 0.559 / max 1.044). The CAD window floors and walls lie behind scanner bridge membranes: at theta 121 and 285 the scanned skirt sags 0.3-0.4 mm inward exactly over the window z-span (13-15 and 12-14), i.e. a membrane across an opening, not closed skirt (zoom 'ring window theta=121/285'); the window at 290 is scanned open and matches the CAD. Scanner fact. scan->CAD in I5 now passes (p95 0.277 / max 0.562). | accept (ACCEPT-BAND, 'zone:I5'), or caliper the window width/height; modelling the CAD to the membrane would model an artefact. |
| outlet collar / O-ring junction (theta ~8, x 22.7, z 0.4; outside I3) | 6 CAD points up to 0.828 at the fused O-ring-to-collar fill (declared invented connection, MODELING_PLAN §6 / L5); present in it1 too (1 pt 0.846). Declared simplification, not a coverage defect; it does not decide any gated result on its own (the gated CAD->scan term is already over band from the bore floor). | keep as declared (L5), or model the O-ring as a separate body. |

Missed band(s): `cad_to_scan_observable: p95 0.255 max 3.120 vs 0.3/0.8`; `zone:I1 nozzle spigot OD lugs latch:cad_to_scan: p95 0.293 max 0.867 vs 0.3/0.8`; `zone:I5 ring windows:cad_to_scan: p95 0.453 max 0.996 vs 0.3/0.8`.

## 10. Named checks

| check | stage | ran | result | note |
|---|---|---|---|---|
| CHK-ACHIEVABLE | verify (`qa/gate.json#checks`) | yes | n/a | no Tier-1 (scan-only, no calipers) |
| CHK-CIRCULAR | verify (`qa/gate.json#checks`) | yes | pass | datum not ICP'd to own CAD; QA T_refine (qa/registration.json) is QA-only and not written back; no expected value taken from the builder. The builder's build/selfcheck.json (frozen datum, no ICP) is a consistency check, not independent evidence. |
| CHK-CLUSTER | verify (`qa/gate.json#checks`) | yes | pass | 1 scan->CAD over-band clusters; unexplained: [] |
| CHK-ENUM | verify (`qa/gate.json#checks`) | yes | pass | every INTAKE feature E01-E25 exists in the CAD; every photographed feature present. it2 fixed the three it1 extent findings: latch now a through-window (photo_2 slot), slits trimmed (no CAD pocket at theta 147 / 229.5), window near 110 deepened to the gap. Remaining window/latch residuals sit behind scanner bridge membranes (see miss_explanations). |
| CHK-FILLET | verify (`qa/gate.json#checks`) | yes | pass | export_check.json fillets: [] (0 3D fillet ops, as MODELING_PLAN §5 plans: every round is a profile arc); nothing silently skipped or reduced |
| CHK-INDEP | verify (`qa/gate.json#checks`) | yes | pass | fresh context; see independence |
| CHK-LIKE4LIKE | verify (`qa/gate.json#checks`) | yes | pass | it1 (_it1_SUPERSEDED/qa/gate.json dd052135f7c2) vs it2 use the identical protocol: same regime.json, byte-identical zones.json and masks.json (declared at it1, before any number), same ICP params (39 its both), same deviation sampling/seeds, same observability params, same QA tessellation (0.005/0.05), same run-local helpers (obs chunk 64). Every it1->it2 delta is geometry, not protocol. |
| CHK-MASK | verify (`qa/gate.json#checks`) | yes | finding | whole part scan_to_cad; zone I4 barb tube and bulb cad_to_scan |
| CHK-OVERLAY | verify (`qa/gate.json#checks`) | yes | pass | every panel shows scan |
| CHK-PATCHWORK | verify (`qa/gate.json#checks`) | yes | pass | QA census it2: 146 faces, 100 % analytic (plane 80, cylinder 33, cone 22, torus 11), 0 B-spline/ruled; model.py grep: no loft/sweep/spline; the same 2 make_polygon calls as it1 (4-pt rectangle model.py:112, 5-pt web model.py:238) |
| PHOTO-PLAUSIBILITY | verify (`qa/gate.json#checks`) | yes | pass | photo_1, photo_2 (catalogue, no scale): nozzle with tip slot, 8-rib nut, band, body, side outlet with collar, black O-ring and thread, cap ring with rectangular windows, cap, hose barb - all present in CAD. Declared simplifications visible in photos: thread modelled as plain cylinder, O-ring fused to the outlet. |
| CHK-PUBLISH | deliver (preflight) | yes | pass | verdict BAND_NOT_MET |
| CHK-SUPERSEDED | deliver (preflight) | yes | pass | all earlier iterations kept intact |
| inputs_unchanged | deliver (preflight) | yes | pass | 3 input file(s) unchanged |
| hash_frozen | deliver (preflight) | yes | pass | every build/ STEP matches hash_frozen |
| regime_declared | deliver (preflight) | yes | pass | regime 'baseline-skill' |

## 11. Declared limitations (each with its re-run trigger)

| id | limitation | re-run trigger | evidence |
|---|---|---|---|
| L1 | no Tier-1 (no calipers run): scan-only job, no caliper readings supplied (DECISIONS MEASUREMENTS). Every caliper-coverable dimension is ABSENT, not passed. | any caliper reading (nozzle OD, lug span, thread OD, O-ring OD, barb OD, window width) triggers a Tier-1 run and a re-grade | qa/gate.json#tier1; DECISIONS.md MEASUREMENTS |
| L2 | Absolute scale is UNVERIFIED (CHK-SCALE flag at intake): units assumed mm, no scale applied. | one caliper reading of any dimension | intake/INTAKE_CARD.md; intake/alignment.json#scale_factor |
| L3 | scan_resolution = full is an agent inference from face count and mean edge length, not owner-confirmed; the gate is labelled OFFICIAL on that inference. | owner confirms the scan is the original export; if it is decimated, the grade becomes inspection-only and is redone on the original | DECISIONS.md OTHER scan_resolution; input/INPUT_HASHES.json#scan_resolution |
| L4 | MASKED PASS, mask-dependent pass: bore interiors (nozzle, outlet, barb) and all internal passages were bridged or never reached by the scanner; named mask M1 removes them. Whole-part scan to CAD passes only masked (max 0.7989, right at the band and fragile); unmasked max is 1.0854 at the outlet bore bridge membrane. The zone I4 barb CAD to scan pass is also mask-dependent. Bores stop at the observed scanner bridge; the real bores continue. | a sectioned part, a CT scan or depth-gauge readings of the three bores | qa/gate.json#deviation.masks; qa/gate.json#auto_limitations; qa/VERDICT.md |
| L5 | NOT A FUNCTIONAL FLOW PART, ASSUMED assembly pose: the assembly was scanned as one closed shell. Sub-part poses are kept as scanned (the nozzle and the cap part sit on their own tilted axes), the O-ring is fused into the single solid (invented connection), the outlet thread is a plain cylinder at the fitted diameter (pitch recorded for identification only), and no internal passages, seat or spring are modelled. | owner asks for a nominal coaxial design, separate parts, a real thread, or supplies the internal geometry | build/MODELING_PLAN.md §1, §6; measure/params.json#out_thread_pitch |
| L6 | NOT MET, cad_to_scan_observable: the observability ray test counts CAD surfaces inside open-mouthed bores, windows and slits as observable although no scan covers them, so the gated term holds the unscanned nozzle bore floor and far bore wall (max 3.1203, p95 0.2554 passes). Zone I1 (latch edge) and zone I5 (ring windows) CAD to scan misses come from scanner bridge membranes over the openings; the independent verifier found no rebuild target left. Accepted by the owner (ACCEPT-BAND). | a scan-coverage-aware observability test, or a rescan that reaches into the bores and windows, triggers a re-grade | qa/gate.json#band_fails; qa/gate.json#miss_explanations; qa/residual_analysis.json; decisions/accept_band.md |
| L7 | Origin definition: the as-built origin is the nozzle axis at its measured mid-station projected along the band normal; the literal intersection of the tilted nozzle axis with the band plane lies a fraction of a millimetre away. The datum audit (report-only) agrees with alignment.json; no effect on the deviation. | owner states which origin definition downstream users need | qa/datum_supplement.json; qa/gate.json#datum_audit |

## 12. Assumptions and invented geometry

- Sub-body stubs inside neighbouring bodies (nozzle stub above the shoulder, body top inside the ring, outlet tube start, groove fill under the O-ring) are construction extents inside material, not visible surfaces. _(source: assumed; build/MODELING_PLAN.md §6)_
- Bore, window and latch pocket floors are placed at the observed scanner bridge / floor; the real openings continue beyond what was scanned. _(source: assumed; build/MODELING_PLAN.md §6)_
- The O-ring is joined to the outlet groove to make one solid; the joint itself is invented. _(source: assumed; build/MODELING_PLAN.md §6)_

## 13. Claim boundary — what this result is NOT

- **Not fit for:** functional flow use or as a working valve: internal passages, seat and spring are not modelled
- **Not fit for:** manufacture, tooling or fit-critical interfaces (nozzle snap, outlet thread, O-ring gland, barb) until calipered: Tier-1 absent, scale unverified
- **Not fit for:** a thread specification: the outlet thread is a plain cylinder
- Fit for: external envelope, packaging and clearance studies
- Fit for: visualisation and as a design-intent reference for the outer geometry
- Fit for: a starting model for a parametric redesign (every dimension is a named parameter in build/model.py and measure/params.json)
- The verdict covers only the Tier-1, deviation and named-check gates above, under the **baseline-skill** regime.

- Verify's own claim boundary (`qa/gate.json#claim_boundary`): Outer-envelope reconstruction of a scanned assembly (one fused solid, sub-parts as scanned). Not a functional flow part (internal passages, valve seat, spring not modelled), not caliper-verified in scale or any dimension, bore depths are scanner-bridge depths, window/latch floors behind scanner membranes are unverified, thread is a plain cylinder. Not fit for tooling, moulding, fits or thread engagement until calipered; fit for visual/envelope/packaging use only after a recorded ACCEPT-BAND.

## 14. Human acceptance of the band miss

Accepted by **Ikbal (owner, session message "del'ver")** on 2026-09-28 (`DECISIONS.md`, ACCEPT-BAND): Accept and deliver: accepts cad_to_scan_observable, zone:I1 nozzle spigot OD lugs latch:cad_to_scan and zone:I5 ring windows:cad_to_scan band misses, gate a7a0a18a5df9 (created 2026-09-28T14:32:56+00:00); remaining misses are unscanned bore floor and scanner bridge membranes, no rebuild target left per independent verify it2.. Record: `decisions/accept_band.md` (sha256 `7e15165fdaaa4ca0accd104405c8d970c63a82723806be20269d95fce680ccf7`).

## 15. Reproduction

```
cd build && python model.py
python <skills>/stl-re-deliver/scripts/repro_check.py --run <run>
```

Fresh-process rebuild check (`deliver/repro.json`): reproducible **yes**; method 2 fresh subprocess rebuild(s) of build/model.py in a scratch copy; STEP re-imported; solids, faces, surface census, volume, bbox compared (raw hash reported, not required); environment python: 3.11.15; platform: Linux-6.18.44-fc-v37-x86_64-with-glibc2.39; build123d: 0.13.0; OCP: 8.0.1.0; numpy: 2.4.6.

| file | volume mm³ | |Δ volume| | max |Δ bbox| | faces equal | identical | raw sha equal |
|---|---|---|---|---|---|---|
| OD-H21_antidrip-valve.step | 19376.4953 | 0 | 0 | yes | yes | no |
| OD-H21_antidrip-valve_datum.step | 19376.4953 | 0 | 0 | yes | yes | no |

_Raw STEP hashes differ between runs because STEP headers carry a timestamp; the geometry is compared._

## 16. Provenance of every number in this file

| file | sha256 |
|---|---|
| `qa/gate.json` | a7a0a18a5df9d7e109b33b1bd5e877bc1d161fb8a48049a08c7ce841fe7123b3 |
| `measure/params.json` | 856833293b94d48ce2f63a8b335f872dd550530a8b8aef8003e8ef2e61f53d1d |
| `build/export_check.json` | e7b7e3bb094c3bbe5287411495612b972d85c6f5610b621b2691c9d2722a2f69 |
| `intake/alignment.json` | b1976a9df8d163ce442e397ccd163ee51e48c4abb2e477a0399be89a9008ed4a |
| `deliver/repro.json` | 18459870b94bd498c18565c76743acc1fbdaede7c8850799f34749baff4c7b49 |
| `deliver/limitations.json` | f2e19b5190a65b9e7160a6e6757f6a77bda74ad18ce8b637d2e0b3ba3e3f5989 |

Generated by `stl-re-deliver/scripts/make_readme.py`. Do not edit numbers by hand; fix the JSON and re-render.
