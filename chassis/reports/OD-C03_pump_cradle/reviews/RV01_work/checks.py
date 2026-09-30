"""Reviewer's own gate computations (RV01). Same functions run on the delivered part and on every mutant."""
import math
import numpy as np
from pathlib import Path
from build123d import Edge, Vector, Compound
from tools.core import read_step, common_volume
from tools.core.validity import validity
from tools.core.shapes import faces, solids
from tools.result import Result, gate
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide,
                           overhang_census, clearance, radial_extent, radial_profile)
from tools.measure.features import kind
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.BRepLProp import BRepLProp_SLProps
from OCP.TopAbs import TopAbs_REVERSED

W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
MM, DEG, MM3 = 0.005, 0.001, 0.001          # GATES bands as carried by the plan (§2)
O, A, R = (0, 0, 0), (0, 0, 1), (1, 0, 0)

def load():
    part = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v01.step")
    pump = read_step(W/"00_Spec/inputs/OD-H01_ulka_ep5_pump.step")
    asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v01.step")
    sleeve = [c for c in asm.children if c.label == "od_h02_sleeve_assumed_A03"][0]
    return part, pump, sleeve

def face_normal(f):
    ad = BRepAdaptor_Surface(f)
    u = (ad.FirstUParameter()+ad.LastUParameter())/2; v = (ad.FirstVParameter()+ad.LastVParameter())/2
    n = BRepLProp_SLProps(ad, u, v, 1, 1e-7).Normal(); n = np.array([n.X(), n.Y(), n.Z()])
    return -n if f.Orientation() == TopAbs_REVERSED else n

def segments(shape, p0, d, L=200.0):
    """material stretches along a line through p0 in direction d (t measured from p0)."""
    p0 = np.array(p0, float); d = np.array(d, float)
    e = Edge.make_line(Vector(*(p0 - d*L)), Vector(*(p0 + d*L)))
    res = shape.intersect(e)
    out = []
    for ed in (res.edges() if res is not None else []):
        a = np.dot(np.array(ed.start_point().to_tuple()) - p0, d); b = np.dot(np.array(ed.end_point().to_tuple()) - p0, d)
        out.append((min(a, b), max(a, b)))
    return sorted(out)

def gap_around(shape, p0, d):
    """the empty stretch containing p0 along d: (lo, hi) relative to p0, None if p0 is in material."""
    segs = segments(shape, p0, d)
    lo, hi = -math.inf, math.inf
    for a, b in segs:
        if a <= 0 <= b: return None
        if b < 0: lo = max(lo, b)
        if a > 0: hi = min(hi, a)
    return lo, hi

def R_(name, val, unit, at=None, detail=None):
    if val is None or not math.isfinite(float(val)): return Result(name, None, unit, status="INCONCLUSIVE", reason="not measured")
    return Result(name, float(val), unit, at=at, detail=detail or {})

