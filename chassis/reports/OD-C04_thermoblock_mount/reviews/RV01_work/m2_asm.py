"""RV01 reviewer measurements: U-04 round trip, the check assembly, REQ-07, the STL."""
import json, math
from pathlib import Path
import numpy as np
from build123d import Solid, Cylinder, Pos, Align, Compound
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN, TopAbs_ON, TopAbs_OUT
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL, TopAbs_SOLID, TopAbs_FACE
from tools.core import read_step, validity, step_roundtrip, write_stl, common_volume, mesh_sagitta
from tools.core.step import labels, file_sha256
from tools.core.shapes import solids, volume_mm3
from tools.measure import (envelope, clearance, interference, bore_census, radial_profile, mesh_census,
                           mesh_deviation, min_wall_mesh)

W = Path("/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount")
OUT = W / "reviews/RV01_work"
R = lambda r: r.to_dict()
out = {}
def count(shape, kind):
    e = TopExp_Explorer(shape.wrapped, kind); n = 0
    while e.More(): n += 1; e.Next()
    return n

mount_file = read_step(W / "02_STEP_STL/od_c04_mount_C1_v01.step")
out["mount_tree"] = {"type": type(mount_file).__name__, "children": [getattr(c, "label", "") for c in getattr(mount_file, "children", [])],
                     "shells": count(mount_file, TopAbs_SHELL), "solids": count(mount_file, TopAbs_SOLID), "faces": count(mount_file, TopAbs_FACE)}
msol = Solid(solids(mount_file)[0]); msol.label = "od_c04_mount"
out["mount_solid_shells"] = count(msol, TopAbs_SHELL); out["mount_solid_faces"] = count(msol, TopAbs_FACE)
out["roundtrip"] = {k: R(r) for k, r in step_roundtrip(msol, OUT / "rt_mount.step", timestamp="2026-09-30T00:00:00").items()}

asm = read_step(W / "02_STEP_STL/od_c04_assembly_C1_v01.step")
out["asm_labels"] = labels(asm)
parts = {}
def walk(s):
    ch = list(getattr(s, "children", ()) or ())
    if ch:
        for c in ch: walk(c)
    else:
        parts[s.label] = s
walk(asm)
out["asm_parts"] = {}
for n, s in parts.items():
    out["asm_parts"][n] = {"solids": len(solids(s)), "volume": volume_mm3(s),
                           "envelope": {k: r.measured for k, r in envelope(s).items()},
                           "validity": {k: (r.measured, r.status, r.reason) for k, r in validity(s).items()}}
M, H = parts["od_c04_mount"], parts["OD-H11_thermoblock"]
S1, S2 = parts["spacer_S1_assumed_A05"], parts["spacer_S2_assumed_A05"]
Hin = read_step(W / "00_Spec/inputs/OD-H11_thermoblock.step")
out["H_input"] = {"volume": volume_mm3(Hin), "envelope": {k: r.measured for k, r in envelope(Hin).items()}}
# assembly mount identical to the part file?
out["mount_vs_asm_common"] = R(common_volume(msol, M))
out["mount_vs_asm_vol"] = [volume_mm3(msol), volume_mm3(M)]
for n, s in (("S1", S1), ("S2", S2)):
    out[f"{n}_bores"] = bore_census(s).detail["bores"]
