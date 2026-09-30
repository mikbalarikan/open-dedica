# INTAKE v01 — 20260930-od-c07-valve-flowmeter-mount

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

All paths relative to the workspace `00_Spec/inputs/`. STEP files are listed and hashed only; their geometry is measured later by `tools/measure` (intake rule 6). PNGs were viewed in full; long markdown/json were read in full.

| # | Path | SHA-256 | Bytes | Type | Pages or views | Read how |
|---|---|---|---|---|---|---|
| 1 | `REQUEST.md` | 6c6921686ccc7f4652d6d24006049b571fb00c7a0694ddc46d6b0ec24e6b5eb7 | 3352 | Markdown | 1 | full text |
| 2 | `bom_rows.csv` | a161d4a39993ba05f256518fa3b4093e77fe646bc21d67e4119a89cd4e6ded6d | 1417 | CSV | 15 rows | full |
| 3 | `CHASSIS_README.md` | 3e4d6625d6be679f9200b0179b4905f34c1a751cca9257b4798bf987a798865c | 3242 | Markdown | 1 | full text |
| 4 | `WATER_FLOW.md` | 39c16b34185dfa94284ec511962677486bed26233489a07cd8eafeb5bfce4aca | 2495 | Markdown | 1 | full text |
| 5 | `SOURCING_GUIDE.md` | 675c019f0dcf52fa3e0bd315e9d12d5e9d325c48f2e4e83137029888df7b80dc | 20514 | Markdown | 1 (9 sections) | full text |
| 6 | `OD-H21_antidrip_valve.step` | 513090becca7d693df18dfe3063f16c4c5bb767c7078fc0258a209426337e88a | 736937 | STEP | — | listed/hashed only, not opened (rule 6) |
| 7 | `OD-H22_3way_valve.step` | bc0ffd003bcba248c7c8c4d68b198994726ee34b6c7e96ac97fbfd6490920028 | 806672 | STEP | — | listed/hashed only, not opened (rule 6) |
| 8 | `OD-H24_flowmeter.step` | 1b4cbdafd03e0edafcc900b8c8c0894b382a48bd71850b59b06201a1fb45696a | 865409 | STEP | — | listed/hashed only, not opened (rule 6) |
| 9 | `reports/OD-H21_antidrip_valve/README.md` | 5d89287b41b045cc53e0dee6de687ef72a97f8ca0890bcd7c38f97cb9ba8fdcc | 3199 | Markdown | 1 | full text |
| 10 | `reports/OD-H21_antidrip_valve/DELIVER_README.md` | de0e9064edd235bc313ef12ce8736b56eb48dc5e9248dbd3488ca5fa9990c961 | 45197 | Markdown | 1 (16 sections) | full text |
| 11 | `reports/OD-H21_antidrip_valve/PARAM_TABLE.md` | 5d29c57ecb02145a476484ce8cde22adabe59b809402cc86f3673ec3ece1d9c6 | 32162 | Markdown | 1 | full text |
| 12 | `reports/OD-H21_antidrip_valve/INTAKE_CARD.md` | d90938625677c77a0f89a9e916c9ab1250a1a4acaafdc00d5420599b67e004c4 | 12261 | Markdown | 1 (10 sections) | full text |
| 13 | `reports/OD-H21_antidrip_valve/DECISIONS.md` | fd0ff654eb7bbf2b6fe6b3fe36ac2f94e2c896fd6a8d466e9e4a2dd034fbbb35 | 2641 | Markdown | 1 | full text |
| 14 | `reports/OD-H21_antidrip_valve/limitations.json` | f2e19b5190a65b9e7160a6e6757f6a77bda74ad18ce8b637d2e0b3ba3e3f5989 | 7021 | JSON | — | full |
| 15 | `reports/OD-H21_antidrip_valve/alignment.json` | b1976a9df8d163ce442e397ccd163ee51e48c4abb2e477a0399be89a9008ed4a | 10026 | JSON | — | full |
| 16 | `reports/OD-H21_antidrip_valve/overlay_z.png` | 133a3039cb22bf5cafb5cd791168f44151a1cb11ed873cb8d4d9af5113abbabd | 369825 | PNG | 9-panel scan/CAD overlay | viewed |
| 17 | `reports/OD-H22_3way_valve/README.md` | 5bc1017c846323b789b0b5c2153ad005e8ee26a964f531a73a8706d9c469d876 | 3736 | Markdown | 1 | full text |
| 18 | `reports/OD-H22_3way_valve/DELIVER_README.md` | b0246ffc398499b57b367e53ba7b2e1911bec9c691342c4aee33dd553ab297d4 | 34613 | Markdown | 1 (16 sections) | full text |
| 19 | `reports/OD-H22_3way_valve/PARAM_TABLE.md` | 1c994fcee911047b81a9e6710ddd4f8fe700e0011858b0119ada21f66f662c73 | 18119 | Markdown | 1 | full text |
| 20 | `reports/OD-H22_3way_valve/params.json` | 2e8f4dafed0892b59b70ffa463751eb6bfe480df0ebec3b29801f6cd5c06eb82 | 27202 | JSON | — | full |
| 21 | `reports/OD-H22_3way_valve/MODELING_PLAN.md` | 0daf1c59a15d07ff1e6c436d020c91f378fcd77164bce1d0f5097047aef0b9c2 | 9559 | Markdown | 1 (8 sections) | full text |
| 22 | `reports/OD-H22_3way_valve/INTAKE_CARD.md` | c99136224ad9e48c1e45ab7c29aac3d4d0c3a095475c6d64d7476d5e1b43147f | 9368 | Markdown | 1 (9 sections) | full text |
| 23 | `reports/OD-H22_3way_valve/DECISIONS.md` | 94cee9bc319707338c5cbb47a19069ddeaf09d31a8243da188487ba158bafd03 | 4059 | Markdown | 1 | full text |
| 24 | `reports/OD-H22_3way_valve/limitations.json` | c28b3bd389e9e792c40e677798a30a8c824471c69d017fdf2b6cc29d867bd44b | 5633 | JSON | — | full |
| 25 | `reports/OD-H22_3way_valve/alignment.json` | 81c7bf4635456e8c66d025e9c3aeff849e9e9604ddbee48ba8a59335f860930a | 12174 | JSON | — | full |
| 26 | `reports/OD-H22_3way_valve/overlay.png` | 5d6bdb75058b19481020aede6c43785fe15a02e9c8a830329036d2454766a5a7 | 579974 | PNG | 13-panel scan/CAD overlay | viewed |
| 27 | `reports/OD-H22_3way_valve/photo_4.png` | 9de91f8c39a26ebf09b2ab30314dfa01f24f2fb669052b9013ac2404fbf65b70 | 310551 | PNG | 1 (own photo, no scale) | viewed |
| 28 | `reports/OD-H24_flowmeter/README.md` | d2aea98d5fe91abed0248984c87e24748b620c77fa1629c8c3558b5f5b093e1d | 6316 | Markdown | 1 | full text |
| 29 | `reports/OD-H24_flowmeter/params.json` | be313d27ea9a5f42868ab654aa36bd775402c65d9f5ad3092ed8ea6927ae9b1d | 2303 | JSON | — | full |
| 30 | `reports/OD-H24_flowmeter/tubes.json` | 94751607485990934a4165ab58e77f51c0ce8034c2c4a09836596b022fbf135e | 8223 | JSON | — | full |
| 31 | `reports/OD-H24_flowmeter/export_check.json` | 5a219c3c85af5781291d19b75b577ba596bc649c56ce0304f90c5ec230aacc90 | 1572 | JSON | — | full |
| 32 | `reports/OD-H24_flowmeter/views_cad.png` | ce5d2af215aa4bc6e46fd57d6d795149e7efb8485e6d677e95fe77dc9535a9e6 | 688578 | PNG | 3 iso views (CAD) | viewed |
| 33 | `reports/OD-H24_flowmeter/views_scan.png` | b0afd67311216d8fc6f6aebc2cbd365a6c9fdf07599afae7c478f982aedfce82 | 710660 | PNG | 3 iso views (scan) | viewed |

