def load_csv(filename):
    # Error handling mabby?
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
     
if __name__ == "__main__":
    lines = load_csv("csv/AdaLovelace.csv")
    print(lines)
