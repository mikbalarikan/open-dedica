# INTAKE v01 — 20260930-od-g01-group-head-housing

Intake: Claude Code, claude-sonnet-5 · data class PUBLIC · brief `briefs/WP-01_intake.md` · 2026-09-30

<!--
Everything the job's inputs say, as tables, one row per value (PLAYBOOK §1 intake,
J0). Nothing here is confirmed: the orchestrator turns §2 and §3 rows into A-##
ledger rows in DESIGN_SPEC §6, and only the Usta confirms one (rule 5). Values
keep their original form and source. No prose summaries, no averaging, no
resolved conflicts, no persona text. A new batch of inputs gets a new version;
an earlier version is never overwritten.
-->

## §1 Files

| # | Path (relative to the workspace) | SHA-256 | Bytes | Type | Pages or views | Read how |
|---|---|---|---|---|---|---|
| 1 | 00_Spec/inputs/OD-G04_brewing_gasket_support.step | 19b4a140c76f2e1ccd92304cb1944a1cb7affcba4d0c7960488cfb26098d6ad2 | 768162 | STEP AP214 | n/a (B-rep) | hashed only, not opened (intake rule 6; geometry measured later by `tools/measure`) |
| 2 | 00_Spec/inputs/OD-G09_group_head_bayonet_cup.step | 2f11c1b73c707effc8ef1d3edeb7155128b4c75e6a3b58eead6e49763a831906 | 1128156 | STEP AP214 | n/a (B-rep) | hashed only, not opened |
| 3 | 00_Spec/inputs/OD-G10_portafilter.step | 3a525af139132f62b2b4182a7575ecfc4c90a7c7da3c61a1110e3deea187b257 | 2359838 | STEP AP214 | n/a (B-rep) | hashed only, not opened |
| 4 | 00_Spec/inputs/REQUEST.md | 059c7982e4e70e622d602e3331608883ea3dbfdd2c82687df93f257f7ac247cf | 3978 | Markdown (Usta request + project excerpts) | 1 | read in full |
| 5 | 00_Spec/inputs/bom_group_head_rows.csv | d583a739e016dd4354925adbe488716d242fe2ef62f4bf4657993cd9a512c032 | 1878 | CSV (BOM rows) | 18 rows (1 header + 17 data) | read in full |
| 6 | 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/DECISIONS.md | b812894ffcbdd224bf1f61fd56431c538dac64c55b89d8a048c8654067e06df4 | 1731 | Markdown (owner decision log) | 1 | read in full |
| 7 | 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/PARAM_TABLE.md | a949b91e5b4ec3af247ae130a7c31b237b7b9d4f951be88bff454e36daef17f9 | 17802 | Markdown (generated parameter table) | 1 (67 param rows) | read in full |
| 8 | 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/README.md | 0fcc6197a2aa5ea4acff96600133ab6cde7e8a01b75b39aa4e9356dd01b0db82 | 3759 | Markdown (RE report) | 1 | read in full |
| 9 | 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/SCAN_README.md | 3c48bf40e1c4fe11354f1df392d36456793578c91b70fa7ac3f9c1f474e4dfd8 | 1194 | Markdown (scan facts) | 1 | read in full |
| 10 | 00_Spec/inputs/reports/OD-G04_brewing_gasket_support/limitations.json | 47e336be163226e504160dbd5bb45c29d2ebf86ed5df3e146049109bb7e85815 | 6618 | JSON (machine-readable limitations) | 1 | read in full |
| 11 | 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/DECISIONS.md | e5994a2c20bc23f91a815cb332df260f3a3eb5986333d785b381ff676e8901f3 | 2261 | Markdown (owner decision log) | 1 | read in full |
| 12 | 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/PARAM_TABLE.md | 29ab601aece8f72a8bf6bdf3ed32cf079d2bdfd98474d6787666c9525db2e76f | 20064 | Markdown (generated parameter table) | 1 (67 param rows) | read in full |
| 13 | 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/README.md | 33c484fae742ce815d9a021349d5ad373e75af40333d9a7ff7d85332c65dcc1d | 2825 | Markdown (RE report) | 1 | read in full |
| 14 | 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/SCAN_README.md | 592037d5d25bd093ec6640d04e80d9df488a14aad3dc36eee820c08ba90a5d8d | 849 | Markdown (scan facts) | 1 | read in full |
| 15 | 00_Spec/inputs/reports/OD-G09_group_head_bayonet_cup/limitations.json | 21eb22f8fe17d7f156b0813abeeffdfbe228cf2f7d576b15f8abe4727b36dbe2 | 8338 | JSON (machine-readable limitations) | 1 | read in full |
| 16 | 00_Spec/inputs/reports/OD-G10_portafilter/DECISIONS.md | 57994dcca37cbf165cccfa07a1739af2eadc1ee2e42af2062f44172e0b5450af | 2978 | Markdown (owner decision log) | 1 | read in full |
| 17 | 00_Spec/inputs/reports/OD-G10_portafilter/PARAM_TABLE.md | d40a17325361faa7e0422ede43d7e93aa50bc6507b1e5fbf697f8e8d8eae5b59 | 35468 | Markdown (generated parameter table) | 1 (157 param rows) | read in full |
| 18 | 00_Spec/inputs/reports/OD-G10_portafilter/README.md | 7e736e16fde93a290d83f983e3f4e8a237be5512368bc005b3cf0f48c2c90980 | 2626 | Markdown (RE report) | 1 | read in full |
| 19 | 00_Spec/inputs/reports/OD-G10_portafilter/SCAN_README.md | c5dbff946156ea1cf02d57f54ad615d6898d37ba7496c52c5b64af97411cc83f | 753 | Markdown (scan facts) | 1 | read in full |
| 20 | 00_Spec/inputs/reports/OD-G10_portafilter/limitations.json | c03b290aba414306fb3312b17cf9f6438aecef587fb5bf0634f357a4bd931420 | 7543 | JSON (machine-readable limitations) | 1 | read in full |

## §2 Dimensions

<!--
Method: text · table · drawing callout · title block · scaled from drawing ·
photo · message. Flags: photo or scaled, not confirmable for fit · conflicts
with X-## · unit assumed · illegible.

