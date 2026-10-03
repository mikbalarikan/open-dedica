"""REQ-01 ... REQ-07 and the cap measurements."""
from common import *
from tools.measure import clearance, envelope, bore_census, locate_bore, radial_extent
from tools.core import common_volume
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeFace
from build123d import Edge, Wire, Face, ShapeList
out = {}
s, ss = part(); P = Solid(ss[0])
r = refs(); E = r["E02"]; G = r["G10"]
pc = bore_census(P)
# REQ-01
req01 = []
for x in (-95, -85, 85, 95):
    lb = locate_bore(pc, (x, 2.0, 77.0), (0, 1, 0))
    req01.append({k: v.measured for k, v in lb.items()} | {"x": x, "at": lb["diameter"].at})
out["REQ01"] = req01
# underside faces: planar faces with outward normal -Y
under = []
for f in P.faces():
    if f.geom_type.name == "PLANE":
        n = f.normal_at(f.center())
        if n.Y < -0.999:
            under.append(round(f.center().Y, 6))
out["underside_y"] = sorted(set(under)); out["env"] = {k: v.measured for k, v in envelope(P).items()}
# REQ-02: line probes along +Z via radial_extent (axis along X through (x, y, 0); ray along +Z)
req02 = []
for (x, y) in [(-100, 100), (100, 100), (-100, 200), (0, 200), (100, 200), (-110, 30), (110, 30)]:
    o = radial_extent(P, (x, y, 0), (1, 0, 0), (0, 0, 1), 0.0, 0.0, side="outer", r_min=85, r_max=120)
    i = radial_extent(P, (x, y, 0), (1, 0, 0), (0, 0, 1), 0.0, 0.0, side="inner", r_min=85, r_max=120)
    req02.append({"x": x, "y": y, "outer": o.measured, "inner": i.measured, "st": (o.status, i.status), "mat": o.detail.get("material")})
out["REQ02"] = req02
# REQ-03 section edges at z 95.5
sec = BRepAlgoAPI_Section(P.wrapped, gp_Pln(gp_Pnt(0, 0, 95.5), gp_Dir(0, 0, 1)))
sec.Build()
edges = list(Compound(sec.Shape()).edges())
lines = []
for e in edges:
    if e.geom_type.name == "LINE":
        a, b = e.start_point(), e.end_point()
        lines.append((round(a.X, 4), round(a.Y, 4), round(b.X, 4), round(b.Y, 4)))
out["sec_z95p5_lines"] = sorted(lines)
out["sec_z95p5_circles"] = sorted({(round(e.arc_center.X, 4), round(e.arc_center.Y, 4), round(e.radius, 4)) for e in edges if e.geom_type.name == "CIRCLE"})
slot = box(-74.8, 74.8, 0.2, 49.8, 93.8, 97.2); win = box(-57.3, 74.8, 0.2, 187.8, 93.8, 97.2)
out["REQ03_boxes"] = [common_volume(P, slot).measured, common_volume(P, win).measured]
# REQ-03 / positive side: boxes grown 0.1 per side touch material at each edge
grown = {"slot_left": box(-75.1, -74.9, 1, 49, 94.5, 96.5), "slot_top_left": box(-74, -58.5, 49.9, 50.1, 94.5, 96.5),
         "win_left": box(-57.6, -57.4, 51, 187, 94.5, 96.5), "right": box(74.9, 75.1, 1, 187, 94.5, 96.5), "top": box(-57, 74, 187.9, 188.1, 94.5, 96.5)}
out["REQ03_edge_bands"] = {k: common_volume(P, b).measured for k, b in grown.items()}
# REQ-06
req06 = {}
for (x, z, y0) in [(-95, 77, 4), (-85, 77, 4), (85, 77, 4), (95, 77, 4), (-110, 90, 2), (110, 90, 2)]:
    c = cyl_y(x, z, 3.0, y0, 260.0)
    req06[f"{x},{z}"] = (common_volume(P, c).measured, clearance(P, c).measured)
out["REQ06"] = req06
# REQ-07
tray = box(-74.8, 74.8, 0, 49.8, -15, 120)
knob = cyl_z(95.5, 140.0, 16.0, 60, 93.8)
out["REQ07"] = {"min_z": envelope(P)["min_z"].measured, "tray": common_volume(P, tray).measured, "knob": common_volume(P, knob).measured,
                "tray_gap": clearance(P, tray).measured, "knob_gap": clearance(P, knob).measured}
print(json.dumps(out, indent=1, default=str), flush=True)
# REQ-04: caps. foremost point in each hole window by distance to a slab at z 100 over the window
holes = {"B1": (-94.2478, 166.5135), "B2": (-98.9908, 139.9014), "B3": (-93.7652, 113.4263)}
caps = {}
for k, (x, y) in holes.items():
    slab = box(x - 7.4, x + 7.4, y - 7.4, y + 7.4, 100.0, 101.0)
    c = clearance(E, slab)
    caps[k] = {"top_z": 100.0 - c.measured, "at": c.at, "on_slab": c.detail["on_b"]}
    # cap axis: centroids of E02 sections inside the window at several levels
    cents = {}
    for z in (89.5, 91.0, 92.5, 94.0, 95.0, 95.5):
        sec = BRepAlgoAPI_Section(E.wrapped, gp_Pln(gp_Pnt(0, 0, z), gp_Dir(0, 0, 1))); sec.Build()
        es = list(Compound(sec.Shape()).edges())
        es = [e for e in es if abs(e.center().X - x) < 7.4 and abs(e.center().Y - y) < 7.4]
        if not es:
            cents[z] = None; continue
        try:
            wires = Wire.combine(es)
            fs = [Face(w) for w in wires if w.is_closed]
            if not fs:
                cents[z] = ("open", len(es)); continue
            fbig = max(fs, key=lambda f: f.area)
            cc = fbig.center()
            cents[z] = (round(cc.X, 4), round(cc.Y, 4), round(fbig.area, 3), len(fs))
        except Exception as ex:
            cents[z] = ("err", str(ex)[:80])
    caps[k]["centroids"] = cents
    print(k, caps[k], flush=True)
out["caps"] = caps
dump("s03_req.json", out)
