import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from build123d import Solid
from tools.core.shapes import faces as F, edges as E
from tools.measure.sampling import Inside
from OCP.BRepAdaptor import BRepAdaptor_Curve, BRepAdaptor_Surface
from OCP.GeomAbs import GeomAbs_Cylinder
import numpy as np, json
s = Solid(solids(read_step(STEP))[0])
out = {}
# foot counterbore cylinder faces: exact min z of their boundary edges by dense sampling
for f in F(s):
    a = BRepAdaptor_Surface(f)
    if a.GetType() != GeomAbs_Cylinder: continue
    loc = a.Cylinder().Location()
    if abs(a.Cylinder().Radius() - 3.25) > 1e-6 or loc.X() == 0: continue
    zs = []
    for e in E(f):
        c = BRepAdaptor_Curve(e)
        for t in np.linspace(c.FirstParameter(), c.LastParameter(), 2001):
            p = c.Value(t); zs.append((p.Z(), p.X(), p.Y()))
    zmin = min(zs)
    out[f"cb({loc.X():.0f},{loc.Y():.0f})"] = {"edge_zmin": zmin, "curve_types": [BRepAdaptor_Curve(e).GetType().name for e in E(f)]}
# material probe just below the analytic rim at (35, -68.75+0.01, 164.81-0.05): must be air (column inside)
ins = Inside(s.wrapped)
out["probe_below_rim_(35,-68.76,164.76)"] = ins.state((35, -68.76, 164.76)).__repr__() if hasattr(ins, "state") else None
out["probe_above_rim_(35,-68.60,165.2)"] = repr(ins.state((35, -68.60, 165.2)))
# plate underside and top faces
from faces_lib import listing
for r in listing(s):
    if r["kind"] == "plane" and r.get("normal") and abs(abs(r["normal"][2]) - 1) < 1e-12:
        out.setdefault("horizontal_planes", []).append((round(r["centre"][2], 6), r["normal"][2], round(r["area"], 3), [round(v, 3) for v in r["centre"]]))
print(json.dumps(out, indent=1, default=str))
dump("m8_probe", out)
