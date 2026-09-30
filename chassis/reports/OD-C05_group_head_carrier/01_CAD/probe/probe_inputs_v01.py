"""WP-02 probe (J2, D2): measure the OD-G01 build v02 and OD-G04 inputs for the carrier plan.
Measures only; builds no carrier geometry. Paths relative to the workspace."""
import json, math, sys
from pathlib import Path

from build123d import Axis, Plane, Pos, Rot, Box, Cylinder, Compound, Face, Location
from tools.core import read_step, validity
from tools.measure import bore_census, locate_bore, envelope, feature_census, clearance, radial_extent

WS = Path(__file__).resolve().parents[2]
IN = WS / "00_Spec" / "inputs"
out = {}

def res(r):
    return {"measured": r.measured, "unit": r.unit, "status": r.status, "reason": r.reason, "at": r.at}

def env(shape):
    e = envelope(shape)
    return {k: round(v.measured, 6) for k, v in e.items()}

# ---------- OD-G01 ----------
g01 = read_step(IN / "OD-G01_housing_C1_v02.step")
out["g01_validity"] = {k: res(v) for k, v in validity(g01).items()}
out["g01_envelope"] = env(g01)

# planar faces facing -Z: z and area
rear = []
for f in g01.faces():
    if f.geom_type.name == "PLANE":
        n = f.normal_at()
        if n.Z < -0.999:
            rear.append({"z": round(f.center().Z, 6), "area": round(f.area, 4)})
rear.sort(key=lambda d: d["z"])
out["g01_down_planes"] = rear
zmin = out["g01_envelope"]["min_z"]
rear_face = [f for f in g01.faces() if f.geom_type.name == "PLANE" and f.normal_at().Z < -0.999
             and abs(f.center().Z - zmin) < 1e-3]
out["g01_rear_face_count"] = len(rear_face)
rf = rear_face[0]
bb = rf.bounding_box()
out["g01_rear_face"] = {"z": round(rf.center().Z, 6), "area": round(rf.area, 4),
                        "bbox": [round(bb.min.X, 4), round(bb.min.Y, 4), round(bb.max.X, 4), round(bb.max.Y, 4)],
                        "inner_wires": len(rf.inner_wires())}
# openings in the rear face: each inner wire's bbox, centre and radial reach
holes = []
for w in rf.inner_wires():
    b = w.bounding_box()
    cx, cy = (b.min.X + b.max.X) / 2, (b.min.Y + b.max.Y) / 2
    reach = max(math.hypot(v.X, v.Y) for v in w.edges().vertices()) if w.edges().vertices() else None
    # radial reach from sampled points
    pts = [w.position_at(t / 200) for t in range(201)]
    rmax = max(math.hypot(p.X, p.Y) for p in pts)
    holes.append({"centre": [round(cx, 4), round(cy, 4)], "size": [round(b.size.X, 4), round(b.size.Y, 4)],
                  "r_centre": round(math.hypot(cx, cy), 4), "r_max": round(rmax, 4)})
out["g01_rear_face_openings"] = sorted(holes, key=lambda h: h["r_centre"])
# outer wire of the rear face: corner arcs
corners = []
for e in rf.outer_wire().edges():
    if e.geom_type.name == "CIRCLE":
        corners.append({"radius": round(e.radius, 4), "centre": [round(e.arc_center.X, 4), round(e.arc_center.Y, 4)]})
out["g01_rear_outline_arcs"] = corners
out["g01_rear_outline_edges"] = len(rf.outer_wire().edges())

# bores
bc = bore_census(g01)
bores = bc.detail["bores"]
out["g01_bore_count"] = bc.measured
out["g01_bores"] = [{"d": round(b["diameter"], 4), "axis": [round(a, 4) for a in b["axis_dir"]],
                     "start": [round(a, 4) for a in b["start"]], "end": [round(a, 4) for a in b["end"]],
                     "len": round(b["length"], 4), "through": b.get("through"), "open_ends": b.get("open_ends")}
                    for b in bores]
ins = {}
for sx in (1, -1):
    for sy in (1, -1):
        L = locate_bore(bc, (44.0 * sx, 44.0 * sy, -24.94 + 2.85), (0, 0, 1))
        ins[f"({44*sx},{44*sy})"] = {k: res(v) | {"detail": {kk: vv for kk, vv in v.detail.items()}} for k, v in L.items()}
out["g01_insert_bores"] = ins
hub = locate_bore(bc, (0, 0, -22.44), (0, 0, 1))
out["g01_hub_bore"] = {k: res(v) for k, v in hub.items()}
out["g01_feature_census"] = {k: v.measured for k, v in feature_census(g01).items()}

