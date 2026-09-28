# Scan → STEP progress

![Scan to STEP progress board](img/step_progress.svg)

The board is **generated** from the `status` column of [`bom.csv`](bom.csv). To move a part along, change its status (`todo` → `scanned` → `modeled` → `validated`) and run:

```
python tools/build_bom.py
python tools/build_progress.py
```

Commit `bom.csv`, `BOM.md` and `img/step_progress.svg` together. CI fails if the board is stale.

| Stage | Done when | Lives in |
|---|---|---|
| 1. Scan | Raw STL/PLY + `calipers.md` + photos merged | `scans/OD-Xnn_<name>/` |
| 2. STEP rebuild | Clean parametric STEP, not a mesh export | `step/OD-Xnn_<name>.step` |
| 3. Deviation gate | Two-way CAD ↔ scan deviation report | `step/reports/OD-Xnn_<name>/` |
| 4. Check-fixture | Printed fixture fits the real part (photo in PR) | `step/OD-Xnn-FX_<name>_fixture.step` |

## Work in progress

![Real part → 3D scan → open STEP](img/scan_to_step_showcase.png)

In the overlays, grey is the rebuilt STEP and red is the raw scan. Where both show, the CAD sits on the scan surface.

| `OD-H01` ULKA EP5 pump: modeled | `OD-H11` Thermoblock: modeled | `OD-H24` Flowmeter: modeled | `OD-H22` 3-way valve: modeled |
|---|---|---|---|
| ![OD-H01 ULKA EP5 pump](img/progress/OD-H01_pump_cad.png) | ![OD-H11 Thermoblock](img/progress/OD-H11_thermoblock_overlay.png) | ![OD-H24 Flowmeter](img/progress/OD-H24_flowmeter_overlay.png) | ![OD-H22 3-way valve](img/progress/OD-H22_3way_valve_overlay.png) |
| [report](../step/reports/OD-H01_ulka_ep5_pump/) | [report](../step/reports/OD-H11_thermoblock/) | [report](../step/reports/OD-H24_flowmeter/) | [report](../step/reports/OD-H22_3way_valve/) |

| `OD-G04` Brewing gasket support: modeled | `OD-S03` Steam knob: modeled | `OD-E01` Power PCB: modeled | `OD-E02` Control button board: modeled |
|---|---|---|---|
| ![OD-G04 Brewing gasket support](img/progress/OD-G04_brewing_gasket_support_overlay.png) | ![OD-S03 Steam knob](img/progress/OD-S03_steam_knob_overlay.png) | ![OD-E01 Power PCB](img/progress/OD-E01_power_pcb_overlay.png) | ![OD-E02 Control button board](img/progress/OD-E02_control_board_overlay.png) |
| [report](../step/reports/OD-G04_brewing_gasket_support/) | [report](../step/reports/OD-S03_steam_knob/) | [report](../step/reports/OD-E01_power_pcb/) | [report](../step/reports/OD-E02_control_board/) |

| `OD-S01` Steam valve: modeled | `OD-S02` Steam wand: modeled | `OD-W03` Tray gasket (tank seat): modeled | `OD-G09` Group head bayonet cup: modeled |
|---|---|---|---|
| ![OD-S01 Steam valve](img/progress/OD-S01_steam_valve_overlay.png) | ![OD-S02 Steam wand](img/progress/OD-S02_steam_wand_overlay.png) | ![OD-W03 Tray gasket (tank seat)](img/progress/OD-W03_tank_seat_overlay.png) | ![OD-G09 Group head bayonet cup](img/progress/OD-G09_group_head_bayonet_cup_overlay.png) |
| [report](../step/reports/OD-S01_steam_valve/) | [report](../step/reports/OD-S02_steam_wand/) | [report](../step/reports/OD-W03_tank_seat/) | [report](../step/reports/OD-G09_group_head_bayonet_cup/) |

| `OD-G10` Portafilter: modeled | `OD-H21` Anti-drip valve: modeled |
|---|---|
| ![OD-G10 Portafilter](img/progress/OD-G10_portafilter_overlay.png) | ![OD-H21 Anti-drip valve](img/progress/OD-H21_antidrip_valve_overlay.png) |
| [report](../step/reports/OD-G10_portafilter/) | [report](../step/reports/OD-H21_antidrip_valve/) |

## Parts on the scanner

Donor parts on the scan turntable, matched to BOM numbers. All matches are confirmed.

![Donor parts matched to BOM numbers](img/donor_parts_bom.png)

![Donor parts matched to BOM numbers, electronics and steam valve](img/donor_parts_bom_2.png)

Next up: check-fixtures for every modeled part (stage 4). Every part still marked `open` in stage 1 needs someone with the part to scan it. See [CONTRIBUTING.md](../CONTRIBUTING.md).
