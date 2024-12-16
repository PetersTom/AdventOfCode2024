import heapq

filepath = "inputs/16.txt"
with open(filepath, "r") as f:
    grid = [[x for x in line.strip()] for line in f.readlines()]

start = (-1, -1)
end = (-1, -1)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "E":
            end = (y, x)
            grid[y][x] = "."
        elif grid[y][x] == "S":
            start = (y, x, 1)
            grid[y][x] = "."


class PrioNode:
    def __init__(self, score, item, dir):
        self.score = score
        self.dist = dist(item, end)
        self.item = item
        self.dir = dir

    def __lt__(self, other):
        return self.score + self.dist < other.score + other.dist

    def __eq__(self, other):
        return self.item == other.item and self.dir == other.dir

    def __hash__(self):
        return self.item.__hash__() + self.dir.__hash__()

    def __str__(self):
        return str(self.item) + "-" + str(self.dir) + "-" + str(self.score + self.dist)

def neighbors(p: PrioNode):
    neighs = []
    neighs.append(PrioNode(p.score + 1000, (p.item[0], p.item[1]), ((p.dir + 1) % 4)))
    neighs.append(PrioNode(p.score + 1000, (p.item[0], p.item[1]), ((p.dir - 1) % 4)))
    if p.dir not in [0, 1, 2, 3]:
        print("hello")
        pass
    dify, difx = [(-1, 0), (0, 1), (1, 0), (0, -1)][p.dir]
    newy, newx = p.item[0] + dify, p.item[1] + difx
    if 0 <= newy < len(grid) and 0 <= newx < len(grid[y]):
        if grid[newy][newx] == ".":
            neighs.append(PrioNode(p.score + 1, (newy, newx), p.dir))
    return neighs


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def find_path(parents, start, end):
    path = []
    for dir in [0, 1, 2, 3]:
        if (end, dir) in parents:
            break
    p = end

    while p[0] != start[0] and p[1] != start[1]:
        path.append(p)
        p, dir = parents[(p, dir)]
    return path


def AStar(start, end):

    parents = {}

    open = [PrioNode(0, (start[0], start[1]), start[2])]
    closed = set()

    while True:
        v = heapq.heappop(open)
        if v.item == end:
            # found the end
            # do something
            return v.score + v.dist, find_path(parents, start, end)
        closed.add(v)
        neighs = neighbors(v)
        for n in neighs:
            if n not in closed:
                heapq.heappush(open, n)
                parents[(n.item, n.dir)] = (v.item, v.dir)


print(AStar(start, end))