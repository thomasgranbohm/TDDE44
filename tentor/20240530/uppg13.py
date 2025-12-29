recept_db = {
    "kladdkaka": ["smör", "socker", "kakao", "mjöl"],
    "typ bröd": ["mjöl", "vatten"],
    "typ kaka": ["mjöl", "socker", "mjölk"],
    "sockerkaka": ["ägg", "socker", "smör", "mjöl"],
    "pannkaka": ["ägg", "socker", "mjöl", "mjölk"],
    "mördegskakaor": ["smör", "socker", "mjöl"],
}


def check_ingredients(database, ingredients):
    recepts = []

    for k, v in database.items():
        if len(set(v) - set(ingredients)) == 0:
            recepts.append(k)

    return recepts


if __name__ == "__main__":
    print(
        check_ingredients(recept_db, ["smör", "socker", "kakao", "mjöl", "vatten"]),
        ["kladdkaka", "typ bröd", "mördegskakaor"],
    )
    print(
        check_ingredients(recept_db, ["smör", "socker", "mjöl", "vatten"]),
        ["typ bröd", "mördegskakaor"],
    )
    print(check_ingredients(recept_db, ["öl", "ost", "kalles kaviar", "nudlar"]), [])
    print(
        check_ingredients(recept_db, ["vatten", "ost", "kalles kaviar", "mjöl"]),
        ["typ bröd"],
    )
