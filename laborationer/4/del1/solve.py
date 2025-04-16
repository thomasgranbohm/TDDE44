from common import load_csv
import matplotlib
import matplotlib.pyplot as plt
import sys

matplotlib.use("AGG")

def prepare_data1(data):
    x_values, y_values = [], []

    for line in data[1:]:
        x_values.append(line[0])
        y_values.append(sum(line[1:]) / len(line[1:]))

    return x_values, y_values

def prepare_data2(data):
    x_values, y_values = [], []

    for x in range(1, 1 + len(data[0][1:])):
        x_values.append(data[0][x])
        y_values.append(sum([data[y][x] for y in range(1, 1 + len(data[1:]))]))
        
    return x_values, y_values

    
def draw_diagram1(values, filenames):
    plt.figure()
    plt.title("Koppar kaffe i snitt vid olika klockslag under en vecka")
    plt.ylabel("antal koppar")

    for [x_values, y_values], filename in zip(values, filenames):
        plt.plot(x_values, y_values, label=filename)

    plt.legend(loc='upper left', bbox_to_anchor=(1, 0, 1, 1))
    plt.savefig("./outputs/{}_1.png".format("_".join(filenames)), bbox_inches="tight")

def draw_diagram2(values, filenames):
    plt.figure()
    plt.title("Koppar kaffe per dag")
    plt.ylabel("antal koppar")

    for [x_values, y_values], filename in zip(values, filenames):
        plt.plot(x_values, y_values, label=filename)
    
    plt.legend(loc='upper left', bbox_to_anchor=(1, 0, 1, 1))
    plt.savefig("./outputs/{}_2.png".format("_".join(filenames)), bbox_inches="tight")


if __name__ == "__main__":
    args = sys.argv[1:];
    filenames = []

    values_1, values_2 = [], []

    for filename in args:
        try:
            path = "csv/{}.csv".format(filename)
            data = load_csv(path)
            values_1.append(prepare_data1(data))
            values_2.append(prepare_data2(data))
            filenames.append(filename)
        except FileExistsError:
            print("Could not find file '{}'".format(path))
            
        
    draw_diagram1(values_1, filenames)
    draw_diagram2(values_2, filenames)

