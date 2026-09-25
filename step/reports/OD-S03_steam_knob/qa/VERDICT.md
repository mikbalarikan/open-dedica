# VERDICT: BAND_NOT_MET

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: fresh agent (CHK-INDEP verifier, it2) that did not build the model; stl-re-verify scripts plus QA-own probes in qa/qa_scripts/ (tess_probe, brep_selfcheck, cos_dev, cluster_probe, c2s_residual_probe, c2s_masked_locate, clock_crosscheck, compare_it1_it2); BUILDER_REPORT.md, build_log.txt, *NOT_QA*, measure/params.json not read; model.py only grepped/diffed for CHK-PATCHWORK. MODELING_PLAN.md it2 section quotes builder self-check numbers; none were used.

Scan: `input/scan.stl` (full-res), label **OFFICIAL (full-res)**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-S03_steam-knob_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 11655.643 mm³ | PASS |
| Validity `OD-S03_steam-knob.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 11655.643 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 3.875° / origin 0.021 mm / points p95 1.632 max 1.863 mm | outside (not blocking) |
| Registration (ICP) | converged | 35/60 its, 0.073° / 0.024 mm | PASS |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 182580 · rms 0.090 · p50 0.026 · p95 0.150 · p99 0.278 · max 2.348 | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 19960 · rms 0.267 · p50 0.035 · p95 0.438 · p99 1.444 · max 2.792 | FAIL |
| zone:Z1 threaded sleeve OD:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 13837 · rms 0.085 · p50 0.054 · p95 0.188 · p99 0.245 · max 0.292 | PASS |
| zone:Z1 threaded sleeve OD:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 18672 · rms 0.084 · p50 0.051 · p95 0.182 · p99 0.257 · max 0.517 | PASS |
| zone:Z2 sleeve bore visible:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 1703 · rms 0.085 · p50 0.052 · p95 0.168 · p99 0.248 · max 0.372 | PASS |
| zone:Z2 sleeve bore visible:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 2946 · rms 0.096 · p50 0.054 · p95 0.169 · p99 0.383 · max 0.518 | PASS |
| zone:Z3 stem ribs and core:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 26609 · rms 0.078 · p50 0.045 · p95 0.158 · p99 0.241 · max 0.518 | PASS |
| zone:Z3 stem ribs and core:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 38192 · rms 0.097 · p50 0.052 · p95 0.213 · p99 0.309 · max 0.567 | PASS |
| zone:Z4 crown cap wall lever:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 105799 · rms 0.089 · p50 0.018 · p95 0.111 · p99 0.226 · max 2.348 | FAIL |
| zone:Z4 crown cap wall lever:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 135627 · rms 0.049 · p50 0.019 · p95 0.104 · p99 0.177 · max 0.390 | PASS |
| zone:Z5 step face and collar:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 21240 · rms 0.080 · p50 0.030 · p95 0.140 · p99 0.376 · max 0.720 | PASS |
| zone:Z5 step face and collar:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 35494 · rms 0.068 · p50 0.031 · p95 0.137 · p99 0.275 · max 0.462 | PASS |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 182580 · rms 0.090 · p50 0.026 · p95 0.150 · p99 0.278 · max 2.348
- scan→CAD masked: n 182580 · rms 0.090 · p50 0.026 · p95 0.150 · p99 0.278 · max 2.348
- CAD→scan unmasked: n 300000 · rms 0.267 · p50 0.035 · p95 0.458 · p99 1.413 · max 2.987
- CAD→scan masked: n 252457 · rms 0.072 · p50 0.028 · p95 0.154 · p99 0.275 · max 0.753
- CAD→scan observable only: n 19960 · rms 0.267 · p50 0.035 · p95 0.438 · p99 1.444 · max 2.792; unobservable fraction 0.20 %

Masks:

- **M1 open boundary** (cad_to_scan): CAD->scan distance measured to the EDGE of a scan hole (17 chrome-reflection holes, unscanned pocket floor, crevice floor, deep bore) is a coverage gap, not a surface deviation; fraction 15.71 %; inside n 47144 · rms 0.652 · p50 0.229 · p95 1.533 · p99 2.237 · max 2.987
- **M2 skin normal** (cad_to_scan): a CAD point whose nearest scan point faces >70 deg away is corresponding to a different (occluded/opposite) wall, not an outer-skin deviation; fraction 0.65 %; inside n 1939 · rms 0.528 · p50 0.451 · p95 0.888 · p99 1.229 · max 1.550

Zones:

- Z1 threaded sleeve OD [whole] scan_to_cad: unmasked n 13837 · rms 0.085 · p50 0.054 · p95 0.188 · p99 0.245 · max 0.292 | masked n 13837 · rms 0.085 · p50 0.054 · p95 0.188 · p99 0.245 · max 0.292
- Z1 threaded sleeve OD [whole] cad_to_scan: unmasked n 18805 · rms 0.085 · p50 0.051 · p95 0.183 · p99 0.259 · max 0.517 | masked n 18672 · rms 0.084 · p50 0.051 · p95 0.182 · p99 0.257 · max 0.517
- Z2 sleeve bore visible [whole] scan_to_cad: unmasked n 1703 · rms 0.085 · p50 0.052 · p95 0.168 · p99 0.248 · max 0.372 | masked n 1703 · rms 0.085 · p50 0.052 · p95 0.168 · p99 0.248 · max 0.372
- Z2 sleeve bore visible [whole] cad_to_scan: unmasked n 4091 · rms 0.106 · p50 0.061 · p95 0.212 · p99 0.352 · max 0.518 | masked n 2946 · rms 0.096 · p50 0.054 · p95 0.169 · p99 0.383 · max 0.518
- Z3 stem ribs and core [whole] scan_to_cad: unmasked n 26609 · rms 0.078 · p50 0.045 · p95 0.158 · p99 0.241 · max 0.518 | masked n 26609 · rms 0.078 · p50 0.045 · p95 0.158 · p99 0.241 · max 0.518
- Z3 stem ribs and core [whole] cad_to_scan: unmasked n 43438 · rms 0.176 · p50 0.060 · p95 0.431 · p99 0.692 · max 0.946 | masked n 38192 · rms 0.097 · p50 0.052 · p95 0.213 · p99 0.309 · max 0.567
- Z4 crown cap wall lever [whole] scan_to_cad: unmasked n 105799 · rms 0.089 · p50 0.018 · p95 0.111 · p99 0.226 · max 2.348 | masked n 105799 · rms 0.089 · p50 0.018 · p95 0.111 · p99 0.226 · max 2.348
- Z4 crown cap wall lever [whole] cad_to_scan: unmasked n 159159 · rms 0.284 · p50 0.024 · p95 0.503 · p99 1.518 · max 2.754 | masked n 135627 · rms 0.049 · p50 0.019 · p95 0.104 · p99 0.177 · max 0.390
- Z5 step face and collar [whole] scan_to_cad: unmasked n 21240 · rms 0.080 · p50 0.030 · p95 0.140 · p99 0.376 · max 0.720 | masked n 21240 · rms 0.080 · p50 0.030 · p95 0.140 · p99 0.376 · max 0.720
- Z5 step face and collar [whole] cad_to_scan: unmasked n 39289 · rms 0.089 · p50 0.034 · p95 0.189 · p99 0.372 · max 0.584 | masked n 35494 · rms 0.068 · p50 0.031 · p95 0.137 · p99 0.275 · max 0.462
- I1 lever pocket floor [interior] scan_to_cad: unmasked n 2493 · rms 0.123 · p50 0.032 · p95 0.306 · p99 0.522 · max 0.675 | masked n 2493 · rms 0.123 · p50 0.032 · p95 0.306 · p99 0.522 · max 0.675
- I1 lever pocket floor [interior] cad_to_scan: unmasked n 9015 · rms 0.932 · p50 0.273 · p95 2.034 · p99 2.457 · max 2.754 | masked n 2962 · rms 0.051 · p50 0.027 · p95 0.105 · p99 0.163 · max 0.252
- I2 stem collar crevice [interior] scan_to_cad: unmasked n 6374 · rms 0.187 · p50 0.078 · p95 0.410 · p99 0.636 · max 1.091 | masked n 6374 · rms 0.187 · p50 0.078 · p95 0.410 · p99 0.636 · max 1.091
- I2 stem collar crevice [interior] cad_to_scan: unmasked n 28300 · rms 0.291 · p50 0.122 · p95 0.654 · p99 0.815 · max 1.143 | masked n 13323 · rms 0.130 · p50 0.062 · p95 0.293 · p99 0.378 · max 0.753
- I3 bore below visible depth [interior] scan_to_cad: unmasked n 268 · rms 0.165 · p50 0.118 · p95 0.335 · p99 0.394 · max 0.596 | masked n 268 · rms 0.165 · p50 0.118 · p95 0.335 · p99 0.394 · max 0.596
- I3 bore below visible depth [interior] cad_to_scan: unmasked n 3920 · rms 1.158 · p50 0.764 · p95 2.294 · p99 2.736 · max 2.987 | masked n 23 · rms 0.111 · p50 0.093 · p95 0.159 · p99 0.161 · max 0.162
- B z 0-5 [region] scan_to_cad: unmasked n 59587 · rms 0.052 · p50 0.016 · p95 0.107 · p99 0.229 · max 0.394 | masked n 59587 · rms 0.052 · p50 0.016 · p95 0.107 · p99 0.229 · max 0.394
- B z 0-5 [region] cad_to_scan: unmasked n 80556 · rms 0.213 · p50 0.021 · p95 0.375 · p99 1.107 · max 2.109 | masked n 67632 · rms 0.052 · p50 0.016 · p95 0.107 · p99 0.228 · max 0.390
- B z 5-13.2 [region] scan_to_cad: unmasked n 46212 · rms 0.121 · p50 0.021 · p95 0.117 · p99 0.201 · max 2.348 | masked n 46212 · rms 0.121 · p50 0.021 · p95 0.117 · p99 0.201 · max 2.348
- B z 5-13.2 [region] cad_to_scan: unmasked n 78603 · rms 0.341 · p50 0.026 · p95 0.717 · p99 1.782 · max 2.754 | masked n 67995 · rms 0.045 · p50 0.022 · p95 0.101 · p99 0.152 · max 0.252
- B z 13.2-17 [region] scan_to_cad: unmasked n 27418 · rms 0.107 · p50 0.035 · p95 0.226 · p99 0.455 · max 1.091 | masked n 27418 · rms 0.107 · p50 0.035 · p95 0.226 · p99 0.455 · max 1.091
- B z 13.2-17 [region] cad_to_scan: unmasked n 58138 · rms 0.178 · p50 0.044 · p95 0.443 · p99 0.727 · max 1.143 | masked n 45779 · rms 0.076 · p50 0.034 · p95 0.156 · p99 0.286 · max 0.694
- B z 17-29.5 [region] scan_to_cad: unmasked n 27519 · rms 0.073 · p50 0.045 · p95 0.148 · p99 0.215 · max 0.336 | masked n 27519 · rms 0.073 · p50 0.045 · p95 0.148 · p99 0.215 · max 0.336
- B z 17-29.5 [region] cad_to_scan: unmasked n 46876 · rms 0.153 · p50 0.058 · p95 0.325 · p99 0.633 · max 0.946 | masked n 41051 · rms 0.101 · p50 0.053 · p95 0.229 · p99 0.323 · max 0.753
- B z 29.5-32.2 neck [region] scan_to_cad: unmasked n 4361 · rms 0.105 · p50 0.052 · p95 0.221 · p99 0.273 · max 0.465 | masked n 4361 · rms 0.105 · p50 0.052 · p95 0.221 · p99 0.273 · max 0.465
- B z 29.5-32.2 neck [region] cad_to_scan: unmasked n 6312 · rms 0.115 · p50 0.055 · p95 0.240 · p99 0.373 · max 0.560 | masked n 5783 · rms 0.115 · p50 0.054 · p95 0.241 · p99 0.379 · max 0.560
- B z 32.2-38.4 sleeve [region] scan_to_cad: unmasked n 17483 · rms 0.089 · p50 0.056 · p95 0.190 · p99 0.250 · max 0.596 | masked n 17483 · rms 0.089 · p50 0.056 · p95 0.190 · p99 0.250 · max 0.596
- B z 32.2-38.4 sleeve [region] cad_to_scan: unmasked n 29515 · rms 0.432 · p50 0.063 · p95 1.047 · p99 2.106 · max 2.987 | masked n 24217 · rms 0.099 · p50 0.054 · p95 0.203 · p99 0.347 · max 0.623

Over-band scan→CAD points (> 0.8 mm): 230 (0.126 %) in 2 clusters ≥ 20 pts.

- cluster 0: n 206, centroid [-2.716, 10.982, 9.34], r [10.633, 12.064], θ [99.6, 108.9], max 2.348 — SCAN ARTEFACT (scan wrong, CAD right); identical to it1 cluster 0. 206 scan pts, r 10.6-12.1, z 6.9-11.1, theta 100-109, d up to 2.35 mm: a curled skin flap hanging 1-2 mm inside the cap wall at the edge of a chrome-reflection hole. All points <=0.75 mm from a scan open boundary (qa/cluster_probe.json); overlays theta=104 and Z=9.3/11.0 show the flap detached from the wall; photos 1,2,4,5 show a smooth intact cap wall. Not modelled; not maskable after the fact.
- cluster 1: n 24, centroid [2.81, -4.756, 15.177], r [5.247, 5.883], θ [295.1, 307.6], max 1.091 — REAL SCAN GEOMETRY the CAD lacks (CAD approximation); same as it1 cluster 1. 24 scan pts, r 5.25-5.9, z 14.9-15.4, theta 295-308, d up to 1.09 mm: at theta ~300 the stem wall continues down to z~15 inside the collar/stem crevice, deeper than the CAD's axisymmetric inner-groove arc (bottom ~16.0); overlay theta=300 shows it, theta 45/104/120 match. Photos 2/4/5 show only a dark gap (depth not resolvable). Points <=0.55 mm from a scan open boundary (crevice floor partly unscanned).

## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | finding | whole part cad_to_scan; zone Z3 stem ribs and core cad_to_scan; zone Z4 crown cap wall lever cad_to_scan |
| CHK-CLUSTER | pass | 2 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | pass | graded after QA's own ICP (35/60 its, converged, 0.073 deg / 0.024 mm); T_refine not written back; no expected value from params.json or the builder; datum audited on the raw scan |
| CHK-LIKE4LIKE | pass | it1 vs it2 under the same protocol (qa/it1_vs_it2.json): regime/masks/zones/icp_scan_masks/datum_spec byte-identical to _it1_SUPERSEDED/qa, same deviation sampling + seeds, same ICP params, same observability params, both OFFICIAL (full-res). Differences are geometry: it1 VALIDITY fail (non-manifold tessellation) cleared; whole CAD->scan masked max 0.893 -> 0.753 and zone Z1 CAD->scan max 0.893 -> 0.517 come from removing the unintended sleeve wedge under the bottom ramp (it1 max located at z 32.4, r 5.7, theta 240-248; qa/c2s_masked_locate.json). Zone Z3 CAD->scan max 0.469 -> 0.567 and B z17-29.5 0.469 -> 0.753 are CAD re-sampling at the collar-mouth/crevice lip z~17.07 (same place it1 had unmasked 0.90), not a new defect. scan->CAD unchanged (p95 0.150, max 2.348). |
| CHK-INDEP | pass | fresh verifier context, own ICP and scripts |
| CHK-FILLET | pass | export_check.json: 4 fillet ops (F04 x2, F06, F07), target == used, all OK |
| CHK-PATCHWORK | pass | census 83 faces (it1 88), QA analytic area 97.6%, 9 B-spline faces only on the helical sleeve ramps (plan-declared helicoids); no loft/ruled/polyline/slice in model.py (grep); model.py diff vs it1 is exactly the two plan-declared construction changes (F11 rib foot -OV, F13 ramp tool floor -h). Tessellation (qa/tess_probe.json): it2 watertight, 0 open / 0 non-manifold edges at 0.003/0.005/0.01/0.02 mm x 0.1 rad and 0.005/0.01 mm x 0.05 rad, both frames. Independent confirmation that it1 had TWO defects: rib foot z 15.99 (all settings) and sleeve bottom z 32.31, r 5.36, theta 192.2 (only at 0.1 rad; it1's single-setting probe missed it). Report-only: BOPAlgo_ArgumentAnalyzer flags 6 InvalidCurveOnSurface pairs (helical ramps z 32.9-37.5, shoulder z 29.2-29.6) in BOTH it1 and it2 (it1 had a 7th at the rib foot, now gone); QA-measured curve-on-surface deviation <= 2.8e-6 mm, below every edge tolerance (qa/cos_dev.json), BRepCheck valid -> analyzer false positive, not a validity fail. |
| CHK-ENUM | finding | E01-E19 present in CAD and consistent with photos 1-5 and overlays (unchanged from it1); E20 bore notch at theta~180 (z 36-37, visible in overlay Z=36.5) not modelled (plan-declared). Assumed closures (bore floor disc z~34.7, lever pocket floor z~8.5) are CAD->scan clusters 1/0 with no scan behind them. Scan->CAD cluster 1 (crevice, theta ~300) is real scan material the CAD lacks. |
| CHK-ACHIEVABLE | n/a | no Tier-1 dims (scan-only) |
| PHOTO-PLAUSIBILITY | pass | photos 1-5 walked: chrome cap with one lever and through-slot pocket (2,4,5), chrome collar rings, white 4-rib stem with a dark gap at the collar (crevice), chrome threaded sleeve, white splined bore (5). Cap wall smooth and intact in every view: the inward scan flap at theta ~100-109 is not a real dent. |

## Misses, per region

- scan_to_cad:masked: p95 0.150 max 2.348 vs 0.3/0.8
- cad_to_scan_observable: p95 0.438 max 2.792 vs 0.3/0.8
- zone:Z4 crown cap wall lever:scan_to_cad: p95 0.111 max 2.348 vs 0.3/0.8
- **whole part scan->CAD max 2.348 (band 0.8) / zone Z4 cap wall scan->CAD max 2.348, theta 100-109, z 6.9-11.1**: scan artefact: chrome skin flap at a reflection hole (cluster 0); CAD matches the photos. p95 passes everywhere (0.150 whole, 0.111 Z4). Options: (a) owner records ACCEPT-BAND naming this miss and citing this gate; (b) rescan the cap with matting spray and re-run verify unchanged; a scan-side mask added now would be after the fact and is not offered.
- **stem/collar crevice theta ~295-308, z 14.9-15.4 (scan->CAD cluster 1, max 1.09)**: non-axisymmetric as-assembled crevice modelled as one revolve groove; floor partly unscanned. Options: (a) accept as a declared simplification under ACCEPT-BAND; (b) a local deepening of the inner groove near theta 300 in a geometry loop (loop 3 of 3) would remove this cluster but would NOT clear the band, which cluster 0 still fails; not recommended on its own.
- **observable CAD->scan p95 0.438 / max 2.792 (band 0.3/0.8); CAD->scan clusters at lever pocket floor z~8.5-11.5 and bore floor disc z~34.7**: CAD surfaces with no scan behind them (assumed pocket floor, assumed bore floor, chrome holes on the cap wall z 1-8); the ray test counts them observable (L4). With the pre-declared masks CAD->scan is p95 0.154 / max 0.753 (passes). Options: (a) ACCEPT-BAND naming cad_to_scan_observable; (b) supply depth readings (caliper/depth gauge) for the pocket floor and bore floor, rebuild those closures and re-verify; (c) fix observability.py (L4) and re-run the gate; no geometry change from the scan alone can fix it.

## Declared limitations (each with its re-run trigger)

1. Tier-1 not run: no calipers (owner, scan-only). Every dimension is ABSENT, not passed. — **Re-run trigger:** any caliper reading supplied -> re-run Tier-1 and this gate
2. Absolute scale not caliper-verified (CHK-SCALE FLAG at intake): units assumed mm, scale_factor 1.0. — **Re-run trigger:** one caliper reading on any feature (e.g. sleeve OD over crests or cap OD)
3. scan_resolution 'full' is an orchestrator inference (DECISIONS.md OTHER), not owner-confirmed. — **Re-run trigger:** owner states the scan is a decimated copy -> relabel INSPECTION ONLY
4. Observability ray test (known defect) counts open-mouthed unscanned regions (lever pocket floor, bore floor, crevice floor) as observable: unobservable fraction only 0.20%, so the gated observable CAD->scan number is inflated. QA coverage proxy (qa/c2s_residual_probe.json, NOT the gate) puts CAD->scan outside scan-hole neighbourhoods at p95 0.155 / max 0.987 (the >0.8 remainder: 5 pts at the unscanned crevice floor z~16.0). — **Re-run trigger:** observability.py fixed to treat unreached cavities as unobservable -> re-run deviation_gate.py
5. Datum audit clock differs 3.88 deg: datum_audit.py's Fourier clock is vertex-count weighted (known defect); QA area-weighted Fourier (3.82 deg) and lever-flank bisector (4.03 deg) in the QA frame reproduce the builder clock within ~0.16 deg (qa/clock_crosscheck.json). Axis 0.02 deg, origin 0.02 mm. — **Re-run trigger:** datum_audit.py fourier clock made area-weighted -> re-run audit
6. Mask-dependent passes: whole-part CAD->scan (unmasked p95 0.458 / max 2.987), zone Z3 CAD->scan (unmasked p95 0.431 / max 0.946), zone Z4 CAD->scan (unmasked p95 0.503 / max 2.754) pass only with the pre-declared M1 open-boundary / M2 skin-normal masks. — **Re-run trigger:** rescan closing the chrome holes / pocket and bore floors -> re-run without masks

## Claim boundary

Scan-only reconstruction under baseline-skill plastic bands, band not met (scan artefacts and unobserved floors). Geometry is one valid, watertight solid. Not fit for manufacture or tooling of the spindle interface (sleeve thread form, bore splines), pocket/bore depths or absolute size until calipered; fit for visual/packaging/envelope use once the owner accepts the listed misses.

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: BAND_NOT_MET, HALT, REVISE._

## Verdict reason

Geometry validity now passes (it1 REVISE cause cleared: tessellation watertight at 12 settings in both frames). The remaining misses are scan->CAD max (2.348, chrome scan flap: scan wrong, CAD right), observable CAD->scan p95/max (unobserved pocket floor / bore floor that the ray test counts as observable) and zone Z4 scan->CAD max (same flap). None can be cleared by more geometry without new data (rescan or depth readings), so REVISE is not the right route; the miss is real, explained per region, and needs an owner ACCEPT-BAND or new data.

Gate identity for an ACCEPT-BAND entry: `qa/gate.json` sha256 `f70ad05cf7ed`, created `2026-09-25T15:11:43+00:00`. band_fails names: `scan_to_cad`, `cad_to_scan_observable`, `zone:Z4 crown cap wall lever:scan_to_cad`.

## Options for the owner (BAND_NOT_MET)

1. **Accept the band miss** and record it: a `DECISIONS.md` `ACCEPT-BAND` line whose evidence file lives outside the pipeline folders (e.g. `decisions/accept_band.md`), cites this gate (sha256 prefix or `created` above) and names the missed band(s) (`scan_to_cad`, `cad_to_scan_observable`, `zone`). Then `deliver/` may proceed with the limitations below.
2. **Rescan** the chrome cap with matting spray (removes the hole-B flap, closes chrome holes) and re-run verify unchanged; expected to clear scan->CAD max / Z4 if the CAD is right, as the photos indicate.
3. **Supply depth readings** (lever-pocket floor depth, bore depth; any caliper reading also clears L1/L2), rebuild those closures and re-verify.
4. **Geometry loop 3 of 3** only for the crevice cluster (local groove deepening at theta ~300): removes cluster 1 but cannot clear the band (cluster 0 remains); not recommended alone.
5. **HALT** if none of the above is wanted.

## it1 vs it2 (CHK-LIKE4LIKE, same protocol; source qa/it1_vs_it2.json)

Protocol: {"inputs_identical": {"regime.json": true, "masks.json": true, "zones.json": true, "icp_scan_masks.json": true, "datum_spec.json": true}, "sampling_identical": true, "icp_params_identical": true, "observability_params_identical": true, "label": ["OFFICIAL (full-res)", "OFFICIAL (full-res)"]}

| Item | it1 | it2 |
|---|---|---|
| OD-S03_steam-knob_datum.step faces / volume / 0.005-0.05 watertight | 88 / 11657.117 / False | 83 / 11655.643 / True |
| OD-S03_steam-knob.step faces / volume / 0.005-0.05 watertight | 88 / 11657.117 / False | 83 / 11655.643 / True |
| ICP its / delta | 44 / 0.073 deg 0.022 mm | 35 / 0.073 deg 0.024 mm |
| datum audit angle / origin / pts p95 | 3.875 / 0.021 / 1.632 | 3.875 / 0.021 / 1.632 |
| scan_to_cad p95 / max | 0.150 / 2.348 | 0.150 / 2.348 |
| cad_to_scan p95 / max | 0.480 / 2.990 | 0.458 / 2.987 |
| cad_to_scan_masked p95 / max | 0.157 / 0.893 | 0.154 / 0.753 |
| cad_to_scan_observable p95 / max | 0.450 / 2.796 | 0.439 / 2.792 |
| zone Z1 threaded sleeve OD scan_to_cad (masked) p95 / max | 0.185 / 0.288 | 0.188 / 0.292 |
| zone Z1 threaded sleeve OD cad_to_scan (masked) p95 / max | 0.200 / 0.893 | 0.182 / 0.517 |
| zone Z2 sleeve bore visible scan_to_cad (masked) p95 / max | 0.166 / 0.370 | 0.168 / 0.371 |
| zone Z2 sleeve bore visible cad_to_scan (masked) p95 / max | 0.167 / 0.514 | 0.169 / 0.518 |
| zone Z3 stem ribs and core scan_to_cad (masked) p95 / max | 0.158 / 0.516 | 0.158 / 0.518 |
| zone Z3 stem ribs and core cad_to_scan (masked) p95 / max | 0.213 / 0.469 | 0.213 / 0.567 |
| zone Z4 crown cap wall lever scan_to_cad (masked) p95 / max | 0.110 / 2.348 | 0.111 / 2.348 |
| zone Z4 crown cap wall lever cad_to_scan (masked) p95 / max | 0.103 / 0.390 | 0.104 / 0.390 |
| zone Z5 step face and collar scan_to_cad (masked) p95 / max | 0.141 / 0.724 | 0.140 / 0.720 |
| zone Z5 step face and collar cad_to_scan (masked) p95 / max | 0.139 / 0.454 | 0.137 / 0.462 |
| zone I1 lever pocket floor scan_to_cad (masked) p95 / max | 0.306 / 0.675 | 0.306 / 0.675 |
| zone I1 lever pocket floor cad_to_scan (masked) p95 / max | 0.103 / 0.259 | 0.105 / 0.252 |
| zone I2 stem collar crevice scan_to_cad (masked) p95 / max | 0.411 / 1.095 | 0.410 / 1.091 |
| zone I2 stem collar crevice cad_to_scan (masked) p95 / max | 0.299 / 0.693 | 0.293 / 0.753 |
| zone I3 bore below visible depth scan_to_cad (masked) p95 / max | 0.333 / 0.598 | 0.335 / 0.596 |
| zone I3 bore below visible depth cad_to_scan (masked) p95 / max | 0.163 / 0.170 | 0.159 / 0.162 |
| zone B z 0-5 scan_to_cad (masked) p95 / max | 0.106 / 0.393 | 0.107 / 0.394 |
| zone B z 0-5 cad_to_scan (masked) p95 / max | 0.105 / 0.390 | 0.107 / 0.390 |
| zone B z 5-13.2 scan_to_cad (masked) p95 / max | 0.117 / 2.348 | 0.117 / 2.348 |
| zone B z 5-13.2 cad_to_scan (masked) p95 / max | 0.101 / 0.259 | 0.101 / 0.252 |
| zone B z 13.2-17 scan_to_cad (masked) p95 / max | 0.228 / 1.095 | 0.227 / 1.091 |
| zone B z 13.2-17 cad_to_scan (masked) p95 / max | 0.159 / 0.693 | 0.156 / 0.694 |
| zone B z 17-29.5 scan_to_cad (masked) p95 / max | 0.149 / 0.335 | 0.148 / 0.336 |
| zone B z 17-29.5 cad_to_scan (masked) p95 / max | 0.227 / 0.469 | 0.229 / 0.753 |
| zone B z 29.5-32.2 neck scan_to_cad (masked) p95 / max | 0.221 / 0.467 | 0.221 / 0.465 |
| zone B z 29.5-32.2 neck cad_to_scan (masked) p95 / max | 0.239 / 0.533 | 0.241 / 0.560 |
| zone B z 32.2-38.4 sleeve scan_to_cad (masked) p95 / max | 0.190 / 0.598 | 0.190 / 0.596 |
| zone B z 32.2-38.4 sleeve cad_to_scan (masked) p95 / max | 0.222 / 0.893 | 0.203 / 0.623 |
| unobservable fraction | 0.0024 | 0.0020 |
| mask-dependent passes | zone Z3 stem ribs and core cad_to_scan; zone Z4 crown cap wall lever cad_to_scan | whole part cad_to_scan; zone Z3 stem ribs and core cad_to_scan; zone Z4 crown cap wall lever cad_to_scan |

Band fails it1 (from _it1_SUPERSEDED/qa/gate.json) vs it2: zone Z1 CAD->scan (max 0.893) no longer fails; the it1 VALIDITY geometry fail is cleared; the other three misses are unchanged (scan artefact / unobserved floors, not geometry).

## Tessellation / watertightness probe (qa/tess_probe.json, both iterations, both frames)

| iter | STEP | tol mm | ang rad | watertight | open | non-manifold |
|---|---|---|---|---|---|---|
| it1 | OD-S03_steam-knob_datum.step | 0.005 | 0.1 | False | 0 | 17 |
| it1 | OD-S03_steam-knob_datum.step | 0.005 | 0.05 | False | 0 | 3 |
| it1 | OD-S03_steam-knob_datum.step | 0.01 | 0.1 | False | 0 | 17 |
| it1 | OD-S03_steam-knob_datum.step | 0.01 | 0.05 | False | 0 | 13 |
| it1 | OD-S03_steam-knob_datum.step | 0.003 | 0.1 | False | 0 | 17 |
| it1 | OD-S03_steam-knob_datum.step | 0.02 | 0.1 | False | 0 | 16 |
| it1 | OD-S03_steam-knob.step | 0.005 | 0.1 | False | 0 | 18 |
| it1 | OD-S03_steam-knob.step | 0.005 | 0.05 | False | 0 | 12 |
| it1 | OD-S03_steam-knob.step | 0.01 | 0.1 | False | 0 | 16 |
| it1 | OD-S03_steam-knob.step | 0.01 | 0.05 | False | 0 | 2 |
| it1 | OD-S03_steam-knob.step | 0.003 | 0.1 | False | 0 | 16 |
| it1 | OD-S03_steam-knob.step | 0.02 | 0.1 | False | 0 | 15 |
| it2 | OD-S03_steam-knob_datum.step | 0.005 | 0.1 | True | 0 | 0 |
| it2 | OD-S03_steam-knob_datum.step | 0.005 | 0.05 | True | 0 | 0 |
| it2 | OD-S03_steam-knob_datum.step | 0.01 | 0.1 | True | 0 | 0 |
| it2 | OD-S03_steam-knob_datum.step | 0.01 | 0.05 | True | 0 | 0 |
| it2 | OD-S03_steam-knob_datum.step | 0.003 | 0.1 | True | 0 | 0 |
| it2 | OD-S03_steam-knob_datum.step | 0.02 | 0.1 | True | 0 | 0 |
| it2 | OD-S03_steam-knob.step | 0.005 | 0.1 | True | 0 | 0 |
| it2 | OD-S03_steam-knob.step | 0.005 | 0.05 | True | 0 | 0 |
| it2 | OD-S03_steam-knob.step | 0.01 | 0.1 | True | 0 | 0 |
| it2 | OD-S03_steam-knob.step | 0.01 | 0.05 | True | 0 | 0 |
| it2 | OD-S03_steam-knob.step | 0.003 | 0.1 | True | 0 | 0 |
| it2 | OD-S03_steam-knob.step | 0.02 | 0.1 | True | 0 | 0 |

it1 defects located (datum frame): rib foot z 15.99 r 6.42 theta 175-182 at every setting; sleeve bottom z 32.31 r 5.36 theta 192.2 only at 0.1 rad (missed by the it1 single-setting probe). it2: none at any setting. B-rep: rib-foot curve-on-surface flag gone; 6 analyzer flags on ramps/shoulder present in both iterations, measured deviation <= 2.8e-6 mm (qa/brep_selfcheck.json, qa/cos_dev.json), report-only.
