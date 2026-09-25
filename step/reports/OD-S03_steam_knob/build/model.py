#!/usr/bin/env python3
"""model.py - OD-S03_steam-knob: params-driven build123d model (stl-re-rebuild-build123d).

Every dimension comes from measure/params.json (read through Params). Feature order and
rationale: build/MODELING_PLAN.md. Datum frame = intake/alignment.json (crown z=0, +Z to the
sleeve, lever on +X). Deterministic; no hard-coded paths.

Run:
  python3 model.py --params ../measure/params.json --alignment ../intake/alignment.json \
      --out . --part OD-S03_steam-knob [--scripts <skill>/scripts]
Exit: 0 ok, 2 export aborted, 3 datum-only (scale_factor != 1).

Documented construction constants (clearances, NOT geometry):
  OV       = 0.5  mm  burial overlap where two sub-bodies are joined (no zero-thickness union)
  CUT_OVER = 1.0  mm  cut-tool overshoot past a face
  EPS      = 0.02 mm  clearance that keeps the helical ramp tools off coincident/tangent faces
                      (heuristic, n=1: B02 build_OOM-B02.py:182-185)
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path
from typing import Any

from build123d import (Align, Axis, BuildSketch, Circle, Cylinder, Edge, Face, GeomType, Helix, Locations,
                       Plane, Pos, Rectangle, Rot, Solid, Vector, Wire, draft, extrude, fillet,
                       revolve, sweep)

HERE = Path(__file__).resolve().parent
OV, CUT_OVER, EPS = 0.5, 1.0, 0.02


def find_scripts(explicit: Path | None) -> Path:
    cands = [explicit, Path(os.environ["STL_RE_REBUILD_SCRIPTS"]) if "STL_RE_REBUILD_SCRIPTS" in os.environ else None,
             HERE.parent / "scripts", Path.home() / ".claude/skills/stl-re-rebuild-build123d/scripts",
             Path("/home/user/agentic_STL-to-CAD/skills/stl-re-rebuild-build123d/scripts")]
    for c in cands:
        if c is not None and (c / "export_frames.py").is_file():
            return c
    raise SystemExit("cannot find stl-re-rebuild-build123d/scripts; pass --scripts")


class Params:
    """Read-only view of measure/params.json; records used params (template pattern)."""

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


# ------------------------------------------------------------------ helpers
def V(r: float, z: float) -> Vector:
    return Vector(r, 0.0, z)


def profile_face(start: tuple[float, float], segs: list[tuple]) -> Face:
    """Closed (r,z) profile in the XZ half-plane. segs: ('L', (r,z)) line to point,
    ('A', (r_mid,z_mid), (r,z)) three-point arc to point. Closes back to start."""
    edges = []
    cur = start
    for s in segs:
        if s[0] == "L":
            edges.append(Edge.make_line(V(*cur), V(*s[1])))
            cur = s[1]
        else:
            edges.append(Edge.make_three_point_arc(V(*cur), V(*s[1]), V(*s[2])))
            cur = s[2]
    if math.dist(cur, start) > 1e-9:
        edges.append(Edge.make_line(V(*cur), V(*start)))
    return Face(Wire(edges))


def revolve_profile(start, segs, cx: float, cy: float) -> Solid:
    return Pos(cx, cy, 0) * revolve(profile_face(start, segs), Axis.Z, 360)


def arc_pt(c: tuple[float, float], R: float, ang_deg: float) -> tuple[float, float]:
    a = math.radians(ang_deg)
    return (c[0] + R * math.cos(a), c[1] + R * math.sin(a))


def helical_sweep(face: Face, rise: float, start_deg: float, end_deg: float, r_path: float) -> Solid:
    """Sweep an (r,z) profile face (drawn at theta=0) along a right-hand helix that rises
    `rise` between start_deg and end_deg (CCW about +Z)."""
    span = (end_deg - start_deg) % 360.0
    hx = Helix(pitch=rise * 360.0 / span, height=rise, radius=r_path)
    p0, p1 = hx.position_at(0), hx.position_at(0.25)
    assert abs(p0.X - r_path) < 1e-6 and abs(p0.Y) < 1e-6 and abs(p0.Z) < 1e-9, "helix must start on +X at z=0"
    assert p1.Y > 0 and p1.Z > 0, "helix must be right-handed (rises with CCW theta)"
    sw = sweep(face, path=hx, is_frenet=True)
    sol = sw.solids()[0] if hasattr(sw, "solids") else sw
    return Rot(0, 0, start_deg) * sol


def line_axis_centre(P: Params, z: float) -> tuple[float, float]:
    t = math.tan(math.radians(P["stem_axis_tilt_deg"]))
    d = math.radians(P["stem_axis_dir_deg"])
    return P["stem_axis_x0"] + t * math.cos(d) * z, P["stem_axis_y0"] + t * math.sin(d) * z


# ------------------------------------------------------------------ build
def build(P: Params, flog: Any) -> Any:
    z0, zs = P["crown_z"], P["step_z"]
    H = zs - z0
    ccx, ccy = P["cap_cx"], P["cap_cy"]

    # F01 cap cylinder (straight; drafted in F05)
    cap = Pos(ccx, ccy, z0) * Cylinder(P["cap_R_z0"], H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    flog.log(f"F01 cap cylinder R{P['cap_R_z0']:.4f} z {z0:.4f}..{zs:.4f} at ({ccx:.4f},{ccy:.4f})")

    # F02 lever outline: flank lines + tip arc tangent to both (centre on the equidistant line)
    t1, t2 = math.tan(math.radians(P["lever_flank_py_plan_deg"])), math.tan(math.radians(P["lever_flank_my_plan_deg"]))
    y0p, y0m = P["lever_flank_py_y0"], P["lever_flank_my_y0"]
    s1, s2 = math.hypot(1, t1), math.hypot(1, t2)
    xc = P["lever_tip_cx"]
    yc = ((y0p + t1 * xc) / s1 + (y0m + t2 * xc) / s2) / (1 / s1 + 1 / s2)
    Rt = (y0p + t1 * xc - yc) / s1
    Tp = (xc - Rt * t1 / s1, yc + Rt / s1)
    Tm = (xc + Rt * t2 / s2, yc - Rt / s2)
    xr = ccx                                   # lever root buried inside the cap (plan §6)
    Ap, Am = (xr, y0p + t1 * xr), (xr, y0m + t2 * xr)
    L = lambda a, b: Edge.make_line(Vector(a[0], a[1], z0), Vector(b[0], b[1], z0))
    outline = Wire([L(Am, Tm), Edge.make_three_point_arc(Vector(Tm[0], Tm[1], z0), Vector(xc + Rt, yc, z0), Vector(Tp[0], Tp[1], z0)),
                    L(Tp, Ap), L(Ap, Am)])
    lever = extrude(Face(outline), H)
    flog.log(f"F02 lever: tip centre ({xc:.4f},{yc:.4f}) tangent R{Rt:.4f} (derived from flank lines), tip x max {xc + Rt:.4f} at z0")

    # F03 union
    body = cap + lever
    flog.log(f"F03 cap+lever union: solids={len(body.solids())} faces={len(body.faces())}")

    # F04 concave blend fillets (local, before the draft)
    def junction(side: int):
        def sel(s):
            out = []
            for e in s.edges().filter_by(GeomType.LINE):
                c = e.center()
                if abs(e.tangent_at(0.5).Z) > 0.999 and abs(math.hypot(c.X - ccx, c.Y - ccy) - P["cap_R_z0"]) < 1.0 and c.Y * side > 0:
                    out.append(e)
            return out
        return sel
    body = flog.apply(body, "F04 lever-cap blend +Y", junction(+1), radii=[P["lever_blend_R_py_z0"]], param="lever_blend_R_py_z0")
    body = flog.apply(body, "F04 lever-cap blend -Y", junction(-1), radii=[P["lever_blend_R_my_z0"]], param="lever_blend_R_my_z0")

    # F05 one mould draft on every side face, neutral plane = crown, widening toward +Z
    side = [f for f in body.faces() if abs(f.normal_at().Z) < 0.1]
    body = draft(side, Plane.XY.offset(z0), -P["draft_deg"])
    rtop = max(e.radius for e in body.edges().filter_by(GeomType.CIRCLE) if abs(e.center().Z - zs) < 1e-6 and e.radius > P["cap_R_z0"] - 1)
    flog.log(f"F05 draft {P['draft_deg']:.4f} deg on {len(side)} side faces; cap top-circle radius at the step face {rtop:.4f} "
             f"(expected R0+H tan = {P['cap_R_z0'] + H * math.tan(math.radians(P['draft_deg'])):.4f}); valid={body.is_valid}")

    # F06 crown loop round, F07 step-face outer loop round (local: before the collar union)
    body = flog.apply(body, "F06 crown round", lambda s: [e for e in s.edges() if abs(e.center().Z - z0) < 1e-3],
                      radii=[P["crown_round_R"]], param="crown_round_R")
    body = flog.apply(body, "F07 step-face edge round", lambda s: [e for e in s.edges() if abs(e.center().Z - zs) < 1e-3],
                      radii=[P["step_edge_R"]], param="step_edge_R")

    # F08 pocket: slot sketch (square inner end with corner rounds, semicircular outer end), drafted, cut
    yp, ym = P["pocket_y_plus_at_step"], P["pocket_y_minus_at_step"]
    xi, xe = P["pocket_x_inner_at_step"], P["pocket_end_cx"]
    zf = P["pocket_floor_z"]
    with BuildSketch(Plane.XY.offset(zf)) as sk:
        with Locations(((xi + xe) / 2, (yp + ym) / 2)):
            Rectangle(xe - xi, yp - ym)
        with Locations((xe, (yp + ym) / 2)):
            Circle((yp - ym) / 2)
        fillet([v for v in sk.vertices() if abs(v.X - xi) < 1e-6], P["pocket_corner_R"])
    tool = extrude(sk.sketch, zs - zf + CUT_OVER)
    tside = [f for f in tool.faces() if abs(f.normal_at().Z) < 0.1]
    tool = draft(tside, Plane.XY.offset(zs), -P["pocket_draft_deg"])
    flog.log(f"F08 pocket tool: {len(tside)} side faces drafted {P['pocket_draft_deg']:.4f} deg about z={zs:.4f}; floor z {zf:.4f}; valid={tool.is_valid}")
    body = body - tool
    flog.log(f"F08 pocket cut: solids={len(body.solids())} faces={len(body.faces())}")

    # F09 collar revolve (collar frame)
    ro, ri, zr = P["mouth_chamfer_r_out"], P["mouth_chamfer_r_in"], P["mouth_ring_z"]
    Rc, Rct, Rcb, zcb = P["collar_R"], P["collar_top_round_R"], P["collar_bot_round_R"], P["collar_bot_z"]
    grc, gR, gzc = P["groove_out_rc"], P["groove_out_R"], P["groove_out_bottom_z"] + P["groove_out_R"]
    fz = P["flange_z"]
    irc, iR, izc = P["groove_in_rc"], P["groove_in_R"], P["groove_in_bottom_z"] + P["groove_in_R"]
    g_out = (grc + math.sqrt(gR ** 2 - (zcb - gzc) ** 2), zcb)
    g_in = (grc - math.sqrt(gR ** 2 - (fz - gzc) ** 2), fz)
    ig_out = (irc + math.sqrt(iR ** 2 - (fz - izc) ** 2), fz)
    r_join = 0.5 * (g_in[0] + ig_out[0])        # flange-face midpoint between the grooves (derived)
    c_ct, c_cb = (Rc + Rct, zr + Rct), (Rc - Rcb, zcb - Rcb)
    collar = revolve_profile((0.0, zs - OV), [
        ("L", (ro, zs - OV)), ("L", (ro, zs)), ("L", (ri, zr)), ("L", (Rc + Rct, zr)),
        ("A", arc_pt(c_ct, Rct, 225.0), (Rc, zr + Rct)),
        ("L", (Rc, zcb - Rcb)), ("A", arc_pt(c_cb, Rcb, 45.0), (Rc - Rcb, zcb)),
        ("L", g_out), ("A", (grc, gzc - gR), g_in), ("L", (r_join, fz)), ("L", (r_join, zr)), ("L", (0.0, zr))],
        P["collar_cx"], P["collar_cy"])
    flog.log(f"F09 collar revolve: groove {g_out[0]:.3f}->{g_in[0]:.3f} bottom {gzc - gR:.3f}; join r {r_join:.3f}; valid={collar.is_valid}")

    # F10 stem revolve (stem frame, Z-parallel at the line's mid-stem height)
    zref_s = 0.5 * (P["stem_base_z"] + P["stem_core_top_z"])
    scx, scy = line_axis_centre(P, zref_s)
    stem = revolve_profile((0.0, zr - OV), [
        ("L", (r_join + OV, zr - OV)), ("L", (r_join + OV, fz)), ("L", ig_out),
        ("A", (irc, izc - iR), (irc - iR, izc)),
        ("L", (P["stem_core_R_base"], P["stem_base_z"])), ("L", (P["stem_core_R_top"], P["stem_core_top_z"])),
        ("L", (P["neck_R"], P["neck_bot_z"])), ("L", (0.0, P["neck_bot_z"]))], scx, scy)
    flog.log(f"F10 stem revolve at ({scx:.4f},{scy:.4f}) [line at z={zref_s:.3f}]; valid={stem.is_valid}")

    # F11 ribs: slot section (full-round tip, R = width/2) extruded along the measured tip line
    ths, tfs, tts, ws, zts = P["rib_theta_deg"], P["rib_tip_r_flange"], P["rib_tip_r_top"], P["rib_width"], P["rib_top_z"]
    assert len(ths) == P["rib_count"] == len(tfs) == len(tts) == len(ws) == len(zts), "rib lists must match rib_count"
    zlo = P["groove_in_bottom_z"] - OV   # it2: rib foot buried OV below the inner-groove torus bottom (it1 foot at
                                         # groove_in_bottom_z touched the torus along a line -> non-manifold tessellation)
    ribs = None
    for th, tf, tt, w, zt in zip(ths, tfs, tts, ws, zts):
        m = (tt - tf) / (zt - fz)
        tip = lambda z: tf + m * (z - fz)
        Plo, Ptop = Vector(tip(zlo) - w / 2, 0, zlo), Vector(tip(zt) - w / 2, 0, zt)
        d = Ptop - Plo
        pl = Plane(origin=Plo, x_dir=Vector(d.Z, 0, -d.X).normalized(), z_dir=d.normalized())
        depth = Plo.X - P["neck_R"]                 # inner face buried inside the core (plan §6)
        with BuildSketch(pl) as rs:
            with Locations((-depth / 2, 0)):
                Rectangle(depth, w)
            Circle(w / 2)
        rib = extrude(rs.sketch, d.length)
        rib = Pos(scx, scy, 0) * (Rot(0, 0, th) * rib)
        ribs = rib if ribs is None else ribs + rib
        flog.log(f"F11 rib theta {th:.3f}: width {w:.3f}, tip r {tip(fz):.3f}@{fz:.2f} -> {tip(zt):.3f}@{zt:.3f}, foot z {zlo:.3f} (groove bottom - OV)")

    # F12 spigot revolve (spigot frame): neck, sleeve with touching crest arcs, bore, shoulder, floor
    zref_p = 0.5 * (P["neck_bot_z"] + P["sleeve_top_z"])
    pcx, pcy = line_axis_centre(P, zref_p)
    zb, zt_, rc, rho, p, c1 = (P["sleeve_bottom_z"], P["sleeve_top_z"], P["sleeve_crest_R"], P["sleeve_ripple_rho"],
                               P["sleeve_ripple_pitch"], P["sleeve_first_crest_z"])
    n = int(math.floor((zt_ - c1) / p)) + 1
    crests = [c1 + k * p for k in range(n)]
    Rb, Rtop = c1 - zb, zt_ - crests[-1]
    assert n >= 2 and 0 < Rb < rho and 0 < Rtop < rho, (n, Rb, Rtop)
    phi = math.degrees(math.atan2(p / 2, math.sqrt(rho ** 2 - (p / 2) ** 2)))
    cusp = lambda k: (rc - rho + math.sqrt(rho ** 2 - (p / 2) ** 2), crests[k] + p / 2)
    segs: list[tuple] = [("L", (P["neck_R"], P["stem_core_top_z"])), ("L", (P["neck_R"], zb)), ("L", (rc - Rb, zb)),
                         ("A", arc_pt((rc - Rb, c1), Rb, -45.0), (rc, c1)),
                         ("A", arc_pt((rc - rho, c1), rho, phi / 2), cusp(0))]
    for k in range(1, n - 1):
        segs.append(("A", (rc, crests[k]), cusp(k)))
    segs += [("A", arc_pt((rc - rho, crests[-1]), rho, -phi / 2), (rc, crests[-1])),
             ("A", arc_pt((rc - Rtop, crests[-1]), Rtop, 45.0), (rc - Rtop, zt_)),
             ("L", (P["bore_R"], zt_)), ("L", (P["bore_R"], P["bore_shoulder_top_z"])),
             ("L", (P["bore_floor_r"], P["bore_floor_z"])), ("L", (0.0, P["bore_floor_z"]))]
    spigot = revolve_profile((0.0, P["stem_core_top_z"]), segs, pcx, pcy)
    flog.log(f"F12 spigot revolve at ({pcx:.4f},{pcy:.4f}) [line at z={zref_p:.3f}]: {n} crests {[round(c, 3) for c in crests]}, "
             f"bottom round R{Rb:.4f} (derived c1-zb), top round R{Rtop:.4f} (derived zt-c_n), cusp r {cusp(0)[0]:.4f}; valid={spigot.is_valid}")

    # F13 bottom ramp: sweep of the region below the rounded sleeve bottom, rising h over [start,end]; cut
    nR = P["neck_R"]
    hb = P["sleeve_bottom_ramp_h"]   # it2: tool floor reaches OV below zb at the END of the ramp too (it1 used zb-OV,
                                     # so for theta > ~193 deg a wedge of sleeve under the ramp survived and the tool
                                     # face grazed the bottom plane -> non-manifold tessellation at z = sleeve_bottom_z)
    fb = profile_face((nR + EPS, zb - OV - hb - EPS), [
        ("L", (rc + CUT_OVER, zb - OV - hb - EPS)), ("L", (rc + CUT_OVER, c1 - EPS)), ("L", (rc, c1 - EPS)),
        ("A", (arc_pt((rc - Rb, c1 - EPS), Rb, -45.0)), (rc - Rb, zb - EPS)), ("L", (nR + EPS, zb - EPS))])
    btool = helical_sweep(fb, P["sleeve_bottom_ramp_h"], P["sleeve_bottom_ramp_start_deg"], P["sleeve_bottom_ramp_end_deg"], rc)
    btool = Pos(pcx, pcy, 0) * btool
    spigot = spigot - btool
    flog.log(f"F13 bottom ramp cut: rise {P['sleeve_bottom_ramp_h']:.4f} over {P['sleeve_bottom_ramp_start_deg']:.2f}->"
             f"{P['sleeve_bottom_ramp_end_deg']:.2f} deg; tool valid={btool.is_valid}; spigot solids={len(spigot.solids())} valid={spigot.is_valid}")

    # F14 top tail: sweep of the rounded top-corner region, rising h over [start,end]; union
    ht = P["sleeve_top_ramp_h"]
    ft = profile_face((P["sleeve_tail_r_in"], zt_ - Rtop - ht - EPS), [
        ("L", (rc - EPS, zt_ - Rtop - ht - EPS)), ("L", (rc - EPS, crests[-1] - EPS)),   # EPS inside: no tangency with the crest torus
        ("A", arc_pt((rc - EPS - Rtop, crests[-1] - EPS), Rtop, 45.0), (rc - EPS - Rtop, zt_ - EPS)), ("L", (P["sleeve_tail_r_in"], zt_ - EPS))])
    ttool = Pos(pcx, pcy, 0) * helical_sweep(ft, ht, P["sleeve_top_ramp_start_deg"], P["sleeve_top_ramp_end_deg"], rc)
    spigot = spigot + ttool
    flog.log(f"F14 top tail union: rise {ht:.4f} over {P['sleeve_top_ramp_start_deg']:.2f}->{P['sleeve_top_ramp_end_deg']:.2f} deg; "
             f"tool valid={ttool.is_valid}; spigot solids={len(spigot.solids())} valid={spigot.is_valid}")

    # F15 union all, clean
    body = body + collar
    flog.log(f"F15a +collar: solids={len(body.solids())}")
    body = body + stem
    flog.log(f"F15b +stem: solids={len(body.solids())}")
    body = body + ribs
    flog.log(f"F15c +ribs: solids={len(body.solids())}")
    body = body + spigot
    flog.log(f"F15d +spigot: solids={len(body.solids())}")
    body = body.clean()
    flog.log(f"F15 union+clean: solids={len(body.solids())} faces={len(body.faces())} valid={body.is_valid} volume={body.volume:.3f}")
    return body


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="OD-S03 steam knob params-driven model")
    ap.add_argument("--params", type=Path, required=True)
    ap.add_argument("--alignment", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--part", default="OD-S03_steam-knob")
    ap.add_argument("--scripts", type=Path)
    a = ap.parse_args(argv)
    sys.path.insert(0, str(find_scripts(a.scripts)))
    from export_frames import ExportAbort, ScaleFrameSkipped, export_frames
    from fillet_log import FilletLog

    import build123d

    P = Params(a.params)
    flog = FilletLog()
    flog.log(f"build123d {build123d.__version__}  params={a.params}  (self-built model; any check here is a self-check, not QA)")
    body = build(P, flog)
    if P.unused():
        flog.log(f"UNUSED params (plan/measure mismatch?): {P.unused()}")
    else:
        flog.log("all params used")
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
                      "volume_mm3": s["volume_mm3"], "fillets": flog.summary(), "scan_bbox": chk["scan"]["bbox"]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
