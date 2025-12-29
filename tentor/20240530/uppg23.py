operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def eval_prefix(expression):
    o, f, s = expression

    def parse(a):
        if isinstance(a, tuple):
            return eval_prefix(a)
        return a

    f = parse(f)
    s = parse(s)

    return operations[o](f, s)


if __name__ == "__main__":
    assert eval_prefix(("+", 1, 2)) == 3
    assert eval_prefix(("+", ("*", 3, 4), ("*", 5, 6))) == 42
    assert eval_prefix(("+", ("/", ("+", 1, 2), 3), ("*", 4, ("-", 5, 6)))) == -3.0
