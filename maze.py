def print_maze(grid):
    print("\n" * 10)
    for r in range(12):
        line = ""
        for c in range(12):
            line = line + grid[r][c] + " "
        print(line)
    print("\nENTER ")


def move(grid, r, c):
    if r < 0 or r > 11 or c < 0 or c > 11:
        return False

    if grid[r][c] == ' ' and (r == 0 or r == 11 or c == 0 or c == 11):
        grid[r][c] = 'o'
        print_maze(grid)
        return True

    if grid[r][c] != ' ' and grid[r][c] != 'o':
        return False

    grid[r][c] = 'o'
    print_maze(grid)
    input()

    grid[r][c] = '.'

    if move(grid, r, c + 1):
        return True
    if move(grid, r + 1, c):
        return True
    if move(grid, r, c - 1):
        return True
    if move(grid, r - 1, c):
        return True

    grid[r][c] = ' '
    print_maze(grid)
    input()
    return False


def main():
    maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['o', 'o', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' '],
        ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

    if move(maze, 2, 0):
        print("Exit is found successfully!")
    else:
        print("Sorry there is no exit found")


main()
