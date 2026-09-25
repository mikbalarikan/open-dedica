def runs(k,lab):
  h,e=np.histogram(th[k],bins=360,range=(-180,180));on=h>0
  rs=[];i=0
  while i<360:
    if on[i]:
      j=i
      while j<360 and on[j]: j+=1
      rs.append((int(e[i]),int(e[j]) if j<360 else 180));i=j
    else:i+=1
  print(f'{lab:24s}',[x for x in rs if x[1]-x[0]>3])
runs(B(31.5,34,r)&(n[:,2]>0.9)&B(-8.2,-7.3,c[:,2]),'tab top')
runs(B(31.5,34,r)&(n[:,2]<-0.9)&B(-10,-9,c[:,2]),'tab bottom')
runs(B(33.5,35,r)&(abs(n[:,2])<0.4),'tab outer wall')
runs(B(31.2,34.6,r)&(abs(n[:,2])<0.4)&B(-9.4,-7.9,c[:,2]),'tab region walls')
# tab end-face angle via faces whose normal is tangential
t_=np.c_[-np.sin(np.radians(th)),np.cos(np.radians(th))]
tn=(n[:,0]*t_[:,0]+n[:,1]*t_[:,1])
for s,lab in [(1,'end faces +tangent'),(-1,'end faces -tangent')]:
  k=B(31.2,34.6,r)&(s*tn>0.85)&B(-9.4,-7.9,c[:,2]);runs(k,lab)
  for a0 in [-160,-40,80]:
    kk=k&B(a0,a0+75,th)
    if kk.sum(): print('   ',a0,'median th %.2f r %.2f n %d'%(np.median(th[kk]),np.median(r[kk]),kk.sum()))
