import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from geo import *
from tools.core import common_volume
from tools.measure import clearance
m = load_mount()
h22, h24, h22p, h24p = load_oem()
H22_0 = comp(h22); H24_0 = comp(h24); H24s = comp(h24p)
hooks = None
for th in (70, 160, 320):
    s = sector(th, 12.0, 18.5, 27.0, 4.0, 40.0); hooks = s if hooks is None else hooks + s
m_nohooks = m - hooks
print("hook-exempt mount volume removed", m.volume - m_nohooks.volume)
R = {"h24": [], "h22": []}
# OD-H24 lowered along -Z from 25 above: every 0.5 mm, hooks exempt; also the hook contact is recorded (not gated)
for d in [25 - 0.5 * i for i in range(51)]:
    P = H24_0.moved(Location((0, 0, 10.0 + d)))
    iv = common_volume(m_nohooks, P).measured
    ivh = common_volume(m & hooks, P).measured
    R["h24"].append((d, iv, ivh))
print("H24 max interference (hooks exempt)", max(r[1] for r in R["h24"]), "poses", len(R["h24"]))
print("H24 hook overlap along the path (snap, exempt):", [(d, round(h, 3)) for d, _, h in R["h24"] if h > 0][:6], "...")
# OD-H22: slide along -Y at +5 from y +45 to 0 (every 1 mm, 0.25 mm over y 18..0), then drop 5 -> 0 every 0.25
ys = sorted(set([45 - i for i in range(46)] + [18 - 0.25 * i for i in range(73)]), reverse=True)
for y in ys:
    P = H22_0.moved(Location((62.0, y, 53.0)))
    iv = common_volume(m, P).measured; iv24 = common_volume(P, H24s).measured
    c = clearance(m, P)
    R["h22"].append(("slide", y, 5.0, iv, iv24, c.measured, c.at))
for dz in [5 - 0.25 * i for i in range(21)]:
    P = H22_0.moved(Location((62.0, 0.0, 48.0 + dz)))
    iv = common_volume(m, P).measured; iv24 = common_volume(P, H24s).measured
    c = clearance(m, P)
    R["h22"].append(("drop", 0.0, dz, iv, iv24, c.measured, c.at))
print("H22 poses", len(R["h22"]), "max interference mount", max(r[3] for r in R["h22"]), "max with H24", max(r[4] for r in R["h22"]))
sl = [r for r in R["h22"] if r[0] == "slide"]
b = min(sl, key=lambda r: r[5]); print("least slide clearance", b)
dr = [r for r in R["h22"] if r[0] == "drop" and r[2] > 0]
b2 = min(dr, key=lambda r: r[5]); print("least drop clearance above the seat", b2)
print("drop clearances", [(r[2], round(r[5], 4)) for r in R["h22"] if r[0] == "drop"])
dump("s08.json", R)
