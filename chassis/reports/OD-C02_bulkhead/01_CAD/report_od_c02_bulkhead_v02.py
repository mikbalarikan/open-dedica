"""D8: write 01_CAD/REPORT_od_c02_bulkhead_v02.md from the measured JSON files
(check, sweep summary, sections, build record, probes) and the designer's text below.
Every number in the tables is read from those files; nothing is typed in."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
CHK = json.loads((HERE / "check_od_c02_bulkhead_v02.json").read_text())
SWP = json.loads((HERE / "sweep_v02/sweep_summary_v02.json").read_text())
SEC = json.loads((HERE / "sections_v02.json").read_text())
REC = json.loads((HERE / "build_record_v02.json").read_text())
PATH = json.loads((HERE / "probe/probe_assembly_path_v02.json").read_text())
F = CHK["facts"]
ROWS = CHK["gates"]
VERSIONS = {"python": "3.13.7", "build123d": "0.11.1", "ocp": "cadquery-ocp-novtk 7.9.3.1.1 (OCCT 7.9.3)",
            "repo_commit": "d7ea010502a30dd025c5123992847da1b15f3ee3"}
SPEC_ROWS = ["U-01", "U-02", "U-03", "U-04", "U-05", "U-06", "U-07", "U-08", "D-01a", "D-01b", "D-02", "D-03a",
             "D-03b", "D-04a", "D-05a", "D-05b", "D-06a", "D-07", "J-05", "E-06", "REQ-01", "REQ-02", "REQ-03",
             "REQ-04", "REQ-05", "REQ-06", "REQ-07", "REQ-08", "REQ-09", "exactly_one_solid", "feature_census",
             "envelope_within_spec"]
RANK = {"FAIL": 0, "INCONCLUSIVE": 1, "PASS_ASSUMED": 2, "PASS": 3, "N/A": 4}


def sha(p):
    return hashlib.sha256((WS / p).read_bytes()).hexdigest()


def fam(g):
    return g.split(".")[0].replace("(Soft)", "").replace("(b)", "")


def fmt(v, nd=4):
    if v is None:
        return "—"
    if isinstance(v, float):
        s = f"{v:.{nd}f}".rstrip("0").rstrip(".")
        return "0" if s in ("-0", "") else s
    return str(v)


def fat(a):
    if a in (None, ""):
        return "—"
    if isinstance(a, str):
        return a
    try:
        if isinstance(a[0], (list, tuple)):
            return "; ".join(fat(x) for x in a)
        return "(" + ", ".join(fmt(float(x)) for x in a) + ")"
    except Exception:  # noqa: BLE001
        return str(a)


def status_words(r):
    s = r["status"]
    if s == "PASS_ASSUMED":
        return f"PASS (assumed: {', '.join(r.get('assumes', []))})"
    return s


def summary(fid):
    rows = [r for r in ROWS if fam(r["gate"]) == fid]
    if not rows:
        return None, []
    def key(r):
        m = r.get("margin")
        return (RANK.get(r["status"], 5), m if isinstance(m, (int, float)) else 1e9)
    return min(rows, key=key), rows


files = ["01_CAD/DESIGN_PLAN.md", "01_CAD/DESIGN_PLAN_v02.md", "01_CAD/check_od_c02_bulkhead_v02.py",
         "01_CAD/build_od_c02_bulkhead_v02.py", "01_CAD/build_record_v02.json",
         "01_CAD/check_od_c02_bulkhead_v02.json", "01_CAD/check_od_c02_bulkhead_v02.log",
         "01_CAD/sections_od_c02_bulkhead_v02.py", "01_CAD/sections_v02.json",
         "01_CAD/sweep_od_c02_bulkhead_v02.sh", "01_CAD/sweep_summary_v02.py",
         "01_CAD/sweep_v02/sweep_summary_v02.json", "01_CAD/probe/probe_assembly_path_v02.py",
         "01_CAD/probe/probe_assembly_path_v02.json", "01_CAD/report_od_c02_bulkhead_v02.py",
         "02_STEP_STL/od_c02_bulkhead_C1_v02.step", "02_STEP_STL/od_c02_assembly_C1_v02.step",
         "02_STEP_STL/od_c02_bulkhead_C1_v02.stl"] + [s["file"] for s in SEC]
notes = {
    "01_CAD/DESIGN_PLAN.md": "the base plan (spec 1.0), unchanged since v01",
    "01_CAD/DESIGN_PLAN_v02.md": "plan amendment for spec 1.1 (brief WP-03), written before the v02 geometry",
    "01_CAD/check_od_c02_bulkhead_v02.py": "checks, written before the v02 build (D3)",
    "01_CAD/build_od_c02_bulkhead_v02.py": "parametric build script (D4)",
    "01_CAD/build_record_v02.json": "build record: parameters, export hashes, placements",
    "01_CAD/check_od_c02_bulkhead_v02.json": f"check results ({len(ROWS)} rows, facts)",
    "01_CAD/check_od_c02_bulkhead_v02.log": "check run log",
    "01_CAD/sections_od_c02_bulkhead_v02.py": "sections script (D6)",
    "01_CAD/sections_v02.json": "sections log",
    "01_CAD/sweep_od_c02_bulkhead_v02.sh": "sweep driver (D7)",
    "01_CAD/sweep_summary_v02.py": "sweep summary script",
    "01_CAD/sweep_v02/sweep_summary_v02.json": "sweep results, 12 variants plus nominal",
    "01_CAD/probe/probe_assembly_path_v02.py": "assembly path probe (L-10), diagnostic",
    "01_CAD/probe/probe_assembly_path_v02.json": "assembly path probe results",
    "01_CAD/report_od_c02_bulkhead_v02.py": "writes this REPORT from the JSON files",
    "02_STEP_STL/od_c02_bulkhead_C1_v02.step": "AP242, re-imported for every measurement",
    "02_STEP_STL/od_c02_assembly_C1_v02.step": "AP242 check assembly, 8 labelled solids",
    "02_STEP_STL/od_c02_bulkhead_C1_v02.stl": (f"tolerance {REC['stl']['tolerance']} mm / angular "
                                               f"{REC['stl']['angular_tolerance']} rad, "
                                               f"{F['mesh_census']['triangles']} triangles, cached "
                                               "triangulation cleared by write_stl"),
}
for s in SEC:
    notes[s["file"]] = (f"{s['view']} {s['plane']} through {tuple(s['through'])}; cut {s['cut_area_mm2']:.2f} mm²; "
                        f"nothing clipped ({s['nothing_clipped']})")
hashes = {p: sha(p) for p in files}

L = []
A = L.append
A("# REPORT — od_c02_bulkhead v02 (20260930-od-c02-bulkhead)")
A("")
A("Designer: Claude Code, claude-opus-5-5 · spec version 1.1 · plan `01_CAD/DESIGN_PLAN.md` with the amendment "
  "`01_CAD/DESIGN_PLAN_v02.md` · 2026-09-30 UTC · brief WP-03, build attempt 2 of 2 · **outcome: SUBMITTED**")
A("")
A("## 1. Files")
A("")
A("| File | SHA-256 | Note |")
A("|---|---|---|")
for p in files:
    A(f"| `{p}` | {hashes[p]} | {notes.get(p, '')} |")
A("")
st = F["stl"]
A("Inputs checked against the brief (WP-02 table, unchanged for WP-03) before any work: all nine SHA-256 match. "
  "Every v01 file is left as it was. `01_CAD/sweep_v02/<variant>/` holds each sweep run's STEP, STL, assembly, "
  "build record and check JSON (not deliverables); `01_CAD/sweep_v02/_mesh_check/remesh_check.stl` is the "
  "check's scratch re-mesh for U-07. No 3MF: the orchestrator's step. STL facts for it: "
  f"{F['mesh_census']['triangles']} triangles, mesh volume {F['mesh_census']['volume']:.3f} mm³ (B-rep "
  f"{F['mass']['volume']:.3f} mm³), bounding box {st['bbox_min']} … {st['bbox_max']} (size {st['bbox_size']}).")
A("")
A("## 2. Versions")
A("")
A(f"Python {VERSIONS['python']} · build123d {VERSIONS['build123d']} · OCP {VERSIONS['ocp']} · repo commit "
  f"{VERSIONS['repo_commit']} (clean)")
A("")
A("## 3. Gate self-check")
A("")
counts = {}
for r in ROWS:
    counts[r["status"]] = counts.get(r["status"], 0) + 1
A(f"Every value is measured from the re-imported STEP (`check_od_c02_bulkhead_v02.json`, {len(ROWS)} rows: "
  + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())) + "). One line per §5 row with its worst sub-row; "
  "every sub-row is in the JSON block. Bands from GATES §0 (mm 0.005, deg and mm³ 0.001, counts 0). `min_wall`, "
  "`min_wall_wide` and `overhang_census` ran at spacing 0.7 (the WP-02 brief's note; largest step 0.697674 mm). "
  "These are self-checks: none clears a Hard gate.")
A("")
A("| Gate | Measured | Required | Margin | At | Status | Assumes |")
A("|---|---|---|---|---|---|---|")
summ = {}
for fid in SPEC_ROWS:
    w, rows = summary(fid)
    if w is None:
        A(f"| {fid} | — | — | — | — | NOT CHECKED | — |")
        continue
    summ[fid] = w
    A(f"| {fid} ({len(rows)} rows; worst: `{w['gate']}`) | {fmt(w['measured'])} {w.get('unit', '')} | "
      f"{w['required']} | {fmt(w.get('margin'))} | {fat(w.get('at'))} | {status_words(w)} | "
      f"{', '.join(w.get('assumes', [])) or '—'} |")
A("")
A("Notes on the rows that are not a plain PASS:")
A("")
A("- **U-03**: INCONCLUSIVE only through `U-03.h11.interference`, which the U-03 row itself makes INCONCLUSIVE "
  "(OD-H11 unsound, OD-C04 A-14); OD-H11 is gated on distance and every other U-03 sub-row reads PASS (assumed: "
  "A-01, A-02). **U-04**: the part round trip and every other assembly part pass; only OD-H11's volume changes on "
  "the write (0.0524 mm³, the unsound input, as in v01).")
A("- **E-06** (reviewer row): one solid; both rails run the wall's whole length z −240 … −30 (sections "
  "`left_x61_wet_flanges`, `left_x69_elec_flanges`: each flange cut is 4200 mm² = 12 × 210 + 8 × 210); no boss "
  "stands free: every bore lies inside a rail. **REQ-09** (Soft bench): INCONCLUSIVE by its row, risk rating "
  "medium: a 4.0 wall 195 tall between the rails, held at four screws below and two above.")
A("- **D-03a**: the gated number is `overhang_census` on the re-imported solid with the six named-exception "
  f"bores refilled by position ({F['D-03a.exception_bores']} bores found, refilled solid {F['D-03a.refilled_faces']} "
  "faces as planned): least 45.0° at the window gables, planar and exact (sampling bound 0), no sample under "
  "45°. Apart: the whole-part census reads "
  f"{fmt(F['D-03a.whole_part_census']['measured'])}° at {fat(F['D-03a.whole_part_census']['at'])} (a base-rail "
  "bore crown). The downward faces split by position:")
A("")
A("| Region (by position) | Faces | Least angle (deg) |")
A("|---|---|---|")
for k, v in sorted(F["down_face_regions_least_deg"].items()):
    A(f"| {k} | {v['faces']} | {fmt(v['least_deg'])} |")
A("")
A("- **D-03b** (reviewer row): the designer's reading is the widest horizontal bore measured by `bore_census`, "
  "4.0 (the six insert bores, the named exception); the four windows carry the 45° gable, and nothing else "
  "bridges (no rib, no collar: sections `front_y150_windows`, `front_y60_w4`, `left_x65_wall`).")
A("")
A("**U-03 (a), REQ-01 and REQ-05 on the parts as placed in the assembly STEP** (nearest point on the bulkhead in `At`):")
A("")
A("| Row | Measured | Required | Margin | At | Status |")
A("|---|---|---|---|---|---|")
for r in ROWS:
    if r["gate"].startswith(("U-03.", "REQ-05.", "REQ-01.plate_coax")):
        A(f"| `{r['gate']}` | {fmt(r['measured'])} {r.get('unit', '')} | {r['required']} | {fmt(r.get('margin'))} | "
          f"{fat(r.get('at'))} | {status_words(r)} |")
A("")
A("The coaxiality rows locate each plate hole at the bulkhead bore's measured axis point 3.0 below the plate top "
  "(y −3), so the offset is the distance between the two axes. The plate holes read "
  + "; ".join(f"z {k.split('_z')[1]}: Ø{fmt(v['diameter'])}, {fmt(v['length'])} long, through {v['through']}"
              for k, v in F.items() if k.startswith("U-03.plate_hole")) + ".")
A("")
A("**The six insert bores and the four windows:**")
A("")
A("| Row | Measured | Required | Margin | At | Status |")
A("|---|---|---|---|---|---|")
for r in ROWS:
    if r["gate"].startswith(("REQ-01.base", "REQ-07.", "D-05a.", "J-05.", "REQ-04.")):
        A(f"| `{r['gate']}` | {fmt(r['measured'])} {r.get('unit', '')} | {r['required']} | {fmt(r.get('margin'))} | "
          f"{fat(r.get('at'))} | {status_words(r)} |")
A("")
roof = [f"{k.split('.')[1]} {k.split('_')[-1]}°: {fmt(v['measured'])} (design {fmt(v['design_mm'])})"
        for k, v in F.items() if ".roof_ray_" in k]
A("Gable roof rays at 60° and 120° from the window axis (reported, not gated): " + "; ".join(roof) + ". The front "
  "end z −30 is one planar face of 1012 mm² (the whole I-profile): window 4 closes inside the wall, its apex "
  "11.0 behind the front end.")
A("")
A("## 4. Robustness sweep (D7)")
A("")
A("Twelve variants, each rebuilt, exported into `01_CAD/sweep_v02/<variant>/`, and put through the same full check "
  "(assembly included). Every run built one valid solid.")
A("")
A("| Parameter | Low · nominal · high | All built, one solid | Not passing (low / high) | Worst gate | Worst margin |")
A("|---|---|---|---|---|---|")
for p in SWP["parameters"]:
    lo = ", ".join(p["failing"]["low"]) or "none"
    hi = ", ".join(p["failing"]["high"]) or "none"
    A(f"| {p['parameter']} | {' · '.join(str(v) for v in p['values'])} | {'yes' if p['all_built'] else 'no'} | "
      f"{lo} / {hi} | {p['worst_gate']} | {fmt(p['worst_margin'])} |")
A("")
A("Worst margin per gate over the nominal build and the twelve variants (the OD-H11 rows INCONCLUSIVE by the row "
  "and the reviewer rows left out):")
A("")
A("| Gate | Worst margin | Row | Variant | Status there |")
A("|---|---|---|---|---|")
for k, v in sorted(SWP["worst_margin_per_gate"].items()):
    A(f"| {k} | {fmt(v['margin'])} | `{v['gate']}` | {v['variant']} | {v['status']} |")
A("")
A("Reading: the nominal part passes every gate. Three parameters pass only on one side of their band, each "
  "because the nominal sits on a spec limit: (1) **bore_depth 6.1** (inside REQ-07's ±0.1) leaves 1.9 between the "
  "top-rail bore floor and the top rail's underside at the wall-face line x 63 / 67, so D-01b and U-06 read 1.9 "
  "(FAIL); at 5.9 and 6.0 they read 2.1 and 2.0. (2) **brail_x0 58.9** fails REQ-05 (min_x ≥ 59.0) and the "
  "carrier-box clearance (3.9 < 4.0). (3) **brail_x1 71.1** fails REQ-08 (max_x ≤ 71.0). REQ-02's ±0.10 band "
  "on the rail's wet face is one-sided in practice (59.0 … 59.1), and so is the electric edge (70.9 … 71.0).")
A("")
A("## 5. Build facts")
A("")
e = F["envelope"]
A(f"- Envelope {fmt(e['size_x'], 3)} × {fmt(e['size_y'], 3)} × {fmt(e['size_z'], 3)} mm at x {fmt(e['min_x'], 3)} … "
  f"{fmt(e['max_x'], 3)}, y {fmt(e['min_y'], 3)} … {fmt(e['max_y'], 3)}, z {fmt(e['min_z'], 3)} … {fmt(e['max_z'], 3)}; "
  f"volume {F['mass']['volume']:.1f} mm³; mass {F['mass']['mass']:.1f} g at 1070 kg/m³ (A-09); centre of mass "
  f"({F['mass']['com_x']:.2f}, {F['mass']['com_y']:.2f}, {F['mass']['com_z']:.2f}).")
A("- Fillets: none in the spec; none requested, none built.")
A("- Features as the plan amendment §3: wall, base rail x 59 … 71, top rail x 59.5 … 70.5, four gabled windows "
  "cut x 62 … 68, four Ø4.0 × 6.0 bores from y 0, two from y 215. Census measured: "
  + ", ".join(f"{k} {v}" for k, v in F["feature_census"].items() if v) + "; 4 bores open at y 0, 2 open at y 215.")
A("- Placements (assembly STEP, 8 labelled solids), unchanged from v01: OD-C01 at the identity; OD-C03 and OD-H01 "
  "at the OD-C01 §4 joint (local x → +Z, y → −Y, z → +X, origin (0, 40, −205)); OD-C04 and OD-H11 at the identity "
  "rotation, origin (0, 70, −140); OD-G01 v02 (local x → X, y → +Z, z → −Y, origin (0, 180.06, 32)); each by a "
  "RigidJoint on the bulkhead's machine frame connected to the part's own STEP origin; the carrier foot box "
  "`od_c05_foot_reference_A02` x ±55, y 0 … 210, z −70 … −26 from the spec's values.")
A(f"- STL: `write_stl` at {REC['stl']['tolerance']} mm / {REC['stl']['angular_tolerance']} rad (≤ 0.2310), "
  f"{F['mesh_census']['triangles']} triangles, sagitta at export {REC['stl']['max_sagitta']:.6f} mm; the re-mesh of "
  "the re-imported STEP reads the same. `mesh_census`: 1 body, 0 naked edges, consistent winding.")
A("- U-04: the part re-reads with volume delta 1.7e-10 mm³, faces delta 0, valid after 1; the assembly keeps 8 "
  "solids, faces and labels; per-part volume deltas ≤ 4.3e-9 mm³ except OD-H11 (0.0524 mm³, unsound input).")
A("")
A("## 6. Plausibility (§P, D6)")
A("")
pc = PATH["clearance_mm"]
A("| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |")
A("|---|---|---|")
A("| P1 | Gravity | The rail's underside sits on the plate's top face (clearance 0.0, 0.0 mm³ in common) and four "
  "M3 × 12 screws from below through the plate's Ø4.0 holes reach inserts in coaxial blind bores (axis offset "
  "0.000; section `top_asm_z-45_screw_path`). In the print it stands on its 12 × 215 rear end, centre of mass "
  "at x 65.00, over the middle of the footprint. |")
A("| P2 | Function chains | Dam: the underside is one face over x 59 … 71, z −240 … −30, holed only by the four "
  "blind bore mouths (closed by the inserts and screws). Wires: the four windows go through the wall with "
  "nothing in front of either mouth (no rib, no collar). Top panel: two blind bores open at y 215. |")
A(f"| P3 | Motion and assembly path | No moving parts. The part is lowered along −Y onto the plate: the box it "
  f"sweeps (its footprint from y 0 to y 400) keeps OD-H01 at {fmt(pc['od_h01_pump']['measured'])}, OD-C03 at "
  f"{fmt(pc['od_c03_cradle']['measured'])}, OD-C04 at {fmt(pc['od_c04_mount']['measured'])}, OD-H11 at "
  f"{fmt(pc['od_h11_thermoblock']['measured'])}, OD-G01 at {fmt(pc['od_g01_housing']['measured'])} and the carrier "
  f"box at {fmt(pc['od_c05_foot_reference_A02']['measured'])} mm (the rail passes the pump's +X end 3.5 away on the "
  "way down; the final pose keeps 7.5 at the wall face). |")
A("| P4 | Human factors | Each screw is driven from below along the bore's axis through the plate, nothing on the "
  "path (the machine turned over, A-03); the inserts are pressed from the rail's underside and the top face, "
  "both open faces. |")
A("| P5 | Next to a real product | A plain printed partition with rails and grommet windows, like a moulded "
  "appliance bulkhead; nothing a domain engineer would flag at once beyond the thin wall's stiffness (REQ-09). |")
A("| P6 | Floating, embedded, mirrored, upside-down | One solid; nothing floating; nothing embedded in a neighbour "
  "(interference 0.0 everywhere measurable); the gables point +Z, the print's up (A-10); the assembly poses are "
  "the OD-C01 joints. |")
A("")
A("## 7. Library and tools used")
A("")
A("Card: UNO10 U5 tank heat-set (size and position kept apart in U-02). Precedent: the v01 scripts of this job. "
  "Tools: `tools.core` `read_step`, `write_step` (AP242), `write_stl`, `validity`, `compare_step`, `common_volume`, "
  "`file_sha256`; `tools.measure` `envelope`, `bore_census`, `locate_bore`, `feature_census`, `min_wall`, "
  "`min_wall_wide`, `overhang_census`, `radial_extent`, `clearance`, `mass_properties`, `mesh_census`; "
  "`tools.result.gate`; `tools.drawing.write_sections`. New job code: the refilled solid for the D-03a census "
  "outside the named exception and the per-face split by position; the axis-to-axis coaxiality point; the "
  "three-ray circle for the windows' round part; the assembly path box. Missing tools: none for a gated number; "
  "D-03b has no tool (reviewer row); `bore_census` cannot see a 180° arc, so `radial_extent` reads the windows.")
A("")
A("## 8. Deviations from the plan")
A("")
A("- Geometry: none against the plan amendment v02 (itself the brief's amendments to the base plan).")
A("- Files: the v02 scripts carry `_v02` in their names and the plan amendment is a new file, so the v01 "
  "scripts and plan stay byte-identical to the v01 REPORT's hashes (the brief: leave every v01 file as it is).")
A("- Sections: the v01 cuts at x 62 (collars) and x 71 (ribs) became x 61 and x 69 (the rail flanges); added "
  "z −200 (window 1), z −210 (top bore 2), z −55 (window 4), y 3 (the base bores) and the assembly cut z −45 "
  "through the screw path.")
A("- Added after the sweep, as a diagnostic only: the assembly path probe (L-10).")
A("")
A("## 9. What I am least sure of")
A("")
least = [
    "D-01b and U-06 at margin 0.000 on the top-rail bores. The Ø4.0 bore on x 65 is exactly as wide as the wall "
    "(x 63 … 67), so the edge of its floor (y 209) lies 2.0 above the top rail's underside (y 207) along the "
    "wall-face lines; `min_wall` reads 2.000 at (63, 207, −60). A bore 6.1 deep, inside REQ-07's ±0.1, reads 1.9 "
    "and fails D-01b. The spec's D-01b row names 3.5 and 4.0 beside the bores but not this floor. A melted-in "
    "Ø4.6 insert widens the bore to x 62.7 … 67.3, over the flange, where 2.0 or more stays under it only while "
    "the bore is no deeper than 6.0.",
    "The D-03a gate reads the census on a derived solid (the six named-exception bores refilled by position), "
    "because `overhang_census` takes no region; the whole-part census reads 0° at the bore crowns, and the "
    "exception is not yet signed by the Usta. The window gables read exactly 45.0° (margin 0, planar).",
    "Three envelope rows sit on their limits by the spec's own numbers: REQ-05 min_x 59.0, REQ-08 max_x 71.0, and "
    "the carrier box at 4.0. Printed standing on z −240, the first layers' squish (elephant's foot) widens only "
    "the rear end, but any outward error on the rail's wet face breaks REQ-05 and the box clearance. The ledger "
    "text also lags §4 in two rows (A-05 names the top bores at x 67.5, A-04 window 4 at z −40); the build "
    "follows §4, REQ-07 and REQ-04 (x 65, z −55).",
]
for i, t in enumerate(least, 1):
    A(f"{i}. {t}")
A("")
A("## 10. Stop")
A("")
A("Not stopped. Fix cycles used: 0 of 3 (the nominal v02 build passed its checks on the first run).")
A("")
gates_json = []
for r in ROWS:
    gates_json.append({"gate": r["gate"], "measured": r["measured"], "unit": r.get("unit", ""),
                       "required": r["required"], "margin": r.get("margin"),
                       "at": None if r.get("at") in (None, "") else str(r.get("at")), "status": r["status"],
                       "assumes": r.get("assumes", [])})
block = {"schema": "oguz-report-v1", "job_id": "20260930-od-c02-bulkhead", "part": "od_c02_bulkhead", "tag": "v02",
         "spec_version": "1.1", "files": [{"path": p, "sha256": hashes[p]} for p in files], "versions": VERSIONS,
         "gates": gates_json,
         "sweep": [{"parameter": p["parameter"], "values": p["values"], "all_built": p["all_built"],
                    "worst_gate": p["worst_gate"], "worst_margin": p["worst_margin"],
                    "failing": p["failing"]} for p in SWP["parameters"]],
         "least_sure": least, "stopped": False}
A("```json")
A(json.dumps(block, indent=1, default=str, ensure_ascii=False))
A("```")
(HERE / "REPORT_od_c02_bulkhead_v02.md").write_text("\n".join(L) + "\n")
print("written", len(L), "lines")
for fid in SPEC_ROWS:
    w = summ.get(fid)
    print(fid, None if w is None else (w["status"], w["measured"], w.get("unit"), w["gate"]))
