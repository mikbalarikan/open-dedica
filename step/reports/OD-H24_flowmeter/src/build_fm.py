"""OD-H24 flowmeter - feature-based (SolidWorks-style) rebuild from scan.

Datum frame (see T.npy, scan -> datum 4x4):
  Z = axis of the cup cylinder (least-squares from side-wall normals + circle fits),
  Z = 0 on the bottom rim face, X/Y locked so the lower (inlet) tube runs along -Y.
All values in mm, measured from the scan; every value is logged in params.json.
Every feature is a named sketch + extrude / revolve / cut - no traced slices.

IN : nothing (all parameters in P)
OUT: build() -> one valid closed build123d Solid (datum frame)
"""

import json
import math
import sys
from pathlib import Path

import numpy as np
from build123d import (
    Align,
    Axis,
    Box,
    Cylinder,
    Face,
    Location,
    Plane,
    Pos,
    Rot,
    Solid,
    Vector,
    Wire,
    export_step,
    export_stl,
)

P = dict(
    # ---- 1. body revolve (cup + flange skirt + central boss), (r, z) ----
    z_rim=0.0,              # bottom rim face (datum Z=0)
    z_panel=2.0,            # recessed bottom panel (measured 2.008)
    r_rim_in=13.98,         # rim inner wall (measured 13.977)
    r_cup0=15.71,           # cup outer radius at z=0
    cup_draft=0.0195,       # dr/dz of cup wall (15.77@z3 -> 15.94@z12, ~1.1 deg)
    z_groove_top=14.7,      # top of the annular gap between cup and flange skirt (partly seen; weld flash inside)
    r_skirt_in=17.1,        # flange skirt inner wall
    z_flange_under=12.67,   # flange underside (measured 12.674)
    r_flange0=20.25,        # flange outer r at underside (measured 20.253 @ z13.5)
    r_flange1=20.37,        # flange outer r at top (measured 20.370 @ z19)
    z_flange_top=19.90,     # flange top face (measured 19.900 @ axis)
    r_boss=7.95,            # central round boss (circle fit 7.9..7.98)
    z_boss_top=21.87,       # boss top (measured 21.869)
    f_rim_out=0.3, f_rim_in=0.3, f_panel=0.5, f_flange_top=0.6, f_flange_under=0.4,
    # ---- 2. bottom: hub, 4 spokes, 2 pins ----
    hub_c=(0.15, -0.05), r_hub=3.59, z_rib=0.1,       # hub + spokes bottom (measured 0.08 / 0.11)
    spoke_w=1.2,                                      # walls measured at -0.40/+0.72 (Y spokes)
    pin1=dict(c=(0.185, 0.093), d=3.8, z0=-7.03, ch=0.4),   # centre (rotor axle) pin, r 1.895
    pin2=dict(c=(-11.78, 0.14), d=2.8, z0=-5.46, ch=0.3),   # second pin, r 1.385
    # ---- 3. flange pockets ----
    win_r=(7.95, 12.45), win_floor=15.0,                     # 4 arc windows, floor measured 14.92..15.19
    win_ang=((69.4, 121.6), (129.3, 182.0), (189.4, 236.5), (266.0, 302.2)),
    slot_r=17.83, slot_L=8.6, slot_W=2.15, slot_cr=0.5, slot_floor=17.25,  # 4 outer slots: walls u 16.75/18.9, ends w +-4.3
    slot_ang0=26.5, slot_n=4,                                            # 26.4/115.4/206.4/296.5 measured
    # ---- 4. connector boss (local frame rotated conn_ang about Z) ----
    conn_ang=5.2,            # side edges measured 5.66 / 4.76 deg
    conn_arc_c=6.1, conn_R=6.5,    # left semicircle centre x', radius (half width 6.5: y' +6.55/-6.47)
    conn_end_R=17.0,         # right end = arc R17 about the body axis
    z_conn_top=24.04,        # measured 24.043
    pin_x=10.68, pin_pitch=3.96, pin_a=1.2, pin_top=36.5, pin_ch=0.4,
    frustum_x=10.75, frustum_bot=(3.3, 3.1), frustum_taper=10.5, z_frustum_top=27.0,  # top measured ~2.3 x 1.9 -> equal 0.55/side draft
    plate_x=(13.8, 15.35), plate_w=3.0, z_plate_top=32.4,   # back plate: -x' face 13.8, +x' face 15.3, top 32.25..32.5
    hook_x0=12.5, z_hook0=29.8,                            # plate top hooks forward over the pin: front face x' 12.5, underside z 29.8
    # ---- 5. tubes: axis point p0 (s=0), direction d, revolve profile (s, r) ----
    tube_low=dict(p0=(-10.613, 0.0, 7.527), d=(0.0096, -0.9998, -0.0156),
                  prof=((6.0, 2.98), (19.9, 2.98), (20.6, 3.43), (21.3, 3.43), (22.4, 2.98), (30.5, 2.98),
                        (31.3, 3.16), (31.9, 3.16), (32.8, 2.98), (35.5, 2.98), (35.9, 2.6)),
                  bore_d=3.5, bore_depth=3.0),
    tube_up=dict(p0=(-4.43, -0.442, 20.254), d=(0.0993, -0.9949, -0.0188),
                 prof=((0.0, 2.89), (19.5, 2.89), (19.6, 3.40), (21.3, 3.40), (22.2, 2.89), (30.5, 2.89),
                       (31.3, 3.10), (31.9, 3.10), (32.8, 2.89), (35.8, 2.89), (36.2, 2.5)),
                 bore_d=4.0, bore_depth=3.0),
)


