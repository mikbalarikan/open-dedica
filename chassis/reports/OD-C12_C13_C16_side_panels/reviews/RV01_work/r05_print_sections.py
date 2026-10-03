"""RV01: panels' D-03a / D-03b / walls at 0.6 mm spacing (the toolkit's named fit);
bracket D-03a outside the named exception; J-05, D-05a; numeric sections for REQ-01,
REQ-02 (lip wedge at z -100 and z +60), REQ-04, E-06; section pictures."""
import sys, math
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels/reviews/RV01_work")
from common import *
import numpy as np
from tools.core import common_volume
from tools.core.shapes import faces as tfaces
from tools.measure import (overhang_census, flat_ceiling_spans, min_wall, radial_profile, envelope)
from tools.drawing import write_sections
from build123d import Box, Cylinder, Pos, Rot, Face, Solid, Align
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_VERTEX, TopAbs_EDGE
from OCP.BRep import BRep_Tool
from OCP.TopoDS import TopoDS
from build123d import Edge

R = one(load("od_c13_right_C1_v01.step")); L = one(load("od_c12_left_C1_v01.step"))
BR = one(load("od_c16_bracket_C1_v01.step"))
out = {}

def sec(shape, origin, normal):
    s = BRepAlgoAPI_Section(shape.wrapped, gp_Pln(gp_Pnt(*origin), gp_Dir(*normal)))
    s.Build()
    res = s.Shape()
    vs, es = set(), []
    ex = TopExp_Explorer(res, TopAbs_EDGE)
    while ex.More():
        e = Edge(TopoDS.Edge_s(ex.Current()))
        a, b = e.position_at(0), e.position_at(1)
        es.append(((round(a.X, 4), round(a.Y, 4), round(a.Z, 4)), (round(b.X, 4), round(b.Y, 4), round(b.Z, 4)),
                   e.geom_type.name, round(e.length, 4)))
        vs.add((round(a.X, 4), round(a.Y, 4), round(a.Z, 4))); vs.add((round(b.X, 4), round(b.Y, 4), round(b.Z, 4)))
        ex.Next()
    return sorted(vs), es

# ---- panel print checks
for key, s, bdir in (("c13", R, (-1, 0, 0)), ("c12", L, (1, 0, 0))):
    out[f"{key}_overhang"] = overhang_census(s, build_dir=bdir, spacing=0.6)
    out[f"{key}_ceiling"] = flat_ceiling_spans(s, build_dir=bdir, max_span=5.0, spacing=0.6)
    out[f"{key}_min_wall"] = min_wall(s, spacing=0.6)
    for k in ("overhang", "ceiling", "min_wall"):
        r = out[f"{key}_{k}"]
        print(key, k, r.measured, r.status, r.at, r.reason[:120], {x: r.detail.get(x) for x in ("per_kind_least_deg", "sampling_bound_deg", "below_min_deg", "wide", "largest_step_mm")})

# ---- bracket D-03a outside the named exception: the insert bore filled back in
plug = Pos(-3.0, 10.0, 0.0) * Rot(0, 90, 0) * Cylinder(2.0, 6.0)
filled = BR.fuse(plug).clean()
out["c16_overhang_all"] = overhang_census(BR, build_dir=(0, 1, 0), spacing=0.5)
out["c16_overhang_outside_exception"] = overhang_census(filled, build_dir=(0, 1, 0), spacing=0.5)
for k in ("c16_overhang_all", "c16_overhang_outside_exception"):
    r = out[k]; print(k, r.measured, r.status, r.at, r.detail.get("per_kind_least_deg"), r.detail.get("sampling_bound_deg"))

# ---- J-05: exact distance from the insert bore's faces to every face not adjacent to it
fl = tfaces(BR)
bore_faces = [f for f in fl if (Face(f).geom_type.name == "CYLINDER" and abs(Face(f).radius - 2.0) < 1e-6)
              or (Face(f).geom_type.name == "PLANE" and abs(Face(f).center().X + 6.0) < 1e-6)]
from OCP.TopTools import TopTools_IndexedMapOfShape
rows = []
for f in fl:
    if any(f.IsSame(b) for b in bore_faces):
        continue
    best = None
    for b in bore_faces:
        d = BRepExtrema_DistShapeShape(b, f); d.Perform()
        v = d.Value()
        p1, p2 = d.PointOnShape1(1), d.PointOnShape2(1)
        if best is None or v < best[0]:
            best = (v, (p1.X(), p1.Y(), p1.Z()), (p2.X(), p2.Y(), p2.Z()))
    F = Face(f)
    rows.append((round(best[0], 6), F.geom_type.name, tuple(round(c, 3) for c in F.center()), best[1], best[2]))
rows.sort()
out["j05_face_distances"] = rows
print("J-05 face distances", [(r[0], r[1], r[2]) for r in rows])

# ---- D-05a: radial_profile about the insert bore axis
rp = radial_profile(BR, (0, 10, 0), (-1, 0, 0), (0, 1, 0), list(range(0, 360, 15)), (0.0, 6.0), margin=(0.0, 0.0),
                    z_step=0.25, side="outer", r_min=2.0)
