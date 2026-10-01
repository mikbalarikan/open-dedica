"""D8 v01b: writes 01_CAD/REPORT_od_c10_top_v01b.md from the v01 REPORT (sections 5-7 and the
v01 file rows kept as they are: same geometry), check_od_c10_top_v01b.json, the generated gate
table (report_tables_v01b.py) and sweep_v01b/sweep_summary.json. Standard library only."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
v01 = (HERE / "REPORT_od_c10_top_v01.md").read_text()
chk = json.loads((HERE / "check_od_c10_top_v01b.json").read_text())
rows = json.loads((HERE / "report_rows_v01b.json").read_text())
table = (HERE / "check_v01b_scratch" / "table_v01b.md").read_text().strip()
sw = json.loads((HERE / "sweep_v01b" / "sweep_summary.json").read_text())
F = chk["facts"]
G = {r["gate"]: r for r in chk["gates"]}


def sha(rel):
    return hashlib.sha256((WS / rel).read_bytes()).hexdigest()


def m(g, nd=3):
    return f"{G[g]['measured']:.{nd}f}"


# section 1: the v01 rows that still describe delivered or unchanged files, then the v01b files
keep = [ln for ln in v01.split("## 1. Files", 1)[1].split("## 2.", 1)[0].splitlines() if ln.startswith("| `")]
v01_files = []
for ln in keep:
    path = ln.split("`")[1]
    if path in ("01_CAD/check_od_c10_top.py",):
        continue   # changed in v01b; its v01 text is kept as check_od_c10_top_v01.py below
    v01_files.append((path, ln.split("|")[3].strip()))
new_files = [
    ("01_CAD/check_od_c10_top_v01.py", "the v01 check script as it ran for the v01 REPORT (copy, unchanged)"),
    ("01_CAD/check_od_c10_top.py", "checks, spec 1.2: U-03 (a) OD-C11 rows rewritten (section 8)"),
    ("01_CAD/check_od_c10_top_v01b.py", "versioned copy of the line above (identical)"),
    ("01_CAD/check_od_c10_top_v01b.json", f"every gate row and fact ({len(chk['gates'])} rows)"),
    ("01_CAD/check_od_c10_top_v01b.log", "the check's printout"),
    ("01_CAD/sweep_recheck_v01b.sh", "v01b re-check driver: the v01b checks on the v01 sweep files, nothing rebuilt"),
    ("01_CAD/sweep_summary_v01b.py", "v01b sweep summary"),
    ("01_CAD/sweep_v01b/sweep_summary.json", "per run: rows not passing, worst margin per family, OD-C11 rows"),
    ("01_CAD/report_tables_v01b.py", "generates section 3 and the JSON gate rows from the v01b check JSON"),
    ("01_CAD/report_rows_v01b.json", "the JSON gate rows below"),
    ("01_CAD/report_v01b.py", "writes this REPORT"),
]
order = [p for p, _ in v01_files if not p.startswith(("02_", "03_"))] + [p for p, _ in new_files] + \
        [p for p, _ in v01_files if p.startswith(("02_", "03_"))]
notes = dict(v01_files) | dict(new_files)
files = [(p, sha(p), notes[p]) for p in order]
for p, s, n in files:   # the v01 rows' hashes must still hold
    old = [ln for ln in keep if f"`{p}`" in ln] if p not in dict(new_files) else []
    if old and s not in old[0]:
        raise SystemExit(f"hash changed since v01: {p}")
ftab = "\n".join(["| File | SHA-256 | Note |", "|---|---|---|"] + [f"| `{p}` | {s} | {n} |" for p, s, n in files])

cp = F["U-03.c11.corner_contact_area_mm2"]
v01_away = F["U-03.c11.clearance_away_line_only_v01_region"]
nominal_bad = sw["nominal"]["not_pass"]
assert not nominal_bad, nominal_bad
hard_bad = [r for r in chk["gates"] if r["status"] in ("FAIL", "INCONCLUSIVE") and r["gate"] not in ("E-06", "REQ-08(Soft)")]
assert not hard_bad, hard_bad


def np_(run):
    return sw[run]["not_pass"]


def worst(prefix_runs, gate_prefix):
    best = None
    for run in prefix_runs:
        for r in json.loads((HERE / "sweep_v01b" / run / "check.json").read_text())["gates"]:
            if r["gate"].startswith(gate_prefix) and r.get("margin") is not None:
                if best is None or r["margin"] < best[1]["margin"]:
                    best = (run, r)
    return best


sk_hi, sk_lo = np_("skirt_bottom_y_hi"), np_("skirt_bottom_y_lo")
sk_hi_c = [r for r in sk_hi if "corner" in r["gate"]][0]["measured"]
sk_lo_i = [r for r in sk_lo if r["gate"] == "U-03.c11.interference"][0]["measured"]
sk_lo_c = [r for r in sk_lo if r["gate"] == "U-03.c11.corner_x+.interference"][0]["measured"]
away_min = min(json.loads((HERE / "sweep_v01b" / r / "check.json").read_text()) and
               [g["measured"] for g in json.loads((HERE / "sweep_v01b" / r / "check.json").read_text())["gates"]
                if g["gate"] == "U-03.c11.clearance_away"][0] for r in sw)
outside_max = max([g["measured"] for g in json.loads((HERE / "sweep_v01b" / r / "check.json").read_text())["gates"]
                   if g["gate"] == "U-03.c11.contact_area_outside_designed_regions"][0] for r in sw)
same_step = all(v["step_unchanged"] for v in sw.values())

v01_sec3 = v01.split("## 3. Gate self-check", 1)[1].split("Every row as measured:", 1)[0]
summary = v01_sec3.split("Summary by §5 row:", 1)[1].strip()
u03_new = (f"| U-03 | PASS (assumed: A-01, A-02, A-03) | (a) column seats 0.000 / 0.000 mm³, coaxial 0.000; OD-C05 "
           f"{m('U-03.c05.clearance')} (pads); OD-C07 {m('U-03.c07.clearance')}; OD-C01 {m('U-03.plate.clearance')}; "
           f"OD-C02 away {m('U-03.c02.clearance_away')}; OD-C11: designed contact (line along x ±116 and the two "
           f"corner patches) clearance {m('U-03.c11.clearance_contact')}, interference {m('U-03.c11.interference')} mm³, "
           f"corner patches {cp['x+']:.3f} and {cp['x-']:.3f} mm² (each corner clearance 0.000, interference 0.000 mm³), "
           f"contact outside the designed regions {m('U-03.c11.contact_area_outside_designed_regions')} mm²; "
           f"away from the whole contact region {m('U-03.c11.clearance_away')} ≥ 0.5. (b) descent from +40 in 2.0 "
           f"steps: 0.000 mm³ with every reference at every step |")
summary = "\n".join(u03_new if ln.startswith("| U-03 |") else ln for ln in summary.splitlines())

s567 = v01.split("## 5. Build facts", 1)[1].split("## 8. Deviations", 1)[0]
s567 = s567.replace("and on the rear skirt's bottom edge on OD-C11's wall.",
                    "and on the rear skirt's bottom on OD-C11's wall top (the edge along x ±116 and the two corner "
                    "patches, spec 1.2).")
s567 = s567.replace("exclusion volumes on the measured column axes, pads and rear skirt for U-03 (a);",
                    "exclusion volumes on the measured column axes, pads, rear skirt and its R 10 corner arcs for "
                    "U-03 (a);")

sweep_rows = [
    ("hole_d", "3.3 · 3.4 · 3.5", "D-04a (at 3.3)", "+0.05 mm; REQ-03/04 hole_d at the band edge (0.000)"),
    ("cbore_d", "6.4 · 6.5 · 6.6", "D-01b / U-06 (at 6.6)", "+0.70 mm (wall 2.70)"),
    ("cbore_floor_y", "217.9 · 218.0 · 218.1", "REQ-03/04 cbore_floor_y", "0.000 (band edge); REQ-07 driver 0.000 mm³"),
    ("col_dx, col_dz", "−0.1 · 0 · +0.1", "REQ-03/04 offsets; U-03 coaxial",
     "0.000 (offset 0.100 at the 0.10 limit); the new `contact_area_outside_designed_regions` 0 mm² in all four"),
    ("col_bottom_y", "214.95 · 215.0 · 215.05", "U-03 seats (designed contacts)",
     "**passes only at nominal**: at 215.05 each seat reads clearance 0.050 (required = 0); at 214.95 each column "
     "overlaps its seat by 4.87 (OD-C02) and 5.03 mm³ (OD-C11)"),
    ("pad_bottom_y", "210.45 · 210.5 · 210.55", "REQ-05 / U-03 clearance to OD-C05", "0.000 (0.450 and 0.550 at the band edges)"),
    ("skirt_bottom_y", "214.9 · 215.0 · 215.1", "U-03 OD-C11 corner patches (designed contact)",
     f"**passes only at nominal**: at 215.1 each corner reads clearance {sk_hi_c:.3f} (required = 0); at 214.9 the "
     f"skirt overlaps OD-C11's wall by {sk_lo_i:.3f} mm³ ({sk_lo_c:.3f} per corner patch). "
     f"`clearance_away` holds at 1.000 there and in every run"),
]
stab = "\n".join(["| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin |",
                  "|---|---|---|---|---|"] + [f"| {a} | {b} | yes | {c} | {d} |" for a, b, c, d in sweep_rows])

jfiles = [{"path": p, "sha256": s} for p, s, _ in files]
v01json = json.loads(re.search(r"```json\n(.*?)\n```", v01, re.S).group(1))
sweep_json = v01json["sweep"]
for e in sweep_json:
    if e["parameter"] == "skirt_bottom_y":
        e["worst_gate"] = "U-03.c11.interference (corner patches, designed contact)"
        e["worst_margin"] = round(-sk_lo_i, 4)
J = {"schema": "oguz-report-v1", "job_id": "20261001-od-c10-top-panel", "part": "od_c10_top", "tag": "v01b",
     "geometry_tag": "v01", "spec_version": "1.2", "files": jfiles, "versions": v01json["versions"],
     "gates": rows, "sweep": sweep_json,
     "least_sure": ["REQ-08 stiffness: 3.0 PETG skin held at x 65 and the rear only, left and front edges free until "
                    "OD-C09/C12/C13 exist",
                    "The OD-C11 reference is its unreviewed build v02; the corner patches follow its wall",
                    "The ribs are a design choice derived from clearances, not a load case; a 5.0 pocket behind each "
                    "rear column"],
     "stopped": False}

text = f"""# REPORT — od_c10_top v01b (20261001-od-c10-top-panel)

