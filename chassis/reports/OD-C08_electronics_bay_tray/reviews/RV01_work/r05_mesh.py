"""U-04 (STEP re-read), U-07 (STL + 3MF): delivered STL against the B-rep, a fresh D5 re-mesh, the 3MF against the STL."""
import sys, math, zipfile, re; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
import numpy as np, trimesh
from tools.core import read_step, validity, compare_step, write_stl
from tools.core.step import labels, node_labels, read_schema, read_length_unit
from tools.measure import mesh_census, mesh_deviation, min_wall_mesh
from tools.measure.wall import load_mesh
from tools.result import Result
t = read_step(PART)
# U-04: re-read the delivered part: schema, unit, label, solids, validity; STEP free of stray shells/faces
txt = PART.read_text(errors="replace")
print("schema", read_schema(PART), "unit", read_length_unit(PART), "labels", node_labels(t))
n_solid = txt.count("MANIFOLD_SOLID_BREP("); n_shell = txt.count("CLOSED_SHELL("); n_open = txt.count("OPEN_SHELL("); n_shm = txt.count("SHELL_BASED_SURFACE_MODEL(")
print("entities: MANIFOLD_SOLID_BREP", n_solid, "CLOSED_SHELL", n_shell, "OPEN_SHELL", n_open, "SHELL_BASED_SURFACE_MODEL", n_shm)
g("U-04", Result("schema_ap242", int(read_schema(PART) == "AP242"), "bool"), "==", 1, note="schema AP242")
g("U-04", Result("label", int(node_labels(t) == ["od_c08_tray"]), "bool", at=str(node_labels(t))), "==", 1, note="named body od_c08_tray")
g("U-04", Result("stray", n_open + n_shm + (n_shell - n_solid), "count"), "==", 0, note=f"stray shells: OPEN_SHELL {n_open}, SBSM {n_shm}, extra CLOSED_SHELL {n_shell - n_solid}")
v = validity(t); g("U-04", v["brep_valid"], "==", 1, note="valid after re-import")
# roundtrip: write the re-imported part with write_step to the work folder, compare (re-export stability)
from tools.core import step_roundtrip
from build123d import Solid
t_free = Solid(t.wrapped); t_free.label = "od_c08_tray"
rt = step_roundtrip(t_free, W / "roundtrip_part.step", timestamp="2026-10-01T00:00:00")
for k, r in rt.items(): print("roundtrip", k, r.measured, r.status, r.reason)
g("U-04", rt["volume_delta"], "<=", 0.0, note="re-write/re-read volume delta")
g("U-04", rt["faces_delta"], "==", 0, note="re-write/re-read faces delta")
g("U-04", rt["labels"], "==", 1, note="re-write/re-read labels")
# assembly file: 4 named parts, each one valid solid (checked in r03); tray in assembly = part (r03 common volume)
a = read_step(ASM); print("asm labels", node_labels(a))
g("U-04", Result("asm_parts", len(a.children), "count", at=str(node_labels(a))), "==", 4, note="assembly STEP: 4 named parts")

# U-07 STL
mc = mesh_census(STL)
for k, r in mc.items(): print("stl", k, r.measured)
g("U-07", mc["bodies"], "==", 1, note="STL bodies"); g("U-07", mc["naked_edges"], "==", 0, note="STL naked edges")
g("U-07", mc["winding"], "==", 1, note="STL winding")
g("U-07", Result("stl_volume_vs_brep", abs(mc["volume"].measured - t.volume), "mm3", at=f"STL {mc['volume'].measured:.3f} vs B-rep {t.volume:.3f}"), "<=", 2.0, note="info: chordal volume loss")
md = mesh_deviation(STL, t); print("mesh_deviation", md.measured, md.at, md.detail)
g("U-07", md, "<=", 0.01, note="delivered STL to B-rep, both ways (achieved chordal tolerance)")
# angular limit 4*acos(1-0.01/Rmax), Rmax 5.0
amax = 4 * math.acos(1 - 0.01 / 5.0); print("angular limit", amax)
# fresh D5 re-mesh at 0.01 / 0.2 and compare with the delivered STL (same triangulation?)
wr = write_stl(t, W / "remesh_0.01_0.2.stl", tolerance=0.01, angular_tolerance=0.2)
print("remesh", wr.detail, wr.checks["max_sagitta"].measured)
g("U-07", wr.checks["max_sagitta"], "<=", 0.01, note="stl_max_sagitta of a fresh 0.01/0.2 rad mesh of the delivered STEP")
g("U-07", Result("angular_tol", 0.2, "rad", at="REPORT record; corroborated by identical re-mesh"), "<=", amax, note=f"angular 0.2 <= 4acos(1-0.01/5) = {amax:.4f}")
m_del = trimesh.load(STL, process=False); m_new = trimesh.load(W / "remesh_0.01_0.2.stl", process=False)
from scipy.spatial import cKDTree
def tri_match(a, b):
    """largest vertex distance between each triangle of a and its nearest-centroid triangle of b, and orientation agreement"""
    ca, cb = a.triangles_center, b.triangles_center
    d, idx = cKDTree(cb).query(ca)
    worst = 0.0; flips = 0
    for i, j in enumerate(idx):
        ta, tb = a.triangles[i], b.triangles[j]
        dd = min(max(np.linalg.norm(ta - np.roll(tb, k, axis=0), axis=1)) for k in range(3))
        worst = max(worst, dd); flips += int(np.dot(a.face_normals[i], b.face_normals[j]) < 0)
    return worst, flips, len(set(idx.tolist()))
