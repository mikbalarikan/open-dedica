"""RV01 part-level re-measurement of the exported tray STEP."""
import sys, math, json, time
sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
import numpy as np
from build123d import Box, Cylinder, Pos, Rot, Plane, Location, Axis as BAxis
from tools.core import read_step, validity
from tools.core.shapes import faces
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide,
                           overhang_census, flat_ceiling_spans, radial_extent, mass_properties)
from tools.measure.features import cylinder
from tools.measure.sampling import kind
from tools.result import Result

t = read_step(PART)
for k, r in validity(t).items():
    g({"solid_count": "U-01", "brep_valid": "U-01", "naked_edges": "U-01"}[k], r, "==", 1 if k != "naked_edges" else 0, note=k)
g("exactly_one_solid", validity(t)["solid_count"], "==", 1)
env = envelope(t)
for ax, n in (("x", 39.0), ("y", 92.0), ("z", 160.0)):
    g("U-02", env[f"size_{ax}"], "in", (n - 0.1, n + 0.1), note=f"size_{ax}")
    g("envelope_within_spec", env[f"size_{ax}"], "in", (n - 0.1, n + 0.1), note=f"size_{ax}")
for k, n in (("min_x", 73.0), ("max_x", 112.0), ("min_y", 0.0), ("max_y", 92.0), ("min_z", -230.0), ("max_z", -70.0)):
    g("U-02", env[k], "in", (n - 0.1, n + 0.1), note="position " + k)
# D-02 bed (lying on wall: bed 92 x 160, height 39) vs 220x220x250 (A-09)
g("D-02", env["size_y"], "<=", 220.0, assumes=["A-09"], note="bed y")
g("D-02", env["size_z"], "<=", 220.0, assumes=["A-09"], note="bed z")
g("D-02", env["size_x"], "<=", 250.0, assumes=["A-09"], note="height x")
# REQ-03
g("REQ-03", env["min_x"], ">=", 73.0, assumes=["A-06"], note="min_x")
g("REQ-03", env["max_z"], "in", (-70.1, -69.9), assumes=["A-06"], note="front z")

fc = feature_census(t)
exp = {"plane_faces": 42, "cylinder_faces": 12, "cone_faces": 0, "sphere_faces": 0, "torus_faces": 0,
       "bspline_faces": 0, "other_faces": 0, "concave_cylinders": 6, "convex_cylinders": 6, "bores": 6}
for k, v in exp.items():
    g("feature_census", fc[k], "==", v, note=k)
bc = bore_census(t)
holes = [(88.0, -222.0), (106.0, -222.0), (88.0, -78.0), (106.0, -78.0)]
for x, z in holes:
    lb = locate_bore(bc, (x, 2.0, z), (0, 1, 0))
    tag = f"hole x{x:g} z{z:g}"
    g("REQ-01", lb["diameter"], "in", (3.3, 3.5), assumes=["A-01"], note=tag + " dia")
    g("REQ-01", lb["offset"], "<=", 0.10, assumes=["A-01"], note=tag + " offset")
    g("REQ-01", lb["length"], "in", (3.9, 4.1), assumes=["A-01"], note=tag + " length")
    g("REQ-01", lb["through"], "==", 1, assumes=["A-01"], note=tag + " through")
    g("D-04a", lb["diameter"], ">=", 3.25, note=tag)
    print("   bore", lb["offset"].detail)
# flange underside: planar faces with normal -Y at min y
unders = []
for f in t.faces():
    if kind(f.wrapped) == "plane":
        n = f.normal_at(f.center()); bb = f.bounding_box()
        if n.Y < -0.999 and bb.max.Y < 0.2: unders.append((bb.min.Y, bb.max.Y, f.area))
print("underside faces", unders)
g("REQ-01", Result("underside_faces", len(unders), "count"), "==", 1, assumes=["A-01"], note="underside one plane")
g("REQ-01", Result("underside_y", max(abs(u[0]) for u in unders) if unders else None, "mm", at=(92.5, 0, -150)), "<=", 0.10, assumes=["A-01"], note="underside |y|")

