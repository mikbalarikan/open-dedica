import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from geo import *
from tools.core import validity, common_volume
from tools.measure import clearance, radial_extent
from tools.result import gate
from build123d import Solid
from OCP.TopoDS import TopoDS
m = load_mount(); h22, h24, h22p, h24p = load_oem(); H24 = comp(h24p); H22 = comp(h22p)
R = {}
def p(k, v): R[k] = v; print(k, str(v)[:600])
inv = Solid(TopoDS.Solid_s(m.wrapped.Reversed()))
v = validity(inv); g = gate("U-01", v["brep_valid"], "==", 1, band=0)
p("control brep_valid on the inside-out part", (g.status, g.measured, v["brep_valid"].reason[:120]))
R["control_brep_valid"] = {"check": "validity.brep_valid", "mutant": "exported part turned inside out (reversed solid)", "got": "FAIL" if g.status == "FAIL" else g.status}
ped = m & ann(14.4, 15.4, 9.0, 10.0)
p("rim face on the pedestal top: clearance / interference", (clearance(ped, H24).measured, clearance(ped, H24).at, common_volume(m, H24).measured))
deck = m & box(43, 81, -9.8, 9.8, 47.0, 48.0)
p("flange back face on the deck top: clearance", (clearance(deck, H22).measured, clearance(deck, H22).at))
p("pedestal outer R at z 7", radial_extent(m, (0,0,0), (0,0,1), (1,0,0), 45.0, 7.0, side="outer", r_min=10, r_max=19.5).measured)
for x in (38.0, 86.0):
    p(f"leg y extent at x={x}, z 20", (ray(m, (x, 0, 20), (0, 1, 0), side="outer", window=(0, 40)).measured, ray(m, (x, 0, 20), (0, -1, 0), side="outer", window=(0, 40)).measured))
p("deck y extent at x 50, z 44", (ray(m, (50, 0, 44), (0, 1, 0), side="outer", window=(0, 40)).measured, ray(m, (50, 0, 44), (0, -1, 0), side="outer", window=(0, 40)).measured))
# ring vs cup across heights of the cup: governing reading and its sensitivity
ring = m & ann(16.0, 18.6, 10.0, 13.5)
for z0, lab in ((0.25, "cup from z_H24 0.25 (end of rim round)"), (0.3, "cup from z_H24 0.30 (A-06 formula r 15.716)"), (0.5, "cup from z_H24 0.50")):
    c = clearance(ring, H24 & ann(15.0, 16.5, 10.0 + z0, 14.0)); p("ring|" + lab, (c.measured, c.at, c.detail["on_b"]))
ribs = H24 & ann(0, 13.98, 10.0, 10.5); rec = m & ann(0, 14.3, 9.0, 10.0)
for rmax in (13.68, 13.8, 13.9, 13.98, 14.056):
    c = clearance(rec, H24 & ann(0, rmax, 10.05, 10.5)); p(f"recess | ribs&hub inside r {rmax}", (round(c.measured, 4), c.at, c.detail["on_b"]))
dump("s12.json", R)
