# mandelbrot.py
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


n = 1000
# generate a grid of points
a = np.linspace(-10, 10, n)
b = np.linspace(-10, 10, n)
# check if the point is in the mandelbrot set and if it is plot it on the graph
# 10 iterations of the function are done and it is removed from the set if the
# magnitude of the point is greater than 100
sucsess = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        sucsess[j][i] = mandelbrotEsq(a[i], b[j], 10, 100)
# plot the points with a histogram and a color map legend
plt.imshow(sucsess, cmap='afmhot', extent=[-10, 10, -10, 10])
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.savefig('mandelbrot.png', dpi=800)
