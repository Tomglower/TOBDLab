import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (x ** 2 + 5)/((2 * y)-1)

x = np.arange(-5, 5, 0.2)
y = np.arange(3, 18, 0.3)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, f(X, Y), cmap="coolwarm")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")

plt.show()