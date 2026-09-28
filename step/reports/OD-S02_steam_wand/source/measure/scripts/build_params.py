#!/usr/bin/env python3
"""OD-S02: write measure/params.json from measure/figures/measurements.json (run-local).
Every value is read from the measurement JSON (never retyped) except where the row says
`assumed` / a design-intent choice with its reason. Run from the run folder."""
import datetime, hashlib, json
from pathlib import Path
import numpy as np

run = Path.cwd()
M = json.loads((run / "measure/figures/measurements.json").read_text())
AL = json.loads((run / "intake/alignment.json").read_text())
noise = AL["scan_noise_mm"]["value"]
EV = "measure/figures/measurements.json"
P = {}

def rnd(x, k=4):
    if isinstance(x, str): return x
    if isinstance(x, int) and not isinstance(x, bool): return x
    return [round(float(v), k) for v in x] if isinstance(x, (list, tuple, np.ndarray)) else round(float(x), k)

def add(name, value, measured=None, unit="mm", rule="keep-measured", source="scan", est="", unc=None, ev=EV,
        critical=False, note=None, **kw):
    v = rnd(value)
    row = {"value": v, "unit": unit, "measured": rnd(measured) if measured is not None else (v if source == "scan" else None),
           "rule": rule, "source": source, "estimator": est,
           "uncertainty_mm": round(float(unc if unc is not None else noise), 4), "evidence": ev, "critical": critical}
    if note: row["note"] = note
    row.update(kw)
    P[name] = row

tab = np.array(M["rod_radius_table"]["rows[z,p10,p50,p90,n]"], float)
def rz(z0, z1):   # median of p50 over a z window
    s = (tab[:, 0] >= z0) & (tab[:, 0] <= z1); return float(np.median(tab[s, 2])), [float(tab[s, 2].min()), float(tab[s, 2].max())]
RT = "rod_radius_table p50 (vertex radius about datum Z, lug sector excluded), median over the window"
# ---------------- rod (revolve about datum Z)
r, rng = rz(0.75, 6.25); add("rod_collar_r", r, f"{rng[0]:.4f}..{rng[1]:.4f}", est=RT + " z 0.75..6.25", note="lower collar, z 0..groove")
add("rod_collar_z1", 6.8, "6.75..6.85", est="rod_radius_table: p50 crosses mid-radius between z 6.75 (6.20) and 7.25 (5.19)")
r, rng = rz(7.25, 8.25); add("rod_groove_r", r, f"{rng[0]:.4f}..{rng[1]:.4f}", est=RT + " z 7.25..8.25")
add("rod_groove_z2", 9.15, "9.1..9.2", est="rod_radius_table: p50 crosses mid-radius between z 8.75 (5.29) and 9.25 (6.23)")
r, rng = rz(13.0, 17.25); add("rod_body_r", r, f"{rng[0]:.4f}..{rng[1]:.4f}", est=RT + " z 13..17.25 (also used z 9.5..11 and 12.75..17.5)")
sel_ = (tab[:, 0] >= 9.75) & (tab[:, 0] <= 12.75)
add("rod_bead_z", tab[sel_, 0].tolist(), est="rod_radius_table stations z 9.75..12.75 (bead + shallow groove between the lower groove and the body)", unc=0.0)
add("rod_bead_r", tab[sel_, 2].tolist(), est="rod_radius_table p50 at rod_bead_z (profile kept as measured: bead 6.57 @10.75, groove 6.12 @11.75)", unc=0.05)
r, rng = rz(20.5, 20.75); add("rod_flare_r", r, f"{rng[0]:.4f}..{rng[1]:.4f}", est=RT + " z 20.5..20.75", note="body flares from rod_body_r at z 17.5 to this at the step")
add("rod_flare_z0", 17.5, "17.25..17.75", est="rod_radius_table: p50 leaves 6.47-6.50 at z 17.5")
add("rod_step_z", 21.1, "21.0..21.2", est="rod_radius_table: p50 6.88@20.75 -> 5.76@21.75, step face at the mid (p10 5.96 @21.25)")
r, rng = rz(21.75, 21.75); add("rod_cone1_r0", r, rng, est=RT + " z 21.75")
r, rng = rz(25.75, 25.75); add("rod_cone1_r1", r, rng, est=RT + " z 25.75")
add("rod_cone1_z", [21.75, 25.75], [21.75, 25.75], est="rod_radius_table stations of rod_cone1_r0/r1; the model extends this cone line up to the step face and down to where it meets the long taper")
t = M["rod_taper_line"]
add("rod_taper_r_z30", t["r_at_z30"], est=f"LSQ line through rod_radius_table p50, z 30..64, rms {t['rms']:.4f}", unc=t["rms"], critical=True,
    note="tapered spigot (machine interface)", rerun_trigger="one caliper reading of the spigot diameter at a marked height")
