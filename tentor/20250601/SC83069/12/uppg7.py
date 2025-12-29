def print_calendar(days, first_day):
    for x in range(-first_day, days):
        c = None

        if x < 0:
            c = ""
        else: 
            c = str(x + 1)

        end_char = None

        if (x + 1 + first_day) % 7 == 0:
            end_char = "\n"
        else: 
            end_char = ""
        
        print(c.rjust(3, " "), end=end_char)

    print()
