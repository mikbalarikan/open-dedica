# INTAKE CARD — OD-S03_steam-knob (DeLonghi-style steam knob)

Scan: `input/scan.stl` sha256 `ce4a9dfcb0acf91a9e1632f0f67c2317ab6890ab8d86e2edcf0c958957fb0dfd`
(`intake/intake.json#inputs`). Working copy: `intake/work.stl` (363,988 → 363,988 faces, **no
decimation**, `intake.json#decimation.applied = false`; seed 0). The working copy IS the
full-resolution mesh (only welded), so work-vs-full deviation is 0 by construction.
Official gates run on the full-resolution original (`scan_resolution: full`, DECISIONS.md OTHER,
orchestrator inference).

## 0. Band regime (declared here, named again in the verdict)
Regime: **baseline-skill, material_class plastic** — p95 ≤ 0.30 / max ≤ 0.80 mm
(`baseline/skills/stl2step-build123d/SKILL.md:87`; `intake/regime.json`).
Why this regime: owner instruction "p95 plastik parça toleransı kullan" (DECISIONS.md REGIME,
2026-09-25, declared before any gate number existed). No calipers (DECISIONS.md MEASUREMENTS:
scan-only), so RE_SPEC Tier-1 cannot run. The part is a chrome-plated plastic cap on a plastic
stem with a chrome threaded sleeve: consumer plastic class.

## 1. What it is (photos + mesh)
Espresso-machine steam-valve knob (photos 1–5). A chrome cap (closed crown, 3° drafted wall)
with one radial lever wing; a stepped chrome ring/collar at the open end; a white plastic stem
with four radial ribs coming out of the collar; a plain neck; a chrome externally-ribbed
(threaded) sleeve at the end with a bore (photo 5 shows a white splined bore inside). The knob
turns the valve spindle: the sleeve/bore and the stem are the functional interface; the cap and
lever are the hand interface. Moving part (rotary). Material/process: moulded plastic, chrome
plated cap and sleeve (inferred from photos). Physically an assembly of ≥3 parts (cap, stem,
sleeve); the scan is one body and the deliverable is ONE fused solid (multi-body out of scope,
task brief).

## 2. Scan health (numbers from intake.json / alignment.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | 363,988 / 182,580 |
| Bodies; kept; removed fragments % | 1 body; kept largest; 0.0 % |
| Scanner table removed % (rule used) | 0.0 % (no table in the scan) |
| Watertight; open boundary edges / loops | false; 1,202 edges / 17 loops (scan holes, see §3) |
| Normal orientation (method, verdict, flipped?) | ray vote on the open mesh (500 samples, seed 0): outward, not flipped |
| bbox raw; bbox datum | raw extents 31.34 × 39.21 × 37.43; datum extents 40.93 × 26.49 × 38.16 (X −13.17..27.76, Y −13.37..13.12, Z −0.056..38.10) |
| Units verdict (CHK-SCALE) | **FLAG**: no calipers, no scale reference in the photos; units assumed mm, scale unverified |
| Noise floor (value, method, region) | plane 0.0187 mm rms (RANSAC+SVD, lever −Y flank, 12,006 faces, `noise_primary.json`); circle 0.0436 mm rms (IRLS circle, cap-mouth ring section z = 14.0, `noise_secondary.json`) |
| Artefact zones | 17 open-boundary holes on the chrome surfaces (reflectivity), the largest on the +Y lever-root/cap wall (r 11–25.7, z 0.4–4.6, θ 12°–95°); lever-pocket bottom unscanned; annular crevice between collar and stem (z ≈ 15–17) partly unscanned; sleeve bore unscanned below z ≈ 34.3–35.8 |

## 3. Coverage / occlusion map (datum frame; from `intake/coverage.json`)
| Zone | r | z | θ | Note |
|---|---|---|---|---|
| hole A (largest) | 11.19–25.66 | 0.41–4.61 | 11.8° → +83.4° | cap wall / +Y lever root near the crown: missing skin, not a feature |
| hole B | 10.65–12.84 | 1.01–10.85 | 100.7° → +41.0° | cap wall: missing skin |
| lever pocket bottom | 13.49–21.98 | 8.42–12.44 | −1.9° → +12.7° | pocket floor not reached by the scanner (floor depth unobserved) |
| stem/collar crevice | 5.46–10.64 | 14.94–17.11 | several loops | deep annular gap between stem base and collar: floor unobserved |
| sleeve bore | 2.82–4.00 | 34.31–35.80 | 350.9° span | bore interior below this is unscanned (floor/splines unobserved) |
| neck | 4.71–5.01 | 29.81–32.26 | 177.5° → +8.7° | small skin hole |
Angular coverage per radial band: r 0–13.9 mm: 355–360°; r > 13.9 mm is the lever only
(22°–50°, expected: the lever is the only material there). No partial angular coverage of a
round feature beyond the listed holes.

