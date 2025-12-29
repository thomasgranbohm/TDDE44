#!/usr/bin/python

import matplotlib
import matplotlib.pyplot as plt
import os

matplotlib.use("AGG")

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def load_csv(filename):
    """Laddar in CSV-filen med data och parsar den"""
    with open(filename, "r") as file:
        lines = []
        for line in file.readlines():
            values = []
            for x in line.split(";"):
                try:
                    values.append(int(x))
                except ValueError:
                    values.append(x)
            lines.append(values)
        return lines


def prepare_output():
    """Skapar outputs-mappen om den inte redan finns."""
    PATH = BASE_PATH + "/outputs"
    if not os.path.isdir(PATH):
        os.makedirs(PATH, exist_ok=True)


def draw_diagram(values, filenames):
    """Sätter upp skelettet för en matplotlib figure."""
    plt.figure()

    for [x_values, y_values], filename in zip(values, filenames):
        plt.plot(x_values, y_values, label=filename)

    plt.legend(loc="upper left", bbox_to_anchor=(1, 0, 1, 1))

    return plt


def save_diagram(diagram, path):
    """Sparar plotten"""
    diagram.savefig(BASE_PATH + "/outputs/" + path, bbox_inches="tight")


def get_basename(path):
    """Returnerar filnamn utan path och extension."""
    return ".".join(path.split("/")[-1].split(".")[:-1])


if __name__ == "__main__":
    lines = load_csv("csv/AdaLovelace.csv")
    print(lines)
