"""OD-000, the Open Dedica top assembly: every printed part of chassis/ and every
OEM part of the step/ library that has a placement, in the machine frame, written as
one STEP with the sub-assemblies OD-C00, OD-G00, OD-H00 and OD-E00, plus a clash
report and (on request) the GLB scenes the renders are made from.

Machine frame (chassis/README.md "Frames for OD-000"): X right, +Y up, +Z front,
plate top y = 0. Every placement is a rigid joint Location(Plane(origin, x_dir =
image of local x, z_dir = image of local z)); the local y image is z x x, checked
right-handed below. Poses come from PLACEMENTS (the joints the part jobs handed
over) or, for OD-G04, OD-G10, OD-H22 and OD-H24, from the Location their part's
check assembly carries (the measured pose), composed with the parent frame. No
pose is fitted to a bounding box; bounding boxes are only compared afterwards
(CROSS_CHECKS) against the same solid in each part's check assembly.

Left out (README.md): the water path OD-W00 (tank not scanned, OD-C06 dock deferred),
the anti-drip valve OD-H21 (it sits in the tube run, no joint), the steam system
OD-S00 (phase 2), the bench fixture OD-T01, and OD-G09 (the OEM cup OD-G01 replaces;
BOM qty 0, reference only; `--with-g09` adds it at the housing identity).

Usage (from the oguz-atolye root, in the tools venv):
  uv run tools/run.py python <this script> [--plate <OD-C01.step>] [--out <assembly.step>]
         [--clash <clash_report.json>] [--no-clash] [--glb-dir <dir>] [--with-g09]
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
from OCP.BRepBuilderAPI import BRepBuilderAPI_Copy
from build123d import Color, Compound, Location, Plane, Solid

from tools.core import compare_step, read_step, solids, write_step

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]                     # open-dedica/
CHASSIS = REPO / "chassis"
LIB = REPO / "step"
REPORTS = CHASSIS / "reports"

TIMESTAMP = "2026-10-05T12:00:00"
BBOX_TOL = 0.05                            # mm, placed solid vs. the same solid in a check assembly
CLASH_NEAR = 1.0                           # mm, pairs whose boxes come this close are measured
INTERFERENCE_FLOOR = 1.0                   # mm3, the report lists every interference above this
CONTACT_GAP = 0.001                        # mm, a least distance at or below this is a contact

X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
NX, NY, NZ = (-1, 0, 0), (0, -1, 0), (0, 0, -1)

# Parent frames: (origin, x_dir, z_dir) in the machine frame.
FRAMES = {
    "machine": None,
    "housing": ((0, 180.06, 32.0), X, NY),     # OD-G01 / OD-C05: x->X, y->+Z, z->-Y
    "c03": ((0, 40, -205), Z, X),              # x->+Z, y->-Y, z->+X
    "c04": ((0, 70, -140), X, Z),              # identity rotation
    "c07": ((-92, 0, -60), NZ, Y),             # x->-Z, y->-X, z->+Y
}

G01_CHECK = "OD-G01_group_head_housing/02_STEP_STL/od_g01_assembly_C1_v03.step"
C07_CHECK = "OD-C07_valve_flowmeter_mount/02_STEP_STL/od_c07_assembly_C1_v01.step"
SIDE_CHECK = "OD-C12_C13_C16_side_panels/02_STEP_STL/od_side_assembly_C1_v01.step"
C09_CHECK = "OD-C09_front_panel/02_STEP_STL/od_c09_assembly_C1_v01.step"
C10_CHECK = "OD-C10_top_panel/02_STEP_STL/od_c10_assembly_C1_v01.step"
C11_CHECK = "OD-C11_back_panel/02_STEP_STL/od_c11_assembly_C1_v03.step"
C01_CHECK = "OD-C01_base_frame/02_STEP_STL/od_c01_assembly_C1_v02.step"
C08_CHECK = "OD-C08_electronics_bay_tray/02_STEP_STL/od_c08_assembly_C1_v01.step"
C14_CHECK = "OD-C14_cord_grommet/02_STEP_STL/od_c14_assembly_C1_v01.step"
C05_CHECK = "OD-C05_group_head_carrier/02_STEP_STL/od_c05_assembly_C4_v04.step"

# label: (sub-assembly, kind, file, frame, pose)
#   kind  PRINT (orange) or OEM (grey)
#   file  "plate" (the --plate argument), chassis/<file> or step/<file>
#   pose  None = identity in its frame; (origin, x_dir, z_dir) in its frame; or
#         ("check", <check assembly>, <child label>): that child's Location, in its frame
PLACEMENTS = {
    # OD-C00: printed chassis
    "OD-C01": ("OD-C00", "PRINT", "plate", "machine", None),
    "OD-C02": ("OD-C00", "PRINT", "chassis/OD-C02_bulkhead.step", "machine", None),
    "OD-C03": ("OD-C00", "PRINT", "chassis/OD-C03_pump_cradle.step", "c03", None),
    "OD-C04": ("OD-C00", "PRINT", "chassis/OD-C04_thermoblock_mount.step", "c04", None),
    "OD-C05": ("OD-C00", "PRINT", "chassis/OD-C05_group_head_carrier.step", "housing", None),
    "OD-C07": ("OD-C00", "PRINT", "chassis/OD-C07_valve_flowmeter_mount.step", "c07", None),
    "OD-C08": ("OD-C00", "PRINT", "chassis/OD-C08_electronics_bay_tray.step", "machine", None),
    "OD-C09": ("OD-C00", "PRINT", "chassis/OD-C09_front_panel.step", "machine", None),
    "OD-C10": ("OD-C00", "PRINT", "chassis/OD-C10_top_panel.step", "machine", None),
    "OD-C11": ("OD-C00", "PRINT", "chassis/OD-C11_back_panel.step", "machine", None),
    "OD-C12": ("OD-C00", "PRINT", "chassis/OD-C12_left_side_panel.step", "machine", None),
    "OD-C13": ("OD-C00", "PRINT", "chassis/OD-C13_right_side_panel.step", "machine", None),
    "OD-C14-A": ("OD-C00", "PRINT", "chassis/OD-C14_cord_grommet.step", "machine", None),
    # the second half: 180 deg about the line through (x 95, y 30) along Z
    "OD-C14-B": ("OD-C00", "PRINT", "chassis/OD-C14_cord_grommet.step", "machine", ((190, 60, 0), NX, Z)),
    "OD-C15-RF": ("OD-C00", "PRINT", "chassis/OD-C15_foot.step", "machine", ((110, -6, 90), X, NY)),
    "OD-C15-LF": ("OD-C00", "PRINT", "chassis/OD-C15_foot.step", "machine", ((-110, -6, 90), X, NY)),
    "OD-C15-RR": ("OD-C00", "PRINT", "chassis/OD-C15_foot.step", "machine", ((110, -6, -295), X, NY)),
    "OD-C15-LR": ("OD-C00", "PRINT", "chassis/OD-C15_foot.step", "machine", ((-110, -6, -295), X, NY)),
    # OD-C16: right translate (117, 0, z_c); left 180 deg about Y, then (-117, 0, z_c)
    "OD-C16-R1": ("OD-C00", "PRINT", "chassis/OD-C16_corner_bracket.step", "machine", ((117, 0, -262), X, Z)),
    "OD-C16-R2": ("OD-C00", "PRINT", "chassis/OD-C16_corner_bracket.step", "machine", ((117, 0, -15), X, Z)),
    "OD-C16-R3": ("OD-C00", "PRINT", "chassis/OD-C16_corner_bracket.step", "machine", ((117, 0, 62), X, Z)),
    "OD-C16-L1": ("OD-C00", "PRINT", "chassis/OD-C16_corner_bracket.step", "machine", ((-117, 0, -262), NX, NZ)),
    "OD-C16-L2": ("OD-C00", "PRINT", "chassis/OD-C16_corner_bracket.step", "machine", ((-117, 0, -15), NX, NZ)),
    "OD-C16-L3": ("OD-C00", "PRINT", "chassis/OD-C16_corner_bracket.step", "machine", ((-117, 0, 62), NX, NZ)),
    # OD-G00: group head (housing frame = the OD-G09 frame; OD-G10 locked at the measured rim z)
    "OD-G01": ("OD-G00", "PRINT", "chassis/OD-G01_group_head_housing.step", "housing", None),
    "OD-G04": ("OD-G00", "OEM", "step/OD-G04_brewing_gasket_support.step", "housing",
               ("check", G01_CHECK, "od_g04_brewing_gasket_support")),
    "OD-G10": ("OD-G00", "OEM", "step/OD-G10_portafilter.step", "housing",
               ("check", G01_CHECK, "od_g10_portafilter")),
    # OD-H00: hydraulics
    "OD-H01": ("OD-H00", "OEM", "step/OD-H01_ulka_ep5_pump.step", "c03", None),
    "OD-H11": ("OD-H00", "OEM", "step/OD-H11_thermoblock.step", "c04", None),
    "OD-H22": ("OD-H00", "OEM", "step/OD-H22_3way_valve.step", "c07", ("check", C07_CHECK, "OD-H22")),
    "OD-H24": ("OD-H00", "OEM", "step/OD-H24_flowmeter.step", "c07", ("check", C07_CHECK, "OD-H24")),
    # OD-E00: electronics, path 1
    "OD-E01": ("OD-E00", "OEM", "step/OD-E01_power_pcb.step", "machine", ((84, 80, -100), NZ, X)),
    "OD-E02": ("OD-E00", "OEM", "step/OD-E02_control_board.step", "machine", ((-99.0, 140.0, 69.35), NY, NZ)),
}
G09 = ("OD-G00", "OEM", "step/OD-G09_group_head_bayonet_cup.step", "housing", None)  # reference only

# label: [(check assembly, child label, frame the check assembly is drawn in)]
CROSS_CHECKS = {
    "OD-C01": [(SIDE_CHECK, "OD-C01", "machine")],
    "OD-C02": [(C10_CHECK, "od_c02_bulkhead", "machine"), (C08_CHECK, "od_c02_bulkhead", "machine")],
    "OD-C03": [(C11_CHECK, "od_c03_cradle", "machine")],
    "OD-C04": [(C01_CHECK, "od_c04_mount", "machine")],
    "OD-C05": [(SIDE_CHECK, "OD-C05", "machine"), (C05_CHECK, "od_c05_carrier", "housing")],
    "OD-C07": [(SIDE_CHECK, "OD-C07", "machine")],
    "OD-C08": [(SIDE_CHECK, "OD-C08", "machine")],
    "OD-C09": [(C09_CHECK, "od_c09_front", "machine")],
    "OD-C10": [(SIDE_CHECK, "OD-C10", "machine")],
    "OD-C11": [(SIDE_CHECK, "OD-C11", "machine")],
    "OD-C12": [(SIDE_CHECK, "od_c12_left", "machine")],
    "OD-C13": [(SIDE_CHECK, "od_c13_right", "machine")],
    "OD-C14-A": [(C14_CHECK, "half_upper", "machine")],
    "OD-C14-B": [(C14_CHECK, "half_lower", "machine")],
    **{f"OD-C15-{k}": [(SIDE_CHECK, f"OD-C15-{k}", "machine")] for k in ("RF", "LF", "RR", "LR")},
    **{f"OD-C16-{s}{i}": [(SIDE_CHECK, f"od_c16_bracket_{s}{i}", "machine")] for s in "RL" for i in (1, 2, 3)},
    "OD-G01": [(C09_CHECK, "OD-G01_housing", "machine"), (G01_CHECK, "od_g01_housing", "housing")],
    "OD-G04": [(C09_CHECK, "OD-G04", "machine")],
    "OD-G10": [(C09_CHECK, "OD-G10_portafilter_locked", "machine")],
    "OD-H01": [(C11_CHECK, "od_h01_pump", "machine")],
    "OD-H11": [(C01_CHECK, "od_h11_thermoblock", "machine")],
    "OD-H22": [(C07_CHECK, "OD-H22", "c07")],
    "OD-H24": [(C07_CHECK, "OD-H24", "c07")],
    "OD-E01": [(C08_CHECK, "od_e01_power_pcb", "machine")],
    "OD-E02": [(C09_CHECK, "OD-E02_control_board", "machine")],
}

SUBASSEMBLIES = ("OD-C00", "OD-G00", "OD-H00", "OD-E00")
COLOURS = {"PRINT": (0.92, 0.47, 0.16), "OEM": (0.69, 0.70, 0.73)}


def _right_handed(xd, zd) -> bool:
    x, z = np.array(xd, float), np.array(zd, float)
    y = np.cross(z, x)
    return abs(np.dot(x, z)) < 1e-12 and np.allclose(np.cross(x, y), z)


def frame_location(pose) -> Location:
    if pose is None:
        return Location()
    origin, xd, zd = pose
    assert _right_handed(xd, zd), (xd, zd)
    return Location(Plane(origin=origin, x_dir=xd, z_dir=zd))


_files: dict = {}


def load(path: Path):
    """The file's one solid, read once."""
    key = str(path)
    if key not in _files:
        found = solids(read_step(path))
        if len(found) != 1:
            raise ValueError(f"{path.name}: expected one solid, found {len(found)}")
        _files[key] = Solid(found[0])
    return _files[key]


