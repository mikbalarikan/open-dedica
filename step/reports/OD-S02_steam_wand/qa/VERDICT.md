# VERDICT: BAND_NOT_MET

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: fresh agent (stl-re-verify stage, iteration 3) that did not build the model; QA scripts from stl-re-verify only plus run-local report-only probes in qa/ (it2_it3_diff.py, zone_probe.py, attribution_probe.py, datum_crosscheck.py adapted from _it2_SUPERSEDED/qa/); own ICP on the it3 STEP; builder numbers, build_log.txt, measure/params.json values and scratchpad files not read; build/model.py only grepped read-only (loft ruled / polyline / sweep); the builder's 'only three features changed' claim was checked on the STEPs (qa/it2_it3_diff.json), not taken from params or the plan.

Scan: `input/scan.stl` (full-res), label **OFFICIAL (full-res)**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-S02_steam-rod_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 13753.489 mm³ | PASS |
| Validity `OD-S02_steam-rod.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 13753.489 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 0.422° / origin 0.326 mm / points p95 0.657 max 0.746 mm | outside (not blocking) |
| Registration (ICP) | converged | 44/60 its, 0.053° / 0.059 mm | PASS |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 234665 · rms 0.115 · p50 0.063 · p95 0.236 · p99 0.366 · max 0.737 | PASS |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 19656 · rms 0.347 · p50 0.067 · p95 0.766 · p99 1.698 · max 2.601 | FAIL |
| zone:Z1 rod spigot taper + O-ring seats:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 39907 · rms 0.062 · p50 0.036 · p95 0.131 · p99 0.192 · max 0.565 | PASS |
| zone:Z1 rod spigot taper + O-ring seats:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 48538 · rms 0.063 · p50 0.033 · p95 0.133 · p99 0.223 · max 0.693 | PASS |
| zone:Z2 steel tube B-bend-C:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 26716 · rms 0.129 · p50 0.099 · p95 0.229 · p99 0.298 · max 0.580 | PASS |
| zone:Z2 steel tube B-bend-C:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 23764 · rms 0.118 · p50 0.093 · p95 0.214 · p99 0.250 · max 0.345 | PASS |
| zone:Z3 lever paddle:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 20978 · rms 0.070 · p50 0.051 · p95 0.134 · p99 0.168 · max 0.247 | PASS |
| zone:Z3 lever paddle:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 23232 · rms 0.068 · p50 0.051 · p95 0.130 · p99 0.161 · max 0.235 | PASS |
| zone:Z4 bushing + tip:scan_to_cad | p95 ≤0.3 / max ≤0.8 | n 54593 · rms 0.144 · p50 0.080 · p95 0.301 · p99 0.455 · max 0.737 | FAIL |
| zone:Z4 bushing + tip:cad_to_scan | p95 ≤0.3 / max ≤0.8 | n 47622 · rms 0.464 · p50 0.087 · p95 1.063 · p99 1.837 · max 2.602 | FAIL |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 251631 · rms 0.358 · p50 0.066 · p95 0.312 · p99 2.056 · max 4.518
- scan→CAD masked: n 234665 · rms 0.115 · p50 0.063 · p95 0.236 · p99 0.366 · max 0.737
- CAD→scan unmasked: n 300000 · rms 0.365 · p50 0.070 · p95 0.896 · p99 1.692 · max 2.617
- CAD→scan masked: n 240232 · rms 0.225 · p50 0.058 · p95 0.275 · p99 1.060 · max 2.602
- CAD→scan observable only: n 19656 · rms 0.347 · p50 0.067 · p95 0.766 · p99 1.698 · max 2.601; unobservable fraction 1.72 %

Masks:

- **M1 D1 torn flash** (scan_to_cad): torn rubber flash/flap at the knob/sleeve junction is specimen damage, not design geometry, and is deliberately not modelled; points there are not a surface deviation of the modelled part; fraction 6.74 %; inside n 16966 · rms 1.310 · p50 0.275 · p95 2.984 · p99 3.961 · max 4.518
- **M1 D1 torn flash** (cad_to_scan): torn rubber flash/flap at the knob/sleeve junction is specimen damage, not design geometry, and is deliberately not modelled; points there are not a surface deviation of the modelled part; fraction 4.07 %; inside n 12223 · rms 0.529 · p50 0.160 · p95 1.306 · p99 1.761 · max 2.113
- **M2 open boundary** (cad_to_scan): CAD->scan distance measured to a scan hole EDGE (33 open-boundary loops, intake coverage.json) is not a surface deviation; fraction 16.94 %; inside n 50834 · rms 0.719 · p50 0.266 · p95 1.625 · p99 2.239 · max 2.617

Zones:

- Z1 rod spigot taper + O-ring seats [whole] scan_to_cad: unmasked n 39907 · rms 0.062 · p50 0.036 · p95 0.131 · p99 0.192 · max 0.565 | masked n 39907 · rms 0.062 · p50 0.036 · p95 0.131 · p99 0.192 · max 0.565
- Z1 rod spigot taper + O-ring seats [whole] cad_to_scan: unmasked n 57398 · rms 0.231 · p50 0.036 · p95 0.501 · p99 1.197 · max 1.689 | masked n 48538 · rms 0.063 · p50 0.033 · p95 0.133 · p99 0.223 · max 0.693
- Z2 steel tube B-bend-C [whole] scan_to_cad: unmasked n 26716 · rms 0.129 · p50 0.099 · p95 0.229 · p99 0.298 · max 0.580 | masked n 26716 · rms 0.129 · p50 0.099 · p95 0.229 · p99 0.298 · max 0.580
- Z2 steel tube B-bend-C [whole] cad_to_scan: unmasked n 26372 · rms 0.134 · p50 0.095 · p95 0.228 · p99 0.424 · max 0.802 | masked n 23764 · rms 0.118 · p50 0.093 · p95 0.214 · p99 0.250 · max 0.345
- Z3 lever paddle [whole] scan_to_cad: unmasked n 20978 · rms 0.070 · p50 0.051 · p95 0.134 · p99 0.168 · max 0.247 | masked n 20978 · rms 0.070 · p50 0.051 · p95 0.134 · p99 0.168 · max 0.247
- Z3 lever paddle [whole] cad_to_scan: unmasked n 24256 · rms 0.079 · p50 0.052 · p95 0.135 · p99 0.185 · max 0.744 | masked n 23232 · rms 0.068 · p50 0.051 · p95 0.130 · p99 0.161 · max 0.235
- Z4 bushing + tip [whole] scan_to_cad: unmasked n 54593 · rms 0.144 · p50 0.080 · p95 0.301 · p99 0.455 · max 0.737 | masked n 54593 · rms 0.144 · p50 0.080 · p95 0.301 · p99 0.455 · max 0.737
- Z4 bushing + tip [whole] cad_to_scan: unmasked n 72226 · rms 0.631 · p50 0.122 · p95 1.571 · p99 2.206 · max 2.617 | masked n 47622 · rms 0.464 · p50 0.087 · p95 1.063 · p99 1.837 · max 2.602
- R rod lower (collar, groove, bead, lug) [region] scan_to_cad: unmasked n 35685 · rms 0.124 · p50 0.083 · p95 0.236 · p99 0.375 · max 0.507 | masked n 35685 · rms 0.124 · p50 0.083 · p95 0.236 · p99 0.375 · max 0.507
- R rod lower (collar, groove, bead, lug) [region] cad_to_scan: unmasked n 46029 · rms 0.264 · p50 0.091 · p95 0.461 · p99 1.337 · max 2.082 | masked n 38130 · rms 0.112 · p50 0.078 · p95 0.211 · p99 0.336 · max 0.646
- R knob + sleeve + band junction [region] scan_to_cad: unmasked n 72677 · rms 0.641 · p50 0.070 · p95 1.644 · p99 3.135 · max 4.518 | masked n 55711 · rms 0.112 · p50 0.056 · p95 0.252 · p99 0.350 · max 0.479
- R knob + sleeve + band junction [region] cad_to_scan: unmasked n 70322 · rms 0.244 · p50 0.061 · p95 0.418 · p99 1.247 · max 2.113 | masked n 56135 · rms 0.114 · p50 0.051 · p95 0.259 · p99 0.369 · max 0.741

Over-band scan→CAD points (> 0.8 mm): 5721 (2.274 %) in 2 clusters ≥ 20 pts.

- cluster 0: n 3857, centroid [10.336, -3.767, -5.904], r [8.458, 13.944], θ [0.0, 360.0], max 4.518 — D1 torn rubber flash, -y side of the sleeve (centroid x 10.3, z -5.9): specimen damage pre-declared at intake, visible in photo_1/photo_2 and overlay x=10 / Z=-8; inside mask M1. Artefact, not a missing feature (same as it1/it2 cluster 0).
- cluster 1: n 1864, centroid [9.077, 6.139, -8.991], r [9.0, 12.823], θ [26.1, 42.1], max 3.190 — D1 torn rubber flash, +y side of the sleeve (centroid x 9.1, z -9.0): same flap, same evidence; inside mask M1 (same as it1/it2 cluster 1).

## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | finding | whole part scan_to_cad; zone Z1 rod spigot taper + O-ring seats cad_to_scan; zone Z2 steel tube B-bend-C cad_to_scan |
| CHK-CLUSTER | pass | 2 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | finding | QA grading is independent: own ICP of the it3 CAD onto the full-res scan (T_refine QA-only, never written back), datum re-derived from the raw scan, no expected value taken from builder params. Finding (carried from it1/it2): the builder's record (MODELING_PLAN §0/§8 self-check passes; it3 re-measurements in measure/figures/measure_it3.json of the same scan) is a scan-derived consistency check, not independent evidence. |
| CHK-LIKE4LIKE | pass | it2 -> it3 compared under the SAME protocol as it1/it2: qa/regime.json (cp of intake/regime.json), masks.json (M1 pre-declared D1 box x 6.5..13 z -15..-1, both directions; M2 open boundary 0.8 mm, CAD->scan, QA-added at it1), zones.json, icp_scan_masks.json and datum_spec.json are byte-identical copies of _it2_SUPERSEDED/qa/ (which were byte-identical to it1). ICP params identical (ns 3M seed 11, nc 300k seed 13, normal 70 deg, boundary 0.8, corr 3.0, cap 60, tol 1e-6); deviation sampling identical (all 251631 scan verts, c2s 300k seed 2, k 8, n_samp 3M seed 0, no vertex candidates); observability identical (20000 seed 5, far 0.5, cone 60, 6 rays, offset 0.05, unbounded); sweep radii 0,0.2,0.4,0.8,1.5,2.5 and cluster params (0.8 mm, eps 1.0, min 20) identical; the it2 overlay panel sets re-drawn identically (overlay_rod, overlay_lower, overlay_it2_extra) plus 8 new it3 panels (overlay_it3_extra). Datum audit and datum_crosscheck reproduce it2 exactly (same alignment.json). Not like-for-like by construction: ICP re-run on the new CAD (it2 49 its 0.060 deg/0.053 mm, it3 44 its 0.053 deg/0.059 mm) and seeded CAD samples fall on a different surface, so M2 and the observable subsample select different points. Probe changes: zone_probe.py chunk 20000 -> 2000 (OOM on the finer it3 tessellation; chunking does not change results); attribution_probe.py adds a scan->CAD Z4 face attribution. Improvements in Z2/Z3 come from geometry (STEP diff confines the change to the bend, the paddle and the tip neck), not from protocol. |
| CHK-INDEP | pass | fresh agent; see independence |
| CHK-FILLET | pass | build/export_check.json (it3): F03 lug corner 0.6 target = 0.6 used OK; F05 plate perimeter round 1.946 target = 1.946 used OK (it2: 1.2 assumed). Z3 now reads p95 0.134 scan->CAD (zone_probe: perimeter mean signed +0.048 vs +0.177 in it2), so the measured radius is confirmed by the gate. Lug radius still ASSUMED. |
| CHK-PATCHWORK | finding | census (QA, both frames): 122 faces (it2 109); plane 47, cone 33, cylinder 31, bspline 5, revolution 3, sphere 2, torus 1; analytic share 77.2 % by QA's count (it2 83.3 %; the bend torus was replaced by one bspline sweep face, area 331). No loft(ruled=True) (model.py:140 ruled=False, the planned fairing loft); no slice stack. New in it3: the bend is ONE sweep of a circle along a spline through 10 scanned centreline stations (model.py:249-258) - a fitted path, not a slice stack, accepted. Minor findings: (a) the bend radius bend_tube_r differs from the straight tube radius, which leaves two small annular ledges (qa/it2_it3_diff.json: two new PLANE faces of 1.61 mm2 at the bend ends) - a modelling artefact, not a scanned feature; (b) carried from it1: the rod bead/groove z 9.75..12.75 is a revolved measured (z,r) polyline. |
| CHK-ENUM | finding | all 12 intake features exist in the it3 CAD (overlays); D1 not modelled by declaration; the it3 tip neck under the bushing is new and is supported by the scan (Z4 hub cells t -10..-8, r<3.5 no longer over band; zone_probe). Finding: a coherent one-signed scan->CAD group at the tube-C entry on the bushing top (nearest CAD face 64, bushing top cone, 895 of 3477 points > 0.3 mm, 100 % scan OUTSIDE the CAD, d max 0.724; tube C end face 60 adds 122 more) shows material the CAD lacks: overlay Z=-33.5 shows the scan bulging 0.3-0.7 mm beyond the CAD around the tube entry, and photo_1 shows a raised collar on the bushing top around the tube. Not modelled -> part of the Z4 scan->CAD miss. |
| CHK-ACHIEVABLE | n/a | no Tier-1 (no calipers) |
| PHOTO-PLAUSIBILITY | pass | photo_1, photo_2 walked by this agent: tapered rod with O-rings, knob, paddle with dish, sleeve + sealing band, steel tube with one bend, white bushing (ribbed/windowed tip-side face and a raised collar where the tube enters, photo_1), steel tip with open bore - all present in CAD except the bushing-top collar (see CHK-ENUM). Torn flap at the knob/sleeve junction visible in both photos (supports M1/D1). Window floors and bore depth not visible. No scale reference. |

## Misses, per region

- cad_to_scan_observable: p95 0.766 max 2.601 vs 0.3/0.8
- zone:Z4 bushing + tip:scan_to_cad: p95 0.301 max 0.737 vs 0.3/0.8
- zone:Z4 bushing + tip:cad_to_scan: p95 1.063 max 2.602 vs 0.3/0.8
- **Z4 bushing + tip scan->CAD (p95 0.301 > 0.30 by <0.001 mm; max 0.737 in band) -- GEOMETRIC cause, fixable by a rebuild, not fixed (loop limit reached; owner accepted per DECISIONS.md), marginal**: Coherent, one-signed residual groups, all with the scan OUTSIDE the CAD (CAD too small): (1) the tube-C entry on the bushing top: nearest face 64 (bushing top cone) 895 of 3477 points > 0.3 mm, 100 % outside, d max 0.724, plus 122 points on the tube C end (face 60), t -22.3..-21.4 / r 2.2..6.6 about the tip axis; overlay Z=-33.5 shows a smooth bulge 0.3-0.7 mm beyond the CAD around the tube entry and photo_1 shows a raised collar there - a missing feature, not modelled. 75 % of these points lie within 0.8 mm of a scan-hole edge (hole loop r 35.5..37.9, z -33..-30.4), so part could be edge curl, but the sign is 100 % one-sided and the photo supports a collar. (2) The bushing barrel underside rim (face 68, t -12.8..-8.6, r 7.5..10.2): 597 points > 0.3, 78 % outside - named in it2 ('barrel/rim r 5..9.5') and not addressed in it3. Report-only what-if (qa/attribution_probe.json): either group at the zone median gives Z4 p95 0.272/0.273. The it3 tip neck fixed the hub (it2 cells t -10..-8, r<3.5: 632 points > 0.3 -> 79). Z4 scan->CAD away from scan-hole edges reads p95 0.247. The miss is frame-sensitive (datum frame 0.297, not gated). Options: Rebuild (would need a 4th, owner-authorised loop): model the bushing-top collar around the tube entry (measure it from sections Z=-32..-35 and x=40) and refit the barrel underside rim; or a supplementary scan of the bushing top to confirm the collar vs hole-edge curl; or accept the <0.001 mm p95 excess (ACCEPT-BAND). Owner chose accept (DECISIONS.md).
- **Whole-part observable CAD->scan (p95 0.766 / max 2.601) and Z4 CAD->scan (p95 1.063 masked / 1.571 unmasked, max 2.602/2.617) -- NOT fixable by geometry**: CAD surface with no scan behind it. Z4: 13892 of 13992 over-0.8 CAD samples lie on the 32 window-pocket/bore faces introduced in it2 (unchanged in it3); the other Z4 faces away from scan holes read p95 0.241 / max 0.511 (qa/attribution_probe.json). Whole part: with D1, scan-hole-adjacent (0.8 mm) and bore points removed CAD->scan reads p95 0.233 / max 2.602, the max being the window floors (unscanned; overlays x=44.4, Z=-43.5, Z=-44.4). Hole-adjacent samples: 50870, p95 1.628. The it3 changes (bend, paddle, neck) do not touch these surfaces; observable p95 moved 0.736 -> 0.766 because the ICP and the seeded CAD samples changed (same protocol, different CAD). Options: cannot be fixed by geometry: any pocket/bore depth leaves an unscanned floor/wall. Pin-gauge/depth readings of the bore and one window (then model the measured depth), a supplementary scan of the bushing underside, or accept with L3 declared (ACCEPT-BAND). A shallower model brings back the it1 scan->CAD clusters.
- **Whole-part scan->CAD UNMASKED (p95 0.312 / max 4.518; gated masked number passes) -- NOT fixable by geometry**: D1 torn flash (clusters 0 and 1: 5721 of 5721 over-band points), specimen damage, deliberately not modelled. Options: rescan a clean specimen, or accept with M1 declared (ACCEPT-BAND).

## Declared limitations (each with its re-run trigger)

1. Scan-only: no calipers, Tier-1 not run, absolute scale not caliper-verified (units assumed mm; DECISIONS MEASUREMENTS, CHK-SCALE finding at intake). — **Re-run trigger:** any caliper reading (>=3 envelope dims for a scale test) -> re-run Tier-1 and scale check
2. Masks. M1 D1 torn flash (pre-declared box, both directions) removes 6.74 % of scan->CAD points (inside p95 2.98 / max 4.52 mm) and 4.07 % of CAD->scan points; the box also hides intact sleeve/knob-fairing surface. Whole-part scan->CAD PASSES ONLY MASKED (masked p95 0.236 / max 0.737; UNMASKED p95 0.312 / max 4.518 mm, over the band). Zone Z1 CAD->scan passes only with the QA-added M2 open-boundary mask (masked p95 0.133 / max 0.693; UNMASKED p95 0.501 / max 1.689). Zone Z2 CAD->scan passes only with M2 (masked p95 0.214 / max 0.345; UNMASKED p95 0.228 / max 0.802, 0.002 over; M1 does not reach Z2, so M2 alone removes it). M2 (CAD->scan only) removes 16.94 %. — **Re-run trigger:** rescan with the torn flap trimmed or pressed back (or a replacement part), and a supplementary scan covering the 33 hole loops (rod theta 180..260, bushing top / tube entry) -> re-run unmasked
3. Unobservable/uncovered CAD: tip bore interior (13.6 mm, builder-declared scan lower bound), bushing underside window pockets (2.52 mm, scan lower bound) and their floors, hidden assembly interfaces (PART-CLASS), 33 scan holes. The OD ray-cone heuristic (subsample 20000 seed 5, far 0.5, cone 60, 6 rays, offset 0.05, unbounded) marks only 1.72 % unobservable, so these surfaces remain inside the gated 'observable' CAD->scan number. — **Re-run trigger:** a pin-gauge/depth reading of the tip bore and of one window pocket, or a supplementary scan of the bushing underside -> re-run CAD->scan
4. Datum audit (report-only) outside the RE_SPEC reference: normals-eigen axis 0.42 deg / origin 0.33 mm vs the builder (identical to it1/it2, same alignment.json); QA section-circle cross-check (qa/datum_crosscheck.json, identical to it2) agrees to 0.04 deg / 0.03 mm, tube clock -0.56 deg. ICP correction small (0.053 deg / 0.059 mm). The Z4 scan->CAD p95 is frame-sensitive at the band edge: 0.297 in the builder datum frame (qa/deviation_datum.json, not gated) vs 0.301 after QA ICP (gated). — **Re-run trigger:** any datum change at intake -> re-run the whole QA
5. Overlays are drawn in the builder's alignment frame (overlay.py has no --registration input); the ICP correction is 0.059 mm, below the line widths. — **Re-run trigger:** if the ICP correction ever exceeds 0.1 mm -> redraw overlays in the registered frame
6. Known unmodelled geometry: the raised collar on the bushing top at the tube-C entry (scan outside the CAD, 895 of 3477 nearest-face points > 0.3 mm, d max 0.724; overlay Z=-33.5, photo_1) and the barrel underside rim (597 points > 0.3 mm, 78 % scan outside). They are the cause of the Z4 scan->CAD p95 0.301 band miss, accepted by the owner rather than fixed. — **Re-run trigger:** any rebuild of the bushing (collar/rim modelled), a caliper reading of the collar, or a supplementary scan of the bushing top -> re-run the full verify

## Claim boundary

Iteration-3 CAD is BAND_NOT_MET (not approved), delivered only on the owner's recorded acceptance. It is a scan-only, uncalipered reconstruction of a damaged assembly specimen: not fit for tooling or for the fit-critical machine interface (rod spigot / O-ring seats) until calipered; the tip bore depth (13.6) and window depth (2.52) are scan lower bounds, not measured depths; the bushing-top collar at the tube entry is not modelled; hidden internal interfaces are not modelled; the one-fused-solid STEP is not a multi-body assembly. The whole-part scan->CAD pass and the Z1/Z2 CAD->scan passes are masked passes.

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: BAND_NOT_MET, HALT, REVISE._

## Iteration comparison it1 → it2 → it3 (CHK-LIKE4LIKE: same regime, masks, zones, ICP params, sampling; see checks)

STEP diff it2 → it3 (qa/it2_it3_diff.json): faces 109 → 122; 25 it2 faces replaced by 38 it3 faces, changed faces by QA zone box {'Z3': 12, 'R knob': 30, 'Z2': 8, 'Z4': 13}; removed material 4 pieces / 95.6125 mm³ in zones [['Z2'], ['Z3'], ['Z4']]; added 3 pieces / 2.0081 mm³ in zones [['Z2'], ['Z4']]. Every removed/added piece sits in Z2 (bend), Z3 (paddle; its pieces run under the knob to x 8.9, which is why 'R knob' faces are listed) or Z4 (tip neck). The 'R knob' face entries are paddle outline faces plus fused neighbours whose area moved by ≤0.73 mm² (boolean re-trim); no piece of material changed outside the three features. Also new: two 1.61 mm² annular ledges at the bend ends (bend radius ≠ straight-tube radius). This confirms the builder's claim (MODELING_PLAN §8 it3): only the bend, the paddle perimeter round and the tip neck changed; windows and bore unchanged (32 of 32 it2 window/bore faces found unchanged in it3).

| Statistic | it1 | it2 | it3 |
|---|---|---|---|
| scan→CAD unmasked | p95 0.366 / max 4.502 | p95 0.366 / max 4.512 | p95 0.312 / max 4.518 |
| scan→CAD masked (gated) | p95 0.291 / max 1.265 | p95 0.292 / max 0.734 | p95 0.236 / max 0.737 |
| CAD→scan unmasked | p95 0.664 / max 2.351 | p95 0.902 / max 2.636 | p95 0.896 / max 2.617 |
| CAD→scan masked | p95 0.301 / max 2.351 | p95 0.350 / max 2.636 | p95 0.275 / max 2.602 |
| CAD→scan observable (gated) | p95 0.575 / max 2.231 | p95 0.736 / max 2.542 | p95 0.766 / max 2.601 |
| Z1 rod spigot taper + O-ring seats scan→CAD masked (gated) | p95 0.134 / max 0.562 | p95 0.133 / max 0.572 | p95 0.131 / max 0.565 |
| Z1 rod spigot taper + O-ring seats scan→CAD unmasked | p95 0.134 / max 0.562 | p95 0.133 / max 0.572 | p95 0.131 / max 0.565 |
| Z1 rod spigot taper + O-ring seats CAD→scan masked (gated) | p95 0.137 / max 0.726 | p95 0.135 / max 0.757 | p95 0.133 / max 0.693 |
| Z1 rod spigot taper + O-ring seats CAD→scan unmasked | p95 0.506 / max 1.669 | p95 0.499 / max 1.663 | p95 0.501 / max 1.689 |
| Z2 steel tube B-bend-C scan→CAD masked (gated) | p95 0.342 / max 0.574 | p95 0.344 / max 0.576 | p95 0.229 / max 0.580 |
| Z2 steel tube B-bend-C scan→CAD unmasked | p95 0.342 / max 0.574 | p95 0.344 / max 0.576 | p95 0.229 / max 0.580 |
| Z2 steel tube B-bend-C CAD→scan masked (gated) | p95 0.334 / max 0.482 | p95 0.340 / max 0.468 | p95 0.214 / max 0.345 |
| Z2 steel tube B-bend-C CAD→scan unmasked | p95 0.354 / max 0.801 | p95 0.357 / max 0.818 | p95 0.228 / max 0.802 |
| Z3 lever paddle scan→CAD masked (gated) | p95 0.365 / max 0.527 | p95 0.375 / max 0.533 | p95 0.134 / max 0.247 |
| Z3 lever paddle scan→CAD unmasked | p95 0.365 / max 0.527 | p95 0.375 / max 0.533 | p95 0.134 / max 0.247 |
| Z3 lever paddle CAD→scan masked (gated) | p95 0.367 / max 0.496 | p95 0.381 / max 0.506 | p95 0.130 / max 0.235 |
| Z3 lever paddle CAD→scan unmasked | p95 0.371 / max 0.709 | p95 0.384 / max 0.690 | p95 0.135 / max 0.744 |
| Z4 bushing + tip scan→CAD masked (gated) | p95 0.326 / max 1.265 | p95 0.324 / max 0.734 | p95 0.301 / max 0.737 |
| Z4 bushing + tip scan→CAD unmasked | p95 0.326 / max 1.265 | p95 0.324 / max 0.734 | p95 0.301 / max 0.737 |
| Z4 bushing + tip CAD→scan masked (gated) | p95 0.911 / max 2.351 | p95 1.069 / max 2.636 | p95 1.063 / max 2.602 |
| Z4 bushing + tip CAD→scan unmasked | p95 1.081 / max 2.351 | p95 1.592 / max 2.636 | p95 1.571 / max 2.617 |
| ICP | 44 its, 0.076° / 0.045 mm | 49 its, 0.060° / 0.053 mm | 44 its, 0.053° / 0.059 mm |
| unobservable fraction | 0.58 % | 1.70 % | 1.72 % |
| scan→CAD over-band clusters | 4 | 2 | 2 |
| band_fails | 8 | 7 | 3 |
| mask-dependent passes | 1 | 2 | 3 |

Signed zone probe (qa/zone_probe.json, same bins as it2; + = scan inside the CAD):
- Z2 all: it2 p95 0.344 mean 0.036 → it3 p95 0.229 mean -0.013; bend bin x 33..35: 0.442 → 0.159.
- Z3 all: it2 p95 0.375 → it3 0.134; perimeter/rounds mean signed 0.177 → 0.048.
- Z4 scan→CAD all: it2 p95 0.324 → it3 0.301; z -35..-31 bin (tube entry, bushing top) 0.396 → 0.401 (unchanged, not addressed).

Reading: the it3 changes did what they were meant to do. Z2 (bend) and Z3 (paddle) now pass both directions (Z2 CAD→scan only masked: unmasked max 0.802). The tip neck removed the Z4 hub cells, bringing Z4 scan→CAD p95 from 0.324 to 0.301, but it is still over the band. The rest is the bushing-top collar at the tube entry and the barrel underside rim; neither was changed. The non-geometric misses (observable CAD→scan, Z4 CAD→scan, unmasked D1) are unchanged in cause. Band fails went from 7 to 3.

## Verdict change (owner decision, DECISIONS.md)

Evidence-based verdict of this verify was REVISE (route geometry, loop 3 of 3; gate 69b36b1ef4d5, created 2026-09-28T09:27:39+00:00, archived as qa/_work/gate_REVISE_69b36b1ef4d5.json): the Z4 scan->CAD p95 0.301 miss has a real, unmodelled geometric cause (raised collar on the bushing top at the tube-C entry, plus the barrel underside rim). REVISE at loop 3 became HALT (DECISIONS.md HALT line). The owner resolved the HALT with 'Kabul et, teslim et' (DECISIONS.md last OTHER line, citing gate 69b36b1ef4d5), accepting the it3 band misses instead of a 4th loop. The gate is therefore re-assembled as BAND_NOT_MET, which was already in allowed_verdicts. No deviation run, mask, zone, band or number changed; only review.json#verdict and this note. The Z4 collar stays listed as a real, unmodelled geometric cause (miss_explanations, limitation L6) with its re-run trigger. Delivery still needs the ACCEPT-BAND line citing this re-assembled gate.

Evidence reading kept from the REVISE assembly: of the 3 band fails, Z4 scan→CAD (p95 0.301) has a coherent, one-signed geometric cause that a rebuild could remove. It is the unmodelled bushing-top collar at the tube entry (scan outside the CAD; overlay Z=-33.5, photo_1), plus the barrel underside rim. The miss is marginal: 0.297 in the builder's datum frame, which is not gated, and 75 % of the collar points are within 0.8 mm of a scan-hole edge. The other two fails (observable CAD→scan, Z4 CAD→scan) and the unmasked D1 number cannot be fixed by geometry. Re-run trigger for the collar: limitation L6.

## Skill defects found

Recurring from it1/it2 (`_it2_SUPERSEDED/qa/VERDICT.md` items 1-10), all re-checked on this run:
1. **RECURS.** Functional-interface zones are silently ungated when `interface_max_mm` is null (`deviation_gate.py:349-350`, `verdict.py:92`). Same workaround: Z1-Z4 are written as `kind: "whole"`.
2. **RECURS.** Zone CAD→scan is gated on the masked stats, but whole-part CAD→scan is gated on the observable split (`verdict.py:71`, `:87` vs `:64`). The QA-added M2 now decides both the Z1 and the Z2 CAD→scan passes. Z2 unmasked max 0.802 vs 0.8.
3. **RECURS.** `datum_audit.py` has no tube-axis clock type and only a normals-eigen axis for axis-primary parts. `qa/datum_crosscheck.py` is reused, report-only.
4. **RECURS.** `overlay.py` has no `--registration` (L5).
5. **RECURS.** Observability heuristic blind spots: the any-ray-escapes rule marks only 1.72 % of the CAD unobservable. The 13.6 mm bore and the 2.52 mm pockets therefore stay in the gated 'observable' CAD→scan number.
6. **RECURS.** The census definition differs between sibling skills: `step_check.py:75` excludes `revolution` (77.2 %), while the builder's export check includes it.
7. **RECURS.** `verdict.py render` has no field for a REVISE route, an iteration comparison or skill defects. These sections were appended by `qa/append_it_compare.py` from the gate.json files.
8. **RECURS.** `SKILL.md:58` sets `S=~/.claude/skills/stl-re-verify/scripts`, which does not exist here. The scripts live in `<repo>/skills/stl-re-verify/scripts`.
9. **RECURS.** CHK-LIKE4LIKE has no tooling: there is no protocol or STEP diff script. `qa/it2_it3_diff.py` was written for this run.
10. **RECURS (in a probe).** A run-local signed-distance probe was OOM-killed (exit 137) with no partial output: `trimesh.proximity.signed_distance` in 20000-point chunks on the 484k-triangle it3 tessellation. It completed with 2000-point chunks. The skill gives no memory guidance. All skill scripts were run one at a time and completed.
New in it3:
11. **Scan→CAD has no open-boundary treatment.** `mask-policy.md` defines `open_boundary` for `applies_to: cad` only. Z4 scan→CAD points within 0.8 mm of a scan-hole edge read p95 0.429 against 0.247 away from edges. The skill offers no pre-declared, symmetric way to report or sensitivity-test hole-edge curl in the scan→CAD direction. This run reports it via a probe only and did not add a mask after the fact.
12. **No 'marginal / frame-sensitive miss' reporting.** `verdict.py` compares the post-ICP p95 to the band with no tolerance. That is correct and should stay. But it does not surface that the builder-datum-frame run (`deviation_datum.json`) passes the same zone (0.297 vs 0.301). Its only datum-vs-ICP check covers whole-part scan→CAD p95 differing by more than the band (`verdict.py` assemble), so a zone flipping across the band between frames goes unflagged.

