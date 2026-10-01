
## 6. Chassis Design Rules (learned from the thesis + OEM teardown)

1. **Two-zone layout.** Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) — the thesis literally used two boxes for prototype 1. In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB.
2. **Copy OEM anti-vibration.** Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter.
3. **Respect the thermal map.** Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural.
4. **Serviceability is the point.** The Dedica's worst trait (thesis: "very difficult to disassemble") is our biggest win: top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock.
