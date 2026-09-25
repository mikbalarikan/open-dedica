# Contributing

All work is coordinated through **GitHub issues and pull requests** — no one is assigned by name. Anyone with the part (or the skills) can pick up a task.

## Workflow

1. **Find an issue.** Filter by phase label (`phase: scan`, `phase: step`, …). Scan requests follow the priority order: pump → thermoblock → group head → portafilter → water tank → valves → flowmeter → PCB → drip tray.
2. **Claim it.** Comment *"I'm taking this"* on the issue so nobody duplicates the work. A maintainer will assign you. If there is no progress for 14 days the issue goes back to the pool.
3. **Work on a branch / fork.** One part = one PR.
4. **Open a PR** that references the issue (`Closes #N`) and fill in the PR checklist.
5. **Review.** A maintainer checks against the issue's acceptance criteria; downstream issues (e.g. STEP rebuild) are opened as soon as a scan is merged — parts are released one at a time, not in batches.

## Naming

Every part has a project part number `OD-NNN` — see [docs/PART_NUMBERING.md](docs/PART_NUMBERING.md) and [docs/BOM.md](docs/BOM.md). Files and folders are named:

```
<part_no>_<short_name>          e.g.  OD-101_ulka_ep5_pump
```

A part that is missing from the BOM gets a number first: add it to `docs/bom.csv`, run `python tools/build_bom.py`, commit both.

## Phase 1 — scan deliverables (`scans/<part>/`)

| File | Content |
|---|---|
| `photos/` | Top, bottom, 4 sides + close-ups of every connector / mounting feature, **part on a grid mat or next to a ruler** |
| `calipers.md` | Caliper measurements of every interface: hole patterns, boss Ø, tube spigots, connector pitch, overall envelope (mm, 0.05 mm resolution). Include a sketch/photo with the dimensions marked. |
| `<name>_raw.stl` (or `.ply`) | Raw scan mesh, **in millimetres**, holes closed if possible. Keep ≤ 50 MB (GitHub hard limit is 100 MB) — decimate or zip if larger, or link an external download in the README. |
| `README.md` | Scanner / method (structured light, photogrammetry, …), scan spray used, known defects of the mesh |

**Rules**

- **Calipers beat scans on every interface.** Scans give us envelopes; calipers give us fits.
- Shiny / chrome / translucent parts: use removable matte scanning spray.
- Photogrammetry: 60–100 photos, even lighting, scale reference in frame.
- State the scan accuracy you believe the mesh has.

## Phase 2 — STEP deliverables (`step/`)

- Parametric rebuild over the mesh — **no raw-mesh STEP exports**. Tubes, gaskets and brackets can be modeled from calipers alone.
- STEP AP214, millimetres, file name per the naming scheme; name the CAD body/component `OD-NNN Name` too.
- Check-fixtures are named `OD-NNN-FX_<name>`.
- When a part moves to scanned / modeled / validated, update its `status` in `docs/bom.csv` in the same PR.
- Validate with a printed check-fixture (ring / cradle) against the real part; add a photo of the fit to the PR.

## Safety

Anything touching the wet side, heater or mains wiring must follow the rules in [docs/SOURCING_GUIDE.md §6](docs/SOURCING_GUIDE.md). PRs that remove the thermal cutoff or put PLA near heat will not be merged.
