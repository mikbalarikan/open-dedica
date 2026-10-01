"""RV01 measurement 2: radial probes of the foot (REQ-01/03/04, J-05, D-04c), foot frame."""
import json, math
from pathlib import Path
from build123d import Box, Cylinder, Align, Pos
from tools.core import read_step
from tools.core.shapes import faces, edges
from tools.measure import radial_extent, radial_profile, min_wall, clearance, envelope
from tools.measure.sampling import kind
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.BRepBndLib import BRepBndLib
from OCP.Bnd import Bnd_Box
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from OCP.TopoDS import TopoDS_Compound
from OCP.BRep import BRep_Builder

W = Path("/home/claude/oguz-env/jobs/20261001-od-c15-feet")
foot = read_step(W / "02_STEP_STL/od_c15_foot_C1_v01.step")
O, Z, X = (0, 0, 0), (0, 0, 1), (1, 0, 0)
out = {}
def r(res): return None if res.measured is None else round(res.measured, 6)
def rx(res): return {"m": r(res), "at": res.at, "st": res.status, "why": res.reason}

# REQ-03 pocket: innermost material at z 6 (pocket middle), r window 2.0..4.5
pk = {}
for z in (2.6, 4.0, 6.0, 8.0, 9.4):
    pk[z] = {a: r(radial_extent(foot, O, Z, X, a, z, side="inner", r_min=2.0)) for a in range(0, 360, 30)}
out["pocket_inner"] = pk
af = {}
for z in pk:
    af[z] = {f"{a}+{a+180}": round(pk[z][a] + pk[z][a + 180], 6) for a in (30, 90, 150)}
    af[z]["centre_dx_dy"] = None
out["across_flats"] = af
# centre: flats at 90/270 give y offset; 30/210 & 150/330 give components
c = {}
for z in pk:
    dy = (pk[z][90] - pk[z][270]) / 2
    d30 = (pk[z][30] - pk[z][210]) / 2
    d150 = (pk[z][150] - pk[z][330]) / 2
    c[z] = (dy, d30, d150, max(abs(dy), abs(d30), abs(d150)))
out["centre_offsets"] = c
# rotation: readings either side of the +Y flat normal at 80 and 100 deg: r = d/cos(theta-90-phi)
rot = {}
for z in (4.0, 6.0, 8.0):
    r80 = radial_extent(foot, O, Z, X, 80, z, side="inner", r_min=2.0).measured
    r100 = radial_extent(foot, O, Z, X, 100, z, side="inner", r_min=2.0).measured
    # d = r80 cos(-10 - phi) = r100 cos(10 - phi) -> tan(phi) = (r100 - r80) cos10 / ((r100 + r80) sin10)... solve numerically
    best = min((abs(r80 * math.cos(math.radians(-10 - p)) - r100 * math.cos(math.radians(10 - p))), p)
               for p in [i / 10000 for i in range(-50000, 50001)])
    rot[z] = {"r80": r80, "r100": r100, "phi_deg": best[1]}
out["flat_rotation"] = rot
# plane normals of the six flats (B-rep, independent corroboration)
fl = []
for f in faces(foot):
    if kind(f) != "plane": continue
    s = BRepAdaptor_Surface(f); p = s.Plane(); n = p.Axis().Direction(); l = p.Location()
    if abs(n.Z()) < 1e-9:
        d = abs(l.X() * n.X() + l.Y() * n.Y())
        fl.append({"normal_deg": round(math.degrees(math.atan2(n.Y(), n.X())) % 180, 6), "dist": round(d, 6)})
out["flat_planes"] = fl
# seat and mouth
out["seat_probe_z2.49_90"] = rx(radial_extent(foot, O, Z, X, 90, 2.49, side="inner"))
out["seat_probe_z2.51_90"] = rx(radial_extent(foot, O, Z, X, 90, 2.51, side="inner"))
out["mouth_z9.999_90"] = rx(radial_extent(foot, O, Z, X, 90, 9.999, side="inner"))
out["mouth_z9.5001_90"] = rx(radial_extent(foot, O, Z, X, 90, 9.5001, side="inner"))
out["mouth_z9.4999_90"] = rx(radial_extent(foot, O, Z, X, 90, 9.4999, side="inner"))
# REQ-04 body
prof = radial_profile(foot, O, Z, X, list(range(0, 360, 10)), (0.6, 8.9), margin=0, z_step=0.5, side="outer")
out["body_profile"] = {k: rx(v) for k, v in prof.items()}
for z in (0.0001, 0.25, 0.4999, 0.5001, 8.9999, 9.0001, 9.5, 9.9999):
    out[f"outer_z{z}"] = rx(radial_extent(foot, O, Z, X, 45, z, side="outer"))
