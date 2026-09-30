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
| 1 | `OD-G01` group head housing | OD-G09, OD-G04, OD-G10 | — (in progress: `reports/OD-G01_group_head_housing/`) |
| 2 | `OD-C05` group head carrier | OD-G01's rear flange, OD-H11 outlet side | OD-G01 |
| 3 | `OD-C03` pump cradle | OD-H01; sleeve OD-H02 and spring OD-H03 | modeled, approved on assumptions (RV02); calipers: H02 sleeve OD, side-wall gap, tie path |
| 4 | `OD-C04` thermoblock mount | OD-H11 with its NTC/TCO brackets (OD-H17, H19) | modeled, approved on assumptions (RV01); calipers: 10.10 mm air gap, spacer lengths, bracket holes |
| 5 | `OD-C07` valve and flowmeter mount | OD-H22, OD-H24 (OD-H21 sits in the water path, not on the mount) | modeled; RV01 REVISE, two seat gaps accepted by the Usta as deviations |
| 6 | `OD-C06` water tank dock | OD-W03 seat; tank OD-W01/W02 | tank not scanned |
| 7 | `OD-C01` base frame / floor plate | the footprints of 2–6; drip tray OD-C21/C22 | drip tray not scanned |
| 8 | `OD-C02` wet/electric bulkhead | OD-C01, the tube runs | — |
| 9 | `OD-C08` electronics bay tray | OD-E01, OD-E02 (path 1) or OD-E51…E58 (path 2) | the Usta picks the path |
| 10 | `OD-C09` front panel with button bezel | OD-G01 mouth, OD-E02 buttons, OD-S03 knob (phase 2) | — |
| 11 | `OD-C10`, `OD-C11` top and back panels | OD-C01, OD-C02 | — |
| 12 | `OD-C12`, `OD-C13` side panels; `OD-C16` corner brackets | OD-C01 | acrylic option is the Usta's call |
| 13 | `OD-C14` cable grommets, `OD-C15` feet (TPU) | OD-C01, OD-E06 cord | — |
| 14 | `OD-T01` group head pressure-test rig | OD-G01, OD-G10 | — |
| 15 | `OD-C00` … `OD-000` assemblies | everything above plus the `step/` library | all parts |

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

OD-000 placements handed over by the part jobs (joint frames; the assembly uses them):

- `OD-C07`: OD-H24 at (0, 0, 10) and OD-H22 at (62, 0, 48) in the mount frame; the mount sits on OD-C01 with mount x → −Z, y → −X, z → +Y, origin (−92, 0, −60) in the OD-C01 frame.
- `OD-G01`: the group head stands with its axis vertical and the mouth down (the spec §2 sentence saying +Z is horizontal is being corrected in spec 1.4).

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
