import json, sys, numpy as np, trimesh
RUN = sys.argv[1]
L = json.load(open(f"{RUN}/measure/figures/axis_stations.json"))["stem_group_line"]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); v = m.vertices
cx = L["x0"] + L["dxdz"] * v[:, 2]; cy = L["y0"] + L["dydz"] * v[:, 2]
x, y, z = v[:, 0] - cx, v[:, 1] - cy, v[:, 2]; r = np.hypot(x, y); th = np.degrees(np.arctan2(y, x))
for nom in [0, 90, 180, -90, 45]:
    d = ((th - nom + 180) % 360) - 180
    line = []
    for z0 in np.arange(15.5, 33.01, 0.25):
        s = (np.abs(z - z0) < 0.125) & (np.abs(d) < 2.5) & (r < 7.5) & (r > 3.5)
        line.append(f"{z0:.2f}:{r[s].max():.2f}" if s.sum() else f"{z0:.2f}:--")
    print(nom, ' '.join(line))
