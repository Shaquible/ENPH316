import numpy as np
import matplotlib.pyplot as plt


def f(x, a):
    return (1-a*np.cos(x))/(1-2*a*np.cos(x)+a**2)


def fN(x, a, N):
    if (N == 0):
        return 1
    else:
        return a**N*np.cos(N*x) + fN(x, a, N-1)


xs = np.linspace(0, 2*np.pi, 1000)
ys = f(xs, 0.3)
ns = [2, 5, 10, 20, 50, 100]
for n in ns:
    ysN = fN(xs, 0.3, n)
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(xs, ys, label='analytical')
    ax[0].plot(xs, ysN, label='N = {}'.format(n))
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[0].legend()
    ax[0].set_title('N = {}'.format(n))
    ax[1].plot(xs, ys-ysN)
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('y')
    ax[1].set_title('residuals')
    # save figure
    fig.add_axes(ax[0])
    fig.add_axes(ax[1])
    fig.savefig('pset3_{}.png'.format(n))
    plt.clf()
