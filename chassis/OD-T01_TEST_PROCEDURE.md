# OD-T01 — group head bench pressure test

The test closes OD-G01 REQ-12: the printed housing carries the brew load
(15 bar on a Ø51 basket, 3.06 kN) through its lugs, body and inserts as it does
in the machine. The rig is `OD-T01_pressure_test_rig` (PLA, Kobra Max 3, lying
on its rear face, no supports, 240 × 160 × 120). Every value below is an assumption from the
spec's §6 (`reports/OD-T01_pressure_test_rig/00_Spec/DESIGN_SPEC.md`) until the
bench confirms it.

> **Rig v02 (25 mm plate).** Review RV01 found the v01 plate (15 mm) only about
> 1.5 times as strong as the load through the hub window; the Usta chose v02. The
> v02 plate runs at about 9.6 MPa at 15 bar, a factor of about 4 against an unsourced
> 40 MPa for printed PLA, and each screw head bears on 5.0 of plate. Review RV02
> flags the **head bearing**: 765 N per screw on the ISO 7380 head's ring (16.4 mm²)
> is about 47 MPa, near printed PLA's compressive yield. So:
> - print the rig with **100 % infill** (or at least the plate solid round the four
>   counterbores); the factor above assumes a solid plate;
> - if you have a Ø7.5 flat-bottomed cutter, open the four counterbores to Ø7.5
>   and put an **M3 steel washer (ISO 7089, Ø7)** under each head (about 25 MPa);
> - in any case watch the heads at each step: a head sinking into the plate is a
>   stop.

## Parts (bought, A-04 / A-06 / A-11)

| Part | Note |
|---|---|
| Hand hydrostatic test pump, or the Ulka pump OD-H01 with its OPV | cold tap water only (A-03) |
| Pressure gauge 0–25 bar | readable from behind the shield |
| Bleed valve and tee | at the top of the line, to purge air |
| PTFE or reinforced tube, rated ≥ 25 bar | to the OEM water connection |
| OEM water connection OD-G07 gasket, OD-H14, OD-H15 | seats on OD-G04's hub tube through the window (A-05) |
| Stainless 51 mm blind basket | in OD-G10; closes the mouth (A-06) |
| 4 × M3 × 10 ISO 7380 (+ 4 × M3 washers ISO 7089, optional) | rig plate into the housing's inserts (5.0 of plate under the head, 5.0 into the 5.7 insert) |
| 4 × M4 or 4 mm wood screws, or 2 clamps | base wings to the bench (A-11) |
| Clear shield (polycarbonate sheet) and safety glasses | between you and the rig |
| Shallow tray ≤ 50 tall | under the portafilter on the base (A-07) |

## Steps

1. Screw the rig to the bench. Set the housing (with its inserts and OD-G04) on
   the plate's underside and drive the four M3 × 10 from above (a 2 mm hex key reaches down the 20 deep counterbores); snug, do not crush.
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

Date, rig version (v02), filament, infill and print settings; washers or not; handle angle at
lock; for each step the gauge reading at start and end of the hold and what was
seen; the highest pressure held; photos of the lugs, the inserts and the rig's
plate before and after. Add the result to
`reports/OD-G01_group_head_housing/` (REQ-12) and
`reports/OD-T01_pressure_test_rig/` (REQ-08, A-02 … A-08, A-11).
