# REQUEST — OD-C15 printed TPU feet (Open Dedica)

Received 2026-10-01 from the Usta (Ikbal, owner of `mikbalarikan/open-dedica`), through the project's standing instruction and the message of 2026-10-01 10:58 UTC. Data class PUBLIC (the project is CC BY 4.0; every input is public on GitHub).

## The Usta's words

Standing instruction (project instructions, Turkish, quoted):

> Kaldığın yerden devam et. Hedef: open-dedica'nın 3D basılabilir bütün tasarım parçaları (OD-G01, OD-C01…C16, OD-T01) ve OD-000 montaj teslimatı; sıra ve bitti tanımı `open-dedica/chassis/README.md`'de. […] Usta'ya yalnız karar gereken yerde sor; açık soruları `A-##` satırı olarak ledger'a yaz ve ilerle.

Message of 2026-10-01 10:58 UTC (quoted):

> what can start now please initiate it
>
> water tank is transparent hard to scan we can just use the tray that step converted as reference and i will hold water tank on the table myself no need to design for it now
>
> c08 i will use original pcb for this stage

The project coordinator assigned this session OD-C15, the TPU feet, as a part that can start now: OD-C01, which the feet screw to, is on open-dedica `main` (PR #46).

## What OD-C15 is

`docs/bom.csv` row: `OD-C15, OD-C00, PRINT, "Foot (alternative to OD-C25/526)", qty 4, DESIGN, TPU, printed, proposed` (the "526" is read as OD-C26). The OEM alternative is the rubber foot pads OD-C25 (ref 34, 5313229381, ×2) and OD-C26 (ref 76, 5313274719, ×2), not scanned or measured.

`chassis/README.md` order-of-work row 13: OD-C14 cable grommets, OD-C15 feet (TPU), designed against OD-C01 and the OD-E06 cord; blocked by nothing.

## Project rules that bind this part (from the inputs)

- `chassis/README.md`: one parametric build script, STEP (mm, one named solid) and STL/3MF per printed part, with its print orientation and material stated; the part is later placed in the OD-000 assembly by joints; `validated` needs a print and a fit check by the Usta.
- `docs/SOURCING_GUIDE.md` §6 rule 2: "Copy OEM anti-vibration. Pump in rubber sleeve + spring, decoupled from panels; TPU feet. Rigid mounts = a machine that walks across the counter." §3.10: "Rubber feet 34/76 or printed TPU feet".
- OD-C01 (delivered, `OD-C01_base_frame.step`, its spec 1.2 REQ-05 and A-12): four Ø3.4 through-holes at (x ±110, z +90) and (x ±110, z −295) in the OD-C01 frame (X right, +Y up, +Z front, plate top y = 0), plate 6.0 thick, 240 × 405, corners R10; A-12 says the feet are "screwed from below through Ø3.4 holes … into inserts of the feet themselves" and is OPEN until the Usta picks the feet.
- Fasteners are the project standard: M3 heat-set inserts (OD-F01), M3 screws ISO 7380 / DIN 912 A2 (OD-F02 M3×8, OD-F10 M3×12).
- Machines: Creality K1C and Anycubic Kobra Max 3, 0.4 mm nozzles; the machine files record PLA only and no build volume.
