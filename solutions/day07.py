from utils.readinput import read_input_as_list
from dataclasses import dataclass
from itertools import product


@dataclass
class CalibrationEquation:
    result: int
    numbers: [int]
    operators: [[str]]

    def update_operators(self, operators):
        self.operators = [list(op) for op in product(operators, repeat=len(self.numbers) - 1)]

    def evaluate(self) -> int:
        for operator_list in self.operators:
            equation = [item for pair in zip(self.numbers, operator_list) for item in pair] + [self.numbers[-1]]
            actual_result = int(equation[0])
            for i in range(1, len(equation), 2):
                op = equation[i]
                num = int(equation[i + 1])
                actual_result = apply_operator(actual_result, op, num)
            if actual_result == self.result:
                return self.result
        else:
            return 0


def apply_operator(a, op, b):
    if op == "||":
        return int(str(a) + str(b))
    elif op == "+":
        return a + b
    elif op == "*":
        return a * b
    else:
        raise ValueError(f"Unsupported operator: {op}")


def parse_day07_input():
    #day07_input = read_input_as_list('input/day07_sample.txt')
    day07_input = read_input_as_list('../input/day07.txt')
    equations = []
    for line in day07_input:
        result_part, numbers_part = line.split(':')
        result = int(result_part.strip())
        numbers = list(map(int, numbers_part.strip().split()))
        equation = CalibrationEquation(result=result, numbers=numbers, operators=[])
        equations.append(equation)
    return equations


def solve_part_1(equations):
    operators = ['+', '*']
    [equation.update_operators(operators) for equation in equations]
    calibration_results = [equation.evaluate() for equation in equations]
    return sum(calibration_results)


def solve_part_2(equations):
    operators = ['+', '*', '||']
    [equation.update_operators(operators) for equation in equations]
    calibration_results = [equation.evaluate() for equation in equations]
    return sum(calibration_results)


if __name__ == '__main__':
    parsed_equations = parse_day07_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_equations)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_equations)))
