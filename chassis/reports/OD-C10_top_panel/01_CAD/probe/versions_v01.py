"""D0: Python, build123d and OCP versions for the REPORT."""
import sys
from importlib.metadata import distributions

import build123d

ocp = sorted(f"{d.metadata['Name']} {d.version}" for d in distributions() if "ocp" in d.metadata["Name"].lower())
print(sys.version.split()[0], build123d.__version__, ocp)
