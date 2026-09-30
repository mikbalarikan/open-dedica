"""WP-02 probe (J2, D2): place OD-C03 (+OD-H01), OD-C04 (+OD-H11), OD-G01 v02 and the
OD-C05 foot reference box by the joints of spec 1.0 section 4, and measure them.
Measures only: the plate is represented by a reference slab (x +-120, y -6..0,
z -305..+100, no corners, no holes) for pre-build estimates, never a gate.
Paths relative to the workspace (pathlib)."""
import json, math, itertools
from pathlib import Path

import numpy as np
from build123d import Box, Location, Plane, Pos, Vector
from tools.core import read_step, validity, common_volume
from tools.measure import bore_census, locate_bore, envelope, clearance

WS = Path(__file__).resolve().parents[2]
IN = WS / "00_Spec" / "inputs"
OUT = WS / "01_CAD" / "probe" / "probe_placements_v01.json"
out = {}


def res(r):
    d = {"measured": None if r.measured is None else (round(r.measured, 6) if isinstance(r.measured, float) else r.measured),
         "unit": r.unit, "status": r.status}
    if r.reason:
        d["reason"] = r.reason
    if r.at is not None:
        d["at"] = r.at
    return d


def env(shape):
    return {k: round(v.measured, 4) for k, v in envelope(shape).items()}


