# REVISE packet — RV01 od_c05_carrier_v01 (20260930-od-c05-group-head-carrier)

Written by Oğuz from `reviews/RV01_od_c05_carrier_v01.md` · spec 1.2 · build attempt 1 of 2 · 2026-09-30

## Blocking findings

| Finding | Measured → required | Risk | Proposed fix |
|---|---|---|---|
| F1 P1 / P5 plausibility (HIGH) | the spec frame (A-02: +Y up, +Z horizontal toward the user) hangs the group head with its axis horizontal → an espresso group head stands with its axis vertical and its mouth down, as in the De'Longhi Dedica the project copies | HIGH: on its side the basket spills on insertion and the brew leaves sideways; the carrier fits the spec, not the machine | change the machine's up direction: −Z of the housing frame is up, the mouth (+Z) down; re-concept the carrier for a vertical axis (a horizontal plate over the housing's rear flange, hung from a wall that stands on OD-C01); re-derive the mug height from the portafilter spouts |

Every geometric row PASS or PASS (assumed): U-01 … U-07, D-01a … D-06a, E-06, REQ-01 … REQ-08; D-03a settled by the reviewer from the B-rep at 45.000°. Also noted, not blocking: F2 (MEDIUM, REQ-09 Soft: the open 5 mm wall may twist visibly under a sideways handle force), F3 (LOW, `overhang_census` cannot close a face tangent at exactly 45°), F4 (LOW, the window checks should gate the innermost radius over the whole ray), F5 (LOW, the R 6 corners stand 0.83 outside the housing outline).

The wrong frame comes from the OD-G01 spec §2 ("in the machine, +Z is horizontal and faces the user"), which this job's spec 1.0 A-02 took as its basis; OD-C01 spec 1.1 §4 places the housing by the same frame. Measured on `step/OD-G10_portafilter.step`: the portafilter reaches 59.0 below its rim face, so with the rim on the housing's shelf (housing z −14.1) the spouts hang about 41.6 below the housing's mouth face; with the mouth down and ≥ 95 under the spouts over a tray top ≤ 36.9, the housing's rear face (the carrier's contact plane, now horizontal) sits ≥ 201.7 above the floor.

## Options

| Option | What happens | Cost and risk |
|---|---|---|
| **A. Another round, new concept** | spec 2.0: A-02 becomes "the group head axis is vertical, −Z up, the mouth down"; concept C4: a horizontal plate 5 thick over the housing's rear flange (the four screws driven from above, the hub window above the OD-G04 hub and the water connection) carried by a wall that stands on OD-C01 behind the housing, with gussets; the housing's rear face at 205 above the floor; OD-C01 spec 1.2 moves the housing pose and the tray under the mouth; the designer plans and builds v02, one new review follows | one build attempt left after v02 (counters reset by the round); one plan, one build, one review; OD-C01's review waits for the new layout |
| **B. Accept as built** | v01 delivered with the housing on its side | the machine does not work as an espresso machine |
| **C. Stop** | the job is `STOPPED`; what exists: build v01 (STEP, STL, 3MF, scripts, REPORT), RV01 | no carrier; OD-C01's layout stays wrong |

**Oğuz recommends:** A. The part as built is sound; the frame it was built to is not.

## The Usta's decision

Decision: A · date: 2026-09-30 · notes: taken on the Usta's standing instruction of 2026-09-30 (proceed on the recommended option, ledger, ask where a decision is needed); the up direction is put to the Usta in the project thread as a decision card, and spec 2.0 waits for no answer but changes if the answer differs.
