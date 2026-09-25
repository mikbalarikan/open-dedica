out=[]
for a in [-154.5,-94.5,-39.5,25.5,81.0,140.5]:
  t=np.radians(a);u=np.array([np.cos(t),np.sin(t)]);v=np.array([-np.sin(t),np.cos(t)])
  d=c[:,:2]@v; al=c[:,:2]@u; nv=n[:,:2]@v
  base=B(10.8,19.8,al)&B(-10,-3.5,c[:,2])&(abs(d)<2)
  lines=[]
  for s in (1,-1):
    k=base&(s*nv>0.85)
    P=c[k,:2]; mu=P.mean(0); w,V=np.linalg.eigh(np.cov((P-mu).T)); dirv=V[:,1]
    if dirv@u<0: dirv=-dirv
    nrm=np.array([-dirv[1],dirv[0]]); dist=mu@nrm; res=(P-mu)@nrm
    lines.append((np.degrees(np.arctan2(dirv[1],dirv[0])),dist,res.std(),k.sum()))
  ang=(lines[0][0]+lines[1][0])/2; t_=abs(lines[0][1]-lines[1][1]); off=(lines[0][1]+lines[1][1])/2
  print(f'rib~{a}: side angles {lines[0][0]:.2f}/{lines[1][0]:.2f} rms {lines[0][2]:.3f}/{lines[1][2]:.3f} n {lines[0][3]}/{lines[1][3]} -> dir {ang:.2f} offset {off:.3f} thick {t_:.3f}')
  out.append(dict(nominal=a,dir_deg=ang,offset_mm=off,t_mm=t_))
json.dump(out,open('measure/figures/ribs_lines.json','w'),indent=1)
