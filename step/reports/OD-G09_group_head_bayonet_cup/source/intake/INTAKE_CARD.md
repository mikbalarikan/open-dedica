# INTAKE CARD — OD-G10 porta filter holder

Scan: `input/scan.stl` sha256 `94adb6866780b8cdc771dad5cb006d218143b05fd55b6032780e6b2b7b7301f3`
(20,006,234 bytes). Working copy: `intake/work.stl` (400,123 → 250,000 faces, work-vs-full
p95 0.0037 / max 0.084 mm, seed 0; `intake/intake.json#decimation`). Official gates run on the
full-resolution original, never on the working copy. `scan_resolution: full` is an agent
declaration (owner upload as exported, non-round face count), `DECISIONS.md` OTHER 2026-09-28.

## 0. Band regime (declared here, named again in the verdict)
Regime: **baseline-skill, material class plastic**: p95 ≤ 0.30 / max ≤ 0.80 mm
(`baseline/skills/stl2step-build123d/SKILL.md:87`), applied to scan→CAD and to the observable part
of CAD→scan (run-contract §12). `intake/regime.json`.
Why: owner instruction "p95 plastik parça toleransı kullan" (`decisions/owner_request_2026-09-28.md`,
`DECISIONS.md` REGIME). No calipers were supplied, so Tier-1 is not run (scan-only,
`DECISIONS.md` MEASUREMENTS).

## 1. What it is (photos + mesh)
Espresso-machine portafilter holder (group-head collar), moulded black plastic (inferred from the
photos: moulding marks, ejector-pin dimples on the plate). A cup of outer Ø≈80.2 mm with three
internal bayonet lugs at the mouth; the portafilter ears enter through the three gaps, rotate under
the lugs until they hit the lug stop, and are drawn up by the lug underside ramps. Inside, a stepped
shelf, a lip ring and a flat plate at the bottom; the plate has a central two-lobed ("keyhole")
water opening and two screw bosses (photos 1, 2). Static part; the machine housing flange below the
cup (photo 1, lower edge) is outside the scanned region.

## 2. Scan health (numbers from intake.json / alignment.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | 400,123 / 202,623 |
| Bodies; kept; removed fragments % | 1; all; 0.0 % |
| Scanner table removed % | 0.0 % (no table in the scan) |
| Watertight; open boundary edges / loops | no; 5,151 / 16 |
| Normal orientation | ray vote (open mesh), verdict outward, not flipped |
| bbox raw; bbox datum | 81.78 × 85.12 × 46.44 (raw); datum x −40.16..40.23, y −40.20..40.36, z −27.84..3.42 |
| Units verdict (CHK-SCALE) | not run: no calipers; units assumed mm, scale unverified (limitation) |
| Noise floor | 0.0405 mm rms, RANSAC+SVD plane on the lug top pads (2529 faces), `intake/noise_primary.json`. Other clean flats on the same scan: shelf 0.0324, step25 0.0353, floor 0.0421 (`intake/noise_shelf.json`, `noise_step25.json`, `noise_floor.json`). All are the same trimmed estimator (\|d\| < 0.1). |
| Artefact zones | rust / deposit on the rim and inner wall (photos 1, 2) — may add small bumps; a few stray points above the rim in the rim notches (`measure/figures/prof_rimnotch.png`) |

