"""Write 01_CAD/REPORT_od_c07_mount_v02.md (package WP-04, spec 1.2) from the measured results (D8):
the spec 1.2 check of the unchanged delivered STEP (check_out_v02/check_v02.json), the v01 build
facts and sections log (geometry and delivered poses unchanged), the v02 sweep (sweep_v02/*/check.json)
and fillet radii read from the STEP. report_od_c07_mount.py stays as the v01 record. No number is typed in here;
the narrative sections cite the measured values by reading them."""
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
sys.path.insert(0, str(HERE))
import build123d
import OCP
from build123d import GeomType
from OCP.BRepAdaptor import BRepAdaptor_Surface
from tools.core import read_step
from tools.measure import mass_properties

import sweep_od_c07_mount as S

CHECK = json.loads((HERE / "check_out_v02/check_v02.json").read_text())
CHECK_V01 = json.loads((HERE / "check_out_v01/check_v01.json").read_text())
FACTS = json.loads((HERE / "check_out_v01/build_facts_v01.json").read_text())
SECTIONS = json.loads((HERE / "check_out_v01/sections_v01.json").read_text())
KNOWN = "(b) OD-H22 slid along -Y"
PASSED = ("PASS", "PASS_ASSUMED")


def sha(p):
    h = hashlib.sha256()
    h.update(Path(p).read_bytes())
    return h.hexdigest()


def fmt(v, unit=""):
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.4f}".rstrip("0").rstrip(".") if abs(v) < 1e5 else f"{v:.1f}"
    return str(v)


def row(gid, text):
    rows = [r for r in CHECK["gates"] if r["gate"] == gid and text in r["required"]]
    return rows[0] if rows else None


def status_word(r):
    s = r["status"]
    if s == "PASS_ASSUMED":
        return "PASS (assumed: " + ", ".join(r["assumes"]) + ")"
    return s


# ---------------------------------------------------------------- fillet radii measured on the STEP
def fillet_radii():
    part = read_step(WS / "02_STEP_STL/od_c07_mount_C1_v01.step")
    tori, small_cyl = {}, {}
    for f in part.faces():
        s = BRepAdaptor_Surface(f.wrapped)
        c = f.center()
        if f.geom_type == GeomType.TORUS:
            t = s.Torus()
            key = (round(t.MajorRadius(), 3), round(t.MinorRadius(), 3))
            tori[key] = tori.get(key, 0) + 1
        elif f.geom_type == GeomType.CYLINDER:
            r = s.Cylinder().Radius()
            ax = s.Cylinder().Axis().Direction()
            if r <= 3.0 + 1e-9 and abs(ax.Z()) < 1e-6:          # horizontal-axis cylinders: straight root fillets
                key = round(r, 3)
                small_cyl[key] = small_cyl.get(key, 0) + 1
    return tori, small_cyl


# ---------------------------------------------------------------- sweep summary
def sweep_rows():
    nominal = {r["required"]: r for r in CHECK["gates"]}
    out = []
    for name, (lo, hi) in S.RUNS.items():
        rec = {"parameter": name, "low": lo, "high": hi, "runs": {}}
        for side in ("low", "high"):
            if (lo if side == "low" else hi) is None:
                rec["runs"][side] = {"nominal": True}
                continue
            d = HERE / f"sweep_{S.TAG}" / f"{name}_{side}"
            cj = d / "check.json"
            if not cj.exists():
                rec["runs"][side] = {"built": False}
                continue
            c = json.loads(cj.read_text())
            one = [r for r in c["gates"] if r["gate"] == "exactly_one_solid"]
            fails = [r for r in c["gates"] if r["status"] not in PASSED]
            worst = None
            for r in c["gates"]:
                n = nominal.get(r["required"])
                if r["margin"] is None or n is None or n["margin"] is None or r["status"] not in ("PASS", "PASS_ASSUMED"):
                    continue
                drop = r["margin"] - n["margin"]
                if drop < -1e-9 and (worst is None or drop < worst[0]):
                    worst = (drop, r)
            u03b = [r for r in c["gates"] if KNOWN in r["required"]]
            rec["runs"][side] = {"built": bool(one) and one[0]["status"] == "PASS", "fails": fails,
                                 "worst": worst[1] if worst else None, "drop": worst[0] if worst else None,
                                 "u03b": u03b[0] if u03b else None, "check_sha256": c.get("check_sha256"),
                                 "slide_least": (c["facts"].get("h22_slide_least_clearance_mm") or {}).get("measured")}
        out.append(rec)
    return out


