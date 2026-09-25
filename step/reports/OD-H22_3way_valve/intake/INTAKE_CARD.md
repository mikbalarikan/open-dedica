# INTAKE CARD — OD-H22_3-way-valve (DeLonghi coffee-machine 3-way valve, moulded black plastic)

Scan: `input/scan.stl` sha256 4ebbb8c4369a8bbcddad7c7dbc57a37a725f605bc266af7697b08c1e63189f92.
Working copy: `intake/work.stl` (495,881 → 250,000 faces, work-vs-full p95 0.0028 / max 0.098 mm,
seed 0; `intake/intake.json#decimation`). Official gates run on the full-resolution original,
never on the working copy. All measure-stage numbers were taken on the full-res scan.

`scan_resolution` = **unknown** (`input/INPUT_HASHES.json`): the user did not state it. Evidence
for full-res: 495,881 faces, one body, mean edge 0.154 mm, 24.8 MB. Orchestrator must confirm
before verify grades (orchestrate §6 row `scan_resolution`).

## 0. Band regime (declared here, named again in the verdict)
Regime: **baseline-skill, material_class plastic: p95 ≤ 0.30 / max ≤ 0.80 mm**
(`baseline/skills/stl2step-build123d/SKILL.md:87`; `intake/regime.json`).
Why: scan-only run (no calipers; `DECISIONS.md` MEASUREMENTS), moulded plastic part, user wrote
"tolerans = p95". Orchestrator default, confirmed by Ikbal via decision card 2026-09-25 10:54
("Plastic 0.30"), declared before any gate numbers (`DECISIONS.md` REGIME ×2).

## 1. What it is (photos + mesh)
A 3-way water valve body. A flange plate with two screw ears (holes Ø≈3.9) mounts it; on the
tray side a boss collar carries a crenellated drive tube (4 slots) that takes the valve
knob/rotor spline; on the back side a stem drops to a symmetric Y-junction with two angled
ports. Each port ends in a square clip block with two through-slots for a U-shaped hose
retaining clip, then a round lip and a bore. Static moulded part (inferred: black thermoplastic,
ejector-pin marks visible on the port sleeves). photo_1..3 are seller catalogue images
(photo_2 watermarked "Ellis Electrical"); photo_4 is a real photo. No scale reference.

## 2. Scan health (numbers from intake.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | 495,881 / 249,510 |
| Bodies; kept; removed fragments % | 1; largest; 0.0 % |
| Scanner table removed % | 0.0 (none present) |
| Watertight; open boundary edges / loops | no; 3,255 / 28 |
| Normal orientation | ray vote on working copy (open mesh), outward (0.226 vs 0.97), not flipped |
| bbox raw; bbox datum | raw extents 40.00 × 42.01 × 48.09; datum extents 42.56 × 39.90 × 44.81 (x −21.12..21.44, y −19.80..20.10, z −30.84..13.98) |
| Units verdict (CHK-SCALE) | FLAG: no calipers, 0 ENV dims < 3 → units assumed mm, scale unverified, none applied |
| Noise floor | plane: 0.0357 mm rms (RANSAC+SVD, flange back face = the primary itself, see §6); tray floor gave 0.0355 (`intake/noise_tray_floor.json`); circle: 0.0767 mm rms (IRLS, drive-tube OD z=7.2, `intake/noise_circle.json`) |
| Artefact zones | +X ear tip damaged/torn (jagged outline x>20.4, visible in renders); scan holes inside the drive-tube bore below z≈1.5 and inside the port bores deeper than t≈13–16 (unscanned interior); small open loops at the junction underside |

