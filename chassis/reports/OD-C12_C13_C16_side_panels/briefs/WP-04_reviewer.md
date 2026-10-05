# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20261002-od-c12-c13-c16-side-panels · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-10-03; SHA-256 72b8690cdccde2b14b533b7f1fceeba2ac02dd8ce80c0725431c02b99b1f7c16) · concept C1 · target `od_side_panels_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of three printed PLA parts of the Open Dedica espresso
machine: the right side panel OD-C13, the left side panel OD-C12 (its mirror plus
a 0.9 relief over the valve mount OD-C07), and the corner bracket OD-C16, used six
times (three per side at z −262, −15, +62) to fasten each panel's foot to the base
plate OD-C01 with M3 screws and heat-set inserts. The lid OD-C10's side skirts rest
on the panel tops, and a 60° wedge lip on each panel's inner rail locates the lid
with a 0.40 gap. Read the plan `01_CAD/DESIGN_PLAN.md` (with the answers of
`briefs/WP-03_designer.md`, which are part of the plan), the REPORT
`01_CAD/REPORT_od_side_panels_v01.md`, the sections in `03_Sections/`, and the
exported files below. Never the designer's scripts or their outputs
(`01_CAD/*.py`, `01_CAD/results_v01/`, `01_CAD/sweep_v01/`).

Spec 1.2 differs from 1.1 (the build's spec) only in U-03 (a)'s coaxiality band:
offset ≤ 0.20 in place of ≤ 0.10, the sum of the REQ-03 and REQ-05 position bands;
the geometry was not rebuilt. Rate the REPORT's §4 sweep findings against spec 1.2.
The REPORT was placed by the orchestrator because a session hook refused the
designer's write; its text is the designer's, unchanged but for the model name.

The bracket poses (spec §2 and §4): bracket frame, block x −19 … 0, y 0 … 16,
z ±8. Right side: translate (117, 0, z_c), identity rotation. Left side: rotate
180° about Y, then translate (−117, 0, z_c). z_c ∈ {−262, −15, +62}. The panels
and every input solid sit at the identity.

## Gate rows (spec §5, every one, PASS rows included)

U-01 … U-07, U-08 (N/A by its row), D-01a, D-01b, D-02, D-03a, D-03b, D-04a,
D-04d, D-05a, D-05b, D-06a, D-07 (N/A by its row), J-05, E-06, REQ-01 … REQ-08
(REQ-08 Soft, bench); the named exception for the bracket's insert-bore crown;
the §P list; the feature census against the plan; positive controls for every
check family used. Build your own check assembly from the three part files and the
inputs at the poses above, not from the designer's assembly file, and run U-03 (a)
and (b) on it. The REPORT's §9.3 says the panels' min_wall sampler does not reach
the lip wedge's 60° apex edge at (±110, 218.81): read that edge and the wedge's
slope from your own sections across the lip (for example at z −100 and z +60).

## Files (relative to the workspace)

| File | SHA-256 | Role |
|---|---|---|
| `02_STEP_STL/od_c13_right_C1_v01.step` | bb029af485a12941c364302b8a2f98c5b9c2436f73aea68e66bb8ed69be11a71 | OD-C13, AP242, one named solid |
| `02_STEP_STL/od_c13_right_C1_v01.stl` | 50beff9b3ddbc572d9020309e4c5e758830331a360c52d55ae1ca117d0dccf88 | its mesh (U-07) |
| `02_STEP_STL/od_c12_left_C1_v01.step` | 972343ab6af3684acf9000208761baa390e489cabe30d238c62ffa36e62f8408 | OD-C12, AP242, one named solid |
| `02_STEP_STL/od_c12_left_C1_v01.stl` | 872489a1afefcb39e725b3339595770184b17368deab05e7e9f1eaca66ee5d55 | its mesh (U-07) |
| `02_STEP_STL/od_c16_bracket_C1_v01.step` | 39faff6ce71326fc8d562d8c3daa42cd938fdf24f4dbe0933d82e9cae569c9fc | OD-C16 in its own frame, one named solid |
| `02_STEP_STL/od_c16_bracket_C1_v01.stl` | 0519dcb42e099fdc6433cc371989b0806ac74bd2e77aa7c43d3891c5ac6f19d5 | its mesh (U-07) |
| `02_STEP_STL/od_side_assembly_C1_v01.step` | aee5a94315143eb416bbe9111e5ef4a8e32e828ee70c522d6e015ac9fd7a58b7 | the designer's check assembly (for reference) |
| `01_CAD/REPORT_od_side_panels_v01.md` | 6b4597a7c05965a7e33a46750077b3bd3de40f4715d5263d0cf400a9e243b112 | the designer's self-check |
| `01_CAD/DESIGN_PLAN.md` | 83911646533081bdd7b41f52a15d45f295aad1c0f69f63fc03f13481131c1498 | the plan |
| `03_Sections/*.png` | REPORT §1 | fifteen sections |
| `00_Spec/inputs/OD-C01_base_frame.step` | 7b5688af0857cd734fea8e5ddb9248517c34128c73a185f470c1ac4e95195805 | reference solid, identity |
| `00_Spec/inputs/OD-C02_bulkhead.step` | 1e36348a8b0ac81d08b0b0316af2c98cd942ac47729f3015b6b87294daf14bdc | reference solid, identity |
| `00_Spec/inputs/OD-C05_group_head_carrier.step` | 7b3d33ad56b010f6056786ae803856f2ed705c18d5fcc730e2b5ce5b76fba5f1 | reference solid, identity |
| `00_Spec/inputs/OD-C07_valve_flowmeter_mount.step` | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c | reference solid, identity |
| `00_Spec/inputs/OD-C08_electronics_bay_tray.step` | 63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91 | reference solid, identity |
| `00_Spec/inputs/OD-C10_top_panel.step` | 0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f | reference solid, identity |
| `00_Spec/inputs/OD-C11_back_panel.step` | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db | reference solid, identity |
| `00_Spec/inputs/OD-C15_foot.step` | 830f80268050b3b40ff38dffde5f68dc158952d47917ffa28e0f98b7704b46d7 | reference solid, placed per its integration notes (`00_Spec/inputs/C15_integration_notes.md`) |

## Environment

Workspace `/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels`; run `source /root/oguz-env/env.sh` in every shell command that
runs Python, then `cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`.
Write only under `reviews/` (`RV01_od_side_panels_v01.md`, `.json`, and
`RV01_work/`). Templates: `atolye/templates/VERDICT.md`; schema
`atolye/schemas/verdict.schema.json`. Tools: `tools/README.md`. Do not call
any mcp__hearthbot__ tool. If a file write is refused, return its full text in
your reply instead. The container can restart: write your work scripts and
intermediate results under `reviews/RV01_work/` as you go, so a resumed run can
continue from them.
