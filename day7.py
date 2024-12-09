filepath = "inputs/7a.txt"
with open(filepath, "r") as f:
    equations = [(int(l.split(":")[0]), [int(x) for x in l.split(":")[1].strip().split(" ")]) for l in f.readlines()]



def check_results(total, operands, current_value, index_in_operands):
    if index_in_operands >= len(operands):
        return False
    if current_value > total:
        return False
    new_addition_value = current_value + operands[index_in_operands]
    new_mult_value = current_value * operands[index_in_operands]
    new_concat_value = int(str(current_value) + str(operands[index_in_operands]))

    if (new_addition_value == total or new_mult_value == total or new_concat_value == total) and index_in_operands == len(operands) - 1:
        return True

    return (check_results(total, operands, new_addition_value, index_in_operands + 1)
            or check_results(total, operands, new_mult_value, index_in_operands + 1)
            or check_results(total, operands, new_concat_value, index_in_operands + 1))

total = 0
for eq in equations:
    if check_results(eq[0], eq[1], 0, 0):
        total += eq[0]
print(total)

