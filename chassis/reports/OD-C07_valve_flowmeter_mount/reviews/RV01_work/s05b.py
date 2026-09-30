import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from geo import *
from tools.measure import radial_extent, radial_profile
m = load_mount(); R = {}
def p(k, v): R[k] = v; print(k, str(v)[:900])
V = (62.0, 0.0, 0.0)
lit = radial_profile(m, V, (0,0,1), (1,0,0), [float(a) for a in range(180, 361)], (41, 47), margin=0, z_step=0.25, side="inner", r_min=0, r_max=27)
un = lit["min"].detail["unread"]
p("unread sample", un[:3]); p("unread angles", sorted({u["angle_deg"] for u in un}))
# re-read the literal window with r_max 60 so long stretches are not refused
lit = radial_profile(m, V, (0,0,1), (1,0,0), [float(a) for a in range(180, 361)], (41, 47), margin=0, z_step=0.25, side="inner", r_min=0, r_max=60)
p("literal 180..360 r_max 60", {k: (r.status, r.measured, r.at, r.detail.get("angle_deg"), r.detail.get("z")) for k, r in lit.items()} | {"unread": len(lit["min"].detail.get("unread") or [])})
# gate reading: 180..360 excluding the two slit windows (|angle-180|,|angle-360| <= 10), plus the full 180..360 below the slit floor (z 41..43.3)
angs = [float(a) for a in range(180, 361) if min(abs(a-180), abs(a-360)) > 10]
g1 = radial_profile(m, V, (0,0,1), (1,0,0), angs, (41, 47), margin=0, z_step=0.25, side="inner", r_min=0, r_max=60)
g2 = radial_profile(m, V, (0,0,1), (1,0,0), [float(a) for a in range(180, 361)], (41, 43.3), margin=0, z_step=0.1, side="inner", r_min=0, r_max=60)
for nm, g in (("slot 190..350 z41..47", g1), ("slot 180..360 z41..43.3", g2)):
    p(nm, {k: (r.status, r.measured, r.at, r.detail.get("angle_deg"), r.detail.get("z")) for k, r in g.items()} | {"unread": len(g["min"].detail.get("unread") or [])})
for bx in (77.447, 46.662):
    rows = []
    for z in (40.4, 41.5, 43.15, 44.8, 45.9, 45.99):
        ends = {}
        for k in range(72):
            a = k * 5.0
            r = radial_extent(m, (bx, 0, 0), (0,0,1), (1,0,0), a, z, side="outer", r_min=0, r_max=60)
            st = [s for s in stretches(r) if s[0] < 2.05]
            ends[a] = (st[0][1] if st else None, r.status, r.reason[:80])
        bad = {a: v for a, v in ends.items() if v[0] is None}
        e = {a: v[0] for a, v in ends.items() if v[0] is not None}
        across = min(e[a] + e[(a + 180) % 360] for a in [k*5.0 for k in range(36)] if a in e and (a+180) % 360 in e)
        wa = min(e, key=lambda a: e[a])
        rows.append((z, round(across, 4), round(e[wa] - 2.0, 4), wa, len(bad), list(bad.items())[:1]))
    p(f"insert pad {bx} (z, least across, least wall, angle, unread)", rows)
for bx, a0 in ((46.662, 0.0), (77.447, 180.0)):
    wrow = []
    for z in (47.999, 47.9, 47.5, 47.0, 46.5, 46.01):
        best = None
        for k in range(-60, 61):
            a = a0 + k * 0.5
            r = radial_extent(m, (bx, 0, 0), (0,0,1), (1,0,0), a, z, side="outer", r_min=0, r_max=60)
            st = [s for s in stretches(r) if s[0] < 1.75]
            if st:
                w = st[0][1] - st[0][0]
                if best is None or w < best[0]: best = (round(w, 4), a)
        wrow.append((z, best))
    p(f"wedge {bx} (z, least wall from the Ø3.4 hole to the slit end, ray angle)", wrow)
dump("s05b.json", R)
