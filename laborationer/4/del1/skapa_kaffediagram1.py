#!/usr/bin/python

"""Labb 4, del 1.

Tar in en eller flera filnamn som argument och genererar en graf
som visar antal koppar kaffe i snitt vid olika klockslag under en vecka
"""

import sys
from common import draw_diagram, get_basename, load_csv, prepare_output, save_diagram


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


def draw_diagram1(values, filenames):
    """Skapar diagramet för del 1."""
    plt = draw_diagram(values, filenames)

    plt.title("Koppar kaffe i snitt vid olika klockslag under en vecka")
    plt.ylabel("antal koppar")
    save_diagram(plt, "{}_1.png".format("_".join(filenames)))


if __name__ == "__main__":
    args = sys.argv[1:]
    filenames = []

    values = []

    prepare_output()

    for filename in args:
        try:
            path = filename
            data = load_csv(path)
            values.append(prepare_data1(data))
            filenames.append(filename)
        except FileExistsError:
            print("Could not find file '{}'".format(path))

    basenames = [get_basename(x) for x in filenames]

    draw_diagram1(values, basenames)
