# How to Source the BOM for an Open-Source DIY De'Longhi Dedica Espresso Machine

*A component-sourcing and reverse-engineering guide for building a custom 3D-printed-chassis espresso machine around genuine De'Longhi Dedica EC685 internals.*

> **Caution — this guide may contain errors and omissions.** Part numbers, prices and links change constantly. We have no relation to any of the sellers linked in this guide — links are provided to verify our findings and to seed your own searches.

> **⚡ SAFETY: This machine runs on mains voltage (230 V or 120 V), heats water to ~125 °C, and pressurizes it to 15 bar.** Anything you build must keep the wet side separated from the electric side, use properly rated wiring and crimps, keep the 192 °C thermal cutoff (TCO) in circuit, and be tested behind an RCD/GFCI. Never print load-bearing or heat-adjacent parts in PLA.

---

## 1. The Concept

The De'Longhi Dedica EC685 is one of the best-value semi-automatic espresso platforms ever made: a 1300 W single-part thermoblock, a genuine ULKA 15-bar vibratory pump, a proper 51 mm portafilter, and a compact plumbing layout — all of whose internal parts are **publicly purchasable as spares**. This was proven by Zack Moss's 2019 MEng thesis *Open Source Espresso Machine for Makers*, which reverse-engineered exactly this machine (EC685.M), rebuilt it around Arduinos, and matched the original in temperature stability and espresso taste.

The one component you **cannot** buy is the chassis-integrated group head housing — De'Longhi molded it into the case. The thesis solved this with a 3D-printed ABS housing holding the genuine gaskets and diffuser. That is our opening: if the group head housing must be printed anyway, the **entire chassis** can be an open-source 3D-printed design.

**The plan:**
1. Source every functional Dedica part (pump, thermoblock, valves, tubes, tank, portafilter, PCB or open controller).
2. 3D-scan / measure each part and produce a STEP file library.
3. Design an open, printable chassis in CAD around the STEP assembly.
4. Publish BOM + STEP + STL/3MF + build instructions.

