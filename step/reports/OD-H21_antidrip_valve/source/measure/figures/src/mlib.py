"""mlib.py - run-local measurement helpers for OD-H21 (builder, stl-re-measure-intent stage).
Everything works in the frozen DATUM frame of intake/alignment.json (theta CCW about +Z from +X).
The skill scripts (sections.py, fits.py, pattern_count.py) assume features coaxial with datum Z;
this part is an assembly whose sub-parts sit on their own (tilted / offset) axes, so the
per-feature axis fits below are run-local code (reported in BUILDER_REPORT as a skill gap).
Deterministic: least_squares with fixed starts, no randomness."""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path
import numpy as np, trimesh
from scipy.optimize import least_squares
RUN = Path(__file__).resolve().parents[3]
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-intake-datum/scripts')
from datum_fit import fit_circle_irls  # noqa: E402

def sha(p):
    h = hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()

_M = None
def mesh():
    global _M
    if _M is None:
        _M = trimesh.load(RUN / 'intake/aligned_work.stl')
    return _M

def axis_dir(tx, ty):
    d = np.array([np.tan(tx), np.tan(ty), 1.0]); return d / np.linalg.norm(d)

def frame(p, d):
    """local frame: e3 = d, e1 = the datum axis least parallel to d, projected (X for near-Z axes, Z otherwise)."""
    d = np.asarray(d, float); d = d / np.linalg.norm(d)
    ref = np.array([0, 0, 1.0]) if abs(d[2]) < 0.9 else np.array([1.0, 0, 0])
    e1 = ref - (ref @ d) * d; e1 /= np.linalg.norm(e1); e2 = np.cross(d, e1)
    return np.asarray(p, float), np.vstack([e1, e2, d])

def to_local(X, p, R):
    return (np.asarray(X) - p) @ R.T

def rho_u(P, cx, cy, z0, tx, ty):
    d = axis_dir(tx, ty); q = P - np.array([cx, cy, z0]); u = q @ d
    return np.linalg.norm(q - np.outer(u, d), axis=1), u

def stats(e):
    e = np.abs(np.asarray(e)); return dict(rms=float(np.sqrt((e**2).mean())), p95=float(np.percentile(e, 95)), max=float(e.max()), n=int(e.size))

def fit_axis_cyl(P, z0, init, taper=False, fix_tilt=False, f_scale=0.05):
    """cylinder (or cone rho = R + k (u)) about an axis through (cx,cy,z0) with tilt (tx,ty) rad.
    Robust soft_l1 loss (scale 0.05 mm ~ 1.5x scan noise)."""
    cx, cy, R0 = init
    x0 = [cx, cy] + ([] if fix_tilt else [0.0, 0.0]) + [R0] + ([0.0] if taper else [])
    def unpack(x):
        i = 2; cx, cy = x[0], x[1]
        if fix_tilt: tx = ty = 0.0
        else: tx, ty = x[2], x[3]; i = 4
        R = x[i]; k = x[i + 1] if taper else 0.0
        return cx, cy, tx, ty, R, k
    def res(x):
        cx, cy, tx, ty, R, k = unpack(x); r, u = rho_u(P, cx, cy, z0, tx, ty); return r - (R + k * u)
    s = least_squares(res, np.array(x0, float), loss='soft_l1', f_scale=f_scale)
    cx, cy, tx, ty, R, k = unpack(s.x)
    d = axis_dir(tx, ty)
    return dict(cx=float(cx), cy=float(cy), z0=float(z0), tx_deg=float(np.degrees(tx)), ty_deg=float(np.degrees(ty)),
                tilt_deg=float(np.degrees(np.arccos(d[2]))), tilt_dir_deg=float(np.degrees(np.arctan2(d[1], d[0]))),
                R=float(R), k=float(k), draft_deg=float(np.degrees(np.arctan(k))), **stats(res(s.x)))

