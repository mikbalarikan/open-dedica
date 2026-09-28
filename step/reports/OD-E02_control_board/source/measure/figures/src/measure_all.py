#!/usr/bin/env python3
"""measure_all.py - OD-E02 control button board: every scan measurement behind measure/params.json.

Run from the run folder:  python3 measure/figures/src/measure_all.py
Reads  intake/aligned_work.stl (datum frame, frozen alignment.json), writes measure/figures/m_all.json.
Deterministic (seed 0 for surface samples). No value here is a CAD choice: make_params.py applies the
rules. Estimators are named per group in the JSON ("estimator" keys).
Frame: datum frame of intake/alignment.json; theta CCW about +Z from +X.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import trimesh
from shapely import distance, points
from shapely.geometry import Polygon

RUN = Path.cwd()
MESH = RUN / "intake/aligned_work.stl"
OUT = RUN / "measure/figures/m_all.json"
m = trimesh.load(MESH)
C, N, A = m.triangles_center, m.face_normals, m.area_faces


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sect(z: float, normal=(0, 0, 1), axis=2) -> np.ndarray:
    o = np.zeros(3)
    o[axis] = z
    s = m.section(plane_origin=o, plane_normal=normal)
    if s is None:
        return np.zeros((0, 3))
    return np.vstack([s.vertices[e.points] for e in s.entities])


def kasa(p: np.ndarray) -> dict:
    Aa = np.c_[2 * p, np.ones(len(p))]
    b = (p ** 2).sum(1)
    c = np.linalg.lstsq(Aa, b, rcond=None)[0]
    r = float(np.sqrt(c[2] + c[0] ** 2 + c[1] ** 2))
    res = np.hypot(*(p - c[:2]).T) - r
    return {"cx": float(c[0]), "cy": float(c[1]), "r": r, "rms": float(np.sqrt((res ** 2).mean())),
            "n": int(len(p))}


def ellipse(p: np.ndarray) -> dict:
    """Geometric-ish least-squares ellipse: residual = (sqrt((x'/a)^2+(y'/b)^2) - 1) * sqrt(a*b),
    solved with scipy least_squares from the Kasa circle start. a = semi-axis along the rotated x'."""
    from scipy.optimize import least_squares
    k = kasa(p)

    def res(t):
        cx, cy, a, b, ph = t
        c, s_ = np.cos(ph), np.sin(ph)
        x = (p[:, 0] - cx) * c + (p[:, 1] - cy) * s_
        y = -(p[:, 0] - cx) * s_ + (p[:, 1] - cy) * c
        return (np.sqrt((x / a) ** 2 + (y / b) ** 2) - 1.0) * np.sqrt(abs(a * b))

    sol = least_squares(res, [k["cx"], k["cy"], k["r"], k["r"] * 1.02, 0.0], loss="soft_l1", f_scale=0.1)
    cx, cy, a, b, ph = sol.x
    r = res(sol.x)
    return {"cx": float(cx), "cy": float(cy), "a_xprime": float(abs(a)), "b_yprime": float(abs(b)),
            "phi_deg": float(np.degrees(ph)), "rms": float(np.sqrt((r ** 2).mean())), "n": int(len(p))}


def plane_fit(sel: np.ndarray, n0, trim=0.12, iters=5) -> dict:
    P, w = C[sel], A[sel]
    keep = np.ones(len(P), bool)
    n0 = np.asarray(n0, float) / np.linalg.norm(n0)
    for _ in range(iters):
        c = (P[keep] * w[keep, None]).sum(0) / w[keep].sum()
        _, _, Vt = np.linalg.svd((P[keep] - c) * np.sqrt(w[keep])[:, None], full_matrices=False)
        n = Vt[2] if Vt[2] @ n0 > 0 else -Vt[2]
        d = (P - c) @ n
        keep = np.abs(d) < trim
    return {"normal": n.tolist(), "point": c.tolist(), "offset": float(n @ c),
            "rms": float(np.sqrt((d[keep] ** 2).mean())), "n_faces": int(keep.sum()),
            "area_mm2": float(w[keep].sum()), "angle_to_z_deg": float(np.degrees(np.arccos(abs(n[2]))))}


def zlevel(nz_sign: int, zlo: float, zhi: float, extra=None) -> dict:
    sel = (N[:, 2] * nz_sign > 0.985) & (C[:, 2] > zlo) & (C[:, 2] < zhi)
    if extra is not None:
        sel &= extra
    z, w = C[sel, 2], A[sel]
    med = float(np.median(z))
    k = np.abs(z - med) < 0.1
    return {"z": float(np.average(z[k], weights=w[k])), "z_p05_p95": [float(np.percentile(z[k], 5)),
            float(np.percentile(z[k], 95))], "area_mm2": float(w[k].sum()), "n_faces": int(k.sum())}


R = {"estimator_notes": {}, "frame": "datum frame of intake/alignment.json; theta CCW about +Z from +X"}

# ------------------------------------------------------------------ z levels (flat-face histogram peaks)
R["z"] = {
    "rim_top": zlevel(+1, 4.7, 5.3, np.hypot(C[:, 0], C[:, 1]) > 0),
    "floor": zlevel(+1, -0.2, 0.2),
    "T0_bottom": zlevel(-1, -7.7, -7.45),
    "T2_bottom": zlevel(-1, -10.3, -9.95),
    "T3_bottom": zlevel(-1, -13.35, -13.0),
    "band_bottom": zlevel(-1, -16.3, -15.95),
    "collar_bottom": zlevel(-1, -19.3, -18.95),
    "hoop_bottom": zlevel(-1, -5.75, -5.4),
    "shroud_top": zlevel(+1, 10.3, 10.7),
    "tab_top": zlevel(+1, 18.7, 19.2),
    "tab_under": zlevel(-1, 16.2, 16.6),
    "screw_cb_floor": zlevel(+1, -3.1, -2.7),
}
R["estimator_notes"]["z"] = "area-weighted mean z of faces with |n.z|>0.985 in a 0.3-0.5 mm window around each flat-face histogram peak, trimmed to +-0.1 of the median"