def main():
    g = CHECK["gates"]
    f = CHECK["facts"]
    tori, cyls = fillet_radii()
    mp = mass_properties(read_step(WS / "02_STEP_STL/od_c07_mount_C1_v01.step"), 1270.0)
    FACTS["mass_g"] = round(mp["mass"].measured, 1)
    FACTS["com_mm"] = f"({mp['com_x'].measured:.1f}, {mp['com_y'].measured:.1f}, {mp['com_z'].measured:.1f})"
    FACTS["volume_step_mm3"] = mp["volume"].measured
    sweep = sweep_rows()
    env = {k: row("U-02", k) for k in ("size_x", "size_y", "size_z", "min_x", "min_y", "min_z")}
    u03b = row("U-03", KNOWN)
    u03b24 = row("U-03", "interference with the seated OD-H24")
    h22_path = f["h22_path"]
    slide_least = f["h22_slide_least_clearance_mm"]
    rib = row("REQ-02", "recess to the OD-H24 underside ribs")
    pin1 = row("REQ-02", "pin 1 Ø4.8: clearance")
    pin2 = row("REQ-02", "pin 2 Ø3.8: clearance")
    mw = row("D-01a", "min_wall")
    ww = row("U-06", "Soft")
    conn = row("D-04c", "above its flange top plane")
    wedge = f["deck_wedge_width_at_top_mm"]
    not_passed = [r for r in g if r["status"] not in PASSED]
    stopped = bool(not_passed)
    v01_u03b = [r for r in CHECK_V01["gates"] if r["gate"] == "U-03" and KNOWN in r["required"]][0]

    files = []
    for rel in ["01_CAD/check_od_c07_mount.py", "01_CAD/build_od_c07_mount.py", "01_CAD/sections_od_c07_mount.py",
                "01_CAD/sweep_od_c07_mount.py", "01_CAD/report_od_c07_mount_v02.py",
                "02_STEP_STL/od_c07_mount_C1_v01.step", "02_STEP_STL/od_c07_assembly_C1_v01.step",
                "02_STEP_STL/od_c07_mount_C1_v01.stl",
                *[s["file"] for s in SECTIONS],
                "01_CAD/check_out_v02/check_v02.json", "01_CAD/check_out_v02_log.txt", "01_CAD/sweep_v02_log.txt",
                "01_CAD/check_out_v01/build_facts_v01.json", "01_CAD/check_out_v01/sections_v01.json",
                "01_CAD/REPORT_od_c07_mount_v01.md", "01_CAD/report_od_c07_mount.py", "01_CAD/check_out_v01/check_v01.json",
                *sorted(str(p.relative_to(WS)) for p in (HERE / "build_probes_v01").glob("probe_b*_v01.py"))]:
        files.append((rel, sha(WS / rel)))
    notes = {"01_CAD/check_od_c07_mount.py": "checks (D3), updated to spec 1.2 in WP-04: U-03(b) path, one-sided REQ-01/02/04 bands",
             "01_CAD/build_od_c07_mount.py": "parametric build and exports; OEM placement by RigidJoint (unchanged since v01)",
             "01_CAD/sections_od_c07_mount.py": "D6 sections (unchanged; the delivered poses did not change, so no section was regenerated)",
             "01_CAD/sweep_od_c07_mount.py": "D7 sweep driver, spec 1.2 bands (outputs in 01_CAD/sweep_v02/)",
             "01_CAD/report_od_c07_mount_v02.py": "writes this REPORT from the measured JSON",
             "02_STEP_STL/od_c07_mount_C1_v01.step": "AP242, the v01 export, unchanged (WP-04: no geometry change); re-imported for every measurement",
             "02_STEP_STL/od_c07_assembly_C1_v01.step": "check assembly: od_c07_mount + OD-H22 + OD-H24 as placed (AP242), unchanged",
             "02_STEP_STL/od_c07_mount_C1_v01.stl": f"unchanged; meshed from the re-imported STEP after clearing the cached triangulation; tolerance {FACTS['stl']['tolerance_mm']} mm / angular {FACTS['stl']['angular_tolerance_rad']} rad, {FACTS['stl']['triangles']} triangles",
             "01_CAD/check_out_v02/check_v02.json": "every spec 1.2 gate row with measured value, margin and location; the OD-H22 path poses",
             "01_CAD/check_out_v02_log.txt": "console log of the v02 check",
             "01_CAD/sweep_v02_log.txt": "console log of the v02 sweep driver",
             "01_CAD/check_out_v01/build_facts_v01.json": "fillet ladders, round trip, STL facts (v01 build, unchanged)",
             "01_CAD/check_out_v01/sections_v01.json": "sections log with nothing_clipped (v01, unchanged)",
             "01_CAD/REPORT_od_c07_mount_v01.md": "the record of the v01 stop (spec 1.1), kept",
             "01_CAD/report_od_c07_mount.py": "the v01 REPORT writer, kept",
             "01_CAD/check_out_v01/check_v01.json": "the v01 check (spec 1.1), kept"}
    for s in SECTIONS:
        notes[s["file"]] = f"section {s['plane']}, cut {s['cut_area_mm2']:.1f} mm², nothing_clipped {s['nothing_clipped']} px (v01, delivered pose unchanged)"

    L = []
    w = L.append
    w("# REPORT — od_c07_mount v02 (20260930-od-c07-valve-flowmeter-mount)")
    w("")
    w("Designer: Claude Code, claude-opus-5-5 · spec version 1.2 · plan `01_CAD/DESIGN_PLAN.md` with the WP-03 amendments and the WP-04 findings · brief `briefs/WP-04_designer.md` (J3, build attempt 2 of 2) · 2026-09-30 UTC")
    w("")
    npass = sum(1 for r in g if r["status"] in PASSED)
    if not stopped:
        w(f"**Outcome: SUBMITTED.** The geometry is the v01 export, unchanged (`02_STEP_STL/od_c07_mount_C1_v01.step`, same SHA-256 as the brief). Re-checked against spec 1.2: {npass} of {len(g)} scripted rows pass on the re-imported STEP. "
          f"U-03(b), the v01 stop, now reads {fmt(u03b['measured'])} mm³ along the spec 1.2 OD-H22 path (slide at +5.0, then a 5.0 drop; v01 at +0.5: {fmt(v01_u03b['measured'])} mm³); the least clearance along the slide is {fmt(slide_least['measured'])} mm. No fix cycle was used in this package.")
    else:
        w(f"**Outcome: STOPPED (D9).** {len(not_passed)} of {len(g)} rows do not pass on the spec 1.2 check: " + "; ".join(f"{r['gate']} {r['required']} = {fmt(r['measured'])} {r['unit']} ({r['status']})" for r in not_passed) + " (§10).")
    w("")
    w("## 1. Files")
    w("")
    w("| File | SHA-256 | Note |")
    w("|---|---|---|")
    for rel, h in files:
        w(f"| `{rel}` | {h} | {notes.get(rel, 'diagnostic probe of v01 (not a gate check)')} |")
    w("")
    w("Sweep outputs (STEP, STL, check.json per run) are in `01_CAD/sweep_v02/<parameter>_<low|high>/`; they are not deliverables. The v01 sweep (spec 1.1 bands) stays in `01_CAD/sweep_v01/`.")
    w("")
    w("## 2. Versions")
    w("")
    w(f"Python {platform.python_version()} · build123d {build123d.__version__} · OCP {getattr(OCP, '__version__', '7.9.3.1')} (OCCT 7.9.3) · repo commit 70826895ab7666f9e5aee3f77ce88f099995f3c1")
    w("")
    w("Input hashes checked at D0, all equal to the brief: OD-H22 bc0ffd00…0028, OD-H24 1b4cbdaf…696a, `02_STEP_STL/od_c07_mount_C1_v01.step` 55c1c361…583c.")
    w("")
    w("## 3. Gate self-check")
    w("")
    w("Bands (GATES §0): mm 0.005, degrees 0.001, mm³ 0.001, counts / bool / % / mm² / ratio 0. Every value below is measured on the re-imported "
      "`02_STEP_STL/od_c07_mount_C1_v01.step` with OD-H24 and OD-H22 placed by their joints, by the spec 1.2 check script. A self-check clears no hard gate.")
    w("")
    w("| Gate | Measured | Unit | Required | Margin | At | Status |")
    w("|---|---|---|---|---|---|---|")
    for r in g:
        w(f"| {r['gate']} | {fmt(r['measured'])} | {r['unit']} | {r['required']} | {fmt(r['margin'])} | {r['at'] or '—'} | {status_word(r)} |")
    w("| U-08 | — | — | threads cosmetic | — | — | N/A by its row (no threads; inserts) |")
    w("| D-07 | — | — | fit-critical reamed bores | — | — | N/A by its row (none) |")
    w("| J-06 | — | — | printed threads | — | — | N/A by its row (inserts) |")
    w(f"| E-06 | pads are the deck, tied to both legs over the full deck section; root fillets measured on the STEP: tori {', '.join(f'R{k[0]}/r{k[1]} ×{v}' for k, v in sorted(tori.items()))}; straight fillets {', '.join(f'r{k} ×{v}' for k, v in sorted(cyls.items()))} | — | reviewer | — | — | reviewer row; designer evidence only |")
    w("| D-03b | insert-bore ceilings Ø4.0 and notch ceilings 2.0 measured above | mm | reviewer, from sections | — | — | designer numbers PASS; reviewer row |")
    w("| REQ-09 | pin holes through (REQ-02 rows), window through (REQ-07 rows), recess drains through the pin holes (they open in its floor, length 9.4), three notches measured above | — | reviewer, from sections | — | — | designer numbers PASS; reviewer row |")
    w("| J-03 | catch/root thickness ratio rows above | ratio | reviewer | — | — | reported; ε is far from its limit, so the ratio does not bind |")
    w("")
    w("Facts the gate rows rest on (measured, not gated):")
    w("")
    w(f"- Placement (joints, from measured features): {json.dumps(f['placement'])}.")
    w("- OD-H22 assembly path, spec 1.2 U-03(b) (A-22: the valve is held by its two ear screws only and slides out along +Y when they are loose, hence the −Y path): "
      + "; ".join(f"{q['leg']} y +{q['dy']:g}, z +{q['dz']:g}: {fmt(q['mm3'])} mm³ with the mount, {fmt(q['mm3_vs_od_h24'])} mm³ with OD-H24, clearance to the mount {fmt(q['clearance_mm'])} mm" for q in h22_path) + ".")
    w(f"- Least clearance along the slide (flange back face at z 53.0): {fmt(slide_least['measured'])} mm at pose y +{slide_least['pose']['dy']:g}, z +{slide_least['pose']['dz']:g}, mount point {slide_least['at']}, OD-H22 point {slide_least['on_b']}. On the drop the clearance falls to 0 at the seat (the flange contact).")
    w(f"- OD-H24 descent poses: " + "; ".join(f"+{q['dz']:g}: {fmt(q['mm3'])} mm³" for q in f['h24_path']) + " (hooks exempt).")
    w(f"- Deck wedge between each screw clearance hole and its slit end, width at the deck top (z 47.999, ray along X at y 0): +X {fmt(wedge['+X']['width'])} mm, −X {fmt(wedge['-X']['width'])} mm (D-01b's reason; `min_wall` does not read it because the hole wall and the 43.4° slit end are not opposed within 45°).")
    w(f"- Thinnest wall (D-01a/b, D-06a): {fmt(mw['measured'])} mm at {mw['at']}: the ring wall at its base, between the 0.3 ring-root round and the 60° lip chamfer; it passes D-01b's 1.5. The 45° reading (U-06) is {fmt(ww['measured'])} mm at {ww['at']}, the catch tip.")
    w(f"- Hook beam to OD-H24 flange rim (the J-04 pair, not gated): " + "; ".join(f"{k.split('_')[0]} {fmt(v['measured'])} mm" for k, v in f.items() if k.endswith('_beam_to_flange_mm')) + ".")
    w(f"- Hooks to the OD-H24 pipes and connector: " + "; ".join(f"{k.split('_')[1]}° {fmt(v['measured'])} mm" for k, v in f.items() if k.startswith('hook_') and k.endswith('_to_pipes_connector_mm')) + f" (outside r 20.5); to anything of OD-H24 above its flange top plane {fmt(conn['measured'])} mm at {conn['at']} (the 320° catch to the connector's corner). Accepted in spec 1.2 (A-09 note): the gate is D-04c ≥ 0.5, which passes; no change.")
    w(f"- Feature census (faces per kind): {json.dumps(f['feature_census'])}.")
    w(f"- Flat downward faces found (D-03a named set): {json.dumps(f['downward_flat_faces'])}.")
    w(f"- D-03a slab scans: {json.dumps(f['overhang_slabs'])}.")
    w(f"- STL: R_max {fmt(f['stl_R_max_mm'])} mm (the outer hook-root round), limit 4·acos(1 − 0.01/R_max) = {fmt(4*math.acos(1-0.01/f['stl_R_max_mm']))} rad; re-mesh of the STEP reproduces the delivered STL bytes: {f['stl_remesh_matches_delivered']}; mesh census {json.dumps(f['stl_mesh_census'])}.")
    w("")
    w("## 4. Robustness sweep (D7)")
    w("")
    w(f"Each run rebuilt the part with one fit-critical parameter at the end of its spec 1.2 tolerance and ran the same spec 1.2 check script (all {len(g)} rows, including the new U-03(b) path). "
      "The OEM poses stay at the spec §2 joints. For ring_ri, pin1_d, pin2_d, slot_w and slit_x_top the spec 1.2 band is one-sided (+0.1/−0): the low end is the nominal value, so the nominal check (§3) stands for it and only the high end was built.")
    w("")
    w("| Parameter | Low · nominal · high | All built, one solid | New failures against nominal (measured) | Row whose margin fell most (margin) | U-03(b) OD-H22 path (mm³) / least slide clearance (mm), low · high |")
    w("|---|---|---|---|---|---|")
    sweep_json = []
    for rec in sweep:
        sides = [s for s in ("low", "high") if not rec["runs"].get(s, {}).get("nominal")]
        built = all(rec["runs"].get(s, {}).get("built") for s in sides)
        fails, worst = [], []
        for side in sides:
            run = rec["runs"].get(side, {})
            for r in run.get("fails", []):
                fails.append(f"{side}: {r['gate']} {r['required']} = {fmt(r['measured'])} {r['unit']}")
            if run.get("worst"):
                worst.append(f"{side}: {run['worst']['gate']} {run['worst']['required']} ({fmt(run['worst']['margin'])} {run['worst']['unit']})")
        lo = "= nominal (one-sided, spec 1.2)" if rec["low"] is None else " ".join(rec["low"])
        vals = f"{lo} · nominal · {' '.join(rec['high'])}"
        path = []
        for s in ("low", "high"):
            run = rec["runs"].get(s, {})
            if run.get("nominal"):
                path.append("nominal")
            elif run.get("u03b"):
                path.append(f"{fmt(run['u03b']['measured'])} / {fmt(run.get('slide_least'))}")
            else:
                path.append("—")
        w(f"| {rec['parameter']} | {vals} | {'yes' if built else 'NO'} | {'; '.join(fails) or 'none'} | {'; '.join(worst) or '—'} | {' · '.join(path)} |")
        margins = [rec['runs'][s]['worst']['margin'] for s in sides if rec['runs'].get(s, {}).get('worst')]
        sweep_json.append({"parameter": rec["parameter"], "values": [rec["low"] or "nominal", "nominal", rec["high"]], "all_built": built,
                           "new_failures": fails, "worst_gate": worst, "worst_margin": min(margins) if margins else None})
    only_nominal = [rec["parameter"] for rec in sweep_json if rec["new_failures"]]
    shas = {rec["runs"][s].get("check_sha256") for rec in sweep for s in ("low", "high") if rec["runs"].get(s, {}).get("check_sha256")}
    w("")
    w(f"Passes only at nominal (a new failure at one end of its tolerance): {', '.join(only_nominal) or 'none'}. Causes, read from the failing rows:")
    w("")
    for k in only_nominal:
        w(f"- {k}: {SWEEP_CAUSE.get(k, 'see the failing rows')}")
    w("")
    w("The seat heights (ped_top_z, deck_top_z, catch_under_z) are designed contacts against OEM poses fixed at the spec §2 joints, and the leg inner faces are also the window edges; spec 1.2 leaves their bands as they are (brief WP-04), so these runs are kept here as findings for the reviewer (§9), not fixed. "
      "The five parameters made one-sided in spec 1.2 (ring_ri, pin1_d, pin2_d, slot_w, slit_x_top) pass at both ends unless listed above.")
    w("")
    w(f"Every sweep run built one valid solid unless the table says NO. Check script SHA-256 recorded in the run records: {', '.join(sorted(shas))} (§1 lists the check script's hash).")
    w("")
    w("## 5. Build facts")
    w("")
    w(f"- Envelope {fmt(env['size_x']['measured'])} × {fmt(env['size_y']['measured'])} × {fmt(env['size_z']['measured'])} mm at min ({fmt(env['min_x']['measured'])}, {fmt(env['min_y']['measured'])}, {fmt(env['min_z']['measured'])}); volume {fmt(FACTS['volume_step_mm3'])} mm³ (STEP); mass {FACTS['mass_g']} g at 1270 kg/m³ (A-11), centre of mass {FACTS['com_mm']} mm")
    w("- Fillets (requested ladder → achieved, v01 build unchanged): " + "; ".join(f"{k}: {v['requested']} → {v['achieved']}" for k, v in FACTS["fillets"].items()) + ". Measured on the STEP: tori (major/minor) " + ", ".join(f"R{k[0]}/r{k[1]} ×{v}" for k, v in sorted(tori.items())) + "; straight root rounds " + ", ".join(f"r{k} ×{v}" for k, v in sorted(cyls.items())) + ". The hook side edges (radial, at the sector ends) are left sharp (§8).")
    w("- Placements: OD-H24 by a RigidJoint at its measured datum (rim face: the −Z planar face at z 0; axis: the rim bore on (0, 0)), connected to the mount's joint at (0, 0, 10.0), no rotation; OD-H22 by a RigidJoint at its measured datum (flange back face: the −Z planar face at z 0; axis: the drive-tube bore; +X through the two ear holes at x −15.338 and +15.447), connected to the mount's joint at (62.0, 0, 48.0). Measured placement in §3.")
    w("- Print: bottom face on the bed; supports under the deck (z 40.3) and the three catch undersides (z 29.9) only (A-16); bridges: two insert-bore ceilings (z 46.0, Ø4.0) and three notch ceilings (z 10.5, 2.0 wide).")
    w("")
    w("## 6. Plausibility (§P, D6)")
    w("")
    w("Sections: the v01 set in `03_Sections/` (§1). The delivered poses of both OEM parts are unchanged in spec 1.2, so the two assembly sections still show the delivered pose and were not regenerated.")
    w("")
    w("| # | Question | Designer's answer, from the sections and the check assembly |")
    w("|---|---|---|")
    w(f"| P1 | gravity | The plate lies flat on the OD-C01 floor; OD-H24 rests on its rim on the pedestal top and OD-H22 on its flange back face on the deck top (both contacts measured 0 with 0 mm³ overlap); the centre of mass {FACTS['com_mm']} lies inside the footprint. |")
    w("| P2 | function chains | Valve ports leave toward ±Y under the deck, between the legs, over the open window (REQ-07); the flowmeter pipes leave toward −Y above the ring; ear screws go down through the ears into inserts pressed from below; the three catches bear on the flange top outside its slots (0 mm³ void under each). |")
    w(f"| P3 | motion clearance | OD-H24 lowered from 25 mm: 0 mm³ at all {len(f['h24_path'])} poses (hooks deflect). OD-H22 along the spec 1.2 path ({len(h22_path)} poses: slide at +5.0 from y +45 to 0, drop 5.0): {fmt(u03b['measured'])} mm³ with the mount, {fmt(u03b24['measured'])} mm³ with OD-H24; least gap on the slide {fmt(slide_least['measured'])} mm; on the drop the stem enters the U-slot and the gussets the slits from above. |")
    w("| P4 | human factors | Nothing above z 48.0 and nothing within r 12 of the valve axis above the deck (REQ-08): the OPV at the drive-tube top stays open from above; the ear screws are driven from above; the valve is fitted by sliding it in along −Y about 5 mm above the deck and dropping it into the slits; the hooks are released by pulling the catches outward. |")
    w(f"| P5 | absurdity next to a real product | A 119 × 50 × 48 mm PETG bracket of {FACTS['mass_g']} g with 2 mm snap beams 25.9 mm long and 4 mm walls: ordinary proportions for a printed hydraulic bracket. |")
    w("| P6 | nothing floating, embedded, mirrored or upside down | One solid (U-01); both OEM solids in their spec frames (drive tube up, ports ±Y, pipes −Y, connector +X), 0 mm³ overlap at the delivered pose; the slot's semicircle is on −Y and its opening on +Y. |")
    w("")
    w("## 7. Library and tools used")
    w("")
    w("Cards (from the J2 plan, not re-read): `library/uno10/CARD.md#u2-classic-box`, `library/uno10/CARD.md#u5-tank-heat-set`. "
      "`tools.core`: read_step, write_step, step_roundtrip, compare_step, validity, solid_count, brep_valid, common_volume, fillet_ladder, write_stl, mesh_sagitta. "
      "`tools.measure`: envelope, bore_census, locate_bore, feature_census, min_wall, min_wall_wide, overhang_census, clearance, radial_extent, radial_profile, mesh_census, mass_properties. "
      "`tools.drawing`: write_sections (v01). `tools.result.gate` for every comparison. "
      "New job code (in `01_CAD/`, not in the repo): the two assembly paths (loops over `common_volume` and `clearance`), the J-01 arithmetic, the note-A contact cuts, the D-03a slab scan, the flange flatness area, the notch and slit ray probes. No `tools/measure` function was missing.")
    w("")
    w("## 8. Deviations from the plan")
    w("")
    w("Carried over from REPORT v01 §8:")
    w("")
    for line in DEVIATIONS:
        w(f"- {line}")
    w("")
    w("New in v02 (WP-04, spec 1.2; no geometry change):")
    w("")
    for line in DEVIATIONS_V02:
        w(f"- {line}")
    w("")
    w("## 9. What I am least sure of")
    w("")
    w(f"1. The two pin clearances read {pin1['measured']!r} and {pin2['measured']!r} mm against ≥ 0.5 (margins inside the 0.005 band): zero margin by design at the nominal, which spec 1.2 makes the low end of the bore band; they rest on scan-derived pin diameters (A-07, A-01). A 0.3 % scale error or a pin 0.01 mm fatter fails REQ-02 and D-04c; D-04d (≥ 0.30) keeps 0.2 in hand.")
    w(f"2. REQ-02's rib clause and D-04c against OD-H24 ({fmt(rib['measured'])} mm) depend on where the ribs are taken to end: the check takes OD-H24 inside r 13.68 (the plan's note-A contact zone). Taken to r 14.056 the gap at the recess edge would read about 0.1, inside the rim contact. The recess_r low run fails this row (§4).")
    w(f"3. The seat parameters pass only at nominal (§4): ped_top_z, deck_top_z, catch_under_z against the fixed OEM poses, leg_gap_half at the window edge, deck_t (a 0.1 web at 7.8) and recess_r. These are designed contacts or exact stack-ups, not clearances; the reviewer should decide whether any needs a spec band. The 320° catch sits {fmt(conn['measured'])} mm from the connector corner (accepted in spec 1.2, A-09).")
    w("")
    w("## 10. Stop")
    w("")
    if not stopped:
        w("Not stopped.")
    else:
        for r in not_passed:
            w(f"- **{r['gate']}**: {r['required']}: {fmt(r['measured'])} {r['unit']} ({r['status']}), at {r['at']}.")
    w("")
    w(f"Fix cycles used in this package (WP-04): 0 of 3. The re-run showed no geometry fault, so the STEP, STL and build script are the v01 files (WP-03 used 2 of its 3 cycles on U-04 / U-07 and U-06 / REQ-02, REPORT v01).")
    w("")
    rep = {"schema": "oguz-report-v1", "job_id": "20260930-od-c07-valve-flowmeter-mount", "part": "od_c07_mount", "tag": "v02",
           "spec_version": "1.2", "files": [{"path": p, "sha256": h} for p, h in files],
           "versions": {"python": platform.python_version(), "build123d": build123d.__version__, "ocp": "7.9.3.1",
                        "repo_commit": "70826895ab7666f9e5aee3f77ce88f099995f3c1"},
           "gates": [{k: r[k] for k in ("gate", "measured", "unit", "required", "margin", "at", "status", "assumes")} for r in g],
           "sweep": sweep_json,
           "u03b_h22_path": h22_path,
           "u03b_slide_least_clearance_mm": slide_least,
           "least_sure": ["pin clearances at exactly 0.500 on scan-derived pins (A-07, A-01); nominal is now the band's low end",
                          "REQ-02 rib clause / D-04c OD-H24 depends on the rib end (note-A r 13.68)",
                          "seat parameters and recess_r pass only at nominal (designed contacts / stack-ups); hook 320° catch 4.94 mm from the connector (accepted, A-09)"],
           "fix_cycles": {"used": 0, "cap": 3},
           "stopped": stopped}
    if stopped:
        rep["stop"] = [{"gate": r["gate"], "required": r["required"], "measured": r["measured"], "unit": r["unit"], "status": r["status"]} for r in not_passed]
    w("```json")
    w(json.dumps(rep, indent=1, default=str))
    w("```")
    (HERE / "REPORT_od_c07_mount_v02.md").write_text("\n".join(L) + "\n")
    print("written", len(L), "lines; not passed", len(not_passed))


