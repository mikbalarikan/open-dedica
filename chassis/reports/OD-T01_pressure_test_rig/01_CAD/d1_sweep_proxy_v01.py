"""D1 diagnostic: OD-G10 / OD-G04 posed in the rig frame (spec 2) against a proxy of the
C1 profile (spec 4: plate, walls, base, chamfers, hub window with 45 deg roof). Not a deliverable."""
from pathlib import Path
import math
from build123d import Polygon, Pos, Rot, Location, extrude, Circle, Plane, Vector, Box
from tools.core import read_step, validity
from tools.measure import envelope, clearance, interference, feature_census

WS = Path(__file__).resolve().parent.parent
INP = WS / "00_Spec" / "inputs"
asm = read_step(INP / "od_g01_assembly_C1_v03.step")
sol = list(asm.solids())
housing, g04, g10 = sol[0], sol[1], sol[2]

POSE = Location((0, 110.06, 0)) * Location((0, 0, 0), (1, 0, 0), 90)
def posed(s, phi=0.0, dy=0.0, dz=0.0):
    return Location((0, dy, dz)) * Location((0, 0, 0), (0, 1, 0), phi) * (POSE * s)

def env(s):
    r = envelope(s)
    return {k: round(v.measured, 2) for k, v in r.items()}

hp = POSE * housing
print("housing posed", env(hp))
print("g04 posed", env(POSE * g04))
print("g10 posed locked", env(POSE * g10))
v = validity(g10); print("g10 validity", {k: (x.measured, x.status) for k, x in v.items()})

# proxy profile in XY (outer ring with 10x10 chamfers in the four inside corners)
c = 10.0
outer = [(-120,0),(120,0),(120,10),(90,10),(90,150),(-90,150),(-90,10),(-120,10)]
inner = [(-75+c,10),(75-c,10),(75,10+c),(75,135-c),(75-c,135),(-75+c,135),(-75,135-c),(-75,10+c)]
prof = Polygon(*outer, align=None) - Polygon(*inner, align=None)
rig = extrude(Plane.XY.offset(-60) * prof, amount=120)
# hub window R30 along Y with 45 deg teardrop toward +Z (apex z = 30*sqrt2 = 42.43)
from build123d import Cylinder
cyl = Pos(0, 145, 0) * Rot(90, 0, 0) * Cylinder(30, 60)
roof = Polygon((-30/math.sqrt(2), 30/math.sqrt(2)), (0, 30*math.sqrt(2)), (30/math.sqrt(2), 30/math.sqrt(2)), (0, 0), align=None)
roofp = extrude(Plane.XZ.offset(-115) * roof, amount=-60)
win = cyl + roofp
print("window env", env(win))
rig = rig - win
from build123d import Vector
print("inside checks", [rig.is_inside(Vector(*q)) for q in [(18.99,136,0),(0,140,0),(0,136,40),(0,140,-29)]])
print("rig proxy env", env(rig), "valid", validity(rig)["brep_valid"].measured)

print("clear housing", clearance(rig, hp).measured)
cg = clearance(rig, POSE * g04); print("clear g04", cg.measured, cg.at, cg.detail.get("on_b"))
for phi in (10,11,12,13,14,15):
    cr = clearance(rig, posed(g10, phi)); print("phi", phi, round(cr.measured,3), cr.at)
print("clear g10 locked", clearance(rig, POSE * g10).measured)
worst = None
for phi in range(-60, 16, 5):
    cr = clearance(rig, posed(g10, phi))
    e = env(posed(g10, phi))
    print(f"phi {phi:+d}: clr {cr.measured:.2f} at {cr.at}  x[{e['min_x']},{e['max_x']}] y[{e['min_y']},{e['max_y']}]")
for dz in range(0, 201, 5):
    s = posed(g10, -50, dy=-15, dz=dz)
    cr = clearance(rig, s)
    if cr.measured < 3 or dz % 50 == 0:
        print(f"b dz {dz}: clr {cr.measured:.2f} at {cr.at}")
for dy in range(0, 31, 2):
    for nm, s in (("housing", housing), ("g04", g04), ("g10", g10)):
        cr = clearance(rig, Location((0, -dy, 0)) * (POSE * s))
        if dy in (0, 30) or cr.measured < 0.5:
            print(f"U03b dy {dy} {nm}: clr {cr.measured:.3f}")
