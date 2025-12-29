import math


def parse_users(filepath):
    try:
        file = open(filepath, "r")
        data = file.read().splitlines()
    except FileNotFoundError:
        print("File does not exist")
        exit(1)

    users = {}

    for i in range(int(len(data) / 2)):
        users[data[i * 2]] = [int(x) for x in data[(i * 2) + 1].strip().split(" ")]

    return users


def scalar(a, b):
    s = 0
    for x, y in zip(a, b):
        s += x * y
    return s


def length(a):
    return math.sqrt(scalar(a, a))


def cosine_similarity(a, b, c):
    users = parse_users(c)

    x = users.get(a)
    y = users.get(b)

    print(scalar(x, y) / (length(x) * length(y)))


if __name__ == "__main__":
    cosine_similarity("Tony", "Tony", "book_ratings.txt")
    cosine_similarity("Tony", "joe", "book_ratings.txt")
    cosine_similarity("NuNu", "Megan", "book_ratings.txt")
    cosine_similarity("McLovin", "Boxxy", "book_ratings.txt")
