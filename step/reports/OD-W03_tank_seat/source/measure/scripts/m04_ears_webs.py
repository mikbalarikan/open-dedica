"""m04_ears_webs.py - ear tab + lug, webs, barb-bore and boss-hole measurements (datum frame).
Estimators: medians of vertex coordinates in windows selected by face-normal direction; IRLS circle
fits on section points; open-boundary loop circles for holes. Writes measure/figures/m04_ears_webs.json."""
import json, sys, numpy as np, trimesh
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-intake-datum/scripts')
from datum_fit import fit_circle_irls, fit_circle
m = trimesh.load('intake/aligned_work.stl')
C, N = m.triangles_center, m.face_normals
def sel(xr=None, yr=None, zr=None, n=None, ncos=0.9):
    k = np.ones(len(C), bool)
    for i, rr in enumerate((xr, yr, zr)):
        if rr is not None: k &= (C[:, i] >= rr[0]) & (C[:, i] <= rr[1])
    if n is not None: k &= (N @ np.asarray(n, float)) > ncos
    return k
def med(k, i): return {"p50": float(np.median(C[k, i])), "p10": float(np.percentile(C[k, i], 10)), "p90": float(np.percentile(C[k, i], 90)), "n": int(k.sum())}
out = {"tool": "measure/scripts/m04_ears_webs.py"}
for s, nm in ((1, 'pos'), (-1, 'neg')):
    X = lambda a, b: (min(s*a, s*b), max(s*a, s*b))
    e = {}
    e['tab_outer_face_x'] = med(sel(X(33.6, 35.2), (-3.5, 3.5), (-2.5, 11), (s, 0, 0), 0.9), 0)
    # tab side faces: y at several z bands (taper)
    for zb in ((-2, 1), (2, 5), (6, 9), (10, 12.5)):
        e[f'tab_side_ypos_z{zb[0]}_{zb[1]}'] = med(sel(X(32.6, 34.2), (3, 6), zb, (0, 1, 0), 0.8), 1)
        e[f'tab_side_yneg_z{zb[0]}_{zb[1]}'] = med(sel(X(32.6, 34.2), (-6, -3), zb, (0, -1, 0), 0.8), 1)
    e['tab_inner_face_x'] = med(sel(X(31.8, 33.2), (-4.4, -1.4), (1, 12), (-s, 0, 0), 0.8), 0)
    e['tab_inner_face_x_ypos'] = med(sel(X(31.8, 33.2), (1.4, 4.4), (1, 12), (-s, 0, 0), 0.8), 0)
    e['lug_top_z'] = med(sel(X(34.5, 41.5), (-3.5, 3.5), (14, 16), (0, 0, 1), 0.9), 2)
    e['lug_side_ypos'] = med(sel(X(34.5, 38.5), (3, 5), (12.5, 14.8), (0, 1, 0), 0.8), 1)
    e['lug_side_yneg'] = med(sel(X(34.5, 38.5), (-5, -3), (12.5, 14.8), (0, -1, 0), 0.8), 1)
    e['lug_side_zmin'] = float(np.percentile(C[sel(X(34.5, 41), (-5, 5), (10, 15), None)][:, 2], 1))
    # hole and end arc from sections
    pts_h, pts_o = [], []
    for z in (13.6, 13.9, 14.2, 14.5):
        sec = m.section([0, 0, 1], [0, 0, z])
        P = np.vstack([sec.vertices[en.points] for en in sec.entities])[:, :2]
        q = P - [s*38.3, 0]; r = np.hypot(*q.T)
        pts_h.append(P[(r < 2.8) & (np.abs(P[:, 0]) > 35)])
        pts_o.append(P[(r > 3.0) & (r < 5.5) & (s*P[:, 0] > 39.0)])
    ph, po = np.vstack(pts_h), np.vstack(pts_o)
    e['lug_hole_fit'] = fit_circle_irls(ph, np.ones(len(ph)), scale=0.3)
    e['lug_end_arc_fit'] = fit_circle_irls(po, np.ones(len(po)), scale=0.3)
    e['lug_end_x_extreme_p99'] = float(np.percentile(s*C[sel(X(40, 44), (-2, 2), (12.5, 15.5))][:, 0], 99)) * s
    # web cup->tab: side faces y and top z
    e['web_tab_side_ypos'] = med(sel(X(31.0, 32.4), (0.4, 2.0), (5, 12), (0, 1, 0), 0.8), 1)
    e['web_tab_side_yneg'] = med(sel(X(31.0, 32.4), (-2.0, -0.4), (5, 12), (0, -1, 0), 0.8), 1)
    e['web_tab_top_z'] = med(sel(X(30.5, 32.3), (-0.8, 0.8), (11.5, 13), (0, 0, 1), 0.9), 2)
    # web cup->boss
    e['web_boss_side_ypos'] = med(sel(X(6.4, 7.6), (0.4, 2.0), (1, 11.5), (0, 1, 0), 0.8), 1)
    e['web_boss_side_yneg'] = med(sel(X(6.4, 7.6), (-2.0, -0.4), (1, 11.5), (0, -1, 0), 0.8), 1)
    e['web_boss_top_z'] = med(sel(X(6.3, 7.7), (-0.8, 0.8), (11.5, 13), (0, 0, 1), 0.9), 2)
    out[nm] = e
# holes from the open-boundary loops of the aligned mesh
from trimesh.grouping import group_rows
edges = m.edges_sorted; g = group_rows(edges, require_count=1); be = edges[g]
import networkx as nx
G = nx.Graph(); G.add_edges_from(be.tolist())
loops = []
for comp in nx.connected_components(G):
    v = m.vertices[list(comp)]
    loops.append(v)
holes = {}
for nm, (cx, zlo) in {'barbA': (-19.485, 26), 'barbB': (19.485, 26), 'boss': (0.0, 10)}.items():
    best = None
    for v in loops:
        c = v[:, :2].mean(0)
        if abs(c[0] - cx) < 1.5 and abs(c[1]) < 1.5 and v[:, 2].min() > zlo:
            f = fit_circle(v[:, :2], 'kasa')
            if best is None or len(v) > best['n_loop']:
                best = {**f, 'n_loop': int(len(v)), 'z_range': [float(v[:, 2].min()), float(v[:, 2].max())]}
    holes[nm] = best
out['hole_loops'] = holes
json.dump(out, open('measure/figures/m04_ears_webs.json', 'w'), indent=1)
def short(d):
    return {k: (round(v['p50'], 3) if isinstance(v, dict) and 'p50' in v else ({kk: round(vv, 3) for kk, vv in v.items() if isinstance(vv, float)} if isinstance(v, dict) else round(v, 3))) for k, v in d.items()}
for nm in ('pos', 'neg'): print(nm, json.dumps(short(out[nm])))
print(json.dumps(holes, indent=0))
