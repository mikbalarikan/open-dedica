import sys, build123d
from importlib.metadata import distributions
ocp = [f"{d.metadata['Name']} {d.version}" for d in distributions() if "ocp" in d.metadata["Name"].lower()]
print(sys.version.split()[0], build123d.__version__, ocp)
