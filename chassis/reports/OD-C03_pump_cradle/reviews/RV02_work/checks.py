"""RV02 reviewer checks: every gate predicate used on the delivered part and on the mutants."""
import math
from pathlib import Path
import build123d as bd
from build123d import Plane, Keep, GeomType, Vector
from tools.result import gate, Result, inconclusive
from tools.core import validity
from tools.core.step import compare_step
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide,
                           overhang_census, radial_profile, radial_extent, clearance, interference)
MM, DEG, MM3, CNT = 0.005, 0.001, 0.001, 0
AX = ((0, 0, 0), (0, 0, 1), (1, 0, 0))
HOLES = [(-34.0, -4.0), (-34.0, 37.0), (34.0, -4.0), (34.0, 37.0)]

def g_validity(s):
    v = validity(s)
    return [gate("U-01", v["solid_count"], "==", 1, band=CNT), gate("U-01", v["brep_valid"], "==", 1, band=CNT),
            gate("U-01", v["naked_edges"], "==", 0, band=CNT)]

def g_envelope(s):
    e = envelope(s)
    return [gate("U-02", e["size_x"], "in", (79.9, 80.1), band=MM), gate("U-02", e["size_y"], "in", (39.9, 40.1), band=MM),
            gate("U-02", e["size_z"], "in", (51.9, 52.1), band=MM),
            gate("REQ-08", e["max_y"], "in", (39.9, 40.1), band=MM, assumes=["A-11"])], e

def g_census(s):
    fc = feature_census(s)
    want = {"plane_faces": 48, "cylinder_faces": 6, "concave_cylinders": 6, "convex_cylinders": 0, "bores": 4,
            "cone_faces": 0, "sphere_faces": 0, "torus_faces": 0, "bspline_faces": 0, "other_faces": 0}
    return [gate("U-05", fc[k], "==", v, band=CNT, required=f"{k} == {v}") for k, v in want.items()]

def g_bores(s):
    bc = bore_census(s); rows = []
    for x, z in HOLES:
        lb = locate_bore(bc, (x, 38.5, z), (0, 1, 0))
        rows += [gate("REQ-07", lb["diameter"], "in", (3.3, 3.5), band=MM, assumes=["A-11"]),
                 gate("REQ-07", lb["offset"], "<=", 0.10, band=MM, assumes=["A-11"]),
                 gate("REQ-07", lb["through"], "==", 1, band=CNT, assumes=["A-11"]),
                 gate("D-04a", lb["diameter"], ">=", 3.25, band=MM)]
    return rows

def g_walls(s):
    mw = min_wall(s); ww = min_wall_wide(s)
    return [gate("D-01a", mw, ">=", 0.8, band=MM), gate("D-01b", mw, ">=", 2.0, band=MM),
            gate("D-06a", mw, ">=", 1.0, band=MM), gate("U-06", ww, ">=", 2.0, band=MM)], mw

def g_overhang(s):
    oh = overhang_census(s, build_dir=(0, -1, 0), min_deg=45)
    return [gate("D-03a", oh, ">=", 45.0, band=DEG, assumes=["A-13"])], oh

def bridge_span(s):
    """Largest flat downward-facing (normal +Y, print along -Y) planar face off the bed: its smaller in-plane size."""
    bed = s.bounding_box().max.Y; spans = []
    for f in s.faces():
        if f.geom_type != GeomType.PLANE: continue
        n = f.normal_at()
        if n.Y > 1 - 1e-9 and abs(f.center().Y - bed) > 0.01:
            bb = f.bounding_box(); spans.append((min(bb.size.X, bb.size.Z), (round(f.center().X, 3), round(f.center().Y, 3), round(f.center().Z, 3))))
    if not spans: return Result("bridge_span", 0.0, "mm", at=None, detail={"flat_ceilings": 0})
    m = max(spans); return Result("bridge_span", m[0], "mm", at=m[1], detail={"flat_ceilings": len(spans)})

def g_bridge(s):
    return [gate("D-03b", bridge_span(s), "<=", 5.0, band=MM)]

def g_radial(s):
    rows = []
    for band in ((-2.5, 2.5), (25.5, 30.5)):
        rp = radial_profile(s, *AX, list(range(50, 131, 5)), band, margin=0, z_step=0.1, side="inner")
        rows += [gate("REQ-01", rp["min"], "in", (26.60, 26.70), band=MM, assumes=["A-03"]),
                 gate("REQ-01", rp["max"], "in", (26.60, 26.70), band=MM, assumes=["A-03"])]
    return rows

