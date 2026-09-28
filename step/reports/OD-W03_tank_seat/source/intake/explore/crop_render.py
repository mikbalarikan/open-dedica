import sys,trimesh,numpy as np,matplotlib
matplotlib.use('Agg');import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
m=trimesh.load(sys.argv[1]); box=np.array(eval(sys.argv[3])); views=eval(sys.argv[4])
c=m.triangles_center; k=np.all((c>=box[0])&(c<=box[1]),axis=1)
m=m.submesh([np.where(k)[0]],append=True)
tri=m.triangles;nrm=m.face_normals
fig=plt.figure(figsize=(7*len(views),7))
for i,(el,az) in enumerate(views):
    ax=fig.add_subplot(1,len(views),i+1,projection='3d')
    e,a=np.radians(el),np.radians(az); vd=np.array([np.cos(e)*np.cos(a),np.cos(e)*np.sin(a),np.sin(e)])
    sh=np.clip(nrm@vd,0,1)*0.8+0.15
    ax.add_collection3d(Poly3DCollection(tri,facecolors=plt.cm.gray(sh),edgecolor='none'))
    b=m.bounds;ctr=b.mean(0);r=(b[1]-b[0]).max()/2
    ax.set_xlim(ctr[0]-r,ctr[0]+r);ax.set_ylim(ctr[1]-r,ctr[1]+r);ax.set_zlim(ctr[2]-r,ctr[2]+r)
    ax.view_init(el,az);ax.set_box_aspect((1,1,1));ax.set_title(f'el{el} az{az}')
    ax.set_xlabel('X');ax.set_ylabel('Y')
plt.tight_layout();plt.savefig(sys.argv[2],dpi=75)
