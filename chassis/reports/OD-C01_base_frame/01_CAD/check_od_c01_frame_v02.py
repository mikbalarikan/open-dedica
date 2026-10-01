"""Checks for od_c01_frame v02 (job 20260930-od-c01-base-frame, concept C1, spec 1.2).

Written before the build (PLAYBOOK D3). Every predicate measures the re-imported
STEP files with tools.core / tools.measure and compares through tools.result.gate
with the GATES.md section 0 band. Thresholds come from DESIGN_SPEC.md 1.2 section 5
only (the SPEC table below cites the row of each value). Any exception or missing
value gives INCONCLUSIVE.

v02 (brief WP-04): twenty insert holes (REQ-10, the OD-C07 pattern, A-17); the
OD-G01 v02 housing at the vertical pose of spec 1.2 section 4 (A-01), read back;
the carrier foot box x +-55, z -70 .. -26; reserved zones and hole webs reported.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/check_od_c01_frame_v02.py \
        --step 02_STEP_STL/od_c01_frame_C1_v02.step \
        --asm 02_STEP_STL/od_c01_assembly_C1_v02.step \
        --stl 02_STEP_STL/od_c01_frame_C1_v02.stl \
        --out 01_CAD/check_od_c01_frame_v02.json [--variant '{"plate_t": 5.9}'] [--light]
Relative paths are taken from the job workspace (the folder above 01_CAD).
"""
from __future__ import annotations

import argparse
import json
import math
import struct
import sys
import time
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
sys.path.insert(0, str(HERE))

from build123d import GeomType, Location  # noqa: E402

from tools.core import common_volume, compare_step, read_step, validity, write_stl  # noqa: E402
from tools.core.step import file_sha256  # noqa: E402
from tools.measure import (bore_census, clearance, envelope, feature_census, locate_bore,  # noqa: E402
                           mass_properties, mesh_census, min_wall, min_wall_wide, overhang_census,
                           radial_extent)
from tools.result import INCONCLUSIVE, MEASURED, Result, gate, inconclusive  # noqa: E402

# ---------------------------------------------------------------------------
# Section 5 thresholds (spec 1.2) and the GATES.md section 0 bands. Nothing below
# this table carries a threshold.
# ---------------------------------------------------------------------------
BAND = {"mm": 0.005, "deg": 0.001, "mm3": 0.001, "count": 0, "bool": 0}
SPEC = {
    # U-02: 240.0 x 6.0 x 405.0 each in [spec - 0.1, spec + 0.1]; position x +-120, y -6..0, z -305..+100
    "size": {"size_x": 240.0, "size_y": 6.0, "size_z": 405.0},
    "size_tol": 0.1,
    "position": {"min_x": -120.0, "max_x": 120.0, "min_y": -6.0, "max_y": 0.0, "min_z": -305.0, "max_z": 100.0},
    # D-02 (A-09): Kobra Max 3 420 x 420 x 500, flat: x and z on the bed, y tall
    "bed": {"size_x": 420.0, "size_z": 420.0, "size_y": 500.0},
    # D-01a, D-01b, D-06a, U-06 (Soft), J-05
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0, "wall_wide": 2.0, "wall_insert": 3.0,
    # D-03a (A-14): >= 45 deg, build direction +Y
    "overhang_deg": 45.0, "build_dir": (0.0, 1.0, 0.0),
    # D-03b: bridge span <= 5
    "bridge_span": 5.0,
    # U-07: STL tol 0.01, angular <= 4*acos(1 - 0.01/6.0), sagitta <= 0.01
    "stl_tol": 0.01, "stl_ang_max": 4.0 * math.acos(1.0 - 0.01 / 6.0),
    # REQ-01 .. REQ-04, REQ-10, D-05b: Dia 4.0 +- 0.05, depth >= 5.7, offset <= 0.10
    "insert_d": 4.0, "insert_tol": 0.05, "insert_depth": 5.7, "offset_max": 0.10,
    "inserts": {
        "REQ-01": [(35.0, -40.0), (-35.0, -40.0), (35.0, -60.0), (-35.0, -60.0)],
        "REQ-02": [(40.0, -148.0), (-40.0, -148.0), (40.0, -114.0), (-40.0, -114.0)],
        "REQ-03": [(-4.0, -239.0), (-4.0, -171.0), (37.0, -239.0), (37.0, -171.0)],
        "REQ-04": [(65.0, -45.0), (65.0, -105.0), (65.0, -165.0), (65.0, -225.0)],
        "REQ-10": [(-113.0, -42.0), (-71.0, -42.0), (-113.0, -148.5), (-71.0, -148.5)],
    },
    "req_assumes": {"REQ-01": ("A-01", "A-11"), "REQ-02": ("A-02", "A-11"), "REQ-03": ("A-03", "A-11"),
                    "REQ-04": ("A-04", "A-11"), "REQ-10": ("A-17", "A-11")},
    # REQ-05, D-04a (A-12): Dia 3.4 +- 0.1, >= 3.25
    "feet": [(110.0, 90.0), (-110.0, 90.0), (110.0, -295.0), (-110.0, -295.0)],
    "foot_d": 3.4, "foot_tol": 0.1, "foot_min": 3.25,
    # REQ-06 (A-13): Dia 8.0 +- 0.1
    "drains": [(-80.0, -120.0), (-80.0, -230.0)], "drain_d": 8.0, "drain_tol": 0.1,
    # D-05a: material >= 8.0 across around each insert hole
    "boss_across": 8.0,
    # REQ-07: top face y 0.00 +- 0.10, thickness 6.0 +- 0.1, one plane
    "top_y": 0.0, "top_tol": 0.10, "thick": 6.0, "thick_tol": 0.1, "top_faces": 1,
    # U-03 (a), REQ-08
    "contact": 0.0, "h01_gap": 2.0, "h11_gap": 10.0, "mount_gap": 2.0, "h11_max_z": -85.0, "g01_gap": 2.0,
    "interference": 0.0,
    # U-05 census (plan section 3 as amended by WP-04): 6 planar, 30 cylindrical (26 concave, 4 convex), 26 bores
    "census": {"plane_faces": 6, "cylinder_faces": 30, "concave_cylinders": 26, "convex_cylinders": 4,
               "bores": 26},
    "bore_groups": {4.0: 20, 3.4: 4, 8.0: 2},
    # A-10 (reported only)
    "density": 1270.0,
}
# a derivation of the plan (section 3), reported beside the measured area, not gated
# 20 x 2.0^2 + 4 x 1.7^2 + 2 x 4.0^2 = 123.56 (WP-04: rederived for 26 holes)
TOP_AREA_DERIVED = 97200.0 - (400.0 - 100.0 * math.pi) - 123.56 * math.pi
WALL_SPACING = 0.7          # plan section 4: the tool's 0.63 mm floor for the 405 x 240 face, rounded up
PATH_LIFTS = (10.0, 1.0, 0.1, 0.0)
PLATE = "od_c01_frame"
LABELS = {"c03": "od_c03_cradle", "h01": "od_h01_pump", "c04": "od_c04_mount", "h11": "od_h11_thermoblock",
          "g01": "od_g01_housing", "box": "od_c05_foot_reference_A01"}
