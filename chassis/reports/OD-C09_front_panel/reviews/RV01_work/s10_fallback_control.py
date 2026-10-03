from common import *
from tools.measure import clearance
s, ss = part(); P = Solid(ss[0]); r = refs()
m = P + box(-30, 30, 170, 188, 94, 97)          # window top lowered to y 170 over x -30 .. 30
G50 = translate(rot_about_axis(r["G10"], -50), (0, -15, 0))
rows = []
for zc in (77.0, 87.0, 97.0, 107.0, 117.0):
    c = clearance(translate(G50, (0, 0, zc - 32)), m)
    rows.append({"axis_z": zc, "clearance": c.measured, "inside": c.detail["inside"], "at": c.at})
fails = [x for x in rows if x["clearance"] <= 0 or x["inside"]]
out = {"rows": rows, "status": "FAIL" if fails else "PASS"}
print(out); dump("s10_fallback_control.json", out)
