filepath = "inputs/13a.txt"
with open(filepath, "r") as f:
    input = ''.join([l for l in f.readlines()])
machines = input.split('\n\n')

machines = [[m.split('\n')[0][10:], m.split('\n')[1][10:], m.split('\n')[2][7:]] for m in machines]

machines = [
    [
        int(m[0].split(', ')[0][2:]),
        int(m[0].split(', ')[1][2:]),
        int(m[1].split(', ')[0][2:]),
        int(m[1].split(', ')[1][2:]),
        int(m[2].split(', ')[0][2:]),
        int(m[2].split(', ')[1][2:])
    ]
    for m in machines
]

def shortest_path(ax, ay, bx, by, px, py, cx, cy, pressA, pressB, memory):
    if cx == px and cy == py:
        return pressA * 3 + pressB
    if cx > px or cy > py:
        return float('inf')
    if (cx, cy, 'A') in memory:
        resultIfPressedA = memory[(cx, cy, 'A')]
    else:
        resultIfPressedA = shortest_path(ax, ay, bx, by, px, py, cx + ax, cy + ay, pressA + 1, pressB, memory)
        memory[(cx, cy, 'A')] = resultIfPressedA
    if (cx, cy, 'B') in memory:
        resultIfPressedB = memory[(cx, cy, 'B')]
    else:
        resultIfPressedB = shortest_path(ax, ay, bx, by, px, py, cx + bx, cy + by, pressA, pressB + 1, memory)
        memory[(cx, cy, 'B')] = resultIfPressedB

    return min(resultIfPressedA, resultIfPressedB)

import numpy as np
def solve_linear(ax, ay, bx, by, px, py):
    px += 10000000000000
    py += 10000000000000
    eqs = np.array([[ax, bx], [ay, by]])
    res = np.array([px, py])
    x = np.linalg.solve(eqs, res)
    x = [int(round(x[0])), int(round(x[1]))]
    if ax * x[0] + bx * x[1] == px and ay * x[0] + by * x[1] == py:
        return x[0] * 3 + x[1]
    else:
        return float('inf')

total = 0
for m in machines:
    cost = solve_linear(*m)
    if cost != float('inf'):
        total += cost
    print(cost)
print(total)



