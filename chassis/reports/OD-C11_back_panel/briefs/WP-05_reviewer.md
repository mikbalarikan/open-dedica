# WP-05 — reviewer brief (J4, the one review of build v03)

Job: 20261001-od-c11-back-panel · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.2 (ratified 2026-10-01 by the Usta with the third build) · concept C1 · target `od_c11_back_v03` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v03 of the printed back panel OD-C11 of the Open Dedica
espresso machine: the plans `01_CAD/DESIGN_PLAN.md`, `01_CAD/DESIGN_PLAN_v02.md`
and `01_CAD/DESIGN_PLAN_v03.md` (amendments, with the briefs WP-03 and WP-04),
the REPORT `01_CAD/REPORT_od_c11_back_v03.md`, and the exported files below.
Never the designer's scripts (`01_CAD/*.py`, `01_CAD/*.sh`, `01_CAD/probe/*.py`),
only JSON results where a row needs them. Builds v01 and v02 were stopped by the
designer on spec faults (1.0, 1.1) and are not under review.

The machine frame: X right, +Y up, +Z front, the plate's top face y 0. The panel
is a 3.0 wall at z −302 … −299 over x ±116, 215 tall, on the OD-C01 plate's rear
edge, with two floor flanges screwed from above into four **new** M3 inserts in
OD-C01 at (±81, −282), (±95, −282) (A-01: not in the OD-C01 STEP yet; the plate
rows rest on the plate's material under each hole), four gussets (outer ones'
wall leg 18 since 1.2), a top ledge with two insert bosses for the top panel
OD-C10's rear screws at (±90, −293), three Ø12 pass-throughs (cord at (95, 30),
tubes at (−100, 30), (−84, 30); the water tank stands on the table, the Usta's
choice) and five vent slots. The wall's foot stands 2.3 from the rims of
OD-C01's feet holes at (±110, −295): U-03 (a) allows ≥ 2.0 for the wall foot
since 1.2. Print: lying on the outer face z −302, build direction +Z, PETG on
the Kobra Max 3 (A-08 … A-10).

## Gate rows (spec §5, every one, PASS rows included)

U-01 … U-08 (U-08 N/A), U-06 Soft; D-01a, D-01b, D-02, D-03a and D-03b (named
exception on the four Ø3.4 flange-hole crowns and the two Ø4.0 boss-bore
crowns), D-04a, D-05a, D-05b, D-06a, D-07 (N/A), J-05, E-06, E-11, REQ-01 …
REQ-09 (REQ-09 Soft bench: INCONCLUSIVE with a risk rating);
`exactly_one_solid`, `feature_census` against the plan as amended,
`envelope_within_spec`; the §P plausibility list; positive controls for every
check family used. U-07: the 3MF `02_STEP_STL/od_c11_back_C1_v03.3mf` was
written by the orchestrator from the designer's STL and re-parsed (3928
triangles, 165531.49 mm³, watertight, bbox x ±116, y 0 … 215, z −302 … −277):
check it against the STL.

