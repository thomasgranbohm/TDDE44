def print_calendar(days, first_day):
    for x in range(-first_day, days):
        c = str(x + 1) if x >= 0 else ""
        end_char = "" if (x + 1 + first_day) % 7 != 0 else "\n"
        print(c.rjust(3, " "), end=end_char)
    print()
