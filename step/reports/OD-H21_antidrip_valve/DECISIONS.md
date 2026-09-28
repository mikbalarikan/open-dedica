# DECISIONS — OD-H21_antidrip-valve

Human decisions that gate this run. One entry per decision; never edit an old entry,
append a new one. Format: `- <date> | <who> | <decision id> | <decision> | <evidence path>`

Decision ids: REGIME (band regime chosen at intake), MEASUREMENTS (calipers supplied /
proceed scan-only), PART-CLASS (unsupported class: proceed or stop), ACCEPT-BAND
(BAND_NOT_MET accepted for delivery), HALT (reason and options), INDEP (verify could not
run in a fresh context), OTHER.

- 2026-09-28 | Ikbal (owner, session message) | MEASUREMENTS | No calipers; proceed scan-only (user message: "p95 plastik parça toleransı kullan. STL ve image ler ekte."; no measurements supplied). Limitations carried to verdict: "Tier-1 not run" and "absolute scale not caliper-verified", re-run trigger: any caliper reading. Photos are catalogue images without a scale reference: feature identification / plausibility only. | session message; input/INPUT_HASHES.json
- 2026-09-28 | Ikbal (owner, session message) | REGIME | baseline-skill, material_class plastic: p95 <= 0.30 / max <= 0.80 mm (baseline/skills/stl2step-build123d/SKILL.md:87). User wrote "p95 plastik parça toleransı kullan" = the baseline-skill plastic class, same regime as OD-H22. Declared before any gate numbers exist. | session message; intake/regime.json
- 2026-09-28 | orchestrator (agent) | OTHER | scan_resolution recorded as `full` by agent inference, not stated by the owner: 600,142 faces, mean edge 0.152 mm, 30.0 MB, same scanner/export family as OD-H22 (495,881 faces, mean edge 0.154 mm) which the owner confirmed full-res on 2026-09-25. Owner to confirm; if it is a decimated export, the verdict is capped at APPROVED_WITH_LIMITATIONS. | input/INPUT_HASHES.json#scan_resolution
- 2026-09-28 | orchestrator (agent) | OTHER | Verify it1 verdict REVISE (gate dd052135f7c2, errors empty): geometric causes named for nozzle latch window, ring windows, skirt slits. Routed --route geometry (loop 2 of 3): measure/ and build/MODELING_PLAN.md + model.py carried forward; change only those three features. The unscanned nozzle-bore-floor CAD->scan term is a coverage fact, not a rebuild target. | _it1_SUPERSEDED/qa/gate.json
- 2026-09-28 | Ikbal (owner, session message "del'ver") | ACCEPT-BAND | Accept and deliver: accepts cad_to_scan_observable, zone:I1 nozzle spigot OD lugs latch:cad_to_scan and zone:I5 ring windows:cad_to_scan band misses, gate a7a0a18a5df9 (created 2026-09-28T14:32:56+00:00); remaining misses are unscanned bore floor and scanner bridge membranes, no rebuild target left per independent verify it2. | decisions/accept_band.md
