"""D1 reference measurement for the DESIGN_PLAN (J2): measures the delivered solids
at their spec section 2 poses. Planning evidence only; no gate is decided here."""
import json
import sys
from pathlib import Path

from build123d import Box, Cylinder, Location, Plane, Vector, Axis, GeomType
from tools.core import read_step, validity
from tools.core.boolean import common_volume
from tools.measure import bore_census, envelope, feature_census, clearance

WS = Path(__file__).resolve().parents[1]
INP = WS / "00_Spec" / "inputs"


def load(name):
    s = read_step(INP / name)
    return s


def placed(shape, origin, xdir, zdir):
    return shape.moved(Location(Plane(origin=origin, x_dir=xdir, z_dir=zdir)))


def env(s):
    e = envelope(s)
    return {k: round(v.measured, 4) if v.measured is not None else None for k, v in e.items()}


def bores(s):
    c = bore_census(s)
    out = []
    for b in (c.detail or {}).get("bores", []):
        out.append({k: (([round(x, 3) for x in v] if isinstance(v, (list, tuple)) else (round(v, 3) if isinstance(v, float) else v)))
                    for k, v in b.items() if k in ("diameter", "axis_dir", "start", "end", "length", "through")})
    return c.measured, out


def planar_faces(s, normal, tol=1e-3):
    n = Vector(*normal)
    res = []
    for f in s.faces():
        if f.geom_type != GeomType.PLANE:
            continue
        fn = f.normal_at()
        if (fn - n).length < tol:
            bb = f.bounding_box()
            res.append([round(bb.min.X, 3), round(bb.max.X, 3), round(bb.min.Y, 3), round(bb.max.Y, 3),
                        round(bb.min.Z, 3), round(bb.max.Z, 3), round(f.area, 2)])
    return res


def cyl_faces(s):
    res = []
    for f in s.faces():
        if f.geom_type != GeomType.CYLINDER:
            continue
        ax = f.axis_of_rotation if hasattr(f, "axis_of_rotation") else None
        bb = f.bounding_box()
        res.append({"r": round(f.radius, 3),
                    "axis_pos": [round(c, 3) for c in ax.position] if ax else None,
                    "axis_dir": [round(c, 3) for c in ax.direction] if ax else None,
                    "bb": [round(bb.min.X, 2), round(bb.max.X, 2), round(bb.min.Y, 2), round(bb.max.Y, 2), round(bb.min.Z, 2), round(bb.max.Z, 2)]})
    return res


def box(x0, x1, y0, y1, z0, z1):
    return Box(x1 - x0, y1 - y0, z1 - z0).moved(Location(((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)))


def cv(a, b):
    r = common_volume(a, b)
    return round(r.measured, 4) if r.measured is not None else f"INCONCLUSIVE {r.reason}"


out = {}
X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
refs = {
    "C01": load("OD-C01_base_frame.step"),
    "C02": load("OD-C02_bulkhead.step"),
    "C05": placed(load("OD-C05_group_head_carrier.step"), (0, 180.06, 32.0), (1, 0, 0), (0, -1, 0)),
    "C07": placed(load("OD-C07_valve_flowmeter_mount.step"), (-92, 0, -60), (0, 0, -1), (0, 1, 0)),
    "C08": load("OD-C08_electronics_bay_tray.step"),
    "C10": load("OD-C10_top_panel.step"),
    "C11": load("OD-C11_back_panel.step"),
}
foot = load("OD-C15_foot.step")
for i, (fx, fz) in enumerate([(110, 90), (-110, 90), (110, -295), (-110, -295)]):
    refs[f"C15_{i}"] = placed(foot, (fx, -6, fz), (1, 0, 0), (0, -1, 0))

for k, s in refs.items():
    v = validity(s)
    out[k] = {"solids": len(s.solids()), "valid": {n: r.measured for n, r in v.items()}, "env": env(s)}

c01 = refs["C01"]
out["C01"]["bores"] = bores(c01)
out["C01"]["top_faces"] = planar_faces(c01, Y)
out["C01"]["side_faces_+x"] = planar_faces(c01, X)
out["C01"]["side_faces_-x"] = planar_faces(c01, (-1, 0, 0))
out["C01"]["vertical_cyls"] = [c for c in cyl_faces(c01) if c["axis_dir"] and abs(abs(c["axis_dir"][1]) - 1) < 1e-3 and c["r"] > 5]
out["C01"]["census"] = {k: r.measured for k, r in feature_census(c01).items()}
pts = [(sx * 104.5, zc) for sx in (1, -1) for zc in (-262.0, -15.0, 62.0)]
# plate solid in a D8 circle about each new insert position (y -6 .. 0)
out["C01"]["insert_disc_fill"] = {}
for x, z in pts:
    disc = Cylinder(4.0, 6.0).moved(Location((x, -3.0, z), (90, 0, 0)))
    out["C01"]["insert_disc_fill"][f"{x},{z}"] = [cv(disc, c01), round(disc.volume, 4)]

c10 = refs["C10"]
out["C10"]["bottom_faces_-y"] = [f for f in planar_faces(c10, (0, -1, 0)) if f[2] < 230]
out["C10"]["inner_skirt_faces_+x"] = [f for f in planar_faces(c10, X) if abs(f[0] + 117) < 0.5]
out["C10"]["inner_skirt_faces_-x"] = [f for f in planar_faces(c10, (-1, 0, 0)) if abs(f[0] - 117) < 0.5]
for sx in (1, -1):
    zone = box(*(sorted((sx * 113, sx * 117))), 200, 247, -285, 85)
    out["C10"][f"lip_zone_common_{sx}"] = cv(zone, c10)
    zone2 = box(*(sorted((sx * 114, sx * 117))), 215, 247, -299, 94)
    out["C10"][f"lipzone_full_length_{sx}"] = cv(zone2, c10)
c11 = refs["C11"]
out["C11"]["faces_+x"] = planar_faces(c11, X)
out["C11"]["faces_-x"] = planar_faces(c11, (-1, 0, 0))
out["C07"]["faces_-x"] = planar_faces(refs["C07"], (-1, 0, 0))

# Proxy screen (planning only): the spec's panel wall/rail/lip and bracket boxes against each reference
proxies = {}
for sx in (1, -1):
    xs = lambda a, b: sorted((sx * a, sx * b))
    proxies[f"wall{sx}"] = box(*xs(117, 120), 0, 215, -295, 90)
    proxies[f"rail{sx}"] = box(*xs(114, 117), 205, 215, -280, 80)
    proxies[f"lip{sx}"] = box(*xs(114, 116.6), 215, 225, -280, 80)
    for zc in (-262.0, -15.0, 62.0):
        proxies[f"br{sx}_{zc}"] = box(*xs(98, 117), 0, 16, zc - 8, zc + 8)
screen = {}
for pk, p in proxies.items():
    for rk, r in refs.items():
        c = clearance(p, r)
        if c.measured is not None and c.measured < 1.0:
            screen[f"{pk}|{rk}"] = round(c.measured, 4)
        elif c.measured is None:
            screen[f"{pk}|{rk}"] = f"INCONCLUSIVE {c.reason}"
out["proxy_screen_lt1mm"] = screen
json.dump(out, sys.stdout, indent=1, default=str)
