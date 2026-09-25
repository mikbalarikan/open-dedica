# OD-S03 Steam knob — scan → STEP reverse-engineering report

![scan vs CAD overlay](qa/overlays/overlay_z.png)

| | |
|---|---|
| Part | `OD-S03` (ref 13, OEM 7313285479) — steam-valve knob: chrome cap with lever and drafted slot pocket, chrome collar, white four-rib stem, chrome threaded sleeve with splined bore (phase 2 — steam) |
| Input | [`scans/OD-S03_steam_knob/OD-S03_steam_knob_raw.stl`](../../../scans/OD-S03_steam_knob/) — 363 988 triangles, full resolution |
| Method | staged pipeline — intake → measure → build (build123d, features F01–F15: drafted cap + lever, loop fillets, pocket, collar / stem / spigot revolves, 4 ribs, helical end ramps) → **independent verifier** → deliver. **Iteration 2 of 3.** |
| Caliper data | **none** — scan-only; units assumed mm, scale not verified |
| Verdict | **`BAND_NOT_MET` — accepted by the owner for delivery** ([`decisions/accept_band.md`](decisions/accept_band.md)) |

**Full report: [`deliver/README.md`](deliver/README.md)** · verifier report: [`qa/VERDICT.md`](qa/VERDICT.md).

> The run's five reference photos are seller / catalogue images and are **not redistributed** here, so image links to `input/photos/` in the run documents are intentionally broken.
> Not copied either: meshes, `qa/dev_arrays.npz` (15 MB), the superseded iteration 1 (`_it1_SUPERSEDED/`), and the `skill_scripts/` helpers that `build/model.py` imports (`export_frames`) — so `model.py` does not run from this folder alone.

## Delivered STEP

| File in this repo | = file in the run | Frame |
|---|---|---|
| [`step/OD-S03_steam_knob.step`](../../OD-S03_steam_knob.step) — **use in CAD** | `build/OD-S03_steam-knob_datum.step` | datum: cap crown face = Z 0 (+Z toward the sleeve), origin on the sleeve / cap axis, lever toward +X |
| *(not published)* | `build/OD-S03_steam-knob.step` | original scan coordinates — apply the inverse of `intake/alignment.json` to the datum STEP to overlay it on the raw scan |

The repo copy differs from the run file only in the STEP product / solid name (`OD-S03 Steam knob`), so the sha256 values in `deliver/MANIFEST.json` refer to the run original.

Re-import check: 1 valid closed solid, 83 faces, volume 11 655.6 mm³, datum bbox 40.96 × 26.44 × 38.10 mm.

## Deviation gate (independent verifier)

| Gate | Band | Measured | Result |
|---|---|---|---|
| scan → CAD (masked) | p95 ≤ 0.30 / max ≤ 0.80 | p95 **0.150** / max 2.35 | FAIL (max only) |
| CAD → scan (observable) | p95 ≤ 0.30 / max ≤ 0.80 | p95 0.438 / max 2.79 | FAIL |
| Z1 threaded sleeve OD | both directions | p95 0.188 / 0.182 | **PASS** |
| Z2 sleeve bore (visible) | both directions | p95 0.168 / 0.169 | **PASS** |
| Z3 stem ribs + core | both directions | p95 0.158 / 0.213 | **PASS** |
| Z4 crown, cap wall, lever | scan → CAD / CAD → scan | p95 0.111 / 0.104, max 2.35 | FAIL (max only) |
| Z5 step face + collar | both directions | p95 0.140 / 0.137 | **PASS** |

- **Best surface fit so far:** scan → CAD p95 **0.150 mm**, and every functional zone passes p95.
- The max 2.35 mm is a scan artefact — a chrome "skin flap" inside the cap wall at a scan-hole edge; the part itself has an intact wall.
- A real non-rotational crevice at the stem / collar (θ ≈ 300°) is modeled as one revolved groove.
- CAD → scan fails on the assumed lever-pocket floor and bore floor, which the scanner never reached.
- The internal splines of the sleeve bore are beyond the scanned depth and are **not modeled**.

Phase 2 part (steam system is not in v1). Before designing the front panel / steam-knob opening, confirm with calipers: sleeve thread OD and pitch, bore Ø and spline count, cap OD, overall height.

## Folder map

`intake/` datum + alignment · `measure/` `params.json`, `PARAM_TABLE.md`, figures + scripts · `build/` `model.py`, `MODELING_PLAN.md`, export checks · `qa/` verdict, gate, deviation, zone probes, overlays, QA scripts · `decisions/`, `DECISIONS.md` owner decisions · `deliver/` report, manifest, limitations, repro · `input/` input hashes (photos withheld).
