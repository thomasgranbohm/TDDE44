import csv
import math


def csv_to_barchart(filename):
    a = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for x, y in reader:
            a.append("%s: %s (%d st)" % (x, "#" * math.floor(int(y) / 2), int(y)))

    return "\n\n".join(a)


if __name__ == "__main__":
    chart = csv_to_barchart("partimandat2022.csv")
    assert (
        chart
        == """ S: ##################################################### (107 st)\nSD: #################################### (73 st)\n M: ################################## (68 st)\n V: ############ (24 st)\n C: ############ (24 st)\nKD: ######### (19 st)\nMP: ######### (18 st)\n L: ######## (16 st)"""
    )
    print(chart)