# ------------------------------------------------------------------ housing core corners (constant across tiers)
EDGES = {"xmin": [0, -12, -2, "min"], "xmax": [0, -12, -2, "max"], "ymin": [1, -30, -18, "min"],
         "ymaxL": [1, -33, -28, "max"], "ymaxR": [1, 20, 30, "max"], "bumpy": [1, -12, 2, "max"],
         "bxL": [0, 9, 11, "min"], "bxR": [0, 9, 11, "max"]}
CORN = {"BL": ["xmin", "ymin", 1, 1, 4], "BR": ["xmax", "ymin", -1, 1, 4], "TL": ["xmin", "ymaxL", 1, -1, 4],
        "TR": ["xmax", "ymaxR", -1, -1, 4], "bumpTL": ["bxL", "bumpy", 1, -1, 3], "bumpTR": ["bxR", "bumpy", -1, -1, 3]}


def edge(P, axis, lo, hi, which):
    o = 1 - axis
    s = (P[:, o] > lo) & (P[:, o] < hi)
    v = P[s, axis]
    return float(np.median(v[v < np.percentile(v, 3) + 0.15]) if which == "min"
                 else np.median(v[v > np.percentile(v, 97) - 0.15]))


corner_runs = []
for z in (-3.0, -4.5, -6.6, -9.0):
    P = sect(z)[:, :2]
    E = {k: edge(P, *v) for k, v in EDGES.items()}
    row = {"z": z}
    for name, (ex, ey, sx, sy, R0) in CORN.items():
        x0, y0 = E[ex], E[ey]
        xs = sorted([x0, x0 + sx * 1.3 * R0])
        ys = sorted([y0, y0 + sy * 1.3 * R0])
        s = (P[:, 0] > xs[0] - 0.3) & (P[:, 0] < xs[1]) & (P[:, 1] > ys[0] - 0.3) & (P[:, 1] < ys[1])
        q = P[s]
        q = q[(np.abs(q[:, 0] - x0) > 0.06) & (np.abs(q[:, 1] - y0) > 0.06)]
        row[name] = kasa(q)
    corner_runs.append(row)
core = {}
for name in CORN:
    cx = [r[name]["cx"] for r in corner_runs]
    cy = [r[name]["cy"] for r in corner_runs]
    core[name] = {"xy": [float(np.median(cx)), float(np.median(cy))],
                  "spread_mm": [float(np.ptp(cx)), float(np.ptp(cy))],
                  "radii_by_z": {str(r["z"]): r[name]["r"] for r in corner_runs},
                  "rms_by_z": {str(r["z"]): r[name]["rms"] for r in corner_runs}}
R["core"] = core
R["estimator_notes"]["core"] = ("Kasa circle on each outline corner arc (points > 0.06 from both straight edges) at "
                               "z -3, -4.5, -6.6, -9; centre = median over the 4 stations (tiers are offsets of one core)")

BL, BR, TR, TL = (core[k]["xy"] for k in ("BL", "BR", "TR", "TL"))
bTL, bTR = core["bumpTL"]["xy"], core["bumpTR"]["xy"]
main_core = Polygon([BL, BR, TR, TL])
ytop_at = lambda x: TL[1] + (TR[1] - TL[1]) * (x - TL[0]) / (TR[0] - TL[0])
bump_core = Polygon([(bTL[0], ytop_at(bTL[0]) - 1.0), (bTR[0], ytop_at(bTR[0]) - 1.0), bTR, bTL])


def offsets(z: float, inner=False) -> dict:
    P = sect(z)[:, :2]
    pp = points(P)
    dm = np.asarray(distance(main_core, pp))
    db = np.asarray(distance(bump_core, pp))
    d = np.minimum(dm, db)
    out = {}
    if inner:
        return {"d_all": d}
    med = np.median(d)
    keep = np.abs(d - med) < 1.2
    isb = (db < dm) & keep & (P[:, 1] > ytop_at(P[:, 0]) + 2.0)
    ism = (dm <= db) & keep
    for lab, sel in [("main", ism), ("main_mY", ism & (P[:, 1] < -13.2)), ("main_pY", ism & (P[:, 1] > 1.3)),
                     ("main_mX", ism & (P[:, 0] < -33)), ("main_pX", ism & (P[:, 0] > 32.4)), ("bump", isb)]:
        v = d[sel]
        if len(v) > 5:
            out[lab] = float(np.median(v))
    return out


def tier(zs, drop_mY=False):
    rows = [offsets(z) for z in zs]
    keys_main = ["main_pY", "main_mX", "main_pX"] + ([] if drop_mY else ["main_mY"])
    mains = [r[k] for r in rows for k in keys_main if k in r]
    bumps = [r["bump"] for r in rows if "bump" in r]
    return {"stations_z": list(zs), "R_main": float(np.median(mains)), "R_main_spread": float(np.ptp(mains)),
            "R_bump": float(np.median(bumps)), "R_bump_spread": float(np.ptp(bumps)), "per_station": rows}


R["tiers"] = {
    "T0": tier([-1.0, -2.0, -3.0, -4.0, -5.0, -6.0]),
    "T2": tier([-8.2, -8.8, -9.4, -9.8]),
    "T3": tier([-10.6, -11.2, -11.8, -12.4], drop_mY=True),
    "rim_out": tier([1.0, 1.8, 2.6, 3.4]),
}
R["estimator_notes"]["tiers"] = ("median distance of section-outline points to the core polygon, per side (main) and "
                                "on the bump; clips/tab excluded by a 1.2 mm window around the median")

