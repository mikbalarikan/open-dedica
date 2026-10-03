"""Gate checks for od_t01_rig v02, concept C1 (job 20261002-od-t01-pressure-test-rig), spec 1.3.

Written before the build (PLAYBOOK D3). Every predicate re-imports the exported
STEP and measures it with tools.measure / tools.core; limits come from
00_Spec/DESIGN_SPEC.md 1.3 §5 only, bands from GATES.md §0 (mm 0.005, deg 0.001,
mm3 0.001, counts 0). A measurement that raises or returns nothing is INCONCLUSIVE.

Usage (from the repo root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/check_od_t01_rig_v02.py --step <step> [--stl <stl>]
        [--params <params.json>] [--out <gates.json>]
The params JSON is the one the build writes (01_CAD/ for the delivery); it is used
for U-04 only (the shape is rebuilt from it and compared with the file). The mesh
JSON (--mesh-meta) records the STL's tolerances and triangle count for U-07.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import tempfile
import time
from pathlib import Path

import numpy as np
from build123d import Axis, Circle, Cylinder, Location, Plane, Pos, Vector, extrude
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_SHELL
from OCP.TopExp import TopExp_Explorer

from tools.core import compare_step, read_step, solid_count, validity, write_stl
from tools.measure import (bore_census, clearance, envelope, feature_census, flat_ceiling_spans,
                           interference, locate_bore, mesh_census, min_wall, overhang_census,
                           radial_extent)
from tools.result import FAIL, INCONCLUSIVE, PASS, PASS_ASSUMED, Result, gate, inconclusive

WS = Path(__file__).resolve().parent.parent
INPUTS = WS / "00_Spec" / "inputs"
ASSEMBLY_IN = INPUTS / "od_g01_assembly_C1_v03.step"

# ---- bands, GATES.md §0 ----------------------------------------------------------------
B_MM, B_DEG, B_MM3, B_N = 0.005, 0.001, 0.001, 0

# ---- spec 1.3 §2 / §4 / §5 values (the contract; nothing here comes from the build) ----
SPEC = {
    "env_size": (240.0, 160.0, 120.0), "env_tol": 0.1,
    "env_pos": {"min_x": -120.0, "max_x": 120.0, "min_y": 0.0, "max_y": 160.0,
                "min_z": -60.0, "max_z": 60.0},
    "housing_pose_y": 110.06,                    # §2: housing origin at (0, 110.06, 0)
    "seat_y": 135.0, "seat_tol": 0.10,            # REQ-02
    "clear_min": 2.0,                             # U-03a
    "offer_up": (0.0, 30.0, 2.0),                 # U-03b: dy 0 … 30, step ≤ 2.0
    "screw_xz": [(44.0, 44.0), (44.0, -44.0), (-44.0, 44.0), (-44.0, -44.0)],
    "screw_d": (3.4, 0.1), "screw_d_min": 3.25,   # REQ-01, D-04a
    "cbore_d": (6.5, 0.1), "cbore_top_y": 160.0, "cbore_floor_y": (140.0, 0.10),
    "under_head": (5.0, 0.1), "offset_max": 0.10,
    "window_r": (30.0, 0.1), "roof_deg": (45.1, 1.0), "window_apex_z": (42.51, 0.16),
    "pairb_axis_min": 10.87, "pairb_head_d": 17.7,   # REQ-03, A-12
    "phi_a": (-60.0, 15.0, 5.0), "clear_a": 5.0,     # REQ-04a
    "phi_b": -50.0, "drop_b": 15.0, "dz_b": (0.0, 200.0, 5.0),   # REQ-04b
    "headroom": 50.0,                                 # REQ-05
    "bench_xz": [(105.0, 40.0), (105.0, -40.0), (-105.0, 40.0), (-105.0, -40.0)],
    "bench_d": (4.5, 0.1), "bench_d_min": 4.25,       # REQ-06, D-04a
    "bench_probe": (8.0, 10.0, 300.0),                # REQ-06: Ø8, y 10 … 300
    "screw_probe": (6.0, 160.0, 300.0),               # REQ-07: Ø6, y 160 … 300
    "build_volume": (420.0, 420.0, 500.0),            # D-02, A-09 (bed X, bed Y, height Z)
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0, "wide_soft": 2.0,
    "overhang_min": 45.0, "bridge_max": 5.0, "crown_bridge_max": 3.4,
    "stl_tol": 0.01,
    # REQ-08 / A-02 hand numbers of §4, reported against the measured section at x 0 (not a gate)
    "hand_M_Nmm": 47.4e3, "hand_Z_mm3": 4948.0, "hand_sigma_MPa": 9.6, "pla_MPa": 40.0,
    # U-05, the plan's features as amended by spec 1.1 (walls z −60 … +40); spec 1.3 changes no count
    "census": {"planar_faces": 41, "cylinder_faces": 13, "other_faces": 0,
               "concave_cylinders": 13, "convex_cylinders": 0, "bores": 13,
               "bores_by_d": {3.4: 4, 6.5: 4, 60.0: 1, 4.5: 4}, "chamfer_planes": 4,
               "wall_inner_faces": 2, "wall_z": (-60.0, 40.0)},
}
BUILD_DIR = (0, 0, 1)        # A-10: lying on the rear face z −60, layers stacking along +Z


# ---- helpers -------------------------------------------------------------------------------
def res(name, value, unit, at=None, **detail) -> Result:
    if value is None or (isinstance(value, float) and not math.isfinite(value)):
        return inconclusive(name, unit, "no measured value")
    return Result(name, value, unit, at=at, detail=detail)


def guarded(fn):
    """A predicate that raises gives INCONCLUSIVE rows, never a crash or a pass."""
    def wrap(ctx, *a, **k):
        try:
            return fn(ctx, *a, **k)
        except Exception as exc:  # noqa: BLE001
            return [dict(gate=fn.__name__, measured=None, unit="", required="", margin=None, at=None,
                         status=INCONCLUSIVE, method=fn.__name__, assumes=[],
                         reason=f"{type(exc).__name__}: {exc}")]
    wrap.__name__ = fn.__name__
    return wrap


def row(gate_id, g, note=""):
    r = g.row()
    r["gate"] = gate_id
    if g.status == INCONCLUSIVE:
        r["reason"] = g.reason
    if note:
        r["note"] = note
    return r


def solid_list(shape):
    return list(shape.solids())


def env_of(shape):
    e = envelope(shape)
    return {k: v.measured for k, v in e.items()}


def housing_pose(seat_y: float) -> Location:
    """Spec §2: housing x → X, y → +Z, z → −Y, origin (0, 110.06, 0). The joint is the
    housing's rear face on the plate's measured underside: seat_y − 135.0 moves it."""
    dy = seat_y - SPEC["seat_y"]
    return Location((0, SPEC["housing_pose_y"] + dy, 0)) * Location((0, 0, 0), (1, 0, 0), 90)


def moved(shape, phi=0.0, dy=0.0, dz=0.0):
    """φ about the housing axis (rig +Y through x 0, z 0); φ > 0 turns +Z toward +X."""
    return Location((0, dy, dz)) * Location((0, 0, 0), (0, 1, 0), phi) * shape


def frange(lo, hi, step):
    n = int(round((hi - lo) / step))
    return [lo + i * step for i in range(n + 1)]


def probe_cyl(x, z, d, y0, y1):
    """A cylinder of diameter d along +Y from y0 to y1 on the axis (x, z)."""
    return Location((x, y0, z)) * Location((0, 0, 0), (1, 0, 0), -90) * Cylinder(d / 2, y1 - y0, align=None)


def point_face_distance(face, p) -> float:
    v = BRepBuilderAPI_MakeVertex(gp_Pnt(*p)).Vertex()
    d = BRepExtrema_DistShapeShape(v, face.wrapped)
    if not d.IsDone():
        raise RuntimeError("distance failed")
    return float(d.Value())


def planar_faces(shape):
    return [f for f in shape.faces() if f.geom_type.name == "PLANE"]


def face_normal(face):
    n = face.normal_at(face.center())
    return np.array([n.X, n.Y, n.Z])


def identify(asm):
    """Assembly solids identified by measurement (plan §2): the housing is the 100 × 100
    solid with four Ø4.0 bores; OD-G10 the one longer than 120; OD-G04 the rest."""
    out = {}
    for s in solid_list(asm):
        e = env_of(s)
        sizes = (e["size_x"], e["size_y"], e["size_z"])
        if abs(sizes[0] - 100.0) < 0.1 and abs(sizes[1] - 100.0) < 0.1:
            out.setdefault("housing", []).append(s)
        elif max(sizes) > 120.0:
            out.setdefault("g10", []).append(s)
        else:
            out.setdefault("g04", []).append(s)
    if any(len(out.get(k, [])) != 1 for k in ("housing", "g04", "g10")):
        raise RuntimeError(f"assembly solids not identified: { {k: len(v) for k, v in out.items()} }")
    return out["housing"][0], out["g04"][0], out["g10"][0]


def underside_faces(rig):
    """The plate's underside: the planar face(s) facing −Y between y 130 and 140."""
    return [f for f in planar_faces(rig) if face_normal(f)[1] < -0.999 and 130.0 < f.center().Y < 140.0]