def g_req02(s):
    rows = []
    for z in (0.0, 28.0):
        for a in (50, 130):
            rows.append(gate("REQ-02", radial_extent(s, *AX, a, z, side="inner"), "<=", 26.70, band=MM, assumes=["A-06"]))
        for a in (40, 140):
            r = radial_extent(s, *AX, a, z, side="inner", r_min=0, r_max=32.0)
            # expected reading: INCONCLUSIVE "no material"; anything found in the window is a FAIL
            nomat = (not r.ok) and r.reason.startswith("NoMaterial")
            rows.append(gate("REQ-02", Result("no_material_r_le_32", int(nomat), "bool", at=(a, z),
                                               detail={"reading": r.reason or r.measured}), "==", 1, band=CNT, assumes=["A-06"]))
    return rows

def cut_faces(s, origin, normal):
    n = Vector(*normal); out = []
    for sol in s.solids():
        half = bd.split(sol, bisect_by=Plane(origin=origin, z_dir=n), keep=Keep.BOTTOM)
        if half is None: continue
        for f in half.faces():
            if f.geom_type == GeomType.PLANE and abs(abs(f.normal_at().dot(n)) - 1) < 1e-6 and abs((f.center() - Vector(*origin)).dot(n)) < 1e-6:
                out.append(f)
    return out

def rib_faces(s):
    """z of the rib side faces in the YZ section at x = 0 (edges at constant z spanning the saddle to the foot top)."""
    zs = []
    for f in cut_faces(s, (0, 0, 0), (1, 0, 0)):
        for e in f.edges():
            a, b = e.position_at(0), e.position_at(1)
            if abs(a.Z - b.Z) < 1e-9 and min(a.Y, b.Y) < 30 and max(a.Y, b.Y) > 30:
                zs.append(round(a.Z, 9))
    return sorted(set(zs))

def g_ribfaces(s):
    zs = rib_faces(s); rows = []
    for want in (-3.0, 3.0, 25.0, 31.0):
        near = min(zs, key=lambda z: abs(z - want)) if zs else None
        r = Result("rib_face_z", near, "mm", at=(0, 30, near)) if near is not None else inconclusive("rib_face_z", "mm", "no rib face in the section")
        rows.append(gate("REQ-02", r, "in", (want - 0.10, want + 0.10), band=MM, assumes=["A-06"]))
    return rows, zs

def slots(s):
    """Slots from the YZ sections at x = +-31.5: the islands of the cut face."""
    res = []
    for x in (-31.5, 31.5):
        for f in cut_faces(s, (x, 0, 0), (1, 0, 0)):
            outer = f.outer_wire(); ob = outer.bounding_box()
            for w in f.inner_wires():
                vert = []; slope = []
                for e in w.edges():
                    a, b = e.position_at(0), e.position_at(1)
                    if abs(a.Z - b.Z) < 1e-9: vert.append((a.Z, min(a.Y, b.Y), max(a.Y, b.Y)))
                    elif abs(a.Y - b.Y) > 1e-9: slope.append(math.degrees(math.atan2(abs(a.Y - b.Y), abs(a.Z - b.Z))))
                wb = w.bounding_box()
                zc = [v[0] for v in vert]
                res.append({"x": x, "clear_z": max(zc) - min(zc), "clear_y": min(v[2] - v[1] for v in vert),
                            "yc": sum((v[1] + v[2]) / 2 for v in vert) / len(vert), "zc": (max(zc) + min(zc)) / 2,
                            "roof_deg": min(slope) if slope else 0.0, "z0": wb.min.Z, "z1": wb.max.Z,
                            "block": (ob.min.Z, ob.max.Z), "post_block_z": None})
    return res

def g_slots(s):
    sl = slots(s); rows = []
    # post block z range at the slot level from the XZ section at y = 7
    for d in sl:
        want_z = 17.0 if d["zc"] < 22.5 else 28.0
        A7 = ["A-07"]
        rows += [gate("REQ-05", Result("slot_clear_z", d["clear_z"], "mm", at=(d["x"], d["yc"], d["zc"])), ">=", 6.0, band=MM, assumes=A7),
                 gate("REQ-05", Result("slot_clear_y", d["clear_y"], "mm", at=(d["x"], d["yc"], d["zc"])), ">=", 2.5, band=MM, assumes=A7),
                 gate("REQ-05", Result("slot_yc", d["yc"], "mm", at=(d["x"], d["yc"], d["zc"])), "in", (6.5, 7.5), band=MM, assumes=A7),
                 gate("REQ-05", Result("slot_zc", d["zc"], "mm", at=(d["x"], d["yc"], d["zc"])), "in", (want_z - 0.5, want_z + 0.5), band=MM, assumes=A7),
                 gate("REQ-05", Result("slot_roof_deg", d["roof_deg"], "deg", at=(d["x"], d["yc"], d["zc"])), ">=", 45.0, band=DEG, assumes=A7 + ["A-13"])]
    # ligaments along z at the slot centre plane y = 7
    for x in (-31.5, 31.5):
        spans = sorted([(f.bounding_box().min.Z, f.bounding_box().max.Z) for f in cut_faces(s, (0, 7.0, 0), (0, 1, 0))
                        if f.bounding_box().min.X * x > 0])
        for z0, z1 in spans:
            rows.append(gate("REQ-05", Result("slot_ligament", z1 - z0, "mm", at=(x, 7.0, (z0 + z1) / 2)), ">=", 2.0, band=MM, assumes=["A-07"]))
    return rows, sl

