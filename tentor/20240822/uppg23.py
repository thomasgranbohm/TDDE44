def parse_wallet(wallet):
    values = {100: 0, 20: 0, 10: 0, 5: 0, 1: 0}
    for coin in wallet:
        values[coin] += 1

    return values


def pay_even(_wallet, owed):
    wallet = parse_wallet(_wallet)
    total = sum(_wallet)

    if total < owed:
        print("kan inte")
        return

    used = []

    for coin in wallet:
        while wallet[coin] > 0:
            if owed >= coin:
                wallet[coin] -= 1
                used.append(coin)
                owed -= coin
            else:
                break

    if owed != 0:
        print("vill inte")
    else:
        print(used)


if __name__ == "__main__":
    wallet = [100, 10, 1, 5, 1, 10, 20, 1]
    pay_even(wallet, 132)
    pay_even(wallet, 500)
    pay_even(wallet, 4)
