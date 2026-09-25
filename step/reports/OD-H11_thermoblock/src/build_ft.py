"""OD-H11 thermoblock - feature-based (SolidWorks-style) rebuild from scan.

Datum frame: base face Z=0, body axis +Z through A, top face Z=47.64. All values
in mm, measured from the scan (see REPORT / params). Every feature is a named
sketch + extrude / revolve / loft / cut; no traced slices.
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
    Spline,
    Vector,
    Wire,
    export_step,
    export_stl,
)

HERE = Path(__file__).resolve().parent
A = (-8.33, -14.13)  # body / bore / counterbore axis (common: fitted centres agree within 0.1)
H = 47.64  # top face

P = dict(
    # body: revolved, drafted below z=20
    # two die halves drafted opposite ways: main sector r grows with z, sector B (theta 69..172) shrinks
    coneA=(33.78, 34.95), coneB=(34.97, 33.85), sectorB=(69.0, 172.0), body_chamfer_bottom=0.5, body_chamfer_top=0.4,
    bore_bottom_chamfer=1.3,
    # bore (3 keyway lobes, lofted bottom->top), web, counterbore
    z_web0=34.5, z_web1=37.8, d_web_hole=6.0, web_hole_chamfer=0.6,
    r_cb_floor=14.13, r_cb_top=14.99, cb_top_chamfer=1.3,
    # grooves (vertical flutes): radius, pitch radius, angle, z range
    groove_r=4.25, groove_pitch=36.75,
    grooves=((9.8, 0.0, 35.3), (49.8, 0.0, 35.3), (189.4, 0.0, 42.4)),
    # top pins: cone on PCD
    pin_pcd_r=25.0, pin_angles=(9.1, 129.1, 249.1), pin_d0=3.9, pin_d1=3.35, pin_top=50.79,
    # rib pads: shared revolved step profile (r, z) intersected with a column prism
    pad_profile=((30.0, 0.0), (39.4, 0.0), (39.4, 5.9), (36.25, 9.05), (36.25, 13.3), (35.05, 14.5),
                 (35.05, 16.4), (36.25, 17.6), (36.25, 18.7), (35.05, 19.3), (35.05, 28.5), (36.25, 29.3),
                 (36.25, 30.3), (35.05, 31.3), (35.05, 33.5), (36.25, 34.7), (36.25, 40.1), (39.4, 42.5),
                 (39.4, H), (30.0, H)),
    padA=dict(theta=262.5, left=((-8.1, 33.4), (-3.3, 39.0)), right=((3.82, 33.0), (3.82, 39.0)),
              notch_v=(-3.65, 1.55), notch_u=33.0, hole_u=(33.0, 37.4)),
    padB=dict(theta=339.0, left=((-5.85, 33.0), (-5.85, 39.0)),
              right_block=((6.68, 34.89), (1.57, 38.58)), right_rib=((6.96, 34.36), (5.0, 35.6)),
              notch_v=(-4.45, 0.5), notch_u=32.45, hole_u=(33.0, 37.4)),
    pad_notch_z=((0.0, 3.5), (44.3, H)), pad_hole_z=((3.5, 6.2), (41.4, 44.3)),
    flatB=dict(theta=339.0, poly=((6.0, 30.0), (6.0, 34.6), (12.2, 34.6), (12.95, 33.9), (14.24, 31.97), (14.3, 30.0)), z=(0.5, H)),
    # side block (local frame at theta 107.5)
    side_theta=107.5,
    # lower block: outer face drafted u 40.95 (z 11.8) -> 39.95 (z 27.6); lofted
    side_block=dict(z=(11.8, 27.6), u_top=(40.95, 39.95), poly=((-10.15, 30.0), (-10.15, -1.45), (-8.7, 0.0), (8.15, 0.0),
                                          (9.5, -1.35), (9.87, -2.75), (9.87, 30.0))),
    side_tab=dict(z=((32.9, 38.6), (43.9, 47.2)), poly=((-10.0, 30.0), (-9.8, 37.0), (-9.5, 38.2), (-8.3, 39.4),
                                                      (-5.8, 39.54), (7.6, 39.54), (8.7, 38.56), (9.05, 37.84),
                                                      (9.45, 30.0))),
    side_tab_slots=dict(z=(32.9, 38.6), v=((-7.98, -4.6), (4.0, 7.4)), u0=37.4),
    side_gaps=(dict(z=(27.6, 32.9), v=(-9.45, 9.4), u0=33.4), dict(z=(38.6, 43.9), v=(-9.3, 9.1), u0=33.15)),
    # lugs: XY sketches closed through the body interior (via A)
    top_lug=dict(z=(36.3, H), poly=((9.29, 15.94), (10.6, 15.8), (11.75, 18.05), (12.8, 18.3), (36.9, 9.05),
                                    (37.4, 8.45), (37.1, 7.0), (26.7, -19.9), (26.7, -21.0))),
    mid_lug=dict(z=(27.6, 36.3), poly=((18.4, 8.33), (19.16, 8.78), (18.9, 10.8), (19.45, 12.7), (20.4, 13.65),
                                       (21.9, 14.3), (23.3, 14.15), (29.7, 11.5), (31.1, 7.6), (30.9, 7.1),
                                       (25.9, 5.2), (23.5, 4.85), (22.0, 4.1), (21.6, 3.6))),
    pipe_lug=dict(z=(0.0, 9.5), poly=((-38.8, 3.41), (-37.28, 7.78), (-39.91, 14.44), (-40.25, 16.15),
                                      (-39.98, 17.57), (-29.35, 32.08), (-27.1, 34.78), (-25.51, 34.42),
                                      (-15.64, 30.34), (-14.96, 29.93), (-13.7, 28.55), (-12.92, 28.15),
                                      (-1.02, 23.68), (-0.59, 23.38), (-0.37, 22.85), (-0.92, 20.84),
                                      (-0.71, 20.17), (-0.08, 19.8), (3.09, 18.97))),
    pipe_lug_step=dict(z=(9.5, 11.8), poly=((-31.94, 11.47), (-28.56, 14.38), (-28.2, 15.05), (-31.52, 28.42),
                                            (-28.51, 33.04), (-26.92, 34.75), (-23.2, 33.5), (-15.73, 30.28),
                                            (-14.94, 29.84), (-14.26, 28.85), (-12.82, 28.06), (-1.14, 23.65),
                                            (-0.39, 22.85), (-1.02, 20.79), (-0.77, 20.09), (3.56, 18.62))),
    lug_notch=dict(z=(0.0, 3.2), poly=((-17.5, 33.0), (-18.6, 30.3), (-19.7, 27.6), (-23.3, 23.1), (-24.1, 21.6),
                                       (-24.2, 19.5), (-23.25, 17.3), (-19.2, 18.95), (-15.0, 20.05), (-14.6, 25.9),
                                       (-13.9, 27.8), (-12.5, 29.5))),
    # pockets (slots 11.9 x 3.6 full-round; recesses)
    slot_L=11.9, slot_W=3.6,
    top_slots=(((-28.2, -30.46), 39.7, 40.8), ((-12.36, 11.53), 101.9, 41.0), ((2.22, -37.96), 113.5, 41.6)),
    bottom_slots=(((1.19, 10.5), 69.3, 8.4), ((8.0, -34.32), 129.9, 9.2)),
    bottom_rect=dict(c=(-33.73, -18.16), L=4.76, W=3.62, ang=9.8, r=0.8, z1=7.2),
    bottom_recess_depth=0.6,
    bottom_recesses=(((-28.54, 0.51), 5.7), ((-27.2, -30.05), 5.9), ((-23.55, 10.09), 7.9), ((-17.34, -37.6), 11.4)),
    top_recess_depth=0.45,
    top_recess_circle=((-31.68, -5.3), 11.8),
    top_label=dict(c=(15.43, -23.92), L=20.4, W=6.4, ang=69.1, r=1.0),
    spotface_d=11.4,  # every slot sits in a shallow round spot-face (top 0.45, bottom 0.6 deep)
    blind_holes=(dict(c=(25.01, 9.08), d=3.5, z=(27.0, 33.2)),     # mid lug, from underside
                 dict(c=(-19.62, 20.18), d=3.6, z=(3.0, 8.0))),    # pipe lug, from the bottom notch
    lug_top_pocket=dict(c=(-35.76, 15.55), L=3.66, W=2.86, ang=43.0, z=(5.8, 10.0)),
)


# ---------------------------------------------------------------- helpers
def UV(theta):
    t = math.radians(theta)
    return np.array([math.cos(t), math.sin(t)]), np.array([-math.sin(t), math.cos(t)])


def local_to_xy(theta, pts):
    U, V = UV(theta)
    a = np.array(A)
    return [tuple(a + u * U + v * V) for v, u in pts]


def face_xy(pts, z=0.0):
    return Face(Wire.make_polygon([Vector(x, y, z) for x, y in pts], close=True))


def prism(pts, z0, z1):
    return Solid.extrude(face_xy(pts, z0), Vector(0, 0, z1 - z0))


def line_at_u(p, q, u):
    (v0, u0), (v1, u1) = p, q
    return (v0 + (v1 - v0) * (u - u0) / (u1 - u0), u)


def column(theta, left, right, u0=28.0, u1=47.0):
    """Column prism between two side lines given in local (v,u); full height."""
    loc = [line_at_u(*left, u0), line_at_u(*left, u1), line_at_u(*right, u1), line_at_u(*right, u0)]
    return prism(local_to_xy(theta, loc), -1.0, H + 1.0)


def revolve_rz(prof):
    ax, ay = A
    w = Wire.make_polygon([Vector(ax + r, ay, z) for r, z in prof], close=True)
    return Solid.revolve(Face(w), 360, Axis((ax, ay, 0), (0, 0, 1)))


def slot(c, L, W, ang, z0, z1):
    """Full-round slot (overall length L, width W) as a solid."""
    s = Box(L - W, W, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    s += Pos(-(L - W) / 2, 0, 0) * Cylinder(W / 2, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    s += Pos((L - W) / 2, 0, 0) * Cylinder(W / 2, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return Location((c[0], c[1], z0), (0, 0, ang)) * s


def rrect(c, L, W, ang, r, z0, z1):
    b = Box(L, W, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    b = b.fillet(r, b.edges().filter_by(Axis.Z))
    return Location((c[0], c[1], z0), (0, 0, ang)) * b


def lug(spec):
    return prism(list(spec["poly"]) + [A], *spec["z"])


# ---------------------------------------------------------------- features
def body():
    p = P
    cb, ct = p["body_chamfer_bottom"], p["body_chamfer_top"]
    def cone(r0, r1):
        k = (r1 - r0) / H
        return revolve_rz([(0.0, 0.0), (r0 - cb, 0.0), (r0 + k * cb, cb), (r1 - k * ct, H - ct), (r1 - ct, H), (0.0, H)])
    t0, t1 = p["sectorB"]
    wedge = prism([A] + [tuple(np.array(A) + 60 * UV(t)[0]) for t in np.linspace(t0, t1, 24)], -1.0, H + 1.0)
    a, b = cone(*p["coneA"]), cone(*p["coneB"])
    return (a - wedge) + (b & wedge)


def pads():
    p = P
    rev = revolve_rz(p["pad_profile"])
    rib_cap = revolve_rz([(r if r <= 36.25 else 36.25, z) for r, z in p["pad_profile"]])
    a = p["padA"]
    out = rev & column(a["theta"], a["left"], a["right"])
    b = p["padB"]
    out += rev & column(b["theta"], b["left"], b["right_block"])
    out += rib_cap & column(b["theta"], b["left"], b["right_rib"])
    f = p["flatB"]
    out += prism(local_to_xy(f["theta"], f["poly"]), *f["z"])
    return out


def pad_cuts():
    p = P
    cut = None
    for key in ("padA", "padB"):
        d = p[key]
        v0, v1 = d["notch_v"]
        for z0, z1 in p["pad_notch_z"]:
            s = prism(local_to_xy(d["theta"], [(v0, d["notch_u"]), (v0, 45), (v1, 45), (v1, d["notch_u"])]), z0 - (0.5 if z0 == 0 else 0), z1 + (0.5 if z1 == H else 0))
            cut = s if cut is None else cut + s
        u0, u1 = d["hole_u"]
        for z0, z1 in p["pad_hole_z"]:
            cut += prism(local_to_xy(d["theta"], [(v0, u0), (v0, u1), (v1, u1), (v1, u0)]), z0 - 0.05, z1 + 0.05)
    return cut


def side_block():
    p = P
    th = p["side_theta"]
    sb = p["side_block"]
    faces = []
    for z, ut in zip(sb["z"], sb["u_top"]):
        loc = [(v, u if u >= 20 else ut + u) for v, u in sb["poly"]]
        faces.append(face_xy(local_to_xy(th, loc), z).outer_wire())
    out = Solid.make_loft(faces, ruled=True)
    for z0, z1 in p["side_tab"]["z"]:
        out += prism(local_to_xy(th, p["side_tab"]["poly"]), z0, z1)
    return out


def side_cuts():
    p = P
    th = p["side_theta"]
    cut = None
    for g in p["side_gaps"]:
        v0, v1 = g["v"]
        s = prism(local_to_xy(th, [(v0, g["u0"]), (v0, 46), (v1, 46), (v1, g["u0"])]), *g["z"])
        cut = s if cut is None else cut + s
    st = p["side_tab_slots"]
    for v0, v1 in st["v"]:
        cut += prism(local_to_xy(th, [(v0, st["u0"]), (v0, 46), (v1, 46), (v1, st["u0"])]), st["z"][0] - 0.05, st["z"][1] + 0.05)
    return cut


def lugs():
    p = P
    out = lug(p["top_lug"]) + lug(p["mid_lug"]) + lug(p["pipe_lug"]) + lug(p["pipe_lug_step"])
    return out


def bore_cut():
    """3-lobe cored bore: lofted between the measured bottom and top profiles (3-fold symmetric)."""
    prof = json.load(open(HERE / "bore_prof.json"))
    secs = []
    for key, z in (("1.2", -0.3), ("33.7", P["z_web0"])):
        r = np.array(prof[key]["prof"])  # 120 x 1 deg, one lobe period
        z0, z1 = 1.2, 33.7
        # linear extrapolation of the draft to the loft end planes
        r_other = np.array(prof["33.7" if key == "1.2" else "1.2"]["prof"])
        zk = 1.2 if key == "1.2" else 33.7
        zo = 33.7 if key == "1.2" else 1.2
        rz = r + (r - r_other) * (z - zk) / (zk - zo)
        rr = np.r_[rz, rz, rz][::3]  # 3-deg spline stations, 120 points round
        ang = np.radians(np.arange(0, 360, 3) + 0.5)
        pts = [Vector(A[0] + q * math.cos(a), A[1] + q * math.sin(a), z) for q, a in zip(rr, ang)]
        secs.append(Wire([Spline(*pts, periodic=True)]))
    loft = Solid.make_loft(secs, ruled=True)
    rb = float(np.min(json.load(open(HERE / "bore_prof.json"))["1.2"]["prof"]))
    ch = P["bore_bottom_chamfer"]
    return loft + revolve_rz([(0, -0.5), (rb + ch + 0.5, -0.5), (rb - 0.05, ch), (0, ch)])


def web_and_counterbore_cut():
    p = P
    ax, ay = A
    web = revolve_rz([(0, p["z_web0"] - 0.2), (p["d_web_hole"] / 2, p["z_web0"] - 0.2), (p["d_web_hole"] / 2, p["z_web1"] - p["web_hole_chamfer"]),
                      (p["d_web_hole"] / 2 + p["web_hole_chamfer"], p["z_web1"]), (0, p["z_web1"])])
    cb = revolve_rz([(0, p["z_web1"]), (p["r_cb_floor"], p["z_web1"]), (p["r_cb_top"] - 0.05, H - p["cb_top_chamfer"]),
                     (p["r_cb_top"] + p["cb_top_chamfer"], H + 0.01), (p["r_cb_top"] + p["cb_top_chamfer"], H + 1), (0, H + 1)])
    return web + cb


def grooves_cut():
    p = P
    out = None
    for ang, z0, z1 in p["grooves"]:
        U, _ = UV(ang)
        c = np.array(A) + p["groove_pitch"] * U
        s = Pos(c[0], c[1], z0 - 0.5) * Cylinder(p["groove_r"], z1 - z0 + 0.5, align=(Align.CENTER, Align.CENTER, Align.MIN))
        out = s if out is None else out + s
    return out


def lug_notch_cut():
    s = P["lug_notch"]
    return prism(s["poly"], s["z"][0] - 0.5, s["z"][1])


def pockets_cut():
    p = P
    cut = None
    for c, ang, z0 in p["top_slots"]:
        s = slot(c, p["slot_L"], p["slot_W"], ang, z0, H + 0.5)
        cut = s if cut is None else cut + s
    for c, ang, z1 in p["bottom_slots"]:
        cut += slot(c, p["slot_L"], p["slot_W"], ang, -0.5, z1)
    b = p["bottom_rect"]
    cut += rrect(b["c"], b["L"], b["W"], b["ang"], b["r"], -0.5, b["z1"])
    for c, d in p["bottom_recesses"]:
        cut += Pos(c[0], c[1], -0.5) * Cylinder(d / 2, p["bottom_recess_depth"] + 0.5, align=(Align.CENTER, Align.CENTER, Align.MIN))
    c, d = p["top_recess_circle"]
    cut += Pos(c[0], c[1], H - p["top_recess_depth"]) * Cylinder(d / 2, 1.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    for c, ang, z0 in p["top_slots"]:
        cut += Pos(c[0], c[1], H - p["top_recess_depth"]) * Cylinder(p["spotface_d"] / 2, 1.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
    for c in [q[0] for q in p["bottom_slots"]] + [p["bottom_rect"]["c"]]:
        cut += Pos(c[0], c[1], -0.5) * Cylinder(p["spotface_d"] / 2, p["bottom_recess_depth"] + 0.5, align=(Align.CENTER, Align.CENTER, Align.MIN))
    for h in p["blind_holes"]:
        cut += Pos(h["c"][0], h["c"][1], h["z"][0]) * Cylinder(h["d"] / 2, h["z"][1] - h["z"][0], align=(Align.CENTER, Align.CENTER, Align.MIN))
    lp = p["lug_top_pocket"]
    cut += slot(lp["c"], lp["L"], lp["W"], lp["ang"], *lp["z"])
    t = p["top_label"]
    cut += rrect(t["c"], t["L"], t["W"], t["ang"], t["r"], H - p["top_recess_depth"], H + 0.5)
    return cut


def pins():
    p = P
    out = None
    for ang in p["pin_angles"]:
        U, _ = UV(ang)
        c = np.array(A) + p["pin_pcd_r"] * U
        s = Solid.make_cone(p["pin_d0"] / 2, p["pin_d1"] / 2, p["pin_top"] - H + 0.2, Plane.XY.move(Location((c[0], c[1], H - 0.2))))
        out = s if out is None else out + s
    return out


def revolved(a, d, prof):
    """Revolve an (t, r) profile about the axis (point a, dir d)."""
    a = np.asarray(a, float)
    d = np.asarray(d, float)
    d /= np.linalg.norm(d)
    pl = Plane(origin=Vector(*a), x_dir=Vector(*d), z_dir=Vector(*np.cross(d, [0, 0, 1.0])))
    pts = [(prof[0][0], 0)] + list(prof) + [(prof[-1][0], 0)]
    w = Wire.make_polygon([pl.from_local_coords((t, r)) for t, r in pts], close=True)
    return Solid.revolve(Face(w), 360, Axis(Vector(*a), Vector(*d)))


def pipes_and_terminals():
    F = json.load(open(HERE / "ports.json"))
    out = None
    for pp in F["pipes"]:
        a, d = np.array(pp["a"]), np.array(pp["d"])
        s = revolved(a, d, pp["prof"])
        cf = pp["clip_flats"]
        w = np.cross(d, [0, 0, 1.0])
        w /= np.linalg.norm(w)
        for sg in (1, -1):
            ctr = a + d * (cf["t0"] + cf["t1"]) / 2 + w * sg * (cf["half_width"] + 2.5)
            pl = Plane(origin=Vector(*ctr), x_dir=Vector(*d), z_dir=Vector(0, 0, 1))
            s -= pl.location * Box(cf["t1"] - cf["t0"], 5.0, 12.0)
        t_end = pp["prof"][0][0]
        bore = Solid.make_cylinder(pp["bore_r"], pp["bore_depth"] + 0.5, Plane(origin=Vector(*(a + (t_end - 0.5) * d)), z_dir=Vector(*d)))
        s -= bore
        out = s if out is None else out + s
    for tt in F["terminals"]:
        s = revolved(tt["a"], tt["d"], tt["prof"])
        n, e1, e2, base = (np.array(tt["blade"][k]) for k in ("n", "e1", "e2", "base"))
        th = tt["blade"]["thick"]
        P3 = [Vector(*(base + q[0] * e1 + q[1] * e2 - n * th / 2)) for q in tt["blade"]["outline_uv"]]
        plate = Solid.extrude(Face(Wire.make_polygon(P3, close=True)), Vector(*(n * th)))
        hc = base + tt["blade"]["hole_uv"][0] * e1 + tt["blade"]["hole_uv"][1] * e2 - n * th
        plate -= Solid.make_cylinder(tt["blade"]["hole_d"] / 2, th * 2, Plane(origin=Vector(*hc), z_dir=Vector(*n)))
        out += s + plate
    return out


def build():
    part = body()
    part += pads()
    part += side_block()
    part += lugs()
    part -= pad_cuts()
    part -= side_cuts()
    part -= grooves_cut()
    part -= lug_notch_cut()
    part -= bore_cut()
    part -= web_and_counterbore_cut()
    part -= pockets_cut()
    part += pins()
    part += pipes_and_terminals()
    return part.clean()


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "out")
    out.mkdir(parents=True, exist_ok=True)
    part = build()
    sol = part.solids()
    print("solids", len(sol), "valid", part.is_valid, "volume %.1f" % part.volume, "faces", len(part.faces()))
    if len(sol) != 1:
        print("solid volumes", sorted((round(s.volume, 2) for s in sol), reverse=True)[:6])
    export_step(part, str(out / "thermoblock_ft_datum.step"))
    export_stl(part, str(out / "thermoblock_ft_datum.stl"), tolerance=0.01, angular_tolerance=0.1)
    json.dump({k: v for k, v in P.items()}, open(out / "params.json", "w"), indent=1)
