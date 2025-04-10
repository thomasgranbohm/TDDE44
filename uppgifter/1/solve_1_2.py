import random

# 1.2.1
def second_in_list(values):
    return values[1]

def last_in_list(values):
    return values[-1]

def second_last_in_list(values):
    return values[-2]

def n_in_list(values, n):
    return values[n]

# 1.2.2
def three_first_in_list(values):
    return values[:3]

def three_last_in_list(values):
    return values[-3:]

def but_five_last_in_list(values):
    return values[:-5]

def every_other_in_list(values):
    return values[::2]

def two_around_n_in_list(values, n):
    return values[n-2:n+3]

# 1.2.3
def new_list_with_n(values, n):
    return values + [n]

# 1.2.4
def append_n_to_list(values, a_value):
    values.append(a_value)
    return values
v = [1, 2, 3,4, 5, 6]
assert append_n_to_list(v, 7) == [1, 2, 3, 4, 5, 6, 7]
assert v == [1, 2, 3, 4, 5, 6, 7]

# 1.2.5
def insert_4_on_pos_3(values):
    values.insert(3, 4)
    return values

# 1.2.6
def extend_vals_to_list(values1, values2):
    values1.extend(values2)
    return values1

# 1.2.7
def remove_from_third_in_list(values):
    del values[2:]
    return values

# 1.2.8
def concatenate_lists(values1, values2):
    return values1 + values2

# 1.2.9
def select_random(values):
    return random.choice(values)