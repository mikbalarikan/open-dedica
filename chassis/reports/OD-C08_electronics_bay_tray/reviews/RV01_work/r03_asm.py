"""RV01 assembly rows: board placed by the reviewer from the input STEP at the spec §4 joint,
checked against the delivered check assembly; U-03 (a)/(b), D-04c/d, E-01, E-05, REQ-04/05, E-11 openness, plate under holes."""
import sys, math, time; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
import numpy as np
from build123d import Box, Cylinder, Pos, Rot, Plane, Location, Align, Compound
from tools.core import read_step, validity, common_volume
from tools.measure import envelope, clearance, bore_census, locate_bore
from tools.result import Result
A = ["A-02", "A-03", "A-06"]
t = read_step(PART)
e_raw = read_step(E01); c01 = read_step(C01); c02 = read_step(C02)
def one(s):
    ss = s.solids(); assert len(ss) == 1, len(ss); return ss[0]
e_raw, c01, c02 = one(e_raw), one(c01), one(c02)
joint = Location(Plane(origin=(84.0, 80.0, -100.0), x_dir=(0, 0, -1), z_dir=(1, 0, 0)))
board = e_raw.moved(joint)
print("board env", {k: round(v.measured, 4) for k, v in envelope(board).items()})
# delivered assembly
asm = read_step(ASM)
parts = {c.label: c for c in asm.children}
print("asm children", list(parts))
def solid_of(c):
    ss = c.solids(); return ss[0] if len(ss) == 1 else c
ab = solid_of(parts["od_e01_power_pcb"]); at = solid_of(parts["od_c08_tray"])
ac01 = solid_of(parts["od_c01_frame"]); ac02 = solid_of(parts["od_c02_bulkhead"])
for nm, a_, b_ in (("board", ab, board), ("tray", at, t), ("c01", ac01, c01), ("c02", ac02, c02)):
    cv = common_volume(a_, b_)
    print(f"asm {nm}: vol asm {a_.volume:.4f} ref {b_.volume:.4f} common {cv.measured} -> self-match delta {a_.volume - (cv.measured or 0):.6f}")
# validity of each assembly part
for nm, s in (("tray", at), ("board", ab), ("c01", ac01), ("c02", ac02)):
    print("valid", nm, {k: v.measured for k, v in validity(s).items()})

# U-03 (a) plate contact
cl = clearance(t, c01); g("U-03", cl, "==", 0.0, assumes=A, note="flange to OD-C01 clearance (designed contact)")
iv = common_volume(t, c01); g("U-03", iv, "<=", 0.0, assumes=A, note="tray/OD-C01 interference")
# whole tray vs board
iv = common_volume(t, board); g("U-03", iv, "<=", 0.0, assumes=A, note="tray/OD-E01 interference")
g("D-04c", iv, "<=", 0.0, assumes=["A-02"], note="tray/OD-E01 interference")
# seat layers: top 0.3 of each standoff column
seat_xy = [(80.0, -100.0, 5.0), (27.99, -100.01, 5.0), (81.98, -157.52, 3.0), (30.99, -157.51, 3.0)]
for y, z, r in seat_xy:
    layer = t & (Pos(82.138, y, z) * Box(0.3, 2 * r + 0.2, 2 * r + 0.2, align=(Align.MIN, Align.CENTER, Align.CENTER)))
    layer = layer.solids()
    lay = layer[0] if len(layer) == 1 else Compound(layer)
    c = clearance(lay, board); g("U-03", c, "==", 0.0, assumes=A, note=f"seat y{y} z{z} on solder face")
# pins: tray above the seat plane near each pin
pins = {}
for y, z in ((81.98, -157.52), (30.99, -157.51)):
    p = (t & (Pos(82.438, y, z) * Box(3.0, 2.5, 2.5, align=(Align.MIN, Align.CENTER, Align.CENTER)))).solids()
    assert len(p) == 1; pins[(y, z)] = p[0]
    print("pin solid vol", p[0].volume, envelope(p[0])["min_x"].measured, envelope(p[0])["max_x"].measured)
    c = clearance(p[0], board)
    g("D-04d", c, ">=", 0.30, assumes=["A-02"], note=f"pin y{y} z{z} to OD-E01 (hole wall)")
    g("U-03", c, ">=", 0.30, assumes=A, note=f"pin y{y} z{z}")
