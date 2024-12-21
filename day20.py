import heapq

filepath = "inputs/20.txt"
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
            start = (y, x)
            grid[y][x] = "."

def dijkstra_neighbors(score, v, remove_blocked = True):
    for difx, dify in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newx, newy = v[1] + difx, v[0] + dify
        if  0 <= newy < len(grid) and 0 <= newx < len(grid[newy]) and (grid[newy][newx] == "." or not remove_blocked):
            yield score + 1, (newy, newx)


def dijkstra(start, end):

    dist_per_node = {}

    current = (0, start)
    queue = [current]
    while len(queue) > 0:
        score, v = heapq.heappop(queue)
        if (v[0], v[1]) == end:
            return score, dist_per_node
        for s, n in dijkstra_neighbors(score, v):
            if n not in dist_per_node.keys() or dist_per_node[n] >= s:
                if n not in dist_per_node:
                    heapq.heappush(queue, (s, n))
                elif dist_per_node[n] > s:
                    heapq.heappush(queue, (s, n))
                dist_per_node[n] = s
    return -1


def dist(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


original_length, dist_per_node = dijkstra(start, end)

from tqdm import tqdm
import itertools
saves = {}

max_it = len(grid) * len(grid[0])
for y1, x1 in tqdm(itertools.product(range(len(grid)), range(len(grid[0]))), total=max_it):
    if grid[y1][x1] != ".":
        continue
    # check all path fields within a certain distance
    other_points = [(y, x) for y, x in itertools.product(range(len(grid)), range(len(grid[0]))) if (dist(y1, x1, y, x) <= 20 and grid[y][x] == ".")]
    for y2, x2 in other_points:
        p1p2dist = dist(y1, x1, y2, x2)
        # potential cheat
        dist1 = dist_per_node[(y1, x1)]
        dist2 = dist_per_node[(y2, x2)]
        if dist1 <= dist2:
            continue
        # dist1 is further from the start than dist2, so (y1, x1) is the target, (y2, x2) is the start
        dist1_with_cheat = dist2 + p1p2dist
        save = dist1 - dist1_with_cheat
        if save <= 0:
            continue
        if save in saves:
            saves[save] += 1
        else:
            saves[save] = 1

saves = {k: v for k, v in saves.items() if k >= 100}
a = sorted(saves.items())
c = [x[1] for x in a]
print(sum(c))


