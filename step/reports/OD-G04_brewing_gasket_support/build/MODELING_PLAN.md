# MODELING PLAN: OD-G04_brewing-gasket-support

Iteration: it1 of 3. Params: `measure/params.json` (67 params, all used; build_log.txt lists no
UNUSED line).

## 0. Build deviations

| Item | Planned | Built | Why | Declared to verify/deliver |
|---|---|---|---|---|
| Edge rounds | fillet ops at the end | drawn as tangent arcs inside the F01/F02 revolve profiles | every measured round lies in the (r,z) profile; profile arcs are exact and cannot fail; `fillets.json` therefore has no entries | yes (here) |
| Slot cut inner wall | r = hub_ring_R_out | r = hub_ring_R_out − 0.001 | a coincident cylinder made the OCC boolean invalid; 1 µm guard (EPS in model.py), 49× below the noise floor | yes (here) |
| Plan changes after the first self-comparison (scan→CAD on 100k samples, not a grade) | — | added: stepped hub bore (hub_bore_*), lip bead (F01b), boss-A webs (F05b), flange/lip fillet; corrected flange_inner_round_R 1.96→2.65, tab_R_out 34.38→34.52 | first self-check p95 0.292 / max 1.02 showed unplanned features at r 11 and r 19.8 on the boss-A lines, at r 31.2 on the lip, and in the hub bore | yes; params evidence probe_p16..p22 |

## 1. Strategy summary
A revolved cup. ONE (r,z) profile (F01) carries the plate, back bead, hub ring, 42.7° cone,
centre bore and post, stepped hub tube with full-round bottom, cup wall, flange with the
inner R2.65 round, and the gasket lip with its full-round top. A 360° lens (F01b) adds the lip
bead. 3 bayonet tabs are sector revolves at 120° (F02). Ribs, ring-rib arcs, bosses and webs are
one instance + placements (F03–F05b). Holes and slots are cut tools subtracted once (F06).

## 2. Expectations (reported, not gated)
- Ops before rounds: 8 (F01, F01b, F02, F03, F04, F05, F05b, F06).
- Expected faces 140–220 (profile ~30 + tabs 3×6 + ribs 6×10 + arcs 2×6 + bosses 4×3 + webs 2×6 + holes 4×4 + slots 4×4). Built: 174.
- Surface types: planes, cylinders, cones, tori (profile arcs). No B-splines, no lofts.

## 3. Ordered feature list
| F## | Operation | Datum / plane | Driving params (source) | Acceptance |
|---|---|---|---|---|
| F01 | revolve rounded (r,z) profile | axis Z, XZ | plate_*, bead_*, hub_ring_*, cone_*, centre_*, hub_bore_*, hub_tube_*, cup_*, flange_*, lip_*, *_round_R (scan; centre_post_R_out photo-inferred) | 1 solid; radii re-measured on STEP |
| F01b | revolve lens (bead) | axis Z | lip_bead_* (scan) | bead peak r 31.175 |
| F02 | 3 × sector revolve | axis Z | tab_* (scan) | 3 tabs, span 61.08°, centres −3.3 + k·120 |
| F03 | 6 × radial rib (2 boxes, stepped bottom) | XY | rib_* (scan, equal pitch with scatter note) | 6 ribs at 22.9 + k·60 |
| F04 | 2 × ring-rib arc (sector revolve) | axis Z | ring_rib_* (scan) | arcs 26–141°, 205–321° (+rib overlap) |
| F05 | 4 × boss cylinder | XY | boss_R_out, bossA_*, bossB_* (scan, measured angles kept) | 4 bosses, 2 bottom heights |
| F05b | 2 × web on boss-A lines | XY | webA_* (scan) | webs hub→wall at −6.55°, 172.95° |
| F06 | cut: 4 counterbored holes + 4 slots | XY | boss_cb_*, boss_hole_*, slot_* (scan) | holes Ø3.06 / cb Ø4.0; slots 40.25° |

## 4. Intake feature map (CHK-ENUM)
| Intake feature | Built by | or: out of scope because |
|---|---|---|
| E1 plate, E2 bead, E3 hub ring/cone/bore, E5 cup wall, E6 flange/lip, E8 hub tube, E9 post | F01 (+F01b bead) | — |
| E4 slots | F06 | — |
| E7 tabs | F02 | — |
| E10 ribs, E11 ring arcs | F03, F04 | — |
| E12 bosses | F05 + F06 | — |
| E13 webs | F05b | — |
| E14 moulded text | — | cosmetic; relief ≲0.3 mm; declared simplification |

## 5. Fillet / chamfer plan (CHK-FILLET)
No fillet ops. All rounds are tangent arcs of the revolve profiles, from params: flange_inner_round_R 2.65,
flange_lip_fillet_R 1.084, wall_flange_fillet_R 0.38, plate_edge_round_R 0.316, flange_outer_round_R 0.196;
full rounds (half the wall) on the bead top, lip top, hub tube bottom and tab outer end. Not modelled
(declared in params.json simplifications): rib bottoms, boss bottom edges, rib/boss root fillets.

## 6. Unscanned or invented geometry (provenance)
| Item | Value | Source tag | Why it is needed |
|---|---|---|---|
| centre post outer radius | 2.5 | photo-inferred | the scanned bore wall (r 1.30 to z −5.64) needs material around it |
| plate underside outside 20–80° | z −2.59 | scan (one sector), assumed planar elsewhere | closes the plate |
| hub interior between post and hub bore | plate underside | assumed | unscanned |

## 7. Known risks
Tab 1 sits 0.15 mm low; tab C bottom recess; rib direction scatter ±1.2°; boss 172.95 larger
counterbore; drafts on cup, lip and hub outer walls (all in params.json simplifications).
