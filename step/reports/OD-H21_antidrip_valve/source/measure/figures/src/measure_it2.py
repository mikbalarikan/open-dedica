"""measure_it2.py - it2 (REVISE, route geometry) re-measurement of the three features the independent
verifier named (qa gate dd052135f7c2, _it1_SUPERSEDED/qa/gate.json#miss_explanations):
  1. nozzle latch windows (E04/E23)   2. ring windows (E17)   3. skirt slits (E21)
Nothing else is re-measured. Writes measure/figures/fits_it2.json. Deterministic."""
from __future__ import annotations
import json
import numpy as np, networkx as nx
from trimesh.grouping import group_rows
from mlib import *

F = json.loads((RUN / 'measure/figures/fits.json').read_text())
out = {"inputs": {"intake/aligned_work.stl": sha(RUN / 'intake/aligned_work.stl'), "measure/figures/fits.json": sha(RUN / 'measure/figures/fits.json')},
       "note": "it2 re-measurement; it1 values stay in _it1_SUPERSEDED/measure"}
m = mesh()

# ---------------------------------------------------------------- 1. nozzle latch windows (nozzle local frame)
ax = F['axes']['nozzle']; Vn = local_verts(ax['p'], ax['d']); rn = np.hypot(Vn[:, 0], Vn[:, 1]); tn = np.degrees(np.arctan2(Vn[:, 1], Vn[:, 0]))
lg = F['lip']; Rn = F['segments']['nozzle']['R']
def rect_sdf(P, x):
    cx, cy, a, b, rc, phi = x
    c, s_ = np.cos(np.radians(-phi)), np.sin(np.radians(-phi)); Q = np.abs((P - [cx, cy]) @ np.array([[c, -s_], [s_, c]]).T)
    qq = Q - np.array([a - rc, b - rc]); return np.hypot(np.maximum(qq[:, 0], 0), np.maximum(qq[:, 1], 0)) + np.minimum(np.maximum(qq[:, 0], qq[:, 1]), 0) - rc
def outline_r(t):
    ds = np.linspace(0, 9, 1801); P = np.c_[np.cos(np.radians(t)) * ds, np.sin(np.radians(t)) * ds]
    return ds[np.where((rect_sdf(P, [lg['cx'], lg['cy'], lg['half_a'], lg['half_b'], lg['corner_r'], lg['phi_deg']]) <= 0) | (ds <= Rn))[0].max()]
lat = []
for c0 in (lg['phi_deg'] + 90.0, lg['phi_deg'] - 90.0):
    dd = ((tn - c0 + 180) % 360) - 180
    band = (Vn[:, 2] > -25.2) & (Vn[:, 2] < -24.65) & (np.abs(dd) < 60)
    rows = []
    for x in np.arange(-60, 60, 1.0):
        t = band & (dd >= x) & (dd < x + 1)
        if t.sum() < 2:
            continue
        env = float(rn[t].max()); o = float(outline_r(x + 0.5 + c0))
        rows.append(dict(dtheta=x + 0.5, env=env, outline=o, deficit=o - env, min_rho=float(rn[t].min()),
                         wall_present=bool((rn[t] > Rn - 0.25).any())))
    dfc = np.array([r['deficit'] for r in rows]); th = np.array([r['dtheta'] for r in rows])
    cut = np.where(dfc > 0.25)[0]
    lo_b, hi_b = th[cut].min(), th[cut].max()                  # outermost bins cut back > 0.25 below the lug outline
    # the cut-back floor is a PLANE parallel to the lug b-side flat: x' = env cos(dtheta) is constant (d)
    wall_cut = [r for r in rows if r['wall_present'] and r['deficit'] > 0.25 and lo_b + 3 <= r['dtheta'] <= hi_b - 3]
    xs = np.array([r['env'] * np.cos(np.radians(r['dtheta'])) for r in wall_cut])
    d_plane = float(np.median(xs))
    rec = dict(side_theta_deg=float(c0), cut_dtheta=[float(lo_b - 0.5), float(hi_b + 0.5)],
               cut_plane_d=d_plane, cut_plane_d_p10_p90=np.percentile(xs, [10, 90]).tolist(), n_bins=len(xs),
               cut_half_width=[float(d_plane * np.tan(np.radians(lo_b - 0.5))), float(d_plane * np.tan(np.radians(hi_b + 0.5)))],
               method='1-deg bins of the outer envelope, u -25.2..-24.65, vs the fitted lug outline; cut-back = bins > 0.25 mm inside it; '
                      'its floor is a plane parallel to the b-side flat at distance d = median(env * cos(dtheta)) over wall bins 3 deg inside the cut edges; '
                      'lateral extent y\' = d tan(edge dtheta)')
    holes = [r['dtheta'] for r in rows if (not r['wall_present']) and lo_b <= r['dtheta'] <= hi_b]
    if len(holes) >= 3:
        span = [float(min(holes) - 0.5 + c0), float(max(holes) + 0.5 + c0)]
        sel = (dd + c0 >= span[0]) & (dd + c0 <= span[1]) & (rn < Rn - 0.25) & (Vn[:, 2] > -25.8) & (Vn[:, 2] < -23.9) & (rn > 3.99)
        rec.update(through_theta=span, through_bins=len(holes), through_u_p3_p97=np.percentile(Vn[sel, 2], [3, 97]).tolist(),
                   bridge_rho_p10_p50=np.percentile(rn[sel], [10, 50]).tolist(),
                   through_method='first..last 1-deg bin inside the cut-back with no nozzle-wall vertex (rho > noz_R - 0.25): window open through the wall (bore wall / bridge seen)')
    rec['bins'] = rows
    lat.append(rec)