## 3. Coverage / occlusion map (datum frame; `intake/coverage.json`, own survey)
| Zone | r | z | θ | Note |
|---|---|---|---|---|
| C1 whole underside | all | all | all | the scan has almost no downward-facing surface: 0.26 % of area with n_z < −0.5 (lip bead underside, lug edges). Every CAD face that faces down (lug undersides, plate underside, bottom closure) has no scan evidence. |
| C2 below scan extent | 39.7–40.6 (outer wall) | < −27.84 | 357° loop | scan ends at z −27.84 (open loop around the outer wall). Photo 1 shows the part continues into a flange; not scanned. |
| C3 plate interior | < 24.6 | ≈ −19.9 | 357° loop r 23.8–28.2 | the plate inside r ≈ 24 is not in the scan; the keyhole opening and the screw bosses are photo-only (photos 1, 2). |
| C4 under the lugs | 31.6–37.1 | −15 .. −1 | lug sectors (2 loops of 55–57°) | undersides and the bore behind the lugs are hidden; only the lug inner face (r ≈ 31.7) and its lower edge are seen. |
| C5 lip wall in lug sectors | 28.1–31.3 | −20.1 .. −17.8 | 2 loops of 68° | narrow gap between plate and pocket, partly unseen. Photo 2 shows dark arcs here: shadowed pockets, not through-slots (pocket floor scanned at z ≈ −16.6). |
| C6 outer wall θ 38–151 | 40.1 | all (−27.8 .. +2) | 113° | the outer wall is not scanned at all over θ 38–151 (outer-wall area per 30° × 4 mm cell = 0–17 mm² vs ~84 elsewhere). Photos 1–2 show the cup joined to the machine housing on that side. The CAD continues the cylinder there (assumed). *Extent corrected 2026-09-28 during the builder self-check; the first entry read "below z −15, partly". Located from the scan, not from the CAD.* |
Angular coverage per radial band (`coverage.json#radial_bands`): r 20.3–24.4 only 41°; r ≥ 24.4 ~360°.

Masks these coverage facts would justify (for verify to decide, declared before any gate number):
CAD-side region "downward-facing" (n_z < −0.5, C1), CAD-side region "below the scan extent / inside
the wall below the floor" (C2), CAD-side region "plate interior r < 24" (C3), open-boundary mask at
the scan hole edges. A pass that depends on them is a limitation, never a clean pass.

## 4. Functional surfaces & interfaces (each can become a gate zone)
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| I1 lug inner faces | r ≈ 31.7, 3 × 54° | centre / guide the portafilter ears | yes (inside jaws across lugs) | regime p95/max |
| I2 lug underside ramps | hidden (C4) | draw the portafilter up | no (hidden) | not gateable |
| I3 lug stops | θs .. θs + 6.5°, down to z ≈ −10.5 | rotation end stop | partly | regime |
| I4 bore | r ≈ 37.0 (drafted) | portafilter clearance | yes | regime |
| I5 shelf / pockets | z −13.4 .. −16.6 | gasket / ear clearance | depth gauge | regime |
| I6 plate top | z ≈ −19.94 | shower plate seat, screw bosses | depth gauge | regime |
`interface_max` is null in this regime, so no zone has its own band; zones are reported.

## 5. Feature enumeration — interior included (CHK-ENUM)
| # | Feature | Seen in mesh (where) | Seen in photo | Status |
|---|---|---|---|---|
| F01 | outer cup wall Ø≈80.2 | r 40.1, z −27.8..+2 | 1 | both |
| F02 | rim: raised inner lip + lower outer ledge | z +3.30 / +2.49 | 1, 2 | both |
| F03 | 6 rim notches (lip cut down to the ledge), 2 per lug | θ 11–18.5, 101–108.5, 130.5–138, 221–228.5, 251–258.5, 341–348.5 | 2 (notches at the rim) | both |
| F04 | bore r≈37.0 with draft | gap sectors | 1 | both |
| F05 | 3 bayonet lugs (top z 0, inner r 31.7, 54° each) | θ 336–30, 96–149.5, 216–270 | 1, 2 | both |
| F06 | lug top channel (z −2.9, between lug and bore), closed at both ends | θs+4 .. θs+45 | 2 (L-shaped channels) | both |
| F07 | lug stop (θs .. θs+6.5, down to z −10.5) | inner face | 1 (block under lug) | both |
| F08 | lug underside: shallow ramp then steep ramp to the lug end | lower edge of inner face | not visible | mesh (edge only) → hidden faces assumed |
| F09 | shelf between lugs (z −14.1 / −13.4 / −14.2) | 3 gaps | 1, 2 | both |
| F10 | under-lug pockets, two steps (outer ≈ −15.0, inner ≈ −16.6), riser r ≈ 34.3 | lug sectors ±5° | 2 (dark arcs) | both |
| F11 | lip ring: rounded shelf edge, wall r≈30.8, lower step r≈31.3 | r 30.7–31.4, z −20..−14.4 | 2 (glossy ring) | both |
| F12 | plate top | z −19.94, r ≥ 24.6 | 1, 2 | both (outer part only) |
| F13 | plate keyhole opening (two lobes) | not scanned (C3) | 1, 2 | photo-only → photo-inferred |
| F14 | 2 screw bosses with holes | not scanned | 1, 2 | photo-only → photo-inferred |
| F15 | through hole next to a boss (bright in photo 2), ejector dimples | not scanned | 2 | photo-only → hole: photo-inferred; dimples cosmetic, not modelled |
| F16 | flange and part below z −27.84 | not scanned (C2) | 1 | not modelled (outside scan) |
| F17 | shallow relief groove at the bore/shelf corner (≈0.3–0.7 deep) | r ≈ 36.8–37.2 | not visible | mesh-only, small → simplified |
CHK-ENUM result: both photos walked (1: 3/4 view into the cup, 2: top view). Radial-band z extents
(coverage.json) show nothing above the rim (z max 3.42) and nothing on the axis. No unexplained
cluster. Open items: F13–F15 are photo-only with no scale reference, declared photo-inferred.

