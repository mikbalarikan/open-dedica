# DECISIONS — OD-G04_brewing-gasket-support

Human decisions that gate this run. One entry per decision; never edit an old entry,
append a new one. Format: `- <date> | <who> | <decision id> | <decision> | <evidence path>`

Decision ids: REGIME (band regime chosen at intake), MEASUREMENTS (calipers supplied /
proceed scan-only), PART-CLASS (unsupported class: proceed or stop), ACCEPT-BAND
(BAND_NOT_MET accepted for delivery), HALT (reason and options), INDEP (verify could not
run in a fresh context), OTHER.

- 2026-09-25 | Ikbal (owner, session message) | REGIME | "p95 plastik parça toleransı kullan" -> baseline-skill, material_class plastic: p95 <= 0.30 / max <= 0.80 mm (baseline/skills/stl2step-build123d/SKILL.md:87). Declared before any gate numbers exist. | session message; intake/regime.json
- 2026-09-25 | Ikbal (owner, session message) | MEASUREMENTS | No calipers supplied; proceed scan-only. Limitations carried to verdict: "Tier-1 not run" and "absolute scale not caliper-verified", re-run trigger: any caliper reading. Photos (4 catalogue images, no scale reference) are feature-identification only. | session message; input/INPUT_HASHES.json
- 2026-09-25 | orchestrator (agent) | OTHER | scan_resolution recorded as `full`: 484,578 faces, one body, mean edge 0.241 mm, original upload file name (not a *_decimated export); same source/quality as OD-H22 which the owner confirmed full-res. Re-run trigger: owner states the scan was decimated. | input/INPUT_HASHES.json#scan_resolution
- 2026-09-25 | Ikbal (owner, decision card) | ACCEPT-BAND | Accept and deliver: accepts scan_to_cad and cad_to_scan_observable band misses, gate 6b2ca357f5c3 (created 2026-09-25T14:13:14+00:00) | decisions/accept_band.md
