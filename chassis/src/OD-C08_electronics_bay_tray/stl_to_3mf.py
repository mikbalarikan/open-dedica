"""stl2_3mf.py <stl> <out.3mf> <name>: write a 3MF (machine frame, mm) from the designer's STL and re-parse it."""
import sys, zipfile
import trimesh
stl, out, name = sys.argv[1:4]
m = trimesh.load(stl, force="mesh")
m.merge_vertices()
v = "".join(f'<vertex x="{x:.6f}" y="{y:.6f}" z="{z:.6f}"/>' for x, y, z in m.vertices)
t = "".join(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in m.faces)
model = ('<?xml version="1.0" encoding="UTF-8"?><model unit="millimeter" xml:lang="en-US" '
         'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">'
         f'<metadata name="Title">{name}</metadata><resources><object id="1" name="{name}" type="model">'
         f'<mesh><vertices>{v}</vertices><triangles>{t}</triangles></mesh></object></resources>'
         '<build><item objectid="1"/></build></model>')
ct = ('<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
      '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
      '<Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>')
rels = ('<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Target="/3D/3dmodel.model" Id="rel0" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>')
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", ct); z.writestr("_rels/.rels", rels); z.writestr("3D/3dmodel.model", model)
import re, numpy as np
with zipfile.ZipFile(out) as z: x = z.read("3D/3dmodel.model").decode()
V = np.array(re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', x), float)
F = np.array(re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', x), int)
r = trimesh.Trimesh(V, F, process=False)
print(f"stl tris {len(m.faces)} vol {m.volume:.2f} | 3mf tris {len(r.faces)} vol {r.volume:.2f} watertight {r.is_watertight} bbox {r.bounds.round(3).tolist()}")