# OD-G01 v02 read-back expected by spec 1.2 section 4 (the joint U-03 cites): rear face y 205.0,
# mouth face y 176.76, x +-50, z -18 .. +82
G01_POSE = {"max_y": 205.0, "min_x": -50.0, "max_x": 50.0, "min_z": -18.0, "max_z": 82.0}
G01_MOUTH_Y = 176.76
# reserved zones of spec 1.2 section 4 (A-05 .. A-08): reported, not gated. Heights: tray 36.9 (A-06 cup
# rest top), valve 48 (OD-C07 envelope, section 4); tank and electronics no height given: 400.
ZONES = {"tray": ((-75.0, 75.0), (0.0, 36.9), (-15.0, 85.0)),
         "tank": ((-70.0, 70.0), (0.0, 400.0), (-305.0, -250.0)),
         "valve": ((-117.0, -67.0), (0.0, 48.0), (-154.0, -35.0)),
         "electronics": ((70.0, 120.0), (0.0, 400.0), (-240.0, -30.0))}
INPUTS = {"c03": "OD-C03_pump_cradle.step", "h01": "OD-H01_ulka_ep5_pump.step",
          "c04": "OD-C04_thermoblock_mount.step", "h11": "OD-H11_thermoblock.step",
          "g01": "OD-G01_housing_C1_v02.step"}


def _safe(fn, name, unit, *args, **kwargs):
    """Run a measurement; any exception is INCONCLUSIVE with its reason."""
    try:
        return fn(*args, **kwargs)
    except Exception as exc:  # noqa: BLE001: a check never raises
        return inconclusive(name, unit, f"{type(exc).__name__}: {exc}")


class Gates:
    def __init__(self):
        self.rows: list[dict] = []

    def add(self, gate_id, result, op, limit, *, assumes=(), required=None, note=""):
        try:
            g = gate(gate_id, result, op, limit, band=BAND.get(result.unit, 0), assumes=assumes,
                     required=required)
            row = g.row()
            row["reason"] = g.reason
        except Exception as exc:  # noqa: BLE001
            row = {"gate": gate_id, "measured": None, "unit": getattr(result, "unit", ""),
                   "required": required or f"{op} {limit}", "margin": None, "at": None,
                   "status": INCONCLUSIVE, "method": getattr(result, "name", ""),
                   "assumes": list(assumes), "reason": f"{type(exc).__name__}: {exc}"}
        if note:
            row["note"] = note
        params = getattr(result, "params", None)
        if params:
            row["params"] = {k: v for k, v in params.items() if isinstance(v, (int, float, str, tuple, list))}
        detail = getattr(result, "detail", None)
        if detail:
            row["detail"] = {k: v for k, v in detail.items()
                             if k not in ("bores", "points", "material", "pairs", "samples")}
        self.rows.append(row)
        return row

    def fixed(self, gate_id, status, required, note, measured=None, unit="", assumes=()):
        self.rows.append({"gate": gate_id, "measured": measured, "unit": unit, "required": required,
                          "margin": None, "at": None, "status": status, "method": "by the row",
                          "assumes": list(assumes), "reason": "", "note": note})


def _children(shape):
    out = {}
    for child in getattr(shape, "children", ()) or ():
        if getattr(child, "children", ()):
            out.update(_children(child))
        else:
            out[child.label] = child
    return out


