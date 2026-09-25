"""Rib cross-section: circle fit to the rib tip (points within 0.45 mm of the tip radius) in the
(tangential, radial) plane per rib per z station; stem frame. Writes ../rib_tip.json"""
import json, sys, numpy as np, trimesh
from scipy.optimize import least_squares
RUN = sys.argv[1]
L = json.load(open(f"{RUN}/measure/figures/axis_stations.json"))["stem_group_line"]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); C = m.triangles_center; A = m.area_faces
x = C[:, 0] - (L["x0"] + L["dxdz"] * C[:, 2]); y = C[:, 1] - (L["y0"] + L["dydz"] * C[:, 2]); r = np.hypot(x, y); th = np.degrees(np.arctan2(y, x))
res = {}
for nom in (0, 90, 180, -90):
    d = ((th - nom + 180) % 360) - 180; Rs = []
    for z0 in np.arange(19.0, 27.1, 1.0):
        s = (np.abs(C[:, 2] - z0) < 0.35) & (np.abs(d) < 10) & (r > 5.5) & (r < 7)
        if s.sum() < 30: continue
        tip = np.percentile(r[s], 98); ss = s & (r > tip - 0.45)
        t = r[ss] * np.radians(d[ss]); u = r[ss]; w = np.sqrt(A[ss])
        so = least_squares(lambda q: (np.hypot(t - q[0], u - q[1]) - q[2]) * w, [0, tip - 0.4, 0.45], loss="soft_l1", f_scale=0.03)
        rr = so.fun / w
        if 0.1 < so.x[2] < 1.5: Rs.append([float(z0), float(so.x[2]), float(np.sqrt(np.mean(rr**2))), int(ss.sum())])
    res[str(nom)] = Rs
    print(nom, [(a, round(b, 3), round(c, 3)) for a, b, c, _ in Rs], 'median', round(float(np.median([v[1] for v in Rs])), 3))
allR = [v[1] for vv in res.values() for v in vv]
res["median_all"] = float(np.median(allR)); print("median all", res["median_all"])
json.dump(res, open(f"{RUN}/measure/figures/rib_tip.json", "w"), indent=1)
