# Builder self-check script (NOT QA, not independent). Usage: python3 selfcheck_NOT_QA.py <RUN> 200000
"""Builder self-check (NOT QA): unsigned scan->CAD and CAD->scan distances, scan frame; worst
clusters reported in the datum frame. Seeded sampling."""
import json, sys, numpy as np, trimesh
R = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 200000
scan = trimesh.load(f"{R}/input/scan.stl"); cad = trimesh.load(f"{R}/build/OD-S03_steam-knob_cad.stl")
T = np.array(json.load(open(f"{R}/intake/alignment.json"))["matrix_4x4"])
rng = np.random.default_rng(0)
ps, _ = trimesh.sample.sample_surface(scan, N, seed=0)
from trimesh.proximity import ProximityQuery
d = ProximityQuery(cad).on_surface(ps)[1]
st = lambda x: {k: round(float(v), 4) for k, v in dict(rms=np.sqrt((x**2).mean()), p50=np.percentile(x, 50), p95=np.percentile(x, 95), p99=np.percentile(x, 99), max=x.max()).items()}
print("scan->CAD", st(d), "frac>0.3 %.4f  frac>0.8 %.5f" % ((d > 0.3).mean(), (d > 0.8).mean()))
pd = (np.c_[ps, np.ones(len(ps))] @ T.T)[:, :3]
# worst regions: bin by feature zones
r = np.hypot(pd[:, 0], pd[:, 1]); z = pd[:, 2]; th = np.degrees(np.arctan2(pd[:, 1], pd[:, 0]))
zones = {"crown z<0.3": z < 0.3, "cap wall/round 0.3-13.2 r<14": (z >= 0.3) & (z < 13.2) & (r < 14.2),
         "lever r>=14.2 z<13.9": (r >= 14.2) & (z < 13.9), "step/mouth 13.2-14.5": (z >= 13.2) & (z < 14.5) & (r < 14.2),
         "collar/grooves 14.5-17.3": (z >= 14.5) & (z < 17.3), "stem 17.3-28.6": (z >= 17.3) & (z < 28.6),
         "neck 28.6-32.2": (z >= 28.6) & (z < 32.2), "sleeve/bore >=32.2": z >= 32.2}
for k, s in zones.items():
    if s.sum(): print(f"  {k:30s} n={s.sum():6d} p95={np.percentile(d[s],95):.3f} max={d[s].max():.3f} frac>0.8={(d[s]>0.8).mean():.4f}")
idx = np.argsort(-d)[:40]
print("worst 15 (datum x,y,z,r,theta,d):")
for i in idx[:15]: print("   %.2f %.2f %.2f r=%.2f th=%.0f d=%.3f" % (pd[i,0], pd[i,1], pd[i,2], r[i], th[i], d[i]))
pc, _ = trimesh.sample.sample_surface(cad, N // 2, seed=1)
d2 = ProximityQuery(scan).on_surface(pc)[1]
print("CAD->scan (raw, includes unscanned interior/holes)", st(d2))
np.savez(f"{R}/../work/selfcheck_last.npz", ps=pd, d=d)
