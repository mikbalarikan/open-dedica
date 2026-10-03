"""RV01: my own variant at the wall plane's +0.1 limit (inner face z -299 -> -298.9 over the foot strip y 0..4):
saved as a mutant STEP for the rim distance reading in m5 (quick mode)."""
from build123d import Box, Location
from tools.core import read_step, write_step
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"
p = read_step(f"{J}/02_STEP_STL/od_c11_back_C1_v03.step")
m = p.fuse(Box(232, 4, 0.1).moved(Location((0, 2, -298.95)))).clean()
write_step(m, f"{W}/mutants/variant_wall_inner_m298p9.step", timestamp="2026-10-01T00:00:00")
