"""Tray/OD-E01 interference without the whole-solid boolean (blind on this seat contact, control r06/r07):
decomposition by measured planes + clearance, each with its own control. Path by clearance per pose."""
import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from build123d import *
from tools.core import read_step
from tools.measure import clearance, envelope
from tools.result import Result
import json
A = ["A-02", "A-03", "A-06"]
t = Solid(read_step(PART).wrapped)
board = read_step(E01).solids()[0].moved(Location(Plane(origin=(84.0, 80.0, -100.0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))))
XCYL = lambda x0, y, z, r, L: Pos(x0, y, z) * Rot(0, 90, 0) * Cylinder(r, L, align=(Align.CENTER, Align.CENTER, Align.MIN))
BOX = lambda x0, y0, z0, dx, dy, dz: Pos(x0, y0, z0) * Box(dx, dy, dz, align=(Align.MIN, Align.MIN, Align.MIN))
PINS = ((81.98, -157.52), (30.99, -157.51))
eb = envelope(board); bx0 = eb["min_x"].measured
def overlap_depth(s):
    """How far the tray, less its two pins, reaches past the board's lowest x inside the board's y/z footprint (+1 mm)."""
    s2 = s
    for py, pz in PINS:
        s2 = s2 - (Pos(82.438, py, pz) * Box(4.0, 3.0, 3.0, align=(Align.MIN, Align.CENTER, Align.CENTER)))
    foot = s2 & BOX(70, eb["min_y"].measured - 1, eb["min_z"].measured - 1, 50, eb["size_y"].measured + 2, eb["size_z"].measured + 2)
    fs = foot.solids(); foot = fs[0] if len(fs) == 1 else Compound(fs)
    e = envelope(foot)
    if e["max_x"].status != "MEASURED":
        print("   envelope inconclusive:", e["max_x"].reason, "solids", len(fs)); return Result("overlap_depth", None, "mm", status="INCONCLUSIVE", reason=e["max_x"].reason)
    return Result("overlap_depth", e["max_x"].measured - bx0, "mm", at=f"tray less pins in the board footprint: max x {e['max_x'].measured:.4f} vs board min x {bx0:.4f}")
def pin_gap(s):
    gaps = []
    for py, pz in PINS:
        p = (s & (Pos(82.438, py, pz) * Box(3.0, 2.6, 2.6, align=(Align.MIN, Align.CENTER, Align.CENTER)))).solids()[0]
        gaps.append(clearance(p, board).measured)
    return min(gaps)
od = overlap_depth(t); pg = pin_gap(t)
print("overlap depth", od.measured, od.at, "pin gap", pg)
g("U-03", od, "<=", 0.0, assumes=A, note=f"tray/OD-E01 interference by decomposition: tray less pins reaches x {bx0 + od.measured:.4f} = board's solder face (contact, no overlap); pins clear by {pg:.4f} > 0")
g("D-04c", od, "<=", 0.0, assumes=["A-02"], note="tray/OD-E01 interference by decomposition (seat contact only)")
m10 = (t - XCYL(76.0, 80.0, -100.0, 5.0, 6.438))
m10 = (m10 + (XCYL(76.0, 80.0, -100.0, 5.0, 6.498) - XCYL(76.438, 80.0, -100.0, 2.0, 6.2))).solids()[0]
from tools.core import common_volume
cvm = common_volume(m10, board); print("CONTROL whole-tray common_volume, H1 standoff rebuilt 0.06 taller:", cvm.measured)
cvt = common_volume(t.moved(Location((0.06, 0, 0))), board); print("CONTROL whole-tray common_volume, tray moved +0.06 x:", cvt.measured)
C0 = [{"check": "common_volume whole tray vs OD-E01 (U-03, D-04c)", "mutant": "resize: H1 standoff rebuilt 0.06 taller", "got": "FAIL" if cvm.measured > 0.001 else "PASS", "measured": cvm.measured},
      {"check": "common_volume whole tray vs OD-E01 (U-03, D-04c)", "mutant": "relocate: tray moved 0.06 in +X", "got": "FAIL" if cvt.measured > 0.001 else "PASS", "measured": cvt.measured}]
oc = overlap_depth(m10); print("CONTROL decomposition seat+0.06:", oc.measured)
C = C0 + [{"check": "interference by decomposition (envelope of the tray less pins in the board footprint vs the board's solder face; U-03, D-04c)", "mutant": "resize: H1 standoff rebuilt 0.06 taller", "got": "FAIL" if oc.measured > 0.005 else "PASS", "measured": oc.measured}]
# path: clearance tray to board at dx 5.0 .. 0.25 (step 0.25) must stay > 0, at dx 0 the decomposition above
res = []
for i in range(20, 0, -1):
    dx = i * 0.25; c = clearance(t, board.moved(Location((dx, 0, 0)))); res.append((dx, c.measured, c.at))
mn = min(res, key=lambda r: r[1]); print("path clearances", [(r[0], round(r[1], 4)) for r in res])
g("U-03", Result("path_min_clearance", mn[1], "mm", at=f"dx {mn[0]} at {mn[2]}"), ">=", 0.001, assumes=A, note="U-03 (b): board slid along -X from +5.0, 20 poses at 0.25 steps, clearance > 0 at every pose (no overlap), seat met at dx 0")
m11 = ((t - XCYL(82.438, 81.98, -157.52, 0.9, 2.6)) + XCYL(82.438, 82.48, -157.52, 0.9, 2.5)).solids()[0]
cm = min(clearance(m11, board.moved(Location((dx, 0, 0)))).measured for dx in (2.0, 1.5, 1.0, 0.5))
print("CONTROL path clearance pin+0.5y:", cm)
C.append({"check": "clearance along the path (U-03 b)", "mutant": "relocate: H5 pin moved 0.5 in +Y", "got": "FAIL" if cm < 0.001 else "PASS", "measured": cm})
# REQ-04 board vs driver cylinders by clearance as well
for x, z in ((88.0, -222.0), (106.0, -222.0), (88.0, -78.0), (106.0, -78.0)):
    cyl = Pos(x, 4.0, z) * Rot(-90, 0, 0) * Cylinder(4.0, 116.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    c = clearance(board, cyl); print("board to driver", x, z, c.measured, c.at)
    g("REQ-04", c, ">=", 0.0, assumes=["A-03"], note=f"board to driver cylinder x{x:g} z{z:g} (clearance corroboration)")
(W / "r08_controls.json").write_text(json.dumps(C, indent=1, default=str))
dump("r08_contact.json", {"path": res})
