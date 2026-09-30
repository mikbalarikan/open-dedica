# REPORT — od_c07_mount v02 (20260930-od-c07-valve-flowmeter-mount)

Designer: Claude Code, claude-opus-5-5 · spec version 1.2 · plan `01_CAD/DESIGN_PLAN.md` with the WP-03 amendments and the WP-04 findings · brief `briefs/WP-04_designer.md` (J3, build attempt 2 of 2) · 2026-09-30 UTC

**Outcome: SUBMITTED.** The geometry is the v01 export, unchanged (`02_STEP_STL/od_c07_mount_C1_v01.step`, same SHA-256 as the brief). Re-checked against spec 1.2: 228 of 228 scripted rows pass on the re-imported STEP. U-03(b), the v01 stop, now reads 0 mm³ along the spec 1.2 OD-H22 path (slide at +5.0, then a 5.0 drop; v01 at +0.5: 15.1971 mm³); the least clearance along the slide is 0.8583 mm. No fix cycle was used in this package.

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/check_od_c07_mount.py` | c30385f18471874b8c8b19e9c1aa405c2f3af3ddcd5371e351c46233a6ecc75e | checks (D3), updated to spec 1.2 in WP-04: U-03(b) path, one-sided REQ-01/02/04 bands |
| `01_CAD/build_od_c07_mount.py` | 8a45119c6543c50e1d16090ec4e62ebf729e1f06121805fa8efb018ab4424f21 | parametric build and exports; OEM placement by RigidJoint (unchanged since v01) |
| `01_CAD/sections_od_c07_mount.py` | a58ac181c746e0ee947a5921b854d5c2b4789b6cb72a0ba72b56ff6fb117f218 | D6 sections (unchanged; the delivered poses did not change, so no section was regenerated) |
| `01_CAD/sweep_od_c07_mount.py` | 587b497caf0f67635e0212d10c2b2f1226ed2e472fc3d767bed65297d984e00d | D7 sweep driver, spec 1.2 bands (outputs in 01_CAD/sweep_v02/) |
| `01_CAD/report_od_c07_mount_v02.py` | 4ff4b0f840fc0f438e56016e4c2c59762a4228ed7a17286a8b6896d9e398988e | writes this REPORT from the measured JSON |
| `02_STEP_STL/od_c07_mount_C1_v01.step` | 55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c | AP242, the v01 export, unchanged (WP-04: no geometry change); re-imported for every measurement |
| `02_STEP_STL/od_c07_assembly_C1_v01.step` | 50d126c13b945edca3cfd9a5082189ddbd6380bfbb6e59cd24bc71c546f6c9d7 | check assembly: od_c07_mount + OD-H22 + OD-H24 as placed (AP242), unchanged |
| `02_STEP_STL/od_c07_mount_C1_v01.stl` | 41bccd61c1fb0e82a7a8171c85da2128d0c01ca6906f80c03c5ffebf83de3c38 | unchanged; meshed from the re-imported STEP after clearing the cached triangulation; tolerance 0.01 mm / angular 0.05 rad, 92262 triangles |
| `03_Sections/od_c07_mount_v01_front_y0.png` | 07e3dfaa6dcf1b66c63899d01e3e4f22878b5607994d31a2c61d4437616f20d4 | section y = 0.00 mm, cut 935.7 mm², nothing_clipped 0 px (v01, delivered pose unchanged) |
| `03_Sections/od_c07_mount_v01_top_z10p25.png` | 12227a9402aac63b16f00cf593480dc9c4e76d17f5e9ef5ddef015f1fb6901cd | section z = 10.25 mm, cut 465.0 mm², nothing_clipped 0 px (v01, delivered pose unchanged) |
| `03_Sections/od_c07_mount_v01_top_z47.png` | 58e1855969367303edd2ba843912635c0572643e92e9308d2740bc6d571c09cc | section z = 47.00 mm, cut 1234.2 mm², nothing_clipped 0 px (v01, delivered pose unchanged) |
| `03_Sections/od_c07_mount_v01_left_x62.png` | b22fd218abd547d0ba49e597cf9e241d62e97b3a596b721367456e593aac7586 | section x = 62.00 mm, cut 61.2 mm², nothing_clipped 0 px (v01, delivered pose unchanged) |
| `03_Sections/od_c07_mount_v01_left_x7p48.png` | fe7e47b4f7fbb36c9674d2bd284c5ecebc51b4768d126f86413e527c99fe0538 | section x = 7.48 mm, cut 465.2 mm², nothing_clipped 0 px (v01, delivered pose unchanged) |
| `03_Sections/od_c07_mount_v01_left_xm11p78.png` | 26f17982ec3da2d0029652a472feeb629874bed6157806c6d542f558eeadd891 | section x = -11.78 mm, cut 334.1 mm², nothing_clipped 0 px (v01, delivered pose unchanged) |
| `03_Sections/od_c07_assembly_v01_front_y0.png` | c82c911de5ea50f00c486ac232a3be73757d6b618e02b364fed83a3ebfa0bb0a | section y = 0.00 mm, cut 2077.9 mm², nothing_clipped 0 px (v01, delivered pose unchanged) |
| `03_Sections/od_c07_assembly_v01_left_x62.png` | 627480207b47ba5bec15e2fc71f72661d680b644b339740bcd878d75cb8677ec | section x = 62.00 mm, cut 575.7 mm², nothing_clipped 0 px (v01, delivered pose unchanged) |
| `01_CAD/check_out_v02/check_v02.json` | cd3a567f088cd7b1fa7c1dd18f71a9f770edfa7d1b39545de07b7d4482d22d0a | every spec 1.2 gate row with measured value, margin and location; the OD-H22 path poses |
| `01_CAD/check_out_v02_log.txt` | cb1f3eee759f228bccd73652c2900ed2c264aa2ff52bfacfed5251caa38f8067 | console log of the v02 check |
| `01_CAD/sweep_v02_log.txt` | a452afe2c2e9457eb68322a64918828f96eb883bc75c7799c5f1f5fc423430f2 | console log of the v02 sweep driver |
| `01_CAD/check_out_v01/build_facts_v01.json` | e9da6f4a97f21078f7aa7e74c004979579322729965814c98138e990ce1f415a | fillet ladders, round trip, STL facts (v01 build, unchanged) |
| `01_CAD/check_out_v01/sections_v01.json` | 1564c0b52f41c50a1b0529632a4c99ac7921340c1cf20bbdf26c7be6eda50adb | sections log with nothing_clipped (v01, unchanged) |
| `01_CAD/REPORT_od_c07_mount_v01.md` | 717ac5c21c442873bfa552e3e062c4ebb881b37a5bc543cc2d5b82d62ea427bc | the record of the v01 stop (spec 1.1), kept |
| `01_CAD/report_od_c07_mount.py` | 3d7fb982a1620b6e103aa294f3451a96194ec4af5fd56224f90411bcdd851f79 | the v01 REPORT writer, kept |
| `01_CAD/check_out_v01/check_v01.json` | b9458e5ed41524be54007e3d267b79f7c99b65a9e66fc5ab4d66ea1dc04509d4 | the v01 check (spec 1.1), kept |
| `01_CAD/build_probes_v01/probe_b1_v01.py` | 7232e5133329411a71d49a88766b5018210960d98591dc704696a6c42eb07808 | diagnostic probe of v01 (not a gate check) |
| `01_CAD/build_probes_v01/probe_b2_v01.py` | fb3ae6383a436b2075ad1766a5765812001df40dc0e84639bb97f5e5b7694348 | diagnostic probe of v01 (not a gate check) |
| `01_CAD/build_probes_v01/probe_b3_v01.py` | 667ffce64a6d63c0571194aff9389012040dd825972577ac018ff6d7ec10e556 | diagnostic probe of v01 (not a gate check) |
| `01_CAD/build_probes_v01/probe_b4_v01.py` | 00fbebf7bd5d7bafad5cb06fd6579d64e23a3ca090b7863edf5a7cfb92317743 | diagnostic probe of v01 (not a gate check) |
| `01_CAD/build_probes_v01/probe_b5_v01.py` | 57cbdd4552def2f84af87cee27f4fd5868d655c39a05fd6aaebf992005c16d3c | diagnostic probe of v01 (not a gate check) |
| `01_CAD/build_probes_v01/probe_b6_v01.py` | a44722f9f1f62fba816f37178798a58291aee108e9f85952187121c2e4597c1a | diagnostic probe of v01 (not a gate check) |
| `01_CAD/build_probes_v01/probe_b7_v01.py` | 054ec4aabd5a2ad5404c87769801ad65cd20609e5f25ff2b89f8d19c20707689 | diagnostic probe of v01 (not a gate check) |

Sweep outputs (STEP, STL, check.json per run) are in `01_CAD/sweep_v02/<parameter>_<low|high>/`; they are not deliverables. The v01 sweep (spec 1.1 bands) stays in `01_CAD/sweep_v01/`.

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1 (OCCT 7.9.3) · repo commit 70826895ab7666f9e5aee3f77ce88f099995f3c1

Input hashes checked at D0, all equal to the brief: OD-H22 bc0ffd00…0028, OD-H24 1b4cbdaf…696a, `02_STEP_STL/od_c07_mount_C1_v01.step` 55c1c361…583c.

## 3. Gate self-check

Bands (GATES §0): mm 0.005, degrees 0.001, mm³ 0.001, counts / bool / % / mm² / ratio 0. Every value below is measured on the re-imported `02_STEP_STL/od_c07_mount_C1_v01.step` with OD-H24 and OD-H22 placed by their joints, by the spec 1.2 check script. A self-check clears no hard gate.

| Gate | Measured | Unit | Required | Margin | At | Status |
|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | count | == 1 | 0 | — | PASS |
| U-01 | 1 | count | solid_count = 1 | 0 | — | PASS |
| U-01 | 1 | bool | brep_valid = 1 | 0 | — | PASS |
| U-01 | 0 | count | naked_edges = 0 | 0 | — | PASS |
| U-02 | 119 | mm | size_x 119.0 ± 0.1 | 0.1 | — | PASS |
| envelope_within_spec | 119 | mm | size_x 119.0 ± 0.1 | 0.1 | — | PASS |
| U-02 | 50 | mm | size_y 50.0 ± 0.1 | 0.1 | — | PASS |
| envelope_within_spec | 50 | mm | size_y 50.0 ± 0.1 | 0.1 | — | PASS |
| U-02 | 48 | mm | size_z 48.0 ± 0.1 | 0.1 | — | PASS |
| envelope_within_spec | 48 | mm | size_z 48.0 ± 0.1 | 0.1 | — | PASS |
| U-02 | -25 | mm | position min_x -25.0 ± 0.1 (reported apart) | 0.1 | — | PASS |
| envelope_within_spec | -25 | mm | position min_x -25.0 ± 0.1 (reported apart) | 0.1 | — | PASS |
| U-02 | -25 | mm | position min_y -25.0 ± 0.1 (reported apart) | 0.1 | — | PASS |
| envelope_within_spec | -25 | mm | position min_y -25.0 ± 0.1 (reported apart) | 0.1 | — | PASS |
| U-02 | 0 | mm | position min_z 0.0 ± 0.1 (reported apart) | 0.1 | — | PASS |
| envelope_within_spec | 0 | mm | position min_z 0.0 ± 0.1 (reported apart) | 0.1 | — | PASS |
| D-02 | 119 | mm | size_x <= 220.0 | 101 | — | PASS (assumed: A-12) |
| D-02 | 50 | mm | size_y <= 220.0 | 170 | — | PASS (assumed: A-12) |
| D-02 | 48 | mm | size_z <= 250.0 | 202 | — | PASS (assumed: A-12) |
| U-03 | 0 | mm3 | interference mount|OD-H24 <= 0 | 0 | — | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0 | mm3 | interference mount|OD-H22 <= 0 | 0 | — | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0 | mm | contact: OD-H24 rim face on the pedestal top, clearance = 0 | 0 | (14.3000, 0.0000, 10.0000) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0 | mm | contact: OD-H22 flange back face on the deck top, clearance = 0 | 0 | (69.0500, 1.2000, 48.0000) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0 | mm | contact: hook 70° catch underside on the OD-H24 flange top, clearance = 0 | 0 | (8.8253, 16.6791, 29.9000) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0 | mm | contact: hook 160° catch underside on the OD-H24 flange top, clearance = 0 | 0 | (-16.6791, 8.8253, 29.9000) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0 | mm | contact: hook 320° catch underside on the OD-H24 flange top, clearance = 0 | 0 | (15.9825, -10.0319, 29.9000) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0.5 | mm | mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 | -0 | (2.5850, 0.0930, 9.4000) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| D-04c | 0.5 | mm | mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 | -0 | (2.5850, 0.0930, 9.4000) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0.503 | mm | mount to OD-H22 below its flange back face >= 0.5 | 0.003 | (55.0529, -1.2000, 43.7660) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| D-04c | 0.503 | mm | mount to OD-H22 below its flange back face >= 0.5 | 0.003 | (55.0529, -1.2000, 43.7660) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| D-04c | 13.3462 | mm | hooks to OD-H24 pipes and connector (outside r 20.5) >= 0.5 | 12.8462 | (12.6548, -13.9976, 29.9000) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| D-04c | 4.9391 | mm | hooks to OD-H24 above its flange top plane (z > 29.901) >= 0.5 | 4.4391 | (15.9825, -10.0319, 31.5000) mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0 | mm3 | (b) OD-H24 lowered along -Z from 25 mm, 9 poses, interference <= 0 (hooks exempt) | 0 | OD-H24 raised 25.0 mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0 | mm3 | (b) OD-H22 slid along -Y at +5 (flange back face z 53) from y +45 to 0 (12 poses), then lowered 5 along -Z (7 poses incl. the slide end); interference with the mount <= 0 | 0 | OD-H22 at y +45.0 mm, z +5.0 mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-03 | 0 | mm3 | (b) OD-H22 along the same 18 poses: interference with the seated OD-H24 <= 0 | 0 | OD-H22 at y +45.0 mm, z +5.0 mm | PASS (assumed: A-02, A-03, A-06, A-07) |
| U-04 | 1 | bool | schema AP242 | 0 | — | PASS |
| U-04 | 1 | count | 1 solid re-read | 0 | — | PASS |
| U-04 | 0 | mm3 | volume delta 0 | -0 | — | PASS |
| U-04 | 0 | count | faces delta 0 | 0 | — | PASS |
| U-04 | 1 | bool | named body re-read unchanged | 0 | — | PASS |
| U-04 | 1 | bool | valid after re-import | 0 | — | PASS |
| REQ-06 | 3.4 | mm | footprint hole (-18, 21) Ø3.4 ± 0.1 | 0.1 | (-18.0000, 21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 0 | mm | footprint hole (-18, 21) offset <= 0.10 | 0.1 | (-18.0000, 21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 4 | mm | footprint hole (-18, 21) length 4.0 ± 0.1 | 0.1 | (-18.0000, 21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 1 | bool | footprint hole (-18, 21) through | 0 | (-18.0000, 21.0000, 0.0000) mm | PASS (assumed: A-14) |
| D-04a | 3.4 | mm | footprint hole (-18, 21) Ø >= 3.25 | 0.15 | (-18.0000, 21.0000, 0.0000) mm | PASS |
| REQ-06 | 3.4 | mm | footprint hole (-18, -21) Ø3.4 ± 0.1 | 0.1 | (-18.0000, -21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 0 | mm | footprint hole (-18, -21) offset <= 0.10 | 0.1 | (-18.0000, -21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 4 | mm | footprint hole (-18, -21) length 4.0 ± 0.1 | 0.1 | (-18.0000, -21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 1 | bool | footprint hole (-18, -21) through | 0 | (-18.0000, -21.0000, 0.0000) mm | PASS (assumed: A-14) |
| D-04a | 3.4 | mm | footprint hole (-18, -21) Ø >= 3.25 | 0.15 | (-18.0000, -21.0000, 0.0000) mm | PASS |
| REQ-06 | 3.4 | mm | footprint hole (88.5, 21) Ø3.4 ± 0.1 | 0.1 | (88.5000, 21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 0 | mm | footprint hole (88.5, 21) offset <= 0.10 | 0.1 | (88.5000, 21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 4 | mm | footprint hole (88.5, 21) length 4.0 ± 0.1 | 0.1 | (88.5000, 21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 1 | bool | footprint hole (88.5, 21) through | 0 | (88.5000, 21.0000, 0.0000) mm | PASS (assumed: A-14) |
| D-04a | 3.4 | mm | footprint hole (88.5, 21) Ø >= 3.25 | 0.15 | (88.5000, 21.0000, 0.0000) mm | PASS |
| REQ-06 | 3.4 | mm | footprint hole (88.5, -21) Ø3.4 ± 0.1 | 0.1 | (88.5000, -21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 0 | mm | footprint hole (88.5, -21) offset <= 0.10 | 0.1 | (88.5000, -21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 4 | mm | footprint hole (88.5, -21) length 4.0 ± 0.1 | 0.1 | (88.5000, -21.0000, 0.0000) mm | PASS (assumed: A-14) |
| REQ-06 | 1 | bool | footprint hole (88.5, -21) through | 0 | (88.5000, -21.0000, 0.0000) mm | PASS (assumed: A-14) |
| D-04a | 3.4 | mm | footprint hole (88.5, -21) Ø >= 3.25 | 0.15 | (88.5000, -21.0000, 0.0000) mm | PASS |
| REQ-05 | 3.4 | mm | screw clearance (77.447, 0) Ø3.4 ± 0.1 | 0.1 | (77.4470, 0.0000, 46.0000) mm | PASS (assumed: A-02, A-13, A-18) |
| REQ-05 | 0 | mm | screw clearance (77.447, 0) offset <= 0.10 | 0.1 | (77.4470, 0.0000, 46.0000) mm | PASS (assumed: A-02, A-13, A-18) |
| REQ-05 | 2 | mm | screw clearance (77.447, 0) depth 2.0 ± 0.1 | 0.1 | (77.4470, 0.0000, 46.0000) mm | PASS (assumed: A-02, A-13, A-18) |
| D-04a | 3.4 | mm | screw clearance (77.447, 0) Ø >= 3.25 | 0.15 | (77.4470, 0.0000, 46.0000) mm | PASS |
| REQ-05 | 4 | mm | insert bore (77.447, 0) Ø4.0 ± 0.05 | 0.05 | (77.4470, 0.0000, 40.3000) mm | PASS (assumed: A-02, A-13, A-18) |
| REQ-05 | 0 | mm | insert bore (77.447, 0) coaxial offset <= 0.10 | 0.1 | (77.4470, 0.0000, 40.3000) mm | PASS (assumed: A-02, A-13, A-18) |
| REQ-05 | 5.7 | mm | insert bore (77.447, 0) depth 5.7 ± 0.1 | 0.1 | (77.4470, 0.0000, 40.3000) mm | PASS (assumed: A-02, A-13, A-18) |
| D-05b | 4 | mm | insert bore (77.447, 0) Ø 4.0 ± 0.05 | 0.05 | (77.4470, 0.0000, 40.3000) mm | PASS (assumed: A-13) |
| D-05b | 5.7 | mm | insert bore (77.447, 0) depth >= 5.7 | 0 | (77.4470, 0.0000, 40.3000) mm | PASS (assumed: A-13) |
| D-05b | 1 | bool | insert bore (77.447, 0) opens on the deck underside | 0 | — | PASS (assumed: A-13) |
| REQ-05 | 3.4 | mm | screw clearance (46.662, 0) Ø3.4 ± 0.1 | 0.1 | (46.6620, 0.0000, 46.0000) mm | PASS (assumed: A-02, A-13, A-18) |
| REQ-05 | 0 | mm | screw clearance (46.662, 0) offset <= 0.10 | 0.1 | (46.6620, 0.0000, 46.0000) mm | PASS (assumed: A-02, A-13, A-18) |
| REQ-05 | 2 | mm | screw clearance (46.662, 0) depth 2.0 ± 0.1 | 0.1 | (46.6620, 0.0000, 46.0000) mm | PASS (assumed: A-02, A-13, A-18) |
| D-04a | 3.4 | mm | screw clearance (46.662, 0) Ø >= 3.25 | 0.15 | (46.6620, 0.0000, 46.0000) mm | PASS |
| REQ-05 | 4 | mm | insert bore (46.662, 0) Ø4.0 ± 0.05 | 0.05 | (46.6620, 0.0000, 40.3000) mm | PASS (assumed: A-02, A-13, A-18) |
| REQ-05 | 0 | mm | insert bore (46.662, 0) coaxial offset <= 0.10 | 0.1 | (46.6620, 0.0000, 40.3000) mm | PASS (assumed: A-02, A-13, A-18) |
| REQ-05 | 5.7 | mm | insert bore (46.662, 0) depth 5.7 ± 0.1 | 0.1 | (46.6620, 0.0000, 40.3000) mm | PASS (assumed: A-02, A-13, A-18) |
| D-05b | 4 | mm | insert bore (46.662, 0) Ø 4.0 ± 0.05 | 0.05 | (46.6620, 0.0000, 40.3000) mm | PASS (assumed: A-13) |
| D-05b | 5.7 | mm | insert bore (46.662, 0) depth >= 5.7 | 0 | (46.6620, 0.0000, 40.3000) mm | PASS (assumed: A-13) |
| D-05b | 1 | bool | insert bore (46.662, 0) opens on the deck underside | 0 | — | PASS (assumed: A-13) |
| REQ-02 | 4.8 | mm | pin 1 Ø4.8 +0.1/-0 (one-sided, spec 1.2) | 0 | (0.1850, 0.0930, 0.0000) mm | PASS (assumed: A-07) |
| REQ-02 | 0 | mm | pin 1 Ø4.8 offset <= 0.10 | 0.1 | (0.1850, 0.0930, 0.0000) mm | PASS (assumed: A-07) |
| REQ-02 | 9.4 | mm | pin 1 Ø4.8 length 9.4 ± 0.1 (recess floor to bottom face) | 0.1 | (0.1850, 0.0930, 0.0000) mm | PASS (assumed: A-07) |
| REQ-02 | 1 | bool | pin 1 Ø4.8 through | 0 | (0.1850, 0.0930, 0.0000) mm | PASS (assumed: A-07) |
| REQ-02 | 0.5 | mm | pin 1 Ø4.8: clearance to the OD-H24 pin >= 0.5 | -0 | (2.5850, 0.0930, 9.4000) mm | PASS (assumed: A-07) |
| D-04d | 0.5 | mm | pin 1 Ø4.8: printed sliding fit >= 0.30 per side | 0.2 | (2.5850, 0.0930, 9.4000) mm | PASS (assumed: A-06, A-07) |
| REQ-02 | 3.8 | mm | pin 2 Ø3.8 +0.1/-0 (one-sided, spec 1.2) | 0 | (-11.7800, 0.1400, 0.0000) mm | PASS (assumed: A-07) |
| REQ-02 | 0 | mm | pin 2 Ø3.8 offset <= 0.10 | 0.1 | (-11.7800, 0.1400, 0.0000) mm | PASS (assumed: A-07) |
| REQ-02 | 9.4 | mm | pin 2 Ø3.8 length 9.4 ± 0.1 (recess floor to bottom face) | 0.1 | (-11.7800, 0.1400, 0.0000) mm | PASS (assumed: A-07) |
| REQ-02 | 1 | bool | pin 2 Ø3.8 through | 0 | (-11.7800, 0.1400, 0.0000) mm | PASS (assumed: A-07) |
| REQ-02 | 0.5 | mm | pin 2 Ø3.8: clearance to the OD-H24 pin >= 0.5 | -0 | (-9.8800, 0.1400, 9.4000) mm | PASS (assumed: A-07) |
| D-04d | 0.5 | mm | pin 2 Ø3.8: printed sliding fit >= 0.30 per side | 0.2 | (-9.8800, 0.1400, 9.4000) mm | PASS (assumed: A-06, A-07) |
| REQ-02 | 14.1 | mm | recess R 14.10 ± 0.1 (radial_profile inner, z 9.5 ... 9.9) min | 0.1 | (13.8858, 2.4484, 9.5500) mm | PASS (assumed: A-07) |
| REQ-02 | 14.15 | mm | recess R 14.10 ± 0.1 (radial_profile inner, z 9.5 ... 9.9) max | 0.05 | (14.1500, 0.0000, 9.8500) mm | PASS (assumed: A-07) |
| REQ-02 | 9.4 | mm | recess floor z 9.40 ± 0.05 | 0.05 | — | PASS (assumed: A-07) |
| REQ-02 | 0.5161 | mm | recess to the OD-H24 underside ribs and hub (H24 inside r 13.68) >= 0.5 | 0.0161 | (14.1000, 0.0000, 9.8000) mm | PASS (assumed: A-07) |
| REQ-01 | 10 | mm | pedestal top z 10.0 ± 0.1 | 0.1 | — | PASS (assumed: A-06) |
| REQ-01 | 16.3 | mm | ring inner R (radial_profile inner 0...359°, z 10.5...12.5) min in [16.30, 16.40] (spec 1.2) | -0 | (16.2603, 1.1370, 10.5500) mm | PASS (assumed: A-06) |
| REQ-01 | 16.3 | mm | ring inner R max in [16.30, 16.40] (spec 1.2) | 0 | (16.3000, 0.0000, 10.5500) mm | PASS (assumed: A-06) |
| REQ-01 | 13 | mm | ring top z 13.0 ± 0.1 | 0.1 | — | PASS (assumed: A-06) |
| REQ-01 | 0.5314 | mm | clearance(ring, OD-H24 cup) in [0.50, 0.70] | 0.0314 | (16.3000, -0.0000, 13.0000) mm | PASS (assumed: A-06) |
| D-04d | 0.5314 | mm | ring gap >= 0.30 per side | 0.2314 | (16.3000, -0.0000, 13.0000) mm | PASS (assumed: A-06, A-07) |
| REQ-03 | 70 | deg | hook 70° centred at 70° ± 1° | 1 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 20.87 | mm | hook 70° beam inner face R 20.87 ± 0.1 over z 6...26 (min) | 0.1 | (9.4372, 18.6144, 6.2500) mm | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 20.87 | mm | hook 70° beam inner face R 20.87 ± 0.1 over z 6...26 (max) | 0.1 | (9.4372, 18.6144, 6.2500) mm | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 29.9 | mm | hook 70° catch underside z 29.9 ± 0.1 | 0.1 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 18.87 | mm | hook 70° catch reaches R 18.87 ± 0.1 | 0.1 | (6.4539, 17.7320, 30.4000) mm | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 45 | deg | hook 70° catch top chamfer 45° ± 1° (from horizontal) | 1 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 0 | mm3 | hook 70° catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0 | 0 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 0 | mm | hook 70° catch underside on the flange top, clearance = 0 | 0 | (8.8253, 16.6791, 29.9000) mm | PASS (assumed: A-06, A-08, A-09) |
| J-04 | 0 | mm3 | hook 70° undeflected at the engaged pose: interference <= 0 | 0 | — | PASS (assumed: A-06, A-08) |
| J-04 | 0 | mm | hook 70° catch underside touches the flange top, clearance = 0 | 0 | (8.8253, 16.6791, 29.9000) mm | PASS (assumed: A-06, A-08) |
| J-02 | 2 | mm | hook 70° beam thickness >= 1.0 | 1 | (9.7607, 18.4469, 26.0000) mm | PASS |
| J-01 | 0.6708 | % | hook 70° ε = 1.5·y·t/(L²·Q) <= 1.5 % (y = 20.37 − catch R, L = plate top to catch underside) | 0.8292 | — | PASS (assumed: A-15) |
| J-03 | 2 | ratio | hook 70° catch/root thickness ratio reported; binding only if ε within 0.2 % of 1.5 % | 1.5 | — | PASS |
| REQ-03 | 160 | deg | hook 160° centred at 160° ± 1° | 1 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 20.87 | mm | hook 160° beam inner face R 20.87 ± 0.1 over z 6...26 (min) | 0.1 | (-18.6144, 9.4372, 6.2500) mm | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 20.87 | mm | hook 160° beam inner face R 20.87 ± 0.1 over z 6...26 (max) | 0.1 | (-18.6144, 9.4372, 6.2500) mm | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 29.9 | mm | hook 160° catch underside z 29.9 ± 0.1 | 0.1 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 18.87 | mm | hook 160° catch reaches R 18.87 ± 0.1 | 0.1 | (-17.7320, 6.4539, 30.4000) mm | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 45 | deg | hook 160° catch top chamfer 45° ± 1° (from horizontal) | 1 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 0 | mm3 | hook 160° catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0 | 0 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 0 | mm | hook 160° catch underside on the flange top, clearance = 0 | 0 | (-16.6791, 8.8253, 29.9000) mm | PASS (assumed: A-06, A-08, A-09) |
| J-04 | 0 | mm3 | hook 160° undeflected at the engaged pose: interference <= 0 | 0 | — | PASS (assumed: A-06, A-08) |
| J-04 | 0 | mm | hook 160° catch underside touches the flange top, clearance = 0 | 0 | (-16.6791, 8.8253, 29.9000) mm | PASS (assumed: A-06, A-08) |
| J-02 | 2 | mm | hook 160° beam thickness >= 1.0 | 1 | (-18.4469, 9.7607, 26.0000) mm | PASS |
| J-01 | 0.6708 | % | hook 160° ε = 1.5·y·t/(L²·Q) <= 1.5 % (y = 20.37 − catch R, L = plate top to catch underside) | 0.8292 | — | PASS (assumed: A-15) |
| J-03 | 2 | ratio | hook 160° catch/root thickness ratio reported; binding only if ε within 0.2 % of 1.5 % | 1.5 | — | PASS |
| REQ-03 | 320 | deg | hook 320° centred at 320° ± 1° | 1 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 20.87 | mm | hook 320° beam inner face R 20.87 ± 0.1 over z 6...26 (min) | 0.1 | (14.2641, -15.2346, 6.2500) mm | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 20.87 | mm | hook 320° beam inner face R 20.87 ± 0.1 over z 6...26 (max) | 0.1 | (14.2641, -15.2346, 6.2500) mm | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 29.9 | mm | hook 320° catch underside z 29.9 ± 0.1 | 0.1 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 18.87 | mm | hook 320° catch reaches R 18.87 ± 0.1 | 0.1 | (14.4553, -12.1294, 30.4000) mm | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 45 | deg | hook 320° catch top chamfer 45° ± 1° (from horizontal) | 1 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 0 | mm3 | hook 320° catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0 | 0 | — | PASS (assumed: A-06, A-08, A-09) |
| REQ-03 | 0 | mm | hook 320° catch underside on the flange top, clearance = 0 | 0 | (15.9825, -10.0319, 29.9000) mm | PASS (assumed: A-06, A-08, A-09) |
| J-04 | 0 | mm3 | hook 320° undeflected at the engaged pose: interference <= 0 | 0 | — | PASS (assumed: A-06, A-08) |
| J-04 | 0 | mm | hook 320° catch underside touches the flange top, clearance = 0 | 0 | (15.9825, -10.0319, 29.9000) mm | PASS (assumed: A-06, A-08) |
| J-02 | 2 | mm | hook 320° beam thickness >= 1.0 | 1 | (13.9960, -15.4812, 26.0000) mm | PASS |
| J-01 | 0.6708 | % | hook 320° ε = 1.5·y·t/(L²·Q) <= 1.5 % (y = 20.37 − catch R, L = plate top to catch underside) | 0.8292 | — | PASS (assumed: A-15) |
| J-03 | 2 | ratio | hook 320° catch/root thickness ratio reported; binding only if ε within 0.2 % of 1.5 % | 1.5 | — | PASS |
| REQ-04 | 48 | mm | deck top z 48.0 ± 0.1 | 0.1 | — | PASS (assumed: A-03) |
| REQ-04 | 0 | mm2 | deck top flat under the OD-H22 flange outline: flange area not on the z 48 plane beyond the slot and slits (mm²) <= 0 | 0 | — | PASS (assumed: A-03) |
| REQ-04 | 7.05 | mm | stem U-slot radial_profile inner about (62, 0), 192°...348° (slit angles aside), z 41...47, min in [7.05, 7.10] (spec 1.2) | -0 | (55.1594, -1.7055, 41.2500) mm | PASS (assumed: A-03) |
| REQ-04 | 7.05 | mm | stem U-slot radial_profile inner, max in [7.05, 7.10] (spec 1.2) | -0 | (55.1041, -1.4658, 41.2500) mm | PASS (assumed: A-03) |
| REQ-04 | 7.05 | mm | slot straight wall +X at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (least) | -0 | (69.0500, 2.5000, 41.0000) mm | PASS (assumed: A-03) |
| REQ-04 | 7.05 | mm | slot straight wall +X at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (greatest) | -0 | (69.0500, 2.5000, 41.0000) mm | PASS (assumed: A-03) |
| REQ-04 | 7.05 | mm | slot straight wall -X at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (least) | -0 | (54.9500, 2.5000, 41.0000) mm | PASS (assumed: A-03) |
| REQ-04 | 7.05 | mm | slot straight wall -X at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (greatest) | -0 | (54.9500, 2.5000, 41.0000) mm | PASS (assumed: A-03) |
| REQ-04 | 14.1 | mm | stem U-slot 14.1 +0.1/-0 wide (least) | -0 | — | PASS (assumed: A-03) |
| REQ-04 | 0 | mm3 | slot open through the deck's +Y edge: material in the channel x 62 ± 6.9, y 0 ... 16 <= 0 | 0 | — | PASS (assumed: A-03) |
| REQ-04 | 7.7 | mm | slot through the deck, length 7.7 ± 0.1 | 0.1 | — | PASS (assumed: A-03) |
| REQ-04 | 0 | count | no closed stem bore | 0 | — | PASS (assumed: A-03) |
| REQ-04 | 11.85 | mm | gusset slit +X reaches 62 ± (11.85 +0.1/-0) at the deck top | 0 | — | PASS (assumed: A-03) |
| REQ-04 | 2.4 | mm | gusset slit +X 2.40 ± 0.1 wide (worst) | 0.1 | — | PASS (assumed: A-03) |
| REQ-04 | 11.85 | mm | gusset slit -X reaches 62 ± (11.85 +0.1/-0) at the deck top | 0 | — | PASS (assumed: A-03) |
| REQ-04 | 2.4 | mm | gusset slit -X 2.40 ± 0.1 wide (worst) | 0.1 | — | PASS (assumed: A-03) |
| REQ-04 | 0.503 | mm | clearance(mount, OD-H22) away from the flange contact >= 0.5; nearest points in 'at' | 0.003 | (55.0529, -1.2000, 43.7660) mm | PASS (assumed: A-03) |
| REQ-07 | 2 | count | the window splits the plate in two (window through over the full Y width) | 0 | — | PASS (assumed: A-04, A-19) |
| REQ-07 | 40 | mm | plate piece -X ends at x 40.0 (window from 40) | 0.1 | — | PASS (assumed: A-04, A-19) |
| REQ-07 | 84 | mm | plate piece +X starts at x 84.0 (window to 84) | 0.1 | — | PASS (assumed: A-04, A-19) |
| REQ-07 | 40 | mm | leg inner face at x 40.0 ± 0.1 | 0.1 | — | PASS (assumed: A-04, A-19) |
| REQ-07 | 84 | mm | leg inner face at x 84.0 ± 0.1 | 0.1 | — | PASS (assumed: A-04, A-19) |
| REQ-08 | 48 | mm | no material above z 48.1 | 0.1 | — | PASS (assumed: A-10) |
| REQ-08 | 0 | mm3 | no material within r 12 of the valve axis above the deck top | 0 | — | PASS (assumed: A-10) |
| REQ-09 | 25 | deg | drain notch 25° at θ 25° ± 1° | 1 | — | PASS |
| REQ-09 | 2 | mm | drain notch 25° 2.0 ± 0.1 wide | 0.1 | — | PASS |
| REQ-09 | 0.5 | mm | drain notch 25° 0.5 ± 0.1 high at the ring base | 0.1 | — | PASS |
| D-03b | 2 | mm | drain notch 25° ceiling bridge span <= 5 | 3 | — | PASS (assumed: A-16) |
| REQ-09 | 1 | bool | drain notch 25° open through the ring wall (no material r 15...18.2 at mid height) | 0 | — | PASS |
| REQ-09 | 115 | deg | drain notch 115° at θ 115° ± 1° | 1 | — | PASS |
| REQ-09 | 2 | mm | drain notch 115° 2.0 ± 0.1 wide | 0.1 | — | PASS |
| REQ-09 | 0.5 | mm | drain notch 115° 0.5 ± 0.1 high at the ring base | 0.1 | — | PASS |
| D-03b | 2 | mm | drain notch 115° ceiling bridge span <= 5 | 3 | — | PASS (assumed: A-16) |
| REQ-09 | 1 | bool | drain notch 115° open through the ring wall (no material r 15...18.2 at mid height) | 0 | — | PASS |
| REQ-09 | 225 | deg | drain notch 225° at θ 225° ± 1° | 1 | — | PASS |
| REQ-09 | 2 | mm | drain notch 225° 2.0 ± 0.1 wide | 0.1 | — | PASS |
| REQ-09 | 0.5 | mm | drain notch 225° 0.5 ± 0.1 high at the ring base | 0.1 | — | PASS |
| D-03b | 2 | mm | drain notch 225° ceiling bridge span <= 5 | 3 | — | PASS (assumed: A-16) |
| REQ-09 | 1 | bool | drain notch 225° open through the ring wall (no material r 15...18.2 at mid height) | 0 | — | PASS |
| D-01a | 1.7224 | mm | min_wall >= 0.8 | 0.9224 | (-16.1007, 2.5198, 10.2555) mm | PASS |
| D-01b | 1.7224 | mm | min_wall >= 1.5 | 0.2224 | (-16.1007, 2.5198, 10.2555) mm | PASS |
| D-06a | 1.7224 | mm | minimum feature >= 1.0 | 0.7224 | (-16.1007, 2.5198, 10.2555) mm | PASS |
| U-06 | 1.6 | mm | Soft: min_wall wide (45°) >= 1.5 | 0.1 | (-16.6791, 8.8253, 31.5000) mm | PASS |
| D-03a | 60.0184 | deg | least overhang >= 45° off the named faces (deck underside, 3 catch undersides supported; 2 insert-bore and 3 notch ceilings bridges) | 15.0184 | (-11.8654, -13.5994, 10.0833) mm | PASS (assumed: A-16) |
| D-03a | 0 | count | no flat downward face other than the named ones | 0 | — | PASS (assumed: A-16) |
| D-03b | 4 | mm | insert bore ceiling (77.447, 0): bridge span (bore Ø) <= 5 | 1 | (77.4470, 0.0000, 40.3000) mm | PASS (assumed: A-16) |
| D-03b | 4 | mm | insert bore ceiling (46.662, 0): bridge span (bore Ø) <= 5 | 1 | (46.6620, 0.0000, 40.3000) mm | PASS (assumed: A-16) |
| D-05a | 16.4748 | mm | insert pad (77.447, 0): material across the bore >= 8.0 (least of 8 diameters × 3 depths) | 8.4748 | angle 0.0°, z 45.80 | PASS (assumed: A-13) |
| J-05 | 3.9218 | mm | insert bore (77.447, 0): wall >= 3.0 over its depth (16 angles × 3 depths) | 0.9218 | angle 180.0°, z 45.80 | PASS |
| D-05a | 16.4748 | mm | insert pad (46.662, 0): material across the bore >= 8.0 (least of 8 diameters × 3 depths) | 8.4748 | angle 0.0°, z 45.80 | PASS (assumed: A-13) |
| J-05 | 3.8128 | mm | insert bore (46.662, 0): wall >= 3.0 over its depth (16 angles × 3 depths) | 0.8128 | angle 0.0°, z 45.80 | PASS |
| feature_census | 12 | count | bores = 12 (4 footprint, 2 pin, 2 screw clearance, 2 insert, recess, ring inner) | 0 | — | PASS |
| U-05 | 1 | count | plate window = 1 | 0 | — | PASS |
| feature_census | 1 | count | plate window = 1 | 0 | — | PASS |
| U-05 | 4 | count | Ø3.4 footprint through-holes = 4 | 0 | — | PASS |
| feature_census | 4 | count | Ø3.4 footprint through-holes = 4 | 0 | — | PASS |
| U-05 | 1 | count | pedestal = 1 | 0 | — | PASS |
| feature_census | 1 | count | pedestal = 1 | 0 | — | PASS |
| U-05 | 1 | count | pedestal recess = 1 | 0 | — | PASS |
| feature_census | 1 | count | pedestal recess = 1 | 0 | — | PASS |
| U-05 | 1 | count | ring wall = 1 | 0 | — | PASS |
| feature_census | 1 | count | ring wall = 1 | 0 | — | PASS |
| U-05 | 3 | count | ring drain notches = 3 | 0 | — | PASS |
| feature_census | 3 | count | ring drain notches = 3 | 0 | — | PASS |
| U-05 | 2 | count | pin clearance through-holes (Ø4.8, Ø3.8) = 2 | 0 | — | PASS |
| feature_census | 2 | count | pin clearance through-holes (Ø4.8, Ø3.8) = 2 | 0 | — | PASS |
| U-05 | 3 | count | hooks = 3 | 0 | — | PASS |
| feature_census | 3 | count | hooks = 3 | 0 | — | PASS |
| U-05 | 3 | count | hooks at the planned angles = 3 | 0 | — | PASS |
| feature_census | 3 | count | hooks at the planned angles = 3 | 0 | — | PASS |
| U-05 | 2 | count | legs = 2 | 0 | — | PASS |
| feature_census | 2 | count | legs = 2 | 0 | — | PASS |
| U-05 | 1 | count | deck = 1 | 0 | — | PASS |
| feature_census | 1 | count | deck = 1 | 0 | — | PASS |
| U-05 | 1 | count | stem U-slot open to +Y (no closed stem bore) = 1 | 0 | — | PASS |
| feature_census | 1 | count | stem U-slot open to +Y (no closed stem bore) = 1 | 0 | — | PASS |
| U-05 | 2 | count | gusset slits = 2 | 0 | — | PASS |
| feature_census | 2 | count | gusset slits = 2 | 0 | — | PASS |
| U-05 | 2 | count | Ø3.4 screw clearance holes = 2 | 0 | — | PASS |
| feature_census | 2 | count | Ø3.4 screw clearance holes = 2 | 0 | — | PASS |
| U-05 | 2 | count | Ø4.0 insert bores = 2 | 0 | — | PASS |
| feature_census | 2 | count | Ø4.0 insert bores = 2 | 0 | — | PASS |
| U-07 | 0.05 | rad | angular a <= 4·acos(1 − 0.01/R_max), R_max 25.88010819142764 | 0.0612 | — | PASS |
| U-07 | 0.004 | mm | stl_max_sagitta <= 0.01 | 0.006 | (-9.3413, 13.3496, 10.2595) mm | PASS |
| U-07 | 1 | count | delivered STL: one body | 0 | — | PASS |
| U-07 | 0 | count | delivered STL: naked edges 0 | 0 | — | PASS |
| U-08 | — | — | threads cosmetic | — | — | N/A by its row (no threads; inserts) |
| D-07 | — | — | fit-critical reamed bores | — | — | N/A by its row (none) |
| J-06 | — | — | printed threads | — | — | N/A by its row (inserts) |
| E-06 | pads are the deck, tied to both legs over the full deck section; root fillets measured on the STEP: tori R16.0/r0.3 ×3, R19.0/r1.0 ×1, R19.37/r1.5 ×3, R24.37/r1.5 ×3; straight fillets r3.0 ×6 | — | reviewer | — | — | reviewer row; designer evidence only |
| D-03b | insert-bore ceilings Ø4.0 and notch ceilings 2.0 measured above | mm | reviewer, from sections | — | — | designer numbers PASS; reviewer row |
| REQ-09 | pin holes through (REQ-02 rows), window through (REQ-07 rows), recess drains through the pin holes (they open in its floor, length 9.4), three notches measured above | — | reviewer, from sections | — | — | designer numbers PASS; reviewer row |
| J-03 | catch/root thickness ratio rows above | ratio | reviewer | — | — | reported; ε is far from its limit, so the ratio does not bind |

Facts the gate rows rest on (measured, not gated):

- Placement (joints, from measured features): {"OD-H24": {"rim_face_area_mm2": 105.96, "axis_origin": [0.0, 0.0, 0.0], "placed_location": [0.0, 0.0, 10.0]}, "OD-H22": {"flange_face_area_mm2": 277.907, "axis_origin": [0.0, 0.0, -0.0], "ear_holes_x": [-15.338, 15.447], "ear_axis_deg": 0.0, "placed_location": [62.0, 0.0, 48.0]}}.
- OD-H22 assembly path, spec 1.2 U-03(b) (A-22: the valve is held by its two ear screws only and slides out along +Y when they are loose, hence the −Y path): slide y +45, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 13.6879 mm; slide y +35, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 7.1574 mm; slide y +25, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 4.4551 mm; slide y +16, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.9257 mm; slide y +14, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.8583 mm; slide y +12, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.8583 mm; slide y +10, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.8583 mm; slide y +8, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.8583 mm; slide y +6, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.8583 mm; slide y +4, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.8583 mm; slide y +2, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.8583 mm; slide y +0, z +5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.8781 mm; drop y +0, z +4: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.503 mm; drop y +0, z +3: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.503 mm; drop y +0, z +2: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.503 mm; drop y +0, z +1: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.503 mm; drop y +0, z +0.5: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0.5 mm; drop y +0, z +0: 0 mm³ with the mount, 0 mm³ with OD-H24, clearance to the mount 0 mm.
- Least clearance along the slide (flange back face at z 53.0): 0.8583 mm at pose y +14, z +5, mount point [69.05, 14.653, 48.0], OD-H22 point [68.460088, 14.653, 48.623379]. On the drop the clearance falls to 0 at the seat (the flange contact).
- OD-H24 descent poses: +25: 0 mm³; +20: 0 mm³; +15: 0 mm³; +10: 0 mm³; +5: 0 mm³; +2: 0 mm³; +1: 0 mm³; +0.5: 0 mm³; +0: 0 mm³ (hooks exempt).
- Deck wedge between each screw clearance hole and its slit end, width at the deck top (z 47.999, ray along X at y 0): +X 1.8981 mm, −X 1.7891 mm (D-01b's reason; `min_wall` does not read it because the hole wall and the 43.4° slit end are not opposed within 45°).
- Thinnest wall (D-01a/b, D-06a): 1.7224 mm at (-16.1007, 2.5198, 10.2555) mm: the ring wall at its base, between the 0.3 ring-root round and the 60° lip chamfer; it passes D-01b's 1.5. The 45° reading (U-06) is 1.6 mm at (-16.6791, 8.8253, 31.5000) mm, the catch tip.
- Hook beam to OD-H24 flange rim (the J-04 pair, not gated): hook 70° 0.51 mm; hook 160° 0.51 mm; hook 320° 0.51 mm.
- Hooks to the OD-H24 pipes and connector: 70° 37.9732 mm; 160° 21.0406 mm; 320° 13.3462 mm (outside r 20.5); to anything of OD-H24 above its flange top plane 4.9391 mm at (15.9825, -10.0319, 31.5000) mm (the 320° catch to the connector's corner). Accepted in spec 1.2 (A-09 note): the gate is D-04c ≥ 0.5, which passes; no change.
- Feature census (faces per kind): {"plane_faces": 53, "cylinder_faces": 30, "cone_faces": 5, "sphere_faces": 0, "torus_faces": 10, "bspline_faces": 0, "other_faces": 0, "concave_cylinders": 25, "convex_cylinders": 5, "bores": 12}.
- Flat downward faces found (D-03a named set): [{"z": 10.5, "area_mm2": 3.979, "centre": [15.665, 7.305]}, {"z": 10.5, "area_mm2": 3.979, "centre": [-12.222, -12.222]}, {"z": 10.5, "area_mm2": 3.979, "centre": [-7.305, 15.665]}, {"z": 40.3, "area_mm2": 1005.295, "centre": [61.999, -1.346]}, {"z": 29.9, "area_mm2": 10.937, "centre": [15.186, -12.743]}, {"z": 29.9, "area_mm2": 10.937, "centre": [-18.629, 6.78]}, {"z": 29.9, "area_mm2": 10.937, "centre": [6.78, 18.629]}, {"z": 46.0, "area_mm2": 3.487, "centre": [46.662, -0.0]}, {"z": 46.0, "area_mm2": 3.487, "centre": [77.447, -0.0]}].
- D-03a slab scans: [{"slab": [0.0, 10.5], "status": "MEASURED", "least_deg": 60.01836063114926, "at": [-11.865427, -13.599438, 10.083333], "reason": "", "bound": 0.009964}, {"slab": [10.5, 29.9], "status": "MEASURED", "least_deg": 60.01836063114926, "at": [18.217331, 1.71711, 10.516667], "reason": "", "bound": 0.009326}, {"slab": [29.9, 40.3], "status": "MEASURED", "least_deg": 90.0, "at": null, "reason": "", "bound": 0.0}, {"slab": [40.3, 46.0], "status": "MEASURED", "least_deg": 90.0, "at": null, "reason": "", "bound": 0.0}, {"slab": [46.0, 49.0], "status": "MEASURED", "least_deg": 90.0, "at": null, "reason": "", "bound": 0.0}].
- STL: R_max 25.8801 mm (the outer hook-root round), limit 4·acos(1 − 0.01/R_max) = 0.1112 rad; re-mesh of the STEP reproduces the delivered STL bytes: True; mesh census {"triangles": 92262, "bodies": 1, "naked_edges": 0, "winding": 1, "volume": 40560.32280203482}.

## 4. Robustness sweep (D7)

Each run rebuilt the part with one fit-critical parameter at the end of its spec 1.2 tolerance and ran the same spec 1.2 check script (all 228 rows, including the new U-03(b) path). The OEM poses stay at the spec §2 joints. For ring_ri, pin1_d, pin2_d, slot_w and slit_x_top the spec 1.2 band is one-sided (+0.1/−0): the low end is the nominal value, so the nominal check (§3) stands for it and only the high end was built.

| Parameter | Low · nominal · high | All built, one solid | New failures against nominal (measured) | Row whose margin fell most (margin) | U-03(b) OD-H22 path (mm³) / least slide clearance (mm), low · high |
|---|---|---|---|---|---|
| foot_hole_d | foot_hole_d=3.3 · nominal · foot_hole_d=3.5 | yes | none | low: REQ-06 footprint hole (-18, 21) Ø3.4 ± 0.1 (0 mm); high: REQ-06 footprint hole (-18, 21) Ø3.4 ± 0.1 (0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| ped_top_z | ped_top_z=9.9 · nominal · ped_top_z=10.1 | yes | low: U-03 contact: OD-H24 rim face on the pedestal top, clearance = 0 = 0.1 mm; low: REQ-02 recess R 14.10 ± 0.1 (radial_profile inner, z 9.5 ... 9.9) max = 14.25 mm; low: REQ-02 recess floor z 9.40 ± 0.05 = 9.3 mm; low: U-05 pedestal recess = 1 = 0 count; low: feature_census pedestal recess = 1 = 0 count; high: U-03 interference mount|OD-H24 <= 0 = 12.3516 mm3; high: U-03 mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 = 0 mm; high: D-04c mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 = 0 mm; high: U-03 (b) OD-H24 lowered along -Z from 25 mm, 9 poses, interference <= 0 (hooks exempt) = 12.3516 mm3; high: REQ-02 pin 2 Ø3.8: clearance to the OD-H24 pin >= 0.5 = 0 mm; high: D-04d pin 2 Ø3.8: printed sliding fit >= 0.30 per side = 0 mm; high: REQ-02 recess floor z 9.40 ± 0.05 = 9.5 mm; high: REQ-02 recess to the OD-H24 underside ribs and hub (H24 inside r 13.68) >= 0.5 = 0.4656 mm; high: REQ-01 ring inner R (radial_profile inner 0...359°, z 10.5...12.5) min in [16.30, 16.40] (spec 1.2) = — mm; high: REQ-01 ring inner R max in [16.30, 16.40] (spec 1.2) = — mm | low: REQ-02 pin 1 Ø4.8 length 9.4 ± 0.1 (recess floor to bottom face) (0 mm); high: REQ-02 pin 1 Ø4.8 length 9.4 ± 0.1 (recess floor to bottom face) (0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| ring_ri | = nominal (one-sided, spec 1.2) · nominal · ring_ri=16.40 | yes | none | high: D-01a min_wall >= 0.8 (0.8235 mm) | nominal · 0 / 0.8583 |
| pin1_d | = nominal (one-sided, spec 1.2) · nominal · pin1_d=4.9 | yes | none | — | nominal · 0 / 0.8583 |
| pin2_d | = nominal (one-sided, spec 1.2) · nominal · pin2_d=3.9 | yes | none | — | nominal · 0 / 0.8583 |
| hook_ri | hook_ri=20.77 catch_reach=1.9 · nominal · hook_ri=20.97 catch_reach=2.1 | yes | none | low: REQ-03 hook 70° beam inner face R 20.87 ± 0.1 over z 6...26 (min) (0 mm); high: REQ-03 hook 70° beam inner face R 20.87 ± 0.1 over z 6...26 (min) (0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| hook_t | hook_t=1.9 · nominal · hook_t=2.1 | yes | none | low: J-02 hook 70° beam thickness >= 1.0 (0.9 mm); high: J-03 hook 70° catch/root thickness ratio reported; binding only if ε within 0.2 % of 1.5 % (1.4524 ratio) | 0 / 0.8583 · 0 / 0.8583 |
| catch_under_z | catch_under_z=29.8 · nominal · catch_under_z=30.0 | yes | low: U-03 interference mount|OD-H24 <= 0 = 1.7888 mm3; low: D-04c hooks to OD-H24 above its flange top plane (z > 29.901) >= 0.5 = 0 mm; low: J-04 hook 70° undeflected at the engaged pose: interference <= 0 = 0.5963 mm3; low: J-04 hook 160° undeflected at the engaged pose: interference <= 0 = 0.5963 mm3; low: J-04 hook 320° undeflected at the engaged pose: interference <= 0 = 0.5963 mm3; high: U-03 contact: hook 70° catch underside on the OD-H24 flange top, clearance = 0 = 0.1 mm; high: U-03 contact: hook 160° catch underside on the OD-H24 flange top, clearance = 0 = 0.1 mm; high: U-03 contact: hook 320° catch underside on the OD-H24 flange top, clearance = 0 = 0.1 mm; high: REQ-03 hook 70° catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0 = 0.4126 mm3; high: REQ-03 hook 70° catch underside on the flange top, clearance = 0 = 0.1 mm; high: J-04 hook 70° catch underside touches the flange top, clearance = 0 = 0.1 mm; high: REQ-03 hook 160° catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0 = 0.4126 mm3; high: REQ-03 hook 160° catch underside on the flange top, clearance = 0 = 0.1 mm; high: J-04 hook 160° catch underside touches the flange top, clearance = 0 = 0.1 mm; high: REQ-03 hook 320° catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0 = 0.4126 mm3; high: REQ-03 hook 320° catch underside on the flange top, clearance = 0 = 0.1 mm; high: J-04 hook 320° catch underside touches the flange top, clearance = 0 = 0.1 mm | low: REQ-03 hook 70° catch underside z 29.9 ± 0.1 (0 mm); high: REQ-03 hook 70° catch underside z 29.9 ± 0.1 (0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| catch_ri | catch_reach=1.9 · nominal · catch_reach=2.1 | yes | none | low: REQ-03 hook 320° catch reaches R 18.87 ± 0.1 (0 mm); high: REQ-03 hook 70° catch reaches R 18.87 ± 0.1 (-0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| leg_gap_half | leg_gap_half=21.9 · nominal · leg_gap_half=22.1 | yes | low: D-03a least overhang >= 45° off the named faces (deck underside, 3 catch undersides supported; 2 insert-bore and 3 notch ceilings bridges) = 0 deg; low: D-03a no flat downward face other than the named ones = 2 count | low: REQ-07 leg inner face at x 40.0 ± 0.1 (0 mm); high: REQ-07 leg inner face at x 40.0 ± 0.1 (0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| deck_top_z | deck_top_z=47.9 · nominal · deck_top_z=48.1 | yes | low: U-03 contact: OD-H22 flange back face on the deck top, clearance = 0 = 0.1 mm; low: REQ-04 deck top flat under the OD-H22 flange outline: flange area not on the z 48 plane beyond the slot and slits (mm²) <= 0 = 98.1893 mm2; high: U-03 interference mount|OD-H22 <= 0 = 22.8905 mm3; high: U-03 mount to OD-H22 below its flange back face >= 0.5 = 0 mm; high: D-04c mount to OD-H22 below its flange back face >= 0.5 = 0 mm; high: U-03 (b) OD-H22 slid along -Y at +5 (flange back face z 53.1) from y +45 to 0 (12 poses), then lowered 5 along -Z (7 poses incl. the slide end); interference with the mount <= 0 = 22.8905 mm3; high: REQ-04 deck top flat under the OD-H22 flange outline: flange area not on the z 48 plane beyond the slot and slits (mm²) <= 0 = 98.9502 mm2; high: REQ-04 clearance(mount, OD-H22) away from the flange contact >= 0.5; nearest points in 'at' = 0 mm | low: U-02 size_z 48.0 ± 0.1 (0 mm); high: U-02 size_z 48.0 ± 0.1 (0 mm) | 0 / 0.9309 · 22.8905 / 0.7856 |
| deck_t | deck_t=7.6 · nominal · deck_t=7.8 | yes | high: D-01a min_wall >= 0.8 = 0.1 mm; high: D-01b min_wall >= 1.5 = 0.1 mm; high: D-06a minimum feature >= 1.0 = 0.1 mm; high: U-06 Soft: min_wall wide (45°) >= 1.5 = 0.1 mm | low: D-05a insert pad (77.447, 0): material across the bore >= 8.0 (least of 8 diameters × 3 depths) (8.3691 mm); high: REQ-04 slot through the deck, length 7.7 ± 0.1 (0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| slot_w | = nominal (one-sided, spec 1.2) · nominal · slot_w=14.2 | yes | none | — | nominal · 0 / 0.8926 |
| slit_w | slit_w=2.3 · nominal · slit_w=2.5 | yes | none | low: REQ-04 gusset slit +X 2.40 ± 0.1 wide (worst) (0 mm); high: REQ-04 gusset slit +X 2.40 ± 0.1 wide (worst) (0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| slit_x_top | = nominal (one-sided, spec 1.2) · nominal · slit_x_top=11.95 | yes | none | high: J-05 insert bore (46.662, 0): wall >= 3.0 over its depth (16 angles × 3 depths) (0.7128 mm) | nominal · 0 / 0.8583 |
| screw_dx | screw_dx=15.347,-15.438 · nominal · screw_dx=15.547,-15.238 | yes | none | — | 0 / 0.8583 · 0 / 0.8583 |
| screw_clear_d | screw_clear_d=3.3 · nominal · screw_clear_d=3.5 | yes | none | low: REQ-05 screw clearance (77.447, 0) Ø3.4 ± 0.1 (0 mm); high: REQ-05 screw clearance (77.447, 0) Ø3.4 ± 0.1 (0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| insert_d | insert_d=3.95 · nominal · insert_d=4.05 | yes | none | low: REQ-05 insert bore (77.447, 0) Ø4.0 ± 0.05 (0 mm); high: D-03b insert bore ceiling (77.447, 0): bridge span (bore Ø) <= 5 (0.95 mm) | 0 / 0.8583 · 0 / 0.8583 |
| recess_r | recess_r=14.0 · nominal · recess_r=14.2 | yes | low: U-03 mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 = 0.4386 mm; low: D-04c mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 = 0.4386 mm; low: REQ-02 recess to the OD-H24 underside ribs and hub (H24 inside r 13.68) >= 0.5 = 0.4386 mm; high: REQ-02 recess R 14.10 ± 0.1 (radial_profile inner, z 9.5 ... 9.9) max = 14.25 mm; high: U-05 pedestal recess = 1 = 0 count; high: feature_census pedestal recess = 1 = 0 count | low: REQ-02 recess R 14.10 ± 0.1 (radial_profile inner, z 9.5 ... 9.9) min (-0 mm); high: REQ-02 recess R 14.10 ± 0.1 (radial_profile inner, z 9.5 ... 9.9) min (0 mm) | 0 / 0.8583 · 0 / 0.8583 |
| recess_depth | recess_depth=0.55 · nominal · recess_depth=0.65 | yes | none | low: REQ-02 pin 1 Ø4.8 length 9.4 ± 0.1 (recess floor to bottom face) (0.05 mm); high: REQ-02 pin 1 Ø4.8 length 9.4 ± 0.1 (recess floor to bottom face) (0.05 mm) | 0 / 0.8583 · 0 / 0.8583 |

Passes only at nominal (a new failure at one end of its tolerance): ped_top_z, catch_under_z, leg_gap_half, deck_top_z, deck_t, recess_r. Causes, read from the failing rows:

- ped_top_z: the pedestal top is the OD-H24 seat; with the pose fixed at the spec joint, 9.9 leaves the rim 0.1 above it and 10.1 pushes it into the flowmeter; the recess moves with the pedestal top, so its floor and its chamfer leave REQ-02's z bands; at 10.1 the pin 2 clearance reads 0 and the REQ-01 ring profile reads nothing (INCONCLUSIVE, the flowmeter pose overlaps the seat).
- catch_under_z: the catch underside is the designed contact with the flange top; 29.8 overlaps the flange, 30.0 leaves 0.1 and the landing prism reads the gap as void.
- leg_gap_half: the leg inner faces are also the window edges (x 40.0 / 84.0); a leg face 0.1 inside the window leaves a 0.1 flat ledge over the window, a downward face D-03a does not name.
- deck_top_z: the deck top is the OD-H22 seat; 47.9 leaves the flange 0.1 above it, 48.1 pushes it into the valve (so the U-03(b) path's final pose overlaps too).
- deck_t: the deck is exactly 2.0 clearance + 5.7 insert deep; at 7.8 a 0.1 web closes the screw path between the two bores.
- recess_r: high: the 0.20 recess edge chamfer adds 0.05 at z 9.85, so R 14.20 reads 14.25 in REQ-02's band z 9.5 … 9.9; low: at R 14.00 the recess edge comes 0.44 from the OD-H24 ribs (note-A cut).

The seat heights (ped_top_z, deck_top_z, catch_under_z) are designed contacts against OEM poses fixed at the spec §2 joints, and the leg inner faces are also the window edges; spec 1.2 leaves their bands as they are (brief WP-04), so these runs are kept here as findings for the reviewer (§9), not fixed. The five parameters made one-sided in spec 1.2 (ring_ri, pin1_d, pin2_d, slot_w, slit_x_top) pass at both ends unless listed above.

Every sweep run built one valid solid unless the table says NO. Check script SHA-256 recorded in the run records: c30385f18471874b8c8b19e9c1aa405c2f3af3ddcd5371e351c46233a6ecc75e (§1 lists the check script's hash).

## 5. Build facts

- Envelope 119 × 50 × 48 mm at min (-25, -25, 0); volume 40560.7346 mm³ (STEP); mass 51.5 g at 1270 kg/m³ (A-11), centre of mass (34.9, -0.1, 17.6) mm
- Fillets (requested ladder → achieved, v01 build unchanged): leg roots: [3.0, 2.0, 1.0] → 3.0; pedestal root: [1.0, 0.5] → 1.0; hook roots (inner and outer faces): [1.5, 1.0, 0.5] → 1.5; ring inner root: [0.3, 0.2, 0.1] → 0.3. Measured on the STEP: tori (major/minor) R16.0/r0.3 ×3, R19.0/r1.0 ×1, R19.37/r1.5 ×3, R24.37/r1.5 ×3; straight root rounds r3.0 ×6. The hook side edges (radial, at the sector ends) are left sharp (§8).
- Placements: OD-H24 by a RigidJoint at its measured datum (rim face: the −Z planar face at z 0; axis: the rim bore on (0, 0)), connected to the mount's joint at (0, 0, 10.0), no rotation; OD-H22 by a RigidJoint at its measured datum (flange back face: the −Z planar face at z 0; axis: the drive-tube bore; +X through the two ear holes at x −15.338 and +15.447), connected to the mount's joint at (62.0, 0, 48.0). Measured placement in §3.
- Print: bottom face on the bed; supports under the deck (z 40.3) and the three catch undersides (z 29.9) only (A-16); bridges: two insert-bore ceilings (z 46.0, Ø4.0) and three notch ceilings (z 10.5, 2.0 wide).

## 6. Plausibility (§P, D6)

Sections: the v01 set in `03_Sections/` (§1). The delivered poses of both OEM parts are unchanged in spec 1.2, so the two assembly sections still show the delivered pose and were not regenerated.

| # | Question | Designer's answer, from the sections and the check assembly |
|---|---|---|
| P1 | gravity | The plate lies flat on the OD-C01 floor; OD-H24 rests on its rim on the pedestal top and OD-H22 on its flange back face on the deck top (both contacts measured 0 with 0 mm³ overlap); the centre of mass (34.9, -0.1, 17.6) lies inside the footprint. |
| P2 | function chains | Valve ports leave toward ±Y under the deck, between the legs, over the open window (REQ-07); the flowmeter pipes leave toward −Y above the ring; ear screws go down through the ears into inserts pressed from below; the three catches bear on the flange top outside its slots (0 mm³ void under each). |
| P3 | motion clearance | OD-H24 lowered from 25 mm: 0 mm³ at all 9 poses (hooks deflect). OD-H22 along the spec 1.2 path (18 poses: slide at +5.0 from y +45 to 0, drop 5.0): 0 mm³ with the mount, 0 mm³ with OD-H24; least gap on the slide 0.8583 mm; on the drop the stem enters the U-slot and the gussets the slits from above. |
| P4 | human factors | Nothing above z 48.0 and nothing within r 12 of the valve axis above the deck (REQ-08): the OPV at the drive-tube top stays open from above; the ear screws are driven from above; the valve is fitted by sliding it in along −Y about 5 mm above the deck and dropping it into the slits; the hooks are released by pulling the catches outward. |
| P5 | absurdity next to a real product | A 119 × 50 × 48 mm PETG bracket of 51.5 g with 2 mm snap beams 25.9 mm long and 4 mm walls: ordinary proportions for a printed hydraulic bracket. |
| P6 | nothing floating, embedded, mirrored or upside down | One solid (U-01); both OEM solids in their spec frames (drive tube up, ports ±Y, pipes −Y, connector +X), 0 mm³ overlap at the delivered pose; the slot's semicircle is on −Y and its opening on +Y. |

## 7. Library and tools used

Cards (from the J2 plan, not re-read): `library/uno10/CARD.md#u2-classic-box`, `library/uno10/CARD.md#u5-tank-heat-set`. `tools.core`: read_step, write_step, step_roundtrip, compare_step, validity, solid_count, brep_valid, common_volume, fillet_ladder, write_stl, mesh_sagitta. `tools.measure`: envelope, bore_census, locate_bore, feature_census, min_wall, min_wall_wide, overhang_census, clearance, radial_extent, radial_profile, mesh_census, mass_properties. `tools.drawing`: write_sections (v01). `tools.result.gate` for every comparison. New job code (in `01_CAD/`, not in the repo): the two assembly paths (loops over `common_volume` and `clearance`), the J-01 arithmetic, the note-A contact cuts, the D-03a slab scan, the flange flatness area, the notch and slit ray probes. No `tools/measure` function was missing.

