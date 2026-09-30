"""Checks for od_c04_mount (job 20260930-od-c04-thermoblock-mount, concept C1).

Written before the build (PLAYBOOK D3). Every predicate measures the re-imported
STEP files with tools.core / tools.measure and compares through tools.result.gate
with the GATES.md section 0 band. Thresholds come from DESIGN_SPEC.md 1.1 section 5
only (the SPEC table below cites the row of each value). Any exception or missing
value gives INCONCLUSIVE.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/check_od_c04_mount.py \
        --step 02_STEP_STL/od_c04_mount_C1_v01.step \
        --asm 02_STEP_STL/od_c04_assembly_C1_v01.step \
        --stl 02_STEP_STL/od_c04_mount_C1_v01.stl \
        --out 01_CAD/check_v01/check_results_v01.json [--variant '{"tip_z": -10.0}']
Relative paths are taken from the job workspace (the folder above 01_CAD).
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

from build123d import CenterOf, Cylinder, GeomType, Pos  # noqa: E402
from OCP.BRepAdaptor import BRepAdaptor_Surface  # noqa: E402

from tools.core import compare_step, common_volume, read_step, validity, write_stl  # noqa: E402
from tools.core.step import file_sha256  # noqa: E402
from tools.measure import (bore_census, clearance, envelope, feature_census, locate_bore,  # noqa: E402
                           mesh_census, min_wall, min_wall_wide, overhang_census, radial_profile)
from tools.result import INCONCLUSIVE, MEASURED, Result, gate, inconclusive  # noqa: E402

# ---------------------------------------------------------------------------
# Section 5 thresholds (spec 1.1) and the GATES.md section 0 bands. Nothing below
# this table carries a threshold.
# ---------------------------------------------------------------------------
BAND = {"mm": 0.005, "deg": 0.001, "mm3": 0.001, "count": 0, "bool": 0}
SPEC = {
    # U-02 envelope 100.0 x 110.0 x 50.0, each in [spec - 0.1, spec + 0.1]; position x +-50, y -70..40, z -17..33
    "size": {"size_x": 100.0, "size_y": 110.0, "size_z": 50.0},
    "size_tol": 0.1,
    "position": {"min_x": -50.0, "max_x": 50.0, "min_y": -70.0, "max_y": 40.0, "min_z": -17.0, "max_z": 33.0},
    # D-02 (A-09): K1C build volume 220 x 220 x 250, plate down
    "bed": {"size_x": 220.0, "size_y": 220.0, "size_z": 250.0},
    # D-01a, D-01b, D-06a, U-06
    "wall_floor": 0.8, "wall_struct": 2.0, "min_feature": 1.0, "wall_wide": 2.0,
    # D-03a
    "overhang_deg": 45.0,
    # D-03b
    "bridge_span": 5.0,
    # U-07: tolerance 0.01, angular <= 4*acos(1 - 0.01/6.0)
    "stl_tol": 0.01, "stl_ang": 4.0 * math.acos(1.0 - 0.01 / 6.0),
    # REQ-01, U-03 (a)
    "air_gap": 10.0,
    # REQ-02: two 4.0 +- 0.1 bores along Z, offset <= 0.10; D-04a >= 3.75
    "standoff_bores": {"S1": (-19.62, 20.18), "S2": (25.01, 9.08)},
    "standoff_bore_d": 4.0, "bore_d_tol": 0.1, "offset_max": 0.10, "standoff_bore_min": 3.75,
    # REQ-06: four 3.4 +- 0.1 bores along Y at (x +-40, z -8 / 26); D-04a >= 3.25
    "frame_holes": [(-40.0, -8.0), (40.0, -8.0), (-40.0, 26.0), (40.0, 26.0)],
    "frame_hole_d": 3.4, "frame_hole_min": 3.25,
    # REQ-03: tips at z -10.10 +- 0.10; spacers S1 10.10 (seat z 0.00), S2 37.70 (seat z 27.60)
    "tip_z": -10.10, "tip_tol": 0.10, "spacer_len": {"S1": 10.10, "S2": 37.70},
    # REQ-04: plate front z -12.00 +- 0.10, back z -17.00 +- 0.10
    "plate_front_z": -12.0, "plate_back_z": -17.0, "face_tol": 0.10,
    # REQ-05: foot underside y -70.00 +- 0.10, 4.0 +- 0.1 thick
    "foot_y": -70.0, "foot_t": 4.0,
    # REQ-07: no material at r <= 45.0 about (-8.330, -14.130) within z 0 .. 47.64
    "keepout_r": 45.0, "keepout_axis": (-8.330, -14.130), "keepout_z": (0.0, 47.64),
    # U-05 census from the plan's frozen feature list (spec 1.1 section 6 / brief amendment):
    # 1 plate, 1 foot, 2 gussets, 2 standoffs, 2 bores 4.0 along Z, 4 bores 3.4 along Y.
    # Face tally: plate+foot 8 planar (x+-50 L faces 2, z-17, z-12, y+40, y-70, y-66, z+33),
    # gussets 3 planar each (6), standoff tips 2 planar, teardrop roofs 2 planar each (8) = 24;
    # cylinders: 2 plate corners + 2 standoff sides (convex) + 2 standoff bores + 4 teardrop arcs (concave) = 10;
    # torus: 2 root fillets.
    "census": {"plane_faces": 24, "cylinder_faces": 10, "cone_faces": 0, "sphere_faces": 0,
               "torus_faces": 2, "bspline_faces": 0, "other_faces": 0,
               "concave_cylinders": 6, "convex_cylinders": 4, "bores": 6},
    "standoff_count": 2, "gusset_count": 2,
    # U-05 / spec 4 C1: standoffs 12.0 diameter x 1.90 high (plate front face to tip)
    "standoff_d": 12.0, "standoff_h": 1.90,
    # E-06: each standoff tied into the plate with a root fillet (torus face per standoff)
    "root_fillets": 2,
}
MOUNT_LABEL = "od_c04_mount"
ODH11_LABEL = "OD-H11_thermoblock"
SPACER_LABELS = {"S1": "spacer_S1_assumed_A05", "S2": "spacer_S2_assumed_A05"}


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
        detail = getattr(result, "detail", None)
        if detail:
            row["detail"] = {k: v for k, v in detail.items() if k not in ("bores", "points", "material")}
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


def _plane_faces(shape, normal_axis):
    """Planar faces whose normal is parallel to the axis index (0 x, 1 y, 2 z), either sense."""
    found = []
    for face in shape.faces():
        if face.geom_type != GeomType.PLANE:
            continue
        n = face.normal_at()
        if abs(abs((n.X, n.Y, n.Z)[normal_axis]) - 1.0) < 1e-9:
            found.append(face)
    return found


def _axis_xy(face):
    """(x, y, radius) of a cylinder's or torus's own axis (Face.center() is a point on
    the surface, not on the axis: BUILD123D-NOTES)."""
    surf = BRepAdaptor_Surface(face.wrapped)
    if face.geom_type == GeomType.CYLINDER:
        c = surf.Cylinder()
        loc, radius = c.Axis().Location(), c.Radius()
    else:
        t = surf.Torus()
        loc, radius = t.Axis().Location(), t.MajorRadius()
    return loc.X(), loc.Y(), radius


def _face_env(face, key):
    return envelope(face)[key]


def run(step_path: Path, asm_path: Path, stl_path: Path | None, params_override: dict | None = None,
        scratch: Path | None = None, heavy: bool = True) -> dict:
    """All predicates; returns {"gates": [...], "facts": {...}}."""
    import build_od_c04_mount as build

    G = Gates()
    facts: dict = {}
    mount = read_step(step_path)

    # exactly_one_solid, U-01 ---------------------------------------------------
    v = validity(mount)
    G.add("exactly_one_solid", v["solid_count"], "==", 1)
    G.add("U-01.solid_count", v["solid_count"], "==", 1)
    G.add("U-01.brep_valid", v["brep_valid"], "==", 1)
    G.add("U-01.naked_edges", v["naked_edges"], "==", 0)
    facts["label"] = getattr(mount, "label", "")

    # envelope_within_spec, U-02, D-02 -----------------------------------------
    env = envelope(mount)
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

    # U-04 clean export --------------------------------------------------------
    p = build.Params(**(params_override or {}))
    built = build.build_mount(p)["mount"]
    rt = compare_step(built, step_path)
    G.add("U-04.schema", rt["schema"], "==", 1)
    G.add("U-04.solids", rt["solids"], "==", 1)
    G.add("U-04.volume_delta", rt["volume_delta"], "<=", 0)
    G.add("U-04.faces_delta", rt["faces_delta"], "==", 0)
    G.add("U-04.labels", rt["labels"], "==", 1)
    G.add("U-04.valid_after", rt["valid_after"], "==", 1)
    facts["label_reimported"] = rt["labels"].detail.get("reimported")

    # U-05 feature census, bores -----------------------------------------------
    fc = feature_census(mount)
    facts["feature_census"] = {k: r.measured for k, r in fc.items()}
    for key, want in SPEC["census"].items():
        G.add(f"U-05.{key}" if key != "bores" else "U-05.bores", fc[key], "==", want)
        G.add(f"feature_census.{key}", fc[key], "==", want)
    census = bore_census(mount)
    facts["bores"] = census.detail.get("bores") if census.status == MEASURED else census.reason

    # standoffs: convex cylinders of the standoff diameter on the S1 / S2 axes
    standoff_faces = {}
    for name, (x, y) in SPEC["standoff_bores"].items():
        hits = []
        for face in mount.faces():
            if face.geom_type != GeomType.CYLINDER:
                continue
            ax, ay, radius = _axis_xy(face)
            if math.hypot(ax - x, ay - y) < 1.0 and abs(radius - SPEC["standoff_d"] / 2) < 1e-3:
                hits.append(face)
        standoff_faces[name] = hits
    n_standoffs = sum(1 for h in standoff_faces.values() if len(h) == 1)
    G.add("U-05.standoffs", Result("standoff_count", n_standoffs, "count",
                                   detail={"method": "one convex cylinder face on each spec standoff axis"}),
          "==", SPEC["standoff_count"])
    # gussets: planar faces whose normal is neither along X, Y nor Z (the hypotenuse), one per gusset
    slanted = [f for f in mount.faces() if f.geom_type == GeomType.PLANE and
               max(abs(f.normal_at().X), abs(f.normal_at().Y), abs(f.normal_at().Z)) < 0.99
               and abs(f.normal_at().X) < 1e-9]
    G.add("U-05.gussets", Result("gusset_count", len(slanted), "count",
                                 at=[tuple(round(v, 3) for v in f.center()) for f in slanted],
                                 detail={"method": "slanted planar faces normal to X (gusset hypotenuse)"}),
          "==", SPEC["gusset_count"])

    # REQ-02, D-04a standoff bores ---------------------------------------------
    zmid = 0.5 * (SPEC["plate_back_z"] + SPEC["tip_z"])
    for name, (x, y) in SPEC["standoff_bores"].items():
        loc = locate_bore(census, (x, y, zmid), (0, 0, 1))
        d0, tol = SPEC["standoff_bore_d"], SPEC["bore_d_tol"]
        G.add(f"REQ-02.{name}.diameter", loc["diameter"], "in", (d0 - tol, d0 + tol), assumes=("A-03",))
        G.add(f"REQ-02.{name}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=("A-03",))
        G.add(f"REQ-02.{name}.through", loc["through"], "==", 1, assumes=("A-03",))
        G.add(f"D-04a.{name}", loc["diameter"], ">=", SPEC["standoff_bore_min"], assumes=("A-04",))
        facts[f"bore_{name}_length"] = loc["length"].measured
        facts[f"bore_{name}_ends"] = loc["length"].detail if loc["length"].status == MEASURED else None

    # REQ-06, D-04a frame holes ------------------------------------------------
    foot_mid_y = SPEC["foot_y"] + 0.5 * SPEC["foot_t"]
    for x, z in SPEC["frame_holes"]:
        tag = f"x{x:+.0f}_z{z:+.0f}"
        loc = locate_bore(census, (x, foot_mid_y, z), (0, 1, 0))
        d0, tol = SPEC["frame_hole_d"], SPEC["bore_d_tol"]
        G.add(f"REQ-06.{tag}.diameter", loc["diameter"], "in", (d0 - tol, d0 + tol), assumes=("A-10",))
        G.add(f"REQ-06.{tag}.offset", loc["offset"], "<=", SPEC["offset_max"], assumes=("A-10",))
        G.add(f"REQ-06.{tag}.through", loc["through"], "==", 1, assumes=("A-10",))
        G.add(f"D-04a.{tag}", loc["diameter"], ">=", SPEC["frame_hole_min"], assumes=("A-04",))

    # REQ-04 plate faces -------------------------------------------------------
    horiz = _plane_faces(mount, 2)
    back = min(horiz, key=lambda f: f.center().Z)
    others = [f for f in horiz if f is not back and abs(f.center().Z - back.center().Z) > 1e-6]
    front = max(others, key=lambda f: f.area)
    t = SPEC["face_tol"]
    G.add("REQ-04.front_z", _face_env(front, "max_z"), "in",
          (SPEC["plate_front_z"] - t, SPEC["plate_front_z"] + t), note="largest horizontal face above the bed face")
    G.add("REQ-04.front_flat", Result("plate_front_flatness", envelope(front)["size_z"].measured, "mm"), "<=", 0.0)
    G.add("REQ-04.back_z", _face_env(back, "min_z"), "in",
          (SPEC["plate_back_z"] - t, SPEC["plate_back_z"] + t), note="lowest horizontal face (the bed face)")

    # REQ-05 foot plane and thickness -----------------------------------------
    G.add("REQ-05.underside_y", env["min_y"], "in", (SPEC["foot_y"] - t, SPEC["foot_y"] + t), assumes=("A-10",))
    xz = sorted(_plane_faces(mount, 1), key=lambda f: f.center().Y)
    try:
        outer, inner = xz[0], xz[1]
        thick = Result("foot_thickness", inner.center().Y - outer.center().Y, "mm",
                       at=tuple(round(v, 3) for v in inner.center()),
                       detail={"outer_y": outer.center().Y, "inner_y": inner.center().Y})
    except Exception as exc:  # noqa: BLE001
        thick = inconclusive("foot_thickness", "mm", f"{type(exc).__name__}: {exc}")
    G.add("REQ-05.thickness", thick, "in", (SPEC["foot_t"] - 0.1, SPEC["foot_t"] + 0.1), assumes=("A-10",))

    # REQ-03 tip faces ---------------------------------------------------------
    tips = {}
    for name, (x, y) in SPEC["standoff_bores"].items():
        cands = [f for f in horiz if math.hypot(f.center(CenterOf.BOUNDING_BOX).X - x,
                                                 f.center(CenterOf.BOUNDING_BOX).Y - y) < 1.0
                 and f.center(CenterOf.BOUNDING_BOX).Z > SPEC["plate_front_z"] + 0.5]
        if len(cands) == 1:
            tips[name] = _face_env(cands[0], "max_z")
        else:
            tips[name] = inconclusive("tip_face_z", "mm", f"{len(cands)} tip faces found on the {name} axis")
        G.add(f"REQ-03.{name}.tip_z", tips[name], "in",
              (SPEC["tip_z"] - SPEC["tip_tol"], SPEC["tip_z"] + SPEC["tip_tol"]), assumes=("A-03", "A-05"))

    front_z = _face_env(front, "max_z")
    for name in SPEC["standoff_bores"]:
        if tips[name].status == MEASURED and front_z.status == MEASURED:
            h = Result("standoff_height", tips[name].measured - front_z.measured, "mm",
                       detail={"tip_z": tips[name].measured, "front_z": front_z.measured})
        else:
            h = inconclusive("standoff_height", "mm", "tip or front face not measured")
        G.add(f"U-05.{name}.standoff_height", h, "==", SPEC["standoff_h"])

    # Assembly: OD-H11 and the spacers as placed --------------------------------
    asm = read_step(asm_path)
    parts = _children(asm)
    facts["assembly_labels"] = sorted(parts)
    odh11 = parts.get(ODH11_LABEL)
    mount_in_asm = parts.get(MOUNT_LABEL)
    spacers = {k: parts.get(lbl) for k, lbl in SPACER_LABELS.items()}
    if odh11 is None or mount_in_asm is None or any(s is None for s in spacers.values()):
        missing = inconclusive("assembly", "mm", f"assembly parts missing: have {sorted(parts)}")
        odh11 = odh11 or None
    # the mount in the assembly must be the delivered mount
    if mount_in_asm is not None:
        facts["assembly_mount_volume_delta"] = abs(mount_in_asm.volume - mount.volume)
    if odh11 is not None:
        vh = validity(odh11)
        facts["odh11_validity"] = {k: (r.measured, r.reason) for k, r in vh.items()}
        facts["odh11_envelope"] = {k: r.measured for k, r in envelope(odh11).items()}
    for name, sp in spacers.items():
        if sp is not None:
            vs = validity(sp)
            facts[f"{name}_spacer_validity"] = {k: r.measured for k, r in vs.items()}
            facts[f"{name}_spacer_envelope"] = {k: r.measured for k, r in envelope(sp).items()}

    # REQ-01 and U-03 (a) mount | OD-H11
    gap = _safe(clearance, "clearance", "mm", mount, odh11) if odh11 is not None else missing
    G.add("REQ-01", gap, ">=", SPEC["air_gap"], assumes=("A-01",))
    G.add("U-03a.mount|OD-H11.clearance", gap, ">=", SPEC["air_gap"], assumes=("A-01", "A-03", "A-05"))
    boolean = _safe(common_volume, "common_volume", "mm3", mount, odh11) if odh11 is not None else missing
    G.add("U-03a.mount|OD-H11.interference", boolean, "<=", 0, assumes=("A-01", "A-03", "A-05"),
          note="INCONCLUSIVE by the row: OD-H11 is unsound for booleans (A-14)")
    for name, sp in spacers.items():
        if sp is None:
            continue
        c_m = _safe(clearance, "clearance", "mm", sp, mount)
        i_m = _safe(common_volume, "common_volume", "mm3", sp, mount)
        c_h = _safe(clearance, "clearance", "mm", sp, odh11)
        i_h = _safe(common_volume, "common_volume", "mm3", sp, odh11)
        G.add(f"U-03a.{name}|mount.clearance", c_m, "==", 0.0, assumes=("A-03", "A-05"))
        G.add(f"U-03a.{name}|mount.interference", i_m, "<=", 0, assumes=("A-03", "A-05"))
        G.add(f"U-03a.{name}|OD-H11.clearance", c_h, "==", 0.0, assumes=("A-01", "A-03", "A-05"))
        G.add(f"U-03a.{name}|OD-H11.interference", i_h, "<=", 0, assumes=("A-01", "A-03", "A-05"),
              note="INCONCLUSIVE by the row: OD-H11 is unsound for booleans (A-14)")
        G.add(f"REQ-03.{name}.spacer|mount.clearance", c_m, "==", 0.0, assumes=("A-03", "A-05"))
        G.add(f"REQ-03.{name}.spacer|OD-H11.clearance", c_h, "==", 0.0, assumes=("A-03", "A-05"))
        length = envelope(sp)["size_z"]
        G.add(f"REQ-03.{name}.spacer_length", length, "==", SPEC["spacer_len"][name], assumes=("A-05",))
        # the spacer's axis on the standoff bore axis
        e = envelope(sp)
        cx = 0.5 * (e["min_x"].measured + e["max_x"].measured)
        cy = 0.5 * (e["min_y"].measured + e["max_y"].measured)
        x, y = SPEC["standoff_bores"][name]
        facts[f"{name}_spacer_axis_offset"] = math.hypot(cx - x, cy - y)
        facts[f"{name}_seat_z"] = e["max_z"].measured
    G.fixed("U-03b", "N/A", "no motion variable", "U-03 (b): the part has no motion variable (N/A by the row)")

    # REQ-07 bracket keep-out --------------------------------------------------
    z0, z1 = SPEC["keepout_z"]
    for tag, (ax, ay) in (("axis", SPEC["keepout_axis"]), ("origin", (0.0, 0.0))):
        keep = Pos(ax, ay, z0) * Cylinder(SPEC["keepout_r"], z1 - z0, align=None)
        # Cylinder(align=None) is centred on its own origin at its base: z z0 .. z1
        cv = _safe(common_volume, "common_volume", "mm3", mount, keep)
        cl = _safe(clearance, "clearance", "mm", mount, keep)
        if tag == "axis":
            G.add("REQ-07", cv, "<=", 0, assumes=("A-02", "A-06"),
                  note="common volume with the keep-out cylinder r 45.0 about (-8.330, -14.130), z 0 .. 47.64")
            G.add("REQ-07.clearance_to_keepout", cl, ">=", 0.0, assumes=("A-02", "A-06"),
                  note="distance from the mount to the keep-out cylinder (corroboration)")
        else:
            facts["REQ-07_origin"] = {"common_volume": cv.measured, "clearance": cl.measured,
                                      "status": cv.status, "at": cl.at}
    if heavy:
        rp = _safe(radial_profile, "radial_profile", "mm", mount, (SPEC["keepout_axis"][0], SPEC["keepout_axis"][1], 0.0),
                   (0, 0, 1), (1, 0, 0), list(range(0, 360, 10)), (z0, z1), margin=0.0, z_step=1.0,
                   side="inner", r_min=0.0, r_max=SPEC["keepout_r"])
        if isinstance(rp, dict):
            r0 = rp.get("min") or next(iter(rp.values()))
            unread = r0.detail.get("unread") if r0.detail else None
            facts["REQ-07_radial_profile"] = {"status": r0.status, "reason": r0.reason[:200],
                                              "rays_unread": len(unread) if unread is not None else None,
                                              "rays": 36 * math.ceil((z1 - z0) / 1.0)}
        else:
            facts["REQ-07_radial_profile"] = {"status": rp.status, "reason": rp.reason[:200]}

    # Walls and process rows -----------------------------------------------------
    if heavy:
        mw = _safe(min_wall, "min_wall", "mm", mount)
        G.add("D-01a", mw, ">=", SPEC["wall_floor"])
        G.add("D-01b", mw, ">=", SPEC["wall_struct"])
        G.add("D-06a", mw, ">=", SPEC["min_feature"])
        ww = _safe(min_wall_wide, "min_wall_wide", "mm", mount)
        G.add("U-06", ww, ">=", SPEC["wall_wide"], note="SOFT")
        oh = _safe(overhang_census, "overhang_census", "deg", mount, (0, 0, 1), min_deg=SPEC["overhang_deg"])
        G.add("D-03a", oh, ">=", SPEC["overhang_deg"], assumes=("A-12",))
        below = oh.detail.get("below_min_deg") if oh.detail else None
        facts["overhang_detail"] = {k: v for k, v in (oh.detail or {}).items() if k != "points"}
        # D-03b: a bridge is a downward face under the overhang limit; none means no span
        if oh.status == MEASURED and below == 0:
            span = Result("bridge_span", 0.0, "mm", detail={"basis": "overhang_census below_min_deg == 0"})
        else:
            span = inconclusive("bridge_span", "mm", "downward faces under 45 deg exist or the census failed: "
                                "the reviewer measures the span from sections")
        G.add("D-03b", span, "<=", SPEC["bridge_span"], note="reviewer, from sections")

    # E-06 root fillets ------------------------------------------------------------
    tori = [f for f in mount.faces() if f.geom_type == GeomType.TORUS]
    on_axes = 0
    for name, (x, y) in SPEC["standoff_bores"].items():
        on_axes += sum(1 for f in tori if math.hypot(_axis_xy(f)[0] - x, _axis_xy(f)[1] - y) < 1.0
                       and abs(f.center(CenterOf.BOUNDING_BOX).Z - SPEC["plate_front_z"]) < 2.0)
    G.add("E-06", Result("root_fillet_count", on_axes, "count",
                         detail={"minor_radii": [round(BRepAdaptor_Surface(f.wrapped).Torus().MinorRadius(), 4) for f in tori]}),
          "==", SPEC["root_fillets"], note="reviewer; torus face at each standoff root")

    # U-07 export mesh ---------------------------------------------------------------
    if stl_path is not None and heavy:
        try:
            scratch = scratch or (HERE / "check_v01")
            w = write_stl(mount, scratch / "remesh_check.stl", tolerance=SPEC["stl_tol"],
                          angular_tolerance=SPEC["stl_ang"])
            G.add("U-07.stl_max_sagitta", w.checks["max_sagitta"], "<=", SPEC["stl_tol"])
            mc = mesh_census(stl_path)
            facts["stl_delivered"] = {k: r.measured for k, r in mc.items()}
            facts["stl_delivered_sha256"] = file_sha256(stl_path)
            facts["stl_remesh_triangles"] = w.detail.get("triangles")
            G.add("U-07.delivered_bodies", mc["bodies"], "==", 1)
            G.add("U-07.delivered_naked_edges", mc["naked_edges"], "==", 0)
            G.add("U-07.delivered_winding", mc["winding"], "==", 1)
        except Exception as exc:  # noqa: BLE001
            G.add("U-07.stl_max_sagitta", inconclusive("stl_max_sagitta", "mm", f"{type(exc).__name__}: {exc}"),
                  "<=", SPEC["stl_tol"])

    G.fixed("U-08", "N/A", "threads cosmetic", "no threaded feature on this target (N/A by the row)")
    G.fixed("D-07", "N/A", "fit-critical bores", "clearance holes only (N/A by the row)")
    G.fixed("REQ-08", INCONCLUSIVE, "holds through a heating cycle", "bench gate: INCONCLUSIVE until the first run",
            assumes=("A-08",))
    return {"gates": G.rows, "facts": facts}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", required=True)
    ap.add_argument("--asm", required=True)
    ap.add_argument("--stl")
    ap.add_argument("--out", required=True)
    ap.add_argument("--variant", default="{}")
    ap.add_argument("--light", action="store_true", help="skip walls, overhang, radial profile and the mesh")
    a = ap.parse_args()
    ws = lambda s: (WS / s) if not Path(s).is_absolute() else Path(s)  # noqa: E731
    out = ws(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        res = run(ws(a.step), ws(a.asm), ws(a.stl) if a.stl else None, json.loads(a.variant),
                  scratch=out.parent, heavy=not a.light)
    except Exception as exc:  # noqa: BLE001
        res = {"gates": [], "facts": {}, "error": f"{type(exc).__name__}: {exc}", "trace": traceback.format_exc()}
    out.write_text(json.dumps(res, indent=1, default=str))
    for r in res["gates"]:
        print(f"{r['gate']:<44} {r['status']:<13} {r['measured']!s:<24} {r['unit']:<6} "
              f"{r['required']:<22} margin {r['margin']}")
    if "error" in res:
        print(res["trace"])


if __name__ == "__main__":
    main()
