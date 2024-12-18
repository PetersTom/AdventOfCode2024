import heapq

filepath = "inputs/18.txt"
with open(filepath, "r") as f:
    falling = [l.split(',') for l in f.readlines()]
    falling = [(int(x[0]), int(x[1].strip())) for x in falling]

gridsize = 71

def dijkstra_neighbors(score, v, obstructed):
    for difx, dify in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newx, newy = v[0] + difx, v[1] + dify
        if 0 <= newx < gridsize and 0 <= newy < gridsize and (newx, newy) not in obstructed:
            yield score + 1, (newx, newy)


def dijkstra(start, end, obstructed):

    parents = {}
    dist_per_node = {}

    current = (0, start)
    queue = [current]
    while len(queue) > 0:
        score, v = heapq.heappop(queue)
        if (v[0], v[1]) == end:
            return score#, find_paths_dijkstra(parents, start, end, v[2])
        for s, n in dijkstra_neighbors(score, v, obstructed):
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
    return -1

start = (0, 0)
end = (70, 70)
def binary_search(low, high):


    mid =  (high + low) // 2

    result = dijkstra(start, end, falling[:mid])
    resultprev = dijkstra(start, end, falling[:mid-1])
    if result == -1 and resultprev != -1:
        return mid
    elif result == -1:
        return binary_search(low, mid - 1)
    else:
        return binary_search(mid + 1, high)

index = binary_search(0,len(falling))
print(falling[index-1])
