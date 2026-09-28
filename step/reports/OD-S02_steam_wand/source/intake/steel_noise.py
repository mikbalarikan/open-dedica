#!/usr/bin/env python3
"""Run-local (OD-S02): circle noise floor of the STEEL tube surface on a stretch that is NOT the
clock crop. datum_fit.py noise only cuts sections normal to datum Z, and the steel tube segment
between the bend and the white bushing is tilted ~16 deg from Z, so this script slices it
normal to its own axis (Kasa circles on vertex slabs, line through centres, 3 passes) and
reports the median station rms. Seeded / deterministic; writes intake/noise_steel.json."""
import json, hashlib, datetime, sys
from pathlib import Path
import numpy as np, trimesh

def frame(d):
    d = d / np.linalg.norm(d); a = np.array([1., 0, 0]) if abs(d[0]) < 0.9 else np.array([0, 1., 0])
    u = np.cross(d, a); u /= np.linalg.norm(u); return u, np.cross(d, u), d

def stations(V, p, d, lo, hi, halfw=0.2, step=0.5, rmax=4.0):
    u, v, d = frame(d); q = V - p; t = q @ d; x, y = q @ u, q @ v
    keep = np.hypot(x, y) < rmax; out = []
    for z in np.arange(lo, hi + 1e-9, step):
        s = keep & (np.abs(t - z) < halfw)
        if s.sum() < 30: continue
        xy = np.c_[x[s], y[s]]; A = np.c_[2 * xy, np.ones(len(xy))]
        sol = np.linalg.lstsq(A, (xy ** 2).sum(1), rcond=None)[0]; r = np.sqrt(sol[2] + sol[0]**2 + sol[1]**2)
        res = np.hypot(xy[:, 0] - sol[0], xy[:, 1] - sol[1]) - r
        out.append([z, sol[0], sol[1], r, float(np.sqrt((res ** 2).mean()))])
    return np.array(out), u, v, d

here = Path(__file__).resolve().parent
mesh = here / "aligned_work.stl"
V = trimesh.load(mesh).vertices
p = np.array([40.541, -3.048, -27.111]); d = np.array([0.0587, 0.2677, 0.9617])   # seed from a scratch read
for _ in range(3):
    st, u, v, d = stations(V, p, d, -3, 3)
    A = np.c_[np.ones(len(st)), st[:, 0]]
    cx = np.linalg.lstsq(A, st[:, 1], rcond=None)[0]; cy = np.linalg.lstsq(A, st[:, 2], rcond=None)[0]
    p = p + cx[0] * u + cy[0] * v; d = d + cx[1] * u + cy[1] * v; d /= np.linalg.norm(d)
st, *_ = stations(V, p, d, -3, 3)
doc = {"schema": "stl-re/datum_fit.noise@1", "tool": "intake/steel_noise.py (run-local)", "tool_version": "OD-S02",
       "inputs": {"intake/aligned_work.stl": hashlib.sha256(mesh.read_bytes()).hexdigest()}, "seed": 0,
       "created": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
       "scan_noise_mm": {"value": float(np.median(st[:, 4])), "p95_mm": float(np.percentile(st[:, 4], 95)),
                         "max_mm": float(st[:, 4].max()),
                         "method": f"median Kasa rms of {len(st)} slabs normal to the steel tube axis, segment between "
                                   "the bend and the white bushing (disjoint from the clock crop)"},
       "axis": {"point": p.tolist(), "direction": d.tolist(), "radius_median_mm": float(np.median(st[:, 3]))}}
(here / "noise_steel.json").write_text(json.dumps(doc, indent=1))
print(json.dumps(doc["scan_noise_mm"], indent=1))
