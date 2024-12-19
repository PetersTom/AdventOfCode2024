from typing import Dict

filepath = "inputs/19.txt"
with open(filepath, "r") as f:
    lines = f.readlines()
towels = lines[0].strip().split(', ')
patterns = [l.strip() for l in lines[2:]]



memory: Dict[str, int] = {}
def can_be_made(pattern, towels):
    if len(pattern) == 0:
        return True
    if pattern in memory:
        return memory[pattern]

    constructable = 0
    for towel in towels:
        if towel == pattern[:len(towel)]:
            amount = can_be_made(pattern[len(towel):], towels)
            constructable += amount
    memory[pattern] = constructable
    print(f"pattern: {pattern}, constructable: {constructable}")
    return constructable

constructable = []
for p in patterns:
    constructable.append(can_be_made(p, towels))
print(sum(constructable))

