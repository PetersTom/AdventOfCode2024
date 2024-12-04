import re

filepath = "inputs/3a.txt"
with open(filepath, "r") as f:
    lines = f.readlines()

pattern = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)")
muls = []
for line in lines:
    muls += re.findall(pattern, line)

total = 0
processing = True
for mul in muls:
    if mul == "do()":
        processing = True
    elif mul == "don't()":
        processing = False
    elif processing:
        ints = [int(x) for x in mul[4:-1].split(",")]
        total += ints[0] * ints[1]
print(total)

