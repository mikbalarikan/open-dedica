# VERDICT: BAND_NOT_MET

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: same independent verifier agent as it1 (stl-re-verify), did not build the model (it1 or it2); QA scripts from skills/stl-re-verify only, plus declared run-local helpers in qa/src/ (observability chunking wrapper, residual/mask composition analysis, datum supplement, zoom sections, heatmaps). Read only input/, intake/INTAKE_CARD.md, alignment.json, regime.json, build/*.step, build/export_check.json, build/MODELING_PLAN.md, DECISIONS.md; build/model.py grepped read-only for CHK-PATCHWORK, never imported. BUILDER_REPORT.md, build_log.txt, measure/ not opened. The STEP was tessellated by QA (0.005 mm / 0.05 rad); build/*_cad.stl not used. MODELING_PLAN.md quotes the builder's self-check numbers; they were not used as expectations. it2: MODELING_PLAN.md §9 was read for the list of changed features only; its self-check numbers were not used as expectations.

Scan: `input/scan.stl` (full-res), label **OFFICIAL (full-res)**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-H21_antidrip-valve_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 19376.495 mm³ | PASS |
| Validity `OD-H21_antidrip-valve.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 19376.495 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 0.018° / origin 0.007 mm / points p95 0.014 max 0.016 mm | within (not blocking) |
| Registration (ICP) | converged | 39/60 its, 0.046° / 0.013 mm | PASS |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 297874 · rms 0.085 · p50 0.041 · p95 0.175 · p99 0.284 · max 0.799 | PASS |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 19982 · rms 0.188 · p50 0.044 · p95 0.255 · p99 0.622 · max 3.120 | FAIL |
| zone:I1 nozzle spigot OD lugs latch:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 30997 · rms 0.116 · p50 0.040 · p95 0.252 · p99 0.464 · max 0.799 | PASS |
| zone:I1 nozzle spigot OD lugs latch:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 32011 · rms 0.121 · p50 0.038 · p95 0.293 · p99 0.430 · max 0.867 | FAIL |
| zone:I2 nozzle shoulder:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 4185 · rms 0.063 · p50 0.045 · p95 0.119 · p99 0.146 · max 0.202 | PASS |
| zone:I2 nozzle shoulder:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 13178 · rms 0.094 · p50 0.049 · p95 0.206 · p99 0.346 · max 0.462 | PASS |
| zone:I3 outlet thread and O-ring:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 18820 · rms 0.085 · p50 0.055 · p95 0.168 · p99 0.220 · max 0.720 | PASS |
| zone:I3 outlet thread and O-ring:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 13896 · rms 0.094 · p50 0.054 · p95 0.190 · p99 0.324 · max 0.564 | PASS |
| zone:I4 barb tube and bulb:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 16777 · rms 0.094 · p50 0.040 · p95 0.204 · p99 0.343 · max 0.775 | PASS |
| zone:I4 barb tube and bulb:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 16195 · rms 0.077 · p50 0.039 · p95 0.163 · p99 0.267 · max 0.414 | PASS |
| zone:I5 ring windows:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 7053 · rms 0.132 · p50 0.078 · p95 0.277 · p99 0.389 · max 0.562 | PASS |
| zone:I5 ring windows:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 6081 · rms 0.200 · p50 0.093 · p95 0.453 · p99 0.684 · max 0.996 | FAIL |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 300181 · rms 0.088 · p50 0.042 · p95 0.178 · p99 0.296 · max 1.085
- scan→CAD masked: n 297874 · rms 0.085 · p50 0.041 · p95 0.175 · p99 0.284 · max 0.799
- CAD→scan unmasked: n 300000 · rms 0.186 · p50 0.044 · p95 0.257 · p99 0.625 · max 3.230
- CAD→scan masked: n 289800 · rms 0.101 · p50 0.043 · p95 0.216 · p99 0.380 · max 0.996
- CAD→scan observable only: n 19982 · rms 0.188 · p50 0.044 · p95 0.255 · p99 0.622 · max 3.120; unobservable fraction 0.09 %

Masks:

- **M1 unscanned bore interiors** (scan_to_cad): the three end bores (nozzle, outlet, barb) were seen only 1.5-4 mm deep; beyond that the scanner bridged them with a membrane (scan side: artefact, not a part surface) and the CAD bore wall/floor has no scan behind it (CAD side: coverage gap). Neither is a surface deviation of the modelled part.; fraction 0.77 %; inside n 2307 · rms 0.280 · p50 0.130 · p95 0.636 · p99 0.917 · max 1.085
- **M1 unscanned bore interiors** (cad_to_scan): the three end bores (nozzle, outlet, barb) were seen only 1.5-4 mm deep; beyond that the scanner bridged them with a membrane (scan side: artefact, not a part surface) and the CAD bore wall/floor has no scan behind it (CAD side: coverage gap). Neither is a surface deviation of the modelled part.; fraction 2.36 %; inside n 7077 · rms 0.998 · p50 0.354 · p95 2.251 · p99 2.759 · max 3.230
- **M2 open boundary** (cad_to_scan): distance from CAD to a scan hole EDGE (7 open loops: bore mouths, 2 ring windows, 2 skirt slits) is not a surface deviation; fraction 2.65 %; inside n 7954 · rms 0.906 · p50 0.359 · p95 2.123 · p99 2.734 · max 3.230

Zones:

- I1 nozzle spigot OD lugs latch [whole] scan_to_cad: unmasked n 30997 · rms 0.116 · p50 0.040 · p95 0.252 · p99 0.464 · max 0.799 | masked n 30997 · rms 0.116 · p50 0.040 · p95 0.252 · p99 0.464 · max 0.799
- I1 nozzle spigot OD lugs latch [whole] cad_to_scan: unmasked n 32022 · rms 0.121 · p50 0.038 · p95 0.294 · p99 0.430 · max 0.867 | masked n 32011 · rms 0.121 · p50 0.038 · p95 0.293 · p99 0.430 · max 0.867
- I2 nozzle shoulder [whole] scan_to_cad: unmasked n 4185 · rms 0.063 · p50 0.045 · p95 0.119 · p99 0.146 · max 0.202 | masked n 4185 · rms 0.063 · p50 0.045 · p95 0.119 · p99 0.146 · max 0.202
- I2 nozzle shoulder [whole] cad_to_scan: unmasked n 13178 · rms 0.094 · p50 0.049 · p95 0.206 · p99 0.346 · max 0.462 | masked n 13178 · rms 0.094 · p50 0.049 · p95 0.206 · p99 0.346 · max 0.462
- I3 outlet thread and O-ring [whole] scan_to_cad: unmasked n 18820 · rms 0.085 · p50 0.055 · p95 0.168 · p99 0.220 · max 0.720 | masked n 18820 · rms 0.085 · p50 0.055 · p95 0.168 · p99 0.220 · max 0.720
- I3 outlet thread and O-ring [whole] cad_to_scan: unmasked n 13923 · rms 0.094 · p50 0.054 · p95 0.191 · p99 0.325 · max 0.564 | masked n 13896 · rms 0.094 · p50 0.054 · p95 0.190 · p99 0.324 · max 0.564
- I4 barb tube and bulb [whole] scan_to_cad: unmasked n 16777 · rms 0.094 · p50 0.040 · p95 0.204 · p99 0.343 · max 0.775 | masked n 16777 · rms 0.094 · p50 0.040 · p95 0.204 · p99 0.343 · max 0.775
- I4 barb tube and bulb [whole] cad_to_scan: unmasked n 16312 · rms 0.083 · p50 0.039 · p95 0.168 · p99 0.288 · max 0.842 | masked n 16195 · rms 0.077 · p50 0.039 · p95 0.163 · p99 0.267 · max 0.414
- I5 ring windows [whole] scan_to_cad: unmasked n 7053 · rms 0.132 · p50 0.078 · p95 0.277 · p99 0.389 · max 0.562 | masked n 7053 · rms 0.132 · p50 0.078 · p95 0.277 · p99 0.389 · max 0.562
- I5 ring windows [whole] cad_to_scan: unmasked n 7730 · rms 0.238 · p50 0.105 · p95 0.559 · p99 0.794 · max 1.044 | masked n 6081 · rms 0.200 · p50 0.093 · p95 0.453 · p99 0.684 · max 0.996
- B1 nozzle bore interior [interior] scan_to_cad: unmasked n 1189 · rms 0.163 · p50 0.065 · p95 0.358 · p99 0.535 · max 0.736 | masked n 0
- B1 nozzle bore interior [interior] cad_to_scan: unmasked n 5924 · rms 1.075 · p50 0.369 · p95 2.324 · p99 2.788 · max 3.230 | masked n 0
- B2 outlet end bore interior [interior] scan_to_cad: unmasked n 669 · rms 0.400 · p50 0.206 · p95 0.872 · p99 1.028 · max 1.085 | masked n 0
- B2 outlet end bore interior [interior] cad_to_scan: unmasked n 688 · rms 0.454 · p50 0.361 · p95 0.807 · p99 0.930 · max 0.994 | masked n 0
- B3 barb end bore interior [interior] scan_to_cad: unmasked n 449 · rms 0.307 · p50 0.188 · p95 0.621 · p99 0.701 · max 0.761 | masked n 0
- B3 barb end bore interior [interior] cad_to_scan: unmasked n 465 · rms 0.390 · p50 0.241 · p95 0.770 · p99 0.870 · max 0.913 | masked n 0
- R nozzle [region] scan_to_cad: unmasked n 33536 · rms 0.118 · p50 0.043 · p95 0.255 · p99 0.468 · max 0.799 | masked n 32347 · rms 0.116 · p50 0.042 · p95 0.250 · p99 0.461 · max 0.799
- R nozzle [region] cad_to_scan: unmasked n 39543 · rms 0.432 · p50 0.047 · p95 0.866 · p99 2.189 · max 3.230 | masked n 33507 · rms 0.125 · p50 0.040 · p95 0.300 · p99 0.427 · max 0.867
- R nut [region] scan_to_cad: unmasked n 38409 · rms 0.089 · p50 0.048 · p95 0.188 · p99 0.249 · max 0.452 | masked n 38409 · rms 0.089 · p50 0.048 · p95 0.188 · p99 0.249 · max 0.452
- R nut [region] cad_to_scan: unmasked n 45081 · rms 0.099 · p50 0.048 · p95 0.220 · p99 0.322 · max 0.513 | masked n 45081 · rms 0.099 · p50 0.048 · p95 0.220 · p99 0.322 · max 0.513
- R band [region] scan_to_cad: unmasked n 38952 · rms 0.069 · p50 0.041 · p95 0.139 · p99 0.199 · max 0.320 | masked n 38952 · rms 0.069 · p50 0.041 · p95 0.139 · p99 0.199 · max 0.320
- R band [region] cad_to_scan: unmasked n 40180 · rms 0.095 · p50 0.048 · p95 0.182 · p99 0.347 · max 0.764 | masked n 40180 · rms 0.095 · p50 0.048 · p95 0.182 · p99 0.347 · max 0.764
- R body outlet web [region] scan_to_cad: unmasked n 67870 · rms 0.087 · p50 0.041 · p95 0.160 · p99 0.286 · max 1.085 | masked n 67201 · rms 0.077 · p50 0.041 · p95 0.155 · p99 0.246 · max 0.720
- R body outlet web [region] cad_to_scan: unmasked n 62585 · rms 0.113 · p50 0.043 · p95 0.230 · p99 0.450 · max 0.994 | masked n 61865 · rms 0.102 · p50 0.043 · p95 0.212 · p99 0.406 · max 0.828
- R ring skirt [region] scan_to_cad: unmasked n 43257 · rms 0.092 · p50 0.046 · p95 0.189 · p99 0.340 · max 0.673 | masked n 43257 · rms 0.092 · p50 0.046 · p95 0.189 · p99 0.340 · max 0.673
- R ring skirt [region] cad_to_scan: unmasked n 41848 · rms 0.139 · p50 0.050 · p95 0.309 · p99 0.566 · max 1.044 | masked n 38986 · rms 0.115 · p50 0.047 · p95 0.246 · p99 0.468 · max 0.996
- R cap [region] scan_to_cad: unmasked n 49217 · rms 0.067 · p50 0.035 · p95 0.130 · p99 0.232 · max 0.724 | masked n 48982 · rms 0.065 · p50 0.034 · p95 0.127 · p99 0.223 · max 0.489
- R cap [region] cad_to_scan: unmasked n 46920 · rms 0.078 · p50 0.035 · p95 0.144 · p99 0.328 · max 0.586 | masked n 46848 · rms 0.077 · p50 0.034 · p95 0.142 · p99 0.329 · max 0.586
- R barb above cap [region] scan_to_cad: unmasked n 28940 · rms 0.098 · p50 0.044 · p95 0.204 · p99 0.314 · max 0.775 | masked n 28726 · rms 0.094 · p50 0.044 · p95 0.199 · p99 0.293 · max 0.775
- R barb above cap [region] cad_to_scan: unmasked n 23843 · rms 0.106 · p50 0.045 · p95 0.205 · p99 0.345 · max 0.913 | masked n 23333 · rms 0.089 · p50 0.044 · p95 0.193 · p99 0.262 · max 0.414

Over-band scan→CAD points (> 0.8 mm): 48 (0.016 %) in 1 clusters ≥ 20 pts.

- cluster 0: n 48, centroid [28.3, -0.203, 2.458], r [28.137, 28.431], θ [0.1, 360.0], max 1.085 — outlet end bore (L3): scanner bridge membrane curling into the bore at x 28.1-28.4, 48 pts, max 1.085 (zoom 'outlet end theta=0'); scanner artefact inside declared mask M1. Unchanged from it1 (the outlet was not rebuilt). The it1 latch cluster is gone.

## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | finding | whole part scan_to_cad; zone I4 barb tube and bulb cad_to_scan |
| CHK-CLUSTER | pass | 1 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | pass | datum not ICP'd to own CAD; QA T_refine (qa/registration.json) is QA-only and not written back; no expected value taken from the builder. The builder's build/selfcheck.json (frozen datum, no ICP) is a consistency check, not independent evidence. |
| CHK-LIKE4LIKE | pass | it1 (_it1_SUPERSEDED/qa/gate.json dd052135f7c2) vs it2 use the identical protocol: same regime.json, byte-identical zones.json and masks.json (declared at it1, before any number), same ICP params (39 its both), same deviation sampling/seeds, same observability params, same QA tessellation (0.005/0.05), same run-local helpers (obs chunk 64). Every it1->it2 delta is geometry, not protocol. |
| CHK-INDEP | pass | fresh context; see independence |
| CHK-FILLET | pass | export_check.json fillets: [] (0 3D fillet ops, as MODELING_PLAN §5 plans: every round is a profile arc); nothing silently skipped or reduced |
| CHK-PATCHWORK | pass | QA census it2: 146 faces, 100 % analytic (plane 80, cylinder 33, cone 22, torus 11), 0 B-spline/ruled; model.py grep: no loft/sweep/spline; the same 2 make_polygon calls as it1 (4-pt rectangle model.py:112, 5-pt web model.py:238) |
| CHK-ENUM | pass | every INTAKE feature E01-E25 exists in the CAD; every photographed feature present. it2 fixed the three it1 extent findings: latch now a through-window (photo_2 slot), slits trimmed (no CAD pocket at theta 147 / 229.5), window near 110 deepened to the gap. Remaining window/latch residuals sit behind scanner bridge membranes (see miss_explanations). |
| CHK-ACHIEVABLE | n/a | no Tier-1 (scan-only, no calipers) |
| PHOTO-PLAUSIBILITY | pass | photo_1, photo_2 (catalogue, no scale): nozzle with tip slot, 8-rib nut, band, body, side outlet with collar, black O-ring and thread, cap ring with rectangular windows, cap, hose barb - all present in CAD. Declared simplifications visible in photos: thread modelled as plain cylinder, O-ring fused to the outlet. |

## Misses, per region

- cad_to_scan_observable: p95 0.255 max 3.120 vs 0.3/0.8
- zone:I1 nozzle spigot OD lugs latch:cad_to_scan: p95 0.293 max 0.867 vs 0.3/0.8
- zone:I5 ring windows:cad_to_scan: p95 0.453 max 0.996 vs 0.3/0.8
- **cad_to_scan_observable (whole part) - nozzle bore floor and far bore wall (B1, M1)**: max 3.120: the CAD bore floor (at the scanner bridge) and the bore wall at theta ~280-340 above z -26 have no scan behind them; the scan's bore wall ends at the ragged mouth z ~-26.1 on that side (qa/overlays/zoom_it2_extra.png 'bore far wall theta=300/315'). COVERAGE FACT, not a through-window error: the through-window cut itself fits the scan (bore wall on the window side theta 60-160 c2s p50 0.04-0.23, max 0.46), and the far wall is the unchanged it1 bore cylinder whose radius matches the scanned wall below z -26 (p50 0.15). The it2 window only opens a new ray path to it, which the OD-H22 #3 ray-test defect then counts as observable. Options: A) owner ACCEPT-BAND citing this gate hash and 'cad_to_scan_observable'; B) fix the observability test to be scan-coverage-aware / compose declared masks (skill defect) and re-grade; C) sectioned part or depth reading of the bore.
- **zone I1 nozzle spigot, CAD->scan (latch through-window edge, theta ~83, r 4.7, z -24.1)**: max 0.867 on 2 points: the upper face of the new through-window near its theta-83 edge sits ~0.87 mm from the scan, whose surface there is the bridge membrane sagging into the window (zoom 'latch edge theta=83'). Scanner fact (membrane), not a fixable geometry error; scan->CAD in I1 now passes (0.799). Options: accept (ACCEPT-BAND, 'zone:I1'), or a caliper/photo with scale of the latch slot height to arbitrate; no further rebuild recommended (it would follow a membrane).
- **zone I5 ring windows, CAD->scan (windows near theta 121 and 285)**: masked p95 0.453 / max 0.996 (unmasked p95 0.559 / max 1.044). The CAD window floors and walls lie behind scanner bridge membranes: at theta 121 and 285 the scanned skirt sags 0.3-0.4 mm inward exactly over the window z-span (13-15 and 12-14), i.e. a membrane across an opening, not closed skirt (zoom 'ring window theta=121/285'); the window at 290 is scanned open and matches the CAD. Scanner fact. scan->CAD in I5 now passes (p95 0.277 / max 0.562). Options: accept (ACCEPT-BAND, 'zone:I5'), or caliper the window width/height; modelling the CAD to the membrane would model an artefact.
- **outlet collar / O-ring junction (theta ~8, x 22.7, z 0.4; outside I3)**: 6 CAD points up to 0.828 at the fused O-ring-to-collar fill (declared invented connection, MODELING_PLAN §6 / L5); present in it1 too (1 pt 0.846). Declared simplification, not a coverage defect; it does not decide any gated result on its own (the gated CAD->scan term is already over band from the bore floor). Options: keep as declared (L5), or model the O-ring as a separate body.

## Declared limitations (each with its re-run trigger)

1. Tier-1 not run: scan-only job, no caliper readings supplied (DECISIONS MEASUREMENTS). Every caliper-coverable dim is ABSENT, not passed. — **Re-run trigger:** any caliper reading (nozzle OD, lug span, thread OD, O-ring OD, barb OD, window width) -> re-run Tier-1 and the gate
2. Absolute scale not caliper-verified (CHK-SCALE flag at intake; units assumed mm, scale 1.0). — **Re-run trigger:** one caliper reading of any dimension
3. scan_resolution = full by agent inference (DECISIONS OTHER: 600,142 faces, mean edge 0.152 mm), not owner-confirmed. The gate is labelled OFFICIAL (full-res) on that inference. — **Re-run trigger:** owner confirms the scan is the original export; if it is decimated, re-label INSPECTION ONLY and re-grade on the original
4. Bore interiors (nozzle, outlet, barb) and all internal passages are unscanned/bridged; named mask M1 removes them. The whole-part scan->CAD pass is MASK-DEPENDENT: masked max 0.799 (0.001 under the band; 0.800 in the builder datum frame, i.e. fragile), unmasked max 1.085 at the outlet bore bridge membrane. — **Re-run trigger:** a sectioned part, CT scan or depth-gauge reading of the three bores
5. Assembly scanned as one closed shell: sub-part poses kept as scanned (nozzle 1.3 deg, cap part 3.4 deg tilt), O-ring fused into the single solid, thread modelled as a plain cylinder (MODELING_PLAN §4, §6). — **Re-run trigger:** owner asks for a nominal (coaxial) design, separate parts or a real thread
6. Observability ray test (observability.py) counts CAD surfaces inside open-mouthed bores, windows and slits as observable although no scan covers them (unobservable fraction 0.09 %); the gated cad_to_scan_observable therefore contains the unscanned nozzle bore floor and far bore wall (max 3.120). QA's run-local composition observable AND NOT (M1, M2) is in qa/residual_analysis.json (p95 0.213 / max 0.871). — **Re-run trigger:** a scan-coverage-aware observability test (or mask composition in deviation_gate/verdict) -> re-run the gate
7. Datum audit (report-only) agrees with alignment.json within 0.018 deg / 0.007 mm; but the as-built origin is the nozzle axis at its measured mid-station projected along the band normal, while the literal 'nozzle axis ∩ band plane' along the 1.16-1.27 deg tilted axis lies 0.37 mm away (qa/datum_supplement.json). No effect on deviation (ICP delta 0.045 deg / 0.015 mm). — **Re-run trigger:** owner states which origin definition downstream users need

## Claim boundary

Outer-envelope reconstruction of a scanned assembly (one fused solid, sub-parts as scanned). Not a functional flow part (internal passages, valve seat, spring not modelled), not caliper-verified in scale or any dimension, bore depths are scanner-bridge depths, window/latch floors behind scanner membranes are unverified, thread is a plain cylinder. Not fit for tooling, moulding, fits or thread engagement until calipered; fit for visual/envelope/packaging use only after a recorded ACCEPT-BAND.

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: BAND_NOT_MET, HALT, REVISE._
