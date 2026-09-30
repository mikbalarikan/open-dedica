# REVISE packet — RV01 od_c03_cradle_v01 (20260930-od-c03-pump-cradle)

Written by Oğuz from `reviews/RV01_od_c03_cradle_v01.md` · spec 1.1 · build attempt 1 of 2 · 2026-09-30

## Blocking findings

| Finding | Measured → required | Risk | Proposed fix |
|---|---|---|---|
| F1 REQ-09 vibration (bench gate, Hard) | not measured → no unacceptable vibration with the OEM sleeve | UNKNOWN: no geometric check can answer it | reclassify REQ-09 as Soft in spec §5 (a bench gate reported and rated, answered by the first run); no geometry change clears it |

Also noted, not blocking: F2 (MEDIUM, the pump's centre of mass at z 7.23 lies ahead of the saddles at z 15 … 31), F3 (MEDIUM, a tie loop crosses the steel side plates at r 31.41 before the assumed sleeve), F4 (MEDIUM, REQ-04's zero-gap contact holds only at r 26.650 and rests on A-03), F5 (MEDIUM, REQ-03 margin 0.300 under the scan's 0.448 p95), F6 (LOW, the slot ligament, slot section and 45° roofs at zero margin by the spec's own values). Every geometric row PASS or PASS (assumed).

## Options

| Option | What happens | Cost and risk |
|---|---|---|
| **A. Another round** | spec 1.2: REQ-09 Soft; rib 1 moved to z −3 … 3 under the centre of mass (F2); slots at z 17 and 28; the designer builds v02 and one new review follows | 1 build attempt left after v02 (cap 2, counters reset by the round); about one designer and one reviewer run |
| **B. Accept documented deviations** | v01 is delivered as reviewed with the statement "vibration with the OEM sleeve untested until the first run; the pump's centre of mass sits 8 mm ahead of the front saddle" | the print may rock on the front rib under vibration (F2) |
| **C. Stop** | the job is `STOPPED`; what exists: build v01 (STEP, STL, scripts, REPORT), RV01 | no cradle |

**Oğuz recommends:** A, because the blocking finding is a spec classification, not a defect, and F2 is a real risk one rib move answers.

## The Usta's decision

Decision: A · date: 2026-09-30 · notes: taken on the Usta's standing instruction of 2026-09-30 (proceed, ledger, ask only where a decision is needed); explicit confirmation pending.
