# OD-000 clash report

33 solids; 61 pairs whose bounding boxes overlap or come within 1.0 mm were measured (common volume and least clearance). Written by `build_od000.py`; the numbers are in `clash_report.json`.

## Interference above 1.0 mm³ (0)

None.

## INCONCLUSIVE (2)

The boolean cannot be trusted on these pairs (an unsound scan solid, or the boolean failed); the raw boolean number is shown as a lead only, never as a measurement.

| a | b | raw boolean mm³ (unchecked) | clearance mm | reason |
|---|---|---:|---:|---|
| OD-C09 | OD-E02 | 0 | 0.0001 | OD-E02: brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface |
| OD-G01 | OD-G10 | 0 | 0.0 | OD-G10: brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface |

## Small overlaps up to 1.0 mm³ (0)

None.

## Contacts at 0 gap (38)

OD-C01 | OD-C02, OD-C01 | OD-C03, OD-C01 | OD-C04, OD-C01 | OD-C05, OD-C01 | OD-C07, OD-C01 | OD-C08, OD-C01 | OD-C09, OD-C01 | OD-C11, OD-C01 | OD-C12, OD-C01 | OD-C13, OD-C01 | OD-C15-RF, OD-C01 | OD-C15-LF, OD-C01 | OD-C15-RR, OD-C01 | OD-C15-LR, OD-C01 | OD-C16-R1, OD-C01 | OD-C16-R2, OD-C01 | OD-C16-R3, OD-C01 | OD-C16-L1, OD-C01 | OD-C16-L2, OD-C01 | OD-C16-L3, OD-C02 | OD-C10, OD-C05 | OD-G01, OD-C07 | OD-H22, OD-C07 | OD-H24, OD-C08 | OD-E01, OD-C09 | OD-C10, OD-C10 | OD-C11, OD-C10 | OD-C12, OD-C10 | OD-C13, OD-C11 | OD-C14-A, OD-C11 | OD-C14-B, OD-C12 | OD-C16-L1, OD-C12 | OD-C16-L2, OD-C12 | OD-C16-L3, OD-C13 | OD-C16-R1, OD-C13 | OD-C16-R2, OD-C13 | OD-C16-R3, OD-G01 | OD-G04

## Clear, volume unchecked but the distance is positive (5)

OD-C04 | OD-H11 (10.1), OD-C05 | OD-G10 (13.689), OD-C09 | OD-G10 (14.0206), OD-C12 | OD-E02 (1.8271), OD-G04 | OD-G10 (0.4782)

## Clear, measured: no common volume, least gap in mm (16)

OD-C05 | OD-H24 (0.2907), OD-C05 | OD-C10 (0.5), OD-C14-A | OD-C14-B (0.8), OD-C07 | OD-C12 (0.9), OD-C03 | OD-H01 (2.3), OD-C11 | OD-C12 (3.0), OD-C11 | OD-C13 (3.0), OD-C09 | OD-C12 (4.1231), OD-C09 | OD-C13 (4.1231), OD-C05 | OD-G04 (5.0), OD-C08 | OD-C13 (5.0), OD-C12 | OD-H24 (5.54), OD-C12 | OD-H22 (5.835), OD-C13 | OD-E01 (7.738), OD-C09 | OD-G01 (8.7757), OD-C05 | OD-C09 (12.0)

## Placement cross-check

Each placed solid's box against the same solid in its part's check assembly (tolerance 0.05 mm).

