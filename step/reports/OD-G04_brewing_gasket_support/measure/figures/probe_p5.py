p,fi=trimesh.sample.sample_surface(m,2000000,seed=0)
pr=np.hypot(p[:,0],p[:,1]);pt=np.arctan2(p[:,1],p[:,0])
# rib angles: find via mass in band r 11-14, z -10.4..-8
k=B(11,14,pr)&B(-10.4,-8,p[:,2])
h,e=np.histogram(np.degrees(pt[k]),bins=360,range=(-180,180))
from scipy.ndimage import uniform_filter1d
hs=uniform_filter1d(h.astype(float),5,mode='wrap')
pk=[i for i in range(360) if hs[i]==max(hs[(i+d)%360] for d in range(-8,9)) and hs[i]>3*np.median(hs)]
print('rib peaks deg',[e[i]+0.5 for i in pk])
for a in [e[i]+0.5 for i in pk]:
  t=np.radians(a); d=-p[:,0]*np.sin(t)+p[:,1]*np.cos(t); along=p[:,0]*np.cos(t)+p[:,1]*np.sin(t)
  kk=(abs(d)<0.35)&(along>0)
  row=[]
  for r0 in np.arange(10.5,20.6,1.0):
    q=kk&B(r0,r0+1,along)&(p[:,2]<-3)
    row.append(round(float(p[q,2].min()),2) if q.sum() else None)
  # thickness: width of rib at z -8 r 11-14
  q=B(11,14,along)&B(-9.5,-6,p[:,2])&(abs(d)<1.5)
  dd=d[q]; w=np.percentile(dd,[2,98])
  print(f'rib {a:.1f}: minz by r 10.5..20.5 {row} width2-98 {w.round(2)} ~{w[1]-w[0]:.2f}')