def box(x0, x1, y0, y1, z0, z1):
    return Box(x1 - x0, y1 - y0, z1 - z0).moved(Location(((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)))


def down_planes(shape, tol=1e-3):
    """Planar faces with normal -Y at the shape's lowest y: y and total area."""
    ymin = envelope(shape)["min_y"].measured
    fs = [f for f in shape.faces() if f.geom_type.name == "PLANE" and f.normal_at().Y < -0.9999
          and abs(f.center().Y - ymin) < tol]
    return {"y": round(ymin, 4), "faces": len(fs), "area_mm2": round(sum(f.area for f in fs), 3),
            "normal": [round(c, 6) for c in fs[0].normal_at().to_tuple()] if fs else None}


def feet_holes(shape, expected, y_mid):
    bc = bore_census(shape)
    rows = {}
    for (x, z) in expected:
        L = locate_bore(bc, (x, y_mid, z), (0, 1, 0))
        rows[f"({x},{z})"] = {k: res(v) for k, v in L.items()} | {"start": L["diameter"].at}
    return rows


# ---- joints of spec section 4 ----
# OD-C03: local x -> +Z, local y -> -Y, local z -> +X, origin (0, 40, -205)
C03_PLANE = Plane(origin=(0, 40, -205), x_dir=(0, 0, 1), z_dir=(1, 0, 0))
L03 = Location(C03_PLANE)
R = np.array([[C03_PLANE.x_dir.X, C03_PLANE.y_dir.X, C03_PLANE.z_dir.X],
              [C03_PLANE.x_dir.Y, C03_PLANE.y_dir.Y, C03_PLANE.z_dir.Y],
              [C03_PLANE.x_dir.Z, C03_PLANE.y_dir.Z, C03_PLANE.z_dir.Z]])
out["c03_rotation"] = {"columns_local_xyz_in_machine": R.T.round(9).tolist(),
                       "determinant": round(float(np.linalg.det(R)), 9),
                       "local_y_maps_to": [round(c, 9) for c in C03_PLANE.y_dir.to_tuple()]}
# point check of the mapping: local (34, 40, -4) -> expected machine (-4, 0, -171)
out["c03_point_check_local(34,40,-4)"] = [round(c, 6) for c in (L03 * Location((34, 40, -4))).position.to_tuple()]
L04 = Location((0, 70, -140))
L_G01 = Location((0, 175, 0))

c03_own = read_step(IN / "OD-C03_pump_cradle.step")
c04_own = read_step(IN / "OD-C04_thermoblock_mount.step")
h01_own = read_step(IN / "OD-H01_ulka_ep5_pump.step")
h11_own = read_step(IN / "OD-H11_thermoblock.step")
g01_own = read_step(IN / "OD-G01_housing_C1_v02.step")

for name, s in (("c03", c03_own), ("c04", c04_own), ("h01", h01_own), ("h11", h11_own), ("g01", g01_own)):
    out[f"{name}_validity"] = {k: res(v) for k, v in validity(s).items()}
    out[f"{name}_envelope_own_frame"] = env(s)

c03 = c03_own.moved(L03)
h01 = h01_own.moved(L03)
c04 = c04_own.moved(L04)
h11 = h11_own.moved(L04)
g01 = g01_own.moved(L_G01)
c05_box = box(-50, 50, 0, 4, -69.94, -24.94)
slab = box(-120, 120, -6, 0, -305, 100)

placed = {"od_c03": c03, "od_h01": h01, "od_c04": c04, "od_h11": h11, "od_g01": g01, "od_c05_foot_box": c05_box}
for n, s in placed.items():
    out[f"{n}_envelope_placed"] = env(s)

# 1, 2: foot underside planes and holes as placed
out["c03_foot_underside_placed"] = down_planes(c03)
out["c04_foot_underside_placed"] = down_planes(c04)
out["c03_holes_placed"] = feet_holes(c03, [(-4, -239), (-4, -171), (37, -239), (37, -171)], 1.5)
out["c04_holes_placed"] = feet_holes(c04, [(40, -148), (-40, -148), (40, -114), (-40, -114)], 2.0)

# 3, 4: OEM parts above the plate (pre-build estimate on the reference slab)
out["h01_min_y_placed"] = out["od_h01_envelope_placed"]["min_y"]
out["h11_min_y_placed"] = out["od_h11_envelope_placed"]["min_y"]
out["h11_max_z_placed"] = out["od_h11_envelope_placed"]["max_z"]
for n in ("od_c03", "od_c04", "od_h01", "od_h11", "od_g01"):
    c = clearance(placed[n], slab)
    out[f"estimate_{n}_to_slab_clearance"] = res(c) | {"on_slab": c.detail["on_b"]}
for n in ("od_c03", "od_c04"):
    out[f"estimate_{n}_slab_common_mm3"] = res(common_volume(placed[n], slab))

# 5, 6: every pair of placed solids
pairs = {}
for a, b in itertools.combinations(placed, 2):
    c = clearance(placed[a], placed[b])
    pairs[f"{a}|{b}"] = res(c) | {"on_b": c.detail["on_b"]}
out["pair_clearances"] = pairs

# reserved zones of spec section 4 (A-05 ... A-08), as prisms y 0 .. 400 above the plate
zones = {"tray_A06": (-75, 75, 10, 100), "tank_A07": (-70, 70, -305, -250),
         "valves_A05": (-120, -70, -160, -60), "electronics_A08": (70, 120, -240, -30)}
zrows = {}
for zn, (x0, x1, z0, z1) in zones.items():
    zb = box(x0, x1, 0, 400, z0, z1)
    zrows[zn] = {n: res(clearance(s, zb)) for n, s in placed.items()}
out["zone_clearances"] = zrows
# bulkhead line x = 65 over z -240 .. -30: each solid's max x inside that z band
bl = {}
for n, s in placed.items():
    band = s & box(-200, 200, -10, 400, -240, -30)
    sol = band.solids() if band else []
    bl[n] = round(max(v.X for so in sol for v in so.vertices()), 4) if sol else None
out["max_x_within_bulkhead_band_z-240..-30"] = bl
out["bulkhead_band_note"] = "vertex max x of the solid cut to z -240..-30; corroborated by the envelope max_x; OD-H11 cut may be unreliable (A-14)"

# 7: hole webs, derivation from the spec section 4 coordinates (exact for circles)
inserts = [(35, -40), (-35, -40), (35, -60), (-35, -60), (40, -148), (-40, -148), (40, -114), (-40, -114),
           (-4, -239), (-4, -171), (37, -239), (37, -171), (65, -45), (65, -105), (65, -165), (65, -225)]
holes = [(x, z, 2.0, "insert") for x, z in inserts] + \
        [(x, z, 1.7, "foot") for x in (110, -110) for z in (90, -295)] + \
        [(-80, -120, 4.0, "drain"), (-80, -230, 4.0, "drain")]
webs = []
for (x1, z1, r1, k1), (x2, z2, r2, k2) in itertools.combinations(holes, 2):
    webs.append((round(math.hypot(x1 - x2, z1 - z2) - r1 - r2, 4), f"{k1}({x1},{z1})", f"{k2}({x2},{z2})"))
webs.sort()
out["hole_to_hole_webs_nearest5"] = webs[:5]
out["hole_to_hole_nearest_insert_pair"] = [w for w in webs if w[1].startswith("insert") and w[2].startswith("insert")][0]


def edge_web(x, z, r, X=120.0, Z0=-305.0, Z1=100.0, R=10.0):
    cx = min(max(x, -X + R), X - R)
    cz = min(max(z, Z0 + R), Z1 - R)
    if abs(x) > X - R and (z > Z1 - R or z < Z0 + R) or (abs(x) == X - R and z in (Z1 - R, Z0 + R)):
        return R - math.hypot(x - cx, z - cz) - r
    return min(X - abs(x), z - Z0, Z1 - z) - r


ew = sorted((round(edge_web(x, z, r), 4), f"{k}({x},{z})") for x, z, r, k in holes)
out["hole_to_edge_webs_nearest5"] = ew[:5]
out["hole_to_edge_nearest_insert"] = [w for w in ew if w[1].startswith("insert")][0]
out["hole_web_note"] = "derivation from spec coordinates and diameters (insert r 2.0, foot r 1.7, drain r 4.0); plate outline x +-120, z -305..+100, corners R 10 centred (+-110, 90) and (+-110, -295)"

# a radial_extent reading on a probe coupon, to fix how J-05 / D-05a will be read at J3
from tools.measure import radial_extent
from build123d import Cylinder, Rot
coupon = box(-20, 20, -6, 0, -20, 20) - Cylinder(2.0, 10).moved(Location((0, -3, 0), (90, 0, 0))) \
    - Cylinder(1.7, 10).moved(Location((12, -3, 0), (90, 0, 0)))
rx = radial_extent(coupon, (0, -3, 0), (0, 1, 0), (1, 0, 0), 0.0, 0.0, side="inner")
out["coupon_radial_extent_toward_second_hole"] = res(rx) | {"material": rx.detail.get("material")}
out["coupon_note"] = "coupon 40 x 6 x 40 with a dia 4.0 hole at the origin and a dia 3.4 hole 12 away along the ray; expected first stretch 2.0 .. 10.3"

print(json.dumps(out, indent=1, default=str))
OUT.write_text(json.dumps(out, indent=1, default=str))