# rest: tray less pins and less the top 1.0 of each standoff column (x>81.438 within r+0.5)
rest = t
for (y, z), p in pins.items():
    rest = rest - (Pos(82.438, y, z) * Box(3.0, 2.5, 2.5, align=(Align.MIN, Align.CENTER, Align.CENTER)))
for y, z, r in seat_xy:
    rest = rest - (Pos(81.438, y, z) * Box(1.5, 2 * r + 1.0, 2 * r + 1.0, align=(Align.MIN, Align.CENTER, Align.CENTER)))
rest = one(rest)
c = clearance(rest, board); print("rest clearance", c.measured, c.at)
g("D-04c", c, ">=", 0.5, assumes=["A-02"], note="tray less pins and top 1.0 of standoffs to OD-E01 (reads the 1.0 standoff step)")
# second reading: tray less pins and standoff columns entirely (the wall, flange, gussets)
body = t
for (y, z), p in pins.items():
    body = body - (Pos(82.438, y, z) * Box(3.0, 2.5, 2.5, align=(Align.MIN, Align.CENTER, Align.CENTER)))
for y, z, r in seat_xy:
    body = body - (Pos(76.0, y, z) * Box(7.0, 2 * r + 1.0, 2 * r + 1.0, align=(Align.MIN, Align.CENTER, Align.CENTER)))
body = one(body)
c2 = clearance(body, board); print("body clearance", c2.measured, c2.at)
g("E-01", c, ">=", 0.5, assumes=["A-02"], note=f"= D-04c; wall/flange/gussets alone {c2.measured:.4f} at {c2.at}")
g("U-03", c, ">=", 0.5, assumes=A, note="everything else of the board from the tray")
# OD-C02
c = clearance(t, c02); g("U-03", c, ">=", 1.5, assumes=A, note="tray to OD-C02")
c = clearance(board, c02); g("U-03", c, ">=", 10.0, assumes=A, note="OD-E01 to OD-C02")
cv = common_volume(t, c02); g("U-03", cv, "<=", 0.0, assumes=A, note="tray/OD-C02 interference")
eb = envelope(board)
g("U-03", eb["min_x"], ">=", 70.0, assumes=A, note="board zone min_x"); g("U-03", eb["max_x"], "<=", 117.0, assumes=A, note="board zone max_x")
g("U-03", eb["min_z"], ">=", -240.0, assumes=A, note="board zone min_z"); g("U-03", eb["max_z"], "<=", -30.0, assumes=A, note="board zone max_z")
g("U-03", eb["min_y"], ">=", 10.0, assumes=A, note="board zone min_y")
# E-05: board hole axes (located on the placed board) vs tray bores / pins
bcb = bore_census(board); bct = bore_census(t)
print("board bores", [(round(b["diameter"], 3), [round(q, 3) for q in b["start"]], [round(q, 3) for q in b["end"]]) for b in bcb.detail["bores"]][:20])
holes = {"H1": (80.0, -100.0), "H2": (27.99, -100.01), "H5": (81.98, -157.52), "H6": (30.99, -157.51)}
pin_axis = {"H5": (81.98, -157.52), "H6": (30.99, -157.51)}
for h, (y, z) in holes.items():
    lb = locate_bore(bcb, (83.2, y, z), (1, 0, 0))
    st = lb["offset"].detail["start"]; d = lb["diameter"].measured
    print(h, "board hole", d, st, lb["offset"].detail["end"], "offset from spec", lb["offset"].measured)
    if h in ("H1", "H2"):
        lt = locate_bore(bct, (80.0, y, z), (1, 0, 0)); tst = lt["offset"].detail["start"]
        off = math.hypot(tst[1] - st[1], tst[2] - st[2])
    else:
        off = math.hypot(pin_axis[h][0] - st[1], pin_axis[h][1] - st[2])
    g("E-05", Result("axis_offset", off, "mm", at=(82.438, st[1], st[2])), "<=", 0.10, assumes=["A-02", "A-03"], note=f"{h} board hole d{d:.3f} vs tray axis")
