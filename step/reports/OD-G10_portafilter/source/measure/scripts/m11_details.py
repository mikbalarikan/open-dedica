"""Remaining detail measurements (datum frame, seeded samples):
pad under-chamfer line x(z) at |y| in [8.5, 11.8]; pad half-width line from neck_pad.json edges;
U-rib inner/outer faces, open-end and round-end x; spout pocket opening radius (height map);
spout boss wall line r(z) and bottom-ring z; lug under-face ramp lines z(theta)."""
import json, numpy as np, trimesh
m = trimesh.load('intake/aligned_work.stl'); P, fi = trimesh.sample.sample_surface(m, 3000000, seed=0); Nf = m.face_normals[fi]
x, y, z = P.T; out = {}
s = (np.abs(y) > 8.5) & (np.abs(y) < 11.8) & (z > -35.8) & (z < -32.2) & (x > 26) & (x < 31.5) & (Nf[:, 2] < -0.3) & (Nf[:, 0] > 0.3)
b, a = np.polyfit(z[s], x[s], 1); e = x[s] - (a + b * z[s])
out["pad_underchamfer"] = {"x = a + b z": [float(a), float(b)], "rms": float(np.sqrt((e**2).mean())), "n": int(s.sum())}
E = np.array(json.load(open('measure/figures/neck_pad.json'))["pad_edges_z_ymin_ymax"]); k = (E[:, 0] >= -24) & (E[:, 0] <= -4)
hw = (E[k, 2] - E[k, 1]) / 2; b2, a2 = np.polyfit(E[k, 0], hw, 1)
out["pad_halfwidth"] = {"hw = a + b z": [float(a2), float(b2)], "rms": float(np.sqrt(((hw - (a2 + b2 * E[k, 0]))**2).mean())), "centre_y": float(np.mean((E[k, 2] + E[k, 1]) / 2))}
leg = (x > -12) & (x < 0) & (z > -33) & (z < -28.5) & (np.abs(y) > 4) & (np.abs(y) < 8.5) & (np.abs(Nf[:, 1]) > 0.85)
inner = leg & (np.sign(Nf[:, 1]) == -np.sign(y)); outer = leg & (np.sign(Nf[:, 1]) == np.sign(y))
out["U_leg_inner_face_absy"] = float(np.median(np.abs(y[inner]))); out["U_leg_outer_face_absy"] = float(np.median(np.abs(y[outer])))
top = (z > -27.6) & (np.hypot(x, y) < 21)
out["U_top_x_range"] = [float(np.percentile(x[top], 0.2)), float(np.percentile(x[top], 99.8))]
end = top & (x > 2); out["U_round_end_outer_x"] = float(np.percentile(x[end], 99.8))
H = np.load('measure/figures/floor_heightmap_max_z.npy'); res = 0.2; n = H.shape[0]; xs = -25 + res * (np.arange(n) + 0.5); X, Y = np.meshgrid(xs, xs)
S = json.load(open('measure/figures/spouts_screw.json')); op = []
for key in ("spout_0", "spout_1"):
    cx, cy = S[key]["cx"], S[key]["cy"]; d = np.hypot(X - cx, Y - cy); deep = (d < 7) & ((H < -48) | np.isnan(H))
    op.append(float(np.percentile(d[deep], 97)))
    rr = np.hypot(x - cx, y - cy); w = (rr > 5.5) & (rr < 7) & (z > -55.3) & (z < -50.3) & (Nf[:, 2] < 0.3)
    bb, aa = np.polyfit(z[w], rr[w], 1); out[f"{key}_boss_wall r = a + b z"] = [float(aa), float(bb)]
    ring = (rr > 4.3) & (rr < 5.4) & (z < -55.8) & (z > -57) & (Nf[:, 2] < -0.8); out[f"{key}_bottom_ring_z"] = float(np.median(z[ring]))
    head = (rr > 3.0) & (rr < 3.4) & (z < -56.9) & (z > -58.2); out[f"{key}_head_z_at_r3.2"] = float(np.median(z[head])) if head.sum() else None
out["spout_pocket_opening_r"] = op
L = json.load(open('measure/figures/lugs_notches.json'))["lugs"]; lr = []
for l in L:
    a_ = np.array([t for t, zz in l["under_z_by_deg"] if zz is not None]); zz_ = np.array([zz for t, zz in l["under_z_by_deg"] if zz is not None])
    a_ = np.where(a_ < l["start_deg"] - 1, a_ + 360, a_); core = (a_ > l["start_deg"] + 3) & (a_ < l["start_deg"] + l["span_deg"] - 4)
    bb, aa = np.polyfit(a_[core] - l["centre_deg"], zz_[core], 1); e = zz_[core] - (aa + bb * (a_[core] - l["centre_deg"]))
    lr.append({"centre_deg": l["centre_deg"], "z_at_centre": float(aa), "dz_per_deg": float(bb), "rms": float(np.sqrt((e**2).mean()))})
out["lug_ramps"] = lr
json.dump(out, open('measure/figures/details.json', 'w'), indent=1); print(json.dumps(out, indent=1))
