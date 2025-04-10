import matplotlib
import matplotlib.pyplot as plt

from module import get_x_squared

matplotlib.use("AGG")

plt.figure()

x_values_1 = list(range(-50, -20 + 1))
x_values_2 = list(range(20, 50 + 1))

plt.plot(x_values_1, get_x_squared(x_values_1))
plt.plot(x_values_2, get_x_squared(x_values_2))

plt.savefig("figur.png")