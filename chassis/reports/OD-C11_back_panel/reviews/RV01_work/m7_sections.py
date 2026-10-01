"""RV01: my own sections (pictures with write_sections, plus the cut regions counted numerically) for
E-06 (boss and gussets tied in), E-11 (vents open, holes clear behind), D-03b, REQ-02, and the
pass-through gaps behind the wall. Args: step [out] [nopng]."""
import json, sys
from pathlib import Path
from build123d import Face, Plane, Pos, Rot, Cylinder, Compound, Location, Box
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
from tools.core import read_step, common_volume
from tools.measure import clearance
from tools.drawing import write_sections
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"
STEP = sys.argv[1] if len(sys.argv) > 1 else f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"
OUT = sys.argv[2] if len(sys.argv) > 2 else f"{W}/m7_sections.json"
PNG = not (len(sys.argv) > 3 and sys.argv[3] == "nopng")
p = read_step(STEP)
out = {}
def cut(axis, value):
    if axis == "x": f = Face(Plane(origin=(value, 100, -290), z_dir=(1, 0, 0))).scale(1) ; big = Box(0.000001, 600, 600)
    big = {"x": Plane(origin=(value, 0, 0), z_dir=(1, 0, 0)), "y": Plane(origin=(0, value, 0), z_dir=(0, 1, 0)),
           "z": Plane(origin=(0, 0, value), z_dir=(0, 0, 1))}[axis]
    from build123d import Rectangle
    face = big * Rectangle(1000, 1000)
    c = BRepAlgoAPI_Common(p.wrapped, face.wrapped); c.Build()
    comp = Compound(c.Shape()); fs = comp.faces()
    regions = []
    for f in fs:
        bb = f.bounding_box()
        regions.append({"area": round(f.area, 3), "lo": [round(v, 3) for v in bb.min], "hi": [round(v, 3) for v in bb.max],
                        "holes": len(f.inner_wires())})
    return regions
plan = {"boss_x90": ("x", 90.0), "boss_xm90": ("x", -90.0), "gusset_x74": ("x", 74.0), "gusset_xm74": ("x", -74.0),
        "gusset_x102": ("x", 102.0), "gusset_xm102": ("x", -102.0), "flanges_y2": ("y", 2.0), "gussets_y10": ("y", 10.0),
        "passthroughs_y30": ("y", 30.0), "vents_y140": ("y", 140.0), "bosses_y207": ("y", 207.0), "ledge_y213": ("y", 213.0),
        "wall_z300p5": ("z", -300.5), "behind_z290": ("z", -290.0), "foot_x110": ("x", 110.0)}
for k, (a, v) in plan.items():
    out[k] = cut(a, v); print(k, len(out[k]), [(r["area"], r["lo"], r["hi"], r["holes"]) for r in out[k]][:6])
# E-11 behind each pass-through: d12 cylinder from z -298.95 to -277 (just off the wall face): common volume and gap
for (x, y) in [(95, 30), (-100, 30), (-84, 30)]:
    cyl = Pos(x, y, (-298.95 - 277) / 2) * Cylinder(6.0, 21.95)
    out[f"behind_{x}"] = {"common": common_volume(cyl, p).measured, "gap": clearance(cyl, p).measured, "at": clearance(cyl, p).at}
    print("behind", x, out[f"behind_{x}"])
json.dump(out, open(OUT, "w"), indent=1, default=str)
if PNG:
    folder = Path(W) / "sections"
    for name, view, thr in [("x90", "left", (90, 100, -295)), ("x74", "left", (74, 15, -290)), ("x102", "left", (102, 15, -290)),
                            ("xm101", "left", (-101, 15, -290)), ("y30", "top", (0, 30, -290)), ("y140", "top", (0, 140, -300)),
                            ("y207", "top", (0, 207, -295)), ("zm290", "front", (0, 100, -290)), ("x100p5", "left", (100.5, 15, -290))]:
        ws = write_sections(p, folder / name, part="od_c11_back_RV01", version=3, views=(view,), through=thr)
        for w in ws: print("png", w.path, w.checks["nothing_clipped"].measured)
