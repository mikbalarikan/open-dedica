# INTAKE CARD — OD-E01_Power-PCB (populated power PCB, board id PCB00572-01)

Scan: `input/scan.stl` sha256 41448c67a63083726a1c7f2288364cfd9445e66204d05ac3bd13a9ba726c5d93.
Working copy: `intake/work.stl` = the full mesh (398,079 faces, no decimation, `intake/intake.json#decimation`).
Official gates run on the full-resolution original.

## 0. Band regime (declared here, named again in the verdict)
Regime: **baseline-skill, material class plastic** — p95 ≤ 0.30 / max ≤ 0.80 mm
(`baseline/skills/stl2step-build123d/SKILL.md:87`; `intake/regime.json`).
Why: owner brief "p95 plastik parça toleransı kullan" (`decisions/owner_brief.md`); scan-only, no calipers.

## 1. What it is (photos + mesh)
A populated single-sided power PCB (board id `PCB00572-01` legible in photos 1 and 4) from an
appliance (photo 2 shows it installed in a black plastic housing, wired to faston tabs). Top side
carries through-hole power parts (heatsink + TO-220 with a spring clip, electrolytic caps, X2 film
cap, blue Y-cap, axial resistor, 6 faston tabs, 4–5 JST-type connectors, an 8-pin through-hole
device) and SMD parts (SOIC, DPAK, SOT/SOD, 0603/0805/1206 passives). The scan sees the component
side only (the solder side is not scanned: opposite-facing area ≈ 0.6 mm², `work/look2.py` log).
Function of the model: an envelope / fit reference for enclosure design (single fused solid).

## 2. Scan health (numbers from intake.json / alignment.json)
| Item | Value |
|---|---|
| Faces / verts (welded) | 398,079 / 203,996 |
| Bodies; kept; removed fragments % | 1; all; 0 |
| Scanner table removed % | 0 (no table in the scan) |
| Watertight; open boundary edges / loops | no; 10,089 / 55 |
| Normal orientation | ray vote, outward, not flipped |
| bbox raw; bbox datum | raw extents 71.65 × 110.06 × 86.47; datum extents 101.85 × 60.81 × 27.57 |
| Units verdict (CHK-SCALE) | FLAG: no calipers; units assumed mm, scale unverified, none applied |
| Noise floor | plane: 0.0275 rms on the X2 film-cap top (`noise_primary.json`); board top itself 0.0344 (`noise_boardtop.json`); circle: 0.0281 rms on the C20 can wall (`noise_circle.json`) |
| Artefact zones | no-data pockets inside connector housings, under the heatsink/clip, between the caps, in hole bores; board warp (see §8) |

## 3. Coverage / occlusion map (datum frame)
| Zone | Where | Note |
|---|---|---|
| Solder side | whole board z < −1.6 | not scanned: the board bottom face is invented (flat, thickness from the edge walls) |
| Connector cavities | J1–J4 housings | no data inside the openings (deep, narrow) |
| Under heatsink / clip / TO-220 | x 38–55, y −41…−1 | fin roots and the spine sides partly occluded |
| Between caps | x 74–86, y −30…−8 | shadowed board and lead area |
| Hole bores | H1, H2 and small holes | walls partly scanned (H1 fully) |
55 open boundary loops (`intake/coverage.json`). Round-part angular bands do not apply (prismatic board).

## 4. Functional surfaces & interfaces
| Zone | Surface | Why functional | Caliper-coverable? | Band |
|---|---|---|---|---|
| I1 | PCB top face + outline edges | seating in enclosure / card guides | yes (ENV-X/Y, F03) | regime band |
| I2 | mounting holes H1, H2 | screw bosses | yes (F01, F02) | regime band |
| I3 | faston tab row | harness access | yes (F04, F05) | regime band |
| I4 | heatsink top, tallest parts | lid clearance | yes (F06, F07) | regime band |
No regime interface band exists (baseline-skill has none); these are named zones for reporting.

