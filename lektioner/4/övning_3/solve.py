import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("AGG")

data_1 = {(0, 1), (5, 10), (10, 17)}
data_2 = {(3, 3), (6, 6), (9, 9)}

plt.figure()

plt.plot([a[0] for a in data_1], [a[1] for a in data_1])
plt.plot([a[0] for a in data_2], [a[1] for a in data_2])

plt.savefig("figur.png")