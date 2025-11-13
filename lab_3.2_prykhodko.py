import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    dx = 2*y
    dy = 4*x - 4*x**3
    return dx, dy


x = np.linspace(-2, 2, 40)
y = np.linspace(-2, 2, 40)
X, Y = np.meshgrid(x, y)

DX, DY = f(X, Y)


plt.figure(figsize=(8, 8))
plt.streamplot(X, Y, DX, DY, density=1.2, linewidth=1, arrowsize=1, color="brown")


eq_points = [(0,0), (1,0), (-1,0)]

plt.scatter(0, 0, s=120, color="red")
plt.text(0.1, 0.1, "(0,0) — сідло", fontsize=11)

plt.scatter(1, 0, s=120, color="green")
plt.text(1.1, 0.1, "(1,0) — центр", fontsize=11)

plt.scatter(-1, 0, s=120, color="green")
plt.text(-1.5, 0.1, "(-1,0) — центр", fontsize=11)


plt.title("Фазовий портрет системи:  x' = 2y,   y' = 4x − 4x³", fontsize=16)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")

plt.show()
