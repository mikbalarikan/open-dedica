#!/usr/bin/env python3
# run-local QA probe (report-only, not a gate, not a skill script). it3 version of
# _it2_SUPERSEDED/qa/attribution_probe.py: SAME categories and the SAME D1 / scan-hole (0.8 mm) / bore
# predicates and fixed tip axis, run on the it3 arrays only (the it2 numbers are read back from
# _it2_SUPERSEDED/qa/attribution_probe.json for the like-for-like comparison). Added for it3:
# scan->CAD attribution of Z4 (nearest B-rep face, sign from the face normal, tip-frame t/r, near a scan
# hole edge or not) to decide whether the Z4 scan->CAD p95 residual is geometry-shaped.
import json, sys
import numpy as np, trimesh
from scipy.spatial import cKDTree
from build123d import import_step
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import header, write_json

m = trimesh.load_mesh('input/scan.stl')
T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4']); Tr = np.array(json.load(open('qa/registration.json'))['T_refine'])
m.apply_transform(T); m.apply_transform(np.linalg.inv(Tr))
eu, ct = np.unique(np.sort(m.edges, axis=1), axis=0, return_counts=True)
bt = cKDTree(m.vertices[np.unique(eu[ct == 1])]); vt = cKDTree(m.vertices); SV = m.vertices
D1 = lambda Q: (Q[:, 0] >= 6.5) & (Q[:, 0] < 13) & (Q[:, 2] >= -15) & (Q[:, 2] < -1)
c = np.array([37.05, -10.69, -52.68]); ax = np.array([-0.184, -0.352, -0.918]); ax /= np.linalg.norm(ax)
def tr(P):
    v = P - c; a = v @ ax; return a, np.linalg.norm(v - np.outer(a, ax), axis=1)
radial = lambda P: tr(P)[1]
bore_it1 = lambda P: (P[:, 0] > 30) & (P[:, 2] < -46) & (radial(P) < 2.3)
bore_ext = lambda P: (P[:, 0] > 30) & (P[:, 2] < -39) & (radial(P) < 2.3)
Z4 = lambda P: (P[:, 0] >= 28) & (P[:, 0] < 50) & (P[:, 2] >= -59) & (P[:, 2] < -31)
def st(x):
    x = np.asarray(x)
    return dict(n=int(len(x)), p95=round(float(np.percentile(x, 95)), 3), max=round(float(x.max()), 3)) if len(x) else dict(n=0)
sol = import_step("build/OD-S02_steam-rod_datum.step").solids()[0]
V, F, L, desc = [], [], [], []
for i, f in enumerate(sol.faces()):
    vs, tt = f.tessellate(0.005, 0.05)
    o = len(V); V += [[v.X, v.Y, v.Z] for v in vs]; F += [[a + o, b + o, c_ + o] for a, b, c_ in tt]; L += [i] * len(tt)
    cc = f.center(); desc.append([str(f.geom_type).split('.')[-1], round(f.area, 4), cc.X, cc.Y, cc.Z])
FM = trimesh.Trimesh(np.array(V), np.array(F), process=False); L = np.array(L)
def nearest(P):
    fi = np.empty(len(P), int); sg = np.empty(len(P))
    for i in range(0, len(P), 3000):
        cp, _, tid = trimesh.proximity.closest_point(FM, P[i:i+3000])
        fi[i:i+3000] = L[tid]; sg[i:i+3000] = np.sign(np.einsum('ij,ij->i', P[i:i+3000] - cp, FM.face_normals[tid]))
    return fi, sg
