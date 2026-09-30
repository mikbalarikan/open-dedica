"""Gate checks for od_c07_mount (job 20260930-od-c07-valve-flowmeter-mount, concept C1, spec 1.2).

Written before build_od_c07_mount.py (PLAYBOOK D3). One predicate per spec §5 gate row,
plus exactly_one_solid, feature_census and envelope_within_spec. Every predicate reads
the exported STEP again (tools.core.read_step), measures with tools.measure / tools.core,
and compares with tools.result.gate using the GATES §0 band of the result's unit:
mm 0.005, degrees 0.001, mm3 0.001, counts / bool / % / mm2 0. A measurement that
raises or returns nothing is INCONCLUSIVE, never PASS.

The two OEM solids are placed by the joints of DESIGN_PLAN §5 (build_od_c07_mount.place_oem:
RigidJoint on each OEM datum measured from its own features, RigidJoint on the mount at
(0, 0, 10.0) and (62.0, 0, 48.0)).

Contact exclusion (DESIGN_PLAN §6 note A): OD-H22 away from its contact is its material
below z 47.999 (mount frame); OD-H24 away from its contacts is the solid less the rim
contact annulus r 13.68 ... 16.21, z 9.999 ... 10.5 (mount frame). The hook beams and the
OD-H24 flange are the J-04 pair; the hooks are checked against the pipes and the connector
(OD-H24 outside r 20.5).

Spec 1.2 (package WP-04, no geometry change): U-03(b) moves the OD-H22 slide to 5.0 above
the seat (flange back face at z 53.0) from y +45 to y 0, then a 5.0 drop along -Z; the path
is set here (U03B below) and replaces the build Params' h22_* fields, which the build never
reads. The REQ-01 ring inner R, the REQ-02 pin bores and the REQ-04 slot width / profile /
straight walls / slit reach are one-sided bands.

Usage (from the repository root, after `source $HOME/oguz.env`):
  uv run tools/run.py python <ws>/01_CAD/check_od_c07_mount.py --step <step> --out <json>
      [--set name=value ...] [--stl <stl>] [--no-mesh]
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from dataclasses import asdict, replace
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
sys.path.insert(0, str(HERE))

from build123d import (Align, Box, Compound, Cylinder, GeomType, Location, Polygon, Solid,  # noqa: E402
                       extrude)
from OCP.BRepAdaptor import BRepAdaptor_Surface  # noqa: E402

from tools.core import (common_volume, compare_step, mesh_sagitta, read_step, solid_count,  # noqa: E402
                        validity, write_stl)
from tools.measure import (bore_census, clearance, envelope, feature_census, locate_bore,  # noqa: E402
                           mesh_census, min_wall, min_wall_wide, overhang_census, radial_extent,
                           radial_profile)
from tools.result import INCONCLUSIVE, MEASURED, Result, gate, inconclusive  # noqa: E402

import build_od_c07_mount as B  # noqa: E402  (parameters, joints; the geometry is read from the STEP)

MM, DEG, MM3, EXACT = 0.005, 0.001, 0.001, 0.0      # GATES §0 bands

# spec 1.2 §5 U-03(b): OD-H22 slid along -Y at 5.0 above its seat from y +45 to y 0 (>= 5 poses),
# then lowered 5.0 along -Z onto the deck (>= 3 poses; the slide's last pose is the drop's start)
U03B = {"h22_lift": 5.0,
        "h22_slide": (45.0, 35.0, 25.0, 16.0, 14.0, 12.0, 10.0, 8.0, 6.0, 4.0, 2.0, 0.0),
        "h22_lower": (4.0, 3.0, 2.0, 1.0, 0.5, 0.0)}
Z = (0, 0, 1)
X = (1, 0, 0)

# spec §5 "Assumes" column
AS = {"U-03": ["A-02", "A-03", "A-06", "A-07"], "D-02": ["A-12"], "D-03a": ["A-16"], "D-03b": ["A-16"],
      "D-04c": ["A-02", "A-03", "A-06", "A-07"], "D-04d": ["A-06", "A-07"], "D-05a": ["A-13"],
      "D-05b": ["A-13"], "J-01": ["A-15"], "J-04": ["A-06", "A-08"], "REQ-01": ["A-06"],
      "REQ-02": ["A-07"], "REQ-03": ["A-06", "A-08", "A-09"], "REQ-04": ["A-03"],
      "REQ-05": ["A-02", "A-13", "A-18"], "REQ-06": ["A-14"], "REQ-07": ["A-04", "A-19"],
      "REQ-08": ["A-10"]}


# ---------------------------------------------------------------- region helpers (mount frame)
def _box(x0, x1, y0, y1, z0, z1):
    return Box(x1 - x0, y1 - y0, z1 - z0, align=(Align.MIN, Align.MIN, Align.MIN)).moved(Location((x0, y0, z0)))


def _cyl(r, z0, z1, cx=0.0, cy=0.0):
    return Cylinder(r, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((cx, cy, z0)))


def _annulus(r0, r1, z0, z1, cx=0.0, cy=0.0):
    outer = _cyl(r1, z0, z1, cx, cy)
    return outer - _cyl(r0, z0 - 1, z1 + 1, cx, cy) if r0 > 0 else outer


def _sector(r0, r1, z0, z1, theta_deg, half_deg):
    reach = 3 * r1
    a0, a1 = math.radians(theta_deg - half_deg), math.radians(theta_deg + half_deg)
    wedge = extrude(Polygon((0, 0), (reach * math.cos(a0), reach * math.sin(a0)),
                            (reach * math.cos(a1), reach * math.sin(a1)), align=None), amount=z1 - z0)
    return _annulus(r0, r1, z0, z1) & wedge.moved(Location((0, 0, z0)))


def _solids(shape):
    try:
        return list(shape.solids())
    except Exception:  # noqa: BLE001
        return []


def _common(a, b):
    """a ∩ b as a Compound of solids (possibly empty)."""
    return Compound(_solids(a & b))


def _cut(a, b):
    return Compound(_solids(a - b))


def _r(name, value, unit, at=None, **detail):
    if value is None or (isinstance(value, float) and not math.isfinite(value)):
        return inconclusive(name, unit, detail.get("reason", "no value"))
    return Result(name, value, unit, at=at, detail=detail)


def _first_stretch(res, r_start, tol=0.02):
    """Outer end of the material stretch that starts at r_start (a bore wall) on a radial_extent ray."""
    if res.status != MEASURED:
        return None
    for a, b in res.detail.get("material", []):
        if abs(a - r_start) <= tol:
            return b
    return None


class Gates:
    def __init__(self):
        self.rows, self.facts = [], {}

    def add(self, gate_id, result, op, limit, band, assumes=(), required=None, note=""):
        g = gate(gate_id, result, op, limit, band=band, assumes=list(assumes), required=required)
        row = g.row()
        row["status"] = g.status
        row["note"] = note or (result.reason if result.status != MEASURED else "")
        self.rows.append(row)
        return g

    def fact(self, key, value):
        self.facts[key] = value


# ---------------------------------------------------------------- the checks
def run(step_path: Path, p: "B.Params", stl_path: Path | None, do_mesh: bool, tmp_dir: Path | None = None) -> dict:
    t0 = time.time()
    p = replace(p, **U03B)
    G = Gates()
    mount = read_step(step_path)
    oem = B.place_oem(WS / "00_Spec" / "inputs")
    h22, h24 = oem["h22"], oem["h24"]
    G.fact("placement", oem["facts"])
    vc = p.valve_x
    ms = _solids(mount)
    solid = ms[0] if ms else mount

    # ---- exactly_one_solid, U-01
    sc = solid_count(mount)
    G.add("exactly_one_solid", sc, "==", 1, EXACT)
    v = validity(mount)
    G.add("U-01", v["solid_count"], "==", 1, EXACT, required="solid_count = 1")
    G.add("U-01", v["brep_valid"], "==", 1, EXACT, required="brep_valid = 1")
    G.add("U-01", v["naked_edges"], "==", 0, EXACT, required="naked_edges = 0")

    # ---- U-02 / envelope_within_spec (size and position apart), D-02
    env = envelope(mount)
    for axis, size in (("x", 119.0), ("y", 50.0), ("z", 48.0)):
        for gid in ("U-02", "envelope_within_spec"):
            G.add(gid, env[f"size_{axis}"], "in", (size - 0.1, size + 0.1), MM, required=f"size_{axis} {size} ± 0.1")
    for axis, pos in (("x", -25.0), ("y", -25.0), ("z", 0.0)):
        for gid in ("U-02", "envelope_within_spec"):
            G.add(gid, env[f"min_{axis}"], "in", (pos - 0.1, pos + 0.1), MM, required=f"position min_{axis} {pos} ± 0.1 (reported apart)")
    for axis, bed in (("x", 220.0), ("y", 220.0), ("z", 250.0)):
        G.add("D-02", env[f"size_{axis}"], "<=", bed, MM, AS["D-02"], required=f"size_{axis} <= {bed}")

    # ---- regions of the mount
    hook_half = math.degrees(math.asin(p.hook_w / 2 / (p.hook_ri + p.hook_t / 2)))
    hook_regions = [_sector(p.hook_ri - p.catch_reach - 0.4, p.hook_ri + p.hook_t + 2.0, p.plate_t, p.hook_top_z + 1.0,
                            th, hook_half + 4.0) for th in p.hook_theta]
    hooks = [_common(solid, hr) for hr in hook_regions]
    hooks_all = Compound([s for h in hooks for s in _solids(h)])
    mount_nohooks = solid
    for hr in hook_regions:
        mount_nohooks = mount_nohooks - hr
    mount_nohooks = Compound(_solids(mount_nohooks))

    # ---- OEM regions (note A)
    rim_zone = _annulus(13.68, 16.21, p.ped_top_z - 0.001, p.ped_top_z + 0.5)
    h24_rim = _common(h24, rim_zone)
    h24_rest = _cut(h24, rim_zone)
    h24_far = _cut(h24, _cyl(20.5, -50, 100))
    h22_rest = _common(h22, _box(vc - 60, vc + 60, -60, 60, -10, p.deck_top_z - 0.001))

    # ---- U-03(a) designed contacts and the rest
    iv = common_volume(solid, h24)
    G.add("U-03", _rn(iv, "interference mount|OD-H24 (delivered pose)"), "<=", 0, MM3, AS["U-03"], required="interference mount|OD-H24 <= 0")
    iv = common_volume(solid, h22)
    G.add("U-03", _rn(iv, "interference mount|OD-H22 (delivered pose)"), "<=", 0, MM3, AS["U-03"], required="interference mount|OD-H22 <= 0")
    c = clearance(mount_nohooks, h24_rim)
    G.add("U-03", c, "==", 0, MM, AS["U-03"], required="contact: OD-H24 rim face on the pedestal top, clearance = 0")
    c = clearance(solid, _common(h22, _box(vc - 60, vc + 60, -60, 60, p.deck_top_z - 0.001, p.deck_top_z + 1.0)))
    G.add("U-03", c, "==", 0, MM, AS["U-03"], required="contact: OD-H22 flange back face on the deck top, clearance = 0")
    for th, hk in zip(p.hook_theta, hooks):
        catch = _common(hk, _box(-60, 60, -60, 60, p.catch_under_z - 0.001, p.catch_under_z + 0.8))
        c = clearance(catch, h24)
        G.add("U-03", c, "==", 0, MM, AS["U-03"], required=f"contact: hook {th:g}° catch underside on the OD-H24 flange top, clearance = 0")
    c_h24 = clearance(mount_nohooks, h24_rest)
    G.add("U-03", c_h24, ">=", 0.5, MM, AS["U-03"], required="mount (hooks aside) to OD-H24 away from the rim contact >= 0.5")
    G.add("D-04c", c_h24, ">=", 0.5, MM, AS["D-04c"], required="mount (hooks aside) to OD-H24 away from the rim contact >= 0.5")
    c_h22 = clearance(solid, h22_rest)
    G.add("U-03", c_h22, ">=", 0.5, MM, AS["U-03"], required="mount to OD-H22 below its flange back face >= 0.5")
    G.add("D-04c", c_h22, ">=", 0.5, MM, AS["D-04c"], required="mount to OD-H22 below its flange back face >= 0.5")
    c_far = clearance(hooks_all, h24_far)
    G.add("D-04c", c_far, ">=", 0.5, MM, AS["D-04c"], required="hooks to OD-H24 pipes and connector (outside r 20.5) >= 0.5")
    h24_above = _common(h24, _box(-60, 60, -60, 60, p.catch_under_z + 0.001, 100.0))
    c_up = clearance(hooks_all, h24_above)
    G.add("D-04c", c_up, ">=", 0.5, MM, AS["D-04c"], required="hooks to OD-H24 above its flange top plane (z > 29.901) >= 0.5")
    G.fact("hooks_to_pipes_connector_mm", {"measured": c_far.measured, "at": c_far.at, "on_b": c_far.detail.get("on_b"),
                                           "A-09 target": ">= 5"})
    for th, hk in zip(p.hook_theta, hooks):
        cf = clearance(hk, h24_far)
        G.fact(f"hook_{th:g}_to_pipes_connector_mm", {"measured": cf.measured, "at": cf.at, "on_b": cf.detail.get("on_b")})

    # ---- U-03(b) assembly paths
    worst = None
    poses = []
    for d in p.h24_path:
        r = common_volume(mount_nohooks, h24.moved(Location((0, 0, d))))
        poses.append({"dz": d, "mm3": r.measured, "status": r.status})
        if r.status != MEASURED:
            worst = r
            break
        if worst is None or (worst.status == MEASURED and r.measured > worst.measured):
            worst = Result("interference", r.measured, "mm3", at=f"OD-H24 raised {d} mm")
    G.add("U-03", worst, "<=", 0, MM3, AS["U-03"], required=f"(b) OD-H24 lowered along -Z from 25 mm, {len(p.h24_path)} poses, interference <= 0 (hooks exempt)")
    G.fact("h24_path", poses)
    worst = None
    worst24 = None
    poses = []
    path = [(0.0, y, p.h22_lift) for y in p.h22_slide] + [(0.0, 0.0, dz) for dz in p.h22_lower]
    for k, (dx, dy, dz) in enumerate(path):
        moved = h22.moved(Location((dx, dy, dz)))
        r = common_volume(solid, moved)
        r24 = common_volume(h24, moved)
        on_slide = k < len(p.h22_slide)
        cl = clearance(solid, moved) if r.status == MEASURED and r.measured <= MM3 else None
        poses.append({"dy": dy, "dz": dz, "leg": "slide" if on_slide else "drop", "mm3": r.measured, "status": r.status,
                      "mm3_vs_od_h24": r24.measured, "clearance_mm": cl.measured if (cl is not None and cl.ok) else None,
                      "clearance_at": cl.at if (cl is not None and cl.ok) else None,
                      "clearance_on_b": cl.detail.get("on_b") if (cl is not None and cl.ok) else None})
        for rr, tag in ((r, "mount"), (r24, "OD-H24")):
            if rr.status != MEASURED:
                worst = rr if tag == "mount" else worst
                worst24 = rr if tag == "OD-H24" else worst24
                continue
            cur = worst if tag == "mount" else worst24
            if cur is None or (cur.status == MEASURED and rr.measured > cur.measured):
                nr = Result("interference", rr.measured, "mm3", at=f"OD-H22 at y +{dy} mm, z +{dz} mm")
                if tag == "mount":
                    worst = nr
                else:
                    worst24 = nr
    n_slide, n_drop = len(p.h22_slide), len(p.h22_lower) + 1
    G.add("U-03", worst, "<=", 0, MM3, AS["U-03"],
          required=f"(b) OD-H22 slid along -Y at +{p.h22_lift:g} (flange back face z {p.deck_top_z + p.h22_lift:g}) from y +{p.h22_slide[0]:g} to 0 ({n_slide} poses), then lowered {p.h22_lift:g} along -Z ({n_drop} poses incl. the slide end); interference with the mount <= 0")
    G.add("U-03", worst24, "<=", 0, MM3, AS["U-03"],
          required=f"(b) OD-H22 along the same {len(path)} poses: interference with the seated OD-H24 <= 0")
    slide_cl = [q for q in poses if q["leg"] == "slide"]
    least = None
    if slide_cl and all(q["clearance_mm"] is not None for q in slide_cl):
        least = min(slide_cl, key=lambda q: q["clearance_mm"])
    G.fact("h22_slide_least_clearance_mm", None if least is None else
           {"measured": least["clearance_mm"], "pose": {"dy": least["dy"], "dz": least["dz"]}, "at": least["clearance_at"],
            "on_b": least["clearance_on_b"]})
    G.fact("h22_path", poses)

    # ---- U-04 STEP round trip against a rebuild with the same parameters
    built, _ = B.build(p, h24)          # the same call as the build: the ring-root rung depends on the OD-H24 gap
    rt = compare_step(built, step_path)
    G.add("U-04", rt["schema"], "==", 1, EXACT, required="schema AP242")
    G.add("U-04", rt["solids"], "==", 1, EXACT, required="1 solid re-read")
    G.add("U-04", rt["volume_delta"], "<=", 0, MM3, required="volume delta 0")
    G.add("U-04", rt["faces_delta"], "==", 0, EXACT, required="faces delta 0")
    G.add("U-04", rt["labels"], "==", 1, EXACT, required="named body re-read unchanged")
    G.add("U-04", rt["valid_after"], "==", 1, EXACT, required="valid after re-import")

    # ---- bores
    census = bore_census(mount)
    G.fact("bores", census.detail.get("bores") if census.ok else census.reason)

    def loc(pt):
        return locate_bore(census, pt, Z)

    # ---- REQ-06 / D-04a footprint holes
    foot = [(x, s * p.foot_y) for x in p.foot_x for s in (1, -1)]
    foot_ok = 0
    for (x, y) in foot:
        lb = loc((x, y, p.plate_t / 2))
        tag = f"footprint hole ({x:g}, {y:g})"
        g1 = G.add("REQ-06", lb["diameter"], "in", (3.3, 3.5), MM, AS["REQ-06"], required=f"{tag} Ø3.4 ± 0.1")
        g2 = G.add("REQ-06", lb["offset"], "<=", 0.10, MM, AS["REQ-06"], required=f"{tag} offset <= 0.10")
        g3 = G.add("REQ-06", lb["length"], "in", (3.9, 4.1), MM, AS["REQ-06"], required=f"{tag} length 4.0 ± 0.1")
        g4 = G.add("REQ-06", lb["through"], "==", 1, EXACT, AS["REQ-06"], required=f"{tag} through")
        G.add("D-04a", lb["diameter"], ">=", 3.25, MM, required=f"{tag} Ø >= 3.25")
        foot_ok += all(g.passed for g in (g1, g2, g3, g4))

    # ---- REQ-05, D-04a, D-05b screw clearance and insert bores
    screw = [(vc + p.screw_dx[0], 0.0), (vc + p.screw_dx[1], 0.0)]
    clr_ok = ins_ok = 0
    for (x, y) in screw:
        tag = f"({x:.3f}, 0)"
        a = loc((x, y, p.deck_top_z - p.screw_clear_depth / 2))
        g1 = G.add("REQ-05", a["diameter"], "in", (3.3, 3.5), MM, AS["REQ-05"], required=f"screw clearance {tag} Ø3.4 ± 0.1")
        g2 = G.add("REQ-05", a["offset"], "<=", 0.10, MM, AS["REQ-05"], required=f"screw clearance {tag} offset <= 0.10")
        g3 = G.add("REQ-05", a["length"], "in", (1.9, 2.1), MM, AS["REQ-05"], required=f"screw clearance {tag} depth 2.0 ± 0.1")
        G.add("D-04a", a["diameter"], ">=", 3.25, MM, required=f"screw clearance {tag} Ø >= 3.25")
        start_top = a["diameter"].ok and max(a["diameter"].detail["start"][2], a["diameter"].detail["end"][2])
        G.fact(f"screw_clearance_{x:.3f}_top_z", start_top)
        b = loc((x, y, p.deck_bot_z + p.insert_depth / 2))
        g4 = G.add("REQ-05", b["diameter"], "in", (3.95, 4.05), MM, AS["REQ-05"], required=f"insert bore {tag} Ø4.0 ± 0.05")
        g5 = G.add("REQ-05", b["offset"], "<=", 0.10, MM, AS["REQ-05"], required=f"insert bore {tag} coaxial offset <= 0.10")
        g6 = G.add("REQ-05", b["length"], "in", (5.6, 5.8), MM, AS["REQ-05"], required=f"insert bore {tag} depth 5.7 ± 0.1")
        G.add("D-05b", b["diameter"], "in", (3.95, 4.05), MM, AS["D-05b"], required=f"insert bore {tag} Ø 4.0 ± 0.05")
        G.add("D-05b", b["length"], ">=", 5.7, MM, AS["D-05b"], required=f"insert bore {tag} depth >= 5.7")
        opens = None
        if b["diameter"].ok:
            zlow = min(b["diameter"].detail["start"][2], b["diameter"].detail["end"][2])
            ends = b["diameter"].detail.get("open_ends") or []
            opens = int(abs(zlow - p.deck_bot_z) < 1e-3 and bool(ends) and ends[0])
        G.add("D-05b", _r("insert_bore_open_on_underside", opens, "bool"), "==", 1, EXACT, AS["D-05b"],
              required=f"insert bore {tag} opens on the deck underside")
        clr_ok += all(g.passed for g in (g1, g2, g3))
        ins_ok += all(g.passed for g in (g4, g5, g6))

    # ---- REQ-02 pin holes, recess
    pins = [((p.pin1_xy[0], p.pin1_xy[1]), p.pin1_d, "pin 1 Ø4.8", 1.9), ((p.pin2_xy[0], p.pin2_xy[1]), p.pin2_d, "pin 2 Ø3.8", 1.4)]
    pin_ok = 0
    for (xy, d, tag, pin_r) in pins:
        lb = loc((xy[0], xy[1], 5.0))
        nominal = 4.8 if "4.8" in tag else 3.8
        g1 = G.add("REQ-02", lb["diameter"], "in", (nominal, nominal + 0.1), MM, AS["REQ-02"], required=f"{tag} +0.1/-0 (one-sided, spec 1.2)")
        g2 = G.add("REQ-02", lb["offset"], "<=", 0.10, MM, AS["REQ-02"], required=f"{tag} offset <= 0.10")
        g3 = G.add("REQ-02", lb["length"], "in", (9.3, 9.5), MM, AS["REQ-02"], required=f"{tag} length 9.4 ± 0.1 (recess floor to bottom face)")
        g4 = G.add("REQ-02", lb["through"], "==", 1, EXACT, AS["REQ-02"], required=f"{tag} through")
        pin_ok += all(g.passed for g in (g1, g2, g3, g4))
        pin_solid = _common(h24, _cyl(3.0, -5, p.ped_top_z - 0.001, xy[0], xy[1]))
        c = clearance(solid, pin_solid)
        G.add("REQ-02", c, ">=", 0.5, MM, AS["REQ-02"], required=f"{tag}: clearance to the OD-H24 pin >= 0.5")
        G.add("D-04d", c, ">=", 0.30, MM, AS["D-04d"], required=f"{tag}: printed sliding fit >= 0.30 per side")
    rp = radial_profile(solid, (0, 0, 0), Z, X, [float(a) for a in range(0, 360, 5)], (9.5, 9.9), margin=0,
                        z_step=0.1, side="inner")
    G.add("REQ-02", rp["min"], "in", (14.0, 14.2), MM, AS["REQ-02"], required="recess R 14.10 ± 0.1 (radial_profile inner, z 9.5 ... 9.9) min")
    G.add("REQ-02", rp["max"], "in", (14.0, 14.2), MM, AS["REQ-02"], required="recess R 14.10 ± 0.1 (radial_profile inner, z 9.5 ... 9.9) max")
    floor = envelope(_common(solid, _cyl(13.9, 5.0, 12.0)))
    G.add("REQ-02", floor["max_z"], "in", (9.35, 9.45), MM, AS["REQ-02"], required="recess floor z 9.40 ± 0.05")
    ribs = _common(h24, _cyl(13.68, p.ped_top_z + 0.001, p.ped_top_z + 3.0))
    c = clearance(solid, ribs)
    G.add("REQ-02", c, ">=", 0.5, MM, AS["REQ-02"], required="recess to the OD-H24 underside ribs and hub (H24 inside r 13.68) >= 0.5")
    G.fact("recess_to_ribs", {"measured": c.measured, "at": c.at, "on_b": c.detail.get("on_b") if c.ok else None})

    # ---- REQ-01 flowmeter seat
    ped = envelope(_common(solid, _annulus(14.4, 15.8, 5.0, 12.0)))
    G.add("REQ-01", ped["max_z"], "in", (9.9, 10.1), MM, AS["REQ-01"], required="pedestal top z 10.0 ± 0.1")
    rp = radial_profile(solid, (0, 0, 0), Z, X, [float(a) for a in range(0, 360)], (10.5, 12.5), margin=0,
                        z_step=0.1, side="inner", r_min=15.0, r_max=18.6)
    G.add("REQ-01", rp["min"], "in", (16.30, 16.40), MM, AS["REQ-01"], required="ring inner R (radial_profile inner 0...359°, z 10.5...12.5) min in [16.30, 16.40] (spec 1.2)")
    G.add("REQ-01", rp["max"], "in", (16.30, 16.40), MM, AS["REQ-01"], required="ring inner R max in [16.30, 16.40] (spec 1.2)")
    ring = _common(solid, _annulus(16.25, 18.6, p.ped_top_z, p.ring_top_z + 1.0))
    ringenv = envelope(ring)
    G.add("REQ-01", ringenv["max_z"], "in", (12.9, 13.1), MM, AS["REQ-01"], required="ring top z 13.0 ± 0.1")
    c = clearance(ring, h24)
    G.add("REQ-01", c, "in", (0.50, 0.70), MM, AS["REQ-01"], required="clearance(ring, OD-H24 cup) in [0.50, 0.70]")
    G.add("D-04d", c, ">=", 0.30, MM, AS["D-04d"], required="ring gap >= 0.30 per side")

    # ---- REQ-03 hooks, J-01 ... J-04
    side_angles = _radial_side_faces(solid, p)
    plate_top = envelope(_common(solid, _box(-24.0, -22.0, -3.0, 3.0, -1.0, 6.0)))["max_z"]
    hooks_found = 0
    eps_all = []
    for th, hk in zip(p.hook_theta, hooks):
        tag = f"hook {th:g}°"
        sides = [a for a in side_angles if _angdiff(a, th) < hook_half + 2.0]
        centre = None
        if len(sides) >= 2:
            lo = min(sides, key=lambda a: _signed(a, th))
            hi = max(sides, key=lambda a: _signed(a, th))
            centre = (th + (_signed(lo, th) + _signed(hi, th)) / 2.0) % 360.0
        cr = _r("hook_centre_angle", centre, "deg", sides=sides)
        g0 = G.add("REQ-03", cr, "in", (th - 1.0, th + 1.0), DEG, AS["REQ-03"], required=f"{tag} centred at {th:g}° ± 1°")
        beam = radial_profile(solid, (0, 0, 0), Z, X, [th - hook_half + 1.0, th, th + hook_half - 1.0], (6.0, 26.0),
                              margin=0, z_step=0.5, side="inner", r_min=19.0, r_max=30.0)
        g1 = G.add("REQ-03", beam["min"], "in", (20.77, 20.97), MM, AS["REQ-03"], required=f"{tag} beam inner face R 20.87 ± 0.1 over z 6...26 (min)")
        g2 = G.add("REQ-03", beam["max"], "in", (20.77, 20.97), MM, AS["REQ-03"], required=f"{tag} beam inner face R 20.87 ± 0.1 over z 6...26 (max)")
        catch_env = envelope(_common(hk, _annulus(p.catch_ri - 0.5, p.hook_ri - 0.2, p.plate_t + 1.0, p.hook_top_z + 1.0)))
        g3 = G.add("REQ-03", catch_env["min_z"], "in", (29.8, 30.0), MM, AS["REQ-03"], required=f"{tag} catch underside z 29.9 ± 0.1")
        cri = radial_extent(solid, (0, 0, 0), Z, X, th, p.catch_under_z + 0.5, side="inner", r_min=17.5, r_max=30.0)
        g4 = G.add("REQ-03", cri, "in", (18.77, 18.97), MM, AS["REQ-03"], required=f"{tag} catch reaches R 18.87 ± 0.1")
        z1, z2 = p.catch_under_z + p.catch_land + 0.5, p.catch_under_z + p.catch_land + 1.5
        r1 = radial_extent(solid, (0, 0, 0), Z, X, th, z1, side="inner", r_min=17.5, r_max=30.0)
        r2 = radial_extent(solid, (0, 0, 0), Z, X, th, z2, side="inner", r_min=17.5, r_max=30.0)
        lead = None
        if r1.ok and r2.ok and r2.measured > r1.measured:
            lead = math.degrees(math.atan2(z2 - z1, r2.measured - r1.measured))
        g5 = G.add("REQ-03", _r("lead_in_angle", lead, "deg", r1=r1.measured, r2=r2.measured), "in", (44.0, 46.0), DEG,
                   AS["REQ-03"], required=f"{tag} catch top chamfer 45° ± 1° (from horizontal)")
        # the catch lands on the flange top: flange material under the catch down to the slot floors
        prism = _sector(p.catch_ri, 19.70, p.catch_under_z - 2.65, p.catch_under_z, th, hook_half - 0.5)
        pv = prism.volume
        cv = common_volume(prism, h24)
        void = None if cv.status != MEASURED else max(0.0, pv - cv.measured)
        g6 = G.add("REQ-03", _r("void_under_catch", void, "mm3", prism_mm3=pv), "<=", 0, MM3, AS["REQ-03"],
                   required=f"{tag} catch lands on the flange top outside slots and windows: void under the catch (r {p.catch_ri}...19.70, 2.65 deep) <= 0")
        cc = clearance(_common(hk, _box(-60, 60, -60, 60, p.catch_under_z - 0.001, p.catch_under_z + 0.8)), h24)
        g7 = G.add("REQ-03", cc, "==", 0, MM, AS["REQ-03"], required=f"{tag} catch underside on the flange top, clearance = 0")
        # J-04
        iv = common_volume(hk, h24)
        G.add("J-04", _rn(iv, f"interference {tag}|OD-H24"), "<=", 0, MM3, AS["J-04"], required=f"{tag} undeflected at the engaged pose: interference <= 0")
        G.add("J-04", cc, "==", 0, MM, AS["J-04"], required=f"{tag} catch underside touches the flange top, clearance = 0")
        bc = clearance(_common(hk, _box(-60, 60, -60, 60, p.plate_t + 2.0, p.catch_under_z - 0.5)), h24)
        G.fact(f"{tag}_beam_to_flange_mm", {"measured": bc.measured, "at": bc.at, "on_b": bc.detail.get("on_b") if bc.ok else None})
        # J-01 / J-02 / J-03
        beam_solid = _common(hk, _box(-60, 60, -60, 60, 6.0, 26.0))
        t = min_wall(beam_solid)
        G.add("J-02", t, ">=", 1.0, MM, required=f"{tag} beam thickness >= 1.0")
        y = (20.37 - cri.measured) if cri.ok else None
        L = (catch_env["min_z"].measured - plate_top.measured) if (catch_env["min_z"].ok and plate_top.ok) else None
        eps = None
        q = None
        if t.ok and y is not None and L is not None:
            ratio = L / t.measured
            q = 1.0 if ratio >= 10.0 else None
            if q is not None:
                eps = 100.0 * 1.5 * y * t.measured / (L * L * q)
        er = _r("snap_root_strain", eps, "%", y=y, t=t.measured, L=L, L_over_t=(L / t.measured) if (t.ok and L) else None, Q=q,
                reason="Q not defined for L/t < 10 in the spec" if q is None else "")
        G.add("J-01", er, "<=", 1.5, EXACT, AS["J-01"], required=f"{tag} ε = 1.5·y·t/(L²·Q) <= 1.5 % (y = 20.37 − catch R, L = plate top to catch underside)")
        eps_all.append(eps)
        root = radial_extent(solid, (0, 0, 0), Z, X, th, 8.0, side="outer", r_min=19.0, r_max=30.0)
        catch_t = radial_extent(solid, (0, 0, 0), Z, X, th, p.catch_under_z + 0.5, side="outer", r_min=17.5, r_max=30.0)
        root_t = (root.measured - radial_extent(solid, (0, 0, 0), Z, X, th, 8.0, side="inner", r_min=19.0, r_max=30.0).measured) if root.ok else None
        tr = None
        if root_t and catch_t.ok and cri.ok:
            tr = (catch_t.measured - cri.measured) / root_t
        G.add("J-03", _r("catch_to_root_thickness_ratio", tr, "ratio", eps_margin_pct=(1.5 - eps) if eps is not None else None), ">=", 0.5, EXACT,
              required=f"{tag} catch/root thickness ratio reported; binding only if ε within 0.2 % of 1.5 %")
        hooks_found += all(g.passed for g in (g0, g1, g2, g3, g4))

    # ---- REQ-04 valve seat
    deck = envelope(_common(solid, _box(vc - 21.5, vc + 21.5, -14.5, 14.5, p.plate_t + 1.0, 60.0)))
    G.add("REQ-04", deck["max_z"], "in", (47.9, 48.1), MM, AS["REQ-04"], required="deck top z 48.0 ± 0.1")
    flat = _flange_flatness(solid, oem["flange_face"], p)
    G.add("REQ-04", flat, "<=", 0.0, EXACT, AS["REQ-04"], required="deck top flat under the OD-H22 flange outline: flange area not on the z 48 plane beyond the slot and slits (mm²) <= 0")
    angs = [float(a) for a in range(192, 349, 2)]
    sp = radial_profile(solid, (vc, 0, 0), Z, X, angs, (41.0, 47.0), margin=0, z_step=0.5, side="inner", r_min=0.0)
    G.add("REQ-04", sp["min"], "in", (7.05, 7.10), MM, AS["REQ-04"], required="stem U-slot radial_profile inner about (62, 0), 192°...348° (slit angles aside), z 41...47, min in [7.05, 7.10] (spec 1.2)")
    G.add("REQ-04", sp["max"], "in", (7.05, 7.10), MM, AS["REQ-04"], required="stem U-slot radial_profile inner, max in [7.05, 7.10] (spec 1.2)")
    walls = []
    for yy in (2.5, 6.0, 10.0, 14.0):
        for zz in (41.0, 44.0, 47.0):
            for ang in (0.0, 180.0):
                r = radial_extent(solid, (vc, yy, 0), Z, X, ang, zz, side="inner", r_min=0.0)
                walls.append((ang, yy, zz, r))
    for ang, side in ((0.0, "+X"), (180.0, "-X")):
        rs = [w[3] for w in walls if w[0] == ang]
        bad = [r for r in rs if not r.ok]
        if bad:
            lo_r = hi_r = bad[0]
        else:
            lo_r = min(rs, key=lambda r: r.measured)
            hi_r = max(rs, key=lambda r: r.measured)
        G.add("REQ-04", lo_r, "in", (7.05, 7.10), MM, AS["REQ-04"], required=f"slot straight wall {side} at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (least)")
        G.add("REQ-04", hi_r, "in", (7.05, 7.10), MM, AS["REQ-04"], required=f"slot straight wall {side} at 7.05 +0.05/-0 from the axis, y 2.5...14, z 41...47 (greatest)")
    wsum = None
    if all(w[3].ok for w in walls):
        wsum = min(a[3].measured + b[3].measured for a in walls for b in walls if a[0] == 0.0 and b[0] == 180.0 and a[1] == b[1] and a[2] == b[2])
    G.add("REQ-04", _r("slot_width", wsum, "mm"), "in", (14.1, 14.2), MM, AS["REQ-04"], required="stem U-slot 14.1 +0.1/-0 wide (least)")
    open_v = common_volume(_box(vc - 6.9, vc + 6.9, 0.0, p.deck_y + 1.0, p.deck_bot_z + 0.05, p.deck_top_z - 0.05), solid)
    G.add("REQ-04", _rn(open_v, "slot channel material to +Y"), "<=", 0, MM3, AS["REQ-04"], required="slot open through the deck's +Y edge: material in the channel x 62 ± 6.9, y 0 ... 16 <= 0")
    sl = envelope(_common(solid, _box(vc + 7.3, vc + 7.6, 2.0, 3.0, 30.0, 60.0)))
    slot_len = None
    if sl["min_z"].ok and sl["max_z"].ok:
        slot_len = sl["max_z"].measured - sl["min_z"].measured
    G.add("REQ-04", _r("slot_length", slot_len, "mm"), "in", (7.6, 7.8), MM, AS["REQ-04"], required="slot through the deck, length 7.7 ± 0.1")
    closed = [b for b in (census.detail.get("bores", []) if census.ok else []) if abs(b["diameter"] - 14.1) < 0.5]
    G.add("REQ-04", _r("closed_stem_bores", len(closed) if census.ok else None, "count"), "==", 0, EXACT, AS["REQ-04"], required="no closed stem bore")
    slits_ok = 0
    for sgn, side in ((1, "+X"), (-1, "-X")):
        ang = 0.0 if sgn > 0 else 180.0
        ra = radial_extent(solid, (vc, 0, 0), Z, X, ang, p.deck_top_z - 0.01, side="inner", r_min=7.3)
        rb = radial_extent(solid, (vc, 0, 0), Z, X, ang, p.deck_top_z - 1.0, side="inner", r_min=7.3)
        reach = None
        if ra.ok and rb.ok:
            slope = (ra.measured - rb.measured) / 0.99
            reach = ra.measured + slope * 0.01
        ga = G.add("REQ-04", _r("slit_top_reach", reach, "mm", at_minus_0p01=ra.measured, at_minus_1=rb.measured), "in", (11.85, 11.95), MM, AS["REQ-04"],
                   required=f"gusset slit {side} reaches 62 ± (11.85 +0.1/-0) at the deck top")
        w = []
        for dx in (8.5, 9.5, 10.5):
            for zz in (47.0, 47.8):
                xs = vc + sgn * dx
                if abs(dx) > (p.slit_x_top - (p.deck_top_z - zz) / math.tan(math.radians(p.slit_angle))) - 0.2:
                    continue
                up = radial_extent(solid, (xs, 0, 0), Z, X, 90.0, zz, side="inner", r_min=0.0)
                dn = radial_extent(solid, (xs, 0, 0), Z, X, 270.0, zz, side="inner", r_min=0.0)
                w.append(up.measured + dn.measured if (up.ok and dn.ok) else None)
        wv = None if (not w or any(x is None for x in w)) else (min(w) if abs(min(w) - 2.4) > abs(max(w) - 2.4) else max(w))
        gb = G.add("REQ-04", _r("slit_width", wv, "mm", samples=w), "in", (2.3, 2.5), MM, AS["REQ-04"], required=f"gusset slit {side} 2.40 ± 0.1 wide (worst)")
        slits_ok += ga.passed and gb.passed
    cr = c_h22
    G.add("REQ-04", cr, ">=", 0.5, MM, AS["REQ-04"], required="clearance(mount, OD-H22) away from the flange contact >= 0.5; nearest points in 'at'")
    G.fact("h22_nearest", {"measured": cr.measured, "at": cr.at, "on_b": cr.detail.get("on_b") if cr.ok else None})
    # the wedge between each screw clearance hole and its slit end (D-01b's reason), at the deck top
    wedges = {}
    for sgn, dx in ((1, p.screw_dx[0]), (-1, p.screw_dx[1])):
        ang = 0.0 if sgn > 0 else 180.0
        r = radial_extent(solid, (vc, 0, 0), Z, X, ang, p.deck_top_z - 0.001, side="outer", r_min=7.3, r_max=abs(dx))
        width = None
        if r.ok:
            for a_, b_ in r.detail.get("material", []):
                if a_ > 10.0:
                    width = b_ - a_
                    break
        wedges[f"{'+X' if sgn > 0 else '-X'}"] = {"width": width, "material": r.detail.get("material") if r.ok else r.reason}
    G.fact("deck_wedge_width_at_top_mm", wedges)

    # ---- REQ-07 hose space
    plate = _common(solid, _box(-30, 100, -30, 30, 0.001, p.plate_t - 0.001))
    pieces = sorted(_solids(plate), key=lambda s: s.center().X)
    G.add("REQ-07", _r("plate_pieces", len(pieces), "count"), "==", 2, EXACT, AS["REQ-07"], required="the window splits the plate in two (window through over the full Y width)")
    if len(pieces) == 2:
        ea, eb = envelope(pieces[0]), envelope(pieces[1])
        G.add("REQ-07", ea["max_x"], "in", (39.9, 40.1), MM, AS["REQ-07"], required="plate piece -X ends at x 40.0 (window from 40)")
        G.add("REQ-07", eb["min_x"], "in", (83.9, 84.1), MM, AS["REQ-07"], required="plate piece +X starts at x 84.0 (window to 84)")
        G.fact("plate_pieces", {"a": {k: ea[k].measured for k in ea}, "b": {k: eb[k].measured for k in eb}})
    for ang, want in ((180.0, 40.0), (0.0, 84.0)):
        r = radial_extent(solid, (vc, 0, 0), Z, X, ang, 20.0, side="inner", r_min=0.0, r_max=40.0)
        xr = None if not r.ok else (vc + r.measured if ang == 0.0 else vc - r.measured)
        G.add("REQ-07", _r("leg_inner_face_x", xr, "mm"), "in", (want - 0.1, want + 0.1), MM, AS["REQ-07"], required=f"leg inner face at x {want:.1f} ± 0.1")

    # ---- REQ-08 OPV reachable
    G.add("REQ-08", env["max_z"], "<=", 48.1, MM, AS["REQ-08"], required="no material above z 48.1")
    ov = common_volume(solid, _cyl(12.0, p.deck_top_z + 0.001, 80.0, vc, 0.0))
    G.add("REQ-08", _rn(ov, "material within r 12 of the valve axis above the deck top"), "<=", 0, MM3, AS["REQ-08"], required="no material within r 12 of the valve axis above the deck top")

    # ---- REQ-09 drainage (reviewer from sections; the designer's numbers)
    notch_ok = _notches(G, solid, p)

    # ---- walls: D-01a, D-01b, D-06a, U-06
    mw = min_wall(mount)
    G.add("D-01a", mw, ">=", 0.8, MM, required="min_wall >= 0.8")
    G.add("D-01b", mw, ">=", 1.5, MM, required="min_wall >= 1.5")
    G.add("D-06a", mw, ">=", 1.0, MM, required="minimum feature >= 1.0")
    ww = min_wall_wide(mount)
    G.add("U-06", ww, ">=", 1.5, MM, required="Soft: min_wall wide (45°) >= 1.5")

    # ---- D-03a overhangs: five horizontal slabs whose floors sit at the named supported / bridge faces
    _overhangs(G, solid, p)

    # ---- D-03b bridges
    for (x, y) in screw:
        b = loc((x, y, p.deck_bot_z + p.insert_depth / 2))
        G.add("D-03b", b["diameter"], "<=", 5.0, MM, AS["D-03b"], required=f"insert bore ceiling ({x:.3f}, 0): bridge span (bore Ø) <= 5")

    # ---- D-05a, J-05 around the insert bores
    for (x, y) in screw:
        across, walls_j = [], []
        for zz in (p.deck_bot_z + 0.2, p.deck_bot_z + p.insert_depth / 2, p.deck_bot_z + p.insert_depth - 0.2):
            outs = {}
            for k in range(16):
                ang = k * 22.5
                r = radial_extent(solid, (x, y, 0), Z, X, ang, zz, side="outer", r_min=p.insert_d / 2 - 0.01)
                o = _first_stretch(r, p.insert_d / 2)
                outs[ang] = o
                walls_j.append((None if o is None else o - p.insert_d / 2, ang, zz))
            for k in range(8):
                a1, a2 = k * 22.5, k * 22.5 + 180.0
                across.append((None if (outs[a1] is None or outs[a2] is None) else outs[a1] + outs[a2], a1, zz))
        bad = [a for a in across if a[0] is None]
        least = None if bad else min(across, key=lambda a: a[0])
        G.add("D-05a", _r("insert_boss_across", None if least is None else least[0], "mm",
                          at=None if least is None else f"angle {least[1]}°, z {least[2]:.2f}"), ">=", 8.0, MM, AS["D-05a"],
              required=f"insert pad ({x:.3f}, 0): material across the bore >= 8.0 (least of 8 diameters × 3 depths)")
        bad = [a for a in walls_j if a[0] is None]
        least = None if bad else min(walls_j, key=lambda a: a[0])
        G.add("J-05", _r("insert_wall", None if least is None else least[0], "mm",
                         at=None if least is None else f"angle {least[1]}°, z {least[2]:.2f}"), ">=", 3.0, MM,
              required=f"insert bore ({x:.3f}, 0): wall >= 3.0 over its depth (16 angles × 3 depths)")

    # ---- U-05 feature census
    fc = feature_census(mount)
    G.fact("feature_census", {k: fc[k].measured for k in fc})
    G.add("feature_census", fc["bores"], "==", p.expected_bores, EXACT,
          required=f"bores = {p.expected_bores} (4 footprint, 2 pin, 2 screw clearance, 2 insert, recess, ring inner)")
    census_rows = [
        ("plate window", 1 if len(pieces) == 2 else 0, 1),
        ("Ø3.4 footprint through-holes", foot_ok, 4),
        ("pedestal", len(_solids(_common(solid, _annulus(0.0, 18.2, p.plate_t + 0.5, p.ped_top_z - 1.0)))), 1),
        ("pedestal recess", 1 if (rp_ok := _in(G, "REQ-02", "recess R")) else 0, 1),
        ("ring wall", len(_solids(_common(solid, _annulus(16.2, 18.4, 10.6, 12.9)))), 1),
        ("ring drain notches", notch_ok, 3),
        ("pin clearance through-holes (Ø4.8, Ø3.8)", pin_ok, 2),
        ("hooks", len(_solids(_common(solid, _annulus(20.5, 23.5, 10.0, 28.0)))), 3),
        ("hooks at the planned angles", hooks_found, 3),
        ("legs", len(_solids(_common(solid, _box(30.0, 94.0, -20.0, 20.0, 10.0, 38.0)))), 2),
        ("deck", len(_solids(_common(solid, _box(vc - 21.5, vc + 21.5, -14.5, 14.5, p.deck_bot_z + 0.2, p.deck_top_z - 0.2)))), 1),
        ("stem U-slot open to +Y (no closed stem bore)", 1 if (_in(G, "REQ-04", "stem U-slot radial_profile") and _in(G, "REQ-04", "slot open through") and _in(G, "REQ-04", "no closed stem bore")) else 0, 1),
        ("gusset slits", slits_ok, 2),
        ("Ø3.4 screw clearance holes", clr_ok, 2),
        ("Ø4.0 insert bores", ins_ok, 2),
    ]
    for name, got, want in census_rows:
        G.add("U-05", _r("feature_count", got, "count"), "==", want, EXACT, required=f"{name} = {want}")
        G.add("feature_census", _r("feature_count", got, "count"), "==", want, EXACT, required=f"{name} = {want}")

    # ---- U-07 mesh
    if do_mesh:
        rmax = _largest_radius(solid)
        limit = 4 * math.acos(1 - 0.01 / rmax) if rmax else None
        G.fact("stl_R_max_mm", rmax)
        G.add("U-07", _r("stl_angular_tolerance", p.stl_angular, "rad", limit=limit), "<=", limit if limit else 0.0, EXACT,
              required=f"angular a <= 4·acos(1 − 0.01/R_max), R_max {rmax}")
        if stl_path and stl_path.exists():
            tmp = (tmp_dir or step_path.parent) / f"_remesh_{step_path.stem}.stl"
            w = write_stl(mount, tmp, tolerance=0.01, angular_tolerance=p.stl_angular)
            G.add("U-07", w.checks["max_sagitta"], "<=", 0.01, MM, required="stl_max_sagitta <= 0.01")
            G.fact("stl_triangles", w.detail.get("triangles"))
            G.fact("stl_remesh_matches_delivered", w.sha256 == B.sha256(stl_path))
            mc = mesh_census(stl_path)
            G.fact("stl_mesh_census", {k: mc[k].measured for k in mc})
            G.add("U-07", mc["bodies"], "==", 1, EXACT, required="delivered STL: one body")
            G.add("U-07", mc["naked_edges"], "==", 0, EXACT, required="delivered STL: naked edges 0")
            tmp.unlink(missing_ok=True)
        else:
            G.add("U-07", inconclusive("stl_max_sagitta", "mm", "no STL given"), "<=", 0.01, MM, required="stl_max_sagitta <= 0.01")

    G.fact("elapsed_s", round(time.time() - t0, 1))
    return {"step": str(step_path.relative_to(WS)) if step_path.is_relative_to(WS) else str(step_path),
            "step_sha256": B.sha256(step_path), "check_sha256": B.sha256(Path(__file__)), "build_sha256": B.sha256(HERE / "build_od_c07_mount.py"),
            "params": asdict(p), "gates": G.rows, "facts": G.facts}


# ---------------------------------------------------------------- helpers
def _rn(res, name):
    """Rename a common_volume Result for the report, keeping its status."""
    if res.status != MEASURED:
        return res
    return Result(name, res.measured, res.unit, at=res.at, detail=res.detail)


def _in(G, gid, text):
    rows = [r for r in G.rows if r["gate"] == gid and text in r["required"]]
    return bool(rows) and all(r["status"] in ("PASS", "PASS_ASSUMED") for r in rows)


def _angdiff(a, b):
    return abs((a - b + 180.0) % 360.0 - 180.0)


def _signed(a, b):
    return (a - b + 180.0) % 360.0 - 180.0


def _radial_side_faces(solid, p):
    """Angles (deg) of the vertical planar faces lying in a plane through the Z axis, between R 20 and 24."""
    out = []
    for f in solid.faces():
        if f.geom_type != GeomType.PLANE:
            continue
        n = f.normal_at()
        c = f.center()
        if abs(n.Z) > 1e-6:
            continue
        if abs(n.X * c.X + n.Y * c.Y) > 1e-4:          # the plane passes through the Z axis
            continue
        r = math.hypot(c.X, c.Y)
        bb = f.bounding_box()
        if not (20.0 < r < 24.0 and bb.max.Z > 20.0):
            continue
        out.append(math.degrees(math.atan2(c.Y, c.X)) % 360.0)
    return sorted(set(round(a, 6) for a in out))


def _flange_flatness(solid, flange_face, p):
    """Area (mm²) of the OD-H22 flange back face, as placed, that neither rests on a mount face
    lying in the plane z = deck top nor lies over the planned slot and slits."""
    try:
        tops = [f for f in solid.faces() if f.geom_type == GeomType.PLANE and f.normal_at().Z > 0.999999
                and abs(f.center().Z - p.deck_top_z) < 1e-6]
        if not tops:
            return inconclusive("flange_area_off_the_deck_plane", "mm2", "no deck top face found")
        slab = extrude(flange_face, amount=0.2, dir=(0, 0, 1))        # upward from the flange back face
        on_top = Compound([s for t in tops for s in _solids(extrude(t, amount=0.2, dir=(0, 0, 1)) & slab)])
        vc = p.valve_x
        a = math.radians(p.slit_angle)
        voids = B.slot_and_slits(p)                                    # the planned openings (same parameters)
        planned = Compound(_solids(slab & voids))
        left = slab - on_top - planned
        area = sum(s.volume for s in _solids(left)) / 0.2
        return Result("flange_area_off_the_deck_plane", area, "mm2",
                      detail={"flange_area_mm2": flange_face.area, "on_deck_mm2": on_top.volume / 0.2,
                              "over_openings_mm2": planned.volume / 0.2, "deck_top_faces": len(tops)})
    except Exception as exc:  # noqa: BLE001
        return inconclusive("flange_area_off_the_deck_plane", "mm2", f"{type(exc).__name__}: {exc}")


def _notches(G, solid, p):
    ceilings = [f for f in solid.faces() if f.geom_type == GeomType.PLANE and f.normal_at().Z < -0.999999
                and abs(f.center().Z - (p.ped_top_z + p.notch_h)) < 0.2 and 15.5 < math.hypot(f.center().X, f.center().Y) < 19.0]
    found = sorted(math.degrees(math.atan2(f.center().Y, f.center().X)) % 360.0 for f in ceilings)
    G.fact("notch_ceiling_angles", found)
    ok = 0
    for th in p.notch_theta:
        tag = f"drain notch {th:g}°"
        near = [a for a in found if _angdiff(a, th) < 5.0]
        g0 = G.add("REQ-09", _r("notch_angle", near[0] if len(near) == 1 else None, "deg", reason=f"{len(near)} ceilings near {th}"),
                   "in", (th - 1.0, th + 1.0), DEG, required=f"{tag} at θ {th:g}° ± 1°")
        rc = (p.ring_ri + p.ring_ro) / 2
        cx, cy = rc * math.cos(math.radians(th)), rc * math.sin(math.radians(th))
        radial = (math.cos(math.radians(th)), math.sin(math.radians(th)), 0.0)
        zc = p.ped_top_z + p.notch_h / 2
        a = radial_extent(solid, (cx, cy, zc), radial, Z, 90.0, 0.0, side="inner", r_min=0.0)
        b = radial_extent(solid, (cx, cy, zc), radial, Z, 270.0, 0.0, side="inner", r_min=0.0)
        width = a.measured + b.measured if (a.ok and b.ok) else None
        g1 = G.add("REQ-09", _r("notch_width", width, "mm"), "in", (1.9, 2.1), MM, required=f"{tag} 2.0 ± 0.1 wide")
        up = radial_extent(solid, (cx, cy, zc), radial, Z, 0.0, 0.0, side="inner", r_min=0.0)
        dn = radial_extent(solid, (cx, cy, zc), radial, Z, 180.0, 0.0, side="inner", r_min=0.0)
        height = up.measured + dn.measured if (up.ok and dn.ok) else None
        g2 = G.add("REQ-09", _r("notch_height", height, "mm"), "in", (0.4, 0.6), MM, required=f"{tag} 0.5 ± 0.1 high at the ring base")
        G.add("D-03b", _r("notch_ceiling_span", width, "mm"), "<=", 5.0, MM, AS["D-03b"], required=f"{tag} ceiling bridge span <= 5")
        # through the ring wall: the ray along the notch at its mid height finds no material between the ring faces
        thr = radial_extent(solid, (0, 0, 0), Z, X, th, zc, side="inner", r_min=15.0, r_max=18.2)
        G.add("REQ-09", _r("notch_through", 1 if thr.status == INCONCLUSIVE and "no material" in thr.reason.lower() else (0 if thr.ok else None), "bool",
                          reason=thr.reason), "==", 1, EXACT, required=f"{tag} open through the ring wall (no material r 15...18.2 at mid height)")
        ok += g0.passed and g1.passed and g2.passed
    return ok


def _overhangs(G, solid, p):
    """overhang_census on horizontal slabs of the part. Each slab's floor lies at the height of the
    named faces D-03a sets aside (the notch ceilings z 10.5, the catch undersides z 29.9, the deck
    underside z 40.3, the insert-bore ceilings z 46.0), so exactly those faces rest on a slab's bed
    and are left out; every other downward face is scanned. The named faces are listed with their areas."""
    cuts = [0.0, p.ped_top_z + p.notch_h, p.catch_under_z, p.deck_bot_z, p.deck_bot_z + p.insert_depth, p.deck_top_z + 1.0]
    named = []
    for f in solid.faces():
        if f.geom_type == GeomType.PLANE and f.normal_at().Z < -0.999999:
            zc = f.center().Z
            if any(abs(zc - c) < 1e-6 for c in cuts[1:-1]):
                named.append({"z": round(zc, 4), "area_mm2": round(f.area, 3), "centre": [round(f.center().X, 3), round(f.center().Y, 3)]})
            elif zc > 1e-6:
                named.append({"z": round(zc, 4), "area_mm2": round(f.area, 3), "centre": [round(f.center().X, 3), round(f.center().Y, 3)], "NOT_NAMED": True})
    G.fact("downward_flat_faces", named)
    least = None
    per = []
    for z0, z1 in zip(cuts[:-1], cuts[1:]):
        slab = _common(solid, _box(-40, 110, -40, 40, z0, z1))
        if not _solids(slab):
            continue
        r = overhang_census(slab, (0, 0, 1), min_deg=45.0, spacing=0.5)
        per.append({"slab": [z0, z1], "status": r.status, "least_deg": r.measured, "at": r.at, "reason": r.reason,
                    "bound": r.detail.get("sampling_bound_deg")})
        if r.status != MEASURED:
            least = r
            break
        if least is None or (least.status == MEASURED and r.measured < least.measured):
            least = r
    G.fact("overhang_slabs", per)
    unnamed = [n for n in named if n.get("NOT_NAMED")]
    G.add("D-03a", least if least is not None else inconclusive("overhang_census", "deg", "no slab"), ">=", 45.0, DEG, AS["D-03a"],
          required="least overhang >= 45° off the named faces (deck underside, 3 catch undersides supported; 2 insert-bore and 3 notch ceilings bridges)")
    G.add("D-03a", _r("unnamed_flat_ceilings", len(unnamed), "count"), "==", 0, EXACT, AS["D-03a"],
          required="no flat downward face other than the named ones")


def _largest_radius(solid):
    best = 0.0
    for f in solid.faces():
        s = BRepAdaptor_Surface(f.wrapped)
        t = f.geom_type
        if t == GeomType.CYLINDER:
            best = max(best, s.Cylinder().Radius())
        elif t == GeomType.TORUS:
            best = max(best, s.Torus().MajorRadius() + s.Torus().MinorRadius())
        elif t == GeomType.CONE:
            bb = f.bounding_box()
            best = max(best, max(math.hypot(x, y) for x in (bb.min.X, bb.max.X) for y in (bb.min.Y, bb.max.Y)))
        elif t == GeomType.SPHERE:
            best = max(best, s.Sphere().Radius())
    return best or None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--stl")
    ap.add_argument("--set", action="append", default=[])
    ap.add_argument("--no-mesh", action="store_true")
    a = ap.parse_args()
    p = B.params_from(a.set)
    step = Path(a.step)
    step = step if step.is_absolute() else WS / step
    stl = None if not a.stl else (Path(a.stl) if Path(a.stl).is_absolute() else WS / a.stl)
    out = Path(a.out)
    out = out if out.is_absolute() else WS / out
    out.parent.mkdir(parents=True, exist_ok=True)
    res = run(step, p, stl, not a.no_mesh, out.parent)
    out.write_text(json.dumps(res, indent=1, default=str))
    fails = [r for r in res["gates"] if r["status"] not in ("PASS", "PASS_ASSUMED")]
    for r in res["gates"]:
        print(f'{r["gate"]:22s} {r["status"]:13s} {r["measured"]!s:>22s} {r["unit"]:6s} {r["required"]}')
    print(f"rows {len(res['gates'])}, not passed {len(fails)}, elapsed {res['facts'].get('elapsed_s')} s")


if __name__ == "__main__":
    main()
