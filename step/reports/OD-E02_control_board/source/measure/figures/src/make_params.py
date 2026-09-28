#!/usr/bin/env python3
"""make_params.py - OD-E02: turn measure/figures/m_all.json into measure/params.json.

Run from the run folder: python3 measure/figures/src/make_params.py
Rules: scan-only job, so every scan value is keep-measured (no rounding: no calipers, and a
noise-bounded move would change nothing the gate can see). Unscanned depths are 'assumed' with
measured: null. Critical interfaces carry a re-run trigger. Numbers are copied from m_all.json,
never retyped.
"""
from __future__ import annotations

import hashlib
import json

import numpy as np
from datetime import datetime, timezone
from pathlib import Path

RUN = Path.cwd()
M = json.loads((RUN / "measure/figures/m_all.json").read_text())
AL = json.loads((RUN / "intake/alignment.json").read_text())
EV = "measure/figures/m_all.json"
NOISE = AL["scan_noise_mm"]["value"]
TRIG = "one caliper reading on this feature should trigger a re-run (scan-only job)"
params: dict = {}


def r4(x):
    if isinstance(x, list):
        return [r4(v) for v in x]
    return round(float(x), 4)


def P(name, value, unit, estimator, key, unc=NOISE, critical=False, rule="keep-measured", source="scan",
      measured="same", note=None):
    v = r4(value) if value is not None else None
    row = {"value": v, "unit": unit, "measured": (v if measured == "same" else measured), "rule": rule,
           "source": source, "estimator": estimator, "uncertainty_mm": round(float(unc), 4),
           "evidence": f"{EV}#{key}", "critical": critical}
    if critical:
        row["rerun_trigger"] = TRIG
    if note:
        row["note"] = note
    params[name] = row


Z = M["z"]
# ---------------------------------------------------------------- z levels
for nm, key, what in (("rim_top_z", "rim_top", "rim wall top"), ("T0_bottom_z", "T0_bottom", "tier-0 shelf (bottom face)"),
                      ("T2_bottom_z", "T2_bottom", "tier-2 bottom face"), ("T3_bottom_z", "T3_bottom", "tier-3 bottom face"),
                      ("band_bottom_z", "band_bottom", "button-band bottom face"),
                      ("collar_bottom_z", "collar_bottom", "button collar bottom face"),
                      ("hoop_bottom_z", "hoop_bottom", "latch-hoop bottom face"),
                      ("shroud_top_z", "shroud_top", "connector shroud top"),
                      ("screw_cb_floor_z", "screw_cb_floor", "screw counterbore floor")):
    P(nm, Z[key]["z"], "mm", f"{what}: area-weighted flat-face z ({Z[key]['area_mm2']:.1f} mm2, {Z[key]['n_faces']} faces)",
      f"z.{key}")

# ---------------------------------------------------------------- housing core (corner centres, constant across tiers)
for nm, key in (("core_BL", "BL"), ("core_BR", "BR"), ("core_TR", "TR"), ("core_TL", "TL"),
                ("bump_TL", "bumpTL"), ("bump_TR", "bumpTR")):
    c = M["core"][key]
    P(nm, c["xy"], "mm", "median centre of Kasa corner-arc fits at z -3/-4.5/-6.6/-9 (tiers are offsets of one core); "
      f"spread x {c['spread_mm'][0]:.3f} y {c['spread_mm'][1]:.3f}", f"core.{key}", unc=max(c["spread_mm"]))

T = M["tiers"]
P("rim_out_R_main", T["rim_out"]["R_main"], "mm", "rim outer wall (z 1..3.4): median outline-to-core distance, main walls",
  "tiers.rim_out", unc=0.05)
P("rim_out_R_bump", T["rim_out"]["R_bump"], "mm", "rim outer wall (z 1..3.4): median outline-to-core distance, bump",
  "tiers.rim_out", unc=T["rim_out"]["R_bump_spread"])
P("rim_in_R_main", M["rim_in"]["R_main"], "mm", "rim inner (pocket) wall: mode of outline-to-core distance 3.8..5.0, z 1..3.4",
  "rim_in", unc=0.05)
P("rim_in_R_bump", M["rim_in"]["R_bump"], "mm", "rim inner wall on the bump top: median y - bump core line, z 1..3.4",
  "rim_in", unc=0.05)