def select_faces(zl, zh, rl, rh, c=(0, 0), ex=(), perp=0.3):
    m = mesh(); C = m.triangles_center; N = m.face_normals
    q = C[:, :2] - np.asarray(c); r = np.hypot(*q.T); th = np.degrees(np.arctan2(q[:, 1], q[:, 0]))
    s = (C[:, 2] > zl) & (C[:, 2] < zh) & (r > rl) & (r < rh) & (np.abs(N[:, 2]) < perp)
    for a, b in ex:
        s &= ~((th > a) & (th < b))
    return s

def local_faces(p, d):
    m = mesh(); pp, R = frame(p, d)
    return to_local(m.triangles_center, pp, R), m.face_normals @ R.T, m.area_faces

def local_verts(p, d):
    m = mesh(); pp, R = frame(p, d); return to_local(m.vertices, pp, R)

def refine_axis(p, d, ulo, uhi, rlo, rhi, R0, taper=False, iters=3):
    """refine an off-Z feature axis by a tilted-cylinder fit in its local frame; returns fit, p, d
    (p re-anchored where the axis crosses the plane through the datum origin normal to d's
    horizontal projection)."""
    p = np.asarray(p, float); d = np.asarray(d, float) / np.linalg.norm(d); f = None
    for _ in range(iters):
        Cl, Nl, _A = local_faces(p, d)
        rr = np.hypot(Cl[:, 0], Cl[:, 1])
        s = (Cl[:, 2] > ulo) & (Cl[:, 2] < uhi) & (rr > rlo) & (rr < rhi) & (np.abs(Nl[:, 2]) < 0.3)
        z0 = 0.5 * (ulo + uhi)
        f = fit_axis_cyl(Cl[s], z0, (0, 0, R0), taper=taper)
        pp, R = frame(p, d)
        dl = axis_dir(np.radians(f['tx_deg']), np.radians(f['ty_deg'])); dn = R.T @ dl
        pn = pp + R.T @ np.array([f['cx'], f['cy'], z0])
        h = dn[:2]; t = -(pn[:2] @ h) / (h @ h); p = pn + t * dn; d = dn
    return f, p, d

def profile_table(p, d, ulo, uhi, du, rmax, keep=None):
    V = local_verts(p, d); rr = np.hypot(V[:, 0], V[:, 1]); th = np.degrees(np.arctan2(V[:, 1], V[:, 0]))
    ok = rr < rmax
    if keep is not None: ok &= keep(th)
    rows = []
    for u in np.arange(ulo, uhi, du):
        t = ok & (V[:, 2] >= u) & (V[:, 2] < u + du)
        if t.sum() >= 3:
            rows.append([float(u + du / 2)] + np.percentile(rr[t], [1, 10, 50, 90, 99]).round(4).tolist() + [int(t.sum())])
    return rows

def fit_arc_rz(p, d, ulo, uhi, rlo, rhi, keep=None, init=None):
    """circle in the (u, rho) meridian plane through all vertices in a window (a revolved round or
    an O-ring section). Returns centre (u_c, rho_c), radius and residuals."""
    V = local_verts(p, d); rr = np.hypot(V[:, 0], V[:, 1]); th = np.degrees(np.arctan2(V[:, 1], V[:, 0]))
    s = (V[:, 2] > ulo) & (V[:, 2] < uhi) & (rr > rlo) & (rr < rhi)
    if keep is not None: s &= keep(th)
    P = np.c_[V[s, 2], rr[s]]
    x0 = init if init is not None else [P[:, 0].mean(), P[:, 1].mean() - 0.5, 0.5]
    res = lambda x: np.hypot(P[:, 0] - x[0], P[:, 1] - x[1]) - x[2]
    sl = least_squares(res, np.array(x0, float), loss='soft_l1', f_scale=0.05)
    return dict(u_c=float(sl.x[0]), rho_c=float(sl.x[1]), a=float(sl.x[2]), **stats(res(sl.x)))