This mirrors the approach of the [OOMWOO open-source vacuum robot BOM guide](https://makerspet.com/blog/how-to-source-bom-for-oomwoo-open-source-vacuum-robot/): salvage/source proven mass-produced components, print everything structural.

---

## 2. Two Sourcing Strategies

### Strategy A — Donor machine (recommended)
Buy a **used, broken, or open-box Dedica EC680 / EC685 / EC885** and strip it. A defective unit sells for €30–70 on eBay/Kleinanzeigen/Marktplaats/local classifieds; even a new one (~€120–150) is cheaper than buying every part individually (the thesis parts list totalled **£295** buying parts one by one, and called the De'Longhi spares "very overpriced"). Most "broken" Dedicas have a scaled thermoblock, a torn brew gasket, or a dead pump — each a €10–25 fix — while every other part is a free spare.

- eBay search seeds: `Dedica EC685 defekt`, `Dedica EC685 parts repair`, `EC680 faulty`
- What kills them: limescale blockage (recoverable — descale/replace tubes), pump failure (€15), leaking group gasket (€3).

### Strategy B — All-new parts
Buy every component as a spare. Slower and pricier, but every part is new and you get exact BOM traceability. Use the part-code tables below. Best hybrid: donor machine for the plumbing + new wear parts (gaskets, O-rings, brew gasket, tubes).

**⚠ Voltage:** EC685 exists in 230 V (EU/UK/AU) and 120 V (US) versions. The thermoblock, pump, PCB and TCO are voltage-specific. AliExpress stock is almost entirely 230 V. Decide your mains voltage first and match **every** electrical part to it.

---

## 3. Component-by-Component Sourcing

Prices are 2026 ballparks; they fluctuate with seasonal sales and coupons. Part codes below are from the official De'Longhi **EC885.M exploded view** (`EC885 Exploded View .pdf` — the EC885 Dedica Arte shares its wet side with the EC685) and from the thesis part list (`860382060-Part-list-final.docx`, with live 4delonghi.co.uk links keyed to EC680).

### 3.1 Pump — ULKA EP5 / EX5 vibratory pump (~€12–25)

The heart of the machine and the easiest part to source — ULKA pumps are a de-facto industry standard used across De'Longhi, Gaggia, Saeco, Breville.

| Spec | Value |
|---|---|
| Model | ULKA EP5 (plastic outlet) or EX5 (brass outlet) |
| Power | 48 W, 230 V 50 Hz (120 V 60 Hz variant: EP5/EX5 120 V) |
| Max pressure | 15 bar |
| De'Longhi code | AS00002825 "PUMP (ULKA 230V 48W)" (exploded view #40) |
| Mounting | Rubber pump protector 5213211161 (#41) + spring 6113210761 (#42) |

- AliExpress: search `ULKA EP5 48W 230V` / `ULKA EX5 vibration pump` — e.g. [this EX5 listing](https://www.aliexpress.com/item/1005004294491879.html)
- eBay: [EP5 48W 230V](https://www.ebay.com/itm/173745525246), [EP5 15 bar](https://www.ebay.com/itm/387082132812)
- Official distributor: [ulkapumps.com](https://ulkapumps.com/en-us)
- The thesis used the Amazon UK ULKA EP5 (~£16) as a drop-in for the OEM pump.

**Chassis note:** the Dedica suspends the pump in a rubber sleeve + spring to damp vibration. The thesis's first rigid printed pump mount produced "unacceptable levels of vibration"; the second iteration replicated the OEM sleeve-and-spring suspension and fixed it. Copy the OEM mounting concept in the printed chassis.

### 3.2 Thermoblock ("generator") — 1300 W single-part (~€20–40)

Single-part aluminium thermoblock with embedded stainless pipe — low leak risk, low scale-up risk, 40 s heat-up.

| Spec | Value |
|---|---|
| De'Longhi code | 5513226671 "GENERATOR (230V 1300W + plastic connector)" (#60) — EC680/EC685 listings also appear as "generator/thermoblock EC680" |
| Sensor | NTC sensor 5217100200 (#55) + fixing bracket 6113211071 (#66) |
| Thermal cutoff | TCO 192 °C, code 511876 (#68) + bracket 6013211951 (#69) — **never omit this** |
| Gaskets | Generator gasket 5313228791 ×2 (#62), spacer 5332239300 (#61) |
| Connections | Right-angle generator connection 5313218931 (#70), connection 5332242400 (#67) |

- Search seeds: `EC685 thermoblock`, `Delonghi generator EC680 1300W`, `Dedica heating element`
- Dedicated Dedica spares pages: [espressocoffeeshop](https://spareparts.espressocoffeeshop.com/en/3901-de-longhi-ec685m-delonghi-dedica-parts), [FixPart EC685.M](https://fixpart.co.uk/coffee-machine-spare-parts/delonghi/ec685m-0132106138-dedica), [4delonghi.co.uk](https://www.4delonghi.co.uk/ec685m/catalogue.pl?path=316723&model_ref=13165954), [yourspares](https://www.yourspares.co.uk/parts/delonghi/coffee-machines/dedica-ec685m.aspx)
- US (120 V) sources: [eReplacementParts EC685M](https://www.ereplacementparts.com/models/coffee-maker/delonghi/id1362996/ec685m/), [Encompass](https://delonghi.encompass.com/model/DEIEC685M)

**Chassis note:** thermoblock skin runs well above 100 °C. Keep ≥10 mm air gap to any printed part, mount it on its OEM bracket geometry, and use ABS/ASA/PC (not PETG, never PLA) for anything within radiant range. The thesis mounted heater and SSRs on metal plates as heat sinks.

### 3.3 Group head — the part you must print (~€12 in gaskets + printing)

The OEM group head housing is integrated into the Dedica casing — the thesis cut it out of the donor case for prototype 1, then designed a 3D-printed ABS replacement for prototype 2 (a ~£12 open-source substitute for group heads that otherwise start at ~£95). **This is the flagship printed part of our chassis.** All the sealing internals are standard spares:

| Part | EC885 code (ref#) | ~Price |
|---|---|---|
| Brewing gasket | 46: 537177 (EC680 link in thesis docx) | €3 |
| Closure gasket | 47: 5313221481 | €3 |
| Brewing gasket support | 48: AS00005377 | €3 |
| Bottom/diffuser gasket | 49: AS00005075 | €3 |
| Diffuser (shower screen) | 52: 6013211191 | €3 |
| Connectors gasket | 54: 5313237781 | €3 |

- Thesis-verified EC680 purchase links for all of these are in `860382060-Part-list-final.docx`.
- Search seeds: `EC680 brewing gasket`, `Dedica diffuser`, `Delonghi 51mm shower screen`
- Print in **ABS/ASA** (thesis: PLA deformed; ABS survived because brew water never directly contacts the housing). Consider a printed housing clamping a machined/laser-cut aluminium or stainless face plate for the portafilter lugs if you want longevity beyond the thesis design.

### 3.4 Portafilter and filters (~€20–30)

| Part | EC885 code (ref#) |
|---|---|
| Filter holder assembly (51 mm) | 06: AS00002706 |
| Small 1-cup filter | 03: AS00003137 |
| Large 2-cup filter | 04: AS00003138 |
| ESE pods filter | 05: 5513281011 |

Aftermarket 51 mm bottomless portafilters for the Dedica are abundant on AliExpress (search `51mm bottomless portafilter Dedica`) and often nicer than OEM — a good open-source-friendly upgrade.

### 3.5 Valves — over-pressure, anti-drip, 3-way (~€10–20)

| Part | EC885 code (ref#) | Role |
|---|---|---|
| Anti-drip valve | 39: 7313260161 | stops dripping after shot |
| Valve (3-way) | 43: AS00004266 | releases puck pressure to drip tray |
| 3-way valve connector | 75: AS00005380 | |
| Spring | 42: 6113210761 | OPV spring (sets ~15 bar static) |
| Valve internals | thesis docx links: valve BARM30E, ring BAR16E, gasket | |

**Mod-friendly note:** the OPV spring is where people do the "9-bar mod" (community-documented for Dedica). An open chassis should make the OPV accessible without disassembly.

### 3.6 Flowmeter (~€10–15)

| Part | EC885 code (ref#) |
|---|---|
| Flowmeter | 45: 5213225251 |
| Flowmeter-pump tube | 37: AS00005774 |

Optional if you run OEM electronics (it's how the PCB doses single/double shots); essential for a smart open controller. Datasheet-driven (hall pulse output) — the thesis recommends wiring it to the microcontroller for volumetric dosing.

### 3.7 Water tank and tubing (~€20–35)

| Part | EC885 code (ref#) |
|---|---|
| Water tank | 32: 7313285109 (assembly 18: 5513200359) |
| Tank tube L270 | 31: 5313219841 |
| Tube L150 | 33: 5313236101 |
| Tube with 2 bushes L230 | 71: 7313285899 |
| Tube with 1 bush L135 | 72: 5513213661 |
| PTFE tube DI2-DE4 L100 | 73: 5532111900 |
| Tray gasket | 30: 5313236391 |
| O-rings D3.85 | 36: 5313217701 (×5+) |
| Springs (connector) | 35: 6132101300 (×4) |
| Clips AISI302 | 65: 6113213191 (×3) |

The OEM silicone/PTFE tube set with molded bushes is cheap — buy it rather than improvising fittings, and design the chassis around OEM tube lengths (or buy generic food-grade silicone tube 4×2 mm + PTFE 2×4 mm for custom routing). The tank is a good candidate to keep OEM (food-safe, has valve + level float geometry) or redesign later as a printed+bottle solution.

### 3.8 Steam system (optional, phase 2)

| Part | EC885 code (ref#) |
|---|---|
| Steam valve assembly | 17: AS00002707 |
| Steam hose assembly | 10: AS00002705 |
| Steam knob | 13: 7313285479 |
| Nozzle | 77: AS00002710 |

The thesis blocked the steam line with high-temp epoxy for prototype 1 and never re-added it. Recommend the same for v1: espresso first, steam later. If skipped, cap the 3-way valve's steam port properly (rated for 125 °C / 15 bar).

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

## 4. Sourcing Tips

1. **Search by part code, then by description.** `5513226671` finds exact hits; `Dedica thermoblock` finds cheaper compatibles. AliExpress sellers often list under EC680 — the EC680/EC685/EC885 wet side is interchangeable for our purposes ([AliExpress EC685 search](https://www.aliexpress.com/w/wholesale-delonghi-ec685-accessories.html)).
2. **Cross-check codes against the exploded view.** `EC885 Exploded View .pdf` is the authoritative ref# ↔ code map (65 numbered positions). For EC685-specific codes use [FixPart's model pages](https://fixpart.co.uk/coffee-machine-spare-parts/delonghi/ec685m-0132106138-dedica) which index by PNC (e.g. 0132106138 = EC685.M).
3. **Buy wear parts ×2.** Gaskets, O-rings, springs, brew gasket — they're €2–3 each and you will tear one during assembly.
4. **Prices swing with sales** (11.11, Anniversary sale, coupons). The €30 part today is €18 next month.
5. **One seller ≠ one order.** Consolidate: most De'Longhi-spares AliExpress stores carry the pump, PCB, thermoblock and gasket kit simultaneously — one store, one shipment, one customs event.
6. **Keep the donor manuals.** `Magnifica Data Sheet and Service Manual.pdf` and `LA SPECIALISTA Data Sheet and Service Manual.pdf` show De'Longhi's service-level test procedures (resistance values, NTC curves) that transfer to the Dedica family.

---

## 5. From Parts to STEP Files (scan & CAD workflow)

Goal: a `step/` library where every purchased part has a dimensionally-trusted model, so the chassis is designed against reality.

**Per-part workflow:**
1. **Photograph** the part on a grid mat (top/bottom/sides + connector close-ups). Store in `SCANS/<part>/photos/`.
2. **Measure** critical interfaces with calipers: mounting hole patterns, boss diameters, tube spigots, connector pitch. Interfaces must be caliper-accurate — scans are for envelopes, calipers are for fits.
3. **Scan** organic/complex parts (thermoblock casting, pump body, tank): photogrammetry (60–100 photos, matte spray on shiny silicone/chrome) or a structured-light scanner. Export mesh (STL/PLY).
4. **Rebuild as parametric CAD**, don't ship raw meshes: import mesh as reference, model clean solids over it (Fusion/SolidWorks/FreeCAD). Simple parts (tubes, gaskets, brackets) get modeled from caliper dims alone.
5. **Export STEP (AP214)** to `step/` with the naming scheme `OD-Xnn_<name>.step` (e.g. `OD-H01_ulka_ep5_pump.step`; see [PART_NUMBERING.md](PART_NUMBERING.md)).
6. **Validate**: print a check-fixture (a ring or cradle) for each critical part and test-fit the real component before trusting the model in the chassis assembly.

We already have a FreeCAD batch pipeline (freecadcmd) for STEP→STL conversion from other projects — reuse it for print exports.

**Scan priority order** (what the chassis actually touches): pump + sleeve → thermoblock + brackets → group head gasket stack + portafilter lugs → water tank + valve seat → flowmeter → PCB outlines + button geometry → drip tray.

---

## 6. Chassis Design Rules (learned from the thesis + OEM teardown)

1. **Two-zone layout.** Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) — the thesis literally used two boxes for prototype 1. In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB.
2. **Copy OEM anti-vibration.** Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter.
3. **Respect the thermal map.** Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural.
4. **Serviceability is the point.** The Dedica's worst trait (thesis: "very difficult to disassemble") is our biggest win: top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock.
5. **Design for the mug.** Group head height ≥ 95 mm above tray (thesis legs were sized for a standard mug); keep the 0.4 m³ envelope limit from the thesis spec.
6. **Pre-infusion & preheat are software.** The thesis proved the hardware is capable — temperature stability comparable to OEM (±2 °C) once control was open. Leave sensor bosses (M3/M4 on thermoblock, tee for a thermocouple between heater and group head) in the chassis design from day one.
7. **Safety spec carries over:** piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing.

---

## 7. Reference Documents

**Reference documents (not redistributed in this repo — copyrighted; obtain from the original sources):**
- `Open Source Espresso Machine for Makers.pdf` — Zack Moss, University of Sheffield 2019. The master reference: EC685.M reverse engineering, temperature experiments, two prototypes, wiring diagram + Arduino code + part list (Appendix 2).
- `860382060-Part-list-final.docx` — thesis parts list with live 4delonghi.co.uk EC680 purchase links (£295 total).
- `EC885 Exploded View .pdf` — official exploded diagram + full part-code table (positions 01–77).
- `LA SPECIALISTA / Magnifica Data Sheet and Service Manual.pdf` — De'Longhi service test values.
- `DESIGB.pdf` — VDI 2221 portafilter redesign paper (method reference for documenting our own redesigns).

**Online:**
- [Makerspet OOMWOO BOM guide](https://makerspet.com/blog/how-to-source-bom-for-oomwoo-open-source-vacuum-robot/) — the sourcing-guide format this document follows
- [CaiJonas Dedica EC685/EC885 mod repo](https://github.com/CaiJonas/DeLonghi-Dedica-EC885-EC685-modification) — reversible pressure/temperature monitoring, sensor BOM
- Spares indexes: [espressocoffeeshop](https://spareparts.espressocoffeeshop.com/en/3901-de-longhi-ec685m-delonghi-dedica-parts) · [FixPart](https://fixpart.co.uk/coffee-machine-spare-parts/delonghi/ec685m-0132106138-dedica) · [4delonghi](https://www.4delonghi.co.uk/ec685m/catalogue.pl?path=316723&model_ref=13165954) · [eReplacementParts (US)](https://www.ereplacementparts.com/models/coffee-maker/delonghi/id1362996/ec685m/) · [Encompass (US)](https://delonghi.encompass.com/model/DEIEC685M) · [ulkapumps.com](https://ulkapumps.com/en-us)

---

## 8. Workflow (Milestone 1)

**M1 definition:** donor machine torn down, every part catalogued against the BOM, STEP library validated with printed check-fixtures, printed group-head housing bench-tested under pressure.

Work is not assigned to people — it is tracked as **GitHub issues** that anyone can pick up. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the scan → STL → STEP → chassis pipeline, naming rules and how to claim a task.

---

## 9. Next Steps

1. Pick mains voltage (230 V assumed below) and order a donor EC685 + wear-part kit (gaskets/O-rings/tubes ×2).
2. Tear down, photograph every stage, log each part against `BOM.md`.
3. Scan/measure per Section 5, build the STEP library.
4. Block out the two-zone chassis around the STEP assembly; print group-head housing first (highest risk part) and pressure-test it on the bench before designing the rest around it.
5. Decide Path 1 (OEM PCB) vs Path 2 (ESP32 + SSR) for v1 electronics.

*Find the master Bill of Materials in [BOM.md](BOM.md).*
