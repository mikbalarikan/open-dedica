# ACCEPT-BAND — OD-E01_Power-PCB, iteration 2 (2026-09-28)

Owner: Ikbal (session chat, answer to the agent's decision question), verbatim choice:
"Kabul et, teslim et (Önerilen)".

Accepted gate: `qa/gate.json` sha256 prefix **948b8a16472b** (created 2026-09-28T09:03:20+00:00), verdict BAND_NOT_MET,
regime baseline-skill / plastic (p95 ≤ 0.30, max ≤ 0.80 mm).

Missed bands accepted for delivery (from gate.json#band_fails):
- scan_to_cad:masked: p95 0.763 / max 1.365 (gate frame after QA ICP; the ICP lifts the CAD +0.72 mm because the
  invented board bottom matches the scanned board top; datum frame p95 0.292 / max 1.027)
- cad_to_scan_observable: p95 1.599 / max 4.408 (invented surfaces with no scan behind them: board bottom,
  deep heatsink fin/spine faces)

Options that were offered and not chosen: a solder-side / oblique scan and re-run; an ICP-radius decision and
re-verify; HALT. The model is delivered with these misses and all limitations in qa/VERDICT.md.
