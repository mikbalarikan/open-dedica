"""Write a minimal 3MF (one mesh object, millimetres) from an STL. Usage: stl_to_3mf.py in.stl out.3mf name"""
import sys, zipfile, hashlib
import numpy as np, trimesh
src, dst, name = sys.argv[1:4]
m = trimesh.load(src, force="mesh")
v, f = m.vertices, m.faces
verts = "".join(f'<vertex x="{x:.6f}" y="{y:.6f}" z="{z:.6f}"/>' for x, y, z in v)
tris = "".join(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in f)
model = ('<?xml version="1.0" encoding="UTF-8"?>'
         '<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">'
         f'<metadata name="Title">{name}</metadata><resources><object id="1" name="{name}" type="model"><mesh>'
         f'<vertices>{verts}</vertices><triangles>{tris}</triangles></mesh></object></resources>'
         '<build><item objectid="1"/></build></model>')
ct = ('<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
      '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
      '<Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>')
rels = ('<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Target="/3D/3dmodel.model" Id="rel0" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>')
with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", ct); z.writestr("_rels/.rels", rels); z.writestr("3D/3dmodel.model", model)
import xml.etree.ElementTree as ET
root = ET.fromstring(zipfile.ZipFile(dst).read("3D/3dmodel.model"))
ns = {"m": "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"}
bv = np.array([[float(e.get(k)) for k in "xyz"] for e in root.iter("{%s}vertex" % ns["m"])])
bf = np.array([[int(e.get(k)) for k in ("v1", "v2", "v3")] for e in root.iter("{%s}triangle" % ns["m"])])
back = trimesh.Trimesh(bv, bf, process=False)
print(f"{name}: stl faces {len(f)} watertight {m.is_watertight} vol {m.volume:.2f}; 3mf faces {len(back.faces)} vol {back.volume:.2f} dvol {abs(back.volume-m.volume):.4f} unit {root.get('unit')}")
print(hashlib.sha256(open(dst,'rb').read()).hexdigest(), dst)