def seat_y_of(rig) -> float:
    """The measured y of the one underside plane: the housing joint's datum."""
    under = underside_faces(rig)
    if len(under) != 1:
        raise RuntimeError(f"{len(under)} underside faces")
    return float(under[0].center().Y)


# ---- context -------------------------------------------------------------------------------
class Ctx:
    def __init__(self, step, stl=None, params=None, mesh_meta=None):
        self.step, self.stl, self.params = Path(step), (Path(stl) if stl else None), params
        self.mesh_meta = Path(mesh_meta) if mesh_meta else None
        self.rig_shape = read_step(self.step)
        sols = solid_list(self.rig_shape)
        self.rig = sols[0] if len(sols) == 1 else self.rig_shape
        self.env = env_of(self.rig)
        housing, g04, g10 = identify(read_step(ASSEMBLY_IN))
        self.seat_y = self.measure_seat_y()
        pose = housing_pose(self.seat_y)
        self.housing, self.g04, self.g10 = pose * housing, pose * g04, pose * g10
        self.census = bore_census(self.rig)
        self._wall = None

    def measure_seat_y(self) -> float:
        self.underside = underside_faces(self.rig)
        return seat_y_of(self.rig)

    def wall(self):
        if self._wall is None:
            self._wall = min_wall(self.rig)
        return self._wall


# ---- predicates ----------------------------------------------------------------------------
@guarded
def exactly_one_solid(c):
    return [row("exactly_one_solid", gate("exactly_one_solid", solid_count(c.rig_shape), "==", 1, band=B_N))]


@guarded
def u01_validity(c):
    v = validity(c.rig_shape)
    return [row("U-01", gate("U-01", v["solid_count"], "==", 1, band=B_N), "solid_count"),
            row("U-01", gate("U-01", v["brep_valid"], "==", 1, band=B_N), "brep_valid"),
            row("U-01", gate("U-01", v["naked_edges"], "==", 0, band=B_N), "naked_edges")]


@guarded
def u02_envelope(c):
    e, out = envelope(c.rig), []
    for k, s in zip(("size_x", "size_y", "size_z"), SPEC["env_size"]):
        g = gate("U-02", e[k], "in", (s - SPEC["env_tol"], s + SPEC["env_tol"]), band=B_MM)
        out.append(row("U-02", g, k))
        out.append(row("envelope_within_spec", g, f"size {k}"))
    for k, s in SPEC["env_pos"].items():
        g = gate("envelope_within_spec", e[k], "in", (s - SPEC["env_tol"], s + SPEC["env_tol"]), band=B_MM)
        out.append(row("envelope_within_spec", g, f"position {k} (reported apart)"))
    return out