Weigh the REPORT's least-sure items: the wall foot's rim distance (+0.200 at the
wall plane's +0.1 limit), the tube holes' 2.0 gap to the gussets (1.95 at Ø12.1),
and the open assumptions A-01 … A-13, chiefly A-01 (new OD-C01 inserts, screws
driven past the ledge), A-03 / A-04 (cord and tube positions with the tank on
the table), A-05 (the ledge inserts the top panel screws into), A-08 (a 232 ×
215 wall printed flat).

## Files (relative to the workspace; SHA-256 as measured now)

| File | SHA-256 |
|---|---|
| `briefs/WP-02_designer.md` | 57891d304a8191866305702e80fdc3a1937fbc4b47828f9287f41cc6bc9b17b5 |
| `briefs/WP-03_designer.md` | 898033cda353ab44b5024dfef031890b90bb36e6632715f3d02d519c0d789fda |
| `briefs/WP-04_designer.md` | 742bb60c40e8a1a2715e818f34f4f534426c0f1b2af3c5adb0efa0e6e87d946b |
| `00_Spec/DESIGN_SPEC.md` | 6da33456e123942bb92e7419ff190f6e01522b0580d36d510fa9c5eee6d61245 |
| `00_Spec/INTAKE_v01.md` | 716850a7c846399f660c89c4bf328f021fe13b06ad667ba7af43445a6f5324fc |
| `01_CAD/DESIGN_PLAN.md` | 83422ec39aec1276e2f24e41550686ba1e43e74bb195622457f45d26a1c4371b |
| `01_CAD/DESIGN_PLAN_v02.md` | 8859dd8b56efde148a9fe7452499be6324dd1bac0ab1d1389d88d8a2f9e9562a |
| `01_CAD/DESIGN_PLAN_v03.md` | 0793968205d092999f56d7b88d9b6e1cec99968e986cfd0af8c312dab1f41d3a |
| `01_CAD/REPORT_od_c11_back_v03.md` | 13eb7024e904449c70b5a36df02ba56982a9605889fd68076e67ae080df75f2f |
| `01_CAD/check_od_c11_back_v03.json` | ec5a36c5dae443d29c2c41e2a9e2f393e7dbb36b03e4e4eb9707d6cabd06262e |
| `01_CAD/build_record_v03.json` | 35f9273ecffa33c0e0362e85eb7de0a5c358c84f33ac7bf82ec5aaee9c9bcc71 |
| `01_CAD/sections_v03.json` | f21464764209634591af3a45211679c440254ff27e12aaef6b676749e6c7f96f |
| `02_STEP_STL/od_c11_assembly_C1_v03.step` | 900c822e2b05cf5d3d67d8ca7874900a845713c9be2d70628e9ad26be95bed73 |
| `02_STEP_STL/od_c11_back_C1_v03.3mf` | 7b18dc32d0aaa85669380cda0c2ed9086e7d70ae4395687b677d7f18f964d91d |
| `02_STEP_STL/od_c11_back_C1_v03.step` | 8ac0df9c351d5b82050526828317aa34c75b03729fd03fccd2bf5207cd0d33db |
| `02_STEP_STL/od_c11_back_C1_v03.stl` | 8fa761335a2bb2aaf5bb75e388c8151f75131bc5b652e19c3f7144625965f96a |
| `03_Sections/od_c11_assembly_feethole_x110_v03_left.png` | c0fb9a23a60defc7b7395c3fd4e0e98795e5f3ab33028bcdb83e9c789971e384 |
| `03_Sections/od_c11_back_bosses_y207_v03_front.png` | b0b2dd144b8302a5675f1eb334e5148fd62370c567b8ef323871ea0995ca06c8 |
| `03_Sections/od_c11_back_cord_gusset_x100p5_v03_left.png` | 7c9f8855208eef808b1e0b350ee2cc29bff32ec780b1e0a67bd76fbd95ca97ad |
| `03_Sections/od_c11_back_flanges_y2_v03_front.png` | 564d5c93d753ec1394d3350de058f5f39cdc56a1ff1b3c8c60c5193a28c2062a |
| `03_Sections/od_c11_back_gusset_x102_v03_left.png` | ae9999df6729761a0fe603f39d3218cbc155dd679e90a64fc1492fc71e6b422c |
| `03_Sections/od_c11_back_gusset_x74_v03_left.png` | f3a435b0cabe0bc1f1fb8d7de24688d765231057e3a1eaf8546340ce797b3118 |
| `03_Sections/od_c11_back_gusset_xm102_v03_left.png` | 116c513c9b80b073135fbd32fac97f87d7cf43c60558cd1ec55fff4d9a035c24 |
| `03_Sections/od_c11_back_gussets_z290_v03_top.png` | 9d1d4a68c51ba6e152e3b4072afe59959d70d3132ff43fe9b180e18b13b083a2 |
| `03_Sections/od_c11_back_hole_x81_v03_left.png` | d7d07411d0ad9e5324d42a3d7a150c8d568f5efff9fe7c5f782af23054a9c1e4 |
| `03_Sections/od_c11_back_hole_x95_v03_left.png` | e3894fc29ca85c98dbea598fadf2bfdf1932cd9283c728e6e77381748f1b0e5e |
| `03_Sections/od_c11_back_insert_x90_v03_left.png` | da9956c89bfe9514d29e7a79bbf3c7955624ffa8b43702859bc04d0532d40df2 |
| `03_Sections/od_c11_back_ledge_y213_v03_front.png` | 39fe83b4a238a84e94526b8ab6a9c12e542e73d4e0a4daeb17b0e7eefa6bd49a |
| `03_Sections/od_c11_back_passthroughs_y30_v03_front.png` | a0972fabb7c90b7b0f17374aa54f00fb145a806f0f3c1e3bf57f4b0bb5d695e2 |
| `03_Sections/od_c11_back_tube84_gusset_y30_v03_front.png` | c775b1db031a86431e0feebb556027e2500f16ca73faf62245c1cf724e1986b7 |
| `03_Sections/od_c11_back_tube_gusset_xm101_v03_left.png` | 1e6a293cae03a0247df044b1f5e68bc4b7a80b80269c7aaf666969448d562b35 |
| `03_Sections/od_c11_back_tube_xm100_v03_left.png` | 21e540cab636f72762df812b49fc0ddb56f3022b3c537a8801f32af3ea3c4a7b |
| `03_Sections/od_c11_back_vents_y140_v03_front.png` | 2d5418bed790b2e4ff886a2ca8af368f784ce31ede60cab830c3a678c75617b6 |
| `03_Sections/od_c11_back_wall_y200_v03_front.png` | 1323787de713cb383a1d434037f39d0c9210976b7e8131ad688ac41ce9eac640 |
| `03_Sections/od_c11_back_wall_y50_v03_front.png` | 6fa671a10f129afbb2a8ce865e488b811210d97f22d1b9d7cbf8c05aa934693d |
| `03_Sections/od_c11_back_wall_z300p5_v03_top.png` | 23577b424f81c5abeedb54777301b2e409aa71cc4a2bfc86df2eaaff150a6a8e |

The sweep results are under `01_CAD/sweep_v03/` (JSON only). Reference solids
(inputs, for the assembly rows): as `briefs/WP-02_designer.md` lists them with
their hashes and placements.

## Environment

Workspace `${OGUZ_JOBS}/20261001-od-c11-back-panel`; run `. $HOME/oguz-env/env.sh`
first in every shell command, then `cd /home/claude/oguz-atolye && uv run
tools/run.py python <script>`. Write only under `reviews/`
(`RV01_od_c11_back_v03.md`, `.json`, and `RV01_work/`); if the Write tool refuses
a file, write it with Bash. `min_wall` and `overhang_census` may need
`spacing=0.7` on the large faces. Templates: `atolye/templates/VERDICT.md`;
schema `atolye/schemas/verdict.schema.json`. Do not call any `mcp__hearthbot__*`
tool; your hand-back goes to the orchestrator only.
