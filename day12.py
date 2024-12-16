filepath = "inputs/12a.txt"
with open(filepath, "r") as f:
    plants = [[x for x in l.strip()] for l in f.readlines()]


def flood_fill(y, x):
    front = set()
    visited = set()
    front.add((y, x))
    while len(front) > 0:
        py, px = front.pop()
        visited.add((py, px))
        for ny, nx in neighbors(py, px):
            if ny < 0 or ny >= len(plants) or nx < 0 or nx >= len(plants[y]):
                continue
            elif plants[ny][nx] != plants[py][px]:
                continue
            else:
                if (ny, nx) not in visited:
                    front.add((ny, nx))
    return visited  # visited


def perimeter(area):
    perim = 0
    for y, x in area:
        for ny, nx in neighbors(y, x):
            if ny < 0 or ny >= len(plants) or nx < 0 or nx >= len(plants[y]):
                perim += 1
            elif plants[ny][nx] != plants[y][x]:
                perim += 1
    return perim


def neighbors(y, x):
    for dify, difx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        yield y + dify, x + difx


def outside(y, x):
    return y < 0 or y >= len(plants) or x < 0 or x >= len(plants[y])


def same(y, x, ny, nx):
    if outside(ny, nx):
        return False
    return plants[y][x] == plants[ny][nx]


def angles270(y, x):
    corners = 0
    if same(y, x, y - 1, x) and same(y, x, y, x + 1) and not same(y, x, y - 1, x + 1):
        corners += 1
    if same(y, x, y - 1, x) and same(y, x, y, x - 1) and not same(y, x, y - 1, x - 1):
        corners += 1
    if same(y, x, y + 1, x) and same(y, x, y, x + 1) and not same(y, x, y + 1, x + 1):
        corners += 1
    if same(y, x, y + 1, x) and same(y, x, y, x - 1) and not same(y, x, y + 1, x - 1):
        corners += 1
    return corners


def angles90(y, x):
    corners = 0
    if not same(y, x, y - 1, x) and not same(y, x, y, x + 1):
        corners += 1
    if not same(y, x, y - 1, x) and not same(y, x, y, x - 1):
        corners += 1
    if not same(y, x, y + 1, x) and not same(y, x, y, x + 1):
        corners += 1
    if not same(y, x, y + 1, x) and not same(y, x, y, x - 1):
        corners += 1
    return corners

areas = []

total_visited = set()
for y in range(len(plants)):
    for x in range(len(plants[y])):
        if (y, x) in total_visited:
            continue
        visited = flood_fill(y, x)
        total_visited = total_visited | visited
        sides = perimeter(visited)

        # vertices = 0
        # for py, px in visited:
        #     vertices += angles90(py, px) +  angles270(py, px)
        # # F + V - E = 1
        # # E = F + V - 1
        # sides = 1 + vertices - 1

        areas.append((len(visited), sides, plants[y][x]))

print(sum(a * b for a, b, c in areas))
