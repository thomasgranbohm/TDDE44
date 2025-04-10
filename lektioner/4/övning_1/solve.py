import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("AGG")

plt.figure()

plt.plot([1, 2, 75, 6, 7])

plt.ylabel('some numbers')

plt.savefig("figur.png")