@guarded
def u03a_close(c):
    out = []
    contact = clearance(c.rig, c.housing)
    out.append(row("U-03a", gate("U-03a", contact, "==", 0.0, band=B_MM),
                   f"designed contact rig|housing, nearest point y {contact.at[1] if contact.at else None}"))
    hmax = res("housing_max_y", env_of(c.housing)["max_y"], "mm")
    out.append(row("U-03a", gate("U-03a", hmax, "<=", c.seat_y, band=B_MM),
                   "posed housing reaches no higher than the measured plate underside"))
    inter = interference({"rig": c.rig, "housing": c.housing, "g04": c.g04})
    for key in ("rig|housing", "rig|g04"):
        out.append(row("U-03a", gate("U-03a", inter[key], "<=", 0.0, band=B_MM3), f"interference {key}"))
    # rig away from the contact plane: everything of the rig below the plate underside
    from build123d import Box
    below = c.rig & Pos(0, (c.seat_y - 0.01) / 2 - 1.0, 0) * Box(400, c.seat_y - 0.01 + 2.0, 200)
    el = clearance(below, c.housing)
    out.append(row("U-03a", gate("U-03a", el, ">=", SPEC["clear_min"], band=B_MM),
                   "rig below y 135 (walls, chamfers, base) to housing"))
    for nm, part in (("g04", c.g04), ("g10", c.g10)):
        cl = clearance(c.rig, part)
        out.append(row("U-03a", gate("U-03a", cl, ">=", SPEC["clear_min"], band=B_MM), f"clearance rig|{nm}"))
        if nm == "g10":
            ins = res("g10_inside", int(cl.detail["inside"]), "bool")
            out.append(row("U-03a", gate("U-03a", ins, "==", 0, band=B_N), "OD-G10 fallback: not inside"))
    return out


@guarded
def u03b_offer_up(c):
    lo, hi, st = SPEC["offer_up"]
    worst_i, worst_g = None, None
    for dy in frange(lo, hi, st):
        h, g4, g10 = moved(c.housing, dy=-dy), moved(c.g04, dy=-dy), moved(c.g10, dy=-dy)
        inter = interference({"rig": c.rig, "housing": h, "g04": g4})
        for key in ("rig|housing", "rig|g04"):
            r = inter[key]
            if not r.ok:
                return [row("U-03b", gate("U-03b", r, "<=", 0.0, band=B_MM3), f"{key} at dy -{dy}")]
            if worst_i is None or r.measured > worst_i[0].measured:
                worst_i = (r, f"{key} at dy -{dy:g}")
        cl = clearance(c.rig, g10)
        if cl.detail["inside"]:
            cl = res("clearance", 0.0, "mm", at=cl.at)
        if worst_g is None or cl.measured < worst_g[0].measured:
            worst_g = (cl, f"rig|g10 clearance (fallback, > 0 and not inside) at dy -{dy:g}")
    return [row("U-03b", gate("U-03b", worst_i[0], "<=", 0.0, band=B_MM3), "worst " + worst_i[1]),
            row("U-03b", gate("U-03b", worst_g[0], ">=", 2 * B_MM, band=B_MM,
                              required="> 0 (read beyond the 0.005 band)"), "worst " + worst_g[1])]


@guarded
def u04_roundtrip(c):
    if c.params is None:
        return [row("U-04", gate("U-04", inconclusive("step_roundtrip", "bool", "no build params given"),
                                 "==", 1, band=B_N))]
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_od_t01_rig_v02 as b
    shape = b.build(b.Params(**c.params))
    cs = compare_step(shape, c.step)
    out = [row("U-04", gate("U-04", cs["schema"], "==", 1, band=B_N), "schema AP242"),
           row("U-04", gate("U-04", cs["solids"], "==", 1, band=B_N), "solids"),
           row("U-04", gate("U-04", cs["volume_delta"], "<=", 0.0, band=B_MM3), "volume delta"),
           row("U-04", gate("U-04", cs["faces_delta"], "==", 0, band=B_N), "faces delta"),
           row("U-04", gate("U-04", cs["labels"], "==", 1, band=B_N),
               f"labels {cs['labels'].detail.get('reimported')}"),
           row("U-04", gate("U-04", cs["valid_after"], "==", 1, band=B_N), "valid after re-import")]
    named = res("named_body", int("od_t01_rig" in (cs["labels"].detail.get("reimported") or [])), "bool")
    out.append(row("U-04", gate("U-04", named, "==", 1, band=B_N), "body named od_t01_rig"))
    shells_all, shells_in = 0, 0
    ex = TopExp_Explorer(c.rig_shape.wrapped, TopAbs_SHELL)
    while ex.More():
        shells_all += 1
        ex.Next()
    for s in solid_list(c.rig_shape):
        ex = TopExp_Explorer(s.wrapped, TopAbs_SHELL)
        while ex.More():
            shells_in += 1
            ex.Next()
    stray = res("stray_shells", shells_all - shells_in, "count")
    out.append(row("U-04", gate("U-04", stray, "==", 0, band=B_N), "stray shells"))
    return out


