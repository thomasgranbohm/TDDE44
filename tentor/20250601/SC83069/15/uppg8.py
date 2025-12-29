def validate_sudoku(sudoku_board):
    for i in range(9):
        row = sudoku_board[i]
        col = [y[i] for y in sudoku_board]

        if len(set(col)) != 9 or len(set(row)) != 9:
            return False

    for y in range(0, 9, 3):
        s = []

        for x in range(0, 9, 3):
            s += sudoku_board[y][x : x + 3]

        if len(set(s)) != 9:
            return False

    return True
