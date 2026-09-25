# MEASUREMENTS — OD-H22_3-way-valve (REQUEST; not filled)

Instrument: caliper (state model and resolution when filled)
Date measured: — (owner decision 2026-09-25: proceed scan-only, no calipers; `DECISIONS.md` MEASUREMENTS)
Status summary: 0 of 20 rows carry a value; all are ABSENT, not passed. The scan is the authority
(`scan-authority`, ungated) for every dimension until a reading arrives; any single reading is a
re-run trigger.

"Scan says" is the scan-predicted value in the datum frame (`intake/alignment.json`; X = ear axis,
Z = valve axis, z=0 = flange back face). Do NOT copy it into the reading column.

## A. Envelope (first; drives CHK-SCALE)
| ID | Feature | Jaw placement (photo ref) | Scan says | Reading (mm) | Status | Photo id | Notes |
|---|---|---|---|---|---|---|---|
| ENV-X | ear tip to ear tip (along the ears) | outside jaws on the two ear ends (photo_4) | 41.6 (−X ear 20.91 + +X ear 20.70; +X tip damaged) | | absent | | |
| ENV-Y | port mouth to port mouth, across the Y | outside jaws on the two port lips | 39.9 (datum y extent) | | absent | | |
| ENV-Z | drive-tube top to flange back face | depth rod / jaws: tube top vs back face | 13.7 (p50 of tube top faces; max 13.98) | | absent | | define on the tube top, the true topmost feature |

## B. Functional dimensions
| ID | Feature | Type | Datum ref | Why it matters | Jaw placement | Scan says | Reading | Status | Photo id |
|---|---|---|---|---|---|---|---|---|---|
| F01 | flange thickness (back face → tray floor) | step | z | seat | depth rod from rim into tray, minus rim height | 2.26 | | absent | |
| F02 | ear hole Ø (each ear) | Ø | ear hole axis | screws | inside jaws | 3.87 / 3.88 | | absent | |
| F03 | ear hole pitch | distance | X | screw pattern | inside-edge to inside-edge + Ø | 30.79 | | absent | |
| F04 | drive tube OD | Ø | Z axis | knob interface | outside jaws above the collar | 12.41 | | absent | |
| F05 | drive tube bore | Ø | Z axis | knob interface | inside jaws | 9.12 | | absent | |
| F06 | slot width, slots on the ear axis (×2) | width | Z axis | drive key | inside jaws in the slot | 3.06 | | absent | |
| F07 | slot width, slots across the ears (×2) | width | Z axis | drive key | inside jaws in the slot | 2.65 | | absent | |
| F08 | boss collar OD | Ø | Z axis | seat | outside jaws | 16.11 | | absent | |
| F09 | stem OD under the flange | Ø | Z axis | — | outside jaws between the gussets | 13.10 | | absent | |
| F10 | stem neck OD | Ø | Z axis | — | outside jaws above the junction | 8.15 | | absent | |
| F11 | port lip OD (each port) | Ø | port axis | hose seal | outside jaws on the round lip | 12.32 | | absent | |
| F12 | port bore at the mouth | Ø | port axis | hose | inside jaws | 8.68 (mouth) / ≈8.3 at 3 mm depth (draft) | | absent | |
| F13 | clip block across flats (both directions) | width | port axis | clip | outside jaws on the block flats | 11.78 × 11.82 | | absent | |
| F14 | clip slot width (along the port) | width | port axis | U-clip | inside jaws in the slot | 1.35 | | absent | |
| F15 | port sleeve OD | Ø | port axis | — | outside jaws mid-sleeve | 11.17 | | absent | |

## C. Wall thicknesses / second tier
| ID | Feature | Jaw placement | Scan says | Reading | Status | Photo id |
|---|---|---|---|---|---|---|
| W01 | tray rim wall | outside jaws on the lip | 1.42 | | absent | |
| W02 | rim height above back face | depth rod | 5.63 | | absent | |

## D. Photo-transcribed candidates
None (no caliper photos supplied).

## E. Extra dims
—