# material behind the rear face?  count solid volume below z_rear - 0.001
from build123d import Box as B
cut = B(400, 400, 100, align=None).moved(Location((-200, -200, -24.94 - 100 - 0.001)))
behind = g01 & cut
out["g01_volume_behind_rear_face_mm3"] = round(sum(s.volume for s in behind.solids()), 6) if behind else 0.0

# ---------- OD-G04 ----------
g04 = read_step(IN / "OD-G04_brewing_gasket_support.step")
out["g04_validity"] = {k: res(v) for k, v in validity(g04).items()}
out["g04_envelope_own"] = env(g04)
# plate back face: planar faces facing +Z, the highest large one
ups = sorted([{"z": round(f.center().Z, 5), "area": round(f.area, 3)} for f in g04.faces()
              if f.geom_type.name == "PLANE" and f.normal_at().Z > 0.999], key=lambda d: -d["area"])
out["g04_up_planes_by_area"] = ups[:6]
downs = sorted([{"z": round(f.center().Z, 5), "area": round(f.area, 3)} for f in g04.faces()
                if f.geom_type.name == "PLANE" and f.normal_at().Z < -0.999], key=lambda d: d["z"])
out["g04_down_planes"] = downs
# tab 1 angle: outermost material at z of tabs, angle sweep in own frame
tab = []
for a10 in range(-300, 3600, 5):
    a = a10 / 10
    r = radial_extent(g04, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, -8.0)
    if r.status == "MEASURED":
        tab.append((a, r.measured))
rmax = max(t[1] for t in tab)
out["g04_outer_radius_at_z-8"] = round(rmax, 4)

# place as OD-G01 REPORT v02 section 5: rotate +6.05 deg about Z, then z -6.82
g04p = g04.rotate(Axis.Z, 6.05).translate((0, 0, -6.82))
out["g04_placed_envelope"] = env(g04p)
out["g04_placed_min_z"] = out["g04_placed_envelope"]["min_z"]
# hub tube bottom: lowest -Z planar annular face near the axis
hubf = []
for f in g04p.faces():
    if f.geom_type.name == "PLANE" and f.normal_at().Z < -0.999:
        c = f.center()
        bbf = f.bounding_box()
        hubf.append({"z": round(c.Z, 4), "centre_r": round(math.hypot(c.X, c.Y), 3),
                     "r_extent": round(max(abs(bbf.min.X), abs(bbf.max.X), abs(bbf.min.Y), abs(bbf.max.Y)), 3),
                     "area": round(f.area, 3)})
out["g04_placed_down_planes"] = sorted(hubf, key=lambda d: d["z"])
# largest radius of OD-G04 material below the housing floor z -19.94 and below the rear face
def rmax_below(shape, zcut):
    box = B(400, 400, 200, align=None).moved(Location((-200, -200, zcut - 200)))
    part = shape & box
    ss = part.solids() if part else []
    if not ss:
        return None, 0.0
    r = 0.0
    for s in ss:
        for v in s.vertices():
            r = max(r, math.hypot(v.X, v.Y))
        for e in s.edges():
            for t in range(21):
                p = e.position_at(t / 20)
                r = max(r, math.hypot(p.X, p.Y))
    return round(r, 4), round(sum(s.volume for s in ss), 4)
out["g04_below_floor_-19.94"] = rmax_below(g04p, -19.94)
out["g04_below_rear_-24.94"] = rmax_below(g04p, -24.94)
out["g04_placed_vs_g01_clearance"] = res(clearance(g04p, g01))

# pre-build estimate only (not a gate, not the carrier): clearance from placed OD-G04 to a probe
# slab occupying the carrier wall region z -29.94..-24.94 with the r<=30 hub window removed
slab = B(100, 200, 5, align=None).moved(Location((-50, -150, -29.94))) - Cylinder(30, 20).moved(Location((0, 0, -27.44)))
c = clearance(g04p, slab)
out["estimate_g04_to_probe_slab_with_R30_window"] = res(c) | {"on_b": c.detail["on_b"]}
c2 = clearance(g01, slab)
out["estimate_g01_to_probe_slab"] = res(c2)
out["estimate_g01_probe_slab_common_mm3"] = round(sum(s.volume for s in (g01 & slab).solids()), 6) if (g01 & slab) else 0.0

print(json.dumps(out, indent=1, default=str))
(WS / "01_CAD" / "probe" / "probe_inputs_v01.json").write_text(json.dumps(out, indent=1, default=str))
