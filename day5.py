from itertools import permutations

from Tools.scripts.update_file import updating_file_with_tmpfile

filepath = "inputs/5a.txt"
with open(filepath, "r") as f:
    lines = [l.strip() for l in f.readlines()]

rules = []
updates = []
for i in lines:
    if "|" in i:
        rules.append(i)
    elif "," in i:
        updates.append(i)


rules = [x.split("|") for x in rules]
rules = [(int(x[0]), int(x[1])) for x in rules]
updates = [[int(x) for x in update.split(",")] for update in updates]


def in_order(rules, update):
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True


def is_root(rules, update, i):
    for rule in rules:
        if rule[1] == i:
            if rule[0] in update:
                return False
    return True


def get_roots(rules, update):
    roots = []
    for i in update:
        if is_root(rules, update, i):
            roots.append(i)
    if len(roots) == 0:
        raise ValueError("Root not found")
    return roots



def get_children(rules, update, i):
    children = []
    for rule in rules:
        if rule[0] == i:
            if rule[1] in update:
                children.append(rule[1])
    return children



def visit(rules, update, n, permanent, temporary, L):
    if n in permanent:
        return
    if n in temporary:
        raise ValueError("At least one cycle")

    temporary.append(n)
    for child in get_children(rules, update, n):
        visit(rules, update, child, permanent, temporary, L)
    permanent.append(n)
    L.insert(0, n)


def correct_order(rules, update):
    L = []
    temporary, permanent = [], []
    while len(permanent) != len(update):
        unmarked = None
        for node in update:
            if node not in temporary and node not in permanent:
                unmarked = node
                break
        visit(rules, update, unmarked, permanent, temporary, L)
    return L



total = 0
for update in updates:
    if not in_order(rules, update):
        perm = correct_order(rules, update)
        middle = perm[int(len(perm) / 2)]
        total += middle
print(total)