# insert bores
inserts = [(80.0, -100.0), (27.99, -100.01)]
for y, z in inserts:
    lb = locate_bore(bc, (80.0, y, z), (1, 0, 0))
    tag = f"insert y{y:g} z{z:g}"
    d = lb["diameter"]; L = lb["length"]
    print("   bore", lb["offset"].detail)
    g("D-05b", d, "in", (3.95, 4.05), assumes=["A-07"], note=tag + " dia")
    g("D-05b", L, "in", (5.9, 6.1), assumes=["A-07"], note=tag + " depth")
    g("D-05b", L, ">=", 5.7, assumes=["A-07"], note=tag + " depth>=5.7")
    g("D-05b", lb["through"], "==", 0, assumes=["A-07"], note=tag + " blind")
    g("REQ-02", d, "in", (3.95, 4.05), assumes=["A-02", "A-03"], note=tag + " dia")
    g("REQ-02", lb["offset"], "<=", 0.10, assumes=["A-02", "A-03"], note=tag + " offset")
    mouth = max(lb["offset"].detail["start"][0], lb["offset"].detail["end"][0])
    g("REQ-02", Result("mouth_x", mouth, "mm", at=(mouth, y, z)), "in", (82.39, 82.49), assumes=["A-02", "A-03"], note=tag + " mouth x")
    # D-05a across and J-05 wall: rays every 15 deg at 3 depths, window 0..6
    across = []; walls = []
    for zz in (0.5, 3.0, 5.5):
        for a in range(0, 180, 15):
            r1 = radial_extent(t, (76.438, y, z), (1, 0, 0), (0, 1, 0), a, zz, side="outer", r_max=6.0)
            r2 = radial_extent(t, (76.438, y, z), (1, 0, 0), (0, 1, 0), a + 180, zz, side="outer", r_max=6.0)
            i1 = radial_extent(t, (76.438, y, z), (1, 0, 0), (0, 1, 0), a, zz, side="inner", r_max=6.0)
            i2 = radial_extent(t, (76.438, y, z), (1, 0, 0), (0, 1, 0), a + 180, zz, side="inner", r_max=6.0)
            ok = all(r.status == "MEASURED" for r in (r1, r2, i1, i2))
            if not ok:
                print("   INCONCL ray", a, zz, [r.reason for r in (r1, r2, i1, i2) if r.status != "MEASURED"])
                across.append((None, a, zz)); continue
            across.append((r1.measured + r2.measured, a, zz, r1.at))
            walls.append((r1.measured - i1.measured, a, zz, r1.at)); walls.append((r2.measured - i2.measured, a + 180, zz, r2.at))
    bad = [c for c in across if c[0] is None]
    amin = min((c for c in across if c[0] is not None), key=lambda c: c[0])
    wmin = min(walls, key=lambda c: c[0])
    g("D-05a", Result("across", None if bad else amin[0], "mm", at=amin[3]) if not bad else Result("across", None, "mm", status="INCONCLUSIVE", reason="ray inconclusive"), ">=", 8.0, assumes=["A-07"], note=tag + f" least across at {amin[1]}deg depth {amin[2]}")
    g("J-05", Result("boss_wall", None if bad else wmin[0], "mm", at=wmin[3]) if not bad else Result("boss_wall", None, "mm", status="INCONCLUSIVE", reason="ray inconclusive"), ">=", 3.0, note=tag + f" least wall at {wmin[1]}deg depth {wmin[2]}")

# cylinders: standoffs and pins
cyls = []
for f in t.faces():
    if kind(f.wrapped) == "cylinder":
        o, d, r = cylinder(f.wrapped); bb = f.bounding_box()
        cyls.append(dict(o=o.tolist(), d=d.tolist(), r=r, xmin=bb.min.X, xmax=bb.max.X, ymin=bb.min.Y, ymax=bb.max.Y, zmin=bb.min.Z, zmax=bb.max.Z))
for c in cyls: print("   cyl", {k: (round(v, 4) if isinstance(v, float) else [round(q, 4) for q in v]) for k, v in c.items()})
pins_spec = [(81.98, -157.52), (30.99, -157.51)]
pin_axes = {}
for y, z in pins_spec:
    cand = [c for c in cyls if abs(c["r"] - 0.9) < 0.2 and abs(c["d"][0]) > 0.999]
    best = min(cand, key=lambda c: math.hypot(c["o"][1] - y, c["o"][2] - z))
    off = math.hypot(best["o"][1] - y, best["o"][2] - z)
    pin_axes[(y, z)] = (best["o"][1], best["o"][2])
    tag = f"pin y{y:g} z{z:g}"
    at = (best["xmin"], best["o"][1], best["o"][2])
    g("REQ-02", Result("pin_d", 2 * best["r"], "mm", at=at), "in", (1.75, 1.85), assumes=["A-02", "A-03"], note=tag + " dia")
    g("REQ-02", Result("pin_len", best["xmax"] - best["xmin"], "mm", at=at), "in", (2.4, 2.6), assumes=["A-02", "A-03"], note=tag + f" length x {best['xmin']:.3f}..{best['xmax']:.3f}")
    g("REQ-02", Result("pin_offset", off, "mm", at=at), "<=", 0.10, assumes=["A-02", "A-03"], note=tag + " offset")
    g("D-06a", Result("pin_d", 2 * best["r"], "mm", at=at), ">=", 1.0, note=tag + " diameter (exact cylinder)")
