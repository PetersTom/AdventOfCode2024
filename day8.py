from itertools import combinations

filepath = "inputs/8a.txt"
with open(filepath, "r") as f:
    map = [[x for x in l.strip()] for l in f.readlines()]

antennas = {}
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] != ".":
            if map[y][x] in antennas:
                antennas[map[y][x]].append((y, x))
            else:
                antennas[map[y][x]] = [(y, x)]

anti_nodes = {}
for name, positions in antennas.items():
    anti_nodes[name] = set()
    for pair in combinations(positions, 2):
        dify = pair[0][0] - pair[1][0]
        difx = pair[0][1] - pair[1][1]
        pos = pair[0]
        while 0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0]):
            anti_nodes[name].add(pos)
            pos = (pos[0] + dify, pos[1] + difx)
        pos = pair[0]
        while 0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0]):
            anti_nodes[name].add(pos)
            pos = (pos[0] - dify, pos[1] - difx)

total_nodes = set()
for name, nodes in anti_nodes.items():
    for n in nodes:
        total_nodes.add(n)
print(len(total_nodes))
print(sorted(list(total_nodes)))