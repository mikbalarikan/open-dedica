# DECISIONS — OD-S01_steam-valve

Human decisions that gate this run. One entry per decision; never edit an old entry,
append a new one. Format: `- <date> | <who> | <decision id> | <decision> | <evidence path>`

Decision ids: REGIME (band regime chosen at intake), MEASUREMENTS (calipers supplied /
proceed scan-only), PART-CLASS (unsupported class: proceed or stop), ACCEPT-BAND
(BAND_NOT_MET accepted for delivery), HALT (reason and options), INDEP (verify could not
run in a fresh context), OTHER.

- 2026-09-28 | Ikbal (owner, session message) | REGIME | baseline-skill, material_class plastic: p95 <= 0.30 / max <= 0.80 mm (baseline/skills/stl2step-build123d/SKILL.md:87). User wrote "p95 plastik parça toleransı kullan". Declared before any gate numbers exist. | session message; intake/regime.json
- 2026-09-28 | Ikbal (owner, question card) | MEASUREMENTS | No calipers; proceed scan-only ("Yes, scan-only"). Limitations carried to verdict: "Tier-1 not run" and "absolute scale not caliper-verified", re-run trigger: any caliper reading. Photos 1-5 are catalogue images without scale reference: feature identification / plausibility only. | session question card; input/INPUT_HASHES.json
- 2026-09-28 | Ikbal (owner, question card) | OTHER | scan_resolution confirmed full-res ("Yes, original full-res"); 499,756 faces, mean edge 0.206 mm, one body. | input/INPUT_HASHES.json#scan_resolution
- 2026-09-28 | Ikbal (owner, session message) | OTHER | Delivery format: one zip with all deliverables + all source files (standing format, skills/stl-re-deliver/references/delivery-package.md). | session message
- 2026-09-28 | orchestrator (agent) | OTHER | REVISE (it1, qa/VERDICT.md) routed --route datum, not verify's suggested 'measure': two findings are CHK-ENUM gaps (bump under the switch, column lug at 320 deg), which orchestrate §4 routes to intake feature enumeration; the datum itself is kept (same spec, deterministic re-run). Loop 2 of 3. | qa/VERDICT.md
- 2026-09-28 | Ikbal (owner, question card) | ACCEPT-BAND | Accept and deliver: accepts scan_to_cad:masked, cad_to_scan_observable and zones Z1/Z2/Z3/Z4/Z6 band fails, gate 19f6d742b0ae (created 2026-09-28T08:12:03+00:00); scan->CAD p95 0.449 max 1.94, observable CAD->scan p95 0.761 max 2.89; loop 3 judged unable to reach the band (QA probe) | decisions/accept_band.md
