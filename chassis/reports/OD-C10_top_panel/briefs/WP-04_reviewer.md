# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20261001-od-c10-top-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-10-01) · concept C1 · target `od_c10_top_v01` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v01 of the printed top panel (lid) OD-C10 of the Open
Dedica espresso machine: the plan `01_CAD/DESIGN_PLAN.md`, the REPORT
`01_CAD/REPORT_od_c10_top_v01b.md` (the current one; `REPORT_od_c10_top_v01.md`
is the earlier stop, kept for the record), and the exported files below. Never
the designer's scripts (`01_CAD/*.py`, `01_CAD/*.sh`, `01_CAD/probe/*.py`), only
JSON results where a row needs them. The geometry was built to spec 1.1 and
stopped on U-03 (a): the rear skirt rests on OD-C11's wall top in two R 10 corner
patches. The Usta accepted them as designed contact; spec 1.2 changes only U-03
(a)'s wording, no geometry: review against 1.2 and write `"spec_version": "1.2"`.

The machine frame: X right, +Y up, +Z front, the plate's top face y 0. The lid
(skin y 247 … 250 over the plate outline, 3.0 skirt down to y 215) is held by
four M3 screws from above into inserts: two in OD-C02's top rail at (65, −60),
(65, −210), two in OD-C11's ledge at (±90, −293); two rest pads 0.5 above the
carrier OD-C05. Placements: OD-C01, OD-C02, OD-C11 identity; OD-C05 local x → X,
y → +Z, z → −Y, origin (0, 180.06, 32.0); OD-C07 local x → −Z, y → −X, z → +Y,
origin (−92, 0, −60). The OD-C11 reference is its **unreviewed build v02**
(its third build is running now with shorter outer gussets near the floor; its
wall, ledge and bores do not change): weigh that. Print: upside down, top face
on the bed, build direction −Y, PETG on the Kobra Max 3 (A-08 … A-10); the side
panels do not exist, so the lid's side and front edges are free (A-04).

## Gate rows (spec §5, every one, PASS rows included)

U-01 … U-08 (as each row says), U-06 Soft; D-01a, D-01b, D-02, D-03a and D-03b
(named exception on the four counterbore floors), D-04a, D-05a (N/A), D-05b,
D-06a, D-07, J-05, E-06, REQ-01 … REQ-08 (REQ-08 Soft bench: INCONCLUSIVE with a
risk rating); `exactly_one_solid`, `feature_census` against the plan,
`envelope_within_spec`; the §P plausibility list; positive controls for every
check family used. U-07: the 3MF `02_STEP_STL/od_c10_top_C1_v01.3mf` was written
by the orchestrator from the designer's STL and re-parsed (5164 triangles,
433996.82 mm³, watertight, bbox x ±120, y 210.5 … 250, z −305 … 100): check it
against the STL.

