# VERDICT: BAND_NOT_MET

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: Fresh QA subagent (it3) that did not build the model and did not run it1/it2 QA; all numbers from stl-re-verify scripts on the full-res input/scan.stl (sha256 a0e8b66e... matches INPUT_HASHES.json). Builder numbers (build_log, selfcheck, measure/) not read or used; build/model.py only grepped read-only for CHK-PATCHWORK; MODELING_PLAN §8 read only to learn what changed. Own datum audit and own ICP (T_refine QA-only, not written back). deviation_gate.py run unchanged through the thin low-memory wrapper reused from it2 (scratchpad qa_work_it3/run_devgate_lowmem.py, byte copy of qa_work_it2's) that only lowers batch sizes (dist chunk 10k, ray chunk 25) for the 15 GB container; batching does not change any number. Zoom sections (qa/overlays/zoom_clusters_qa.png) drawn by a QA-only script on QA's own tessellation of the datum STEP.

Scan: `input/scan.stl` (full-res), label **OFFICIAL (full-res)**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-E02_control-button-board_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 36865.172 mm³ | PASS |
| Validity `OD-E02_control-button-board.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 36865.172 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 0.068° / origin 0.014 mm / points p95 0.056 max 0.062 mm | within (not blocking) |
| Registration (ICP) | converged | 33/60 its, 0.087° / 0.023 mm | PASS |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 294367 · rms 0.109 · p50 0.044 · p95 0.237 · p99 0.395 · max 0.922 | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 19695 · rms 0.537 · p50 0.043 · p95 0.633 · p99 3.167 · max 5.422 | FAIL |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 294367 · rms 0.109 · p50 0.044 · p95 0.237 · p99 0.395 · max 0.922
- scan→CAD masked: n 294367 · rms 0.109 · p50 0.044 · p95 0.237 · p99 0.395 · max 0.922
- CAD→scan unmasked: n 300000 · rms 0.558 · p50 0.043 · p95 0.930 · p99 3.175 · max 5.472
- CAD→scan masked: n 270144 · rms 0.264 · p50 0.038 · p95 0.283 · p99 1.223 · max 5.406
- CAD→scan observable only: n 19695 · rms 0.537 · p50 0.043 · p95 0.633 · p99 3.167 · max 5.422; unobservable fraction 1.52 %

Masks:

- **M3 open boundary** (cad_to_scan): distance from CAD to the edge of a scan hole (23 open loops, INTAKE_CARD §2-§3) is not a surface deviation; fraction 8.87 %; inside n 26608 · rms 1.643 · p50 0.567 · p95 3.730 · p99 4.588 · max 5.472
- **M4 skin normal** (cad_to_scan): a CAD point whose nearest scan triangle faces >70 deg away is an occluded/opposite-wall correspondence, not a skin deviation; fraction 2.40 %; inside n 7191 · rms 1.586 · p50 0.618 · p95 3.474 · p99 4.483 · max 5.404

Zones:

- Z1 back cover floor [functional_interface] scan_to_cad: unmasked n 19834 · rms 0.041 · p50 0.023 · p95 0.077 · p99 0.141 · max 0.555 | masked n 19834 · rms 0.041 · p50 0.023 · p95 0.077 · p99 0.141 · max 0.555
- Z1 back cover floor [functional_interface] cad_to_scan: unmasked n 28966 · rms 0.257 · p50 0.024 · p95 0.148 · p99 1.690 · max 2.804 | masked n 27472 · rms 0.065 · p50 0.023 · p95 0.073 · p99 0.210 · max 2.804
- Z2 housing tiers [functional_interface] scan_to_cad: unmasked n 108878 · rms 0.108 · p50 0.049 · p95 0.229 · p99 0.373 · max 0.737 | masked n 108878 · rms 0.108 · p50 0.049 · p95 0.229 · p99 0.373 · max 0.737
- Z2 housing tiers [functional_interface] cad_to_scan: unmasked n 106394 · rms 0.865 · p50 0.058 · p95 2.364 · p99 4.012 · max 5.472 | masked n 91236 · rms 0.363 · p50 0.048 · p95 0.269 · p99 1.921 · max 5.406
- Z3 caps and collars [functional_interface] scan_to_cad: unmasked n 46334 · rms 0.102 · p50 0.050 · p95 0.208 · p99 0.364 · max 0.922 | masked n 46334 · rms 0.102 · p50 0.050 · p95 0.208 · p99 0.364 · max 0.922
- Z3 caps and collars [functional_interface] cad_to_scan: unmasked n 36613 · rms 0.150 · p50 0.045 · p95 0.347 · p99 0.672 · max 1.136 | masked n 31742 · rms 0.096 · p50 0.040 · p95 0.156 · p99 0.448 · max 0.892
- Z4 mounting tab [functional_interface] scan_to_cad: unmasked n 38865 · rms 0.062 · p50 0.021 · p95 0.134 · p99 0.275 · max 0.396 | masked n 38865 · rms 0.062 · p50 0.021 · p95 0.134 · p99 0.275 · max 0.396
- Z4 mounting tab [functional_interface] cad_to_scan: unmasked n 44247 · rms 0.068 · p50 0.019 · p95 0.121 · p99 0.368 · max 0.579 | masked n 43860 · rms 0.068 · p50 0.018 · p95 0.118 · p99 0.368 · max 0.579
- Z5 screw holes [functional_interface] scan_to_cad: unmasked n 5970 · rms 0.073 · p50 0.034 · p95 0.154 · p99 0.260 · max 0.440 | masked n 5970 · rms 0.073 · p50 0.034 · p95 0.154 · p99 0.260 · max 0.440
- Z5 screw holes [functional_interface] cad_to_scan: unmasked n 9232 · rms 1.440 · p50 0.145 · p95 3.302 · p99 3.909 · max 4.454 | masked n 3809 · rms 0.093 · p50 0.029 · p95 0.211 · p99 0.361 · max 0.679
- Z6 connector shroud [functional_interface] scan_to_cad: unmasked n 25033 · rms 0.137 · p50 0.066 · p95 0.275 · p99 0.575 · max 0.761 | masked n 25033 · rms 0.137 · p50 0.066 · p95 0.275 · p99 0.575 · max 0.761
- Z6 connector shroud [functional_interface] cad_to_scan: unmasked n 30450 · rms 0.389 · p50 0.076 · p95 1.048 · p99 1.561 · max 2.839 | masked n 26429 · rms 0.282 · p50 0.069 · p95 0.710 · p99 1.172 · max 2.434
- I1 shroud interior [interior] scan_to_cad: unmasked n 1665 · rms 0.175 · p50 0.152 · p95 0.301 · p99 0.464 · max 0.574 | masked n 1665 · rms 0.175 · p50 0.152 · p95 0.301 · p99 0.464 · max 0.574
- I1 shroud interior [interior] cad_to_scan: unmasked n 5427 · rms 3.002 · p50 2.854 · p95 4.645 · p99 5.122 · max 5.472 | masked n 719 · rms 3.057 · p50 3.195 · p95 4.706 · p99 5.238 · max 5.406
- I2 cap-collar gaps [interior] scan_to_cad: unmasked n 12049 · rms 0.155 · p50 0.087 · p95 0.322 · p99 0.491 · max 0.922 | masked n 12049 · rms 0.155 · p50 0.087 · p95 0.322 · p99 0.491 · max 0.922
- I2 cap-collar gaps [interior] cad_to_scan: unmasked n 8782 · rms 0.227 · p50 0.091 · p95 0.558 · p99 0.720 · max 1.136 | masked n 6215 · rms 0.166 · p50 0.074 · p95 0.390 · p99 0.630 · max 0.812
- zb tab z>5 [region] scan_to_cad: unmasked n 54977 · rms 0.088 · p50 0.027 · p95 0.172 · p99 0.360 · max 0.761 | masked n 54977 · rms 0.088 · p50 0.027 · p95 0.172 · p99 0.360 · max 0.761
- zb tab z>5 [region] cad_to_scan: unmasked n 61464 · rms 0.103 · p50 0.023 · p95 0.180 · p99 0.505 · max 0.817 | masked n 60876 · rms 0.102 · p50 0.022 · p95 0.176 · p99 0.503 · max 0.817
- zb rim z0-5 [region] scan_to_cad: unmasked n 68937 · rms 0.135 · p50 0.062 · p95 0.298 · p99 0.452 · max 0.723 | masked n 68937 · rms 0.135 · p50 0.062 · p95 0.298 · p99 0.452 · max 0.723
- zb rim z0-5 [region] cad_to_scan: unmasked n 93204 · rms 0.352 · p50 0.048 · p95 0.997 · p99 1.474 · max 3.001 | masked n 84301 · rms 0.259 · p50 0.042 · p95 0.406 · p99 1.299 · max 2.816
- zb tiers z-13.2-0 [region] scan_to_cad: unmasked n 104469 · rms 0.101 · p50 0.044 · p95 0.216 · p99 0.362 · max 0.737 | masked n 104469 · rms 0.101 · p50 0.044 · p95 0.216 · p99 0.362 · max 0.737
- zb tiers z-13.2-0 [region] cad_to_scan: unmasked n 89539 · rms 0.943 · p50 0.060 · p95 2.657 · p99 4.131 · max 5.472 | masked n 75981 · rms 0.396 · p50 0.048 · p95 0.272 · p99 2.378 · max 5.406
- zb band z-16.2--13.2 [region] scan_to_cad: unmasked n 19650 · rms 0.113 · p50 0.057 · p95 0.239 · p99 0.356 · max 0.679 | masked n 19650 · rms 0.113 · p50 0.057 · p95 0.239 · p99 0.356 · max 0.679
- zb band z-16.2--13.2 [region] cad_to_scan: unmasked n 19180 · rms 0.176 · p50 0.057 · p95 0.409 · p99 0.706 · max 1.091 | masked n 17244 · rms 0.128 · p50 0.052 · p95 0.264 · p99 0.549 · max 0.812
- zb collars z-19.2--16.2 [region] scan_to_cad: unmasked n 20302 · rms 0.134 · p50 0.068 · p95 0.291 · p99 0.444 · max 0.922 | masked n 20302 · rms 0.134 · p50 0.068 · p95 0.291 · p99 0.444 · max 0.922
- zb collars z-19.2--16.2 [region] cad_to_scan: unmasked n 15021 · rms 0.225 · p50 0.073 · p95 0.558 · p99 0.758 · max 1.136 | masked n 10207 · rms 0.149 · p50 0.053 · p95 0.305 · p99 0.655 · max 0.892
- zb caps z<-19.2 [region] scan_to_cad: unmasked n 26032 · rms 0.067 · p50 0.042 · p95 0.129 · p99 0.185 · max 0.737 | masked n 26032 · rms 0.067 · p50 0.042 · p95 0.129 · p99 0.185 · max 0.737
- zb caps z<-19.2 [region] cad_to_scan: unmasked n 21592 · rms 0.055 · p50 0.036 · p95 0.109 · p99 0.146 · max 0.218 | masked n 21535 · rms 0.055 · p50 0.036 · p95 0.109 · p99 0.146 · max 0.215

Over-band scan→CAD points (> 0.8 mm): 9 (0.003 %) in 0 clusters ≥ 20 pts.


## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | pass | no pass depends on a mask |
| CHK-CLUSTER | pass | 0 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | pass | QA datum not ICP'd to its own CAD; gate uses QA's own ICP on the raw full-res scan; no expected value taken from params.json or the builder. The builder self-check in MODELING_PLAN §8 (datum frame, 200k samples) is a consistency check, not independent evidence, and is not compared. |
| CHK-LIKE4LIKE | pass | Same protocol as it2 (and it1): regime.json, zones.json, masks.json, datum_spec.json, icp_scan_masks.json byte-identical to _it2_SUPERSEDED/qa; ICP params identical (3M/seed 11, 300k/seed 13, 70 deg, 0.8 mm, 3.0 mm, cap 60, tol 1e-6); sampling identical (all scan verts, 300k CAD seed 2, k 8, n_samp 3M seed 0; observability 20k seed 5, 0.5 mm, 60 deg cone); same overlay panel set. Only the CAD changed. After ICP it1 -> it2 -> it3: scan->CAD p95 0.243 -> 0.243 -> 0.237, max 1.690 -> 1.062 -> 0.922, scan pts >0.8 81 -> 24 -> 9; CAD->scan observable p95 0.674 -> 0.650 -> 0.633, max 5.119 -> 5.358 -> 5.422; CAD->scan raw p95 0.973 -> 0.943 -> 0.931; CAD pts >0.8 16,672 -> 16,189 -> 15,903. Improvement is geometry (it3: sloped recess profiles, B1/B3 middle sectors), not protocol. |
| CHK-INDEP | pass | fresh agent, own scripts; see independence |
| CHK-FILLET | finding | export_check.json (datum and scan frames) and fillets.json: 22 fillets, 20 OK, 2 REDUCED: F02 rim top outer edge 0.5451 -> 0.4777, F13 shroud top inner edge 0.6254 -> 0.5031 (wall too thin for both measured rounds), declared in MODELING_PLAN §0. Unchanged from it1/it2. No FAILED/NO_EDGES. |
| CHK-PATCHWORK | pass | 374 faces, analytic area share 95.4% (plane 201, cylinder 110, torus 36, cone 3, revolution 6, extrusion 2, bspline 16). model.py grep: no loft(, ruled, Polyline, sweep, spline; Wire.make_polygon builds the tab YZ profile (fitted plane-line intersections) and, new in it3, a 5-point (r,z) recess profile that is revolved (recess_cone -> planes + cones), not a scan-slice stack. |
| CHK-ENUM | finding | Every intake feature E01-E18 is present in CAD sections. Finding (carried from it2, reduced not removed): the scanned surface at the tip of the B1 side-collar tilted cut inside the B1 cap-collar gap, around (-28.9, 1.15, -16.6), curves where the CAD cut is a straight plane; 9 scan pts over 0.8 (max 0.922, it2 24 pts / 1.062). Logos/icons (E13) not modelled (declared cosmetic). No invented CAD feature except assumed closures in unscanned regions (shroud interior floor z -2.33, slot floor, through-bores, recess ceilings). |
| CHK-ACHIEVABLE | n/a | no Tier-1 (scan-only job, no calipers) |
| PHOTO-PLAUSIBILITY | pass | photo 1 (back + 3/4 front) and photo 2 (front) walked: shroud with white pin header, 2 screw holes, tab with hole and side flanges, 4 latch hoops, stepped tiers, 3 caps with slanted side tops, collars; all present in CAD except the header pins and logos/icons (declared). |

## Misses, per region

- scan_to_cad:masked: p95 0.237 max 0.922 vs 0.3/0.8
- cad_to_scan_observable: p95 0.633 max 5.422 vs 0.3/0.8
- **whole part CAD->scan observable (p95 0.633 > 0.30, max 5.422 > 0.80)**: 15,903 of 300,000 CAD samples (5.30%) over 0.8 mm; 15,661 (98.5%) lie in four unscanned openings (shroud interior 7639, shroud-to-rim slot 4179, screw bores 1938 + 1905) whose CAD surfaces are assumptions with no scan behind them; 74 on the B3 recess ceiling, 53 on the B1 wedge floor, 29 at a scan hole on the -Y hoop notch wall, 86 in small groups. Only 1.52% of the CAD is ray-unobservable, so the observable split does not remove the openings. Informational (not a gate, not a mask): CAD->scan raw outside the four opening boxes reads p95 0.276 / max 1.136 (242 pts > 0.8). Datum frame reads p95 0.628 / max 5.416, so not a registration effect. Three geometry loops moved this p95 only 0.674 -> 0.650 -> 0.633: geometry built from this scan cannot close it. Options: (a) owner accepts BAND_NOT_MET with the openings declared as assumed geometry (ACCEPT-BAND in DECISIONS.md citing this gate.json); (b) supply data: a re-scan of the shroud interior, slot and bores, or depth / pin-gauge readings, then re-run; (c) HALT. Not REVISE: loop 3 of 3 is used and no geometry change from the existing scan can clear it.
- **whole part scan->CAD max (0.922 > 0.80; p95 0.237 passes; unmasked = masked, no scan masks)**: 9 of 294,367 scan vertices (0.003%) over 0.8 mm, one group of < 20 pts at the tip of the B1 side-collar tilted cut inside the B1 cap-collar gap (-28.9, 1.15, -16.6): the scanned surface curves where the CAD cut is a plane (max 0.122 over band). it1 81 pts / 1.690, it2 24 / 1.062, it3 9 / 0.922. Datum frame max 0.911. This is a geometry approximation of real scan material in an occluded ~1 mm gap, not a data gap; in principle a finer side-collar cut would clear it, but loop 3 of 3 is used, and fixing it alone would not pass the part because of the CAD->scan miss above. Options: (a) owner accepts the 9-point, 0.12 mm over-band residual inside the B1 cap-collar gap (ACCEPT-BAND); (b) owner authorises one extra geometry loop beyond the 3-loop limit to shape the B1 side-collar cut tip (would not clear the CAD->scan miss); (c) HALT.

## Declared limitations (each with its re-run trigger)

1. Scan-only: Tier-1 not run, absolute scale not caliper-verified (CHK-SCALE flag at intake). — **Re-run trigger:** any caliper reading (e.g. envelope X/Y, cap diameter, tab hole)
2. Unscanned regions are modelled from assumptions: shroud interior depth, shroud-to-rim slot floor, screw through-bores, cap-collar recess ceilings, B1/B3 wedge floors. The four opening clusters hold 15,661 of the 15,903 CAD->scan points over 0.8 mm (98.5%); the OD ray heuristic counts them observable because they open to the outside (unobservable fraction only 1.52%). — **Re-run trigger:** a re-scan covering the shroud interior, slot, bores and cap gaps, or depth/pin-gauge readings of them
3. Functional zones Z1-Z6 are reported per zone only: baseline-skill has interface_max_mm = null; their points are inside the whole-part gate. — **Re-run trigger:** a project spec that bands the interfaces
4. Two fillets REDUCED (F02 rim top outer 0.545 -> 0.478; F13 shroud top inner 0.625 -> 0.503). — **Re-run trigger:** wall thickness caliper reading on rim and shroud
5. Loose button caps modelled at their scanned pose (B2 tilted ~1.6 deg in its bore); the fused solid is the assembly as scanned. — **Re-run trigger:** owner request for per-part STEP or nominal cap pose
6. Overlays and zoom sections are drawn in the builder datum frame (pre-ICP; ICP correction 0.087 deg / 0.023 mm). — **Re-run trigger:** ICP correction above 0.1 mm on a re-run

## Claim boundary

Not an approved model. Not fit for tooling, manufacture or fit-critical use of the connector shroud interior, the shroud-to-rim slot, the screw bores or the cap-collar gaps (assumed, unscanned geometry). Scale is not caliper-verified. The outer housing, tab, caps and back floor agree with the scan within p95 0.30 mm scan->CAD (whole-part scan->CAD p95 0.237, max 0.922 at one 9-point spot); that is the only claim.

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: BAND_NOT_MET, HALT, REVISE._
