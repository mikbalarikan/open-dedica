#!/usr/bin/env python3
# run-local QA probe (report-only, not a gate, not a skill script): WHERE and in WHICH SIGN do the
# zone p95 misses Z2 (tube), Z3 (paddle) and Z4 scan->CAD sit? Signed scan->CAD distance
# (trimesh signed_distance: + = scan point inside the CAD solid = CAD too big there; - = scan outside
# the CAD = CAD too small) on the QA-registered scan points from qa/dev_arrays.npz, against QA's own
# tessellation of the it3 datum STEP (it3 copy of _it2_SUPERSEDED/qa/zone_probe.py, same bins and the same fixed tip axis) (0.005/0.05, as step_to_mesh). Decides whether the misses are
# geometry-shaped (coherent sign/offset) or noise/form-shaped.
import json, sys
import numpy as np, trimesh
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import header, write_json, step_to_mesh
cad = step_to_mesh("build/OD-S02_steam-rod_datum.step", "qa/_work/it3_datum_qa_tess.stl")
z = np.load("qa/dev_arrays.npz"); S = z["s2c_pts"]; ds = z["s2c_d"]
def st(x):
    x = np.asarray(x)
    if not len(x): return {"n": 0}
    return {"n": int(len(x)), "p50": round(float(np.percentile(np.abs(x), 50)), 3), "p95": round(float(np.percentile(np.abs(x), 95)), 3),
            "mean_signed": round(float(np.mean(x)), 3), "frac_inside_cad": round(float((x > 0).mean()), 3)}
def signed(P):
    out = np.empty(len(P))
    for i in range(0, len(P), 2000):  # it3: chunk 20000 -> 2000 (OOM on the finer it3 tessellation; results unchanged by chunking)
        out[i:i+2000] = trimesh.proximity.signed_distance(cad, P[i:i+2000])
    return out
res = {}
# ---- Z2 steel tube (x 23.5..50, z -31..-5): bins along x for B+bend, along z for C
m = (S[:, 0] >= 23.5) & (S[:, 0] < 50) & (S[:, 2] >= -31) & (S[:, 2] < -5)
P = S[m]; sd = signed(P); res["Z2_all"] = st(sd)
bins = {}
for lo in range(23, 42, 2):
    k = (P[:, 0] >= lo) & (P[:, 0] < lo + 2) & (P[:, 2] > -14)
    if k.sum() > 200: bins[f"x {lo}..{lo+2}, z>-14"] = st(sd[k])
for lo in range(-31, -13, 3):
    k = (P[:, 2] >= lo) & (P[:, 2] < lo + 3) & (P[:, 0] > 33)
    if k.sum() > 200: bins[f"z {lo}..{lo+3}, x>33 (tube C)"] = st(sd[k])
res["Z2_bins"] = bins
# ---- Z3 paddle (x -22.5..-9.5, z -28..-3): by scan-point side (datum y relative to the paddle mid-plane) and by x
m = (S[:, 0] >= -22.5) & (S[:, 0] < -9.5) & (S[:, 2] >= -28) & (S[:, 2] < -3)
P = S[m]; sd = signed(P); res["Z3_all"] = st(sd)
# local face normal from the CAD at the closest point
cp, _, tid = trimesh.proximity.closest_point(cad, P); n = cad.face_normals[tid]
side = {"+Y face (|ny|>0.8, ny>0)": n[:, 1] > 0.8, "-Y face (ny<-0.8)": n[:, 1] < -0.8, "perimeter/rounds (|ny|<=0.8)": np.abs(n[:, 1]) <= 0.8}
res["Z3_by_cad_face_side"] = {k: st(sd[v]) for k, v in side.items()}
res["Z3_by_x"] = {f"x {lo}..{lo+2}": st(sd[(P[:, 0] >= lo) & (P[:, 0] < lo + 2)]) for lo in range(-23, -9, 2) if ((P[:, 0] >= lo) & (P[:, 0] < lo + 2)).sum() > 200}
res["Z3_face_side_by_x"] = {k: {f"x {lo}..{lo+3}": st(sd[v & (P[:, 0] >= lo) & (P[:, 0] < lo + 3)]) for lo in range(-23, -9, 3) if (v & (P[:, 0] >= lo) & (P[:, 0] < lo + 3)).sum() > 100} for k, v in side.items() if k != "perimeter/rounds (|ny|<=0.8)"}
# ---- Z4 scan->CAD (x 28..50, z -59..-31)
m = (S[:, 0] >= 28) & (S[:, 0] < 50) & (S[:, 2] >= -59) & (S[:, 2] < -31)
P = S[m]; sd = signed(P); res["Z4_s2c_all"] = st(sd)
res["Z4_s2c_by_z"] = {f"z {lo}..{lo+4}": st(sd[(P[:, 2] >= lo) & (P[:, 2] < lo + 4)]) for lo in range(-59, -31, 4) if ((P[:, 2] >= lo) & (P[:, 2] < lo + 4)).sum() > 200}
write_json("qa/zone_probe.json", {**header("zone_probe", "qa/zone_probe.py (run-local)", ["qa/dev_arrays.npz", "build/OD-S02_steam-rod_datum.step"], None), **res})
print(json.dumps(res, indent=1))
# ---- Z4 scan->CAD >0.3 mm points, located in the bushing/tip frame (axis = the it1 attribution-probe tip axis)
c = np.array([37.05, -10.69, -52.68]); ax = np.array([-0.184, -0.352, -0.918]); ax /= np.linalg.norm(ax)
v = P - c; t = v @ ax; r = np.linalg.norm(v - np.outer(t, ax), axis=1)
hi = np.abs(sd) > 0.3
tb, rb = np.arange(-16, 18, 2), [0, 2.5, 3.5, 5, 7.5, 9.5, 30]
tab = []
for i in range(len(tb) - 1):
    for j in range(len(rb) - 1):
        k = (t >= tb[i]) & (t < tb[i+1]) & (r >= rb[j]) & (r < rb[j+1])
        if k.sum() >= 150 and (hi & k).sum() >= 30:
            tab.append({"axial_t": [int(tb[i]), int(tb[i+1])], "r": [rb[j], rb[j+1]], "n": int(k.sum()), "n_over0.3": int((hi & k).sum()),
                        "frac_over0.3": round(float((hi & k).sum() / k.sum()), 3), "mean_signed": round(float(sd[k].mean()), 3), "p95": round(float(np.percentile(np.abs(sd[k]), 95)), 3)})
res["Z4_s2c_over0.3_cells(t along tip axis from tip-end side negative, r from tip axis)"] = sorted(tab, key=lambda e: -e["n_over0.3"])[:12]
write_json("qa/zone_probe.json", {**header("zone_probe", "qa/zone_probe.py (run-local)", ["qa/dev_arrays.npz", "build/OD-S02_steam-rod_datum.step"], None), **res})
print(json.dumps(res["Z4_s2c_over0.3_cells(t along tip axis from tip-end side negative, r from tip axis)"], indent=0))
