"""Labb 4, del 1.

Tar in en eller flera filnamn som argument och
genererar graferna som beskrivs i uppgiften.
"""

from common import load_csv
import matplotlib
import matplotlib.pyplot as plt
import sys
import os

matplotlib.use("AGG")

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def prepare_output():
    """Skapar outputs-mappen om den inte redan finns."""
    PATH = BASE_PATH + "/outputs"
    if not os.path.isdir(PATH):
        os.makedirs(PATH, exist_ok=True)


def prepare_data1(data):
    """Samlar all data baserat på klockslag.

    x-värdena är klockslagen och
    y-värdena är den genomsnittliga mängden koppar vid det klockslaget
    """
    x_values, y_values = [], []

    for line in data[1:]:
        x_values.append(line[0])
        y_values.append(sum(line[1:]) / len(line[1:]))

    return x_values, y_values


def prepare_data2(data):
    """Samlar all data baserat på veckodag.

    x-värdena är veckodagen och
    y-värdena är den mängden koppar under den dagen
    """
    x_values, y_values = [], []

    for x in range(1, 1 + len(data[0][1:])):
        x_values.append(data[0][x])
        y_values.append(sum([data[y][x] for y in range(1, 1 + len(data[1:]))]))

    return x_values, y_values


def draw_diagram(values, filenames):
    """Sätter upp skelettet för en matplotlib figure."""
    plt.figure()

    for [x_values, y_values], filename in zip(values, filenames):
        plt.plot(x_values, y_values, label=filename)

    plt.legend(loc="upper left", bbox_to_anchor=(1, 0, 1, 1))

    return plt


def draw_diagram1(values, filenames):
    """Skapar diagramet för del 1."""
    plt = draw_diagram(values, filenames)

    plt.title("Koppar kaffe i snitt vid olika klockslag under en vecka")
    plt.ylabel("antal koppar")
    plt.savefig(
        BASE_PATH + "/outputs/{}_1.png".format("_".join(filenames)), bbox_inches="tight"
    )


def draw_diagram2(values, filenames):
    """Skapar diagramet för del 2."""
    plt = draw_diagram(values, filenames)

    plt.title("Koppar kaffe per dag")
    plt.ylabel("antal koppar")
    plt.savefig(
        BASE_PATH + "/outputs/{}_2.png".format("_".join(filenames)), bbox_inches="tight"
    )


def get_basename(path):
    """Returnerar filnamn utan path och extension."""
    return ".".join(path.split("/")[-1].split(".")[:-1])


if __name__ == "__main__":
    args = sys.argv[1:]
    filenames = []

    values_1, values_2 = [], []

    prepare_output()

    for filename in args:
        try:
            path = filename
            data = load_csv(path)
            values_1.append(prepare_data1(data))
            values_2.append(prepare_data2(data))
            filenames.append(filename)
        except FileExistsError:
            print("Could not find file '{}'".format(path))

    basenames = [get_basename(x) for x in filenames]

    draw_diagram1(values_1, basenames)
    draw_diagram2(values_2, basenames)
