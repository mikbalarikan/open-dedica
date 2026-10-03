"""RV02 part checks on the delivered STEP (reviewer's own script)."""
import json, sys
from pathlib import Path
from tools.core import step as st
from tools.core.validity import validity
from tools.core.shapes import solids, faces
from tools.measure import (envelope, feature_census, bore_census, locate_bore, mass_properties)
W = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig")
OUT = W / "reviews/RV02_work"
P = W / "02_STEP_STL/od_t01_rig_C1_v02.step"
rig = st.read_step(P)
res = {}
res["schema"] = st.read_schema(P); res["unit"] = st.read_length_unit(P); res["labels"] = st.labels(rig)
res["validity"] = {k: v.to_dict() for k, v in validity(rig).items()}
res["envelope"] = {k: v.measured for k, v in envelope(rig).items()}
fc = feature_census(rig)
res["census"] = {k: v.measured for k, v in fc.items()}
bc = bore_census(rig)
res["bores"] = bc.detail["bores"]
loc = {}
for x in (-44, 44):
    for z in (-44, 44):
        loc[f"screw({x},{z})"] = {k: v.measured for k, v in locate_bore(bc, (x, 137.5, z), (0, 1, 0)).items()}
        loc[f"cbore({x},{z})"] = {k: v.measured for k, v in locate_bore(bc, (x, 150.0, z), (0, 1, 0)).items()}
for x in (-105, 105):
    for z in (-40, 40):
        loc[f"bench({x},{z})"] = {k: v.measured for k, v in locate_bore(bc, (x, 5.0, z), (0, 1, 0)).items()}
loc["window"] = {k: v.measured for k, v in locate_bore(bc, (0, 147.5, 0), (0, 1, 0)).items()}
res["locate"] = loc
res["mass"] = {k: v.measured for k, v in mass_properties(rig, 1240).items()}
# planar faces: list normal, plane point, bbox
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GeomAbs import GeomAbs_Plane
from OCP.BRepBndLib import BRepBndLib
from OCP.Bnd import Bnd_Box
from OCP.TopAbs import TopAbs_REVERSED
pl = []
for f in faces(rig):
    s = BRepAdaptor_Surface(f)
    if s.GetType() != GeomAbs_Plane:
        continue
    ax = s.Plane().Axis(); d = ax.Direction()
    n = [d.X(), d.Y(), d.Z()]
    if f.Orientation() == TopAbs_REVERSED:
        n = [-c for c in n]
    b = Bnd_Box(); BRepBndLib.Add_s(f, b); b.SetGap(0)
    pl.append({"n": [round(c, 5) for c in n], "bbox": [round(c, 4) for c in b.Get()]})
res["planes"] = pl
(OUT / "part_basic.json").write_text(json.dumps(res, indent=1, default=str))
print(json.dumps({k: res[k] for k in ("schema", "unit", "labels", "envelope", "census", "mass")}, indent=1, default=str))
print({k: (v["measured"], v["status"], v["reason"]) for k, v in res["validity"].items()})
for k, v in loc.items(): print(k, v)
for b in res["bores"]: print(round(b["diameter"],4), b["start"], b["end"], b["span_deg"], b.get("through"), b.get("open_ends"))
for p in pl: print(p)
