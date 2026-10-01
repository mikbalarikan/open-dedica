"""Checks for od_c05_carrier v02, concept C4 (job 20260930-od-c05-group-head-carrier,
spec 2.0 section 5).

Written before the build (PLAYBOOK D3). Every predicate re-imports the exported STEP
files, measures with tools.measure / tools.core, and compares through
tools.result.gate with the GATES.md section 0 band. A raised exception or a missing
value is INCONCLUSIVE, never PASS.

Frame: the OD-G01 STEP frame (spec 2.0 section 2): Z the group head axis, +Z the
mouth (down in the machine), +Y the front; plate z -29.94 .. -24.94, floor z +180.06.
Print: on its side, the x = -55 face on the bed, build direction +X (A-13).

Usage (from the repository root):
  uv run tools/run.py python <ws>/01_CAD/check_od_c05_carrier_v02.py \
      [--step P] [--assembly P] [--stl P] [--expect JSON] [--out JSON]
Defaults are the v02 deliverables of this workspace. --expect overrides the
build-derived positive-control values (sweep runs); the gate limits never change.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import traceback
from pathlib import Path

import numpy as np
from build123d import Box, Location
from OCP.BRep import BRep_Builder, BRep_Tool
from OCP.BRepTools import BRepTools
from OCP.GeomLProp import GeomLProp_SLProps
from OCP.TopoDS import TopoDS_Shell, TopoDS_Solid

from tools.core import common_volume, compare_step, mesh_sagitta, read_step, validity
from tools.core.shapes import faces as occ_faces
from tools.core.shapes import vertices as occ_vertices
from tools.measure import (bore_census, clearance, envelope, feature_census, interference,
                           locate_bore, mass_properties, mesh_census, min_wall, overhang_census,
                           radial_extent)
from tools.measure.features import cylinder as cyl_axis
from tools.measure.sampling import kind as face_kind
from tools.measure.sampling import outward_normal
from tools.measure.wall import load_mesh
from tools.result import INCONCLUSIVE, Gate, Result, gate, inconclusive

WS = Path(__file__).resolve().parents[1]
TAG = "v02"

# ---- band: GATES.md section 0 (L-21) -------------------------------------------------
BAND_MM, BAND_DEG, BAND_MM3, BAND_N = 0.005, 0.001, 0.001, 0

# ---- limits: spec 2.0 section 5 only (D-009) -----------------------------------------
SPEC = {
    "size": (110.0, 152.0, 210.0), "size_tol": 0.1,                         # U-02
    "pos": {"min_x": -55.0, "max_x": 55.0, "min_y": -102.0, "max_y": 50.0,
            "min_z": -29.94, "max_z": 180.06},                              # U-02 position, reported apart
    "og04_clearance_min": 2.0,                                              # U-03
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0,              # D-01a, D-01b, D-06a
    "wide_wall": 2.0,                                                       # U-06 (Soft)
    "bed_xy": 220.0, "height": 250.0,                                       # D-02, A-08: y, z on the bed, x tall
    "build_dir": (1.0, 0.0, 0.0),                                           # D-03a threshold text, section 4, A-13
    "overhang_min_deg": 45.0,                                               # D-03a
    "bridge_max": 5.0, "exception_bridge_max": 6.6,                         # D-03b and its named exception
    "clearance_hole_min_d": 3.25,                                           # D-04a
    "hole_d": 3.4, "hole_d_tol": 0.1, "hole_offset_max": 0.10,              # REQ-01, REQ-06
    "cb_d": 6.5, "cb_d_tol": 0.1, "cb_depth": 2.0, "cb_depth_tol": 0.1,     # REQ-02
    "z_top": -29.94, "z_under": -24.94, "face_tol": 0.10, "plate_t": 5.0,   # REQ-03 (plate 3.0 + 2.0)
    "hub_r": 30.0,                                                          # REQ-04
    "z_floor": 180.06, "floor_tol": 0.10, "foot_t": 4.0, "foot_t_tol": 0.1, # REQ-05
    "keepout_min_y": -102.0,                                                # REQ-07
    "gusset_gap_min": 1.0, "wall_gap_min": 2.0,                             # REQ-08
    "stl_tol": 0.01, "stl_ang_limit": 4 * math.acos(1 - 0.01 / 6.0),        # U-07
}
# U-05 feature census: DESIGN_PLAN_v02 section 3 counts.
CENSUS_EXPECT = {"plane_faces": 24, "cylinder_faces": 15, "cone_faces": 0, "sphere_faces": 0,
                 "torus_faces": 0, "bspline_faces": 0, "other_faces": 0,
                 "concave_cylinders": 13, "convex_cylinders": 2, "bores": 13}
# REQ-04 readings named by the spec row (theta 0: gable apex; theta 90: the arc).
EXPECT = {"hub_apex_r": 30.0 * math.sqrt(2), "hub_side_r": 30.0,
          "gusset_x_in": 51.0, "wall_y_front": -52.0, "z_foot_top": 176.06}   # section 4 C4 (the sweep moves them)
DENSITY = 1070.0                                   # kg/m3, spec section 3, A-12 (reported only)
Z_LEVELS = (-29.9, -29.44, -27.44, -25.44, -24.98)  # inside the plate z -29.94 .. -24.94
HOLES_PLATE = [(sx * 44.0, sy * 44.0) for sy in (1, -1) for sx in (1, -1)]
HOLES_FOOT = [(sx * 35.0, y) for y in (-72.0, -92.0) for sx in (1, -1)]


def gusset_boxes(e):
    """Gusset regions by position (section 4 C4): x range, y range, z range, following
    the swept wall front face and foot top (the gate limits never change)."""
    yf, zf = e["wall_y_front"], e["z_foot_top"]
    return {f"{side} {pair}": ((lo, lo + 4.0), ys, zs)
            for side, lo in (("+X", 51.0), ("-X", -55.0))
            for pair, ys, zs in (("front", (yf, yf + 40.0), (-24.94, 15.06)),
                                 ("rear", (-98.0, -58.0), (zf - 40.0, zf)))}


def g(gid, result, op, limit, band, assumes=(), required=None):
    try:
        return gate(gid, result, op, limit, band=band, assumes=assumes, required=required)
    except Exception as exc:   # noqa: BLE001
        return Gate(gid, None, getattr(result, "unit", ""), str(limit), None, None, INCONCLUSIVE,
                    getattr(result, "name", "?"), tuple(assumes), f"{type(exc).__name__}: {exc}")


def value(name, measured, unit, at=None, **detail):
    if measured is None:
        return inconclusive(name, unit, "no value")
    return Result(name, measured, unit, at=at, detail=detail)


def na(gid, why):
    return Gate(gid, None, "", "N/A", None, None, "N/A", "none", (), why)


def label_parts(asm):
    return {child.label: child for child in (getattr(asm, "children", ()) or ())}


def box_between(x, y, z):
    """A build123d box spanning the given (low, high) ranges."""
    return Location((x[0], y[0], z[0])) * Box(x[1] - x[0], y[1] - y[0], z[1] - z[0], align=None)


def solid_of(shape_faces, keep):
    """A solid built from the chosen faces of a solid, orientation kept: used only to
    run overhang_census with the named-exception faces left out (spec 2.0 D-03a)."""
    builder = BRep_Builder()
    shell = TopoDS_Shell()
    builder.MakeShell(shell)
    for f in shape_faces:
        if keep(f):
            builder.Add(shell, f)
    solid = TopoDS_Solid()
    builder.MakeSolid(solid)
    builder.Add(solid, shell)
    return solid


def exception_face(f) -> bool:
    """The twelve bores along Z of the named exception (4 plate holes, 4 counterbores,
    4 foot holes): cylindrical, axis along Z, radius 1.5 .. 3.5, axis within 0.2 of a
    hole centre (selected by position)."""
    if face_kind(f) != "cylinder":
        return False
    origin, direction, radius = cyl_axis(f)
    if abs(abs(direction[2]) - 1.0) > 1e-6 or not (1.5 <= radius <= 3.5):
        return False
    return any(math.hypot(origin[0] - x, origin[1] - y) <= 0.2 for x, y in HOLES_PLATE + HOLES_FOOT)


def face_center(f):
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    p = GProp_GProps()
    BRepGProp.SurfaceProperties_s(f, p)
    c = p.CentreOfMass()
    return (c.X(), c.Y(), c.Z())


def face_area(f):
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    p = GProp_GProps()
    BRepGProp.SurfaceProperties_s(f, p)
    return p.Mass()


def analytic_downward(carrier, build_dir, bed_x):
    """Every downward face with its least angle from horizontal (job code, beside the
    census; RV01 F3): a plane by its normal; a cylinder by its normal over 3601 points
    of its u range, its bounds included (its normal does not change along v). Points
    within 0.01 of the bed height are left out, as overhang_census does. Returns a list
    of dicts, least first."""
    b = np.asarray(build_dir, float)
    out = []
    for f in occ_faces(carrier):
        k = face_kind(f)
        u0, u1, v0, v1 = BRepTools.UVBounds_s(f)
        props = GeomLProp_SLProps(BRep_Tool.Surface_s(f), 1, 1e-7)
        if k == "plane":
            us = [0.5 * (u0 + u1)]
        elif k == "cylinder":
            us = list(np.linspace(u0, u1, 3601))
        else:
            out.append({"kind": k, "least_deg": None, "note": "not listed analytically"})
            continue
        vs = (v0, 0.5 * (v0 + v1), v1) if k == "cylinder" else (0.5 * (v0 + v1),)
        best = None
        for u in us:
            n = outward_normal(f, u, 0.5 * (v0 + v1), props)
            if n is None:
                continue
            toward = -float(np.dot(n, b))
            if toward <= 1e-9:
                continue
            ang = math.degrees(math.acos(min(1.0, toward)))
            for v in vs:
                p = props
                p.SetParameters(u, v)
                pt = p.Value()
                h = float(np.dot((pt.X(), pt.Y(), pt.Z()), b))
                if h - bed_x <= 0.01:
                    continue
                if best is None or ang < best[0]:
                    best = (ang, (round(pt.X(), 4), round(pt.Y(), 4), round(pt.Z(), 4)))
                break
        if k == "plane":
            c = face_center(f)
            if best is not None and abs(float(np.dot(c, b)) - bed_x) <= 0.01:
                best = None      # the bed face itself
        if best is None:
            continue
        verts = [BRep_Tool.Pnt_s(v) for v in occ_vertices(f)]
        pts = np.array([[p.X(), p.Y(), p.Z()] for p in verts]) if verts else np.zeros((0, 3))
        span = float(max(np.linalg.norm(pts[i] - pts[j]) for i in range(len(pts)) for j in range(len(pts)))) \
            if len(pts) > 1 else None
        entry = {"kind": k, "least_deg": round(best[0], 9), "at": best[1], "exception": exception_face(f),
                 "area_mm2": round(face_area(f), 4), "vertex_span_mm": None if span is None else round(span, 4)}
        if k == "cylinder":
            o, d, r = cyl_axis(f)
            entry.update(radius=round(r, 4), axis_point=tuple(round(float(x), 4) for x in o),
                         axis_dir=tuple(round(float(x), 4) for x in d))
        else:
            entry["center"] = tuple(round(x, 4) for x in face_center(f))
        out.append(entry)
    out.sort(key=lambda e: 999 if e["least_deg"] is None else e["least_deg"])
    return out


def ray_set(part, z_levels):
    """REQ-04 (RV01 F4): the innermost material on the whole ray from the axis at every
    10 deg on each level; the least over all rays, with where. Any ray that reads no
    value makes the set INCONCLUSIVE."""
    least, at, bad, n = None, None, [], 0
    for z in z_levels:
        for a in range(0, 360, 10):
            r = radial_extent(part, (0, 0, 0), (0, 0, 1), (1, 0, 0), a, z, side="inner")
            n += 1
            if not r.ok:
                bad.append((a, z, r.reason))
                continue
            if least is None or r.measured < least:
                least, at = r.measured, (a, z, r.at)
    if bad:
        return inconclusive("hub_window_innermost_r", "mm", f"{len(bad)} rays unread: {bad[0]}")
    return Result("hub_window_innermost_r", least, "mm", at=at[2], detail={"rays": n, "theta_deg": at[0], "z": at[1]})


def run(step: Path, assembly: Path | None, stl: Path | None, expect: dict) -> dict:
    S, E = SPEC, {**EXPECT, **expect}
    rows: list[Gate] = []
    facts: dict = {}
    part = read_step(step)
    solids = part.solids()
    carrier = solids[0] if len(solids) == 1 else part

    # exactly_one_solid, U-01
    v = validity(part)
    rows.append(g("exactly_one_solid", v["solid_count"], "==", 1, BAND_N))
    rows.append(g("U-01 solid_count", v["solid_count"], "==", 1, BAND_N))
    rows.append(g("U-01 brep_valid", v["brep_valid"], "==", 1, BAND_N))
    rows.append(g("U-01 naked_edges", v["naked_edges"], "==", 0, BAND_N))

    # envelope: U-02, envelope_within_spec, D-02, REQ-03 top, REQ-05 floor, REQ-07
    env = envelope(part)
    for key, nominal in zip(("size_x", "size_y", "size_z"), S["size"]):
        rows.append(g(f"U-02 {key}", env[key], "in", (nominal - S["size_tol"], nominal + S["size_tol"]), BAND_MM))
    for key, nominal in S["pos"].items():
        rows.append(g(f"envelope_within_spec {key}", env[key], "in", (nominal - S["size_tol"], nominal + S["size_tol"]), BAND_MM))
    rows.append(g("D-02 on the bed y", env["size_y"], "<=", S["bed_xy"], BAND_MM, ("A-08",)))
    rows.append(g("D-02 on the bed z", env["size_z"], "<=", S["bed_xy"], BAND_MM, ("A-08",)))
    rows.append(g("D-02 tall x", env["size_x"], "<=", S["height"], BAND_MM, ("A-08",)))
    rows.append(g("REQ-03 top face z (envelope min_z)", env["min_z"], "in", (S["z_top"] - S["face_tol"], S["z_top"] + S["face_tol"]), BAND_MM, ("A-01",)))
    rows.append(g("REQ-05 foot underside z (envelope max_z)", env["max_z"], "in", (S["z_floor"] - S["floor_tol"], S["z_floor"] + S["floor_tol"]), BAND_MM, ("A-03", "A-04")))
    rows.append(g("REQ-07 min_y", env["min_y"], ">=", S["keepout_min_y"], BAND_MM, ("A-05",)))
    facts["envelope"] = {k: r.measured for k, r in env.items()}

    # U-04 round trip: the file re-read against its own re-import
    rt = compare_step(read_step(step), step)
    rows.append(g("U-04 schema", rt["schema"], "==", 1, BAND_N))
    rows.append(g("U-04 solids", rt["solids"], "==", 1, BAND_N))
    rows.append(g("U-04 volume_delta", rt["volume_delta"], "<=", 0.0, BAND_MM3))
    rows.append(g("U-04 faces_delta", rt["faces_delta"], "==", 0, BAND_N))
    rows.append(g("U-04 valid_after", rt["valid_after"], "==", 1, BAND_N))
    labels_found = [c.label for c in (getattr(part, "children", ()) or ())] or [part.label]
    rows.append(g("U-04 name od_c05_carrier", value("step_label", int("od_c05_carrier" in labels_found), "bool",
                                                    labels=labels_found), "==", 1, BAND_N))

    # feature census, U-05
    fc = feature_census(carrier)
    for key, n in CENSUS_EXPECT.items():
        rows.append(g(f"feature_census {key}", fc[key], "==", n, BAND_N))
    all_faces = occ_faces(carrier)
    facts["cylinders_outside_exception"] = sorted(
        (round(cyl_axis(f)[2], 4), tuple(round(float(x), 3) for x in cyl_axis(f)[0]))
        for f in all_faces if face_kind(f) == "cylinder" and not exception_face(f))

    # bores: U-05, D-04a, REQ-01, REQ-02, REQ-03, REQ-05 thickness, REQ-06
    bc = bore_census(carrier)
    facts["bores"] = bc.detail.get("bores") if bc.ok else bc.reason
    asm_parts, g01_bores = {}, []
    if assembly is not None and assembly.exists():
        asm_parts = label_parts(read_step(assembly))
        facts["assembly_labels"] = list(asm_parts)
    g01 = asm_parts.get("od_g01_housing")
    if g01 is not None:
        gb = bore_census(g01)
        for x, y in HOLES_PLATE:
            loc = locate_bore(gb, (x, y, -22.0), (0, 0, 1))
            if loc["offset"].ok and loc["offset"].measured < 1.0:
                s = loc["offset"].detail["start"]
                g01_bores.append((s[0], s[1]))
            else:
                g01_bores.append(None)
        facts["g01_insert_bores"] = g01_bores
    for i, (x, y) in enumerate(HOLES_PLATE):
        tag = f"({x:+.0f},{y:+.0f})"
        loc = locate_bore(bc, (x, y, S["z_under"] - 1.5), (0, 0, 1))
        rows.append(g(f"U-05/REQ-01 hole {tag} dia", loc["diameter"], "in", (S["hole_d"] - S["hole_d_tol"], S["hole_d"] + S["hole_d_tol"]), BAND_MM, ("A-01",)))
        rows.append(g(f"D-04a plate hole {tag}", loc["diameter"], ">=", S["clearance_hole_min_d"], BAND_MM))
        rows.append(g(f"REQ-01 hole {tag} offset from nominal", loc["offset"], "<=", S["hole_offset_max"], BAND_MM, ("A-01",)))
        rows.append(g(f"REQ-01 hole {tag} through", loc["through"], "==", 1, BAND_N))
        ref = g01_bores[i] if g01_bores else None
        if ref is None:
            r = inconclusive("bore_axis_offset", "mm", "OD-G01 insert bore not located in the check assembly")
        else:
            r = locate_bore(bc, (ref[0], ref[1], S["z_under"] - 1.5), (0, 0, 1))["offset"]
        rows.append(g(f"U-03a/REQ-01 hole {tag} offset from OD-G01 insert", r, "<=", S["hole_offset_max"], BAND_MM, ("A-01",)))
        cb = locate_bore(bc, (x, y, S["z_top"] + 0.5), (0, 0, 1))
        rows.append(g(f"U-05/REQ-02 cb {tag} dia", cb["diameter"], "in", (S["cb_d"] - S["cb_d_tol"], S["cb_d"] + S["cb_d_tol"]), BAND_MM, ("A-09",)))
        rows.append(g(f"REQ-02 cb {tag} depth", cb["length"], "in", (S["cb_depth"] - S["cb_depth_tol"], S["cb_depth"] + S["cb_depth_tol"]), BAND_MM, ("A-09",)))
        rows.append(g(f"REQ-02 cb {tag} coaxial", cb["offset"], "<=", S["hole_offset_max"], BAND_MM, ("A-09",)))
        start_z = None
        if cb["diameter"].ok:
            start_z = min(cb["diameter"].detail["start"][2], cb["diameter"].detail["end"][2])
        rows.append(g(f"REQ-03 top face z (cb {tag} open end)", value("top_face_z", start_z, "mm", at=(x, y, start_z)), "in",
                      (S["z_top"] - S["face_tol"], S["z_top"] + S["face_tol"]), BAND_MM, ("A-01",)))
        under = (start_z + loc["length"].measured + cb["length"].measured) \
            if (start_z is not None and loc["length"].ok and cb["length"].ok) else None
        rows.append(g(f"REQ-03 underside z at {tag} (cb start + cb + hole lengths)", value("underside_z", under, "mm", at=(x, y, under)), "in",
                      (S["z_under"] - S["face_tol"], S["z_under"] + S["face_tol"]), BAND_MM, ("A-01",)))
    for x, y in HOLES_FOOT:
        tag = f"({x:+.0f},{y:.0f})"
        loc = locate_bore(bc, (x, y, S["z_floor"] - 2.0), (0, 0, 1))
        rows.append(g(f"U-05/REQ-06 foot hole {tag} dia", loc["diameter"], "in", (S["hole_d"] - S["hole_d_tol"], S["hole_d"] + S["hole_d_tol"]), BAND_MM, ("A-04",)))
        rows.append(g(f"D-04a foot hole {tag}", loc["diameter"], ">=", S["clearance_hole_min_d"], BAND_MM))
        rows.append(g(f"REQ-06 foot hole {tag} offset", loc["offset"], "<=", S["hole_offset_max"], BAND_MM, ("A-04",)))
        rows.append(g(f"REQ-06 foot hole {tag} through", loc["through"], "==", 1, BAND_N))
        rows.append(g(f"REQ-05 foot thickness at {tag}", loc["length"], "in", (S["foot_t"] - S["foot_t_tol"], S["foot_t"] + S["foot_t_tol"]), BAND_MM, ("A-03", "A-04")))

    # walls: D-01a, D-01b, D-06a, U-06
    mw = min_wall(carrier)
    rows.append(g("D-01a min_wall", mw, ">=", S["wall_floor"], BAND_MM))
    rows.append(g("D-01b min_wall", mw, ">=", S["wall_struct"], BAND_MM))
    rows.append(g("D-06a min feature", mw, ">=", S["min_feature"], BAND_MM))
    wide = mw.detail.get("wide") if mw.ok else None
    wide_mm = wide.get("measured") if isinstance(wide, dict) else None
    wide_at = wide.get("at") if isinstance(wide, dict) else None
    rows.append(g("U-06 (Soft) min_wall wide", value("min_wall_wide", wide_mm, "mm", at=wide_at), ">=", S["wide_wall"], BAND_MM))
    facts["min_wall_detail"] = {k: mw.detail.get(k) for k in ("wide", "largest_step_mm")} if mw.ok else mw.reason

    # D-03a: the census outside the named exception; the exception reported apart
    b = S["build_dir"]
    n_exc = sum(exception_face(f) for f in all_faces)
    facts["d03a_exception_faces"] = n_exc
    rows.append(g("D-03a named-exception faces found (12 expected)", value("exception_faces", n_exc, "count"), "==", 12, BAND_N))
    oh_rest = overhang_census(solid_of(all_faces, lambda f: not exception_face(f)), build_dir=b,
                              min_deg=S["overhang_min_deg"])
    rows.append(g("D-03a overhang outside the named exception", oh_rest, ">=", S["overhang_min_deg"], BAND_DEG, ("A-13",)))
    facts["d03a_rest"] = oh_rest.to_dict()
    bed_x = env["min_x"].measured
    bed_faces = [f for f in all_faces if face_kind(f) == "plane" and abs(face_center(f)[0] - bed_x) < 1e-3]
    oh_exc = overhang_census(solid_of(all_faces, lambda f: exception_face(f) or any(f.IsSame(x) for x in bed_faces)),
                             build_dir=b, min_deg=S["overhang_min_deg"])
    facts["d03a_exception_least"] = oh_exc.to_dict()
    listing = analytic_downward(carrier, b, bed_x)
    facts["d03a_analytic_downward_faces"] = listing
    rest = [e for e in listing if not e.get("exception") and e.get("least_deg") is not None]
    least = rest[0] if rest else None
    rows.append(g("D-03a analytic least angle outside the exception (corroboration)",
                  value("analytic_overhang_deg", least["least_deg"] if least else 90.0, "deg",
                        at=least["at"] if least else None), ">=", S["overhang_min_deg"], BAND_DEG, ("A-13",)))
    gables = [e for e in listing if e["kind"] == "plane" and not e["exception"] and abs(e["least_deg"] - 45.0) < 0.01]
    facts["d03a_gable_flats_deg"] = [e["least_deg"] for e in gables]
    # D-03b: a bridge is a horizontal downward face (under 1 deg) outside the exception;
    # its span is the largest distance between its vertices (the longest straight line
    # between its carried edges). Inside the exception: the widest bore crown.
    flats = [e for e in rest if e["least_deg"] < 1.0]
    span = max((e["vertex_span_mm"] or 0.0) for e in flats) if flats else 0.0
    worst = max(flats, key=lambda e: e["vertex_span_mm"] or 0.0) if flats else None
    rows.append(g("D-03b bridge span outside the named exception", value("bridge_span", span, "mm",
                  at=worst.get("center") if worst else None, faces=len(flats)), "<=", S["bridge_max"], BAND_MM))
    exc_span = max((bb["diameter"] for bb in (bc.detail.get("bores") or [])
                    if abs(abs(bb["axis_dir"][2]) - 1) < 1e-6 and bb["diameter"] < 10), default=None) if bc.ok else None
    rows.append(g("D-03b named exception crown span", value("crown_span", exc_span, "mm"), "<=", S["exception_bridge_max"], BAND_MM))

    # REQ-04 hub window: innermost material over the whole ray (RV01 F4)
    hub = ray_set(carrier, Z_LEVELS)
    rows.append(g("REQ-04 innermost material r, 36 x 5 rays", hub, ">=", S["hub_r"], BAND_MM, ("A-06",)))
    ctl = radial_extent(carrier, (0, 0, 0), (0, 0, 1), (1, 0, 0), 0, -27.44, side="inner")
    rows.append(g("REQ-04 theta 0 (gable apex)", ctl, "==", E["hub_apex_r"], BAND_MM, ("A-06",)))
    ctl = radial_extent(carrier, (0, 0, 0), (0, 0, 1), (1, 0, 0), 90, -27.44, side="inner")
    rows.append(g("REQ-04 theta 90", ctl, "==", E["hub_side_r"], BAND_MM, ("A-06",)))

    # E-06: four gussets tie plate, wall and foot (one solid, each gusset's full volume)
    for name, (xs, ys, zs) in gusset_boxes(E).items():
        cv = common_volume(carrier, box_between(xs, ys, zs))
        expected = 0.5 * 40.0 * 40.0 * (55.0 - E["gusset_x_in"])    # derivation: legs 40, |x| gusset_x_in .. 55
        rows.append(g(f"E-06 gusset {name} volume", cv, "==", expected, BAND_MM3))
    inner = [f for f in all_faces if face_kind(f) == "plane" and abs(abs(face_center(f)[0]) - E["gusset_x_in"]) < 0.01]
    rows.append(g("E-06 gusset inner faces (one solid)", value("gussets", len(inner) if len(solids) == 1 else None, "count"), "==", 4, BAND_N))

    # U-03 assembly as placed, REQ-08
    if g01 is None or "od_g04_brewing_gasket_support" not in asm_parts:
        for gid in ("U-03a carrier|OD-G01 contact clearance", "U-03a carrier|OD-G01 interference",
                    "U-03a carrier|OD-G04 clearance", "U-03a carrier|OD-G04 interference",
                    "REQ-08 housing to front gussets", "REQ-08 housing to wall"):
            rows.append(Gate(gid, None, "", "", None, None, INCONCLUSIVE, "assembly", (), "no check assembly"))
    else:
        g04 = asm_parts["od_g04_brewing_gasket_support"]
        ac = asm_parts.get("od_c05_carrier")
        facts["assembly_carrier_volume_delta"] = abs(ac.volume - carrier.volume) if ac is not None else None
        facts["validity_g01"] = {k: r.measured for k, r in validity(g01).items()}
        facts["validity_g04"] = {k: r.measured for k, r in validity(g04).items()}
        c1 = clearance(carrier, g01)
        rows.append(g("U-03a carrier|OD-G01 contact clearance", c1, "==", 0.0, BAND_MM, ("A-01",)))
        facts["g01_contact_at"] = c1.at if c1.ok else c1.reason
        it = interference({"od_c05_carrier": carrier, "od_g01_housing": g01, "od_g04": g04})
        rows.append(g("U-03a carrier|OD-G01 interference", it["od_c05_carrier|od_g01_housing"], "<=", 0.0, BAND_MM3, ("A-01",)))
        c4 = clearance(carrier, g04)
        rows.append(g("U-03a carrier|OD-G04 clearance", c4, ">=", S["og04_clearance_min"], BAND_MM, ("A-06",)))
        facts["og04_nearest"] = {"on_carrier": c4.at, "on_g04": c4.detail.get("on_b")} if c4.ok else c4.reason
        rows.append(g("U-03a carrier|OD-G04 interference", it["od_c05_carrier|od_g04"], "<=", 0.0, BAND_MM3, ("A-06",)))
        rows.append(g("U-03 assembly carrier equals part file", value("carrier_volume_delta", facts["assembly_carrier_volume_delta"], "mm3"), "<=", 0.0, BAND_MM3))
        # REQ-08: the carrier off the contact plane, cut by position from the re-imported solid
        below = (S["z_under"], S["z_floor"] + 1.0)
        front = carrier & box_between((-60, 60), (-52.0, 60.0), below)
        wall = carrier & box_between((-60, 60), (-110.0, -52.0), below)
        cf = clearance(g01, front)
        rows.append(g("REQ-08 housing to front gussets", cf, ">=", S["gusset_gap_min"], BAND_MM, ("A-01",)))
        cw = clearance(g01, wall)
        rows.append(g("REQ-08 housing to wall", cw, ">=", S["wall_gap_min"], BAND_MM, ("A-01",)))
        facts["req08_nearest"] = {"gussets": {"on_housing": cf.at, "on_carrier": cf.detail.get("on_b")} if cf.ok else cf.reason,
                                  "wall": {"on_housing": cw.at, "on_carrier": cw.detail.get("on_b")} if cw.ok else cw.reason,
                                  "front_piece_volume": front.volume, "wall_piece_volume": wall.volume}
    rows.append(na("U-03b", "no motion variable (spec section 5 U-03 b)"))

    # U-07 mesh
    if stl is not None and stl.exists():
        sg = mesh_sagitta(carrier_for_mesh(step))
        rows.append(g("U-07 stl_max_sagitta (B-rep re-meshed at the export settings)", sg, "<=", S["stl_tol"], BAND_MM))
        mc = mesh_census(stl)
        facts["stl_census"] = {k: r.measured for k, r in mc.items()}
        mesh = load_mesh(stl)
        facts["stl_bbox"] = [[round(float(x), 4) for x in row] for row in mesh.bounds]
        rows.append(g("U-07 stl bodies", mc["bodies"], "==", 1, BAND_N))
        rows.append(g("U-07 stl naked_edges", mc["naked_edges"], "==", 0, BAND_N))
        rows.append(g("U-07 stl winding", mc["winding"], "==", 1, BAND_N))
        rows.append(g("U-07 angular tolerance used", value("stl_angular_rad", MESH_ANG, "rad"), "<=", S["stl_ang_limit"], 0.00002))
    rows.append(na("U-08", "no threads on this part (spec section 5 U-08)"))
    rows.append(na("D-07", "clearance holes only, no fit bores (spec section 5 D-07)"))
    rows.append(Gate("REQ-09", None, "", "Soft bench: no visible flex", None, None, INCONCLUSIVE, "bench",
                     ("A-11",), "Soft bench gate, not geometric: answered by the first print"))
    mp = mass_properties(carrier, DENSITY)
    facts["mass"] = {k: r.measured for k, r in mp.items()}
    return {"step": step.name, "gates": [dict(r.row(), reason=r.reason) for r in rows], "facts": facts}


MESH_TOL, MESH_ANG = 0.01, 0.20


def carrier_for_mesh(step):
    """The re-imported carrier meshed afresh at the export settings so mesh_sagitta
    reads the triangulation the STL carries."""
    from OCP.BRepMesh import BRepMesh_IncrementalMesh
    shape = read_step(step)
    BRepTools.Clean_s(shape.wrapped)
    BRepMesh_IncrementalMesh(shape.wrapped, MESH_TOL, False, MESH_ANG, True)
    return shape


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", default=str(WS / f"02_STEP_STL/od_c05_carrier_C4_{TAG}.step"))
    ap.add_argument("--assembly", default=str(WS / f"02_STEP_STL/od_c05_assembly_C4_{TAG}.step"))
    ap.add_argument("--stl", default=str(WS / f"02_STEP_STL/od_c05_carrier_C4_{TAG}.stl"))
    ap.add_argument("--expect", default="{}")
    ap.add_argument("--out", default=str(WS / f"01_CAD/check_od_c05_carrier_{TAG}.json"))
    a = ap.parse_args(argv)
    try:
        out = run(Path(a.step), Path(a.assembly) if a.assembly else None,
                  Path(a.stl) if a.stl else None, json.loads(a.expect))
    except Exception as exc:   # noqa: BLE001: a check never passes on an exception
        out = {"step": a.step, "error": f"{type(exc).__name__}: {exc}", "trace": traceback.format_exc(),
               "gates": [{"gate": "ALL", "status": INCONCLUSIVE, "reason": str(exc)}]}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1, default=str))
    bad = [r for r in out["gates"] if r["status"] not in ("PASS", "PASS_ASSUMED", "N/A")]
    for r in out["gates"]:
        print(f"{r['status']:13s} {r['gate']:66s} {r.get('measured')} {r.get('unit', '')} margin {r.get('margin')} {str(r.get('reason', ''))[:90]}")
    print(f"not passing: {len(bad)}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
