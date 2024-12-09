filepath = "inputs/9a.txt"
import re
with open(filepath, "r") as f:
    l = f.read()

# l = "1564215642315"

files = []
index = 0
file = True
for c in l:
    if file:
        files += [str(index)] * int(c)
        index += 1
        file = False
    else:
        files += ["."] * int(c)
        file = True


def get_last(l, condition):
    for i, x in enumerate(reversed(l)):
        if condition(x):
            return len(l) - 1 - i

def first_available_spot(files, end_of_search, required_length):
    current_start = 0
    dots = False
    for i in range(end_of_search + 1):
        if files[i] == ".":
            if not dots:
                current_start = i
                dots = True
        else:
            if dots:
                dots = False
                length = i - current_start
                if length >= required_length:
                    return current_start
    return -1


def swap(files, first_start, second_start, item):
    while second_start < len(files) and files[second_start] == item:
        files[first_start], files[second_start] = files[second_start], files[first_start]
        first_start += 1
        second_start += 1
    return files

print(files)
for index in range(int(len(l) / 2), -1, -1):
    last_index = get_last(files, lambda b: b == str(index))
    first_index = last_index
    while first_index >= 0 and files[first_index] == files[last_index]:
        first_index -= 1
    first_index += 1
    amount = last_index - first_index + 1
    available_spot = first_available_spot(files, first_index, amount)
    if available_spot == -1:
        continue
    files = swap(files, available_spot, first_index, files[first_index])
    # print(files)






# while not re.match(r"^[0-9]+\.+$", "".join(files)):
#     to_place_at = files.index(".")
#     to_place_from = len(files) - 1 - get_last(files, lambda b: b.isdigit())
#
#     files[to_place_at], files[to_place_from] = files[to_place_from], files[to_place_at]

total = 0
for i, c in enumerate(files):
    if c.isdigit():
        total += i * int(c)
print("total: " + str(total))