| Gate | Measured | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|
| U-01.solid_count | 1 count | == 1 | 0 | — | PASS | — |
| U-01.brep_valid | 1 bool | == 1 | 0 | — | PASS | — |
| U-01.naked_edges | 0 count | == 0 | 0 | — | PASS | — |
| exactly_one_solid | 1 count | == 1 | 0 | — | PASS | — |
| U-02.size_x | 240 mm | in [239.9, 240.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size_x | 240 mm | in [239.9, 240.1] | 0.1 | — | PASS | — |
| U-02.size_y | 39.5 mm | in [39.4, 39.6] | 0.1 | — | PASS | — |
| envelope_within_spec.size_y | 39.5 mm | in [39.4, 39.6] | 0.1 | — | PASS | — |
| U-02.size_z | 405 mm | in [404.9, 405.1] | 0.1 | — | PASS | — |
| envelope_within_spec.size_z | 405 mm | in [404.9, 405.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_x | -120 mm | in [-120.1, -119.9] | 0.1 | — | PASS | — |
| envelope_within_spec.position.max_x | 120 mm | in [119.9, 120.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_y | 210.5 mm | in [210.4, 210.6] | 0.1 | — | PASS | — |
| envelope_within_spec.position.max_y | 250 mm | in [249.9, 250.1] | 0.1 | — | PASS | — |
| envelope_within_spec.position.min_z | -305 mm | in [-305.1, -304.9] | 0.1 | — | PASS | — |
| envelope_within_spec.position.max_z | 100 mm | in [99.9, 100.1] | 0.1 | — | PASS | — |
| D-02.size_x | 240 mm | <= 420.0 | 180 | — | PASS (assumed: A-09) | A-09 |
| D-02.size_z | 405 mm | <= 420.0 | 15 | — | PASS (assumed: A-09) | A-09 |
| D-02.size_y | 39.5 mm | <= 500.0 | 460.5 | — | PASS (assumed: A-09) | A-09 |
| REQ-01.max_y | 250 mm | in [249.9, 250.1] | 0.1 | — | PASS (assumed: A-06) | A-06 |
| REQ-02.min_x | -120 mm | in [-120.1, -119.9] | 0.1 | — | PASS (assumed: A-04) | A-04 |
| REQ-02.max_x | 120 mm | in [119.9, 120.1] | 0.1 | — | PASS (assumed: A-04) | A-04 |
| REQ-02.min_z | -305 mm | in [-305.1, -304.9] | 0.1 | — | PASS (assumed: A-04) | A-04 |
| REQ-02.max_z | 100 mm | in [99.9, 100.1] | 0.1 | — | PASS (assumed: A-04) | A-04 |
| REQ-01.top_faces | 1 count | == 1 | 0 | — | PASS (assumed: A-06) | A-06 |
| REQ-01.top_face_y | 250 mm | in [249.9, 250.1] | 0.1 | (-120.0000, 250.0000, -305.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x0_z-150 | 3 mm | in [2.9, 3.1] | 0.1 | (0.0000, 248.5000, -150.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x-100_z-100 | 3 mm | in [2.9, 3.1] | 0.1 | (-100.0000, 248.5000, -100.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x100_z0 | 3 mm | in [2.9, 3.1] | 0.1 | (100.0000, 248.5000, 0.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x0_z0 | 3 mm | in [2.9, 3.1] | 0.1 | (0.0000, 248.5000, 0.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-01.skin_t.x-80_z80 | 3 mm | in [2.9, 3.1] | 0.1 | (-80.0000, 248.5000, 80.0000) mm | PASS (assumed: A-06) | A-06 |
| REQ-02.corner_r.x110_z-295.a15 | 10 mm | in [9.9, 10.1] | 0.1 | (119.6593, 230.0000, -297.5882) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z-295.a45 | 10 mm | in [9.9, 10.1] | 0.1 | (117.0711, 230.0000, -302.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z-295.a75 | 10 mm | in [9.9, 10.1] | 0.1 | (112.5882, 230.0000, -304.6593) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.corner_x110_z-295 | 3 mm | in [2.9, 3.1] | 0.1 | (117.0711, 230.0000, -302.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z90.a285 | 10 mm | in [9.9, 10.1] | 0.1 | (112.5882, 230.0000, 99.6593) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z90.a315 | 10 mm | in [9.9, 10.1] | 0.1 | (117.0711, 230.0000, 97.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x110_z90.a345 | 10 mm | in [9.9, 10.1] | 0.1 | (119.6593, 230.0000, 92.5882) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.corner_x110_z90 | 3 mm | in [2.9, 3.1] | 0.1 | (117.0711, 230.0000, 97.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z-295.a105 | 10 mm | in [9.9, 10.1] | 0.1 | (-112.5882, 230.0000, -304.6593) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z-295.a135 | 10 mm | in [9.9, 10.1] | 0.1 | (-117.0711, 230.0000, -302.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z-295.a165 | 10 mm | in [9.9, 10.1] | 0.1 | (-119.6593, 230.0000, -297.5882) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.corner_x-110_z-295 | 3 mm | in [2.9, 3.1] | 0.1 | (-117.0711, 230.0000, -302.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z90.a195 | 10 mm | in [9.9, 10.1] | 0.1 | (-119.6593, 230.0000, 92.5882) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z90.a225 | 10 mm | in [9.9, 10.1] | 0.1 | (-117.0711, 230.0000, 97.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.corner_r.x-110_z90.a255 | 10 mm | in [9.9, 10.1] | 0.1 | (-112.5882, 230.0000, 99.6593) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.corner_x-110_z90 | 3 mm | in [2.9, 3.1] | 0.1 | (-117.0711, 230.0000, 97.0711) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+x.at0_-150 | 3 mm | in [2.9, 3.1] | 0.1 | (120.0000, 230.0000, -150.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+x.at0_0 | 3 mm | in [2.9, 3.1] | 0.1 | (120.0000, 230.0000, 0.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+x.at0_60 | 3 mm | in [2.9, 3.1] | 0.1 | (120.0000, 230.0000, 60.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-x.at0_-150 | 3 mm | in [2.9, 3.1] | 0.1 | (-120.0000, 230.0000, -150.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-x.at0_0 | 3 mm | in [2.9, 3.1] | 0.1 | (-120.0000, 230.0000, -0.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-x.at0_60 | 3 mm | in [2.9, 3.1] | 0.1 | (-120.0000, 230.0000, 60.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-z.at-40_0 | 3 mm | in [2.9, 3.1] | 0.1 | (-40.0000, 230.0000, -305.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-z.at0_0 | 3 mm | in [2.9, 3.1] | 0.1 | (0.0000, 230.0000, -305.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.-z.at40_0 | 3 mm | in [2.9, 3.1] | 0.1 | (40.0000, 230.0000, -305.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+z.at-40_0 | 3 mm | in [2.9, 3.1] | 0.1 | (-40.0000, 230.0000, 100.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+z.at0_0 | 3 mm | in [2.9, 3.1] | 0.1 | (-0.0000, 230.0000, 100.0000) mm | PASS (assumed: A-04) | A-04 |
| REQ-02.skirt_t.+z.at40_0 | 3 mm | in [2.9, 3.1] | 0.1 | (40.0000, 230.0000, 100.0000) mm | PASS (assumed: A-04) | A-04 |
| U-05.skirt_bottom_faces | 1 count | == 1 | 0 | — | PASS | — |
| REQ-02.skirt_bottom_y | 215 mm | in [214.9, 215.1] | 0.1 | (-120.0000, 215.0000, -305.0000) mm | PASS (assumed: A-04) | A-04 |
| U-05.plane_faces | 59 count | == 59 | 0 | — | PASS | — |
| feature_census.plane_faces | 59 count | == 59 | 0 | — | PASS | — |
| U-05.cylinder_faces | 22 count | == 22 | 0 | — | PASS | — |
| feature_census.cylinder_faces | 22 count | == 22 | 0 | — | PASS | — |
| U-05.concave_cylinders | 12 count | == 12 | 0 | — | PASS | — |
| feature_census.concave_cylinders | 12 count | == 12 | 0 | — | PASS | — |
| U-05.convex_cylinders | 10 count | == 10 | 0 | — | PASS | — |
| feature_census.convex_cylinders | 10 count | == 10 | 0 | — | PASS | — |
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
| U-05.bores | 8 count | == 8 | 0 | — | PASS | — |
| feature_census.bores | 8 count | == 8 | 0 | — | PASS | — |
| U-05.bores_d34_y_through | 4 count | == 4 | 0 | — | PASS | — |
| U-05.bores_d65_y_blind | 4 count | == 4 | 0 | — | PASS | — |
| U-05.column_cylinders | 4 count | == 4 | 0 | — | PASS | — |
| feature_census.column_cylinders | 4 count | == 4 | 0 | — | PASS | — |
| U-05.pad_cylinders | 2 count | == 2 | 0 | — | PASS | — |
| feature_census.pad_cylinders | 2 count | == 2 | 0 | — | PASS | — |
| U-05.bulk_rib_sides | 8 count | == 8 | 0 | — | PASS | — |
| feature_census.bulk_rib_sides | 8 count | == 8 | 0 | — | PASS | — |
| U-05.bulk_rib_hyp | 4 count | == 4 | 0 | — | PASS | — |
| feature_census.bulk_rib_hyp | 4 count | == 4 | 0 | — | PASS | — |
| U-05.rear_rib_sides | 16 count | == 16 | 0 | — | PASS | — |
| feature_census.rear_rib_sides | 16 count | == 16 | 0 | — | PASS | — |
| U-05.rear_rib_bottoms | 4 count | == 4 | 0 | — | PASS | — |
| feature_census.rear_rib_bottoms | 4 count | == 4 | 0 | — | PASS | — |
| U-05.rear_rib_hyp | 4 count | == 4 | 0 | — | PASS | — |
| feature_census.rear_rib_hyp | 4 count | == 4 | 0 | — | PASS | — |
| U-05.skin_under_faces | 3 count | == 3 | 0 | — | PASS | — |
| feature_census.skin_under_faces | 3 count | == 3 | 0 | — | PASS | — |
| REQ-03.x65_z-60.column_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.column_d_face | 12 mm | in [11.9, 12.1] | 0.1 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.column_d_x | 12 mm | in [11.9, 12.1] | 0.1 | (71.0000, 215.5000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.column_d_z | 12 mm | in [11.9, 12.1] | 0.1 | (65.0000, 215.5000, -66.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.column_bottom_y | 215 mm | in [214.95, 215.05] | 0.05 | (59.0000, 215.0000, -66.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.hole_d | 3.4 mm | in [3.3, 3.5] | 0.1 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.hole_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.hole_through | 1 bool | == 1 | 0 | (65.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| D-04a.x65_z-60.hole_d | 3.4 mm | >= 3.25 | 0.15 | (65.0000, 215.0000, -60.0000) mm | PASS | — |
| REQ-03.x65_z-60.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (65.0000, 218.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-60.cbore_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 218.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-07.x65_z-60.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (65.0000, 218.0000, -60.0000) mm | PASS | — |
| REQ-03.x65_z-60.cbore_floor_y | 218 mm | in [217.9, 218.1] | 0.1 | (65.0000, 218.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-07.x65_z-60.cbore_mouth_y | 250 mm | in [249.9, 250.1] | 0.1 | (65.0000, 250.0000, -60.0000) mm | PASS | — |
| REQ-07.x65_z-60.driver_path_interference | 0 mm3 | <= 0.0 | 0 | — | PASS | — |
| REQ-03.x65_z-210.column_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.column_d_face | 12 mm | in [11.9, 12.1] | 0.1 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.column_d_x | 12 mm | in [11.9, 12.1] | 0.1 | (71.0000, 215.5000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.column_d_z | 12 mm | in [11.9, 12.1] | 0.1 | (65.0000, 215.5000, -216.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.column_bottom_y | 215 mm | in [214.95, 215.05] | 0.05 | (59.0000, 215.0000, -216.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.hole_d | 3.4 mm | in [3.3, 3.5] | 0.1 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.hole_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.hole_through | 1 bool | == 1 | 0 | (65.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| D-04a.x65_z-210.hole_d | 3.4 mm | >= 3.25 | 0.15 | (65.0000, 215.0000, -210.0000) mm | PASS | — |
| REQ-03.x65_z-210.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (65.0000, 218.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-03.x65_z-210.cbore_offset | 0 mm | <= 0.1 | 0.1 | (65.0000, 218.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-07.x65_z-210.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (65.0000, 218.0000, -210.0000) mm | PASS | — |
| REQ-03.x65_z-210.cbore_floor_y | 218 mm | in [217.9, 218.1] | 0.1 | (65.0000, 218.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| REQ-07.x65_z-210.cbore_mouth_y | 250 mm | in [249.9, 250.1] | 0.1 | (65.0000, 250.0000, -210.0000) mm | PASS | — |
| REQ-07.x65_z-210.driver_path_interference | 0 mm3 | <= 0.0 | 0 | — | PASS | — |
| REQ-04.x90_z-293.column_offset | 0 mm | <= 0.1 | 0.1 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.column_d_face | 12 mm | in [11.9, 12.1] | 0.1 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.column_d_x | 12 mm | in [11.9, 12.1] | 0.1 | (96.0000, 215.5000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.column_d_z | 12 mm | in [11.9, 12.1] | 0.1 | (90.0000, 215.5000, -299.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.column_bottom_y | 215 mm | in [214.95, 215.05] | 0.05 | (84.0000, 215.0000, -299.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.hole_d | 3.4 mm | in [3.3, 3.5] | 0.1 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.hole_offset | 0 mm | <= 0.1 | 0.1 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.hole_through | 1 bool | == 1 | 0 | (90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| D-04a.x90_z-293.hole_d | 3.4 mm | >= 3.25 | 0.15 | (90.0000, 215.0000, -293.0000) mm | PASS | — |
| REQ-04.x90_z-293.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x90_z-293.cbore_offset | 0 mm | <= 0.1 | 0.1 | (90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-07.x90_z-293.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (90.0000, 218.0000, -293.0000) mm | PASS | — |
| REQ-04.x90_z-293.cbore_floor_y | 218 mm | in [217.9, 218.1] | 0.1 | (90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-07.x90_z-293.cbore_mouth_y | 250 mm | in [249.9, 250.1] | 0.1 | (90.0000, 250.0000, -293.0000) mm | PASS | — |
| REQ-07.x90_z-293.driver_path_interference | 0 mm3 | <= 0.0 | 0 | — | PASS | — |
| REQ-04.x-90_z-293.column_offset | 0 mm | <= 0.1 | 0.1 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.column_d_face | 12 mm | in [11.9, 12.1] | 0.1 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.column_d_x | 12 mm | in [11.9, 12.1] | 0.1 | (-84.0000, 215.5000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.column_d_z | 12 mm | in [11.9, 12.1] | 0.1 | (-90.0000, 215.5000, -299.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.column_bottom_y | 215 mm | in [214.95, 215.05] | 0.05 | (-96.0000, 215.0000, -299.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.hole_d | 3.4 mm | in [3.3, 3.5] | 0.1 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.hole_offset | 0 mm | <= 0.1 | 0.1 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.hole_through | 1 bool | == 1 | 0 | (-90.0000, 215.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| D-04a.x-90_z-293.hole_d | 3.4 mm | >= 3.25 | 0.15 | (-90.0000, 215.0000, -293.0000) mm | PASS | — |
| REQ-04.x-90_z-293.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (-90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-04.x-90_z-293.cbore_offset | 0 mm | <= 0.1 | 0.1 | (-90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-07.x-90_z-293.cbore_d | 6.5 mm | in [6.4, 6.6] | 0.1 | (-90.0000, 218.0000, -293.0000) mm | PASS | — |
| REQ-04.x-90_z-293.cbore_floor_y | 218 mm | in [217.9, 218.1] | 0.1 | (-90.0000, 218.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| REQ-07.x-90_z-293.cbore_mouth_y | 250 mm | in [249.9, 250.1] | 0.1 | (-90.0000, 250.0000, -293.0000) mm | PASS | — |
| REQ-07.x-90_z-293.driver_path_interference | 0 mm3 | <= 0.0 | 0 | — | PASS | — |
| REQ-05.x48_z30.pad_offset | 0 mm | <= 0.1 | 0.1 | (48.0000, 210.5000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.pad_d_x | 10 mm | in [9.9, 10.1] | 0.1 | (53.0000, 220.0000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.pad_d_z | 10 mm | in [9.9, 10.1] | 0.1 | (48.0000, 220.0000, 25.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.pad_bottom_y | 210.5 mm | in [210.45, 210.55] | 0.05 | (43.0000, 210.5000, 25.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.pad_offset | 0 mm | <= 0.1 | 0.1 | (-48.0000, 210.5000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.pad_d_x | 10 mm | in [9.9, 10.1] | 0.1 | (-43.0000, 220.0000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.pad_d_z | 10 mm | in [9.9, 10.1] | 0.1 | (-48.0000, 220.0000, 25.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.pad_bottom_y | 210.5 mm | in [210.45, 210.55] | 0.05 | (-53.0000, 210.5000, 25.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-06.headroom_interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-06) | A-06 |
| D-03b.flat_ceiling_span | 3.1386 mm | <= 5.0 | 1.8614 | (66.5000, 218.0000, -60.8000) mm | PASS (assumed: A-08) | A-08 |
| U-03.seat.x65_z-60.c02.clearance | 0 mm | == 0.0 | 0 | (67.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.seat.x65_z-60.c02.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.coaxial.x65_z-60 | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -60.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-03.x65_z-60.coaxial_with_insert | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -60.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| U-03.seat.x65_z-210.c02.clearance | 0 mm | == 0.0 | 0 | (67.0000, 215.0000, -210.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.seat.x65_z-210.c02.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.coaxial.x65_z-210 | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -210.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-03.x65_z-210.coaxial_with_insert | 0 mm | <= 0.1 | 0.1 | (65.0000, 209.0000, -210.0000) mm | PASS (assumed: A-01, A-05) | A-01, A-05 |
| U-03.seat.x90_z-293.c11.clearance | 0 mm | == 0.0 | 0 | (96.0000, 215.0000, -293.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.seat.x90_z-293.c11.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.coaxial.x90_z-293 | 0 mm | <= 0.1 | 0.1 | (90.0000, 209.0000, -293.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-04.x90_z-293.coaxial_with_insert | 0 mm | <= 0.1 | 0.1 | (90.0000, 209.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| U-03.seat.x-90_z-293.c11.clearance | 0 mm | == 0.0 | 0 | (-84.0000, 215.0000, -293.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.seat.x-90_z-293.c11.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.coaxial.x-90_z-293 | 0 mm | <= 0.1 | 0.1 | (-90.0000, 209.0000, -293.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-04.x-90_z-293.coaxial_with_insert | 0 mm | <= 0.1 | 0.1 | (-90.0000, 209.0000, -293.0000) mm | PASS (assumed: A-02, A-05) | A-02, A-05 |
| U-03.c05.clearance | 0.5 mm | in [0.45, 0.55] | 0.05 | (-43.0000, 210.5000, 30.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c05.clearance_without_pads | 6.4031 mm | >= 0.5 | 5.9031 | (59.0000, 215.0000, -60.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c05.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| REQ-05.x48_z30.clearance_to_c05 | 0.5 mm | in [0.45, 0.55] | 0.05 | (53.0000, 210.5000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.clearance_to_c05 | 0.5 mm | in [0.45, 0.55] | 0.05 | (-43.0000, 210.5000, 30.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.hub_r | 43.0416 mm | >= 40.0 | 3.0416 | — | PASS (assumed: A-03) | A-03 |
| REQ-05.x48_z30.to_counterbores | 33.94 mm | >= 20.0 | 13.94 | (44.0000, 210.0000, -12.0000) mm | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.hub_r | 43.0416 mm | >= 40.0 | 3.0416 | — | PASS (assumed: A-03) | A-03 |
| REQ-05.x-48_z30.to_counterbores | 33.94 mm | >= 20.0 | 13.94 | (-44.0000, 210.0000, -12.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03.c07.clearance | 167.2991 mm | >= 3.0 | 164.2991 | (-117.0000, 215.0000, -114.9500) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.plate.clearance | 210.5 mm | >= 3.0 | 207.5 | (-43.0000, 210.5000, 30.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c02.clearance_away | 14.3309 mm | >= 0.5 | 13.8309 | (70.8611, 229.3264, -208.5000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.clearance_contact | 0 mm | == 0.0 | 0 | (-110.0000, 215.0000, -302.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.clearance_away | 1 mm | >= 0.5 | 0.5 | (-95.5000, 216.0000, -301.9500) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.corner_x+.clearance | 0 mm | == 0.0 | 0 | (109.9500, 215.0000, -302.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.corner_x+.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.corner_x-.clearance | 0 mm | == 0.0 | 0 | (-109.9500, 215.0000, -302.0000) mm | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.corner_x-.interference | 0 mm3 | <= 0.0 | 0 | — | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03.c11.contact_area_outside_designed_regions | 0 mm2 | <= 0.0 | 0 | [] | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03(b).plate.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03(b).c02.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03(b).c05.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03(b).c07.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-03(b).c11.worst_interference | 0 mm3 | <= 0.0 | 0 | dy 40 | PASS (assumed: A-01, A-02, A-03) | A-01, A-02, A-03 |
| U-04.part.schema | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.part.solids | 1 count | == 1 | 0 | — | PASS | — |
| U-04.part.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.part.faces_delta | 0 count | == 0 | 0 | — | PASS | — |
| U-04.part.labels | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.part.valid_after | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.schema | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.solids | 6 count | == 6 | 0 | — | PASS | — |
| U-04.assembly.faces_delta | 0 count | == 0 | 0 | — | PASS | — |
| U-04.assembly.labels | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.valid_after | 1 bool | == 1 | 0 | — | PASS | — |
| U-04.assembly.od_c10_top.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c01_frame.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c02_bulkhead.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c05_carrier.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c07_valve_mount.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| U-04.assembly.od_c11_back.volume_delta | 0 mm3 | in [0.0, 0.0] | 0 | — | PASS | — |
| D-01a | 2.75 mm | >= 0.8 | 1.95 | (-92.9792, 247.0000, -294.2989) mm | PASS | — |
| D-01b | 2.75 mm | >= 2.0 | 0.75 | (-92.9792, 247.0000, -294.2989) mm | PASS | — |
| D-06a | 2.75 mm | >= 1.0 | 1.75 | (-92.9792, 247.0000, -294.2989) mm | PASS | — |
| U-06(Soft) | 2.75 mm | >= 2.0 | 0.75 | (-92.9792, 247.0000, -294.2989) mm | PASS | — |
| D-03a | 90 deg | >= 45.0 | 45 | — | PASS (assumed: A-08) | A-08 |
| U-07.mesh.bodies | 1 count | == 1 | 0 | — | PASS | — |
| U-07.mesh.naked_edges | 0 count | == 0 | 0 | — | PASS | — |
| U-07.mesh.winding | 1 bool | == 1 | 0 | — | PASS | — |
| U-07.angular_tolerance | 0.17 rad | <= 0.17890034867493382 | 0.0089 | — | PASS | — |
| U-07.tolerance | 0.01 mm | <= 0.01 | 0 | — | PASS | — |
| U-07.max_sagitta | 0.0054 mm | <= 0.01 | 0.0046 | (-84.4084, 215.5000, -295.1609) mm | PASS | — |
| U-07.max_sagitta_delivered | 0.0054 mm | <= 0.01 | 0.0046 | — | PASS | — |
| U-08 | — | N/A | — | — | N/A | — |
| D-05a | — | N/A | — | — | N/A | — |
| D-05b | — | N/A | — | — | N/A | — |
| D-07 | — | N/A | — | — | N/A | — |
| J-05 | — | N/A | — | — | N/A | — |
| E-06 | — | reviewer | — | — | INCONCLUSIVE | — |
| REQ-08(Soft) | — | bench | — | — | INCONCLUSIVE | A-04, A-11 |
