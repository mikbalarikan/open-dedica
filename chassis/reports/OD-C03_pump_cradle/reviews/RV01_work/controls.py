import json, math, sys, struct
import numpy as np
sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c03-pump-cradle/reviews/RV01_work")
from checks import load, run, W, gate
from build123d import *
from tools.core import compare_step, write_stl, write_step
from tools.core.validity import validity
from tools.measure import mesh_census, mesh_deviation
BAND_MM = 0.005
WK = W/"reviews/RV01_work/mutants"; WK.mkdir(exist_ok=True)
part, pump, sleeve = load()

def box(x0,x1,y0,y1,z0,z1): return Pos((x0+x1)/2,(y0+y1)/2,(z0+z1)/2)*Box(x1-x0,y1-y0,z1-z0)
def sector(r0, r1, a0, a1, z0, z1):
    R = r1*2
    pts = [(0,0)] + [(R*math.cos(math.radians(a)), R*math.sin(math.radians(a))) for a in np.linspace(a0, a1, 9)]
    f = (Circle(r1) - Circle(r0)) & Polygon(*pts, align=None)
    return extrude(Pos(0,0,z0)*f, z1-z0)
def hole(x, z, d): return Pos(x, 38.5, z)*Rot(90,0,0)*Cylinder(d/2, 5)
def one(s):
    s = s.solids(); return s[0] if len(s)==1 else Compound(list(s))
plug = hole(-34,-4,3.41)
M = {
 "M01 loose box beside the part (2 solids)": lambda part: Compound([part, box(50,52,0,2,0,2)]),
 "M02 foot grown to z 42.5": lambda part: one(part + box(-40,40,37,40,42,42.5)),
 "M03 part moved +0.2 in Y": lambda part: Pos(0,0.2,0)*part,
 "M04 hole (-34,-4) filled": lambda part: one(part + plug),
 "M05 hole (-34,-4) moved 0.5 to z -3.5": lambda part: one((part + plug) - hole(-34,-3.5,3.4)),
 "M06 hole (-34,-4) resized to 3.1": lambda part: one((part + plug) - hole(-34,-4,3.1)),
 "M07 -X z18 slot cut into its end ligament, 0.6 left": lambda part: one(part - box(-33.6,-29.4,5.75,8.25,13.6,15.0)),
 "M08 -X z18 slot gable filled: flat 6.0 ceiling": lambda part: one(part + box(-33.5,-29.5,2.7,5.76,15,21)),
 "M09 -X post inner face moved in 0.5 (x -29.0)": lambda part: one(part + box(-29.5,-29.0,0,37.5,13,33)),
 "M10 saddle 1 radius 26.55 (0.10 into the sleeve)": lambda part: one(part + sector(26.55,26.66,46,134,15,21)),
 "M11 both saddles opened to r 26.75 (0.10 gap)": lambda part: one(part - sector(26.6,26.75,40,140,14,32)),
 "M12 rib 1 extended to theta 38 (material at 40 deg, r<32)": lambda part: one(part + sector(26.65,32.0,37.5,45.5,15,21)),
 "M13 rib 1 face moved to z 21.3": lambda part: one(part + (Pos(0,0,0.8)*Compound(list(part.intersect(box(-23,23,18,37.5,19.5,20.5)).solids())))),
 "M14 -X z18 slot narrowed to 5.5": lambda part: one(part + box(-33.5,-29.5,5.7,8.3,20.5,21.0)),
}
res = {}
names = list(M.keys())
for name in names:
    part, pump, sleeve = load()
    m = M[name](part)
    G = run(m, pump, sleeve, walls=name.startswith(("M07","M01")) )
    res[name] = {k: (g.status, g.measured, g.margin) for k, g in G.items()}
    fails = [f"{k}={g.measured if not isinstance(g.measured,float) else round(g.measured,4)}" for k,g in G.items() if g.status in ("FAIL","INCONCLUSIVE")]
    print(name, "->", len(fails), "FAIL/INC:", "; ".join(fails)[:900], flush=True)
# M15 STEP round trip against a mutant file
mf = WK/"M04_hole_filled.step"
part, pump, sleeve = load()
write_step(M["M04 hole (-34,-4) filled"](part), mf, timestamp="2026-09-30T00:00:00")
cs = compare_step(part, mf)
g1 = gate("U-04", cs["volume_delta"], "<=", 0.001, band=0.001); g2 = gate("U-04", cs["faces_delta"], "==", 0, band=0)
print("M15 compare_step(part, hole-filled file):", g1.status, g1.measured, g2.status, g2.measured)
res["M15"] = [(g1.status,g1.measured),(g2.status,g2.measured)]
# M16 mesh: coarse remesh and a holed STL
coarse = WK/"coarse_tol0p1.stl"
wr = write_stl(part, coarse, tolerance=0.1, angular_tolerance=0.5)
g3 = gate("U-07", wr.checks["max_sagitta"], "<=", 0.01, band=BAND_MM)
md = mesh_deviation(str(coarse), part); g4 = gate("U-07", md, "<=", 0.01, band=BAND_MM)
print("M16 STL at tol 0.1: sagitta", g3.status, g3.measured, "; deviation", g4.status, g4.measured)
raw = (W/"02_STEP_STL/od_c03_cradle_C1_v01.stl").read_bytes()
n = struct.unpack("<I", raw[80:84])[0]
holed = raw[:80] + struct.pack("<I", n-1) + raw[84:84+50*(n-1)]
(WK/"holed.stl").write_bytes(holed)
mc = mesh_census(str(WK/"holed.stl"))
g5 = gate("U-07", mc["naked_edges"], "==", 0, band=0)
print("M17 delivered STL with one triangle dropped: naked_edges", g5.status, g5.measured)
res["M16"]=[(g3.status,g3.measured),(g4.status,g4.measured)]; res["M17"]=(g5.status,g5.measured)
# M18 validity: open shell (one face removed)
fs = part.faces(); sh = Shell(list(fs)[1:])
v = validity(sh); print("M18 open shell:", {k:(x.measured,x.status) for k,x in v.items()})
res["M18"] = {k:(x.measured,x.status) for k,x in v.items()}
json.dump(res, open(W/"reviews/RV01_work/controls.json","w"), indent=1, default=str)