# chamfer faces: z and r extents of the cones from their bounding boxes
cones = []
for f in faces(foot):
    if kind(f) != "cone": continue
    b = Bnd_Box(); BRepBndLib.AddOptimal_s(f, b, False, False)
    x0, y0, z0, x1, y1, z1 = b.Get()
    s = BRepAdaptor_Surface(f).Cone()
    cones.append({"z": (round(z0, 6), round(z1, 6)), "r_max": round(x1, 6), "semi_angle_deg": round(math.degrees(s.SemiAngle()), 6), "ref_radius": round(s.RefRadius(), 6)})
out["cones"] = cones
# mouth chamfer planes: z extents and normal
mc = []
for f in faces(foot):
    if kind(f) != "plane": continue
    n = BRepAdaptor_Surface(f).Plane().Axis().Direction()
    if 1e-6 < abs(n.Z()) < 0.999999:
        b = Bnd_Box(); BRepBndLib.AddOptimal_s(f, b, False, False)
        mc.append({"nz": round(n.Z(), 6), "z": (round(b.Get()[2], 6), round(b.Get()[5], 6))})
out["mouth_chamfer_planes"] = mc
# REQ-01 top annulus: outer radius at z 0 = inner edge of top face; probe at z 0.00001 on 12 angles
out["top_outer_r_z1e-5"] = [r(radial_extent(foot, O, Z, X, a, 1e-5, side="outer")) for a in range(0, 360, 30)]
# J-05 ring z 2.5..10
ring = foot & Pos(0, 0, 2.5) * Cylinder(20, 10, align=(Align.CENTER, Align.CENTER, Align.MIN))
out["ring_envelope"] = {k: round(v.measured, 6) for k, v in envelope(ring).items()}
mw = min_wall(ring); out["J05_ring_min_wall"] = rx(mw); out["J05_ring_wide"] = mw.detail.get("wide")
# least face-to-face distance, pocket faces (flats + mouth chamfer planes) to outer faces (cylinder Ø18 + counter cone)
def comp(fs):
    b = BRep_Builder(); c = TopoDS_Compound(); b.MakeCompound(c)
    for f in fs: b.Add(c, f)
    return c
pocket_f, outer_f = [], []
for f in faces(ring):
    k = kind(f); s = BRepAdaptor_Surface(f)
    if k == "plane":
        n = s.Plane().Axis().Direction()
        if abs(n.Z()) < 0.999999: pocket_f.append(f)
    elif k == "cylinder" and s.Cylinder().Radius() > 8: outer_f.append(f)
    elif k == "cone": outer_f.append(f)
d = BRepExtrema_DistShapeShape(comp(pocket_f), comp(outer_f)); d.Perform()
p1, p2 = d.PointOnShape1(1), d.PointOnShape2(1)
out["J05_pocket_to_outer"] = {"d": round(d.Value(), 6), "n_pocket": len(pocket_f), "n_outer": len(outer_f),
                              "on_pocket": (round(p1.X(), 4), round(p1.Y(), 4), round(p1.Z(), 4)),
                              "on_outer": (round(p2.X(), 4), round(p2.Y(), 4), round(p2.Z(), 4))}
# corner radial material at 0,60..300 over z 2.6..10
corner = {}
for a in range(0, 360, 60):
    vals = []
    for z in (2.6, 5.0, 9.0, 9.5, 9.9, 9.999):
        ri = radial_extent(foot, O, Z, X, a, z, side="inner", r_min=2.0).measured
        ro = radial_extent(foot, O, Z, X, a, z, side="outer").measured
        vals.append((z, round(ri, 4), round(ro, 4), round(ro - ri, 4)))
    corner[a] = vals
out["J05_corner_radial"] = corner
# D-04c: ring vs shank envelope Ø3.0, z 2.5..6.0
shank = Pos(0, 0, 2.5) * Cylinder(1.5, 3.5, align=(Align.CENTER, Align.CENTER, Align.MIN))
out["D04c"] = rx(clearance(ring, shank))
json.dump(out, open(W / "reviews/RV01_work/m02_radial.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
