# WP-05 — designer brief, J3 package (build v02, the round after RV01)

Job: 20260930-od-c03-pump-cradle · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c03_cradle_v02` · build attempt 1 of 2 (counters reset by the REVISE round) · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan the orchestrator checked,
`01_CAD/DESIGN_PLAN.md` (D2, package WP-02), with the amendments of
`briefs/WP-03_designer.md` (spec 1.1, built as v01) and the amendments below
(spec 1.2). Start from your own v01 scripts `01_CAD/check_od_c03_cradle.py` and
`01_CAD/build_od_c03_cradle.py`: change the parameters the amendments name,
keep everything else. Export through `tools.core.write_step` (AP242) into
`02_STEP_STL/od_c03_cradle_C1_v02.step`, the check assembly into
`02_STEP_STL/od_c03_assembly_C1_v02.step`, the STL into
`02_STEP_STL/od_c03_cradle_C1_v02.stl`; re-import and measure; sections into
`03_Sections/` with `_v02` in their names; the sweep into `01_CAD/sweep_v02/`;
the check results into `01_CAD/check_od_c03_cradle_v02.json`; the REPORT into
`01_CAD/REPORT_od_c03_cradle_v02.md` with its JSON block. Leave every v01 file as
it is. Return the block your skill defines. At the fix-cycle cap, or when a hard
gate cannot be met, stop with the measured failure (D9). If the Write tool
refuses a file, write it with Bash.

## Plan amendments (spec 1.2, checked by the orchestrator)

The plan and the WP-03 amendments stand, except these rows from spec 1.2 (its
§4 C1, §5 REQ-01, REQ-02, REQ-05, REQ-06, REQ-09, and §8). Build to them and
list each as a deviation from the plan in REPORT §8; do not rewrite the plan.

| Plan row | Amendment |
|---|---|
| rib1_z0 | rib 1 over z −3.0 … 3.0 (under the pump's centre of mass at z 7.2, RV01 F2); rib 2 stays z 25.0 … 31.0; rib faces at z −3.0, 3.0, 25.0, 31.0 (REQ-02) |
| REQ-01 windows | `radial_profile` over θ 50° … 130° at every 5°, z −2.5 … 2.5 and 25.5 … 30.5 |
| REQ-02 sections | at z 0.0 and z 28.0: inner ≤ 26.70 at θ 50° / 130°, no material within r ≤ 32.0 at θ 40° / 140° (INCONCLUSIVE "no material" recorded as such; positive control: the post at r 38.51 on the whole ray) |
| post_w block | post blocks span z 12.0 … 33.0 (inner face |x| 29.5, 4.0 thick, top y 0.0 unchanged; REQ-06) |
| slots | centres at y 7.0 and z 17.0 / 28.0 (REQ-05); clear 6.0 (Z) × 2.5 (Y), 45° gable roofs, ligament ≥ 2.0 beside each slot as before |
| REQ-09 | Soft in spec 1.2: report it INCONCLUSIVE (bench), never as a hard failure |
| §6 census | unchanged: 2 saddle ribs, 2 post blocks, 4 slots, 4 Ø3.4 through-holes, 1 foot plate |

Rib 1 at z −3 … 3 sits inside the sleeve span (A-03: z −6.0 … 32.0) and opposite
the −Y side features (spade tabs z ≤ 5.5, slot box z ≤ 13.6, all on the −Y side,
plan §2a): the web and rib lie on the +Y side over θ 45° … 135°. If the built
cradle reads under 2.0 to OD-H01 anywhere, or rib 1 meets an OD-H01 feature, that
is a FAIL to fix within the fix cycles, or a stop with the measured clearance
(D9), never a changed spec value. The OD-H01 joint (identity at the origin, axis
+Z) and the A-03 sleeve solid (`od_h02_sleeve_assumed_A03`, ID 47.3, OD 53.3,
z −6.0 … 32.0, cut to |x| ≤ 23.5) stand.

## Gate IDs to check (spec §5)

U-01, U-02, U-03, U-04, U-05, U-06, U-07, U-08 (N/A by its row), D-01a, D-01b,
D-02, D-03a, D-03b, D-04a, D-04c, D-06a, D-07 (N/A by its row), REQ-01 … REQ-09
(REQ-09 Soft bench: INCONCLUSIVE, say so); plus `exactly_one_solid`,
`feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-H01_ulka_ep5_pump.step` | b05302af204c225fbf6bab0476ead4e0b185527d184a055006fd367550c3fb62 | the pump, placed at the identity pose by a joint at the origin, axis +Z (sound: validity 1/1/0, plan §2a) |
| `00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/params.json` | 21e02bf5c06fefb1f4fa9d4ade7810cfdcdc89ec533a29939c6aa624ba61c43c | the pump's parameters |
| `00_Spec/inputs/reports/OD-H01_ulka_ep5_pump/README.md` | 52b06473b31a2365a638bf0daa993d2dfa32f1121a0caefbb74ff58c72657fa2 | the pump's frame definition |
| `01_CAD/REPORT_od_c03_cradle_v01.md` | (v01, for reference) | your v01 REPORT; v02 changes only what the amendments name |

## Environment

Workspace: `${OGUZ_JOBS}/20260930-od-c03-pump-cradle` with `OGUZ_WORK=${OGUZ_WORK}`,
`OGUZ_JOBS=${OGUZ_JOBS}` (`source /home/claude/oguz-env.sh`). Run any Python
through `uv run tools/run.py python <script>` from the repository root
`/home/claude/oguz-atolye` (build123d 0.11.1, OCCT 7.9.3 in the tools venv).
Templates: `atolye/templates/REPORT.md`. Tools documentation: `tools/README.md`.

## Findings to fix (RV01, `reviews/RV01_od_c03_cradle_v01.md` §6)

| Finding | What v02 does |
|---|---|
| F1 REQ-09 Hard INCONCLUSIVE (blocking) | spec 1.2 makes the row Soft; report INCONCLUSIVE with the bench note |
| F2 centre of mass at z 7.23 ahead of the saddles (MEDIUM) | rib 1 moved to z −3 … 3 so the saddle span brackets the centre of mass; report the centre of mass of OD-H01 against the span z −3 … 31 in REPORT §7 |
| F3 tie loop crosses the side plates (MEDIUM) | carried in spec A-07; no geometry change; note it in REPORT §7 |
| F4 REQ-04 zero-gap only at r 26.650 (MEDIUM) | carried in A-03; keep r 26.65 exactly; no change |
| F5 REQ-03 margin 0.300 under the scan p95 (MEDIUM) | carried in A-01, A-04; no change; report the measured clearance and nearest points |
| F6 zero-margin ligaments and slot section (LOW) | by the spec's own values; no change |