# rim pocket inner wall: histogram peaks of distances below the outer wall
inn = []
for z in (1.0, 1.8, 2.6, 3.4):
    d = offsets(z, inner=True)["d_all"]
    inn.append(d)
d = np.concatenate(inn)
h, e = np.histogram(d, bins=np.arange(3.8, 5.0, 0.02))
R["rim_in"] = {"R_main": float(e[np.argmax(h)] + 0.01),
               "note": "mode of outline-to-core distances in 3.8..5.0 (inner rim wall) at z 1..3.4"}
# bump inner: points near the bump top (y>ytop+5)
inb = []
for z in (1.0, 1.8, 2.6, 3.4):
    P = sect(z)[:, :2]
    s = (P[:, 0] > -8) & (P[:, 0] < 4) & (P[:, 1] > 11.9) & (P[:, 1] < 13.9)
    inb += list(P[s, 1] - np.interp(P[s, 0], [bTL[0], bTR[0]], [bTL[1], bTR[1]]))
R["rim_in"]["R_bump"] = float(np.median(inb))

# concave junction fillets (main top edge meets bump side wall), per tier
def concave(z, Rm, Rb):
    P = sect(z)[:, :2]
    res = {}
    for side, bx, sx in (("L", bTL[0], -1), ("R", bTR[0], 1)):
        xw = bx + sx * Rb          # bump side wall x
        yw = ytop_at(xw + sx * 2) + Rm  # main top wall y
        s = (np.abs(P[:, 0] - (xw + sx * 1.2)) < 1.4) & (P[:, 1] > yw - 0.3) & (P[:, 1] < yw + 2.8)
        q = P[s]
        q = q[(np.abs(q[:, 0] - xw) > 0.08) & (np.abs(q[:, 1] - yw) > 0.08)]
        q = q[(q[:, 0] - xw) * sx > 0]
        res[side] = kasa(q) if len(q) > 6 else None
    return res


R["concave"] = {
    "T0": concave(-4.0, R["tiers"]["T0"]["R_main"], R["tiers"]["T0"]["R_bump"]),
    "T2": concave(-9.0, R["tiers"]["T2"]["R_main"], R["tiers"]["T2"]["R_bump"]),
    "T3": concave(-11.8, R["tiers"]["T3"]["R_main"], R["tiers"]["T3"]["R_bump"]),
}

# rim junction radii (z 1/2/3): outer concave fillet and the pocket (inner wall) junction fillet
def rim_junctions():
    res = {"outer": {"L": [], "R": []}, "pocket": {"L": [], "R": []}}
    Rmo, Rbo = R["tiers"]["rim_out"]["R_main"], R["tiers"]["rim_out"]["R_bump"]
    Rmi, Rbi = R["rim_in"]["R_main"], R["rim_in"]["R_bump"]
    for z in (1.0, 2.0, 3.0):
        P = sect(z)[:, :2]
        d = np.minimum(np.asarray(distance(main_core, points(P))), np.asarray(distance(bump_core, points(P))))
        for side, bx, sx in (("L", bTL[0], -1), ("R", bTR[0], 1)):
            xw, yw = bx + sx * Rbo, ytop_at(bx + sx * Rbo) + Rmo
            sel = ((P[:, 0] - xw) * sx > 0.08) & ((P[:, 0] - xw) * sx < 3.4) & (P[:, 1] > yw + 0.08) & (P[:, 1] < yw + 3.4) & (d > 5.2)
            if sel.sum() > 6:
                res["outer"][side].append(kasa(P[sel]))
            xw, yw = bx + sx * Rbi, ytop_at(bx + sx * Rbi) + Rmi
            sel = ((P[:, 0] - xw) * sx > 0.08) & ((P[:, 0] - xw) * sx < 3.5) & (P[:, 1] > yw + 0.08) & (P[:, 1] < yw + 3.5) & (d < 5.0) & (d > 3.5)
            if sel.sum() > 6:
                res["pocket"][side].append(kasa(P[sel]))
    return res


R["rim_junctions"] = rim_junctions()

# ------------------------------------------------------------------ -Y chamfer plane
n0 = np.array([0, -1, -1]) / np.sqrt(2)
R["chamfer"] = plane_fit((N @ n0 > 0.97) & (C[:, 2] < -10) & (C[:, 2] > -17) & (C[:, 1] < -8), n0)

# ------------------------------------------------------------------ button band (z -13.2..-16.1)
Pb = sect(-14.4)[:, :2]
band = {}
for side, lo, hi in (("L", -22, -10), ("R", 10, 22)):
    s = (Pb[:, 0] > lo) & (Pb[:, 0] < hi) & (Pb[:, 1] > 0)
    b, a = np.polyfit(Pb[s, 0], Pb[s, 1], 1)
    band["top_line_" + side] = {"a": float(a), "b": float(b), "y_at_x": float(a + b * (lo + hi) / 2)}
for side, sel in (("L", Pb[:, 0] < -28.5), ("R", Pb[:, 0] > 28.5)):
    band["end_disk_" + side] = kasa(Pb[sel])
band["mid_disk"] = kasa(Pb[(np.abs(Pb[:, 0]) < 5) & (Pb[:, 1] > 4)])
R["band"] = band

# ------------------------------------------------------------------ collars + caps
v, _ = trimesh.sample.sample_surface(m, 400000, seed=0)


def stations(center, rlo, rhi, zs):
    out = []
    for z in zs:
        P = sect(z)[:, :2]
        q = P - center
        s = (np.hypot(*q.T) > rlo) & (np.hypot(*q.T) < rhi)
        if s.sum() > 40:
            k = kasa(P[s])
            out.append({"z": float(z), **k})
    return out


