# INTAKE CARD — OD-E02_control-button-board (DeLonghi control button board assembly)

Scan: `input/scan.stl` sha256 a0e8b66e15d5b404d69149ba6ea843348d588e2d0f3202a069412341d3b4a12f
(`intake/intake.json#inputs`). Working copy: `intake/work.stl` (586,137 → 300,000 faces, seeded
quadric decimation; work-vs-full p95 0.0046 / max 0.0271 mm, seed 0). Official gates run on the
full-resolution original (owner confirmed full-res, `DECISIONS.md` OTHER 2026-09-28), never on the
working copy.

## 0. Band regime (declared here, named again in the verdict)
Regime: **baseline-skill, material_class plastic** — p95 ≤ 0.30 / max ≤ 0.80 mm
(`baseline/skills/stl2step-build123d/SKILL.md:87`; no source given in that file). Applies to scan→CAD
and to the observable part of CAD→scan (run-contract §12). `intake/regime.json`.
Why this regime: the owner wrote "p95 plastik parça toleransı kullan"; the part is moulded black
plastic; there are no calipers, so RE_SPEC Tier-1 cannot run. `DECISIONS.md` REGIME 2026-09-28.

## 1. What it is (photos + mesh)
Front control button board of a DeLonghi espresso machine, scanned as one assembled body: a stepped
moulded housing with a snap-fitted back cover, a PCB connector shroud on the back, two screw holes
through the housing, a bent mounting tab with a screw hole, snap-latch hoops on the long sides, and
three push-button caps (photo 2, left→right: 1 cup, 2 cups, steam; in the datum frame B1 at −X,
B2 on the origin, B3 at +X — mapping photo-inferred from the tab/bump orientation). The button caps
are separate moving parts: B2 sits 1.63° tilted in its bore (`alignment.json` first run, see §6), so
they are loose in the assembly. Material: black thermoplastic (inferred). The deliverable is one
fused solid of the assembly as scanned (single-solid is the supported class; multi-body STEP would be
a separate job, orchestrate §6).

## 2. Scan health (numbers from intake.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | 586,137 / 294,367 |
| Bodies; kept; removed fragments % | 1; all; 0.0 % |
| Scanner table removed % (rule used) | 0.0 % (no table in the scan) |
| Watertight; open boundary edges / loops | no; 2,691 / 23 |
| Normal orientation (method, verdict, flipped?) | seeded ray vote (500 samples): outward, not flipped |
| bbox raw; bbox datum | raw 71.41 × 72.28 × 44.05; datum 77.02 × 54.09 × 48.23 (x −38.72..38.31, y −37.84..16.25, z −29.25..18.98) |
| Units verdict (CHK-SCALE) | FLAG: no calipers, units assumed mm, scale unverified, none applied |
| Noise floor (value, method, region) | plane 0.0265 mm (RANSAC+SVD on the mounting-tab top face, `noise_primary.json`); circle 0.0294 mm (median IRLS over the origin collar stations, self-referential, `noise_circle.json`) |
| Artefact zones | connector interior (pins, unscanned), narrow gaps between button caps and their collars, the screw-hole bores, the slot between the connector shroud and the rim wall |

## 3. Coverage / occlusion map (datum frame; `intake/coverage.json`, 23 open loops)
| Zone | r | z | θ | Note |
|---|---|---|---|---|
| connector shroud interior | 1.1–23.6 | −2.8..5.7 | 18..177° | pins and inner floor not scanned; open |
| shroud-to-rim slot (inside the rim pocket) | 11.7–26.0 | 0..5 | 67..163° | narrow slot, open |
| gaps around B1/B3 collars | 19–34 | −19.4..−14.8 | several | button-to-collar clearance, open |
| screw-hole bores (front side) | 11.9–18.5 | −14.9..−11.7 | −161°, −44° | bore interior partly open |
| gap under −Y latch hoops | 13–19 | −6.2..−1.8 | −156°, −38° | hoop windows |
Not a turned part, so θ-coverage per radial band is not meaningful here.

