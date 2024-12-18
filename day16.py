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


def dijkstra_neighbors(score, node):
    neighs = []
    y, x, dir = node
    neighs.append((score + 1000, (y, x, (dir + 1) % 4)))
    neighs.append((score + 1000, (y, x, (dir - 1) % 4)))
    dify, difx = [(-1, 0), (0, 1), (1, 0), (0, -1)][dir]
    newy, newx = y + dify, x + difx
    if 0 <= newy < len(grid) and 0 <= newx < len(grid[y]):
        if grid[newy][newx] == ".":
            neighs.append((score + 1, (newy, newx, dir)))
    return neighs


def find_paths_dijkstra(parents, start, end, end_dir):
    p = (*end, end_dir)

    part_of_a_path = []
    front = {p}

    while not (len(front) == 1 and next(iter(front)) == start):
        next_front = set()
        for p in front:
            part_of_a_path.append(p)
            parents_of_p = parents[p]
            for ps in parents_of_p:
                next_front.add(ps)
        front = next_front

    return part_of_a_path


def dijkstra(start, end):

    parents = {}
    dist_per_node = {}

    current = (0, start)
    queue = [current]
    while len(queue) > 0:
        score, v = heapq.heappop(queue)
        if (v[0], v[1]) == end:
            return score, find_paths_dijkstra(parents, start, end, v[2])
        neighs = dijkstra_neighbors(score, v)
        for s, n in neighs:
            if n not in dist_per_node.keys() or dist_per_node[n] >= s:
                if n not in dist_per_node:
                    heapq.heappush(queue, (s, n))
                elif dist_per_node[n] > s:
                    heapq.heappush(queue, (s, n))

                if n not in dist_per_node.keys() or dist_per_node[n] == s:
                    if n in parents:
                        parents[n].append(v)
                    else:
                        parents[n] = [v]
                elif dist_per_node[n] > s:
                    assert n in parents
                    parents[n] = [v]
                dist_per_node[n] = s


best_scoreDijkstra, nodes_on_path = dijkstra(start, end)

nodes_on_path = set([(x[0], x[1]) for x in nodes_on_path])
print(len(nodes_on_path))
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            print("#", end='')
        elif grid[y][x] == ".":
            if (y, x) in nodes_on_path:
                print("O", end='')
            else:
                print(".", end='')
    print()

print(best_scoreDijkstra, len(nodes_on_path))
