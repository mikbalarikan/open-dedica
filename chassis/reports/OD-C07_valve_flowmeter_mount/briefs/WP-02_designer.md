# WP-02 — designer brief, J2 package (plan only)

Job: 20260930-od-c07-valve-flowmeter-mount · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c07_mount_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md`. Build
nothing. The orchestrator checks that every spec feature (§4 C1) and every §5 gate
row has a planned feature and check before the J3 package is sent. Measure the two
reference solids at D1 as much as you need to plan the seats (their frames and the
values the spec carries as A-## rows); a spec value your measurement contradicts is
a question in the plan's §7, never a silent change.

## Gate IDs to plan a check for (spec §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04c, D-04d, D-05a, D-05b, D-06a, D-07
(N/A by its row), J-01, J-02, J-03, J-04, J-05, J-06 (N/A by its row), E-06,
REQ-01 … REQ-09; plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-H22_3way_valve.step` | bc0ffd003bcba248c7c8c4d68b198994726ee34b6c7e96ac97fbfd6490920028 | mating part, imported and placed by joint (spec §2 frame: its datum frame is the mount frame translated by (62.0, 0, 48.0)) |
| `00_Spec/inputs/OD-H24_flowmeter.step` | 1b4cbdafd03e0edafcc900b8c8c0894b382a48bd71850b59b06201a1fb45696a | mating part, imported and placed by joint (its datum frame is the mount frame translated by (0, 0, 10.0)) |
| `00_Spec/inputs/reports/OD-H22_3way_valve/PARAM_TABLE.md`, `params.json` | (hashed in `00_Spec/INTAKE_v01.md` §1) | the reverse-engineering parameters of OD-H22 with their rules and ± |
| `00_Spec/inputs/reports/OD-H24_flowmeter/params.json`, `tubes.json` | (hashed in `00_Spec/INTAKE_v01.md` §1) | the parameters of OD-H24 (pipes in `tubes.json`) |

Frames of the imported parts (from their reports): OD-H22 has z = 0 at its flange
back face with +Z toward the drive tube (the stem, gussets and ports are in −Z),
origin on the valve axis, +X through the ear holes, ports in the YZ plane. OD-H24
has z = 0 at its rim face with +Z toward the flange and connector (the base pins
are in −Z), origin on the cup axis, both pipes running toward −Y, the connector at
+X. Place both by measured features (the flange back face and ear holes; the rim
face, cup and pins), never by bounding boxes; confirm each frame by measurement
before you plan a seat on it.

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c07-valve-flowmeter-mount` with
`OGUZ_WORK=${OGUZ_WORK}`, `OGUZ_JOBS=${OGUZ_JOBS}` (`source $HOME/oguz.env`,
where OGUZ_JOBS=/root/oguz-jobs). Run any Python through
`uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/DESIGN_PLAN.md`. Library index: `library/INDEX.md`
(at most two cards). Tools documentation: `tools/README.md`.

## Findings to fix

None (first package).