def child(asm_rel: str, label: str):
    asm = load_asm(asm_rel)
    hits = [c for c in asm.children if c.label == label]
    if len(hits) != 1:
        raise KeyError(f"{asm_rel}: {len(hits)} children labelled {label!r}")
    return hits[0]


_asms: dict = {}


def load_asm(asm_rel: str):
    if asm_rel not in _asms:
        _asms[asm_rel] = read_step(REPORTS / asm_rel)
    return _asms[asm_rel]


def source_path(file: str, plate: Path) -> Path:
    return plate if file == "plate" else REPO / file


def pose_location(frame: str, pose) -> Location:
    """Machine-frame Location of a part: its parent frame, then its pose in that frame."""
    parent = frame_location(FRAMES[frame])
    if isinstance(pose, tuple) and pose and pose[0] == "check":
        _, asm_rel, label = pose
        return parent * child(asm_rel, label).location
    return parent * frame_location(pose)


def bbox(shape) -> list[float]:
    b = shape.bounding_box()
    return [b.min.X, b.min.Y, b.min.Z, b.max.X, b.max.Y, b.max.Z]


def place_all(plate: Path, with_g09: bool) -> dict:
    table = dict(PLACEMENTS)
    if with_g09:
        table["OD-G09"] = G09
    placed = {}
    for label, (sub, kind, file, frame, pose) in table.items():
        src = source_path(file, plate)
        # a fresh copy per placement: a solid placed twice would otherwise share one
        # STEP product, and every instance would carry the last label written
        shape = Solid(BRepBuilderAPI_Copy(load(src).wrapped).Shape()).moved(pose_location(frame, pose))
        shape.label = label
        shape.color = Color(*COLOURS[kind])
        placed[label] = {"shape": shape, "sub": sub, "kind": kind, "source": str(src.relative_to(REPO))
                         if src.is_relative_to(REPO) else str(src)}
    return placed


