def validate_sudoku(sudoku_board):
    MAX_VALUE = 45

    for i in range(9):
        row = sudoku_board[i]
        col = [y[i] for y in sudoku_board]
        
        if sum(row) is not MAX_VALUE or sum(col) is not MAX_VALUE:
            return False


    for y in range(0, 9, 3):
        s = 0
        for x in range(0, 9, 3):
            s += sum(sudoku_board[y][x:x+3])
        
        if s is not MAX_VALUE:
            return False

    return True
