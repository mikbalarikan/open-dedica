"""RV01: assembly rows U-03 (a)(b), REQ-05, REQ-08 on the panel and reference solids placed by me from the
inputs (and compared with the designer's assembly STEP). Args: part_step [out]."""
import json, sys, math
import numpy as np
from build123d import Box, Cylinder, Location, Plane, Pos, Rot, Vector, Face, Compound
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common, BRepAlgoAPI_Cut
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
from tools.core import read_step, common_volume, validity
from tools.measure import clearance, bore_census, envelope
J = "/root/oguz-jobs/20261001-od-c11-back-panel"
STEP = sys.argv[1] if len(sys.argv) > 1 else f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"
OUT = sys.argv[2] if len(sys.argv) > 2 else f"{J}/reviews/RV01_work/m5_assy.json"
FULL = (len(sys.argv) <= 3) or sys.argv[3] == "full"
I = f"{J}/00_Spec/inputs"
panel = read_step(STEP)
plate = read_step(f"{I}/OD-C01_base_frame.step")
bulk = read_step(f"{I}/OD-C02_bulkhead.step")
loc = Location(Plane(origin=(0, 40, -205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))
cradle = read_step(f"{I}/OD-C03_pump_cradle.step").moved(loc)
pump = read_step(f"{I}/OD-H01_ulka_ep5_pump.step").moved(loc)
refs = {"od_c01": plate, "od_c02": bulk, "od_c03": cradle, "od_h01": pump}
out = {}
def rd(r): return r.to_dict()
def area(shape):
    g = GProp_GProps(); BRepGProp.SurfaceProperties_s(shape.wrapped if hasattr(shape, "wrapped") else shape, g); return g.Mass()
def dist(a, b):
    d = BRepExtrema_DistShapeShape(a.wrapped if hasattr(a, "wrapped") else a, b.wrapped if hasattr(b, "wrapped") else b)
    d.Perform(); return d.Value(), d.PointOnShape1(1), d.PointOnShape2(1)
# placements read back
for k, s in refs.items():
    e = envelope(s); out[f"env_{k}"] = {kk: v.measured for kk, v in e.items()}
print({k: (out[f"env_{k}"]["min_z"], out[f"env_{k}"]["max_z"], out[f"env_{k}"]["min_y"]) for k in refs})
# compare with the designer's assembly children
if FULL:
    asm = read_step(f"{J}/02_STEP_STL/od_c11_assembly_C1_v03.step")
    kids = {c.label: c for c in asm.children}
    out["asm_labels"] = list(kids)
    mine = {"od_c11_back": panel, "od_c01_frame": plate, "od_c02_bulkhead": bulk, "od_c03_cradle": cradle, "od_h01_pump": pump}
    cmp = {}
    for lab, s in mine.items():
        k = kids.get(lab)
        if k is None: cmp[lab] = "missing"; continue
        cv = common_volume(s, k); va = s.volume; vb = k.volume
        cmp[lab] = {"mine": va, "theirs": vb, "common": cv.measured, "status": cv.status}
    out["asm_compare"] = cmp; print("asm", cmp)
# U-03 (a) contact with the plate
out["plate_clearance"] = rd(clearance(panel, plate)); out["plate_common"] = rd(common_volume(panel, plate))
print("plate", out["plate_clearance"]["measured"], out["plate_common"]["measured"])
# footprint: the panel's faces at y 0 facing -Y; plate top faces at y 0 facing +Y
def faces_at(shape, y, ny):
    fs = []
    for f in shape.faces():
        if f.geom_type.name != "PLANE": continue
        bb = f.bounding_box()
        if abs(bb.min.Y - y) < 1e-6 and abs(bb.max.Y - y) < 1e-6:
            n = f.normal_at(f.center())
            if abs(n.Y - ny) < 1e-6: fs.append(f)
    return fs
foot = faces_at(panel, 0.0, -1.0); top = faces_at(plate, 0.0, 1.0)
out["footprint_faces"] = len(foot); out["plate_top_faces"] = len(top)
F = foot[0]; T = top[0]
A_foot = F.area
common_ft = Face  # placeholder
c = BRepAlgoAPI_Common(F.wrapped, T.wrapped); c.Build(); A_common = area(c.Shape())
# outline: the plate top face's outer wire as a face without holes
outline = Face(T.outer_wire()); c2 = BRepAlgoAPI_Common(F.wrapped, outline.wrapped); c2.Build(); A_in_outline = area(c2.Shape())
out["footprint_area"] = A_foot; out["area_outside_outline"] = A_foot - A_in_outline; out["area_over_holes"] = A_in_outline - A_common
d_out, p1, p2 = dist(T.outer_wire(), F)
out["footprint_to_outline"] = {"d": d_out, "at_outline": (p1.X(), p1.Y(), p1.Z()), "at_foot": (p2.X(), p2.Y(), p2.Z())}
print("footprint", A_foot, out["area_outside_outline"], out["area_over_holes"], out["footprint_to_outline"])
# split at the wall's inner face z -299 (nominal plane; the wall's inner face reads -299.000 by REQ-02)
zin = -299.0
wallbox = Box(400, 10, 200).moved(Location((0, 0, zin - 100)))
flbox = Box(400, 10, 200).moved(Location((0, 0, zin + 100)))
def part(face, box):
    cc = BRepAlgoAPI_Common(face.wrapped, box.wrapped); cc.Build(); return Compound(cc.Shape())
wallfoot, flanges = part(F, wallbox), part(F, flbox)
out["wallfoot_area"] = area(wallfoot); out["flange_area"] = area(flanges)
pb = bore_census(plate); yb = [b for b in pb.detail["bores"] if abs(abs(b["axis_dir"][1]) - 1) < 1e-6]
out["plate_bores_along_y"] = len(yb); out["plate_bores_total"] = pb.measured
rims = []
from build123d import Edge, Axis
for b in yb:
    x, z, r = b["start"][0], b["start"][2], b["radius"]
    rim = Edge.make_circle(r, Plane(origin=(x, 0, z), z_dir=(0, 1, 0)))
    dw = dist(rim, wallfoot)[0]; df = dist(rim, flanges)[0]
    rims.append({"x": x, "z": z, "d": 2 * r, "rim_to_wallfoot": dw, "rim_to_flanges": df})
out["rims"] = rims
mw = min(rims, key=lambda q: q["rim_to_wallfoot"]); mf = min(rims, key=lambda q: q["rim_to_flanges"])
out["rim_wallfoot_min"] = mw; out["rim_flange_min"] = mf
print("rims", len(yb), "wall", mw, "flange", mf)
# under each flange hole: plug d3.4 x 6 along the hole axis inside the plate; nearest existing hole centre
under = {}
for (x, z) in [(81, -282), (95, -282), (-81, -282), (-95, -282)]:
    plug = Pos(x, -3, z) * Rot(90, 0, 0) * Cylinder(1.7, 6.0)
    cv = common_volume(plug, plate)
    near = min(math.hypot(b["start"][0] - x, b["start"][2] - z) for b in yb)
    under[f"{x}"] = {"plug": plug.volume, "common": cv.measured, "missing": plug.volume - cv.measured, "nearest_centre": near}
out["under_holes"] = under; print("under", under)
# neighbours
for k in ("od_c02", "od_c03", "od_h01"):
    out[f"clear_{k}"] = rd(clearance(panel, refs[k])); out[f"common_{k}"] = rd(common_volume(panel, refs[k]))
    print(k, out[f"clear_{k}"]["measured"], out[f"clear_{k}"]["at"], out[f"common_{k}"]["measured"])
# U-03 (b) lowering along -Y from +40 in 1.0 steps
if FULL:
    worst = {k: 0.0 for k in refs}; inc = []
    for i in range(0, 41):
        dy = 40.0 - i
        m = panel.moved(Location((0, dy, 0)))
        for k, s in refs.items():
            cv = common_volume(m, s)
            if cv.status != "MEASURED": inc.append((dy, k, cv.reason)); continue
            worst[k] = max(worst[k], cv.measured)
    out["lowering"] = {"poses": 41, "step": 1.0, "worst": worst, "inconclusive": inc}; print("lowering", out["lowering"])
# REQ-05 keep-out
box = Box(140, 100, 48.8).moved(Location((0, 50, (-298.8 - 250) / 2)))
out["req05_box"] = rd(common_volume(box, panel)); print("req05", out["req05_box"]["measured"])
# REQ-08 driver cylinders d6 y 4..260
r8 = {}
for (x, z) in [(81, -282), (95, -282), (-81, -282), (-95, -282)]:
    cyl = Pos(x, 132, z) * Rot(90, 0, 0) * Cylinder(3.0, 256.0)
    cyl2 = Pos(x, 132.25, z) * Rot(90, 0, 0) * Cylinder(3.0, 255.5)
    r8[f"{x}"] = {"common": common_volume(cyl, panel).measured, "clear_above_4p5": clearance(cyl2, panel).measured,
                  "clear_at": clearance(cyl2, panel).at}
out["req08"] = r8; print("req08", r8)
json.dump(out, open(OUT, "w"), indent=1, default=str)
