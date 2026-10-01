"""RV01 positive controls: mutants of this job's exported part, built by me from the STEP, each run through the
check family it controls and compared with the spec §5 limit via tools.result.gate. A control must FAIL."""
import json, sys, math
import numpy as np, trimesh
from build123d import Box, Cylinder, Location, Pos, Rot, Compound
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
from tools.core import read_step, write_step, validity, common_volume, compare_step, write_stl, mesh_sagitta
from tools.measure import (envelope, feature_census, bore_census, locate_bore, radial_extent, min_wall, min_wall_wide,
                           overhang_census, flat_ceiling_spans, clearance, mesh_census, mesh_deviation)
from tools.result import gate, Result
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"; M = f"{W}/mutants"
I = f"{J}/00_Spec/inputs"
STEP = f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"
WHICH = sys.argv[1].split(",") if len(sys.argv) > 1 else None
p = read_step(STEP)
res = {}
try: res = json.load(open(f"{W}/m8_controls.json"))
except Exception: pass
def rec(family, mutant, g):
    res[family] = {"mutant": mutant, "gate": g.gate, "measured": g.measured, "required": g.required, "status": g.status,
                   "got": "FAIL" if g.status == "FAIL" else ("INCONCLUSIVE" if g.status == "INCONCLUSIVE" else "PASS"),
                   "reason": getattr(g, "reason", "")}
    print(family, res[family], flush=True); json.dump(res, open(f"{W}/m8_controls.json", "w"), indent=1, default=str)
def save(shape, name):
    path = f"{M}/{name}.step"; write_step(shape, path, timestamp="2026-10-01T00:00:00"); return read_step(path)
def want(k): return WHICH is None or k in WHICH
yrot = Rot(90, 0, 0)
if want("validity"):   # a second, loose solid beside the panel
    m = Compound([p, Box(5, 5, 5).moved(Location((0, 100, -320)))])
    v = validity(m); rec("validity (solid_count)", "a loose 5 mm cube 18 mm in front of the outer face", gate("U-01", v["solid_count"], "==", 1, band=0))
if want("envelope"):   # wall end extended 0.5 mm in +X
    m = save(p.fuse(Box(0.5, 215, 3).moved(Location((116.25, 107.5, -300.5)))).clean(), "env_x116p5")
    e = envelope(m); rec("envelope", "wall's +X end extended 0.5 mm (x 116 -> 116.5)", gate("U-02", e["size_x"], "in", (231.9, 232.1), band=0.005))
if want("census"):     # vent slot at x 110 filled
    m = save(p.fuse(Box(4, 80, 3).moved(Location((110, 140, -300.5)))).clean(), "census_vent110_filled")
    c = feature_census(m); rec("feature_census", "vent slot at x 110 filled (removed)", gate("U-05", c["cylinder_faces"], "==", 19, band=0))
if want("bore"):       # flange hole at (-81,-282) removed
    m = save(p.fuse(Pos(-81, 2, -282) * yrot * Cylinder(1.7, 4)).clean(), "bore_flange_m81_filled")
    b = bore_census(m); rec("bore_census", "flange hole at (-81, -282) filled (removed)", gate("U-05", b, "==", 9, band=0))
if want("locate"):     # flange hole at (81,-282) moved 0.5 mm to x 81.5
    m = p.fuse(Pos(81, 2, -282) * yrot * Cylinder(1.7, 4)).clean().cut(Pos(81.5, 2, -282) * yrot * Cylinder(1.7, 6))
    m = save(m, "locate_flange81_dx0p5")
    l = locate_bore(bore_census(m), (81, 2.0, -282), (0, 1, 0)); rec("locate_bore", "flange hole (81, -282) moved 0.5 mm along +X", gate("REQ-01", l["offset"], "<=", 0.10, band=0.005, assumes=["A-01"]))
if want("radial"):     # +X boss side cut back 1.0 mm (x 96 -> 95): bore wall 4.0 -> 3.0... make it 2.5
    m = save(p.cut(Box(1.5, 8, 12).moved(Location((95.25, 207, -293)))).clean(), "radial_boss90_thinned")
    r = radial_extent(m, (90, 209, -293), (0, 1, 0), (1, 0, 0), 0, 1.0, side="outer", r_min=1.0, r_max=12)
    r2 = Result("j05_wall", r.measured - 2.0, "mm", at=r.at) if r.ok else r
    rec("radial_extent", "+X side of the boss at x 90 cut back 1.5 mm (bore wall 4.0 -> 2.5)", gate("J-05", r2, ">=", 3.0, band=0.005))
