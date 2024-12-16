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


def print_robots(positions, score, iteration, file_location = "test.txt"):
    with open(file_location, "w") as f:
        print(score, iteration, file=f)
        for y in range(height):
            for x in range(width):
                if (x, y) in positions:
                    print("#", end="", file=f)
                else:
                    print(" ", end="", file=f)
            print(file=f)
        for _ in range(3):
            for _ in range(width):
                print("-", end="", file=f)
            print(file=f)



def average_surround(positions):
    total_surround = 0
    for x, y in positions:
        for difx, dify in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            newx = x + difx
            newy = y + dify
            if (newx, newy) in positions:
                total_surround += 1
    return total_surround / len(positions)


highest_surround = 0
highest_surround_positions = []

from tqdm import tqdm
for s in tqdm(range(8006)):
    for i in range(len(positions)):
        p = positions[i]
        v = velocities[i]
        positions[i] = ((p[0] + v[0]) % width, (p[1] + v[1]) % height)
    # a = average_surround(positions)
    # if a > highest_surround:
    #     highest_surround = a
    #     highest_surround_positions = [p for p in positions]
    # print_robots(positions, highest_surround, s)
print_robots(positions, 0, 0)



# top_left = len([p for p in positions if p[0] < width // 2 and p[1] < height // 2])
# top_right = len([p for p in positions if p[0] > width / 2 and p[1] < height // 2])
# bot_left = len([p for p in positions if p[0] < width // 2 and p[1] > height / 2])
# bot_right = len([p for p in positions if p[0] > width / 2 and p[1] > height / 2])
# print(top_left * top_right * bot_right * bot_left)