# REQUEST — OD-C10 top panel (job 20261001-od-c10-top-panel)

BOM row: `OD-C10, Top panel (removable — 4 screws), ASA, printed`. chassis/README order
of work row 11: designed against OD-C01, OD-C02. SOURCING_GUIDE §6 rule 4: top and back
panels removable with 4 screws each; OPV reachable. OD-C02 provides two M3 inserts for
the top panel in its top rail (spec 1.2 REQ-07, A-05). OD-C05 spec 2.2 A-14: the housing
screws and the carrier's foot screws are reached from above through the removable top
panel; A-06 and A-07: the water connection and the hot water tube (TUBE 7) rise above
the carrier's plate (top y 210) into the hub window. OD-C07 spec A-10: the OPV is adjusted
from above with the top panel off.
## The Usta's words (project thread "Chassis C08 C10 C11", 2026-10-01 10:58Z, verbatim)

> what can start now please initiate it
>
> water tank is transparent hard to scan we can just use the tray that step converted as reference and i will hold water tank on the table myself no need to design  for it now
>
> c08 i will use original pcb for this stage

## Standing instruction (project instructions, in force since 2026-09-30)

Design every 3D-printable part of open-dedica (OD-G01, OD-C01 … C16, OD-T01) with the
pipeline, in the order of `chassis/README.md`; ask the Usta only where a decision is
needed; write open questions as `A-##` rows in the ledger and proceed. Every scan- or
report-derived value is an assumption until the Usta confirms it; calipers beat scans.
Data class PUBLIC (CC BY 4.0).

## Orchestrator's reading of the request (for the record, not the Usta's words)

- OD-C06 (water tank dock) is not designed now. The tank stands on the table beside the
  machine; its seat OD-W03 (BOM name "Tray gasket", the "tray" the Usta refers to) is the
  scanned reference for the tank's ports. Its two tubes (tank → flowmeter OD-W11, and the
  bypass return TUBE 3) therefore enter the machine from outside.
- OD-C08 holds the OEM electronics, path 1 (OD-E01 power PCB; OD-E02 is the front
  control board).
- Delivered neighbours: OD-C01 base frame (spec 1.2), OD-C02 bulkhead (spec 1.2),
  OD-C03, OD-C04, OD-C05 (spec 2.2), OD-C07; all in the OD-C01 machine frame
  (X right, +Y up, +Z front, plate top y = 0).
