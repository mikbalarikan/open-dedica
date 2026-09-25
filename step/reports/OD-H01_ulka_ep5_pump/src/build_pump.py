"""OD-H01 pump (ULKA-type vibration pump) - design-intent rebuild from scan.

Frame: datum frame "T1" = pump axis on +Z (outlet toward -Z, inlet barb +Z),
X = normal of the steel frame side plates, origin on the axis. All values in mm,
measured from the scan (see params in report). Exports STEP in the datum frame
and in the original STL frame (inverse of T1) for overlay.
"""

import math
import sys
from pathlib import Path

import numpy as np
from build123d import (
    Kind,
    offset,
    Align,
    Axis,
    Box,
    BuildLine,
    BuildPart,
    BuildSketch,
    Circle,
    Cylinder,
    Location,
    Locations,
    Mode,
    Plane,
    Polyline,
    Pos,
    Rectangle,
    RectangleRounded,
    Rot,
    SlotCenterToCenter,
    export_step,
    export_stl,
    extrude,
    fillet,
    make_face,
    make_hull,
    revolve,
)

P = dict(
    # revolve - outlet side (r, z)
    tip_z=-66.45, tip_chamfer=0.4, flat_af=11.6, flat_z0=-53.7, flat_z1=-47.6, bore_r=4.55, bore_depth=7.0,
    r_nozzle=7.00, z_nozzle=-60.0,
    r_t1=6.92, z_t1=-54.0,
    r_t2=6.78, z_t2=-40.7,
    r_t3=6.57, z_t3=-36.0,
    r_t4=6.74, z_step=-32.75,
    r_s1=10.25, z_cone0=-26.4, z_cone1=-24.5,
    r_body=12.0,
    # revolve - inlet side
    z_rear=37.65, r_washer=7.85, z_washer=38.15, r_boss=6.50, z_boss=42.2,
    r_ring=6.85, z_ring=43.6, r_barb=2.95, r_barb_ridge=3.48,
    z_barb1=47.3, z_ridge1=47.9, z_barb2=50.25, z_ridge2=50.9, z_tip_in=55.5,
    r_in_bore=1.5,
    # coil
    r_coil=23.65, coil_cx=-0.2, coil_cy=0.1, z_coil0=-8.8, z_coil1=34.5, r_core=8.0, coil_fillet=1.0,
    # steel U-frame (band, extruded along Y)
    fx0=-27.2, fx1=26.85, fz0=-12.4, fz1=37.65, fy=16.2, ft=3.1, fr_out=4.5,
    notch_y=3.3, notch_x=22.4, notch_z=-6.75,
    slot_front_w=2.6, slot_front_y0=11.5, rear_slot_w=4.2, rear_slot_y0=12.0, rear_slot_depth=0.85,
    # diamond flange + screws
    dia_r_center=12.05, dia_lobe_r=3.9, dia_lobe_x=19.2, dia_z0=-12.4, dia_z1=-18.7,
    pocket_rim=1.2, boss_r=5.1, pocket_z=-16.5,
    win_w=2.4, win_y=10.3, win_z0=-16.9, win_z1=-13.8,
    screw_centers=((19.0, -0.3), (-19.2, 0.15)), screw_r=3.85, screw_z1=-21.9,
    recess_ang=(70.0, 60.0), recess_w=1.3, recess_l=4.6, recess_z=-20.3,
    # terminal block + tabs + rib + housing
    tb_x0=-23.05, tb_x1=22.65, tb_y0=-31.4, tb_ystep=-22.3, tb_y1=-9.0, tb_z0=-9.4, tb_z0b=-8.85, tb_z1=-3.3, tb_z1b=-3.3, tb_step_x1=3.0, tb_step_y1=-26.5, tb_step_z=-3.78, tb_fillet=1.5,
    tabpk_y1=-29.6, tabpk_z0=-6.35,
    tab_y0=-30.95, tab_y1=-30.15, tab_z1=5.5, tabA=(-18.4, -11.9), tabB=(-5.6, 0.8),
    rib_x=(-10.2, -8.6),
    hs_cx=12.89, hs_cy=-22.59, hs_ang=29.6, hs_l=11.5, hs_w=5.0, hs_z1=13.6, hs_fillet=0.9,
)


