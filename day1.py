filepath = "inputs/1a.txt"
with open(filepath, "r") as f:
    lines = f.readlines()
lines = [l.split() for l in lines]
lines = [[int(l[0]), int(l[1])] for l in lines]
list1, list2 = [], []
for l in lines:
    list1.append(l[0])
    list2.append(l[1])

# total = 0
# for i in range(len(list1)):
#     total += abs(list1[i] - list2[i])

total = 0
for i in list1:
    total += i * list2.count(i)
print(total)