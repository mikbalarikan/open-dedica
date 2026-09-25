#!/usr/bin/env python3
"""model.py - OD-H22_3-way-valve, params-driven build123d model (stl-re-rebuild-build123d).

Every dimension comes from measure/params.json (read through Params); the feature order is
build/MODELING_PLAN.md F01..F12. Datum frame (intake/alignment.json): z=0 flange back face,
+Z = valve axis towards the drive tube, +X = ear axis, ports in the YZ plane.
Port lists are ordered [+Y port, -Y port].

Documented clearances (not geometry): CUT_OVERSHOOT = 1.0 mm on every through/blind cut tool
and BURY = 0.5 / 1.0 mm where a sub-body is extended into a body it is fused with.

Run:
  python3 model.py --params ../measure/params.json --alignment ../intake/alignment.json \
      --out . --part OD-H22_3-way-valve --scripts <skills>/stl-re-rebuild-build123d/scripts
Exit codes: 0 ok, 2 export aborted, 3 datum-only (scale_factor != 1).
This file's own checks are a builder SELF-CHECK, not QA (CHK-INDEP).
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path
from typing import Any

from build123d import (Align, Axis, Box, BuildLine, BuildSketch, Circle, Cylinder, Edge, Face,
                       GeomType, Line, Location, Locations, Part, Plane, Pos, Rot, SlotOverall, ThreePointArc,
                       Vector, Wire, extrude, make_face, mirror, revolve)

HERE = Path(__file__).resolve().parent
CUT_OVERSHOOT = 1.0   # documented clearance: cut tools overshoot the faces they open
BURY = 0.5            # documented clearance: sub-body extended into its host (no visible surface)


def find_scripts(explicit: Path | None) -> Path:
    cands = [explicit, Path(os.environ["STL_RE_REBUILD_SCRIPTS"]) if "STL_RE_REBUILD_SCRIPTS" in os.environ else None,
             HERE.parent / "scripts", Path.home() / ".claude/skills/stl-re-rebuild-build123d/scripts"]
    for c in cands:
        if c is not None and (c / "export_frames.py").is_file():
            return c
    raise SystemExit("cannot find stl-re-rebuild-build123d/scripts; pass --scripts")


class Params:
    """Read-only view of measure/params.json; records which params were used."""

    def __init__(self, path: Path) -> None:
        d = json.loads(path.read_text(encoding="utf-8"))
        self.raw: dict[str, dict[str, Any]] = d["params"]
        for k, v in self.raw.items():
            if "value" not in v or "source" not in v:
                raise SystemExit(f"param {k}: needs value and source (run-contract.md section 4)")
        self.used: set[str] = set()

    def __getitem__(self, key: str) -> Any:
        self.used.add(key)
        return self.raw[key]["value"]

    def unused(self) -> list[str]:
        return sorted(set(self.raw) - self.used)


# ----------------------------------------------------------------------------- helpers
def revolve_profile(pts: list[tuple[float, float]]) -> Part:
    """Revolve a closed (r, h) polygon drawn in the local XZ half-plane (r >= 0) about local Z."""
    face = Face(Wire.make_polygon([Vector(r, 0, h) for r, h in pts], close=True))
    return revolve(face, Axis.Z, 360)


def ear_geometry(P: Params, off: float) -> list[dict[str, float]]:
    """Per ear: hole centre x, end radius and the tangent side lines, shrunk inward by `off`."""
    a = math.radians(P["ear_side_angle_deg"])
    out = []
    for xh in P["ear_hole_x"]:
        s = 1.0 if xh > 0 else -1.0
        re = P["ear_end_R"] - off
        tx, ty = abs(xh) + re * math.sin(a), re * math.cos(a)     # tangent point (ear on +x side)
        y0 = ty + tx * math.tan(a)                                 # side line height at x=0
        out.append({"s": s, "xh": abs(xh), "re": re, "tx": tx, "ty": ty, "y0": y0, "tan": math.tan(a)})
    return out


def outline_prism(P: Params, off: float, z0: float, z1: float) -> Part:
    """Flange outline (disc plate_R union two tapered ears) offset inward by `off`, extruded z0..z1."""
    R = P["plate_R"] - off
    with BuildSketch(Plane.XY.offset(z0)) as sk:
        Circle(R)
        for e in ear_geometry(P, off):
            s = e["s"]
            with BuildLine():
                Line((0, e["y0"]), (s * e["tx"], e["ty"]))
                ThreePointArc((s * e["tx"], e["ty"]), (s * (e["xh"] + e["re"]), 0), (s * e["tx"], -e["ty"]))
                Line((s * e["tx"], -e["ty"]), (0, -e["y0"]))
                Line((0, -e["y0"]), (0, e["y0"]))
            make_face()
    return extrude(sk.sketch, amount=z1 - z0)


def concave_corners(P: Params, off: float) -> list[tuple[float, float]]:
    """(x, y) where each ear side line meets the disc (the 4 concave outline corners)."""
    R = P["plate_R"] - off
    pts = []
    for e in ear_geometry(P, off):
        # line y = y0 - tan*|x| ; solve x^2 + y^2 = R^2 for |x| > 0
        t, y0 = e["tan"], e["y0"]
        A, B, C = 1 + t * t, -2 * y0 * t, y0 * y0 - R * R
        xa = (-B + math.sqrt(B * B - 4 * A * C)) / (2 * A)
        ya = y0 - t * xa
        pts += [(e["s"] * xa, ya), (e["s"] * xa, -ya)]
    return pts


def vertical_edges_at(pts: list[tuple[float, float]], tol: float):
    def sel(shape: Any) -> list[Any]:
        out = []
        for ed in shape.edges().filter_by(GeomType.LINE):
            d = ed.end_point() - ed.start_point()
            if abs(d.X) + abs(d.Y) > 1e-6:
                continue
            c = ed.center()
            if any(math.hypot(c.X - x, c.Y - y) < tol for x, y in pts):
                out.append(ed)
        return out
    return sel


def port_plane(P: Params, i: int) -> Plane:
    """Port frame: origin on the Z axis at port_axis_z0[i], z_dir = port axis t, x_dir = +X (u)."""
    e = math.radians(P["port_elev_deg"][i])
    s = 1.0 if i == 0 else -1.0
    d = Vector(0, s * math.cos(e), -math.sin(e))
    return Plane(origin=(0, 0, P["port_axis_z0"][i]), x_dir=(1, 0, 0), z_dir=d)


# ----------------------------------------------------------------------------- build
def build(P: Params, flog: Any) -> Part:
    top = P["rim_top_z"]
    # F01 flange outline prism
    plate = outline_prism(P, 0.0, 0.0, top)
    flog.log(f"F01 flange prism: faces={len(plate.faces())} vol={plate.volume:.1f}")
    # F02 concave disc/ear blends (4 vertical edges)
    corners = concave_corners(P, 0.0)
    flog.log(f"F02 concave corner points {[(round(x, 3), round(y, 3)) for x, y in corners]}")
    plate = flog.apply(plate, "F02 concave outline blends", vertical_edges_at(corners, 0.05),
                       radii=[P["outline_blend_R"]], param="outline_blend_R")
    # F03 back-edge round: bottom outline loop (local, before anything is fused to the back face)
    plate = flog.apply(plate, "F03 back-edge round",
                       lambda s: [ed for ed in s.edges() if abs(ed.center().Z) < 1e-6
                                  and abs(ed.start_point().Z) < 1e-6 and abs(ed.end_point().Z) < 1e-6],
                       radii=[P["back_edge_R"]], param="back_edge_R")
    # F04 tray pocket: inward offset by rim_wall_t, blends grow by the offset
    t_rim = P["rim_wall_t"]
    floor = P["flange_floor_z"]
    pocket = outline_prism(P, t_rim, floor, top + CUT_OVERSHOOT)
    pocket = flog.apply(pocket, "F04 pocket-tool concave blends (outline_blend_R + rim_wall_t)",
                        vertical_edges_at(concave_corners(P, t_rim), 0.05),
                        radii=[P["outline_blend_R"] + t_rim], param="outline_blend_R")
    plate = plate - pocket
    flog.log(f"F04 tray pocket: floor z={floor}, wall={t_rim}")

    # F05 core revolve (stem cyl, 40 deg cone, neck; collar; drive tube) - one (r,z) profile
    k = math.tan(math.radians(P["stem_cone_half_angle_deg"]))
    z_ct = P["stem_cone_top_z"]
    z_cb = z_ct - (P["stem_R"] - P["stem_neck_R"]) / k
    flog.log(f"F05 cone: top z={z_ct:.3f} r={P['stem_R']}, bottom z={z_cb:.3f} r={P['stem_neck_R']} (derived)")
    core = revolve_profile([
        (0.0, P["stem_neck_bottom_z"]), (P["stem_neck_R"], P["stem_neck_bottom_z"]),
        (P["stem_neck_R"], z_cb), (P["stem_R"], z_ct), (P["stem_R"], BURY),
        (P["collar_R"], BURY), (P["collar_R"], P["collar_top_z"]),
        (P["tube_R"], P["collar_top_z"]), (P["tube_R"], P["tube_top_z"]), (0.0, P["tube_top_z"]),
    ])
    body = plate + core
    flog.log(f"F05 core revolve fused: solids={len(body.solids())}")

    # F06 gussets (XZ plane triangle, +X instance mirrored to -X)
    ga = math.tan(math.radians(P["gusset_angle_deg"]))
    gx = P["gusset_x_at_z0"]
    with BuildSketch(Plane.XZ) as gs:
        with BuildLine():
            Line((0, BURY), (gx + BURY / ga, BURY))
            Line((gx + BURY / ga, BURY), (0, -gx * ga))
            Line((0, -gx * ga), (0, BURY))
        make_face()
    gus = extrude(gs.sketch, amount=P["gusset_t"] / 2, both=True)
    body = body + gus + mirror(gus, about=Plane.YZ)
    flog.log(f"F06 gussets: bottom z at axis {-gx * ga:.3f}; solids={len(body.solids())}")

    # F07/F08 ports
    port_cuts = []
    for i in range(2):
        pl = port_plane(P, i)
        loc = pl.location
        t0, t1, te, ts = P["port_block_t0"][i], P["port_block_t1"][i], P["port_end_t"][i], P["port_sleeve_t"][i]
        prof = revolve_profile([(0.0, 0.0), (P["port_neck_R"], 0.0), (P["port_neck_R"], ts),
                                (P["port_sleeve_R"], ts), (P["port_sleeve_R"], t1),
                                (P["port_lip_R"], t1), (P["port_lip_R"], te), (0.0, te)])
        blk = Pos(0, 0, (t0 + t1) / 2) * Box(2 * P["port_block_half_u"], 2 * P["port_block_half_v"], t1 - t0)
        blk = flog.apply(blk, f"F08 port{i} block axial corner rounds",
                         lambda s: s.edges().filter_by(Axis.Z), radii=[P["port_block_corner_R"]],
                         param="port_block_corner_R")
        body = body + loc * prof + loc * blk
        flog.log(f"F07/F08 port{i}: elev={P['port_elev_deg'][i]} z0={P['port_axis_z0'][i]} "
                 f"t sleeve/block/end = {ts}/{t0}..{t1}/{te}; solids={len(body.solids())}")
        # F11 port cut tools (local frame), collected and subtracted once with F10
        step = P["port_bore_step_t"]
        c1 = Pos(0, 0, step) * Cylinder(P["port_bore_R"], te - step + CUT_OVERSHOOT,
                                        align=(Align.CENTER, Align.CENTER, Align.MIN))
        e2 = P["port_bore2_end_t"]
        c2 = Pos(0, 0, e2) * Cylinder(P["port_bore2_R"], step - e2 + BURY,
                                      align=(Align.CENTER, Align.CENTER, Align.MIN))
        vin, vout, w = P["port_slot_v_in"], P["port_slot_v_out"], P["port_slot_w"]
        tc = t0 + P["port_slot_dt0"] + w / 2
        slot_pl = Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))  # sketch x = v, sketch y = t
        tools = c1 + c2
        for sv in (1.0, -1.0):
            with BuildSketch(slot_pl) as ss:
                with Locations((sv * (vin + vout) / 2, tc)):
                    SlotOverall(vout - vin, w)
            tools = tools + extrude(ss.sketch, amount=P["port_block_half_u"] + CUT_OVERSHOOT, both=True)
        port_cuts.append(loc * tools)

    # F09 bottom rib (top buried in the stem cylinder)
    rb = P["rib_bottom_z"]
    rtop = P["stem_neck_bottom_z"] + 2 * BURY
    rib = Pos(0, 0, (rb + rtop) / 2) * Box(P["rib_t"], 2 * P["rib_half_len"], rtop - rb)
    body = body + rib
    flog.log(f"F09 rib: z {rb}..{rtop:.3f} (top buried {2 * BURY} into the stem); solids={len(body.solids())}")

    # F10 core cut tools: tube bore, 4 slots at measured angles/widths, ear holes
    zb = P["tube_bore_bottom_z"]
    ztop = P["tube_top_z"]
    cuts = Pos(0, 0, zb) * Cylinder(P["tube_bore_r"], ztop - zb + CUT_OVERSHOOT,
                                    align=(Align.CENTER, Align.CENTER, Align.MIN))
    r_in = P["tube_bore_r"] - BURY
    r_out = P["tube_R"] + CUT_OVERSHOOT
    n_slot = int(P["slot_count"])
    assert len(P["slot_theta_deg"]) == n_slot == len(P["slot_w"]), "slot_count vs per-slot lists"
    for th, w in zip(P["slot_theta_deg"], P["slot_w"]):
        zfl = P["slot_bottom_z_x"] if abs(math.cos(math.radians(th))) > 0.7 else P["slot_bottom_z_y"]
        tool = Pos((r_in + r_out) / 2, 0, zfl) * Box(r_out - r_in, w, ztop - zfl + CUT_OVERSHOOT,
                                                     align=(Align.CENTER, Align.CENTER, Align.MIN))
        cuts = cuts + Rot(0, 0, th) * tool
        flog.log(f"F10 tube slot theta={th} w={w} floor z={zfl}")
    for xh in P["ear_hole_x"]:
        cuts = cuts + Pos(xh, 0, -CUT_OVERSHOOT) * Cylinder(P["ear_hole_r"], top + 2 * CUT_OVERSHOOT,
                                                            align=(Align.CENTER, Align.CENTER, Align.MIN))
    for pc in port_cuts:
        cuts = cuts + pc
    body = body - cuts
    flog.log(f"F10/F11 cut tools subtracted once: solids={len(body.solids())}")
    body = body.clean()
    flog.log(f"F12 clean: faces={len(body.faces())} volume={body.volume:.2f}")
    return body


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="OD-H22_3-way-valve params-driven build123d model")
    ap.add_argument("--params", type=Path, required=True)
    ap.add_argument("--alignment", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--part", default="OD-H22_3-way-valve")
    ap.add_argument("--scripts", type=Path)
    a = ap.parse_args(argv)
    sys.path.insert(0, str(find_scripts(a.scripts)))
    from export_frames import ExportAbort, ScaleFrameSkipped, export_frames
    from fillet_log import FilletLog

    import build123d

    P = Params(a.params)
    flog = FilletLog()
    flog.log(f"build123d {build123d.__version__}  params={a.params}  (builder self-check, not QA)")
    body = build(P, flog)
    if P.unused():
        flog.log(f"UNUSED params (plan/measure mismatch?): {P.unused()}")
    a.out.mkdir(parents=True, exist_ok=True)
    flog.write(a.out / "fillets.json", a.out / "build_log.txt", inputs=[a.params, Path(__file__)])
    try:
        chk = export_frames(body, a.alignment, a.out, a.part, fillets_json=a.out / "fillets.json",
                            model_py=Path(__file__).resolve(), params_json=a.params)
    except ScaleFrameSkipped as ex:
        print(f"DATUM-ONLY: {ex}", file=sys.stderr)
        return 3
    except ExportAbort as ex:
        print(f"ABORT: {ex}", file=sys.stderr)
        return 2
    s = chk["datum"]
    print(json.dumps({"solids": s["solids"], "valid": s["valid"], "closed": s["closed"], "faces": s["faces"],
                      "volume_mm3": s["volume_mm3"], "fillets": flog.summary(),
                      "scan_bbox": chk["scan"]["bbox"]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
