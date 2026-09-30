import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from tools.core.validity import validity
from tools.core.step import read_schema, read_length_unit, labels, node_labels, compare_step, step_roundtrip
from tools.measure import envelope, feature_census, bore_census, locate_bore, mass_properties
from tools.measure.sampling import kind
c = carrier()
res = {}
res["labels"] = labels(c); res["node_labels"] = node_labels(c)
res["schema"] = read_schema(STEP); res["unit"] = read_length_unit(STEP)
res["n_solids"] = len(solids(c)); res["n_faces"] = len(faces(c))
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL, TopAbs_FACE, TopAbs_SOLID
def count(shape, t, avoid=None):
    e = TopExp_Explorer(occ(shape), t) if avoid is None else TopExp_Explorer(occ(shape), t, avoid)
    n = 0
    while e.More(): n += 1; e.Next()
    return n
res["shells"] = count(c, TopAbs_SHELL)
res["free_shells"] = count(c, TopAbs_SHELL, TopAbs_SOLID)
res["free_faces"] = count(c, TopAbs_FACE, TopAbs_SHELL)
res["validity"] = validity(c)
res["envelope"] = envelope(c)
res["census"] = feature_census(c)
bc = bore_census(c)
res["bores"] = bc
locs = {}
for (x, y, z) in [(44,44,-26.44),(-44,44,-26.44),(44,-44,-26.44),(-44,-44,-26.44)]:
    locs[f"hole({x},{y})"] = locate_bore(bc, (x, y, z), (0,0,1))
    locs[f"cb({x},{y})"] = locate_bore(bc, (x, y, -28.94), (0,0,1))
for (x, y) in [(35,-72),(-35,-72),(35,-92),(-35,-92)]:
    locs[f"fhole({x},{y})"] = locate_bore(bc, (x, y, 178.06), (0,0,1))
    locs[f"fcb({x},{y})"] = locate_bore(bc, (x, y, 175.5), (0,0,1))
res["locate"] = locs
res["mass"] = mass_properties(c, 1070)
res["compare_self"] = compare_step(c, STEP)
res["roundtrip"] = step_roundtrip(c, OUT / "rt_carrier.step", timestamp="2026-09-30T00:00:00")
# face listing
fl = []
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
for i, f in enumerate(faces(c)):
    g = GProp_GProps(); BRepGProp.SurfaceProperties_s(f, g)
    cm = g.CentreOfMass()
    fl.append({"i": i, "kind": kind(f), "area": g.Mass(), "c": (round(cm.X(),3), round(cm.Y(),3), round(cm.Z(),3))})
res["faces"] = fl
dump("m1_basic", res)
print("done")
