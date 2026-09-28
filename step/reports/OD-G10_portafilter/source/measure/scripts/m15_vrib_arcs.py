"""it2 (verify it1 clusters 1/10: V-rib inner ends). The crest centreline (median xy of crest samples, z within
-0.35..+0.4 of the m08 top z, |u| < 4 of the m08 PCA line, per 0.5 mm bin along it) is straight over most of
the rib and turns at the inner end. Model: two straight segments, fitted by total least squares to the
centreline bins s < s_k - 0.5 and s > s_k + 0.5, with the knee s_k chosen by minimum total residual over
s_k in [4, s_end - 1.5]. Bins with s < t_min + 2.5 are dropped from segment 1: there the crest window also
catches the insert wall top (u spread > 3 mm); the outer end is the segment-1 point at s = t_min (the rib runs into
the wall there; the model extends it into the wall). Joint = intersection of the two lines; inner end = projection of the last bin on
segment 2; outer end = projection of the first bin on segment 1. Writes vrib_segments.json."""
import json, numpy as np, trimesh
m = trimesh.load('intake/aligned_work.stl'); P, _ = trimesh.sample.sample_surface(m, 3000000, seed=0)
rf = json.load(open('measure/figures/ribs_floor.json')); out = {}
def tls(pts):
    c = pts.mean(0); _, sv, vt = np.linalg.svd(pts - c); d = vt[0]; r = (pts - c) @ np.array([-d[1], d[0]])
    return c, d, r
for key in ('V_pos', 'V_neg'):
    V = rf[key]; c0 = np.array(V['centre']); d0 = np.array(V['dir']); n0 = np.array([-d0[1], d0[0]])
    q = P[:, :2] - c0; s = q @ d0; u = q @ n0
    top = (P[:, 2] > V['top_z'] - 0.35) & (P[:, 2] < V['top_z'] + 0.4) & (np.abs(u) < 4) & (s > V['t_min'] - 3) & (s < V['t_max'] + 3)
    S_, X_ = [], []
    for s0 in np.arange(V['t_min'] - 3, V['t_max'] + 3, 0.5):
        b = top & (s >= s0) & (s < s0 + 0.5)
        if b.sum() >= 20: S_.append(s0 + 0.25); X_.append(np.median(P[b, :2], axis=0))
    S_, X_ = np.array(S_), np.array(X_)
    best = None
    for sk in np.arange(4.0, S_[-1] - 1.5, 0.25):
        a, b = X_[(S_ < sk - 0.5) & (S_ > V['t_min'] + 2.5)], X_[S_ > sk + 0.5]
        if len(a) < 5 or len(b) < 3: continue
        ca, da, ra = tls(a); cb, db, rb = tls(b); tot = float((ra**2).sum() + (rb**2).sum())
        if best is None or tot < best[0]: best = (tot, sk, ca, da, ra, cb, db, rb)
    tot, sk, ca, da, ra, cb, db, rb = best
    M = np.c_[da, -db]; tt = np.linalg.solve(M, cb - ca); joint = ca + da * tt[0]
    inner = cb + db * ((X_[-1] - cb) @ db); outer = ca + da * ((c0 + d0 * V['t_min'] - ca) @ da)
    turn = float(np.degrees(np.arccos(abs(da @ db))))
    out[key] = {"knee_s": float(sk), "outer_end": outer.tolist(), "joint": joint.tolist(), "inner_end": inner.tolist(),
                "seg1_rms": float(np.sqrt((ra**2).mean())), "seg2_rms": float(np.sqrt((rb**2).mean())), "turn_deg": turn,
                "n_bins": [int(len(ra)), int(len(rb))]}
json.dump(out, open('measure/figures/vrib_segments.json', 'w'), indent=1); print(json.dumps(out, indent=1))
