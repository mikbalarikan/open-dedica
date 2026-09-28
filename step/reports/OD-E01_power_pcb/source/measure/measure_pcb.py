#!/usr/bin/env python3
"""Run-local measurement script for OD-E01_Power-PCB (stl-re-measure-intent stage).

Provenance: NEW code written for this run (the skill scripts cover turned parts; this part is a
prismatic PCB assembly). It reads ONLY intake/aligned_work.stl (frozen datum frame) and
intake/alignment.json, and writes measure/figures/*.json|png and measure/params.json.
Deterministic: every random sample is seeded (seed 0); no wall-clock value except `created`.

Run from the run root:  python3 measure/measure_pcb.py
Blind spots: the solder side is not scanned (board bottom invented flat); connector cavity
floors, heatsink root, TO-220 lower body and Y-cap back face are occluded (tagged assumed).
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
from pathlib import Path

import numpy as np
import trimesh
from scipy import ndimage as ndi
from shapely.geometry import MultiPoint
from skimage.morphology import skeletonize

RUN = Path(__file__).resolve().parents[1]
FIG = RUN / "measure" / "figures"
FIG.mkdir(parents=True, exist_ok=True)
SEED = 0
RES = 0.1          # height-map raster (mm); parameter, not a threshold
REL_MIN = 0.18     # component detection height above the local board surface (mm) = ~6x noise


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def r3(v):
    if isinstance(v, (list, tuple, np.ndarray)):
        return [r3(x) for x in v]
    return round(float(v), 3)


# ----------------------------------------------------------------------------- inputs
MESH_P = RUN / "intake" / "aligned_work.stl"
ALIGN_P = RUN / "intake" / "alignment.json"
ALIGN = json.loads(ALIGN_P.read_text())
NOISE = float(ALIGN["scan_noise_mm"]["value"])
M = trimesh.load_mesh(MESH_P, process=True)
FC, FN, FA = M.triangles_center, M.face_normals, M.area_faces

# ----------------------------------------------------------------------------- height map
X0, Y0, X1, Y1 = -6.5, -57.5, 96.5, 5.5
W, H = int(round((X1 - X0) / RES)), int(round((Y1 - Y0) / RES))
pts, _ = trimesh.sample.sample_surface(M, 12_000_000, seed=SEED)
ix = ((pts[:, 0] - X0) / RES).astype(int)
iy = ((pts[:, 1] - Y0) / RES).astype(int)
ok = (ix >= 0) & (ix < W) & (iy >= 0) & (iy < H)
hm = np.full(H * W, -np.inf)
np.maximum.at(hm, iy[ok] * W + ix[ok], pts[ok, 2])
hm[hm == -np.inf] = np.nan
HM = hm.reshape(H, W)
XS = X0 + (np.arange(W) + 0.5) * RES
YS = Y0 + (np.arange(H) + 0.5) * RES
XX, YY = np.meshgrid(XS, YS)
FIN = np.isfinite(HM)
np.savez_compressed(FIG / "hmap.npz", hm=HM.astype(np.float32), x0=X0, y0=Y0, res=RES)
out: dict = {}


def region(xa, xb, ya, yb):
    return (XX > xa) & (XX < xb) & (YY > ya) & (YY < yb)


def fregion(xa, xb, ya, yb, za=-9.0, zb=99.0):
    return (FC[:, 0] > xa) & (FC[:, 0] < xb) & (FC[:, 1] > ya) & (FC[:, 1] < yb) & (FC[:, 2] > za) & (FC[:, 2] < zb)


def robust_line(u, v, scale=0.05, it=15):
    A = np.c_[u, np.ones(len(u))]
    k = np.linalg.lstsq(A, v, rcond=None)[0]
    for _ in range(it):
        r = v - A @ k
        w = 1.0 / (1.0 + (r / scale) ** 2)
        k = np.linalg.lstsq(A * np.sqrt(w)[:, None], v * np.sqrt(w), rcond=None)[0]
    r = v - A @ k
    return k, float(np.sqrt(np.mean(r ** 2)))


def kasa(x, y):
    A = np.c_[2 * x, 2 * y, np.ones(len(x))]
    cx, cy, c = np.linalg.lstsq(A, x ** 2 + y ** 2, rcond=None)[0]
    r = np.sqrt(c + cx ** 2 + cy ** 2)
    res = np.hypot(x - cx, y - cy) - r
    return float(cx), float(cy), float(r), float(np.sqrt(np.mean(res ** 2)))


def irls_circle(x, y, w=None, scale=0.3, it=20):
    if w is None:
        w = np.ones(len(x))
    cx, cy, r, _ = kasa(x, y)
    for _ in range(it):
        res = np.hypot(x - cx, y - cy) - r
        ww = w / (1 + (res / scale) ** 2)
        A = np.c_[2 * x, 2 * y, np.ones(len(x))] * np.sqrt(ww)[:, None]
        b = (x ** 2 + y ** 2) * np.sqrt(ww)
        cx, cy, c = np.linalg.lstsq(A, b, rcond=None)[0]
        r = np.sqrt(c + cx ** 2 + cy ** 2)
    res = np.hypot(x - cx, y - cy) - r
    return float(cx), float(cy), float(r), float(np.sqrt(np.average(res ** 2, weights=w)))


def face_hole(sel, u_axis, u0, u1, v0, v1, grid=0.1, close_it=3, min_area=0.5):
    """Largest enclosed empty disc in a face-set occupancy image (u = world axis index, v = z).
    The faces are densely sampled (seeded) so the image is not limited by the face spacing."""
    sub = M.submesh([np.where(sel)[0]], append=True)
    pp, _ = trimesh.sample.sample_surface(sub, max(2000, int(sub.area * 400)), seed=SEED)
    uu, vv = pp[:, u_axis], pp[:, 2]
    img = np.zeros((int((v1 - v0) / grid), int((u1 - u0) / grid)), bool)
    iu_ = ((uu - u0) / grid).astype(int)
    iv_ = ((vv - v0) / grid).astype(int)
    k = (iu_ >= 0) & (iu_ < img.shape[1]) & (iv_ >= 0) & (iv_ < img.shape[0])
    img[iv_[k], iu_[k]] = True
    img = ndi.binary_closing(img, iterations=close_it)
    lab_, n_ = ndi.label(~img)
    best_ = None
    for i in range(1, n_ + 1):
        e = lab_ == i
        a, b = np.nonzero(e)
        if e.sum() * grid * grid < min_area or a.min() == 0 or b.min() == 0 or a.max() == img.shape[0] - 1 or b.max() == img.shape[1] - 1:
            continue
        edge = e & ~ndi.binary_erosion(e)
        ea, eb = np.nonzero(edge)
        cu, cv, r_, rms_ = kasa(eb * grid + u0 + grid / 2, ea * grid + v0 + grid / 2)
        if best_ is None or e.sum() > best_["n_px"]:
            best_ = {"u": cu, "z": cv, "d_fit": 2 * r_ + grid, "fit_rms": rms_, "n_px": int(e.sum()),
                     "d_equiv": 2 * np.sqrt(e.sum() * grid * grid / np.pi)}
    return best_


def wall_bounds(x0, x1, y0, y1, zlo, zhi, margin=0.8, cone=25.0):
    """Outer side walls of a box-like part from the scan faces (not the top-view silhouette, which
    also catches top-edge flares and scanner fringe). For each side: faces whose normal is within
    `cone` of the outward axis, on that side of the centre, in the z band; value = median of the
    faces within 0.25 mm of the area-weighted histogram peak (0.1 mm bins), i.e. the dominant wall,
    not a terminal or lead toe standing proud of it. Returns None for a side with < 15 faces."""
    cx_, cy_ = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
    reg_ = fregion(x0 - margin, x1 + margin, y0 - margin, y1 + margin, zlo, zhi)
    ct = np.cos(np.radians(cone))
    res = {}
    for key, ax_, sg, side_ok in (("x0", 0, -1, FC[:, 0] < cx_), ("x1", 0, 1, FC[:, 0] > cx_),
                                  ("y0", 1, -1, FC[:, 1] < cy_), ("y1", 1, 1, FC[:, 1] > cy_)):
        m_ = reg_ & side_ok & (FN[:, ax_] * sg > ct)
        if m_.sum() < 15:
            res[key] = None
            continue
        v_ = FC[m_, ax_]
        a_ = FA[m_]
        nb_ = max(1, int(np.ceil((v_.max() - v_.min()) / 0.1)))
        hh_, ee_ = np.histogram(v_, bins=nb_, weights=a_)
        pk_ = 0.5 * (ee_[np.argmax(hh_)] + ee_[np.argmax(hh_) + 1])
        k_ = (np.abs(v_ - pk_) < 0.25)
        res[key] = float(np.median(v_[k_]))
        res[key + "_n"] = int(k_.sum())
    return res


# ----------------------------------------------------------------------------- 1. board
edges = {}
for name, nv, axis, lo, hi in [("x_max", [1, 0, 0], 0, 94.5, 96.5), ("x_min", [-1, 0, 0], 0, -6.5, -4.5),
                               ("y_max", [0, 1, 0], 1, 3.3, 5.0), ("y_min", [0, -1, 0], 1, -57.0, -55.4)]:
    s = (FN @ np.array(nv) > np.cos(np.radians(15))) & (FC[:, axis] > lo) & (FC[:, axis] < hi) & (FC[:, 2] < 0.05)
    other = 1 - axis
    k, rms = robust_line(FC[s, other], FC[s, axis])
    mid = 0.5 * (FC[s, other].min() + FC[s, other].max())
    # thickness: per 3 mm station, z extent of the edge-wall faces
    zs = []
    for a in np.arange(FC[s, other].min(), FC[s, other].max(), 3.0):
        t = s & (FC[:, other] >= a) & (FC[:, other] < a + 3.0)
        if t.sum() > 20:
            vz = M.vertices[M.faces[t]].reshape(-1, 3)[:, 2]
            zs.append((float(vz.max()), float(vz.min())))
    edges[name] = {"pos": float(k[1] + k[0] * mid), "slope_deg": float(np.degrees(np.arctan(k[0]))),
                   "rms": rms, "n_faces": int(s.sum()), "wall_stations": zs}
thick = [a - b for e in edges.values() for a, b in e["wall_stations"]]
bottoms = [b for e in edges.values() for a, b in e["wall_stations"]]
out["board"] = {"edges": edges, "thickness_station_p50": float(np.median(thick)),
                "thickness_stations": [r3(t) for t in thick],
                "wall_bottom_z_p50": float(np.median(bottoms))}
BX0, BX1 = edges["x_min"]["pos"], edges["x_max"]["pos"]
BY0, BY1 = edges["y_min"]["pos"], edges["y_max"]["pos"]
INB = region(BX0 + 0.2, BX1 - 0.2, BY0 + 0.2, BY1 - 0.2)

# local board surface (warp) : quadratic fit to near-zero pixels
b = INB & FIN & (np.abs(np.nan_to_num(HM)) < 0.2)
surf = np.zeros_like(HM)
for _ in range(3):
    A = np.c_[np.ones(b.sum()), XX[b], YY[b], XX[b] ** 2, XX[b] * YY[b], YY[b] ** 2]
    kq = np.linalg.lstsq(A, HM[b], rcond=None)[0]
    surf = np.stack([np.ones_like(XX), XX, YY, XX ** 2, XX * YY, YY ** 2], -1) @ kq
    b = INB & FIN & (np.abs(np.nan_to_num(HM - surf, nan=9)) < 0.12)
REL = HM - surf
out["board"]["warp_quadratic"] = {"coef_1_x_y_xx_xy_yy": r3(kq), "rms_after_mm": float(np.sqrt(np.mean(REL[b] ** 2))),
                                  "surface_min_mm": float(surf[INB].min()), "surface_max_mm": float(surf[INB].max())}

# slot on the -X edge
sl = region(BX0 - 0.5, 4.0, -28.0, -25.0) & ~FIN
lab, n = ndi.label(sl)
k = 1 + int(np.argmax(ndi.sum(sl, lab, range(1, n + 1))))
sl = lab == k
cols = [(YY[sl[:, j], j].min() - RES / 2, YY[sl[:, j], j].max() + RES / 2) for j in range(W)
        if -4.0 < XS[j] < 1.0 and sl[:, j].sum() > 3]
cols = np.array(cols)
out["board"]["slot"] = {"y_min": float(np.median(cols[:, 0])), "y_max": float(np.median(cols[:, 1])),
                        "x_end": float(XX[sl].max() + RES / 2), "n_columns": int(len(cols)),
                        "method": "no-data pixels of the routed slot, per-column extent median over x -4..1 (height map, 0.1 mm)"}

# holes: boundary of the no-data disc, Kasa
HOLE_GUESS = {"H1": (0.0, 0.0), "H2": (-0.1, -51.8), "H3": (11.6, -6.5), "H4": (11.0, -18.8),
              "H5": (57.4, 2.8), "H6": (57.4, -49.9)}
holes = {}
for hn, (gx, gy) in HOLE_GUESS.items():
    s = ~FIN & (np.hypot(XX - gx, YY - gy) < 3.0) & INB
    lab, n = ndi.label(s)
    kk = 1 + int(np.argmax([((lab == i).sum() if np.hypot(XX[lab == i].mean() - gx, YY[lab == i].mean() - gy) < 1.5 else 0)
                            for i in range(1, n + 1)]))
    s = lab == kk
    e = s & ~ndi.binary_erosion(s)
    cx, cy, r, rms = kasa(XX[e], YY[e])
    holes[hn] = {"cx": cx, "cy": cy, "r_raster": r + RES / 2, "rms": rms, "n_boundary_px": int(e.sum())}
    q_ = FC[:, :2] - [cx, cy]
    rq = np.hypot(q_[:, 0], q_[:, 1])
    wall = (np.abs(FN[:, 2]) < 0.3) & (rq < r + 0.9) & (FC[:, 2] > -1.45) & (FC[:, 2] < -0.15)
    wall &= ((FN[:, :2] * (q_ / np.maximum(rq, 1e-9)[:, None])).sum(1)) < -0.3   # inner wall faces point to the axis
    if wall.sum() >= 30:
        wx, wy, wr, wrms = irls_circle(FC[wall, 0], FC[wall, 1], FA[wall], scale=0.1)
        th_ = np.degrees(np.arctan2(FC[wall, 1] - wy, FC[wall, 0] - wx))
        holes[hn].update({"wall_cx": wx, "wall_cy": wy, "wall_r": wr, "wall_rms": wrms, "wall_faces": int(wall.sum()),
                          "wall_angular_coverage_deg": int(len(np.unique(np.floor((th_ + 180) / 10))) * 10)})
# H1 radius from the wall-face datum fit (better than raster)
holes["H1"]["r_wall_fit"] = ALIGN["secondary"]["r_by_feature"][next(iter(ALIGN["secondary"]["r_by_feature"]))]["r_mean"]
out["holes"] = holes

# ----------------------------------------------------------------------------- 2. segmentation
MASK = INB & FIN & (np.nan_to_num(REL, nan=-9) > REL_MIN)
LAB, NSEG = ndi.label(MASK)
SPECIAL = {  # regions owned by dedicated measurements (datum frame xy boxes)
    "heatsink_group": (38.5, 55.5, -41.5, -1.2),
    "C1": (65.5, 72.5, -3.2, 3.5), "C2": (70.0, 77.6, -20.0, -12.5), "C345": (80.5, 94.5, -28.5, 1.8),
    "D12": (66.0, 72.6, -14.5, -2.4), "L2": (77.3, 81.0, -25.0, -11.0),
    "resistor_R1": (64.0, 72.5, -46.0, -21.5),
    "ycap_CY1": (75.5, 90.0, -48.5, -37.0),
    "x2_CX1": (73.0, 91.5, -36.0, -29.5),
    "faston_row": (34.0, 90.0, -55.5, -45.8),
    "J1": (6.5, 13.0, -40.0, -21.3), "J2": (-4.0, 3.0, -47.0, -36.2), "J3": (6.0, 12.2, -5.2, 3.3),
    "K1": (5.0, 13.0, -55.5, -46.8), "K2": (-4.5, 2.6, -35.0, -28.5),
}
# small SMD parts that fall inside a special box but are not part of it are still auto boxes
SPECIAL_KEEP_SMALL = {"C1", "C2", "C345", "D12", "L2", "resistor_R1", "faston_row", "heatsink_group"}
segs = []
for i in range(1, NSEG + 1):
    s = LAB == i
    area = s.sum() * RES * RES
    if area < 0.25:
        continue
    cx, cy = float(XX[s].mean()), float(YY[s].mean())
    z90 = float(np.percentile(REL[s], 90))
    owner = None
    for nm, (xa, xb, ya, yb) in SPECIAL.items():
        if xa < cx < xb and ya < cy < yb:
            owner = nm
            break
    if owner in SPECIAL_KEEP_SMALL and z90 < 1.3 and area < 8.0:
        owner = None
    segs.append({"id": i, "area": area, "cx": cx, "cy": cy, "z90_rel": z90, "owner": owner})

for nm in ("J1", "J2", "J3", "K1", "K2"):
    own_ = [s_ for s_ in segs if s_["owner"] == nm]
    if len(own_) > 1:
        big = max(own_, key=lambda s_: s_["area"])
        for s_ in own_:
            if s_ is not big:
                s_["owner"] = None
                s_["note"] = f"inside {nm}: modelled as its own box"
boxes = []
extra_boxes = []
for sg in segs:
    if sg["owner"] is not None:
        continue
    s = LAB == sg["id"]
    h = sg["z90_rel"]
    half = s & (REL >= 0.5 * h)
    lab2, n2 = ndi.label(half)
    if n2 > 1:  # keep the main body only
        k2 = 1 + int(np.argmax(ndi.sum(half, lab2, range(1, n2 + 1))))
        half = lab2 == k2
    topm = half & (REL >= 0.8 * h)
    x0, x1 = float(XX[half].min() - RES / 2), float(XX[half].max() + RES / 2)
    y0, y1 = float(YY[half].min() - RES / 2), float(YY[half].max() + RES / 2)
    zt = float(np.median(HM[topm]))
    rr = MultiPoint(np.c_[XX[half], YY[half]]).minimum_rotated_rectangle
    c4 = np.array(rr.exterior.coords)[:4]
    ang = float(np.degrees(np.arctan2(*(c4[1] - c4[0])[::-1])) % 90.0)
    ang = ang if ang < 45 else ang - 90
    footprint = "half-height top-view bbox"
    if h > 1.4:   # tall part: side walls are scanned well enough to replace the top-view silhouette
        wb = wall_bounds(x0, x1, y0, y1, zt - 0.6 * h, zt - 0.12 * h)   # upper band: terminals / lead toes excluded
        tf_ = half & (REL >= 0.8 * h)       # the top face: walls must sit at its edge (+/-0.6), not at lead toes
        tv_ = {"x0": float(XX[tf_].min() - RES / 2), "x1": float(XX[tf_].max() + RES / 2),
               "y0": float(YY[tf_].min() - RES / 2), "y1": float(YY[tf_].max() + RES / 2)}
        got = [k_ for k_ in tv_ if wb.get(k_) is not None and abs(wb[k_] - tv_[k_]) < 0.6]
        x0, x1, y0, y1 = [(wb[k_] if k_ in got else tv_[k_]) for k_ in ("x0", "x1", "y0", "y1")]
        footprint = f"side-wall faces for {got}, top-view bbox for the rest"
    if h > 1.4:   # terminals / lead rows standing outside the body: their own boxes
        res_ = s & (REL > 0.3) & ~region(x0 - 0.2, x1 + 0.2, y0 - 0.2, y1 + 0.2)
        lab3, n3 = ndi.label(res_)
        for i3 in range(1, n3 + 1):
            e3 = lab3 == i3
            if e3.sum() * RES * RES < 0.15:
                continue
            extra_boxes.append({"seg": sg["id"], "x0": float(XX[e3].min() - RES / 2), "x1": float(XX[e3].max() + RES / 2),
                                "y0": float(YY[e3].min() - RES / 2), "y1": float(YY[e3].max() + RES / 2),
                                "ztop": float(np.percentile(HM[e3], 90)), "h_rel": float(np.percentile(REL[e3], 90)),
                                "footprint": f"terminal / lead group of segment {sg['id']} outside its body box",
                                "minrect_angle_deg": 0.0, "fill_bbox": None})
    boxes.append({"seg": sg["id"], "x0": x0, "x1": x1, "y0": y0, "y1": y1, "ztop": zt, "h_rel": h, "footprint": footprint,
                  "minrect_angle_deg": ang, "fill_bbox": float(half.sum() * RES * RES / ((x1 - x0) * (y1 - y0)))})
boxes += extra_boxes
boxes.sort(key=lambda b_: (round(b_["x0"], 1), round(b_["y0"], 1)))
out["segments"] = [{k_: (r3(v) if isinstance(v, float) else v) for k_, v in s_.items()} for s_ in segs]
out["auto_boxes"] = [{k_: (r3(v) if isinstance(v, float) else v) for k_, v in b_.items()} for b_ in boxes]


# ----------------------------------------------------------------------------- 3. vertical caps
def cap_fit(name, gx, gy, r0, zband):
    s = fregion(gx - r0 - 1.2, gx + r0 + 1.2, gy - r0 - 1.2, gy + r0 + 1.2, zband[0], zband[1])
    s &= np.abs(FN[:, 2]) < 0.3
    q = FC[:, :2] - [gx, gy]
    rr = np.hypot(q[:, 0], q[:, 1])
    s &= (rr > r0 - 0.9) & (rr < r0 + 0.9)
    s &= ((FN[:, :2] * (q / np.maximum(rr, 1e-9)[:, None])).sum(1)) > 0.3  # outward-facing wall
    cx, cy, r, rms = irls_circle(FC[s, 0], FC[s, 1], FA[s], scale=0.1)
    th = np.degrees(np.arctan2(FC[s, 1] - cy, FC[s, 0] - cx))
    cov = len(np.unique(np.floor((th + 180) / 10))) * 10
    inner = np.hypot(XX - cx, YY - cy) < 0.75 * r
    ztop = float(np.nanmedian(HM[inner & FIN]))
    zt90 = float(np.nanpercentile(HM[inner & FIN], 90))
    # second station just below the top rim (sleeve / bulge check): same wall-face IRLS
    s2 = fregion(gx - r0 - 1.5, gx + r0 + 1.5, gy - r0 - 1.5, gy + r0 + 1.5, zt90 - 1.8, zt90 - 0.5) & (np.abs(FN[:, 2]) < 0.3)
    q2 = FC[:, :2] - [cx, cy]
    rr2 = np.hypot(q2[:, 0], q2[:, 1])
    s2 &= (rr2 > r - 0.8) & (rr2 < r + 1.0) & (((FN[:, :2] * (q2 / np.maximum(rr2, 1e-9)[:, None])).sum(1)) > 0.3)
    cx2, cy2, r2, rms2 = irls_circle(FC[s2, 0], FC[s2, 1], FA[s2], scale=0.1)
    return {"name": name, "cx": cx, "cy": cy, "r": r, "rms": rms, "n_faces": int(s.sum()),
            "angular_coverage_deg": int(cov), "z_band": list(zband), "ztop_p50": ztop, "ztop_p90": zt90,
            "upper": {"cx": cx2, "cy": cy2, "r": r2, "rms": rms2, "n_faces": int(s2.sum()), "z_band": [zt90 - 1.8, zt90 - 0.5]}}


def cap_profile(cp):
    bins = []
    for z0 in np.arange(0.5, cp["ztop_p90"] - 0.4, 1.0):
        q_ = FC[:, :2] - [cp["cx"], cp["cy"]]
        rr_ = np.hypot(q_[:, 0], q_[:, 1])
        s_ = (np.abs(FN[:, 2]) < 0.3) & (FC[:, 2] > z0) & (FC[:, 2] < z0 + 1) & (rr_ > cp["r"] - 1.0) & (rr_ < cp["r"] + 1.0) & \
            (((FN[:, :2] * (q_ / np.maximum(rr_, 1e-9)[:, None])).sum(1)) > 0.3)
        if s_.sum() < 30:
            continue
        th_ = np.degrees(np.arctan2(q_[s_, 1], q_[s_, 0]))
        cx_, cy_, r_, rms_ = irls_circle(FC[s_, 0], FC[s_, 1], FA[s_], scale=0.1)
        bins.append({"z": float(z0 + 0.5), "n": int(s_.sum()), "cov": int(len(np.unique(np.floor((th_ + 180) / 15))) * 15),
                     "cx": cx_, "cy": cy_, "r": r_, "rms": rms_})
    good = [b_ for b_ in bins if b_["rms"] < 0.08 and b_["cov"] >= 225]
    bins_ok = [b_ for b_ in bins if b_["rms"] < 0.3]
    zz = np.array([b_["z"] for b_ in good])
    w_ = np.array([b_["n"] for b_ in good], float)
    kx = np.polyfit(zz, [b_["cx"] for b_ in good], 1, w=np.sqrt(w_))
    ky = np.polyfit(zz, [b_["cy"] for b_ in good], 1, w=np.sqrt(w_))
    upper = [b_ for b_ in bins_ok if b_["z"] >= 0.6 * cp["ztop_p90"]]
    r_body = float(np.median([b_["r"] for b_ in upper]))
    low = [b_ for b_ in bins_ok if b_["z"] < cp["ztop_p90"] - 1.5]
    grv = [b_ for b_ in low if b_["r"] < r_body - 0.12]
    if grv:   # keep the contiguous run that contains the narrowest bin
        zs_ = sorted(b_["z"] for b_ in grv)
        zmin_ = min(grv, key=lambda b_: b_["r"])["z"]
        run = [zmin_]
        for z_ in sorted([z_ for z_ in zs_ if z_ > zmin_]):
            if z_ - run[-1] <= 1.01:
                run.append(z_)
        for z_ in sorted([z_ for z_ in zs_ if z_ < zmin_], reverse=True):
            if run[0] - z_ <= 1.01:
                run.insert(0, z_)
        grv = [b_ for b_ in grv if b_["z"] in run]
    prof = {"axis_x_at_z0": float(np.polyval(kx, 0.0)), "axis_y_at_z0": float(np.polyval(ky, 0.0)),
            "axis_dx_dz": float(kx[0]), "axis_dy_dz": float(ky[0]), "r_body": r_body, "bins": bins}
    # stand-off: board-level scan faces seen under the can (inside its base radius) -> the can sits on a stem
    q0 = FC[:, :2] - [float(np.polyval(kx, 0.0)), float(np.polyval(ky, 0.0))]
    r0_ = np.hypot(q0[:, 0], q0[:, 1])
    r_base_est = max(b_["r"] for b_ in bins_ok if b_["z"] < 3.0) if any(b_["z"] < 3.0 for b_ in bins_ok) else r_body
    under = (FC[:, 2] < 0.3) & (FN[:, 2] > 0.8) & (r0_ < r_base_est - 0.3)
    if under.sum() >= 50:
        wl = (np.abs(FN[:, 2]) < 0.5) & (r0_ > r_base_est - 0.6) & (r0_ < r_base_est + 0.4) & (FC[:, 2] < 3.0) & \
            (((FN[:, :2] * (q0 / np.maximum(r0_, 1e-9)[:, None])).sum(1)) > 0.3)
        th0 = np.degrees(np.arctan2(q0[:, 1], q0[:, 0]))
        zso = None
        for z_ in np.arange(0.0, 3.0, 0.2):
            kk = wl & (FC[:, 2] >= z_) & (FC[:, 2] < z_ + 0.2)
            if kk.sum() >= 10 and len(np.unique(np.floor((th0[kk] + 180) / 15))) * 15 >= 180:
                zso = float(z_)
                break
        prof_stand = {"stem_r": float(np.percentile(r0_[under], 1) - 0.1), "standoff_z": zso,
                      "n_board_faces_under": int(under.sum()),
                      "method": "stem r = 1st pct radius of board-level faces seen under the can - 0.1; stand-off = lowest "
                                "0.2 mm z bin whose outward can-wall faces cover >= 180 deg; applied only when the board is "
                                "seen deep under the can (stem r < 0.7 x base r), otherwise it is the curled bottom edge",
                      "r_base_est": float(r_base_est)} if zso else None
        if prof_stand and prof_stand["stem_r"] >= 0.7 * r_base_est:
            prof_stand = {"not_applied": prof_stand}
    else:
        prof_stand = None
    prof["standoff"] = prof_stand
    if grv:
        zg0 = min(b_["z"] for b_ in grv) - 0.5
        zg1 = max(b_["z"] for b_ in grv) + 0.5
        base = [b_ for b_ in low if b_["z"] < zg0]
        prof.update({"groove_z0": float(zg0), "groove_z1": float(zg1), "r_groove": float(min(b_["r"] for b_ in grv)),
                     "r_base": float(np.median([b_["r"] for b_ in base])) if base else float(min(b_["r"] for b_ in grv))})
    else:
        prof.update({"groove_z0": 0.0, "groove_z1": 0.0, "r_groove": r_body, "r_base": r_body})
    return prof


CAPS = [("C1", 69.0, 0.2, 2.7, (1.5, 4.5)), ("C2", 73.85, -16.3, 3.25, (3.0, 10.0)),
        ("C3", 85.8, -12.5, 5.1, (4.0, 11.5)), ("C4", 87.8, -22.8, 5.1, (4.0, 11.5)),
        ("C5", 89.2, -3.2, 3.7, (3.0, 6.6))]
out["caps"] = [cap_fit(*c) for c in CAPS]
for cp in out["caps"]:
    cp["profile"] = cap_profile(cp)
c1 = out["caps"][0]
rq_ = np.hypot(XX - c1["cx"], YY - c1["cy"])
bp = region(c1["cx"] - 4.0, c1["cx"] + 4.0, c1["cy"] - 4.0, c1["cy"] + 4.0) & FIN & (np.nan_to_num(REL) > 0.6) & \
    (np.nan_to_num(REL) < 2.2) & (rq_ > c1["profile"]["r_body"] + 0.25)
lab_, n_ = ndi.label(bp)
k_ = [i for i in range(1, n_ + 1) if (lab_ == i).sum() * RES * RES > 1.0]
bp = np.isin(lab_, k_)
bb_ = {"x0": float(XX[bp].min() - RES / 2), "x1": float(XX[bp].max() + RES / 2),
       "y0": float(YY[bp].min() - RES / 2), "y1": float(YY[bp].max() + RES / 2)}
wb_ = wall_bounds(bb_["x0"], bb_["x1"], bb_["y0"], bb_["y1"], 0.35, 1.2)
used_ = [k2 for k2 in bb_ if wb_.get(k2) is not None and abs(wb_[k2] - bb_[k2]) < 0.6]
c1["base_plate"] = {**{k2: (wb_[k2] if k2 in used_ else bb_[k2]) for k2 in bb_}, "walls_used": used_,
                    "ztop": float(np.median(HM[bp & (np.nan_to_num(REL) > 1.0)])),
                    "method": "SMD V-chip base: pixels 0.6..2.2 above the board outside the can (+0.25), side walls z 0.35..1.2"}


# ----------------------------------------------------------------------------- 4. X2 film cap and plain big boxes
def big_box(name, xa, xb, ya, yb, frac=0.5):
    s = region(xa, xb, ya, yb) & MASK
    lab_, n_ = ndi.label(s)
    k_ = 1 + int(np.argmax(ndi.sum(s, lab_, range(1, n_ + 1))))
    s = lab_ == k_
    h = float(np.percentile(REL[s], 90))
    half = s & (REL >= frac * h)
    topm = half & (REL >= 0.85 * h)
    bb = {"x0": float(XX[half].min() - RES / 2), "x1": float(XX[half].max() + RES / 2),
          "y0": float(YY[half].min() - RES / 2), "y1": float(YY[half].max() + RES / 2)}
    zt = float(np.median(HM[topm]))
    wb = wall_bounds(bb["x0"], bb["x1"], bb["y0"], bb["y1"], zt - 0.6 * h, zt - 0.12 * h)
    used = [k_ for k_ in bb if wb.get(k_) is not None and abs(wb[k_] - bb[k_]) < 1.0]
    return {"name": name, **{k_: (wb[k_] if k_ in used else bb[k_]) for k_ in bb}, "topview_bbox": bb, "walls_used": used,
            "ztop": zt, "ztop_spread_p5_p95": r3(np.percentile(HM[topm], [5, 95]))}


out["x2_CX1"] = big_box("CX1", *SPECIAL["x2_CX1"])


# ----------------------------------------------------------------------------- 5. fastons
FAST_X = [36.1, 51.2, 64.7, 71.1, 77.6, 88.1]
fastons = []
for fx in FAST_X:
    blade = fregion(fx - 1.2, fx + 1.2, -54.3, -47.0, 3.0, 9.0)
    xm = blade & (FN[:, 0] < -0.9)
    xp = blade & (FN[:, 0] > 0.9)
    xa_ = float(np.median(FC[xm, 0])) if xm.sum() > 10 else np.nan
    xb_ = float(np.median(FC[xp, 0])) if xp.sum() > 10 else np.nan
    yb = fregion(fx - 1.2, fx + 1.2, -56.0, -45.0, 3.0, 9.0)
    ym = yb & (FN[:, 1] < -0.9)
    yp = yb & (FN[:, 1] > 0.9)
    y0_ = float(np.median(FC[ym, 1]))
    y1_ = float(np.median(FC[yp, 1]))
    foot = fregion(fx - 1.5, fx + 1.5, -56.0, -45.0, 0.3, 1.5)
    fm = foot & (FN[:, 1] < -0.9)
    fp = foot & (FN[:, 1] > 0.9)
    top = region(fx - 1.0, fx + 1.0, -53.0, -48.0) & FIN
    zt = float(np.percentile(HM[top], 95))
    # y extent of the blade at 0.3 below the top (chamfer)
    near = region(fx - 1.0, fx + 1.0, -55.0, -46.0) & FIN & (np.nan_to_num(HM) > zt - 0.3)
    # foot top: highest z where the section is wider than the blade (+0.5 mm)
    fz = []
    for z in np.arange(0.5, 4.0, 0.1):
        ss = fregion(fx - 1.5, fx + 1.5, -56.0, -45.0, z - 0.05, z + 0.05) & (np.abs(FN[:, 1]) > 0.8)
        if ss.sum() > 4 and (FC[ss, 1].max() - FC[ss, 1].min()) > (y1_ - y0_) + 0.5:
            fz.append(z)
    fastons.append({"x_face_minus": xa_, "x_face_plus": xb_, "x_centre": np.nanmean([xa_, xb_]) if np.isfinite(xa_) and np.isfinite(xb_) else (xa_ if np.isfinite(xa_) else xb_),
                    "thickness": (xb_ - xa_) if np.isfinite(xa_) and np.isfinite(xb_) else None,
                    "y0": y0_, "y1": y1_, "width": y1_ - y0_,
                    "foot_y0": float(np.median(FC[fm, 1])) if fm.sum() > 5 else None,
                    "foot_y1": float(np.median(FC[fp, 1])) if fp.sum() > 5 else None,
                    "foot_top_z": float(max(fz)) if fz else None,
                    "foot_x_minus": float(np.median(FC[foot & (FN[:, 0] < -0.9), 0])) if (foot & (FN[:, 0] < -0.9)).sum() > 5 else None,
                    "foot_x_plus": float(np.median(FC[foot & (FN[:, 0] > 0.9), 0])) if (foot & (FN[:, 0] > 0.9)).sum() > 5 else None,
                    "ztop_p95": zt, "top_y_extent_at_minus0.3": float(YY[near].max() - YY[near].min() + RES) if near.any() else None})
out["fastons"] = fastons
# detent hole, measured on every tab (-X face occupancy image)
holes_f = []
for f_ in fastons:
    fx = f_["x_centre"]
    sel = fregion(fx - 1.2, fx + 0.1, -54.0, -47.0, 3.5, 9.0) & (FN[:, 0] < -0.8)
    hh = face_hole(sel, 1, -54.0, -47.0, 3.5, 9.0)
    holes_f.append(hh)
out["faston_detent_holes"] = holes_f


# ----------------------------------------------------------------------------- 6. connectors with cavities (J1..J3)
def connector(name, xa, xb, ya, yb):
    s = region(xa, xb, ya, yb) & (MASK | ~FIN)
    s = ndi.binary_fill_holes(s & region(xa, xb, ya, yb))
    rim = region(xa, xb, ya, yb) & MASK
    h = float(np.percentile(REL[rim], 90))
    rimh = rim & (REL > 0.6 * h)
    lab_, n_ = ndi.label(ndi.binary_closing(rimh, iterations=3))
    k_ = 1 + int(np.argmax(ndi.sum(rimh, lab_, range(1, n_ + 1))))
    rimh &= lab_ == k_
    x0, x1 = float(XX[rimh].min() - RES / 2), float(XX[rimh].max() + RES / 2)
    y0, y1 = float(YY[rimh].min() - RES / 2), float(YY[rimh].max() + RES / 2)
    ztop = float(np.median(HM[rimh & (REL > 0.85 * h)]))
    wb = wall_bounds(x0, x1, y0, y1, ztop - 0.6 * h, ztop - 0.12 * h)
    tv = {"x0": x0, "x1": x1, "y0": y0, "y1": y1}
    used = [k_ for k_ in tv if wb.get(k_) is not None and abs(wb[k_] - tv[k_]) < 1.0]
    x0, x1, y0, y1 = [(wb[k_] if k_ in used else tv[k_]) for k_ in ("x0", "x1", "y0", "y1")]
    body = region(x0, x1, y0, y1)
    cav = region(x0 + 0.4, x1 - 0.4, y0 + 0.4, y1 - 0.4) & ~(FIN & (np.nan_to_num(REL) > 0.6 * h))
    lab_, n_ = ndi.label(cav)
    k_ = 1 + int(np.argmax(ndi.sum(cav, lab_, range(1, n_ + 1))))
    cav = lab_ == k_
    cx0, cx1 = np.percentile(XX[cav], [2, 98])
    cy0, cy1 = np.percentile(YY[cav], [2, 98])
    # inner walls (normals point INTO the cavity): refine each side from the faces near the raster edge
    ccx, ccy = 0.5 * (cx0 + cx1), 0.5 * (cy0 + cy1)
    band = fregion(x0 + 0.2, x1 - 0.2, y0 + 0.2, y1 - 0.2, ztop - 0.6 * h, ztop - 0.12 * h)
    inner = {}
    for key, ax_, sg, ref in (("cav_x0", 0, 1, cx0), ("cav_x1", 0, -1, cx1), ("cav_y0", 1, 1, cy0), ("cav_y1", 1, -1, cy1)):
        m_ = band & (FN[:, ax_] * sg > 0.9) & (np.abs(FC[:, ax_] - ref) < 0.8)
        if m_.sum() >= 15:
            inner[key] = float(np.median(FC[m_, ax_]))
            inner[key + "_n"] = int(m_.sum())
    cx0, cx1 = inner.get("cav_x0", cx0), inner.get("cav_x1", cx1)
    cy0, cy1 = inner.get("cav_y0", cy0), inner.get("cav_y1", cy1)
    floor_seen = HM[cav & FIN]
    upf = fregion(cx0 + 0.1, cx1 - 0.1, cy0 + 0.1, cy1 - 0.1, -0.5, ztop - 0.5 * h) & (FN[:, 2] > 0.8)
    floor_med = float(np.median(FC[upf, 2])) if upf.sum() >= 20 else None
    fl_ = floor_med if floor_med is not None else (float(np.min(floor_seen)) if floor_seen.size else 0.0)
    pins = []
    pm = region(cx0 + 0.15, cx1 - 0.15, cy0 + 0.15, cy1 - 0.15) & FIN & (np.nan_to_num(HM) > max(fl_, 0.0) + 0.8)
    lab_, n_ = ndi.label(pm)
    for i in range(1, n_ + 1):
        e_ = lab_ == i
        if e_.sum() * RES * RES < 0.3:
            continue
        pins.append([float(XX[e_].min() - RES / 2), float(XX[e_].max() + RES / 2), float(YY[e_].min() - RES / 2),
                     float(YY[e_].max() + RES / 2), float(np.percentile(HM[e_], 90))])
    return {"name": name, "x0": x0, "x1": x1, "y0": y0, "y1": y1, "ztop": ztop,
            "cav_x0": float(cx0), "cav_x1": float(cx1), "cav_y0": float(cy0), "cav_y1": float(cy1),
            "cav_floor_seen_min": float(np.min(floor_seen)) if floor_seen.size else None,
            "cav_floor_upfacing_median": floor_med, "cav_floor_upfacing_n": int(upf.sum()),
            "cav_nodata_frac": float((~FIN & cav).sum() / cav.sum()), "topview_bbox": tv, "walls_used": used, "inner_walls": inner, "inner_parts": pins}


out["connectors"] = [connector(nm, *SPECIAL[nm]) for nm in ("J1", "J2", "J3")]


# ----------------------------------------------------------------------------- 7. base + riser blocks (K1, K2)
def base_riser(name, xa, xb, ya, yb):
    s = region(xa, xb, ya, yb) & MASK
    lab_, n_ = ndi.label(s)
    k_ = 1 + int(np.argmax(ndi.sum(s, lab_, range(1, n_ + 1))))
    s = lab_ == k_
    zb = float(np.percentile(REL[s], 50))
    base = s & (REL > 0.5 * zb)
    riser = s & (REL > zb + 1.5)
    lab_, n_ = ndi.label(riser)
    k_ = 1 + int(np.argmax(ndi.sum(riser, lab_, range(1, n_ + 1))))
    riser = lab_ == k_
    zr = float(np.percentile(REL[riser], 90))
    riser &= REL > zb + 0.6 * (zr - zb)
    rx0_, rx1_ = float(XX[riser].min() - RES / 2), float(XX[riser].max() + RES / 2)
    ry0_, ry1_ = float(YY[riser].min() - RES / 2), float(YY[riser].max() + RES / 2)
    zr_top = float(np.percentile(HM[riser], 90))
    # sloped back (+X) face: faces with a +X normal component on the riser's +X side, above the base top
    zb_abs = float(np.median(HM[s & (np.abs(REL - zb) < 0.6)]))
    bk = fregion(0.5 * (rx0_ + rx1_), rx1_ + 1.5, ry0_ + 0.3, ry1_ - 0.3, zb_abs + 0.4, zr_top - 0.3) & (FN[:, 0] > 0.5)
    slope = None
    if bk.sum() > 20:
        kx = np.polyfit(FC[bk, 2], FC[bk, 0], 1)
        slope = {"x_at_base_top": float(np.polyval(kx, zb_abs)), "x_at_top": float(np.polyval(kx, zr_top)), "n_faces": int(bk.sum()),
                 "fit_rms": float(np.sqrt(np.mean((FC[bk, 0] - np.polyval(kx, FC[bk, 2])) ** 2)))}
    basetop = base & ~ndi.binary_dilation(riser, iterations=3) & (np.abs(REL - zb) < 0.6)
    tv = {"x0": float(XX[base].min() - RES / 2), "x1": float(XX[base].max() + RES / 2),
          "y0": float(YY[base].min() - RES / 2), "y1": float(YY[base].max() + RES / 2)}
    zbt = float(np.median(HM[basetop]))
    wb = wall_bounds(tv["x0"], tv["x1"], tv["y0"], tv["y1"], 0.4 * zbt, 0.88 * zbt)
    used = [k_ for k_ in tv if wb.get(k_) is not None and abs(wb[k_] - tv[k_]) < 1.0]
    bx = [(wb[k_] if k_ in used else tv[k_]) for k_ in ("x0", "x1", "y0", "y1")]
    bumps = []
    bm = base & ~ndi.binary_dilation(riser, iterations=4) & (REL > zb + 0.5)
    lab4, n4 = ndi.label(bm)
    for i4 in range(1, n4 + 1):
        e4 = lab4 == i4
        if e4.sum() * RES * RES < 0.2:
            continue
        bumps.append([float(XX[e4].min() - RES / 2), float(XX[e4].max() + RES / 2), float(YY[e4].min() - RES / 2),
                      float(YY[e4].max() + RES / 2), float(np.percentile(HM[e4], 90))])
    return {"name": name, "walls_used": used, "bumps": bumps,
            "base": [*bx, zbt],
            "riser": [rx0_, rx1_, ry0_, ry1_, zr_top], "riser_back_slope": slope}


out["base_riser"] = [base_riser(nm, *SPECIAL[nm]) for nm in ("K1", "K2")]


# ----------------------------------------------------------------------------- 8. horizontal axial bodies along Y
def axial_y(name, body_box, zmin_body, lead_boxes):
    """Cylinder with its axis parallel to Y: circle fit in (x, z) on the body's upper faces;
    y ends from the height map; leads as (x, y_end, z_axis) of the thin strips."""
    xa, xb, ya, yb = body_box
    s = fregion(xa, xb, ya, yb, zmin_body, 30.0) & (FN[:, 1] ** 2 < 0.5)
    cx, cz, r, rms = irls_circle(FC[s, 0], FC[s, 2], FA[s], scale=0.1)
    top = region(xa, xb, ya, yb) & FIN & (np.nan_to_num(HM) > cz)
    lab_, n_ = ndi.label(top)
    k_ = 1 + int(np.argmax(ndi.sum(top, lab_, range(1, n_ + 1))))
    top = lab_ == k_
    res = {"name": name, "x_axis": cx, "z_axis": cz, "r": r, "fit_rms": rms, "n_faces": int(s.sum()),
           "y0": float(YY[top].min() - RES / 2), "y1": float(YY[top].max() + RES / 2),
           "ztop_hm_p90": float(np.percentile(HM[top], 90)), "leads": []}
    for lb in lead_boxes:
        la, lb_, lc, ld = lb
        m = region(la, lb_, lc, ld) & FIN & (np.nan_to_num(REL) > 0.5)
        if m.sum() < 5:
            res["leads"].append(None)
            continue
        lead = {"box": lb, "x": float(np.median(XX[m])), "y_min": float(YY[m].min() - RES / 2),
                "y_max": float(YY[m].max() + RES / 2), "z_top_p90": float(np.percentile(HM[m], 90)),
                "width_px": float(np.median(m.sum(1)[m.sum(1) > 0]) * RES)}
        # descending part: median y of the lead faces per 0.4 mm z bin, from the board up to 0.6 below the lead top
        fl = fregion(la, lb_, lc, ld, 0.1, lead["z_top_p90"] - 1.0)
        desc = []
        for z_ in np.arange(0.2, lead["z_top_p90"] - 1.0, 0.4):
            k_ = fl & (np.abs(FC[:, 2] - z_) < 0.2)
            if k_.sum() >= 5:
                desc.append([float(np.median(FC[k_, 0])), float(np.median(FC[k_, 1])), float(z_)])
        lead["descent_xyz"] = desc
        res["leads"].append(lead)
    # low parts beside the body that merged into this segment in the top view (shadowed SMD parts)
    side = region(xa - 2.0, xb + 2.0, ya, yb) & FIN & (np.nan_to_num(REL) > 0.25) & (np.nan_to_num(REL) < 1.5) & \
        (np.abs(XX - cx) > r + 0.3)
    lab_, n_ = ndi.label(side)
    res["side_parts"] = []
    for i in range(1, n_ + 1):
        e_ = lab_ == i
        if e_.sum() * RES * RES < 1.0:
            continue
        h_ = float(np.percentile(REL[e_], 90))
        e2 = e_ & (REL > 0.5 * h_)
        res["side_parts"].append([float(XX[e2].min() - RES / 2), float(XX[e2].max() + RES / 2), float(YY[e2].min() - RES / 2),
                                  float(YY[e2].max() + RES / 2), float(np.median(HM[e2 & (REL > 0.8 * h_)]))])
    return res


out["resistor_R1"] = axial_y("R1", (66.3, 71.8, -39.6, -27.2), 4.6, [(67.8, 70.0, -27.2, -21.8), (67.5, 70.5, -45.5, -39.6)])
out["axial_D1"] = axial_y("D1", (66.2, 69.2, -11.6, -5.8), 0.5, [(67.0, 68.8, -5.8, -2.6), (67.0, 68.8, -14.5, -11.6)])
out["axial_D2"] = axial_y("D2", (69.3, 72.3, -11.6, -5.8), 0.5, [(69.6, 71.2, -5.8, -2.6), (69.6, 71.2, -14.5, -11.6)])
out["axial_L2"] = axial_y("L2", (77.6, 81.0, -24.8, -16.8), 0.8, [(78.3, 80.2, -16.8, -11.0)])


# ----------------------------------------------------------------------------- 9. Y-capacitor (tilted disc)
# epoxy-dipped ceramic disc = a flat core disc of radius Rc swept by a sphere of radius rho
# (full-round rim). Robust least squares on the visible surface (leads excluded by z > 6.5).
from scipy.optimize import least_squares
s = fregion(75.5, 89.5, -48.8, -38.6, 6.5, 14.0)
neck = ((FC[:, 1] > -41.5) & (FC[:, 0] > 79.5) & (FC[:, 0] < 84.0)) | \
    ((FC[:, 1] > -43.5) & (FC[:, 0] > 84.5) & (FC[:, 0] < 88.8) & (FC[:, 2] < 9.0))   # epoxy necks onto the leads
tabs = (FC[:, 1] < -45.9) & ((np.abs(FC[:, 0] - 77.74) < 1.3) | (np.abs(FC[:, 0] - 88.1) < 1.3))  # faston blades
s &= ~neck & ~tabs
P = FC[s]
w = FA[s]


def _unit_from_angles(a, b):
    return np.array([np.sin(a) * np.cos(b), np.sin(a) * np.sin(b), np.cos(a)])


def _sdf(prm, X):
    c = prm[:3]
    n_ = _unit_from_angles(prm[3], prm[4])
    Rc, rho = prm[5], prm[6]
    q_ = X - c
    ax_ = q_ @ n_
    rad = np.linalg.norm(q_ - np.outer(ax_, n_), axis=1)
    return np.hypot(np.maximum(rad - Rc, 0.0), ax_) - rho


mu = np.average(P, axis=0, weights=w)
_, _, vt = np.linalg.svd((P - mu) * np.sqrt(w)[:, None], full_matrices=False)
n0 = vt[2] if vt[2][2] > 0 else -vt[2]
fit = None
for tl in (0.8, 1.1, 1.3):          # multi-start on the tilt/azimuth (seedless, deterministic)
    for az in (1.2, 1.5):
        x0_ = np.r_[82.3, -43.5, 7.5, tl, az, 4.5, 2.0]
        f_ = least_squares(lambda prm: _sdf(prm, P) * np.sqrt(w / w.mean()), x0_, loss="soft_l1", f_scale=0.1)
        if fit is None or f_.cost < fit.cost:
            fit = f_
res_ = _sdf(fit.x, P)
nrm = _unit_from_angles(fit.x[3], fit.x[4])
out["ycap_CY1"] = {"centre": fit.x[:3].tolist(), "normal": nrm.tolist(), "core_R": float(fit.x[5]), "rim_rho": float(fit.x[6]),
                   "outer_D": float(2 * (fit.x[5] + fit.x[6])), "thickness": float(2 * fit.x[6]),
                   "tilt_from_z_deg": float(np.degrees(np.arccos(nrm[2]))),
                   "sdf_rms": float(np.sqrt(np.average(res_ ** 2, weights=w))), "sdf_p95_abs": float(np.percentile(np.abs(res_), 95)),
                   "n_faces": int(s.sum()), "method": "robust (soft-L1) SDF fit of a rounded disc to faces z>6.5, epoxy necks and faston blades excluded"}
# Y-cap leads: 3D line fits on vertices in the lead windows
ylead = []
for (xa, xb, ya, yb, za, zb) in [(80.6, 82.2, -39.8, -37.5, 0.4, 5.0), (84.8, 88.8, -43.0, -39.3, 0.4, 5.2)]:
    s = fregion(xa, xb, ya, yb, za, zb)
    Q = FC[s]
    c = Q.mean(0)
    _, _, vt2 = np.linalg.svd(Q - c, full_matrices=False)
    dv = vt2[0] if vt2[0][2] > 0 else -vt2[0]
    t = (Q - c) @ dv
    p_lo, p_hi = c + dv * t.min(), c + dv * t.max()
    perp = np.linalg.norm((Q - c) - np.outer(t, dv), axis=1)
    ylead.append({"p_low": p_lo.tolist(), "p_high": p_hi.tolist(), "perp_p90": float(np.percentile(perp, 90)), "n": int(s.sum())})
out["ycap_leads"] = ylead


# ----------------------------------------------------------------------------- 10. heatsink profile
reg = region(40.5, 56.0, -40.0, -1.5)
top = reg & (np.nan_to_num(HM, nan=-9) > 24.3)
top = ndi.binary_closing(top, iterations=1)
lab_, n_ = ndi.label(top)
top = lab_ == (1 + int(np.argmax(ndi.sum(top, lab_, range(1, n_ + 1)))))
hs = {"top_z_p50": float(np.nanmedian(HM[top])), "top_z_p90": float(np.nanpercentile(HM[top], 90))}
hubs = {}
for nm, gy in (("upper", -7.9), ("lower", -33.4)):
    s = reg & ~FIN & (np.hypot(XX - 48.1, YY - gy) < 2.2)
    lab2, n2 = ndi.label(s)
    s = lab2 == (1 + int(np.argmax(ndi.sum(s, lab2, range(1, n2 + 1)))))
    e = s & ~ndi.binary_erosion(s)
    cx, cy, r, rms = kasa(XX[e], YY[e])
    rq = np.hypot(XX - cx, YY - cy)
    fills = []
    for r0 in np.arange(2.0, 6.0, 0.1):
        ring = reg & FIN & (rq >= r0) & (rq < r0 + 0.1)
        fills.append(float(top[ring].sum() / max(1, ring.sum())))
    fills = np.array(fills)
    r_hub = float(2.0 + 0.1 * np.argmax(fills < 0.8))
    hubs[nm] = {"cx": cx, "cy": cy, "hole_r": r + RES / 2, "hole_rms": rms, "r_hub_fill80": r_hub}
# C-shaped screw channel: the hub is open between the two short fins. Gap = empty run across the
# channel axis (hub centre -> outward, +Y for the upper hub, -Y for the lower) at r = 2.4 .. 3.2
for nm, sgn in (("upper", 1.0), ("lower", -1.0)):
    h_ = hubs[nm]
    runs = []
    for rr_ in np.arange(1.6, 3.3, 0.1):
        yrow = h_["cy"] + sgn * rr_
        j_ = int(round((yrow - Y0) / RES - 0.5))
        row = top[j_]
        i0 = int(round((h_["cx"] - X0) / RES - 0.5))
        if row[i0]:
            continue
        a_ = i0
        while a_ > 0 and not row[a_ - 1]:
            a_ -= 1
        b_ = i0
        while b_ < W - 1 and not row[b_ + 1]:
            b_ += 1
        runs.append((rr_, XS[a_] - RES / 2, XS[b_] + RES / 2))
    runs = np.array(runs)
    h_["channel"] = {"stations": runs.tolist(), "x0": float(np.median(runs[:, 1])), "x1": float(np.median(runs[:, 2])),
                     "method": "empty top-mask run across the channel axis at r 1.6..3.2 from the hub centre (median)"}
hs["hubs"] = hubs
sp = top & (YY < hubs["upper"]["cy"] - 5) & (YY > hubs["lower"]["cy"] + 5) & (XX > 46.5) & (XX < 50.0)
xs_ = np.array([(XS[r_].min() - RES / 2, XS[r_].max() + RES / 2) for r_ in sp if r_.sum() > 3])
hs["spine_x"] = [float(np.median(xs_[:, 0])), float(np.median(xs_[:, 1]))]
arms_m = top.copy()
for h_ in hubs.values():
    arms_m &= np.hypot(XX - h_["cx"], YY - h_["cy"]) > h_["r_hub_fill80"] + 0.9
arms_m &= ~((XX > hs["spine_x"][0] - 0.4) & (XX < hs["spine_x"][1] + 0.4))
lab_, n_ = ndi.label(arms_m)
arms = []
widths = []
raw = []
for i in range(1, n_ + 1):
    s = lab_ == i
    if s.sum() < 40:
        continue
    Pp = np.c_[XX[s], YY[s]]
    mu2 = Pp.mean(0)
    hn = min(hubs, key=lambda k_: np.hypot(mu2[0] - hubs[k_]["cx"], mu2[1] - hubs[k_]["cy"]))
    hc = np.array([hubs[hn]["cx"], hubs[hn]["cy"]])
    Q = Pp - mu2
    wv, vv = np.linalg.eigh(Q.T @ Q)
    dv = vv[:, 1] if vv[:, 1] @ (mu2 - hc) > 0 else -vv[:, 1]
    nv = np.array([-dv[1], dv[0]])
    t, p = Q @ dv, Q @ nv
    ws = [(p[(t >= a) & (t < a + 0.3)].max() - p[(t >= a) & (t < a + 0.3)].min()) + RES
          for a in np.arange(t.min() + 0.8, t.max() - 0.8, 0.3) if ((t >= a) & (t < a + 0.3)).sum() > 3]
    wmed = float(np.median(ws)) if len(ws) >= 2 else None
    if wmed:
        widths.append(wmed)
    if t.max() - t.min() < 2.5:   # short fin: its stub outside the hub is too short for PCA
        a0 = np.arctan2(mu2[1] - hc[1], mu2[0] - hc[0])
        thq = np.arctan2(YY - hc[1], XX - hc[0])
        dd = np.angle(np.exp(1j * (thq - a0)))
        Pw = np.c_[XX[top & (np.abs(dd) < np.radians(14)) & (np.hypot(XX - hc[0], YY - hc[1]) > hubs[hn]["hole_r"] + 0.9)],
                   YY[top & (np.abs(dd) < np.radians(14)) & (np.hypot(XX - hc[0], YY - hc[1]) > hubs[hn]["hole_r"] + 0.9)]]
        for _ in range(3):
            m3 = Pw.mean(0)
            Q3 = Pw - m3
            _, v3 = np.linalg.eigh(Q3.T @ Q3)
            d3 = v3[:, 1] if v3[:, 1] @ (m3 - hc) > 0 else -v3[:, 1]
            n3 = np.array([-d3[1], d3[0]])
            Pw = Pw[np.abs(Q3 @ n3) < 0.8]
        mu2, dv = Pw.mean(0), d3
        nv = np.array([-dv[1], dv[0]])
        Q = Pw - mu2
        t, p = Q @ dv, Q @ nv
        wmed = None
    raw.append((hn, mu2, dv, nv, t, p, wmed))
w_fin = float(np.median(widths))
for hn, mu2, dv, nv, t, p, wmed in raw:
    wv_ = wmed if wmed else w_fin
    # short fins: direction from the hub-side root is unreliable -> keep PCA, width = median fin width
    far = mu2 + dv * t.max()
    tip = far - dv * wv_ / 2
    root = mu2 + dv * t.min() - dv * 1.2     # 1.2 mm back into the hub/spine (overlap for the union)
    arms.append({"hub": hn, "root": [float(root[0]), float(root[1])], "tip": [float(tip[0]), float(tip[1])],
                 "width": float(wv_), "width_measured": wmed is not None,
                 "dir_deg": float(np.degrees(np.arctan2(dv[1], dv[0])))})
arms.sort(key=lambda a: (a["hub"], a["dir_deg"]))
hs["arms"] = arms
hs["fin_width_median"] = w_fin
# profile agreement (IoU of the modelled 2D profile vs the scan top mask), for the record
from shapely.geometry import Point, LineString, box as sbox
from shapely.ops import unary_union
prof = [Point(h_["cx"], h_["cy"]).buffer(h_["r_hub_fill80"], 64) for h_ in hubs.values()]
prof.append(sbox(hs["spine_x"][0], hubs["lower"]["cy"], hs["spine_x"][1], hubs["upper"]["cy"]))
prof += [LineString([a["root"], a["tip"]]).buffer(a["width"] / 2, 32) for a in arms]
prof = unary_union(prof).difference(unary_union([Point(h_["cx"], h_["cy"]).buffer(h_["hole_r"], 64) for h_ in hubs.values()]))
from shapely import contains_xy
inside = contains_xy(prof, XX, YY)
cmp_reg = reg & FIN
iou = float((inside & top & cmp_reg).sum() / max(1, ((inside | top) & cmp_reg).sum()))
hs["profile_iou_vs_top_mask"] = iou
out["heatsink"] = hs

# ----------------------------------------------------------------------------- 11. TO-220 (Q1) on the spine
q = {}
fr = fregion(42.0, 44.2, -26.0, -16.5, 4.5, 16.0) & (FN[:, 0] < -0.85)
q["body_front_x_all"] = float(np.median(FC[fr, 0]))
frt = fr & (FC[:, 2] > 13.7) & (FC[:, 2] < 14.9)   # above the clip strap: the strap's inner face is not the body
q["body_front_x"] = float(np.median(FC[frt, 0]))
q["body_front_n_faces"] = int(frt.sum())
q["body_bottom_z"] = float(np.percentile(FC[fr, 2], 1))
bt = region(43.2, 45.7, -26.0, -16.8) & FIN & (np.nan_to_num(HM) > 13.8) & (np.nan_to_num(HM) < 16.5)
q["body_top_z"] = float(np.median(HM[bt]))
by = region(42.6, 46.1, -28.0, -14.0) & FIN & (np.nan_to_num(HM) > 13.8) & (np.nan_to_num(HM) < 16.5)
q["body_y0"] = float(np.percentile(YY[by], 1) - RES / 2)
q["body_y1"] = float(np.percentile(YY[by], 99) + RES / 2)
tb = region(46.0, hs["spine_x"][0] + 0.05, -26.5, -16.0) & FIN & (np.nan_to_num(HM) > 16.5) & (np.nan_to_num(HM) < 23.5)
q["tab_top_z_hm_p50"] = float(np.median(HM[tb]))
tf = fregion(45.5, 46.9, -26.5, -16.0, 15.8, 23.0) & (FN[:, 0] < -0.85)
q["tab_front_x"] = float(np.median(FC[tf, 0]))
q["tab_top_z_faces_p99"] = float(np.percentile(FC[tf, 2], 99))
q["tab_y0"] = float(np.percentile(FC[tf, 1], 0.5))
q["tab_y1"] = float(np.percentile(FC[tf, 1], 99.5))
q["tab_hole_occupancy"] = face_hole(tf, 1, -27.0, -15.0, 15.5, 23.0)
# screw hole through tab + spine: bore-wall faces inside the spine (normal perpendicular to X), IRLS circle in (y, z)
hb = fregion(47.6, 49.0, -22.6, -18.9, 16.0, 18.6) & (np.abs(FN[:, 0]) < 0.3)   # only the lower arc is scanned
hy_, hz_, hr_, hrms_ = irls_circle(FC[hb, 1], FC[hb, 2], FA[hb], scale=0.1)
tw = fregion(46.1, 47.45, -23.6, -18.9, 16.0, 21.0) & (np.abs(FN[:, 0]) < 0.3)
ty_, tz_, tr_, trms_ = irls_circle(FC[tw, 1], FC[tw, 2], FA[tw], scale=0.1)
q["tab_hole_in_tab"] = {"u": ty_, "z": tz_, "d_fit": 2 * tr_, "fit_rms": trms_, "n_faces": int(tw.sum()),
                        "method": "IRLS circle (Cauchy 0.1) in (y, z) on the bore-wall faces inside the tab (x 46.1..47.45)"}
q["tab_hole"] = {"u": hy_, "z": hz_, "d_fit": 2 * hr_, "fit_rms": hrms_, "n_faces": int(hb.sum()),
                 "method": "IRLS circle (Cauchy 0.1) in (y, z) on the bore-wall faces inside the spine (x 47.6..49.0); only the lower arc (z < 18.6) is scanned"}
# spine face seen below the tab: the tab (and package back) stands off the spine below this z
# the package back (tab back face, normal +X) is visible from +X below the heatsink spine:
# the spine has a notch there. Tab back x = median of those faces; notch = their y/z extent.
tbk = fregion(46.8, 48.2, -27.0, -15.5, 3.0, 13.0) & (FN[:, 0] > 0.85)
q["tab_back_x"] = float(np.median(FC[tbk, 0]))
q["spine_notch"] = {"y0": float(np.percentile(FC[tbk, 1], 1)), "y1": float(np.percentile(FC[tbk, 1], 99)),
                    "z_top": float(np.percentile(FC[tbk, 2], 98)), "z_min_seen": float(np.percentile(FC[tbk, 2], 2)),
                    "n_faces": int(tbk.sum()),
                    "method": "+X-facing faces at x 46.8..48.2 below z 13 (package back seen through the spine notch)"}
# leads: faces below the body, cluster in y
lf = fregion(42.5, 46.0, -25.5, -16.5, 0.4, 3.6)
ly = FC[lf, 1]
leads = []
for yc in (-23.6, -21.1, -18.6):
    m_ = lf & (np.abs(FC[:, 1] - yc) < 0.9)
    if m_.sum() > 10:
        leads.append({"y": float(np.median(FC[m_, 1])), "x": float(np.median(FC[m_, 0])),
                      "y_span_p5_p95": r3(np.percentile(FC[m_, 1], [5, 95]))})
# lead paths (bent forward to the board): median x per 0.5 mm z bin, per lead
for l_ in leads:
    m_ = fregion(39.0, 45.8, l_["y"] - 0.6, l_["y"] + 0.6, 0.15, 5.6)
    prof_ = []
    for z_ in np.arange(0.25, 5.6, 0.5):
        k_ = m_ & (np.abs(FC[:, 2] - z_) < 0.25)
        if k_.sum() >= 5:
            prof_.append([float(np.median(FC[k_, 0])), float(z_)])
    l_["path_xz"] = prof_
q["leads"] = leads
out["to220_Q1"] = q

# ----------------------------------------------------------------------------- 12. spring clip (strap)
reg2 = region(38.8, 55.2, -41.3, -1.2)
strap = reg2 & FIN & (np.nan_to_num(HM) > 12.3) & (np.nan_to_num(HM) < 14.3)
strap = ndi.binary_opening(strap, iterations=1)
lab_, n_ = ndi.label(strap)
strap = lab_ == (1 + int(np.argmax(ndi.sum(strap, lab_, range(1, n_ + 1)))))
dist = ndi.distance_transform_edt(strap) * RES
sk = skeletonize(strap)
thick_px = 2 * dist[sk]
# order skeleton pixels into a path: start at an end point, greedy walk
yx = np.argwhere(sk)
from scipy.spatial import cKDTree
tree = cKDTree(yx)
nb = [len(tree.query_ball_point(p_, 1.5)) - 1 for p_ in yx]
ends = [i for i, c in enumerate(nb) if c == 1]
start = max(ends, key=lambda i: XS[yx[i][1]] + YS[yx[i][0]]) if ends else 0  # top-right end first
path = [start]
used = {start}
cur = start
while True:
    cands = [j for j in tree.query_ball_point(yx[cur], 1.5) if j not in used]
    if not cands:
        cands = [j for j in tree.query_ball_point(yx[cur], 3.0) if j not in used]
        if not cands:
            break
    j = min(cands, key=lambda j_: np.linalg.norm(yx[j_] - yx[cur]))
    path.append(j)
    used.add(j)
    cur = j
pp = np.c_[XS[yx[path, 1]], YS[yx[path, 0]]]
ls = LineString(pp).simplify(0.25)
verts = np.array(ls.coords)
side = fregion(38.8, 55.2, -41.3, -1.2, 5.5, 14.5) & (np.abs(FN[:, 2]) < 0.3)
strap_band = np.zeros(len(FC), bool)
for a_, b_ in zip(verts[:-1], verts[1:]):
    seg = LineString([a_, b_])
    near_ = side & (np.abs(FC[:, 0] - (a_[0] + b_[0]) / 2) < abs(a_[0] - b_[0]) / 2 + 0.8) & \
        (np.abs(FC[:, 1] - (a_[1] + b_[1]) / 2) < abs(a_[1] - b_[1]) / 2 + 0.8)
    idx = np.where(near_)[0]
    dd = np.array([seg.distance(Point(FC[k_, 0], FC[k_, 1])) for k_ in idx]) if len(idx) else np.array([])
    strap_band[idx[dd < 0.7]] = True
# lower hook: the strap wraps the lower-right short fin tip below the top-view strap band
sec = M.section(plane_origin=[0, 0, 10.0], plane_normal=[0, 0, 1])
hook = None
if sec is not None:
    best_h = None
    for e_ in sec.entities:
        pp_ = sec.vertices[e_.points][:, :2]
        k_ = (pp_[:, 0] > 48.0) & (pp_[:, 0] < 51.2) & (pp_[:, 1] > -38.9) & (pp_[:, 1] < -36.3)
        if k_.sum() >= 5 and (best_h is None or k_.sum() > best_h[0]):
            best_h = (int(k_.sum()), pp_[k_])      # chain order kept (section polyline order)
    if best_h is not None:
        hk = LineString(best_h[1]).simplify(0.25)
        hook = {"outer_surface_vertices": np.array(hk.coords).tolist(), "section_z": 10.0,
                "method": "section z 10 of the scan in x 48.0..51.2, y -38.9..-36.3 (strap outer surface around the fin tip), DP 0.25"}
out["clip_S1_hook"] = hook
out["clip_S1"] = {"path_vertices": verts.tolist(), "n_skeleton_px": int(len(path)), "n_skeleton_total": int(sk.sum()),
                  "top_z_p90": float(np.percentile(HM[strap], 90)), "top_z_p50": float(np.median(HM[strap])),
                  "bottom_z_p2": float(np.percentile(FC[strap_band, 2], 2)) if strap_band.any() else None,
                  "width_topview_p50": float(np.median(thick_px)), "simplify_tol_mm": 0.25}

# ----------------------------------------------------------------------------- 13. cluster audit (CHK-CLUSTER)
owned = {s_["owner"] for s_ in segs if s_["owner"]}
out["cluster_audit"] = {"n_segments": len(segs), "n_auto_boxes": len(boxes),
                        "owners": sorted(owned), "unowned_nonbox": []}

hdr = {"schema": "stl-re/pcb_measure@1", "tool": "measure/measure_pcb.py", "tool_version": "run-local@1",
       "inputs": {"intake/aligned_work.stl": sha(MESH_P), "intake/alignment.json": sha(ALIGN_P)},
       "seed": SEED, "created": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")}


def clean(o):
    if isinstance(o, dict):
        return {k_: clean(v) for k_, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else round(float(o), 4)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


(FIG / "pcb_measure.json").write_text(json.dumps({**hdr, **clean(out)}, indent=1))
print("wrote", FIG / "pcb_measure.json")

# ----------------------------------------------------------------------------- overview figure
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle, Circle
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.imshow(HM, origin="lower", extent=[X0, X1, Y0, Y1], cmap="gray", vmin=-0.5, vmax=15)
    for b_ in boxes:
        ax.add_patch(Rectangle((b_["x0"], b_["y0"]), b_["x1"] - b_["x0"], b_["y1"] - b_["y0"], fill=False, ec="lime", lw=0.6))
    for c in out["caps"]:
        ax.add_patch(Circle((c["cx"], c["cy"]), c["r"], fill=False, ec="red", lw=0.8))
    for a in arms:
        ax.plot([a["root"][0], a["tip"][0]], [a["root"][1], a["tip"][1]], "c-", lw=1)
    v_ = np.array(out["clip_S1"]["path_vertices"])
    ax.plot(v_[:, 0], v_[:, 1], "m.-", lw=0.8, ms=3)
    for hn, h_ in holes.items():
        ax.add_patch(Circle((h_["cx"], h_["cy"]), h_["r_raster"], fill=False, ec="yellow", lw=0.8))
    ax.set_xlim(X0, X1)
    ax.set_ylim(Y0, Y1)
    ax.set_title("OD-E01 measurement overview (datum frame): boxes green, caps red, fins cyan, clip magenta, holes yellow")
    fig.savefig(FIG / "overview.png", dpi=110, bbox_inches="tight")
except Exception as exc:  # figure is optional
    print("figure skipped:", exc)
