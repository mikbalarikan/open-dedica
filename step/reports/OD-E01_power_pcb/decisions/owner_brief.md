# Owner brief (2026-09-28, Ikbal, session chat)

Verbatim request (Turkish):

> yeni bir STL tersine mühendislik görevi:
> p95 plastik parça toleransı kullan.
> STL ve image ler ekte. İş bittiğinde zip dosyasında bütün source file ve deliverables olarak
> indirebilir şekilde deliver et.

Inputs supplied: `fe50d1cd-OD-E01-Power-PCB.stl` (-> `input/scan.stl`) and four product photos
(-> `input/photos/1.png` .. `4.png`, web/catalogue photos of the same PCB, board id `PCB00572-01`
readable in photos 1 and 4). No caliper sheet, no drawing.

Agent reading of the brief:
- "p95 plastik parça toleransı" = regime `baseline-skill`, material class `plastic`
  (p95 <= 0.30 / max <= 0.80 mm, `baseline/skills/stl2step-build123d/SKILL.md:87`).
- No calipers were supplied and the owner asked for a finished delivery -> scan-only run.
- The part is a populated PCB (board + components), not a moulded plastic part; the owner still
  named the plastic band. It is modelled as ONE fused envelope solid (board + component bodies),
  which is what an enclosure / fit design needs; a per-component multi-body assembly is not
  produced (orchestrate §6: multi-body STEP is a separate job).
- Delivery = the standing zip format (`skills/stl-re-deliver/references/delivery-package.md`).
