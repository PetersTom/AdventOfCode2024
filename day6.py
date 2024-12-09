filepath = "inputs/6a.txt"
with open(filepath, "r") as f:
    matrix = [[x for x in l.strip()] for l in f.readlines()]

guard = (0, 0)

for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == "^":
            guard = (y, x)


def is_loop(start, matrix):
    guard = start
    dir = 0  # directions are up, right, down, left 0, 1, 2, 3
    visited = set()
    visited.add((guard, dir))
    while True:
        if dir == 0:
            new_pos = (guard[0] - 1, guard[1])
        elif dir == 1:
            new_pos = (guard[0], guard[1] + 1)
        elif dir == 2:
            new_pos = (guard[0] + 1, guard[1] )
        elif dir == 3:
            new_pos = (guard[0], guard[1] - 1)

        # we have found the edge and will walk off it this round
        if new_pos[0] < 0 or new_pos[0] >= len(matrix[0]) or new_pos[1] < 0 or new_pos[1] >= len(matrix):
            return False

        if matrix[new_pos[0]][new_pos[1]] == "#":
            dir = (dir + 1) % 4
        else:
            guard = new_pos
            if len(visited) > 1 and (guard, dir) in visited:
                # we have found a position we found before
                return True
            visited.add((guard, dir))


loop_positions = []
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == ".":
            # check if an obstacle here would create a loop
            matrix[y][x] = "#"
            if is_loop(guard, matrix):
                loop_positions.append((y, x))
            matrix[y][x] = "."
print(len(loop_positions))