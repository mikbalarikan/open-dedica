# Open Dedica — open-source DIY espresso machine

A community-built espresso machine: **genuine De'Longhi Dedica EC685 internals** (ULKA pump, 1300 W thermoblock, 51 mm portafilter, OEM valves and tubes) inside a **fully open, 3D-printable chassis**.

The only part of a Dedica you cannot buy as a spare is the group-head housing, which is molded into the case. If that part must be printed anyway, the whole chassis can be an open design.

> ⚠️ **Safety:** this machine runs on mains voltage (230 V / 120 V), heats water to ~125 °C and pressurizes it to 15 bar. Keep the wet side separated from the electric side, keep the 192 °C thermal cutoff (TCO) in circuit, test behind an RCD/GFCI, and never print load-bearing or heat-adjacent parts in PLA.

## Roadmap

| Phase | Goal | Tracking |
|---|---|---|
| **1. 3D scanning** ← *we are here* | Photos + caliper sheet + raw STL for every part the chassis touches | [`phase: scan`](../../issues?q=is%3Aissue+label%3A%22phase%3A+scan%22) |
| 2. STEP library | Rebuild each scan as clean parametric CAD, validate with a printed check-fixture | `phase: step` |
| 3. Chassis | Two-zone printed chassis designed around the STEP assembly; group-head housing first | `phase: chassis` |
| 4. Electronics | OEM PCB (path 1) vs ESP32 + SSR open controller (path 2) | `phase: electronics` |
| 5. Test & release | Pressure / leak / PAT tests, BOM + STEP + STL/3MF + build guide | `phase: test` |

**Milestone 1:** donor machine torn down, every part catalogued against the BOM, STEP library validated with printed check-fixtures, printed group-head housing bench-tested under pressure.

## How to help

Nobody is pre-assigned — **pick any open issue**. Start with [`good first issue`](../../issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) or the scan requests. Read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## Repository layout

```
docs/          SOURCING_GUIDE.md, BOM.md (generated) + bom.csv (source), PART_NUMBERING.md
tools/         build_bom.py — regenerates docs/BOM.md from docs/bom.csv
scans/         OD-Xnn_<name>/  photos/, calipers.md, raw STL/PLY   (phase 1)
step/          OD-Xnn_<name>.step  clean parametric models          (phase 2)
chassis/       printed chassis CAD + STL/3MF exports                     (phase 3)
electronics/   wiring, pinouts, firmware                                  (phase 4)
```

## Credits & references

- Zack Moss, *Open Source Espresso Machine for Makers*, MEng thesis, University of Sheffield, 2019 — reverse-engineered the EC685.M and proved the concept.
- [CaiJonas Dedica EC685/EC885 mod](https://github.com/CaiJonas/DeLonghi-Dedica-EC885-EC685-modification) — pressure/temperature sensor mod.
- Part codes: De'Longhi EC885.M exploded view (not redistributed here).

This project is not affiliated with or endorsed by De'Longhi. "De'Longhi" and "Dedica" are trademarks of their owners.

## License

Designs and documentation: [CC BY 4.0](LICENSE).
