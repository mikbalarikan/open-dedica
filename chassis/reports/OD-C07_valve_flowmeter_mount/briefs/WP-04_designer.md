# WP-04 — designer brief, J3 package (build, second attempt)

Job: 20260930-od-c07-valve-flowmeter-mount · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 (chosen) · target `od_c07_mount_v01` · build attempt 2 of 2 · fix_cycles 3

## Package

A **J3 package** on the same target and the same geometry: your v01 build
(package WP-03, REPORT `01_CAD/REPORT_od_c07_mount_v01.md`) stopped on U-03(b)
alone, and spec 1.2 answers it by changing the assembly path, not the part. Do
not rebuild or move any feature. Update the check script to spec 1.2, re-run the
whole check on the exported `02_STEP_STL/od_c07_mount_C1_v01.step` and the
assembly, re-run the sweep only if the check script's rows changed for the swept
parameters (they do: the bands below), regenerate the two assembly sections if the
poses in them change, and write `01_CAD/REPORT_od_c07_mount_v02.md` with its JSON
block (v01 stays on disk as the record of the stop). The STEP, STL and build script
are unchanged unless a re-run shows a real geometry fault; if it does, that is a fix
cycle, reported as such. Return the block your skill defines. At the fix-cycle cap,
or when a hard gate cannot be met, stop with the measured failure (D9).

## Findings to fix (spec 1.2)

| Finding | Change |
|---|---|
| U-03(b): the −Y slide at +0.5 runs the gussets through the deck arms (15.197 mm³, y +12 … +2) | spec 1.2 U-03(b): OD-H22 slides along −Y at 5.0 above the seat (flange back face at z 53.0) from y +45 to y 0, then lowers 5.0 along −Z onto the deck; ≥ 5 poses on the slide, ≥ 3 on the drop (for example z offsets 5.0, 3.0, 1.0, 0), `interference ≤ 0` mm³ against everything; report the least clearance along the slide (your measurement: 0 mm³, 0.858 at h 5.0) |
| Sweep: ring_ri, pin1_d, pin2_d, slot_w, slit_x_top fail the 0.5 clearance at their lower tolerance end | spec 1.2 makes those bands one-sided: REQ-01 ring inner R in [16.30, 16.40]; REQ-02 Ø4.8 +0.1/−0 and Ø3.8 +0.1/−0; REQ-04 slot width 14.1 +0.1/−0, `radial_profile` band [7.05, 7.10], straight walls y ±(7.05 +0.05/−0), slit reach 62 ± (11.85 +0.1/−0). Update the check rows and sweep those parameters at the new ends (nominal is now the low end) |
| Hook 320° catch 4.94 from the OD-H24 connector against A-09's 5 | accepted in spec 1.2 (A-09 note): the gate is D-04c ≥ 0.5; report the value, no change |
| REPORT §4 "passes only at nominal" for ped_top_z, catch_under_z, deck_top_z, deck_t, leg_gap_half, recess_r | no spec change: seat heights against fixed OEM poses and the leg/window edge are designed contacts; keep the finding in REPORT v02 §4 and §9 for the reviewer |

Everything else in spec 1.1 stands (WP-03's amendments table). Deviations from
the plan carry over from REPORT v01 §8.

## Gate IDs to check (spec §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its row),
D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-04c, D-04d, D-05a, D-05b, D-06a, D-07
(N/A by its row), J-01, J-02, J-03, J-04, J-05, J-06 (N/A by its row), E-06,
REQ-01 … REQ-09; plus `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs (paths relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `00_Spec/inputs/OD-H22_3way_valve.step` | bc0ffd003bcba248c7c8c4d68b198994726ee34b6c7e96ac97fbfd6490920028 | mating part, placed at mount frame + (62.0, 0, 48.0) |
| `00_Spec/inputs/OD-H24_flowmeter.step` | 1b4cbdafd03e0edafcc900b8c8c0894b382a48bd71850b59b06201a1fb45696a | mating part, placed at mount frame + (0, 0, 10.0) |
| `02_STEP_STL/od_c07_mount_C1_v01.step` | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c | your v01 export, unchanged |
| `01_CAD/check_od_c07_mount.py`, `build_od_c07_mount.py`, `sweep_od_c07_mount.py`, `sections_od_c07_mount.py`, `report_od_c07_mount.py` | (REPORT v01 §1) | your J3 scripts; edit the check (and the sweep bands) only |

## Environment

As WP-03: workspace `${OGUZ_JOBS}/20260930-od-c07-valve-flowmeter-mount`
(`source $HOME/oguz.env`, OGUZ_JOBS=/root/oguz-jobs); Python through
`uv run tools/run.py python <script>` from `/home/claude/oguz-atolye`.
Templates: `atolye/templates/REPORT.md`. Tools documentation: `tools/README.md`.
