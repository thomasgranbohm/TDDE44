#!/usr/bin/python

"""Labb 4, del 3.

Tar in en eller flera filnamn som argument och genererar två grafer,
de två som är definerade i uppgift 1 och uppgift 2.
"""

import sys
from common import prepare_output, load_csv, get_basename
from skapa_kaffediagram1 import draw_diagram1, prepare_data1
from skapa_kaffediagram2 import draw_diagram2, prepare_data2

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