def _stl_facts(path: Path) -> dict:
    """Triangle count and bounding box read straight from a binary STL (a corroboration
    for the orchestrator's 3MF read-back; the gate reads the B-rep)."""
    data = path.read_bytes()
    n = struct.unpack_from("<I", data, 80)[0]
    lo = [math.inf] * 3
    hi = [-math.inf] * 3
    for i in range(n):
        vals = struct.unpack_from("<12f", data, 84 + 50 * i)
        for v in range(3):
            for a in range(3):
                c = vals[3 + 3 * v + a]
                lo[a] = min(lo[a], c)
                hi[a] = max(hi[a], c)
    return {"triangles_header": n, "bytes": len(data), "bbox_min": lo, "bbox_max": hi,
            "bbox_size": [hi[a] - lo[a] for a in range(3)]}


def _hole_rows(G, census, gid, pts, d0, tol, *, assumes, mid_y, depth_min=None, dmin=None, dmin_gate=None,
               dmin_assumes=()):
    for x, z in pts:
        tag = f"x{x:+g}_z{z:+g}"
        loc = _safe(locate_bore, "locate_bore", "mm", census, (x, mid_y, z), (0, 1, 0))
        if isinstance(loc, Result):
            loc = {"diameter": loc, "offset": loc, "length": loc, "through": loc}
        G.add(f"{gid}.{tag}.diameter", loc["diameter"], "in", (d0 - tol, d0 + tol), assumes=assumes)
        G.add(f"{gid}.{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=assumes)
        G.add(f"{gid}.{tag}.through", loc["through"], "==", 1, assumes=assumes)
        if depth_min is not None:
            G.add(f"D-05b.{tag}.diameter", loc["diameter"], "in", (d0 - tol, d0 + tol), assumes=("A-11",))
            G.add(f"D-05b.{tag}.depth", loc["length"], ">=", depth_min, assumes=("A-11",))
            G.add(f"D-05b.{tag}.through", loc["through"], "==", 1, assumes=("A-11",))
        if dmin is not None:
            G.add(f"{dmin_gate}.{tag}", loc["diameter"], ">=", dmin, assumes=dmin_assumes)


def _nearest_angle(x, z, others):
    """Angle (deg, right hand about +Y from +X) toward the nearest other hole centre."""
    best = min(others, key=lambda o: math.hypot(o[0] - x, o[1] - z))
    dx, dz = best[0] - x, best[1] - z
    return math.degrees(math.atan2(-dz, dx)) % 360.0, best


def _insert_rings(G, plate, facts):
    """D-05a and J-05 located readings: from each insert axis, material continuous from
    the hole wall outward; the first stretch's end is the material radius."""
    inserts = [pt for pts in SPEC["inserts"].values() for pt in pts]
    all_holes = inserts + SPEC["feet"] + SPEC["drains"]
    least_end, least_wall, where = math.inf, math.inf, None
    rays = 0
    failures = []
    per_hole = {}
    t0 = time.time()
    for x, z in inserts:
        near_ang, near = _nearest_angle(x, z, [h for h in all_holes if h != (x, z)])
        angles = [float(a) for a in range(0, 360, 10)] + [near_ang]
        for lvl in (2.5, 0.0, -2.5):            # y -0.5, -3.0, -5.5 about the axis origin y -3.0
            for a in angles:
                rays += 1
                r = _safe(radial_extent, "radial_extent", "mm", plate, (x, -3.0, z), (0, 1, 0), (1, 0, 0),
                          a, lvl, side="inner")
                mat = (r.detail or {}).get("material") if r.status == MEASURED else None
                if not mat:
                    failures.append({"at": (x, z, a, lvl), "reason": r.reason})
                    continue
                first = min(mat, key=lambda s: s[0])
                end, wall = first[1], first[1] - first[0]
                ph = per_hole.setdefault(f"x{x:+g}_z{z:+g}", {"least_web_mm": math.inf, "at_deg": None})
                if wall < ph["least_web_mm"]:
                    ph["least_web_mm"], ph["at_deg"] = wall, round(a, 3)
                if end < least_end:
                    least_end, where = end, (x, -3.0 + lvl, z, round(a, 3))
                least_wall = min(least_wall, wall)
    facts["insert_rings"] = {"rays": rays, "failed": len(failures), "first_failures": failures[:5],
                             "least_first_stretch_end_mm": least_end, "least_wall_mm": least_wall,
                             "at": where, "seconds": round(time.time() - t0, 1), "per_hole": per_hole}
    if failures or not math.isfinite(least_end):
        across = inconclusive("insert_material_across", "mm", f"{len(failures)} of {rays} rays unread")
        wall = inconclusive("insert_ring_wall", "mm", f"{len(failures)} of {rays} rays unread")
    else:
        across = Result("insert_material_across", 2.0 * least_end, "mm", at=where,
                        detail={"rays": rays, "least_first_stretch_end": least_end,
                                "method": "2 x least radius of material continuous from the hole wall"})
        wall = Result("insert_ring_wall", least_wall, "mm", at=where,
                      detail={"rays": rays, "method": "least (first stretch end - hole wall radius)"})
    G.add("D-05a", across, ">=", SPEC["boss_across"], assumes=("A-11",))
    G.add("J-05.ring", wall, ">=", SPEC["wall_insert"], note="located reading around the 20 insert holes")


def run(step_path: Path, asm_path: Path, stl_path: Path | None, params_override: dict | None = None,
        scratch: Path | None = None, heavy: bool = True) -> dict:
    """All predicates; returns {"gates": [...], "facts": {...}}."""
    import build_od_c01_frame_v02 as build

    G = Gates()
    facts: dict = {"wall_spacing_mm": WALL_SPACING}
    plate = read_step(step_path)

    # exactly_one_solid, U-01 ---------------------------------------------------
    v = validity(plate)
    G.add("exactly_one_solid", v["solid_count"], "==", 1)
    G.add("U-01.solid_count", v["solid_count"], "==", 1)
    G.add("U-01.brep_valid", v["brep_valid"], "==", 1)
    G.add("U-01.naked_edges", v["naked_edges"], "==", 0)

    # envelope_within_spec, U-02, D-02 -----------------------------------------
    env = envelope(plate)
    facts["envelope"] = {k: r.measured for k, r in env.items()}
    for key, nominal in SPEC["size"].items():
        lo, hi = nominal - SPEC["size_tol"], nominal + SPEC["size_tol"]
        G.add(f"U-02.{key}", env[key], "in", (lo, hi))
        G.add(f"envelope_within_spec.size.{key}", env[key], "in", (lo, hi))
    for key, nominal in SPEC["position"].items():
        G.add(f"envelope_within_spec.position.{key}", env[key], "in",
              (nominal - SPEC["size_tol"], nominal + SPEC["size_tol"]),
              note="position against the datum, reported apart from size (U-02)")
    for key, limit in SPEC["bed"].items():
        G.add(f"D-02.{key}", env[key], "<=", limit, assumes=("A-09",))
    mp = _safe(mass_properties, "mass_properties", "g", plate, SPEC["density"])
    facts["mass_properties"] = {k: (r.measured, r.unit) for k, r in mp.items()} if isinstance(mp, dict) else mp.reason

    # U-04 clean export (part) -------------------------------------------------
    p = build.Params(**(params_override or {}))
    built = build.build_plate(p)
    rt = compare_step(built, step_path)
    for k, want, op in (("schema", 1, "=="), ("solids", 1, "=="), ("volume_delta", 0, "<="),
                        ("faces_delta", 0, "=="), ("labels", 1, "=="), ("valid_after", 1, "==")):
        G.add(f"U-04.part.{k}", rt[k], op, want)
    facts["label_reimported"] = rt["labels"].detail.get("reimported") if rt["labels"].detail else None

    # U-05 feature census, bores -----------------------------------------------
    fc = feature_census(plate)
    facts["feature_census"] = {k: r.measured for k, r in fc.items()}
    for key in fc:
        want = SPEC["census"].get(key, 0)
        G.add(f"U-05.{key}", fc[key], "==", want)
        G.add(f"feature_census.{key}", fc[key], "==", want)
    census = bore_census(plate)
    bores = census.detail.get("bores", []) if census.status == MEASURED else []
    facts["bore_census"] = census.measured if census.status == MEASURED else census.reason
    for d0, n in SPEC["bore_groups"].items():
        k = sum(1 for b in bores if abs(b["diameter"] - d0) < 0.2 and b.get("through", True))
        G.add(f"U-05.bores_dia{d0}", Result("bore_group_count", k, "count",
                                            detail={"method": "bore_census bores within 0.2 of the diameter"}),
              "==", n)

    webs = []
    for i, b1 in enumerate(bores):
        for b2 in bores[i + 1:]:
            s1, s2 = b1.get("start"), b2.get("start")
            if s1 is None or s2 is None:
                continue
            dist = math.hypot(s1[0] - s2[0], s1[2] - s2[2])
            webs.append((dist - 0.5 * b1["diameter"] - 0.5 * b2["diameter"],
                         (round(s1[0], 3), round(s1[2], 3), round(b1["diameter"], 3)),
                         (round(s2[0], 3), round(s2[2], 3), round(b2["diameter"], 3))))
    webs.sort(key=lambda w: w[0])
    valve = SPEC["inserts"]["REQ-10"]
    facts["hole_webs"] = {"nearest_10": webs[:10],
                          "valve_holes": {f"x{x:+g}_z{z:+g}": [w for w in webs if any(
                              abs(e[0] - x) < 0.2 and abs(e[1] - z) < 0.2 for e in (w[1], w[2]))][:3] for x, z in valve},
                          "asked": [w for w in webs if any(abs(e[0] - hx) < 0.2 and abs(e[1] - hz) < 0.2 for e in (w[1], w[2])
                                                         for hx, hz in ((-80.0, -120.0), (-110.0, 90.0)))
                                      and any(abs(e[0] - x) < 0.2 and abs(e[1] - z) < 0.2 for e in (w[1], w[2])
                                              for x, z in valve)],
                          "method": "bore_census axis start points (x, z); web = centre distance - r1 - r2"}

    # REQ-01 .. REQ-04, REQ-10, D-05b; REQ-05, D-04a; REQ-06 ----------------------
    mid_y = -0.5 * SPEC["thick"]
    for gid, pts in SPEC["inserts"].items():
        _hole_rows(G, census, gid, pts, SPEC["insert_d"], SPEC["insert_tol"], assumes=SPEC["req_assumes"][gid],
                   mid_y=mid_y, depth_min=SPEC["insert_depth"])
    _hole_rows(G, census, "REQ-05", SPEC["feet"], SPEC["foot_d"], SPEC["foot_tol"], assumes=("A-12",),
               mid_y=mid_y, dmin=SPEC["foot_min"], dmin_gate="D-04a", dmin_assumes=("A-12",))
    _hole_rows(G, census, "REQ-06", SPEC["drains"], SPEC["drain_d"], SPEC["drain_tol"], assumes=("A-13",),
               mid_y=mid_y)

    # REQ-07 floor plane -----------------------------------------------------------
    t = SPEC["top_tol"]
    G.add("REQ-07.top_y", env["max_y"], "in", (SPEC["top_y"] - t, SPEC["top_y"] + t), assumes=("A-01", "A-02", "A-03"))
    G.add("REQ-07.thickness", env["size_y"], "in", (SPEC["thick"] - SPEC["thick_tol"], SPEC["thick"] + SPEC["thick_tol"]))
    ymax = env["max_y"].measured
    tops = [f for f in plate.faces() if f.geom_type == GeomType.PLANE and f.normal_at().Y > 1 - 1e-9
            and ymax is not None and abs(envelope(f)["max_y"].measured - ymax) < 1e-6]
    ups = [f for f in plate.faces() if f.geom_type == GeomType.PLANE and f.normal_at().Y > 1 - 1e-9]
    facts["top_face"] = {"faces_up": len(ups), "faces_at_max_y": len(tops),
                         "area_mm2": sum(f.area for f in tops), "area_derived_mm2": TOP_AREA_DERIVED,
                         "flatness_mm": [envelope(f)["size_y"].measured for f in tops]}
    G.add("REQ-07.top_faces", Result("top_plane_count", len(ups), "count",
                                     detail={"at_max_y": len(tops), "area_mm2": facts["top_face"]["area_mm2"]}),
          "==", SPEC["top_faces"], note="planar faces with normal +Y; the only one is at max y")
    if tops:
        G.add("REQ-07.top_flatness", envelope(tops[0])["size_y"], "<=", 0.0,
              note="the top face's own y extent (one plane)")

    # Assembly as placed ---------------------------------------------------------
    asm = _safe(read_step, "read_step", "mm", asm_path)
    parts = _children(asm) if not isinstance(asm, Result) else {}
    facts["assembly_labels"] = sorted(parts)
    missing = inconclusive("assembly", "mm", f"assembly parts missing: have {sorted(parts)}")
    P = {k: parts.get(lbl) for k, lbl in LABELS.items()}
    plate_asm = parts.get(PLATE)
    if plate_asm is not None:
        facts["assembly_plate_volume_delta_mm3"] = abs(plate_asm.volume - plate.volume)
    sound = {}
    for k, s in P.items():
        if s is None:
            sound[k] = False
            continue
        vv = validity(s)
        facts[f"{k}_validity"] = {n: (r.measured, r.reason[:120] if r.reason else "") for n, r in vv.items()}
        facts[f"{k}_envelope"] = {n: r.measured for n, r in envelope(s).items()}
        sound[k] = all(r.status == MEASURED for r in vv.values()) and vv["brep_valid"].measured == 1 \
            and vv["solid_count"].measured == 1 and vv["naked_edges"].measured == 0

    def cl(a, b):
        return _safe(clearance, "clearance", "mm", a, b) if a is not None and b is not None else missing

    def iv(a, b, ka):
        if a is None or b is None:
            return missing
        if not sound.get(ka, False):
            return inconclusive("common_volume", "mm3", f"{LABELS[ka]} is not a sound solid (validity); "
                                "a boolean against it is INCONCLUSIVE (OD-C04 A-14)")
        return _safe(common_volume, "common_volume", "mm3", a, b)

    A03, A02, A01 = ("A-03",), ("A-02",), ("A-01",)
    # plate | mounts: designed contacts, coaxial holes
    for k, asm_ in (("c03", A03), ("c04", A02)):
        m = P[k]
        G.add(f"U-03a.plate|{LABELS[k]}.clearance", cl(plate, m), "==", SPEC["contact"], assumes=asm_)
        G.add(f"U-03a.plate|{LABELS[k]}.interference", iv(plate, m, k), "<=", SPEC["interference"], assumes=asm_)
        pts = SPEC["inserts"]["REQ-03" if k == "c03" else "REQ-02"]
        mc = _safe(bore_census, "bore_census", "count", m) if m is not None else missing
        for x, z in pts:
            tag = f"x{x:+g}_z{z:+g}"
            try:
                ml = locate_bore(mc, (x, 1.0, z), (0, 1, 0))
                st = ml["diameter"].detail["start"]
                facts[f"{k}_hole_{tag}"] = {"diameter": ml["diameter"].measured, "start": st,
                                            "end": ml["diameter"].detail["end"], "offset_to_spec": ml["offset"].measured}
                pl = locate_bore(census, (st[0], mid_y, st[2]), (0, 1, 0))
                off = pl["offset"]
                off = Result("coaxial_offset", off.measured, "mm", at=(st[0], mid_y, st[2]),
                             detail={"mount_axis_xz": (st[0], st[2]), "mount_dia": ml["diameter"].measured,
                                     "plate_dia": pl["diameter"].measured}) if off.status == MEASURED else off
            except Exception as exc:  # noqa: BLE001
                off = inconclusive("coaxial_offset", "mm", f"{type(exc).__name__}: {exc}")
            G.add(f"U-03a.plate|{LABELS[k]}.coaxial.{tag}", off, "<=", SPEC["offset_max"], assumes=asm_)
    G.add("U-03a.plate|od_h01_pump.clearance", cl(plate, P["h01"]), ">=", SPEC["h01_gap"], assumes=A03)
    G.add("U-03a.plate|od_h01_pump.interference", iv(plate, P["h01"], "h01"), "<=", SPEC["interference"], assumes=A03)
    h11_gap = cl(plate, P["h11"])
    G.add("U-03a.plate|od_h11_thermoblock.clearance", h11_gap, ">=", SPEC["h11_gap"], assumes=A02)
    G.add("U-03a.plate|od_h11_thermoblock.interference", iv(plate, P["h11"], "h11"), "<=", SPEC["interference"],
          assumes=A02, note="INCONCLUSIVE by the row: OD-H11 is unsound for booleans (OD-C04 A-14)")
    G.add("U-03a.od_c03|od_c04.clearance", cl(P["c03"], P["c04"]), ">=", SPEC["mount_gap"], assumes=("A-02", "A-03"))
    h11_env = envelope(P["h11"])["max_z"] if P["h11"] is not None else missing
    G.add("U-03a.od_h11.max_z", h11_env, "<=", SPEC["h11_max_z"], assumes=A02)
    G.add("REQ-08.max_z", h11_env, "<=", SPEC["h11_max_z"], assumes=A02)
    G.add("REQ-08.clearance", h11_gap, ">=", SPEC["h11_gap"], assumes=A02)
    for k in ("plate", "c03", "h01", "c04", "h11", "box"):
        other = plate if k == "plate" else P[k]
        name = PLATE if k == "plate" else LABELS[k]
        G.add(f"U-03a.od_g01|{name}.clearance", cl(P["g01"], other), ">=", SPEC["g01_gap"], assumes=A01)
        if k == "h11":
            G.add(f"U-03a.od_g01|{name}.interference", iv(other, P["g01"], "h11"), "<=", SPEC["interference"],
                  assumes=A01, note="INCONCLUSIVE by the row: OD-H11 is unsound (OD-C04 A-14)")
        else:
            gi = iv(P["g01"], other, "g01") if sound.get(k, True) else inconclusive(
                "common_volume", "mm3", f"{name} not sound")
            G.add(f"U-03a.od_g01|{name}.interference", gi, "<=", SPEC["interference"], assumes=A01)
    # OD-G01 v02 pose read-back (spec 1.2 section 4 joint, cited by U-03; A-01)
    if P["g01"] is not None:
        ge = envelope(P["g01"])
        for key, want in G01_POSE.items():
            G.add(f"U-03a.od_g01.pose.{key}", ge[key], "==", want, assumes=A01,
                  note="read-back of the housing at the vertical pose (spec 1.2 section 4)")
        try:
            mouth = [f for f in P["g01"].faces() if f.geom_type == GeomType.PLANE and f.normal_at().Y < -1 + 1e-9]
            ys = sorted({round(envelope(f)["min_y"].measured, 4) for f in mouth})
            facts["g01_downward_planes_y"] = ys
            hit = [y for y in ys if abs(y - G01_MOUTH_Y) <= BAND["mm"]]
            mr = Result("g01_mouth_face_y", hit[0], "mm", detail={"downward_planes_y": ys[:12]}) if hit else \
                inconclusive("g01_mouth_face_y", "mm", f"no downward plane at y {G01_MOUTH_Y}: {ys[:12]}")
        except Exception as exc:  # noqa: BLE001
            mr = inconclusive("g01_mouth_face_y", "mm", f"{type(exc).__name__}: {exc}")
        G.add("U-03a.od_g01.pose.mouth_face_y", mr, "==", G01_MOUTH_Y, assumes=A01,
              note="a downward (-Y) planar face at the mouth height: the mouth faces down")
    else:
        G.add("U-03a.od_g01.pose", missing, "==", 1, assumes=A01)
    # information (brief WP-04): the carrier foot box to OD-C04 and to the tray zone; zone clearances
    from build123d import Align as _Al, Box as _Box, Pos as _Pos
    zone_solids = {}
    for zn, ((x0, x1), (y0, y1), (z0, z1)) in ZONES.items():
        zone_solids[zn] = _Pos(x0, y0, z0) * _Box(x1 - x0, y1 - y0, z1 - z0, align=(_Al.MIN, _Al.MIN, _Al.MIN))
    zc = {}
    for k in ("c03", "h01", "c04", "h11", "g01", "box"):
        zc[LABELS[k]] = {}
        for zn, zs in zone_solids.items():
            r = cl(P[k], zs)
            zc[LABELS[k]][zn] = r.measured if r.status == MEASURED else r.reason
    facts["zone_clearance_mm"] = {"zones": {k: v for k, v in ZONES.items()}, "clearance": zc,
                                  "note": "0 would mean the placed solid enters the zone prism; not gated"}
    bc = cl(P["box"], P["c04"])
    facts["carrier_box_gaps_mm"] = {"to_od_c04_foot": (bc.measured, getattr(bc, "at", None)),
                                    "to_tray_zone": zc[LABELS["box"]].get("tray")}
    G.add("U-03a.plate|od_c05_foot_reference_A01.clearance", cl(plate, P["box"]), "==", SPEC["contact"], assumes=A01)
    G.add("U-03a.plate|od_c05_foot_reference_A01.interference", iv(plate, P["box"], "box"), "<=",
          SPEC["interference"], assumes=A01)
    # assembly path (L-10): each seated part lowered straight down -Y onto y 0
    for k in ("c03", "c04", "box"):
        for lift in PATH_LIFTS:
            m = P[k]
            if m is None:
                r = missing
            else:
                r = cl(plate, m.moved(Location((0.0, lift, 0.0))))
            G.add(f"U-03a.path.{LABELS[k]}.lift{lift:g}", r, "==", lift, assumes=A01 if k == "box" else (A02 if k == "c04" else A03),
                  note="clearance to the plate equals the lift: nothing of the plate in the way down")
    G.fixed("U-03b", "N/A", "N/A", "U-03 (b): no motion variable (N/A by the row)")

    # U-04 clean export (assembly) -------------------------------------------------
    try:
        built_asm = build.build_assembly(p)["assembly"]
        ra = compare_step(built_asm, asm_path)
        for k, want, op in (("schema", 1, "=="), ("solids", 7, "=="), ("faces_delta", 0, "=="), ("labels", 1, "==")):
            G.add(f"U-04.assembly.{k}", ra[k], op, want)
        whole = ra["volume_delta"]
        G.add("U-04.assembly.volume_delta_whole", inconclusive(
            "step_roundtrip_volume_delta", "mm3",
            f"the whole-assembly volume includes OD-H11, unsound (brep_valid 0, OD-C04 A-14): measured "
            f"{whole.measured} mm3; gated per part below"), "<=", 0, note="INCONCLUSIVE by OD-C04 A-14")
        facts["assembly_valid_after_whole"] = (ra["valid_after"].measured, ra["valid_after"].reason[:200]
                                               if ra["valid_after"].reason else "")
        built_parts = _children(built_asm)
        for k, lbl in [("plate", PLATE)] + list(LABELS.items()):
            back = parts.get(lbl)
            src = built_parts.get(lbl)
            if back is None or src is None:
                G.add(f"U-04.assembly.{lbl}.present", missing, "==", 1)
                continue
            dv = Result("part_volume_delta", abs(back.volume - src.volume), "mm3",
                        detail={"built_mm3": src.volume, "reimported_mm3": back.volume})
            df = Result("part_faces_delta", abs(len(back.faces()) - len(src.faces())), "count")
            G.add(f"U-04.assembly.{lbl}.faces_delta", df, "==", 0)
            if k != "h11":
                G.add(f"U-04.assembly.{lbl}.volume_delta", dv, "<=", 0)
            if k == "h11":
                # an unsound solid's volume is not a sound measurement: reported, never passed
                facts["h11_roundtrip_volume_delta_mm3"] = dv.measured
                try:
                    from build123d import Solid
                    gen1 = Solid(back.solids()[0].wrapped)
                    gen1.label = "od_h11_gen2_probe"
                    scratch_dir = scratch or HERE
                    g2p = scratch_dir / "h11_gen2_probe.step"
                    from tools.core import write_step
                    write_step(gen1, g2p, timestamp="2026-09-30T00:00:00")
                    gen2 = read_step(g2p)
                    facts["h11_second_generation_volume_delta_mm3"] = abs(gen2.volume - back.volume)
                    g2p.unlink(missing_ok=True)
                except Exception as exc:  # noqa: BLE001
                    facts["h11_second_generation_volume_delta_mm3"] = f"{type(exc).__name__}: {exc}"
                G.add(f"U-04.assembly.{lbl}.volume_delta", inconclusive(
                    "part_volume_delta", "mm3",
                    f"OD-H11 is unsound (brep_valid 0, a pcurve off its edge, OD-C04 A-14): the writer's pcurve "
                    f"rebuild changes its volume once, measured {dv.measured} mm3; second generation "
                    f"{facts['h11_second_generation_volume_delta_mm3']} mm3"), "<=", 0,
                    note="INCONCLUSIVE by OD-C04 A-14; measured value in the reason")
                vin = validity(src)["brep_valid"]
                vb = validity(back)["brep_valid"]
                same = Result("h11_validity_unchanged", int(vin.measured == vb.measured), "bool",
                              detail={"input": vin.measured, "reimported": vb.measured})
                G.add(f"U-04.assembly.{lbl}.validity_unchanged", same, "==", 1,
                      note="OD-H11 was brep_valid 0 on input (OD-C04 A-14); gated as unchanged")
            else:
                vb = validity(back)["brep_valid"]
                G.add(f"U-04.assembly.{lbl}.valid_after", vb, "==", 1)
    except Exception as exc:  # noqa: BLE001
        G.add("U-04.assembly", inconclusive("assembly_roundtrip", "count", f"{type(exc).__name__}: {exc}"), "==", 1)

    # Walls, process rows ----------------------------------------------------------
    if heavy:
        t0 = time.time()
        mw = _safe(min_wall, "min_wall", "mm", plate, spacing=WALL_SPACING)
        facts["min_wall_seconds"] = round(time.time() - t0, 1)
        G.add("D-01a", mw, ">=", SPEC["wall_floor"], note=f"spacing {WALL_SPACING} mm")
        G.add("D-01b", mw, ">=", SPEC["wall_struct"], note=f"spacing {WALL_SPACING} mm")
        G.add("D-06a", mw, ">=", SPEC["min_feature"], note=f"spacing {WALL_SPACING} mm")
        G.add("J-05.min_wall", mw, ">=", SPEC["wall_insert"], note=f"spacing {WALL_SPACING} mm; the part's thinnest wall")
        ww = _safe(min_wall_wide, "min_wall_wide", "mm", plate, spacing=WALL_SPACING)
        G.add("U-06", ww, ">=", SPEC["wall_wide"], note=f"SOFT; spacing {WALL_SPACING} mm")
        t0 = time.time()
        oh = _safe(overhang_census, "overhang_census", "deg", plate, build_dir=SPEC["build_dir"],
                   min_deg=SPEC["overhang_deg"], spacing=WALL_SPACING)
        facts["overhang_seconds"] = round(time.time() - t0, 1)
        G.add("D-03a", oh, ">=", SPEC["overhang_deg"], assumes=("A-14",), note=f"spacing {WALL_SPACING} mm")
        below = oh.detail.get("below_min_deg") if oh.detail else None
        if oh.status == MEASURED and below == 0:
            span = Result("bridge_span", 0.0, "mm", detail={"basis": "overhang_census below_min_deg == 0: "
                                                                     "no downward face off the bed"})
        else:
            span = inconclusive("bridge_span", "mm", "downward faces under 45 deg exist or the census failed")
        G.add("D-03b", span, "<=", SPEC["bridge_span"], note="derived from D-03a; the reviewer confirms from sections")
        _insert_rings(G, plate, facts)

    # U-07 export mesh -------------------------------------------------------------
    if stl_path is not None and heavy:
        try:
            scratch = scratch or HERE
            ang = p.stl_ang
            w = write_stl(plate, scratch / "remesh_check.stl", tolerance=SPEC["stl_tol"], angular_tolerance=ang)
            G.add("U-07.stl_max_sagitta", w.checks["max_sagitta"], "<=", SPEC["stl_tol"])
            G.add("U-07.angular_tolerance", Result("stl_angular_tolerance", ang, "rad",
                                                   detail={"limit": SPEC["stl_ang_max"]}), "<=", SPEC["stl_ang_max"])
            facts["stl_remesh"] = {"triangles": w.detail.get("triangles"), "sha256": w.sha256}
            (scratch / "remesh_check.stl").unlink(missing_ok=True)
            mc = mesh_census(stl_path)
            facts["stl_delivered"] = {k: r.measured for k, r in mc.items()}
            facts["stl_delivered_sha256"] = file_sha256(stl_path)
            facts["stl_delivered_bbox"] = _stl_facts(stl_path)
            G.add("U-07.delivered_bodies", mc["bodies"], "==", 1)
            G.add("U-07.delivered_naked_edges", mc["naked_edges"], "==", 0)
            G.add("U-07.delivered_winding", mc["winding"], "==", 1)
        except Exception as exc:  # noqa: BLE001
            G.add("U-07.stl_max_sagitta", inconclusive("stl_max_sagitta", "mm", f"{type(exc).__name__}: {exc}"),
                  "<=", SPEC["stl_tol"])
        G.fixed("U-07.3mf", "ORCHESTRATOR_STEP", "the 3MF carries the same mesh",
                "orchestrator step (brief WP-03): the orchestrator writes the 3MF from the delivered STL and "
                "verifies it by re-parsing against the STL facts in the REPORT")

    G.fixed("U-08", "N/A", "threads cosmetic", "no threaded feature on this target (N/A by the row)")
    G.fixed("D-07", "N/A", "fit-critical bores", "insert, clearance and drain holes only (N/A by the row)")
    G.fixed("E-06", "N/A", "boss support", "no bosses on this part (N/A by the row)")
    G.fixed("REQ-09", INCONCLUSIVE, "flat in service (Soft, bench)",
            "Soft bench gate: not geometric; answered by the first print", assumes=("A-10", "A-14"))
    return {"gates": G.rows, "facts": facts}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", required=True)
    ap.add_argument("--asm", required=True)
    ap.add_argument("--stl")
    ap.add_argument("--out", required=True)
    ap.add_argument("--variant", default="{}")
    ap.add_argument("--light", action="store_true", help="skip walls, overhang, rings and the mesh")
    a = ap.parse_args()
    ws = lambda s: (WS / s) if not Path(s).is_absolute() else Path(s)  # noqa: E731
    out = ws(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    variant = json.loads(a.variant)
    try:
        res = run(ws(a.step), ws(a.asm), ws(a.stl) if a.stl else None, variant or None,
                  scratch=out.parent, heavy=not a.light)
    except Exception as exc:  # noqa: BLE001
        res = {"gates": [], "facts": {}, "error": f"{type(exc).__name__}: {exc}", "trace": traceback.format_exc()}
    res["inputs"] = {"step": a.step, "asm": a.asm, "stl": a.stl, "variant": variant}
    out.write_text(json.dumps(res, indent=1, default=str))
    for r in res["gates"]:
        print(f"{r['gate']:<52} {r['status']:<13} {r['measured']!s:<22} {r['unit']:<6} "
              f"{r['required']:<22} margin {r['margin']}")
    if "error" in res:
        print(res["trace"])


if __name__ == "__main__":
    main()
