import json
from pathlib import Path
R = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle/reviews")
d = json.load(open(R/"RV02_od_c03_cradle_v02.json"))
ST = {"PASS": "PASS", "PASS_ASSUMED": "PASS (assumed: {})", "FAIL": "FAIL", "INCONCLUSIVE": "INCONCLUSIVE", "NOT_APPLICABLE": "N/A: {}"}
def fmt(v):
    if v is None: return "—"
    if isinstance(v, float) and v != 0 and abs(v) < 1e-6: return f"{v:.1e}"
    if isinstance(v, float): return f"{v:+.3f}".rstrip("0").rstrip(".") if False else f"{v:.5g}"
    return str(v)
def sgn(v):
    if v is None: return "—"
    if v != 0 and abs(v) < 1e-6: return f"{v:+.1e}"
    return f"{v:+.5g}"
L = []
L += ["# RV02 — od_c03_cradle_v02 (20260930-od-c03-pump-cradle) — 2026-09-30 UTC", "",
 "Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted",
 "Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with the WP-03 and WP-05 amendments) · report `01_CAD/REPORT_od_c03_cradle_v02.md`", "",
 "**VERDICT: APPROVED (assumption-conditional)**",
 "Blocking findings: 0 · open assumptions relied on: " + ", ".join(d["assumptions_relied_on"]), "",
 d["summary"], "",
 "Method: every row re-measured with `tools.measure` / `tools.core` on the delivered STEP files, re-imported (`reviews/RV02_work/checks.py`, `run_gates.py`, `m1`…`m6`), compared through `tools.result.gate` with the GATES.md §0 bands (0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts). No designer script, sweep file or check JSON value was used as evidence. OD-H01 read sound (1/1/0).", "",
 "## 1. Files reviewed", "", "| File | SHA-256 | Matches REPORT |", "|---|---|---|"]
for f in d["files"]:
    note = "yes" if f["matches_report"] else "NO"
    if f["path"] in ("01_CAD/REPORT_od_c03_cradle_v02.md", "01_CAD/DESIGN_PLAN.md", "00_Spec/inputs/OD-H01_ulka_ep5_pump.step"):
        note += " (brief; the REPORT does not list its own or the plan's hash)" if not f["path"].startswith("00_") else " (brief and REPORT §1)"
    L.append(f"| `{f['path']}` | {f['sha256']} | {note} |")
L += ["", "Completeness: every §5 row is answered in the REPORT and every listed file is present with a matching SHA-256. The delivered STL is byte-identical to a fresh `write_stl` of the delivered STEP at 0.01 mm / 0.1 rad (SHA-256 529a0cc2…6be4).", "",
 "## 2. Gate table", "", "| Gate | Measured | Required | Margin | At | Status | Method | Assumes |", "|---|---|---|---|---|---|---|---|"]
for g in d["gates"]:
    st = g["status"]
    s = ST[st].format(", ".join(g["assumes"])) if st == "PASS_ASSUMED" else (ST[st].format("by its row") if st == "NOT_APPLICABLE" else st)
    if g["gate"] == "REQ-09": s = "INCONCLUSIVE (Soft: bench, non-blocking)"
    if g["gate"] == "U-06": s = "PASS (Soft)"
    m = "—" if g["measured"] is None else f"{fmt(g['measured'])} {g['unit']}"
    L.append(f"| {g['gate']} | {m} | {g['required']} | {sgn(g['margin'])} | {g['at'] or '—'} | {s} | `{g['method']}` | {', '.join(g['assumes']) or '—'} |")
L += ["", "U-03 (b): no motion variable (ties not modelled). The assembly path was checked anyway: OD-H01 with the sleeve lowered along +Y from 60 mm above to the final pose keeps ≥ 2.300 mm to the cradle and 0.0 mm³ at every step (−60 … 0 mm), and the sleeve first touches the saddles at the final pose.", "",
 "## 3. Feature census against the plan", "", "| Plan feature | Expected | Found | Status |", "|---|---|---|---|"]
