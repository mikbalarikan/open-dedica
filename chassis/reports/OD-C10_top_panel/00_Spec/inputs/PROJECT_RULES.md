# PROJECT_RULES — extracts from the open-dedica repository (commit e83c0e6, 2026-10-01)

Verbatim extracts, written by the orchestrator for the OD-C08, OD-C10 and OD-C11 jobs. Source paths are given above each block.

## From docs/SOURCING_GUIDE.md §3.9 (electronics paths) and §3.10 (chassis hardware)

### 3.9 Electronics — two paths

**Path 1 — OEM PCB (fastest to working machine, ~€40–55):**

| Part | EC885 code (ref#) |
|---|---|
| Power PCB | 59: AS00002829 — AliExpress: [EC680/EC685 power board ~$40](https://www.aliexpress.com/item/4001101696035.html); eBay: [power PCB 230V EC680/685/695/785](https://www.ebay.com/itm/175759949100) |
| Control board (front buttons) | 15: 7313285189 |
| Microswitch | 16: 5113210421 |
| On/off button 28: 5913216331, unipolar switch 29: 5128109300, mains cord 53, wiring looms 56–58 | |

You keep OEM behavior (single/double dosing via flowmeter, 3 temperature levels) but the machine stays a black box.

**Path 2 — Open controller (the thesis route, ~€50–80):** microcontroller (the thesis used 2× Arduino Uno; today use one **ESP32**) + SSR for the 1300 W heater + relay/triac for the pump + MAX31855 thermocouple or NTC + the OEM flowmeter. Gets you PID temperature control, pre-infusion profiles, shot-by-flow, and eventually pressure display (see the [CaiJonas Dedica sensor mod](https://github.com/CaiJonas/DeLonghi-Dedica-EC885-EC685-modification) for a proven pressure+temp sensor BOM: 0–300 PSI G1/4 transducer, 104GT-2 NTC, OLED). The thesis wiring diagram and Arduino code are in its Appendix 2. Community PID projects (Gaggiuino-style) are the reference for doing this safely with proper mains isolation.

The thesis SSR/relay/thermocouple part links (RS, TME, Pimoroni) are preserved in `860382060-Part-list-final.docx`.

### 3.10 Chassis hardware (~€15)

- M3 heat-set inserts + M3 screws (the thesis tapped printed holes; inserts are better)
- Cup rack 07/12, drip tray 09: 5313249971 + float 08: 5313249981 — OEM tray is convenient, or design a printed tray + laser-cut grate
- Rubber feet 34/76 or printed TPU feet
- Optional: 3 mm acrylic panels (the thesis's second prototype used laser-cut black/clear acrylic with 16 printed corner brackets — a good look for an open machine: printed frame + acrylic skins)

---


## From docs/SOURCING_GUIDE.md §6 (chassis design rules)

## 6. Chassis Design Rules (learned from the thesis + OEM teardown)

1. **Two-zone layout.** Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) — the thesis literally used two boxes for prototype 1. In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB.
2. **Copy OEM anti-vibration.** Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter.
3. **Respect the thermal map.** Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural.
4. **Serviceability is the point.** The Dedica's worst trait (thesis: "very difficult to disassemble") is our biggest win: top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock.
5. **Design for the mug.** Group head height ≥ 95 mm above tray (thesis legs were sized for a standard mug); keep the 0.4 m³ envelope limit from the thesis spec.
6. **Pre-infusion & preheat are software.** The thesis proved the hardware is capable — temperature stability comparable to OEM (±2 °C) once control was open. Leave sensor bosses (M3/M4 on thermoblock, tee for a thermocouple between heater and group head) in the chassis design from day one.
7. **Safety spec carries over:** piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing.

---


## From docs/WATER_FLOW.md (flow, step by step)

## Flow, step by step

| # | From → To | Tube | Medium | Notes |
|---|---|---|---|---|
| 1 | Water tank `OD-W01` → Flowmeter `OD-H24` | `OD-W11` (L270) | cold | Tank outlet valve seat |
| 2 | Flowmeter `OD-H24` → Pump `OD-H01` | `OD-H25` | cold | Flowmeter pulses are used for volumetric dosing |
| 3 | Pump `OD-H01` → 3-way valve `OD-H22` | TUBE 1 | cold, up to 15 bar | ULKA EP5 vibratory pump |
| 4 | 3-way valve `OD-H22` → Thermoblock `OD-H11` | TUBE 2 | cold, pressurised | |
| 5 | 3-way valve `OD-H22` → Water tank `OD-W01` | TUBE 3 | cold | Bypass / over-pressure return |
| 6 | Thermoblock `OD-H11` → 3-way valve connector `OD-H23` port A | TUBE 4 | hot | NTC `OD-H16` and TCO 192 °C `OD-H18` sit on the thermoblock |
| 7 | Connector port C → Group head `OD-G00` / portafilter `OD-G10` | TUBE 7 | hot | Coffee path |
| 8 | Connector port B → Steam valve `OD-S01` | TUBE 5 | hot / steam | **Phase 2.** Port B is blanked in v1 (`OD-F05`) |
| 9 | Steam valve `OD-S01` → Steam wand `OD-S02` / nozzle `OD-S04` | TUBE 6 | steam | **Phase 2** |

## From chassis/README.md (goal, order of work, interfaces to OD-C01)


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
| 2 | `OD-C05` group head carrier | OD-G01's rear flange, OD-H11 outlet side | modeled, RV02 approved on assumptions (ASA, K1C); open: drain for the foot trough, counterbore floors to sign, a ≥ 210 mm driver |
| 3 | `OD-C03` pump cradle | OD-H01; sleeve OD-H02 and spring OD-H03 | modeled, approved on assumptions (RV02); calipers: H02 sleeve OD, side-wall gap, tie path |
| 4 | `OD-C04` thermoblock mount | OD-H11 with its NTC/TCO brackets (OD-H17, H19) | modeled, approved on assumptions (RV01); calipers: 10.10 mm air gap, spacer lengths, bracket holes |
| 5 | `OD-C07` valve and flowmeter mount | OD-H22, OD-H24 (OD-H21 sits in the water path, not on the mount) | modeled; RV01 REVISE, two seat gaps accepted by the Usta as deviations |
| 6 | `OD-C06` water tank dock | OD-W03 seat; tank OD-W01/W02 | tank not scanned |
| 7 | `OD-C01` base frame / floor plate | the footprints of 2–6; drip tray OD-C21/C22 | modeled, RV01 passed (PETG, Kobra Max 3); flatness is a bench check; layout assumes the group head vertical, housing rear face 205 mm above the base (awaits the Usta's axis decision) |
| 8 | `OD-C02` wet/electric bulkhead | OD-C01, the tube runs | modeled, RV01 approved on assumptions (ASA, K1C); M3×12 into the base rail (`OD-F10`) |
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

Insert pattern as built into OD-C01 (OD-C01 frame, x and z in mm):

| Part | x | z |
|---|---|---|
| `OD-C05` | ±35 | −40, −60 |
| `OD-C04` | ±40 | −148, −114 |
| `OD-C03` | −4, 37 | −239, −171 |
| `OD-C02` | 65 | −45, −105, −165, −225 |
| `OD-C07` | −113, −71 | −42, −148.5 |

Frames for OD-000: OD-C01, OD-C02 and OD-C07's footprint use the machine frame (X right, +Y up, +Z front, plate top y = 0); OD-C05 is in the housing frame (x → X, y → +Z, z → −Y, origin (0, 180.06, 32.0)). Check every insert pattern with calipers before the first print.

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