def axis_line(st):
    z = np.array([s["z"] for s in st])
    cx = np.array([s["cx"] for s in st])
    cy = np.array([s["cy"] for s in st])
    bx, ax = np.polyfit(z, cx, 1)
    by, ay = np.polyfit(z, cy, 1)
    d = np.array([bx, by, 1.0])
    d /= np.linalg.norm(d)
    return {"dir": d.tolist(), "tilt_deg": float(np.degrees(np.arccos(d[2]))),
            "tilt_dir_deg": float(np.degrees(np.arctan2(by, bx))), "xy_at_z0": [float(ax), float(ay)]}


caps = {}
cB2 = stations(np.array([0.0, 0.0]), 5.5, 7.2, np.linspace(-28.6, -19.8, 12))
caps["B2"] = {"stations": cB2, "r": float(np.median([s["r"] for s in cB2])), "axis": axis_line(cB2)}
sel = (N[:, 2] < -0.97) & (C[:, 2] < -28.7) & (np.hypot(C[:, 0], C[:, 1]) < 5.8)
caps["B2"]["top"] = plane_fit(sel, [0, 0, -1], trim=0.08)
for name, c0, sgn in (("B1", np.array([-26.6, -4.8]), -1), ("B3", np.array([26.5, -5.2]), 1)):
    st = stations(c0, 5.3, 7.0, np.linspace(-21.6, -19.4, 7))
    els = []
    for z in np.linspace(-21.2, -19.4, 6):
        P = sect(z)[:, :2]
        q = P - c0
        k = (np.hypot(*q.T) > 5.3) & (np.hypot(*q.T) < 7.0)
        els.append({"z": float(z), **ellipse(P[k])})
    caps[name] = {"stations": st, "r": float(np.median([s["r"] for s in st])), "axis": axis_line(st),
                  "centre_median": [float(np.median([s["cx"] for s in st])), float(np.median([s["cy"] for s in st]))],
                  "ellipse_stations": els,
                  "ellipse": {k: float(np.median([e[k] for e in els])) for k in ("cx", "cy", "a_xprime", "b_yprime", "phi_deg", "rms")}}
    # inclined top face: outward normal (sgn*0.3, 0, -0.95) (top rises toward the outer end)
    nt = np.array([sgn * 0.3, 0.0, -0.95])
    q = C[:, :2] - np.array(caps[name]["centre_median"])
    sel = (N @ (nt / np.linalg.norm(nt)) > 0.97) & (np.hypot(*q.T) < 5.6) & (C[:, 2] < -20.5)
    caps[name]["top"] = plane_fit(sel, nt, trim=0.08)
R["caps"] = caps
coll = {}
coll["B2"] = {"stations": stations(np.array([0.0, 0.0]), 7.6, 8.8, np.linspace(-18.7, -16.4, 9))}
coll["B2"]["r"] = float(np.median([s["r"] for s in coll["B2"]["stations"]]))
for name, c0 in (("B1", np.array(caps["B1"]["centre_median"])), ("B3", np.array(caps["B3"]["centre_median"]))):
    st = stations(c0, 7.4, 9.2, np.linspace(-18.7, -16.5, 6))
    coll[name] = {"stations": st, "r": float(np.median([s["r"] for s in st])),
                  "centre_median": [float(np.median([s["cx"] for s in st])), float(np.median([s["cy"] for s in st]))]}
    # outer-sector gap: angles where the ring has no points at z -17.2
    P = sect(-17.2)[:, :2] - c0
    rr = np.hypot(*P.T)
    th = np.degrees(np.arctan2(P[:, 1], P[:, 0])) % 360
    ring = th[(rr > 7.4) & (rr < 9.0)]
    hist, e = np.histogram(ring, bins=np.arange(0, 361, 2))
    empty = e[:-1][hist == 0]
    coll[name]["gap_bins_deg"] = empty.tolist()
    # floor of the cut sector (-z faces near z -15.1 within r<8.4 of the axis)
    q = C[:, :2] - c0
    s2 = (N[:, 2] < -0.985) & (C[:, 2] > -15.6) & (C[:, 2] < -14.6) & (np.hypot(*q.T) < 8.4)
    coll[name]["sector_floor"] = {"z": float(np.median(C[s2, 2])), "area_mm2": float(A[s2].sum()),
                                  "theta_p05_p95": np.percentile(np.degrees(np.arctan2(q[s2, 1], q[s2, 0])) % 360, [5, 95]).tolist()}