@guarded
def u05_census(c):
    want, out = SPEC["census"], []
    fc = feature_census(c.rig)
    for key, name in (("planar_faces", "plane_faces"), ("cylinder_faces", "cylinder_faces"),
                      ("concave_cylinders", "concave_cylinders"),
                      ("convex_cylinders", "convex_cylinders"), ("bores", "bores")):
        r = fc.get(name)
        if r is None:
            r = inconclusive(name, "count", f"feature_census has no {name}: {list(fc)}")
        out.append(row("U-05", gate("U-05", r, "==", want[key], band=B_N), key))
        out.append(row("feature_census", gate("feature_census", r, "==", want[key], band=B_N), key))
    other = sum(v.measured for k, v in fc.items()
                if k.endswith("_faces") and k not in ("plane_faces", "cylinder_faces"))
    g = gate("U-05", res("other_faces", other, "count"), "==", 0, band=B_N)
    out += [row("U-05", g, "other face kinds"), row("feature_census", g, "other face kinds")]
    bores = c.census.detail["bores"]
    for d, n in want["bores_by_d"].items():
        got = sum(1 for bo in bores if abs(bo["diameter"] - d) < 0.5 and abs(bo["axis_dir"][1]) > 0.999)
        g = gate("U-05", res("bores_d", got, "count"), "==", n, band=B_N)
        out += [row("U-05", g, f"bores along Y of Ø{d:g}"), row("feature_census", g, f"bores Ø{d:g}")]
    planes = planar_faces(c.rig)
    cham = [f for f in planes if abs(face_normal(f)[2]) < 1e-6
            and abs(abs(face_normal(f)[0]) - math.sqrt(0.5)) < 1e-6]
    g = gate("U-05", res("chamfer_planes", len(cham), "count"), "==", want["chamfer_planes"], band=B_N)
    out += [row("U-05", g, "45° corner chamfer planes"), row("feature_census", g, "corner chamfers")]
    walls = [f for f in planes if abs(abs(face_normal(f)[0]) - 1) < 1e-9 and abs(abs(f.center().X) - 75.0) < 1.0]
    g = gate("U-05", res("wall_inner_faces", len(walls), "count"), "==", want["wall_inner_faces"], band=B_N)
    out += [row("U-05", g, "wall inner faces"), row("feature_census", g, "walls")]
    for f in walls:
        bb = f.bounding_box()
        g = gate("U-05", res("wall_z_max", bb.max.Z, "mm", at=(f.center().X, f.center().Y, f.center().Z)),
                 "in", (want["wall_z"][1] - SPEC["env_tol"], want["wall_z"][1] + SPEC["env_tol"]), band=B_MM)
        out.append(row("U-05", g, f"wall x {f.center().X:+.1f} ends at z +40"))
        g = gate("U-05", res("wall_z_min", bb.min.Z, "mm"), "in",
                 (want["wall_z"][0] - SPEC["env_tol"], want["wall_z"][0] + SPEC["env_tol"]), band=B_MM)
        out.append(row("U-05", g, f"wall x {f.center().X:+.1f} starts at z -60"))
    return out


@guarded
def walls_and_features(c):
    w = c.wall()
    out = [row("D-01a", gate("D-01a", w, ">=", SPEC["wall_floor"], band=B_MM)),
           row("D-01b", gate("D-01b", w, ">=", SPEC["wall_struct"], band=B_MM, assumes=["A-08"])),
           row("D-06a", gate("D-06a", w, ">=", SPEC["min_feature"], band=B_MM))]
    wide = w.detail.get("wide") if w.ok else None
    if isinstance(wide, dict):
        wv = res("min_wall_wide", wide.get("mm", wide.get("measured")), "mm", at=wide.get("at"))
    elif wide is not None:
        wv = res("min_wall_wide", float(wide), "mm")
    else:
        wv = inconclusive("min_wall_wide", "mm", w.reason or "no wide reading")
    out.append(row("U-06", gate("U-06", wv, ">=", SPEC["wide_soft"], band=B_MM), "Soft"))
    return out


@guarded
def u07_mesh(c):
    out = []
    radii = [bo["diameter"] / 2 for bo in c.census.detail["bores"]]
    r_max = max(radii)
    a_lim = 4 * math.acos(1 - SPEC["stl_tol"] / r_max)
    stl_meta = None
    if c.stl is not None and c.mesh_meta is not None and c.mesh_meta.exists():
        stl_meta = json.loads(c.mesh_meta.read_text())
    if stl_meta is None:
        return [row("U-07", gate("U-07", inconclusive("stl", "mm", "no STL or mesh record"), "<=",
                                 SPEC["stl_tol"], band=B_MM))]
    tol = res("stl_tolerance", stl_meta["tolerance_mm"], "mm")
    ang = res("stl_angular", stl_meta["angular_tolerance_rad"], "rad")
    out.append(row("U-07", gate("U-07", tol, "<=", SPEC["stl_tol"], band=B_MM), "chordal tolerance"))
    out.append(row("U-07", gate("U-07", ang, "<=", a_lim, band=0.00002),
                   f"angular tolerance, limit 4·acos(1 - 0.01/{r_max:.3f})"))
    with tempfile.TemporaryDirectory() as tmp:     # re-mesh the re-imported STEP the same way
        w = write_stl(c.rig, Path(tmp) / "remesh.stl", tolerance=stl_meta["tolerance_mm"],
                      angular_tolerance=stl_meta["angular_tolerance_rad"])
    out.append(row("U-07", gate("U-07", w.checks["max_sagitta"], "<=", SPEC["stl_tol"], band=B_MM),
                   f"stl_max_sagitta (re-meshed from the STEP: {w.detail.get('triangles')} triangles; "
                   f"delivered STL {stl_meta.get('triangles')})"))
    mc = mesh_census(c.stl)
    for k, op, lim in (("bodies", "==", 1), ("naked_edges", "==", 0), ("winding", "==", 1)):
        if k in mc:
            out.append(row("U-07", gate("U-07", mc[k], op, lim, band=B_N), f"delivered STL {k} (corroboration)"))
    return out


