filepath = "inputs/2a.txt"
with open(filepath, "r") as f:
    lines = f.readlines()
lines = [l.split() for l in lines]
lines = [[int(x) for x in l] for l in lines]

def is_safe(line):
    if (sorted(line) != line and list(reversed(sorted(line))) != line) or len(line) != len(set(line)):
        return False
    for i in range(len(line) - 1):
        if 1 > abs(line[i] - line[i+1]) or 3 < abs(line[i] - line[i+1]):
            return False
    return True

safe = 0
for line in lines:
    if is_safe(line):
        safe += 1
    else:
        for i in range(len(line)):
            changed_line = [x for x in line]
            changed_line.pop(i)
            if is_safe(changed_line):
                safe += 1
                break

print(safe)
