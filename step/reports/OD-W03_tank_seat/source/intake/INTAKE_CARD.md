# INTAKE CARD — OD-W03 water tank valve (DeLonghi-type tank valve cover)

Scan: `input/scan.stl` sha256 4784d93dafd0e5ba815368c89572b92c2ba1af17b054725a6503b4c1fa59e1fb.
Working copy: `intake/work.stl` (400,657 → 400,657 faces, no decimation, nothing removed).
Official gates run on the full-resolution original (owner confirmed full-res, DECISIONS.md 2026-09-28).

## 0. Band regime
Regime: **baseline-skill, material_class plastic** — p95 ≤ 0.30 / max ≤ 0.80 mm
(`baseline/skills/stl2step-build123d/SKILL.md:87`), written to `intake/regime.json`.
Why: owner instruction "p95 plastik parça toleransı kullan"; scan-only (no calipers, DECISIONS.md
MEASUREMENTS), so RE_SPEC Tier-1 cannot run. Declared before any gate numbers.

## 1. What it is
Translucent moulded plastic valve cover for a water tank (photo `input/photos/OD-W03_photo1.png`).
A stadium flange plate with a short skirt carries two valve cups (each topped by a conical shoulder
and a single-barb hose nipple with a through bore), a small middle boss with a top hole, 2 mm webs
tying cup–boss–cup and cup–ear together, and an L-shaped ear at each end (vertical tab + horizontal
lug with a screw/locating hole). Static part; seats on the tank on its (unscanned) underside.
Material/process inferred (translucent PP/POM-like, injection moulded).

## 2. Scan health (intake.json, alignment.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | 400,657 / 202,383 |
| Bodies; kept; removed fragments % | 1; 1; 0.0 % |
| Scanner table removed % | 0.0 % (no table in the scan) |
| Watertight; open boundary edges / loops | no; 4,171 / 25 |
| Normal orientation | ray vote (open mesh), verdict outward, not flipped |
| bbox raw | extents 65.91 × 63.98 × 42.50 (arbitrary scanner frame) |
| bbox datum | extents 85.09 × 30.55 × 31.80; x −42.44..42.66, y −15.59..14.97, z −3.17..28.64 |
| Units verdict (CHK-SCALE) | FLAG: no calipers; units assumed mm, scale unverified, no scale applied |
| Noise floor | plane 0.0409 mm (flange top, primary itself: self-referential); circle 0.0708 mm (barb A shank z=16, independent); circle 0.0829 mm used for the secondary STOP check (cup walls themselves: self-referential, `intake/noise_cups.json`) |
| Artefact zones | ±0.15 mm ripple on cup walls above z≈3 (translucent material); bridging "membrane" inside the barb tips; ragged skirt lower edge (scan stops at z −2.0..−3.17); junk facets where the tab inner face meets the lug underside (x≈±33, z 12.5–14.5) |

## 3. Coverage / occlusion map (datum frame; `intake/coverage.json`)
| Zone | Where | Note |
|---|---|---|
| Underside of flange, skirt inner face | z < −0.3 inside the skirt | **not scanned at all** — one 358° open loop along the skirt lower edge (r 14–42) |
| Cup and boss interiors | inside r < 11 / r < 6 | not scanned (outer skin only) |
| Barb bores | r ≈ 1.2 at z 27.7–28.6 | opening only (loops at both barb tips) |
| Boss top hole | r ≈ 2.08, z 11.0–11.8 | opening + ~1 mm of wall |
| Lug holes | r ≈ 2.1 about x ±38.5 | wall partly seen |
| Slots cup↔tab, cup↔boss beside the webs | 1.3–1.5 mm gaps | web side faces seen only above z≈6 near the tabs |
| Tab inner faces / lug undersides | x ±32.6, z 12–13 | partly occluded |
| Flange front edge | y ≈ −14.8, x −2..5 | small scan hole on the top edge |
Angular coverage of the round features is complete above the flange (outer skin).

## 4. Functional surfaces & interfaces
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| Z1 | flange top + skirt outline | seats / locates the cover on the tank | yes (ENV-X/Y) | baseline-skill has no interface band → reported |
| Z2 | barb nipples A/B (shank, lip, tip) | hose connections | yes (lip Ø, shank Ø) | reported |
| Z3 | ear lugs + holes | screw / peg fixing | yes (hole Ø, pitch) | reported |
| Z4 | cup outer walls | valve housings (seal/cap fit) | yes | reported |

