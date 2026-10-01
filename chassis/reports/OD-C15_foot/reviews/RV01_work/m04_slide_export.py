"""RV01 measurement 4: U-03(b) slide (nut z x nut s x pocket af jointly), designer assembly vs own placement, U-04, U-07, REQ-07."""
import json, math, hashlib
from pathlib import Path
from build123d import Cylinder, Polygon, extrude, Location, Align
from tools.core import read_step, validity, step_roundtrip, write_stl
from tools.core.boolean import common_volume
from tools.core.step import labels, read_schema
from tools.core.shapes import solids, faces, volume_mm3
from tools.measure import envelope, clearance, interference, mesh_census, mesh_deviation, min_wall_mesh
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL

W = Path("/home/claude/oguz-env/jobs/20261001-od-c15-feet"); R = W / "reviews/RV01_work"
foot = read_step(W / "02_STEP_STL/od_c15_foot_C1_v01.step")
out = {}
def rx(res): return {"m": None if res.measured is None else round(res.measured, 6), "at": res.at, "st": res.status, "why": res.reason}
def hexagon(s):
    e2 = s / math.sqrt(3)
    return Polygon(*[(e2 * math.cos(math.radians(60 * k)), e2 * math.sin(math.radians(60 * k))) for k in range(6)], align=None)
def nut(s=5.5, top=2.5):
    body = extrude(hexagon(s), 2.4)
    body = body - Cylinder(1.5, 3, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -0.3)))
    return body.moved(Location((0, 0, top)))
def screw():
    head = Cylinder(2.85, 1.65, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -7.65)))
    shank = Cylinder(1.5, 12.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -6.0)))
    return head + shank

# pocket af 5.65 variant of the exported part (tolerance corner): enlarge flats z 2.5..9.5 by a 5.65 hex prism
foot565 = foot - extrude(hexagon(5.65), 7.0).moved(Location((0, 0, 2.5)))
out["foot565_valid"] = {k: v.measured for k, v in validity(foot565).items()}
# U-03(b): nut top face from z 10.5 (outside) through 10.0 (mouth) to 2.5 (seat) in 0.25 steps
tops = [10.5 - 0.25 * k for k in range(0, 33)]
slide = {}
worst = 0.0
for af_name, fshape in (("af5.60", foot), ("af5.65", foot565)):
    for s in (5.32, 5.50):
        vals = []
        for t in tops:
            v = common_volume(fshape, nut(s, t))
            vals.append((round(t, 3), None if v.measured is None else round(v.measured, 9), v.status))
            if v.measured is None: worst = None
            elif worst is not None: worst = max(worst, v.measured)
        seat_c = clearance(nut(s, 2.5), fshape - Cylinder(5, 2.5, align=(Align.CENTER, Align.CENTER, Align.MIN)))  # flats only (lid removed)
        slide[f"{af_name}_s{s}"] = {"n_poses": len(vals), "max_mm3": max(x[1] for x in vals), "inconclusive": sum(1 for x in vals if x[2] != "MEASURED"),
                                    "per_side_at_seat": rx(seat_c)}
out["U03b_slide"] = slide; out["U03b_worst_mm3"] = worst
# REQ-03 nut envelope to each flat: clearance nut (s5.5 at seat) to foot material above the seat
ring = foot - Cylinder(10, 2.5, align=(Align.CENTER, Align.CENTER, Align.MIN))
out["REQ03_nut_to_flats_nominal"] = rx(clearance(nut(5.5, 2.5), ring))
out["REQ03_nut_s5.32_to_flats"] = rx(clearance(nut(5.32, 2.5), ring))

# REQ-07: screw envelope in the foot frame
se = envelope(screw()); out["REQ07_screw_env_foot"] = {k: round(v.measured, 6) for k, v in se.items()}

# designer assembly vs own placement
asm = read_step(W / "02_STEP_STL/od_c15_assembly_C1_v01.step")
names = labels(asm); out["asm_labels"] = names
def leaves(s):
    ch = list(getattr(s, "children", ()) or ())
    return [x for c in ch for x in leaves(c)] if ch else [s]
parts = {l.label: l for l in leaves(asm)}
plate = read_step(W / "00_Spec/inputs/OD-C01_base_frame.step")
cmp = {}
P = ((110, 90), (-110, 90), (110, -295), (-110, -295))
for nm, p in parts.items():
    d = {"solids": len(solids(p)), "vol": round(volume_mm3(p), 4), "env": {k: round(v.measured, 4) for k, v in envelope(p).items() if k.startswith("min") or k.startswith("max")}}
    cmp[nm] = d
# match each designer foot to my placed foot by volume of symmetric difference
mine = {}
for i, (X, Zh) in enumerate(P, 1):
    loc = Location((X, -6.0, Zh), (90, 0, 0))
    mine[i] = (foot.moved(loc), nut().moved(loc), screw().moved(loc))
for nm, p in parts.items():
    if nm == "plate":
        cmp[nm]["sym_diff_vs_input"] = round(volume_mm3(p) + volume_mm3(plate) - 2 * common_volume(p, plate).measured, 6); continue
    kindn = nm.split("_")[0]; idx = {"foot": 0, "nut": 1, "screw": 2}[kindn]
    best = None
    for i in mine:
        m = mine[i][idx]; cv = common_volume(p, m).measured
        sd = volume_mm3(p) + volume_mm3(m) - 2 * cv
        if best is None or sd < best[0]: best = (sd, i)
    cmp[nm]["sym_diff_vs_mine"] = round(best[0], 6); cmp[nm]["matches_pose"] = best[1]
out["designer_assembly"] = cmp

# U-04: delivered file facts + own round trip
shells = 0; e = TopExp_Explorer(foot.wrapped, TopAbs_SHELL)
while e.More(): shells += 1; e.Next()
out["U04_file"] = {"schema": read_schema(W / "02_STEP_STL/od_c15_foot_C1_v01.step"), "labels": labels(foot), "solids": len(solids(foot)), "shells": shells}
rt = step_roundtrip(foot, R / "rt_foot.step", timestamp="2026-10-01T00:00:00")
out["U04_roundtrip"] = {k: rx(v) for k, v in rt.items()}

# U-07: STL
stl = W / "02_STEP_STL/od_c15_foot_C1_v01.stl"
mc = mesh_census(stl); out["U07_mesh_census"] = {k: rx(v) for k, v in mc.items()}
out["U07_mesh_deviation"] = rx(mesh_deviation(stl, foot))
out["U07_angular_limit"] = 4 * math.acos(1 - 0.01 / 9.0)
wr = write_stl(read_step(W / "02_STEP_STL/od_c15_foot_C1_v01.step"), R / "own_remesh_0.01_0.18.stl", tolerance=0.01, angular_tolerance=0.18)
out["U07_own_remesh"] = {"sha256": wr.sha256, "triangles": wr.detail["triangles"], "sagitta": rx(wr.checks["max_sagitta"]),
                         "delivered_sha256": hashlib.sha256(stl.read_bytes()).hexdigest()}
out["U07_min_wall_mesh"] = rx(min_wall_mesh(stl))
json.dump(out, open(R / "m04_slide_export.json", "w"), indent=1, default=str)
for k, v in out.items(): print(k, json.dumps(v, default=str)[:1500])