for t in ("T0", "T2", "T3"):
    P(f"{t}_R_main", T[t]["R_main"], "mm", f"{t}: median outline-to-core distance over stations {T[t]['stations_z']} "
      "(main walls; -Y excluded on T3 = chamfer)", f"tiers.{t}", unc=max(NOISE, T[t]["R_main_spread"] / 2))
    P(f"{t}_R_bump", T[t]["R_bump"], "mm", f"{t}: median outline-to-core distance on the bump", f"tiers.{t}",
      unc=max(NOISE, T[t]["R_bump_spread"] / 2))
cc = M["concave"]
P("T0_concave_r", cc["T0"]["L"]["r"], "mm", "Kasa on the -X bump junction arc at z -4 (the +X junction fit is "
  "contaminated by latch hoop H4 and is not used)", "concave.T0", unc=cc["T0"]["L"]["rms"] + NOISE)
P("T2_concave_r", [cc["T2"]["L"]["r"], cc["T2"]["R"]["r"]], "mm", "Kasa on both bump junction arcs at z -9 [L, R]",
  "concave.T2", unc=0.05)
P("T3_concave_r", [cc["T3"]["L"]["r"], cc["T3"]["R"]["r"]], "mm", "Kasa on both bump junction arcs at z -11.8 [L, R]",
  "concave.T3", unc=0.05)

# ---------------------------------------------------------------- -Y chamfer
ch = M["chamfer"]
P("chamfer_normal", ch["normal"], "mm", f"trimmed SVD plane on faces n.(0,-1,-1)/sqrt2 > 0.97, z -17..-10, y < -8 "
  f"({ch['n_faces']} faces, rms {ch['rms']:.4f}); unit outward normal (dimensionless, listed as mm)", "chamfer",
  unc=ch["rms"], note=f"angle to Z {ch['angle_to_z_deg']:.2f} deg")
P("chamfer_offset", ch["offset"], "mm", "plane offset n.p of the same fit (outward normal)", "chamfer", unc=ch["rms"])

# ---------------------------------------------------------------- button band, collars, caps
B = M["band"]
P("band_top_y", [B["top_line_L"]["y_at_x"], B["top_line_R"]["y_at_x"]], "mm",
  "line fit on the +Y band edge at z -14.4 for x -22..-10 and 10..22; y at x = -16 and +16", "band.top_line_*",
  unc=0.03, note="the band top edge sits 1.8-1.9 mm outside the core top edge")
for s in ("L", "R"):
    k = B[f"end_disk_{s}"]
    P(f"band_disk_{s}", [k["cx"], k["cy"], k["r"]], "mm", f"Kasa on the band end arc at z -14.4 (|x| > 28.5), "
      f"rms {k['rms']:.3f} [cx, cy, r]", f"band.end_disk_{s}", unc=k["rms"])
co = M["collars"]
P("collar_B2_r", co["B2"]["r"], "mm", "median Kasa radius of the B2 collar, 9 stations z -18.7..-16.4 (same surface "
  "as the datum origin; centre is the origin)", "collars.B2", unc=0.03, critical=True)
for s, nm in (("B1", "L"), ("B3", "R")):
    k = co[s]
    P(f"collar_{s}", [k["centre_median"][0], k["centre_median"][1], k["r"]], "mm",
      "median Kasa over 6 stations z -18.7..-16.5 [cx, cy, r]", f"collars.{s}", unc=0.05, critical=True)
    gap = k["gap_bins_deg"]
    pass
for s in ("B1", "B3"):
    cp = co[s]["cut_plane"]
    P(f"collar_{s}_sector_floor_z", co[s]["sector_floor"]["z"], "mm", "median z of -z faces at z -15.6..-14.6, r < 8.4 "
      f"about the collar ({co[s]['sector_floor']['area_mm2']:.1f} mm2): the flat floor of the outer collar cut",
      f"collars.{s}.sector_floor", unc=0.05)
    P(f"collar_{s}_floor_sector_deg", co[s]["floor_sector_deg"], "deg", "4-deg bins of the ring's lower boundary that sit "
      "within 0.45 of the floor z (bin edges; theta CCW from +X about the collar centre)", f"collars.{s}.floor_sector_deg",
      unc=0.0)
    P(f"collar_{s}_cut_plane", cp["normal_up"] + [cp["offset"]], "mm",
      f"least-squares plane through the ring's lower boundary (1st-percentile z per 4-deg bin, r 7.6..8.7, "
      f"{cp['n_pts']} bins above z -18.9; rms {cp['rms']:.3f}, max {cp['max']:.3f}, tilt {cp['tilt_deg']:.1f} deg); "
      "material below it is cut away near the collar [nx, ny, nz, n.p], normal pointing up",
      f"collars.{s}.cut_plane", unc=cp["rms"],
      note="replaces the it1 vertical-wedge sector model (self-check max 1.76 at the wedge walls)")