def revolve_body():
    p = P
    front = [
        (0, p["tip_z"]),
        (p["bore_r"], p["tip_z"]),
        (p["r_nozzle"] - p["tip_chamfer"], p["tip_z"]),
        (p["r_nozzle"], p["tip_z"] + p["tip_chamfer"]),
        (p["r_nozzle"], p["z_nozzle"]),
        (p["r_t1"], p["z_nozzle"]),
        (p["r_t1"], p["z_t1"]),
        (p["r_t2"], p["z_t1"]),
        (p["r_t2"], p["z_t2"]),
        (p["r_t3"], p["z_t2"]),
        (p["r_t3"], p["z_t3"]),
        (p["r_t4"], p["z_t3"]),
        (p["r_t4"], p["z_step"]),
        (p["r_s1"], p["z_step"]),
        (p["r_s1"], p["z_cone0"]),
        (p["r_body"], p["z_cone1"]),
        (p["r_body"], p["fz0"] + 1.0),
        (0, p["fz0"] + 1.0),
    ]
    rear = [
        (0, p["z_rear"] - 1.0),
        (p["r_washer"], p["z_rear"] - 1.0),
        (p["r_washer"], p["z_washer"]),
        (p["r_boss"], p["z_washer"]),
        (p["r_boss"], p["z_boss"]),
        (p["r_ring"], p["z_boss"] + 0.2),
        (p["r_ring"], p["z_ring"]),
        (p["r_barb"], p["z_ring"]),
        (p["r_barb"], p["z_barb1"]),
        (p["r_barb_ridge"], p["z_ridge1"]),
        (3.05, p["z_barb2"]),
        (p["r_barb_ridge"] - 0.01, p["z_ridge2"]),
        (2.95, p["z_tip_in"] - 0.5),
        (2.6, p["z_tip_in"]),
        (0, p["z_tip_in"]),
    ]
    parts = []
    for pts in (front, rear):
        with BuildPart() as bp:
            with BuildSketch(Plane.XZ):
                with BuildLine():
                    Polyline(*pts, close=True)
                make_face()
            revolve(axis=Axis.Z)
        parts.append(bp.part)
    body = parts[0] + parts[1]
    # visible bores (nozzle bore at outlet; barb bore through the barb)
    body -= Pos(0, 0, p["tip_z"]) * Cylinder(p["bore_r"], p["bore_depth"], align=(Align.CENTER, Align.CENTER, Align.MIN))
    body -= Pos(0, 0, p["z_ring"]) * Cylinder(p["r_in_bore"], p["z_tip_in"] - p["z_ring"] + 0.1, align=(Align.CENTER, Align.CENTER, Align.MIN))
    # wrench flats on the outlet tube (±X, across-flats flat_af)
    for sx in (-1, 1):
        body -= Pos(sx * (p["flat_af"] / 2 + 5), 0, (p["flat_z0"] + p["flat_z1"]) / 2) * Box(10, 20, p["flat_z1"] - p["flat_z0"])
    return body


def coil():
    p = P
    with BuildPart() as bp:
        with Locations((p["coil_cx"], p["coil_cy"], p["z_coil0"])):
            Cylinder(p["r_coil"], p["z_coil1"] - p["z_coil0"], align=(Align.CENTER, Align.CENTER, Align.MIN))
        fillet(bp.edges().group_by(Axis.Z)[0] + bp.edges().group_by(Axis.Z)[-1], p["coil_fillet"])
    return bp.part