Designer: Claude Code (Claude Agent SDK), claude-opus-5-5 · spec version 1.2 · plan `01_CAD/DESIGN_PLAN.md` · 2026-10-01 UTC · brief `briefs/WP-03_designer.md` (check-only, build attempt 2 of 2)

Outcome: **SUBMITTED**. This is a re-check of build v01 as built. Nothing geometric was changed or
re-exported. The part STEP is `0f85c4d7…` and the assembly STEP `d5881320…`, the same as in
the v01 REPORT. They were re-hashed before and after the run, and the check JSON records the
hash it measured. Spec 1.2 widens U-03 (a)'s designed contact on OD-C11. It now covers the
line along x ±116 and also the rear skirt's bottom face over its R 10 corner arcs at
x ±110 … ±116. The checks were updated to match (section 8) and re-run on every row. Every
Hard row passes, or is N/A or INCONCLUSIVE by its own row (E-06 belongs to the reviewer;
REQ-08 is a Soft bench row). The OD-C11 reference is still its **unreviewed** build v02 STEP.
The v01 REPORT is kept unchanged as `01_CAD/REPORT_od_c10_top_v01.md`.

## 1. Files

{ftab}

The 3MF is the orchestrator's step. The STL is unchanged from v01: 5164 triangles, volume
433996.82 mm³ (B-rep 434010.64 mm³), bbox 240 × 39.5 × 405 mm (x −120 … 120, y 210.5 … 250,
z −305 … 100).

