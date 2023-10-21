import matplotlib.pyplot as plt
import numpy as np

a = 4
b = 3
c = 7

x_values = np.arange(-5, 5 + 1, 1)
y1_values = a * x_values ** 2
y2_values = b * x_values + c

fig, ax = plt.subplots(figsize=(5, 5))

ax.plot(x_values, y1_values, color="green", linestyle="-.", linewidth=1.5, label="y1(x)")

ax.scatter(x_values, y2_values, color="blue", marker="*", label="y2(x)")

ax.legend(loc="upper right")

ax.set_title("Графики функций y1(x) и y2(x)", fontsize=16, color="red")

ax.set_xlabel("x", fontsize=16, color="red")
ax.set_ylabel("y", fontsize=16, color="red")

plt.show()