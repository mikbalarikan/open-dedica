"""QA-only: skirt and tab/lug residual breakdown (z bins, side vs end), signed (+ = scan outside CAD)."""
import sys, numpy as np, trimesh
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import load_mesh, select
z = np.load("qa/dev_arrays.npz"); P, d = z["s2c_pts"], z["s2c_d"]
cad = load_mesh("/tmp/claude-0/-home-user-agentic-STL-to-CAD/d8e5b691-152f-55fe-9a52-555e01807691/scratchpad/qa_cad.stl")
def signed(m):
    cp, dist, tri = trimesh.proximity.closest_point(cad, P[m]); return np.sign(((P[m]-cp)*cad.face_normals[tri]).sum(1))*dist
print("SKIRT (z<-0.3) by z-bin and part (side |x|<19.5 / end |x|>=19.5 & |x|<32 / tab |x|>=32):")
for lo, hi in [(-3.3,-2.5),(-2.5,-2.0),(-2.0,-1.5),(-1.5,-1.0),(-1.0,-0.3)]:
    for nm, pr in [("side", {"abs_x":[None,19.5]}), ("end", {"abs_x":[19.5,32]}), ("tab", {"abs_x":[32,None]})]:
        m = select({"z":[lo,hi], **pr}, P)
        if m.sum() < 30: continue
        s = signed(m)
        print(f"  z[{lo},{hi}) {nm:4s} n {m.sum():6d} p95|d| {np.percentile(d[m],95):.3f} frac>0.3 {np.mean(d[m]>0.3):.3f} signed med {np.median(s):+.3f} p5 {np.percentile(s,5):+.3f} p95 {np.percentile(s,95):+.3f}")
print("SIDE skirt y>0 vs y<0 (z -2.5..-0.3):")
for nm, pr in [("y>0", {"y":[0,None]}), ("y<0", {"y":[None,0]})]:
    m = select({"z":[-2.5,-0.3], "abs_x":[None,19.5], **pr}, P); s = signed(m)
    print(f"  {nm} n {m.sum()} signed med {np.median(s):+.3f} p5 {np.percentile(s,5):+.3f} p95 {np.percentile(s,95):+.3f} | y median {np.median(P[m,1]):+.3f}")
print("TABS/LUGS |x|>=32, z>0.3 by sub-part:")
for nm, pr in [("tab outer faces/sides z0.3-11", {"abs_x":[32,None], "z":[0.3,11]}), ("lug z11-15.5 x 32-35", {"abs_x":[32,35], "z":[11,15.5]}),
               ("lug z11-15.5 x 35-43", {"abs_x":[35,43], "z":[11,15.5]}), ("lug top z>=14.7", {"abs_x":[32,43], "z":[14.7,None]})]:
    for sx, px in [("+X", {"x":[0,None]}), ("-X", {"x":[None,0]})]:
        m = select({**pr, **px}, P)
        if m.sum() < 30: continue
        s = signed(m)
        print(f"  {nm:30s} {sx} n {m.sum():6d} p95|d| {np.percentile(d[m],95):.3f} max {d[m].max():.3f} frac>0.3 {np.mean(d[m]>0.3):.3f} signed med {np.median(s):+.3f} p5 {np.percentile(s,5):+.3f} p95 {np.percentile(s,95):+.3f}")
print("CUP WALLS by z-bin (|x| 7-32, |y|>=1.5), per cup:")
for lo, hi in [(0.3,3.6),(3.6,7),(7,9.5),(9.5,11.8)]:
    for sx, px in [("A -X", {"x":[None,0]}), ("B +X", {"x":[0,None]})]:
        m = select({"abs_x":[7,32], "abs_y":[1.5,None], "z":[lo,hi], **px}, P); s = signed(m)
        print(f"  z[{lo},{hi}) {sx} n {m.sum():6d} p95|d| {np.percentile(d[m],95):.3f} frac>0.3 {np.mean(d[m]>0.3):.3f} signed med {np.median(s):+.3f} p5 {np.percentile(s,5):+.3f} p95 {np.percentile(s,95):+.3f}")
