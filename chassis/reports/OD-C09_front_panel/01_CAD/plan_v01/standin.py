"""Planning probe only (never exported, never delivered): spec section 4 C1 features as plain
boxes and cylinders, so D1 can measure clearances against the planned panel."""
from build123d import Box, Cylinder, Pos, Solid
from OCP.BRepAlgoAPI import BRepAlgoAPI_Fuse


def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0+x1)/2, (y0+y1)/2, (z0+z1)/2) * Box(x1-x0, y1-y0, z1-z0)


def cyl_z(cx, cy, r, z0, z1):
    return Pos(cx, cy, (z0+z1)/2) * Cylinder(r, z1-z0)


def panel(holes, boss_axes, boss_end, boss_d=11.0, hole_d=15.0):
    """holes: list of (x, y, d); boss_axes: [(x, y)]; boss_end: z of each boss end."""
    wall = box(-116, 116, 0, 215, 94, 97)
    wall = wall - box(-75, 75, 0, 50, 93, 98) - box(-57.5, 75, 0, 188, 93, 98)
    for x, y, d in holes:
        wall = wall - cyl_z(x, y, d/2, 93, 98)
    parts = {"wall": wall,
             "R1": box(-60.5, 78, 188, 191, 84, 94), "R2": box(75, 78, 0, 191, 84, 94),
             "R3": box(-60.5, -57.5, 50, 191, 84, 94), "R4": box(-78, -75, 0, 53, 84, 94),
             "R5": box(-78, -57.5, 50, 53, 84, 94),
             "FL": box(-104, -76, 0, 4, 72, 94), "FR": box(76, 104, 0, 4, 72, 94)}
    for i, ((x, y), ze) in enumerate(zip(boss_axes, boss_end)):
        parts[f"boss{i}"] = cyl_z(x, y, boss_d/2, ze, 94)
    return parts
