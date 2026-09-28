"""Fine r(z) profiles (p10/p50/p90 of face radii per 0.2 mm z-bin) in theta windows clear of attachments.
Writes measure/figures/profiles.json (evidence for the column top round, groove profile, window floor)."""
import json, numpy as np, trimesh
m=trimesh.load('intake/aligned_work.stl'); C=m.triangles_center; N=m.face_normals
th=np.degrees(np.arctan2(C[:,1],C[:,0]))%360; r=np.hypot(C[:,0],C[:,1]); nr=(N[:,0]*C[:,0]+N[:,1]*C[:,1])/np.maximum(r,1e-9)
clean=((th>300)|(th<60)|((th>165)&(th<250)))
out={}
def prof(name, sel, zs, extra=None):
    rows=[]
    for z in zs:
        s=sel&(np.abs(C[:,2]-z)<0.1)
        if extra is not None: s&=extra
        if s.sum()>=5: rows.append([round(float(z),2),int(s.sum())]+[round(float(v),3) for v in np.percentile(r[s],[10,50,90])])
    out[name]={'columns':['z','n','r_p10','r_p50','r_p90'],'rows':rows}
prof('column_top', clean&(r<9.5), np.arange(25.5,28.6,0.2))
prof('neck_groove', clean&(r<9.5), np.arange(32.4,37.4,0.2))
prof('neck_block', clean&(r<9.5), np.arange(41.8,44.4,0.2))
prof('top_rim', clean&(r<9.5), np.arange(46.6,48.8,0.2))
prof('window_180', (th>165)&(th<195)&(nr>0.5)&(r<9.2), np.arange(10.0,15.6,0.4))
prof('window_0', ((th>350)|(th<8))&(nr>0.5)&(r<9.2), np.arange(10.0,15.6,0.4))
json.dump(out,open('measure/figures/profiles.json','w'),indent=1); print('profiles.json written')