## 4. Functional surfaces & interfaces (gate zones)
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| Z1 | back cover floor (primary) | board plane, datum | depth gauge | regime |
| Z2 | housing outer tiers (T0 rim .. T4 button band) | fits the machine front panel opening | yes (ENV-X/Y) | regime |
| Z3 | button caps B1–B3 and collars | pass through the front panel; user interface | yes | regime |
| Z4 | mounting tab + Ø hole | screw mount to the chassis | yes | regime |
| Z5 | screw holes ×2 | screw mount | pin gauge | regime |
| Z6 | connector shroud | mates the cable connector | yes | regime |

## 5. Feature enumeration — interior included (CHK-ENUM)
| # | Feature | Seen in mesh (where) | Seen in photo (id) | Status |
|---|---|---|---|---|
| E01 | Back cover floor, flat, z = 0 | whole back inside the rim | photo 1 left | both |
| E02 | Rim wall around the back floor, z 0..4.98, ~1.3 thick, with a raised bump on +Y (x −25..16) | sections z 2..4.5 | photo 1 left | both |
| E03 | Stepped housing tiers below the rim: bottoms at z −5.58, −7.58, −10.13, −13.18, −16.13 | flat-face histogram, sections | photo 1 right, photo 2 | both |
| E04 | 45° chamfer face on the −Y side between z −10.1 and −16.1 | YZ sections x −20..5 | photo 2 (sloped face under the tab) | both |
| E05 | Button band (z −13.2..−16.1): bar + round bosses around the three buttons + notches at the screw holes | section z −14.5 | photo 2 | both |
| E06 | Collars around the buttons (z −16.1..−19.1): B2 r 8.19; B1/B3 about r 8.3 | sections z −16.5..−19 | photo 2 | both |
| E07 | Button cap B2 (2 cups): cylinder r ≈ 6.37, flat top z ≈ −29.15, tilted 1.6° in its bore | sections z −20..−29 | photo 2 middle | both |
| E08 | Button caps B1 (1 cup, −X) and B3 (steam, +X): cylinders r ≈ 6.1–6.2 with inclined top faces (lower toward the middle) | XZ section y = 0 | photo 2 left/right (tops visibly slanted in photo 1 right) | both |
| E09 | Two screw holes through the housing at (±13, −8): back counterbore r ≈ 3.8 to z −2.88, bore through, front notch r ≈ 3.3 in the button band | sections z −1..−15 | photo 1 left (back), photo 2 (front holes) | both (bore interior partly occluded) |
| E10 | Connector shroud: rectangular tube x ≈ −22..5, y ≈ 1..11, z 0..10.48, wall ≈ 1 | sections y 0..3, z 4.5 | photo 1 left (white header with pins) | both; interior pins/floor occluded |
| E11 | Mounting tab: 2.55 thick plate, vertical from the −Y wall, 45° incline, horizontal flange at z 16.4..18.9 with a hole r ≈ 1.2, plus two side flanges x ≈ ±15.5 | YZ sections x 0/5, XZ y −19.5/−25 | photo 1 left/right | both |
| E12 | Snap-latch hoops on the housing sides (−Y: x ≈ ±20..29; +Y bump top x ≈ −21..−11; +Y right x ≈ 20..30) | sections z −4.5..4.5, XZ y −19.5 | photo 1 right, photo 2 | both |
| E13 | Embossed recycling logo and "1" on the back floor; icons on the button tops | back render | photo 1 left, photo 2 | both; cosmetic, not modelled (declared) |
| E14 | Small edge blends between tiers (≈ 0.3–0.5) | sections | photos | both; declared simplification |
| E15 | Inner latch bosses inside the rim behind hoops H1, H2, H4 (z 0..3.48, 1.2 mm proud of the rim inner wall) | sections z 0.5..3.2 | photo 1 left (thick rim at the latches) | both — **added by the builder self-check (CHK-ENUM finding at intake)** |
| E16 | Catch ramps flooring the four hoop windows (20–54° planes) | hoop window faces | photo 1 right | both — added by the self-check |
| E17 | Clearance recesses between each cap and its collar (r ≈ 7.3–7.6, 1–4 mm deep) | r-z maps about each cap | photo 2 (dark ring round each cap) | both — added by the self-check |
| E18 | Side collars cut on the outer side by a ~27° plane with a flat floor at z ≈ −15 | ring lower-boundary map | photo 1 right | both — re-measured by the self-check |
CHK-ENUM result: both photos checked (1 = back + 3/4 front, 2 = front); the highest material is the
tab (z 18.98), nothing stands above it; on-axis material below the origin is the B2 cap (E07). No
unexplained cluster. Photo-only items: none. Mesh-only items: none.