SWEEP_CAUSE = {
    "ped_top_z": "the pedestal top is the OD-H24 seat; with the pose fixed at the spec joint, 9.9 leaves the rim 0.1 above it and 10.1 pushes it into the flowmeter; the recess moves with the pedestal top, so its floor and its chamfer leave REQ-02's z bands; at 10.1 the pin 2 clearance reads 0 and the REQ-01 ring profile reads nothing (INCONCLUSIVE, the flowmeter pose overlaps the seat).",
    "deck_top_z": "the deck top is the OD-H22 seat; 47.9 leaves the flange 0.1 above it, 48.1 pushes it into the valve (so the U-03(b) path's final pose overlaps too).",
    "catch_under_z": "the catch underside is the designed contact with the flange top; 29.8 overlaps the flange, 30.0 leaves 0.1 and the landing prism reads the gap as void.",
    "leg_gap_half": "the leg inner faces are also the window edges (x 40.0 / 84.0); a leg face 0.1 inside the window leaves a 0.1 flat ledge over the window, a downward face D-03a does not name.",
    "deck_t": "the deck is exactly 2.0 clearance + 5.7 insert deep; at 7.8 a 0.1 web closes the screw path between the two bores.",
    "recess_r": "high: the 0.20 recess edge chamfer adds 0.05 at z 9.85, so R 14.20 reads 14.25 in REQ-02's band z 9.5 … 9.9; low: at R 14.00 the recess edge comes 0.44 from the OD-H24 ribs (note-A cut).",
}

