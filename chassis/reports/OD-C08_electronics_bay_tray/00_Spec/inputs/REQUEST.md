# REQUEST — OD-C08 electronics bay tray (job 20261001-od-c08-electronics-bay-tray)

BOM row: `OD-C08, Electronics bay tray, PETG, printed`. chassis/README order of work
row 9: designed against OD-E01, OD-E02 (path 1) or OD-E51 … E58 (path 2); "the Usta
picks the path" — answered 2026-10-01: path 1, the original OEM PCB.

Where it goes: the electronics zone of OD-C01, x 70 … 120, z −240 … −30 behind the
bulkhead OD-C02 (OD-C01 spec A-08: "OD-C08 with either path within x 70 … 120,
z −240 … −30 behind the bulkhead, its own tray screwed to bulkhead and plate later";
OD-C02 spec A-07: "OD-C08 is not designed and can keep 3 mm from the wall").
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
