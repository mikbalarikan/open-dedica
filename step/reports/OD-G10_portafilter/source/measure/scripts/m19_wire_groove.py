"""it2 (builder self-check on the full-res scan): a V-shaped groove in the rim bore that seats the wire spring.
Full-res scan in the datum frame; per 5-degree bin: max r of samples in z [-3.6, -2.2], r [27.4, 29.4].
Groove theta span = the longest run of bins with that max r > bore(z) + 0.35, gaps up to 15 deg bridged
(the wire hides the groove in places). Profile: in the span, the groove apex
(r, z) = median of the deepest point per bin, and the upper/lower groove edges = p75 / p25 z of the samples more than 0.1 mm behind the bore line,
above / below the apex (robust against the rim round above and the wire below)."""
import json, numpy as np, trimesh
A = json.load(open('intake/alignment.json')); T = np.array(A['matrix_4x4'])
m = trimesh.load('input/scan.stl'); P = m.vertices @ T[:3, :3].T + T[:3, 3]
B = json.load(open('measure/figures/body_profile.json'))['bore_upper']; bore = lambda z: B['a'] + B['b'] * z
r = np.hypot(P[:, 0], P[:, 1]); th = np.degrees(np.arctan2(P[:, 1], P[:, 0])); z = P[:, 2]
bins = []
for a in range(-180, 180, 5):
    s = (th >= a) & (th < a + 5) & (z > -3.6) & (z < -2.2) & (r > 27.4) & (r < 29.4)
    if s.sum() < 10: bins.append((a, None, None)); continue
    k = np.argmax(r[s] - bore(z[s])); bins.append((a, float(r[s][k] - bore(z[s][k])), float(z[s][k])))
deep = [b for b in bins if b[1] is not None and b[1] > 0.35]
th_in = [b[0] for b in deep]
# longest contiguous run
runs, cur = [], [th_in[0]]
for t in th_in[1:]:
    if t - cur[-1] <= 15: cur.append(t)
    else: runs.append(cur); cur = [t]
runs.append(cur); run = max(runs, key=len)
t0, t1 = run[0], run[-1] + 5
sel = (th >= t0) & (th < t1) & (r > 27.4) & (r < 29.4) & (z > -4.5) & (z < -1.2)
dep = r[sel] - bore(z[sel]); zz = z[sel]
apex_z = float(np.median([b[2] for b in deep if t0 <= b[0] < t1])); apex_d = float(np.median([b[1] for b in deep if t0 <= b[0] < t1]))
up = zz[(dep > 0.1) & (zz > apex_z)]; lo = zz[(dep > 0.1) & (zz < apex_z)]
out = {"bins": bins, "theta_span_deg": [float(t0), float(t1)], "apex_depth_mm": apex_d, "apex_z": apex_z,
       "upper_edge_z": float(np.percentile(up, 75)), "lower_edge_z": float(np.percentile(lo, 25)), "runs": runs}
json.dump(out, open('measure/figures/wire_groove.json', 'w'), indent=1)
print({k: v for k, v in out.items() if k not in ('bins',)})
