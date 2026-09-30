import json
from pathlib import Path
import build123d as bd
from build123d import Plane, Keep, GeomType, Vector, Compound
from tools.core.step import read_step
from tools.drawing import write_sections
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
R = W/"reviews/RV02_work"
part = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v02.step")
asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v02.step")
def cut(shape, origin, normal):
    n = Vector(*normal); out = []
    for s in shape.solids():
        half = bd.split(s, bisect_by=Plane(origin=origin, z_dir=n), keep=Keep.BOTTOM)
        if half is None: continue
        for f in half.faces():
            if f.geom_type == GeomType.PLANE and abs(abs(f.normal_at().dot(n)) - 1) < 1e-6 and abs((f.center() - Vector(*origin)).dot(n)) < 1e-6:
                edges = []
                for e in f.edges():
                    a, b = e.position_at(0), e.position_at(1)
                    edges.append({"type": e.geom_type.name, "a": [round(a.X, 4), round(a.Y, 4), round(a.Z, 4)], "b": [round(b.X, 4), round(b.Y, 4), round(b.Z, 4)], "len": round(e.length, 4)})
                bb = f.bounding_box()
                out.append({"area": round(f.area, 4), "min": [round(bb.min.X,4), round(bb.min.Y,4), round(bb.min.Z,4)], "max": [round(bb.max.X,4), round(bb.max.Y,4), round(bb.max.Z,4)], "edges": edges})
    return out
planes = {"xy_z0": ((0,0,0),(0,0,1)), "xy_z17": ((0,0,17),(0,0,1)), "xy_z28": ((0,0,28),(0,0,1)),
          "yz_x0": ((0,0,0),(1,0,0)), "yz_x31p5": ((31.5,0,0),(1,0,0)), "yz_xm31p5": ((-31.5,0,0),(1,0,0)), "yz_x34": ((34,0,0),(1,0,0)),
          "xz_y7": ((0,7,0),(0,1,0)), "xz_y38p5": ((0,38.5,0),(0,1,0)), "xz_y4": ((0,4,0),(0,1,0))}
res = {k: cut(part, *v) for k, v in planes.items()}
(R/"m3_sections.json").write_text(json.dumps(res, indent=1))
# pictures
pics = []
sec = R/"sections"
for name, view, through in (("rv02_cradle_z0", "top", (0,20,0)), ("rv02_cradle_z17", "top", (0,20,17)), ("rv02_cradle_z28", "top", (0,20,28)),
                            ("rv02_cradle_x31p5", "left", (31.5,20,20)), ("rv02_cradle_x0", "left", (0,20,20)), ("rv02_cradle_y7", "front", (0,7,16))):
    w = write_sections(part, sec, part=name, version=2, views=(view,), through=through)
    for x in w: pics.append({"file": x.path.name, "sha256": x.sha256, "nothing_clipped": x.checks["nothing_clipped"].measured, "cut_area": x.detail["cut_area_mm2"]})
asmc = Compound(children=[c for c in asm.children])
for name, view, through in (("rv02_asm_z0", "top", (0,0,0)), ("rv02_asm_z17", "top", (0,0,17)), ("rv02_asm_z28", "top", (0,0,28)), ("rv02_asm_x0", "left", (0,0,10))):
    try:
        w = write_sections(asmc, sec, part=name, version=2, views=(view,), through=through)
        for x in w: pics.append({"file": x.path.name, "sha256": x.sha256, "nothing_clipped": x.checks["nothing_clipped"].measured, "cut_area": x.detail["cut_area_mm2"]})
    except Exception as e:
        pics.append({"file": name, "error": repr(e)})
(R/"m3_pics.json").write_text(json.dumps(pics, indent=1)); print(json.dumps(pics, indent=1))
