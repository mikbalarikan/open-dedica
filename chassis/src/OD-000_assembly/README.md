# OD-000 top assembly — build script

`build_od000.py` places every printed part of `chassis/` and every OEM part of
`step/` that has a joint, in the machine frame (X right, +Y up, +Z front, plate top
y = 0), and writes `chassis/OD-000_open_dedica_assembly.step` (AP242, mm) with four
named sub-assembly compounds:

| Sub-assembly | Solids (each labelled with its part number) |
|---|---|
| `OD-C00` printed chassis | OD-C01 … C05, C07 … C13; OD-C14-A/-B (two grommet halves); OD-C15-RF/LF/RR/LR (feet); OD-C16-R1…R3, L1…L3 (brackets) |
| `OD-G00` group head | OD-G01 housing, OD-G04 gasket support, OD-G10 portafilter (locked) |
| `OD-H00` hydraulics | OD-H01 pump, OD-H11 thermoblock, OD-H22 3-way valve, OD-H24 flowmeter |
| `OD-E00` electronics (path 1) | OD-E01 power PCB, OD-E02 control board |

33 solids. Printed parts are orange, OEM parts grey (STEP colours and renders).

## Placements

One table, `PLACEMENTS`, at the top of the script: per part its sub-assembly, its
file, its parent frame (`FRAMES`: machine, housing, OD-C03, OD-C04, OD-C07) and its
pose in that frame as a rigid joint `(origin, x_dir, z_dir)`, taken from
`chassis/README.md` ("Frames for OD-000", "OD-000 placements handed over by the part
jobs"). OD-G04, OD-G10 (housing frame) and OD-H22, OD-H24 (mount frame) take the
`Location` their part's check assembly carries (`od_g01_assembly_C1_v03.step`, the
measured locked rim z −11.251; `od_c07_assembly_C1_v01.step`). No pose is fitted to
a bounding box.

`CROSS_CHECKS` then compares each placed solid's box with the same solid in every
check assembly under `chassis/reports/*/02_STEP_STL/` that holds it (tolerance
0.05 mm); the result is in `clash_report.json` / `.md`.

## Left out

- `OD-W00` water path: the tank OD-W01/W02 is not scanned and the dock OD-C06 is
  deferred (the tank stands on the table; its tubes leave through OD-C11).
- `OD-G09` OEM bayonet cup: reference geometry that OD-G01 replaces (BOM qty 0); its
  frame is the housing frame, so `--with-g09` adds it at the housing identity for
  an overlay.
- `OD-H21` anti-drip valve: it sits in the tube run and has no joint yet.
- `OD-S00` steam system (phase 2), `OD-T01` (bench fixture), screws, inserts,
  spacers, tubes and wiring (not modelled).

## Run

From the `oguz-atolye` root, in the tools venv:

```
uv run tools/run.py python <open-dedica>/chassis/src/OD-000_assembly/build_od000.py \
    [--plate <OD-C01.step>] [--out <assembly.step>] [--clash <clash_report.json>] \
    [--no-clash] [--glb-dir <dir>] [--with-g09]
```

`--plate` defaults to `chassis/OD-C01_base_frame.step`; pass a new plate (revision
B) to rebuild against it. The run takes about a minute without the clash report,
longer with it (one soundness check per source solid, then one distance and one
boolean per near pair).

Outputs: the STEP (re-read after writing: schema, solid count, labels), and beside
this script `clash_report.json` (placements, cross-check, every near pair) and
`clash_report.md` (the summary). The interference volume is fail-closed as
`tools.core.common_volume`: a pair with an unsound solid (most scan-rebuilt OEM
parts are not valid B-reps) is INCONCLUSIVE, with the raw boolean kept apart as a
lead only, and the least clearance beside it.

`--glb-dir` writes `od000_closed.glb` and `od000_open.glb` (lid OD-C10 and left
panel OD-C12 hidden) in the machine frame, Y up, for the three.js / playwright
render pipeline (a viewer without the Z-up rotation the part renders use).
