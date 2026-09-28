#!/usr/bin/env python3
"""QA diagnostic (NOT a gate, NOT a mask): attribute the gated statistics' over-band points to regions.

Reads the arrays deviation_gate.py saved (--save-arrays), re-tessellates the same STEP with the same call,
re-runs observability.observable_split with the same parameters (seed 5, 20k, 0.5 mm, 60 deg; chunk 200 for
memory only) to recover the per-point observable mask, checks that it reproduces deviation.json's
cad_to_scan_observable stats exactly, then labels over-band points (> max band) with the same KD radius
graph as deviation_gate.over_band_clusters (eps 1.0, sizes sorted descending) and with named region
predicates (datum frame). Region predicates are descriptive buckets for the per-region miss table only;
no statistic here feeds gate.json's pass/fail.

usage: cluster_attrib.py <arrays.npz> <step> <deviation.json> <out.json>
"""
import json
import sys
import tempfile
from pathlib import Path

import numpy as np

S = "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts"
sys.path.insert(0, S)
from _common import header, stats, step_to_mesh, write_json  # noqa: E402
from observability import observable_split  # noqa: E402
from scipy.sparse import coo_matrix  # noqa: E402
from scipy.sparse.csgraph import connected_components  # noqa: E402
from scipy.spatial import cKDTree  # noqa: E402

arr_p, step, dev_p, out_p = sys.argv[1:5]
A = np.load(arr_p)
dev = json.load(open(dev_p))
THR = 0.8

# descriptive region buckets (datum frame); first match wins
REGIONS = [
    ("grip_strip_unscanned", lambda P, r, t: (P[:, 0] > 100) & (t > 3.5) & (t < 8.0)),
    ("spout_tips_heads", lambda P, r, t: P[:, 2] < -54.0),
    ("outlet_pockets_trough", lambda P, r, t: (r < 24.5) & (P[:, 2] < -38.5) & (P[:, 2] >= -54.0)
                                              & (((t > 10) & (t < 105)) | ((t > 250) & (t < 352)))),
    ("insert_centre_urib", lambda P, r, t: (r < 19.0) & (P[:, 2] < -26.0) & (P[:, 2] >= -54.0)),
    ("insert_wall_ring", lambda P, r, t: (r >= 19.0) & (r < 24.5) & (P[:, 2] < -26.0) & (P[:, 2] >= -54.0)),
    ("wire_bore_top", lambda P, r, t: (r < 29.0) & (P[:, 2] > -7.0)),
    ("lugs", lambda P, r, t: (r >= 30.5) & (r < 37.0) & (P[:, 2] > -7.5)),
    ("neck_pad", lambda P, r, t: (P[:, 0] >= 29.0) & (P[:, 0] < 50.0)),
    ("handle", lambda P, r, t: P[:, 0] >= 50.0),
]


def region_of(P):
    r = np.hypot(P[:, 0], P[:, 1]); t = (np.degrees(np.arctan2(P[:, 1], P[:, 0])) + 360) % 360
    lab = np.array(["other"] * len(P), dtype=object)
    free = np.ones(len(P), bool)
    for name, f in REGIONS:
        m = f(P, r, t) & free
        lab[m] = name; free &= ~m
    return lab


def cluster_labels(P, d):
    sel = np.where(d > THR)[0]
    lab_full = np.full(len(d), -1)
    if len(sel) == 0:
        return lab_full
    Q = P[sel]
    pairs = cKDTree(Q).query_pairs(1.0, output_type="ndarray")
    g = coo_matrix((np.ones(len(pairs)), (pairs[:, 0], pairs[:, 1])), shape=(len(Q), len(Q)))
    _, lab = connected_components(g, directed=False)
    ids, cnt = np.unique(lab, return_counts=True)
    order = np.lexsort((ids, -cnt))
    rank = {int(ids[o]): k if cnt[o] >= 20 else -2 for k, o in enumerate(order)}
    lab_full[sel] = [rank[int(x)] for x in lab]
    return lab_full


def breakdown(P, d, n_total):
    reg = region_of(P)
    out = {}
    for name in [n for n, _ in REGIONS] + ["other"]:
        m = reg == name
        if not m.any():
            continue
        dd = d[m]
        out[name] = {"n": int(m.sum()), "frac_of_set": float(m.sum() / n_total), "p95": float(np.percentile(dd, 95)),
                     "max": float(dd.max()), "n_over_max_band": int((dd > THR).sum()),
                     "share_of_over_band": float((dd > THR).sum() / max((d > THR).sum(), 1))}
    return out


res = {"threshold_mm": THR}
# scan -> CAD (all points, masked == unmasked: no scan-side mask)
sp, sd = A["s2c_pts"], A["s2c_d"]
res["scan_to_cad_by_region"] = breakdown(sp, sd, len(sd))
lab = cluster_labels(sp, sd)
res["scan_to_cad_over_band_by_cluster"] = {str(k): int((lab == k).sum()) for k in sorted(set(lab[lab >= 0]))}
res["scan_to_cad_over_band_in_small_clusters"] = int((lab == -2).sum())

# CAD -> scan observable subset
cp, cfi, cd = A["c2s_pts"], A["c2s_fid"], A["c2s_d"]
cad = step_to_mesh(step, Path(tempfile.mkdtemp()) / "t.stl")
ob = observable_split(cad, cp, cfi, cd, 20000, 5, 0.5, 60.0, chunk=200)
ref = dev["cad_to_scan_observable"]
res["observable_reproduced"] = {k: [ob["observable"][k], ref[k]] for k in ("n", "p95", "max")}
assert ob["observable"]["n"] == ref["n"] and abs(ob["observable"]["p95"] - ref["p95"]) < 1e-12, "not reproduced"
sub, om = ob["_sub"], ob["_obs_mask"]
op, od = cp[sub][om], cd[sub][om]
res["cad_to_scan_observable_by_region"] = breakdown(op, od, len(od))
clab = cluster_labels(cp, cd)[sub][om]
res["cad_to_scan_observable_over_band_by_full_cluster"] = {str(k): int((clab == k).sum())
                                                           for k in sorted(set(clab[clab >= 0]))}
res["cad_to_scan_observable_over_band_in_small_clusters"] = int((clab == -2).sum())
# top-5 observable maxima with their location
top = np.argsort(-od)[:8]
res["cad_to_scan_observable_top8"] = [{"d": float(od[i]), "xyz": op[i].round(2).tolist(),
                                       "region": str(region_of(op[i:i + 1])[0]), "full_cluster": int(clab[i])}
                                      for i in top]
write_json(out_p, {**header("cluster_attrib", "qa/scripts/cluster_attrib.py", [arr_p, step, dev_p], 5),
                   "note": "QA diagnostic, not a gate and not a mask: region buckets describe where the over-band "
                           "points are; gate.json pass/fail is unaffected.", **res})
print(json.dumps(res, indent=1))