if want("wall"):       # 20 x 20 pocket 1.5 deep from the outer face at (0, 60): wall 3.0 -> 1.5, and a ceiling
    m = save(p.cut(Box(20, 20, 1.5).moved(Location((0, 60, -301.25)))).clean(), "wall_pocket_1p5")
    w = min_wall(m, spacing=0.7); rec("min_wall", "20 x 20 pocket 1.5 deep cut into the outer face at (0, 60): wall 1.5", gate("D-01b", w, ">=", 2.0, band=0.005))
    ww = min_wall_wide(m, spacing=0.7); rec("min_wall_wide", "same pocket mutant", gate("U-06", ww, ">=", 2.0, band=0.005))
if want("overhang"):   # pocket mutant with the six exception holes refilled: the pocket's ceiling faces -Z off the bed
    m = read_step(f"{M}/wall_pocket_1p5.step")
    for (x, z, d, y0, y1) in [(81, -282, 3.4, 0, 4), (95, -282, 3.4, 0, 4), (-81, -282, 3.4, 0, 4), (-95, -282, 3.4, 0, 4),
                              (90, -293, 4.0, 209, 215), (-90, -293, 4.0, 209, 215)]:
        m = m.fuse(Pos(x, (y0 + y1) / 2, z) * yrot * Cylinder(d / 2, y1 - y0)).clean()
    o = overhang_census(m, build_dir=(0, 0, 1), spacing=0.7)
    rec("overhang_census", "pocket mutant (20 x 20 flat ceiling at z -300.5), exception holes refilled", gate("D-03a", o, ">=", 45.0, band=0.001, assumes=["A-08"]))
if want("bridge"):
    m = read_step(f"{M}/wall_pocket_1p5.step")
    f = flat_ceiling_spans(m, build_dir=(0, 0, 1), max_span=5.0, spacing=0.7)
    rec("flat_ceiling_spans", "pocket mutant (20 x 20 flat ceiling at z -300.5)", gate("D-03b", f, "<=", 5.0, band=0.005, assumes=["A-08"]))
if want("common"):     # 5 mm cube in the tank zone in front of the wall
    m = save(p.fuse(Box(5, 5, 5).moved(Location((0, 50, -296.5)))).clean(), "common_tankzone_cube")
    box = Box(140, 100, 48.8).moved(Location((0, 50, (-298.8 - 250) / 2)))
    rec("common_volume (interference)", "5 mm cube fused to the wall's inner face at (0, 50) in the tank zone", gate("REQ-05", common_volume(box, m), "<=", 0.0, band=0.001, assumes=["A-07"]))
if want("lowering"):   # a tab into the bulkhead's path: x 60..70, y 100..105, z -299..-235
    m = save(p.fuse(Box(10, 5, 64).moved(Location((65, 102.5, -267)))).clean(), "lowering_tab_into_c02")
    bulk = read_step(f"{I}/OD-C02_bulkhead.step"); worst = 0.0
    for i in range(0, 41, 2):
        cv = common_volume(m.moved(Location((0, 40.0 - i, 0))), bulk); worst = max(worst, cv.measured or 0)
    rec("common_volume (lowering path)", "tab x 60..70, y 100..105 reaching z -235 into OD-C02's space", gate("U-03", Result("lowering_worst", worst, "mm3"), "<=", 0.0, band=0.001, assumes=["A-01", "A-02", "A-07"]))
if want("driver"):     # a 2 mm rib over the screw axis at (95, -282), y 150..152
    m = save(p.fuse(Box(6, 2, 10).moved(Location((95, 151, -284)))).clean(), "driver_rib_over_95")
    cyl = Pos(95, 132, -282) * yrot * Cylinder(3.0, 256.0)
    rec("common_volume (driver)", "rib 6 x 2 x 10 at y 151 over the screw axis (95, -282)", gate("REQ-08", common_volume(cyl, m), "<=", 0.0, band=0.001))