## 8. Deviations from the plan

Carried over from REPORT v01 §8:

- Spec 1.1 amendments built as the brief states (checked by the orchestrator): Q1 → P-1, a U-slot 14.1 wide, semicircular about (62, 0) on −Y, straight walls at x 62 ± 7.05 open through the deck's +Y edge, no closed stem bore (the brief's "walls at y ±7.05" read as ±7.05 from the axis across X, since the slot opens along +Y); Q2 → slits 2.40 wide (y ±1.20) reaching x 62 ± 11.85 at the top, end taper 43.42°; Q3 → P-3 recess R 14.10 × 0.60 (floor z 9.40), pin holes 9.4 long; Q4 → P-4 hook 3 at 320°; Q5 → P-5 three notches 2.0 × 0.5 at 25°, 115°, 225°; Q6 → the insert-bore and notch ceilings are gated under D-03b and named out of D-03a; J-01 computed with y measured (1.5); the U-05 census list of the brief; U-03(b) path along −Y at +0.5 (spec 1.1; replaced by the spec 1.2 path, below); A-22 cited in §3.
- Deck unioned before the root fillets (plan: after): the window splits the plate in two, and only the deck joins the halves, so the fillet ladder's one-solid test needs it in place.
- Hook root fillets (fix cycle 1): the plan filleted the hook foot edges with `fillet_ladder`; that result lost 0.0027 mm³ through the STEP round trip (U-04 band 0.001), from the corner blends where the radial and arc fillets meet. The fillets are now webs of radius 1.5 in the revolved hook profile (inner and outer beam faces), so they are exact tori cut by the sector planes; the ladder (1.5, 1.0, 0.5) is kept with a one-valid-solid test per rung; the two radial side edges of each hook foot are left sharp. Round trip after: 1.8e-09 mm³.
- STL angular tolerance 0.05 rad (plan: 0.1183, the U-07 upper bound): at 0.1183 the mesher left 0.037 mm sagitta on the 0.3 ring-root round (fix cycle 1); 0.05 gives 0.0040 mm with 92 262 triangles.
- Ring lip chamfer 0.30 radial × 0.52 high, 60° from horizontal (plan F05b: 0.30 × 45°): a cone at exactly 45° reads INCONCLUSIVE in `overhang_census` (its sampling bound straddles the limit).
- Catch land 1.6 (plan: 1.0), fix cycle 2: U-06 (Soft) read the catch tip, where the underside and the 45° lead-in are opposed within 45°, as a 1.0 wall. Hook top now z 33.5. Catch underside, reach, lead-in, L, y and ε are unchanged.
- Recess edge chamfer 0.20 × 45° (not in the plan), fix cycle 2: with a sharp recess rim the OD-H24 ribs (note-A cut, r ≤ 13.68) were 0.432 from the rim edge against REQ-02's ≥ 0.5; now 0.516. The recess reads R 14.10 … 14.15 over REQ-02's band z 9.5 … 9.9, the floor z 9.40.
- The build script's last edit (where `main()` writes the build-facts JSON: `01_CAD/check_out_v01/` instead of `02_STEP_STL/`) came after the v01 export; the geometry code is unchanged, and the check's U-04 rebuild with the listed script matches the delivered STEP (volume delta and faces delta in §3).
- Ring inner root fillet 0.3 achieved with the plan's acceptance test (ring gap to the OD-H24 cup ≥ 0.50 after the rung).
- REQ-04 slot profile read over 192° … 348° instead of 180° … 360°: the two slits leave the slot along ±X and, at z ≥ 43.4, open the rays at 180° and 360° to the slit ends; the straight walls and the width are read separately at y 2.5 … 14. The flatness clause is gated as the flange-back-face area (mm²) that neither rests on the z 48 deck plane nor lies over the planned slot and slits.
- D-03a is scanned in five horizontal slabs whose floors lie at z 10.5, 29.9, 40.3 and 46.0, so exactly the named faces (3 notch ceilings, 3 catch undersides, the deck underside, 2 insert-bore ceilings) rest on a slab's bed; a second row counts flat downward faces outside that set (0).
- Two D-04c rows added to the plan's: the hooks to OD-H24 outside r 20.5 (pipes, connector) and the hooks to OD-H24 above its flange top plane.
- REQ-03's landing clause is gated as the void under each catch (sector r 18.87 … 19.70, 2.65 deep to the slot floors) ≤ 0 mm³, not against the J2 probe's 20.69 mm³.

