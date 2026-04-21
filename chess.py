def is_safe(matrix, r, c, n):
    for i in range(r):
        if matrix[i][c] == 'Q': return False
        if c - (r - i) >= 0 and matrix[i][c - (r - i)] == 'Q': return False
        if c + (r - i) < n and matrix[i][c + (r - i)] == 'Q': return False
    return True

def solve(matrix, r, n):
    if r == n:
        for row in matrix:
            print(" ".join(row))
        return True

    for c in range(n):
        if is_safe(matrix, r, c, n):
            matrix[r][c] = 'Q'
            if solve(matrix, r + 1, n):
                return True
            matrix[r][c] = '*'
    return False

user_input = input("Enter N: ")
if not user_input.strip().isdigit():
    print("Wrong input: please enter a valid integer")
else:
    n = int(user_input)
    if n == 1:
        print("Q")
    elif n < 4:
        print("Wrong input: N must be 4 or greater for a solution")
    elif n > 8:
        print("Wrong input: Number too large")
    else:
        lst = [['*' for i in range(n)] for j in range(n)]
        solve(lst, 0, n)