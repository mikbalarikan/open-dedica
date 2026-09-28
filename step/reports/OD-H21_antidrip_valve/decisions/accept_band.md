# ACCEPT-BAND — OD-H21_antidrip-valve, iteration 2

- Date: 2026-09-28
- Who: Ikbal (owner), session message "del'ver" (= deliver), sent after the orchestrator showed the
  it2 CAD→scan heatmap (qa/overlays/heatmap_cad_to_scan.png) and said delivery needs the owner's
  band acceptance.
- Gate: qa/gate.json sha256 a7a0a18a5df9d7e109b33b1bd5e877bc1d161fb8a48049a08c7ce841fe7123b3
  (prefix a7a0a18a5df9), created 2026-09-28T14:32:56+00:00, verdict BAND_NOT_MET, errors [].
- Accepted band misses (gate.json#band_fails):
  - cad_to_scan_observable (p95 passes; max misses: the unscanned nozzle bore floor, counted observable by the ray test)
  - zone:I1 nozzle spigot OD lugs latch:cad_to_scan (max: scanner bridge membrane at the latch edge)
  - zone:I5 ring windows:cad_to_scan (p95/max: scanner bridge membranes sagging over the window openings)
- Why a rebuild cannot fix them: the independent verifier (it2) found no geometric rebuild target left;
  the remaining misses are coverage/scanner facts (qa/VERDICT.md, gate.json#miss_explanations).
  scan→CAD passes only with the declared M1 bore mask (unmasked max over band) — a mask-dependent pass,
  carried as a limitation.
