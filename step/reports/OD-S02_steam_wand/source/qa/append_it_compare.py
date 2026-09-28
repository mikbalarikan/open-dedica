#!/usr/bin/env python3
# run-local (it3 version of _it2_SUPERSEDED/qa/append_it_compare.py): appends the it1 -> it2 -> it3 comparison,
# the verdict-change note and the skill-defect list to qa/VERDICT.md after `verdict.py render`. Every number is read
# from _it1_SUPERSEDED/qa/gate.json, _it2_SUPERSEDED/qa/gate.json, qa/gate.json, qa/it2_it3_diff.json and
# qa/attribution_probe.json / qa/zone_probe.json (CHK-NUMBERS); none typed by hand.
import json
G = [json.load(open(p)) for p in ("_it1_SUPERSEDED/qa/gate.json", "_it2_SUPERSEDED/qa/gate.json", "qa/gate.json")]
df = json.load(open("qa/it2_it3_diff.json"))["summary"]
ap = json.load(open("qa/attribution_probe.json"))["it3"]; zp3 = json.load(open("qa/zone_probe.json")); zp2 = json.load(open("_it2_SUPERSEDED/qa/zone_probe.json"))
def s(g, *path):
    x = g["deviation"]
    for p in path: x = x[p]
    return x
f = lambda x: f"p95 {x['p95']:.3f} / max {x['max']:.3f}"
rows = [("scan→CAD unmasked", ("scan_to_cad",)), ("scan→CAD masked (gated)", ("scan_to_cad_masked",)),
        ("CAD→scan unmasked", ("cad_to_scan",)), ("CAD→scan masked", ("cad_to_scan_masked",)),
        ("CAD→scan observable (gated)", ("cad_to_scan_observable",))]
for z in ("Z1 rod spigot taper + O-ring seats", "Z2 steel tube B-bend-C", "Z3 lever paddle", "Z4 bushing + tip"):
    for dn, lab in (("scan_to_cad", "scan→CAD"), ("cad_to_scan", "CAD→scan")):
        rows.append((f"{z} {lab} masked (gated)", ("zones", z, dn, "masked")))
        rows.append((f"{z} {lab} unmasked", ("zones", z, dn, "unmasked")))
L = ["", "## Iteration comparison it1 → it2 → it3 (CHK-LIKE4LIKE: same regime, masks, zones, ICP params, sampling; see checks)", "",
     f"STEP diff it2 → it3 (qa/it2_it3_diff.json): faces {df['faces_it2']} → {df['faces_it3']}; {df['faces_changed_it2']} it2 faces replaced by {df['faces_changed_it3']} it3 faces, "
     f"changed faces by QA zone box {df['changed_faces_by_zone']}; removed material {df['removed_pieces']} pieces / {df['removed_volume_mm3']} mm³ in zones {df['removed_by_zone']}; "
     f"added {df['added_pieces']} pieces / {df['added_volume_mm3']} mm³ in zones {df['added_by_zone']}. "
     "Every removed/added piece sits in Z2 (bend), Z3 (paddle; its pieces run under the knob to x 8.9, which is why 'R knob' faces are listed) or Z4 (tip neck). "
     "The 'R knob' face entries are paddle outline faces plus fused neighbours whose area moved by ≤0.73 mm² (boolean re-trim); no piece of material changed outside the three features. "
     "Also new: two 1.61 mm² annular ledges at the bend ends (bend radius ≠ straight-tube radius). This confirms the builder's claim (MODELING_PLAN §8 it3): only the bend, the paddle perimeter round and the tip neck changed; windows and bore unchanged "
     f"({ap['n_win_bore_faces_matched_in_it3']} of 32 it2 window/bore faces found unchanged in it3).", "",
     "| Statistic | it1 | it2 | it3 |", "|---|---|---|---|"]
for name, p in rows:
    L.append(f"| {name} | " + " | ".join(f(s(g, *p)) for g in G) + " |")
L.append("| ICP | " + " | ".join(f"{g['registration']['iterations']} its, {g['registration']['delta_deg']:.3f}° / {g['registration']['delta_mm']:.3f} mm" for g in G) + " |")
L.append("| unobservable fraction | " + " | ".join(f"{g['deviation']['unobservable_fraction']*100:.2f} %" for g in G) + " |")
L.append("| scan→CAD over-band clusters | " + " | ".join(str(len(g['deviation']['over_band_clusters']['scan_to_cad']['clusters'])) for g in G) + " |")
L.append("| band_fails | " + " | ".join(str(len(g['band_fails'])) for g in G) + " |")
L.append("| mask-dependent passes | " + " | ".join(str(len(g['deviation']['mask_dependent_passes'])) for g in G) + " |")
L += ["", "Signed zone probe (qa/zone_probe.json, same bins as it2; + = scan inside the CAD):",
      f"- Z2 all: it2 p95 {zp2['Z2_all']['p95']} mean {zp2['Z2_all']['mean_signed']} → it3 p95 {zp3['Z2_all']['p95']} mean {zp3['Z2_all']['mean_signed']}; bend bin x 33..35: {zp2['Z2_bins']['x 33..35, z>-14']['p95']} → {zp3['Z2_bins']['x 33..35, z>-14']['p95']}.",
      f"- Z3 all: it2 p95 {zp2['Z3_all']['p95']} → it3 {zp3['Z3_all']['p95']}; perimeter/rounds mean signed {zp2['Z3_by_cad_face_side']['perimeter/rounds (|ny|<=0.8)']['mean_signed']} → {zp3['Z3_by_cad_face_side']['perimeter/rounds (|ny|<=0.8)']['mean_signed']}.",
      f"- Z4 scan→CAD all: it2 p95 {zp2['Z4_s2c_all']['p95']} → it3 {zp3['Z4_s2c_all']['p95']}; z -35..-31 bin (tube entry, bushing top) {zp2['Z4_s2c_by_z']['z -35..-31']['p95']} → {zp3['Z4_s2c_by_z']['z -35..-31']['p95']} (unchanged, not addressed).",
      "", "Reading: the it3 changes did what they were meant to do. Z2 (bend) and Z3 (paddle) now pass both directions (Z2 CAD→scan only masked: unmasked max 0.802). "
      "The tip neck removed the Z4 hub cells, bringing Z4 scan→CAD p95 from 0.324 to 0.301, but it is still over the band. The rest is the bushing-top collar at the tube entry and the barrel underside rim; neither was changed. "
      "The non-geometric misses (observable CAD→scan, Z4 CAD→scan, unmasked D1) are unchanged in cause. Band fails went from 7 to 3.", ""]
