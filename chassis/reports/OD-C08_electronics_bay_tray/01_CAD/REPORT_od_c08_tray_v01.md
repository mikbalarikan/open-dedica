# REPORT — od_c08_tray v01 (20261001-od-c08-electronics-bay-tray)

Designer: Claude Code, claude-opus-5-5 · spec version 1.0 · plan `01_CAD/DESIGN_PLAN.md` · 2026-10-01 UTC

## 1. Files

| File | SHA-256 | Note |
|---|---|---|
| `01_CAD/DESIGN_PLAN.md` | 08cce6b90703d0d0ed6b62e0feddab77f624b354940881f46850d45c7261ae31 |  |
| `01_CAD/probe/probe_inputs.py` | 1aa52c8c0a9d2c75c5df2a47504b58a253a7ec06fdbe6fac8fd9a34a53c38189 |  |
| `01_CAD/probe/probe_inputs.json` | 7fe1a3f885bfaf224d456ae218addcf5cd431ab627e57a5dfa88fd299f8688eb |  |
| `01_CAD/check_od_c08_tray.py` | a6448dff4bdda7042392567aa766acb7a33e0427e6f22c2fa27d28e10ba9fda5 | checks, written before the build (D3) |
| `01_CAD/build_od_c08_tray.py` | c1e8293a571d7dfc6cf36cc61a5d8367bfeb63ba03ba512183d8372ef03a6b80 | parametric build script |
| `01_CAD/sections_od_c08_tray.py` | 8db0c12ea4c8aaa66e9c8391509fc826e1e2f671b60390b15cec2e4d936d717c |  |
| `01_CAD/sweep_od_c08_tray_v01.sh` | 4a86d0f542754ed7147b149028def5cc01254ab0e3ed106bc29677f8cb5245b5 |  |
| `01_CAD/report_od_c08_tray_v01.py` | e6a374301df1727bb44c1cd5121af9893813f981bcae8e40419779ef7418d632 |  |
| `01_CAD/report_text_v01.json` | 9fde474598aabb5de0a01a996c6fcc2c4ef19840b1729f6caf1510ce1332f7c6 |  |
| `01_CAD/build_record_v01.json` | 8d22e681e824e45c355c244679e40590dc5e36d5c09bc1d845139848610fde0a |  |
| `01_CAD/check_od_c08_tray_v01.json` | da444cc036634ea24054fd722d287573ea26bac7d0e6f017f72220c0b620e948 |  |
| `01_CAD/check_od_c08_tray_v01.log` | 333fc5678bcda01ad074ef4e678486a4e7cda77b8c7952f1d08c947f4f5fa6d6 |  |
| `01_CAD/sections_v01.json` | 309152fa51687e8cb051bb8a840f7c0c01f0a2fe984676249b9b753800fa9131 |  |
| `02_STEP_STL/od_c08_tray_C1_v01.step` | 63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91 | AP242, the part, re-imported for every measurement |
| `02_STEP_STL/od_c08_assembly_C1_v01.step` | 21e6f254048e2239216b63e493d764510f7e002180ba0498bf91406c56ecc9aa | AP242 check assembly: tray + OD-E01 at the joint + OD-C01 + OD-C02 |
| `02_STEP_STL/od_c08_tray_C1_v01.stl` | 2ac2db7f63d8ffc91c9d0e3af809a9964152b68826eba5e76eb237d36c22df49 | tolerance 0.01 mm / angular 0.2 rad, 3244 triangles, cached triangulation cleared |
| `03_Sections/od_c08_tray_v01_top_z-100_H1_H2_inserts.png` | 20cbcd2153a170545f1de4f2085ee04e3b7014bfaeeb6ed70174438c2c7cedae | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_top_z-157.5_H5_H6_pins.png` | 6382c2eac986e610923cc35051ee2b58640baec50d25ff3951d3e2055563b390 | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_top_z-222_rear_holes.png` | 9bdd66c0d58ea9762fe1e4f49557f8c4e7078761b89e156a4986682a3673b360 | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_top_z-78_front_holes.png` | cd04361ebe0c1996483b7043af58981a8c864a1503aaf008255c75be176591ba | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_top_z-86.5_gusset.png` | 96fa67317ccca30d1a0196c23823493e18c85d0fd84d54a435bee6583a281294 | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_top_z-168_tie_slot.png` | 35837c7db250dc05aa90c995cabed425ad244eed0d06e129a5ec08649684c060 | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_left_x74.5_wall.png` | 938e82334fc516d77bbabf4ec542c1600bef598486982dafd1b6d79b5b6d742c | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_left_x79.4_standoffs.png` | 8e42662377d3ae8f3ac12a832bac1e4944a42a1492c32e53c12e3290d1b6c9dd | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_left_x83.5_pins.png` | 2ac719bf7346a7ffacd956665fe81b00c016cac25d085ea82be1e73ee9f28bfb | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_front_y2_flange.png` | 69064a409d082daa490977cc3b47c2b14bccdf6013e4c5d54512355dbc93a162 | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_front_y88_slots.png` | 21be331cd7d3f2d1e67a8b8f45753e8a6b858adc35918a35604a78bcc654e14a | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_front_y80_H1_H5.png` | c124b9824d3e7fd860f9dd9a58c29e2c174c23d5d77723deadc398966d72eb65 | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_top_asm_z-100_board_H1_H2.png` | 4659069f7949a636389f7d5b3f2e43ed3004f3a92d609160ba0b25035257f4e5 | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_top_asm_z-157.5_board_pins.png` | 717a12a29c878423261e43a050a429dfd04de8abaef2fb1badb632ea7d5da7cc | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_front_asm_y80_board_H1_H5.png` | 996fd9d4516e9b6391123a22f4c36d3392ce12b469a6dc005aa07e2d8f1e0c7e | section, nothing clipped |
| `03_Sections/od_c08_tray_v01_top_asm_z-222_screw_path.png` | 548f6f5712e012d3781b1a9e2d1c9c83a3667f9cb8e34733469ff405561d3c42 | section, nothing clipped |

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP 7.9.3.1 (OCCT 7.9.3) · tools venv from tools/uv.lock · repo commit 10929db1408d89144bd4af9cad971440427933d0 (working tree clean)

## 3. Gate self-check

Every row of `01_CAD/check_od_c08_tray_v01.json`, measured on the re-imported STEP files. Band: GATES §0 (mm 0.005, mm³ 0.001, deg 0.001, counts 0). Margin is signed, positive inside the limit. The summary per §5 gate ID follows the full table.

| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01.solid_count | 1 count | == 1 | 0 | — | PASS | — |
| U-01.brep_valid | 1 bool | == 1 | 0 | — | PASS | — |
| U-01.naked_edges | 0 count | == 0 | 0 | — | PASS | — |
| exactly_one_solid | 1 count | == 1 | 0 | — | PASS | — |
| U-02.size_x | 39 mm | in [38.9, 39.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size_x | 39 mm | in [38.9, 39.1] | 0.1 | — | PASS | — |
| U-02.size_y | 92 mm | in [91.9, 92.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size_y | 92 mm | in [91.9, 92.1] | 0.1 | — | PASS | — |
| U-02.size_z | 160 mm | in [159.9, 160.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size_z | 160 mm | in [159.9, 160.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_x | 73 mm | in [72.9, 73.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.max_x | 112 mm | in [111.9, 112.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_y | 0 mm | in [-0.1, 0.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.max_y | 92 mm | in [91.9, 92.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_z | -230 mm | in [-230.1, -229.9] | 0.1 | — | PASS | — |
| envelope_within_spec.position.max_z | -70 mm | in [-70.1, -69.9] | 0.1 | — | PASS | — |
| D-02.size_y | 92 mm | <= 220.0 | 128 | — | PASS_ASSUMED | A-09 |
| D-02.size_z | 160 mm | <= 220.0 | 60 | — | PASS_ASSUMED | A-09 |
| D-02.size_x | 39 mm | <= 250.0 | 211 | — | PASS_ASSUMED | A-09 |
| REQ-03.min_x | 73 mm | >= 73.0 | 0 | — | PASS_ASSUMED | A-06 |
| REQ-03.front_z | -70 mm | in [-70.1, -69.9] | 0.1 | — | PASS_ASSUMED | A-06 |
| U-05.plane_faces | 42 count | == 42 | 0 | — | PASS | — |
| feature_census.plane_faces | 42 count | == 42 | 0 | — | PASS | — |
| U-05.cylinder_faces | 12 count | == 12 | 0 | — | PASS | — |
| feature_census.cylinder_faces | 12 count | == 12 | 0 | — | PASS | — |
| U-05.concave_cylinders | 6 count | == 6 | 0 | — | PASS | — |
| feature_census.concave_cylinders | 6 count | == 6 | 0 | — | PASS | — |
| U-05.convex_cylinders | 6 count | == 6 | 0 | — | PASS | — |
| feature_census.convex_cylinders | 6 count | == 6 | 0 | — | PASS | — |
| U-05.cone_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.cone_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.sphere_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.sphere_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.torus_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.torus_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.bspline_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.bspline_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.other_faces | 0 count | == 0 | 0 | — | PASS | — |
| feature_census.other_faces | 0 count | == 0 | 0 | — | PASS | — |
| U-05.bores | 6 count | == 6 | 0 | — | PASS | — |
| feature_census.bores | 6 count | == 6 | 0 | — | PASS | — |
| U-05.bores_x_blind | 2 count | == 2 | 0 | — | PASS | — |
| U-05.bores_y_through | 4 count | == 4 | 0 | — | PASS | — |
| U-05.pins | 2 count | == 2 | 0 | — | PASS | — |
| U-05.standoffs_d10 | 2 count | == 2 | 0 | — | PASS | — |
| U-05.standoffs_d6 | 2 count | == 2 | 0 | — | PASS | — |
| U-05.gussets | 4 count | == 4 | 0 | — | PASS | — |
| E-06.gussets | 4 count | == 4 | 0 | — | PASS | — |
| U-05.slot_faces | 16 count | == 16 | 0 | — | PASS | — |
| U-05.slots | 4 count | == 4 | 0 | — | PASS | — |
| E-11.slots | 4 count | == 4 | 0 | — | PASS_ASSUMED | A-11 |
| REQ-01.x88_z-222.diameter | 3.4 mm | in [3.3, 3.5] | 0.1 | (88.0000, 0.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x88_z-222.offset | 0 mm | <= 0.1 | 0.1 | (88.0000, 0.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x88_z-222.length | 4 mm | in [3.9, 4.1] | 0.1 | (88.0000, 0.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x88_z-222.through | 1 bool | == 1 | 0 | (88.0000, 0.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| D-04a.x88_z-222.diameter | 3.4 mm | >= 3.25 | 0.15 | (88.0000, 0.0000, -222.0000) mm | PASS | — |
| REQ-01.x106_z-222.diameter | 3.4 mm | in [3.3, 3.5] | 0.1 | (106.0000, 0.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x106_z-222.offset | 0 mm | <= 0.1 | 0.1 | (106.0000, 0.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x106_z-222.length | 4 mm | in [3.9, 4.1] | 0.1 | (106.0000, 0.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x106_z-222.through | 1 bool | == 1 | 0 | (106.0000, 0.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| D-04a.x106_z-222.diameter | 3.4 mm | >= 3.25 | 0.15 | (106.0000, 0.0000, -222.0000) mm | PASS | — |
| REQ-01.x88_z-78.diameter | 3.4 mm | in [3.3, 3.5] | 0.1 | (88.0000, 0.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x88_z-78.offset | 0 mm | <= 0.1 | 0.1 | (88.0000, 0.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x88_z-78.length | 4 mm | in [3.9, 4.1] | 0.1 | (88.0000, 0.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x88_z-78.through | 1 bool | == 1 | 0 | (88.0000, 0.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| D-04a.x88_z-78.diameter | 3.4 mm | >= 3.25 | 0.15 | (88.0000, 0.0000, -78.0000) mm | PASS | — |
| REQ-01.x106_z-78.diameter | 3.4 mm | in [3.3, 3.5] | 0.1 | (106.0000, 0.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x106_z-78.offset | 0 mm | <= 0.1 | 0.1 | (106.0000, 0.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x106_z-78.length | 4 mm | in [3.9, 4.1] | 0.1 | (106.0000, 0.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.x106_z-78.through | 1 bool | == 1 | 0 | (106.0000, 0.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| D-04a.x106_z-78.diameter | 3.4 mm | >= 3.25 | 0.15 | (106.0000, 0.0000, -78.0000) mm | PASS | — |
| REQ-01.underside_faces | 1 count | == 1 | 0 | — | PASS_ASSUMED | A-01 |
| REQ-01.underside_y | 0 mm | in [-0.1, 0.1] | 0.1 | (73.0000, 0.0000, -230.0000) mm | PASS_ASSUMED | A-01 |
| REQ-02.seat_faces | 4 count | == 4 | 0 | — | PASS_ASSUMED | A-02, A-03 |
| REQ-02.seat_1.x | 82.438 mm | in [82.39, 82.49] | 0.048 | (82.4380, 78.9800, -160.5200) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.seat_2.x | 82.438 mm | in [82.39, 82.49] | 0.048 | (82.4380, 27.9900, -160.5100) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.seat_3.x | 82.438 mm | in [82.39, 82.49] | 0.048 | (82.4380, 22.9900, -105.0100) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.seat_4.x | 82.438 mm | in [82.39, 82.49] | 0.048 | (82.4380, 75.0000, -105.0000) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.seats_coplanar | 0 mm | <= 0.0 | 0 | — | PASS_ASSUMED | A-02, A-03 |
| REQ-02.insert_y80_z-100.diameter | 4 mm | in [3.95, 4.05] | 0.05 | (76.4380, 80.0000, -100.0000) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.insert_y80_z-100.depth | 6 mm | in [5.9, 6.1] | 0.1 | (76.4380, 80.0000, -100.0000) mm | PASS_ASSUMED | A-02, A-03 |
| D-05b.insert_y80_z-100.diameter | 4 mm | in [3.95, 4.05] | 0.05 | (76.4380, 80.0000, -100.0000) mm | PASS_ASSUMED | A-07 |
| D-05b.insert_y80_z-100.depth | 6 mm | in [5.9, 6.1] | 0.1 | (76.4380, 80.0000, -100.0000) mm | PASS_ASSUMED | A-07 |
| D-05b.insert_y80_z-100.depth_min | 6 mm | >= 5.7 | 0.3 | (76.4380, 80.0000, -100.0000) mm | PASS_ASSUMED | A-07 |
| D-05b.insert_y80_z-100.blind | 0 bool | == 0 | 0 | (76.4380, 80.0000, -100.0000) mm | PASS_ASSUMED | A-07 |
| REQ-02.insert_y80_z-100.offset | 0 mm | <= 0.1 | 0.1 | (76.4380, 80.0000, -100.0000) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.insert_y80_z-100.mouth_x | 82.438 mm | in [82.39, 82.49] | 0.048 | (76.4380, 80.0000, -100.0000) mm | PASS_ASSUMED | A-02, A-03 |
| D-05a.insert_y80_z-100.across_0_180 | 10 mm | >= 8.0 | 2 | [(79.438, 85.0, -100.0), (79.438, 75.0, -100.0)] | PASS_ASSUMED | A-07 |
| D-05a.insert_y80_z-100.across_90_270 | 10 mm | >= 8.0 | 2 | [(79.438, 80.0, -95.0), (79.438, 80.0, -105.0)] | PASS_ASSUMED | A-07 |
| J-05.insert_y80_z-100.ray_0 | 3 mm | >= 3.0 | 0 | (79.4380, 85.0000, -100.0000) mm | PASS | — |
| J-05.insert_y80_z-100.ray_90 | 3 mm | >= 3.0 | 0 | (79.4380, 80.0000, -95.0000) mm | PASS | — |
| J-05.insert_y80_z-100.ray_180 | 3 mm | >= 3.0 | 0 | (79.4380, 75.0000, -100.0000) mm | PASS | — |
| J-05.insert_y80_z-100.ray_270 | 3 mm | >= 3.0 | 0 | (79.4380, 80.0000, -105.0000) mm | PASS | — |
| REQ-02.insert_y27.99_z-100.01.diameter | 4 mm | in [3.95, 4.05] | 0.05 | (76.4380, 27.9900, -100.0100) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.insert_y27.99_z-100.01.depth | 6 mm | in [5.9, 6.1] | 0.1 | (76.4380, 27.9900, -100.0100) mm | PASS_ASSUMED | A-02, A-03 |
| D-05b.insert_y27.99_z-100.01.diameter | 4 mm | in [3.95, 4.05] | 0.05 | (76.4380, 27.9900, -100.0100) mm | PASS_ASSUMED | A-07 |
| D-05b.insert_y27.99_z-100.01.depth | 6 mm | in [5.9, 6.1] | 0.1 | (76.4380, 27.9900, -100.0100) mm | PASS_ASSUMED | A-07 |
| D-05b.insert_y27.99_z-100.01.depth_min | 6 mm | >= 5.7 | 0.3 | (76.4380, 27.9900, -100.0100) mm | PASS_ASSUMED | A-07 |
| D-05b.insert_y27.99_z-100.01.blind | 0 bool | == 0 | 0 | (76.4380, 27.9900, -100.0100) mm | PASS_ASSUMED | A-07 |
| REQ-02.insert_y27.99_z-100.01.offset | 0 mm | <= 0.1 | 0.1 | (76.4380, 27.9900, -100.0100) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.insert_y27.99_z-100.01.mouth_x | 82.438 mm | in [82.39, 82.49] | 0.048 | (76.4380, 27.9900, -100.0100) mm | PASS_ASSUMED | A-02, A-03 |
| D-05a.insert_y27.99_z-100.01.across_0_180 | 10 mm | >= 8.0 | 2 | [(79.438, 32.99, -100.01), (79.438, 22.99, -100.01)] | PASS_ASSUMED | A-07 |
| D-05a.insert_y27.99_z-100.01.across_90_270 | 10 mm | >= 8.0 | 2 | [(79.438, 27.99, -95.01), (79.438, 27.99, -105.01)] | PASS_ASSUMED | A-07 |
| J-05.insert_y27.99_z-100.01.ray_0 | 3 mm | >= 3.0 | 0 | (79.4380, 32.9900, -100.0100) mm | PASS | — |
| J-05.insert_y27.99_z-100.01.ray_90 | 3 mm | >= 3.0 | 0 | (79.4380, 27.9900, -95.0100) mm | PASS | — |
| J-05.insert_y27.99_z-100.01.ray_180 | 3 mm | >= 3.0 | 0 | (79.4380, 22.9900, -100.0100) mm | PASS | — |
| J-05.insert_y27.99_z-100.01.ray_270 | 3 mm | >= 3.0 | 0 | (79.4380, 27.9900, -105.0100) mm | PASS | — |
| REQ-02.pin_y81.98_z-157.52.diameter | 1.8 mm | in [1.75, 1.85] | 0.05 | (82.4380, 81.0800, -158.4200) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.pin_y81.98_z-157.52.length | 2.5 mm | in [2.4, 2.6] | 0.1 | (84.9380, 81.0800, -158.4200) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.pin_y81.98_z-157.52.offset | 0 mm | <= 0.1 | 0.1 | (82.4380, 81.0800, -158.4200) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.pin_y30.99_z-157.51.diameter | 1.8 mm | in [1.75, 1.85] | 0.05 | (82.4380, 30.0900, -158.4100) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.pin_y30.99_z-157.51.length | 2.5 mm | in [2.4, 2.6] | 0.1 | (84.9380, 30.0900, -158.4100) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-02.pin_y30.99_z-157.51.offset | 0 mm | <= 0.1 | 0.1 | (82.4380, 30.0900, -158.4100) mm | PASS_ASSUMED | A-02, A-03 |
| D-01a | 1.8 mm | >= 0.8 | 1 | (82.6880, 31.5190, -158.2381) mm | PASS | — |
| D-06a | 1.8 mm | >= 1.0 | 0.8 | (82.6880, 31.5190, -158.2381) mm | PASS | — |
| D-01b | 2 mm | >= 2.0 | 0 | (75.7500, 92.0000, -113.4783) mm | PASS | — |
| U-06(Soft) | 2 mm | >= 2.0 | 0 | (75.7500, 92.0000, -113.4783) mm | PASS | — |
| D-03a | 90 deg | >= 45.0 | 45 | — | PASS_ASSUMED | A-08 |
| D-03b.flat_ceilings | 0 mm | <= 5.0 | 5 | — | PASS_ASSUMED | A-08 |
| D-03b.horizontal_holes | 3.4 mm | <= 5.0 | 1.6 | — | PASS_ASSUMED | A-08 |
| U-03.plate.clearance | 0 mm | == 0.0 | 0 | (73.0000, 0.0000, -230.0000) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.plate.interference | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.board.interference | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.seat_y27.99_z-100.01.clearance | 0 mm | == 0.0 | 0 | (82.4380, 32.9900, -100.0100) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.seat_y80.00_z-100.00.clearance | 0 mm | == 0.0 | 0 | (82.4380, 80.0010, -102.0250) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.seat_y30.99_z-157.51.clearance | 0 mm | == 0.0 | 0 | (82.4380, 33.9900, -157.5100) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.seat_y81.98_z-157.52.clearance | 0 mm | == 0.0 | 0 | (82.4380, 81.9760, -158.7620) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.pin_y81.98_z-157.52.clearance | 0.3389 mm | >= 0.3 | 0.0389 | (82.4380, 82.8531, -157.7383) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| D-04d.pin_y81.98_z-157.52.clearance | 0.3389 mm | >= 0.3 | 0.0389 | (82.4380, 82.8531, -157.7383) mm | PASS_ASSUMED | A-02 |
| U-03.pin_y30.99_z-157.51.clearance | 0.3278 mm | >= 0.3 | 0.0278 | (82.4380, 30.1850, -157.1075) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| D-04d.pin_y30.99_z-157.51.clearance | 0.3278 mm | >= 0.3 | 0.0278 | (82.4380, 30.1850, -157.1075) mm | PASS_ASSUMED | A-02 |
| U-03.rest.clearance | 6.438 mm | >= 0.5 | 5.938 | (76.0000, 24.0000, -94.8380) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| D-04c.rest.clearance | 6.438 mm | >= 0.5 | 5.938 | (76.0000, 24.0000, -94.8380) mm | PASS_ASSUMED | A-02 |
| E-01.rest.clearance | 6.438 mm | >= 0.5 | 5.938 | (76.0000, 24.0000, -94.8380) mm | PASS_ASSUMED | A-02 |
| U-03.c02.tray_clearance | 2 mm | >= 1.5 | 0.5 | (73.0000, 0.0000, -230.0000) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.c02.board_clearance | 15.438 mm | >= 10.0 | 5.438 | (82.4380, 24.0000, -94.8380) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.board_zone.min_x | 82.438 mm | >= 70.0 | 12.438 | — | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.board_zone.max_x | 109.262 mm | <= 117.0 | 7.738 | — | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.board_zone.min_z | -195.002 mm | >= -240.0 | 44.998 | — | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.board_zone.max_z | -94.838 mm | <= -30.0 | 64.838 | — | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.board_zone.min_y | 24 mm | >= 10.0 | 14 | — | PASS_ASSUMED | A-02, A-03, A-06 |
| U-03.plate_under_x88_z-222.missing_volume | 0 mm3 | <= 0.0 | 0 | (88.0000, -3.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x88_z-222.missing_volume | 0 mm3 | <= 0.0 | 0 | (88.0000, -3.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x88_z-222.hole_gap | 19.4948 mm | >= 6.0 | 13.4948 | (65.0000, -6.0000, -225.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x88_z-222.hole_gap | 19.4948 mm | >= 6.0 | 13.4948 | (65.0000, -6.0000, -225.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x88_z-222.edge_gap | 30.3 mm | >= 8.0 | 22.3 | (120.0000, -3.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x88_z-222.edge_gap | 30.3 mm | >= 8.0 | 22.3 | (120.0000, -3.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x106_z-222.missing_volume | 0 mm3 | <= 0.0 | 0 | (106.0000, -3.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x106_z-222.missing_volume | 0 mm3 | <= 0.0 | 0 | (106.0000, -3.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x106_z-222.hole_gap | 37.4096 mm | >= 6.0 | 31.4096 | (65.0000, -6.0000, -225.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x106_z-222.hole_gap | 37.4096 mm | >= 6.0 | 31.4096 | (65.0000, -6.0000, -225.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x106_z-222.edge_gap | 12.3 mm | >= 8.0 | 4.3 | (120.0000, -3.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x106_z-222.edge_gap | 12.3 mm | >= 8.0 | 4.3 | (120.0000, -3.0000, -222.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x88_z-78.missing_volume | 0 mm3 | <= 0.0 | 0 | (88.0000, -3.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x88_z-78.missing_volume | 0 mm3 | <= 0.0 | 0 | (88.0000, -3.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x88_z-78.hole_gap | 31.7683 mm | >= 6.0 | 25.7683 | (65.0000, -6.0000, -105.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x88_z-78.hole_gap | 31.7683 mm | >= 6.0 | 25.7683 | (65.0000, -6.0000, -105.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x88_z-78.edge_gap | 30.3 mm | >= 8.0 | 22.3 | (120.0000, -3.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x88_z-78.edge_gap | 30.3 mm | >= 8.0 | 22.3 | (120.0000, -3.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x106_z-78.missing_volume | 0 mm3 | <= 0.0 | 0 | (106.0000, -3.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x106_z-78.missing_volume | 0 mm3 | <= 0.0 | 0 | (106.0000, -3.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x106_z-78.hole_gap | 45.3918 mm | >= 6.0 | 39.3918 | (65.0000, -6.0000, -105.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x106_z-78.hole_gap | 45.3918 mm | >= 6.0 | 39.3918 | (65.0000, -6.0000, -105.0000) mm | PASS_ASSUMED | A-01 |
| U-03.plate_under_x106_z-78.edge_gap | 12.3 mm | >= 8.0 | 4.3 | (120.0000, -3.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| REQ-01.plate_under_x106_z-78.edge_gap | 12.3 mm | >= 8.0 | 4.3 | (120.0000, -3.0000, -78.0000) mm | PASS_ASSUMED | A-01 |
| E-05.H1.offset | 0.0032 mm | <= 0.1 | 0.0968 | (76.4380, 80.0000, -100.0000) mm | PASS_ASSUMED | A-02, A-03 |
| E-05.H2.offset | 0.0032 mm | <= 0.1 | 0.0968 | (76.4380, 27.9900, -100.0100) mm | PASS_ASSUMED | A-02, A-03 |
| E-05.H5.offset | 0.0041 mm | <= 0.1 | 0.0959 | (82.4380, 81.9760, -157.5190) mm | PASS_ASSUMED | A-02, A-03 |
| E-05.H6.offset | 0.0022 mm | <= 0.1 | 0.0978 | (82.4380, 30.9920, -157.5110) mm | PASS_ASSUMED | A-02, A-03 |
| REQ-04.x88_z-222.tray | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-03 |
| REQ-04.x88_z-222.board | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-03 |
| REQ-04.x106_z-222.tray | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-03 |
| REQ-04.x106_z-222.board | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-03 |
| REQ-04.x88_z-78.tray | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-03 |
| REQ-04.x88_z-78.board | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-03 |
| REQ-04.x106_z-78.tray | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-03 |
| REQ-04.x106_z-78.board | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-03 |
| REQ-05.box | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-03 |
| E-11.open_plus_x | 0 mm3 | <= 0.0 | 0 | — | PASS_ASSUMED | A-11 |
| U-03(b).interference_max | 0 mm3 | <= 0.0 | 0 | (5.0000, 0.0000, 0.0000) mm | PASS_ASSUMED | A-02, A-03, A-06 |
| U-04.part.solids | 1 count | == 1 | 0 | — | PASS | — |
| U-04.part.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.part.faces_delta | 0 count | == 0 | 0 | — | PASS | — |
| U-04.part.labels | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.part.valid_after | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.solids | 4 count | == 4 | 0 | — | PASS | — |
| U-04.assembly.faces_delta | 0 count | == 0 | 0 | — | PASS | — |
| U-04.assembly.labels | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.valid_after | 1 bool | == 1 | 0 | — | PASS | — |
| U-07.mesh.bodies | 1 count | == 1 | 0 | — | PASS | — |
| U-07.mesh.naked_edges | 0 count | == 0 | 0 | — | PASS | — |
| U-07.mesh.winding | 1 bool | == 1 | 0 | — | PASS | — |
| U-07.tolerance | 0.01 mm | <= 0.01 | 0 | — | PASS | — |
| U-07.angular_tolerance | 0.2 rad | <= 0.25302439550057354 | 0.053 | — | PASS | — |
| U-07.build_sagitta | 0.0049 mm | <= 0.01 | 0.0051 | — | PASS | — |
| U-07.max_sagitta | 0.0049 mm | <= 0.01 | 0.0051 | (77.6095, 78.7963, -104.8479) mm | PASS | — |
| U-08 | —  | N/A | — | — | N/A | — |
| D-07 | —  | N/A | — | — | N/A | — |
| REQ-06(Soft) | —  | bench | — | — | INCONCLUSIVE | A-04, A-12 |

**Summary per §5 gate ID** (worst status of its rows; the row with the least margin):

| §5 gate | Status | Worst row | Measured | Margin | Note |
|---|---|---|---|---|---|
| U-01 | PASS | U-01.solid_count | 1 count | 0 |  |
| U-02 | PASS | U-02.size_x | 39 mm | 0.1 |  |
| U-03 | PASS_ASSUMED | U-03.plate_under_x88_z-78.missing_volume | 0 mm3 | 0 | assembly STEP, parts as placed; plate rows rest on A-01 (no inserts in OD-C01 yet) |
| U-03(b) | PASS_ASSUMED | U-03(b).interference_max | 0 mm3 | 0 | 11 poses, +5.0 to 0 along -X, step 0.5; every boolean completed |
| U-04 | PASS | U-04.part.volume_delta | 0 mm3 | 0 |  |
| U-05 | PASS | U-05.plane_faces | 42 count | 0 | 42 planes, 12 cylinders (6 convex, 6 concave), 6 bores, 2 pins, 4 slots, 4 gussets |
| U-06(Soft) | PASS | U-06(Soft) | 2 mm | 0 | on the solid without the pins; whole part 1.8 (the pins) |
| U-07 | PASS | U-07.mesh.bodies | 1 count | 0 |  |
| U-08 | N/A | U-08 | —  | — | N/A by its row |
| D-01a | PASS | D-01a | 1.8 mm | 1 |  |
| D-01b | PASS | D-01b | 2 mm | 0 | the 2.0 web above the tie slots (y 90 ... 92), exactly at the limit |
| D-02 | PASS_ASSUMED | D-02.size_z | 160 mm | 60 |  |
| D-03a | PASS_ASSUMED | D-03a | 90 deg | 45 | the four flange holes refilled by position; whole part least 0.0 deg, only on the four hole crowns (named exception) |
| D-03b | PASS_ASSUMED | D-03b.horizontal_holes | 3.4 mm | 1.6 | reviewer row; designer's reading only |
| D-04a | PASS | D-04a.x88_z-222.diameter | 3.4 mm | 0.15 |  |
| D-04c | PASS_ASSUMED | D-04c.rest.clearance | 6.438 mm | 5.938 |  |
| D-04d | PASS_ASSUMED | D-04d.pin_y30.99_z-157.51.clearance | 0.3278 mm | 0.0278 |  |
| D-05a | PASS_ASSUMED | D-05a.insert_y80_z-100.across_0_180 | 10 mm | 2 |  |
| D-05b | PASS_ASSUMED | D-05b.insert_y80_z-100.blind | 0 bool | 0 |  |
| D-06a | PASS | D-06a | 1.8 mm | 0.8 |  |
| D-07 | N/A | D-07 | —  | — | N/A by its row |
| J-05 | PASS | J-05.insert_y80_z-100.ray_0 | 3 mm | 0 | the Ø10 boss around the Ø4.0 bore: 3.0 exactly |
| E-01 | PASS_ASSUMED | E-01.rest.clearance | 6.438 mm | 5.938 |  |
| E-05 | PASS_ASSUMED | E-05.H5.offset | 0.0041 mm | 0.0959 |  |
| E-06 | PASS | E-06.gussets | 4 count | 0 | reviewer row; designer's reading: four gussets counted |
| E-11 | PASS_ASSUMED | E-11.slots | 4 count | 0 | reviewer row; designer's reading: four slots, nothing of the tray over the board on +X |
| REQ-01 | PASS_ASSUMED | REQ-01.plate_under_x88_z-78.missing_volume | 0 mm3 | 0 |  |
| REQ-02 | PASS_ASSUMED | REQ-02.seat_faces | 4 count | 0 |  |
| REQ-03 | PASS_ASSUMED | REQ-03.min_x | 73 mm | 0 |  |
| REQ-04 | PASS_ASSUMED | REQ-04.x88_z-222.tray | 0 mm3 | 0 |  |
| REQ-05 | PASS_ASSUMED | REQ-05.box | 0 mm3 | 0 |  |
| REQ-06(Soft) | INCONCLUSIVE | REQ-06(Soft) | —  | — | Soft bench gate, INCONCLUSIVE by its row (A-04, A-12) |
| exactly_one_solid | PASS | exactly_one_solid | 1 count | 0 |  |
| feature_census | PASS | feature_census.plane_faces | 42 count | 0 |  |
| envelope_within_spec | PASS | envelope_within_spec.size_x | 39 mm | 0.1 |  |

Notes on the rows:

- **The four OD-C01 inserts do not exist in the OD-C01 STEP (A-01).** U-03 (a) and REQ-01 are therefore gated on the plate's material under each flange hole: the Ø3.4 footprint through the 6.0 plate lies over solid plate (missing volume 0), its nearest existing plate hole is 19.49 away (≥ 6.0) and its nearest plate edge 12.3 away (≥ 8.0, the two holes at x 106). Every such row reads PASS (assumed: A-01).
- **OD-E01 booleans.** The board is one fused 1233-face solid; every `common_volume` against it completed (5.2 s for tray against board; the 11-pose path in about 100 s), none INCONCLUSIVE. Clearances are gated on `clearance` beside them.
- **Contacts measured apart.** The seat contact is read on the top 1.0 of each standoff (clearance 0 to the board, four rows); the pins are read above the seat plane x 82.438 (0.339 in H5, 0.328 in H6); the rest of the tray, less the four standoff columns (x ≥ 76, radius + 0.5), is 6.438 from the board (the wall face to the solder face). The tray less the pins and the seat layers reads 1.0 (the cut face of the seat layer: the construction's own depth), recorded in the facts, not gated.
- **Nothing of OD-E01 lies on the solder side below the board** (probe: no face at x < 82.40; the solder side is invented flat in the scan, A-05).
- **Named exception (D-03a):** the four Ø3.4 flange holes' crowns are the only downward faces in the print (least 0.0 deg at the hole tops, four faces, `down_faces` in the facts); with them refilled the census reads 90 (nothing downward off the bed).
- `min_wall`, `min_wall_wide` and `overhang_census` ran at spacing 0.7 (brief: the tools refuse the large faces at the default); the largest step used was 0.696 mm.

## 4. Robustness sweep (D7)

Every fit-critical parameter of DESIGN_PLAN §4 at its low and high value, one at a time (there is no motion variable; the assembly path U-03 (b) is run in every sweep run), rebuilt and exported into `01_CAD/sweep_v01/<run>/` and measured by the same check script (`01_CAD/sweep_od_c08_tray_v01.sh`). Nominal is the delivered v01 (§3). Low and high are the spec's tolerance band of each value (REQ-02, D-05b, REQ-01) and, for the standoff positions, the 0.10 offset that REQ-02 and E-05 allow.

| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin | Rows not passing (low / high) |
|---|---|---|---|---|---|
| pin_d | 1.75 · 1.8 · 1.85 | yes | REQ-02.pin_y81.98_z-157.52.diameter | 0 | none / none |
| bore_d | 3.95 · 4.0 · 4.05 | yes | J-05.insert_y80_z-100.ray_0 | -0.025 | none / J-05:FAIL |
| hole_d | 3.3 · 3.4 · 3.5 | yes | REQ-01.x88_z-222.diameter | 0 | none / none |
| seat_x | 82.388 · 82.438 · 82.488 | yes | U-03.board.interference | -8.2944 | U-03:FAIL / U-03(b):FAIL, U-03:FAIL |
| shift_y (standoffs, bores, pins) | -0.1 · 0.0 · 0.1 | yes | U-03.pin_y30.99_z-157.51.clearance | -0.072 | D-04d:FAIL, U-03:FAIL / D-04d:FAIL, U-03:FAIL |
| shift_z (standoffs, bores, pins) | -0.1 · 0.0 · 0.1 | yes | U-03.pin_y30.99_z-157.51.clearance | -0.071 | D-04d:FAIL, U-03:FAIL / D-04d:FAIL, D-05a:INCONCLUSIVE, J-05:INCONCLUSIVE, U-03:FAIL |

Reading of the sweep:

- **pin_d, hole_d, bore_d low:** every gate passes at both ends; the least D-04d gap is 0.303 (H6) at pin Ø1.85.
- **bore_d high (4.05):** J-05 reads 2.975 against 3.0 around both insert bores: the spec fixes the boss at Ø10 and J-05 at 3.0, so the boss wall is exactly at the limit at Ø4.00 and any oversize bore takes it under. Passes only at nominal and below.
- **seat_x ±0.05:** the seat is a designed exact contact on the measured solder face; 0.05 low leaves a 0.05 gap (contact rows FAIL by design), 0.05 high gives 8.29 mm³ of interference with the board. The seat must stay at the measured 82.438; REQ-02's ±0.05 is not a usable build tolerance for a zero-clearance contact.
- **shift_y / shift_z ±0.1:** the pins' gap in H5 and H6 drops to 0.228 … 0.247 (D-04d FAIL) while E-05 still reads ≈ 0.10. D-04d (≥ 0.30 per side) leaves only 0.028 (H6) and 0.039 (H5) of position error, so E-05's 0.10 allowance and D-04d cannot both be used: a spec tension for the orchestrator. In shift_z_high one D-05a and one J-05 ray (H2, 270 deg) read INCONCLUSIVE: the ray toward −Z runs tangent to the H6 standoff's side 57.5 away (y 27.99 = 30.99 − 3.0); the other three rays of that bore read 3.0 / 10.0.

The part therefore passes every gate at nominal; it passes only at nominal for seat_x (by design), for bore_d high (J-05) and for standoff positions off by more than about 0.03 (D-04d).

## 5. Build facts

- Envelope 39 × 92 × 160 mm at x 73 … 112, y 0 … 92, z -230 … -70; volume 70596 mm³; mass 89.7 g at 1270 kg/m³ (A-10); centre of mass (81.18, 30.63, -149.41)
- STL (for the orchestrator's 3MF): 3244 triangles, volume 70594.5 mm³, bounding box [73.0, 0.0, -230.0] … [112.0, 92.0, -70.0] (size [39.0, 92.0, 160.0]), one closed body, sagitta 0.00489 mm
- Fillets: none requested by the spec, none made
- Placement: od_e01_power_pcb: RigidJoint joint_board on the tray (machine frame) -> own_frame; Location: (position=(84, 80, -100), orientation=(0, 90, 0))
- Placement: od_c01_frame: RigidJoint joint_plate on the tray (machine frame) -> own_frame; Location: (position=(0, 0, 0), orientation=(0, 0, 0))
- Placement: od_c02_bulkhead: RigidJoint joint_c02 on the tray (machine frame) -> own_frame; Location: (position=(0, 0, 0), orientation=(0, 0, 0))

- Seat x: taken from the measured solder face of the placed OD-E01 (82.438), not the rounded 82.44 of the spec (DESIGN_PLAN §1, §4).
- Board joint confirmed on the placed solid (probe): H1 at (y 80.001, z −100.003), H2 (27.991, −100.013), H5 (81.976, −157.519), H6 (30.992, −157.511), Ø4.044 / 4.012 / 2.486 / 2.460.
- Tray to OD-C02: 2.0 (x 73 against the base rail's x 71); OD-E01 to OD-C02: 15.438 (solder face to the electric face x 67).
- Gussets: four, hypotenuse faces counted at z −230 … −227, −212 … −209, −88 … −85, −73 … −70.

## 6. Plausibility (§P, D6)

| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |
|---|---|---|
| P1 | Gravity: does it stand and hold as installed? | The flange lies on the plate top (measured contact 0) and is screwed at four corners; the wall rises from the flange's −X edge, tied by four gussets; the 0.1 kg board hangs on four standoffs off the wall, two of them screwed. In the print it lies flat on the wall's outer face with everything rising from it. |
| P2 | Function chains: does each function have a complete path? | Plate insert → M3 × 8 through the Ø3.4 flange hole (driver path clear to y 120); board → seat → screws in the Ø4.0 insert bores, pins in H5 / H6; wires → tie slots above the board's top edge. The plate inserts themselves do not exist yet (A-01). |
| P3 | Motion clearance: is every motion path clear? | The board's mounting path (along −X onto the pins, from +5.0) was measured in 11 poses with interference 0; the pins enter H5 / H6 with 0.33 per side; the driver cylinders on the four screw axes meet nothing. |
| P4 | Human factors: can a person assemble and service it? | Screws reached from above with the top panel off and the board mounted (REQ-04); faston tabs open on +X (REQ-05 box empty); the board slides on along −X over the two pins, then two screws. |
| P5 | Absurdity next to a real product? | A 3 mm PETG wall with 6.4 mm standoffs and a 4 mm screwed flange is the usual PCB-on-edge bracket; 90 g of PETG; nothing oversized or flimsy apart from the Ø1.8 pins, which only locate. |
| P6 | Nothing floating, embedded, mirrored or upside-down? | One solid; standoffs grow from the wall face x 76; components face +X toward the side panel and the solder side faces the bulkhead, as §1 asks; the board sits on the seats, not in them (interference 0); the flange's underside is on the plate (y 0). |

Sections (`01_CAD/sections_v01.json`): `od_c08_tray_v01_top_z-100_H1_H2_inserts.png` nothing_clipped 0; `od_c08_tray_v01_top_z-157.5_H5_H6_pins.png` nothing_clipped 0; `od_c08_tray_v01_top_z-222_rear_holes.png` nothing_clipped 0; `od_c08_tray_v01_top_z-78_front_holes.png` nothing_clipped 0; `od_c08_tray_v01_top_z-86.5_gusset.png` nothing_clipped 0; `od_c08_tray_v01_top_z-168_tie_slot.png` nothing_clipped 0; `od_c08_tray_v01_left_x74.5_wall.png` nothing_clipped 0; `od_c08_tray_v01_left_x79.4_standoffs.png` nothing_clipped 0; `od_c08_tray_v01_left_x83.5_pins.png` nothing_clipped 0; `od_c08_tray_v01_front_y2_flange.png` nothing_clipped 0; `od_c08_tray_v01_front_y88_slots.png` nothing_clipped 0; `od_c08_tray_v01_front_y80_H1_H5.png` nothing_clipped 0; `od_c08_tray_v01_top_asm_z-100_board_H1_H2.png` nothing_clipped 0; `od_c08_tray_v01_top_asm_z-157.5_board_pins.png` nothing_clipped 0; `od_c08_tray_v01_front_asm_y80_board_H1_H5.png` nothing_clipped 0; `od_c08_tray_v01_top_asm_z-222_screw_path.png` nothing_clipped 0

## 7. Library and tools used

- Card read: UNO10 U5 tank heat-set (the boss and blind-bore pattern; how big and where kept apart in the envelope rows).
- `tools.core`: `write_step` (AP242, part and assembly), `write_stl`, `read_step`, `validity`, `compare_step`, `common_volume`.
- `tools.measure`: `envelope`, `feature_census`, `bore_census`, `locate_bore`, `min_wall`, `min_wall_wide`, `overhang_census`, `flat_ceiling_spans`, `clearance`, `radial_extent`, `mass_properties`, `mesh_census`; `tools.measure.features.cylinder` for the pins' axes (convex, not in `bore_census`).
- `tools.drawing.write_sections` with `nothing_clipped`.
- New job code (in `01_CAD/` only): region solids cut from the re-imported STEP (pins, seat layers, standoff columns), the driver cylinders and the faston box, the U-03 (b) path loop, the plate-material probe under the flange holes, the report writer.
- No `tools/measure` function was missing for a gated row.
- Tool finding (not a gate value): `min_wall`'s `detail["solids"]` reads 4 on a one-solid part; in `tools/measure/wall.py` the name `found` (the solids) is reused for a ray's exit tuple of four values before the detail is written. The measured wall is unaffected.

## 8. Deviations from the plan

None in the geometry. One change to the check script after a dry run in the scratchpad and before the v01 export: the `radial_extent` rays of D-05a / J-05 had `r_min` just outside the bore, which the tool refuses as a stretch crossing the window (INCONCLUSIVE); `r_min` was removed (the window is 0 … 6.0, the bore is air). The build record, the sections script and the report writer are added beside the plan's files.

## 9. What I am least sure of

1. D-04d against E-05: the pins keep 0.339 (H5) and 0.328 (H6) per side only because they sit within 0.004 of the scanned hole axes; the sweep shows that the 0.10 position allowance of REQ-02 / E-05 takes D-04d to 0.23. The holes are scan values (A-02, no calipers), so the real margin may be smaller than measured.
2. The seat at x 82.438 is an exact contact on a scanned, invented-flat solder face (A-05): the heatsink's solder-side screw heads (X-35, X-36) are not in the model, so nothing on the solder side could be checked against the standoffs; and the seat contact rows FAIL for any seat other than the measured face.
3. Two walls sit exactly at their limits as the spec dimensions them: the 2.0 web above the tie slots (D-01b, margin 0) and the 3.0 boss wall around each Ø4.0 insert bore (J-05, margin 0; 2.975 at a Ø4.05 bore).

## 10. Stop

Not stopped.

```json
{
 "schema": "oguz-report-v1",
 "job_id": "20261001-od-c08-electronics-bay-tray",
 "part": "od_c08_tray",
 "tag": "v01",
 "spec_version": "1.0",
 "files": [
  {
   "path": "01_CAD/DESIGN_PLAN.md",
   "sha256": "08cce6b90703d0d0ed6b62e0feddab77f624b354940881f46850d45c7261ae31"
  },
  {
   "path": "01_CAD/probe/probe_inputs.py",
   "sha256": "1aa52c8c0a9d2c75c5df2a47504b58a253a7ec06fdbe6fac8fd9a34a53c38189"
  },
  {
   "path": "01_CAD/probe/probe_inputs.json",
   "sha256": "7fe1a3f885bfaf224d456ae218addcf5cd431ab627e57a5dfa88fd299f8688eb"
  },
  {
   "path": "01_CAD/check_od_c08_tray.py",
   "sha256": "a6448dff4bdda7042392567aa766acb7a33e0427e6f22c2fa27d28e10ba9fda5"
  },
  {
   "path": "01_CAD/build_od_c08_tray.py",
   "sha256": "c1e8293a571d7dfc6cf36cc61a5d8367bfeb63ba03ba512183d8372ef03a6b80"
  },
  {
   "path": "01_CAD/sections_od_c08_tray.py",
   "sha256": "8db0c12ea4c8aaa66e9c8391509fc826e1e2f671b60390b15cec2e4d936d717c"
  },
  {
   "path": "01_CAD/sweep_od_c08_tray_v01.sh",
   "sha256": "4a86d0f542754ed7147b149028def5cc01254ab0e3ed106bc29677f8cb5245b5"
  },
  {
   "path": "01_CAD/report_od_c08_tray_v01.py",
   "sha256": "e6a374301df1727bb44c1cd5121af9893813f981bcae8e40419779ef7418d632"
  },
  {
   "path": "01_CAD/report_text_v01.json",
   "sha256": "9fde474598aabb5de0a01a996c6fcc2c4ef19840b1729f6caf1510ce1332f7c6"
  },
  {
   "path": "01_CAD/build_record_v01.json",
   "sha256": "8d22e681e824e45c355c244679e40590dc5e36d5c09bc1d845139848610fde0a"
  },
  {
   "path": "01_CAD/check_od_c08_tray_v01.json",
   "sha256": "da444cc036634ea24054fd722d287573ea26bac7d0e6f017f72220c0b620e948"
  },
  {
   "path": "01_CAD/check_od_c08_tray_v01.log",
   "sha256": "333fc5678bcda01ad074ef4e678486a4e7cda77b8c7952f1d08c947f4f5fa6d6"
  },
  {
   "path": "01_CAD/sections_v01.json",
   "sha256": "309152fa51687e8cb051bb8a840f7c0c01f0a2fe984676249b9b753800fa9131"
  },
  {
   "path": "02_STEP_STL/od_c08_tray_C1_v01.step",
   "sha256": "63686c46a32753fdd8bcd669a9a89bcb5ffc853a0c15f7777048caca446cda91"
  },
  {
   "path": "02_STEP_STL/od_c08_assembly_C1_v01.step",
   "sha256": "21e6f254048e2239216b63e493d764510f7e002180ba0498bf91406c56ecc9aa"
  },
  {
   "path": "02_STEP_STL/od_c08_tray_C1_v01.stl",
   "sha256": "2ac2db7f63d8ffc91c9d0e3af809a9964152b68826eba5e76eb237d36c22df49"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_top_z-100_H1_H2_inserts.png",
   "sha256": "20cbcd2153a170545f1de4f2085ee04e3b7014bfaeeb6ed70174438c2c7cedae"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_top_z-157.5_H5_H6_pins.png",
   "sha256": "6382c2eac986e610923cc35051ee2b58640baec50d25ff3951d3e2055563b390"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_top_z-222_rear_holes.png",
   "sha256": "9bdd66c0d58ea9762fe1e4f49557f8c4e7078761b89e156a4986682a3673b360"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_top_z-78_front_holes.png",
   "sha256": "cd04361ebe0c1996483b7043af58981a8c864a1503aaf008255c75be176591ba"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_top_z-86.5_gusset.png",
   "sha256": "96fa67317ccca30d1a0196c23823493e18c85d0fd84d54a435bee6583a281294"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_top_z-168_tie_slot.png",
   "sha256": "35837c7db250dc05aa90c995cabed425ad244eed0d06e129a5ec08649684c060"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_left_x74.5_wall.png",
   "sha256": "938e82334fc516d77bbabf4ec542c1600bef598486982dafd1b6d79b5b6d742c"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_left_x79.4_standoffs.png",
   "sha256": "8e42662377d3ae8f3ac12a832bac1e4944a42a1492c32e53c12e3290d1b6c9dd"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_left_x83.5_pins.png",
   "sha256": "2ac719bf7346a7ffacd956665fe81b00c016cac25d085ea82be1e73ee9f28bfb"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_front_y2_flange.png",
   "sha256": "69064a409d082daa490977cc3b47c2b14bccdf6013e4c5d54512355dbc93a162"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_front_y88_slots.png",
   "sha256": "21be331cd7d3f2d1e67a8b8f45753e8a6b858adc35918a35604a78bcc654e14a"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_front_y80_H1_H5.png",
   "sha256": "c124b9824d3e7fd860f9dd9a58c29e2c174c23d5d77723deadc398966d72eb65"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_top_asm_z-100_board_H1_H2.png",
   "sha256": "4659069f7949a636389f7d5b3f2e43ed3004f3a92d609160ba0b25035257f4e5"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_top_asm_z-157.5_board_pins.png",
   "sha256": "717a12a29c878423261e43a050a429dfd04de8abaef2fb1badb632ea7d5da7cc"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_front_asm_y80_board_H1_H5.png",
   "sha256": "996fd9d4516e9b6391123a22f4c36d3392ce12b469a6dc005aa07e2d8f1e0c7e"
  },
  {
   "path": "03_Sections/od_c08_tray_v01_top_asm_z-222_screw_path.png",
   "sha256": "548f6f5712e012d3781b1a9e2d1c9c83a3667f9cb8e34733469ff405561d3c42"
  }
 ],
 "versions": {
  "python": "3.13.7",
  "build123d": "0.11.1",
  "ocp": "7.9.3.1",
  "repo_commit": "10929db1408d89144bd4af9cad971440427933d0"
 },
 "gates": [
  {
   "gate": "U-01.solid_count",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01.brep_valid",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-01.naked_edges",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
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
   "gate": "U-02.size_x",
   "measured": 39.0,
   "unit": "mm",
   "required": "in [38.9, 39.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size_x",
   "measured": 39.0,
   "unit": "mm",
   "required": "in [38.9, 39.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02.size_y",
   "measured": 92.0,
   "unit": "mm",
   "required": "in [91.9, 92.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size_y",
   "measured": 92.0,
   "unit": "mm",
   "required": "in [91.9, 92.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-02.size_z",
   "measured": 160.0,
   "unit": "mm",
   "required": "in [159.9, 160.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.size_z",
   "measured": 160.0,
   "unit": "mm",
   "required": "in [159.9, 160.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.min_x",
   "measured": 73.0,
   "unit": "mm",
   "required": "in [72.9, 73.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.max_x",
   "measured": 112.0,
   "unit": "mm",
   "required": "in [111.9, 112.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.min_y",
   "measured": 0.0,
   "unit": "mm",
   "required": "in [-0.1, 0.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.max_y",
   "measured": 92.0,
   "unit": "mm",
   "required": "in [91.9, 92.1]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.min_z",
   "measured": -230.0,
   "unit": "mm",
   "required": "in [-230.1, -229.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "envelope_within_spec.position.max_z",
   "measured": -70.0,
   "unit": "mm",
   "required": "in [-70.1, -69.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-02.size_y",
   "measured": 92.0,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 128.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "D-02.size_z",
   "measured": 160.0,
   "unit": "mm",
   "required": "<= 220.0",
   "margin": 60.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "D-02.size_x",
   "measured": 39.0,
   "unit": "mm",
   "required": "<= 250.0",
   "margin": 211.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-09"
   ]
  },
  {
   "gate": "REQ-03.min_x",
   "measured": 73.0,
   "unit": "mm",
   "required": ">= 73.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "REQ-03.front_z",
   "measured": -70.0,
   "unit": "mm",
   "required": "in [-70.1, -69.9]",
   "margin": 0.1,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-06"
   ]
  },
  {
   "gate": "U-05.plane_faces",
   "measured": 42,
   "unit": "count",
   "required": "== 42",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.plane_faces",
   "measured": 42,
   "unit": "count",
   "required": "== 42",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.cylinder_faces",
   "measured": 12,
   "unit": "count",
   "required": "== 12",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.cylinder_faces",
   "measured": 12,
   "unit": "count",
   "required": "== 12",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.concave_cylinders",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.concave_cylinders",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.convex_cylinders",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.convex_cylinders",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.cone_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.cone_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.sphere_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.sphere_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.torus_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.torus_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bspline_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.bspline_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.other_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.other_faces",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bores",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "feature_census.bores",
   "measured": 6,
   "unit": "count",
   "required": "== 6",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bores_x_blind",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.bores_y_through",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.pins",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.standoffs_d10",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.standoffs_d6",
   "measured": 2,
   "unit": "count",
   "required": "== 2",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.gussets",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "E-06.gussets",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.slot_faces",
   "measured": 16,
   "unit": "count",
   "required": "== 16",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-05.slots",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "E-11.slots",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-11"
   ]
  },
  {
   "gate": "REQ-01.x88_z-222.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(88.0000, 0.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x88_z-222.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(88.0000, 0.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x88_z-222.length",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(88.0000, 0.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x88_z-222.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(88.0000, 0.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "D-04a.x88_z-222.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(88.0000, 0.0000, -222.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.x106_z-222.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(106.0000, 0.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x106_z-222.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(106.0000, 0.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x106_z-222.length",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(106.0000, 0.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x106_z-222.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(106.0000, 0.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "D-04a.x106_z-222.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(106.0000, 0.0000, -222.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.x88_z-78.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(88.0000, 0.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x88_z-78.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(88.0000, 0.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x88_z-78.length",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(88.0000, 0.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x88_z-78.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(88.0000, 0.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "D-04a.x88_z-78.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(88.0000, 0.0000, -78.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.x106_z-78.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": "in [3.3, 3.5]",
   "margin": 0.1,
   "at": "(106.0000, 0.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x106_z-78.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(106.0000, 0.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x106_z-78.length",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.9, 4.1]",
   "margin": 0.1,
   "at": "(106.0000, 0.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.x106_z-78.through",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": "(106.0000, 0.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "D-04a.x106_z-78.diameter",
   "measured": 3.4,
   "unit": "mm",
   "required": ">= 3.25",
   "margin": 0.15,
   "at": "(106.0000, 0.0000, -78.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-01.underside_faces",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.underside_y",
   "measured": -0.0,
   "unit": "mm",
   "required": "in [-0.1, 0.1]",
   "margin": 0.1,
   "at": "(73.0000, 0.0000, -230.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-02.seat_faces",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.seat_1.x",
   "measured": 82.438,
   "unit": "mm",
   "required": "in [82.39, 82.49]",
   "margin": 0.048,
   "at": "(82.4380, 78.9800, -160.5200) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.seat_2.x",
   "measured": 82.438,
   "unit": "mm",
   "required": "in [82.39, 82.49]",
   "margin": 0.048,
   "at": "(82.4380, 27.9900, -160.5100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.seat_3.x",
   "measured": 82.438,
   "unit": "mm",
   "required": "in [82.39, 82.49]",
   "margin": 0.048,
   "at": "(82.4380, 22.9900, -105.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.seat_4.x",
   "measured": 82.438,
   "unit": "mm",
   "required": "in [82.39, 82.49]",
   "margin": 0.048,
   "at": "(82.4380, 75.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.seats_coplanar",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.insert_y80_z-100.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(76.4380, 80.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.insert_y80_z-100.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(76.4380, 80.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "D-05b.insert_y80_z-100.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(76.4380, 80.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-05b.insert_y80_z-100.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(76.4380, 80.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-05b.insert_y80_z-100.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(76.4380, 80.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-05b.insert_y80_z-100.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(76.4380, 80.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02.insert_y80_z-100.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(76.4380, 80.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.insert_y80_z-100.mouth_x",
   "measured": 82.438,
   "unit": "mm",
   "required": "in [82.39, 82.49]",
   "margin": 0.048,
   "at": "(76.4380, 80.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "D-05a.insert_y80_z-100.across_0_180",
   "measured": 10.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 2.0,
   "at": "[(79.438, 85.0, -100.0), (79.438, 75.0, -100.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-05a.insert_y80_z-100.across_90_270",
   "measured": 10.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 2.0,
   "at": "[(79.438, 80.0, -95.0), (79.438, 80.0, -105.0)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "J-05.insert_y80_z-100.ray_0",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.0,
   "at": "(79.4380, 85.0000, -100.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.insert_y80_z-100.ray_90",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.0,
   "at": "(79.4380, 80.0000, -95.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.insert_y80_z-100.ray_180",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.0,
   "at": "(79.4380, 75.0000, -100.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.insert_y80_z-100.ray_270",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.0,
   "at": "(79.4380, 80.0000, -105.0000) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-02.insert_y27.99_z-100.01.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(76.4380, 27.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.insert_y27.99_z-100.01.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(76.4380, 27.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "D-05b.insert_y27.99_z-100.01.diameter",
   "measured": 4.0,
   "unit": "mm",
   "required": "in [3.95, 4.05]",
   "margin": 0.05,
   "at": "(76.4380, 27.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-05b.insert_y27.99_z-100.01.depth",
   "measured": 6.0,
   "unit": "mm",
   "required": "in [5.9, 6.1]",
   "margin": 0.1,
   "at": "(76.4380, 27.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-05b.insert_y27.99_z-100.01.depth_min",
   "measured": 6.0,
   "unit": "mm",
   "required": ">= 5.7",
   "margin": 0.3,
   "at": "(76.4380, 27.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-05b.insert_y27.99_z-100.01.blind",
   "measured": 0,
   "unit": "bool",
   "required": "== 0",
   "margin": 0.0,
   "at": "(76.4380, 27.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "REQ-02.insert_y27.99_z-100.01.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(76.4380, 27.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.insert_y27.99_z-100.01.mouth_x",
   "measured": 82.438,
   "unit": "mm",
   "required": "in [82.39, 82.49]",
   "margin": 0.048,
   "at": "(76.4380, 27.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "D-05a.insert_y27.99_z-100.01.across_0_180",
   "measured": 10.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 2.0,
   "at": "[(79.438, 32.99, -100.01), (79.438, 22.99, -100.01)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "D-05a.insert_y27.99_z-100.01.across_90_270",
   "measured": 10.0,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 2.0,
   "at": "[(79.438, 27.99, -95.01), (79.438, 27.99, -105.01)]",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-07"
   ]
  },
  {
   "gate": "J-05.insert_y27.99_z-100.01.ray_0",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.0,
   "at": "(79.4380, 32.9900, -100.0100) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.insert_y27.99_z-100.01.ray_90",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.0,
   "at": "(79.4380, 27.9900, -95.0100) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.insert_y27.99_z-100.01.ray_180",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.0,
   "at": "(79.4380, 22.9900, -100.0100) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "J-05.insert_y27.99_z-100.01.ray_270",
   "measured": 3.0,
   "unit": "mm",
   "required": ">= 3.0",
   "margin": 0.0,
   "at": "(79.4380, 27.9900, -105.0100) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "REQ-02.pin_y81.98_z-157.52.diameter",
   "measured": 1.8,
   "unit": "mm",
   "required": "in [1.75, 1.85]",
   "margin": 0.05,
   "at": "(82.4380, 81.0800, -158.4200) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.pin_y81.98_z-157.52.length",
   "measured": 2.5,
   "unit": "mm",
   "required": "in [2.4, 2.6]",
   "margin": 0.1,
   "at": "(84.9380, 81.0800, -158.4200) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.pin_y81.98_z-157.52.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(82.4380, 81.0800, -158.4200) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.pin_y30.99_z-157.51.diameter",
   "measured": 1.8,
   "unit": "mm",
   "required": "in [1.75, 1.85]",
   "margin": 0.05,
   "at": "(82.4380, 30.0900, -158.4100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.pin_y30.99_z-157.51.length",
   "measured": 2.5,
   "unit": "mm",
   "required": "in [2.4, 2.6]",
   "margin": 0.1,
   "at": "(84.9380, 30.0900, -158.4100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-02.pin_y30.99_z-157.51.offset",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.1,
   "at": "(82.4380, 30.0900, -158.4100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "D-01a",
   "measured": 1.7999999999982679,
   "unit": "mm",
   "required": ">= 0.8",
   "margin": 1.0,
   "at": "(82.6880, 31.5190, -158.2381) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-06a",
   "measured": 1.7999999999982679,
   "unit": "mm",
   "required": ">= 1.0",
   "margin": 0.8,
   "at": "(82.6880, 31.5190, -158.2381) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-01b",
   "measured": 1.999999999999997,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": -3.1086244689504383e-15,
   "at": "(75.7500, 92.0000, -113.4783) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-06(Soft)",
   "measured": 1.999999999999997,
   "unit": "mm",
   "required": ">= 2.0",
   "margin": -3.1086244689504383e-15,
   "at": "(75.7500, 92.0000, -113.4783) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "D-03a",
   "measured": 90.0,
   "unit": "deg",
   "required": ">= 45.0",
   "margin": 45.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ]
  },
  {
   "gate": "D-03b.flat_ceilings",
   "measured": 0.0,
   "unit": "mm",
   "required": "<= 5.0",
   "margin": 5.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ]
  },
  {
   "gate": "D-03b.horizontal_holes",
   "measured": 3.4,
   "unit": "mm",
   "required": "<= 5.0",
   "margin": 1.6,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-08"
   ]
  },
  {
   "gate": "U-03.plate.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(73.0000, 0.0000, -230.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.plate.interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.board.interference",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.seat_y27.99_z-100.01.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(82.4380, 32.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.seat_y80.00_z-100.00.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(82.4380, 80.0010, -102.0250) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.seat_y30.99_z-157.51.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(82.4380, 33.9900, -157.5100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.seat_y81.98_z-157.52.clearance",
   "measured": 0.0,
   "unit": "mm",
   "required": "== 0.0",
   "margin": 0.0,
   "at": "(82.4380, 81.9760, -158.7620) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.pin_y81.98_z-157.52.clearance",
   "measured": 0.3388768943743703,
   "unit": "mm",
   "required": ">= 0.3",
   "margin": 0.038876894,
   "at": "(82.4380, 82.8531, -157.7383) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "D-04d.pin_y81.98_z-157.52.clearance",
   "measured": 0.3388768943743703,
   "unit": "mm",
   "required": ">= 0.3",
   "margin": 0.038876894,
   "at": "(82.4380, 82.8531, -157.7383) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "U-03.pin_y30.99_z-157.51.clearance",
   "measured": 0.3277639320224975,
   "unit": "mm",
   "required": ">= 0.3",
   "margin": 0.027763932,
   "at": "(82.4380, 30.1850, -157.1075) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "D-04d.pin_y30.99_z-157.51.clearance",
   "measured": 0.3277639320224975,
   "unit": "mm",
   "required": ">= 0.3",
   "margin": 0.027763932,
   "at": "(82.4380, 30.1850, -157.1075) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "U-03.rest.clearance",
   "measured": 6.438000000000002,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 5.938,
   "at": "(76.0000, 24.0000, -94.8380) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "D-04c.rest.clearance",
   "measured": 6.438000000000002,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 5.938,
   "at": "(76.0000, 24.0000, -94.8380) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "E-01.rest.clearance",
   "measured": 6.438000000000002,
   "unit": "mm",
   "required": ">= 0.5",
   "margin": 5.938,
   "at": "(76.0000, 24.0000, -94.8380) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02"
   ]
  },
  {
   "gate": "U-03.c02.tray_clearance",
   "measured": 2.0,
   "unit": "mm",
   "required": ">= 1.5",
   "margin": 0.5,
   "at": "(73.0000, 0.0000, -230.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.c02.board_clearance",
   "measured": 15.438000000000002,
   "unit": "mm",
   "required": ">= 10.0",
   "margin": 5.438,
   "at": "(82.4380, 24.0000, -94.8380) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.board_zone.min_x",
   "measured": 82.438,
   "unit": "mm",
   "required": ">= 70.0",
   "margin": 12.438,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.board_zone.max_x",
   "measured": 109.262,
   "unit": "mm",
   "required": "<= 117.0",
   "margin": 7.738,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.board_zone.min_z",
   "measured": -195.002,
   "unit": "mm",
   "required": ">= -240.0",
   "margin": 44.998,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.board_zone.max_z",
   "measured": -94.838,
   "unit": "mm",
   "required": "<= -30.0",
   "margin": 64.838,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.board_zone.min_y",
   "measured": 24.0,
   "unit": "mm",
   "required": ">= 10.0",
   "margin": 14.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-03.plate_under_x88_z-222.missing_volume",
   "measured": -1.4210854715202004e-14,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 1.4210854715202004e-14,
   "at": "(88.0000, -3.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x88_z-222.missing_volume",
   "measured": -1.4210854715202004e-14,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 1.4210854715202004e-14,
   "at": "(88.0000, -3.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x88_z-222.hole_gap",
   "measured": 19.494827009486404,
   "unit": "mm",
   "required": ">= 6.0",
   "margin": 13.494827009,
   "at": "(65.0000, -6.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x88_z-222.hole_gap",
   "measured": 19.494827009486404,
   "unit": "mm",
   "required": ">= 6.0",
   "margin": 13.494827009,
   "at": "(65.0000, -6.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x88_z-222.edge_gap",
   "measured": 30.3,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 22.3,
   "at": "(120.0000, -3.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x88_z-222.edge_gap",
   "measured": 30.3,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 22.3,
   "at": "(120.0000, -3.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x106_z-222.missing_volume",
   "measured": -1.4210854715202004e-14,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 1.4210854715202004e-14,
   "at": "(106.0000, -3.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x106_z-222.missing_volume",
   "measured": -1.4210854715202004e-14,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 1.4210854715202004e-14,
   "at": "(106.0000, -3.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x106_z-222.hole_gap",
   "measured": 37.40960958218893,
   "unit": "mm",
   "required": ">= 6.0",
   "margin": 31.409609582,
   "at": "(65.0000, -6.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x106_z-222.hole_gap",
   "measured": 37.40960958218893,
   "unit": "mm",
   "required": ">= 6.0",
   "margin": 31.409609582,
   "at": "(65.0000, -6.0000, -225.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x106_z-222.edge_gap",
   "measured": 12.3,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 4.3,
   "at": "(120.0000, -3.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x106_z-222.edge_gap",
   "measured": 12.3,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 4.3,
   "at": "(120.0000, -3.0000, -222.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x88_z-78.missing_volume",
   "measured": 7.105427357601002e-15,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": -7.105427357601002e-15,
   "at": "(88.0000, -3.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x88_z-78.missing_volume",
   "measured": 7.105427357601002e-15,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": -7.105427357601002e-15,
   "at": "(88.0000, -3.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x88_z-78.hole_gap",
   "measured": 31.7682957019364,
   "unit": "mm",
   "required": ">= 6.0",
   "margin": 25.768295702,
   "at": "(65.0000, -6.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x88_z-78.hole_gap",
   "measured": 31.7682957019364,
   "unit": "mm",
   "required": ">= 6.0",
   "margin": 25.768295702,
   "at": "(65.0000, -6.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x88_z-78.edge_gap",
   "measured": 30.3,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 22.3,
   "at": "(120.0000, -3.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x88_z-78.edge_gap",
   "measured": 30.3,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 22.3,
   "at": "(120.0000, -3.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x106_z-78.missing_volume",
   "measured": 7.105427357601002e-15,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": -7.105427357601002e-15,
   "at": "(106.0000, -3.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x106_z-78.missing_volume",
   "measured": 7.105427357601002e-15,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": -7.105427357601002e-15,
   "at": "(106.0000, -3.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x106_z-78.hole_gap",
   "measured": 45.39175083453431,
   "unit": "mm",
   "required": ">= 6.0",
   "margin": 39.391750835,
   "at": "(65.0000, -6.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x106_z-78.hole_gap",
   "measured": 45.39175083453431,
   "unit": "mm",
   "required": ">= 6.0",
   "margin": 39.391750835,
   "at": "(65.0000, -6.0000, -105.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "U-03.plate_under_x106_z-78.edge_gap",
   "measured": 12.3,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 4.3,
   "at": "(120.0000, -3.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "REQ-01.plate_under_x106_z-78.edge_gap",
   "measured": 12.3,
   "unit": "mm",
   "required": ">= 8.0",
   "margin": 4.3,
   "at": "(120.0000, -3.0000, -78.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-01"
   ]
  },
  {
   "gate": "E-05.H1.offset",
   "measured": 0.003162277660169997,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.096837722,
   "at": "(76.4380, 80.0000, -100.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "E-05.H2.offset",
   "measured": 0.003162277660168874,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.096837722,
   "at": "(76.4380, 27.9900, -100.0100) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "E-05.H5.offset",
   "measured": 0.004123105625623561,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.095876894,
   "at": "(82.4380, 81.9760, -157.5190) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "E-05.H6.offset",
   "measured": 0.0022360679775041115,
   "unit": "mm",
   "required": "<= 0.1",
   "margin": 0.097763932,
   "at": "(82.4380, 30.9920, -157.5110) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03"
   ]
  },
  {
   "gate": "REQ-04.x88_z-222.tray",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04.x88_z-222.board",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04.x106_z-222.tray",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04.x106_z-222.board",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04.x88_z-78.tray",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04.x88_z-78.board",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04.x106_z-78.tray",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-04.x106_z-78.board",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "REQ-05.box",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-03"
   ]
  },
  {
   "gate": "E-11.open_plus_x",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": null,
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-11"
   ]
  },
  {
   "gate": "U-03(b).interference_max",
   "measured": 0.0,
   "unit": "mm3",
   "required": "<= 0.0",
   "margin": 0.0,
   "at": "(5.0000, 0.0000, 0.0000) mm",
   "status": "PASS_ASSUMED",
   "assumes": [
    "A-02",
    "A-03",
    "A-06"
   ]
  },
  {
   "gate": "U-04.part.solids",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.part.volume_delta",
   "measured": 1.0186340659856796e-10,
   "unit": "mm3",
   "required": "in [0.0, 0.0]",
   "margin": -1.0186340659856796e-10,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.part.faces_delta",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.part.labels",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.part.valid_after",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.solids",
   "measured": 4,
   "unit": "count",
   "required": "== 4",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.faces_delta",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.labels",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-04.assembly.valid_after",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.mesh.bodies",
   "measured": 1,
   "unit": "count",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.mesh.naked_edges",
   "measured": 0,
   "unit": "count",
   "required": "== 0",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.mesh.winding",
   "measured": 1,
   "unit": "bool",
   "required": "== 1",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.tolerance",
   "measured": 0.01,
   "unit": "mm",
   "required": "<= 0.01",
   "margin": 0.0,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.angular_tolerance",
   "measured": 0.2,
   "unit": "rad",
   "required": "<= 0.25302439550057354",
   "margin": 0.053024396,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.build_sagitta",
   "measured": 0.004893867400154526,
   "unit": "mm",
   "required": "<= 0.01",
   "margin": 0.005106133,
   "at": null,
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-07.max_sagitta",
   "measured": 0.004893867400154526,
   "unit": "mm",
   "required": "<= 0.01",
   "margin": 0.005106133,
   "at": "(77.6095, 78.7963, -104.8479) mm",
   "status": "PASS",
   "assumes": []
  },
  {
   "gate": "U-08",
   "measured": null,
   "unit": "",
   "required": "N/A",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "D-07",
   "measured": null,
   "unit": "",
   "required": "N/A",
   "margin": null,
   "at": null,
   "status": "N/A",
   "assumes": []
  },
  {
   "gate": "REQ-06(Soft)",
   "measured": null,
   "unit": "",
   "required": "bench",
   "margin": null,
   "at": null,
   "status": "INCONCLUSIVE",
   "assumes": [
    "A-04",
    "A-12"
   ]
  }
 ],
 "sweep": [
  {
   "parameter": "pin_d",
   "values": [
    1.75,
    1.8,
    1.85
   ],
   "all_built": true,
   "worst_gate": "REQ-02.pin_y81.98_z-157.52.diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "bore_d",
   "values": [
    3.95,
    4.0,
    4.05
   ],
   "all_built": true,
   "worst_gate": "J-05.insert_y80_z-100.ray_0",
   "worst_margin": -0.025
  },
  {
   "parameter": "hole_d",
   "values": [
    3.3,
    3.4,
    3.5
   ],
   "all_built": true,
   "worst_gate": "REQ-01.x88_z-222.diameter",
   "worst_margin": 0.0
  },
  {
   "parameter": "seat_x",
   "values": [
    82.388,
    82.438,
    82.488
   ],
   "all_built": true,
   "worst_gate": "U-03.board.interference",
   "worst_margin": -8.294363933
  },
  {
   "parameter": "shift_y (standoffs, bores, pins)",
   "values": [
    -0.1,
    0.0,
    0.1
   ],
   "all_built": true,
   "worst_gate": "U-03.pin_y30.99_z-157.51.clearance",
   "worst_margin": -0.072004902
  },
  {
   "parameter": "shift_z (standoffs, bores, pins)",
   "values": [
    -0.1,
    0.0,
    0.1
   ],
   "all_built": true,
   "worst_gate": "U-03.pin_y30.99_z-157.51.clearance",
   "worst_margin": -0.0710198
  }
 ],
 "least_sure": [
  "D-04d against E-05: the pins keep 0.339 (H5) and 0.328 (H6) per side only because they sit within 0.004 of the scanned hole axes; the sweep shows that the 0.10 position allowance of REQ-02 / E-05 takes D-04d to 0.23. The holes are scan values (A-02, no calipers), so the real margin may be smaller than measured.",
  "The seat at x 82.438 is an exact contact on a scanned, invented-flat solder face (A-05): the heatsink's solder-side screw heads (X-35, X-36) are not in the model, so nothing on the solder side could be checked against the standoffs; and the seat contact rows FAIL for any seat other than the measured face.",
  "Two walls sit exactly at their limits as the spec dimensions them: the 2.0 web above the tie slots (D-01b, margin 0) and the 3.0 boss wall around each Ø4.0 insert bore (J-05, margin 0; 2.975 at a Ø4.05 bore)."
 ],
 "stopped": false
}
```