## 5. Feature enumeration (CHK-ENUM)
| # | Feature | Seen in mesh | Seen in photo | Status |
|---|---|---|---|---|
| E01 | stadium flange plate, top at z=0 | yes | yes | both |
| E02 | skirt below the flange edge | yes (to z≈−3.1) | yes (edge) | both |
| E03 | cup A / cup B (step at z≈7, rounded top edge) | yes | yes | both |
| E04 | conical shoulders cups → barbs | yes | yes | both |
| E05 | barb nipples: shank, 28° flare, lip, 7° tip taper | yes | yes | both |
| E06 | barb bores (through into the cup, inferred) | tip opening only | yes (dark tip) | occluded → assumed depth |
| E07 | middle boss with top hole | yes | yes | both |
| E08 | webs cup↔boss (×2), cup↔tab (×2), 1.9 mm wide, full height | yes (tops, upper sides) | yes | both |
| E09 | ear tabs (vertical, tapered sides) ×2 | yes | yes | both |
| E10 | ear lugs with holes ×2 | yes | yes | both |
| E11 | parting-line ridge along y=0 over the cup shoulders | faint | no | cosmetic, not modelled |
| E12 | interior walls / valve seats / underside | no | no | occluded → hollow shell, assumed 1.2 mm walls (owner decision) |
CHK-ENUM result: the single photo checked; material above the cups = barbs only (coverage radial bands);
no unexplained cluster. **pass** (E11 cosmetic, E06/E12 declared assumed).

## 6. Datum plan and result (`intake/alignment.json`)
- Primary: flange top face → XY @ z = 0, material below (−z). WHY: largest clean moulded flat, parallel to the
  unscanned seat; every feature rises from it. Fit rms 0.0409 / max 0.1026 (23,812 faces).
- Secondary / origin XY: cup A and cup B outer-wall axes (wall-face IRLS, z 1.2–3.6, 3 stations each);
  origin = midpoint of the two axes (`combine: midpoint`). Median circle rms 0.0829 / worst 0.656.
  Cup-axis separation 38.970 mm.
- Clock: `feature_line` cup A axis → cup B axis along +X, rotation 119.762°.
- Origin: midpoint of cup A/B axes ∩ flange top face.
- Tilt (CHK-TILT): 0.27° ± 0.31° over a 1.6 mm span (6 stations) — within its own stderr, i.e. not
  resolvable at this span; longer spans (z 2–7.4, rougher wall) gave 0.26°, not resolvable. Report-only.
- Sanity landmarks: primary at z=0 (0.001 ok); cup A top face 12.329 (exp 12.4 ±0.3, ok); barb tip
  28.638 (exp 28.5 ±0.4, ok); skirt lower edge −3.167 (exp −3.1 ±0.4, ok).
- Status: **OK** — after a first STOP (secondary rms 0.0815 > independent barb circle noise 0.0708) resolved
  by the self-referential noise path; recorded in DECISIONS.md (OTHER) and as a finding.

## 7. Rebuild strategy summary
Mirror-symmetric about YZ (cup A/B, ears) with measured per-side values where they differ beyond noise.
Revolve cups+shoulder+barb profile; revolve boss; extrude stadium flange + skirt; extruded webs; tab as a
tapered prism (loft of two rectangles, analytic planes); lug as slot extrude with hole. Hollow shell:
cup/boss interiors and flange underside cut with assumed 1.2 mm wall; barb bore through.

## 8. Risk flags and operator declarations
- Interior geometry is invented (owner chose hollow shell, 1.2 mm walls): CAD→scan observable will count
  the unscanned underside/interiors (OD-H22 defect 3); expect verify to report it.
- Absolute scale unverified (no calipers).
- Lug thickness / underside and tab inner face only partly seen.
- Cup walls carry scanner ripple ±0.15 mm; p95 budget is tight on them.

## 9. Measurement request → `intake/MEASUREMENTS.md`
Written for a later caliper pass (scan-only now; any reading is a re-run trigger).
