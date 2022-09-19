import numpy as np
import matplotlib.pyplot as plt


def mandelbrotEsq(a, b, n, thresh):
    xn = 0
    yn = 0
    for i in range(n):
        x = np.exp(xn)*np.cos(yn)+a
        y = np.exp(xn)*np.sin(yn)+b
        if np.linalg.norm([x, y], 2) > thresh:
            return False
        xn = x
        yn = y
    return True


n = 400
a = np.linspace(-10, 10, n)
b = np.linspace(-10, 10, n)

# check if the point is in the mandelbrot set and if it is plot it on the graph
for i in range(n):
    for j in range(n):
        if mandelbrotEsq(a[i], b[j], 5, 100):
            plt.plot(a[i], b[j], 'k.', markersize=0.3)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()