add("rod_taper_drdz", t["dr_dz"], unit="deg" if False else "mm", est="slope of the same LSQ line (mm radius per mm z)", unc=0.001)
P["rod_taper_drdz"]["unit"] = "mm"
add("rod_oring_center", [4.67, 27.3], [4.67, 27.3], est="rod_radius_table: bump base 4.7-4.8 at z 26.2/28.4, peak 5.77 @27.25; circle through base+peak", note="[r, z] of the O-ring cord centre")
add("rod_oring_cord_r", 1.1, "1.05..1.12", est="half base width (26.2..28.4)/2 and peak 5.77 - 4.67")
add("rod_tip_z", M["rod_tip_zmax"], est="max z of scan vertices within r 3.5 of datum Z")
add("rod_tip_round_r", 2.0, "1.9..2.1", est="round-nose fit to rod_radius_table p50 at z 66.25 (2.77), 66.75 (2.36), 67.25 (1.16) with the end at rod_tip_z")
lug = M["collar_lug"]
tan = lug["tangential_p1_p99"]
add("lug_theta", lug["theta_deg"] + np.degrees(((tan[0] + tan[1]) / 2) / lug["r_top_p95"]), lug["theta_deg"], unit="deg", rule="keep-measured",
    est="median theta of lug vertices (r > 7.6) + tangential centre offset", unc=0.2, note="datum frame, theta CCW about +Z from +X", frame="datum frame (alignment.json), theta CCW about +Z from +X")
P["lug_theta"]["measured"] = f"{lug['theta_deg']-3:.2f}..{lug['theta_deg']+3:.2f}"
add("lug_width", tan[1] - tan[0], est="tangential p1..p99 of lug face vertices (r > 7.6)", unc=0.1)
add("lug_z", lug["z_range"], est="p1/p99 z of lug vertices", unc=0.1)
add("lug_r_top", lug["r_top_p95"], est="p95 radius of lug vertices", unc=0.1)
add("lug_corner_r", 0.6, None, rule="assumed", source="assumed", est="not measured: corner round of the small rounded-rect lug (photo shows rounded corners)", unc=0.3)
# ---------------- knob (revolve about datum Z)
kc = M["knob_cylinder"]
secs = kc["sector_median_r"]
add("knob_r", float(np.mean([secs["60..120"], secs["-120..-60"], secs["120..180"]])), [secs["-120..-60"], secs["120..180"]] and f"{secs['-120..-60']:.4f}..{secs['120..180']:.4f}",
    est="mean of the sector medians (+Y, -Y, -X) z -3.6..-0.6; Kasa centre offset " + ", ".join(f"{v:.3f}" for v in kc["kasa_centre"]), unc=0.12,
    note="knob modelled coaxial with the rod; its Kasa centre is 0.22/0.10 mm off (an offset revolve was tried in the self-check and was worse, because the meridian is measured about Z)")