# outer-side collar cut: the ring's lower boundary z(theta) (1st percentile z per 4-deg bin, ring r 7.6..8.7)
# follows a tilted plane; fit z = a + b*(x - cx) + c*(y - cy) to the boundary points above the collar bottom
for name in ("B1", "B3"):
    cx_, cy_, rr_ = coll[name]["centre_median"] + [coll[name]["r"]]
    q = v[:, :2] - np.array([cx_, cy_])
    rv = np.hypot(*q.T)
    th = np.degrees(np.arctan2(q[:, 1], q[:, 0])) % 360
    k = (rv > 7.6) & (rv < 8.7) & (v[:, 2] < -14.8) & (v[:, 2] > -19.4)
    bpts = []
    outward = 180.0 if name == "B1" else 0.0   # outer side of the housing end (-X for B1, +X for B3)
    for b in np.arange(0, 360, 4):
        if abs(((b + 2 - outward + 180) % 360) - 180) > 100:   # outer half-ring only (inner side is the band bar)
            continue
        sb = k & (th >= b) & (th < b + 4)
        if sb.sum() > 10:
            zb = np.percentile(v[sb, 2], 1)
            if zb > -18.9:
                i = np.argmin(np.abs(v[sb, 2] - zb))
                bpts.append(v[sb][i])
    bp = np.array(bpts)
    # bins whose ring boundary sits within 0.45 of the flat floor: the floor sector
    thb = (np.degrees(np.arctan2(bp[:, 1] - cy_, bp[:, 0] - cx_)) - outward + 180) % 360 - 180
    fl = thb[bp[:, 2] > coll[name]["sector_floor"]["z"] - 0.45]
    coll[name]["floor_sector_deg"] = [float(fl.min() + outward - 2.0), float(fl.max() + outward + 2.0)]
    Mx = np.c_[np.ones(len(bp)), bp[:, 0] - cx_, bp[:, 1] - cy_]
    coef, *_ = np.linalg.lstsq(Mx, bp[:, 2], rcond=None)
    res = bp[:, 2] - Mx @ coef
    nrm = np.array([-coef[1], -coef[2], 1.0])
    nrm /= np.linalg.norm(nrm)
    coll[name]["cut_plane"] = {"a": float(coef[0]), "b": float(coef[1]), "c": float(coef[2]), "n_pts": int(len(bp)),
                               "rms": float(np.sqrt((res ** 2).mean())), "max": float(np.abs(res).max()),
                               "normal_up": nrm.tolist(), "offset": float(nrm @ np.array([cx_, cy_, coef[0]])),
                               "tilt_deg": float(np.degrees(np.arccos(nrm[2])))}
# bore recess between each cap and its collar (clearance around the moving cap); denser samples (seed 0)
v, _ = trimesh.sample.sample_surface(m, 1500000, seed=0)
rec = {}
for name, c0, outward in (("B2", np.array([0.0, 0.0]), None), ("B1", np.array(coll["B1"]["centre_median"]), 180.0),
                          ("B3", np.array(coll["B3"]["centre_median"]), 0.0)):
    q = v[:, :2] - c0
    rv = np.hypot(*q.T)
    base = (rv > 6.45) & (rv < 7.7) & (v[:, 2] > -19.0) & (v[:, 2] < -14.5)
    r_out = float(np.percentile(rv[base & (v[:, 2] > -18.95) & (v[:, 2] < -17.9)], 97))
    if outward is None:
        rec[name] = {"r": r_out, "top_z": float(np.percentile(v[base, 2], 95))}
    else:
        th = (np.degrees(np.arctan2(q[:, 1], q[:, 0])) - outward + 180) % 360 - 180
        inner = base & (np.abs(th) > 90)
        outer = base & (np.abs(th) < 60)
        # sector where the recess is open up to the floor: 10-deg bins whose 90th-pct z is within 0.6 of the floor
        zf = coll[name]["sector_floor"]["z"]
        k7 = (rv > 6.5) & (rv < 7.3) & (v[:, 2] > -19.0) & (v[:, 2] < -14.4)
        ok = []
        for b in range(-120, 120, 10):
            sb = k7 & (th >= b) & (th < b + 10)
            if sb.sum() > 5 and np.percentile(v[sb, 2], 90) >= zf - 0.6:
                ok.append(b)
        # recess ceiling ramp: per 10-deg bin 90th-pct z (r 6.5..7.3); bins between the inner ceiling and the floor
        # are fitted with a plane z = a + b*dx + c*dy (dx, dy at r 6.9 about the collar centre)
        zc_in = float(np.percentile(v[inner, 2], 95))
        thabs = np.degrees(np.arctan2(q[:, 1], q[:, 0])) % 360
        rp = []
        for b in range(0, 360, 10):
            sb = k7 & (thabs >= b) & (thabs < b + 10)
            if sb.sum() > 5:
                zz = float(np.percentile(v[sb, 2], 90))
                if zc_in + 0.3 < zz < zf - 0.3:
                    t = np.radians(b + 5)
                    rp.append([6.9 * np.cos(t), 6.9 * np.sin(t), zz])
        rp = np.array(rp)
        Mx = np.c_[np.ones(len(rp)), rp[:, 0], rp[:, 1]]
        cf, *_ = np.linalg.lstsq(Mx, rp[:, 2], rcond=None)
        rs = rp[:, 2] - Mx @ cf
        nr = np.array([-cf[1], -cf[2], 1.0])
        nr /= np.linalg.norm(nr)
        rec[name + "_ramp"] = {"n_bins": int(len(rp)), "rms": float(np.sqrt((rs ** 2).mean())), "max": float(np.abs(rs).max()),
                               "normal_up": nr.tolist(), "offset": float(nr @ np.array([c0[0], c0[1], cf[0]]))}
        # it3: middle sectors -- bins whose 90th-pct z lies 0.6..1.3 below the floor (cap hook region on B1)
        mids = []
        for b in range(0, 360, 10):
            sb = k7 & (thabs >= b) & (thabs < b + 10)
            if sb.sum() > 5:
                zz = float(np.percentile(v[sb, 2], 90))
                if zf - 1.3 <= zz < zf - 0.6:
                    if mids and mids[-1][1] == b:
                        mids[-1][1] = b + 10
                        mids[-1][2] = min(mids[-1][2], zz)
                    else:
                        mids.append([b, b + 10, zz])
        rec[name + "_mid"] = [[float(a), float(b_), float(z_)] for a, b_, z_ in mids]
        rec[name] = {"r": r_out, "top_z_inner": float(np.percentile(v[inner, 2], 95)),
                     "outer_p50_z": float(np.percentile(v[outer, 2], 50)),
                     "floor_sector_deg": [float(min(ok) + outward), float(max(ok) + 10 + outward)], "bins_ok": ok}
R["recess"] = rec
R["collars"] = coll

