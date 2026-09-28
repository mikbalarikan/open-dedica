"""Run-local QA helper (qa/ only): localise over-band CAD->scan points that survive masks M1-M5
and the scan->CAD >0.3/>0.8 points, from a deviation_gate --save-arrays npz. Uses QA's own STEP
tessellation (_common.step_to_mesh, same 0.005/0.05 as deviation_gate) and the same sampling seed
(c2s seed 2, 300k) so the per-point normals match. Report only; writes qa/<out>.json."""
import json, sys, tempfile
from pathlib import Path
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import step_to_mesh, select, load_mesh, load_matrix
import trimesh
from scipy.spatial import cKDTree
npz, regf, out = sys.argv[1], (sys.argv[2] if sys.argv[2] != "-" else None), sys.argv[3]
A = np.load(npz)
cad = step_to_mesh(Path("build/OD-G10_porta_filter_holder_datum.step"), Path(tempfile.mkdtemp()) / "c.stl")
cp, cfi = trimesh.sample.sample_surface(cad, 300_000, seed=2)
assert np.allclose(cp, A["c2s_pts"]), "sample mismatch"
cn = cad.face_normals[cfi]; d2 = A["c2s_d"]
masks = json.load(open("qa/masks.json"))["masks"]
inm = np.zeros(len(cp), bool)
for mk in masks:
    if mk["type"] == "region":
        inm |= select(mk["select"], cp, cn)
# open boundary (M5): boundary vertices of the aligned (and registered) scan vs the nearest scan point
s = load_mesh("input/scan.stl"); s.apply_transform(load_matrix("intake/alignment.json"))
if regf:
    s.apply_transform(np.linalg.inv(np.asarray(json.load(open(regf))["T_refine"])))
eu, ct = np.unique(np.sort(s.edges, axis=1), axis=0, return_counts=True)
bt = cKDTree(s.vertices[np.unique(eu[ct == 1])])
st = cKDTree(s.vertices)
_, iv = st.query(cp, workers=-1)
inm |= bt.query(s.vertices[iv], workers=-1)[0] <= 0.8   # approx: nearest scan VERTEX, not closest point
res = {"note": "M5 approximated with the nearest scan vertex (deviation_gate uses the closest point)",
       "c2s_kept": int((~inm).sum())}
def buckets(P, N, d, thr):
    sel = d > thr
    r = np.hypot(P[:, 0], P[:, 1]); th = (np.degrees(np.arctan2(P[:, 1], P[:, 0])) + 360) % 360
    rows = []
    for zlo, zhi in ((0.1, 9), (-3.5, 0.1), (-11, -3.5), (-14, -11), (-17.2, -14), (-20.3, -17.2), (-40, -20.3)):
        for rlo, rhi in ((0, 30.6), (30.6, 32.2), (32.2, 36.4), (36.4, 37.7), (37.7, 39.5), (39.5, 50)):
            m = sel & (P[:, 2] >= zlo) & (P[:, 2] < zhi) & (r >= rlo) & (r < rhi)
            if m.sum() >= 20:
                t = th[m]
                h = np.histogram(t, bins=72, range=(0, 360))[0]
                rows.append({"z": [zlo, zhi], "r": [rlo, rhi], "n": int(m.sum()), "d_p50": round(float(np.median(d[m])), 3),
                             "d_max": round(float(d[m].max()), 3),
                             "nz_mean": round(float(N[m, 2].mean()), 2) if N is not None else None,
                             "theta_bins_5deg": [i * 5 for i in np.nonzero(h >= 3)[0].tolist()]})
    return rows
k = ~inm
res["c2s_masked_over_0.8"] = buckets(cp[k], cn[k], d2[k], 0.8)
res["c2s_masked_over_0.3"] = buckets(cp[k], cn[k], d2[k], 0.3)
res["c2s_masked_n_over_0.3"] = int((d2[k] > 0.3).sum()); res["c2s_masked_n_over_0.8"] = int((d2[k] > 0.8).sum())
sp, d1 = A["s2c_pts"], A["s2c_d"]
res["s2c_over_0.8_points"] = [[round(float(v), 3) for v in list(p) + [np.hypot(p[0], p[1]), (np.degrees(np.arctan2(p[1], p[0])) + 360) % 360, dd]] for p, dd in zip(sp[d1 > 0.8], d1[d1 > 0.8])]
res["s2c_over_0.5"] = buckets(sp, None, d1, 0.5)
json.dump(res, open(out, "w"), indent=1)
print(json.dumps(res, indent=0)[:6000])
