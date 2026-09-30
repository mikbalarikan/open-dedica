"""RV01 B: U-04 round trip, U-07 mesh and 3MF, on the delivered files."""
import json, math, zipfile, re, struct
from pathlib import Path
import numpy as np
from build123d import Location
from tools.core import read_step, step_roundtrip, compare_step, write_stl, mesh_sagitta, validity, volume_mm3
from tools.core.step import labels, file_sha256
from tools.measure.wall import mesh_census, mesh_deviation
J = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
W = J / "reviews/RV01_work"
out = {}
TS = "2026-09-30T00:00:00"
plate = read_step(J / "02_STEP_STL/od_c01_frame_C1_v02.step")
rt = step_roundtrip(plate, W / "rt_plate.step", timestamp=TS)
out["rt_plate"] = {k: [v.measured, v.status, v.reason, v.detail.get("built") if k in ("labels","faces_delta") else None] for k, v in rt.items()}
out["plate_labels"] = labels(plate)
asm = read_step(J / "02_STEP_STL/od_c01_assembly_C1_v02.step")
out["asm_labels"] = labels(asm)
rta = step_roundtrip(asm, W / "rt_asm.step", timestamp=TS)
out["rt_asm"] = {k: [v.measured, v.status, v.reason] for k, v in rta.items()}
print("RTA", out["rt_asm"])
back = read_step(W / "rt_asm.step") if (W / "rt_asm.step").exists() else read_step(J / "02_STEP_STL/od_c01_assembly_C1_v02.step")
out["rt_asm_note"] = "rewritten" if (W / "rt_asm.step").exists() else "rewrite refused; per-part rows compare delivered with itself"
per = {}
bk = {c.label: c for c in back.children}
for c in asm.children:
    b = bk.get(c.label)
    per[c.label] = {"vol_delivered": volume_mm3(c), "vol_rewritten": volume_mm3(b) if b else None,
                    "faces": [len(c.faces()), len(b.faces()) if b else None]}
out["rt_asm_per_part"] = per
# OD-H11: the input as placed vs the assembly's copy (first generation)
h11 = read_step(J / "00_Spec/inputs/OD-H11_thermoblock.step").moved(Location((0, 70, -140)))
a11 = [c for c in asm.children if c.label == "od_h11_thermoblock"][0]
out["h11_input_vol"] = volume_mm3(h11); out["h11_asm_vol"] = volume_mm3(a11)
out["h11_input_faces"] = len(h11.faces()); out["h11_asm_faces"] = len(a11.faces())
# vertex comparison
vi = sorted([tuple(round(c, 5) for c in v.to_tuple()) for v in h11.vertices()])
va = sorted([tuple(round(c, 5) for c in v.to_tuple()) for v in a11.vertices()])
out["h11_vertex_sets_equal_1e-5"] = vi == va
out["h11_nvert"] = [len(vi), len(va)]
# my own write of the unplaced input OD-H11 alone: does the reader/writer alone move its volume?
h11raw = read_step(J / "00_Spec/inputs/OD-H11_thermoblock.step")
rth = step_roundtrip(h11raw, W / "rt_h11_input.step", timestamp=TS)
out["rt_h11_input_by_reviewer"] = {k: [v.measured, v.status, v.reason[:120]] for k, v in rth.items()}
# mesh: delivered STL
stl = J / "02_STEP_STL/od_c01_frame_C1_v02.stl"
mc = mesh_census(stl); out["stl_census"] = {k: [v.measured, v.status] for k, v in mc.items()}
raw = stl.read_bytes(); out["stl_header"] = raw[:80].decode("latin1").strip("\x00 ")
ntri = struct.unpack("<I", raw[80:84])[0]; out["stl_ntri_header"] = ntri
tri = np.frombuffer(raw[84:84 + 50 * ntri], dtype=np.dtype([("n", "<f4", 3), ("v", "<f4", (3, 3)), ("a", "<u2")]))
V = tri["v"].reshape(-1, 3)
out["stl_bbox"] = [V.min(0).tolist(), V.max(0).tolist()]
# reproduce the D5 export with the REPORT's settings
w = write_stl(plate, W / "reexport.stl", tolerance=0.01, angular_tolerance=0.20)
out["reexport"] = {"sha": w.sha256, "same_bytes_as_delivered": w.sha256 == file_sha256(stl), "detail": w.detail,
                   "sagitta": [w.checks["max_sagitta"].measured, w.checks["max_sagitta"].status]}
ms = mesh_sagitta(plate); out["mesh_sagitta_after"] = [ms.measured, ms.status, ms.detail.get("triangles")]
out["ang_limit"] = 4 * math.acos(1 - 0.01 / 6.0)
md = mesh_deviation(stl, plate); out["mesh_deviation_delivered"] = [md.measured, md.status, md.reason, str(md.at)]
# 3MF
z = zipfile.ZipFile(J / "02_STEP_STL/od_c01_frame_C1_v02.3mf")
out["3mf_names"] = z.namelist()
model = [n for n in z.namelist() if n.endswith(".model")][0]
xml = z.read(model).decode()
verts = np.array([[float(a), float(b), float(c)] for a, b, c in re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', xml)])
tris = np.array([[int(a), int(b), int(c)] for a, b, c in re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', xml)])
out["3mf_unit"] = re.findall(r'unit="([^"]+)"', xml)
out["3mf_counts"] = [len(verts), len(tris)]
out["3mf_bbox"] = [verts.min(0).tolist(), verts.max(0).tolist()]
out["3mf_transform"] = re.findall(r'transform="([^"]+)"', xml)
p = verts[tris]
vol = float(np.einsum("ij,ij->i", p[:, 0], np.cross(p[:, 1], p[:, 2])).sum() / 6)
out["3mf_volume"] = vol
# same mesh as STL: every 3MF triangle's vertex set matches an STL triangle (float32 rounding)
key = lambda T: tuple(sorted(tuple(np.round(q, 3)) for q in T))
stl_set = {key(t) for t in tri["v"].astype(float)}
m3_set = {key(t) for t in p}
out["3mf_vs_stl"] = {"stl_unique": len(stl_set), "3mf_unique": len(m3_set), "common": len(stl_set & m3_set)}
(W / "rv_b.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps(out, indent=0, default=str)[:6000])
