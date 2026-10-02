"""RV01 E-06 by sections: in a section plane, is each feature's sample point in the same cut region as a wall point?
Run on the delivered part and on the detached-boss mutant (positive control)."""
import json, sys
from build123d import Plane, Rectangle, Compound, Vertex
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from tools.core import read_step
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"
def regions(shape, axis, value):
    pl = {"x": Plane(origin=(value, 0, 0), z_dir=(1, 0, 0)), "y": Plane(origin=(0, value, 0), z_dir=(0, 1, 0))}[axis]
    cc = BRepAlgoAPI_Common(shape.wrapped, (pl * Rectangle(1000, 1000)).wrapped); cc.Build(); return Compound(cc.Shape()).faces()
def which(regs, pt):
    for i, f in enumerate(regs):
        d = BRepExtrema_DistShapeShape(Vertex(*pt).wrapped, f.wrapped); d.Perform()
        if d.Value() < 1e-6: return i
    return None
# (name, axis, value, feature point, wall point, extra point)
TIES = [("boss +90 to wall and ledge", "x", 93.0, (93, 207, -293), (93, 207, -300.5), (93, 213, -290)),
        ("boss -90 to wall and ledge", "x", -93.0, (-93, 207, -293), (-93, 207, -300.5), (-93, 213, -290)),
        ("inner gusset +X to wall and flange", "x", 74.0, (74, 15, -295), (74, 15, -300.5), (74, 2, -280)),
        ("inner gusset -X to wall and flange", "x", -74.0, (-74, 15, -295), (-74, 15, -300.5), (-74, 2, -280)),
        ("outer gusset +X to wall and flange", "x", 102.0, (102, 10, -295), (102, 10, -300.5), (102, 2, -280)),
        ("outer gusset -X to wall and flange", "x", -102.0, (-102, 10, -295), (-102, 10, -300.5), (-102, 2, -280)),
        ("ledge to wall", "x", 0.0, (0, 213, -290), (0, 213, -300.5), (0, 100, -300.5))]
def run(path):
    p = read_step(path); out = {}
    for name, ax, v, a, b, c in TIES:
        regs = regions(p, ax, v); ia, ib, ic = which(regs, a), which(regs, b), which(regs, c)
        out[name] = {"regions": len(regs), "feature": ia, "wall": ib, "other": ic, "tied": ia is not None and ia == ib == ic}
    return out
res = {"delivered": run(f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"), "mutant_boss90_detached": run(f"{W}/mutants/sections_boss90_detached.step")}
for k, v in res.items():
    print(k); [print("  ", n, r) for n, r in v.items()]
json.dump(res, open(f"{W}/m9_ties.json", "w"), indent=1)