# ---------------------------------------------------------------- helpers
def revolve_rz(prof):
    """Revolve a closed (r, z) polygon 360 deg about the datum Z axis."""
    w = Wire.make_polygon([Vector(r, 0, z) for r, z in prof], close=True)
    return Solid.revolve(Face(w), 360, Axis.Z)


def prism(pts, z0, z1):
    f = Face(Wire.make_polygon([Vector(x, y, z0) for x, y in pts], close=True))
    return Solid.extrude(f, Vector(0, 0, z1 - z0))


def cyl(c, r, z0, z1):
    return Pos(c[0], c[1], z0) * Cylinder(r, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN))


def fillet_circles(s, specs, tol=0.05):
    """Fillet the circular edges of a revolved solid given as (r, z, R)."""
    for r, z, R in specs:
        es = [e for e in s.edges() if e.geom_type.name == "CIRCLE" and abs(e.radius - r) < tol
              and abs(e.center().Z - z) < tol]
        if not es:
            raise RuntimeError(f"no circular edge at r={r} z={z}")
        s = s.fillet(R, es)
    return s


def rot(ang_deg):
    a = math.radians(ang_deg)
    return lambda x, y: (x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a))


def sector(r0, r1, a0, a1, z0, z1):
    """Annular sector r0..r1, a0..a1 deg: (tube) & (radial wedge) - true arcs + radial planes."""
    ring = cyl((0, 0), r1, z0, z1) - cyl((0, 0), r0, z0 - 1, z1 + 1)
    far = 2.5 * r1
    am = 0.5 * (a0 + a1)
    wedge = prism([(0, 0)] + [(far * math.cos(math.radians(a)), far * math.sin(math.radians(a))) for a in (a0, am, a1)], z0 - 1, z1 + 1)
    return ring & wedge


# ---------------------------------------------------------------- features
def body():
    """F1 revolve: bottom panel + rim, drafted cup wall, gap under flange, flange skirt, central boss."""
    p = P
    r_top = p["r_cup0"] + p["cup_draft"] * p["z_groove_top"]
    prof = [(0.0, p["z_panel"]), (p["r_rim_in"], p["z_panel"]), (p["r_rim_in"], p["z_rim"]),
            (p["r_cup0"], p["z_rim"]), (r_top, p["z_groove_top"]), (p["r_skirt_in"], p["z_groove_top"]),
            (p["r_skirt_in"], p["z_flange_under"]), (p["r_flange0"], p["z_flange_under"]),
            (p["r_flange1"], p["z_flange_top"]), (p["r_boss"], p["z_flange_top"]),
            (p["r_boss"], p["z_boss_top"]), (0.0, p["z_boss_top"])]
    s = revolve_rz(prof)
    return fillet_circles(s, [(p["r_cup0"], p["z_rim"], p["f_rim_out"]),
                              (p["r_rim_in"], p["z_rim"], p["f_rim_in"]),
                              (p["r_rim_in"], p["z_panel"], p["f_panel"]),
                              (p["r_flange1"], p["z_flange_top"], p["f_flange_top"]),
                              (p["r_flange0"], p["z_flange_under"], p["f_flange_under"])])


