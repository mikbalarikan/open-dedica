import json
from pathlib import Path
W = Path("/home/claude/oguz-jobs/20260930-od-c04-thermoblock-mount")
d = json.loads((W / "reviews/RV01_od_c04_mount_v01.json").read_text())
ST = {"PASS": "PASS", "FAIL": "FAIL", "INCONCLUSIVE": "INCONCLUSIVE", "NOT_APPLICABLE": "N/A: by its row"}
def st(g):
    if g["status"] == "PASS_ASSUMED": return "PASS (assumed: " + ", ".join(g["assumes"]) + ")"
    return ST[g["status"]]
def num(v): return "—" if v is None else f"{v:g}"
L = []
L += ["# RV01 — od_c04_mount_v01 (20260930-od-c04-thermoblock-mount) — 2026-09-30 UTC", "",
      "Reviewer: Claude Code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted",
      "Spec 1.2 · plan `01_CAD/DESIGN_PLAN.md` (with the amendments of `briefs/WP-03_designer.md`) · report `01_CAD/REPORT_od_c04_mount_v01.md`", "",
      "**VERDICT: APPROVED (assumption-conditional)**",
      "Blocking findings: 0 · open assumptions relied on: " + ", ".join(d["assumptions_relied_on"]), "",
      d["summary"], "",
      "Method: every row was re-measured with `tools.core` / `tools.measure` on the delivered STEP, STL and check-assembly STEP, and compared through `tools.result.gate` within the GATES.md §0 band (0.005 mm, 0.001 deg, 0.001 mm3, 0 for counts). No CAD code was read. Scripts, results and sections are in `reviews/RV01_work/` (`m1_part.py` … `m8_controls2.py`, `m*.json`, `sections/`, `mutants/`).", "",
      "## 1. Files reviewed", "", "| File | SHA-256 | Matches REPORT |", "|---|---|---|"]
for f in d["files"]:
    note = "yes" if f["path"].startswith(("01_CAD/check", "01_CAD/build", "01_CAD/sweep", "02_", "03_")) else "yes (matches the brief; the REPORT does not list its own hash or the plan's)" if f["path"].startswith("01_CAD/") else "yes (input, matches the brief)"
    L.append(f"| `{f['path']}` | {f['sha256']} | {note} |")
L += ["", "The delivery must carry exactly these bytes. The delivered STL's bytes differ from a re-mesh of the re-imported STEP (`0cc3d677…`, identical to the designer's `remesh_check.stl`), but it has the same 8516 triangles at the recorded 0.01 mm / 0.23097 rad and a measured deviation of 0.00636 mm from the B-rep (U-07).", "",
      "## 2. Gate table", "", "| Gate | Measured | Required | Margin | At | Status | Method | Assumes |", "|---|---|---|---|---|---|---|---|"]
for g in d["gates"]:
    L.append(f"| {g['gate']} | {num(g['measured'])} {g['unit'] if g['measured'] is not None else ''} | {g['required']} | {num(g['margin'])} | {g['at'] or '—'} | {st(g)} | `{g['method']}` | {', '.join(g['assumes']) or '—'} |")
L += ["", "Assembly and motion: no motion variable (U-03 b). Assembly path, measured with `clearance` at offsets of the placed parts: OD-H11 with both spacers approaching along −Z reads a least clearance of 0.10 / 0.50 / 1.0 / 2.0 / 5.0 / 10.0 / 12.49 / 14.32 / 29.75 mm at 0.1 / 0.5 / 1 / 2 / 5 / 10 / 20 / 40 / 60 mm of travel (first contact is the designed spacer contact); OD-H11 alone lowered along −Y reads 10.100 mm from 0.5 to 60 mm of travel. REQ-07 about the origin, reported beside the gated axis reading: 0.000 mm3.", "",
      "## 3. Feature census against the plan", "", "| Plan feature | Expected | Found | Status |", "|---|---|---|---|"]
for c in d["feature_census"]:
    L.append(f"| {c['feature']} | {c['expected']} | {c['found']} | {c['status']} |")
L += ["", "Totals (`feature_census`): 24 planar, 10 cylindrical (4 convex, 6 concave), 2 toroidal, 0 other; `bore_census` 6.", "",
      "## 4. Plausibility (`GATES.md` §P, one line each)", "", "| # | Question | Answer | Status |", "|---|---|---|---|"]
Q = {"P1": "Gravity: does every part rest and mount the way the product is used?", "P2": "Function chains connected and aimed (air, drive, liquid, cable)?",
     "P3": "Moving parts oriented for their motion, with clearance?", "P4": "Human factors: grip, reach, insertion direction obvious?",
     "P5": "Next to a comparable real product, does anything look absurd?", "P6": "Nothing floating, embedded, mirrored, or upside-down?"}
for p in d["plausibility"]:
    k = p["question"][:2]
    L.append(f"| {k} | {Q[k]} | {p['answer']} | {'N/A' if p['status']=='NOT_APPLICABLE' else p['status']} |")
L += ["", "Evidence: the reviewer's own sections (`reviews/RV01_work/sections/`: x −19.62, 25.01, 40, −46; y −68; z −11, −10.2; assembly x −19.62 and 25.01, `nothing_clipped` 0 on all nine) and the measurements above; renders were not used.", "",
      "## 5. Positive controls", "", "| Check | Mutant of this job's part | Got |", "|---|---|---|"]
for c in d["positive_controls"]:
    L.append(f"| {c['check']} | {c['mutant']} | {c['got']} |")
L += ["", "Every check family used in §2 FAILs on its mutant; no gate rests on a check that could not fail. `radial_profile` returns INCONCLUSIVE on the part and on the mutant alike (every ray without material is unread by its contract), so REQ-07 is gated on `common_volume` and the per-ray reasons are the recorded reading.", "",
      "## 6. Findings", "", "| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |", "|---|---|---|---|---|---|---|---|---|---|"]
for f in d["findings"]:
    meas = "INCONCLUSIVE" if f["measured"] is None else f"{f['measured']:g} {f['unit']}"
    L.append(f"| {f['id']} | {f['gate']} | {f['kind']} | {meas} → {f['required']} | {num(f['margin'])} | {f['at']} | {'yes' if f['blocks'] else 'no'} | {f['risk']} | {f['risk_basis']} | {f['fix_direction']} |")
L += ["", "## 7. \"Least sure of\", answered", "", "| REPORT item | What the review found |", "|---|---|"]
for a in d["least_sure_answers"]:
    L.append(f"| {a['item']} | {a['answer']} |")
(W / "reviews/RV01_od_c04_mount_v01.md").write_text("\n".join(L) + "\n")
print("ok")
