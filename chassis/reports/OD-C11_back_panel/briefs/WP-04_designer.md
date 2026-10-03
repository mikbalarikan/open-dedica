# WP-04 — designer brief, J3 package (build v03)

Job: 20261001-od-c11-back-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-10-01 by the Usta with the third build; 1.1 kept as `00_Spec/DESIGN_SPEC_v1.1.md`) · concept C1 · target `od_c11_back_v03` · build attempt 3 of 3 (the Usta raised the cap) · fix_cycles 3

## Package

The third build. Your plans (`01_CAD/DESIGN_PLAN.md`, `01_CAD/DESIGN_PLAN_v02.md`)
stand except where spec 1.2 changes them; write the changes as
`01_CAD/DESIGN_PLAN_v03.md` (a short amendment). Spec 1.2 answers both v02
stops (REPORT v02 §10): the **outer gussets** (x ±(100.0 … 104.0)) keep their
16.0 leg along the flange but their leg up the wall is **18.0** (top at y 22,
2.0 below the pass-throughs' bottoms at y 24); the inner gussets keep 30.0.
U-03 (a)'s hole-edge distance is now **≥ 3.0 for the flanges and ≥ 2.0 for the
wall's foot**. Everything else is unchanged.

Rebuild from the v02 scripts, versioned (`build_od_c11_back_v03.py`,
`check_od_c11_back_v03.py`, `sections_od_c11_back_v03.py`, sweep `_v03`), export
into `02_STEP_STL/od_c11_back_C1_v03.step`, `od_c11_assembly_C1_v03.step`,
`od_c11_back_C1_v03.stl`; sections `_v03` (include one through each
pass-through and its nearest gusset); sweep into `01_CAD/sweep_v03/`; check
results `01_CAD/check_od_c11_back_v03.json`; REPORT
`01_CAD/REPORT_od_c11_back_v03.md` with its JSON block. Never overwrite a v01 or
v02 file. The 3MF is the orchestrator's step (report the STL's triangle count,
volume and bounding box). Return the block your skill defines; at the fix-cycle
cap or a hard gate that cannot be met, stop with the measured failure (D9) and
give the trade-off options. This is the last build attempt under the raised cap.

## Gate IDs to check (spec §5)

As WP-02: U-01 … U-08 (U-08 N/A), D-01a, D-01b, D-02, D-03a, D-03b, D-04a,
D-05a, D-05b, D-06a, D-07 (N/A), J-05, E-06, E-11, REQ-01 … REQ-09 (REQ-09 Soft
bench: INCONCLUSIVE); `exactly_one_solid`, `feature_census`, `envelope_within_spec`.

## Inputs

As `briefs/WP-02_designer.md`, with `00_Spec/DESIGN_SPEC.md` now
6da33456e123942bb92e7419ff190f6e01522b0580d36d510fa9c5eee6d61245 (1.2).

## Environment

As WP-02: workspace `${OGUZ_JOBS}/20261001-od-c11-back-panel`, `. $HOME/oguz-env/env.sh`
first in every shell command, Python through `uv run tools/run.py python <script>`
from `/home/claude/oguz-atolye`. Do not call any `mcp__hearthbot__*` tool; your
hand-back goes to the orchestrator only.

## Findings to fix

Your v02 stop (REPORT v02 §10): stop 1 (wall foot 2.300 from the feet holes'
rims) is answered by U-03 (a)'s ≥ 2.0 for the wall's foot, no geometry change;
stop 2 (outer gussets over the pass-throughs) by the 18.0 wall leg.