w1, f1, u1 = tri_match(m_del, m_new); w2, f2, u2 = tri_match(m_new, m_del)
print("delivered vs fresh: worst vertex", w1, w2, "flips", f1, f2, "unique matches", u1, u2, len(m_del.faces), len(m_new.faces))
pa = np.vstack([m_del.vertices, m_del.triangles_center]); pb = np.vstack([m_new.vertices, m_new.triangles_center])
sd = max(trimesh.proximity.closest_point(m_new, pa)[1].max(), trimesh.proximity.closest_point(m_del, pb)[1].max())
print("surface distance delivered<->fresh", sd, "area", m_del.area, m_new.area)
g("U-07", Result("stl_vs_D5_remesh", float(sd), "mm", at=f"{len(m_del.faces)} vs {len(m_new.faces)} triangles; planar-face diagonals differ, surfaces coincide"), "<=", 1e-4, note="delivered STL coincides with a cleared-triangulation re-mesh at 0.01/0.2 rad")
# 3MF vs STL
z = zipfile.ZipFile(TMF); xml = z.read("3D/3dmodel.model").decode()
vx = np.array([[float(a), float(b), float(c)] for a, b, c in re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', xml)])
tr = np.array([[int(a), int(b), int(c)] for a, b, c in re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', xml)])
m3 = trimesh.Trimesh(vx, tr, process=False)
unit = re.search(r'unit="(\w+)"', xml).group(1)
print("3mf unit", unit, "objects", xml.count("<object "), "items", xml.count("<item "), "tris", len(tr), "verts", len(vx), "watertight", m3.is_watertight, "vol", m3.volume, "bbox", m3.bounds.tolist())
# compare triangle sets (as rounded coordinate triples, orientation preserved by cyclic normalization)
md_ = trimesh.load(STL, process=False)
w3, f3, u3 = tri_match(m3, md_); w4, f4, u4 = tri_match(md_, m3)
print("3mf vs stl: worst vertex", w3, w4, "flips", f3, f4, "unique", u3, u4)
k3 = set(); ks = {1} if (max(w3, w4) > 1e-4 or f3 + f4 or u3 != len(md_.faces)) else set()
g("U-07", Result("3mf_same_mesh", int(len(k3 ^ ks) == 0 and unit == "millimeter" and xml.count("<object ") == 1), "bool", at=f"3MF {len(tr)} tris, unit {unit}, vol {m3.volume:.2f}, watertight {m3.is_watertight}"), "==", 1, note="3MF carries the STL's triangles exactly (same winding), mm")
g("U-07", Result("3mf_watertight", int(m3.is_watertight and m3.is_winding_consistent and m3.volume > 0), "bool"), "==", 1, note="3MF one closed shell facing out")
# mesh wall corroboration (D-025): min_wall_mesh >= B-rep 1.8 - chordal
mm = min_wall_mesh(STL); print("min_wall_mesh", mm.measured, mm.at, mm.status, mm.reason, mm.detail.get("vertex_precision_mm"))
g("U-07", mm, ">=", 1.8 - 0.01 - 1e-4, note="mesh wall corroborates B-rep 1.8 (pins) within chordal tolerance")
dump("r05_mesh.json")
