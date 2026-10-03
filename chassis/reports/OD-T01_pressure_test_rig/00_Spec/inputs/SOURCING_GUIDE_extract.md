# docs/SOURCING_GUIDE.md lines 40-70
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

# docs/SOURCING_GUIDE.md lines 240-260

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
