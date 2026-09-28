"""m02_cup_profile.py - meridian (r,z) profile of cups A/B and the middle boss about their fitted axes.
Axis x-positions come from intake/alignment.json (clock detail: centre_from/centre_to, rotated into the
datum frame they sit at x = -sep/2, +sep/2, y = 0). Sectors within 30 deg of +-X (webs, ears) are excluded.
Writes measure/figures/m02_profile_<name>.npz, m02_cup_profile.png, m02_cup_profile.json."""
import json, numpy as np, trimesh, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
al = json.load(open('intake/alignment.json'))
sep = al['clock']['detail']['separation_mm']
m = trimesh.load('intake/aligned_work.stl'); V = m.vertices
axes = {'cupA': -sep/2, 'cupB': sep/2, 'boss': 0.0}
out = {"tool": "measure/scripts/m02_cup_profile.py", "cup_axis_x": [-sep/2, sep/2], "sector_excl_deg": 30}
fig, axs = plt.subplots(1, 3, figsize=(24, 14))
for ax, (nm, cx) in zip(axs, axes.items()):
    q = V[:, :2] - [cx, 0]; r = np.hypot(*q.T); th = np.degrees(np.arctan2(q[:, 1], q[:, 0]))
    k = (np.abs(np.abs(th) - 90) < 60) & (r < (16 if nm != 'boss' else 7.5))
    np.savez_compressed(f'measure/figures/m02_profile_{nm}.npz', r=r[k], z=V[k, 2], th=th[k])
    ax.plot(r[k], V[k, 2], ',', alpha=0.4)
    ax.set_title(nm); ax.set_aspect('equal'); ax.minorticks_on(); ax.grid(True, which='major', lw=0.5); ax.grid(True, which='minor', lw=0.15)
    ax.set_xticks(np.arange(0, 17, 1)); ax.set_yticks(np.arange(-3, 30, 1))
plt.tight_layout(); plt.savefig('measure/figures/m02_cup_profile.png', dpi=60)
json.dump(out, open('measure/figures/m02_cup_profile.json', 'w'), indent=1)
