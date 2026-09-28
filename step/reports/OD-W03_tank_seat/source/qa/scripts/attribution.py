"""QA-only ATTRIBUTION (not a mask, not a gate): scan->CAD masked p95 recomputed with one region left
out at a time, to show which region carries the p95 miss. Masks = qa/masks.json M1+M2 (scan side)."""
import sys, json, numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import select
z = np.load("qa/dev_arrays.npz"); P, d = z["s2c_pts"], z["s2c_d"]
masks = [m for m in json.load(open("qa/masks.json"))["masks"] if m["type"] == "region" and m["applies_to"] == "scan"]
M = np.zeros(len(P), bool)
for m in masks: M |= select(m["select"], P)
base = d[~M]
print(f"masked p95 {np.percentile(base,95):.4f}  n {len(base)}  frac>0.30 {np.mean(base>0.3):.4f}")
regs = {"skirt z<-1.5": {"z": [None, -1.5]},
        "tab/lug x>=32 z>=11": {"abs_x": [32, None], "z": [11, None]},
        "tabs x>=32 z<11": {"abs_x": [32, None], "z": [None, 11]},
        "cup B upper wall z9.5-11.8": {"x": [7, 32], "abs_y": [1.5, None], "z": [9.5, 11.8]},
        "cup walls both (z0.3-11.8)": {"abs_x": [7, 32], "abs_y": [1.5, None], "z": [0.3, 11.8]},
        "barbs z>=16": {"abs_x": [15, 24], "z": [16, None]},
        "webs |y|<1.2": {"abs_y": [None, 1.2], "z": [0.3, None]}}
out = {}
for k, pr in regs.items():
    r = select(pr, P) & ~M
    s = d[~M & ~r]
    out[k] = {"n_region": int(r.sum()), "p95_without_region": float(np.percentile(s, 95)), "over_0.30_in_region": int((d[r] > 0.3).sum())}
    print(f"without {k:28s} n_reg {r.sum():6d} over0.3 {out[k]['over_0.30_in_region']:6d} p95 {out[k]['p95_without_region']:.4f}")
json.dump({"note": "attribution only, not a mask and not a gate", "masked_p95": float(np.percentile(base, 95)), "leave_region_out": out}, open("qa/scripts/attribution.json", "w"), indent=1)
