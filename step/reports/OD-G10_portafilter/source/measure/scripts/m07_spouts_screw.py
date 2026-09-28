"""Spout bosses (2) and centre screw: axis from IRLS circle fits on boss outer sections z -50..-55;
meridian r(z) about each axis (outer boss, tip dome, inner pocket seen from the cup); centre screw
disc and recess from the bottom height map."""
import json, sys, numpy as np, trimesh, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0, sys.argv[1]); from datum_fit import fit_circle
m = trimesh.load('intake/aligned_work.stl'); P, fi = trimesh.sample.sample_surface(m, 3000000, seed=0); Nf = m.face_normals[fi]
out = {}
fig, axs = plt.subplots(1, 3, figsize=(30, 12))
for k, (cx0, cy0) in enumerate(((10.0, 15.0), (10.0, -15.0))):
    st = []
    for zc in np.arange(-55.0, -49.4, 0.5):
        L = trimesh.intersections.mesh_plane(m, [0, 0, 1], [0, 0, zc]).reshape(-1, 3)
        q = L[np.hypot(L[:, 0] - cx0, L[:, 1] - cy0) < 8.5][:, :2]
        if len(q) > 30: st.append({"z": float(zc), **fit_circle(q, 'irls', 0.30)})
    cx = float(np.median([s["cx"] for s in st])); cy = float(np.median([s["cy"] for s in st]))
    rr = np.hypot(P[:, 0] - cx, P[:, 1] - cy); s = rr < 9
    out[f"spout_{k}"] = {"cx": cx, "cy": cy, "stations": [{kk: (round(v, 4) if isinstance(v, float) else v) for kk, v in x.items()} for x in st],
                         "theta_deg": float(np.degrees(np.arctan2(cy, cx))), "radius_from_axis": float(np.hypot(cx, cy))}
    zz = P[s, 2]; out[f"spout_{k}"]["tip_zmin"] = float(np.percentile(zz[rr[s] < 1.5], 0.5))
    axs[k].scatter(rr[s], zz, s=0.1, c=Nf[s, 2], cmap='coolwarm'); axs[k].set_xlim(0, 9); axs[k].set_ylim(-60, -36); axs[k].set_aspect('equal'); axs[k].minorticks_on(); axs[k].grid(which='both', alpha=.4)
# centre screw disc / recess on the bottom
H = np.load('/tmp/claude-0/-home-user-agentic-STL-to-CAD/cc506760-1589-506d-be19-e4c0f022b577/scratchpad/Hbot.npy'); res = 0.2; x0 = -31
n = H.shape[0]; xs = x0 + res * (np.arange(n) + 0.5); X, Y = np.meshgrid(xs, xs); R = np.hypot(X, Y)
dome = 51.1 - np.sqrt(100.536**2 - R**2); D = H - dome
disc = (D > 0.08) & (D < 0.5) & (np.hypot(X + 3, Y) < 6)
w = disc.astype(float); cxs = float((X * w).sum() / w.sum()); cys = float((Y * w).sum() / w.sum())
rd = np.hypot(X - cxs, Y - cys)
out["centre_screw"] = {"cx": cxs, "cy": cys, "disc_r_p98": float(np.percentile(rd[disc], 98)), "disc_raise_median": float(np.median(D[disc])),
                       "recess_cells_D_gt_0p6": int(((D > 0.6) & (rd < 3)).sum()), "recess_depth_max": float(np.nanmax(np.where(rd < 3, D, np.nan)))}
rec = (D > 0.6) & (rd < 3)
out["centre_screw"]["recess_extent_x"] = [float(X[rec].min() - cxs), float(X[rec].max() - cxs)]
out["centre_screw"]["recess_extent_y"] = [float(Y[rec].min() - cys), float(Y[rec].max() - cys)]
axs[2].imshow(np.clip(D, -0.3, 2.5), origin='lower', extent=[x0, -x0, x0, -x0], cmap='jet'); axs[2].set_xlim(-9, 3); axs[2].set_ylim(-6, 6); axs[2].minorticks_on(); axs[2].grid(which='both', alpha=.4)
plt.tight_layout(); plt.savefig('measure/figures/spouts_screw.png', dpi=45)
json.dump(out, open('measure/figures/spouts_screw.json', 'w'), indent=1)
print({k: {kk: vv for kk, vv in v.items() if kk != 'stations'} for k, v in out.items()})
for s in out["spout_0"]["stations"][::3]: print(s)
