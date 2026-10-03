# OD-C15 feet — integration notes for the OD-G01 thread

Job `20261001-od-c15-feet`, build v01, spec 1.2, RV01 `APPROVED_ASSUMPTION_CONDITIONAL`
(no findings). Deliverables on open-dedica branch `claude/project-thread-o9rnj8`
(PR #47, merged to main 2026-10-01): `chassis/OD-C15_foot.step/.stl/.3mf`,
`chassis/src/OD-C15_foot/`, record `chassis/reports/OD-C15_foot/`.
The shared files below are yours to change; nothing here was edited by the C15 job.

## docs/bom.csv

- `OD-C15`: status `proposed` → `modeled`; name may read "Foot (TPU, Ø18 × 10, captive M3 nut; alternative to OD-C25/C26)" (the current "OD-C25/526" is read as OD-C26); material `TPU 95A (A-03)`; source `printed (Creality K1C)`; qty 4.
- New fasteners (4 each), or fold into existing rows:
  - M3×12 ISO 7380 A2 button head, one per foot, from the plate top. Same screw as `OD-F10`: raise that row's qty from 4 to 8 and add "and the four OD-C15 feet" to its name, or add a new `OD-F11` row.
  - ISO 4032 M3 A2 hex nut ×4, captive in the feet (new row, e.g. `OD-F12`). Optional: a nylon-insert nut ISO 10511 M3 then needs M3×16 (spec A-07).
- `OD-C25` / `OD-C26` (OEM pads) stay as the alternative (spec A-10, concept C2 deferred).
- Then regenerate: `python tools/build_bom.py && python tools/build_progress.py`.

## chassis/README.md

- Order-of-work row 13: `OD-C15` modeled, RV01 approved on assumptions (TPU 95A, K1C); Ø18 × 10 puck, M3×12 from the top into a captive M3 nut.
- Interfaces to OD-C01: the feet use the four Ø3.4 through-holes at (±110, +90) and (±110, −295); no inserts in the plate.
- Keep-out for later parts (spec A-09): a Ø8 × 2.0 cylinder above each foot hole on the plate top (y 0 … 2.0) holds the screw head (Ø5.7 × 1.65). OD-C12, OD-C13, OD-C16 and OD-C06 must leave it free.
- OD-C01 A-12 ("screwed from below into inserts of the feet") is superseded by OD-C15 A-02 (screw from above, captive nut): worth a line on the OD-C01 row.

## OD-000 placement (joint frames)

- Foot frame: origin at the centre of the top face (against the plate), +Z down in the machine (print direction), foot z 0 … 10.
- Joint into the OD-C01 (machine) frame: foot x → X, y → +Z, z → −Y; origins (+110, −6, +90), (−110, −6, +90), (+110, −6, −295), (−110, −6, −295). Counter faces land at y −16.0: the whole machine stands 16 mm above the counter at the plate top; OD-000 may put the counter at y −16.
- Screw (envelope only): head on y 0 … 1.65 at (±110, ±z), tip at y −12.0. Nut: foot z 2.5 … 4.9 (y −8.5 … −10.9).
- The check assembly `chassis/reports/OD-C15_foot/02_STEP_STL/od_c15_assembly_C1_v01.step` already places plate + 4 feet + screws + nuts that way.

## docs/HANDOVER.md (oguz-atolye)

- C15 is at J5_DELIVER; next: the Usta's merge, then J6 close with PHYSICAL_OUTCOME pending the first printed foot (A-06 nut grip, A-07 creep, A-03 TPU grade).
- Tool notes from this job: `overhang_census` is INCONCLUSIVE on a cone at exactly 45° (sampling bound ~0.01°), so specs should put printed chamfers at ≥ 46° or 60°; the session's file hook blocked the designer's REPORT write once (the orchestrator placed the returned text verbatim).
