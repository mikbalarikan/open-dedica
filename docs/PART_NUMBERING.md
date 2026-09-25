# Part numbering

Every part in the project — OEM spare, printed part, screw, assembly, test fixture — has one **part number** `OD-Xnn`.
The same number is used in the BOM, CAD file names, scan folders, issue titles and PR titles.

## Format

```
OD-Xnn
   │└┴─ item within the group (01–99)
   └─── group letter
```

| Letter | Group | Examples |
|---|---|---|
| `OD-000` | Top assembly (whole machine) | |
| **H** | **H**ydraulic core — pump, thermoblock, valves, flowmeter | `OD-H01` pump, `OD-H10` thermoblock sub-assy, `OD-H11` thermoblock |
| **G** | **G**roup head & portafilter | `OD-G01` printed group head housing, `OD-G10` portafilter |
| **W** | **W**ater path — tank, tubes, springs, O-rings, clips | `OD-W01` water tank assy |
| **E** | **E**lectronics — `E01…E49` OEM path 1, `E51…E99` open-controller path 2 | `OD-E01` power PCB, `OD-E51` ESP32 |
| **C** | **C**hassis & body — `C01…C19` printed chassis, `C21…` tray / cup rest / feet | `OD-C03` pump cradle |
| **F** | **F**asteners, standard hardware & consumables | `OD-F01` M3 heat-set insert |
| **S** | **S**team system (phase 2) | `OD-S01` steam valve |
| **R** | OEM parts we do not use — **R**eference only | `OD-R01` OEM upper cover |
| **T** | **T**est fixtures & rigs | `OD-T01` group head pressure rig |

Rules:

1. **`OD-X00` is the assembly of its group** (`OD-H00` hydraulic core, `OD-C00` chassis). Sub-assemblies inside a group use a round ten (`OD-H10` thermoblock sub-assembly, `OD-G10` portafilter).
2. **Numbers are never reused.** A dropped part keeps its number with status `deferred`; a new part takes the next free number in its group.
3. **Variants of the same part** get a letter suffix: `OD-G01A`, `OD-G01B` (e.g. two group-head housing designs being compared). The winner keeps the plain number.
4. **Check fixtures** use the part number plus `-FX`: `OD-H11-FX` is the check-fixture for the thermoblock. They are not listed in the BOM.
5. **Revisions are git history**, not file names. Tag releases (`v0.1`, …) instead of `_rev2` files.
6. The BOM keeps the De'Longhi **Ref#** and **OEM code** next to every OEM part, so ordering and the exploded view stay traceable.

## File and folder names

```
<part_no>_<short_name>
```

| Where | Example |
|---|---|
| Scan folder | `scans/OD-H11_thermoblock/` |
| STEP | `step/OD-H11_thermoblock.step` |
| Assembly STEP | `step/OD-H10_thermoblock_assy.step` |
| Printed part | `chassis/OD-C03_pump_cradle.step` + `.3mf` |
| Check fixture | `step/OD-H11-FX_thermoblock_fixture.step` |

`short_name`: lowercase, `snake_case`, ≤ 30 characters.

In CAD, name the **body / component** with the part number too (`OD-H11 Thermoblock`) so assemblies stay readable after STEP export.

## Adding a part

1. Add a row to [`bom.csv`](bom.csv) with the next free number in the right group.
2. Run `python tools/build_bom.py` to regenerate [BOM.md](BOM.md).
3. Commit both files in the same PR.
