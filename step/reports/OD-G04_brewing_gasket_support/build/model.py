#!/usr/bin/env python3
"""build/model.py - OD-G04 brewing gasket support, params-driven build123d model.

Built from stl-re-rebuild-build123d/templates/model_template.py. Every dimension comes from
measure/params.json (P["..."]); the only literals are documented clearances (cut-tool
overshoot, boolean overlaps). Feature order follows build/MODELING_PLAN.md.

Run:  python model.py --params ../measure/params.json --alignment ../intake/alignment.json \
                      --out . --part OD-G04_brewing-gasket-support
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path
from typing import Any

from build123d import (Align, Axis, Box, BuildLine, Cylinder, Face, Line, Part, Pos, Rot,
                       ThreePointArc, Vector, Wire, revolve)

HERE = Path(__file__).resolve().parent
OVL = 0.3   # boolean overlap into the parent body so unions are volumetric, not tangent (clearance)
OVS = 1.0   # cut-tool overshoot past the faces it opens (clearance)
EPS = 1e-3  # numerical guard: slot tool inner wall 1 um inside the hub-ring cylinder (a coincident
            # cylinder makes the OCC boolean invalid); 49x below the scan noise floor

def find_scripts(explicit: Path | None) -> Path:
    """Locate stl-re-rebuild-build123d/scripts (flag, env, sibling folder, ~/.claude/skills)."""
    cands = [explicit, Path(os.environ["STL_RE_REBUILD_SCRIPTS"]) if "STL_RE_REBUILD_SCRIPTS" in os.environ else None,
             HERE.parent / "scripts", HERE.parents[2] / "skills/stl-re-rebuild-build123d/scripts", Path.home() / ".claude/skills/stl-re-rebuild-build123d/scripts"]
    for c in cands:
        if c is not None and (c / "export_frames.py").is_file():
            return c
    raise SystemExit("cannot find stl-re-rebuild-build123d/scripts; pass --scripts")


class Params:
    """Read-only view of measure/params.json. Records which params the model used, so the
    build log can list unused params (a param nobody uses is a plan/measure mismatch)."""

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

    def group(self, prefix: str) -> list[Any]:
        """A placement group of measured values (e.g. hole/leg angles), either form
        (run-contract.md section 11 - a consumer must accept both):
          * a single list-valued param named `prefix` (e.g. "leg_theta": {"value": [60, 150, -60], ...}), or
          * numbered keys prefix_1, prefix_2, ... in numeric order.
        Never silently returns []: an empty list value, or no keys of either form, raises,
        so a pattern can never place zero instances without someone noticing."""
        if prefix in self.raw and isinstance(self.raw[prefix]["value"], list):
            val = self[prefix]
            if not val:
                raise KeyError(f"param {prefix!r}: list value is empty (run-contract.md section 11)")
            return list(val)
        keys = sorted((k for k in self.raw if k.startswith(prefix + "_") and k[len(prefix) + 1:].isdigit()),
                      key=lambda k: int(k[len(prefix) + 1:]))
        if not keys:
            raise KeyError(f"no params for group {prefix!r}: expected a list-valued {prefix!r} or "
                          f"numbered {prefix}_1, {prefix}_2, ... (run-contract.md section 11)")
        return [self[k] for k in keys]

    def unused(self) -> list[str]:
        return sorted(set(self.raw) - self.used)



def rounded_profile(pts: list[tuple[float, float, float]]) -> Face:
    """Closed (r, z) polygon in the XZ half-plane; each vertex (r, z, R) gets a tangent arc of
    radius R (R = 0: sharp corner). Two adjacent arcs whose tangent points meet form a full round."""
    n = len(pts)
    P2 = [Vector(r, 0, z) for r, z, _ in pts]
    segs = []   # per vertex: (t_in, mid, t_out) or (p, None, p)
    for i, (r, z, R) in enumerate(pts):
        p, a, c = P2[i], P2[i - 1], P2[(i + 1) % n]
        if R <= 0:
            segs.append((p, None, p))
            continue
        u1, u2 = (a - p).normalized(), (c - p).normalized()
        half = math.acos(max(-1.0, min(1.0, u1.dot(u2)))) / 2
        d = R / math.tan(half)
        b = (u1 + u2).normalized()
        centre = p + b * (R / math.sin(half))
        segs.append((p + u1 * d, centre - b * R, p + u2 * d))
    with BuildLine() as bl:
        for i in range(n):
            t_in, mid, t_out = segs[i]
            if mid is not None:
                ThreePointArc(t_in, mid, t_out)
            nxt = segs[(i + 1) % n][0]
            if (nxt - t_out).length > 1e-6:
                Line(t_out, nxt)
    return Face(Wire(bl.edges()))


def sector_revolve(pts: list[tuple[float, float, float]], a0: float, span: float) -> Part:
    """Revolve a rounded (r, z) profile by `span` deg, starting at angle a0 (deg, CCW from +X)."""
    return Rot(0, 0, a0) * revolve(rounded_profile(pts), Axis.Z, span)


def build(P: Params, flog: Any) -> Part:
    # ---------------------------------------------------------------- F01 main revolve
    # One (r,z) profile: centre bore + post, conical recess, hub ring, plate, back bead,
    # cup wall, flange with gasket lip, and the hub tube (stepped bore, full-round bottom). Edge rounds
    # measured in the profile are drawn as tangent arcs of the profile (not fillet ops).
    zu = P["plate_under_z"]
    zb = P["plate_back_z"]
    z_cone_bot = P["hub_ring_top_z"] - P["cone_slope"] * (P["cone_R_top"] - P["centre_bore_r"])
    ht = (P["hub_tube_R_out"] - P["hub_bore_R_lower"]) / 2   # hub tube full-round bottom
    lp = (P["flange_R_out"] - P["lip_R_in"]) / 2               # lip full-round top
    bd = (P["bead_R_out"] - P["bead_R_in"]) / 2                # bead full-round top
    prof = [
        (P["centre_bore_r"], z_cone_bot, 0),
        (P["centre_bore_r"], P["centre_post_bot_z"], 0),
        (P["centre_post_R_out"], P["centre_post_bot_z"], 0),
        (P["centre_post_R_out"], zu, 0),
        (P["hub_bore_R_upper"], zu, 0),
        (P["hub_bore_R_upper"], P["hub_bore_step_z"], 0),
        (P["hub_bore_R_lower"], P["hub_bore_step_z"], 0),
        (P["hub_bore_R_lower"], P["hub_tube_bot_z"], ht),
        (P["hub_tube_R_out"], P["hub_tube_bot_z"], ht),
        (P["hub_tube_R_out"], zu, 0),
        (P["cup_R_in"], zu, 0),
        (P["cup_R_in"], P["flange_bot_z"], P["flange_inner_round_R"]),
        (P["flange_R_out"], P["flange_bot_z"], P["flange_outer_round_R"]),
        (P["flange_R_out"], P["lip_top_z"], lp),
        (P["lip_R_in"], P["lip_top_z"], lp),
        (P["lip_R_in"], P["flange_top_z"], P["flange_lip_fillet_R"]),
        (P["cup_R_out"], P["flange_top_z"], P["wall_flange_fillet_R"]),
        (P["cup_R_out"], zb, P["plate_edge_round_R"]),
        (P["bead_R_out"], zb, 0),
        (P["bead_R_out"], P["bead_top_z"], bd),
        (P["bead_R_in"], P["bead_top_z"], bd),
        (P["bead_R_in"], zb, 0),
        (P["hub_ring_R_out"], zb, 0),
        (P["hub_ring_R_out"], P["hub_ring_top_z"], 0),
        (P["cone_R_top"], P["hub_ring_top_z"], 0),
    ]
    body = revolve(rounded_profile(prof), Axis.Z, 360)
    flog.log(f"F01 revolve (r,z) profile, {len(prof)} vertices; cone bottom z={z_cone_bot:.4f}; faces={len(body.faces())}")

    # ---------------------------------------------------------------- F01b lip outer bead (360 deg lens)
    r_in_lens = P["flange_R_out"] - lp            # lens chord buried in the lip mid-wall
    with BuildLine() as bl:
        Line(Vector(r_in_lens, 0, P["lip_bead_z_lo"]), Vector(P["flange_R_out"], 0, P["lip_bead_z_lo"]))
        ThreePointArc(Vector(P["flange_R_out"], 0, P["lip_bead_z_lo"]), Vector(P["lip_bead_R"], 0, P["lip_bead_z"]),
                      Vector(P["flange_R_out"], 0, P["lip_bead_z_hi"]))
        Line(Vector(P["flange_R_out"], 0, P["lip_bead_z_hi"]), Vector(r_in_lens, 0, P["lip_bead_z_hi"]))
        Line(Vector(r_in_lens, 0, P["lip_bead_z_hi"]), Vector(r_in_lens, 0, P["lip_bead_z_lo"]))
    body = body + revolve(Face(Wire(bl.edges())), Axis.Z, 360)
    flog.log(f"F01b lip bead: arc through r={P['lip_bead_R']} at z={P['lip_bead_z']}, z {P['lip_bead_z_lo']}..{P['lip_bead_z_hi']}")

    # ---------------------------------------------------------------- F02 bayonet tabs x3
    tr = (P["tab_top_z"] - P["tab_bot_z"]) / 2                   # tab outer end full round
    r_root = P["flange_R_out"] - lp                                # tab root buried in the lip mid-wall (no coincident faces)
    tab_prof = [(r_root, P["tab_bot_z"], 0), (P["tab_R_out"], P["tab_bot_z"], tr),
                (P["tab_R_out"], P["tab_top_z"], tr), (r_root, P["tab_top_z"], 0)]
    n_tab = P["tab_count"]
    for k in range(n_tab):
        a_c = P["tab_phase_deg"] + k * P["tab_pitch_deg"]
        body = body + sector_revolve(tab_prof, a_c - P["tab_span_deg"] / 2, P["tab_span_deg"])
    flog.log(f"F02 {n_tab} tabs, span {P['tab_span_deg']} deg, centres {[round(P['tab_phase_deg'] + k * P['tab_pitch_deg'], 2) for k in range(n_tab)]}")

    # ---------------------------------------------------------------- F03 radial ribs x6
    t = P["rib_t"]
    r0, r1, rs = P["hub_tube_R_out"] - OVL, P["cup_R_in"] + OVL, P["rib_step_r"]
    shallow = Pos((r0 + rs) / 2, 0, (P["rib_shallow_bot_z"] + zu + OVL) / 2) * Box(rs - r0, t, zu + OVL - P["rib_shallow_bot_z"])
    deep = Pos((rs + r1) / 2, 0, (P["flange_bot_z"] + zu + OVL) / 2) * Box(r1 - rs, t, zu + OVL - P["flange_bot_z"])
    rib = shallow + deep
    n_rib = P["rib_count"]
    rib_angles = [P["rib_phase_deg"] + k * P["rib_pitch_deg"] for k in range(n_rib)]
    for a in rib_angles:
        body = body + Rot(0, 0, a) * rib
    flog.log(f"F03 {n_rib} ribs t={t} at {[round(a, 2) for a in rib_angles]}; shallow bottom {P['rib_shallow_bot_z']} r<{rs}, deep bottom = flange_bot_z beyond")

    # ---------------------------------------------------------------- F04 ring-rib arcs
    ring_prof = [(P["ring_rib_R_in"], P["ring_rib_bot_z"], 0), (P["ring_rib_R_out"], P["ring_rib_bot_z"], 0),
                 (P["ring_rib_R_out"], zu + OVL, 0), (P["ring_rib_R_in"], zu + OVL, 0)]
    arcs = P.group("ring_rib_arcs_deg")
    r_mid = (P["ring_rib_R_in"] + P["ring_rib_R_out"]) / 2
    ext = math.degrees(t / 2 / r_mid)          # overlap each arc end into its rib by half a rib thickness
    for a0, a1 in zip(arcs[0::2], arcs[1::2]):
        body = body + sector_revolve(ring_prof, a0 - ext, (a1 - a0) + 2 * ext)
    flog.log(f"F04 ring-rib arcs {list(zip(arcs[0::2], arcs[1::2]))} (+/-{ext:.2f} deg overlap into ribs)")

    # ---------------------------------------------------------------- F05 screw bosses x4
    bosses = []
    for pre in ("bossA", "bossB"):
        for th in P.group(f"{pre}_theta_deg"):
            bosses.append((P[f"{pre}_r"], th, P[f"{pre}_bot_z"]))
    for rr, th, zbot in bosses:
        h = zu + OVL - zbot
        body = body + Rot(0, 0, th) * Pos(rr, 0, zbot) * Cylinder(P["boss_R_out"], h, align=(Align.CENTER, Align.CENTER, Align.MIN))
    flog.log(f"F05 {len(bosses)} bosses R={P['boss_R_out']}: {[(round(b[0], 2), b[1], b[2]) for b in bosses]}")

    # ---------------------------------------------------------------- F05b webs hub -> boss pair A -> cup wall
    web_len = (P["cup_R_in"] + OVL) - (P["hub_tube_R_out"] - OVL)
    web = Pos(P["hub_tube_R_out"] - OVL + web_len / 2, 0, (P["webA_bot_z"] + zu + OVL) / 2) * Box(web_len, P["webA_t"], zu + OVL - P["webA_bot_z"])
    for th in P.group("bossA_theta_deg"):
        body = body + Rot(0, 0, th) * web
    flog.log(f"F05b 2 webs t={P['webA_t']} bottom {P['webA_bot_z']} through boss pair A, hub tube to cup wall")

    # ---------------------------------------------------------------- F06 cut tools, subtracted once
    tools = None
    for rr, th, zbot in bosses:   # counterbore + pilot hole from each boss mouth
        cb = Pos(rr, 0, zbot - OVS) * Cylinder(P["boss_cb_r"], P["boss_cb_depth"] + OVS, align=(Align.CENTER, Align.CENTER, Align.MIN))
        hole = Pos(rr, 0, zbot - OVS) * Cylinder(P["boss_hole_r"], P["boss_hole_depth"] + OVS, align=(Align.CENTER, Align.CENTER, Align.MIN))
        tl = Rot(0, 0, th) * (cb + hole)
        tools = tl if tools is None else tools + tl
    r_si = P["hub_ring_R_out"] - EPS
    slot_prof = [(r_si, zu - OVS, 0), (P["slot_R_out"], zu - OVS, 0),
                 (P["slot_R_out"], P["hub_ring_top_z"] + OVS, 0), (r_si, P["hub_ring_top_z"] + OVS, 0)]
    n_slot = P["slot_count"]
    for k in range(n_slot):
        a_c = P["slot_phase_deg"] + k * 360.0 / n_slot
        tools = tools + sector_revolve(slot_prof, a_c - P["slot_span_deg"] / 2, P["slot_span_deg"])
    body = body - tools
    flog.log(f"F06 cut once: {len(bosses)} counterbored pilot holes + {n_slot} through slots (span {P['slot_span_deg']} deg, phase {P['slot_phase_deg']})")
    return body.clean()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="params-driven build123d model (stl-re-rebuild-build123d template)")
    ap.add_argument("--params", type=Path)
    ap.add_argument("--alignment", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--part", default="OD-G04_brewing-gasket-support")
    ap.add_argument("--scripts", type=Path, help="stl-re-rebuild-build123d/scripts folder")
    a = ap.parse_args(argv)
    if not (a.params and a.alignment and a.out):
        ap.error("--params, --alignment and --out are required")
    sys.path.insert(0, str(find_scripts(a.scripts)))
    from export_frames import ExportAbort, export_frames
    from fillet_log import FilletLog

    import build123d

    P = Params(a.params)
    flog = FilletLog()
    flog.log(f"build123d {build123d.__version__}  params={a.params}")  # version drift is real
    body = build(P, flog)
    if P.unused():
        flog.log(f"UNUSED params (plan/measure mismatch?): {P.unused()}")
    a.out.mkdir(parents=True, exist_ok=True)
    flog.write(a.out / "fillets.json", a.out / "build_log.txt", inputs=[a.params, Path(__file__)])
    from export_frames import ScaleFrameSkipped

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
