import sys,trimesh,numpy as np,matplotlib
matplotlib.use('Agg');import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import fast_simplification
def render(path,out,views=((30,-60),(30,120),(-30,-60),(90,-90),(0,-90),(0,0)),target=60000):
    m=trimesh.load(path)
    if len(m.faces)>target:
        v,f=fast_simplification.simplify(m.vertices,m.faces,1-target/len(m.faces)); m=trimesh.Trimesh(v,f)
    tri=m.triangles; nrm=m.face_normals
    fig=plt.figure(figsize=(6*len(views)/2,12))
    for i,(el,az) in enumerate(views):
        ax=fig.add_subplot(2,(len(views)+1)//2,i+1,projection='3d')
        e,a=np.radians(el),np.radians(az)
        vd=np.array([np.cos(e)*np.cos(a),np.cos(e)*np.sin(a),np.sin(e)])
        sh=np.clip(np.abs(nrm@vd),0.1,1)
        pc=Poly3DCollection(tri,facecolors=plt.cm.gray(sh*0.8+0.1),edgecolor='none')
        ax.add_collection3d(pc)
        b=m.bounds;ctr=b.mean(0);r=(b[1]-b[0]).max()/2
        ax.set_xlim(ctr[0]-r,ctr[0]+r);ax.set_ylim(ctr[1]-r,ctr[1]+r);ax.set_zlim(ctr[2]-r,ctr[2]+r)
        ax.view_init(el,az);ax.set_title(f'el{el} az{az}');ax.set_box_aspect((1,1,1))
        ax.set_xlabel('X');ax.set_ylabel('Y');ax.set_zlabel('Z')
    plt.tight_layout();plt.savefig(out,dpi=70)
if __name__=='__main__': render(sys.argv[1],sys.argv[2])
