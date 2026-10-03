## Gate rows (all)

| Gate | Item | Measured | Unit | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|---|---|
| exactly_one_solid | solid_count | 1 | count | == 1 | 0 | — | PASS | — |
| U-01 | solid_count | 1 | count | == 1 | 0 | — | PASS | — |
| U-01 | brep_valid | 1 | bool | == 1 | 0 | — | PASS | — |
| U-01 | naked_edges | 0 | count | == 0 | 0 | — | PASS | — |
| U-02 | size_x | 232 | mm | in [231.9, 232.1] | 0.1 | — | PASS | — |
| envelope_within_spec | size_x | 232 | mm | in [231.9, 232.1] | 0.1 | — | PASS | — |
| U-02 | size_y | 215 | mm | in [214.9, 215.1] | 0.1 | — | PASS | — |
| envelope_within_spec | size_y | 215 | mm | in [214.9, 215.1] | 0.1 | — | PASS | — |
| U-02 | size_z | 25 | mm | in [24.9, 25.1] | 0.1 | — | PASS | — |
| envelope_within_spec | size_z | 25 | mm | in [24.9, 25.1] | 0.1 | — | PASS | — |
| envelope_within_spec | position_min_x — position against the datum, reported apart from size | -116 | mm | in [-116.1, -115.9] | 0.1 | — | PASS | — |
| envelope_within_spec | position_max_x — position against the datum, reported apart from size | 116 | mm | in [115.9, 116.1] | 0.1 | — | PASS | — |
| envelope_within_spec | position_min_y — position against the datum, reported apart from size | -0 | mm | in [-0.1, 0.1] | 0.1 | — | PASS | — |
| envelope_within_spec | position_max_y — position against the datum, reported apart from size | 215 | mm | in [214.9, 215.1] | 0.1 | — | PASS | — |
| envelope_within_spec | position_min_z — position against the datum, reported apart from size | 72 | mm | in [71.9, 72.1] | 0.1 | — | PASS | — |
| envelope_within_spec | position_max_z — position against the datum, reported apart from size | 97 | mm | in [96.9, 97.1] | 0.1 | — | PASS | — |
| D-02 | size_x | 232 | mm | <= 420.0 | 188 | — | PASS (assumed: A-10) | A-10 |
| D-02 | size_y | 215 | mm | <= 420.0 | 205 | — | PASS (assumed: A-10) | A-10 |
| D-02 | size_z | 25 | mm | <= 500.0 | 475 | — | PASS (assumed: A-10) | A-10 |
| REQ-02 | x_min | -116 | mm | in [-116.1, -115.9] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | x_max | 116 | mm | in [115.9, 116.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | top_y | 215 | mm | in [214.9, 215.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-07 | min_z | 72 | mm | >= 72.0 | 0 | — | PASS (assumed: A-06, A-13) | A-06, A-13 |
| U-04 | schema_AP242 | 1 | bool | == 1 | 0 | — | PASS | — |
| U-04 | solids | 1 | count | == 1 | 0 | — | PASS | — |
| U-04 | volume_delta | 0 | mm3 | <= 0.0 | -0 | — | PASS | — |
| U-04 | faces_delta | 0 | count | == 0 | 0 | — | PASS | — |
| U-04 | labels | 1 | bool | == 1 | 0 | — | PASS | — |
| U-04 | valid_after | 1 | bool | == 1 | 0 | — | PASS | — |
| U-05 | bores_total — 4 flange + 3 button + 2 insert | 9 | count | == 9 | 0 | — | PASS | — |
| U-05 | flange_holes_d3.4_along_Y | 4 | count | == 4 | 0 | — | PASS | — |
| U-05 | button_holes_d15_along_Z | 3 | count | == 3 | 0 | — | PASS | — |
| U-05 | insert_bores_d4_blind_along_Z | 2 | count | == 2 | 0 | — | PASS | — |
| feature_census | bores_total — 4 flange + 3 button + 2 insert | 9 | count | == 9 | 0 | — | PASS | — |
| feature_census | flange_holes_d3.4_along_Y | 4 | count | == 4 | 0 | — | PASS | — |
| feature_census | button_holes_d15_along_Z | 3 | count | == 3 | 0 | — | PASS | — |
| feature_census | insert_bores_d4_blind_along_Z | 2 | count | == 2 | 0 | — | PASS | — |
| U-05 | gusset_hypotenuse_planes | 4 | count | == 4 | 0 | — | PASS | — |
| U-05 | boss_d11_axes | 2 | count | == 2 | 0 | — | PASS | — |
| U-05 | collar_reliefs | 2 | count | == 2 | 0 | — | PASS | — |
| feature_census | gusset_hypotenuse_planes | 4 | count | == 4 | 0 | — | PASS | — |
| feature_census | boss_d11_axes | 2 | count | == 2 | 0 | — | PASS | — |
| feature_census | collar_reliefs | 2 | count | == 2 | 0 | — | PASS | — |
| U-05 | named_features_present — wall, R1-R5, 2 flanges, 4 gussets by a probe point in each | 12 | count | == 12 | 0 | — | PASS | — |
| U-05 | brew_opening_open | 4 | count | == 4 | 0 | — | PASS | — |
| U-05 | faces_plane — reference count recorded | 40 | count | >= 0 | 40 | — | PASS | — |
| U-05 | faces_cylinder — reference count recorded | 13 | count | >= 0 | 13 | — | PASS | — |
| U-05 | faces_cone — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| U-05 | faces_sphere — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| U-05 | faces_torus — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| U-05 | faces_bspline — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| U-05 | faces_other — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| feature_census | named_features_present — wall, R1-R5, 2 flanges, 4 gussets by a probe point in each | 12 | count | == 12 | 0 | — | PASS | — |
| feature_census | brew_opening_open | 4 | count | == 4 | 0 | — | PASS | — |
| feature_census | faces_plane — reference count recorded | 40 | count | >= 0 | 40 | — | PASS | — |
| feature_census | faces_cylinder — reference count recorded | 13 | count | >= 0 | 13 | — | PASS | — |
| feature_census | faces_cone — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| feature_census | faces_sphere — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| feature_census | faces_torus — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| feature_census | faces_bspline — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| feature_census | faces_other — reference count recorded | 0 | count | >= 0 | 0 | — | PASS | — |
| REQ-01 | hole(-95,77)_diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(-95,77)_offset | 0 | mm | <= 0.1 | 0.1 | (-95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(-95,77)_length | 4 | mm | in [3.9, 4.1] | 0.1 | (-95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(-95,77)_through | 1 | bool | == 1 | 0 | (-95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| D-04a | hole(-95,77)_diameter | 3.4 | mm | >= 3.25 | 0.15 | (-95.0000, 0.0000, 77.0000) mm | PASS | — |
| D-03b | hole(-95,77)_bridge_span — the horizontal hole's crown bridges its diameter; reviewer confirms from sections | 3.4 | mm | <= 5.0 | 1.6 | (-95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-09) | A-09 |
| REQ-01 | hole(-85,77)_diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(-85,77)_offset | 0 | mm | <= 0.1 | 0.1 | (-85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(-85,77)_length | 4 | mm | in [3.9, 4.1] | 0.1 | (-85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(-85,77)_through | 1 | bool | == 1 | 0 | (-85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| D-04a | hole(-85,77)_diameter | 3.4 | mm | >= 3.25 | 0.15 | (-85.0000, 0.0000, 77.0000) mm | PASS | — |
| D-03b | hole(-85,77)_bridge_span — the horizontal hole's crown bridges its diameter; reviewer confirms from sections | 3.4 | mm | <= 5.0 | 1.6 | (-85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-09) | A-09 |
| REQ-01 | hole(+85,77)_diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(+85,77)_offset | 0 | mm | <= 0.1 | 0.1 | (85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(+85,77)_length | 4 | mm | in [3.9, 4.1] | 0.1 | (85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(+85,77)_through | 1 | bool | == 1 | 0 | (85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| D-04a | hole(+85,77)_diameter | 3.4 | mm | >= 3.25 | 0.15 | (85.0000, 0.0000, 77.0000) mm | PASS | — |
| D-03b | hole(+85,77)_bridge_span — the horizontal hole's crown bridges its diameter; reviewer confirms from sections | 3.4 | mm | <= 5.0 | 1.6 | (85.0000, 0.0000, 77.0000) mm | PASS (assumed: A-09) | A-09 |
| REQ-01 | hole(+95,77)_diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(+95,77)_offset | 0 | mm | <= 0.1 | 0.1 | (95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(+95,77)_length | 4 | mm | in [3.9, 4.1] | 0.1 | (95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| REQ-01 | hole(+95,77)_through | 1 | bool | == 1 | 0 | (95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-01) | A-01 |
| D-04a | hole(+95,77)_diameter | 3.4 | mm | >= 3.25 | 0.15 | (95.0000, 0.0000, 77.0000) mm | PASS | — |
| D-03b | hole(+95,77)_bridge_span — the horizontal hole's crown bridges its diameter; reviewer confirms from sections | 3.4 | mm | <= 5.0 | 1.6 | (95.0000, 0.0000, 77.0000) mm | PASS (assumed: A-09) | A-09 |
| REQ-01 | underside_faces_y_min | 0 | mm | in [-0.1, 0.1] | 0.1 | — | PASS (assumed: A-01) | A-01 |
| REQ-01 | underside_faces_y_max | 0 | mm | in [-0.1, 0.1] | 0.1 | — | PASS (assumed: A-01) | A-01 |
| D-05b | upper_diameter | 4 | mm | in [3.95, 4.05] | 0.05 | (-91.0555, 153.2349, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| D-05b | upper_depth | 6 | mm | in [5.9, 6.1] | 0.1 | (-91.0555, 153.2349, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| D-05b | upper_blind | 0 | bool | == 0 | 0 | (-91.0555, 153.2349, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| E-05 | upper_axis_offset — board hole axis (-91.0555, 153.2349) d 3.5376 | 0 | mm | <= 0.1 | 0.1 | (-91.0555, 153.2349, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| D-05a | upper_across | 10.7737 | mm | >= 8.0 | 2.7737 | angle 90 deg, 1.5 mm from the boss end | PASS (assumed: A-03) | A-03 |
| J-05 | upper_wall | 3.05 | mm | >= 3.0 | 0.05 | (-92.2772, 158.1349, 85.5850) mm | PASS (assumed: A-03) | A-03 |
| D-05b | lower_diameter | 4 | mm | in [3.95, 4.05] | 0.05 | (-90.9987, 127.2515, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| D-05b | lower_depth | 6 | mm | in [5.9, 6.1] | 0.1 | (-90.9987, 127.2515, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| D-05b | lower_blind | 0 | bool | == 0 | 0 | (-90.9987, 127.2515, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| E-05 | lower_axis_offset — board hole axis (-90.9987, 127.2515) d 3.4412 | 0 | mm | <= 0.1 | 0.1 | (-90.9987, 127.2515, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| D-05a | lower_across | 10.9582 | mm | >= 8.0 | 2.9582 | angle 90 deg, 1.5 mm from the boss end | PASS (assumed: A-03) | A-03 |
| J-05 | lower_wall | 3.2879 | mm | >= 3.0 | 0.2879 | (-92.0981, 122.0791, 85.5850) mm | PASS (assumed: A-03) | A-03 |
| REQ-04 | B1_foremost_z | 95.3326 | mm | >= 95.0 | 0.3326 | (-95.0803, 161.4411, 95.3326) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-04 | B1_hole_offset — cap axis at z 95.5: (-94.2478, 166.5135) | 0 | mm | <= 0.25 | 0.25 | (-94.2478, 166.5135, 94.0000) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-04 | B2_foremost_z | 98.5647 | mm | >= 97.5 | 1.0647 | (-96.3901, 144.7806, 98.5647) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-04 | B2_hole_offset — cap axis at z 95.5: (-98.9908, 139.9014) | 0 | mm | <= 0.25 | 0.25 | (-98.9908, 139.9014, 94.0000) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-04 | B3_foremost_z | 95.3449 | mm | >= 95.0 | 0.3449 | (-94.9164, 118.4549, 95.3449) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| REQ-04 | B3_hole_offset — cap axis at z 95.5: (-93.7652, 113.4263) | 0 | mm | <= 0.25 | 0.25 | (-93.7652, 113.4263, 94.0000) mm | PASS (assumed: A-03, A-04) | A-03, A-04 |
| U-03 | a_contact_wall_foot_on_C01 | 0 | mm | == 0.0 | 0 | (-116.0000, 0.0000, 97.0000) mm | PASS (assumed: A-02) | A-02 |
| U-03 | a_contact_flange_L_on_C01 | 0 | mm | == 0.0 | 0 | (-104.0000, 0.0000, 94.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03 | a_contact_flange_R_on_C01 | 0 | mm | == 0.0 | 0 | (75.0000, 0.0000, 94.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03 | a_contact_C10_skirt_on_wall_top | 0 | mm | == 0.0 | 0 | (110.0000, 215.0000, 97.0000) mm | PASS (assumed: A-07) | A-07 |
| U-03 | a_contact_boss_upper_on_E02 | 0.0001 | mm | == 0.0 | -0.0001 | (-93.9253, 157.9268, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| U-03 | a_contact_boss_lower_on_E02 | 0.0001 | mm | == 0.0 | -0.0001 | (-93.2170, 122.2187, 85.4850) mm | PASS (assumed: A-03) | A-03 |
| U-03 | a_interference_panel|C01 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_panel|C05 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_panel|housing | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_panel|G04 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_panel|C10 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_C01|C05 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_C01|housing | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_C01|G04 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_C01|C10 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_C05|housing | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_C05|G04 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_C05|C10 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_housing|G04 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_housing|C10 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_G04|C10 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_G10|C01 | 1 (clearance 132.2956 mm) | bool | clearance > 0 and inside == False | 0 | (18.4856, 132.2956, 33.4007) mm | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_E02|C01 | 1 (clearance 101.84 mm) | bool | clearance > 0 and inside == False | 0 | (-85.8827, 101.8400, 75.2476) mm | PASS (assumed: A-03) | A-03 |
| U-03 | a_interference_G10|C05 | 1 (clearance 13.689 mm) | bool | clearance > 0 and inside == False | 0 | (26.5716, 191.3110, 46.4451) mm | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_E02|C05 | 1 (clearance 39.0708 mm) | bool | clearance > 0 and inside == False | 0 | (-82.2267, 176.9781, 75.2476) mm | PASS (assumed: A-03) | A-03 |
| U-03 | a_interference_G10|housing | 1 (clearance 0 mm) | bool | clearance > 0 and inside == False | 0 | (30.8756, 186.5108, 24.9062) mm | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_E02|housing | 1 (clearance 30.4172 mm) | bool | clearance > 0 and inside == False | 0 | (-61.5743, 155.2093, 51.4248) mm | PASS (assumed: A-03) | A-03 |
| U-03 | a_interference_G10|G04 | 1 (clearance 0.4782 mm) | bool | clearance > 0 and inside == False | 0 | (5.9898, 187.4442, 9.3504) mm | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_E02|G04 | 1 (clearance 50.4778 mm) | bool | clearance > 0 and inside == False | 0 | (-61.5310, 155.2202, 51.6726) mm | PASS (assumed: A-03) | A-03 |
| U-03 | a_interference_G10|C10 | 1 (clearance 20.4524 mm) | bool | clearance > 0 and inside == False | 0 | (35.9336, 191.3110, 30.5028) mm | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_E02|C10 | 1 (clearance 39.5434 mm) | bool | clearance > 0 and inside == False | 0 | (-102.6099, 178.1678, 75.2476) mm | PASS (assumed: A-03) | A-03 |
| U-03 | a_interference_E02|G10 | 1 (clearance 35.5638 mm) | bool | clearance > 0 and inside == False | 0 | (-61.5895, 155.2070, 51.3723) mm | PASS (assumed: A-03, A-05) | A-03, A-05 |
| U-03 | a_interference_panel|G10 | 1 (clearance 14.0206 mm) | bool | clearance > 0 and inside == False | 0 | (37.0484, 188.0000, 97.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03 | a_interference_panel|E02 — panel pulled 0.005 (the mm band) off the board along +Z: the boss ends are designed contacts | 1 (clearance 0.0051 mm) | bool | clearance > 0 and inside == False | 0 | (-93.2170, 122.2187, 85.4900) mm | PASS (assumed: A-03) | A-03 |
| U-03 | a_footprint_to_plate_edge | 0.7805 | mm | >= 0.5 | 0.2805 | (116.0000, 0.0000, 97.0000) mm | PASS (assumed: A-02) | A-02 |
| U-03 | a_flange_L_to_C01_holes | 4.3 | mm | >= 3.0 | 1.3 | (-104.0000, 0.0000, 90.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03 | a_flange_R_to_C01_holes | 4.3 | mm | >= 3.0 | 1.3 | (104.0000, 0.0000, 90.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03 | a_wall_foot_to_C01_holes | 2.3 | mm | >= 2.0 | 0.3 | (-110.0000, 0.0000, 94.0000) mm | PASS (assumed: A-02) | A-02 |
| U-03 | a_flange_hole_centres_to_C01_hole_centres | 19.8494 | mm | >= 6.0 | 13.8494 | flange hole (-95.0, 77.0) to C01 hole (-110.00, 90.00) | PASS (assumed: A-01) | A-01 |
| U-03 | a_panel_to_C05 | 12 | mm | >= 2.0 | 10 | (-55.0000, 210.0000, 94.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03 | a_panel_to_housing | 8.7757 | mm | >= 2.0 | 6.7757 | (-44.0000, 191.0000, 84.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03 | a_panel_to_G04 | 18.0531 | mm | >= 2.0 | 16.0531 | (-1.3302, 191.0000, 84.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03 | a_panel|C15_keepout(-110,90) | 0 | mm3 | <= 0.0 | 0 | — | PASS | — |
| U-03 | a_panel|C15_keepout(+110,90) | 0 | mm3 | <= 0.0 | 0 | — | PASS | — |
| U-03 | b_lowering_C01 — worst step at +40.0 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | b_lowering_C05 — worst step at +40.0 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | b_lowering_housing — worst step at +40.0 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | b_lowering_G04 — worst step at +40.0 | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05) | A-05 |
| U-03 | b_lowering_G10_separated — least step at +0.0 | 1 (clearance 14.0206 mm) | bool | clearance > 0 and inside == False | 0 | (37.0484, 188.0000, 97.0000) mm | PASS (assumed: A-05) | A-05 |
| E-01 | panel_without_bosses_to_E02 | 1.1361 | mm | >= 0.5 | 0.6361 | (-94.6782, 146.0375, 94.0000) mm | PASS (assumed: A-03) | A-03 |
| E-01 | boss_upper_from_end+0.5 — boss end measured at z 85.4850; reads <= 0.5 by construction | 0.5 | mm | >= 0.5 | -0 | (-90.5729, 158.7137, 85.9850) mm | PASS (assumed: A-03) | A-03 |
| E-01 | boss_upper_from_end+2.0_side_gap — reported side gap | 0.5 | mm | >= 0.5 | -0 | (-90.5729, 158.7137, 87.4850) mm | PASS (assumed: A-03) | A-03 |
| E-01 | boss_lower_from_end+0.5 — boss end measured at z 85.4850; reads <= 0.5 by construction | 0.5 | mm | >= 0.5 | -0 | (-90.8794, 121.7528, 85.9850) mm | PASS (assumed: A-03) | A-03 |
| E-01 | boss_lower_from_end+2.0_side_gap — reported side gap | 0.5 | mm | >= 0.5 | -0 | (-90.8794, 121.7528, 87.4850) mm | PASS (assumed: A-03) | A-03 |
| REQ-02 | outer_face_at(-100,100) | 97 | mm | in [96.9, 97.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | inner_face_at(-100,100) | 94 | mm | in [93.9, 94.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | outer_face_at(+100,100) | 97 | mm | in [96.9, 97.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | inner_face_at(+100,100) | 94 | mm | in [93.9, 94.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | outer_face_at(-100,200) | 97 | mm | in [96.9, 97.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | inner_face_at(-100,200) | 94 | mm | in [93.9, 94.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | outer_face_at(+0,200) | 97 | mm | in [96.9, 97.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | inner_face_at(+0,200) | 94 | mm | in [93.9, 94.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | outer_face_at(+100,200) | 97 | mm | in [96.9, 97.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-02 | inner_face_at(+100,200) | 94 | mm | in [93.9, 94.1] | 0.1 | — | PASS (assumed: A-02) | A-02 |
| REQ-03 | slot_left_x | -75 | mm | in [-75.1, -74.9] | 0.1 | — | PASS (assumed: A-06) | A-06 |
| REQ-03 | slot_right_x | 75 | mm | in [74.9, 75.1] | 0.1 | — | PASS (assumed: A-06) | A-06 |
| REQ-03 | window_left_x | -57.5 | mm | in [-57.6, -57.4] | 0.1 | — | PASS (assumed: A-05) | A-05 |
| REQ-03 | window_right_x | 75 | mm | in [74.9, 75.1] | 0.1 | — | PASS (assumed: A-05) | A-05 |
| REQ-03 | window_top_y | 188 | mm | in [187.9, 188.1] | 0.1 | — | PASS (assumed: A-05) | A-05 |
| REQ-03 | slot_top_y_at_step | 50 | mm | in [49.9, 50.1] | 0.1 | — | PASS (assumed: A-06) | A-06 |
| REQ-03 | panel|slot_box | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05, A-06) | A-05, A-06 |
| REQ-03 | panel|window_box | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-05, A-06) | A-05, A-06 |
| REQ-05 | a_G10_to_panel_least — worst phi +10 deg | 2.5114 | mm | >= 2.0 | 0.5114 | (75.0000, 160.2973, 97.0000) mm | PASS (assumed: A-05) | A-05 |
| REQ-05 | a_G10_to_E02_least — worst phi -55 deg | 28.6686 | mm | >= 2.0 | 26.6686 | (-61.5264, 155.5486, 58.9320) mm | PASS (assumed: A-05) | A-05 |
| REQ-05 | b_carry_G10_vs_panel — worst step: axis at z 67 | 1 (clearance 11.689 mm) | bool | clearance > 0 and inside == False at every step | 0 | (10.7103, 188.0000, 95.2843) mm | PASS (assumed: A-05) | A-05 |
| REQ-05 | b_carry_G10_vs_E02 — worst step: axis at z 62 | 1 (clearance 29.9146 mm) | bool | clearance > 0 and inside == False at every step | 0 | (-61.5264, 155.5486, 58.9320) mm | PASS (assumed: A-05) | A-05 |
| REQ-06 | panel|driver_flange(-95,77) | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-14) | A-14 |
| REQ-06 | panel|driver_flange(-85,77) | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-14) | A-14 |
| REQ-06 | panel|driver_flange(+85,77) | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-14) | A-14 |
| REQ-06 | panel|driver_flange(+95,77) | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-14) | A-14 |
| REQ-06 | panel|driver_C15(-110,90) | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-14) | A-14 |
| REQ-06 | panel|driver_C15(+110,90) | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-14) | A-14 |
| REQ-07 | panel|tray_box | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-06, A-13) | A-06, A-13 |
| REQ-07 | panel|knob_place | 0 | mm3 | <= 0.0 | 0 | — | PASS (assumed: A-06, A-13) | A-06, A-13 |
| E-06 | self_check_ties — self-check only; the reviewer gates E-06 from sections | 6 | count | == 6 | 0 | — | PASS | — |
| D-01a | min_wall | 3 | mm | >= 0.8 | 2.2 | (-115.7756, 0.2244, 97.0000) mm | PASS | — |
| D-06a | min_wall | 3 | mm | >= 1.0 | 2 | (-115.7756, 0.2244, 97.0000) mm | PASS | — |
| D-01b | min_wall | 3 | mm | >= 2.0 | 1 | (-115.7756, 0.2244, 97.0000) mm | PASS (assumed: A-11) | A-11 |
| U-06 | min_wall_wide — Soft | 3 | mm | >= 2.0 | 1 | (-115.7756, 0.2244, 97.0000) mm | PASS | — |
| D-03a | least_downward_angle_excluding_flange_hole_crowns | 90 | deg | >= 45.0 | 45 | — | PASS (assumed: A-09) | A-09 |
| D-03a | flange_hole_crowns_named_exception — whole part including the crowns: least 0.0 at (-95.0, 4.0, 75.3) | 0 | deg |  | — | — | INFO | — |
| D-03b | flat_ceiling_spans_lead — lead for the reviewer, on the part with the four horizontal holes filled | 0 | mm | <= 5.0 | 5 | — | PASS (assumed: A-09) | A-09 |
| U-07 | stl_tolerance | 0.01 | mm | <= 0.01 | 0 | — | PASS | — |
| U-07 | stl_max_sagitta | 0.0049 | mm | <= 0.01 | 0.0051 | (-97.2477, 132.6118, 96.2500) mm | PASS | — |
| U-07 | angular_tolerance — bound 4*acos(1-0.01/R_max) with R_max 8.6907 = 0.19191 rad | 0.15 | rad | <= 0.19190631329799243 | 0.0419 | — | PASS | — |
| U-07 | delivered_stl_is_this_mesh — triangles 3932 | 1 | bool | == 1 | 0 | — | PASS | — |
| U-08 | threads — no threads on this target (row text) | — |  |  | — | — | N/A | — |
| D-07 | fit_critical_bores — none: insert bores formed by the insert (row text) | — |  |  | — | — | N/A | — |
| REQ-08 | stiffness — Soft, bench: answered by the first print (A-12) | — |  |  | — | — | INCONCLUSIVE | A-12 |

## Sweep runs

| Run | Overrides | Built, one solid | Gates not PASS / PASS_ASSUMED | Worst margin per gate (least of the run) |
|---|---|---|---|---|

## Sweep worst margin per gate

| Gate | Worst margin over the sweep | Run | Item | Measured |
|---|---|---|---|---|
