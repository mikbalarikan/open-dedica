import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from geo import *
from tools.measure import radial_extent, overhang_census, clearance, envelope
from tools.core import common_volume, validity, step_roundtrip, read_step
from build123d import Solid
m = load_mount(); R = {}
def p(k, v): R[k] = v; print(k, str(v)[:900])
# ---- E-06: torus / fillet faces
tor = []
for f in m.faces():
    if f.geom_type.name == "TORUS":
        s = f.geom_adaptor(); t = s.Torus() if hasattr(s, "Torus") else None
        bb = f.bounding_box(); tor.append((round(f.area, 3), (round(bb.min.Z, 3), round(bb.max.Z, 3)), (round(t.MajorRadius(), 3), round(t.MinorRadius(), 3)) if t else None))
p("torus faces", tor)
cyl = []
for f in m.faces():
    if f.geom_type.name == "CYLINDER":
        s = f.geom_adaptor(); c = s.Cylinder(); bb = f.bounding_box()
        cyl.append((round(c.Radius(), 4), tuple(round(v, 3) for v in (bb.min.X, bb.max.X, bb.min.Y, bb.max.Y, bb.min.Z, bb.max.Z))))
p("cylinder faces", sorted(cyl))
cones = []
for f in m.faces():
    if f.geom_type.name == "CONE":
        s = f.geom_adaptor(); c = s.Cone(); bb = f.bounding_box()
        cones.append((round(math.degrees(c.SemiAngle()), 4), round(c.RefRadius(), 4), tuple(round(v, 3) for v in (bb.min.Z, bb.max.Z)), round(f.area, 3)))
p("cone faces", cones)
# ---- deck tied to legs: section at x 38 and x 86 through legs at z 44 (material continuous from deck into leg)
for x in (38.0, 86.0, 41.0, 83.0):
    r = ray(m, (x, 0, 60), (0, 0, -1))
    p(f"vray x={x}", [(round(60-b,4), round(60-a,4)) for a, b in stretches(r)])
# ---- U-04 round trip of the delivered body
raw = read_step(MOUNT)
from tools.core.shapes import occ
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL, TopAbs_SOLID, TopAbs_FACE
def count(sh, kind, avoid=None):
    e = TopExp_Explorer(occ(sh), kind) if avoid is None else TopExp_Explorer(occ(sh), kind, avoid); n = 0
    while e.More(): n += 1; e.Next()
    return n
p("file: shells / shells outside solids / faces outside shells", (count(raw, TopAbs_SHELL), count(raw, TopAbs_SHELL, TopAbs_SOLID), count(raw, TopAbs_FACE, TopAbs_SHELL)))
body = Solid(solids(raw)[0]); body.label = "od_c07_mount"
rt = step_roundtrip(body, W / "roundtrip_mount.step", timestamp="2026-09-30T00:00:00")
p("roundtrip of the re-read body", {k: (r.measured, r.status, r.reason[:80]) for k, r in rt.items()})
dump("s07b.json", R)
