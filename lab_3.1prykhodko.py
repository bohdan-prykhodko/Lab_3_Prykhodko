import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    dx = -y
    dy = x - 3*x**2
    return dx, dy


x = np.linspace(-1.5, 1.5, 40)
y = np.linspace(-1.5, 1.5, 40)
X, Y = np.meshgrid(x, y)

DX, DY = f(X, Y)

plt.figure(figsize=(8, 8))


plt.streamplot(X, Y, DX, DY, density=1.2, linewidth=1, arrowsize=1)


plt.scatter(0, 0, color="orange", s=100)
plt.text(0.05, 0.05, "(0,0)", fontsize=12)

plt.scatter(1/3, 0, color="green", s=100)
plt.text(1/3 + 0.05, 0.05, "(1/3,0)", fontsize=12)

plt.title("Фазовий портрет: x'=-y,   y'=x-3x^2", fontsize=16)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()