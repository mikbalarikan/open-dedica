import json, struct
from pathlib import Path
import numpy as np
from tools.core import read_step
from tools.measure import radial_extent
J = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); W = J / "reviews/RV01_work"
def tris(p):
    raw = Path(p).read_bytes(); n = struct.unpack("<I", raw[80:84])[0]
    t = np.frombuffer(raw[84:84 + 50 * n], dtype=np.dtype([("n", "<f4", 3), ("v", "<f4", (3, 3)), ("a", "<u2")]))
    return {tuple(sorted(tuple(q) for q in T.tolist())) for T in t["v"]}, raw[:80]
a, ha = tris(J / "02_STEP_STL/od_c01_frame_C1_v02.stl"); b, hb = tris(W / "reexport.stl")
out = {"delivered": len(a), "reexport": len(b), "common_exact": len(a & b), "headers_equal": ha == hb}
p = read_step(J / "02_STEP_STL/od_c01_frame_C1_v02.step")
corners = {}
for (x, z, ang) in [(110, 90, 45), (-110, 90, 135), (110, -295, 315), (-110, -295, 225)]:
    # axis along -Y; ref +X; angle measured right-hand about -Y from +X
    r = radial_extent(p, (x, 0, z), (0, -1, 0), (1, 0, 0), ang, 3.0, side="outer")
    corners[f"{x},{z}@{ang}"] = r.detail["material"]
out["corner_rays"] = corners
(W / "rv_g.json").write_text(json.dumps(out, indent=1, default=str)); print(json.dumps(out, default=str))
