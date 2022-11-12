import numpy as np
import matplotlib.pyplot as plt


def y(x, m):
    y = np.pi/2*np.ones_like(x)
    for M in range(0, m):
        y = y - 4/np.pi*np.cos((2*M+1)*x)/(2*M+1)**2
    return y


def g(x, m):
    g = np.zeros_like(x)
    for M in range(0, m):
        g = g + 4/np.pi*np.sin((2*M+1)*x)/(2*M+1)
    return g


def h(x, m):
    h = np.zeros_like(x)
    for M in range(0, m):
        h = h + 4/np.pi*np.cos((2*M+1)*x)
    return h


xs = np.linspace(-np.pi, np.pi, 1000)

yreal = abs(xs)
plt.plot(xs, yreal, label='real')
Is = [1, 3, 5, 10, 20, 50]

for i in Is:
    plt.plot(xs, y(xs, i), label='m = %d' % i)
plt.legend()
plt.show()

greal = xs/abs(xs)
plt.plot(xs, greal, label='real')
for i in Is:
    plt.plot(xs, g(xs, i), label='m = %d' % i)

plt.legend()
plt.show()

# hreal is dirac delta function
for i in Is:
    plt.plot(xs, h(xs, i), label='m = %d' % i)
# set y limit to be -1 to 5

plt.legend()
plt.show()