def bottom_ribs():
    """F2 extrudes: hub disc + 4 spokes (+X/-X/+Y/-Y) standing on the panel, and the two pins."""
    p = P
    cx, cy = p["hub_c"]
    z0, z1 = p["z_rib"], p["z_panel"] + 0.2
    L = 2 * p["r_rim_in"] + 1.0
    w = p["spoke_w"]
    ribs = cyl(p["hub_c"], p["r_hub"], z0, z1)
    ribs += Pos(cx, cy, z0) * Box(L, w, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    ribs += Pos(cx, cy, z0) * Box(w, L, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    ribs = ribs & cyl((0, 0), p["r_rim_in"] + 0.2, z0 - 1, z1 + 1)
    for key in ("pin1", "pin2"):
        q = p[key]
        r = q["d"] / 2
        pin = Solid.make_cone(r - q["ch"], r, q["ch"], Plane.XY.move(Location((q["c"][0], q["c"][1], q["z0"]))))
        pin += cyl(q["c"], r, q["z0"] + q["ch"], p["z_panel"] + 0.2)
        ribs += pin
    return ribs


def flange_pockets():
    """F3 cuts: 4 arc windows beside the boss (floor z 15.0) and 4 tangential outer slots (90 deg pattern)."""
    p = P
    cut = None
    for a0, a1 in p["win_ang"]:
        s = sector(p["win_r"][0], p["win_r"][1], a0, a1, p["win_floor"], p["z_flange_top"] + 1)
        cut = s if cut is None else cut + s
    for k in range(p["slot_n"]):
        th = p["slot_ang0"] + 360.0 * k / p["slot_n"]
        b = Box(p["slot_L"], p["slot_W"], 3.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
        b = b.fillet(p["slot_cr"], b.edges().filter_by(Axis.Z))
        c = (p["slot_r"] * math.cos(math.radians(th)), p["slot_r"] * math.sin(math.radians(th)))
        cut += Location((c[0], c[1], p["slot_floor"]), (0, 0, th + 90)) * b
    return cut


def connector():
    """F4: connector boss (semicircle + parallel sides + R17 end arc, rotated 5.2 deg), 3 pin bases
    (drafted pyramid-frustum extrudes), 3 square pins, 3 hooked back plates."""
    p = P
    R = rot(p["conn_ang"])
    zb, zt = p["z_flange_top"] - 0.01, p["z_conn_top"]
    hw = p["conn_R"]
    rect = prism([R(p["conn_arc_c"], -hw), R(p["conn_end_R"] + 2, -hw), R(p["conn_end_R"] + 2, hw), R(p["conn_arc_c"], hw)], zb, zt)
    rect = rect & cyl((0, 0), p["conn_end_R"], zb - 1, zt + 1)
    c = R(p["conn_arc_c"], 0.0)
    boss = rect + cyl(c, hw, zb, zt)
    loc = Location((0, 0, 0), (0, 0, p["conn_ang"]))
    for j in (-1, 0, 1):
        yp = j * p["pin_pitch"]
        bw, bd = p["frustum_bot"]
        fx = p["frustum_x"]
        h = p["z_frustum_top"] - zt + 0.01
        f0 = Face(Wire.make_polygon([Vector(fx + a * bw / 2, yp + b * bd / 2, zt - 0.01) for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))], close=True))
        base = Solid.extrude_taper(f0, Vector(0, 0, h), p["frustum_taper"])  # draft on all 4 sides (planar faces)
        a = p["pin_a"]
        pin = Pos(p["pin_x"], yp, zt) * Box(a, a, p["pin_top"] - zt, align=(Align.CENTER, Align.CENTER, Align.MIN))
        pin = pin.chamfer(p["pin_ch"], None, pin.edges().group_by(Axis.Z)[-1])
        x0, x1 = p["plate_x"]
        plate = Pos((x0 + x1) / 2, yp, zt - 0.01) * Box(x1 - x0, p["plate_w"], p["z_plate_top"] - zt, align=(Align.CENTER, Align.CENTER, Align.MIN))
        hook = Pos((p["hook_x0"] + x0) / 2, yp, p["z_hook0"]) * Box(x0 - p["hook_x0"] + 0.01, p["plate_w"], p["z_plate_top"] - p["z_hook0"], align=(Align.CENTER, Align.CENTER, Align.MIN))
        boss += loc * (base + pin + plate + hook)
    return boss


def tube(spec):
    """F5 revolve about a measured tube axis: barb collar + bead, end chamfer; returns (solid, bore cut)."""
    a = np.array(spec["p0"], float)
    d = np.array(spec["d"], float)
    d /= np.linalg.norm(d)
    xd = np.cross(d, [0, 0, 1.0])
    xd /= np.linalg.norm(xd)
    pl = Plane(origin=Vector(*a), x_dir=Vector(*d), z_dir=Vector(*xd))
    prof = spec["prof"]
    pts = [(prof[0][0], 0.0)] + list(prof) + [(prof[-1][0], 0.0)]
    w = Wire.make_polygon([pl.from_local_coords((s, r)) for s, r in pts], close=True)
    body = Solid.revolve(Face(w), 360, Axis(Vector(*a), Vector(*d)))
    s_end = prof[-1][0]
    bo = a + d * (s_end - spec["bore_depth"])
    bore = Solid.make_cylinder(spec["bore_d"] / 2, spec["bore_depth"] + 1.0, Plane(origin=Vector(*bo), z_dir=Vector(*d)))
    return body, bore


def build():
    part = body()
    part += bottom_ribs()
    part += connector()
    part -= flange_pockets()
    bores = []
    for key in ("tube_low", "tube_up"):
        t, b = tube(P[key])
        part += t
        bores.append(b)
    for b in bores:
        part -= b
    return part.clean()


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "out")
    out.mkdir(parents=True, exist_ok=True)
    part = build()
    sol = part.solids()
    from collections import Counter
    print("solids", len(sol), "valid", part.is_valid, "volume %.1f" % part.volume, "faces", len(part.faces()),
          dict(Counter(f.geom_type.name for f in part.faces())))
    if len(sol) != 1:
        print("solid volumes", sorted((round(s.volume, 2) for s in sol), reverse=True)[:6])
    export_step(part, str(out / "flowmeter_datum.step"))
    export_stl(part, str(out / "flowmeter_datum.stl"), tolerance=0.01, angular_tolerance=0.1)
    json.dump(P, open(out / "params.json", "w"), indent=1)
