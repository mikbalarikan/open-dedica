"""v03 fact (not a gate; E-11, P2): the gap between each pass-through's opening and the panel's
material in front of the wall, for the nominal export and every sweep run. Each hole is taken as
measured (bore_census on the re-imported STEP: diameter, axis), extended as a cylinder from its
measured end at the wall's inner face to z -277; reported: common volume with the panel, and
clearance to the panel's material at z >= that end (flanges, gussets, ledge, bosses)."""
import json
from pathlib import Path

import numpy as np
from build123d import Align, Box, Cylinder, Pos

from tools.core import common_volume, read_step
from tools.measure import bore_census, clearance

WS = Path(__file__).resolve().parents[2]
steps = {"nominal_export": WS / "02_STEP_STL" / "od_c11_back_C1_v03.step"}
for d in sorted((WS / "01_CAD" / "sweep_v03").iterdir()):
    s = list(d.glob("od_c11_back_C1_v03_*.step"))
    if s:
        steps[d.name] = s[0]
out = {}
for run, path in steps.items():
    one = read_step(path).solids()[0]
    rows = {}
    for b in bore_census(one).detail["bores"]:
        a = np.array(b["axis_dir"], float)
        if abs(abs(a[2]) - 1.0) > 1e-6 or abs(b["diameter"] - 12.0) > 0.5:
            continue
        x, y = b["start"][0], b["start"][1]
        z_in = max(b["start"][2], b["end"][2])
        cyl = Pos(x, y, z_in) * Cylinder(0.5 * b["diameter"], -277.0 - z_in, align=(Align.CENTER, Align.CENTER, Align.MIN))
        front = one & (Pos(-1000, -1000, z_in) * Box(2000, 2000, 30.0, align=(Align.MIN, Align.MIN, Align.MIN)))
        cv, cl = common_volume(one, cyl), clearance(front, cyl)
        rows[f"x{x:.1f}_y{y:.1f}"] = {"diameter": round(b["diameter"], 4), "z_inner_end": round(z_in, 4),
                                      "common_mm3": cv.measured, "clearance_mm": cl.measured, "at": cl.at}
    out[run] = rows
(WS / "01_CAD" / "probe" / "probe_passthrough_gap_v03.json").write_text(json.dumps(out, indent=1, default=str))
for run, rows in out.items():
    print(run, {k: (v["diameter"], v["common_mm3"], round(v["clearance_mm"], 4)) for k, v in rows.items()})
