import numpy as np

data = np.genfromtxt(
    "grades.csv",          # your file name
    delimiter=",",
    dtype=None,              # let NumPy figure out types
    encoding="utf-8",
    names=True               # read the header row
)

print(data[:5])