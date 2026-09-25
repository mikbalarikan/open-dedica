# Part numbering

Every part in the project — OEM spare, printed part, screw, assembly, test fixture — has one **part number** `OD-NNN`.
The same number is used in the BOM, CAD file names, scan folders, issue titles and PR titles.

## Format

```
OD-NNN
   │└┴─ item within the group (01–99)
   └─── group
```

| Range | Group |
|---|---|
| `OD-000` | Top assembly (whole machine) |
| `OD-1xx` | Hydraulic core — pump, thermoblock (`OD-110` sub-assembly), valves, flowmeter |
| `OD-2xx` | Group head & portafilter |
| `OD-3xx` | Water path — tank, tubes, springs, O-rings, clips |
| `OD-4xx` | Electronics — `OD-401…449` OEM path 1, `OD-451…499` open-controller path 2 |
| `OD-5xx` | Chassis & body — `OD-501…519` printed chassis, `OD-521…` tray / cup rest / feet |
| `OD-6xx` | Standard hardware & consumables |
| `OD-7xx` | Steam system (phase 2) |
| `OD-8xx` | OEM parts we do **not** use — reference only |
| `OD-9xx` | Fixtures & test rigs |

Rules:

1. **`OD-x00` is the assembly of its group.** Sub-assemblies inside a group use a round ten (`OD-110` thermoblock sub-assembly, `OD-210` portafilter).
2. **Numbers are never reused.** A dropped part keeps its number with status `deferred`; a new part takes the next free number in its group.
3. **Variants of the same part** get a letter suffix: `OD-201A`, `OD-201B` (e.g. two group-head housing designs being compared). The winner keeps the plain number.
4. **Check fixtures** use the part number plus `-FX`: `OD-111-FX` is the check-fixture for the thermoblock. They are not listed in the BOM.
5. **Revisions are git history**, not file names. Tag releases (`v0.1`, …) instead of `_rev2` files.
6. The BOM keeps the De'Longhi **Ref#** and **OEM code** next to every OEM part, so ordering and the exploded view stay traceable.

## File and folder names

```
<part_no>_<short_name>
```

| Where | Example |
|---|---|
| Scan folder | `scans/OD-111_thermoblock/` |
| STEP | `step/OD-111_thermoblock.step` |
| Assembly STEP | `step/OD-110_thermoblock_assy.step` |
| Printed part | `chassis/OD-503_pump_cradle.step` + `.3mf` |
| Check fixture | `step/OD-111-FX_thermoblock_fixture.step` |

`short_name`: lowercase, `snake_case`, ≤ 30 characters.

In CAD, name the **body / component** with the part number too (`OD-111 Thermoblock`) so assemblies stay readable after STEP export.

## Adding a part

1. Add a row to [`bom.csv`](bom.csv) with the next free number in the right group.
2. Run `python tools/build_bom.py` to regenerate [BOM.md](BOM.md).
3. Commit both files in the same PR.
