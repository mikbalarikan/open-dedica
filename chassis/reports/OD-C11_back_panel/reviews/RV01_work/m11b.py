"""RV01 U-04 debug: why the round trip is INCONCLUSIVE (reason), and compare_step of the re-read part against its own file."""
from tools.core import read_step, step_roundtrip, compare_step
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"
s = read_step(f"{J}/02_STEP_STL/od_c11_back_C1_v03.step")
rt = step_roundtrip(s, f"{W}/roundtrip_part.step", timestamp="2026-10-01T00:00:00")
print({k: v.reason for k, v in rt.items()})
c = compare_step(s, f"{J}/02_STEP_STL/od_c11_back_C1_v03.step")
print({k: (v.measured, v.status, v.reason[:80]) for k, v in c.items()})
