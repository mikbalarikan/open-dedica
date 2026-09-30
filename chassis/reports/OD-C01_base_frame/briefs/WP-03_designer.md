# WP-03 — designer brief, J3 package (build v01)

Job: 20260930-od-c01-base-frame · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c01_frame_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan the orchestrator checked,
`01_CAD/DESIGN_PLAN.md` (D2, package WP-02), with the notes below. Write
`01_CAD/build_od_c01_frame.py` (parametric, every §4 parameter a named value) and
`01_CAD/check_od_c01_frame.py`. Export through `tools.core.write_step` (AP242) into
`02_STEP_STL/od_c01_frame_C1_v01.step`, the check assembly (plate + OD-C03 +
OD-C04 + OD-H01 + OD-H11 + OD-G01 v02 + the carrier foot box, as the plan places
them) into `02_STEP_STL/od_c01_assembly_C1_v01.step`, the STL into
`02_STEP_STL/od_c01_frame_C1_v01.stl`; re-import and measure; sections into
`03_Sections/` with `_v01` in their names; the sweep into `01_CAD/sweep_v01/`; the
check results into `01_CAD/check_od_c01_frame_v01.json`; the REPORT into
`01_CAD/REPORT_od_c01_frame_v01.md` with its JSON block. Return the block your
skill defines. At the fix-cycle cap, or when a hard gate cannot be met, stop with
the measured failure (D9). If the Write tool refuses a file, write it with Bash.

## Notes on the plan (checked by the orchestrator)

| Plan item | Note |
|---|---|
| U-07, 3MF clause | Do not write a 3MF. The orchestrator writes it from your STL with the project's own writer (as for OD-C03 and OD-C04) and verifies it by re-parsing; report the STL's triangle count, volume and bounding box in the REPORT so that check has its reference. Gate the sagitta clause normally and mark the 3MF clause "orchestrator step" in the JSON, not INCONCLUSIVE |
| min_wall / overhang_census spacing | 0.7 as the plan says; state the spacing in the REPORT beside every value it produced |
| K-1, K-2 (plan §7) | report OD-G01's lowest point (y 125.0 at the flange) and OD-H11's height above the plate (16.4925) in REPORT §7 as measured facts against the spec's §4 prose; no geometry change |
| OD-H11 | booleans INCONCLUSIVE by OD-C04 A-14; `clearance` gated (REQ-08 ≥ 10.0, U-03); if the assembly STEP writer refuses it, report U-04 per part and say so |
| Carrier foot box | a reference box x ±50, y 0 … 4, z −69.94 … −24.94 in the assembly, named `od_c05_foot_reference_A01`; not a solid of the deliverable |

Every value is the spec's; if a built value fails a Hard row, fix within the fix
cycles or stop with the measured failure; never change a spec value.

## Gate IDs to check (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b, D-04a, D-05a, D-05b, D-06a, D-07 (N/A by its row), J-05,
E-06 (N/A by its row), REQ-01 … REQ-09 (REQ-09 Soft bench: INCONCLUSIVE, say
so); plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

As in `briefs/WP-02_designer.md` (the five STEP files and the reports, hashes
there), plus your plan `01_CAD/DESIGN_PLAN.md`
(086dde812dcc207fa171977fb45f9d2ed5a8df324099bce8c813eb3651aa7217) and your
probes under `01_CAD/probe/` (reuse their placement code).

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c01-base-frame` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/REPORT.md`. Tools documentation: `tools/README.md`.
Precedent for the scripts' shape: `${OGUZ_JOBS}/20260930-od-c04-thermoblock-mount/01_CAD/`.

## Findings to fix

None (first build).
