"""Run-local QA diagnostic (qa/ only, NOT a gate): at the datum pose, which CAD regions supply the
ICP correspondences that tier2_icp.py keeps (same filter: |n.n|>cos70, d<3.0, >0.8 mm off a scan
boundary), and which way they pull. Reduced sampling (1M scan / 100k CAD) for speed."""
import json, sys, math, tempfile
from pathlib import Path
import numpy as np, trimesh
from scipy.spatial import cKDTree
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import load_mesh, load_matrix, step_to_mesh, select
s = load_mesh("input/scan.stl", process=False); s.merge_vertices(); s.apply_transform(load_matrix("intake/alignment.json"))
eu, ct = np.unique(np.sort(s.edges, axis=1), axis=0, return_counts=True)
bt = cKDTree(s.vertices[np.unique(eu[ct == 1])])
sp, sf = trimesh.sample.sample_surface(s, 1_000_000, seed=11); sn = s.face_normals[sf]
c = step_to_mesh(Path("build/OD-G10_porta_filter_holder_datum.step"), Path(tempfile.mkdtemp()) / "c.stl")
cp, cf = trimesh.sample.sample_surface(c, 100_000, seed=13); cn = c.face_normals[cf]
d, i = cKDTree(sp).query(cp, workers=-1)
ok = (np.abs((cn * sn[i]).sum(1)) > math.cos(math.radians(70))) & (d < 3.0) & (bt.query(sp[i], workers=-1)[0] > 0.8)
masks = [m for m in json.load(open("qa/masks.json"))["masks"] if m["type"] == "region"]
out = {"kept_fraction": float(ok.mean()), "mean_d_kept": float(d[ok].mean()), "regions": {}}
anym = np.zeros(len(cp), bool)
for m in masks:
    r = select(m["select"], cp, cn); anym |= r
    k = ok & r
    v = (sp[i][k] - cp[k]).mean(0) if k.any() else np.zeros(3)
    out["regions"][m["name"]] = {"cad_frac": float(r.mean()), "kept_n": int(k.sum()), "share_of_kept": float(k.sum() / ok.sum()),
                                 "mean_d_kept": float(d[k].mean()) if k.any() else None,
                                 "antiparallel_normals_frac": float(((cn[k] * sn[i][k]).sum(1) < 0).mean()) if k.any() else None,
                                 "mean_pull_vec_mm": v.round(3).tolist()}
k = ok & ~anym
out["regions"]["scanned (outside M1-M4)"] = {"kept_n": int(k.sum()), "share_of_kept": float(k.sum() / ok.sum()),
    "mean_d_kept": float(d[k].mean()), "mean_pull_vec_mm": (sp[i][k] - cp[k]).mean(0).round(3).tolist()}
json.dump(out, open("qa/icp_diagnose.json", "w"), indent=1); print(json.dumps(out, indent=1))
