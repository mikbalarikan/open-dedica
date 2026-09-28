"""Section loops at z (or x/y) simplified by Douglas-Peucker; prints vertices. usage: loop_simplify.py axis v tol [minlen]"""
import sys, numpy as np, trimesh, shapely.geometry as sg, shapely.ops as so
m=trimesh.load('intake/aligned_work.stl'); ax=sys.argv[1]; v=float(sys.argv[2]); tol=float(sys.argv[3])
k='xyz'.index(ax); o=[i for i in range(3) if i!=k]; n=np.eye(3)[k]
seg=trimesh.intersections.mesh_plane(m,n,n*v)
lines=[sg.LineString(s[:,o]) for s in seg]
merged=so.linemerge(lines)
geoms=list(merged.geoms) if hasattr(merged,'geoms') else [merged]
geoms=sorted(geoms,key=lambda g:-g.length)
for g in geoms[:int(sys.argv[4]) if len(sys.argv)>4 else 6]:
    s=g.simplify(tol)
    print(f'len {g.length:.1f} closed {g.is_ring} n {len(s.coords)}:', ' '.join(f'({x:.2f},{y:.2f})' for x,y in s.coords))
