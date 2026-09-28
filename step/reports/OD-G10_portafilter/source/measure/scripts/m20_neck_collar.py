"""it2 (builder self-check): the neck cone and the collar are not coaxial with the grip axis. IRLS circle fits
on full x-sections (aligned working copy) of the neck cone (x 41.9..44.2, beyond the channel end) and the
collar front flank (x 44.9..47.3), 0.1 mm steps; per part: line fits r(x) and centre offset (cy, cz) relative
to the grip axis (handle_axis.json), median over the stations. Replaces the upper-envelope p99 fits of m09
for these two parts (p99 of noisy samples biased them outward)."""
import json, sys, numpy as np, trimesh
sys.path.insert(0, sys.argv[1]); from datum_fit import fit_circle
A = json.load(open('measure/figures/handle_axis.json')); p0 = np.array(A['axis_point_x0']); d = np.array(A['axis_dir'])
m = trimesh.load('intake/aligned_work.stl'); out = {}
for key, lo, hi in (("neck_cone", 41.9, 44.2), ("collar_flank", 44.9, 47.3)):
    st = []
    for x in np.arange(lo, hi + 1e-6, 0.1):
        L = trimesh.intersections.mesh_plane(m, [1, 0, 0], [x, 0, 0]).reshape(-1, 3)[:, 1:]
        L = L[(np.abs(L[:, 0]) < 20) & (L[:, 1] < -10) & (L[:, 1] > -52)]
        if len(L) < 40: continue
        c = fit_circle(L, 'irls', 0.30)
        st.append([x, c['cx'] - (p0[1] + d[1] / d[0] * x), c['cy'] - (p0[2] + d[2] / d[0] * x), c['r'], c['rms']])
    S = np.array(st); b, a = np.polyfit(S[:, 0], S[:, 3], 1); res = S[:, 3] - (a + b * S[:, 0])
    out[key] = {"r = a + b t": [float(a), float(b)], "r_rms": float(np.sqrt((res**2).mean())), "dy_off": float(np.median(S[:, 1])), "dz_off": float(np.median(S[:, 2])),
                "circle_rms_median": float(np.median(S[:, 4])), "n": int(len(S)), "x_range": [lo, hi]}
json.dump(out, open('measure/figures/neck_collar.json', 'w'), indent=1); print(json.dumps(out, indent=1))
