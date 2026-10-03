# docs/SOURCING_GUIDE.md section 6 (verbatim excerpt)
215:## 6. Chassis Design Rules (learned from the thesis + OEM teardown)

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

