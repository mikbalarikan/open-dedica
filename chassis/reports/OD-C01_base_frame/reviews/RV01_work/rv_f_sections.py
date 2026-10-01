import json
from pathlib import Path
from build123d import Box, Pos, Solid
from tools.core import read_step
from tools.measure.wall import min_wall_mesh
J = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); W = J / "reviews/RV01_work"
p = read_step(J / "02_STEP_STL/od_c01_frame_C1_v02.step"); p = Solid(p.solids()[0].wrapped)
t = 0.002
out = {}
for name, slab in {"z-42": Pos(0, -3, -42) * Box(300, 20, t), "x-113": Pos(-113, -3, -100) * Box(t, 20, 500),
                   "y-3": Pos(0, -3, -100) * Box(300, t, 500), "y-0.001": Pos(0, -0.001, -100) * Box(300, t, 500),
                   "y-5.999": Pos(0, -5.999, -100) * Box(300, t, 500), "z-148": Pos(0, -3, -148) * Box(300, 20, t)}.items():
    c = p & slab
    sol = c.solids()
    out[name] = {"area": round(sum(s.volume for s in sol) / t, 3), "pieces": len(sol),
                 "ybox": [round(c.bounding_box().min.Y, 4), round(c.bounding_box().max.Y, 4)]}
r = min_wall_mesh(J / "02_STEP_STL/od_c01_frame_C1_v02.stl")
out["min_wall_mesh"] = [r.measured, r.status, r.at, r.reason, r.detail.get("vertex_precision_mm")]
(W / "rv_f.json").write_text(json.dumps(out, indent=1, default=str)); print(json.dumps(out, default=str))
