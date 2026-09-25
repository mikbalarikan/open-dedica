"""Lever plan geometry per z: flank lines (y = a + b x), tip circle, pocket walls. Datum frame.
Writes ../lever.json"""
import json, sys, numpy as np, trimesh
from scipy.optimize import least_squares
RUN = sys.argv[1]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); C, N, A = m.triangles_center, m.face_normals, m.area_faces
out = {"per_z": []}
def circfit(P, w):
    f = lambda q: (np.hypot(P[:, 0]-q[0], P[:, 1]-q[1]) - q[2]) * w
    s = least_squares(f, [P[:, 0].mean() - 3, P[:, 1].mean(), 4.8], loss="soft_l1", f_scale=0.05); rr = s.fun / w
    return s.x, float(np.sqrt(np.mean(rr**2)))
for z0 in [2.5, 4.0, 5.5, 7.0, 8.5, 10.0, 11.5, 12.8]:
    sz = np.abs(C[:, 2] - z0) < 0.4
    row = {"z": z0}
    for side, sg in (("+Y", 1), ("-Y", -1)):
        s = sz & (N[:, 1] * sg > 0.97) & (C[:, 1] * sg > 3.0) & (C[:, 0] > 14) & (C[:, 0] < 23)
        if s.sum() > 20:
            X = np.c_[np.ones(s.sum()), C[s, 0]]; a, b = np.linalg.lstsq(X, C[s, 1], rcond=None)[0]
            res = C[s, 1] - X @ [a, b]; row[f"flank{side}"] = {"a": a, "b": b, "ang_deg": float(np.degrees(np.arctan(b))), "rms": float(res.std()), "n": int(s.sum()), "y_at_x18": a + 18 * b}
    s = sz & (C[:, 0] > 23.5) & (N[:, 0] > 0.3) & (np.abs(N[:, 2]) < 0.3)
    if s.sum() > 20:
        (cx, cy, R), rms = circfit(C[s, :2], np.sqrt(A[s])); row["tip"] = {"cx": cx, "cy": cy, "R": R, "rms": rms, "n": int(s.sum()), "xmax": float(cx + R)}
    out["per_z"].append(row)
    print(z0, {k: ({kk: round(float(vv), 3) for kk, vv in v.items()} if isinstance(v, dict) else v) for k, v in row.items()})
json.dump(out, open(f"{RUN}/measure/figures/lever.json", "w"), indent=1, default=float)
