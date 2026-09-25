exec(open('measure/figures/probe_p8.py').read().split('runs(B(31.5')[0])
rlev(B(6.9,8.2,r)&B(-2.4,-0.2,c[:,2]),False,'slot outer wall (inward-facing)')
rlev(B(5.6,6.8,r)&B(-2.4,-0.3,c[:,2]),True,'slot inner wall = hub ring outer (below z0)')
runs(B(6.9,8.2,r)&B(-2.4,-0.2,c[:,2])&(abs(n[:,2])<0.3),'slot outer wall')
t_=np.c_[-np.sin(np.radians(th)),np.cos(np.radians(th))];tn=(n[:,0]*t_[:,0]+n[:,1]*t_[:,1])
for s in (1,-1):
  k=B(6.2,7.4,r)&(s*tn>0.85)&B(-2.4,-0.2,c[:,2])
  for a0 in [-40,50,140,-130]:
    kk=k&B(a0,a0+90,th)
    if kk.sum()>5: print('slot end',s,a0,'th %.2f n %d'%(np.median(th[kk]),kk.sum()))
k=(r>6.2)&(r<7.4)&(th>170)|(r>6.2)&(r<7.4)&(th<-160)
k=k&(np.abs(tn)>0.85)&B(-2.4,-0.2,c[:,2]); print('wrap slot ends', np.round(np.sort(th[k])[[0,-1]],1) if k.sum() else None, k.sum())
zlev(B(0,3,r)&B(-6,-4,c[:,2]),False,'bore bottom?')
rlev(B(1,1.8,r)&B(-5.5,-2.5,c[:,2]),False,'centre bore wall')
