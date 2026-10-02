# OD-C08, OD-C10, OD-C11 — integration notes for the OD-G01 thread

Three jobs, each reviewed once, all RV01 `APPROVED_ASSUMPTION_CONDITIONAL` with no
blocking findings. Deliverables on open-dedica branch `claude/project-thread-vf4oxz`
(PR linked in the "C08/C10/C11" thread): `chassis/OD-C08_electronics_bay_tray.*`,
`chassis/OD-C10_top_panel.*`, `chassis/OD-C11_back_panel.*` (STEP, STL, 3MF),
`chassis/src/<part>/`, records `chassis/reports/<part>/`. The shared files below
are yours to change; nothing listed here was edited by these jobs.

| Part | Job | Build | Spec | Material / printer |
|---|---|---|---|---|
| OD-C08 tray | 20261001-od-c08-electronics-bay-tray | v01 | 1.0 | PETG, K1C |
| OD-C10 top panel | 20261001-od-c10-top-panel | v01 | 1.2 | PETG, Kobra Max 3 (BOM says ASA, A-10) |
| OD-C11 back panel | 20261001-od-c11-back-panel | v03 (third build ordered by the Usta) | 1.2 | PETG, Kobra Max 3 (BOM says ASA, A-10) |

## OD-C01 change needed (the plate STEP has none of these yet)

Eight **new** M3 heat-set inserts (Ø4.0 × 6 blind bores from the plate's top face,
axis along −Y) in OD-C01, for screws driven from above:
- OD-C08 flange: (x 88, z −222), (106, −222), (88, −78), (106, −78).
- OD-C11 flanges: (±81, −282), (±95, −282).
Each reviewer confirmed the plate is solid under each hole (≥ 6 from every existing
hole, ≥ 8 from the edge). The plate is 6 thick, so a 6 deep bore from the top
reaches the underside: OD-C01's spec decides through vs. blind (a boss below or a
5.0 bore with a shorter insert).

## docs/bom.csv

- `OD-C08`: status `proposed` → `modeled`; name "Electronics bay tray (holds the OEM power PCB OD-E01 on edge)"; source `printed (Creality K1C)`.
- `OD-C10`: status → `modeled`; material `PETG (A-10; BOM said ASA)`; source `printed (Anycubic Kobra Max 3)`.
- `OD-C11`: status → `modeled`; same material and printer as OD-C10; name may add "cord and two tube pass-throughs, vents".
- `OD-F01` inserts: +12 (8 in OD-C01 above, 2 in the OD-C08 standoffs for board holes H1/H2, 2 in the OD-C11 ledge for OD-C10's rear screws). OD-C10 itself has no inserts; it screws into OD-C02's two top-rail inserts (already counted) and OD-C11's two.
- `OD-F02` M3×8: +12 (OD-C08 flange 4, OD-C11 flanges 4, OD-C10 lid 4). The two OD-C08 board screws are **M3×6** (new row): OD-C08 RV01 F3 found that an M3×8 through the 1.562 board bottoms 0.44 in the 6.0 bore; M3×8 works only with a ≥ 0.5 washer.
- `OD-F09` cable ties: OD-C08 has two tie-slot pairs for the board's looms; +2 ties of the same 4.8 mm (or a 2.5 mm tie: the slots are 2 × 4).
- Then regenerate: `python tools/build_bom.py && python tools/build_progress.py`.

## chassis/README.md

- Row 9 `OD-C08`: modeled, path 1 (the Usta keeps the OEM PCB OD-E01 for this stage); OD-E02 (front buttons) belongs to OD-C09, not the tray.
- Row 11 `OD-C10`, `OD-C11`: modeled, both reviewed; OD-C11 took three builds (spec faults in 1.0 and 1.1, recorded).
- OD-C06 (tank dock) deferred: the tank stands on the table (the Usta, 2026-10-01); its tubes and the mains cord leave through OD-C11's three Ø12 pass-throughs at y 30.

## OD-000 placement

All three parts are modelled **in the machine frame** (X right, +Y up, +Z front,
plate top y 0): place each at the identity. OD-E01 sits on OD-C08 with board
x → −Z, y → +Y, z → +X, origin (84, 80, −100). The check assemblies already place
the neighbours: `chassis/reports/<part>/02_STEP_STL/od_c0?_assembly_C1_v0?.step`.
OD-C10 was checked against OD-C11's build v02, whose wall, ledge and bores are the
same as the delivered v03 (v03 changed only the outer gussets near the floor).

## Interfaces and keep-outs for later parts

- OD-C11's wall foot stands 2.3 from the rims of OD-C01's feet holes at (±110, −295):
  OD-C15's screw heads (Ø5.7) clear the wall by 1.15; the C15 keep-out cylinder
  (Ø8 × 2 above each hole) touches the wall's inner face (z −299) at 0.0 without overlap.
- OD-C10's rear skirt rests on OD-C11's wall top (a line plus two 5.9 mm² corner
  patches, accepted by the Usta). The lid's side and front edges are free until
  the side panels OD-C12/C13 and front panel OD-C09 exist: they should end at y 215
  under the lid's skirt (x ±117 … ±120, z −305 … +100 is the lid's 3 mm skirt).
- OD-C10 RV01 F1: the lid's centre of mass is 24 mm outside its four-column polygon
  on −X, so it settles onto the −X rest pad (0.5 over OD-C05) until the side panels
  carry its edges.
- OD-C08 occupies x 73 … 112, z −230 … −70, y 0 … 92 (with the board, to x ≈ 109.3).

## docs/HANDOVER.md (oguz-atolye)

- All three jobs at J5_DELIVER; next: the Usta's merge, then J6 close with
  PHYSICAL_OUTCOME pending the first prints (stiffness bench rows: OD-C08 REQ-06,
  OD-C10 REQ-08, OD-C11 REQ-09).
- Tool notes: `tools.core.common_volume` returned 0 mm³ for a real 3.65 mm³ overlap
  in fused topology at a seat plane (OD-C08 RV01 F5): it should fail closed. A
  `package_sent` recorded in J2_PLAN counts as a plan package and blocks the J3
  entry until a `package_done` closes it (OD-C10 EVENTS); record J3 first.
