def combo(i, A, B, C):
    if 0 <= i <= 3:
        return i
    if i == 4:
        return A
    elif i == 5:
        return B
    elif i == 6:
        return C
    elif i == 7:
        raise ValueError("Illegal program")


def truncate(x):
    mask = (1 << 3) - 1  # the 3 least significant bits
    return x & mask

def run_program(A, program):
    B = 0
    C = 0
    output = []
    pointer = 0
    while pointer < len(program):
        instruction = program[pointer]
        operand = program[pointer + 1]
        if instruction == 0:
            A = A // (2**combo(operand, A, B, C))
        elif instruction == 1:
            B = B ^ operand
        elif instruction == 2:
            B = truncate(combo(operand, A, B, C) % 8)
        elif instruction == 3:
            if A == 0:
                pass
            else:
                pointer = operand
                continue
        elif instruction == 4:
            B = B ^ C  # ignores operand
        elif instruction == 5:
            output.append(combo(operand, A, B, C) % 8)
        elif instruction == 6:
            B = A // (2 ** combo(operand, A, B, C))
        elif instruction == 7:
            C = A // (2 ** combo(operand, A, B, C))
        pointer += 2
    return output

program = [2, 4, 1, 2, 7, 5, 0, 3, 1, 7, 4, 1, 5, 5, 3, 0]
ranges_to_check = [range(0, 8)]

found = False
while not found:
    new_ranges_to_check = []
    for r in ranges_to_check:
        for i in r:
            potential_output = run_program(i, program)
            if potential_output == program[-len(potential_output):]:
                if len(potential_output) == len(program):
                    # found solution
                    print(f"found it: {i}")
                    found = True
                    break
                # this is potential continuation
                new_ranges_to_check.append(range(i * 8, i * 8 + 8))
        if found:
            break
    ranges_to_check = new_ranges_to_check