def cross_check(placed: dict) -> dict:
    """The placed solid's box against the same solid in every check assembly that has it."""
    out = {}
    for label, refs in CROSS_CHECKS.items():
        if label not in placed:
            continue
        mine = bbox(placed[label]["shape"])
        rows = []
        for asm_rel, child_label, frame in refs:
            ref = child(asm_rel, child_label)
            ref_box = bbox(ref.moved(frame_location(FRAMES[frame])) if FRAMES[frame] else ref)
            delta = max(abs(a - b) for a, b in zip(mine, ref_box))
            rows.append({"check_assembly": asm_rel, "child": child_label, "frame": frame,
                         "max_delta_mm": round(delta, 4), "ok": delta <= BBOX_TOL,
                         "ref_bbox": [round(v, 3) for v in ref_box]})
        out[label] = {"bbox": [round(v, 3) for v in mine], "checks": rows}
    return out


def build_assembly(placed: dict) -> Compound:
    subs = []
    for sub in SUBASSEMBLIES:
        kids = [p["shape"] for p in placed.values() if p["sub"] == sub]
        compound = Compound(children=kids)
        compound.label = sub
        subs.append(compound)
    top = Compound(children=subs)
    top.label = "OD-000"
    return top


# ---------------------------------------------------------------- clash report

