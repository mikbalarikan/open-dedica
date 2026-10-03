# WP-05 — designer brief, J3 package (build v02)

Job: 20261002-od-t01-pressure-test-rig · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.3 (ratified 2026-10-03 by the Usta's decision; SHA-256 9f329e11a2b8eba3921e81eddcc593e203550b65c65d588e11b2d9bb11330195) · concept C1 · target `od_t01_rig_v02` · build attempt 2 of 2 · fix_cycles 3

## Package

A **J3 package**: rebuild the rig to spec 1.3 from your v01 scripts
(`01_CAD/build_od_t01_rig.py`, `check_od_t01_rig.py`, `sweep_od_t01_rig.py`,
`sections_od_t01_rig.py`) and plan `01_CAD/DESIGN_PLAN.md` (SHA-256
544bde71e61f60d81c0d2c6b3868a6d9a017457f29aa9d5d96560a5212c10a5d). Keep v01's
files untouched; write v02 outputs beside them: `02_STEP_STL/od_t01_rig_C1_v02.step`,
`.stl`, `02_STEP_STL/od_t01_assembly_C1_v02.step`; sections `03_Sections/*_v02*`;
sweep into `01_CAD/sweep_v02/`; gates `01_CAD/gates_od_t01_rig_v02.json`; the REPORT
`01_CAD/REPORT_od_t01_rig_v02.md` answering every §5 row of spec 1.3 and the §P list,
with a short delta section against v01.

## What changed (spec 1.3, §7 and §8; review `reviews/RV01_od_t01_rig_v01.md`)

- **RV01 F1 (MEDIUM, REQ-08):** the top plate is **25.0 thick, y 135.0 … 160.0**
  (was 150.0). The four Ø6.5 counterbores run from **y 160.0 to y 140.00 ± 0.10**,
  leaving **5.0 ± 0.1** of plate under each head (M3 × 10 ISO 7380). Envelope
  **240 × 160 × 120**. REQ-07's driver cylinders run y 160 … 300. Report the hand
  numbers of spec §4 (window section Z 4948 mm³, σ ≈ 9.6 MPa) against your
  measured section at x 0.
- **RV01 F2 (LOW, REQ-03):** apex band ± 0.16.
- Everything else (walls, base, window R 30, teardrops at 45.1°, bench holes,
  chamfers) is unchanged; re-run every gate, the sweep included, on v02.

## Gate IDs (spec 1.3 §5)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A), D-01a,
D-01b, D-02, D-03a, D-03b, D-04a, D-06a, D-07 (N/A), J-05 (N/A), REQ-01 … REQ-07,
REQ-08 (Soft, bench); plus `exactly_one_solid`, `feature_census`,
`envelope_within_spec`.

## Inputs

As WP-02 (same files and SHA-256 values in `00_Spec/inputs/`).

## Environment

Workspace: `/root/oguz-jobs/20261002-od-t01-pressure-test-rig`. Run
`source /root/oguz-env/env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Traps:
`library/BUILD123D-NOTES.md`. Write only under `01_CAD/`, `02_STEP_STL/`,
`03_Sections/`. Do not call any mcp__hearthbot__ tool. If a file write is blocked
by a hook, return the file's full text in your answer instead.

## Findings to fix

RV01 F1 and F2, as above.
