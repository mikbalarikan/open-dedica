"""Reviewer helpers: regions and ray probes (own code)."""
import math
from build123d import Cylinder, Box, Pos, Rot, Align, Solid
from tools.measure import radial_extent
C = (Align.CENTER, Align.CENTER, Align.MIN)
def ann(r0, r1, z0, z1, x=0, y=0):
    s = Pos(x, y, z0) * Cylinder(r1, z1 - z0, align=C)
    if r0 > 0: s = s - Pos(x, y, z0 - 1) * Cylinder(r0, z1 - z0 + 2, align=C)
    return s
def box(x0,x1,y0,y1,z0,z1):
    return Pos(x0, y0, z0) * Box(x1-x0, y1-y0, z1-z0, align=(Align.MIN,)*3)
def sector(theta_c, half_deg, r0, r1, z0, z1):
    """annular sector about Z centred on theta_c (deg)."""
    a = ann(r0, r1, z0, z1)
    big = 3 * r1
    # wedge from two half-planes: keep points within +-half of theta_c
    w = Pos(0, 0, z0 - 1) * Box(big, big, z1 - z0 + 2, align=(Align.MIN, Align.MIN, Align.MIN))
    lo = Rot(0, 0, theta_c - half_deg) * w          # quadrant starting at theta_c-half
    hi = Rot(0, 0, theta_c + half_deg - 90) * w      # quadrant ending at theta_c+half
    assert half_deg <= 45
    return a & lo & hi
def ray(shape, origin, direction, side="inner", window=(0, None)):
    """first/last material along a ray from origin in direction (unit), via radial_extent."""
    d = [float(c) for c in direction]; n = math.sqrt(sum(c*c for c in d)); d = [c/n for c in d]
    # pick an axis perpendicular to d
    a = (0, 0, 1) if abs(d[2]) < 0.9 else (1, 0, 0)
    # make axis exactly perpendicular: a - (a.d)d
    dot = sum(x*y for x, y in zip(a, d)); ax = [x - dot*y for x, y in zip(a, d)]
    m = math.sqrt(sum(c*c for c in ax)); ax = [c/m for c in ax]
    return radial_extent(shape, tuple(origin), tuple(ax), tuple(d), 0.0, 0.0, side=side, r_min=window[0], r_max=window[1])
def stretches(res):
    return res.detail.get("material", []) if res.measured is not None else []
