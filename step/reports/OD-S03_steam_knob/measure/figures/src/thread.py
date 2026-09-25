"""Sleeve thread/ripple: per-azimuth r(z) profile in the stem-group frame; valley/crest z per azimuth
-> helix pitch + handedness; end-edge heights per azimuth. Writes ../thread.json"""
import json, sys, numpy as np, trimesh
RUN = sys.argv[1]
L = json.load(open(f"{RUN}/measure/figures/axis_stations.json"))["stem_group_line"]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); v = m.vertices
cx = L["x0"] + L["dxdz"] * v[:, 2]; cy = L["y0"] + L["dydz"] * v[:, 2]
x, y, z = v[:, 0] - cx, v[:, 1] - cy, v[:, 2]; r = np.hypot(x, y); th = np.degrees(np.arctan2(y, x))
dz = 0.05; zg = np.arange(31.5, 38.3, dz)
res = {"theta": [], "valleys": [], "crests": [], "bot_edge": [], "top_edge": [], "prof": {}}
for t0 in np.arange(-180, 180, 10.0):
    d = ((th - t0 + 180) % 360) - 180
    s = (np.abs(d) < 2.0) & (r > 3.5) & (r < 6.5)
    prof = np.full(len(zg), np.nan)
    for i, zz in enumerate(zg):
        ss = s & (np.abs(z - zz) < dz / 2 + 0.02)
        if ss.sum(): prof[i] = r[ss].max()
    res["prof"][str(t0)] = [None if np.isnan(p) else round(float(p), 3) for p in prof]
    # sleeve band: r > 5.5
    band = prof > 5.5
    idx = np.where(band)[0]
    if len(idx) == 0: continue
    zb, zt = zg[idx[0]], zg[idx[-1]]
    # valleys: local minima of r within band interior (exclude 0.4 at ends), smoothed
    p = prof.copy(); good = ~np.isnan(p)
    ps = np.convolve(np.where(good, p, np.nanmean(p)), np.ones(3) / 3, mode="same")
    vals = [zg[i] for i in range(idx[0] + 6, idx[-1] - 6) if ps[i] < ps[i - 3] and ps[i] <= ps[i + 3] and ps[i] == min(ps[i - 4:i + 5])]
    crs = [zg[i] for i in range(idx[0] + 4, idx[-1] - 4) if ps[i] == max(ps[i - 5:i + 6])]
    res["theta"].append(t0); res["valleys"].append(vals); res["crests"].append(crs); res["bot_edge"].append(float(zb)); res["top_edge"].append(float(zt))
    print(f"th={t0:6.0f} bot={zb:.2f} top={zt:.2f} valleys={[round(a,2) for a in vals]} crests={[round(a,2) for a in crs]}")
json.dump(res, open(f"{RUN}/measure/figures/thread.json", "w"))
