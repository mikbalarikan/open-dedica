# VERDICT: BAND_NOT_MET

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: fresh verify agent (it2) that did not build the model; QA scripts from skills/stl-re-verify only; every number re-derived on the raw full-res input/scan.stl (sha256 41448c67..., re-hashed = INPUT_HASHES.json); build/model.py only grepped read-only (CHK-PATCHWORK); measure/params.json values, build/build_log.txt, measure/figures and the builder scratchpad were not read; builder self-check numbers in MODELING_PLAN §8 not used.

Scan: `input/scan.stl` (full-res), label **OFFICIAL (full-res)**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-E01_Power-PCB_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 20609.895 mm³ | PASS |
| Validity `OD-E01_Power-PCB.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 20609.895 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 0.074° / origin 0.080 mm / points p95 0.064 max 0.088 mm | within (not blocking) |
| Registration (ICP) | converged | 65/200 its, 0.147° / 0.725 mm | PASS |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 203996 · rms 0.455 · p50 0.289 · p95 0.763 · p99 0.784 · max 1.365 | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 18392 · rms 0.830 · p50 0.672 · p95 1.599 · p99 2.738 · max 4.408 | FAIL |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 203996 · rms 0.455 · p50 0.289 · p95 0.763 · p99 0.784 · max 1.365
- scan→CAD masked: n 203996 · rms 0.455 · p50 0.289 · p95 0.763 · p99 0.784 · max 1.365
- CAD→scan unmasked: n 300000 · rms 0.942 · p50 0.693 · p95 1.986 · p99 3.137 · max 5.068
- CAD→scan masked: n 135843 · rms 0.583 · p50 0.585 · p95 0.892 · p99 1.227 · max 4.503
- CAD→scan observable only: n 18392 · rms 0.830 · p50 0.672 · p95 1.599 · p99 2.738 · max 4.408; unobservable fraction 8.04 %

Masks:

- **M1 solder side unscanned** (cad_to_scan): the board bottom (solder side) was never scanned, so CAD->scan distance there measures the invented flat bottom face against the board top/edges, not a surface deviation; fraction 24.10 %; inside n 72286 · rms 1.021 · p50 0.854 · p95 1.811 · p99 2.653 · max 4.425
- **M2 scan open boundary** (cad_to_scan): distance measured to a scan hole EDGE (55 open-boundary loops: connector cavities, under heatsink, hole bores) is not a surface deviation; fraction 31.55 %; inside n 94663 · rms 1.298 · p50 0.732 · p95 2.790 · p99 3.693 · max 5.068
- **M3 skin normal disagreement** (cad_to_scan): a CAD point whose nearest scan triangle faces > 70 deg away is an occluded/interior correspondence, not an outer-skin deviation; fraction 9.22 %; inside n 27647 · rms 1.333 · p50 0.645 · p95 2.927 · p99 3.855 · max 4.997

Zones:

- I1 board top face [functional_interface] scan_to_cad: unmasked n 1912 · rms 0.478 · p50 0.465 · p95 0.694 · p99 0.737 · max 0.891 | masked n 1912 · rms 0.478 · p50 0.465 · p95 0.694 · p99 0.737 · max 0.891
- I1 board top face [functional_interface] cad_to_scan: unmasked n 58941 · rms 0.746 · p50 0.706 · p95 0.961 · p99 1.628 · max 3.437 | masked n 49044 · rms 0.729 · p50 0.717 · p95 0.914 · p99 1.043 · max 1.705
- I1 board outline edges [functional_interface] scan_to_cad: unmasked n 3973 · rms 0.138 · p50 0.096 · p95 0.278 · p99 0.361 · max 0.448 | masked n 3973 · rms 0.138 · p50 0.096 · p95 0.278 · p99 0.361 · max 0.448
- I1 board outline edges [functional_interface] cad_to_scan: unmasked n 5997 · rms 0.436 · p50 0.283 · p95 0.842 · p99 1.044 · max 1.231 | masked n 4097 · rms 0.465 · p50 0.361 · p95 0.847 · p99 1.041 · max 1.231
- I2 mounting holes H1 H2 [functional_interface] scan_to_cad: unmasked n 316 · rms 0.083 · p50 0.049 · p95 0.162 · p99 0.271 · max 0.423 | masked n 316 · rms 0.083 · p50 0.049 · p95 0.162 · p99 0.271 · max 0.423
- I2 mounting holes H1 H2 [functional_interface] cad_to_scan: unmasked n 506 · rms 0.428 · p50 0.214 · p95 0.893 · p99 0.994 · max 1.065 | masked n 288 · rms 0.281 · p50 0.105 · p95 0.646 · p99 0.811 · max 0.966
- I3 faston tab row [functional_interface] scan_to_cad: unmasked n 12734 · rms 0.145 · p50 0.071 · p95 0.319 · p99 0.500 · max 0.796 | masked n 12734 · rms 0.145 · p50 0.071 · p95 0.319 · p99 0.500 · max 0.796
- I3 faston tab row [functional_interface] cad_to_scan: unmasked n 11473 · rms 0.220 · p50 0.079 · p95 0.578 · p99 0.785 · max 0.919 | masked n 10532 · rms 0.204 · p50 0.074 · p95 0.551 · p99 0.784 · max 0.919
- I4 heatsink top and tallest parts [functional_interface] scan_to_cad: unmasked n 28912 · rms 0.293 · p50 0.147 · p95 0.644 · p99 0.791 · max 1.142 | masked n 28912 · rms 0.293 · p50 0.147 · p95 0.644 · p99 0.791 · max 1.142
- I4 heatsink top and tallest parts [functional_interface] cad_to_scan: unmasked n 43065 · rms 0.971 · p50 0.521 · p95 2.248 · p99 2.899 · max 3.655 | masked n 15354 · rms 0.487 · p50 0.231 · p95 0.981 · p99 1.127 · max 2.500
- X solder side [interior] scan_to_cad: unmasked n 8732 · rms 0.421 · p50 0.284 · p95 0.784 · p99 0.963 · max 1.293 | masked n 8732 · rms 0.421 · p50 0.284 · p95 0.784 · p99 0.963 · max 1.293
- X solder side [interior] cad_to_scan: unmasked n 73503 · rms 1.012 · p50 0.852 · p95 1.800 · p99 2.649 · max 4.425 | masked n 257 · rms 0.073 · p50 0.054 · p95 0.124 · p99 0.219 · max 0.315
- X under heatsink clip TO-220 [interior] scan_to_cad: unmasked n 15565 · rms 0.253 · p50 0.143 · p95 0.536 · p99 0.813 · max 1.365 | masked n 15565 · rms 0.253 · p50 0.143 · p95 0.536 · p99 0.813 · max 1.365
- X under heatsink clip TO-220 [interior] cad_to_scan: unmasked n 38095 · rms 1.563 · p50 0.767 · p95 3.336 · p99 4.130 · max 5.068 | masked n 11514 · rms 0.754 · p50 0.247 · p95 1.616 · p99 3.056 · max 4.503
- X between caps [interior] scan_to_cad: unmasked n 5239 · rms 0.216 · p50 0.061 · p95 0.587 · p99 0.746 · max 0.987 | masked n 5239 · rms 0.216 · p50 0.061 · p95 0.587 · p99 0.746 · max 0.987
- X between caps [interior] cad_to_scan: unmasked n 6430 · rms 0.447 · p50 0.078 · p95 1.080 · p99 1.589 · max 2.099 | masked n 3904 · rms 0.213 · p50 0.054 · p95 0.604 · p99 0.756 · max 1.343
- Z1 board band z<0.3 [region] scan_to_cad: unmasked n 95621 · rms 0.604 · p50 0.650 · p95 0.772 · p99 0.781 · max 1.293 | masked n 95621 · rms 0.604 · p50 0.650 · p95 0.772 · p99 0.781 · max 1.293
- Z1 board band z<0.3 [region] cad_to_scan: unmasked n 144026 · rms 0.885 · p50 0.777 · p95 1.413 · p99 2.460 · max 4.425 | masked n 56579 · rms 0.697 · p50 0.703 · p95 0.907 · p99 1.042 · max 2.309
- Z2 low parts z 0.3-3 [region] scan_to_cad: unmasked n 27036 · rms 0.292 · p50 0.108 · p95 0.695 · p99 0.819 · max 1.164 | masked n 27036 · rms 0.292 · p50 0.108 · p95 0.695 · p99 0.819 · max 1.164
- Z2 low parts z 0.3-3 [region] cad_to_scan: unmasked n 35152 · rms 0.717 · p50 0.306 · p95 1.545 · p99 2.409 · max 3.574 | masked n 19840 · rms 0.471 · p50 0.140 · p95 0.858 · p99 1.193 · max 2.309
- Z3 mid parts z 3-12 [region] scan_to_cad: unmasked n 52427 · rms 0.225 · p50 0.093 · p95 0.528 · p99 0.717 · max 1.365 | masked n 52427 · rms 0.225 · p50 0.093 · p95 0.528 · p99 0.717 · max 1.365
- Z3 mid parts z 3-12 [region] cad_to_scan: unmasked n 77757 · rms 1.104 · p50 0.300 · p95 2.777 · p99 3.818 · max 5.068 | masked n 44070 · rms 0.490 · p50 0.121 · p95 0.832 · p99 1.791 · max 4.503
- Z4 high parts z>12 [region] scan_to_cad: unmasked n 28912 · rms 0.293 · p50 0.147 · p95 0.644 · p99 0.791 · max 1.142 | masked n 28912 · rms 0.293 · p50 0.147 · p95 0.644 · p99 0.791 · max 1.142
- Z4 high parts z>12 [region] cad_to_scan: unmasked n 43065 · rms 0.971 · p50 0.521 · p95 2.248 · p99 2.899 · max 3.655 | masked n 15354 · rms 0.487 · p50 0.231 · p95 0.981 · p99 1.127 · max 2.500

Over-band scan→CAD points (> 0.8 mm): 1576 (0.773 %) in 21 clusters ≥ 20 pts.

- cluster 0: n 131, centroid [47.962, -22.396, 20.934], r [50.888, 55.041], θ [331.1, 341.3], max 1.142 — Spine z~21.6 surface (x 47.0-48.4, y -26.6..-16.3): scanned surface INSIDE the modelled heatsink spine in the plane of the TO-220 tab top. Same scan points in the datum frame p50 0.73 / max 0.96 (38% > 0.8), and it is the only >=20-point over-band cluster in the datum frame. Not modelled by design (MODELING_PLAN §9: likely reconstruction artefact continuing the tab-top surface; cannot be reached by a straight line from outside). UNRESOLVED: real slot vs artefact is not decidable from scan or photos (limitation L7).
- cluster 1: n 122, centroid [0.236, 0.434, -2.547], r [1.746, 2.16], θ [5.3, 354.7], max 1.293 — ICP-bias artefact: H1 bore lower rim / board-bottom edge fringe (gate-frame z -2.8..-2.4). Same points in the datum frame p50 0.26 / max 0.59 (within band). Caused by the +0.72 mm z lift of the QA ICP (L3).
- cluster 2: n 113, centroid [10.216, -51.491, 2.053], r [50.274, 55.077], θ [279.0, 283.4], max 0.855 — ICP-bias artefact: flat top of a low box (x 8.0-11.7, y -53.9..-49.0). Datum frame p50 0.008 / max 0.041.
- cluster 3: n 69, centroid [47.562, -21.583, 5.066], r [50.471, 53.615], θ [332.4, 340.6], max 1.365 — Spine notch / TO-220 body at z~5 (x 47.4-47.7, y -24.9..-16.8), partly occluded zone under the heatsink. Datum frame p50 0.33 / max 0.79 (within band); over band only through the ICP bias.
- cluster 4: n 61, centroid [-0.375, -31.29, 2.37], r [30.053, 32.993], θ [265.6, 271.9], max 0.949 — ICP-bias artefact: block top (x -2.3..1.0, y -33..-30). Datum frame p50 0.035 / max 0.16.
- cluster 5: n 48, centroid [49.645, -55.901, -2.429], r [71.305, 78.552], θ [308.3, 314.6], max 0.984 — ICP-bias artefact: board bottom edge fringe along the y -56 edge (x 44-55). Datum frame p50 0.10 / max 0.20.
- cluster 6: n 48, centroid [7.726, 3.756, -2.473], r [5.549, 12.551], θ [17.7, 43.6], max 1.101 — ICP-bias artefact: board bottom edge fringe along the y +3.8 edge (x 4-12). Datum frame p50 0.19 / max 0.40.
- cluster 7: n 47, centroid [44.8, -24.309, 14.11], r [49.187, 52.515], θ [329.9, 333.2], max 0.963 — ICP-bias artefact: horizontal top at z~14 beside the TO-220 / clip (x 43.7-46.0, y -25.4..-22.2). Datum frame p50 0.15 / max 0.25.
- cluster 8: n 46, centroid [11.466, -36.225, 1.88], r [37.789, 38.101], θ [286.8, 287.8], max 1.164 — ICP-bias artefact: low part top at (11.5,-36.2,z~1.9). Datum frame p50 0.24 / max 0.38.
- cluster 9: n 43, centroid [73.454, -15.963, 11.121], r [74.042, 76.517], θ [346.5, 348.8], max 0.893 — ICP-bias artefact: can top at z~11.1 (x 72.2-74.8, y -17.8..-14.4). Datum frame p50 0.17 / max 0.24.
- cluster 10: n 42, centroid [27.493, -51.48, 1.51], r [55.768, 59.512], θ [296.5, 300.0], max 0.922 — ICP-bias artefact: SMD box top (x 25.5-29.3, y -52.6..-49.2). Datum frame p50 0.023 / max 0.13.
- cluster 11: n 37, centroid [85.692, -43.344, 2.213], r [95.243, 96.266], θ [332.6, 333.8], max 1.085 — Y-cap lead wire (x 85.3-86.4, y -44.3..-42.1, z 0.8-4.0): lead modelled as a standard 0.8 mm straight wire; datum frame p50 0.58 / max 0.83 (3 of 37 points > 0.8, by 0.03 mm); rest of the excess is the ICP bias. Minor lead-path residual.

## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | pass | no pass depends on a mask |
| CHK-CLUSTER | pass | 12 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | finding | QA gate independent: QA's own datum audit on the raw scan (0.074 deg / 0.080 mm), QA's own ICP (T_refine never written back to intake/alignment.json), no expected value from params.json or the builder. Finding (carried from it1): the builder record contains self-referential checks - MODELING_PLAN §8 builder self-check against the same scan (it2: scan->CAD p95 0.259 / max 0.968) and the intake datum try 2 noise floor measured on the board top itself (DECISIONS.md) - consistency checks, not independent evidence. |
| CHK-LIKE4LIKE | pass | it1 (_it1_SUPERSEDED/qa) vs it2 use the same protocol: same regime file, identical zones.json predicates and masks.json masks/parameters (M1 region, M2 open boundary 0.8, M3 normal 70), same ICP parameters incl. the same once-raised cap 200, same deviation sampling (all scan vertices, 300k CAD samples seed 2, k 8, n_samp 3M, obs 20k seed 5), same datum spec regions. Deltas therefore come from geometry: gate scan->CAD p95 0.764 -> 0.763, max 1.501 -> 1.365; gate CAD->scan observable p95 1.623 -> 1.599, max 4.408 -> 4.408; datum-frame scan->CAD p95 0.294 -> 0.292, max 1.499 -> 1.027; diagnostic max-corr-1.0 run scan->CAD max 1.509 -> 1.068; ICP 0.162 deg/0.726 mm (62 its) -> 0.147 deg/0.725 mm (65 its). Per it1 finding region, same scan points, datum frame (it1 -> it2): C5 ring part max 1.499 -> 0.543; J3 cavity floor max 1.487 (43.5% > 0.8) -> 0.314 (0%); TO-220 tab/spine hole max 1.201 -> 0.719; K2 bump max 1.141 -> 0.332; hub-channel / clip lower hook (48.5,-37.6) max 0.977 -> 0.623; spine z~21.6 surface max 0.963 -> 0.963 (unchanged, not modelled by design). |
| CHK-INDEP | pass | fresh agent; see independence |
| CHK-FILLET | pass | MODELING_PLAN §5 plans no fillet/chamfer operation; build/fillets.json and export_check.json fillets empty (0 OK/REDUCED/FAILED/NO_EDGES/SELECTOR_ERROR); nothing skipped or shrunk. |
| CHK-PATCHWORK | pass | QA census (qa/step_check.json): 1233 faces, 100% analytic area (plane 1054, cylinder 178, torus 1), no B-spline/ruled faces; plane faces are ~60 SMD boxes and component bodies, not facets. model.py grep: no loft/ruled; Wire.make_polygon only for small parametric profiles (can r-z revolve profile, faston blade, K riser trapezoid); clip strap/hook are slot chains of a measured polyline extruded once, not a stack of scan slices. Plan expected cone faces; census has none (cans built as revolved polygons with vertical walls) - reported, not gated. |
| CHK-ENUM | finding | Every intake feature family E01-E15 exists in the CAD (overlays Z -0.8/0.1/1.9/4.2/10/12/18.4/21.6/24.5, x 9.0/46.6/48.2/90.7, y -0.6/-8.5/-23/-32.8/-37.6/-50.5); E16/E17 declared not modelled. No hallucinated body: all CAD->scan clusters sit on declared unscanned/invented surfaces (board bottom, heatsink fin/spine sides and roots, lower can walls between caps, connector cavities, X2/C box sides, raised-part undersides). All five routed it1 scan->CAD findings are fixed (see CHK-LIKE4LIKE). Open finding: the scanned surface inside the heatsink spine at z~21.6 (x 48.1-48.4, y -26.4..-16.3) is still not modelled (builder declares it a reconstruction artefact, MODELING_PLAN §9); not decidable from the scan or photos. Minor residuals below the 20-point cluster floor in the datum frame: 17 pts at the north hub channel (48.0,-6.7,z 0.9-5.6) max 0.944 and 9 pts at the south hub channel (47.9,-34.6,z 1.1-3.1) max 0.895 (unmodelled channel content, e.g. a screw), 3 pts of Y-cap lead (85.4,-44.0) max 0.826, 3 pts of fringe below the +X board edge (96.0,-8.5,-1.5) max 1.027. |
| CHK-ACHIEVABLE | n/a | no Tier-1 dims (scan-only run), nothing to attribute |
| PHOTO-PLAUSIBILITY | finding | Photos 1-4 walked. Photo 1 matches the scanned configuration (star heatsink with TO-220 held by the gold spring strap, 3 large cans + small cans, drum/can part top-left, grey X2 box, blue Y-cap, 6 faston tabs, 5 white connectors, SOIC, edge pads): every photographed feature family exists in the CAD. Photos 2-4 are installed/catalogue photos of a variant (no spring clip, different heatsink), so they cannot confirm heatsink/clip/spine detail. No photo shows the solder side, the spine z~21.6 region or the hub channel interiors. |

## Misses, per region

- scan_to_cad:masked: p95 0.763 max 1.365 vs 0.3/0.8
- cad_to_scan_observable: p95 1.599 max 4.408 vs 0.3/0.8
- **whole part scan->CAD (gated, post-ICP): p95 0.763 / max 1.365 vs 0.30 / 0.80**: p95: almost entirely the QA ICP +0.72 mm z lift (L3), which shifts every board-level point and box top by ~0.7 mm (zone Z1 board band p95 0.772 post-ICP vs 0.243 datum frame). In the builder datum frame the same statistic is p95 0.292 / max 1.027 (0.05% of points > 0.8), and with the diagnostic ICP p95 0.287 / max 1.068. Residual max in the datum frame: 3-point fringe below the +X board edge at (96.0,-8.5,-1.5) 1.027 (scan fringe of the unscanned bottom edge, artefact); spine z~21.6 surface 0.963 (L7, unresolved); unmodelled content in both heatsink hub screw channels 0.944 / 0.895 (17 + 9 points); Y-cap lead 0.826 (3 points). All five it1 geometry findings are fixed. Options: (a) owner ACCEPT-BAND (BAND_NOT_MET) quoting the gated numbers; (b) record an owner/skill decision on the ICP correspondence radius for thin plates with one invented face and re-run QA with both protocols (would bring p95 inside band; the max would still be ~1.03-1.07); (c) optional minor geometry: hub-channel content, spine z~21.6 once decided by a photo - neither clears the CAD->scan miss below.
- **whole part CAD->scan observable (gated): p95 1.599 / max 4.408 vs 0.30 / 0.80 (datum frame 1.832 / 4.419)**: CAD surface with no scan behind it that the CAD-only ray test still counts as observable: the invented board bottom (26.8% of the observable subset, p95 1.788 / max 4.103), the heatsink block with its deep fin/spine side faces and roots (21.4%, p95 2.506 / max 4.408), and in the rest of the part (51.8%, p95 0.901 / max 2.949 post-ICP; 0.539 / 3.216 datum frame) lower can walls between the caps, connector cavities, box sides and raised-part undersides (qa/diag_observable_breakdown.json, diagnostic). With all three named CAD masks the number is still p95 0.892 / max 4.503 (M1 24.1%, M2 31.6%, M3 9.2%); leave-one-out and the open-boundary radius sweep all stay over band. Not fixable by geometry without scan data of those faces. Options: (a) solder-side scan plus oblique scans of the heatsink fins, the inter-cap area and the connector cavities, then rebuild those faces from data and re-run verify; (b) owner ACCEPT-BAND (BAND_NOT_MET) for a component-side envelope use, quoting the unmasked numbers.
- **named zones (reported; the regime has no interface band)**: I1 board top face post-ICP captures only 1,912 scan points because the +0.72 mm bias moves the scanned top out of the zone window (datum frame n 57,138, p95 0.170 / max 0.847); I1 outline edges scan->CAD p95 0.278 / max 0.448; I2 H1/H2 bores p95 0.162 / max 0.423; I3 faston row p95 0.319 / max 0.796; I4 heatsink/tall parts p95 0.644 / max 1.142 (ICP bias + spine surface). CAD->scan in I1/I4 is dominated by invented faces. Options: as above (L3 decision; L7 photo).

## Declared limitations (each with its re-run trigger)

1. No Tier-1: scan-only run, no caliper reading exists (dims.json: 12 requested dims all ABSENT, not passed); the regime has no Tier-1 band. Absolute scale is not caliper-verified (CHK-SCALE flag at intake, units assumed mm). — **Re-run trigger:** caliper readings for ENV-X, ENV-Y, F01 (H1 dia), F02 (H1-H2 pitch) and F03 (board thickness) entered in input/MEASUREMENTS.md -> re-run intake CHK-SCALE and verify
2. Unscanned surfaces are invented (MODELING_PLAN §6/§9): the whole solder side (board bottom; M1 = 24.1% of CAD samples; 26.8% of the observable CAD->scan subset), deep heatsink fin/spine sides and roots (21.4% of the observable subset), connector cavity floors, lower can walls between the caps, undersides of raised parts, Y-cap back. The ray test grades them 'observable', and they drive the gated CAD->scan miss (qa/diag_observable_breakdown.json, diagnostic). — **Re-run trigger:** a scan of the solder side plus oblique scans of the heatsink fins and connector cavities -> re-run verify on the merged full-res scan
3. QA ICP bias (datum finding raised by verdict.py): with the it1/golden parameters (sign-free 70 deg normal test, 3.0 mm correspondence radius) the invented board bottom corresponds to the scanned board top 1.6 mm away, so the ICP lifts the CAD +0.72 mm in z (0.147 deg / 0.725 mm). The official post-ICP scan->CAD p95 (0.763) differs from the datum-frame p95 (0.292) by more than the band. The datum audit (0.074 deg / 0.080 mm, within the RE_SPEC reference) and the DIAGNOSTIC ICP with max-corr 1.0 mm (0.064 deg / 0.094 mm; scan->CAD p95 0.287 / max 1.068) show the datum is sound; the gap is a registration artefact of an unscanned face. The diagnostic run is not the gate. — **Re-run trigger:** a solder-side scan (real data for the bottom face) or a recorded owner/skill decision in DECISIONS.md on the ICP correspondence radius / signed normal test for thin plates with one unscanned face -> re-run tier2_icp and deviation_gate, reporting both protocols
4. Board warp (datum-frame board top about -0.35..+0.1 mm) is not modelled: flat design-intent board (INTAKE_CARD §8). In the datum frame zone I1 board top reads scan->CAD p95 0.170 / max 0.847. — **Re-run trigger:** owner asks for the as-scanned warped board, or an enclosure fit check needs the warp
5. ICP did not converge at the default cap 60 (qa/registration_run1_cap60.json); the cap was raised once to 200 (same reason and raise as it1) and converged at 65 with the same correction. Both runs kept. — **Re-run trigger:** any rebuild -> re-run ICP with the same cap and report both runs again
6. Photos are catalogue/installed photos; photos 2-4 show a variant heatsink without the spring clip, so heatsink, clip and spine details are confirmed by photo 1 only. — **Re-run trigger:** photos of the scanned unit (top, both heatsink sides, spine top) supplied -> re-run PHOTO-PLAUSIBILITY / CHK-ENUM
7. Scanned surface inside the heatsink spine at z~21.6 (x 47.0-48.4, y -26.6..-16.3) is not modelled; datum-frame max 0.963 (38% of its 131 gate-cluster points > 0.8). Real slot vs reconstruction artefact is undecided. — **Re-run trigger:** a side photo / oblique scan of the spine above the TO-220 tab, or an owner statement -> model it (slot) or mask it as a named artefact with evidence, then re-run verify

## Claim boundary

Component-side envelope / fit reference only, iteration 2, band NOT met. Not fit for manufacture, tooling, PCB footprint or electrical work, or any solder-side / board-thickness-critical fit: the solder side, heatsink fin roots and sides, connector cavity floors and part undersides are invented; absolute scale is not caliper-verified; the board is modelled flat; the spine z~21.6 surface is undecided. Delivery needs a recorded owner ACCEPT-BAND citing this gate.

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: BAND_NOT_MET, HALT, REVISE._
