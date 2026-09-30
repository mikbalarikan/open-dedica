import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from geo import *
from tools.measure import radial_extent, radial_profile, bore_census, locate_bore, envelope
from tools.core import common_volume
m = load_mount(); R = {}
def p(k, v): R[k] = v; print(k, v)
# --- REQ-06 / REQ-05 / REQ-02 bores
bc = bore_census(m)
for tag, pt in (("foot(-18,21)", (-18, 21, 2)), ("foot(-18,-21)", (-18, -21, 2)), ("foot(88.5,21)", (88.5, 21, 2)), ("foot(88.5,-21)", (88.5, -21, 2)),
                ("clr(77.447)", (77.447, 0, 47)), ("clr(46.662)", (46.662, 0, 47)), ("ins(77.447)", (77.447, 0, 43)), ("ins(46.662)", (46.662, 0, 43)),
                ("pin1", (0.185, 0.093, 5)), ("pin2", (-11.78, 0.14, 5))):
    lb = locate_bore(bc, pt, (0, 0, 1))
    p("bore " + tag, {k: (round(r.measured, 5) if r.measured is not None else None) for k, r in lb.items()} | {"start": lb["diameter"].detail.get("start"), "end": lb["diameter"].detail.get("end"), "open_ends": lb["diameter"].detail.get("open_ends")})
# --- plate top / pedestal top / ring top / recess floor via vertical rays
for tag, xy in (("plate top", (-22, 0)), ("pedestal top", (15.0, 0)), ("ring top", (17.3, 0)), ("recess floor", (8.0, 5.0)), ("deck", (70, -10)), ("deck2", (50, 10))):
    r = ray(m, (xy[0], xy[1], 60), (0, 0, -1)); p("vray " + tag, [(round(60 - b, 5), round(60 - a, 5)) for a, b in stretches(r)])
# --- REQ-01 ring inner profile
rp = radial_profile(m, (0, 0, 0), (0, 0, 1), (1, 0, 0), [float(a) for a in range(360)], (10.5, 12.5), margin=0, z_step=0.25, side="inner", r_min=15.0, r_max=19.0)
p("REQ-01 ring inner", {k: (r.status, r.measured, r.at, r.detail.get("angle_deg"), r.detail.get("z")) for k, r in rp.items()} | {"unread": rp["min"].detail.get("unread")})
# ring outer too
rpo = radial_profile(m, (0, 0, 0), (0, 0, 1), (1, 0, 0), [float(a) for a in range(0, 360, 5)], (10.6, 12.9), margin=0, z_step=0.5, side="outer", r_min=15.0, r_max=19.0)
p("ring outer", {k: (r.measured, r.at) for k, r in rpo.items()})
# --- REQ-02 recess profile z 9.5..9.9
rr = radial_profile(m, (0, 0, 0), (0, 0, 1), (1, 0, 0), [float(a) for a in range(360)], (9.5, 9.9), margin=0, z_step=0.1, side="inner", r_min=13.0, r_max=17.0)
p("REQ-02 recess inner", {k: (r.status, r.measured, r.at) for k, r in rr.items()} | {"unread": rr["min"].detail.get("unread")})
# --- hooks
for th in (70, 160, 320):
    # angular edges at z 15, r 21.87
    edges = []
    prev = None
    for i in range(-1200, 1201):
        a = th + i * 0.01
        x, y = 21.87 * math.cos(math.radians(a)), 21.87 * math.sin(math.radians(a))
        inside = None
    # side faces: rays tangential from a point on the hook centreline
    c = (21.87*math.cos(math.radians(th)), 21.87*math.sin(math.radians(th)), 15.0)
    t = (-math.sin(math.radians(th)), math.cos(math.radians(th)), 0)
    rp_ = ray(m, c, t, side="outer", window=(0, 10)); rm_ = ray(m, c, (-t[0], -t[1], 0), side="outer", window=(0, 10))
    hp = stretches(rp_)[0][1] if stretches(rp_) else None; hm = stretches(rm_)[0][1] if stretches(rm_) else None
    # chord half-lengths from centre -> side faces are radial planes; angle of each side
    ap = math.degrees(math.atan2(hp, 21.87)); am = math.degrees(math.atan2(hm, 21.87))
    centre = th + (ap - am) / 2
    # beam inner/outer at the centre over z 6..26
    prof_in = radial_profile(m, (0,0,0), (0,0,1), (1,0,0), [th - 5.0, th, th + 5.0], (6, 26), margin=0, z_step=0.5, side="inner", r_min=19.5, r_max=24)
    prof_out = radial_profile(m, (0,0,0), (0,0,1), (1,0,0), [th - 5.0, th, th + 5.0], (6, 26), margin=0, z_step=0.5, side="outer", r_min=19.5, r_max=24)
    catch = radial_extent(m, (0,0,0), (0,0,1), (1,0,0), th, 30.4, side="inner", r_min=17.0, r_max=24)
    catch_e = [radial_extent(m, (0,0,0), (0,0,1), (1,0,0), th + d, 30.4, side="inner", r_min=17.0, r_max=24).measured for d in (-7.0, 7.0)]
    # catch underside: vertical ray down at r 19.5 from z 40
    cx, cy = 19.5*math.cos(math.radians(th)), 19.5*math.sin(math.radians(th))
    vr = ray(m, (cx, cy, 45), (0, 0, -1))
    # chamfer: inner radius at z 32.0 and 33.0
    c1 = radial_extent(m, (0,0,0), (0,0,1), (1,0,0), th, 32.0, side="inner", r_min=17.0, r_max=24).measured
    c2 = radial_extent(m, (0,0,0), (0,0,1), (1,0,0), th, 33.0, side="inner", r_min=17.0, r_max=24).measured
    ch = math.degrees(math.atan2(1.0, c2 - c1))
    # root-level thickness (t) at z 6, 15, 25
    tt = []
    for z in (6.0, 15.0, 25.0):
        o = radial_extent(m, (0,0,0), (0,0,1), (1,0,0), th, z, side="outer", r_min=19.5, r_max=24).measured
        i_ = radial_extent(m, (0,0,0), (0,0,1), (1,0,0), th, z, side="inner", r_min=19.5, r_max=24).measured
        tt.append(round(o - i_, 5))
    catch_t = radial_extent(m, (0,0,0), (0,0,1), (1,0,0), th, 30.4, side="outer", r_min=17.0, r_max=24).measured - catch.measured
    p(f"hook {th}", {"half_chords": (hp, hm), "centre_deg": round(centre, 4), "beam_in": (prof_in["min"].measured, prof_in["max"].measured), "beam_out": (prof_out["min"].measured, prof_out["max"].measured),
                     "catch_R": catch.measured, "catch_R_edges": catch_e, "vray_r19.5": [(round(45 - b, 4), round(45 - a, 4)) for a, b in stretches(vr)],
                     "chamfer_deg": round(ch, 4), "c1c2": (c1, c2), "t": tt, "catch_radial_len": catch_t})
dump("s04.json", R)
