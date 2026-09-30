import json, math
import numpy as np
from pathlib import Path
from build123d import Cylinder, Pos, Rot, Axis
from tools.core.step import read_step
from tools.core.shapes import faces, solids
from tools.core.validity import validity
from tools.measure import radial_extent, radial_profile, overhang_census, bore_census, locate_bore
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead"); W = J/"reviews/RV01_work"
s = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
out = {}
def d(r): return r.to_dict()
# --- windows: inner rays on the lower half-circle, fit a circle; apex ray; gable rays
wins = {"w1": (150, -200), "w2": (150, -130), "w3": (150, -60), "w4": (60, -55)}
W_out = {}
for name, (yc, zc) in wins.items():
    pts = []; rays = {}
    for ang in range(95, 270, 10):   # 90..270 is the -Z half (ref +Z, right hand about +X: 90 deg -> -Y)
        for xl in (63.5, 65.0, 66.5):
            r = radial_extent(s, (0, yc, zc), (1, 0, 0), (0, 0, 1), ang, xl, side="inner")
            if r.ok:
                a = math.radians(ang)
                pts.append((yc - r.measured*math.sin(a), zc + r.measured*math.cos(a)))
            rays[f"{ang}@{xl}"] = r.measured if r.ok else r.reason
    P = np.array(pts)
    A = np.c_[2*P[:,0], 2*P[:,1], np.ones(len(P))]; b = (P**2).sum(1)
    cy, cz, c = np.linalg.lstsq(A, b, rcond=None)[0]; R = math.sqrt(c + cy*cy + cz*cz)
    resid = float(np.abs(np.hypot(P[:,0]-cy, P[:,1]-cz) - R).max())
    apex = radial_extent(s, (0, yc, zc), (1, 0, 0), (0, 0, 1), 0.0, 65.0, side="inner")
    g30 = radial_extent(s, (0, yc, zc), (1, 0, 0), (0, 0, 1), 30.0, 65.0, side="inner")
    g330 = radial_extent(s, (0, yc, zc), (1, 0, 0), (0, 0, 1), 330.0, 65.0, side="inner")
    # through along X: material on a ray along X through the centre
    thr = radial_extent(s, (0, yc, zc), (0, 0, 1), (1, 0, 0), 0.0, 0.0, side="outer")
    W_out[name] = {"diameter": 2*R, "centre": (cy, cz), "offset": math.hypot(cy-yc, cz-zc), "fit_resid": resid,
                   "n": len(pts), "apex": d(apex), "g30": d(g30), "g330": d(g330), "x_ray": d(thr), "rays": rays}
out["windows"] = W_out
# gable 30deg expected: roof line through apex (0,14) at 45deg: point on ray at 30deg: r such that r*sin30 + r*cos30 = 14 -> r = 14/(0.5+0.866)
out["gable30_design"] = 14/(math.sin(math.radians(30))+math.cos(math.radians(30)))
# --- bores: radial profile outer, wall = min outer - measured radius; D-05a across X
bc = bore_census(s)
B = {}
for tag, y0, zs in (("base", 0.0, (-45, -105, -165, -225)), ("top", 209.0, (-60, -210))):
    for z in zs:
        prof = radial_profile(s, (65, y0, z), (0, 1, 0), (1, 0, 0), list(range(0, 360, 10)), (0.0, 6.0), margin=0, z_step=0.5, side="outer", r_min=2.0 - 1e-6)
        e = {k: d(v) for k, v in prof.items()} if isinstance(prof, dict) else d(prof)
        px = radial_extent(s, (65, y0, z), (0, 1, 0), (1, 0, 0), 0.0, 3.0, side="outer")
        mx = radial_extent(s, (65, y0, z), (0, 1, 0), (1, 0, 0), 180.0, 3.0, side="outer")
        lb = locate_bore(bc, (65, y0 + 3, z), (0, 1, 0))
        B[f"{tag}_z{z}"] = {"profile": {k: (v["measured"], v["at"], v["status"], v["reason"]) for k, v in e.items()} if isinstance(e, dict) and "measured" not in e else e,
                            "plus_x": px.measured, "minus_x": mx.measured, "across_x": px.measured + mx.measured,
                            "diameter": lb["diameter"].measured}
out["bores"] = B
# --- wall faces x over the height (REQ-02) and rail top / underside
grid = []
for y in list(np.arange(12.5, 207, 2.5)):
    for z in (-235, -215, -170, -165, -100, -90, -30.5, -239.5, -80, -140, -20 - 25):
        r = radial_extent(s, (0, y, z), (0, 0, 1), (1, 0, 0), 0.0, 0.0, side="outer")
        mats = r.detail.get("material") if r.ok else None
        grid.append((float(y), z, mats if r.ok else r.reason))
xs0 = [m[0][0] for _,_,m in grid if isinstance(m, list) and m]
xs1 = [m[-1][1] for _,_,m in grid if isinstance(m, list) and m]
out["wall_x"] = {"rays": len(grid), "min_x0": min(xs0), "max_x0": max(xs0), "min_x1": min(xs1), "max_x1": max(xs1),
                 "no_material": [g for g in grid if not isinstance(g[2], list) or not g[2]],
                 "multi": [g for g in grid if isinstance(g[2], list) and len(g[2]) != 1]}
# y extents along +Y rays at several x, z (REQ-03 underside, rail top; REQ-06 top)
yr = {}
for x in (59.5, 61.0, 62.5, 64.0, 66.0, 67.5, 69.0, 70.5):
    for z in (-239.5, -200, -150.5, -100, -55, -30.5):
        r = radial_extent(s, (x, -10, z), (0, 0, 1), (0, 1, 0), 0.0, 0.0, side="outer")
        yr[f"{x},{z}"] = [[round(a - 10, 6), round(b - 10, 6)] for a, b in r.detail["material"]] if r.ok else r.reason
out["y_rays"] = yr
# --- D-03a on a refilled solid (named-exception bores refilled by position)
fill = s
for b in bc.detail["bores"]:
    st, en = np.array(b["start"]), np.array(b["end"])
    L = float(np.linalg.norm(en - st)); mid = (st + en) / 2
    c = Pos(*mid) * Rot(90, 0, 0) * Cylinder(b["radius"] + 0.1, L + 0.05)   # Rot X 90: cylinder axis along Y
    fill = fill.fuse(c).clean()
out["refill_valid"] = {k: v.measured for k, v in validity(fill).items()}
out["refill_faces"] = len(faces(fill)); out["refill_bores"] = bore_census(fill).measured
out["overhang_refilled"] = d(overhang_census(fill, build_dir=(0, 0, 1), spacing=0.7))
(W/"m4_rays.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps({k: v for k, v in out.items() if k not in ("y_rays",)}, default=str)[:200])
