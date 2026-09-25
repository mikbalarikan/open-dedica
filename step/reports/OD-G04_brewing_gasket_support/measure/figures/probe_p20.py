# lip outer profile away from the tabs (first self-check showed a band at r~31.2, z~-8.2)
notab=~(B(-160,-86,th)|B(-40,34,th)|B(80,154,th))
print('outermost r per z bin (p98 of all faces r 30-32.5), away from tabs; and angular coverage')
for z0 in np.arange(-10.0,-6.8,0.2):
  k=B(30.0,32.5,r)&B(z0,z0+0.2,c[:,2])&notab
  if k.sum()>20:
    h,_=np.histogram(th[k],bins=36,range=(-180,180))
    print(f'  z {z0:.1f} r98 {np.percentile(r[k],98):.3f} r50 {np.median(r[k]):.3f} n {k.sum()} bins_with_pts {int((h>0).sum())}/36')
k=B(30.95,31.6,r)&B(-8.8,-7.6,c[:,2])&notab
h,_=np.histogram(th[k],bins=72,range=(-180,180));print('bulge faces angular hist 5deg:',h.tolist())
