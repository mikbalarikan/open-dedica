"""Handle / neck circle stations: sections x = const of the aligned scan, Kasa + IRLS circle
on the largest loop (or open arcs), centre (y,z) and radius vs x. Writes measure/figures/handle_stations.json."""
import json, sys, numpy as np, trimesh
sys.path.insert(0, sys.argv[1])  # stl-re-intake-datum/scripts (fit_circle)
from datum_fit import fit_circle
m = trimesh.load('intake/aligned_work.stl')
out = []
for x in np.arange(41.0, 166.0, 1.0):
    L = trimesh.intersections.mesh_plane(m, [1, 0, 0], [x, 0, 0])
    if len(L) == 0: continue
    pts = L.reshape(-1, 3)[:, 1:]
    pts = pts[(np.abs(pts[:, 0]) < 25) & (pts[:, 1] < -5) & (pts[:, 1] > -60)]
    if len(pts) < 30: continue
    c = fit_circle(pts, 'irls', 0.30)
    k = fit_circle(pts, 'kasa')
    out.append({"x": float(x), "cy": c["cx"], "cz": c["cy"], "r": c["r"], "rms": c["rms"], "max": c["max"],
                "r_kasa": k["r"], "n": int(len(pts))})
json.dump({"stations": out}, open('measure/figures/handle_stations.json', 'w'), indent=1)
for s in out[::3]: print(f'{s["x"]:6.1f} cy {s["cy"]:7.3f} cz {s["cz"]:8.3f} r {s["r"]:7.3f} rms {s["rms"]:.3f} max {s["max"]:.3f}')
