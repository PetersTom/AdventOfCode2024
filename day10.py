filepath = "inputs/10a.txt"
with open(filepath, "r") as f:
    matrix = [[int(x) for x in l.strip()] for l in f.readlines()]

zeroes = []
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] == 0:
            zeroes.append((y, x))


def neighbors(y, x, matrix):
    for difx, dify in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newy = y + dify
        newx = x + difx
        if 0 <= newy < len(matrix) and 0 <= newx < len(matrix[newy]):
            if matrix[newy][newx] == matrix[y][x] + 1:
                yield newy, newx


def calculate_score(y, x, matrix):
    nines_reached = 0
    visited = set()
    front = set()
    front.add((y, x))
    while len(front) > 0:
        py, px = front.pop()
        visited.add((py, px))
        if matrix[py][px] == 9:
            nines_reached += 1
            continue
        N = neighbors(py, px, matrix)
        for ny, nx in N:
            if (ny, nx) not in visited:
                front.add((ny, nx))
    return nines_reached


def dfs(y, x, visited, path):
    if matrix[y][x] == 9:
        print(path)
        return 1
    visited.add((y, x))
    paths_from_here = 0
    for ny, nx in neighbors(y, x, matrix):
        paths_from_here += dfs(ny, nx, visited, path + [(ny, nx)])
    return paths_from_here


total = 0
for y, x in zeroes:
    s = dfs(y, x, set(), [])
    print(s)
    total += s
print("total: " + str(total))