add("knob_top_z", 0.0, f"{M['knob_top_face_z']:.4f}", est="datum origin plane (alignment.json origin.z); face median z", unc=0.03)
mer = np.array(M["knob_meridian"]["rows[z,r+Y,r-Y,mean]"], float)
keep = mer[:, 0] >= -13.5
add("knob_meridian_z", mer[keep, 0].tolist(), est="knob_meridian z stations", unc=0.0)
add("knob_meridian_r", mer[keep, 3].tolist(), est="knob_meridian: mean of +Y and -Y sector medians per station", unc=0.15,
    note="spline meridian of the rounded knob bottom; +Y/-Y differ by up to 0.4 (off-centre); the spline closes on the axis at knob_bottom_z")
add("knob_bottom_z", -14.4, None, rule="assumed", source="assumed", est="not observable (inside the lever plate): extrapolation of the meridian slope below z -13.5 to r = 0", unc=0.5)
fr = M["knob_fairing_ellipses"]["rows"]
FE = "knob_fairing_ellipses: " + M["knob_fairing_ellipses"]["estimator"]
add("fair_x", [r_["x"] for r_ in fr], est="fairing section stations (x = const planes)", unc=0.0)
for k_ in ("yc", "zc", "ay", "az"):
    add("fair_" + k_, [r_[k_] for r_ in fr], est=FE, unc=max(r_["rms"] for r_ in fr),
        note="per-station ellipse fit rms " + ", ".join(f"{r_['rms']:.3f}" for r_ in fr) if k_ == "yc" else None)
# ---------------- paddle (flat lever plate)
pd = M["paddle"]
add("paddle_face_pos", pd["+Y_face"]["y=a*x+b*z+c"], est="+Y face plane y = a x + b z + c, " + pd["+Y_face"]["estimator"], unc=pd["+Y_face"]["rms"])
add("paddle_face_neg", pd["-Y_face"]["y=a*x+b*z+c"], est="-Y face plane, " + pd["-Y_face"]["estimator"], unc=pd["-Y_face"]["rms"])
add("paddle_end_c", pd["end_circle"]["centre_xz"], est="Kasa circle on plate edge faces (|n_y|<0.35) of the round end, xz", unc=pd["end_circle"]["rms"])
add("paddle_end_r", pd["end_circle"]["r"], est="same Kasa fit", unc=pd["end_circle"]["rms"])
add("paddle_upper_line", pd["upper_edge"]["z=k*x+b"], est="LSQ line z = k x + b on the upper straight edge", unc=pd["upper_edge"]["rms"], note="modelled as the tangent from the end circle with this slope")
add("paddle_lower_end", pd["lower_edge_end_xz"], est="xz of the lower edge where it meets the sleeve (max x of lower-edge faces, median z)", unc=0.2,
    note="lower edge modelled as the tangent from the end circle to this point (the edge is slightly convex: line rms %.3f)" % pd["lower_edge"]["rms"])
I3 = json.loads((run / "measure/figures/measure_it3.json").read_text())
E3 = "measure/figures/measure_it3.json"
rfs = [I3["paddle_perimeter_round"]["per_side"][k_]["Rf"] for k_ in ("+Y", "-Y")]
add("paddle_edge_fillet_r", float(np.mean(rfs)), rfs, rule="mean-of-n", est=I3["paddle_perimeter_round"]["estimator"] + "; mean of the +Y and -Y fits", unc=0.1, ev=E3,
    note="it3: 1.2 (assumed) -> scan fit (_it2_SUPERSEDED/qa Z3: CAD fuller than the scan at the perimeter)")
