"""REQ-05: OD-G10 swing (a) and carry (b), plus the lowering at phi -50, swept together."""
from common import *
from tools.measure import clearance
out = {}
s, ss = part(); P = Solid(ss[0])
r = refs(); E = r["E02"]; G = r["G10"]
a = []
phis = [-55 + 5 * i for i in range(14)] + [7.5, 8.5, 9.0, 9.5, 11.0, 12.0]
for phi in phis:
    Gp = rot_about_axis(G, phi)
    c1 = clearance(Gp, P); c2 = clearance(Gp, E)
    a.append({"phi": phi, "panel": c1.measured, "panel_at": c1.detail["on_b"], "inside": c1.detail["inside"], "e02": c2.measured, "e02_inside": c2.detail["inside"]})
    print(a[-1], flush=True)
out["a"] = a
# lowering at phi -50 from the locked height (0 .. 15 every 2.5), axis at z 32
low = []
G50 = rot_about_axis(G, -50)
for i in range(7):
    dy = -2.5 * i
    Gp = translate(G50, (0, dy, 0))
    c1 = clearance(Gp, P); c2 = clearance(Gp, E)
    low.append({"dy": dy, "panel": c1.measured, "inside": c1.detail["inside"], "e02": c2.measured, "e02_inside": c2.detail["inside"]})
    print(low[-1], flush=True)
out["lower"] = low
b = []
for i in range(31):
    dz = 5.0 * i
    Gp = translate(G50, (0, -15.0, dz))
    c1 = clearance(Gp, P); c2 = clearance(Gp, E)
    b.append({"axis_z": 32 + dz, "panel": c1.measured, "panel_at": c1.detail["on_b"], "inside": c1.detail["inside"], "e02": c2.measured, "e02_inside": c2.detail["inside"]})
    print(b[-1], flush=True)
out["b"] = b
dump("s04_req05.json", out)
