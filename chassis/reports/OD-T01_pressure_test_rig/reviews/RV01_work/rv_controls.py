"""RV01 positive controls: mutants of the exported rig STEP; each check family must FAIL on its mutant."""
import json, sys, math, struct
from pathlib import Path
import numpy as np
from build123d import Solid, Compound, Location, Cylinder, Box, Pos
from tools.core import read_step, solids, validity, write_stl, mesh_sagitta, compare_step, write_step, common_volume
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide,
                           overhang_census, flat_ceiling_spans, clearance, mesh_census)
from tools.result import gate
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN, TopAbs_OUT
J = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig"); W = J / "reviews/RV01_work"; M = W / "mutants"; M.mkdir(exist_ok=True)
which = sys.argv[1].split(",") if len(sys.argv) > 1 else ["all"]
def want(k): return "all" in which or k in which
rig = Solid(solids(read_step(J / "02_STEP_STL/od_t01_rig_C1_v01.step"))[0])
BAND = 0.005
def yc(r, h, x, y0, z):   # cylinder along +Y from y0, length h
    return Cylinder(r, h, align=None).moved(Location((x, y0, z)) * Location((0, 0, 0), (1, 0, 0), -90))
def box(x0, x1, y0, y1, z0, z1):
    return Box(x1 - x0, y1 - y0, z1 - z0, align=None).moved(Location((x0, y0, z0)))
def one(s):
    ss = solids(s); assert len(ss) == 1, len(ss); return Solid(ss[0])
out = {}
def rec(k, g, mutant):
    out[k] = {"mutant": mutant, "status": g.status, "measured": g.measured, "required": g.required, "margin": g.margin}
    print(k, g.status, g.measured, g.required, flush=True)
asm = read_step(J / "00_Spec/inputs/od_g01_assembly_C1_v03.step"); A = [Solid(s) for s in solids(asm)]
POSE = Location((0, 110.06, 0)) * Location((0, 0, 0), (1, 0, 0), 90)
def posed(s, phi=0.0, dy=0.0, dz=0.0):
    return s.moved(Location((0, dy, dz)) * Location((0, 0, 0), (0, 1, 0), phi) * POSE)
H, G10 = A[0], A[2]   # identified by measurement in rv_asm.py (housing 0, OD-G10 2)
if want("validity"):
    two = Compound([rig, rig.moved(Location((300, 0, 0)))])
    rec("validity_solid_count", gate("U-01", validity(two)["solid_count"], "==", 1, band=0), "rig plus a relocated copy (2 solids)")
    from OCP.BRepBuilderAPI import BRepBuilderAPI_Sewing
    sew = BRepBuilderAPI_Sewing(1e-6)
    for f in rig.faces()[1:]: sew.Add(f.wrapped)
    sew.Perform()
    rec("validity_naked_edges", gate("U-01", validity(sew.SewedShape())["naked_edges"], "==", 0, band=0), "rig with one face removed (open shell)")
if want("envelope"):
    m = one(rig.fuse(box(119, 121, 0, 10, -10, 10)))
    rec("envelope_size_x", gate("U-02", envelope(m)["size_x"], "in", (239.9, 240.1), band=BAND), "base resized +1.0 at +X")
if want("census"):
    m = rig
    m = one(m.fuse(yc(1.8, 3.0, 44, 135, 44)))         # remove hole (44,44)
    fc = feature_census(m)
    rec("feature_census_bores", gate("U-05", fc["bores"], "==", 13, band=0), "Ø3.4 hole at (44,44) removed")
    rec("feature_census_cyl", gate("U-05", fc["cylinder_faces"], "==", 13, band=0), "Ø3.4 hole at (44,44) removed")
    m2 = one(m.cut(yc(1.7, 3.0, 44.5, 135, 44)))      # relocated 0.5 in X
    lb = locate_bore(bore_census(m2), (44.0, 136.5, 44.0), (0, 1, 0))
    rec("locate_bore_offset", gate("REQ-01", lb["offset"], "<=", 0.10, band=BAND), "Ø3.4 hole at (44,44) relocated +0.5 in X")
    m3 = one(m.cut(yc(1.6, 3.0, 44.0, 135, 44)))      # resized Ø3.2
    lb3 = locate_bore(bore_census(m3), (44.0, 136.5, 44.0), (0, 1, 0))
    rec("bore_diameter", gate("D-04a", lb3["diameter"], ">=", 3.25, band=BAND), "Ø3.4 hole at (44,44) resized to Ø3.2")
