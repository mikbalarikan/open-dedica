"""WP-02 probe (D2): the OD-C01 plate near its rear edge, OD-C03 + OD-H01 as OD-C01
A-03 places them, and OD-C02's rear end, measured in the machine frame. Measures
only; no gate reads this file. Paths relative to the workspace (pathlib)."""
import json
import math
from pathlib import Path

from build123d import Box, Location, Plane
from tools.core import read_step, validity
from tools.measure import bore_census, clearance, envelope, locate_bore

WS = Path(__file__).resolve().parents[2]
IN = WS / "00_Spec" / "inputs"
OUT = WS / "01_CAD" / "probe" / "probe_placements_v01.json"
out = {}


def res(r):
    d = {"measured": r.measured if not isinstance(r.measured, float) else round(r.measured, 6),
         "unit": r.unit, "status": r.status}
    if r.reason:
        d["reason"] = r.reason
    if r.at is not None:
        d["at"] = r.at
    return d


def env(s):
    return {k: round(v.measured, 4) for k, v in envelope(s).items()}


def box(x0, x1, y0, y1, z0, z1):
    return Box(x1 - x0, y1 - y0, z1 - z0).moved(Location(((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)))


def one(shape):
    s = shape.solids()
    return s[0] if len(s) == 1 else shape


# --- plate at the identity
plate = one(read_step(IN / "OD-C01_base_frame.step"))
out["plate_validity"] = {k: res(v) for k, v in validity(plate).items()}
out["plate_envelope"] = env(plate)
ymax = envelope(plate)["max_y"].measured
tops = [f for f in plate.faces() if f.geom_type.name == "PLANE" and f.normal_at().Y > 0.9999
        and abs(f.center().Y - ymax) < 1e-3]
out["plate_top_face"] = {"y": round(ymax, 6), "faces": len(tops), "area_mm2": round(sum(f.area for f in tops), 3)}
rear = [f for f in plate.faces() if f.geom_type.name == "PLANE" and f.normal_at().Z < -0.9999]
out["plate_rear_faces"] = [{"z": round(f.center().Z, 6), "x_min": round(f.bounding_box().min.X, 4),
                            "x_max": round(f.bounding_box().max.X, 4)} for f in rear]
sides = [f for f in plate.faces() if f.geom_type.name == "PLANE" and abs(f.normal_at().X) > 0.9999]
out["plate_side_faces"] = [{"x": round(f.center().X, 6), "z_min": round(f.bounding_box().min.Z, 4),
                            "z_max": round(f.bounding_box().max.Z, 4)} for f in sides]
corners = []
for f in plate.faces():
    if f.geom_type.name != "CYLINDER":
        continue
    bb = f.bounding_box()
    if bb.max.Z > -250 or (bb.max.Y - bb.min.Y) < 5.9:
        continue
    corners.append({"radius": round(f.radius, 6), "axis_origin": [round(v, 4) for v in tuple(f.axis_of_rotation.position)],
                    "axis_dir": [round(v, 6) for v in tuple(f.axis_of_rotation.direction)],
                    "bbox_min": [round(bb.min.X, 4), round(bb.min.Y, 4), round(bb.min.Z, 4)],
                    "bbox_max": [round(bb.max.X, 4), round(bb.max.Y, 4), round(bb.max.Z, 4)]})
out["plate_cylinders_near_rear"] = corners
# where the corner arc lies at x = +-116 (the wall's ends): a ray of material along -Z at x 116, y -3
for x in (116.0, -116.0, 114.0, -114.0):
    probe = box(x - 0.0005, x + 0.0005, -3.0005, -2.9995, -320.0, -280.0)
    common = plate & probe
    zs = [v.Z for so in (common.solids() if common else []) for v in so.vertices()]
    out[f"plate_rear_edge_at_x{x:g}"] = round(min(zs), 4) if zs else None
bc = bore_census(plate)
out["plate_bore_census_count"] = bc.measured
out["plate_bores"] = [{"diameter": round(b["diameter"], 4), "start": [round(v, 4) for v in b["start"]],
                       "end": [round(v, 4) for v in b["end"]], "axis_dir": [round(v, 6) for v in b["axis_dir"]],
                       "through": b.get("through")} for b in bc.detail.get("bores", [])]
for x, z in ((110.0, -295.0), (-110.0, -295.0)):
    L = locate_bore(bc, (x, -3.0, z), (0, 1, 0))
    out[f"plate_feet_hole_({x:g},{z:g})"] = {k: res(v) for k, v in L.items()}
# the four new insert positions (A-01): nearest existing hole centre, plate edge distance
new = [(81.0, -290.0), (100.0, -290.0), (-81.0, -290.0), (-100.0, -290.0)]
rows = {}
for x, z in new:
    near = min(((math.hypot(b["start"][0] - x, b["start"][2] - z), b) for b in bc.detail.get("bores", [])
                if abs(abs(b["axis_dir"][1]) - 1) < 1e-6), key=lambda t: t[0])
    rows[f"({x:g},{z:g})"] = {"nearest_hole_centre_mm": round(near[0], 4),
                              "nearest_hole": [round(near[1]["start"][0], 4), round(near[1]["start"][2], 4),
                                               round(near[1]["diameter"], 4)]}
out["new_insert_positions"] = rows

# --- OD-C02 at the identity
c02 = one(read_step(IN / "OD-C02_bulkhead.step"))
out["c02_validity"] = {k: res(v) for k, v in validity(c02).items()}
out["c02_envelope"] = env(c02)

# --- OD-C03 + OD-H01 as OD-C01 A-03 places them
L03 = Location(Plane(origin=(0, 40, -205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))
out["c03_location_matrix_rows"] = [[round(v, 6) for v in row] for row in
                                   [list(r) for r in L03.to_tuple()]] if hasattr(L03, "to_tuple") else str(L03)
c03 = one(read_step(IN / "OD-C03_pump_cradle.step"))
h01 = read_step(IN / "OD-H01_ulka_ep5_pump.step")
out["c03_local_envelope"] = env(c03)
out["h01_local_envelope"] = env(h01)
c03p, h01p = c03.moved(L03), h01.moved(L03)
out["c03_validity"] = {k: res(v) for k, v in validity(c03).items()}
out["h01_validity"] = {k: res(v) for k, v in validity(h01).items()}
out["c03_placed_envelope"] = env(c03p)
out["h01_placed_envelope"] = env(h01p)
# local axes after placement
for name, v in (("x", (1, 0, 0)), ("y", (0, 1, 0)), ("z", (0, 0, 1))):
    from build123d import Vector
    w = L03 * Location(Vector(*v))
    p0 = L03.position
    out[f"c03_local_{name}_maps_to"] = [round(a - b, 6) for a, b in zip(tuple(w.position), tuple(p0))]
# foot underside on y 0: the lowest planar face facing -Y
lows = [f for f in c03p.faces() if f.geom_type.name == "PLANE" and f.normal_at().Y < -0.9999]
lowest = min(lows, key=lambda f: f.center().Y) if lows else None
out["c03_foot_underside_y"] = round(lowest.center().Y, 6) if lowest else None
plane283 = box(-130, 130, 0, 260, -283.0005, -282.9995)
for n, s in (("c03", c03p), ("h01", h01p), ("c02", c02)):
    c = clearance(s, plane283)
    out[f"{n}_to_plane_z-283"] = res(c) | {"on_part": c.detail.get("on_a"), "on_plane": c.detail.get("on_b")}
    c2 = clearance(s, plate)
    out[f"{n}_to_plate"] = res(c2)
print(json.dumps(out, indent=1, default=str))
OUT.write_text(json.dumps(out, indent=1, default=str))
