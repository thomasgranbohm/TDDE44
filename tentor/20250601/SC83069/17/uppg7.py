def print_calendar(days, first_day):
    for x in range(-first_day, days):
        c = str(x + 1)

        if x < 0:
            c = ""

        end_char = ""

        if (x + 1 + first_day) % 7 == 0:
            end_char = "\n"

        print(c.rjust(3, " "), end=end_char)

    print()


if __name__ == "__main__":
    for days in [30, 31]:
        for first_day in range(0, 7):
            print(f"print_calendar({days}, {first_day})")
            print_calendar(days, first_day)
            print()