New in v02 (WP-04, spec 1.2; no geometry change):

- U-03(b) OD-H22 path per spec 1.2: the check sets it in its own constant `U03B` (slide at +5.0 over y 45, 35, 25, 16, 14, 12, 10, 8, 6, 4, 2, 0, then the drop at z +4, 3, 2, 1, 0.5, 0) and replaces the build Params' h22_* fields with it (the build never reads them; the build script is not edited, brief WP-04). The path is checked against the mount and, in a second row, against the seated OD-H24 (spec: 'against everything but the hooks'); the clearance to the mount is measured at every slide pose and the least is reported.
- One-sided bands of spec 1.2 in the check: REQ-01 ring inner R [16.30, 16.40]; REQ-02 pin bores Ø4.8 / Ø3.8 +0.1/−0; REQ-04 slot profile [7.05, 7.10], slot width 14.1 +0.1/−0, slit reach 11.85 +0.1/−0. The slot straight-wall row, one row per side in v01 (the reading farthest from 7.05), is now two rows per side (least and greatest), since a one-sided band has no single worst direction. The brief's 'straight walls y ±(7.05 +0.05/−0)' is read, as in v01, as ±7.05 from the axis across X.
- The check writes its temporary re-mesh (U-07) next to its output JSON instead of `check_out_v01/`, so parallel sweep runs no longer share one temporary file.
- The sweep driver writes to `01_CAD/sweep_v02/`; the five one-sided parameters are swept at the high end only (their low end is the nominal). A new REPORT writer `report_od_c07_mount_v02.py`; the v01 writer and REPORT stay as the record of the stop.
- No section was regenerated: the delivered poses in the two assembly sections are unchanged in spec 1.2.

