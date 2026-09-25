import numpy as np, trimesh, json, sys
sys.path.insert(0,'/home/claude/agentic_STL-to-CAD/skills/stl-re-intake-datum/scripts')
from datum_fit import fit_circle_kasa
m=trimesh.load_mesh(sys.argv[1]); out=sys.argv[2]; R={'method':'Kasa circle on z-section points, 5.5<r<7.5, |sin(theta)|>0.35 (excludes the XZ-plane gussets)','stations':[]}
for z in (-3.5,-3.0,-2.5,-2.0,-1.5,-1.0):
    s=trimesh.intersections.mesh_plane(m,[0,0,1],[0,0,z]).reshape(-1,3)[:,:2]; r=np.hypot(*s.T); th=np.arctan2(s[:,1],s[:,0])
    k=(r<7.5)&(r>5.5)&(np.abs(np.sin(th))>0.35); c=fit_circle_kasa(s[k]); R['stations'].append({'z':z,**{kk:float(v) for kk,v in c.items() if isinstance(v,(float,int))},'n':int(k.sum())})
json.dump(R,open(out,'w'),indent=1)
