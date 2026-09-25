# Master BOM — Open Dedica (EC685 platform, 230 V build)

> **Generated from [`bom.csv`](bom.csv) by `tools/build_bom.py` — edit the CSV, not this file.**

Every part that appears in CAD, in a scan folder, or on the shopping list has a project **part number** `OD-Xnn`.
See [PART_NUMBERING.md](PART_NUMBERING.md) for the rules. Ref# / OEM code = De'Longhi EC885.M exploded view
(EC680/EC685 interchange on the wet side — verify by PNC before ordering). Prices are 2026 estimates in €.

**Type:** ASM assembly · OEM De'Longhi spare · PRINT our printed part · MFG our non-printed part ·
ELEC off-the-shelf electronics · STD standard hardware · REF reference only · FIX fixture/test rig
**CAD:** SCAN scan + parametric rebuild · CALIPER model from calipers · ENVELOPE simple placeholder solid ·
DESIGN native design · VENDOR vendor STEP
**Status:** ☐ todo · ✎ proposed · 📷 scanned · 🧊 modeled · ✅ validated (check-fixture) · ⏸ deferred

## Assembly tree

- `OD-000` Open Dedica espresso machine (top assembly)
  - `OD-H00` Hydraulic core
    - `OD-H10` Thermoblock sub-assembly
  - `OD-G00` Group head
    - `OD-G10` Portafilter 51 mm (filter holder assembly)
  - `OD-W00` Water path
    - `OD-W01` Water tank assembly
  - `OD-E00` Electronics (choose Path 1 OEM or Path 2 open controller)
  - `OD-C00` Chassis & body
    - `OD-C21` Drip tray (or printed replacement)
  - `OD-S00` Steam system (phase 2 — not in v1)

## OD-000 — Top assembly

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-000` |  | ASM | **Open Dedica espresso machine (top assembly)** |  |  | 1 | DESIGN |  |  |  |  | ☐ |

## H — Hydraulic core

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-H00` | OD-000 | ASM | **Hydraulic core** |  |  | 1 | DESIGN |  |  |  |  | ☐ |
| `OD-H01` | OD-H00 | OEM | Pump ULKA EP5/EX5 48 W 230 V 15 bar | 40 | AS00002825 | 1 | SCAN |  | AliExpress `ULKA EP5 48W 230V` / eBay / ulkapumps.com | 12–25 | #1 | ☐ |
| `OD-H02` | OD-H00 | OEM | Pump protector (rubber sleeve) | 41 | 5213211161 | 1 | SCAN | rubber | AliExpress / FixPart | 4 | #1 | ☐ |
| `OD-H03` | OD-H00 | OEM | Pump suspension spring | 42 | 6113210761 | 1 | CALIPER | steel | FixPart / 4delonghi | 3 | #1 | ☐ |
| `OD-H10` | OD-H00 | ASM | **Thermoblock sub-assembly** |  |  | 1 | DESIGN |  |  |  | #2 | ☐ |
| `OD-H11` | OD-H10 | OEM | Thermoblock (generator 230 V 1300 W + plastic connector) | 60 | 5513226671 | 1 | SCAN | aluminium casting | AliExpress `EC680 thermoblock` / espressocoffeeshop | 25–40 | #2 | 📷 |
| `OD-H12` | OD-H10 | OEM | Spacer | 61 | 5332239300 | 2 | CALIPER |  | 4delonghi | 3 |  | ☐ |
| `OD-H13` | OD-H10 | OEM | Generator gasket | 62 | 5313228791 | 2 (+2 spare) | CALIPER | rubber | 4delonghi | 3 |  | ☐ |
| `OD-H14` | OD-H10 | OEM | Connection | 67 | 5332242400 | 1 | CALIPER |  | 4delonghi | 3 |  | ☐ |
| `OD-H15` | OD-H10 | OEM | Right-angle generator connection | 70 | 5313218931 | 1 | CALIPER |  | 4delonghi | 4 |  | ☐ |
| `OD-H16` | OD-H10 | OEM | NTC sensor | 55 | 5217100200 | 1 | CALIPER |  | FixPart | 5 | #2 | ☐ |
| `OD-H17` | OD-H10 | OEM | NTC fixing bracket | 66 | 6113211071 | 1 | SCAN | steel | FixPart | 3 | #2 | ☐ |
| `OD-H18` | OD-H10 | OEM | TCO 192 °C thermal cutoff — **mandatory** | 68 | 511876 | 1 (+1 spare) | CALIPER |  | FixPart | 5 | #2 | ☐ |
| `OD-H19` | OD-H10 | OEM | TCO fixing bracket | 69 | 6013211951 | 1 | SCAN | steel | FixPart | 3 | #2 | ☐ |
| `OD-H21` | OD-H00 | OEM | Anti-drip valve | 39 | 7313260161 | 1 | SCAN |  | FixPart / 4delonghi | 5 | #6 | ☐ |
| `OD-H22` | OD-H00 | OEM | 3-way valve | 43 | AS00004266 | 1 | SCAN |  | 4delonghi `valve BARM30E` | 5 | #6 | ☐ |
| `OD-H23` | OD-H00 | OEM | 3-way valve connector | 75 | AS00005380 | 1 | CALIPER |  | 4delonghi | 3 | #6 | ☐ |
| `OD-H24` | OD-H00 | OEM | Flowmeter | 45 | 5213225251 | 1 | SCAN |  | FixPart / 4delonghi | 10–15 | #7 | ☐ |
| `OD-H25` | OD-H00 | OEM | Flowmeter–pump tube | 37 | AS00005774 | 1 | ENVELOPE |  | FixPart | 4 |  | ☐ |