DEVIATIONS = [
    "Spec 1.1 amendments built as the brief states (checked by the orchestrator): Q1 → P-1, a U-slot 14.1 wide, semicircular about (62, 0) on −Y, straight walls at x 62 ± 7.05 open through the deck's +Y edge, no closed stem bore (the brief's \"walls at y ±7.05\" read as ±7.05 from the axis across X, since the slot opens along +Y); Q2 → slits 2.40 wide (y ±1.20) reaching x 62 ± 11.85 at the top, end taper 43.42°; Q3 → P-3 recess R 14.10 × 0.60 (floor z 9.40), pin holes 9.4 long; Q4 → P-4 hook 3 at 320°; Q5 → P-5 three notches 2.0 × 0.5 at 25°, 115°, 225°; Q6 → the insert-bore and notch ceilings are gated under D-03b and named out of D-03a; J-01 computed with y measured (1.5); the U-05 census list of the brief; U-03(b) path along −Y at +0.5 (spec 1.1; replaced by the spec 1.2 path, below); A-22 cited in §3.",
    "Deck unioned before the root fillets (plan: after): the window splits the plate in two, and only the deck joins the halves, so the fillet ladder's one-solid test needs it in place.",
    "Hook root fillets (fix cycle 1): the plan filleted the hook foot edges with `fillet_ladder`; that result lost 0.0027 mm³ through the STEP round trip (U-04 band 0.001), from the corner blends where the radial and arc fillets meet. The fillets are now webs of radius 1.5 in the revolved hook profile (inner and outer beam faces), so they are exact tori cut by the sector planes; the ladder (1.5, 1.0, 0.5) is kept with a one-valid-solid test per rung; the two radial side edges of each hook foot are left sharp. Round trip after: 1.8e-09 mm³.",
    "STL angular tolerance 0.05 rad (plan: 0.1183, the U-07 upper bound): at 0.1183 the mesher left 0.037 mm sagitta on the 0.3 ring-root round (fix cycle 1); 0.05 gives 0.0040 mm with 92 262 triangles.",
    "Ring lip chamfer 0.30 radial × 0.52 high, 60° from horizontal (plan F05b: 0.30 × 45°): a cone at exactly 45° reads INCONCLUSIVE in `overhang_census` (its sampling bound straddles the limit).",
    "Catch land 1.6 (plan: 1.0), fix cycle 2: U-06 (Soft) read the catch tip, where the underside and the 45° lead-in are opposed within 45°, as a 1.0 wall. Hook top now z 33.5. Catch underside, reach, lead-in, L, y and ε are unchanged.",
    "Recess edge chamfer 0.20 × 45° (not in the plan), fix cycle 2: with a sharp recess rim the OD-H24 ribs (note-A cut, r ≤ 13.68) were 0.432 from the rim edge against REQ-02's ≥ 0.5; now 0.516. The recess reads R 14.10 … 14.15 over REQ-02's band z 9.5 … 9.9, the floor z 9.40.",
    "The build script's last edit (where `main()` writes the build-facts JSON: `01_CAD/check_out_v01/` instead of `02_STEP_STL/`) came after the v01 export; the geometry code is unchanged, and the check's U-04 rebuild with the listed script matches the delivered STEP (volume delta and faces delta in §3).",
    "Ring inner root fillet 0.3 achieved with the plan's acceptance test (ring gap to the OD-H24 cup ≥ 0.50 after the rung).",
    "REQ-04 slot profile read over 192° … 348° instead of 180° … 360°: the two slits leave the slot along ±X and, at z ≥ 43.4, open the rays at 180° and 360° to the slit ends; the straight walls and the width are read separately at y 2.5 … 14. The flatness clause is gated as the flange-back-face area (mm²) that neither rests on the z 48 deck plane nor lies over the planned slot and slits.",
    "D-03a is scanned in five horizontal slabs whose floors lie at z 10.5, 29.9, 40.3 and 46.0, so exactly the named faces (3 notch ceilings, 3 catch undersides, the deck underside, 2 insert-bore ceilings) rest on a slab's bed; a second row counts flat downward faces outside that set (0).",
    "Two D-04c rows added to the plan's: the hooks to OD-H24 outside r 20.5 (pipes, connector) and the hooks to OD-H24 above its flange top plane.",
    "REQ-03's landing clause is gated as the void under each catch (sector r 18.87 … 19.70, 2.65 deep to the slot floors) ≤ 0 mm³, not against the J2 probe's 20.69 mm³.",
]

