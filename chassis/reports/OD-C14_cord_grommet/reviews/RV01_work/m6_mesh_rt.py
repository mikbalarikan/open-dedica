import sys, hashlib
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c14-cord-grommet/reviews/RV01_work")
from common import *
from tools.core import write_stl, step_roundtrip
from tools.measure import mesh_census, min_wall_mesh, envelope
import math
A = half(); A.label = "od_c14_grommet_half"
p = W/"reviews/RV01_work/regen_0.01_0.10.stl"
w = write_stl(A, p, tolerance=0.01, angular_tolerance=0.10)
print("regen triangles", w.detail.get("triangles"), "sagitta", w.checks["max_sagitta"].measured, "limit ang", 4*math.acos(1-0.01/10.0))
print("regen sha", hashlib.sha256(p.read_bytes()).hexdigest()[:16], "delivered sha", hashlib.sha256((W/"02_STEP_STL/od_c14_grommet_half_C1_v01.stl").read_bytes()).hexdigest()[:16])
d = W/"02_STEP_STL/od_c14_grommet_half_C1_v01.stl"
import numpy as np, struct
def tris(path):
    b = path.read_bytes(); n = struct.unpack("<I", b[80:84])[0]
    a = np.frombuffer(b[84:84+50*n], dtype=np.dtype([("n","<f4",3),("v","<f4",(3,3)),("x","<u2")]))
    return a["v"]
t1, t2 = tris(d), tris(p)
print("delivered tris", len(t1), "regen", len(t2), "same vertices", len(t1)==len(t2) and np.allclose(np.sort(t1.reshape(-1,9),axis=0), np.sort(t2.reshape(-1,9),axis=0)))
print("mesh bbox", t1.reshape(-1,3).min(0), t1.reshape(-1,3).max(0))
rt = step_roundtrip(A, W/"reviews/RV01_work/roundtrip_half.step", timestamp="2026-10-02T00:00:00")
for k, v in rt.items(): print("rt", k, v.measured, v.status, v.reason[:100])
