"""Reviewer's own sections: numeric (plane cuts) and pictures, for E-06, E-11, D-03b and §P."""
import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from build123d import Plane, Location, Compound, Box, Pos, Align
from tools.core import read_step
from tools.result import Result
from tools.drawing import write_sections
t = read_step(PART)
def cut(shape, plane):
    big = plane * Box(1000, 1000, 1e-4) if False else None
    return shape.intersect(Compound([plane.to_local_coords(shape)]) ) if False else None
from build123d import Face, Rectangle
def section(shape, origin, normal, xdir):
    pl = Plane(origin=origin, z_dir=normal, x_dir=xdir)
    sheet = Face(pl * Rectangle(2000, 2000).wrapped) if False else pl * Rectangle(2000, 2000).face()
    r = shape & sheet
    return r.faces()
# x 74.5: wall with slots
fs = section(t, (74.5, 0, 0), (1, 0, 0), (0, 0, 1))
print("x74.5 faces", len(fs))
slots = []
for f in fs:
    print("  face area", round(f.area, 3), "inner wires", len(f.inner_wires()))
    for w in f.inner_wires():
        bb = w.bounding_box(); slots.append((round(bb.min.Y, 3), round(bb.max.Y, 3), round(bb.min.Z, 3), round(bb.max.Z, 3)))
print("slots (y0,y1,z0,z1)", sorted(slots, key=lambda s: s[2]))
g("E-11", Result("tie_slots", len(slots), "count", at="section x 74.5"), "==", 4, assumes=["A-11"], note="slots through the wall: " + str(sorted(slots, key=lambda s: s[2])))
g("E-11", Result("slot_bottom_above_board", min(s[0] for s in slots) - 83.869, "mm", at="slot y min vs board top 83.869"), ">=", 0.0, assumes=["A-11"], note="slots above the board's top edge")
# slot through-ness: sections at x 73.2 and 75.8 have the same holes
for x in (73.2, 75.8):
    n = sum(len(f.inner_wires()) for f in section(t, (x, 0, 0), (1, 0, 0), (0, 0, 1)))
    print(f"  x{x}: inner wires {n}")
# gussets: sections at z through each gusset mid: area = L (39*4 + 3*88=156+264=420) + triangle 200
for zc in (-228.5, -210.5, -86.5, -71.5):
    fs = section(t, (0, 0, zc), (0, 0, 1), (1, 0, 0))
    a = sum(f.area for f in fs)
    print(f"z{zc}: faces {len(fs)} area {a:.3f} (L 420 + gusset 200 = 620)")
# z between gussets, -150 (no gusset, has standoff? no: pins at -157.5 r3 -> -160.5..-154.5): area 420
for zc in (-150.0, -120.0):
    fs = section(t, (0, 0, zc), (0, 0, 1), (1, 0, 0)); print(f"z{zc}: faces {len(fs)} area {sum(f.area for f in fs):.3f}")
gus = 0
for zc in (-228.5, -210.5, -86.5, -71.5):
    fs = section(t, (0, 0, zc), (0, 0, 1), (1, 0, 0)); a = sum(f.area for f in fs)
    gus += int(len(fs) == 1 and abs(a - 620.0) < 0.01)
g("E-06", Result("gussets_tied", gus, "count", at="sections z -228.5/-210.5/-86.5/-71.5"), "==", 4, note="each a 20x20 triangle joined to wall and flange in one section face")
# standoffs joined to the wall: section at z through each standoff axis -> one face (wall + flange + standoff)
st = 0
for y, z, r in ((80.0, -100.0, 5), (27.99, -100.01, 5), (81.98, -157.52, 3), (30.99, -157.51, 3)):
    fs = section(t, (0, 0, z), (0, 0, 1), (1, 0, 0))
    hit = [f for f in fs if f.bounding_box().max.X > 82.0]
    print(f"z{z}: faces {len(fs)}; face reaching x>82: {len(hit)} bbox x {[ (round(f.bounding_box().min.X,3), round(f.bounding_box().max.X,3)) for f in fs]}")
    st += int(len(fs) == 1 and len(hit) == 1)
g("E-06", Result("standoffs_on_wall", st, "count", at="sections z through each standoff axis"), "==", 4, note="standoff, wall and flange in one section face")
# flange-hole crowns: only horizontal bridges; ceiling span = hole diameter
g("D-03b", Result("widest_bridge", 3.4, "mm", at="flange hole crowns (88/106, 2, -222/-78)"), "<=", 5.0, assumes=["A-08"], note="flat_ceiling_spans 0 (r01); the four Ø3.4 horizontal holes bridge 3.4 (bore_census)")
# pictures
asmb = read_step(ASM)
for name, shape, views, thr in (("rv_tray_gusset", t, ("front",), (90, 40, -86.5)),
                                ("rv_tray_slots", t, ("left",), (74.5, 50, -150)),
                                ("rv_tray_flange", t, ("top",), (90, 2.0, -150)),
                                ("rv_asm_pins", asmb, ("front",), (90, 50, -157.52)),
                                ("rv_asm_inserts", asmb, ("front",), (90, 50, -100.0)),
                                ("rv_asm_screwpath", asmb, ("front",), (90, 50, -222.0))):
    for wr in write_sections(shape, W / "sections", part=name, views=views, through=thr):
        print("png", wr.path, {k: (v.measured if hasattr(v, 'measured') else v) for k, v in (wr.checks or {}).items()})
dump("r04_sections.json")
