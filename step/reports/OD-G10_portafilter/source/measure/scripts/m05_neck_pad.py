"""Neck arch (x = 32..37.5 sections, handle-axis frame) and the flat pad on the cup wall (+X side).
Arch: outer radius about the handle axis (points above the axis), channel half-width (inner side walls),
channel roof radius, leg-foot z. Pad: plane fit on points 0.4 mm proud of the cup cone, lateral edges vs z."""
import json, numpy as np, trimesh
A = json.load(open('measure/figures/handle_axis.json')); p0 = np.array(A['axis_point_x0']); d = np.array(A['axis_dir'])
m = trimesh.load('intake/aligned_work.stl'); P, N_ = None, None
P, fi = trimesh.sample.sample_surface(m, 3000000, seed=0); Nf = m.face_normals[fi]
out = {}
# --- arch sections in the handle frame: v = y - axis_y(x), w = z - axis_z(x)
x = P[:, 0]; ay = p0[1] + d[1] / d[0] * x; az = p0[2] + d[2] / d[0] * x
v = P[:, 1] - ay; w = P[:, 2] - az; rr = np.hypot(v, w)
s = (x > 32) & (x < 37.5)
top = s & (w > 2) & (rr > 8.5) & (rr < 11.5)
out["arch_outer_r"] = {"median": float(np.median(rr[top])), "p05": float(np.percentile(rr[top], 5)), "p95": float(np.percentile(rr[top], 95)), "n": int(top.sum())}
roof = s & (w > 3) & (rr > 4.5) & (rr < 7.5) & (Nf[:, 2] < 0)  # channel roof faces point down
out["channel_roof_r"] = {"median": float(np.median(rr[roof])), "n": int(roof.sum())}
wall = s & (w < -1) & (w > -5.5) & (np.abs(v) > 4.5) & (np.abs(v) < 7.5) & (np.abs(Nf[:, 1]) > 0.8)
inner = wall & (np.sign(v) == -np.sign(Nf[:, 1]))  # channel walls face the channel
out["channel_halfwidth"] = {"v_pos": float(np.median(v[inner & (v > 0)])), "v_neg": float(np.median(v[inner & (v < 0)])), "n": int(inner.sum())}
side = s & (w < -1) & (w > -5) & (np.abs(v) > 8.5) & (np.abs(v) < 11)
out["leg_outer_halfwidth"] = {"v_pos": float(np.median(v[side & (v > 0)])), "v_neg": float(np.median(v[side & (v < 0)]))}
foot = s & (w < -5) & (np.abs(v) > 6) & (np.abs(v) < 10)
out["foot_min_w"] = {"p01": float(np.percentile(w[foot], 1)), "median_of_lowest_decile": float(np.median(np.sort(w[foot])[: max(1, foot.sum() // 10)]))}
out["axis_z_at_x35"] = float(p0[2] + d[2] / d[0] * 35)
# channel end (x where channel roof stops) and cone flare start
for lo, hi, key in ((38.0, 45.0, "roof_x_extent"),):
    ss = (x > 28) & (x < 46) & (w > 3) & (rr > 4.5) & (rr < 7.5) & (Nf[:, 2] < -0.5)
    out[key] = {"x_min": float(np.percentile(x[ss], 0.5)), "x_max": float(np.percentile(x[ss], 99.5))}
ss = (x > 38) & (x < 46) & (np.abs(Nf[:, 0]) > 0.9) & (rr > 5) & (rr < 11) & (Nf[:, 0] < 0)
out["channel_end_x"] = float(np.median(x[ss])) if ss.sum() else None
# --- pad
r = np.hypot(P[:, 0], P[:, 1]); cone = 30.5864 + 0.044919 * P[:, 2]
pad = (P[:, 0] > 25) & (P[:, 0] < 34) & (np.abs(P[:, 1]) < 11.5) & (P[:, 2] > -33) & (P[:, 2] < -2) & (r - cone > 0.3) & (Nf[:, 0] > 0.9) & ~((np.abs(v) < 10.5) & (w < 10.5))
X = np.c_[P[pad, 1], P[pad, 2], np.ones(pad.sum())]; c, *_ = np.linalg.lstsq(X, P[pad, 0], rcond=None); res = P[pad, 0] - X @ c
out["pad_plane_x_eq"] = {"x = a*y + b*z + c": c.tolist(), "rms": float(np.sqrt((res**2).mean())), "max": float(np.abs(res).max()), "n": int(pad.sum())}
edges = []
for zc in np.arange(-34, -1, 2.0):
    sz = (P[:, 0] > 25) & (P[:, 0] < 34) & (np.abs(P[:, 2] - zc) < 0.5) & (np.abs(P[:, 1]) < 17) & (r - cone > 0.25) & (np.abs(P[:, 1]) > 9)
    if sz.sum() > 10: edges.append([float(zc), float(np.percentile(P[sz, 1], 0.5)), float(np.percentile(P[sz, 1], 99.5))])
out["pad_edges_z_ymin_ymax"] = edges
json.dump(out, open('measure/figures/neck_pad.json', 'w'), indent=1); print(json.dumps(out, indent=1))
