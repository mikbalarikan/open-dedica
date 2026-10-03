"""D1 interface measurement for OD-C14 (plan only): OD-C11 cord hole, wall, nearest features; OD-C01 top and rear."""
import json, sys, platform
from pathlib import Path
import build123d, OCP
from build123d import Box, Pos, Cylinder, Axis
from tools.core import read_step, validity
from tools.measure import bore_census, locate_bore, envelope, clearance, feature_census

WS = Path(__file__).resolve().parents[1]
c11 = read_step(WS / "00_Spec/inputs/OD-C11_back_panel.step")
c01 = read_step(WS / "00_Spec/inputs/OD-C01_base_frame.step")
out = {"python": platform.python_version(), "build123d": build123d.__version__,
       "ocp": getattr(OCP, "__version__", "?")}
def r(res):
    return {"measured": res.measured, "unit": res.unit, "status": str(res.status), "at": res.at,
            "reason": getattr(res, "reason", None)}
out["c11_validity"] = {k: r(v) for k, v in validity(c11).items()}
out["c11_env"] = {k: r(v) for k, v in envelope(c11).items()}
out["c01_env"] = {k: r(v) for k, v in envelope(c01).items()}
cen = bore_census(c11)
loc = locate_bore(cen, (95.0, 30.0, -300.5), (0, 0, 1))
out["c11_hole"] = {k: r(v) for k, v in loc.items()}
out["c11_hole_detail"] = loc["diameter"].detail
# bores near the hole
near = [b for b in cen.detail["bores"] if abs(b["start"][0]-95) < 40 and abs(b["start"][1]-30) < 40]
out["c11_bores_near"] = near
# wall faces: planar faces of c11 normal to Z near the hole
from build123d import GeomType
wall = []
for s in c11.solids():
    for f in s.faces():
        if f.geom_type == GeomType.PLANE:
            bb = f.bounding_box()
            if bb.min.X <= 95 <= bb.max.X and bb.min.Y <= 30 <= bb.max.Y:
                n = f.normal_at()
                wall.append({"z": round(f.center().Z, 4), "normal": [round(n.X,4), round(n.Y,4), round(n.Z,4)],
                             "bbox": [round(bb.min.X,3), round(bb.min.Y,3), round(bb.min.Z,3), round(bb.max.X,3), round(bb.max.Y,3), round(bb.max.Z,3)]})
out["c11_faces_spanning_axis_xy"] = wall
# local features: clip C11 to a box around the hole and list the box
probe = Pos(95, 15, -290) * Box(40, 40, 40)
local = c11 & probe
out["c11_local_env"] = {k: r(v) for k, v in envelope(local).items()}
faces = []
for f in local.faces():
    bb = f.bounding_box(); n = f.normal_at() if f.geom_type == GeomType.PLANE else None
    faces.append({"type": str(f.geom_type), "n": None if n is None else [round(n.X,3), round(n.Y,3), round(n.Z,3)],
                  "bbox": [round(v,3) for v in (bb.min.X, bb.min.Y, bb.min.Z, bb.max.X, bb.max.Y, bb.max.Z)]})
out["c11_local_faces"] = faces
# clearance probes: whole-grommet envelope (Ø20 flange disc) and tie head box vs C11 and C01
flange = Pos(95, 30, -303) * Cylinder(10, 2)
out["flange_disc_to_c11"] = r(clearance(flange, c11))
out["flange_disc_to_c01"] = r(clearance(flange, c01))
collar = Pos(95, 30, -295.1) * Cylinder(5.7, 8.2)
out["collar_inside_to_c11"] = r(clearance(collar, c11))
tie = Pos(95, 30, -296.6) * (Cylinder(6.4, 4.8) - Cylinder(5.1, 4.8))
out["tie_ring_to_c11"] = r(clearance(tie, c11))
out["tie_ring_to_c01"] = r(clearance(tie, c01))
head = Pos(95, 30 + 6.4 + 3.0, -296.6) * Box(5, 6, 5)  # head above the band, 6 tall in Y
out["tie_head_to_c11"] = r(clearance(head, c11))
cord = Pos(95, 30, -295) * Cylinder(3.5, 70)
out["cord_to_c01"] = r(clearance(cord, c01))
out["cord_to_c11"] = r(clearance(cord, c11))
print(json.dumps(out, indent=1, default=str))
