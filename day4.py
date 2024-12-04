filepath = "inputs/4a.txt"
with open(filepath, "r") as f:
    lines = [[x for x in l.strip()] for l in f.readlines()]

for line in lines:
    if "\n" in line:
        line.remove("\n")
        line.remove("\n")

# word = {"X": "M", "M":"A", "A": "S"}
# total = 0
# for y in range(len(lines)):
#     for x in range(len(lines[0])):
#         if lines[y][x] == "X":
#             for dirx, diry in [(-1, -1), (0, -1), (1, -1), (1, 0), (-1, 0), (0, 1), (1, 1), (-1, 1)]:
#                 last = "X"
#                 continuing = True
#                 testx = x
#                 testy = y
#                 while continuing:
#                     testx += dirx
#                     testy += diry
#                     if 0 <= testx < len(lines[0]) and 0 <= testy < len(lines):
#                         if lines[testy][testx] == word[last]:
#                             last = word[last]
#                             if last == "S":
#                                 total += 1
#                                 break
#                         else:
#                             continuing = False
#                     else:
#                         break

def check_X(lines, y, x):
    if not(0 < x < len(lines[0]) - 1 and 0 < y < len(lines) - 1):
        return False
    if ((lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S") or (lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M")) and ((lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S") or (lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M")):
        return True
    return False

total = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "A":
            if check_X(lines, y, x):
                total += 1

print(total)