for c in d["feature_census"]:
    L.append(f"| {c['feature']} | {c['expected']} | {c['found']} | {c['status']} |")
L += ["", "## 4. Plausibility (`GATES.md` §P, one line each)", "", "| # | Question | Answer | Status |", "|---|---|---|---|"]
Q = {"P1": "Gravity: does every part rest and mount the way the product is used?", "P2": "Function chains connected and aimed (air, drive, liquid, cable)?",
     "P3": "Moving parts oriented for their motion, with clearance?", "P4": "Human factors: grip, reach, insertion direction obvious?",
     "P5": "Next to a comparable real product, does anything look absurd?", "P6": "Nothing floating, embedded, mirrored, or upside-down?"}
for p in d["plausibility"]:
    k = p["question"][:2]; L.append(f"| {k} | {Q[k]} | {p['answer']} | {p['status']} |")
L += ["", "Sections used (reviewer's own, `reviews/RV02_work/sections/`, each `nothing_clipped` 0; numeric outlines in `m3_sections.json`): cradle XY at z 0, 17, 28; YZ at x 0 and 31.5; XZ at y 7; check assembly XY at z 0, 17, 28 and YZ at x 0.", "",
 "## 5. Positive controls", "", "| Check | Mutant of this job's part | Got |", "|---|---|---|"]
for c in d["positive_controls"]:
    L.append(f"| {c['check']} | {c['mutant']} | {c['got']} |")
L += ["", "Every mutant was made from the delivered STEP by my own script (`RV02_work/controls.py`, results in `controls.json`) and run through the same predicate code as the gate table. The first bridge-span control (a 7.0 × 4.0 flat pocket) passed a metric that took the smaller face size; the metric was corrected to the larger size (conservative) and both the control and the gate table were re-run: the control now FAILs and the delivered part still reads 0.0 (no flat downward face).", "",
 "## 6. Findings", "", "| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |", "|---|---|---|---|---|---|---|---|---|---|"]
for f in d["findings"]:
    m = "not measured" if f["measured"] is None else f"{fmt(f['measured'])} {f['unit']}"
    L.append(f"| {f['id']} | {f['gate']} | {f['kind']} | {m} → {f['required']} | {sgn(f['margin'])} | {f['at'] or '—'} | {'yes' if f['blocks'] else 'no'} | {f['risk']} | {f['risk_basis']} | {f['fix_direction']} |")
L += ["", "RV01 findings in this round (brief): F1 (REQ-09) is now a Soft row, carried here as F1 SOFT_GATE_MISS, UNKNOWN, non-blocking. RV01 F2 (centre of mass ahead of the saddles) is answered: rib 1 measures z −3.000 … 3.000 and the OD-H01 centroid z 7.232 lies inside the span z −3.0 … 31.0, no finding. RV01 F3 → F2 here (MEDIUM, A-07), F4 → F3 (MEDIUM, A-03, now with the coil-radius evidence), F5 → F4 (MEDIUM, A-01, A-04), F6 → F5 (LOW, the spec's own zero-margin values); F6 here records the sleeve model's overlap with OD-H01 (LOW).", "",
 "Tool note (not a part finding): `tools.measure.min_wall` still reports `detail['solids'] = 4` on this one-solid part; the measured wall is unaffected (`validity` reads solid_count 1).", "",
 "## 7. \"Least sure of\", answered", "", "| REPORT item | What the review found |", "|---|---|"]
for a in d["least_sure_answers"]:
    L.append(f"| {a['item']} | {a['answer']} |")
def fix(line):
    if not line.startswith("| ") or line.startswith("|---"): return line
    cells = line[2:-2].split(" | ")
    return "| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |"
(R/"RV02_od_c03_cradle_v02.md").write_text("\n".join(fix(x) for x in L) + "\n")
print("ok")
