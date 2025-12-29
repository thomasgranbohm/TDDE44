import random


def sum_divisible(values, divisor):
    s = 0
    for v in values:
        if v % divisor == 0:
            s += v
    return s


def deal_twentyone():
    s = 0
    v = []
    while s != 21:
        a = random.randint(1, 11)

        if s + a <= 21:
            s += a
            v.append(a)
    return v


if __name__ == "__main__":
    assert sum_divisible([2, 3, 4, 5, 6, 7, 8], 3) == 9
    assert sum_divisible([5, -7, 2, -5, -6], 4) == 0
    assert sum_divisible([-2, -9, 5, 5, 4, 5, -8, -1, 10, 2], 2) == 6
    assert sum_divisible([4, -7, 2, -5, -8, -3, 2], 2) == 0

    assert sum(deal_twentyone()) == 21
    assert sum(deal_twentyone()) == 21
