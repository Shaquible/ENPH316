# julia.py
import numpy as np
import matplotlib.pyplot as plt


def julia(x, y, a, b, n, thresh):
    for i in range(n):
        #zn = zn**2 + c
        xn = x**2 - y**2 + a
        yn = 2*x*y + b
        if np.linalg.norm([xn, yn], 2) > thresh:
            return False
        x = xn
        y = yn
    return True


a = -0.83
b = 0.18

n = 2000
x = np.linspace(-2, 2, n)
y = np.linspace(-2, 2, n)
sucsess = np.zeros((n, n))
# check if the point is in the julia set and if it is plot it on the graph
# 15 iterations of the function are done and it is removed from the set if the
# magnitude of the point is greater than 1000
for i in range(n):
    for j in range(n):
        sucsess[j][i] = julia(x[i], y[j], a, b, 15, 1000)
# plot the points with a histogram
plt.imshow(sucsess, cmap='afmhot', extent=[-2, 2, -2, 2])
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.savefig('julia.png', dpi=800)
