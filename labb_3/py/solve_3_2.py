# 3.2.1
def sum_of_ints2(value_list):
    s = 0

    for x in value_list:
        if type(x) is list:
            s += sum_of_ints2(x)
        elif type(x) is int:
            s += x

    return s
assert sum_of_ints2([["a", 1], [2, 3.0, "hej"]]) == 3

# 3.2.2
def flatten_list1(list_of_lists: list):
    flat = []

    for x in list_of_lists:
        if type(x) is list:
            flat.extend(flatten_list1(x))
        else:
            flat.append(x)
    
    return flat
assert flatten_list1([[1, 2], [3], [1, 2, 3]]) == [1, 2, 3, 1, 2, 3]

# 3.2.3
def flatten_list2(list_of_lists: list):
    return flatten_list1(list_of_lists)
assert flatten_list2([[1, 2], [3], 4, [1, 2, 3], 4, 5]) == [1, 2, 3, 4, 1, 2, 3, 4, 5]

# 3.2.4
def get_first_column(matrix: list):
    return flatten_list1(matrix)[::len(matrix[0])]
m1 = [[1, 2, 4],
      [3, 0, 6],
      [0, 5, 1]]
assert get_first_column(m1) == [1, 3, 0]

# 3.2.5
def get_nth_column(n: int, matrix: list):
    return [matrix[i][n] for i in range(len(matrix))]
assert get_nth_column(1, m1) == [2, 0, 5]

# 3.2.6
def get_all_columns(matrix):
    cols = []

    for i in range(len(matrix[0])):
        cols.append(get_nth_column(i, matrix))

    return cols
assert get_all_columns(m1) == [[1, 3, 0], [2, 0, 5], [4, 6, 1]]

# 3.2.7
def scalar_product(vec1, vec2):
    s = 0

    for i in range(len(vec1)):
        s += vec1[i] * vec2[i]

    return s

# 3.2.8
def matrix_square(matrix):
    new_matrix = [[[] for i in range(len(matrix))] for i in range(len(matrix))]

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            col = get_nth_column(x, matrix)
            new_matrix[y][x] = scalar_product(col, matrix[y])
            
    return new_matrix
m = [[1, 2, 4],
     [3, 0, 6],
     [0, 5, 1]]
assert matrix_square(m) == [[7, 22, 20],[3, 36, 18],[15, 5, 31]]