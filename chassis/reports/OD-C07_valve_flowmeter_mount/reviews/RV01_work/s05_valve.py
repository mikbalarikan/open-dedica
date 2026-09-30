import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from geo import *
from tools.measure import radial_extent, radial_profile, envelope, clearance
from tools.core import common_volume
from build123d import Face, Plane
m = load_mount(); R = {}
def p(k, v): R[k] = v; print(k, str(v)[:700])
def short(rp): return {k: (r.status, r.measured, r.at, r.detail.get("angle_deg"), r.detail.get("z")) for k, r in rp.items()} | {"unread": len(rp["min"].detail.get("unread") or [])}
rr = radial_profile(m, (0, 0, 0), (0, 0, 1), (1, 0, 0), [float(a) for a in range(360)], (9.5, 9.9), margin=0, z_step=0.1, side="inner", r_min=13.0, r_max=19.0)
p("REQ-02 recess inner", short(rr))
# ---- REQ-04 slot profile literal 180..360, z 41..47
V = (62.0, 0.0, 0.0)
lit = radial_profile(m, V, (0,0,1), (1,0,0), [float(a) for a in range(180, 361)], (41, 47), margin=0, z_step=0.25, side="inner", r_min=0, r_max=27)
p("REQ-04 slot literal 180..360", short(lit))
pts = lit["min"].detail["points"]
over = [q for q in pts if q["radius"] > 7.10 + BAND_MM]
p("  literal rays above 7.10", {"n": len(over), "angles": sorted({q["angle_deg"] for q in over}), "z_min": min(q["z"] for q in over) if over else None})
nonslit = [q for q in pts if not (q["angle_deg"] in {a for a in [q2["angle_deg"] for q2 in over]})]
# rays outside the slit windows: |y| > 1.2 at r 7.05 -> angle more than asin(1.2/7.05) from 180/360
lim = math.degrees(math.asin(1.2/7.05)); p("slit half-window deg", lim)
ok = [q["radius"] for q in pts if min(abs(q["angle_deg"]-180), abs(q["angle_deg"]-360)) > lim]
p("  rays outside slit windows min/max", (min(ok), max(ok), len(ok)))
low = [q["radius"] for q in pts if q["z"] < 43.3]
p("  all 180..360 rays below z 43.3 min/max", (min(low), max(low), len(low)))
# straight walls
walls = {}
for y in (2.5, 5, 8, 11, 14):
    for z in (41.0, 44.0, 47.0):
        a = ray(m, (62, y, z), (1, 0, 0), window=(0, 30)).measured; b = ray(m, (62, y, z), (-1, 0, 0), window=(0, 30)).measured
        walls[(y, z)] = (a, b)
p("slot straight walls (+X,-X) by (y,z)", {str(k): v for k, v in walls.items()})
p("slot open to +Y: material in x 62+-6.9, y 0..16, z 40..48.5", common_volume(m, box(55.1, 68.9, 0, 16, 40, 48.5)).measured)
p("slot through deck: vertical ray at (62,-6.9)", [(round(60-b,4), round(60-a,4)) for a, b in stretches(ray(m, (62, -7.3, 60), (0,0,-1)))])
p("slot closed bore? ray at 90deg (toward +Y) from axis z 44", ray(m, (62, 0, 44), (0, 1, 0), window=(0, 30)).detail.get("material"))
# slits: width at x = 62 +- 9.5 z 47.5 & 45.5 ; reach at top from rays along +-X at y 0 and several z
sl = {}
for sx in (+1, -1):
    for z in (47.9, 47.5, 46.5, 45.5, 44.5):
        e = ray(m, (62, 0, z), (sx, 0, 0), window=(0, 30)).measured
        sl[(sx, z)] = e
    for z in (47.5, 46.0):
        wy = [ray(m, (62 + sx*9.5, 0, z), (0, d, 0), window=(0, 20)).measured for d in (1, -1)]
        sl[(sx, "w", z)] = wy
p("slit rays", {str(k): v for k, v in sl.items()})
for sx in (+1, -1):
    z1, z2 = 47.9, 45.5
    e1, e2 = sl[(sx, z1)], sl[(sx, z2)]
    slope = (e1 - e2) / (z1 - z2); reach = e1 + slope * (48.0 - z1); ang = math.degrees(math.atan2(z1 - z2, e1 - e2))
    p(f"slit {sx:+d} reach at z48 / taper deg", (reach, ang))
# deck top z and flatness under the flange outline
h22, h24, h22p, h24p = load_oem()
H22 = comp(h22p)
ff = [f for f in H22.faces() if f.geom_type.name == "PLANE" and abs(f.center().Z - 48.0) < 1e-6 and f.normal_at(f.center()).Z < -0.99]
p("flange back faces", [(round(f.area, 3)) for f in ff])
F = ff[0]
tops = [f for f in m.faces() if f.geom_type.name == "PLANE" and f.normal_at(f.center()).Z > 0.99 and f.center().Z > 40]
p("mount +Z planes above z40", [(round(f.center().Z, 5), round(f.area, 3)) for f in tops])
supported = sum((F & t).area for t in tops if abs(t.center().Z - 48.0) < 1e-6)
sec = m & box(30, 95, -30, 30, 47.99, 48.0)   # thin slab of the deck top
slab_area = sum(f.area for f in sec.faces() if f.normal_at(f.center()).Z > 0.99)
p("flange area / on z48 top faces / flange over openings", (F.area, supported, F.area - supported))
# openings under flange from the thin slab (openings = flange minus slab-top)
fs = sum((F & f).area for f in sec.faces() if f.normal_at(f.center()).Z > 0.99)
p("flange over material at z 47.99..48 (slab top) ", fs)
# REQ-07
plate = m & box(-30, 100, -30, 30, -1, 4.0)
ps = solids(plate)
p("plate pieces", [tuple(round(v, 4) for v in (Solid(s).bounding_box().min.X, Solid(s).bounding_box().max.X, Solid(s).bounding_box().min.Y, Solid(s).bounding_box().max.Y)) for s in ps])
p("window material x 40.001..83.999 z -1..40.299", common_volume(m, box(40.001, 83.999, -26, 26, -1, 40.299)).measured)
lg = {}
for y in (-14, 0, 14):
    for z in (6, 20, 39):
        lg[(y, z)] = (62 - ray(m, (62, y, z), (-1, 0, 0), window=(0, 40)).measured, 62 + ray(m, (62, y, z), (1, 0, 0), window=(0, 40)).measured)
p("leg inner faces", {str(k): v for k, v in lg.items()})
# REQ-08
e = envelope(m); p("max z", e["max_z"].measured)
p("material within r12 of valve axis above deck", common_volume(m, ann(0, 12, 48.0, 70, 62, 0)).measured)
p("material within r12, z 48.0001..70", common_volume(m, ann(0, 12, 48.0001, 70, 62, 0)).measured)
dump("s05.json", R)