def post_faces(s):
    """Inner faces of the post blocks: planar faces with normal toward the axis along X at 26 < |x| < 36."""
    out = []
    for f in s.faces():
        if f.geom_type != GeomType.PLANE: continue
        n = f.normal_at(); c = f.center(); bb = f.bounding_box()
        if abs(abs(n.X) - 1) < 1e-9 and 26 < abs(c.X) < 36 and n.X * c.X < 0 and bb.size.Y > 20:
            out.append({"x": c.X, "z0": bb.min.Z, "z1": bb.max.Z, "y0": bb.min.Y, "y1": bb.max.Y})
    return out

def g_posts(s):
    rows = []
    for p in post_faces(s):
        A6 = ["A-06"]
        rows += [gate("REQ-06", Result("post_inner_x", abs(p["x"]), "mm", at=(p["x"], 18.5, 22.5)), "in", (29.4, 29.6), band=MM, assumes=A6),
                 gate("REQ-06", Result("post_z0", p["z0"], "mm", at=(p["x"], 18.5, p["z0"])), "in", (11.9, 12.1), band=MM, assumes=A6),
                 gate("REQ-06", Result("post_z1", p["z1"], "mm", at=(p["x"], 18.5, p["z1"])), "in", (32.9, 33.1), band=MM, assumes=A6)]
    return rows

def foot_thickness(s):
    top = [f for f in s.faces() if f.geom_type == GeomType.PLANE and f.normal_at().Y < -1 + 1e-9 and f.bounding_box().size.X > 70]
    if not top: return inconclusive("foot_thickness", "mm", "no foot top face")
    y = top[0].center().Y; return Result("foot_thickness", s.bounding_box().max.Y - y, "mm", at=(0, y, 16))

def g_foot(s):
    return [gate("REQ-08", foot_thickness(s), "in", (2.9, 3.1), band=MM, assumes=["A-11"])]

def g_pump(s, pump, sleeve):
    c = clearance(s, pump); cs = clearance(s, sleeve)
    it = interference({"cradle": s, "pump": pump, "sleeve": sleeve})
    return [gate("REQ-03", c, ">=", 2.0, band=MM, assumes=["A-01", "A-03"]),
            gate("D-04c", c, ">=", 0.5, band=MM, assumes=["A-01"]),
            gate("U-03", c, ">=", 2.0, band=MM, assumes=["A-01", "A-03"]),
            gate("U-03", it["cradle|pump"], "<=", 0.0, band=MM3, assumes=["A-01"]),
            gate("U-03", cs, "==", 0.0, band=MM, assumes=["A-03"]),
            gate("U-03", it["cradle|sleeve"], "<=", 0.0, band=MM3, assumes=["A-03"]),
            gate("REQ-04", cs, "==", 0.0, band=MM, assumes=["A-03"]),
            gate("REQ-04", it["cradle|sleeve"], "<=", 0.0, band=MM3, assumes=["A-03"])], (c, cs, it)

def g_roundtrip(s, path):
    r = compare_step(s, path)
    return [gate("U-04", r["schema"], "==", 1, band=CNT), gate("U-04", r["solids"], "==", 1, band=CNT),
            gate("U-04", r["volume_delta"], "<=", 0.001, band=MM3), gate("U-04", r["faces_delta"], "==", 0, band=CNT),
            gate("U-04", r["labels"], "==", 1, band=CNT), gate("U-04", r["valid_after"], "==", 1, band=CNT)]

def worst(rows):
    bad = [r for r in rows if r.status in ("FAIL", "INCONCLUSIVE")]
    return "FAIL" if any(r.status == "FAIL" for r in bad) else ("INCONCLUSIVE" if bad else "PASS")
