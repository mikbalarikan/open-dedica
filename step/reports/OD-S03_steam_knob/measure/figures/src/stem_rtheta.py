"""Stem core R(theta) and rib geometry in the stem-group local frame (tilted line from axis_stations.json).
Writes ../stem_rtheta.json."""
import json, sys, numpy as np, trimesh
RUN = sys.argv[1]
L = json.load(open(f"{RUN}/measure/figures/axis_stations.json"))["stem_group_line"]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); v = m.vertices
cx = L["x0"] + L["dxdz"] * v[:, 2]; cy = L["y0"] + L["dydz"] * v[:, 2]
x, y, z = v[:, 0] - cx, v[:, 1] - cy, v[:, 2]; r = np.hypot(x, y); th = np.degrees(np.arctan2(y, x))
out = {}
for z0 in [18.0, 20.0, 22.0, 24.0, 26.0, 27.5]:
    s = (np.abs(z - z0) < 0.25) & (r > 4.5) & (r < 7)
    bins = np.arange(-180, 181, 2.0); prof = []
    for a, b in zip(bins[:-1], bins[1:]):
        ss = s & (th >= a) & (th < b)
        prof.append(float(np.max(r[ss])) if ss.sum() else None)
    out[f"z{z0}"] = prof
    # print compact: every 10 deg
    print(z0, ' '.join(f"{int(a)}:{p:.2f}" if p else f"{int(a)}:--" for a, p in list(zip(bins[:-1], prof))[::5]))
json.dump({"theta_bins_deg": list(np.arange(-180, 180, 2.0)), "rmax_per_bin": out}, open(f"{RUN}/measure/figures/stem_rtheta.json", "w"))
