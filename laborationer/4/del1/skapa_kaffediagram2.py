#!/usr/bin/python

"""Labb 4, del 2.

Tar in en eller flera filnamn som argument och genererar en graf
som visar antal koppar kaffe per dag under en vecka
"""

import sys
from common import draw_diagram, get_basename, load_csv, prepare_output, save_diagram


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


def draw_diagram2(values, filenames):
    """Skapar diagramet för del 2."""
    plt = draw_diagram(values, filenames)

    plt.title("Koppar kaffe per dag")
    plt.ylabel("antal koppar")
    save_diagram(plt, "{}_2.png".format("_".join(filenames)))


if __name__ == "__main__":
    args = sys.argv[1:]
    filenames = []

    values = []

    prepare_output()

    for filename in args:
        try:
            path = filename
            data = load_csv(path)
            values.append(prepare_data2(data))
            filenames.append(filename)
        except FileExistsError:
            print("Could not find file '{}'".format(path))

    basenames = [get_basename(x) for x in filenames]

    draw_diagram2(values, basenames)