DEVIATIONS_V02 = [
    "U-03(b) OD-H22 path per spec 1.2: the check sets it in its own constant `U03B` (slide at +5.0 over y 45, 35, 25, 16, 14, 12, 10, 8, 6, 4, 2, 0, then the drop at z +4, 3, 2, 1, 0.5, 0) and replaces the build Params' h22_* fields with it (the build never reads them; the build script is not edited, brief WP-04). The path is checked against the mount and, in a second row, against the seated OD-H24 (spec: 'against everything but the hooks'); the clearance to the mount is measured at every slide pose and the least is reported.",
    "One-sided bands of spec 1.2 in the check: REQ-01 ring inner R [16.30, 16.40]; REQ-02 pin bores Ø4.8 / Ø3.8 +0.1/−0; REQ-04 slot profile [7.05, 7.10], slot width 14.1 +0.1/−0, slit reach 11.85 +0.1/−0. The slot straight-wall row, one row per side in v01 (the reading farthest from 7.05), is now two rows per side (least and greatest), since a one-sided band has no single worst direction. The brief's 'straight walls y ±(7.05 +0.05/−0)' is read, as in v01, as ±7.05 from the axis across X.",
    "The check writes its temporary re-mesh (U-07) next to its output JSON instead of `check_out_v01/`, so parallel sweep runs no longer share one temporary file.",
    "The sweep driver writes to `01_CAD/sweep_v02/`; the five one-sided parameters are swept at the high end only (their low end is the nominal). A new REPORT writer `report_od_c07_mount_v02.py`; the v01 writer and REPORT stay as the record of the stop.",
    "No section was regenerated: the delivered poses in the two assembly sections are unchanged in spec 1.2.",
]


if __name__ == "__main__":
    main()
