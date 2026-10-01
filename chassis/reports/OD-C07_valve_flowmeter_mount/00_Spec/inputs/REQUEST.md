# REQUEST — OD-C07 valve and flowmeter mount (Open Dedica)

Received 2026-09-30 from the Usta (Ikbal, owner of `mikbalarikan/open-dedica`), through the project's standing instruction and the message of 2026-09-30 12:00 UTC. Data class PUBLIC (the project is CC BY 4.0; every input is public on GitHub).

## The Usta's words

Standing instruction (project instructions, Turkish, quoted):

> Kaldığın yerden devam et. Hedef: open-dedica'nın 3D basılabilir bütün tasarım parçaları (OD-G01, OD-C01…C16, OD-T01) ve OD-000 montaj teslimatı; sıra ve bitti tanımı `open-dedica/chassis/README.md`'de. […] Onaylanan çıktıları `open-dedica/chassis/` altına koy, montaj STEP'ine ekle, `docs/bom.csv`'yi güncelle, BOM ve panoyu yeniden üret, `claude/…` dalına push'la ve PR aç; sonra sıradaki parçanın işini aç. Usta'ya yalnız karar gereken yerde sor; açık soruları `A-##` satırı olarak ledger'a yaz ve ilerle.

Message of 2026-09-30 12:00 UTC (quoted):

> watch old ses'on and initiate parallel fable 5.1 agent sessions where they also design other parts

The project coordinator assigned this session the chassis parts OD-C06 … OD-C11 and, after reading `chassis/README.md`, narrowed it to OD-C07 as the only unblocked part of that range; the parallel ask overrides the one-part-at-a-time rule of the standing instruction.

## What OD-C07 is

`docs/bom.csv` row: `OD-C07, OD-C00, PRINT, "Valve & flowmeter mount (OPV reachable without disassembly)", qty 1, DESIGN, PETG, printed, issue #6, proposed`.

`chassis/README.md` order-of-work row 5: OD-C07 valve and flowmeter mount, designed against OD-H21 (anti-drip valve), OD-H22 (3-way valve), OD-H24 (flowmeter); blocked by nothing.

The three OEM parts exist as scan-rebuilt STEP files in `step/` (inputs of this job) with their reverse-engineering reports. None has caliper measurements: every dimension comes from the scan, scale unverified.

## Project rules that bind this part (from the inputs)

- `chassis/README.md`: one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated; the part is later placed in the OD-000 assembly by joints; `validated` needs a print and a fit check by the Usta.
- `docs/SOURCING_GUIDE.md` §3.5: "An open chassis should make the OPV accessible without disassembly." §6 chassis design rules: two-zone layout (wet zone separated from the electric zone, a leak drips to the tray), copy OEM anti-vibration, respect the thermal map (ABS/ASA near heat, PETG elsewhere, PLA nowhere structural), serviceability (OPV reachable, gaskets replaceable), piping rated 125 °C / 15 bar.
- Fasteners are the project standard: M3 heat-set inserts (OD-F01) and M3 × 8 screws (OD-F02).
- Machines: Creality K1C (enclosed: ASA, PC) and Anycubic Kobra Max 3 (large panels: PETG), 0.4 mm nozzles; build volumes not yet recorded in the machine files.
- The base frame OD-C01 (which OD-C07 mounts to) is not designed yet: it is designed after OD-C07, against the footprints of parts 2–6 of the order of work. OD-C07 therefore defines its own mounting footprint, which OD-C01 will follow.
- Not scanned yet: the tubes (OD-H25 flowmeter–pump tube, OD-W11 tank–flowmeter tube), the tank seat OD-W03 side of the water path, the pump OD-H01 position (OD-C03 is not designed yet).