## 2. Versions

Python 3.13.7 · build123d 0.11.1 · OCP (cadquery-ocp-novtk) 7.9.3.1.1 · tools venv as
pinned (`tools/uv.lock`) · repo commit 10929db1408d89144bd4af9cad971440427933d0 (re-read for v01b)

## 3. Gate self-check

These rows are generated from `01_CAD/check_od_c10_top_v01b.json` (`report_tables_v01b.py`).
They were measured on the re-imported STEP files (`02_STEP_STL/od_c10_top_C1_v01.step` and
`od_c10_assembly_C1_v01.step`). Bands (GATES.md §0): mm 0.005, mm³ 0.001, deg 0.001,
rad 0.00002, counts and every other unit 0. A self-check clears no HARD gate.

Summary by §5 row:

{summary}

U-03 (a) on OD-C11, as spec 1.2 words it:
- Designed contact: the whole lid's clearance to OD-C11 is {m('U-03.c11.clearance_contact')}, nearest at
  (−110.0, 215.0, −302.0), with interference {m('U-03.c11.interference')} mm³. Each corner arc piece
  (|x| ≥ 109.95, z ≤ −294.95) reads clearance 0.000 and interference 0.000 mm³.
- The corner patches' area (face intersection at y 215, reported because the spec sets no limit)
  is x+ {cp['x+']:.3f} mm² and x− {cp['x-']:.3f} mm², each at x ±110 … ±116 and z −302 … −299.
  Spec 1.2 gives about 5.9.
- Contact patches at y 215 outside the column seats (r 6.05 about the measured axes) and the
  corner regions: {m('U-03.c11.contact_area_outside_designed_regions')} mm².
- Away from the whole contact region: {m('U-03.c11.clearance_away')} ≥ 0.5 (margin
  {G['U-03.c11.clearance_away']['margin']:.3f}). This is the lid less its column volumes, less the
  rear skirt behind z −301.95, and less the two corner arcs, measured against OD-C11. The nearest
  point is (−95.5, 216.0, −301.95): a rear rib's bottom at y 216, 1.0 above OD-C11's ledge.