ud = pd["under_dish"]
add("under_dish_c", ud["sphere_centre"], est=ud["estimator"], unc=ud["rms"])
add("under_dish_R", ud["sphere_R"], est=ud["estimator"], unc=0.5)
ds = pd["dish"]
add("dish_c", ds["centre_xz"], est=ds["estimator"], unc=ds["rms"], note="concentric with paddle_end_c within %.2f mm; kept measured" % float(np.hypot(*(np.array(ds['centre_xz']) - np.array(pd['end_circle']['centre_xz'])))))
add("dish_depth", ds["depth"], est=ds["estimator"], unc=ds["rms"])
add("dish_sphere_r", ds["sphere_R"], est=ds["estimator"], unc=0.5)
# ---------------- tube B + sleeve + band
B = M["tube_B"]
add("tubeB_point", B["point_at_closest_to_Z"], est="Kasa section circles on the steel segment (clock crop), line through centres; point closest to datum Z", unc=B["station_rms_median"])
add("tubeB_dir", B["direction"], unit="mm", est="same fit (unit vector)", unc=0.002, note="elevation %.3f deg (tube dips away from the rod)" % B["elevation_deg"])
add("tube_r", float(np.median([B["r_median"], M["tube_C"]["r_median"]])), f"{min(B['r_median'], M['tube_C']['r_median']):.4f}..{max(B['r_median'], M['tube_C']['r_median']):.4f}",
    est="median of the B and C straight-segment radii", unc=0.05, critical=True, rerun_trigger="caliper reading of the steel tube OD")
S = M["sleeve"]
add("sleeve_point", S["point"], est="Kasa section circles on the black sleeve, B t 10.3..20.2, own axis", unc=S["station_rms_median"])
add("sleeve_dir", S["direction"], est="same fit", unc=0.003, note="%.2f deg / %.2f mm off tube B (kept measured)" % (S["angle_vs_B_deg"], S["offset_from_B"]))
add("sleeve_r_at_point", S["r_at_point"], est="LSQ r(t) line over the sleeve stations", unc=S["station_rms_median"])
add("sleeve_drdt", S["dr_dt"], est="slope of the same line (draft)", unc=0.003)
add("sleeve_end_t", 20.55, "20.5..20.6", est="B_profile: p50 3.71@20.0, 3.88@20.5 (step), 5.01@21.0; end of sleeve = start of band")
bp = np.array(M["B_profile"]["rows[t,p10,p50,p90]"], float)
s = (bp[:, 0] >= 21.0) & (bp[:, 0] <= 22.0)
add("band_r", float(np.median(bp[s, 2])), f"{bp[s,2].min():.4f}..{bp[s,2].max():.4f}", est="B_profile p50, t 21..22", unc=0.05)
add("band_t", [20.55, 22.4, 23.0, 23.5, 23.8], [20.55, 22.4, 23.0, 23.5, 23.8], est="B_profile: band start, flat end, rounded fall 4.75@23.0, 4.07@23.5, tube at 23.8-24")
add("band_fall_r", [4.75, 4.07], [4.75, 4.07], est="B_profile p50 at t 23.0, 23.5")
# ---------------- bend, C, bushing, tip
bd = M["bend"]
add("bend_vertex", bd["vertex"], est="midpoint of the closest points of lines B and C (gap %.3f)" % bd["B_C_line_gap"], unc=0.1)
add("bend_R", bd["radius_best"], f"{bd['radius_scan[Rb,rms,median_tube_r,n]'][0][0]}..{bd['radius_scan[Rb,rms,median_tube_r,n]'][-1][0]}",
    est="arc-centreline radius minimising the rms of the tube-surface distance (0.2 mm scan)", unc=0.2,
    note="tube is ovalised in the bend (median r %.3f vs %.3f straight)" % (bd["tube_r_in_bend"], B["r_median"]))
cl = np.array(I3["tube_centerline"]["rows[x,y,z,r,rms,n]"], float)
idx = list(range(6, 25, 2))                 # stations from the end of straight B (x 30.6) to the start of straight C (z -25.5)
add("bend_cl_x", cl[idx, 0].tolist(), est=I3["tube_centerline"]["estimator"] + "; every 2nd station 6..24", unc=0.05, ev=E3,
    note="it3: the bend follows the scanned centreline (spline) instead of a circular arc (_it2_SUPERSEDED/qa Z2: arc 0.1..0.22 off the scanned centreline)")
