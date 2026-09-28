"""QA run-local wrapper: runs stl-re-verify/scripts/deviation_gate.py unchanged, except that the
observability ray test (observability.py:observable_split) is called with chunk=OBS_CHUNK rays per
batch instead of its default 2000. Reason: observability.py:63-84 builds per-ray candidate lists on
the ~520k-triangle QA tessellation (trimesh ray_triangle, no embree); 2000 long rays per batch can
exhaust the 15 GB machine. Chunking changes memory only; per-ray results are identical (each ray is
tested independently). Records peak RSS."""
import functools, resource, sys
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts')
import observability, deviation_gate
OBS_CHUNK = 64
observability.observable_split = functools.partial(observability.observable_split, chunk=OBS_CHUNK)
rc = deviation_gate.main(sys.argv[1:])
print(f"[run_deviation] obs chunk {OBS_CHUNK}; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB", flush=True)
raise SystemExit(rc)
