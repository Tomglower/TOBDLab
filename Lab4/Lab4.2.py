import matplotlib.pyplot as plt
import numpy as np
import math

a = 2
b = 3
c = 1
d = -4
h = 0.1 

def y1(x):
    return math.cos(b * x)

def y2(x):
    return math.cos(b + x)

def y3(x):
    return a * math.cos(b*x)

def y4(x):
    return a * math.pow(x,2)

def y5(x):
    return a * math.pow(x,2) + c

def y6(x):
    return a * x + b * math.pow(x,2)

x_values = np.arange(-10, 10, h)
y1_values = []
y2_values = []
y3_values = []
y4_values = []
y5_values = []
y6_values = []

for x in x_values:
    y1_values.append(y1(x))
    y2_values.append(y2(x))
    y3_values.append(y3(x))
    y4_values.append(y4(x))
    y5_values.append(y5(x))
    y6_values.append(y6(x))

# Построим графики функций
fig1, ax1 = plt.subplots()
ax1.plot(x_values, y1_values, label="y1(x)")
ax1.plot(x_values, y2_values, label="y2(x)")
ax1.plot(x_values, y3_values, label="y3(x)")
ax1.legend()
ax1.set_xlabel("x")
ax1.set_ylabel("y")

fig2, ax2 = plt.subplots()
ax2.plot(x_values, y4_values, label="y4(x)")
ax2.plot(x_values, y5_values, label="y5(x)")
ax2.plot(x_values, y6_values, label="y6(x)")
ax2.legend()
ax2.set_xlabel("x")
ax2.set_ylabel("y")

plt.show()