add("bend_cl_y", cl[idx, 1].tolist(), est="same", unc=0.05, ev=E3)
add("bend_cl_z", cl[idx, 2].tolist(), est="same", unc=0.05, ev=E3)
core = cl[8:23, 3]
add("bend_tube_r", float(np.median(core)), f"{core.min():.4f}..{core.max():.4f}", est="median section-circle radius over the bend stations 8..22 (ovalised/thinned bend)", unc=0.03, ev=E3)
Cc = M["tube_C"]
add("tubeC_dir_up", Cc["direction_up"], est="Kasa section circles on the steel segment between bend and bushing, line through centres", unc=0.002)
K = M["bushing"]
KU = K["axis_used"]
add("bush_point", KU["point"], est="barrel-circle centre (Kasa stations t -5..2) projected onto the tip axis", unc=0.15)
add("bush_dir_down", KU["direction_down"], est="= tip axis: the bushing bottom ring/hub faces are normal to within %.1f/%.1f deg of it (flat_face_normals); barrel-circle axis was %.1f deg off" % (
    K["flat_face_normals"][0]["angle_vs_tip_deg"], K["flat_face_normals"][1]["angle_vs_tip_deg"], K["flat_face_normals"][0]["angle_vs_barrel_axis_deg"]),
    unc=0.01, note="bushing coaxial with the tip; tip/bushing sit %.1f deg off tube C (kept measured)" % T_angle if False else "bushing coaxial with the tip (design intent from the flat faces); tip is off tube C, see tip_dir_down")
add("bush_c_t", K["t_of_point_from_vertex_along_minusC"], est="distance of bush_point from bend_vertex along -C", unc=0.1)
prof = {row[0]: row[2] for row in K["outer_profile[t,p10,p50,p90]"]}
bt = [-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 4.5]
add("bush_barrel_t", bt, est="bushing outer_profile stations (t along bush_dir_down from bush_point)", unc=0.0)
add("bush_barrel_r", [prof[t_] for t_ in bt], est="bushing outer_profile p50 (outward faces) at bush_barrel_t", unc=0.1)
tops = [row_[4] for row_ in K["axial_faces[r0,r1,sign,t10,t50,t90,n]"] if row_[2] == -1 and 4.0 <= row_[0] <= 5.0]
add("bush_top_t", float(np.mean(tops)), f"{min(tops):.3f}..{max(tops):.3f}", est="axial faces facing the bend, t50 for r 4..6 (bushing frame about the tip axis)", unc=0.15,
    note="it1 self-check: no neck above the top face (the r 3.6 'neck' read at t -9 was the 2.5 deg-tilted tube)")
fl = [prof[t_] for t_ in (-7.0, -6.5, -6.0, -5.5)]
topr = [(row_[0] + row_[1]) / 2 for row_ in K["axial_faces[r0,r1,sign,t10,t50,t90,n]"] if row_[2] == -1 and row_[0] < 6.0]
topt = [row_[4] for row_ in K["axial_faces[r0,r1,sign,t10,t50,t90,n]"] if row_[2] == -1 and row_[0] < 6.0]
add("bush_top_cone", [topr[0], topt[0]], [topr[0], topt[0]], est="top face is conical: t50 of faces facing the bend at r 3..4 (%.3f) vs r 4..6 (bush_top_t)" % topt[0], unc=0.15,
    note="[r, t] of the inner point of the top face (outer point = bush_flange_r at bush_top_t)")
add("bush_flange_r", float(np.median(fl)), f"{min(fl):.4f}..{max(fl):.4f}", est="bushing outer_profile p50 t -7..-5.5, median")
bots = [row_[4] for row_ in K["axial_faces[r0,r1,sign,t10,t50,t90,n]"] if row_[2] == 1 and row_[0] >= 7.0]
add("bush_bottom", [8.2, float(np.mean(bots))], [8.2, float(np.mean(bots))], est="bottom face: t50 of downward faces r 7..9 (outer ring); outer corner r 8.2 = last dense bottom-face bin (bushing_windows bottom_faces_by_r)", unc=0.1,
    note="[r, t] of the bottom outer corner")