## G — Group head & portafilter

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-G00` | OD-000 | ASM | **Group head** |  |  | 1 | DESIGN |  |  |  | #3 | ☐ |
| `OD-G01` | OD-G00 | PRINT | Group head housing (open-source replacement for the molded OEM housing) |  |  | 1 | DESIGN | ABS/ASA | printed — thesis Appendix 2 as starting point | print | #3 | ☐ |
| `OD-G02` | OD-G00 | OEM | Brewing gasket | 46 | 537177 | 1 (+1 spare) | CALIPER | silicone | 4delonghi | 3 | #3 | ☐ |
| `OD-G03` | OD-G00 | OEM | Closure gasket | 47 | 5313221481 | 1 (+1 spare) | CALIPER |  | FixPart | 3 | #3 | ☐ |
| `OD-G04` | OD-G00 | OEM | Brewing gasket support | 48 | AS00005377 | 1 | CALIPER |  | 4delonghi | 3 | #3 | ☐ |
| `OD-G05` | OD-G00 | OEM | Bottom (diffuser) gasket | 49 | AS00005075 | 1 (+1 spare) | CALIPER |  | 4delonghi | 3 | #3 | ☐ |
| `OD-G06` | OD-G00 | OEM | Diffuser (shower screen) | 52 | 6013211191 | 1 | SCAN | stainless | 4delonghi | 3 | #3 | ☐ |
| `OD-G07` | OD-G00 | OEM | Connectors gasket | 54 | 5313237781 | 1 | CALIPER |  | FixPart | 3 | #3 | ☐ |
| `OD-G08` | OD-G00 | MFG | Group head face plate with portafilter lugs (optional upgrade) |  |  | 1 | DESIGN | aluminium / stainless (laser-cut or machined) | local shop | — |  | ✎ |
| `OD-G10` | OD-G00 | OEM | Portafilter 51 mm (filter holder assembly) | 06 | AS00002706 | 1 | SCAN |  | OEM / AliExpress `51mm bottomless portafilter Dedica` | 20–30 | #4 | ☐ |
| `OD-G11` | OD-G10 | OEM | Filter basket 1-cup | 03 | AS00003137 | 1 | CALIPER | stainless | OEM / aftermarket | 5 | #4 | ☐ |
| `OD-G12` | OD-G10 | OEM | Filter basket 2-cup | 04 | AS00003138 | 1 | CALIPER | stainless | OEM / aftermarket | 5 | #4 | ☐ |
| `OD-G13` | OD-G10 | OEM | ESE pods filter (optional) | 05 | 5513281011 | 1 | CALIPER |  | OEM | 5 |  | ☐ |

## W — Water path

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-W00` | OD-000 | ASM | **Water path** |  |  | 1 | DESIGN |  |  |  |  | ☐ |
| `OD-W01` | OD-W00 | OEM | Water tank assembly | 18 | 5513200359 | 1 | SCAN |  | FixPart / 4delonghi | 8–15 | #5 | ☐ |
| `OD-W02` | OD-W01 | OEM | Water tank | 32 | 7313285109 | 1 | SCAN |  | 4delonghi / FixPart | (in OD-W01) | #5 | ☐ |
| `OD-W03` | OD-W01 | OEM | Tray gasket | 30 | 5313236391 | 1 | CALIPER |  | 4delonghi | 3 | #5 | ☐ |
| `OD-W11` | OD-W00 | OEM | Tube L270 (tank → flowmeter) | 31 | 5313219841 | 1 | ENVELOPE | silicone | 4delonghi | 4 |  | ☐ |
| `OD-W12` | OD-W00 | OEM | Tube L150 | 33 | 5313236101 | 1 | ENVELOPE | silicone | FixPart | 4 |  | ☐ |
| `OD-W13` | OD-W00 | OEM | Tube with 2 bushes L230 | 71 | 7313285899 | 1 | ENVELOPE |  | 4delonghi | 5 |  | ☐ |
| `OD-W14` | OD-W00 | OEM | Tube with 1 bush L135 | 72 | 5513213661 | 1 | ENVELOPE |  | FixPart | 4 |  | ☐ |
| `OD-W15` | OD-W00 | OEM | PTFE tube with 2 bushes DI2-DE4 L100 | 73 | 5532111900 | 1 | ENVELOPE | PTFE | FixPart | 4 |  | ☐ |
| `OD-W21` | OD-W00 | OEM | Connector spring | 35 | 6132101300 | 4 | CALIPER | steel | 4delonghi | 8 (set) |  | ☐ |
| `OD-W22` | OD-W00 | OEM | O-ring D3.85 T2 | 36 | 5313217701 | 5 (+5 spare) | CALIPER | rubber | 4delonghi | 8 (set) |  | ☐ |
| `OD-W23` | OD-W00 | OEM | Clip (wire 1.2 AISI302) | 65 | 6113213191 | 3 | CALIPER | stainless | FixPart | 4 |  | ☐ |

