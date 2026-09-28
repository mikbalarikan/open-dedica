import sys, numpy as np, trimesh, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
def render(m, views, out, title=''):
    n=len(views); fig,axs=plt.subplots(1,n,figsize=(6*n,6))
    if n==1: axs=[axs]
    for ax,(name,R) in zip(axs,views):
        v=m.vertices@R.T; f=m.faces
        tri=v[f]; nz=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]); nn=np.linalg.norm(nz,axis=1)+1e-12; nz=nz/nn[:,None]
        vis=nz[:,2]>0
        tri=tri[vis]; nzv=nz[vis]
        order=np.argsort(tri[:,:,2].mean(1))
        light=np.array([0.3,0.4,0.85]); light/=np.linalg.norm(light)
        sh=np.clip(nzv@light,0,1)*0.8+0.15
        cols=np.stack([sh,sh,sh*1.05],1).clip(0,1)
        pc=PolyCollection(tri[order][:,:,:2],facecolors=cols[order],edgecolors='none')
        ax.add_collection(pc); ax.set_aspect('equal'); ax.autoscale(); ax.set_title(name); ax.grid(alpha=.3)
    fig.suptitle(title); fig.tight_layout(); fig.savefig(out,dpi=90); plt.close(fig)
def rot(ax_to_view):
    pass
if __name__=='__main__':
    m=trimesh.load(sys.argv[1]); 
    if len(m.faces)>150000: m=m.simplify_quadric_decimation(face_count=150000)
    c=m.bounds.mean(0); m.apply_translation(-c)
    I=np.eye(3)
    views=[('+Z top (x right,y up)',I),('-Z bottom',np.diag([1,-1,-1])),('+Y view',np.array([[1,0,0],[0,0,1],[0,-1,0]])),('+X view',np.array([[0,1,0],[0,0,1],[1,0,0]]))]
    render(m,views,sys.argv[2])