# ------------------------------------------------------------------ screw holes
holes = {}
for name, c0 in (("L", np.array([-13.3, -8.0])), ("R", np.array([12.7, -8.0]))):
    cb = stations(c0, 3.3, 4.3, [-0.6, -1.2, -1.8, -2.4])
    q = v[:, :2] - c0
    rr = np.hypot(*q.T)
    thr = rr[(rr < 2.4) & (v[:, 2] < -3.3) & (v[:, 2] > -5.5)]
    frt = rr[(rr > 2.6) & (rr < 3.4) & (v[:, 2] < -13.6) & (v[:, 2] > -15.8)]
    holes[name] = {"cb_stations": cb, "cb_r": float(np.median([s["r"] for s in cb])),
                   "centre": [float(np.median([s["cx"] for s in cb])), float(np.median([s["cy"] for s in cb]))],
                   "through_r_p50": float(np.median(thr)) if len(thr) else None, "through_n": int(len(thr)),
                   "front_r_p50": float(np.median(frt)) if len(frt) else None, "front_n": int(len(frt)),
                   "front_scan_top_z": float(np.percentile(v[(rr < 3.4) & (rr > 2.6) & (v[:, 2] < -11) & (v[:, 2] > -16), 2], 99)),
                   "through_scan_bottom_z": float(np.percentile(v[(rr < 2.2) & (v[:, 2] < -3.0) & (v[:, 2] > -9), 2], 1))}
for name in ("L", "R"):
    c0 = np.array(holes[name]["centre"])
    fr = []
    for z in (-13.6, -14.2, -14.8):
        P = sect(z)[:, :2]
        q = P - c0
        k = (np.hypot(*q.T) < 4.2) & (q[:, 1] > -1.5)
        fr.append({"z": z, **kasa(P[k])})
    holes[name]["front_stations"] = fr
    holes[name]["front_circle"] = [float(np.median([f[k] for f in fr])) for k in ("cx", "cy", "r")]
R["holes"] = holes

# ------------------------------------------------------------------ inner latch bosses (inside the rim, behind hoops H1, H2, H4)
bosses = {}
for name, lo, hi, xr in (("mY_L", -16.8, -15.5, (-33, -16.5)), ("mY_R", -16.8, -15.5, (16, 32)), ("pY_R", 3.8, 5.2, (12, 32))):
    segs_all = []
    for z in (0.6, 1.5, 2.5):
        P = sect(z)[:, :2]
        q = P[(P[:, 1] > lo) & (P[:, 1] < hi) & (P[:, 0] > xr[0]) & (P[:, 0] < xr[1])]
        xs = np.sort(q[:, 0])
        br = np.where(np.diff(xs) > 1.0)[0]
        seg = max(np.split(xs, br + 1), key=len)
        segs_all.append([float(seg.min()), float(seg.max())])
    nsign = 1 if name.startswith("mY") else -1
    k = (N[:, 1] * nsign > 0.97) & (C[:, 1] > lo) & (C[:, 1] < hi) & (C[:, 2] > 0.3) & (C[:, 2] < 3.2) & \
        (C[:, 0] > xr[0]) & (C[:, 0] < xr[1])
    bosses[name] = {"x": [float(np.median([a[0] for a in segs_all])), float(np.median([a[1] for a in segs_all]))],
                    "x_by_z": segs_all, "inner_face_y": float(np.average(C[k, 1], weights=A[k])),
                    "inner_face_area_mm2": float(A[k].sum())}
R["bosses"] = bosses
R["z"]["boss_top"] = zlevel(+1, 3.2, 3.8)

# ------------------------------------------------------------------ connector shroud
P7 = sect(7.0)[:, :2]
s = (P7[:, 0] > -26) & (P7[:, 0] < 9) & (P7[:, 1] > -2) & (P7[:, 1] < 13)
q = P7[s]
sh = {"outer": {"xmin": float(np.percentile(q[:, 0], 0.2)), "xmax": float(np.percentile(q[:, 0], 99.8)),
                "ymin": float(np.percentile(q[:, 1], 0.2)), "ymax": float(np.percentile(q[:, 1], 99.8))}}
cx0 = 0.5 * (sh["outer"]["xmin"] + sh["outer"]["xmax"])
cy0 = 0.5 * (sh["outer"]["ymin"] + sh["outer"]["ymax"])
# inner wall: points more than 0.6 inside the outer box
ins = q[(q[:, 0] > sh["outer"]["xmin"] + 0.6) & (q[:, 0] < sh["outer"]["xmax"] - 0.6) &
        (q[:, 1] > sh["outer"]["ymin"] + 0.6) & (q[:, 1] < sh["outer"]["ymax"] - 0.6)]
sh["inner"] = {"xmin": float(np.percentile(ins[:, 0], 0.5)), "xmax": float(np.percentile(ins[:, 0], 99.5)),
               "ymin": float(np.percentile(ins[:, 1], 0.5)), "ymax": float(np.percentile(ins[:, 1], 99.5))}
# outer corner radius: Kasa on the 4 corner arcs
cr = []
for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
    x0 = sh["outer"]["xmin"] if sx < 0 else sh["outer"]["xmax"]
    y0 = sh["outer"]["ymin"] if sy < 0 else sh["outer"]["ymax"]
    k = q[(np.abs(q[:, 0] - x0) < 2.0) & (np.abs(q[:, 1] - y0) < 2.0) & (np.abs(q[:, 0] - x0) > 0.05) &
          (np.abs(q[:, 1] - y0) > 0.05)]
    k = k[((k[:, 0] - x0) * -sx < 1.6) & ((k[:, 1] - y0) * -sy < 1.6)]
    k = k[np.hypot(k[:, 0] - (x0 - sx * 1.2), k[:, 1] - (y0 - sy * 1.2)) < 1.6]
    if len(k) > 6:
        cr.append(kasa(k)["r"])