out['latch_windows'] = lat

# ---------------------------------------------------------------- 2. ring windows (cap local frame, occupancy of the outer skirt surface)
axc = F['axes']['cap_part']; Vc = local_verts(axc['p'], axc['d']); rc = np.hypot(Vc[:, 0], Vc[:, 1]); tc = np.degrees(np.arctan2(Vc[:, 1], Vc[:, 0]))
tcw = np.where(tc < -150, tc + 360, tc); Rr = F['segments']['cap_part']['R_ring']
W = []
for wd in F['ring_windows']:
    c = wd['theta_c'] if wd['theta_c'] >= -150 else wd['theta_c'] + 360
    ths = np.arange(c - 14, c + 14, 1.0); us = np.arange(11.6, 15.4, 0.2)
    s = (np.abs(tcw - c) < 16) & (Vc[:, 2] > 11.4) & (Vc[:, 2] < 15.6)
    ti = np.floor((tcw[s] - ths[0]) / 1.0).astype(int); ui = np.floor((Vc[s, 2] - us[0]) / 0.2).astype(int)
    ok = (ti >= 0) & (ti < len(ths)) & (ui >= 0) & (ui < len(us))
    occ = np.zeros((len(us), len(ths)), int); outer = np.zeros_like(occ); minr = np.full(occ.shape, np.inf)
    np.add.at(occ, (ui[ok], ti[ok]), 1); np.add.at(outer, (ui[ok], ti[ok]), (rc[s][ok] > Rr - 0.35).astype(int))
    np.minimum.at(minr, (ui[ok], ti[ok]), rc[s][ok])
    opn = outer == 0                                   # no outer-skirt vertex in the cell = window (empty cells inside a window are scan holes, L2/L4)
    core_u = (us > 12.7) & (us < 13.9)
    colfrac = opn[core_u].mean(0); cols = np.where(colfrac >= 0.5)[0]
    runs = np.split(cols, np.where(np.diff(cols) > 1)[0] + 1); cr = max(runs, key=len)
    t0, t1 = ths[cr[0]], ths[cr[-1]] + 1.0
    rowfrac = opn[:, cr[0]:cr[-1] + 1].mean(1); rws = np.where(rowfrac >= 0.5)[0]
    runs = np.split(rws, np.where(np.diff(rws) > 1)[0] + 1); rr_ = max(runs, key=len)
    u0, u1 = us[rr_[0]], us[rr_[-1]] + 0.2
    inner = opn[rr_[0]:rr_[-1] + 1, cr[0]:cr[-1] + 1]; MR = minr[rr_[0]:rr_[-1] + 1, cr[0]:cr[-1] + 1]
    mr = MR[inner & np.isfinite(MR)]
    floor = float(np.median(mr[mr >= 11.0]))           # shallow floor: the latch hook / skirt inner wall seen through the window
    deepc = inner & np.isfinite(MR) & (MR < 11.0)       # cells opening into the skirt/body gap
    rec_w = dict(theta0=float(((t0 + 180) % 360) - 180), theta1=float(((t1 + 180) % 360) - 180), u_lo=float(u0), u_hi=float(u1),
                 floor_rho=floor, deep_cells=int(deepc.sum()), open_cells=int(inner.sum()))
    if deepc.sum() >= 6:
        ii, jj = np.where(deepc)
        rec_w.update(deep_theta=[float(((ths[cr[0] + jj.min()] + 180) % 360) - 180), float(((ths[cr[0] + jj.max()] + 1.0 + 180) % 360) - 180)],
                     deep_u=[float(us[rr_[0] + ii.min()]), float(us[rr_[0] + ii.max()] + 0.2)], deep_floor_rho=float(np.percentile(MR[deepc], 10)))
    W.append(dict(rec_w, floor_rule='median of the per-cell minimum radius over window cells >= r 11.0; cells < r 11.0 (>= 6) form a deeper through-window to their p10 radius',
                  method='cap frame, 1 deg x 0.2 mm cells; open = scanned cell with no outer-skirt vertex (rho > ring_R - 0.35); theta span = columns open in >= 50 % of rows u 12.7..13.9; u span = rows open in >= 50 % of those columns'))
