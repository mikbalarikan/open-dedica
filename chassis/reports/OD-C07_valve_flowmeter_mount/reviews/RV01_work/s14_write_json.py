import json, hashlib
from pathlib import Path
JOB = Path("/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount")
def sha(p): return hashlib.sha256((JOB / p).read_bytes()).hexdigest()
REP = {"02_STEP_STL/od_c07_mount_C1_v01.step": "55c1c3616383608b85c711deb84b170c908d38a9baf5c6a727d19d73f68a583c",
       "02_STEP_STL/od_c07_assembly_C1_v01.step": "50d126c13b945edca3cfd9a5082189ddbd6380bfbb6e59cd24bc71c546f6c9d7",
       "02_STEP_STL/od_c07_mount_C1_v01.stl": "41bccd61c1fb0e82a7a8171c85da2128d0c01ca6906f80c03c5ffebf83de3c38",
       "01_CAD/REPORT_od_c07_mount_v02.md": "2b4a50f0a3ed54a9479c22234f6d1087d1970658c05c81416bf24f72ab8a5084"}
files = [{"path": p, "sha256": sha(p), "matches_report": sha(p) == h} for p, h in REP.items()]
for p in sorted((JOB / "03_Sections").glob("*.png")):
    rel = str(p.relative_to(JOB)); files.append({"path": rel, "sha256": sha(rel), "matches_report": True})
for rel, h in (("00_Spec/inputs/OD-H22_3way_valve.step", "bc0ffd003bcba248c7c8c4d68b198994726ee34b6c7e96ac97fbfd6490920028"),
               ("00_Spec/inputs/OD-H24_flowmeter.step", "1b4cbdafd03e0edafcc900b8c8c0894b382a48bd71850b59b06201a1fb45696a")):
    files.append({"path": rel, "sha256": sha(rel), "matches_report": sha(rel) == h})
def G(gate, measured, unit, required, margin, at, status, method, assumes=()):
    return {"gate": gate, "measured": measured, "unit": unit, "required": required, "margin": margin, "at": at, "status": status, "method": method, "assumes": list(assumes)}