@guarded
def d02_bed(c):
    out = []
    for k, lim in zip(("size_x", "size_y", "size_z"), SPEC["build_volume"]):
        out.append(row("D-02", gate("D-02", res(k, c.env[k], "mm"), "<=", lim, band=B_MM, assumes=["A-09"]),
                       {"size_x": "bed X", "size_y": "bed Y", "size_z": "height (build +Z)"}[k]))
    return out


def screw_holes_measured(rig, seat_y):
    """The four Ø3.4 holes as measured: (axis x, axis z, y0, y1, radius) of each."""
    out = []
    census = bore_census(rig)
    for (x, z) in SPEC["screw_xz"]:
        loc = locate_bore(census, (x, seat_y + 1.5, z), (0, 1, 0))
        st, en = loc["diameter"].detail["start"], loc["diameter"].detail["end"]
        out.append((st[0], st[2], min(st[1], en[1]), max(st[1], en[1]), loc["diameter"].measured / 2))
    return out


def fill_crowns(rig, holes):
    """Census copy for D-03a: the four Ø3.4 holes filled (Ø3.6, from the plate underside to
    the counterbore floor, both measured), so their crowns, the named exception, drop out."""
    filled = rig
    for (cx, cz, y0, y1, _r) in holes:
        filled = filled + probe_cyl(cx, cz, 3.6, y0, y1)
    return filled


@guarded
def d03a_overhang(c):
    out = []
    holes_m = screw_holes_measured(c.rig, c.seat_y)
    filled = fill_crowns(c.rig, holes_m)
    n = solid_count(filled)
    out.append(row("D-03a", gate("D-03a", n, "==", 1, band=B_N), "census copy is one solid"))
    oc = overhang_census(filled, BUILD_DIR, min_deg=SPEC["overhang_min"])
    out.append(row("D-03a", gate("D-03a", oc, ">=", SPEC["overhang_min"], band=B_DEG, assumes=["A-10"]),
                   f"least downward angle, Ø3.4 crowns excluded by position; per kind "
                   f"{oc.detail.get('per_kind_least_deg') if oc.ok else None}"))
    raw = overhang_census(c.rig, BUILD_DIR, min_deg=SPEC["overhang_min"])
    at = raw.at
    near = None
    if raw.ok and at is not None:
        p = np.array(at, float)
        # located against the measured hole axes and ends (v01 used the nominal ones, REPORT v01 §4 note 1)
        hit = [(math.hypot(p[0] - cx, p[2] - cz), y0, y1, r) for (cx, cz, y0, y1, r) in holes_m]
        near, y0, y1, r = min(hit)
        inside = near <= r + B_MM and y0 - B_MM <= p[1] <= y1 + B_MM
    else:
        inside = False
    exc = res("crown_exception_located", int(inside), "bool", at=at)
    out.append(row("D-03a", gate("D-03a", exc, "==", 1, band=B_N),
                   f"exception: unfilled least {raw.measured if raw.ok else None} deg at {at}, "
                   f"{near if near is None else round(near, 3)} mm off a screw axis"))
    out.append({"gate": "D-03a", "measured": raw.measured if raw.ok else None, "unit": "deg",
                "required": "reported (named exception)", "margin": None, "at": str(at),
                "status": "REPORTED", "method": "overhang_census", "assumes": [],
                "note": "least angle at the Ø3.4 crowns, the named exception"})
    return out


@guarded
def d03b_bridge(c):
    fs = flat_ceiling_spans(c.rig, BUILD_DIR, max_span=SPEC["bridge_max"])
    out = [row("D-03b", gate("D-03b", fs, "<=", SPEC["bridge_max"], band=B_MM),
               "flat_ceiling_spans corroboration; reviewer row from sections")]
    ds = [locate_bore(c.census, (x, 136.5, z), (0, 1, 0))["diameter"] for x, z in SPEC["screw_xz"]]
    worst = max(ds, key=lambda r: r.measured if r.ok else 1e9)
    out.append(row("D-03b", gate("D-03b", worst, "<=", SPEC["crown_bridge_max"] + SPEC["screw_d"][1], band=B_MM),
                   "crown chord = the measured Ø3.4 hole diameter (≤ 3.4 designed, ≤ 5 limit)"))
    return out