out['ring_windows'] = W

# ---------------------------------------------------------------- 3. skirt slits = open boundary loops L5 / L7 in the cap frame
e = m.edges_sorted; be = e[group_rows(e, require_count=1)]
G = nx.Graph(); G.add_edges_from(be.tolist())
p, R = frame(axc['p'], axc['d']); SL = []
for comp in nx.connected_components(G):
    idx = np.array(sorted(comp)); Vd = m.vertices[idx]; r = np.hypot(Vd[:, 0], Vd[:, 1])
    if not ((r.min() > 9.5) & (r.max() < 11.6) & (Vd[:, 2].min() > 8)):
        continue
    L = to_local(Vd, p, R); rl = np.hypot(L[:, 0], L[:, 1]); tl = np.degrees(np.arctan2(L[:, 1], L[:, 0]))
    SL.append(dict(theta0=float(tl.min()), theta1=float(tl.max()), u_top=float(L[:, 2].max()), u_min=float(L[:, 2].min()),
                   rho_in=float(rl.min()), rho_out=float(rl.max()), n=int(len(idx)),
                   datum_theta=[float(np.degrees(np.arctan2(Vd[:, 1], Vd[:, 0])).min()), float(np.degrees(np.arctan2(Vd[:, 1], Vd[:, 0])).max())],
                   method='open-boundary loop (intake/coverage.json L5/L7) vertices in the cap frame: the scanned edge of each slit'))
SL.sort(key=lambda d: d['theta0'])
# The open loops mark only the hole in each slit's scanned surface; the scanned slit ceiling (vertices inside
# the skirt, rho 10.0..11.8) extends beyond the loop. Slit extent = 1-deg bins whose highest vertex is more than
# halfway from the ring-bottom groove level to the ceiling (ring bottom + 0.9), contiguous around each loop.
ub = F['levels']['ring_bottom']['u_median']
inside = (rc > 10.0) & (rc < 11.8) & (Vc[:, 2] > ub + 0.2) & (Vc[:, 2] < 12.5)
for s_ in SL:
    c = 0.5 * (s_['theta0'] + s_['theta1'])
    bins = []
    for t in np.arange(c - 25, c + 25, 1.0):
        d_ = ((tc - t + 180) % 360) - 180
        b = inside & (d_ >= 0) & (d_ < 1.0)
        bins.append((t, float(Vc[b, 2].max()) if b.sum() else -np.inf))
    bins = np.array(bins); hi = bins[:, 1] >= ub + 0.9
    k = int(np.argmin(np.abs(bins[:, 0] - c)))
    while not hi[k]: k += 1 if bins[k, 0] < c + 12 else -1
    i0 = i1 = k
    while i0 > 0 and hi[i0 - 1]: i0 -= 1
    while i1 < len(hi) - 1 and hi[i1 + 1]: i1 += 1
    t0, t1 = bins[i0, 0], bins[i1, 0] + 1.0
    d0 = ((tc - t0 + 180) % 360) - 180
    pts = inside & (d0 >= 0) & (d0 < t1 - t0) & (Vc[:, 2] > ub + 0.9)
    s_.update(ceiling_theta0=float(t0), ceiling_theta1=float(t1), ceiling_u=float(np.median(bins[i0:i1 + 1, 1])),
              ceiling_rho_p2_p95=np.percentile(rc[pts], [2, 95]).tolist(), ceiling_n=int(pts.sum()),
              ceiling_method='1-deg bins of the highest scan vertex inside the skirt (rho 10.0..11.8); slit = contiguous bins above ring_bottom_u + 0.9 around the loop; ceiling = median of those maxima; radial span = p2..p95 of the vertices above ring_bottom_u + 0.9')
out['skirt_slits'] = SL
(RUN / 'measure/figures/fits_it2.json').write_text(json.dumps(out, indent=1, default=float))
for r in lat: print({k: v for k, v in r.items() if k != 'bins'})
for w in W: print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in w.items() if k not in ('method', 'floor_rule')})
for s_ in SL: print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in s_.items() if k != 'method'})