Scope note: OD-G09 (the reference geometry for OD-G01) is captured in full —
every named parameter of its PARAM_TABLE.md. OD-G04 is captured for the
brief's named touchpoints (flange, plate, tabs, bosses, hub tube); its
internal ribs, ring-ribs, webs and back bead are NOT captured here (not named
in the brief and not a housing interface). OD-G10 is captured only for the
brief's named touchpoints (bayonet ear count/position/height/swept radius,
cup rim diameter at the gasket seat); its handle, grip, collar, spouts,
pressurised-insert internals and wire spring are NOT captured here (out of
brief scope; the housing only interfaces with the ears and the cup rim/wall).
All values below are copied from each report's generated PARAM_TABLE.md
exactly as given (rule 5) — "Value as given" and "Value in mm or deg" are
identical because the source units are already mm/deg/count. Multi-instance
values (e.g. three lugs' individual readings) are kept in one row exactly as
the source table presents them, slash-separated, per rule 5 ("keep the
original"); this mirrors the upstream report's own row granularity rather
than inventing a split the source did not make.
-->

| ID | What (feature or interface) | Value as given | Unit as given | Value in mm or deg | Tolerance as given | File | Page, view, or zone | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-001 | OD-G09 cup outer wall radius (envelope for housing bore) | 40.11 | mm | 40.11 | ±0.05 | #12 | PARAM_TABLE.md row `WALL_R_OUT`; measure/figures/rz_profile.json#outer_wall_r_vs_z | table | — |
| X-002 | OD-G09 cup lowest scanned point / scan-extent closure z (not a real face) | -27.835 | mm | -27.835 | ±0.0404511 | #12 | PARAM_TABLE.md row `Z_BOTTOM`; intake/alignment.json#bounds_aligned | table | — |
| X-003 | OD-G09 rim lip top z | 3.298 | mm | 3.298 | ±0.0404511 | #12 | PARAM_TABLE.md row `RIM_LIP_TOP_Z`; measure/figures/levels.json#rim_lip_top | table | — |
| X-004 | OD-G09 rim lip outer radius | 38.5 | mm | 38.5 | ±0.15 | #12 | PARAM_TABLE.md row `RIM_LIP_OUTER_R`; measure/figures/misc_fits.json | table | — |
| X-005 | OD-G09 rim ledge z at r=38.5 mm | 2.618 | mm | 2.618 | ±0.05 | #12 | PARAM_TABLE.md row `RIM_LEDGE_Z_AT_38p5`; measure/figures/misc_fits.json#rim_ledge_line_z_vs_r | table | — |
| X-006 | OD-G09 rim ledge z at r=39.8 mm | 2.348 | mm | 2.348 | ±0.05 | #12 | PARAM_TABLE.md row `RIM_LEDGE_Z_AT_39p8`; measure/figures/misc_fits.json#rim_ledge_line_z_vs_r | table | — |
| X-007 | OD-G09 rim outer corner fillet radius | 0.4 | mm | 0.4 | ±0.1 | #12 | PARAM_TABLE.md row `RIM_OUTER_FILLET_R`; measure/figures/prof_rim.png | table | — |
| X-008 | OD-G09 rim lip corner fillet radius | 0.3 | mm | 0.3 | ±0.1 | #12 | PARAM_TABLE.md row `RIM_LIP_FILLET_R`; measure/figures/prof_rim.png | table | — |
| X-009 | OD-G09 cup bore radius at z=0 (drafted bore) | 37.074 | mm | 37.074 | ±0.0815 | #12 | PARAM_TABLE.md row `BORE_R_Z0`; measure/figures/misc_fits.json#bore_gap_line | table | — |
| X-010 | OD-G09 cup bore draft angle (opens toward +z) | 0.645 | deg | 0.645 | ±0.0815 | #12 | PARAM_TABLE.md row `BORE_DRAFT_DEG`; measure/figures/misc_fits.json#bore_gap_line | table | — |
| X-011 | OD-G09 stepped shelf z, per gap (3 gaps, gap k follows lug k) | -14.101 / -13.44 / -14.233 | mm | -14.101 / -13.44 / -14.233 | ±0.0404511 | #12 | PARAM_TABLE.md row `SHELF_Z`; measure/figures/instances.json#gaps | table | — |
| X-012 | OD-G09 shelf-to-lip-wall edge fillet radius, per gap | 2.426 / 2.483 / 1.961 | mm | 2.426 / 2.483 / 1.961 | ±0.13 | #12 | PARAM_TABLE.md row `SHELF_EDGE_FILLET_R`; measure/figures/valley_fit.json#shelf_edge | table | — |
| X-013 | OD-G09 lip ring upper radius (gap sectors) | 30.82 | mm | 30.82 | ±0.08 | #12 | PARAM_TABLE.md row `LIP_UPPER_R`; measure/figures/rz_profile.json#lip_gap_r_vs_z | table | — |
| X-014 | OD-G09 lip ring lower radius (gap sectors) | 31.33 | mm | 31.33 | ±0.05 | #12 | PARAM_TABLE.md row `LIP_LOWER_R`; measure/figures/rz_profile.json#lip_gap_r_vs_z | table | — |
| X-015 | OD-G09 z where lip radius steps from upper to lower | -17.9 | mm | -17.9 | ±0.15 | #12 | PARAM_TABLE.md row `LIP_STEP_Z`; measure/figures/rz_profile.json#lip_gap_r_vs_z | table | — |
| X-016 | OD-G09 lip ring radius under the lugs (lug sectors) | 30.74 | mm | 30.74 | ±0.05 | #12 | PARAM_TABLE.md row `LIP_LUG_R`; measure/figures/rz_profile.json#lip_lug_r_vs_z | table | — |
| X-017 | OD-G09 bottom plate top face z (floor level) | -19.937 | mm | -19.937 | ±0.0404511 | #12 | PARAM_TABLE.md row `FLOOR_Z`; measure/figures/instances.json#floor_z_p50 | table | — |
| X-018 | OD-G09 bottom plate thickness | 2.5 | mm | 2.5 | ±1 | #12 | PARAM_TABLE.md row `PLATE_T`; input/photos/1.webp | table | assumed, no scan/caliper evidence |
| X-019 | OD-G09 lower cup wall inner radius, below the plate | 37 | mm | 37 | ±1 | #12 | PARAM_TABLE.md row `LOWER_WALL_R_IN`; intake/INTAKE_CARD.md#3 | table | assumed, no scan/caliper evidence |
| X-020 | OD-G09 bayonet lug (internal channel lug) count | 3 | count | 3 | exact | #12 | PARAM_TABLE.md row `LUG_COUNT`; measure/figures/count_lugs.json | table | — |
| X-021 | OD-G09 lug 1 start angle | 336 | deg | 336 | ±0.25 | #12 | PARAM_TABLE.md row `LUG1_START_DEG`; measure/figures/lugs.json#lug_top | table | — |
| X-022 | OD-G09 lug pitch angle | 120 | deg | 120 | ±0.25 | #12 | PARAM_TABLE.md row `LUG_PITCH_DEG`; measure/figures/lugs.json#lug_top | table | conflicts with X-124, X-131, X-138 (§4 Q4) |
| X-023 | OD-G09 lug angular span | 54 | deg | 54 | ±0.25 | #12 | PARAM_TABLE.md row `LUG_SPAN_DEG`; measure/figures/lugs.json#lugs | table | — |
| X-024 | OD-G09 lug inner-face radius (channel wall the portafilter ear rides against) | 31.682 | mm | 31.682 | ±0.0487 | #12 | PARAM_TABLE.md row `LUG_INNER_R`; measure/figures/instances.json#lug_inner_faces_circle | table | — |
| X-025 | OD-G09 top channel inner-wall radius, per lug | 34.455 | mm | 34.455 | ±0.16 | #12 | PARAM_TABLE.md row `CHANNEL_INNER_R`; measure/figures/lugs.json#lugs | table | — |
| X-026 | OD-G09 top channel floor z | -2.911 | mm | -2.911 | ±0.0404511 | #12 | PARAM_TABLE.md row `CHANNEL_Z`; measure/figures/levels.json#lug_channel | table | — |
| X-027 | OD-G09 channel floor start angle, offset from lug start | 3.83 | deg | 3.83 | ±0.5 | #12 | PARAM_TABLE.md row `CHANNEL_START_OFF_DEG`; measure/figures/lugs.json#channel_floor | table | — |
| X-028 | OD-G09 channel floor end angle, offset from lug start | 44.5 | deg | 44.5 | ±0.5 | #12 | PARAM_TABLE.md row `CHANNEL_END_OFF_DEG`; measure/figures/lugs.json#channel_floor | table | — |
| X-029 | OD-G09 bayonet stop-face end angle, offset from lug start | 5.76 | deg | 5.76 | ±0.5 | #12 | PARAM_TABLE.md row `STOP_END_OFF_DEG`; measure/figures/lugs.json#lugs | table | — |
| X-030 | OD-G09 bayonet stop-face bottom z, per lug | -10.524 | mm | -10.524 | ±0.2 | #12 | PARAM_TABLE.md row `STOP_BOTTOM_Z`; measure/figures/lugs.json#lugs | table | — |
| X-031 | OD-G09 stop-to-bore-wall root fillet radius | 1 | mm | 1 | ±0.2 | #12 | PARAM_TABLE.md row `STOP_ROOT_FILLET_R`; measure/figures/prof_stop_start.png | table | — |
| X-032 | OD-G09 lug underside z at +7 deg offset (shallow ramp segment) | -6.574 | mm | -6.574 | ±0.110544 | #12 | PARAM_TABLE.md row `UNDERSIDE_Z_AT_7`; measure/figures/underside_notch.json#underside_shallow | table | — |
| X-033 | OD-G09 ramp start angle offset (shallow-to-ramp transition) | 41.84 | deg | 41.84 | ±1 | #12 | PARAM_TABLE.md row `RAMP_START_OFF_DEG`; measure/figures/underside_notch.json | table | — |
| X-034 | OD-G09 lug underside z at ramp start | -5.588 | mm | -5.588 | ±0.110544 | #12 | PARAM_TABLE.md row `UNDERSIDE_Z_AT_RAMP`; measure/figures/underside_notch.json#underside_shallow | table | — |
| X-035 | OD-G09 lug underside ramp z at +54 deg offset | -1.149 | mm | -1.149 | ±0.0941147 | #12 | PARAM_TABLE.md row `RAMP_Z_AT_54`; measure/figures/underside_notch.json#underside_ramp | table | — |
| X-036 | OD-G09 under-lug pocket floor start angle offset | -5 | deg | -5 | ±0.5 | #12 | PARAM_TABLE.md row `POCKET_START_OFF_DEG`; measure/figures/lugs.json#pocket_inner_floor | table | — |
| X-037 | OD-G09 under-lug pocket floor end angle offset | 58.5 | deg | 58.5 | ±0.5 | #12 | PARAM_TABLE.md row `POCKET_END_OFF_DEG`; measure/figures/lugs.json#pocket_inner_floor | table | — |
| X-038 | OD-G09 outer valley (under-lug outer band) cylinder axis angle, per lug | 2.14 / 119.46 / 250.61 | deg | 2.14 / 119.46 / 250.61 | ±0.5 | #12 | PARAM_TABLE.md row `VALLEY_OUTER_THETA_C`; measure/figures/valley_fit.json#outer_valley | table | — |
| X-039 | OD-G09 outer valley lowest z, per lug | -15.267 / -15.036 / -15.085 | mm | -15.267 / -15.036 / -15.085 | ±0.097 | #12 | PARAM_TABLE.md row `VALLEY_OUTER_ZMIN`; measure/figures/valley_fit.json#outer_valley | table | — |
| X-040 | OD-G09 outer valley cylinder radius, per lug | 237.2 / 209.8 / 207.5 | mm | 237.2 / 209.8 / 207.5 | ±0.097 | #12 | PARAM_TABLE.md row `VALLEY_OUTER_RC`; measure/figures/valley_fit.json#outer_valley | table | — |
| X-041 | OD-G09 pocket inner-floor cylinder axis angle, per lug | 1.44 / 121.63 / 248.68 | deg | 1.44 / 121.63 / 248.68 | ±0.5 | #12 | PARAM_TABLE.md row `POCKET_INNER_THETA_C`; measure/figures/valley_fit.json#pocket_inner | table | — |
| X-042 | OD-G09 pocket inner-floor lowest z, per lug | -16.808 / -16.665 / -16.794 | mm | -16.808 / -16.665 / -16.794 | ±0.057 | #12 | PARAM_TABLE.md row `POCKET_INNER_ZMIN`; measure/figures/valley_fit.json#pocket_inner | table | — |
| X-043 | OD-G09 pocket inner-floor cylinder radius, per lug | 209 / 217.8 / 169.3 | mm | 209 / 217.8 / 169.3 | ±0.057 | #12 | PARAM_TABLE.md row `POCKET_INNER_RC`; measure/figures/valley_fit.json#pocket_inner | table | — |
| X-044 | OD-G09 bore wall radius, recessed behind each lug/pocket | 37.379 | mm | 37.379 | ±0.1 | #12 | PARAM_TABLE.md row `BORE_RECESS_R`; measure/figures/valley_fit.json#bore_recess | table | — |
| X-045 | OD-G09 pocket riser-wall radius (lug sectors) | 34.391 | mm | 34.391 | ±0.15 | #12 | PARAM_TABLE.md row `POCKET_RISER_R`; measure/figures/misc_fits.json#pocket_riser_r | table | — |
| X-046 | OD-G09 groove inner radius where the pocket floor starts to drop (lug sectors) | 36.7 | mm | 36.7 | ±0.1 | #12 | PARAM_TABLE.md row `GROOVE_R_IN`; measure/figures/misc_fits.json#groove_lug | table | — |
| X-047 | OD-G09 groove bottom z (lug sectors) | -15.571 | mm | -15.571 | ±0.2 | #12 | PARAM_TABLE.md row `GROOVE_BOTTOM_Z`; measure/figures/misc_fits.json#groove_lug | table | — |
| X-048 | OD-G09 rim notch 1 start angle, offset from lug start | 5 | deg | 5 | ±0.5 | #12 | PARAM_TABLE.md row `NOTCH1_START_OFF_DEG`; measure/figures/lugs.json#rim_ledge_at_lip_radius | table | — |
| X-049 | OD-G09 rim notch 2 start angle, offset from lug start | 34.83 | deg | 34.83 | ±0.5 | #12 | PARAM_TABLE.md row `NOTCH2_START_OFF_DEG`; measure/figures/lugs.json#rim_ledge_at_lip_radius | table | — |
| X-050 | OD-G09 rim notch angular width (6 notches total, 2 per lug) | 7.5 | deg | 7.5 | ±0.5 | #12 | PARAM_TABLE.md row `NOTCH_WIDTH_DEG`; measure/figures/lugs.json#rim_ledge_at_lip_radius | table | — |
| X-051 | OD-G09 rim notch floor z | 2.515 | mm | 2.515 | ±0.03 | #12 | PARAM_TABLE.md row `NOTCH_FLOOR_Z`; measure/figures/underside_notch.json#rim_notch_floor_z | table | — |
| X-052 | OD-G09 water-opening keyhole centre reach, plate interior | 13 | mm | 13 | ±3 | #12 | PARAM_TABLE.md row `KEY_CENTRAL_R`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-053 | OD-G09 water-opening lobe A axis angle | 133 | deg | 133 | ±10 | #12 | PARAM_TABLE.md row `KEY_LOBE_A_THETA`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-054 | OD-G09 water-opening lobe A end reach from plate centre | 23.5 | mm | 23.5 | ±3 | #12 | PARAM_TABLE.md row `KEY_LOBE_A_REACH`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-055 | OD-G09 water-opening lobe A width across | 7.2 | mm | 7.2 | ±3 | #12 | PARAM_TABLE.md row `KEY_LOBE_A_WIDTH`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-056 | OD-G09 water-opening lobe B axis angle | 310 | deg | 310 | ±10 | #12 | PARAM_TABLE.md row `KEY_LOBE_B_THETA`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-057 | OD-G09 water-opening lobe B end reach from plate centre | 20.5 | mm | 20.5 | ±3 | #12 | PARAM_TABLE.md row `KEY_LOBE_B_REACH`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-058 | OD-G09 water-opening lobe B width across | 10.5 | mm | 10.5 | ±3 | #12 | PARAM_TABLE.md row `KEY_LOBE_B_WIDTH`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-059 | OD-G09 screw boss 1 angular position | 66 | deg | 66 | ±10 | #12 | PARAM_TABLE.md row `BOSS_THETA_1`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-060 | OD-G09 screw boss pitch-circle radius | 20 | mm | 20 | ±3 | #12 | PARAM_TABLE.md row `BOSS_PCR`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use; conflicts with X-092, X-095 (§4 Q1) |
| X-061 | OD-G09 screw boss hole diameter | 3.4 | mm | 3.4 | ±3 | #12 | PARAM_TABLE.md row `BOSS_HOLE_D`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use; conflicts with X-100 (§4 Q2) |
| X-062 | OD-G09 screw boss outer ring diameter | 8 | mm | 8 | ±3 | #12 | PARAM_TABLE.md row `BOSS_OD`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-063 | OD-G09 side through-hole angular position | 269 | deg | 269 | ±10 | #12 | PARAM_TABLE.md row `SIDE_HOLE_THETA`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-064 | OD-G09 side through-hole radius from plate centre | 20.8 | mm | 20.8 | ±3 | #12 | PARAM_TABLE.md row `SIDE_HOLE_R`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-065 | OD-G09 side through-hole diameter | 6 | mm | 6 | ±3 | #12 | PARAM_TABLE.md row `SIDE_HOLE_D`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-066 | OD-G09 angle between the two screw bosses | 180 | deg | 180 | ±10 | #12 | PARAM_TABLE.md row `BOSS_PITCH_DEG`; input/photos/2.webp (polar unwrap measure/figures/p2_polar.png, zoom p2_plate.png); photo angle -> datum angle by piecewise-linear lug matching | photo (via param table) | photo-inferred; not confirmable for fit-critical use; conflicts with X-093, X-096 (§4 Q3) |
| X-067 | OD-G09 screw boss raised ring height | 0.6 | mm | 0.6 | ±0.5 | #12 | PARAM_TABLE.md row `BOSS_H`; input/photos/1.webp | table | assumed, no scan/caliper evidence |
| X-068 | OD-G04 plate back face z (datum origin) | 0 | mm | 0 | ±0.0489226 | #7 | PARAM_TABLE.md row `plate_back_z`; measure/figures/probe_p1.txt#plate back | table | — |
| X-069 | OD-G04 plate underside z | -2.59 | mm | -2.59 | ±0.0489226 | #7 | PARAM_TABLE.md row `plate_under_z`; measure/figures/probe_p2.txt#underside sector 0-95 | table | — |
| X-070 | OD-G04 plate outer-edge round radius | 0.316 | mm | 0.316 | ±0.054 | #7 | PARAM_TABLE.md row `plate_edge_round_R`; measure/figures/probe_p14.txt#plate outer edge round | table | — |
| X-071 | OD-G04 flange top z | -10.76 | mm | -10.76 | ±0.0489226 | #7 | PARAM_TABLE.md row `flange_top_z`; measure/figures/probe_p1.txt#flange top | table | — |
| X-072 | OD-G04 flange bottom z | -13.12 | mm | -13.12 | ±0.0489226 | #7 | PARAM_TABLE.md row `flange_bot_z`; measure/figures/probe_p1.txt#flange bottom | table | — |
| X-073 | OD-G04 flange outer radius | 30.8 | mm | 30.8 | ±0.0489226 | #7 | PARAM_TABLE.md row `flange_R_out`; measure/figures/probe_p1.txt#lip outer wall below tabs | table | — |
| X-074 | OD-G04 gasket-seat lip inner radius (groove width) | 29.32 | mm | 29.32 | ±0.0489226 | #7 | PARAM_TABLE.md row `lip_R_in`; measure/figures/probe_p1.txt#lip inner wall | table | — |
| X-075 | OD-G04 lip top z | -7.03 | mm | -7.03 | ±0.0489226 | #7 | PARAM_TABLE.md row `lip_top_z`; measure/figures/probe_p1.txt#lip top; probe_p14.txt#lip top | table | — |
| X-076 | OD-G04 flange inner corner fillet radius | 2.65 | mm | 2.65 | ±0.18 | #7 | PARAM_TABLE.md row `flange_inner_round_R`; measure/figures/probe_p18.txt#constrained tangent-arc | table | — |
| X-077 | OD-G04 flange-to-lip inner fillet radius | 1.084 | mm | 1.084 | ±0.05 | #7 | PARAM_TABLE.md row `flange_lip_fillet_R`; measure/figures/probe_p18.txt#flange-lip inner fillet | table | — |
| X-078 | OD-G04 cup wall-to-flange-top fillet radius | 0.38 | mm | 0.38 | ±0.06 | #7 | PARAM_TABLE.md row `wall_flange_fillet_R`; measure/figures/probe_p14.txt#wall-flange top fillet | table | — |
| X-079 | OD-G04 flange outer-bottom edge round radius | 0.196 | mm | 0.196 | ±0.07 | #7 | PARAM_TABLE.md row `flange_outer_round_R`; measure/figures/probe_p14.txt#flange outer-bottom round | table | — |
| X-080 | OD-G04 lip outer bead peak radius | 31.175 | mm | 31.175 | ±0.0489226 | #7 | PARAM_TABLE.md row `lip_bead_R`; measure/figures/probe_p20.txt | table | — |
| X-081 | OD-G04 lip outer bead peak z | -8.3 | mm | -8.3 | ±0.1 | #7 | PARAM_TABLE.md row `lip_bead_z`; measure/figures/probe_p20.txt | table | — |
| X-082 | OD-G04 lip outer bead lower extent z | -9.1 | mm | -9.1 | ±0.1 | #7 | PARAM_TABLE.md row `lip_bead_z_lo`; measure/figures/probe_p20.txt | table | — |
| X-083 | OD-G04 lip outer bead upper extent z | -7.6 | mm | -7.6 | ±0.1 | #7 | PARAM_TABLE.md row `lip_bead_z_hi`; measure/figures/probe_p20.txt | table | — |
| X-084 | OD-G04 bayonet tab count | 3 | count | 3 | exact | #7 | PARAM_TABLE.md row `tab_count`; measure/figures/count_tabs.json | table | — |
| X-085 | OD-G04 tab outer radius (across tabs) | 34.52 | mm | 34.52 | ±0.0489226 | #7 | PARAM_TABLE.md row `tab_R_out`; measure/figures/probe_p21.txt | table | — |
| X-086 | OD-G04 tab top z | -7.76 | mm | -7.76 | ±0.0489226 | #7 | PARAM_TABLE.md row `tab_top_z`; measure/figures/probe_p1.txt#tab top | table | — |
| X-087 | OD-G04 tab bottom z | -9.52 | mm | -9.52 | ±0.0489226 | #7 | PARAM_TABLE.md row `tab_bot_z`; measure/figures/probe_p1.txt#tab bottom | table | — |
| X-088 | OD-G04 tab angular span | 61.08 | deg | 61.08 | ±0.1 | #7 | PARAM_TABLE.md row `tab_span_deg`; measure/figures/probe_p8.txt#end faces | table | — |
| X-089 | OD-G04 tab pitch angle | 120 | deg | 120 | ±0.1 | #7 | PARAM_TABLE.md row `tab_pitch_deg`; measure/figures/probe_p8.txt#end faces | table | — |
| X-090 | OD-G04 tab 1 phase angle in the datum frame | -3.3 | deg | -3.3 | ±0.1 | #7 | PARAM_TABLE.md row `tab_phase_deg`; measure/figures/probe_p8.txt#end faces | table | — |
| X-091 | OD-G04 screw boss outer radius | 3.49 | mm | 3.49 | ±0.01 | #7 | PARAM_TABLE.md row `boss_R_out`; measure/figures/probe_p6.txt | table | — |
| X-092 | OD-G04 boss pair A centre radius | 15.5 | mm | 15.5 | ±0.05 | #7 | PARAM_TABLE.md row `bossA_r`; measure/figures/probe_p6.txt | table | conflicts with X-060 (§4 Q1) |
| X-093 | OD-G04 boss pair A angular positions | -6.55 / 172.95 | deg | -6.55 / 172.95 | ±0.1 | #7 | PARAM_TABLE.md row `bossA_theta_deg`; measure/figures/probe_p6.txt | table | conflicts with X-066 (§4 Q3) |
| X-094 | OD-G04 boss pair A bottom z | -16.12 | mm | -16.12 | ±0.05 | #7 | PARAM_TABLE.md row `bossA_bot_z`; measure/figures/probe_p6.txt | table | — |
| X-095 | OD-G04 boss pair B centre radius | 19.03 | mm | 19.03 | ±0.05 | #7 | PARAM_TABLE.md row `bossB_r`; measure/figures/probe_p6.txt | table | conflicts with X-060 (§4 Q1) |
| X-096 | OD-G04 boss pair B angular positions | 113.27 / -62.02 | deg | 113.27 / -62.02 | ±0.1 | #7 | PARAM_TABLE.md row `bossB_theta_deg`; measure/figures/probe_p6.txt | table | conflicts with X-066 (§4 Q3) |
| X-097 | OD-G04 boss pair B bottom z | -14.88 | mm | -14.88 | ±0.05 | #7 | PARAM_TABLE.md row `bossB_bot_z`; measure/figures/probe_p6.txt | table | — |
| X-098 | OD-G04 boss hole counterbore radius | 2 | mm | 2 | ±0.05 | #7 | PARAM_TABLE.md row `boss_cb_r`; measure/figures/probe_p15.txt | table | — |
| X-099 | OD-G04 boss hole counterbore depth | 1 | mm | 1 | ±0.25 | #7 | PARAM_TABLE.md row `boss_cb_depth`; measure/figures/probe_p15.txt | table | — |
| X-100 | OD-G04 boss through-hole radius | 1.53 | mm | 1.53 | ±0.03 | #7 | PARAM_TABLE.md row `boss_hole_r`; measure/figures/probe_p15.txt | table | conflicts with X-061 (§4 Q2) |
| X-101 | OD-G04 boss through-hole depth | 2.75 | mm | 2.75 | ±0.15 | #7 | PARAM_TABLE.md row `boss_hole_depth`; measure/figures/probe_p6.txt | table | — |
| X-102 | OD-G04 hub ring outer radius | 6.13 | mm | 6.13 | ±0.0489226 | #7 | PARAM_TABLE.md row `hub_ring_R_out`; measure/figures/probe_p1.txt#hub ring outer wall; probe_p12.txt#slot inner wall | table | — |
| X-103 | OD-G04 hub ring top z | 0.94 | mm | 0.94 | ±0.0489226 | #7 | PARAM_TABLE.md row `hub_ring_top_z`; measure/figures/probe_p1.txt#hub ring top | table | — |
| X-104 | OD-G04 centre conical recess radius at top | 4.7 | mm | 4.7 | ±0.05 | #7 | PARAM_TABLE.md row `cone_R_top`; measure/figures/probe_p2.txt#cone fit | table | — |
| X-105 | OD-G04 centre conical recess slope (dz/dr) | 0.924 | mm | 0.924 | ±0.02 | #7 | PARAM_TABLE.md row `cone_slope`; measure/figures/probe_p2.txt#cone fit | table | — |
| X-106 | OD-G04 centre bore radius | 1.3 | mm | 1.3 | ±0.0489226 | #7 | PARAM_TABLE.md row `centre_bore_r`; measure/figures/probe_p12.txt#centre bore wall | table | — |
| X-107 | OD-G04 centre post bottom z (deepest scanned point) | -5.64 | mm | -5.64 | ±0.1 | #7 | PARAM_TABLE.md row `centre_post_bot_z`; measure/figures/probe_p2.txt#centre r<3.5 | table | — |
| X-108 | OD-G04 centre post outer radius | 2.5 | mm | 2.5 | ±— | #7 | PARAM_TABLE.md row `centre_post_R_out`; input/photos/1.png | photo (via param table) | photo-inferred; not confirmable for fit-critical use |
| X-109 | OD-G04 hub back-face slot outer radius | 7.5 | mm | 7.5 | ±0.0489226 | #7 | PARAM_TABLE.md row `slot_R_out`; measure/figures/probe_p12.txt#slot outer wall | table | — |
| X-110 | OD-G04 hub back-face slot count | 4 | count | 4 | exact | #7 | PARAM_TABLE.md row `slot_count`; measure/figures/probe_p13.txt | table | — |
| X-111 | OD-G04 hub back-face slot angular width | 40.25 | deg | 40.25 | ±1 | #7 | PARAM_TABLE.md row `slot_span_deg`; measure/figures/probe_p13.txt | table | — |
| X-112 | OD-G04 hub back-face slot phase angle | -4.9 | deg | -4.9 | ±1 | #7 | PARAM_TABLE.md row `slot_phase_deg`; measure/figures/probe_p13.txt | table | — |
| X-113 | OD-G04 hub bore radius, upper step | 7.81 | mm | 7.81 | ±0.0489226 | #7 | PARAM_TABLE.md row `hub_bore_R_upper`; measure/figures/probe_p17.txt#hub bore upper; probe_p16.txt | table | — |
| X-114 | OD-G04 hub bore radius, lower step | 8.38 | mm | 8.38 | ±0.0489226 | #7 | PARAM_TABLE.md row `hub_bore_R_lower`; measure/figures/probe_p17.txt#hub bore lower; probe_p16.txt | table | — |
| X-115 | OD-G04 hub bore step z | -10.45 | mm | -10.45 | ±0.0489226 | #7 | PARAM_TABLE.md row `hub_bore_step_z`; measure/figures/probe_p17.txt#hub bore step face | table | — |
| X-116 | OD-G04 hub tube outer radius | 10.03 | mm | 10.03 | ±0.0489226 | #7 | PARAM_TABLE.md row `hub_tube_R_out`; measure/figures/probe_p17.txt#hub tube outer all z | table | — |
| X-117 | OD-G04 hub tube bottom z | -15.73 | mm | -15.73 | ±0.0489226 | #7 | PARAM_TABLE.md row `hub_tube_bot_z`; measure/figures/probe_p1.txt#hub tube bottom; probe_p14.txt#hub tube bottom U | table | — |
| X-118 | OD-G10 bayonet ear (lug) count | 3 | count | 3 | — | #17 | Checks table, `CHK-COUNT` row ("lugs 3 ... counted as separated angular/area clusters"); also 3 distinct lug1/2/3 parameter sets | table | — |
| X-119 | OD-G10 cup rim top z (datum, gasket-seat face) | 0 | mm | 0 | ±0.0224485 | #17 | PARAM_TABLE.md row `rim_top_z`; measure/figures/body_profile.json#rim_top_z | table | — |
| X-120 | OD-G10 cup outer wall radius at the rim (z=0) -- half the cup rim OD | 30.5864 | mm | 30.5864 | ±0.0284676 | #17 | PARAM_TABLE.md row `outer_wall_r_at_z0`; measure/figures/body_profile.json#outer_wall | table | — |
| X-121 | OD-G10 cup outer wall draft (dr/dz) | 0.0449187 | mm | 0.0449187 | ±0.0284676 | #17 | PARAM_TABLE.md row `outer_wall_dr_dz`; measure/figures/body_profile.json#outer_wall | table | — |
| X-122 | OD-G10 rim bore radius at z=0 -- half the basket-seat bore ID | 27.8964 | mm | 27.8964 | ±0.0406132 | #17 | PARAM_TABLE.md row `bore_r_at_z0`; measure/figures/body_profile.json#bore_upper | table | — |
| X-123 | OD-G10 rim bore draft (dr/dz) | 0.0520802 | mm | 0.0520802 | ±0.0406132 | #17 | PARAM_TABLE.md row `bore_dr_dz`; measure/figures/body_profile.json#bore_upper | table | — |
| X-124 | OD-G10 bayonet ear 1 centre angle | 59.5 | deg | 59.5 | ±0.28798 | #17 | PARAM_TABLE.md row `lug1_centre_deg`; measure/figures/lugs_notches.json#lugs | table | conflicts with X-022 (§4 Q4) |
| X-125 | OD-G10 bayonet ear 1 angular span | 37 | deg | 37 | ±0.57596 | #17 | PARAM_TABLE.md row `lug1_span_deg`; measure/figures/lugs_notches.json#lugs | table | — |
| X-126 | OD-G10 bayonet ear 1 outer (swept) radius -- half the ear swept diameter | 35.9647 | mm | 35.9647 | ±0.05 | #17 | PARAM_TABLE.md row `lug1_r_outer`; measure/figures/lugs_notches.json#lugs | table | — |
| X-127 | OD-G10 bayonet ear 1 underside z at ear centre (main ramp) | -5.12755 | mm | -5.12755 | ±0.0714969 | #17 | PARAM_TABLE.md row `lug1_under_z_centre`; measure/figures/details.json#lug_ramps | table | — |
| X-128 | OD-G10 bayonet ear 1 main ramp slope (mm per deg) | 0.0254284 | mm | 0.0254284 | ±0.0714969 | #17 | PARAM_TABLE.md row `lug1_under_dz_per_deg`; measure/figures/details.json#lug_ramps | table | — |
| X-129 | OD-G10 bayonet ear 1 underside lead-out z at ear centre | -9.06168 | mm | -9.06168 | ±0.0215218 | #17 | PARAM_TABLE.md row `lug1_leadout_z_centre`; measure/figures/lug_ends.json | table | — |
| X-130 | OD-G10 bayonet ear 1 lead-out ramp slope (mm per deg) | 0.331098 | mm | 0.331098 | ±0.0215218 | #17 | PARAM_TABLE.md row `lug1_leadout_dz_per_deg`; measure/figures/lug_ends.json | table | — |
| X-131 | OD-G10 bayonet ear 2 centre angle | 180 | deg | 180 | ±0.28798 | #17 | PARAM_TABLE.md row `lug2_centre_deg`; measure/figures/lugs_notches.json#lugs | table | conflicts with X-022 (§4 Q4) |
| X-132 | OD-G10 bayonet ear 2 angular span | 36 | deg | 36 | ±0.57596 | #17 | PARAM_TABLE.md row `lug2_span_deg`; measure/figures/lugs_notches.json#lugs | table | — |
| X-133 | OD-G10 bayonet ear 2 outer (swept) radius -- half the ear swept diameter | 35.7734 | mm | 35.7734 | ±0.05 | #17 | PARAM_TABLE.md row `lug2_r_outer`; measure/figures/lugs_notches.json#lugs | table | — |
| X-134 | OD-G10 bayonet ear 2 underside z at ear centre (main ramp) | -5.1021 | mm | -5.1021 | ±0.0609133 | #17 | PARAM_TABLE.md row `lug2_under_z_centre`; measure/figures/details.json#lug_ramps | table | — |
| X-135 | OD-G10 bayonet ear 2 main ramp slope (mm per deg) | 0.0259829 | mm | 0.0259829 | ±0.0609133 | #17 | PARAM_TABLE.md row `lug2_under_dz_per_deg`; measure/figures/details.json#lug_ramps | table | — |
| X-136 | OD-G10 bayonet ear 2 underside lead-out z at ear centre | -8.52679 | mm | -8.52679 | ±0.0513207 | #17 | PARAM_TABLE.md row `lug2_leadout_z_centre`; measure/figures/lug_ends.json | table | — |
| X-137 | OD-G10 bayonet ear 2 lead-out ramp slope (mm per deg) | 0.30401 | mm | 0.30401 | ±0.0513207 | #17 | PARAM_TABLE.md row `lug2_leadout_dz_per_deg`; measure/figures/lug_ends.json | table | — |
| X-138 | OD-G10 bayonet ear 3 centre angle | 300.5 | deg | 300.5 | ±0.28798 | #17 | PARAM_TABLE.md row `lug3_centre_deg`; measure/figures/lugs_notches.json#lugs | table | conflicts with X-022 (§4 Q4) |
| X-139 | OD-G10 bayonet ear 3 angular span | 35 | deg | 35 | ±0.57596 | #17 | PARAM_TABLE.md row `lug3_span_deg`; measure/figures/lugs_notches.json#lugs | table | — |
| X-140 | OD-G10 bayonet ear 3 outer (swept) radius -- half the ear swept diameter | 35.942 | mm | 35.942 | ±0.05 | #17 | PARAM_TABLE.md row `lug3_r_outer`; measure/figures/lugs_notches.json#lugs | table | — |
| X-141 | OD-G10 bayonet ear 3 underside z at ear centre (main ramp) | -5.01749 | mm | -5.01749 | ±0.0522816 | #17 | PARAM_TABLE.md row `lug3_under_z_centre`; measure/figures/details.json#lug_ramps | table | — |
| X-142 | OD-G10 bayonet ear 3 main ramp slope (mm per deg) | 0.0258546 | mm | 0.0258546 | ±0.0522816 | #17 | PARAM_TABLE.md row `lug3_under_dz_per_deg`; measure/figures/details.json#lug_ramps | table | — |
| X-143 | OD-G10 bayonet ear 3 underside lead-out z at ear centre | -8.76378 | mm | -8.76378 | ±0.0268742 | #17 | PARAM_TABLE.md row `lug3_leadout_z_centre`; measure/figures/lug_ends.json | table | — |
| X-144 | OD-G10 bayonet ear 3 lead-out ramp slope (mm per deg) | 0.333525 | mm | 0.333525 | ±0.0268742 | #17 | PARAM_TABLE.md row `lug3_leadout_dz_per_deg`; measure/figures/lug_ends.json | table | — |

## §3 Requirements and constraints

<!-- Material, process, quantity, finish, environment, loads, interfaces to other parts, standards named, dates. -->

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-145 | Job directive: draw the custom-design parts one at a time from the reference STEP files; start with the highest-priority part | "open dedica projesinde referans STEP dosyalarımızı kullanarak custom design yapılması gereken parçaları tek tek çizmemiz lazım. ilk öncelikli olan parçayı çizerek başlayalım" (Turkish, quoted verbatim) | #4 | Usta's message, 2026-09-30, quoted at the top of REQUEST.md |
| X-146 | Project frame: OD-G01 is the only Dedica part that cannot be bought as a spare (molded into the OEM case); if it must be printed, the whole chassis can be an open design | "The only part of a Dedica you cannot buy as a spare is the group-head housing, which is molded into the case. If that part must be printed anyway, the whole chassis can be an open design." | #4 | REQUEST.md, "Open Dedica" project README excerpt |
| X-147 | Safety: mains voltage (230 V / 120 V), water heated to ~125 °C at 15 bar; wet side separated from electric side; 192 °C TCO always in circuit; test behind RCD/GFCI; never print load-bearing or heat-adjacent parts in PLA | "this machine runs on mains voltage (230 V / 120 V), heats water to ~125 °C and pressurizes it to 15 bar. Keep the wet side separated from the electric side, keep the 192 °C thermal cutoff (TCO) in circuit, test behind an RCD/GFCI, and never print load-bearing or heat-adjacent parts in PLA." | #4 | REQUEST.md, project README "Safety" warning |
| X-148 | Process: parametric rebuild over the mesh only — no raw-mesh STEP exports; tubes, gaskets and brackets may be modeled from calipers alone | "Parametric rebuild over the mesh — **no raw-mesh STEP exports**. Tubes, gaskets and brackets can be modeled from calipers alone." | #4 | REQUEST.md, "Phase 2 — STEP deliverables" section |
| X-149 | Standard: STEP AP214, millimetres, file name per the naming scheme; CAD body/component also named "OD-Xnn Name" | "STEP AP214, millimetres, file name per the naming scheme; name the CAD body/component `OD-Xnn Name` too." | #4 | REQUEST.md, "Phase 2 — STEP deliverables" section |
| X-150 | Standard: check-fixtures are named `OD-Xnn-FX_<name>` | "Check-fixtures are named `OD-Xnn-FX_<name>`." | #4 | REQUEST.md, "Phase 2 — STEP deliverables" section |
| X-151 | Process: when a part moves to scanned / modeled / validated, update its `status` in `docs/bom.csv` in the same PR | "When a part moves to scanned / modeled / validated, update its `status` in `docs/bom.csv` in the same PR." | #4 | REQUEST.md, "Phase 2 — STEP deliverables" section |
| X-152 | Process: validate with a printed check-fixture (ring / cradle) against the real part; add a photo of the fit to the PR | "Validate with a printed check-fixture (ring / cradle) against the real part; add a photo of the fit to the PR." | #4 | REQUEST.md, "Phase 2 — STEP deliverables" section |
| X-153 | Chassis rule 1 — two-zone layout: wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains); a printed bulkhead + drainage path so a leak drips to the tray, not the PCB | "Two-zone layout. Wet zone ... physically separated from the electric zone ... In one chassis: a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #4 | REQUEST.md, "6. Chassis Design Rules", rule 1 |
| X-154 | Chassis rule 2 — copy OEM anti-vibration: pump in rubber sleeve + spring, decoupled from panels; TPU feet; rigid mounts rejected | "Copy OEM anti-vibration. Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #4 | REQUEST.md, "6. Chassis Design Rules", rule 2 |
| X-155 | Chassis rule 3 — thermal map: thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural | "Respect the thermal map. Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #4 | REQUEST.md, "6. Chassis Design Rules", rule 3 |
| X-156 | Chassis rule 4 — serviceability: top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock | "Serviceability is the point. ... top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #4 | REQUEST.md, "6. Chassis Design Rules", rule 4 |
| X-157 | Chassis rule 5 — design for the mug: group head height ≥ 95 mm above tray; keep the 0.4 m³ envelope limit from the thesis spec | "Design for the mug. Group head height ≥ 95 mm above tray (thesis legs were sized for a standard mug); keep the 0.4 m³ envelope limit from the thesis spec." | #4 | REQUEST.md, "6. Chassis Design Rules", rule 5 |
| X-158 | Chassis rule 6 — pre-infusion/preheat are software; leave sensor bosses (M3/M4 on thermoblock, tee for a thermocouple between heater and group head) in the chassis design from day one | "Pre-infusion & preheat are software. ... Leave sensor bosses (M3/M4 on thermoblock, tee for a thermocouple between heater and group head) in the chassis design from day one." | #4 | REQUEST.md, "6. Chassis Design Rules", rule 6 |
| X-159 | Chassis rule 7 — safety spec carries over: piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing | "Safety spec carries over: piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #4 | REQUEST.md, "6. Chassis Design Rules", rule 7 |
| X-160 | Framing: the group-head housing is the one part that must be printed and is the highest-risk part of the project; its internal geometry is defined entirely by the OEM part stack plus the portafilter lugs | "The group-head housing is the one part we must print and the highest-risk part of the project. Its internal geometry is defined entirely by this stack of OEM parts + the portafilter lugs." | #4 | REQUEST.md, GitHub issue 3 body excerpt |
| X-161 | Critical interface: diffuser (ref 52) — OD, thickness, screw/hole pattern | "Critical interfaces: Diffuser (52): OD, thickness, screw/hole pattern;" | #4 | REQUEST.md, GitHub issue 3 body excerpt |
| X-162 | Critical interface: brewing gasket (46), closure gasket (47), support (48), diffuser gasket (49), connectors gasket (54) — ID/OD/thickness/profile of each | "Brewing gasket (46), closure gasket (47), support (48), diffuser gasket (49), connectors gasket (54): ID/OD/thickness/profile;" | #4 | REQUEST.md, GitHub issue 3 body excerpt |
| X-163 | Critical interface: stack height when assembled | "Stack height when assembled;" | #4 | REQUEST.md, GitHub issue 3 body excerpt |
| X-164 | Critical interface: portafilter bayonet — lug count, lug angle span, ramp pitch, engagement depth | "Portafilter bayonet: lug count, lug angle span, ramp pitch, engagement depth;" | #4 | REQUEST.md, GitHub issue 3 body excerpt |
| X-165 | Critical interface: water inlet position into the group | "Water inlet position into the group." | #4 | REQUEST.md, GitHub issue 3 body excerpt |
| X-166 | OD-G00 Group head (assembly): design status todo, tracked in issue #3 | "OD-G00,OD-000,ASM,Group head,,,1,DESIGN,,,,#3,todo" | #5 | bom_group_head_rows.csv, row `OD-G00` |
| X-167 | OD-G01 Group head housing: material ABS/ASA; process printed; source note "printed — thesis Appendix 2 as starting point"; qty 1; status todo; issue #3 | "OD-G01,OD-G00,PRINT,Group head housing (open-source replacement for the molded OEM housing),,,1,DESIGN,ABS/ASA,printed — thesis Appendix 2 as starting point,print,#3,todo" | #5 | bom_group_head_rows.csv, row `OD-G01` |
| X-168 | OD-G02 Brewing gasket: ref 46, OEM code 537177; material silicone; qty 1 (+1 spare); source 4delonghi; price 3 EUR; issue #3, status todo | "OD-G02,OD-G00,OEM,Brewing gasket,46,537177,1 (+1 spare),CALIPER,silicone,4delonghi,3,#3,todo" | #5 | bom_group_head_rows.csv, row `OD-G02` |
| X-169 | OD-G03 Closure gasket: ref 47, OEM code 5313221481; material blank; qty 1 (+1 spare); source FixPart; price 3 EUR; issue #3, status todo | "OD-G03,OD-G00,OEM,Closure gasket,47,5313221481,1 (+1 spare),CALIPER,,FixPart,3,#3,todo" | #5 | bom_group_head_rows.csv, row `OD-G03` |
| X-170 | OD-G04 Brewing gasket support: ref 48, OEM code AS00005377; material blank in BOM; qty 1; method SCAN; source 4delonghi; price 3 EUR; issue #3, status modeled | "OD-G04,OD-G00,OEM,Brewing gasket support,48,AS00005377,1,SCAN,,4delonghi,3,#3,modeled" | #5 | bom_group_head_rows.csv, row `OD-G04` |
| X-171 | OD-G05 Bottom (diffuser) gasket: ref 49, OEM code AS00005075; material blank; qty 1 (+1 spare); source 4delonghi; price 3 EUR; issue #3, status todo | "OD-G05,OD-G00,OEM,Bottom (diffuser) gasket,49,AS00005075,1 (+1 spare),CALIPER,,4delonghi,3,#3,todo" | #5 | bom_group_head_rows.csv, row `OD-G05` |
| X-172 | OD-G06 Diffuser (shower screen): ref 52, OEM code 6013211191; material stainless; qty 1; method SCAN; source 4delonghi; price 3 EUR; issue #3, status todo | "OD-G06,OD-G00,OEM,Diffuser (shower screen),52,6013211191,1,SCAN,stainless,4delonghi,3,#3,todo" | #5 | bom_group_head_rows.csv, row `OD-G06` |
| X-173 | OD-G07 Connectors gasket: ref 54, OEM code 5313237781; material blank; qty 1; source FixPart; price 3 EUR; issue #3, status todo | "OD-G07,OD-G00,OEM,Connectors gasket,54,5313237781,1,CALIPER,,FixPart,3,#3,todo" | #5 | bom_group_head_rows.csv, row `OD-G07` |
| X-174 | OD-G08 Group head face plate with portafilter lugs (optional upgrade): material aluminium / stainless (laser-cut or machined); qty 1; source local shop; no price; status proposed | "OD-G08,OD-G00,MFG,Group head face plate with portafilter lugs (optional upgrade),,,1,DESIGN,aluminium / stainless (laser-cut or machined),local shop,—,,proposed" | #5 | bom_group_head_rows.csv, row `OD-G08` |
| X-175 | OD-G09 OEM group head bayonet cup: reference geometry for OD-G01, molded into the case; material molded plastic; qty 0 (REF); method SCAN; source donor; issue #38; status modeled | "OD-G09,OD-G00,REF,OEM group head bayonet cup (molded into the case — reference geometry for OD-G01),,,0,SCAN,molded plastic,donor,—,#38,modeled" | #5 | bom_group_head_rows.csv, row `OD-G09` |
| X-176 | OD-G10 Portafilter 51 mm (filter holder assembly): ref 06, OEM code AS00002706; material blank in BOM; qty 1; method SCAN; source OEM / AliExpress "51mm bottomless portafilter Dedica"; price 20-30 EUR; issue #39; status modeled | "OD-G10,OD-G00,OEM,Portafilter 51 mm (filter holder assembly),06,AS00002706,1,SCAN,,OEM / AliExpress `51mm bottomless portafilter Dedica`,20–30,#39,modeled" | #5 | bom_group_head_rows.csv, row `OD-G10` |
| X-177 | OD-G11 Filter basket 1-cup: ref 03, OEM code AS00003137; material stainless; qty 1; method CALIPER; source OEM/aftermarket; price 5 EUR; issue #4, status todo | "OD-G11,OD-G10,OEM,Filter basket 1-cup,03,AS00003137,1,CALIPER,stainless,OEM / aftermarket,5,#4,todo" | #5 | bom_group_head_rows.csv, row `OD-G11` |
| X-178 | OD-C05 Group head carrier (ties OD-G00 to frame): material ASA; process printed; qty 1; status proposed; issue #3 | "OD-C05,OD-C00,PRINT,Group head carrier (ties OD-G00 to frame),,,1,DESIGN,ASA,printed,print,#3,proposed" | #5 | bom_group_head_rows.csv, row `OD-C05` |
| X-179 | OD-F01 M3 heat-set insert: material brass M3; qty ~40; source AliExpress; price 10 (set); status todo | "OD-F01,OD-000,STD,M3 heat-set insert,,,~40,VENDOR,brass M3,AliExpress,10 (set),,todo" | #5 | bom_group_head_rows.csv, row `OD-F01` |
| X-180 | OD-F02 M3×8 screw: standard ISO 7380 / DIN 912 A2; qty ~40; source AliExpress; status todo | "OD-F02,OD-000,STD,M3×8 screw,,,~40,VENDOR,ISO 7380 / DIN 912 A2,AliExpress,(set),,todo" | #5 | bom_group_head_rows.csv, row `OD-F02` |
| X-181 | OD-G12 Filter basket 2-cup: ref 04, OEM code AS00003138; material stainless; qty 1; method CALIPER; source OEM/aftermarket; price 5 EUR; issue #4, status todo | "OD-G12,OD-G10,OEM,Filter basket 2-cup,04,AS00003138,1,CALIPER,stainless,OEM / aftermarket,5,#4,todo" | #5 | bom_group_head_rows.csv, row `OD-G12` |
| X-182 | OD-G13 ESE pods filter (optional): ref 05, OEM code 5513281011; material blank; qty 1; method CALIPER; source OEM; price 5 EUR; no issue; status todo | "OD-G13,OD-G10,OEM,ESE pods filter (optional),05,5513281011,1,CALIPER,,OEM,5,,todo" | #5 | bom_group_head_rows.csv, row `OD-G13` |

## §4 Conflicts and gaps

<!-- Also information the spec will need that no input gives, as a question, never as an answer. -->

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-060, X-092, X-095 | OD-G09's screw-boss pitch-circle radius (`BOSS_PCR` = 20 mm, photo-inferred, ±3 mm) does not match either of OD-G04's two scan-measured boss radii (`bossA_r` = 15.5 mm, `bossB_r` = 19.03 mm). Which of OD-G04's boss pairs (A or B) is the pair whose "two fixing screws" (per the job statement) pass through OD-G09's plate bosses, and does the mismatch matter, or is OD-G09's boss geometry simply not evidence-backed (photo-inferred, coverage C3, "not scanned")? |
| 2 | X-061, X-100 | OD-G09's screw-boss hole diameter (`BOSS_HOLE_D` = 3.4 mm, photo-inferred, ±3 mm) is close to but not identical to OD-G04's scan-measured through-hole diameter (`boss_hole_r` × 2 ≈ 3.06 mm). Is this the same fastener clearance hole, and if so which value should govern — noting `BOSS_HOLE_D` is explicitly "not fit for... manufacture or fit-critical use" per OD-G09's `limitations.json` (L5)? |
| 3 | X-066, X-093, X-096 | OD-G09's two screw bosses are photo-inferred as `BOSS_PITCH_DEG` = 180° apart (an assumed "intent: opposite", the photo itself read 178°). OD-G04 has two boss pairs: A at -6.55°/172.95° (≈179.5° apart, near-diametric) and B at 113.27°/-62.02° (≈175.3° apart, explicitly noted "NOT diametric" in OD-G04's PARAM_TABLE.md). Which OD-G04 boss pair is the one meant to align with OD-G09's two plate bosses, and should the housing accommodate the diametric assumption or OD-G04's actual (non-diametric) boss B spacing? |
| 4 | X-022, X-124, X-131, X-138 | OD-G09 models its internal bayonet-lug pitch as an idealised, perfectly symmetric 120° (`LUG_PITCH_DEG`, rule "symmetry"). OD-G10's real portafilter ears sit at 59.5°/180°/300.5° (spacing 120.5°/120.5°/119°), and OD-G10's own PARAM_TABLE.md notes this spacing is "not within noise, so no 3-fold symmetry is enforced." Since the housing (OD-G01) must accept the real portafilter, should its internal channel be sized/positioned to the portafilter's actual (slightly asymmetric) ear spacing rather than OD-G09's idealised symmetric model, and by how much clearance? |
| 5 | X-001 to X-067 (all OD-G09 rows) | OD-G09 (the sole reference geometry named for OD-G01) carries **no official grade**: its independent verify run returned HALT because the ICP registration did not converge (`limitations.json` L0), and it was delivered only on the owner's explicit override ("bu haliyle deliver et"). Within it, the plate keyhole, both screw bosses, and the side hole (rows X-052 to X-066) are photo-inferred from a single un-scaled photo (±3 to ±10 mm/deg) and are explicitly declared "not fit for... manufacture, tooling or fit-critical use" (`limitations.json` claim_boundary). Given OD-G01's fit to this cup's channel, bosses and water opening is central to the job, should design proceed using these HALT-grade / photo-inferred values as placeholders pending a caliper re-run of OD-G09, or must OD-G09 be re-measured first? |
| 6 | X-018, X-068, X-069 | OD-G09's plate thickness (`PLATE_T` = 2.5 mm) is itself photo-inferred/assumed ("no scan of the underside... photo 1 keyhole edge suggests ~2-3 mm"). OD-G04's plate has no single "thickness" parameter; its `plate_back_z` (0, datum) and `plate_under_z` (-2.59 mm) imply a thickness by subtraction, but OD-G04's own README says "Confirm plate thickness ... before the housing is frozen" and its DECISIONS/limitations mark scale as caliper-unverified. Which plate-thickness figure (if either) should the housing design use, and should the ~2.59 mm implied by X-068/X-069 be treated as measured or only as a datum-offset pending confirmation? |
| 7 | X-084, X-091 to X-101 | The job statement (brief, not a listed input) says OD-G01 must "seat the OEM brewing gasket support (OD-G04) with its two fixing screws," but OD-G04 has 4 screw bosses (2 pairs, A and B; rows X-091 to X-101), each with a counterbored through-hole, plus 3 bayonet tabs (row X-084, `tab_count` = 3) separate from the bosses. Which two of OD-G04's four bosses are "the two fixing screws," and do the tabs engage a separate feature on OD-G01/OD-G09 (see Q8), or are they merely OD-G04's own retention geometry against the housing bore? |
| 8 | X-048, X-049, X-050, X-084, X-088 | OD-G09 has six rim notches (2 per lug, rows X-048–X-050, `NOTCH1/2_START_OFF_DEG`, `NOTCH_WIDTH_DEG`), and OD-G04 has three bayonet tabs (rows X-084, X-088, `tab_count`, `tab_span_deg`). No input states whether OD-G04's tabs seat into OD-G09's rim notches, into a different feature of OD-G01, or whether the notches serve a different OEM part (e.g. the closure gasket OD-G03, not in this intake's inputs). Which feature does the housing need to reproduce for this mating? |
| 9 | X-167, X-155 | The BOM (row X-167) already fixes OD-G01's material as ABS/ASA, but REQUEST.md's chassis rule 3 (row X-155) makes ABS/ASA conditional ("ABS/ASA near heat, PETG elsewhere, PLA nowhere structural"). Is the group-head housing formally classified as "near heat" (thermoblock-adjacent) for this rule, confirming ABS/ASA, or should the material choice be revisited once the thermoblock-connection geometry (through OD-G04's hub, rows X-102–X-117) is designed? |
| 10 | X-157 | Chassis rule 5 sets "group head height ≥ 95 mm above tray" and a 0.4 m³ overall chassis envelope, both inherited from an external thesis not among this job's inputs. Does the 95 mm figure apply to OD-G01 alone (e.g. its bottom plate/floor level, row X-017 `FLOOR_Z`) or to the group head assembly (OD-G00) including the portafilter engaged below it (OD-G10's overall length is not captured as a row in this intake — out of the brief's named scope — but is long enough to matter for a tray clearance check)? |

## §5 Unreadable

None. All 20 listed inputs were processed without error: the 3 STEP files (#1-3) were hashed only and not opened, per intake rule 6 (their geometry is measured later by `tools/measure`); the 17 markdown/CSV/JSON files (#4-20) were read in full. No page, image, or region was illegible or inaccessible.