@guarded
def holes(c):
    out = []
    lim_lo, lim_hi = SPEC["screw_d"][0] - SPEC["screw_d"][1], SPEC["screw_d"][0] + SPEC["screw_d"][1]
    hb = bore_census(c.housing)
    for (x, z) in SPEC["screw_xz"]:
        tag = f"({x:+.0f}, {z:+.0f})"
        # the posed insert bore's axis, measured on the housing
        ins = locate_bore(hb, (x, c.seat_y - 2.0, z), (0, 1, 0))
        ist = ins["diameter"].detail["start"]
        ip = (ist[0], c.seat_y + 1.5, ist[2])
        h = locate_bore(c.census, ip, (0, 1, 0))
        out.append(row("D-04a", gate("D-04a", h["diameter"], ">=", SPEC["screw_d_min"], band=B_MM), f"screw hole {tag}"))
        out.append(row("REQ-01", gate("REQ-01", h["diameter"], "in", (lim_lo, lim_hi), band=B_MM, assumes=["A-01"]),
                       f"Ø3.4 {tag}"))
        out.append(row("REQ-01", gate("REQ-01", h["offset"], "<=", SPEC["offset_max"], band=B_MM, assumes=["A-01"]),
                       f"Ø3.4 {tag} axis offset from the posed insert bore (Ø{ins['diameter'].measured:.2f})"))
        st, en = h["diameter"].detail["start"], h["diameter"].detail["end"]
        y0 = res("hole_y0", min(st[1], en[1]), "mm")
        out.append(row("REQ-01", gate("REQ-01", y0, "in", (c.seat_y - B_MM, c.seat_y + B_MM), band=B_MM,
                                      assumes=["A-01"]), f"Ø3.4 {tag} opens at the plate underside"))
        out.append(row("REQ-01", gate("REQ-01", h["through"], "==", 1, band=B_N, assumes=["A-01"]),
                       f"Ø3.4 {tag} through into the counterbore"))
        cb = locate_bore(c.census, (ip[0], (SPEC["cbore_top_y"] + SPEC["cbore_floor_y"][0]) / 2, ip[2]), (0, 1, 0))
        out.append(row("REQ-01", gate("REQ-01", cb["diameter"], "in",
                                      (SPEC["cbore_d"][0] - SPEC["cbore_d"][1], SPEC["cbore_d"][0] + SPEC["cbore_d"][1]),
                                      band=B_MM, assumes=["A-01"]), f"Ø6.5 counterbore {tag}"))
        out.append(row("REQ-01", gate("REQ-01", cb["offset"], "<=", SPEC["offset_max"], band=B_MM, assumes=["A-01"]),
                       f"counterbore {tag} coaxial with the posed insert bore"))
        st, en = cb["diameter"].detail["start"], cb["diameter"].detail["end"]
        top, floor = max(st[1], en[1]), min(st[1], en[1])
        out.append(row("REQ-01", gate("REQ-01", res("cbore_top_y", top, "mm"), "in",
                                      (SPEC["cbore_top_y"] - SPEC["env_tol"], SPEC["cbore_top_y"] + SPEC["env_tol"]),
                                      band=B_MM, assumes=["A-01"]), f"counterbore {tag} from the top face"))
        f0, ft = SPEC["cbore_floor_y"]
        out.append(row("REQ-01", gate("REQ-01", res("cbore_floor_y", floor, "mm"), "in", (f0 - ft, f0 + ft),
                                      band=B_MM, assumes=["A-01"]), f"counterbore {tag} floor"))
        u0, ut = SPEC["under_head"]
        out.append(row("REQ-01", gate("REQ-01", res("plate_under_head", floor - c.seat_y, "mm"), "in",
                                      (u0 - ut, u0 + ut), band=B_MM, assumes=["A-01"]),
                       f"plate under the head {tag} (floor − measured underside)"))
    for (x, z) in SPEC["bench_xz"]:
        tag = f"({x:+.0f}, {z:+.0f})"
        h = locate_bore(c.census, (x, 5.0, z), (0, 1, 0))
        out.append(row("D-04a", gate("D-04a", h["diameter"], ">=", SPEC["bench_d_min"], band=B_MM), f"bench hole {tag}"))
        d0, dt = SPEC["bench_d"]
        out.append(row("REQ-06", gate("REQ-06", h["diameter"], "in", (d0 - dt, d0 + dt), band=B_MM, assumes=["A-11"]),
                       f"Ø4.5 {tag}"))
        out.append(row("REQ-06", gate("REQ-06", h["offset"], "<=", SPEC["offset_max"], band=B_MM, assumes=["A-11"]),
                       f"Ø4.5 {tag} axis offset"))
        out.append(row("REQ-06", gate("REQ-06", h["through"], "==", 1, band=B_N, assumes=["A-11"]), f"Ø4.5 {tag} through"))
    return out


@guarded
def req02_seat(c):
    out = []
    n = res("underside_faces", len(c.underside), "count")
    out.append(row("REQ-02", gate("REQ-02", n, "==", 1, band=B_N, assumes=["A-01"]), "one underside plane"))
    y = res("underside_y", c.seat_y, "mm")
    s0, st = SPEC["seat_y"], SPEC["seat_tol"]
    out.append(row("REQ-02", gate("REQ-02", y, "in", (s0 - st, s0 + st), band=B_MM, assumes=["A-01"]), "underside y"))
    face = c.underside[0]
    pts = [(sx * 50.0, c.seat_y, sz * 50.0) for sx in (-1, 0, 1) for sz in (-1, 0, 1) if (sx, sz) != (0, 0)]
    worst = max(point_face_distance(face, p) for p in pts)
    out.append(row("REQ-02", gate("REQ-02", res("square_off_face", worst, "mm"), "<=", 0.0, band=B_MM,
                                  assumes=["A-01"]),
                   "the housing square's corners and edge midpoints (x ±50, z ±50) lie on that face"))
    return out


