# OD-S02 Steam wand (steam hose assembly + nozzle) — scan → STEP reverse-engineering report

![scan vs CAD overlay](qa/overlays/overlay_it2_extra.png)

| | |
|---|---|
| Part | `OD-S02` (ref 10 + 77, OEM AS00002705 + AS00002710) — Coffee-machine steam wand assembly (black connector rod with O-ring seats, knob with lever paddle, sleeve and sealing band, bent steel tube, white bushing, steel tip), scanned as one mesh and delivered as ONE fused solid (owner decision). |
| Input | [`scans/OD-S02_steam_wand/OD-S02_steam_wand_raw.stl`](../../../scans/OD-S02_steam_wand/) — full-resolution scan |
| Method | staged pipeline — intake → measure → build (build123d) → independent verifier → deliver |
| Caliper data | **none** — scan-only; units assumed mm |
| Status | **Owner-reviewed and accepted** (`DECISIONS.md`, `decisions/`) — tracked in #36 |

> **Part number:** Scanned and modeled as one fused solid: the steam hose assembly (bent steel tube, white ball-joint seal, tip) together with the nozzle `OD-S04` (black elbow, knob paddle, tapered connector).

**Full report: [`deliver/README.md`](deliver/README.md)** · verifier report: [`qa/VERDICT.md`](qa/VERDICT.md).

## Delivered STEP

[`step/OD-S02_steam_wand.step`](../../OD-S02_steam_wand.step) — **use in CAD**. Datum frame: Datum: rod spigot axis is +Z (axis primary, section-circle refined cone fit), origin on the knob top face, the steel tube leaving the elbow clocks +X.

Same solid as the run's `build/OD-S02_steam-rod_datum.step`; only the STEP product / solid name was changed to `OD-S02 Steam wand (steam hose assembly + nozzle)`, so sha256 values in `deliver/MANIFEST.json` refer to the run original. No scan-frame STEP is published — apply the inverse of `source/intake/alignment.json` to overlay the CAD on the raw scan.

Re-import check: 1 valid closed solid, 122 faces, volume 13,753.5 mm³, datum bbox 71.64 × 25.22 × 125.19 mm.

## Deviation (CAD ↔ scan)

| Direction | Measured |
|---|---|
| scan → CAD | p95 **0.236** / max 0.737 mm |
| CAD → scan (observable surface) | p95 0.766 / max 2.601 mm |

**Per zone:**

| Zone | Measured |
|---|---|
| Z1 rod spigot taper + O-ring seats:scan_to_cad | p95 0.131 / max 0.565 |
| Z1 rod spigot taper + O-ring seats:cad_to_scan | p95 0.133 / max 0.693 |
| Z2 steel tube B-bend-C:scan_to_cad | p95 0.229 / max 0.580 |
| Z2 steel tube B-bend-C:cad_to_scan | p95 0.214 / max 0.345 |
| Z3 lever paddle:scan_to_cad | p95 0.134 / max 0.247 |
| Z3 lever paddle:cad_to_scan | p95 0.130 / max 0.235 |
| Z4 bushing + tip:scan_to_cad | p95 0.301 / max 0.737 |
| Z4 bushing + tip:cad_to_scan | p95 1.063 / max 2.602 |

CAD → scan is dominated by surfaces the scanner never reached (bores, undersides, assembly interfaces); see `qa/VERDICT.md` for masks and clusters.

## Notes

- Own photos are in [`scans/OD-S02_steam_wand/photos/`](../../../scans/OD-S02_steam_wand/photos/).
- Not copied from the run: meshes, STEP duplicates, NX files, deviation arrays and other files > 5 MB, superseded iterations.
- `deliverables/` of the run is at this folder's root; the run's `source/` (intake, measure, qa work files) is in [`source/`](source/).
