# DECISIONS — OD-E02_control-button-board

Human decisions that gate this run. One entry per decision; never edit an old entry,
append a new one. Format: `- <date> | <who> | <decision id> | <decision> | <evidence path>`

Decision ids: REGIME (band regime chosen at intake), MEASUREMENTS (calipers supplied /
proceed scan-only), PART-CLASS (unsupported class: proceed or stop), ACCEPT-BAND
(BAND_NOT_MET accepted for delivery), HALT (reason and options), INDEP (verify could not
run in a fresh context), OTHER.

- 2026-09-28 | Ikbal (owner, session message) | REGIME | baseline-skill, material_class plastic: p95 <= 0.30 / max <= 0.80 mm (baseline/skills/stl2step-build123d/SKILL.md:87). User wrote "p95 plastik parça toleransı kullan". Declared before any gate numbers exist. | session message; intake/regime.json
- 2026-09-28 | Ikbal (owner, session message) | MEASUREMENTS | No calipers supplied ("STL ve image ler ekte"); proceed scan-only. Limitations carried to verdict: "Tier-1 not run" and "absolute scale not caliper-verified", re-run trigger: any caliper reading. Photos (2 catalogue images, no scale reference) are feature identification / plausibility only. | session message; input/INPUT_HASHES.json
- 2026-09-28 | Ikbal (owner, question card) | OTHER | scan_resolution confirmed full-res (original scanner export, 586,137 faces, mean edge 0.247 mm). | input/INPUT_HASHES.json#scan_resolution
- 2026-09-28 | Ikbal (owner, session message) | OTHER | Delivery format: one downloadable zip with all source files and deliverables (standing format, stl-re-deliver/references/delivery-package.md). | session message
- 2026-09-28 | builder (agent) | OTHER | Intake CHK-ENUM missed four sub-features (inner latch bosses, hoop catch ramps, cap-collar recesses, side-collar tilted cut); the builder self-check (not QA) found them inside iteration 1 before verify; measure re-ran and params were regenerated each time (build/MODELING_PLAN.md §8). Not a loop: no verify verdict existed. | build/MODELING_PLAN.md; intake/INTAKE_CARD.md E15-E18
- 2026-09-28 | orchestrator (agent) | OTHER | Verify it1 verdict REVISE (gate errors empty, allowed BAND_NOT_MET/HALT/REVISE). Chose REVISE (loop 1 of 3, route geometry): verify names fixable geometry (band/T3 seam, band ends, header base inside the shroud, B1 collar floor). Remaining expected miss after it2: CAD->scan observable in unscanned openings. | qa/VERDICT.md
- 2026-09-28 | orchestrator (agent) | OTHER | Verify it2 verdict REVISE (gate errors empty). Loop 2 of 3 used; chose REVISE again, route geometry: verify names the B1 cap lip inside the cap-collar gap and over-deep recess ceilings as fixable. This is the last allowed loop; a REVISE at it3 means HALT. | qa/VERDICT.md
- 2026-09-28 | Ikbal (owner, question card) | ACCEPT-BAND | Accept and deliver: accepts scan_to_cad:masked (max) and cad_to_scan_observable (p95, max) band misses, gate 1e9b7dcea587 (created 2026-09-28T08:54:19+00:00); 98.5% of the CAD->scan miss is in unscanned openings (shroud interior, shroud-to-rim slot, screw bores). | decisions/accept_band.md
