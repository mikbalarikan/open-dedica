"""WP-02 probe (J2): OD-G04 hub tube as placed by the OD-G01 REPORT v02 section 5 joint."""
import json, math
from pathlib import Path
from build123d import Axis, Cylinder, Location, Box
from tools.core import read_step
from tools.measure import radial_extent, envelope

WS = Path(__file__).resolve().parents[2]
g04 = read_step(WS / "00_Spec/inputs/OD-G04_brewing_gasket_support.step")
g04p = g04.rotate(Axis.Z, 6.05).translate((0, 0, -6.82))
out = {}
# annulus r 0 .. 11.0 below the floor z -19.94 (hub tube region, inside pair A at r >= 12.01)
core = Cylinder(11.0, 10.0, align=None).moved(Location((0, 0, -19.94 - 10.0)))
hub = g04p & core
ss = hub.solids() if hub else []
bb = hub.bounding_box()
out["hub_below_floor_bbox"] = [round(v, 4) for v in (bb.min.X, bb.min.Y, bb.min.Z, bb.max.X, bb.max.Y, bb.max.Z)]
out["hub_below_floor_volume"] = round(sum(s.volume for s in ss), 4)
out["hub_bottom_face_kinds"] = sorted({f.geom_type.name for f in hub.faces() if abs(f.center().Z - bb.min.Z) < 0.05})
# hub OD and ID at z -21.0 over 36 angles, window r <= 11.5
od, idr = [], []
for a in range(0, 360, 10):
    r = radial_extent(g04p, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, -21.0, side="outer", r_min=0, r_max=11.5)
    q = radial_extent(g04p, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, -21.0, side="inner", r_min=0, r_max=11.5)
    if r.status == "MEASURED": od.append(r.measured)
    if q.status == "MEASURED": idr.append(q.measured)
out["hub_outer_r_at_z-21"] = [round(min(od), 4), round(max(od), 4), len(od)] if od else None
out["hub_inner_r_at_z-21"] = [round(min(idr), 4), round(max(idr), 4), len(idr)] if idr else None
# max radius of any OD-G04 material between z -24.94 and -19.94 at 1 deg steps, several levels
worst = (0, None)
for z in (-20.0, -20.5, -21.0, -21.5, -22.0, -22.5, -22.9):
    for a in range(0, 360, 1):
        r = radial_extent(g04p, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, z, side="outer", r_min=0, r_max=40)
        if r.status == "MEASURED" and r.measured > worst[0]:
            worst = (r.measured, (a, z))
out["g04_max_r_below_floor_rays"] = [round(worst[0], 4), worst[1]]
print(json.dumps(out, indent=1))
(WS / "01_CAD/probe/probe_g04_hub_v01.json").write_text(json.dumps(out, indent=1))