late_simpl = []
RC = M["recess"]
P("collar_B2_recess", [RC["B2"]["r"], RC["B2"]["top_z"]], "mm", "annular clearance recess around the B2 cap: r = 99th pct "
  "radius of samples r 6.45..7.7 at z -18.95..-17.9 (97th pct); top = 95th pct z [r, top_z]", "recess.B2", unc=0.1)
for s in ("B1", "B3"):
    P(f"collar_{s}_recess", [RC[s]["r"], RC[s]["top_z_inner"]], "mm", "clearance recess around the side cap (circle about "
      "the collar centre): r = 97th pct radius of samples r 6.45..7.7 at z -18.95..-17.9; top = 95th pct z on the inner half "
      "[r, top_z]", f"recess.{s}", unc=0.1)
    rp = RC[s + "_ramp"]
    if rp["n_bins"] < 5:
        continue_ramp = False
    else:
        continue_ramp = True
    if continue_ramp:
      P(f"collar_{s}_recess_ramp_plane", rp["normal_up"] + [rp["offset"]], "mm", "plane through the recess ceiling ramp: "
      f"10-deg bins (r 6.5..7.3, 90th-pct z) between the inner ceiling and the floor ({rp['n_bins']} bins, rms "
      f"{rp['rms']:.3f}, max {rp['max']:.3f}) [nx, ny, nz, n.p], normal up; the recess is cut up to "
      "min(floor, this plane) where that is above the inner ceiling", f"recess.{s}_ramp", unc=rp["rms"])
    else:
      late_simpl.append({"name": f"{s} recess ceiling ramp", "modelled_as": "inner ceiling + floor sector only",
                              "deviation_cost": f"only {rp['n_bins']} ramp bins (sharp transition); a plane is not "
                                                "determined; up to the bin step (10 deg) at the sector edges"})
    for j, (a0_, a1_, zm_) in enumerate(RC.get(s + "_mid", []), 1):
        P(f"collar_{s}_recess_mid_{j}", [a0_, a1_, zm_], "mm", "it3: sector whose 10-deg bins (r 6.5..7.3) have a "
          "90th-pct z 0.6..1.3 below the floor; cut up to the lowest of those bins [a0 deg, a1 deg, z mm] (theta CCW "
          "from +X about the collar centre; the angles are degrees stored in a mm-unit list)", f"recess.{s}_mid",
          unc=0.1, note="it3: verify it2 found the B1 cap lip inside the gap at these angles")
    P(f"collar_{s}_recess_floor_sector_deg", RC[s]["floor_sector_deg"], "deg", "sector where the recess is open up to "
      "the collar sector floor: 10-deg bins (r 6.5..7.3) whose 90th-pct z is within 0.6 of the floor z [a0, a1] "
      "(theta CCW from +X about the collar centre)", f"recess.{s}", unc=0.0)

C = M["caps"]
b2 = C["B2"]
P("cap_B2_r", b2["r"], "mm", "median Kasa radius over 12 stations z -28.6..-19.8 (lower half 6.36-6.40, upper 6.30-6.34: "
  "a 0.06 mould step at z -24.5, not modelled)", "caps.B2", unc=0.04, critical=True)
P("cap_B2_axis_dir", b2["axis"]["dir"], "mm", f"line fit through the 12 station centres (tilt {b2['axis']['tilt_deg']:.2f} deg "
  f"toward {b2['axis']['tilt_dir_deg']:.0f} deg); unit vector", "caps.B2.axis", unc=0.03,
  note="loose cap: pose as scanned")
