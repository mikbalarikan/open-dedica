"""Two-way CAD-vs-scan deviation gate (stl2step section 7), datum frame.

IN : argv[1] original scan STL, argv[2] T.npy (scan->datum), argv[3] CAD datum STL, argv[4] out dir
     optional argv[5] repaired (pymeshfix) scan PLY in datum frame, for the no-scan-data class
OUT: out/deviation_report.json, out/deviation_signed_map.png, out/gate_d1.npy, out/gate_d2.npy
Sign convention: + = CAD proud of the scan (CAD bigger, red), - = CAD short (blue).
"""

import json
import sys
from pathlib import Path

import matplotlib
import numpy as np
import trimesh
from scipy.spatial import cKDTree

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def closest_on_mesh(pts, mesh, k=8, n_samp=3_000_000, seed=0):
    """Exact point-triangle distance on k candidate triangles found by a dense KD-tree."""
    samp, fi = trimesh.sample.sample_surface(mesh, n_samp, seed=seed)
    _, idx = cKDTree(samp).query(pts, k=k)
    cand = fi[idx].reshape(-1)
    P = np.repeat(pts, k, axis=0)
    cp = trimesh.triangles.closest_point(mesh.triangles[cand], P)
    d = np.linalg.norm(cp - P, axis=1).reshape(-1, k)
    j = d.argmin(1)
    ii = np.arange(len(pts))
    return d[ii, j], cp.reshape(-1, k, 3)[ii, j], cand.reshape(-1, k)[ii, j]


def st(d):
    d = np.abs(d)
    return dict(n=int(len(d)), RMS=round(float(np.sqrt((d**2).mean())), 3), p95=round(float(np.percentile(d, 95)), 3),
                p99=round(float(np.percentile(d, 99)), 3), max=round(float(d.max()), 3),
                frac_le_0_3=round(float((d <= 0.3).mean()), 4))


def region(p):
    x, y, z = p.T
    r = np.hypot(x, y)
    return np.select(
        [(y < -15.0) & (r > 20.0),              # free tube lengths beyond the flange
         z < 2.2,                               # bottom: rim, panel, ribs, pins
         z > 21.95,                             # connector boss top, pins, plates, upper-tube crown
         (z >= 12.4) & (r > 16.8)],             # flange skirt, flange top, slots
        ["tubes (free length)", "bottom (z<2.2)", "top features (z>21.95)", "flange"], "cup wall + boss + windows")


def main():
    scan = trimesh.load_mesh(sys.argv[1])
    scan.apply_transform(np.load(sys.argv[2]))
    cad = trimesh.load_mesh(sys.argv[3])
    out = Path(sys.argv[4])
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(0)
    sv = scan.vertices[rng.choice(len(scan.vertices), 150_000, replace=False)]
    d1, cp1, f1 = closest_on_mesh(sv, cad)
    s1 = -np.sign(np.einsum("ij,ij->i", sv - cp1, cad.face_normals[f1]))  # scan point inside CAD -> CAD bigger
    cs, cfi = trimesh.sample.sample_surface(cad, 80_000, seed=1)
    d2, cp2, _ = closest_on_mesh(cs, scan, n_samp=4_000_000)
    s2 = np.sign(np.einsum("ij,ij->i", cs - cp2, cad.face_normals[cfi]))
    # CAD area where the scanner saw nothing: far from the scan AND near a scan hole boundary,
    # or where the pymeshfix patch fits the CAD much better than the raw scan does.
    from trimesh.grouping import group_rows
    be = scan.edges_sorted[group_rows(scan.edges_sorted, require_count=1)]
    bv = scan.vertices[np.unique(be)]
    near_hole = cKDTree(bv).query(cp2)[0] < 1.0
    nodata = (d2 > 0.3) & near_hole
    if len(sys.argv) > 5:
        rep = trimesh.load_mesh(sys.argv[5])
        d2r, _, _ = closest_on_mesh(cs, rep, n_samp=4_000_000, seed=3)
        nodata |= (d2 > 0.3) & (d2r < 0.5 * d2)
    R = {"scan->CAD": st(d1), "CAD->scan (all)": st(d2), "CAD->scan (scanned surface only)": st(d2[~nodata]),
         "CAD area on no-scan-data patches (fraction)": round(float(nodata.mean()), 4),
         "scan->CAD signed mean": round(float((s1 * d1).mean()), 3)}
    for name, P, d in (("scan->CAD", sv, d1), ("CAD->scan (scanned only)", cs[~nodata], d2[~nodata])):
        rg = region(P)
        R[name + " by region"] = {g: st(d[rg == g]) for g in np.unique(rg)}
        bad = P[np.abs(d) > 0.8]
        R[name + " worst samples (d>0.8)"] = np.round(bad[rng.choice(len(bad), min(15, len(bad)), replace=False)], 1).tolist() if len(bad) else []
    np.save(out / "gate_d1.npy", np.c_[sv, s1 * d1])
    np.save(out / "gate_d2.npy", np.c_[cs, s2 * d2, nodata])
    json.dump(R, open(out / "deviation_report.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in R.items() if "worst" not in k}, indent=1))

    # signed map: side unwrap (theta, z) + top + bottom, scan points coloured by signed scan->CAD
    sd = s1 * d1
    x, y, z = sv.T
    r = np.hypot(x, y)
    th = np.degrees(np.arctan2(y, x)) % 360
    fig = plt.figure(figsize=(30, 22))
    kw = dict(cmap="bwr", vmin=-0.8, vmax=0.8, s=0.6)
    ax = fig.add_subplot(2, 2, (1, 2))
    side = (r > 14.5) & (r < 21.5) & (z > -0.5) & (z < 21)
    o = np.argsort(np.abs(sd[side]))
    sc = ax.scatter(th[side][o], z[side][o], c=sd[side][o], **kw)
    ax.set_title("side unwrap (theta, z), outer walls r 14.5..21.5 - scan->CAD signed (+ red = CAD proud)", fontsize=18)
    ax.set_xlabel("theta deg")
    ax.set_ylabel("z mm")
    ax.grid(alpha=0.3)
    views = ((sv[:, 2] > 12, "TOP view (z>12 points)"), (sv[:, 2] < 12, "BOTTOM view (z<12 points, seen from below: x mirrored)"))
    for i, (sel, t) in enumerate(views):
        ax = fig.add_subplot(2, 2, 3 + i)
        o = np.argsort(sv[sel][:, 2] * (1 if i == 0 else -1))  # nearest-to-viewer drawn last
        xx = sv[sel][o, 0] * (1 if i == 0 else -1)
        ax.scatter(xx, sv[sel][o, 1], c=sd[sel][o], **kw)
        ax.set_aspect("equal")
        ax.set_title(t, fontsize=18)
        ax.grid(alpha=0.3)
    fig.colorbar(sc, ax=fig.axes, shrink=0.5, label="signed deviation mm")
    plt.savefig(out / "deviation_signed_map.png", dpi=50)


if __name__ == "__main__":
    main()