## E — Electronics

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-E00` | OD-000 | ASM | **Electronics (choose Path 1 OEM or Path 2 open controller)** |  |  | 1 | DESIGN |  |  |  | #8 | ☐ |
| `OD-E01` | OD-E00 | OEM | Power PCB 230 V — Path 1 | 59 | AS00002829 | 1 | SCAN |  | AliExpress 4001101696035 / eBay | 35–45 | #8 | ☐ |
| `OD-E02` | OD-E00 | OEM | Control board assembly (front buttons) — Path 1 | 15 | 7313285189 | 1 | SCAN |  | FixPart / eBay | 15–25 | #8 | ☐ |
| `OD-E03` | OD-E00 | OEM | Microswitch | 16 | 5113210421 | 1 | CALIPER |  | FixPart | 4 | #8 | ☐ |
| `OD-E04` | OD-E00 | OEM | On/off push button | 28 | 5913216331 | 1 | CALIPER |  | FixPart | 3 |  | ☐ |
| `OD-E05` | OD-E00 | OEM | Unipolar switch 16 A 250 V | 29 | 5128109300 | 1 | CALIPER |  | FixPart | 4 |  | ☐ |
| `OD-E06` | OD-E00 | OEM | Power supply cord with plug (region-specific; AU code shown) | 53 | 5013276449 | 1 | ENVELOPE |  | FixPart / generic | 8 |  | ☐ |
| `OD-E07` | OD-E00 | OEM | 6-pole wiring | 56 | 5013211961 | 1 | ENVELOPE |  | FixPart | 10 (set) |  | ☐ |
| `OD-E08` | OD-E00 | OEM | Wiring with connectors | 57 | 5032509200 | 1 | ENVELOPE |  | FixPart | (set) |  | ☐ |
| `OD-E09` | OD-E00 | OEM | Wiring | 58 | 5013276049 | 1 | ENVELOPE |  | FixPart | (set) |  | ☐ |
| `OD-E51` | OD-E00 | ELEC | ESP32 dev board — Path 2 |  |  | 1 | VENDOR | 3.3 V WiFi | AliExpress | 5–10 |  | ☐ |
| `OD-E52` | OD-E00 | ELEC | SSR for heater — Path 2 |  |  | 1 | VENDOR | ≥25 A zero-cross mains-rated | RS / TME (no no-name for mains) | 8–15 |  | ☐ |
| `OD-E53` | OD-E00 | ELEC | Relay / SSR for pump — Path 2 |  |  | 1 | VENDOR | ≥2 A 230 V | RS / TME | 5–12 |  | ☐ |
| `OD-E54` | OD-E00 | ELEC | Thermocouple type K — Path 2 |  |  | 1 | ENVELOPE | glass-braid | Pimoroni / AliExpress | 20 (with OD-E55) |  | ☐ |
| `OD-E55` | OD-E00 | ELEC | MAX31855 thermocouple board — Path 2 |  |  | 1 | VENDOR |  | Pimoroni / AliExpress | (with OD-E54) |  | ☐ |
| `OD-E56` | OD-E00 | ELEC | Pressure transducer (optional) — Path 2 |  |  | 1 | VENDOR | 0–300 PSI G1/4 | per CaiJonas repo BOM | 15 |  | ☐ |
| `OD-E57` | OD-E00 | STD | G1/4 tee for pressure transducer (optional) |  |  | 1 | VENDOR | brass; 15 bar / 125 °C rated | hardware / AliExpress | 5 |  | ☐ |
| `OD-E58` | OD-E00 | ELEC | Logic PSU — Path 2 |  |  | 1 | VENDOR | 5 V or 24 V | Mean Well-style | 10 |  | ☐ |
| `OD-E59` | OD-E00 | MFG | SSR heat-sink plate |  |  | 1 | DESIGN | aluminium | local shop / scrap | — |  | ✎ |
| `OD-E60` | OD-E00 | STD | IEC inlet with fuse (alternative to OD-E06) |  |  | 1 | VENDOR |  | TME / AliExpress | 4 |  | ☐ |

## C — Chassis & body

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-C00` | OD-000 | ASM | **Chassis & body** |  |  | 1 | DESIGN |  |  |  |  | ☐ |
| `OD-C01` | OD-C00 | PRINT | Base frame / floor plate |  |  | 1 | DESIGN | ASA | printed | print |  | ✎ |
| `OD-C02` | OD-C00 | PRINT | Wet/electric bulkhead with drainage path |  |  | 1 | DESIGN | ASA | printed | print |  | ✎ |
| `OD-C03` | OD-C00 | PRINT | Pump cradle (sleeve + spring suspension) |  |  | 1 | DESIGN | PETG | printed | print | #1 | ✎ |
| `OD-C04` | OD-C00 | PRINT | Thermoblock mount (≥10 mm air gap to printed walls) |  |  | 1 | DESIGN | ASA / PC | printed | print | #2 | ✎ |
| `OD-C05` | OD-C00 | PRINT | Group head carrier (ties OD-G00 to frame) |  |  | 1 | DESIGN | ASA | printed | print | #3 | ✎ |
| `OD-C06` | OD-C00 | PRINT | Water tank dock / inlet seat |  |  | 1 | DESIGN | PETG | printed | print | #5 | ✎ |
| `OD-C07` | OD-C00 | PRINT | Valve & flowmeter mount (OPV reachable without disassembly) |  |  | 1 | DESIGN | PETG | printed | print | #6 | ✎ |
| `OD-C08` | OD-C00 | PRINT | Electronics bay tray |  |  | 1 | DESIGN | PETG | printed | print | #8 | ✎ |
| `OD-C09` | OD-C00 | PRINT | Front panel with button bezel |  |  | 1 | DESIGN | ASA | printed | print | #8 | ✎ |
| `OD-C10` | OD-C00 | PRINT | Top panel (removable — 4 screws) |  |  | 1 | DESIGN | ASA | printed | print |  | ✎ |
| `OD-C11` | OD-C00 | PRINT | Back panel (removable — 4 screws) |  |  | 1 | DESIGN | ASA | printed | print |  | ✎ |
| `OD-C12` | OD-C00 | PRINT | Left side panel |  |  | 1 | DESIGN | ASA / PETG or 3 mm acrylic | printed | print |  | ✎ |
| `OD-C13` | OD-C00 | PRINT | Right side panel |  |  | 1 | DESIGN | ASA / PETG or 3 mm acrylic | printed | print |  | ✎ |
| `OD-C14` | OD-C00 | PRINT | Cable strain relief / grommet |  |  | 2 | DESIGN | TPU | printed | print |  | ✎ |
| `OD-C15` | OD-C00 | PRINT | Foot (alternative to OD-C25/526) |  |  | 4 | DESIGN | TPU | printed | print |  | ✎ |
| `OD-C16` | OD-C00 | PRINT | Corner bracket for acrylic skins (optional) |  |  | 16 | DESIGN | ASA / PETG | printed | print |  | ✎ |
| `OD-C21` | OD-C00 | OEM | Drip tray (or printed replacement) | 09 | 5313249971 | 1 | SCAN |  | FixPart / printed | 8–12 | #9 | ☐ |
| `OD-C22` | OD-C21 | OEM | Float | 08 | 5313249981 | 1 | SCAN |  | FixPart | (with OD-C21) | #9 | ☐ |
| `OD-C23` | OD-C00 | OEM | Cup holder | 07 | 6013214801 | 1 | CALIPER |  | FixPart / printed | 5 | #9 | ☐ |
| `OD-C24` | OD-C00 | OEM | Cup holder with frame | 12 | 5513226761 | 1 | CALIPER |  | FixPart / printed | (with OD-C23) | #9 | ☐ |
| `OD-C25` | OD-C00 | OEM | Rubber foot pad | 34 | 5313229381 | 2 | CALIPER | rubber | FixPart | 4 (set) |  | ☐ |
| `OD-C26` | OD-C00 | OEM | Rubber foot pad | 76 | 5313274719 | 2 | CALIPER | rubber | FixPart | (set) |  | ☐ |

