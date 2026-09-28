"""Render shaded orthographic views of a mesh (inspection only). usage: render_views.py mesh.stl out.png [--frame raw|datum]"""
import sys, numpy as np, trimesh, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
m = trimesh.load(sys.argv[1]); out = sys.argv[2]
V = m.vertices; F = m.faces; N = m.face_normals; C = m.triangles_center
views = {"+X":np.array([1,0,0]),"-X":np.array([-1,0,0]),"+Y":np.array([0,1,0]),"-Y":np.array([0,-1,0]),"+Z":np.array([0,0,1]),"-Z":np.array([0,0,-1]),
         "iso1":np.array([1,1,1])/3**.5,"iso2":np.array([-1,-1,-1])/3**.5}
fig, axs = plt.subplots(2,4, figsize=(20,10))
for ax,(k,d) in zip(axs.flat, views.items()):
    up = np.array([0,0,1.]) if abs(d[2])<0.9 else np.array([0,1.,0])
    u = np.cross(up,d); u/=np.linalg.norm(u); v=np.cross(d,u)
    depth = C@d; order=np.argsort(depth)
    shade = np.clip(N@d,0,1)[order]
    tri = V[F[order]]
    P = np.stack([tri@u, tri@v],-1)
    from matplotlib.collections import PolyCollection
    pc = PolyCollection(P, facecolors=plt.cm.gray(0.15+0.8*shade), edgecolors='none')
    ax.add_collection(pc); ax.autoscale(); ax.set_aspect('equal'); ax.set_title(f"view from {k} (u={u.round(2)}, v={v.round(2)})", fontsize=8); ax.grid(alpha=.3)
plt.tight_layout(); plt.savefig(out, dpi=80)
