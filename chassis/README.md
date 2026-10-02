# chassis/ — the printed parts and the assembly

Printed chassis CAD and STL/3MF exports (phase 3), designed part by part with the
OGUZ Atölye pipeline (`mikbalarikan/oguz-atolye`); each part's job record sits in
`reports/<part>/` with a README that says how to resume it.

## Goal

Every custom part of the machine that is 3D-printable, designed and reviewed, and
the whole machine delivered as an assembly:

- one parametric build script, STEP (mm, one named solid) and STL/3MF per printed
  part, with its print orientation and material stated;
- the top assembly `OD-000` as a STEP that places every printed part and every OEM
  part of the `step/` library by joints, with the sub-assemblies `OD-H00`, `OD-G00`,
  `OD-W00`, `OD-E00`, `OD-C00`;
- `docs/bom.csv` at `modeled` for every part, `docs/BOM.md` and the progress board
  regenerated, and a build guide (`docs/BUILD_GUIDE.md`) that goes from the BOM to a
  running machine.

`validated` needs a print and a fit check by the Usta; the group head also needs the
bench pressure test (`OD-T01`).

## Order of work

Each part is designed against the scanned OEM parts it touches. A part whose OEM
neighbour is not scanned yet carries that neighbour as an assumption row and is
revisited when the scan lands.

| # | Part | Designed against | Blocked by |
|---|---|---|---|
| 1 | `OD-G01` group head housing | OD-G09, OD-G04, OD-G10 | modeled, RV01 REVISE on REQ-12 alone (brew-load strength, answered only by the OD-T01 bench test), accepted by the Usta as a documented deviation (2026-10-02); every geometric row passes |
| 2 | `OD-C05` group head carrier | OD-G01's rear flange, OD-H11 outlet side | modeled, RV02 approved on assumptions (ASA, K1C); open: drain for the foot trough, counterbore floors to sign, a ≥ 210 mm driver |
| 3 | `OD-C03` pump cradle | OD-H01; sleeve OD-H02 and spring OD-H03 | modeled, approved on assumptions (RV02); calipers: H02 sleeve OD, side-wall gap, tie path |
| 4 | `OD-C04` thermoblock mount | OD-H11 with its NTC/TCO brackets (OD-H17, H19) | modeled, approved on assumptions (RV01); calipers: 10.10 mm air gap, spacer lengths, bracket holes |
| 5 | `OD-C07` valve and flowmeter mount | OD-H22, OD-H24 (OD-H21 sits in the water path, not on the mount) | modeled; RV01 REVISE, two seat gaps accepted by the Usta as deviations |
| 6 | `OD-C06` water tank dock | OD-W03 seat; tank OD-W01/W02 | deferred: the tank stands on the table (the Usta, 2026-10-01); its tubes and the mains cord leave through OD-C11's three Ø12 pass-throughs at y 30 |
| 7 | `OD-C01` base frame / floor plate | the footprints of 2–6; drip tray OD-C21/C22 | modeled, RV01 passed (PETG, Kobra Max 3); flatness is a bench check; layout assumes the group head vertical, housing rear face 205 mm above the base (awaits the Usta's axis decision); OD-C01 A-12 (feet screwed from below) is superseded by OD-C15 A-02 (screw from above, captive nut); the 8 inserts for OD-C08 and OD-C11 below are not in the plate STEP yet |
| 8 | `OD-C02` wet/electric bulkhead | OD-C01, the tube runs | modeled, RV01 approved on assumptions (ASA, K1C); M3×12 into the base rail (`OD-F10`) |
| 9 | `OD-C08` electronics bay tray | OD-E01, OD-E02 (path 1) or OD-E51…E58 (path 2) | modeled, RV01 approved on assumptions (PETG, K1C); path 1, the OEM PCB OD-E01 on edge; OD-E02 (front buttons) belongs to OD-C09 |
| 10 | `OD-C09` front panel with button bezel | OD-G01 mouth, OD-E02 buttons, OD-S03 knob (phase 2) | — |
| 11 | `OD-C10`, `OD-C11` top and back panels | OD-C01, OD-C02 | modeled, both RV01 approved on assumptions (PETG, Kobra Max 3); OD-C11 took three builds (spec faults in 1.0 and 1.1, recorded) |
| 12 | `OD-C12`, `OD-C13` side panels; `OD-C16` corner brackets | OD-C01 | printed, not acrylic (the Usta, 2026-10-02) |
| 13 | `OD-C14` cable grommets, `OD-C15` feet (TPU) | OD-C01, OD-E06 cord | `OD-C15` modeled, RV01 approved on assumptions (TPU 95A, K1C): Ø18 × 10 puck, M3×12 from the top into a captive M3 nut; `OD-C14` open |
| 14 | `OD-T01` group head pressure-test rig | OD-G01, OD-G10 | — |
| 15 | `OD-C00` … `OD-000` assemblies | everything above plus the `step/` library | all parts |

**Material for now:** the Usta set PLA for every printed part (2026-10-02); the BOM
keeps each part's service material next to it. PLA softens near 60 °C, so PLA
prints of `OD-G01`, `OD-C04` and `OD-C05` (next to the thermoblock and the group
head) are dry fit checks only: never run hot water or pressure through them, and
run the OD-T01 bench test on an ASA housing.

Machine profiles: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large
panels: PETG); build volumes to be read into `oguz-atolye/atolye/machines/`.

## Interfaces to OD-C01

Parts that bolt to the base frame fix it with M3 screws into heat-set inserts
(`OD-F01`) in `OD-C01`. Coordinates are in each part's own frame, from its job
record; OD-C01 must carry an insert at each.

