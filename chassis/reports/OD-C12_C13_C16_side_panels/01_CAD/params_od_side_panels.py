"""One parameter structure for OD-C12, OD-C13, OD-C16 and the check assembly (spec 1.1, plan section 4).

Every build script imports `P` (the nominal set) or a `replace(P, ...)` of it (the D7 sweep).
No dimension is written anywhere below this file. Sources are in the plan's parameter
table, amended by spec 1.1 (REPORT section 8).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field, replace  # noqa: F401  (replace is re-exported for the sweep)


@dataclass(frozen=True)
class Params:
    # --- panel wall (spec 1.1 section 4 Wall; REQ-01), OD-C13 frame = machine frame ---
    wall_inner_x: float = 117.0
    wall_outer_x: float = 120.0
    wall_y0: float = 0.0
    wall_top_y: float = 215.0
    wall_z_rear: float = -295.0          # 1.1 Q2: square ends where the plate's corner arcs begin
    wall_z_front: float = 90.0
    # --- top rail (1.1 section 4 Top rail) ---
    rail_inner_x: float = 110.0
    rail_y0: float = 205.0
    rail_z0: float = -280.0
    rail_z1: float = 80.0
    # --- lip wedge (1.1 section 4 Lip; REQ-02; D-04d) ---
    lip_outer_x: float = 116.6           # fit-critical: 0.40 to OD-C10's skirt inner face x 117.0
    lip_slope_deg: float = 60.0          # from the panel's plane; apex y = 215 + (outer - inner) / tan(60)
    lip_z0: float = -280.0
    lip_z1: float = 80.0
    # --- panel holes (REQ-03) ---
    panel_hole_d: float = 3.4            # fit-critical
    panel_hole_y: float = 10.0           # fit-critical (coaxial with the bracket's insert bore)
    hole_z: tuple = (-262.0, -15.0, 62.0)  # z_c, section 2 poses, A-07
    panel_hole_dy: float = 0.0           # sweep offsets of the panel holes (0 at nominal)
    panel_hole_dz: float = 0.0
    # --- OD-C12 relief (1.1 Q4; REQ-04) ---
    relief_floor_x: float = -117.9       # fit-critical (OD-C07 clearance; wall 2.1)
    relief_y1: float = 55.0
    relief_z0: float = -160.0
    relief_z1: float = -29.0
    # --- OD-C16 bracket, its own frame (section 4 OD-C16; REQ-05) ---
    block_x0: float = -19.0
    block_x1: float = 0.0
    block_y1: float = 16.0
    block_half_z: float = 8.0
    br_hole_d: float = 3.4               # fit-critical
    br_hole_x: float = -12.5             # fit-critical: plate hole at x +-104.5 when placed
    br_hole_z: float = 0.0
    cbore_d: float = 6.5                 # fit-critical
    cbore_floor_y: float = 3.0           # fit-critical
    insert_bore_d: float = 4.0           # fit-critical (D-05b, A-12)
    insert_bore_depth: float = 6.0       # fit-critical (D-05b)
    insert_bore_y: float = 10.0          # fit-critical (coaxial with the panel hole)
    insert_bore_z: float = 0.0
    # --- placements (section 2) ---
    bracket_origin_x: float = 117.0
    # --- export (U-07; DESIGN_PLAN parameter table) ---
    stl_tol: float = 0.01
    step_timestamp: str = "2026-10-02T00:00:00"
    # --- cutter overrun: a through cut runs this far past both faces it opens (derivation: any
    #     value > 0 that clears the face; 1.0 is far above OCCT's tolerances and touches nothing) ---
    overrun: float = 1.0

    @property
    def lip_top_y(self) -> float:
        """Apex of the wedge: rise = run / tan(slope) (spec 1.1: 218.81 at nominal)."""
        return self.wall_top_y + (self.lip_outer_x - self.rail_inner_x) / math.tan(math.radians(self.lip_slope_deg))

    def stl_angular(self, r_max: float) -> float:
        """U-07: a = 4 * acos(1 - tol / R_max) rad, R_max the part's largest curved-face radius."""
        return 4.0 * math.acos(1.0 - self.stl_tol / r_max)


P = Params()