if want("clearance"):  # panel moved 18 mm forward: OD-C02 clearance 37 -> 19
    cradle_loc = Location((0, 0, 18.0))
    bulk = read_step(f"{I}/OD-C02_bulkhead.step")
    rec("clearance", "whole panel moved 18 mm toward the front (+Z)", gate("U-03", clearance(p.moved(cradle_loc), bulk), ">=", 20.0, band=0.005, assumes=["A-01", "A-02", "A-07"]))
if want("footprint"):  # flange extended 3 mm outward (x 104 -> 107): rim of the feet hole at 110 gets 1.3
    from build123d import Plane, Edge, Face
    m = save(p.fuse(Box(3, 4, 22).moved(Location((105.5, 2, -288)))).clean(), "footprint_flange_107")
    foot = [f for f in m.faces() if f.geom_type.name == "PLANE" and abs(f.bounding_box().min.Y) < 1e-6 and abs(f.bounding_box().max.Y) < 1e-6][0]
    flbox = Box(400, 10, 200).moved(Location((0, 0, -299 + 100)))
    cc = BRepAlgoAPI_Common(foot.wrapped, flbox.wrapped); cc.Build()
    from OCP.BRepExtrema import BRepExtrema_DistShapeShape
    rim = Edge.make_circle(1.7, Plane(origin=(110, 0, -295), z_dir=(0, 1, 0)))
    d = BRepExtrema_DistShapeShape(rim.wrapped, cc.Shape()); d.Perform()
    rec("footprint rim distance (job code)", "flange's +X end extended 3 mm (x 104 -> 107) toward the feet hole (110, -295)", gate("U-03", Result("rim_to_flange", d.Value(), "mm"), ">=", 3.0, band=0.005, assumes=["A-01", "A-02", "A-07"]))
if want("roundtrip"):  # the envelope mutant compared with the delivered STEP file
    m = read_step(f"{M}/env_x116p5.step")
    c = compare_step(m, STEP); rec("compare_step (round trip)", "the +0.5 mm envelope mutant compared with the delivered STEP", gate("U-04", c["volume_delta"], "in", (0.0, 0.0), band=0.001))
if want("mesh"):
    mm = trimesh.load(f"{J}/02_STEP_STL/od_c11_back_C1_v03.stl", process=False)
    bad = trimesh.Trimesh(vertices=mm.vertices, faces=mm.faces[2:], process=False); bad.export(f"{M}/stl_two_triangles_removed.stl")
    mc = mesh_census(f"{M}/stl_two_triangles_removed.stl")
    rec("mesh_census", "delivered STL with two triangles removed", gate("U-07", mc["naked_edges"], "==", 0, band=0))
    w = write_stl(p, f"{M}/stl_coarse_0p1.stl", tolerance=0.1, angular_tolerance=0.5)
    rec("mesh_sagitta", "re-mesh at tolerance 0.1 mm, 0.5 rad", gate("U-07", w.checks["max_sagitta"], "<=", 0.01, band=0.0))
if want("sections"):   # E-06 by section regions: boss detached from the wall by a 0.5 mm gap
    from build123d import Plane, Rectangle
    m = save(p.cut(Box(12, 8, 0.5).moved(Location((90, 207, -298.75)))).cut(Box(12, 0.5, 12).moved(Location((90, 210.75, -293)))).clean(), "sections_boss90_detached")
    # the boss at x 90 tied in: the section at x 92 (off the bore) holds the boss block (y 203..211) in one region with the wall
    face = Plane(origin=(93, 0, 0), z_dir=(1, 0, 0)) * Rectangle(1000, 1000)
    cc = BRepAlgoAPI_Common(m.wrapped, face.wrapped); cc.Build(); regs = Compound(cc.Shape()).faces()
    tied = [f for f in regs if f.bounding_box().min.Y <= 203.0 + 1e-6 and f.bounding_box().max.Y >= 205 and f.bounding_box().min.Z <= -301.9 and f.bounding_box().max.Z >= -287.1 and f.bounding_box().min.Y < 150]
    rec("section regions (E-06 tie)", "boss at x 90 cut free of the wall (0.5 gap at z -299) and of the ledge (0.5 gap at y 211)", gate("E-06", Result("boss_tied", int(len(tied) == 1), "bool"), "==", 1, band=0))