out["d05a_radial_profile"] = rp
print("D-05a", {k: (v.measured, v.status, v.at, v.reason[:80]) for k, v in rp.items()})

# ---- numeric sections
secs = {}
for name, s, o, n in (
        ("c13_z-100", R, (0, 0, -100), (0, 0, 1)), ("c13_z+60", R, (0, 0, 60), (0, 0, 1)),
        ("c12_z-100", L, (0, 0, -100), (0, 0, 1)), ("c12_z+60", L, (0, 0, 60), (0, 0, 1)),
        ("c13_y50", R, (0, 50, 0), (0, 1, 0)), ("c13_y200", R, (0, 200, 0), (0, 1, 0)),
        ("c12_y50", L, (0, 50, 0), (0, 1, 0)), ("c12_y200", L, (0, 200, 0), (0, 1, 0)),
        ("c12_y30", L, (0, 30, 0), (0, 1, 0)),
        ("c16_z0", BR, (0, 0, 0), (0, 0, 1)), ("c16_x-3", BR, (-3, 0, 0), (1, 0, 0)),
        ("c16_y10", BR, (0, 10, 0), (0, 1, 0))):
    vs, es = sec(s, o, n)
    secs[name] = {"vertices": vs, "edges": es}
    print(name, "vertices", vs if len(vs) < 40 else len(vs))
out["sections"] = secs

def wedge(name, side):
    es = secs[name]["edges"]
    sl = [e for e in es if abs(e[0][0] - e[1][0]) > 1e-3 and abs(e[0][1] - e[1][1]) > 1e-3]
    (a, b) = sl[0][0], sl[0][1]
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
    ang_from_panel_plane = math.degrees(math.atan2(dx, dy))
    apex = max((a, b), key=lambda p: p[1]); toe = min((a, b), key=lambda p: p[1])
    return {"slope_edges": sl, "slope_deg_from_panel_plane": ang_from_panel_plane, "apex": apex, "toe": toe,
            "apex_included_deg": 90 - math.degrees(math.atan2(dy, dx)) if False else math.degrees(math.atan2(dx, dy)),
            "thickness_1mm_below_apex": (1.0) * math.tan(math.radians(math.degrees(math.atan2(dx, dy))))}
for nm in ("c13_z-100", "c13_z+60", "c12_z-100", "c12_z+60"):
    w = wedge(nm, 1)
    out[f"wedge_{nm}"] = w
    print("wedge", nm, w["slope_deg_from_panel_plane"], w["apex"], w["toe"], w["slope_edges"])

# ---- REQ-01 footprint over plate material
c01 = one(read_step(INP / "OD-C01_base_frame.step"))
for key, s in (("c13", R), ("c12", L)):
    under = [f for f in tfaces(s) if Face(f).geom_type.name == "PLANE" and abs(Face(f).center().Y) < 1e-9
             and Face(f).normal_at(Face(f).center()).Y < -0.99]
    F = Face(under[0])
    prism = Solid.extrude(F, (0, -6.0, 0))
    cvr = common_volume(prism, c01)
    out[f"{key}_footprint"] = {"area": F.area, "prism_volume": prism.volume, "common": cvr, "n_under_faces": len(under)}
    print(key, "footprint", len(under), F.area, prism.volume, cvr.measured, cvr.status)

# ---- REQ-04 relief: floor face and its envelope
rel = [f for f in tfaces(L) if Face(f).geom_type.name == "PLANE" and abs(Face(f).center().X + 117.9) < 0.2]
out["c12_relief_floor"] = [(Face(f).center().to_tuple(), envelope(Face(f))) for f in rel]
for c, e in out["c12_relief_floor"]:
    print("relief floor", c, {k: round(v.measured, 4) for k, v in e.items()})

# ---- section pictures (evidence; renders never)
pics = {}
pdir = WORK / "sections"
for part, s, thr, views in (("rv01_c13", R, (115, 100, -100), ("top",)), ("rv01_c13_z60", R, (115, 100, 60), ("top",)),
                            ("rv01_c12", L, (-115, 100, -100), ("top",)), ("rv01_c12_z60", L, (-115, 100, 60), ("top",)),
                            ("rv01_c13_y50", R, (118, 50, -100), ("front",)), ("rv01_c13_y200", R, (118, 200, -100), ("front",)),
                            ("rv01_c12_y30", L, (-118, 30, -100), ("front",)), ("rv01_c12_y200", L, (-118, 200, -100), ("front",)),
                            ("rv01_c16", BR, (-9.5, 8, 0), ("top", "front")), ("rv01_c16_x-3", BR, (-3, 8, 0), ("left",))):
    try:
        ws = write_sections(s, pdir, part=part, version=1, views=views, through=thr)
        pics[part] = [(str(w.path.name), w.sha256, w.checks["nothing_clipped"].measured, w.detail) for w in ws]
    except Exception as exc:
        pics[part] = f"{type(exc).__name__}: {exc}"
    print("pic", part, pics[part] if isinstance(pics[part], str) else [(p[0], p[2]) for p in pics[part]])
out["pictures"] = pics
dump(out, "print_sections.json")
