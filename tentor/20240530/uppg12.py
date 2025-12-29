def tree_depth_rec(tree):
    depth = 0

    for v in tree:
        if isinstance(v, list):
            a = 1 + tree_depth_rec(v)

            if a > depth:
                depth = a

    return depth


if __name__ == "__main__":
    assert tree_depth_rec([1]) == 0
    assert tree_depth_rec([[2], 3]) == 1
    assert tree_depth_rec([["a"], 5, [["b"], [7.0]], 8]) == 2
    assert tree_depth_rec([[], [[]], [[[]]]]) == 3
