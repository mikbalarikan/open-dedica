"""Checks for od_c05_carrier (job 20260930-od-c05-group-head-carrier, spec 1.1 section 5).

Written before the build (PLAYBOOK D3). Every predicate re-imports the exported STEP
files, measures with tools.measure / tools.core, and compares through
tools.result.gate with the GATES.md section 0 band. A raised exception or a missing
value is INCONCLUSIVE, never PASS.

Usage (from the repository root):
  uv run tools/run.py python <ws>/01_CAD/check_od_c05_carrier.py \
      [--step P] [--assembly P] [--stl P] [--expect JSON] [--out JSON]
Defaults are the v01 deliverables of this workspace. --expect overrides the
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
from OCP.BRep import BRep_Builder
from OCP.TopoDS import TopoDS_Shell, TopoDS_Solid

from tools.core import compare_step, mesh_sagitta, read_step, validity
from tools.core.shapes import faces as occ_faces
from tools.core.shapes import solids as occ_solids
from tools.measure import (bore_census, clearance, envelope, feature_census, interference,
                           locate_bore, mass_properties, mesh_census, min_wall, overhang_census,
                           radial_extent)
from tools.measure.features import cylinder as cyl_axis
from tools.measure.sampling import kind as face_kind
from tools.result import INCONCLUSIVE, MEASURED, Gate, Result, gate, inconclusive

WS = Path(__file__).resolve().parents[1]

# ---- band: GATES.md section 0 (L-21) -------------------------------------------------
BAND_MM, BAND_DEG, BAND_MM3, BAND_N = 0.005, 0.001, 0.001, 0

# ---- limits: spec 1.1 section 5 only (D-009) -----------------------------------------
SPEC = {
    "size": (100.0, 225.0, 45.0), "size_tol": 0.1,                         # U-02
    "pos": {"min_x": -50.0, "max_x": 50.0, "min_y": -175.0, "max_y": 50.0,
            "min_z": -69.94, "max_z": -24.94},                             # U-02 position, reported apart
    "og04_clearance_min": 2.0,                                             # U-03
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0,             # D-01a, D-01b, D-06a
    "wide_wall": 2.0,                                                      # U-06 (Soft)
    "bed": (220.0, 220.0, 250.0),                                          # D-02, A-08: x, z on the bed, y tall
    "overhang_min_deg": 45.0,                                              # D-03a
    "bridge_max": 5.0, "exception_bridge_max": 6.5,                        # D-03b and its named exception
    "clearance_hole_min_d": 3.25,                                          # D-04a
    "hole_d": 3.4, "hole_d_tol": 0.1, "hole_xy": 44.0, "hole_offset_max": 0.10,   # REQ-01
    "cb_d": 6.5, "cb_d_tol": 0.1, "cb_depth": 2.0, "cb_depth_tol": 0.1,     # REQ-02
    "z_front": -24.94, "z_rear": -29.94, "face_tol": 0.10,                  # REQ-03
    "hub_r": 30.0,                                                         # REQ-04
    "y_floor": -175.0, "floor_tol": 0.10, "foot_t": 4.0, "foot_t_tol": 0.1, # REQ-05
    "foot_hole_x": 35.0, "foot_hole_z": (-40.0, -60.0),                     # REQ-06
    "keepout_min_z": -70.0,                                                # REQ-07
    "low_c": (0.0, -110.0), "low_r": 25.0,                                 # REQ-08
    "stl_tol": 0.01, "stl_ang_limit": 4 * math.acos(1 - 0.01 / 6.0),       # U-07
}
# U-05 feature census: DESIGN_PLAN section 3 counts (K-1 changes only the convex radius).
CENSUS_EXPECT = {"plane_faces": 20, "cylinder_faces": 16, "cone_faces": 0, "sphere_faces": 0,
                 "torus_faces": 0, "bspline_faces": 0, "other_faces": 0,
                 "concave_cylinders": 14, "convex_cylinders": 2, "bores": 14}
# Positive controls of REQ-04 / REQ-08 (probe checks, derived from the spec geometry).
EXPECT = {"hub_apex_r": 30.0 * math.sqrt(2), "hub_side_r": 30.0,
          "low_apex_r": 25.0 * math.sqrt(2), "low_bottom_r": 25.0}
DENSITY = 1070.0   # kg/m3, spec section 3, A-12 (reported only)
Z_LEVELS = (-29.5, -27.44, -25.4)   # inside the wall z -29.94 .. -24.94
HOLES_Z = [(sx * 44.0, sy * 44.0) for sy in (1, -1) for sx in (1, -1)]
HOLES_Y = [(sx * 35.0, z) for z in (-40.0, -60.0) for sx in (1, -1)]


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
    out = {}
    for child in getattr(asm, "children", ()) or ():
        out[child.label] = child
    return out


def solid_of(shape_occ_faces, keep):
    """A solid built from the chosen faces of a solid, orientation kept: used only to
    run overhang_census with the named-exception faces left out (spec 1.1 D-03a)."""
    builder = BRep_Builder()
    shell = TopoDS_Shell()
    builder.MakeShell(shell)
    for f in shape_occ_faces:
        if keep(f):
            builder.Add(shell, f)
    solid = TopoDS_Solid()
    builder.MakeSolid(solid)
    builder.Add(solid, shell)
    return solid


def exception_face(f) -> bool:
    """The eight horizontal holes and counterbores along Z at (+-44, +-44): cylindrical,
    axis along Z, axis within 0.2 of a hole centre, radius 1.5 .. 3.5 (by position)."""
    if face_kind(f) != "cylinder":
        return False
    origin, direction, radius = cyl_axis(f)
    if abs(abs(direction[2]) - 1.0) > 1e-6 or not (1.5 <= radius <= 3.5):
        return False
    return any(math.hypot(origin[0] - x, origin[1] - y) <= 0.2 for x, y in HOLES_Z)


def ray_set(part, origin, r_max, name):
    """radial_extent at every 10 deg on three levels through the wall over r <= r_max.
    Returns a Result counting rays that found material; INCONCLUSIVE if a ray failed for
    any reason other than 'no material' (the expected reading) or a bound crossing."""
    found, empty, other = [], 0, []
    for z in Z_LEVELS:
        for a in range(0, 360, 10):
            r = radial_extent(part, origin, (0, 0, 1), (1, 0, 0), a, z, side="inner",
                              r_min=0.0, r_max=r_max)
            if r.status == MEASURED:
                found.append((a, z, r.measured))
            elif "no material" in r.reason:
                empty += 1
            elif "crosses the window" in r.reason:
                found.append((a, z, r.reason))
            else:
                other.append((a, z, r.reason))
    if other:
        return inconclusive(name, "count", f"{len(other)} rays unread: {other[0]}")
    return Result(name, len(found), "count", detail={"rays": 36 * len(Z_LEVELS), "no_material": empty,
                                                     "material": found[:5]})


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

    # envelope: U-02, envelope_within_spec, D-02, REQ-03 front, REQ-05 floor, REQ-07
    env = envelope(part)
    for key, nominal in zip(("size_x", "size_y", "size_z"), S["size"]):
        rows.append(g(f"U-02 {key}", env[key], "in", (nominal - S["size_tol"], nominal + S["size_tol"]), BAND_MM))
    for key, nominal in S["pos"].items():
        rows.append(g(f"envelope_within_spec {key}", env[key], "in", (nominal - S["size_tol"], nominal + S["size_tol"]), BAND_MM))
    rows.append(g("D-02 bed x", env["size_x"], "<=", S["bed"][0], BAND_MM, ("A-08",)))
    rows.append(g("D-02 bed z", env["size_z"], "<=", S["bed"][1], BAND_MM, ("A-08",)))
    rows.append(g("D-02 height y", env["size_y"], "<=", S["bed"][2], BAND_MM, ("A-08",)))
    rows.append(g("REQ-03 front face z", env["max_z"], "in", (S["z_front"] - S["face_tol"], S["z_front"] + S["face_tol"]), BAND_MM, ("A-01",)))
    rows.append(g("REQ-05 underside y", env["min_y"], "in", (S["y_floor"] - S["floor_tol"], S["y_floor"] + S["floor_tol"]), BAND_MM, ("A-03", "A-04")))
    rows.append(g("REQ-07 min_z", env["min_z"], ">=", S["keepout_min_z"], BAND_MM, ("A-05",)))
    facts["envelope"] = {k: r.measured for k, r in env.items()}

    # U-04 round trip: the file re-read against its own re-import (named body, volume, faces, valid)
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
    conv = [f for f in occ_faces(carrier) if face_kind(f) == "cylinder" and not exception_face(f)]
    facts["cylinder_radii"] = sorted(round(cyl_axis(f)[2], 4) for f in conv)

    # bores: U-05, D-04a, REQ-01, REQ-02, REQ-03 rear, REQ-06, REQ-05 thickness
    bc = bore_census(carrier)
    facts["bores"] = bc.detail.get("bores") if bc.ok else bc.reason
    asm_parts = {}
    g01_bores = []
    if assembly is not None:
        asm = read_step(assembly)
        asm_parts = label_parts(asm)
        facts["assembly_labels"] = list(asm_parts)
    g01 = asm_parts.get("od_g01_housing")
    if g01 is not None:
        gb = bore_census(g01)
        for x, y in HOLES_Z:
            loc = locate_bore(gb, (x, y, -22.0), (0, 0, 1))
            if loc["offset"].ok and loc["offset"].measured < 1.0:
                s = loc["offset"].detail["start"]
                g01_bores.append((s[0], s[1]))
            else:
                g01_bores.append(None)
        facts["g01_insert_bores"] = g01_bores
    for i, (x, y) in enumerate(HOLES_Z):
        tag = f"({x:+.0f},{y:+.0f})"
        loc = locate_bore(bc, (x, y, S["z_front"] - 1.5), (0, 0, 1))
        rows.append(g(f"U-05/REQ-01 hole {tag} dia", loc["diameter"], "in", (S["hole_d"] - S["hole_d_tol"], S["hole_d"] + S["hole_d_tol"]), BAND_MM, ("A-01",)))
        rows.append(g(f"D-04a hole Z {tag}", loc["diameter"], ">=", S["clearance_hole_min_d"], BAND_MM))
        rows.append(g(f"REQ-01 hole {tag} offset from nominal", loc["offset"], "<=", S["hole_offset_max"], BAND_MM, ("A-01",)))
        rows.append(g(f"REQ-01 hole {tag} through", loc["through"], "==", 1, BAND_N))
        ref = g01_bores[i] if g01_bores else None
        if ref is None:
            r = inconclusive("bore_axis_offset", "mm", "OD-G01 insert bore not located in the check assembly")
        else:
            r = locate_bore(bc, (ref[0], ref[1], S["z_front"] - 1.5), (0, 0, 1))["offset"]
        rows.append(g(f"U-03a/REQ-01 hole {tag} offset from OD-G01 insert", r, "<=", S["hole_offset_max"], BAND_MM, ("A-01",)))
        cb = locate_bore(bc, (x, y, S["z_rear"] + 0.5), (0, 0, 1))
        rows.append(g(f"U-05/REQ-02 cb {tag} dia", cb["diameter"], "in", (S["cb_d"] - S["cb_d_tol"], S["cb_d"] + S["cb_d_tol"]), BAND_MM, ("A-09",)))
        rows.append(g(f"REQ-02 cb {tag} depth", cb["length"], "in", (S["cb_depth"] - S["cb_depth_tol"], S["cb_depth"] + S["cb_depth_tol"]), BAND_MM, ("A-09",)))
        rows.append(g(f"REQ-02 cb {tag} coaxial", cb["offset"], "<=", S["hole_offset_max"], BAND_MM, ("A-09",)))
        start_z = None
        if cb["diameter"].ok:
            ends = [cb["diameter"].detail["start"][2], cb["diameter"].detail["end"][2]]
            start_z = min(ends)
        rows.append(g(f"REQ-03 rear face z (cb {tag} open end)", value("rear_face_z", start_z, "mm", at=(x, y, start_z)), "in",
                      (S["z_rear"] - S["face_tol"], S["z_rear"] + S["face_tol"]), BAND_MM, ("A-01",)))
        tot = (loc["length"].measured + cb["length"].measured) if (loc["length"].ok and cb["length"].ok) else None
        rows.append(g(f"REQ-03 wall through {tag} (hole + cb length)", value("wall_length", tot, "mm"), "in",
                      (5.0 - S["face_tol"], 5.0 + S["face_tol"]), BAND_MM, ("A-01",)))
    for x, z in HOLES_Y:
        tag = f"({x:+.0f}, z {z:.0f})"
        loc = locate_bore(bc, (x, S["y_floor"] + 2.0, z), (0, 1, 0))
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
    all_faces = occ_faces(carrier)
    n_exc = sum(exception_face(f) for f in all_faces)
    facts["d03a_exception_faces"] = n_exc
    oh_rest = overhang_census(solid_of(all_faces, lambda f: not exception_face(f)), build_dir=(0, 1, 0),
                              min_deg=S["overhang_min_deg"])
    rows.append(g("D-03a overhang outside the named exception", oh_rest, ">=", S["overhang_min_deg"], BAND_DEG, ("A-13",)))
    bottom = [f for f in all_faces if face_kind(f) == "plane" and abs(_face_center(f)[1] - S["y_floor"]) < 1e-3]
    oh_exc = overhang_census(solid_of(all_faces, lambda f: exception_face(f) or any(f.IsSame(b) for b in bottom)),
                             build_dir=(0, 1, 0), min_deg=S["overhang_min_deg"])
    facts["d03a_exception_least_deg"] = oh_exc.to_dict()
    rows.append(g("D-03a exception faces counted (8 expected)", value("exception_faces", n_exc, "count"), ">=", 8, BAND_N))
    # D-03b: outside the exception, a bridge is a downward face under 45 deg; none if D-03a passes.
    # overhang_census's own count of grid samples under 45 deg (detail["below_min_deg"]) is read
    # whether or not the least angle settled: zero samples under 45 deg outside the exception
    # means no horizontal span, so the widest bridge there is 0.
    below = oh_rest.detail.get("below_min_deg")
    facts["d03a_rest"] = oh_rest.to_dict()
    bridges = 0.0 if below == 0 else None
    rows.append(g("D-03b bridge span outside the named exception", value("bridge_span", bridges, "mm",
                  below_min_deg=below), "<=", S["bridge_max"], BAND_MM))
    # diagnostics (not gates): the planar downward faces alone, and the curved ones alone
    facts["d03a_planes_only"] = overhang_census(
        solid_of(all_faces, lambda f: face_kind(f) == "plane"), build_dir=(0, 1, 0),
        min_deg=S["overhang_min_deg"]).to_dict()
    facts["d03a_window_arcs_only"] = overhang_census(
        solid_of(all_faces, lambda f: (face_kind(f) == "cylinder" and not exception_face(f))
                 or any(f.IsSame(b) for b in bottom)), build_dir=(0, 1, 0),
        min_deg=S["overhang_min_deg"]).to_dict()
    exc_span = max((b["diameter"] for b in (bc.detail.get("bores") or [])
                    if abs(abs(b["axis_dir"][2]) - 1) < 1e-6 and b["diameter"] < 10) , default=None) if bc.ok else None
    rows.append(g("D-03b named exception crown span", value("crown_span", exc_span, "mm"), "<=", S["exception_bridge_max"], BAND_MM))

    # REQ-04 hub window and REQ-08 lower window
    hub = ray_set(carrier, (0, 0, 0), S["hub_r"], "hub_rays_with_material")
    rows.append(g("REQ-04 rays with material r<=30 (108 rays)", hub, "==", 0, BAND_N, ("A-06",)))
    ctl = radial_extent(carrier, (0, 0, 0), (0, 0, 1), (1, 0, 0), 90, -27.44, side="inner")
    rows.append(g("REQ-04 control theta 90 apex", ctl, "==", E["hub_apex_r"], BAND_MM))
    ctl = radial_extent(carrier, (0, 0, 0), (0, 0, 1), (1, 0, 0), 0, -27.44, side="inner")
    rows.append(g("REQ-04 control theta 0", ctl, "==", E["hub_side_r"], BAND_MM))
    lc = (S["low_c"][0], S["low_c"][1], 0.0)
    low = ray_set(carrier, lc, S["low_r"], "low_rays_with_material")
    rows.append(g("REQ-08 rays with material r<=25 (108 rays)", low, "==", 0, BAND_N, ("A-07",)))
    ctl = radial_extent(carrier, lc, (0, 0, 1), (1, 0, 0), 90, -27.44, side="inner")
    rows.append(g("REQ-08 control theta 90 apex", ctl, "==", E["low_apex_r"], BAND_MM))
    ctl = radial_extent(carrier, lc, (0, 0, 1), (1, 0, 0), 270, -27.44, side="inner")
    rows.append(g("REQ-08 control theta 270", ctl, "==", E["low_bottom_r"], BAND_MM))

    # E-06: two gussets tie the wall to the foot (inner faces x = +-46, one solid)
    gus = [f for f in all_faces if face_kind(f) == "plane" and abs(abs(_face_center(f)[0]) - 46.0) < 0.01]
    rows.append(g("E-06 gusset inner faces (one solid)", value("gussets", len(gus) if len(solids) == 1 else None, "count"), "==", 2, BAND_N))

    # U-03 assembly as placed
    if g01 is None or "od_g04_brewing_gasket_support" not in asm_parts:
        for gid in ("U-03a carrier|OD-G01 clearance", "U-03a carrier|OD-G01 interference",
                    "U-03a carrier|OD-G04 clearance", "U-03a carrier|OD-G04 interference"):
            rows.append(Gate(gid, None, "", "", None, None, INCONCLUSIVE, "assembly", (), "no check assembly"))
    else:
        g04 = asm_parts["od_g04_brewing_gasket_support"]
        ac = asm_parts.get("od_c05_carrier")
        facts["assembly_carrier_volume_delta"] = abs(ac.volume - carrier.volume) if ac is not None else None
        vg1, vg4 = validity(g01), validity(g04)
        facts["validity_g01"] = {k: r.measured for k, r in vg1.items()}
        facts["validity_g04"] = {k: r.measured for k, r in vg4.items()}
        c1 = clearance(carrier, g01)
        rows.append(g("U-03a carrier|OD-G01 contact clearance", c1, "==", 0.0, BAND_MM, ("A-01",)))
        it = interference({"od_c05_carrier": carrier, "od_g01_housing": g01, "od_g04": g04})
        rows.append(g("U-03a carrier|OD-G01 interference", it["od_c05_carrier|od_g01_housing"], "<=", 0.0, BAND_MM3, ("A-01",)))
        c4 = clearance(carrier, g04)
        rows.append(g("U-03a carrier|OD-G04 clearance", c4, ">=", S["og04_clearance_min"], BAND_MM, ("A-06",)))
        facts["og04_nearest"] = {"on_carrier": c4.at, "on_g04": c4.detail.get("on_b")} if c4.ok else c4.reason
        rows.append(g("U-03a carrier|OD-G04 interference", it["od_c05_carrier|od_g04"], "<=", 0.0, BAND_MM3, ("A-06",)))
        rows.append(g("U-03 assembly carrier equals part file", value("carrier_volume_delta", facts["assembly_carrier_volume_delta"], "mm3"), "<=", 0.0, BAND_MM3))
    rows.append(na("U-03b", "no motion variable (spec section 5 U-03 b)"))

    # U-07 mesh
    if stl is not None and stl.exists():
        sg = mesh_sagitta(carrier_for_mesh(step))
        rows.append(g("U-07 stl_max_sagitta (B-rep re-meshed at the export settings)", sg, "<=", S["stl_tol"], BAND_MM))
        mc = mesh_census(stl)
        facts["stl_census"] = {k: r.measured for k, r in mc.items()}
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
    """The re-imported carrier meshed afresh at the export settings (write_stl's own
    mesher settings) so mesh_sagitta reads the triangulation the STL carries."""
    from OCP.BRepMesh import BRepMesh_IncrementalMesh
    from OCP.BRepTools import BRepTools
    shape = read_step(step)
    BRepTools.Clean_s(shape.wrapped)
    BRepMesh_IncrementalMesh(shape.wrapped, MESH_TOL, False, MESH_ANG, True)
    return shape


def _face_center(f):
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    p = GProp_GProps()
    BRepGProp.SurfaceProperties_s(f, p)
    c = p.CentreOfMass()
    return (c.X(), c.Y(), c.Z())


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", default=str(WS / "02_STEP_STL/od_c05_carrier_C1_v01.step"))
    ap.add_argument("--assembly", default=str(WS / "02_STEP_STL/od_c05_assembly_C1_v01.step"))
    ap.add_argument("--stl", default=str(WS / "02_STEP_STL/od_c05_carrier_C1_v01.stl"))
    ap.add_argument("--expect", default="{}")
    ap.add_argument("--out", default=str(WS / "01_CAD/check_od_c05_carrier_v01.json"))
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
        print(f"{r['status']:13s} {r['gate']:60s} {r.get('measured')} {r.get('unit', '')} margin {r.get('margin')} {r.get('reason', '')[:80]}")
    print(f"not passing: {len(bad)}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
