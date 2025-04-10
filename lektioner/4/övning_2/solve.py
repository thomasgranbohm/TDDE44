import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("AGG")

def f(x):
    return x * x

def get_x_squared(x_values):
    return [f(x) for x in x_values]

plt.figure()

plt.plot(get_x_squared(list(range(-5, 6))))

plt.savefig("övning_2.png")