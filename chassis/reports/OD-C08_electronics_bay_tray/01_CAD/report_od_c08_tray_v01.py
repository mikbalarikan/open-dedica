"""Write 01_CAD/REPORT_od_c08_tray_v01.md from the measured check results (PLAYBOOK D8).

Every number in the gate and sweep tables is read from 01_CAD/check_od_c08_tray_v01.json
and 01_CAD/sweep_v01/*/check.json (written by check_od_c08_tray.py from the re-imported
STEP files); nothing is retyped. The prose sections are in TEXT below.
Usage: uv run tools/run.py python <ws>/01_CAD/report_od_c08_tray_v01.py
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
RANK = {"FAIL": 4, "INCONCLUSIVE": 3, "PASS_ASSUMED": 1, "PASS": 0, "N/A": -1}
SPEC_IDS = ["U-01", "U-02", "U-03", "U-03(b)", "U-04", "U-05", "U-06(Soft)", "U-07", "U-08", "D-01a", "D-01b",
            "D-02", "D-03a", "D-03b", "D-04a", "D-04c", "D-04d", "D-05a", "D-05b", "D-06a", "D-07", "J-05", "E-01",
            "E-05", "E-06", "E-11", "REQ-01", "REQ-02", "REQ-03", "REQ-04", "REQ-05", "REQ-06(Soft)",
            "exactly_one_solid", "feature_census", "envelope_within_spec"]
SWEEP = [("pin_d", "pin_d_low", "pin_d_high", 1.75, 1.8, 1.85),
         ("bore_d", "bore_d_low", "bore_d_high", 3.95, 4.0, 4.05),
         ("hole_d", "hole_d_low", "hole_d_high", 3.3, 3.4, 3.5),
         ("seat_x", "seat_x_low", "seat_x_high", 82.388, 82.438, 82.488),
         ("shift_y (standoffs, bores, pins)", "shift_y_low", "shift_y_high", -0.1, 0.0, 0.1),
         ("shift_z (standoffs, bores, pins)", "shift_z_low", "shift_z_high", -0.1, 0.0, 0.1)]
# the rows each swept parameter acts on: the worst margin is read among them (all rows are scanned for failures)
FOCUS = {"pin_d": ("D-04d", "REQ-02.pin"), "bore_d": ("J-05", "D-05b", "D-05a"), "hole_d": ("REQ-01.x", "D-04a"),
         "seat_x": ("U-03.seat", "U-03.board", "U-03(b)", "REQ-02.seat"),
         "shift_y (standoffs, bores, pins)": ("D-04d", "E-05", "REQ-02"),
         "shift_z (standoffs, bores, pins)": ("D-04d", "E-05", "REQ-02")}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def spec_id(gate: str) -> str:
    if gate.startswith("U-03(b)"):
        return "U-03(b)"
    for sid in sorted(SPEC_IDS, key=len, reverse=True):
        if gate == sid or gate.startswith(sid + ".") or gate.startswith(sid + "("):
            return sid
    return gate.split(".")[0]


def fmt(v, nd=4):
    if v is None:
        return "—"
    if isinstance(v, float):
        if abs(v) < 1e-9:
            return "0"
        return f"{v:.{nd}f}".rstrip("0").rstrip(".")
    return str(v)


def summary(rows):
    """Per spec gate: the worst status, and the row with the least margin among those."""
    out = {}
    for r in rows:
        sid = spec_id(r["gate"])
        cur = out.get(sid)
        key = (RANK.get(r["status"], 0), -(r["margin"] if isinstance(r.get("margin"), (int, float)) else 1e9))
        if cur is None or key > cur[0]:
            out[sid] = (key, r)
    return {k: v[1] for k, v in out.items()}


def worst_margin(rows):
    best = None
    for r in rows:
        m = r.get("margin")
        req = str(r.get("required", ""))
        if not isinstance(m, (int, float)) or r.get("unit") in ("count", "bool", "") or req.startswith("=="):
            continue
        if req.startswith("in [0.0, 0.0]") or "0.0]" == req[-4:] and "in [0.0" in req:
            continue
        if best is None or m < best["margin"]:
            best = r
    return best


def main():
    chk = json.loads((HERE / "check_od_c08_tray_v01.json").read_text())
    rows, facts = chk["gates"], chk["facts"]
    rec = json.loads((HERE / "build_record_v01.json").read_text())
    secs = json.loads((HERE / "sections_v01.json").read_text())
    text = json.loads((HERE / "report_text_v01.json").read_text())
    files = ["01_CAD/DESIGN_PLAN.md", "01_CAD/probe/probe_inputs.py", "01_CAD/probe/probe_inputs.json",
             "01_CAD/check_od_c08_tray.py", "01_CAD/build_od_c08_tray.py", "01_CAD/sections_od_c08_tray.py",
             "01_CAD/sweep_od_c08_tray_v01.sh", "01_CAD/report_od_c08_tray_v01.py", "01_CAD/report_text_v01.json",
             "01_CAD/build_record_v01.json", "01_CAD/check_od_c08_tray_v01.json", "01_CAD/check_od_c08_tray_v01.log",
             "01_CAD/sections_v01.json",
             "02_STEP_STL/od_c08_tray_C1_v01.step", "02_STEP_STL/od_c08_assembly_C1_v01.step",
             "02_STEP_STL/od_c08_tray_C1_v01.stl"] + [s["file"] for s in secs if s.get("file")]
    notes = {"01_CAD/check_od_c08_tray.py": "checks, written before the build (D3)",
             "01_CAD/build_od_c08_tray.py": "parametric build script",
             "02_STEP_STL/od_c08_tray_C1_v01.step": "AP242, the part, re-imported for every measurement",
             "02_STEP_STL/od_c08_assembly_C1_v01.step": "AP242 check assembly: tray + OD-E01 at the joint + OD-C01 + OD-C02",
             "02_STEP_STL/od_c08_tray_C1_v01.stl": (f"tolerance {rec['stl']['tolerance']} mm / angular "
                                                    f"{rec['stl']['angular_tolerance']} rad, {rec['stl']['triangles']} "
                                                    f"triangles, cached triangulation cleared")}
    hashes = [(f, sha(WS / f)) for f in files]
    L = []
    L.append("# REPORT — od_c08_tray v01 (20261001-od-c08-electronics-bay-tray)\n")
    L.append(f"Designer: Claude Code, claude-opus-5-5 · spec version 1.0 · plan `01_CAD/DESIGN_PLAN.md` · {text['date']}\n")
    L.append("## 1. Files\n\n| File | SHA-256 | Note |\n|---|---|---|")
    for f, h in hashes:
        note = notes.get(f, "section, nothing clipped" if f.startswith("03_Sections") else "")
        L.append(f"| `{f}` | {h} | {note} |")
    L.append("\n## 2. Versions\n\n" + text["versions_line"] + "\n")
    L.append("## 3. Gate self-check\n\nEvery row of `01_CAD/check_od_c08_tray_v01.json`, measured on the re-imported "
             "STEP files. Band: GATES §0 (mm 0.005, mm³ 0.001, deg 0.001, counts 0). Margin is signed, positive "
             "inside the limit. The summary per §5 gate ID follows the full table.\n")
    L.append("| Gate | Measured | Required | Margin | At | Status | Assumes |\n|---|---|---|---|---|---|---|")
    for r in rows:
        meas = fmt(r.get("measured"))
        unit = r.get("unit") or ""
        L.append(f"| {r['gate']} | {meas} {unit} | {r.get('required')} | {fmt(r.get('margin'))} | "
                 f"{r.get('at') or '—'} | {r['status']} | {', '.join(r.get('assumes', [])) or '—'} |")
    summ = summary(rows)
    L.append("\n**Summary per §5 gate ID** (worst status of its rows; the row with the least margin):\n")
    L.append("| §5 gate | Status | Worst row | Measured | Margin | Note |\n|---|---|---|---|---|---|")
    for sid in SPEC_IDS:
        r = summ.get(sid)
        if r is None:
            L.append(f"| {sid} | — | (no row) | — | — | — |")
            continue
        L.append(f"| {sid} | {r['status']} | {r['gate']} | {fmt(r.get('measured'))} {r.get('unit') or ''} | "
                 f"{fmt(r.get('margin'))} | {text['gate_notes'].get(sid, '')} |")
    L.append("\n" + text["section3_notes"] + "\n")
    # sweep
    L.append("## 4. Robustness sweep (D7)\n")
    L.append(text["sweep_intro"] + "\n")
    L.append("| Parameter | Low · nominal · high | All built, one solid | Worst gate | Worst margin | Rows not passing (low / high) |\n"
             "|---|---|---|---|---|---|")
    sweep_json = []
    for name, lo, hi, vlo, vnom, vhi in SWEEP:
        runs = {}
        for tag in (lo, hi):
            p = HERE / "sweep_v01" / tag / "check.json"
            runs[tag] = json.loads(p.read_text())["gates"] if p.exists() else None
        built = all(r is not None and any(x["gate"] == "U-01.solid_count" and x["status"] == "PASS" for x in r)
                    for r in runs.values())
        allrows = [x for r in runs.values() if r for x in r if x["status"] not in ("N/A",) and
                   not x["gate"].startswith("REQ-06")]
        fails = [x for x in allrows if x["status"] == "FAIL" and isinstance(x.get("margin"), (int, float))]
        focus = [x for x in allrows if x["gate"].startswith(FOCUS[name]) and isinstance(x.get("margin"), (int, float))
                 and x.get("unit") not in ("count", "bool")]
        pool = fails or focus
        w = min(pool, key=lambda x: x["margin"]) if pool else worst_margin(allrows)
        np_ = []
        for tag in (lo, hi):
            r = runs[tag] or []
            bad = sorted({spec_id(x["gate"]) + ":" + x["status"] for x in r if x["status"] in ("FAIL", "INCONCLUSIVE")
                          and not x["gate"].startswith("REQ-06")})
            np_.append(", ".join(bad) or "none")
        L.append(f"| {name} | {vlo} · {vnom} · {vhi} | {'yes' if built else 'no'} | "
                 f"{w['gate'] if w else '—'} | {fmt(w.get('margin')) if w else '—'} | {np_[0]} / {np_[1]} |")
        sweep_json.append({"parameter": name, "values": [vlo, vnom, vhi], "all_built": built,
                           "worst_gate": w["gate"] if w else None,
                           "worst_margin": w.get("margin") if w else None})
    L.append("\n" + text["sweep_notes"] + "\n")
    L.append("## 5. Build facts\n")
    env = facts["envelope"]
    m = facts["mass"]
    L.append(f"- Envelope {fmt(env['size_x'])} × {fmt(env['size_y'])} × {fmt(env['size_z'])} mm at x "
             f"{fmt(env['min_x'])} … {fmt(env['max_x'])}, y {fmt(env['min_y'])} … {fmt(env['max_y'])}, z "
             f"{fmt(env['min_z'])} … {fmt(env['max_z'])}; volume {fmt(m['volume'], 1)} mm³; mass "
             f"{fmt(m['mass'], 1)} g at 1270 kg/m³ (A-10); centre of mass ({fmt(m['com_x'], 2)}, "
             f"{fmt(m['com_y'], 2)}, {fmt(m['com_z'], 2)})")
    st = facts.get("stl", {})
    mc = facts.get("mesh_census", {})
    L.append(f"- STL (for the orchestrator's 3MF): {st.get('triangles_header')} triangles, volume "
             f"{fmt(mc.get('volume'), 1)} mm³, bounding box {st.get('bbox_min')} … {st.get('bbox_max')} "
             f"(size {st.get('bbox_size')}), one closed body, sagitta {fmt(rec['stl']['max_sagitta'], 5)} mm")
    L.append("- Fillets: none requested by the spec, none made")
    for lab, pl in rec.get("placements", {}).items():
        L.append(f"- Placement: {lab}: {pl['joint']}; {pl['location']}")
    L.append("\n" + text["build_facts_extra"] + "\n")
    L.append("## 6. Plausibility (§P, D6)\n\n| # | Question (`GATES.md` §P) | Designer's answer, from the sections and views |\n|---|---|---|")
    for k, q, a in text["plausibility"]:
        L.append(f"| {k} | {q} | {a} |")
    L.append("\nSections (`01_CAD/sections_v01.json`): " + "; ".join(
        f"`{s['file'].split('/')[-1]}` nothing_clipped {s['nothing_clipped']}" for s in secs if s.get("file")) + "\n")
    L.append("## 7. Library and tools used\n\n" + text["tools"] + "\n")
    L.append("## 8. Deviations from the plan\n\n" + text["deviations"] + "\n")
    L.append("## 9. What I am least sure of\n")
    for i, s in enumerate(text["least_sure"], 1):
        L.append(f"{i}. {s}")
    L.append("\n## 10. Stop\n\n" + text["stop"] + "\n")
    jgates = []
    for r in rows:
        st_ = r["status"]
        jgates.append({"gate": r["gate"], "measured": r.get("measured"), "unit": r.get("unit") or "",
                       "required": r.get("required"), "margin": r.get("margin"), "at": r.get("at"),
                       "status": st_, "assumes": r.get("assumes", [])})
    block = {"schema": "oguz-report-v1", "job_id": "20261001-od-c08-electronics-bay-tray", "part": "od_c08_tray",
             "tag": "v01", "spec_version": "1.0", "files": [{"path": f, "sha256": h} for f, h in hashes],
             "versions": text["versions"], "gates": jgates, "sweep": sweep_json,
             "least_sure": text["least_sure"], "stopped": False}
    L.append("```json\n" + json.dumps(block, indent=1, ensure_ascii=False, default=str) + "\n```\n")
    out = "\n".join(L)
    (HERE / "REPORT_od_c08_tray_v01.md").write_text(out, encoding="utf-8")
    # return-block summary
    for sid in SPEC_IDS:
        r = summ.get(sid)
        if r:
            print(f"{sid} {r['status']} {fmt(r.get('measured'))} {r.get('unit') or ''} | {r['gate']}")
    for f, h in hashes:
        print(f, h)


if __name__ == "__main__":
    main()
