# VERDICT: BAND_NOT_MET

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: fresh verifier agent (not the builder); stl-re-verify scripts only; own datum spec, zones, masks and ICP; build/model.py only grepped for loft/ruled (CHK-PATCHWORK); BUILDER_REPORT.md and builder self-check numbers were not read before this gate was written. Re-graded OFFICIAL (full-res) after the owner confirmed on 2026-09-25 11:41 that the scan is full resolution (DECISIONS.md OTHER); the earlier INSPECTION ONLY runs are kept as deviation_run1.json, deviation_run2.json and registration_run1_inspection.json (same numbers)

Scan: `input/scan.stl` (full-res), label **OFFICIAL (full-res)**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-H22_3-way-valve_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 6395.594 mm³ | PASS |
| Validity `OD-H22_3-way-valve.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 6395.594 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 0.216° / origin 0.046 mm / points p95 0.105 max 0.118 mm | within (not blocking) |
| Registration (ICP) | converged | 33/60 its, 0.384° / 0.014 mm | PASS |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 245229 · rms 0.120 · p50 0.067 · p95 0.235 · p99 0.390 · max 1.427 | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 19911 · rms 0.603 · p50 0.078 · p95 1.484 · p99 2.926 · max 4.858 | FAIL |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 249510 · rms 0.133 · p50 0.068 · p95 0.248 · p99 0.445 · max 1.427
- scan→CAD masked: n 245229 · rms 0.120 · p50 0.067 · p95 0.235 · p99 0.390 · max 1.427
- CAD→scan unmasked: n 300000 · rms 0.621 · p50 0.077 · p95 1.548 · p99 3.023 · max 5.166
- CAD→scan masked: n 249902 · rms 0.478 · p50 0.068 · p95 0.394 · p99 2.625 · max 5.166
- CAD→scan observable only: n 19911 · rms 0.603 · p50 0.078 · p95 1.484 · p99 2.926 · max 4.858; unobservable fraction 0.44 %

Masks:

- **M1 damaged +X ear tip** (scan_to_cad): the +X ear tip of this specimen is damaged/torn (jagged outline); the CAD follows the undamaged -X ear by symmetry, so deviation here is specimen damage, not a surface deviation of the modelled design; fraction 1.72 %; inside n 4281 · rms 0.440 · p50 0.234 · p95 0.965 · p99 1.196 · max 1.276
- **M1 damaged +X ear tip** (cad_to_scan): the +X ear tip of this specimen is damaged/torn (jagged outline); the CAD follows the undamaged -X ear by symmetry, so deviation here is specimen damage, not a surface deviation of the modelled design; fraction 0.49 %; inside n 1470 · rms 0.207 · p50 0.139 · p95 0.422 · p99 0.482 · max 0.528
- **M2 open boundary** (cad_to_scan): distance from a CAD point to a scan hole EDGE (unscanned bore interiors, 28 open loops) is not a surface deviation; fraction 16.25 %; inside n 48757 · rms 1.096 · p50 0.291 · p95 2.564 · p99 3.891 · max 5.030

Zones:

- Z1 flange back face and ear holes [functional_interface] scan_to_cad: unmasked n 15913 · rms 0.113 · p50 0.070 · p95 0.173 · p99 0.345 · max 1.427 | masked n 15913 · rms 0.113 · p50 0.070 · p95 0.173 · p99 0.345 · max 1.427
- Z1 flange back face and ear holes [functional_interface] cad_to_scan: unmasked n 21498 · rms 0.120 · p50 0.071 · p95 0.195 · p99 0.517 · max 0.946 | masked n 18947 · rms 0.086 · p50 0.068 · p95 0.144 · p99 0.235 · max 0.518
- Z2 drive tube and collar [functional_interface] scan_to_cad: unmasked n 48452 · rms 0.110 · p50 0.071 · p95 0.223 · p99 0.291 · max 0.464 | masked n 48452 · rms 0.110 · p50 0.071 · p95 0.223 · p99 0.291 · max 0.464
- Z2 drive tube and collar [functional_interface] cad_to_scan: unmasked n 54533 · rms 0.869 · p50 0.086 · p95 2.533 · p99 3.706 · max 4.858 | masked n 44614 · rms 0.444 · p50 0.072 · p95 0.271 · p99 2.839 · max 4.194
- Z3 ports clip blocks and bores [functional_interface] scan_to_cad: unmasked n 63062 · rms 0.135 · p50 0.071 · p95 0.299 · p99 0.444 · max 0.675 | masked n 63062 · rms 0.135 · p50 0.071 · p95 0.299 · p99 0.444 · max 0.675
- Z3 ports clip blocks and bores [functional_interface] cad_to_scan: unmasked n 92174 · rms 0.880 · p50 0.114 · p95 2.063 · p99 3.521 · max 5.166 | masked n 64907 · rms 0.848 · p50 0.087 · p95 2.079 · p99 3.550 · max 5.166
- Z4 stem junction gussets tray rim [region] scan_to_cad: unmasked n 122083 · rms 0.141 · p50 0.064 · p95 0.247 · p99 0.565 · max 1.419 | masked n 117802 · rms 0.117 · p50 0.062 · p95 0.219 · p99 0.368 · max 1.419
- Z4 stem junction gussets tray rim [region] cad_to_scan: unmasked n 131795 · rms 0.150 · p50 0.062 · p95 0.262 · p99 0.620 · max 1.714 | masked n 121434 · rms 0.112 · p50 0.060 · p95 0.219 · p99 0.354 · max 1.714
- I1 drive tube bore lower (occluded) [interior] scan_to_cad: unmasked n 3715 · rms 0.126 · p50 0.093 · p95 0.234 · p99 0.333 · max 0.391 | masked n 3715 · rms 0.126 · p50 0.093 · p95 0.234 · p99 0.333 · max 0.391
- I1 drive tube bore lower (occluded) [interior] cad_to_scan: unmasked n 12095 · rms 1.833 · p50 1.021 · p95 3.655 · p99 4.262 · max 4.858 | masked n 2810 · rms 1.708 · p50 0.142 · p95 3.230 · p99 3.846 · max 4.194
- B1 z above 5.7 (tube) [region] scan_to_cad: unmasked n 34384 · rms 0.135 · p50 0.082 · p95 0.249 · p99 0.417 · max 0.778 | masked n 34378 · rms 0.135 · p50 0.082 · p95 0.249 · p99 0.412 · max 0.778
- B1 z above 5.7 (tube) [region] cad_to_scan: unmasked n 29990 · rms 0.129 · p50 0.073 · p95 0.254 · p99 0.396 · max 0.692 | masked n 28930 · rms 0.127 · p50 0.073 · p95 0.251 · p99 0.387 · max 0.692
- B2 z 0..5.7 (plate, tray, collar) [region] scan_to_cad: unmasked n 97682 · rms 0.149 · p50 0.073 · p95 0.255 · p99 0.605 · max 1.427 | masked n 93407 · rms 0.120 · p50 0.070 · p95 0.219 · p99 0.358 · max 1.427
- B2 z 0..5.7 (plate, tray, collar) [region] cad_to_scan: unmasked n 115785 · rms 0.604 · p50 0.078 · p95 1.148 · p99 3.170 · max 4.858 | masked n 98940 · rms 0.308 · p50 0.070 · p95 0.234 · p99 0.670 · max 4.194
- B3 z -12..0 (stem, gussets) [region] scan_to_cad: unmasked n 27071 · rms 0.088 · p50 0.058 · p95 0.177 · p99 0.250 · max 0.497 | masked n 27071 · rms 0.088 · p50 0.058 · p95 0.177 · p99 0.250 · max 0.497
- B3 z -12..0 (stem, gussets) [region] cad_to_scan: unmasked n 27991 · rms 0.221 · p50 0.061 · p95 0.469 · p99 1.077 · max 1.714 | masked n 23993 · rms 0.106 · p50 0.057 · p95 0.173 · p99 0.228 · max 1.714
- B4 z below -12 (junction, ports) [region] scan_to_cad: unmasked n 90373 · rms 0.123 · p50 0.062 · p95 0.266 · p99 0.420 · max 0.675 | masked n 90373 · rms 0.123 · p50 0.062 · p95 0.266 · p99 0.420 · max 0.675
- B4 z below -12 (junction, ports) [region] cad_to_scan: unmasked n 126234 · rms 0.754 · p50 0.087 · p95 2.000 · p99 3.242 · max 5.166 | masked n 98039 · rms 0.693 · p50 0.068 · p95 2.001 · p99 3.211 · max 5.166

Over-band scan→CAD points (> 0.8 mm): 564 (0.226 %) in 3 clusters ≥ 20 pts.

- cluster 0: n 278, centroid [21.196, -3.049, 3.985], r [21.047, 21.668], θ [350.7, 354.2], max 1.276 — +X ear tip, scan beyond the CAD (x 20.8-21.5, y -3.4..-2.2, z 2.3-5.2; 278 pts, max 1.28). This is the region intake pre-declared as damaged (inside mask M1). photo_4 suggests it may be a real pip; see CHK-ENUM. It does not drive the max (the masked max is the same)
- cluster 1: n 156, centroid [20.811, 3.487, 4.209], r [20.866, 21.219], θ [8.7, 10.2], max 1.046 — +X ear tip, other side (x 20.5-20.9, y 3.2-3.7, z 2.9-5.4; 156 pts, max 1.05). Same cause as cluster 0 (inside M1)
- cluster 2: n 130, centroid [16.212, -0.218, 0.274], r [15.948, 16.545], θ [0.1, 360.0], max 1.427 — scan material inside the +X ear screw hole at the back face (x 15.9-16.5, y -0.8..0.6, z 0.05-0.56; 130 pts, max 1.43). Photos show both ear holes open through; the -X hole has no such material. Probably scanner bridging/fuzz over the small hole mouth (flash cannot be ruled out). Not pre-declared, so not masked. This cluster sets the whole-part scan->CAD max

## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | pass | no pass depends on a mask |
| CHK-CLUSTER | pass | 3 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | pass | QA ICP registers the builder CAD onto the raw scan through intake/alignment.json. T_refine is QA-only and was not written back. No expected value was taken from builder params. The datum was not ICP'd to its own CAD. The builder's own self-check was not consulted for grading |
| CHK-LIKE4LIKE | n/a | iteration 1; no _itN_SUPERSEDED to compare |
| CHK-INDEP | pass | fresh agent context, separate from the builder |
| CHK-FILLET | pass | build/export_check.json fillets: 5/5 OK, target == used (4.617, 1.868, 6.064, 0.5, 0.5) |
| CHK-PATCHWORK | pass | census: 162 faces (plane 93, cylinder 60, torus 8, cone 1), 100% analytic area, no B-spline. MODELING_PLAN.md:57 and model.py have no loft/ruled/polyline stack |
| CHK-ENUM | finding | Intake features E01-E14 appear in both CAD and scan (overlays). Findings: (a) photo_4 shows a round pip/lump at the right ear tip. The scan also has a lump beyond the CAD at the +X ear tip (clusters 0,1). Intake declared this as damage and masked it (M1), but it may be a real feature. (b) photo_4 shows internal structure inside a port mouth. That area is unscanned, and the CAD models a plain bore (assumed) |
| CHK-ACHIEVABLE | n/a | no Tier-1 (no calipers) |
| PHOTO-PLAUSIBILITY | finding | photos 1-4 checked: plate, ears and through holes, tray rim, crenellated drive tube (4 slots), stem, gussets, Y ports, clip blocks with 2 slots, and lips are all in the CAD. Nothing in the CAD is absent from both photos and scan. Open points: the ear-tip pip and the port-internal structure, as in CHK-ENUM |

## Misses, per region

- scan_to_cad:masked: p95 0.235 max 1.427 vs 0.3/0.8
- cad_to_scan_observable: p95 1.484 max 4.858 vs 0.3/0.8
- **VERDICT BASIS (why BAND_NOT_MET): whole part**: This is an OFFICIAL full-res grade: the owner confirmed on 2026-09-25 11:41 that the scan is full resolution. ICP converged and the solid is valid. Two gated bands miss: scan->CAD masked max, and observable CAD->scan p95 and max. Both misses come from one scan artefact and from interiors the scanner did not reach, not from geometry a rebuild could correct. REVISE would therefore spend a loop without new data, and nothing here needs a HALT. Options: Deliver as-is: needs a DECISIONS.md ACCEPT-BAND entry from the owner that cites this gate.json by sha256 prefix or created time, names a missed band (scan_to_cad and/or cad_to_scan_observable), and points to an evidence file outside qa/ build/ measure/ intake/ deliver/ (e.g. decisions/accept_band.md). Or supply data (rescan of the bores, calipers, specimen inspection of the +X ear hole) and then run a measure-route loop 2.
- **+X ear screw hole, back-face mouth (scan->CAD cluster 2)**: scan->CAD max 1.427 > 0.80: 130 scan points lie inside a through hole that photos show as open. Probable scan bridging artefact, not a CAD omission. The rest of scan->CAD is within the band (masked p95 0.235). Options: (a) owner accepts it as an artefact via an ACCEPT-BAND entry citing this gate; (b) inspect the specimen for flash in the +X hole; (c) declare an artefact mask in DECISIONS before a re-grade. That would be a declared mask-dependent result, never silent
- **drive-tube bore lower + floor (CAD->scan cluster 1, 6,564 pts, max 4.86)**: the scan is open below z~1.5-1.9 inside the bore, so the CAD bore floor/web has no scan behind it (INTAKE_CARD §3). Geometry cannot be checked there, and a rebuild cannot fix it without data. Options: rescan the bore, caliper the tube depth, or accept it as a coverage limitation
- **port bores and clip-slot interiors (CAD->scan clusters 0, 2, 4, 5; ~15,700 pts, max 5.17)**: port bores beyond t~13-16 and slot interiors were not scanned (INTAKE_CARD §3). CAD bore walls there are assumed, and photo_4 hints at internal structure. Options: rescan or section a port; caliper the bore diameter/depth; or accept as unobservable
- **stem/gusset root and tray rim -Y (CAD->scan clusters 3, 6, 7; ~800 pts, max 1.71)**: small scan holes at the gusset roots (INTAKE_CARD §3 'small holes at gusset root') and a local gap on the inner tray rim. The CAD surface has no scan behind it there. Options: rescan these areas, or accept as a coverage limitation

## Declared limitations (each with its re-run trigger)

1. No Tier-1: no calipers were supplied (DECISIONS.md MEASUREMENTS), so absolute scale is not caliper-verified. — **Re-run trigger:** any caliper reading (e.g. drive tube OD, ear hole pitch)
2. Unscanned interiors are assumed geometry: the drive-tube bore floor/lower bore, port bores beyond t~13-16, clip-slot interiors, the stem/gusset root coverage hole, and the internal flow passages. The ray test counts the open-mouthed bores as observable (unobservable only 0.44%), so these drive the CAD->scan observable miss. — **Re-run trigger:** rescan covering the bores, or a sectioned/caliper measurement of bore depths and the tube floor
3. Mask M1 (+X ear tip, pre-declared at intake as damage) rests on an unconfirmed premise: photo_4 shows a pip at an ear tip. Unmasked and masked scan->CAD max are identical (1.427), so M1 does not change any result. — **Re-run trigger:** operator confirms whether the +X ear-tip lump is damage or a moulded feature

## Claim boundary

Official full-res grade. Scan->CAD p95 is within the band, so the outer skin the scanner saw matches. Bore interiors, the tube floor, the flow passages and absolute scale are unverified (no calipers). Not fit for tooling or for hose, clip or drive-spline fit decisions until the bores are measured.

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: BAND_NOT_MET, HALT, REVISE._
