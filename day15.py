filepath = "inputs/15a.txt"
with open(filepath, "r") as f:
    inp = ''.join(f.readlines())
    grid = inp.split('\n\n')[0]
    moves = inp.split('\n\n')[1]

moves = ''.join(moves.split('\n'))  # remove enters

grid = [list(x) for x in grid.split('\n')]


def print_grid(grid, robot):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (y, x) == robot:
                print("@", end="")
            else:
                print(grid[y][x], end="")
        print()
    print("-------------------------------")

new_width = len(grid[0]) * 2
for y in range(len(grid)):
    x = 0
    while x < new_width:
        if grid[y][x] == ".":
            grid[y].insert(x, ".")
        elif grid[y][x] == "#":
            grid[y].insert(x, "#")
        elif grid[y][x] == "@":
            grid[y].insert(x + 1, ".")
        elif grid[y][x] == "O":
            grid[y][x] = "]"
            grid[y].insert(x, "[")
        x += 2

robot = (-1,-1)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "@":
            robot = (y, x)
            break
    if robot != (-1, -1):
        break

grid[robot[0]][robot[1]] = "."


def move(robot, move):
    global grid
    difx, dify = [(0, -1), (1, 0), (0, 1), (-1, 0)][move]
    y, x = robot
    if grid[y + dify][x + difx] == ".":
        return y + dify, x + difx
    elif grid[y + dify][x + difx] == "#":
        return robot
    else:
        # check if we can move boxes
        p = robot

        if dir == 1 or dir == 3:
            while True:
                p = (p[0] + dify, p[1] + difx)
                if grid[p[0]][p[1]] == "[" or grid[p[0]][p[1]] == "]":
                    continue
                elif grid[p[0]][p[1]] == "#":
                    # we can not move
                    return robot
                else:
                    # we can move
                    assert grid[p[0]][p[1]] == "."
                    # move all boxes over

                    for X in range(p[1], robot[1], -1 if dir == 1 else 1):
                        if dir == 3:
                            grid[p[0]][X] = grid[p[0]][X + 1]
                        else:
                            grid[p[0]][X] = grid[p[0]][X - 1]
                    return y + dify, x + difx
        else:
            boxes_to_move = set()
            to_check = {robot}
            grid[robot[0]][robot[1]] = "@" # temporary add the robot to make the while loop not go out on the first iteration
            while True:
                if all(grid[p[0]][p[1]] == "." for p in to_check):
                    # we can move, so do the move
                    new_grid = [[x for x in row] for row in grid]
                    # remove old boxes
                    for b in boxes_to_move:
                        new_grid[b[0]][b[1]] = "."
                        new_grid[b[0]][b[1] + 1] = "."
                    # add new boxes
                    for b in boxes_to_move:
                        new_grid[b[0] + dify][b[1]] = "["
                        new_grid[b[0] + dify][b[1] + 1] = "]"
                    new_grid[robot[0]][robot[1]] = "."
                    if new_grid[robot[0] + dify][robot[1]] == "[":
                        new_grid[robot[0] + dify][robot[1]] = "."
                        new_grid[robot[0] + dify][robot[1] + 1] = "."
                    elif new_grid[robot[0] + dify][robot[1]] == "]":
                        new_grid[robot[0] + dify][robot[1]] = "."
                        new_grid[robot[0] + dify][robot[1] - 1] = "."
                    grid = new_grid
                    return robot[0] + dify, robot[1]
                elif any(grid[p[0]][p[1]] == "#" for p in to_check):
                    # we cannot do a move
                    grid[robot[0]][robot[1]] = "."
                    return robot
                else:
                    # combination of boxes and empty
                    new_to_check = set()
                    for p in to_check:
                        # if it is a box, add the new locations we need to check
                        if grid[p[0]][p[1]] == "]":
                            new_to_check.add((p[0] + dify, p[1] + difx))
                            new_to_check.add((p[0] + dify, p[1] + difx - 1))
                            boxes_to_move.add((p[0], p[1] - 1))
                        elif grid[p[0]][p[1]] == "[":
                            new_to_check.add((p[0] + dify, p[1] + difx))
                            new_to_check.add((p[0] + dify, p[1] + difx + 1))
                            boxes_to_move.add((p[0], p[1]))
                        elif grid[p[0]][p[1]] == "@":
                            new_to_check.add((p[0] + dify, p[1] + difx))
                    to_check = new_to_check


def sum_gps(grid):
    total_gps = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "[":
                total_gps += x + y * 100
    return total_gps


print_grid(grid, robot)


for i, m in enumerate(moves):
    dir = -1
    if m == "^":
        dir = 0
    elif m == ">":
        dir = 1
    elif m == "v":
        dir = 2
    elif m == "<":
        dir = 3

    robot = move(robot, dir)
    print(i)
    # print_grid(grid, robot)

print_grid(grid, robot)

print(sum_gps(grid))