## F — Fasteners, standard hardware & consumables

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-F01` | OD-000 | STD | M3 heat-set insert |  |  | ~40 | VENDOR | brass M3 | AliExpress | 10 (set) |  | ☐ |
| `OD-F02` | OD-000 | STD | M3×8 screw |  |  | ~40 | VENDOR | ISO 7380 / DIN 912 A2 | AliExpress | (set) |  | ☐ |
| `OD-F03` | OD-000 | STD | Acrylic sheet 3 mm (optional skins) |  |  | per design | — | PMMA | local laser / leftover stock | 25 |  | ☐ |
| `OD-F04` | OD-000 | STD | Food-safe silicone tube 4×2 mm (routing reserve) |  |  | 1 m | ENVELOPE | silicone | AliExpress | 5 |  | ☐ |
| `OD-F05` | OD-000 | STD | High-temp epoxy (steam port blank) |  |  | 1 | — | 125 °C / 15 bar | hardware store | 8 |  | ☐ |
| `OD-F06` | OD-000 | STD | 6.3 mm insulated spade terminals + 105 °C wire (own looms) |  |  | 1 set | — |  | TME / AliExpress | 5 |  | ☐ |

## S — Steam system (phase 2)

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-S00` | OD-000 | ASM | **Steam system (phase 2 — not in v1)** |  |  | 1 | DESIGN |  |  |  |  | ⏸ |
| `OD-S01` | OD-S00 | OEM | Steam valve assembly | 17 | AS00002707 | 1 | SCAN |  | FixPart | 15 |  | ⏸ |
| `OD-S02` | OD-S00 | OEM | Steam hose assembly | 10 | AS00002705 | 1 | ENVELOPE |  | FixPart | 12 |  | ⏸ |
| `OD-S03` | OD-S00 | OEM | Steam knob | 13 | 7313285479 | 1 | CALIPER |  | FixPart | 6 |  | ⏸ |
| `OD-S04` | OD-S00 | OEM | Nozzle | 77 | AS00002710 | 1 | CALIPER |  | FixPart | 5 |  | ⏸ |
| `OD-S05` | OD-S00 | OEM | Dispenser cover | 11 | 5313237931 | 1 | CALIPER |  | FixPart | 4 |  | ⏸ |

