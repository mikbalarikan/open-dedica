"""Run-local wrapper (owner override 2026-09-28, decisions/owner_override_2026-09-28.md).
Runs one stl-re-deliver script with HALT added to _common.DELIVERABLE_VERDICTS for THIS run only.
Every other preflight check (inputs unchanged, hash freeze, headline verdict, regime, superseded)
is untouched. Usage: python3 override_run.py <script.py> [script args...]"""
import runpy, sys
from pathlib import Path
SCRIPTS = Path('/home/user/agentic_STL-to-CAD/skills/stl-re-deliver/scripts')
sys.path.insert(0, str(SCRIPTS))
import _common
_common.DELIVERABLE_VERDICTS = tuple(_common.DELIVERABLE_VERDICTS) + ('HALT',)
script = sys.argv[1]
sys.argv = [str(SCRIPTS / script)] + sys.argv[2:]
runpy.run_path(str(SCRIPTS / script), run_name='__main__')
