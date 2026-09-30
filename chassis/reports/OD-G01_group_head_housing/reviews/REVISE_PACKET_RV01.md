# REVISE packet — RV01 od_g01_housing_v03 (20260930-od-g01-group-head-housing)

Written by Oğuz from `reviews/RV01_od_g01_housing_v03.md` · spec 1.3 · build attempt 2 of 2 (round 2) · 2026-09-30

## Blocking findings

| Finding | Measured → required | Risk | Proposed fix |
|---|---|---|---|
| F1 REQ-12 brew load | no measurement → 15 bar on a Ø51 basket (3.06 kN) held on the OD-T01 bench rig | UNKNOWN: no geometric check answers a strength row; A-21 records that no strength calculation exists and spec §5 itself defers the row to a bench test that has not been run | none in CAD: print the part (ASA, mouth up, supports under the lugs and stop blocks) and run the OD-T01 pressure test; a strength calculation of the lug roots would narrow the risk before the print |

Also noted, not blocking: F2 (MEDIUM) one ear top of three touches at the locked pose (0 / 0.090 / 0.021 mm: the scanned ears sit at 120.5/120.5/119°, the lugs at 120°, A-25); F3 (UNKNOWN) no boolean against OD-G10, its STEP is not a sound solid (A-28), the row stands on distance; F4 (MEDIUM) no lug root fillet achieved (sharp roots on the section that carries the brew load); F5 (LOW) the STL is meshed at 0.002 mm, finer than U-07's 0.01, because at 0.01 the mesher's sagitta reads 0.043; F6 (LOW) the insert holes have zero depth margin and open on the flange front; F7 (LOW) the ear-to-stop gap at the locked clock is 0.276 mm, the tightest gap on the lock path.

## Options

| Option | What happens | Cost and risk |
|---|---|---|
| **A. Another round** | Nothing in CAD can answer F1; a round could only address F4 (a lug root fillet the fillet ladder refused at every rung, so it needs a different construction of the lug underside) and F6 (a taller boss or a thicker slab). Build attempts are at the cap (2 of 2): the round needs `halt_decision raise_cap` too | one more designer package and one more review; the bayonet geometry does not change; F1 stays open regardless |
| **B. Accept documented deviations** | F1 is accepted as the spec's own deferral; the delivery states: "The housing has passed every geometric check against the scanned OEM parts. Its strength under brew pressure (15 bar on the 51 mm basket, about 3 kN on the three bayonet lugs) has not been calculated or tested: print it in ASA, run the OD-T01 bench pressure test behind a shield before any use with hot water, and treat the lug roots (sharp, no fillet) as the section to watch." F2–F7 are recorded in the evidence and the part's README | the untested strength is carried into the part; the bench test is the Usta's, with the risk stated |
| **C. Stop** | The job is `STOPPED`; what exists: the v03 STEP, STL, the check assembly, the plan, three REPORTs, RV01 with its positive controls | no printed housing; the programme's first part stays at `todo` |

**Oğuz recommends:** B, because REQ-12 can only ever be answered by the physical test the spec defers to, every geometric row passes on the reviewer's own measurement, and spec §7 (ratified) already states that this row is reported INCONCLUSIVE and carried into the delivery.

## The Usta's decision

Decision: pending · date: — · notes: the orchestrator does not decide in the Usta's place (PLAYBOOK rule 4, D-012); the standing instruction of 2026-09-30 covers building the part, not accepting a review deviation.