## 5. Feature enumeration (CHK-ENUM)
| # | Feature | Seen in mesh | Seen in photo | Status |
|---|---|---|---|---|
| E01 | PCB plate, rectangular, with a routed slot on the −X edge (y≈−26.5) | edges, top | 1,3,4 | both |
| E02 | mounting holes H1 (0,0), H2 (0,−51.8) Ø≈4 | yes | 4 | both |
| E03 | 4 small holes Ø≈1.3–2 (x≈11.6/11/57.4) | yes | 4 | both |
| E04 | heatsink, extruded star profile, 2 hubs with screw channels, 16 fins + spine | top + fins | 1,2,3,4 | both |
| E05 | TO-220 on the heatsink spine (−X face), 3 leads | side view | 1 (tab), 4 | both |
| E06 | spring clip (strap) around heatsink + TO-220 | z 6.9–13.5 | 1 (gold strap) | both |
| E07 | electrolytic caps ×5 (Ø≈10.2 ×2, Ø≈7.7, Ø≈6.5, Ø≈5.5) | yes | 1,3,4 | both |
| E08 | X2 film capacitor (grey box) | yes | 1,3,4 | both |
| E09 | blue ceramic Y-capacitor (tilted disc) | yes | 1,2,3,4 | both |
| E10 | axial resistor, raised, with bent leads | yes | 1,3,4 | both |
| E11 | 6 faston tabs 6.3 × 0.8 with detent hole | yes | 1,2,3,4 | both |
| E12 | JST-type connectors (white) ×4 + 1 small 2-pin block | yes (cavities no data) | 1,3,4 | both |
| E13 | 8-pin THT device near the caps | yes | 1,3 | both |
| E14 | SMD power inductor (square, ≈9.5) | yes | 3,4 | both |
| E15 | SOIC IC, DPAK, SOT/SOD, SMD passives (≈70) | yes | 1,4 | both |
| E16 | edge contact pads (programming) | flat, no height | 1,4 | not modelled (copper, < 0.1 mm) |
| E17 | silkscreen, traces, solder joints, QR label | texture | 1,4 | not modelled (declared) |
CHK-ENUM: every photo checked (1–4); every height cluster > 0.18 mm above the board is in
`measure/figures/seg.json` and mapped to a row above; no unexplained cluster.

## 6. Datum plan and result (`intake/alignment.json`, status OK)
- Primary: PCB top face → XY at z = 0, +Z out of the component side. WHY: component seating plane /
  enclosure reference. Fit rms 0.0342 / max 0.110 (trimmed), untrimmed rms 0.0498 / max 0.254.
- Secondary: mounting hole H1 axis (wall-face IRLS, 4 stations), r 2.021, rms 0.0165 / max 0.107.
- Clock: plane_normal on the +X short board edge → +X, 121.954°. Cross-check (line fits on all four
  edge walls in the datum frame): edges parallel to the axes within 0.083°.
- Origin: H1 axis ∩ PCB top face.
- Tilt (CHK-TILT, finding): 1.03 ± 0.34° over a 0.78 mm span (the board is 1.6 mm thick; not a
  meaningful axis tilt; drilled hole assumed perpendicular).
- Sanity landmark: primary plane at z=0 (0.0011, ok).
- Datum history: try 1 STOPPED (primary rms 0.0342 > film-cap noise 0.0275;
  `intake/_datum_try1_STOP/`). Cause: the board is bowed/twisted (quadratic board-top model spans
  about −0.2…+0.1 mm, corners at H1 lowest) and carries copper-trace relief. Re-run with the noise
  measured on the board top itself (self-referential, as the OD-H22 run did) — recorded as a
  finding in `DECISIONS.md`.

## 7. Rebuild strategy summary
Board: one sketch (rectangle + slot + holes) extruded −t. Components: one instance per part type
placed at measured positions (boxes, vertical cylinders, faston tab instances, connector boxes with
pockets); heatsink: ONE extruded profile (hubs + spine + fin slots − channels); clip: extruded
thick polyline; resistor / Y-cap: cylinders on measured axes. All unioned into one solid.

## 8. Risk flags and operator declarations
- Board warp ±0.2 mm is not modelled (flat design-intent board) — declared simplification.
- Solder side, hidden lower parts of components, connector cavity depths, heatsink root: invented/assumed.
- Scale unverified (no calipers).
- SMD passives modelled as boxes of measured footprint and height; solder fillets not modelled.

## 9. Measurement request → `intake/MEASUREMENTS.md` (not filled: scan-only run)

## 10. Update after measure (CHK-ENUM / CHK-CLUSTER feedback, 2026-09-28)
- E13 "8-pin THT device" is two axial bodies side by side (D1, D2; Ø≈2.6–2.7) lying along Y, not a DIP
  (`measure/figures/pcb_measure.json#axial_D1/D2`).
- An axial part between the caps (L2, Ø≈3.0, partly hidden) was added by measure (CHK-CLUSTER).
- C1 is an SMD V-chip electrolytic (square plastic base + can); C5 is a flanged can / drum part.
- The heatsink hubs are C-shaped screw channels (open outward); the spine is notched under the TO-220
  and drilled for its screw.
