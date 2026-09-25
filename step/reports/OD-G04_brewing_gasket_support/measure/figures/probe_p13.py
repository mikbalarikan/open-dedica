p,fi=trimesh.sample.sample_surface(m,3000000,seed=1)
pr=np.hypot(p[:,0],p[:,1]);pt=np.degrees(np.arctan2(p[:,1],p[:,0]))
k=B(6.5,7.2,pr)&B(-0.25,0.25,p[:,2])
h,e=np.histogram(pt[k],bins=360,range=(-180,180));on=h>0
gaps=[];i=0
while i<360:
  if not on[i]:
    j=i
    while j<360 and not on[j]: j+=1
    gaps.append((int(e[i]),int(e[j]) if j<360 else 180));i=j
  else:i+=1
print('backface gaps (slots) 1deg:',gaps)
