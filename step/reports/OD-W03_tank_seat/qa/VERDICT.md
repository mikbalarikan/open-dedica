# VERDICT: BAND_NOT_MET

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: fresh agent/context that did not build the model; QA scripts from stl-re-verify only (plus two declared workarounds in qa/scripts/ that import those scripts' own functions); builder numbers, build_log.txt, measure/params.json and model.py (beyond the CHK-PATCHWORK grep) not used

Scan: `input/scan.stl` (full-res), label **OFFICIAL (full-res)**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-W03_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 6260.772 mm³ | PASS |
| Validity `OD-W03.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 6260.772 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 0.020° / origin 0.003 mm / points p95 0.010 max 0.013 mm | within (not blocking) |
| Tier-1 ENV-X length over the two ear lug ends | ungated | CAD 84.796 | reported |
| Tier-1 ENV-Y flange width over straight skirt sides (mid-length) | ungated | CAD 29.432 | reported |
| Tier-1 F02 barb A shank OD z=20 | ungated | CAD 5.366 | reported |
| Tier-1 F04 cup A outer OD z=1 (jaws off the webs) | ungated | CAD 23.949 | reported |
| Tier-1 F06 lug hole ID (+X) z=14 | ungated | CAD 4.214 | reported |
| Registration (ICP) | converged | 29/60 its, 0.086° / 0.027 mm | PASS |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 199176 · rms 0.145 · p50 0.081 · p95 0.307 · p99 0.462 · max 0.785 | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 19730 · rms 0.856 · p50 0.296 · p95 1.512 · p99 1.944 · max 3.063 | FAIL |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 202383 · rms 0.151 · p50 0.082 · p95 0.320 · p99 0.488 · max 1.113
- scan→CAD masked: n 199176 · rms 0.145 · p50 0.081 · p95 0.307 · p99 0.462 · max 0.785
- CAD→scan unmasked: n 300000 · rms 0.864 · p50 0.304 · p95 1.526 · p99 1.936 · max 3.085
- CAD→scan masked: n 238679 · rms 0.830 · p50 0.198 · p95 1.438 · p99 1.716 · max 3.027
- CAD→scan observable only: n 19730 · rms 0.856 · p50 0.296 · p95 1.512 · p99 1.944 · max 3.063; unobservable fraction 1.35 %

Masks:

- **M1 barb-tip bridging membrane** (scan_to_cad): scanner bridging film across the open barb bore mouth (translucent tip): scan material inside a through hole is not a surface of the part; fraction 0.33 %; inside n 662 · rms 0.265 · p50 0.138 · p95 0.641 · p99 0.886 · max 1.113
- **M2 tab-lug junction junk facets** (scan_to_cad): junk scan facets where the tab inner face meets the lug underside (occluded re-entrant corner, partly seen): scanner artefact, not part surface; fraction 1.26 %; inside n 2545 · rms 0.367 · p50 0.314 · p95 0.651 · p99 0.811 · max 0.865
- **M3 open boundary** (cad_to_scan): distance from CAD to a scan hole EDGE is not a surface deviation (25 open loops incl. the 358° skirt lower-edge loop); fraction 20.44 %; inside n 61321 · rms 0.983 · p50 0.683 · p95 1.849 · p99 2.432 · max 3.085

Zones:

- Z1 flange top + skirt outline [functional_interface] scan_to_cad: unmasked n 31742 · rms 0.149 · p50 0.059 · p95 0.364 · p99 0.518 · max 0.600 | masked n 31742 · rms 0.149 · p50 0.059 · p95 0.364 · p99 0.518 · max 0.600
- Z1 flange top + skirt outline [functional_interface] cad_to_scan: unmasked n 37419 · rms 0.351 · p50 0.056 · p95 0.783 · p99 1.630 · max 3.005 | masked n 25581 · rms 0.078 · p50 0.037 · p95 0.161 · p99 0.279 · max 1.356
- Z2 barb nipples A+B [functional_interface] scan_to_cad: unmasked n 24284 · rms 0.160 · p50 0.103 · p95 0.317 · p99 0.404 · max 1.113 | masked n 23622 · rms 0.156 · p50 0.102 · p95 0.312 · p99 0.392 · max 0.513
- Z2 barb nipples A+B [functional_interface] cad_to_scan: unmasked n 24516 · rms 0.764 · p50 0.155 · p95 1.697 · p99 1.965 · max 2.127 | masked n 18803 · rms 0.771 · p50 0.134 · p95 1.728 · p99 1.979 · max 2.127
- Z3 ear lugs + holes [functional_interface] scan_to_cad: unmasked n 9844 · rms 0.158 · p50 0.085 · p95 0.341 · p99 0.489 · max 0.677 | masked n 9844 · rms 0.158 · p50 0.085 · p95 0.341 · p99 0.489 · max 0.677
- Z3 ear lugs + holes [functional_interface] cad_to_scan: unmasked n 10353 · rms 0.682 · p50 0.182 · p95 1.533 · p99 1.912 · max 2.268 | masked n 3280 · rms 0.300 · p50 0.073 · p95 0.284 · p99 1.869 · max 2.268
- Z4 cup outer walls [functional_interface] scan_to_cad: unmasked n 56785 · rms 0.146 · p50 0.085 · p95 0.307 · p99 0.428 · max 0.626 | masked n 56785 · rms 0.146 · p50 0.085 · p95 0.307 · p99 0.428 · max 0.626
- Z4 cup outer walls [functional_interface] cad_to_scan: unmasked n 83624 · rms 0.812 · p50 0.266 · p95 1.367 · p99 1.534 · max 2.118 | masked n 80175 · rms 0.802 · p50 0.243 · p95 1.342 · p99 1.489 · max 1.790
- I1 underside + skirt inner (unscanned) [interior] scan_to_cad: unmasked n 820 · rms 0.226 · p50 0.159 · p95 0.432 · p99 0.538 · max 0.703 | masked n 820 · rms 0.226 · p50 0.159 · p95 0.432 · p99 0.538 · max 0.703
- I1 underside + skirt inner (unscanned) [interior] cad_to_scan: unmasked n 44343 · rms 1.279 · p50 1.211 · p95 1.783 · p99 2.399 · max 3.063 | masked n 27528 · rms 1.287 · p50 1.224 · p95 1.645 · p99 1.870 · max 3.027
- I2 downward-facing interior (cavity ceilings, inner shoulders) [interior] scan_to_cad: unmasked n 982 · rms 0.310 · p50 0.234 · p95 0.558 · p99 0.591 · max 0.599 | masked n 982 · rms 0.310 · p50 0.234 · p95 0.558 · p99 0.591 · max 0.599
- I2 downward-facing interior (cavity ceilings, inner shoulders) [interior] cad_to_scan: unmasked n 20884 · rms 1.212 · p50 1.219 · p95 1.386 · p99 1.666 · max 1.974 | masked n 20242 · rms 1.224 · p50 1.223 · p95 1.388 · p99 1.665 · max 1.974
- I3 barb bores [interior] scan_to_cad: unmasked n 662 · rms 0.265 · p50 0.138 · p95 0.641 · p99 0.886 · max 1.113 | masked n 0
- I3 barb bores [interior] cad_to_scan: unmasked n 6354 · rms 1.410 · p50 1.388 · p95 1.934 · p99 2.047 · max 2.127 | masked n 4467 · rms 1.480 · p50 1.430 · p95 1.966 · p99 2.059 · max 2.127
- I4 boss hole [interior] scan_to_cad: unmasked n 224 · rms 0.182 · p50 0.083 · p95 0.438 · p99 0.573 · max 0.597 | masked n 224 · rms 0.182 · p50 0.083 · p95 0.438 · p99 0.573 · max 0.597
- I4 boss hole [interior] cad_to_scan: unmasked n 169 · rms 0.200 · p50 0.121 · p95 0.418 · p99 0.640 · max 0.711 | masked n 0
- B1 z -3.3..0.3 skirt+plate [region] scan_to_cad: unmasked n 40450 · rms 0.148 · p50 0.063 · p95 0.347 · p99 0.516 · max 0.703 | masked n 40450 · rms 0.148 · p50 0.063 · p95 0.347 · p99 0.516 · max 0.703
- B1 z -3.3..0.3 skirt+plate [region] cad_to_scan: unmasked n 88314 · rms 0.959 · p50 0.862 · p95 1.639 · p99 2.178 · max 3.063 | masked n 58674 · rms 0.914 · p50 0.893 · p95 1.538 · p99 1.754 · max 3.027
- B2 z 0.3..7 lower walls [region] scan_to_cad: unmasked n 51012 · rms 0.138 · p50 0.077 · p95 0.286 · p99 0.482 · max 0.785 | masked n 51012 · rms 0.138 · p50 0.077 · p95 0.286 · p99 0.482 · max 0.785
- B2 z 0.3..7 lower walls [region] cad_to_scan: unmasked n 77585 · rms 0.872 · p50 0.306 · p95 1.463 · p99 1.961 · max 3.085 | masked n 66126 · rms 0.827 · p50 0.208 · p95 1.365 · p99 1.596 · max 2.402
- B3 z 7..12.6 upper walls+tops [region] scan_to_cad: unmasked n 61895 · rms 0.150 · p50 0.087 · p95 0.314 · p99 0.438 · max 0.709 | masked n 61551 · rms 0.149 · p50 0.087 · p95 0.313 · p99 0.438 · max 0.709
- B3 z 7..12.6 upper walls+tops [region] cad_to_scan: unmasked n 86564 · rms 0.840 · p50 0.308 · p95 1.443 · p99 1.721 · max 2.268 | masked n 76548 · rms 0.821 · p50 0.246 · p95 1.391 · p99 1.622 · max 2.268
- B4 z 12.6..18 shoulders+lugs [region] scan_to_cad: unmasked n 32741 · rms 0.174 · p50 0.101 · p95 0.367 · p99 0.540 · max 0.865 | masked n 30540 · rms 0.147 · p50 0.096 · p95 0.300 · p99 0.415 · max 0.677
- B4 z 12.6..18 shoulders+lugs [region] cad_to_scan: unmasked n 30333 · rms 0.660 · p50 0.142 · p95 1.402 · p99 1.741 · max 1.974 | masked n 25344 · rms 0.693 · p50 0.136 · p95 1.433 · p99 1.753 · max 1.974
- B5 z 18..29 barbs [region] scan_to_cad: unmasked n 16285 · rms 0.147 · p50 0.087 · p95 0.295 · p99 0.391 · max 1.113 | masked n 15623 · rms 0.139 · p50 0.085 · p95 0.288 · p99 0.370 · max 0.513
- B5 z 18..29 barbs [region] cad_to_scan: unmasked n 17204 · rms 0.738 · p50 0.134 · p95 1.670 · p99 1.993 · max 2.127 | masked n 11987 · rms 0.746 · p50 0.105 · p95 1.738 · p99 2.016 · max 2.127

Over-band scan→CAD points (> 0.8 mm): 48 (0.024 %) in 0 clusters ≥ 20 pts.


## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | pass | no pass depends on a mask |
| CHK-CLUSTER | pass | 0 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | pass | datum re-derived from the raw scan by QA (qa/datum_audit.json); QA ICP T_refine is QA-only and never written back to intake/alignment.json; no expected value taken from params.json or this scan. The builder's own self-checks in MODELING_PLAN §8 (scan->CAD p95 0.308/0.299 on 200k samples) are a consistency check, not independent evidence, and QA's full-vertex number differs (see gate). |
| CHK-LIKE4LIKE | n/a | iteration 1: no _itN_SUPERSEDED folder, no previous QA gate to compare. Within this QA, the default (sign-free) ICP run is kept as deviation_run1.json and labelled; it is not presented as an improvement. |
| CHK-INDEP | pass | fresh context; did not build the model |
| CHK-FILLET | pass | build/export_check.json + fillets.json: 5/5 fillets OK, target == used for every one (0.653, 0.646, 0.469, 0.657, 0.378); no REDUCED/FAILED/NO_EDGES |
| CHK-PATCHWORK | pass | QA census (qa/step_check.json): 106 faces, analytic area 98.6 %; 46 plane (no facet swarm), 35 cone, 17 cylinder, 8 B-spline (1.4 % area; declared in MODELING_PLAN §0 as OCC cone/cone round blends); grep of build/model.py for loft(/ruled/Polyline: no match |
| CHK-ENUM | pass | INTAKE E01-E10 all present in CAD and visible in overlays (flange, skirt, 2 cups with step, shoulders, barbs with flare/lip/tip, bores, boss + hole, 4 webs, 2 tapered tabs, 2 lugs + holes); E11 parting ridge not modelled (cosmetic, declared); E12 interior invented (owner decision, declared). No scan->CAD over-band cluster >= 20 pts, i.e. no missing feature; every CAD->scan cluster explained below (invented interior or coverage gap). |
| CHK-ACHIEVABLE | n/a | no Tier-1 reading exists (0 of 12 calipered), so no Tier-1 miss to attribute |
| PHOTO-PLAUSIBILITY | pass | OD-W03_photo1 (catalogue photo, no scale): stadium flange with skirt, two cups each with a single-barb nipple, small middle boss, webs, L-shaped ears with holes at both ends: all in CAD; nothing in CAD's outer skin is absent from photo+scan. Photo cannot confirm interior/underside (not visible). |

## Misses, per region

- scan_to_cad:masked: p95 0.307 max 0.785 vs 0.3/0.8
- cad_to_scan_observable: p95 1.512 max 3.063 vs 0.3/0.8
- **whole part scan->CAD (p95 band 0.30)**: Masked p95 0.307 (unmasked 0.320) is a small, distributed overshoot. Attribution (qa/scripts/attribution.json, not a mask): (1) skirt lower band z < -1.5, where the scan lies INSIDE the CAD by a median -0.24..-0.36 mm growing with depth (2,315 pts > 0.30; p95 without it 0.288) — either an unmodelled draft/edge break on the skirt's lower outer edge or scan curl at the ragged open boundary (scan stops at z -2.0..-3.17), undecidable from the scan; (2) cup B upper wall z 9.5-11.8, scan OUTSIDE the CAD by median +0.11 / p95 +0.40 (p95 without it 0.296) — CAD cup B upper radius short near the top: a measurable geometry error; (3) tab/lug junction and tab side faces (p95 0.44-0.57 at x 32-35, z 11-15.5); (4) the translucent cup-wall ripple ±0.15 mm raises the floor everywhere (INTAKE §2). Options: (a) REVISE route=geometry/measure: re-measure cup B upper-wall radius/draft near the top; add a skirt lower-edge draft or break ONLY if an underside photo or an ENV-Y caliper at seat vs top confirms it; (b) one caliper pass (ENV-Y at the skirt bottom and top, F04) arbitrates skirt-curl vs real taper; (c) human ACCEPT-BAND of 0.307 vs 0.30.
- **whole part scan->CAD max (band 0.80), unmasked only**: Unmasked max 1.113 mm = bridging film across barb A's bore mouth (M1); next 0.865 = junk facets at the tab/lug junction (M2). Masked max 0.785 passes, so the max is a masked pass (declared as a limitation). Not a geometry error. Options: rescan the barb tips and ear junction (matt spray on the translucent part) and re-run unmasked; or accept with the masks declared.
- **CAD->scan observable (p95 1.512 / max 3.063 vs 0.30 / 0.80)**: Dominated by the invented hollow shell (owner decision: 1.2 mm walls, pocket under the plate, cavities, through bores; cluster c2s_0, 122k pts, d_p50 1.22): it was never scanned, yet the ray-cone observability heuristic counts it observable (only 1.35 % unobservable) because rays leave through the open underside. Remaining clusters are coverage gaps under the lug overhangs and inside the 1.3-1.5 mm slots. More geometry cannot fix this without data. Options: (a) scan the underside/interiors (or section the part) and rebuild the shell from data; (b) caliper W01 wall thickness + F03 bore; (c) human ACCEPT-BAND with the invented interior declared; (d) if the interior is not needed downstream, the owner may choose a different interior decision (e.g., solid) — an owner decision, not a QA fix.

## Declared limitations (each with its re-run trigger)

1. No Tier-1: 0 of 12 requested dimensions calipered (all ABSENT, not passed); absolute scale not caliper-verified (CHK-SCALE flag at intake). Every size is scan-derived. — **Re-run trigger:** any caliper reading in input/MEASUREMENTS.md (ENV-X/ENV-Y first, for scale) -> re-run verify
2. Interior, underside, wall thickness (1.2 mm), bore and boss-hole depths are assumed (owner decision), not measured; CAD->scan observable numbers are dominated by these unscanned surfaces. — **Re-run trigger:** an underside/interior scan or a W01 wall-thickness caliper reading -> rebuild + re-run
3. Gate registration = QA workaround qa/scripts/tier2_icp_signed.py (signed normal agreement; everything else tier2_icp.py defaults): 29 its, 0.086 deg / 0.027 mm, consistent with the datum audit. The shipped tier2_icp.py (sign-free normal test) converged to 0.180 deg / 0.659 mm (+z), pulled by invented interior faces 1.2 mm behind the skin; graded in that frame scan->CAD p95 is 0.588 (qa/deviation_run1.json, shown in gate.json deviation_runs). Both runs reported. — **Re-run trigger:** tier2_icp.py fixed (signed normal test or CAD-side mask) -> re-run registration + deviation gate
4. Scan->CAD max passes only masked: masks M1 (barb-tip bridging film, 0.33 %) and M2 (tab/lug junk facets, 1.26 %) were declared from INTAKE §2 before any number; unmasked max 1.113 mm (> 0.80). The whole-part p95 fails masked and unmasked. — **Re-run trigger:** rescan of barb tips and ear junction without bridging/junk -> re-run unmasked
5. Datum audit ran through qa/scripts/datum_audit_pair.py (datum_audit.py has no two-cup midpoint origin / feature_line clock); it reuses datum_audit.py's own fit functions. — **Re-run trigger:** datum_audit.py supports circle_pair + feature_line clock -> re-run the audit
6. Overlays are drawn in the builder's datum frame (overlay.py has no --registration); the gate's ICP correction is 0.027 mm, below what the panels resolve. — **Re-run trigger:** a registration correction > 0.1 mm -> regenerate overlays in the ICP frame
7. Functional-interface zones Z1-Z4 are reported, not gated (baseline-skill has no interface band); Z2/Z4 CAD->scan zone numbers include invented bore/cavity walls inside the zone boxes. — **Re-run trigger:** a regime with interface_max declared at intake -> re-run

## Claim boundary

This result is NOT a dimensional certification: no dimension is caliper-verified and scale is unverified; the outer skin follows the full-res scan to scan->CAD p95 0.307 mm masked / 0.320 unmasked (band 0.30 missed), and the interior, underside, wall thickness and bore depths are invented. Not fit for tooling, seal/hose fit decisions or manufacture until calipered and the underside is captured; usable as a visual/envelope model of the outer skin only.

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: BAND_NOT_MET, HALT, REVISE._