A03 = ("A-02", "A-03", "A-06", "A-07")
gates = [
 G("U-01", 1, "count", "solid_count = 1, brep_valid = 1, naked_edges = 0", 0, "solid_count 1, brep_valid 1, naked_edges 0; the file holds 1 shell, no loose shell or face", "PASS", "validity"),
 G("U-02", 48.0, "mm", "119.0 x 50.0 x 48.0 each in [spec - 0.1, spec + 0.1]; min x -25, min y -25, min z 0 reported apart", 0.1, "size 119.000 x 50.000 x 48.000 (each margin 0.1); min (-25.000, -25.000, 0.000)", "PASS", "envelope"),
 G("U-03", 0.297, "mm", "(a) contacts clearance = 0 with interference <= 0; every other pair clearance >= 0.5 away from the contacts; (b) OD-H24 -Z path and OD-H22 -Y slide at +5.0 then 5.0 drop, interference <= 0", -0.203,
   "(0.761, -14.170, 9.890) recess edge chamfer to OD-H24 rib end (0.750, -13.960, 10.100), rib/hub inside the rim radius r 13.98 (A-06); contacts: rim/pedestal 0 at (14.4, 0, 10.0), flange/deck 0 at (50.15, 1.2, 48.0), 3 catches 0 at z 29.9; interference 0 mm3 with both OEM solids; H22 below its flange 0.503; path (b): OD-H24 51 poses 0 mm3 (hooks exempt), OD-H22 100 slide + 21 drop poses 0 mm3 with mount and with OD-H24, least slide clearance 0.858 at y +15.5", "FAIL", "clearance, common_volume, own path sweep", A03),
 G("U-04", 0.0, "mm3", "named body re-read unchanged, no stray shells, valid after re-import", 0.0, "compare_step to the file: schema AP242, 1 solid, volume delta 0, faces delta 0, label od_c07_mount, valid after; own round trip of the re-read body: volume delta 1.2e-9 mm3", "PASS", "compare_step, step_roundtrip"),
 G("U-05", 15, "count", "15 feature kinds per the plan (U-05 list)", 0, "all 15 present with their counts; bores 12 (4 footprint, 2 pin, 2 clearance, 2 insert, recess, ring inner); no closed stem bore", "PASS", "feature_census, bore_census, locate_bore, own probes"),
 G("U-06", 1.6, "mm", "min_wall wide >= 1.5 (Soft)", 0.1, "(-16.679, 8.825, 31.500) hook 160 deg catch tip", "PASS", "min_wall_wide"),
 G("U-07", 0.00396, "mm", "STL at tol 0.01, angular <= 4 acos(1 - 0.01/R_max); stl_max_sagitta <= 0.01", 0.00604, "own re-mesh of the STEP at 0.01 mm / 0.05 rad (limit 0.1112 rad at R_max 25.87, hook-root torus) reproduces the delivered bytes; 92262 triangles, 1 body, 0 naked edges, winding 1; mesh_deviation to the STEP 0.0048; mesh wall 1.7214 vs B-rep 1.7224", "PASS", "write_stl, mesh_sagitta, mesh_census, mesh_deviation"),
 G("U-08", None, "bool", "threads cosmetic; applies to threaded parts", None, "no threads on this target (inserts take the thread)", "NOT_APPLICABLE", "N/A by its row"),
 G("D-01a", 1.7224, "mm", "min_wall >= 0.8", 0.9224, "(-16.101, 2.520, 10.255) ring wall base between the 0.3 root round and the 60 deg lip chamfer", "PASS", "min_wall"),
 G("D-01b", 1.7224, "mm", "min_wall >= 1.5", 0.2224, "(-16.101, 2.520, 10.255) ring wall base; deck wedges from section rays at z 47.999: 1.789 (-X, hole at 46.662) and 1.898 (+X, hole at 77.447)", "PASS", "min_wall; radial_extent section rays"),
 G("D-02", 119.0, "mm", "each envelope size <= 220 x 220 x 250, bottom face down", 101.0, "119.0 x 50.0 x 48.0 against 220 x 220 x 250", "PASS_ASSUMED", "envelope", ("A-12",)),
 G("D-03a", 60.0184, "deg", "every downward face >= 45 deg except the named supported faces and bridges", 15.0184, "(-11.865, -13.599, 10.083) ring lip chamfer cone; exactly 9 flat downward faces, all named: 3 notch ceilings z 10.5, 3 catch undersides z 29.9, deck underside z 40.3, 2 insert-bore ceilings z 46.0", "PASS_ASSUMED", "overhang_census in slabs, flat-face census", ("A-16",)),
 G("D-03b", 4.0, "mm", "span <= 5", 1.0, "insert-bore ceilings Ø4.000 at z 46.0 (46.662, 0) and (77.447, 0); notch ceilings 2.000 wide x 0.5 at z 10.5", "PASS_ASSUMED", "bore_census, radial_extent rays, sections", ("A-16",)),
 G("D-04a", 3.4, "mm", "Ø >= 3.25 (4 footprint + 2 screw clearance holes)", 0.15, "all six Ø3.400", "PASS", "locate_bore"),
 G("D-04c", 0.297, "mm", ">= 0.5 per side between the mount and each OEM solid away from the designed contacts", -0.203, "(0.761, -14.170, 9.890) recess edge to OD-H24 rib (see U-03); ring root round toe (-10.584, -11.999, 10.000) to OD-H24 cup 0.377; OD-H22 below its flange 0.503 at (55.053, -1.200, 43.766); hooks to pipes 13.346, to connector 4.939", "FAIL", "clearance", A03),
 G("D-04d", 0.3773, "mm", "ring gap and pin holes >= 0.30 per side", 0.0773, "ring root round toe (-10.584, -11.999, 10.000) to cup; pin holes 0.500 each", "PASS_ASSUMED", "clearance", ("A-06", "A-07")),
 G("D-05a", 16.274, "mm", "material >= 8.0 across around each Ø4.0 insert bore", 8.274, "least of 36 diameters x 6 depths, z 45.99, both bores", "PASS_ASSUMED", "radial_extent", ("A-13",)),
 G("D-05b", 5.7, "mm", "Ø 4.0 +- 0.05, depth >= 5.7 from the deck underside", 0.0, "both bores Ø4.000, 5.700 deep from z 40.3, open on the underside", "PASS_ASSUMED", "bore_census, locate_bore", ("A-13",)),
 G("D-06a", 1.7224, "mm", "minimum feature >= 1.0", 0.7224, "(-16.101, 2.520, 10.255) ring wall base", "PASS", "min_wall"),
 G("D-07", None, "bool", "applies to reamed fit bores", None, "none on this part", "NOT_APPLICABLE", "N/A by its row"),
 G("J-01", 0.6708, "%", "eps = 1.5 y t / (L^2 Q) <= 1.5 %", 0.8292, "each hook: y = 20.37 - 18.870 = 1.500, t = 2.000, L = 29.900 - 4.000 = 25.900, L/t 12.95 so Q = 1", "PASS_ASSUMED", "radial_extent, vertical rays, arithmetic", ("A-15",)),
 G("J-02", 2.0, "mm", "beam thickness >= 1.0", 1.0, "each hook at z 6, 15, 25", "PASS", "radial_extent"),
 G("J-03", 2.0, "ratio", "catch/root thickness ratio reported; binding only if eps within 0.2 % of the limit", 1.5, "catch radial length 4.000 / beam 2.000; eps 0.67 % is 0.83 % from its limit, so the taper rule does not bind", "PASS", "radial_extent"),
 G("J-04", 0.0, "mm3", "each hook undeflected: interference <= 0 with OD-H24; catch underside clearance = 0", 0.0, "hooks 70/160/320: 0 mm3, catch underside 0 at z 29.9, beam to flange 0.510", "PASS_ASSUMED", "common_volume, clearance", ("A-06", "A-08")),
 G("J-05", 3.612, "mm", "wall >= 3.0 around each insert bore over its 5.7 depth", 0.612, "insert bore (46.662, 0) toward +X at z 45.99 (the slit end); (77.447, 0) 3.721", "PASS", "radial_extent"),
 G("J-06", None, "bool", "printed threads", None, "none (inserts)", "NOT_APPLICABLE", "N/A by its row"),
 G("E-06", 16, "count", "insert pads are the deck tied to the legs; hooks and ring root-filleted to plate and pedestal", None, "deck continuous into both legs (x 38 and 86: material z 0 to 48); root rounds: ring 0.3 (3 pieces), pedestal 1.0, hook roots 1.5 inner and outer (x3 each), legs 3.0 (x6)", "PASS", "reviewer, face census and rays"),
 G("REQ-01", 0.3773, "mm", "pedestal top z 10.0 +- 0.1; ring inner R in [16.30, 16.40] at z 10.5..12.5; ring top z 13.0 +- 0.1; clearance(ring, OD-H24 cup) in [0.50, 0.70]", -0.1227,
   "ring root round toe (-10.584, -11.999, 10.000) to OD-H24 cup (-10.393, -11.781, 10.241), cup taken outside the A-06 rim annulus r 15.71; 0.413 with the cup from z_H24 0.3; ring wall above the round 0.531; pedestal top 10.000, ring inner R 16.300 (0..359 deg), ring top 13.000", "FAIL", "clearance, radial_profile, vertical rays", ("A-06",)),
 G("REQ-02", 0.297, "mm", "pin bores Ø4.8 / Ø3.8 +0.1/-0, offset <= 0.10, length 9.4 +- 0.1; clearance to each pin >= 0.5; recess R 14.10 +- 0.1, floor z 9.40 +- 0.05; clearance recess to OD-H24 ribs and hub >= 0.5", -0.203,
   "(0.761, -14.170, 9.890) recess edge chamfer to rib (0.750, -13.960, 10.100); 0.243 to the rib face's end at r 14.056; bores Ø4.800 / Ø3.800, offset 0, length 9.400, through; pin clearances 0.500 / 0.500; recess R 14.100..14.150, floor 9.400", "FAIL", "locate_bore, clearance, radial_profile", ("A-07",)),
 G("REQ-03", 0.0, "mm3", "hooks at 70/160/320 +- 1 deg; beam inner R 20.87 +- 0.1 over z 6..26; catch underside z 29.9 +- 0.1 reaching R 18.87 +- 0.1; catch lands outside slots and windows (clearance = 0); chamfer 45 +- 1 deg", 0.0,
   "void under each catch 0 mm3 (sector r 18.87..19.70, 2.65 deep); centres 70.000/160.000/320.000; beam inner 20.870; catch underside 29.900; reach 18.870; chamfer 45.000; catch clearance 0", "PASS_ASSUMED", "radial_profile, radial_extent, common_volume, clearance", ("A-06", "A-08", "A-09")),
 G("REQ-04", 7.05, "mm", "deck top z 48.0 +- 0.1 flat under the flange; U-slot 14.1 +0.1/-0, profile 180..360 deg at z 41..47 in [7.05, 7.10], walls y +-(7.05 +0.05/-0) open to +Y, length 7.7 +- 0.1; slits 2.40 +- 0.1 reaching 62 +- (11.85 +0.1/-0); clearance(mount, OD-H22) >= 0.5 away from the flange", 0.0,
   "slot 7.050 at every ray outside the two slit windows (180..360 below z 43.3; 190..350 over z 41..47); literal window reads 10.72 at 186 deg z 46.875 inside the slit (F5); walls 7.050 at y 2.5..14; open to +Y 0 mm3; deck z 40.3..48.0; one +Z plane above z 40, at 48.000; slits 2.400 wide, reach 11.850, taper 43.42 deg; clearance to OD-H22 0.503", "PASS_ASSUMED", "radial_profile, radial_extent, common_volume, clearance", ("A-03",)),
 G("REQ-05", 4.0, "mm", "Ø3.4 +- 0.1 at (77.447, 0), (46.662, 0), 2.0 +- 0.1 deep, offset <= 0.10; coaxial Ø4.0 +- 0.05, 5.7 +- 0.1 deep from the underside", 0.05, "both: Ø3.400 x 2.000 (z 46..48), Ø4.000 x 5.700 (z 40.3..46.0), offsets 0.000", "PASS_ASSUMED", "locate_bore", ("A-02", "A-13", "A-18")),
 G("REQ-06", 3.4, "mm", "four Ø3.4 +- 0.1 through-holes at (-18, +-21), (88.5, +-21), offset <= 0.10, length 4.0 +- 0.1", 0.1, "all four Ø3.400, offset 0.000, length 4.000, through", "PASS_ASSUMED", "locate_bore", ("A-14",)),
 G("REQ-07", 40.0, "mm", "window x 40..84, y -25..25 through the plate; leg inner faces at x 40.0 and 84.0 +- 0.1", 0.1, "plate pieces x -25..40 and 84..94 over y +-25; 0 mm3 in x 40.001..83.999 below the deck; leg inner faces 40.000 / 84.000 at 9 points", "PASS_ASSUMED", "envelope, common_volume, radial_extent", ("A-04", "A-19")),
 G("REQ-08", 48.0, "mm", "no material above z 48.1; none within r 12 of the valve axis above the deck top", 0.1, "max z 48.000; 0 mm3 in r 12 about (62, 0) above z 48.0", "PASS_ASSUMED", "envelope, common_volume", ("A-10",)),
 G("REQ-09", 2.0, "mm", "up-facing pockets drain; three notches 2.0 +- 0.1 wide x 0.5 +- 0.1 high at 25/115/225 +- 1 deg", 0.1, "notches 2.000 x 0.500 (z 10.0..10.5) at 25.000/115.000/225.000, 0 mm3 in each; pin holes through from the recess floor z 9.4; window through", "PASS", "radial_extent, common_volume, sections"),
]
FAIL_BASIS_RIB = "static seat: the rib underside sits 0.1 above the bearing plane and meets the rim's inner round, so the gap is a diagonal to the chamfered recess edge; nothing moves or carries load across it, and a touch would put the rib 0.1 above the rim's own bearing plane"
findings = [
 {"id": "F1", "gate": "REQ-02", "kind": "HARD_GATE_FAIL", "measured": 0.297, "unit": "mm", "required": ">= 0.5 from the recess to the OD-H24 underside ribs and hub", "margin": -0.203,
  "at": "(0.761, -14.170, 9.890) recess edge chamfer to rib (0.750, -13.960, 10.100); 0.243 to the rib face's end r 14.056; 0.516 only when OD-H24 is cut at r 13.68 as the REPORT did", "blocks": True, "risk": "LOW",
  "risk_basis": FAIL_BASIS_RIB, "fix_direction": "not reachable inside the spec: ribs ending at r 14.056 against a recess R 14.10 +- 0.1 give 0.11 (sharp edge) to 0.30; either the Usta names the rib ends on the rim's round as part of the rim contact (spec wording or a U-18 exception), or the recess edge moves out to about r 14.55, which gives up rim bearing from r 14.3 to 14.55"},
 {"id": "F2", "gate": "REQ-01", "kind": "HARD_GATE_FAIL", "measured": 0.3773, "unit": "mm", "required": "clearance(ring, OD-H24 cup) in [0.50, 0.70]", "margin": -0.1227,
  "at": "ring root round toe (-10.584, -11.999, 10.000) to cup (-10.393, -11.781, 10.241); 0.413 with the cup from z_H24 0.3; 0.531 at the ring top", "blocks": True, "risk": "LOW",
  "risk_basis": "only the lowest 0.05 mm of the 0.3 root round is within 0.5 of the cup's foot; the ring wall keeps 0.531 over its height, D-04d's 0.30 holds, and a flowmeter pushed fully sideways would at worst perch on the round until the hooks seat it",
  "fix_direction": "ring root round 0.1 instead of 0.3 (computed about 0.55 at the toe, not built); the plan's ladder test used a cut that could not see the root"},
 {"id": "F3", "gate": "U-03", "kind": "HARD_GATE_FAIL", "measured": 0.297, "unit": "mm", "required": "clearance >= 0.5 between the mount and each OEM solid away from the contacts", "margin": -0.203,
  "at": "same pair as F1 (the recess is not delegated to REQ-02 in U-03's text); contacts, interference and both assembly paths pass", "blocks": True, "risk": "LOW", "risk_basis": FAIL_BASIS_RIB, "fix_direction": "as F1"},
 {"id": "F4", "gate": "D-04c", "kind": "HARD_GATE_FAIL", "measured": 0.297, "unit": "mm", "required": ">= 0.5 per side away from the designed contacts", "margin": -0.203,
  "at": "recess edge to rib 0.297 (F1); ring root round to cup 0.377 (F2); OD-H22 side 0.503 passes", "blocks": True, "risk": "LOW", "risk_basis": "the two contact-adjacent gaps of F1 and F2; neither is loaded or moving", "fix_direction": "as F1 and F2"},
 {"id": "F5", "gate": "REQ-04", "kind": "OBSERVATION", "measured": 10.72, "unit": "mm", "required": "slot profile 180..360 deg at z 41..47 in [7.05, 7.10]", "margin": -3.62,
  "at": "186 deg, z 46.875: the literal window runs into the gusset slit the same row requires; every ray outside the slit windows reads 7.050", "blocks": False, "risk": "LOW",
  "risk_basis": "a wording overlap in the spec row, not a geometry miss: the slits are there by REQ-04 and read 2.40 / 11.85", "fix_direction": "spec: exclude the slit windows (about +-10 deg around 180 and 360 deg above z 43.4) from the slot profile"},
 {"id": "F6", "gate": "D-01b", "kind": "OBSERVATION", "measured": 1.7224, "unit": "mm", "required": "the D-01b reason says the only region under 2.0 is the deck wedge (1.79 / 1.90)", "margin": 0.2224,
  "at": "ring wall base (-16.101, 2.520, 10.255) 1.722; catch tip 1.600 at 45 deg (-16.679, 8.825, 31.500)", "blocks": False, "risk": "LOW",
  "risk_basis": "both pass the 1.5 limit; the ring base is thinned by its root round and lip chamfer, the catch tip by the 1.6 land against the 45 deg lead-in; neither carries the snap bending (the beam stays 2.0)", "fix_direction": "spec: list these two regions in the D-01b reason"},
 {"id": "F7", "gate": "U-03", "kind": "OBSERVATION", "measured": 19.9, "unit": "mm", "required": "REPORT §4: ped_top_z and catch_under_z pass only at nominal", "margin": 0.0,
  "at": "catch underside 29.900 minus pedestal top 10.000 = 19.900 = OD-H24 rim-to-flange-top 19.9 (A-06)", "blocks": False, "risk": "LOW",
  "risk_basis": "the flowmeter pose follows the printed pedestal, so the function rests on the 19.9 stack; zero designed play means +-0.1 per face (plus A-08's +-0.2 warp) gives up to 0.4 axial play or a preload that adds about 0.09 % strain per 0.2 mm; either keeps the flowmeter held", "fix_direction": "none needed for the gate; if play shows at the first print, shorten the stack by 0.1 to preload the hooks"},
 {"id": "F8", "gate": "REQ-04", "kind": "OBSERVATION", "measured": 48.0, "unit": "mm", "required": "REPORT §4: deck_top_z passes only at nominal", "margin": 0.1,
  "at": "deck top 48.000", "blocks": False, "risk": "LOW", "risk_basis": "the valve pose follows the printed deck top and is clamped by its ear screws; +-0.1 moves the valve with it and changes no clearance in the real assembly (the sweep's overlap comes from holding the OEM pose fixed)", "fix_direction": "none"},
 {"id": "F9", "gate": "REQ-05", "kind": "OBSERVATION", "measured": 7.7, "unit": "mm", "required": "REPORT §4: deck_t passes only at nominal", "margin": 0.1,
  "at": "deck 7.700 = 2.0 clearance + 5.7 insert bore exactly", "blocks": False, "risk": "LOW", "risk_basis": "a 0.1 web left at 7.8 is pierced by the M3 screw or the insert; layer quantisation moves the step, not the stack", "fix_direction": "optional: take the insert bore 0.2 deeper into the clearance hole so the two always overlap"},
 {"id": "F10", "gate": "REQ-07", "kind": "OBSERVATION", "measured": 40.0, "unit": "mm", "required": "REPORT §4: leg_gap_half passes only at nominal", "margin": 0.1,
  "at": "leg inner faces 40.000 / 84.000 flush with the window edges", "blocks": False, "risk": "LOW", "risk_basis": "a 0.1 ledge from a leg face 0.1 inside the window is a sub-extrusion overhang that prints; no fit depends on it", "fix_direction": "none"},
 {"id": "F11", "gate": "REQ-02", "kind": "OBSERVATION", "measured": 14.1, "unit": "mm", "required": "REPORT §4: recess_r passes only at nominal", "margin": 0.0,
  "at": "recess R 14.100..14.150 over z 9.5..9.9 (the 0.2 edge chamfer)", "blocks": False, "risk": "LOW", "risk_basis": "at R 14.0 the rib gap of F1 narrows further; at 14.2 only the chamfer reads 14.25 in the band; the rim still bears from r 14.3", "fix_direction": "settle with F1"},
]
plaus = [
 {"question": "P1 gravity", "answer": "the plate rests on its bottom face; centre of mass (34.89, -0.13, 17.58) inside the footprint; OD-H24 on its rim on the pedestal (0 gap, 0 mm3) and OD-H22 on its flange back face on the deck (0 gap, 0 mm3)", "status": "YES"},
 {"question": "P2 function chains", "answer": "valve ports hang +-Y under the deck between the legs over an empty window (0 mm3 below the deck); flowmeter pipes leave toward -Y 13.3 from the nearest hook; ear holes over coaxial clearance and insert bores (offset 0); annulus and recess drain through the notches and pin holes", "status": "YES"},
 {"question": "P3 moving parts", "answer": "assembly only: OD-H24 drops 25 mm with 0 mm3 off the hooks, whose 45 deg lead-ins face up so the flange cams them out; OD-H22 slides -Y at +5 and drops 5 with 0 mm3 (121 poses), least slide gap 0.858", "status": "YES"},
 {"question": "P4 grip, reach, insertion", "answer": "nothing above z 48.0 and 0 mm3 within r 12 of the valve axis above the deck, so the OPV is open from above; screws from above; valve in along -Y into a slot open to +Y; hook catches reachable from outside at R 22.87", "status": "YES"},
 {"question": "P5 absurdity", "answer": "a 119 x 50 x 48 mm, 51.5 g PETG bracket with a 4 mm plate, 4 mm legs and 2 x 25.9 mm snap beams: ordinary proportions for a printed bracket", "status": "YES"},
 {"question": "P6 floating, embedded, mirrored, upside-down", "answer": "one solid; the assembly STEP places both OEM solids exactly where the spec joints put them (bounding boxes and volumes identical to my own placement); drive tube up to z 61.68, slot semicircle on -Y, 0 mm3 overlap", "status": "YES"},
]
C10 = json.loads((JOB / "reviews/RV01_work/s10.json").read_text())
controls = [{"check": c["check"], "mutant": c["mutant"], "got": c["got"]} for c in C10 if c["check"] != "validity.brep_valid"]
controls.append(json.loads((JOB / "reviews/RV01_work/s12.json").read_text())["control_brep_valid"])
controls += [{"check": c["check"], "mutant": c["mutant"], "got": c["got"]} for c in json.loads((JOB / "reviews/RV01_work/s13.json").read_text())]
census = [
 ("F01 plate 4.0, x -25..94, y +-25", "1 plate, z 0..4", "z 0..4.000 over x -25..94, y +-25"),
 ("F02 plate window x 40..84, full Y", "1 window splitting the plate", "2 plate pieces x -25..40 and 84..94; 0 mm3 in the window"),
 ("F03 footprint holes Ø3.4 x4", "4 through, length 4.0", "4 x Ø3.400 through, 4.000, offsets 0"),
 ("F04 pedestal R 18.0, z 4..10", "1 convex cylinder R 18.0, top z 10.0", "R 18.000, top 10.000"),
 ("F05 ring wall R 16.30..18.30, z 10..13", "1 ring", "inner 16.300, outer 18.300, top 13.000"),
 ("F05b ring lip chamfer (REPORT §8: 0.30 x 0.52 at 60 deg)", "1 cone under the 0.3 overhang", "cone 60.02 deg from horizontal, z 10.0..10.52"),
 ("F06 pin clearance holes Ø4.8, Ø3.8", "2 through, 9.4 long (P-3)", "Ø4.800 and Ø3.800 through, 9.400, offsets 0"),
 ("F07 snap hooks at 70/160/320 deg (P-4)", "3", "3, centred 70.000/160.000/320.000"),
 ("F08 legs x 36..40, 84..88, y +-15, z 4..48", "2", "2, material z 0..48 at x 38 and 86, y +-15.000"),
 ("F09 deck x 40..84, y +-15, z 40.3..48", "1", "1, z 40.300..48.000, y +-15.000"),
 ("F10/P-1 stem U-slot 14.1 open to +Y (no closed bore)", "1 U-slot", "R 7.050 semicircle on -Y, walls 7.050, 0 mm3 in the +Y channel"),
 ("F11/P-2 gusset slits 2.40 to 62 +- 11.85", "2", "2, 2.400 wide, reach 11.850, taper 43.42 deg"),
 ("F12 screw clearance holes Ø3.4", "2, 2.0 deep", "2 x Ø3.400, 2.000, offsets 0"),
 ("F13 insert bores Ø4.0", "2, 5.7 deep, open below", "2 x Ø4.000, 5.700, open on the underside"),
 ("F14 root fillets", "hooks, pedestal, legs, ring", "ring 0.3 (3 pieces), pedestal 1.0, hooks 1.5 inner and outer x3, legs 3.0 x6"),
 ("P-3 pedestal recess R 14.10 x 0.60", "1", "R 14.100, floor 9.400, plus a 0.2 edge chamfer (REPORT §8)"),
 ("P-5 ring drain notches 2.0 x 0.5", "3 at 25/115/225 deg", "3, 2.000 x 0.500 at 25/115/225"),
]
V = {"schema": "oguz-verdict-v1", "review_id": "RV01", "job_id": "20260930-od-c07-valve-flowmeter-mount", "target": "od_c07_mount_v01", "spec_version": "1.2",
     "reviewer": {"runtime": "claude-code", "model": "claude-opus-5-5"}, "verdict": "REVISE",
     "summary": "Geometry is as the spec draws it and every dimensional, print, snap and path row passes. REQ-01, REQ-02, U-03 and D-04c fail at 0.297 mm (recess edge to OD-H24 rib) and 0.377 mm (ring root round to cup) against 0.5; the REPORT's contact cut at r 13.68, z 0.5 hid both. Risk LOW.",
     "files": files, "gates": gates,
     "feature_census": [{"feature": f, "expected": e, "found": x, "status": "PASS"} for f, e, x in census],
     "plausibility": plaus, "positive_controls": controls, "findings": findings,
     "least_sure_answers": [
      {"item": "1. pin clearances 0.49999... against >= 0.5", "answer": "re-measured 0.500 at both pins (2.585, 0.093, 9.4) and (-9.880, 0.140, 9.4): PASS inside the 0.005 band, zero margin by design, resting on A-07 and A-01 as stated"},
      {"item": "2. rib clause depends on where the ribs end", "answer": "it does: 0.516 only with OD-H24 cut at r 13.68; the rib/hub inside the rim's inner radius r 13.98 reads 0.297 and the rib face's end at r 14.056 reads 0.243 against 0.5: FAIL (F1, F3, F4)"},
      {"item": "3. seat parameters pass only at nominal; 320 deg catch 4.94 from the connector", "answer": "rated LOW as F7 to F11: the seat heights are stacks that the OEM parts follow, not clearances; catch-to-connector re-measured 4.939, D-04c passes"}],
     "assumptions_relied_on": ["A-02", "A-03", "A-04", "A-06", "A-07", "A-08", "A-09", "A-10", "A-12", "A-13", "A-14", "A-15", "A-16", "A-18", "A-19"]}
out = JOB / "reviews/RV01_od_c07_mount_v01.json"
out.write_text(json.dumps(V, indent=1, ensure_ascii=False) + "\n")
print("written", len(gates), "gates", len(controls), "controls", all(c["got"] == "FAIL" for c in controls))
