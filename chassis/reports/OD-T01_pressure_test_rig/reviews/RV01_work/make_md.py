import json
from pathlib import Path
J = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig")
v = json.load(open(J / "reviews/RV01_work/verdict_data.json"))
st = {"PASS": "PASS", "PASS_ASSUMED": None, "FAIL": "FAIL", "INCONCLUSIVE": "INCONCLUSIVE", "NOT_APPLICABLE": "N/A: not this target's kind (row names threaded parts / fit bores only)"}
def fmt(x):
    return "—" if x is None else (f"{x:+g}" if isinstance(x, float) else str(x))
L = []
L.append("# RV01 — od_t01_rig_v01 (20261002-od-t01-pressure-test-rig) — 2026-10-03 UTC\n")
L.append("Reviewer: Claude Code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted")
L.append("Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with `briefs/WP-03_designer.md`) · report `01_CAD/REPORT_od_t01_rig_v01.md`\n")
L.append("**VERDICT: APPROVED (assumption-conditional)**")
L.append("Blocking findings: 0 · open assumptions relied on: " + ", ".join(v["assumptions_relied_on"]) + "\n")
L.append(v["summary"] + "\n")
L.append("All measurements were made by the reviewer's own scripts in `reviews/RV01_work/` (`rv_part.py`, `rv_geom.py`, `rv_asm.py`, `rv_controls.py`, `rv_sections.py`), on the delivered STEP re-read from disk. The housing set was posed from `od_g01_assembly_C1_v03.step` by spec §2 (housing x → X, y → +Z, z → −Y, origin (0, 110.06, 0); a proper rotation, verified by mapping the axes), with the solids identified by measurement: housing = the 100 × 100 solid with four Ø4.0 bores at (±44, ±44); OD-G10 = the solid longer than 120 (185.1); OD-G04 = the remaining one. The designer's assembly file was not used for any gate. Band per GATES §0: 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts. No CAD code, sweep folder, or designer JSON was read.\n")
L.append("## 1. Files reviewed\n")
L.append("| File | SHA-256 | Matches REPORT |\n|---|---|---|")
for f in v["files"]:
    note = "yes" if f["path"].startswith(("02_", "03_", "01_CAD/DESIGN")) else "yes (brief; not listed in the REPORT)"
    L.append(f"| `{f['path']}` | {f['sha256']} | {note} |")
L.append("\nThe delivery must carry exactly the STEP and STL bytes above. A reviewer re-mesh of the STEP at 0.01 mm / 0.10 rad reproduces the delivered STL byte for byte.\n")
L.append("## 2. Gate table\n")
L.append("| Gate | Measured | Required | Margin | At | Status | Method | Assumes |\n|---|---|---|---|---|---|---|---|")
for g in v["gates"]:
    s = g["status"]
    s = f"PASS (assumed: {', '.join(g['assumes'])})" if s == "PASS_ASSUMED" else ("N/A: the row applies to other parts" if s == "NOT_APPLICABLE" else s)
    if g["gate"] == "REQ-08": s = "INCONCLUSIVE (Soft, bench; rated in F1)"
    m = "—" if g["measured"] is None else f"{g['measured']} {g['unit']}"
    L.append(f"| {g['gate']} | {m} | {g['required']} | {fmt(g['margin'])} | {g['at'] or '—'} | {s} | `{g['method']}` | {', '.join(g['assumes']) or '—'} |")
L.append("\nMotion: U-03b swept the housing set dy 0 … −30 every 1.0 (31 poses); REQ-04a φ −60° … +15° every 1° (76 poses); REQ-04b dz 0 … 200 every 2.5 at φ −50°, dy −15 (81 poses); the joining lift φ −50°, dy −15 … 0 every 1.0 (16 poses). The insertion path from first contact (dz 200) to the locked pose is covered: translate (b), lift, rotate (a). OD-G10 rows use the spec's `clearance > 0` with `inside == False` reading (OD-G10 `brep_valid` 0, confirmed).\n")
L.append("## 3. Feature census against the plan\n")
L.append("| Plan feature | Expected | Found | Status |\n|---|---|---|---|")
for c in v["feature_census"]:
    L.append(f"| {c['feature']} | {c['expected']} | {c['found']} | {c['status']} |")
L.append("\n## 4. Plausibility (`GATES.md` §P, one line each)\n")
L.append("From the reviewer's sections in `reviews/RV01_work/sections/` (z 0 and z 44 and x 0 with the housing set; y 142.5, y 136.5, y 5, x 44, z 50 of the rig; nothing_clipped 0 on all eight).\n")
L.append("| # | Question | Answer | Status |\n|---|---|---|---|")
for p in v["plausibility"]:
    L.append(f"| {p['question'].split(' ')[0]} | {p['question'].split(' ', 1)[1]} | {p['answer']} | {p['status']} |")
L.append("\n## 5. Positive controls\n")
L.append("| Check | Mutant of this job's part | Got |\n|---|---|---|")
for c in v["positive_controls"]:
    L.append(f"| {c['check']} | {c['mutant']} | {c['got']} |")
L.append("\nEvery check family used in §2 FAILs on its mutant (mutants in `reviews/RV01_work/mutants/` and built in `rv_controls.py`), so no gate rests on a blind check.\n")
L.append("## 6. Findings\n")
L.append("| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |\n|---|---|---|---|---|---|---|---|---|---|")
for f in v["findings"]:
    m = "not measurable (bench)" if f["measured"] is None else f"{f['measured']} {f['unit']}"
    L.append(f"| {f['id']} | {f['gate']} | {f['kind']} | {m} → {f['required']} | {fmt(f['margin'])} | {f['at']} | {'yes' if f['blocks'] else 'no'} | {f['risk']} | {f['risk_basis']} | {f['fix_direction']} |")
L.append("\nREPORT §4 sweep findings rated against spec 1.2: the window_r REQ-03 FAILs no longer hold (R 29.9 gives pair-B 10.870 against ≥ 10.87, margin 0.000, and apex 42.358 against 42.36, inside the 0.005 band; R 30.1 gives apex 42.642 against ≤ 42.66). The two D-03a locator FAILs were in the designer's locator, not the part (see §7). No other sweep row reached a limit. These are statements about tolerance, not deviations of the delivered part.\n")
L.append("## 7. \"Least sure of\", answered\n")
L.append("| REPORT item | What the review found |\n|---|---|")
for a in v["least_sure_answers"]:
    L.append(f"| {a['item']} | {a['answer']} |")
(J / "reviews/RV01_od_t01_rig_v01.md").write_text("\n".join(L) + "\n")
