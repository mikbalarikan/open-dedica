# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20260930-od-c04-thermoblock-mount · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-09-30) · concept C1 · target `od_c04_mount_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the printed thermoblock mount OD-C04 of the Open
Dedica espresso machine: the plan `01_CAD/DESIGN_PLAN.md` (with the amendments of
`briefs/WP-03_designer.md`, which is part of the plan), the REPORT
`01_CAD/REPORT_od_c04_mount_v01.md`, and the exported files listed below.
Never the designer's scripts (`01_CAD/*.py`, `01_CAD/probe/`, `01_CAD/sweep_v01/`,
`01_CAD/check_v01/`).

The build was made to spec 1.1; spec 1.2 changed one row only, REQ-08 (heat, a
bench gate) from Hard to Soft, and no geometry. Review against 1.2 and write
`"spec_version": "1.2"` in the JSON twin.

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a: clearance and boolean; b N/A by its row), U-04, U-05, U-06
(Soft), U-07, U-08 (N/A by its row), D-01a, D-01b, D-02, D-03a, D-03b, D-04a,
D-06a, D-07 (N/A by its row), E-06, REQ-01 … REQ-08 (REQ-08 is a Soft bench gate:
INCONCLUSIVE with a risk rating); the §P list; the feature census against the
plan (as amended: 1 rear plate, 1 foot, 2 gussets, 2 standoffs Ø12.0, 2 Ø4.0
bores, 4 Ø3.4 holes); positive controls for every check family used.

OD-H11 reads `brep_valid = 0` (spec A-14): the U-03 boolean is INCONCLUSIVE by
its row; gate the clearance rows on distance measurements. The two spacer solids
(`spacer_S1_assumed_A05`, `spacer_S2_assumed_A05`, Ø7.0, lengths 10.10 and
37.70) are the designer's constructions from spec A-05: gate REQ-03 and U-03
against them as the spec writes them, and rate what rests on them. Weigh the
REPORT's own least-sure items: the S1 tip sits 0.100 above the 10.0 air gap
against a scan with p95 error 0.474 (A-01).

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `01_CAD/REPORT_od_c04_mount_v01.md` | 52bb0fc7b1a73ebc5ea4a50a17c9b59b04747d55447d03ce5475cdec7300621b |
| `01_CAD/DESIGN_PLAN.md` | 74daa6d136c72db9cb5a96885450c4aaa738b3644beb2a836e596bc812cb87aa |
| `01_CAD/check_v01/check_results_v01.json` | 7857c10cbfa5bc4c4a544e6a6f8789a4d854248d0c3f00fc75777d3d4cb48259 |
| `01_CAD/check_v01/sections_v01.json` | bec9bf1a40472d8ce4672fb4832dbe0e27cd04688927547240e1cf109bfb6089 |
| `01_CAD/build_record_v01.json` | 8725dfedd9b26a7d25cc66de980b52e7e00577994e4cad98eb2ef11629a3121c |
| `01_CAD/sweep_v01/sweep_summary_v01.json` | 511c9f73792aca0e9654b6855d437bbf1aef4206931b217aa056da3335196a6a |
| `02_STEP_STL/od_c04_assembly_C1_v01.step` | f301128de7df7c8b6190ea54cefaddbaecbfd090377cf96be15fca0818175e2a |
| `02_STEP_STL/od_c04_mount_C1_v01.step` | 31904ca8fd3a11f00330639f47978de4f02ccb5965450c0b3c56767eb77fa221 |
| `02_STEP_STL/od_c04_mount_C1_v01.stl` | c579d4159966a522cb84282e97aefcbaec22cbb9ece844241cd0ba8e9e1b13f7 |
| `03_Sections/od_c04_mount_v01_front_yFoot.png` | a2458bcae6da5aca42ee212809d589798a8ee7230eeb8fe45db48605af1a8c54 |
| `03_Sections/od_c04_mount_v01_left_asm_xS1.png` | 22616d2b8774b890a7421147c1d471588470ed97e4e20f3a64107a3af5afbf7f |
| `03_Sections/od_c04_mount_v01_left_asm_xS2.png` | 73ae433c317ebd33629ef99e7a64a977f774e26c6ccacfe9533fcf7900e2d7a1 |
| `03_Sections/od_c04_mount_v01_left_xFrameHoles.png` | 56488e256c571e6ea6a00b7bb895c073647caa6fe394b5af3baaed8d046efc38 |
| `03_Sections/od_c04_mount_v01_left_xGusset.png` | 646d299e0969133bb4aedeb8aa2791f0258c0245ccfdfd075096fa1ec0ace1a6 |
| `03_Sections/od_c04_mount_v01_left_xS1.png` | 48457a0eb641e7f3e0655a0fad8401d8ac35fc2db8989fd3d7cd6905b8add91a |
| `03_Sections/od_c04_mount_v01_left_xS2.png` | 7ed90bedac941c6f521bf04a6166cddaf0daf4e326397db4a315bd3644dbbf9d |
| `03_Sections/od_c04_mount_v01_top_zStandoffs.png` | 0d4121a3c428eae55f529b81862af305f15fb1b63ae315efd7e3cad4cc496f24 |

Reference solid (input, for the assembly rows):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-H11_thermoblock.step` | e2d186f22cf7a4e235636cccdab24d4cc2a32e25448d41e797b319287d4038ff |
| `00_Spec/inputs/reports/OD-H11_thermoblock/params.json` | 46f1b43a54e82c08a96b2463d88622e9d5a5ae71245ccc3440c1d960ba1c5203 |
| `00_Spec/inputs/reports/OD-H11_thermoblock/README.md` | 61061c517ac0c20dfe1fa86a5e75dbf959eb52d272a843b2c613d77da4dddec0 |

OD-H11 is placed at the identity pose (joint at the origin, axis +Z); its body
axis is measured at (x −8.330, y −14.130) (spec §2, A-02), which REQ-07 uses.

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-c04-thermoblock-mount` (`/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount`); run
`source /home/claude/oguz-env.sh` in every shell command that runs Python, then
`cd /home/claude/oguz-atolye && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV01_od_c04_mount_v01.md`, `.json`, and `RV01_work/`); if
the Write tool refuses a file, write it with Bash.
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
