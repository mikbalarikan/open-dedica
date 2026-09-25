"""Builder watertightness self-check (NOT QA): tessellate each exported STEP at 0.005 mm and count
open/non-manifold edges. Usage: python3 tess_check_NOT_QA.py <step> [<step> ...]"""
import sys, numpy as np, trimesh
from build123d import import_step
for p in sys.argv[1:]:
    s = import_step(p)
    for tol in (0.005,):
        v, f = s.tessellate(tol, 0.1)
        m = trimesh.Trimesh(np.array([[a.X, a.Y, a.Z] for a in v]), np.array(f), process=True)
        e = np.sort(m.edges, axis=1); u, c = np.unique(e, axis=0, return_counts=True)
        nm = int((c > 2).sum()); op = int((c == 1).sum())
        bad = u[c != 2]
        print(f"{p.split('/')[-1]} tol={tol}: faces={len(m.faces)} watertight={m.is_watertight} winding={m.is_winding_consistent} "
              f"non_manifold_edges={nm} open_edges={op} volume={m.volume:.3f}")
        if len(bad): print("   bad edge midpoints (first 5):", np.round(m.vertices[bad[:5]].mean(1), 3).tolist())
