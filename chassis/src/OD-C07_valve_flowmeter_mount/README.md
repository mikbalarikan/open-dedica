# OD-C07 valve and flowmeter mount — build source

Parametric build123d script of `chassis/OD-C07_valve_flowmeter_mount.step` (`.stl`,
`.3mf`), designed with the OGUZ Atölye pipeline; the job record with the spec, plan,
report and the independent review is `chassis/reports/OD-C07_valve_flowmeter_mount/`.

- `build_od_c07_mount.py`: the part, with every dimension in its `Params` structure;
  places OD-H22 and OD-H24 by joints for the check assembly.
- `check_od_c07_mount.py`: the gate checks (spec §5) run on the exported STEP.

Run from the `oguz-atolye` repository root, in its tools venv, with the job workspace
recreated as the record's README describes:

```
uv run tools/run.py python <workspace>/01_CAD/build_od_c07_mount.py
```

Frame: bottom face z = 0, +Z up (print direction), origin on the flowmeter axis, the
valve axis at (62, 0). Accepted deviations: spec §5 named exceptions (RV01 F1–F4).
