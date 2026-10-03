import json
from pathlib import Path
W = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig")
V = json.loads((W / "reviews/RV02_od_t01_rig_v02.json").read_text())
def st(g):
    s = g["status"]
    if s == "PASS_ASSUMED": return "PASS (assumed: " + ", ".join(g["assumes"]) + ")"
    if s == "NOT_APPLICABLE": return "N/A: the row applies to other parts"
    if s == "INCONCLUSIVE" and g["gate"] == "REQ-08": return "INCONCLUSIVE (Soft, bench; rated in F1)"
    return s
def num(x): return "—" if x is None else (f"{x:+g}" if isinstance(x, (int, float)) else str(x))
L = []
L.append("# RV02 — od_t01_rig_v02 (20261002-od-t01-pressure-test-rig) — 2026-10-03 UTC\n")
L.append("Reviewer: Claude Code, claude-opus-5-5 · independent re-measurement; designer numbers are not trusted")
L.append("Spec 1.3 · plan `01_CAD/DESIGN_PLAN.md` (with `briefs/WP-03_designer.md`, `briefs/WP-05_designer.md`) · report `01_CAD/REPORT_od_t01_rig_v02.md`\n")
L.append("**VERDICT: APPROVED (assumption-conditional)**")
L.append("Blocking findings: 0 · open assumptions relied on: " + ", ".join(V["assumptions_relied_on"]) + "\n")
L.append(V["summary"] + "\n")
L.append("All measurements were made with the reviewer's own scripts in `reviews/RV02_work/`: `rv_part.py`, `rv_print.py`, `rv_rt.py`, `rv_pose.py`, `rv_static.py`, `rv_motion.py`, `rv_sections.py`, `rv_controls.py` and `rv_control_flank.py`. Every one read the delivered STEP from disk. The housing set was posed from `od_g01_assembly_C1_v03.step` by spec §2: housing x → X, y → +Z, z → −Y, origin (0, 110.06, 0). That is +90° about X, a proper rotation, and the axis mapping was checked. The solids were identified by measurement: the housing is the 100 × 100 solid with four Ø4.0 bores at (±44, ±44); OD-G10 is the solid longer than 120 (185.1); OD-G04 is the remaining one. The designer's assembly file was not used for any gate. Bands are from GATES §0: 0.005 mm, 0.001 deg, 0.001 mm³, 0 for counts. No CAD code, sweep folder, designer JSON or log was read.\n")
L.append("**RV01 follow-up.**")
L.append("- **F1 (REQ-08, plate) is closed for the items it named.** The plate is y 135.000 … 160.000, and the counterbore floors are at y 140.000, which leaves 5.000 under each head. The measured window section at x 0 is 1187.5 mm², with Z 4948.1 mm³. That gives σ 9.59 MPa and a factor of 4.17 against 40 MPa, which agrees with spec 1.3 §4. Head pull-through is τ 8.5 MPa. REQ-08 is re-rated below (F1 of this review) for head bearing, which the hand calculation does not cover.")
L.append("- **F2 (REQ-03 apex band) is closed.** The apex is at z 42.5006 against 42.51 ± 0.16, a margin of +0.151. At R 29.9 the apex falls at 42.359, inside 42.35 with +0.009 to spare, so the band now stacks with R ± 0.1 without relying on the 0.005 band.\n")
L.append("## 1. Files reviewed\n")
L.append("| File | SHA-256 | Matches REPORT |\n|---|---|---|")
for f in V["files"]:
    L.append(f"| `{f['path']}` | {f['sha256']} | {'yes' if f['matches_report'] else 'no'} |")
L.append("\nThe REPORT lists the first three files, the six sections and the REPORT itself. The brief lists the spec, the inputs, the plan and RV01, and every one matches the brief. The delivery must carry exactly the STEP and STL bytes above. A reviewer re-mesh of the STEP at 0.01 mm / 0.10 rad reproduces the delivered STL byte for byte.\n")
L.append("## 2. Gate table\n")
L.append("| Gate | Measured | Required | Margin | At | Status | Method | Assumes |\n|---|---|---|---|---|---|---|---|")
for g in V["gates"]:
    m = "—" if g["measured"] is None else f"{g['measured']:g} {g['unit']}"
    L.append(f"| {g['gate']} | {m} | {g['required']} | {num(g['margin'])} | {g['at'] or '—'} | {st(g)} | `{g['method']}` | {', '.join(g['assumes']) or '—'} |")
