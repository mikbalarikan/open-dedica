import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from tools.measure import clearance, interference
from tools.core import common_volume
from build123d import Cylinder, Box, Pos, Align
m = load_mount()
h22, h24, h22p, h24p = load_oem()
H24 = comp(h24p); H22 = comp(h22p)
C = (Align.CENTER, Align.CENTER, Align.MIN)
def ann(r0, r1, z0, z1, x=0, y=0):
    s = Pos(x, y, z0) * Cylinder(r1, z1 - z0, align=C)
    if r0 > 0: s = s - Pos(x, y, z0 - 1) * Cylinder(r0, z1 - z0 + 2, align=C)
    return s
def box(x0,x1,y0,y1,z0,z1):
    return Pos(x0, y0, z0) * Box(x1-x0, y1-y0, z1-z0, align=(Align.MIN,)*3)
def cl(a, b, tag):
    r = clearance(a, b); print("%-55s %s %.4f at %s on_b %s" % (tag, r.status, r.measured if r.measured is not None else -1, r.at, r.detail.get("on_b")), r.reason); return r
out = {}
out["int_mount_h24"] = common_volume(m, H24).measured; out["int_mount_h22"] = common_volume(m, H22).measured
out["int_h22_h24"] = common_volume(H22, H24).measured
print(out)
out["cl_mount_h24"] = cl(m, H24, "mount|H24 all").to_dict()
out["cl_mount_h22"] = cl(m, H22, "mount|H22 all").to_dict()
# contact neighbourhoods
N24 = ann(13.98, 15.71, 10.0 - 0.001, 10.3)       # A-06 rim annulus up to the top of its edge rounds (H24 z 0.3)
H24away = H24 - N24
H22below = H22 - box(0, 130, -60, 60, 48.0 - 0.001, 80)   # everything strictly below the flange back face plane
out["cl_mount_h24away"] = cl(m, H24away, "mount|H24 minus rim neighbourhood").to_dict()
out["cl_mount_h22below"] = cl(m, H22below, "mount|H22 below flange plane").to_dict()
# mount regions near H24
ring = m & ann(16.0, 18.6, 10.0, 13.5)                # ring incl. its root fillet (toe at r 16.0)
recess = m & ann(0, 14.3, 9.0, 10.0)                   # recess floor, wall and edge chamfer
hooks = m & (ann(18.5, 30, 4.0, 40) )
pins_region = m & (ann(0, 13.5, 0, 9.41))
for tag, reg in (("ring(r>=16)", ring), ("recess(r<=14.3,z<=10)", recess), ("pedestal-inner(r<13.5,z<=9.41)", pins_region), ("hooks(r>=18.5,z>=4)", hooks)):
    out["cl_"+tag] = cl(reg, H24away, tag + " | H24 away").to_dict()
# H24 parts
ribs = H24 & ann(0, 13.98, 10.0, 10.5)                # rib/hub material inside the rim's inner radius
cup = H24 & ann(15.71, 16.5, 10.0, 14.0)
out["cl_recess_ribs"] = cl(recess, ribs, "recess | ribs&hub (r<13.98, z_H24<=0.5)").to_dict()
out["cl_mount_ribs"] = cl(m, ribs, "mount | ribs&hub (r<13.98)").to_dict()
ribs_all = (H24 & ann(0, 14.2, 10.05, 10.5))            # rib plane incl. its end on the rim inner round (to r 14.056)
out["cl_recess_ribs_full"] = cl(recess, ribs_all, "recess | ribs incl ends (r<14.2, z_H24 0.05..0.5)").to_dict()
out["cl_ring_cup"] = cl(ring, cup, "ring(incl fillet) | cup (r>=15.71)").to_dict()
ring_wall = m & ann(16.0, 18.6, 10.3, 13.5)
out["cl_ringwall_cup"] = cl(ring_wall, cup, "ring wall above fillet (z>=10.3) | cup").to_dict()
for z0 in (0.3, 0.5, 1.0):
    cupz = H24 & ann(15.0, 16.5, 10.0 + z0, 14.0)
    out[f"cl_ring_cup_z{z0}"] = cl(ring, cupz, f"ring | H24 r>15, z_H24>={z0}").to_dict()
# H22 regions
deck = m & box(36, 88, -16, 16, 40.0, 48.0)
out["cl_deck_h22below"] = cl(deck, H22below, "deck | H22 below").to_dict()
legs = m & box(30, 94, -26, 26, 0, 40.29)
out["cl_legsplate_h22"] = cl(legs, H22, "legs+plate below deck | H22").to_dict()
dump("s03.json", out)
