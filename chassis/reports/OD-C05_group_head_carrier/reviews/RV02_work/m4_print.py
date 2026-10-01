import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from faces_lib import listing, flat_ceilings, shared_edges
from build123d import Solid, Pos, Cylinder, Box, Polyline, make_face, extrude, Plane, Location, Align
from tools.measure import overhang_census, radial_extent
from tools.core.validity import validity
from tools.core.shapes import faces as F
import numpy as np, math
path = Path(sys.argv[1]) if len(sys.argv) > 1 else STEP
tag = sys.argv[2] if len(sys.argv) > 2 else "nominal"
s = Solid(solids(read_step(path))[0])
res = {}
L = listing(s)
res["listing"] = L
down = [r for r in L if r.get("down")]
res["downward"] = down
# exception faces by position: flat downward rings at z -27.94 about (+-44,+-44) and at z 176.06 about (+-35,-72/-92)
def is_exc(r):
    if not r.get("down") or r.get("angle") is None or r["angle"] > 1e-6: return False
    x, y, z = r["centre"]
    plate = abs(z + 27.94) < 1e-6 and abs(abs(x) - 44) < 1e-6 and abs(abs(y) - 44) < 1e-6
    foot = abs(z - 176.06) < 1e-6 and abs(abs(x) - 35) < 1e-6 and (abs(y + 72) < 1e-6 or abs(y + 92) < 1e-6)
    return plate or foot
exc = [r for r in down if is_exc(r)]
rest = [r for r in down if not is_exc(r)]
res["exception_faces"] = exc; res["other_downward"] = rest
res["least_other_deg"] = min((r["angle"] for r in rest), default=90.0)
res["least_exception_deg"] = min((r["angle"] for r in exc), default=None)
res["flat_ceilings_outside_exception"] = [r for r in rest if r["angle"] < 1.0]
# plugged part for overhang_census: fill the eight counterbores (to their floors) with Ø6.5 plugs trimmed by the roof prism
plugs = None
for x in (44, -44):
    for y in (44, -44):
        p = Pos(x, y, -28.94) * Cylinder(3.25, 2.0)
        plugs = p if plugs is None else plugs + p
roof = extrude(make_face(Plane.YZ * Polyline((-58, 154.06), (-78, 174.06), (-98, 154.06), (-98, 180.06), (-58, 180.06), close=True)), amount=55, both=True)
for x in (35, -35):
    for y in (-72, -92):
        p = (Pos(x, y, 163.06) * Cylinder(3.25, 26.0)) & roof
        plugs = plugs + p
plugged = s + plugs
pl = Solid(solids(plugged)[0]) if len(solids(plugged)) == 1 else plugged
res["plugged_nsolids"] = len(solids(plugged))
res["plugged_validity"] = validity(pl)
res["plugged_volume_added"] = pl.volume - s.volume
res["overhang_plugged"] = overhang_census(pl, build_dir=(0, 0, 1))
res["overhang_whole"] = overhang_census(s, build_dir=(0, 0, 1))
Lp = listing(pl)
res["plugged_down"] = [r for r in Lp if r.get("down")]
# roof / window geometry: peaks
roofs = [r for r in rest if abs(r["centre"][0]) < 1e-6 and r["centre"][2] > 150 and abs(abs(r["normal"][1]) - 0.7071) < 1e-3] if rest and "normal" in rest[0] else []
dfaces = F(s)
rf = [dfaces[r["i"]] for r in rest]
pairs = []
for a in range(len(rest)):
    for b in range(a + 1, len(rest)):
        se = shared_edges(s, rf[a], rf[b])
        if se:
            pairs.append({"a": rest[a]["i"], "b": rest[b]["i"], "na": rest[a].get("normal"), "nb": rest[b].get("normal"), "edges": se,
                          "za": (rest[a]["zmin"], rest[a]["zmax"]), "zb": (rest[b]["zmin"], rest[b]["zmax"])})
res["downward_pairs"] = pairs
# REQ-04 radial extent inner, whole ray, every 10 deg, 5 levels
rad = []
for z in (-29.9, -29.44, -27.44, -25.44, -24.98):
    for a in range(0, 360, 10):
        r = radial_extent(s, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, z, side="inner")
        rad.append({"z": z, "a": a, "r": r.measured, "status": r.status, "reason": r.reason, "at": r.at})
res["radial"] = rad
ok = [x for x in rad if x["status"] == "MEASURED"]
res["radial_min"] = min(ok, key=lambda x: x["r"]) if ok else None
res["radial_n"] = (len(rad), len(ok))
dump(f"m4_print_{tag}", res)
print("done", tag)