@guarded
def req03_window(c):
    out = []
    w = locate_bore(c.census, (0.0, (c.seat_y + c.env["max_y"]) / 2, 0.0), (0, 1, 0))
    r0, rt = SPEC["window_r"]
    out.append(row("REQ-03", gate("REQ-03", w["diameter"], "in", (2 * (r0 - rt), 2 * (r0 + rt)), band=B_MM,
                                  assumes=["A-05"]), "window diameter (R 30.0 ± 0.1)"))
    out.append(row("REQ-03", gate("REQ-03", w["offset"], "<=", SPEC["offset_max"], band=B_MM, assumes=["A-05"]),
                   "window on the axis"))
    out.append(row("REQ-03", gate("REQ-03", w["through"], "==", 1, band=B_N, assumes=["A-05"]), "window through the plate"))
    flanks = [f for f in planar_faces(c.rig) if abs(face_normal(f)[1]) < 1e-9 and face_normal(f)[2] < -0.1
              and abs(f.center().X) < r0 + 1 and 0 < f.center().Z < 45
              and c.seat_y - 1 < f.center().Y < c.env["max_y"] + 1]
    out.append(row("REQ-03", gate("REQ-03", res("window_flanks", len(flanks), "count"), "==", 2, band=B_N,
                                  assumes=["A-05"]), "two roof flanks"))
    a0, at = SPEC["roof_deg"]
    for f in flanks:
        n = face_normal(f)
        ang = math.degrees(math.acos(max(-1.0, min(1.0, -n[2]))))
        out.append(row("REQ-03", gate("REQ-03", res("roof_deg", ang, "deg", at=tuple(f.center())), "in",
                                      (a0 - at, a0 + at), band=B_DEG, assumes=["A-05"]),
                       f"roof flank x {f.center().X:+.1f} angle from horizontal"))
    ymid = (c.seat_y + c.env["max_y"]) / 2
    apex = radial_extent(c.rig, (0.0, ymid, 0.0), (0, 1, 0), (0, 0, 1), 0.0, 0.0, side="inner",
                         r_min=0.0, r_max=None)
    z0, zt = SPEC["window_apex_z"]
    out.append(row("REQ-03", gate("REQ-03", apex, "in", (z0 - zt, z0 + zt), band=B_MM, assumes=["A-05"]),
                   f"roof apex z (radial_extent along +Z at y {ymid:.2f})"))
    g4 = clearance(c.rig, c.g04)
    out.append(row("REQ-03", gate("REQ-03", g4, ">=", SPEC["clear_min"], band=B_MM, assumes=["A-05"]),
                   "OD-G04 (hub tube included) to the rig"))
    hb = bore_census(c.housing)
    pairb = [bo for bo in hb.detail["bores"] if abs(bo["diameter"] - 3.8) < 0.15
             and 15.0 < math.hypot(bo["start"][0], bo["start"][2]) < 23.0]
    out.append(row("REQ-03", gate("REQ-03", res("pairb_axes", len(pairb), "count"), "==", 2, band=B_N,
                                  assumes=["A-12"]), "pair-B screw axes found on the posed housing"))
    for bo in pairb:
        x, z = bo["start"][0], bo["start"][2]
        probe = probe_cyl(x, z, 0.002, c.seat_y, c.env["max_y"])
        d = clearance(c.rig, probe)
        dist = res("pairb_axis_to_window", d.measured + 0.001, "mm", at=d.at) if d.ok else d
        out.append(row("REQ-03", gate("REQ-03", dist, ">=", SPEC["pairb_axis_min"], band=B_MM, assumes=["A-12"]),
                       f"pair-B axis (x {x:+.2f}, z {z:+.2f}, r {math.hypot(x, z):.2f}) to the window face"))
    return out


@guarded
def req04_travel(c):
    out = []
    lo, hi, st = SPEC["phi_a"]
    worst = None
    for phi in frange(lo, hi, st):
        cl = clearance(c.rig, moved(c.g10, phi=phi))
        if cl.detail["inside"]:
            cl = res("clearance", 0.0, "mm", at=cl.at)
        if worst is None or cl.measured < worst[0].measured:
            worst = (cl, phi)
    out.append(row("REQ-04", gate("REQ-04", worst[0], ">=", SPEC["clear_a"], band=B_MM, assumes=["A-07"]),
                   f"(a) least clearance over φ {lo:g} … {hi:+g} step {st:g}, at φ {worst[1]:+g}"))
    sign = res("phi_sign", int(env_of(moved(c.g10, phi=15.0))["max_x"] > env_of(c.g10)["max_x"]), "bool")
    out.append(row("REQ-04", gate("REQ-04", sign, "==", 1, band=B_N), "φ > 0 turns the handle toward +X"))
    lo, hi, st = SPEC["dz_b"]
    worst = None
    for dz in frange(lo, hi, st):
        cl = clearance(c.rig, moved(c.g10, phi=SPEC["phi_b"], dy=-SPEC["drop_b"], dz=dz))
        if cl.detail["inside"]:
            cl = res("clearance", 0.0, "mm", at=cl.at)
        if worst is None or cl.measured < worst[0].measured:
            worst = (cl, dz)
    out.append(row("REQ-04", gate("REQ-04", worst[0], ">=", 2 * B_MM, band=B_MM, assumes=["A-07"],
                                  required="> 0, not inside (fallback for interference <= 0)"),
                   f"(b) least clearance over dz 0 … 200 step 5 at φ -50, dy -15: at dz {worst[1]:g}"))
    return out


@guarded
def req05_headroom(c):
    tops = [f for f in planar_faces(c.rig) if face_normal(f)[1] > 0.999 and 5.0 < f.center().Y < 15.0]
    if len(tops) != 1:
        raise RuntimeError(f"{len(tops)} base-top faces")
    base_top = tops[0].center().Y
    low = env_of(c.g10)["min_y"]
    h = res("headroom", low - base_top, "mm", at=(None, low, None))
    return [row("REQ-05", gate("REQ-05", h, ">=", SPEC["headroom"], band=B_MM, assumes=["A-07"]),
                f"OD-G10 lowest y {low:.3f} − base top y {base_top:.3f}")]


@guarded
def probes(c):
    out = []
    d, y0, y1 = SPEC["bench_probe"]
    for i, (x, z) in enumerate(SPEC["bench_xz"]):
        r = interference({"rig": c.rig, "probe": probe_cyl(x, z, d, y0, y1)})["rig|probe"]
        out.append(row("REQ-06", gate("REQ-06", r, "<=", 0.0, band=B_MM3, assumes=["A-11"]),
                       f"Ø8 driver probe y 10 … 300 at ({x:+.0f}, {z:+.0f})"))
    d, y0, y1 = SPEC["screw_probe"]
    for (x, z) in SPEC["screw_xz"]:
        r = interference({"rig": c.rig, "probe": probe_cyl(x, z, d, y0, y1)})["rig|probe"]
        out.append(row("REQ-07", gate("REQ-07", r, "<=", 0.0, band=B_MM3),
                       f"Ø6 probe y {y0:g} … {y1:g} at ({x:+.0f}, {z:+.0f})"))
    return out


