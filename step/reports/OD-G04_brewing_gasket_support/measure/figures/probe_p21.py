# tab outer radius, top and bottom z versus angle across each tab (bayonet ramp check)
rd=(n[:,0]*c[:,0]+n[:,1]*c[:,1])/np.maximum(r,1e-9)
for c0 in [-123.44,-3.29,116.78]:
  print('tab centre',c0)
  for da in np.arange(-30,30.1,6):
    a0=c0+da
    kk=B(a0-3,a0+3,th)
    ko=kk&B(33,35.5,r)&(rd>0.7)&B(-9.3,-8.0,c[:,2])
    kt=kk&B(31.6,33.6,r)&(n[:,2]>0.9)&B(-8.4,-7.2,c[:,2])
    kb=kk&B(31.6,33.6,r)&(n[:,2]<-0.9)&B(-10.2,-9.0,c[:,2])
    f=lambda k,a: f'{np.median(a[k]):.3f}' if k.sum()>5 else '  -   '
    print(f'   da {da:+5.0f}  R_out {f(ko,r)}  top {f(kt,c[:,2])}  bot {f(kb,c[:,2])}')
