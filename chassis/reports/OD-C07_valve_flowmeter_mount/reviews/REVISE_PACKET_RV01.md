# REVISE packet — RV01 od_c07_mount_v01 (20260930-od-c07-valve-flowmeter-mount)

Written by Oğuz from `reviews/RV01_od_c07_mount_v01.md` · spec 1.2 · build attempt 2 of 2 · 2026-09-30

## Blocking findings

| Finding | Measured → required | Risk | Proposed fix |
|---|---|---|---|
| F1 (REQ-02), F3 (U-03), F4 (D-04c): the recess edge chamfer to the ends of the OD-H24 underside ribs | 0.297 → ≥ 0.5 mm | LOW: static seat, no load or motion across the gap; a touch would lift the rib 0.1 above the rim's own bearing plane | not reachable inside the spec (ribs end at r 14.056, recess R 14.10 ± 0.1): move the recess edge out to R 14.60 (spec 1.3, REQ-02), giving up rim bearing between r 14.28 and 14.60 (the rim still bears over r 14.60 … 15.71, 1.1 wide), or name the rib ends as part of the rim contact (U-18 exception) |
| F2 (REQ-01), F4 (D-04c): the ring's 0.3 root round to the cup's foot | 0.377 → in [0.50, 0.70] mm | LOW: only the lowest 0.05 of the round is within 0.5; the wall keeps 0.531; D-04d's 0.30 holds | ring root round 0.1 instead of 0.3 (reviewer computes ≈ 0.55 at the toe) |

Also noted, not blocking (all LOW): F5 REQ-04's slot window wording overlaps the slits (spec wording, fix in 1.3); F6 the ring base (1.72) and catch tip (1.60) are also under 2.0 (both pass D-01b's 1.5; spec reason to be reworded); F7–F11 six fit parameters pass only at nominal, chiefly because the hook catch to pedestal stack equals the OEM rim-to-flange height 19.9 exactly (zero designed play: a print 0.1 tall does not snap, 0.1 short lets the flowmeter rock 0.1). Everything else passes: 121 OD-H22 poses and 51 OD-H24 poses at 0 mm³, every print, snap, bore and drainage row, 26 positive controls.

## Options

| Option | What happens | Cost and risk |
|---|---|---|
| **A. Another round** | Spec 1.3: recess R 14.60, ring root round 0.1, the two wording fixes (F5, F6), and 0.1 of designed play under the catch (catch underside z 30.0, REQ-03, J-04 as a 0…0.1 gap) if the Usta wants F7 closed too; the designer rebuilds (attempt 3, cap raised to 3), one new review RV02 | one designer and one reviewer run; the geometry moves by tenths only; the part is then clean with no exception |
| **B. Accept documented deviations** | F1–F4 are accepted as they are; the record states: "the recess edge sits 0.30 from the flowmeter's underside ribs and the ring root 0.38 from its cup, both static unloaded gaps above the 0.30 sliding-fit floor" | the two gaps ride into the print; a scan-scale error (A-01) of 0.3 % could close the 0.30 gap |
| **C. Stop** | The job is `STOPPED`; what exists: the v01 STEP/STL, REPORT v02, RV01 | no OD-C07 |

**Oğuz recommends:** A, because both fixes are single parameters, the part is otherwise clean, and no exception has to travel with it.

## The Usta's decision

Decision: <A | B | C> · date: <yyyy-mm-dd> · notes: <…>
