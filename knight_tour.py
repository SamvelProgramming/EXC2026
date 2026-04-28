n = int(input("Enter a length of chess board: "))

board = [[-1 for _ in range(n)] for _ in range(n)]
board[0][0] = 0


def print_board():
    for i in range(n):
        for j in range(n):
            val = str(board[i][j])
            print(val + " " * (4 - len(val)), end="")
        print("\n")


def get_moves(i, j):
    move_i = (2, 1, 2, 1, -2, -1, -2, -1)
    move_j = (1, 2, -1, -2, 1, 2, -1, -2)
    moves = []
    for k in range(8):
        di = i + move_i[k]
        dj = j + move_j[k]
        if 0 <= di < n and 0 <= dj < n and board[di][dj] == -1:
            moves.append([di, dj])
    return moves


def solve(i, j, count):
    if count == n * n:
        return True

    pos = get_moves(i, j)
    if not pos:
        return False

    while len(pos) > 0:
        idx_of_min = 0
        min_degree = len(get_moves(pos[0][0], pos[0][1]))

        for k in range(1, len(pos)):
            current_degree = len(get_moves(pos[k][0], pos[k][1]))
            if current_degree < min_degree:
                min_degree = current_degree
                idx_of_min = k

        next_move = pos.pop(idx_of_min)
        ni, nj = next_move[0], next_move[1]

        board[ni][nj] = count
        if solve(ni, nj, count + 1):
            return True

        board[ni][nj] = -1

    return False


if solve(0, 0, 1):
    print_board()
else:
    print("No solution")
