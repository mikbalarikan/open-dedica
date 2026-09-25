"""Fit the sleeve end-edge offset f(theta): planar sector A (level 0) + helical ramp B (0 -> h) + step.
Uses bottom/top edge heights per 10-deg azimuth from ../thread.json (stem-group frame).
Also finer 2-deg edge heights. Writes ../jog.json"""
import json, sys, numpy as np, trimesh
from scipy.optimize import least_squares
RUN = sys.argv[1]
L = json.load(open(f"{RUN}/measure/figures/axis_stations.json"))["stem_group_line"]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); v = m.vertices
cx = L["x0"] + L["dxdz"] * v[:, 2]; cy = L["y0"] + L["dydz"] * v[:, 2]
x, y, z = v[:, 0] - cx, v[:, 1] - cy, v[:, 2]; r = np.hypot(x, y); th = np.degrees(np.arctan2(y, x)) % 360
T = np.arange(0, 360, 3.0); bot = []; top = []
for t0 in T:
    d = ((th - t0 + 180) % 360) - 180
    s = (np.abs(d) < 1.5)
    sb = s & (r > 5.45) & (r < 6.3) & (z > 31.8) & (z < 34)      # sleeve OD near the bottom
    st = s & (r > 4.6) & (r < 5.4) & (z > 36.5) & (z < 38.4)     # top face mid-radius band (r 4.6-5.4)
    bot.append(np.percentile(z[sb], 1) if sb.sum() > 5 else np.nan)
    top.append(np.percentile(z[st], 99) if st.sum() > 5 else np.nan)
bot, top = np.array(bot), np.array(top)
def model(q, t):
    b0, b1, h, zb = q  # ramp start/end angles (deg, 0..360), ramp height, level
    tt = (t - b1) % 360          # angle after the step (step at b1)
    span = (b1 - b0) % 360
    f = np.where(tt >= 360 - span, h * (tt - (360 - span)) / span, 0.0)
    return zb + f
out = {}
for nm, e in (("bottom", bot), ("top", top)):
    g = ~np.isnan(e)
    q0 = [130.0, 250.0, 1.0, np.nanmedian(e)]
    so = least_squares(lambda q: model(q, T[g]) - e[g], q0, loss="soft_l1", f_scale=0.05)
    res = so.fun
    out[nm] = {"ramp_start_deg": so.x[0] % 360, "ramp_end_step_deg": so.x[1] % 360, "ramp_h": so.x[2], "level_z": so.x[3],
               "rms": float(np.sqrt(np.mean(res**2))), "p95": float(np.percentile(np.abs(res), 95)), "n": int(g.sum())}
    print(nm, {k: round(float(v), 3) for k, v in out[nm].items()})
# joint fit: common angles & height, separate levels
g1, g2 = ~np.isnan(bot), ~np.isnan(top)
def rj(q):
    b0, b1, h, zb, zt = q
    return np.r_[model([b0, b1, h, zb], T[g1]) - bot[g1], model([b0, b1, h, zt], T[g2]) - top[g2]]
so = least_squares(rj, [130, 250, 1.0, 32.3, 37.2], loss="soft_l1", f_scale=0.05); rr = so.fun
out["joint"] = {"ramp_start_deg": so.x[0] % 360, "ramp_end_step_deg": so.x[1] % 360, "ramp_h": so.x[2], "bottom_level_z": so.x[3],
                "top_level_z": so.x[4], "rms": float(np.sqrt(np.mean(rr**2))), "p95": float(np.percentile(np.abs(rr), 95)), "max": float(np.abs(rr).max())}
print("joint", {k: round(float(v), 3) for k, v in out["joint"].items()})
out["theta_deg"] = T.tolist(); out["bottom_edge_z_p1"] = [None if np.isnan(a) else float(a) for a in bot]; out["top_face_z_p99_r4.6-5.4"] = [None if np.isnan(a) else float(a) for a in top]
out["frame"] = "stem-group local frame: datum XY shifted to the tilted stem-group line (axis_stations.json); theta CCW about +Z from datum +X, 0..360"
json.dump(out, open(f"{RUN}/measure/figures/jog.json", "w"), indent=1)
