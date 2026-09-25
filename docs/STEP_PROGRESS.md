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

In the overlays, grey is the rebuilt STEP and red is the raw scan. Where both show, the CAD sits on the scan surface.

| `OD-H01` ULKA EP5 pump: modeled | `OD-H11` Thermoblock: modeled | `OD-H24` Flowmeter: STEP rebuild in progress |
|---|---|---|
| ![OD-H01 pump STEP](img/progress/OD-H01_pump_cad.png) | ![OD-H11 thermoblock STEP vs scan](img/progress/OD-H11_thermoblock_overlay.png) | ![OD-H24 flowmeter STEP vs scan](img/progress/OD-H24_flowmeter_overlay.png) |
| [report](../step/reports/OD-H01_ulka_ep5_pump/) | [report](../step/reports/OD-H11_thermoblock/) | issue #7 |

Next up: a check-fixture for `OD-H01` and `OD-H11` (stage 4). Every part still marked `open` in stage 1 needs someone with the part to scan it. See [CONTRIBUTING.md](../CONTRIBUTING.md).