- For comparison, the v01 exclusion (line only, no corner arcs) still reads
  {v01_away['measured']:.3f} at ({v01_away['at'][0]:.2f}, {v01_away['at'][1]:.1f}, {v01_away['at'][2]:.2f}).
  It is kept as a fact, not a gate.

Every row as measured:

{table}

## 4. Robustness sweep (D7)

No geometry change, so nothing was rebuilt. The v01b checks ran on the 17 v01 sweep files
(`01_CAD/sweep_v01/<run>/`; each STEP re-hashed against its build record, {'all 17 unchanged' if same_step else 'NOT ALL UNCHANGED'}). The results are in `01_CAD/sweep_v01b/<run>/check.json`. Every run is one
valid solid with 81 faces. Across all runs, `U-03.c11.clearance_away` is never below
{away_min:.3f} and the contact area outside the designed regions is never above {outside_max:g} mm².
Outside the two rows below, no run has a row that does not pass.

{stab}

Designed contacts (clearance = 0) pass only at nominal. That is in the nature of a contact
row, the same as in v01. A skirt or column printed 0.05 to 0.1 off still seats under the screw clamp.

## 5. Build facts
{s567}## 8. Deviations from the plan

1. to 4. As in the v01 REPORT §8: check-script corrections and fix cycle 1 of 3, with no
   geometry change.
5. **v01b, check only (WP-03).** The U-03 (a) OD-C11 rows were rewritten for spec 1.2:
   - `clearance_line_contact` became `U-03.c11.clearance_contact` (same measurement, the
     whole lid against OD-C11 = 0).
   - `clearance_away` now also sets aside the rear skirt's two R 10 corner arcs
     (|x| ≥ 110 − 0.05, z ≤ −295 + 0.05). That is the arcs' tangent points from §4,
     with the same 0.05 margin v01 used for the line.
   - New rows: `corner_x±.clearance` (== 0), `corner_x±.interference` (≤ 0) and
     `contact_area_outside_designed_regions` (≤ 0 mm²).
   - The v01 row `skirt_contact_area_off_the_line` is removed. Its patches are now
     designed contact, and their area is reported as a fact.
   - Every threshold is from spec 1.2 §5. The v01 script is kept as
     `check_od_c10_top_v01.py`.
6. **Fix cycle 2 of 3 (check only, no geometry change, nothing re-exported).** The first
   v01b sweep re-check (kept as `01_CAD/sweep_v01b_try1/`) showed that the new
   `contact_area_outside_designed_regions` set the rear column seats aside by their nominal
   positions. In the col_dx and col_dz runs it therefore counted the seat patches
   (201.06 mm²) as outside contact. It now uses the measured column axes. The nominal check
   and all 17 sweep re-checks were then re-run. All the numbers above come from the corrected
   script.
7. Changes to `check_od_c10_top.py` are confined to the U-03 (a) OD-C11 rows and the spec
   1.2 wording in its header. Every other row's measured value and status is identical to
   v01. 240 rows are shared with v01; the only change among them is `U-03.c11.clearance_away`,
   from 0.000 FAIL to 1.000 PASS.

## 9. What I am least sure of

1. **Stiffness (REQ-08, A-11).** A 3.0 PETG skin of 240 × 405 is held at x 65 and along the
   rear only, and its left and front edges stay free until OD-C09/C12/C13 exist. The left half
   overhangs about 185 mm beyond the bulkhead line, with only the 32 mm skirt for depth. Sag
   and rattle risk at the free left-front corner: HIGH until the side and front panels land.
2. **The OD-C11 reference is unreviewed (build v02).** The corner patches, the line contact and
   the rear seats all follow its wall and ledge as they measure today. If OD-C11's wall top or its
   x ±116 end changes, U-03 (a) has to be measured again against the new STEP.
3. **The ribs are my design choice.** They are derived in plan §4 from clearances; no load case
   sizes them. Each rear column has a closed 5.0-wide pocket behind it. The reviewer should
   judge E-06 from `od_c10_top_col_z-60_v01_top.png`, `od_c10_top_plan_y230_v01_front.png` and
   `od_c10_top_rearrib_x94_v01_left.png`.

## 10. The Usta's answer to the v01 stop

The v01 REPORT stopped on U-03 (a): the rear skirt's corner arcs rest on OD-C11's wall top
over two patches of 5.907 mm² each, off the named line contact. The Usta accepted option 1
(decision card, 2026-10-01 13:06Z; spec change log row). Spec 1.2 names those patches as part
of U-03 (a)'s designed contact (`clearance = 0`, `interference ≤ 0`). No §4 value changes and
no geometry changes. Measured against 1.2, U-03 (a) passes (section 3). Nothing is stopped.

```json
{json.dumps(J, ensure_ascii=False)}
```
"""
(HERE / "REPORT_od_c10_top_v01b.md").write_text(text)
print("written", len(text))
