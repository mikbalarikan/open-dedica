"""Stem ribs: angle, width, tip radius vs z, top end z. Stem-group local frame (tilted line).
Writes ../ribs.json"""
import json, sys, numpy as np, trimesh
RUN = sys.argv[1]
L = json.load(open(f"{RUN}/measure/figures/axis_stations.json"))["stem_group_line"]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); v = m.vertices
cx = L["x0"] + L["dxdz"] * v[:, 2]; cy = L["y0"] + L["dydz"] * v[:, 2]
x, y, z = v[:, 0] - cx, v[:, 1] - cy, v[:, 2]; r = np.hypot(x, y); th = np.degrees(np.arctan2(y, x))
res = {}
for nom in [0, 90, 180, -90]:
    d = ((th - nom + 180) % 360) - 180
    rows = []
    for z0 in np.arange(17.5, 31.6, 1.0):
        s = (np.abs(z - z0) < 0.2) & (np.abs(d) < 15) & (r > 5.75) & (r < 7)
        if s.sum() < 5: rows.append((z0, None)); continue
        # tangential coordinate
        t = r[s] * np.radians(d[s]); rr = r[s]
        tip = float(np.percentile(rr, 98)); ang = float(np.average(d[s], weights=(rr - 5.7)))
        wid_at = {}
        for rl in (5.9, 6.1):
            ss = np.abs(rr - rl) < 0.04
            wid_at[rl] = float(t[ss].max() - t[ss].min()) if ss.sum() > 3 else None
        rows.append((z0, dict(tip=tip, ang=ang, w59=wid_at[5.9], w61=wid_at[6.1], n=int(s.sum()))))
    res[str(nom)] = rows
    print("rib", nom)
    for z0, dd in rows:
        print(f"  z={z0:5.1f}", "none" if dd is None else f"tip={dd['tip']:.3f} ang={dd['ang']:+.2f} w@5.9={dd['w59']} w@6.1={dd['w61']} n={dd['n']}")
    # top end: highest z with r>5.7 in rib sector
    s = (np.abs(d) < 6) & (r > 5.6) & (z > 25) & (z < 33)
    zz = z[s]; print("  top z (r>5.6): p99 %.3f max %.3f" % (np.percentile(zz, 99), zz.max()))
json.dump(res, open(f"{RUN}/measure/figures/ribs.json", "w"), indent=1)