## 6. Datum plan and result (`intake/alignment.json`, status OK)
- Primary (levels): back cover floor → XY @ z = 0, material on −z (the housing hangs below).
  WHY: board plane; buttons, screw holes and connector are normal to it. Trimmed fit rms 0.0218 /
  max 0.0997 mm over 14,256 faces (1,291 mm²); untrimmed rms 0.0259 / max 0.1725.
- Secondary / origin XY: middle button collar (housing boss around B2), 9 Kåsa stations z −18.7..−16.4,
  median rms 0.0294 / worst 0.0954; r 8.19. WHY: housing feature that guides B2; the part is laid out
  about it. The loose B2 cap was tried first and not used (rms 0.03–0.08, tilted in its bore).
- Clock: rule plane_normal, the +X end face of the housing → +X, angle 111.49°; plane rms 0.0273,
  the face is 1.61° out of perpendicular (moulding draft). WHY: the three buttons lie along X.
- Origin: middle button collar axis ∩ back cover floor plane.
- Tilt (CHK-TILT): 1.76 ± 0.46° over a 2.3 mm span (collar, 1 feature) → finding (short span, stderr
  large). The first datum run on the B2 cap gave 1.63 ± 0.10° over 4.3 mm (the cap's own tilt in its
  bore). Decision for measure/rebuild: the back floor is functional; housing features are modelled
  normal to it; the B2 cap tilt is measured and reported, not silently re-levelled.
- Sanity landmarks: primary at z = 0 (obs −0.0010, ok); tab top zmax 18.95 exp / 18.98 obs, ok;
  B2 top centre median −29.10 exp / −29.15 obs, ok.
- Status: OK.
- Noise note (finding): the single-station collar circle noise (0.0266) and the 9-station median
  (0.0294) tie within estimator precision (skill defect D1 in `evals/real-runs/OD-H22.md`). The
  secondary noise reference is therefore the self-referential 9-station median; independent clean
  circles on this scan read 0.0105–0.0393 (screw holes, B2 cap), so the collar is not warped.
- Frame note for measure: the housing long walls read −0.33..−0.60° in this frame while the end walls
  read +0.06..+0.32° (moulding draft / slight skew). Measure should record a housing yaw parameter
  rather than re-clock the datum.

## 7. Rebuild strategy summary
Plan-view sketch + extrude per tier (the tiers are concentric offsets of one core outline: corner
centres are constant across tiers, only the radii change), a cut pocket for the rim, 45° half-space
cut for the −Y chamfer, sub-bodies for the button band bosses, collars, button caps (B1/B3 with
inclined top cuts), connector shroud, mounting tab (profile extrude in YZ + side flanges) and latch
hoops, then cut tools for the screw holes, shroud interior and tab hole. Ordered plan:
`build/MODELING_PLAN.md`.

## 8. Risk flags and operator declarations
- Loose button caps: modelled at their measured scan pose (assembly as scanned), not an ideal pose.
- Connector interior (pins, header) not scanned: shroud interior depth is assumed.
- Screw-hole bore diameter below the counterbore partly occluded.
- Scan-only: absolute scale unverified; Tier-1 not run.
- Question for the operator (non-blocking): is a separate STEP per sub-part (housing, cover, caps)
  wanted later? This run delivers one fused solid.

## 9. Measurement request → `intake/MEASUREMENTS.md`
Written with scan-predicted values; the owner supplied no calipers (`DECISIONS.md` MEASUREMENTS), so
every row is ABSENT, not passed.