if want("wall"):
    m = one(rig.cut(yc(3.25, 2.5, -44, 135.6, -44)))   # counterbore floor 138 -> 135.6
    mw = min_wall(m)
    rec("min_wall_D01b", gate("D-01b", mw, ">=", 2.0, band=BAND), "counterbore (-44,-44) deepened: 0.6 of plate under the head")
    rec("min_wall_D01a", gate("D-01a", mw, ">=", 0.8, band=BAND), "same")
    mww = min_wall_wide(m)
    rec("min_wall_wide_U06", gate("U-06", mww, ">=", 2.0, band=BAND), "same")
    lb = locate_bore(bore_census(m), (-44.0, 144.0, -44.0), (0, 1, 0))
    out["cbore_mutant_start"] = lb["diameter"].detail.get("start")
    write_step(m, M / "mut_cbore_deep.step", timestamp="2026-10-03T00:00:00") if False else None
if want("overhang"):
    plugs = [yc(1.8, 3.0, sx * 44.0, 135.0, sz * 44.0) for sx in (1, -1) for sz in (1, -1)]
    m = rig.cut(box(55, 65, 134, 151, 0, 5))            # flat-roofed slot through the plate, x 55..65, z 0..5
    for p in plugs: m = m.fuse(p)
    m = one(m)
    if "fcs_only" not in which: rec("overhang_census", gate("D-03a", overhang_census(m, build_dir=(0, 0, 1), min_deg=45), ">=", 45.0, band=0.001), "crown-filled census copy with a 10-wide flat-roofed slot through the plate at x 55..65, z 0..5")
    fcs = flat_ceiling_spans(m, build_dir=(0, 0, 1), max_span=5.0); print("fcs", fcs.status, fcs.reason, fcs.measured)
    rec("flat_ceiling_spans", gate("D-03b", fcs, "<=", 5.0, band=BAND), "same slot (10 wide ceiling)")
if want("clearance"):
    m = rig if "pb" in which else one(rig.fuse(box(62, 75, 80, 100, 25, 40)))     # block on the +X wall's inner front
    worst = None
    for phi in (() if "pb" in which else range(-60, 16, 5)):
        c = clearance(m, posed(G10, phi=phi))
        if worst is None or c.measured < worst.measured: worst = c
    if worst is not None: rec("clearance_REQ04a", gate("REQ-04", worst, ">=", 5.0, band=BAND), "block x 62..75, y 80..100, z 25..40 on the +X wall's inner front")
    # pair-B distance: window face relocated 0.5 toward the pair-B axis (rig moved +0.5 in X and -0.5 in Z: axis (10.64,-15.78))
    from build123d import Edge
    mv = rig.moved(Location((-0.35, 0, 0.35)))
    seg = Edge.make_line((10.641441, 135.0, -15.776585), (10.641441, 150.0, -15.776585))
    rec("clearance_pairB", gate("REQ-03", clearance(seg, mv), ">=", 10.87, band=BAND), "rig relocated (-0.35, 0, +0.35): window face 0.49 nearer the pair-B axis")
if want("interference"):
    up = posed(H, dy=0.5)
    rec("interference_U03", gate("U-03", common_volume(rig, up), "<=", 0.0, band=0.001), "housing relocated 0.5 up into the plate")
    m = one(rig.fuse(box(40, 48, 150, 160, 40, 48)))
    rec("interference_REQ07", gate("REQ-07", common_volume(m, yc(3.0, 150.0, 44, 150, 44)), "<=", 0.0, band=0.001), "a boss added above the plate on the (44,44) screw axis")
    rec("clearance_contact", gate("U-03", clearance(rig, posed(H, dy=-0.2)), "==", 0.0, band=BAND), "housing relocated 0.2 down (gap at the seat)")