# clearances
C = {}
C["mount|H_asm"] = R(clearance(M, H))
C["mount_file|H_input"] = R(clearance(msol, Hin))
C["S1|mount"] = R(clearance(S1, M)); C["S2|mount"] = R(clearance(S2, M))
C["S1|H"] = R(clearance(S1, H)); C["S2|H"] = R(clearance(S2, H))
C["S1|S2"] = R(clearance(S1, S2))
out["clearance"] = C
out["interference"] = {k: R(r) for k, r in interference({"mount": M, "OD-H11": H, "S1": S1, "S2": S2}).items()}
# spacer seat: fraction of the S1 / S2 top annulus (r 2.0..3.5) with casting material within 0.05 above it
Hs = solids(H)[0]
def seat(cx, cy, z, dz=0.05):
    cl = BRepClass3d_SolidClassifier(Hs); n = inside = 0; pts = []
    for r in np.linspace(2.05, 3.45, 8):
        for a in np.arange(0, 360, 5):
            x, y = cx + r*math.cos(math.radians(a)), cy + r*math.sin(math.radians(a))
            cl.Perform(gp_Pnt(x, y, z + dz), 1e-6); st = cl.State(); n += 1
            if st == TopAbs_IN: inside += 1; pts.append(a)
            cl.Perform(gp_Pnt(x, y, z - dz), 1e-6)
            if cl.State() == TopAbs_IN: out.setdefault("seat_violations", []).append((x, y, z - dz))
    return {"samples": n, "bearing_fraction": inside / n, "angles_with_bearing": sorted(set(pts))}
out["seat_S1"] = seat(-19.62, 20.18, 0.0)
out["seat_S2"] = seat(25.01, 9.08, 27.6)
# classify points along the spacer bodies inside the casting (distance-free overlap probe, since the boolean is refused)
def probe_body(cx, cy, z0, z1):
    cl = BRepClass3d_SolidClassifier(Hs); hits = 0; n = 0
    for z in np.linspace(z0 + 0.02, z1 - 0.02, 60):
        for r in (2.0, 2.75, 3.5):
            for a in range(0, 360, 10):
                cl.Perform(gp_Pnt(cx + r*math.cos(math.radians(a)), cy + r*math.sin(math.radians(a)), z), 1e-6); n += 1
                if cl.State() == TopAbs_IN: hits += 1
    return {"samples": n, "inside_casting": hits}
out["S1_body_probe"] = probe_body(-19.62, 20.18, -10.1, 0.0)
out["S2_body_probe"] = probe_body(25.01, 9.08, -10.1, 27.6)
# REQ-07 keep-out cylinder r 45.0 about (-8.330, -14.130), z 0 .. 47.64
ax = (-8.330, -14.130)
keep = Pos(ax[0], ax[1], 0) * Cylinder(45.0, 47.64, align=(Align.CENTER, Align.CENTER, Align.MIN))
out["REQ07_common"] = R(common_volume(M, keep))
out["REQ07_clearance"] = R(clearance(M, keep))
keep0 = Cylinder(45.0, 47.64, align=(Align.CENTER, Align.CENTER, Align.MIN))
out["REQ07_origin_common"] = R(common_volume(M, keep0))
rp = radial_profile(M, (ax[0], ax[1], 0), (0, 0, 1), (1, 0, 0), list(range(0, 360, 10)), (0.0, 47.64),
                    margin=(0, 0), z_step=2.0, side="inner", r_min=0, r_max=45.0)
out["REQ07_radial"] = {k: {"measured": r.measured, "status": r.status, "reason": r.reason[:300],
                           "unread": len(r.detail.get("unread", []) or [])} for k, r in rp.items()}
# STL
stl = W / "02_STEP_STL/od_c04_mount_C1_v01.stl"
out["stl_sha"] = file_sha256(stl)
out["stl_census"] = {k: (r.measured, r.status) for k, r in mesh_census(stl).items()}
out["stl_deviation"] = R(mesh_deviation(stl, msol))
mine = write_stl(msol, OUT / "rv_remesh.stl", tolerance=0.01, angular_tolerance=4*math.acos(1-0.01/6.0))
out["my_stl"] = {"sha": mine.sha256, "detail": mine.detail, "sagitta": R(mine.checks["max_sagitta"])}
out["stl_minwall"] = R(min_wall_mesh(stl))
import trimesh
tm = trimesh.load(stl); out["stl_bounds"] = tm.bounds.tolist(); out["stl_volume"] = float(tm.volume); out["stl_triangles"] = len(tm.faces)
(OUT / "m2_asm.json").write_text(json.dumps(out, indent=1, default=str))
print("done")