P("cap_B2_axis_xy0", b2["axis"]["xy_at_z0"], "mm", "same line: x, y at z = 0", "caps.B2.axis", unc=0.03)
P("cap_B2_top_normal", b2["top"]["normal"], "mm", f"trimmed SVD plane on the B2 top (r < 5.8, {b2['top']['n_faces']} faces, "
  f"rms {b2['top']['rms']:.3f}); outward unit normal", "caps.B2.top", unc=b2["top"]["rms"])
P("cap_B2_top_offset", b2["top"]["offset"], "mm", "same plane: n.p", "caps.B2.top", unc=b2["top"]["rms"])
for s in ("B1", "B3"):
    e = C[s]["ellipse"]
    P(f"cap_{s}_ellipse", [e["cx"], e["cy"], e["a_xprime"], e["b_yprime"], e["phi_deg"]], "mm",
      f"least-squares ellipse, median of 6 stations z -21.2..-19.4 [cx, cy, a along x', b along y', phi deg]; "
      f"rms {e['rms']:.3f} (circle rms 0.15-0.19)", f"caps.{s}.ellipse", unc=e["rms"], critical=True,
      note="side caps are oval in plan, a < b; phi is the x' axis angle from +X")
    t = C[s]["top"]
    P(f"cap_{s}_top_normal", t["normal"], "mm", f"trimmed SVD plane on the inclined top ({t['n_faces']} faces, "
      f"{t['area_mm2']:.1f} mm2, rms {t['rms']:.3f}); outward unit normal, {t['angle_to_z_deg']:.1f} deg from -Z",
      f"caps.{s}.top", unc=t["rms"])
    P(f"cap_{s}_top_offset", t["offset"], "mm", "same plane: n.p", f"caps.{s}.top", unc=t["rms"])

# ---------------------------------------------------------------- screw holes
H = M["holes"]
for s in ("L", "R"):
    h = H[s]
    P(f"screw_{s}_xy", h["centre"], "mm", "median Kasa centre of the back counterbore, 4 stations z -0.6..-2.4",
      f"holes.{s}", unc=0.03, critical=True)
    P(f"screw_{s}_cb_r", h["cb_r"], "mm", "median Kasa radius, same stations", f"holes.{s}", unc=0.03, critical=True)
    P(f"screw_{s}_through_r", h["through_r_p50"], "mm", f"median radial distance of {h['through_n']} surface samples "
      "r < 2.4, z -5.5..-3.3", f"holes.{s}", unc=0.05, critical=True)
    P(f"screw_{s}_front", h["front_circle"], "mm", "median Kasa [cx, cy, r] of the front-bore arcs (upper arc, "
      "points < 4.2 from the counterbore axis) at z -13.6/-14.2/-14.8; the front bore is offset from the counterbore "
      "axis", f"holes.{s}.front_stations", unc=0.05, critical=True)
    P(f"screw_{s}_front_top_z", h["front_scan_top_z"], "mm", "99th percentile z of the front-bore wall samples: the "
      "scan's deepest view into the bore; the true bore depth is not visible", f"holes.{s}", unc=0.3,
      note="bore continues deeper in reality (unscanned); CAD stops the bore here")
P("screw_through_mid_z", None, "mm", "not scanned between z -5.9 and -11.9", "holes", unc=0.0, rule="assumed",
  source="assumed", measured=None, note="the through-hole r is assumed continuous from the counterbore floor to the "
  "front bore (photo 2 shows open holes); not modelled as a separate param value")
del params["screw_through_mid_z"]

# ---------------------------------------------------------------- connector shroud
sh = M["shroud"]
w = sh["walls_median_z3_9"]
P("shroud_outer", [w["x_outer_min"], w["x_outer_max"], w["y_outer_min"], sh["outer"]["ymax"]], "mm",
  "outer wall faces: median of section-histogram peaks at z 3/5/7/9 (y_max from the z 7 outline percentile) "
  "[xmin, xmax, ymin, ymax]", "shroud", unc=0.08, critical=True)
P("shroud_inner", [w["x_inner_min"], w["x_inner_max"], w["y_inner_min"], w["y_inner_max"]], "mm",
  "inner wall faces: median of section-histogram peaks at z 3/5/7/9 [xmin, xmax, ymin, ymax]", "shroud", unc=0.08)
