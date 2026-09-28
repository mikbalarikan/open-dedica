# INTAKE CARD: OD-S01 steam valve assembly (iteration 2)

Iteration 2 re-ran intake with the same spec (`--route datum` after the it1 REVISE): the same work mesh, matrix and noise
(`_it1_SUPERSEDED/intake/` for comparison). Only the feature enumeration changed (E16–E18).

Scan: `input/scan.stl` sha256 `98cd118312fbb9b43d844cbc063c3be897c553541154b1f5988d5be0c2127ebf`
(24,987,884 bytes). Working copy: `intake/work.stl` (499,756 → 250,000 faces, work-vs-full
p95 0.0049 / max 0.0295 mm, seed 0). Official gates run on the full-resolution original, never on
the working copy.

## 0. Band regime (declared here, named again in the verdict)

Regime: **baseline-skill, material class plastic: p95 ≤ 0.30 / max ≤ 0.80 mm**
(`baseline/skills/stl2step-build123d/SKILL.md:87`; `intake/regime.json`).
Why: the owner wrote "p95 plastik parça toleransı kullan" (use the plastic-part p95 tolerance);
the part is moulded black plastic. No calipers, so RE_SPEC Tier-1 cannot run.
Recorded in `DECISIONS.md` (REGIME, 2026-09-28) before any gate number existed.

## 1. What it is (photos + mesh)

A De'Longhi-type steam valve assembly (`input/photos/1..5.png`, catalogue photos, no scale).
A rotary valve: a splined spindle (knob side) drives a cap disc with a 3-fold cam ring (3 posts,
3 trapezoid snap teeth). The valve column carries a top clip port (square block, 2 clip slots per
side), two side hose ports along −X (Ø11 tubes, Ø8 bores, drafted clip plates, internal orifice
web, U-windows near the column), a hose barb along −Y and a microswitch (2 blade terminals on
top, 1 side tab) held in a bracket/holder on +X. The scan is **one connected mesh of the whole
assembly** (cap, body, switch), so the deliverable is one fused solid. The interior (valve bore,
spool, passages) was not scanned. Material and process: moulded plastic (inferred); the
microswitch and blades are a purchased part (inferred).

## 2. Scan health (numbers from intake.json)

| Item | Value |
|---|---|
| Faces / verts (welded) | 499,756 / 250,308 |
| Bodies; kept; removed fragments % | 1; 1 (largest); 0.0 % |
| Scanner table removed % (rule used) | 0.0 % (no table in the scan) |
| Watertight; open boundary edges / loops | no; 1,058 / 22 |
| Normal orientation (method, verdict, flipped?) | ray vote (500 samples, seed 0), outward (0.246 / 0.988), not flipped |
| bbox raw; bbox datum (from alignment.json) | 47.97 × 47.49 × 54.67 mm; datum extents in `alignment.json#extents_aligned` (z −14.85 … 48.67) |
| Units verdict (CHK-SCALE) | **FLAG**: no calipers and no scale reference. Units assumed mm, scale unverified |
| Noise floor (value, method, region) | 0.0360 mm, rms of RANSAC+SVD plane on the cap disc outer face (3,497 faces); circle noise 0.0479 mm (IRLS circle on the upper column at z 40, `noise_circle.json`) |
| Artefact zones | microswitch label/print relief; ribbed top-port bore; small cap-disc slots only partly scanned; mean edge 0.206 mm |

## 3. Coverage / occlusion map (datum frame; `coverage.json`)

22 open boundary loops. The main ones: the port-web orifices and bore interiors (r 4.6..18.6,
z 30..35 on the upper port; r 9..13, z 17..23 on the lower port), the top-port bore (r 2.9..4.9,
z 42.6..46.7), the column windows (r 9..13, z 8..15), the cap slots (r 9..10.7, z 0..2.1) and the
cam-ring pockets. The inside of the valve column, the spool and the flow passages are not
visible. The column surface just below the switch (θ 0..20°, z 11.5..15) is hidden by the switch
and holder. The cam ring is seen all round (360°).

## 4. Functional surfaces & interfaces (gate zones)

| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| Z1 spindle | splined spindle, D-flat, key | knob drive | yes (OD, flat, key) | regime |
| Z2 cap + cam ring | cap disc Ø28.7, posts/teeth r 12.5..12.7 | rotating cap, detent | yes | regime |
| Z3 top clip port | block 12.7 × 12.4, bore r 4.97, slots | hose clip port | yes | regime |
| Z4 side ports | Ø11 tubes, Ø8 bores, clip plates | hose ports | yes | regime |
| Z5 barb | shaft r 2.70, crest r 3.45 | hose barb | yes | regime |
| Z6 microswitch | box, blades | purchased part | yes | regime |

## 5. Feature enumeration, interior included (CHK-ENUM)