if want("roundtrip"):
    m = one(rig.cut(yc(3.25, 2.5, -44, 135.6, -44))); m.label = "od_t01_rig"
    write_step(m, M / "mut_cbore_deep.step", timestamp="2026-10-03T00:00:00")
    cs = compare_step(rig, M / "mut_cbore_deep.step")
    rec("compare_step_volume", gate("U-04", cs["volume_delta"], "<=", 0.0, band=0.001), "delivered shape compared with a re-export whose counterbore is deepened")
    rec("compare_step_faces", gate("U-04", cs["faces_delta"], "==", 0, band=0), "same")
if want("mesh"):
    w = write_stl(rig, M / "coarse.stl", tolerance=0.1, angular_tolerance=0.5)
    rec("mesh_sagitta", gate("U-07", w.checks["max_sagitta"], "<=", 0.01, band=BAND), "rig re-meshed at chordal 0.1, angular 0.5")
    data = (J / "02_STEP_STL/od_t01_rig_C1_v01.stl").read_bytes()
    n = struct.unpack("<I", data[80:84])[0]
    cut = data[:80] + struct.pack("<I", n - 1) + data[84:84 + 50 * (n - 1)]
    (M / "holed.stl").write_bytes(cut)
    rec("mesh_census_naked", gate("U-07", mesh_census(M / "holed.stl")["naked_edges"], "==", 0, band=0), "delivered STL with its last triangle removed")
if want("plane"):
    # REQ-02 grid and REQ-03 flank/apex script on mutants
    m = one(rig.cut(box(45, 49, 134, 135.5, -20, -10)))
    cl = BRepClass3d_SolidClassifier(m.wrapped); bad = 0
    for x in np.linspace(-50, 50, 101):
        for z in np.linspace(-50, 50, 101):
            if math.hypot(x, z) < 30.001 or (z > 0 and abs(x) <= 42.5 - z + 1e-3) or any(math.hypot(x - sx * 44, z - sz * 44) < 1.701 for sx in (1, -1) for sz in (1, -1)): continue
            cl.Perform(gp_Pnt(x, 135.002, z), 1e-6)
            if cl.State() != TopAbs_IN: bad += 1
    out["REQ02_grid_mutant"] = {"mutant": "0.5-deep pocket x 45..49, z -20..-10 in the underside", "not_material_above": bad, "status": "FAIL" if bad else "PASS"}
    print("REQ02 grid mutant", bad)
    # apex: relocated rig +0.5 in Z, flanks measured by the same plane method
    mv = rig.moved(Location((0, 0, 0.5)))
    from OCP.BRepAdaptor import BRepAdaptor_Surface
    from OCP.GeomAbs import GeomAbs_Plane
    fl = []
    for f in mv.faces():
        if BRepAdaptor_Surface(f.wrapped).GetType() != GeomAbs_Plane: continue
        n = f.normal_at(f.center()); c = f.center()
        if abs(n.Y) < 1e-6 and abs(n.X) > 1e-3 and abs(n.Z) > 1e-3 and c.Y > 134.9 and abs(c.X) < 40: fl.append(((n.X, n.Z), (c.X, c.Z)))
    A_ = np.array([[fl[0][0][0], fl[0][0][1]], [fl[1][0][0], fl[1][0][1]]]); b_ = np.array([np.dot(fl[0][0], fl[0][1]), np.dot(fl[1][0], fl[1][1])])
    ax, az = np.linalg.solve(A_, b_)
    from tools.result import Result
    rec("apex_plane_method", gate("REQ-03", Result("window_apex_z", float(az), "mm"), "in", (42.36, 42.66), band=BAND), "rig relocated +0.5 in Z")
(W / f"controls_{'_'.join(which)}.json").write_text(json.dumps(out, indent=1, default=str))
