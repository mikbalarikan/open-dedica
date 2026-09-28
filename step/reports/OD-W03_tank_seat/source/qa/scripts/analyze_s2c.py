"""QA-only analysis of scan->CAD residuals from qa/dev_arrays.npz (gate frame): where do the
points over the p95 band (0.30) sit, and which side of the CAD are they (signed: + = scan outside CAD)."""
import sys, numpy as np, trimesh
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import step_to_mesh, select
z = np.load("qa/dev_arrays.npz"); P, d = z["s2c_pts"], z["s2c_d"]
cad = step_to_mesh("build/OD-W03_datum.step", "/tmp/claude-0/-home-user-agentic-STL-to-CAD/d8e5b691-152f-55fe-9a52-555e01807691/scratchpad/qa_cad.stl")
rng = np.random.default_rng(0); idx = rng.choice(len(P), 60000, replace=False)
cp, dist, tri = trimesh.proximity.closest_point(cad, P[idx])
sgn = np.sign(((P[idx] - cp) * cad.face_normals[tri]).sum(1))
sd = sgn * dist
regions = {
 "flange top (z±0.3, up)": {"z": [-0.3, 0.3]},
 "skirt outer z<-0.3": {"z": [None, -0.3]},
 "cup walls |x|7-32 z0.3-11.8": {"abs_x": [7, 32], "abs_y": [1.5, None], "z": [0.3, 11.8]},
 "cup tops+shoulders z11.8-16, |x|7-32": {"abs_x": [7, 32], "z": [11.8, 16]},
 "barbs z>=16": {"z": [16, None], "abs_x": [15, 24]},
 "boss |x|<7 z>0.3": {"abs_x": [None, 7], "z": [0.3, None], "abs_y": [1.2, None]},
 "webs |y|<1.2 z>0.3": {"abs_y": [None, 1.2], "z": [0.3, None], "not": {"abs_x": [15, 24], "z": [12, None]}},
 "tabs+lugs |x|>=32": {"abs_x": [32, None], "z": [0.3, None]},
}
N = len(P)
print(f"all: n {N} frac>0.30 {np.mean(d>0.3):.4f} frac>0.8 {np.mean(d>0.8):.5f}")
for k, pr in regions.items():
    m = select(pr, P)
    ms = select(pr, P[idx])
    print(f"{k:38s} n {m.sum():7d} share {m.mean():.3f} p95 {np.percentile(d[m],95):.3f} max {d[m].max():.3f} "
          f"frac>0.3 {np.mean(d[m]>0.3):.3f} share_of_all_over {np.sum(d[m]>0.3)/np.sum(d>0.3):.3f} "
          f"| signed median {np.median(sd[ms]):+.3f} p5 {np.percentile(sd[ms],5):+.3f} p95 {np.percentile(sd[ms],95):+.3f}")