# windows+bore faces introduced in it2 (it1->it2 diff), matched by signature on the it3 solid; it3-changed faces from qa/it2_it3_diff.json
d12 = json.load(open('_it2_SUPERSEDED/qa/it1_it2_diff.json'))['faces_only_it2']; d23 = json.load(open('qa/it2_it3_diff.json'))['faces_only_it3']
def match(dsc, lst): return any(dsc[0] == f[0].split('.')[-1] and abs(dsc[1] - f[1]) < 2e-3 and np.linalg.norm(np.array(dsc[2:5]) - np.array(f[2:5])) < 2e-3 for f in lst)
win_bore = np.array([match(dd, d12) for dd in desc]); it3chg = np.array([match(dd, d23) for dd in desc])
z = np.load('qa/dev_arrays.npz'); P = z['c2s_pts']; d = z['c2s_d']; S = z['s2c_pts']; ds = z['s2c_d']
_, iv = vt.query(P); nb = bt.query(SV[iv])[0] <= 0.8
o = {"n_faces_it3": len(desc), "n_win_bore_faces_matched_in_it3": int(win_bore.sum()), "n_it3_changed_faces_matched": int(it3chg.sum())}
o['c2s_all'] = st(d); o['c2s_minus_D1'] = st(d[~D1(P)]); o['c2s_minus_D1_holes'] = st(d[~D1(P) & ~nb])
o['c2s_minus_D1_holes_bore_it1pred'] = st(d[~D1(P) & ~nb & ~bore_it1(P)])
k = ~D1(P) & ~nb & ~bore_ext(P); o['c2s_minus_D1_holes_boreext'] = st(d[k])
o['bore_it1pred_pts'] = st(d[bore_it1(P)]); o['bore_ext_pts'] = st(d[bore_ext(P)]); o['near_hole_pts'] = st(d[nb])
z4 = Z4(P); fi, _ = nearest(P[z4]); dz = d[z4]; nbz = nb[z4]; wb = win_bore[fi]; c3 = it3chg[fi]
o['Z4_c2s'] = st(dz); o['Z4_c2s_on_windows_bore_faces'] = st(dz[wb]); o['Z4_c2s_on_other_faces'] = st(dz[~wb])
o['Z4_c2s_other_faces_not_near_hole'] = st(dz[~wb & ~nbz]); o['Z4_c2s_windows_bore_not_near_hole'] = st(dz[wb & ~nbz])
o['Z4_c2s_on_it3_changed_faces(neck)'] = st(dz[c3])
o['Z4_over0.8_total'] = int((dz > 0.8).sum()); o['Z4_over0.8_on_windows_bore_faces'] = int(((dz > 0.8) & wb).sum()); o['Z4_over0.8_near_hole'] = int(((dz > 0.8) & nbz).sum())
top = np.argsort(-d * k)[:12]; o['c2s_residual_top_after_D1_holes_bore'] = [[*P[i].round(2).tolist(), round(float(d[i]), 3)] for i in top]
# whole-part observable: what the gated set is made of is in deviation.json; here only the residual after the non-geometric categories
# ---- Z4 scan->CAD attribution
zs = Z4(S); PS = S[zs]; dS = ds[zs]; fS, sS = nearest(PS); tS, rS = tr(PS); nbS = bt.query(PS)[0] <= 0.8
o['Z4_s2c'] = st(dS); o['Z4_s2c_p95_exact'] = float(np.percentile(dS, 95))
o['Z4_s2c_not_near_hole'] = st(dS[~nbS]); o['Z4_s2c_near_hole(<=0.8 mm of a scan boundary edge)'] = st(dS[nbS])
o['Z4_s2c_p95_exact_not_near_hole'] = float(np.percentile(dS[~nbS], 95))
hi = dS > 0.3
grp = {}
for i in np.where(hi)[0]:
    dd = desc[fS[i]]; g = f"{fS[i]}:{dd[0]} area {round(dd[1], 3)} c {np.round(dd[2:5], 2).tolist()}{' [win/bore]' if win_bore[fS[i]] else ''}{' [it3 changed]' if it3chg[fS[i]] else ''}"
    e = grp.setdefault(g, {"n_over0.3": 0, "n_scan_outside_cad(-)": 0, "n_near_hole": 0, "t": [], "r": [], "d": []})
    e["n_over0.3"] += 1; e["n_scan_outside_cad(-)"] += int(sS[i] > 0); e["n_near_hole"] += int(nbS[i]); e["t"].append(tS[i]); e["r"].append(rS[i]); e["d"].append(dS[i])
tab = {}
for g, e in sorted(grp.items(), key=lambda t: -t[1]["n_over0.3"])[:15]:
    nf = int((fS == int(g.split(':')[0])).sum())
    tab[g] = {"n_over0.3": e["n_over0.3"], "n_face_pts": nf, "frac_over0.3": round(e["n_over0.3"] / max(nf, 1), 3),
              "frac_scan_outside_cad": round(e["n_scan_outside_cad(-)"] / e["n_over0.3"], 3), "frac_near_hole": round(e["n_near_hole"] / e["n_over0.3"], 3),
              "t_range": [round(min(e["t"]), 2), round(max(e["t"]), 2)], "r_range": [round(min(e["r"]), 2), round(max(e["r"]), 2)], "d_max": round(max(e["d"]), 3)}
o['Z4_s2c_over0.3_by_nearest_face (sign: outside = scan beyond the CAD surface, CAD too small there)'] = tab
o['Z4_s2c_n_over0.3'] = int(hi.sum()); o['Z4_s2c_n_over0.3_near_hole'] = int((hi & nbS).sum())
# what-if (report-only, NOT a gate): Z4 p95 if the points nearest each of the top-3 face groups read at the zone median
for g in list(tab)[:3]:
    fid = int(g.split(':')[0]); x = dS.copy(); x[fS == fid] = np.median(dS)
    o.setdefault('whatif_Z4_s2c_p95_if_face_group_at_median', {})[g] = round(float(np.percentile(x, 95)), 4)
write_json("qa/attribution_probe.json", {**header("attribution_probe", "qa/attribution_probe.py (run-local)",
    ["qa/dev_arrays.npz", "qa/registration.json", "build/OD-S02_steam-rod_datum.step", "_it2_SUPERSEDED/qa/it1_it2_diff.json", "qa/it2_it3_diff.json", "input/scan.stl"], None), "it3": o})
print(json.dumps(o, indent=1))