def frame():
    p = P
    w = p["fx1"] - p["fx0"]
    h = p["fz1"] - p["fz0"]
    cx = (p["fx0"] + p["fx1"]) / 2
    cz = (p["fz0"] + p["fz1"]) / 2
    t = p["ft"]
    with BuildPart() as bp:
        with BuildSketch(Plane.XZ.offset(-p["fy"])):  # Plane.XZ normal is -Y; offset(-fy) sits at y=+fy
            with Locations((cx, cz)):
                RectangleRounded(w, h, p["fr_out"])
                RectangleRounded(w - 2 * t, h - 2 * t, p["fr_out"] - t, mode=Mode.SUBTRACT)
        extrude(amount=2 * p["fy"])
        # side-plate notches at the front edge (both sides)
        for sx in (-1, 1):
            x_mid = sx * (p["notch_x"] + 10)
            with Locations((x_mid, 0, (p["fz0"] - 1 + p["notch_z"]) / 2)):
                Box(20, 2 * p["notch_y"], p["notch_z"] - p["fz0"] + 1, mode=Mode.SUBTRACT)
        # front plate slot (+Y edge)
        sl = p["fy"] + 1 - p["slot_front_y0"]
        with BuildSketch(Plane.XY.offset(p["fz0"] - 0.5)):
            with Locations((0, p["slot_front_y0"] + p["slot_front_w"] / 2 + (sl - p["slot_front_w"] / 2) / 2)):
                SlotCenterToCenter(sl - p["slot_front_w"] / 2, p["slot_front_w"], rotation=90)
        extrude(amount=t + 1, mode=Mode.SUBTRACT)
        # rear plate slots (both Y edges)
        sl = p["fy"] + 1 - p["rear_slot_y0"]
        with BuildSketch(Plane.XY.offset(p["fz1"] - p["rear_slot_depth"])):
            yc = p["rear_slot_y0"] + p["rear_slot_w"] / 2 + (sl - p["rear_slot_w"] / 2) / 2
            with Locations((0, yc), (0, -yc)):
                SlotCenterToCenter(sl - p["rear_slot_w"] / 2, p["rear_slot_w"], rotation=90)
        extrude(amount=p["rear_slot_depth"] + 1, mode=Mode.SUBTRACT)
    return bp.part


def diamond_flange():
    """Lozenge flange (hull of Ø24.4 hub + two R3.9 lobes) with a recessed
    underside pocket: rim + screw bosses stay at dia_z1, pocket floor at pocket_z."""
    p = P
    with BuildPart() as bp:
        with BuildSketch(Plane.XY.offset(p["dia_z1"])):
            Circle(p["dia_r_center"])
            with Locations((p["dia_lobe_x"], 0), (-p["dia_lobe_x"], 0)):
                Circle(p["dia_lobe_r"])
            make_hull()
        extrude(amount=p["dia_z0"] - p["dia_z1"])
        with BuildSketch(Plane.XY.offset(p["dia_z1"] - 0.1)):
            Circle(p["dia_r_center"])
            with Locations((p["dia_lobe_x"], 0), (-p["dia_lobe_x"], 0)):
                Circle(p["dia_lobe_r"])
            make_hull()
            offset(amount=-p["pocket_rim"], kind=Kind.INTERSECTION, mode=Mode.REPLACE)
            Circle(p["r_body"], mode=Mode.SUBTRACT)
            with Locations(*p["screw_centers"]):
                Circle(p["boss_r"], mode=Mode.SUBTRACT)
        extrude(amount=p["pocket_z"] - p["dia_z1"] + 0.1, mode=Mode.SUBTRACT)
    return bp.part


def screws():
    """Two pan-head screws: domed head revolved from the measured (r, z) profile."""
    p = P
    prof = [(0, p["dia_z1"] + 0.3), (0, p["screw_z1"]), (2.0, p["screw_z1"] + 0.15), (2.8, -21.0),
            (3.25, -20.5), (3.65, -20.0), (p["screw_r"], -19.2), (p["screw_r"], p["dia_z1"] + 0.3)]
    with BuildPart() as bp:
        with BuildSketch(Plane.XZ):
            with BuildLine():
                Polyline(*prof, close=True)
            make_face()
        revolve(axis=Axis.Z)
    head = bp.part
    out = None
    for c in p["screw_centers"]:
        h = Pos(c[0], c[1], 0) * head
        ang = p["recess_ang"][p["screw_centers"].index(c)]
        for a in (ang, ang + 90):
            h -= Location((c[0], c[1], (p["screw_z1"] - 0.5 + p["recess_z"]) / 2), (0, 0, a)) * Box(
                p["recess_l"], p["recess_w"], p["recess_z"] - p["screw_z1"] + 0.5)
        out = h if out is None else out + h
    return out


