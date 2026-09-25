"""Two-way CAD-vs-scan deviation gate (datum frame). Fast: KD-tree on dense
samples + exact point-triangle distance on k nearest candidate triangles."""
import json, sys
import numpy as np, trimesh
from scipy.spatial import cKDTree
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

def dist_to_mesh(pts, mesh, k=8, n_samp=3_000_000, seed=0):
    samp, fi = trimesh.sample.sample_surface(mesh, n_samp, seed=seed)
    tree = cKDTree(samp)
    _, idx = tree.query(pts, k=k)
    cand = fi[idx]                       # (n,k) triangle ids
    tri = mesh.triangles[cand.reshape(-1)]
    P = np.repeat(pts, k, axis=0)
    cp = trimesh.triangles.closest_point(tri, P)
    d = np.linalg.norm(cp - P, axis=1).reshape(-1, k).min(1)
    return d

def stats(d):
    return dict(rms=float(np.sqrt((d**2).mean())), p95=float(np.percentile(d, 95)), p99=float(np.percentile(d, 99)), max=float(d.max()), mean=float(d.mean()), n=int(len(d)))

scan = trimesh.load_mesh(sys.argv[1]); scan.apply_transform(np.load(sys.argv[2]))
cad = trimesh.load_mesh(sys.argv[3])
out = sys.argv[4]
sv = scan.vertices
d1 = dist_to_mesh(sv, cad)
cp, cfi = trimesh.sample.sample_surface(cad, 300_000, seed=2)
d2 = dist_to_mesh(cp, scan)
res = {"scan_to_cad": stats(d1), "cad_to_scan": stats(d2)}
# regions by z along axis
regions = {"outlet_tube z<-24.5": sv[:,2] < -24.5, "front_body -24.5..-9.6": (sv[:,2] >= -24.5) & (sv[:,2] < -9.6),
           "coil+frame -9.6..37.7": (sv[:,2] >= -9.6) & (sv[:,2] < 37.7), "inlet z>=37.7": sv[:,2] >= 37.7}
res["scan_to_cad_regions"] = {k: stats(d1[m]) for k, m in regions.items()}
cz = cp[:,2]
regs2 = {"outlet_tube z<-24.5": cz < -24.5, "front_body -24.5..-9.6": (cz >= -24.5) & (cz < -9.6),
         "coil+frame -9.6..37.7": (cz >= -9.6) & (cz < 37.7), "inlet z>=37.7": cz >= 37.7}
res["cad_to_scan_regions"] = {k: stats(d2[m]) for k, m in regs2.items()}
json.dump(res, open(out + "_gate.json", "w"), indent=2)
for k in ("scan_to_cad", "cad_to_scan"):
    s = res[k]; print(flush=True); print("%-12s RMS %.3f p95 %.3f p99 %.3f max %.3f" % (k, s["rms"], s["p95"], s["p99"], s["max"]))
for grp in ("scan_to_cad_regions", "cad_to_scan_regions"):
    for k, s in res[grp].items(): print("  %s %-26s p95 %.3f max %.3f n %d" % (grp[:4], k, s["p95"], s["max"], s["n"]))
np.save(out + "_d1.npy", d1); np.save(out + "_cadpts.npy", np.c_[cp, d2])
# overlay: scan points colored by deviation, 4 views
fig, axs = plt.subplots(1, 4, figsize=(28, 12))
views = [((0, 2), "XZ (from -Y)"), ((1, 2), "YZ (from +X)"), ((0, 1), "XY (from +Z)")]
sel = np.random.default_rng(0).choice(len(sv), 250000, replace=False)
for ax, (ij, t) in zip(axs[:3], views):
    o = np.argsort(d1[sel])
    sc = ax.scatter(sv[sel][o, ij[0]], sv[sel][o, ij[1]], c=d1[sel][o], s=0.3, cmap="turbo", vmin=0, vmax=1.0)
    ax.set_aspect("equal"); ax.set_title("scan->CAD " + t); ax.grid(alpha=.3)
o = np.argsort(d2)
axs[3].scatter(cp[o, 0], cp[o, 2], c=d2[o], s=0.3, cmap="turbo", vmin=0, vmax=1.0); axs[3].set_aspect("equal"); axs[3].set_title("CAD->scan XZ")
fig.colorbar(sc, ax=axs, shrink=0.6, label="mm")
plt.savefig(out + "_dev.png", dpi=60)

# ---- observability of CAD->scan outliers (line-of-sight test on the CAD itself)
# A CAD point far from the scan is "unobservable" when every ray in a 60deg cone
# about its outward normal hits the CAD again within 60 mm (gap between frame plate
# and coil, bore interiors, flange pocket): no scanner could have recorded it.
import time
rng = np.random.default_rng(5)
sub = rng.choice(len(cp), 20000, replace=False)
far = sub[d2[sub] > 0.5]
nrm = cad.face_normals[cfi[far]]
a = np.cross(nrm, [0.3, 0.5, 0.8]); a /= np.linalg.norm(a, axis=1)[:, None]; b = np.cross(nrm, a)
dirs = [nrm] + [np.cos(np.radians(60))*nrm + np.sin(np.radians(60))*(np.cos(t)*a + np.sin(t)*b) for t in np.linspace(0, 2*np.pi, 6, endpoint=False)]
t0 = time.time()
hit_all = np.ones(len(far), bool)
from trimesh.ray.ray_triangle import RayMeshIntersector
rmi = RayMeshIntersector(cad)
for D in dirs:
    for c0 in range(0, len(far), 2000):
        sl = slice(c0, c0 + 2000)
        todo = np.where(hit_all[sl])[0]
        if len(todo) == 0: continue
        O = cp[far][sl][todo] + 0.05*nrm[sl][todo]
        h = rmi.intersects_any(O, D[sl][todo])
        idx = np.arange(len(far))[sl][todo]
        hit_all[idx[~h]] = False
unobs = far[hit_all]
obs_mask = ~np.isin(sub, unobs)
res["cad_to_scan_observable"] = stats(d2[sub][obs_mask])
res["cad_to_scan_unobservable_fraction"] = float(1 - obs_mask.mean())
json.dump(res, open(out + "_gate.json", "w"), indent=2)
s = res["cad_to_scan_observable"]
print("cad_to_scan (observable only, n=%d) RMS %.3f p95 %.3f p99 %.3f max %.3f | unobservable %.1f%%  [%.0fs]" % (s["n"], s["rms"], s["p95"], s["p99"], s["max"], 100*res["cad_to_scan_unobservable_fraction"], time.time()-t0), flush=True)
np.save(out + "_obs.npy", np.c_[cp[sub], d2[sub], obs_mask])
