"""D-01b / U-06 on the tray less its two pins (cut exactly at the seat plane x 82.438)."""
import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from build123d import Box, Pos, Align
from tools.core import read_step, validity
from tools.measure import min_wall, min_wall_wide, feature_census
t = read_step(PART)
nopin = t
for py, pz in ((81.98, -157.52), (30.99, -157.51)):
    nopin = nopin - Pos(82.438, py, pz) * Box(4.0, 3.0, 3.0, align=(Align.MIN, Align.CENTER, Align.CENTER))
s = nopin.solids(); print("solids", len(s)); nopin = s[0]
print({k: v.measured for k, v in validity(nopin).items()}, "vol", t.volume - nopin.volume, "expected", 3.14159265*0.81*2.5)
print({k: v.measured for k, v in feature_census(nopin).items()})
mw = min_wall(nopin, spacing=0.7); print("min_wall", mw.measured, mw.at, mw.status, mw.reason, mw.detail.get("largest_step_mm"))
g("D-01b", mw, ">=", 2.0, note="tray less the two pins")
mww = min_wall_wide(nopin, spacing=0.7); print("wide", mww.measured, mww.at, mww.status)
g("U-06", mww, ">=", 2.0, note="tray less the two pins, wide")
nopin.export_step = None
from build123d import export_step
export_step(nopin, str(W / "nopin.step"))
dump("r02_nopin.json")
