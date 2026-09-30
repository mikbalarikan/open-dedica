import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from tools.core import write_stl, mesh_sagitta
from tools.core.step import file_sha256
from tools.measure import mesh_census, mesh_deviation, min_wall_mesh
import time, math
R = {}
def p(k, v): R[k] = v; print(k, str(v)[:900])
m = load_mount()
# R_max: the largest distance from its own axis over every curved face (cylinder r, cone rim, torus R+r)
rmax = 0; which = None
for f in m.faces():
    g = f.geom_type.name; a = f.geom_adaptor()
    if g == "CYLINDER": r = a.Cylinder().Radius()
    elif g == "TORUS": t = a.Torus(); r = t.MajorRadius() + t.MinorRadius()
    elif g == "CONE":
        c = a.Cone(); ax = c.Axis(); o = ax.Location(); d = ax.Direction(); r = 0
        for v in f.vertices():
            vx, vy, vz = v.X - o.X(), v.Y - o.Y(), v.Z - o.Z(); t_ = vx*d.X()+vy*d.Y()+vz*d.Z()
            r = max(r, math.sqrt(max(vx*vx+vy*vy+vz*vz - t_*t_, 0)))
        bb = f.bounding_box(); r = max(r, (bb.max.X - bb.min.X) / 2)
    else: continue
    if r > rmax: rmax, which = r, (g, round(f.area, 3))
lim = 4 * math.acos(1 - 0.01 / rmax)
p("R_max / face / angular limit rad", (rmax, which, lim))
mc = mesh_census(STL); p("delivered census", {k: (r.measured if hasattr(r, 'measured') else r) for k, r in (mc.items() if isinstance(mc, dict) else [("r", mc)])})
wr = write_stl(m, W / "remesh_0.01_0.05.stl", tolerance=0.01, angular_tolerance=0.05)
p("re-mesh 0.01/0.05", {"sha": file_sha256(W / "remesh_0.01_0.05.stl"), "delivered_sha": file_sha256(STL), "same_bytes": (W / "remesh_0.01_0.05.stl").read_bytes() == STL.read_bytes(), "checks": {k: (v.measured, v.status) for k, v in wr.checks.items()}, "detail": str(wr.detail)[:300]})
sg = mesh_sagitta(m); p("mesh_sagitta of that triangulation", (sg.measured, sg.status, sg.at))
t = time.time(); md = mesh_deviation(STL, m); p("mesh_deviation delivered STL vs STEP", (md.measured, md.status, md.at, md.reason[:100], round(time.time() - t)))
mw = min_wall_mesh(STL); p("min_wall_mesh", (mw.measured, mw.status, mw.reason[:120], mw.detail.get("vertex_precision_mm")))
dump("s09.json", R)
