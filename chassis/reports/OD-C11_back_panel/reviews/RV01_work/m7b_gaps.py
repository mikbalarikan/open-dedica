"""RV01: pass-through gap behind the wall (to material in front of the wall face, z > -299), and remaining section pictures."""
import json, sys
from pathlib import Path
from build123d import Pos, Cylinder, Box, Location
from tools.core import read_step, common_volume
from tools.measure import clearance
from tools.drawing import write_sections
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"
STEP = sys.argv[1] if len(sys.argv) > 1 else f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"
p = read_step(STEP)
front = p.intersect(Box(300, 300, 30).moved(Location((0, 100, -299.0 + 15))))
out = {}
for (x, y) in [(95, 30), (-100, 30), (-84, 30)]:
    cyl = Pos(x, y, (-299 - 277) / 2) * Cylinder(6.0, 22.0)
    c = clearance(cyl, front)
    out[f"gap_{x}"] = {"gap": c.measured, "at": c.at, "detail": c.detail, "common_full": common_volume(cyl, p).measured}
    print(x, out[f"gap_{x}"])
json.dump(out, open(f"{W}/m7b_gaps.json", "w"), indent=1, default=str)
if len(sys.argv) <= 2:
    folder = Path(W) / "sections"
    for name, view, thr in [("y206", "top", (0, 206, -295)), ("zm290", "front", (0, 100, -290)), ("x100p5", "left", (100.5, 15, -290)), ("x110", "left", (110, 100, -295))]:
        try:
            ws = write_sections(p, folder / name, part="od_c11_back_RV01", version=3, views=(view,), through=thr)
            for w in ws: print("png", w.path, w.checks["nothing_clipped"].measured)
        except Exception as e: print(name, "refused", e)