# U-03 (b) path: board slid along -X from +5.0 to 0, step 0.25, interference and clearance
worst = 0.0; path = []
for i in range(20, -1, -1):
    dx = i * 0.25
    b = board.moved(Location((dx, 0, 0)))
    cv = common_volume(t, b)
    path.append((dx, cv.measured, cv.status))
    if cv.status != "MEASURED": worst = None; print("path inconcl", dx, cv.reason); break
    worst = max(worst, cv.measured)
print("path", path)
g("U-03", Result("path_interference_max", worst, "mm3", at="dx 5.0..0 step 0.25") if worst is not None else Result("p", None, "mm3", status="INCONCLUSIVE", reason="boolean failed"), "<=", 0.0, assumes=A, note="U-03 (b) path, 21 poses")
# REQ-04: Ø8 cylinders y 4..120 on hole axes
for x, z in ((88.0, -222.0), (106.0, -222.0), (88.0, -78.0), (106.0, -78.0)):
    cyl = Pos(x, 4.0, z) * Rot(-90, 0, 0) * Cylinder(4.0, 116.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    print("driver env", {k: round(v.measured, 3) for k, v in envelope(cyl).items() if k.startswith("m")})
    a1 = common_volume(t, cyl); a2 = common_volume(board, cyl); c = clearance(t, cyl)
    g("REQ-04", a1, "<=", 0.0, assumes=["A-03"], note=f"driver x{x:g} z{z:g} vs tray (clearance {c.measured:.3f} at {c.at})")
    g("REQ-04", a2, "<=", 0.0, assumes=["A-03"], note=f"driver x{x:g} z{z:g} vs board")
# REQ-05 faston box
bx = Pos(85.0, 4.0, -195.0) * Box(32.0, 88.0, 100.0, align=(Align.MIN, Align.MIN, Align.MIN))
g("REQ-05", common_volume(t, bx), "<=", 0.0, assumes=["A-03"], note="box x85..117 y4..92 z-195..-95 vs tray")
# E-11 openness: +X above standoffs; ±Z ends; above
for nm, box in (("open +X (x 85..117, full height over board span)", bx),
                ("open front z -95..-60 above gussets y 25..120", Pos(76.001, 25.0, -95.0) * Box(41.0, 95.0, 35.0, align=(Align.MIN, Align.MIN, Align.MIN))),
                ("open rear z -240..-195 above gussets y 25..120", Pos(76.001, 25.0, -240.0) * Box(41.0, 95.0, 45.0, align=(Align.MIN, Align.MIN, Align.MIN))),
                ("open above y 86..120 at x>76", Pos(76.001, 86.0, -240.0) * Box(41.0, 34.0, 180.0, align=(Align.MIN, Align.MIN, Align.MIN)))):
    g("E-11", common_volume(t, box), "<=", 0.0, assumes=["A-11"], note=nm)
# plate material under each flange hole (A-01): Ø10 x 6 column must be full plate material
for x, z in ((88.0, -222.0), (106.0, -222.0), (88.0, -78.0), (106.0, -78.0)):
    col = Pos(x, -6.0, z) * Rot(-90, 0, 0) * Cylinder(5.0, 6.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    cv = common_volume(c01, col); miss = col.volume - cv.measured
    g("U-03", Result("plate_missing", miss, "mm3", at=(x, -3.0, z)), "<=", 0.0, assumes=["A-01"], note=f"plate under hole x{x:g} z{z:g}: Ø10x6 column, missing material")
    g("REQ-01", Result("plate_missing", miss, "mm3", at=(x, -3.0, z)), "<=", 0.0, assumes=["A-01"], note=f"plate under hole x{x:g} z{z:g}")
    # distance from Ø4 insert hole column to plate boundary (nearest non-top face): via clearance of plate complement
    ring = Pos(x, -6.0, z) * Rot(-90, 0, 0) * Cylinder(2.0, 6.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    out = (Pos(x, -3.0, z) * Box(60, 5.98, 60)) - c01
    os_ = out.solids()
    if os_:
        d = min(clearance(ring, s).measured for s in os_)
        print(f"   hole x{x} z{z}: Ø4 insert hole to nearest plate void/edge within 30: {d:.3f}")
    else:
        print(f"   hole x{x} z{z}: no plate void within 30")
dump("r03_asm.json", {"path": path})
