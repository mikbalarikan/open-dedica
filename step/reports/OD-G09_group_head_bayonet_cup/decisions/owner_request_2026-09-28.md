# Owner request (Ikbal, chat, 2026-09-28)

Verbatim (Turkish): "yeni bir STL tersine mühendislik görevi: p95 plastik parça toleransı kullan.
STL ve image ler ekte. İş bittiğinde zip dosyasında bütün source file ve deliverables olarak
indirebilir şekilde deliver et."

Read as:
- REGIME: baseline-skill, material class plastic (p95 <= 0.30 / max <= 0.80 mm,
  baseline/skills/stl2step-build123d/SKILL.md:87). Chosen by the owner.
- Inputs: one STL (`77049a24-OD-G10-Porta-Filter-Holder.stl`) and two photos (1.webp, 2.webp).
  No caliper sheet was supplied; the owner asked for an end-to-end delivery, so the run proceeds
  scan-only with the two scan-only limitations declared (Tier-1 not run; absolute scale not
  caliper-verified).
- Scan resolution: not stated. Declared `full` by the agent: the file is the owner's upload as
  exported (400,123 faces, a non-round count; 20.0 MB binary STL; no "decimated" in the name).
  Re-run trigger if the owner says it was decimated.
- Delivery: one zip with deliverables + all source files (standing format,
  skills/stl-re-deliver/references/delivery-package.md).