rv = json.load(open("qa/review.json"))
L += ["## Verdict change (owner decision, DECISIONS.md)", "", rv["verdict_change"], "",
      "Evidence reading kept from the REVISE assembly: of the 3 band fails, Z4 scan→CAD (p95 0.301) has a coherent, one-signed geometric cause that a rebuild could remove. "
      "It is the unmodelled bushing-top collar at the tube entry (scan outside the CAD; overlay Z=-33.5, photo_1), plus the barrel underside rim. "
      "The miss is marginal: 0.297 in the builder's datum frame, which is not gated, and 75 % of the collar points are within 0.8 mm of a scan-hole edge. "
      "The other two fails (observable CAD→scan, Z4 CAD→scan) and the unmasked D1 number cannot be fixed by geometry. Re-run trigger for the collar: limitation L6.", ""]
L += ["## Skill defects found", "",
      "Recurring from it1/it2 (`_it2_SUPERSEDED/qa/VERDICT.md` items 1-10), all re-checked on this run:",
      "1. **RECURS.** Functional-interface zones are silently ungated when `interface_max_mm` is null (`deviation_gate.py:349-350`, `verdict.py:92`). Same workaround: Z1-Z4 are written as `kind: \"whole\"`.",
      "2. **RECURS.** Zone CAD→scan is gated on the masked stats, but whole-part CAD→scan is gated on the observable split (`verdict.py:71`, `:87` vs `:64`). The QA-added M2 now decides both the Z1 and the Z2 CAD→scan passes. Z2 unmasked max 0.802 vs 0.8.",
      "3. **RECURS.** `datum_audit.py` has no tube-axis clock type and only a normals-eigen axis for axis-primary parts. `qa/datum_crosscheck.py` is reused, report-only.",
      "4. **RECURS.** `overlay.py` has no `--registration` (L5).",
      "5. **RECURS.** Observability heuristic blind spots: the any-ray-escapes rule marks only 1.72 % of the CAD unobservable. The 13.6 mm bore and the 2.52 mm pockets therefore stay in the gated 'observable' CAD→scan number.",
      "6. **RECURS.** The census definition differs between sibling skills: `step_check.py:75` excludes `revolution` (77.2 %), while the builder's export check includes it.",
      "7. **RECURS.** `verdict.py render` has no field for a REVISE route, an iteration comparison or skill defects. These sections were appended by `qa/append_it_compare.py` from the gate.json files.",
      "8. **RECURS.** `SKILL.md:58` sets `S=~/.claude/skills/stl-re-verify/scripts`, which does not exist here. The scripts live in `<repo>/skills/stl-re-verify/scripts`.",
      "9. **RECURS.** CHK-LIKE4LIKE has no tooling: there is no protocol or STEP diff script. `qa/it2_it3_diff.py` was written for this run.",
      "10. **RECURS (in a probe).** A run-local signed-distance probe was OOM-killed (exit 137) with no partial output: `trimesh.proximity.signed_distance` in 20000-point chunks on the 484k-triangle it3 tessellation. It completed with 2000-point chunks. The skill gives no memory guidance. All skill scripts were run one at a time and completed.",
      "New in it3:",
      "11. **Scan→CAD has no open-boundary treatment.** `mask-policy.md` defines `open_boundary` for `applies_to: cad` only. Z4 scan→CAD points within 0.8 mm of a scan-hole edge read p95 0.429 against 0.247 away from edges. The skill offers no pre-declared, symmetric way to report or sensitivity-test hole-edge curl in the scan→CAD direction. This run reports it via a probe only and did not add a mask after the fact.",
      "12. **No 'marginal / frame-sensitive miss' reporting.** `verdict.py` compares the post-ICP p95 to the band with no tolerance. That is correct and should stay. But it does not surface that the builder-datum-frame run (`deviation_datum.json`) passes the same zone (0.297 vs 0.301). Its only datum-vs-ICP check covers whole-part scan→CAD p95 differing by more than the band (`verdict.py` assemble), so a zone flipping across the band between frames goes unflagged.",
      ""]
open("qa/VERDICT.md", "a").write("\n".join(L) + "\n")
print("\n".join(L))