def run(part, pump, sleeve, *, walls=True, tag=""):
    G = {}
    v = validity(part)
    G["U-01 solid_count"] = gate("U-01", v["solid_count"], "==", 1, band=0)
    G["U-01 brep_valid"] = gate("U-01", v["brep_valid"], "==", 1, band=0)
    G["U-01 naked_edges"] = gate("U-01", v["naked_edges"], "==", 0, band=0)
    env = envelope(part)
    for k, s in (("size_x", 80.0), ("size_y", 40.0), ("size_z", 52.0)):
        G[f"U-02 {k}"] = gate("U-02", env[k], "in", (s-0.1, s+0.1), band=MM)
    G["D-02 size_x"] = gate("D-02", env["size_x"], "<=", 420, band=MM, assumes=["A-10"])
    G["D-02 size_z"] = gate("D-02", env["size_z"], "<=", 420, band=MM, assumes=["A-10"])
    G["D-02 size_y"] = gate("D-02", env["size_y"], "<=", 500, band=MM, assumes=["A-10"])
    G["REQ-08 max_y"] = gate("REQ-08", env["max_y"], "in", (39.9, 40.1), band=MM, assumes=["A-11"])
    # foot thickness: the foot top plane (normal -Y, largest such face) to max_y
    tops = [f for f in faces(part) if kind(f) == "plane" and np.allclose(face_normal(f), (0, -1, 0), atol=1e-6)]
    top = max(tops, key=lambda f: envelope(f)["size_x"].measured * envelope(f)["size_z"].measured)
    ty = envelope(top)["min_y"].measured
    G["REQ-08 thickness"] = gate("REQ-08", R_("foot_thickness", env["max_y"].measured - ty, "mm", at=(0, ty, 16)), "in", (2.9, 3.1), band=MM, assumes=["A-11"])
    # census
    fc = feature_census(part)
    G["U-05 plane"] = gate("U-05", fc["plane_faces"], "==", 48, band=0)
    G["U-05 cylinder"] = gate("U-05", fc["cylinder_faces"], "==", 6, band=0)
    G["U-05 concave"] = gate("U-05", fc["concave_cylinders"], "==", 6, band=0)
    G["U-05 bores"] = gate("U-05", fc["bores"], "==", 4, band=0)
    bc = bore_census(part)
    for x in (-34.0, 34.0):
        for z in (-4.0, 37.0):
            lb = locate_bore(bc, (x, 38.5, z), (0, 1, 0))
            G[f"REQ-07 d {x},{z}"] = gate("REQ-07", lb["diameter"], "in", (3.3, 3.5), band=MM, assumes=["A-11"])
            G[f"REQ-07 off {x},{z}"] = gate("REQ-07", lb["offset"], "<=", 0.10, band=MM, assumes=["A-11"])
            G[f"REQ-07 thr {x},{z}"] = gate("REQ-07", lb["through"], "==", 1, band=0, assumes=["A-11"])
            G[f"D-04a {x},{z}"] = gate("D-04a", lb["diameter"], ">=", 3.25, band=MM)
    # saddle arcs / rib / post / slot counts by position
    cyl = [f for f in faces(part) if kind(f) == "cylinder"]
    arcs = [f for f in cyl if abs(envelope(f)["max_y"].measured - 26.65) < 0.2]
    G["U-05 saddle arcs"] = gate("U-05", R_("saddle_arcs", len(arcs), "count"), "==", 2, band=0)
    posts = [f for f in faces(part) if kind(f) == "plane" and abs(abs(envelope(f)["min_x"].measured) - 29.5) < 0.6
             and envelope(f)["size_x"].measured < 1e-6 and envelope(f)["size_y"].measured > 30]
    G["U-05 post blocks"] = gate("U-05", R_("post_inner_faces", len(posts), "count"), "==", 2, band=0)
    for f in posts:
        e = envelope(f); sx = "+" if e["min_x"].measured > 0 else "-"
        G[f"REQ-06 x {sx}"] = gate("REQ-06", R_("post_inner_x", abs(e["min_x"].measured), "mm", at=(e["min_x"].measured, 18.5, 23)), "in", (29.4, 29.6), band=MM, assumes=["A-06"])
        G[f"REQ-06 z0 {sx}"] = gate("REQ-06", e["min_z"], "in", (12.9, 13.1), band=MM, assumes=["A-06"])
        G[f"REQ-06 z1 {sx}"] = gate("REQ-06", e["max_z"], "in", (32.9, 33.1), band=MM, assumes=["A-06"])
    foot_under = [f for f in faces(part) if kind(f) == "plane" and np.allclose(face_normal(f), (0, 1, 0), atol=1e-6) and abs(envelope(f)["min_y"].measured - 40) < 0.2]
    G["U-05 foot"] = gate("U-05", R_("foot_underside", len(foot_under), "count"), "==", 1, band=0)
    # slots by line probes through each post at x = +-31.5
    nslots = 0
    for sx in (-31.5, 31.5):
        for zc in (18.0, 28.0):
            g = gap_around(part, (sx, 7.0, zc), (1, 0, 0))            # through along X
            thr = g is not None and g[0] < -2.0 - 1e-6 and g[1] > 2.0 + 1e-6
            if thr: nslots += 1
            zg = [gap_around(part, (sx, y, zc), (0, 0, 1)) for y in (5.76, 7.0, 8.24)]
            z7 = gap_around(part, (sx, 7.0, zc), (0, 0, 1))
            yg = [None] if z7 is None or not all(map(math.isfinite, z7)) else \
                 [gap_around(part, (sx, 7.0, z), (0, 1, 0)) for z in (zc + z7[0] + 1e-4, zc + z7[1] - 1e-4)]
            yc = gap_around(part, (sx, 7.0, zc), (0, 1, 0))
            if None in zg or None in yg or yc is None:
                for k in ("clear_z", "clear_y", "yc", "zc", "lig"):
                    G[f"REQ-05 {k} {sx},{zc}"] = gate("REQ-05", R_("x", None, "mm"), ">=", 0, band=MM)
                continue
            cz = min(b - a for a, b in zg); cy = min(b - a for a, b in yg)
            floor = 7.0 + yc[1]; ycent = floor - cy/2
            zmid = zc + (zg[1][0] + zg[1][1])/2
            G[f"REQ-05 clear_z {sx},{zc}"] = gate("REQ-05", R_("slot_clear_z", cz, "mm", at=(sx, 7.0, zc)), ">=", 6.0, band=MM, assumes=["A-07"])
            G[f"REQ-05 clear_y {sx},{zc}"] = gate("REQ-05", R_("slot_clear_y", cy, "mm", at=(sx, 7.0, zc)), ">=", 2.5, band=MM, assumes=["A-07"])
            G[f"REQ-05 yc {sx},{zc}"] = gate("REQ-05", R_("slot_centre_y", ycent, "mm", at=(sx, ycent, zc)), "in", (6.5, 7.5), band=MM, assumes=["A-07"])
            G[f"REQ-05 zc {sx},{zc}"] = gate("REQ-05", R_("slot_centre_z", zmid, "mm", at=(sx, 7.0, zmid)), "in", (zc-0.5, zc+0.5), band=MM, assumes=["A-07"])
            G[f"REQ-05 through {sx},{zc}"] = gate("REQ-05", R_("slot_through", int(thr), "bool"), "==", 1, band=0, assumes=["A-07"])
            # ligaments along Z beside the slot at y 7 and above the apex along Y
            segsz = segments(part, (sx, 7.0, zc), (0, 0, 1))
            near = [(a, b) for a, b in segsz if b <= zg[1][0] + 1e-6 and b > zg[1][0] - 20 or a >= zg[1][1] - 1e-6 and a < zg[1][1] + 20]
            lig = min(b - a for a, b in near) if near else None
            segsy = segments(part, (sx, 7.0, zc), (0, 1, 0)); above = [(a, b) for a, b in segsy if b <= yc[0] + 1e-6]
            lig_top = min(b - a for a, b in above) if above else None
            G[f"REQ-05 lig {sx},{zc}"] = gate("REQ-05", R_("slot_ligament_z", lig, "mm"), ">=", 2.0, band=MM, assumes=["A-07"])
            G[f"REQ-05 ligtop {sx},{zc}"] = gate("REQ-05", R_("slot_ligament_top", lig_top, "mm"), ">=", 2.0, band=MM, assumes=["A-07"])
    G["U-05 slots"] = gate("U-05", R_("through_slots", nslots, "count"), "==", 4, band=0)
    ribs = [f for f in faces(part) if kind(f) == "plane" and abs(abs(face_normal(f)[2]) - 1) < 1e-6 and 40 < envelope(f)["size_x"].measured < 50 and envelope(f)["min_y"].measured > 18]
    G["U-05 ribs"] = gate("U-05", R_("rib_side_faces/2", len(ribs)/2, "count"), "==", 2, band=0)
    zs = sorted(envelope(f)["min_z"].measured for f in ribs)
    for i, want in enumerate((15.0, 21.0, 25.0, 31.0)):
        val = zs[i] if i < len(zs) else None
        G[f"REQ-02 face {want}"] = gate("REQ-02", R_("rib_face_z", val, "mm", at=(0, 30, val)), "in", (want-0.1, want+0.1), band=MM, assumes=["A-06"])
    # REQ-01 / REQ-02 radial
    for band_ in ((15.5, 20.5), (25.5, 30.5)):
        rp = radial_profile(part, O, A, R, list(range(50, 131, 5)), band_, margin=0, z_step=0.1, side="inner")
        G[f"REQ-01 min {band_}"] = gate("REQ-01", rp["min"], "in", (26.60, 26.70), band=MM, assumes=["A-03"])
        G[f"REQ-01 max {band_}"] = gate("REQ-01", rp["max"], "in", (26.60, 26.70), band=MM, assumes=["A-03"])
    for z in (18.0, 28.0):
        for a in (50.0, 130.0):
            G[f"REQ-02 in {a},{z}"] = gate("REQ-02", radial_extent(part, O, A, R, a, z, side="inner"), "<=", 26.70, band=MM, assumes=["A-06"])
        for a in (40.0, 140.0):
            w = radial_extent(part, O, A, R, a, z, side="inner", r_max=32.0)
            whole = radial_extent(part, O, A, R, a, z, side="inner")
            nomat = (w.status == "INCONCLUSIVE" and w.reason.startswith("NoMaterial") and whole.ok and whole.measured > 32.0)
            # the spec's expected reading: no material in r <= 32; gated on the first material of the whole ray
            # spec: the r <= 32 window must read INCONCLUSIVE "no material"; recorded, and gated on the whole ray's first material
            ok = w.status == "INCONCLUSIVE" and w.reason.startswith("NoMaterial")
            G[f"REQ-02 window {a},{z}"] = gate("REQ-02", R_("window_no_material", int(ok), "bool", detail={"reason": w.reason, "measured": w.measured}), "==", 1, band=0, assumes=["A-06"])
            G[f"REQ-02 nomat {a},{z}"] = gate("REQ-02", whole, ">=", 32.0, band=MM, assumes=["A-06"])
    # assembly
    c = clearance(part, pump)
    G["REQ-03"] = gate("REQ-03", c, ">=", 2.0, band=MM, assumes=["A-01", "A-03"])
    G["D-04c"] = gate("D-04c", c, ">=", 0.5, band=MM, assumes=["A-01"])
    G["U-03 pump clr"] = gate("U-03", c, ">=", 2.0, band=MM, assumes=["A-01", "A-03"])
    ip = common_volume(part, pump)
    G["U-03 pump interf"] = gate("U-03", ip, "<=", 0, band=MM3, assumes=["A-01", "A-03"])
    cs = clearance(part, sleeve)
    G["REQ-04 clr"] = gate("REQ-04", cs, "==", 0, band=MM, assumes=["A-03"])
    G["U-03 sleeve clr"] = gate("U-03", cs, "==", 0, band=MM, assumes=["A-01", "A-03"])
    isl = common_volume(part, sleeve)
    G["REQ-04 interf"] = gate("REQ-04", isl, "<=", 0, band=MM3, assumes=["A-03"])
    G["U-03 sleeve interf"] = gate("U-03", isl, "<=", 0, band=MM3, assumes=["A-01", "A-03"])
    # nearest point on a saddle arc: r 26.65 +-0.05 and theta within 45..135 at a rib z
    if cs.ok and cs.at:
        x, y, z = cs.at; r = math.hypot(x, y); th = math.degrees(math.atan2(y, x))
        on = int(abs(r - 26.65) <= 0.05 + MM and 45 - DEG <= th <= 135 + DEG and (15 - MM <= z <= 21 + MM or 25 - MM <= z <= 31 + MM))
        G["REQ-04 on arc"] = gate("REQ-04", R_("nearest_on_saddle_arc", on, "bool", at=cs.at), "==", 1, band=0, assumes=["A-03"])
    # REQ-06 post clearance (inside REQ-03): per post block
    from build123d import Box, Pos
    for sx, xc in (("-", -29.0), ("+", 29.0)):
        blk = Pos(xc, 17.95, 23) * Box(10.0, 37.9, 22.0)     # |x| 24..34, y -1..36.9, z 12..34: the post block only
        cut = part.intersect(blk)
        G[f"REQ-06 clr {sx}"] = gate("REQ-06", clearance(Compound(list(cut.solids())), pump) if cut is not None else R_("clearance", None, "mm"), ">=", 2.0, band=MM, assumes=["A-06"])
    # rib contact per rib: each saddle touches the sleeve
    for zc in (18.0, 28.0):
        cut = part.intersect(Pos(0, 30, zc) * Box(50, 30, 6.2))
        G[f"REQ-04 rib {zc}"] = gate("REQ-04", clearance(Compound(list(cut.solids())), sleeve) if cut is not None else R_("clearance", None, "mm"), "==", 0, band=MM, assumes=["A-03"])
    # print
    oh = overhang_census(part, build_dir=(0, -1, 0), min_deg=45)
    G["D-03a"] = gate("D-03a", oh, ">=", 45.0, band=DEG, assumes=["A-13"])
    G["REQ-05 roof"] = gate("REQ-05", oh, ">=", 45.0, band=DEG, assumes=["A-07", "A-13"])
    # D-03b: downward horizontal planes off the bed (normal +Y, y < 39.99): their shorter span
    spans = []
    for f in faces(part):
        if kind(f) == "plane" and np.allclose(face_normal(f), (0, 1, 0), atol=1e-3):
            e = envelope(f)
            if e["max_y"].measured < 40.0 - 0.01:
                spans.append(max(e["size_x"].measured, e["size_z"].measured))   # conservative: the longer side
    G["D-03b"] = gate("D-03b", R_("largest_bridge_span", max(spans) if spans else 0.0, "mm"), "<=", 5.0, band=MM)
    if walls:
        mw = min_wall(part)
        G["D-01a"] = gate("D-01a", mw, ">=", 0.8, band=MM)
        G["D-01b"] = gate("D-01b", mw, ">=", 2.0, band=MM)
        G["D-06a"] = gate("D-06a", mw, ">=", 1.0, band=MM)
        G["U-06"] = gate("U-06", min_wall_wide(part), ">=", 2.0, band=MM)
    return G
