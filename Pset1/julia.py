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

n = 1000
x = np.linspace(-2, 2, n)
y = np.linspace(-2, 2, n)
for i in range(n):
    for j in range(n):
        if julia(x[i], y[j], a, b, 15, 1000):
            plt.plot(x[i], y[j], 'k.', markersize=0.3)

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()
