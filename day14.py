filepath = "inputs/14a.txt"
with open(filepath, "r") as f:
    robots = [l.strip().split(' ') for l in f.readlines()]

robots = [[int(r[0][2:].split(',')[0]),
           int(r[0][2:].split(',')[1]),
           int(r[1][2:].split(',')[0]),
           int(r[1][2:].split(',')[1]),
           ] for r in robots]

positions = [(r[0], r[1]) for r in robots]
velocities = [(r[2], r[3]) for r in robots]

width = 101
height = 103
# width = 11
# height = 7

import zlib
def compressed_size(positions):
    bitstring = ""
    for y in range(height):
        for x in range(width):
            if (x, y) in positions:
                bitstring += "1"
            else:
                bitstring += "0"
    # print(len(bitstring))
    compressed = zlib.compress(bitstring.encode())
    # print(compressed)
    return len(compressed)


def print_robots(positions):
    for y in range(height):
        for x in range(width):
            if (x, y) in positions:
                print(".", end="")
            else:
                print("#", end="")
        print()
    print("\n\n\n")


lowest_randomness = 100000000000000000000
best_positions = []

for s in range(100000):
    for i in range(len(positions)):
        p = positions[i]
        v = velocities[i]
        positions[i] = ((p[0] + v[0]) % width, (p[1] + v[1]) % height)
    randomness = compressed_size(positions)
    if randomness < lowest_randomness:
        lowest_randomness = randomness
        best_positions = [p for p in positions]
        print_robots(best_positions)



# top_left = len([p for p in positions if p[0] < width // 2 and p[1] < height // 2])
# top_right = len([p for p in positions if p[0] > width / 2 and p[1] < height // 2])
# bot_left = len([p for p in positions if p[0] < width // 2 and p[1] > height / 2])
# bot_right = len([p for p in positions if p[0] > width / 2 and p[1] > height / 2])
# print(top_left * top_right * bot_right * bot_left)