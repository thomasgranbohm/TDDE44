import math

# 3.3.1
def fac_rec(n):
    if n == 1:
        return n
    else:
        return n * fac_rec(n - 1)
assert fac_rec(7) == 5040

# 3.3.2
def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
assert fib(19) == 4181

# 3.3.3
def pascal(row, col):
    if row == 0 or col == 0 or col == row:
        return 1
    else:
        return pascal(row - 1, col) + pascal(row - 1, col - 1)

# 3.3.4
def keep_if_even(lst):
    a = []
    for x in lst:
        if x % 2 == 0:
            a.append(x)
    return a
assert keep_if_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

# 3.3.5
def reverse_rec(lst):
    a = []

    for x in lst[::-1]:
        a.append(x)

    return a

assert reverse_rec([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]
assert reverse_rec([1, [2, 3], 4, [5, [6]]]) == [[5, [6]], 4, [2, 3], 1]

# 3.3.6
def keep_if_even_all(lst):
    a = []
    for x in lst:
        if type(x) is list:
            a.append(keep_if_even_all(x))
        elif x % 2 == 0:
            a.append(x)

    return a

assert keep_if_even_all([1, 2, [1, 3], [4, 7], 6]) == [2, [], [4], 6]
assert keep_if_even_all([1, 2, [3, 4], [5, [6, 7, [[8]]]]]) == [2, [4], [[6, [[8]]]]]

# 3.3.7
def reverse_rec_all(lst):
    a = []
    
    for x in lst[::-1]:
        if type(x) is list:
            a.append(reverse_rec_all(x))
        else: 
            a.append(x)

    return a

reverse_rec_all([1, [2, 3, 4], 5, 6]) == [6, 5, [4, 3, 2], 1]
reverse_rec_all([1, [2, 3], 4, [5, [6]]]) == [[[6], 5], 4, [3, 2], 1]

# 3.3.8
def is_in_list(lst, element):
    for x in lst:
        if type(x) is list:
            return is_in_list(x, element)
        elif x == element:
            return True

    return False
assert is_in_list(["a", "b", "b", "a"], "b") == True
assert is_in_list(["a", "b", "b", "a"], "c") == False

assert is_in_list([1, 2, 3, [4, 5, [6]]], 6) == True
assert is_in_list([1, 2, 3, [4, 5, [6]]], 7) == False

def count_all(lst):
    c = 0

    for x in lst:
        if type(x) is list:
            c += count_all(x)
        else: 
            c += 1

    return c

assert count_all(["a", "b", "b", "a"]) == 4
assert count_all([1, 2, 3, [4, 5, [6]]]) == 6

# 3.3.10
def subst_all(lst, element, new_value):
    for i, x in enumerate(lst[::]):
        if type(x) is list:
            lst[i] = subst_all(x, element, new_value)
        elif x == element:
            lst[i] = new_value
    return lst

assert subst_all(["a", "b", "b", "a"], "b", "l") == ['a', 'l', 'l', 'a']
assert subst_all([1, 2, 3, [4, 5, [6]]], 6, "x") == [1, 2, 3, [4, 5, ['x']]]

# 3.3.11
def multiply(factor1, factor2):
    if factor2 == 1:
        return factor1
    
    return factor1 + multiply(factor1, factor2 - 1)

assert multiply(3, 7) == 21
assert multiply(7, 3) == 21

# 3.3.E1
def linear_search(key, seq):
    for i, x in enumerate(seq):
        if x == key:
            return i
    return -1

assert linear_search(9, [1,2,3,4,5,6,7,8,9]) == 8
assert linear_search('b', "anna") == -1

# 3.3.E2
def binary_search(key, sorted_lst):
    l = 0
    h = len(sorted_lst) - 1

    while l <= h:
        m = math.floor((l + h) / 2)

        if sorted_lst[m] < key:
            l = m + 1
        elif key < sorted_lst[m]:
            h = m - 1
        else:
            return m
    
    return -1

assert binary_search(9, [1,2,3,4,5,6,7,8,9]) == 8
assert binary_search(0, [1,2,3,4,5,6,7,8,9]) == -1
assert binary_search(10, [1,2,3,4,5,6,7,8,9]) == -1
