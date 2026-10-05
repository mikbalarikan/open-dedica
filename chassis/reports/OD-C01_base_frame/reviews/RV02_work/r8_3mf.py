import struct, zipfile, re, json
from pathlib import Path
import numpy as np
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
raw = (W/"02_STEP_STL/od_c01_frame_C1_v03.stl").read_bytes()
n = struct.unpack("<I", raw[80:84])[0]
t = np.frombuffer(raw[84:], dtype=np.dtype([("n","<3f4"),("v","<3,3f4"),("a","<u2")]), count=n)
S = t["v"].astype(np.float64)                      # n,3,3
with zipfile.ZipFile(W/"02_STEP_STL/od_c01_frame_C1_v03.3mf") as z:
    xml = z.read([x for x in z.namelist() if x.endswith(".model")][0]).decode()
P = np.array(re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', xml), float)
T = np.array(re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', xml), int)
M = P[T]                                           # m,3,3
def key(A):
    # canonical per-triangle: rotate so smallest vertex first (keeps winding), then lexsort rows
    A = np.round(A, 5)
    out=[]
    for tri in A:
        i = int(np.lexsort((tri[:,2],tri[:,1],tri[:,0]))[0])
        out.append(np.roll(tri, -i, axis=0).ravel())
    K = np.array(out)
    return K[np.lexsort(tuple(K[:,i] for i in range(8,-1,-1)))]
KS, KM = key(S), key(M)
same = KS.shape==KM.shape and bool(np.allclose(KS,KM,atol=1e-4,rtol=0))
res = dict(stl_tri=int(n), mf_tri=int(len(T)), identical_triangle_set=same,
           max_abs_diff=float(np.abs(KS-KM).max()) if KS.shape==KM.shape else None,
           stl_bbox=[S.reshape(-1,3).min(0).tolist(), S.reshape(-1,3).max(0).tolist()],
           mf_bbox=[P.min(0).tolist(), P.max(0).tolist()])
print(json.dumps(res, indent=1))
json.dump(res, open(W/"reviews/RV02_work/r8_3mf.json","w"), indent=1)
