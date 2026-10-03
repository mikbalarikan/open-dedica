
#### od_c13_right: every predicate (131 rows)

| Gate | Measured | Unit | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | count | == 1 | 0 |  | PASS | — |
| U-01 solid_count | 1 | count | == 1 | 0 |  | PASS | — |
| U-01 brep_valid | 1 | bool | == 1 | 0 |  | PASS | — |
| U-01 naked_edges | 0 | count | == 0 | 0 |  | PASS | — |
| U-02 size_x | 10 | mm | in [9.9, 10.1] | 0.1 |  | PASS | — |
| U-02 size_y | 218.8105 | mm | in [218.71, 218.91] | 0.0995 |  | PASS | — |
| U-02 size_z | 385 | mm | in [384.9, 385.1] | 0.1 |  | PASS | — |
| envelope_within_spec size_x | 10 | mm | in [9.9, 10.1] | 0.1 |  | PASS | — |
| envelope_within_spec size_y | 218.8105 | mm | in [218.71, 218.91] | 0.0995 |  | PASS | — |
| envelope_within_spec size_z | 385 | mm | in [384.9, 385.1] | 0.1 |  | PASS | — |
| U-02 position min_x | 110 | mm | in [109.9, 110.1] | 0.1 |  | PASS | — |
| U-02 position max_x | 120 | mm | in [119.9, 120.1] | 0.1 |  | PASS | — |
| U-02 position min_y | 0 | mm | in [-0.1, 0.1] | 0.1 |  | PASS | — |
| U-02 position max_y | 218.8105 | mm | in [218.71, 218.91] | 0.0995 |  | PASS | — |
| U-02 position min_z | -295 | mm | in [-295.1, -294.9] | 0.1 |  | PASS | — |
| U-02 position max_z | 90 | mm | in [89.9, 90.1] | 0.1 |  | PASS | — |
| D-02 bed length (z) | 385 | mm | <= 420.0 | 35 |  | PASS (assumed: A-09) | A-09 |
| D-02 bed width (y) | 218.8105 | mm | <= 420.0 | 201.1895 |  | PASS (assumed: A-09) | A-09 |
| D-02 height (x) | 10 | mm | <= 500.0 | 490 |  | PASS (assumed: A-09) | A-09 |
| U-04 schema | 1 | bool | == 1 | 0 |  | PASS | — |
| U-04 solids | 1 | count | == 1 | 0 |  | PASS | — |
| U-04 volume_delta | 0 | mm3 | <= 0.0 | -0 |  | PASS | — |
| U-04 faces_delta | 0 | count | == 0 | 0 |  | PASS | — |
| U-04 labels | 1 | bool | == 1 | 0 |  | PASS | — |
| U-04 valid_after | 1 | bool | == 1 | 0 |  | PASS | — |
| U-05 plane_faces | 11 | count | == 11 | 0 |  | PASS | — |
| feature_census plane_faces | 11 | count | == 11 | 0 |  | PASS | — |
| U-05 cylinder_faces | 3 | count | == 3 | 0 |  | PASS | — |
| feature_census cylinder_faces | 3 | count | == 3 | 0 |  | PASS | — |
| U-05 cone_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census cone_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 sphere_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census sphere_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 torus_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census torus_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 bspline_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census bspline_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 other_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census other_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 concave_cylinders | 3 | count | == 3 | 0 |  | PASS | — |
| feature_census concave_cylinders | 3 | count | == 3 | 0 |  | PASS | — |
| U-05 convex_cylinders | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census convex_cylinders | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 bores | 3 | count | == 3 | 0 |  | PASS | — |
| feature_census bores | 3 | count | == 3 | 0 |  | PASS | — |
| U-05 bores along X | 3 | count | == 3 | 0 |  | PASS | — |
| D-01a | 3 | mm | >= 0.8 | 2.2 | (117.0000, 214.5023, -294.5013) mm | PASS | — |
| D-01b | 3 | mm | >= 2.0 | 1 | (117.0000, 214.5023, -294.5013) mm | PASS | — |
| D-06a | 3 | mm | >= 1.0 | 2 | (117.0000, 214.5023, -294.5013) mm | PASS | — |
| U-06 (Soft) | 3 | mm | >= 2.0 | 1 | (117.0000, 214.5023, -294.5013) mm | PASS | — |
| D-03a | 60 | deg | >= 45.0 | 15 | (116.6000, 215.0000, 80.0000) mm | PASS | — |
| REQ-02 slope (overhang_census) | 60 | deg | in [59.0, 61.0] | 1 | (116.6000, 215.0000, 80.0000) mm | PASS | — |
| D-03b (corroboration; reviewer from sections) | 0 | mm | <= 5.0 | 5 |  | PASS | — |
| REQ-03 hole z-262 diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (117.0000, 10.0000, -262.0000) mm | PASS | — |
| REQ-03 hole z-262 offset | 0 | mm | <= 0.1 | 0.1 | (117.0000, 10.0000, -262.0000) mm | PASS | — |
| REQ-03 hole z-262 through | 1 | bool | == 1 | 0 | (117.0000, 10.0000, -262.0000) mm | PASS | — |
| D-04a hole z-262 | 3.4 | mm | >= 3.25 | 0.15 | (117.0000, 10.0000, -262.0000) mm | PASS | — |
| REQ-03 hole z-15 diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (117.0000, 10.0000, -15.0000) mm | PASS | — |
| REQ-03 hole z-15 offset | 0 | mm | <= 0.1 | 0.1 | (117.0000, 10.0000, -15.0000) mm | PASS | — |
| REQ-03 hole z-15 through | 1 | bool | == 1 | 0 | (117.0000, 10.0000, -15.0000) mm | PASS | — |
| D-04a hole z-15 | 3.4 | mm | >= 3.25 | 0.15 | (117.0000, 10.0000, -15.0000) mm | PASS | — |
| REQ-03 hole z+62 diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (117.0000, 10.0000, 62.0000) mm | PASS | — |
| REQ-03 hole z+62 offset | 0 | mm | <= 0.1 | 0.1 | (117.0000, 10.0000, 62.0000) mm | PASS | — |
| REQ-03 hole z+62 through | 1 | bool | == 1 | 0 | (117.0000, 10.0000, 62.0000) mm | PASS | — |
| D-04a hole z+62 | 3.4 | mm | >= 3.25 | 0.15 | (117.0000, 10.0000, 62.0000) mm | PASS | — |
| REQ-01 outer face count | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 outer face x | 120 | mm | in [119.9, 120.1] | 0.1 |  | PASS | — |
| REQ-01 outer face z min | -295 | mm | in [-295.1, -294.9] | 0.1 |  | PASS | — |
| REQ-01 outer face z max | 90 | mm | in [89.9, 90.1] | 0.1 |  | PASS | — |
| REQ-01 section y50 z-294 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 50.0000, -294.0000) mm | PASS | — |
| REQ-01 section y50 z-294 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 50.0000, -294.0000) mm | PASS | — |
| REQ-01 section y50 z-200 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 50.0000, -200.0000) mm | PASS | — |
| REQ-01 section y50 z-200 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 50.0000, -200.0000) mm | PASS | — |
| REQ-01 section y50 z-100 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 50.0000, -100.0000) mm | PASS | — |
| REQ-01 section y50 z-100 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 50.0000, -100.0000) mm | PASS | — |
| REQ-01 section y50 z-60 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 50.0000, -60.0000) mm | PASS | — |
| REQ-01 section y50 z-60 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 50.0000, -60.0000) mm | PASS | — |
| REQ-01 section y50 z+0 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 50.0000, 0.0000) mm | PASS | — |
| REQ-01 section y50 z+0 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 50.0000, 0.0000) mm | PASS | — |
| REQ-01 section y50 z+50 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 50.0000, 50.0000) mm | PASS | — |
| REQ-01 section y50 z+50 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 50.0000, 50.0000) mm | PASS | — |
| REQ-01 section y50 z+89 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 50.0000, 89.0000) mm | PASS | — |
| REQ-01 section y50 z+89 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 50.0000, 89.0000) mm | PASS | — |
| REQ-01 section y200 z-294 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 200.0000, -294.0000) mm | PASS | — |
| REQ-01 section y200 z-294 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 200.0000, -294.0000) mm | PASS | — |
| REQ-01 section y200 z-200 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 200.0000, -200.0000) mm | PASS | — |
| REQ-01 section y200 z-200 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 200.0000, -200.0000) mm | PASS | — |
| REQ-01 section y200 z-100 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 200.0000, -100.0000) mm | PASS | — |
| REQ-01 section y200 z-100 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 200.0000, -100.0000) mm | PASS | — |
| REQ-01 section y200 z-60 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 200.0000, -60.0000) mm | PASS | — |
| REQ-01 section y200 z-60 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 200.0000, -60.0000) mm | PASS | — |
| REQ-01 section y200 z+0 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 200.0000, 0.0000) mm | PASS | — |
| REQ-01 section y200 z+0 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 200.0000, 0.0000) mm | PASS | — |
| REQ-01 section y200 z+50 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 200.0000, 50.0000) mm | PASS | — |
| REQ-01 section y200 z+50 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 200.0000, 50.0000) mm | PASS | — |
| REQ-01 section y200 z+89 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (120.0000, 200.0000, 89.0000) mm | PASS | — |
| REQ-01 section y200 z+89 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (117.0000, 200.0000, 89.0000) mm | PASS | — |
| REQ-01 underside planes | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 underside y | 0 | mm | in [-0.05, 0.05] | 0.05 |  | PASS | — |
| REQ-01 top face count | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 top face y | 215 | mm | in [214.95, 215.05] | 0.05 |  | PASS | — |
| REQ-01 top face inner x | 116.6 | mm | in [116.5, 116.69999999999999] | 0.1 |  | PASS | — |
| REQ-01 top face outer x | 120 | mm | in [119.9, 120.1] | 0.1 |  | PASS | — |
| REQ-01 rear end face count | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 rear end z | -295 | mm | in [-295.1, -294.9] | 0.1 |  | PASS | — |
| REQ-01 rear end square (rectangle 1/0) | 1 | bool | == 1 | 0 |  | PASS | — |
| REQ-01 front end face count | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 front end z | 90 | mm | in [89.9, 90.1] | 0.1 |  | PASS | — |
| REQ-01 front end square (rectangle 1/0) | 1 | bool | == 1 | 0 |  | PASS | — |
| REQ-01 footprint outside plate | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-02 sloped faces | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-02 slope from panel plane | 60 | deg | in [59.0, 61.0] | 1 |  | PASS | — |
| REQ-02 lip inner x (vertices 1, 3) | 110 | mm | in [109.9, 110.1] | 0.1 |  | PASS | — |
| REQ-02 lip outer x (vertex 2) | 116.6 | mm | in [116.5, 116.69999999999999] | 0.1 |  | PASS | — |
| REQ-02 lip base y (vertices 1, 2) | 215 | mm | in [214.9, 215.1] | 0.1 |  | PASS | — |
| REQ-02 lip apex y (vertex 3) | 218.8105 | mm | in [218.71, 218.91] | 0.0995 |  | PASS | — |
| REQ-02 lip z0 | -280 | mm | in [-280.1, -279.9] | 0.1 |  | PASS | — |
| REQ-02 lip z1 | 80 | mm | in [79.9, 80.1] | 0.1 |  | PASS | — |
| REQ-02 apex x (vertex 3) | 110 | mm | in [109.9, 110.1] | 0.1 |  | PASS | — |
| REQ-02 lip to OD-C10 | 0.4 | mm | in [0.35000000000000003, 0.45] | 0.05 | (116.6000, 215.0000, -280.0000) mm | PASS (assumed: A-02, A-14) | A-02, A-14 |
| D-04d lip to OD-C10 skirt | 0.4 | mm | >= 0.3 | 0.1 | (116.6000, 215.0000, -280.0000) mm | PASS (assumed: A-02, A-14) | A-02, A-14 |
| REQ-02 lid material in x +-(109.5..117) over the lip's zone | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-02) | A-02 |
| U-07 stl_max_sagitta | 0.005 | mm | <= 0.01 | 0.005 | (117.0000, 10.2587, -260.3249) mm | PASS | — |
| U-07 angular tolerance | 0.4341 | rad | <= 0.4340738745346826 | 0 |  | PASS | — |
| U-07 delivered STL triangles = fresh mesh | 536 | count | == 536 | 0 |  | PASS | — |
| U-07 delivered STL bodies | 1 | count | == 1 | 0 |  | PASS | — |
| U-07 delivered STL naked edges | 0 | count | == 0 | 0 |  | PASS | — |
| U-08 (no threads (row's own N/A)) | — |  |  | — |  | N/A | — |
| D-07 (no fit-critical bores (row's own N/A)) | — |  |  | — |  | N/A | — |
| E-06 | 1 | count | one solid; lip tied into rail, rail into wall (reviewer from sections) | — |  | PASS | — |
| REQ-08 (Soft, bench) (not geometric; risk MEDIUM (A-13)) | — |  | no visible flex or drumming (first print) | — |  | INCONCLUSIVE | A-13 |

#### od_c12_left: every predicate (135 rows)

| Gate | Measured | Unit | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | count | == 1 | 0 |  | PASS | — |
| U-01 solid_count | 1 | count | == 1 | 0 |  | PASS | — |
| U-01 brep_valid | 1 | bool | == 1 | 0 |  | PASS | — |
| U-01 naked_edges | 0 | count | == 0 | 0 |  | PASS | — |
| U-02 size_x | 10 | mm | in [9.9, 10.1] | 0.1 |  | PASS | — |
| U-02 size_y | 218.8105 | mm | in [218.71, 218.91] | 0.0995 |  | PASS | — |
| U-02 size_z | 385 | mm | in [384.9, 385.1] | 0.1 |  | PASS | — |
| envelope_within_spec size_x | 10 | mm | in [9.9, 10.1] | 0.1 |  | PASS | — |
| envelope_within_spec size_y | 218.8105 | mm | in [218.71, 218.91] | 0.0995 |  | PASS | — |
| envelope_within_spec size_z | 385 | mm | in [384.9, 385.1] | 0.1 |  | PASS | — |
| U-02 position min_x | -120 | mm | in [-120.1, -119.9] | 0.1 |  | PASS | — |
| U-02 position max_x | -110 | mm | in [-110.1, -109.9] | 0.1 |  | PASS | — |
| U-02 position min_y | 0 | mm | in [-0.1, 0.1] | 0.1 |  | PASS | — |
| U-02 position max_y | 218.8105 | mm | in [218.71, 218.91] | 0.0995 |  | PASS | — |
| U-02 position min_z | -295 | mm | in [-295.1, -294.9] | 0.1 |  | PASS | — |
| U-02 position max_z | 90 | mm | in [89.9, 90.1] | 0.1 |  | PASS | — |
| D-02 bed length (z) | 385 | mm | <= 420.0 | 35 |  | PASS (assumed: A-09) | A-09 |
| D-02 bed width (y) | 218.8105 | mm | <= 420.0 | 201.1895 |  | PASS (assumed: A-09) | A-09 |
| D-02 height (x) | 10 | mm | <= 500.0 | 490 |  | PASS (assumed: A-09) | A-09 |
| U-04 schema | 1 | bool | == 1 | 0 |  | PASS | — |
| U-04 solids | 1 | count | == 1 | 0 |  | PASS | — |
| U-04 volume_delta | 0 | mm3 | <= 0.0 | -0 |  | PASS | — |
| U-04 faces_delta | 0 | count | == 0 | 0 |  | PASS | — |
| U-04 labels | 1 | bool | == 1 | 0 |  | PASS | — |
| U-04 valid_after | 1 | bool | == 1 | 0 |  | PASS | — |
| U-05 plane_faces | 15 | count | == 15 | 0 |  | PASS | — |
| feature_census plane_faces | 15 | count | == 15 | 0 |  | PASS | — |
| U-05 cylinder_faces | 3 | count | == 3 | 0 |  | PASS | — |
| feature_census cylinder_faces | 3 | count | == 3 | 0 |  | PASS | — |
| U-05 cone_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census cone_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 sphere_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census sphere_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 torus_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census torus_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 bspline_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census bspline_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 other_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census other_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 concave_cylinders | 3 | count | == 3 | 0 |  | PASS | — |
| feature_census concave_cylinders | 3 | count | == 3 | 0 |  | PASS | — |
| U-05 convex_cylinders | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census convex_cylinders | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 bores | 3 | count | == 3 | 0 |  | PASS | — |
| feature_census bores | 3 | count | == 3 | 0 |  | PASS | — |
| U-05 bores along X | 3 | count | == 3 | 0 |  | PASS | — |
| D-01a | 2.1 | mm | >= 0.8 | 1.3 | (-120.0000, 54.2477, -29.1904) mm | PASS | — |
| D-01b | 2.1 | mm | >= 2.0 | 0.1 | (-120.0000, 54.2477, -29.1904) mm | PASS | — |
| D-06a | 2.1 | mm | >= 1.0 | 1.1 | (-120.0000, 54.2477, -29.1904) mm | PASS | — |
| U-06 (Soft) | 2.1 | mm | >= 2.0 | 0.1 | (-120.0000, 54.2477, -29.1904) mm | PASS | — |
| D-03a | 60 | deg | >= 45.0 | 15 | (-110.0000, 218.8105, 80.0000) mm | PASS | — |
| REQ-02 slope (overhang_census) | 60 | deg | in [59.0, 61.0] | 1 | (-110.0000, 218.8105, 80.0000) mm | PASS | — |
| D-03b (corroboration; reviewer from sections) | 0 | mm | <= 5.0 | 5 |  | PASS | — |
| REQ-03 hole z-262 diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-120.0000, 10.0000, -262.0000) mm | PASS | — |
| REQ-03 hole z-262 offset | 0 | mm | <= 0.1 | 0.1 | (-120.0000, 10.0000, -262.0000) mm | PASS | — |
| REQ-03 hole z-262 through | 1 | bool | == 1 | 0 | (-120.0000, 10.0000, -262.0000) mm | PASS | — |
| D-04a hole z-262 | 3.4 | mm | >= 3.25 | 0.15 | (-120.0000, 10.0000, -262.0000) mm | PASS | — |
| REQ-03 hole z-15 diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-120.0000, 10.0000, -15.0000) mm | PASS | — |
| REQ-03 hole z-15 offset | 0 | mm | <= 0.1 | 0.1 | (-120.0000, 10.0000, -15.0000) mm | PASS | — |
| REQ-03 hole z-15 through | 1 | bool | == 1 | 0 | (-120.0000, 10.0000, -15.0000) mm | PASS | — |
| D-04a hole z-15 | 3.4 | mm | >= 3.25 | 0.15 | (-120.0000, 10.0000, -15.0000) mm | PASS | — |
| REQ-03 hole z+62 diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-120.0000, 10.0000, 62.0000) mm | PASS | — |
| REQ-03 hole z+62 offset | 0 | mm | <= 0.1 | 0.1 | (-120.0000, 10.0000, 62.0000) mm | PASS | — |
| REQ-03 hole z+62 through | 1 | bool | == 1 | 0 | (-120.0000, 10.0000, 62.0000) mm | PASS | — |
| D-04a hole z+62 | 3.4 | mm | >= 3.25 | 0.15 | (-120.0000, 10.0000, 62.0000) mm | PASS | — |
| REQ-01 outer face count | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 outer face x | -120 | mm | in [-120.1, -119.9] | 0.1 |  | PASS | — |
| REQ-01 outer face z min | -295 | mm | in [-295.1, -294.9] | 0.1 |  | PASS | — |
| REQ-01 outer face z max | 90 | mm | in [89.9, 90.1] | 0.1 |  | PASS | — |
| REQ-01 section y50 z-294 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 50.0000, -294.0000) mm | PASS | — |
| REQ-01 section y50 z-294 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 50.0000, -294.0000) mm | PASS | — |
| REQ-01 section y50 z-200 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 50.0000, -200.0000) mm | PASS | — |
| REQ-01 section y50 z-200 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 50.0000, -200.0000) mm | PASS | — |
| REQ-01 section y50 z+0 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 50.0000, 0.0000) mm | PASS | — |
| REQ-01 section y50 z+0 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 50.0000, 0.0000) mm | PASS | — |
| REQ-01 section y50 z+50 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 50.0000, 50.0000) mm | PASS | — |
| REQ-01 section y50 z+50 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 50.0000, 50.0000) mm | PASS | — |
| REQ-01 section y50 z+89 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 50.0000, 89.0000) mm | PASS | — |
| REQ-01 section y50 z+89 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 50.0000, 89.0000) mm | PASS | — |
| REQ-01 section y200 z-294 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 200.0000, -294.0000) mm | PASS | — |
| REQ-01 section y200 z-294 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 200.0000, -294.0000) mm | PASS | — |
| REQ-01 section y200 z-200 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 200.0000, -200.0000) mm | PASS | — |
| REQ-01 section y200 z-200 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 200.0000, -200.0000) mm | PASS | — |
| REQ-01 section y200 z-100 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 200.0000, -100.0000) mm | PASS | — |
| REQ-01 section y200 z-100 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 200.0000, -100.0000) mm | PASS | — |
| REQ-01 section y200 z-60 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 200.0000, -60.0000) mm | PASS | — |
| REQ-01 section y200 z-60 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 200.0000, -60.0000) mm | PASS | — |
| REQ-01 section y200 z+0 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 200.0000, 0.0000) mm | PASS | — |
| REQ-01 section y200 z+0 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 200.0000, 0.0000) mm | PASS | — |
| REQ-01 section y200 z+50 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 200.0000, 50.0000) mm | PASS | — |
| REQ-01 section y200 z+50 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 200.0000, 50.0000) mm | PASS | — |
| REQ-01 section y200 z+89 outer | 120 | mm | in [119.9, 120.1] | 0.1 | (-120.0000, 200.0000, 89.0000) mm | PASS | — |
| REQ-01 section y200 z+89 inner | 117 | mm | in [116.9, 117.1] | 0.1 | (-117.0000, 200.0000, 89.0000) mm | PASS | — |
| REQ-01 underside planes | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 underside y | 0 | mm | in [-0.05, 0.05] | 0.05 |  | PASS | — |
| REQ-01 top face count | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 top face y | 215 | mm | in [214.95, 215.05] | 0.05 |  | PASS | — |
| REQ-01 top face inner x | 116.6 | mm | in [116.5, 116.69999999999999] | 0.1 |  | PASS | — |
| REQ-01 top face outer x | 120 | mm | in [119.9, 120.1] | 0.1 |  | PASS | — |
| REQ-01 rear end face count | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 rear end z | -295 | mm | in [-295.1, -294.9] | 0.1 |  | PASS | — |
| REQ-01 rear end square (rectangle 1/0) | 1 | bool | == 1 | 0 |  | PASS | — |
| REQ-01 front end face count | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-01 front end z | 90 | mm | in [89.9, 90.1] | 0.1 |  | PASS | — |
| REQ-01 front end square (rectangle 1/0) | 1 | bool | == 1 | 0 |  | PASS | — |
| REQ-01 footprint outside plate | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-02 sloped faces | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-02 slope from panel plane | 60 | deg | in [59.0, 61.0] | 1 |  | PASS | — |
| REQ-02 lip inner x (vertices 1, 3) | 110 | mm | in [109.9, 110.1] | 0.1 |  | PASS | — |
| REQ-02 lip outer x (vertex 2) | 116.6 | mm | in [116.5, 116.69999999999999] | 0.1 |  | PASS | — |
| REQ-02 lip base y (vertices 1, 2) | 215 | mm | in [214.9, 215.1] | 0.1 |  | PASS | — |
| REQ-02 lip apex y (vertex 3) | 218.8105 | mm | in [218.71, 218.91] | 0.0995 |  | PASS | — |
| REQ-02 lip z0 | -280 | mm | in [-280.1, -279.9] | 0.1 |  | PASS | — |
| REQ-02 lip z1 | 80 | mm | in [79.9, 80.1] | 0.1 |  | PASS | — |
| REQ-02 apex x (vertex 3) | 110 | mm | in [109.9, 110.1] | 0.1 |  | PASS | — |
| REQ-02 lip to OD-C10 | 0.4 | mm | in [0.35000000000000003, 0.45] | 0.05 | (-116.6000, 215.0000, -280.0000) mm | PASS (assumed: A-02, A-14) | A-02, A-14 |
| D-04d lip to OD-C10 skirt | 0.4 | mm | >= 0.3 | 0.1 | (-116.6000, 215.0000, -280.0000) mm | PASS (assumed: A-02, A-14) | A-02, A-14 |
| REQ-02 lid material in x +-(109.5..117) over the lip's zone | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-02) | A-02 |
| U-07 stl_max_sagitta | 0.005 | mm | <= 0.01 | 0.005 | (-117.0000, 9.7413, -260.3249) mm | PASS | — |
| U-07 angular tolerance | 0.4341 | rad | <= 0.4340738745346826 | 0 |  | PASS | — |
| U-07 delivered STL triangles = fresh mesh | 552 | count | == 552 | 0 |  | PASS | — |
| U-07 delivered STL bodies | 1 | count | == 1 | 0 |  | PASS | — |
| U-07 delivered STL naked edges | 0 | count | == 0 | 0 |  | PASS | — |
| U-08 (no threads (row's own N/A)) | — |  |  | — |  | N/A | — |
| D-07 (no fit-critical bores (row's own N/A)) | — |  |  | — |  | N/A | — |
| E-06 | 1 | count | one solid; lip tied into rail, rail into wall (reviewer from sections) | — |  | PASS | — |
| REQ-08 (Soft, bench) (not geometric; risk MEDIUM (A-13)) | — |  | no visible flex or drumming (first print) | — |  | INCONCLUSIVE | A-13 |
| REQ-04 relief floor faces | 1 | count | == 1 | 0 |  | PASS | — |
| REQ-04 relief floor x | -117.9 | mm | in [-117.95, -117.85000000000001] | 0.05 |  | PASS (assumed: A-04) | A-04 |
| REQ-04 relief y0 | 0 | mm | in [-0.1, 0.1] | 0.1 |  | PASS | — |
| REQ-04 relief y1 | 55 | mm | in [54.9, 55.1] | 0.1 |  | PASS | — |
| REQ-04 relief z0 | -160 | mm | in [-160.1, -159.9] | 0.1 |  | PASS | — |
| REQ-04 relief z1 | -29 | mm | in [-29.1, -28.9] | 0.1 |  | PASS | — |
| REQ-04 wall at the relief (info for D-01b) | 2.1 | mm | >= 2.0 | 0.1 |  | PASS | — |
| REQ-04 clearance OD-C12 to OD-C07 | 0.9 | mm | >= 0.5 | 0.4 | (-117.9000, 0.0000, -100.0000) mm | PASS (assumed: A-04) | A-04 |

#### od_c16_bracket: every predicate (85 rows)

| Gate | Measured | Unit | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|---|
| exactly_one_solid | 1 | count | == 1 | 0 |  | PASS | — |
| U-01 solid_count | 1 | count | == 1 | 0 |  | PASS | — |
| U-01 brep_valid | 1 | bool | == 1 | 0 |  | PASS | — |
| U-01 naked_edges | 0 | count | == 0 | 0 |  | PASS | — |
| U-02 size_x | 19 | mm | in [18.9, 19.1] | 0.1 |  | PASS | — |
| U-02 size_y | 16 | mm | in [15.9, 16.1] | 0.1 |  | PASS | — |
| U-02 size_z | 16 | mm | in [15.9, 16.1] | 0.1 |  | PASS | — |
| envelope_within_spec size_x | 19 | mm | in [18.9, 19.1] | 0.1 |  | PASS | — |
| envelope_within_spec size_y | 16 | mm | in [15.9, 16.1] | 0.1 |  | PASS | — |
| envelope_within_spec size_z | 16 | mm | in [15.9, 16.1] | 0.1 |  | PASS | — |
| REQ-05 block size_x | 19 | mm | in [18.9, 19.1] | 0.1 |  | PASS | — |
| REQ-05 block size_y | 16 | mm | in [15.9, 16.1] | 0.1 |  | PASS | — |
| REQ-05 block size_z | 16 | mm | in [15.9, 16.1] | 0.1 |  | PASS | — |
| U-02 position min_x | -19 | mm | in [-19.1, -18.9] | 0.1 |  | PASS | — |
| U-02 position max_x | 0 | mm | in [-0.1, 0.1] | 0.1 |  | PASS | — |
| U-02 position min_y | -0 | mm | in [-0.1, 0.1] | 0.1 |  | PASS | — |
| U-02 position max_y | 16 | mm | in [15.9, 16.1] | 0.1 |  | PASS | — |
| U-02 position min_z | -8 | mm | in [-8.1, -7.9] | 0.1 |  | PASS | — |
| U-02 position max_z | 8 | mm | in [7.9, 8.1] | 0.1 |  | PASS | — |
| D-02 size_x | 19 | mm | <= 220.0 | 201 |  | PASS (assumed: A-10) | A-10 |
| D-02 size_y | 16 | mm | <= 220.0 | 204 |  | PASS (assumed: A-10) | A-10 |
| D-02 size_z | 16 | mm | <= 250.0 | 234 |  | PASS (assumed: A-10) | A-10 |
| U-04 schema | 1 | bool | == 1 | 0 |  | PASS | — |
| U-04 solids | 1 | count | == 1 | 0 |  | PASS | — |
| U-04 volume_delta | 0 | mm3 | <= 0.0 | -0 |  | PASS | — |
| U-04 faces_delta | 0 | count | == 0 | 0 |  | PASS | — |
| U-04 labels | 1 | bool | == 1 | 0 |  | PASS | — |
| U-04 valid_after | 1 | bool | == 1 | 0 |  | PASS | — |
| U-05 plane_faces | 8 | count | == 8 | 0 |  | PASS | — |
| feature_census plane_faces | 8 | count | == 8 | 0 |  | PASS | — |
| U-05 cylinder_faces | 3 | count | == 3 | 0 |  | PASS | — |
| feature_census cylinder_faces | 3 | count | == 3 | 0 |  | PASS | — |
| U-05 cone_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census cone_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 sphere_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census sphere_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 torus_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census torus_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 bspline_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census bspline_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 other_faces | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census other_faces | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 concave_cylinders | 3 | count | == 3 | 0 |  | PASS | — |
| feature_census concave_cylinders | 3 | count | == 3 | 0 |  | PASS | — |
| U-05 convex_cylinders | 0 | count | == 0 | 0 |  | PASS | — |
| feature_census convex_cylinders | 0 | count | == 0 | 0 |  | PASS | — |
| U-05 bores | 3 | count | == 3 | 0 |  | PASS | — |
| feature_census bores | 3 | count | == 3 | 0 |  | PASS | — |
| D-01a | 3 | mm | >= 0.8 | 2.2 | (-13.4028, 3.0000, -3.0694) mm | PASS | — |
| D-01b | 3 | mm | >= 2.0 | 1 | (-13.4028, 3.0000, -3.0694) mm | PASS | — |
| D-06a | 3 | mm | >= 1.0 | 2 | (-13.4028, 3.0000, -3.0694) mm | PASS | — |
| U-06 (Soft) | 3 | mm | >= 2.0 | 1 | (-13.4028, 3.0000, -3.0694) mm | PASS | — |
| REQ-05 hole diameter | 3.4 | mm | in [3.3, 3.5] | 0.1 | (-12.5000, 0.0000, 0.0000) mm | PASS | — |
| REQ-05 hole offset | 0 | mm | <= 0.1 | 0.1 | (-12.5000, 0.0000, 0.0000) mm | PASS | — |
| REQ-05 hole through | 1 | bool | == 1 | 0 | (-12.5000, 0.0000, 0.0000) mm | PASS | — |
| D-04a hole diameter | 3.4 | mm | >= 3.25 | 0.15 | (-12.5000, 0.0000, 0.0000) mm | PASS | — |
| REQ-05 counterbore diameter | 6.5 | mm | in [6.4, 6.6] | 0.1 |  | PASS | — |
| REQ-05 counterbore floor y | 3 | mm | in [2.9, 3.1] | 0.1 |  | PASS | — |
| REQ-05 counterbore opens at y 16 | 16 | mm | in [15.9, 16.1] | 0.1 |  | PASS | — |
| REQ-05 counterbore floor closed (1 = closed) | 1 | bool | == 1 | 0 |  | PASS | — |
| REQ-05 counterbore offset | 0 | mm | <= 0.1 | 0.1 |  | PASS | — |
| D-05b insert bore diameter | 4 | mm | in [3.95, 4.05] | 0.05 | (-6.0000, 10.0000, -0.0000) mm | PASS (assumed: A-12) | A-12 |
| D-05b insert bore depth | 6 | mm | in [5.9, 6.1] | 0.1 | (-6.0000, 10.0000, -0.0000) mm | PASS (assumed: A-12) | A-12 |
| D-05b insert bore depth >= insert | 6 | mm | >= 5.7 | 0.3 | (-6.0000, 10.0000, -0.0000) mm | PASS (assumed: A-12) | A-12 |
| D-05b insert bore blind (through = 0) | 0 | bool | == 0 | 0 | (-6.0000, 10.0000, -0.0000) mm | PASS | — |
| REQ-05 insert bore offset | 0 | mm | <= 0.1 | 0.1 | (-6.0000, 10.0000, -0.0000) mm | PASS | — |
| REQ-05 insert bore opens at x 0 | 0 | mm | in [-0.1, 0.1] | 0.1 |  | PASS | — |
| REQ-05 insert bore mouth open (1/0) | 1 | bool | == 1 | 0 |  | PASS | — |
| D-05a material across the insert bore | 12 | mm | >= 8.0 | 4 | (-0.0220, 16.0000, 0.0000) mm | PASS (assumed: A-12) | A-12 |
| J-05 radial wall around the insert bore | 4 | mm | >= 3.0 | 1 | (-0.0220, 16.0000, 0.0000) mm | PASS | — |
| J-05 axial web, insert-bore floor to counterbore | 3.25 | mm | >= 3.0 | 0.25 |  | PASS | — |
| D-03a planes (every face but the insert bore) | 90 | deg | >= 45.0 | 45 |  | PASS | — |
| D-03a cylinders not along Y = the insert bore only | 1 | count | == 1 | 0 |  | PASS | — |
| D-03a exception: insert-bore crown least angle (named exception (spec 5, Usta U-18); at (-6.0, 12.0, 0.0); per kind {'cylinder': 0.0}) | 0 | deg |  | — |  | INFO | — |
| D-03b flat ceilings (corroboration) | 0 | mm | <= 5.0 | 5 |  | PASS | — |
| D-03b insert-bore crown bridge (its diameter; reviewer from sections) | 4 | mm | <= 5.0 | 1 |  | PASS (assumed: A-11) | A-11 |
| U-07 stl_max_sagitta | 0.005 | mm | <= 0.01 | 0.005 | (-10.8100, 0.7500, 0.1298) mm | PASS | — |
| U-07 angular tolerance | 0.3139 | rad | <= 0.31386632987537666 | 0 |  | PASS | — |
| U-07 delivered STL triangles = fresh mesh | 588 | count | == 588 | 0 |  | PASS | — |
| U-07 delivered STL bodies | 1 | count | == 1 | 0 |  | PASS | — |
| U-07 delivered STL naked edges | 0 | count | == 0 | 0 |  | PASS | — |
| U-08 (no threads (row's own N/A)) | — |  |  | — |  | N/A | — |
| D-07 (no fit-critical bores (row's own N/A)) | — |  |  | — |  | N/A | — |
| E-06 | 1 | count | the bracket is one solid block (reviewer from sections) | — |  | PASS | — |
| J-05 global min_wall (beside, never instead) (at (-13.402778, 3.0, -3.069444)) | 3 | mm |  | — |  | INFO | — |

#### od_side_assembly: every predicate (199 rows)

| Gate | Measured | Unit | Required | Margin | At | Status | Assumes |
|---|---|---|---|---|---|---|---|
| assembly labels match the placements | 1 | bool | == 1 | 0 |  | PASS | — |
| assembly solids = placed part files (max centre / volume delta) | 0 | mm | <= 0.0 | -0 |  | PASS | — |
| assembly: one solid per label | 0 | count | == 0 | 0 |  | PASS | — |
| assembly solid count | 19 | count | == 19 | 0 |  | PASS | — |
| U-03a contact od_c13_right/OD-C01 clearance | 0 | mm | == 0.0 | 0 | (120.0000, 0.0000, 90.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03a contact od_c13_right/OD-C01 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c13_right/OD-C02 clearance | 39.5 | mm | >= 0.5 | 39 | (110.0000, 207.0000, -240.0000) mm | PASS | — |
| U-03a od_c13_right/OD-C05 clearance | 55 | mm | >= 0.5 | 54.5 | (110.0000, 205.0000, 80.0000) mm | PASS | — |
| U-03a od_c13_right/OD-C07 clearance | 184 | mm | >= 0.5 | 183.5 | (117.0000, 0.0000, -100.0000) mm | PASS (assumed: A-04) | A-04 |
| U-03a od_c13_right/OD-C08 clearance | 5 | mm | >= 0.5 | 4.5 | (117.0000, 0.0000, -70.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03a contact od_c13_right/OD-C10 clearance | 0 | mm | == 0.0 | 0 | (117.0000, 215.0000, 90.0000) mm | PASS (assumed: A-02) | A-02 |
| U-03a contact od_c13_right/OD-C10 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c13_right/OD-C11 clearance | 3 | mm | >= 0.5 | 2.5 | (117.0000, 215.0000, -295.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03a od_c13_right/OD-C15-RF clearance | 6 | mm | >= 0.5 | 5.5 | (118.7100, 0.0000, 90.0000) mm | PASS | — |
| U-03a od_c13_right/OD-C15-LF clearance | 218.0969 | mm | >= 0.5 | 217.5969 | (117.0000, 0.0000, 90.0000) mm | PASS | — |
| U-03a od_c13_right/OD-C15-RR clearance | 6 | mm | >= 0.5 | 5.5 | (118.7100, 0.0000, -295.0000) mm | PASS | — |
| U-03a od_c13_right/OD-C15-LR clearance | 218.0969 | mm | >= 0.5 | 217.5969 | (117.0000, 0.0000, -295.0000) mm | PASS | — |
| U-03a od_c13_right/od_c12_left clearance | 220 | mm | >= 0.5 | 219.5 | (110.0000, 205.0000, 80.0000) mm | PASS | — |
| U-03a contact od_c13_right/od_c16_bracket_R1 clearance | 0 | mm | == 0.0 | 0 | (117.0000, 0.0000, -270.0000) mm | PASS | — |
| U-03a contact od_c13_right/od_c16_bracket_R1 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c13_right/od_c16_bracket_L1 clearance | 215 | mm | >= 0.5 | 214.5 | (117.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a contact od_c13_right/od_c16_bracket_R2 clearance | 0 | mm | == 0.0 | 0 | (117.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a contact od_c13_right/od_c16_bracket_R2 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c13_right/od_c16_bracket_L2 clearance | 215 | mm | >= 0.5 | 214.5 | (117.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a contact od_c13_right/od_c16_bracket_R3 clearance | 0 | mm | == 0.0 | 0 | (117.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a contact od_c13_right/od_c16_bracket_R3 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c13_right/od_c16_bracket_L3 clearance | 215 | mm | >= 0.5 | 214.5 | (117.0000, 0.0000, 70.0000) mm | PASS | — |
| U-03a contact od_c12_left/OD-C01 clearance | 0 | mm | == 0.0 | 0 | (-120.0000, 0.0000, -295.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03a contact od_c12_left/OD-C01 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c12_left/OD-C02 clearance | 169.5 | mm | >= 0.5 | 169 | (-110.0000, 215.0000, -240.0000) mm | PASS | — |
| U-03a od_c12_left/OD-C05 clearance | 55 | mm | >= 0.5 | 54.5 | (-110.0000, 205.0000, 80.0000) mm | PASS | — |
| U-03a od_c12_left/OD-C07 clearance | 0.9 | mm | >= 0.5 | 0.4 | (-117.9000, 0.0000, -100.0000) mm | PASS (assumed: A-04) | A-04 |
| U-03a od_c12_left/OD-C08 clearance | 190 | mm | >= 0.5 | 189.5 | (-117.0000, 0.0000, -160.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03a contact od_c12_left/OD-C10 clearance | 0 | mm | == 0.0 | 0 | (-117.0000, 215.0000, 90.0000) mm | PASS (assumed: A-02) | A-02 |
| U-03a contact od_c12_left/OD-C10 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c12_left/OD-C11 clearance | 3 | mm | >= 0.5 | 2.5 | (-117.0000, 215.0000, -295.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03a od_c12_left/OD-C15-RF clearance | 218.0969 | mm | >= 0.5 | 217.5969 | (-117.0000, 0.0000, 90.0000) mm | PASS | — |
| U-03a od_c12_left/OD-C15-LF clearance | 6 | mm | >= 0.5 | 5.5 | (-117.0000, 0.0000, 90.0000) mm | PASS | — |
| U-03a od_c12_left/OD-C15-RR clearance | 218.0969 | mm | >= 0.5 | 217.5969 | (-117.0000, 0.0000, -295.0000) mm | PASS | — |
| U-03a od_c12_left/OD-C15-LR clearance | 6 | mm | >= 0.5 | 5.5 | (-117.0000, 0.0000, -295.0000) mm | PASS | — |
| U-03a od_c12_left/od_c16_bracket_R1 clearance | 215 | mm | >= 0.5 | 214.5 | (-117.0000, 0.0000, -270.0000) mm | PASS | — |
| U-03a contact od_c12_left/od_c16_bracket_L1 clearance | 0 | mm | == 0.0 | 0 | (-117.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a contact od_c12_left/od_c16_bracket_L1 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c12_left/od_c16_bracket_R2 clearance | 215 | mm | >= 0.5 | 214.5 | (-117.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a contact od_c12_left/od_c16_bracket_L2 clearance | 0 | mm | == 0.0 | 0 | (-117.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a contact od_c12_left/od_c16_bracket_L2 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c12_left/od_c16_bracket_R3 clearance | 215 | mm | >= 0.5 | 214.5 | (-117.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a contact od_c12_left/od_c16_bracket_L3 clearance | 0 | mm | == 0.0 | 0 | (-117.0000, 0.0000, 70.0000) mm | PASS | — |
| U-03a contact od_c12_left/od_c16_bracket_L3 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a contact od_c16_bracket_R1/OD-C01 clearance | 0 | mm | == 0.0 | 0 | (98.0000, 0.0000, -270.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03a contact od_c16_bracket_R1/OD-C01 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c16_bracket_R1/OD-C02 clearance | 30.4138 | mm | >= 0.5 | 29.9138 | (98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/OD-C05 clearance | 188.9577 | mm | >= 0.5 | 188.4577 | (98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/OD-C07 clearance | 192.9378 | mm | >= 0.5 | 192.4378 | (98.0000, 0.0000, -254.0000) mm | PASS (assumed: A-04) | A-04 |
| U-03a od_c16_bracket_R1/OD-C08 clearance | 24 | mm | >= 0.5 | 23.5 | (98.0000, 0.0000, -254.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03a od_c16_bracket_R1/OD-C10 clearance | 199 | mm | >= 0.5 | 198.5 | (117.0000, 16.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/OD-C11 clearance | 7 | mm | >= 0.5 | 6.5 | (98.0000, 0.0000, -270.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03a od_c16_bracket_R1/OD-C15-RF clearance | 335.0631 | mm | >= 0.5 | 334.5631 | (110.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/OD-C15-LF clearance | 393.0488 | mm | >= 0.5 | 392.5488 | (98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/OD-C15-RR clearance | 17.2699 | mm | >= 0.5 | 16.7699 | (110.0000, 0.0000, -270.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/OD-C15-LR clearance | 200.6024 | mm | >= 0.5 | 200.1024 | (98.0000, 0.0000, -270.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/od_c16_bracket_L1 clearance | 196 | mm | >= 0.5 | 195.5 | (98.0000, 0.0000, -270.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/od_c16_bracket_R2 clearance | 231 | mm | >= 0.5 | 230.5 | (98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/od_c16_bracket_L2 clearance | 302.9472 | mm | >= 0.5 | 302.4472 | (98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/od_c16_bracket_R3 clearance | 308 | mm | >= 0.5 | 307.5 | (98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_R1/od_c16_bracket_L3 clearance | 365.0753 | mm | >= 0.5 | 364.5753 | (98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a contact od_c16_bracket_L1/OD-C01 clearance | 0 | mm | == 0.0 | 0 | (-98.0000, 0.0000, -254.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03a contact od_c16_bracket_L1/OD-C01 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c16_bracket_L1/OD-C02 clearance | 157.623 | mm | >= 0.5 | 157.123 | (-98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/OD-C05 clearance | 188.9577 | mm | >= 0.5 | 188.4577 | (-98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/OD-C07 clearance | 100 | mm | >= 0.5 | 99.5 | (-117.0000, 0.0000, -254.0000) mm | PASS (assumed: A-04) | A-04 |
| U-03a od_c16_bracket_L1/OD-C08 clearance | 172.676 | mm | >= 0.5 | 172.176 | (-98.0000, 0.0000, -254.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03a od_c16_bracket_L1/OD-C10 clearance | 199 | mm | >= 0.5 | 198.5 | (-117.0000, 16.0000, -270.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/OD-C11 clearance | 7 | mm | >= 0.5 | 6.5 | (-98.0000, 0.0000, -270.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03a od_c16_bracket_L1/OD-C15-RF clearance | 393.0488 | mm | >= 0.5 | 392.5488 | (-98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/OD-C15-LF clearance | 335.0631 | mm | >= 0.5 | 334.5631 | (-110.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/OD-C15-RR clearance | 200.6024 | mm | >= 0.5 | 200.1024 | (-98.0000, 0.0000, -270.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/OD-C15-LR clearance | 17.2699 | mm | >= 0.5 | 16.7699 | (-110.0000, 0.0000, -270.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/od_c16_bracket_R2 clearance | 302.9472 | mm | >= 0.5 | 302.4472 | (-98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/od_c16_bracket_L2 clearance | 231 | mm | >= 0.5 | 230.5 | (-98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/od_c16_bracket_R3 clearance | 365.0753 | mm | >= 0.5 | 364.5753 | (-98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a od_c16_bracket_L1/od_c16_bracket_L3 clearance | 308 | mm | >= 0.5 | 307.5 | (-98.0000, 0.0000, -254.0000) mm | PASS | — |
| U-03a contact od_c16_bracket_R2/OD-C01 clearance | 0 | mm | == 0.0 | 0 | (98.0000, 0.0000, -23.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03a contact od_c16_bracket_R2/OD-C01 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c16_bracket_R2/OD-C02 clearance | 27.8927 | mm | >= 0.5 | 27.3927 | (98.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_R2/OD-C05 clearance | 43 | mm | >= 0.5 | 42.5 | (98.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_R2/OD-C07 clearance | 165.4358 | mm | >= 0.5 | 164.9358 | (98.0000, 0.0000, -23.0000) mm | PASS (assumed: A-04) | A-04 |
| U-03a od_c16_bracket_R2/OD-C08 clearance | 47 | mm | >= 0.5 | 46.5 | (98.0000, 0.0000, -23.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03a od_c16_bracket_R2/OD-C10 clearance | 199 | mm | >= 0.5 | 198.5 | (117.0000, 16.0000, -7.0000) mm | PASS | — |
| U-03a od_c16_bracket_R2/OD-C11 clearance | 254 | mm | >= 0.5 | 253.5 | (98.0000, 0.0000, -23.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03a od_c16_bracket_R2/OD-C15-RF clearance | 88.2397 | mm | >= 0.5 | 87.7397 | (110.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a od_c16_bracket_R2/OD-C15-LF clearance | 220.6018 | mm | >= 0.5 | 220.1018 | (98.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a od_c16_bracket_R2/OD-C15-RR clearance | 263.0803 | mm | >= 0.5 | 262.5803 | (110.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_R2/OD-C15-LR clearance | 333.4783 | mm | >= 0.5 | 332.9783 | (98.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_R2/od_c16_bracket_L2 clearance | 196 | mm | >= 0.5 | 195.5 | (98.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_R2/od_c16_bracket_R3 clearance | 61 | mm | >= 0.5 | 60.5 | (98.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a od_c16_bracket_R2/od_c16_bracket_L3 clearance | 205.273 | mm | >= 0.5 | 204.773 | (98.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a contact od_c16_bracket_L2/OD-C01 clearance | 0 | mm | == 0.0 | 0 | (-98.0000, 0.0000, -7.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03a contact od_c16_bracket_L2/OD-C01 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c16_bracket_L2/OD-C02 clearance | 157.156 | mm | >= 0.5 | 156.656 | (-98.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_L2/OD-C05 clearance | 43 | mm | >= 0.5 | 42.5 | (-98.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_L2/OD-C07 clearance | 12 | mm | >= 0.5 | 11.5 | (-117.0000, 0.0000, -23.0000) mm | PASS (assumed: A-04) | A-04 |
| U-03a od_c16_bracket_L2/OD-C08 clearance | 177.3415 | mm | >= 0.5 | 176.8415 | (-98.0000, 0.0000, -23.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03a od_c16_bracket_L2/OD-C10 clearance | 199 | mm | >= 0.5 | 198.5 | (-117.0000, 16.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_L2/OD-C11 clearance | 254 | mm | >= 0.5 | 253.5 | (-98.0000, 0.0000, -23.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03a od_c16_bracket_L2/OD-C15-RF clearance | 220.6018 | mm | >= 0.5 | 220.1018 | (-98.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a od_c16_bracket_L2/OD-C15-LF clearance | 88.2397 | mm | >= 0.5 | 87.7397 | (-110.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a od_c16_bracket_L2/OD-C15-RR clearance | 333.4783 | mm | >= 0.5 | 332.9783 | (-98.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_L2/OD-C15-LR clearance | 263.0803 | mm | >= 0.5 | 262.5803 | (-110.0000, 0.0000, -23.0000) mm | PASS | — |
| U-03a od_c16_bracket_L2/od_c16_bracket_R3 clearance | 205.273 | mm | >= 0.5 | 204.773 | (-98.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a od_c16_bracket_L2/od_c16_bracket_L3 clearance | 61 | mm | >= 0.5 | 60.5 | (-98.0000, 0.0000, -7.0000) mm | PASS | — |
| U-03a contact od_c16_bracket_R3/OD-C01 clearance | 0 | mm | == 0.0 | 0 | (98.0000, 0.0000, 54.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03a contact od_c16_bracket_R3/OD-C01 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c16_bracket_R3/OD-C02 clearance | 88.2326 | mm | >= 0.5 | 87.7326 | (98.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a od_c16_bracket_R3/OD-C05 clearance | 85.5862 | mm | >= 0.5 | 85.0862 | (98.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a od_c16_bracket_R3/OD-C07 clearance | 187.4727 | mm | >= 0.5 | 186.9727 | (98.0000, 0.0000, 54.0000) mm | PASS (assumed: A-04) | A-04 |
| U-03a od_c16_bracket_R3/OD-C08 clearance | 124 | mm | >= 0.5 | 123.5 | (98.0000, 0.0000, 54.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03a od_c16_bracket_R3/OD-C10 clearance | 199 | mm | >= 0.5 | 198.5 | (117.0000, 16.0000, 70.0000) mm | PASS | — |
| U-03a od_c16_bracket_R3/OD-C11 clearance | 331 | mm | >= 0.5 | 330.5 | (98.0000, 0.0000, 54.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03a od_c16_bracket_R3/OD-C15-RF clearance | 12.7765 | mm | >= 0.5 | 12.2765 | (110.0000, 0.0000, 70.0000) mm | PASS | — |
| U-03a od_c16_bracket_R3/OD-C15-LF clearance | 200.0649 | mm | >= 0.5 | 199.5649 | (98.0000, 0.0000, 70.0000) mm | PASS | — |
| U-03a od_c16_bracket_R3/OD-C15-RR clearance | 340.0621 | mm | >= 0.5 | 339.5621 | (110.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a od_c16_bracket_R3/OD-C15-LR clearance | 397.3351 | mm | >= 0.5 | 396.8351 | (98.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a od_c16_bracket_R3/od_c16_bracket_L3 clearance | 196 | mm | >= 0.5 | 195.5 | (98.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a contact od_c16_bracket_L3/OD-C01 clearance | 0 | mm | == 0.0 | 0 | (-98.0000, 0.0000, 70.0000) mm | PASS (assumed: A-01) | A-01 |
| U-03a contact od_c16_bracket_L3/OD-C01 interference | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03a od_c16_bracket_L3/OD-C02 clearance | 178.059 | mm | >= 0.5 | 177.559 | (-98.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a od_c16_bracket_L3/OD-C05 clearance | 85.5862 | mm | >= 0.5 | 85.0862 | (-98.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a od_c16_bracket_L3/OD-C07 clearance | 89 | mm | >= 0.5 | 88.5 | (-117.0000, 0.0000, 54.0000) mm | PASS (assumed: A-04) | A-04 |
| U-03a od_c16_bracket_L3/OD-C08 clearance | 211.2274 | mm | >= 0.5 | 210.7274 | (-98.0000, 0.0000, 54.0000) mm | PASS (assumed: A-05) | A-05 |
| U-03a od_c16_bracket_L3/OD-C10 clearance | 199 | mm | >= 0.5 | 198.5 | (-117.0000, 16.0000, 54.0000) mm | PASS | — |
| U-03a od_c16_bracket_L3/OD-C11 clearance | 331 | mm | >= 0.5 | 330.5 | (-98.0000, 0.0000, 54.0000) mm | PASS (assumed: A-03) | A-03 |
| U-03a od_c16_bracket_L3/OD-C15-RF clearance | 200.0649 | mm | >= 0.5 | 199.5649 | (-98.0000, 0.0000, 70.0000) mm | PASS | — |
| U-03a od_c16_bracket_L3/OD-C15-LF clearance | 12.7765 | mm | >= 0.5 | 12.2765 | (-110.0000, 0.0000, 70.0000) mm | PASS | — |
| U-03a od_c16_bracket_L3/OD-C15-RR clearance | 397.3351 | mm | >= 0.5 | 396.8351 | (-98.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a od_c16_bracket_L3/OD-C15-LR clearance | 340.0621 | mm | >= 0.5 | 339.5621 | (-110.0000, 0.0000, 54.0000) mm | PASS | — |
| U-03a lip od_c13_right/OD-C10 gap | 0.4 | mm | in [0.35, 0.45] | 0.05 | (116.6000, 215.0000, -280.0000) mm | PASS (assumed: A-02, A-14) | A-02, A-14 |
| U-03a lip od_c12_left/OD-C10 gap | 0.4 | mm | in [0.35, 0.45] | 0.05 | (-116.6000, 215.0000, -280.0000) mm | PASS (assumed: A-02, A-14) | A-02, A-14 |
| U-03a coaxial od_c16_bracket_R1 insert bore / od_c13_right hole | 0 | mm | <= 0.1 | 0.1 |  | PASS | — |
| REQ-05 plate hole od_c16_bracket_R1 at (+104.5, -262) | 0 | mm | <= 0.1 | 0.1 | (104.5000, 0.0000, -262.0000) mm | PASS (assumed: A-01, A-07) | A-01, A-07 |
| U-03a coaxial od_c16_bracket_L1 insert bore / od_c12_left hole | 0 | mm | <= 0.1 | 0.1 |  | PASS | — |
| REQ-05 plate hole od_c16_bracket_L1 at (-104.5, -262) | 0 | mm | <= 0.1 | 0.1 | (-104.5000, 0.0000, -262.0000) mm | PASS (assumed: A-01, A-07) | A-01, A-07 |
| U-03a coaxial od_c16_bracket_R2 insert bore / od_c13_right hole | 0 | mm | <= 0.1 | 0.1 |  | PASS | — |
| REQ-05 plate hole od_c16_bracket_R2 at (+104.5, -15) | 0 | mm | <= 0.1 | 0.1 | (104.5000, 0.0000, -15.0000) mm | PASS (assumed: A-01, A-07) | A-01, A-07 |
| U-03a coaxial od_c16_bracket_L2 insert bore / od_c12_left hole | 0 | mm | <= 0.1 | 0.1 |  | PASS | — |
| REQ-05 plate hole od_c16_bracket_L2 at (-104.5, -15) | 0 | mm | <= 0.1 | 0.1 | (-104.5000, 0.0000, -15.0000) mm | PASS (assumed: A-01, A-07) | A-01, A-07 |
| U-03a coaxial od_c16_bracket_R3 insert bore / od_c13_right hole | 0 | mm | <= 0.1 | 0.1 |  | PASS | — |
| REQ-05 plate hole od_c16_bracket_R3 at (+104.5, +62) | 0 | mm | <= 0.1 | 0.1 | (104.5000, 0.0000, 62.0000) mm | PASS (assumed: A-01, A-07) | A-01, A-07 |
| U-03a coaxial od_c16_bracket_L3 insert bore / od_c12_left hole | 0 | mm | <= 0.1 | 0.1 |  | PASS | — |
| REQ-05 plate hole od_c16_bracket_L3 at (-104.5, +62) | 0 | mm | <= 0.1 | 0.1 | (-104.5000, 0.0000, 62.0000) mm | PASS (assumed: A-01, A-07) | A-01, A-07 |
| REQ-06 (+104.5,-262) to plate edge | 15.5 | mm | >= 8.0 | 7.5 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,-262) to nearest OD-C01 hole | 33.4552 | mm | >= 6.0 | 27.4552 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,-262) to nearest handed-over insert | 22.1416 | mm | >= 6.0 | 16.1416 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,-262) plate solid in a D8 disc (missing volume) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,-15) to plate edge | 15.5 | mm | >= 8.0 | 7.5 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,-15) to nearest OD-C01 hole | 49.6009 | mm | >= 6.0 | 43.6009 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,-15) to nearest handed-over insert | 63.0179 | mm | >= 6.0 | 57.0179 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,-15) plate solid in a D8 disc (missing volume) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,+62) to plate edge | 15.5 | mm | >= 8.0 | 7.5 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,+62) to nearest OD-C01 hole | 28.5351 | mm | >= 6.0 | 22.5351 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,+62) to nearest handed-over insert | 140.008 | mm | >= 6.0 | 134.008 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (+104.5,+62) plate solid in a D8 disc (missing volume) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,-262) to plate edge | 15.5 | mm | >= 8.0 | 7.5 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,-262) to nearest OD-C01 hole | 33.4552 | mm | >= 6.0 | 27.4552 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,-262) to nearest handed-over insert | 22.1416 | mm | >= 6.0 | 16.1416 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,-262) plate solid in a D8 disc (missing volume) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,-15) to plate edge | 15.5 | mm | >= 8.0 | 7.5 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,-15) to nearest OD-C01 hole | 28.3064 | mm | >= 6.0 | 22.3064 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,-15) to nearest handed-over insert | 202.5469 | mm | >= 6.0 | 196.5469 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,-15) plate solid in a D8 disc (missing volume) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,+62) to plate edge | 15.5 | mm | >= 8.0 | 7.5 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,+62) to nearest OD-C01 hole | 28.5351 | mm | >= 6.0 | 22.5351 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,+62) to nearest handed-over insert | 238.0257 | mm | >= 6.0 | 232.0257 |  | PASS (assumed: A-01) | A-01 |
| REQ-06 (-104.5,+62) plate solid in a D8 disc (missing volume) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-01) | A-01 |
| REQ-07 keep-out D8x2 at foot (+110,+90) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-07 keep-out D8x2 at foot (-110,+90) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-07 keep-out D8x2 at foot (+110,-295) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-07 keep-out D8x2 at foot (-110,-295) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-07 driver access od_c16_bracket_R1 (r4, y16..215) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-05) | A-05 |
| REQ-07 panel screw access od_c16_bracket_R1 (r4, 20 outside) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-07 driver access od_c16_bracket_L1 (r4, y16..215) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-05) | A-05 |
| REQ-07 panel screw access od_c16_bracket_L1 (r4, 20 outside) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-07 driver access od_c16_bracket_R2 (r4, y16..215) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-05) | A-05 |
| REQ-07 panel screw access od_c16_bracket_R2 (r4, 20 outside) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-07 driver access od_c16_bracket_L2 (r4, y16..215) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-05) | A-05 |
| REQ-07 panel screw access od_c16_bracket_L2 (r4, 20 outside) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-07 driver access od_c16_bracket_R3 (r4, y16..215) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-05) | A-05 |
| REQ-07 panel screw access od_c16_bracket_R3 (r4, 20 outside) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| REQ-07 driver access od_c16_bracket_L3 (r4, y16..215) | 0 | mm3 | <= 0.0 | 0 |  | PASS (assumed: A-05) | A-05 |
| REQ-07 panel screw access od_c16_bracket_L3 (r4, 20 outside) | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03b path bracket od_c16_bracket_R1 down from +20 | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03b path bracket od_c16_bracket_L1 down from +20 | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03b path bracket od_c16_bracket_R2 down from +20 | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03b path bracket od_c16_bracket_L2 down from +20 | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03b path bracket od_c16_bracket_R3 down from +20 | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03b path bracket od_c16_bracket_L3 down from +20 | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03b path panel od_c13_right inward from 20 outside | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03b path panel od_c12_left inward from 20 outside | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |
| U-03b path OD-C10 down from +40 | 0 | mm3 | <= 0.0 | 0 |  | PASS | — |

#### summary per gate id (worst row)

od_c13_right     exactly_one_solid      PASS          1 count  [exactly_one_solid]
od_c13_right     U-01                   PASS          1 count  [U-01 solid_count]
od_c13_right     U-02                   PASS          218.8105 mm  [U-02 size_y]
od_c13_right     envelope_within_spec   PASS          218.8105 mm  [envelope_within_spec size_y]
od_c13_right     D-02                   PASS_ASSUMED  385 mm  [D-02 bed length (z)]
od_c13_right     U-04                   PASS          0 mm3  [U-04 volume_delta]
od_c13_right     U-05                   PASS          11 count  [U-05 plane_faces]
od_c13_right     feature_census         PASS          11 count  [feature_census plane_faces]
od_c13_right     D-01a                  PASS          3 mm  [D-01a]
od_c13_right     D-01b                  PASS          3 mm  [D-01b]
od_c13_right     D-06a                  PASS          3 mm  [D-06a]
od_c13_right     U-06                   PASS          3 mm  [U-06 (Soft)]
od_c13_right     D-03a                  PASS          60 deg  [D-03a]
od_c13_right     REQ-02                 PASS_ASSUMED  0 mm3  [REQ-02 lid material in x +-(109.5..117) over the lip's zone]
od_c13_right     D-03b                  PASS          0 mm  [D-03b (corroboration; reviewer from sections)]
od_c13_right     REQ-03                 PASS          1 bool  [REQ-03 hole z-262 through]
od_c13_right     D-04a                  PASS          3.4 mm  [D-04a hole z-262]
od_c13_right     REQ-01                 PASS          1 count  [REQ-01 outer face count]
od_c13_right     D-04d                  PASS_ASSUMED  0.4 mm  [D-04d lip to OD-C10 skirt]
od_c13_right     U-07                   PASS          0.4341 rad  [U-07 angular tolerance]
od_c13_right     U-08                   N/A           —   [U-08]
od_c13_right     D-07                   N/A           —   [D-07]
od_c13_right     E-06                   PASS          1 count  [E-06]
od_c13_right     REQ-08                 INCONCLUSIVE  —   [REQ-08 (Soft, bench)]
od_c12_left      exactly_one_solid      PASS          1 count  [exactly_one_solid]
od_c12_left      U-01                   PASS          1 count  [U-01 solid_count]
od_c12_left      U-02                   PASS          218.8105 mm  [U-02 size_y]
od_c12_left      envelope_within_spec   PASS          218.8105 mm  [envelope_within_spec size_y]
od_c12_left      D-02                   PASS_ASSUMED  385 mm  [D-02 bed length (z)]
od_c12_left      U-04                   PASS          0 mm3  [U-04 volume_delta]
od_c12_left      U-05                   PASS          15 count  [U-05 plane_faces]
od_c12_left      feature_census         PASS          15 count  [feature_census plane_faces]
od_c12_left      D-01a                  PASS          2.1 mm  [D-01a]
od_c12_left      D-01b                  PASS          2.1 mm  [D-01b]
od_c12_left      D-06a                  PASS          2.1 mm  [D-06a]
od_c12_left      U-06                   PASS          2.1 mm  [U-06 (Soft)]
od_c12_left      D-03a                  PASS          60 deg  [D-03a]
od_c12_left      REQ-02                 PASS_ASSUMED  0 mm3  [REQ-02 lid material in x +-(109.5..117) over the lip's zone]
od_c12_left      D-03b                  PASS          0 mm  [D-03b (corroboration; reviewer from sections)]
od_c12_left      REQ-03                 PASS          1 bool  [REQ-03 hole z-262 through]
od_c12_left      D-04a                  PASS          3.4 mm  [D-04a hole z-262]
od_c12_left      REQ-01                 PASS          1 count  [REQ-01 outer face count]
od_c12_left      D-04d                  PASS_ASSUMED  0.4 mm  [D-04d lip to OD-C10 skirt]
od_c12_left      U-07                   PASS          0.4341 rad  [U-07 angular tolerance]
od_c12_left      U-08                   N/A           —   [U-08]
od_c12_left      D-07                   N/A           —   [D-07]
od_c12_left      E-06                   PASS          1 count  [E-06]
od_c12_left      REQ-08                 INCONCLUSIVE  —   [REQ-08 (Soft, bench)]
od_c12_left      REQ-04                 PASS_ASSUMED  -117.9 mm  [REQ-04 relief floor x]
od_c16_bracket   exactly_one_solid      PASS          1 count  [exactly_one_solid]
od_c16_bracket   U-01                   PASS          1 count  [U-01 solid_count]
od_c16_bracket   U-02                   PASS          19 mm  [U-02 size_x]
od_c16_bracket   envelope_within_spec   PASS          19 mm  [envelope_within_spec size_x]
od_c16_bracket   REQ-05                 PASS          1 bool  [REQ-05 hole through]
od_c16_bracket   D-02                   PASS_ASSUMED  19 mm  [D-02 size_x]
od_c16_bracket   U-04                   PASS          0 mm3  [U-04 volume_delta]
od_c16_bracket   U-05                   PASS          8 count  [U-05 plane_faces]
od_c16_bracket   feature_census         PASS          8 count  [feature_census plane_faces]
od_c16_bracket   D-01a                  PASS          3 mm  [D-01a]
od_c16_bracket   D-01b                  PASS          3 mm  [D-01b]
od_c16_bracket   D-06a                  PASS          3 mm  [D-06a]
od_c16_bracket   U-06                   PASS          3 mm  [U-06 (Soft)]
od_c16_bracket   D-04a                  PASS          3.4 mm  [D-04a hole diameter]
od_c16_bracket   D-05b                  PASS_ASSUMED  4 mm  [D-05b insert bore diameter]
od_c16_bracket   D-05a                  PASS_ASSUMED  12 mm  [D-05a material across the insert bore]
od_c16_bracket   J-05                   PASS          3.25 mm  [J-05 axial web, insert-bore floor to counterbore]
od_c16_bracket   D-03a                  PASS          1 count  [D-03a cylinders not along Y = the insert bore only]
od_c16_bracket   D-03b                  PASS_ASSUMED  4 mm  [D-03b insert-bore crown bridge (its diameter; reviewer from sections)]
od_c16_bracket   U-07                   PASS          0.3139 rad  [U-07 angular tolerance]
od_c16_bracket   U-08                   N/A           —   [U-08]
od_c16_bracket   D-07                   N/A           —   [D-07]
od_c16_bracket   E-06                   PASS          1 count  [E-06]
od_side_assembly assembly_file          PASS          0 mm  [assembly solids = placed part files (max centre / volume delta)]
od_side_assembly U-03                   PASS_ASSUMED  0 mm  [U-03a contact od_c13_right|OD-C01 clearance]
od_side_assembly REQ-05                 PASS_ASSUMED  0 mm  [REQ-05 plate hole od_c16_bracket_R1 at (+104.5, -262)]
od_side_assembly REQ-06                 PASS_ASSUMED  0 mm3  [REQ-06 (+104.5,-262) plate solid in a D8 disc (missing volume)]
od_side_assembly REQ-07                 PASS_ASSUMED  0 mm3  [REQ-07 driver access od_c16_bracket_R1 (r4, y16..215)]
