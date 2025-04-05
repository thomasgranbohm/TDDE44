# 2.1.1
def greeting(name):
    if name[0] != "M":
        return "Hej %s!" % (name)
    
    return "Hej %s, visste du att M är min favoritbokstav!" % (name)
assert greeting("Pontus") == "Hej Pontus!"
assert greeting("Morgan") == "Hej Morgan, visste du att M är min favoritbokstav!"

# 2.1.2
def is_this_a_long_list(values):
    return len(values) > 5

# 2.1.3
def get_grade(score):
    if score > 80:
        return "VG"
    elif score >= 50:
        return "G"
    
    return "U"
    
assert get_grade(80) == "G"
assert get_grade(81) == "VG"
assert get_grade(12) == "U"

# 2.1.4
def days_in_month(name_of_month):
    months = {
        "januari": 31,
        "februari": 28,
        "mars": 31,
        "april": 30,
        "maj": 31,
        "juni": 30,
        "juli": 31,
        "augusti": 31,
        "september": 30,
        "oktober": 31,
        "november": 30,
        "december": 31,
    }

    return months[name_of_month]

# 2.1.5
def odd(value):
    return value % 2 == 1

# 2.1.6
def get_integer_description(value):
    if value == 0:
        return 0

    is_odd = odd(value)

    return (1 if is_odd else 2) * (1 if value > 0 else -1)

# 2.1.7
def appraisal_factor(rare, good_condition):
    return 1 + \
        (.25 if rare else -.25) + \
        (.5 if good_condition else -0.5)