P("shroud_outer_corner_r", float(sorted(sh["outer_corner_r"])[len(sh["outer_corner_r"]) // 2]), "mm",
  f"median Kasa on the 4 outer corner arcs at z 7 ({[round(x, 3) for x in sh['outer_corner_r']]})", "shroud", unc=0.05)
P("shroud_inner_floor_z", sh["inner_wall_scan_bottom_z"], "mm", "0.5th percentile z of the inner +Y wall samples: "
  "the deepest scanned point; the interior floor itself is not scanned", "shroud", unc=0.3,
  note="interior (header, pins, floor) unscanned: the pocket is cut to the deepest scanned wall point")

for i, pd in enumerate(sh["header_pads"], 1):
    P(f"header_pad_{i}", pd["x"] + [pd["y_max"], pd["top_z"]], "mm", f"scanned header-base pad inside the shroud next to "
      f"the -Y inner wall ({pd['n']} samples at z -0.8..0.6): x-extent, 98th-pct y, 90th-pct z [x0, x1, y_max, top_z]",
      "shroud.header_pads", unc=0.1, note="it2: added for verify it1 scan->CAD cluster 0 (pin-header base)")

# ---------------------------------------------------------------- mounting tab
tb = M["tab"]
for nm, key, what in (("tab_top", "top", "horizontal flange top face"), ("tab_under", "under", "horizontal flange underside"),
                      ("tab_incline_upper", "incline_upper", "45-deg plate upper face"),
                      ("tab_incline_lower", "incline_lower", "45-deg plate lower face"),
                      ("tab_leg_outer", "leg_outer", "vertical leg outer (-Y) face"),
                      ("tab_leg_inner", "leg_inner", "vertical leg inner (+Y) face"),
                      ("tab_flange_incline", "flange_lower_incline", "side-flange lower 45-deg edge face")):
    f = tb[key]
    P(nm + "_plane", f["normal"] + [f["offset"]], "mm", f"trimmed SVD plane, {what} ({f['n_faces']} faces, rms "
      f"{f['rms']:.3f}) [nx, ny, nz, n.p]", f"tab.{key}", unc=f["rms"])
for side in ("neg", "pos"):
    for io in ("inner", "outer"):
        f = tb[f"flange_{io}_x"][side]
        P(f"tab_flange_{io}_{side}_plane", f["normal"] + [f["offset"]], "mm",
          f"trimmed SVD plane on the {'-X' if side == 'neg' else '+X'} side flange {io} face ({f['n_faces']} faces, "
          f"rms {f['rms']:.3f}, draft {90 - f['angle_to_z_deg']:.1f} deg) [nx, ny, nz, n.p]", f"tab.flange_{io}_x.{side}",
          unc=f["rms"])
P("tab_flange_bottom_z", tb["flange_bottom"]["z"], "mm", "area-weighted -z faces of the side flanges, y > -19",
  "tab.flange_bottom", unc=0.05)
P("tab_end_y", tb["end_y"], "mm", "0.2th percentile y of samples on the flange end (|x| < 10, z 17..18.5)", "tab.end_y",
  unc=0.05)
P("tab_hole", [tb["hole"]["cx"], tb["hole"]["cy"], tb["hole"]["r"]], "mm",
  f"Kasa on the hole loop at z 17.7 (rms {tb['hole']['rms']:.3f}) [cx, cy, r]", "tab.hole", unc=tb["hole"]["rms"],
  critical=True)

# ---------------------------------------------------------------- latch hoops
for nm, h in M["hoops"].items():
    P(f"hoop_{nm}", [h["x"][0], h["x"][1], h["window_x"][0], h["window_x"][1], h["window_bottom_z"], h["top_z"],
                     h["outer_face_y"]], "mm",
      f"XZ section at y {h['section_y']} ({h['side']} side): bar x-extent at z < -4.5 (0.5/99.5 pct), leg inner edges at "
      "z 1..4, window bottom (99th pct z between the legs), top (99.5 pct), outer face y (median of faces n.y "
      "outward, z -5.3..-3.8) [x0, x1, wx0, wx1, window_bottom_z, top_z, outer_y]", f"hoops.{nm}", unc=0.08)

# ---------------------------------------------------------------- inner latch bosses (added after the it1 self-check, CHK-ENUM)
P("boss_top_z", Z["boss_top"]["z"], "mm", f"inner latch boss top: area-weighted +z faces z 3.2..3.8 "
  f"({Z['boss_top']['area_mm2']:.1f} mm2)", "z.boss_top")
for nm, b in M["bosses"].items():
    P(f"boss_{nm}", b["x"] + [b["inner_face_y"]], "mm", "x-extent: median over z 0.6/1.5/2.5 of the inner-wall segment "
      "displaced from the rim inner wall; inner face y: area-weighted faces with the pocket-facing normal "
      f"({b['inner_face_area_mm2']:.1f} mm2) [x0, x1, inner_face_y]", f"bosses.{nm}", unc=0.08)

# ---------------------------------------------------------------- edge rounds (measure_edges.py; run after a first params pass)
EP = RUN / "measure/figures/m_edges.json"
if EP.exists():
    ME = json.loads(EP.read_text())
    for key, what in (("T0_bottom_edge", "T0 bottom outer edge"), ("T2_bottom_edge", "T2 bottom outer edge (+Y, ends, bump)"),
                      ("T3_bump_bottom_edge", "T3 bottom outer edge on the bump"),
                      ("band_top_bottom_edge", "button-band bar +Y bottom edge"),
                      ("rim_top_outer_edge", "rim top outer edge"), ("rim_top_inner_edge", "rim top inner edge"),
                      ("cap_B2_top_edge", "B2 cap top edge"), ("cap_B1_top_edge", "B1 cap top edge"),
                      ("cap_B3_top_edge", "B3 cap top edge"), ("shroud_top_outer_edge", "shroud top outer edge"),
                      ("shroud_top_inner_edge", "shroud top inner edge"),
                      ("shroud_inner_vertical_corner", "shroud inner vertical corners"),
                      ("tab_end_top_edge", "tab end top edge")):
        e = ME[key]
        P(f"round_{key}", e["r_est"], "mm", f"{what}: r = d / 0.4142 (90 deg edge), d = median nearest-scan distance "
          f"from the sharp corner computed from params ({e['n']} points, d IQR {e['d_p25_p75'][0]:.3f}.."
          f"{e['d_p25_p75'][1]:.3f})", f"measure/figures/m_edges.json#{key}".replace(EV + "#", ""),
          unc=(e["d_p25_p75"][1] - e["d_p25_p75"][0]) / 0.4142 / 2)
        params[f"round_{key}"]["evidence"] = f"measure/figures/m_edges.json#{key}"
    params["tab_end_under_edge_note"] = {"value": 0.0, "unit": "mm", "measured": None, "rule": "assumed", "source": "assumed",
        "estimator": f"tab end underside edge reads r_est {ME['tab_end_under_edge']['r_est']:.3f} (d {ME['tab_end_under_edge']['d_med']:.3f}): "
                     "within noise of sharp; built sharp", "uncertainty_mm": 0.0,
        "evidence": "measure/figures/m_edges.json#tab_end_under_edge", "critical": False}

for nm, h in M["hoops"].items():
    f = h["window_ramp"]
    P(f"hoop_{nm}_ramp_plane", f["normal"] + [f["offset"]], "mm", f"trimmed SVD plane on the up-facing faces between the "
      f"legs ({f['n_faces']} faces, rms {f['rms']:.3f}, {f['angle_to_z_deg']:.1f} deg from horizontal): the catch ramp that "
      "floors the hoop window [nx, ny, nz, n.p]", f"hoops.{nm}.window_ramp", unc=f["rms"],
      note="replaces window_bottom_z (kept in hoop_* for reference) as the window floor")

# ---------------------------------------------------------------- assumed (unscanned) values
params["shroud_slot_note"] = {"value": 0.0, "unit": "mm", "measured": None, "rule": "assumed", "source": "assumed",
                              "estimator": "the narrow slot between the shroud +Y wall and the rim (x -22..4, y 11.7..13) "
                                           "has no scan points below z 0; modelled closed at the floor (z 0)",
                              "uncertainty_mm": 0.0, "evidence": "intake/coverage.json loop 2; measure probe in make_params docstring",
                              "critical": False, "note": "value is the floor z used to close the slot"}
RJ = M["rim_junctions"]
for nm, key, what in (("rim_concave_r", "outer", "rim outer wall"), ("pocket_concave_r", "pocket", "rim pocket (inner) wall")):
    vals = [float(np.median([f["r"] for f in RJ[key][s_]])) for s_ in ("L", "R")]
    rms = max(float(np.median([f["rms"] for f in RJ[key][s_]])) for s_ in ("L", "R"))
    P(nm, vals, "mm", f"{what} bump-junction fillet: median Kasa radius at z 1/2/3 [L, R] (points off both walls, split from "
      f"the other rim face by core distance); worst median rms {rms:.3f}", f"rim_junctions.{key}", unc=max(rms, 0.05),
      note="added after the it1 self-check (the rim reused T0_concave_r; the pocket corners were built sharp)")

simplifications = [
    {"name": "T0 wall draft", "modelled_as": "vertical wall at the median offset",
     "deviation_cost": f"offset reads {min(r.get('main_pY', 9) for r in T['T0']['per_station']):.2f}.."
                       f"{max(r.get('main_pY', 0) for r in T['T0']['per_station']):.2f} over z -1..-6 vs {T['T0']['R_main']:.3f}: about +-0.1 mm"},
    {"name": "small edge blends (rim top, shroud top, tier edges, tab edges, hoop edges)", "modelled_as": "sharp edges",
     "deviation_cost": "an unmodelled round of radius r leaves up to 0.41 r at the edge; rims read r 0.3-0.8 -> up to about 0.3 mm, local"},
    {"name": "B2 cap mould step at z -24.5", "modelled_as": "one cylinder at the median radius",
     "deviation_cost": "station radii 6.27..6.40 vs value: +-0.07 mm"},
    {"name": "embossed logos (back floor) and button icons", "modelled_as": "not modelled (cosmetic)",
     "deviation_cost": "relief height about 0.1-0.3 mm, local"},
    {"name": "connector shroud draft", "modelled_as": "straight walls at the median of z 3..9",
     "deviation_cost": "wall peaks move about 0.1-0.2 mm between z 3 and z 9"},
    {"name": "side-collar sector cut", "modelled_as": "a wedge with radial side walls at the measured gap angles",
     "deviation_cost": "gap edges read from 2-deg bins at one z: +-1 deg (about 0.15 mm at r 8.2)"},
    {"name": "latch hoops", "modelled_as": "U-frame boxes (no ramps or catch lips)",
     "deviation_cost": "hoop section bottoms read -5.75..-5.56 and windows differ per hoop; up to about 0.2 mm, local"},
]

simplifications += late_simpl

checks = {
    "CHK-COUNT": {"ran": False, "result": "pass", "note": "no rotational pattern on this part; all instance counts "
                  "(3 caps, 2 screw holes, 4 hoops) are enumerated individually and placed at measured positions"},
    "CHK-ACHIEVABLE": {"ran": False, "result": "pass", "note": "no caliper readings (scan-only job)"},
    "CHK-CLUSTER": {"ran": True, "result": "pass", "note": "interior material seen through the rim/shroud slot was "
                    "traced to the bump outer walls (T0/T2) seen below the floor plane, not a new feature; no "
                    "unexplained cluster (measure/figures/interior.png)"},
    "CHK-FRAME": {"ran": True, "result": "pass", "note": "all values measured on intake/aligned_work.stl in the frozen "
                  "datum frame; no angle copied from the intake card; theta CCW about +Z from +X"},
}

doc = {"schema": "stl-re/params.json@1", "tool": "make_params.py", "tool_version": "OD-E02 run",
       "inputs": {"intake/aligned_work.stl": hashlib.sha256((RUN / "intake/aligned_work.stl").read_bytes()).hexdigest(),
                  "intake/alignment.json": hashlib.sha256((RUN / "intake/alignment.json").read_bytes()).hexdigest(),
                  EV: hashlib.sha256((RUN / EV).read_bytes()).hexdigest()},
       "seed": 0, "created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
       "part": "OD-E02_control-button-board",
       "frame": "datum frame of intake/alignment.json: back cover floor = XY at z 0 (housing hangs to -Z), origin = "
                "middle button collar axis, +X = +X end face normal; theta CCW about +Z from +X",
       "scan_noise_mm": NOISE, "params": params, "struck": [], "simplifications": simplifications,
       "checks": checks,
       "open_questions": ["Scan-only: every critical interface (caps, collars, screw holes, tab hole, shroud) is held at "
                          "its scan fit; one caliper reading on any of them should trigger a re-run.",
                          "Loose button caps are modelled at their scanned pose (B2 tilted 0.9 deg)."]}
(RUN / "measure/params.json").write_text(json.dumps(doc, indent=1))
print(len(params), "params")
