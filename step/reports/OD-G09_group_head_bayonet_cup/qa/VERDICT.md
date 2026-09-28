# VERDICT: HALT

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: fresh agent that did not build the model; QA scripts from stl-re-verify only (plus run-local helpers qa/scan_coverage_survey.py, qa/residual_locate.py, qa/icp_diagnose.py, report-only); builder numbers not used as expected values; build/model.py only grepped read-only; measure/, build_log, selfcheck/ not read. QA had read the builder's self-check figures quoted in build/MODELING_PLAN.md §8 before choosing masks.

Scan: `input/scan.stl` (full-res), label **INVALID**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-G10_porta_filter_holder_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 40425.376 mm³ | PASS |
| Validity `OD-G10_porta_filter_holder.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 40425.376 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 1.890° / origin 0.005 mm / points p95 1.326 max 1.341 mm | outside (not blocking) |
| Registration (ICP) | converged | 500/500 its, 0.904° / 0.989 mm | INVALID |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 202623 · rms 0.597 · p50 0.528 · p95 0.971 · p99 1.083 · max 1.826 | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 19098 · rms 3.502 · p50 0.901 · p95 9.008 · p99 12.295 · max 15.583 | FAIL |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 202623 · rms 0.597 · p50 0.528 · p95 0.971 · p99 1.083 · max 1.826
- scan→CAD masked: n 202623 · rms 0.597 · p50 0.528 · p95 0.971 · p99 1.083 · max 1.826
- CAD→scan unmasked: n 300000 · rms 3.472 · p50 0.922 · p95 8.920 · p99 12.146 · max 15.629
- CAD→scan masked: n 147863 · rms 0.793 · p50 0.573 · p95 1.516 · p99 2.600 · max 4.549
- CAD→scan observable only: n 19098 · rms 3.502 · p50 0.901 · p95 9.008 · p99 12.295 · max 15.583; unobservable fraction 4.51 %

Masks:

- **M1 C1 downward-facing CAD** (cad_to_scan): the scan has almost no downward-facing surface (scanned from above): CAD faces facing down (lug undersides, plate underside, bottom closure) have no scan behind them; their CAD->scan distance is a coverage fact, not a surface deviation; fraction 19.68 %; inside n 59054 · rms 4.801 · p50 2.783 · p95 10.689 · p99 12.824 · max 15.629
- **M2 C2 below plate top inside wall** (cad_to_scan): no scan exists inside the outer wall below the plate top: the plate underside, the assumed lower inner wall and the closure at the scan extent are assumed geometry (MODELING_PLAN §6) with nothing to compare against; fraction 22.88 %; inside n 68635 · rms 5.344 · p50 3.300 · p95 11.037 · p99 13.862 · max 15.629
- **M3 C3 plate interior** (cad_to_scan): the plate inside r ~24 is not in the scan; the keyhole, bosses and side hole there are photo-inferred, so no scan distance is meaningful; fraction 10.26 %; inside n 30766 · rms 7.848 · p50 6.648 · p95 13.233 · p99 14.915 · max 15.629
- **M4 C6 outer wall unscanned sector** (cad_to_scan): the outer cup wall is not scanned at all over this sector (cup joined to the machine housing there, photos 1-2); the CAD continues the cylinder (assumed) with no scan behind it; fraction 9.96 %; inside n 29865 · rms 4.805 · p50 2.440 · p95 10.336 · p99 11.697 · max 12.295
- **M5 open boundary** (cad_to_scan): distance from CAD to a scan hole EDGE is not a surface deviation (the scan is open: 5,151 boundary edges / 16 loops); fraction 34.65 %; inside n 103951 · rms 5.033 · p50 2.492 · p95 11.097 · p99 13.766 · max 15.629

Zones:

- I1 lug inner faces [functional_interface] scan_to_cad: unmasked n 4228 · rms 0.284 · p50 0.176 · p95 0.568 · p99 0.848 · max 1.100 | masked n 4228 · rms 0.284 · p50 0.176 · p95 0.568 · p99 0.848 · max 1.100
- I1 lug inner faces [functional_interface] cad_to_scan: unmasked n 7539 · rms 0.690 · p50 0.718 · p95 1.015 · p99 1.213 · max 1.577 | masked n 6570 · rms 0.679 · p50 0.718 · p95 0.984 · p99 1.135 · max 1.389
- I3 lug stops [functional_interface] scan_to_cad: unmasked n 4437 · rms 0.539 · p50 0.377 · p95 0.935 · p99 0.986 · max 1.062 | masked n 4437 · rms 0.539 · p50 0.377 · p95 0.935 · p99 0.986 · max 1.062
- I3 lug stops [functional_interface] cad_to_scan: unmasked n 4996 · rms 1.369 · p50 0.815 · p95 2.869 · p99 3.568 · max 4.142 | masked n 3313 · rms 1.182 · p50 0.758 · p95 2.676 · p99 3.591 · max 4.142
- I4 bore [functional_interface] scan_to_cad: unmasked n 12422 · rms 0.410 · p50 0.377 · p95 0.665 · p99 0.750 · max 0.879 | masked n 12422 · rms 0.410 · p50 0.377 · p95 0.665 · p99 0.750 · max 0.879
- I4 bore [functional_interface] cad_to_scan: unmasked n 24132 · rms 0.785 · p50 0.582 · p95 1.867 · p99 2.293 · max 2.999 | masked n 22295 · rms 0.746 · p50 0.554 · p95 1.082 · p99 2.293 · max 2.999
- I5 shelf and pockets [functional_interface] scan_to_cad: unmasked n 19888 · rms 0.593 · p50 0.536 · p95 0.892 · p99 1.030 · max 1.427 | masked n 19888 · rms 0.593 · p50 0.536 · p95 0.892 · p99 1.030 · max 1.427
- I5 shelf and pockets [functional_interface] cad_to_scan: unmasked n 15204 · rms 0.874 · p50 0.589 · p95 1.653 · p99 2.989 · max 4.371 | masked n 12561 · rms 0.718 · p50 0.558 · p95 0.986 · p99 2.531 · max 4.371
- I6 plate top [functional_interface] scan_to_cad: unmasked n 1296 · rms 0.290 · p50 0.311 · p95 0.359 · p99 0.362 · max 0.363 | masked n 1296 · rms 0.290 · p50 0.311 · p95 0.359 · p99 0.362 · max 0.363
- I6 plate top [functional_interface] cad_to_scan: unmasked n 13394 · rms 1.219 · p50 0.793 · p95 2.664 · p99 3.839 · max 4.988 | masked n 4853 · rms 0.768 · p50 0.756 · p95 1.026 · p99 1.050 · max 1.069
- I2 lug undersides (hidden) [interior] cad_to_scan: unmasked n 6677 · rms 1.904 · p50 1.803 · p95 2.927 · p99 3.216 · max 3.726 | masked n 0
- rim z above 0.1 [region] scan_to_cad: unmasked n 33473 · rms 0.525 · p50 0.427 · p95 0.949 · p99 1.075 · max 1.120 | masked n 33473 · rms 0.525 · p50 0.427 · p95 0.949 · p99 1.075 · max 1.120
- rim z above 0.1 [region] cad_to_scan: unmasked n 24869 · rms 0.686 · p50 0.565 · p95 1.171 · p99 1.549 · max 2.026 | masked n 22108 · rms 0.661 · p50 0.565 · p95 1.113 · p99 1.240 · max 1.430
- band z -7 to 0.1 [region] scan_to_cad: unmasked n 52865 · rms 0.604 · p50 0.538 · p95 0.975 · p99 1.192 · max 1.826 | masked n 52865 · rms 0.604 · p50 0.538 · p95 0.975 · p99 1.192 · max 1.826
- band z -7 to 0.1 [region] cad_to_scan: unmasked n 59752 · rms 1.248 · p50 0.688 · p95 2.578 · p99 3.360 · max 4.380 | masked n 41067 · rms 0.741 · p50 0.558 · p95 1.103 · p99 2.690 · max 3.694
- band z -14 to -7 [region] scan_to_cad: unmasked n 29450 · rms 0.585 · p50 0.518 · p95 0.941 · p99 1.052 · max 1.358 | masked n 29450 · rms 0.585 · p50 0.518 · p95 0.941 · p99 1.052 · max 1.358
- band z -14 to -7 [region] cad_to_scan: unmasked n 44451 · rms 1.471 · p50 0.763 · p95 2.755 · p99 4.135 · max 5.435 | masked n 32057 · rms 1.064 · p50 0.620 · p95 2.294 · p99 2.855 · max 4.549
- band z -20.3 to -14 [region] scan_to_cad: unmasked n 60887 · rms 0.598 · p50 0.530 · p95 0.963 · p99 1.093 · max 1.556 | masked n 60887 · rms 0.598 · p50 0.530 · p95 0.963 · p99 1.093 · max 1.556
- band z -20.3 to -14 [region] cad_to_scan: unmasked n 78095 · rms 3.407 · p50 0.808 · p95 8.879 · p99 12.636 · max 15.530 | masked n 40614 · rms 0.698 · p50 0.556 · p95 1.058 · p99 2.077 · max 4.371
- below z -20.3 [region] scan_to_cad: unmasked n 25948 · rms 0.678 · p50 0.646 · p95 1.003 · p99 1.050 · max 1.136 | masked n 25948 · rms 0.678 · p50 0.646 · p95 1.003 · p99 1.050 · max 1.136
- below z -20.3 [region] cad_to_scan: unmasked n 92833 · rms 5.199 · p50 2.925 · p95 10.850 · p99 13.395 · max 15.629 | masked n 12017 · rms 0.626 · p50 0.600 · p95 0.954 · p99 0.975 · max 0.996
- outer wall scanned sectors [region] scan_to_cad: unmasked n 34017 · rms 0.351 · p50 0.300 · p95 0.579 · p99 0.605 · max 0.859 | masked n 34017 · rms 0.351 · p50 0.300 · p95 0.579 · p99 0.605 · max 0.859
- outer wall scanned sectors [region] cad_to_scan: unmasked n 63325 · rms 0.633 · p50 0.524 · p95 0.952 · p99 1.774 · max 3.696 | masked n 57943 · rms 0.573 · p50 0.514 · p95 0.915 · p99 1.099 · max 1.280
- outer wall C6 sector [region] scan_to_cad: unmasked n 3510 · rms 0.437 · p50 0.324 · p95 0.791 · p99 0.920 · max 1.052 | masked n 3510 · rms 0.437 · p50 0.324 · p95 0.791 · p99 0.920 · max 1.052
- outer wall C6 sector [region] cad_to_scan: unmasked n 29865 · rms 4.805 · p50 2.440 · p95 10.336 · p99 11.697 · max 12.295 | masked n 0

Over-band scan→CAD points (> 0.8 mm): 39959 (19.721 %) in 35 clusters ≥ 20 pts.

- cluster 0: n 6860, centroid [6.818, -37.574, -16.935], r [39.102, 39.31], θ [248.6, 307.0], max 1.007 — outer wall theta 249-307, z ~-17: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 1: n 6794, centroid [1.947, 35.684, -6.955], r [37.053, 38.419], θ [35.5, 132.0], max 1.316 — bore/rim theta 35-132: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 2: n 5580, centroid [9.297, -21.995, -20.877], r [23.077, 30.685], θ [223.4, 337.7], max 1.136 — lip ring / plate edge theta 223-338: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 3: n 3535, centroid [-15.293, -29.739, -2.887], r [32.484, 36.552], θ [217.3, 267.6], max 1.463 — lug-3 top and channel theta 217-268: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 4: n 2916, centroid [-3.919, -29.916, 1.566], r [37.889, 39.308], θ [183.8, 329.4], max 1.120 — rim theta 184-329: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 5: n 2093, centroid [-13.264, -26.429, -4.372], r [30.55, 36.258], θ [214.4, 272.5], max 1.826 — lug-3 inner/channel theta 214-273: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 6: n 1780, centroid [-25.742, -17.864, -15.81], r [31.539, 36.778], θ [170.3, 264.2], max 1.231 — shelf/pockets theta 170-264: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 7: n 1727, centroid [-4.817, 28.193, -17.39], r [31.54, 32.865], θ [49.9, 146.2], max 1.186 — lip ring theta 50-146: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 8: n 1370, centroid [21.152, -25.89, -15.105], r [32.244, 36.461], θ [284.5, 329.9], max 1.081 — shelf/pockets theta 284-330: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 9: n 1032, centroid [9.428, 30.299, -19.674], r [32.021, 32.405], θ [51.6, 90.2], max 1.078 — lip ring theta 52-90: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 10: n 955, centroid [-10.96, 30.327, -3.209], r [32.481, 32.714], θ [97.4, 130.4], max 1.033 — lug-2 inner face theta 97-130: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).
- cluster 11: n 804, centroid [-16.59, 34.307, -13.886], r [38.176, 38.436], θ [105.4, 127.0], max 1.058 — bore theta 105-127 z ~-14: registration artefact, not a missing feature: the ICP pose (T_refine, NOT converged at 500 its) is biased by contaminated correspondences (qa/icp_diagnose.json: unscanned CAD faces pair with the opposite wall/plate through 2.4-2.8 mm, pulling ~+z and -y), so the whole scan sits ~0.9 mm off the CAD (scan->CAD p50 0.53). In the builder datum frame (qa/deviation_datum.json) this region has no over-band cluster: scan->CAD has 0 clusters >= 20 pts and only 6 points > 0.8 mm in total (lug-3 end, theta 270.7, z -1.7, max 0.878).

## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | pass | no pass depends on a mask |
| CHK-CLUSTER | pass | 12 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | finding | QA grading is independent: own ICP (not written back), own datum audit, no expected value from this scan (Tier-1 has none). Finding on the builder record: MODELING_PLAN §8 iterated geometry against its own scan self-check (NOT QA) to max 0.761 -- a consistency check, not independent evidence; QA's datum-frame max on the full-res scan is 0.878. The intake noise floor was measured on the same lug pads that set the primary datum (INTAKE_CARD §6, self-referential). |
| CHK-LIKE4LIKE | n/a | first QA run (it1); no superseded qa/. Builder self-check numbers (MODELING_PLAN §8) use a different protocol and are not compared as an improvement. |
| CHK-INDEP | pass | fresh agent; see independence |
| CHK-FILLET | pass | build/export_check.json: 7 fillets (6 fillet_2d profile + F04b 3D stop-root R1.0), every status OK, target == used, both frames |
| CHK-PATCHWORK | pass | census: 182 faces, 100 % analytic area (plane 98, cylinder 57, cone 8, torus 19), no B-spline/ruled faces; model.py grep: no loft/ruled; Wire.make_polygon used only for parameter-driven (r,z) revolve profiles of 4-~20 named points, not stacks of scan slices; matches MODELING_PLAN (revolve/split/boolean only) |
| CHK-ENUM | finding | intake F01-F17 ticked against CAD, overlays and photos 1-2: F01-F12 present and track the scan in the overlays; F13-F15 keyhole, 2 bosses with holes, side hole present (photo-inferred, no scan); dimples not modelled (cosmetic, declared); F16 flange not modelled (outside scan, declared); F17 simplified in gap sectors (declared). No CAD feature lacks photo/scan support. Finding: photo 1 shows a small rectangular window at the base of the outer cup wall (front right, at the flange junction) that the intake list does not enumerate; the scan has no evidence of it (outer-wall coverage tapers at the ragged lower scan edge z -27.8..-24, no scan->CAD cluster), and it is not modelled. |
| CHK-ACHIEVABLE | n/a | no Tier-1 reading, so no Tier-1 miss to attribute |
| PHOTO-PLAUSIBILITY | pass | photos 1 (3/4 view) and 2 (top view) walked: 3 lugs with L-shaped top channels and stops, 6 rim notches, shelf + pocket arcs, lip ring, plate with two-lobed keyhole, 2 screw bosses, bright through-hole, dimples -- CAD is plausible against both; see CHK-ENUM for the one unenumerated photo feature |

## Misses, per region

- scan_to_cad:masked: p95 0.971 max 1.826 vs 0.3/0.8
- cad_to_scan_observable: p95 9.008 max 15.583 vs 0.3/0.8
- **whole part scan->CAD (datum frame, inspection only)**: p95 0.244 passes; max 0.878 > 0.80 from 6 points (no cluster >= 20) at the lug-3 end, theta 270.7, r 33.4-34.3, z -1.7 (overlay panel theta 270.7 shows a thin scan trace past the modelled lug end); lugs are one instance copied at 120 deg pitch. Options: measure the lug-3 end angle on the scan and model per-instance lug spans, or declare it as edge fuzz with photo evidence
- **CAD->scan observable (both frames)**: coverage, not geometry: unscanned CAD surfaces the ray test calls observable (C6 outer wall sector, C4 bore behind the lugs, cavity below the plate) -- datum frame observable p95 9.31 / max 14.61; masked (M1-M5) p95 0.357 / max 5.13, residual dominated by the hidden bore behind the lugs (r 36.4-37.7, z -14..-3.5, lug sectors). Options: more scan coverage, or a human decision to grade CAD->scan on the scanned region only; geometry changes cannot fix it
- **post-ICP gate (INVALID)**: unconverged, contaminated ICP pose shifts the scan ~0.9 mm; every post-ICP band misses for this reason (scan->CAD p95 0.97 / max 1.83). Options: see L3

## Declared limitations (each with its re-run trigger)

1. Tier-1 not run (no calipers): 0 of 15 requested dims measured; all ABSENT, not passed (intake/MEASUREMENTS.md; its header says 16 rows, the tables hold 15 ids). — **Re-run trigger:** filled input/MEASUREMENTS.md with caliper readings -> re-run verify
2. Absolute scale not caliper-verified (CHK-SCALE not run; units assumed mm). — **Re-run trigger:** one caliper reading of ENV-D (outer cup diameter) and ENV-Z2 -> re-run verify
3. Independent ICP did not converge: 60/60 its (0.506 deg / 0.987 mm) and, after the one allowed raise, 500/500 its (0.904 deg / 0.989 mm), still sliding about the axis (~0.0006 deg/it). Diagnosis (qa/icp_diagnose.json, report-only): ~13 % of kept correspondences come from unscanned CAD faces (downward faces, below-plate walls, C6 outer wall) that pair with the opposite wall/plate across 2.4-2.8 mm with antiparallel normals, which tier2_icp.py accepts (|n.n| filter, 3.0 mm cut-off). The Tier-2 gate is therefore INVALID and the post-ICP numbers are biased (scan->CAD p95 0.97 vs 0.24 in the datum frame). — **Re-run trigger:** human decision on the registration protocol (e.g. an ICP that excludes the declared unscanned CAD regions or uses signed normals, or accepting datum-frame grading) -> re-run verify
4. Coverage: the CAD->scan observability split is a CAD line-of-sight test and does not exclude surfaces the scanner could not or did not see (C4 bore behind the lugs, C6 outer wall sector theta 37-152, the open cavity below the plate): only 4.1-4.5 % reads unobservable, so the observable-only CAD->scan number is dominated by coverage, not by geometry. — **Re-run trigger:** a scan with the C6 sector, the underside and the under-lug region covered -> re-run verify
5. Photo-inferred and assumed geometry not graded: keyhole, bosses, side hole (photo-only, +-3 mm / +-10 deg), plate thickness 2.5, lower wall, lug undersides and stop radial depth (hidden, C1-C4). — **Re-run trigger:** caliper readings F-KEY, F-BOSS, F-PLATE, F-LUGT, F-STOP or a photo with a scale -> re-run verify
6. Datum audit (report-only): axis 0.010 deg and origin 0.005 mm agree with the builder, but the 3-fold Fourier clock differs by 1.89 deg overall (4.02 deg with a wider lug-band region, qa/datum_audit_clock_sens.json): the clock is region-sensitive on this part. — **Re-run trigger:** a clock datum on a named flat face (e.g. a lug stop face) agreed with the owner -> re-run datum audit
7. Full resolution is an agent declaration (DECISIONS.md OTHER 2026-09-28), not an owner statement. — **Re-run trigger:** owner says the upload was decimated -> re-run verify on the original

## Blockers (no official grade)

- registration did not converge: gate invalid

## Claim boundary

No official Tier-2 grade: the QA registration did not converge, so the full-res gate is INVALID; datum-frame numbers are inspection only. Not fit for manufacture, tooling or fit-critical use (bayonet engagement): scale and all dimensions are uncalipered, the lug undersides/ramps, stop depth, plate underside and everything below the plate are assumed, and the plate keyhole/bosses/holes are photo-inferred. Not evidence of the outer wall over theta 37-152 or below z -27.84 (unscanned).

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: HALT, REVISE._
