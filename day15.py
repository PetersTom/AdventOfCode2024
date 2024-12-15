filepath = "inputs/15a.txt"
with open(filepath, "r") as f:
    inp = ''.join(f.readlines())
    grid = inp.split('\n\n')[0]
    moves = inp.split('\n\n')[1]

moves = ''.join(moves.split('\n'))  # remove enters

grid = [list(x) for x in grid.split('\n')]

robot = (-1,-1)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "@":
            robot = (y, x)
            break
    if robot != (-1, -1):
        break

grid[robot[0]][robot[1]] = "."
