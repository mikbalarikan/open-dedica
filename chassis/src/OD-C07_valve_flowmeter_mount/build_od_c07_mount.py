"""Build od_c07_mount, concept C1, spec 1.1 (job 20260930-od-c07-valve-flowmeter-mount).

build123d Algebra mode, one parameter structure (Params) and no magic numbers below it
except geometric overcut allowances named in Params. Frame (spec §2): bottom face z = 0,
+Z up and print direction, origin on the OD-H24 axis, valve axis at (62.0, 0).
OD-H24 and OD-H22 are placed by RigidJoints from their measured datum features
(DESIGN_PLAN §5), never by bounding boxes.

Usage (from the repository root, after `source $HOME/oguz.env`):
  uv run tools/run.py python <ws>/01_CAD/build_od_c07_mount.py            # deliverable v01
  uv run tools/run.py python <ws>/01_CAD/build_od_c07_mount.py --set ring_ri=16.25 --outdir 01_CAD/sweep_v01/ring_ri_low
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import asdict, dataclass, field, fields, replace
from pathlib import Path

from build123d import (Align, Axis, Box, Circle, Compound, Cylinder, GeomType, Location, Plane, Polygon, Rectangle,
                       RigidJoint, extrude, revolve)

from tools.core import brep_valid, fillet_ladder, read_step, solid_count, step_roundtrip, write_step, write_stl
from tools.measure import bore_census, clearance
from tools.result import MEASURED

HERE = Path(__file__).resolve().parent
WS = HERE.parent
TIMESTAMP = "2026-09-30T12:00:00"


@dataclass(frozen=True)
class Params:
    # plate (§4 C1)
    plate_x0: float = -25.0
    plate_x1: float = 94.0
    plate_y: float = 25.0
    plate_t: float = 4.0
    window_x0: float = 40.0
    window_x1: float = 84.0
    foot_x: tuple = (-18.0, 88.5)
    foot_y: float = 21.0
    foot_hole_d: float = 3.4
    # flowmeter station
    ped_r: float = 18.0
    ped_top_z: float = 10.0
    recess_r: float = 14.10
    recess_depth: float = 0.60
    recess_chamfer: float = 0.20         # fix cycle 2: 45° edge break on the recess rim, clears the OD-H24 ribs by >= 0.5 (REQ-02)
    ring_ri: float = 16.30
    ring_ro: float = 18.30
    ring_top_z: float = 13.0
    ring_lip_rise: float = 0.52          # chamfer under the ring's 0.30 overhang: 0.30 radial x 0.52 up (60° from horizontal)
    notch_theta: tuple = (25.0, 115.0, 225.0)
    notch_w: float = 2.0
    notch_h: float = 0.5
    pin1_xy: tuple = (0.185, 0.093)
    pin1_d: float = 4.8
    pin2_xy: tuple = (-11.78, 0.14)
    pin2_d: float = 3.8
    hook_theta: tuple = (70.0, 160.0, 320.0)
    hook_ri: float = 20.87
    hook_t: float = 2.0
    hook_w: float = 6.0                  # chord at the beam mid radius
    catch_under_z: float = 29.9
    catch_reach: float = 2.0             # catch inner R = hook_ri - catch_reach = 18.87
    catch_land: float = 1.6              # fix cycle 2: U-06 wide reads the catch tip (underside vs 45° lead-in) as a wall of this height
    lead_in_deg: float = 45.0
    # valve station
    valve_x: float = 62.0
    leg_gap_half: float = 22.0           # inner faces at valve_x ± 22 = 40.0 / 84.0
    leg_t: float = 4.0
    deck_y: float = 15.0
    deck_top_z: float = 48.0
    deck_t: float = 7.7
    slot_w: float = 14.1
    slit_w: float = 2.40
    slit_x_top: float = 11.85
    slit_angle: float = 43.42
    screw_dx: tuple = (15.447, -15.338)
    screw_clear_d: float = 3.4
    screw_clear_depth: float = 2.0
    insert_d: float = 4.0
    insert_depth: float = 5.7
    # fillet ladders (descending), DESIGN_PLAN §4
    fillet_leg: tuple = (3.0, 2.0, 1.0)
    fillet_ped: tuple = (1.0, 0.5)
    fillet_hook: tuple = (1.5, 1.0, 0.5)
    fillet_ring: tuple = (0.3, 0.2, 0.1)
    ring_gap_min: float = 0.50           # REQ-01 lower bound, the ring-root rung acceptance
    # geometric allowances (overcuts past faces so no cut is coplanar with a face it must clear)
    over: float = 1.0
    # checks and exports
    h24_path: tuple = (25.0, 20.0, 15.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.0)
    h22_slide: tuple = (45.0, 35.0, 25.0, 16.0, 12.0, 8.0, 4.0, 2.0, 0.0)
    h22_lift: float = 0.5
    h22_lower: tuple = (0.25, 0.0)
    expected_bores: int = 12
    stl_tol: float = 0.01
    stl_angular: float = 0.05            # <= 4·acos(1 − 0.01/22.87) = 0.1183 (U-07); at 0.1183 the mesher left 0.037 mm sagitta on the ring root fillet

    @property
    def hook_ro(self):
        return self.hook_ri + self.hook_t

    @property
    def catch_ri(self):
        return self.hook_ri - self.catch_reach

    @property
    def hook_top_z(self):
        return self.catch_under_z + self.catch_land + self.catch_reach * math.tan(math.radians(self.lead_in_deg))

    @property
    def deck_bot_z(self):
        return self.deck_top_z - self.deck_t


def params_from(settings) -> Params:
    p = Params()
    types = {f.name: f.type for f in fields(Params)}
    kw = {}
    for s in settings:
        k, v = s.split("=", 1)
        if k not in types:
            raise SystemExit(f"unknown parameter {k}")
        cur = getattr(p, k)
        kw[k] = tuple(float(x) for x in v.split(",")) if isinstance(cur, tuple) else type(cur)(v)
    return replace(p, **kw)


def sha256(path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


# ---------------------------------------------------------------- primitives
def box(x0, x1, y0, y1, z0, z1):
    return Box(x1 - x0, y1 - y0, z1 - z0, align=(Align.MIN, Align.MIN, Align.MIN)).moved(Location((x0, y0, z0)))


def cyl(r, z0, z1, cx=0.0, cy=0.0):
    return Cylinder(r, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((cx, cy, z0)))


def wedge(theta_deg, half_deg, reach, z0, z1):
    a0, a1 = math.radians(theta_deg - half_deg), math.radians(theta_deg + half_deg)
    tri = Polygon((0, 0), (reach * math.cos(a0), reach * math.sin(a0)), (reach * math.cos(a1), reach * math.sin(a1)),
                  align=None)
    return extrude(tri, amount=z1 - z0).moved(Location((0, 0, z0)))


def edges_at_z(shape, z, keep):
    """Edges lying in the plane z (both ends and midpoint), filtered by keep(midpoint)."""
    out = []
    for e in shape.edges():
        bb = e.bounding_box()
        if abs(bb.min.Z - z) > 1e-6 or abs(bb.max.Z - z) > 1e-6:
            continue
        m = e.position_at(0.5)
        if keep(m):
            out.append(e)
    return out


# ---------------------------------------------------------------- OEM placement by joints
def _datum(solid, face_area_min, axis_d, axis_tol):
    """Datum of an OEM solid from measured features: the largest planar face facing -Z at z 0
    (the seating face), the bore of diameter axis_d (the axis). Returns Location and facts."""
    seat = [f for f in solid.faces() if f.geom_type == GeomType.PLANE and f.normal_at().Z < -0.999999
            and abs(f.center().Z) < 1e-6 and f.area > face_area_min]
    seat.sort(key=lambda f: -f.area)
    if not seat:
        raise RuntimeError("seating face not found")
    census = bore_census(solid)
    if census.status != MEASURED:
        raise RuntimeError(f"bore census: {census.reason}")
    axis = [b for b in census.detail["bores"] if abs(b["diameter"] - axis_d) < axis_tol
            and abs(abs(b["axis_dir"][2]) - 1) < 1e-6]
    if not axis:
        raise RuntimeError(f"axis bore Ø{axis_d} not found")
    ax = axis[0]["start"]
    return seat[0], (ax[0], ax[1], seat[0].center().Z), census


def place_oem(inputs: Path):
    """Read both OEM solids and place them with RigidJoints on a frame anchor at the spec §2 seats."""
    p = Params()
    h24 = read_step(inputs / "OD-H24_flowmeter.step")
    h22 = read_step(inputs / "OD-H22_3way_valve.step")
    rim, o24, _ = _datum(h24, 50.0, 27.96, 0.1)
    flange, o22, c22 = _datum(h22, 200.0, 9.122, 0.05)
    ears = [b for b in c22.detail["bores"] if abs(b["diameter"] - 3.872) < 0.05 and abs(abs(b["axis_dir"][2]) - 1) < 1e-6]
    if len(ears) != 2:
        raise RuntimeError(f"expected 2 ear holes, found {len(ears)}")
    ears.sort(key=lambda b: b["start"][0])
    ear_dir = math.degrees(math.atan2(ears[1]["start"][1] - ears[0]["start"][1], ears[1]["start"][0] - ears[0]["start"][0]))
    # the datum frames: origins on the measured axes at the measured seating faces, +X through the ear holes
    RigidJoint("datum", h24, joint_location=Location(o24))
    RigidJoint("datum", h22, joint_location=Location(o22, (0, 0, ear_dir)))
    anchor = box(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5)
    RigidJoint("h24_seat", anchor, joint_location=Location((0.0, 0.0, p.ped_top_z)))
    RigidJoint("h22_seat", anchor, joint_location=Location((p.valve_x, 0.0, p.deck_top_z)))
    anchor.joints["h24_seat"].connect_to(h24.joints["datum"])
    anchor.joints["h22_seat"].connect_to(h22.joints["datum"])
    flange_placed = flange.moved(h22.location)
    facts = {"OD-H24": {"rim_face_area_mm2": round(rim.area, 3), "axis_origin": [round(v, 6) for v in o24],
                        "placed_location": [round(v, 6) for v in h24.location.position]},
             "OD-H22": {"flange_face_area_mm2": round(flange.area, 3), "axis_origin": [round(v, 6) for v in o22],
                        "ear_holes_x": [round(e["start"][0], 4) for e in ears], "ear_axis_deg": round(ear_dir, 6),
                        "placed_location": [round(v, 6) for v in h22.location.position]}}
    return {"h24": h24, "h22": h22, "flange_face": flange_placed, "facts": facts}


# ---------------------------------------------------------------- the part
def slot_and_slits(p: Params):
    """The stem U-slot (semicircle on -Y, open to +Y) and the two gusset slits, as cutters."""
    vc = p.valve_x
    z0, z1 = p.deck_bot_z - p.over, p.deck_top_z + p.over
    slot = cyl(p.slot_w / 2, z0, z1, vc, 0.0) + box(vc - p.slot_w / 2, vc + p.slot_w / 2, 0.0, p.deck_y + p.over, z0, z1)
    a = math.radians(p.slit_angle)
    slits = None
    for s in (1, -1):
        top = p.deck_top_z + p.over
        bot = p.deck_bot_z - p.over
        x_top = p.slit_x_top + p.over / math.tan(a)           # the end line carried above the top face
        x_bot = p.slit_x_top - (p.deck_top_z - bot) / math.tan(a)
        prof = Polygon((vc, top), (vc + s * x_top, top), (vc + s * x_bot, bot), (vc, bot), align=None)
        sl = extrude(Plane.XZ * prof, amount=p.slit_w / 2, both=True)
        slits = sl if slits is None else slits + sl
    return slot + slits


def make_hooks(p: Params, rf: float):
    """F07: the hook RZ profile (beam, catch, 45° lead-in) plus its root fillet webs of radius rf on
    the plate top at the inner and outer beam faces, revolved about Z and cut to each hook's sector."""
    ri, ro, zc, zb = p.hook_ri, p.hook_ro, p.catch_under_z, p.plate_t
    profile = Polygon((ri, zb), (ro, zb), (ro, p.hook_top_z), (ri, p.hook_top_z),
                      (p.catch_ri, zc + p.catch_land), (p.catch_ri, zc), (ri, zc), align=None)
    if rf > 0:
        web_in = Rectangle(rf, rf, align=(Align.MIN, Align.MIN)).moved(Location((ri - rf, zb))) - \
            Circle(rf).moved(Location((ri - rf, zb + rf)))
        web_out = Rectangle(rf, rf, align=(Align.MIN, Align.MIN)).moved(Location((ro, zb))) - \
            Circle(rf).moved(Location((ro + rf, zb + rf)))
        profile = profile + web_in + web_out
    ring = revolve(Plane.XZ * profile, Axis.Z)
    half = math.degrees(math.asin(p.hook_w / 2 / (ri + p.hook_t / 2)))
    return [ring & wedge(th, half, 3 * (ro + rf + 1.0), zb - p.over, p.hook_top_z + p.over) for th in p.hook_theta]


