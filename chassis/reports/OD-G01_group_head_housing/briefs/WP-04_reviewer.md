# WP-04 — reviewer brief (J4, the one review of build v01)

Job: 20260930-od-g01-group-head-housing · data class PUBLIC · spec `00_Spec/DESIGN_SPEC.md` version 1.3 (ratified 2026-09-30) · concept C1 · target `od_g01_housing_v03` · review RV01 · attempt 1 (one review per build, D-012)

## What to review

The designer's build v03 of the printed group-head housing OD-G01 of the Open
Dedica espresso machine (round 2, attempt 2; v03 is v02's geometry re-measured
under spec 1.3): the plan `01_CAD/DESIGN_PLAN.md` with the amendments of
`briefs/WP-03_designer.md`, `WP-05` and `WP-06` (they are part of the plan), the
REPORT `01_CAD/REPORT_od_g01_housing_v03.md`, and the exported files listed
below. Never the designer's scripts (`01_CAD/*.py`), and not the v01 or v02
exports except where the REPORT cites the v02 sweep record.

## Gate rows (spec §5, every one, PASS rows included)

U-01, U-02, U-03 (a and b), U-04, U-05, U-06 (Soft), U-07, U-08 (N/A by its
row), D-01a, D-01b, D-02, D-03a, D-03b, D-04a, D-05a, D-05b, D-06a, D-07 (N/A by
its row), J-05, E-06, REQ-01 … REQ-13 (REQ-12 is the OD-T01 bench test: INCONCLUSIVE by the spec's own row); the §P list P1–P6; the feature census
against the plan; positive controls for every check family used.

## Files (relative to the workspace; SHA-256 as the REPORT lists them)

| File | SHA-256 | Role |
|---|---|---|
| `01_CAD/DESIGN_PLAN.md` | 3033b42551718f76820f8d5704056a67b49453f3fcb6d7201937ed32507daf28 | the plan (D2) |
| `briefs/WP-03_designer.md` | 92ecbb01206d649428b59f59332e77ab22408c08934151eaf5d097ec5172394a | plan amendments (spec 1.1) |
| `briefs/WP-05_designer.md` | d6a55ab2fd286a8ac23075eb12b63806deb648481bd25dc50090a510cd0c06cd | plan amendments (spec 1.2) |
| `briefs/WP-06_designer.md` | afb09dc7dfbf5b4af3a672c88a13ea805cd8b60969d73f04e13f4fedcb5b02da | plan amendments (spec 1.3) |
| `01_CAD/REPORT_od_g01_housing_v03.md` | f9778dac49d98bbf78c4a5fe2e1ef6c998e0e79aa1e6eb90531fdeb9663ce1af | the REPORT under review |
| `01_CAD/REPORT_od_g01_housing_v02.md` | 02ee81dea9dc7fd9d2dd249cc32481fa96c61e6c89c627df5d8c59466742d5b6 | round-2 REPORT whose D7 sweep v03 cites (same build script) |
| `01_CAD/sweep_v02/sweep_v02.json` | b3b29bd8d72d27a13ef352568b27edfc9dcf0d1ac35fa47c282aca8ac7e7b9d3 | the D7 sweep record v03 cites |
| `02_STEP_STL/od_g01_housing_C1_v03.step` | 55478e0b243c0d0bc97b4ec2a18df5ba6ab8ac797bc387b070e01f7332f37399 | the part, AP242: the file under review and for delivery |
| `02_STEP_STL/od_g01_assembly_C1_v03.step` | 9fd18eb5dfa628bc76c9d325dce5f94bcf2b8073fdc6daf94f6f9451124926f2 | the check assembly: housing + OD-G04 + OD-G10 as placed |
| `02_STEP_STL/od_g01_housing_C1_v03.stl` | 0e8fe8e265284ca76cff363dbbd2ab6df5c8485d8e4e8610f58ad29295f38cec | the print mesh |
| `03_Sections/od_g01_housing_v03_front.png` | 440317bad3e524ec54b9dab46a13aabb1ff480cd8bc50d39768596cea1232fb1 | section, D6 |
| `03_Sections/od_g01_housing_v03_top.png` | 9c37e36c00ede2a0b82f02c086a4e4a3f41111a2e271569079514f7a754a81c2 | section, D6 |
| `03_Sections/od_g01_housing_v03_left.png` | b1a5f5ca4e8ea8891288192d75d01f3fad3bc93fdb140a10b777cb3935b2627a | section, D6 |
| `03_Sections/od_g01_housing_stopblock_v03_front.png` | f101901d79a301a8fb48524e44a207f7ec1661c93dd410bd6f32e0502aeb7a95 | section, D6 |
| `03_Sections/od_g01_housing_lugunderside_v03_front.png` | 46f4ccc995a5ca0143b7d2faef5f1287687440e53cc411a90702c9722aad7d06 | section, D6 |
| `03_Sections/od_g01_housing_insertboss_v03_front.png` | 2a6022aaa1f071911d3a9b21fcbc1a3d629bdd507e975801444a4cbe32ddcdba | section, D6 |

Reference solids (inputs, for the assembly rows and the overlay):

| File | SHA-256 |
|---|---|
| `00_Spec/inputs/OD-G09_group_head_bayonet_cup.step` | 2f11c1b73c707effc8ef1d3edeb7155128b4c75e6a3b58eead6e49763a831906 |
| `00_Spec/inputs/OD-G04_brewing_gasket_support.step` | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 |
| `00_Spec/inputs/OD-G10_portafilter.step` | 3a525af139132f62b2b4182a7575ecfc4c90a7c7da3c61a1110e3deea187b257 |

`validity(OD-G09)` and `validity(OD-G10)` both read `brep_valid = 0` (the plan's
R7; spec A-28): nothing is gated on the OEM cup, and the boolean against OD-G10
is INCONCLUSIVE by the input, so spec 1.3's U-03 rows against OD-G10 are
distance rows (`clearance`), as §5 states them; OD-G04 is sound and takes the
boolean. Both are placed by the joints the plan's §5 and the WP-03 amendments
state (OD-G04: +6.05° about Z, back face at z −6.82; OD-G10: 180° about +X, then
+60.26° about Z at the locked clock or +122.5° at the insertion clock, rim at the
pose's z).

## Environment

Workspace `${OGUZ_JOBS}/20260930-od-g01-group-head-housing`; run
`source the OGUZ env file` in every shell command that runs Python, then
`cd <repo> && uv run tools/run.py python <script>`. Write only
under `reviews/` (`RV01_od_g01_housing_v01.md`, `.json`, and `RV01_work/`).
Templates: `atolye/templates/VERDICT.md`; schema `atolye/schemas/verdict.schema.json`.