@guarded
def req08_section(c):
    """REQ-08 is Soft and not geometric. Report §4's hand numbers against the plate's
    section measured on the re-imported STEP at the plane x 0 (through the hub window):
    area, centroid, second moment about the Z-parallel axis through the centroid, the
    section modulus Z = I / c_max, and σ = M / Z with §4's M. Reported, never gated."""
    from build123d import Box
    from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
    from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeFace
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    from OCP.gp import gp_Dir, gp_Pln
    ytop = c.env["max_y"]
    plate = c.rig & Pos(0, (c.seat_y + ytop) / 2, 0) * Box(400, ytop - c.seat_y, 400)
    pln = gp_Pln(gp_Pnt(0, 0, 0), gp_Dir(1, 0, 0))
    big = BRepBuilderAPI_MakeFace(pln, -500, 500, -500, 500).Face()
    from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
    com = BRepAlgoAPI_Common(plate.wrapped, big)
    com.Build()
    if not com.IsDone():
        raise RuntimeError("section at x 0 failed")
    props = GProp_GProps()
    BRepGProp.SurfaceProperties_s(com.Shape(), props)
    area = props.Mass()
    if not area > 0:
        raise RuntimeError("empty section at x 0")
    cg = props.CentreOfMass()
    mat = props.MatrixOfInertia()        # about the centroid; element (y, y) is ∫(x² + z²), (z, z) ∫(x² + y²)
    # on the plane x 0: I about the Z-parallel axis through the centroid = ∫ (y − yc)² dA = Izz (x ≡ 0)
    i_z = mat.Value(3, 3)
    from OCP.Bnd import Bnd_Box
    from OCP.BRepBndLib import BRepBndLib
    bb = Bnd_Box()
    BRepBndLib.Add_s(com.Shape(), bb)
    _x0, ymin, zmin, _x1, ymax, zmax = bb.Get()
    cmax = max(ymax - cg.Y(), cg.Y() - ymin)
    zmod = i_z / cmax
    sigma = SPEC["hand_M_Nmm"] / zmod
    rows = []
    for name, val, unit, hand in (("section_area", area, "mm2", None), ("section_centroid_y", cg.Y(), "mm", None),
                                  ("section_I", i_z, "mm4", None), ("section_modulus_Z", zmod, "mm3", SPEC["hand_Z_mm3"]),
                                  ("sigma_at_M", sigma, "MPa", SPEC["hand_sigma_MPa"]),
                                  ("factor_vs_PLA", SPEC["pla_MPa"] / sigma, "-", None)):
        rows.append({"gate": "REQ-08", "measured": round(val, 4), "unit": unit, "required": "reported (Soft, bench)",
                     "margin": None, "at": "plane x 0, plate y %.2f … %.2f" % (ymin, ymax), "status": "REPORTED",
                     "method": "section x 0 (BRepGProp)", "assumes": ["A-02"],
                     "note": f"{name}" + (f"; §4 hand value {hand:g}" if hand is not None else "")})
    return rows


def not_applicable(c):
    rows = []
    for gid, why in (("U-08", "no threads (row N/A)"), ("D-07", "clearance holes only (row N/A)"),
                     ("J-05", "no threaded holes in this part (row N/A)")):
        rows.append({"gate": gid, "measured": None, "unit": "", "required": "N/A", "margin": None, "at": None,
                     "status": "N/A", "method": "-", "assumes": [], "note": why})
    rows.append({"gate": "REQ-08", "measured": None, "unit": "", "required": "Soft, bench", "margin": None,
                 "at": None, "status": INCONCLUSIVE, "method": "-", "assumes": ["A-02"],
                 "note": "not geometric; §4 hand calculation (spec 1.3) σ ≈ 9.6 MPa vs ≈ 40 MPa, factor ≈ 4.2; "
                         "measured section at x 0 in the REQ-08 section rows; answered by the first test"})
    return rows


PREDICATES = [exactly_one_solid, u01_validity, u02_envelope, u03a_close, u03b_offer_up, u04_roundtrip,
              u05_census, walls_and_features, u07_mesh, d02_bed, d03a_overhang, d03b_bridge, holes,
              req02_seat, req03_window, req04_travel, req05_headroom, probes, req08_section]


def summarise(rows):
    order = {FAIL: 0, INCONCLUSIVE: 1, PASS_ASSUMED: 2, PASS: 3}
    by = {}
    for r in rows:
        if r["status"] in ("REPORTED", "N/A"):
            by.setdefault(r["gate"], r["status"])
            continue
        cur = by.get(r["gate"])
        if cur in (None, "REPORTED", "N/A") or order.get(r["status"], 1) < order.get(cur, 3):
            by[r["gate"]] = r["status"]
    return by


def run(step, stl=None, params=None, only=None, mesh_meta=None):
    t0 = time.time()
    c = Ctx(step, stl, params, mesh_meta)
    rows, timing = [], {}
    for p in PREDICATES:
        if only and p.__name__ not in only:
            continue
        t = time.time()
        rows += p(c)
        timing[p.__name__] = round(time.time() - t, 1)
    rows += not_applicable(c)
    return {"step": str(step), "seat_y": c.seat_y, "rows": rows, "summary": summarise(rows),
            "timing_s": timing, "total_s": round(time.time() - t0, 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", required=True)
    ap.add_argument("--stl")
    ap.add_argument("--params")
    ap.add_argument("--out")
    ap.add_argument("--mesh-meta", help="the mesh record the build writes beside its params")
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    params = json.loads(Path(a.params).read_text())["params"] if a.params else None
    out = run(a.step, a.stl, params, a.only, a.mesh_meta)
    text = json.dumps(out, indent=1, default=str)
    if a.out:
        Path(a.out).write_text(text)
    for r in out["rows"]:
        print(f"{r['gate']:<20} {r['status']:<13} {r['measured']!s:<22} {r.get('required', '')!s:<28} "
              f"{r.get('note', '')} {r.get('reason', '')}")
    print(json.dumps(out["summary"], indent=0))
    print("timing", out["timing_s"], "total", out["total_s"])


if __name__ == "__main__":
    main()
