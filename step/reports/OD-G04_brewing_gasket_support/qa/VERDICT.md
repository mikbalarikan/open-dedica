# VERDICT: BAND_NOT_MET

Regime: **baseline-skill** (baseline/skills/stl2step-build123d/SKILL.md:87); bands {'p95_mm': 0.3, 'max_mm': 0.8, 'tier1_abs_mm': None, 'interface_max_mm': None}.
Independence: fresh agent (stl-re-verify stage), did not build the model; QA scripts from skills/stl-re-verify only; build/model.py only grepped for loft/polyline (never imported/executed); measure/params.json and build_log.txt not read; datum spec, zones and masks written by QA from INTAKE_CARD/alignment descriptions. Boss-hole zone boxes were placed from the STEP's own hole faces (B-rep query, reporting boxes only, not expected values).

Scan: `input/scan.stl` (full-res), label **OFFICIAL (full-res)**.

## Gate table

| Gate | Band | Measured | Result |
|---|---|---|---|
| Hash freeze | unchanged | unchanged | PASS |
| Validity `OD-G04_brewing-gasket-support_datum.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 17086.244 mm³ | PASS |
| Validity `OD-G04_brewing-gasket-support.step` | 1 valid closed solid | solids 1, valid True, naked edges 0, V 17086.244 mm³ | PASS |
| Datum audit (report-only) | ≤0.3° / ≤0.15 mm (RE_SPEC.md:241) | 1.309° / origin 0.031 mm / points p95 0.752 max 0.834 mm | outside (not blocking) |
| Registration (ICP) | converged | 200/300 its, 0.337° / 0.332 mm | PASS |
| scan_to_cad:masked | p95 ≤0.3 / max ≤0.8 | n 245660 · rms 0.200 · p50 0.136 · p95 0.376 · p99 0.450 · max 0.832 | FAIL |
| cad_to_scan_observable | p95 ≤0.3 / max ≤0.8 | n 18753 · rms 0.922 · p50 0.219 · p95 2.325 · p99 3.274 · max 4.592 | FAIL |

## Deviation detail (masked and unmasked side by side)

- scan→CAD unmasked: n 245660 · rms 0.200 · p50 0.136 · p95 0.376 · p99 0.450 · max 0.832
- scan→CAD masked: n 245660 · rms 0.200 · p50 0.136 · p95 0.376 · p99 0.450 · max 0.832
- CAD→scan unmasked: n 300000 · rms 1.085 · p50 0.241 · p95 2.594 · p99 3.555 · max 4.814
- CAD→scan masked: n 300000 · rms 1.085 · p50 0.241 · p95 2.594 · p99 3.555 · max 4.814
- CAD→scan observable only: n 18753 · rms 0.922 · p50 0.219 · p95 2.325 · p99 3.274 · max 4.592; unobservable fraction 6.24 %

Masks:

- none

Zones:

- Z1_back_face_bead [functional_interface] scan_to_cad: unmasked n 32326 · rms 0.219 · p50 0.187 · p95 0.366 · p99 0.392 · max 0.430 | masked n 32326 · rms 0.219 · p50 0.187 · p95 0.366 · p99 0.392 · max 0.430
- Z1_back_face_bead [functional_interface] cad_to_scan: unmasked n 33406 · rms 0.269 · p50 0.272 · p95 0.380 · p99 0.400 · max 1.006 | masked n 33406 · rms 0.269 · p50 0.272 · p95 0.380 · p99 0.400 · max 1.006
- Z2_flange_lip [functional_interface] scan_to_cad: unmasked n 79465 · rms 0.214 · p50 0.166 · p95 0.383 · p99 0.452 · max 0.551 | masked n 79465 · rms 0.214 · p50 0.166 · p95 0.383 · p99 0.452 · max 0.551
- Z2_flange_lip [functional_interface] cad_to_scan: unmasked n 79008 · rms 0.318 · p50 0.215 · p95 0.461 · p99 1.157 · max 2.761 | masked n 79008 · rms 0.318 · p50 0.215 · p95 0.461 · p99 1.157 · max 2.761
- Z3_bayonet_tabs [functional_interface] scan_to_cad: unmasked n 20554 · rms 0.266 · p50 0.217 · p95 0.419 · p99 0.561 · max 0.832 | masked n 20554 · rms 0.266 · p50 0.217 · p95 0.419 · p99 0.561 · max 0.832
- Z3_bayonet_tabs [functional_interface] cad_to_scan: unmasked n 15488 · rms 0.405 · p50 0.278 · p95 0.727 · p99 1.611 · max 2.095 | masked n 15488 · rms 0.405 · p50 0.278 · p95 0.727 · p99 1.611 · max 2.095
- Z4_boss_holes [functional_interface] scan_to_cad: unmasked n 6804 · rms 0.202 · p50 0.155 · p95 0.367 · p99 0.460 · max 0.545 | masked n 6804 · rms 0.202 · p50 0.155 · p95 0.367 · p99 0.460 · max 0.545
- Z4_boss_holes [functional_interface] cad_to_scan: unmasked n 3828 · rms 0.369 · p50 0.209 · p95 0.854 · p99 1.109 · max 1.362 | masked n 3828 · rms 0.369 · p50 0.209 · p95 0.854 · p99 1.109 · max 1.362
- I1_hub_interior [interior] scan_to_cad: unmasked n 2054 · rms 0.114 · p50 0.081 · p95 0.210 · p99 0.313 · max 0.352 | masked n 2054 · rms 0.114 · p50 0.081 · p95 0.210 · p99 0.313 · max 0.352
- I1_hub_interior [interior] cad_to_scan: unmasked n 1644 · rms 1.330 · p50 1.114 · p95 2.426 · p99 2.827 · max 3.133 | masked n 1644 · rms 1.330 · p50 1.114 · p95 2.426 · p99 2.827 · max 3.133
- I2_plate_underside_unscanned_sectors [interior] scan_to_cad: unmasked n 0 | masked n 0
- I2_plate_underside_unscanned_sectors [interior] cad_to_scan: unmasked n 12326 · rms 2.293 · p50 2.275 · p95 2.546 · p99 2.659 · max 2.832 | masked n 12326 · rms 2.293 · p50 2.275 · p95 2.546 · p99 2.659 · max 2.832
- I3_outer_wall_gap [interior] scan_to_cad: unmasked n 3121 · rms 0.243 · p50 0.255 · p95 0.320 · p99 0.335 · max 0.359 | masked n 3121 · rms 0.243 · p50 0.255 · p95 0.320 · p99 0.335 · max 0.359
- I3_outer_wall_gap [interior] cad_to_scan: unmasked n 11141 · rms 2.170 · p50 1.967 · p95 3.874 · p99 4.428 · max 4.814 | masked n 11141 · rms 2.170 · p50 1.967 · p95 3.874 · p99 4.428 · max 4.814
- B1_zband_plate [region] scan_to_cad: unmasked n 46209 · rms 0.214 · p50 0.185 · p95 0.360 · p99 0.391 · max 0.626 | masked n 46209 · rms 0.214 · p50 0.185 · p95 0.360 · p99 0.391 · max 0.626
- B1_zband_plate [region] cad_to_scan: unmasked n 66836 · rms 1.177 · p50 0.307 · p95 2.384 · p99 2.580 · max 2.873 | masked n 66836 · rms 1.177 · p50 0.307 · p95 2.384 · p99 2.580 · max 2.873
- B2_zband_mid [region] scan_to_cad: unmasked n 116220 · rms 0.169 · p50 0.102 · p95 0.359 · p99 0.425 · max 0.832 | masked n 116220 · rms 0.169 · p50 0.102 · p95 0.359 · p99 0.425 · max 0.832
- B2_zband_mid [region] cad_to_scan: unmasked n 164577 · rms 1.249 · p50 0.247 · p95 3.035 · p99 3.801 · max 4.814 | masked n 164577 · rms 1.249 · p50 0.247 · p95 3.035 · p99 3.801 · max 4.814
- B3_zband_front [region] scan_to_cad: unmasked n 83231 · rms 0.230 · p50 0.179 · p95 0.401 · p99 0.493 · max 0.817 | masked n 83231 · rms 0.230 · p50 0.179 · p95 0.401 · p99 0.493 · max 0.817
- B3_zband_front [region] cad_to_scan: unmasked n 68587 · rms 0.230 · p50 0.142 · p95 0.418 · p99 0.526 · max 1.362 | masked n 68587 · rms 0.230 · p50 0.142 · p95 0.418 · p99 0.526 · max 1.362

Over-band scan→CAD points (> 0.8 mm): 3 (0.001 %) in 0 clusters ≥ 20 pts.


## Checks

| Check | Result | Note |
|---|---|---|
| CHK-MASK | pass | no pass depends on a mask |
| CHK-CLUSTER | pass | 0 scan->CAD over-band clusters; unexplained: [] |
| CHK-OVERLAY | pass | every panel shows scan |
| CHK-CIRCULAR | finding | QA gate independent: own ICP (T_refine QA-only, not written back), no expected values used. Finding: the builder's plan-change loop used a scan->CAD self-comparison on 100k samples (MODELING_PLAN §0) and every param is scan-derived (scan-only run) - that record is a consistency check, not independent evidence. |
| CHK-LIKE4LIKE | n/a | iteration 1; no _itN_SUPERSEDED to compare |
| CHK-INDEP | pass | fresh agent context; own scripts; builder numbers not used |
| CHK-FILLET | pass | export_check fillets [] (no fillet ops); all rounds are tangent arcs in revolve profiles, declared in MODELING_PLAN §0/§5; rib/boss root fillets declared not modelled (not silent) |
| CHK-PATCHWORK | pass | QA census: 174 faces, analytic area 100% (plane 107, cylinder 54, torus 12, cone 1), 0 freeform; grep of build/model.py: no loft/ruled/polyline |
| CHK-ENUM | finding | intake E1-E13 all present in CAD and visible in overlays/photos (6 ribs, 2 ring arcs, 4 bosses, 2 webs, 3 tabs, hub tube, 4 back slots, centre post); nothing hallucinated. Finding: E14 moulded text and the ejector-pin dimples on the flange (photo 1) are not modelled (declared/cosmetic); no scan->CAD over-band cluster >=20 pts |
| CHK-ACHIEVABLE | n/a | Tier-1 not run (no calipers) |
| PHOTO-PLAUSIBILITY | pass | 4 catalogue photos walked: front (ribs, arcs, bosses, hub, tabs), back (plate, bead, conical recess, 4 slots, centre bore) and side views agree with CAD overlays; no scale reference |

## Misses, per region

- scan_to_cad:masked: p95 0.376 max 0.832 vs 0.3/0.8
- cad_to_scan_observable: p95 2.325 max 4.592 vs 0.3/0.8
- **whole part scan->CAD p95 (0.376 vs 0.30)**: registration, not geometry: default QA ICP matched CAD faces to the opposite skin across 2.3-2.6 mm walls (sign-free normal test, 3 mm correspondence) and shifted the CAD 0.29 mm in z; even the flat back face Z1 reads p95 0.366 post-ICP vs 0.146 in the builder datum frame. Datum frame p95 0.218 and diagnostic ICP (max_corr 1.0) p95 0.194 both pass. Options: accept on the datum-frame/diagnostic evidence (human ACCEPT-BAND), or re-grade after a skill-level decision on ICP correspondence distance
- **whole part scan->CAD max (0.832 vs 0.80)**: 3 isolated scan points of 245,660 (no cluster >=20): one on a bayonet-tab end corner r 35.35 theta 257.6 z -8.55 (scan extends ~0.8 mm beyond the CAD tab radius 34.52 locally), two at r 21.6 theta 263 z -13.5 at the cup-wall/flange root. Persists in every frame (datum 0.833, diagnostic 0.857). Options: REVISE tab end/root geometry locally (small), or accept as scan edge fuzz; a caliper reading of tab outer radius would arbitrate
- **CAD->scan observable (p95 2.325 / max 4.592 vs 0.30/0.80)**: coverage: the front cavity (plate underside outside 20-80 deg, rib sides, cup inner wall, hub interior) and the outer wall gap theta -69..+27 were not scanned (INTAKE_CARD §3); the ray test counts them as observable. Where the scan exists it overlays the CAD (overlays). Not fixable by geometry. Options: rescan the front cavity/outer wall, or calipers on plate thickness, rib heights and wall thickness; or human acceptance of the unscanned-region extrapolation

## Declared limitations (each with its re-run trigger)

1. Tier-1 not run: no caliper sheet (scan-only run, DECISIONS.md MEASUREMENTS). — **Re-run trigger:** any caliper reading
2. Absolute scale not caliper-verified (CHK-SCALE not run; units assumed mm). — **Re-run trigger:** any caliper reading
3. Default-parameter QA ICP (max_corr 3.0 mm) converged only after raising the cap 60->300 (run1 at cap 60 not converged: registration_run1_cap60.json) and applies a 0.29 mm +z shift contradicting QA's own datum audit (plane origin offset 0.03 mm); a diagnostic ICP with max_corr 1.0 mm (qa/diagnostic/, not the gate) moves only 0.044 mm. — **Re-run trigger:** skill decision on ICP correspondence distance for thin-walled parts, then re-run verify
4. Observability split is blind to line-of-sight-visible but unscanned surfaces: the front cavity (plate underside outside 20-80 deg, rib sides, hub interior) and the outer-wall gap count as 'observable'. 65% of CAD->scan over-band samples have their nearest scan point within 0.8 mm of a scan hole edge. — **Re-run trigger:** a rescan covering the front cavity and the outer wall theta -69..+27
5. deviation_gate.py observability OOM-killed at ~13.6 GB with the default 2000-ray chunk; run through a call wrapper that lowers observable_split(chunk=) to 50 (identical per-ray results). No skill script was edited. — **Re-run trigger:** none needed unless the skill changes the ray engine

## Claim boundary

Not a caliper-verified or tolerance-grade model: no Tier-1, scale unverified, front cavity and hub interior extrapolated from partial scan. Fit for form/visual and fit-check prototyping only; not for tooling or mating-interface manufacture until calipered.

_All numbers above are read from `qa/gate.json` (CHK-NUMBERS). Allowed verdicts given the evidence: BAND_NOT_MET, HALT, REVISE._
