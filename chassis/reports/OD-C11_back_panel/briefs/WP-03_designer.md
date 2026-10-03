# WP-03 — designer brief, J3 package (build v02)

Job: 20261001-od-c11-back-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.1 (ratified 2026-10-01; 1.0 kept as `00_Spec/DESIGN_SPEC_v1.0.md`) · concept C1 · target `od_c11_back_v02` · build attempt 2 of 2 · fix_cycles 3

## Package

The second build. Your v01 plan (`01_CAD/DESIGN_PLAN.md`) stands except where
spec 1.1 changes it; write the changes as `01_CAD/DESIGN_PLAN_v02.md` (a short
amendment, not a rewrite). Spec 1.1 answers your v01 question and the driver
fact: the floor flanges now span x ±(72.0 … 104.0) and z −299.0 … −277.0 (22
deep), clear of the feet holes; the flange holes move to (x ±81.0, z −282.0) and
(x ±95.0, z −282.0), 5.0 in front of the ledge, so a straight Ø6 driver reaches
each from above (REQ-08 now runs to y 260); the outer gussets move to
x ±(100.0 … 104.0); the envelope is 232 × 215 × 25; U-03 (a) now reads the
footprint ≥ 3.0 from the edge of every existing OD-C01 hole; REQ-05's tank-zone
box starts at z −298.8. Everything else is unchanged.

Rebuild with the same scripts, versioned (`build_od_c11_back_v02.py`,
`check_od_c11_back_v02.py`, or parameters bumped with the v02 tag), export into
`02_STEP_STL/od_c11_back_C1_v02.step`, `od_c11_assembly_C1_v02.step`,
`od_c11_back_C1_v02.stl`; sections `_v02`; sweep into `01_CAD/sweep_v02/`
(include the wall-plane ±0.1 against REQ-05's new box); check results
`01_CAD/check_od_c11_back_v02.json`; REPORT `01_CAD/REPORT_od_c11_back_v02.md`
with its JSON block. Never overwrite a v01 file. The 3MF is the orchestrator's
step. Return the block your skill defines; at the fix-cycle cap or a hard gate
that cannot be met, stop with the measured failure (D9). This is the last build
attempt under the cap.

## Gate IDs to check (spec §5)

As WP-02: U-01 … U-08 (U-08 N/A), D-01a, D-01b, D-02, D-03a, D-03b, D-04a,
D-05a, D-05b, D-06a, D-07 (N/A), J-05, E-06, E-11, REQ-01 … REQ-09 (REQ-09 Soft
bench: INCONCLUSIVE); `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs

As `briefs/WP-02_designer.md`, with `00_Spec/DESIGN_SPEC.md` now
c4369d16b1ae88e83b088a2427ae55b7f0c8e0a96393470474cd147b79a117d2 (1.1).

## Environment

As WP-02: workspace `${OGUZ_JOBS}/20261001-od-c11-back-panel`, `. $HOME/oguz-env/env.sh`
first in every shell command, Python through `uv run tools/run.py python <script>`
from `/home/claude/oguz-atolye`.

## Findings to fix

Your v01 stop (REPORT v01 §8, §9): the feet holes under the flanges, and the
ledge over the flange screws — both answered by spec 1.1 as above.