## 9. What I am least sure of

1. The two pin clearances read 0.49999999999999967 and 0.49999999999999833 mm against ≥ 0.5 (margins inside the 0.005 band): zero margin by design at the nominal, which spec 1.2 makes the low end of the bore band; they rest on scan-derived pin diameters (A-07, A-01). A 0.3 % scale error or a pin 0.01 mm fatter fails REQ-02 and D-04c; D-04d (≥ 0.30) keeps 0.2 in hand.
2. REQ-02's rib clause and D-04c against OD-H24 (0.5161 mm) depend on where the ribs are taken to end: the check takes OD-H24 inside r 13.68 (the plan's note-A contact zone). Taken to r 14.056 the gap at the recess edge would read about 0.1, inside the rim contact. The recess_r low run fails this row (§4).
3. The seat parameters pass only at nominal (§4): ped_top_z, deck_top_z, catch_under_z against the fixed OEM poses, leg_gap_half at the window edge, deck_t (a 0.1 web at 7.8) and recess_r. These are designed contacts or exact stack-ups, not clearances; the reviewer should decide whether any needs a spec band. The 320° catch sits 4.9391 mm from the connector corner (accepted in spec 1.2, A-09).

## 10. Stop

Not stopped.

Fix cycles used in this package (WP-04): 0 of 3. The re-run showed no geometry fault, so the STEP, STL and build script are the v01 files (WP-03 used 2 of its 3 cycles on U-04 / U-07 and U-06 / REQ-02, REPORT v01).

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20260930-od-c07-valve-flowmeter-mount",
 "part": "od_c07_mount",
 "tag": "v02",
 "spec_version": "1.2",
 "files": [
  {
   "path": "01_CAD/check_od_c07_mount.py",
   "sha256": "c30385f18471874b8c8b19e9c1aa405c2f3af3ddcd5371e351c46233a6ecc75e"
  },
  {
   "path": "01_CAD/build_od_c07_mount.py",
   "sha256": "8a45119c6543c50e1d16090ec4e62ebf729e1f06121805fa8efb018ab4424f21"
  },
  {
   "path": "01_CAD/sections_od_c07_mount.py",
   "sha256": "a58ac181c746e0ee947a5921b854d5c2b4789b6cb72a0ba72b56ff6fb117f218"
  },
  {
   "path": "01_CAD/sweep_od_c07_mount.py",
   "sha256": "587b497caf0f67635e0212d10c2b2f1226ed2e472fc3d767bed65297d984e00d"
  },
  {
   "path": "01_CAD/report_od_c07_mount_v02.py",
   "sha256": "4ff4b0f840fc0f438e56016e4c2c59762a4228ed7a17286a8b6896d9e398988e"
  },
  {
   "path": "02_STEP_STL/od_c07_mount_C1_v01.step",
   "sha256": "55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c"
  },
  {
   "path": "02_STEP_STL/od_c07_assembly_C1_v01.step",
   "sha256": "50d126c13b945edca3cfd9a5082189ddbd6380bfbb6e59cd24bc71c546f6c9d7"
  },
  {
   "path": "02_STEP_STL/od_c07_mount_C1_v01.stl",
   "sha256": "41bccd61c1fb0e82a7a8171c85da2128d0c01ca6906f80c03c5ffebf83de3c38"
  },
  {
   "path": "03_Sections/od_c07_mount_v01_front_y0.png",
   "sha256": "07e3dfaa6dcf1b66c63899d01e3e4f22878b5607994d31a2c61d4437616f20d4"
  },
  {
   "path": "03_Sections/od_c07_mount_v01_top_z10p25.png",
   "sha256": "12227a9402aac63b16f00cf593480dc9c4e76d17f5e9ef5ddef015f1fb6901cd"
  },
  {
   "path": "03_Sections/od_c07_mount_v01_top_z47.png",
   "sha256": "58e1855969367303edd2ba843912635c0572643e92e9308d2740bc6d571c09cc"
  },
  {
   "path": "03_Sections/od_c07_mount_v01_left_x62.png",
   "sha256": "b22fd218abd547d0ba49e597cf9e241d62e97b3a596b721367456e593aac7586"
  },
  {
   "path": "03_Sections/od_c07_mount_v01_left_x7p48.png",
   "sha256": "fe7e47b4f7fbb36c9674d2bd284c5ecebc51b4768d126f86413e527c99fe0538"
  },
  {
   "path": "03_Sections/od_c07_mount_v01_left_xm11p78.png",
   "sha256": "26f17982ec3da2d0029652a472feeb629874bed6157806c6d542f558eeadd891"
  },
  {
   "path": "03_Sections/od_c07_assembly_v01_front_y0.png",
   "sha256": "c82c911de5ea50f00c486ac232a3be73757d6b618e02b364fed83a3ebfa0bb0a"
  },
  {
   "path": "03_Sections/od_c07_assembly_v01_left_x62.png",
   "sha256": "627480207b47ba5bec15e2fc71f72661d680b644b339740bcd878d75cb8677ec"
  },
  {
   "path": "01_CAD/check_out_v02/check_v02.json",
   "sha256": "cd3a567f088cd7b1fa7c1dd18f71a9f770edfa7d1b39545de07b7d4482d22d0a"
  },
  {
   "path": "01_CAD/check_out_v02_log.txt",
   "sha256": "cb1f3eee759f228bccd73652c2900ed2c264aa2ff52bfacfed5251caa38f8067"
  },
  {
   "path": "01_CAD/sweep_v02_log.txt",
   "sha256": "a452afe2c2e9457eb68322a64918828f96eb883bc75c7799c5f1f5fc423430f2"
  },
  {
   "path": "01_CAD/check_out_v01/build_facts_v01.json",
   "sha256": "e9da6f4a97f21078f7aa7e74c004979579322729965814c98138e990ce1f415a"
  },
  {
   "path": "01_CAD/check_out_v01/sections_v01.json",
   "sha256": "1564c0b52f41c50a1b0529632a4c99ac7921340c1cf20bbdf26c7be6eda50adb"
  },
  {
   "path": "01_CAD/REPORT_od_c07_mount_v01.md",
   "sha256": "717ac5c21c442873bfa552e3e062c4ebb881b37a5bc543cc2d5b82d62ea427bc"
  },
  {
   "path": "01_CAD/report_od_c07_mount.py",
   "sha256": "3d7fb982a1620b6e103aa294f3451a96194ec4af5fd56224f90411bcdd851f79"
  },
  {
   "path": "01_CAD/check_out_v01/check_v01.json",
   "sha256": "b9458e5ed41524be54007e3d267b79f7c99b65a9e66fc5ab4d66ea1dc04509d4"
  },
  {
   "path": "01_CAD/build_probes_v01/probe_b1_v01.py",
   "sha256": "7232e5133329411a71d49a88766b5018210960d98591dc704696a6c42eb07808"
  },
  {
   "path": "01_CAD/build_probes_v01/probe_b2_v01.py",
   "sha256": "fb3ae6383a436b2075ad1766a5765812001df40dc0e84639bb97f5e5b7694348"
  },
  {
   "path": "01_CAD/build_probes_v01/probe_b3_v01.py",
   "sha256": "667ffce64a6d63c0571194aff9389012040dd825972577ac018ff6d7ec10e556"
  },
  {
   "path": "01_CAD/build_probes_v01/probe_b4_v01.py",
   "sha256": "00fbebf7bd5d7bafad5cb06fd6579d64e23a3ca090b7863edf5a7cfb92317743"
  },
  {
   "path": "01_CAD/build_probes_v01/probe_b5_v01.py",
   "sha256": "57cbdd4552def2f84af87cee27f4fd5868d655c39a05fd6aaebf992005c16d3c"
  },
  {
   "path": "01_CAD/build_probes_v01/probe_b6_v01.py",
   "sha256": "a44722f9f1f62fba816f37178798a58291aee108e9f85952187121c2e4597c1a"
  },
  {
   "path": "01_CAD/build_probes_v01/probe_b7_v01.py",
   "sha256": "054ec4aabd5a2ad5404c87769801ad65cd20609e5f25ff2b89f8d19c20707689"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "7.9.3.1",
  "repo_commit": "70826895ab7666f9e5aee3f77ce88f099995f3c1"
 },
 "gates": [
  {
   "gate": "exactly_one_solid",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01",
   "measured": 1,
   "unit": "count",
   "required": "solid_count = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01",
   "measured": 1,
   "unit": "bool",
   "required": "brep_valid = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01",
   "measured": 0,
   "unit": "count",
   "required": "naked_edges = 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02",
   "measured": 119.0,
   "unit": "mm",
   "required": "size_x 119.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec",
   "measured": 119.0,
   "unit": "mm",
   "required": "size_x 119.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02",
   "measured": 50.0,
   "unit": "mm",
   "required": "size_y 50.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec",
   "measured": 50.0,
   "unit": "mm",
   "required": "size_y 50.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02",
   "measured": 48.0,
   "unit": "mm",
   "required": "size_z 48.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec",
   "measured": 48.0,
   "unit": "mm",
   "required": "size_z 48.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02",
   "measured": -25.0,
   "unit": "mm",
   "required": "position min_x -25.0 \u00b1 0.1 (reported apart)",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec",
   "measured": -25.0,
   "unit": "mm",
   "required": "position min_x -25.0 \u00b1 0.1 (reported apart)",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02",
   "measured": -25.0,
   "unit": "mm",
   "required": "position min_y -25.0 \u00b1 0.1 (reported apart)",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec",
   "measured": -25.0,
   "unit": "mm",
   "required": "position min_y -25.0 \u00b1 0.1 (reported apart)",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02",
   "measured": 0.0,
   "unit": "mm",
   "required": "position min_z 0.0 \u00b1 0.1 (reported apart)",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec",
   "measured": 0.0,
   "unit": "mm",
   "required": "position min_z 0.0 \u00b1 0.1 (reported apart)",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-02",
   "measured": 119.0,
   "unit": "mm",
   "required": "size_x <= 220.0",
   "margin": 101.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-12"
   ]
  },
  {
   "gate": "D-02",
   "measured": 50.0,
   "unit": "mm",
   "required": "size_y <= 220.0",
   "margin": 170.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-12"
   ]
  },
  {
   "gate": "D-02",
   "measured": 48.0,
   "unit": "mm",
   "required": "size_z <= 250.0",
   "margin": 202.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-12"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm3",
   "required": "interference mount|OD-H24 <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm3",
   "required": "interference mount|OD-H22 <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm",
   "required": "contact: OD-H24 rim face on the pedestal top, clearance = 0",
   "margin": 0.0,
   "at": "(14.3000, 0.0000, 10.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm",
   "required": "contact: OD-H22 flange back face on the deck top, clearance = 0",
   "margin": 0.0,
   "at": "(69.0500, 1.2000, 48.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm",
   "required": "contact: hook 70\u00b0 catch underside on the OD-H24 flange top, clearance = 0",
   "margin": 0.0,
   "at": "(8.8253, 16.6791, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm",
   "required": "contact: hook 160\u00b0 catch underside on the OD-H24 flange top, clearance = 0",
   "margin": 0.0,
   "at": "(-16.6791, 8.8253, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm",
   "required": "contact: hook 320\u00b0 catch underside on the OD-H24 flange top, clearance = 0",
   "margin": 0.0,
   "at": "(15.9825, -10.0319, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.49999999999999833,
   "unit": "mm",
   "required": "mount (hooks aside) to OD-H24 away from the rim contact >= 0.5",
   "margin": -1.6653345369377348e-15,
   "at": "(2.5850, 0.0930, 9.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "D-04c",
   "measured": 0.49999999999999833,
   "unit": "mm",
   "required": "mount (hooks aside) to OD-H24 away from the rim contact >= 0.5",
   "margin": -1.6653345369377348e-15,
   "at": "(2.5850, 0.0930, 9.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.5029999999999994,
   "unit": "mm",
   "required": "mount to OD-H22 below its flange back face >= 0.5",
   "margin": 0.003,
   "at": "(55.0529, -1.2000, 43.7660) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "D-04c",
   "measured": 0.5029999999999994,
   "unit": "mm",
   "required": "mount to OD-H22 below its flange back face >= 0.5",
   "margin": 0.003,
   "at": "(55.0529, -1.2000, 43.7660) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "D-04c",
   "measured": 13.346234984778842,
   "unit": "mm",
   "required": "hooks to OD-H24 pipes and connector (outside r 20.5) >= 0.5",
   "margin": 12.846234985,
   "at": "(12.6548, -13.9976, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "D-04c",
   "measured": 4.9390973732692,
   "unit": "mm",
   "required": "hooks to OD-H24 above its flange top plane (z > 29.901) >= 0.5",
   "margin": 4.439097373,
   "at": "(15.9825, -10.0319, 31.5000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm3",
   "required": "(b) OD-H24 lowered along -Z from 25 mm, 9 poses, interference <= 0 (hooks exempt)",
   "margin": 0.0,
   "at": "OD-H24 raised 25.0 mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm3",
   "required": "(b) OD-H22 slid along -Y at +5 (flange back face z 53) from y +45 to 0 (12 poses), then lowered 5 along -Z (7 poses incl. the slide end); interference with the mount <= 0",
   "margin": 0.0,
   "at": "OD-H22 at y +45.0 mm, z +5.0 mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-03",
   "measured": 0.0,
   "unit": "mm3",
   "required": "(b) OD-H22 along the same 18 poses: interference with the seated OD-H24 <= 0",
   "margin": 0.0,
   "at": "OD-H22 at y +45.0 mm, z +5.0 mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "U-04",
   "measured": 1,
   "unit": "bool",
   "required": "schema AP242",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04",
   "measured": 1,
   "unit": "count",
   "required": "1 solid re-read",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04",
   "measured": 1.7826096154749393e-09,
   "unit": "mm3",
   "required": "volume delta 0",
   "margin": -2e-09,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04",
   "measured": 0,
   "unit": "count",
   "required": "faces delta 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04",
   "measured": 1,
   "unit": "bool",
   "required": "named body re-read unchanged",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04",
   "measured": 1,
   "unit": "bool",
   "required": "valid after re-import",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-06",
   "measured": 3.4,
   "unit": "mm",
   "required": "footprint hole (-18, 21) \u00d83.4 \u00b1 0.1",
   "margin": 0.1,
   "at": "(-18.0000, 21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 0.0,
   "unit": "mm",
   "required": "footprint hole (-18, 21) offset <= 0.10",
   "margin": 0.1,
   "at": "(-18.0000, 21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 4.0,
   "unit": "mm",
   "required": "footprint hole (-18, 21) length 4.0 \u00b1 0.1",
   "margin": 0.1,
   "at": "(-18.0000, 21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 1,
   "unit": "bool",
   "required": "footprint hole (-18, 21) through",
   "margin": 0.0,
   "at": "(-18.0000, 21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": "footprint hole (-18, 21) \u00d8 >= 3.25",
   "margin": 0.15,
   "at": "(-18.0000, 21.0000, 0.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-06",
   "measured": 3.4,
   "unit": "mm",
   "required": "footprint hole (-18, -21) \u00d83.4 \u00b1 0.1",
   "margin": 0.1,
   "at": "(-18.0000, -21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 0.0,
   "unit": "mm",
   "required": "footprint hole (-18, -21) offset <= 0.10",
   "margin": 0.1,
   "at": "(-18.0000, -21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 4.0,
   "unit": "mm",
   "required": "footprint hole (-18, -21) length 4.0 \u00b1 0.1",
   "margin": 0.1,
   "at": "(-18.0000, -21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 1,
   "unit": "bool",
   "required": "footprint hole (-18, -21) through",
   "margin": 0.0,
   "at": "(-18.0000, -21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": "footprint hole (-18, -21) \u00d8 >= 3.25",
   "margin": 0.15,
   "at": "(-18.0000, -21.0000, 0.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-06",
   "measured": 3.4,
   "unit": "mm",
   "required": "footprint hole (88.5, 21) \u00d83.4 \u00b1 0.1",
   "margin": 0.1,
   "at": "(88.5000, 21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 0.0,
   "unit": "mm",
   "required": "footprint hole (88.5, 21) offset <= 0.10",
   "margin": 0.1,
   "at": "(88.5000, 21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 4.0,
   "unit": "mm",
   "required": "footprint hole (88.5, 21) length 4.0 \u00b1 0.1",
   "margin": 0.1,
   "at": "(88.5000, 21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 1,
   "unit": "bool",
   "required": "footprint hole (88.5, 21) through",
   "margin": 0.0,
   "at": "(88.5000, 21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": "footprint hole (88.5, 21) \u00d8 >= 3.25",
   "margin": 0.15,
   "at": "(88.5000, 21.0000, 0.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-06",
   "measured": 3.4,
   "unit": "mm",
   "required": "footprint hole (88.5, -21) \u00d83.4 \u00b1 0.1",
   "margin": 0.1,
   "at": "(88.5000, -21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 0.0,
   "unit": "mm",
   "required": "footprint hole (88.5, -21) offset <= 0.10",
   "margin": 0.1,
   "at": "(88.5000, -21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 4.0,
   "unit": "mm",
   "required": "footprint hole (88.5, -21) length 4.0 \u00b1 0.1",
   "margin": 0.1,
   "at": "(88.5000, -21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "REQ-06",
   "measured": 1,
   "unit": "bool",
   "required": "footprint hole (88.5, -21) through",
   "margin": 0.0,
   "at": "(88.5000, -21.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-14"
   ]
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": "footprint hole (88.5, -21) \u00d8 >= 3.25",
   "margin": 0.15,
   "at": "(88.5000, -21.0000, 0.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-05",
   "measured": 3.4,
   "unit": "mm",
   "required": "screw clearance (77.447, 0) \u00d83.4 \u00b1 0.1",
   "margin": 0.1,
   "at": "(77.4470, 0.0000, 46.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 0.0,
   "unit": "mm",
   "required": "screw clearance (77.447, 0) offset <= 0.10",
   "margin": 0.1,
   "at": "(77.4470, 0.0000, 46.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 2.0,
   "unit": "mm",
   "required": "screw clearance (77.447, 0) depth 2.0 \u00b1 0.1",
   "margin": 0.1,
   "at": "(77.4470, 0.0000, 46.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": "screw clearance (77.447, 0) \u00d8 >= 3.25",
   "margin": 0.15,
   "at": "(77.4470, 0.0000, 46.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-05",
   "measured": 4.0,
   "unit": "mm",
   "required": "insert bore (77.447, 0) \u00d84.0 \u00b1 0.05",
   "margin": 0.05,
   "at": "(77.4470, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 0.0,
   "unit": "mm",
   "required": "insert bore (77.447, 0) coaxial offset <= 0.10",
   "margin": 0.1,
   "at": "(77.4470, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 5.700000000000003,
   "unit": "mm",
   "required": "insert bore (77.447, 0) depth 5.7 \u00b1 0.1",
   "margin": 0.1,
   "at": "(77.4470, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "D-05b",
   "measured": 4.0,
   "unit": "mm",
   "required": "insert bore (77.447, 0) \u00d8 4.0 \u00b1 0.05",
   "margin": 0.05,
   "at": "(77.4470, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "D-05b",
   "measured": 5.700000000000003,
   "unit": "mm",
   "required": "insert bore (77.447, 0) depth >= 5.7",
   "margin": 2.6645352591003757e-15,
   "at": "(77.4470, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "D-05b",
   "measured": 1,
   "unit": "bool",
   "required": "insert bore (77.447, 0) opens on the deck underside",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 3.4,
   "unit": "mm",
   "required": "screw clearance (46.662, 0) \u00d83.4 \u00b1 0.1",
   "margin": 0.1,
   "at": "(46.6620, 0.0000, 46.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 0.0,
   "unit": "mm",
   "required": "screw clearance (46.662, 0) offset <= 0.10",
   "margin": 0.1,
   "at": "(46.6620, 0.0000, 46.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 2.0,
   "unit": "mm",
   "required": "screw clearance (46.662, 0) depth 2.0 \u00b1 0.1",
   "margin": 0.1,
   "at": "(46.6620, 0.0000, 46.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "D-04a",
   "measured": 3.4,
   "unit": "mm",
   "required": "screw clearance (46.662, 0) \u00d8 >= 3.25",
   "margin": 0.15,
   "at": "(46.6620, 0.0000, 46.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-05",
   "measured": 4.0,
   "unit": "mm",
   "required": "insert bore (46.662, 0) \u00d84.0 \u00b1 0.05",
   "margin": 0.05,
   "at": "(46.6620, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 0.0,
   "unit": "mm",
   "required": "insert bore (46.662, 0) coaxial offset <= 0.10",
   "margin": 0.1,
   "at": "(46.6620, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "REQ-05",
   "measured": 5.700000000000003,
   "unit": "mm",
   "required": "insert bore (46.662, 0) depth 5.7 \u00b1 0.1",
   "margin": 0.1,
   "at": "(46.6620, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-13",
    "A-18"
   ]
  },
  {
   "gate": "D-05b",
   "measured": 4.0,
   "unit": "mm",
   "required": "insert bore (46.662, 0) \u00d8 4.0 \u00b1 0.05",
   "margin": 0.05,
   "at": "(46.6620, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "D-05b",
   "measured": 5.700000000000003,
   "unit": "mm",
   "required": "insert bore (46.662, 0) depth >= 5.7",
   "margin": 2.6645352591003757e-15,
   "at": "(46.6620, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "D-05b",
   "measured": 1,
   "unit": "bool",
   "required": "insert bore (46.662, 0) opens on the deck underside",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 4.8,
   "unit": "mm",
   "required": "pin 1 \u00d84.8 +0.1/-0 (one-sided, spec 1.2)",
   "margin": 0.0,
   "at": "(0.1850, 0.0930, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 0.0,
   "unit": "mm",
   "required": "pin 1 \u00d84.8 offset <= 0.10",
   "margin": 0.1,
   "at": "(0.1850, 0.0930, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 9.4,
   "unit": "mm",
   "required": "pin 1 \u00d84.8 length 9.4 \u00b1 0.1 (recess floor to bottom face)",
   "margin": 0.1,
   "at": "(0.1850, 0.0930, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 1,
   "unit": "bool",
   "required": "pin 1 \u00d84.8 through",
   "margin": 0.0,
   "at": "(0.1850, 0.0930, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 0.49999999999999967,
   "unit": "mm",
   "required": "pin 1 \u00d84.8: clearance to the OD-H24 pin >= 0.5",
   "margin": -3.3306690738754696e-16,
   "at": "(2.5850, 0.0930, 9.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-04d",
   "measured": 0.49999999999999967,
   "unit": "mm",
   "required": "pin 1 \u00d84.8: printed sliding fit >= 0.30 per side",
   "margin": 0.2,
   "at": "(2.5850, 0.0930, 9.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 3.8,
   "unit": "mm",
   "required": "pin 2 \u00d83.8 +0.1/-0 (one-sided, spec 1.2)",
   "margin": 0.0,
   "at": "(-11.7800, 0.1400, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 0.0,
   "unit": "mm",
   "required": "pin 2 \u00d83.8 offset <= 0.10",
   "margin": 0.1,
   "at": "(-11.7800, 0.1400, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 9.4,
   "unit": "mm",
   "required": "pin 2 \u00d83.8 length 9.4 \u00b1 0.1 (recess floor to bottom face)",
   "margin": 0.1,
   "at": "(-11.7800, 0.1400, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 1,
   "unit": "bool",
   "required": "pin 2 \u00d83.8 through",
   "margin": 0.0,
   "at": "(-11.7800, 0.1400, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 0.49999999999999833,
   "unit": "mm",
   "required": "pin 2 \u00d83.8: clearance to the OD-H24 pin >= 0.5",
   "margin": -1.6653345369377348e-15,
   "at": "(-9.8800, 0.1400, 9.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-04d",
   "measured": 0.49999999999999833,
   "unit": "mm",
   "required": "pin 2 \u00d83.8: printed sliding fit >= 0.30 per side",
   "margin": 0.2,
   "at": "(-9.8800, 0.1400, 9.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 14.099999999999998,
   "unit": "mm",
   "required": "recess R 14.10 \u00b1 0.1 (radial_profile inner, z 9.5 ... 9.9) min",
   "margin": 0.1,
   "at": "(13.8858, 2.4484, 9.5500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 14.149999999999954,
   "unit": "mm",
   "required": "recess R 14.10 \u00b1 0.1 (radial_profile inner, z 9.5 ... 9.9) max",
   "margin": 0.05,
   "at": "(14.1500, 0.0000, 9.8500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 9.4,
   "unit": "mm",
   "required": "recess floor z 9.40 \u00b1 0.05",
   "margin": 0.05,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02",
   "measured": 0.5161395160225561,
   "unit": "mm",
   "required": "recess to the OD-H24 underside ribs and hub (H24 inside r 13.68) >= 0.5",
   "margin": 0.016139516,
   "at": "(14.1000, 0.0000, 9.8000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-01",
   "measured": 10.0,
   "unit": "mm",
   "required": "pedestal top z 10.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "REQ-01",
   "measured": 16.299999999999997,
   "unit": "mm",
   "required": "ring inner R (radial_profile inner 0...359\u00b0, z 10.5...12.5) min in [16.30, 16.40] (spec 1.2)",
   "margin": -3.552713678800501e-15,
   "at": "(16.2603, 1.1370, 10.5500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "REQ-01",
   "measured": 16.3,
   "unit": "mm",
   "required": "ring inner R max in [16.30, 16.40] (spec 1.2)",
   "margin": 0.0,
   "at": "(16.3000, 0.0000, 10.5500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "REQ-01",
   "measured": 13.0,
   "unit": "mm",
   "required": "ring top z 13.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "REQ-01",
   "measured": 0.5313989773719694,
   "unit": "mm",
   "required": "clearance(ring, OD-H24 cup) in [0.50, 0.70]",
   "margin": 0.031398977,
   "at": "(16.3000, -0.0000, 13.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "D-04d",
   "measured": 0.5313989773719694,
   "unit": "mm",
   "required": "ring gap >= 0.30 per side",
   "margin": 0.231398977,
   "at": "(16.3000, -0.0000, 13.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-07"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 70.0,
   "unit": "deg",
   "required": "hook 70\u00b0 centred at 70\u00b0 \u00b1 1\u00b0",
   "margin": 1.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 20.87,
   "unit": "mm",
   "required": "hook 70\u00b0 beam inner face R 20.87 \u00b1 0.1 over z 6...26 (min)",
   "margin": 0.1,
   "at": "(9.4372, 18.6144, 6.2500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 20.87,
   "unit": "mm",
   "required": "hook 70\u00b0 beam inner face R 20.87 \u00b1 0.1 over z 6...26 (max)",
   "margin": 0.1,
   "at": "(9.4372, 18.6144, 6.2500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 29.9,
   "unit": "mm",
   "required": "hook 70\u00b0 catch underside z 29.9 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 18.869999999999997,
   "unit": "mm",
   "required": "hook 70\u00b0 catch reaches R 18.87 \u00b1 0.1",
   "margin": 0.1,
   "at": "(6.4539, 17.7320, 30.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 45.000000000025445,
   "unit": "deg",
   "required": "hook 70\u00b0 catch top chamfer 45\u00b0 \u00b1 1\u00b0 (from horizontal)",
   "margin": 1.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 0.0,
   "unit": "mm3",
   "required": "hook 70\u00b0 catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 0.0,
   "unit": "mm",
   "required": "hook 70\u00b0 catch underside on the flange top, clearance = 0",
   "margin": 0.0,
   "at": "(8.8253, 16.6791, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "J-04",
   "measured": 0.0,
   "unit": "mm3",
   "required": "hook 70\u00b0 undeflected at the engaged pose: interference <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08"
   ]
  },
  {
   "gate": "J-04",
   "measured": 0.0,
   "unit": "mm",
   "required": "hook 70\u00b0 catch underside touches the flange top, clearance = 0",
   "margin": 0.0,
   "at": "(8.8253, 16.6791, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08"
   ]
  },
  {
   "gate": "J-02",
   "measured": 1.999999999999549,
   "unit": "mm",
   "required": "hook 70\u00b0 beam thickness >= 1.0",
   "margin": 1.0,
   "at": "(9.7607, 18.4469, 26.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-01",
   "measured": 0.6708307866607529,
   "unit": "%",
   "required": "hook 70\u00b0 \u03b5 = 1.5\u00b7y\u00b7t/(L\u00b2\u00b7Q) <= 1.5 % (y = 20.37 \u2212 catch R, L = plate top to catch underside)",
   "margin": 0.829169213,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-15"
   ]
  },
  {
   "gate": "J-03",
   "measured": 2.0000000000000018,
   "unit": "ratio",
   "required": "hook 70\u00b0 catch/root thickness ratio reported; binding only if \u03b5 within 0.2 % of 1.5 %",
   "margin": 1.5,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-03",
   "measured": 160.0,
   "unit": "deg",
   "required": "hook 160\u00b0 centred at 160\u00b0 \u00b1 1\u00b0",
   "margin": 1.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 20.87,
   "unit": "mm",
   "required": "hook 160\u00b0 beam inner face R 20.87 \u00b1 0.1 over z 6...26 (min)",
   "margin": 0.1,
   "at": "(-18.6144, 9.4372, 6.2500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 20.87,
   "unit": "mm",
   "required": "hook 160\u00b0 beam inner face R 20.87 \u00b1 0.1 over z 6...26 (max)",
   "margin": 0.1,
   "at": "(-18.6144, 9.4372, 6.2500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 29.9,
   "unit": "mm",
   "required": "hook 160\u00b0 catch underside z 29.9 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 18.869999999999997,
   "unit": "mm",
   "required": "hook 160\u00b0 catch reaches R 18.87 \u00b1 0.1",
   "margin": 0.1,
   "at": "(-17.7320, 6.4539, 30.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 45.000000000025445,
   "unit": "deg",
   "required": "hook 160\u00b0 catch top chamfer 45\u00b0 \u00b1 1\u00b0 (from horizontal)",
   "margin": 1.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 0.0,
   "unit": "mm3",
   "required": "hook 160\u00b0 catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 0.0,
   "unit": "mm",
   "required": "hook 160\u00b0 catch underside on the flange top, clearance = 0",
   "margin": 0.0,
   "at": "(-16.6791, 8.8253, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "J-04",
   "measured": 0.0,
   "unit": "mm3",
   "required": "hook 160\u00b0 undeflected at the engaged pose: interference <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08"
   ]
  },
  {
   "gate": "J-04",
   "measured": 0.0,
   "unit": "mm",
   "required": "hook 160\u00b0 catch underside touches the flange top, clearance = 0",
   "margin": 0.0,
   "at": "(-16.6791, 8.8253, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08"
   ]
  },
  {
   "gate": "J-02",
   "measured": 1.9999999999942453,
   "unit": "mm",
   "required": "hook 160\u00b0 beam thickness >= 1.0",
   "margin": 1.0,
   "at": "(-18.4469, 9.7607, 26.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-01",
   "measured": 0.6708307866589739,
   "unit": "%",
   "required": "hook 160\u00b0 \u03b5 = 1.5\u00b7y\u00b7t/(L\u00b2\u00b7Q) <= 1.5 % (y = 20.37 \u2212 catch R, L = plate top to catch underside)",
   "margin": 0.829169213,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-15"
   ]
  },
  {
   "gate": "J-03",
   "measured": 2.0000000000000018,
   "unit": "ratio",
   "required": "hook 160\u00b0 catch/root thickness ratio reported; binding only if \u03b5 within 0.2 % of 1.5 %",
   "margin": 1.5,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-03",
   "measured": 320.0,
   "unit": "deg",
   "required": "hook 320\u00b0 centred at 320\u00b0 \u00b1 1\u00b0",
   "margin": 1.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 20.87,
   "unit": "mm",
   "required": "hook 320\u00b0 beam inner face R 20.87 \u00b1 0.1 over z 6...26 (min)",
   "margin": 0.1,
   "at": "(14.2641, -15.2346, 6.2500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 20.87,
   "unit": "mm",
   "required": "hook 320\u00b0 beam inner face R 20.87 \u00b1 0.1 over z 6...26 (max)",
   "margin": 0.1,
   "at": "(14.2641, -15.2346, 6.2500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 29.9,
   "unit": "mm",
   "required": "hook 320\u00b0 catch underside z 29.9 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 18.87,
   "unit": "mm",
   "required": "hook 320\u00b0 catch reaches R 18.87 \u00b1 0.1",
   "margin": 0.1,
   "at": "(14.4553, -12.1294, 30.4000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 45.000000000025544,
   "unit": "deg",
   "required": "hook 320\u00b0 catch top chamfer 45\u00b0 \u00b1 1\u00b0 (from horizontal)",
   "margin": 1.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 0.0,
   "unit": "mm3",
   "required": "hook 320\u00b0 catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "REQ-03",
   "measured": 0.0,
   "unit": "mm",
   "required": "hook 320\u00b0 catch underside on the flange top, clearance = 0",
   "margin": 0.0,
   "at": "(15.9825, -10.0319, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08",
    "A-09"
   ]
  },
  {
   "gate": "J-04",
   "measured": 0.0,
   "unit": "mm3",
   "required": "hook 320\u00b0 undeflected at the engaged pose: interference <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08"
   ]
  },
  {
   "gate": "J-04",
   "measured": 0.0,
   "unit": "mm",
   "required": "hook 320\u00b0 catch underside touches the flange top, clearance = 0",
   "margin": 0.0,
   "at": "(15.9825, -10.0319, 29.9000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06",
    "A-08"
   ]
  },
  {
   "gate": "J-02",
   "measured": 1.9999999999977005,
   "unit": "mm",
   "required": "hook 320\u00b0 beam thickness >= 1.0",
   "margin": 1.0,
   "at": "(13.9960, -15.4812, 26.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-01",
   "measured": 0.6708307866601313,
   "unit": "%",
   "required": "hook 320\u00b0 \u03b5 = 1.5\u00b7y\u00b7t/(L\u00b2\u00b7Q) <= 1.5 % (y = 20.37 \u2212 catch R, L = plate top to catch underside)",
   "margin": 0.829169213,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-15"
   ]
  },
  {
   "gate": "J-03",
   "measured": 2.0,
   "unit": "ratio",
   "required": "hook 320\u00b0 catch/root thickness ratio reported; binding only if \u03b5 within 0.2 % of 1.5 %",
   "margin": 1.5,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-04",
   "measured": 48.0,
   "unit": "mm",
   "required": "deck top z 48.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 0.0,
   "unit": "mm2",
   "required": "deck top flat under the OD-H22 flange outline: flange area not on the z 48 plane beyond the slot and slits (mm\u00b2) <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 7.049999999999958,
   "unit": "mm",
   "required": "stem U-slot radial_profile inner about (62, 0), 192\u00b0...348\u00b0 (slit angles aside), z 41...47, min in [7.05, 7.10] (spec 1.2)",
   "margin": -4.1744385725905886e-14,
   "at": "(55.1594, -1.7055, 41.2500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 7.049999999999959,
   "unit": "mm",
   "required": "stem U-slot radial_profile inner, max in [7.05, 7.10] (spec 1.2)",
   "margin": -4.085620730620576e-14,
   "at": "(55.1041, -1.4658, 41.2500) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 7.049999999999997,
   "unit": "mm",
   "required": "slot straight wall +X at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (least)",
   "margin": -2.6645352591003757e-15,
   "at": "(69.0500, 2.5000, 41.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 7.049999999999997,
   "unit": "mm",
   "required": "slot straight wall +X at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (greatest)",
   "margin": -2.6645352591003757e-15,
   "at": "(69.0500, 2.5000, 41.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 7.049999999999997,
   "unit": "mm",
   "required": "slot straight wall -X at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (least)",
   "margin": -2.6645352591003757e-15,
   "at": "(54.9500, 2.5000, 41.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 7.049999999999997,
   "unit": "mm",
   "required": "slot straight wall -X at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (greatest)",
   "margin": -2.6645352591003757e-15,
   "at": "(54.9500, 2.5000, 41.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 14.099999999999994,
   "unit": "mm",
   "required": "stem U-slot 14.1 +0.1/-0 wide (least)",
   "margin": -5.329070518200751e-15,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 0.0,
   "unit": "mm3",
   "required": "slot open through the deck's +Y edge: material in the channel x 62 \u00b1 6.9, y 0 ... 16 <= 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 7.700000000000003,
   "unit": "mm",
   "required": "slot through the deck, length 7.7 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 0,
   "unit": "count",
   "required": "no closed stem bore",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 11.850000000000453,
   "unit": "mm",
   "required": "gusset slit +X reaches 62 \u00b1 (11.85 +0.1/-0) at the deck top",
   "margin": 4.5297099404706387e-13,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 2.4,
   "unit": "mm",
   "required": "gusset slit +X 2.40 \u00b1 0.1 wide (worst)",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 11.850000000000444,
   "unit": "mm",
   "required": "gusset slit -X reaches 62 \u00b1 (11.85 +0.1/-0) at the deck top",
   "margin": 4.440892098500626e-13,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 2.4,
   "unit": "mm",
   "required": "gusset slit -X 2.40 \u00b1 0.1 wide (worst)",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04",
   "measured": 0.5029999999999994,
   "unit": "mm",
   "required": "clearance(mount, OD-H22) away from the flange contact >= 0.5; nearest points in 'at'",
   "margin": 0.003,
   "at": "(55.0529, -1.2000, 43.7660) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-07",
   "measured": 2,
   "unit": "count",
   "required": "the window splits the plate in two (window through over the full Y width)",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04",
    "A-19"
   ]
  },
  {
   "gate": "REQ-07",
   "measured": 40.0,
   "unit": "mm",
   "required": "plate piece -X ends at x 40.0 (window from 40)",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04",
    "A-19"
   ]
  },
  {
   "gate": "REQ-07",
   "measured": 84.0,
   "unit": "mm",
   "required": "plate piece +X starts at x 84.0 (window to 84)",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04",
    "A-19"
   ]
  },
  {
   "gate": "REQ-07",
   "measured": 40.0,
   "unit": "mm",
   "required": "leg inner face at x 40.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04",
    "A-19"
   ]
  },
  {
   "gate": "REQ-07",
   "measured": 84.0,
   "unit": "mm",
   "required": "leg inner face at x 84.0 \u00b1 0.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-04",
    "A-19"
   ]
  },
  {
   "gate": "REQ-08",
   "measured": 48.0,
   "unit": "mm",
   "required": "no material above z 48.1",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-08",
   "measured": 0.0,
   "unit": "mm3",
   "required": "no material within r 12 of the valve axis above the deck top",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-10"
   ]
  },
  {
   "gate": "REQ-09",
   "measured": 24.99999999999948,
   "unit": "deg",
   "required": "drain notch 25\u00b0 at \u03b8 25\u00b0 \u00b1 1\u00b0",
   "margin": 1.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-09",
   "measured": 1.9999999999995606,
   "unit": "mm",
   "required": "drain notch 25\u00b0 2.0 \u00b1 0.1 wide",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-09",
   "measured": 0.5,
   "unit": "mm",
   "required": "drain notch 25\u00b0 0.5 \u00b1 0.1 high at the ring base",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03b",
   "measured": 1.9999999999995606,
   "unit": "mm",
   "required": "drain notch 25\u00b0 ceiling bridge span <= 5",
   "margin": 3.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-16"
   ]
  },
  {
   "gate": "REQ-09",
   "measured": 1,
   "unit": "bool",
   "required": "drain notch 25\u00b0 open through the ring wall (no material r 15...18.2 at mid height)",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-09",
   "measured": 114.99999999999952,
   "unit": "deg",
   "required": "drain notch 115\u00b0 at \u03b8 115\u00b0 \u00b1 1\u00b0",
   "margin": 1.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-09",
   "measured": 1.9999999999995604,
   "unit": "mm",
   "required": "drain notch 115\u00b0 2.0 \u00b1 0.1 wide",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-09",
   "measured": 0.5,
   "unit": "mm",
   "required": "drain notch 115\u00b0 0.5 \u00b1 0.1 high at the ring base",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03b",
   "measured": 1.9999999999995604,
   "unit": "mm",
   "required": "drain notch 115\u00b0 ceiling bridge span <= 5",
   "margin": 3.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-16"
   ]
  },
  {
   "gate": "REQ-09",
   "measured": 1,
   "unit": "bool",
   "required": "drain notch 115\u00b0 open through the ring wall (no material r 15...18.2 at mid height)",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-09",
   "measured": 224.99999999999997,
   "unit": "deg",
   "required": "drain notch 225\u00b0 at \u03b8 225\u00b0 \u00b1 1\u00b0",
   "margin": 1.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-09",
   "measured": 2.0000000000097664,
   "unit": "mm",
   "required": "drain notch 225\u00b0 2.0 \u00b1 0.1 wide",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-09",
   "measured": 0.5,
   "unit": "mm",
   "required": "drain notch 225\u00b0 0.5 \u00b1 0.1 high at the ring base",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03b",
   "measured": 2.0000000000097664,
   "unit": "mm",
   "required": "drain notch 225\u00b0 ceiling bridge span <= 5",
   "margin": 3.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-16"
   ]
  },
  {
   "gate": "REQ-09",
   "measured": 1,
   "unit": "bool",
   "required": "drain notch 225\u00b0 open through the ring wall (no material r 15...18.2 at mid height)",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01a",
   "measured": 1.7223748416156628,
   "unit": "mm",
   "required": "min_wall >= 0.8",
   "margin": 0.922374842,
   "at": "(-16.1007, 2.5198, 10.2555) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01b",
   "measured": 1.7223748416156628,
   "unit": "mm",
   "required": "min_wall >= 1.5",
   "margin": 0.222374842,
   "at": "(-16.1007, 2.5198, 10.2555) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-06a",
   "measured": 1.7223748416156628,
   "unit": "mm",
   "required": "minimum feature >= 1.0",
   "margin": 0.722374842,
   "at": "(-16.1007, 2.5198, 10.2555) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-06",
   "measured": 1.6000000000000014,
   "unit": "mm",
   "required": "Soft: min_wall wide (45\u00b0) >= 1.5",
   "margin": 0.1,
   "at": "(-16.6791, 8.8253, 31.5000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03a",
   "measured": 60.01836063114926,
   "unit": "deg",
   "required": "least overhang >= 45\u00b0 off the named faces (deck underside, 3 catch undersides supported; 2 insert-bore and 3 notch ceilings bridges)",
   "margin": 15.018360631,
   "at": "(-11.8654, -13.5994, 10.0833) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-16"
   ]
  },
  {
   "gate": "D-03a",
   "measured": 0,
   "unit": "count",
   "required": "no flat downward face other than the named ones",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-16"
   ]
  },
  {
   "gate": "D-03b",
   "measured": 4.0,
   "unit": "mm",
   "required": "insert bore ceiling (77.447, 0): bridge span (bore \u00d8) <= 5",
   "margin": 1.0,
   "at": "(77.4470, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-16"
   ]
  },
  {
   "gate": "D-03b",
   "measured": 4.0,
   "unit": "mm",
   "required": "insert bore ceiling (46.662, 0): bridge span (bore \u00d8) <= 5",
   "margin": 1.0,
   "at": "(46.6620, 0.0000, 40.3000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-16"
   ]
  },
  {
   "gate": "D-05a",
   "measured": 16.474808677,
   "unit": "mm",
   "required": "insert pad (77.447, 0): material across the bore >= 8.0 (least of 8 diameters \u00d7 3 depths)",
   "margin": 8.474808677,
   "at": "angle 0.0\u00b0, z 45.80",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "J-05",
   "measured": 3.9218086769999996,
   "unit": "mm",
   "required": "insert bore (77.447, 0): wall >= 3.0 over its depth (16 angles \u00d7 3 depths)",
   "margin": 0.921808677,
   "at": "angle 180.0\u00b0, z 45.80",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-05a",
   "measured": 16.474808677,
   "unit": "mm",
   "required": "insert pad (46.662, 0): material across the bore >= 8.0 (least of 8 diameters \u00d7 3 depths)",
   "margin": 8.474808677,
   "at": "angle 0.0\u00b0, z 45.80",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-13"
   ]
  },
  {
   "gate": "J-05",
   "measured": 3.8128086769999996,
   "unit": "mm",
   "required": "insert bore (46.662, 0): wall >= 3.0 over its depth (16 angles \u00d7 3 depths)",
   "margin": 0.812808677,
   "at": "angle 0.0\u00b0, z 45.80",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 12,
   "unit": "count",
   "required": "bores = 12 (4 footprint, 2 pin, 2 screw clearance, 2 insert, recess, ring inner)",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 1,
   "unit": "count",
   "required": "plate window = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 1,
   "unit": "count",
   "required": "plate window = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 4,
   "unit": "count",
   "required": "\u00d83.4 footprint through-holes = 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 4,
   "unit": "count",
   "required": "\u00d83.4 footprint through-holes = 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 1,
   "unit": "count",
   "required": "pedestal = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 1,
   "unit": "count",
   "required": "pedestal = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 1,
   "unit": "count",
   "required": "pedestal recess = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 1,
   "unit": "count",
   "required": "pedestal recess = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 1,
   "unit": "count",
   "required": "ring wall = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 1,
   "unit": "count",
   "required": "ring wall = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 3,
   "unit": "count",
   "required": "ring drain notches = 3",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 3,
   "unit": "count",
   "required": "ring drain notches = 3",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 2,
   "unit": "count",
   "required": "pin clearance through-holes (\u00d84.8, \u00d83.8) = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 2,
   "unit": "count",
   "required": "pin clearance through-holes (\u00d84.8, \u00d83.8) = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 3,
   "unit": "count",
   "required": "hooks = 3",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 3,
   "unit": "count",
   "required": "hooks = 3",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 3,
   "unit": "count",
   "required": "hooks at the planned angles = 3",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 3,
   "unit": "count",
   "required": "hooks at the planned angles = 3",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 2,
   "unit": "count",
   "required": "legs = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 2,
   "unit": "count",
   "required": "legs = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 1,
   "unit": "count",
   "required": "deck = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 1,
   "unit": "count",
   "required": "deck = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 1,
   "unit": "count",
   "required": "stem U-slot open to +Y (no closed stem bore) = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 1,
   "unit": "count",
   "required": "stem U-slot open to +Y (no closed stem bore) = 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 2,
   "unit": "count",
   "required": "gusset slits = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 2,
   "unit": "count",
   "required": "gusset slits = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 2,
   "unit": "count",
   "required": "\u00d83.4 screw clearance holes = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 2,
   "unit": "count",
   "required": "\u00d83.4 screw clearance holes = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05",
   "measured": 2,
   "unit": "count",
   "required": "\u00d84.0 insert bores = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census",
   "measured": 2,
   "unit": "count",
   "required": "\u00d84.0 insert bores = 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07",
   "measured": 0.05,
   "unit": "rad",
   "required": "angular a <= 4\u00b7acos(1 \u2212 0.01/R_max), R_max 25.88010819142764",
   "margin": 0.061200293,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07",
   "measured": 0.0039588308467848774,
   "unit": "mm",
   "required": "stl_max_sagitta <= 0.01",
   "margin": 0.006041169,
   "at": "(-9.3413, 13.3496, 10.2595) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07",
   "measured": 1,
   "unit": "count",
   "required": "delivered STL: one body",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07",
   "measured": 0,
   "unit": "count",
   "required": "delivered STL: naked edges 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  }
 ],
 "sweep": [
  {
   "parameter": "foot_hole_d",
   "values": [
    [
     "foot_hole_d=3.3"
    ],
    "nominal",
    [
     "foot_hole_d=3.5"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "low: REQ-06 footprint hole (-18, 21) \u00d83.4 \u00b1 0.1 (0 mm)",
    "high: REQ-06 footprint hole (-18, 21) \u00d83.4 \u00b1 0.1 (0 mm)"
   ],
   "worst_margin": 0.0
  },
  {
   "parameter": "ped_top_z",
   "values": [
    [
     "ped_top_z=9.9"
    ],
    "nominal",
    [
     "ped_top_z=10.1"
    ]
   ],
   "all_built": true,
   "new_failures": [
    "low: U-03 contact: OD-H24 rim face on the pedestal top, clearance = 0 = 0.1 mm",
    "low: REQ-02 recess R 14.10 \u00b1 0.1 (radial_profile inner, z 9.5 ... 9.9) max = 14.25 mm",
    "low: REQ-02 recess floor z 9.40 \u00b1 0.05 = 9.3 mm",
    "low: U-05 pedestal recess = 1 = 0 count",
    "low: feature_census pedestal recess = 1 = 0 count",
    "high: U-03 interference mount|OD-H24 <= 0 = 12.3516 mm3",
    "high: U-03 mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 = 0 mm",
    "high: D-04c mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 = 0 mm",
    "high: U-03 (b) OD-H24 lowered along -Z from 25 mm, 9 poses, interference <= 0 (hooks exempt) = 12.3516 mm3",
    "high: REQ-02 pin 2 \u00d83.8: clearance to the OD-H24 pin >= 0.5 = 0 mm",
    "high: D-04d pin 2 \u00d83.8: printed sliding fit >= 0.30 per side = 0 mm",
    "high: REQ-02 recess floor z 9.40 \u00b1 0.05 = 9.5 mm",
    "high: REQ-02 recess to the OD-H24 underside ribs and hub (H24 inside r 13.68) >= 0.5 = 0.4656 mm",
    "high: REQ-01 ring inner R (radial_profile inner 0...359\u00b0, z 10.5...12.5) min in [16.30, 16.40] (spec 1.2) = \u2014 mm",
    "high: REQ-01 ring inner R max in [16.30, 16.40] (spec 1.2) = \u2014 mm"
   ],
   "worst_gate": [
    "low: REQ-02 pin 1 \u00d84.8 length 9.4 \u00b1 0.1 (recess floor to bottom face) (0 mm)",
    "high: REQ-02 pin 1 \u00d84.8 length 9.4 \u00b1 0.1 (recess floor to bottom face) (0 mm)"
   ],
   "worst_margin": 0.0
  },
  {
   "parameter": "ring_ri",
   "values": [
    "nominal",
    "nominal",
    [
     "ring_ri=16.40"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "high: D-01a min_wall >= 0.8 (0.8235 mm)"
   ],
   "worst_margin": 0.823538406
  },
  {
   "parameter": "pin1_d",
   "values": [
    "nominal",
    "nominal",
    [
     "pin1_d=4.9"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [],
   "worst_margin": null
  },
  {
   "parameter": "pin2_d",
   "values": [
    "nominal",
    "nominal",
    [
     "pin2_d=3.9"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [],
   "worst_margin": null
  },
  {
   "parameter": "hook_ri",
   "values": [
    [
     "hook_ri=20.77",
     "catch_reach=1.9"
    ],
    "nominal",
    [
     "hook_ri=20.97",
     "catch_reach=2.1"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "low: REQ-03 hook 70\u00b0 beam inner face R 20.87 \u00b1 0.1 over z 6...26 (min) (0 mm)",
    "high: REQ-03 hook 70\u00b0 beam inner face R 20.87 \u00b1 0.1 over z 6...26 (min) (0 mm)"
   ],
   "worst_margin": 0.0
  },
  {
   "parameter": "hook_t",
   "values": [
    [
     "hook_t=1.9"
    ],
    "nominal",
    [
     "hook_t=2.1"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "low: J-02 hook 70\u00b0 beam thickness >= 1.0 (0.9 mm)",
    "high: J-03 hook 70\u00b0 catch/root thickness ratio reported; binding only if \u03b5 within 0.2 % of 1.5 % (1.4524 ratio)"
   ],
   "worst_margin": 0.9
  },
  {
   "parameter": "catch_under_z",
   "values": [
    [
     "catch_under_z=29.8"
    ],
    "nominal",
    [
     "catch_under_z=30.0"
    ]
   ],
   "all_built": true,
   "new_failures": [
    "low: U-03 interference mount|OD-H24 <= 0 = 1.7888 mm3",
    "low: D-04c hooks to OD-H24 above its flange top plane (z > 29.901) >= 0.5 = 0 mm",
    "low: J-04 hook 70\u00b0 undeflected at the engaged pose: interference <= 0 = 0.5963 mm3",
    "low: J-04 hook 160\u00b0 undeflected at the engaged pose: interference <= 0 = 0.5963 mm3",
    "low: J-04 hook 320\u00b0 undeflected at the engaged pose: interference <= 0 = 0.5963 mm3",
    "high: U-03 contact: hook 70\u00b0 catch underside on the OD-H24 flange top, clearance = 0 = 0.1 mm",
    "high: U-03 contact: hook 160\u00b0 catch underside on the OD-H24 flange top, clearance = 0 = 0.1 mm",
    "high: U-03 contact: hook 320\u00b0 catch underside on the OD-H24 flange top, clearance = 0 = 0.1 mm",
    "high: REQ-03 hook 70\u00b0 catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0 = 0.4126 mm3",
    "high: REQ-03 hook 70\u00b0 catch underside on the flange top, clearance = 0 = 0.1 mm",
    "high: J-04 hook 70\u00b0 catch underside touches the flange top, clearance = 0 = 0.1 mm",
    "high: REQ-03 hook 160\u00b0 catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0 = 0.4126 mm3",
    "high: REQ-03 hook 160\u00b0 catch underside on the flange top, clearance = 0 = 0.1 mm",
    "high: J-04 hook 160\u00b0 catch underside touches the flange top, clearance = 0 = 0.1 mm",
    "high: REQ-03 hook 320\u00b0 catch lands on the flange top outside slots and windows: void under the catch (r 18.87...19.70, 2.65 deep) <= 0 = 0.4126 mm3",
    "high: REQ-03 hook 320\u00b0 catch underside on the flange top, clearance = 0 = 0.1 mm",
    "high: J-04 hook 320\u00b0 catch underside touches the flange top, clearance = 0 = 0.1 mm"
   ],
   "worst_gate": [
    "low: REQ-03 hook 70\u00b0 catch underside z 29.9 \u00b1 0.1 (0 mm)",
    "high: REQ-03 hook 70\u00b0 catch underside z 29.9 \u00b1 0.1 (0 mm)"
   ],
   "worst_margin": 0.0
  },
  {
   "parameter": "catch_ri",
   "values": [
    [
     "catch_reach=1.9"
    ],
    "nominal",
    [
     "catch_reach=2.1"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "low: REQ-03 hook 320\u00b0 catch reaches R 18.87 \u00b1 0.1 (0 mm)",
    "high: REQ-03 hook 70\u00b0 catch reaches R 18.87 \u00b1 0.1 (-0 mm)"
   ],
   "worst_margin": -3.552713678800501e-15
  },
  {
   "parameter": "leg_gap_half",
   "values": [
    [
     "leg_gap_half=21.9"
    ],
    "nominal",
    [
     "leg_gap_half=22.1"
    ]
   ],
   "all_built": true,
   "new_failures": [
    "low: D-03a least overhang >= 45\u00b0 off the named faces (deck underside, 3 catch undersides supported; 2 insert-bore and 3 notch ceilings bridges) = 0 deg",
    "low: D-03a no flat downward face other than the named ones = 2 count"
   ],
   "worst_gate": [
    "low: REQ-07 leg inner face at x 40.0 \u00b1 0.1 (0 mm)",
    "high: REQ-07 leg inner face at x 40.0 \u00b1 0.1 (0 mm)"
   ],
   "worst_margin": 0.0
  },
  {
   "parameter": "deck_top_z",
   "values": [
    [
     "deck_top_z=47.9"
    ],
    "nominal",
    [
     "deck_top_z=48.1"
    ]
   ],
   "all_built": true,
   "new_failures": [
    "low: U-03 contact: OD-H22 flange back face on the deck top, clearance = 0 = 0.1 mm",
    "low: REQ-04 deck top flat under the OD-H22 flange outline: flange area not on the z 48 plane beyond the slot and slits (mm\u00b2) <= 0 = 98.1893 mm2",
    "high: U-03 interference mount|OD-H22 <= 0 = 22.8905 mm3",
    "high: U-03 mount to OD-H22 below its flange back face >= 0.5 = 0 mm",
    "high: D-04c mount to OD-H22 below its flange back face >= 0.5 = 0 mm",
    "high: U-03 (b) OD-H22 slid along -Y at +5 (flange back face z 53.1) from y +45 to 0 (12 poses), then lowered 5 along -Z (7 poses incl. the slide end); interference with the mount <= 0 = 22.8905 mm3",
    "high: REQ-04 deck top flat under the OD-H22 flange outline: flange area not on the z 48 plane beyond the slot and slits (mm\u00b2) <= 0 = 98.9502 mm2",
    "high: REQ-04 clearance(mount, OD-H22) away from the flange contact >= 0.5; nearest points in 'at' = 0 mm"
   ],
   "worst_gate": [
    "low: U-02 size_z 48.0 \u00b1 0.1 (0 mm)",
    "high: U-02 size_z 48.0 \u00b1 0.1 (0 mm)"
   ],
   "worst_margin": 0.0
  },
  {
   "parameter": "deck_t",
   "values": [
    [
     "deck_t=7.6"
    ],
    "nominal",
    [
     "deck_t=7.8"
    ]
   ],
   "all_built": true,
   "new_failures": [
    "high: D-01a min_wall >= 0.8 = 0.1 mm",
    "high: D-01b min_wall >= 1.5 = 0.1 mm",
    "high: D-06a minimum feature >= 1.0 = 0.1 mm",
    "high: U-06 Soft: min_wall wide (45\u00b0) >= 1.5 = 0.1 mm"
   ],
   "worst_gate": [
    "low: D-05a insert pad (77.447, 0): material across the bore >= 8.0 (least of 8 diameters \u00d7 3 depths) (8.3691 mm)",
    "high: REQ-04 slot through the deck, length 7.7 \u00b1 0.1 (0 mm)"
   ],
   "worst_margin": 2.6645352591003757e-15
  },
  {
   "parameter": "slot_w",
   "values": [
    "nominal",
    "nominal",
    [
     "slot_w=14.2"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [],
   "worst_margin": null
  },
  {
   "parameter": "slit_w",
   "values": [
    [
     "slit_w=2.3"
    ],
    "nominal",
    [
     "slit_w=2.5"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "low: REQ-04 gusset slit +X 2.40 \u00b1 0.1 wide (worst) (0 mm)",
    "high: REQ-04 gusset slit +X 2.40 \u00b1 0.1 wide (worst) (0 mm)"
   ],
   "worst_margin": 0.0
  },
  {
   "parameter": "slit_x_top",
   "values": [
    "nominal",
    "nominal",
    [
     "slit_x_top=11.95"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "high: J-05 insert bore (46.662, 0): wall >= 3.0 over its depth (16 angles \u00d7 3 depths) (0.7128 mm)"
   ],
   "worst_margin": 0.712808677
  },
  {
   "parameter": "screw_dx",
   "values": [
    [
     "screw_dx=15.347,-15.438"
    ],
    "nominal",
    [
     "screw_dx=15.547,-15.238"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [],
   "worst_margin": null
  },
  {
   "parameter": "screw_clear_d",
   "values": [
    [
     "screw_clear_d=3.3"
    ],
    "nominal",
    [
     "screw_clear_d=3.5"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "low: REQ-05 screw clearance (77.447, 0) \u00d83.4 \u00b1 0.1 (0 mm)",
    "high: REQ-05 screw clearance (77.447, 0) \u00d83.4 \u00b1 0.1 (0 mm)"
   ],
   "worst_margin": 0.0
  },
  {
   "parameter": "insert_d",
   "values": [
    [
     "insert_d=3.95"
    ],
    "nominal",
    [
     "insert_d=4.05"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "low: REQ-05 insert bore (77.447, 0) \u00d84.0 \u00b1 0.05 (0 mm)",
    "high: D-03b insert bore ceiling (77.447, 0): bridge span (bore \u00d8) <= 5 (0.95 mm)"
   ],
   "worst_margin": 0.0
  },
  {
   "parameter": "recess_r",
   "values": [
    [
     "recess_r=14.0"
    ],
    "nominal",
    [
     "recess_r=14.2"
    ]
   ],
   "all_built": true,
   "new_failures": [
    "low: U-03 mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 = 0.4386 mm",
    "low: D-04c mount (hooks aside) to OD-H24 away from the rim contact >= 0.5 = 0.4386 mm",
    "low: REQ-02 recess to the OD-H24 underside ribs and hub (H24 inside r 13.68) >= 0.5 = 0.4386 mm",
    "high: REQ-02 recess R 14.10 \u00b1 0.1 (radial_profile inner, z 9.5 ... 9.9) max = 14.25 mm",
    "high: U-05 pedestal recess = 1 = 0 count",
    "high: feature_census pedestal recess = 1 = 0 count"
   ],
   "worst_gate": [
    "low: REQ-02 recess R 14.10 \u00b1 0.1 (radial_profile inner, z 9.5 ... 9.9) min (-0 mm)",
    "high: REQ-02 recess R 14.10 \u00b1 0.1 (radial_profile inner, z 9.5 ... 9.9) min (0 mm)"
   ],
   "worst_margin": -1.7763568394002505e-15
  },
  {
   "parameter": "recess_depth",
   "values": [
    [
     "recess_depth=0.55"
    ],
    "nominal",
    [
     "recess_depth=0.65"
    ]
   ],
   "all_built": true,
   "new_failures": [],
   "worst_gate": [
    "low: REQ-02 pin 1 \u00d84.8 length 9.4 \u00b1 0.1 (recess floor to bottom face) (0.05 mm)",
    "high: REQ-02 pin 1 \u00d84.8 length 9.4 \u00b1 0.1 (recess floor to bottom face) (0.05 mm)"
   ],
   "worst_margin": 0.05
  }
 ],
 "u03b_h22_path": [
  {
   "dy": 45.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 13.687873929672799,
   "clearance_at": [
    54.95,
    15.0,
    40.3
   ],
   "clearance_on_b": [
    56.546722,
    26.230109,
    32.638862
   ]
  },
  {
   "dy": 35.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 7.157403651435691,
   "clearance_at": [
    54.95,
    15.0,
    40.3
   ],
   "clearance_on_b": [
    56.500673,
    19.010808,
    34.578352
   ]
  },
  {
   "dy": 25.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 4.455081141359943,
   "clearance_at": [
    54.95,
    15.0,
    40.3
   ],
   "clearance_on_b": [
    58.078294,
    16.82074,
    37.70261
   ]
  },
  {
   "dy": 16.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.9257465027074064,
   "clearance_at": [
    54.95,
    15.0,
    48.0
   ],
   "clearance_on_b": [
    55.539912,
    15.347,
    48.623379
   ]
  },
  {
   "dy": 14.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.8582526360431376,
   "clearance_at": [
    69.05,
    14.653,
    48.0
   ],
   "clearance_on_b": [
    68.460088,
    14.653,
    48.623379
   ]
  },
  {
   "dy": 12.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.8582526360431376,
   "clearance_at": [
    69.05,
    12.653,
    48.0
   ],
   "clearance_on_b": [
    68.460088,
    12.653,
    48.623379
   ]
  },
  {
   "dy": 10.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.8582526360431376,
   "clearance_at": [
    69.05,
    10.653,
    48.0
   ],
   "clearance_on_b": [
    68.460088,
    10.653,
    48.623379
   ]
  },
  {
   "dy": 8.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.8582526360431376,
   "clearance_at": [
    69.05,
    8.653,
    48.0
   ],
   "clearance_on_b": [
    68.460088,
    8.653,
    48.623379
   ]
  },
  {
   "dy": 6.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.8582526360431376,
   "clearance_at": [
    69.05,
    6.653,
    48.0
   ],
   "clearance_on_b": [
    68.460088,
    6.653,
    48.623379
   ]
  },
  {
   "dy": 4.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.8582526360431376,
   "clearance_at": [
    54.95,
    3.347,
    48.0
   ],
   "clearance_on_b": [
    55.539912,
    3.347,
    48.623379
   ]
  },
  {
   "dy": 2.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.8582526360431376,
   "clearance_at": [
    54.95,
    1.347,
    48.0
   ],
   "clearance_on_b": [
    55.539912,
    1.347,
    48.623379
   ]
  },
  {
   "dy": 0.0,
   "dz": 5.0,
   "leg": "slide",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.8781084352947337,
   "clearance_at": [
    55.052878,
    -1.2,
    48.0
   ],
   "clearance_on_b": [
    55.714858,
    -1.085654,
    48.565493
   ]
  },
  {
   "dy": 0.0,
   "dz": 4.0,
   "leg": "drop",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.5029999999999998,
   "clearance_at": [
    68.947122,
    -1.2,
    48.0
   ],
   "clearance_on_b": [
    68.451462,
    -1.114383,
    48.0
   ]
  },
  {
   "dy": 0.0,
   "dz": 3.0,
   "leg": "drop",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.502999999999999,
   "clearance_at": [
    68.947122,
    -1.2,
    48.0
   ],
   "clearance_on_b": [
    68.451462,
    -1.114383,
    48.0
   ]
  },
  {
   "dy": 0.0,
   "dz": 2.0,
   "leg": "drop",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.5029999999999994,
   "clearance_at": [
    68.947122,
    -1.2,
    48.0
   ],
   "clearance_on_b": [
    68.451462,
    -1.114383,
    48.0
   ]
  },
  {
   "dy": 0.0,
   "dz": 1.0,
   "leg": "drop",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.5030000000003505,
   "clearance_at": [
    68.947122,
    -1.2,
    48.0
   ],
   "clearance_on_b": [
    68.451462,
    -1.114383,
    48.0
   ]
  },
  {
   "dy": 0.0,
   "dz": 0.5,
   "leg": "drop",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.5,
   "clearance_at": [
    73.85,
    -1.2,
    48.0
   ],
   "clearance_on_b": [
    73.85,
    -1.2,
    48.5
   ]
  },
  {
   "dy": 0.0,
   "dz": 0.0,
   "leg": "drop",
   "mm3": 0.0,
   "status": "MEASURED",
   "mm3_vs_od_h24": 0.0,
   "clearance_mm": 0.0,
   "clearance_at": [
    69.05,
    1.2,
    48.0
   ],
   "clearance_on_b": [
    69.05,
    1.2,
    48.0
   ]
  }
 ],
 "u03b_slide_least_clearance_mm": {
  "measured": 0.8582526360431376,
  "pose": {
   "dy": 14.0,
   "dz": 5.0
  },
  "at": [
   69.05,
   14.653,
   48.0
  ],
  "on_b": [
   68.460088,
   14.653,
   48.623379
  ]
 },
 "least_sure": [
  "pin clearances at exactly 0.500 on scan-derived pins (A-07, A-01); nominal is now the band's low end",
  "REQ-02 rib clause / D-04c OD-H24 depends on the rib end (note-A r 13.68)",
  "seat parameters and recess_r pass only at nominal (designed contacts / stack-ups); hook 320\u00b0 catch 4.94 mm from the connector (accepted, A-09)"
 ],
 "fix_cycles": {
  "used": 0,
  "cap": 3
 },
 "stopped": false
}
```