sh["outer_corner_r"] = cr
sh["inner_scan_bottom_z"] = float(np.percentile(v[(v[:, 0] > sh["inner"]["xmin"] + 0.3) & (v[:, 0] < sh["inner"]["xmax"] - 0.3) & (v[:, 2] > -6) &
                                                   (v[:, 1] > sh["inner"]["ymax"] - 0.4) & (v[:, 1] < sh["inner"]["ymax"] + 0.05) & (v[:, 2] > -8), 2], 0.5))
peaks = {"y": [], "x": []}
for zz in (3.0, 5.0, 7.0, 9.0):
    Pq = sect(zz)[:, :2]
    qy = Pq[(Pq[:, 0] > -15) & (Pq[:, 0] < -2) & (Pq[:, 1] > -2) & (Pq[:, 1] < 12.5), 1]
    qx = Pq[(Pq[:, 1] > 3) & (Pq[:, 1] < 8) & (Pq[:, 0] > -25) & (Pq[:, 0] < 8), 0]
    for key, qq, edges in (("y", qy, [(-1, 0.5), (0.5, 2), (9.5, 11.1), (11.1, 12.5)]),
                           ("x", qx, [(-24, -22.1), (-22.1, -20.5), (3.5, 5.0), (5.0, 6.5)])):
        peaks[key].append([float(np.median(qq[(qq > lo) & (qq < hi)])) for lo, hi in edges])
sh["walls_median_z3_9"] = {"y_outer_min": float(np.median([r[0] for r in peaks["y"]])), "y_inner_min": float(np.median([r[1] for r in peaks["y"]])),
                           "y_inner_max": float(np.median([r[2] for r in peaks["y"]])), "y_outer_max": float(np.median([r[3] for r in peaks["y"]])),
                           "x_outer_min": float(np.median([r[0] for r in peaks["x"]])), "x_inner_min": float(np.median([r[1] for r in peaks["x"]])),
                           "x_inner_max": float(np.median([r[2] for r in peaks["x"]])), "x_outer_max": float(np.median([r[3] for r in peaks["x"]]))}
kz = (v[:, 0] > -15) & (v[:, 0] < -2) & (np.abs(v[:, 1] - 10.5) < 0.25) & (v[:, 2] > -8) & (v[:, 2] < 10)
sh["inner_wall_scan_bottom_z"] = float(np.percentile(v[kz, 2], 0.5))
# it2: scanned header-base pads at z ~ 0 next to the -Y inner wall (verify it1 over-band cluster 0)
kp = (v[:, 0] > sh["walls_median_z3_9"]["x_inner_min"] + 0.1) & (v[:, 0] < sh["walls_median_z3_9"]["x_inner_max"] - 0.1) & \
     (v[:, 1] > sh["walls_median_z3_9"]["y_inner_min"] + 0.35) & (v[:, 1] < sh["walls_median_z3_9"]["y_inner_min"] + 2.5) & \
     (v[:, 2] > -0.8) & (v[:, 2] < 0.6)
qp = v[kp]
xs_ = np.sort(qp[:, 0])
groups = np.split(xs_, np.where(np.diff(xs_) > 1.2)[0] + 1)
pads = []
for g_ in groups:
    sg = (qp[:, 0] >= g_.min()) & (qp[:, 0] <= g_.max())
    if sg.sum() >= 20:
        pads.append({"x": [float(g_.min()), float(g_.max())], "y_max": float(np.percentile(qp[sg, 1], 98)),
                     "top_z": float(np.percentile(qp[sg, 2], 90)), "n": int(sg.sum())})
sh["header_pads"] = pads
R["shroud"] = sh
# slot between shroud +Y wall and the rim bump inner wall
R["slot_scan_bottom_z"] = float(np.percentile(v[(v[:, 0] > -12) & (v[:, 0] < 2) & (v[:, 1] > sh["outer"]["ymax"] + 0.3) &
                                                (v[:, 1] < sh["outer"]["ymax"] + 1.3) & (v[:, 2] > -8), 2], 0.5))

# ------------------------------------------------------------------ mounting tab
xin = np.abs(C[:, 0]) < 11
tab = {}
tab["top"] = plane_fit(xin & (N[:, 2] > 0.985) & (C[:, 2] > 18) & (C[:, 1] < -28), [0, 0, 1], trim=0.08)
tab["under"] = plane_fit(xin & (N[:, 2] < -0.985) & (C[:, 2] > 15.5) & (C[:, 2] < 17) & (C[:, 1] < -29), [0, 0, -1], trim=0.08)
tab["incline_upper"] = plane_fit(xin & (N @ np.array([0, 0.707, 0.707]) > 0.97) & (C[:, 2] > 7.5) & (C[:, 2] < 18.5) & (C[:, 1] < -16), [0, 1, 1])
tab["incline_lower"] = plane_fit(xin & (N @ np.array([0, -0.707, -0.707]) > 0.97) & (C[:, 2] > 7.0) & (C[:, 2] < 16) & (C[:, 1] < -18), [0, -1, -1])
tab["leg_outer"] = plane_fit(xin & (N[:, 1] < -0.985) & (C[:, 2] > 0.5) & (C[:, 2] < 5.5) & (C[:, 1] < -18), [0, -1, 0], trim=0.08)
tab["leg_inner"] = plane_fit(xin & (N[:, 1] > 0.985) & (C[:, 2] > 0.5) & (C[:, 2] < 5.5) & (C[:, 1] > -18) & (C[:, 1] < -15.5), [0, 1, 0], trim=0.08)
Pe = sect(-37.0, normal=(0, 1, 0), axis=1)
tab["end_y"] = float(np.percentile(v[(np.abs(v[:, 0]) < 10) & (v[:, 2] > 17) & (v[:, 2] < 18.5), 1], 0.2))
widths = {}
for y in (-21.0, -27.0, -33.0, -36.5):
    P = sect(y, normal=(0, 1, 0), axis=1)
    hi = P[P[:, 2] > 3]
    widths[str(y)] = {"x_outer": [float(np.percentile(P[:, 0], 0.3)), float(np.percentile(P[:, 0], 99.7))],
                      "z_min": float(P[:, 2].min())}
    # flange inner faces: points below the plate underside
    lo = P[P[:, 2] < float(np.percentile(P[:, 2], 50)) - 1.0]
    if len(lo):
        widths[str(y)]["x_inner"] = [float(lo[lo[:, 0] < 0, 0].max()) if (lo[:, 0] < 0).any() else None,
                                     float(lo[lo[:, 0] > 0, 0].min()) if (lo[:, 0] > 0).any() else None]
