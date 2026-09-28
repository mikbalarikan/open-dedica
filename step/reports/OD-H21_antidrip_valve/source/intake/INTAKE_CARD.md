# INTAKE CARD — OD-H21_antidrip-valve (DeLonghi anti-drip valve, scanned assembly)

Scan: `input/scan.stl` sha256 `4553ccbeee70167f15be759ac21ebe8b1b3cba9cd03a87f75b310eba0be85aad`
(`intake/intake.json#inputs`). Working copy: `intake/work.stl` (600,142 → 600,142 faces, **not
decimated**, `--work-faces 0 --keep all`; sha256 `fe337680…a375e9c`). The working copy is the full
resolution original, welded; official gates still run on `input/scan.stl`.

## 0. Band regime (declared here, named again in the verdict)
Regime: **baseline-skill, material class plastic: p95 ≤ 0.30 / max ≤ 0.80 mm**
(`baseline/skills/stl2step-build123d/SKILL.md:87`), written to `intake/regime.json`.
Why: owner instruction 2026-09-28 "p95 plastik parça toleransı kullan" (DECISIONS.md REGIME);
scan-only job, so RE_SPEC Tier-1 cannot run. Applies to scan→CAD and to the observable part of
CAD→scan (run-contract §12).

## 1. What it is (photos + mesh)
Anti-drip / steam valve of a DeLonghi espresso machine (catalogue photos `photo_1.png`,
`photo_2.png`, no scale). Moulded white plastic (inferred) plus one black elastomer O-ring.
From the nozzle end: a plug-in **spigot (nozzle)** Ø11.56 with four corner lugs and a latch window at
its tip → **ribbed nut** (8 ribs) whose bottom face is the nozzle shoulder → **band ring** (two steps)
→ **body cylinder** Ø20.04 carrying a radial **side outlet** (tube, collar, black O-ring, G1/8-like
thread, end bore) → **cap part** (ring skirt Ø26.5 with 4 rectangular windows + cap Ø24.3) → a
**hose barb** lying across the cap top.
**It is an assembly scanned as one closed shell**: the sub-parts sit on their own axes. Measured in
the datum frame (`measure/figures/fits.json#segments`): the nozzle axis is tilted 1.36° to the band
face normal; the cap part (ring + cap, one moulding: common axis fit rms 0.051/0.035) is tilted
3.36°; nut / band / body centres are offset 0.07–0.25 mm from each other. Static part, no moving
features visible. Internal flow passages and valve internals are **not in the scan** (bridged).

## 2. Scan health (numbers from intake.json / alignment.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | 600,142 / 300,181 |
| Bodies; kept; removed fragments % | 1; all; 0.0 % |
| Scanner table removed % (rule used) | 0.0 % (none present) |
| Watertight; open boundary edges / loops | no; 238 edges / 7 loops (coverage §3) |
| Normal orientation | ray vote (open mesh), outward, hit-against 0.98, not flipped |
| bbox raw; bbox datum | raw 47.37 × 33.90 × 60.63; datum 43.83 × 38.01 × 55.94 (z −27.455 … 28.483) |
| Units verdict (CHK-SCALE) | **FLAG**: no calipers, no scale reference; units assumed mm, no scale applied |
| Noise floor | plane: 0.0347 mm rms on the nozzle end face (`noise_primary.json`); circle: 0.0325 mm rms on a cap OD section (`noise_circle.json`). Other flats for reference: band top 0.0266, shoulder 0.0407, cap top 0.0457 (`noise_plane_*.json`) |
| Artefact zones | nozzle tip bore mouth ragged (open loop 1); interior bridged everywhere; small speckle on the ring top edge (θ ≈ −120, −5, 20, 140); O-ring is a separate black part |

## 3. Coverage / occlusion map (datum frame; from `intake/coverage.json`)
| Zone | r | z | θ | Note |
|---|---|---|---|---|
| L1 nozzle bore wall end | 3.07–3.96 | −26.37…−22.84 | 350° span | bore seen ~2–4 mm deep, then open (unscanned) |
| L2 ring window θ≈180 | 11.87–13.16 | 13.61–14.98 | 175–187 | window opens into unscanned interior |
| L4 ring window θ≈107 | 11.17–12.76 | 13.53–14.87 | 102–113 | same |
| L3 outlet end bore | 28.24–29.97 | 2.53–4.59 | −2…2 | bore mouth ~1.5 mm deep then open |
| L6 barb end bore | 26.71–27.91 | 24.04–25.18 | 53–56 | bore mouth ~1.6 mm deep then open |
| L5, L7 under ring skirt | 10.3–11.3 | 9.96–11.59 | −149, 152 | slits between ring skirt and body, interior unseen |
Angular coverage: every radial band r < 15.1 covers 360° (bands r > 15 are the outlet and barb, not
round). No partial angular coverage on the round features.

