"""Provisional frame for exploration only (not the datum). Writes intake/prov.stl"""
import numpy as np, trimesh
m=trimesh.load('intake/work.stl')
n=np.array([-0.392,-0.489,-0.779]); n/=np.linalg.norm(n); z=-n
x=np.cross([0,0,1.],z); x/=np.linalg.norm(x); y=np.cross(z,x); R=np.stack([x,y,z])
T=np.eye(4); T[:3,:3]=R; T[:3,3]=-np.array([10.25,-97.22,-190.49])
m.apply_transform(T); m.export('intake/prov.stl'); print(m.bounds)