| Part | Inserts in OD-C01 (x, z) mm | Hardware |
|---|---|---|
| `OD-C03` pump cradle | (±34, −4), (±34, 37) | 4 × M3 (`OD-F02`), 2 × cable tie (`OD-F09`) |
| `OD-C04` thermoblock mount | (±40, −8), (±40, 26) | 4 × M3 (`OD-F02`); the thermoblock sits on the metal spacers `OD-F07` and `OD-F08` (M3 through their Ø4 bores; screw length set when the spacers are cut) |
| `OD-C07` valve and flowmeter mount | four Ø3.4 through-holes at (−18, ±21) and (88.5, ±21) in the mount frame; OD-C01 spec 1.1 REQ-10 provides them | 4 × M3 (`OD-F02`) into OD-C01; 2 × M3 insert (`OD-F01`) for OD-H22 |
| `OD-C08` electronics bay tray | flange (88, −222), (106, −222), (88, −78), (106, −78) | 4 × M3×8 (`OD-F02`); 2 × M3×6 (`OD-F11`) for the board into 2 inserts in the tray's standoffs |
| `OD-C11` back panel | flanges (±81, −282), (±95, −282) | 4 × M3×8 (`OD-F02`); 2 inserts in its ledge take OD-C10's rear screws |
| `OD-C10` top panel | none: 2 screws into OD-C02's top-rail inserts, 2 into OD-C11's ledge | 4 × M3×8 (`OD-F02`) |
| `OD-C15` feet | none: the four Ø3.4 through-holes at (±110, +90) and (±110, −295) | 4 × M3×12 (`OD-F10`) from the plate top, 4 × M3 nut (`OD-F12`) captive in the feet |

Insert pattern as built into OD-C01 (OD-C01 frame, x and z in mm):

| Part | x | z |
|---|---|---|
| `OD-C05` | ±35 | −40, −60 |
| `OD-C04` | ±40 | −148, −114 |
| `OD-C03` | −4, 37 | −239, −171 |
| `OD-C02` | 65 | −45, −105, −165, −225 |
| `OD-C07` | −113, −71 | −42, −148.5 |
| `OD-C08` (new, not in the plate STEP yet) | 88, 106 | −222, −78 |
| `OD-C11` (new, not in the plate STEP yet) | ±81, ±95 | −282 |

The eight new inserts sit from the plate's top face (axis −Y), each ≥ 6 from every existing hole and ≥ 8 from the edge (checked by the C08 and C11 reviewers). The plate is 6 thick, so a 6 deep bore reaches the underside: an OD-C01 revision decides through vs. blind (a boss below, or a 5.0 bore with a shorter insert).

Frames for OD-000: OD-C01, OD-C02, OD-C08, OD-C10, OD-C11 and OD-C07's footprint use the machine frame (X right, +Y up, +Z front, plate top y = 0); OD-C05 is in the housing frame (x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0)). Check every insert pattern with calipers before the first print.

OD-000 placements handed over by the part jobs (joint frames; the assembly uses them):

- `OD-C07`: OD-H24 at (0, 0, 10) and OD-H22 at (62, 0, 48) in the mount frame; the mount sits on OD-C01 with mount x → −Z, y → −X, z → +Y, origin (−92, 0, −60) in the OD-C01 frame.
- `OD-C08`, `OD-C10`, `OD-C11`: modelled in the machine frame, placed at the identity. OD-E01 sits on OD-C08 with board x → −Z, y → +Y, z → +X, origin (84, 80, −100). Check assemblies: `reports/<part>/02_STEP_STL/`.
- `OD-C15`: foot frame origin at the centre of its top face, foot z 0 … 10; foot x → X, y → +Z, z → −Y, origins (±110, −6, +90) and (±110, −6, −295). The counter is at y −16. Check assembly: `reports/OD-C15_foot/02_STEP_STL/od_c15_assembly_C1_v01.step`.
- `OD-G01`: the group head stands with its axis vertical and the mouth down (the spec §2 sentence saying +Z is horizontal is being corrected in spec 1.4).

Keep-outs for later parts:

- `OD-C15` (spec A-09): a Ø8 × 2.0 cylinder above each foot hole on the plate top (y 0 … 2.0) holds the screw head. OD-C11's wall foot clears it by 0.0 (touching, no overlap); OD-C12, OD-C13, OD-C16 and OD-C06 must leave it free.
- `OD-C08` occupies x 73 … 112, z −230 … −70, y 0 … 92 (with the board, to x ≈ 109.3).
- `OD-C10`'s side and front edges are free until OD-C09, OD-C12 and OD-C13 exist: those panels end at y 215 under the lid's 3 mm skirt (x ±117 … ±120, z −305 … +100). Until then the lid settles onto its −X rest pad (centre of mass 24 mm outside its four columns, OD-C10 RV01 F1).

"Approved on assumptions" (`APPROVED_ASSUMPTION_CONDITIONAL`) means every gate
passes on scan-derived values that the Usta has not confirmed with calipers yet;
the BOM shows such parts as `modeled`, and `validated` still needs the print and
fit check.

## Files

```
chassis/
  OD-Cnn_<short_name>.step  .stl  .3mf     one per printed part (OD-G01 too)
  OD-000_open_dedica_assembly.step         the top assembly, sub-assemblies inside
  src/OD-Xnn_<short_name>/build_*.py       parametric build and check scripts
  reports/OD-Xnn_<short_name>/             the job record of each part
```
