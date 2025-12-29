from math import pow


def print_mat(mat):
    for y in mat:
        print(y)


def make_circle_segment(r):
    a = []

    for y in range(r):
        b = []
        for x in range(r):
            if pow(x + 1 / 2, 2) + pow(y + 1 / 2, 2) < pow(r, 2):
                b.append(1)
            else:
                b.append(0)

        a.append(b)

    return a


if __name__ == "__main__":
    print_mat(make_circle_segment(5))
    assert make_circle_segment(5) == [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0],
    ]
    assert make_circle_segment(8) == [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
    ]
