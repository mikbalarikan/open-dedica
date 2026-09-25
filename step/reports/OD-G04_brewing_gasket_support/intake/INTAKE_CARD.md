# INTAKE CARD — OD-G04 brewing gasket support

Scan: `input/scan.stl` sha256 `328fdbef574049ee1f0464882a402b6c40b59d231c812a10770938f445ba6010`.
Working copy: `intake/work.stl` (484,578 → 249,999 faces, work-vs-full p95 0.0043 / max 0.066 mm,
seed 0). Official gates run on the full-resolution original, never on the working copy.

## 0. Band regime (declared here, named again in the verdict)
Regime: **baseline-skill, material_class plastic** — p95 ≤ 0.30 / max ≤ 0.80 mm
(`baseline/skills/stl2step-build123d/SKILL.md:87`; `intake/regime.json`).
Why: owner instruction "p95 plastik parça toleransı kullan" (session message, DECISIONS.md
`REGIME`); moulded plastic part; no calipers (scan-only, DECISIONS.md `MEASUREMENTS`).

## 1. What it is (photos + mesh)
Brew-group gasket support disc (espresso machine, inferred from the file name). A moulded
plastic cup: flat back face with a raised bead near the rim and a conical centre recess with a
Ø2.6 centre bore; on the front a hub tube, 6 radial ribs, 2 ring-rib arcs, 4 screw bosses and 2
boss webs; an outer flange with an upstanding gasket lip (with an outer bead) and 3 bayonet
tabs at 120°. Static part, clamped by the bayonet tabs. Material/process: injection-moulded
plastic (inferred: draft, sink-free ribs, photos).

## 2. Scan health (numbers from intake.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | 484,578 / 245,660 |
| Bodies; kept; removed fragments % | 1; largest; 0.0 % |
| Scanner table removed % (rule used) | 0.0 % (none present) |
| Watertight; open boundary edges / loops | no; 6,872 / 40 |
| Normal orientation (method, verdict, flipped?) | ray vote, outward, not flipped |
| bbox raw; bbox datum | 68.03 × 50.78 × 47.23 (tilted); datum extents 67.03 × 68.74 × 17.42 (alignment.json) |
| Units verdict (CHK-SCALE) | not run: no caliper envelope dims (finding: "units assumed mm, scale unverified") |
| Noise floor (value, method, region) | 0.0489 mm, rms of RANSAC+SVD plane on the plate back face (9,868 faces) |
| Artefact zones | none dominant; scan gaps listed in §3 |

## 3. Coverage / occlusion map (datum frame; from `intake.py coverage`, 38 open loops)
| Zone | r | z | θ | Note |
|---|---|---|---|---|
| Plate underside (front floor) | 10–20 | −2.59 | scanned only 20…80° | elsewhere unscanned: plate thickness known from one sector |
| Cup outer wall + flange top | 22.6–26.7 | −10.8…0 | −79…+67° (loop), wall missing −69…+27° | scan gap (outer wall, part of flange top, part of tab 1 top) |
| Hub interior | < 7.8 | −16…−2.6 | 360° | only the centre bore wall (r 1.30, to z −5.64) scanned |
| Rib interiors / rib sides | 10–20.6 | −13…−2.6 | per rib | one-sided rib walls in places |
Angular coverage: outer wall ~270° (alignment secondary fit), tab-1 top face −13…+28° only.

## 4. Functional surfaces & interfaces
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| Z1 | plate back face + bead | seats against the brew-group stack | yes (thickness) | regime |
| Z2 | flange / lip / lip bead | gasket seat | yes | regime |
| Z3 | bayonet tabs | locking | yes | regime |
| Z4 | boss holes | screws | pin gauge | regime |

## 5. Feature enumeration — interior included (CHK-ENUM)
| # | Feature | Seen in mesh (where) | Seen in photo (id) | Status |
|---|---|---|---|---|
| E1 | plate + flat back face | z 0 | 2.png, 4.png back | both |
| E2 | back bead ring r 20.3–21.5 | z 0…1.09 | 2.png | both |
| E3 | hub ring + conical recess + centre bore | r < 6.1 | 2.png, 1.png | both |
| E4 | 4 arc slots round the hub ring | r 6.1–7.5 | 2.png (notches), 1.png | both |
| E5 | cup wall r 20.6/22.95 | z −13…0 | 3.png | both |
| E6 | flange + gasket lip + lip outer bead | r 22.95–31.2 | 3.png, 4.png | both (bead: mesh, faint in 3.png) |
| E7 | 3 bayonet tabs | r 30.8–34.5 | all | both |
| E8 | hub tube (stepped bore) | r 7.8–10.0, z to −15.7 | 1.png, 3.png | both |
| E9 | centre post | bore r 1.30 to z −5.64 | 1.png | mesh (bore) + photo (post) |
| E10 | 6 radial ribs (stepped bottom) | r 10–20.6 | 1.png, 3.png | both |
| E11 | 2 ring-rib arcs r 14.85–16.09 | 4 sectors | 1.png | both |
| E12 | 4 screw bosses (2 heights) with counterbored holes | r 15.5 / 19.0 | 1.png, 3.png | both |
| E13 | 2 webs hub → boss A → wall | boss-A lines | 1.png | mesh; found by the rebuild self-check (see measure) |
| E14 | moulded text on the plate underside | sector 20–80° | 1.png | both — out of scope (declared simplification) |
CHK-ENUM result: all four photos checked; on-axis material = centre bore/post (CHK-CLUSTER in
measure); E13 and the lip bead were enumerated late (after a first CAD self-comparison), recorded
as a finding, not hidden.

## 6. Datum plan and result (from alignment.json)
- Primary: plate back face → XY @ z = 0, material in −Z. WHY: largest clean moulded flat, the
  seating face. Fit rms / max 0.0489 / 0.1097 mm (trimmed; untrimmed 0.066 / 0.193).
- Secondary: outer cylindrical wall of the cup (R 22.90), wall-face IRLS. Fit rms 0.0198 (median
  station), 4 stations.
- Clock: fourier_mass n=3 on the tabs (r 32–35), angle 6.83°. Label rule: tab nearest +X is
  tab 1. Measured tab-1 centre in the frozen frame: −3.30° (the scan gap on tab 1 biases the mass
  phase; CHK-FRAME in measure).
- Origin: cup outer wall axis ∩ plate back face plane.
- Tilt (CHK-TILT): 0.277° ± 0.136° over 2.8 mm (4 stations, one feature) — short span, report-only.
- Sanity landmarks: primary plane at z=0 → observed −0.0088 (tol 0.049) ok.
- Status: OK.

## 7. Rebuild strategy summary
One revolve (r,z) profile carries plate, bead, hub ring, cone, bore/post, hub tube, cup wall,
flange, lip; tabs = 3 sector revolves; ribs, webs, bosses = one instance + placements; slots
and boss holes = cut tools subtracted once. Plan: `build/MODELING_PLAN.md`.

## 8. Risk flags and operator declarations
- No calipers: absolute scale unverified; Tier-1 not run.
- Unscanned: plate underside outside 20–80°, hub interior, centre post outer Ø (assumed 5.0).
- Scan gap on the outer wall/flange top at θ −69…+27°.
- Tab 1 sits 0.15 mm lower than tabs 2/3 (measured, not modelled).

## 9. Measurement request → `intake/MEASUREMENTS.md`
