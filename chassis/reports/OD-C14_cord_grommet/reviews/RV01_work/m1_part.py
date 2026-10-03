import json, sys, math
from pathlib import Path
from tools.core import read_step, validity, compare_step, mesh_sagitta, write_stl
from tools.core.step import labels, node_labels, read_schema, read_length_unit
from tools.core.shapes import solids, faces, volume_mm3
from tools.measure import (envelope, feature_census, bore_census, min_wall, min_wall_wide,
    overhang_census, flat_ceiling_spans, mesh_census, mesh_deviation, min_wall_mesh, mass_properties)
W = Path("/root/oguz-jobs/20261002-od-c14-cord-grommet")
step = W/"02_STEP_STL/od_c14_grommet_half_C1_v01.step"
stl = W/"02_STEP_STL/od_c14_grommet_half_C1_v01.stl"
out = {}
def r(k, x):
    out[k] = x.to_dict() if hasattr(x, "to_dict") else {kk: v.to_dict() for kk, v in x.items()} if isinstance(x, dict) else x
    print(k, json.dumps(out[k] if not isinstance(out[k], dict) or "measured" not in out[k] else {a: out[k][a] for a in ("measured","at","status","reason")}, default=str)[:600])
s = read_step(step)
r("schema", read_schema(step)); r("unit", read_length_unit(step))
r("labels", labels(s)); r("node_labels", node_labels(s))
r("validity", validity(s))
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL, TopAbs_SOLID, TopAbs_FACE
from tools.core.shapes import occ
def cnt(sh, kind, avoid=None):
    e = TopExp_Explorer(occ(sh), kind) if avoid is None else TopExp_Explorer(occ(sh), kind, avoid)
    n=0
    while e.More(): n+=1; e.Next()
    return n
r("shells_total", cnt(s, TopAbs_SHELL)); r("shells_free", cnt(s, TopAbs_SHELL, TopAbs_SOLID)); r("faces_free", cnt(s, TopAbs_FACE, TopAbs_SHELL))
r("volume", volume_mm3(s))
r("envelope", envelope(s))
r("feature_census", feature_census(s))
bc = bore_census(s); r("bore_census", bc)
# face list
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GeomAbs import GeomAbs_Plane, GeomAbs_Cylinder, GeomAbs_Cone
from OCP.BRepBndLib import BRepBndLib
from OCP.Bnd import Bnd_Box
fl=[]
for f in faces(s):
    a = BRepAdaptor_Surface(f); t=a.GetType(); b=Bnd_Box(); BRepBndLib.AddOptimal_s(f,b,False,False)
    bb=[round(v,4) for v in b.Get()]
    d={"bbox":bb}
    if t==GeomAbs_Plane:
        p=a.Plane(); n=p.Axis().Direction(); l=p.Location(); d.update(kind="plane", n=[round(n.X(),4),round(n.Y(),4),round(n.Z(),4)], loc=[round(l.X(),4),round(l.Y(),4),round(l.Z(),4)])
    elif t==GeomAbs_Cylinder:
        c=a.Cylinder(); l=c.Location(); dd=c.Axis().Direction(); d.update(kind="cyl", r=round(c.Radius(),5), loc=[round(l.X(),4),round(l.Y(),4)], dir=[round(dd.X(),5),round(dd.Y(),5),round(dd.Z(),5)])
    elif t==GeomAbs_Cone:
        c=a.Cone(); l=c.Location(); dd=c.Axis().Direction(); d.update(kind="cone", semi_deg=round(math.degrees(c.SemiAngle()),4), refr=round(c.RefRadius(),5), loc=[round(l.X(),4),round(l.Y(),4),round(l.Z(),4)], dir=[round(dd.X(),5),round(dd.Y(),5),round(dd.Z(),5)])
    else: d.update(kind=str(t))
    fl.append(d)
r("faces", fl)
for d in fl: print("  ", d)
mw = min_wall(s); r("min_wall", mw); print("  wide", mw.detail.get("wide"))
r("min_wall_wide", min_wall_wide(s))
r("overhang", overhang_census(s, (0,0,1))); print("  ", out["overhang"]["detail"])
r("flat_ceiling", flat_ceiling_spans(s, (0,0,1), max_span=5.0))
r("mass", mass_properties(s, 1240))
r("mesh_census", mesh_census(stl))
r("mesh_deviation", mesh_deviation(stl, s))
r("min_wall_mesh", min_wall_mesh(stl))
# U-04: re-export the re-read solid and compare
w = W/"reviews/RV01_work/roundtrip_half.step"
from tools.core.step import step_roundtrip
r("roundtrip", step_roundtrip(s, w, timestamp="2026-10-02T00:00:00"))
r("compare_delivered", compare_step(s, step))
json.dump(out, open(W/"reviews/RV01_work/m1_part.json","w"), indent=1, default=str)
