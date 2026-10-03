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
tdr = Circle(30) + Polygon((-30/math.sqrt(2), 30/math.sqrt(2)), (0, 30*math.sqrt(2)), (30/math.sqrt(2), 30/math.sqrt(2)), (0,0), align=None)
win = extrude(Plane.XZ.offset(-160) * tdr, amount=-40)  # XZ normal is -Y; check below
print("window env", env(win))
rig = rig - win
print("rig proxy env", env(rig), "valid", validity(rig)["brep_valid"].measured)


cr = clearance(rig, POSE * g04); print("g04 clr", cr.measured, cr.at, cr.detail if hasattr(cr,'detail') else '')
for phi in (10, 11, 12, 13, 14, 15):
    cr = clearance(rig, posed(g10, phi)); print("phi", phi, round(cr.measured, 3), cr.at)
try:
    it = interference({"rig": rig, "g10": posed(g10, 15)}); print("interf phi15", {k:(v.measured, v.status, getattr(v,'reason',None)) for k,v in it.items()})
except Exception as e: print("interf raised", e)
for zf in (55, 50, 45, 40):
    cutter = Pos(0, 0, zf + 50) * Box(500, 500, 100)
    r2 = rig - cutter
    cr = clearance(r2, posed(g10, 15)); print("front at z", zf, "clr phi15", round(cr.measured, 3), cr.at)
