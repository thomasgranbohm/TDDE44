import sudoku_examples


names = [
    "valid1",
    "valid2",
    "valid3",
    "invalid1",
    "invalid2",
    "invalid3",
]


def validate_sudoku(sudoku_board):
    for i in range(9):
        row = sudoku_board[i]
        col = [y[i] for y in sudoku_board]

        if len(set(col)) != 9 or len(set(row)) != 9:
            return False

    for b_i in range(0, 9):
        s = []

        for s_i in range(0, 9):
            s.append(
                sudoku_board[(b_i // 3) * 3 + (s_i // 3)][(b_i % 3) * 3 + (s_i % 3)]
            )

        if len(set(s)) != 9:
            return False

    return True


def swap_in_row(board):
    board[0][5] = board[0][6]
    return board


def swap_in_column(board):
    board[5][0] = board[6][0]
    return board


def swap_in_diagnal(board):
    board[2][2] = board[1][1]
    return board


def parse_sudoku_string(s):
    board = []
    for i, c in enumerate(s):
        if i % 9 == 0:
            board.append([])
        board[-1].append(int(c))
    return board


def other_validate_sudoku(sudoku_board):
    return (
        check_rows(sudoku_board)
        and check_columns(sudoku_board)
        and check_zones(sudoku_board)
    )


def list_ok(candidate, reference=range(1, 10)):
    for val in reference:
        if val not in candidate:
            return False
    return True


def check_rows(matrix):
    for row in matrix:
        if not list_ok(row):
            return False
    return True


def check_columns(matrix):
    # Since matrix is square, we could use height as width but here we choose
    # to be explicit and base board width on the length of the first element.
    board_width = len(matrix[0])
    tmp_column = [None] * board_width
    for col in range(board_width):
        for row in range(len(matrix)):
            tmp_column[row] = matrix[row][col]
        if not list_ok(tmp_column):
            return False
    return True


def check_zones(matrix, zone_width=3, zone_height=3):
    board_width = len(matrix[0])
    n_zones = int(board_width / zone_width)
    for zone_col in range(n_zones):
        for zone_row in range(int(len(matrix) / zone_height)):
            if not check_zone(matrix, zone_col * zone_width, zone_row * zone_height):
                return False
    return True


def check_zone(matrix, start_col, start_row, zone_width=3, zone_height=3):
    tmp_zone = []
    for row in range(zone_height):
        tmp_zone.extend(matrix[start_row + row][start_col : start_col + zone_width])
    return list_ok(tmp_zone)


if __name__ == "__main__":
    assert validate_sudoku(sudoku_examples.valid1)
    assert validate_sudoku(sudoku_examples.valid2)
    assert validate_sudoku(sudoku_examples.valid3)
    assert not validate_sudoku(sudoku_examples.invalid1)
    assert not validate_sudoku(sudoku_examples.invalid2)
    assert not validate_sudoku(sudoku_examples.invalid3)
    assert not validate_sudoku(sudoku_examples.invalid_box1)
    assert not validate_sudoku(sudoku_examples.invalid_box2)
    assert not validate_sudoku(sudoku_examples.invalid_box3)

    # with open("sudoku.csv", "r") as f:
    #     lines = f.read().splitlines()
    #     # for i, line in enumerate(lines):
    #     #     bs = line.split(",")[1]
    #     #     assert validate_sudoku(parse_sudoku_string(bs))
    #     #     print(f"Test case #{str(i).rjust(6, '0')}: {bs} [PASSES]")
    #     for i, line in enumerate(lines):
    #         bs = line.split(",")[1]
    #         print(f"Test case #{str(i).rjust(6, '0')}: {bs}")
    #         s = parse_sudoku_string(bs)

    #         assert validate_sudoku(parse_sudoku_string(bs))
    #         print("[PASSES]", end=" ")
    #         assert not validate_sudoku(swap_in_row(parse_sudoku_string(bs)))
    #         print("[PASSES]", end=" ")
    #         assert not validate_sudoku(swap_in_column(parse_sudoku_string(bs)))
    #         print("[PASSES]", end=" ")
    #         assert not validate_sudoku(swap_in_diagnal(parse_sudoku_string(bs)))
    #         print("[PASSES]")
    #         print("Their solution:")
    #         assert other_validate_sudoku(parse_sudoku_string(bs))
    #         print("[PASSES]", end=" ")
    #         assert not other_validate_sudoku(swap_in_row(parse_sudoku_string(bs)))
    #         print("[PASSES]", end=" ")
    #         assert not other_validate_sudoku(swap_in_column(parse_sudoku_string(bs)))
    #         print("[PASSES]", end=" ")
    #         assert not other_validate_sudoku(swap_in_diagnal(parse_sudoku_string(bs)))
    #         print("[PASSES]")
