# WP-02 — designer brief, J2 package (plan only)

Job: 20260930-od-c03-pump-cradle · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.0 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c03_cradle_v01` · attempt 1 of 2 · fix_cycles 3 (not used in a J2 package)

## Package

A **J2 package**: run D0–D2 and return the plan `01_CAD/DESIGN_PLAN.md`. Build
nothing. The orchestrator checks that every spec feature (§4 C1) and every §5 gate
row has a planned feature and check before the J3 package is sent.

Two things the plan must settle by measuring the OD-H01 STEP (spec A-04, A-06):
which long edge of the sheet-metal frame carries its side plate (the U's spine) and
where the frame's corners sit, so that the saddle sector (θ 45° … 135°) and the
posts (inner faces at |x| = 29.5) keep ≥ 2.0 mm to every part of the pump; record
the measured frame extents in the plan's parameter table with their source. If the
spec's sector or post position cannot keep 2.0 mm, stop and report the measured
conflict (the orchestrator amends the spec; never change a spec value yourself).
Also report whether `validity(OD-H01)` reads sound, since U-03's boolean depends on it.

## Gate IDs to plan a check for (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b, D-04a, D-04c, D-06a, D-07 (N/A by its row), REQ-01 … REQ-09
(REQ-09 is a bench gate: the plan says so); plus `exactly_one_solid`,
`feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | the pump the cradle holds; same frame as the cradle (spec §2), placed at the identity pose (a joint at the origin, axis +Z). Measure it to record the frame extents (A-04) |
| `00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/params.json` | 21e02bf5c06fefb1f4fa9d4ade7810cfdcdc89ec533a29939c6aa624ba61c43c | the reverse-engineering parameters of the pump (INTAKE §2 rows X-01 … X-126) |
| `00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/README.md` | 52b06473b31a2365a638bf0daa993d2dfa32f1121a0caefbb74ff58c72657fa2 | the pump's frame definition and model tree |

The rubber sleeve OD-H02 has no input: the plan models it as the assumed solid of
spec A-03 (a tube ID 47.3, OD 53.3, z −6.0 … 32.0 on the pump axis) for the U-03
and REQ-04 checks, and names it as such.

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c03-pump-cradle` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/DESIGN_PLAN.md`. Library index: `library/INDEX.md`
(at most two cards). Tools documentation: `tools/README.md`.

## Findings to fix

None (first package).
