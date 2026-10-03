"""Positive controls: one mutant of this part per check family; each check must FAIL on it."""
from common import *
import struct, sys
from tools.core import validity, compare_step, write_stl, common_volume
from tools.measure import (envelope, feature_census, bore_census, locate_bore, clearance, radial_profile, radial_extent,
                           overhang_census, flat_ceiling_spans, mesh_census, mesh_deviation, min_wall)
from tools.result import gate
which = sys.argv[1] if len(sys.argv) > 1 else "fast"
s, ss = part(); P = Solid(ss[0])
out = {}
def G(gid, res, op, lim, band):
    g = gate(gid, res, op, lim, band=band); return {"status": g.status, "measured": res.measured, "res_status": res.status}
if which == "fast":
    r = refs()
    # 1 validity
    m = Compound([P, box(200, 210, 0, 10, 0, 10)])
    out["validity"] = G("U-01", validity(m)["solid_count"], "==", 1, 0)
    # 2 envelope: a 0.5 nub behind the left flange
    m = P + box(-100, -98, 0, 2, 71.5, 72.0)
    e = envelope(m); out["envelope_minz"] = G("REQ-07", e["min_z"], ">=", 72.0, 0.005); out["envelope_sizez"] = G("U-02", e["size_z"], "in", (24.9, 25.1), 0.005)
    # 3 compare_step: delivered file against a mutant with a button hole filled
    m = P + cyl_z(-98.9908, 139.9014, 7.5, 94.0, 97.0)
    cs = compare_step(m, PART_STEP); out["compare_step_volume"] = G("U-04", cs["volume_delta"], "<=", 0.0, 0.001); out["compare_step_faces"] = G("U-04", cs["faces_delta"], "==", 0, 0)
    # 4 census: hole removed -> 8 bores; flange hole relocated 0.5 in x
    fc = feature_census(m); out["census_bores_removed"] = G("U-05", fc["bores"], "==", 9, 0)
    m2 = (P + cyl_y(-85, 77, 1.7, 0, 4)) - cyl_y(-84.5, 77, 1.7, -1, 5)
    lb = locate_bore(bore_census(m2), (-85, 2, 77), (0, 1, 0)); out["locate_bore_relocated"] = G("REQ-01", lb["offset"], "<=", 0.10, 0.005)
    m3 = (P + cyl_y(-85, 77, 1.7, 0, 4)) - cyl_y(-85, 77, 1.6, -1, 5)
    lb = locate_bore(bore_census(m3), (-85, 2, 77), (0, 1, 0)); out["bore_diameter_resized"] = G("D-04a", lb["diameter"], ">=", 3.25, 0.005)
    # 5 clearance: panel raised 0.5 (contact), boss enlarged (E-01), window right edge moved 3 left (REQ-05 a)
    out["clearance_contact"] = G("U-03", clearance(translate(P, (0, 0.5, 0)), r["C01"]), "<=", 0.0, 0.005)
    m = P + cyl_z(-91.0555, 153.2349, 6.2, 86.0, 94.0)
    out["clearance_E01_boss"] = G("E-01", clearance(m & cyl_z(-91.0555, 153.2349, 7.0, 85.985, 93.99), r["E02"]), ">=", 0.5, 0.005)
    m = P + box(72.0, 75.0, 50, 188, 94, 97)
    out["clearance_REQ05a"] = G("REQ-05", clearance(rot_about_axis(r["G10"], 10.0), m), ">=", 2.0, 0.005)
    # 6 the clearance fallback for unsound OD-G10: window top lowered to y 170 over x 0..30 (carry pose axis z 182)
    m = P + box(0, 30, 170, 188, 94, 97)
    Gp = translate(rot_about_axis(r["G10"], -50), (0, -15, 150))
    c = clearance(Gp, m); out["fallback_REQ05b"] = {"clearance": c.measured, "inside": c.detail["inside"], "status": "FAIL" if (c.measured <= 0 or c.detail["inside"]) else "PASS"}
    c = clearance(Gp, P); out["fallback_REQ05b_base"] = {"clearance": c.measured, "inside": c.detail["inside"]}
    # 7 interference: R2 thickened 0.5 into the tray slot
    m = P + box(74.5, 75.0, 0, 49, 84, 94)
    out["interference_tray"] = G("REQ-07", common_volume(m, box(-74.8, 74.8, 0, 49.8, -15, 120)), "<=", 0.0, 0.001)
    # 8 radial_profile: insert bore enlarged to 5.2
    m = P - cyl_z(-91.0555, 153.2349, 2.6, 85.0, 91.485)
    pr = radial_profile(m, (-91.0555, 153.2349, 85.485), (0, 0, 1), (1, 0, 0), [2.0 * i for i in range(180)], (0.0, 6.0), margin=(0.0, 0.0), z_step=0.25, side="outer", r_min=2.6, r_max=7.0)
    out["radial_J05"] = {"min_minus_bore": pr["min"].measured - 2.6, "status": "FAIL" if pr["min"].measured - 2.6 < 3.0 - 0.005 else "PASS"}
    # radial_extent on a wall pocket (REQ-02)
    m = P - box(-5, 5, 195, 205, 93, 96.5)
    re_ = radial_extent(m, (0, 200, 0), (1, 0, 0), (0, 0, 1), 0.0, 0.0, side="inner", r_min=85, r_max=120)
    out["radial_REQ02"] = G("REQ-02", re_, "in", (93.9, 94.1), 0.005)
    # 9 overhang and bridge: a ledge off R2
    m = P + box(78, 86, 100, 110, 84, 86)
    oc = overhang_census(m, build_dir=(0, 0, -1)); out["overhang_ledge"] = G("D-03a", oc, ">=", 45.0, 0.001)
    fc2 = flat_ceiling_spans(m, build_dir=(0, 0, -1), max_span=5.0); out["bridge_ledge"] = G("D-03b", fc2, "<=", 5.0, 0.005)
    # 10 mesh: one triangle dropped; delivered STL against the part moved 0.1
    raw = PART_STL.read_bytes(); n = struct.unpack("<I", raw[80:84])[0]
    bad = raw[:80] + struct.pack("<I", n - 1) + raw[84 + 50:]
    (WORK / "mutant_drop1.stl").write_bytes(bad)
    mc = mesh_census(WORK / "mutant_drop1.stl"); out["mesh_census_drop1"] = G("U-07", mc["naked_edges"], "==", 0, 0)
    out["mesh_deviation_moved"] = G("U-07", mesh_deviation(PART_STL, translate(P, (0.1, 0, 0))), "<=", 0.01, 0.005)
    w = write_stl(P, WORK / "mutant_coarse.stl", tolerance=0.1, angular_tolerance=0.5)
    out["sagitta_coarse"] = G("U-07", w.checks["max_sagitta"], "<=", 0.01, 0.005)
    # U-04 roundtrip on a parent-free copy of the solid (fresh write into the work folder)
    dump("s08_controls_fast.json", out)
    from tools.core import step_roundtrip
    Q = Solid(ss[0]); Q.label = "od_c09_front"
    rt = step_roundtrip(Q, WORK / "rt_od_c09_front.step", timestamp="2026-10-03T00:00:00")
    out["roundtrip_work"] = {k: (v.measured, v.status) for k, v in rt.items()}
    dump("s08_controls_fast.json", out)
else:
    m = P - box(-5, 5, 195, 205, 94.0, 96.5)       # top bar thinned to 0.5
    mw = min_wall(m, spacing=0.45); out["min_wall_thin"] = G("D-01a", mw, ">=", 0.8, 0.005)
    dump("s08_controls_minwall.json", out)
print(json.dumps(out, indent=1, default=str))
