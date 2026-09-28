"""Run-local: binned r-z medians in theta windows (full-res, datum frame): rim, walls, bead.
Writes measure/figures/rz_profile.json"""
import json, numpy as np, trimesh
m = trimesh.load('input/scan.stl'); T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4']); m.apply_transform(T)
V = m.vertices; r = np.hypot(V[:, 0], V[:, 1]); th = np.degrees(np.arctan2(V[:, 1], V[:, 0])) % 360; z = V[:, 2]
gap = ((th > 50) & (th < 85)) | ((th > 165) & (th < 200)) | ((th > 285) & (th < 320))
out = {}
# rim top: z vs r (up surfaces), r 36.9..40.3
s = gap & (z > 1.0) & (r > 36.8)
rb = np.arange(36.8, 40.4, 0.1); rim = []
for a in rb:
    t = s & (r >= a) & (r < a + 0.1)
    if t.sum() > 20: rim.append([round(a + 0.05, 2), round(float(np.percentile(z[t], 90)), 3), int(t.sum())])
out['rim_zmax_vs_r_gap'] = rim
# walls: r vs z (vertical surfaces) outer r>39.5, bore 36.5<r<37.6 (gap sectors), per 1mm z bin
for name, (r0, r1, sel) in {'outer_wall': (39.5, 40.6, np.ones_like(gap)), 'bore_gap': (36.6, 37.6, gap)}.items():
    rows = []
    for zz in np.arange(-28, 3, 1.0):
        t = sel & (r > r0) & (r < r1) & (z >= zz) & (z < zz + 1)
        if t.sum() > 50: rows.append([zz + 0.5, round(float(np.median(r[t])), 3), int(t.sum())])
    out[name + '_r_vs_z'] = rows
# lip/bead: r vs z in gap sectors, 30<r<32.5, per 0.25 z
rows = []
for zz in np.arange(-20, -14, 0.25):
    t = gap & (r > 30.0) & (r < 32.3) & (z >= zz) & (z < zz + 0.25)
    if t.sum() > 30: rows.append([zz + 0.125, round(float(np.median(r[t])), 3), int(t.sum())])
out['lip_gap_r_vs_z'] = rows
lug = ((th - 336) % 120 > 5) & ((th - 336) % 120 < 50)
rows = []
for zz in np.arange(-20, -16, 0.25):
    t = lug & (r > 29.5) & (r < 31.5) & (z >= zz) & (z < zz + 0.25)
    if t.sum() > 30: rows.append([zz + 0.125, round(float(np.median(r[t])), 3), int(t.sum())])
out['lip_lug_r_vs_z'] = rows
json.dump(out, open('measure/figures/rz_profile.json', 'w'), indent=1)
for k, v in out.items(): print(k, v)
