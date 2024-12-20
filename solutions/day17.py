#REGISTER_A = 2024
#REGISTER_B = 0
#REGISTER_C = 0
#PROGRAM = [0, 3, 5, 4, 3, 0]

REGISTER_A = 61657405
REGISTER_B = 0
REGISTER_C = 0
PROGRAM = [2, 4, 1, 2, 7, 5, 4, 3, 0, 3, 1, 7, 5, 5, 3, 0]


def lookup_combo_operand(operand) -> int:
    match operand:
        case 4:
            return REGISTER_A
        case 5:
            return REGISTER_B
        case 6:
            return REGISTER_C
        case 7:
            raise ValueError(f"Not valid program (reserved operand): {operand}")
        case _:
            return operand


def adv(operand):
    global REGISTER_A
    combo_operand = lookup_combo_operand(operand)
    REGISTER_A = REGISTER_A // (2**combo_operand)


def bdv(operand):
    global REGISTER_A, REGISTER_B
    combo_operand = lookup_combo_operand(operand)
    REGISTER_B = REGISTER_A // (2**combo_operand)


def cdv(operand):
    global REGISTER_A, REGISTER_C
    combo_operand = lookup_combo_operand(operand)
    REGISTER_C = REGISTER_A // (2**combo_operand)


def bxl(operand):
    global REGISTER_B
    REGISTER_B = REGISTER_B ^ operand


def bst(operand):
    global REGISTER_B
    combo_operand = lookup_combo_operand(operand)
    REGISTER_B = combo_operand % 8


def jnz(operand, index) -> int:
    global REGISTER_A
    if REGISTER_A == 0:
        return index+2
    return operand


def bxc(_):
    global REGISTER_B, REGISTER_C
    REGISTER_B = REGISTER_B ^ REGISTER_C


def out(operand) -> int:
    combo_operand = lookup_combo_operand(operand)
    return combo_operand % 8


def run_program(program) -> [int]:
    output = []
    index = 0
    while index < len(program):

        if index + 1 >= len(program):
            break

        op_code = program[index]
        operand = program[index + 1]
        index += 2

        match op_code:
            case 0:
                adv(operand)
            case 1:
                bxl(operand)
            case 2:
                bst(operand)
            case 3:
                index = jnz(operand, index)
                continue
            case 4:
                bxc(operand)
            case 5:
                output.append(out(operand))
            case 6:
                bdv(operand)
            case 7:
                cdv(operand)
            case _:
                raise ValueError(f"Unknown op_code: {op_code}")
    return output


def reverse_eng(program) -> int:
    prev = {0}
    for value in program[::-1]:
        new_prev = set()
        for prev_a in prev:
            for last in range(0, 8):
                if not prev_a and not last:
                    continue
                a = prev_a * 8 + last
                b = a % 8
                b = b ^ 2
                c = a // (2 ** b)
                b = b ^ 7
                b = b ^ c
                if b % 8 == value:
                    new_prev.add(a)
        if not new_prev:
            raise ValueError(f"Unknown state: {new_prev}")
        prev = new_prev
    return min(prev)


def solve_part_1():
    program = PROGRAM.copy()
    output = run_program(program)
    return ",".join(str(instruction) for instruction in output)


def solve_part_2():
    program = PROGRAM.copy()
    return reverse_eng(program)


if __name__ == '__main__':
    print("Answer to part 1: {}".format(solve_part_1()))
    print("Answer to part 2: {}".format(solve_part_2()))
