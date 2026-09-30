import json
from pathlib import Path
from build123d import Cylinder, Pos, Rot, Solid
from tools.core import read_step
from tools.measure import min_wall, min_wall_wide
from tools.result import gate
J = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); W = J / "reviews/RV01_work"
p = read_step(J / "02_STEP_STL/od_c01_frame_C1_v02.step"); p = Solid(p.solids()[0].wrapped)
yc = lambda d, x, z, y0, h: Pos(x, y0 + h / 2, z) * Rot(90, 0, 0) * Cylinder(d / 2, h)
m = p + yc(4.0, -113, -42, -6, 6) - yc(4.0, -117.5, -42, -7, 8)
m = Solid(m.solids()[0].wrapped)
r = min_wall(m, spacing=0.7); rw = min_wall_wide(m, spacing=0.7)
out = {"mutant": "OD-C07 hole (-113, -42) moved to x -117.5: web 0.5 to the edge",
       "min_wall": [r.measured, r.status, r.at, r.reason], "D-01a": gate("D-01a", r, ">=", 0.8, band=0.005).status,
       "J-05": gate("J-05", r, ">=", 3.0, band=0.005).status, "U-06": gate("U-06", rw, ">=", 2.0, band=0.005).status,
       "wide": [rw.measured, rw.status]}
(W / "rv_e.json").write_text(json.dumps(out, indent=1, default=str)); print(out)
