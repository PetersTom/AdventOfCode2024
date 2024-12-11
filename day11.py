filepath = "inputs/11a.txt"
with open(filepath, "r") as f:
    stones = [int(x) for x in f.read().strip().split(" ")]

memory = {}


def apply_step(x):
    if x == 0:
        return (1,)
    elif len(str(x)) % 2 == 0:
        mid = len(str(x)) // 2
        first = int(str(x)[:mid])
        second = int(str(x)[mid:])
        return first, second
    else:
        return (x * 2024,)


def number_of_stones_after_blinks(x, iterations_left):
    if iterations_left == 0:
        return 1
    if (x, iterations_left) in memory:
        return memory[(x, iterations_left)]
    total = 0
    for v in apply_step(x):
        total += number_of_stones_after_blinks(v, iterations_left - 1)
    memory[(x, iterations_left)] = total
    return total


print(stones)
total = 0
for v in stones:
    total += number_of_stones_after_blinks(v, 75)
print(total)