def terminal_block():
    """Terminal block: YZ profile (sloped top, stepped floor) extruded across X,
    two 6.3-type spade tabs standing in front pockets, sloped rib, fuse housing."""
    p = P
    prof = [(p["tb_y0"], p["tb_z0"]), (p["tb_ystep"], p["tb_z0"]), (p["tb_ystep"], p["tb_z0b"]),
            (p["tb_y1"], p["tb_z0b"]), (p["tb_y1"], p["tb_z1b"]), (p["tb_y0"], p["tb_z1"])]
    with BuildPart() as bp:
        with BuildSketch(Plane.YZ.offset(p["tb_x0"])):
            with BuildLine():
                Polyline(*prof, close=True)
            make_face()
        extrude(amount=p["tb_x1"] - p["tb_x0"])
        ends = bp.faces().sort_by(Axis.X)
        fedges = [e for f in (ends[0], ends[-1]) for e in f.edges() if abs(e.tangent_at(0.5).Z) < 0.5 and (e.center().Z > -5 or e.center().Y < p["tb_ystep"])]
        fillet(fedges, p["tb_fillet"])
        # 0.48 mm lowered land at the front-left of the top face
        with Locations(((p["tb_x0"] - 1 + p["tb_step_x1"]) / 2, (p["tb_y0"] - 1 + p["tb_step_y1"]) / 2, p["tb_step_z"] + 1)):
            Box(p["tb_step_x1"] - p["tb_x0"] + 1, p["tb_step_y1"] - p["tb_y0"] + 1, 2, mode=Mode.SUBTRACT)
        # pockets in the front face under each tab
        for x0, x1 in (p["tabA"], p["tabB"]):
            with Locations(((x0 + x1) / 2, (p["tb_y0"] - 0.5 + p["tabpk_y1"]) / 2, (p["tabpk_z0"] + 0.5) / 2)):
                Box(x1 - x0 + 0.4, p["tabpk_y1"] - p["tb_y0"] + 0.5, 0.5 - p["tabpk_z0"], mode=Mode.SUBTRACT)
        # spade tabs
        for x0, x1 in (p["tabA"], p["tabB"]):
            with Locations(((x0 + x1) / 2, (p["tab_y0"] + p["tab_y1"]) / 2, (p["tabpk_z0"] - 0.1 + p["tab_z1"]) / 2)):
                Box(x1 - x0, p["tab_y1"] - p["tab_y0"], p["tab_z1"] - p["tabpk_z0"] + 0.1)
        # sloped rib (x = rib_x), profile in YZ
        with BuildSketch(Plane.YZ.offset(p["rib_x"][0])):
            with BuildLine():
                Polyline((-29.6, -4.5), (-29.6, -0.9), (-22.0, 12.6), (-19.0, 12.6), (-19.0, -4.5), close=True)
            make_face()
        extrude(amount=p["rib_x"][1] - p["rib_x"][0])
        # fuse/terminal housing (rotated box; closed top - pocket not resolved by scan)
        loc = Location((p["hs_cx"], p["hs_cy"], (-4.5 + p["hs_z1"]) / 2), (0, 0, p["hs_ang"]))
        with Locations(loc):
            Box(p["hs_l"], p["hs_w"], p["hs_z1"] + 4.5)
        fillet(bp.edges().filter_by(Axis.Z).filter_by_position(Axis.Z, (-4.5 + p["hs_z1"]) / 2 - 1, (-4.5 + p["hs_z1"]) / 2 + 1)
               .filter_by(lambda e: np.hypot(e.center().X - p["hs_cx"], e.center().Y - p["hs_cy"]) < 7), p["hs_fillet"])
    return bp.part


def build():
    body = revolve_body()
    body = body + coil()
    # solenoid core tube: plate-to-plate, hidden inside the coil; ties coil to frame
    body = body + Pos(0, 0, P["fz0"] + P["ft"] - 0.05) * Cylinder(
        P["r_core"], (P["fz1"] - P["ft"]) - (P["fz0"] + P["ft"]) + 0.1, align=(Align.CENTER, Align.CENTER, Align.MIN))
    body = body + frame()
    body = body + diamond_flange()
    body = body + screws()
    body = body + terminal_block()
    # U-windows through the flange + hub wall at both Y tips (cut last: the hub fills them otherwise)
    with BuildPart() as win:
        with BuildSketch(Plane.XY.offset(P["win_z0"])):
            for sy in (-1, 1):
                with Locations((0, sy * (P["win_y"] + P["win_w"] / 2 + 3))):
                    SlotCenterToCenter(6, P["win_w"], rotation=90)
        extrude(amount=P["win_z1"] - P["win_z0"])
    body = body - win.part
    return body


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "out")
    out.mkdir(parents=True, exist_ok=True)
    part = build()
    solids = part.solids()
    print("solids", len(solids), "valid", part.is_valid, "volume %.1f" % part.volume, "faces", len(part.faces()))
    bb = part.bounding_box()
    print("bbox", bb.min, bb.max)
    export_step(part, str(out / "pump_datum.step"))
    export_stl(part, str(out / "pump_datum.stl"), tolerance=0.01, angular_tolerance=0.1)