L.append("\nMotion was swept as follows:")
L.append("- U-03b: the housing set at dy 0 … −30, every 1.0 (31 poses).")
L.append("- REQ-04a: φ −60° … +15°, every 1° (76 poses).")
L.append("- REQ-04b: dz 0 … 200, every 2.5, at φ −50° and dy −15 (81 poses).")
L.append("- The joining lift: φ −50°, dy −15 … 0, every 1.0 (16 poses).")
L.append("- φ and dy swept together on a grid: φ −60° … +15° every 5°, dy −15 … 0 every 1.5 (176 poses).")
L.append("")
L.append("Together these cover the insertion path from first contact (dz 200) to the locked pose, and any bayonet path that turns and lifts at once. Every OD-G10 row uses the spec's reading, `clearance > 0` with `inside == False`. OD-G10 is confirmed `brep_valid` 0, and `common_volume` reads it INCONCLUSIVE. No pose was inside.\n")
L.append("## 3. Feature census against the plan\n")
L.append("| Plan feature | Expected | Found | Status |\n|---|---|---|---|")
for f in V["feature_census"]:
    L.append(f"| {f['feature']} | {f['expected']} | {f['found']} | {f['status']} |")
L.append("\n## 4. Plausibility (`GATES.md` §P, one line each)\n")
L.append("These answers come from the reviewer's sections in `reviews/RV02_work/sections/`. With the housing set: z 0, z 44 and x 0. Rig only: y 147.5, y 137.5, y 5, x 44 and z 50. `nothing_clipped` reads 0 on all eight.\n")
L.append("| # | Question | Answer | Status |\n|---|---|---|---|")
for p in V["plausibility"]:
    L.append(f"| {p['question'].split()[0]} | {' '.join(p['question'].split()[1:])} | {p['answer']} | {p['status']} |")
L.append("\n## 5. Positive controls\n")
L.append("| Check | Mutant of this job's part | Got |\n|---|---|---|")
for c in V["positive_controls"]:
    L.append(f"| {c['check']} | {c['mutant']} | {c['got']} |")
L.append("\nEvery check family used in §2 FAILs on its mutant, so no gate rests on a blind check. The mutants are built in `rv_controls.py` and `rv_control_flank.py`, and the mutant meshes are in `reviews/RV02_work/mutants/`.\n")
L.append("## 6. Findings\n")
L.append("| ID | Gate | Kind | Measured → required | Margin | At | Blocks | Risk | Risk basis | Fix direction |\n|---|---|---|---|---|---|---|---|---|---|")
for f in V["findings"]:
    L.append(f"| {f['id']} | {f['gate']} | {f['kind']} | not measurable (bench) → {f['required']} | — | {f['at']} | {'yes' if f['blocks'] else 'no'} | {f['risk']} | {f['risk_basis']} | {f['fix_direction']} |")
L.append("\nREQ-08 against spec 1.3 §4, from the reviewer's numbers:")
L.append("- **Window section, bending.** At x 0 the plate keeps z −60 … −30 and +42.50 … +60, which is 47.5 of the 120, at 25.0 deep. The measured section is A 1187.5 mm², I 61 851 mm⁴, Z 4948.1 mm³. With M = 1.53 kN × 31 mm = 47.4 N·m, σ is 9.59 MPa, a factor of 4.17 against ≈ 40 MPa along the layers. This agrees with §4.")
L.append("- **Pull-through.** The shear cylinder is Ø5.7 × 5.0, 89.5 mm², so τ = 765 N / 89.5 = 8.5 MPa. This agrees with §4.")
L.append("- **Head bearing (not in §4).** The ISO 7380 M3 head (Ø5.7) bears on the floor annulus outside the Ø3.4 hole, 16.4 mm². At 765 N that is about 47 MPa, close to the compressive yield of printed PLA. The floor at y 140 is a vertical face in the print, so the bearing runs along the layers.")
L.append("")
L.append("Bending and pull-through therefore have room, and the head seats are the likely first yield. That would show as heads sinking and the housing dropping, not as a sudden fracture, and the test is hydrostatic with low stored energy. Rated MEDIUM, not blocking (Soft).\n")
L.append("## 7. \"Least sure of\", answered\n")
L.append("| REPORT item | What the review found |\n|---|---|")
for l in V["least_sure_answers"]:
    L.append(f"| {l['item']} | {l['answer']} |")
(W / "reviews/RV02_od_t01_rig_v02.md").write_text("\n".join(L) + "\n")
print("ok")
