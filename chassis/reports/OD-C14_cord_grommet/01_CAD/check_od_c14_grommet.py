"""Checks for od_c14_grommet_half, concept C1 (job 20261002-od-c14-cord-grommet).

Written before the build (D3). One predicate group per gate row of DESIGN_SPEC 1.1 §5,
plus exactly_one_solid, feature_census and envelope_within_spec. Every value is measured
on the B-rep of the re-imported STEP files (the half and the check assembly), with
tools/measure, and compared by tools.result.gate with the GATES §0 band of its unit.
A raised exception or a missing value gives INCONCLUSIVE.

Limits are spec §5 values only (SPEC below). The build module is imported for two
things only: the parameters a run was built with (to rebuild the in-memory solid for the
U-04 round trip) and the STL settings the export used.

Usage (from the repo root, through tools/run.py):
  python 01_CAD/check_od_c14_grommet.py                        nominal, 02_STEP_STL files
  python 01_CAD/check_od_c14_grommet.py --run <sweep_v01/run>  a sweep run folder
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
sys.path.insert(0, str(HERE))

import build123d as bd                                   # noqa: E402
from build123d import Box, Compound, GeomType, Pos       # noqa: E402

from tools.core import compare_step, read_step, validity, write_stl            # noqa: E402
from tools.measure import (bore_census, clearance, envelope, feature_census,   # noqa: E402
                           flat_ceiling_spans, interference, locate_bore, mesh_census,
                           mesh_deviation, min_wall, min_wall_mesh, min_wall_wide,
                           overhang_census, radial_extent, radial_profile)
from tools.measure.features import cylinder                                     # noqa: E402
from OCP.BRepAdaptor import BRepAdaptor_Surface                                  # noqa: E402
from tools.result import INCONCLUSIVE, Result, gate, inconclusive               # noqa: E402

import build_od_c14_grommet as build                                            # noqa: E402

# ---- spec 1.1 §5 limits (the only thresholds in this file) -------------------------
SPEC = {
    "envelope": {"size": (20.0, 9.6, 13.0), "tol": 0.1,
                 "pos": {"x": (85.0, 105.0), "y": (30.4, 40.0), "z": (-304.0, -291.0)}},
    "contact": 0.0,                      # designed contacts, clearance = 0
    "neck_to_hole_min": 0.30,            # U-03 a/b, D-04d
    "axial_play": (0.15, 0.25),          # 0.20 ± 0.05, tie and head box to OD-C11 inner face
    "halves_gap": (0.75, 0.85),          # 0.80 ± 0.05
    "to_c11_features_min": 0.5,          # gussets and floor flange
    "to_c01_min": 10.0,
    "tie_outer_d_min": 12.0,             # exceeds the hole's Ø12.0
    "squeeze": (0.35, 0.45),             # 0.40 ± 0.05
    "path": {"start": -20.0, "step": 2.0},
    "interference_max": 0.0,
    "min_wall_d01a": 0.8, "min_wall_d01b": 1.6, "min_wall_d06a": 1.0, "min_wall_u06": 1.6,
    "build_volume": (220.0, 220.0, 250.0),     # A-07
    "overhang_min_deg": 45.0,
    "bridge_max": 5.0,
    "stl_tol": 0.01,
    "profile": {   # REQ-01: (radius nominal, radius tol) and z bands (machine z)
        "flange": (10.0, 0.05, (-304.0, -302.0)),
        "neck": (5.65, 0.025, (-302.0, -298.8)),
        "groove": (5.15, 0.025, (-298.8, -293.6)),
        "collar": (5.65, 0.025, (-292.734, -291.0)),
    },
    "z_tol": 0.1,
    "flank_deg": (59.0, 61.0),
    "coax_max": 0.05,
    "bore_r": (3.45, 3.55),
    "split_y": (30.38, 30.42),
    "chamfer_in": {"radial": (0.4, 0.6), "axial": (0.4, 0.6)},
    "chamfer_out": {"radial": (0.19, 0.39), "axial": (0.4, 0.6)},
    "groove_w": (5.1, 5.3),
    "census": {"plane": 6, "cylinder": 5, "cone": 3, "sphere": 0, "torus": 0, "bspline": 0,
               "other": 0, "concave_cylinders": 1, "convex_cylinders": 4, "bores": 0},
}
BAND = {"mm": 0.005, "deg": 0.001, "mm3": 0.001, "count": 0, "bool": 0, "rad": 0.00002}

LABELS = ("od_c11_back_panel", "od_c01_base_frame", "half_upper", "half_lower",
          "cord_envelope", "tie_envelope", "tie_head_box")

ROWS: list[dict] = []


def put(gate_id, result, op, limit, *, assumes=(), required=None, note=""):
    g = gate(gate_id, result, op, limit, band=BAND.get(result.unit, 0), assumes=assumes,
             required=required)
    row = g.row()
    row["reason"] = g.reason
    row["note"] = note
    ROWS.append(row)
    return g


def put_inconclusive(gate_id, unit, reason, note=""):
    ROWS.append({"gate": gate_id, "measured": None, "unit": unit, "required": "", "margin": None,
                 "at": None, "status": INCONCLUSIVE, "method": "", "assumes": [], "reason": reason,
                 "note": note})


def guarded(gate_id, unit="mm"):
    def wrap(fn):
        def inner(*a, **k):
            try:
                return fn(*a, **k)
            except Exception as exc:                     # noqa: BLE001: INCONCLUSIVE, never a pass
                put_inconclusive(gate_id, unit, f"{type(exc).__name__}: {exc}",
                                 note=traceback.format_exc(limit=2)[-300:])
        return inner
    return wrap


def value(name, x, unit, at=None, **detail):
    if x is None or not math.isfinite(x):
        return inconclusive(name, unit, "no value")
    return Result(name, float(x), unit, at=at, detail=detail)


# ---- helpers: selection by type and measured geometry, clips ----------------------
def by_label(shape, label):
    found = []

    def walk(node):
        if getattr(node, "label", "") == label and node.solids():
            found.append(node)
            return
        for child in getattr(node, "children", ()) or ():
            walk(child)
    walk(shape)
    if len(found) != 1:
        raise ValueError(f"label {label!r} found {len(found)} times in the assembly")
    solids = found[0].solids()
    return solids[0] if len(solids) == 1 else Compound(solids)


def clip(shape, zlo=-1e4, zhi=1e4, ylo=-1e4, yhi=1e4, xlo=-1e4, xhi=1e4):
    box = Pos((xlo + xhi) / 2, (ylo + yhi) / 2, (zlo + zhi) / 2) * Box(xhi - xlo, yhi - ylo, zhi - zlo)
    out = shape & box
    if not out.solids():
        raise ValueError("the clip left no solid")
    return out


def planar_faces(shape, normal_axis):
    """Planar faces whose normal runs along machine axis `normal_axis` (0, 1, 2)."""
    out = []
    for f in shape.faces():
        if f.geom_type != GeomType.PLANE:
            continue
        n = f.normal_at()
        comp = (n.X, n.Y, n.Z)
        if abs(abs(comp[normal_axis]) - 1.0) < 1e-6:
            out.append(f)
    return out


def faces_of(shape, kind):
    return [f for f in shape.faces() if f.geom_type == kind]


def env(shape):
    e = envelope(shape)
    for k, r in e.items():
        if not r.ok:
            raise ValueError(f"envelope {k} INCONCLUSIVE: {r.reason}")
    return {k: r.measured for k, r in e.items()}


# ---- the predicates ---------------------------------------------------------------
def run(half_step: Path, asm_step: Path, stl: Path, params: dict, out_dir: Path, fast: bool):
    c11_in = read_step(WS / "00_Spec/inputs/OD-C11_back_panel.step")
    hole = locate_bore(bore_census(c11_in), (95.0, 30.0, -300.5), (0, 0, 1))
    for k in ("diameter", "offset"):
        if not hole[k].ok:
            raise RuntimeError(f"the OD-C11 hole cannot be located: {hole[k].reason}")
    start = hole["diameter"].detail["start"]
    axis_o = (start[0], start[1], start[2])          # wall outer face on the hole axis
    hole_r = hole["diameter"].measured / 2.0
    zc = lambda z_machine: z_machine - axis_o[2]     # machine z -> z along the axis from axis_o
    half = read_step(half_step)

    # exactly_one_solid, U-01
    v = validity(half)
    put("exactly_one_solid", v["solid_count"], "==", 1)
    put("U-01.solid_count", v["solid_count"], "==", 1)
    put("U-01.brep_valid", v["brep_valid"], "==", 1)
    put("U-01.naked_edges", v["naked_edges"], "==", 0)
    hs = half.solids()
    if len(hs) != 1:
        raise RuntimeError("not exactly one solid: the remaining checks have no part to measure")
    half = hs[0]

    # U-02 / envelope_within_spec / D-02
    e = env(half)
    size_spec, tol = SPEC["envelope"]["size"], SPEC["envelope"]["tol"]
    for i, a in enumerate("xyz"):
        r = value(f"envelope_size_{a}", e[f"size_{a}"], "mm")
        put(f"U-02.size_{a}", r, "in", (size_spec[i] - tol, size_spec[i] + tol))
        put(f"envelope_within_spec.size_{a}", r, "in", (size_spec[i] - tol, size_spec[i] + tol))
        lo, hi = SPEC["envelope"]["pos"][a]
        ROWS.append({"gate": f"envelope_within_spec.position_{a}", "measured": [e[f"min_{a}"], e[f"max_{a}"]],
                     "unit": "mm", "required": f"reported against {lo} … {hi}",
                     "margin": None, "at": None, "status": "REPORTED", "method": "envelope", "assumes": [],
                     "reason": "", "note": f"offsets {e[f'min_{a}'] - lo:+.4f} / {e[f'max_{a}'] - hi:+.4f}"})
        put(f"D-02.size_{a}", r, "<=", SPEC["build_volume"][i], assumes=("A-07",))

    # U-04 round trip: rebuild in memory with the run's parameters, compare with the file
    built = build.build_half(params, build.hole_frame(c11_in))
    rt = compare_step(built, half_step)
    put("U-04.schema", rt["schema"], "==", 1)
    put("U-04.solids", rt["solids"], "==", 1)
    put("U-04.volume_delta", rt["volume_delta"], "<=", 0.0)
    put("U-04.faces_delta", rt["faces_delta"], "==", 0)
    put("U-04.labels", rt["labels"], "==", 1)
    put("U-04.valid_after", rt["valid_after"], "==", 1)

    # U-05 / feature_census / J-06
    census = feature_census(half)
    for k, n in SPEC["census"].items():
        key = k if k in ("concave_cylinders", "convex_cylinders", "bores") else f"{k}_faces"
        put(f"U-05.{key}", census[key], "==", n)
        put(f"feature_census.{key}", census[key], "==", n)
    bc = bore_census(half)
    helical = (census["bspline_faces"].measured + census["other_faces"].measured
               if census["bspline_faces"].ok and census["other_faces"].ok else None)
    put("J-06.threaded_or_helical_faces", value("helical_faces", helical, "count"), "==", 0)
    put("J-06.bores", bc, "==", 0)

    profile_and_bore(half, axis_o, zc, hole_r)
    walls_and_print(half)
    mesh(half, stl, params, out_dir)
    assembly(half, asm_step, axis_o, zc, hole_r, fast)


@guarded("REQ-01")
def profile_and_bore(half, axis_o, zc, hole_r):
    ax = ((axis_o[0], axis_o[1], axis_o[2]), (0, 0, 1), (1, 0, 0))
    angles = [10.0 + 10.0 * i for i in range(17)]        # 10° … 170°, inside the half's arc
    for name, (r_nom, r_tol, (z0, z1)) in SPEC["profile"].items():
        prof = radial_profile(half, *ax, angles, (zc(z0), zc(z1)), margin=0, z_step=0.2)
        put(f"REQ-01.{name}_r_max", prof["max"], "in", (r_nom - r_tol, r_nom + r_tol), assumes=("A-01",))
        put(f"REQ-01.{name}_r_min", prof["min"], "in", (r_nom - r_tol, r_nom + r_tol), assumes=("A-01",))
        if prof["max"].ok and prof["min"].ok:
            spread = prof["max"].measured - prof["min"].measured
            put(f"REQ-01.{name}_radial_spread", value("radial_spread", spread, "mm"), "<=",
                SPEC["coax_max"], assumes=("A-01",))
        if name in ("neck", "collar") and prof["max"].ok:
            put(f"D-04d.{name}_radial_gap", value("hole_r_minus_r_max", hole_r - prof["max"].measured, "mm",
                                                  at=prof["max"].at), ">=", SPEC["neck_to_hole_min"],
                assumes=("A-01",))
    # coaxiality: every cylinder's and cone's axis against the cord axis (the B-rep surface's own axis)
    worst, tilt = 0.0, 0.0
    for f in faces_of(half, GeomType.CYLINDER):
        o, d, _ = cylinder(f.wrapped)
        worst = max(worst, math.hypot(o[0] - axis_o[0], o[1] - axis_o[1]))
        tilt = max(tilt, math.degrees(math.acos(min(1.0, abs(float(d[2]))))))
    for f in faces_of(half, GeomType.CONE):
        a = BRepAdaptor_Surface(f.wrapped).Cone().Axis()
        o, d = a.Location(), a.Direction()
        worst = max(worst, math.hypot(o.X() - axis_o[0], o.Y() - axis_o[1]))
        tilt = max(tilt, math.degrees(math.acos(min(1.0, abs(d.Z())))))
    put("REQ-01.coaxial_offset", value("cylinder_axis_offset", worst, "mm"), "<=", SPEC["coax_max"],
        assumes=("A-01",), note=f"largest axis tilt off Z {tilt:.2e} deg")
    # z positions: planar faces square to Z, and the flank cone
    zf = sorted({round(env(f)["min_z"], 6) for f in planar_faces(half, 2)})
    e = env(half)
    cones = sorted(faces_of(half, GeomType.CONE), key=lambda f: env(f)["min_z"])
    if len(cones) != 3:
        raise ValueError(f"{len(cones)} conical faces, the plan has 3")
    ch_out, flank, ch_in = cones
    fe = env(flank)
    targets = {"flange_bottom": (e["min_z"], -304.0), "collar_top": (e["max_z"], -291.0),
               "flank_start": (fe["min_z"], -293.6), "flank_end": (fe["max_z"], -292.734)}
    for nom, label in ((-302.0, "flange_top"), (-298.8, "neck_end")):
        near = min(zf, key=lambda z: abs(z - nom))
        targets[label] = (near, nom)
    for label, (meas, nom) in targets.items():
        put(f"REQ-01.z_{label}", value(f"z_{label}", meas, "mm"), "in", (nom - SPEC["z_tol"], nom + SPEC["z_tol"]),
            assumes=("A-01",))
    # flank angle from two radial readings across it
    za, zb = fe["min_z"] + 0.2 * fe["size_z"], fe["min_z"] + 0.8 * fe["size_z"]
    ra = radial_extent(half, *ax, 90.0, zc(za))
    rb = radial_extent(half, *ax, 90.0, zc(zb))
    ang = (math.degrees(math.atan2(zb - za, rb.measured - ra.measured)) if ra.ok and rb.ok else None)
    put("REQ-01.flank_deg", value("flank_from_horizontal", ang, "deg"), "in", SPEC["flank_deg"],
        assumes=("A-01",))
    put("D-03a.flank_deg_corroboration", value("flank_from_horizontal", ang, "deg"), ">=",
        SPEC["overhang_min_deg"], assumes=("A-06",))

    # REQ-02: bore radius, split face, chamfers
    for ang_deg in (20.0, 90.0, 160.0):
        for z_m in (-303.0, -296.2, -291.8):
            r = radial_extent(half, *ax, ang_deg, zc(z_m), side="inner")
            put(f"REQ-02.bore_r_{int(ang_deg)}deg_z{z_m}", r, "in", SPEC["bore_r"], assumes=("A-02", "A-05"))
    split = [f for f in planar_faces(half, 1)]
    put("REQ-02.split_faces", value("split_faces", len(split), "count"), "==", 2,
        note="one plane carried by two faces, either side of the bore (spec 1.1 Q3)")
    ys = [env(f) for f in split]
    put("REQ-02.split_y_min", value("split_y_min", min(y["min_y"] for y in ys), "mm"), "in", SPEC["split_y"],
        assumes=("A-05",))
    put("REQ-02.split_y_max", value("split_y_max", max(y["max_y"] for y in ys), "mm"), "in", SPEC["split_y"],
        assumes=("A-05",))
    bore_r = radial_extent(half, *ax, 90.0, zc(-296.2), side="inner").measured
    for label, face in (("in", ch_in), ("out", ch_out)):
        ce = env(face)
        radial = (ce["max_y"] - axis_o[1]) - bore_r
        put(f"REQ-02.chamfer_{label}_radial", value("chamfer_radial", radial, "mm"), "in",
            SPEC[f"chamfer_{label}"]["radial"], assumes=("A-02",))
        put(f"REQ-02.chamfer_{label}_axial", value("chamfer_axial", ce["size_z"], "mm"), "in",
            SPEC[f"chamfer_{label}"]["axial"], assumes=("A-02",))
    # REQ-04 groove floor width: the cylinder of the groove radius
    groove = [f for f in faces_of(half, GeomType.CYLINDER)
              if abs(cylinder(f.wrapped)[2] - SPEC["profile"]["groove"][0]) < 0.2]
    if len(groove) != 1:
        raise ValueError(f"{len(groove)} groove-floor faces")
    put("REQ-04.groove_width", value("groove_floor_width", env(groove[0])["size_z"], "mm"), "in",
        SPEC["groove_w"], assumes=("A-04",))


@guarded("D-01")
def walls_and_print(half):
    mw = min_wall(half)
    put("D-01a", mw, ">=", SPEC["min_wall_d01a"])
    put("D-01b", mw, ">=", SPEC["min_wall_d01b"], assumes=("A-03",))
    put("D-06a", mw, ">=", SPEC["min_wall_d06a"])
    wide = mw.detail.get("wide") if mw.ok else None
    r = (Result("min_wall_wide", wide["measured"], "mm", at=wide.get("at")) if isinstance(wide, dict)
         and wide.get("measured") is not None else inconclusive("min_wall_wide", "mm", "no wide reading"))
    put("U-06 (Soft)", r, ">=", SPEC["min_wall_u06"])
    put("D-03a", overhang_census(half, build_dir=(0, 0, 1), min_deg=SPEC["overhang_min_deg"]), ">=",
        SPEC["overhang_min_deg"], assumes=("A-06",))
    put("D-03b (corroboration)", flat_ceiling_spans(half, build_dir=(0, 0, 1), max_span=SPEC["bridge_max"]),
        "<=", SPEC["bridge_max"], assumes=("A-06",), note="the gate is the reviewer's, from sections")


@guarded("U-07")
def mesh(half, stl, params, out_dir):
    tol, ang = params["stl_tol"], params["stl_ang"]
    radii = [cylinder(f.wrapped)[2] for f in faces_of(half, GeomType.CYLINDER)]
    r_max = max(radii)
    limit = 4.0 * math.acos(1.0 - SPEC["stl_tol"] / r_max)
    put("U-07.tolerance", value("stl_tolerance", tol, "mm"), "<=", SPEC["stl_tol"])
    put("U-07.angular", value("stl_angular_tolerance", ang, "rad"), "<=", limit,
        required=f"<= 4·acos(1 − 0.01/{r_max:.3f}) = {limit:.4f}")
    remesh = write_stl(half, out_dir / "remesh_of_reimported_step.stl", tolerance=tol, angular_tolerance=ang)
    put("U-07.stl_max_sagitta", remesh.checks["max_sagitta"], "<=", SPEC["stl_tol"])
    mc = mesh_census(stl)
    ROWS.append({"gate": "U-07.delivered_stl (corroboration)", "measured": {k: r.measured for k, r in mc.items()},
                 "unit": "", "required": "bodies 1, naked 0, winding 1, volume > 0", "margin": None, "at": None,
                 "status": ("PASS" if mc["bodies"].measured == 1 and mc["naked_edges"].measured == 0 and
                            mc["winding"].measured == 1 and mc["volume"].ok and mc["volume"].measured > 0
                            else "FAIL"), "method": "mesh_census", "assumes": [], "reason": "",
                 "note": f"remesh triangles {remesh.detail['triangles']}"})
    put("U-07.delivered_stl_deviation (corroboration)", mesh_deviation(stl, half), "<=", SPEC["stl_tol"] + 0.001)
    mwm = min_wall_mesh(stl)
    ROWS.append({"gate": "D-01 mesh corroboration", "measured": mwm.measured, "unit": "mm", "required": "",
                 "margin": None, "at": mwm.at, "status": "REPORTED" if mwm.ok else INCONCLUSIVE,
                 "method": "min_wall_mesh", "assumes": [], "reason": mwm.reason, "note": ""})


@guarded("U-03")
def assembly(half, asm_step, axis_o, zc, hole_r, fast):
    asm = read_step(asm_step)
    parts = {k: by_label(asm, k) for k in LABELS}
    av = [validity(parts[k])["solid_count"].measured for k in LABELS]
    put("U-03.assembly_parts", value("assembly_solids", sum(av), "count"), "==", len(LABELS),
        note="one solid per label: " + ", ".join(LABELS))
    up, lo = parts["half_upper"], parts["half_lower"]
    # the assembly halves are the half file, and the lower one is it turned 180° about the axis
    put("REQ-03.upper_equals_half_volume", value("volume_delta", abs(up.volume - half.volume), "mm3"), "<=", 0.0)
    turned = half.rotate(bd.Axis(axis_o, (0, 0, 1)), 180)
    put("REQ-03.lower_is_half_turned_180", interference({"a": turned, "b": lo})["a|b"], "in",
        (half.volume - 0.001, half.volume + 0.001), required="common volume = the half's volume")
    c11, c01 = parts["od_c11_back_panel"], parts["od_c01_base_frame"]
    cord, tie, head = parts["cord_envelope"], parts["tie_envelope"], parts["tie_head_box"]
    wall_outer, wall_inner = axis_o[2], axis_o[2] + 3.0
    c11_feat = clip(c11, zlo=wall_inner + 0.01)              # OD-C11 less its wall: flange, gussets
    halves = {"upper": up, "lower": lo}

    # (a) open pose
    for n, h in halves.items():
        flange_zone = clip(h, zhi=wall_outer + 0.1)
        put(f"U-03a.flange_face_on_c11_outer_face[{n}]", clearance(flange_zone, c11), "==", 0.0)
        rest = clip(h, zlo=wall_outer + 0.1)
        g = put(f"U-03a.half_to_c11[{n}]", clearance(rest, c11), ">=", SPEC["neck_to_hole_min"], assumes=("A-01",))
        put(f"D-04d.neck_to_hole_open[{n}]", clearance(rest, c11), ">=", SPEC["neck_to_hole_min"], assumes=("A-01",))
        put(f"U-03a.bore_on_cord[{n}]", clearance(h, cord), "==", 0.0, assumes=("A-02",))
        put(f"U-03a.tie_on_groove_floor[{n}]", clearance(h, tie), "==", 0.0, assumes=("A-04",))
        put(f"U-03a.half_to_c11_features[{n}]", clearance(h, c11_feat), ">=", SPEC["to_c11_features_min"])
        put(f"U-03a.half_to_c01[{n}]", clearance(h, c01), ">=", SPEC["to_c01_min"])
    put("U-03a.halves_gap", clearance(up, lo), "in", SPEC["halves_gap"], assumes=("A-05",))
    put("U-03a.tie_to_c11_inner_face", clearance(tie, c11), "in", SPEC["axial_play"], assumes=("A-04",))
    put("U-03a.head_to_c11_inner_face", clearance(head, c11), "in", SPEC["axial_play"], assumes=("A-04",))
    for n, s in (("tie", tie), ("head", head)):
        put(f"U-03a.{n}_to_c11_features", clearance(s, c11_feat), ">=", SPEC["to_c11_features_min"],
            assumes=("A-04",))
        put(f"U-03a.{n}_to_c01", clearance(s, c01), ">=", SPEC["to_c01_min"], assumes=("A-04",))
    put("REQ-04.head_to_c11_features", clearance(head, c11_feat), ">=", SPEC["to_c11_features_min"],
        assumes=("A-04",))
    te = env(tie)
    tie_od = value("tie_outer_d", te["size_x"], "mm")
    put("U-03a.tie_overlaps_hole_rim", tie_od, ">=", SPEC["tie_outer_d_min"], assumes=("A-04",))
    put("REQ-04.tie_outer_d", tie_od, ">=", SPEC["tie_outer_d_min"], assumes=("A-04",))
    named = {k: parts[k] for k in LABELS}
    worst, where = 0.0, None
    for pair, r in interference(named).items():
        if not r.ok:
            put_inconclusive(f"U-03a.interference[{pair}]", "mm3", r.reason)
            continue
        if r.measured > worst or where is None:
            worst, where = max(worst, r.measured), pair if r.measured >= worst else where
        put(f"U-03a.interference[{pair}]", r, "<=", SPEC["interference_max"])

    # (b) closed pose: each half 0.4 toward the axis along Y
    shift = {}
    for n, h in halves.items():
        sign = -1.0 if h.center().Y > axis_o[1] else 1.0
        shift[n] = h.moved(bd.Location((0, sign * 0.4, 0)))
    put("U-03b.halves_touch", clearance(shift["upper"], shift["lower"]), "==", 0.0, assumes=("A-05",))
    put("U-03b.halves_interference", interference({"u": shift["upper"], "l": shift["lower"]})["u|l"], "<=",
        SPEC["interference_max"], assumes=("A-05",))
    ax = ((axis_o[0], axis_o[1], axis_o[2]), (0, 0, 1), (1, 0, 0))
    for n, h in shift.items():
        put(f"U-03b.half_to_c11[{n}]", clearance(clip(h, zlo=wall_outer + 0.1), c11), ">=",
            SPEC["neck_to_hole_min"], assumes=("A-01",))
        put(f"U-03b.half_c11_interference[{n}]", interference({"h": h, "c": c11})["h|c"], "<=",
            SPEC["interference_max"])
        angle = 90.0 if n == "upper" else 270.0
        for z_m in (-301.0, -296.2, -291.8):
            r = radial_extent(h, *ax, angle, zc(z_m), side="inner")
            sq = value("squeeze", 3.5 - r.measured if r.ok else None, "mm", at=r.at)
            put(f"U-03b.squeeze[{n}, z {z_m}]", sq, "in", SPEC["squeeze"], assumes=("A-02", "A-05"),
                note="cord envelope Ø7.0 less the closed half-bore's inner radius")
    pair = env(Compound([shift["upper"], shift["lower"]]))
    put("REQ-03.closed_pair_size_x", value("pair_size_x", pair["size_x"], "mm"), "in", (19.9, 20.1))
    put("REQ-03.closed_pair_size_y", value("pair_size_y", pair["size_y"], "mm"), "in", (19.1, 19.3))
    put("REQ-03.closed_pair_size_z", value("pair_size_z", pair["size_z"], "mm"), "in", (12.9, 13.1))

    # (c) assembly path: both halves at the open pose from 20.0 outside to the seat, step 2.0
    path_c11 = clip(c11, xlo=70, xhi=120, ylo=5, yhi=55, zlo=-330, zhi=-280)   # holds every pose with margin
    steps = []
    d = SPEC["path"]["start"]
    while d <= 1e-9:
        steps.append(round(d, 6))
        d += SPEC["path"]["step"]
    worst_i, worst_at, min_cl = 0.0, None, (math.inf, None)
    for d in steps:
        for n, h in halves.items():
            moved = h.moved(bd.Location((0, 0, d)))
            for other, solid in (("c11", path_c11), ("c01", c01)):
                r = interference({"h": moved, "o": solid})["h|o"]
                if not r.ok:
                    put_inconclusive(f"U-03c.interference[{n}, {other}, dz {d}]", "mm3", r.reason)
                    continue
                if r.measured >= worst_i:
                    worst_i, worst_at = r.measured, f"{n} vs {other} at dz {d}"
            if d < 0:
                c = clearance(moved, path_c11)
                if c.ok and c.measured < min_cl[0]:
                    min_cl = (c.measured, f"{n} at dz {d}")
    put("U-03c.path_interference_worst", value("path_interference", worst_i, "mm3", at=worst_at), "<=",
        SPEC["interference_max"], note=f"{len(steps)} poses, dz {steps[0]} … {steps[-1]}, step {SPEC['path']['step']}")
    put("D-04d.path_min_clearance_to_c11", value("path_clearance", min_cl[0], "mm", at=min_cl[1]), ">=",
        SPEC["neck_to_hole_min"], assumes=("A-01",), note="collar and neck passing the hole, poses dz < 0")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default=None, help="sweep run folder (relative to 01_CAD), else nominal")
    ap.add_argument("--fast", action="store_true")
    args = ap.parse_args()
    if args.run:
        folder = HERE / args.run
        params = json.loads((folder / "params.json").read_text())
        half_step = folder / "od_c14_grommet_half.step"
        asm_step = folder / "od_c14_assembly.step"
        stl = folder / "od_c14_grommet_half.stl"
        out_dir = folder
    else:
        params = dict(build.PARAMS)
        half_step = WS / "02_STEP_STL/od_c14_grommet_half_C1_v01.step"
        asm_step = WS / "02_STEP_STL/od_c14_assembly_C1_v01.step"
        stl = WS / "02_STEP_STL/od_c14_grommet_half_C1_v01.stl"
        out_dir = HERE / "check_v01"
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        run(half_step, asm_step, stl, params, out_dir, args.fast)
    except Exception as exc:                              # noqa: BLE001
        put_inconclusive("check_script", "", f"{type(exc).__name__}: {exc}", note=traceback.format_exc()[-800:])
    (out_dir / "check_results.json").write_text(json.dumps(ROWS, indent=1, default=str) + "\n")
    counts = {}
    for r in ROWS:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    for r in ROWS:
        if r["status"] not in ("PASS", "PASS_ASSUMED", "REPORTED"):
            print(f"{r['status']:13s} {r['gate']}: {r['measured']} {r['unit']} req {r['required']} {r['reason']}")
    print(json.dumps(counts))


if __name__ == "__main__":
    main()
