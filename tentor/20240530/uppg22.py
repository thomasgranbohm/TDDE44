family = {
    "ada": ["adam", "arthur"],
    "boris": ["sven", "selina", "saga"],
    "adam": ["maria", "magnus"],
    "sven": ["nathalie", "nisse"],
    "maria": ["alva", "alfred"],
    "david": ["alva", "alfred"],
    "magnus": ["emma", "erik"],
    "nathalie": ["emma", "erik"],
    "alva": ["astrid"],
}


def is_descendant(young_person, old_person, family_tree):
    if old_person not in family_tree:
        return False

    to_check: list = family_tree[old_person]

    while len(to_check) > 0:
        a = to_check.pop()

        if young_person in a:
            return True
        elif a in family_tree:
            to_check += family_tree[a]

    return False


if __name__ == "__main__":
    assert is_descendant("ada", "arthur", family) is False
    assert is_descendant("arthur", "ada", family) is True
    assert is_descendant("maria", "ada", family) is True
    assert is_descendant("maria", "arthur", family) is False
    assert is_descendant("astrid", "maria", family) is True
    assert is_descendant("astrid", "david", family) is True
