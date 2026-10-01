"""D7 v01b: per sweep run, the rows that do not pass and the worst margin per gate family,
from 01_CAD/sweep_v01b/<run>/check.json (the v01b checks on the v01 sweep files, nothing
rebuilt). Build facts come from 01_CAD/sweep_v01/<run>/build_record.json, and each run's STEP
is re-hashed against that record. Writes 01_CAD/sweep_v01b/sweep_summary.json. Standard library only."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC, SW = HERE / "sweep_v01", HERE / "sweep_v01b"
BY_ROW = ("E-06", "REQ-08(Soft)", "U-08", "D-05a", "D-05b", "D-07", "J-05")
out = {}
for d in sorted(p for p in SW.iterdir() if (p / "check.json").exists()):
    j = json.loads((d / "check.json").read_text())
    rec = json.loads((SRC / d.name / "build_record.json").read_text())
    step = SRC / d.name / f"od_c10_top_C1_v01_{d.name}.step"
    sha_now = hashlib.sha256(step.read_bytes()).hexdigest()
    rows = [r for r in j["gates"] if r["gate"] not in BY_ROW]
    not_pass = [{"gate": r["gate"], "status": r["status"], "measured": r["measured"], "margin": r.get("margin")}
                for r in rows if r["status"] not in ("PASS", "PASS_ASSUMED")]
    fam = {}
    for r in rows:
        if r.get("margin") is None:
            continue
        f = r["gate"].split(".")[0]
        if f not in fam or r["margin"] < fam[f]["margin"]:
            fam[f] = {"gate": r["gate"], "margin": r["margin"], "measured": r["measured"], "unit": r["unit"]}
    c11 = {r["gate"]: (r["status"], r["measured"]) for r in j["gates"] if ".c11." in r["gate"]}
    out[d.name] = {"solids": rec["solids"], "faces": rec["faces"],
                   "variant": {k: rec["params"][k] for k in ("hole_d", "cbore_d", "cbore_floor_y", "col_dx", "col_dz",
                                                            "col_bottom_y", "pad_bottom_y", "skirt_bottom_y")},
                   "not_pass": not_pass, "worst_per_family": fam, "c11_rows": c11,
                   "corner_contact_area_mm2": j["facts"].get("U-03.c11.corner_contact_area_mm2"),
                   "step_sha256": sha_now, "step_unchanged": sha_now == rec["step"]["sha256"]}
(SW / "sweep_summary.json").write_text(json.dumps(out, indent=1))
for k, v in out.items():
    print(f"{k:<20} solids {v['solids']} faces {v['faces']} same_step {v['step_unchanged']} not_pass "
          f"{[(n['gate'], n['status'], n['measured']) for n in v['not_pass']]}")