## 3. Coverage / occlusion map (datum frame; `intake/coverage.json`)
| Zone | r | z | θ | Note |
|---|---|---|---|---|
| Drive-tube bore bottom | 4.19–4.69 | 1.9–6.9 | 354° | bore wall open below z≈1.5: bore floor / internal web NOT scanned |
| Port underside / clip slots | 10.6–17.9 | −28.8..−18.5 | 6–34° spans | slot interiors and port bore beyond t≈13 (pY) / 16 (nY) not seen |
| Stem / gusset roots | 6.4–9.9 | −4.0..0 | 113° | small holes at gusset root |
| Plate back edge | 9.4–13.1 | −0.1..0.7 | 17–61° | small holes on the back-edge round |
Angular coverage per radial band (coverage.json#radial_bands): 360° for r < 13 mm; 230°/186°/158°/96°
for the bands 13–21.6 mm — expected, those radii are the ears and ports (not a round feature),
so partial θ there is geometry, not missing scan.

## 4. Functional surfaces & interfaces (each becomes a gate zone)
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| Z1 | flange back face + screw-ear holes | mounting seat, screws | yes (thickness, hole Ø, hole pitch) | regime |
| Z2 | drive tube OD/bore + 4 slots | knob/rotor drive interface | yes (OD, bore, slot widths) | regime |
| Z3 | port bores, lips, clip blocks + slots | hose connection + retaining clip | yes (bore Ø, lip Ø, block across flats) | regime |
| Z4 | stem, junction, gussets, tray rim | structural / cosmetic | partly | regime |

## 5. Feature enumeration — interior included (CHK-ENUM)
| # | Feature | Seen in mesh (where) | Seen in photo (id) | Status |
|---|---|---|---|---|
| E01 | Flange plate, central disc + 2 ears, back face flat | z 0..2.26 | 1,2,3,4 | both |
| E02 | Back-edge round of the plate | outline inset vs z, z<1.9 | 4 | both |
| E03 | Tray rim wall (lip) around the whole outline, top z≈5.63 | tray side | 1,2,3 | both |
| E04 | Ear screw holes ×2 | (±15.39, 0) | 1,2,3,4 | both |
| E05 | Boss collar Ø16.1, top z 4.74 | tray side | 1,3 | both |
| E06 | Drive tube Ø12.4, bore Ø9.1, top z 13.7, 4 slots | z 4.7..13.98 | 1,2,3 | both |
| E07 | Tube-bore floor / internal web | NOT in mesh (open loop) | 1–3 show fingers only | occluded → assumed |
| E08 | Stem: Ø13.1 cylinder, 40° cone, Ø8.15 neck | z 0..−12 | 1,2,3,4 | both |
| E09 | Two triangular gussets stem→plate in the XZ plane | y≈0, x ±4..11 | 1,4 | both |
| E10 | Y-junction, two ports ~34–35° below horizontal in the YZ plane | z −12..−31 | 1,2,3,4 | both |
| E11 | Port neck Ø8.3 → sleeve Ø11.2 step | t≈7 | 4 | both |
| E12 | Square clip block with 2 through-slots per port (U-clip) | t≈15–19 | 1,2,3,4 | both |
| E13 | Round lip + bore at the port mouth | t≈19–20 | 1,2,3,4 | both |
| E14 | Bottom rib (web) under the junction, flat bottom z≈−23.7 | x≈0, |y|<4 | 4 (crotch) | both |
| E15 | Ejector-pin circles (shallow) on port sleeves | sleeve sides | 3,4 | both → cosmetic, not modelled |
| E16 | Internal flow passages (bores to junction) | NOT in mesh | not visible | occluded → not modelled |
CHK-ENUM result: every photo checked (1–4). On-axis material above the tube top: none (zmax 13.98 =
tube top; radial band r<2.2 lives only at z −23.7..−19.5, i.e. the bottom rib). No unexplained
cluster. **pass** (E07, E16 are declared occlusions, not open items).

## 6. Datum plan and result (`intake/alignment.json`, status **OK**)
- Primary: flange plate back face (stem side) → XY @ z=0, +Z towards the tray/drive tube
  (`material_side +z`). WHY: mounting flange seating face clamped by the two ear screws; the
  largest clean moulded flat. Fit rms 0.0357 / max 0.1086 mm (trimmed, 8,304 faces, 261 mm²);
  untrimmed rms 0.0508 / max 0.202.
- STOP-rule note: the first pass used the tray floor as the independent plane noise reference
  (0.0355) and STOPPED on 0.0357 > 0.0355. Across RANSAC seeds 0–7 the two trimmed rms values
  span 0.0344–0.0361 (primary) and 0.0354–0.0373 (tray): a tie within estimator precision, not a
  warped primary (band means within ±0.006 mm). Re-run with the noise measured on the primary
  itself (the skill's self-referential path, Step 3); align.py records the finding. Logged as a
  skill defect in BUILDER_REPORT.md.
- Secondary: valve axis = median centre of 17 Kåsa section circles over 3 coaxial features
  (boss collar r 8.05, drive tube r 6.21, stem neck r 4.08). WHY: rotor/drive axis ⟂ flange.
  Median circle rms 0.0694 / worst 0.230 mm vs circle noise 0.0767.
- Clock: fourier_mass n=2 on ear vertex mass (r 12.5–22, z 0.2–5.8), −84.99° → ears on ±X.
  Label rule: ear nearest +90° in the pre-clock frame → +X (mirror-symmetric part, convention).
- Origin: valve axis ∩ flange back-face plane.
- Tilt (CHK-TILT, finding): pooled 0.470° ± 0.014° over 18.2 mm; per feature 0.485° (collar,
  ±0.58), 0.564° (tube, ±0.23), 0.525° (neck, ±0.14); directions disagree → **not resolvable**
  (heuristic). All three read ≈0.5°, above the 0.3° reference (report-only). Decision: the
  flange face is the functional primary; the axis is modelled ⟂ to it (design intent); the
  ≈0.5° / ≈0.1–0.17 mm lateral offset of the lower body is a declared simplification.
- Sanity landmarks: primary z 0.004 ✓, tray floor 2.245 (exp 2.25) ✓, top 13.979 (exp 14.0) ✓,
  bottom −30.835 (exp −30.8) ✓.

## 7. Rebuild strategy summary
Plate: one XY sketch (disc ∪ tapered ears, concave blends) extruded, tray pocketed by an inward
offset; revolve the axisymmetric core (collar, tube, stem, cone, neck); slots as 4 cut tools;
gussets as one mirrored extruded triangle; each port as a revolve about its own measured axis
plus a square block, slot and bore cut tools; rib as a box. Ports placed at their measured
per-port angles (not forced symmetric). Plan: `build/MODELING_PLAN.md`.

## 8. Risk flags and operator declarations
- No calipers: absolute scale unverified; Tier-1 not run.
- Unscanned interior (tube-bore floor, port bores beyond t≈13–16, flow passages) is assumed.
- +X ear tip damaged on this specimen; the model follows the undamaged −X ear by symmetry.
- Tilt ≈0.5° between flange normal and the axis features: warp vs design unknown (question for operator).
- scan_resolution unknown (see header).

## 9. Measurement request → `intake/MEASUREMENTS.md`
