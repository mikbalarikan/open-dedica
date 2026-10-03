# OD-T01 — group head bench pressure test

The test closes OD-G01 REQ-12: the printed housing carries the brew load
(15 bar on a Ø51 basket, 3.06 kN) through its lugs, body and inserts as it does
in the machine. The rig is `OD-T01_pressure_test_rig` (PLA, Kobra Max 3, lying
on its rear face, no supports). Every value below is an assumption from the
spec's §6 (`reports/OD-T01_pressure_test_rig/00_Spec/DESIGN_SPEC.md`) until the
bench confirms it.

> **Rig v01 strength warning (review RV01, finding F1).** The hub window leaves
> 47.5 of the plate's 120 mm width between the screw lines, so at 15 bar the plate
> runs at about 27 MPa: a factor of about 1.5 on an unsourced 40 MPa for printed
> PLA, not the 3.8 the spec estimated. Stress scales with pressure: about 18 MPa at
> 10 bar. With v01, raise the pressure only in the steps below, from behind the
> shield, and stop at the first sign of trouble on the rig. A v02 with a 25 mm plate
> (factor about 4) is proposed.

## Parts (bought, A-04 / A-06 / A-11)

| Part | Note |
|---|---|
| Hand hydrostatic test pump, or the Ulka pump OD-H01 with its OPV | cold tap water only (A-03) |
| Pressure gauge 0–25 bar | readable from behind the shield |
| Bleed valve and tee | at the top of the line, to purge air |
| PTFE or reinforced tube, rated ≥ 25 bar | to the OEM water connection |
| OEM water connection OD-G07 gasket, OD-H14, OD-H15 | seats on OD-G04's hub tube through the window (A-05) |
| Stainless 51 mm blind basket | in OD-G10; closes the mouth (A-06) |
| 4 × M3 × 8 ISO 4762 | rig plate into the housing's inserts, as on OD-C05 |
| 4 × M4 or 4 mm wood screws, or 2 clamps | base wings to the bench (A-11) |
| Clear shield (polycarbonate sheet) and safety glasses | between you and the rig |
| Shallow tray ≤ 50 tall | under the portafilter on the base (A-07) |

## Steps

1. Screw the rig to the bench. Set the housing (with its inserts and OD-G04) on
   the plate's underside and drive the four M3 × 8 from above; snug, do not crush.
2. Fit the water connection on the hub tube through the window and run the line
   pump → tee with bleed → gauge → connection.
3. Put the blind basket in the portafilter, insert it turned about −50°, lift
   and lock it. Note the handle angle at lock (A-07).
4. Fill with the bleed open until water runs without air, then close the bleed.
5. Behind the shield, raise the pressure in steps of **3, 6, 9, 12, 15 bar**,
   holding each for **60 s**. At each step, watch the gauge and look at:
   the housing's lugs and body; the inserts; the rig's plate between the screw
   lines beside the hub window (F1); the counterbore floors under the screw heads.
6. At 15 bar hold **5 min**.
7. Release through the bleed, unlock, and inspect the housing and the rig.

**Stop at once** on any of: a step drop on the gauge, a crack or whitening on
the housing or the rig, a weep at the lugs or inserts, a screw head pulling
into the plate, or the plate visibly bowing.

## Pass (A-03)

The housing holds 15 bar for 5 min with no crack, no step in the gauge and no
weep at the lugs. The rig passes REQ-08 when it shows no visible yield or crack.

## Record

Date, rig version (v01 or v02), filament and print settings; handle angle at
lock; for each step the gauge reading at start and end of the hold and what was
seen; the highest pressure held; photos of the lugs, the inserts and the rig's
plate before and after. Add the result to
`reports/OD-G01_group_head_housing/` (REQ-12) and
`reports/OD-T01_pressure_test_rig/` (REQ-08, A-02 … A-08, A-11).