Note: no `OD-H24_flowmeter/INTAKE_CARD.md`, `DECISIONS.md`, `DELIVER_README.md`, `MODELING_PLAN.md`, or `alignment.json` exist under `reports/OD-H24_flowmeter/` (only the files listed above are present in the workspace and in the brief's input list) — see §5.

## §2 Dimensions

Frames (stated once here, repeated in each part's "What" cell as `[frame]`):
- **OD-H22 datum**: origin = valve axis ∩ flange back face; z=0 = flange back face, +Z = valve axis (towards drive tube/tray side); +X = flange ear axis (fourier_mass n=2, −84.99° clock); ports lie in the YZ plane; theta CCW about +Z from +X; port-local t = distance along port axis from its crossing of y=0.
- **OD-H21 datum**: origin = nozzle OD axis ∩ band top face plane; z=0 (u=0) = band top face (up-facing annular step where body leaves the band ring), +Z(+u) = towards the cap; +X = side-outlet collar outer-face normal (clock 13.878°); theta CCW about +Z from +X.
- **OD-H24 datum**: Z = cup axis (LSQ of wall normals), Z=0 = bottom rim face; inlet (lower) pipe runs toward −Y; connector local frame rotated 5.2° from datum X.

Method legend: table = read from a source table (PARAM_TABLE.md / params.json / DELIVER_README §5), all scan-only (no calipers on any of the three parts — CHK-SCALE flagged on all three; §3 also carries this as a project-wide gap).

Rerun triggers ("critical: yes" rows) are flagged `photo or scaled, not confirmable for fit` because they are scan-authority, fit-critical, and not caliper-verified (skill rule 3).

### OD-H22 3-way valve — dimensions (source: `reports/OD-H22_3way_valve/PARAM_TABLE.md`, `params.json`, `DELIVER_README.md` §5; datum per above)

| ID | What (feature) | Value as given | Unit | Value in mm/deg | ± | File | Location | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-001 | flange plate thickness = flange floor z [OD-H22 datum] | 2.26 (measured 2.262) | mm | 2.26 | 0.036 | #19 | `flange_floor_z` | table | critical; photo or scaled, not confirmable for fit |
| X-002 | tray rim top z [OD-H22 datum] | 5.63 | mm | 5.63 | 0.036 | #19 | `rim_top_z` | table | — |
| X-003 | flange central disc radius | 11.7 (measured 11.697) | mm | 11.7 | 0.036 | #19 | `plate_R` | table | — |
| X-004 | ear hole centre, +X ear | 15.447 | mm | 15.447 | 0.036 | #19 | `ear_hole_x`[0] | table | critical; held per hole, not symmetrised; photo or scaled, not confirmable for fit |
| X-005 | ear hole centre, −X ear | −15.338 | mm | −15.338 | 0.036 | #19 | `ear_hole_x`[1] | table | critical; differs from X-004 by 0.109 mm > noise, kept per instance; photo or scaled, not confirmable for fit |
| X-006 | ear hole radius | 1.936 (measured 1.933/1.939 both holes) | mm | 1.936 | 0.036 | #19 | `ear_hole_r` | table | critical; symmetry rule; photo or scaled, not confirmable for fit |
| X-007 | ear side taper angle | 10.07 | deg | 10.07 | 0.036 | #19 | `ear_side_angle_deg` | table | — |
| X-008 | ear end radius (tangent circle at hole) | 5.484 (measured range 5.254..5.568) | mm | 5.484 | 0.036 | #19 | `ear_end_R` | table | +X tip damaged on specimen (see X-095); −X value 5.568 used as undamaged reference |
| X-009 | outline blend radius (disc/ear concave corner) | 4.617 (measured 4.887/4.346, mean of 2 of 4 corners; other 2 rejected) | mm | 4.617 | 0.27 | #19 | `outline_blend_R` | table | mean-of-n, 2 of 4 corners fitted |
| X-010 | rim wall thickness | 1.447 (measured 1.42/1.444/1.446/1.478) | mm | 1.447 | 0.036 | #19 | `rim_wall_t` | table | mean-of-n |
| X-011 | plate back-edge round radius | 1.868 | mm | 1.868 | 0.04 | #19 | `back_edge_R` | table | — |
| X-012 | boss collar radius (tray side) | 8.06 (measured 8.057) | mm | 8.06 | 0.072 | #19 | `collar_R` | table | — |
| X-013 | boss collar top z | 4.73 (measured 4.734) | mm | 4.73 | 0.036 | #19 | `collar_top_z` | table | — |
| X-014 | drive tube OD radius | 6.203 | mm | 6.203 | 0.074 | #19 | `tube_R` | table | critical; photo or scaled, not confirmable for fit |
| X-015 | drive tube bore radius | 4.561 | mm | 4.561 | 0.101 | #19 | `tube_bore_r` | table | critical; photo or scaled, not confirmable for fit |
| X-016 | drive tube top z (finger tops uneven, p10 13.61/p90 13.92) | 13.68 (measured 13.682) | mm | 13.68 | 0.15 | #19 | `tube_top_z` | table | critical; photo or scaled, not confirmable for fit |
| X-017 | drive tube bore floor z | 1.5 | mm | 1.5 | — | #19 | `tube_bore_bottom_z` | assumed (not scanned) | ASSUMED — bore continues below scan coverage; not a real floor |
| X-018 | drive-tube slot count | 4 | count | 4 | 0 | #19 | `slot_count` | table (FFT pattern) | — |
| X-019 | drive-tube slot 1 angle (near ear axis) | −0.11 | deg | −0.11 | 0.036 | #19 | `slot_theta_deg`[0] | table | critical; held per slot, not snapped to 0/90/180/270; photo or scaled, not confirmable for fit |
| X-020 | drive-tube slot 2 angle | 90.2 | deg | 90.2 | 0.036 | #19 | `slot_theta_deg`[1] | table | critical; same as X-019 |
| X-021 | drive-tube slot 3 angle | 179.79 | deg | 179.79 | 0.036 | #19 | `slot_theta_deg`[2] | table | critical; same as X-019 |
| X-022 | drive-tube slot 4 angle | 269.38 | deg | 269.38 | 0.036 | #19 | `slot_theta_deg`[3] | table | critical; same as X-019 |
| X-023 | drive-tube slot 1 width (ear-axis slot) | 3.086 | mm | 3.086 | 0.036 | #19 | `slot_w`[0] | table | critical; two key sizes: ear-axis slots ≈3.05–3.09, cross slots ≈2.57–2.72 (keyed drive) |
| X-024 | drive-tube slot 2 width (cross slot) | 2.722 | mm | 2.722 | 0.036 | #19 | `slot_w`[1] | table | critical |
| X-025 | drive-tube slot 3 width (ear-axis slot) | 3.041 | mm | 3.041 | 0.036 | #19 | `slot_w`[2] | table | critical |
| X-026 | drive-tube slot 4 width (cross slot) | 2.572 | mm | 2.572 | 0.036 | #19 | `slot_w`[3] | table | critical |
| X-027 | slot bottom z, θ≈0/180 slots | 8.912 (measured 8.907/8.918) | mm | 8.912 | 0.036 | #19 | `slot_bottom_z_x` | table | — |
| X-028 | slot bottom z, θ≈90/270 slots | 8.704 (measured 8.691/8.717) | mm | 8.704 | 0.036 | #19 | `slot_bottom_z_y` | table | — |
| X-029 | stem cylinder radius | 6.547 (measured 6.538/6.547/6.55/6.552) | mm | 6.547 | 0.045 | #19 | `stem_R` | table | mean-of-n |
| X-030 | stem cone half-angle | 40.09 | deg | 40.09 | 0.036 | #19 | `stem_cone_half_angle_deg` | table | — |
| X-031 | stem cone top z (cone/cylinder join) | −4.234 | mm | −4.234 | 0.1 | #19 | `stem_cone_top_z` | table | — |
| X-032 | stem neck radius | 4.074 | mm | 4.074 | 0.075 | #19 | `stem_neck_R` | table | — |
| X-033 | stem neck bottom z (junction with ports) | −19.587 | mm | −19.587 | 0.036 | #19 | `stem_neck_bottom_z` | table | ports and bottom rib branch off below this |
| X-034 | gusset thickness | 1.306 (measured 1.247/1.365) | mm | 1.306 | 0.06 | #19 | `gusset_t` | table | mean-of-n |
| X-035 | gusset angle below horizontal | 43.42 (measured 43.924/42.916) | deg | 43.42 | 0.5 | #19 | `gusset_angle_deg` | table | mean-of-n |
| X-036 | gusset x at z=0 (back face) | 11.085 (measured 11.014/11.155) | mm | 11.085 | 0.1 | #19 | `gusset_x_at_z0` | table | mean-of-n |
| X-037 | port axis elevation, +Y port | 34.059 | deg | 34.059 | 0.3 | #19 | `port_elev_deg`[0] | table | critical; ports differ 0.97° > fit scatter, kept per port; photo or scaled, not confirmable for fit |
| X-038 | port axis elevation, −Y port | 35.03 | deg | 35.03 | 0.3 | #19 | `port_elev_deg`[1] | table | critical; same as X-037 |
| X-039 | port axis z at y=0, +Y port | −14.301 | mm | −14.301 | 0.1 | #19 | `port_axis_z0`[0] | table | axis modelled at x=0 (see X-096 simplification) |
| X-040 | port axis z at y=0, −Y port | −14.42 | mm | −14.42 | 0.1 | #19 | `port_axis_z0`[1] | table | same as X-039 |
| X-041 | port neck radius | 4.173 (measured 4.178/4.168, symmetry) | mm | 4.173 | 0.036 | #19 | `port_neck_R` | table | — |
| X-042 | port sleeve start t, +Y port | 7.25 | mm | 7.25 | 0.1 | #19 | `port_sleeve_t`[0] | table | — |
| X-043 | port sleeve start t, −Y port | 6.85 | mm | 6.85 | 0.1 | #19 | `port_sleeve_t`[1] | table | — |
| X-044 | port sleeve radius | 5.585 (measured 5.578/5.592) | mm | 5.585 | 0.036 | #19 | `port_sleeve_R` | table | symmetry |
| X-045 | port clip-block start t, +Y port | 15.368 | mm | 15.368 | 0.036 | #19 | `port_block_t0`[0] | table | — |
| X-046 | port clip-block start t, −Y port | 15.077 | mm | 15.077 | 0.036 | #19 | `port_block_t0`[1] | table | — |
| X-047 | port clip-block end t, +Y port | 19.022 | mm | 19.022 | 0.036 | #19 | `port_block_t1`[0] | table | — |
| X-048 | port clip-block end t, −Y port | 18.78 | mm | 18.78 | 0.036 | #19 | `port_block_t1`[1] | table | — |
| X-049 | port mouth (end) t, +Y port | 20.054 | mm | 20.054 | 0.036 | #19 | `port_end_t`[0] | table | critical; photo or scaled, not confirmable for fit |
| X-050 | port mouth (end) t, −Y port | 19.873 | mm | 19.873 | 0.036 | #19 | `port_end_t`[1] | table | critical; same as X-049 |
| X-051 | port clip-block half-width u | 5.891 (measured 5.902/5.88) | mm | 5.891 | 0.036 | #19 | `port_block_half_u` | table | critical; symmetry; photo or scaled, not confirmable for fit |
| X-052 | port clip-block half-width v | 5.913 (measured 5.915/5.912) | mm | 5.913 | 0.036 | #19 | `port_block_half_v` | table | critical; symmetry; photo or scaled, not confirmable for fit |
| X-053 | port lip radius | 6.162 (measured 6.164/6.159) | mm | 6.162 | 0.036 | #19 | `port_lip_R` | table | critical; symmetry; photo or scaled, not confirmable for fit |
| X-054 | port bore radius (mouth) | 4.339 (measured 4.342/4.337) | mm | 4.339 | 0.036 | #19 | `port_bore_R` | table | critical; symmetry; photo or scaled, not confirmable for fit |
| X-055 | port clip-block corner round radius | 0.5 | mm | 0.5 | — | #19 | `port_block_corner_R` | assumed (visible, not fitted) | ASSUMED |
| X-056 | port bore step t (bore diameter change) | 16.445 | mm | 16.445 | 0.2 | #19 | `port_bore_step_t` | table | +Y port only; −Y bore not scanned that deep |
| X-057 | port bore radius below step | 3.557 (measured range 3.541..3.581) | mm | 3.557 | 0.05 | #19 | `port_bore2_R` | table | +Y port only |
| X-058 | port inner bore end t | 12.5 | mm | 12.5 | — | #19 | `port_bore2_end_t` | assumed (deepest scanned wall ~13; passage to junction not scanned) | ASSUMED |
| X-059 | port clip-slot near-wall offset from block start | 1.161 (measured 1.152/1.17) | mm | 1.161 | 0.036 | #19 | `port_slot_dt0` | table | symmetry |
| X-060 | port clip-slot width | 1.353 (measured 1.354/1.352) | mm | 1.353 | 0.036 | #19 | `port_slot_w` | table | critical; symmetry; photo or scaled, not confirmable for fit |
| X-061 | port clip-slot inner v extent | 0.932 (measured 0.957/0.907) | mm | 0.932 | 0.036 | #19 | `port_slot_v_in` | table | symmetry |
| X-062 | port clip-slot outer v extent | 4.72 (measured 4.739/4.701) | mm | 4.72 | 0.036 | #19 | `port_slot_v_out` | table | symmetry |
| X-063 | bottom rib thickness | 1.624 | mm | 1.624 | 0.08 | #19 | `rib_t` | table | rib centre x = 0.143 |
| X-064 | bottom rib bottom z | −23.696 | mm | −23.696 | 0.036 | #19 | `rib_bottom_z` | table | — |
| X-065 | bottom rib half-length | 4.5 | mm | 4.5 | — | #19 | `rib_half_len` | assumed (ends buried in port sleeves; any 3.9–5.5 gives same outer surface) | ASSUMED |
| X-066 | overall datum bbox (OD-H22, delivered STEP) | 41.75 × 39.88 × 44.55 | mm | 41.75 × 39.88 × 44.55 | — | #17 | README "Delivered STEP" | title-block / export check | re-import check, 162 faces |
| X-067 | valve axis tilt vs flange normal (assembly warp/design, unresolved) | 0.470 (per-feature 0.485/0.564/0.525, disagree >stderr) | deg | 0.470 | 0.014 (stderr) | #22, #25 | INTAKE_CARD §6, alignment.json `tilt_deg` | table | finding, NOT RESOLVABLE; open question — warp vs moulding design intent |

### OD-H21 anti-drip valve — dimensions (source: `reports/OD-H21_antidrip_valve/PARAM_TABLE.md`, `DELIVER_README.md` §5; datum per above)

| ID | What (feature) | Value as given | Unit | Value in mm/deg | ± | File | Location | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-068 | band top face level (datum primary, u=0 by construction) | 0.0002 | mm | 0.0002 | 0.028 | #11 | `primary_u` | table | — |
| X-069 | nozzle (spigot) radius | 5.7799 | mm | 5.7799 | 0.034 | #11 | `noz_R` | table | critical; photo or scaled, not confirmable for fit |
| X-070 | nozzle axis centre (x,y at z=−18.5) | −0.0036 / 0.0049 | mm | −0.0036 / 0.0049 | 0.034 | #11 | `noz_axis_c` | table | — |
| X-071 | nozzle axis tilt (tx,ty) | −0.6193 / −1.2119 | deg | −0.6193 / −1.2119 | 0.034 | #11 | `noz_axis_tilt` | table | total tilt 1.267° vs band-face normal (CHK-TILT finding) |
| X-072 | nozzle tip level [OD-H21 datum] | −27.3016 | mm | −27.3016 | 0.0362 | #11 | `noz_tip_u` | table | — |
| X-073 | nozzle tip outer round radius | 0.5227 | mm | 0.5227 | 0.0282 | #11 | `noz_tip_round_R` | table | — |
| X-074 | nozzle/shoulder root fillet radius | 0.5096 | mm | 0.5096 | 0.054 | #11 | `noz_root_R` | table | — |
| X-075 | nozzle bore radius | 3.9415 | mm | 3.9415 | 0.1022 | #11 | `noz_bore_R` | table | critical; photo or scaled, not confirmable for fit |
| X-076 | nozzle bore floor level (blind, observed only) | −23.4063 (range −23.6878..−23.1248) | mm | −23.4063 | 0.3 | #11 | `noz_bore_floor_u` | table | ASSUMED depth — real flow bore continues past scanner bridge |
| X-077 | corner lug centre (x,y) | −0.0033 / −0.0477 | mm | −0.0033 / −0.0477 | 0.0524 | #11 | `lug_c` | table | — |
| X-078 | corner lug half-width a (inside nozzle cylinder side) | 5.634 | mm | 5.634 | 0.0524 | #11 | `lug_half_a` | table | band-to-band spread 5.251..5.634 |
| X-079 | corner lug half-width b (latch-window side) | 5.9639 | mm | 5.9639 | 0.0524 | #11 | `lug_half_b` | table | critical; photo or scaled, not confirmable for fit |
| X-080 | corner lug corner radius | 0.4931 | mm | 0.4931 | 0.0524 | #11 | `lug_corner_R` | table | — |
| X-081 | corner lug orientation angle | 23.9706 | deg | 23.9706 | 0.0524 | #11 | `lug_phi_deg` | table | — |
| X-082 | corner lug z range, low | −25.7555 | mm | −25.7555 | 0.0947 | #11 | `lug_u_lo` | table | median over 4 corners |
| X-083 | corner lug z range, high | −23.1261 | mm | −23.1261 | 0.0287 | #11 | `lug_u_hi` | table | median over 4 corners |
| X-084 | latch window z range, low | −25.3037 / −25.2525 | mm | −25.3037 / −25.2525 | 0.1 | #11 | `latch_u_lo` | table | 2 measured edges (it2 revision) |
| X-085 | latch window z range, high | −24.168 / −24.5909 | mm | −24.168 / −24.5909 | 0.1 | #11 | `latch_u_hi` | table | 2 measured edges |
| X-086 | latch window through-angle span | 82.9706 / 137.971 | deg | 82.9706 / 137.971 | 1 | #11 | `latch_through_theta` | table | window open through wall to bore/bridge |
| X-087 | latch cut-back depth (2 sides, it2 finding) | 5.4247 / 5.5724 | mm | 5.4247 / 5.5724 | 0.1 | #11 | `latch_cut_d` | table | floor plane parallel to b-side flat; supersedes it1 cylindrical-floor model |
| X-088 | latch cut lateral extent y0 | −4.3929 / −4.1991 | mm | −4.3929 / −4.1991 | 0.2 | #11 | `latch_cut_y0` | table | — |
| X-089 | latch cut lateral extent y1 | 4.0878 / 4.0486 | mm | 4.0878 / 4.0486 | 0.2 | #11 | `latch_cut_y1` | table | — |
| X-090 | nozzle shoulder level (nut bottom face) | −14.037 | mm | −14.037 | 0.0581 | #11 | `nut_shoulder_u` | table | — |
| X-091 | nut base radius (drafted cone, between ribs) | 10.8335 | mm | 10.8335 | 0.0314 | #11 | `nut_R0` | table | at z0=−10 |
| X-092 | nut axis centre | −0.067 / −0.1553 | mm | −0.067 / −0.1553 | 0.0314 | #11 | `nut_axis_c` | table | — |
| X-093 | nut cone draft (dρ/du) | 0.0311 | mm/mm | 0.0311 | 0.0314 | #11 | `nut_k` | table | draft 1.781° |
| X-094 | nut→band chamfer start level | −6.7794 | mm | −6.7794 | 0.1208 | #11 | `nut_chamfer_u0` | table | — |
| X-095 | nut→band chamfer end level | −6.15 | mm | −6.15 | 0.1208 | #11 | `nut_top_u` | table | — |
| X-096 | nut→band chamfer radius at end level | 11.6626 | mm | 11.6626 | 0.1208 | #11 | `nut_top_rho` | table | — |
| X-097 | nut rib count | 8 | count | 8 | 0 | #11 | `rib_count` | table (FFT pattern) | pitch 44.9–45.4°, phase 23.75±0.25 |
| X-098 | nut rib angular positions (8 instances) | −156.364 / −110.936 / −66.0427 / −21.1463 / 23.8071 / 68.7206 / 113.629 / 158.66 | deg | (as given) | 0.3 | #11 | `rib_theta_deg` | table | 8 ribs, per-instance |
| X-099 | nut rib rod-centre radius (8 instances) | 10.6615 / 10.501 / 10.5797 / 10.6452 / 10.4459 / 10.5318 / 10.5361 / 10.601 | mm | (as given) | 0.1 | #11 | `rib_rho_c` | table | 8 ribs, per-instance |
| X-100 | nut rib rod radius (8 instances) | 1.3415 / 1.421 / 1.4451 / 1.4158 / 1.5281 / 1.4255 / 1.433 / 1.3824 | mm | (as given) | 0.1 | #11 | `rib_rod_R` | table | 8 ribs, per-instance |
| X-101 | band lower ring radius (drafted, between outlet sector) | 12.2048 | mm | 12.2048 | 0.0611 | #11 | `bandlo_R0` | table | at z0=−4.35 |
| X-102 | band lower ring axis centre | −0.096 / −0.2359 | mm | −0.096 / −0.2359 | 0.0611 | #11 | `bandlo_axis_c` | table | — |
| X-103 | band lower ring base level (nut→band transition end) | −5.6 | mm | −5.6 | 0.1 | #11 | `bandlo_base_u` | table | — |
| X-104 | band lower ring draft | 0.051 | mm/mm | 0.051 | 0.0611 | #11 | `bandlo_k` | table | draft 2.92° |
| X-105 | band step level (up-facing) | −2.5407 | mm | −2.5407 | 0.0655 | #11 | `band_step_u` | table | — |
| X-106 | band upper ring radius | 12.0089 | mm | 12.0089 | 0.044 | #11 | `bandup_R` | table | cylinder, z −2.3..−0.75 |
| X-107 | band upper ring axis centre | 0.1076 / −0.196 | mm | 0.1076 / −0.196 | 0.044 | #11 | `bandup_axis_c` | table | — |
| X-108 | band upper top edge round radius | 0.5647 | mm | 0.5647 | 0.0369 | #11 | `bandup_top_round_R` | table | — |
| X-109 | body cylinder radius | 10.0218 | mm | 10.0218 | 0.0601 | #11 | `body_R` | table | outlet sector ±35° excluded |
| X-110 | body cylinder axis centre | 0.1495 / −0.1614 | mm | 0.1495 / −0.1614 | 0.0601 | #11 | `body_axis_c` | table | — |
| X-111 | outlet ring skirt radius (ring portion of cap part) | 13.2709 | mm | 13.2709 | 0.0512 | #11 | `ring_R` | table | windows excluded |
| X-112 | cap radius (cap portion of cap part) | 12.1411 | mm | 12.1411 | 0.0349 | #11 | `cap_R` | table | barb sector excluded |
| X-113 | cap-part axis centre | 0.1136 / −0.1879 | mm | 0.1136 / −0.1879 | 0.0349 | #11 | `cap_axis_c` | table | joint ring+cap fit |
| X-114 | cap-part axis tilt | 2.8553 / −1.7752 | deg | 2.8553 / −1.7752 | 0.0349 | #11 | `cap_axis_tilt` | table | total tilt 3.361° vs band normal (as-scanned assembly state) |
| X-115 | ring bottom level | 9.5778 | mm | 9.5778 | 0.0863 | #11 | `ring_bottom_u` | table | — |
| X-116 | ring bottom outer edge round radius | 0.8026 | mm | 0.8026 | 0.0785 | #11 | `ring_bottom_round_R` | table | — |
| X-117 | ring top level | 16.817 | mm | 16.817 | 0.0688 | #11 | `ring_top_u` | table | — |
| X-118 | ring top outer edge round radius | 0.5206 | mm | 0.5206 | 0.0405 | #11 | `ring_top_round_R` | table | — |
| X-119 | cap root fillet radius (concave) | 0.4232 | mm | 0.4232 | 0.0373 | #11 | `cap_root_R` | table | — |
| X-120 | cap top level | 23.2744 | mm | 23.2744 | 0.0584 | #11 | `cap_top_u` | table | — |
| X-121 | cap top edge round radius | 0.5583 | mm | 0.5583 | 0.0381 | #11 | `cap_top_round_R` | table | — |
| X-122 | ring window 1 z-range low / high (θ≈−67) | 12.4 / 14.6 | mm | 12.4 / 14.6 | 0.2 | #11 | `win_u_lo`[0] / `win_u_hi`[0] | table | it2 revised; window instance 1 |
| X-123 | ring window 2 z-range low / high (θ≈0) | 12.4 / 14.0 | mm | 12.4 / 14.0 | 0.2 | #11 | `win_u_lo`[1] / `win_u_hi`[1] | table | it2 revised; window instance 2 |
| X-124 | ring window 3 z-range low / high (θ≈112) | 12.4 / 14.4 | mm | 12.4 / 14.4 | 0.2 | #11 | `win_u_lo`[2] / `win_u_hi`[2] | table | it2 revised; window instance 3 |
| X-125 | ring window 4 z-range low / high (θ≈180) | 12.6 / 14.2 | mm | 12.6 / 14.2 | 0.2 | #11 | `win_u_lo`[3] / `win_u_hi`[3] | table | it2 revised; window instance 4 |
| X-126 | ring window floor radius, windows 1–4 | 11.9258 / 12.1263 / 11.4953 / 11.9058 | mm | (as given) | 0.4 | #11 | `win_floor_rho` | table | per-instance; window 3 deeper (see X-129) |
| X-127 | ring window angular span, window 1 | −74.75 to −58.75 | deg | (as given) | 1 | #11 | `win_theta0_deg`[0] / `win_theta1_deg`[0] | table | — |
| X-128 | ring window angular span, window 2 | −8.25 to 8.75 | deg | (as given) | 1 | #11 | `win_theta0_deg`[1] / `win_theta1_deg`[1] | table | — |
| X-128b | ring window angular span, window 3 | 103 to 121 | deg | (as given) | 1 | #11 | `win_theta0_deg`[2] / `win_theta1_deg`[2] | table | — |
| X-128c | ring window angular span, window 4 | 174 to −173 | deg | (as given) | 1 | #11 | `win_theta0_deg`[3] / `win_theta1_deg`[3] | table | — |
| X-129 | ring window 3 deep-cell extra span (opens into skirt/body gap) | θ 104–116, z 12.8–14, floor ρ 10.5134 | deg / mm | (as given) | 0.2–1 | #11 | `win_deep_theta`, `win_deep_u`, `win_deep_floor_rho` | table | window near 110° only |
| X-130 | skirt slit 1 angular span | −158.135 to −140.135 | deg | (as given) | 1 | #11 | `slit_theta0_deg`[0] / `slit_theta1_deg`[0] | table | it2 revised; not modelled as open (interior gap) |
| X-131 | skirt slit 2 angular span | 151.607 to 172.607 | deg | (as given) | 1 | #11 | `slit_theta0_deg`[1] / `slit_theta1_deg`[1] | table | it2 revised |
| X-132 | skirt slit ceiling level, slit 1 / 2 | 10.8622 / 10.9502 | mm | (as given) | 0.1 | #11 | `slit_u_top` | table | — |
| X-133 | skirt slit inner radius, slit 1 / 2 | 10.0568 / 10.0127 | mm | (as given) | 0.1 | #11 | `slit_rho_in` | table | — |
| X-134 | skirt slit outer radius, slit 1 / 2 | 10.7359 / 10.6312 | mm | (as given) | 0.1 | #11 | `slit_rho_out` | table | — |
| X-135 | outlet-to-ring web half-width at x=10.5 | 3.5278 | mm | 3.5278 | 0.179 | #11 | `web_hw_at_10p5` | table | — |
| X-136 | outlet-to-ring web half-width slope | −1.3759 | mm/mm | −1.3759 | 0.179 | #11 | `web_hw_slope` | table | — |
| X-137 | outlet-to-ring web centre y | −0.4327 | mm | −0.4327 | 0.179 | #11 | `web_y_centre` | table | — |
| X-138 | side outlet tube radius | 4.6084 | mm | 4.6084 | 0.05 | #11 | `out_tube_R` | table | — |
| X-139 | side outlet tube/collar root fillet | 0.5272 | mm | 0.5272 | 0.0821 | #11 | `out_root_R` | table | — |
| X-140 | outlet collar inner-face level | 20.0062 | mm | 20.0062 | 0.0542 | #11 | `out_collar_in_u` | table | — |
| X-141 | outlet collar radius | 6.8482 | mm | 6.8482 | 0.0348 | #11 | `out_collar_R` | table | critical; photo or scaled, not confirmable for fit |
| X-142 | outlet collar round radius | 1.0766 | mm | 1.0766 | 0.0442 | #11 | `out_collar_round_R` | table | — |
| X-143 | outlet collar outer-face level (clock plane) | 22.706 | mm | 22.706 | 0.0324 | #11 | `out_collar_out_u` | table | defines +X clock |
| X-144 | O-ring section centre level | 23.5965 | mm | 23.5965 | 0.0889 | #11 | `oring_u` | table | critical; photo or scaled, not confirmable for fit |
| X-145 | O-ring torus major radius | 4.4273 | mm | 4.4273 | 0.0889 | #11 | `oring_rho` | table | critical; photo or scaled, not confirmable for fit |
| X-146 | O-ring torus minor (section) radius | 0.9153 | mm | 0.9153 | 0.0889 | #11 | `oring_a` | table | critical; photo or scaled, not confirmable for fit; O-ring fused to outlet, joint invented (L3) |
| X-147 | outlet end bore radius | 1.5923 | mm | 1.5923 | 0.0987 | #11 | `out_bore_R` | table | — |
| X-148 | outlet end bore floor level (blind, observed) | 29.2112 (range 28.3385..30.084) | mm | 29.2112 | 0.6 | #11 | `out_bore_floor_u` | table | ASSUMED depth |
| X-149 | outlet end chamfer slope | −0.4463 | mm/mm | −0.4463 | 0.05 | #11 | `out_chamfer_slope` | table | — |
| X-150 | outlet end chamfer radius at start | 4.3882 | mm | 4.3882 | 0.05 | #11 | `out_chamfer_rho0` | table | at u 29.3 |
| X-151 | outlet end face level | 29.9816 | mm | 29.9816 | 0.0359 | #11 | `out_end_u` | table | — |
| X-152 | outlet thread mean radius (modelled as plain cylinder) | 4.4169 | mm | 4.4169 | 0.1829 | #11 | `out_thread_R` | table | critical; scan-smoothed, plain cylinder not real thread; photo or scaled, not confirmable for fit |
| X-153 | outlet thread pitch (for ID only, ≈28 TPI / G1/8, not modelled) | 0.908 | mm | 0.908 | 0.01 | #11 | `out_thread_pitch` | table | recorded for identification only, not modelled |
| X-154 | side outlet axis point | 0.0008 / −0.1633 / 3.4172 | mm | (as given) | 0.05 | #12 | `outlet_axis_p` | table | — |
| X-155 | side outlet axis direction | 1 / 0.0048 / 0.0076 | (unit) | (as given) | 0.05 | #12 | `outlet_axis_d` | table | unit vector |
| X-156 | barb tube taper radius at u=17.5 | 2.7516 | mm | 2.7516 | 0.0425 | #11 | `barb_R0` | table | critical; photo or scaled, not confirmable for fit |
| X-157 | barb tube taper slope | −0.0084 | mm/mm | −0.0084 | 0.0425 | #11 | `barb_k` | table | tube narrows outward |
| X-158 | barb rear end face level | −2.9976 | mm | −2.9976 | 0.0661 | #11 | `barb_rear_u` | table | — |
| X-159 | barb rear end round radius | 0.9344 | mm | 0.9344 | 0.0798 | #11 | `barb_rear_round_R` | table | — |
| X-160 | barb flare slope | 0.6245 | mm/mm | 0.6245 | 0.2641 | #11 | `barb_flare_slope` | table | — |
| X-161 | barb flare radius at u=23.6 | 2.823 | mm | 2.823 | 0.2641 | #11 | `barb_flare_rho0` | table | — |
| X-162 | barb bulb cone centre offset | 0.1744 / −0.0616 | mm | (as given) | 0.067 | #11 | `bulb_offset` | table | — |
| X-163 | barb bulb cone radius at u=26.5 | 3.3506 | mm | 3.3506 | 0.067 | #11 | `bulb_R0` | table | critical; photo or scaled, not confirmable for fit |
| X-164 | barb bulb cone slope | −0.2775 | mm/mm | −0.2775 | 0.067 | #11 | `bulb_k` | table | half-angle 15.51° |
| X-165 | barb end face level | 28.3727 | mm | 28.3727 | 0.067 | #11 | `barb_end_u` | table | — |
| X-166 | barb end bore radius | 1.2518 | mm | 1.2518 | 0.0951 | #11 | `barb_bore_R` | table | — |
| X-167 | barb end bore floor level (blind, observed) | 27.2827 (range 26.6189..27.9464) | mm | 27.2827 | 0.4 | #11 | `barb_bore_floor_u` | table | ASSUMED depth |
| X-168 | barb axis point | 0.4488 / −0.3066 / 24.2486 | mm | (as given) | 0.0478 | #11 | `barb_axis_p` | table | — |
| X-169 | barb axis direction | 0.5641 / 0.8257 / 0.0082 | (unit) | (as given) | 0.0478 | #11 | `barb_axis_d` | table | unit vector, az 55.66° elev 0.469° |
| X-170 | overall datum bbox (OD-H21, delivered STEP) | 43.49 × 38.18 × 55.80 | mm | 43.49 × 38.18 × 55.80 | — | #9 | README "Delivered STEP" | title-block / export check | re-import check, 146 faces |
| X-171 | nozzle tilt vs band-face normal (as-scanned assembly state, finding) | 1.267 | deg | 1.267 | 0.032 | #12 | INTAKE_CARD §6, `tilt_deg` | table | finding; nozzle really tilted vs band; body square (0.11°); cap tilted 3.36° |

### OD-H24 flowmeter — dimensions (source: `reports/OD-H24_flowmeter/params.json`, `tubes.json`, `README.md`; datum per above)

| ID | What (feature) | Value as given | Unit | Value in mm/deg | ± | File | Location | Method | Flags |
|---|---|---|---|---|---|---|---|---|---|
| X-172 | body panel level | 2.0 | mm | 2.0 | — | #29 | `z_panel` | table (params.json) | photo or scaled, not confirmable for fit (no ± given in source) |
| X-173 | rim inner radius | 13.98 | mm | 13.98 | — | #29 | `r_rim_in` | table | same flag |
| X-174 | rim face level (datum Z=0) | 0.0 | mm | 0.0 | — | #29 | `z_rim` | table | datum origin plane |
| X-175 | cup radius at rim (drafted) | 15.71 | mm | 15.71 | — | #29 | `r_cup0` | table | — |
| X-176 | cup draft (dρ/dz) | 0.0195 | mm/mm | 0.0195 | — | #29 | `cup_draft` | table | ≈1.1° |
| X-177 | cup/skirt groove top level | 14.7 | mm | 14.7 | — | #29 | `z_groove_top` | table | skirt-gap depth only partly seen — estimated (README) |
| X-178 | skirt inner radius | 17.1 | mm | 17.1 | — | #29 | `r_skirt_in` | table | cup-to-skirt gap radius 15.99→17.1 per README feature-tree text |
| X-179 | flange underside level | 12.67 | mm | 12.67 | — | #29 | `z_flange_under` | table | — |
| X-180 | flange outer radius, lower | 20.25 | mm | 20.25 | — | #29 | `r_flange0` | table | flange outer r 20.25→20.37 (README) |
| X-181 | flange outer radius, upper | 20.37 | mm | 20.37 | — | #29 | `r_flange1` | table | — |
| X-182 | flange top level | 19.9 | mm | 19.9 | — | #29 | `z_flange_top` | table | — |
| X-183 | centre hub radius (boss) | 7.95 | mm | 7.95 | — | #29 | `r_boss` | table | also used as window inner radius (X-192) |
| X-184 | centre hub top level | 21.87 | mm | 21.87 | — | #29 | `z_boss_top` | table | — |
| X-185 | fillet: rim outer | 0.3 | mm | 0.3 | — | #29 | `f_rim_out` | table | — |
| X-186 | fillet: rim inner | 0.3 | mm | 0.3 | — | #29 | `f_rim_in` | table | — |
| X-187 | fillet: panel | 0.5 | mm | 0.5 | — | #29 | `f_panel` | table | — |
| X-188 | fillet: flange top | 0.6 | mm | 0.6 | — | #29 | `f_flange_top` | table | — |
| X-189 | fillet: flange underside | 0.4 | mm | 0.4 | — | #29 | `f_flange_under` | table | — |
| X-190 | base hub disc centre (x,y) | 0.15 / −0.05 | mm | 0.15 / −0.05 | — | #29 | `hub_c` | table | — |
| X-191 | base hub disc radius | 3.59 | mm | 3.59 | — | #29 | `r_hub` | table | README states Ø7.18 (= 2×3.59) |
| X-192 | base rib level | 0.1 | mm | 0.1 | — | #29 | `z_rib` | table | — |
| X-193 | base radial rib width (4 ribs, ±X/±Y) | 1.2 | mm | 1.2 | — | #29 | `spoke_w` | table | 4 ribs |
| X-194 | rotor axle pin 1 centre (x,y) | 0.185 / 0.093 | mm | 0.185 / 0.093 | — | #29 | `pin1.c` | table | — |
| X-195 | rotor axle pin 1 diameter | 3.8 | mm | 3.8 | — | #29 | `pin1.d` | table | — |
| X-196 | rotor axle pin 1 bottom level | −7.03 | mm | −7.03 | — | #29 | `pin1.z0` | table | — |
| X-197 | rotor axle pin 1 chamfer | 0.4 | mm | 0.4 | — | #29 | `pin1.ch` | table | — |
| X-198 | second pin 2 centre (x,y) | −11.78 / 0.14 | mm | −11.78 / 0.14 | — | #29 | `pin2.c` | table | — |
| X-199 | second pin 2 diameter | 2.8 | mm | 2.8 | — | #29 | `pin2.d` | table | — |
| X-200 | second pin 2 bottom level | −5.46 | mm | −5.46 | — | #29 | `pin2.z0` | table | — |
| X-201 | second pin 2 chamfer | 0.3 | mm | 0.3 | — | #29 | `pin2.ch` | table | — |
| X-202 | flange arc window radial span | 7.95 – 12.45 | mm | 7.95 – 12.45 | — | #29 | `win_r` | table | 4 windows share this radial span |
| X-203 | flange arc window floor level | 15.0 | mm | 15.0 | — | #29 | `win_floor` | table | blind pocket; internal rotor/partition shows through in scan (README) |
| X-204 | flange arc window 1 angular span | 69.4 – 121.6 | deg | 69.4 – 121.6 | — | #29 | `win_ang`[0] | table | window instance 1 |
| X-205 | flange arc window 2 angular span | 129.3 – 182.0 | deg | 129.3 – 182.0 | — | #29 | `win_ang`[1] | table | window instance 2 |
| X-206 | flange arc window 3 angular span | 189.4 – 236.5 | deg | 189.4 – 236.5 | — | #29 | `win_ang`[2] | table | window instance 3; upper pipe passes through 236–266° gap |
| X-207 | flange arc window 4 angular span | 266.0 – 302.2 | deg | 266.0 – 302.2 | — | #29 | `win_ang`[3] | table | window instance 4 |
| X-208 | tangential outer slot radius | 17.83 | mm | 17.83 | — | #29 | `slot_r` | table | 4 slots |
| X-209 | tangential outer slot length | 8.6 | mm | 8.6 | — | #29 | `slot_L` | table | — |
| X-210 | tangential outer slot width | 2.15 | mm | 2.15 | — | #29 | `slot_W` | table | 58% of flange deviation error from irregular flash/tab remnants in these slots (README) |
| X-211 | tangential outer slot corner round | 0.5 | mm | 0.5 | — | #29 | `slot_cr` | table | — |
| X-212 | tangential outer slot floor level | 17.25 | mm | 17.25 | — | #29 | `slot_floor` | table | — |
| X-213 | tangential outer slot start angle | 26.5 | deg | 26.5 | — | #29 | `slot_ang0` | table | 90° pattern from this angle |
| X-214 | tangential outer slot count | 4 | count | 4 | — | #29 | `slot_n` | table | — |
| X-215 | connector local frame rotation | 5.2 | deg | 5.2 | — | #29 | `conn_ang` | table | — |
| X-216 | connector arc chord/offset | 6.1 | mm | 6.1 | — | #29 | `conn_arc_c` | table | — |
| X-217 | connector half-round radius | 6.5 | mm | 6.5 | — | #29 | `conn_R` | table | — |
| X-218 | connector far-end arc radius (about body axis) | 17.0 | mm | 17.0 | — | #29 | `conn_end_R` | table | — |
| X-219 | connector top level | 24.04 | mm | 24.04 | — | #29 | `z_conn_top` | table | — |
| X-220 | connector pin x position (local frame) | 10.68 | mm | 10.68 | — | #29 | `pin_x` | table | — |
| X-221 | connector pin pitch | 3.96 (≈0.156") | mm | 3.96 | — | #29 | `pin_pitch` | table | critical to mating connector; suggested caliper check (README) |
| X-222 | connector pin square side | 1.2 | mm | 1.2 | — | #29 | `pin_a` | table | 3 pins |
| X-223 | connector pin top level | 36.5 | mm | 36.5 | — | #29 | `pin_top` | table | — |
| X-224 | connector pin chamfer | 0.4 | mm | 0.4 | — | #29 | `pin_ch` | table | — |
| X-225 | connector pin frustum base x position | 10.75 | mm | 10.75 | — | #29 | `frustum_x` | table | — |
| X-226 | connector pin frustum base size | 3.3 × 3.1 | mm | 3.3 × 3.1 | — | #29 | `frustum_bot` | table | — |
| X-227 | connector pin frustum taper | 10.5 | deg | 10.5 | — | #29 | `frustum_taper` | table | draft angle |
| X-228 | connector pin frustum top level | 27.0 | mm | 27.0 | — | #29 | `z_frustum_top` | table | — |
| X-229 | connector back plate x positions | 13.8 / 15.35 | mm | 13.8 / 15.35 | — | #29 | `plate_x` | table | 3 plates with forward hooks |
| X-230 | connector back plate width | 3.0 | mm | 3.0 | — | #29 | `plate_w` | table | — |
| X-231 | connector back plate top level | 32.4 | mm | 32.4 | — | #29 | `z_plate_top` | table | — |
| X-232 | connector hook x0 | 12.5 | mm | 12.5 | — | #29 | `hook_x0` | table | — |
| X-233 | connector hook z0 | 29.8 | mm | 29.8 | — | #29 | `z_hook0` | table | — |
| X-234 | inlet (lower) pipe axis origin | −10.613 / 0.0 / 7.527 | mm | (as given) | — | #29, #30 | `tube_low.p0` | table | tangential pipe |
| X-235 | inlet (lower) pipe axis direction | 0.0096 / −0.9998 / −0.0156 | (unit) | (as given) | — | #29, #30 | `tube_low.d` | table | runs toward −Y |
| X-236 | inlet pipe OD (main run) | 5.96 (2×2.98, profile s=6..19.9) | mm | 5.96 | — | #29, #30 | `tube_low.prof` | table (README summary + profile array) | README states Ø5.96; profile table in tubes.json gives per-station radius |
| X-237 | inlet pipe collar OD (barb bead 1, s≈20.6–21.3) | 6.86 (2×3.43) | mm | 6.86 | — | #29, #30 | `tube_low.prof` | table | — |
| X-238 | inlet pipe bead OD (barb bead 2, s≈31.3–31.9) | 6.32 (2×3.16) | mm | 6.32 | — | #29, #30 | `tube_low.prof` | table | — |
| X-239 | inlet pipe tip s (end of profile) | 35.9 | mm | 35.9 | — | #29 | `tube_low` profile last station | table | — |
| X-240 | inlet pipe end bore diameter × depth | 3.5 × 3.0 | mm | 3.5 × 3.0 | — | #29 | `tube_low.bore_d` / `bore_depth` | table | blind bore, visible depth only |
| X-241 | outlet (upper) pipe axis origin | −4.43 / −0.442 / 20.254 | mm | (as given) | — | #29, #30 | `tube_up.p0` | table | tangential pipe |
| X-242 | outlet (upper) pipe axis direction | 0.0993 / −0.9949 / −0.0188 | (unit) | (as given) | — | #29, #30 | `tube_up.d` | table | runs toward −Y |
| X-243 | outlet pipe OD (main run) | 5.78 (2×2.89, profile s=0–19.5) | mm | 5.78 | — | #29, #30 | `tube_up.prof` | table | README states Ø5.78 |
| X-244 | outlet pipe collar OD (at flange edge, s≈19.6–21.3) | 6.8 (2×3.4) | mm | 6.8 | — | #29, #30 | `tube_up.prof` | table | collar at the flange edge (README) |
| X-245 | outlet pipe bead OD (s≈31.3–31.9) | 6.2 (2×3.1) | mm | 6.2 | — | #29, #30 | `tube_up.prof` | table | — |
| X-246 | outlet pipe tip s (end of profile) | 36.2 | mm | 36.2 | — | #29 | `tube_up` profile last station | table | — |
| X-247 | outlet pipe end bore diameter × depth | 4.0 × 3.0 | mm | 4.0 × 3.0 | — | #29 | `tube_up.bore_d` / `bore_depth` | table | blind bore, visible depth only |
| X-248 | overall datum bbox (OD-H24, delivered STEP) | 40.72 × 57.07 × 43.53 | mm | 40.72 × 57.07 × 43.53 | — | #28 | README "Deliverables"; #31 export_check.json bbox_min/max | title-block / export check | re-import check, 203 faces, volume 19858.9 mm³ |
| X-249 | part warp (flange tilt, upper vs lower planes disagree) | upper planes 0.6–0.9° one way, lower planes 0.8–0.9° the other (~1.5° wedge) | deg | ~1.5° wedge | — | #28 | README "Verdict: PARTIAL" | table (prose in README, no JSON field) | finding; modelled square to axis (design intent) → ±0.2 mm at flange edge |

## §3 Requirements and constraints

| ID | Requirement | Source quote | File | Location |
|---|---|---|---|---|
| X-250 | Part identity and function | "`chassis/README.md` order-of-work row 5: OD-C07 valve and flowmeter mount, designed against OD-H21 (anti-drip valve), OD-H22 (3-way valve), OD-H24 (flowmeter); blocked by nothing." | #1 | REQUEST.md, "What OD-C07 is" |
| X-251 | BOM identity | "OD-C07, OD-C00, PRINT, \"Valve & flowmeter mount (OPV reachable without disassembly)\", qty 1, DESIGN, PETG, printed, issue #6, proposed" | #2 | bom_rows.csv row OD-C07 |
| X-252 | Material | "material_spec" column = PETG for OD-C07 | #2 | bom_rows.csv row OD-C07 |
| X-253 | Material | "material_spec" column = ASA for OD-C01 (the part OD-C07 mounts to; not yet designed) | #2 | bom_rows.csv row OD-C01 |
| X-254 | Deliverable format | "one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated" | #3 | CHASSIS_README.md, "Goal" |
| X-255 | Assembly integration | "the top assembly `OD-000` as a STEP that places every printed part and every OEM part of the `step/` library by joints" | #3 | CHASSIS_README.md, "Goal" |
| X-256 | Validation gate | "`validated` needs a print and a fit check by the Usta" | #3 | CHASSIS_README.md, "Goal" |
| X-257 | OPV accessibility | "An open chassis should make the OPV accessible without disassembly." | #5, #1 | SOURCING_GUIDE.md §3.5; REQUEST.md project rules |
| X-258 | OPV / mod-friendly note | "the OPV spring is where people do the \"9-bar mod\" (community-documented for Dedica). An open chassis should make the OPV accessible without disassembly." | #5 | SOURCING_GUIDE.md §3.5 |
| X-259 | Two-zone layout | "Wet zone (tank, pump, thermoblock, valves) physically separated from the electric zone (PCB/controller, SSR, mains) ... a printed bulkhead + drainage path so a leak drips to the tray, not the PCB." | #5 | SOURCING_GUIDE.md §6.1 |
| X-260 | Anti-vibration | "Copy OEM anti-vibration. Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." | #5 | SOURCING_GUIDE.md §6.2 |
| X-261 | Thermal map | "Respect the thermal map. Thermoblock and its 192 °C TCO stay clear of printed walls; SSR on an aluminium plate; ABS/ASA near heat, PETG elsewhere, PLA nowhere structural." | #5 | SOURCING_GUIDE.md §6.3 |
| X-262 | Serviceability | "Serviceability is the point. ... top + back panels removable with 4 screws each, OPV reachable, gaskets replaceable without unhousing the thermoblock." | #5 | SOURCING_GUIDE.md §6.4 |
| X-263 | Envelope / mug clearance | "Design for the mug. Group head height ≥ 95 mm above tray ... keep the 0.4 m³ envelope limit from the thesis spec." | #5 | SOURCING_GUIDE.md §6.5 |
| X-264 | Sensor bosses (future) | "Leave sensor bosses (M3/M4 on thermoblock, tee for a thermocouple between heater and group head) in the chassis design from day one." | #5 | SOURCING_GUIDE.md §6.6 |
| X-265 | Piping / safety rating | "piping rated 125 °C / 15 bar, TCO always in the heater circuit, PAT-testable build, RCD during all testing." | #5 | SOURCING_GUIDE.md §6.7 |
| X-266 | Safety banner (mains/pressure) | "This machine runs on mains voltage (230 V or 120 V), heats water to ~125 °C, and pressurizes it to 15 bar. Anything you build must keep the wet side separated from the electric side ... Never print load-bearing or heat-adjacent parts in PLA." | #5 | SOURCING_GUIDE.md, top safety banner |
| X-267 | Fasteners | "Fasteners are the project standard: M3 heat-set inserts (OD-F01) and M3 × 8 screws (OD-F02)." | #1 | REQUEST.md, project rules |
| X-268 | Fastener BOM row, insert | "OD-F01, OD-000, STD, M3 heat-set insert, ~40, VENDOR, brass M3, AliExpress, 10 (set)" | #2 | bom_rows.csv |
| X-269 | Fastener BOM row, screw | "OD-F02, OD-000, STD, M3×8 screw, ~40, VENDOR, ISO 7380 / DIN 912 A2, AliExpress" | #2 | bom_rows.csv |
| X-270 | Machines / nozzle | "Machines: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large panels: PETG), 0.4 mm nozzles; build volumes not yet recorded in the machine files." | #1 | REQUEST.md, project rules |
| X-271 | OD-C01 relationship | "The base frame OD-C01 (which OD-C07 mounts to) is not designed yet ... OD-C07 therefore defines its own mounting footprint, which OD-C01 will follow." | #1 | REQUEST.md, project rules |
| X-272 | Unscanned neighbours | "Not scanned yet: the tubes (OD-H25 flowmeter–pump tube, OD-W11 tank–flowmeter tube), the tank seat OD-W03 side of the water path, the pump OD-H01 position (OD-C03 is not designed yet)." | #1 | REQUEST.md, project rules |
| X-273 | Scan-only caveat (all 3 reference parts) | "The three OEM parts exist as scan-rebuilt STEP files ... with their reverse-engineering reports. None has caliper measurements: every dimension comes from the scan, scale unverified." | #1 | REQUEST.md, "What OD-C07 is" |
| X-274 | Water path: tank → flowmeter | "Water tank `OD-W01` → Flowmeter `OD-H24` | `OD-W11` (L270) | cold | Tank outlet valve seat" | #4 | WATER_FLOW.md table row 1 |
| X-275 | Water path: flowmeter → pump | "Flowmeter `OD-H24` → Pump `OD-H01` | `OD-H25` | cold | Flowmeter pulses are used for volumetric dosing" | #4 | WATER_FLOW.md table row 2 |
| X-276 | Water path: pump → 3-way valve | "Pump `OD-H01` → 3-way valve `OD-H22` | TUBE 1 | cold, up to 15 bar | ULKA EP5 vibratory pump" | #4 | WATER_FLOW.md table row 3 |
| X-277 | Water path: 3-way valve → thermoblock | "3-way valve `OD-H22` → Thermoblock `OD-H11` | TUBE 2 | cold, pressurised" | #4 | WATER_FLOW.md table row 4 |
| X-278 | Water path: 3-way valve → tank (bypass) | "3-way valve `OD-H22` → Water tank `OD-W01` | TUBE 3 | cold | Bypass / over-pressure return" | #4 | WATER_FLOW.md table row 5 |
| X-279 | Anti-drip valve position (not in WATER_FLOW table) | OD-H21 (anti-drip valve) does not appear in the WATER_FLOW.md flow table at all — its position in the flow path is not stated in this input | #4 | WATER_FLOW.md (absence noted) |
| X-280 | Valve BOM identity, OD-H21 | "OD-H21,OD-H00,OEM,Anti-drip valve,39,7313260161,1,SCAN,,FixPart / 4delonghi,5,#41,modeled" | #2 | bom_rows.csv |
| X-281 | Valve BOM identity, OD-H22 | "OD-H22,OD-H00,OEM,3-way valve,43,AS00004266,1,SCAN,,4delonghi `valve BARM30E`,5,#6,modeled" | #2 | bom_rows.csv |
| X-282 | Flowmeter BOM identity | "OD-H24,OD-H00,OEM,Flowmeter,45,5213225251,1,SCAN,,FixPart / 4delonghi,10–15,#7,modeled" | #2 | bom_rows.csv |
| X-283 | Valve sourcing rule / roles | "Anti-drip valve | 39: 7313260161 | stops dripping after shot" / "Valve (3-way) | 43: AS00004266 | releases puck pressure to drip tray" / "Spring | 42: 6113210761 | OPV spring (sets ~15 bar static)" | #5 | SOURCING_GUIDE.md §3.5 |
| X-284 | Flowmeter sourcing rule | "Flowmeter | 45: 5213225251" / "Datasheet-driven (hall pulse output) — the thesis recommends wiring it to the microcontroller for volumetric dosing." | #5 | SOURCING_GUIDE.md §3.6 |
| X-285 | Flowmeter optionality | "Optional if you run OEM electronics (it's how the PCB doses single/double shots); essential for a smart open controller." | #5 | SOURCING_GUIDE.md §3.6 |
| X-286 | Piping source (OEM tube set) | "The OEM silicone/PTFE tube set with molded bushes is cheap — buy it rather than improvising fittings, and design the chassis around OEM tube lengths." | #5 | SOURCING_GUIDE.md §3.7 |
| X-287 | Scan/CAD workflow validation step | "Validate: print a check-fixture (a ring or cradle) for each critical part and test-fit the real component before trusting the model in the chassis assembly." | #5 | SOURCING_GUIDE.md §5 step 6 |
| X-288 | Milestone 1 definition of done | "M1 definition: donor machine torn down, every part catalogued against the BOM, STEP library validated with printed check-fixtures, printed group-head housing bench-tested under pressure." | #5 | SOURCING_GUIDE.md §8 |
| X-289 | Standing instruction — order of work and delivery mechanics | "Kaldığın yerden devam et. Hedef: open-dedica'nın 3D basılabilir bütün tasarım parçaları ... Onaylanan çıktıları `open-dedica/chassis/` altına koy, montaj STEP'ine ekle, `docs/bom.csv`'yi güncelle, BOM ve panoyu yeniden üret, `claude/…` dalına push'la ve PR aç; sonra sıradaki parçanın işini aç. Usta'ya yalnız karar gereken yerde sor; açık soruları `A-##` satırı olarak ledger'a yaz ve ilerle." (Turkish, quoted verbatim) | #1 | REQUEST.md, "The Usta's words" |
| X-290 | Message that reassigned this session to OD-C07 | "watch old ses'on and initiate parallel fable 5.1 agent sessions where they also design other parts" (quoted verbatim) | #1 | REQUEST.md, message of 2026-09-30 12:00 UTC |
| X-291 | OD-C07 scope narrowing (agent-stated, not the Usta's own words) | "The project coordinator assigned this session the chassis parts OD-C06 … OD-C11 and, after reading `chassis/README.md`, narrowed it to OD-C07 as the only unblocked part of that range; the parallel ask overrides the one-part-at-a-time rule of the standing instruction." | #1 | REQUEST.md, narrative paragraph (not a direct Usta quote) |

## §4 Conflicts and gaps

| # | Rows | Question for the Usta |
|---|---|---|
| 1 | X-233, X-232 (connector hooks) vs X-231/X-230 (plates) | tubes.json / params.json give the connector back-plate and hook geometry only as bare numbers with no cross-reference to WATER_FLOW.md's connector part `OD-H23`. Is the OD-H22 "connector" feature (pins, plates, hooks, F04 in MODELING_PLAN) the same physical part as `OD-H23` (3-way valve connector, WATER_FLOW.md), or a different sub-assembly of OD-H22 itself? No input states this. |
| 2 | — | How was each of OD-H21, OD-H22, OD-H24 fixed to the OEM chassis (screw ears / plug-in spigot with latch lugs / flange with slots, per the brief's own framing)? No input in this workspace describes the OEM mounting bosses, screw bosses, or clip receptacles on the *chassis side* — only the parts' own outer geometry was scanned. |
| 3 | — | What is the orientation of each of OD-H21, OD-H22, OD-H24 inside the assembled machine (which way is "up", which way do the ports/tubes point in the installed machine)? The datum frames recorded here (X-per-part) are scan/measurement frames chosen for cleanest fit, not stated machine-installed orientations. |
| 4 | X-274–X-278 vs OD-H21 | WATER_FLOW.md's flow table lists 9 steps through OD-H24, OD-H01, OD-H22, OD-H11, OD-S01 etc., but never places OD-H21 (anti-drip valve) in the sequence at all (see X-279). Where does the anti-drip valve sit in the water path, and what tube(s) connect to it? |
| 5 | — | What are the tube routes (paths in 3-D space) between OD-H24, OD-H01 (pump, not yet positioned — OD-C03 not designed), and OD-H22? REQUEST.md X-272 states the connecting tubes OD-H25 and OD-W11 are "not scanned yet" and the pump position depends on OD-C03, which is not designed. |
| 6 | — | Where is the floor (top face) of OD-C01 (base frame), i.e. what z-height and orientation will OD-C07 sit at relative to the machine's structural datum? REQUEST.md X-271 states OD-C01 is not designed yet and will follow OD-C07's footprint — so no reference datum exists yet for how OD-C07 attaches to OD-C01 beyond "M3 heat-set inserts" (X-267). |
| 7 | — | What is the function of the OD-H24 flowmeter's 4 tangential outer slots (X-208–X-214) and 4 arc windows (X-202–X-207) — are they OEM chassis engagement features (snap/guide) that the mount must replicate, or purely internal-rotor-cover features with no external mating role? README (#28) says window interiors show "the internal rotor / partition", and slot interiors show "irregular flash / tab remnants" — neither report states an external function. |
| 8 | X-067, X-171, X-249 | All three parts show unresolved tilt/warp findings between the scan-derived axis and datum plane (OD-H22 0.47° not resolvable; OD-H21 nozzle 1.267° vs cap 3.36°; OD-H24 ~1.5° wedge). Each report asks whether this is real assembly/moulding state or specimen damage/measurement noise, and each was modelled "square to the axis" as a declared simplification. Should the mount design treat each part as its modelled (squared) geometry, or account for the observed tilt? |
| 9 | X-004/X-005 (OD-H22 ear tip) | The +X ear tip of the OD-H22 specimen is scan-damaged (jagged outline); the CAD follows the intact −X ear by symmetry, but photo_4 shows what might be a real moulded pip at an ear tip (limitations.json L4, DECISIONS.md CHK-ENUM finding). Is the +X ear tip damage or a real feature the mount should clear? |
| 10 | — | None of the three reports states a caliper reading; every dimension in §2 is scan-only with CHK-SCALE flagged (units assumed mm, absolute scale unverified) per X-273. Before OD-C07's fit-critical interfaces (nozzle spigot, latch lugs, ear-hole pitch, port bores, connector pin pitch, drive-tube slots) are frozen, should any of these be caliper-verified against the physical parts, per SOURCING_GUIDE.md §5 step 6 (X-287)? |

## §5 Unreadable

None. Every file listed in the brief was found in the workspace, opened, and read in full (markdown/JSON/CSV as text, PNG as images); the three STEP files were listed and hashed only, per skill rule 6 (their geometry is measured later by `tools/measure`). Note (not an unreadable file, but a scope gap against the brief's input list): the brief's input list names files only under `reports/OD-H21_antidrip_valve/` and `reports/OD-H22_3way_valve/` for INTAKE_CARD.md, DECISIONS.md, DELIVER_README.md, and MODELING_PLAN.md — no such files exist (or were listed) for `reports/OD-H24_flowmeter/`, so OD-H24's feature enumeration, datum-fit residuals, and human accept-band decision are not available in this workspace; only `README.md`, `params.json`, `tubes.json`, and `export_check.json` exist for OD-H24, plus the two view PNGs, all of which were read/viewed.
