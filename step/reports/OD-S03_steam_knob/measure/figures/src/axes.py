"""Per-feature axis positions in the frozen datum frame (axis kept parallel to datum Z).
Area-weighted face centres, outward-facing wall selection by n.r_hat sign, robust (soft_l1) fit.
Writes ../axes.json. Builder measurement script (stl-re-measure-intent step 4 companion)."""
import json, sys, numpy as np, trimesh
from scipy.optimize import least_squares
RUN = sys.argv[1]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl")
C, N, A = m.triangles_center, m.face_normals, m.area_faces
def sel(zlo, zhi, rlo, rhi, outer=True, th_ex=None, c0=(0, 0), perp=0.3):
    x, y = C[:, 0] - c0[0], C[:, 1] - c0[1]; r = np.hypot(x, y); th = np.degrees(np.arctan2(y, x))
    ndr = (N[:, 0] * x + N[:, 1] * y) / np.maximum(r, 1e-9)
    s = (C[:, 2] > zlo) & (C[:, 2] < zhi) & (r > rlo) & (r < rhi) & (np.abs(N[:, 2]) < perp)
    s &= (ndr > 0.5) if outer else (ndr < -0.5)
    if th_ex: s &= ~((th > th_ex[0]) & (th < th_ex[1]))
    return s
def fit(s, cone=False):
    P = C[s]; w = np.sqrt(A[s])
    def res(q):
        cx, cy, R = q[:3]; k = q[3] if cone else 0.0
        return (np.hypot(P[:, 0] - cx, P[:, 1] - cy) - (R + k * P[:, 2])) * w
    q0 = [0, 0, np.median(np.hypot(P[:, 0], P[:, 1]))] + ([0.0] if cone else [])
    sol = least_squares(res, q0, loss="soft_l1", f_scale=0.05)
    rr = sol.fun / w
    out = {"cx": sol.x[0], "cy": sol.x[1], "R_at_z0" if cone else "R": sol.x[2], "n_faces": int(s.sum()),
           "rms": float(np.sqrt(np.mean(rr ** 2))), "p95": float(np.percentile(np.abs(rr), 95))}
    if cone:
        out["k_dr_dz"] = sol.x[3]; out["draft_deg"] = float(np.degrees(np.arctan(sol.x[3])))
    return {k: (round(float(v), 4) if isinstance(v, (float, np.floating)) else v) for k, v in out.items()}
F = {
 "cap_wall_cone": (sel(2.8, 12.9, 12.3, 13.6, th_ex=(-50, 50)), True, "cap wall z 2.8-12.9, lever sector -50..50 deg excluded"),
 "mouth_ring": (sel(14.2, 14.45, 11.0, 11.5), False, "collar top (below ring face) z 14.2-14.45"),
 "collar": (sel(14.6, 15.9, 10.7, 11.5), False, "collar cylinder z 14.6-15.9"),
 "stem_core_45": (sel(19, 27.5, 4.8, 5.6, th_ex=None), False, "stem core z 19-27.5 (ribs excluded by r<5.6)"),
 "neck": (sel(30.0, 31.3, 4.4, 5.0), False, "neck z 30.0-31.3"),
 "sleeve_crest": (sel(33.4, 36.8, 5.6, 6.2), False, "sleeve ripple envelope z 33.4-36.8"),
 "bore": (sel(36.0, 37.0, 3.7, 4.4, outer=False), False, "sleeve bore z 36.0-37.0 (inward-facing)"),
}
out = {}
for k, (s, cone, desc) in F.items():
    out[k] = {"desc": desc, **fit(s, cone)}
    print(k, out[k])
json.dump(out, open(f"{RUN}/measure/figures/axes.json", "w"), indent=1)
