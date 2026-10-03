"""common_volume on whole tray x OD-E01 missed a 3.6 mm3 seat overlap (control r06). Re-measure the contact
interference rows on regions cut from the tray, and prove each region method on its own mutant."""
import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from build123d import *
from tools.core import read_step, common_volume, validity
from tools.measure import clearance, envelope
from tools.result import Result
A = ["A-02", "A-03", "A-06"]
t = Solid(read_step(PART).wrapped)
board = read_step(E01).solids()[0].moved(Location(Plane(origin=(84.0, 80.0, -100.0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))))
c01 = read_step(C01).solids()[0]
XCYL = lambda x0, y, z, r, L: Pos(x0, y, z) * Rot(0, 90, 0) * Cylinder(r, L, align=(Align.CENTER, Align.CENTER, Align.MIN))
BOX = lambda x0, y0, z0, dx, dy, dz: Pos(x0, y0, z0) * Box(dx, dy, dz, align=(Align.MIN, Align.MIN, Align.MIN))
def region(s, x0):  # tray material at x >= x0 (the board lies wholly at x >= 82.438)
    return (s & BOX(x0, -10, -300, 60, 200, 300))
def cv_region(s, b, x0=82.0):
    r = region(s, x0); rs = r.solids()
    tot = 0.0
    for p in rs:
        c = common_volume(p, b)
        if c.status != "MEASURED": return c
        tot += c.measured
    return Result("common_volume_region", tot, "mm3", at=f"tray at x >= {x0}: {len(rs)} pieces")
print("board min_x", envelope(board)["min_x"].measured, "-> only tray material at x >= 82.438 can overlap the board")
reg = region(t, 82.0).solids(); print("region pieces", len(reg), [round(p.volume, 3) for p in reg])
r = cv_region(t, board); g("U-03", r, "<=", 0.0, assumes=A, note="tray/OD-E01 interference, on the tray's pieces at x >= 82.0 (4 seat slices + 2 pins), each against the board")
g("D-04c", r, "<=", 0.0, assumes=["A-02"], note="tray/OD-E01 interference (region method)")
# control: H1 seat raised 0.06
m10 = (t + (XCYL(82.438, 80.0, -100.0, 5.0, 0.06) - XCYL(82.3, 80.0, -100.0, 2.0, 0.3))).solids()[0]
rc = cv_region(m10, board); print("CONTROL region common_volume seat+0.06:", rc.measured, rc.status)
C = [{"check": "common_volume on regions (U-03, D-04c interference)", "mutant": "resize: H1 seat raised 0.06", "got": "FAIL" if (rc.status == "MEASURED" and rc.measured > 0.001) else ("INCONCLUSIVE" if rc.status != "MEASURED" else "PASS"), "measured": rc.measured}]
# path with the region method, step 0.25 from +5.0
worst = 0.0
for i in range(20, -1, -1):
    dx = i * 0.25; c = cv_region(t, board.moved(Location((dx, 0, 0))))
    if c.status != "MEASURED": worst = None; break
    worst = max(worst, c.measured)
g("U-03", Result("path_region", worst, "mm3", at="dx 5.0..0 step 0.25, tray x >= 82.0"), "<=", 0.0, assumes=A, note="U-03 (b) path on the region (21 poses)")
wc = max(cv_region(m10, board.moved(Location((dx, 0, 0)))).measured for dx in (0.25, 0.0))
C.append({"check": "common_volume on regions along the path (U-03 b)", "mutant": "resize: H1 seat raised 0.06 (meets the board in the last 0.06 of travel)", "got": "FAIL" if wc > 0.001 else "PASS", "measured": wc})
print("CONTROL path region", wc)
# plate contact: whole-tray common_volume vs OD-C01, and its control (flange sunk 0.05 into the plate)
p0 = common_volume(t, c01); print("tray/C01 whole", p0.measured, p0.status)
m_sink = t.moved(Location((0, -0.05, 0)))
p1 = common_volume(m_sink, c01); print("CONTROL whole tray sunk 0.05 vs C01:", p1.measured, p1.status, "expected ~", 6203.68 * 0.05)
# region alternative for the plate: tray at y <= 1 vs C01
def cv_low(s, b):
    rs = (s & BOX(60, -10, -300, 80, 11, 300)).solids(); tot = 0.0
    for p in rs:
        c = common_volume(p, b)
        if c.status != "MEASURED": return c
        tot += c.measured
    return Result("common_volume_region", tot, "mm3", at="tray at y <= 1")
p2 = cv_low(m_sink, c01); print("CONTROL region tray sunk 0.05 vs C01:", p2.measured)
p3 = cv_low(t, c01); print("region tray vs C01", p3.measured)
C.append({"check": "common_volume whole tray vs OD-C01 (U-03 plate interference)", "mutant": "relocate: tray sunk 0.05 into the plate", "got": "FAIL" if (p1.status == "MEASURED" and p1.measured > 0.001) else ("INCONCLUSIVE" if p1.status != "MEASURED" else "PASS"), "measured": p1.measured})
C.append({"check": "common_volume on the flange region vs OD-C01 (U-03 plate interference)", "mutant": "relocate: tray sunk 0.05 into the plate", "got": "FAIL" if (p2.status == "MEASURED" and p2.measured > 0.001) else "PASS", "measured": p2.measured})
g("U-03", p3, "<=", 0.0, assumes=A, note="tray/OD-C01 interference, flange region y <= 1 (region method)")
# tray vs OD-C02: clearance 2.0 > 0 settles interference; control: tray moved -2.5 in x
cc = clearance(t.moved(Location((-2.5, 0, 0))), read_step(C02).solids()[0]); print("CONTROL clearance tray moved -2.5x vs C02", cc.measured)
C.append({"check": "clearance (U-03 tray to OD-C02)", "mutant": "relocate: tray moved 2.5 in -X", "got": "FAIL" if cc.measured < 1.5 else "PASS", "measured": cc.measured})
import json; (W / "r07_controls.json").write_text(json.dumps(C, indent=1, default=str))
dump("r07_region.json")
