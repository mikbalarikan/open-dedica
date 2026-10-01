import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from geo import *
from tools.measure import radial_extent, overhang_census, clearance, envelope
from tools.core import common_volume, validity, step_roundtrip, read_step
from build123d import Solid
m = load_mount(); R = {}
def p(k, v): R[k] = v; print(k, str(v)[:900])
# ---- flat or shallow downward faces census (planar faces with normal -Z above the bed)
dn = []
for f in m.faces():
    if f.geom_type.name == "PLANE":
        n = f.normal_at(f.center())
        if n.Z < -0.99 and f.center().Z > 0.01:
            dn.append((round(f.center().Z, 4), round(f.area, 3), (round(f.center().X, 3), round(f.center().Y, 3))))
p("flat downward faces", sorted(dn))
# ---- overhang census in slabs whose floors sit on the named supported / bridge planes
slabs = [(0.0, 10.5), (10.5, 29.9), (29.9, 40.3), (40.3, 46.0), (46.0, 48.5)]
oh = []
for z0, z1 in slabs:
    s = m & box(-30, 100, -30, 30, z0, z1)
    r = overhang_census(s, (0, 0, 1), min_deg=45.0, spacing=0.5)
    oh.append({"slab": (z0, z1), "status": r.status, "least": r.measured, "at": r.at, "reason": r.reason, "bound": r.detail.get("sampling_bound_deg"), "below": r.detail.get("below_min_deg"), "per_kind": r.detail.get("per_kind_least_deg")})
p("overhang slabs", oh)
whole = overhang_census(m, (0, 0, 1), min_deg=45.0, spacing=0.5)
p("overhang whole part", (whole.status, whole.measured, whole.at, whole.detail.get("below_min_deg"), whole.detail.get("per_kind_least_deg")))
# ---- notches (REQ-09): tangential rays from the notch centreline at r 17.3, z 10.25; vertical ray for height
for th in (25, 115, 225):
    c = (17.3*math.cos(math.radians(th)), 17.3*math.sin(math.radians(th)))
    t = (-math.sin(math.radians(th)), math.cos(math.radians(th)), 0)
    wp = ray(m, (c[0], c[1], 10.25), t, window=(0, 10)).measured; wm = ray(m, (c[0], c[1], 10.25), (-t[0], -t[1], 0), window=(0, 10)).measured
    ang_off = math.degrees(math.atan2((wp - wm) / 2, 17.3))
    vr = ray(m, (c[0], c[1], 20), (0, 0, -1))
    rad = radial_extent(m, (0,0,0), (0,0,1), (1,0,0), th, 10.25, side="inner", r_min=14.5, r_max=19.5)
    through = common_volume(m, sector(th, 2.0, 15.0, 19.0, 10.05, 10.45)).measured
    through_box = common_volume(m, Rot(0, 0, th) * box(15.0, 19.0, -0.9, 0.9, 10.02, 10.48)).measured
    p(f"notch {th}", {"width": wp + wm, "centre_deg": th + ang_off, "vray": [(round(20-b,4), round(20-a,4)) for a, b in stretches(vr)], "radial_ray_at_centre": (rad.status, rad.measured, rad.reason[:60]), "material_in_notch_box": through_box})
# ---- hooks: J-04 interference / catch contact; landing void under each catch
h22, h24, h22p, h24p = load_oem(); H24 = comp(h24p)
for th in (70, 160, 320):
    hk = m & sector(th, 12.0, 18.5, 27.0, 4.0, 40.0)
    iv = common_volume(hk, H24).measured
    cl = clearance(hk, H24)
    beam = m & sector(th, 12.0, 20.5, 27.0, 5.6, 29.8)
    clb = clearance(beam, H24)
    # void under the catch: sector r 18.87..19.70 over the catch's angular span (+-7.88 deg), z 27.25..29.9
    prism = sector(th, 7.88, 18.87, 19.70, 27.25, 29.9)
    void = prism.volume - common_volume(prism, H24).measured
    catch_face = m & sector(th, 7.88, 18.87, 20.37, 29.9, 29.95)
    under = clearance(catch_face, H24)
    # hooks to anything of H24 above the flange top plane / outside r 20.5
    above = H24 & box(-40, 40, -60, 40, 29.901, 60)
    outside = H24 - ann(0, 20.5, 0, 60)
    p(f"hook {th}", {"interference_mm3": iv, "clearance": (cl.measured, cl.at), "beam_to_H24": (clb.measured, clb.at), "catch_underside_to_H24": (under.measured, under.at), "void_under_catch_mm3": void, "prism_vol": prism.volume,
                     "to_H24_above_flange_top": (clearance(hk, above).measured, clearance(hk, above).at), "to_H24_outside_r20.5": clearance(hk, outside).measured})
# ---- E-06: torus / fillet faces
tor = []
for f in m.faces():
    if f.geom_type.name == "TORUS":
        s = f._geom_adaptor(); t = s.Torus() if hasattr(s, "Torus") else None
        bb = f.bounding_box(); tor.append((round(f.area, 3), (round(bb.min.Z, 3), round(bb.max.Z, 3)), (round(t.MajorRadius(), 3), round(t.MinorRadius(), 3)) if t else None))
p("torus faces", tor)
cyl = []
for f in m.faces():
    if f.geom_type.name == "CYLINDER":
        s = f._geom_adaptor(); c = s.Cylinder(); bb = f.bounding_box()
        cyl.append((round(c.Radius(), 4), tuple(round(v, 3) for v in (bb.min.X, bb.max.X, bb.min.Y, bb.max.Y, bb.min.Z, bb.max.Z))))
p("cylinder faces", sorted(cyl))
cones = []
for f in m.faces():
    if f.geom_type.name == "CONE":
        s = f._geom_adaptor(); c = s.Cone(); bb = f.bounding_box()
        cones.append((round(math.degrees(c.SemiAngle()), 4), round(c.RefRadius(), 4), tuple(round(v, 3) for v in (bb.min.Z, bb.max.Z)), round(f.area, 3)))
p("cone faces", cones)
# ---- deck tied to legs: section at x 38 and x 86 through legs at z 44 (material continuous from deck into leg)
for x in (38.0, 86.0, 41.0, 83.0):
    r = ray(m, (x, 0, 60), (0, 0, -1))
    p(f"vray x={x}", [(round(60-b,4), round(60-a,4)) for a, b in stretches(r)])
# ---- U-04 round trip of the delivered body
raw = read_step(MOUNT)
from tools.core.shapes import occ
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL, TopAbs_SOLID, TopAbs_FACE
def count(sh, kind, avoid=None):
    e = TopExp_Explorer(occ(sh), kind) if avoid is None else TopExp_Explorer(occ(sh), kind, avoid); n = 0
    while e.More(): n += 1; e.Next()
    return n
p("file: shells / shells outside solids / faces outside shells", (count(raw, TopAbs_SHELL), count(raw, TopAbs_SHELL, TopAbs_SOLID), count(raw, TopAbs_FACE, TopAbs_SHELL)))
body = Solid(solids(raw)[0]); body.label = "od_c07_mount"
rt = step_roundtrip(body, W / "roundtrip_mount.step", timestamp="2026-09-30T00:00:00")
p("roundtrip of the re-read body", {k: (r.measured, r.status, r.reason[:80]) for k, r in rt.items()})
dump("s07.json", R)
