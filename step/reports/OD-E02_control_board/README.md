# OD-E02 Control button board — scan → STEP reverse-engineering report

![scan vs CAD overlay](qa/overlays/overlay.png)

| | |
|---|---|
| Part | `OD-E02` (ref 15, OEM 7313285189) — Front control button board of a DeLonghi espresso machine: stepped moulded housing with a snap-fitted back cover, PCB connector shroud, two screw holes, bent mounting tab, four latch hoops and three push-button caps (1 cup, 2 cups, steam), delivered as one fused solid of the assembly as scanned. |
| Input | [`scans/OD-E02_control_board/OD-E02_control_board_raw.stl`](../../../scans/OD-E02_control_board/) — full-resolution scan |
| Method | staged pipeline — intake → measure → build (build123d) → independent verifier → deliver |
| Caliper data | **none** — scan-only; units assumed mm |
| Status | **Owner-reviewed and accepted** (`DECISIONS.md`, `decisions/`) — tracked in #34 |

**Full report: [`deliver/README.md`](deliver/README.md)** · verifier report: [`qa/VERDICT.md`](qa/VERDICT.md).

## Delivered STEP

[`step/OD-E02_control_board.step`](../../OD-E02_control_board.step) — **use in CAD**. Datum frame: Intake: sha256 of the scan, working copy, noise floor on the mounting-tab top face, datum = back cover floor (XY), origin on the middle button collar axis, +X from the housing end face.

Same solid as the run's `build/OD-E02_control-button-board_datum.step`; only the STEP product / solid name was changed to `OD-E02 Control button board`, so sha256 values in `deliver/MANIFEST.json` refer to the run original. No scan-frame STEP is published — apply the inverse of `source/intake/alignment.json` to overlay the CAD on the raw scan.

Re-import check: 1 valid closed solid, 374 faces, volume 36,865.2 mm³, datum bbox 76.79 × 53.65 × 48.17 mm.

## Deviation (CAD ↔ scan)

| Direction | Measured |
|---|---|
| scan → CAD | p95 **0.237** / max 0.922 mm |
| CAD → scan (observable surface) | p95 0.633 / max 5.422 mm |

CAD → scan is dominated by surfaces the scanner never reached (bores, undersides, assembly interfaces); see `qa/VERDICT.md` for masks and clusters.

## Notes

- The run's reference photos were catalogue / web images and are **not redistributed**, so image links to `input/photos/` in the run documents are intentionally broken.
- Not copied from the run: meshes, STEP duplicates, NX files, deviation arrays and other files > 5 MB, superseded iterations.
- `deliverables/` of the run is at this folder's root; the run's `source/` (intake, measure, qa work files) is in [`source/`](source/).
