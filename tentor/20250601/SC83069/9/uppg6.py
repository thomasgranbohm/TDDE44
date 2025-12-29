import random


def roll(expr):
    s = 0
    dices = expr.split("+")
    for dice in dices:
        if "d" not in dice and dice.isdigit:
            s += int(dice)
        else:
            times, sides = [int(x) for x in dice.split("d")]

            for _ in range(times):
                s += random.randint(1, sides)
    return s


# def test(e, m, M):
#     a = roll(e)
#     assert m <= a and a <= M

# test('1d8+3d6+3', 1 + 3 + 3, 29)
# test('1d8+3d6+3', 1 + 3 + 3, 8 + (3 * 6) + 3)
# test('1d20+5', 1 + 5, 20 + 5)
# test('4', 4, 4)
# test('2d12+8+2d12+8+1d12+2d6', (2 * 1) + 8 + (2 * 1) + 8 + 1 + 2, (2 * 12) + 8 + (2 * 12) + 8 + 12 + (2 * 6))
