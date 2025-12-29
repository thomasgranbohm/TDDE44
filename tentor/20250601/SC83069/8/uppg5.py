import csv
import math

def least_common_popular_name(year, filepath):
    with open(filepath, "r") as f:
        reader = csv.reader(f, delimiter=";")
        lines = list(reader)

        col_index = None

        for i, y in enumerate(lines[0]):
            if not y.isdigit():
                continue
            if int(y) == year:
                col_index = i
                break

        name = None
        least = math.inf
        for y in lines[1:]:
            if not y[col_index].isdigit():
                continue
            
            a = int(y[col_index])
            if a < least:
                least = a

                name = y[0]
        
        return name