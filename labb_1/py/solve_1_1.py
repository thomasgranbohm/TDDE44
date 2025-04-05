import math

# 1.1.1
def return_five():
    return "five"

# 1.1.2
def print_five():
    print("five")

# 1.1.3
def add_strings():
    return "hej" + "san"

# 1.1.4
def use_the_var():
    value = 5
    return value * 5

# 1.1.5
def use_the_arg(a_string):
    print(a_string)
    return a_string

# 1.1.6
def to_string(a_value):
    return str(a_value)

# 1.1.7
def to_integer(a_value):
    return int(a_value)

# 1.1.8
def to_float(a_value):
    return float(a_value)

# 1.1.9
def to_any_type(a_value, a_type):
    return a_type(a_value)
assert to_any_type("123", int)

# 1.1.10
def print_type(a_value):
    print(type(a_value))

# 1.1.11
def subtract(value1, value2):
    return value1 - value2

# 1.1.12
def split_bill(amount, number_of_people):
    return amount / number_of_people # Typ floats eller?

# 1.1.13
def round_up(value):
    return math.ceil(value)

# 1.1.14
def round_down(value):
    return math.floor(value)

# 1.1.15
def fahrenheit_to_celsius(temperature):
    return float(temperature - 32) * 5 / 9
assert fahrenheit_to_celsius(68) == 20.0

# 1.1.16
def celsius_to_fahrenheit(temperature):
    return (temperature * 9 / 5) + 32
assert celsius_to_fahrenheit(20) == 68.0

# extra test
assert fahrenheit_to_celsius(celsius_to_fahrenheit(100)) == 100.0

def pythagoras(x, y):
    return math.sqrt(x**2 + y**2)
assert pythagoras(3, 4) == 5