| # | Feature | Seen in mesh (where) | Seen in photo (id) | Status |
|---|---|---|---|---|
| E01 | splined spindle with D-flat and key, tip chamfer, small tip hole | z −14.85..0 | 2, 4 | both (tip hole: mesh-only, r ~0.9, not modelled) |
| E02 | cap disc Ø28.7 with 3 slots and 3 shallow dimples | z 0..2.13 | 2, 4 | both |
| E03 | cam ring: 3 posts (θ 1/121/240) + 3 trapezoid teeth (θ 62/182/300), 2-level pocket floors | z 2.13..8.2 | 2, 3, 4, 5 | both |
| E04 | shoulder block on post 120 (r 14), block on post 240 (r 12.6) | z 2..15 | 1, 3, 5 | both |
| E05 | collar sectors and vertical ribs (r 9.4..9.9), conical column windows at θ 160..205 and 340..25 | z 8.2..15.4 | 1 | both |
| E06 | column r 8.6 with a rounded top edge | z 8.2..27.67 | 1, 3, 5 | both |
| E07 | neck r 5.35 / groove r 4.0 / neck r 5.38 | z 27.7..43.4 | 1, 3, 5 | both |
| E08 | top clip port: square block with rounded lug outline, round rim, bore + counterbore, 2 clip slots per ±X side | z 43.4..48.6 | 1, 3, 5 | both |
| E09 | upper side port along −X (y 12.9, z 30.1), drafted clip plates, orifice web, +Y U-window | x −20.4..0 | 1, 3, 5 | both |
| E10 | lower side port along −X (y −14.1, z 18.2), plates, web, −Y U-window | x −20.4..0 | 1, 3, 5 | both |
| E11 | hose barb along −Y (x −0.09, z 30.76) with collar and a small top rib | y −21.9..−5 | 3, 5 | both (rib not modelled) |
| E12 | microswitch box, 2 top blades, side tab | x 9.7..18 | 1, 2, 4 | both |
| E13 | switch bracket plate (+Y) and holder block (column to switch) | x −0.3..9.7 | 2, 4 | both |
| E14 | fin under the switch (x 8.6..12.8, y −4.8..−3.5) | z 8.5..15.7 | 1 | mesh-only (under the switch; photos do not show that side), modelled |
| E15 | interior bores, spool, passages | not scanned | not visible | occluded (not modelled) |
| E16 | bump under the microswitch (x 10.7..13.9, y 1.8..3.8, z 14.4..15.7) | under the switch | not visible | mesh-only; **added in it2** (QA it1 CHK-ENUM finding, cluster 4) |
| E17 | small lug on the column at theta 312..328, z 22.3..23.2 | +X/−Y side of the column | not visible | mesh-only; **added in it2** (QA it1 CHK-ENUM finding, cluster 8) |
| E18 | horizontal bar at theta ~330 (x to 12.3, y −6.7..−5.6, z 10.8..12.2) | below the switch | not visible | mesh-only; it1 had it as a small sector "rib 320" with the wrong extent (QA it1 cluster 5); **re-measured in it2** |

CHK-ENUM result (it2, after QA it1 found E16/E17 missing): photos 1..5 checked; every feature they show is listed above. The material on
the axis and above the top face was checked (the top face is the highest point at z 48.67).
Unexplained clusters: none. The residual clusters from the builder self-check are at
enumerated features (see `measure/params.json#simplifications`).

## 6. Datum plan and result (from alignment.json)

- Primary (levels): **cap disc outer face → XY at z = 0, +Z into the body**. WHY: the knob-side
  flat of the cap, perpendicular to the spindle. Fit rms 0.0343 / max 0.1039 mm (3,426 faces).
- Secondary: **upper valve column axis**, Kåsa on 10 sections z 37.7..41.8 (r 5.391). WHY: the
  valve spool column. Median rms 0.0448 mm, below the circle noise 0.0479. A first try that also
  used the cap OD failed the circle-noise test (`alignment_try1_two_features.json`) and was
  replaced, because the cap is a separate rotating part.
- Clock: plane_normal, **microswitch outer face normal → +X**, angle −160.62° (plane rms 0.018).
  WHY: the largest flat vertical face. The vertical-face normal histogram peaks every 90°, so the
  ports and the barb land on ±X/±Y.
- Origin: upper valve column axis ∩ cap disc outer face.
- Tilt (CHK-TILT): **finding**. The single-feature fit reads 0.76 ± 0.16° over only 4.1 mm. The
  first two-feature fit read "not resolvable" (cap 2.06° over 1.4 mm vs column 0.46°). Centres of
  5 coaxial features (column z 21, neck z 30, groove z 35, neck z 40, rim z 48) drift ≤ 0.18 mm
  over 27 mm (about 0.4°). The model is coaxial by intent. Cost ≤ 0.11 mm at the cap rim.
- Sanity landmarks: primary at z 0 (0.0017, ok); spindle tip −14.85 (expected −14.8, ok);
  top face 48.67 (expected 48.7, ok).
- Status: **OK**.

## 7. Rebuild strategy summary

One (r,z) revolve for the cap, the pocket floors, the column, the neck and the groove. A 3-fold
cam ring from sector solids (radial post flanks, planar sloped tooth flanks). The top port,
ports, barb and switch are built as sub-bodies and unioned. All cut tools are subtracted once at
the end. The ordered plan is in `build/MODELING_PLAN.md`.

## 8. Risk flags and operator declarations

- The scan is an assembly. It is delivered as one fused solid (as scanned); a multi-body STEP
  would be a separate job.
- Scan-only: Tier-1 is not run, and the absolute scale is not caliper-verified (CHK-SCALE FLAG).
- The spindle spline tooth count is not resolved (CHK-COUNT finding in measure).
- Interior: not scanned, not invented.

## 9. Measurement request → `intake/MEASUREMENTS.md`

Written with scan-predicted values. The owner chose scan-only (`DECISIONS.md` MEASUREMENTS), so
every row is ABSENT, not passed.
