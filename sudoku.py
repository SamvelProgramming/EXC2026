def sudoku(matrix):
    for row in matrix:
        for ch in row:
            if ch != '.' and row.count(ch) > 1:
                return False
            
    for c in range(9):
        column = [matrix[r][c] for r in range(9)]
        for ch in column:
            if ch != '.' and column.count(ch) > 1:
                return False


    for row in range(0, 9, 3):
        for ch in range(0, 9, 3):
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(matrix[row + i][ch + j])
            for ch in box:
                if ch != '.' and box.count(ch) > 1:
                    return False

    return True

matrix = [['5','3','.','.','4','.','.','.','.'],
          ['6','.','.','1','9','5','.','.','.'],
          ['.','9','8','.','.','.','.','6','.'],
          ['8','.','.','.','6','.','.','.','3'],
          ['4','.','.','8','.','3','.','.','1'],
          ['7','.','.','.','2','.','.','.','6'],
          ['.','6','.','.','.','.','2','8','.'],
          ['.','.','.','4','1','9','.','.','5'],
          ['.','.','.','.','8','.','.','7','9']]

print(sudoku(matrix))