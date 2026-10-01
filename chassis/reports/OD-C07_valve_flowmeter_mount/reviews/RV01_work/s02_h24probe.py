import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from tools.measure import radial_extent
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GeomAbs import GeomAbs_Plane
h22, h24, h22p, h24p = load_oem()
H = comp(h24)
print("H24 solids", len(h24))
# planar faces facing -Z low in H24
from build123d import Face
for f in H.faces():
    if f.geom_type.name == "PLANE":
        n = f.normal_at(f.center()); c = f.center()
        if n.Z < -0.99 and c.Z < 1.0:
            bb = f.bounding_box()
            print(" -Z plane z=%.4f area=%.3f bb x %.3f..%.3f y %.3f..%.3f" % (c.Z, f.area, bb.min.X, bb.max.X, bb.min.Y, bb.max.Y))
# inner/outer radii profile along several angles at low z
for ang in (0, 45, 90, 135, 180, 200, 270, 300):
    row = []
    for z in (0.02, 0.05, 0.08, 0.12, 0.2, 0.3, 0.5, 1.0):
        r = radial_extent(H, (0,0,0), (0,0,1), (1,0,0), ang, z, side="inner", r_min=12.0, r_max=17.0)
        ro = radial_extent(H, (0,0,0), (0,0,1), (1,0,0), ang, z, side="outer", r_min=12.0, r_max=17.0)
        row.append((z, None if r.measured is None else round(r.measured, 4), None if ro.measured is None else round(ro.measured,4), r.detail.get("material")))
    print(ang, row)