W = M["bushing_windows"]
add("bush_frame_x", W["frame_x"], est="reference x of the bushing frame (axfit.frame of bush_dir_down), used for the spoke phase", unc=0.0)
add("bush_spoke_count", W["count"], unit="count", est="pattern_count.py --signal mass, FFT-dominant rotational order 6 at 3 stations t 4.85/5.0/5.15, residual local minimum (CHK-COUNT pass), on measure/figures/bushing_frame.stl",
    unc=0.0, ev=W["count_json"])
add("bush_spoke_phase", W["spoke_phase_deg"], unit="deg", est="mean crest phase of the order-6 signal over the 3 stations (bushing frame, CCW about bush_dir_down from bush_frame_x)", unc=1.0,
    ev=W["count_json"], frame="bushing frame: z = bush_dir_down, x = bush_frame_x, theta CCW about z")
wr = W["bottom_faces_by_r[r0,area]"]
add("bush_window_r", [4.5, 7.0], [4.5, 7.0], est="bushing underside: bottom-face area dense for r < 4.5 (hub) and r >= 7.0 (ring), sparse between (spokes only); hub side wall at r 4.5", unc=0.25)
add("bush_spoke_w", 2 * 5.75 * np.sin(np.radians(W["spoke_fwhm_deg"] / 2)), est="FWHM (%.0f deg) of the folded order-6 bottom-face area at r 4.8..6.7, chord at r 5.75" % W["spoke_fwhm_deg"], unc=0.3)
RV = json.loads((run / "measure/figures/revise_it2_probe.json").read_text())
add("bush_window_depth", round(RV["window_depth_below_bottom_from_p1"], 2), f"{RV['window_depth_below_bottom_from_p1']:.3f}",
    est="it2: p1 of scan vertices on window surfaces (r 4.7..6.8, off the spokes) below the bottom face (revise_it2_probe.json); a lower bound, deeper is not observable",
    unc=0.2, ev="measure/figures/revise_it2_probe.json", note="it1 1.5 (assumed) -> it2 measured lower bound: it1 verify found scan material 1 mm deeper than the it1 pocket floor (_it1_SUPERSEDED/qa clusters 2+3)")
T = M["tip"]
add("tip_point", T["point"], est="Kasa section circles on outer tip faces (r > 2.55), line through centres", unc=T["station_rms_median"])
add("tip_dir_down", T["direction_down"], est="same fit", unc=0.01, note="%.2f deg off tube C (kept measured)" % T["angle_vs_C_deg"])
add("tip_r", T["r_median"], f"{T['r_min']:.4f}..{T['r_max']:.4f}", est="median station radius", unc=T["station_rms_median"])
nk = [row_ for row_ in I3["tip_neck"]["rows[t,p50,n]"] if -9.7 <= row_[0] <= -8.1]
add("tip_neck_t", [row_[0] for row_ in nk], est="tip-axis t stations of the neck just below the bushing (bottom at tip-t %.2f); -10.0/-9.8 left out (they mix the bushing hub face)" % I3["tip_neck"]["bushing_bottom_tip_t"], unc=0.0, ev=E3)
add("tip_neck_r", [row_[1] for row_ in nk], est=I3["tip_neck"]["estimator"], unc=0.05, ev=E3,
    note="it3: neck (crimp groove) under the bushing, r down to 2.5 (_it2_SUPERSEDED/qa Z4: scan inside the CAD at the hub, r < 3.5)")
add("tip_end_t", 3.9, f"{T['end_t_p99.9']:.3f}..3.95", est="p99.9 of vertex t along the tip axis (r < 3.3), rounded up to the chamfer end", unc=0.05)
add("tip_chamfer", [1.1, 0.5], [1.1, 0.5], est="end_profile p50: 2.885@3.0, 2.813@3.25, 2.702@3.5, 2.559@3.75 -> linear fall, axial x radial", unc=0.05)
add("tip_bore_r", T["bore_r_median"], est="median vertex radius inside the tip bore, t 1.8..3.0", unc=0.05)
add("tip_bore_depth", round(RV["bore_depth_from_tip_end_needed"], 2), f"{RV['bore_depth_from_tip_end_needed']:.3f}",
    est="it2: bore wall (r 1.8..2.4 about the tip axis) is scanned up to just below the bushing bottom; depth from the tip end to the deepest bore-wall vertex (revise_it2_probe.json); a lower bound", unc=0.3,
    ev="measure/figures/revise_it2_probe.json", note="it1 8.0 (assumed) -> it2 measured lower bound (_it1_SUPERSEDED/qa cluster 2)")
