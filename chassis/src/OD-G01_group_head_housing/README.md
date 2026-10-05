# OD-G01 printed group head housing — build scripts

Job `20260930-od-g01-group-head-housing` (record: `chassis/reports/OD-G01_group_head_housing/`),
build v03 to DESIGN_SPEC 1.3 (concept C1), reviewed once: RV01 `REVISE` on REQ-12
alone, the brew-load row that only the OD-T01 bench test can answer
(`reports/OD-G01_group_head_housing/reviews/RV01_od_g01_housing_v03.md`). The Usta
accepted it as a documented deviation on 2026-10-02 (`REVISE_PACKET_RV01.md`, option B).
Every geometric row passes on the reviewer's own measurement against the scanned
OEM bayonet cup (OD-G09), gasket support (OD-G04) and portafilter (OD-G10).

**Strength is not proven.** The housing's strength under brew pressure (15 bar on
the Ø51 basket, about 3 kN on the three bayonet lugs) has not been calculated or
tested. Run the OD-T01 bench pressure test behind a shield before any use with hot
water, and watch the lug roots (sharp, no fillet: RV01 F4). The Usta set PLA for
all prints for now (2026-10-02): PLA softens near 60 °C, so a PLA housing is a dry
fit check of the bayonet and the carrier only, never for hot water or pressure;
the service print and the bench test need ASA (spec §3).

Also recorded in RV01, not blocking: F2 one ear top of three touches at the locked
pose (A-25), F3 no boolean against OD-G10 (its STEP is not a sound solid, A-28),
F5 the STL is meshed at 0.002 mm, F6 the insert holes have no depth margin and open
on the flange front, F7 the ear-to-stop gap at the locked clock is 0.276 mm.

In the machine the housing stands with its axis vertical and the mouth down
(spec §2's "+Z is horizontal" sentence is wrong and is corrected in spec 1.4, which
awaits the Usta's ratification); it prints mouth up, with supports under the lugs
and stop blocks.

| File | What it is |
|---|---|
| `build_od_g01_housing_v03.py` | parametric build123d model of the housing; writes STEP (AP242) and STL |
| `check_od_g01_housing_v03.py` | the designer's gate checks (spec §5) on the re-imported STEP |
| `assemble_od_g01_check_v03.py` | the check assembly with OD-G09, OD-G04 and OD-G10 at the locked pose |
| `stl_to_3mf.py` | writes the delivered `.3mf` (one mesh object, millimetres) from the delivered STL |

Run from the `oguz-atolye` repository root with its tools venv
(`uv run tools/run.py python <script>`, build123d 0.11.1 / OCCT 7.9.3); the
scripts expect the job workspace at `${OGUZ_JOBS}/20260930-od-g01-group-head-housing`.

`OD-G01_group_head_housing.step` and `.stl` in `chassis/` are byte-identical copies
of the reviewed `02_STEP_STL/od_g01_housing_C1_v03.*` (SHA-256 `55478e0b…` and
`0e8fe8e2…`, as listed in RV01); the `.3mf` is written from that STL.
