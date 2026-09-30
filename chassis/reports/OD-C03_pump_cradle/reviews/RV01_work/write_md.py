import json
from pathlib import Path
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
V = json.load(open(W/"reviews/RV01_work/verdict_data.json"))
def fmt(v):
    if v is None: return "—"
    if isinstance(v, float):
        if v != 0 and abs(v) < 1e-3: return f"{v:.1e}"
        return f"{v:.3f}".rstrip("0").rstrip(".") if abs(v) < 1000 else f"{v:.1f}"
    return str(v)
def sgn(v):
    if v is None: return "—"
    s = fmt(v); return s if s.startswith("-") or s == "0" else "+" + s
st = {"PASS": "PASS", "PASS_ASSUMED": None, "FAIL": "FAIL", "INCONCLUSIVE": "INCONCLUSIVE", "NOT_APPLICABLE": "N/A: by its row (no threads / no fit bores on this part)"}
L = []
L.append("# RV01 — od_c03_cradle_v01 (20260930-od-c03-pump-cradle) — 2026-09-30 UTC\n")
L.append("Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted")
L.append("Spec 1.1 · plan `01_CAD/DESIGN_PLAN.md` (with the amendments of `briefs/WP-03_designer.md`) · report `01_CAD/REPORT_od_c03_cradle_v01.md`\n")
L.append("**VERDICT: REVISE**")
L.append("Blocking findings: 1 (F1, REQ-09 HARD_GATE_INCONCLUSIVE, bench gate) · open assumptions relied on: " + ", ".join(V["assumptions_relied_on"]) + "\n")
L.append("Every geometric §5 row re-measures PASS or PASS (assumed) from the exported files. The one blocking finding is REQ-09. It is a Hard row that only a bench run can answer. By rule an INCONCLUSIVE Hard gate blocks, and no rebuild of the geometry can clear it. The decision on it is the Usta's (F1). Findings F2 to F6 are non-blocking observations, rated MEDIUM or LOW. They are for the Usta to accept knowingly.\n")
L.append("Tolerance bands (GATES §0 as the plan carries them): 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts and 1/0 facts. Every comparison goes through `tools.result.gate`. Reviewer scripts, mutants and sections are in `reviews/RV01_work/` (`checks.py` is the one gate code, run on the delivery and on every mutant).\n")
L.append("## 1. Files reviewed\n")
L.append("| File | SHA-256 | Matches REPORT |\n|---|---|---|")
for f in V["files"]:
    L.append(f"| `{f['path']}` | {f['sha256']} | {'yes' if f['matches_report'] else 'NO'} |")
L.append("\nAll hashes match the brief and REPORT §1 (the OD-H01 input matches the brief). Completeness: every §5 row is answered in the REPORT and every listed file is present. The delivered STL is byte-identical to a fresh `write_stl` of the delivered STEP at 0.01 mm / 0.1 rad.\n")
L.append("## 2. Gate table\n")
L.append("| Gate | Measured | Required | Margin | At | Status | Method | Assumes |\n|---|---|---|---|---|---|---|---|")
for g in V["gates"]:
    s = g["status"]
    s = f"PASS (assumed: {', '.join(g['assumes'])})" if s == "PASS_ASSUMED" else ("N/A: by its row" if s == "NOT_APPLICABLE" else s)
    m = "—" if g["measured"] is None else f"{fmt(g['measured'])} {g['unit']}"
    L.append(f"| {g['gate']} | {m} | {g['required']} | {sgn(g['margin'])} | {g['at'] or '—'} | {s} | `{g['method']}` | {', '.join(g['assumes']) or '—'} |")
L.append("\nMotion and assembly: there is no motion variable (U-03 b, ties not modelled). I checked the assembly path by moving OD-H01 and the sleeve along +Y from −60 mm to the final pose. The clearance to OD-H01 falls to 2.300 at Δy −10 mm and stays there. The sleeve first touches the saddles at the final pose (6.000 at −10, 0.071 at −0.1, 0 at 0).\n")
L.append("## 3. Feature census against the plan\n")
L.append("| Plan feature | Expected | Found | Status |\n|---|---|---|---|")
for c in V["feature_census"]:
    L.append(f"| {c['feature']} | {c['expected']} | {c['found']} | {c['status']} |")
L.append("\n## 4. Plausibility (`GATES.md` §P, one line each)\n")
L.append("| # | Question | Answer | Status |\n|---|---|---|---|")
Q = {"P1": "Gravity: does every part rest and mount the way the product is used?", "P2": "Function chains connected and aimed (air, drive, liquid, cable)?",
     "P3": "Moving parts oriented for their motion, with clearance?", "P4": "Human factors: grip, reach, insertion direction obvious?",
     "P5": "Next to a comparable real product, does anything look absurd?", "P6": "Nothing floating, embedded, mirrored, or upside-down?"}
for p in V["plausibility"]:
    k = p["question"].split()[0]
    L.append(f"| {k} | {Q[k]} | {p['answer']} | {p['status']} |")
L.append("\nEvidence: my own sections in `reviews/RV01_work/sections/` (assembly at z 18.0 and x 0.0, cradle at x −31.5). I also cut numeric sections through the B-rep at z 18/23/28, x 0/±31.5/34 and y 7/38.5 (`m3_rows.json`). The radial probes of OD-H01 over the tie bands and the driver cylinders are in `m4_pump.py`.\n")
L.append("## 5. Positive controls\n")
L.append("| Check | Mutant of this job's part | Got |\n|---|---|---|")
for c in V["positive_controls"]:
    L.append(f"| {c['check']} | {c['mutant']} | {c['got']} |")
L.append("\nEvery mutant is built from the delivered STEP by `reviews/RV01_work/controls.py`, using a fresh read each time, and run through the same `checks.run`. M04 to M06 plug the hole with a 5 mm cylinder, which also stands 1 mm proud of the underside. Their size_y and REQ-08 fails are that side effect. The targeted rows (bores 3, offset 0.500, diameter 3.1) fail as intended.\n")
L.append("## 6. Findings\n")
L.append("| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |\n|---|---|---|---|---|---|---|---|---|---|")
for f in V["findings"]:
    m = "not measured" if f["measured"] is None else f"{fmt(f['measured'])} {f['unit']}"
    L.append(f"| {f['id']} | {f['gate']} | {f['kind']} | {m} → {f['required']} | {sgn(f['margin'])} | {f['at'] or '—'} | {'yes' if f['blocks'] else 'no'} | {f['risk']} | {f['risk_basis']} | {f['fix_direction']} |")
L.append("\nTool note (not a part finding): `tools.measure.min_wall` reports `detail['solids'] = 4` on this one-solid part. In `wall.py` the loop variable `found` is re-bound to the ray-hit tuple before `len(found)` is taken. The measured wall is not affected: `validity` reads solid_count 1.\n")
L.append("## 7. \"Least sure of\", answered\n")
L.append("| REPORT item | What the review found |\n|---|---|")
for a in V["least_sure_answers"]:
    L.append(f"| {a['item']} | {a['answer']} |")
(W/"reviews/RV01_od_c03_cradle_v01.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("ok")
