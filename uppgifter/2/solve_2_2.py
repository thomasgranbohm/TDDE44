import math

# 2.2.1
def create_ten_list_while():
    i = 0
    a = []

    while i <= 10:
        a.append(i)
        i += 1
    
    return a
assert create_ten_list_while() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def create_ten_list_for():
    a = []

    for i in range(11):
        a.append(i)

    return a
assert create_ten_list_for() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2.2.2
def create_zero_to_number_list_while(number):
    i = 0
    a = []

    while i <= number:
        a.append(i)
        i += 1
    
    return a
assert create_zero_to_number_list_while(3) == [0, 1, 2, 3]

def create_zero_to_number_list_for(number):
    a = []

    for i in range(number + 1):
        a.append(i)

    return a
assert create_zero_to_number_list_for(3) == [0, 1, 2, 3]

# 2.2.3
def create_number_to_number_list_while(start_number, end_number):
    i = start_number
    a = []

    while i <= end_number:
        a.append(i)
        i += 1
    
    return a
assert create_number_to_number_list_while(5, 9) == [5, 6, 7, 8, 9]
    
def create_number_to_number_list_for(start_number, end_number):
    a = []

    for i in range(start_number, end_number + 1):
        a.append(i)

    return a

assert create_number_to_number_list_for(5, 9) == [5, 6, 7, 8, 9]


# 2.2.4
def get_max_while(integer_list):
    m = -math.inf
    i = 0

    while i < len(integer_list):
        if m < integer_list[i]:
            m = integer_list[i]
        
        i += 1

    return m
assert get_max_while([4, 7, 8, 1, 2, 7]) == 8

def get_max_for(integer_list):
    m = -math.inf

    for n in integer_list:
        if m < n:
            m = n

    return m
assert get_max_for([4, 7, 8, 1, 2, 7]) == 8

# 2.2.5
def get_min(integer_list):
    m = math.inf

    for n in integer_list:
        if m > n:
            m = n
    
    return m
assert get_min([9, 3, 6, 3, 100, 2, 30]) == 2

# 2.2.6
def word_in_list_while(words, word):
    i = 0

    while i < len(words):
        if words[i] == word:
            return True
        
        i += 1

    return False

def word_in_list_for(words, word):
    for s in words:
        if s == word:
            return True
    
    return False


# 2.2.7
def count_integers_while(value_list):
    n = 0
    i = 0

    while i < len(value_list):
        if type(value_list[i]) == int:
            n += 1

        i += 1

    return n

def count_integers_for(value_list):
    n = 0

    for x in value_list:
        if type(x) == int:
            n += 1

    return n

# 2.2.8
def average_while(values):
    s = 0.0

    i = 0
    while i < len(values):
        s += values[i]
        i += 1

    return s / len(values)

def average_for(values):
    s = 0.0

    for x in values:
        s += x

    return s / len(values)

# 2.2.9
def population(pop_a, rate_a, pop_b, rate_b):
    if rate_a <= rate_b:
        return -1

    i = 0

    while True:
        if pop_a >= pop_b:
            return i

        pop_a *= 1 + (rate_a / 100)
        pop_b *= 1 + (rate_b / 100)

        i += 1
    

# 2.2.10
def birthday(n):
    a = 1

    for x in range(1, n + 1):
        a *= (366 - x) / 365
    
    return 1 - a


# 2.2.11
def sum_of_ints(value_list):
    s = 0
    
    for x in value_list:
        if type(x) is int:
            s += x
    
    return s
assert sum_of_ints(['a', 1, 2, 3, 4.0]) == 6