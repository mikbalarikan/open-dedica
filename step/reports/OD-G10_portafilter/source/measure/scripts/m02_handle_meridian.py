"""Handle axis = least-squares line through the IRLS circle centres (x 50..155, clean grip);
meridian r(x) about that axis for all scan points near the handle. Writes handle_axis.json + PNG."""
import json, numpy as np, trimesh, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
S = json.load(open('measure/figures/handle_stations.json'))['stations']
st = [s for s in S if 50 <= s['x'] <= 155]
x = np.array([s['x'] for s in st]); cy = np.array([s['cy'] for s in st]); cz = np.array([s['cz'] for s in st]); r = np.array([s['r'] for s in st])
by, ay = np.polyfit(x, cy, 1); bz, az = np.polyfit(x, cz, 1)
d = np.array([1, by, bz]); d /= np.linalg.norm(d); p0 = np.array([0, ay, az])
lin = np.polyfit(x, r, 1); quad = np.polyfit(x, r, 2)
res_lin = r - np.polyval(lin, x); res_q = r - np.polyval(quad, x)
m = trimesh.load('intake/aligned_work.stl')
P, _ = trimesh.sample.sample_surface(m, 2000000, seed=0)
q = P - p0; t = q @ d; rad = np.linalg.norm(q - np.outer(t, d), axis=1)
sel = (t > 28) & (rad < 20)
ang = np.degrees(np.arctan2((q - np.outer(t, d))[:, 1], (q - np.outer(t, d))[:, 2]))  # 0 = +z (top)
out = {"axis_point_x0": p0.tolist(), "axis_dir": d.tolist(),
       "axis_tilt_deg": float(np.degrees(np.arccos(d[0]))), "yz_slope": [float(by), float(bz)],
       "r_linear": {"slope": float(lin[0]), "r_at_x0": float(lin[1]), "rms": float(np.sqrt((res_lin**2).mean())), "max": float(np.abs(res_lin).max())},
       "r_quadratic": quad.tolist(), "r_quad_rms": float(np.sqrt((res_q**2).mean())), "n_stations": len(st)}
json.dump(out, open('measure/figures/handle_axis.json', 'w'), indent=1); print(json.dumps(out, indent=1))
fig, ax = plt.subplots(2, 1, figsize=(22, 12))
for a, (lo, hi, rl, rh) in zip(ax, [(28, 60, 4, 17), (145, 168, 4, 17)]):
    s = sel & (t > lo) & (t < hi)
    a.scatter(t[s], rad[s], s=0.2, c=np.abs(ang[s]), cmap='jet'); a.set_xlim(lo, hi); a.set_ylim(rl, rh); a.set_aspect('equal'); a.minorticks_on(); a.grid(which='both', alpha=.4)
plt.tight_layout(); plt.savefig('measure/figures/handle_meridian.png', dpi=55)
np.save('/tmp/claude-0/-home-user-agentic-STL-to-CAD/cc506760-1589-506d-be19-e4c0f022b577/scratchpad/hax.npy', np.r_[p0, d])
