"""RV01: list every face (kind, normal, bbox, area) of the exported STEP for the positional feature census."""
import json
from tools.core import read_step
J = "/root/oguz-jobs/20261001-od-c11-back-panel"
p = read_step(f"{J}/02_STEP_STL/od_c11_back_C1_v03.step")
rows = []
for f in p.faces():
    bb = f.bounding_box()
    t = f.geom_type.name if hasattr(f.geom_type, "name") else str(f.geom_type)
    n = None
    if t == "PLANE":
        n = tuple(round(c, 4) for c in f.normal_at(f.center()))
    rows.append(dict(kind=t, n=n, area=round(f.area, 3), lo=tuple(round(c, 3) for c in bb.min), hi=tuple(round(c, 3) for c in bb.max)))
rows.sort(key=lambda r: (r["kind"], r["n"] or (), r["lo"]))
for r in rows: print(r)
json.dump(rows, open(f"{J}/reviews/RV01_work/m2_faces.json", "w"), indent=1)
