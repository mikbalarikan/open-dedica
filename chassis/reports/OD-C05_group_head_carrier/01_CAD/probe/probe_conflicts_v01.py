"""WP-02 probe (J2): measure two spec-value interactions on probe coupons (not the carrier).
Coupon A: the wall's top-right corner (R 8 corner arc centred (42, 42), wall z -29.94 .. -24.94)
with the spec's Ø3.4 hole and Ø6.5 x 2.0 counterbore at (44, 44): min_wall there (D-01b, U-06).
Coupon B: a 5.0 wall along Z with one Ø3.4 hole and a Ø6.5 x 2.0 counterbore along Z, printed with
build direction +Y: overhang_census (D-03a) reads the horizontal hole crowns."""
import json
from pathlib import Path
from build123d import Box, Cylinder, Location, Pos, Rectangle, RectangleRounded, extrude, Plane, fillet, Axis
from tools.measure import min_wall, min_wall_wide, overhang_census

WS = Path(__file__).resolve().parents[2]
out = {}
Z_REAR, Z_FRONT = -29.94, -24.94
T = Z_FRONT - Z_REAR
# coupon A: square x 30..50, y 30..50 with the (50, 50) corner rounded R 8 (centre (42, 42))
blk = Box(20, 20, T, align=None).moved(Location((30, 30, Z_REAR)))
corner_edge = blk.edges().filter_by(Axis.Z).sort_by(Axis.X)[-1:]  # probe only
corner_edge = [e for e in blk.edges().filter_by(Axis.Z) if abs(e.center().X - 50) < 1e-6 and abs(e.center().Y - 50) < 1e-6]
blk = fillet(corner_edge, 8.0)
hole = Cylinder(1.7, T + 2, align=None).moved(Location((44, 44, Z_REAR - 1)))
cb = Cylinder(3.25, 2.0 + 1, align=None).moved(Location((44, 44, Z_REAR - 1)))
coupon_a = blk - hole - cb
for label, cbd in (("nominal", 6.5), ("cb_high_6.6", 6.6)):
    c = blk - hole - Cylinder(cbd / 2, 3.0, align=None).moved(Location((44, 44, Z_REAR - 1)))
    mw = min_wall(c)
    out[f"coupon_a_min_wall_{label}"] = {"measured": mw.measured, "status": mw.status, "at": mw.at,
                                         "reason": mw.reason, "wide": mw.detail.get("wide")}
# coupon B
wall = Box(30, 30, T, align=None).moved(Location((-15, -15, Z_REAR)))
cb_b = wall - Cylinder(1.7, T + 2, align=None).moved(Location((0, 0, Z_REAR - 1))) \
            - Cylinder(3.25, 3.0, align=None).moved(Location((0, 0, Z_REAR - 1)))
oc = overhang_census(cb_b, build_dir=(0, 1, 0))
out["coupon_b_overhang_census"] = {"measured": oc.measured, "status": oc.status, "at": oc.at, "reason": oc.reason,
                                    "per_kind_least_deg": oc.detail.get("per_kind_least_deg"),
                                    "below_min_deg": oc.detail.get("below_min_deg")}
print(json.dumps(out, indent=1, default=str))
(WS / "01_CAD/probe/probe_conflicts_v01.json").write_text(json.dumps(out, indent=1, default=str))
