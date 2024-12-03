from utils.readinput import read_input
import re


def parse_day03_input():
    day03_input = read_input('input/day03.txt')
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    enabler_pattern = r"do\(\)|don't\(\)"
    parsed_mul_instructions = [((int(mul.group(1)), int(mul.group(2))), mul.start()) for mul in re.finditer(mul_pattern, day03_input)]
    enabler_instructions = [(enabler.group(), enabler.start()) for enabler in re.finditer(enabler_pattern, day03_input)]
    parsed_enabler_instructions = [((-1, -1) if enabler[0] == "don't()" else (0, 0), enabler[1]) for enabler in enabler_instructions]
    parsed_instructions = sorted(parsed_mul_instructions + parsed_enabler_instructions, key=lambda x: x[1])
    instructions = [instruction[0] for instruction in parsed_instructions]
    return instructions


def solve_part_1(instructions):
    mul_instructions = [instruction for instruction in instructions if instruction != (0, 0) or instruction != (-1, -1)]
    return sum([x*y for x, y in mul_instructions])


def solve_part_2(instructions):
    enabled = True
    result = []
    for instruction in instructions:
        match instruction:
            case (0, 0):
                enabled = True
            case (-1, -1):
                enabled = False
            case _:
                if enabled:
                    result.append(instruction)

    return sum([x*y for x, y in result])


if __name__ == '__main__':
    parsed_input = parse_day03_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input)))
