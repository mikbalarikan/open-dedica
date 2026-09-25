"""Station-by-station centre fits (Z-parallel circle per slab) for the stem/sleeve group and the cap,
to test whether the stem group is a tilted line. Writes ../axis_stations.json."""
import json, sys, numpy as np, trimesh
from scipy.optimize import least_squares
RUN = sys.argv[1]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); C, N, A = m.triangles_center, m.face_normals, m.area_faces
r0 = np.hypot(C[:, 0], C[:, 1]); th = np.degrees(np.arctan2(C[:, 1], C[:, 0])); ndr = (N[:, 0]*C[:, 0]+N[:, 1]*C[:, 1])/np.maximum(r0, 1e-9)
def circ(s):
    P = C[s]; w = np.sqrt(A[s])
    f = lambda q: (np.hypot(P[:, 0]-q[0], P[:, 1]-q[1]) - q[2]) * w
    so = least_squares(f, [0, 0, np.median(r0[s])], loss="soft_l1", f_scale=0.05); rr = so.fun / w
    return so.x, float(np.sqrt(np.mean(rr**2))), int(s.sum())
rows = []
def run(name, zs, dz, rlo, rhi, outer=True, thex=None):
    for z in zs:
        s = (np.abs(C[:, 2]-z) < dz) & (r0 > rlo) & (r0 < rhi) & (np.abs(N[:, 2]) < 0.3) & ((ndr > 0.5) if outer else (ndr < -0.5))
        if thex: s &= ~((th > thex[0]) & (th < thex[1]))
        if s.sum() < 40: continue
        (cx, cy, R), rms, n = circ(s); rows.append(dict(feature=name, z=float(z), cx=float(cx), cy=float(cy), R=float(R), rms=rms, n=n))
run("cap", np.arange(3.5, 12.6, 1.0), 0.5, 12.3, 13.6, thex=(-50, 50))
run("collar", [14.9, 15.5], 0.3, 10.7, 11.5)
run("stem_core", np.arange(18.5, 28.0, 1.0), 0.5, 4.8, 5.6)
run("neck", [30.3, 30.9], 0.3, 4.4, 5.0)
run("sleeve", np.arange(33.7, 36.8, 0.6), 0.3, 5.6, 6.2)
run("bore", [36.3, 36.8], 0.25, 3.7, 4.4, outer=False)
for r in rows: print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()})
g = [r for r in rows if r["feature"] in ("stem_core", "neck", "sleeve", "bore")]
z = np.array([r["z"] for r in g]); X = np.c_[np.ones_like(z), z]
bx = np.linalg.lstsq(X, [r["cx"] for r in g], rcond=None)[0]; by = np.linalg.lstsq(X, [r["cy"] for r in g], rcond=None)[0]
res = np.hypot(np.array([r["cx"] for r in g]) - X@bx, np.array([r["cy"] for r in g]) - X@by)
line = {"x0": bx[0], "dxdz": bx[1], "y0": by[0], "dydz": by[1], "tilt_deg": float(np.degrees(np.arctan(np.hypot(bx[1], by[1])))),
        "dir_deg": float(np.degrees(np.arctan2(by[1], bx[1]))), "resid_rms": float(np.sqrt(np.mean(res**2))), "resid_max": float(res.max()), "n": len(g)}
print("stem-group line", {k: round(v, 4) for k, v in line.items()})
gc = [r for r in rows if r["feature"] == "cap"]; zc = np.array([r["z"] for r in gc]); Xc = np.c_[np.ones_like(zc), zc]
cxl = np.linalg.lstsq(Xc, [r["cx"] for r in gc], rcond=None)[0]; cyl = np.linalg.lstsq(Xc, [r["cy"] for r in gc], rcond=None)[0]
print("cap line", cxl, cyl, np.degrees(np.arctan(np.hypot(cxl[1], cyl[1]))))
json.dump({"stations": rows, "stem_group_line": line, "cap_line": {"x0": cxl[0], "dxdz": cxl[1], "y0": cyl[0], "dydz": cyl[1]}}, open(f"{RUN}/measure/figures/axis_stations.json", "w"), indent=1, default=float)