## 4. Functional surfaces & interfaces (each becomes a gate zone)
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| I1 | nozzle OD Ø11.56 + corner lugs + latch window | plug-in spigot, bayonet/latch in the machine | yes (OD, lug span) | p95/max |
| I2 | nozzle shoulder (nut bottom face) | axial seat of the spigot | depth only | p95/max |
| I3 | outlet thread (≈G1/8, pitch 0.908) and O-ring | sealed threaded port | yes (thread OD, O-ring OD) | p95/max |
| I4 | barb tube Ø5.5 + bulb Ø7.4 | hose connection | yes | p95/max |
| I5 | cap ring windows ×4 | snap latches (cap part to body) | width only | p95/max |

## 5. Feature enumeration — interior included (CHK-ENUM)
| # | Feature | Seen in mesh (where) | Seen in photo (id) | Status |
|---|---|---|---|---|
| E01 | nozzle cylinder Ø11.56 (tilted 1.36°) | z −27.3…−14.0 | photo_2 left, photo_1 left | both |
| E02 | nozzle tip face, outer round, bore mouth Ø7.88 | z −27.3; open loop L1 | photo_2 (open end) | both; bore depth occluded |
| E03 | four corner lugs (rounded rectangle 11.27 × 11.93) | z −25.8…−23.1 | photo_2 (lip at the tip) | both |
| E04 | latch window through the lug side at θ≈114 | z −25.3…−24.25 | photo_2 (slot at the tip) | both |
| E05 | nozzle shoulder (nut bottom face) + root fillet | z −14.04 | photo_2 | both |
| E06 | nut: drafted cylinder + 8 vertical ribs (45° pitch) | z −14.0…−6.2 | photo_2 (ribbed nut) | both |
| E07 | nut → band chamfer | z −6.9…−5.6 | photo_2 | both |
| E08 | band lower ring Ø24.4 (drafted) | z −5.6…−2.55 | photo_2 (band) | both |
| E09 | band upper ring Ø24.0 with top round; band top face (primary) | z −2.55…0 | photo_2 | both |
| E10 | body cylinder Ø20.04 | z 0…9.6 | photo_1, photo_2 | both |
| E11 | side outlet tube Ø9.22 | outlet u 10…19.5 | photo_1, photo_2 | both |
| E12 | outlet collar Ø13.70 with rounds | u 20.0…22.7 | photo_2 | both |
| E13 | O-ring (black) | u 22.7…24.5 | photo_1, photo_2 (black ring) | both (separate part) |
| E14 | outlet thread (pitch 0.908, crest/root smoothed by the scanner) | u 24.6…29.4 | photo_2 (thread) | both |
| E15 | outlet end chamfer, end face, end bore Ø3.2 | u 29.3…30.0, L3 | photo_2 | both; bore depth occluded |
| E16 | cap part ring skirt Ø26.54 (tilted 3.36°) | z 9.6…16.8 | photo_1, photo_2 | both |
| E17 | 4 ring windows (θ ≈ −67, 0, 112, 180) | z 12.2…14.9; L2, L4 | photo_1, photo_2 (rectangular windows) | both |
| E18 | cap Ø24.28 + top face + edge rounds | z 16.8…23.3 | photo_1, photo_2 | both |
| E19 | barb tube Ø5.5 across the cap top (az 55.7°), rear end at u −3.0 | z 21.5…27.2 | photo_1, photo_2 | both |
| E20 | barb flare + bulb cone + end face + end bore Ø2.5 | u 23…28.4, L6 | photo_1, photo_2 | both; bore depth occluded |
| E21 | slits under the ring skirt (L5, L7) | θ −149, 152 | not visible | mesh-only: assembly gap, interior; not modelled |
| E22 | ring-top speckle bumps | θ −120, −5, 20, 140 | not visible | mesh-only: < 0.3 mm, scan speckle / gate marks; not modelled |
| E23 | shallow recess on lug side θ≈−66 | z −25.4…−24.2, depth ≈ 0.2 | not visible | mesh-only: < 0.25 mm; not modelled (declared) |
| E24 | internal flow passages, valve seat, spring (anti-drip function) | not in scan (bridged shell) | not visible | occluded → out of scope, declared |

CHK-ENUM result: **pass**. Both profile photos checked (photo_1, photo_2); on-axis / above-top material
checked: the only material on the axis above the cap top (r < 3, z 23.4–27.1) is the barb tube
crossing the axis (E19). Unexplained clusters: none. E21–E24 carry declarations.