def _near(a: list, b: list, gap: float) -> bool:
    return all(a[i] - gap <= b[i + 3] and b[i] - gap <= a[i + 3] for i in range(3))


def clash_report(placed: dict) -> dict:
    """Every pair whose boxes overlap or come within CLASH_NEAR: the common volume and
    the least clearance. The volume is fail-closed, as tools.core.common_volume: a
    solid that is not sound (tools.core.boolean.unsound: brep_valid, naked edges) makes
    the pair INCONCLUSIVE, with the boolean's raw number kept apart as indicative only.
    Soundness is checked once per source file (the same solid placed again is the same
    solid), which is the only difference from calling common_volume pair by pair."""
    from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
    from tools.core.boolean import unsound
    from tools.core.shapes import volume_mm3
    from tools.measure import clearance

    labels = list(placed)
    boxes = {k: bbox(placed[k]["shape"]) for k in labels}
    sound: dict[str, str | None] = {}
    for k in labels:
        src = placed[k]["source"]
        if src not in sound:
            t = time.time()
            sound[src] = unsound(placed[k]["shape"].wrapped)
            print(f"  soundness {src}: {sound[src] or 'sound'} ({time.time() - t:.1f} s)", flush=True)

    pairs = []
    for i, a in enumerate(labels):
        for b in labels[i + 1:]:
            if not _near(boxes[a], boxes[b], CLASH_NEAR):
                continue
            t = time.time()
            sa, sb = placed[a]["shape"], placed[b]["shape"]
            row = {"a": a, "b": b}
            try:
                c = clearance(sa, sb)
                row["clearance_mm"] = round(c.measured, 4)
                row["clearance_at"] = c.at
                row["inside"] = c.detail["inside"]
            except Exception as exc:                       # noqa: BLE001: reported, never hidden
                row["clearance_mm"] = None
                row["clearance_error"] = f"{type(exc).__name__}: {exc}"
            raw, raw_err = None, None
            try:
                op = BRepAlgoAPI_Common(sa.wrapped, sb.wrapped)
                if not op.IsDone():
                    raw_err = "the boolean did not finish"
                elif op.Shape().IsNull():
                    raw_err = "the boolean returned a null shape"
                else:
                    raw = sum(volume_mm3(s) for s in solids(op.Shape()))
            except Exception as exc:                       # noqa: BLE001
                raw_err = f"{type(exc).__name__}: {exc}"
            why = [f"{x}: {sound[placed[x]['source']]}" for x in (a, b) if sound[placed[x]["source"]]]
            if raw_err:
                why.append(raw_err)
            if why:
                row.update(status="INCONCLUSIVE", interference_mm3=None, reason="; ".join(why),
                           indicative_raw_boolean_mm3=None if raw is None else round(raw, 3))
            else:
                row.update(status="MEASURED", interference_mm3=round(raw, 3))
            row["verdict"] = _verdict(row)
            row["seconds"] = round(time.time() - t, 2)
            print(f"  {a} | {b}: {row['verdict']} vol={row.get('interference_mm3')} "
                  f"raw={row.get('indicative_raw_boolean_mm3')} gap={row.get('clearance_mm')} "
                  f"({row['seconds']} s)", flush=True)
            pairs.append(row)
    return {"near_mm": CLASH_NEAR, "interference_floor_mm3": INTERFERENCE_FLOOR,
            "solids": len(labels), "pairs_measured": len(pairs),
            "soundness": {k: (v or "sound") for k, v in sound.items()}, "pairs": pairs}


