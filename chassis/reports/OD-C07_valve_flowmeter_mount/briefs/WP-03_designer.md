# WP-03 — designer brief, J3 package (build)

Job: 20260930-od-c07-valve-flowmeter-mount · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c07_mount_v01` · build attempt 1 of 2 · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan the orchestrator checked,
`01_CAD/DESIGN_PLAN.md` (D2, package WP-02). Write the checks first
(`01_CAD/check_od_c07_mount.py`), then the build (`01_CAD/build_od_c07_mount.py`)
and the placement of OD-H22 and OD-H24 for the U-03, J-04 and REQ checks; export
through `tools.core.write_step` (AP242) into `02_STEP_STL/od_c07_mount_C1_v01.step`,
the check assembly (mount + OD-H22 + OD-H24 as placed) into
`02_STEP_STL/od_c07_assembly_C1_v01.step`, the STL into
`02_STEP_STL/od_c07_mount_C1_v01.stl`; re-import and measure; sections into
`03_Sections/`; the sweep into `01_CAD/sweep_v01/`; the REPORT into
`01_CAD/REPORT_od_c07_mount_v01.md` with its JSON block. Return the block your
skill defines. At the fix-cycle cap, or when a hard gate cannot be met, stop with
the measured failure (D9).

## Plan amendments (spec 1.1, checked by the orchestrator)

Your J2 plan `01_CAD/DESIGN_PLAN.md` is checked and stands. Its §7 questions Q1 … Q6
are answered in spec 1.1 (§4 C1, §5 rows U-03, U-05, U-06, D-01b, D-03a, D-03b,
REQ-02, REQ-03, REQ-04, REQ-09; §6 A-09, A-22; §7). Build to the amendments below
and list each as a deviation from the plan in REPORT §8; do not rewrite the plan.

| Plan row | Amendment |
|---|---|
| Q1 → P-1 (F11 stem opening) | accepted: a U-slot 14.1 wide through the deck, semicircular about the valve axis (62, 0) on its −Y side, straight walls at y ±7.05 open through the deck's +Y edge (y +15). The gusset slits leave the slot along ±X as before. No closed stem bore |
| U-03(b) OD-H22 path | slide along −Y at 0.5 above the seat (flange back face at z 48.5) from y +45 to y 0, then lower 0.5 onto the deck; ≥ 5 poses, `interference ≤ 0` mm³ against the mount. OD-H24's −Z path from 25 above stands |
| REQ-04 | deck top flat wherever it lies under the flange outline; slot check: `radial_profile` inner about (62, 0) over 180° … 360° at z 41 … 47 in [7.00, 7.10]; slits 2.40 ± 0.1 wide reaching x 62 ± 11.85 ± 0.1 |
| Q2 (F12 slits) | 2.40 wide (y ±1.20), top reach x 62 ± 11.85, taper 43.4° as planned; the deck wedge between each screw clearance hole and its slit end (1.79 / 1.90) is accepted: D-01b is now `min_wall ≥ 1.5`, U-06 wide ≥ 1.5. Report the wedge's own width from a section, since `min_wall` may not see it |
| Q3 → P-3 (F04 recess) | accepted: recess R 14.10, 0.60 deep, floor z 9.40, in the pedestal top; the pin holes open in its floor and are 9.4 ± 0.1 long (REQ-02); `clearance` recess to the OD-H24 ribs and hub ≥ 0.5 |
| Q4 → P-4 (F07 hook 3) | at θ 320° (REQ-03, A-09); confirm the catch lands on the flange top outside slots and windows and its distance to the pipes and connector |
| Q5 → P-5 (F05 notches) | accepted: three notches 2.0 wide × 0.5 high through the ring wall, z 10.0 … 10.5, at θ 25°, 115°, 225° (REQ-09); REQ-01's band z 10.5 … 12.5 is unaffected |
| Q6 (D-03a / D-03b) | the two insert-bore ceilings (Ø4.0) and the three notch ceilings (2.0) are bridges under D-03b; exclude them from D-03a by name in the check and say so in the REPORT |
| J-01 | ε = 1.5 · y · t / (L² · Q) with y = 20.37 − 18.87 = 1.5 from the STEP: 0.67 % expected; measure y, t, L on the built hooks |
| U-05 census | 1 plate window, 4 Ø3.4 footprint through-holes, 1 pedestal, 1 pedestal recess, 1 ring wall, 3 ring drain notches, 2 pin through-holes (Ø4.8, Ø3.8), 3 hooks, 2 legs, 1 deck, 1 stem U-slot, 2 gusset slits, 2 Ø3.4 screw clearance holes, 2 Ø4.0 insert bores |
| A-22 | new ledger row: the valve is held by its two ear screws only and slides out along +Y when they are loose; nothing to build, cite it in the REPORT where U-03(b) is reported |

The joints of plan §5 stand: OD-H24 datum frame = mount frame + (0, 0, 10.0);
OD-H22 datum frame = mount frame + (62.0, 0, 48.0). If the built mount still
overlaps either OEM solid at these poses, that is a FAIL to fix within the fix
cycles, or a stop with the measured overlap (D9), never a changed pose. The
notes of plan §7 (flange face area, ring overhang chamfer, fillet fallbacks)
stand as written.

## Gate IDs to check (spec §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04c, D-04d, D-05a, D-05b, D-06a, D-07
(N/A by its row), J-01, J-02, J-03, J-04, J-05, J-06 (N/A by its row), E-06,
REQ-01 … REQ-09; plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-H22_3way_valve.step` | bc0ffd003bcba248c7c8c4d68b198994726ee34b6c7e96ac97fbfd6490920028 | mating part, imported and placed by joint (spec §2: its datum frame is the mount frame translated by (62.0, 0, 48.0)) |
| `00_Spec/inputs/OD-H24_flowmeter.step` | 1b4cbdafd03e0edafcc900b8c8c0894b382a48bd71850b59b06201a1fb45696a | mating part, imported and placed by joint (its datum frame is the mount frame translated by (0, 0, 10.0)) |
| `00_Spec/inputs/reports/OD-H22_3way_valve/PARAM_TABLE.md`, `params.json` | (hashed in `00_Spec/INTAKE_v01.md` §1) | the reverse-engineering parameters of OD-H22 with their rules and ± |
| `00_Spec/inputs/reports/OD-H24_flowmeter/params.json`, `tubes.json` | (hashed in `00_Spec/INTAKE_v01.md` §1) | the parameters of OD-H24 (pipes in `tubes.json`) |
| `01_CAD/plan_probes_v01/probe_m1_v01.py` … `probe_m5_v01.py` | (yours, J2) | your D1 probes; reuse their placement code |

Frames of the imported parts (from their reports): OD-H22 has z = 0 at its flange
back face with +Z toward the drive tube (the stem, gussets and ports are in −Z),
origin on the valve axis, +X through the ear holes, ports in the YZ plane. OD-H24
has z = 0 at its rim face with +Z toward the flange and connector (the base pins
are in −Z), origin on the cup axis, both pipes running toward −Y, the connector at
+X. Place both by measured features (the flange back face and ear holes; the rim
face, cup and pins), never by bounding boxes.

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c07-valve-flowmeter-mount` with
`OGUZ_WORK=${OGUZ_WORK}`, `OGUZ_JOBS=${OGUZ_JOBS}` (`source $HOME/oguz.env`,
where OGUZ_JOBS=/root/oguz-jobs). Run any Python through
`uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/REPORT.md`. Library index: `library/INDEX.md` (at most two cards). Tools
documentation: `tools/README.md`.

## Findings to fix

None (first build). Deviations from the plan go in REPORT §8.