def build(p: Params, h24=None):
    facts = {"fillets": {}}
    # F01 plate, F02 window
    plate = box(p.plate_x0, p.plate_x1, -p.plate_y, p.plate_y, 0.0, p.plate_t)
    window = box(p.window_x0, p.window_x1, -p.plate_y - p.over, p.plate_y + p.over, -p.over, p.plate_t + p.over)
    plate = plate - window
    # F04 pedestal, F05 ring wall
    pedestal = cyl(p.ped_r, p.plate_t, p.ped_top_z)
    ring = cyl(p.ring_ro, p.ped_top_z, p.ring_top_z) - cyl(p.ring_ri, p.ped_top_z - p.over, p.ring_top_z + p.over)
    ri, ro = p.hook_ri, p.hook_ro
    # F08 legs
    vc = p.valve_x
    leg_a = box(vc - p.leg_gap_half - p.leg_t, vc - p.leg_gap_half, -p.deck_y, p.deck_y, p.plate_t, p.deck_top_z)
    leg_b = box(vc + p.leg_gap_half, vc + p.leg_gap_half + p.leg_t, -p.deck_y, p.deck_y, p.plate_t, p.deck_top_z)
    # F09 deck: it joins the two plate pieces the window leaves, so it goes in before the fillets
    deck = box(vc - p.leg_gap_half, vc + p.leg_gap_half, -p.deck_y, p.deck_y, p.deck_bot_z, p.deck_top_z)
    body = plate + pedestal + ring + leg_a + leg_b + deck
    body = body.clean()

    # F14 root fillets, each group through its ladder
    leg_x = [(vc - p.leg_gap_half - p.leg_t, vc - p.leg_gap_half), (vc + p.leg_gap_half, vc + p.leg_gap_half + p.leg_t)]
    inner_x = (vc - p.leg_gap_half, vc + p.leg_gap_half)

    def leg_edge(m):
        on_leg = any(a - 1e-6 <= m.X <= b + 1e-6 for a, b in leg_x) and abs(m.Y) <= p.deck_y + 1e-6
        return on_leg and all(abs(m.X - x) > 1e-6 for x in inner_x)

    groups = [
        ("leg roots", lambda s: edges_at_z(s, p.plate_t, leg_edge), p.fillet_leg),
        ("pedestal root", lambda s: edges_at_z(s, p.plate_t, lambda m: abs(math.hypot(m.X, m.Y) - p.ped_r) < 1e-4), p.fillet_ped),
    ]
    for name, pick, ladder in groups:
        edges = pick(body)
        res = fillet_ladder(body, edges, ladder)
        facts["fillets"][name] = {"edges": len(edges), "requested": list(ladder), "achieved": res.radius,
                                  "tried": [list(t) for t in res.tried]}
        body = res.shape
    # F07 hooks with their root fillets in the revolved profile, through the ladder: a rung counts
    # when the body stays one valid solid (the fillets are exact tori cut by the sector planes, so
    # they survive the STEP round trip; see REPORT §8)
    achieved, tried = None, []
    for rf in p.fillet_hook:
        try:
            cand = body
            for h in make_hooks(p, rf):
                cand = cand + h
            cand = cand.clean()
            n, ok = solid_count(cand), brep_valid(cand)
            if n.measured == 1 and ok.status == MEASURED and ok.measured == 1:
                body, achieved = cand, rf
                break
            tried.append([rf, f"{n.measured} solid(s), brep_valid {ok.measured}"])
        except Exception as exc:  # noqa: BLE001  the next rung
            tried.append([rf, type(exc).__name__])
    if achieved is None:
        for h in make_hooks(p, 0.0):
            body = body + h
        body = body.clean()
    facts["fillets"]["hook roots (inner and outer faces)"] = {"requested": list(p.fillet_hook), "achieved": achieved, "tried": tried}
    facts["hook_half_angle_deg"] = math.degrees(math.asin(p.hook_w / 2 / (ri + p.hook_t / 2)))

    # the ring inner root: a rung counts only if the ring keeps REQ-01's gap to the cup
    ring_edges = edges_at_z(body, p.ped_top_z, lambda m: abs(math.hypot(m.X, m.Y) - p.ring_ri) < 1e-4)
    achieved, tried = None, []
    for r in p.fillet_ring:
        res = fillet_ladder(body, ring_edges, [r])
        if res.radius is None:
            tried.append([r, res.tried[0][1] if res.tried else "failed"])
            continue
        if h24 is not None:
            region = cyl(p.ring_ro + p.over, p.ped_top_z, p.ring_top_z + p.over) - cyl(p.ring_ri - 0.05, p.ped_top_z - p.over, p.ring_top_z + 2 * p.over)
            gap = clearance(res.shape & region, h24)
            if gap.status != MEASURED or gap.measured < p.ring_gap_min:
                tried.append([r, f"ring gap {gap.measured}"])
                continue
        body, achieved = res.shape, r
        break
    facts["fillets"]["ring inner root"] = {"edges": len(ring_edges), "requested": list(p.fillet_ring), "achieved": achieved,
                                           "tried": tried}

    # F05b ring lip chamfer under the ring's overhang past the pedestal
    lip = Polygon((p.ped_r, p.ped_top_z), (p.ring_ro + p.over, p.ped_top_z),
                  (p.ring_ro + p.over, p.ped_top_z + p.ring_lip_rise * (p.ring_ro + p.over - p.ped_r) / (p.ring_ro - p.ped_r)),
                  align=None)
    body = body - revolve(Plane.XZ * lip, Axis.Z)
    # F03 footprint holes
    for x in p.foot_x:
        for s in (1, -1):
            body = body - cyl(p.foot_hole_d / 2, -p.over, p.plate_t + p.over, x, s * p.foot_y)
    # P-3 recess, F06 pin clearance holes
    body = body - cyl(p.recess_r, p.ped_top_z - p.recess_depth, p.ped_top_z + p.over)
    if p.recess_chamfer > 0:
        c = p.recess_chamfer
        brk = Polygon((p.recess_r, p.ped_top_z - c), (p.recess_r + c, p.ped_top_z), (p.recess_r + c, p.ped_top_z + p.over),
                      (p.recess_r, p.ped_top_z + p.over), align=None)
        body = body - revolve(Plane.XZ * brk, Axis.Z)
    for (xy, d) in ((p.pin1_xy, p.pin1_d), (p.pin2_xy, p.pin2_d)):
        body = body - cyl(d / 2, -p.over, p.ped_top_z, xy[0], xy[1])
    # P-5 drain notches through the ring base
    for th in p.notch_theta:
        n = box(p.ring_ri - p.over, p.ring_ro + p.over, -p.notch_w / 2, p.notch_w / 2, p.ped_top_z, p.ped_top_z + p.notch_h)
        body = body - n.rotate(Axis.Z, th)
    # F10/P-1 stem U-slot, F11/P-2 gusset slits
    body = body - slot_and_slits(p)
    # F12 screw clearance holes, F13 insert bores
    for dx in p.screw_dx:
        body = body - cyl(p.screw_clear_d / 2, p.deck_top_z - p.screw_clear_depth, p.deck_top_z + p.over, vc + dx, 0.0)
        body = body - cyl(p.insert_d / 2, p.deck_bot_z - p.over, p.deck_bot_z + p.insert_depth, vc + dx, 0.0)
    body = body.clean()
    solids = list(body.solids())
    if len(solids) != 1:
        raise RuntimeError(f"build gave {len(solids)} solids")
    part = solids[0]
    part.label = "od_c07_mount"
    return part, facts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", action="append", default=[])
    ap.add_argument("--outdir", default="02_STEP_STL")
    ap.add_argument("--tag", default="v01")
    ap.add_argument("--no-assembly", action="store_true")
    a = ap.parse_args()
    p = params_from(a.set)
    out = WS / a.outdir
    out.mkdir(parents=True, exist_ok=True)
    oem = place_oem(WS / "00_Spec" / "inputs")
    part, facts = build(p, oem["h24"])
    step = out / f"od_c07_mount_C1_{a.tag}.step"
    rt = step_roundtrip(part, step, timestamp=TIMESTAMP)
    facts["roundtrip"] = {k: (r.measured, r.status, r.reason) for k, r in rt.items()}
    back = read_step(step)
    stl = out / f"od_c07_mount_C1_{a.tag}.stl"
    w = write_stl(back, stl, tolerance=p.stl_tol, angular_tolerance=p.stl_angular)
    facts["stl"] = w.detail
    files = {str(step.relative_to(WS)): sha256(step), str(stl.relative_to(WS)): sha256(stl)}
    if not a.no_assembly:
        m = back.solids()[0] if hasattr(back, "solids") else back
        m.label = "od_c07_mount"
        h22 = oem["h22"].moved(Location())
        h24 = oem["h24"].moved(Location())
        h22.label, h24.label = "OD-H22", "OD-H24"
        asm = Compound(label="od_c07_assembly", children=[m, h22, h24])
        asm_path = out / f"od_c07_assembly_C1_{a.tag}.step"
        write_step(asm, asm_path, timestamp=TIMESTAMP)
        files[str(asm_path.relative_to(WS))] = sha256(asm_path)
    facts["params"] = asdict(p)
    facts["placement"] = oem["facts"]
    facts["files"] = files
    facts["volume_mm3"] = part.volume
    facts_dir = HERE / "check_out_v01" if a.outdir == "02_STEP_STL" else out   # nothing but geometry in 02_STEP_STL
    facts_dir.mkdir(parents=True, exist_ok=True)
    (facts_dir / f"build_facts_{a.tag}.json").write_text(json.dumps(facts, indent=1, default=str))
    print(json.dumps({"files": files, "fillets": facts["fillets"], "roundtrip": facts["roundtrip"],
                      "stl": {k: facts["stl"][k] for k in ("triangles", "max_sagitta_mm")}}, indent=1, default=str))


if __name__ == "__main__":
    main()
