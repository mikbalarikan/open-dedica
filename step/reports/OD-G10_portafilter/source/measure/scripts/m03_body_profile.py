"""Body (cup) revolve profile: primitive fits on (r,z) scan points from clean sectors
theta in [102,155] U [-155,-102] (no lugs, spouts, neck, rim notches), datum frame.
Floor cone + floor fillet from theta in [150,210] with the U-rib band removed.
Writes measure/figures/body_profile.json and body_profile.png (fits overlaid)."""
import json, numpy as np, trimesh, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
m = trimesh.load('intake/aligned_work.stl')
P, _ = trimesh.sample.sample_surface(m, 3000000, seed=0)
r = np.hypot(P[:, 0], P[:, 1]); z = P[:, 2]; th = np.degrees(np.arctan2(P[:, 1], P[:, 0]))
clean = ((th > 102) & (th < 155)) | ((th < -102) & (th > -155))
back = (np.abs(th) > 150)
urib = (P[:, 0] > -17) & (P[:, 0] < 6) & (np.abs(np.abs(P[:, 1]) - 5.6) < 1.5)
def line(sel, xa, ya):  # ya = a + b*xa
    b, a = np.polyfit(xa[sel], ya[sel], 1); res = ya[sel] - (a + b * xa[sel])
    return {"a": float(a), "b": float(b), "rms": float(np.sqrt((res**2).mean())), "max": float(np.abs(res).max()), "n": int(sel.sum())}
def circ(sel, u, v):
    A = np.c_[2*u[sel], 2*v[sel], np.ones(sel.sum())]; bb = u[sel]**2 + v[sel]**2
    c, *_ = np.linalg.lstsq(A, bb, rcond=None); R = np.sqrt(c[2] + c[0]**2 + c[1]**2)
    res = np.hypot(u[sel]-c[0], v[sel]-c[1]) - R
    return {"cu": float(c[0]), "cv": float(c[1]), "R": float(R), "rms": float(np.sqrt((res**2).mean())), "max": float(np.abs(res).max()), "n": int(sel.sum())}
def sphere_axis(sel):  # centre on the axis: r^2 + (z-z0)^2 = R^2  -> z^2 + r^2 = 2 z z0 + (R^2 - z0^2)
    A = np.c_[2*z[sel], np.ones(sel.sum())]; bb = z[sel]**2 + r[sel]**2
    c, *_ = np.linalg.lstsq(A, bb, rcond=None); z0 = c[0]; R = np.sqrt(c[1] + z0**2)
    res = np.hypot(r[sel], z[sel]-z0) - R
    return {"z0": float(z0), "R": float(R), "apex_z": float(z0 - R), "rms": float(np.sqrt((res**2).mean())), "max": float(np.abs(res).max()), "n": int(sel.sum())}
F = {}
F["rim_top_z"] = {"median": float(np.median(z[clean & (r > 28.4) & (r < 30.1) & (z > -0.3)])),
                  "p05": float(np.percentile(z[clean & (r > 28.4) & (r < 30.1) & (z > -0.3)], 5))}
F["outer_wall"] = line(clean & (z < -3) & (z > -38) & (r > 28.6) & (r < 31), z, r)         # r = a + b z
F["dome"] = sphere_axis(clean & (r > 7) & (r < 24) & (z < -45))
F["dome_center_flat_z"] = float(np.median(z[clean & (r < 5.5) & (z < -48.5)])) if (clean & (r < 5.5) & (z < -48.5)).sum() else None
F["bottom_corner"] = circ(clean & (r > 26.3) & (r < 29.0) & (z > -46.3) & (z < -41.5) & (r - (F["outer_wall"]["a"] + F["outer_wall"]["b"] * z) < -0.05), r, z)
F["bore_upper"] = line(clean & (z < -7.5) & (z > -10.8) & (r > 27.2) & (r < 27.9), z, r)
F["ledge_z"] = {"median": float(np.median(z[clean & (r > 26.0) & (r < 27.0) & (z > -12) & (z < -11)]))}
F["insert_wall"] = line(clean & (z < -17) & (z > -32) & (r > 23.5) & (r < 24.8), z, r)
F["ledge_taper"] = line(clean & (z < -12.3) & (z > -15.5) & (r > 24.2) & (r < 25.9), z, r)
F["floor_cone"] = line(back & ~urib & (r > 1) & (r < 16) & (z < -32) & (z > -38.5), r, z)   # z = a + b r
F["floor_fillet"] = circ(back & ~urib & (r > 20.5) & (r < 23.8) & (z < -33.5) & (z > -37.5), r, z)
F["rim_inner_round"] = circ(clean & (r > 27.4) & (r < 28.4) & (z > -1.2) & (z < -0.05), r, z)
F["rim_outer_round"] = circ(clean & (r > 30.1) & (r < 30.8) & (z > -0.6) & (z < -0.03), r, z)
json.dump(F, open('measure/figures/body_profile.json', 'w'), indent=1)
print(json.dumps(F, indent=1))
fig, ax = plt.subplots(1, 2, figsize=(22, 14))
for a in ax:
    s = clean; a.scatter(r[s], z[s], s=0.1, c='k'); s = back & ~urib & (r < 24); a.scatter(r[s], z[s], s=0.1, c='g')
    a.set_aspect('equal'); a.minorticks_on(); a.grid(which='both', alpha=.4)
zz = np.linspace(-40, 0, 50); ax[0].plot(F["outer_wall"]["a"] + F["outer_wall"]["b"]*zz, zz, 'r-')
rr = np.linspace(0, 26, 50); ax[0].plot(rr, F["dome"]["z0"] - np.sqrt(F["dome"]["R"]**2 - rr**2), 'r-')
rr = np.linspace(0, 22, 50); ax[1].plot(rr, F["floor_cone"]["a"] + F["floor_cone"]["b"]*rr, 'r-')
zz = np.linspace(-34, -16, 20); ax[1].plot(F["insert_wall"]["a"] + F["insert_wall"]["b"]*zz, zz, 'r-')
for k, a in (("bottom_corner", ax[0]), ("floor_fillet", ax[1]), ("rim_inner_round", ax[1]), ("rim_outer_round", ax[0])):
    t = np.linspace(0, 2*np.pi, 100); c = F[k]; a.plot(c["cu"] + c["R"]*np.cos(t), c["cv"] + c["R"]*np.sin(t), 'b-')
ax[0].set_xlim(0, 36); ax[0].set_ylim(-52, 1); ax[1].set_xlim(0, 30); ax[1].set_ylim(-42, 1)
plt.tight_layout(); plt.savefig('measure/figures/body_profile.png', dpi=50)
