# ACCEPT-BAND — OD-E02_control-button-board

Date: 2026-09-28. Who: Ikbal (owner), question card in the session ("Accept and deliver").

Gate: `qa/gate.json` sha256 prefix 1e9b7dcea587 (created 2026-09-28T08:54:19+00:00), verdict BAND_NOT_MET,
iteration 3 of 3, regime baseline-skill plastic.

Accepted band misses (from gate.json#band_fails):
- scan_to_cad:masked — max misses (9 of 294,367 scan points over the band, at the B1 side-collar cut);
  p95 passes.
- cad_to_scan_observable — p95 and max miss; 98.5 % of the over-band CAD points lie in openings the scanner
  never reached (connector shroud interior, shroud-to-rim slot, screw bores).

What the owner was shown before deciding: the two band misses with their numbers, the per-region explanation
(qa/VERDICT.md), and the options (accept and deliver, or stop and supply a re-scan / depth readings).
Decision: accept and deliver. Re-run trigger: a re-scan covering the openings or depth readings of them.