# standoffs grow from wall
so = [c for c in cyls if abs(c["r"] - 5.0) < 0.01 or abs(c["r"] - 3.0) < 0.01]
for c in so:
    print("   standoff r", c["r"], "x", c["xmin"], c["xmax"], "axis", c["o"])
# seats: +X planar faces at x~82.438
seats = []
for f in t.faces():
    if kind(f.wrapped) == "plane":
        n = f.normal_at(f.center()); bb = f.bounding_box()
        if n.X > 0.999 and 82.0 < bb.min.X < 83.0: seats.append((bb.min.X, bb.max.X, f.center().Y, f.center().Z, f.area))
print("seats", seats)
g("REQ-02", Result("seat_faces", len(seats), "count"), "==", 4, assumes=["A-02", "A-03"], note="seat faces +X at x~82.44")
for s in seats:
    g("REQ-02", Result("seat_x", s[0], "mm", at=(s[0], s[2], s[3])), "in", (82.39, 82.49), assumes=["A-02", "A-03"], note=f"seat y{s[2]:.2f} z{s[3]:.2f} area {s[4]:.2f}")
g("REQ-02", Result("seat_coplanar", max(s[0] for s in seats) - min(s[0] for s in seats), "mm"), "<=", 0.0, assumes=["A-02", "A-03"], note="coplanar spread")

# walls
t0 = time.time()
mw = min_wall(t, spacing=0.7); print("min_wall", mw.measured, mw.at, mw.status, mw.reason, round(time.time() - t0), "s", {k: mw.detail.get(k) for k in ("wide", "largest_step_mm")})
g("D-01a", mw, ">=", 0.8, note="whole part")
g("D-06a", mw, ">=", 1.0, note="whole part min_wall")
mww = min_wall_wide(t, spacing=0.7); print("wide whole", mww.measured, mww.at, mww.status)
g("U-06", mww, ">=", 2.0, note="whole part, wide 45deg")
# without pins: cut x>82.438 within r 2 of each pin axis
nopin = t
for (y, z), (py, pz) in pin_axes.items():
    nopin = nopin - Pos(84.0, py, pz) * Box(3.2, 3.0, 3.0)
nopin = nopin.solids()[0] if hasattr(nopin, "solids") and len(nopin.solids()) == 1 else nopin
print("nopin volume", nopin.volume, "orig", t.volume)
mwn = min_wall(nopin, spacing=0.7); print("min_wall nopin", mwn.measured, mwn.at, mwn.status, mwn.reason)
g("D-01b", mwn, ">=", 2.0, note="part less the two pins")
mwwn = min_wall_wide(nopin, spacing=0.7); print("wide nopin", mwwn.measured, mwwn.at, mwwn.status)
g("U-06", mwwn, ">=", 2.0, note="part less the two pins, wide 45deg")

# overhang, build +X
oc = overhang_census(t, build_dir=(1, 0, 0), spacing=0.7); print("overhang whole", oc.measured, oc.at, oc.status, oc.reason, {k: oc.detail.get(k) for k in ("per_kind_least_deg", "below_min_deg", "bed_samples", "sampling_bound_deg")})
filled = t
for x, z in holes:
    filled = filled + Pos(x, 2.0, z) * Rot(90, 0, 0) * Cylinder(1.7, 4.0)
print("filled solids", len(filled.solids()), filled.volume)
filled = filled.solids()[0]
ocf = overhang_census(filled, build_dir=(1, 0, 0), spacing=0.7); print("overhang filled", ocf.measured, ocf.at, ocf.status, ocf.reason, ocf.detail.get("per_kind_least_deg"))
g("D-03a", ocf, ">=", 45.0, assumes=["A-08"], note="four flange holes refilled by position (named exception); whole part least %s deg at %s" % (oc.measured, oc.at))
fcs = flat_ceiling_spans(t, build_dir=(1, 0, 0), max_span=5.0, spacing=0.7); print("flat ceilings", fcs.measured, fcs.at, fcs.status, fcs.reason)
g("D-03b", fcs, "<=", 5.0, assumes=["A-08"], note="flat ceilings, build +X")
mp = mass_properties(t, 1270); print({k: (v.measured, v.at) for k, v in mp.items()})
dump("r01_part.json", {"cyls": cyls, "seats": seats, "unders": unders, "bores": bc.detail["bores"], "pin_axes": {str(k): v for k, v in pin_axes.items()},
                       "min_wall_detail": str(mw.detail)[:2000], "overhang_whole": [oc.measured, oc.at, str(oc.detail)[:3000]]})