| part | check assembly | child | max delta mm | ok |
|---|---|---|---:|---|
| OD-C01 | `od_side_assembly_C1_v01.step` | OD-C01 | 0.0 | yes |
| OD-C02 | `od_c10_assembly_C1_v01.step` | od_c02_bulkhead | 0.0 | yes |
| OD-C02 | `od_c08_assembly_C1_v01.step` | od_c02_bulkhead | 0.0 | yes |
| OD-C03 | `od_c11_assembly_C1_v03.step` | od_c03_cradle | 0.0 | yes |
| OD-C04 | `od_c01_assembly_C1_v02.step` | od_c04_mount | 0.0 | yes |
| OD-C05 | `od_side_assembly_C1_v01.step` | OD-C05 | 0.0 | yes |
| OD-C05 | `od_c05_assembly_C4_v04.step` | od_c05_carrier | 0.0 | yes |
| OD-C07 | `od_side_assembly_C1_v01.step` | OD-C07 | 0.0 | yes |
| OD-C08 | `od_side_assembly_C1_v01.step` | OD-C08 | 0.0 | yes |
| OD-C09 | `od_c09_assembly_C1_v01.step` | od_c09_front | 0.0 | yes |
| OD-C10 | `od_side_assembly_C1_v01.step` | OD-C10 | 0.0 | yes |
| OD-C11 | `od_side_assembly_C1_v01.step` | OD-C11 | 0.0 | yes |
| OD-C12 | `od_side_assembly_C1_v01.step` | od_c12_left | 0.0 | yes |
| OD-C13 | `od_side_assembly_C1_v01.step` | od_c13_right | 0.0 | yes |
| OD-C14-A | `od_c14_assembly_C1_v01.step` | half_upper | 0.0 | yes |
| OD-C14-B | `od_c14_assembly_C1_v01.step` | half_lower | 0.0 | yes |
| OD-C15-RF | `od_side_assembly_C1_v01.step` | OD-C15-RF | 0.0 | yes |
| OD-C15-LF | `od_side_assembly_C1_v01.step` | OD-C15-LF | 0.0 | yes |
| OD-C15-RR | `od_side_assembly_C1_v01.step` | OD-C15-RR | 0.0 | yes |
| OD-C15-LR | `od_side_assembly_C1_v01.step` | OD-C15-LR | 0.0 | yes |
| OD-C16-R1 | `od_side_assembly_C1_v01.step` | od_c16_bracket_R1 | 0.0 | yes |
| OD-C16-R2 | `od_side_assembly_C1_v01.step` | od_c16_bracket_R2 | 0.0 | yes |
| OD-C16-R3 | `od_side_assembly_C1_v01.step` | od_c16_bracket_R3 | 0.0 | yes |
| OD-C16-L1 | `od_side_assembly_C1_v01.step` | od_c16_bracket_L1 | 0.0 | yes |
| OD-C16-L2 | `od_side_assembly_C1_v01.step` | od_c16_bracket_L2 | 0.0 | yes |
| OD-C16-L3 | `od_side_assembly_C1_v01.step` | od_c16_bracket_L3 | 0.0 | yes |
| OD-G01 | `od_c09_assembly_C1_v01.step` | OD-G01_housing | 0.0 | yes |
| OD-G01 | `od_g01_assembly_C1_v03.step` | od_g01_housing | 0.0 | yes |
| OD-G04 | `od_c09_assembly_C1_v01.step` | OD-G04 | 0.0 | yes |
| OD-G10 | `od_c09_assembly_C1_v01.step` | OD-G10_portafilter_locked | 0.0 | yes |
| OD-H01 | `od_c11_assembly_C1_v03.step` | od_h01_pump | 0.0 | yes |
| OD-H11 | `od_c01_assembly_C1_v02.step` | od_h11_thermoblock | 0.0 | yes |
| OD-H22 | `od_c07_assembly_C1_v01.step` | OD-H22 | 0.0 | yes |
| OD-H24 | `od_c07_assembly_C1_v01.step` | OD-H24 | 0.0 | yes |
| OD-E01 | `od_c08_assembly_C1_v01.step` | od_e01_power_pcb | 0.0 | yes |
| OD-E02 | `od_c09_assembly_C1_v01.step` | OD-E02_control_board | 0.0 | yes |

## Unsound source solids

- `step/OD-G10_portafilter.step`: brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface
- `step/OD-H11_thermoblock.step`: brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface
- `step/OD-E02_control_board.step`: brep_valid is 0: BOPAlgo finds BOPAlgo_InvalidCurveOnSurface
