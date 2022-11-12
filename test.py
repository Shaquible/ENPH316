import numpy as np
from scipy.linalg import expm
v = np.array([[0, 1], [-1, 0]])
print(v)
print(expm(v))
