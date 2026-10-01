import json
from pathlib import Path
JOB = Path("/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount")
D = json.loads((JOB / "reviews/RV01_od_c07_mount_v01.json").read_text())
ST = {"PASS": "PASS", "FAIL": "FAIL", "INCONCLUSIVE": "INCONCLUSIVE"}
def st(g):
    if g["status"] == "PASS_ASSUMED": return "PASS (assumed: " + ", ".join(g["assumes"]) + ")"
    if g["status"] == "NOT_APPLICABLE": return "N/A: by its row"
    return g["status"]
def num(x): return "—" if x is None else (f"{x:g}" if isinstance(x, (int, float)) else str(x))
def cell(s): return str(s).replace("|", "/")
L = []
L.append(f"# RV01 — od_c07_mount_v01 (20260930-od-c07-valve-flowmeter-mount) — 2026-09-30 UTC\n")
L.append("Reviewer: claude-code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted")
L.append("Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with `briefs/WP-03_designer.md`, `briefs/WP-04_designer.md`) · report `01_CAD/REPORT_od_c07_mount_v02.md`\n")
L.append("**VERDICT: REVISE**")
L.append("Blocking findings: 4 (F1–F4, arising from two geometric deviations) · open assumptions relied on: " + ", ".join(D["assumptions_relied_on"]) + "\n")
L.append(D["summary"] + "\n")
L.append("Method. Every row was re-measured on `02_STEP_STL/od_c07_mount_C1_v01.step` as re-read, with OD-H24 placed at mount + (0, 0, 10.0) and OD-H22 at mount + (62.0, 0, 48.0) (spec §2). The assembly STEP holds the same three solids at the same places (volumes and bounding boxes identical to my placement). Bands (GATES §0): mm 0.005, deg 0.001, mm³ 0.001, counts 0. No designer script was read. My scripts, logs and sections are in `reviews/RV01_work/`.\n")
L.append("Contact neighbourhoods. The spec does not define \"away from the designed contacts\". I took the OD-H24 rim contact as A-06's rim annulus r 13.98 … 15.71 up to z_H24 0.3, the height where the rim's edge rounds end (measured). I took the OD-H22 flange contact as everything at or above its flange back face. REPORT v02 cut OD-H24 wider, at r 13.68 … 16.21 up to z_H24 0.5. That cut removes the rib ends and the cup's foot, and with them the two gaps in F1–F4.\n")
L.append("## 1. Files reviewed\n")
L.append("| File | SHA-256 | Matches REPORT |\n|---|---|---|")
for f in D["files"]: L.append(f"| `{f['path']}` | {f['sha256']} | {'yes' if f['matches_report'] else 'NO'} |")
L.append("\nEvery other file REPORT v02 §1 lists (scripts, logs, check JSON, probes) also matches its SHA-256; I hashed them only and read none of the scripts.\n")
L.append("## 2. Gate table\n")
L.append("| Gate | Measured | Required | Margin | At | Status | Method | Assumes |\n|---|---|---|---|---|---|---|---|")
for g in D["gates"]:
    L.append(f"| {g['gate']} | {num(g['measured'])} {g['unit'] if g['measured'] is not None else ''} | {cell(g['required'])} | {num(g['margin'])} | {cell(g['at'])} | {st(g)} | `{g['method']}` | {', '.join(g['assumes']) or '—'} |")
L.append("\nMotion (U-03 b). Each path was swept with all of its motion variables together, from first contact to the final pose.\n- **OD-H24:** lowered along −Z from +25 in 0.5 mm steps (51 poses): 0 mm³ against the mount with the three hook sectors exempt. The hooks overlap the flange from +9.5 down to the seat, which is the snap deflection (catch overlap 1.5).\n- **OD-H22:** slid along −Y at +5.0 from y +45 to 0 (1 mm steps, 0.25 mm over y 18 … 0; 100 poses), then dropped 5.0 in 0.25 mm steps (21 poses): 0 mm³ against the mount and against the seated OD-H24 at every pose. The least slide clearance is 0.858 at y +15.5, at the slot mouth corner (54.95, 15.0, 48.0). On the drop the gap holds 0.503 (stem to slot) down to +0.75, then closes onto the flange contact.\n")
L.append("Deck wedges (brief). I measured these from sections of the exported STEP: exact rays from each Ø3.4 clearance-hole wall to the slit end over ±30° at z 47.999 … 46.01. At the deck top the wedges are **1.789 mm** (−X, hole at 46.662) and **1.898 mm** (+X, hole at 77.447). They widen with depth, to 3.891 / 4.000 at z 46.01. Both pass D-01b's 1.5. `min_wall` does not see them, because the faces are not opposed within 25°.\n")
L.append("## 3. Feature census against the plan\n")
L.append("| Plan feature | Expected | Found | Status |\n|---|---|---|---|")
for c in D["feature_census"]: L.append(f"| {cell(c['feature'])} | {cell(c['expected'])} | {cell(c['found'])} | {c['status']} |")
L.append("\nAll 15 U-05 features are present. Two changes from the plan are both declared in REPORT §8: the recess edge chamfer 0.2 and the catch land 1.6.\n")
L.append("## 4. Plausibility (`GATES.md` §P, one line each)\n")
L.append("| # | Question | Answer | Status |\n|---|---|---|---|")
for p in D["plausibility"]: L.append(f"| {p['question'].split()[0]} | {' '.join(p['question'].split()[1:])} | {cell(p['answer'])} | {p['status']} |")
L.append("\nEvidence: my sections in `reviews/RV01_work/sections/` (deck top z 47.99, notches z 10.25, insert bore x 46.662, assembly at x 62 / y 0, the rib at x 0.75, the ring root at y −12). Each has 0 px clipped.\n")
L.append("## 5. Positive controls\n")
L.append("| Check | Mutant of this job's part | Got |\n|---|---|---|")
for c in D["positive_controls"]: L.append(f"| {c['check']} | {cell(c['mutant'])} | {c['got']} |")
L.append("\nEvery check family FAILs on its mutant. `brep_valid` passes on an open shell because BRepCheck does not catch that case; `naked_edges` does (14 edges). `brep_valid` itself FAILs on the inside-out solid.\n")
L.append("## 6. Findings\n")
L.append("| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |\n|---|---|---|---|---|---|---|---|---|---|")
for f in D["findings"]:
    L.append(f"| {f['id']} | {f['gate']} | {f['kind']} | {num(f['measured'])} {f['unit']} → {cell(f['required'])} | {num(f['margin'])} | {cell(f['at'])} | {'yes' if f['blocks'] else 'no'} | {f['risk']} | {cell(f['risk_basis'])} | {cell(f['fix_direction'])} |")
L.append("\nF1–F4 come from two geometric facts. The Usta can accept them knowingly (D-022):\n1. **Rib ends.** OD-H24's underside rib plane (z_H24 0.1) runs out to r 14.056 on the rim's inner round. The spec's recess R 14.10 ± 0.1 therefore cannot give 0.5 to it at any radius inside its band. This one needs a spec decision, not a rebuild.\n2. **Ring root round.** The 0.3 round at the ring root brings the ring within 0.377 of the cup's foot. A 0.1 round would clear it.\n\nF7–F11 rate REPORT §4's parameters that pass only at nominal, as the brief asks.\n")
L.append("## 7. \"Least sure of\", answered\n")
L.append("| REPORT item | What the review found |\n|---|---|")
for a in D["least_sure_answers"]: L.append(f"| {cell(a['item'])} | {cell(a['answer'])} |")
(JOB / "reviews/RV01_od_c07_mount_v01.md").write_text("\n".join(L) + "\n")
print("ok")
