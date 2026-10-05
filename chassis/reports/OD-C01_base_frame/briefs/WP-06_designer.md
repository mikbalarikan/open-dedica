# WP-06 — designer brief, J3 package (build v03, spec 1.3, revision B)

Job: 20260930-od-c01-base-frame · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.3 (ratified 2026-10-05) · concept C1 (chosen) · target `od_c01_frame_v03` · revision B · build attempt 1 of 2 (the Usta ordered this round: halt_decision another_round, 2026-10-05) · fix_cycles 3

## Package

A **J3 package**: run D3–D9 against the plan `01_CAD/DESIGN_PLAN.md` with the notes of
`briefs/WP-03_designer.md` and `briefs/WP-04_designer.md` (part of the plan) and the
amendments below. Build v02 (`01_CAD/REPORT_od_c01_frame_v02.md`, reviewed RV01
`APPROVED_ASSUMPTION_CONDITIONAL`) is the starting point: copy your v02 scripts to
`_v03` names, change only what the amendments name, keep everything else (outline,
thickness, the twenty existing insert holes, feet, drains, the OD-C03/C04/G01 joints).
Export into `02_STEP_STL/od_c01_frame_C1_v03.step`, `02_STEP_STL/od_c01_assembly_C1_v03.step`,
`02_STEP_STL/od_c01_frame_C1_v03.stl`; sections with `_v03`; the sweep into
`01_CAD/sweep_v03/`; results into `01_CAD/check_od_c01_frame_v03.json`; the REPORT
into `01_CAD/REPORT_od_c01_frame_v03.md`. Leave every v01 and v02 file as it is. The
3MF is the orchestrator's step (report the STL's triangle count, volume and bounding
box). Return the block your skill defines. At the fix-cycle cap, or when a hard gate
cannot be met, stop with the measured failure (D9).

## Plan amendments (spec 1.3, checked by the orchestrator)

| Plan row | Amendment |
|---|---|
| Insert holes | **thirty-eight** Ø4.0 through-holes along Y (insert from the top, the existing convention): the twenty of v02 plus eighteen new ones. OD-C08 tray (REQ-11, A-18): (x 88.0, z −222.0), (106.0, −222.0), (88.0, −78.0), (106.0, −78.0). OD-C11 back panel (REQ-12, A-18): (±81.0, −282.0), (±95.0, −282.0). OD-C16 side-panel brackets (REQ-13, A-19): (±104.5, −262.0), (±104.5, −15.0), (±104.5, +62.0). OD-C09 front panel (REQ-14, A-20): (±85.0, +77.0), (±95.0, +77.0). U-05: 38 Ø4.0 + 4 Ø3.4 + 2 Ø8.0 = 44 bores; D-05a, D-05b, J-05 on all thirty-eight |
| Hole spacing (REQ-11 … REQ-14) | report, for every new hole, the nearest centre-to-centre distance to any other hole (≥ 6.0) and the distance to the plate's outline including the R 10 corner arcs (≥ 8.0) |
| Top face area (U-05 census) | rederive for 44 holes |
| Check assembly (U-03, 1.3 additions) | add the delivered parts in `00_Spec/inputs/` at their poses: `OD-C08_electronics_bay_tray.step`, `OD-C11_back_panel.step` and `OD-C09_front_panel.step` at the identity (modelled in this frame); `OD-C16_corner_bracket.step` six times: right side translate (117, 0, z_c), left side rotate 180° about Y (x → −X, y → Y, z → −Z) then translate (−117, 0, z_c), z_c ∈ {−262, −15, +62}. For each: designed contact with the plate top `clearance = 0`, `interference ≤ 0` mm³ with the plate, and each of its Ø3.4 plate-facing holes coaxial with the plate's Ø4.0 hole, offset ≤ 0.20 (`locate_bore` on both solids). Also check `OD-C07_valve_flowmeter_mount.step` (now delivered) against REQ-10's four holes by the A-17 joint the same way, and report it |
| Material (§3, A-10) | PLA, density 1240 kg/m³, for the mass figure; no geometry change |
| Zones (reported, not gated) | as v02; the electronics zone now holds OD-C08 (x 73 … 112, z −230 … −70) |
| Everything else | as v02 |

Spec 1.3 changed §1, §2 (four new input rows), §3, §4, U-03, U-05, D-05b, J-05, REQ-11 … REQ-14, A-08, A-10, A-12, A-18 … A-20; read the spec, not this table, where they differ.

## Gate IDs to check (spec §5)

U-01 … U-08 (U-08 N/A), D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-05a, D-05b,
D-06a, D-07 (N/A), J-05, E-06 (N/A), REQ-01 … REQ-14 (REQ-09 Soft bench:
INCONCLUSIVE, say so); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs and environment

As in `briefs/WP-02_designer.md` … `WP-04_designer.md`; your v02 scripts and REPORT.
New inputs (SHA-256):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-C07_valve_flowmeter_mount.step` | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c |
| `00_Spec/inputs/OD-C08_electronics_bay_tray.step` | 63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91 |
| `00_Spec/inputs/OD-C09_front_panel.step` | 0d688d24b7954e959291b171fa6e464dd30834e3f737eb73b696dfc992148ab5 |
| `00_Spec/inputs/OD-C11_back_panel.step` | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db |
| `00_Spec/inputs/OD-C16_corner_bracket.step` | 39faff6ce71326fc8d562d8c3daa42cd938fdf24f4dbe0933d82e9cae569c9fc |
| `00_Spec/inputs/reports/<part>/DESIGN_SPEC.md` for OD-C07, C08, C09, C11 and C12_C13_C16 | the neighbours' frames and hole definitions |

Run from the `oguz-atolye` root with `uv run tools/run.py python <script>`; the
environment variables `OGUZ_WORK`, `OGUZ_JOBS`, `OGUZ_DELIVERY`, `OGUZ_ARTIFACTS` must
be set (`source /home/claude/oguz-env.sh`). The workspace is
`${OGUZ_JOBS}/20260930-od-c01-base-frame`.

## Findings to fix

None from RV01 that change geometry (RV01 approved v02 on assumptions).
