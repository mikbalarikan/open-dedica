"""Write a 3MF (core spec, mm) from a binary or ASCII STL, vertices deduplicated exactly."""
import struct, sys, zipfile
def read_stl(p):
    b=open(p,'rb').read()
    n=struct.unpack('<I',b[80:84])[0]
    if 84+50*n==len(b):
        tris=[struct.unpack('<9f',b[84+50*i+12:84+50*i+48]) for i in range(n)]
    else:
        v=[tuple(map(float,l.split()[1:4])) for l in b.decode().splitlines() if l.strip().startswith('vertex')]
        tris=[v[i]+v[i+1]+v[i+2] for i in range(0,len(v),3)]
    return tris
def main(stl,out,name):
    tris=read_stl(stl); idx={}; verts=[]; faces=[]
    for t in tris:
        f=[]
        for k in range(3):
            p=t[3*k:3*k+3]
            if p not in idx: idx[p]=len(verts); verts.append(p)
            f.append(idx[p])
        faces.append(f)
    vx="".join(f'<vertex x="{x!r}" y="{y!r}" z="{z!r}"/>' for x,y,z in verts)
    tx="".join(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a,b,c in faces)
    model=('<?xml version="1.0" encoding="UTF-8"?>\n<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">'
      f'<resources><object id="1" type="model" name="{name}"><mesh><vertices>{vx}</vertices><triangles>{tx}</triangles></mesh></object></resources>'
      '<build><item objectid="1"/></build></model>')
    ct='<?xml version="1.0" encoding="UTF-8"?>\n<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>'
    rels='<?xml version="1.0" encoding="UTF-8"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Target="/3D/3dmodel.model" Id="rel0" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>'
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for n,d in (("[Content_Types].xml",ct),("_rels/.rels",rels),("3D/3dmodel.model",model)):
            zi=zipfile.ZipInfo(n,(2026,1,1,0,0,0)); zi.compress_type=zipfile.ZIP_DEFLATED; z.writestr(zi,d)
    print(out,len(tris),'triangles',len(verts),'vertices')
main(*sys.argv[1:4])
