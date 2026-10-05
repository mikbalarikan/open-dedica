import sys
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels/reviews/RV01_work")
from common import *
import numpy as np, struct
from tools.core import volume_mm3
from tools.measure import envelope
def tris(p):
    b = Path(p).read_bytes(); n = struct.unpack("<I", b[80:84])[0]
    a = np.frombuffer(b[84:84 + 50 * n], dtype=np.dtype([("n", "<f4", 3), ("v", "<f4", (3, 3)), ("a", "<u2")]))
    return b[:80], a
res = {}
for stem in ("od_c13_right_C1_v01", "od_c12_left_C1_v01", "od_c16_bracket_C1_v01"):
    hd, d = tris(EXP / f"{stem}.stl"); hf, f = tris(WORK / f"fresh_{stem}.stl")
    dv = np.sort(d["v"].reshape(-1, 3).round(4), axis=0); fv = np.sort(f["v"].reshape(-1, 3).round(4), axis=0)
    shape = load(f"{stem}.step"); e = envelope(shape)
    allv = d["v"].reshape(-1, 3)
    box = (allv.min(0).tolist(), allv.max(0).tolist())
    brep = ([e["min_x"].measured, e["min_y"].measured, e["min_z"].measured], [e["max_x"].measured, e["max_y"].measured, e["max_z"].measured])
    dbox = float(np.max(np.abs(np.array(box) - np.array(brep))))
    res[stem] = {"header_delivered": hd.decode("latin1").strip("\x00 "), "header_fresh": hf.decode("latin1").strip("\x00 "),
                 "same_vertex_multiset": bool(dv.shape == fv.shape and np.allclose(dv, fv, atol=1e-4)),
                 "same_triangle_order": bool(np.array_equal(d["v"], f["v"])),
                 "normals_equal": bool(np.array_equal(d["n"], f["n"])),
                 "mesh_bbox": box, "brep_bbox": brep, "bbox_delta": dbox, "brep_volume": volume_mm3(shape)}
    print(stem, res[stem])
dump(res, "mesh_compare.json")
