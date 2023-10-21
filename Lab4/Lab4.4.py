import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return x ** 2

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, f(X, Y), cmap="coolwarm")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")

plt.show()