Weigh the REPORT's least-sure items: the designed-contact rows (columns on their
seats, the skirt on OD-C11) pass only at nominal in the sweep; the lid seats on
four columns plus the skirt line and corner patches (over-constraint, rocking);
REQ-08 stiffness of a 3 mm skin 240 × 405; and the open assumptions A-01 …
A-13, chiefly A-02 (OD-C11 interface), A-03 (the pads over the carrier), A-06
(headroom), A-09 (the Kobra's bed), A-10 (PETG over the group head).

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `briefs/WP-02_designer.md` | 962fb47ff1442a6f5bf76381f4b6f2fa3b77ab17f824c6a0df8cb3c9cc7f895d |
| `briefs/WP-03_designer.md` | 7693e9d5117e54132f4df56cfdf207d0ded10404abe5806cd16f6e1a02f7b160 |
| `00_Spec/DESIGN_SPEC.md` | e2eda540dd141c27a3ca8f7a84f2d05cfbf99a1d8df283c03bff28000c4ee966 |
| `00_Spec/INTAKE_v01.md` | 564b6330dd5a59098930fbe80bdd76406ae6966ebd7919401ecdedab70c49ba7 |
| `01_CAD/DESIGN_PLAN.md` | 0d0fc1a890e8431278bdd05ace29f67e8403dfa7a030ea4c36ce7c460171c0f7 |
| `01_CAD/REPORT_od_c10_top_v01.md` | 35c4ac84dd77b606a1f807ca91b68e951264d77e7ae1b615be5248d8d420386d |
| `01_CAD/REPORT_od_c10_top_v01b.md` | 2d5462f20f3fb0dd4267474db4a696cbff4cf71592837bee649437fca9802a8e |
| `01_CAD/check_od_c10_top_v01b.json` | 1076b253f353c7cf8bd50c5a92e87e5bcb689696d2235b26bcf31428afbe5d4a |
| `01_CAD/build_record_v01.json` | 61569d261817da34b2749064f9ad75e21f8b834ea6198d6ba439e83cbc12d197 |
| `01_CAD/sections_v01.json` | 49b94714e3466d9229f3041509586bd50241c525a23732262fe6d9fe8a84474d |
| `02_STEP_STL/od_c10_assembly_C1_v01.step` | d5881320038a66454cfb9d8a2b89aba4ca38c4cc69cd9182cad4eb6a9ef3c9d9 |
| `02_STEP_STL/od_c10_top_C1_v01.3mf` | cbab510c1faddc029fe40c16b5b351a9c6179b44547af0bcac30729f5fc6e643 |
| `02_STEP_STL/od_c10_top_C1_v01.step` | 0f85c4d7f7208b56aadf77888d17e9f0e9e8ab6e9937aaadb6e076b7239ab89f |
| `02_STEP_STL/od_c10_top_C1_v01.stl` | 2e3f1c736115fe1b6efca9110229357fca8c840fe8786f4b0ccced3e39d93bc9 |
| `03_Sections/od_c10_assembly_cols_x65_v01_left.png` | c6702fec12c6a21d010c0961dd8e07e3f8e69cacc1f0fc3258e94b949206d910 |
| `03_Sections/od_c10_assembly_cols_z-293_v01_top.png` | 082ba947ac1d2a4730cd006dde741c8d22cbe428ba6713cfdede5531a7e26db6 |
| `03_Sections/od_c10_assembly_corner_x113_v01_left.png` | eb7d44b9d4cb016737b8b8cad260922ab5097af70fd6817fc4a6d9771f1076db |
| `03_Sections/od_c10_assembly_corner_z-300p5_v01_top.png` | c55987e90d7c4bce645c4248d145703d8653c6d1f4dfb7409e8eaceeb10e4e21 |
| `03_Sections/od_c10_assembly_pads_z30_v01_top.png` | b76a8149f36bb4dfed43d1f80a5ca4f2d50a9eaae9153fe4fff5584ee4b748c6 |
| `03_Sections/od_c10_top_col_x-90_v01_left.png` | c3cbc6040f945fb77b8bd5b908c69a5a20f74e9b0c010c8d9262865bf0dc31ea |
| `03_Sections/od_c10_top_col_x90_v01_left.png` | 464acc51c567575adcc4999a94586b1b2460691cb496cb345bc76b6d2478e209 |
| `03_Sections/od_c10_top_col_z-210_v01_top.png` | 2aa0f9576829183e7aef8caab96e0f2a6cf0226b9a4747377bf2c587e8aaa0ce |
| `03_Sections/od_c10_top_col_z-60_v01_top.png` | e146b098c66eb8a8ab67ffe37eb361b800fd7190fd692bdd5201e047bf6d3858 |
| `03_Sections/od_c10_top_cols_x65_v01_left.png` | 9e63029fa3a1a33ab21d16719e713ee1510d6c801fb7323e5e7fd3e55eee32ab |
| `03_Sections/od_c10_top_cols_z-293_v01_top.png` | 128aa96e47bbea1176cea850e617f56a365291a18db34b58969291019e68e8bd |
| `03_Sections/od_c10_top_holes_y216p5_v01_front.png` | 297f6b993b1e5837585c73f1189b248cf211c055856be56f7bea96f438b1664e |
| `03_Sections/od_c10_top_pads_z30_v01_top.png` | ebddc98b1be7b5a6882331365e8d8d171907474da89da592e092b39dc467bec6 |
| `03_Sections/od_c10_top_plan_y230_v01_front.png` | bef87b584ef2298fa2bda237db2b370f9c94c4f44dc2f559129764f84cbd1afb |
| `03_Sections/od_c10_top_rearrib_x94_v01_left.png` | 61e4bf68f172944a5426f3ef61ffddfac118a2178dabf2347c944d062b311a58 |
| `03_Sections/od_c10_top_skin_y248p5_v01_front.png` | 0d578a5695b336da330ed0dfe723b40d44ef9de5b1894ee38bb85f1056aaff52 |

The sweep results are under `01_CAD/sweep_v01b/` (JSON only). Reference solids
(inputs, for the assembly rows): as `briefs/WP-02_designer.md` lists them with
their hashes and placements.

## Environment

Workspace `${OGUZ_JOBS}/20261001-od-c10-top-panel`; run `. $HOME/oguz-env/env.sh`
first in every shell command, then `cd /home/claude/oguz-atolye && uv run
tools/run.py python <script>`. Write only under `reviews/`
(`RV01_od_c10_top_v01.md`, `.json`, and `RV01_work/`); if the Write tool refuses a
file, write it with Bash. The lid is large: crop reference solids by bounding box
for clearance runs; `min_wall` and `overhang_census` may need `spacing=0.7`.
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
Do not call any `mcp__hearthbot__*` tool; your hand-back goes to the orchestrator only.
