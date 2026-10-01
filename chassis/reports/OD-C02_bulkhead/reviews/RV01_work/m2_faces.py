import json
from pathlib import Path
from tools.core.step import read_step
from tools.core.shapes import faces
from tools.measure.sampling import kind
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.BRepGProp import BRepGProp
from OCP.GProp import GProp_GProps
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib
from OCP.TopAbs import TopAbs_REVERSED
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_WIRE
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead")
s = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
rows = []
for i, f in enumerate(faces(s)):
    ad = BRepAdaptor_Surface(f)
    g = GProp_GProps(); BRepGProp.SurfaceProperties_s(f, g)
    b = Bnd_Box(); BRepBndLib.Add_s(f, b); x0,y0,z0,x1,y1,z1 = b.Get()
    k = kind(f)
    info = {"i": i, "kind": k, "area": round(g.Mass(), 4),
            "bbox": [round(v, 4) for v in (x0,y0,z0,x1,y1,z1)]}
    ex = TopExp_Explorer(f, TopAbs_WIRE); nw = 0
    while ex.More(): nw += 1; ex.Next()
    info["wires"] = nw
    if k == "plane":
        pl = ad.Plane(); n = pl.Axis().Direction()
        sgn = -1 if f.Orientation() == TopAbs_REVERSED else 1
        info["normal"] = [round(sgn*n.X(), 6), round(sgn*n.Y(), 6), round(sgn*n.Z(), 6)]
    else:
        c = ad.Cylinder(); a = c.Axis()
        info["r"] = round(c.Radius(), 6); info["axis"] = [round(a.Direction().X(),6), round(a.Direction().Y(),6), round(a.Direction().Z(),6)]
        info["loc"] = [round(a.Location().X(),4), round(a.Location().Y(),4), round(a.Location().Z(),4)]
    rows.append(info)
(J/"reviews/RV01_work/m2_faces.json").write_text(json.dumps(rows, indent=0))
for r in rows: print(r)