## R — OEM parts not used (reference only)

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-R01` |  | REF | Upper cover (OEM case — reference only) | 01 | 7313285179 | 0 | — |  | donor | — |  | — |
| `OD-R02` |  | REF | Left profile (OEM case — reference only) | 19 | 5313251321 | 0 | — |  | donor | — |  | — |
| `OD-R03` |  | REF | Right profile (OEM case — reference only) | 26 | 5313251311 | 0 | — |  | donor | — |  | — |
| `OD-R04` |  | REF | Coffee measuring spoon (accessory) | 02 | 7313286119 | 0 | — |  | donor | — |  | — |
| `OD-R05` |  | REF | Cleaning tool (accessory) | 000 | AS00003850 | 0 | — |  | donor | — |  | — |
| `OD-R06` |  | REF | Ecomulticlean 10 ml vial (accessory) | 000 | AS00000378 | 0 | — |  | donor | — |  | — |

## T — Test fixtures & rigs

| Part No | Parent | Type | Name | Ref# | OEM code | Qty | CAD | Material / spec | Source | ~€ | Issue | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `OD-T01` |  | FIX | Group head bench pressure-test rig (M1 close-out) |  |  | 1 | DESIGN |  | printed + fittings | — | #3 | ✎ |

## Budget summary (230 V, no donor)

| Block | Estimate |
|---|---|
| H Hydraulic core | €85–120 |
| G Group head + portafilter | €45–60 |
| W Water path | €50 |
| E Electronics (either path) | €60–100 |
| C/F Chassis hardware | €50 |
| **Total (all new parts)** | **€290–380** |
| **Donor-machine route** (broken EC685 €50 + wear kit €40 + chassis €50) | **~€140** |

Thesis reference total (2019, all-new UK spares): £295.