## 6. Datum plan and result (from alignment.json, status **OK**)
- Primary (levels): **band top face** (up-facing annulus r 10–11.5 where the body leaves the band) →
  XY @ z = 0, +Z towards the cap. WHY: flat perpendicular to the valve axis at the band/body
  interface and the cleanest scanned flat (0.0266 over seeds 0–7; the nozzle shoulder reads
  0.041–0.042, which would STOP against the 0.0347 end-face noise). Its normal agrees with the body
  axis within 0.11° (`fits.json#segments.body_tiltfree`). Fit rms 0.0266 / max 0.1016
  (untrimmed 0.0256 / 0.1016), 7,175 faces, 52.6 mm².
- Secondary: nozzle OD axis (Kåsa, 15 stations z −22…−15): median rms 0.0313 / worst 0.1130 vs
  circle noise 0.0325 (tie margin small, see risk R6). WHY: the plug-in spigot is the functional
  insertion axis and the cleanest circle.
- Clock: plane_normal of the **side-outlet collar outer face** → +X, rotation 13.878°; collar face fit
  rms 0.0255, 0.54° out of perpendicular to Z. WHY: the threaded outlet is the second functional port.
- Origin: **nozzle OD axis ∩ band top face plane**.
- Tilt (CHK-TILT, **finding**): 1.267° ± 0.032° over 7.0 mm (nozzle only). The nozzle is really tilted
  against the band face; the body is square to it (0.11°); the cap part is tilted 3.36°. This is the
  as-scanned assembly state; measure and rebuild carry each sub-part's own axis (keep-measured).
- Sanity landmarks: primary at z = 0 (−0.0003, ok); nozzle tip zmin −27.455 (exp −27.3 ±0.4, ok);
  shoulder −14.033 (exp −14.0 ±0.3, ok); cap top 23.480 (exp 23.7 ±0.5, ok); barb top 28.483
  (exp 28.5 ±0.6, ok).

## 7. Rebuild strategy summary
Sub-bodies unioned into one solid, each a revolve about its **own measured axis**: nozzle (+ lug
rounded-rectangle prism, latch-window cut, blind bore to the observed depth), nut (drafted revolve +
8 rib rods at 45° pitch), band lower / band upper, body, cap part (ring + cap one revolve, 4 window
pockets), outlet (revolve about its axis: tube, collar, O-ring torus, thread as plain cylinder, end
bore), barb (revolve: tube, flare, bulb cone with measured offset, end bore). Plan: `build/MODELING_PLAN.md`.

## 8. Risk flags and operator declarations
- R1 Assembly misalignment is modelled as scanned (per-part axes). If the owner wants a nominal
  (coaxial, square) valve instead, that is a different deliverable and would miss the band at the cap
  (3.36° × r 12 ≈ 0.7 mm).
- R2 Unseen interior (E24) and bore depths (E02, E15, E20): modelled only to the observed depth.
- R3 O-ring: a separate part fused into the single solid (invented connection).
- R4 Thread: scanned depth only ≈ 0.37 mm peak-to-peak; modelled as a plain cylinder.
- R5 Scale unverified (no calipers); scan_resolution recorded as full by agent inference (DECISIONS.md OTHER).
- R6 Datum STOP margins are small: nozzle circle 0.0313 vs circle noise 0.0325; different flats read
  0.027–0.046, so the noise floor itself spreads by ~0.02 (OD-H22 D1 class).

## 9. Measurement request → `intake/MEASUREMENTS.md`
Scan-only job (DECISIONS.md MEASUREMENTS): the request lists the caliper-coverable dims with their
scan-predicted values for a future re-run; all rows are ABSENT, not passed.

## 10. Addendum (measure / build feedback, it1) — CHK-ENUM items found after intake
Added on 2026-09-28 by the builder; §5 above is left as written at intake.
| # | Feature | Seen in mesh (where) | Seen in photo | Status |
|---|---|---|---|---|
| E21 (revised) | two slits under the ring skirt (θ ≈ −160…−127 and 146…173 in the cap frame, up to u ≈ 11.0) into the skirt/body gap | open loops L5, L7; self-check cluster s2c 1.4–1.5 mm | not visible | mesh-only; **now modelled** as sector pockets (measure/params.json `slit_*`) |
| E23 (revised) | the lug cut-back on the phi−90 side is the bridged twin of the phi+90 latch window (lugs cut back to the nozzle cylinder between the corners on both sides) | lip envelope 0.3–0.5 mm inside the lug outline over 72° | photo_2 (slot at the tip) | both; modelled (`latch_*`) |
| E25 (new) | web joining the outlet tube top to the ring bottom (x 10–13, z 8–9) | sections z 8.3–8.5; self-check cluster | photo_1 (outlet root under the ring) | both; modelled (`web_*`) |
CHK-ENUM: these three were missed at intake (found by the builder's self-check residual clusters): recorded as a
**CHK-CLUSTER finding** in measure/params.json, no open item remains.