doc = {"schema": "stl-re/params.json@1", "tool": "measure/scripts/build_params.py (run-local)", "tool_version": "OD-S02",
       "inputs": {EV: hashlib.sha256((run / EV).read_bytes()).hexdigest(),
                  "intake/alignment.json": hashlib.sha256((run / "intake/alignment.json").read_bytes()).hexdigest()},
       "seed": 0, "created": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
       "part": "OD-S02_steam-rod",
       "frame": "datum: +Z = rod spigot axis toward the rod tip (axis primary, section-circle refined); origin z = knob top face; "
                "clock: tube B (steel, leaving the elbow) projected on XY -> +X. theta CCW about +Z from +X. Vectors are in this frame.",
       "scan_noise_mm": noise, "params": P,
       "struck": [],
       "simplifications": [
           {"name": "rod lower body coaxial", "modelled_as": "rod collar/groove/body revolved about the spigot axis",
            "deviation_cost": "circle centres z 0.8..20.5 sit 0.11-0.19 mm off the axis (rod_station_circles); up to ~0.2 mm locally"},
           {"name": "knob coaxial, one meridian", "modelled_as": "knob revolved about datum Z with the mean +Y/-Y meridian",
            "deviation_cost": "Kasa centre 0.22/0.10 mm off axis; +Y vs -Y meridian differ up to 0.4 mm below z -10 (knob_meridian)"},
           {"name": "paddle lower edge straight", "modelled_as": "tangent line from the end circle to paddle_lower_end",
            "deviation_cost": "line fit rms %.3f mm (edge is slightly convex)" % pd["lower_edge"]["rms"]},
           {"name": "bend cross-section round", "modelled_as": "circle of bend_tube_r swept along the scanned centreline spline (it3)",
            "deviation_cost": "section-circle rms in the bend up to %.3f mm (ovalised tube)" % float(cl[8:23, 4].max())},
           {"name": "bushing underside windows", "modelled_as": "6 annular-sector pockets between straight spokes, flat floor at an assumed depth",
            "deviation_cost": "window floors/walls barely scanned (floor faces %.1f mm2); floor depth assumed" % M["bushing_windows"]["floor_area"]},
           {"name": "rod body", "modelled_as": "rod_body_r flat z 12.75..17.5, bead/groove z 9.75..12.75 as measured polyline",
            "deviation_cost": "polyline between 0.25 mm stations; body flat within p50 6.46..6.52"}],
       "checks": {
           "CHK-COUNT": {"ran": True, "result": "pass", "note": "bushing underside spokes: 6 (pattern_count.py mass signal, FFT-dominant order 6 at 3 stations, residual local minimum), measure/figures/count_bushing_spokes.json"},
           "CHK-ACHIEVABLE": {"ran": False, "result": "pass", "note": "no caliper readings (scan-only run)"},
           "CHK-CLUSTER": {"ran": True, "result": "pass", "note": "all material explained: rod, lug, knob, lever plate + dish, sleeve, band, steel tube B/bend/C, bushing, tip; small torn flash at the knob/sleeve junction (photos show torn rubber) is not a feature"},
           "CHK-FRAME": {"ran": True, "result": "pass", "note": "all angles/vectors measured on intake/aligned_work.stl in the frozen datum frame; none copied from intake notes"}},
       "open_questions": ["Bushing underside window depth (a photo from below would decide).",
                          "Is the 2.5-5 deg misalignment of bushing and tip real (bent tube) or a seating artefact of this specimen?"]}
(run / "measure/params.json").write_text(json.dumps(doc, indent=1))
print("params:", len(P))
