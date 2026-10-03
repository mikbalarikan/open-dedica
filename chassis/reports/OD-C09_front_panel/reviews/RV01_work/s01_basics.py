from common import *
from tools.core import validity
from tools.measure import envelope, feature_census, bore_census
import hashlib
out = {}
s, ss = part()
out["n_solids"] = len(ss)
out["labels"] = [getattr(s, "label", None)] + [getattr(c, "label", None) for c in getattr(s, "children", [])]
out["validity"] = {k: R(v) for k, v in validity(s).items()}
out["envelope"] = R(envelope(s))
out["volume"] = volume_mm3(s)
fc = feature_census(s)
out["feature_census"] = {k: v.measured for k, v in fc.items()}
bc = bore_census(s)
out["bores"] = bc.detail["bores"]
out["concave_arcs"] = bc.detail["concave_arcs"]
r = refs()
out["ident"] = r["_ident"]
for k in ("C01", "C10", "C05", "HOUS", "G04", "G10", "E02"):
    bb = r[k].bounding_box()
    out["bb_" + k] = [round(bb.min.X, 3), round(bb.min.Y, 3), round(bb.min.Z, 3), round(bb.max.X, 3), round(bb.max.Y, 3), round(bb.max.Z, 3)]
    out["valid_" + k] = {kk: vv.measured for kk, vv in validity(r[k]).items()}
dump("s01_basics.json", out)
print(json.dumps(out, indent=1, default=str))