def _verdict(row: dict) -> str:
    if row["status"] == "INCONCLUSIVE":
        raw = row.get("indicative_raw_boolean_mm3")
        gap = row.get("clearance_mm")
        if gap is not None and gap > CONTACT_GAP:
            return "CLEAR (volume INCONCLUSIVE; the distance is positive)"
        return "INCONCLUSIVE" + ("" if raw is None else f" (raw boolean {raw} mm3, unchecked)")
    v = row["interference_mm3"]
    if v > INTERFERENCE_FLOOR:
        return "INTERFERENCE"
    if v > 0:
        return "OVERLAP <= 1 mm3"
    return "CONTACT" if (row.get("clearance_mm") or 0) <= CONTACT_GAP else "CLEAR"


def clash_markdown(report: dict, cross: dict, placed: dict) -> str:
    rows = report["pairs"]
    hits = sorted([r for r in rows if r["verdict"] == "INTERFERENCE"], key=lambda r: -r["interference_mm3"])
    inc = [r for r in rows if r["verdict"].startswith("INCONCLUSIVE")]
    clear_inc = [r for r in rows if r["verdict"].startswith("CLEAR (")]
    small = [r for r in rows if r["verdict"] == "OVERLAP <= 1 mm3"]
    contact = [r for r in rows if r["verdict"] == "CONTACT"]
    clear = sorted([r for r in rows if r["verdict"] == "CLEAR"], key=lambda r: r["clearance_mm"])
    out = ["# OD-000 clash report", "",
           f"{report['solids']} solids; {report['pairs_measured']} pairs whose bounding boxes overlap or come "
           f"within {report['near_mm']} mm were measured (common volume and least clearance). Written by "
           "`build_od000.py`; the numbers are in `clash_report.json`.", "",
           f"## Interference above {INTERFERENCE_FLOOR} mm³ ({len(hits)})", ""]
    if hits:
        out += ["| a | b | volume mm³ | clearance mm |", "|---|---|---:|---:|"]
        out += [f"| {r['a']} | {r['b']} | {r['interference_mm3']:.2f} | {r['clearance_mm']} |" for r in hits]
    else:
        out.append("None.")
    out += ["", f"## INCONCLUSIVE ({len(inc)})", "",
            "The boolean cannot be trusted on these pairs (an unsound scan solid, or the boolean failed); "
            "the raw boolean number is shown as a lead only, never as a measurement.", ""]
    if inc:
        out += ["| a | b | raw boolean mm³ (unchecked) | clearance mm | reason |", "|---|---|---:|---:|---|"]
        out += [f"| {r['a']} | {r['b']} | {r.get('indicative_raw_boolean_mm3')} | {r.get('clearance_mm')} "
                f"| {r['reason']} |" for r in inc]
    else:
        out.append("None.")
    out += ["", f"## Small overlaps up to {INTERFERENCE_FLOOR} mm³ ({len(small)})", ""]
    out += [f"- {r['a']} | {r['b']}: {r['interference_mm3']} mm³" for r in small] or ["None."]
    out += ["", f"## Contacts at 0 gap ({len(contact)})", "",
            ", ".join(f"{r['a']} | {r['b']}" for r in contact) or "None.", "",
            f"## Clear, volume unchecked but the distance is positive ({len(clear_inc)})", "",
            ", ".join(f"{r['a']} | {r['b']} ({r['clearance_mm']})" for r in clear_inc) or "None.", "",
            f"## Clear, measured: no common volume, least gap in mm ({len(clear)})", "",
            ", ".join(f"{r['a']} | {r['b']} ({r['clearance_mm']})" for r in clear) or "None.", "",
            "## Placement cross-check", "",
            f"Each placed solid's box against the same solid in its part's check assembly (tolerance {BBOX_TOL} mm).", "",
            "| part | check assembly | child | max delta mm | ok |", "|---|---|---|---:|---|"]
    for label, row in cross.items():
        for c in row["checks"]:
            out.append(f"| {label} | `{c['check_assembly'].split('/')[-1]}` | {c['child']} | {c['max_delta_mm']} "
                       f"| {'yes' if c['ok'] else '**no**'} |")
    out += ["", "## Unsound source solids", ""]
    out += [f"- `{k}`: {v}" for k, v in report["soundness"].items() if v != "sound"] or ["None."]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- GLB scenes

