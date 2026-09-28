# MEASUREMENTS — OD-H21_antidrip-valve (request)

Instrument: digital caliper (state model and resolution when filled); thread gauge for T-01.
Date measured: not measured — scan-only job (DECISIONS.md MEASUREMENTS, 2026-09-28).
Status summary: 0 of 17 rows carry a value; all are ABSENT, not passed. Any reading returned later
is a re-run trigger (CHK-SCALE, Tier-1).

"Scan says" is the scan-predicted value in the datum frame (intake/alignment.json; per-feature
fits in measure/figures/fits.json). Do NOT copy it into the reading column.

## A. Envelope (first; drives CHK-SCALE)
| ID | Feature | Jaw placement (photo ref) | Scan says | Reading (mm) | Status | Photo id | Notes |
|---|---|---|---|---|---|---|---|
| ENV-Z | overall length, nozzle tip face → top of the barb tube (the true topmost feature) | tip face and barb crest, part standing on the tip | 55.94 (datum z −27.455 … 28.483) | | absent | photo_2 | cap part is tilted 3.4°: read at the barb crest |
| ENV-X | nozzle axis → outlet end face | outlet end face and the nozzle OD, subtract Ø/2 | 29.98 (outlet u) | | absent | photo_2 | |
| ENV-Y | barb end face → opposite ring skirt | across the part along the barb | 28.37 + 13.27 ≈ 41.6 | | absent | photo_1 | |

## B. Functional dimensions (priority order)
| ID | Feature | Type | Datum ref | Why it matters | Jaw placement | Scan says | Reading | Status | Photo id |
|---|---|---|---|---|---|---|---|---|---|
| F-01 | nozzle OD | Ø | nozzle axis | plug-in spigot fit | outside jaws mid-length | 11.560 | | absent | photo_2 |
| F-02 | nozzle bore | Ø | nozzle axis | flow bore | inside jaws at the tip | 7.883 | | absent | photo_2 |
| F-03 | lug span, wide pair (across the latch-window sides) | width | lug rectangle | latch geometry | outside jaws on the flats at θ 114 / −66 | 11.93 | | absent | photo_2 |
| F-04 | lug corner-to-corner | width (max) | lug rectangle | bayonet reach | across opposite corners | 15.98 | | absent | photo_2 |
| F-05 | shoulder → nozzle tip | depth | shoulder face | insertion depth | depth rod | 13.26 | | absent | photo_2 |
| F-06 | outlet thread major Ø | Ø | outlet axis | sealed port | outside jaws on the crests | 9.15 (scan crest p99; scanner-smoothed) | | absent | photo_2 |
| F-07 | outlet thread pitch | pitch | outlet axis | G1/8 identification | thread gauge | 0.908 | | absent | photo_2 |
| F-08 | O-ring OD / cross-section | Ø / Ø | outlet axis | seal | outside jaws; remove O-ring for the section | 10.69 / 1.83 | | absent | photo_1 |
| F-09 | outlet collar OD | Ø | outlet axis | O-ring seat | outside jaws | 13.70 | | absent | photo_2 |
| F-10 | barb tube OD | Ø | barb axis | hose | outside jaws mid-tube | 5.50 | | absent | photo_1 |
| F-11 | barb bulb max OD | Ø | barb axis | hose retention | outside jaws at the bulb shoulder | 7.36 (p50) – 7.76 (p90) | | absent | photo_1 |
| F-12 | ring window width / height | width | cap axis | snap latch | inside jaws | 3.0–4.15 / 1.9–2.6 (per window) | | absent | photo_2 |

## C. Wall thicknesses / second tier
| ID | Feature | Jaw placement | Scan says | Reading | Status | Photo id |
|---|---|---|---|---|---|---|
| C-01 | cap Ø | outside jaws | 24.28 | | absent | photo_2 |
| C-02 | ring skirt Ø | outside jaws | 26.54 | | absent | photo_2 |
| C-03 | nut rib crest Ø (across two opposite ribs) | outside jaws | 23.99 (rib peaks, mean) | | absent | photo_2 |
| — | internal bores beyond the observed mouths | not visible — needs a sectioned part or a CT scan | — | | N/A | — |

## D. Photo-transcribed candidates — confirm the attribution or strike it
| ID | Photo | Reading | Inferred feature | Maps to | Confirmed by / date |
|---|---|---|---|---|---|
| — | none (catalogue photos carry no readings) | | | | |

## E. Extra dims measured on the operator's own initiative
| ID | Feature | Reading | Notes |
|---|---|---|---|