tab["sections"] = widths
fl = (np.abs(C[:, 0]) > 13.2) & (np.abs(C[:, 0]) < 15.8)
tab["flange_lower_incline"] = plane_fit(fl & (N @ np.array([0, -0.707, -0.707]) > 0.97) & (C[:, 1] < -27) & (C[:, 2] > 0), [0, -1, -1])
tab["flange_bottom"] = zlevel(-1, -2.3, -1.5, fl & (C[:, 1] < -19))
tab["flange_inner_x"] = {
    "neg": plane_fit((C[:, 0] < -12) & (C[:, 0] > -14.5) & (N[:, 0] > 0.985) & (C[:, 2] < 12), [1, 0, 0], trim=0.08),
    "pos": plane_fit((C[:, 0] > 12) & (C[:, 0] < 14.5) & (N[:, 0] < -0.985) & (C[:, 2] < 12), [-1, 0, 0], trim=0.08)}
tab["flange_outer_x"] = {
    "neg": plane_fit((C[:, 0] < -14.5) & (N[:, 0] < -0.985) & (C[:, 1] < -18.8) & (C[:, 2] > -1), [-1, 0, 0], trim=0.08),
    "pos": plane_fit((C[:, 0] > 14.5) & (N[:, 0] > 0.985) & (C[:, 1] < -18.8) & (C[:, 2] > -1), [1, 0, 0], trim=0.08)}
Ph = sect(17.7)[:, :2]
s = (np.abs(Ph[:, 0]) < 2.5) & (Ph[:, 1] < -30) & (Ph[:, 1] > -36)
tab["hole"] = kasa(Ph[s])
R["tab"] = tab

# ------------------------------------------------------------------ latch hoops (U-shaped, protruding from the T0 wall)
hoops = {}
spec = {"H1": (-1, -31.0, -17.5, -19.7), "H2": (-1, 17.0, 31.0, -19.7),
        "H3": (1, -24.5, -9.5, 15.3), "H4": (1, 17.5, 30.0, 7.9)}
for name, (sgn, xlo, xhi, ycut) in spec.items():
    P = sect(ycut, normal=(0, 1, 0), axis=1)
    P = P[(P[:, 0] > xlo) & (P[:, 0] < xhi) & (P[:, 2] > -7) & (P[:, 2] < 6)]
    bar = P[P[:, 2] < -4.5]
    xs = [float(np.percentile(bar[:, 0], 0.5)), float(np.percentile(bar[:, 0], 99.5))]
    xm = 0.5 * sum(xs)
    up = P[(P[:, 2] > 1.0) & (P[:, 2] < 4.0)]
    wx = [float(up[up[:, 0] < xm, 0].max()), float(up[up[:, 0] > xm, 0].min())]
    mid = P[(P[:, 0] > wx[0] + 0.5) & (P[:, 0] < wx[1] - 0.5)]
    selo = (C[:, 0] > xs[0] + 0.5) & (C[:, 0] < xs[1] - 0.5) & (C[:, 2] < -3.8) & (C[:, 2] > -5.3) & (N[:, 1] * sgn > 0.95)
    hoops[name] = {"side": "+Y" if sgn > 0 else "-Y", "section_y": ycut, "x": xs, "window_x": wx,
                   "window_bottom_z": float(np.percentile(mid[:, 2], 99)) if len(mid) else None,
                   "top_z": float(np.percentile(P[:, 2], 99.5)), "bottom_z": float(np.percentile(P[:, 2], 0.5)),
                   "outer_face_y": float(np.median(C[selo, 1])) if selo.any() else None}
# window floor of each hoop is an inclined catch ramp: plane fit on its up-facing faces
for name, h in hoops.items():
    sgn = 1 if h["side"] == "+Y" else -1
    wx = h["window_x"]
    yo = h["outer_face_y"]
    sel = (N[:, 2] > 0.5) & (C[:, 0] > wx[0] + 0.3) & (C[:, 0] < wx[1] - 0.3) & (C[:, 2] < 0.5) & (C[:, 2] > -5) & \
          ((C[:, 1] - yo) * sgn > -2.0) & ((C[:, 1] - yo) * sgn < 0.3)
    h["window_ramp"] = plane_fit(sel, [0, -0.6 * sgn, 0.8], trim=0.12)
R["hoops"] = hoops

hdr = {"schema": "stl-re/measure_all@1", "tool": "measure_all.py", "tool_version": "OD-E02 run",
       "inputs": {"intake/aligned_work.stl": sha(MESH), "intake/alignment.json": sha(RUN / "intake/alignment.json")},
       "seed": 0, "created": datetime.now(timezone.utc).isoformat(timespec="seconds")}
OUT.write_text(json.dumps({**hdr, **R}, indent=1))
print("wrote", OUT)
