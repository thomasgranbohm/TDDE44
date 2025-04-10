# 2.3.1
def replace_periods_with_newlines(string_value):
    return "\n".join(string_value.split("."))
assert replace_periods_with_newlines("hej.hur mår du.jag mår bra!") == "hej\nhur mår du\njag mår bra!"

# 2.3.2
def replace_char_in_string(original_string, search_character, replacement):
    return replacement.join(original_string.split(search_character))
assert replace_char_in_string("bob", "b", "l") == "lol"

# 2.3.3a
def reverse_string_while(string_value):
    a = ""
    i = len(string_value) - 1

    while i >= 0:
        a += string_value[i]
        i -= 1
    
    return a
assert reverse_string_while("python är kul") == "luk rä nohtyp"

# 2.3.3b
def reverse_string_for(string_value):
    a = ""
    
    for i in range(len(string_value)):
        a += string_value[len(string_value) - i - 1]

    return a
assert reverse_string_for("python är kul") == "luk rä nohtyp"

# 2.3.4
def get_five_first(value_list):
    a = []

    for i in range(5):
        a.append(value_list[i])

    return a

# 2.3.5
def get_nfirst(value_list, n):
    a = []

    for i in range(n):
        a.append(value_list[i])

    return a

# 2.3.6
def get_all_less_than(values, cutoff):
    a = []

    for x in values:
        if x < cutoff:
            a.append(x)
    
    return a

# 2.3.7
def get_all_even(values):
    a = []
    
    for x in values:
        if x % 2 == 0:
            a.append(x)

    return a

# 2.3.8
def get_all_divisible(values, divisor):
    a = []
    
    for x in values:
        if x % divisor == 0:
            a.append(x)

    return a

# 2.3.9
def multiply_for_each(values, multiplier):
    for i in range(len(values)):
        values[i] *= multiplier
    
    return values

# 2.3.10
def insert_at_asc_place(values, new_value):
    a = []
    added = False

    for x in values:
        if added is False and new_value <= x:
            a.append(new_value)
            added = True
        a.append(x)

    if added == False:
        a.append(new_value)

    return a
assert insert_at_asc_place([3, 7, 8, 11], 7.9) == [3, 7, 7.9, 8, 11]
assert insert_at_asc_place([3], 1) == [1, 3]

# 2.3.11 
def sort_asc(values):
    a = []
    for x in values:
        a = insert_at_asc_place(a, x)

    return a
assert sort_asc([3, 9, 7, 1, 11]) == [1, 3, 7, 9, 11]