## 6. Datum plan and result (`intake/alignment.json`, status OK)
- Primary (levels): the three bayonet lug top pads → XY @ z = 0. WHY: the lug pads are moulded
  flats square to the cup axis and carry the bayonet; the plate/floor is tilted ~0.24° against the
  axis and wavy (`measure/figures/levels.json`), so it is not a clean datum. Fit rms 0.0405 /
  max 0.099 mm (untrimmed rms 0.0436 / max 0.159). **The noise floor was measured on the same pads**
  (self-referential STOP check, the OD-H22 precedent); the other flats read 0.032–0.042 with the same
  estimator, so the STOP rule has no tie margin here (open defect D1, `evals/real-runs/OD-H22.md`).
- Secondary: outer cup-wall axis, wall-face IRLS, 8 stations over z −23.5..−2.5, R 40.104 ± 0.033,
  median circle rms 0.057, worst 0.525. WHY: portafilter/bayonet rotation axis. No circle noise
  floor (no closed section loop exists), so the secondary residual is not compared (finding).
- Clock: fourier_mass n = 3 on the lug band, angle 34.76°; lug 1 = the candidate nearest +X
  (convention; the lugs are identical within the scan: starts at 336 / 96 / 216°).
- Origin: cup outer-wall axis ∩ bayonet lug top plane.
- Tilt (CHK-TILT): 0.205° ± 0.025° over 21 mm (one feature), below the 0.3° reference: pass.
- Sanity landmarks: primary at z 0 (−0.0015), rim top 3.42 (exp 3.4 ± 0.4), floor −19.94
  (exp −19.95 ± 0.4), outer wall r 40.10 (exp 40.1 ± 0.2): all ok.

## 7. Rebuild strategy summary
Revolve of the gap-sector half profile (outer wall, rim lip and ledge, drafted bore, shelf, lip
ring, plate); three lugs as arc-sector prisms from the bore to r 31.7 with a channel cut, a stop
block and two planar underside cuts; three under-lug pocket cuts; six rim-notch cuts; per-instance
shelf/pocket levels where the scan differs beyond noise; plate keyhole and bosses photo-inferred.
Below the plate: assumed plate thickness and a wall continuing to the scan extent (C2 closure).
Plan: `build/MODELING_PLAN.md`.

## 8. Risk flags and operator declarations
- Scan-only: absolute scale not caliper-verified; Tier-1 not run.
- Plate keyhole, bosses and holes: photo-inferred from an oblique photo without a scale reference
  (±3 mm, ±10°); a caliper/photo with a ruler would confirm them.
- Everything below the plate top and under the lugs is assumed (no scan).
- Shelf and pocket floors are wavy (3-lobed, up to ±0.4 mm within one sector) and one gap is
  0.7 mm higher than the other two; could be moulding warp or a compressed gasket insert. The
  model uses flat per-instance levels (declared simplification).
- Inner features (lug inner faces) sit 0.19 mm off the outer-wall axis (`measure/figures/instances.json`).
Question for the owner: is the inner stepped ring (shelf / pockets / lip) a separate rubber gasket
or part of the moulding? The scan shows one body; it is modelled as one solid.

## 9. Measurement request → `intake/MEASUREMENTS.md`
Filled with scan-predicted values. No readings were supplied (scan-only run).
