import json, math
from pathlib import Path
import numpy as np
from build123d import Face, Plane, Vector, Box, Location, Rectangle
from tools.core import read_step
from tools.core.shapes import faces, volume_mm3
from tools.measure import envelope, radial_extent, radial_profile
from tools.measure.features import kind
from OCP.BRepGProp import BRepGProp
from OCP.GProp import GProp_GProps
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GeomAbs import GeomAbs_Plane
from OCP.BRepLProp import BRepLProp_SLProps
from OCP.BRepTools import BRepTools
from OCP.TopAbs import TopAbs_REVERSED
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
p = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v01.step")
O, A, R = (0,0,0), (0,0,1), (1,0,0)
out = {}
def rd(r): return r.to_dict()
# REQ-01
angs = list(range(50,131,5))
for band in ((15.5,20.5),(25.5,30.5)):
    rp = radial_profile(p, O, A, R, angs, band, margin=0, z_step=0.1, side="inner", r_max=32.0)
    out[f"REQ01_{band}"] = {k: {"m": v.measured, "st": v.status, "at": v.at, "reason": v.reason, "unread": v.detail.get("unread"), "on_face": v.detail.get("on_face")} for k,v in rp.items()}
# REQ-02
for z in (18.0, 28.0):
    for a in (50.0, 130.0):
        r = radial_extent(p, O, A, R, a, z, side="inner", r_max=32.0); out[f"REQ02_in_{a}_{z}"] = (r.measured, r.status, r.at, r.reason)
    for a in (40.0, 140.0):
        r = radial_extent(p, O, A, R, a, z, side="inner", r_max=32.0); out[f"REQ02_nomat_{a}_{z}"] = (r.measured, r.status, r.reason)
        r2 = radial_extent(p, O, A, R, a, z, side="inner"); out[f"REQ02_ray_{a}_{z}"] = (r2.measured, r2.status, r2.reason, r2.detail.get("material"))
    # sector edge scan: first material along ray from 40 to 50 deg in 0.5 steps within r<=32
    edge = []
    for a in np.arange(40.0, 50.01, 0.5):
        for aa in (a, 180-a):
            r = radial_extent(p, O, A, R, float(aa), z, side="inner", r_max=32.0)
            edge.append((float(aa), r.measured, r.status))
    out[f"REQ02_edge_{z}"] = edge
# faces census by normal & position
rows = []
for f in faces(p):
    ad = BRepAdaptor_Surface(f)
    u = (ad.FirstUParameter()+ad.LastUParameter())/2; v=(ad.FirstVParameter()+ad.LastVParameter())/2
    pr = BRepLProp_SLProps(ad, u, v, 1, 1e-7)
    n = pr.Normal(); n = np.array([n.X(),n.Y(),n.Z()])
    if f.Orientation()==TopAbs_REVERSED: n=-n
    e = {k: round(x.measured,4) for k,x in envelope(f).items()}
    g=GProp_GProps(); BRepGProp.SurfaceProperties_s(f,g)
    rows.append({"kind": kind(f), "n": [round(float(x),4) for x in n], "env": e, "area": round(g.Mass(),3)})
out["faces"] = rows
# sections: intersect with big planar faces
def section(plane, size=200):
    f = plane * Rectangle(size, size)
    sec = p.intersect(f.faces()[0])
    res=[]
    for ff in (sec.faces() if sec is not None else []):
        e = ff.bounding_box()
        verts = sorted({(round(v.X,3),round(v.Y,3),round(v.Z,3)) for v in ff.vertices()})
        res.append({"area": round(ff.area,3), "bbox":[round(e.min.X,3),round(e.min.Y,3),round(e.min.Z,3),round(e.max.X,3),round(e.max.Y,3),round(e.max.Z,3)], "verts": verts})
    return res
sections = {}
sections["xy_z18"] = section(Plane.XY.offset(18.0))
sections["xy_z28"] = section(Plane.XY.offset(28.0))
sections["xy_z23"] = section(Plane.XY.offset(23.0))
sections["yz_x0"] = section(Plane.YZ.offset(0.0))
sections["yz_x31.5"] = section(Plane.YZ.offset(31.5))
sections["yz_x-31.5"] = section(Plane.YZ.offset(-31.5))
sections["yz_x34"] = section(Plane.YZ.offset(34.0))
sections["xz_y7"] = section(Plane.XZ.offset(-7.0))
sections["xz_y38.5"] = section(Plane.XZ.offset(-38.5))
out["sections"] = sections
json.dump(out, open(W/"reviews/RV01_work/m3_rows.json","w"), indent=1, default=str)
for k,v in out.items():
    if k in ("faces","sections"): continue
    print(k, json.dumps(v, default=str)[:600])
for r in rows: print(r)
for k,v in sections.items():
    print("==",k)
    for s in v: print("  ", s["area"], s["bbox"], s["verts"] if len(s["verts"])<40 else len(s["verts"]))
