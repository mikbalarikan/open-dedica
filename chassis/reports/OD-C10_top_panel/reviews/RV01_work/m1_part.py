import sys, time, json
sys.path.insert(0, "/root/oguz-jobs/20261001-od-c10-top-panel/reviews/RV01_work")
from common import *
from tools.core import validity
from tools.core.shapes import faces, volume_mm3
from tools.measure import envelope, feature_census, bore_census, locate_bore, mass_properties, radial_extent
from tools.measure.sampling import kind
from tools.core.step import read_schema, read_header, labels
out = {}
t = time.time()
L = lid()
raw = read_step(LID)
out["labels"] = labels(raw); out["schema"] = read_schema(LID)
v = validity(L); out["validity"] = {k: (r.measured, r.status, r.reason) for k, r in v.items()}
e = envelope(L); out["envelope"] = {k: r.measured for k, r in e.items()}
fc = feature_census(L); out["feature_census"] = {k: r.measured for k, r in fc.items()}
bc = bore_census(L); out["bores"] = bc.detail["bores"]
out["volume"] = volume_mm3(L)
# faces by kind and position
fl = []
from build123d import Face
for f0 in faces(L):
    f = Face(f0); bb = f.bounding_box()
    fl.append({"kind": kind(f0), "area": round(f.area, 3), "min": [round(c, 3) for c in bb.min.to_tuple()],
               "max": [round(c, 3) for c in bb.max.to_tuple()]})
out["faces"] = fl
loc = {}
for (x, z) in [(65, -60), (65, -210), (90, -293), (-90, -293)]:
    h = locate_bore(bc, (x, 216.5, z), (0, 1, 0)); c = locate_bore(bc, (x, 234.0, z), (0, 1, 0))
    loc[f"{x},{z}"] = {"hole": {k: (r.measured, r.at, r.detail.get("start"), r.detail.get("end")) for k, r in h.items()},
                       "cbore": {k: (r.measured, r.at, r.detail.get("start"), r.detail.get("end")) for k, r in c.items()}}
    # column outer diameter by rays at y 215.5 and 230, 4 angles
    rr = {}
    for yy in (215.5, 230.0):
        for a in (0, 90, 180, 270):
            try:
                r = radial_extent(L, (x, 0, z), (0, 1, 0), (1, 0, 0), a + 45, yy, side="outer", r_min=1.0, r_max=7.5)
                rr[f"y{yy}_a{a}"] = (r.measured, r.status, r.reason)
            except Exception as ex:
                rr[f"y{yy}_a{a}"] = ("ERR", str(ex))
    loc[f"{x},{z}"]["col_r"] = rr
out["columns"] = loc
pads = {}
for x in (48, -48):
    rr = {}
    for yy in (211.0, 230.0):
        for a in (0, 90, 180, 270):
            try:
                r = radial_extent(L, (x, 0, 30), (0, 1, 0), (1, 0, 0), a, yy, side="outer", r_min=0, r_max=7.0)
                rr[f"y{yy}_a{a}"] = (r.measured, r.at, r.status, r.reason)
            except Exception as ex:
                rr[f"y{yy}_a{a}"] = ("ERR", str(ex))
    pads[x] = rr
out["pads"] = pads
mp = mass_properties(L, 1270); out["mass"] = {k: r.measured for k, r in mp.items()}
out["t"] = time.time() - t
dump("m1_part.json", out)
print(json.dumps({k: out[k] for k in out if k not in ("faces",)}, default=str))
