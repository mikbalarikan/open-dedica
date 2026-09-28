# ACCEPT-BAND — OD-G11_portafilter, iteration 2

Owner: Ikbal (session messages, 2026-09-28).
- Message 1, while the iteration-2 verify was running: "teslim et artık".
- Message 2, same period: "tamam, band kaçarsa kabul ediyorum, teslim et" (accepts any band miss for delivery).

Before message 2 the owner was told how it would be recorded: a verdict of BAND_NOT_MET would be accepted by
quoting this message, and the acceptance would be bound to the resulting gate. A REVISE verdict was explicitly
excluded; the owner would be asked again. The verdict came back BAND_NOT_MET, so this acceptance applies.

Bound to gate: `qa/gate.json` sha256 prefix **0f2d41f2bdd2**, created 2026-09-28T11:17:26+00:00.
Missed bands accepted (gate.json#band_fails):
- scan_to_cad:masked — p95 passes (within 0.30); max misses the 0.80 band (wire arc simplification, scan-hole edges, screw-head recesses, lug ends).
- cad_to_scan_observable — p95 and max miss; driven by unscanned regions (grip strip, spout pocket bores, insert floor holes).
Numbers: see qa/gate.json and qa/VERDICT.md (not retyped here).