def write_glb(placed: dict, path: Path, hide: tuple = ()) -> None:
    """A glTF scene in the machine frame (glTF is Y-up, as the machine frame is):
    printed parts orange, OEM parts grey, one node per solid."""
    import trimesh
    rgba = {"PRINT": [235, 120, 40, 255], "OEM": [175, 178, 185, 255]}
    scene = trimesh.Scene()
    for label, p in placed.items():
        if label in hide:
            continue
        verts, tris = p["shape"].tessellate(0.1, 0.3)
        mesh = trimesh.Trimesh(np.array([v.to_tuple() for v in verts]), np.array(tris), process=False)
        mesh.visual = trimesh.visual.ColorVisuals(mesh, face_colors=rgba[p["kind"]])
        scene.add_geometry(mesh, node_name=label)
    path.parent.mkdir(parents=True, exist_ok=True)
    scene.export(path)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--plate", type=Path, default=CHASSIS / "OD-C01_base_frame.step")
    ap.add_argument("--out", type=Path, default=CHASSIS / "OD-000_open_dedica_assembly.step")
    ap.add_argument("--clash", type=Path, default=HERE / "clash_report.json")
    ap.add_argument("--no-clash", action="store_true")
    ap.add_argument("--glb-dir", type=Path, default=None)
    ap.add_argument("--with-g09", action="store_true", help="add the OEM cup OD-G09 (reference only)")
    ap.add_argument("--timestamp", default=TIMESTAMP)
    args = ap.parse_args(argv)

    t0 = time.time()
    placed = place_all(args.plate.resolve(), args.with_g09)
    print(f"placed {len(placed)} solids ({time.time() - t0:.1f} s)", flush=True)

    cross = cross_check(placed)
    bad = [(k, c) for k, r in cross.items() for c in r["checks"] if not c["ok"]]
    for k, c in bad:
        print(f"  CROSS-CHECK {k} vs {c['check_assembly']} [{c['child']}]: {c['max_delta_mm']} mm", flush=True)
    print(f"cross-check: {sum(len(r['checks']) for r in cross.values()) - len(bad)} ok, {len(bad)} off", flush=True)

    top = build_assembly(placed)
    written = write_step(top, args.out, timestamp=args.timestamp)
    back = compare_step(top, args.out)
    roundtrip = {k: {"measured": r.measured, "status": r.status} for k, r in back.items()}
    print(f"wrote {args.out} ({written.size_bytes} bytes, sha256 {written.sha256[:12]}); roundtrip {roundtrip}", flush=True)

    if args.glb_dir:
        write_glb(placed, args.glb_dir / "od000_closed.glb")
        write_glb(placed, args.glb_dir / "od000_open.glb", hide=("OD-C10", "OD-C12"))
        print(f"wrote GLB scenes to {args.glb_dir}", flush=True)

    summary = {"assembly": str(args.out), "sha256": written.sha256, "plate": str(args.plate),
               "parts": {k: {"sub": p["sub"], "kind": p["kind"], "source": p["source"]} for k, p in placed.items()},
               "roundtrip": roundtrip, "cross_check": cross}
    if not args.no_clash:
        report = clash_report(placed)
        summary["clash"] = report
        args.clash.parent.mkdir(parents=True, exist_ok=True)
        args.clash.with_suffix(".md").write_text(clash_markdown(report, cross, placed), encoding="utf-8")
    args.clash.write_text(json.dumps(summary, indent=1, default=str) + "\n", encoding="utf-8")
    print(f"done in {time.time() - t0:.0f} s", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