## 4. Functional surfaces & interfaces (each becomes a gate zone)
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| Z1 | threaded sleeve OD / ripple, z 32.3–38.1 | screws/locates on the valve side | yes (OD over crests) | regime p95/max |
| Z2 | sleeve bore r ≈ 4.0 (visible to z ≈ 35.5) | receives the valve spindle | inside jaws, shallow | regime |
| Z3 | stem ribs + core, z 16.5–29 | rotational drive / guide in the panel | yes (across ribs, across core) | regime |
| Z4 | crown + cap wall + lever | hand interface, cosmetic | yes | regime |
| Z5 | step face z ≈ 13.7, collar r ≈ 11.1 | seats against the machine panel (inferred) | yes | regime |

## 5. Feature enumeration — interior included (CHK-ENUM)
| # | Feature | Seen in mesh (where) | Seen in photo (id) | Status |
|---|---|---|---|---|
| E01 | crown face (flat, closed cap end, coplanar with lever top) | z = 0 plane, 45,575 faces | 2, 3, 5 | both |
| E02 | crown edge round (cap + lever) | r ≈ 10.5 → 12.7, z 0 → 2.3 | 1, 3, 5 | both |
| E03 | cap wall, drafted (≈3°) | r 12.7 → 13.3, z 2.3 → 13.3 | 1, 2, 4, 5 | both |
| E04 | lever wing, radial at +X, drafted flanks, round tip | x to 27.8, width ≈ 9.7, z 0 → 13.7 | 1–5 | both |
| E05 | concave blends lever flank ↔ cap wall | plan view x ≈ 8–13 | 2, 4, 5 | both |
| E06 | lever pocket (blind slot open toward +Z, on the step-face side) | x 13.3–22, y ±2.3, from z 13.7 down (floor unscanned) | 2, 4, 5 | both (floor occluded → provenance tag) |
| E07 | step face (cap open-end face + lever underside) | z ≈ 13.7, r 12.2 → 13.3 and lever | 1, 4, 5 | both |
| E08 | outer edge round at the step face | r 13.3, z 13.2 → 13.7 | 4, 5 | both |
| E09 | mouth bead/ring (step face → collar) | r 12.4 → 11.3, z 13.7 → 14.3 | 4, 5 (first chrome ring) | both |
| E10 | collar cylinder | r ≈ 11.1, z 14.3 → 16.4 | 1, 4, 5 (second chrome ring) | both |
| E11 | collar bottom face with an annular groove | z ≈ 16.6, groove r ≈ 9.3, bottom z ≈ 16.15 | 5 (ring detail) | both |
| E12 | annular crevice between collar ring and stem base | r ≈ 6.1–7.0, deeper than z 15.85 | 4, 5 (dark gap) | both (floor occluded) |
| E13 | stem core (white), slightly drafted, non-round | r ≈ 5.0–5.3, z 16.5 → 28.5 | 1, 3, 4, 5 | both |
| E14 | 4 radial stem ribs at ≈ 0°/90°/180°/270° | r to ≈ 6.4 → 6.0 (tapered) | 1, 3 (vertical lines), 4 | both |
| E15 | stem-to-neck shoulder / bead | z ≈ 28.4–29.7 | 1, 3 | both |
| E16 | neck (white) | r ≈ 4.65–4.9, z 29.5 → 32.3 | 1, 2, 3 | both |
| E17 | chrome threaded sleeve, helical ripple (pitch ≈ 1.2), helical start at the bottom and helical tail at the top | r crest ≈ 5.97, valley ≈ 5.81, z 32.2 → 38.1 | 1–5 | both |
| E18 | sleeve top face | z ≈ 37.2, r 4.25 → 5.5 | 5 | both |
| E19 | sleeve bore + inner shoulder | r ≈ 4.03 from z 37.2 to ≈ 35.6, shoulder toward r ≈ 3.2 at z ≈ 35.1 | 5 (white splined bore) | both; splines deeper are photo-only → occluded, not modelled |
| E20 | small notch in the bore wall at θ ≈ 180° | z 36–37 | not resolvable in photos | mesh-only → investigate in measure |
CHK-ENUM result: every profile photo checked (1, 2, 3, 4, 5). Nothing stands proud above the
sleeve (the +Z extreme 38.10 is the sleeve's helical tail, landmark in alignment.json). On-axis
material: only the crown (r 0–2.8 band z −0.04..0.01, `coverage.json#radial_bands[0]`); the bore
is open. Unexplained clusters: none at intake; E20 goes to measure (CHK-CLUSTER). Photo-only:
the internal bore splines (photo 5) are beyond the scanned bore depth → occluded, declared.

## 6. Datum plan and result (from alignment.json; status **OK**)
- Primary (levels): cap crown face → XY @ z = 0, material +Z (toward the stem/sleeve).
  WHY: largest moulded flat, perpendicular to the turning axis; cap and lever are referenced from
  it. Fit rms / max: 0.01464 / 0.0980 mm (trimmed, 45,575 faces, 320.3 mm²; untrimmed 0.01466 /
  0.1080). Normal cone narrowed to 3° (from the 10° default) so the onset of the crown edge round
  (r > 10, rms 0.032 alone) is not counted as plane: with 10° the fit read 0.0216 > 0.0187 and
  align.py stopped (evidence `intake/alignment_attempt1_STOP.json`; the crown
  r < 10 alone reads 0.0132). Noise reference for the STOP rule: the lever −Y flank (0.0187),
  an independent flat — the check is not self-referential.
- Secondary: axis = median of 25 section-circle centres: 14 Kåsa sections of the sleeve thread
  envelope (z 33.45–36.7, r mean 5.880) + 11 IRLS wall-face slabs on the drafted cap wall
  (z 3.35–12.35, r mean 12.989). Median circle rms 0.0431 / worst 0.3507 mm vs circle noise
  0.0436 (pass). Centre std 0.048 / 0.152 mm.
- Clock: fourier_mass n = 1 on r 16–28.5 (lever only), **area-weighted face centres** (workaround
  wrapper `intake/workaround/align_areaw.py`; align.py's vertex-count phase was biased 3.8° by
  scan vertex density/holes), angle −147.83°. Result: the lever centreline is +X; the two lever
  flank planes read −0.64° and +1.03° about X (bisector +0.2°). WHY: the lever is the only
  non-axisymmetric feature; n = 1, so the label is unique.
- Origin: spigot/cap common axis (median of the section centres) ∩ crown face plane.
- Tilt (CHK-TILT): **finding, not resolvable**. Pooled 1.50° ± 0.045° over 33.35 mm; per
  feature: cap wall 1.46° ± 0.35° (IRLS centre biased by the lever-root faces, which are on one
  side only), thread envelope 2.57° ± 0.64° over only 3.25 mm (helix makes the section centre
  wobble). Neither estimator is trustworthy. Independent diagnostic (builder, not a skill
  script): a free-axis cone fit to the cap wall excluding ±40° around the lever reads 0.13° from
  the crown normal (rms 0.027 mm); the sleeve/neck axis sits ≈ 0.2–0.3 mm laterally from the cap
  axis at z ≈ 30–35. Decision for measure/rebuild: the crown normal is the Z axis; each coaxial
  group (cap, stem+sleeve) gets its measured axis position in the frozen frame (measure step),
  never a re-levelled frame.
- Sanity landmarks: primary plane at z = 0 → −0.0008 (ok); sleeve tip zmax 38.099 vs 38.2 ± 0.5
  (ok); lever tip rmax 27.737 vs 27.7 ± 0.5 (ok); step face (lever underside) z median 13.692 vs
  13.7 ± 0.3 (ok).
- Status: OK. matrix_4x4 in `alignment.json` (raw → datum, rigid, scale 1.0).

## 7. Rebuild strategy summary
- Cap + collar + stem core/neck + sleeve: revolve of (r,z) half-profiles about Z (two coaxial
  groups if measure confirms the lateral offset).
- Lever: plan sketch (flanks + round tip + concave blends) extruded over the cap height, draft
  and crown round per measure; pocket as a separate cut tool.
- Stem ribs: one rib instance + 4 placements at measured angles.
- Sleeve helix: helical ripple and helical ends if build123d gives a valid single solid;
  otherwise a declared simplification with its measured deviation cost.

## 8. Risk flags and operator declarations
- Scale unverified (no calipers, CHK-SCALE FLAG). Re-run trigger: any caliper reading.
- Chrome holes (17 loops) — no skin there, not features.
- Occluded, not invented: lever pocket floor depth, collar/stem crevice floor, bore beyond
  z ≈ 35, internal bore splines (photo 5). Each gets an `assumed`/`photo-inferred` provenance.
- The real object is an assembly (cap, stem, sleeve) fused into one solid by task brief.
- Sleeve construction (thread on a tube vs formed coil) is not decidable from the scan: the
  ripple is only ≈ 0.17 mm deep (scanner smoothing of the true thread form is likely on chrome).
  Question for the operator: thread spec (e.g. M12 × ?) if known.

## 9. Measurement request → `intake/MEASUREMENTS.md`
Written with scan-predicted values; the owner declined calipers (DECISIONS.md MEASUREMENTS), so
every row is ABSENT, not passed.
