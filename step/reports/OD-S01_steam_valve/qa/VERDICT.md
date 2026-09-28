# VERDICT: BAND_NOT_MET

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: Fresh QA agent (iteration 2) that did not build the model; every gate number re-derived with the stl-re-verify scripts on the full-resolution input/scan.stl (own ICP, own tessellation of the frozen STEP). Not read: build/selfcheck/, build/build_log.txt, measure/params.json values (only #simplifications, to name declared simplifications), _it1_SUPERSEDED/build/selfcheck; build/model.py only grepped for loft|ruled|Polyline. build/MODELING_PLAN.md quotes builder self-check aggregates; they were not used as expectations. Datum spec, zones and masks are the it1 QA files reused verbatim (CHK-LIKE4LIKE), fixed before any it2 deviation number existed. qa/probe/*.py are QA-only localisation aids, never gate numbers.

Scan: `input/scan.stl` (full-res), label **OFFICIAL (full-res)**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-S01_steam-valve_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 15837.550 mm³ | PASS |
| Validity `OD-S01_steam-valve.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 15837.550 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 0.256° / origin 0.166 mm / points p95 0.188 max 0.231 mm | outside (not blocking) |
| Registration (ICP) | converged | 41/60 its, 0.134° / 0.064 mm | PASS |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 250308 · rms 0.213 · p50 0.075 · p95 0.449 · p99 0.813 · max 1.940 | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 19446 · rms 0.357 · p50 0.077 · p95 0.761 · p99 1.632 · max 2.890 | FAIL |
| zone:Z1_spindle:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 16768 · rms 0.160 · p50 0.090 · p95 0.284 · p99 0.460 · max 1.338 | FAIL |
| zone:Z2_cap_cam_ring:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 46719 · rms 0.265 · p50 0.092 · p95 0.615 · p99 0.970 · max 1.593 | FAIL |
| zone:Z3_top_clip_port:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 17649 · rms 0.206 · p50 0.111 · p95 0.425 · p99 0.582 · max 0.890 | FAIL |
| zone:Z4_side_ports:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 42323 · rms 0.137 · p50 0.060 · p95 0.272 · p99 0.563 · max 0.956 | FAIL |
| zone:Z5_barb:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 7270 · rms 0.089 · p50 0.051 · p95 0.152 · p99 0.302 · max 0.764 | PASS |
| zone:Z6_microswitch:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 25290 · rms 0.226 · p50 0.099 · p95 0.474 · p99 0.719 · max 0.883 | FAIL |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 250308 · rms 0.213 · p50 0.075 · p95 0.449 · p99 0.813 · max 1.940
- scan→CAD masked: n 250308 · rms 0.213 · p50 0.075 · p95 0.449 · p99 0.813 · max 1.940
- CAD→scan unmasked: n 300000 · rms 0.405 · p50 0.080 · p95 0.934 · p99 1.762 · max 3.465
- CAD→scan masked: n 279090 · rms 0.355 · p50 0.073 · p95 0.777 · p99 1.557 · max 3.465
- CAD→scan observable only: n 19446 · rms 0.357 · p50 0.077 · p95 0.761 · p99 1.632 · max 2.890; unobservable fraction 2.77 %

Masks:

- **M1 open boundary** (cad_to_scan): a CAD point whose nearest scan point lies within 0.8 mm of a scan hole edge measures the distance to the edge of a coverage gap (22 open loops: port-web orifices, bore interiors, column windows, cap slots), not a surface deviation; fraction 6.97 %; inside n 20910 · rms 0.817 · p50 0.444 · p95 1.757 · p99 2.518 · max 3.465

Zones:

- Z1_spindle [whole] scan_to_cad: unmasked n 16768 · rms 0.160 · p50 0.090 · p95 0.284 · p99 0.460 · max 1.338 | masked n 16768 · rms 0.160 · p50 0.090 · p95 0.284 · p99 0.460 · max 1.338
- Z2_cap_cam_ring [whole] scan_to_cad: unmasked n 46719 · rms 0.265 · p50 0.092 · p95 0.615 · p99 0.970 · max 1.593 | masked n 46719 · rms 0.265 · p50 0.092 · p95 0.615 · p99 0.970 · max 1.593
- Z3_top_clip_port [whole] scan_to_cad: unmasked n 17649 · rms 0.206 · p50 0.111 · p95 0.425 · p99 0.582 · max 0.890 | masked n 17649 · rms 0.206 · p50 0.111 · p95 0.425 · p99 0.582 · max 0.890
- Z4_side_ports [whole] scan_to_cad: unmasked n 42323 · rms 0.137 · p50 0.060 · p95 0.272 · p99 0.563 · max 0.956 | masked n 42323 · rms 0.137 · p50 0.060 · p95 0.272 · p99 0.563 · max 0.956
- Z5_barb [whole] scan_to_cad: unmasked n 7270 · rms 0.089 · p50 0.051 · p95 0.152 · p99 0.302 · max 0.764 | masked n 7270 · rms 0.089 · p50 0.051 · p95 0.152 · p99 0.302 · max 0.764
- Z6_microswitch [whole] scan_to_cad: unmasked n 25290 · rms 0.226 · p50 0.099 · p95 0.474 · p99 0.719 · max 0.883 | masked n 25290 · rms 0.226 · p50 0.099 · p95 0.474 · p99 0.719 · max 0.883
- Z1_spindle_c2s [region] cad_to_scan: unmasked n 12347 · rms 0.139 · p50 0.074 · p95 0.289 · p99 0.471 · max 0.785 | masked n 12171 · rms 0.136 · p50 0.074 · p95 0.282 · p99 0.436 · max 0.605
- Z2_cap_cam_ring_c2s [region] cad_to_scan: unmasked n 57601 · rms 0.266 · p50 0.085 · p95 0.619 · p99 0.973 · max 1.651 | masked n 52376 · rms 0.227 · p50 0.077 · p95 0.547 · p99 0.840 · max 1.218
- Z3_top_clip_port_c2s [region] cad_to_scan: unmasked n 18680 · rms 0.366 · p50 0.161 · p95 0.761 · p99 1.295 · max 2.097 | masked n 17265 · rms 0.338 · p50 0.151 · p95 0.666 · p99 1.220 · max 2.097
- Z4_side_ports_c2s [region] cad_to_scan: unmasked n 58236 · rms 0.222 · p50 0.061 · p95 0.447 · p99 0.999 · max 1.752 | masked n 55242 · rms 0.172 · p50 0.057 · p95 0.323 · p99 0.773 · max 1.731
- Z5_barb_c2s [region] cad_to_scan: unmasked n 11005 · rms 0.650 · p50 0.071 · p95 1.322 · p99 1.364 · max 1.631 | masked n 10369 · rms 0.644 · p50 0.065 · p95 1.322 · p99 1.358 · max 1.631
- Z6_microswitch_c2s [region] cad_to_scan: unmasked n 18494 · rms 0.181 · p50 0.067 · p95 0.402 · p99 0.692 · max 0.912 | masked n 18424 · rms 0.181 · p50 0.067 · p95 0.403 · p99 0.692 · max 0.912
- I1_top_bore_interior [interior] scan_to_cad: unmasked n 2725 · rms 0.263 · p50 0.187 · p95 0.516 · p99 0.661 · max 0.890 | masked n 2725 · rms 0.263 · p50 0.187 · p95 0.516 · p99 0.661 · max 0.890
- I1_top_bore_interior [interior] cad_to_scan: unmasked n 3034 · rms 1.084 · p50 0.496 · p95 2.289 · p99 2.673 · max 2.898 | masked n 1239 · rms 0.907 · p50 0.385 · p95 1.960 · p99 2.375 · max 2.651
- I2_column_windows_below_switch [interior] scan_to_cad: unmasked n 808 · rms 0.306 · p50 0.122 · p95 0.722 · p99 0.911 · max 1.069 | masked n 808 · rms 0.306 · p50 0.122 · p95 0.722 · p99 0.911 · max 1.069
- I2_column_windows_below_switch [interior] cad_to_scan: unmasked n 1706 · rms 0.560 · p50 0.188 · p95 1.302 · p99 1.477 · max 1.583 | masked n 734 · rms 0.356 · p50 0.149 · p95 0.697 · p99 1.162 · max 1.401
- B1_z_below_0 [region] scan_to_cad: unmasked n 16768 · rms 0.160 · p50 0.090 · p95 0.284 · p99 0.460 · max 1.338 | masked n 16768 · rms 0.160 · p50 0.090 · p95 0.284 · p99 0.460 · max 1.338
- B1_z_below_0 [region] cad_to_scan: unmasked n 12347 · rms 0.139 · p50 0.074 · p95 0.289 · p99 0.471 · max 0.785 | masked n 12171 · rms 0.136 · p50 0.074 · p95 0.282 · p99 0.436 · max 0.605
- B2_z_0_8p2 [region] scan_to_cad: unmasked n 46719 · rms 0.265 · p50 0.092 · p95 0.615 · p99 0.970 · max 1.593 | masked n 46719 · rms 0.265 · p50 0.092 · p95 0.615 · p99 0.970 · max 1.593
- B2_z_0_8p2 [region] cad_to_scan: unmasked n 57601 · rms 0.266 · p50 0.085 · p95 0.619 · p99 0.973 · max 1.651 | masked n 52376 · rms 0.227 · p50 0.077 · p95 0.547 · p99 0.840 · max 1.218
- B3_z_8p2_15p4 [region] scan_to_cad: unmasked n 31120 · rms 0.219 · p50 0.081 · p95 0.472 · p99 0.798 · max 1.559 | masked n 31120 · rms 0.219 · p50 0.081 · p95 0.472 · p99 0.798 · max 1.559
- B3_z_8p2_15p4 [region] cad_to_scan: unmasked n 37793 · rms 0.506 · p50 0.104 · p95 1.132 · p99 2.314 · max 3.465 | masked n 33817 · rms 0.431 · p50 0.090 · p95 0.831 · p99 2.061 · max 3.465
- B4_z_15p4_27p7 [region] scan_to_cad: unmasked n 84036 · rms 0.196 · p50 0.074 · p95 0.424 · p99 0.710 · max 1.940 | masked n 84036 · rms 0.196 · p50 0.074 · p95 0.424 · p99 0.710 · max 1.940
- B4_z_15p4_27p7 [region] cad_to_scan: unmasked n 102894 · rms 0.386 · p50 0.074 · p95 0.856 · p99 1.807 · max 3.001 | masked n 97957 · rms 0.336 · p50 0.070 · p95 0.616 · p99 1.604 · max 3.001
- B5_z_27p7_43p4 [region] scan_to_cad: unmasked n 54016 · rms 0.201 · p50 0.054 · p95 0.312 · p99 1.050 · max 1.877 | masked n 54016 · rms 0.201 · p50 0.054 · p95 0.312 · p99 1.050 · max 1.877
- B5_z_27p7_43p4 [region] cad_to_scan: unmasked n 70685 · rms 0.496 · p50 0.065 · p95 1.294 · p99 1.909 · max 2.920 | masked n 65504 · rms 0.444 · p50 0.059 · p95 1.266 · p99 1.729 · max 2.920
- B6_z_above_43p4 [region] scan_to_cad: unmasked n 17649 · rms 0.206 · p50 0.111 · p95 0.425 · p99 0.582 · max 0.890 | masked n 17649 · rms 0.206 · p50 0.111 · p95 0.425 · p99 0.582 · max 0.890
- B6_z_above_43p4 [region] cad_to_scan: unmasked n 18680 · rms 0.366 · p50 0.161 · p95 0.761 · p99 1.295 · max 2.097 | masked n 17265 · rms 0.338 · p50 0.151 · p95 0.666 · p99 1.220 · max 2.097

Over-band scan→CAD points (> 0.8 mm): 2638 (1.054 %) in 26 clusters ≥ 20 pts.

- cluster 0: n 790, centroid [-1.847, 6.56, 29.085], r [5.297, 8.329], θ [98.1, 121.0], max 1.940 — NEW IN IT2, REAL GEOMETRY ERROR (CAD excess, fixable). Upper side port junction box by the neck: 790 scan points all INSIDE the CAD (mean scan normal -X/-Y), x -3.2..-1.0, y 4.7..7.7, z 27.3..32.3, up to 1.94 mm. The it2 junction box (x -4..-0.12, MODELING_PLAN F10) fills the space between the port underside and the neck where the scan shows a sloped -X-facing wall running from the port (y ~7.7) down to the neck (r ~5.3). Overlays Z=29, Z=30.8 (CAD rectangle vs scan diagonal), y=6.0, x=-2.0. The it1 end-wall cluster at x ~-0.1 is gone, but this box over-fills. Largest single cluster; the scan->CAD max comes from here.
- cluster 1: n 381, centroid [-7.999, 5.547, 7.838], r [8.564, 12.011], θ [135.9, 149.2], max 1.593 — DECLARED SIMPLIFICATION, still over band. Shoulder block on post 120, sloped top: 381 pts INSIDE the CAD (was 657 in it1), theta 136..149, r 8.6..12.0, z 4.2..11.6, up to 1.59 mm, scan normal outward/up. The it2 planar slope (params simplifications 'shoulder block upper shell') does not follow the scanned surface near its lower/outer edge; overlays radial 135, x=-7, y=6.0.
- cluster 2: n 196, centroid [-1.087, 9.857, 6.592], r [9.446, 10.822], θ [93.2, 99.5], max 1.542 — DECLARED SIMPLIFICATION ('cam x~0 step walls ... not modelled'), same as it1 cluster 6: +X-facing step wall at x -1.6..-0.6, theta 93..100, z 5.9..7.4, 196 pts INSIDE the CAD, up to 1.54 mm. Overlays radial 96, Z=6.5.
- cluster 3: n 134, centroid [-0.412, -10.311, 6.459], r [9.62, 11.171], θ [266.0, 269.0], max 1.207 — DECLARED SIMPLIFICATION, same as it1 cluster 7: cam x~0 step wall at theta 266..269, z 4.7..7.5, 134 pts INSIDE the CAD, up to 1.21 mm. Overlay radial 270.
- cluster 4: n 120, centroid [1.097, 8.92, 21.342], r [8.165, 10.744], θ [74.6, 87.3], max 1.356 — CAD EXCESS at the switch-holder / +Y bracket junction, unchanged from it1 cluster 11 (120 pts INSIDE the CAD, x 0.4..2.5, y 8.2..10.7, z 18.4..22.5, up to 1.36 mm); the it2 holder opening did not reach this face. c2s cluster 7 (x 2.3..3.9, y 7.7..8.3, up to 2.49 mm) is the same CAD material with no scan behind it. Overlays Z=18, Z=23, radial 80.
- cluster 5: n 91, centroid [8.852, 4.075, 6.788], r [9.375, 10.46], θ [14.3, 28.6], max 1.275 — CAM RING FLANK (declared 'cam ring flanks and edges ... 0.3..1.0 mm'): post/tooth flank at theta 14..29, r 9.4..10.5, z 5.9..7.4, 91 pts INSIDE the CAD, up to 1.27 mm (CAD flank placed ~1 mm into the scanned pocket). Overlays radial 20, Z=6.5.
- cluster 6: n 82, centroid [-0.779, 10.384, 3.269], r [9.96, 10.883], θ [92.7, 95.8], max 1.316 — DECLARED SIMPLIFICATION, cam x~0 step wall family (theta 93..96, z 2.7..4.0, 82 pts INSIDE the CAD, up to 1.32 mm), lower level of cluster 2.
- cluster 7: n 64, centroid [-10.12, 16.353, 32.313], r [18.207, 20.158], θ [120.3, 123.4], max 0.911 — DECLARED SIMPLIFICATION ('port plate inner-edge lips and hooks'): upper port clip plate edge at x -10.8..-9.3, y 15.6..17.1, z 31.6..33.0, 64 pts OUTSIDE the CAD, up to 0.91 mm (lip not modelled). Overlay y=12.9 / Z=30.8.
- cluster 8: n 63, centroid [8.223, -4.054, 17.783], r [8.731, 9.856], θ [331.7, 335.4], max 1.041 — HOLDER FACE (fixable, small): scan face y ~-4.05 (normal -Y) at x 7.7..8.9, z 17.1..19.3 lies INSIDE the CAD: the CAD holder/fin -Y face stands ~0.9 mm proud of the scan here, 63 pts, up to 1.04 mm. Overlay Z=18.
- cluster 9: n 61, centroid [-1.662, -11.813, 22.984], r [11.297, 12.756], θ [257.9, 265.3], max 1.253 — LOWER PORT JUNCTION (fixable, same family as cluster 0): x -2.7..-0.9, y -12.5..-11.3, z 22.2..23.4, 61 pts INSIDE the CAD, up to 1.25 mm - top edge of the it2 lower junction box; c2s clusters 0/8 are the matching CAD-with-no-scan. Overlay Z=23.
- cluster 10: n 61, centroid [-0.8, -0.161, -13.681], r [0.421, 1.121], θ [126.0, 233.3], max 1.338 — DECLARED NOT MODELLED: spindle tip hole (r 0.4..1.1, z -13.9..-13.4), 61 pts INSIDE the CAD (CAD solid where the scan has a hole), up to 1.34 mm. INTAKE E01 'tip hole ... not modelled'; photos 2/4 show it. Would need a ~r0.9 hole of known depth (depth partly unscanned).
- cluster 11: n 52, centroid [-2.802, 9.312, 11.205], r [9.493, 10.082], θ [104.6, 108.3], max 1.300 — COLLAR / SHOULDER-BLOCK EDGE (fixable, small): theta 105..108, r 9.5..10.1, z 10.9..11.6, 52 pts INSIDE the CAD, up to 1.30 mm - the collar sector edge next to the post-120 block stands proud of the scan (CAD excess). Overlays radial 110, Z=11.5.

## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | pass | no pass depends on a mask |
| CHK-CLUSTER | pass | 12 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | pass | grading gate = QA's own ICP on the raw full-res scan against the frozen it2 STEP; T_refine is QA-only and not written back to intake/alignment.json; no expected value taken from params.json. Builder self-check numbers in MODELING_PLAN §8 are a consistency check, not independent evidence, and were not used. |
| CHK-LIKE4LIKE | pass | it1 vs it2 use the same protocol: same regime file content, same scan (sha256 98cd1183...), identical alignment matrix (max abs diff 0.0; the alignment.json hash differs only by its re-written header), same datum_spec/zones/masks (copied verbatim), same ICP parameters (3M/seed 11, 300k/seed 13, 70 deg, 0.8 mm, 3.0 mm, cap 60, tol 1e-6), same deviation sampling (all scan verts, 300k CAD samples seed 2, k 8, n_samp 3M, seed 0; observability 20k seed 5, 0.5 mm, 60 deg), same tessellation tolerance. Only the CAD changed, so it1->it2 deltas are geometry changes, not protocol. Overlays add panels (Z=29, theta 20/110, x=-2.0, y=6.0) for new clusters; the it1 panels are all kept. Side-by-side table: qa/probe/like4like_it1_it2.json and the generated section at the end of VERDICT.md. |
| CHK-INDEP | pass | fresh agent, own scripts; see independence |
| CHK-FILLET | pass | build/export_check.json + fillets.json: 3/3 OK (col_top_fillet 1.5, spindle_tip_chamfer 0.7, top_blk_edge_r 1.7 x4 edges), target == used, 0 FAILED/REDUCED/NO_EDGES/SELECTOR_ERROR. No other edge rounds are modelled (declared sharp edges); qa/probe/edge_share.json shows the 0.3..0.8 mm population is not an edge-only effect. |
| CHK-PATCHWORK | pass | QA census (qa/step_check.json): 351 faces, 100 % analytic area (plane 254, cylinder 76, cone 20, torus 1), 0 B-spline/ruled faces; plane median area ~5.9 mm2 (face_stats.json, reported not gated). grep of build/model.py for loft|ruled|Polyline: 0 hits. No faceted skin. |
| CHK-ENUM | finding | it1 findings closed: switch underside bump (E16), column lug at 320 (E17), bar at 330 (E18), barb top rib all now in the CAD; their it1 clusters are gone (qa/probe/over_share_it2.json regions R4/R5/R6 now max <= 0.68). No new unenumerated scan feature found: every one of the 26 scan->CAD clusters >= 20 pts (qa/probe/cluster_probe.json) sits on an enumerated feature. Remaining finding: CAD material with no scan behind it at the it2 port junction boxes (s2c cluster 0: 790 scan pts INSIDE the CAD by up to 1.94 mm at x -3.2..-1.0, y 4.7..7.7, z 27.3..32.3; c2s clusters 0/4/8) - the it2 junction box between the upper port and the neck fills a region where the scan shows a -X-facing sloped wall (overlays Z=29, Z=30.8, y=6.0, x=-2.0). Declared-not-modelled features stay over band: spline teeth, spindle tip hole (cluster 10), cap dimples, cam x~0 step walls (clusters 2, 3, 6), switch labels, plate lips. |
| CHK-ACHIEVABLE | n/a | no Tier-1 (no calipers, DECISIONS.md MEASUREMENTS scan-only); nothing to attribute |
| PHOTO-PLAUSIBILITY | finding | photos 1..5 (catalogue, low-res, no scale) walked by this QA agent: splined spindle with tip hole (1,2,4), cap disc with slots and dimples (2,4), cam ring/teeth (2,3,4,5), two side ports with clip plates (1,3,5), barb (3,5), top clip port (1,3,5), microswitch with blades and bracket (1,2,4) are all present in the CAD; nothing in the CAD is absent from photos+scan except the interior material inside the column and the port junction boxes (buried/assumed, MODELING_PLAN §6). Photographed but not modelled (declared): spline teeth, spindle tip hole, cap dimples. |

## Misses, per region

- scan_to_cad:masked: p95 0.449 max 1.940 vs 0.3/0.8
- cad_to_scan_observable: p95 0.761 max 2.890 vs 0.3/0.8
- zone:Z1_spindle:scan_to_cad: p95 0.284 max 1.338 vs 0.3/0.8
- zone:Z2_cap_cam_ring:scan_to_cad: p95 0.615 max 1.593 vs 0.3/0.8
- zone:Z3_top_clip_port:scan_to_cad: p95 0.425 max 0.890 vs 0.3/0.8
- zone:Z4_side_ports:scan_to_cad: p95 0.272 max 0.956 vs 0.3/0.8
- zone:Z6_microswitch:scan_to_cad: p95 0.474 max 0.883 vs 0.3/0.8
- **whole part scan->CAD (gated)**: p95 and max over band (numbers in the gate table; it1 vs it2 in the generated table at the end). 10.8 % of scan points are over 0.30 mm (p95 <= 0.30 needs <= 5 %) and 1.05 % over 0.80 mm in 26 clusters >= 20 pts plus 65 points in small clusters (qa/probe/over_share_it2.json). Scan is clean (noise ~0.04 mm), full-res, datum/ICP not implicated. Over-0.30 share by z band: cam ring z 0..8.2 29 %, column/lower port z 15.4..27.7 33 %, collar band z 8.2..15.4 15 %, neck/upper port 11 %, top clip port 10 %, spindle 2 %. Two populations: (a) >0.8 mm clusters on named regions - it2 port junction boxes over-filling by the neck (cluster 0, new regression, 790 pts), shoulder-block slope (1), declared cam x~0 steps (2, 3, 6), holder/bracket junction (4), cam flanks (5, 12), declared spindle tip hole (10), cap slots, plate lips; (b) a diffuse 0.3..0.8 mm face-placement population (cam flanks and pocket floors, top-port lug outline rounded vs rectangular CAD - overlay Z=45.5, collar sectors) that is NOT concentrated at sharp edges (qa/probe/edge_share.json: excluding points within 1 mm of sharp CAD edges does not lower p95). Hypothetical upper bound (probe, not a gate): making EVERY >0.8 mm cluster neighbourhood perfect (bbox +1.5 mm, 10 % of the scan) would still leave p95 ~0.34 and max ~1.09. Options: (1) ACCEPT-BAND now (owner decision in DECISIONS.md citing this gate.json hash and a band_fails name), delivering it2 with this per-region list. (2) Loop 3 (last) on the fixable items: trim the it2 port junction boxes to the scanned sloped wall (cluster 0/9/13, c2s 0/4/8), refit the shoulder-block slope (1), open the holder/bracket junction (4, c2s 7), model the cam x~0 steps (2/3/6), tip hole (10), plate lips (7, c2s 5/6/10/11), cam flank placement (5/12), top-port lug outline. Realistic expectation: p95 falls toward ~0.35-0.40 and max toward ~1.1-1.3 mm; the probe bound says p95 0.30 and max 0.80 are NOT reachable by cluster fixes alone and would also need a full refit of the diffuse 0.3..0.8 mm face placement plus features the scan cannot define (spline tooth count unresolved, cap slots/dimples partly scanned). (3) Supply calipers/measurements or a different regime - an owner decision, never QA's.
- **whole part CAD->scan, observable subset (gated)**: p95 and max over band. Unobservable fraction is small (~2.8 %), so this is not mainly a coverage artefact: the biggest contributors are CAD material with no scan behind it at the port junction boxes and lower/upper port plates (c2s 0, 4, 5, 6, 8, 10, 11, up to ~3.5 mm), the holder/bracket junction remnant (c2s 7) and the holder top under the switch (c2s 9); the barb/port bore interiors (c2s 1, 2) and the top-bore counterbore walls (c2s 3) are unscanned and count only where the ray test found line of sight. Options: same as above; trimming the junction boxes and plate inner edges to the scanned outline is the main fixable lever; bore interiors cannot be graded without more scan data.
- **Z2_cap_cam_ring (gated, whole band)**: p95 and max over band, essentially unchanged from it1: shoulder-block slope (cluster 1, smaller than it1), declared cam x~0 step walls (2, 3, 6), cam flank placement (5, 12), cap slot walls (probe 16/18/21/24), declared dimples; 16.6 % of this zone is over 0.30 mm. Options: model the x~0 steps and per-pocket floors, refit post/tooth flanks per instance (not one 120-degree pattern), refit the block slope; or accept.
- **Z6_microswitch (gated)**: p95 and max both improved strongly vs it1 (bump and bar 330 now modelled; see the it1/it2 table) but both stay over band: max is at the switch outer face y ~9.1 (probe cluster 15, 41 pts OUTSIDE the CAD, moulded marks/labels, declared) and the p95 residual is spread over the plain sharp-edged box (switch edge rounds and labels declared not modelled). Options: model the switch box edge rounds and raised marks, or accept (purchased part).
- **Z3_top_clip_port (gated)**: p95 over band, max just over (0.89): bore floor fixed in it2, remaining miss is the lug outline (scan rounded/irregular vs CAD rectangle with 1.7 mm rounds, overlay Z=45.5) and averaged internal ribs (declared). Options: model the lug outline from the scan section; ribs need better scan coverage.
- **Z1_spindle (gated)**: p95 passes, max over band at the declared-not-modelled tip hole (cluster 10) and spline teeth (median cylinder; tooth count unresolved, CHK-COUNT). Options: model the tip hole; teeth need a tooth count (photo/caliper) or stay a declared miss.
- **Z4_side_ports (gated)**: p95 passes, max over band at plate lips (cluster 7, declared) and plate/junction edges. Options: model plate lips/hooks; trim junction boxes.

## Declared limitations (each with its re-run trigger)

1. Tier-1 not run: no calipers (DECISIONS.md MEASUREMENTS, scan-only). Every intake/MEASUREMENTS.md row is ABSENT, not passed. — **Re-run trigger:** any caliper reading supplied
2. Absolute scale not caliper-verified (CHK-SCALE FLAG). The it1 QA uniform-scale probe on the same scan and alignment read about -0.13 %, so scale does not explain the miss; not re-run in it2 because scan and matrix are identical. — **Re-run trigger:** one caliper reading of any overall dimension
3. Datum audit outside the RE_SPEC reference band (report-only, never blocking): see gate.json#datum_audit; identical to it1 because intake it2 reproduced the same matrix. The QA ICP correction is small (gate.json#registration) and the datum-frame and post-ICP scan->CAD p95 agree within a few hundredths of a mm (deviation_datum_frame), so the datum is not the cause of the miss. — **Re-run trigger:** a new intake alignment (route datum with a changed spec)
4. Overlays (qa/overlays/*.png) are drawn in the builder's alignment frame (overlay.py has no --registration option); the gate itself is post-ICP. The ICP correction is below the drawn line width at these scales. — **Re-run trigger:** overlay.py gains a --registration option
5. deviation_gate.py keeps only the top 12 scan->CAD clusters in gate.json while 26 clusters of >= 20 pts exist; the other 14 (all <= 49 pts, <= 1.26 mm) are characterised in qa/probe/cluster_probe.json and summarised in review.json, not individually in gate.json. — **Re-run trigger:** fix of the 12-cluster cap in deviation_gate.py, then re-run QA

## Claim boundary

Not an approved model. This QA result grades iteration 2 against the owner's baseline-skill plastic band (p95 <= 0.30 / max <= 0.80 mm) on the scan only: the band is missed in both gated directions and in 5 of 6 zones. It is not evidence of any dimension (no calipers, scale unverified), says nothing about the unscanned interior (bores, spool, passages are not modelled and not graded), and is not fit for tooling, manufacture or mating-part design. Delivery needs a recorded ACCEPT-BAND. Zone Z5 (barb) passing is a local result and does not excuse the whole part.

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: BAND_NOT_MET, HALT, REVISE._

## It1 vs it2, same protocol (CHK-LIKE4LIKE; generated by qa/probe/like4like_it1_it2.py from both gate.json files)

it1 gate `_it1_SUPERSEDED/qa/gate.json` sha256 9c4d18bf6798…; it2 gate `qa/gate.json` sha256 19f6d742b0ae….

| Gated item | it1 p95 | it1 max | it1 | it2 p95 | it2 max | it2 |
|---|---|---|---|---|---|---|
| scan_to_cad:masked | 0.520 | 2.270 | FAIL | 0.449 | 1.940 | FAIL |
| cad_to_scan_observable | 0.800 | 3.129 | FAIL | 0.761 | 2.890 | FAIL |
| zone:Z1_spindle:scan_to_cad | 0.270 | 1.327 | FAIL | 0.284 | 1.338 | FAIL |
| zone:Z2_cap_cam_ring:scan_to_cad | 0.618 | 1.626 | FAIL | 0.615 | 1.593 | FAIL |
| zone:Z3_top_clip_port:scan_to_cad | 0.433 | 0.890 | FAIL | 0.425 | 0.890 | FAIL |
| zone:Z4_side_ports:scan_to_cad | 0.280 | 0.962 | FAIL | 0.272 | 0.956 | FAIL |
| zone:Z5_barb:scan_to_cad | 0.150 | 0.742 | PASS | 0.152 | 0.764 | PASS |
| zone:Z6_microswitch:scan_to_cad | 0.516 | 1.747 | FAIL | 0.474 | 0.883 | FAIL |

| Other | it1 | it2 |
|---|---|---|
| registration | iterations 38, max_iterations 60, converged True, delta_deg 0.094, delta_mm 0.068 | iterations 41, max_iterations 60, converged True, delta_deg 0.134, delta_mm 0.064 |
| datum_audit | angle_deg 0.256, origin_offset_mm 0.166, point_disagreement_p95_mm 0.188, point_disagreement_max_mm 0.231 | angle_deg 0.256, origin_offset_mm 0.166, point_disagreement_p95_mm 0.188, point_disagreement_max_mm 0.231 |
| unobservable_fraction | 0.030 | 0.028 |
| cad_to_scan_raw | p95 1.037, max 3.499 | p95 0.934, max 3.465 |
| datum_frame_scan_to_cad | p95 0.517, max 2.254 | p95 0.440, max 1.931 |
| n_over_0.8_scan_to_cad | 4437 | 2638 |
| clusters_ge20 | 31 | 26 |
| faces | 314 | 351 |
| verdict | REVISE | BAND_NOT_MET |

## QA process notes (hand-written; every figure is in gate.json, the generated table above, or qa/probe/*.json)

- **Can loop 3 (the last) reach the band?** Not realistically. Two loops of targeted fixes moved the gated scan→CAD p95 by
  well under half of the gap to 0.30, and the probe bound (`qa/probe/over_share_it2.json`, hypothetical, not a gate) says
  that even making every >0.8 mm cluster neighbourhood perfect leaves p95 above 0.30 and max above 0.80. Reaching the band
  would also need a refit of the diffuse 0.3–0.8 mm face placement (cam ring, collar, top-port lug outline) and features the
  scan cannot define (spline tooth count, partly scanned cap slots/dimples, tip-hole depth). Hence BAND_NOT_MET, not REVISE.
  A loop 3 is still worth it only if the owner wants a closer model before accepting (junction-box regression, shoulder
  slope, holder junction, cam x~0 steps are concrete, scan-measurable fixes).
- **It1 → it2:** all it1 CHK-ENUM items and most named it1 clusters are fixed (port end walls, barb rib, switch bump,
  bar 330, column lug, top-bore floor); the zone that gained most is Z6. One regression was introduced: the it2 port
  junction box by the neck (cluster 0) is now the largest single cluster and carries the whole-part max. Z1 moved slightly
  the other way with an unchanged spindle; that is a registration/tessellation effect (different ICP optimum), not geometry.
- **Skill/script defects met (same as it1, still present):** (1) `deviation_gate.py` keeps only the top 12 scan→CAD
  clusters in gate.json (limitation L5); (2) `overlay.py` has no `--registration` option (L4); (3) documentation gap: a
  `functional_interface` zone is silently ungated when the regime has no `interface_max_mm`, so intake zones were declared
  `whole` on scan→CAD only (same as it1); (4) `verdict.py render` has no place for an iteration comparison, so the it1/it2
  table is generated by `qa/probe/like4like_it1_it2.py` and appended here (rendering again drops it: re-run the probe);
  (5) `edge_share.py` (it1 probe, reused) reports p95 of the points *away* from edges, which is not a hypothetical fix;
  it is used here only to show the diffuse error is not edge-concentrated.
- The `qa/overlays/` folder existed empty before this QA started (created by the supersede step); nothing else in `qa/`
  pre-existed.
