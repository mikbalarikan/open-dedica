# Contributing

All work is coordinated through **GitHub issues and pull requests** — no one is assigned by name. Anyone with the part (or the skills) can pick up a task.

## Workflow

1. **Find an issue.** Filter by phase label (`phase: scan`, `phase: step`, …). Scan requests follow the priority order: pump → thermoblock → group head → portafilter → water tank → valves → flowmeter → PCB → drip tray.
2. **Claim it.** Comment *"I'm taking this"* on the issue so nobody duplicates the work. A maintainer will assign you. If there is no progress for 14 days the issue goes back to the pool.
3. **Work on a branch / fork.** One part = one PR.
4. **Open a PR** that references the issue (`Closes #N`) and fill in the PR checklist.
5. **Review.** A maintainer checks against the issue's acceptance criteria; downstream issues (e.g. STEP rebuild) are opened as soon as a scan is merged — parts are released one at a time, not in batches.

## Naming

Everything is keyed to the ref# and OEM code from the EC885.M exploded view / [docs/BOM.md](docs/BOM.md):

```
<ref#>_<code>_<short_name>          e.g.  40_AS00002825_ulka_ep5_pump
```

Use `xx` for ref# and `open` for code on parts that are ours (e.g. `xx_open_group_head_housing`).

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
- STEP AP214, millimetres, file name per the naming scheme.
- Validate with a printed check-fixture (ring / cradle) against the real part; add a photo of the fit to the PR.

## Safety

Anything touching the wet side, heater or mains wiring must follow the rules in [docs/SOURCING_GUIDE.md §6](docs/SOURCING_GUIDE.md). PRs that remove the thermal cutoff or put PLA near heat will not be merged.
