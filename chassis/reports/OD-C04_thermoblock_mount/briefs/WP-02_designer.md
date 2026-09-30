# WP-02 — designer brief, J2 package (plan only)

Job: 20260930-od-c04-thermoblock-mount · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c04_mount_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md`. Build
nothing. The orchestrator checks that every spec feature (§4 C1) and every §5 gate
row has a planned feature and check before the J3 package is sent.

Things the plan must settle by measuring the OD-H11 STEP (spec A-02, A-03, A-06):
for each of the two blind screw holes, the face it opens on and the direction it
opens toward (use `bore_census` and `locate_bore`; a hole that opens toward +Z
cannot be reached from the rear plate: stop and report it, since the spec must
change); the z of that face, so the standoff tip sits 10.0 mm short of it (REQ-03);
the thermoblock's rearmost surface (its base face at z = 0 and anything below it),
so the plate's front face at z −12.0 keeps REQ-01; and the radial extent of the
pads at θ 262.5° and 339.0°. Also report whether `validity(OD-H11)` reads sound,
since U-03's boolean depends on it. If any spec value cannot be met, stop and report
the measured conflict; never change a spec value yourself.

## Gate IDs to plan a check for (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b, D-04a, D-06a, D-07 (N/A by its row), E-06, REQ-01 … REQ-08
(REQ-08 is a bench gate: the plan says so); plus `exactly_one_solid`,
`feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038f | the thermoblock the mount holds; same frame as the mount (spec §2), placed at the identity pose (a joint at the origin, axis +Z). Measure it for A-03 and REQ-01 |
| `00_Spec/inputs/reports/OD-H11_thermoblock/params.json` | 46f1b43a54e82c08a96b2463d88622e9d5a5ae71245ccc3440c1d960ba1c520 | the reverse-engineering parameters (INTAKE §2 rows X-01 … X-50) |
| `00_Spec/inputs/reports/OD-H11_thermoblock/ports.json` | 77fbb8b2a53e929216ddea4752a7b18e67f6f57ba1ba3864ec24e179cf224fd | pipe and terminal axes (INTAKE X-51 … X-84) |
| `00_Spec/inputs/reports/OD-H11_thermoblock/README.md` | 61061c517ac0c20dfe1fa86a5e75dbf959eb52d272a843b2c613d77da4dddec | the thermoblock's frame definition and feature tree |

The spacers (spec A-05) have no input: the plan models each as a solid Ø7.0 × 10.0
with a Ø4.0 bore, seated on the standoff tip and the thermoblock's face, for the
U-03 and REQ-03 checks, and names them as such.

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c04-thermoblock-mount` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/DESIGN_PLAN.md`. Library index: `library/INDEX.md`
(at most two cards). Tools documentation: `tools/README.md`.

## Findings to fix

None (first package).
