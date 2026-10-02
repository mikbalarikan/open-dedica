# REQUEST — OD-C12, OD-C13 side panels and OD-C16 corner brackets

Written for this job from the Usta's words in the project thread (2026-10-02 22:58 UTC) and the project's standing instruction; the Usta's message is quoted verbatim.

## The Usta's message (2026-10-02 22:58 UTC), answering four open questions

> 1/ merge
> 2/ accept
> 3/ printed
> 4/ 7mm
>
> all printed in pla for now

Question 3 was "Acrylic or printed side panels. This decides how C12, C13 and C16 get designed." The answer is **printed**. "All printed in PLA for now" sets the material of every printed part of this job.

## What the job delivers

- OD-C12 left side panel and OD-C13 right side panel of the Open Dedica machine, 3D-printed (not 3 mm acrylic skins), in PLA.
- OD-C16 corner brackets: the BOM row says "Corner bracket for acrylic skins (optional)", qty 16; with printed panels the bracket is the part that fastens the panels to the base frame OD-C01 (this job's design choice, to be stated in the spec).
- Per part: parametric build script, STEP (mm, one named solid), STL and 3MF, and one independent review, as every chassis part (chassis/README.md "Goal").

## Constraints stated by the project (coordinator brief, 2026-10-02)

- The top panel OD-C10 currently leans on a left rest pad until the side panels carry its edges (OD-C10 RV01 F1; C08_C11_integration_notes.md): the side panels should end at y 215 under the lid's 3 mm skirt (x ±117 … ±120).
- Keep the Ø8 × 2 screw-head keep-out above each OD-C15 foot hole free (C15_integration_notes.md).
- The shared files (docs/bom.csv, chassis/README.md, OD-000) belong to another thread: this job hands its changes over in integration notes and edits none of them.
